# Unified DESIGN.md — MetaMask / Crypto Wallet Trust

This file is the single-pack runtime view for `metamask-crypto-wallet-trust`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/metamask-crypto-wallet-trust`
Component semantic slices: `pack/components/metamask-crypto-wallet-trust`

---

## Baseline: `coinbase`

Source: `pack/design-md/coinbase/DESIGN.md`

---
version: alpha
name: Coinbase-design-analysis
description: An institutional-grade crypto exchange whose marketing surfaces read like a quietly-confident financial-services brand. The base canvas is pure white; Coinbase Blue (`#0052ff`) is the single brand voltage, used scarcely on primary CTAs, signature glyphs, and inline accent moments. Type runs Coinbase's licensed CoinbaseDisplay (display) and CoinbaseSans (body) at modest weights — display sits at weight 400 not 700, signaling editorial calm rather than fintech-bombastic. Page rhythm rotates between bright white sections, soft gray elevation bands, and full-bleed dark editorial heroes (`#0a0b0d`) carrying product-ui mockup cards. Iconography is geometric and minimal; depth comes from card-on-card layering, never decorative shadows.

colors:
  primary: "#0052ff"
  primary-active: "#003ecc"
  primary-disabled: "#a8b8cc"
  ink: "#0a0b0d"
  body: "#5b616e"
  body-strong: "#0a0b0d"
  muted: "#7c828a"
  muted-soft: "#a8acb3"
  hairline: "#dee1e6"
  hairline-soft: "#eef0f3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-strong: "#eef0f3"
  surface-dark: "#0a0b0d"
  surface-dark-elevated: "#16181c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-soft: "#a8acb3"
  semantic-up: "#05b169"
  semantic-down: "#cf202f"
  accent-yellow: "#f4b000"

typography:
  display-mega:
    fontFamily: "'Coinbase Display', -apple-system, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -2px
  display-xl:
    fontFamily: "'Coinbase Display', sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -1.6px
  display-lg:
    fontFamily: "'Coinbase Display', sans-serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -1.3px
  display-md:
    fontFamily: "'Coinbase Display', sans-serif"
    fontSize: 44px
    fontWeight: 400
    lineHeight: 1.09
    letterSpacing: -1px
  display-sm:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.11
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.13
    letterSpacing: -0.4px
  title-md:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  number-display:
    fontFamily: "'Coinbase Mono', 'Coinbase Sans', monospace"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0
  nav-link:
    fontFamily: "'Coinbase Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 100px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  base: 16px
  md: 20px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

components:
  top-nav-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-on-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-secondary-light:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  button-secondary-dark:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  button-outline-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 11px 19px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button}"
  button-pill-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 16px 32px
    height: 56px
  hero-band-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-mega}"
    padding: 96px
  hero-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: 96px
  product-ui-card-dark:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
    padding: 32px
  product-ui-card-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
  feature-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  asset-row:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 16px 0
  price-up-cell:
    backgroundColor: transparent
    textColor: "{colors.semantic-up}"
    typography: "{typography.number-display}"
  price-down-cell:
    backgroundColor: transparent
    textColor: "{colors.semantic-down}"
    typography: "{typography.number-display}"
  pricing-tier-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  cta-band-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    padding: 96px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 14px 16px
    height: 48px
  search-input-pill:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    height: 44px
  badge-pill:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  asset

[truncated in unified pack view; see source file for full content]

## Baseline: `binance`

Source: `pack/design-md/binance/DESIGN.md`

---
version: alpha
name: Binance-design-analysis
description: A confident financial-platform interface anchored on a deep near-black canvas, where Binance's iconic yellow (#FCD535) carries every primary CTA, brand accent, and value-claim moment. Type runs Binance's custom BinanceNova / BinancePlex stack at modest weights — the system trusts size and yellow voltage over bold weight. Marketing and product surfaces default to the dark theme; transactional surfaces (buy crypto, deposit, exchange) flip to a light theme that shares the same yellow CTAs and gray-blue hairlines. Trading green (up) and red (down) accents thread through both modes for price-direction signals.

