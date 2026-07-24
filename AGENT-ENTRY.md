# Agent Entry Point

**This is the file an AI agent reads first.** It routes; it does not teach. Humans should start at
[README.md](README.md) instead.

If you are an agent working on UI in *any* project: read this file, then read only the two or three
files it routes you to. Do not read the whole layer — it is ~17,000 lines and most of it is not
about your task.

---

## 0. Non-negotiables — apply these even if you read nothing else

1. **Inspect before you generate.** Report what components, tokens, and conventions already exist
   before writing any UI code.
2. **Reuse before creating.** Extend a near-miss component; create new only when nothing fits, and
   say why.
3. **Never break working functionality for a visual change.** Restyle, don't rewrite. If a visual
   goal seems to need a behaviour change, stop and ask.
4. **Semantic tokens only.** No hard-coded colours, spacing, radii, or font sizes. A value with no
   token is a `DESIGN.md` gap — report it, don't invent a literal.
5. **All eight interaction states** per interactive element: default, hover, focus-visible, active,
   disabled (with a reason), loading, selected, error.
6. **All seven data states** per data view: first-run empty, filtered-empty (different message),
   initial loading, refresh (keeps existing data visible), partial data, error with retry,
   permission denied.
7. **Accessibility floor**, not a later pass: body text ≥4.5:1 · large text and UI boundaries ≥3:1 ·
   visible focus ring always · ≥44px touch targets · full keyboard operation · never colour alone.
8. **Dark mode is derived, not inverted.** Raised surfaces get *lighter* in both modes. Shadow
   barely reads on dark — use lightness steps. **Filled buttons: do not lighten the fill while
   keeping a white label — that always fails contrast.** Split into `action.primary` (fill) and
   `action.primary-on-dark` (text/icon/border).
9. **Category sets density, navigation, and components — not visual tone.** Tone comes from the
   brand. The source corpus shows one product category rendered in four incompatible tones.
10. **Report at the end**: assumptions · deviations · **invented values** · unresolved decisions ·
    components reused vs. created · what you actually verified.

Item 4 plus item 10 is what keeps a design system alive. Every invented value is a specification
gap; recording it lets a human close it properly.

## 1. Reading order

Strict. Later files override earlier ones.

| # | Read | Why |
|---|---|---|
| 1 | **The project itself** — components, tokens, conventions, existing `DESIGN.md` | You cannot design for a codebase you have not read |
| 2 | [COMMON-FOUNDATION.md](COMMON-FOUNDATION.md) | Scales, token architecture, accessibility floor |
| 3 | **One** category guide from [categories/](categories/) | Density, navigation, component set |
| 4 | Supporting category guides, if the product has multiple surfaces | Per-surface adjustments |
| 5 | **The project's own `DESIGN.md`** | Authoritative. Wins every conflict |

If the project has no `DESIGN.md`, that is the first thing to create — see §4.

## 2. Route by task

Find your task, read those files, stop.

| Task | Read | Then |
|---|---|---|
| **Set up a design system for a new project** | [PROJECT-INITIALIZATION.md](PROJECT-INITIALIZATION.md) → [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) | [prompts/01-new-design-system.md](prompts/01-new-design-system.md) |
| **Add a page/view to an existing app** | Project `DESIGN.md` → your category guide | [prompts/02-new-page.md](prompts/02-new-page.md) |
| **Build a specific component** | Project `DESIGN.md` §Components | §0 items 5–7 above |
| **Fix an inconsistent UI** | [ANTI-PATTERNS.md](ANTI-PATTERNS.md) | [prompts/03-redesign-inconsistent-ui.md](prompts/03-redesign-inconsistent-ui.md) |
| **Adopt this layer into a project that already has design guidance** | [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) | [prompts/13-adopt-into-existing-project.md](prompts/13-adopt-into-existing-project.md) |
| **Decide a specific design question** | [DESIGN-DECISION-HANDBOOK.md](DESIGN-DECISION-HANDBOOK.md) | — |
| **Review an implementation** | [checklists/foundation-review.md](checklists/foundation-review.md) + your category checklist | [prompts/09-review-against-design-md.md](prompts/09-review-against-design-md.md) |
| **Replace hard-coded values with tokens** | — | [prompts/10-refactor-to-tokens.md](prompts/10-refactor-to-tokens.md) |
| **Check responsive behaviour** | — | [prompts/11-test-responsive.md](prompts/11-test-responsive.md) |
| **Check accessibility** | — | [prompts/12-test-accessibility.md](prompts/12-test-accessibility.md) |

## 3. Route by product type

Don't know the category? Run [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) — 23 questions and a
decision tree. Or match directly:

