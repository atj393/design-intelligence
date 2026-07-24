# Prompt 04 — Build a conversational or assistant interface

---

```
Build a <FORM: full-page chat | side panel | floating assistant | persistent bar |
task copilot> for <PRODUCT / HOST APPLICATION>.

FIRST, ANSWER THIS
Is conversation the product, or a feature of a product that does something else?
If the user's request could be expressed as a form with fewer than about 8 fields, tell me —
a form would serve them better, and I would rather know now.

CONTEXT
- What the assistant does: <capability>
- Where it lives: <standalone | inside an application; which surfaces>
- Context it can access: <documents, records, selection, whole workspace>
- Tools it can call: <search, retrieval, actions, code execution>
- Does it produce structured output? <if yes, what shape>
- Multi-conversation history? <yes/no>
- Model or mode selection exposed? <yes/no>
- Attachments supported? <types, limits>
- Citations required? <yes/no>

STEP 1 — INSPECT. Report before writing code:
- The project DESIGN.md and the host application's tokens
- The host's density mode and canvas polarity — the assistant MUST inherit both
- Existing components: message list, code block, markdown renderer, toast, panel
- Streaming infrastructure available
- How the host handles focus management and live regions

Read design-intelligence/categories/conversational-ai.md fully. Note its evidence banner:
this category is predominantly synthesized, so treat its specifics as a starting position.

STEP 2 — BUILD

Layout:
- Message column max-width 680-760px. Assistant output is prose and obeys a readable measure.
  A full-width response is genuinely harder to read.
- Assistant turns: NO bubble. Plain container, full column width, document-like structure.
- User turns: subtle surface tint or a right-aligned bubble. The asymmetry is deliberate.
- Distinguish speakers by at least TWO channels (label + tint, or label + gutter marker).
  Never by colour alone, never by alignment alone.
- 24px between turns, 12px within a turn.

Composer:
- Min 56px, auto-grow to ~200px then scroll internally.
- Enter sends, Shift+Enter newlines, Cmd/Ctrl+Enter always sends, Esc stops generation,
  Up-arrow on empty recalls the last message.
- Send button becomes Stop during streaming, in the SAME position and size.
- Persist the draft across navigation, reload, and error. Never lose it.
- Clear the input only AFTER the send is accepted.
- Concrete placeholder text, not "Type a message...".

Generation states — implement every one:
- Submitted: user message appears IMMEDIATELY, before any server response
- Thinking: indicator within 100ms, distinct from streaming
- Tool use: name the operation ("Searching invoices..."), not a generic spinner
- Streaming: stop control available throughout
- Complete: copy, regenerate, edit, feedback actions appear in a RESERVED row
- Stopped: keep partial output, label it, offer continue
- Error: KEEP the user's message, explain, offer retry
- Rate-limited: state the limit and when it lifts

Layout stability during streaming — this is the failure mode that matters most:
- Reserve the turn container before content arrives
- Never animate height per chunk
- Buffer incremental markdown to safe boundaries so an unclosed code fence does not reflow
- Never animate individual characters
- Auto-scroll ONLY while the user is already at the bottom; stop on scroll-up and show a
  "jump to latest" control

Content rendering:
- Full markdown: headings, lists, tables, code
- Code blocks: dedicated surface, mono, language label, copy button with confirmation,
  horizontal scroll (never wrap)
- Tables: real tables, horizontally scrollable in a bounded container
- Images: constrained to column width, alt text
- Citations (if applicable): inline markers at the claim, hover/focus preview, numbered list
  below, >=24px click target. Say plainly when an answer is unsourced.

Context and privacy:
- Show what is in context as removable chips
- Say when context was truncated
- State retention and visibility at the point of use, not only in a policy link

Empty state:
- 3-5 SPECIFIC suggested prompts drawn from real capability. Not "Ask me anything".
- Suggestions populate the composer (editable) rather than sending immediately
- Distinguish first-run empty from cleared-history empty

Accessibility:
- aria-live="polite" on the response region. Announce start and completion —
  NEVER announce every token; that makes the interface unusable with a screen reader.
- Do not steal focus on new messages; keep it in the composer
- Each turn is a landmark or list item with an accessible speaker label
- Stop control keyboard-reachable throughout, Esc bound
- No typing animations under prefers-reduced-motion
- Message actions >=44px on touch; no hover-only affordances

CONSTRAINTS
- The assistant INHERITS the host's tokens, density, and polarity. It must not carry its own
  visual identity.
- Do not build a chat where a form would serve better.
- Do not put long output in bubbles.
- Reuse the host's existing components.

REPORT
ASSUMPTIONS / DEVIATIONS / INVENTED VALUES / UNRESOLVED / REUSED / CREATED / VERIFIED
Plus: confirm explicitly that (a) input is never lost on error, (b) layout does not shift during
streaming, (c) a stop control is available throughout generation.
```
