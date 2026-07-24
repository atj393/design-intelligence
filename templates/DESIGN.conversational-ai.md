---
# Conversational AI / assistant DESIGN.md
# Copy to your project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends design-intelligence/templates/DESIGN.foundation.md — the token architecture,
# scales, and accessibility floor there apply here in full.
# Category guide: design-intelligence/categories/conversational-ai.md
#   NOTE: that guide's evidence is predominantly SYNTHESIZED. Validate with users early.

version: 1
name: [[SET: product-name]]-design-system
category: conversational-ai
form: [[CHOOSE: full-page | side-panel | floating | persistent-bar | task-copilot]]
density: default
mode: [[CHOOSE: inherit-from-host | light | dark | both]]
description: >
  [[SET: What the assistant does, who uses it, and whether conversation is the product or a
  feature of something else. If it is a feature, name the host application — this assistant
  inherits the host's tokens, density, and canvas polarity.]]

# If form is side-panel, floating, persistent-bar, or task-copilot, DELETE the primitives
# and semantic blocks below and reference the host application's tokens instead.
# An embedded assistant with its own visual identity reads as bolted on.

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]", info: "[[SET]]" }

semantic:
  light:
    surface-canvas: "{primitives.neutral.50}"
    surface-user-turn: "{primitives.neutral.100}"      # user turn tint
    surface-code: "{primitives.neutral.100}"            # code block well
    surface-composer: "#ffffff"
    surface-raised: "#ffffff"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    border-composer: "{primitives.neutral.300}"
    border-subtle: "{primitives.neutral.200}"
    action-primary: "{primitives.accent.600}"
    citation-marker: "{primitives.accent.600}"
    focus-ring: "{primitives.accent.500}"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-user-turn: "{primitives.neutral.900}"
    surface-code: "#000000"
    surface-composer: "{primitives.neutral.900}"
    surface-raised: "{primitives.neutral.900}"
    text-primary: "[[SET: not #ffffff — avoids halation]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    border-composer: "rgba(255,255,255,0.14)"
    border-subtle: "rgba(255,255,255,0.08)"
    action-primary: "{primitives.accent.500}"
    citation-marker: "{primitives.accent.400}"
    focus-ring: "{primitives.accent.400}"

typography:
  families:
    body: "[[SET: family, system-ui, sans-serif]]"
    mono: "[[SET: family, ui-monospace, monospace]]"
  substitutes: { body: "[[SET: if proprietary]]" }
  scale:
    # Note the low ceiling. This is an application surface, not a marketing page.
    heading-1: { size: 24px, weight: 600, lineHeight: 1.25, tracking: -0.3px }
    heading-2: { size: 20px, weight: 600, lineHeight: 1.30, tracking: -0.2px }
    heading-3: { size: 17px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:      { size: 16px, weight: 400, lineHeight: 1.55, tracking: 0 }   # message text
    body-sm:   { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }
    caption:   { size: 12px, weight: 400, lineHeight: 1.40, tracking: 0.1px }
    label:     { size: 14px, weight: 500, lineHeight: 1.20, tracking: 0 }
    code:      { size: 14px, weight: 400, lineHeight: 1.55, tracking: 0, family: mono }
    citation:  { size: 11px, weight: 500, lineHeight: 1.0, tracking: 0 }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px }
  turn-gap: 24px          # between speaker turns
  within-turn-gap: 12px   # between blocks inside one turn

radius: { none: 0, xs: 4px, sm: 6px, md: 8px, lg: 12px, xl: 16px, full: 9999px }

layout:
  message-column: 720px         # 680-760px. Assistant output is prose; it obeys a measure.
  conversation-sidebar: 280px
  panel-width: 400px            # side-panel form
  floating-panel: { width: 400px, height: "min(600px, 80vh)" }
  launcher: 56px
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px }

motion:
  instant: 100ms
  fast: 150ms
  base: 250ms
  streaming: "NO animation. Content appends without transition."
  reduced-motion: "no typing animation, no auto-scroll animation"

components:
  composer:
    min-height: 56px
    max-height: 200px
    padding: "12px 16px"
    radius: lg
    surface: surface-composer
    border: border-composer
    send-button: 32px
  user-turn:
    surface: surface-user-turn
    padding: "12px 16px"
    radius: lg
    max-width: "80%"
    align: "[[CHOOSE: right | left-with-tint]]"
  assistant-turn:
    surface: transparent      # NO bubble. Plain container, document-like.
    padding: 0
    max-width: "100%"
    label: "24px avatar or text label at turn start"
  code-block:
    surface: surface-code
    padding: 16px
    radius: md
    type: code
    overflow: "horizontal scroll, never wrap"
    header: "language label + copy button"
  citation-marker: { type: citation, color: citation-marker, min-target: 24px }
  context-chip: { height: 32px, padding: "6px 10px", radius: full, removable: true }
  attachment-chip: { height: 36px, padding: "8px 12px", radius: md, removable: true }
  tool-call-row: { height: 32px, padding: "6px 12px", type: body-sm, collapsible: true }
  suggested-prompt: { padding: "12px 16px", radius: md, border: border-subtle, type: body-sm }
