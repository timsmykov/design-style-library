#!/usr/bin/env python3
"""Run remaining no-login style-pack waves with at most two concurrent workers.

This is a parent-side supervisor for the design-style-library project. It launches
Hermes CLI workers in isolated git worktrees, waits for each two-worker wave,
verifies outputs, merges successful branches into main, and closes Kanban cards.

It intentionally keeps parallelism at 2 to avoid overlapping global writes and
Mobbin/CDP load spikes.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import textwrap
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path('/root/hermes-workspace/design-style-library')
WORKTREES = Path('/root/hermes-workspace/design-style-library-worktrees')
PROFILE_CONFIG = Path('/root/.hermes/profiles/orchestrator/config.yaml')
BOARD = 'design-style-library'
LOG_ROOT = ROOT / 'orchestration' / 'waves' / 'logs'
PROMPT_ROOT = ROOT / 'orchestration' / 'waves' / 'generated-worker-prompts'

@dataclass(frozen=True)
class Target:
    wave: str
    card: str
    style_id: str
    name: str
    category: str
    public_urls: tuple[str, ...]
    screens_query: str
    sections_query: str
    flows_query: str

WAVES: list[list[Target]] = [
    [
        Target('no-login-wave-02', 't_a0b0b77b', 'linear-operational-workspace', 'Linear Operational Workspace', 'operational_workspace', ('https://linear.app/', 'https://linear.app/pricing'), 'Linear issues projects cycles roadmap command menu settings web app', 'Linear website product features pricing customer stories changelog', 'Linear onboarding create workspace invite team create issue upgrade settings'),
        Target('no-login-wave-02', 't_339d2d7a', 'stripe-trust-commerce', 'Stripe Trust Commerce', 'payments_trust', ('https://stripe.com/', 'https://stripe.com/pricing'), 'Stripe dashboard payments checkout invoices balances pricing settings web app', 'Stripe website pricing payments checkout cards trust compliance enterprise docs', 'Stripe onboarding business verification checkout payment subscription invoice payout settings'),
    ],
    [
        Target('no-login-wave-03', 't_eb7a2337', 'vercel-developer-control-plane', 'Vercel Developer Control Plane', 'developer_control_plane', ('https://vercel.com/', 'https://vercel.com/pricing', 'https://vercel.com/docs'), 'Vercel dashboard deployments projects logs environment variables domains analytics settings', 'Vercel website developer platform pricing docs templates enterprise feature cards', 'Vercel onboarding import project deploy configure domain environment variables upgrade'),
        Target('no-login-wave-03', 't_b8c24881', 'cursor-ai-ide', 'Cursor AI IDE', 'developer_control_plane', ('https://cursor.com/', 'https://cursor.com/pricing'), 'Cursor AI IDE code editor chat composer sidebar agents settings model selector terminal', 'Cursor website AI code editor pricing features enterprise docs developer cards', 'Cursor onboarding install import project chat with code upgrade settings model selection'),
    ],
    [
        Target('no-login-wave-04', 't_89a4d1b3', 'raycast-command-native', 'Raycast Command Native', 'command_native_utility', ('https://www.raycast.com/', 'https://www.raycast.com/pricing'), 'Raycast command palette extensions AI snippets settings preferences search actions', 'Raycast website command palette AI extensions teams pricing feature cards', 'Raycast onboarding install extension command palette AI setup preferences upgrade'),
        Target('no-login-wave-04', 't_9bf98322', 'figma-collaborative-canvas', 'Figma Collaborative Canvas', 'collaborative_canvas', ('https://www.figma.com/', 'https://www.figma.com/pricing/'), 'Figma editor canvas layers properties inspector comments multiplayer design file toolbar', 'Figma website design collaboration FigJam pricing enterprise feature cards', 'Figma onboarding create team file invite comment prototype upgrade settings'),
    ],
    [
        Target('no-login-wave-05', 't_5c210f38', 'metamask-crypto-wallet-trust', 'MetaMask / Crypto Wallet Trust', 'crypto_wallet_trust', ('https://metamask.io/', 'https://metamask.io/swaps/'), 'MetaMask wallet send receive swap tokens network gas risk warning portfolio browser extension', 'MetaMask website wallet swap portfolio security developer product cards', 'MetaMask onboarding create wallet import seed phrase send token swap connect dapp risk warning'),
        Target('no-login-wave-05', 't_df158a9c', 'airbnb-marketplace-warm-consumer', 'Airbnb Marketplace Warm Consumer', 'marketplace_consumer', ('https://www.airbnb.com/',), 'Airbnb search listing detail booking checkout filters map reviews host profile web app', 'Airbnb website home booking listing cards travel categories trust host sections', 'Airbnb search stay filter listing detail reserve checkout payment cancellation host onboarding'),
    ],
]


def run(cmd: list[str] | str, *, cwd: Path = ROOT, check: bool = True, stdout=None, stderr=None, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), shell=isinstance(cmd, str), text=True, check=check, stdout=stdout, stderr=stderr, timeout=timeout)


def out(cmd: list[str] | str, *, cwd: Path = ROOT, check: bool = True) -> str:
    return run(cmd, cwd=cwd, check=check, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout


def kanban(args: list[str], *, check: bool = False) -> str:
    cmd = ['hermes', 'kanban', '--board', BOARD] + args
    try:
        return out(cmd, check=check)
    except subprocess.CalledProcessError as e:
        return e.stdout or ''


def ensure_clean_main() -> None:
    run(['git', 'status', '--short'], cwd=ROOT, stdout=subprocess.PIPE)
    status = out(['git', 'status', '--short'], cwd=ROOT).strip()
    if status:
        raise SystemExit(f'main worktree not clean before wave start:\n{status}')


def toggle_consensus(enabled: bool) -> None:
    s = PROFILE_CONFIG.read_text()
    old = '  consensus:\n    url: https://mcp.consensus.app/mcp\n    auth: oauth\n    enabled: true\n'
    new = '  consensus:\n    url: https://mcp.consensus.app/mcp\n    auth: oauth\n    enabled: false\n'
    if enabled:
        if new in s:
            PROFILE_CONFIG.write_text(s.replace(new, old, 1))
    else:
        if old in s:
            PROFILE_CONFIG.write_text(s.replace(old, new, 1))


def create_prompt(t: Target) -> Path:
    PROMPT_ROOT.mkdir(parents=True, exist_ok=True)
    public = '\n'.join(f'- {u}' for u in t.public_urls)
    prompt = f"""# Worker Prompt — {t.name}

