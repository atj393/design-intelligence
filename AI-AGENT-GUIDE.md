# AI Agent Usage Guide

How an AI coding agent should use this layer to generate, review, and refactor interfaces.

---

## 1. Reading order

**Fixed. Read in this order, and let later files override earlier ones.**

| # | Read | Purpose |
|---|---|---|
| 1 | **Project context** — the repo, existing components, tokens, conventions | You cannot design for a codebase you have not read |
| 2 | [COMMON-FOUNDATION.md](COMMON-FOUNDATION.md) | Scales, token architecture, accessibility floor |
| 3 | The **primary category guide** in [categories/](categories/) | Density, navigation, component set |
| 4 | Any **supporting category guides** | For secondary surfaces |
| 5 | The **project `DESIGN.md`** | Authoritative. Wins every conflict |

**Why this order:** the foundation gives coherent defaults; the category corrects them for the
product type; the project `DESIGN.md` encodes decisions already made. Reading the project file
first means you interpret it without knowing what it is deviating from.

**Consult as needed, not in sequence:**

- [DESIGN-DECISION-HANDBOOK.md](DESIGN-DECISION-HANDBOOK.md) — when a document says "choose"
- [ANTI-PATTERNS.md](ANTI-PATTERNS.md) — before generating, and during review
- [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) — when the category is not yet decided
- [checklists/](checklists/) — when reviewing

## 2. The source `DESIGN.md` files are evidence, not instructions

The 74 files in `design-md/` are the raw material this layer was derived from. When working on a
product:

| Do | Do not |
|---|---|
| Read them to understand how a structural technique works | Copy one into a project as its design system |
| Cite them when explaining where a principle came from | Reproduce a brand's palette, typeface, or identity |
| Use "adopt the surface-ladder approach" reasoning | Use "make it look like Brand X" reasoning |

They document **other companies' brands**. Reproducing one means shipping someone else's visual
identity, built for their product, their audience, and their constraints — and implying an
endorsement that does not exist. See [LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md).

**Language matters here.** Use: *adopt the structural principle · use the density model · follow
the hierarchy approach · adapt the interaction pattern*. Never: *clone · copy exactly · make it
identical to · replicate*.

## 3. Non-negotiable behaviours

These apply to every prompt in [prompts/](prompts/) and to any ad-hoc request.

### Inspect before generating

Before writing UI code, establish and **report**:

1. What component library or design system already exists
2. Which components are already available and what they are called
3. How tokens are delivered — CSS variables, Tailwind config, token JSON, theme object
4. Existing naming and file conventions
5. Whether a project `DESIGN.md` exists
6. Whether light/dark theming exists and how it switches

Generating a new button in a codebase that has three is how design systems degrade.

### Reuse before creating

| Situation | Action |
|---|---|
| A component exists and fits | Use it |
| A component exists and nearly fits | Extend it — add a variant or a prop |
| Nothing fits | Create one, following existing conventions, and **say why** |
| Three similar components exist | Flag the duplication; do not add a fourth |

### Never break working functionality for a visual change

A restyle changes appearance. It does not change behaviour, remove features, alter data flow, or
rewrite working logic. If achieving a visual goal appears to require a functional change, **stop
and report** rather than proceeding.

### Consume tokens, never hard-code

Every colour, spacing value, radius, font size, and duration references a token. If a needed value
has no token, that is a gap in the `DESIGN.md` — report it rather than inventing a literal.

### Implement all states

For every interactive component: default, hover, focus-visible, active, disabled, loading,
selected, error.

For every data-bearing view: first-run empty, filtered-empty, initial loading, refresh loading,
partial data, error, permission denied.

**This is the most commonly skipped work and the most commonly filed bug.**

### Meet the accessibility floor

Contrast, focus visibility, keyboard operability, touch targets, colour independence, labels,
heading structure, reduced motion. Not a later pass — a constraint on the code you write now.

### Report at the end

Always, in this shape:

```
ASSUMPTIONS
  - <what you assumed and why>

DEVIATIONS
  - <where you departed from DESIGN.md or a guide, and why>

INVENTED VALUES
  - <values not specified anywhere — these are gaps to fix in DESIGN.md, not in code>

UNRESOLVED
  - <decisions needing a human>

REUSED / CREATED
  - reused: <components>
  - created: <components, with justification>
```

The **INVENTED VALUES** section is what keeps the system from drifting. Every invented value is a
specification gap; recording it lets someone close it properly.

## 4. Prompt library

Twelve prompts in [prompts/](prompts/), each with an inspect step, constraints, and a required
report.

