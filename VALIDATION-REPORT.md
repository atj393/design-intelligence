# Validation Report

What was checked, what passed, what was fixed, and what remains uncertain.

The last section is the important one. A validation report that only lists passes is not a
validation report.

---

## 1. Automated checks

Run programmatically over all files in `design-intelligence/`.

| Check | Result |
|---|---|
| Markdown files in the layer | 59 at first validation pass; **67** final |
| Relative links checked | 226 at first pass; **297** final |
| Broken links | 10 at first pass — **all to Phase 11 files not yet written**; **0** final |
| Distinct `design-md/…` source paths cited | 123 |
| Cited source paths that do not exist | **0** |
| Source directories cited by explicit path | **74 of 74** |
| Unresolved `[[SET:]]` / `[[CHOOSE:]]` outside `templates/` | 0 |
| Empty or heading-only files | 0 |
| Binary assets, images, or font files | 0 |
| Absolute local paths in published text | 0 |

Every source citation in this layer points at a file that exists. That was the check most likely to
fail, and it is the one that makes the traceability claims meaningful.

## 2. Numeric coherence

### Type scales

- [x] Adjacent steps differ by 1.15×–1.35× in every published scale (foundation, and all 11 templates)
- [x] Line-height falls monotonically as size rises in every scale
- [x] Negative tracking present on all display steps above 40px; magnitude ~2–4% of size
- [x] Positive tracking on every `overline` / small-uppercase token
- [x] No template sets body below 14px, or below 16px on mobile
- [x] Display ceilings respect their category (marketing 56–80 · docs 36–56 · app 24–32 · dashboard 20–28)
- [x] `numeric` / `amount` / `price` tokens carry `tabular-nums` in every template that has them

### Spacing scales

- [x] Every published spacing value is a multiple of 4
- [x] Progressions are monotonic with no duplicate steps
- [x] Section rhythm consistent between each category guide, the comparison matrix, and its template
- [x] Grouping ratio (between-group ≈ 2× within-group) holds in the form guidance

### Component dimensions

- [x] Control heights match their stated density mode in every template
- [x] Input height equals button height in every template
- [x] Table row heights match density modes (32 / 40 / 48)
- [x] Compact-mode values never below 13px body or 32px controls
- [x] Every template using compact density states that compact is pointer-only
- [x] Touch minimum of 44px stated wherever compact appears

### Responsive

- [x] Breakpoint sets identical across all templates (480 / 768 / 1024 / 1280 / 1440)
- [x] No template defines a behaviour that contradicts the foundation's model
- [x] Every category guide's responsive table covers <768 / 768–1024 / >1024
- [x] Categories claiming partial mobile parity say so explicitly and require in-interface disclosure

## 3. Inconsistencies found and fixed

Found during validation, corrected rather than shipped. Recorded because a report claiming zero
findings would not be credible.

### 3a — Found by document review

| # | Issue | Fix |
|---|---|---|
| 1 | An early foundation draft presented 1280px as a universal container width | Corrected to modal-plus-range: 1280px (27 files), 1200px (19), 1440px (10) |
| 2 | An early conversational-AI draft specified a 44px composer height, contradicting the foundation's own control-height table | Corrected to a 56px min-height with the multiline rationale stated |
| 3 | `categories/conversational-ai.md` listed a 780px spacious message column while its own prose and the comparison matrix said 680–760px | Changed to 760px |
| 4 | `CATEGORY-COMPARISON.md` listed dashboard section rhythm as 32–48px; the dashboard guide and template both use 16–32px | Comparison matrix corrected to 16–32 (dashboard), 40–64 (high-trust), 16–24 (analytics) |
| 5 | The root README addition claimed the collection holds "74 established products", contradicting the `count-73` badge on the same page | Count claim removed; heading shortened to match surrounding style |

### 3b — Found by building the dashboard template

**Document review missed all ten of these.** They surfaced within minutes of an actual build. Full
report: [research/TEMPLATE-VALIDATION.md](research/TEMPLATE-VALIDATION.md).