---

# [[SET: Product name]] — Conversational Interface Design System

## 1. Product context

- **Is conversation the product or a feature?** [[CHOOSE: the product | a feature of [[SET: host]]]]
- **Why conversation rather than a form:** [[SET: the request must be open-ended, exploratory,
  or unstructured. If it could be 8 form fields, say so here and reconsider.]]
- **Capability:** [[SET: what the assistant can actually do]]
- **Context it can access:** [[SET: documents, records, selection, workspace]]
- **Tools it can call:** [[SET: search, retrieval, actions, code execution]]
- **Produces structured output:** [[CHOOSE: no | yes — [[SET: shape, and which host component
  receives it]]]]
- **Multi-conversation history:** [[CHOOSE: yes | no]]
- **Model/mode selection exposed:** [[CHOOSE: no | yes]]
- **Citations required:** [[CHOOSE: no | yes]]

## 2. Users

| Attribute | Value |
|---|---|
| Expertise | [[SET]] |
| Frequency | [[SET]] |
| Session length | [[SET]] |
| Device split | [[SET]] |
| Tolerance for latency | [[SET]] |

## 3. Experience principles

1. **The user's words are never lost.** Input survives error, navigation, reload, and timeout.
2. **The user is always in control of generation.** Stop is available throughout.
3. **[[SET: your third principle, and what it rules out]]**

## 4. Visual theme

