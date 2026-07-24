# Prompt 06 — Build a role-based commercial platform surface

---

```
Build <SURFACE> for the <ROLE> layer of <PLATFORM>.

ROLE CONTEXT
- Role: <name>
- Expertise: <novice | trained | expert>
- Frequency: <weekly | daily | all day>
- Session length: <minutes | hours>
- Device: <desktop | mobile | both>
- Top 3 tasks: <list>
- Data scope: <own | team | organisation | platform>
- Can affect other roles' data: <yes/no>
- Destructive capability: <what they can irreversibly do>
- Error consequence: <trivial | recoverable | data loss | financial | regulatory>

PLATFORM CONTEXT
- All roles: <list>
- Does one person hold multiple roles? <yes/no — this decides how much layers may diverge>
- Multi-tenant / organisation switching? <yes/no>
- Impersonation or support access exists? <yes/no>

STEP 1 — INSPECT. Report before writing code:
- The project DESIGN.md and any role experience map
- The shared component library — what already exists
- How OTHER roles' equivalent surfaces look. This surface must belong to the same product.
- The platform's status vocabulary. I need the canonical list, not an invented one.
- How permissions are represented in code
- How role and organisation context is stored and displayed
Report what you found, and specifically: which status values already exist and what each means.

STEP 2 — BUILD

Shared with every other role — do not vary these:
- All tokens, type scale, radius character, spacing base
- STATUS COLOUR MEANINGS. "Amber = needs attention" must be identical platform-wide.
  Status drift between role surfaces causes real operational errors.
- Component behaviour and all interaction states
- Form conventions, feedback patterns, destructive-action patterns
- Terminology for shared objects
- Accessibility floor
- Keyboard conventions

Varies for THIS role:
- Density: <compact for operators/admins, default for customers>
- Navigation pattern and destination set
- Section rhythm and page padding, matching the density
- Information density and default view
- Available actions, by permission
- Workflow depth

Required for this surface:
- A default view that answers THIS role's first question of the day. Do not reuse another
  role's dashboard.
- Current role and organisation visible at all times, not only in a menu.
- If impersonation is possible: a persistent, NON-DISMISSIBLE banner naming the account being
  viewed, with an exit control. This survives navigation.
- Permissions: show unavailable actions DISABLED with an explanation of what permission is
  needed and who can grant it. Hide only when the feature is irrelevant to the role or its
  existence is confidential. Never disable without explanation.
- Status: colour + icon + text. Never colour alone.
- Audit history if this role can affect others' data: who, what, when, previous value.
  Absolute timestamps with timezone.
- Bulk actions if applicable: visible on selection without layout shift, count shown,
  confirmation naming count and action, per-item partial-failure reporting, undo where
  reversible.
- All data states: first-run empty, filtered-empty, loading, refresh (keep data visible),
  partial, error, permission denied.
- Tables: sticky header, hairline rows (no zebra), right-aligned tabular numerics, pinned
  identifying column when scrolling, em-dash for empty cells, filter state in the URL.

Expert accelerators layered on comfortable defaults:
- Keyboard shortcuts, command palette, saved views, density toggle, bulk operations.
  Invisible to novices, essential to experts. Do not build two interfaces.

Responsive:
- Full parity is NOT expected for operator and admin layers. Decide per capability and STATE
  in the interface when something requires a larger screen. Do not silently hide controls.
- Customer layers DO need full parity.
- Force comfortable density on touch regardless of the role's default.

CONSTRAINTS
- Do NOT design this role's experience independently. It is a layer on a shared foundation.
- Do NOT use a different theme to signal an administrative context. Use a persistent labelled
  marker.
- Do NOT invent a new status value. Use the platform's vocabulary; if a new one is genuinely
  needed, flag it as a platform-level decision.
- Do NOT expose internal administrative complexity to end-customer roles.
- Do NOT force experts through novice-oriented wizards. Offer both paths.

REPORT
SHARED           - what this surface inherits unchanged
VARIED           - what differs for this role, and why the role requires it
STATUS VOCABULARY- confirm you used existing values; list any new one proposed
PERMISSIONS      - how unavailable actions are communicated
REUSED / CREATED
ASSUMPTIONS / DEVIATIONS / INVENTED VALUES / UNRESOLVED
MOBILE LIMITS    - capabilities unavailable on small screens, and how that is communicated
```
