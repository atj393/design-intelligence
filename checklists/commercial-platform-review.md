# Commercial Multi-Role Platform Review Checklist

Run [foundation-review.md](foundation-review.md) and, for operator surfaces,
[dashboard-review.md](dashboard-review.md) first.

Reference: [../categories/commercial-multi-role-platform.md](../categories/commercial-multi-role-platform.md) ·
[../templates/ROLE-EXPERIENCE-MAP.md](../templates/ROLE-EXPERIENCE-MAP.md) —
**predominantly synthesized; validate with real users of each role.**

---

## 1. Shared foundation — must be identical across every role

- [ ] Primitive and semantic tokens
- [ ] Type families and scale ratios
- [ ] Radius character
- [ ] Spacing base unit
- [ ] **Status colour meanings**
- [ ] Core component behaviour and all eight interaction states
- [ ] Form conventions — label position, validation timing, error presentation
- [ ] Feedback semantics — toast vs. banner vs. modal
- [ ] Destructive-action pattern
- [ ] Accessibility floor
- [ ] Terminology for shared objects
- [ ] Keyboard conventions

**Test:** open two roles' surfaces side by side. Does a button, an input, a table row, and a status
badge look and behave identically?

## 2. Status vocabulary

The most consequential item in this checklist — drift here causes real operational errors.

- [ ] One central vocabulary, defined once
- [ ] Every status has colour + icon + text
- [ ] **The same word means the same thing in every role surface**
- [ ] Colour mapping is consistent — amber is always "needs attention"
- [ ] Terminal and transient states are visually distinguished
- [ ] Definitions are available to users (hover or legend)
- [ ] No surface has invented a status outside the vocabulary

**Test:** list every status string in the codebase. Any duplicates with different meanings, or
synonyms for the same state, are findings.

## 3. Per-role appropriateness

- [ ] Each role's default landing view answers **that role's** first question of the day
- [ ] **No two roles share an identical dashboard** — if they do, at least one is poorly served
- [ ] Density matches the role's frequency and device
- [ ] Navigation destination count matches the role's actual scope
- [ ] Terminology matches the role's vocabulary, with mappings documented
- [ ] Onboarding depth matches the role's expertise
- [ ] A novice role is not given an expert-density interface
- [ ] An expert role is not forced through a novice wizard

## 4. Role and organisation context

- [ ] **Current role visible at all times**, not only in a menu
- [ ] **Current organisation visible** when multi-tenant
- [ ] Switcher in a consistent, predictable location
- [ ] Switching gives unambiguous confirmation of the new context
- [ ] A subtle persistent marker differentiates contexts
- [ ] **No different theme for administrative contexts** — a labelled marker instead
- [ ] Context changes announced to assistive tech

## 5. Impersonation and support access

If impersonation exists:

- [ ] Persistent banner naming the account being viewed
- [ ] **Non-dismissible**
- [ ] **Survives navigation**
- [ ] Includes an exit control
- [ ] First in the accessibility tree, and announced
- [ ] Visible at every viewport width
- [ ] Destructive actions during impersonation carry extra confirmation

**Test:** enter impersonation, navigate three pages, resize to 375px. Is the banner still there?

## 6. Permissions

- [ ] Unavailable-but-gettable actions are **disabled with an explanation**
- [ ] The explanation states what permission is needed **and who can grant it**
- [ ] Nothing is disabled without an explanation
- [ ] Hidden features are hidden only because they are irrelevant or confidential
- [ ] Whole-feature unavailability has an empty state with a request path
- [ ] Read-only records carry a banner and visibly non-editable fields
- [ ] Partial permission shows permitted actions active, others disabled with reasons
- [ ] Mid-session permission change notifies rather than failing silently
- [ ] `aria-disabled` used with a **reachable** explanation — a disabled element unreachable by
      keyboard hides its own explanation

## 7. Workflow and approval

- [ ] Progress shown as step N of M; completed steps reviewable
- [ ] **Partial progress saved** — a half-finished multi-step form is never lost
- [ ] Approval state machine visible
- [ ] Current owner of each step visible, and how long it has been there
- [ ] Rejections require a reason
- [ ] Delegation and reassignment appear in the history
- [ ] Handoffs notify the receiving role in a channel they actually watch
- [ ] The sending role gets confirmation

## 8. Audit and history

Where any role can affect another's data:

- [ ] Who, what, when, from where recorded
- [ ] Previous value recorded for changes
- [ ] Per-record history, not only a global log
- [ ] Filterable by actor, action type, and date range
- [ ] **Absolute timestamps with timezone**
- [ ] Immutable, and visibly so
- [ ] Corrections appear as new entries, never as edits

## 9. Bulk actions and destructive operations

- [ ] Bar appears without layout shift; count shown
- [ ] Confirmation names count and action
- [ ] Partial failures reported per item
- [ ] Undo for reversible operations
- [ ] Destructive not adjacent to primary; never default-focused
- [ ] Actions affecting other people's data state that explicitly

## 10. Expert accelerators

Layered on comfortable defaults, not replacing them:

- [ ] Keyboard shortcuts
- [ ] Command palette (with discoverable alternatives)
- [ ] Saved views
- [ ] Density toggle
- [ ] Bulk operations
- [ ] An expert form path alongside any guided path
- [ ] None of these degrade the novice experience

## 11. Boundary discipline

- [ ] Internal administrative complexity is **not** exposed to customer roles
- [ ] Customer-facing terminology does not leak internal jargon
- [ ] No role can see another's data without an explicit permission
- [ ] Role surfaces do not read as separate products

**Test:** show a customer surface and an admin surface to someone unfamiliar with the product. Do
they identify them as one product?

## 12. Responsive

- [ ] Customer layer: **full parity**
- [ ] Operator and admin layers: parity not claimed
- [ ] Unavailable capabilities **stated in the interface**, not silently hidden
- [ ] Role and organisation context visible at every width
- [ ] Impersonation banner visible at every width
- [ ] Comfortable density forced on touch, regardless of the role's default

## 13. Accessibility

- [ ] Role and organisation changes announced
- [ ] Permission-disabled controls have reachable explanations
- [ ] Status available as text in dense tables
- [ ] Bulk selection announced
- [ ] Table keyboard navigation works
- [ ] Workflow state changes announced
- [ ] Multi-step forms use `aria-current`; errors summarised with links to fields
- [ ] Touch targets ≥44px in every layer

## 14. The two failure modes

Check for both. They pull in opposite directions.

**Fragmentation** — four products wearing one logo:
- [ ] Tokens identical across roles
- [ ] Component behaviour identical
- [ ] Status meanings identical
- [ ] A user moving between roles recognises the system

**Flattening** — everyone gets the same interface:
- [ ] Densities differ where frequency differs
- [ ] Landing views differ per role
- [ ] Navigation scope differs per role
- [ ] No role is paying for another role's needs
