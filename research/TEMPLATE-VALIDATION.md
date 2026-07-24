# Template Validation — Build Test

The templates were unproven. This is what happened when one was actually built.

**Test:** an operator dashboard ("invoice exceptions queue") implemented strictly from
[../templates/DESIGN.dashboard-admin.md](../templates/DESIGN.dashboard-admin.md) as a
single-file HTML/CSS/JS build, then rendered in a real browser, measured programmatically, and
audited against [../checklists/dashboard-review.md](../checklists/dashboard-review.md) and
[../checklists/foundation-review.md](../checklists/foundation-review.md).

**Why this template:** dashboard is the weakest-evidence category with the largest component
surface — the highest-risk combination in the layer.

**Result: 10 defects found, of which 2 were internal self-contradictions the template could not
satisfy.** All 10 are now fixed. The build artifact was a test instrument and was not committed;
it lived in a session scratchpad.

---

## Method

| | |
|---|---|
| Scope | App shell, sticky chrome, metric tiles, data table, 6 data states, bulk actions, destructive confirmation with typed confirmation, command palette, toasts, density switcher, theme switcher, mobile card transform |
| Rendered at | 1280×860 and 375×760, light and dark |
| Measured | Row heights vs. declared per density mode · sticky chrome as % of viewport · 18 contrast pairs per theme, computed from resolved CSS custom properties · touch-target audit · overflow audit |
| Not measured | Real assistive-technology behaviour; real user performance |

Measurement ran in-page against computed styles, so the numbers are what a browser actually
produced — not what the CSS intended.

---

## Defects found

Severity: **critical** = the template cannot be satisfied as written, or produces an
accessibility failure. **major** = produces a visible defect. **minor** = forces the builder to
invent a spec.

### T-01 — critical — Density modes did not control density

The template declared row heights of 32 / 40 / 48px per density mode. Measured actual heights:

| Mode | Declared | Actual | Rows exceeding declared |
|---|---|---|---|
| Compact | 32px | 50–51px | **8 of 8** |
| Standard | 40px | 57–58px | **8 of 8** |
| Comfortable | 48px | 94–118px | **8 of 8** |

Every row in every mode exceeded its declared height, by 45–146%. Comfortable rows were also
*ragged* (94–118px) because one supplier name wrapped to three lines. The
comfortable:compact ratio came out at **1.92** against an intended 1.50.

**Cause:** the template specified row height but said nothing about column widths or per-column
wrap/truncate policy. Content wrapping silently overrode the entire density system. A density
system that specifies row height without specifying column sizing does not work.

**Fix applied:** added a `table-columns` block with an explicit `policy` per column
(`truncate` / `wrap-2` / `nowrap` / `fixed`) plus widths, a requirement to use
`table-layout: fixed` with a `<colgroup>`, and a rule that the table's `min-width` is the sum of
column widths with the container scrolling horizontally.

**Re-test after fix:**

| Mode | Declared | Actual | Rows exceeding |
|---|---|---|---|
| Compact | 32px | 33–34px | **0 of 8** |
| Standard | 40px | 40–58px | 1 of 8 |
| Comfortable | 48px | 48–71px | 4 of 8 |

Table height for 8 rows fell from 405/460/779px to 270/338/478px. Compact became exact.

**Residual, and it is inherent:** a `wrap-2` column that fits one line at 13px needs two at
16px, so the wrap penalty *grows* with density. Ratio improved 1.92 → 1.77 but did not reach
1.50. Rather than pretend otherwise, the template now states the tradeoff explicitly: **zero
wrapping columns gives exact row heights; one wrapping column makes the declared height a floor
and yields ~1.75×.** Two wrapping columns are prohibited.

### T-02 — critical — The sticky-chrome budget was arithmetically impossible

The template declared `sticky-budget: "20vh"` and, separately, specified `top-bar: 56px`,
`page-header: 56px`, `toolbar: 48px` — while also *requiring* a sticky table header.

Measured with all four sticky, as the template instructed:

| Viewport height | Sticky chrome | % of viewport | Budget |
|---|---|---|---|
| 860px | 196px | **22.8%** | 20% |
| 768px | 196px | **25.5%** | 20% |

The template's own values could not satisfy its own budget. This is the clearest example of a
defect invisible on the page and obvious in a build.