colors:
  primary: "#fcd535"
  primary-active: "#f0b90b"
  primary-disabled: "#3a3a1f"
  ink: "#181a20"
  body: "#eaecef"
  body-on-light: "#181a20"
  muted: "#707a8a"
  muted-strong: "#929aa5"
  hairline-on-light: "#eaecef"
  hairline-on-dark: "#2b3139"
  border-strong: "#cdd1d6"
  canvas-light: "#ffffff"
  canvas-dark: "#0b0e11"
  surface-card-dark: "#1e2329"
  surface-elevated-dark: "#2b3139"
  surface-soft-light: "#fafafa"
  surface-strong-light: "#f5f5f5"
  on-primary: "#181a20"
  on-dark: "#ffffff"
  trading-up: "#0ecb81"
  trading-down: "#f6465d"
  accent-turquoise: "#2dbdb6"
  info: "#3b82f6"
  info-ring: "#3b82f6"

typography:
  hero-display:
    fontFamily: "BinanceNova, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  number-display:
    fontFamily: "BinancePlex, BinanceNova, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  number-md:
    fontFamily: "BinancePlex, BinanceNova, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  number-sm:
    fontFamily: "BinancePlex, BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "BinanceNova, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 32px
  button-secondary-on-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-secondary-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button}"
  button-trading-up:
    backgroundColor: "{colors.trading-up}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
  button-trading-down:
    backgroundColor: "{colors.trading-down}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
  button-subscribe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
    height: 28px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  top-nav-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.hero-display}"
    padding: 80px
  stat-callout-card:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.number-display}"
  trust-badge:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 16px 20px
  markets-table-card:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 24px
  markets-row:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.number-md}"
    padding: 12px 0
  price-up-cell:
    backgroundColor: transparent
    textColor: "{colors.trading-up}"
    typography: "{typography.number-md}"
  price-down-cell:
    backgroundColor: transparent
    textColor: "{colors.trading-down}"
    typography: "{typography.number-md}"
  search-input-on-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 10px 16px
    height: 40px
  text-input-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 40px
  funds-safu-band:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
    padding: 80px
  feature-photo-card:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
  qr-promo-card:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xl}"
    padding: 32px
  faq-row:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 20px 0
  cta-band-dark:
    backgroundColor

[truncated in unified pack view; see source file for full content]

## Baseline: `kraken`

Source: `pack/design-md/kraken/DESIGN.md`

# Design System Inspired by Kraken

## 1. Visual Theme & Atmosphere

Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color. The design operates on white backgrounds with Kraken Purple (`#7132f5`, `#5741d8`, `#5b1ecf`) creating a distinctive, professional crypto identity. The proprietary Kraken-Brand font handles display headings with bold (700) weight and negative tracking, while Kraken-Product (with IBM Plex Sans fallback) serves as the UI workhorse.

**Key Characteristics:**
- Kraken Purple (`#7132f5`) as primary brand with darker variants (`#5741d8`, `#5b1ecf`)
- Kraken-Brand (display) + Kraken-Product (UI) dual font system
- Near-black (`#101114`) text with cool blue-gray neutral scale
- 12px radius buttons (rounded but not pill)
- Subtle shadows (`rgba(0,0,0,0.03) 0px 4px 24px`) — whisper-level
- Green accent (`#149e61`) for positive/success states

## 2. Color Palette & Roles

### Primary
- **Kraken Purple** (`#7132f5`): Primary CTA, brand accent, links
- **Purple Dark** (`#5741d8`): Button borders, outlined variants
- **Purple Deep** (`#5b1ecf`): Deepest purple
- **Purple Subtle** (`rgba(133,91,251,0.16)`): Purple at 16% — subtle button backgrounds
- **Near Black** (`#101114`): Primary text

### Neutral
- **Cool Gray** (`#686b82`): Primary neutral, borders at 24% opacity
- **Silver Blue** (`#9497a9`): Secondary text, muted elements
- **White** (`#ffffff`): Primary surface
- **Border Gray** (`#dedee5`): Divider borders

### Semantic
- **Green** (`#149e61`): Success/positive at 16% opacity for badges
- **Green Dark** (`#026b3f`): Badge text

## 3. Typography Rules

