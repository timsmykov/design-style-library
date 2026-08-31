# AI Workbench Pattern

## Use for

AI coding tools, research assistants, artifact workspaces, source/file-backed generation, and task runners.

## Structure

```text
Workbench shell
├── Compact sidebar / history / project nav
├── Large quiet canvas
├── Current artifact/document/code/file panel when output exists
└── Bottom-centered composer command card
```

## Sidebar

- Warm off-white surface.
- Compact list rows.
- Soft selected state: pale fill, no bright active pill.
- Group history by time/project.
- Utility banners or integration nudges stay at the bottom and are dismissible.

## Composer command card

- Floating rounded card, not full-width chat bar.
- Top row: prompt/input.
- Secondary row: context chips like model, repo/project, branch, environment, attachment/source.
- One warm or dark primary run/send button.
- Thin border, minimal shadow.

## Artifact surface

- Artifact panels are functional first-class workspaces.
- Include title, status, source/context metadata, and actions.
- Code/data surfaces may use dark treatment only when technically justified.
- Avoid decorative previews that cannot be acted on.

## Empty state

- Large whitespace is acceptable.
- One tiny friendly illustration or icon can soften the canvas.
- Do not fill empty space with generic feature cards.
