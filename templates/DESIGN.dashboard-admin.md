---
# Dashboard / administration / analytics DESIGN.md
# Copy to your project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md. Category guide: categories/dashboard-admin.md
#   For analytics, also apply categories/data-analytics.md (charts, palettes, queries).
#   NOTE: both guides are predominantly SYNTHESIZED. Validate with real operators early.

version: 1
name: [[SET: product-name]]-design-system
category: dashboard-admin
density: [[CHOOSE: standard (default) | compact | comfortable]]
mode: [[CHOOSE: light | dark | both]]
description: >
  [[SET: What operators do here, how many hours a day they do it, and what a mistake costs.
  The governing constraint for this category is that someone uses this eight hours a day —
  every value below should be defensible against that.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]", info: "[[SET]]" }
  # Categorical series palette — ONLY if charts are present. 6-8 hues, greyscale-distinguishable,
  # no collision with status hues, assigned deterministically per series key.
  series: [ "[[SET]]", "[[SET]]", "[[SET]]", "[[SET]]", "[[SET]]", "[[SET]]" ]

semantic:
  light:
    surface-canvas: "{primitives.neutral.50}"
    surface-shell: "#ffffff"
    surface-raised: "#ffffff"
    surface-sunken: "{primitives.neutral.100}"     # table header, code wells
    surface-row-hover: "{primitives.neutral.100}"
    surface-row-selected: "[[SET: accent tint at ~8%]]"
    surface-overlay: "#ffffff"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    text-disabled: "{primitives.neutral.400}"
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    action-primary: "{primitives.accent.600}"
    action-destructive: "{primitives.status.danger}"
    status-success: "{primitives.status.success}"
    status-success-surface: "[[SET: tint, >=3:1 vs canvas]]"
    status-warning: "[[SET: darkened — amber text rarely reaches 4.5:1]]"
    status-warning-surface: "[[SET: tint]]"
    status-danger: "{primitives.status.danger}"
    status-danger-surface: "[[SET: tint]]"
    status-info: "{primitives.status.info}"
    status-info-surface: "[[SET: tint]]"
    focus-ring: "{primitives.accent.500}"
    scrim: "rgba(0,0,0,0.40)"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-shell: "{primitives.neutral.900}"
    surface-raised: "{primitives.neutral.900}"
    surface-sunken: "#000000"
    surface-row-hover: "{primitives.neutral.800}"
    surface-row-selected: "[[SET: accent tint at ~14%]]"
    surface-overlay: "{primitives.neutral.800}"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    text-disabled: "{primitives.neutral.600}"
    border-subtle: "rgba(255,255,255,0.08)"
    border-default: "rgba(255,255,255,0.14)"
    # CRITICAL — verified by build test (research/TEMPLATE-VALIDATION.md T-03).
    # "Lighten saturated colours for dark mode" and "filled buttons use #ffffff text"
    # are CONTRADICTORY: lightening a fill while keeping white text always REDUCES
    # contrast. Measured on a real build: white on lightened accent.500 = 3.68:1,
    # white on a lightened danger = 2.92:1. Both fail the 4.5:1 floor.
    # Dark mode therefore needs TWO tokens per action colour:
    #   *-fill    the filled-button background. Must keep >=4.5:1 against its own
    #             label colour. Usually this means NOT lightening it.
    #   *-on-dark the lightened variant, for TEXT, ICONS, LINKS and BORDERS on dark
    #             surfaces — which is where the lightening rule actually applies.
    # Never use an *-on-dark value as a filled-button background.
    action-primary: "{primitives.accent.600}"          # fill: keeps white label at >=4.5:1
    action-primary-on-dark: "{primitives.accent.400}"  # text/icon/link/border use only
    action-destructive: "{primitives.status.danger}"   # fill: verify white label >=4.5:1
    action-destructive-on-dark: "[[SET: lightened 10-20% — TEXT/ICON/BORDER ONLY]]"
    status-success: "[[SET: lightened]]"
    status-success-surface: "[[SET: dark tint]]"
    status-warning: "[[SET: lightened]]"
    status-warning-surface: "[[SET: dark tint]]"
    status-danger: "[[SET: lightened]]"
    status-danger-surface: "[[SET: dark tint]]"
    status-info: "[[SET: lightened]]"
    status-info-surface: "[[SET: dark tint]]"
    focus-ring: "{primitives.accent.400}"
    scrim: "rgba(0,0,0,0.60)"

typography:
  families:
    body: "[[SET: family with good small-size legibility and unambiguous l/I/1]]"
    mono: "[[SET: family, ui-monospace, monospace]]"
  substitutes: { body: "[[SET: if proprietary]]" }
  scale:
    # Low ceiling by design. Marketing display sizes have no place here.
    heading-1: { size: 24px, weight: 600, lineHeight: 1.25, tracking: -0.3px }
    heading-2: { size: 18px, weight: 600, lineHeight: 1.35, tracking: -0.2px }
    heading-3: { size: 15px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:      { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }
    body-sm:   { size: 13px, weight: 400, lineHeight: 1.40, tracking: 0 }
    caption:   { size: 12px, weight: 400, lineHeight: 1.35, tracking: 0.1px }
    overline:  { size: 11px, weight: 600, lineHeight: 1.30, tracking: 0.6px, transform: uppercase }
    label:     { size: 13px, weight: 500, lineHeight: 1.20, tracking: 0 }
    code:      { size: 13px, weight: 400, lineHeight: 1.50, tracking: 0, family: mono }
    numeric:   { size: 14px, weight: 400, lineHeight: 1.40, tracking: 0, features: "tabular-nums" }
    metric:    { size: 28px, weight: 600, lineHeight: 1.10, tracking: -0.5px, features: "tabular-nums" }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px }
  section: 24px       # NOT 96px. This is not a marketing page.
  page-padding: { mobile: 16px, tablet: 16px, desktop: 24px }

radius: { none: 0, xs: 3px, sm: 4px, md: 6px, lg: 8px, full: 9999px }
# Tighter than the foundation default — near-square geometry supports density.

# Z-INDEX SCALE — added after build test (T-06). This template specifies overlapping
# sticky, pinned, bulk-bar, dropdown, modal and toast layers but previously gave no
# z-index tokens, forcing a builder to invent seven values.
z-index:
  sticky: 10        # top bar, page header, toolbar, table header
  pinned: 11        # pinned table column (must sit above the sticky header's row)
  bulk-bar: 20
  dropdown: 30
  scrim: 40
  modal: 41
  toast: 50

layout:
  container: fluid
  prose: 640px
  top-bar: 56px
  page-header: 56px
  toolbar: 48px
  sidebar-nav: 240px
  sidebar-rail: 56px
  detail-panel: 360px

  # STICKY BUDGET — reconciled after build test (research/TEMPLATE-VALIDATION.md T-02).
  # The earlier version of this template declared a 20vh budget AND specified
  # top-bar 56 + page-header 56 + toolbar 48 + a required sticky table header (~36).
  # That sums to 196px = 22.8% at 860px viewport height and 25.5% at 768px.
  # The budget was arithmetically unachievable using the template's own values.
  # Resolution: AT MOST THREE of the four layers may be sticky at once. Pick per view.
  sticky-budget: "20vh"
  sticky-layers-max: 3
  sticky-priority: [table-header, top-bar, toolbar, page-header]
  # table-header is highest priority: it is what makes a long table readable.
  # page-header is lowest: it usually scrolls away harmlessly.
  # If a view genuinely needs all four, reduce top-bar to 48px and toolbar to 40px
  # and re-measure. Do not ship an unmeasured sticky stack.
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

density-modes:
  compact:     { row: 32px, control: 32px, body: 13px, card-padding: 12px, page-padding: 16px, cell-padding: "6px 10px" }
  standard:    { row: 40px, control: 36px, body: 14px, card-padding: 16px, page-padding: 24px, cell-padding: "8px 12px" }
  comfortable: { row: 48px, control: 40px, body: 16px, card-padding: 24px, page-padding: 32px, cell-padding: "12px 16px" }
# Density scales dimensions only — never contrast.
#
# TOUCH GUARD — build test found this insufficient (T-05).
# `@media (pointer: coarse)` alone is NOT enough: at a 375px viewport reporting a fine
# pointer, a real build shipped 26 targets below 44px. Guard on BOTH signals:
#   @media (pointer: coarse), (max-width: 767px) { ...force comfortable... }
touch-guard: "(pointer: coarse), (max-width: 767px)"

# ---------------------------------------------------------------------------
# ROW HEIGHT IS A FLOOR, NOT A HEIGHT — added after build test (T-01).
#
# The row heights above do NOT control density on their own. A real build measured:
#   declared 32px -> actual 50-51px      declared 40px -> actual 57-58px
#   declared 48px -> actual 94-118px     (100% of rows exceeded declared, all modes)
# Comfortable:compact came out at 1.92x instead of the intended 1.5x, and comfortable
# rows were RAGGED (94-118px) because one supplier name wrapped to three lines.
#
# Cause: content wrapping overrides row height. A density system that specifies row
# height without specifying column width and per-column wrap policy does not work.
# Every column therefore needs an explicit sizing + overflow policy.
# ---------------------------------------------------------------------------
table-columns:
  # policy: truncate | wrap-2 | nowrap | fixed
  #   truncate = single line, ellipsis, full value on hover AND focus
  #   wrap-2   = max 2 lines then ellipsis (use -webkit-line-clamp)
  #   nowrap   = never wraps; column widens instead (identifiers, amounts, dates)
  #   fixed    = fixed width (checkbox, status, actions)
  - { key: select,     policy: fixed,    width: 40px }
  - { key: identifier, policy: nowrap,   min-width: 130px, pinned: true, font: mono }
  - { key: name,       policy: truncate, min-width: 160px, max-width: 260px }
  - { key: description,policy: wrap-2,   min-width: 140px, max-width: 240px }
  - { key: amount,     policy: nowrap,   min-width: 96px,  align: right, font: numeric }
  - { key: age,        policy: nowrap,   min-width: 64px,  align: right }
  - { key: status,     policy: fixed,    width: 128px }
  - { key: owner,      policy: truncate, min-width: 96px }
  - { key: timestamp,  policy: nowrap,   min-width: 168px, font: mono }
  - { key: actions,    policy: fixed,    width: 88px, align: right }
# Rules, all confirmed by measurement:
# - The pinned identifier column MUST be `nowrap` with a min-width sized to the longest
#   REAL value. Measured failure: a 109px pinned column wrapped a 14-character reference
#   across two lines, defeating the point of pinning. 140px fixed it.
# - Use `table-layout: fixed` with an explicit <colgroup>. Without it the browser sizes
#   columns by content and the widths above have no effect.
# - Set `min-width` on the table to the sum of column widths, and let the container
#   scroll horizontally. That is the intended behaviour, not a defect.
#
# - THE WRAPPING TRADEOFF. Applying the policies above took row heights from
#   32/40/48 declared -> 50/58/94-118 actual, down to 33/40-58/48-71. Compact became
#   exact (0 of 8 rows exceeded). Standard and comfortable did NOT: 1 of 8 and 4 of 8
#   still exceeded, and the comfortable:compact ratio landed at 1.77 instead of 1.50.
#   Cause: a `wrap-2` column that fits on one line at 13px needs two lines at 16px, so
#   the wrap penalty GROWS with density. This is inherent, not a bug.
#   Choose one:
#     (a) FIXED ROW HEIGHT  -> zero wrapping columns. Everything is nowrap or truncate.
#                              Row height then holds exactly in all three modes.
#     (b) VARIABLE ROW HEIGHT -> at most one `wrap-2` column, and treat the declared row
#                              height as a FLOOR. Expect ~1.75x rather than 1.5x between
#                              compact and comfortable, and expect ragged rows.
#   Never allow two wrapping columns: ragged height then compounds unpredictably.
#
# - Verify by MEASURING rendered row heights against declared, in all three density
#   modes, before shipping. This gap was invisible until someone built it.

elevation:
  0: "none"
  1: "1px solid {semantic.border-subtle}"          # cards, panels — border-first
  2: "{semantic.surface-row-hover}"                 # hover
  3: "0 4px 12px rgba(0,0,0,0.10)"                  # dropdowns; dark: surface-overlay + border
  4: "0 12px 32px rgba(0,0,0,0.14)"                 # modals + scrim
  strategy: border-first

motion:
  instant: 100ms
  fast: 150ms
  # Nothing else. Users see these interactions hundreds of times a day; animation is a tax.
  reduced-motion: "instant, state changes preserved"

components:
  button-primary:     { height: 36px, padding: "8px 14px", radius: md, surface: action-primary, text: "#ffffff", type: label }
  button-secondary:   { height: 36px, padding: "8px 14px", radius: md, surface: surface-raised, border: border-default, type: label }
  button-destructive: { height: 36px, padding: "8px 14px", radius: md, surface: action-destructive, text: "#ffffff", type: label }
  text-input:         { height: 36px, padding: "8px 12px", radius: md, border: border-default, type: body }
  table-header:       { height: 36px, surface: surface-sunken, type: overline, sticky: true }
  table-row:          { height: 40px, padding: "8px 12px", border-bottom: border-subtle, type: body }
  # NO zebra striping — it consumes the channel hover and selection need.
  table-cell-numeric: { align: right, type: numeric }
  filter-chip:        { height: 28px, padding: "4px 8px", radius: full, type: caption, removable: true }
  status-badge:       { height: 20px, padding: "2px 8px", radius: full, type: caption }
  metric-tile:        { padding: 16px, radius: lg, border: border-subtle }
  bulk-action-bar:    { height: 48px, surface: surface-overlay, elevation: 3, reserved: true }
  command-palette:    { width: 600px, top: "20vh", radius: lg, elevation: 4 }
  # Toast position/stacking added after build test (T-07) — previously unspecified.
  toast:              { width: 360px, padding: 14px, radius: md, elevation: 3,
                        position: "fixed bottom-right", inset: 24px, stack: "upward, gap 8px",
                        max-visible: 3, dismissible: true, auto-dismiss: "6s (never for errors)",
                        mobile: "full-width minus 2x page-padding, bottom, above safe-area" }
  modal-confirm:      { width: 420px, padding: 24px, radius: lg, elevation: 4, scrim: true }
  # Skeleton added after build test (T-08) — the template required skeletons matching
  # final layout but provided no fill token or animation spec.
  skeleton:           { fill: "surface-sunken (light) / neutral.800 (dark)", radius: sm,
                        animation: "opacity pulse 1.4s ease-in-out infinite",
                        reduced-motion: "static fill, no animation",
                        rule: "match the final element's box, not a generic bar" }
---

# [[SET: Product name]] — Dashboard Design System

## 1. Product context

- **Who uses it:** [[SET: role, expertise, environment]]
- **Hours per day:** [[SET]] ← the governing number
- **Primary task:** [[CHOOSE: monitor | operate | administer | resolve exceptions | analyse]]
- **Typical row counts:** [[SET]]
- **Destructive capabilities:** [[SET]]
- **Real-time updates:** [[CHOOSE: none | occasional | continuous]]
- **Device:** [[SET: desktop primary, and what mobile is used for]]

## 2. Users and roles

| Role | Expertise | Hours/day | Density | Primary view |
|---|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET]] | [[SET]] |

