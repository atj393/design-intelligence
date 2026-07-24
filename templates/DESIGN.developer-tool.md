---
# Developer tool / technical platform DESIGN.md
# Copy to project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md. Guide: categories/developer-tools.md

version: 1
name: [[SET: product-name]]-design-system
category: developer-tool
surfaces: [ "[[SET: marketing]]", "[[SET: docs]]", "[[SET: console]]" ]
mode: both        # developers expect a theme choice; absence gets filed as an issue
description: >
  [[SET: What the product does, who uses it, and where it sits in their workflow — beside an
  IDE, in a browser, in CI. That placement decides canvas polarity far more than genre does.
  The corpus splits evenly between dark and light developer tools; there is no default.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  link: { 500: "[[SET: may differ from accent — several sources separate action from link]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]", info: "[[SET]]" }
  env: { test: "[[SET]]", live: "[[SET: must be unmistakably different from test]]" }
  # Syntax token colours — every one must pass contrast in BOTH themes.
  # Comment colours are the usual failure: mid-grey on dark frequently lands near 2:1.
  syntax: { keyword: "[[SET]]", string: "[[SET]]", number: "[[SET]]", comment: "[[SET: verify >=4.5:1]]", function: "[[SET]]", type: "[[SET]]", operator: "[[SET]]" }

semantic:
  light:
    surface-canvas: "#ffffff"
    surface-raised: "{primitives.neutral.50}"
    surface-code: "{primitives.neutral.100}"
    surface-terminal: "{primitives.neutral.950}"   # terminals stay dark in light mode — a legitimate exception
    surface-sunken: "{primitives.neutral.100}"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    text-link: "{primitives.link.500}"
    text-on-terminal: "{primitives.neutral.100}"
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    action-primary: "{primitives.accent.600}"
    focus-ring: "{primitives.accent.500}"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-raised: "{primitives.neutral.900}"
    surface-code: "#000000"
    surface-terminal: "#000000"
    surface-sunken: "#000000"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    text-link: "[[SET: lightened]]"
    text-on-terminal: "{primitives.neutral.100}"
    border-subtle: "rgba(255,255,255,0.08)"
    border-default: "rgba(255,255,255,0.14)"
    action-primary: "{primitives.accent.500}"
    focus-ring: "{primitives.accent.400}"

typography:
  families:
    display: "[[SET]]"
    body: "[[SET]]"
    mono: "[[SET: REQUIRED for this category]]"
  substitutes: { display: "[[SET: if proprietary]]", body: "[[SET]]", mono: "[[SET]]" }
  scale:
    # Three surfaces, three ceilings. See §layout.
    display-1:   { size: 56px, weight: 600, lineHeight: 1.05, tracking: -1.5px }  # marketing only
    page-title:  { size: 36px, weight: 600, lineHeight: 1.15, tracking: -0.8px }  # docs
    heading-1:   { size: 24px, weight: 600, lineHeight: 1.25, tracking: -0.3px }  # console
    heading-2:   { size: 20px, weight: 600, lineHeight: 1.30, tracking: -0.2px }
    heading-3:   { size: 16px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:        { size: 16px, weight: 400, lineHeight: 1.60, tracking: 0 }
    body-dense:  { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }        # console
    caption:     { size: 13px, weight: 400, lineHeight: 1.45, tracking: 0 }
    overline:    { size: 11px, weight: 600, lineHeight: 1.30, tracking: 0.6px, transform: uppercase, family: mono }
    label:       { size: 14px, weight: 500, lineHeight: 1.20, tracking: 0 }
    code:        { size: 14px, weight: 400, lineHeight: 1.55, tracking: 0, family: mono }
    code-inline: { size: 14px, weight: 400, tracking: 0, family: mono }   # ~1-2px below body
    terminal:    { size: 13px, weight: 400, lineHeight: 1.45, tracking: 0, family: mono }
    identifier:  { size: 13px, weight: 400, tracking: 0, family: mono }   # keys, IDs, paths, SHAs

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px, 16: 64px, 20: 80px }
  section: { marketing: 80px, docs: 48px, console: 24px }
  page-padding: { mobile: 20px, tablet: 24px, desktop: 32px }

radius: { none: 0, xs: 3px, sm: 4px, md: 6px, lg: 8px, xl: 12px, full: 9999px }
# Restrained by default — tight geometry reads as engineered and supports density.

layout:
  marketing: { container: 1280px, prose: 680px, max-display: 56px, density: spacious }
  docs:      { container: 1280px, prose: 680px, sidebar: 260px, toc: 220px, max-display: 36px, density: default }
  console:   { container: fluid, prose: 640px, sidebar: 240px, rail: 56px, max-display: 24px, density: compact }
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation: { 0: "none", 1: "1px solid {semantic.border-subtle}", 3: "0 4px 12px rgba(0,0,0,0.10)", 4: "0 12px 32px rgba(0,0,0,0.14)", strategy: border-first }

motion: { instant: 100ms, fast: 150ms, base: 200ms, reduced-motion: "instant, state preserved" }

components:
  code-block:    { surface: surface-code, padding: 16px, radius: md, type: code, overflow: "horizontal scroll, NEVER wrap", header: "language label + copy button", copy-confirmation: "~2s icon and label swap" }
  code-inline:   { surface: surface-sunken, padding: "2px 5px", radius: xs, type: code-inline }
  terminal:      { surface: surface-terminal, padding: 16px, radius: md, type: terminal, selectable: true, follow: "only while at bottom" }
  log-line:      { type: terminal, timestamp-column: "mono, dimmed, fixed width", severity: "colour + TEXT level" }
  api-key:       { type: identifier, masked-by-default: true, display: "prefix + last 4", copy-without-reveal: true }
  method-badge:  { padding: "2px 6px", radius: xs, type: overline, content: "TEXT + colour, never colour alone" }
  env-indicator: { height: 28px, padding: "4px 10px", radius: full, persistent: true, content: "text label + colour" }
  param-table:   { columns: "name | type | required | description | default", type: body-dense }
  callout:       { padding: 16px, radius: md, border-left: "3px solid <status>", icon: required, label: required }
  language-tabs: { height: 40px, persist-selection: "site-wide" }
  copy-button:   { size: 28px, placement: "top-right of block", confirmation: required }
  error-panel:   { padding: 16px, radius: md, content: "code (mono, copyable) + cause + fix + request ID" }
---

# [[SET: Product name]] — Developer Tool Design System

## 1. Product context

- **What it does:** [[SET]]
- **Who uses it:** [[SET: role, and where in their workflow]]
- **Runs alongside:** [[CHOOSE: an IDE/terminal (favours dark) | a browser (either) | CI (either)]]
- **Surfaces:** [[SET: marketing / docs / console — which exist]]
- **Docs page count:** [[SET]] — above ~200, search becomes primary navigation
- **Secrets or API keys shown:** [[CHOOSE: no | yes]]
- **Environments:** [[SET: e.g. test / live]]
- **Logs or terminal output shown:** [[CHOOSE: no | yes]]

## 2. Experience principles

1. **Precision over polish.** Developers trust measured claims and complete examples.
2. **Every error is diagnosable.** Copyable identifier, cause, fix.
3. **[[SET: your third, and what it rules out]]**

## 3. Visual theme

- **Polarity:** [[SET]] — **justify from environment and brand, not genre.** The corpus splits
  evenly; there is no correct default.
- **Both themes shipped:** [[CHOOSE: yes (recommended) | no — [[SET: why]]]]
- **Decoration budget:** [[CHOOSE: none | minimal]]
- **What carries interest:** [[CHOOSE: code | product screenshots | terminal output | typography]]

## 4. Monospace discipline

**Mono is for:** code (inline and block), terminal output, file paths, API keys, tokens, hashes,
IDs, version numbers, commit SHAs, environment variable names, log lines, aligned numerics.

**Mono is not for:** navigation, buttons, headings, body prose, form labels, marketing copy.

One corpus source sets an entire page in monospace. It is coherent, deliberate, and an exception —
total mono removes the distinction that makes code *read* as code, and reduces reading speed.

**Pairing:** `code-inline` runs 1–2px below body at the same optical weight, because most mono
faces read visually larger at the same nominal size.

## 5. Colour discipline

- One accent for actions; **a separate link colour is legitimate** and several sources use one.
- **Every syntax token colour must pass ≥4.5:1 in both themes.** Comments are the usual failure.
- **`env.test` and `env.live` must be unmistakably different** — plus a text label, because colour
  alone is not enough to prevent a destructive operation against production.
- Method badges (`GET`, `POST`) carry text, not colour alone.
- Log severity carries a text level (`ERROR`, `WARN`), not colour alone.

## 6. Layout per surface

| Surface | Container | Prose | Section | Max display | Body | Density |
|---|---|---|---|---|---|---|
| Marketing | 1280px | 680px | 80px | 56px | 16px | spacious |
| Docs | 1280px + 260/220 rails | 680px | 48px | 36px | 16px | default |
| Console | fluid | 640px | 24px | 24px | 14px | compact |

**One token foundation across all three; vary density.** Docs at marketing density is
unscannable; a console at marketing density is slow.

## 7. Code and terminal

- **Code blocks:** horizontal scroll, never wrap. Language label. Copy button with a **confirmed
  state** (~2s) — an unconfirmed copy button gets pressed repeatedly.
- **Line height 1.5–1.6.** Code needs more leading than prose, not less.
- **Multi-language tabs:** selection persisted **site-wide**.
- **Terminal:** dark surface even in light mode. Real selectable text, never an image or canvas.
  ANSI colours contrast-verified. Wrapping off with a toggle.
- **Log following:** auto-scroll **only while the user is at the bottom**; stop on scroll-up;
  provide a follow toggle. Virtualise; cap retained lines with a visible truncation notice.

## 8. Secrets and environments

- Keys **masked by default**: `[[SET: prefix]]_••••••••[[SET: last4]]`
- Reveal is an explicit, temporary action; re-authenticate for production keys.
- **Copy the full value without revealing it.**
- On creation, show once with an explicit "you will not see this again" warning.
- Metadata: created, last used, scope, environment.
- Rotation is a first-class action; revocation is immediate, confirmed, with impact stated.
- **Never render a secret in log output, even masked.**
- `env-indicator` persistent and visible. Destructive actions in production name the environment.

## 9. API reference

- Endpoint: `method-badge` + path in mono
- `param-table`: name, type, required, description, default
- **Complete, runnable examples with realistic values.** Never `"string"`. Never omit auth headers.
- Error responses enumerated with codes, causes, and fixes
- Rate limits stated; deprecations noted at the endpoint
- Try-it sandbox clearly marked as test

## 10. Error diagnosis

Every error surface provides: identifier (mono, **copyable**), plain-language cause, location
(file/line/request ID/resource), a concrete next step, collapsed stack trace (copyable in full),
a link to surrounding logs, and whether retrying is safe.

**The copyable unique identifier is the highest-value element** — it is what gets pasted into a
search box or a support ticket.

## 11. States

All ten from the foundation, plus: build/deploy in progress · quota exceeded · key revoked ·
version deprecated · sandbox vs. production mismatch.

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Docs sidebar | Drawer | Drawer | 260px |
| Docs TOC | Accordion at top | Hidden | 220px |
| Code blocks | Scroll, 13px | Scroll | Full |
| Language tabs | Select | Tabs | Tabs |
| Console nav | Drawer | Rail | Full |
| Logs | Scroll, 12px | Full | Full |
| API param tables | Definition list | Scroll | Full |
| Try-it panel | Below example | Below | Side-by-side |

Documentation on mobile matters — code blocks must scroll cleanly and copy buttons stay reachable.

## 13. Accessibility commitments

- [ ] Every syntax token ≥4.5:1 in **both** themes
- [ ] Code blocks keyboard-reachable and scrollable; copy buttons named, success announced
- [ ] Diff markers use `+`/`−` characters as well as colour
- [ ] Log severity has a text level
- [ ] Method badges carry text
- [ ] Terminal output is real selectable text
- [ ] Environment indicators are text-labelled
- [ ] Language tab changes announced
- [ ] One `h1`; no skipped levels; skip-to-content link
- [ ] Contrast ≥4.5:1 body, ≥3:1 UI, both themes
- [ ] 200% zoom reflows; code may scroll internally

## 14. Content guidance

- Publish real numbers **with their measurement method**. "Blazing fast" is noise to this audience.
- Name limitations. Implying there are none costs credibility.
- Status page and incident history public.
- Public, clear pricing for self-serve tiers.
- Terminology: [[SET: canonical names for your core objects]]

## 15. Do

- Choose polarity from environment and brand
- Ship both themes
- Reserve mono for code and identifiers
- Scroll code horizontally
- Confirm every copy action
- Persist language-tab selection site-wide
- Mask secrets; allow copy without reveal
- Keep environment context persistent and unmistakable
- Give every error a copyable identifier and a next step
- Show complete, runnable examples

## 16. Do not

- Do not set interface text in monospace
- Do not wrap code blocks
- Do not ship syntax colours that fail contrast
- Do not reveal secrets by default or log them
- Do not let test and live look alike
- Do not use `"string"` placeholder values
- Do not omit auth from example requests
- Do not use marketing superlatives instead of measured claims
- Do not auto-scroll a log the user has scrolled away from
- Do not inherit marketing density into docs or console
- Do not render terminal output as an image

## 17. Implementation notes

- **Token delivery:** [[SET]]
- **Syntax highlighting:** [[SET: library + theme, and where token contrast was verified]]
- **Docs platform:** [[SET]]
- **Log streaming:** [[SET: transport + virtualisation]]
- **Secret handling:** [[SET: masking and copy-without-reveal implementation]]
- **Existing components to reuse:** [[SET]]

## 18. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/developer-tools.md`, then this file. This file wins.

**Before generating:** inspect existing code-block, terminal, callout, and table components; the
syntax-highlighting setup; how environments are indicated; how secrets are handled. Report
findings.

**While generating:** mono only where §4 permits; horizontal code scroll; confirmed copy buttons;
verified syntax contrast; masked secrets; persistent environment indicator; copyable error
identifiers.

**Then report:** assumptions, deviations, invented values, unresolved decisions, reused vs. created
components, **and the computed contrast ratio for every syntax token you introduced, in both
themes**.
