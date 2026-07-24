# Commercial Multi-Role Platforms

Products serving three or more materially different user types — customers, end users,
operators, company administrators, support staff, field technicians, reviewers, analysts,
platform maintainers — on one shared foundation.

> **Evidence strength: weak / predominantly synthesized.**
> The corpus contains **no documented role-based application**. It offers two structurally
> useful adjacents: `design-md/uber/DESIGN.md` documents multi-*audience* marketing (riders,
> drivers, business) on one visual system, and `design-md/hashicorp/DESIGN.md` documents
> per-product accent colours as identity tokens. The dual-track polarity pattern in
> `design-md/binance/` and `design-md/shopify/` is the empirical basis for the
> shared-foundation model here. Everything about permissions, role switching, audit, and
> approval flows is general interface reasoning.

---

## 1. The central problem

A multi-role platform fails in one of two directions, and both are common:

| Failure | Symptom | Cause |
|---|---|---|
| **Fragmentation** | Four products wearing one logo. Users who move between roles have to relearn | Each role designed independently |
| **Flattening** | Everyone gets the same interface; novices are overwhelmed, experts are slowed | One design forced onto incompatible needs |

The answer is neither. It is **one foundation, several experience layers** — the same model
the corpus's dual-track sources arrived at for marketing versus transactional surfaces, scaled
up to roles.

## 2. What is shared and what varies

The single most important table in this guide. Get this split wrong in either direction and
you produce one of the two failures above.

### Must be identical across every role

| Shared | Why |
|---|---|
| Primitive and semantic tokens | One product, one visual identity |
| Type families and scale ratios | Cross-role recognition |
| Radius character | Inconsistency here is immediately visible |
| Spacing base unit | Alignment across shared components |
| **Status colour meanings** | "Amber = needs attention" must never differ by role. This is the one that causes real errors |
| Core component behaviour | A button, input, and table behave the same everywhere |
| Form conventions | Label position, validation timing, error presentation |
| Feedback patterns | Toast vs. banner vs. modal semantics |
| Destructive-action patterns | Confirmation always looks and works the same |
| Accessibility floor | Non-negotiable, all roles |
| Terminology for shared objects | An "order" is an order in every role |
| Keyboard conventions | Shortcuts do not change meaning by role |

### May vary by role

| Variable | Range |
|---|---|
| Density mode | Customer: default · Operator: compact |
| Navigation pattern | Customer: top bar or shallow side nav · Operator: side nav + command palette |
| Section rhythm and page padding | 48px customer · 32px operator |
| Information density | Summary cards vs. dense tables |
| Available actions | By permission |
| Workflow depth | Guided multi-step vs. single dense form |
| Data visibility | Own records vs. all records |
| Role-specific terminology | Where a role genuinely uses a different word for its own concept |
| Onboarding depth | Heavy for customers, minimal for trained operators |
| Default views and landing page | Per role's primary task |

**Terminology needs care.** Shared objects keep one name. But if operators say "claim" for
what customers see as "request", forcing one word onto both is worse than mapping them —
document the mapping explicitly so nobody invents a third term.

## 3. Role modelling

Before any design work, complete
[templates/ROLE-EXPERIENCE-MAP.md](../templates/ROLE-EXPERIENCE-MAP.md). Per role you need:

| Dimension | Why it matters |
|---|---|
| Primary tasks (top 3) | Determines the default view |
| Expertise | Determines guidance and density |
| Frequency | Determines density and rhythm |
| Session length | Determines fatigue tolerance |
| Device | Determines whether compact is even legal (touch → 44px floor) |
| Data scope | Own / team / organisation / platform |
| Destructive capability | Determines confirmation and audit needs |
| Error consequence | Determines error-prevention investment |
| Can this role see other roles' data? | Privacy and permission design |
| Does one person hold multiple roles? | Determines whether you need role switching at all |

**That last question is decisive.** If people hold exactly one role, you can diverge further
between layers. If one person switches roles during a session, cross-role consistency
becomes critical and role identity must be unmissable.

## 4. Navigation architecture

### Per-role navigation

Do not build one navigation containing every destination with most items hidden. Build
role-appropriate navigation from the shared component.

