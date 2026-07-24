# Assumptions and Decisions

Decisions taken without asking, and the reasoning behind each. Anything here can be
overturned — the point of writing them down is that overturning them is cheap and
informed rather than expensive and blind.

---

### D-01 — Folder name is `design-intelligence`, not `design intelligence`

A space in a top-level repository path breaks relative Markdown links in some renderers,
requires quoting in every shell invocation, and is inconsistent with the existing
`design-md/` directory. Hyphenated is the same name, spelled safely.

### D-02 — The source corpus is treated as evidence of *marketing surface* design

This is the single most consequential judgment in the whole layer, so it is stated
plainly. The corpus does not document application interfaces. Its own `Known Gaps`
sections repeatedly say the opposite of what a casual reader might assume:

- "In-product app chrome … not in the captured set — the marketing site is documented
  here, not the in-product analytics interface." (`design-md/posthog/DESIGN.md`)
- "The in-product app surface is its own design system." (`design-md/raycast/DESIGN.md`)
- "Logged-in dashboard surfaces … are out of scope; only the public marketing canvas is
  documented." (`design-md/resend/DESIGN.md`)
- "The MyRenault application surfaces (logged-in product) are out of scope."
  (`design-md/renault/DESIGN.md`)

Consequence: token-level, typographic, and structural guidance is well supported by this
corpus. Application-interaction guidance — dashboards, chat, maps, role-based workspaces —
is *not*, and every guide that covers those says so in its own evidence banner. See
[VALIDATION-REPORT.md](VALIDATION-REPORT.md).

### D-03 — Numeric guidance is modal-plus-range, never an average

The corpus spans a 0px-radius enterprise system and a 40px-radius payments brand. Their
mean is a value neither uses and neither would accept. Every dimension in
[COMMON-FOUNDATION.md](COMMON-FOUNDATION.md) therefore ships as *default / compact /
spacious*, with the observed distribution recorded in
[research/VALUE-DISTRIBUTIONS.md](research/VALUE-DISTRIBUTIONS.md).

### D-04 — Frequency is reported as frequency, not as endorsement

That 61 of 74 files place major section spacing at 96px is a fact about a corpus of
marketing sites. It is not evidence that 96px is correct for an operations console, where
that much vertical air costs the user scroll on every visit. Frequency data is presented
with its population attached.

### D-05 — Mobile-first is a dimension, not a standalone category guide

The instruction listed mobile-first among candidate categories and permitted merging where
evidence is insufficient. It is insufficient here in an unusually specific way: the source
files *themselves* flag their responsive guidance as synthesized — "Mobile screenshots not
captured — responsive behavior synthesizes … from desktop evidence and the breakpoint
stack" appears verbatim across many files. Building a mobile-native guide on top of
already-synthesized responsive claims would stack invention on invention. Mobile logic is
instead mandatory in every category guide and gets a full section in
[DESIGN-DECISION-HANDBOOK.md](DESIGN-DECISION-HANDBOOK.md).

### D-06 — Checklists live in `checklists/`, a folder the prescribed structure did not name

The documentation architecture named `categories/`, `templates/`, `prompts/`, `research/`.
Review checklists were required deliverables with no named home. Inlining five checklists
into their guides would have made the guides harder to use as a review instrument — a
reviewer wants a page they can work down. Separate folder, cross-linked both ways.

### D-07 — Category assignment reads the file, then the brand

Categories were assigned from each file's own description and component vocabulary, not
from what the company sells. A payments company whose documented surface is an editorial
marketing page is primary-category *marketing website*, secondary *financial / high
trust*. Recorded per source in
[research/CATEGORY-INVENTORY.md](research/CATEGORY-INVENTORY.md).

### D-08 — One root file was modified: a pointer added to `README.md`

The instruction allowed "a small root README update … later justified". A derived layer
nobody can find has no value, and the root README is the only discovery surface this
repository has. The change is additive — one section, no existing line edited, no existing
claim altered, no restructuring. Everything else outside `design-intelligence/` is
untouched. If this is unwanted it reverts with `git checkout README.md`.

### D-09 — Documented discrepancies are *reported*, not repaired

The root README undercounts entries and describes preview files that do not exist. Both
are confirmed. Neither was edited, because both plausibly reflect an upstream publishing
process this checkout cannot see — the previews are live on the project's website, and the
unlisted entry may be unreleased. Reporting is correct here; silently rewriting another
project's index on an inference is not. See
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md).

### D-10 — Extraction scripts were not committed

Three throwaway Python scripts drove the quantitative analysis. They ran from a session
scratchpad. The instruction said not to build software for this task, and a repository of
Markdown design documents should not acquire a script directory as a side effect. Their
method is documented in [METHODOLOGY.md](METHODOLOGY.md) and their findings transcribed
into `research/` so results are reproducible without them.

### D-11 — No brand names in derived recommendations, only in source citations

Brand names appear in `Source inspiration` sections and in
[research/](research/) traceability tables. They do not appear in normative guidance. A
rule that reads "use the four-step surface ladder approach" is portable; one that reads
"do it like Brand X" invites literal copying and implies an endorsement that does not
exist.

### D-12 — Contrast claims in the corpus are treated as unverified

56 files reference WCAG or contrast ratios; 35 assert AAA and 13 assert AA. Those ratios
were not recomputed from the hex values during this work. The derived layer therefore sets
its own accessibility floor from the WCAG specification rather than inheriting any source's
self-assessment. Flagged as a source limitation in the validation report.
