# Baselines

This directory stores broad DESIGN.md baselines used by runtime agents before selecting a deeper local style pack.

## Default baseline

- Source: `VoltAgent/awesome-design-md`
- Local fork: `timsmykov/awesome-design-md`
- Snapshot path: `baselines/voltagent-awesome-design-md/`
- Upstream commit: `664b3e78fd1a298ba11973822da988483256d4b4`
- License: MIT; original license retained at `baselines/voltagent-awesome-design-md/LICENSE`.

Runtime policy: load the broad baseline only as a starting grammar, then prefer `styles/<style-id>/` for exact, evidence-backed packs.