**Fix applied:** added `sticky-layers-max: 3` and a `sticky-priority` order
(`table-header` highest — it is what makes a long table readable; `page-header` lowest — it
scrolls away harmlessly), plus an instruction to reduce heights and re-measure if a view
genuinely needs all four.

**Re-test:** 109px = **12.7%** at 860px, **14.2%** at 768px. Within budget.

### T-03 — critical — The dark-mode rule contradicted the contrast requirement

The template instructed: lighten and desaturate saturated colours for dark mode. It separately
specified filled buttons as `text: "#ffffff"`.

**These are incompatible.** Lightening a fill while keeping a white label always reduces
contrast. Measured in dark mode:

| Pair | Ratio | Required | Result |
|---|---|---|---|
| White on lightened accent fill | **3.68:1** | 4.5:1 | Fail |
| White on lightened danger fill | **2.92:1** | 4.5:1 | Fail |

Following the template correctly produced two accessibility failures on the two most important
buttons in the product.

**Fix applied — to the template, the foundation, and the foundation template**, since the rule
originated in [../COMMON-FOUNDATION.md](../COMMON-FOUNDATION.md) §6 and propagated. Each action
colour now splits into two dark-mode tokens:

| Token | Use | Constraint |
|---|---|---|
| `action.primary` | Filled background | ≥4.5:1 against its own label — usually means *not* lightening |
| `action.primary-on-dark` | Text, icons, links, borders on dark | ≥4.5:1 against the dark surface |

**Re-test:** white on primary fill **5.17:1**, white on destructive fill **5.33:1**,
`-on-dark` as text **6.86:1**. All pass.

### T-04 — major — The responsive table omitted the page header and toolbar

Both are specified as sticky with fixed heights. Neither appeared in the template's responsive
table, so neither had defined behaviour below 768px.

Consequence at 375px: the page header, laid out as a non-wrapping flex row (title + two
actions), overflowed its 345px container to **413px**, forcing horizontal scroll on `<main>` — a
blocker under the foundation checklist. The sticky toolbar, offset by a hard-coded
`top: 56px`, also overlapped content once the title wrapped to two lines.

**Fix applied:** added page-header and toolbar rows to the responsive table (both un-stick and
wrap below 768px), plus two general rules — anything specified as sticky with a fixed height
needs an explicit responsive rule, and a fixed `top:` offset is wrong the moment the element
above it wraps.

### T-05 — major — The touch guard was a single point of failure

The template's only mechanism for forcing comfortable density on touch was
`@media (pointer: coarse)`.

At a 375px viewport reporting a fine pointer, the build shipped **26 interactive targets below
44px** — violating the 44px floor the template itself lists as mandatory.

**Fix applied:** guard on both signals — `(pointer: coarse), (max-width: 767px)`.

### T-06 — minor — No z-index scale

The template specifies sticky chrome, pinned columns, a bulk bar, dropdowns, a scrim, modals,
and toasts — all of which must stack correctly — but provided no z-index tokens. The build
required inventing seven values, and the pinned-column-over-sticky-header interaction is
genuinely subtle.

**Fix applied:** added a seven-step `z-index` block, with a note that the pinned column must
sit above the sticky header's row.

### T-07 — minor — Toast position and stacking unspecified

Width, padding, radius, and elevation were given. Position, stack direction, gap, maximum
visible, auto-dismiss timing, and mobile behaviour were not.

**Fix applied:** added position, inset, stack direction and gap, `max-visible: 3`, auto-dismiss
timing with an explicit "never for errors", and mobile behaviour.

### T-08 — minor — No skeleton specification

The template requires skeletons matching final layout but supplied no fill token and no
animation guidance.

**Fix applied:** added a `skeleton` component spec with fill, radius, animation, reduced-motion
behaviour, and the rule that a skeleton matches the final element's box rather than being a
generic bar.

### T-09 — minor — Pinned column had no minimum width

The template requires pinning the identifying column but gave no width guidance. At the width
the layout produced (109px), a 14-character monospace reference wrapped to two lines — defeating
the purpose of pinning.

**Fix applied:** `min-width: 130px` on the identifier column, `nowrap` policy, and a rule to
size it to the longest real value. Re-test at 140px: no wrapping.

