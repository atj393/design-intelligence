# Repository Discrepancy Report

Statements in the host repository that do not match the checkout, plus internal
inconsistencies within the source corpus. Every item below was verified against the working
tree at the time of writing — none is inferred from documentation.

**Nothing in this report was "fixed".** These are reported findings about someone else's
repository, and several plausibly reflect an upstream publishing process this checkout
cannot see. See [ASSUMPTIONS.md](ASSUMPTIONS.md) decision D-09.

**Verification context:** branch `main`, working tree clean apart from pre-existing
untracked `.vscode/` and `.remember/` directories.

---

## D1 — Preview files described in the README do not exist in the repository

**Severity: high** (it is the most likely thing to mislead a reader or an agent)

The root `README.md`, under *What's Inside Each DESIGN.md*, presents a table stating that
each site includes:

| File | Purpose |
|------|---------|
| `DESIGN.md` | The design system (what agents read) |
| `preview.html` | Visual catalog showing color swatches, type scale, buttons, cards |
| `preview-dark.html` | Same catalog with dark surfaces |

Verified: **zero** `preview.html` or `preview-dark.html` files exist anywhere in the
checkout.

```
$ find design-md -name 'preview*.html' | wc -l
0
```

`CONTRIBUTING.md` compounds this by instructing contributors to "Update the `preview.html`
and `preview-dark.html` if your changes affect displayed tokens" — a step that cannot be
performed in this repository.

The per-site stub READMEs point to the project website for "previews, dark mode examples,
and download options", which suggests the previews are a website feature that either never
shipped in-repo or was removed from it. Consumers of the derived layer should assume
**Markdown only**.

## D2 — Entry count is 74, not the 73 the README badge claims

**Severity: low. Resolved as a consequence of D3 — not an independent issue.**

- `design-md/` contains **74** directories, each with exactly one `DESIGN.md`.
- The README badge reads `DESIGN.md count-73`.
- The README's *Collection* section lists **73** entries across its ten category headings.

The badge and the visible list agree with each other and are both exactly one behind the
filesystem. There is no separate counting error: fix D3 and D2 closes with it.

## D3 — `design-md/slack/` is present but absent from the README collection

**Severity: low. RESOLVED: incomplete re-publication — an oversight in a re-add, not a
deliberate withholding.**

`design-md/slack/DESIGN.md` exists (25,011 bytes, 482 lines, well-formed, 10 `##` sections). It
is linked nowhere in the root README (`grep -ci slack README.md` → `0`), and it is the only
source directory **without** a stub `README.md`.

### Evidence trail

Git history resolves this. Five commits touch `design-md/slack/`:

| # | Commit | Action |
|---|---|---|
| 1 | `e2ada21` *update urls* | slack **added** — `DESIGN.md` (215 lines) + stub `README.md` (5 lines). Listed in the root README. |
| 2 | `3440bf2` *remove old link* | The slack **line removed from the root README** — a single-line deletion: `- [**Slack**](https://getdesign.md/slack/design-md) - Team communication platform…` |
| 3 | `da06867` *remove old entry* | The slack **folder deleted** — 220 deletions across `DESIGN.md` and `README.md`. |
| 4 | `beec066` *update DESIGN.md to v2* | `slack/DESIGN.md` **re-added at 482 lines** — more than double the original. This commit **also touched `README.md`**, but did not re-list slack and did not restore the stub. |
| 5 | `e06a966` *update design name* | One-line edit to `slack/DESIGN.md`. |

### Determination

**Steps 2 and 3 were a deliberate, complete removal** — link first, then folder. Clean and
intentional.

**Step 4 reversed the content removal but not the index removal.** The determination rests on
three points:

1. **Nobody re-adds a larger, upgraded v2 file for an entry they still want gone.** The re-added
   file is 482 lines against the original 215.
2. **The re-adding commit was already editing `README.md`.** The author had the index open in that
   very commit and simply did not add slack back — the signature of a bulk regeneration where one
   index line was missed, not of a decision.
3. **The altered brand spelling is not the explanation.** This file uses "Slacc", which one might
   read as trademark-driven withholding. But all six other altered-spelling files — `sentry`,
   `shopify`, `spacex`, `stripe`, `supabase`, `superhuman` — **are** listed. Altered spelling does
   not correlate with delisting; slack is the only one missing.

So the folder is not an orphan left behind by a deletion. It is a re-published entry whose index
line and stub README were never restored.

### Recommended fix (maintainers)

1. Restore the stub `design-md/slack/README.md`, matching the pattern of the other 73.
2. Re-add the collection line under *Productivity & SaaS*, in the pattern of its neighbours.
3. Update the badge to `DESIGN.md count-74` — which closes D2.

### Why this layer did not apply the fix

