---
# Copy this file into your project root as DESIGN.md, then work through every
# [[SET: ...]] and [[CHOOSE: ...]] marker. Values already filled in are researched
# defaults — change them only with a reason you can state.
#
# Derived from design-intelligence/COMMON-FOUNDATION.md.
# Not affiliated with or endorsed by any brand referenced in the source research.

version: 1
name: [[SET: product-name]]-design-system
category: foundation
density: [[CHOOSE: compact | default | spacious]]
mode: [[CHOOSE: light-only | dark-only | both]]
description: >
  [[SET: two or three sentences. What the product is, who uses it, and the single
  most important quality the interface must have. Write this before choosing any
  visual value — everything below should be defensible against it.]]

# ---------------------------------------------------------------------------
# PRIMITIVE TOKENS — raw values, no meaning attached.
# Components must never reference these directly.
# ---------------------------------------------------------------------------
primitives:
  neutral:
    50:  "[[SET: #fafafa]]"    # canvas (light)
    100: "[[SET: #f4f4f5]]"    # raised surface (light)
    200: "[[SET: #e4e4e7]]"    # subtle border (light)
    300: "[[SET: #d4d4d8]]"    # default border (light)
    400: "[[SET: #a1a1aa]]"    # disabled text (light) / secondary text (dark)
    500: "[[SET: #71717a]]"    # tertiary text (light)
    600: "[[SET: #52525b]]"    # secondary text (light)
    700: "[[SET: #3f3f46]]"    # default border (dark)
    800: "[[SET: #27272a]]"    # raised surface (dark)
    900: "[[SET: #18181b]]"    # primary text (light) / canvas (dark)
    950: "[[SET: #09090b]]"    # deep canvas (dark)
  accent:
    # ONE brand hue. See "Colour discipline" below before adding a second.
    500: "[[SET: #3b82f6]]"
    600: "[[SET: #2563eb]]"    # action.primary
    700: "[[SET: #1d4ed8]]"    # action.primary-active
    400: "[[SET: #60a5fa]]"    # dark-mode action (lighter, holds contrast)
  status:
    success: "[[SET: #16a34a]]"
    warning: "[[SET: #d97706]]"
    danger:  "[[SET: #dc2626]]"
    info:    "[[SET: #0284c7]]"

# ---------------------------------------------------------------------------
# SEMANTIC TOKENS — intent. This is the layer components consume.
# Both modes are specified separately. Dark mode is NOT an inversion.
# ---------------------------------------------------------------------------
semantic:
  light:
    surface-canvas:    "{primitives.neutral.50}"
    surface-raised:    "#ffffff"
    surface-sunken:    "{primitives.neutral.100}"
    surface-overlay:   "#ffffff"
    surface-inverse:   "{primitives.neutral.900}"
    text-primary:      "{primitives.neutral.900}"
    text-secondary:    "{primitives.neutral.600}"
    text-tertiary:     "{primitives.neutral.500}"
    text-disabled:     "{primitives.neutral.400}"
    text-on-accent:    "#ffffff"
    text-on-inverse:   "{primitives.neutral.50}"
    text-link:         "{primitives.accent.600}"
    border-subtle:     "{primitives.neutral.200}"
    border-default:    "{primitives.neutral.300}"
    border-strong:     "{primitives.neutral.400}"
    action-primary:    "{primitives.accent.600}"
    action-hover:      "{primitives.accent.700}"
    action-active:     "{primitives.accent.700}"
    action-disabled:   "{primitives.neutral.200}"
    status-success:    "{primitives.status.success}"
    status-warning:    "{primitives.status.warning}"
    status-danger:     "{primitives.status.danger}"
    status-info:       "{primitives.status.info}"
    focus-ring:        "{primitives.accent.500}"
    scrim:             "rgba(0,0,0,0.40)"
  dark:
    # Deliberately re-derived, not inverted. Note: accent shifts lighter,
    # borders lighten instead of darkening, text stops short of pure white.
    surface-canvas:    "{primitives.neutral.950}"
    surface-raised:    "{primitives.neutral.900}"
    surface-sunken:    "#000000"
    surface-overlay:   "{primitives.neutral.800}"
    surface-inverse:   "{primitives.neutral.50}"
    text-primary:      "[[SET: #ededf0]]"   # not #ffffff — avoids halation
    text-secondary:    "{primitives.neutral.400}"
    text-tertiary:     "{primitives.neutral.500}"
    text-disabled:     "{primitives.neutral.600}"
    text-on-accent:    "#ffffff"
    text-on-inverse:   "{primitives.neutral.900}"
    text-link:         "{primitives.accent.400}"
    border-subtle:     "rgba(255,255,255,0.08)"
    border-default:    "rgba(255,255,255,0.14)"
    border-strong:     "rgba(255,255,255,0.24)"
    # TWO tokens per action colour, not one. Lightening a FILL while keeping a white
    # label always REDUCES contrast — a build test of this layer measured 3.68:1 and
    # 2.92:1 doing exactly that. See COMMON-FOUNDATION.md section 6.
    #   action-primary          = filled background. NOT lightened. White label >=4.5:1.
    #   action-primary-on-dark  = lightened, for TEXT/ICON/LINK/BORDER on dark only.
    # Never use an *-on-dark value as a filled background.
    action-primary:         "{primitives.accent.600}"
    action-primary-on-dark: "{primitives.accent.400}"
    action-hover:           "{primitives.accent.700}"
    action-active:          "{primitives.accent.700}"
    action-disabled:        "{primitives.neutral.800}"
    # Status colours follow the same split: the *-surface tint is a background (so the
    # status TEXT on it must reach 4.5:1), while these values are the text/icon colour.
    status-success:    "[[SET: lighter, desaturated 10-20% — text/icon on dark]]"
    status-warning:    "[[SET: lighter, desaturated 10-20% — text/icon on dark]]"
    status-danger:     "[[SET: lighter, desaturated 10-20% — text/icon on dark]]"
    status-info:       "[[SET: lighter, desaturated 10-20% — text/icon on dark]]"
    focus-ring:        "{primitives.accent.400}"
    scrim:             "rgba(0,0,0,0.60)"

