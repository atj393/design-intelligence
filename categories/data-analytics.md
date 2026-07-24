# Data-Intensive Analytics Products

Interfaces for exploring data rather than monitoring it: BI tools, analytics workspaces,
observability platforms, query interfaces, reporting builders, multi-series comparison.

> **Evidence strength: weak / predominantly synthesized.**
> The corpus documents **no analytics interface**. `design-md/posthog/DESIGN.md` is an
> analytics company whose own gaps section excludes its product UI. Six sources publish a
> `stat-display` typography token, which tells us large numerics are a recognised type role and
> nothing more. Categorical palettes, chart mechanics, and query interfaces are general
> data-visualisation reasoning.

---

## 1. Analytics versus dashboard

Related but distinct, and the distinction determines the whole design.

| | Dashboard | Analytics |
|---|---|---|
| Question | Known, fixed | Unknown, emergent |
| User action | Reads prepared views | Builds their own views |
| Primary component | Metric tiles, status | Query builder, chart canvas |
| Iteration | Rare | **Constant** |
| Success | Notice a problem fast | Reach a defensible conclusion |
| Interaction depth | Shallow | Deep — drill, pivot, segment, compare |

If users mostly read views someone else made, use [dashboard-admin.md](dashboard-admin.md). If
they mostly build their own, this guide applies. Most products need both, sharing one foundation.

## 2. The governing constraint

**Iteration speed is the product.** An analyst may change a filter, dimension, or timeframe
dozens of times per session. Every interaction cost is multiplied by that.

Consequences:

- Query changes must be cheap: no full page reload, no losing scroll position, no re-entering
  parameters.
- Results should update in place, keeping the previous result visible while loading.
- Every state must be in the URL so a view can be shared, bookmarked, and returned to.
- Undo for query changes — an analyst who has just destroyed a good configuration by one click
  needs it back.
- Never animate anything the user triggers dozens of times.

## 3. Layout

```
┌──────────────────────────────────────────────────┐
│ top bar 48px — workspace, saved views, share     │
├─────────┬─────────────────────────────┬──────────┤
│ nav     │  query controls (48-96px)   │ inspector│
│ rail    ├─────────────────────────────┤ 320px    │
│ 56px    │  chart canvas               │ (toggle) │
│         ├─────────────────────────────┤          │
│         │  data table                 │          │
└─────────┴─────────────────────────────┴──────────┘
```

| Element | Value |
|---|---|
| Top bar | 48px — thinner than a dashboard; every pixel is canvas |
| Nav | Rail 56px by default; expandable |
| Query controls | 48–96px, sticky |
| Chart canvas | Flexible, minimum 320px height |
| Data table | Resizable, collapsible |
| Inspector | 320–400px, toggleable |
| Density | **Compact** |
| Section gap | 16–24px |
| Body | 13–14px |
| Max display | 20–24px (numeric callouts excepted) |

**Chrome is minimised aggressively in this category.** The canvas is the product. A 64px header
plus a 96px filter bar plus a 48px toolbar leaves a laptop user with very little room to see
data.

## 4. Chart design

### Chart type selection

| Data relationship | Chart |
|---|---|
| Change over time | Line (multi-series), area (cumulative) |
| Comparison across categories | Horizontal bar (long labels), vertical bar (few, short) |
| Part of a whole | Stacked bar — **avoid pie beyond 3 slices** |
| Distribution | Histogram, box plot |
| Correlation | Scatter |
| Density over 2 dimensions | Heatmap |
| Single value vs. target | Bullet or gauge with the threshold marked |
| Flow between states | Sankey, funnel |
| Hierarchy + magnitude | Treemap |

**Pie charts fail beyond three slices** — humans compare angles poorly. Use a bar chart.

**Horizontal bars for long category labels.** Rotated 45° labels are hard to read and are a
symptom of the wrong chart orientation.

### Chart requirements

| Element | Requirement |
|---|---|
| Axis labels | Always, with units |
| Y-axis zero | Start at zero for bars — truncating exaggerates differences misleadingly. Lines may truncate if the range is labelled clearly |
| Gridlines | Subtle, horizontal only, `border-subtle` |
| Legend | When >1 series. Position where it does not shrink the plot area |
| Direct labelling | Better than a legend when only 2–4 series — label the line ends |
| Tooltip | On hover **and** focus. Show all series at that x-position, not just the nearest point |
| Empty state | "No data for this period" inside the chart frame, not a blank box |
| Loading | Skeleton at final dimensions |
| Partial data | Mark incomplete periods explicitly — a partial final day looks like a crash |
| Precision | Round in display; keep full precision on hover |
| Annotations | Support marking deploys, incidents, campaign starts |

**Marking incomplete periods is the most common analytics bug.** Today's partial data plotted
next to complete days looks like a catastrophic drop and generates false alarms.

### Categorical palette

Required for multi-series work — the one place a categorical palette is legitimate.

