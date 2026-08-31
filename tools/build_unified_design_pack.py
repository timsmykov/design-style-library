#!/usr/bin/env python3
from __future__ import annotations
import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / 'baselines' / 'voltagent-awesome-design-md'
PACK = ROOT / 'pack'
MAP_PATH = ROOT / 'baselines' / 'style-baseline-map.json'

STYLE_NAMES = {
    'rudn-academic-dataviz': 'RUDN Academic Data Visualization',
    'anthropic-claude': 'Anthropic / Claude Editorial Workbench',
    'perplexity-answer-engine': 'Perplexity Answer Engine',
    'notion-document-os': 'Notion Document OS',
    'linear-operational-workspace': 'Linear Operational Workspace',
    'stripe-trust-commerce': 'Stripe Trust Commerce',
    'metamask-crypto-wallet-trust': 'MetaMask / Crypto Wallet Trust',
    'vercel-developer-control-plane': 'Vercel Developer Control Plane',
    'raycast-command-native': 'Raycast Command Native',
    'figma-collaborative-canvas': 'Figma Collaborative Canvas',
    'airbnb-marketplace-warm-consumer': 'Airbnb Marketplace Warm Consumer',
    'cursor-ai-ide': 'Cursor AI IDE',
}

def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))

def copytree(src: Path, dst: Path) -> None:
    if dst.exists() or dst.is_symlink():
        if dst.is_symlink():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    shutil.copytree(src, dst)

def safe_read(path: Path, max_chars: int = 5000) -> str:
    if not path.exists():
        return ''
    s = path.read_text(encoding='utf-8', errors='ignore')
    return s if len(s) <= max_chars else s[:max_chars] + '\n\n[truncated in unified pack view; see source file for full content]\n'