## 3. Experience principles

1. **Whitespace is scroll paid on every visit.** Space must earn its place.
2. **Never lose the user's context.** Refresh keeps data; filters survive reload.
3. **[[SET: your third, and what it rules out]]**

## 4. Visual theme

- **Polarity:** [[SET]] — decide from environment and brand, **not** from genre. There is no
  correlation between "dashboard" and "dark".
- **Decoration budget: none.** No gradients, no glows, no illustration in the working surface.
- **What carries interest:** the data.

## 5. Colour discipline

- One accent on `action-primary` and `focus-ring`.
- **Semantic colours do the real work here.** Full set with surface variants — a warning needs a
  background tint for banners and rows, and it cannot be the same value as warning text.
- **Status = colour + icon + text.** Non-negotiable in dense tables.
- Series palette (if charts): deterministic per series key. If filtering one series changes
  another's colour, the operator loses their mental map on every interaction.

## 6. Layout and shell

- Top bar `{layout.top-bar}` · page header `{layout.page-header}` · toolbar `{layout.toolbar}`
- Sidebar `{layout.sidebar-nav}`, collapsible to `{layout.sidebar-rail}`, **state persisted**
- **Sticky chrome budget `{layout.sticky-budget}`.** Audit this at 768px height — it is easy to
  leave a laptop user 300px of content.
