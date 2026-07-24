# Traceability

Which sources support which recommendation, and which recommendations have no source at all.

Read alongside [../SOURCE-INVENTORY.md](../SOURCE-INVENTORY.md) (per-source detail) and the
`Source inspiration` section of each [category guide](../categories/).

**Verification status:** every source path cited across this layer was checked to exist — 123
distinct citations, all resolving. All 74 source directories are cited by explicit path at least
once.

---

## 1. Corpus-backed universal recommendations

Each supported by a clear majority. Counts are files, from
[VALUE-DISTRIBUTIONS.md](VALUE-DISTRIBUTIONS.md).

| Recommendation | Support | Where published |
|---|---|---|
| 4px base grid, 8px preferred increments | 57 files state a base of 4 or 8 | Foundation §3 |
| Core spacing sequence `4·8·12·16·24·32` | 61–73 files per step | Foundation §3 |
| 16px default body text | 61 files | Foundation §4 |
| Breakpoints 480 / 768 / 1024 / 1280 / 1440 | 20–37 files per value | Foundation §10 |
| 44px minimum touch target | 48 files | Foundation §13 |
| Line-height falls as size rises | ~70 files | Foundation §4 |
| Negative tracking scales with display size | ~24 of 26 files with display >80px | Foundation §4 |
| Positive tracking on small uppercase | ~40 of 45 files with an overline token | Foundation §4 |
| One accent, used scarcely | 44 files single-accent, 6 zero-accent | Foundation §5 |
| Multiple accents must map to structure | ~11 of 13 multi-accent files | Foundation §5 |
| 8px control radius as default | 47 files | Foundation §8 |
| 24px card padding as default | 20 files (mode) | Foundation §9 |
| Control heights cluster 36–48px | 40px in 22, 44px in 19, 48px in 14 | Foundation §9 |
| Nav heights cluster 56–64px | 64px in 22, 56px in 14 | Foundation §9 |
| 1280px modal container width | 27 files; 1200px in 19 | Foundation §9 |
| Prose measure narrower than container | Every file documenting both | Foundation §4 |
| Border-first elevation | ~38 files | Foundation §7 |
| Dark canvas → lightness ladder, not shadow | ~14 of 14 dark systems | Foundation §6 |
| Dark mode is not an inversion | 0 files describe it as one; 24 document both modes separately | Foundation §6 |
| Substitution guidance for proprietary faces | 59 files | Foundation §4, all templates |
| Tabular figures for compared numerics | `design-md/stripe/` explicit; 6 files with `stat-display` | Foundation §4 |

## 2. Category recommendations with direct evidence

