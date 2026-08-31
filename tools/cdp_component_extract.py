#!/usr/bin/env python3
"""Capture browser/CDP DOM + computed-style component evidence.

This tool uses the local Chrome DevTools Protocol at 127.0.0.1:9224 and writes
repo evidence under styles/<style>/components/extracted/browser-cdp/.
It never logs in or submits credentials. If an authenticated surface redirects to
login, it records that as an auth blocker.
"""
from __future__ import annotations

import base64
import json
import re
import time
import urllib.request
from pathlib import Path
from typing import Any

import websocket

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "styles" / "anthropic-claude"
OUT = STYLE / "components" / "extracted" / "browser-cdp"

TARGETS = [
    {
        "slug": "claude-login",
        "url": "https://claude.ai/login?from=logout",
        "expected_components": ["auth-onboarding"],
        "auth_required": False,
    },
    {
        "slug": "claude-new-auth-check",
        "url": "https://claude.ai/new",
        "expected_components": ["app-shell-sidebar", "composer-command-card", "artifact-workbench-panel"],
        "auth_required": True,
    },
    {
        "slug": "claude-settings-auth-check",
        "url": "https://claude.ai/settings/profile",
        "expected_components": ["settings-preferences"],
        "auth_required": True,
    },
    {
        "slug": "anthropic-claude-public",
        "url": "https://www.anthropic.com/claude",
        "expected_components": ["editorial-hero-section", "feature-tile-grid", "model-comparison-figure"],
        "auth_required": False,
    },
    {
        "slug": "anthropic-pricing-public",
        "url": "https://www.anthropic.com/pricing?subjects=claude&type=product",
        "expected_components": ["pricing-plan-cards", "model-comparison-figure"],
        "auth_required": False,
    },
]

