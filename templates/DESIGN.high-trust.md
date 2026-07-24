---
# Financial / security / legal / high-consequence DESIGN.md
# Copy to project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md. Guide: categories/financial-high-trust.md
#   Visual expression is corpus-backed. VERIFICATION, CONFIRMATION, AUDIT, and IRREVERSIBLE
#   ACTION FLOWS ARE SYNTHESIZED — and they are the part that matters most here.

version: 1
name: [[SET: product-name]]-design-system
category: high-trust
density: default            # NEVER compact. Mis-clicks are the failure mode here.
mode: [[CHOOSE: light | dark | both]]
description: >
  [[SET: What the product does, what a user error costs, and which actions cannot be undone.
  Trust in this category is produced by behaviour — clarity, confirmation, traceability,
  error prevention — not by a conservative palette. State the highest-consequence action here.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET: must be distinct from accent if accent is red]]", info: "[[SET]]" }
  value: { positive: "[[SET]]", negative: "[[SET]]", neutral: "[[SET]]" }
  # Value direction ALSO requires a sign and an arrow. Red/green is exactly the pair
  # colour-blind users cannot distinguish.

semantic:
  light:
    surface-canvas: "{primitives.neutral.50}"
    surface-raised: "#ffffff"
    surface-sunken: "{primitives.neutral.100}"
    surface-overlay: "#ffffff"
    surface-review: "[[SET: distinct surface for confirmation/review steps]]"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    text-legal: "{primitives.neutral.700}"   # 16px MINIMUM. Small print is a design failure.
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    action-primary: "{primitives.accent.600}"
    action-commit: "[[SET: the money-moving / binding action]]"
    action-destructive: "{primitives.status.danger}"
    status-pending: "{primitives.status.warning}"
    status-pending-surface: "[[SET]]"
    status-settled: "{primitives.status.success}"
    status-settled-surface: "[[SET]]"
    status-failed: "{primitives.status.danger}"
    status-failed-surface: "[[SET]]"
    value-positive: "{primitives.value.positive}"
    value-negative: "{primitives.value.negative}"
    focus-ring: "{primitives.accent.500}"
    scrim: "rgba(0,0,0,0.50)"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-raised: "{primitives.neutral.900}"
    surface-sunken: "#000000"
    surface-overlay: "{primitives.neutral.800}"
    surface-review: "[[SET]]"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    text-legal: "{primitives.neutral.300}"
    border-subtle: "rgba(255,255,255,0.08)"
    border-default: "rgba(255,255,255,0.14)"
    action-primary: "{primitives.accent.500}"
    action-commit: "[[SET]]"
    action-destructive: "[[SET: lightened, desaturated 10-20%]]"
    status-pending: "[[SET]]"
    status-pending-surface: "[[SET]]"
    status-settled: "[[SET]]"
    status-settled-surface: "[[SET]]"
    status-failed: "[[SET]]"
    status-failed-surface: "[[SET]]"
    value-positive: "[[SET]]"
    value-negative: "[[SET]]"
    focus-ring: "{primitives.accent.400}"
    scrim: "rgba(0,0,0,0.65)"

typography:
  families: { display: "[[SET]]", body: "[[SET]]", mono: "[[SET: for references and IDs]]" }
  substitutes: { display: "[[SET: if proprietary]]", body: "[[SET]]" }
  scale:
    display-1:  { size: 44px, weight: "[[CHOOSE: 300 | 400 | 500 | 700 | 900]]", lineHeight: 1.08, tracking: -1.0px }
    heading-1:  { size: 30px, weight: 600, lineHeight: 1.20, tracking: -0.4px }
    heading-2:  { size: 22px, weight: 600, lineHeight: 1.30, tracking: -0.2px }
    heading-3:  { size: 17px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:       { size: 16px, weight: 400, lineHeight: 1.55, tracking: 0 }
    body-sm:    { size: 14px, weight: 400, lineHeight: 1.50, tracking: 0 }
    legal:      { size: 16px, weight: 400, lineHeight: 1.65, tracking: 0 }   # NEVER smaller
    caption:    { size: 13px, weight: 400, lineHeight: 1.45, tracking: 0 }
    label:      { size: 15px, weight: 500, lineHeight: 1.20, tracking: 0 }
    amount-xl:  { size: 40px, weight: 600, lineHeight: 1.10, tracking: -0.6px, features: "tabular-nums" }
    amount-lg:  { size: 26px, weight: 600, lineHeight: 1.20, tracking: -0.3px, features: "tabular-nums" }
    amount:     { size: 17px, weight: 500, lineHeight: 1.35, tracking: 0, features: "tabular-nums" }
    amount-sm:  { size: 15px, weight: 400, lineHeight: 1.35, tracking: 0, features: "tabular-nums" }
    reference:  { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0, family: mono }
# TABULAR FIGURES ON EVERY NUMERIC TOKEN. Non-negotiable in this category.

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px, 16: 64px }
  section: { marketing: 64px, product: 40px }
  destructive-separation: 32px   # minimum gap between a committing and a safe action
  page-padding: { mobile: 20px, tablet: 24px, desktop: 32px }

