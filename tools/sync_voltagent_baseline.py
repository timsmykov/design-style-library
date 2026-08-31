#!/usr/bin/env python3
from __future__ import annotations
import json, re, shutil, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path('/root/hermes-workspace/awesome-design-md')
BASELINE_DIR = ROOT / 'baselines' / 'voltagent-awesome-design-md'

STYLE_MAP = {
    'anthropic-claude': ['claude'],
    'perplexity-answer-engine': [],
    'notion-document-os': ['notion'],
    'linear-operational-workspace': ['linear.app'],
    'stripe-trust-commerce': ['stripe'],
    'metamask-crypto-wallet-trust': ['coinbase', 'binance', 'kraken'],
    'vercel-developer-control-plane': ['vercel'],
    'raycast-command-native': ['raycast'],
    'figma-collaborative-canvas': ['figma'],
    'airbnb-marketplace-warm-consumer': ['airbnb'],
    'cursor-ai-ide': ['cursor'],
}

def git(path: Path, *args: str) -> str:
    return subprocess.check_output(['git', '-C', str(path), *args], text=True).strip()

def clean_copy(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git', '.github'))

def title_from_design(text: str) -> str:
    m = re.search(r'^name:\s*(.+)$', text, re.M)
    if m:
        return m.group(1).strip().strip('"')
    return ''

def description_from_design(text: str) -> str:
    m = re.search(r'^description:\s*(.+)$', text, re.M)
    if m:
        return m.group(1).strip().strip('"')[:1000]
    return ''

def main() -> int:
    src = Path(__import__('sys').argv[1]) if len(__import__('sys').argv) > 1 else DEFAULT_SOURCE
    if not (src / 'design-md').exists():
        raise SystemExit(f'missing design-md in {src}')

    clean_copy(src, BASELINE_DIR)
    commit = git(src, 'rev-parse', 'HEAD')
    url = subprocess.check_output(['gh', 'repo', 'view', 'timsmykov/awesome-design-md', '--json', 'url', '-q', '.url'], text=True).strip()
    upstream = subprocess.check_output(['gh', 'repo', 'view', 'VoltAgent/awesome-design-md', '--json', 'url', '-q', '.url'], text=True).strip()

    design_dirs = sorted([p for p in (BASELINE_DIR / 'design-md').iterdir() if p.is_dir()])
    styles = []
    for d in design_dirs:
        design = d / 'DESIGN.md'
        readme = d / 'README.md'
        text = design.read_text(encoding='utf-8', errors='ignore') if design.exists() else ''
        styles.append({
            'id': d.name,
            'path': str(design.relative_to(ROOT)) if design.exists() else '',
            'readme': str(readme.relative_to(ROOT)) if readme.exists() else '',
            'title': title_from_design(text),
            'description': description_from_design(text),
            'bytes': design.stat().st_size if design.exists() else 0,
        })

    meta = {
        'source': 'VoltAgent/awesome-design-md',
        'fork': 'timsmykov/awesome-design-md',
        'source_url': upstream,
        'fork_url': url,
        'upstream_commit': commit,
        'license': 'MIT',
        'synced_at': datetime.now(timezone.utc).isoformat(),
        'design_md_count': len([s for s in styles if s['path']]),
        'usage': 'default broad DESIGN.md baseline for runtime agents; local style packs override it for deep evidence-backed work',
        'styles': styles,
    }
    (BASELINE_DIR / 'baseline-index.json').write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding='utf-8')
    (ROOT / 'baselines').mkdir(exist_ok=True)
    (ROOT / 'baselines' / 'README.md').write_text(f"""# Baselines

This directory stores broad DESIGN.md baselines used by runtime agents before selecting a deeper local style pack.

## Default baseline

- Source: `VoltAgent/awesome-design-md`
- Local fork: `timsmykov/awesome-design-md`
- Snapshot path: `baselines/voltagent-awesome-design-md/`
- Upstream commit: `{commit}`
- License: MIT; original license retained at `baselines/voltagent-awesome-design-md/LICENSE`.

Runtime policy: load the broad baseline only as a starting grammar, then prefer `styles/<style-id>/` for exact, evidence-backed packs.
""", encoding='utf-8')

    # Link existing deep packs to the relevant VoltAgent baseline docs.
    mapping_rows = []
    for style_id, baseline_ids in STYLE_MAP.items():
        style_dir = ROOT / 'styles' / style_id
        if not style_dir.exists():
            continue
        out_dir = style_dir / 'baseline' / 'voltagent'
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        rows = []
        for bid in baseline_ids:
            src_design = BASELINE_DIR / 'design-md' / bid / 'DESIGN.md'
            if src_design.exists():
                shutil.copy2(src_design, out_dir / f'{bid}.DESIGN.md')
                rows.append((bid, f'styles/{style_id}/baseline/voltagent/{bid}.DESIGN.md'))
        mapping_rows.append({'style_id': style_id, 'baseline_ids': baseline_ids, 'copied': [r[0] for r in rows]})
        if rows:
            table = '\n'.join(f'- `{bid}` → `{path}`' for bid, path in rows)
            note = 'Use these as broad baseline grammar. Our `STYLE.md`, `tokens/`, `components/`, evidence, and eval override the generic baseline.'
        else:
            table = '- No exact VoltAgent DESIGN.md match; use global baseline index plus our deep pack only.'
            note = 'No direct baseline exists; do not force a weak adjacent match unless explicitly useful.'
        (out_dir / 'README.md').write_text(f"""# VoltAgent baseline link — {style_id}

{table}

{note}

Source snapshot: `baselines/voltagent-awesome-design-md/` from fork `timsmykov/awesome-design-md` / upstream `VoltAgent/awesome-design-md` commit `{commit}`.
""", encoding='utf-8')
    (ROOT / 'baselines' / 'style-baseline-map.json').write_text(json.dumps(mapping_rows, indent=2, ensure_ascii=False), encoding='utf-8')

    # Root DESIGN.md makes the default style contract discoverable by generic coding/design agents.
    (ROOT / 'DESIGN.md').write_text(f"""# DESIGN.md — Hermes Design Style Library Default

This repository uses a two-layer design system for agents.

## Default load order

1. **Broad baseline:** read `baselines/voltagent-awesome-design-md/baseline-index.json` and the relevant `DESIGN.md` from `baselines/voltagent-awesome-design-md/design-md/`.
2. **Deep override:** if a matching local pack exists, prefer `styles/<style-id>/STYLE.md`, `tokens/`, `patterns/`, `components/capsules/`, evidence, and eval.
3. **Runtime rule:** use local files only. Do not call Mobbin, GitHub, web search, Firecrawl, browser, or external galleries at runtime to understand the style.

## Why this exists

The VoltAgent snapshot gives agents a wide default vocabulary across many brands. The local `styles/` packs are deeper: local visual evidence, source maps, component capsules, extracted DOM/CSS evidence, auth blockers, and eval gates.

## Non-cloning rule

Use DESIGN.md files as design grammar and constraints, not as permission to impersonate brands, copy logos, or reproduce source screens pixel-perfectly.

Snapshot: `VoltAgent/awesome-design-md` commit `{commit}` via fork `timsmykov/awesome-design-md`.
""", encoding='utf-8')

    print(json.dumps({'baseline_dir': str(BASELINE_DIR), 'design_md_count': meta['design_md_count'], 'commit': commit, 'mapped_packs': len(mapping_rows)}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
