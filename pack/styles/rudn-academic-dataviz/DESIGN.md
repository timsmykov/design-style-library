# Unified DESIGN.md — RUDN Academic Data Visualization

This file is the single-pack runtime view for `rudn-academic-dataviz`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/rudn-academic-dataviz`
Component semantic slices: `pack/components/rudn-academic-dataviz`

---

## Baseline

No exact VoltAgent DESIGN.md baseline exists. Use the global pack catalog plus this deep extension.


---

# Hermes deep extension override

## STYLE.md excerpt

# RUDN Academic Data Visualization

Status: **draft v1.0** - complete offline style package derived from the supplied 24-page course deck and palette reference.

## Canonical one-liner

**Academic clarity with workshop energy:** a white, rule-based teaching canvas where black Inter typography carries the argument, electric blue marks the learning path, and lavender bands hold evidence, caveats, and instructions.

## What this style is

This is the visual system for the RUDN data-visualization course and adjacent academic materials. It is designed to make a room of students understand the next action, the method, and the evidence within seconds. It should feel rigorous but not bureaucratic, contemporary but not fashionable, and energetic without becoming decorative.

This is not an official reconstruction of the university's full corporate identity. The supplied evidence is a course deck and a palette configuration, so the pack governs course presentations, learning visuals, worksheets, charts, tables, and lightweight digital artifacts.

## Signature

- White 16:9 canvas with generous empty space.
- Inter Bold for decisive headings; Inter Regular for explanation; Inter Light only for oversized numerals or symbols.
- Black and charcoal do most of the work.
- Electric blue `#2E6BFE` highlights the learning path, variable, timebox, or conclusion.
- Indigo `#4950BC` is the cross-medium action/link color when a calmer control color is needed.
- Pale lavender `#DADBF0` is an information surface, never decoration.
- Thin gray or black rules organize sequences, comparisons, and tables.
- Cards are flat, square to softly rounded, and almost shadowless.
- Every visual has one dominant message and one obvious next reading step.

## Use when

- Teaching a method, formula, workflow, or quality criterion.
- Building a seminar deck, assignment sheet, data story, rubric, or handout.
- Presenting charts or tables that must be discussed and checked.
- Explaining a contrast such as official versus personal, input versus output, or valid versus invalid.
- Creating course interfaces where clarity and accessibility matter more than brand spectacle.

## Avoid when

- The output needs entertainment, emotional storytelling, luxury, or cinematic drama.
- The content is a dense real-time operational dashboard.
- The design depends on photography, gradients, glass, 3D objects, or decorative illustration.
- The audience cannot see a projected slide clearly; in that case increase scale and reduce content before adding components.

## Non-negotiable rules

1. One slide or frame answers one question.
2. Titles state the topic or insight in plain language; blue may emphasize only the meaningful phrase.
3. A slide uses no more than one dominant blue fill and one lavender support band.
4. Never encode a categorical dataset with many unrelated bright colors. Use blue plus neutral tints.
5. Put caveats next to the method they qualify, not in a distant footnote.
6. Tables must have a reading task: compare, verify, rank, or decide.
7. Keep a visible evidence trail: label source, period, unit, and method whenever a number is shown.
8. Do not use the RUDN name or logo as decoration. If an official logo is later supplied, follow its separate asset and clear-space rules.

## Source confidence

- `observed`: slide geometry, repeated layouts, Inter family, electric blue, lavender bands, black text, flat cards, thin rules.
- `extracted`: source deck size `960 x 540 pt`, 24 pages, embedded Inter Regular/Light/Bold, dominant colors near `#2E6BFE` and `#DADBF0`.
- `observed`: palette screenshot values `#4950BC`, `#000000`, `#272525`, `#FFFFFF`.
- `adapted`: cross-medium token roles, responsive web behavior, chart palette, and component recipes.


## Component atlas excerpt

# Component atlas

| Component | Mediums | Primary job |
|---|---|---|
| `course-title-slide` | presentation | Open a unit with a clear topic and mode |
| `numbered-method-strip` | presentation, worksheet | Explain a transparent sequence |
| `two-column-comparison` | presentation, report | Compare two definitions or methods |
| `evidence-band` | all | Hold caveat, source, prompt, or method note |
| `insight-chart-card` | presentation, report, web | Pair a chart with the conclusion and evidence |
| `checkpoint-card` | presentation, worksheet, web | State target and recovery path |

The components are intentionally structural. Reuse their logic; do not turn them into a library of decorative cards.


## Agent contract excerpt

# Agent contract

## Required context

Read `STYLE.md`, `tokens/tokens.json`, the medium-specific pattern, and `eval/checklist.yaml` before generating an artifact.

## Generation sequence

1. Write the single learning question or communication goal.
2. Choose one layout archetype from `patterns/` or a component capsule.
3. Establish title, reading order, and evidence before decoration.
4. Apply tokens exactly. Use electric blue for instructional emphasis and indigo for controls/links.
5. Add source, period, unit, method, or caveat wherever the claim requires it.
6. Render at the target size and run the checklist.

## Hard constraints

- Default presentation ratio is 16:9.
- Use Inter; fall back to Arial, Helvetica, then sans-serif.
- White canvas is the default. Dark backgrounds require an explicit content reason.
- Maximum of three semantic chromatic roles on one frame: electric blue, indigo, lavender.
- Do not invent an official RUDN logo, seal, pattern, or corporate color claim.
- Do not use gradients, glassmorphism, glossy 3D, neon glow, or heavy drop shadows.
- Do not shrink body text to make overcrowded content fit.
- Do not present a chart without readable labels and a sentence stating what to notice.

## Medium routing

- Presentation: `patterns/presentations.md`
- Data visualization: `patterns/data-viz.md`
- Worksheet/handout: `patterns/worksheets.md`
- Web or interactive artifact: `patterns/digital-surfaces.md`

## Completion evidence

An artifact is done only after rendered inspection at intended size. For slides, inspect the full deck contact sheet and at least every dense slide at 100%. For web, inspect desktop and mobile. For charts, verify contrast, units, labels, and source note.
