# Foundation Review Checklist

Applies to every product. Run this before the category checklist.

Reference: [../COMMON-FOUNDATION.md](../COMMON-FOUNDATION.md) ·
[../ANTI-PATTERNS.md](../ANTI-PATTERNS.md)

---

## 1. Tokens

- [ ] No hard-coded colours in components (hex, `rgb()`, `hsl()`, named colours)
- [ ] No hard-coded spacing, radius, font-size, or duration values
- [ ] Components reference **semantic** tokens, not primitives
- [ ] Every semantic token in use is defined for **both** light and dark
- [ ] The minimum semantic set exists: surface, text, border, action, status, focus, utility
- [ ] Status tokens have text **and** surface variants — a fill light enough to sit behind text is
      too light to be text
- [ ] Values used that have no token are recorded as `DESIGN.md` gaps, not invented in code

## 2. Scales

- [ ] All spacing values are on the 4px grid
- [ ] Adjacent type steps differ by 1.15×–1.35×
- [ ] Line-height falls as size rises (1.5 body → 1.05–1.15 display)
- [ ] Negative tracking scales with display size above ~40px
- [ ] Small uppercase text has **positive** tracking
- [ ] One radius character throughout; nesting rule applied (inner = outer − gap)
- [ ] Radius scales with component size — no 16px radius on a 32px control
- [ ] Elevation uses a defined 0–4 scale; no arbitrary shadow values
- [ ] Mechanisms are not stacked at one level (border **and** shadow **and** surface lift)

## 3. Typography

- [ ] Body text ≥14px; ≥16px on mobile
- [ ] Display size respects the category ceiling (marketing 56–80 · docs 36–56 · app 24–32 ·
      dashboard 20–28)
- [ ] Prose measure 60–70 characters regardless of container width
- [ ] Tabular figures wherever numbers are compared vertically
- [ ] Monospace used only for code, paths, identifiers, and aligned data
- [ ] A substitution note exists for any proprietary typeface
- [ ] Heading levels are distinguishable at a glance in a scroll-past

## 4. Colour

- [ ] Accent count matches `DESIGN.md`; accent is scarce (primary action, brand mark, focus, active)
- [ ] Any additional accent maps to something structural — not decoration
- [ ] Semantic colours are not reused decoratively
- [ ] Danger is distinguishable from the brand hue if the brand is red
- [ ] `status-info` is distinguishable from `action-primary` if both are blue
- [ ] Neutral temperature is consistent (warm canvas → warm ink)

## 5. Light and dark

- [ ] Dark mode is **derived**, not inverted
- [ ] Dark canvas is not `#000000`; dark text is not `#ffffff`
- [ ] Raised surfaces get **lighter** in both modes
- [ ] Dark elevation uses lightness steps, not shadow
- [ ] Borders lighten in dark mode instead of darkening
- [ ] The brand accent has a dark-mode variant that holds contrast
- [ ] Saturated colours are desaturated 10–20% for dark

## 6. Interaction states

For every interactive element:

- [ ] Default
- [ ] Hover (pointer only)
- [ ] Focus-visible — 2px ring, 2px offset, ≥3:1 against element **and** surface
- [ ] Active/pressed, distinct from hover
- [ ] Disabled — reduced contrast, `not-allowed`, **and an explanation of why**. Aim for ≥3:1
      as a quality bar; note that WCAG 1.4.3 **exempts** disabled controls, so a value below
      3:1 here is a judgment call, not a conformance failure
- [ ] Loading — in place, dimensions preserved, interaction disabled
- [ ] Selected — distinct from both hover and focus
- [ ] Error — border + icon + message

- [ ] No `outline: none` without a replacement
- [ ] Hover, focus, and selected are three visibly different things

## 7. Data states

For every data-bearing view:

- [ ] First-run empty — explains and offers a primary action
- [ ] Filtered-empty — **distinct** from first-run; offers to clear filters
- [ ] Initial loading — skeleton matching final layout
- [ ] Refresh loading — existing data stays visible
- [ ] Partial data — shows what loaded, marks what failed, offers retry
- [ ] Error — what happened, what to do, retry
- [ ] Permission denied — what is needed, who grants it