- Section gap `{spacing.section}`

## 7. Navigation

- **Primary:** [[CHOOSE: side nav | rail]] — destinations: [[SET: count]]
- **Command palette:** `Cmd/Ctrl+K`. Also provide a discoverable path to everything in it.
- **Breadcrumbs:** [[CHOOSE: yes (hierarchy 3+ deep) | no]]
- Never duplicate destinations across two navigation systems.
- Current location identifiable even in the collapsed rail.

## 8. Table specification

The primary component. Most of this product's quality lives here.

| Property | Value |
|---|---|
| Header | Sticky, `surface-sunken`, `overline`, sortable with `aria-sort` |
| Rows | `border-subtle` bottom. **No zebra striping** |
| Hover | Full-row `surface-row-hover` |
| Selection | Checkbox column 40px; `surface-row-selected` |
| First column | Identifying value; **pinned** when horizontal scroll is possible |
| Numerics | Right-aligned, `numeric` token with tabular figures |
| Empty cell | Em-dash `—`, never blank |
| Long text | Truncate; full value on hover **and** focus |
| Status | Badge: colour + icon + text |
| Pagination | With totals: "1–50 of 1,340". **Not** infinite scroll |
| Filter state | **In the URL** — shareable, reload-safe |
| Result count | Always: "24 of 1,340" |
| Active filters | Removable chips + clear-all |
| Keyboard | Arrow keys between cells, `Home`/`End`, visible focus, no traps |
| Virtualisation | Above [[SET: row count]] |
| Sort stability | Secondary sort key so equal values do not reorder |

