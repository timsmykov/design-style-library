#!/usr/bin/env python3
"""Build a source map + component evidence extraction from the local Anthropic Mobbin corpus.

This is not a scraper for proprietary app code. It turns local Mobbin screenshot evidence
into deterministic repo artifacts: source URLs, image facts, OCR text, component matches,
and normalized implementation recipes that runtime agents can use.
"""
from __future__ import annotations

import csv
import json
import math
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "styles" / "anthropic-claude"
MOBBIN = STYLE / "evidence" / "mobbin"
OUT = STYLE / "evidence" / "source-map"
EXTRACTED = STYLE / "components" / "extracted" / "from-mobbin-screenshots"

COMPONENT_RULES = [
    ("auth-onboarding", ["login", "sign up", "signup", "continue with google", "phone", "verification", "verify", "onboarding", "welcome", "account"]),
    ("pricing-plan-cards", ["free", "pro", "max", "team", "plan", "pricing", "upgrade", "subscribe", "subscription", "$", "billing"]),
    ("settings-preferences", ["settings", "profile", "preferences", "billing", "account", "customize", "style", "manage"]),
    ("artifact-workbench-panel", ["artifact", "preview", "code", "file", "terminal", "editor", "project", "branch", "repository", "claude code"]),
    ("composer-command-card", ["ask claude", "message claude", "new chat", "attach", "search", "write", "prompt", "composer"]),
    ("model-comparison-figure", ["opus", "sonnet", "haiku", "model", "context", "token", "api", "rate", "latency"]),
    ("data-viz-figure-card", ["chart", "graph", "visualize", "axis", "trend", "data", "table", "analysis"]),
    ("docs-help-layout", ["docs", "documentation", "api", "help", "release", "support", "guide", "learn"]),
    ("feature-tile-grid", ["feature", "product", "coding", "agents", "productivity", "customer support", "use case", "learn more"]),
    ("editorial-hero-section", ["hero", "claude", "meet", "frontier", "ai assistant", "build", "research"]),
    ("app-shell-sidebar", ["chats", "projects", "recents", "artifacts", "sidebar", "home", "claude"]),
]

STOP = set("the and for with you your are this that from into claude anthropic web screen section flow onboarding".split())


