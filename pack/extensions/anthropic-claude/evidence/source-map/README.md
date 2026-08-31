# Mobbin Source Map — Anthropic / Claude

Total local screenshots/sections/flow screens processed: **211**.

This map links local evidence files to Mobbin source URLs where available and derives deterministic component/code facts from the local images.

## Coverage by component

| Component | Count | Primary evidence |
|---|---:|---|
| `auth-onboarding` | 54 | `text:auth/verification`, `flow fallback:onboarding`, `flow:logging in` |
| `artifact-workbench-panel` | 41 | `source:claude-code/workbench`, `text:artifact/workbench` |
| `settings-preferences` | 40 | `text:settings`, `flow:settings` |
| `pricing-plan-cards` | 34 | `flow:subscribing to a plan`, `flow:upgrading plan`, `text:pricing/plan` |
| `feature-tile-grid` | 18 | `section fallback` |
| `model-comparison-figure` | 11 | `text:model/comparison` |
| `editorial-hero-section` | 8 | `text:hero/editorial` |
| `app-shell-sidebar` | 4 | `screen fallback` |
| `composer-command-card` | 1 | `screen:composer` |

## Files

- `mobbin-source-map.jsonl` — full structured map.
- `mobbin-source-map.csv` — spreadsheet-friendly map.
- `../../components/extracted/from-mobbin-screenshots/<component>/` — component-level extracted facts.

## Limits

For Claude app/authenticated screens, the repo stores image-derived facts and Mobbin source URLs. Exact DOM/CSS requires a live authenticated browser session and must be captured separately under `components/extracted/<component_id>/`.
