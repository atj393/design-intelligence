# Design Intelligence

A derived design guidance layer: category-based design systems, decision frameworks, reusable
`DESIGN.md` templates, AI agent instructions, and review checklists — synthesized from the 74
brand design analyses in the [`design-md/`](../design-md/) collection of this repository.

**What this is not:** a collection of brand design systems. The source collection already does
that, well. This layer answers a different question — *given a product I am about to build, what
design decisions should I make?*

---

## The problem this solves

The source collection tells you how 74 established websites look. It does not tell you what to do
when you are building something new. Copying one brand's system means inheriting a visual identity
built for someone else's product, audience, and constraints.

This layer extracts what generalises, separates it from what does not, and organises the result
around **product categories** rather than brands.

## Start here

| If you are… | Read |
|---|---|
| **An AI agent** | [AGENT-ENTRY.md](AGENT-ENTRY.md) — routing, not teaching. Read it, then only the 2–3 files it points to |
| **Wiring this into other projects** | [integration/README.md](integration/README.md) — skills, vendoring, cloud, Codex |
| Starting a new product | [PROJECT-INITIALIZATION.md](PROJECT-INITIALIZATION.md) |
| Unsure which design direction fits | [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) |
| Setting up scales and tokens | [COMMON-FOUNDATION.md](COMMON-FOUNDATION.md) |
| Building a specific product type | [categories/](categories/) |
| Writing a project `DESIGN.md` | [templates/](templates/) |
| Instructing an AI coding agent | [AI-AGENT-GUIDE.md](AI-AGENT-GUIDE.md) · [prompts/](prompts/) |
| Reviewing an implementation | [checklists/](checklists/) |
| Deciding a specific design question | [DESIGN-DECISION-HANDBOOK.md](DESIGN-DECISION-HANDBOOK.md) |
| Checking what not to do | [ANTI-PATTERNS.md](ANTI-PATTERNS.md) |
| Assessing how much to trust this | [VALIDATION-REPORT.md](VALIDATION-REPORT.md) |

## The workflow

```
1. Discover      product purpose, users, roles, frequency, density, constraints
                 → PROJECT-INITIALIZATION.md Stage 1

2. Select        primary category + supporting categories + density + tone
                 → CATEGORY-SELECTION.md

3. Found         tokens, scales, breakpoints, accessibility floor
                 → COMMON-FOUNDATION.md

4. Specialise    density, navigation, components, interaction patterns
                 → categories/<your-category>.md

5. Specify       write the project DESIGN.md
                 → templates/DESIGN.<category>.md

6. Build         instruct the agent
                 → AI-AGENT-GUIDE.md + prompts/

7. Verify        review the implementation
                 → checklists/
```

## Structure

```
design-intelligence/
├── README.md                        this file (humans)
├── AGENT-ENTRY.md                   entry point for AI agents — routing table
├── PROGRESS.md                      build log
├── METHODOLOGY.md                   how the synthesis was done
├── ASSUMPTIONS.md                   decisions taken, and why
├── SOURCE-INVENTORY.md              all 74 sources, what each documents
├── REPOSITORY-DISCREPANCIES.md      where the host repo does not match itself
├── COMMON-FOUNDATION.md             the general design foundation
├── CATEGORY-SELECTION.md            how to choose a design direction
├── CATEGORY-COMPARISON.md           eleven categories side by side
├── DESIGN-DECISION-HANDBOOK.md      requirement → design consequence
├── ANTI-PATTERNS.md                 failures, why they harm, corrections
├── AI-AGENT-GUIDE.md                how agents should use this layer
├── PROJECT-INITIALIZATION.md        six-stage setup, with a worked example
├── VALIDATION-REPORT.md             what was checked; what is uncertain
├── SOURCES.md                       source identification
├── ATTRIBUTION.md                   credit and relationship to the original
├── LICENSING-CONSIDERATIONS.md      repository licence vs. third-party marks
├── PUBLISHING-CHECKLIST.md          pre-publication checks
├── categories/    (12 files)        one guide per product category
├── templates/     (12 files)        copy-paste DESIGN.md templates
├── prompts/       (13 files)        reusable agent prompts
├── checklists/    (6 files)         review checklists
├── research/      (8 files)         normalized analysis, traceability, validation results
└── integration/   (7 files)         use this layer from other projects, cloud, and other agents
```

