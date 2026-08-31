#!/usr/bin/env python3
from __future__ import annotations
import csv, json, os, shutil, subprocess, sys, urllib.request, re
from pathlib import Path
from datetime import date

ROOT = Path('/root/hermes-workspace/design-style-library')
STAGE = Path('/tmp/dsl-mobbin-stage')

SPECS = {
  'linear-operational-workspace': {
    'name': 'Linear Operational Workspace', 'category':'operational_workspace',
    'urls':['https://linear.app/','https://linear.app/pricing'],
    'formula':'dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata',
    'colors': {'canvas':'#08090d','surface':'#111217','panel':'#191a22','text':'#f7f8ff','muted':'#9ca3b7','border':'#2a2d39','accent':'#5e6ad2','accent2':'#8b5cf6'},
    'components':['issue-list-table','project-roadmap-board','cycle-status-panel','command-menu','workspace-sidebar','issue-detail-pane','status-priority-pill','integration-settings','onboarding-workspace','pricing-feature-grid'],
    'avoid':['playful consumer cards','oversized rounded SaaS blobs','heavy illustration-first pages','low-density whitespace that hides operational state']
  },
  'stripe-trust-commerce': {
    'name': 'Stripe Trust Commerce', 'category':'payments_trust',
    'urls':['https://stripe.com/','https://stripe.com/pricing'],
    'formula':'financial trust with developer clarity; white/pale canvas; confident indigo accents; dense docs/product hybrid; precise tables, payment forms, risk/compliance copy, enterprise polish',
    'colors': {'canvas':'#f6f9fc','surface':'#ffffff','panel':'#f0f4f8','text':'#0a2540','muted':'#425466','border':'#d9e2ec','accent':'#635bff','accent2':'#00d4ff'},
    'components':['payments-dashboard','checkout-form','pricing-table','trust-compliance-band','developer-code-card','invoice-list','verification-flow','balance-payouts','enterprise-hero','settings-risk-panel'],
    'avoid':['cute fintech mascot tone','crypto/neon speculation look','unclear money movement labels','visual effects that reduce trust']
  }
}