Both remaining actions depend on one fact this checkout cannot establish: **whether
`getdesign.md/slack/design-md` is live.** The stub README's only content is a redirect to that
URL, and the collection line links to it. If the page was taken down at step 2 and never
restored, applying either fix would publish a broken link into another project's public index —
worse than the current inconsistency. Verifying it requires fetching an external URL, which is
outside what this synthesis does.

The determination is now evidence-backed rather than a guess, which is what was missing. The
one check the maintainers can make and this layer cannot: load that URL.

## D4 — Source files do not all follow the format the README specifies

**Severity: high** (this one has direct consequences for anyone writing tooling against
the corpus)

The README states: "Every file follows the [Stitch DESIGN.md format] with extended
sections", and lists a 9-section structure — Visual Theme & Atmosphere, Color Palette &
Roles, Typography Rules, Component Stylings, Layout Principles, Depth & Elevation, Do's and
Don'ts, Responsive Behavior, Agent Prompt Guide.

**Only 10 of 74 files use that structure.** Grouping every file by its exact `##` heading
sequence yields five distinct document formats:

| Files | Sections | Structure | Frontmatter |
|-------|----------|-----------|-------------|
| **42** | 11 | Overview · Colors · Typography · Layout · Elevation & Depth · Shapes · Components · Do's and Don'ts · Responsive Behavior · Iteration Guide · Known Gaps | YAML |
| **13** | 8 | as above, minus Responsive Behavior / Iteration Guide / Known Gaps (responsive appears as an `###` inside Layout) | YAML |
| **10** | 9 | The README's numbered Stitch format | **none** — opens `# Design System Inspired by …` |
| **8** | 10 | The 11-section format minus Known Gaps | YAML |
| **1** | 8 | Overview · Colors · Typography · Layout · **Elevation** · Components · Responsive Behavior · Known Gaps (`design-md/airbnb/`) | YAML |

Practical consequences:

- 64 files carry a machine-readable YAML frontmatter block with `colors`, `typography`,
  `rounded`, `spacing`, and `components` keys. **10 files carry no frontmatter at all** —
  any parser that assumes it will fail on them.
- `Do's and Don'ts` is the most consistent section, present in 73 of 74 files. The
  exception is `design-md/airbnb/DESIGN.md`. Guardrails are the corpus's most reliable
  seam.
- `Known Gaps` exists in only 43 files, and `Iteration Guide` in 50.
- The README's promised *Agent Prompt Guide* section exists in **10** files — the same 10
  that use the Stitch format. The dominant format has no agent-prompt section.

## D5 — Corpus depth varies by more than an order of magnitude

**Severity: medium** — it makes cross-source comparison uneven, which is a real limit on
any synthesis including this one.

| | File | Size |
|---|------|------|
| Largest | `design-md/mintlify/DESIGN.md` | 44,935 bytes / 852 lines |
| Smallest | `design-md/kraken/DESIGN.md` | 4,475 bytes / 125 lines |

`design-md/kraken/DESIGN.md` is a genuine outlier at roughly one-tenth the corpus median.
It is the only file in its structural group of one, and it omits several sections its
neighbours carry. Comparisons involving it are correspondingly weak, and it was excluded
from distribution counts where it has no value to contribute.

## D6 — Files reference tooling and scripts that do not exist in this repository

**Severity: medium**

- **34 files** instruct the reader to run `npx @google/design.md lint DESIGN.md`, typically
  as a step in their `Iteration Guide`. That is a third-party package; nothing in this
  repository provides, pins, or documents it. There is no `package.json` anywhere in the
  checkout.
- **12 files** attribute their example blocks to `scripts/derive-examples-block.mjs`. No
  `scripts/` directory and no `.mjs` file exists in the repository.

An agent following these instructions literally will fail. Treat both as vestigial
references to an upstream authoring pipeline.

## D7 — Thirteen files contain auto-generated, non-observed component blocks

**Severity: high for anyone mining the corpus for application-UI patterns**