| # | Severity | Issue | Fix |
|---|---|---|---|
| T-01 | Critical | **Density modes did not control density.** Declared 32/40/48px rows rendered at 50/58/94–118px — 100% of rows exceeded declared height in all three modes. Comfortable:compact ratio 1.92 vs. intended 1.50 | Added a `table-columns` block with per-column width and wrap policy, `table-layout: fixed` requirement, and an explicit fixed-vs-variable row-height tradeoff. Re-test: compact exact (0/8 exceeding) |
| T-02 | Critical | **Sticky budget arithmetically impossible.** Template declared a 20% viewport budget while specifying heights summing to 196px = 22.8% at 860px, 25.5% at 768px | Added `sticky-layers-max: 3` and a priority order. Re-test: 12.7% at 860px |
| T-03 | Critical | **Dark-mode rule contradicted the contrast floor.** "Lighten saturated colours" + "filled buttons use `#ffffff`" measured 3.68:1 (accent) and 2.92:1 (danger) — both failing 4.5:1 | Split each action colour into a `*-fill` and a `*-on-dark` token. Re-test: 5.17:1 and 5.33:1. Propagated to the foundation, which was the source of the rule |
| T-04 | Major | **Responsive table omitted the page header and toolbar** — both specified as sticky with fixed heights. A non-wrapping page header overflowed 345px → 413px at 375px, forcing horizontal page scroll | Added both rows; both un-stick below 768px. Added a rule that fixed `top:` offsets break when the element above wraps |
| T-05 | Major | **Touch guard was a single point of failure.** `pointer: coarse` alone let 26 sub-44px targets ship at 375px | Guard on `(pointer: coarse), (max-width: 767px)` |
| T-06 | Minor | No z-index scale, despite specifying 7 overlapping layers | Added a 7-step scale |
| T-07 | Minor | Toast position, stacking, and dismissal unspecified | Added |
| T-08 | Minor | No skeleton token or animation spec, despite requiring skeletons | Added |
| T-09 | Minor | Pinned column had no min-width; a 109px column wrapped a 14-char reference, defeating the pin | `min-width: 130px` + `nowrap` |
| T-10 | Minor | Mobile card transform had no anatomy | Added a 4-line card spec |
| C-01 | Minor | **The foundation checklist's contrast rule was too broad.** "UI boundaries ≥3:1" unqualified flagged decorative row dividers (1.36:1) as failures — WCAG 1.4.11 exempts them. False blockers train reviewers to ignore the rule | Rule now distinguishes meaningful boundaries from exempt separators; added a filled-button-label check; softened the disabled-state item to note WCAG 1.4.3 exempts disabled controls |

**Two of the three critical defects were self-contradictions** — cases where the template gave two
instructions that could not both be followed. Neither was visible on review. That is the strongest
argument in this report for building over reading.

### 3c — Found by adversarially reviewing the weak-evidence guides

Full report: [research/WEAK-GUIDE-REVIEW.md](research/WEAK-GUIDE-REVIEW.md).

| # | Issue | Fix |
|---|---|---|
| A-01 | "Never bubble assistant responses" was wrong for short-turn assistants (support bots, booking flows) where users hold a messaging mental model | Conditioned on expected response length, with a decision table and a safe default |
| A-02 | The 680–760px message column was presented as resolved while the same guide required code blocks and tables, which need 900px+. An unresolvable tension asserted away | Tension stated, with three ranked resolutions and a warning against the naive fix |
| A-03 | "Never zebra-stripe" too absolute — striping genuinely helps row tracking in 15+ column tables that scroll horizontally | Downgraded to "avoid", with the exception and a subtlety constraint |
| A-04 | "Panels must be ≥90% opaque" confused mechanism with goal; the requirement is contrast over the worst-case basemap | Restated as a contrast requirement, with opacity as the fallback |
| A-05 | "Disable and explain" under-qualified: the explanation discloses system capability and the required role to a lower-privilege user | Added a third hide condition and a per-action decision rule |
| A-06 | Two thresholds (20% sticky, 30% occlusion) are **invented numbers presented as rules** | Occlusion budget relabelled a synthesized heuristic. Sticky budget retained — the build test showed it discriminating a real failure from a real fix — but its origin is now recorded |

## 4. Evidence integrity

The checks that matter most, given what this layer is.

- [x] Every category guide opens with an evidence-strength banner
- [x] Four guides explicitly labelled predominantly or fully synthesized: conversational AI,
      dashboard/administration, multi-role platform, data analytics; spatial labelled **fully**
      synthesized
- [x] No synthesized recommendation presented as corpus-derived
- [x] Every universal claim in the foundation carries a file count
- [x] Brand-specific findings appear only in `Source inspiration` sections and research tables
- [x] **No brand name appears in any normative rule** — verified by grep across all guidance files
- [x] Exceptions (all-monospace page, 0/9999 radius scale, 136–144px display) are labelled as
      exceptions, not patterns
- [x] Documented disagreements present both positions with the deciding condition, not a winner
- [x] `research/TRACEABILITY.md` §3 lists synthesized recommendations explicitly, by section

### Specific claims verified against the corpus

