---
style_id: anthropic-claude
component_id: artifact-workbench-panel
title: Artifact / workbench panel
component_type: artifact_panel
mediums:
  - web_app
  - ai_workbench
  - developer_tool
intents:
  - generated artifact
  - code preview
  - document output
  - analysis report
  - right-side work panel
aliases:
  - artifact
  - workbench
  - preview panel
  - code panel
  - output document
tags:
  - anthropic
  - claude
  - artifact
  - workbench
  - code
evidence_paths:
  - evidence/mobbin/screens/screen-008-claude-artifact-b1cedcfe.webp
  - evidence/mobbin/screens/screen-019-claude-mobbin-98255484.webp
  - evidence/mobbin/screens/
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/AUTH_BLOCKERS.md
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/artifact-workbench-panel
confidence: extracted
updated_at: 2026-06-30
---

# Artifact / workbench panel

## Use when

Display generated work as a durable object: document, code, table, chart, preview, or analysis report.

## Structure

```text
Artifact panel
├── artifact title / file name
├── status/context row
├── main generated object
│   ├── document
│   ├── code
│   ├── table
│   ├── preview
│   └── chart/analysis block
└── actions: copy, open, edit, share, continue
```

## Implementation recipe

- Make the artifact a first-class surface, not just a chat attachment.
- Use warm/white document surfaces for text and analysis.
- Use dark inverse panels only for code/developer/proof contexts.
- Put actions close to the artifact title or right edge, not scattered.
- Use document hierarchy inside the artifact: headings, tables, captions.

## Code extraction targets

- Split-pane dimensions and resize/collapse behavior.
- Artifact card/panel border/radius/shadow.
- Header action button spacing.
- Code/document/table internal typography.

## Avoid

- Treating artifact as a screenshot placeholder, heavy dashboard chrome, detached floating action clutter.