## 8. Layout and responsive

- [ ] No horizontal page scroll at any width (bounded containers may scroll internally)
- [ ] Behaviour defined per element at each breakpoint (resize/reflow/collapse/stack/scroll/
      drawer/transform/defer/omit)
- [ ] Wide tables scroll with a pinned identifying column, or transform — never squeeze
- [ ] Every hover affordance has a tap equivalent
- [ ] Touch targets ≥44px with ≥8px separation below 1024px
- [ ] Sticky chrome ≤ ~20% of viewport height
- [ ] Page padding ≥16px on mobile
- [ ] Density is coherent — spacing, control height, and type size agree
- [ ] Omitted capabilities are **stated in the interface**, not silently hidden

## 9. Layout stability

- [ ] Images have intrinsic dimensions
- [ ] Space reserved for async content
- [ ] Font loading does not shift text
- [ ] Streaming or polling content does not shift layout
- [ ] Nothing jumps on a slow-network reload

## 10. Accessibility

- [ ] Body text ≥4.5:1; large text (≥24px, or ≥19px bold) ≥3:1 — **computed, both modes**
- [ ] **Meaningful** UI boundaries ≥3:1 — the edges needed to *identify* a control or its
      state: input borders, unchecked checkboxes, focus rings, toggle tracks, chart series
      boundaries. Purely decorative separators (table row rules, section dividers, card
      hairlines) are **exempt** under WCAG 1.4.11 and should not be flagged. A build test
      confirmed the unqualified version of this rule generates false blockers: table row
      dividers measured 1.36:1, which is correct design and a spurious failure
- [ ] **Filled buttons: label vs. fill ≥4.5:1, computed in both modes.** This is the pair most
      often broken by a dark-mode "lighten the accent" rule — lightening a fill while keeping a
      white label always reduces contrast. Measured failures in a real build: 3.68:1 and 2.92:1
- [ ] Focus visible on every interactive element
- [ ] Every action keyboard-reachable; logical tab order; no traps
- [ ] Modals trap focus and return it to the trigger on close
- [ ] Nothing conveyed by colour alone (**verify by greyscaling the OS**)
- [ ] Form fields have programmatic labels; placeholder is not a label
- [ ] Errors associated with their field and announced
- [ ] One `h1`; no skipped heading levels
- [ ] Meaningful `alt`; `alt=""` on decorative images
- [ ] Icon-only buttons have accessible names
- [ ] Async changes announced via live regions, `polite` not `assertive`
- [ ] `prefers-reduced-motion` honoured with state changes preserved
- [ ] Usable at 200% zoom
- [ ] Skip-to-content link, visible on focus

## 11. Motion

- [ ] Every animation serves causality, hierarchy, progress, or spatial change
- [ ] Durations within scale (100 / 150–200 / 250–300ms)
- [ ] Only `transform` and `opacity` animated — not `width`, `height`, `top`
- [ ] Nothing loops except progress indicators
- [ ] No animation delays a blocking interaction
- [ ] Reduced motion replaces movement without removing the state change

## 12. Consistency

- [ ] One component per purpose; variants documented and distinct
- [ ] Adjacent controls have matching heights
- [ ] Naming follows existing conventions
- [ ] No duplicate components serving the same purpose
- [ ] No card containing a single paragraph; no nested cards
- [ ] Navigation destinations not duplicated across two systems

## 13. Content

- [ ] One primary action per view
- [ ] Buttons name outcomes, not "OK" / "Submit"
- [ ] Destructive actions name the target and count
- [ ] Errors state what happened and what to do next
- [ ] Numbers have units and timeframes
- [ ] Dates: absolute in records, relative for recency
- [ ] Sentence case for UI text
- [ ] One canonical term per object, used everywhere

## 14. Sign-off

- [ ] All **blockers** resolved
- [ ] `DESIGN.md` gaps recorded and assigned
- [ ] Deviations from `DESIGN.md` documented with reasons **in `DESIGN.md`** — an undocumented
      exception is indistinguishable from a mistake six months later
- [ ] Verified claims are based on things actually checked; anything unverified is stated as such
