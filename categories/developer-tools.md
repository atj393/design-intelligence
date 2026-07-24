# Developer Tools and Technical Platforms

Products whose users are developers: APIs, SDKs, infrastructure, CLIs, IDEs, monitoring,
databases, deployment platforms, agent frameworks.

> **Evidence strength: moderate-strong for tone and typography, synthesized for console
> surfaces.** Twenty of 74 sources are developer-domain, and five document real documentation
> surfaces. What the corpus supports well is the *visual register* of this category — and it
> supports something counterintuitive (see §1). API keys, logs, environment switching, and
> error diagnosis are synthesized.

---

## 1. The corpus refutes the genre stereotype

**Developer tools do not have to be dark.** The corpus splits almost exactly evenly:

| Dark canvas | Light / cream canvas |
|---|---|
| linear.app, raycast, voltagent, warp, sanity, resend, composio, clickhouse | cursor, lovable, posthog, replicate, expo, supabase, vercel, ollama |

One source sells a code editor and chose a warm cream canvas *because* the genre defaults to
dark. Another opens on parchment, described in its own file as a deliberate rejection of
cold-white developer convention. A third builds a playful illustrated identity for a
monitoring product.

**Consequence: choose polarity from your brand and your users' environment, not from genre
convention.**

| Choose dark when | Choose light when |
|---|---|
| The product runs alongside an IDE or terminal | The product is read more than operated |
| Users work in dark environments | Documentation is a primary surface |
| Continuity with the tool's own chrome matters | You want to differentiate from the genre |
| The product displays code as its main content | Long-form content dominates |

**Support both wherever practical.** Developers expect a theme choice, and it is the one
audience that will file an issue about its absence.

## 2. Monospace discipline

The most abused decision in this category.

**Use monospace for:**

| Content | Reason |
|---|---|
| Code — inline and block | Alignment and character disambiguation |
| Terminal / CLI output | Column alignment is semantic |
| File paths | Disambiguates `l`/`1`/`I`, `0`/`O` |
| API keys, tokens, hashes, IDs | Character-level accuracy matters |
| Version numbers, commit SHAs | Same |
| Environment variable names | Same |
| Log lines | Alignment aids scanning |
| Numeric data in tables | Or proportional font with tabular figures |

**Do not use monospace for:** navigation, buttons, headings, body prose, form labels, or
marketing copy.

One corpus source sets an entire page in monospace. It is coherent, deliberate, and a
recognised exception — it reduces reading speed and, more importantly, **eliminates the visual
distinction that makes code read as code**. If everything is mono, nothing is code.

**Mono pairing:** size mono ~1–2px smaller than adjacent proportional text at the same optical
weight — most mono faces run visually larger at the same nominal size. 14px body → 13px inline
code.

## 3. Code presentation

The category's most important component.

| Property | Requirement |
|---|---|
| Surface | Distinct from page — `surface-sunken` (light) or a step below canvas (dark) |
| Padding | 16px (12px compact) |
| Radius | Match `radius.md`–`radius.lg` |
| Font size | 13–14px |
| Line height | 1.5–1.6 — code needs more leading than prose, not less |
| Overflow | **Horizontal scroll, never wrap.** Wrapping breaks indentation semantics |
| Line numbers | Optional; non-selectable if present |
| Language label | Top-right or in a header bar |
| Copy button | Always. Top-right, with a confirmed state |
| Syntax highlighting | Yes, with contrast-checked token colours |
| Line highlighting | For drawing attention to specific lines |
| Diff view | `+`/`−` markers plus colour, never colour alone |

**Syntax highlighting must pass contrast.** Comment colours are the usual failure — a mid-grey
comment on a dark surface frequently lands near 2:1. Every token colour needs ≥4.5:1, or
≥3:1 if it is genuinely non-essential.

**Copy buttons need confirmation.** A copy button with no feedback gets pressed repeatedly.
Swap the icon and label for ~2 seconds.

**Multi-language examples:** tabbed, with the selection persisted across the whole site. A user
reading Python examples wants Python on every page, permanently.

## 4. Terminal and log output

| Element | Requirement |
|---|---|
| Surface | Near-black, even in light mode — this is a legitimate exception; terminals are dark |
| Font | Mono, 13px |
| Line height | 1.4–1.5 |
| Colour | Support ANSI colours; ensure each passes contrast on your background |
| Timestamps | Left column, mono, dimmed, consistently formatted |
| Severity | Colour + a text level (`ERROR`, `WARN`) — never colour alone |
| Wrapping | Off by default, with a toggle |
| Following | Auto-scroll while at the bottom; stop on scroll-up; "follow" toggle |
| Search | Within output, with match highlighting and count |
| Selection | Text must be selectable and copyable, including multi-line |
| Volume | Virtualise; cap retained lines with a clear indication of truncation |

