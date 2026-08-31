# Unified VoltAgent + Hermes Design Pack

## Decision

`VoltAgent/awesome-design-md` is no longer treated as a separate runtime baseline. It is the foundation inside the single Hermes runtime pack at `pack/`.

We keep the fork and source snapshot for provenance/build sync:

- Fork: `https://github.com/timsmykov/awesome-design-md`
- Upstream: `https://github.com/VoltAgent/awesome-design-md`
- Local fork clone: `/root/hermes-workspace/awesome-design-md`
- Source snapshot: `baselines/voltagent-awesome-design-md/`
- Runtime pack: `pack/`
- Server pointer: `/srv/agents/shared/style-system.md`

## Runtime model

Agents do not think in two separate systems. They load one package:

1. `pack/DESIGN.md`
2. `pack/registry.json`
3. `pack/styles/<style-id>/DESIGN.md` for deep styles
4. `pack/design-md/<brand>/DESIGN.md` for broad-only styles

## Relationship

VoltAgent gives the foundation. Hermes adds deeper local evidence, component capsules, source maps, DOM/CSS captures, auth blockers, and eval gates as extensions inside the same pack.

## Non-cloning rule

The pack is design grammar, not permission to impersonate brands or reproduce exact proprietary screens/code.
