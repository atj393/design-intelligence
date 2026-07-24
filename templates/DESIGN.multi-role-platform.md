---
# Commercial multi-role platform DESIGN.md
# ONE file for the whole platform. Do not fork per role — that produces several products
# wearing one logo. Complete ROLE-EXPERIENCE-MAP.md alongside this.
# Extends DESIGN.foundation.md. Guide: categories/commercial-multi-role-platform.md
#   NOTE: that guide is predominantly SYNTHESIZED. Validate with real users of each role.

version: 1
name: [[SET: platform-name]]-design-system
category: multi-role-platform
roles: [ "[[SET: role]]", "[[SET: role]]", "[[SET: role]]" ]
multi-tenant: [[CHOOSE: no | yes]]
one-person-multiple-roles: [[CHOOSE: no | yes]]   # if yes, cross-role consistency is critical
impersonation-exists: [[CHOOSE: no | yes]]
mode: [[CHOOSE: light | dark | both]]
description: >
  [[SET: What the platform does, which roles use it, and what must feel identical to someone
  who moves between roles. The design problem in this category is the boundary between shared
  and varied — get it wrong in either direction and you get fragmentation or flattening.]]

# ===========================================================================
# SHARED — identical for EVERY role. Changing any of these fragments the product.
# ===========================================================================
primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]", info: "[[SET]]", neutral: "[[SET]]" }

semantic:
  light:
    surface-canvas: "{primitives.neutral.50}"
    surface-shell: "#ffffff"
    surface-raised: "#ffffff"
    surface-sunken: "{primitives.neutral.100}"
    surface-row-hover: "{primitives.neutral.100}"
    surface-row-selected: "[[SET: accent tint ~8%]]"
    surface-overlay: "#ffffff"
    surface-impersonation: "[[SET: distinct, high-visibility — for the banner ONLY]]"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    text-disabled: "{primitives.neutral.400}"
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    action-primary: "{primitives.accent.600}"
    action-destructive: "{primitives.status.danger}"
    status-success: "{primitives.status.success}"
    status-success-surface: "[[SET]]"
    status-warning: "[[SET: darkened for text contrast]]"
    status-warning-surface: "[[SET]]"
    status-danger: "{primitives.status.danger}"
    status-danger-surface: "[[SET]]"
    status-info: "{primitives.status.info}"
    status-info-surface: "[[SET]]"
    focus-ring: "{primitives.accent.500}"
    scrim: "rgba(0,0,0,0.40)"
  dark:
    # Derived, not inverted. See DESIGN.foundation.md for the full derivation rules.
    surface-canvas: "{primitives.neutral.950}"
    surface-shell: "{primitives.neutral.900}"
    surface-raised: "{primitives.neutral.900}"
    surface-sunken: "#000000"
    surface-row-hover: "{primitives.neutral.800}"
    surface-row-selected: "[[SET: accent tint ~14%]]"
    surface-overlay: "{primitives.neutral.800}"
    surface-impersonation: "[[SET]]"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    text-disabled: "{primitives.neutral.600}"
    border-subtle: "rgba(255,255,255,0.08)"
    border-default: "rgba(255,255,255,0.14)"
    action-primary: "{primitives.accent.500}"
    action-destructive: "[[SET: lightened]]"
    status-success: "[[SET]]"
    status-success-surface: "[[SET]]"
    status-warning: "[[SET]]"
    status-warning-surface: "[[SET]]"
    status-danger: "[[SET]]"
    status-danger-surface: "[[SET]]"
    status-info: "[[SET]]"
    status-info-surface: "[[SET]]"
    focus-ring: "{primitives.accent.400}"
    scrim: "rgba(0,0,0,0.60)"

