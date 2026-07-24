# Design Intelligence — UI and design system rules

> For ChatGPT Codex, Cursor, Copilot, Gemini CLI, Aider, and any agent that reads `AGENTS.md`.
> Self-contained: the critical rules are inline, so an agent that opens no other file still
> follows them.

**Applies to any task that creates, changes, or reviews user interface.**

Full guidance lives in `.design-intelligence/` if this repo has been vendored. Start at
`.design-intelligence/AGENT-ENTRY.md` — it routes by task and product type.

---

## Reading order — strict, later overrides earlier

1. **This repository** — existing components, design tokens, naming conventions
2. `.design-intelligence/COMMON-FOUNDATION.md` — scales, tokens, accessibility floor
3. **One** category guide from `.design-intelligence/categories/` (see routing below)
4. Supporting category guides, if the product has several surfaces
5. **This project's `DESIGN.md`** — authoritative, wins every conflict

If this project has no `DESIGN.md`, say so. Offer to create one from
`.design-intelligence/templates/`. Do not silently invent a design system while implementing a
feature.

---

## Non-negotiable rules

### Process

1. **Inspect before generating.** Report what components, tokens, and conventions already exist
   before writing UI code.
2. **Reuse before creating.** Extend a near-miss component. Create new only when nothing fits, and
   state why.
3. **Never break working functionality for a visual change.** This is a restyle, not a rewrite. If a
   visual goal appears to need a behaviour change, stop and ask.
4. **Report at the end**: assumptions · deviations · **invented values** · unresolved decisions ·
   components reused vs. created · what you actually verified.

### Tokens

5. **Semantic tokens only.** No hard-coded colours, spacing, radii, or font sizes in components.
   Reference `text.primary`, not `#171b1f`.
6. **A value with no token is a specification gap.** Report it; do not invent a literal.
7. **Two layers.** Primitives (raw values) → semantics (intent). Components consume semantics only.

### States — the most commonly skipped work

8. **All eight interaction states** on every interactive element: default · hover ·
   focus-visible · active · disabled (with an explanation of why) · loading · selected · error.
9. **All seven data states** on every data-bearing view: first-run empty (with a primary action) ·
   filtered-empty (a *different* message, offering to clear filters) · initial loading (skeleton
   matching final layout) · refresh (**keeps existing data visible**) · partial data · error with
   retry · permission denied.
10. **Hover, focus, and selected are three different meanings** and need three different
    appearances.

### Accessibility — a constraint on the code you write now, not a later pass

11. Body text ≥4.5:1 · large text (≥24px, or ≥19px bold) and meaningful UI boundaries ≥3:1.
12. **Visible focus indicator always.** Never `outline: none` without a replacement. 2px ring, 2px
    offset, ≥3:1 against both the element and the surrounding surface.
13. **Touch targets ≥44×44px** with ≥8px separation.
14. **Never convey meaning by colour alone.** Every status needs an icon or text label too.
15. Every action keyboard-reachable; logical tab order; no focus traps.
16. Form fields need programmatic labels. **Placeholder is not a label.**
17. Honour `prefers-reduced-motion` without removing the state change itself.

### Layout and type

18. **4px spacing grid**, 8px preferred increments. Every spacing value is a token.
19. **16px default body text.** Never below 14px; never below 16px on mobile.
20. **Prose measure 60–70 characters** regardless of container width. A 1440px container does not
    mean 1440px paragraphs — container width and reading measure are two different numbers.
21. Type steps 1.15×–1.35× apart. Line-height falls as size rises (1.5 body → 1.05–1.15 display).
22. **Tabular figures** wherever numbers are compared vertically.
23. Breakpoints: 480 / 768 / 1024 / 1280 / 1440.
24. **Display size ceiling by surface:** marketing 56–80px · docs 36–56px · application 24–32px ·
    dashboard 20–28px. Marketing display sizes inside an application are a category error.

### Colour and depth

25. **One accent colour**, reserved for the primary action, brand mark, and focus state. Any
    additional accent must map to something structural (product line, category, data series) —
    never decoration.
