# Conversational AI and Assistant Interfaces

> **Evidence strength: very weak / predominantly synthesized.**
> The source corpus contains **no documented conversational interface**. Its strongest
> contribution is a single component — a persistent chat bar in
> `design-md/tesla/DESIGN.md`. Two sources document the *marketing sites* of conversational
> products (`design-md/claude/`, `design-md/intercom/`), which tells you how such companies
> present themselves and nothing about how their chat UI works.
> Everything below is general interface reasoning, stated with its rationale so you can
> disagree with the argument rather than just the conclusion. **Validate with real users
> earlier than you would for a corpus-backed category.**

---

## 1. The first decision: is conversation the product or a feature?

Get this wrong and everything downstream is wrong.

| | Conversation is the product | Conversation is a feature |
|---|---|---|
| User's mental model | "I am talking to something" | "I am doing my work, with help" |
| Layout | Conversation owns the viewport | Conversation occupies a panel or bar |
| History | First-class, navigable, persistent | Often ephemeral or scoped to context |
| Success measure | Quality of the exchange | Task completed in the host application |
| Failure mode if wrong | — | A chat box bolted onto a product that needed a better form |

**A chat interface is a poor substitute for a good form.** If the user knows exactly what
they want and the system needs five specific values, a form collects them faster, validates
them better, and does not hallucinate. Conversation earns its place when the request is
**open-ended, exploratory, or unstructured** — when the user cannot articulate the request as
fields.

Ask before committing:

1. Can the user's intent be expressed as a form with fewer than ~8 fields? → Build the form.
2. Does the user need to iterate on the output? → Conversation helps.
3. Is the input genuinely unstructured (prose, a document, a vague goal)? → Conversation helps.
4. Does the user need to see many results at once and compare them? → Conversation hurts.
   Chat is a linear, single-threaded medium.

**Not every AI feature should look like a chat.** Better shapes for AI capability, in rough
order of how often they are the right answer:

| Shape | Use when | Example |
|---|---|---|
| **Inline suggestion** | The user is already in the right place | Autocomplete, next-line suggestion |
| **Selection action** | The AI acts on something the user picked | "Summarise this", "Rewrite selection" |
| **Generated field** | One value needs producing | "Draft a description" button beside a field |
| **Structured output panel** | The result has known shape | Extracted entities in a form-shaped panel |
| **Command palette entry** | Expert users, keyboard-first | Natural-language command in the palette |
| **Background agent** | Long work with a reviewable result | "Analysing 400 records — notify me" |
| **Conversation** | Genuinely open-ended, iterative dialogue | Research, drafting, debugging |

## 2. Product forms

### 2a. Full-page chat application

Conversation is the product. Layout: conversation-list sidebar + message column +
composer.

| Element | Default | Compact | Spacious |
|---|---|---|---|
| Conversation sidebar | 280px | 240px | 320px |
| Message column max-width | 720px | 640px | 760px |
| Composer max-width | matches message column | — | — |
| Message vertical gap (between turns) | 24px | 16px | 32px |
| Message vertical gap (within a turn) | 12px | 8px | 16px |
| Composer min-height | 56px | 48px | 64px |
| Composer max-height before scroll | 200px (~8 lines) | 160px | 240px |

**Message column max-width is the most consequential number here.** Assistant responses are
prose. Prose obeys the 60–75 character measure like all other prose — a 1400px-wide response
is genuinely harder to read, and the width is why long AI answers feel exhausting. 680–760px
at 16px body is the target.

> **Unresolved tension, flagged rather than papered over** (see
> [research/WEAK-GUIDE-REVIEW.md](../research/WEAK-GUIDE-REVIEW.md) A-02). Prose wants 680px.
> **Code blocks and wide tables want 900px+.** A single column width cannot serve both, and an
> earlier draft of this guide did not admit that.
>
> Three workable resolutions, in order of preference:
>
> 1. **Let structured blocks break out.** Prose stays at 680px; code blocks, tables, and images
>    are allowed to extend to ~900px (or the panel width) while staying left-aligned to the
>    prose. Best of both, slightly more layout work.
> 2. **Widen the column to 820px** and accept a measure at the upper end of comfortable. Simplest;
>    reasonable when code appears in most responses.
> 3. **Move long code and generated artifacts to a side panel.** Best when the output is the
>    deliverable rather than part of the conversation.
>
> Do not simply widen to 1200px to fit code. That fixes code and breaks every prose answer.

### 2b. Side-panel assistant

Docked panel inside a host application. Panel width 360–480px; 400px default.

- **Inherit the host's density, polarity, and tokens.** An assistant panel that looks like a
  different product inside your application is the most common failure of this form.