| Claim | Verification |
|---|---|
| "No source describes dark mode as an inversion" | Checked all 24 files documenting both modes |
| "50 of 74 use zero or one accent" | 44 single-accent + 6 zero-accent |
| "`empty state` appears in one file" | `grep -ril 'empty state' design-md/*/DESIGN.md` → 1 |
| "Corpus contains no map or spatial evidence" | Grep for map/geospatial/mapbox/3D terms; all 16 hits are unrelated senses |
| "73 of 74 files carry `Do's and Don'ts`" | Counted; `design-md/airbnb/` is the exception |
| "13 files contain auto-generated example blocks" | Counted, with 2 `TO_FILL` markers in each |
| "59 files publish font-substitution guidance" | Counted `Note on Font Substitutes` |
| "34 files reference `npx @google/design.md`" | Counted; no `package.json` exists in the repository |

## 5. Structural checks

- [x] All 11 category guides contain both recommendations **and** anti-patterns
- [x] All 11 templates contain accessibility commitments as checkable statements
- [x] All 11 templates specify all eight interaction states
- [x] All 11 templates specify data states including empty, loading, error, permission-denied
- [x] All 11 templates require a typeface substitution note
- [x] All 11 templates contain agent prompt guidance with the reading order
- [x] All 12 prompts contain an inspect step, a preserve-functionality constraint, and a required
      report
- [x] Every folder has a README index
- [x] Cross-references between guides, templates, checklists, and prompts resolve in both directions
- [x] Filenames and headings consistent within each folder

## 6. Remaining uncertainties

Not defects — genuine limits, stated so nobody mistakes reasoning for evidence.

### 6.0 Nine of ten templates remain unbuilt

**New, and now the most actionable limitation.** The dashboard template was built and yielded 10
defects, 2 of them self-contradictions it could not satisfy. The other nine have not been executed
by anyone.

There is no reason to think the dashboard template was unusually flawed, so expect a comparable
defect count in each remaining one. The two most likely to contain the same class of
self-contradiction:

- **`DESIGN.conversational-ai.md`** — the most intricate state machine in the layer (streaming,
  stop, layout stability, live-region announcements)
- **`DESIGN.spatial.md`** — the most unusual layout constraints (occlusion budget, panels over an
  uncontrolled canvas), and the only fully-synthesized category

**Consequence:** treat the dashboard template as materially more trustworthy than the other nine.
Its evidence base is unchanged — still zero corpus sources — but its *internal consistency* is now
verified rather than assumed. Reproduction method:
[research/TEMPLATE-VALIDATION.md](research/TEMPLATE-VALIDATION.md) §Reproducing this.

### 6.1 Four categories rest on reasoning, not evidence

The most significant limitation. Dashboard/administration, conversational AI, multi-role platform,
and data analytics have **zero** direct sources; spatial has none at all.

These guides are internally coherent and follow established interface practice. They are **not
evidence-backed**. The uncomfortable pattern is that the categories most in demand for new software
are the ones this corpus supports least.

**Mitigation:** evidence banners on every affected guide; explicit listing in
`research/TRACEABILITY.md` §3; a recommendation throughout to validate with real users earlier than a
corpus-backed category would need.

### 6.2 Contrast ratios were not recomputed

56 sources reference WCAG or contrast; 35 assert AAA, 13 assert AA. **None demonstrates a computed
ratio for a specific token pair.** AAA requires 7:1 for normal text, and several documented palettes
pair mid-grey muted text against tinted canvases in ways that make a blanket AAA claim implausible.

These were not verified — doing it properly means resolving every semantic pair per mode across 74
systems.

**Mitigation:** this layer takes its accessibility floor from the WCAG specification directly and
inherits no source's self-assessment. Every template requires computed verification in both modes.

### 6.3 Source accuracy against live sites is unverified

Whether a documented hex value, type size, or breakpoint still matches the live website was not
checked. Websites change. Some sources may describe a state that no longer exists.

**Mitigation:** the layer synthesizes *patterns*, which are more durable than specific values. No
recommendation depends on a single source's exact number.

### 6.4 Interaction states are almost entirely synthesized

The corpus documents almost none. Many files state "hover states not documented by system policy";
validation states are repeatedly listed as unobserved; `empty state` appears in one file of 74.

Every state specification in this layer is general practice. Notably, this is probably *why*
AI-generated interfaces routinely omit these states — the training material omits them too.

### 6.5 Responsive guidance is synthesized twice over

Source responsive sections are frequently declared **by their own authors** as synthesized from
desktop evidence — many state that mobile screenshots were not captured. Building on top of that is
reasoning atop reasoning.

**Mitigation:** mobile-first was not given a standalone guide for exactly this reason
([ASSUMPTIONS.md](ASSUMPTIONS.md) D-05). Breakpoint values are corpus-backed; behaviour guidance is
practice-based.