**Log viewers fail on the follow behaviour more than anything else.** The rule is the same as
for chat streaming: follow while the user is at the bottom, stop the moment they scroll up,
and give them a visible way back.

## 5. API keys and secrets

Synthesized entirely, and worth care because the failure modes are security failures.

| Requirement | Detail |
|---|---|
| Default state | **Masked.** `sk_live_••••••••4a2f` — show a prefix and last 4 |
| Reveal | Explicit action, temporary, ideally re-authenticated for production keys |
| Copy | Copy the full value without revealing it |
| Creation | Show once, prominently, with an explicit "you will not see this again" warning |
| Metadata | Created date, last used, scope, environment |
| Rotation | First-class action, not buried in settings |
| Revocation | Immediate, confirmed, with impact stated |
| Environment | Visually distinct: test vs. live must be unmistakable |
| Logs | Never render a secret in log output, even masked |

**Test versus live must be unmistakable.** A persistent environment indicator — a labelled
badge, and a colour treatment as a *second* channel — prevents the expensive mistake of
running a destructive operation against production.

## 6. Environment and project context

| Element | Requirement |
|---|---|
| Current project / org | Always visible in the top bar |
| Environment | Always visible; visually distinct per environment |
| Region | Visible where it affects behaviour |
| Switcher | Consistent location; searchable when many |
| Production marker | Persistent and unmissable |
| Destructive in production | Extra confirmation, naming the environment |

## 7. Navigation

Developer products typically span three surfaces:

| Surface | Pattern |
|---|---|
| Marketing | Top bar, 5–7 destinations |
| Documentation | 3-column: sidebar / prose / TOC (see [general-website.md](general-website.md)) |
| Console / dashboard | Side nav or rail (see [dashboard-admin.md](dashboard-admin.md)) |

**Keep one token foundation across all three; vary density.** Documentation at marketing
density is unscannable; a console at marketing density is slow.

**Search is critical.** Developers search rather than browse. `Cmd/Ctrl+K` everywhere; results
should span docs, API reference, and console resources.

## 8. API reference

| Element | Requirement |
|---|---|
| Endpoint | Method badge (colour + text) + path in mono |
| Parameters | Table: name, type, required, description, default |
| Types | Mono, linked to type definitions |
| Request example | Copy-ready, multi-language tabs |
| Response example | Real, complete, realistic values — not `"string"` |
| Error responses | Enumerated with codes, causes, and fixes |
| Try-it | Sandbox where possible, clearly marked as test |
| Versioning | Prominent; note deprecations at the endpoint |
| Rate limits | Stated where relevant |

**Examples must be complete and runnable.** A snippet omitting authentication headers or
required fields costs the reader more time than no example at all.

## 9. Configuration surfaces

| Requirement | Detail |
|---|---|
| Show effective value | Alongside inherited or default values |
| Show source | Where a value comes from — default, org, project, env var |
| Reset to default | Per field |
| Validate structurally | For config files, validate syntax and schema; show the error line |
| Dangerous settings | Separated, confirmed |
| Diff before apply | For anything affecting a running system |
| Unsaved state | Visible; warn on navigate-away |

## 10. Error diagnosis

Developers debug. Design for that.

| Requirement | Detail |
|---|---|
| Error identity | Code or type, in mono, copyable |
| Cause | Plain-language explanation |
| Location | File, line, request ID, or resource |
| Fix | Concrete next step, or a link to the relevant documentation |
| Stack trace | Available, collapsed by default, copyable in full |
| Request ID | Always shown for API errors; copyable for support |
| Related logs | Link from the error to the surrounding log context |
| Retryable | Say whether retrying is safe |

**A copyable, unique error identifier is the highest-value element** — it is what gets pasted
into a search box or a support ticket.

## 11. Trust signals for a technical audience

Developers evaluate differently. What builds trust here:

| Effective | Ineffective |
|---|---|
| Real code in the hero, legible and correct | Stock photography |
| Actual product screenshots | Abstract illustration of "the cloud" |
| Honest, complete documentation | Marketing superlatives |
| Visible status page and incident history | "99.99% uptime" with no history |
| Open-source presence, changelogs | Award badges |
| Precise performance numbers with method | "Blazing fast" |
| Clear, public pricing | "Contact sales" for self-serve tiers |
| Named limitations | Implying there are none |

Several corpus sources lead with terminal or code-editor mockups as the hero rather than
photography — the product working *is* the argument.

## 12. Layout and typography