### Font Families
- **Display**: `Kraken-Brand`, fallbacks: `IBM Plex Sans, Helvetica, Arial`
- **UI / Body**: `Kraken-Product`, fallbacks: `Helvetica Neue, Helvetica, Arial`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Kraken-Brand | 48px | 700 | 1.17 | -1px |
| Section Heading | Kraken-Brand | 36px | 700 | 1.22 | -0.5px |
| Sub-heading | Kraken-Brand | 28px | 700 | 1.29 | -0.5px |
| Feature Title | Kraken-Product | 22px | 600 | 1.20 | normal |
| Body | Kraken-Product | 16px | 400 | 1.38 | normal |
| Body Medium | Kraken-Product | 16px | 500 | 1.38 | normal |
| Button | Kraken-Product | 16px | 500–600 | 1.38 | normal |
| Caption | Kraken-Product | 14px | 400–700 | 1.43–1.71 | normal |
| Small | Kraken-Product | 12px | 400–500 | 1.33 | normal |
| Micro | Kraken-Product | 7px | 500 | 1.00 | uppercase |

## 4. Component Stylings

### Buttons

**Primary Purple**
- Background: `#7132f5`
- Text: `#ffffff`
- Padding: 13px 16px
- Radius: 12px

**Purple Outlined**
- Background: `#ffffff`
- Text: `#5741d8`
- Border: `1px solid #5741d8`
- Radius: 12px

**Purple Subtle**
- Background: `rgba(133,91,251,0.16)`
- Text: `#7132f5`
- Padding: 8px
- Radius: 12px

**White Button**
- Background: `#ffffff`
- Text: `#101114`
- Radius: 10px
- Shadow: `rgba(0,0,0,0.03) 0px 4px 24px`

**Secondary Gray**
- Background: `rgba(148,151,169,0.08)`
- Text: `#101114`
- Radius: 12px

### Badges
- Success: `rgba(20,158,97,0.16)` bg, `#026b3f` text, 6px radius
- Neutral: `rgba(104,107,130,0.12)` bg, `#484b5e` text, 8px radius

## 5. Layout Principles

### Spacing: 1px, 2px, 3px, 4px, 5px, 6px, 8px, 10px, 12px, 13px, 15px, 16px, 20px, 24px, 25px
### Border Radius: 3px, 6px, 8px, 10px, 12px, 16px, 9999px, 50%

## 6. Depth & Elevation
- Subtle: `rgba(0,0,0,0.03) 0px 4px 24px`
- Micro: `rgba(16,24,40,0.04) 0px 1px 4px`

## 7. Do's and Don'ts

