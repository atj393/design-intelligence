# Dashboard and Administration Review Checklist

Run [foundation-review.md](foundation-review.md) first.

Reference: [../categories/dashboard-admin.md](../categories/dashboard-admin.md) ·
[../categories/data-analytics.md](../categories/data-analytics.md) —
**both predominantly synthesized; validate with real operators.**

---

## 1. Density

- [ ] Compact, standard, and comfortable modes are defined
- [ ] The default is appropriate to the actual usage frequency
- [ ] Users can switch, and the choice **persists**
- [ ] Every value moves together — no compact table inside comfortable padding
- [ ] Body text never below 13px
- [ ] Density scales **dimensions only**, never contrast
- [ ] Compact is not shipped to touch without expanded hit areas
- [ ] Comfortable is forced on touch devices

## 2. Shell

- [ ] **Total sticky chrome ≤20% of viewport height** — measure it at 768px height
- [ ] Side nav collapses to a rail; state persists
- [ ] Current location identifiable even when collapsed
- [ ] No marketing-scale display type (ceiling 20–28px)
- [ ] No decorative elements in the working surface

## 3. Tables

- [ ] Sticky header
- [ ] Sortable headers are buttons with `aria-sort` and visible direction
- [ ] **No zebra striping**
- [ ] Full-row hover
- [ ] Selection state distinct from hover
- [ ] Identifying column **pinned** when horizontal scroll is possible
- [ ] Numerics right-aligned with **tabular figures**
- [ ] Empty cells show an em-dash, never blank
- [ ] Long text truncated with the full value on hover **and focus**
- [ ] Status shown as colour + icon + text
- [ ] Secondary sort key so equal values do not reorder randomly
- [ ] Virtualised above a sensible row count
- [ ] **Keyboard navigation:** arrows between cells, `Home`/`End`, visible focus, no traps

## 4. Filtering, sorting, views

- [ ] Result count always shown: "24 of 1,340"
- [ ] Active filters shown as removable chips
- [ ] Clear-all available whenever filters are active
- [ ] **Filter, sort, and page state in the URL** — shareable and reload-safe
- [ ] Filters preserved across navigation within the same context
- [ ] Zero-result state distinct from "no data yet", offering to relax filters
- [ ] Saved views: name, save, set default
- [ ] Search states which fields it covers

## 5. Pagination

- [ ] Pagination, not infinite scroll
- [ ] Total count and current range shown
- [ ] Page state survives reload

## 6. Bulk actions

- [ ] Bar appears on selection **without shifting content**
- [ ] Count shown: "12 selected"
- [ ] "Select all N" is a distinct, explicit option
- [ ] Confirmation names count and action
- [ ] **Partial failures reported per item**, not "some items failed"
- [ ] Undo for reversible operations
- [ ] Selection state announced to assistive tech

## 7. Inline editing

- [ ] Editability is discoverable
- [ ] `Enter` commits, `Esc` cancels, `Tab` moves to the next editable cell
- [ ] Saving state shown in place without shifting the row
- [ ] Validation error shown at the cell
- [ ] **On failure, the edited value is kept** — never reverted

## 8. States

- [ ] First-run empty: explains and offers a primary action
- [ ] Filtered-empty: **distinct** message, offers to clear
- [ ] Initial loading: skeleton matching final layout
- [ ] **Refresh keeps existing data visible** — the table is never blanked
- [ ] Partial data: shows what loaded, marks failures, offers targeted retry
- [ ] Error: cause, action, retry
- [ ] Permission denied: what is needed and who grants it
- [ ] Stale data: timestamp + refresh
- [ ] Offline: banner, network actions disabled, drafts preserved
- [ ] Too many results: suggests narrowing rather than silently truncating

## 9. Real-time

- [ ] **Rows never reorder under the cursor** — "N new — show" affordance instead
- [ ] Changes highlighted briefly (1–2s), then settle
- [ ] Focus never stolen
- [ ] Connection state visible when live updates are expected
- [ ] Pause control where the update rate impedes reading
- [ ] Announced via `aria-live="polite"`, never `assertive`

## 10. Destructive actions

- [ ] Severity matched to pattern (toast+undo / modal / typed confirmation)
- [ ] Danger colour used
- [ ] **Not adjacent** to the primary action
- [ ] **Never the default focus** in a dialog
- [ ] Confirmation button names the action, not "Confirm"
- [ ] Modal states what will and will not be affected
- [ ] Bulk destructive shows count and a sample
- [ ] Archive offered in place of delete where the domain allows

## 11. Metrics and charts

- [ ] Values use tabular figures
- [ ] **Every number has a timeframe**
- [ ] Comparisons state their basis: "↑ 12% vs. previous 24h"
- [ ] Direction semantics are per-metric — "up" is not hard-coded as good
- [ ] Thresholds shown where they exist
- [ ] "No data" distinguished from `0`
- [ ] Charts: axis labels with units; legend when >1 series
- [ ] **Incomplete periods marked** — a partial final day must not read as a crash
- [ ] Bar charts start at zero
- [ ] Series colours assigned **deterministically** per key
- [ ] Series distinguishable in greyscale (markers, dashes, direct labels)
- [ ] **Every chart has a data table or text alternative**
- [ ] Chart loading uses a skeleton at final dimensions

## 12. Forms and configuration

- [ ] Long forms sectioned with sticky section navigation
- [ ] Unsaved-changes state visible; warns before navigating away
- [ ] Save mechanism unambiguous (explicit save vs. autosave)
- [ ] Effective value shown alongside inherited/default values
- [ ] Reset-to-default available per field
- [ ] Dangerous settings visually separated and individually confirmed

## 13. Command palette

- [ ] `Cmd/Ctrl+K` opens it
- [ ] Results grouped by labelled category
- [ ] Arrow keys move, `Enter` runs, `Esc` closes
- [ ] Empty state teaches available categories
- [ ] **Everything in it also has a discoverable path** — the palette is never the only route

## 14. Responsive

- [ ] Nav becomes a drawer below 768px
- [ ] Tables transform to cards **or** scroll with a pinned column — never squeezed
- [ ] Filters move to a drawer with explicit apply
- [ ] Detail panel becomes a full-screen route
- [ ] Metric tiles reflow sensibly
- [ ] Comfortable density forced on touch
- [ ] **Capabilities unavailable on mobile are stated in the interface**

## 15. Accessibility

- [ ] Table keyboard navigation works end to end
- [ ] Selection announced: "12 of 340 selected"
- [ ] Status available as text — non-negotiable in dense tables
- [ ] Charts have accessible alternatives
- [ ] Live updates `polite`, never `assertive`
- [ ] Compact density still meets 44px hit areas on touch
- [ ] Usable at 200% zoom (internal scroll acceptable, page-level not)
- [ ] Toolbars are `role="toolbar"` with arrow-key navigation
- [ ] Disabled controls explain why

## 16. Frequency test

The category's governing question. Ask it of every screen:

- [ ] If someone opens this forty times a day, does the spacing cost them scroll?
- [ ] Is there any animation they will see hundreds of times?
- [ ] Can they reach their most common action without a mouse?
- [ ] Does refresh preserve their place, their filters, and their scroll position?