radius:
  character: "[[CHOOSE: squared | default | soft]]"
  # The corpus refutes "high-trust must be squared" — a major payments brand is
  # pill-dominant with 40px hero corners. Choose from audience, not from assumption.
  none: 0
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  full: 9999px

layout:
  container: 1200px
  prose: 680px
  legal-prose: 680px
  confirmation: 560px
  sidebar-nav: 240px
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px }

elevation: { 0: "none", 1: "1px solid {semantic.border-subtle}", 3: "0 4px 12px rgba(0,0,0,0.10)", 4: "0 12px 32px rgba(0,0,0,0.16)", strategy: border-first }

motion: { fast: 150ms, base: 200ms, reduced-motion: "instant, state preserved" }

components:
  button-primary:   { height: 44px, padding: "12px 20px", radius: md, surface: action-primary, text: "#ffffff", type: label }
  button-commit:    { height: 48px, padding: "14px 24px", radius: md, surface: action-commit, text: "#ffffff", type: label, names-action-and-amount: true }
  button-destructive:{ height: 44px, padding: "12px 20px", radius: md, surface: action-destructive, text: "#ffffff", type: label }
  text-input:       { height: 44px, padding: "12px 14px", radius: md, border: border-default }
  amount-input:     { height: 56px, padding: "16px", radius: md, type: amount-lg, inputmode: decimal, echo-parsed-value: true }
  balance-block:    { shows: "available + pending + total, each LABELLED", type: amount-xl }
  value-change:     { content: "sign + arrow + colour", type: amount }
  transaction-row:  { padding: "14px 0", border-bottom: border-subtle, includes: "date, description, counterparty, amount, status, balance-after" }
  status-badge:     { height: 22px, padding: "3px 9px", radius: full, type: caption, content: "icon + text + colour" }
  review-panel:     { padding: 24px, radius: lg, surface: surface-review, itemises: "amount, all fees, rate + timestamp, recipient, arrival, cancellability" }
  confirm-modal:    { width: 560px, padding: 28px, radius: lg, elevation: 4, scrim: true, typed-confirmation-for-irreversible: true }
  session-warning:  { placement: "banner", warns-before-timeout: true, offers-extension: true, preserves-form-data: true }
  legal-block:      { type: legal, max-width: legal-prose, downloadable: true, version-and-date-shown: true }
  consent-checkbox: { unchecked-by-default: true, specific-not-bundled: true, records: "timestamp + document version" }
  support-link:     { placement: "every transactional surface", shows-expected-response-time: true }
---

# [[SET: Product name]] — High-Trust Design System

## 1. Product context

- **What it does:** [[SET]]
- **What a user error costs:** [[SET]]
- **Irreversible actions:** [[SET: enumerate them — this list drives §6]]
- **Regulatory constraints:** [[SET]]
- **Verification required:** [[CHOOSE: none | identity | documents | multi-step]]
- **Multi-currency:** [[CHOOSE: no | yes — [[SET: currencies]]]]
- **Balance concepts:** [[SET: e.g. available, pending, total — each needs its own label]]

## 2. Experience principles

1. **Prevent, then confirm, then allow recovery.** In that order.
2. **The user always knows whether something happened.** Especially on failure.
3. **[[SET: your third, and what it rules out]]**

## 3. Trust is behaviour, not aesthetic

