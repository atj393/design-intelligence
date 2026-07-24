# Sources

What this layer was derived from, and how to check any claim in it.

---

## Primary source

**The `design-md/` collection in this repository** — 74 `DESIGN.md` files documenting the design
languages of established websites and digital products.

| | |
|---|---|
| Location | [`design-md/`](../design-md/) |
| Host project | [Awesome DESIGN.md](../README.md) |
| Publisher | VoltAgent |
| Repository licence | MIT ([`LICENSE`](../LICENSE)) |
| Files used | All 74 |
| Read directly | Yes — not summarised from the collection's README |

**This is the only substantive source.** No other design system, style guide, or published
methodology was used as a source of specific values.

## Secondary references

Used for the accessibility floor and for named specification criteria, not for design values:

| Reference | Used for |
|---|---|
| WCAG 2.2 (W3C) | Contrast thresholds, focus visibility, target size, error prevention (3.3.4), timing (2.2.1), colour independence (1.4.1) |
| The `DESIGN.md` concept | Named in the host README as originating with Google Stitch. Referenced as context, not quoted |

Where guidance comes from general interface-design practice rather than either of the above, it is
labelled **synthesized** inline and carries its reasoning so it can be evaluated on the argument.

## What was not used

Stated explicitly, because absence matters for judging the work:

- **No live-site verification.** Whether a source's documented hex value still matches the live
  website today was not checked.
- **No recomputed contrast ratios.** 56 source files assert WCAG conformance; none demonstrates a
  computed pair. This layer sets its own floor from the specification rather than inheriting any
  source's self-assessment.
- **No brand assets.** No logo, screenshot, font file, image, or trademarked material was copied
  into this layer.
- **No other design-system documentation.** Not Material, not Carbon, not HIG, not any published
  design system. One source file (`design-md/ibm/DESIGN.md`) references a public design system in
  its own description; that reference was read as part of that file, not consulted separately.
- **No preview files.** The host README describes per-site `preview.html` and `preview-dark.html`
  files. **Zero exist in this checkout.** See
  [REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D1.

## Traceability

Three levels, so any claim can be traced back:

| Level | Where |
|---|---|
| **Per-source** — what each file documents and contributes | [SOURCE-INVENTORY.md](SOURCE-INVENTORY.md) |
| **Per-recommendation** — which sources support which claim | [research/TRACEABILITY.md](research/TRACEABILITY.md) |
| **Per-category** — the `Source inspiration` section in each guide | [categories/](categories/) |

Every source path cited in this layer was verified to exist at the time of writing: **123 distinct
citations, all resolving; all 74 source directories cited by explicit path at least once.**

## Verification method

How the quantitative claims were produced, in enough detail to reproduce them:
[METHODOLOGY.md](METHODOLOGY.md).

Distributions were extracted with **section-scoped** parsing rather than document-wide regex,
because a naive search finds `9999` from the pill-radius table and reports it as a breakpoint. Two
runnable re-derivation examples are in METHODOLOGY.md §7.

Extraction scripts ran from a session scratchpad and were deliberately not committed — the host
repository is Markdown content and should not acquire a script directory as a side effect
([ASSUMPTIONS.md](ASSUMPTIONS.md) D-10). Their outputs are transcribed into
[research/](research/).

## Citation style used here

Sources are cited by **relative repository path and section**, for example:

> `design-md/linear.app/DESIGN.md` § *Elevation & Depth*

This is verifiable in the checkout and survives any reorganisation of the collection's website.

**Sources are cited as evidence of technique, never as templates.** The distinction runs through
the whole layer: guides say *adopt the surface-ladder approach* or *use the density model*, never
*look like Brand X*. See [ATTRIBUTION.md](ATTRIBUTION.md).

## Source quality notes

Facts about the corpus that affect how much weight any given citation carries. Full detail in
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md).

| Note | Consequence for this layer |
|---|---|
| 5 distinct document formats, not the 1 the README describes | Cross-source comparison required vocabulary normalization ([research/PATTERN-MATRIX.md](research/PATTERN-MATRIX.md) §1) |
| 10 of 74 files have no machine-readable frontmatter | Token-level analysis covers 64 files, not 74 |
| File depth ranges from 4.5 KB to 45 KB | The thinnest source contributes little; comparisons involving it are weak |
| 43 of 74 files carry a `Known Gaps` section | These are the corpus's most valuable content for calibration — they state what was *not* observed |
| 13 files contain machine-generated app-UI component blocks | **Not treated as evidence.** They are extrapolations from marketing primitives, and two `TO_FILL` markers remain in each |
| ~90% of files document marketing surfaces only | Bounds four category guides to reasoning rather than evidence |
| 7 files use deliberately altered brand spellings | Noted as a trademark-handling inconsistency in the source, not corrected here |
| 34 files reference tooling absent from the repository | Vestigial references to an upstream pipeline; not actionable |

## If you are auditing a specific claim

1. Find the recommendation in a guide or the foundation.
2. Check its `Source inspiration` section (category guides) or
   [research/TRACEABILITY.md](research/TRACEABILITY.md) for the supporting sources.
3. Open the cited file at the cited section.
4. If the claim is labelled **synthesized**, there is no source to check — evaluate the stated
   reasoning instead. That labelling is deliberate and load-bearing.
