---
title: Design Style Component — anthropic-claude / artifact-workbench-panel
type: design-style-component
style_id: anthropic-claude
component_id: artifact-workbench-panel
component_type: artifact_panel
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/artifact-workbench-panel.md
tags: anthropic, claude, artifact, workbench, code
---

# Artifact / workbench panel

Style: `anthropic-claude`

Component: `artifact-workbench-panel`

Mediums: web_app, ai_workbench, developer_tool

Intents: generated artifact, code preview, document output, analysis report, right-side work panel

Aliases: artifact, workbench, preview panel, code panel, output document

Repo source: `styles/anthropic-claude/components/capsules/artifact-workbench-panel.md`

## Capsule

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
