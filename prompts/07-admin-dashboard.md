# Prompt 07 — Build a dashboard or administration surface

---

```
Build <SURFACE> — a dashboard/admin view for <PRODUCT>.

CONTEXT
- Who uses it: <role, expertise>
- How often: <daily | all day>  ← this drives density more than anything else
- Primary task: <monitor | operate | administer | resolve exceptions>
- Data: <entities, typical row counts, which columns matter>
- Actions available: <including destructive ones>
- Real-time updates: <none | occasional | continuous>
- Device: <desktop | desktop + occasional mobile>

STEP 1 — INSPECT. Report before writing code:
- The project DESIGN.md
- The existing app shell: top bar, side nav, page header, toolbar — heights and behaviour
- Existing table, filter, and empty-state components
- Whether a density mode system exists
- How URL state is managed (filters, sort, pagination)
- Existing destructive-confirmation pattern
Report what exists. Do not build a second table component.

STEP 2 — BUILD

Remember the governing constraint: someone uses this eight hours a day. Marketing values are
actively wrong here. Decorative whitespace is a performance defect; so is illegible density.

Density (default to standard, let users choose and persist it):
- Compact:     32px rows, 32px controls, 13px body, 12px card padding, 16px page padding
- Standard:    40px rows, 36px controls, 14px body, 16px card padding, 24px page padding
- Comfortable: 48px rows, 40px controls, 16px body, 24px card padding, 32px page padding
Every value moves together. Compact is POINTER-ONLY — force comfortable on touch.
Density scales dimensions, never contrast.

Shell:
- Total sticky chrome <=20% of viewport height. Top bar + page header + toolbar + sticky table
  header adds up fast; on a laptop it can leave 300px of content.
- Side nav 240px, collapsible to a 56px rail with persisted state.

Tables — the primary component. Required:
- Sticky header, sortable with aria-sort and visible direction
- Hairline row borders. NO zebra striping — it consumes the channel hover and selection need.
- Full-row hover shift
- Right-aligned numerics with TABULAR FIGURES
- Identifying column PINNED when horizontal scroll is possible
- Em-dash for empty cells, never blank
- Truncate long text with the full value on hover/focus
- Status as colour + icon + text
- Selection: checkbox column, count shown, "select all N" as an explicit separate option
- Bulk action bar appears WITHOUT shifting content
- Pagination with totals ("1-50 of 1,340"). NOT infinite scroll.
- Filter/sort/page state in the URL so views are shareable and survive reload
- Result count always: "24 of 1,340"
- Active filters as removable chips with a clear-all control
- Keyboard navigation: arrow keys between cells, Home/End, visible focus, no traps

States — implement all:
- First-run empty: explain what appears here + a primary action
- Filtered-empty: DISTINCT message, offer to clear filters
- Initial loading: skeleton matching final layout
- Refresh: KEEP existing data visible with a subtle indicator. Never blank the table.
- Partial data: show what loaded, mark what failed, offer retry for the failed part
- Error: what happened, what to do, retry
- Permission denied: what is needed, who grants it
- Stale data: timestamp + refresh control

Real-time (if applicable):
- NEVER reorder rows under the cursor. New items get a "3 new — show" affordance.
- Brief 1-2s highlight on change, then settle
- Never steal focus
- Show connection state; offer a pause control if the rate makes reading hard

Destructive actions:
- Reversible: direct + toast with undo
- Hard to reverse: modal naming the target
- Irreversible: modal + typed confirmation of the resource name
- Bulk: modal + count + sample of affected items
- Danger colour; NOT adjacent to the primary action; never the default focus target
- Confirmation button names the action: "Delete project", not "Confirm"

Metrics (if present):
- Value with tabular figures, label, TIMEFRAME (a number without a timeframe is not
  information), and comparison with basis: "↑ 12% vs. previous 24h"
- Show the threshold where one exists
- "No data" is not zero

Command palette: Cmd/Ctrl+K, 560-640px, grouped results. Also provide a discoverable path to
everything in it — the palette must not be the only route.

Responsive:
- <768px: nav drawer, tables transform to cards OR scroll with pinned column, filters in a
  drawer, bulk actions deferred, comfortable density forced
- State in the interface when a capability requires a larger screen

CONSTRAINTS
- No marketing spacing, no display type above 28px, no decorative elements
- No animation on anything users see hundreds of times a day
- Do not reduce contrast to achieve density
- Reuse existing components

REPORT
DENSITY          - which mode is default and why
REUSED / CREATED
STATES           - confirm each of the eight data states is implemented
ASSUMPTIONS / DEVIATIONS / INVENTED VALUES / UNRESOLVED
VERIFIED         - keyboard table navigation, sticky chrome budget, refresh behaviour
MOBILE LIMITS    - what is unavailable and how that is communicated
```