| Role type | Pattern | Destinations |
|---|---|---|
| Customer / end user | Top bar, or side nav if >7 destinations | 4–8 |
| Operator | Side nav 240px + command palette | 8–20 |
| Administrator | Side nav with nested groups | 15–40 |
| Support | Side nav + global search-first | 10–20 |
| Field / mobile | Bottom nav, 3–5 destinations | 3–5 |

**Never duplicate a destination in two navigation systems.** It forces the user to learn which
one is authoritative.

### Role and organisation switching

If one person holds multiple roles or works across tenants:

| Element | Requirement |
|---|---|
| Current role | **Always visible**, not only in a menu |
| Current organisation | Always visible when multi-tenant |
| Switcher placement | Top bar or sidebar header — a consistent, predictable location |
| Switch feedback | Unambiguous confirmation of the new context |
| Visual differentiation | A subtle persistent marker per context (a label, or a 3px accent bar) |
| Impersonation / support access | **Unmistakable.** A persistent banner naming whose account is being viewed and offering exit |

**Impersonation without a persistent, high-visibility banner is how support staff take
destructive actions in the wrong account.** This is not a styling preference; it is an error-
prevention requirement. The banner must survive navigation and must not be dismissible.

### Elevated-permission modes

When an administrator holds destructive capability:

- Distinguish the administrative context visually — a persistent marker, not a different theme.
- **A different theme is the wrong answer.** It breaks cross-role recognition and doubles the
  design surface. A labelled bar or accent stripe is enough.
- Require re-authentication for the highest-consequence actions.
- Make it obvious when an action affects other people's data.

## 5. Permissions

The corpus offers nothing here. All synthesized, and all learned from how permission UIs fail.

| Situation | Correct treatment |
|---|---|
| Action not permitted | **Show it disabled with an explanation** — do not hide it |
| Explanation content | What permission is needed and who can grant it |
| Whole feature unavailable | Empty state explaining access, with a request path |
| Read-only record | Banner at the top; visibly non-editable fields |
| Partial permission | Permitted actions active, others disabled with reasons |
| Permission changed mid-session | Notify; do not fail silently on the next click |

**Hidden versus disabled** is the key judgment:

- **Disable + explain** when the user could plausibly gain the permission. This teaches the
  permission model.
- **Hide** when the feature is irrelevant to the role, when its existence is confidential, or —
  added after adversarial review (see
  [research/WEAK-GUIDE-REVIEW.md](../research/WEAK-GUIDE-REVIEW.md) A-05) — **when revealing it
  discloses system capability to a lower-privilege user.**

> **The security qualification matters and an earlier draft under-stated it.** "Disable and
> explain" is right for ordinary business permissions, where the explanation teaches the model
> and reduces support load. It is **wrong** where the control's existence is itself sensitive:
> an unprivileged user learning that a "force-reset all credentials" or "export full customer
> database" action exists has learned something useful to an attacker, and the explanation
> ("requires Security Admin") tells them which role to target.
>
> **Decision rule:** disable-and-explain by default; hide when the action's existence, name, or
> required role is information you would not put in public documentation. In a security-sensitive
> product, make that judgment per action rather than adopting one policy platform-wide.

Never disable without explanation *where you have chosen to disable rather than hide*. A
greyed-out button with no tooltip generates support tickets and reads as a bug.

## 6. Component requirements

### Tables — the primary operator surface

| Property | Customer | Operator |
|---|---|---|
| Row height | 48px | 36px |
| Font size | 16px | 14px |
| Visible columns | 4–6 | 8–12 |
| Sort | Yes | Yes |
| Filter | Simple | Faceted + saved views |
| Bulk actions | Rare | Required |
| Inline editing | No | Often |
| Density toggle | No | Useful |

Full table guidance: [dashboard-admin.md](dashboard-admin.md) §Tables.

### Workflow and approval flows

- Show progress: step N of M, with completed steps reviewable.
- Save partial progress. Losing a half-finished multi-step form is unacceptable at any
  frequency.
- Approval states need a visible state machine: submitted → in review → approved / rejected /
  changes requested.