- **Polarity:** [[SET: if embedded, this is the host's — state which]]
- **Assistant output is a document, not a message.** Plain container, full column width,
  full Markdown structure.
- **User input is an utterance.** Tinted or bubbled, max 80% width.
- **The asymmetry is deliberate** and is the primary speaker-distinction channel.

## 5. Colour discipline

- One accent, on `action-primary`, `citation-marker`, and `focus-ring`.
- Speaker distinction uses **two** channels minimum (label + surface tint, or label + gutter
  marker). Never colour alone. Never alignment alone — it fails at narrow widths.
- `status-danger` for errors and rate limits only.

## 6. Layout

- Message column `{layout.message-column}`. **Full-width responses are genuinely harder to read.**
- `{spacing.turn-gap}` between turns, `{spacing.within-turn-gap}` within a turn.
- Composer matches the message column width.
- [[SET: sidebar / panel behaviour for your form]]

## 7. Composer specification

| Property | Value |
|---|---|
| Placeholder | [[SET: concrete and short — "Ask about your invoices", not "Type a message…"]] |
| `Enter` | Send |
| `Shift+Enter` | Newline |
| `Cmd/Ctrl+Enter` | Send (always works) |
| `Esc` | Stop generation; else blur |
| `↑` on empty | Recall previous message for editing |
| Configurable send key | [[CHOOSE: yes (recommended) | no]] |
| Draft persistence | Across navigation, reload, and error — **required** |
| Clear timing | **After** send is accepted, never before |

## 8. Generation states

| State | Treatment |
|---|---|
| Submitted | User turn appears **immediately**, before any server response |
| Thinking | Indicator within 100ms, distinct from streaming |
| Tool use | [[SET: named operations, e.g. "Searching invoices…"]] — never a generic spinner |
| Streaming | Send button becomes **Stop**, same position and size |
| Complete | Actions in a **reserved** row: copy, regenerate, edit, feedback |
| Stopped | Partial output kept and labelled; continue offered |
| Error | User's message **kept**; explanation; retry |
| Rate-limited | [[SET: state the limit and when it lifts]] |
| Offline | Disable with explanation; preserve draft |

### Layout stability during streaming — required

- Turn container reserved before content arrives
- **No height transition** on chunk arrival
- Incremental Markdown buffered to safe boundaries (an unclosed code fence must not reflow the
  block)
- **No per-character animation**
- Auto-scroll only while the user is at the bottom; stop on scroll-up; show "jump to latest"

## 9. Content rendering

| Content | Treatment |
|---|---|
| Markdown | Full: headings, lists, tables, code |
| Code | `code-block` component; horizontal scroll; language label; copy with confirmation |
| Tables | Real tables, scrollable in a bounded container |
| Images | Constrained to column width; alt text; click to expand |
| Long output | Rendered fully; jump-to-latest available |
| Artifacts | [[CHOOSE: inline | side panel — [[SET: width]]]] |
| Reasoning summary | Collapsed by default; visually subordinate; **never above the answer** |

## 10. Context, citations, privacy

- **Context chips** naming every document/record/selection in scope. Removable.
- State when context is truncated: [[SET: e.g. "using the first 40 pages"]]
- Citations: inline marker at the claim, hover/focus preview, numbered list below, ≥24px target.
  Say plainly when an answer is unsourced.
- **Retention and visibility stated at the point of use:** [[SET: e.g. "Conversations are
  deleted after 30 days" / "Visible to your workspace admins"]] — not only in a policy link.

## 11. Conversation management

- Titles: auto-generated from the first exchange, user-renameable. Never "New conversation ×14".
- Grouped by recency: Today · Yesterday · Previous 7 days · Older.
- Search across content, not only titles, above ~20 conversations.
- Editing a user turn invalidates everything after it — **say so before doing it**.
- Regeneration: [[CHOOSE: replaces | appends with a version switcher (preserves more user work)]]
- Deletion: confirm, name the target, soft-delete with undo where possible.

## 12. Empty state

- 3–5 **specific** suggested prompts drawn from real capability:
  1. [[SET]]
  2. [[SET]]
  3. [[SET]]
- Suggestions populate the composer (editable), not send immediately.
- **Never "Ask me anything."**
- First-run empty and cleared-history empty are distinct.

## 13. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Sidebar | Drawer | Drawer | 280px visible |
| Message column | Full − 32px | 640px | `{layout.message-column}` |
| Composer | Fixed bottom, safe-area aware | Fixed bottom | In-flow or fixed |
| Floating panel | Full-screen sheet | 400×600 | 400×600 |
| Side panel | Overlay sheet | Overlay | Docked 400px |
| Suggestions | Stack, 2–3 | Wrap | Row of 3–5 |
| Message actions | Visible or long-press — **no hover-only** | Visible | Hover or visible |

Keyboard must not cover the composer or the latest message.

## 14. Accessibility commitments

- [ ] `aria-live="polite"` on the response region. **Announce start and completion only —
      never every token.** Per-token announcement makes the interface unusable with a screen
      reader.
- [ ] Focus stays in the composer; never stolen by an arriving message
- [ ] Each turn is a landmark or list item with an accessible speaker label
- [ ] Stop control keyboard-reachable throughout; `Esc` bound
- [ ] Speaker identity available as text, not by colour or position alone
- [ ] Code blocks reachable and scrollable; copy buttons named and announcing success
- [ ] Citations are real links/buttons with accessible names
- [ ] Message actions ≥44px on touch
- [ ] No typing animation under `prefers-reduced-motion`
- [ ] Heading structure inside long responses so users can navigate within them
- [ ] Contrast ≥4.5:1 body, ≥3:1 UI, in both modes

## 15. Content guidance

- Error text: what happened + what to do next. Never "Something went wrong".
- Rate limits: state the limit and the reset time.
- Capability limits stated briefly in the empty state, not buried.
- Tool-call labels in the user's vocabulary, not internal names.

## 16. Do

- Show the user's message immediately
- Constrain the message column to a readable measure
- Give assistant output document structure
- Reserve layout space before streaming
- Keep the stop control in a stable position
- Preserve partial output when stopped or errored
- Persist the composer draft always
- Name what tools are doing
- Show removable context chips
- Suggest specific, capability-accurate prompts
- Inherit the host's tokens and density when embedded

## 17. Do not

- Do not bubble long assistant responses
- Do not treat user and assistant turns identically
- Do not auto-scroll away from a user who scrolled up
- Do not animate height per chunk, or animate characters
- Do not discard the user's message on error
- Do not clear the composer before send is accepted
- Do not hide tool failures behind a confident answer
- Do not show reasoning above the answer or expanded by default
- Do not use "Ask me anything"
- Do not auto-expand a floating assistant unprompted
- Do not let the launcher cover primary actions or bottom navigation
- Do not announce every token
- Do not build a chat where a form serves better
- Do not give an embedded assistant its own visual identity

## 18. Implementation notes

- **Streaming transport:** [[SET: SSE / WebSocket / polling]]
- **Markdown renderer:** [[SET: library, and how incremental parsing is handled safely]]
- **Syntax highlighting:** [[SET: library — verify every token colour passes contrast]]
- **Draft persistence:** [[SET: localStorage / server]]
- **Host components to reuse:** [[SET: list]]

## 19. Agent prompt guidance

Read `design-intelligence/COMMON-FOUNDATION.md`, then
`design-intelligence/categories/conversational-ai.md`, then this file. This file wins.

**Before generating:** inspect the codebase — existing message list, Markdown renderer, code
block, panel, toast components; the host's tokens and density; streaming infrastructure; focus
and live-region conventions. Report what you found.

**While generating:** reference semantic tokens by name. Implement every generation state in §8.
Implement the layout-stability requirements — they are the failure mode that matters most.

**Confirm explicitly in your report:**
1. Input is never lost on error
2. Layout does not shift during streaming
3. A stop control is available throughout generation
4. Screen readers are not announced per token

**Then report:** assumptions, deviations, invented values, unresolved decisions, components
reused vs. created.

**Review checklist:** `design-intelligence/checklists/conversational-ai-review.md`