The corpus refutes both common assumptions: a major payments brand is maximally *soft* (40px hero
corners, pill cards); trusted financial brands use display weights from 300 to 900. What is
consistent is restrained accent use, tabular figures, and clear separation of marketing from
transactional surfaces.

**So: invest in confirmation, traceability, and error prevention.** A conservative palette is not a
trust strategy.

## 4. Displaying money and values

| Requirement | Applied here |
|---|---|
| **Tabular figures** | Every numeric token. Non-negotiable |
| Currency | [[SET: explicit code or unambiguous symbol]] |
| Decimal places | [[SET: consistent per context; never silently truncated]] |
| Alignment | Right in tables and lists |
| Negatives | Minus sign **and** colour. [[CHOOSE: minus | parentheses (accounting)]] |
| Large numbers | Localised thousands separators |
| Rounding | Stated when a displayed value is rounded |
| Pending vs. settled | Visually distinguished, **both labelled** |
| Exchange rate | Rate + timestamp + fee, shown separately |
| **Balances** | `available`, `pending`, `total` — **separately labelled.** Never one ambiguous "balance" |

**Value direction requires three channels:** `+2.41% ▲` / `−1.08% ▼` — sign, arrow, and colour.

## 5. Records

- `transaction-row`: date, description, counterparty, amount, status, balance-after.
- **Absolute timestamps with timezone.** Relative time is for recency, never for records.
- Copyable `reference` on every record.
- Detail view: full fee breakdown, exchange rate, timestamp per state change.
- Downloadable receipt; export with stated fields and applied filters.
- **Corrections are additive.** A record that silently changes is not a record — show the original
  and the correction, linked.

## 6. Confirmation and irreversible actions

| Consequence | Pattern |
|---|---|
| Reversible, low value | Direct + toast with undo |
| Reversible, high value | Confirmation stating amount and recipient |
| Delayed execution | Show the cancellation window and how to use it |
| **Irreversible** | `review-panel` + `confirm-modal` + **typed confirmation** |
| Affects others | State exactly who is affected and how |
| Legally binding | Full terms shown; deliberate affirmative action; consent recorded |

### Review step — required before any money movement or binding commitment

Shows: exact amount in source **and** destination currency · **all fees itemised** · exchange rate
with timestamp · recipient with verifiable detail · expected arrival · whether and until when it
can be cancelled · a clear route back to edit.

- **`button-commit` names the action and amount:** "Send £2,400 to J. Okafor". Never "Confirm".
- **Never default-focus the committing action.**
- **Minimum `{spacing.destructive-separation}` between the committing action and cancel/back.**

**Irreversible actions requiring typed confirmation:** [[SET: list from §1]]

## 7. Verification and sessions

- Explain what is needed, why, and how long it takes — **before** starting.
- Document upload: requirements shown, validated before submission, retry allowed.
- Verification pending: state and expected duration. Failed: reason and remedy.
- MFA setup: explain the method, **provide and confirm recovery codes**.
- Step-up auth: explain why *this* action requires it.
- **`session-warning`: warn before timeout, allow extension, preserve form data.** Losing a
  half-completed form to a timeout is unacceptable here (WCAG 2.2.1).
- On expiry, return the user to where they were with their input intact.

## 8. Security settings

Current state visible: active factors, trusted devices, open sessions (device, location, last
active) with individual and bulk revoke. Password change requires the current password, states
requirements up front, and **never blocks paste**. Recovery codes generated, shown once, confirmed
saved, regenerable. Security event log. Out-of-band notification for security-relevant changes.
Dangerous settings separated and individually confirmed, with the consequence of disabling a
protection stated.

## 9. Errors

Every error states: what happened · why, if known · what to do next · a copyable reference ·
**whether anything was charged, changed, or committed.**

That last item is specific to this category and routinely omitted. "Payment failed" leaves the user
not knowing if they were charged. **"Payment failed — you have not been charged. Try another card."**
resolves it.

**Never a generic error in a money flow.**

## 10. Legal and regulatory content

`legal-block` at `{typography.legal}` — **16px minimum. Small print for legally material text is a
design failure and increasingly a compliance one.** Structured with headings and a table of
contents for long documents. Version and effective date shown; previous versions accessible.
Changes notified with a summary of what changed. Consent unchecked by default, specific rather than
bundled, recorded with timestamp and document version. Downloadable.