JS_EXTRACT = r"""
(() => {
  const PROPS = [
    'display','position','boxSizing','width','height','minWidth','maxWidth','minHeight','maxHeight',
    'marginTop','marginRight','marginBottom','marginLeft','paddingTop','paddingRight','paddingBottom','paddingLeft',
    'fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','textTransform',
    'color','backgroundColor','backgroundImage','borderTopColor','borderRightColor','borderBottomColor','borderLeftColor',
    'borderTopWidth','borderRightWidth','borderBottomWidth','borderLeftWidth','borderStyle','borderRadius',
    'boxShadow','opacity','zIndex','overflow','gap','rowGap','columnGap','alignItems','justifyContent',
    'gridTemplateColumns','gridTemplateRows','flexDirection','flexWrap'
  ];
  const componentSelectors = {
    'auth-onboarding': ['form','input','button','[type="email"]','[type="tel"]','[autocomplete]','[href*="login"]','[href*="signup"]'],
    'pricing-plan-cards': ['[class*="price" i]','[class*="plan" i]','[class*="card" i]','section','article','table','button','a'],
    'settings-preferences': ['[class*="setting" i]','[class*="profile" i]','[class*="billing" i]','[role="switch"]','form','input','button'],
    'app-shell-sidebar': ['nav','aside','[class*="sidebar" i]','[aria-label*="nav" i]','[role="navigation"]'],
    'composer-command-card': ['textarea','[contenteditable="true"]','[role="textbox"]','[class*="composer" i]','[class*="prompt" i]','button'],
    'artifact-workbench-panel': ['[class*="artifact" i]','[class*="preview" i]','[class*="code" i]','pre','code','[role="tabpanel"]'],
    'editorial-hero-section': ['h1','h2','header','section','[class*="hero" i]','a','button'],
    'feature-tile-grid': ['[class*="card" i]','[class*="tile" i]','[class*="grid" i]','section','article'],
    'model-comparison-figure': ['table','[class*="model" i]','[class*="compare" i]','[class*="chart" i]','figure','section'],
    'data-viz-figure-card': ['svg','canvas','figure','[class*="chart" i]','[class*="graph" i]']
  };
  const text = (el) => (el.innerText || el.textContent || '').replace(/\s+/g,' ').trim().slice(0, 500);
  const cssPath = (el) => {
    const parts=[]; let n=el;
    while(n && n.nodeType===1 && parts.length<6){
      let s=n.tagName.toLowerCase();
      if(n.id){ s += '#' + n.id.replace(/[^a-zA-Z0-9_-]/g,''); parts.unshift(s); break; }
      const cls=[...n.classList].slice(0,2).map(c=>'.'+c.replace(/[^a-zA-Z0-9_-]/g,''));
      s += cls.join('');
      const parent=n.parentElement;
      if(parent){
        const same=[...parent.children].filter(c=>c.tagName===n.tagName);
        if(same.length>1) s += `:nth-of-type(${same.indexOf(n)+1})`;
      }
      parts.unshift(s); n=n.parentElement;
    }
    return parts.join(' > ');
  };
  const styleOf = (el) => {
    const cs = getComputedStyle(el); const out={};
    for (const p of PROPS) out[p]=cs[p];
    const vars={};
    for (const name of Array.from(cs).filter(x => x.startsWith('--')).slice(0,120)) vars[name]=cs.getPropertyValue(name).trim();
    return {props: out, cssVars: vars};
  };
  const sanitize = (html) => html
    .replace(/\s(?:nonce|integrity|crossorigin|data-[a-zA-Z0-9_-]+)=("[^"]*"|'[^']*')/g, '')
    .replace(/\s+/g, ' ')
    .slice(0, 2500);
  const seen = new Set();
  const components = {};
  for (const [cid, selectors] of Object.entries(componentSelectors)) {
    const els = [];
    for (const sel of selectors) {
      try { els.push(...document.querySelectorAll(sel)); } catch(e) {}
    }
    const filtered = [];
    for (const el of els) {
      if (seen.has(cid + ':' + cssPath(el))) continue;
      const r = el.getBoundingClientRect();
      const t = text(el);
      if ((r.width < 4 || r.height < 4) && !t) continue;
      seen.add(cid + ':' + cssPath(el));
      filtered.push({
        tag: el.tagName.toLowerCase(),
        role: el.getAttribute('role'),
        ariaLabel: el.getAttribute('aria-label'),
        type: el.getAttribute('type'),
        href: el.getAttribute('href'),
        text: t,
        className: String(el.className || '').slice(0,500),
        id: el.id || null,
        path: cssPath(el),
        rect: {x: Math.round(r.x), y: Math.round(r.y), width: Math.round(r.width), height: Math.round(r.height)},
        style: styleOf(el),
        html: sanitize(el.outerHTML || '')
      });
      if (filtered.length >= 30) break;
    }
    components[cid]=filtered;
  }
  const rootStyle = styleOf(document.documentElement);
  const bodyStyle = styleOf(document.body);
  const headings = [...document.querySelectorAll('h1,h2,h3,h4')].slice(0,80).map(el=>({tag:el.tagName.toLowerCase(), text:text(el), path:cssPath(el), rect:(()=>{const r=el.getBoundingClientRect(); return {x:Math.round(r.x), y:Math.round(r.y), width:Math.round(r.width), height:Math.round(r.height)}})(), style: styleOf(el)}));
  return {
    url: location.href,
    title: document.title,
    readyState: document.readyState,
    viewport: {width: innerWidth, height: innerHeight, scrollX, scrollY},
    rootStyle,
    bodyStyle,
    headings,
    components,
    bodyTextSample: document.body.innerText.replace(/\s+/g,' ').trim().slice(0,2000)
  };
})()
"""

class CDP:
    def __init__(self, wsurl: str):
        self.ws = websocket.create_connection(wsurl, timeout=20)
        self.i = 0
    def call(self, method: str, params: dict | None = None) -> Any:
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.i:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg.get("result")
    def close(self):
        self.ws.close()

def browser_ws() -> str:
    data = json.loads(urllib.request.urlopen("http://127.0.0.1:9224/json/version", timeout=5).read().decode())
    return data["webSocketDebuggerUrl"]

