# Vercel Developer Control Plane

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `vercel-developer-control-plane`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#000000; `surface`=#0a0a0a; `panel`=#111111; `text`=#fafafa; `muted`=#a1a1aa; `border`=#27272a; `accent`=#ffffff; `accent2`=#0070f3.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `analytics-chart` — analytics chart
- `deployment-list` — deployment list
- `docs-code-block` — docs code block
- `domain-settings` — domain settings
- `environment-variable-table` — environment variable table
- `import-project-flow` — import project flow
- `logs-console` — logs console
- `pricing-plan-grid` — pricing plan grid
- `project-card` — project card
- `template-gallery` — template gallery

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/vercel-developer-control-plane/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 20
- Public web pages captured: 3
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/vercel-developer-control-plane/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/vercel-developer-control-plane/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/vercel-developer-control-plane/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/vercel-developer-control-plane/eval/checklist.yaml` and `eval/failure-modes.md`.
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