Ты субагент Hermes. Итоговый self-report дай по-русски.

Durable coordinates:
- project_id: design-style-library
- board: design-style-library
- wave_id: {t.wave}
- card_id: {t.card}
- component: {t.style_id}
- owner_mode: implementation-worker

## Рабочее место

- Worktree/root: `/root/hermes-workspace/design-style-library-worktrees/{t.style_id}`
- Branch: `style/{t.style_id}-{t.wave}`
- Target pack: `styles/{t.style_id}/`
- Generated Gbrain slices: `gbrain_export/components/{t.style_id}/`

## Source docs

Read in the worktree:
- `docs/no-login-style-factory.md`
- `extraction-plans/no-login-batch-01.yaml`
- `docs/style-pack-contract.md`
- `docs/extraction-pipeline.md`
- `docs/component-retrieval-architecture.md`
- use `styles/anthropic-claude/`, `styles/perplexity-answer-engine/`, and `styles/notion-document-os/` as structural references only; do not edit them.

## Goal

Build a draft/reference no-login style pack for **{t.name}**. Target the same standard as the current Perplexity/Notion packs: evidence-backed, componentized, offline-usable draft pack.

## Inputs

Category: `{t.category}`

Public URLs:
{public}

Mobbin queries:
- screens: {t.screens_query}
- sections: {t.sections_query}
- flows: {t.flows_query}

