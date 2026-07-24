# Prompt Bootstrap

For any agent with no file convention — a fresh ChatGPT conversation, a web chat, a coding agent
without `AGENTS.md` support. **Paste the block below at the start of the conversation.**

One screen. Self-contained: it carries the rules inline, so it works with no repo access and no
network.

---

```
Follow these design rules for any UI work in this conversation. They come from a synthesis of 74
real product design systems. Where a rule is labelled SYNTHESIZED, it is reasoning rather than
evidence — tell me if my context contradicts it.

PROCESS
- Inspect the existing code before generating. Tell me what components, tokens, and conventions
  already exist, and what you plan to reuse.
- Reuse before creating. Extend a near-miss component; create new only with a stated reason.
- Never break working functionality for a visual change. Restyle, don't rewrite. If a visual goal
  needs a behaviour change, stop and ask me.
- End every response with: assumptions, deviations, INVENTED VALUES (anything I didn't specify),
  unresolved decisions, components reused vs. created, and what you actually verified.

TOKENS
- Two layers: primitives (raw values) -> semantics (intent). Components consume semantics only.
- No hard-coded colours, spacing, radii, or font sizes. A value with no token is a gap — report it,
  don't invent a literal.

STATES (most commonly skipped — do not skip)
- Eight interaction states per interactive element: default, hover, focus-visible, active,
  disabled (with a reason shown), loading, selected, error.
- Seven data states per data view: first-run empty (with a primary action), filtered-empty (a
  DIFFERENT message offering to clear filters), initial loading (skeleton matching final layout),
  refresh (KEEPS existing data visible), partial data, error with retry, permission denied.
- Hover, focus, and selected mean three different things and need three different appearances.

ACCESSIBILITY (a constraint now, not a later pass)
- Body text >=4.5:1; large text and meaningful UI boundaries >=3:1.
- Visible focus ring always: 2px, 2px offset, >=3:1 against both element and surface. Never
  outline:none without a replacement.
- Touch targets >=44x44px, >=8px apart. Full keyboard operation, no focus traps.
- Never convey meaning by colour alone — always add an icon or text label.
- Form fields need real labels. Placeholder is NOT a label.
- Honour prefers-reduced-motion without removing the state change.

LAYOUT AND TYPE
- 4px spacing grid, 8px preferred increments.
- 16px body text. Never below 14px; never below 16px on mobile.
- Prose measure 60-70 characters REGARDLESS of container width. Container width and reading
  measure are two different numbers.
- Type steps 1.15x-1.35x apart. Line-height falls as size rises (1.5 body -> 1.05-1.15 display).
- Tabular figures wherever numbers are compared vertically.
- Breakpoints: 480 / 768 / 1024 / 1280 / 1440.
- Display ceiling by surface: marketing 56-80px, docs 36-56px, app 24-32px, dashboard 20-28px.
  Marketing display sizes inside an application are a category error.

COLOUR AND DEPTH
- ONE accent colour, reserved for primary action, brand mark, and focus. Any additional accent must
  map to something structural (product line, category, data series) — never decoration.
- Border-first elevation. Border or surface step for grouping; shadow only for things that float.
  Never stack border + shadow + surface lift at one level.
- Dark mode is DERIVED, not inverted. Raised surfaces get LIGHTER in both modes. Shadow barely
  reads on dark — use lightness steps. Dark canvas is not #000000; dark text is not #ffffff.
- NEVER lighten a filled button's background while keeping a white label — that always reduces
  contrast and usually fails 4.5:1. Use two tokens: the fill (not lightened) and a lightened
  variant for text/icons/borders only.

MOTION
- Motion must communicate causality, hierarchy, progress, or spatial change. Otherwise remove it.
- Animate transform and opacity only. Never width, height, or top.
- 100ms feedback, 150-200ms small transitions, 250-300ms panels. Nothing loops except progress.
  Never animate a blocking interaction.

DENSITY — from how often one person uses the surface
- Once/rarely: spacious. 80-96px section rhythm, 16-18px body, 44-48px controls.
- Weekly: default. 48-64px rhythm, 16px body, 40px controls, 48px table rows.
- Daily/all day: compact. 24-32px rhythm, 13-14px body, 32-36px controls, 32-40px rows.
- Compact is POINTER-ONLY. On touch, 44px targets override it.

CATEGORY sets density, navigation, and component set. It does NOT set visual tone — tone comes
from the brand. The same product category is rendered in four incompatible tones across the source
corpus, so don't ask "what should a fintech app look like"; ask how dense it is, how it's
navigated, and which components carry the work.

Ask me which of these applies before choosing values: chat/assistant (SYNTHESIZED) ·
marketing/landing (evidence-backed) · docs/informational · dashboard/admin/ops (SYNTHESIZED) ·
multi-role platform (SYNTHESIZED) · developer tool · e-commerce/checkout · financial/high-trust ·
editorial/long-form · analytics/BI (SYNTHESIZED) · map/spatial/3D (FULLY SYNTHESIZED).

NEVER
- Never copy one brand's design system wholesale. Adopt structural principles; derive your own
  values.
- Never wrap every block in a rounded shadowed card, or nest cards.
- Never use more than one decorative device (gradient, glow, pattern) per surface.
- Never let a wide table shrink — scroll it with the identifying column pinned, or transform rows
  into cards.
- Never silently omit a capability on mobile. If it genuinely doesn't work, say so in the interface.
- Never claim something is verified without having checked it.
```

---

## Notes on using this

- **The last line of the PROCESS block does most of the work.** Requiring a report of *invented
  values* is what surfaces the places your spec was silent, which is where design systems drift.
- **The SYNTHESIZED labels are deliberate.** They tell the agent which rules to hold loosely, so it
  defers to your context instead of arguing from a document.
- For repeated use, prefer `AGENTS.design-intelligence.md` (Codex, Cursor, Copilot) or the Claude
  Code skill — both persist across sessions instead of needing a paste each time.
- If the agent can read files, point it at `AGENT-ENTRY.md` instead. This bootstrap is a compressed
  substitute, not a replacement for the full guides.
