# Progress Log

Working document for the derived design intelligence layer. Updated at the end of each
waterfall phase. This is a build log, not a design document — read
[README.md](README.md) for what the layer actually contains.

**Status:** All 12 build phases complete, plus a Phase 13 follow-up (below) that acted on the
completion report's own recommendations.
**Location decision:** the derived layer lives in `design-intelligence/` (hyphenated, no
space) because a space in a top-level repository path breaks common tooling paths, shell
invocations, and Markdown relative links. The instruction named the folder "design
intelligence"; the hyphenated form is the same name in a filesystem-safe spelling.

---

## Phase status

| # | Phase | Status | Primary artifacts |
|---|-------|--------|-------------------|
| 1 | Repository safety | Complete | `PROGRESS.md`, `ASSUMPTIONS.md`, `METHODOLOGY.md` |
| 2 | Repository inventory | Complete | `SOURCE-INVENTORY.md`, `research/CATEGORY-INVENTORY.md`, `REPOSITORY-DISCREPANCIES.md` |
| 3 | Pattern extraction | Complete | `research/PATTERN-MATRIX.md`, `research/VALUE-DISTRIBUTIONS.md`, `research/PATTERN-CLUSTERS.md` |
| 4 | Common foundation | Complete | `COMMON-FOUNDATION.md`, `templates/DESIGN.foundation.md` |
| 5 | Category taxonomy + selection | Complete | `CATEGORY-SELECTION.md`, `CATEGORY-COMPARISON.md` |
| 6 | Category guides | Complete | `categories/` (11 guides) |
| 7 | Design logic + anti-patterns | Complete | `DESIGN-DECISION-HANDBOOK.md`, `ANTI-PATTERNS.md` |
| 8 | AI agent usage | Complete | `AI-AGENT-GUIDE.md`, `prompts/` (12 prompts) |
| 9 | Templates + checklists + init | Complete | `templates/` (11), `checklists/` (5), `PROJECT-INITIALIZATION.md` |
| 10 | Validation | Complete | `VALIDATION-REPORT.md` |
| 11 | Publication preparation | Complete | `README.md`, `SOURCES.md`, `ATTRIBUTION.md`, `LICENSING-CONSIDERATIONS.md`, `PUBLISHING-CHECKLIST.md` |
| 12 | Final audit | Complete | Completion report delivered in session; `research/TRACEABILITY.md` |

---

## Phase 1 — Repository safety

**Verified before writing anything:**

- Working directory: the repository root, branch `main`, clean except one pre-existing untracked
  editor directory (`.vscode/`) plus an untracked tool directory (`.remember/`). Neither belongs
  to this task; both were left untouched.
- Read in full or in substantial part: `README.md`, `CONTRIBUTING.md`, `LICENSE`,
  `.gitignore`, `.github/FUNDING.yml`, `.github/ISSUE_TEMPLATE/design-md-request.yml`, and
  representative `DESIGN.md` files across every structural variant.
- License is MIT, copyright "VoltAgent" (2026). This matters for
  [LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md) — MIT covers the repository
  text, not the third-party trademarks the text describes.
- Confirmed there is no build system, no `package.json`, no scripts directory. The
  repository is pure Markdown content. No tooling was added.

**Decisions recorded:** see [ASSUMPTIONS.md](ASSUMPTIONS.md).

**Files touched outside `design-intelligence/`:** one — a short pointer section appended
to the root `README.md`. Justified in ASSUMPTIONS.md decision D-08. No file under
`design-md/` was created, deleted, renamed, or edited.

---

## Phase 2 — Repository inventory

Inventory was built by direct filesystem and file-content inspection, not from the root
README's descriptions. Throwaway extraction scripts ran from the session scratchpad and
were deliberately **not** committed into the repository; their outputs are transcribed
into `research/`.

**Headline counts (verified):**

- 74 source directories under `design-md/`, each containing exactly one `DESIGN.md`.
- 73 stub `README.md` files — `design-md/slack/` has none.
- 0 `preview.html` / `preview-dark.html` files anywhere in the checkout.
- 5 distinct document structures, not the single format the root README describes.

**Unresolved at end of phase, carried forward:** whether the root README's omission of one entry
was intentional or an oversight. Recorded as a discrepancy rather than "fixed", since fixing it
would have meant editing a source-of-truth file on a guess.

**Resolved in Phase 13** via git history — see
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D3.

---

## Phase 3 — Pattern extraction

Extraction covered YAML frontmatter token blocks (64 files), Markdown hierarchy tables,
and section-scoped narrative text. Values were tagged explicit / inferred / unavailable
rather than defaulted to zero.