typography:
  families:
    display: "[[SET: family, fallback-1, fallback-2, sans-serif]]"
    body:    "[[SET: family, system-ui, sans-serif]]"
    mono:    "[[SET: family, ui-monospace, monospace]]"
  substitutes:
    # REQUIRED if any family above is proprietary or licensed.
    # A system built on a font nobody can license is decoration, not a system.
    display: "[[SET: openly-available substitute + weights]]"
    body:    "[[SET: openly-available substitute + weights]]"
  scale:
    # Sizes are the "default" density column. Compact/spacious in the notes below.
    display-1: { size: 56px, weight: 600, lineHeight: 1.05, tracking: -1.5px }
    display-2: { size: 44px, weight: 600, lineHeight: 1.10, tracking: -1.0px }
    display-3: { size: 36px, weight: 600, lineHeight: 1.15, tracking: -0.6px }
    heading-1: { size: 28px, weight: 600, lineHeight: 1.20, tracking: -0.4px }
    heading-2: { size: 22px, weight: 600, lineHeight: 1.30, tracking: -0.2px }
    heading-3: { size: 18px, weight: 600, lineHeight: 1.40, tracking: 0 }
    subtitle:  { size: 18px, weight: 400, lineHeight: 1.50, tracking: 0 }
    body-lg:   { size: 18px, weight: 400, lineHeight: 1.55, tracking: 0 }
    body:      { size: 16px, weight: 400, lineHeight: 1.50, tracking: 0 }
    body-sm:   { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }
    caption:   { size: 12px, weight: 400, lineHeight: 1.40, tracking: 0.1px }
    overline:  { size: 12px, weight: 600, lineHeight: 1.30, tracking: 0.8px, transform: uppercase }
    label:     { size: 14px, weight: 500, lineHeight: 1.20, tracking: 0 }
    code:      { size: 14px, weight: 400, lineHeight: 1.50, tracking: 0, family: mono }
    numeric:   { size: 16px, weight: 400, lineHeight: 1.40, tracking: 0, features: "tabular-nums" }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 5: 20px, 6: 24px, 8: 32px, 10: 40px, 12: 48px, 16: 64px, 20: 80px, 24: 96px }
  section: "[[CHOOSE: 48px (compact) | 80px (default) | 96px (spacious)]]"
  page-padding: { mobile: 16px, tablet: 24px, desktop: 32px }

radius:
  character: "[[CHOOSE: squared | default | soft]]"
  # Values shown are the "default" character. Swap the whole ladder if you change character.
  none: 0
  xs: 4px
  sm: 6px
  md: 8px      # buttons, inputs
  lg: 12px     # cards
  xl: 16px
  2xl: 24px
  full: 9999px