def load_batch_metadata() -> dict[str, dict[str, Any]]:
    by_path: dict[str, dict[str, Any]] = {}
    for f in sorted((MOBBIN / "_batches").glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        for key in ("copied", "skipped"):
            items = data.get(key, []) or []
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                local = item.get("local_path")
                if local:
                    rec = dict(item)
                    rec["batch_file"] = str(f.relative_to(STYLE))
                    rec["batch_bucket"] = key
                    by_path[local] = rec
        for flow in data.get("flows", []) or []:
            for s in flow.get("screens", []) or []:
                local = s.get("local_path")
                if local:
                    rec = dict(s)
                    rec["flow_name"] = flow.get("name")
                    rec["flow_screen_count"] = flow.get("screen_count")
                    rec["batch_file"] = str(f.relative_to(STYLE))
                    rec["batch_bucket"] = "flows"
                    by_path[local] = rec
    return by_path


def palette(path: Path, n=6) -> list[str]:
    im = Image.open(path).convert("RGB")
    im.thumbnail((160, 160))
    colors = im.quantize(colors=n, method=2).convert("RGB").getcolors(160 * 160)
    colors = sorted(colors or [], reverse=True)
    return ["#%02x%02x%02x" % rgb for _, rgb in colors[:n]]


def image_stats(path: Path) -> dict[str, Any]:
    im = Image.open(path).convert("RGB")
    w, h = im.size
    small = im.resize((max(1, min(80, w)), max(1, min(80, h))))
    px = list(small.getdata())  # Pillow<14 compatibility
    lightness = mean((r + g + b) / (3 * 255) for r, g, b in px)
    # crude edge/detail density using luminance deltas
    edge = 0
    sw, sh = small.size
    lum = [sum(p) / 3 for p in px]
    for y in range(sh):
        for x in range(sw - 1):
            if abs(lum[y * sw + x] - lum[y * sw + x + 1]) > 28:
                edge += 1
    density = edge / max(1, sw * sh)
    return {"width": w, "height": h, "aspect_ratio": round(w / h, 4), "lightness": round(lightness, 4), "edge_density": round(density, 4), "palette": palette(path)}


def ocr(path: Path) -> str:
    try:
        res = subprocess.run(
            ["tesseract", str(path), "stdout", "--psm", "6", "-l", "eng"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=25,
        )
        text = res.stdout if res.returncode == 0 else ""
    except Exception:
        text = ""
    text = re.sub(r"\s+", " ", text).strip()
    return text[:5000]


def classify(rel: str, text: str, meta: dict[str, Any]) -> tuple[str, list[str]]:
    hay = " ".join([rel, text, json.dumps(meta, ensure_ascii=False)]).lower()
    flow_name = str(meta.get("flow_name") or meta.get("name") or "").lower()

    # Flow-level intent is usually more reliable than OCR noise.
    if "subscrib" in flow_name or "upgrading" in flow_name or "upgrade" in hay:
        return "pricing-plan-cards", [f"flow:{flow_name or 'upgrade/subscription'}"]
    if "settings" in flow_name:
        return "settings-preferences", ["flow:settings"]
    if "logging" in flow_name or "login" in flow_name:
        return "auth-onboarding", [f"flow:{flow_name}"]

    # Hard source lanes.
    if "claude-code" in rel or "terminal" in hay or "repository" in hay or "file explorer" in hay:
        return "artifact-workbench-panel", ["source:claude-code/workbench"]

    # High-confidence visual/text signatures.
    if any(k in hay for k in ["plans that grow", "free pro max", "choose your plan", "billed", "subscribe", "subscription", "upgrade plan"]):
        return "pricing-plan-cards", ["text:pricing/plan"]
    if any(k in hay for k in ["verify your phone", "create your account", "continue with google", "log in", "sign up", "verification"]):
        return "auth-onboarding", ["text:auth/verification"]
    if any(k in hay for k in ["settings", "profile", "customize style", "billing", "preferences"]):
        return "settings-preferences", ["text:settings"]
    if any(k in hay for k in ["artifact", "preview", "code", "editor", "project"]):
        return "artifact-workbench-panel", ["text:artifact/workbench"]
    if any(k in hay for k in ["opus", "sonnet", "haiku", "model comparison", "model card", "token"]):
        return "model-comparison-figure", ["text:model/comparison"]
    if any(k in hay for k in ["chart", "graph", "axis", "data visualization", "trend"]):
        return "data-viz-figure-card", ["text:data-viz"]
    if any(k in hay for k in ["docs", "documentation", "api docs", "release notes", "help center", "support"]):
        return "docs-help-layout", ["text:docs/help"]
    if any(k in hay for k in ["meet claude", "think fast", "frontier", "hero"]):
        return "editorial-hero-section", ["text:hero/editorial"]

    if "/sections/" in rel:
        return "feature-tile-grid", ["section fallback"]
    if "/flows/" in rel:
        return "auth-onboarding", [f"flow fallback:{flow_name or 'unknown'}"]
    if "composer" in hay or "ask claude" in hay or "message claude" in hay:
        return "composer-command-card", ["screen:composer"]
    return "app-shell-sidebar", ["screen fallback"]


def words(text: str) -> list[str]:
    toks = re.findall(r"[A-Za-z][A-Za-z0-9+.-]{2,}", text.lower())
    return [t for t in toks if t not in STOP and len(t) < 28]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    meta_by_path = load_batch_metadata()
    records = []
    images = sorted(MOBBIN.rglob("*.webp"))
    for i, path in enumerate(images, 1):
        rel_style = str(path.relative_to(STYLE))
        meta = meta_by_path.get(rel_style, {})
        text = ocr(path)
        stats = image_stats(path)
        component, evidence = classify(rel_style, text, meta)
        source_type = "flow_screen" if "/flows/" in rel_style else "section" if "/sections/" in rel_style else "screen"
        rec = {
            "index": i,
            "style_id": "anthropic-claude",
            "source_type": source_type,
            "local_path": rel_style,
            "component_id": component,
            "component_match_evidence": evidence,
            "mobbin_url": meta.get("mobbin_url"),
            "mobbin_id": meta.get("id") or meta.get("screen_id") or meta.get("flow_id"),
            "flow_id": meta.get("flow_id"),
            "flow_name": meta.get("flow_name") or meta.get("name"),
            "flow_position": meta.get("position"),
            "image_url": meta.get("image_url"),
            "query": meta.get("query") or meta.get("query_page"),
            "batch_file": meta.get("batch_file"),
            "image": stats,
            "ocr_text": text,
            "ocr_terms_top": [w for w, _ in Counter(words(text)).most_common(20)],
            "implementation_status": "visual_extracted_from_screenshot",
            "runtime_policy": "Use as evidence and normalized recipe input; do not copy proprietary production CSS/JS.",
        }
        records.append(rec)

    # write maps
    (OUT / "mobbin-source-map.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")
    with (OUT / "mobbin-source-map.csv").open("w", newline="", encoding="utf-8") as fh:
        fieldnames = ["index", "source_type", "component_id", "local_path", "mobbin_url", "mobbin_id", "flow_id", "flow_name", "flow_position", "image_url", "query"]
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        for r in records:
            w.writerow({k: r.get(k) for k in fieldnames})

    by_comp: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in records:
        by_comp[r["component_id"]].append(r)

    overview = ["# Mobbin Source Map — Anthropic / Claude", "", f"Total local screenshots/sections/flow screens processed: **{len(records)}**.", "", "This map links local evidence files to Mobbin source URLs where available and derives deterministic component/code facts from the local images.", "", "## Coverage by component", "", "| Component | Count | Primary evidence |", "|---|---:|---|"]
    for comp, rows in sorted(by_comp.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        evidence = ", ".join([f"`{x}`" for x, _ in Counter(e for r in rows for e in r["component_match_evidence"]).most_common(3)])
        overview.append(f"| `{comp}` | {len(rows)} | {evidence} |")
    overview += ["", "## Files", "", "- `mobbin-source-map.jsonl` — full structured map.", "- `mobbin-source-map.csv` — spreadsheet-friendly map.", "- `../../components/extracted/from-mobbin-screenshots/<component>/` — component-level extracted facts.", "", "## Limits", "", "For Claude app/authenticated screens, the repo stores image-derived facts and Mobbin source URLs. Exact DOM/CSS requires a live authenticated browser session and must be captured separately under `components/extracted/<component_id>/`."]
    (OUT / "README.md").write_text("\n".join(overview) + "\n", encoding="utf-8")

    for comp, rows in by_comp.items():
        cdir = EXTRACTED / comp
        cdir.mkdir(parents=True, exist_ok=True)
        (cdir / "screenshot-facts.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        terms = Counter(w for r in rows for w in r["ocr_terms_top"])
        pals = Counter(c for r in rows for c in r["image"]["palette"][:3])
        source_types = Counter(r["source_type"] for r in rows)
        mobbin_urls = [r["mobbin_url"] for r in rows if r.get("mobbin_url")]
        readme = [
            f"# Extracted Screenshot Facts — {comp}", "",
            f"Evidence count: **{len(rows)}** local Mobbin refs.", "",
            "## Source mix", "",
            *[f"- `{k}`: {v}" for k, v in source_types.most_common()],
            "", "## Dominant palettes", "",
            *[f"- `{k}` × {v}" for k, v in pals.most_common(10)],
            "", "## OCR terms", "",
            *[f"- `{k}` × {v}" for k, v in terms.most_common(30)],
            "", "## Source URL samples", "",
            *[f"- {u}" for u in mobbin_urls[:20]],
            "", "## Normalized implementation recipe", "",
            "Use these facts as visual/code evidence for the component capsule. This is not copied production CSS/JS; it is a repo-local implementation guide derived from observed screenshots.", "",
            "```text",
            f"component_id: {comp}",
            f"evidence_count: {len(rows)}",
            "surface: warm ivory/off-white, low contrast borders, restrained action hierarchy",
            "layout: generous whitespace, compact utility controls, editorial typography rhythm",
            "states_to_extract_next: hover, focus, disabled, loading, selected, billing/verification errors",
            "```",
        ]
        (cdir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
        token = {
            "component_id": comp,
            "evidence_count": len(rows),
            "source_type_counts": dict(source_types),
            "dominant_palettes": pals.most_common(12),
            "ocr_terms": terms.most_common(40),
            "confidence": "visual_extracted",
        }
        (cdir / "component.tokens.json").write_text(json.dumps(token, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"processed": len(records), "components": {k: len(v) for k, v in sorted(by_comp.items())}, "source_map": str(OUT / 'mobbin-source-map.jsonl')}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