| Recommendation | Sources | Category guide |
|---|---|---|
| Marketing section rhythm 80–96px | 61 files at 96px, 24 at 80px | marketing-website §2 |
| Marketing display ceiling 56–80px | median largest display 64–72px | marketing-website §3 |
| Full-bleed bands with contained content | dominant structure across 55 marketing sources | marketing-website §2 |
| Alternating surface polarity for section rhythm | `design-md/apple/`, `design-md/playstation/`, `design-md/nvidia/`, `design-md/together.ai/` | marketing-website §5 |
| 3–4 pricing tiers, featured lifted by surface | `design-md/notion/`, `design-md/miro/`, `design-md/mongodb/`, `design-md/linear.app/` | marketing-website §7 |
| Card grid 3-up → 2-up at 1024 → 1-up at 768 | documented collapsing strategy across many sources | marketing-website §11 |
| Docs 3-column layout (nav / prose / TOC) | `design-md/mintlify/`, `design-md/minimax/`, `design-md/mongodb/`, `design-md/nvidia/`, `design-md/voltagent/` | general-website §2 |
| Docs prose measure 640–960px | `design-md/ollama/` (720/960), `design-md/together.ai/` (900) | general-website §2 |
| Docs display ceiling 36–56px | same 5 docs sources vs. their own marketing scales | general-website §3 |
| Docs section rhythm 48–64px | same comparison | general-website §2 |
| Editorial body 18–19px, serif legitimate | `design-md/wired/` (19px serif body) | content-editorial §2 |
| Editorial colour at panel scale | `design-md/theverge/` (full-bleed colour story tiles) | content-editorial §4 |
| Masonry for mixed-aspect content | `design-md/pinterest/` | content-editorial §4, ecommerce §2 |
| Developer tools split evenly dark/light | 8 dark vs. 8 light in the same domain | developer-tools §1 |
| Mono confined to code contexts | `design-md/linear.app/`, `design-md/vercel/`; counter-example `design-md/opencode.ai/` | developer-tools §2 |
| Terminal/code mockup as hero argument | `design-md/composio/`, `design-md/warp/`, `design-md/voltagent/`, `design-md/expo/` | developer-tools §11 |
| Two commerce registers on one page | `design-md/nike/` (campaign type above dense retail chrome) | ecommerce §1 |
| PDP and configurator structure | `design-md/meta/` | ecommerce §3 |
| Narrower container on detail than browse pages | `design-md/airbnb/` (1080 vs 1280) | ecommerce §12 |
| Dual-track polarity by surface purpose | `design-md/binance/`, `design-md/shopify/` | multi-role §4, ecommerce §1, high-trust §3 |
| Restraint + tabular figures in finance | `design-md/stripe/`, `design-md/coinbase/` | high-trust §4 |
| High-trust does not require squared geometry | `design-md/mastercard/` (40px hero radius, pill cards) | high-trust §3 |
| Directional semantic colour for value change | `design-md/binance/` | high-trust §4 |
| Four-step surface ladder without shadow | `design-md/linear.app/` | Foundation §6, dashboard §, spatial § |
| Content-supplies-colour dark app shell | `design-md/spotify/` (the corpus's only real app UI) | dashboard §16, spatial §16 |
| Per-product accent as identity token | `design-md/hashicorp/`, `design-md/webflow/` | multi-role §13, marketing §15 |
| Tiered single-hue surface roles | `design-md/starbucks/` (four calibrated greens) | multi-role §13, ecommerce §12 |
| Multi-audience consistency on one system | `design-md/uber/` | multi-role §13 |
| Scoped accent for an AI sub-brand | `design-md/intercom/` | conversational-ai §14 |
| Persistent chat bar as a real pattern | `design-md/tesla/` — the corpus's only conversational component | conversational-ai §2d, §14 |

## 3. Synthesized recommendations — no corpus support

Stated plainly. These come from general interface-design reasoning, are labelled inline where they
appear, and carry their reasoning so the argument can be evaluated rather than the authority.

| Recommendation | Why the corpus cannot support it | Where |
|---|---|---|
| Primitive/semantic token two-layer model | No source states the model; naming discipline is present but the rule is not | Foundation §2 |
| Full semantic status set with surface variants | `info` appears in 4 files; surface variants in none | Foundation §5 |
| All eight interaction states | Many files state "hover states not documented by system policy" | Foundation §11 |
| Empty / loading / error / partial / permission states | `empty state` appears in 1 file of 74; 10 mention loading | Foundation §17, all guides |
| Focus ring specification | 14 files document a focus ring; none specifies offset or dual contrast | Foundation §5 |
| Mobile-specific requirements | Source responsive sections are frequently self-declared as synthesized from desktop evidence | Foundation §10 |
| Motion duration and easing scale | 44 files mention motion; durations rarely given | Foundation §12 |
| Accessibility floor thresholds | Taken from WCAG 2.2 directly; 56 sources assert conformance, none demonstrates a ratio | Foundation §13 |
| Form conventions | Structure documented; validation and error behaviour not | Foundation §16 |
| Feedback mechanism semantics | Not documented anywhere in the corpus | Foundation §17 |
| **All conversational interaction design** | Corpus contributes one component | conversational-ai, most sections |
| **All dashboard table, filter, and bulk-action design** | Zero documented dashboards; `Tables` in 3 files | dashboard-admin §4–12 |
| **All permission, audit, and approval design** | No role-based application documented | multi-role §7–9 |
| **All chart mechanics and categorical palettes** | No analytics interface documented | data-analytics §4–7 |
| **All checkout design** | No checkout flow documented | ecommerce §8 |
| **All verification, confirmation, and irreversible-action flows** | Not documented | high-trust §6–9 |
| **Everything spatial** | Corpus is entirely silent on maps and 3D | spatial-map-3d, all sections |
| Density-mode systems | Density is inferable from padding and type, never stated as a mode system | dashboard §2, all guides |
| Command palette specification | 9 files mention keyboard/shortcuts, as a marketed feature | dashboard §9 |
| URL-state requirement for filters | Not documented | dashboard §4 |

## 4. Recommendations that contradict the corpus's own frequency

Cases where the modal corpus value was deliberately **not** adopted, because the population is
marketing websites and the guidance is for other surfaces.

| Corpus mode | What this layer recommends instead | Reason |
|---|---|---|
| 96px section rhythm (61 files) | 64–80px default; 32–48px for daily-use tools | Rhythm that reads as considered on a first visit is a scroll cost on the fortieth |
| 64–72px display ceiling | 24–32px in application surfaces | Marketing scale inside a product wastes screen on decoration |
| 1280px container everywhere (27 files) | Container **and** a separate 640–760px prose measure | Full-width paragraphs are a layout defect |
| Light or dark only (~50 files) | Design both modes separately | Single-mode systems reflect a marketing surface, not a product |
| Hover states undocumented | All eight states required | Absence from documentation is not absence from the product |

Each of these is a case where reporting frequency as endorsement would have produced bad advice.
See [../ASSUMPTIONS.md](../ASSUMPTIONS.md) D-04.

## 5. Documented disagreements

Where sources conflict and this layer presents a condition rather than a winner. Full analysis in
[PATTERN-CLUSTERS.md](PATTERN-CLUSTERS.md) §4.

| Disagreement | Positions | Deciding condition | Where |
|---|---|---|---|
| Display weight for trust | 300–400 (`stripe`, `coinbase`, `ibm`, `playstation`) vs. 700–900 (`binance`, `wise`, `vodafone`) | Audience sophistication and channel | high-trust §3, Handbook §12 |
| Radius in finance | 0–4px (`ibm`, `nvidia`, `hp`) vs. soft/pill (`mastercard`, `revolut`, `wise`) | Infrastructure vs. consumer-facing | high-trust §3, Handbook §7 |
| Developer tool polarity | 8 dark vs. 8 light | Continuity with IDE/terminal vs. with reading | developer-tools §1 |
| Section rhythm | 96px (61 files) vs. 32–64px (docs, editorial) | Visit frequency | Foundation §3 |
| Shadow vs. border | ~14 shadow vs. ~38 border vs. ~10 contextual | Canvas lightness, then grouping vs. physical lift | Foundation §7, Handbook §6 |

## 6. Source coverage of this layer

| Source group | Files | Contribution weight |
|---|---|---|
| Marketing-only sources | 55 | High for marketing, typography, tokens, spacing, elevation |
| Documentation surfaces | 5 | **Disproportionately high** — same brands at two densities isolates category logic from brand |
| Dual-track sources | 2 | **Disproportionately high** — the empirical basis for the hybrid layering model |
| Real editorial products | 2 | High for editorial typography and reading density |
| Real application UI | 1 | High for dark app-shell surface ladder |
| Commerce surfaces | 6 | Moderate for discovery and PDP; nothing for checkout |
| Retro reconstructions | 2 | Low — period-specific; used as counter-examples on density |
| Structural outlier | 1 | Minimal (`design-md/kraken/`, ~1/10 corpus median) |
| Auto-generated example blocks | 13 files | **Excluded as evidence** — extrapolations, not observations (D7) |

The two smallest groups — 5 documentation surfaces and 2 dual-track sources — carry more analytical
weight than their count suggests, because they hold brand constant while varying surface purpose.
That is the closest thing to a controlled comparison the corpus offers.

## 7. How to audit a claim

1. Find the recommendation in the foundation or a category guide.
2. Check §1–3 above, or the guide's `Source inspiration` section.
3. If listed in §1 or §2, open the cited file at the cited section.
4. If listed in §3, **there is no source** — evaluate the stated reasoning instead.
5. If listed in §4, the corpus says something different and the reason is given.
6. If listed in §5, sources disagree and the condition is what matters.

If a recommendation appears in none of these categories, that is a traceability gap. Report it.