- Panel is resizable and collapsible; remember the state per user.
- Below 1024px the panel becomes an overlay or sheet, not a squeezed column.
- Message column is the panel width minus padding — measure constraints still apply, and at
  400px you are at the *narrow* end, so avoid additional inset.

### 2c. Floating assistant / launcher

Launcher button plus expanding surface.

| Element | Value |
|---|---|
| Launcher size | 56px (44px minimum) |
| Launcher position | 24px from viewport edges; respect safe-area insets |
| Expanded panel | 400×600px desktop, full-screen sheet below 768px |
| Expanded max-height | `min(600px, 80vh)` |
| z-index | Above content, **below** critical system dialogs |

- The launcher must never cover a primary action or persistent controls. Check the mobile
  bottom-right corner specifically — it collides with bottom navigation and floating action
  buttons.
- Unread or proactive states need a badge, but proactive messages that auto-expand are an
  interruption. Default to a badge; expand only on explicit user action.

### 2d. Persistent bar

A single always-visible input, usually at the bottom or in the header. This is the corpus's
one observed pattern (`design-md/tesla/DESIGN.md`).

| Element | Value |
|---|---|
| Bar height | 56–64px |
| Position | Fixed bottom, or integrated into the top bar |
| Behaviour on submit | Expands into a panel, or navigates to a conversation view |

Good when the assistant is a **shortcut into the product** rather than a workspace. It
signals availability without claiming screen real estate.

### 2e. Document- or context-aware assistant

The assistant reads something the user is looking at.

- **Show what is in context, always.** A chip or list naming the documents, records, or
  selection currently visible to the assistant. Users cannot reason about an answer without
  knowing what produced it.
- Make context removable — a chip with a dismiss affordance.
- When context is truncated ("using the first 40 pages"), say so before the user asks.
- Never silently include something the user did not expect. If the assistant can see the
  whole workspace, say so at the point of use, not in a settings page.

### 2f. Task copilot

Scoped to one workflow, producing structured output.

- Output goes into the host UI's own components — a form, a table, a diff — **not** into a
  message bubble. A bubble containing a table the user then has to retype is a design
  failure.
- Always offer accept / modify / reject. Never auto-apply without a review step for anything
  consequential.
- Show the diff for edits to existing content. "Here is the new version" without a diff makes
  review impossible.

---

## 3. Conversation structure

### Message presentation

**Do not put *long* assistant responses in bubbles.** Bubbles are a messaging idiom sized for
short turns. A 600-word bubble with a 20px radius reads as a mistake, and long bubbles waste
horizontal space to the rounded edges.

> **Qualified after adversarial review** (see
> [research/WEAK-GUIDE-REVIEW.md](../research/WEAK-GUIDE-REVIEW.md) A-01). An earlier draft
> stated this as an absolute, which is wrong for one real case: **short-turn assistants** —
> support bots, booking flows, triage — where responses are one or two sentences and users
> arrive with a messaging mental model. There, bubbling both sides is correct and the
> asymmetric treatment below reads as broken.
>
> **Decide by expected response length, not by product category:**
>
> | Typical assistant response | Treatment |
> |---|---|
> | Under ~40 words, conversational | Bubble both sides. Messaging idiom is right |
> | Mixed, occasionally long | Bubble user; plain container for assistant |
> | Usually long-form, structured, with code or tables | Plain container for assistant |
>
> If you cannot predict length, use the plain container — it degrades gracefully for short
> responses, whereas a bubble degrades badly for long ones.

Recommended asymmetry:

| | User turn | Assistant turn |
|---|---|---|
| Container | Subtle surface tint or right-aligned bubble | **Plain — no container** |
| Radius | 12px if bubbled | n/a |
| Alignment | Right or left-with-tint | Left, full column width |
| Max width | 80% of column | 100% of column |
| Padding | 12px 16px | 0 (rely on vertical rhythm) |

The asymmetry is the point: the user's input is a discrete utterance; the assistant's output
is a document. Treating them identically serves neither.

**Distinguishing turns without bubbles** — use at least two channels:

1. A small persistent label or avatar (24px) at the turn start
2. Surface tint on user turns only
3. Vertical rhythm — 24px between turns, 12px within
4. Optionally a left border or gutter marker on assistant turns

Never rely on colour alone. Never rely on alignment alone — it fails at narrow widths.

### Message grouping

- Consecutive turns from the same participant share one label; do not repeat the avatar.
- Timestamps: only on hover, on group boundaries, or after a time gap. A timestamp on every
  message is noise.
- Insert a divider on a significant time gap ("Yesterday") — it helps users re-orient in long
  histories.

