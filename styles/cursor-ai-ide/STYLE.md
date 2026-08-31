# Cursor AI IDE

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

AI code editor workspace; dark IDE shell; chat/composer sidecar; files, diffs, terminal and model controls as first-class surfaces; practical developer speed over decoration

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `cursor-ai-ide`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#0b0d12; `surface`=#11141b; `panel`=#171b24; `text`=#f4f7fb; `muted`=#9aa4b2; `border`=#2a3140; `accent`=#7c3aed; `accent2`=#38bdf8.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `ai-chat-panel` — ai chat panel
- `composer-command-card` — composer command card
- `diff-review-pane` — diff review pane
- `editor-shell` — editor shell
- `file-explorer` — file explorer
- `model-selector` — model selector
- `onboarding-import-project` — onboarding import project
- `pricing-plan-grid` — pricing plan grid
- `settings-preferences` — settings preferences
- `terminal-panel` — terminal panel

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/cursor-ai-ide/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 20
- Public web pages captured: 2
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/cursor-ai-ide/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/cursor-ai-ide/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/cursor-ai-ide/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/cursor-ai-ide/eval/checklist.yaml` and `eval/failure-modes.md`.
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
