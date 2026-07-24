# Category Selection Framework

How to choose a design direction for a product you are about to build. This framework
evaluates **what the product does**, never which brand you admire.

Output: a primary category, zero or more supporting categories, a density mode, a visual
tone, and a list of design risks to watch.

---

## The central finding this framework rests on

**Product category determines density, navigation, and component set. It does not determine
visual tone.**

The corpus proves this. Developer tools appear in four incompatible tone clusters — dark
technical, warm editorial, clinical minimal, and documentation-first. Financial products
appear both maximally squared and maximally soft. One source sells a code editor and chose a
warm cream canvas *because* its genre defaults to dark.

So: **do not** ask "what should a fintech app look like?" That question has no answer. Ask
"how dense should it be, how do people navigate it, and which components carry the work?"
Those have answers, and this framework produces them. Tone is then a brand decision made
independently — see [DESIGN-DECISION-HANDBOOK.md](DESIGN-DECISION-HANDBOOK.md) §Tone.

---

## Part 1 — Discovery questions

Answer all 23 before selecting. Guessing here produces a confident wrong answer later.

### Purpose and audience

**Q1. What is the product's main goal?**
inform · persuade · sell · enable a task · monitor · analyse · communicate · create · manage

**Q2. Who is the primary user?**
[[free text — be specific: "warehouse supervisor on a shared terminal", not "business user"]]

**Q3. How many distinct user roles exist?**
1 · 2 · 3–5 · 6+
*3+ triggers the multi-role platform guide.*

**Q4. Public, authenticated, or both?**
public only · authenticated only · both
*Both means at least two surfaces and probably two densities.*

**Q5. How often does one person use it?**
once · rarely · weekly · daily · all day
*The single highest-leverage answer in this list. It drives density and section rhythm more
than anything else.*

**Q6. What level of expertise can you assume?**
none (public) · learnable in minutes · trained users · domain experts

### Task shape

**Q7. What are users primarily doing?** (pick up to two)
reading · discovering/browsing · communicating · creating · managing/administering ·
comparing · purchasing · monitoring · completing structured tasks · analysing

**Q8. How much information is on screen at once?**
sparse (one idea per view) · moderate · dense (tables, lists, many fields) · very dense
(multi-panel, simultaneous data)

**Q9. How many distinct workflows does the product contain?**
1–3 · 4–10 · 11–30 · 30+
*11+ means navigation architecture is your primary design problem, not visual style.*

**Q10. How deep is the navigation hierarchy?**
flat (1 level) · 2 levels · 3 levels · 4+
*3+ requires breadcrumbs.*

### Stakes and outcomes

**Q11. How important is conversion?**
not applicable · secondary · primary goal

**Q12. What are the consequences of a user error?**
trivial · recoverable annoyance · data loss · financial loss · regulatory or safety impact
*The last two force the high-trust guide as a supporting category regardless of domain.*

**Q13. How important is trust and risk reduction?**
low · moderate · critical

**Q14. Are there real-time state changes users must notice?**
no · occasionally · continuously

### Data and interface needs

**Q15. Is data visualisation needed?**
none · simple indicators · charts · complex multi-series analysis

**Q16. Are maps, spatial, or 3D interfaces needed?**
no · maps as a supporting view · maps as the primary canvas · 3D/spatial as primary

**Q17. How much content will exist?**
under 20 pages/records · 20–200 · 200–5,000 · 5,000+
*200+ makes search a primary navigation mechanism, not a convenience.*

### Constraints

**Q18. How important is mobile use?**
not supported · secondary · equal priority · primary

**Q19. How important is keyboard operation?**
standard accessibility only · valued by power users · essential to the core workflow

**Q20. What accessibility level is required?**
WCAG AA (assume this minimum) · AA plus specific commitments · AAA · regulated/procurement

**Q21. How strong is the existing brand identity?**
none — invent it · guidelines exist · strong and enforced · strong and expressed mainly in marketing

**Q22. Is role-based or per-tenant theming needed?**
no · light theming (logo, accent) · full per-tenant theming

**Q23. What technical constraints exist?**
[[free text: existing component library, framework, SSR, embedding context, performance
budget, browser support]]

