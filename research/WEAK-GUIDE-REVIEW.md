# Weak-Evidence Guide Review

An adversarial pass over the four guides with no corpus support, plus a protocol for the user
testing that this review **cannot substitute for**.

---

## What this is, and what it is not

**The recommended next step was "validate the four weak-evidence guides with real users."** That
was not done, because it cannot be — this synthesis has no access to users, products, or sessions.
Claiming otherwise would be the exact failure the evidence banners exist to prevent.

What was done instead, in two parts:

| Part | What it is | What it proves |
|---|---|---|
| **§1 Adversarial review** | A deliberate attempt to break each guide's own claims — find rules stated too absolutely, thresholds with no basis, and tensions papered over | That the guides are internally defensible. **Not** that they work for users |
| **§2 Validation protocol** | An executable test plan with tasks, metrics, and pass criteria | Nothing yet. It is the instrument, not the result |

**Adversarial review substitutes for user testing about as well as proofreading substitutes for
publishing.** It catches self-contradiction and over-claiming. It cannot tell you whether an
operator can actually clear their queue.

Guides reviewed — the four with **zero** direct corpus sources, plus spatial with none at all:

- [../categories/conversational-ai.md](../categories/conversational-ai.md)
- [../categories/dashboard-admin.md](../categories/dashboard-admin.md)
- [../categories/commercial-multi-role-platform.md](../categories/commercial-multi-role-platform.md)
- [../categories/spatial-map-3d.md](../categories/spatial-map-3d.md)