## 11. Support

`support-link` on **every** transactional surface, with expected response time. Provide the
reference identifier before the user asks. Never a dead end — if a channel is closed, say when it
opens. Immediate path for urgent matters (suspected fraud, card loss).

## 12. States

All ten from the foundation, plus: verification pending · verification failed · payment declined ·
payment technical failure (distinguish!) · awaiting approval · cancellation window open ·
account restricted · session expiring.

## 13. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Transaction list | Card rows | Table, scroll | Full table |
| Transaction detail | Full-screen route | Overlay | Panel or route |
| Confirmation flow | **One step per screen** | One step per screen | Steps or single review |
| Amount entry | `amount-input`, numeric keyboard | Standard | Standard |
| Legal documents | Full − 40px, **16px body** | 680px | 680px |
| Security settings | Stacked sections | Sections | Sections |

**Full mobile parity expected** — money is managed on phones. Confirmation flows must be *more*
careful on mobile, not less: smaller targets, more distraction, higher error rates.

## 14. Accessibility commitments

- [ ] **Error prevention: reversible, checked, or confirmed** (WCAG 3.3.4)
- [ ] **Timeout warning with extension** (WCAG 2.2.1) and form data preserved
- [ ] Value direction never colour alone (WCAG 1.4.1)
- [ ] Amounts programmatically associated with their labels
- [ ] Errors announced; focus moved to the summary (WCAG 3.3.1)
- [ ] Consent controls fully keyboard-operable and clearly labelled
- [ ] Legal text usable at 200% zoom without loss
- [ ] `inputmode` set for numeric entry
- [ ] Status changes announced (pending → settled)
- [ ] **No financially material information revealed only on hover**
- [ ] Amount entry echoes the parsed value before confirmation: "You are sending £1,200.00" —
      ambiguity between `1,200` and `1.200` is a real cross-locale failure
- [ ] Contrast ≥4.5:1 body, ≥3:1 UI, both modes
- [ ] Paste permitted in password and card fields

## 15. Do

- Use tabular figures everywhere
- Label available, pending, and total separately
- Convey direction with sign, arrow, and colour
- Use absolute timestamps with timezone in records
- Make corrections additive
- Itemise every fee
- Name the action and amount in the commit button
- Require typed confirmation for irreversible actions
- Warn before timeout and preserve data
- State whether the user was charged when payment fails
- Keep legal text at 16px minimum
- Show support on every transactional surface

## 16. Do not

- Do not use compact density
- Do not use relative timestamps in records
- Do not show a single ambiguous balance
- Do not convey gain/loss by colour alone
- Do not use generic errors in money flows
- Do not place the commit action beside cancel, or default-focus it
- Do not set legally material text below 16px
- Do not pre-check or bundle consent
- Do not lose form data on timeout or error
- Do not block paste in password or card fields
- Do not bury support
- Do not treat a conservative palette as the trust strategy

## 17. Implementation notes

- **Token delivery:** [[SET]]
- **Amount parsing and locale handling:** [[SET: how `1,200` vs `1.200` is disambiguated]]
- **Session timeout mechanism:** [[SET: warning threshold + data preservation]]
- **Audit log source:** [[SET]]
- **Consent recording:** [[SET: what is stored]]
- **Payment provider:** [[SET: and how charged-vs-not-charged is determined on failure]]
- **Existing components to reuse:** [[SET]]

## 18. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/financial-high-trust.md`, then this file. This file
wins.

**Before generating:** inspect existing amount formatting, transaction components, confirmation
patterns, session handling, and audit logging. Report findings.

**While generating:** tabular figures on every numeric. Separate balance labels. Three-channel
value direction. Absolute timestamps. Itemised fees. Named commit buttons. Typed confirmation for
irreversible actions. Never compact density.

**Then report:** assumptions, deviations, invented values, unresolved decisions, reused vs. created
components, and explicitly confirm: (a) every irreversible action has a review step and typed
confirmation, (b) payment failure states whether the user was charged, (c) session timeout warns
and preserves data, (d) no legally material text is below 16px, (e) value direction uses three
channels.
