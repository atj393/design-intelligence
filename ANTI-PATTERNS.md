# Anti-Pattern Guide

Design failures, why each is harmful, when a similar technique is nevertheless legitimate, and
how to correct it.

**Source note.** The general anti-patterns draw on the corpus's own `Do's and Don'ts` sections —
present in 73 of 74 files and the richest evidence seam in the repository for this purpose.
Nearly every prohibition below is a rule some source states about its own system. The
category-specific sections are synthesized, matching their guides' evidence strength.

Each entry follows: **what it is → why it harms → when it is legitimate → correction.**

---

## Part 1 — AI-generated design failures

These recur in machine-generated interfaces because they are the statistically average
appearance of "modern web design" rather than decisions.

### A1. Gradient everywhere

**What:** Gradients on buttons, cards, backgrounds, text, borders, icons.

**Why it harms:** A gradient is a strong visual signal. When everything has one, nothing stands
out, and the interface reads as texture rather than structure. Gradient text frequently fails
contrast because the ratio changes across the glyph. Gradient buttons make it hard to distinguish
primary from secondary.

**Legitimate when:** One gradient, in one place, as a deliberate brand signature — a hero
backdrop, a single feature panel, a data visualisation ramp. Several corpus sources use exactly
one atmospheric gradient as their entire decorative system.

**Correction:** Pick at most one gradient surface per page. Solid fills for all controls. If
gradient text is required, verify contrast at the lightest point of the glyph.

### A2. Everything is a rounded card

**What:** Every content block in a 12–16px rounded, bordered, shadowed container. Cards nested
inside cards.

**Why it harms:** Cards mean "these things are separate and comparable". When the whole page is
cards, the grouping signal is gone and every border is visual noise competing with content. Nested
cards produce three borders doing one job.

**Legitimate when:** Items genuinely are independent, comparable, and individually actionable —
product grids, feature comparisons, dashboards of distinct metrics.

**Correction:** Ask what the card is grouping. If the answer is "one paragraph", delete the card.
If the answer is "the page's content", the page is already the container. Never nest cards; use
spacing and headings inside a single container.

### A3. Glassmorphism by default

**What:** `backdrop-filter: blur()` with translucent surfaces on panels, navigation, and modals.

**Why it harms:** Text contrast becomes dependent on whatever is behind it — so it is
unpredictable and frequently fails. `backdrop-filter` is expensive on large surfaces and drops
frames on mid-range hardware. Over dense content, blurred backgrounds read as smudged.

**Legitimate when:** A small overlay above simple, controlled content, where contrast has been
verified against the actual worst-case background. A translucent nav over a solid hero can work.

**Correction:** Opaque surfaces for anything containing text. If translucency is a brand
requirement, add enough opacity that contrast is guaranteed regardless of backdrop — typically
≥90%.

### A4. Random shadows

**What:** Shadows applied at varying, arbitrary values with no elevation system — `0 4px 6px`
here, `0 10px 40px` there.

**Why it harms:** Shadow communicates height. Inconsistent shadows communicate inconsistent
heights, so the layering model becomes noise. Users read heavy shadows as clickable, so static
elements with big shadows are misleading.

**Legitimate when:** A defined elevation scale with 3–5 levels, each mapped to a purpose.