### 6.6 Category assignment involved judgment

Each source's primary category was assigned by reading its content. Several are defensible in more
than one category. The Surface/Domain split in
[SOURCE-INVENTORY.md](SOURCE-INVENTORY.md) makes the reasoning inspectable, but the calls are
judgments, not measurements.

### 6.7 Corpus depth varies by an order of magnitude

45 KB largest, 4.5 KB smallest. Comparisons involving `design-md/kraken/` are weak, and it was
excluded from distributions where it had nothing to contribute.

### 6.8 The population is marketing websites

Repeated because it is the frame for everything: ~90% of sources document acquisition surfaces.
Frequency data describes what brand websites do. Where the modal corpus value was wrong for another
surface type, this layer deliberately departed from it —
`research/TRACEABILITY.md` §4 lists all five such cases.

## 7. Recommendations relying more on reasoning than repository evidence

Consolidated list, so it can be read in one place. Detail in `research/TRACEABILITY.md` §3.

| Area | Status |
|---|---|
| Primitive/semantic token two-layer model | Synthesized (naming discipline present in corpus; rule is not) |
| Full semantic status set with surface variants | Synthesized (`info` in 4 files; surface variants in none) |
| All eight interaction states | Synthesized |
| Empty / loading / error / partial / permission states | Synthesized |
| Focus ring specification | Synthesized (14 files mention a ring; none specifies offset or dual contrast) |
| Motion durations and easing | Synthesized |
| Accessibility thresholds | From WCAG 2.2 specification |
| Form conventions and validation behaviour | Synthesized |
| Feedback mechanism semantics | Synthesized |
| Density-mode systems | Synthesized (density inferable, never stated as a mode system) |
| URL-state requirement for filters | Synthesized |
| Command palette specification | Synthesized |
| All conversational interaction design | Synthesized (corpus contributes one component) |
| All dashboard table/filter/bulk design | Synthesized |
| All permission/audit/approval design | Synthesized |
| All chart mechanics and categorical palettes | Synthesized |
| All checkout design | Synthesized |
| All verification/confirmation/irreversible flows | Synthesized |
| Everything spatial | Synthesized |

## 8. What was deliberately not validated

| Not done | Why |
|---|---|
| Live-site verification of source values | Outside scope; recorded as limitation 6.3 |
| Recomputing 74 systems' contrast pairs | Disproportionate; floor taken from spec instead |
| Usability testing of the guidance | Requires real users and real products |
| Verifying the third-party `npx` tool 34 files reference | Not part of this repository |
| Legal review of licensing guidance | [LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md) states it is not legal advice |
| Testing the templates by building a product | The correct next step, and outside this scope |

## 9. Confidence summary

| Layer content | Confidence | Basis |
|---|---|---|
| Token architecture and scales | **High** | 74 sources, strong convergence |
| Typography rules | **High** | Near-universal patterns |
| Breakpoints and touch targets | **High** | 20–48 files per value |
| Marketing guidance | **High** | 55 direct sources |
| Elevation and dark-mode model | **High** | Consistent across all dark systems |
| Developer tools, editorial, general website | Moderate | Partial direct evidence |
| E-commerce discovery and PDP | Moderate | 6 sources |
| High-trust visual expression | Moderate | 8 domain sources |
| Interaction and data states | **Reasoning** | Corpus near-silent |
| Dashboard, analytics, multi-role, conversational | **Reasoning** | No direct sources |
| Spatial | **Reasoning only** | Corpus silent |
| Accessibility floor | **High** | WCAG specification |

## 10. Verdict

The layer is internally consistent, its citations all resolve, its numeric scales are coherent, and
its evidence claims are labelled honestly. **Twenty-two defects were found and fixed rather than
shipped** — 5 by document review, 11 by building one template, and 6 by adversarially reviewing the
weak-evidence guides.

**The distribution of those defects is the most useful thing in this report.** Document review found
5, mostly cosmetic. Building *one* template found 11, including two self-contradictions that made
the template impossible to satisfy correctly — and one of those produced a genuine accessibility
failure for anyone who followed the guidance as written. Reading a specification cannot find a
specification that contradicts itself; executing it finds that in minutes.

**So the single highest-value action remaining is building the other nine templates** (§6.0), ahead
of any further writing or analysis.

**Its main weakness is not a defect in the work — it is the shape of the source material.** A corpus
of marketing websites cannot ground guidance about dashboards, chat interfaces, role-based platforms,
or maps. The layer's response is to say so, in a banner, at the top of every affected file.

Use the corpus-backed sections with confidence. Treat the reasoning-based sections as a considered
starting position, and test them.