### T-10 — minor — Mobile card transform had no anatomy

The template said "transform to cards **or** scroll + pinned column" without specifying what a
card contains.

**Fix applied:** a four-line card anatomy table, a 44px leading checkbox hit area, a
visible-label requirement (the table header is hidden), and guidance to show 3–4 fields rather
than all ten.

---

## Checklist defect found

### C-01 — The contrast rule was stated too broadly

[../checklists/foundation-review.md](../checklists/foundation-review.md) required
"UI boundaries ≥3:1" without qualification. Applied literally, the build's table row dividers
measured **1.36:1** and registered as failures — but WCAG 1.4.11 covers boundaries needed to
*identify* a control or its state, not decorative separators. The rule as written generates
false blockers, which trains reviewers to ignore it.

**Fix applied:** the rule now distinguishes meaningful boundaries (input borders, unchecked
checkboxes, focus rings, toggle tracks) from exempt decorative separators (row rules, dividers,
card hairlines), and adds a dedicated filled-button-label check — the pair T-03 showed is most
often broken.

Also softened: the disabled-state contrast item now notes that WCAG 1.4.3 exempts disabled
controls, so ≥3:1 there is a quality bar rather than a conformance requirement. The build
measured 2.92:1 for disabled text, which is a defensible choice and was previously flagged as a
failure.

---

## What the test also confirmed working

Not everything broke. These parts of the template survived contact with a real build unchanged:

- The two-layer token architecture. Switching theme and density touched only `:root` attributes;
  no component needed editing. This is the layer's central structural claim and it held.
- All seven data states were specifiable and distinguishable — first-run empty, filtered-empty
  (with a genuinely different message), initial loading, refresh-keeps-data, partial data with
  targeted retry, error with a copyable reference, permission-denied.
- Reserved space for the bulk-action bar prevented layout shift on selection, exactly as
  specified.
- Typed confirmation for the destructive action, with the count named in the button.
- Per-item partial-failure reporting ("2 of 3 rejected. 1 failed: … is locked by A. Reyes").
- Per-metric direction semantics — the tile where "up" is bad rendered correctly in the danger
  colour, confirming the template was right to reject hard-coded green-for-increase.
- "No data" rendering distinctly from zero.
- Em-dash for empty cells; tabular figures aligning correctly in the amount column.
- No zebra striping, so hover and selection both read clearly.

---

## What this changes about confidence in the layer

**The 10 defects were all in the template, not in the corpus analysis.** Nothing in
[VALUE-DISTRIBUTIONS.md](VALUE-DISTRIBUTIONS.md) or
[PATTERN-CLUSTERS.md](PATTERN-CLUSTERS.md) was contradicted. The failures were specification
gaps and internal contradictions in the *derived* guidance — which is exactly the class of
defect a build test is for, and exactly the class that reading cannot find.

**Two of the three critical defects were self-contradictions.** T-02 and T-03 were cases where
the template gave two instructions that could not both be followed. Neither was visible on
review; both were unmissable within minutes of building. That is the strongest argument for
building over reviewing.

**The dashboard template is now materially more trustworthy than the other nine.** It has been
executed once; they have not. Its evidence base is unchanged — still no corpus sources — but its
*internal consistency* is now verified rather than assumed.

**Recommendation:** run the same test on the conversational-AI and spatial templates before
relying on them. Conversational AI has the most intricate state machine (streaming, stop,
layout stability) and spatial has the most unusual layout constraints (occlusion budget,
panel-over-canvas) — both are prime candidates for the same class of self-contradiction found
here.

## Reproducing this

1. Build the smallest complete surface the template describes — one screen, but *every* state.
2. Render it in a real browser at 1280×860 and 375×760, in both themes.
3. Measure, do not eyeball. Specifically:
   - rendered row/control heights against declared values, in **every** density mode
   - total sticky chrome as a percentage of viewport height, at 768px height
   - every contrast pair, computed from resolved custom properties, in **both** themes —
     including white-on-fill for every filled button
   - every interactive target's box at 375px
   - `scrollWidth > clientWidth` on every element, to find overflow sources
4. Audit against the foundation checklist, then the category checklist.
5. Fix the **template**, not just the build. Then re-measure to confirm.

Step 5 is the point. A build that works while the template still misleads has fixed nothing.
