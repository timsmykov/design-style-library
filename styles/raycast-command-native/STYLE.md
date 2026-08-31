# Raycast Command Native

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `raycast-command-native`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#0b0b10; `surface`=#15151c; `panel`=#1d1d27; `text`=#f8fafc; `muted`=#a1a1aa; `border`=#2b2b36; `accent`=#ff6363; `accent2`=#8b5cf6.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `ai-action-panel` — ai action panel
- `command-palette` — command palette
- `empty-state-command` — empty state command
- `extension-card-grid` — extension card grid
- `onboarding-install` — onboarding install
- `preferences-modal` — preferences modal
- `pricing-card` — pricing card
- `search-results-list` — search results list
- `shortcut-row` — shortcut row
- `team-admin-table` — team admin table

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/raycast-command-native/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 20
- Public web pages captured: 2
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/raycast-command-native/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/raycast-command-native/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/raycast-command-native/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/raycast-command-native/eval/checklist.yaml` and `eval/failure-modes.md`.
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
