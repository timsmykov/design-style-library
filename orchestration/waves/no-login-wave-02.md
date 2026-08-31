# no-login-wave-02

Status: supervisor-managed wave, max 2 concurrent workers.

| Card | Style | Worktree | Branch |
|---|---|---|---|
| `t_a0b0b77b` | `linear-operational-workspace` | `/root/hermes-workspace/design-style-library-worktrees/linear-operational-workspace` | `style/linear-operational-workspace-no-login-wave-02` |
| `t_339d2d7a` | `stripe-trust-commerce` | `/root/hermes-workspace/design-style-library-worktrees/stripe-trust-commerce` | `style/stripe-trust-commerce-no-login-wave-02` |

Acceptance: each worker creates an evidence-backed no-login draft/reference style pack, commits on its branch, parent verifies `stylepack_verify.py`, source-map counts, component capsules, and merges successful branches into `main`.
