# Attribution

---

## This is derived work

This layer is a **synthesis of** the [`design-md/`](../design-md/) collection in this repository. It
does not replace, supersede, or reproduce that collection — it reads it and draws conclusions from
it.

Without the collection, this layer could not exist. The 74 source analyses represent substantial
original work: reading real websites closely and documenting their design languages in consistent,
machine-readable detail. That documentation is the raw material here.

**Credit for the source collection:** the [Awesome DESIGN.md](../README.md) project, published by
VoltAgent, and its contributors.

## What this layer added

| Contribution | Description |
|---|---|
| Cross-source analysis | Value distributions, co-occurrence clusters, documented disagreements |
| Category taxonomy | Eleven product categories organised by interaction need, not industry |
| Common foundation | General scales and token architecture, with alternatives and decision rules |
| Decision framework | 23 discovery questions, a decision tree, a recommendation model |
| Templates | Eleven `DESIGN.md` templates on a shared skeleton |
| Agent instructions | Reading order, twelve prompts, required reporting format |
| Checklists | Five review instruments |
| Evidence calibration | Explicit strength banners, and honest gap reporting |

## What this layer did not do

- **Did not modify the source collection.** No file under `design-md/` was created, changed,
  renamed, or deleted.
- **Did not copy source text.** Passages were not lifted. Short quotations appear only where a
  source's own words establish a limitation, and are attributed inline.
- **Did not copy brand assets.** No logos, screenshots, font files, images, or trademarked material.
- **Did not reproduce any brand's design system** as a usable artefact.

---

## No affiliation or endorsement

**This layer is not affiliated with, endorsed by, sponsored by, or approved by any brand,
company, product, or organisation referenced in the source research.**

Brand names appear in exactly two places:

1. **Source citations** — identifying which file a finding came from, e.g.
   `design-md/linear.app/DESIGN.md` § *Elevation & Depth*
2. **Research tables** — inventory and traceability records

Brand names do **not** appear in normative guidance. Every rule in this layer is written to be
portable: *"use a four-step surface ladder with hairline borders"*, never *"do it like Brand X"*.
That is a deliberate discipline, for two reasons — a brand-named rule invites literal copying, and
it implies an endorsement that does not exist.

## Trademarks

All product names, company names, brand names, and typeface names mentioned are the trademarks or
registered trademarks of their respective owners. They are used **nominatively** — to identify the
subject of a source analysis — and no claim of ownership, licence, affiliation, or approval is made
or implied.

## The source collection's own position

The host repository's README states its position on this, and it applies equally here:

> "This repository is a curated collection of design system documents extracted from public
> websites. … The extracted design tokens represent publicly visible CSS values. We do not claim
> ownership of any site's visual identity."

This layer takes the same position, one step further removed: it does not even document those
identities. It documents patterns *across* them.

**Note on source naming inconsistency:** seven source files use deliberately altered brand
spellings (e.g. "Stripi", "Slacc"), apparently as trademark distancing, while thirteen files in the
same phrasing group use accurate names. This layer uses **accurate names** consistently, because
nominative use of a trademark to identify its subject is the clearer and more honest position than
partial obfuscation. The inconsistency in the source is recorded as
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D8 for the maintainers' decision.

---

## Licence

The source repository is licensed **MIT** ([`LICENSE`](../LICENSE), copyright VoltAgent). This
derived work sits inside that repository and inherits it.

**MIT covers the repository's text. It does not and cannot license third-party trademarks, brand
identities, or proprietary typefaces described by that text.** That distinction matters and is
explained in [LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md).

## If you use this layer

You do not need to credit it — MIT does not require attribution beyond preserving the notice. But
if you find it useful, credit the **source collection** rather than this synthesis. The close
reading of 74 real websites was the hard part; organising it was comparatively easy.

## If you extract this layer into a separate repository

Work through [PUBLISHING-CHECKLIST.md](PUBLISHING-CHECKLIST.md) first. Minimum requirements:

- [ ] Preserve the MIT licence and copyright notice
- [ ] Identify the source collection prominently, with a link
- [ ] Keep the no-affiliation and trademark statements above
- [ ] Convert relative source citations (`design-md/…`) into links to the source repository, or
      state clearly that they refer to it
- [ ] Keep the evidence-strength banners on every category guide — removing them turns honest
      reasoning into false authority
- [ ] Keep [REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md), or clearly note that the
      layer's citations refer to a specific state of the source repository

**The evidence banners are the most important thing to preserve.** Four of the eleven category
guides are reasoning rather than evidence. Published without that stated, they would be four
confident-sounding documents making claims they cannot support — which is precisely the failure this
layer was built to avoid.