**Correction:** Define levels 0–4. Every element references a level. Prefer borders for grouping
(the corpus's dominant approach — ~38 of 74 sources) and reserve shadow for genuinely floating
layers.

### A5. Inconsistent spacing

**What:** 13px here, 18px there, 22px somewhere else. No grid.

**Why it harms:** Misalignment is perceptible even when it is not identifiable — the interface
reads as unfinished. It also makes maintenance guesswork: the next developer invents another
value.

**Legitimate when:** Never. Optical adjustments (±1–2px to compensate for a glyph's side bearing)
are a different thing and should be documented.

**Correction:** 4px grid, 8px increments preferred. Every spacing value is a token. Reject any
value not on the scale.

### A6. Weak typographic hierarchy

**What:** `h1` 24px, `h2` 22px, `h3` 20px, body 16px. Everything at similar weight.

**Why it harms:** Scanning fails. Users navigate by heading, and headings only work when levels
are distinguishable at a glance without comparison.

**Legitimate when:** Deliberately flat hierarchies in very dense interfaces — but then distinguish
levels by weight, colour, or case rather than by 2px of size.

**Correction:** 1.15×–1.35× between adjacent steps. If three levels are needed in a narrow range,
differentiate by weight and colour as well as size.

### A7. Oversized hero on every surface

**What:** 72px display type and 100vh height on application pages, dashboards, settings, and
documentation.

**Why it harms:** Marketing scale inside a product wastes the screen on decoration when the user
came to work. A 100vh hero hides the fact that the page continues.

**Legitimate when:** A marketing or brand surface where a single visit and a single message are
the whole job.

**Correction:** Display ceiling by surface — 56–80px marketing, 36–56px documentation, 24–32px
application, 20–28px dashboard. Hero height ≤85vh so the page edge is visible.

### A8. Decorative elements with no meaning

**What:** Floating blurred orbs, abstract shapes, grid patterns, animated particles, "AI"
sparkles.

**Why it harms:** Attention is finite. Every decorative element competes with content, adds
weight, and dates the interface. In products, it reads as unserious.

**Legitimate when:** A brand system where the decorative language is deliberate, consistent, and
confined to marketing surfaces. Several corpus sources use exactly one atmospheric device as
their whole decorative vocabulary.

**Correction:** Remove it and see whether anything is lost. If the answer is no, the decision is
made. Never carry decoration into application surfaces.

### A9. Excessive animation

**What:** Scroll-triggered reveals on every element, hover animations everywhere, animated page
transitions, looping decorative motion.

**Why it harms:** Motion demands attention involuntarily. Repeated animation on frequently-used
paths is a cumulative time tax. Perpetual motion is a permanent distraction and a battery cost.
It also frequently fails `prefers-reduced-motion`.

**Legitimate when:** Motion communicates causality, hierarchy, progress, or spatial change — a
2D-to-3D camera move, a drawer sliding from the edge it belongs to, a progress indicator.

**Correction:** Justify each animation against those four purposes. Cap durations: 100ms feedback,
150–200ms small transitions, 250–300ms panels. Nothing loops except progress. Honour reduced
motion.

### A10. Insufficient contrast

**What:** Light grey on white for secondary text, placeholders, borders, disabled states,
captions.

**Why it harms:** Fails a meaningful share of users outright, and everyone in bright light or on
a poor screen. It is the most common accessibility defect and the easiest to prevent.

**Legitimate when:** Genuinely decorative elements carrying no information. That is a narrow set.

**Correction:** Body ≥4.5:1, large text ≥3:1, UI boundaries and focus ≥3:1. Verify in **both**
modes — palettes that pass in light frequently fail in dark on secondary text and the brand
accent.

### A11. Repeated card grid as the entire page

**What:** Section after section of identical 3-across card grids with an icon, a heading, and two
lines of text.

**Why it harms:** No hierarchy, no rhythm, no reason to read past the first grid. It is the
default output of "make a features section" and it looks like it.

**Legitimate when:** One such grid, once, where the items really are parallel.

**Correction:** Vary section structure — alternate polarity, change layout (split, full-bleed,
list, comparison), vary item scale to show importance. If six sections are all card grids, five
of them have not been designed.

### A12. Pill everything

**What:** `border-radius: 9999px` on buttons, inputs, badges, cards, images, containers.

**Why it harms:** Pills consume horizontal space at the ends, blur alignment in dense layouts, and
remove the radius channel for distinguishing element types. Pill inputs make left-aligned text
sit oddly.

**Legitimate when:** Pills are your radius character *and* the layout is low-density — several
corpus consumer brands are pill-dominant and coherent. Also always correct for avatars, tags, and
toggles.

**Correction:** Reserve `full` for avatars, tags, toggles, and status pills. Use `radius.md` for
buttons and inputs. Never pill a data-dense row or a table cell.

### A13. Uncontrolled colour

**What:** Six or seven accent colours used decoratively, alongside semantic status colours.

**Why it harms:** Colour is your clearest instruction channel. When it is used decoratively,
users cannot tell decoration from a warning. Semantic colours stop working.

**Legitimate when:** Each colour maps to something structural — product lines, content categories,
object types, data series. Every multi-accent corpus source does this.

**Correction:** One accent unless you can state each additional colour's structural mapping.
Semantic colours are reserved and never reused decoratively.

### A14. Inaccessible state communication

**What:** Red for error, green for success, amber for warning — with no icon, no label, no other
channel.

**Why it harms:** Roughly 8% of men have a colour-vision deficiency; red/green is the pair they
cannot distinguish. It also fails in greyscale, in bright sunlight, and for users with custom
stylesheets.

**Legitimate when:** Never as the sole channel. Colour as a *reinforcing* channel is good design.

**Correction:** Every status needs colour + icon + text. In tables, the text label is not optional.
Test by setting the OS to greyscale.

### A15. Mobile as compressed desktop

**What:** The desktop layout scaled down. Tables squeezed to 375px. Hover-only actions. 32px
controls.

**Why it harms:** Nothing works. Tables become unreadable, hover actions are unreachable, targets
are too small, and priority is wrong because the desktop ranking was never re-evaluated.

**Legitimate when:** Never. Simple content-only pages may need little adaptation, but that is
because the layout was already simple, not because compression worked.

**Correction:** Re-rank priority for mobile. Tables transform to cards or scroll with a pinned
column. All hover affordances get a tap equivalent. 44px targets. Design at 375px deliberately.

### A16. Component inconsistency

**What:** Three button styles for the same purpose. Two card treatments. Inputs of different
heights on one form.

**Why it harms:** Users learn interfaces by pattern. Inconsistency breaks the pattern, so each
variant must be interpreted individually. It also signals that nobody is in control of the system.

**Legitimate when:** Genuine variants with distinct meanings — primary vs. secondary vs.
destructive — that are documented and used consistently.

**Correction:** One component per purpose, with documented variants. Input height must equal button
height where they sit adjacent. Audit for duplicates before adding a new component.

### A17. Duplicated navigation

**What:** The same destinations in a top bar and a sidebar. Or a footer repeating the full nav
alongside a mega-menu.

**Why it harms:** The user must decide which navigation is authoritative, and they cannot tell.
Active-state management across two systems is unreliable, so they frequently disagree.

**Legitimate when:** Different *levels* in each — global sections in the top bar, within-section
pages in the sidebar. That is hierarchy, not duplication.

**Correction:** One navigation system per hierarchy level. Footers may repeat links as a
convenience but should not mirror the primary nav's structure.

### A18. Placeholder as label

**What:** Form fields labelled only by placeholder text.

**Why it harms:** The label disappears the moment the user types, so they cannot check what they
entered. Placeholder text typically fails contrast. Screen readers treat it inconsistently.
Autofill can obscure it entirely.

**Legitimate when:** Never for labelling. Placeholders are for format hints — "DD/MM/YYYY" —
alongside a real label.

**Correction:** Visible label above every field. Placeholder only for format examples.

### A19. Missing states

**What:** Only the happy path is designed. No empty, loading, error, partial, or permission-denied
state.

**Why it harms:** These states occur constantly in real use. An unstyled empty table reads as a
bug. An error with no recovery path is a dead end. This is the most common gap in generated
interfaces — and notably, the source corpus does not document these states either (`empty state`
appears in one file of 74), which is likely part of why generated output omits them.

**Legitimate when:** Never.

**Correction:** For every data-bearing view, specify: first-run empty, filtered-empty, initial
loading, refresh loading, partial data, error, and permission denied. Two distinct empty states
matter: "nothing exists yet" and "your filters matched nothing" need different messages.

### A20. Layout shift

**What:** Content jumping as images load, fonts swap, ads inject, or async content arrives.

**Why it harms:** Users mis-click. Reading position is lost. It is the most viscerally
irritating category of interface defect, and it is almost entirely preventable.

**Legitimate when:** Never.

**Correction:** Intrinsic dimensions on all media. Reserve space for async content. `font-display:
optional` or metric-compatible fallbacks. Skeletons that match final dimensions. Never animate
height on streaming content.

---

## Part 2 — Category-specific anti-patterns

### Conversational AI

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Oversized message bubbles** | A 600-word bubble with 20px radius is the wrong idiom; rounded edges waste width | Plain container for assistant turns; bubbles only for short user turns |
| **Unclear source distinction** | Users cannot tell their words from the model's — a correctness risk | Two channels minimum: label plus surface tint or gutter marker |
| **Unstable streaming layout** | Reflow on every chunk disrupts reading | Reserve the container; never transition height; buffer Markdown to safe boundaries |
| **Hidden context state** | Answers seem arbitrary; users cannot reason about them, and privacy is unclear | Visible, removable context chips |
| **Full-width message column** | Long prose at 1400px is unreadable | 680–760px measure |
| **No stop control** | User trapped watching unwanted output | Stop replaces send, same position |
| **Input lost on error** | Retyping; fast trust erosion | Preserve message and draft always |
| **Every-token screen-reader announcement** | Unusable with assistive tech | Announce start and completion only |
| **Chat where a form belongs** | Slower, error-prone, hallucination-exposed | Build the form; add AI at the field level |
| **Assistant with its own design language** | Reads as bolted on | Inherit host tokens and density |

### Marketing websites

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Unsupported claims** | Sceptical evaluators discount everything, including true claims | State the comparison basis, or cut the claim |
| **Visual noise** | Competes with the product demonstration | One decorative device, used consistently |
| **Excessive sections** | Each costs scroll and attention; the last ones are never seen | Cut to the sequence that persuades |
| **Weak CTAs** | "Learn more" ×12 tells the user nothing | Name the outcome: "Start free trial" |
| **100vh hero** | Hides that the page continues | ≤85vh |
| **Hero scale repeated** | Destroys the hierarchy that makes the hero work | One hero scale per page |
| **Text on imagery without contrast check** | Illegible against the worst-case region | Scrim, safe area, or move the text |
| **Pricing hidden behind contact forms** | Filters out buyers, not just browsers | Publish self-serve pricing |
| **Animation on every scroll pass** | Cumulative irritation | Once per element, first view only |

### Multi-role platforms

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Mixed permissions** | Users see actions they cannot take, with no explanation | Disable + explain who can grant it |
| **Inconsistent terminology** | Roles cannot communicate about the same object | One name per shared object; document genuine role-specific mappings |
| **Identical dashboards for different roles** | At least one role is poorly served | Role-specific default views answering that role's first question |
| **Status meaning drift** | "Pending" differs by surface — causes real operational errors | One central status vocabulary |
| **Admin theme switching** | Breaks cross-role recognition; doubles the design surface | Persistent labelled marker instead |
| **Invisible impersonation** | Destructive actions taken in the wrong account | Non-dismissible banner naming the account |
| **Independent per-role design** | Four products wearing one logo | Shared foundation, layered variation |
| **Admin complexity exposed to customers** | Confusion and support load | Scope surfaces by role |

### Dashboards and administration

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Oversized controls** | Fewer rows per screen in an all-day tool | 32–36px per density mode |
| **Excessive whitespace** | Scroll paid on every visit, forever | 16–24px rhythm; compact/standard density |
| **Hidden bulk actions** | Operators use them hourly and cannot find them | Visible on selection, no layout shift |
| **Ambiguous destructive operations** | Wrong data deleted | Name target and count; separate from primary |
| **Zebra striping** | Consumes the channel hover and selection need | Hairline row borders only |
| **Infinite scroll on tables** | Position lost; footer unreachable; "where was I?" | Pagination with totals |
| **Table cleared on refresh** | Unusable on a polling dashboard | Keep data; indicate refreshing |
| **Rows reordering under the cursor** | Mis-clicks on destructive actions | "3 new — show" affordance |
| **Filters lost on reload** | Daily irritation; views unshareable | Full state in the URL |
| **Blank empty cells** | Reads as a rendering fault | Em-dash |
| **Proportional digits** | Columns jitter; comparison harder | Tabular figures, right-aligned |
| **No keyboard table navigation** | Table unusable without a mouse | Arrow keys, visible focus |

### E-commerce

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Decorated checkout** | Every element is a conversion risk | Strip to plain and functional |
| **Forced account creation** | Major abandonment cause | Guest checkout; offer account after purchase |
| **Surprise shipping costs** | The largest single cause of abandonment | Surface early |
| **Hidden out-of-stock variants** | Users think their size does not exist | Show disabled with a reason |
| **Mixed grid aspect ratios** | Grid reads as broken | Fixed frame; crop or letterbox |
| **Dead-end search** | Lost sale | Alternatives, categories, popular items |
| **Blocked paste in card fields** | Errors and abandonment | Allow paste |
| **Double-submittable payment** | Real financial bug | Disable on submit; guard server-side |
| **Undismissable urgency timers** | Manipulative and inaccessible | Dismissible or absent |

### Financial and high-trust

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Single ambiguous "balance"** | User misjudges available funds | Separate labelled available/pending/total |
| **Colour-only gain/loss** | Core information invisible to colour-blind users | Sign + arrow + colour |
| **Relative timestamps in records** | Records unverifiable | Absolute with timezone |
| **Generic payment errors** | User does not know if they were charged | State cause and charge status |
| **Session timeout losing data** | Abandonment; anger | Warn, extend, preserve |
| **Unstated fees** | Perceived deception | Itemise everything |
| **Committing action beside cancel** | Expensive mis-clicks | Separate them; never default-focus the commit |
| **Small-print legal text** | Ethical and increasingly compliance failure | 16px minimum |
| **Pre-checked or bundled consent** | Invalid consent | Unchecked, specific, recorded |
| **Conservative palette as the trust strategy** | Looks safe while behaving unsafely | Invest in confirmation and traceability |

### Content and editorial

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Full-width body text** | Reading fails past ~90 characters | 640–720px measure |
| **Large sticky header** | A permanently lost line of text per screen | ≤48px, or hide on scroll-down |
| **Modal before first read** | Most reliable way to lose a reader | Let them read first |
| **Content inserted mid-paragraph** | Breaks the sentence | Between sections only |
| **Uniform index grid** | No editorial guidance; reads as a wall | Vary scale for hierarchy |
| **Cumulative interruption overload** | Article becomes unreadable | Budget interruptions as a total |
| **Display face used for body** | Reading speed collapses | Display for headlines only |
| **Sponsored content indistinguishable from editorial** | Erodes trust; often a regulatory issue | Unambiguous labelling |

### Data and analytics

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Unmarked partial periods** | Today's partial data looks like a crash | Mark incomplete explicitly |
| **Missing data rendered as zero** | Wrong conclusions | Distinguish "no data" from `0` |
| **Truncated bar y-axis** | Misleadingly exaggerates differences | Start bars at zero |
| **Non-deterministic series colour** | Mental map lost on every filter change | Deterministic assignment |
| **Colour-only series distinction** | Unreadable for many users and in greyscale | Markers, dashes, direct labels |
| **Pie charts beyond three slices** | Angle comparison is unreliable | Bar chart |
| **Missing timezone** | Analyses not comparable | State it always |
| **No cancel on long queries** | Users reload and lose state | Cancel control |
| **Charts with no data alternative** | Core content inaccessible | Data table |
| **Animated chart transitions** | Tax paid dozens of times per session | Instant updates |

### Spatial and map interfaces

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Inspector covering the selection** | User cannot see what they selected | Pan the canvas on open |
| **Translucent panels over imagery** | Unreadable text | Opaque panels |
| **Chrome occluding the canvas centre** | Working through a keyhole | ≤30% occlusion; edge-clustered controls |
| **Hidden attribution** | Licence violation | Always visible |
| **Silent feature truncation** | Conclusions from partial data | State the limit explicitly |
| **Topmost-wins on overlapping features** | Wrong feature inspected | Disambiguation list |
| **Whole-shape undo** | Lost work from one mis-click | Per-vertex undo |
| **Assumed units** | Real measurement errors | State and allow switching |
| **Instant 2D/3D cut** | Disorientation | 300–500ms camera transition |
| **Derived values shown as measured** | Misplaced confidence in costly decisions | Distinguish and label |
| **Map-only information** | Inaccessible by construction | List or table alternative |

### Developer tools

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Monospace for interface text** | Slower reading; removes the distinction that makes code read as code | Mono for code and identifiers only |
| **Wrapped code blocks** | Indentation semantics destroyed | Horizontal scroll |
| **Copy button without feedback** | Pressed repeatedly; user unsure it worked | Confirmed state ~2s |
| **Syntax colours failing contrast** | Comments and strings unreadable | Verify every token in both themes |
| **Test and live indistinguishable** | Destructive operations against production | Persistent labelled environment indicator |
| **`"string"` placeholder examples** | Examples do not run | Realistic, complete values |
| **Secrets revealed by default** | Shoulder-surfing and screenshot exposure | Mask; copy without reveal |
| **Log auto-scroll fighting the user** | Cannot read what scrolled past | Follow only when at the bottom |
| **Docs at marketing density** | Unscannable reference material | 48px rhythm, 680px measure |

---

## Part 3 — Process anti-patterns

Failures in how design work is produced rather than in the output.

| Anti-pattern | Harm | Correction |
|---|---|---|
| **Copying one brand's system wholesale** | Inherits an identity built for someone else's product, audience, and constraints | Adopt structural principles; derive your own values |
| **Averaging several systems** | Produces values none of the sources would accept — the mean of a 0px and 40px radius is 10px, which satisfies neither position | Choose a coherent position |
| **Picking a category by industry label** | Industry does not determine interaction needs | Derive category from tasks, frequency, and density |
| **Category without density** | Half an answer; the difference between usable and exhausting | Always pair category with a density mode |
| **Tokens defined but not consumed** | Hard-coded values drift immediately; the token file becomes decorative | Enforce in review; lint where possible |
| **Undocumented exceptions** | Indistinguishable from mistakes six months later | Record the reason in the project `DESIGN.md` |
| **Accessibility deferred to a later pass** | Structural fixes become expensive; usually never happens | Derive palette, sizing, and interaction with the constraints applied |
| **Design system with no states specified** | Every implementer invents their own | Specify all eight interaction states per component |
| **Visual redesign that replaces working code** | Regressions in functionality for a cosmetic gain | Restyle; do not rebuild. Preserve behaviour |
| **Trusting a source's self-assessed accessibility** | 56 corpus sources assert WCAG conformance; none demonstrates a computed ratio | Compute your own pairs |

---

## Part 4 — Using this guide in review

Fast pass, in priority order — these catch the majority of real problems:

1. **Contrast** — set the OS to greyscale. Is every status still distinguishable? Are secondary
   text and borders still visible?
2. **Keyboard** — complete one full task without a mouse. Is focus always visible? Any traps?
3. **States** — force empty, loading, error, and permission-denied. Are they designed?
4. **Mobile** — open at 375px. Is it re-ranked, or just compressed?
5. **Tokens** — search the diff for hex values, `px` in colours, and one-off spacing numbers.
6. **Consistency** — count button variants, card treatments, and radius values in use.
7. **Density coherence** — do spacing, control height, and type size agree on one density?
8. **Motion** — enable `prefers-reduced-motion`. Does everything still work and still communicate?

Category-specific checklists: [checklists/](checklists/).