- Show *who* is responsible for the current step and since when.
- Rejections require a reason. A rejected item with no reason generates a support conversation.
- Delegation and reassignment must be visible in the history.

### Status systems

**One status vocabulary across the whole platform.** The most common multi-role defect is
"pending" meaning different things in two surfaces.

| Requirement | Detail |
|---|---|
| Fixed set | Define every status once, centrally |
| Colour + icon + label | Never colour alone |
| Consistent colour mapping | Amber is always "needs attention", everywhere |
| Terminal vs. transient | Visually distinguish states that will change from those that will not |
| Definitions available | Hover or a legend — "what does 'held' mean?" must be answerable |

### Audit and history

Required wherever a role can affect another role's data:

- Who, what, when, from where — and the previous value for changes.
- Per-record history, not only a global log.
- Filterable by actor, action type, and date range.
- Absolute timestamps with timezone. Relative time is for recency, not for records.
- Immutable and visibly so.

### Notifications

- Role-appropriate: operators need work-queue notifications, customers need status changes.
- Separate *actionable* from *informational* — different treatment, ideally different tabs.
- Grouping and bulk-dismiss. An unbounded notification list is ignored.
- Never the only channel for something consequential.

### Bulk actions

- Selection state visible and counted: "12 selected".
- Action bar appears on selection without shifting the table.
- Confirmation names the count and the action: "Reject 12 claims?".
- Report partial failure honestly: "9 succeeded, 3 failed" with per-item reasons.
- Provide undo for reversible bulk operations, since bulk mistakes are large mistakes.

## 7. Designing for novices and experts simultaneously

The category's other hard problem. Neither audience should pay for the other.

| Technique | Serves novices | Serves experts |
|---|---|---|
| **Progressive disclosure** | Simple default view | Advanced options one click away |
| **Keyboard shortcuts** | Ignorable | Essential |
| **Command palette** | Never discovered, no cost | Primary navigation |
| **Density toggle** | Default comfortable | Compact available |
| **Saved views** | Sensible defaults | Own configurations |
| **Inline help** | Discoverable, dismissible | Dismissed once, permanently |
| **Guided flow + expert form** | Wizard path | Single dense form path |
| **Bulk operations** | Hidden until selection | Immediately available |

**The pattern that works: comfortable defaults, powerful accelerators.** Do not build two
interfaces — build one that rewards learning. Do not make novices configure their way to
usability, and do not force experts through a wizard they have completed four hundred times.

**Anti-pattern: identical dashboards for different roles.** If the customer dashboard and the
operator dashboard show the same six cards, at least one role is being poorly served. Each
role's landing view should answer *that role's* first question of the day.

## 8. Layout

| Property | Customer layer | Operator layer | Admin layer |
|---|---|---|---|
| Density | default | compact | compact |
| Container | 1280px | fluid to 1440px | fluid |
| Section rhythm | 48px | 32px | 32px |
| Page padding | 32px | 24px | 24px |
| Nav | top bar / side nav | side nav 240px or rail | side nav, nested |
| Card padding | 24px | 16px | 16px |
| Control height | 40px | 36px | 36px |
| Table row | 48px | 36px | 36px |
| Body size | 16px | 14px | 14px |
| Max display | 28px | 24px | 24px |

Note that every value moves together. A compact table inside default page padding reads as an
accident rather than a density choice.

## 9. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav | Drawer | Drawer or rail | Full side nav |
| Role switcher | In drawer header, still visible in top bar | Top bar | Top bar |
| Impersonation banner | **Always visible** | Always visible | Always visible |
| Tables | Transform to cards | Scroll + pin first column | Full |
| Bulk actions | Deferred or unavailable | Available | Available |
| Filters | Drawer | Drawer | Inline or panel |
| Multi-step forms | One step per screen | One step per screen | Steps or single form |
| Admin features | Some genuinely omitted — state it | Most available | All |

**Full mobile parity is not expected for operator and admin layers**, and pretending otherwise
produces unusable cramped interfaces. Decide per capability, and when something is
unavailable, say so in the interface rather than hiding the control.

Customer layers **do** need full parity.