## 9. States — implement every one

| State | Treatment |
|---|---|
| First-run empty | [[SET: explanation + primary action]] |
| Filtered-empty | **Distinct message**; offer to clear filters |
| Initial loading | Skeleton matching final layout |
| Refresh loading | **Keep existing data visible**; subtle indicator. Never blank the table |
| Partial data | Show what loaded; mark what failed; retry the failed part |
| Error | What happened, what to do, retry |
| Permission denied | What is needed, who grants it |
| Stale data | Timestamp + refresh control |
| Offline | Banner; disable network actions; preserve drafts |
| Too many results | Suggest narrowing; never silently truncate |

## 10. Real-time behaviour

- **Never reorder rows under the cursor.** New items get a "N new — show" affordance.
- 1–2s subtle highlight on change, then settle.
- Never steal focus.
- Show connection state; offer pause if the rate makes reading hard.
- Announce via `aria-live="polite"`, never `assertive`.

## 11. Destructive actions

| Consequence | Pattern |
|---|---|
| Reversible | Direct + toast with undo |
| Hard to reverse | Modal naming the target |
| Irreversible | Modal + typed confirmation of the resource name |
| Bulk | Modal + count + sample of affected items |
| Affects others | Modal + explicit impact statement |

- `action-destructive` colour; **not adjacent** to the primary action; **never** the default focus.
- Confirmation button names the action: "Delete project", not "Confirm".
- Prefer archive over delete where the domain allows.