## Required work

1. Use Mobbin MCP if visible (`mcp_mobbin_search_screens`, `mcp_mobbin_search_sections`, `mcp_mobbin_search_flows`). If it is not visible, run/inspect the Mobbin smoke from `senior-ui-reference-research`; report a real blocker, do not fabricate evidence.
2. Save local screenshots/sections/flows under `styles/{t.style_id}/evidence/mobbin/...`. Target 80+ local refs if feasible; truth and relevance beat quota.
3. Build `evidence/source-map/mobbin-source-map.jsonl` and `.csv` covering every local ref with local path, source type, Mobbin URL/image URL when available, OCR/palette/layout facts where available, component match, implementation status.
4. Build screenshot-derived component facts under `components/extracted/from-mobbin-screenshots/<component>/`.
5. Capture public no-login web evidence for the URLs above using available Firecrawl/browser/CDP/tools. Save DOM/CSS/computed/screenshots under `evidence/web/...` or `evidence/web/original-code/` consistently. Keep production CSS as evidence only, not runtime dependency.
6. Create all required pack files: `manifest.yaml`, `STYLE.md`, `agent-contract.md`, `evidence/sources.yaml`, `evidence/observations.yaml`, `dna/*`, `tokens/*`, `patterns/index.md`, `components/component-atlas.md`, `components/capsules/*.md`, `eval/*`.
7. Run `./tools/component_index.py .` if present and ensure `gbrain_export/components/{t.style_id}/` exists.
8. Record `AUTH_BLOCKERS.md` for any login-only/app-only surfaces.
9. Ensure required evidence placeholder dirs exist even if empty: `evidence/web/pages`, `evidence/web/css`, `evidence/web/computed`, `evidence/web/fonts`.
10. Run `./tools/stylepack_verify.py .` and JSON/JSONL sanity checks.
11. Commit changes on your branch. Do not merge to `main`.

## Constraints

Allowed paths:
- `styles/{t.style_id}/`
- `gbrain_export/components/{t.style_id}/`

Avoid global/shared edits. Forbidden:
- login/OAuth/credentials;
- modifying Anthropic/Perplexity/Notion/other packs;
- gateway lifecycle commands;
- printing secrets;
- changing schemas/tools unless you only write a proposed patch note.

## Final self-report schema

Return:
- status: completed | partial | blocked | failed
- branch
- commit_sha
- files_changed
- counts: mobbin_refs, source_map_rows, components, public_pages, cdp_targets
- commands_run
- verification
- blockers
- parent_must_verify
"""
    p = PROMPT_ROOT / f'{t.style_id}.md'
    p.write_text(prompt)
    return p


def create_wave_ledger(wave: str, targets: list[Target]) -> None:
    p = ROOT / 'orchestration' / 'waves' / f'{wave}.md'
    rows = '\n'.join(f'| `{t.card}` | `{t.style_id}` | `/root/hermes-workspace/design-style-library-worktrees/{t.style_id}` | `style/{t.style_id}-{wave}` |' for t in targets)
    p.write_text(f"""# {wave}

Status: supervisor-managed wave, max 2 concurrent workers.

| Card | Style | Worktree | Branch |
|---|---|---|---|
{rows}