### Using it from other projects

This layer is designed to be the design reference for **every** project, not just this one. Four
deployment modes — personal skill, vendored copy, project skill, published repo — are documented in
[integration/README.md](integration/README.md), with a resolver that finds the layer automatically
and a `vendor.py` that copies it into any repo with links rewritten.

## Categories covered

Conversational AI · general informational websites · marketing websites · commercial multi-role
platforms · dashboards and administration · developer tools · e-commerce · financial and
high-trust · content and editorial · data-intensive analytics · spatial/map/3D.

Full list with evidence strength: [categories/README.md](categories/README.md).

---

## Honest limits

Read this section before trusting any specific recommendation.

**The source corpus is ~90% public marketing websites.** That is not a criticism of the collection —
it is what the collection is for. But it bounds what can be derived from it. The source files
themselves say so repeatedly; many state that in-product surfaces, authenticated chrome, hover
states, and form-validation states were not captured.

| Layer content | Evidence |
|---|---|
| Token architecture, scales, breakpoints, typography rules | **Strong** — 74 sources |
| Marketing website guidance | **Strong** — 55 direct sources |
| Developer tools, e-commerce, editorial, high-trust, general website | Moderate — partial direct evidence |
| Dashboard, analytics, multi-role, conversational | **Reasoning, not evidence** — no direct sources |
| Spatial / map / 3D | **Fully synthesized** — corpus is silent |
| Interaction states, empty/loading/error patterns | Synthesized — the corpus documents almost none |
| Accessibility floor | From the WCAG specification, not from the corpus |

**The uncomfortable pattern:** the categories most in demand for new software are the ones this
corpus supports least. Every category guide states its own evidence strength in a banner at the
top. Where guidance is labelled synthesized, it is reasoning you can argue with — and if your
context contradicts it, your context is probably right.

**Other limits:**

- Source accuracy against live websites was not re-verified. Values may have drifted.
- Contrast ratios asserted by source files were not recomputed. 56 sources claim WCAG conformance;
  none demonstrates a computed ratio. This layer takes its accessibility floor from the
  specification instead.
- Thirteen source files contain machine-generated application-UI component blocks that are
  extrapolations, not observations. They are not treated as evidence here. See
  [REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D7.

## Working principles

1. **Modal value plus range, never an average.** The mean of a 0px-radius and a 40px-radius system
   is 10px — a value neither would accept.
2. **Frequency is reported as frequency, not endorsement.** That 61 of 74 sources use 96px section
   rhythm is a fact about marketing websites, not advice for an operations console.
3. **Category determines density, navigation, and components — not visual tone.** The corpus shows
   the same product category rendered in four incompatible tones. Tone is a brand decision.
4. **Synthesized guidance is labelled.** Every guide carries an evidence banner.
5. **Structural principles, not identities.** Adopt the surface-ladder approach; do not reproduce a
   brand's palette.

## Relationship to the source collection

This is a **derived layer inside** the [Awesome DESIGN.md](../README.md) repository. It adds
synthesis; it changes nothing.

- No file under [`design-md/`](../design-md/) was created, modified, renamed, or deleted.
- The source files are cited by relative path throughout, so every claim is checkable.
- No brand assets, logos, screenshots, or trademarked material were copied into this layer.
- Brand names appear only in source citations and research tables, never in normative guidance.

**Not affiliated with, endorsed by, or sponsored by any brand referenced in the source research.**
See [ATTRIBUTION.md](ATTRIBUTION.md) and
[LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md).

## Contributing

Useful contributions, in rough order of value:

1. **Evidence for the weak categories.** Documented dashboard, conversational, multi-role, or
   spatial interfaces would upgrade four guides from reasoning to evidence.
2. **Corrections where guidance is wrong in practice.** Especially in synthesized sections — they
   are arguments, and arguments can be beaten.
3. **Computed contrast verification** for the source palettes, which would close the D9 gap.
4. **Additional source coverage** in the parent collection, which flows through to this layer.

When contributing, keep the discipline: state your evidence, distinguish observation from
reasoning, and do not promote a single source's choice to a universal rule.
