#!/usr/bin/env python3
"""Extract public Anthropic page implementation facts into the style repo.

The output is evidence: DOM snapshots, linked CSS URLs, inline style summaries, headings,
class-token frequencies, and CSS token candidates. Runtime components must adapt these facts,
not copy Anthropic production code as a dependency.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "styles" / "anthropic-claude"
OUT = STYLE / "evidence" / "web" / "original-code"
CSS_DIR = STYLE / "evidence" / "web" / "css"
PAGES = {
    "claude-product": "https://www.anthropic.com/claude",
    "pricing-product": "https://www.anthropic.com/pricing?subjects=claude&type=product",
    "claude-api": "https://www.anthropic.com/claude/api",
}

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 HermesDesignStyleExtractor/1.0"


def fetch(url: str, timeout=40) -> str:
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
    with urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def dump_dom_chromium(url: str) -> str | None:
    chrome = subprocess.run("command -v chromium || command -v google-chrome", shell=True, capture_output=True, text=True).stdout.strip()
    if not chrome:
        return None
    try:
        res = subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--dump-dom", url], capture_output=True, text=True, timeout=70)
        if res.returncode == 0 and len(res.stdout) > 1000:
            return res.stdout
    except Exception:
        return None
    return None


def css_candidates(text: str) -> dict:
    colors = Counter(re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)", text))
    radii = Counter(re.findall(r"border-radius\s*:\s*([^;}{]+)", text))
    fonts = Counter(re.findall(r"font-family\s*:\s*([^;}{]+)", text))
    shadows = Counter(re.findall(r"box-shadow\s*:\s*([^;}{]+)", text))
    vars_ = Counter(re.findall(r"--[a-zA-Z0-9_-]+\s*:\s*([^;}{]+)", text))
    return {
        "colors": colors.most_common(50),
        "border_radius": radii.most_common(30),
        "font_family": fonts.most_common(20),
        "box_shadow": shadows.most_common(20),
        "css_custom_values": vars_.most_common(50),
    }


def summarize_page(slug: str, url: str, html: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "noscript"]):
        tag.decompose()
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    headings = []
    for h in soup.find_all(re.compile("^h[1-4]$"))[:120]:
        txt = h.get_text(" ", strip=True)
        if txt:
            headings.append({"tag": h.name, "text": txt[:240], "classes": h.get("class", [])})
    buttons_links = []
    for el in soup.find_all(["a", "button"])[:240]:
        txt = el.get_text(" ", strip=True)
        if txt:
            buttons_links.append({"tag": el.name, "text": txt[:120], "href": el.get("href"), "classes": el.get("class", [])})
    classes = Counter(c for el in soup.find_all(True) for c in (el.get("class") or []))
    css_links = [urljoin(url, l.get("href")) for l in soup.find_all("link", rel=lambda v: v and "stylesheet" in v) if l.get("href")]
    inline_styles = "\n".join(s.get_text("\n", strip=False) for s in soup.find_all("style"))
    text = soup.get_text("\n", strip=True)
    words = Counter(re.findall(r"[A-Za-z][A-Za-z0-9+.-]{2,}", text.lower()))
    return {
        "slug": slug,
        "url": url,
        "title": title,
        "headings": headings,
        "actions": buttons_links,
        "class_frequency": classes.most_common(100),
        "css_links": css_links,
        "inline_css_candidates": css_candidates(inline_styles),
        "text_terms": words.most_common(100),
        "html_bytes": len(html.encode("utf-8")),
        "body_text_chars": len(text),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    CSS_DIR.mkdir(parents=True, exist_ok=True)
    all_pages = []
    css_seen = {}
    for slug, url in PAGES.items():
        page_dir = OUT / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        html = dump_dom_chromium(url) or fetch(url)
        (page_dir / "dom.html").write_text(html, encoding="utf-8")
        summary = summarize_page(slug, url, html)
        for css_url in summary["css_links"][:20]:
            if css_url in css_seen:
                continue
            try:
                req = Request(css_url, headers={"User-Agent": UA})
                data = urlopen(req, timeout=30).read().decode("utf-8", "replace")
                name = re.sub(r"[^a-zA-Z0-9_.-]+", "-", urlparse(css_url).path.strip("/") or "style.css")[-120:]
                css_path = CSS_DIR / name
                css_path.write_text(data, encoding="utf-8")
                css_seen[css_url] = str(css_path.relative_to(STYLE))
            except Exception as e:
                css_seen[css_url] = f"ERROR:{type(e).__name__}:{e}"
        summary["downloaded_css"] = {u: css_seen.get(u) for u in summary["css_links"]}
        (page_dir / "source-facts.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        # compact markdown report
        md = [f"# Public Code Facts — {slug}", "", f"Source: {url}", "", f"Title: {summary['title']}", "", "## Headings", ""]
        md += [f"- `{h['tag']}` {h['text']}" for h in summary["headings"][:40]]
        md += ["", "## Actions", ""]
        md += [f"- `{a['tag']}` {a['text']} → {a.get('href') or ''}" for a in summary["actions"][:60]]
        md += ["", "## Top class tokens", ""]
        md += [f"- `{k}` × {v}" for k, v in summary["class_frequency"][:40]]
        md += ["", "## CSS token candidates", "", "```json", json.dumps(summary["inline_css_candidates"], indent=2, ensure_ascii=False)[:6000], "```", "", "Policy: evidence only; do not copy production code as runtime dependency."]
        (page_dir / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        all_pages.append(summary)
    # aggregate CSS candidates from downloaded CSS
    css_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in CSS_DIR.glob("*.css"))
    agg = {"pages": [{"slug": p["slug"], "url": p["url"], "title": p["title"], "css_links": p["css_links"]} for p in all_pages], "css_candidates": css_candidates(css_text), "css_files": sorted(str(p.relative_to(STYLE)) for p in CSS_DIR.glob("*.css"))}
    (OUT / "public-code-index.json").write_text(json.dumps(agg, indent=2, ensure_ascii=False), encoding="utf-8")
    (OUT / "README.md").write_text("# Public Anthropic Code Evidence\n\n" + "\n".join(f"- `{p['slug']}` — {p['url']}" for p in all_pages) + "\n\nEvidence only; runtime recipes must be original/adapted.\n", encoding="utf-8")
    print(json.dumps({"pages": len(all_pages), "css_files": len(agg["css_files"]), "out": str(OUT)}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