def main() -> int:
    if not BASELINE.exists():
        raise SystemExit('missing baseline snapshot; run sync_voltagent_baseline.py first')
    old_registry_generated_at = None
    old_registry = PACK / 'registry.json'
    if old_registry.exists():
        try:
            old_registry_generated_at = json.loads(old_registry.read_text(encoding='utf-8')).get('generated_at')
        except Exception:
            old_registry_generated_at = None
    if PACK.exists() or PACK.is_symlink():
        if PACK.is_symlink():
            PACK.unlink()
        else:
            shutil.rmtree(PACK)
    PACK.mkdir()
    (PACK / 'styles').mkdir()
    (PACK / 'extensions').mkdir()
    (PACK / 'components').mkdir()
    (PACK / 'catalog').mkdir()

    # Copy broad DESIGN.md catalog into the single runtime pack.
    copytree(BASELINE / 'design-md', PACK / 'design-md')
    shutil.copy2(BASELINE / 'LICENSE', PACK / 'LICENSE.voltagent-awesome-design-md')
    shutil.copy2(BASELINE / 'README.md', PACK / 'UPSTREAM_README.md')

    baseline_index = json.loads((BASELINE / 'baseline-index.json').read_text())
    baseline_map = json.loads(MAP_PATH.read_text()) if MAP_PATH.exists() else []
    map_by_style = {m['style_id']: m for m in baseline_map}

    unified_entries = []
    for style_dir in sorted((ROOT / 'styles').iterdir()):
        if not style_dir.is_dir():
            continue
        sid = style_dir.name
        out = PACK / 'styles' / sid
        out.mkdir(parents=True)
        ext_link = PACK / 'extensions' / sid
        comp_link = PACK / 'components' / sid
        if ext_link.exists() or ext_link.is_symlink():
            ext_link.unlink() if ext_link.is_symlink() else shutil.rmtree(ext_link)
        if comp_link.exists() or comp_link.is_symlink():
            comp_link.unlink() if comp_link.is_symlink() else shutil.rmtree(comp_link)
        copytree(style_dir, ext_link)
        component_source = ROOT / 'gbrain_export' / 'components' / sid
        if component_source.exists():
            copytree(component_source, comp_link)
        else:
            comp_link.mkdir(parents=True, exist_ok=True)

        copied = map_by_style.get(sid, {}).get('copied', [])
        baseline_sections = []
        for bid in copied:
            bpath = PACK / 'design-md' / bid / 'DESIGN.md'
            if bpath.exists():
                baseline_sections.append(f"## Baseline: `{bid}`\n\nSource: `pack/design-md/{bid}/DESIGN.md`\n\n" + safe_read(bpath, 8000))
        if not baseline_sections:
            baseline_sections.append('## Baseline\n\nNo exact VoltAgent DESIGN.md baseline exists. Use the global pack catalog plus this deep extension.\n')

        style_md = safe_read(style_dir / 'STYLE.md', 8000)
        atlas = safe_read(style_dir / 'components' / 'component-atlas.md', 5000)
        contract = safe_read(style_dir / 'agent-contract.md', 5000)
        design_text = f"""# Unified DESIGN.md — {STYLE_NAMES.get(sid, sid)}

This file is the single-pack runtime view for `{sid}`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/{sid}`
Component semantic slices: `pack/components/{sid}`

---

{chr(10).join(baseline_sections)}

---

# Hermes deep extension override

## STYLE.md excerpt

{style_md}

## Component atlas excerpt

{atlas}

## Agent contract excerpt

{contract}
"""
        (out / 'DESIGN.md').write_text(design_text, encoding='utf-8')
        (out / 'README.md').write_text(f"""# {STYLE_NAMES.get(sid, sid)}

Single-pack entry for `{sid}`.

- Unified DESIGN: `pack/styles/{sid}/DESIGN.md`
- Deep extension: `pack/extensions/{sid}`
- Component slices: `pack/components/{sid}`
- Baselines: {', '.join(copied) if copied else 'none exact'}

Use this directory as the runtime-facing pack entry. The historical `baselines/` and `styles/` directories remain source/provenance/build artifacts.
""", encoding='utf-8')
        unified_entries.append({
            'id': sid,
            'name': STYLE_NAMES.get(sid, sid),
            'entry': f'pack/styles/{sid}/DESIGN.md',
            'extension': f'pack/extensions/{sid}',
            'components': f'pack/components/{sid}',
            'baseline_ids': copied,
        })

    registry = {
        'id': 'hermes-unified-design-pack',
        'generated_at': old_registry_generated_at or baseline_index.get('synced_at'),
        'role': 'single runtime pack combining VoltAgent broad DESIGN.md baseline with Hermes deep extensions',
        'source_baseline': {
            'fork': 'timsmykov/awesome-design-md',
            'upstream': 'VoltAgent/awesome-design-md',
            'upstream_commit': baseline_index.get('upstream_commit'),
            'license': 'MIT',
            'design_md_count': baseline_index.get('design_md_count'),
        },
        'runtime_entrypoints': {
            'root_contract': 'pack/DESIGN.md',
            'registry': 'pack/registry.json',
            'broad_catalog': 'pack/design-md/',
            'unified_styles': 'pack/styles/',
            'deep_extensions': 'pack/extensions/',
            'component_slices': 'pack/components/',
        },
        'authority_order': [
            'pack/DESIGN.md',
            'pack/styles/<style-id>/DESIGN.md',
            'pack/extensions/<style-id> deep source files',
            'pack/components/<style-id> semantic component slices',
        ],
        'styles': unified_entries,
    }
    (PACK / 'registry.json').write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding='utf-8')
    (PACK / 'README.md').write_text(f"""# Hermes Unified Design Pack

This is the single runtime-facing design pack for agents.

It consolidates:

- broad VoltAgent `DESIGN.md` catalog: `pack/design-md/`
- Hermes deep style extensions: `pack/extensions/<style-id>`
- generated component slices: `pack/components/<style-id>`
- unified per-style entrypoints: `pack/styles/<style-id>/DESIGN.md`

Agents should treat `pack/` as the design system package. The older `baselines/` and `styles/` roots remain source/provenance/build layers, not the runtime mental model.

## Default decision rule

1. If a task names a style, load `pack/styles/<style-id>/DESIGN.md`.
2. If only a category is named, use `pack/registry.json` and root `registry.yaml` to choose the closest style.
3. If no deep style exists, use `pack/design-md/<brand>/DESIGN.md` from the broad catalog.
4. If implementing a component, prefer `pack/components/<style-id>/...` and `pack/extensions/<style-id>/components/capsules/...`.

## Non-cloning rule

Use style grammar, not brand impersonation. Do not copy logos, private data, proprietary code, or exact production screens.
""", encoding='utf-8')
    (PACK / 'DESIGN.md').write_text(f"""# Hermes Unified Design Pack — Default DESIGN.md

Use `pack/` as one consolidated design package.

## What this pack is

This pack is a fork-based expansion of VoltAgent `awesome-design-md`:

- VoltAgent provides broad `DESIGN.md` coverage across many brands and product categories.
- Hermes adds deeper evidence-backed extensions for selected styles: local evidence, tokens, component capsules, DOM/CSS captures, eval gates, and Gbrain component slices.

## Runtime load order

1. Open `pack/registry.json`.
2. Choose a style from `pack/styles/<style-id>/DESIGN.md` when a deep Hermes extension exists.
3. Otherwise choose a broad baseline from `pack/design-md/<brand>/DESIGN.md`.
4. For implementation detail, use `pack/extensions/<style-id>/` and `pack/components/<style-id>/`.

## Authority

A deep Hermes extension overrides broad VoltAgent baseline guidance. The baseline is the foundation; Hermes extension is the build-out.

## Boundary

Runtime agents use local files only. GitHub, Mobbin, Firecrawl, Browser/CDP, and auth sessions are build-time enrichment tools only.
""", encoding='utf-8')
    print(json.dumps({'pack': 'pack', 'styles': len(unified_entries), 'baseline_design_md': baseline_index.get('design_md_count')}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
