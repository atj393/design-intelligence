# Research

The analysis the guidance was built from. Read these to check a claim, argue with a conclusion, or
re-run the extraction.

Nothing here is guidance. These are findings.

---

| File | Contents |
|---|---|
| [CATEGORY-INVENTORY.md](CATEGORY-INVENTORY.md) | Category rollups, tone clusters, and **evidence strength per derived category** |
| [PATTERN-MATRIX.md](PATTERN-MATRIX.md) | Vocabulary normalization map, extraction coverage per dimension, per-source structural matrix, deliberate absences |
| [VALUE-DISTRIBUTIONS.md](VALUE-DISTRIBUTIONS.md) | Observed numeric distributions — spacing, radius, type, breakpoints, widths, targets, colour |
| [PATTERN-CLUSTERS.md](PATTERN-CLUSTERS.md) | Co-occurring decision sets, reliable correlations, incompatible combinations, documented disagreements |
| [TRACEABILITY.md](TRACEABILITY.md) | Which sources support which recommendation, and **which have no source at all** |

## Reading order

1. **[CATEGORY-INVENTORY.md](CATEGORY-INVENTORY.md) §3** first. It is the table that determines how
   much to trust everything else: four requested categories have zero direct sources.
2. **[VALUE-DISTRIBUTIONS.md](VALUE-DISTRIBUTIONS.md)** for the numbers, remembering the population
   is ~90% marketing websites.
3. **[PATTERN-CLUSTERS.md](PATTERN-CLUSTERS.md)** for why values travel together — more useful than
   any single distribution.
4. **[TRACEABILITY.md](TRACEABILITY.md)** to audit a specific claim.
5. **[PATTERN-MATRIX.md](PATTERN-MATRIX.md)** when you need the normalization mapping or want to see
   what the corpus could not answer.

## Two things to keep in mind

**A distribution is not a recommendation.** 61 of 74 sources use 96px section rhythm. That is a fact
about marketing websites. Transplanted into an all-day operations tool it becomes a scroll cost paid
forty times a day. Frequency is always reported with its population attached; see
[../ASSUMPTIONS.md](../ASSUMPTIONS.md) D-04.

**Absence is recorded as absence, never as zero.** A file publishing a radius scale of `0px` and
`9999px` only is stating an editorial position. A file with no radius data is missing data. Collapsing
the two would fabricate a design opinion. The deliberate absences are catalogued in
[PATTERN-MATRIX.md](PATTERN-MATRIX.md) §4.

## Method

Extraction technique, confidence tagging, and pattern classification:
[../METHODOLOGY.md](../METHODOLOGY.md).

Extraction ran from a session scratchpad and was **not committed** — the host repository is Markdown
content and should not acquire a script directory as a side effect
([../ASSUMPTIONS.md](../ASSUMPTIONS.md) D-10). Two runnable re-derivation examples are in
METHODOLOGY.md §7; the distributions here can be reproduced from the corpus directly.

## The single most important finding

The corpus documents **public marketing and brand surfaces**. Its own `Known Gaps` sections say so —
authenticated product chrome, dashboards, hover states, and form-validation states are repeatedly
listed as out of scope by the source authors themselves.

Consequence: token, typography, spacing, elevation, and layout guidance rests on strong evidence.
Dashboard, conversational, multi-role, and spatial guidance is **reasoning**. Both are useful. Only
one is evidence, and every affected guide says which it is at the top of the file.