| Requirement | Detail |
|---|---|
| Length | 6–8 distinguishable hues; beyond that, grouping beats colouring |
| Distinguishability | In greyscale, and under the common colour-vision deficiencies |
| Consistency | The same series is the same colour across every chart in the product |
| Semantic collision | Must not collide with success/warning/danger meanings |
| Order | Assign deterministically, not by render order — a series must not change colour when another is filtered out |
| Sequential | Separate single-hue ramp for magnitude |
| Diverging | Separate two-hue ramp with a meaningful midpoint |

**Colour is never the only channel.** Add markers, dash patterns, or direct labels. A
seven-series line chart distinguished only by hue is unreadable to a colour-blind user and
difficult for everyone in greyscale print.

**Deterministic colour assignment matters more than it sounds.** If filtering out series 2 makes
series 3 change colour, the analyst loses their mental map on every interaction.

## 5. Metric display

| Element | Requirement |
|---|---|
| Value | Large, **tabular figures** |
| Unit | Adjacent, smaller |
| Timeframe | Always: "last 24h", "Mar 1–31" |
| Comparison | Direction + magnitude + basis: "↑ 12% vs. previous 24h" |
| Direction colour | Plus arrow and sign — never colour alone. And note: "up" is not always good |
| Threshold | Show it when one exists |
| Sparkline | Optional trend context |
| No data | "No data", not `0` — they mean different things |

**`0` and "no data" are different facts.** Rendering missing data as zero is a correctness
error, and in analytics it produces wrong conclusions.

**"Up" is not universally good.** Error rate up is bad. Do not hard-code green-for-increase;
make direction semantics per-metric.

## 6. Data tables in analytics

