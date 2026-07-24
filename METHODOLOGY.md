# Methodology

How the derived layer was produced, so that its claims can be checked and its analysis
re-run.

---

## 1. What was treated as evidence

**Primary evidence:** the 74 `DESIGN.md` files under `design-md/`. Read directly.

**Not treated as evidence:** the root `README.md` descriptions. The README is a catalog
index written for readers; it describes the collection's intent, and in several verifiable
respects it does not match the checkout (see
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md)). Where README and file
disagreed, the file won.

**Treated as evidence about limits:** the `Known Gaps` sections, present in 43 files.
These are the most useful part of the corpus for calibration, because they state what their
authors did *not* observe. A recommendation cannot honestly be grounded in a surface the
source says it never captured.

---

## 2. Extraction

Three passes, all read-only, all from a session scratchpad outside the repository.

**Pass 1 — structure and tokens.** Parsed the YAML-style frontmatter block from the 64
files that have one, harvesting `colors`, `typography`, `rounded`, `spacing`, and
`components` sub-keys. Collected every `##` and `###` heading to derive the real document
structures. Collected `description` (frontmatter) or the Visual Theme narrative (the other
10 files) for categorization.

**Pass 2 — section-scoped dimensions.** Naive document-wide regex over-collects: a search
for breakpoints finds `9999` from the pill-radius table. So pass 2 scoped each search to
the section that owns the value — breakpoints only from `Responsive Behavior › Breakpoints`,
container widths only from `Layout › Grid & Container`, touch minimums only from
`Responsive Behavior › Touch Targets`, control padding only from
`Components › Buttons` and `Components › Inputs & Forms`. Every distribution in
[research/VALUE-DISTRIBUTIONS.md](research/VALUE-DISTRIBUTIONS.md) comes from the scoped
pass.

**Pass 3 — targeted verification.** Direct greps to confirm or refute specific claims
before writing them: which files mention chat, maps, tables, roles; how many assert WCAG
conformance; which files carry auto-generated example blocks; whether referenced tooling
exists in the repository. Several intuitions died here, which was the point.

---

## 3. Value tagging

Each extracted value carries a confidence tag, and unavailable is never coerced to zero:

| Tag | Meaning |
|-----|---------|
| **explicit** | A number stated in the file (frontmatter token or table cell). |
| **inferred** | Derived from an explicit relationship, e.g. control height from stated padding plus line-height. |
| **ambiguous** | Stated but contradicted elsewhere in the same file, or given only as a range. |
| **unavailable** | Not present. Recorded as absent — never as `0`, never as "the source rejects it". |

The distinction matters most for absence. `design-md/bugatti/DESIGN.md` publishes a radius
scale of `none: 0px, pill: 9999px, full: 9999px` — that is an explicit editorial position
(no mid-radius exists in that system). A file with no radius data at all is `unavailable`.
Collapsing the two would fabricate a design opinion.

---

## 4. Pattern classification

Every finding was sorted into one of five buckets before it was allowed to influence a
recommendation:

| Class | Test applied | Example from this corpus |
|-------|--------------|--------------------------|
| **Universal** | Holds across most sources *and* survives a usability argument independent of the corpus | 4px/8px base grid; 16px default body; 44px touch minimum |
| **Category-dependent** | Clusters by product type | Uppercase tracked display type clusters in automotive and campaign retail; monospace-forward chrome clusters in developer tooling |
| **Context-dependent** | Varies with density, device, expertise, risk, or use frequency | Section rhythm: 96px on a scroll-once marketing page, far tighter in a daily-use tool |
| **Brand-specific** | Traceable to one identity; portable only as a *structural* principle | A named brand hue; a proprietary typeface; one company's signature gradient |
| **Exception** | Defensible for its source, unsafe as general advice | An all-monospace page; a 0px-radius-everywhere system; a 136px display size |

Only the first three classes produce normative guidance. Brand-specific findings appear as
structural lessons in `Source inspiration` sections. Exceptions appear in
[ANTI-PATTERNS.md](ANTI-PATTERNS.md) with the conditions under which they are legitimate.

---

## 5. Evidence thresholds

A claim needed one of these to ship:

1. **Corpus convergence** — the pattern appears in a clear majority, and the count is
   published alongside it.
2. **Cluster evidence** — it appears consistently within a category cluster, with the
   cluster named and its members listed.
3. **Declared synthesis** — it comes from general interface-design reasoning rather than
   this corpus, is labelled *synthesized*, and carries its reasoning inline so a reader can
   disagree with the argument rather than just the conclusion.

Nothing shipped as fact on a single source. Where sources genuinely disagree, the
disagreement is documented with the conditions favouring each side — see
`research/PATTERN-CLUSTERS.md`, section *Documented disagreements*.

---

## 6. Deliberate non-goals

- **No averaging across incompatible systems.** See ASSUMPTIONS D-03.
- **No tooling.** No database, web app, or build step was added. The corpus is Markdown;
  the derived layer is Markdown.
- **No copying.** No passage was lifted from a source file. Short quotations appear only
  where a source's own words establish a limitation, and are attributed inline.
- **No re-verification of source accuracy against live websites.** The derived layer
  synthesizes what the corpus says. Whether a given hex value still matches a live site
  today is outside scope and is recorded as a limitation, not silently assumed.

---

## 7. Reproducing the quantitative findings

The scripts were not committed (ASSUMPTIONS D-10). Each published distribution can be
re-derived from the corpus directly. Two worked examples:

Structural variants — group files by their `##` heading sequence:

```bash
python -c "
import glob, os, re, collections
g = collections.defaultdict(list)
for p in sorted(glob.glob('design-md/*/DESIGN.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    g[tuple(re.findall(r'^## (.+)$', t, re.M))].append(os.path.basename(os.path.dirname(p)))
for k, v in sorted(g.items(), key=lambda x: -len(x[1])):
    print(len(v), len(k), v)
"
```

Section-scoped breakpoints — the pass-2 technique, in miniature:

```bash
python -c "
import glob, re, collections
c = collections.Counter()
for p in glob.glob('design-md/*/DESIGN.md'):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^###\s*Breakpoints\s*$(.*?)(?=^###|\Z)', t, re.M | re.S)
    if m:
        c.update({int(x) for x in re.findall(r'(\d{3,4})\s*px', m.group(1)) if 280 <= int(x) <= 2000})
print(sorted(c.items()))
"
```

Both are read-only. Neither writes to the repository.