### Long responses

| Problem | Treatment |
|---|---|
| Very long response | Render fully; do not truncate mid-thought. Offer a jump-to-latest control |
| Structured content | Full Markdown rendering — headings, lists, tables, code |
| Tables | Real `<table>`, horizontally scrollable in a bounded container |
| Code | Dedicated surface, monospace, language label, copy button, syntax highlighting |
| Generated artifacts | Consider a side-by-side artifact panel rather than inline |
| Images | Constrained to column width, click to expand, `alt` text always |
| Math / diagrams | Render them; do not show raw source |

**Auto-scroll rule.** Follow the stream *only while the user is already at the bottom*. The
moment they scroll up, stop following and show a "jump to latest" affordance. Yanking a
reading user back to the bottom is among the most disliked behaviours in this category.

---

## 4. The composer

The single most-used control in the product. Specify it exhaustively.

| Property | Value |
|---|---|
| Min height | 56px (single line + padding) |
| Max height | ~200px, then internal scroll |
| Growth | Auto-expand with content |
| Padding | 12px 16px, plus right inset for the send button |
| Radius | 12px, or `full` at single-line height only |
| Border | 1px `border-default`; `focus-ring` on focus |
| Placeholder | Concrete and short. "Ask about your invoices" beats "Type a message…" |
| Send button | 32–40px, inside the composer, right-aligned |
| Character/token counter | Only when a limit is near — not always visible |

**Keyboard behaviour** — non-negotiable and frequently wrong:

| Key | Action |
|---|---|
| `Enter` | Send |
| `Shift+Enter` | Newline |
| `Esc` | Stop generation if streaming; else blur |
| `↑` (empty composer) | Recall previous message for editing |
| `Cmd/Ctrl+Enter` | Send — always works, even where `Enter` is configured as newline |

Let users configure `Enter` versus `Cmd+Enter`. Both conventions have strong constituencies
and getting it wrong loses drafts.

**States:**

| State | Treatment |
|---|---|
| Empty | Placeholder; send disabled |
| Typing | Send enabled |
| Sending | Brief disable; clear input **only after** the send is accepted |
| Streaming | Send becomes **Stop**. Same position, same size |
| Rate-limited | Explain the limit and when it lifts. Never a bare "error" |
| Over length | Show the limit and the current count; do not silently truncate |
| Offline | Disable with an explanation; preserve the draft |
| Attachment pending | Show upload progress; block send until resolved or removed |

**Never lose a draft.** Persist composer content across navigation, reload, and error. This
is the cheapest trust-building behaviour available in this category.

---

## 5. Generation states

The category's defining interaction problem, and the corpus offers nothing here.

### State sequence

```
idle → submitted → thinking → [tool use] → streaming → complete
                                    ↓
                              stopped | error | rate-limited
```

| State | Requirement |
|---|---|
| **Submitted** | User turn appears **immediately**. Never wait for the server to show it |
| **Thinking** | Indicator within 100ms. Distinct from streaming |
| **Tool use** | Name what is happening: "Searching invoices…" not a generic spinner |
| **Streaming** | Token-by-token or chunked. Stop control available throughout |
| **Complete** | Actions appear: copy, regenerate, edit, feedback |
| **Stopped** | Keep partial output. Label it as stopped. Offer continue |
| **Error** | Keep the user's message. Explain. Offer retry. **Never discard input** |

### Layout stability during streaming

**The most damaging failure mode in this category.** Content appended token by token causes
reflow, and reflow while the user is reading is disorienting.

- Reserve the turn container before content arrives.
- Never animate height on each chunk. Let content grow; do not transition it.
- Render Markdown incrementally but stably — an unclosed code fence must not flip the whole
  block's layout each chunk. Buffer to a safe boundary.
- Keep action buttons in a reserved row so they do not shift content on appearing.
- Do not animate individual characters. It looks expensive and reads worse.

### Reasoning summaries

If the product exposes intermediate reasoning:

- **Collapsed by default.** It is supporting evidence, not the answer.
- Visually subordinate — smaller, lower contrast, distinct surface.
- Labelled honestly. If it is a summary rather than the literal process, do not imply
  otherwise.
- Never place it above the answer. Users want the answer.

### Tool calls

- Show tool activity as a compact, labelled row: icon, action, target, status.
- Collapse completed calls to one line; expand on demand.
- **Show failures.** A silently failed retrieval that produces a confident answer is a
  correctness problem the interface is hiding.
- Group repeated calls: "Searched 4 sources" rather than four rows.

---

## 6. Citations and provenance

Where the interface most directly affects whether users are misled.

