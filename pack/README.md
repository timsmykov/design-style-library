# Hermes Unified Design Pack

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
