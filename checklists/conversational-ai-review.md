# Conversational AI Review Checklist

Run [foundation-review.md](foundation-review.md) first.

Reference: [../categories/conversational-ai.md](../categories/conversational-ai.md) —
**evidence is predominantly synthesized; validate with real users too.**

---

## 1. Is this the right shape?

- [ ] Conversation is genuinely the right interface — the request is open-ended, exploratory, or
      unstructured
- [ ] The task could **not** be served better by a form of fewer than ~8 fields
- [ ] If conversation is a feature rather than the product, it occupies a panel or bar, not the
      whole viewport
- [ ] AI capability that suits inline suggestion, selection action, or a generated field is not
      forced into a chat

## 2. Message presentation

- [ ] Message column is 680–760px, not full width
- [ ] Assistant turns are **not** in bubbles — plain container, full column width
- [ ] User and assistant turns are visibly asymmetric
- [ ] Speakers distinguished by **at least two** channels (label + tint, or label + gutter)
- [ ] Not distinguished by colour alone, nor by alignment alone
- [ ] 24px between turns, 12px within a turn
- [ ] Consecutive same-speaker turns share one label
- [ ] Timestamps are not on every message
- [ ] Full Markdown renders: headings, lists, tables, code

## 3. Composer

- [ ] Min 56px, auto-grows, scrolls internally beyond ~200px
- [ ] `Enter` sends; `Shift+Enter` newlines; `Cmd/Ctrl+Enter` always sends
- [ ] `Esc` stops generation
- [ ] `↑` on empty recalls the previous message
- [ ] Send becomes **Stop** during streaming, in the **same position and size**
- [ ] Placeholder is concrete, not "Type a message…"
- [ ] **Draft persists** across navigation, reload, and error
- [ ] Input clears only **after** send is accepted
- [ ] Over-length shows the limit and current count; does not silently truncate
- [ ] Rate-limited state explains the limit and when it lifts

## 4. Generation states

- [ ] User message appears **immediately** on send, before any server response
- [ ] Thinking indicator within 100ms, distinct from streaming
- [ ] Tool activity is **named** ("Searching invoices…"), not a generic spinner
- [ ] Tool **failures are visible** — not hidden behind a confident answer
- [ ] Stop control available throughout generation
- [ ] Stopped: partial output kept and labelled; continue offered
- [ ] Error: **user's message kept**, explanation given, retry offered
- [ ] Complete: copy, regenerate, edit, feedback appear in a **reserved** row

## 5. Layout stability — the critical section

- [ ] Turn container reserved before content arrives
- [ ] **No height transition** on chunk arrival
- [ ] Incremental Markdown buffered — an unclosed code fence does not reflow the block
- [ ] **No per-character animation**
- [ ] Action row space reserved so buttons do not shift content on appearing
- [ ] Auto-scroll follows **only** while the user is at the bottom
- [ ] Stops following the moment the user scrolls up
- [ ] "Jump to latest" affordance appears when not at the bottom

## 6. Content rendering

- [ ] Code blocks: dedicated surface, mono, language label, copy button with confirmation
- [ ] Code scrolls horizontally, never wraps
- [ ] Tables are real tables, scrollable in a bounded container
- [ ] Images constrained to column width with `alt` text
- [ ] Long responses render fully — not truncated mid-thought
- [ ] Structured output goes into host UI components, not a bubble the user must retype from

## 7. Context and provenance

- [ ] What is in context is **visible** as chips
- [ ] Context chips are removable
- [ ] Truncated context is stated ("using the first 40 pages")
- [ ] Nothing is silently included that the user would not expect
- [ ] Citations: inline marker at the claim, hover **and focus** preview, numbered list below
- [ ] Citation targets ≥24px (≥44px on touch)
- [ ] Unavailable sources are marked, not rendered as live links
- [ ] Unsourced answers say so plainly
- [ ] Retention and visibility stated at the point of use, not only in a policy link

## 8. Attachments

- [ ] Drop zone with a visible drag-over state
- [ ] Chips show type, filename, size, and a remove control
- [ ] Filenames truncate in the **middle**, preserving the extension
- [ ] Per-file upload progress; send blocked until resolved
- [ ] Per-file errors with reasons
- [ ] Limits stated **before** the user tries

## 9. Conversation management

- [ ] Titles are meaningful, auto-generated, and renameable
- [ ] History grouped by recency
- [ ] Search covers content, not only titles (above ~20 conversations)
- [ ] Editing a user turn warns that everything after it is invalidated
- [ ] Regeneration behaviour is consistent (replace or append — pick one)
- [ ] Branching, if present, shows structure and allows sibling switching
- [ ] Deletion confirms, names the target, and offers undo where possible
- [ ] Model/mode selection is near the composer, labelled by outcome, always visible

## 10. Empty state

- [ ] 3–5 **specific** suggested prompts drawn from real capability
- [ ] **Not** "Ask me anything"
- [ ] Suggestions populate the composer (editable) rather than sending immediately
- [ ] First-run empty is distinct from cleared-history empty
- [ ] Capability limits stated briefly

## 11. Embedded forms

- [ ] Inherits the host's tokens, density, and canvas polarity
- [ ] Does **not** carry its own visual identity
- [ ] Panel is resizable and collapsible, with state remembered
- [ ] Floating launcher does not cover primary actions or bottom navigation
- [ ] Launcher does not auto-expand unprompted
- [ ] Below 1024px, the panel becomes an overlay or sheet, not a squeezed column

## 12. Accessibility

- [ ] `aria-live="polite"` on the response region
- [ ] **Start and completion announced — not every token.** Per-token announcement makes the
      interface unusable with a screen reader
- [ ] Focus is **not stolen** by an arriving message; stays in the composer
- [ ] Each turn is a landmark or list item with an accessible speaker label
- [ ] Speaker identity available as text, not by colour or position alone
- [ ] Stop control keyboard-reachable throughout; `Esc` bound
- [ ] Code blocks reachable and scrollable; copy buttons named, success announced
- [ ] Citations are real links or buttons with accessible names
- [ ] Message actions ≥44px on touch; no hover-only affordances
- [ ] Long responses have heading structure so users can navigate within them
- [ ] No typing animation or animated auto-scroll under `prefers-reduced-motion`

## 13. Mobile

- [ ] Composer sits above the safe-area inset
- [ ] On-screen keyboard does not cover the composer or the latest message
- [ ] Message actions visible or long-press — never hover-only
- [ ] Suggested prompts stack to 2–3
- [ ] Code blocks scroll cleanly with copy buttons reachable

## 14. The four confirmations

Confirm these explicitly before sign-off. Each is a known high-frequency failure:

1. [ ] **Input is never lost on error.**
2. [ ] **Layout does not shift during streaming.**
3. [ ] **A stop control is available throughout generation.**
4. [ ] **Screen readers are not announced per token.**