layout:
  container: "[[CHOOSE: 1024px (compact) | 1280px (default) | 1440px (spacious)]]"
  prose: 680px           # follows measure (60-70 chars), NOT the container
  sidebar-nav: 240px
  sidebar-rail: 56px
  sidebar-detail: 320px
  breakpoints: { xs: 0, sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation:
  0: "none"
  1: "1px solid {semantic.border-subtle}"
  2: "0 1px 3px rgba(0,0,0,0.08)"        # dark mode: surface-raised + border-subtle
  3: "0 4px 12px rgba(0,0,0,0.10)"       # dark mode: surface-overlay + border-default
  4: "0 12px 32px rgba(0,0,0,0.14)"      # dark mode: surface-overlay + border-strong
  strategy: "[[CHOOSE: border-first (recommended) | shadow-first]]"

motion:
  instant: 100ms      # colour, opacity
  fast: 150ms         # dropdowns, tooltips, toggles
  base: 250ms         # panels, drawers, modals
  easing-enter: "cubic-bezier(0.16, 1, 0.3, 1)"    # ease-out
  easing-exit: "cubic-bezier(0.4, 0, 1, 1)"        # ease-in
  reduced-motion: "cross-fade only, state change preserved"

components:
  button-primary:   { height: 40px, padding: "10px 18px", radius: md, surface: action-primary, text: text-on-accent, type: label }
  button-secondary: { height: 40px, padding: "10px 18px", radius: md, surface: surface-raised, text: text-primary, border: border-default, type: label }
  button-ghost:     { height: 40px, padding: "10px 18px", radius: md, surface: transparent, text: text-primary, type: label }
  button-destructive: { height: 40px, padding: "10px 18px", radius: md, surface: status-danger, text: "#ffffff", type: label }
  text-input:       { height: 40px, padding: "10px 14px", radius: md, surface: surface-raised, border: border-default, text: text-primary, type: body }
  card:             { padding: 24px, radius: lg, surface: surface-raised, border: border-subtle, elevation: 1 }
  modal:            { padding: 24px, radius: lg, width: 560px, surface: surface-overlay, elevation: 4, scrim: true }
  nav-bar:          { height: 64px, padding: "0 32px", surface: surface-canvas, border-bottom: border-subtle }
  table-row:        { height: 48px, padding: "12px 16px", border-bottom: border-subtle, type: body-sm }
  toast:            { width: 360px, padding: 16px, radius: md, surface: surface-overlay, elevation: 3 }
  badge:            { padding: "2px 8px", radius: full, type: caption }
---

# [[SET: Product name]] — Design System

## 1. Product context

- **What it is:** [[SET: one sentence]]
- **Primary job the interface must do:** [[SET: e.g. let operators resolve exceptions fast; convince evaluators to start a trial; help readers finish an article]]
- **Visit frequency:** [[CHOOSE: first-time/rare | occasional | daily | all-day]] — this drives density and section rhythm more than any other single fact
- **Primary devices:** [[SET: desktop / mobile / both, with rough split if known]]
- **Public or authenticated:** [[CHOOSE: public | authenticated | both]]
- **Primary design category:** [[SET: from design-intelligence/CATEGORY-SELECTION.md]]
- **Supporting categories:** [[SET: or "none"]]

## 2. Users and roles

| Role | Expertise | Frequency | Primary tasks | Density |
|---|---|---|---|---|
| [[SET: role]] | [[novice \| intermediate \| expert]] | [[rare \| weekly \| daily]] | [[SET]] | [[compact \| default \| spacious]] |

If more than two roles exist, also complete
`design-intelligence/templates/ROLE-EXPERIENCE-MAP.md`.

## 3. Experience principles

Three to five. Each must be falsifiable — a principle that cannot be violated is decoration.
Replace these examples:

1. **[[SET: e.g. "The data is the interface."]]** — [[SET: what this rules out]]
2. **[[SET: e.g. "Never block on something we can recover from."]]** — [[SET: what this rules out]]
3. **[[SET: e.g. "One primary action per screen."]]** — [[SET: what this rules out]]

## 4. Visual theme

- **Canvas polarity:** [[CHOOSE: light | dark | dual-track by surface purpose]]
- **Character:** [[SET: 3–5 adjectives, and the one you'd sacrifice last]]
- **Decoration budget:** [[CHOOSE: none | minimal | moderate | expressive]]
- **What carries visual interest:** [[CHOOSE: typography | photography | illustration | data | product UI | colour blocking]]
- **What must recede:** [[SET: usually the chrome]]

If dual-track: keep typography, radius, spacing, and button vocabulary **identical** across
tracks; vary only canvas polarity, density, and decoration budget.

## 5. Colour discipline

- **Accent count:** [[CHOOSE: 0 | 1 (recommended) | 2 | 3+]]
- **The accent is reserved for:** primary action, brand mark, focus ring, active state.
  Nothing else.
- **If more than one accent:** state what each maps to structurally — product line, content
  category, object type, data series. An accent with no mapping is decoration and will
  dilute your status colours.
  - [[SET: accent → meaning]]
- **Status colours are never the sole carrier of meaning.** Every status needs an icon or
  text label as well.
- **Contrast floor:** body text ≥4.5:1, large text ≥3:1, UI boundaries ≥3:1, focus ring
  ≥3:1 against both the element and the surface. Verify in **both** modes.

## 6. Layout

- **Container:** `{layout.container}`. **Prose measure:** `{layout.prose}` — these are
  different numbers and must stay different.
- **Grid:** [[SET: e.g. 12-column, 24px gutters]]
- **Card grid reflow:** [[SET: e.g. 4-up → 3-up at 1280 → 2-up at 1024 → 1-up at 768]]
- **Whitespace rationale:** [[SET: what the space is doing — separating groups, pacing a
  narrative, or giving a dense table room to breathe]]

## 7. Navigation

- **Primary pattern:** [[CHOOSE: top bar | side nav | rail | tabs | bottom nav | command palette]]
- **Destination count:** [[SET: number]] — >7 favours side nav; ≤7 favours top bar
- **Secondary pattern:** [[SET: or "none"]]
- **Never duplicate destinations across two navigation systems.**
- **Mobile:** [[SET: what collapses, what moves to a drawer, what becomes a bottom sheet]]
- **Keyboard:** [[SET: shortcuts, if any; skip-to-content link is required regardless]]

## 8. Components

Specify surface, text, type token, radius, padding, and **all states** for each. The
frontmatter `components:` block holds the base specs; document deviations and additions
here.

For every interactive component, all eight states are required:

| State | Treatment |
|---|---|
| Default | Per frontmatter spec |
| Hover | Surface shifts ~4% (light) / ~6% (dark). Pointer only |
| Focus-visible | 2px `{semantic.focus-ring}`, 2px offset |
| Active | Surface shifts ~8% (light) / ~10% (dark) |
| Disabled | Reduced contrast, `not-allowed`, **and an explanation of why** |
| Loading | In-place indicator, dimensions preserved, interaction disabled |
| Selected | Visually distinct from both hover and focus |
| Error | Border + icon + message |

- [[SET: component name — spec + any state deviations]]

## 9. States, feedback and edge cases

Specify every one. These are the states that get skipped and then get filed as bugs:

- **Empty (first-run):** [[SET: explanation + primary action]]
- **Empty (filtered to nothing):** [[SET: distinct from first-run — offer to clear filters]]
- **Loading (initial):** [[SET: skeleton matching final shape, or spinner]]
- **Loading (in-place):** [[SET: must not shift layout]]
- **Partial / degraded data:** [[SET: show what loaded; mark what failed]]
- **Error (recoverable):** [[SET: what happened + what to do next + retry]]
- **Error (permission denied):** [[SET: what is needed and who can grant it]]
- **Offline:** [[SET: or "not handled" — but say so]]
- **Destructive confirmation:** [[SET: name the target and the count in the button]]
- **Success:** [[CHOOSE: toast | inline | no confirmation needed]] — never a modal

## 10. Responsive behaviour

Per element, state which behaviour applies: resize · reflow · collapse · stack · scroll ·
drawer · transform · defer · omit.

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Navigation | [[SET]] | [[SET]] | [[SET]] |
| Primary content | [[SET]] | [[SET]] | [[SET]] |
| Data tables | [[SET: scroll with pinned first column, or transform to cards]] | [[SET]] | [[SET]] |
| Sidebars | [[SET: drawer]] | [[SET]] | [[SET]] |
| Filters | [[SET]] | [[SET]] | [[SET]] |

**A wide table must not merely shrink.** Scroll it in a bounded container with the
identifying column pinned, or transform rows into cards.

**If a capability is genuinely unavailable on small screens, say so in the interface.**
Silent omission is worse than a clear message.

## 11. Accessibility commitments

Non-negotiable, all categories:

- [ ] Body text ≥4.5:1; large text ≥3:1; UI boundaries ≥3:1 — verified in both modes
- [ ] Visible focus indicator on every interactive element, ≥3:1, never removed
- [ ] Every action keyboard-reachable; logical tab order; no focus traps
- [ ] Touch targets ≥44×44px with ≥8px separation
- [ ] No meaning carried by colour alone
- [ ] Form fields have programmatic labels; errors are associated with their field
- [ ] One `h1` per page; no skipped heading levels
- [ ] Meaningful `alt` text; `alt=""` on decorative images
- [ ] Async changes announced via live regions
- [ ] `prefers-reduced-motion` respected
- [ ] Usable at 200% zoom

## 12. Content guidance

- **Case:** sentence case for UI text; uppercase only for `overline`
- **Buttons name outcomes:** "Save changes", not "Submit"
- **Destructive actions name the target:** "Delete 3 invoices"
- **Errors:** what happened + what to do next
- **Numbers:** units and timeframe — "1,284 requests (last 24h)"
- **Dates:** absolute in records, relative for recency
- **Terminology:** [[SET: the canonical term for each core object, and the terms you will
  not use. One object, one name, everywhere.]]

## 13. Do

- Consume semantic tokens in components; never primitives
- Keep the accent scarce — primary action, brand mark, focus, active state
- Design light and dark as separate systems
- Carry elevation with borders and surface steps before reaching for shadow
- Keep prose measure at 60–70 characters regardless of container width
- Use tabular figures wherever numbers are compared vertically
- Match input height to button height
- Specify every interaction state before shipping a component
- State the reason when you deviate from a foundation default

## 14. Do not

- Do not add a second decorative accent
- Do not invert light mode to produce dark mode
- Do not use pure `#000000` canvas with pure `#ffffff` text
- Do not use marketing display sizes (56px+) inside an application surface
- Do not use placeholder text as a label
- Do not remove focus outlines
- Do not encode status in colour alone
- Do not put body text below 14px, or below 16px on mobile
- Do not mix elevation mechanisms at one level
- Do not animate blocking interactions
- Do not let a wide table shrink instead of scroll or transform
- Do not introduce a value outside the scales above without recording why

## 15. Implementation notes

- **Token delivery:** [[SET: CSS custom properties / Tailwind config / design-token JSON / other]]
- **Component library:** [[SET: existing library to extend, or "building fresh"]]
- **Theme switching:** [[SET: class-based, media-query, or user setting persisted where]]
- **Existing components to reuse:** [[SET: list — agents must extend these, not duplicate them]]
- **Known deviations already in the codebase:** [[SET: with reason and whether they will be
  reconciled]]

## 16. Agent prompt guidance

**Reading order.** Read this file **after** `design-intelligence/COMMON-FOUNDATION.md` and
your category guide. This file wins on any conflict.

**Before generating any UI:**

1. Inspect the existing codebase — components, tokens, layout primitives, naming
   conventions. Report what you found.
2. Reuse existing components. Extend them if they are close. Create new ones only when
   nothing fits, and say why.
3. Never replace working functionality to achieve a visual change.

**When generating:**

- Reference semantic tokens by name. Never hard-code a colour, size, or spacing value that
  exists as a token.
- Implement all eight interaction states for interactive components.
- Implement empty, loading, error, and partial-data states — not just the happy path.
- Meet the §11 accessibility commitments; do not defer them.
- Match the existing code's conventions, naming, and structure.

**After generating, report:**

- Assumptions you made
- Deviations from this document, with reasons
- Design decisions still unresolved and needing a human
- Values you had to invent because this document did not specify them (these are gaps to
  fix here, not in the code)

**Example prompts:**

> Using DESIGN.md, build a [[SET: component]]. Use existing components where they fit —
> inspect the codebase first and tell me what you found before writing code. Implement all
> interaction states plus empty, loading, and error states. Report any value you had to
> invent.

> Review `[[SET: path]]` against DESIGN.md. List every hard-coded value that should be a
> token, every missing interaction state, and every accessibility commitment not met. Do not
> change behaviour — propose the diff first.