| Prompt | Use for |
|---|---|
| [01-new-design-system.md](prompts/01-new-design-system.md) | Creating a `DESIGN.md` for a new product |
| [02-new-page.md](prompts/02-new-page.md) | Adding a page or view to an existing app |
| [03-redesign-inconsistent-ui.md](prompts/03-redesign-inconsistent-ui.md) | Bringing an inconsistent interface onto a system |
| [04-chatbot-interface.md](prompts/04-chatbot-interface.md) | Conversational or assistant UI |
| [05-marketing-website.md](prompts/05-marketing-website.md) | Marketing or conversion pages |
| [06-multi-role-platform.md](prompts/06-multi-role-platform.md) | Role-based commercial platform |
| [07-admin-dashboard.md](prompts/07-admin-dashboard.md) | Dashboard or administration surface |
| [08-spatial-interface.md](prompts/08-spatial-interface.md) | Map, spatial, or 3D interface |
| [09-review-against-design-md.md](prompts/09-review-against-design-md.md) | Auditing code against `DESIGN.md` |
| [10-refactor-to-tokens.md](prompts/10-refactor-to-tokens.md) | Replacing hard-coded values with tokens |
| [11-test-responsive.md](prompts/11-test-responsive.md) | Verifying responsive behaviour |
| [12-test-accessibility.md](prompts/12-test-accessibility.md) | Verifying accessibility |

## 5. Working with an existing codebase

### If a project `DESIGN.md` exists

It is authoritative. Where it conflicts with anything in this layer, it wins. Where it is silent,
fall back to the category guide, then the foundation. Where you had to invent a value, report it as
a gap in the `DESIGN.md`.

### If no `DESIGN.md` exists

Two options, and asking is usually right:

1. **Preferred:** derive one first, using
   [PROJECT-INITIALIZATION.md](PROJECT-INITIALIZATION.md) and prompt 01. Building a screen
   without a system means the next screen disagrees with it.
2. **If the task is small and urgent:** work from the codebase's existing patterns, follow the
   foundation for anything unspecified, and report every invented value so the system can be
   written down afterwards.

Do not silently invent a design system while implementing a feature.

### If the codebase contradicts itself

Common. Do not pick a side silently.

1. Identify the dominant pattern by count.
2. Follow the dominant pattern for new work.
3. Report the inconsistency with locations and counts.
4. Do not refactor unrelated code as a side effect of a feature — propose it separately.

## 6. Conflict resolution

| Conflict | Winner |
|---|---|
| Project `DESIGN.md` vs. category guide | Project `DESIGN.md` |
| Category guide vs. foundation | Category guide (density, navigation, components only) |
| Foundation vs. accessibility floor | **Accessibility floor, always** |
| Existing codebase vs. this layer | Codebase, if consistent — but report the divergence |
| Brand guidelines vs. this layer | Brand, for tone; this layer for structure and accessibility |
| Aesthetic preference vs. accessibility | **Accessibility** |
| User's explicit instruction vs. this layer | The user's instruction — but state the tradeoff once |

## 7. What agents get wrong most often

Ordered by frequency in practice. Each maps to an entry in
[ANTI-PATTERNS.md](ANTI-PATTERNS.md) Part 1.

| Failure | Guard |
|---|---|
| Only the happy path is built | Enumerate states before writing code |
| Hard-coded colours and spacing | Search your own output for hex values and literal `px` |
| A new component duplicating an existing one | Inspect first; report what you found |
| Marketing type scale in an application | Check the category's display ceiling |
| Everything wrapped in a rounded shadowed card | Ask what the card groups |
| Missing focus states | Never `outline: none` without a replacement |
| Status by colour alone | Colour + icon + text |
| Mobile as a compressed desktop | Re-rank priority; transform tables |
| Decorative gradients and glows | One decorative device maximum, marketing surfaces only |
| Animation on frequently-repeated interactions | Justify against causality/hierarchy/progress/spatial |
| Silent invention of unspecified values | Report every one |
| Refactoring working code during a restyle | Restyle only; propose refactors separately |

## 8. Verification before claiming done

Do not report success without checking. Minimum:

- [ ] It renders without console errors
- [ ] Every interaction state exists and is visibly distinct
- [ ] Empty, loading, and error states exist
- [ ] Keyboard-navigable; focus always visible
- [ ] Tested at 375px and 1280px
- [ ] Both themes checked, if the project supports both
- [ ] No hard-coded values that should be tokens
- [ ] Contrast verified on new colour pairings
- [ ] Existing functionality unchanged
- [ ] Report delivered in the §3 shape

**If verification was not possible, say so and say why.** "Should work" is not "works".

## 9. Honest limits of this layer

An agent should know how much to trust what it is reading.

| Layer content | Trust |
|---|---|
| Token architecture, scales, breakpoints, typography rules | High — corpus-backed across 74 sources |
| Marketing website guidance | High — 55 direct sources |
| Developer tools, e-commerce, editorial, high-trust, general website | Moderate — partial direct evidence |
| Dashboard, analytics, multi-role, conversational guidance | **Reasoning, not evidence** — no direct sources |
| Spatial guidance | **Fully synthesized** — corpus is silent |
| Interaction states, empty/loading/error patterns | Synthesized — the corpus documents almost none |
| Accessibility floor | From the WCAG specification, not from the corpus |

Every category guide states its own evidence strength in a banner at the top. When guidance is
synthesized, it is reasoning that can be argued with — so if a user's context contradicts it,
the user is probably right. Say so rather than defending the document.
