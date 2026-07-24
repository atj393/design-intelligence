# Dashboards and Administration Systems

Authenticated, information-dense interfaces used frequently by trained users: operational
consoles, admin panels, work queues, management systems, monitoring surfaces.

> **Evidence strength: weak / predominantly synthesized.**
> The corpus documents **zero dashboards**. `design-md/posthog/DESIGN.md` belongs to an
> analytics company and its own gaps section excludes the product interface.
> `design-md/spotify/DESIGN.md` is the corpus's only real application UI and contributes its
> surface-ladder model. The `ex-data-table-cell` and `ex-app-shell-row` entries in 13 files
> are machine-generated from marketing primitives, not observed interfaces
> ([discrepancy D7](../REPOSITORY-DISCREPANCIES.md)) — they are not treated as evidence here.
> This guide is general interface reasoning. Validate early with real operators.

---

## 1. The governing constraint

**Someone will use this eight hours a day, every working day.**

Every design decision must be evaluated against that, and it inverts marketing instincts
completely:

| Marketing value | Dashboard reality |
|---|---|
| Generous whitespace reads as confident | Whitespace is scroll paid on every visit |
| Large type reads as premium | Large type means less data per screen |
| Beautiful empty states | Users see them once |
| Animated transitions delight | Animations become a tax at the 200th repetition |
| Full-bleed imagery impresses | Imagery is space not spent on data |

**Decorative whitespace in an operational tool is a performance defect.** So is illegible
density. The goal is *efficient legibility*, and the corpus's marketing values — 96px section
rhythm, 64px display type, 32px card padding — are actively wrong here.

## 2. Density modes

Define all three; ship a sensible default and let users choose.

| Property | Compact | Standard | Comfortable |
|---|---|---|---|
| Table row height | 32px | 40px | 48px |
| Control height | 32px | 36px | 40px |
| Body size | 13px | 14px | 16px |
| Card padding | 12px | 16px | 24px |
| Page padding | 16px | 24px | 32px |
| Section gap | 16px | 24px | 32px |
| Grid gap | 12px | 16px | 24px |
| Table cell padding | 6px 10px | 8px 12px | 12px 16px |
| Icon size | 16px | 16px | 20px |
| Max display size | 20px | 24px | 28px |

**When to use which:**

| Use | Mode |
|---|---|
| Expert users, pointer devices, monitoring many rows | Compact |
| Mixed expertise, mostly desktop, general operations | **Standard (default)** |
| Occasional users, touch devices, accessibility needs | Comfortable |

**Constraints:**

- **Compact is a pointer-only mode.** On touch, 44px targets override it. Never allow compact
  on a touch device without expanding hit areas beyond the visual row height.
- Never go below 13px body text; below that, comprehension degrades measurably.
- Density scales *dimensions*, never contrast or colour. A compact table with reduced text
  contrast is not denser, it is worse.
- Apply density per surface, consistently. A compact table inside comfortable page padding
  looks like a mistake.
- Persist the user's density choice.

## 3. Application shell

```
┌───────────────────────────────────────────────┐
│ top bar 56px — context, search, account       │
├──────────┬────────────────────────────────────┤
│ side nav │  content region                    │
│ 240px    │  ┌──────────────────────────────┐  │
│ or rail  │  │ page header: title, actions  │  │
│ 56px     │  ├──────────────────────────────┤  │
│          │  │ filters / toolbar            │  │
│          │  ├──────────────────────────────┤  │
│          │  │ primary content (table/grid) │  │
│          │  └──────────────────────────────┘  │
└──────────┴────────────────────────────────────┘
```

| Element | Value |
|---|---|
| Top bar | 56px (64px comfortable) |
| Side nav | 240px expanded, 56px rail |
| Page header | 56–64px, sticky |
| Toolbar | 48px, sticky below the header |
| Content padding | Per density |
| Detail panel | 320–400px right, or a route |

**Sticky discipline:** total sticky chrome must not exceed ~20% of viewport height. Top bar +
page header + toolbar already reaches ~160px; adding a sticky filter row and a sticky table
header can leave a laptop user with 300px of actual content.

**Collapsed rail:** icons only, with tooltips. Persist the collapsed state. Never collapse to
a state where the current location is unidentifiable.

## 4. Tables

The primary component of the category. Specify it exhaustively — most dashboard quality lives
here.

### Structure

