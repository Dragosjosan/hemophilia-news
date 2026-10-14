# Josan AI Design System

Design system for **Josan AI** products by [Dragos Josan](https://dragosjosan.com) — an AI Engineer based in Munich, Germany.

## Sources
- **Codebase**: `designSystem/` (local mount) — `src/app.jsx`, `src/curve-editor.jsx`, `src/factor-chart.jsx`, `src/decay-engine.js`, `src/styles.css`
- **Screenshots**: `designSystem/screenshots/` and `designSystem/uploads/`
- No Figma file or GitHub repo was provided.

---

## Products

### Factor VIII Monitor
A clinical hemophilia management dashboard. Tracks blood Factor VIII levels for patients on clotting factor replacement therapies (e.g. Altuvoct). Features:
- Exponential decay modelling from user measurements (peak level, measured level, time elapsed)
- Weekly infusion schedule display with countdown to next dose
- Interactive SVG factor-level chart (area, line, stepped modes) with hover readout
- Multi-medicine comparison (multiple decay curves overlaid)
- Add/edit medicine side panel with live decay constant computation
- **Two visual skins**: Clinical (default) and Document

### dragosjosan.com (personal site)
Personal portfolio site using the **Document skin** — full monospace, zero border-radius, blue accent, `→` prefix on links. Minimal personal/project listing.

---

## Content Fundamentals

### Tone
- **Clinical and precise.** Copy is matter-of-fact, never reassuring or fluffy.
- Short sentences. No marketing language. Data speaks.
- Consistent disclaimer at footer: *"Not medical advice. Discuss data with your doctor."*
- Numeric values always in monospace with units. Never prose for numbers.

### Voice
- Third person for labels (*"Current factor level"*, *"Next infusion in"*).
- First-person avoided in UI. Second-person avoided unless onboarding.
- No exclamation marks. No emoji in UI text.
- Technical terms used precisely: *decay constant*, *halving time*, *IU/dL*, not simplified.

### Casing
- Page titles: Sentence case. *"Factor VIII levels on Altuvoct"*
- Card/section titles: Sentence case. *"Weekly infusion schedule"*
- Navigation: Title case. *"Account home"*, *"Dashboard"*
- Section labels (eyebrow): ALL CAPS + tracking. *"MEDICINES"*, *"OVERVIEW"*
- Document skin: section headers prefixed `# `, nav items prefixed `→`

### Copy examples
- ✅ *"1 infusion · decay constant −0.03198"*
- ✅ *"k = −0.03198 · t½ 21.7h"*
- ✅ *"Live · updated 09:49 AM"*
- ❌ *"Your factor levels are looking great!"*
- ❌ *"Add your first medicine to get started 🎉"*

---

## Visual Foundations

### Colors
Two color contexts: **Clinical** (default teal) and **Document** (bright blue).

| Token | Clinical | Document |
|---|---|---|
| `--bg` | `#fafbfc` | `#fafafa` |
| `--surface` | `#ffffff` | `#fafafa` |
| `--ink` | `#1a1d21` | `#0d0d0d` |
| `--accent` | `oklch(0.58 0.12 210)` | `#1a4fff` |
| `--hairline` | `#e8eaed` | `#d8d8d8` |

Danger: `oklch(0.55 0.18 25)` (red-orange). Success: `oklch(0.55 0.14 150)` (green). Warning: `oklch(0.62 0.14 75)` (amber).

Dark mode replaces all surfaces and inks via `[data-theme="dark"]`.

### Typography
- **Primary**: Inter (400/500/600/700). All UI text.
- **Monospace**: JetBrains Mono (400/500). All numbers, units, decay values, keyboard shortcuts, code.
- Base: 14px / 1.5. Page title: 26px / 600 / −0.02em. Card title: 14px / 600. Stat numbers: 28px mono / 600 / −0.02em. Section labels: 11px / upper / 0.08em tracking.
- Document skin: JetBrains Mono replaces Inter everywhere. Section headers get `# ` prefix in CSS `::before`.

### Spacing
4px base grid. Main page padding: 32px (compact: 20px). Card padding: 20px. Sidebar width: 232px. Side panel width: 440px.

### Layout
- Two-column app shell: fixed 232px sidebar + fluid main content area.
- Cards: white surface, 1px `--hairline` border, 6px radius, 20px padding.
- Stats row: borderless, separated by top/bottom hairlines and vertical hairline dividers between columns.
- Side panel: 440px fixed from right, slides in with `cubic-bezier(0.2, 0.8, 0.2, 1)` at 0.22s.
- Sidebar: sticky full-height, `--surface` bg, right hairline border.

### Backgrounds & Textures
No gradients, no illustrations, no full-bleed imagery. Flat solid surfaces. Document skin: same flat approach but no card chrome — sections divided by hairline top borders only.

### Borders
1px solid lines. `--hairline` for cards, dividers, inputs unfocused. `--hairline-strong` for button borders. Document skin: dashed borders on list rows (`border-bottom-style: dashed`).

### Border radius
Clinical: 4px (inputs, buttons), 6px (cards), 100px (badges/pills), 0px (document skin).

### Shadows
Subtle depth: sm (2px), md (8px), lg (20px). Panel: 40px. Never decorative — only for overlaid surfaces (side panel, modal).

### Hover / press states
- Buttons: `filter: brightness(1.08)` on primary; `background: var(--bg)` on default; ghost adds hairline border.
- Nav items: `background: var(--bg)` on hover; `background: var(--accent-soft)`, `color: var(--accent)` when active.
- Icon buttons: `color: var(--ink)`, `border-color: var(--hairline-strong)` on hover.
- No scale/shrink on press. No animated ripple.

### Animations
Minimal. Side panel: slide-in translateX with `cubic-bezier(0.2, 0.8, 0.2, 1)`. Scrim: opacity fade 0.18s ease. Buttons: 0.1s ease on background/filter. No bounce, no spring, no page transitions.

### Imagery
No decorative imagery. Charts are hand-rolled SVG (no external lib). Sparklines are inline SVG polylines. No illustrations, no icons beyond Unicode glyphs.

### Corner radius
Clinical 4px (controls) / 6px (cards) / 100px (pills). Document: 0px everywhere.

---

## Iconography

No dedicated icon library. All icons are Unicode glyphs or emoji-as-icon:
- `✕` — close / remove
- `✎` — edit
- `👁` — toggle visibility
- `⋯` — more / overflow
- `◉` — active item indicator
- `→` — document skin nav prefix (CSS `::before`)
- `# ` — document skin section prefix (CSS `::before`)
- `⌘K` — keyboard shortcut badge (monospace `<kbd>`)

No SVG icon set, no CDN icon font. If icons need to scale up, consider adding Lucide (matching the stroke-weight aesthetic) and flagging as an addition.

**Intentional additions:** None. All component families mirror what exists in the source codebase.

---

## Components

| Component | Path | Description |
|---|---|---|
| Button | `components/buttons/` | Primary, ghost, danger, default variants |
| IconButton | `components/buttons/` | 28×28 icon-only button |
| LinkButton | `components/buttons/` | Inline text-link action |
| Input | `components/forms/` | Text/number field with optional unit affix |
| Field | `components/forms/` | Label + input wrapper |
| Select | `components/forms/` | Styled native dropdown |
| SegmentedControl | `components/controls/` | Mutually exclusive option toggle |
| Card | `components/data/` | Surface container with title/subtitle/actions |
| StatCard | `components/data/` | Metric with number, unit, delta, sparkline |
| Badge | `components/data/` | Pill status/metadata tag |
| SidePanel | `components/layout/` | 440px slide-in drawer |

---

## UI Kits

| Kit | Path | Description |
|---|---|---|
| Factor VIII Monitor | `ui_kits/factor-monitor/` | Full clinical dashboard: chart, stats, schedule, medicines |
| Personal Site | `ui_kits/personal-site/` | dragosjosan.com — document skin minimal portfolio |

---

## File Index

```
styles.css                     ← root CSS entry (imports only)
tokens/
  fonts.css                    ← Google Fonts @import (⚠ CDN substitution)
  colors.css                   ← all color tokens + dark/document variants
  typography.css               ← font stack, size, weight, leading tokens
  spacing.css                  ← spacing scale, layout dimensions
  effects.css                  ← radius, shadow, transition tokens
  base.css                     ← HTML reset
components/
  buttons/                     ← Button, IconButton, LinkButton
  forms/                       ← Input, Field, Select
  controls/                    ← SegmentedControl
  data/                        ← Card, StatCard, Badge
  layout/                      ← SidePanel
guidelines/
  colors-*.card.html           ← accent, neutral, semantic color specimens
  type-*.card.html             ← display, body, mono type specimens
  spacing.card.html            ← spacing scale
  effects.card.html            ← radius + shadow
  skins.card.html              ← clinical vs document side-by-side
ui_kits/
  factor-monitor/              ← dashboard UI kit
  personal-site/               ← personal site UI kit
assets/
  screenshots/                 ← reference screenshots
```

---

## Font Note ⚠
Inter and JetBrains Mono are served via Google Fonts CDN (`tokens/fonts.css`). For offline or production use, download the woff2 files and replace with self-hosted `@font-face` rules.