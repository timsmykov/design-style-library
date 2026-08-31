# DESIGN.md — Hermes Unified Design Pack Default

Agents should use `pack/` as one consolidated local design package.

## Runtime entrypoint

Start at:

1. `pack/DESIGN.md`
2. `pack/registry.json`
3. `pack/styles/<style-id>/DESIGN.md` when a deep style exists
4. `pack/design-md/<brand>/DESIGN.md` for broad styles without a deep extension

## What is inside

`pack/` is a fork-based expansion of `VoltAgent/awesome-design-md`:

- the VoltAgent catalog is the broad foundation;
- Hermes deep style work is the extension/override layer inside the same pack;
- component slices and deep source files are exposed under the pack via local links.

## Authority

Deep Hermes style entries in `pack/styles/<style-id>/DESIGN.md` override broad baseline guidance. Treat `baselines/` and `styles/` as source/provenance/build locations; treat `pack/` as the runtime product.

## Runtime boundary

Use local files only. Do not call GitHub, Mobbin, Firecrawl, browser/CDP, or external galleries at runtime to understand style.

## Non-cloning rule

Use style grammar and implementation constraints, not brand impersonation, copied logos, exact screen cloning, private data, or proprietary source code.