| Requirement | Treatment |
|---|---|
| Inline markers | Numbered superscript or a small chip at the claim, not only at the end |
| Hover/focus preview | Source title, snippet, and location |
| Full list | Below the response, numbered to match inline markers |
| Click target | ≥24px; ≥44px on touch |
| Unavailable source | Say so; never render a dead citation as live |
| Uncertainty | Surface the model's stated uncertainty rather than flattening it |
| No sources | State plainly that the answer is unsourced |

Citation markers must be **visually quiet but reachable**. Superscript at `caption` size in
`text-link` colour, with a real focus state, is enough.

## 7. Attachments

| Element | Value |
|---|---|
| Drop zone | The whole composer, with a visible drag-over state |
| Chip size | 32–40px tall, in a row above the input |
| Chip content | Type icon, filename (truncate middle, not end — extensions matter), size, remove |
| Image preview | 48–64px thumbnail |
| Upload progress | Per-file; block send until resolved |
| Errors | Per-file, with the reason: too large, wrong type, failed |
| Limits | State them *before* the user tries — "up to 5 files, 20MB each" |

Truncate long filenames in the middle: `quarterly-report-…-final.pdf`. Truncating the end
hides the extension, which is often the most informative part.

---

## 8. Conversation management

### History and navigation

- **Titles must be meaningful.** Auto-generate from the first exchange, and let users rename.
  "New conversation ×14" is a broken history.
- Group by recency: Today · Yesterday · Previous 7 days · Older.
- Search across conversation content, not just titles, once a user has more than ~20.
- Pin or favourite for long-running work.
- Deletion is destructive: confirm, name the target, and prefer soft-delete with undo.

### Editing and branching

- Editing a user turn **invalidates everything after it.** Say so before doing it.
- Branching is powerful and confusing. If you support it, show the branch structure and let
  users switch between siblings ("2 / 3"). If you cannot show it clearly, prefer edit-and-
  replace with a warning.
- Regeneration replaces or appends — pick one and be consistent. Appending with a
  version switcher preserves more user work.

### Model and mode selection

- Put it near the composer, not in a settings page — it is a per-message decision.
- Label by *outcome*, not by internal name: "Faster" / "More thorough", with the technical
  name available on hover for users who want it.
- Show the current selection at all times. Mode is state, and hidden state causes confusion
  about why answers changed.
- Changing mode mid-conversation needs a visible marker in the thread.

### Empty and onboarding states

The empty state is the product's most important teaching surface.

- 3–5 **specific** suggested prompts, drawn from real capability. "Summarise my Q3 pipeline"
  teaches; "Ask me anything" does not.
- Suggestions must be tappable and must populate the composer (editable) rather than sending
  immediately.
- State capability limits plainly and briefly.
- If the assistant needs context to be useful, ask for it here rather than failing later.
- Distinguish first-run empty from cleared-history empty.

## 9. Privacy and destructive actions

- State at the point of use whether conversations are retained, used for training, or visible
  to an administrator. A privacy policy link is not disclosure at the moment of typing.
- Show retention: "Conversations are deleted after 30 days."
- In multi-tenant or team products, indicate who else can see the conversation.
- Destructive actions — delete conversation, clear all history, revoke context — require
  confirmation naming the target and count, and should offer undo where technically possible.

---

## 10. Accessibility

Additional to the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor). This
category has specific hazards.

| Requirement | Implementation |
|---|---|
| Streaming announcements | `aria-live="polite"` on the response region. Do **not** announce every token — announce start and completion, and let users read |
| Focus on new message | Do not steal focus. Keep it in the composer |
| Turn structure | Each turn a landmark or list item with an accessible label naming the speaker |
| Stop control | Keyboard-reachable at all times during streaming, `Esc` bound |
| Code blocks | Reachable, scrollable, copy button labelled |
| Citations | Real links or buttons with accessible names, not decorative superscripts |
| Speaker identity | Available to screen readers via text, never by colour or position alone |
| Reduced motion | No typing animations, no auto-scroll animation |
| Long output | Skip-link or heading structure so screen-reader users can navigate within a response |

**Announcing every streamed token is the classic failure.** It makes the interface unusable
with a screen reader. Announce "Response started" and "Response complete", and render the
content in a region users can read at their own pace.

## 11. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Conversation sidebar | Drawer | Drawer | Visible 280px |
| Message column | Full width − 32px | 640px | 720px |
| Composer | Fixed bottom, safe-area aware | Fixed bottom | In-flow or fixed |
| Floating panel | Full-screen sheet | 400×600 | 400×600 |
| Side panel | Overlay sheet | Overlay | Docked 400px |
| Suggested prompts | Vertical stack, 2–3 max | Wrap | Row of 3–5 |
| Attachments | Compact chips | Chips | Chips + previews |
| Code blocks | Scroll, smaller font | Scroll | Full |

