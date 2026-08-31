# Default Agent Style Workflow

The runtime design system is a single local package: `pack/`.

## Load order

1. Read root `DESIGN.md` only to discover the pack.
2. Load `pack/DESIGN.md` and `pack/registry.json`.
3. If the task maps to one of our deep styles, load `pack/styles/<style-id>/DESIGN.md`.
4. If no deep style exists, use `pack/design-md/<brand>/DESIGN.md` from the broad VoltAgent catalog.
5. For implementation detail, use `pack/extensions/<style-id>/components/capsules/` and `pack/components/<style-id>/`.
6. Check eval/failure modes inside `pack/extensions/<style-id>/eval/` before claiming quality.

## Authority order

`pack/styles/<style-id>/DESIGN.md` is authoritative for deep styles. It includes the broad VoltAgent baseline plus Hermes extension guidance in one runtime view.

## Runtime boundary

Runtime agents must not call GitHub, Mobbin, Firecrawl, browser, or web search to understand default style. Those are build-time enrichment tools only.

## Safe use

Use the pack to adapt design grammar, not to clone logos, copy exact screens, impersonate brands, or import proprietary code as a dependency.