**Key decision:** numeric guidance in the derived layer is expressed as *modal value plus
observed range*, never as a single average. Averaging a 4px-radius enterprise system with
a 40px-radius consumer-payments system produces a number no source actually uses.

**Most consequential finding:** the corpus documents **public marketing and brand
surfaces**. The `Known Gaps` sections say so repeatedly and explicitly — authenticated
product chrome, dashboards, form-validation states, and hover states are documented as out
of scope in the majority of files that have a gaps section. This bounds what the derived
layer can claim as evidence-backed, and it is the single most important input to
[VALIDATION-REPORT.md](VALIDATION-REPORT.md).

---

## Phase 4 — Common foundation

Built from cross-category convergence only. Where the corpus converges hard (breakpoints,
touch targets, section rhythm, base unit, body size) the foundation states a default and
cites the distribution. Where it splits into genuinely incompatible schools (radius
character, display weight, canvas polarity) the foundation refuses to pick a winner and
instead gives a decision rule.

Primitive/semantic token separation is a **synthesized** structural recommendation. The
corpus supports it indirectly — 64 files use `{colors.x}` reference syntax and role-named
tokens like `on-primary`, `hairline`, `canvas` — but no source file states the two-layer
model as a rule. Labelled accordingly.

---

## Phase 5 — Category taxonomy and selection

Twelve candidate categories were evaluated. Outcome:

- **11 guides written.** Content/editorial and data-analytics were kept separate from
  general-website and dashboard respectively, because their layout and density logic
  diverge materially.
- **Mobile-first was merged**, not given its own guide. The corpus contains no
  mobile-native evidence (responsive behavior is frequently synthesized *by the source
  authors*, per their own gaps sections), so a standalone mobile guide would have been
  invention dressed as synthesis. Mobile logic instead lives as a required dimension in
  every category guide plus a dedicated section in the decision handbook. Recorded as
  decision D-05.
- Marketing and general informational websites were **split**, as instructed, and the
  split is defensible from the evidence: the corpus's conversion-oriented sources and its
  documentation-oriented sources use measurably different type scales and section rhythms.

---

## Phase 6 — Category guides

Each guide carries a `Source inspiration` section naming real relative paths, and an
`Evidence strength` banner stating whether its guidance is corpus-backed or synthesized.
Three guides are explicitly flagged as predominantly synthesized: conversational AI,
dashboard/administration, and spatial. Writing those without the flag would have been the
most likely failure mode of this whole task.

---

## Phase 7 — Design logic and anti-patterns

The handbook encodes derivation rules (requirement → design decision) rather than style
preferences. The anti-pattern guide's AI-generated-design section is drawn from the
corpus's own `Don't` lists — 73 files carry one, which turned out to be the richest
evidence seam in the entire repository for this purpose.

---

## Phase 8 — AI agent usage

Twelve prompts written as specified. Every prompt includes an inspect-before-you-generate
step, a do-not-break-working-functionality constraint, and a required deviations report.
Reading order is fixed: project context → foundation → primary category → supporting
category → project `DESIGN.md`.

---

## Phase 9 — Templates, checklists, initialization

Eleven templates on one shared skeleton, five review checklists, one initialization guide
with a worked hybrid-platform example. Templates state defaults and mark customization
points with `[[CHOOSE: ...]]` and `[[SET: ...]]` markers so an agent can tell a
recommendation from a placeholder.

---

## Phase 10 — Validation

See [VALIDATION-REPORT.md](VALIDATION-REPORT.md). Checks run: numeric coherence of every
published scale, cross-reference link integrity, source-path existence, brand-specific
claims not promoted to universal, dark mode not presented as inversion, accessibility and
interaction states present in all templates, recommendations vs. anti-patterns present in
all category guides.

Two internal inconsistencies were found and fixed during this phase rather than shipped:
an early draft of the foundation quoted a 1280px content width as universal (it is modal,
not universal — 1200px and 1440px are both well represented), and an early conversational
AI draft specified a 44px input height that contradicted the foundation's own comfortable
control height. Both corrected.

---

## Phase 11 — Publication preparation

License inspected before licensing guidance was written. No brand assets, logos, or
screenshots were copied into the derived layer. No remote was created, nothing was pushed,
nothing was committed — the instruction did not authorize it and neither did the session.

---

## Phase 12 — Final audit

`git status` and `git diff --stat` confirmed: no file under `design-md/` modified, added,
deleted, or renamed; all 74 source directories present; the only tracked change outside
`design-intelligence/` is the root README pointer. Full completion report delivered in the
session response.

---

## Phase 13 — Acting on the completion report's recommendations

The Phase 12 report ended with five recommended next steps. All five were then executed. This
phase is the reason the layer's numbers changed after "completion", and it materially altered two
files' contents.

### 13.1 — Root README addition reviewed

**Outcome: kept, revised.** The review found a defect in the addition itself — it stated the
collection contains "74 established products", which **contradicts the `count-73` badge on the
same page**. Also shortened the heading (`## Design Intelligence`) to match the surrounding
heading style, and dropped one table row. Net addition now 16 lines, additive only.