### Do
- Use Kraken Purple (#7132f5) for CTAs and links
- Apply 12px radius on all buttons
- Use Kraken-Brand for headings, Kraken-Product for body

### Don't
- Don't use pill buttons — 12px is the max radius for buttons
- Don't use other purples outside the defined scale

## 8. Responsive Behavior
Breakpoints: 375px, 425px, 640px, 768px, 1024px, 1280px, 1536px

## 9. Agent Prompt Guide

### Quick Color Reference
- Brand: Kraken Purple (`#7132f5`)
- Dark variant: `#5741d8`
- Text: Near Black (`#101114`)
- Secondary text: `#9497a9`
- Background: White (`#ffffff`)

### Example Component Prompts
- "Create hero: white background. Kraken-Brand 48px weight 700, letter-spacing -1px. Purple CTA (#7132f5, 12px radius, 13px 16px padding)."


---

# Hermes deep extension override

## STYLE.md excerpt

# MetaMask / Crypto Wallet Trust

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `metamask-crypto-wallet-trust`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#f7f4f0; `surface`=#ffffff; `panel`=#fff8f2; `text`=#171717; `muted`=#6b7280; `border`=#e5e7eb; `accent`=#f6851b; `accent2`=#763d16.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `connect-dapp-permission` — connect dapp permission
- `gas-fee-warning` — gas fee warning
- `network-selector` — network selector
- `portfolio-card` — portfolio card
- `security-warning` — security warning
- `seed-phrase-onboarding` — seed phrase onboarding
- `send-receive-flow` — send receive flow
- `swap-quote-card` — swap quote card
- `token-list` — token list
- `wallet-home-balance` — wallet home balance

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/metamask-crypto-wallet-trust/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 18
- Public web pages captured: 2
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/metamask-crypto-wallet-trust/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/metamask-crypto-wallet-trust/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/metamask-crypto-wallet-trust/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/metamask-crypto-wallet-trust/eval/checklist.yaml` and `eval/failure-modes.md`.
6. If the output feels generic, increase fidelity through component structure and hierarchy, not by copying exact source screens.

## Do

- Use local tokens and capsules as the first source of truth.
- Make state, status, and user action obvious.
- Keep density and spacing consistent across related surfaces.
- Use evidence-backed component vocabulary when describing or implementing the UI.

## Do not

- Do not call web search, GitHub, Mobbin, browser/CDP, or external services at runtime for style guidance.
- Do not clone exact production screens, logos, copy, private account data, or proprietary code.
- Do not mix this style with another pack unless the user explicitly asks for a hybrid.
- Do not substitute a moodboard description for component-level structure.


## Component atlas excerpt

# Component atlas

Runtime component atlas for `metamask-crypto-wallet-trust`.

Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.

## `connect-dapp-permission` — MetaMask / Crypto Wallet Trust — Connect Dapp Permission

Use when: the artifact needs `connect dapp permission` behavior, layout, or decision structure.
Capsule: `components/capsules/connect-dapp-permission.md`
Semantic slice: `pack/components/metamask-crypto-wallet-trust/connect-dapp-permission.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Connect Dapp Permission Use this capsule when the artifact needs `connect dapp permission` behavior in the MetaMask / Crypto Wallet Trust style. ## Grammar - Style formula: crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution - Evidence refs: 6 local images. - Token anchors: canvas `#f7f4f0`, surface `#ffffff`, text `#171717`, accent `#f6851b`. - Preserve information h

## `gas-fee-warning` — MetaMask / Crypto Wallet Trust — Gas Fee Warning

Use when: the artifact needs `gas fee warning` behavior, layout, or decision structure.
Capsule: `components/capsules/gas-fee-warning.md`
Semantic slice: `pack/components/metamask-crypto-wallet-trust/gas-fee-warning.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Gas Fee Warning Use this capsule when the artifact needs `gas fee warning` behavior in the MetaMask / Crypto Wallet Trust style. ## Grammar - Style formula: crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution - Evidence refs: 6 local images. - Token anchors: canvas `#f7f4f0`, surface `#ffffff`, text `#171717`, accent `#f6851b`. - Preserve information hierarchy and act

## `network-selector` — MetaMask / Crypto Wallet Trust — Network Selector

Use when: the artifact needs `network selector` behavior, layout, or decision structure.
Capsule: `components/capsules/network-selector.md`
Semantic slice: `pack/components/metamask-crypto-wallet-trust/network-selector.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Network Selector Use this capsule when the artifact needs `network selector` behavior in the MetaMask / Crypto Wallet Trust style. ## Grammar - Style formula: crypto wallet trust surface; extension/mobile-like cards; token balances, network pills, gas/risk warnings and connect permissions; orange fox identity with security-first caution - Evidence refs: 6 local images. - Token anchors: canvas `#f7f4f0`, surface `#ffffff`, text `#171717`,

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — MetaMask / Crypto Wallet Trust

This contract tells an agent how to use `metamask-crypto-wallet-trust` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/metamask-crypto-wallet-trust/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/metamask-crypto-wallet-trust/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/metamask-crypto-wallet-trust/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/metamask-crypto-wallet-trust/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/metamask-crypto-wallet-trust/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/metamask-crypto-wallet-trust/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/metamask-crypto-wallet-trust/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

## Authority rule

The deep Hermes extension overrides the broad VoltAgent baseline whenever they differ. The baseline provides vocabulary; this extension provides implementation constraints, local evidence, component structure, and failure modes.

## Runtime boundary

Use local files only. GitHub, Mobbin, Firecrawl, Browser/CDP, Playwright, and authenticated sessions are build-time enrichment lanes. Runtime style use should remain offline, deterministic, and repo-first.

## Generation protocol

- Identify the product job and information hierarchy before styling.
- Select the nearest component capsule by semantic job, not by visual decoration.
- Apply tokens exactly where possible; when adapting, keep role semantics stable.
- Preserve accessibility basics: readable contrast, usable target sizes, clear focus/selected/error states.
- State uncertainty if the requested surface has no matching capsule, then compose from the closest primitives.

## Review protocol

A result is acceptable only if it passes the local eval layer and can name which capsules/tokens shaped it. If it cannot cite local pack paths, it did not really use the style system.

## Safety

Adapt style grammar. Do not impersonate the brand, reuse logos, reproduce exact screens, copy private data, or import proprietary source code.

