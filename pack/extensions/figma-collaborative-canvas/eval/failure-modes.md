# Failure modes — `figma-collaborative-canvas`

## Generic moodboard output

Symptom: the result uses a few colors from the pack but ignores component structure, states, and hierarchy.

Fix: reload `components/component-atlas.md`, choose the closest capsule, and rebuild the layout around the component's semantic job.

## Exact screen cloning

Symptom: the output copies a reference screen too literally, including brand-specific layout, copy, logo placement, or private-data shapes.

Fix: preserve grammar and hierarchy, but change information architecture to fit the user's actual product.

## Token drift

Symptom: colors, radius, shadows, or type sizes are invented because they "feel close".

Fix: use `tokens/tokens.json` and `tokens/css-vars.css`; when a new value is needed, derive it from an existing role and explain the adaptation.

## Component mismatch

Symptom: a pricing card is used for a settings table, a command palette is used for a dashboard, or a gallery pattern is used where a status list is needed.

Fix: select capsules by job-to-be-done. If no exact capsule exists, combine two closest capsules and say which parts came from each.

## Missing states

Symptom: the main mockup looks correct but selected, focus, error, loading, empty, permission, and responsive states are absent.

Fix: use the checklist and add the states that matter for the requested user flow.

## Runtime external dependency

Symptom: the agent tries to open Mobbin, GitHub, browser/CDP, or web search to understand the style during normal generation.

Fix: stop and use local `pack/` files. External tools are build-time enrichment only.

## Brand impersonation

Symptom: the artifact appears to be an official screen from the reference brand or uses their logo/private interface details.

Fix: remove brand-specific marks and exact-copy details; keep only transferable design grammar.