# THE STATUS VOCABULARY — defined ONCE, identical in every role surface.
# Status drift between surfaces causes real operational errors. This block is the fix.
status-vocabulary:
  - { value: "[[SET: e.g. draft]]",     colour: status-neutral, icon: "[[SET]]", label: "[[SET]]", terminal: false, means: "[[SET]]" }
  - { value: "[[SET: e.g. submitted]]", colour: status-info,    icon: "[[SET]]", label: "[[SET]]", terminal: false, means: "[[SET]]" }
  - { value: "[[SET: e.g. review]]",    colour: status-warning, icon: "[[SET]]", label: "[[SET]]", terminal: false, means: "needs attention" }
  - { value: "[[SET: e.g. approved]]",  colour: status-success, icon: "[[SET]]", label: "[[SET]]", terminal: true,  means: "[[SET]]" }
  - { value: "[[SET: e.g. rejected]]",  colour: status-danger,  icon: "[[SET]]", label: "[[SET]]", terminal: true,  means: "[[SET]]" }

typography:
  families: { body: "[[SET]]", mono: "[[SET]]" }
  substitutes: { body: "[[SET: if proprietary]]" }
  scale:
    heading-1: { size: 26px, weight: 600, lineHeight: 1.25, tracking: -0.4px }
    heading-2: { size: 20px, weight: 600, lineHeight: 1.30, tracking: -0.2px }
    heading-3: { size: 16px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:      { size: 16px, weight: 400, lineHeight: 1.50, tracking: 0 }   # customer layer
    body-dense:{ size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }   # operator layer
    body-sm:   { size: 13px, weight: 400, lineHeight: 1.40, tracking: 0 }
    caption:   { size: 12px, weight: 400, lineHeight: 1.35, tracking: 0.1px }
    overline:  { size: 11px, weight: 600, lineHeight: 1.30, tracking: 0.6px, transform: uppercase }
    label:     { size: 14px, weight: 500, lineHeight: 1.20, tracking: 0 }
    numeric:   { size: 15px, weight: 400, lineHeight: 1.40, tracking: 0, features: "tabular-nums" }
    code:      { size: 13px, weight: 400, lineHeight: 1.50, tracking: 0, family: mono }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px }

radius:
  character: "[[CHOOSE: squared | default | soft]]"
  none: 0
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  full: 9999px

# ===========================================================================
# PER-LAYER — these MAY vary by role. Everything above may not.
# ===========================================================================
layers:
  customer:
    density: default
    container: 1280px
    section: 48px
    page-padding: 32px
    nav: "[[CHOOSE: top bar | side nav 240px]]"
    control-height: 40px
    table-row: 48px
    body-token: body
    max-display: 26px
  operator:
    density: compact
    container: fluid
    section: 32px
    page-padding: 24px
    nav: "side nav 240px, collapsible to 56px rail, + command palette"
    control-height: 36px
    table-row: 36px
    body-token: body-dense
    max-display: 20px
  admin:
    density: compact
    container: fluid
    section: 32px
    page-padding: 24px
    nav: "side nav with nested groups + search"
    control-height: 36px
    table-row: 36px
    body-token: body-dense
    max-display: 20px

layout:
  prose: 680px
  top-bar: 56px
  detail-panel: 360px
  sticky-budget: 20vh
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation:
  0: "none"
  1: "1px solid {semantic.border-subtle}"
  3: "0 4px 12px rgba(0,0,0,0.10)"
  4: "0 12px 32px rgba(0,0,0,0.14)"
  strategy: border-first

motion: { instant: 100ms, fast: 150ms, base: 200ms, reduced-motion: "instant, state preserved" }

components:
  # Shared across all roles. Only dimensions vary by layer density.
  button-primary:     { padding: "8px 14px", radius: md, surface: action-primary, text: "#ffffff", type: label }
  button-destructive: { padding: "8px 14px", radius: md, surface: action-destructive, text: "#ffffff", type: label }
  text-input:         { padding: "8px 12px", radius: md, border: border-default }
  status-badge:       { padding: "2px 8px", radius: full, type: caption, content: "icon + text + colour" }
  table-row:          { border-bottom: border-subtle, no-zebra: true }
  role-switcher:      { height: 36px, placement: "top bar, consistent location", always-visible: true }
  org-switcher:       { height: 36px, placement: "top bar", searchable-above: 8 }
  impersonation-banner: { height: 44px, surface: surface-impersonation, dismissible: false, persistent-across-navigation: true }
  permission-tooltip: { max-width: 280px, content: "what permission is needed + who grants it" }
  audit-row:          { type: body-sm, timestamp: "absolute with timezone" }
  bulk-action-bar:    { height: 48px, elevation: 3, reserved: true }
  approval-stepper:   { step-size: 24px, shows: "current owner + duration in state" }
  command-palette:    { width: 600px, top: 20vh, radius: lg, elevation: 4 }