(The fifth weak guide, [data-analytics.md](../categories/data-analytics.md), inherits the
dashboard guide's table and density model; findings A-03 and A-06 apply to it.)

---

## §1 — Adversarial findings

Method: for each normative rule, ask three questions. *Is there a real product where following
this produces a worse result? Does the guide state a number it cannot justify? Does it resolve a
tension that is actually unresolvable?* Six findings survived. All six are now fixed in the
guides.

### A-01 — "Never bubble assistant responses" was wrong for short-turn assistants

**The claim:** assistant turns get a plain container, never a bubble.

**The counter-case:** support bots, booking flows, and triage assistants where responses are one
or two sentences. Users arrive with a messaging mental model, and there the asymmetric plain
container reads as broken — not as considered. The rule was derived from long-form assistants and
over-generalised to the category.

**Fixed:** the rule is now conditioned on expected response length, with a three-row decision
table, plus a default (plain container) for when length is unpredictable, because it degrades
gracefully for short responses while a bubble degrades badly for long ones.

### A-02 — The message-column width had an unresolvable tension, presented as resolved

**The claim:** 680–760px, from the prose measure.

**The problem:** the guide simultaneously requires full Markdown rendering — code blocks and
tables. **Prose wants 680px; code wants 900px+.** One column width cannot serve both, and the
guide asserted the prose number while requiring the code content, without acknowledging that
following both instructions produces horizontally-scrolling code on every technical answer.

**Fixed:** the tension is now stated, with three ranked resolutions (let structured blocks break
out of the prose column; widen to 820px; move artifacts to a side panel) and an explicit warning
against the naive fix of widening to 1200px, which repairs code and ruins every prose answer.

### A-03 — "Never zebra-stripe" was too absolute

**The claim:** never stripe; stripes consume the channel hover and selection need.

**The counter-case:** tables of ~15+ columns that scroll horizontally. Hover alone does not let a
user track a row across a viewport they cannot see all of at once. The stated *reason* was sound;
the absolute prohibition was not.

**Fixed:** downgraded from "never" to "avoid", with the wide-table exception and a concrete
constraint — stripe at roughly a 2% surface shift against hover's 4%, so hover and selection still
dominate.

### A-04 — The spatial opacity rule confused the mechanism with the goal

**The claim:** panels must be opaque or ≥90% opaque.

**The problem:** the actual requirement is that panel text meets its contrast floor over the
worst-case basemap. A translucent panel with sufficient blur plus a darkening layer can meet it,
and capable map tools do this. The guide mandated one implementation rather than the outcome.

**Fixed:** restated as a contrast requirement measured against the worst case (the brightest
region the panel can overlap, for satellite basemaps), with opacity as the fallback when the
basemap is user-switchable and the guarantee cannot be made.

### A-05 — "Disable and explain" was under-qualified for security-sensitive products

**The claim:** show unavailable actions disabled, with an explanation of what permission is needed
and who grants it.

**The counter-case:** the explanation is an information disclosure. An unprivileged user learning
that "export full customer database" exists — and that it requires Security Admin — has learned
which capability exists and which role to target. Good guidance for ordinary business permissions;
actively harmful for privileged security actions.

**Fixed:** added a third hide condition ("when revealing it discloses system capability to a
lower-privilege user"), a decision rule (hide when the action's existence, name, or required role
is information you would not put in public documentation), and a note to judge per action rather
than adopting one platform-wide policy.

### A-06 — Two thresholds are invented numbers presented as rules

Found by asking "where did this number come from?" of every numeric threshold in the four guides.

| Threshold | Guide | Basis |
|---|---|---|
| Sticky chrome **≤20%** of viewport | dashboard-admin | **Invented.** No corpus source, no cited research |
| Panel occlusion **≤30%** of viewport | spatial-map-3d | **Invented.** Same |

Both are plausible and both are useful as forcing functions — the build test in
[TEMPLATE-VALIDATION.md](TEMPLATE-VALIDATION.md) showed the 20% figure catching a genuine defect
(196px of sticky chrome = 22.8%). But neither has evidence behind it, and both read like measured
findings.

**Fixed:** the spatial occlusion budget is now explicitly labelled a synthesized heuristic whose
purpose is to prompt measurement. The dashboard sticky budget is retained as a rule because the
build test demonstrated it discriminating a real failure from a real fix (22.8% → 12.7%) — but it
is listed here so its origin is not mistaken for evidence.

### Rules that survived the pass

Worth recording, since a review that finds everything wrong is as useless as one that finds
nothing:

| Rule | Why it held |
|---|---|
| Never announce every streamed token to screen readers | Makes the interface unusable with assistive tech. No counter-case |
| Never lose the user's input on error | No product benefits from discarding typed input |
| Reserve layout space before streaming | Reflow while reading is disruptive in every case |
| Never reorder live rows under the cursor | Causes mis-clicks on destructive actions |
| Status meanings identical across every role | The counter-case (per-role status semantics) causes operational errors |
| Impersonation banner non-dismissible | The counter-case is destructive actions in the wrong account |
| Pan the map so the selection stays visible | No case where hiding the selected feature helps |
| "No data" distinguished from zero | A correctness requirement, not a preference |
| Refresh keeps existing data visible | Verified in the build test; the alternative is unusable |
| Compact density is pointer-only | Follows from the 44px floor |

---

## §2 — User validation protocol

Executable. Run this to get the evidence §1 cannot provide.

### Scope and cost

| | |
|---|---|
| Participants | 5–6 per guide being validated. Diminishing returns above 6 for this kind of test |
| Session length | 45–60 minutes |
| Format | Moderated, think-aloud, on a real build (not a prototype — states matter here) |
| Total effort | ~2 days per guide including recruitment, sessions, and analysis |
| Prerequisite | A build covering **every state**, not the happy path. See [TEMPLATE-VALIDATION.md](TEMPLATE-VALIDATION.md) |

**Test the guide, not the product.** Every task below targets a specific guide claim so a failure
points at a rule to change.

### Recruitment

| Guide | Recruit | Disqualify |
|---|---|---|
| Dashboard | People who currently use an operational tool ≥4 hours/day | Anyone who would use it monthly |
| Multi-role | At least one participant per role; at least one holding two roles | Single-role-only panels |
| Conversational | Mix of AI-fluent and AI-naive; both matter and behave differently | AI-fluent only |
| Spatial | Domain practitioners (GIS, survey, planning) | General software users |

The disqualifications matter more than the inclusions. A dashboard tested only with occasional
users will validate spacious density and mislead you.

### Task scripts

Each task names the claim it tests and what would falsify it.

**Dashboard** — [dashboard-admin.md](../categories/dashboard-admin.md)

| # | Task | Claim tested | Falsified if |
|---|---|---|---|
| D1 | "Find every exception over £10,000 older than 3 days and assign them to yourself." | Filter + bulk action discoverability | >2 participants cannot find bulk actions unprompted |
| D2 | Mid-task, trigger a background refresh. | Refresh keeps data and place | Any participant loses their place or their selection |
| D3 | "Work through the queue as you normally would" — 10 minutes, default density. | Density default is right | >half switch density immediately, or ask for a denser view |
| D4 | "Reject these three items." | Destructive confirmation is proportionate | Anyone rejects without reading, **or** anyone abandons because the friction felt excessive |
| D5 | Present the filtered-empty state cold. | Empty states are distinguishable | Any participant reads it as a system error |
| D6 | Keyboard only, no mouse. | Keyboard table navigation | Any participant cannot complete D1 |

**Conversational AI** — [conversational-ai.md](../categories/conversational-ai.md)

| # | Task | Claim tested | Falsified if |
|---|---|---|---|
| C1 | Ask something requiring a long structured answer. | Column width and A-02 resolution | Participants scroll horizontally to read code, or complain the text is too wide |
| C2 | Interrupt a generation mid-stream. | Stop control discoverability and position | >1 participant cannot find stop within 3 seconds |
| C3 | Force an error mid-conversation. | Input preservation | Any participant loses text, or expects to have lost it and is surprised |
| C4 | "Where did that answer come from?" | Citation affordance | >2 cannot reach a source |
| C5 | Present the empty state cold: "What can this do?" | Suggested prompts teach capability | Participants ask a question the assistant cannot handle |
| C6 | Screen-reader session, one participant minimum. | Announcement strategy | The participant cannot follow a response, or announcements overwhelm |

**Multi-role** — [commercial-multi-role-platform.md](../categories/commercial-multi-role-platform.md)

| # | Task | Claim tested | Falsified if |
|---|---|---|---|
| M1 | Show two role surfaces. "Are these the same product?" | Shared foundation reads as one product | Any participant says no |
| M2 | Dual-role participant switches role mid-session. | Role context is unmissable | Any participant acts in the wrong role, or has to check which they are in |
| M3 | Hit a permission wall. | Disable-and-explain vs. A-05 | Participant cannot tell what to do next, **or** learns something they should not |
| M4 | Ask a customer-role participant to describe an object using its name. | Terminology consistency | Participants and operators use different words for the same object |
| M5 | Show the impersonation banner; ask whose account they are in. | Banner visibility | Any hesitation |
| M6 | Ask an operator to complete a task designed for novices. | Expert path exists | Operator visibly frustrated by wizard steps |

**Spatial** — [spatial-map-3d.md](../categories/spatial-map-3d.md)

| # | Task | Claim tested | Falsified if |
|---|---|---|---|
| S1 | "Select that feature and tell me its area." | Inspector does not hide its subject | Any participant loses sight of what they selected |
| S2 | Draw a polygon, misplace one vertex, recover. | Per-vertex undo | Any participant loses the whole shape |
| S3 | Turn on a layer that renders nothing at the current zoom. | Empty-layer reasons | Participant concludes the tool is broken |
| S4 | Read a value from a choropleth over satellite imagery. | Contrast and A-04 basemap rule | Any misreading |
| S5 | "Is this measurement measured or calculated?" | Derived-vs-measured distinction | >1 participant cannot tell |
| S6 | Same task at 375px. | Honest mobile limits | Participant hunts for a control that was silently omitted |

### Metrics

Record per task: completion (yes / with help / no), time, errors, unprompted comments, and — most
useful — **the point at which the participant hesitated.** Hesitation localises the defect better
than completion rate.

### Interpreting results

| Pattern | Meaning | Action |
|---|---|---|
| 1 of 6 fails | Individual variance | Note it; do not change the guide |
| 2 of 6 fail | Signal | Investigate; likely a build defect |
| 3+ of 6 fail | **The guidance is wrong** | Change the guide, not just the build |
| All succeed but complain | Works, feels bad | Usually a density or friction calibration issue |
| Succeed fast, wrong result | Worst case | The interface is confidently misleading. Highest priority |

**When 3+ participants fail a task, update the guide** and record it here with the evidence.
That is how these four guides move from *reasoning* to *evidence* — and it is the only way they
will.

### Reporting back

Append findings to this file under a new `§3 — User validation results` heading, with: date,
participant count and profile, task, failure rate, the guide claim falsified, and the change
made. Then update the guide's evidence banner and the strength table in
[CATEGORY-INVENTORY.md](CATEGORY-INVENTORY.md) §3.

**Until that section exists, these four guides remain reasoning.** §1 improved their internal
quality. It did not change their evidence status, and this file should not be read as though it
did.