## 12. Bulk actions

- Bar appears on selection **without shifting content** (`reserved: true`).
- Count shown; "select all N" is a separate explicit option.
- Confirmation names count and action.
- **Per-item partial-failure reporting** — never a bare "some items failed".
- Undo where reversible.

## 13. Metrics and charts

- Value in `metric` token with tabular figures.
- **Always a timeframe.** A number without one is not information.
- Comparison with basis: "↑ 12% vs. previous 24h".
- Direction is per-metric — "up" is not universally good (error rate up is bad).
- Show thresholds where they exist.
- "No data" ≠ `0`.
- Charts: axis labels with units, legend when >1 series, **accessible data alternative**,
  incomplete periods marked, bars start at zero.

## 14. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Top bar | Sticky, 56px, actions collapse to overflow menu | Sticky | Sticky |
| **Page header** | **Stacks: title on its own line, actions below. Not sticky.** | Sticky | Sticky |
| **Toolbar** | **Wraps to multiple lines. Not sticky.** | Sticky | Sticky |
| Sidebar | Drawer | Rail | Full |
| Tables | [[CHOOSE: transform to cards | scroll + pinned column]] | Scroll + pin | Full |
| Filters | Drawer, explicit apply | Drawer | Inline |
| Bulk actions | Deferred | Available | Available |
| Detail panel | Full-screen route | Overlay | Docked |
| Metric tiles | 1-up | 2-up | [[SET]]-up |
| Density | **Comfortable forced** | Standard | User choice |

The page-header and toolbar rows were **missing from this table** until a build test caught it
(T-04). The consequence was concrete: a page header laid out as a non-wrapping flex row
(title + 2 actions) overflowed its 345px container to 413px at a 375px viewport, producing
horizontal page scroll — a blocker under
[foundation-review.md](../checklists/foundation-review.md).