---

# [[SET: Platform name]] — Multi-Role Design System

## 1. Product context

- **What the platform does:** [[SET]]
- **Roles:** [[SET: list]]
- **Does one person hold several roles?** [[SET]] — if yes, cross-role consistency is critical
  and role identity must be unmissable
- **Multi-tenant:** [[SET]]
- **Impersonation / support access:** [[SET]]
- **Highest-consequence action on the platform:** [[SET]]

## 2. Roles

Summary only. Complete [ROLE-EXPERIENCE-MAP.md](ROLE-EXPERIENCE-MAP.md) for the detail.

| Role | Layer | Expertise | Frequency | Data scope | Can affect others | Density |
|---|---|---|---|---|---|---|
| [[SET]] | [[customer/operator/admin]] | [[SET]] | [[SET]] | [[own/team/org/platform]] | [[yes/no]] | [[SET]] |

## 3. Experience principles

1. **One product, several densities.** A user moving between roles must recognise the system.
2. **Status means the same thing everywhere.** No exceptions.
3. **[[SET: your third, and what it rules out]]**

## 4. Shared and varied — the boundary

### Identical for every role

Tokens · type families and scale ratios · radius character · spacing base ·
**status colour meanings** · component behaviour and all eight interaction states ·
form conventions · feedback patterns · destructive-action patterns · accessibility floor ·
terminology for shared objects · keyboard conventions

### Varies by role

Density · navigation pattern and destinations · section rhythm and padding · information density ·
available actions (by permission) · workflow depth · data visibility · default landing view ·
onboarding depth · role-specific terminology (documented below)

## 5. Terminology

Shared objects keep one name platform-wide. Where roles genuinely use different words for their
own concepts, map them explicitly rather than letting a third term appear.

| Concept | Canonical | Customer says | Operator says | Admin says |
|---|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET]] | [[SET]] |

## 6. Navigation per role