---

## Part 2 — Decision tree

Walk it in order. First match wins for the **primary** category; keep walking to collect
supporting ones.

```
START
│
├─ Q16 = maps/3D primary?
│   └─ YES → PRIMARY: Spatial / Map / 3D
│            supporting: Data-Intensive Analytics, Dashboard
│            (highest-risk category — evidence is fully synthesized)
│
├─ Q7 includes "communicating" AND conversation is the main interface?
│   ├─ Conversation IS the product → PRIMARY: Conversational AI
│   │                                supporting: whatever hosts it
│   └─ Conversation is a FEATURE   → PRIMARY: the host category
│                                    supporting: Conversational AI (embedded pattern)
│
├─ Q3 ≥ 3 roles AND Q4 = authenticated or both?
│   └─ YES → PRIMARY: Commercial Multi-Role Platform
│            supporting: Dashboard (operator surfaces),
│                        Marketing Website (if Q4 = both),
│                        High-Trust (if Q12 ≥ financial loss)
│
├─ Q4 = public only?
│   ├─ Q11 = primary conversion goal → PRIMARY: Marketing Website
│   │                                  supporting: E-commerce (if Q7 = purchasing)
│   ├─ Q7 = reading, long-form        → PRIMARY: Content & Editorial
│   ├─ Q7 = purchasing                → PRIMARY: E-commerce & Transactional
│   │                                  supporting: Marketing Website, High-Trust
│   └─ otherwise                      → PRIMARY: General Informational Website
│                                       supporting: Developer Tools (if audience technical)
│
├─ Q8 = dense/very dense AND Q5 = daily/all-day?
│   ├─ Q15 = complex analysis   → PRIMARY: Data-Intensive Analytics
│   │                              supporting: Dashboard
│   └─ otherwise                → PRIMARY: Dashboard & Administration
│                                 supporting: High-Trust (if Q12 ≥ data loss)
│
├─ Q2 = developers AND product is technical infrastructure?
│   └─ YES → PRIMARY: Developer Tools
│            supporting: General Website (docs), Dashboard (console)
│
├─ Q12 ≥ financial loss OR Q13 = critical?
│   └─ YES → PRIMARY: Financial & High-Trust
│            supporting: Dashboard, Marketing Website
│
└─ DEFAULT → PRIMARY: Dashboard & Administration
             (the most common shape for authenticated single-role software)
```

### Density mode

| Q5 visit frequency | Q8 information density | Density |
|---|---|---|
| once / rarely | sparse / moderate | **spacious** |
| rarely / weekly | moderate | **default** |
| daily | moderate / dense | **default → compact** |
| daily / all-day | dense / very dense | **compact** |
| any | any, but Q18 = mobile primary | **default** (never compact — touch needs 44px) |

**Compact is a pointer-device mode.** If the surface is used on touch, 44px targets override
compact heights.

### Visual tone — decided separately

Tone is not derived from category. Derive it from brand and audience:

| Q21 brand strength | Q6 expertise | Suggested tone | Decoration budget |
|---|---|---|---|
| None / weak | expert | Clinical minimal | none–minimal |
| None / weak | novice | Warm approachable | minimal–moderate |
| Guidelines exist | any | Apply the guidelines; use the foundation for what they omit | per guidelines |
| Strong, enforced | any | Brand leads; foundation fills the gaps | per brand |
| Strong in marketing only | expert | **Dual-track**: expressive marketing, restrained product | split |

That last row is the corpus's documented pattern (see
[research/PATTERN-CLUSTERS.md](research/PATTERN-CLUSTERS.md) C7) and the correct answer for
most companies with a strong brand and a serious product.

---

## Part 3 — Recommendation model

Produce this block. An agent can emit it verbatim; a human can review it in a minute.

```
PRIMARY CATEGORY:     <one>
SUPPORTING:           <zero or more, with the surface each applies to>
DENSITY MODE:         compact | default | spacious
VISUAL TONE:          <cluster> + <decoration budget>
CANVAS POLARITY:      light | dark | dual-track
NAVIGATION MODEL:     <pattern> (+ secondary)
ACCENT COUNT:         0 | 1 | 2+ (if 2+, state the structural mapping)
CONTAINER / MEASURE:  <container px> / <prose px>
SECTION RHYTHM:       <px>
DESIGN RISKS:         <ranked list>
EVIDENCE STRENGTH:    <from the primary category guide's banner>
OPEN QUESTIONS:       <decisions needing a human>
```

