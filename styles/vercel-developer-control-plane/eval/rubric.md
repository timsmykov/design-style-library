# Evaluation rubric — `vercel-developer-control-plane`

Score the generated artifact from 0-100. A usable result is 80+. A result that will be shown to users should be 90+.

## 1. Pack usage — 20 points

- 20: Uses `pack/styles/vercel-developer-control-plane/DESIGN.md`, tokens, capsules, and eval files explicitly.
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

When reviewing, name the exact local files used. If the output cannot point back to `pack/styles/vercel-developer-control-plane/DESIGN.md`, a token file, and at least one capsule, treat the style-system usage as incomplete.