def create_target(url="about:blank") -> str:
    b = CDP(browser_ws())
    try:
        res = b.call("Target.createTarget", {"url": url, "newWindow": False, "background": True})
        return res["targetId"]
    finally:
        b.close()

def target_ws(target_id: str) -> str:
    tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9224/json/list", timeout=5).read().decode())
    for t in tabs:
        if t.get("id") == target_id:
            return t["webSocketDebuggerUrl"]
    raise RuntimeError(f"target not found {target_id}")

def safe_slug(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "-", s).strip("-")

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    target_id = create_target()
    cdp = CDP(target_ws(target_id))
    try:
        cdp.call("Page.enable")
        cdp.call("Runtime.enable")
        for target in TARGETS:
            slug = target["slug"]
            odir = OUT / slug
            odir.mkdir(parents=True, exist_ok=True)
            cdp.call("Page.navigate", {"url": target["url"]})
            time.sleep(8)
            # Let late hydration settle
            for _ in range(8):
                state = cdp.call("Runtime.evaluate", {"expression": "document.readyState", "returnByValue": True}).get("result", {}).get("value")
                if state == "complete": break
                time.sleep(1)
            time.sleep(2)
            res = cdp.call("Runtime.evaluate", {"expression": JS_EXTRACT, "returnByValue": True, "awaitPromise": True, "timeout": 30000})
            val = res.get("result", {}).get("value") or {}
            html = cdp.call("Runtime.evaluate", {"expression": "document.documentElement.outerHTML", "returnByValue": True, "timeout": 20000}).get("result", {}).get("value", "")
            shot = cdp.call("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})
            (odir / "screenshot.png").write_bytes(base64.b64decode(shot["data"]))
            (odir / "dom.html").write_text(html, encoding="utf-8")
            auth_blocked = bool(target["auth_required"] and ("/login" in val.get("url", "") or "sign in" in (val.get("title", "") + val.get("bodyTextSample", "")).lower()))
            facts = {
                "target": target,
                "captured_url": val.get("url"),
                "title": val.get("title"),
                "auth_blocked": auth_blocked,
                "capture_method": "chrome_devtools_protocol_runtime_evaluate_getComputedStyle",
                "policy": "Evidence only. Do not copy proprietary CSS/JS as runtime dependency.",
                "data": val,
            }
            (odir / "computed.json").write_text(json.dumps(facts, indent=2, ensure_ascii=False), encoding="utf-8")
            # component summaries
            comp_counts = {cid: len(items) for cid, items in (val.get("components") or {}).items() if items}
            md = [f"# Browser/CDP Evidence — {slug}", "", f"Requested URL: {target['url']}", f"Captured URL: {val.get('url')}", f"Title: {val.get('title')}", f"Auth blocked: `{auth_blocked}`", "", "## Component matches", ""]
            md += [f"- `{k}`: {v} elements" for k, v in sorted(comp_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]]
            md += ["", "## Files", "", "- `computed.json` — full computed style facts.", "- `dom.html` — page DOM snapshot.", "- `screenshot.png` — viewport screenshot.", "", "Policy: evidence only; runtime output must be original/adapted."]
            (odir / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")
            index.append({"slug": slug, "requested_url": target["url"], "captured_url": val.get("url"), "title": val.get("title"), "auth_required": target["auth_required"], "auth_blocked": auth_blocked, "expected_components": target["expected_components"], "component_counts": comp_counts, "path": str(odir.relative_to(STYLE))})
    finally:
        cdp.close()
    (OUT / "browser-cdp-index.json").write_text(json.dumps({"targets": index}, indent=2, ensure_ascii=False), encoding="utf-8")
    (OUT / "README.md").write_text("# Browser/CDP Component Evidence\n\n" + "\n".join(f"- `{x['slug']}` — {x['captured_url']} — auth_blocked={x['auth_blocked']}" for x in index) + "\n", encoding="utf-8")
    print(json.dumps({"captured": len(index), "auth_blocked": [x["slug"] for x in index if x["auth_blocked"]], "out": str(OUT)}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