Thirteen files carry an `### Examples (illustrative)` subsection whose own preamble reads:
"Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`) …
`TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass."

Affected: `dell-1996`, `nintendo-2001`, `together.ai`, `uber`, `vercel`, `vodafone`,
`voltagent`, `warp`, `webflow`, `wired`, `wise`, `x.ai`, `zapier`.

These blocks define exactly the application-surface components a synthesis effort most
wants — `ex-data-table-cell`, `ex-app-shell-row`, `ex-modal-card`, `ex-toast`,
`ex-empty-state-card`, `ex-auth-form-card`, `ex-cart-drawer`, `ex-pricing-tier`. They are
**machine extrapolations from marketing primitives, not observations of a real interface**.
One entry says so outright: `ex-cart-drawer` is described as a "Subscription summary —
re-purposed for SaaS / B2B (line items per add-on, not literal cart)."

Each of the 13 files also still contains 2 unresolved `TO_FILL` markers.

This derived layer does **not** treat these blocks as evidence of how application UI is
built. It cites them only as evidence that *re-skinning a marketing token set onto app
surfaces is a recognised operation* — which is a genuinely useful, and much narrower,
finding.

## D8 — Brand naming is inconsistent, including deliberate misspellings

**Severity: low as a design matter, non-trivial as a trademark matter** — see
[LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md).

Twenty files open with "An inspired interpretation of X's design language". Within that
group, some name the brand accurately (`Uber`, `Vercel`, `Zapier`, `Wired`, `HP`) while
others use a visibly altered spelling:

| File | Spelling used |
|------|---------------|
| `design-md/sentry/DESIGN.md` | "Sentri" |
| `design-md/shopify/DESIGN.md` | "Shopifi" |
| `design-md/slack/DESIGN.md` | "Slacc" |
| `design-md/spacex/DESIGN.md` | "Spasex" |
| `design-md/stripe/DESIGN.md` | "Stripi" |
| `design-md/supabase/DESIGN.md` | "Supabaze" |
| `design-md/superhuman/DESIGN.md` | "Superhumon" |

The altered spellings appear to be trademark distancing. Applied to 7 files while 13
neighbours in the same phrasing group use real names, the effect is inconsistent rather
than protective — and the directory names, file links, and typeface names are unaltered in
all cases. Worth a maintainer decision one way or the other.

## D9 — Accessibility conformance is asserted but not demonstrated

**Severity: medium**

56 files reference WCAG, contrast ratios, or specific ratio thresholds. Of those, **35
assert WCAG AAA** and **13 assert WCAG AA**. No file in the corpus shows a computed ratio
for a specific foreground/background token pair.

AAA requires 7:1 for normal-size text. That is a demanding threshold, and several
documented palettes pair mid-grey muted text against tinted canvases in ways that make a
blanket AAA claim implausible without per-pair computation.

These ratios were **not** recomputed during this work — doing so properly means resolving
every semantic token pair per mode across 74 systems. Consequence for the derived layer:
accessibility floors in [COMMON-FOUNDATION.md](COMMON-FOUNDATION.md) are taken from the
WCAG specification directly, and no source's self-assessment is inherited. Recorded as a
source limitation in [VALIDATION-REPORT.md](VALIDATION-REPORT.md).

## D10 — Terminology for the same concept varies across files

**Severity: low individually, cumulatively the main obstacle to comparison**

No file is wrong; there is simply no enforced vocabulary. Examples:

| Concept | Names observed |
|---------|----------------|
| Page background | `canvas`, `canvas-soft`, `canvas-dark`, `surface`, `bg`, `base` |
| Primary text | `ink`, `body`, `body-strong`, `ink-deep`, `text` |
| Secondary text | `muted`, `mute`, `ink-muted`, `ink-mute`, `ink-subtle`, `muted-soft`, `on-dark-soft` |
| Hairline border | `hairline`, `hairline-soft`, `hairline-strong`, `border-strong`, `divider-soft` |
| Largest display size | `display-xl`, `display-xxl`, `display-mega`, `hero-display`, `display-hero`, `display-campaign` |
| Scale steps | `xxs…xxl`, `xs…3xl`, `xxxs…super`, `hair/xxs…hero`, `sm/md/huge` |

Some files also diverge structurally: 8 place `Border Radius Scale` under `Layout` rather
than under `Shapes`.

The derived layer normalizes to one vocabulary — see
[research/PATTERN-MATRIX.md](research/PATTERN-MATRIX.md) for the mapping table used, and
[COMMON-FOUNDATION.md](COMMON-FOUNDATION.md) for the canonical names it publishes.

---

## Aggregate

| Finding | Count | Verification |
|---------|-------|--------------|
| Source directories | 74 | `ls -d design-md/*/ \| wc -l` |
| Directories with `DESIGN.md` | 74 | one per directory |
| Directories with stub `README.md` | 73 | `slack` missing |
| Preview HTML files | 0 | README claims 2 per site |
| Distinct document structures | 5 | README describes 1 |
| Files with YAML frontmatter | 64 | 10 without |
| Files with `Do's and Don'ts` | 73 | most consistent section |
| Files with `Known Gaps` | 43 | |
| Files with `Agent Prompt Guide` | 10 | README implies all |
| Files with auto-generated example blocks | 13 | contain `TO_FILL` |
| Files referencing absent tooling | 34 | `npx @google/design.md` |

## What none of this changes

The corpus is a substantive, unusually detailed body of design documentation, and the
discrepancies above are mostly index-drift and format evolution rather than defects in the
analysis it contains. This report exists so the derived layer can state what it is standing
on, and so that anyone building tooling against the corpus does not assume a uniformity
that is not there.
