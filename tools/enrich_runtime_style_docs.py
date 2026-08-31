#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACK_REGISTRY = ROOT / "pack" / "registry.json"

THRESHOLDS = {
    "STYLE.md": 2500,
    "agent-contract.md": 900,
    "components/component-atlas.md": 1800,
    "eval/checklist.yaml": 900,
    "eval/rubric.md": 1200,
    "eval/failure-modes.md": 900,
    "evidence/observations.yaml": 900,
    "patterns/index.md": 900,
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write_if_thin(path: Path, rel: str, body: str, force: bool = False) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    current = read(path)
    min_len = THRESHOLDS.get(rel, 0)
    if force or len(current) < min_len:
        path.write_text(body.rstrip() + "\n", encoding="utf-8")
        return True
    return False


def titleize(slug: str) -> str:
    return " ".join(part.upper() if part in {"ai", "api", "ide"} else part.capitalize() for part in slug.replace("/", "-").split("-"))


def load_json(path: Path) -> Any:
    try:
        return json.loads(read(path))
    except Exception:  # noqa: BLE001
        return {}


def parse_style_formula(text: str, sid: str) -> str:
    m = re.search(r"## Style formula\s+(.+?)(?:\n## |\Z)", text, re.S | re.I)
    if m:
        return " ".join(m.group(1).split())
    m = re.search(r"claim:\s*(.+)", read(ROOT / "styles" / sid / "evidence" / "observations.yaml"))
    if m:
        return m.group(1).strip()
    return f"Evidence-backed {titleize(sid)} style grammar derived from local tokens, component capsules, and captured visual corpus."


def component_entries(style_dir: Path) -> list[dict[str, Any]]:
    path = style_dir / "components" / "component-index.jsonl"
    entries = []
    for line in read(path).splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except Exception:  # noqa: BLE001
            continue
        entries.append(item)
    if entries:
        return entries
    for cap in sorted((style_dir / "components" / "capsules").glob("*.md")):
        entries.append({"component_id": cap.stem, "title": titleize(cap.stem), "body_excerpt": read(cap)[:500]})
    return entries


def token_summary(tokens: dict[str, Any]) -> tuple[str, str, str]:
    color = tokens.get("color") or tokens.get("colors") or {}
    typography = tokens.get("typography") or {}
    spacing = tokens.get("spacing") or {}
    radius = tokens.get("radius") or {}
    color_bits = []
    if isinstance(color, dict):
        for key, val in list(color.items())[:10]:
            if isinstance(val, dict):
                value = val.get("value") or val.get("hex") or val.get("role") or ""
            else:
                value = val
            color_bits.append(f"`{key}`={value}")
    typo_bits = []
    if isinstance(typography, dict):
        for key, val in list(typography.items())[:6]:
            if isinstance(val, dict):
                fam = val.get("family") or val.get("fontFamily") or val.get("usage") or ""
            else:
                fam = val
            typo_bits.append(f"`{key}`={fam}")
    system_bits = []
    if spacing:
        system_bits.append("spacing scale present")
    if radius:
        system_bits.append("radius scale present")
    return "; ".join(color_bits) or "token colors in `tokens/tokens.json`", "; ".join(typo_bits) or "type roles in `tokens/tokens.json`", ", ".join(system_bits) or "spacing/radius roles in `tokens/tokens.json`"


def counts(style_dir: Path) -> dict[str, int]:
    def c(path: str, patterns: tuple[str, ...]) -> int:
        base = style_dir / path
        return sum(1 for pat in patterns for _ in base.glob(pat)) if base.exists() else 0
    return {
        "screens": c("evidence/mobbin/screens", ("*.webp", "*.png", "*.jpg")),
        "sections": c("evidence/mobbin/sections", ("*.webp", "*.png", "*.jpg")),
        "flows": c("evidence/mobbin/flows", ("*.webp", "*.png", "*.jpg")),
        "web_pages": c("evidence/web/pages", ("*.html", "*.md", "*.json")),
        "auth": c("evidence/authenticated", ("**/*.png", "**/*.webp", "**/*.jpg")),
    }


def style_md(sid: str, display: str, formula: str, tokens: dict[str, Any], comps: list[dict[str, Any]], cnt: dict[str, int]) -> str:
    colors, typo, systems = token_summary(tokens)
    component_list = "\n".join(f"- `{c.get('component_id')}` — {c.get('aliases', [titleize(c.get('component_id','component'))])[0] if c.get('aliases') else titleize(c.get('component_id','component'))}" for c in comps[:14])
    return f"""# {display}

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

{formula}

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `{sid}`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: {colors}.
- Use the typography roles deliberately. Type anchors: {typo}.
- Respect the shape and density system: {systems}.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

{component_list}

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/{sid}/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: {cnt['screens']}
- Mobbin sections: {cnt['sections']}
- Mobbin flow previews: {cnt['flows']}
- Public web pages captured: {cnt['web_pages']}
- Authenticated screenshots: {cnt['auth']}

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/{sid}/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/{sid}/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/{sid}/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/{sid}/eval/checklist.yaml` and `eval/failure-modes.md`.
6. If the output feels generic, increase fidelity through component structure and hierarchy, not by copying exact source screens.

## Do

- Use local tokens and capsules as the first source of truth.
- Make state, status, and user action obvious.
- Keep density and spacing consistent across related surfaces.
- Use evidence-backed component vocabulary when describing or implementing the UI.

## Do not

- Do not call web search, GitHub, Mobbin, browser/CDP, or external services at runtime for style guidance.
- Do not clone exact production screens, logos, copy, private account data, or proprietary code.
- Do not mix this style with another pack unless the user explicitly asks for a hybrid.
- Do not substitute a moodboard description for component-level structure.
"""


def contract_md(sid: str, display: str) -> str:
    return f"""# Agent contract — {display}

This contract tells an agent how to use `{sid}` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/{sid}/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/{sid}/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/{sid}/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/{sid}/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/{sid}/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/{sid}/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/{sid}/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

## Authority rule

The deep Hermes extension overrides the broad VoltAgent baseline whenever they differ. The baseline provides vocabulary; this extension provides implementation constraints, local evidence, component structure, and failure modes.

## Runtime boundary

Use local files only. GitHub, Mobbin, Firecrawl, Browser/CDP, Playwright, and authenticated sessions are build-time enrichment lanes. Runtime style use should remain offline, deterministic, and repo-first.

## Generation protocol

- Identify the product job and information hierarchy before styling.
- Select the nearest component capsule by semantic job, not by visual decoration.
- Apply tokens exactly where possible; when adapting, keep role semantics stable.
- Preserve accessibility basics: readable contrast, usable target sizes, clear focus/selected/error states.
- State uncertainty if the requested surface has no matching capsule, then compose from the closest primitives.

## Review protocol

A result is acceptable only if it passes the local eval layer and can name which capsules/tokens shaped it. If it cannot cite local pack paths, it did not really use the style system.

## Safety

Adapt style grammar. Do not impersonate the brand, reuse logos, reproduce exact screens, copy private data, or import proprietary source code.
"""


def atlas_md(sid: str, comps: list[dict[str, Any]], formula: str) -> str:
    lines = ["# Component atlas", "", f"Runtime component atlas for `{sid}`.", "", "Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.", ""]
    for c in comps:
        cid = c.get("component_id", "component")
        title = c.get("title") or titleize(cid)
        aliases = ", ".join(c.get("aliases", [])) if isinstance(c.get("aliases"), list) else titleize(cid)
        excerpt = c.get("body_excerpt", "")
        evidence_count = len(c.get("evidence_paths", [])) + len(c.get("extracted_paths", []))
        lines.extend([
            f"## `{cid}` — {title}",
            "",
            f"Use when: the artifact needs `{aliases}` behavior, layout, or decision structure.",
            f"Capsule: `components/capsules/{cid}.md`",
            f"Semantic slice: `pack/components/{sid}/{cid}.md`",
            f"Evidence links recorded: `{evidence_count}` index path groups; see local source map and extracted folders for detail.",
            "",
            "Design job:",
            f"- Preserve this style formula: {formula}",
            "- Keep the component's primary object obvious before adding decoration.",
            "- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.",
            "- Adapt the grammar to the new product context; do not clone exact evidence screens.",
            "",
            "Implementation notes:",
            "- Start with semantic structure and states.",
            "- Add controls, status, metadata, and supporting copy in that order.",
            "- Check responsive behavior and empty/error/loading states when relevant.",
            "",
        ])
        if excerpt:
            first = " ".join(excerpt.split())[:500]
            lines.extend(["Evidence excerpt:", f"> {first}", ""])
    return "\n".join(lines)


def checklist_yaml(sid: str) -> str:
    return f"""style_id: {sid}
version: 1
runtime_quality_gate:
  load_order:
    - check: loaded_unified_design_entry
      pass_if: "pack/styles/{sid}/DESIGN.md was used before generation"
    - check: loaded_tokens
      pass_if: "tokens/tokens.json or css-vars.css shaped concrete color/type/spacing choices"
    - check: loaded_component_capsule
      pass_if: "at least one local component capsule was selected by semantic job"
  composition:
    - check: hierarchy_preserved
      pass_if: "primary object, metadata, controls, and ambient decoration are visually separable"
    - check: density_matches_pack
      pass_if: "spacing, radii, and surface density match the local style formula"
    - check: states_present
      pass_if: "interactive surfaces include selected/hover/focus/error/loading/empty states when relevant"
    - check: responsive_structure
      pass_if: "layout can compress without losing primary action or status clarity"
  evidence_use:
    - check: local_only
      pass_if: "no runtime web, GitHub, Mobbin, browser/CDP, or authenticated service dependency was used"
    - check: provenance_available
      pass_if: "chosen components can point to capsule/source-map/evidence paths inside the pack"
  safety:
    - check: non_cloning
      pass_if: "output adapts style grammar without copying exact screens, logos, private data, or proprietary code"
    - check: brand_distance
      pass_if: "artifact fits the requested product, not an impersonation of the reference brand"
  final_answer:
    - check: cite_pack_paths
      pass_if: "agent can name the style entry, tokens, capsules, and eval paths it used"
"""


def rubric_md(sid: str) -> str:
    return f"""# Evaluation rubric — `{sid}`

Score the generated artifact from 0-100. A usable result is 80+. A result that will be shown to users should be 90+.

## 1. Pack usage — 20 points

- 20: Uses `pack/styles/{sid}/DESIGN.md`, tokens, capsules, and eval files explicitly.
- 14: Uses the unified DESIGN.md and tokens, but component selection is weak.
- 8: Uses only broad mood/style language.
- 0: Does not cite or follow local pack files.

## 2. Component fit — 20 points

- 20: Chooses the closest capsule by semantic job and preserves its structure.
- 14: Uses a plausible capsule but misses some states or metadata.
- 8: Surface looks visually related but component behavior is generic.
- 0: No recognizable local component grammar.

## 3. Visual fidelity — 20 points

- 20: Token roles, typography, density, hierarchy, and surfaces match the pack.
- 14: Major visual language is right, with minor spacing/type/radius drift.
- 8: Some colors or styling match, but hierarchy and density drift.
- 0: Generic UI with a copied palette.

## 4. Product clarity — 15 points

- 15: Primary user job and action path are obvious.
- 10: Main task is visible but secondary controls compete.
- 5: Decorative fidelity harms comprehension.
- 0: User cannot tell what to do.

## 5. States and resilience — 10 points

- 10: Handles empty, loading, error, selected, focus, and responsive states where relevant.
- 6: Covers the main state and one or two secondary states.
- 3: Mostly static mockup.
- 0: Broken or inaccessible state behavior.

## 6. Safety and originality — 15 points

- 15: Adapts grammar without brand impersonation, exact screen cloning, logos, private data, or proprietary code.
- 10: Mostly safe, but too close to reference layout or copy.
- 5: Looks like a clone with small substitutions.
- 0: Uses protected assets/private data or misrepresents brand ownership.

## Required reviewer note

When reviewing, name the exact local files used. If the output cannot point back to `pack/styles/{sid}/DESIGN.md`, a token file, and at least one capsule, treat the style-system usage as incomplete.
"""


def failure_modes_md(sid: str) -> str:
    return f"""# Failure modes — `{sid}`

## Generic moodboard output

Symptom: the result uses a few colors from the pack but ignores component structure, states, and hierarchy.

Fix: reload `components/component-atlas.md`, choose the closest capsule, and rebuild the layout around the component's semantic job.

## Exact screen cloning

Symptom: the output copies a reference screen too literally, including brand-specific layout, copy, logo placement, or private-data shapes.

Fix: preserve grammar and hierarchy, but change information architecture to fit the user's actual product.

## Token drift

Symptom: colors, radius, shadows, or type sizes are invented because they "feel close".

Fix: use `tokens/tokens.json` and `tokens/css-vars.css`; when a new value is needed, derive it from an existing role and explain the adaptation.

## Component mismatch

Symptom: a pricing card is used for a settings table, a command palette is used for a dashboard, or a gallery pattern is used where a status list is needed.

Fix: select capsules by job-to-be-done. If no exact capsule exists, combine two closest capsules and say which parts came from each.

## Missing states

Symptom: the main mockup looks correct but selected, focus, error, loading, empty, permission, and responsive states are absent.

Fix: use the checklist and add the states that matter for the requested user flow.

## Runtime external dependency

Symptom: the agent tries to open Mobbin, GitHub, browser/CDP, or web search to understand the style during normal generation.

Fix: stop and use local `pack/` files. External tools are build-time enrichment only.

## Brand impersonation

Symptom: the artifact appears to be an official screen from the reference brand or uses their logo/private interface details.

Fix: remove brand-specific marks and exact-copy details; keep only transferable design grammar.
"""


def observations_yaml(sid: str, formula: str, tokens: dict[str, Any], comps: list[dict[str, Any]], cnt: dict[str, int]) -> str:
    colors, typo, systems = token_summary(tokens)
    comp_ids = [c.get("component_id", "component") for c in comps]
    return f"""observations:
  - id: style-formula
    claim: "{formula.replace('"', '\\"')}"
    confidence: medium
    evidence: STYLE.md plus local visual corpus
  - id: local-corpus
    claim: "Local visual corpus contains {cnt['screens']} screens, {cnt['sections']} sections, {cnt['flows']} flow previews, {cnt['web_pages']} public web captures, and {cnt['auth']} authenticated screenshots."
    confidence: high
    evidence: evidence/ directories and source-map files
  - id: token-system
    claim: "Token system exposes color, typography, spacing, and radius roles for implementation. Color anchors: {colors.replace('"', '\\"')}. Type anchors: {typo.replace('"', '\\"')}. Structural anchors: {systems.replace('"', '\\"')}."
    confidence: high
    evidence: tokens/tokens.json and tokens/css-vars.css
  - id: component-grammar
    claim: "Component grammar is normalized into {len(comp_ids)} capsules: {', '.join(comp_ids)}."
    confidence: high
    evidence: components/component-index.jsonl and components/capsules/
  - id: runtime-boundary
    claim: "Runtime agents can use this style offline from pack files only; external tools are build-time enrichment lanes."
    confidence: high
    evidence: agent-contract.md and unified pack DESIGN.md
"""


def patterns_md(sid: str, comps: list[dict[str, Any]], formula: str) -> str:
    lines = ["# Patterns", "", f"Reusable runtime patterns for `{sid}`.", "", f"Style formula: {formula}", "", "## Selection rule", "", "Pick patterns by semantic job first, visual similarity second. Use the corresponding capsule when implementing.", ""]
    for c in comps:
        cid = c.get("component_id", "component")
        label = titleize(cid)
        lines.extend([
            f"## {label}",
            "",
            f"Capsule: `components/capsules/{cid}.md`",
            "",
            "Use when the artifact needs this job-to-be-done, not merely when the reference image looks similar.",
            "Keep hierarchy, state semantics, density, and token roles aligned with the capsule. Adapt content and layout to the user's product context.",
            "",
        ])
    lines.extend([
        "## Cross-pattern rules",
        "",
        "- Navigation and shell patterns should establish orientation before content density increases.",
        "- Data/status patterns should make state legible before showing secondary metadata.",
        "- Marketing/pricing patterns should keep proof, action, and comparison cleanly separated.",
        "- Settings/admin patterns should privilege scanability, defaults, and clear destructive-action treatment.",
    ])
    return "\n".join(lines)


def main() -> int:
    reg = json.loads(read(PACK_REGISTRY))
    changed: list[str] = []
    for entry in reg.get("styles", []):
        sid = entry["id"]
        style_dir = ROOT / "styles" / sid
        if not style_dir.exists():
            continue
        display = entry.get("name") or titleize(sid)
        original_style = read(style_dir / "STYLE.md")
        formula = parse_style_formula(original_style, sid)
        tokens = load_json(style_dir / "tokens" / "tokens.json")
        comps = component_entries(style_dir)
        cnt = counts(style_dir)
        candidates = {
            "STYLE.md": style_md(sid, display, formula, tokens, comps, cnt),
            "agent-contract.md": contract_md(sid, display),
            "components/component-atlas.md": atlas_md(sid, comps, formula),
            "eval/checklist.yaml": checklist_yaml(sid),
            "eval/rubric.md": rubric_md(sid),
            "eval/failure-modes.md": failure_modes_md(sid),
            "evidence/observations.yaml": observations_yaml(sid, formula, tokens, comps, cnt),
            "patterns/index.md": patterns_md(sid, comps, formula),
        }
        for rel, body in candidates.items():
            path = style_dir / rel
            before = read(path)
            if write_if_thin(path, rel, body):
                changed.append(f"{sid}/{rel}: {len(before)} -> {len(body)}")
    print(f"changed={len(changed)}")
    for item in changed:
        print(item)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