### Worked example 1 — internal claims-processing tool

Answers: Q1 enable a task · Q3 3 roles · Q4 authenticated · Q5 all day · Q6 trained ·
Q7 completing structured tasks + managing · Q8 dense · Q9 12 workflows · Q11 n/a ·
Q12 financial loss · Q15 simple indicators · Q18 secondary · Q19 essential · Q21 none

```
PRIMARY CATEGORY:     Commercial Multi-Role Platform
SUPPORTING:           Dashboard & Administration (operator workspace)
                      Financial & High-Trust (payout and adjustment flows)
DENSITY MODE:         compact
VISUAL TONE:          Clinical minimal, decoration budget: none
CANVAS POLARITY:      light (dark mode optional, not launch-critical)
NAVIGATION MODEL:     side nav 240px + command palette (Q19 essential)
ACCENT COUNT:         1 — plus a full semantic status set, which does the real work here
CONTAINER / MEASURE:  fluid to 1440px / 680px for policy text
SECTION RHYTHM:       32–48px
DESIGN RISKS:         1. Marketing-scale spacing making all-day work slow
                      2. Three roles drifting into three unrelated products
                      3. Irreversible payout actions without adequate confirmation
                      4. Status conveyed by colour alone in dense tables
EVIDENCE STRENGTH:    Weak — predominantly synthesized. Validate with users early.
OPEN QUESTIONS:       Does the adjuster role need offline capability?
```

### Worked example 2 — API product with docs and a console

Answers: Q1 enable a task · Q3 2 roles · Q4 both · Q5 weekly · Q6 developers ·
Q7 creating + monitoring · Q8 moderate · Q9 6 · Q11 secondary · Q12 recoverable ·
Q15 charts · Q17 200+ docs pages · Q19 valued · Q21 weak

```
PRIMARY CATEGORY:     Developer Tools
SUPPORTING:           General Informational Website (documentation)
                      Marketing Website (acquisition pages)
                      Dashboard & Administration (usage console)
DENSITY MODE:         default; compact for the console's log and usage views
VISUAL TONE:          Choose one — dark technical OR warm editorial. Both are
                      well-evidenced for this category; pick on brand, not genre.
CANVAS POLARITY:      dual-track is unnecessary here; one polarity across all three
                      surfaces, with light+dark both supported (developer expectation)
NAVIGATION MODEL:     top bar (marketing) · 3-column docs (sidebar/prose/TOC) ·
                      side nav (console). Search is primary at 200+ pages.
ACCENT COUNT:         1, plus a separate link colour and a mono treatment for code
CONTAINER / MEASURE:  1280px marketing / 960px docs shell / 680px prose
SECTION RHYTHM:       80px marketing · 48px docs · 32px console
DESIGN RISKS:         1. Docs inheriting marketing type scale and losing scannability
                      2. Monospace applied to interface text rather than code
                      3. API keys and secrets shown without copy/reveal/redaction care
                      4. Three surfaces drifting into three visual systems
EVIDENCE STRENGTH:    Moderate-strong for tone and docs; synthesized for console.
OPEN QUESTIONS:       Is the console embedded in the docs or a separate app shell?
```

---

## Part 4 — Hybrid products

Most real products are hybrids. **Do not force a hybrid into one visual pattern.**

The corpus documents the answer directly. Two sources describe explicit dual-track systems
where marketing runs dark and cinematic while transactional surfaces run light and dense —
sharing typography, radius, spacing, and button vocabulary, differing in canvas polarity,
density, and decoration.

### The layering model

**One token foundation. Multiple experience layers. Each layer sets its own density,
navigation, and component emphasis.**