| Role | Pattern | Destinations | Default landing view |
|---|---|---|---|
| [[SET]] | [[SET]] | [[SET: count]] | [[SET: answers THIS role's first question of the day]] |

- **Never duplicate destinations across two navigation systems.**
- **Current role and organisation visible at all times**, not only in a menu.
- Role/org switching: [[SET: placement and switch confirmation]]

## 7. Impersonation and elevated context

[[If impersonation does not exist, state that and delete the rest of this section.]]

- **Banner:** `impersonation-banner`, naming the account being viewed, with an exit control.
  **Non-dismissible. Survives navigation.** First element in the accessibility tree, and announced.
- **Administrative context marker:** [[SET: a persistent label or accent bar]] —
  **not a different theme.** A theme switch breaks cross-role recognition and doubles the design
  surface.
- Re-authentication required for: [[SET: list the highest-consequence actions]]
- Actions affecting other people's data state that fact explicitly.

## 8. Permissions

| Situation | Treatment |
|---|---|
| Action not permitted, permission is gettable | **Disabled + explanation**: what permission, who grants it |
| Action irrelevant to the role | Hidden |
| Existence is confidential | Hidden |
| Whole feature unavailable | Empty state explaining access, with a request path |
| Read-only record | Banner at top; visibly non-editable fields |
| Partial permission | Permitted actions active; others disabled with reasons |
| Permission changed mid-session | Notify; never fail silently on the next click |

**Never disable without an explanation.** A greyed-out control with no tooltip generates support
tickets and reads as a bug.

## 9. Workflow, approval, audit

- **Progress:** step N of M, completed steps reviewable, partial progress saved.
- **Approval state machine:** [[SET: the states, from status-vocabulary]]
- Show the **current owner** of each step and **how long** it has been there.
- Rejections require a reason.
- Delegation and reassignment appear in the history.
- **Audit** wherever a role can affect another's data: who, what, when, from where, previous
  value. Per-record, not only a global log. Filterable by actor, action, date.
  **Absolute timestamps with timezone.** Immutable, and visibly so.

## 10. States

All ten: first-run empty · filtered-empty · initial loading · refresh (keep data) · partial data ·
error · **permission denied** · stale data · offline · too many results.

Permission denied is the one specific to this category — specify it per role.

## 11. Novice and expert together

Comfortable defaults, powerful accelerators. **Do not build two interfaces.**

| Accelerator | Present |
|---|---|
| Keyboard shortcuts | [[SET]] |
| Command palette | [[SET]] |
| Saved views | [[SET]] |
| Density toggle | [[SET]] |
| Bulk operations | [[SET]] |
| Expert form path alongside a guided path | [[SET]] |

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav | Drawer | Drawer / rail | Full |
| Role + org context | Visible in top bar | Visible | Visible |
| Impersonation banner | **Always visible** | Always | Always |
| Tables | Transform to cards | Scroll + pinned column | Full |
| Bulk actions | Deferred | Available | Available |
| Multi-step forms | One step per screen | One step per screen | Steps or single form |
| Density | Comfortable forced | Standard | Per layer |

- **Customer layer: full parity required.**
- **Operator and admin layers: parity not expected.** Unavailable capabilities:
  [[SET: list]] — **stated in the interface**, not silently hidden.

## 13. Accessibility commitments

- [ ] Contrast ≥4.5:1 body, ≥3:1 UI, both modes
- [ ] Role and organisation changes announced (live region)
- [ ] Impersonation banner first in the accessibility tree and announced
- [ ] Permission-disabled controls carry `aria-disabled` **and** a reachable explanation
- [ ] Status available as text, never colour alone — critical in dense tables
- [ ] Bulk selection announced: "12 of 340 selected"
- [ ] Table keyboard navigation: arrows, `Home`/`End`, visible focus, no traps
- [ ] Workflow state changes announced
- [ ] Multi-step forms use `aria-current`; errors summarised with links to fields
- [ ] Touch targets ≥44px in every layer, including compact ones

## 14. Do

- Derive every role layer from this one foundation
- Keep status meanings identical everywhere
- Give each role a landing view answering its own first question
- Make role and organisation always visible
- Make impersonation unmistakable and non-dismissible
- Disable-and-explain when the permission is gettable
- Provide audit history wherever roles affect each other
- Save partial progress in every multi-step flow
- Report bulk partial failures per item
- Use absolute timestamps with timezone in records

## 15. Do not

- Do not design role experiences independently
- Do not use a different theme for administrative contexts
- Do not let status colours differ by surface
- Do not show identical dashboards to roles with different jobs
- Do not disable a control without explaining why
- Do not expose administrative complexity to customer roles
- Do not force experts through novice wizards
- Do not hide bulk actions operators use hourly
- Do not claim full mobile parity for operator tooling
- Do not invent a status value outside the vocabulary above

## 16. Implementation notes

- **Token delivery:** [[SET]]
- **Permission model in code:** [[SET: how capability checks are expressed]]
- **Role/org context storage:** [[SET]]
- **Impersonation mechanism:** [[SET: and how the banner is guaranteed to render]]
- **Audit log source:** [[SET]]
- **Shared component library:** [[SET: path — all layers extend these]]

## 17. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/commercial-multi-role-platform.md`, then this file.
This file wins.

**Before generating:** inspect the shared component library, how **other roles'** equivalent
surfaces look, the existing status vocabulary, and how permissions are represented. Report the
canonical status values — **do not invent new ones.**

**While generating:** this surface is a *layer on a shared foundation*, not an independent design.
Vary only what §4 permits. Implement permission communication, all ten states, and the audit
requirements.

**Then report:** what this surface inherits unchanged; what varies and why the role requires it;
confirmation that you used existing status values; how unavailable actions are communicated;
reused vs. created components; assumptions, deviations, invented values, unresolved decisions;
and which capabilities are unavailable on mobile and how that is communicated.

**Review checklist:** `design-intelligence/checklists/commercial-platform-review.md`