26. **Border-first elevation.** Use a border or a surface step for grouping; reserve shadow for
    things that genuinely float. Never stack border + shadow + surface lift at one level.
27. **Dark mode is derived, not inverted.** Raised surfaces get *lighter* in both modes. Shadow
    barely reads on dark — use lightness steps. Dark canvas is not `#000000`; dark body text is not
    `#ffffff`.
28. **Never lighten a filled button's background while keeping a white label** — that always reduces
    contrast and typically drops below 4.5:1. Split into two tokens: `action.primary` (the fill, not
    lightened) and `action.primary-on-dark` (lightened, for text/icons/borders only).

### Motion

29. Motion must communicate causality, hierarchy, progress, or spatial change. Otherwise remove it.
30. Animate `transform` and `opacity` only. Never animate `width`, `height`, or `top`.
31. Durations: 100ms feedback · 150–200ms small transitions · 250–300ms panels. Nothing loops except
    progress indicators. **Never animate a blocking interaction.**

---

## Category routing

Density, navigation, and component set come from the product category. **Visual tone does not** —
that comes from the brand.

| Product type | Guide |
|---|---|
| Chat / assistant | `categories/conversational-ai.md` |
| Marketing / landing pages | `categories/marketing-website.md` |
| Docs / support / informational | `categories/general-website.md` |
| Dashboard / admin / ops console | `categories/dashboard-admin.md` |
| 3+ user roles on one platform | `categories/commercial-multi-role-platform.md` |
| Developer tool / API / infrastructure | `categories/developer-tools.md` |
| Catalogue / cart / checkout | `categories/ecommerce.md` |
| Money / security / legal / irreversible | `categories/financial-high-trust.md` |
| Publication / long-form reading | `categories/content-editorial.md` |
| Analytics / BI / exploration | `categories/data-analytics.md` |
| Map / spatial / 3D | `categories/spatial-map-3d.md` |

Unsure? Read `CATEGORY-SELECTION.md`. Most products need two or three: one token foundation with
several experience layers, each setting its own density and navigation.

### Density, by how often one person uses the surface

| Visit frequency | Density | Section rhythm | Body | Control height | Table row |
|---|---|---|---|---|---|
| Once / rarely | spacious | 80–96px | 16–18px | 44–48px | — |
| Weekly | default | 48–64px | 16px | 40px | 48px |
| Daily / all day | compact | 24–32px | 13–14px | 32–36px | 32–40px |

**Compact is pointer-only.** On touch, 44px targets override it.

---

## Evidence honesty — state this to the user

This guidance is synthesized from 74 real brand design analyses, but that corpus is **~90% public
marketing websites**. Consequently:

| Area | Status |
|---|---|
| Tokens, typography, spacing, elevation, breakpoints | **Evidence-backed** |
| Marketing website guidance | **Evidence-backed** (55 direct sources) |
| Developer tools, e-commerce, editorial, high-trust, docs | Partial evidence |
| Dashboard, conversational, multi-role, analytics | **Reasoning, not evidence** — no direct sources |
| Spatial / map / 3D | **Fully synthesized** — zero corpus support |
| Interaction and data states | Synthesized — the corpus documents almost none |
| Accessibility floor | From the WCAG 2.2 specification |

**When a user's product falls in a synthesized category, say so.** They should know whether they are
getting evidence or a considered argument. If their context contradicts synthesized guidance, they
are probably right — say that rather than defending the document.

---

## Never

- Never copy a brand's design system wholesale. Adopt structural principles; derive your own values.
- Never apply marketing density (96px rhythm, 72px display type) to an application surface.
- Never wrap every content block in a rounded shadowed card, or nest cards.
- Never use more than one decorative device (gradient, glow, pattern) on a surface.
- Never let a wide table shrink — scroll it with the identifying column pinned, or transform rows
  into cards.
- Never silently omit a capability on mobile. If it genuinely does not work, say so in the interface.
- Never claim work is verified without having checked it. "Should work" is not "works".