Acceptance: each worker creates an evidence-backed no-login draft/reference style pack, commits on its branch, parent verifies `stylepack_verify.py`, source-map counts, component capsules, and merges successful branches into `main`.
""")


def setup_worktree(t: Target) -> None:
    branch = f'style/{t.style_id}-{t.wave}'
    wt = WORKTREES / t.style_id
    if wt.exists() and not (wt / '.git').exists():
        raise SystemExit(f'worktree path exists but is not git worktree: {wt}')
    if not wt.exists():
        run(['git', 'worktree', 'add', '-B', branch, str(wt), 'HEAD'], cwd=ROOT)
    else:
        run(['git', 'fetch', '--all', '--prune'], cwd=wt, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        run(['git', 'checkout', '-B', branch, 'HEAD'], cwd=wt)
    # Worktree starts from the main HEAD at time of creation/update.
    # Ensure no copied prompt dirs from earlier manual launches remain dirty.
    if (wt / 'orchestration').exists():
        shutil.rmtree(wt / 'orchestration')


def claim_task(t: Target) -> None:
    kanban(['promote', t.card, f'{t.wave} supervisor launch'], check=False)
    kanban(['claim', t.card], check=False)
    kanban(['heartbeat', t.card, '--note', f'{t.wave}: launching worker in isolated worktree /root/hermes-workspace/design-style-library-worktrees/{t.style_id}. Parent verification required before merge.'], check=False)


def launch_worker(t: Target, prompt_path: Path, log_path: Path) -> subprocess.Popen:
    wt = WORKTREES / t.style_id
    cmd = [
        'hermes', 'chat', '-Q', '--yolo', '--max-turns', '140',
        '--toolsets', 'terminal,file,browser,vision,mobbin,firecrawl',
        '--query', prompt_path.read_text(),
    ]
    env = os.environ.copy()
    env['HERMES_ACCEPT_HOOKS'] = '1'
    log_f = log_path.open('w')
    proc = subprocess.Popen(cmd, cwd=str(wt), env=env, stdout=log_f, stderr=subprocess.STDOUT, text=True)
    # Keep file handle attached via proc object for lifetime.
    proc._hermes_log_file = log_f  # type: ignore[attr-defined]
    return proc


def ensure_required_web_dirs(t: Target) -> None:
    base = WORKTREES / t.style_id / 'styles' / t.style_id / 'evidence' / 'web'
    for sub in ['pages', 'css', 'computed', 'fonts']:
        d = base / sub
        d.mkdir(parents=True, exist_ok=True)
        keep = d / '.gitkeep'
        if not any(d.iterdir()):
            keep.touch()


def post_worker_fix_and_verify(t: Target) -> dict:
    wt = WORKTREES / t.style_id
    ensure_required_web_dirs(t)
    run(['git', 'add', f'styles/{t.style_id}', f'gbrain_export/components/{t.style_id}'], cwd=wt, check=False)
    status = out(['git', 'status', '--short'], cwd=wt).strip()
    # If worker left useful uncommitted changes, commit them before verification/merge.
    if status:
        run(['git', 'commit', '-m', f'Finalize {t.name} style pack'], cwd=wt, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Verify.
    shutil.rmtree(wt / 'gbrain_export' / 'shared', ignore_errors=True)
    verify = out(['./tools/stylepack_verify.py', '.'], cwd=wt, check=True)
    style = wt / 'styles' / t.style_id
    sm = style / 'evidence' / 'source-map' / 'mobbin-source-map.jsonl'
    imgs = [p for p in (style / 'evidence' / 'mobbin').rglob('*') if p.suffix.lower() in {'.webp', '.png', '.jpg', '.jpeg'}] if (style / 'evidence' / 'mobbin').exists() else []
    caps = list((style / 'components' / 'capsules').glob('*.md')) if (style / 'components' / 'capsules').exists() else []
    cdp_idx = style / 'components' / 'extracted' / 'browser-cdp' / 'browser-cdp-index.json'
    public_idx = style / 'evidence' / 'web' / 'original-code' / 'public-code-index.json'
    rows = sum(1 for _ in sm.open()) if sm.exists() else 0
    head = out(['git', 'rev-parse', '--short', 'HEAD'], cwd=wt).strip()
    return {'verify': verify.strip(), 'rows': rows, 'images': len(imgs), 'capsules': len(caps), 'cdp': cdp_idx.exists(), 'public': public_idx.exists(), 'head': head}


def merge_target(t: Target, metrics: dict) -> None:
    branch = f'style/{t.style_id}-{t.wave}'
    run(['git', 'merge', '--no-ff', branch, '-m', f'Merge {t.name} style pack'], cwd=ROOT)
    shutil.rmtree(ROOT / 'gbrain_export' / 'shared', ignore_errors=True)
    out(['./tools/stylepack_verify.py', '.'], cwd=ROOT, check=True)
    result = f"Completed and parent-verified in {t.wave}. Merged {branch} into main. Evidence: {metrics['images']} local refs, {metrics['rows']} source-map rows, {metrics['capsules']} component capsules, public_code_index={metrics['public']}, cdp_index={metrics['cdp']}, verify={metrics['verify']}, branch_head={metrics['head']}."
    kanban(['complete', t.card, '--result', result], check=False)


def commit_orchestration_files() -> None:
    run(['git', 'add', 'orchestration/waves'], cwd=ROOT)
    status = out(['git', 'status', '--short'], cwd=ROOT).strip()
    if status:
        run(['git', 'commit', '-m', 'Add remaining no-login wave orchestration'], cwd=ROOT)


def main() -> int:
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    WORKTREES.mkdir(parents=True, exist_ok=True)
    ensure_clean_main()
    for wave_targets in WAVES:
        wave = wave_targets[0].wave
        print(f'=== {wave}: setup ===', flush=True)
        create_wave_ledger(wave, wave_targets)
        prompts = {t.style_id: create_prompt(t) for t in wave_targets}
        commit_orchestration_files()
        for t in wave_targets:
            setup_worktree(t)
            claim_task(t)
        print(f'=== {wave}: launch ===', flush=True)
        toggle_consensus(False)
        try:
            procs = {}
            for t in wave_targets:
                log_path = LOG_ROOT / f'{t.wave}-{t.style_id}.log'
                p = launch_worker(t, prompts[t.style_id], log_path)
                procs[t.style_id] = (t, p, log_path)
                kanban(['heartbeat', t.card, '--note', f'{wave}: worker process pid={p.pid}, log={log_path}.'], check=False)
        finally:
            # Restore profile config immediately after process startup; workers keep their startup snapshot.
            toggle_consensus(True)
        failed: list[tuple[Target, str]] = []
        for style_id, (t, p, log_path) in procs.items():
            rc = p.wait()
            try:
                p._hermes_log_file.close()  # type: ignore[attr-defined]
            except Exception:
                pass
            print(f'{wave}: {t.style_id} exited rc={rc} log={log_path}', flush=True)
            if rc != 0:
                failed.append((t, f'worker exited {rc}; see {log_path}'))
                kanban(['block', t.card, '--reason', f'Worker exited {rc}; log={log_path}'], check=False)
        # Verify and merge successful worker branches sequentially.
        for t in wave_targets:
            if any(x.card == t.card for x, _ in failed):
                continue
            try:
                metrics = post_worker_fix_and_verify(t)
                merge_target(t, metrics)
                print(f'{wave}: merged {t.style_id}: {metrics}', flush=True)
            except Exception as e:
                failed.append((t, f'parent verification/merge failed: {e}'))
                kanban(['block', t.card, '--reason', f'{wave}: parent verification/merge failed: {e}'], check=False)
                print(f'ERROR {wave} {t.style_id}: {e}', flush=True)
        # Keep main clean before next wave.
        shutil.rmtree(ROOT / 'gbrain_export' / 'shared', ignore_errors=True)
        status = out(['git', 'status', '--short'], cwd=ROOT).strip()
        if status:
            print(f'WARNING main dirty after {wave}:\n{status}', flush=True)
        if failed:
            print(f'{wave}: failures: {failed}', flush=True)
            # Continue to next independent wave only if main is clean; failed cards are blocked.
        print(f'=== {wave}: done ===', flush=True)
    print('=== all remaining waves attempted ===', flush=True)
    print(out(['git', 'status', '--short'], cwd=ROOT), flush=True)
    print(out(['git', 'log', '--oneline', '-12'], cwd=ROOT), flush=True)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