| Property | Requirement |
|---|---|
| Header | Sticky, `surface-sunken`, `overline` or `label` type, sort affordance |
| Rows | `border-subtle` bottom. **Avoid zebra striping** — it conflicts with selection and hover |
| Hover | Full-row surface shift; makes the row scannable across wide tables |
| Selection | Checkbox column, 40px wide; selected rows get a distinct surface |
| Focus | Visible cell or row focus for keyboard navigation |
| First column | Identifying value; **pinned** when horizontal scroll is possible |
| Last column | Row actions, right-aligned |
| Numeric columns | Right-aligned, **tabular figures** |
| Dates | Consistent format; absolute in records |
| Status | Badge with colour + icon + text |
| Empty cell | An em-dash `—`, never blank. Blank reads as a rendering fault |
| Long text | Truncate with ellipsis + full value on hover/focus |
| Row density | Per density mode |

**Three rules that matter more than they look:**

1. **Right-align numbers and use tabular figures.** Proportional digits make columns jitter and
   make comparison genuinely harder. This is the cheapest real improvement available to most
   dashboards.
2. **Pin the identifying column when scrolling horizontally.** Scrolling a wide table without
   knowing which row you are on is useless.
3. **Avoid zebra striping** — stripes consume the visual channel that hover and selection need,
   and they add visual noise at density. Use hairline row borders instead.
   **One genuine exception**, added after adversarial review (see
   [research/WEAK-GUIDE-REVIEW.md](../research/WEAK-GUIDE-REVIEW.md) A-03): in **very wide
   tables (~15+ columns) that scroll horizontally**, hover alone is not enough to track a row
   across the viewport, and striping measurably helps. If you stripe, make the stripe far
   subtler than your hover state (roughly a 2% surface shift against hover's 4%) so hover and
   selection still dominate. An earlier draft stated this as an absolute, which was wrong.

### Sorting, filtering, views

| Feature | Requirement |
|---|---|
| Sort | Click header; show direction; support multi-column where useful |
| Filter | Show active filters as removable chips above the table |
| Filter result count | "24 of 1,340" — always |
| Clear all | One control, always available when filters are active |
| Saved views | Name, save, set default, share where appropriate |
| URL state | Filters, sort, and page in the URL so views are shareable and survive reload |
| Search | Scoped to the table; state which fields it searches |

**Put filter state in the URL.** A filtered view a user cannot bookmark or send to a colleague
is half a feature, and reload-loses-everything is a daily irritation.

### Pagination versus infinite scroll

| Use | When |
|---|---|
| Pagination | Known totals, need for position, printing, deep navigation — **default for tables** |
| Load more | Feeds; unknown totals |
| Virtual scroll | Very large sets where the user scans continuously |
| **Not** infinite scroll | Tables. It breaks position, footers, and "where was I?" |

Show total count and current range: "1–50 of 1,340". Operators need the total to reason about
their work.

### Bulk actions

- Action bar appears on selection **without shifting content**. Reserve the space or overlay.
- Show count: "12 selected", with "select all 1,340" as a distinct, explicit option.
- Confirmation names count and action: "Archive 12 records?".
- Report partial failure per item — never a bare "some items failed".
- Undo for reversible bulk operations.

### Inline editing

- Make editability discoverable — a hover affordance or an explicit edit mode.
- `Enter` commits, `Esc` cancels, `Tab` moves to the next editable cell.
- Show saving state in place; do not shift the row.
- Validate on commit, showing the error at the cell.
- On failure, keep the edited value. Reverting the user's input loses their work.

### Mobile

At <768px, a 10-column table has two honest options:

1. **Transform to cards** — one card per row, 3–4 key fields, tap for detail. Better for
   reading.
2. **Horizontal scroll with a pinned first column** — better for comparison.

Choose based on whether users scan or compare. **Do not squeeze ten columns into 375px.**

## 5. Filters

| Filter type | Component |
|---|---|
| Single choice, ≤5 options | Segmented control |
| Single choice, >5 | Select |
| Multi choice | Checkbox list in a popover, with counts |
| Date range | Presets (today, 7d, 30d, custom) + calendar |
| Numeric range | Two inputs; slider only when the range is intuitive |
| Free text | Debounced search input |
| Boolean | Toggle or checkbox |

- Show active filters as chips with individual remove controls.
- Preserve filters across navigation within the same context.
- Filters that produce zero results need an empty state distinct from "no data yet", offering
  to clear or relax them.

## 6. Metrics and charts

For deep analytical work see [data-analytics.md](data-analytics.md). Dashboard basics:

| Element | Requirement |
|---|---|
| Metric tile | Value (large, tabular), label, timeframe, comparison |
| Comparison | Direction + magnitude + basis: "↑ 12% vs. last week" |
| Chart | Axis labels, units, legend when >1 series |
| Chart height | 200–320px in a dashboard grid |
| No data | Explicit "no data for this period", not an empty chart frame |
| Loading | Skeleton matching final dimensions |
| Precision | Round sensibly. "1,284" not "1284.0000" |

**A number without a timeframe is not information.** "1,284 requests" means nothing; "1,284
requests (last 24h)" does.

**A tile with a threshold should show the threshold.** If 95% is the SLA, the tile should make
clear whether 94% is a problem.

## 7. Forms

Follow the [foundation form rules](../COMMON-FOUNDATION.md#16-forms). Additions for admin
contexts:

- Long configuration forms need sectioning with sticky section navigation.
- Show unsaved-changes state; warn before navigating away.
- Support both explicit save and per-field autosave — but never leave which one is active
  ambiguous.
- Dangerous settings need visual separation and confirmation.
- Show current effective value alongside inherited or default values.
- Provide reset-to-default per field where defaults exist.

## 8. Destructive actions

| Consequence | Treatment |
|---|---|
| Reversible | Direct action + toast with undo |
| Hard to reverse | Confirmation modal naming the target |
| Irreversible | Modal + typed confirmation of the resource name |
| Affects other users | Modal + explicit statement of the impact and scope |
| Bulk destructive | Modal + count + list or sample of affected items |

Requirements:

- Destructive buttons use `status-danger`, and are **not** placed adjacent to the primary
  action.
- The confirmation button names the action: "Delete project", not "Confirm".
- The modal states what will and will not be deleted.
- Never make destructive the default focus target in a dialog.
- Prefer archive over delete where the domain allows it.

## 9. Command palette

Strongly recommended for expert users, at low cost — invisible to those who never find it.

| Property | Value |
|---|---|
| Trigger | `Cmd/Ctrl+K` |
| Width | 560–640px |
| Position | Centred, ~20vh from the top |
| Content | Navigation, actions, recent items, search results |
| Grouping | Labelled sections |
| Keyboard | Arrows to move, `Enter` to run, `Esc` to close |
| Empty state | Show available categories, teaching the vocabulary |

Also expose a discoverable path to everything in the palette. A command palette must not be
the *only* route to a feature.

## 10. States

Every one of these will occur. Specify them all.

| State | Requirement |
|---|---|
| First-run empty | Explain what appears here + primary action to create the first item |
| Filtered-empty | Distinct from first-run; offer to clear filters |
| Loading (initial) | Skeleton matching final layout |
| Loading (refresh) | Subtle indicator; keep showing existing data |
| Partial data | Show what loaded; mark what failed; offer retry for the failed part |
| Error | What happened, what to do, retry |
| Permission denied | What is needed, who can grant it |
| Stale data | Timestamp + refresh, when data can age |
| Offline | Banner; disable actions that need the network; preserve drafts |
| Too many results | Suggest narrowing rather than truncating silently |

**Refresh must not clear the screen.** Replacing a populated table with a skeleton on every
poll makes a dashboard unusable. Keep the data; indicate refreshing.

## 11. Real-time updates

| Requirement | Detail |
|---|---|
| Never reorder under the cursor | New items get a "3 new — show" affordance instead of inserting |
| Highlight changes briefly | 1–2s subtle tint, then settle |
| Do not steal focus | Never |
| Show connection state | When live updates are expected and stop, say so |
| Pause control | Where the update rate makes reading difficult |
| Reduced motion | Announce changes without animating them |

**Content jumping under the pointer causes mis-clicks on destructive actions.** This is the
main reason real-time dashboards get distrusted.

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Side nav | Drawer | Rail | Full 240px |
| Top bar | 56px, condensed | 56px | 56px |
| Tables | Transform to cards | Scroll + pinned column | Full |
| Filters | Drawer | Drawer or popover | Inline |
| Bulk actions | Deferred | Available | Available |
| Detail panel | Full-screen route | Overlay | Docked 320–400px |
| Metric tiles | 1-up | 2-up | 3–4-up |
| Charts | Simplified, fewer series | Full | Full |
| Density | Comfortable (forced) | Standard | User choice |

Force comfortable density on touch. Compact on a phone is unusable and inaccessible.

Some capabilities may be genuinely unavailable on mobile. **Say so** — a message explaining
that bulk reassignment requires a larger screen beats a hidden control.

## 13. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- **Table keyboard navigation:** arrow keys between cells, `Home`/`End`, visible focus, no
  traps. This is the biggest accessibility gap in typical dashboards.
- Sortable headers are buttons with `aria-sort`.
- Selection state announced: "Row 3 selected, 12 of 340 selected".
- Status conveyed as text, not colour — non-negotiable in dense tables.
- Charts have an accessible alternative: a data table, or a text summary of the trend.
- Live updates use `aria-live="polite"`; never `assertive` for routine updates.
- Compact density must still meet 44px hit areas on touch, even where the visual row is 32px.
- Dense interfaces must remain usable at 200% zoom — expect horizontal scroll in bounded
  regions, not on the page.
- Toolbars and filter groups are `role="toolbar"` with arrow-key navigation.

## 14. Do

- Define compact, standard, and comfortable modes and let users choose
- Right-align numbers and use tabular figures
- Pin the identifying column on horizontally scrolling tables
- Put filter, sort, and page state in the URL
- Show result counts: "24 of 1,340"
- Keep existing data visible during refresh
- Reserve space for the bulk-action bar
- Confirm destructive actions with the target named and counted
- Report bulk partial failures per item
- Provide undo for anything reversible
- Give charts a timeframe and an accessible alternative
- Use "3 new — show" instead of inserting rows under the cursor
- Provide a command palette *and* a discoverable path

## 15. Do not

- Do not inherit marketing spacing or display sizes
- Do not zebra-stripe tables
- Do not use infinite scroll for tables
- Do not leave empty cells blank — use an em-dash
- Do not clear the table on refresh
- Do not reorder live content under the pointer
- Do not exceed ~20% of viewport height in sticky chrome
- Do not place destructive actions next to primary actions
- Do not make destructive the default focus in a dialog
- Do not reduce contrast to achieve density
- Do not allow compact density on touch without expanded hit areas
- Do not squeeze wide tables into narrow viewports
- Do not convey status by colour alone
- Do not animate anything a user sees hundreds of times a day

## 16. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/spotify/DESIGN.md` § *Color Palette & Roles* | The corpus's only real application UI. A three-step charcoal surface ladder where content supplies colour and the chrome recedes — directly applicable to a dark dashboard shell |
| `design-md/linear.app/DESIGN.md` § *Elevation & Depth* | Four-step surface ladder with hairline borders and no shadow. The most transferable elevation model for a dense application shell |
| `design-md/stripe/DESIGN.md` § *Typography* | A dedicated tabular-figure body token where numerics matter. Small decision, large effect on table readability |
| `design-md/nvidia/DESIGN.md` § *Layout*, § *Shapes* | Dense multi-column technical content separated by hairline rules; 2px radius throughout. Evidence that near-square geometry supports density |
| `design-md/ibm/DESIGN.md` § *Elevation & Depth* | Thin-bordered tiles with no shadow at all — the flat, information-first register |
| `design-md/raycast/DESIGN.md` § *Components* | Command-palette-style rows and hairline borders as a marketing surface. The clearest corpus reference for how a palette-driven expert interface reads |
| `design-md/binance/DESIGN.md` § *Colors* | Directional semantic colour (up/down) in a data context, plus a light theme for transactional density |

**Adopt the density model and the surface-ladder approach. Do not adopt any of these brands'
identities.**

## 17. Common mistakes

| Mistake | Correction |
|---|---|
| Marketing whitespace in an operational tool | 16–24px rhythm, compact/standard density |
| Oversized controls | 32–36px, per density mode |
| Hidden bulk actions | Visible on selection, without layout shift |
| Ambiguous destructive operations | Name the target and count; separate from primary |
| Proportional digits in tables | Tabular figures, right-aligned |
| Table cleared on refresh | Keep data, indicate refreshing |
| Filters lost on reload | URL state |
| Rows inserted under the cursor | "N new — show" affordance |
| Status by colour alone | Colour + icon + text |
| Generic dashboard of six identical cards | Design for the role's actual first question |
| No keyboard table navigation | Arrow keys, visible focus |
| Compact density shipped to touch | Force comfortable, or expand hit areas |

## 18. Review checklist

[checklists/dashboard-review.md](../checklists/dashboard-review.md)

## 19. Template

[templates/DESIGN.dashboard-admin.md](../templates/DESIGN.dashboard-admin.md)