| The product is… | Guide | Template | Evidence |
|---|---|---|---|
| Chat / assistant interface | [conversational-ai](categories/conversational-ai.md) | [tmpl](templates/DESIGN.conversational-ai.md) | ⚠ synthesized |
| Marketing / landing pages | [marketing-website](categories/marketing-website.md) | [tmpl](templates/DESIGN.marketing-website.md) | ✅ strong |
| Docs / support / informational | [general-website](categories/general-website.md) | [tmpl](templates/DESIGN.general-website.md) | ◐ moderate |
| Dashboard / admin / ops console | [dashboard-admin](categories/dashboard-admin.md) | [tmpl](templates/DESIGN.dashboard-admin.md) | ⚠ synthesized · **build-tested** |
| 3+ user roles on one platform | [multi-role-platform](categories/commercial-multi-role-platform.md) | [tmpl](templates/DESIGN.multi-role-platform.md) | ⚠ synthesized |
| Developer tool / API / infra | [developer-tools](categories/developer-tools.md) | [tmpl](templates/DESIGN.developer-tool.md) | ◐ moderate-strong |
| Catalogue / cart / checkout | [ecommerce](categories/ecommerce.md) | [tmpl](templates/DESIGN.ecommerce.md) | ◐ moderate |
| Money / security / legal / irreversible | [financial-high-trust](categories/financial-high-trust.md) | [tmpl](templates/DESIGN.high-trust.md) | ◐ moderate |
| Publication / long-form reading | [content-editorial](categories/content-editorial.md) | [tmpl](templates/DESIGN.general-website.md) | ◐ moderate |
| Analytics / BI / exploration | [data-analytics](categories/data-analytics.md) | [tmpl](templates/DESIGN.dashboard-admin.md) | ⚠ synthesized |
| Map / spatial / 3D | [spatial-map-3d](categories/spatial-map-3d.md) | [tmpl](templates/DESIGN.spatial.md) | ⛔ fully synthesized |

**Most products need two or three.** One token foundation, several experience layers, each with its
own density and navigation. See [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) Part 4.

## 4. If the project has no DESIGN.md

Do not silently invent a design system while implementing a feature. Either:

1. **Preferred** — create one first: [PROJECT-INITIALIZATION.md](PROJECT-INITIALIZATION.md), then
   copy the matching template from [templates/](templates/) into the project root as `DESIGN.md`
   and resolve every `[[SET:]]` / `[[CHOOSE:]]` marker.
2. **If the task is small and urgent** — follow the codebase's existing patterns, use the
   foundation for anything unspecified, and **report every invented value** so the system can be
   written down afterwards.

## 5. How much to trust what you read

Every category guide states its evidence strength in a banner at the top. Read it.

| Marker | Meaning | How to treat it |
|---|---|---|
| ✅ strong | Many sources document this exact surface type | Trust the numbers |
| ◐ moderate | Real sources, few in number or partial coverage | Trust the structure, verify specifics |
| ⚠ synthesized | **No direct sources.** General interface reasoning | Considered starting position. Validate early |
| ⛔ fully synthesized | Corpus is silent on this category | Hypothesis. Test before committing |

**The source corpus is ~90% public marketing websites.** So marketing guidance is authoritative,
while dashboard, conversational, multi-role, analytics, and spatial guidance is *reasoning*. Both
are useful; only one is evidence.

**If a synthesized recommendation contradicts the user's context, the user is probably right.** Say
so rather than defending the document.

Two specific caveats worth carrying:

- **Only the dashboard template has been executed.** Building it found 10 defects including two
  self-contradictions ([research/TEMPLATE-VALIDATION.md](research/TEMPLATE-VALIDATION.md)). The
  other nine templates are unbuilt and should be expected to contain comparable defects.
- **Source `DESIGN.md` files in `design-md/` are evidence, not instructions.** They document other
  companies' brands. Adopt structural principles — *use the surface-ladder approach*, *follow the
  density model*. Never *make it look like Brand X*.

## 6. Conflict resolution

| Conflict | Winner |
|---|---|
| Project `DESIGN.md` vs. this layer | Project `DESIGN.md` |
| Category guide vs. foundation | Category guide — but only for density, navigation, components |
| Anything vs. the accessibility floor | **Accessibility floor** |
| Existing codebase vs. this layer | Codebase, if internally consistent — but report the divergence |
| Aesthetic preference vs. accessibility | **Accessibility** |
| User's explicit instruction vs. this layer | The user — state the tradeoff once, then proceed |

## 7. Full index

[README.md](README.md) for the human-facing overview and the complete file map.