| Must stay constant | May vary per layer |
|---|---|
| Primitive tokens (colour ramp, type families) | Density mode |
| Semantic token *names* | Section rhythm and page padding |
| Type scale ratios | Which scale steps are used |
| Radius character | Which radius steps dominate |
| Spacing base unit | Container width |
| Status colour meanings | Navigation pattern |
| Component behaviour and states | Decoration budget |
| Accessibility floor | Canvas polarity |
| Form conventions | Imagery strategy |
| Interaction and feedback patterns | Information density |
| Terminology for shared objects | Role-specific terminology |

The left column is what makes it one product. The right column is what makes each surface
fit its job. Getting this split wrong in either direction is the classic hybrid failure:
freeze everything and the operator console is a slow brochure; free everything and you have
four products wearing one logo.

### Worked hybrid — commercial platform with five surfaces

| Layer | Category | Density | Navigation | Rhythm | Polarity |
|---|---|---|---|---|---|
| Public marketing | Marketing Website | spacious | top bar | 96px | dark (brand) |
| Customer app | Dashboard | default | side nav 240px | 48px | light |
| Operator workspace | Dashboard + Multi-Role | compact | rail + command palette | 32px | light |
| Platform administration | Multi-Role + High-Trust | compact | side nav, nested | 32px | light |
| Embedded AI assistant | Conversational AI | default | side panel 400px | n/a | inherits host |

All five share one colour ramp, one type family, one radius character, one status
vocabulary, one set of form conventions.

The assistant is the case worth studying: it appears in three of the other four layers and
must **inherit each host's density and polarity** rather than carrying its own. An assistant
panel that looks like a separate product inside your operator console is the most common
version of this mistake. See
[categories/conversational-ai.md](categories/conversational-ai.md) §Embedded assistants.

Full walkthrough: [PROJECT-INITIALIZATION.md](PROJECT-INITIALIZATION.md) §Worked example.

---

## Part 5 — Category quick reference

| Category | Choose when | Density | Guide |
|---|---|---|---|
| Conversational AI | Conversation is the primary interface | default | [guide](categories/conversational-ai.md) |
| General Informational Website | Public, clarity and findability over persuasion | default | [guide](categories/general-website.md) |
| Marketing Website | Public, conversion is the goal | spacious | [guide](categories/marketing-website.md) |
| Commercial Multi-Role Platform | 3+ roles, authenticated | default→compact | [guide](categories/commercial-multi-role-platform.md) |
| Dashboard & Administration | Authenticated, dense, daily | compact | [guide](categories/dashboard-admin.md) |
| Developer Tools | Technical audience, technical product | default | [guide](categories/developer-tools.md) |
| E-commerce & Transactional | Browsing and buying | default | [guide](categories/ecommerce.md) |
| Financial & High-Trust | Money, security, legal, irreversible actions | default | [guide](categories/financial-high-trust.md) |
| Content & Editorial | Long-form reading at volume | default | [guide](categories/content-editorial.md) |
| Data-Intensive Analytics | Multi-series analysis and exploration | compact | [guide](categories/data-analytics.md) |
| Spatial / Map / 3D | Map or 3D canvas is the primary surface | compact | [guide](categories/spatial-map-3d.md) |

Side-by-side comparison: [CATEGORY-COMPARISON.md](CATEGORY-COMPARISON.md).

---

## Part 6 — Selection anti-patterns

| Mistake | Why it fails | Fix |
|---|---|---|
| Choosing by industry label | Industry does not determine interaction needs. Two fintechs with different tasks need different designs | Answer Q7, Q8, Q5 |
| Choosing by admired brand | You inherit a visual identity built for someone else's product and audience | Choose category from tasks; choose tone from your own brand |
| Forcing a hybrid into one category | Produces either a slow console or a chaotic brand | Use the layering model |
| Skipping density selection | Category without density is half an answer — it is the difference between usable and exhausting | Answer Q5 and Q8 |
| Assuming dashboard means dark | Zero correlation in the corpus | Decide polarity from brand and environment |
| Treating conversational AI as a category for any AI feature | Not every AI feature is a chat | Ask whether conversation is the interface or a feature |
| Ignoring Q12 consequence-of-error | Silently drops confirmation, audit, and error-prevention requirements | Add High-Trust as supporting whenever Q12 ≥ data loss |
| Picking compact for a touch product | Breaks the 44px floor | Compact is pointer-only |