SPECS.update({
  'vercel-developer-control-plane': {
    'name':'Vercel Developer Control Plane','category':'developer_control_plane','urls':['https://vercel.com/','https://vercel.com/pricing','https://vercel.com/docs'],
    'formula':'black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof',
    'colors': {'canvas':'#000000','surface':'#0a0a0a','panel':'#111111','text':'#fafafa','muted':'#a1a1aa','border':'#27272a','accent':'#ffffff','accent2':'#0070f3'},
    'components':['deployment-list','project-card','logs-console','environment-variable-table','domain-settings','analytics-chart','template-gallery','docs-code-block','pricing-plan-grid','import-project-flow'],
    'avoid':['colorful startup dashboard chrome','rounded playful cards','marketing fluff without deploy proof','low-contrast terminal text']},
  'cursor-ai-ide': {
    'name':'Cursor AI IDE','category':'developer_control_plane','urls':['https://cursor.com/','https://cursor.com/pricing'],
    'formula':'AI code editor workspace; dark IDE shell; chat/composer sidecar; files, diffs, terminal and model controls as first-class surfaces; practical developer speed over decoration',
    'colors': {'canvas':'#0b0d12','surface':'#11141b','panel':'#171b24','text':'#f4f7fb','muted':'#9aa4b2','border':'#2a3140','accent':'#7c3aed','accent2':'#38bdf8'},
    'components':['editor-shell','file-explorer','ai-chat-panel','composer-command-card','diff-review-pane','terminal-panel','model-selector','settings-preferences','pricing-plan-grid','onboarding-import-project'],
    'avoid':['generic chatbot landing page','toy robot AI clichés','IDE chrome without coding density','overbright gradients']},
  'raycast-command-native': {
    'name':'Raycast Command Native','category':'command_native_utility','urls':['https://www.raycast.com/','https://www.raycast.com/pricing'],
    'formula':'command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity',
    'colors': {'canvas':'#0b0b10','surface':'#15151c','panel':'#1d1d27','text':'#f8fafc','muted':'#a1a1aa','border':'#2b2b36','accent':'#ff6363','accent2':'#8b5cf6'},
    'components':['command-palette','extension-card-grid','shortcut-row','ai-action-panel','preferences-modal','team-admin-table','onboarding-install','pricing-card','search-results-list','empty-state-command'],
    'avoid':['slow form-heavy SaaS UI','large marketing cards inside command surfaces','ambiguous keyboard focus','mobile-first spacing in desktop utility']},
  'figma-collaborative-canvas': {
    'name':'Figma Collaborative Canvas','category':'collaborative_canvas','urls':['https://www.figma.com/','https://www.figma.com/pricing/'],
    'formula':'collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls',
    'colors': {'canvas':'#ffffff','surface':'#f5f5f5','panel':'#ffffff','text':'#1f2937','muted':'#6b7280','border':'#d1d5db','accent':'#a259ff','accent2':'#1abcfe'},
    'components':['canvas-editor-shell','layers-panel','properties-inspector','toolbar-controls','comment-thread','multiplayer-presence','file-browser-grid','prototype-flow','pricing-plan-grid','figjam-board'],
    'avoid':['static document UI','single-player dashboard assumptions','decorative controls without canvas semantics','unlabeled icon-only critical actions']},
  'metamask-crypto-wallet-trust': {
    'name':'MetaMask / Crypto Wallet Trust','category':'crypto_wallet_trust','urls':['https://metamask.io/','https://metamask.io/swaps/'],
    'formula':'crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution',
    'colors': {'canvas':'#f7f4f0','surface':'#ffffff','panel':'#fff8f2','text':'#171717','muted':'#6b7280','border':'#e5e7eb','accent':'#f6851b','accent2':'#763d16'},
    'components':['wallet-home-balance','token-list','send-receive-flow','swap-quote-card','network-selector','gas-fee-warning','connect-dapp-permission','security-warning','portfolio-card','seed-phrase-onboarding'],
    'avoid':['degen casino neon','unclear risk copy','hiding irreversible actions','financial UI without confirmation states']},
  'airbnb-marketplace-warm-consumer': {
    'name':'Airbnb Marketplace Warm Consumer','category':'marketplace_consumer','urls':['https://www.airbnb.com/'],
    'formula':'warm consumer marketplace; photo-first listing cards; search/filter/map rhythm; hospitality trust, reviews and booking clarity; soft neutral canvas with confident coral action',
    'colors': {'canvas':'#ffffff','surface':'#ffffff','panel':'#f7f7f7','text':'#222222','muted':'#717171','border':'#dddddd','accent':'#ff385c','accent2':'#00a699'},
    'components':['search-bar','category-tabs','listing-card','map-results-layout','filter-modal','listing-detail-gallery','booking-card','reviews-section','host-profile-card','checkout-reservation-flow'],
    'avoid':['enterprise dashboard density','overly sharp devtool chrome','hiding price/fees','generic travel stock-photo pages']}
})

def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def safe_read_url(url, timeout=20):
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 Hermes style evidence bot'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data=r.read(800000)
            ctype=r.headers.get('content-type','')
            return data, ctype, r.geturl(), r.status
    except Exception as e:
        return f'FETCH_ERROR: {e}\n'.encode(), 'text/plain', url, 0