Mobile specifics:

- Composer sits above the safe-area inset; account for the on-screen keyboard.
- The keyboard must not cover the composer or the latest message.
- Do not use hover-only affordances for message actions — provide a visible or long-press
  path.
- 44px minimum on every message action.

---

## 12. Do

- Show the user's message immediately on send
- Constrain the message column to a readable measure
- Give assistant output the space and structure of a document, not a bubble
- Reserve layout space before streaming begins
- Provide a stop control throughout generation, in a stable position
- Preserve partial output when stopped or errored
- Persist the composer draft across navigation and failure
- Name what tools are doing, in the user's terms
- Show what is in context, and let it be removed
- Make citations reachable, previewable, and honest about unavailability
- Suggest specific prompts in the empty state
- Announce streaming start and completion, not every token
- Inherit the host application's tokens and density for embedded forms

## 13. Do not

- Do not put long assistant responses in chat bubbles
- Do not use identical treatment for user and assistant turns
- Do not auto-scroll away from a user who has scrolled up
- Do not animate height on every streaming chunk
- Do not animate individual characters
- Do not discard the user's message on error
- Do not clear the composer before the send is accepted
- Do not hide tool failures behind a confident answer
- Do not show reasoning summaries above the answer, or expanded by default
- Do not use "Ask me anything" as an empty state
- Do not auto-expand a floating assistant unprompted
- Do not let the launcher cover primary actions or bottom navigation
- Do not announce every token to screen readers
- Do not build a chat when a form would serve the user better
- Do not let an embedded assistant carry its own visual identity

## 14. Source inspiration

What the corpus contributed, precisely — and it is little.

| Source | What was learned |
|---|---|
| `design-md/tesla/DESIGN.md` § *Component Stylings › Persistent Chat Bar* | The only observed conversational component in the corpus. Establishes the persistent-bar form as a real pattern: a single always-available input signalling availability without claiming layout |
| `design-md/claude/DESIGN.md` § *Overview*, § *Colors* | A conversational product's brand surface. Contributes the structural idea that dark product surfaces can sit inside a warm light canvas — useful for code blocks and artifact panels within an otherwise light chat UI |
| `design-md/intercom/DESIGN.md` § *Overview* | Accent colour scoped to an AI sub-brand rather than applied product-wide. Directly applicable: an assistant feature can carry a scoped accent without restyling its host |
| `design-md/raycast/DESIGN.md` § *Components* | Command-palette-style rows and hairline borders — the closest corpus analogue to a compact, keyboard-driven assistant entry point |
| `design-md/mintlify/`, `design-md/minimax/` § *Layout* | 3-column layouts with a narrow prose measure. Transfers directly: assistant output is prose and obeys the same measure |
| `design-md/spotify/DESIGN.md` § *Colors* | The corpus's one real application UI: a dark charcoal surface ladder where content supplies colour. Applicable to a dark chat surface where message content should dominate |

**Adopt the structural principles, not the identities.** The persistent-bar *placement*
logic, the *scoped-accent* technique, the *surface-ladder* approach, the *narrow-measure*
discipline. Nothing here means make your assistant look like any of these brands.

## 15. Common mistakes

| Mistake | Consequence | Correction |
|---|---|---|
| Chat for structured input | Slower, error-prone, hallucination-exposed | Build the form; add AI to fields |
| Full-width message column | Long answers become unreadable | 680–760px measure |
| Bubbles for long output | Wasted space, wrong idiom | Plain container for assistant turns |
| No stop control | User trapped watching output they don't want | Stop replaces send during streaming |
| Layout shift while streaming | Reading is disrupted | Reserve space; never transition height |
| Lost input on error | Retyping; erodes trust fast | Preserve message and draft always |
| Generic loading spinner | User cannot tell thinking from a hang | Name the operation |
| Hidden context | Answers seem arbitrary; privacy concerns | Show context chips |
| Decorative citations | Look sourced, aren't verifiable | Real links with previews |
| Every-token announcements | Unusable with a screen reader | Announce start and completion |
| Assistant with its own design language | Feels bolted on | Inherit host tokens and density |
| Suggested prompts that are marketing copy | Teach nothing | Use real, specific, capability-accurate prompts |

## 16. Review checklist

[checklists/conversational-ai-review.md](../checklists/conversational-ai-review.md)

## 17. Template

[templates/DESIGN.conversational-ai.md](../templates/DESIGN.conversational-ai.md)