## 10. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- Role and organisation context announced on change (live region).
- Permission-disabled controls carry `aria-disabled` **and** an accessible explanation —
  disabled elements that are unreachable by keyboard hide their own explanation.
- Impersonation banner is the first thing in the accessibility tree, and announced.
- Status is available as text, never colour alone — critical in dense tables.
- Bulk selection state announced: "12 of 340 rows selected".
- Table keyboard navigation: arrow keys between cells, clear focus, no traps.
- Approval and workflow state changes announced.
- Multi-step forms: `aria-current` on the active step; errors summarised with links to fields.

## 11. Do

- Build one token foundation and derive every role layer from it
- Keep status meanings identical across every role
- Make current role and organisation always visible
- Make impersonation unmistakable and non-dismissible
- Disable-and-explain rather than hide, when the permission is gettable
- Give each role a landing view answering that role's first question
- Provide audit history wherever one role affects another's data
- Save partial progress in every multi-step flow
- Report bulk-action partial failures per item
- Layer expert accelerators on comfortable defaults
- Use absolute timestamps with timezone in records
- Document the terminology mapping when roles genuinely differ

## 12. Do not

- Do not design role experiences independently
- Do not use a different theme to signal an administrative context
- Do not let status colours mean different things in different surfaces
- Do not show identical dashboards to roles with different jobs
- Do not disable a control without explaining why
- Do not expose internal administrative complexity to end customers
- Do not force experts through novice-oriented wizards
- Do not make novices configure their way to a usable default
- Do not allow impersonation without a persistent banner
- Do not hide bulk actions behind a menu operators use hourly
- Do not claim full mobile parity for operator tooling — state the limits
- Do not use relative timestamps in audit records

## 13. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/uber/DESIGN.md` § *Overview*, § *Components* | Multiple audiences (riders, drivers, business) on one rigorously consistent visual system — one pill geometry, one type voice, one illustration register. The recognition benefit of a shared foundation across audiences |
| `design-md/hashicorp/DESIGN.md` § *Colors* | Per-product accent colours as **identity tokens rather than decoration**. Transfers directly to per-role or per-tenant differentiation: vary one mapped token, keep the system |
| `design-md/binance/DESIGN.md` § *Overview*, § *Colors* | Explicit dual-track: dark marketing, light transactional, shared CTA colour and hairlines. Proof that one system can carry opposite polarities when the surface's job differs |
| `design-md/shopify/DESIGN.md` § *Overview* | Two tracks sharing typographic DNA and diverging sharply in canvas polarity and density — marketing vs. pricing/signup/dashboard |
| `design-md/starbucks/DESIGN.md` § *Color Palette & Roles* | Four calibrated shades of one brand hue, each mapped to a specific surface role. The model for differentiating layers without introducing new colours |
| `design-md/linear.app/DESIGN.md` § *Elevation & Depth* | A four-step surface ladder carrying hierarchy without shadow — the mechanism for building density variation inside one palette |

## 14. Common mistakes

| Mistake | Consequence | Correction |
|---|---|---|
| Independent per-role design | Four products, one logo | Shared foundation, layered variation |
| Identical dashboards per role | At least one role poorly served | Role-specific default views |
| Status drift between surfaces | Real operational errors | One central status vocabulary |
| Silent permission failures | Support tickets, perceived bugs | Disable + explain |
| Admin theme switching | Breaks recognition, doubles surface | Persistent marker instead |
| Invisible impersonation | Destructive actions in wrong accounts | Non-dismissible banner |
| Marketing density in operator tools | Slow all-day work | Compact mode, 32px rhythm |
| Wizard-only workflows | Experts obstructed | Offer an expert path |
| No audit trail | Disputes unresolvable | Per-record history |
| Bulk actions without partial-failure reporting | Silent data problems | Per-item results |

## 15. Review checklist

[checklists/commercial-platform-review.md](../checklists/commercial-platform-review.md)

## 16. Templates

- [templates/DESIGN.multi-role-platform.md](../templates/DESIGN.multi-role-platform.md)
- [templates/ROLE-EXPERIENCE-MAP.md](../templates/ROLE-EXPERIENCE-MAP.md)