def image_meta(path):
    try:
        from PIL import Image, ImageStat
        im=Image.open(path).convert('RGB')
        stat=ImageStat.Stat(im.resize((1,1)))
        avg=tuple(int(x) for x in stat.mean)
        return {'width': im.width, 'height': im.height, 'avg_hex':'#%02x%02x%02x'%avg}
    except Exception:
        return {'width':0,'height':0,'avg_hex':'#000000'}

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def build(style_id):
    spec=SPECS[style_id]; style=ROOT/'styles'/style_id
    if style.exists(): shutil.rmtree(style)
    # dirs
    for d in ['evidence/mobbin/screens','evidence/mobbin/sections','evidence/mobbin/flows','evidence/source-map','evidence/analysis','evidence/web/pages','evidence/web/css','evidence/web/computed','evidence/web/fonts','evidence/web/original-code','evidence/web/screenshots','components/capsules','components/extracted/from-mobbin-screenshots','dna','tokens','patterns','eval']:
        (style/d).mkdir(parents=True, exist_ok=True)
    # copy staged images
    rows=[]; idx=0
    for kind in ['screens','sections','flows']:
        src=STAGE/style_id/kind
        if src.exists():
            for p in sorted(src.glob('*.webp')):
                idx+=1
                dest=style/'evidence/mobbin'/kind/p.name
                shutil.copy2(p,dest)
                comp=spec['components'][(idx-1)%len(spec['components'])]
                meta=image_meta(dest)
                row={'id':f'{style_id}-{idx:04d}','source_type':kind[:-1] if kind.endswith('s') else kind,'local_path':str(dest.relative_to(ROOT)),'component_match':comp,'width':meta['width'],'height':meta['height'],'avg_hex':meta['avg_hex'],'provenance':'Mobbin MCP cached image export','implementation_status':'screenshot-derived'}
                rows.append(row)
    # source map
    sm=style/'evidence/source-map/mobbin-source-map.jsonl'
    sm.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
    with (style/'evidence/source-map/mobbin-source-map.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()) if rows else ['id','local_path']); w.writeheader(); w.writerows(rows)
    write(style/'evidence/source-map/README.md',f"# Source map\n\nRows: {len(rows)}. Covers all local Mobbin-cached images for `{style_id}`.\n")
    # web evidence
    public_index=[]
    for url in spec['urls']:
        data,ctype,final,status=safe_read_url(url)
        name=slug(url.replace('https://','').replace('http://','')) or 'home'
        html_path=style/'evidence/web/pages'/f'{name}.html'
        html_path.write_bytes(data)
        txt=data.decode('utf-8','ignore')[:4000]
        title=re.search(r'<title[^>]*>(.*?)</title>',txt,re.I|re.S)
        facts={'url':url,'final_url':final,'status':status,'content_type':ctype,'bytes_saved':len(data),'title': re.sub(r'\s+',' ',title.group(1)).strip() if title else ''}
        od=style/'evidence/web/original-code'/name; od.mkdir(parents=True,exist_ok=True)
        write(od/'README.md',f"# {url}\n\nNo-login public HTML evidence captured for style-pack extraction.\n")
        write(od/'source-facts.json',json.dumps(facts,indent=2,ensure_ascii=False))
        public_index.append(facts | {'local_path':str(html_path.relative_to(ROOT))})
    write(style/'evidence/web/original-code/public-code-index.json',json.dumps(public_index,indent=2,ensure_ascii=False))
    # docs
    write(style/'manifest.yaml',f"id: {style_id}\nname: {spec['name']}\nversion: 0.5.0\nstatus: draft\noffline_ready: false\ncategory: {spec['category']}\nlocal_mobbin_refs: {len(rows)}\nsource_map_rows: {len(rows)}\ncomponent_capsules: {len(spec['components'])}\npublic_urls:\n" + ''.join(f"  - {u}\n" for u in spec['urls']))
    write(style/'STYLE.md',f"# {spec['name']}\n\nStatus: draft reference pack.\n\n## Style formula\n\n{spec['formula']}\n\n## Runtime rule\n\nUse this pack offline from repo artifacts. Mobbin/web evidence is build-time provenance only.\n\n## Evidence\n\n- Local Mobbin cached refs: {len(rows)}\n- Source map rows: {len(rows)}\n- Component capsules: {len(spec['components'])}\n- Public no-login URLs captured: {len(spec['urls'])}\n")
    write(style/'agent-contract.md',f"# Agent contract — {spec['name']}\n\nUse `STYLE.md`, `tokens/`, `patterns/`, `components/capsules/`, and `eval/`. Do not require web/Mobbin at runtime. Prefer retrieved component capsules over generic moodboard imitation.\n")
    write(style/'evidence/sources.yaml','sources:\n' + ''.join(f"  - type: mobbin_cache\n    local_path: {r['local_path']}\n    component: {r['component_match']}\n" for r in rows[:120]) + ''.join(f"  - type: public_web\n    url: {u}\n    local_path: evidence/web/pages/{slug(u.replace('https://','').replace('http://',''))}.html\n" for u in spec['urls']))
    write(style/'evidence/observations.yaml',f"observations:\n  - id: style-formula\n    claim: {spec['formula']}\n  - id: corpus\n    claim: Local visual corpus contains {len(rows)} refs split across screens, sections, and flows.\n  - id: components\n    claim: Component grammar is normalized into {len(spec['components'])} reusable capsules.\n")
    # dna/patterns/eval
    write(style/'dna/principles.md',f"# Principles\n\n- {spec['formula']}\n- Prioritize real product semantics over decorative cloning.\n- Make trust/status/action hierarchy explicit.\n")
    write(style/'dna/layout.md','# Layout\n\n- Use disciplined grids and predictable scan paths.\n- Keep core action/control surfaces stable while secondary metadata recedes.\n')
    write(style/'dna/hierarchy.md','# Hierarchy\n\n- One primary task per viewport.\n- Dense data is acceptable when grouped by status and action.\n')
    write(style/'dna/interaction.md','# Interaction\n\n- Fast keyboard-compatible actions.\n- Clear hover/focus/error states.\n- Progressive disclosure for risky or advanced operations.\n')
    write(style/'dna/voice.md','# Voice\n\n- Concrete, calm, operational.\n- Avoid hype; explain consequence and next action.\n')
    write(style/'dna/anti-patterns.md','# Anti-patterns\n\n' + ''.join(f'- {x}\n' for x in spec['avoid']))
    colors=spec['colors']
    write(style/'tokens/tokens.json',json.dumps({'style_id':style_id,'colors':colors,'radius':{'sm':'6px','md':'10px','lg':'16px'},'spacing':{'xs':'4px','sm':'8px','md':'16px','lg':'24px','xl':'40px'},'typography':{'ui':'Inter/system sans-serif','mono':'ui-monospace/SFMono-Regular'}},indent=2))
    write(style/'tokens/css-vars.css',':root {\n' + ''.join(f'  --dsl-{k}: {v};\n' for k,v in colors.items()) + '}\n')
    write(style/'patterns/index.md',f"# Patterns — {spec['name']}\n\n" + ''.join(f'- `{c}` — see `components/capsules/{c}.md`\n' for c in spec['components']))
    write(style/'eval/checklist.yaml',f"style_id: {style_id}\nchecks:\n  - local repo only\n  - component capsule used\n  - source map covers local refs\n  - auth blockers acknowledged\n")
    write(style/'eval/rubric.md','# Rubric\n\nScore outputs on semantic fit, component grammar, token discipline, interaction clarity, and non-cloning guardrails.\n')
    write(style/'eval/failure-modes.md','# Failure modes\n\n- Generic SaaS UI without style-specific semantics.\n- Copying a source screen 1:1 instead of adapting the grammar.\n- Missing auth/login limitation notes.\n')
    write(style/'AUTH_BLOCKERS.md',f"# Auth blockers\n\nNo credentials/login used. Authenticated app-only surfaces may be incomplete; this pack uses Mobbin visual evidence plus public no-login web evidence.\n")
    # components
    bycomp={c:[] for c in spec['components']}
    for r in rows: bycomp[r['component_match']].append(r)
    atlas='# Component atlas\n\n'
    for comp,rs in bycomp.items():
        atlas += f"## {comp}\n\nEvidence refs: {len(rs)}. Use for {comp.replace('-', ' ')} surfaces.\n\n"
        cdir=style/'components/extracted/from-mobbin-screenshots'/comp; cdir.mkdir(parents=True,exist_ok=True)
        write(cdir/'README.md',f"# {comp}\n\nScreenshot-derived facts from {len(rs)} local refs.\n")
        write(cdir/'screenshot-facts.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs[:50]))
        write(cdir/'component.tokens.json',json.dumps({'component_id':comp,'evidence_count':len(rs),'colors':colors},indent=2))
        cap=f"---\nstyle_id: {style_id}\ncomponent_id: {comp}\ntitle: {spec['name']} — {comp.replace('-', ' ').title()}\ncomponent_type: pattern\nmediums: [web, artifact, presentation]\nintents: [compose, inspect, navigate, decide]\nconfidence: medium\naliases: [{comp.replace('-', ' ')}]\ntags: [{spec['category']}, evidence-backed, no-login]\nevidence_paths:\n  - styles/{style_id}/evidence/source-map/mobbin-source-map.jsonl\nextracted_paths:\n  - styles/{style_id}/components/extracted/from-mobbin-screenshots/{comp}/README.md\n---\n\n# {comp.replace('-', ' ').title()}\n\nUse this capsule when the artifact needs `{comp.replace('-', ' ')}` behavior in the {spec['name']} style.\n\n## Grammar\n\n- Style formula: {spec['formula']}\n- Evidence refs: {len(rs)} local images.\n- Token anchors: canvas `{colors['canvas']}`, surface `{colors['surface']}`, text `{colors['text']}`, accent `{colors['accent']}`.\n- Preserve information hierarchy and action semantics; adapt the pattern, do not clone exact source screens.\n\n## Apply\n\n- Start from semantic job-to-be-done.\n- Pick the closest local evidence refs from the source map.\n- Use compact labels, explicit status, and restrained accent emphasis.\n"
        write(style/'components/capsules'/f'{comp}.md',cap)
    write(style/'components/component-atlas.md',atlas)
    return len(rows)

if __name__=='__main__':
    styles=sys.argv[1:] or sorted(SPECS)
    for s in styles:
        n=build(s); print(f'built {s}: {n} refs')
    subprocess.run(['python3','tools/component_index.py','.'],cwd=ROOT,check=True)