| Property | Marketing | Docs | Console |
|---|---|---|---|
| Container | 1280px | 1024–1280px shell | fluid |
| Prose measure | 680px | 680px | 640px |
| Section rhythm | 80px | 48px | 24–32px |
| Max display | 56px | 36–48px | 24px |
| Body | 16px | 16px | 14px |
| Code | 14px | 14px | 13px |
| Control height | 44px | 40px | 36px |
| Density | spacious | default | compact |

## 13. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Docs sidebar | Drawer | Drawer | 260px |
| Docs TOC | Accordion at top | Hidden | 220px |
| Code blocks | Scroll, 13px | Scroll | Full |
| Language tabs | Select | Tabs | Tabs |
| Console nav | Drawer | Rail | Full |
| Logs | Scroll, 12px | Full | Full |
| API tables | Transform to definition list | Scroll | Full |
| Try-it panel | Below example | Below | Side-by-side |

Documentation on mobile matters — often read by someone away from their desk. Code blocks must
scroll cleanly and copy buttons must remain reachable.

## 14. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- Syntax-highlighting token colours all pass contrast, in both themes.
- Code blocks keyboard-reachable and scrollable; copy buttons have accessible names and
  announce success.
- Diff markers use `+`/`−` characters as well as colour.
- Log severity has a text level, not just colour.
- Method badges (`GET`, `POST`) carry text, not colour alone.
- Terminal output is real selectable text, never an image or canvas.
- Environment indicators are text-labelled, not colour-only.
- Language tab selection is announced on change.

## 15. Do

- Choose canvas polarity from brand and environment, not genre
- Support both themes where practical
- Reserve monospace for code, paths, keys, IDs, and aligned data
- Scroll code horizontally; never wrap it
- Put a confirmed copy button on every code block and every key
- Persist language-tab selection site-wide
- Mask secrets by default; allow copy without reveal
- Make environment context persistent and unmistakable
- Give every error a copyable identifier and a concrete next step
- Show complete, runnable examples with realistic values
- Publish real numbers with their measurement method
- Keep one token foundation across marketing, docs, and console

## 16. Do not

- Do not set interface text in monospace
- Do not wrap code blocks
- Do not use a copy button without confirmation feedback
- Do not ship syntax colours that fail contrast
- Do not reveal secrets by default or render them in logs
- Do not let test and live environments look alike
- Do not show `"string"` placeholder values in examples
- Do not omit authentication from example requests
- Do not use marketing superlatives instead of measured claims
- Do not auto-scroll a log the user has scrolled away from
- Do not inherit marketing density into docs or console
- Do not render terminal output as an image

## 17. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/cursor/DESIGN.md` § *Overview* | Warm cream canvas for a code editor — an explicit rejection of the dark-IDE default. Also: a pastel state palette confined to *in-product* timeline visualisations rather than applied as chrome |
| `design-md/opencode.ai/DESIGN.md` § *Typography* | An entirely monospaced page. Documented here as an exception and a caution: total mono removes the distinction that makes code legible as code |
| `design-md/warp/DESIGN.md` § *Shapes*, § *Components* | Tight 1–6px radius ladder and terminal-mockup imagery. Restrained geometry supporting density |
| `design-md/composio/DESIGN.md` § *Overview* | 2×2 terminal-pane hero — showing the product's output as the primary argument |
| `design-md/linear.app/DESIGN.md` § *Typography*, § *Elevation & Depth* | Mono confined to code contexts inside product screenshots, never on chrome; surface ladder for dark hierarchy |
| `design-md/mintlify/DESIGN.md` § *Layout*, § *Components* | Full 3-column docs model with dedicated code surfaces, alongside a marketing surface at entirely different density |
| `design-md/vercel/DESIGN.md` § *Typography* | A dedicated monospaced caption face for technical labels — mono as a *semantic* register rather than a whole-page aesthetic |
| `design-md/clickhouse/DESIGN.md` § *Colors* | Single accent carrying CTAs and stat numerals; code blocks embedded in dark cards |
| `design-md/posthog/DESIGN.md` § *Overview* | Illustrated warmth in a monitoring product — evidence that technical credibility does not require a somber aesthetic |

## 18. Common mistakes

| Mistake | Correction |
|---|---|
| Monospace as the whole interface | Mono for code and identifiers only |
| Wrapped code blocks | Horizontal scroll |
| Copy button without feedback | Confirmed state for ~2s |
| Comment colours failing contrast | Verify every syntax token |
| Test and live indistinguishable | Persistent labelled environment indicator |
| Incomplete examples | Complete, runnable, realistic |
| Docs at marketing density | 48px rhythm, 680px measure, 36–48px display |
| Log auto-scroll fighting the user | Follow only when at bottom |
| Secrets revealed by default | Mask; copy without reveal |
| Errors without identifiers | Copyable code + request ID |

## 19. Template

[templates/DESIGN.developer-tool.md](../templates/DESIGN.developer-tool.md)