### 13.2 — Slack discrepancy resolved

**Outcome: determined to be an incomplete re-publication, not a deliberate withholding.** Git
history produced a five-commit trail: added and listed → delisted → folder deleted → `DESIGN.md`
re-added at 482 lines (v2, more than double the original) in a commit that touched `README.md`
without re-listing it. Nobody re-adds a larger v2 of something they want removed.

The fix was **not applied**, for one specific reason: both remaining actions publish a link to an
external URL whose liveness this checkout cannot verify. Full evidence trail and the one-line
check the maintainers can make: [REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D3.
D2 closed as a consequence.

### 13.3 — Dashboard template build-tested

**Outcome: 10 defects found, including 2 self-contradictions the template could not satisfy. All
fixed.** An operator dashboard was built strictly from the template, rendered in a real browser,
and measured.

The two critical self-contradictions:

- **Sticky budget was arithmetically impossible.** The template declared a 20% viewport budget and
  separately specified heights summing to 196px = 22.8% at 860px viewport height.
- **The dark-mode rule contradicted the contrast floor.** "Lighten saturated colours" plus "filled
  buttons use white labels" measured **3.68:1** and **2.92:1** — following the template correctly
  produced two accessibility failures.

Plus: density modes did not control density (100% of rows exceeded declared height in all three
modes), the responsive table omitted the page header and toolbar, and the touch guard was a single
point of failure (26 sub-44px targets at 375px).

Fixes propagated to `templates/DESIGN.dashboard-admin.md`,
`templates/DESIGN.foundation.md`, `COMMON-FOUNDATION.md` §6, and
`checklists/foundation-review.md`. Full report:
[research/TEMPLATE-VALIDATION.md](research/TEMPLATE-VALIDATION.md).

### 13.4 — Weak-evidence guides adversarially reviewed

**Outcome: 6 findings, all fixed — but this is not the user validation that was recommended.**
User testing was not possible; claiming it happened would defeat the purpose of the evidence
banners. An adversarial pass was run instead and is labelled as a substitute of lesser value.

Findings included three rules stated too absolutely (never-bubble, never-zebra-stripe,
panels-must-be-opaque), one unresolvable tension presented as resolved (prose measure vs. code
width), one security under-qualification (disable-and-explain discloses capability), and two
invented thresholds presented as rules.

An executable 6-participant-per-guide validation protocol was written for the user testing that
still needs doing: [research/WEAK-GUIDE-REVIEW.md](research/WEAK-GUIDE-REVIEW.md).

### 13.5 — Publishing checklist executed

**Outcome: passes every automatable check; not published.** 0 broken links (324 checked), 0 binary
assets, 0 non-Markdown files, 0 unresolved markers outside `templates/`, 0 TODO markers, all 11
evidence banners present, all 5 folder READMEs present. Two real fixes applied: an absolute local
path in this file, and a stale "unresolved" note about the slack entry.

Nothing was published, pushed, or committed. No remote was created.

### Files changed in Phase 13

| File | Change |
|---|---|
| `README.md` (root) | Addition revised — count conflict removed, heading shortened |
| `REPOSITORY-DISCREPANCIES.md` | D2 and D3 resolved with evidence trail |
| `templates/DESIGN.dashboard-admin.md` | 8 defect fixes: column policy, sticky budget, dark tokens, z-index, toast, skeleton, responsive rows, card anatomy |
| `templates/DESIGN.foundation.md` | Dark-mode action token split |
| `COMMON-FOUNDATION.md` | §6 dark-mode contradiction resolved |
| `checklists/foundation-review.md` | Contrast rule precision; filled-button check added |
| `categories/conversational-ai.md` | A-01, A-02 qualifications |
| `categories/dashboard-admin.md` | A-03 qualification |
| `categories/commercial-multi-role-platform.md` | A-05 security qualification |
| `categories/spatial-map-3d.md` | A-04 restatement; occlusion budget labelled synthesized |
| `research/TEMPLATE-VALIDATION.md` | New |
| `research/WEAK-GUIDE-REVIEW.md` | New |
| `PROGRESS.md`, `VALIDATION-REPORT.md` | Updated with Phase 13 findings |