Beyond the [dashboard table guidance](dashboard-admin.md#4-tables):

| Requirement | Detail |
|---|---|
| Row height | 32px (compact) |
| Column management | Show/hide, reorder, resize; persist per user |
| Aggregation row | Totals or averages, visually distinct and pinned |
| Grouping | Collapsible groups with subtotals |
| Pivot | Row/column dimension swap where the model supports it |
| Cell formatting | Numeric, percentage, currency, duration — per column type |
| Conditional formatting | Data bars or colour scales, with the scale legend shown |
| Drill-down | Click a cell to see contributing rows |
| Export | CSV and clipboard; state included columns and applied filters |
| Virtualisation | Required beyond ~500 rows |
| Sort stability | Secondary sort key so equal values do not reorder randomly |

## 7. Query and filter interfaces

| Pattern | Use when |
|---|---|
| Faceted filters | Fixed, known dimensions |
| Visual query builder | Non-technical users; moderate complexity |
| Text query language | Expert users; high complexity |
| Both, with sync | The strongest option — builder and text view of the same query |
| Saved segments | Reusable filter sets |

Requirements:

- Show the current query in a human-readable form, even when built visually.
- Validate before running; show errors at the offending clause.
- Show the row count the query will return before or immediately after running.
- Long-running queries: progress, elapsed time, and a **cancel** control.
- Query history, so a user can return to what they ran twenty minutes ago.
- Never lose a query on navigation or error.

**A cancel control on long queries is essential.** An analyst who has just realised the query is
wrong should not have to wait ninety seconds or reload the page.

## 8. Time range control

The most-used control in analytics. Design it carefully.

| Element | Requirement |
|---|---|
| Presets | Last hour / 24h / 7d / 30d / 90d / this month / last month / YTD |
| Custom range | Calendar with direct text entry as well |
| Granularity | Auto-select, and allow override (hour / day / week / month) |
| Comparison | "vs. previous period" and "vs. same period last year" |
| Timezone | **Always stated.** Ambiguous timezone invalidates analysis |
| Relative vs. absolute | Distinguish "last 7 days" (moves) from a fixed range (does not) — critical for saved views |
| Persistence | Maintained across navigation within the workspace |

**Timezone must be explicit.** "Yesterday" differs by up to a day across timezones, and an
analyst comparing two views on different timezone assumptions reaches wrong conclusions.

## 9. Saved views and sharing

| Element | Requirement |
|---|---|
| URL state | **Complete** — every filter, dimension, range, and chart setting |
| Save | Named, with description, personal or shared |
| Default view | Per user, per workspace |
| Share | Link that reproduces exactly what the sender saw |
| Relative range warning | A saved "last 7 days" shows different data tomorrow — say so |
| Permissions | Who can see a shared view, and whose data access applies when they open it |
| Versioning | Warn when a shared view's underlying schema changed |

**Data-access semantics on shared views are a real hazard.** If a shared view runs with the
*viewer's* permissions, results differ per person and that must be visible. If it runs with the
*author's*, that is a data-exposure decision needing explicit design.

## 10. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav | Drawer | Rail | Rail or full |
| Query controls | Drawer, applied explicitly | Collapsed | Inline |
| Charts | One at a time, simplified, fewer series | 1–2 up | Grid |
| Data table | Scroll + pinned first column | Scroll | Full |
| Inspector | Full-screen route | Overlay | Docked |
| Time range | Presets only | Full | Full |
| Query builder | **Often unavailable** — state it | Simplified | Full |
| Export | Available | Available | Available |

**Full parity is not achievable and should not be claimed.** Multi-series comparison across
eight dimensions on a 375px screen is not a solvable layout problem. Deliver read-and-share on
mobile, and **state in the interface** that building queries requires a larger screen.

Prioritise for mobile: viewing a saved view, reading a metric, sharing a link, receiving an
alert. Not: building a query, pivoting a table, comparing eight series.

## 11. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor). Charts are the
hard part.

| Requirement | Implementation |
|---|---|
| Chart alternative | Every chart has an accessible data table or a text summary of the trend. This is the single most important item |
| Series distinguishable without colour | Markers, dash patterns, direct labels |
| Tooltips on focus | Keyboard users must reach the same information hover provides |
| Chart keyboard navigation | Arrow keys between data points, with announced values |
| Axis labels | Real text, programmatically associated |
| Table keyboard navigation | Arrow keys, `Home`/`End`, visible focus |
| Aggregation rows | Marked as such, not just visually distinct |
| Compact density on touch | Expand hit areas to 44px even where rows are 32px |
| Live-updating data | `aria-live="polite"`; never `assertive` |
| Conditional formatting | Include the value as text; colour is supplementary |
| 200% zoom | Usable; internal scroll acceptable, page-level horizontal scroll not |

**"The chart is inaccessible so we'll skip it" is not acceptable.** A data table alternative is
straightforward, and it is also useful to sighted users who want exact values.

## 12. Do

- Minimise chrome; the canvas is the product
- Keep the previous result visible while the next loads
- Put complete state in the URL
- Assign series colours deterministically
- Mark incomplete periods explicitly
- Distinguish "no data" from zero
- Start bar charts at zero
- Use horizontal bars for long labels
- Show timezone on every time range
- Distinguish relative from absolute ranges in saved views
- Provide cancel on long-running queries
- Keep query history
- Give every chart an accessible data alternative
- Provide undo for query changes
- Add a secondary sort key for stability

## 13. Do not

- Do not use pie charts beyond three slices
- Do not truncate a bar chart's y-axis
- Do not distinguish series by colour alone
- Do not let series colours change when another series is filtered
- Do not render missing data as zero
- Do not plot partial periods without marking them
- Do not hard-code green-for-increase
- Do not animate interactions the user repeats dozens of times
- Do not reload the page on a filter change
- Do not lose a query on navigation or error
- Do not omit timezone
- Do not claim mobile parity for query building
- Do not ship a chart with no accessible alternative
- Do not reduce contrast to achieve density

## 14. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/posthog/DESIGN.md` § *Overview*, § *Known Gaps* | An analytics company documented at marketing level only — its gaps section explicitly excludes the product interface. Its useful contribution is a counter-example on tone: a warm, illustrated identity in a genre that defaults to somber dark |
| `design-md/stripe/DESIGN.md` § *Typography* | A dedicated tabular-figure token. Foundational for any numeric table or metric display |
| `design-md/binance/DESIGN.md` § *Colors*, § *Typography* | Directional semantic colour for value change, plus dedicated `number-display` type steps at multiple sizes — evidence that numeric display is its own typographic role |
| `design-md/miro/`, `design-md/mistral.ai/`, `design-md/clickhouse/` § *Typography* | A `stat-display` token at 56–64px in six sources — large numerics as an established type role, distinct from display headings |
| `design-md/linear.app/DESIGN.md` § *Elevation & Depth* | Four-step surface ladder with hairlines and no shadow — the most transferable model for a dense multi-panel workspace |
| `design-md/nvidia/DESIGN.md` § *Layout* | Dense multi-column technical content separated by hairline rules; 2px radius supporting density |
| `design-md/hashicorp/DESIGN.md` § *Colors* | Accent colours mapped to structural identity rather than decoration — the discipline a categorical series palette needs |

## 15. Common mistakes

| Mistake | Consequence | Correction |
|---|---|---|
| Partial periods unmarked | False alarms about drops | Mark incomplete explicitly |
| Missing data as zero | Wrong conclusions | Distinguish clearly |
| Truncated bar y-axis | Exaggerated differences | Start at zero |
| Non-deterministic series colour | Analyst loses mental map on every filter | Deterministic assignment |
| Colour-only series distinction | Unreadable for many users | Markers and direct labels |
| Missing timezone | Analyses not comparable | State it always |
| Relative range in a saved view, unmarked | Shared view shows different data | Warn explicitly |
| No cancel on long queries | Users reload and lose state | Cancel control |
| State not in URL | Views unshareable | Complete URL state |
| Charts with no data alternative | Inaccessible core content | Data table |
| Heavy chrome | Little room for data | Minimise; 48px top bar |
| Animated chart transitions | A tax paid dozens of times per session | Instant updates |

## 16. Template

Use [templates/DESIGN.dashboard-admin.md](../templates/DESIGN.dashboard-admin.md) as the base
and add this guide's chart, palette, query, and time-range sections. The shell, table, and
density models are shared; analytics adds the visualisation layer.