Two rules follow, and both matter:

- **Anything specified as sticky with a fixed height needs an explicit responsive rule.** A
  fixed `top:` offset is wrong the moment the element above it wraps to a second line.
- **Below 768px, un-stick the page header and toolbar.** Three sticky layers plus a sticky
  table header does not fit in a 760px-tall viewport, and it violates the sticky budget above.

### Mobile card transform

If you chose `transform to cards`, this is the anatomy — previously unspecified (T-10):

| Slot | Content |
|---|---|
| Line 1 | Identifier (mono, `font-weight: 600`) + status badge, right-aligned |
| Line 2 | Primary name, may wrap to 2 lines |
| Line 3 | Amount (tabular) + age, as a labelled pair |
| Line 4 | Owner + timestamp, `caption` size, `text-secondary` |
| Leading | Selection checkbox, 44px hit area |
| Whole card | Tappable → detail route |

Each field carries a visible label (`data-label` or equivalent) because the table header is
hidden. Aim for 3–4 fields, not all ten — the rest belong on the detail view.

**Capabilities unavailable on small screens:** [[SET: list]] — **and state this in the interface.**
Silent omission reads as a broken product.

## 15. Accessibility commitments

- [ ] Contrast ≥4.5:1 body, ≥3:1 UI and large — verified in both modes
- [ ] Table keyboard navigation: arrows, `Home`/`End`, visible focus, no traps
- [ ] Sortable headers are buttons with `aria-sort`
- [ ] Selection announced: "12 of 340 selected"
- [ ] Status available as text, never colour alone
- [ ] Charts have a data table or text alternative
- [ ] Live updates `polite`, never `assertive`
- [ ] Compact density still meets 44px hit areas on touch
- [ ] Usable at 200% zoom (internal scroll acceptable, page-level not)
- [ ] Toolbars are `role="toolbar"` with arrow-key navigation
- [ ] Disabled controls explain why

## 16. Content guidance

- Numbers get units and timeframes.
- Dates: absolute with timezone in records; relative only for recency.
- Buttons name outcomes.
- Destructive actions name target and count.
- Errors: what happened + what to do.
- Empty states explain and offer an action.
- One canonical term per object, everywhere: [[SET: glossary]]

## 17. Do

- Define all three density modes; persist the user's choice
- Right-align numerics with tabular figures
- Pin the identifying column on horizontally scrolling tables
- Put filter, sort, and page state in the URL
- Keep data visible during refresh
- Reserve space for the bulk-action bar
- Use "N new — show" instead of inserting rows
- Report bulk partial failures per item
- Give charts an accessible alternative

## 18. Do not

- Do not use marketing spacing or display type above 28px
- Do not zebra-stripe
- Do not use infinite scroll on tables
- Do not leave empty cells blank
- Do not blank the table on refresh
- Do not reorder live content under the pointer
- Do not exceed the sticky chrome budget
- Do not place destructive beside primary, or default-focus it
- Do not reduce contrast for density
- Do not ship compact density to touch without expanded hit areas
- Do not squeeze wide tables into narrow viewports
- Do not convey status by colour alone
- Do not animate anything seen hundreds of times a day

## 19. Implementation notes

- **Token delivery:** [[SET]]
- **Table library:** [[SET: and whether it supports pinning, virtualisation, keyboard nav]]
- **URL state management:** [[SET]]
- **Chart library:** [[SET: and how the data alternative is generated]]
- **Density switching:** [[SET: mechanism and persistence]]
- **Existing components to reuse:** [[SET]]

## 20. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/dashboard-admin.md` (and
`categories/data-analytics.md` if charts are central), then this file. This file wins.

**Before generating:** inspect the app shell, existing table/filter/empty-state components,
whether a density system exists, how URL state is managed, and the existing destructive-
confirmation pattern. Report findings. **Do not build a second table component.**

**While generating:** semantic tokens only. All eight interaction states. All ten data states
from §9. Sticky budget respected. Keyboard table navigation implemented.

**Then report:** assumptions, deviations, invented values, unresolved decisions, reused vs.
created components, and what you verified — specifically keyboard table navigation, refresh
behaviour, and the sticky chrome measurement.

**Review checklist:** `design-intelligence/checklists/dashboard-review.md`
