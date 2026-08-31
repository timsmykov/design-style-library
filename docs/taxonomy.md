# Style Taxonomy v0.1

The registry assigns each style to a primary category and optional secondary use cases.

## Categories

| Category | Use when | First styles |
|---|---|---|
| `ai_workbench` | AI outputs, artifact panels, files/code/source context | Anthropic / Claude |
| `answer_search_engine` | Answer pages, citations, research/search UX | Perplexity |
| `document_os` | Documents, databases, blocks, flexible workspaces | Notion |
| `operational_workspace` | Tasks/issues/projects, dense productivity | Linear |
| `payments_trust` | Payments, pricing, compliance, trust | Stripe |
| `crypto_wallet_trust` | Wallets, assets, irreversible crypto actions | MetaMask |
| `developer_control_plane` | Deployments, config, logs, APIs, status | Vercel |
| `command_native_utility` | Keyboard-first utilities, launchers, compact actions | Raycast |
| `collaborative_canvas` | Creation canvases, inspectors, multiplayer | Figma |
| `marketplace_consumer` | Discovery, imagery, cards, booking/purchase trust | Airbnb |

## Selection rules

Agents should choose by user job and medium, not by visual preference alone.

- Scientific/explanatory AI note -> `anthropic-claude`.
- Source-backed answer/search product -> `perplexity-answer-engine`.
- Flexible docs/database workspace -> `notion-document-os`.
- Project/task operations -> `linear-operational-workspace`.
- Payments/trust/checkout -> `stripe-trust-commerce`.
- Crypto/wallet/transaction review -> `metamask-crypto-wallet-trust`.
- Developer deployment/control surfaces -> `vercel-developer-control-plane`.
- Command palette / power-user launcher -> `raycast-command-native`.
- Collaborative editor/canvas -> `figma-collaborative-canvas`.
- Consumer marketplace/discovery -> `airbnb-marketplace-warm-consumer`.
