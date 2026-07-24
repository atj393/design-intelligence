# Prompt 13 — Adopt Design Intelligence into an existing project

Paste-and-run. **Requires no project details** — the agent discovers the project by inspecting the
workspace it is already running in. The only editable line is the source location, and even that has
a working default.

Use when a project already has design guidance — a research report earlier in the conversation, a
style guide, a brand deck, an existing `DESIGN.md` — and you want it reconciled against this layer,
with this layer taking priority on standards.

Produces three deliverables: a **gap analysis**, a **theme definition**, and a **phased redesign
plan**. It writes no code.

---

```
Redesign this project's UI using an external design standard as the primary reference.
You are already running inside the project — discover it yourself; I am not going to
describe it to you.

════════════════════════════════════════════════════════════════════════
THE DESIGN STANDARD — the only thing configured here
════════════════════════════════════════════════════════════════════════
Resolve in this order and use the FIRST one that works:

  1. LOCAL   d:/repos/support/design-intelligence
  2. LOCAL   d:/repos/support/awesome-design-md/design-intelligence
  3. VENDORED ./.design-intelligence/            (inside this repo, if present)
  4. PUBLIC  https://github.com/atj393/design-intelligence
             fetch files from:
             https://raw.githubusercontent.com/atj393/design-intelligence/main/<path>

If a local path exists, prefer it — it is faster and may be newer. Otherwise fetch
from the public repo; it is complete and self-sufficient.

Confirm you found the standard by reading AGENT-ENTRY.md, and tell me which source
resolved. If none resolve, STOP and tell me — do not proceed from memory and do not
invent design values.
════════════════════════════════════════════════════════════════════════

STEP 1 — DISCOVER THIS PROJECT YOURSELF

Inspect the workspace and report before reading anything else:

- Project name, and what it does
- EVERY distinct UI surface: for each, its folder, what kind of interface it is
  (chat, dashboard, marketing site, docs, admin console, catalogue, map...), and who
  uses it. A repo often holds several — do not assume one.
- Framework, component library, styling approach, build tooling
- Whether the UI is translated, and into which languages
- Any existing design guidance you can find:
    * a design research report or plan earlier in THIS conversation
    * DESIGN.md, STYLEGUIDE.md, brand docs, docs/ folders, CLAUDE.md, AGENTS.md
    * theme config, token files, variables files
  Say which of these exist. If a design report appears above in this conversation,
  treat it as the project's existing guidance and read it in full.
- If you find NO existing guidance anywhere, say so — then skip Step 4 and derive
  the theme in Step 5 from the code and brand assets alone.

Report all of this as a short inventory before continuing.

STEP 2 — READ THE STANDARD, IN THIS ORDER

  1. AGENT-ENTRY.md              routing + the ten non-negotiables
  2. COMMON-FOUNDATION.md        token architecture, scales, dark mode, a11y floor
  3. CATEGORY-SELECTION.md       only what you need to classify the surfaces you found
  4. One category guide PER SURFACE from categories/ — surfaces of different kinds get
     different guides. Do not force one category onto the whole repo.
  5. ANTI-PATTERNS.md, Part 1    the 20 recurring failures

Do not read the whole layer — it is large and most of it will not apply. Read the
above and stop.

For EVERY category guide you use, quote its EVIDENCE STRENGTH banner from the top of
the file. Parts of this standard are corpus-backed and parts are explicitly reasoning
rather than evidence. I need to know which I am getting before I act on it. Do not
paraphrase this away or omit it.

STEP 3 — INVENTORY THE CURRENT DESIGN STATE

Report on the actual code, concretely:

- Which component-library components are already used, and how theming is configured
- Every colour, spacing value, font size, and radius currently in use — and for each,
  whether it is a token or a hard-coded literal
- Which values are defined in a tokens/variables file AND ALSO hard-coded elsewhere
- What the surfaces share versus duplicate
- Existing interaction states per component (hover / focus / disabled / loading)
- Existing data states per view (empty / loading / error / permission-denied)
- Accessibility state: focus visibility, computed contrast on the main text pairs,
  keyboard operability, touch target sizes
- Layout assumptions that would break under longer translated text

Be specific. "Uses SCSS variables" is not useful. "18 colours in _variables.scss, 11
of which are also hard-coded in components" is useful.

STEP 4 — PRECEDENCE  (the part I care most about)

DESIGN INTELLIGENCE WINS on HOW TO DESIGN:
  token architecture (primitives -> semantics; components consume semantics only) ·
  type / spacing / radius / elevation scales and their ratios · density model and
  which density each surface gets · required interaction states and data states ·
  accessibility floor · category-appropriate navigation, layout and component set ·
  anti-patterns · dark mode derivation

THE PROJECT'S EXISTING GUIDANCE WINS on FACTS ABOUT THIS PRODUCT:
  actual brand colours, logo, typeface licences · real user research and personas ·
  business and compliance requirements · technical constraints and the existing
  component library · domain terminology · anything measured or observed about THIS
  product

NEITHER wins automatically on VISUAL TONE. The standard is explicit that category
determines density, navigation and components — NOT tone. Derive tone in Step 6.

ONE CARVE-OUT, and I want it applied: where a Design Intelligence recommendation is
labelled SYNTHESIZED and the project's existing guidance contradicts it with actual
evidence about this product, the existing guidance wins — flag it as a conflict and
give me both sides rather than silently choosing. The standard says the same about
itself: where my context contradicts its synthesized reasoning, my context is
probably right. Do not use this to sidestep the standard; apply it only where there
is real evidence on the other side.

STEP 5 — DELIVERABLE 1: GAP ANALYSIS

A table, one row per meaningful difference:

| # | Topic | Existing guidance says | Design Intelligence says | Resolution | Why | Effort |

Resolution: ADOPT-DI · KEEP-EXISTING · MERGE · CONFLICT-NEEDS-DECISION
Effort: S / M / L

Cover at minimum: colour system and token structure · typography scale · spacing
scale · density · radius · elevation · navigation model · component inventory ·
interaction states · data states · dark mode · accessibility · responsive strategy ·
motion.

Then summarise the counts, and list every CONFLICT-NEEDS-DECISION separately at the
end — those are what I have to answer before you go further.

(If there was no existing guidance, replace this with a straight conformance gap:
what the code does today versus what the standard requires.)

STEP 6 — DELIVERABLE 2: THEME DEFINITION

Derive the visual theme from brand and audience, NOT from product category.

Produce:
- Theme name and a one-line character statement
- Canvas polarity per surface (light / dark / both / dual-track) and the reason
- Decoration budget: none / minimal / moderate / expressive
- What carries visual interest; what must recede
- Accent strategy: how many accents, and for any beyond the first, the structural
  thing it maps to
- A complete token set as a table: primitives -> semantics, with LIGHT AND DARK
  SPECIFIED SEPARATELY (dark is derived, never inverted)
- Type scale: size / weight / line-height / tracking / intended use per step
- Spacing, radius and elevation scales
- Density mode PER SURFACE, with the visit-frequency reasoning. Surfaces of different
  kinds must not share one density.

Every colour pair needs a COMPUTED contrast ratio, in both modes — the actual number,
not "should pass". Include filled-button label-on-fill pairs specifically; that is the
pair most often broken by a dark-mode rule.

State how this maps onto the project's existing component library and theming API. I
am theming the library, not replacing it.

STEP 7 — DELIVERABLE 3: PHASED REDESIGN PLAN

Ordered phases, lowest risk first. For each: what changes, which files, what users
will notice, what could break, how to verify, and whether it is INDEPENDENTLY
SHIPPABLE. I want to be able to stop after any phase and still have a coherent product.

Suggested shape — adjust if your inventory says otherwise:
  Phase 0  Token foundation. Define semantics. No visual change intended.
  Phase 1  Replace hard-coded values with tokens. No visual change intended.
  Phase 2  Typography and spacing onto the new scales.
  Phase 3  Component-by-component restyle, most-used first.
  Phase 4  Missing interaction states.
  Phase 5  Missing data states.
  Phase 6  Accessibility fixes.
  Phase 7  Dark mode, if in scope.
  Phase 8  Per-surface density and navigation corrections.

Call out explicitly anything that CANNOT be done as a restyle and would require a
functional change — I will decide those separately.

STEP 8 — RISKS AND OPEN QUESTIONS

- What is most likely to break
- Where the existing component library constrains the standard, and how you propose to
  work WITHIN it rather than around it
- Which recommendations rest on synthesized rather than corpus-backed evidence, so I
  know what to validate with real users
- Every decision you need from me, numbered so I can answer inline

════════════════════════════════════════════════════════════════════════
CONSTRAINTS — apply to this plan and to any later implementation
════════════════════════════════════════════════════════════════════════
- DO NOT write or change any code in this response. Plan only. I approve phases one
  at a time.
- Never break working functionality for a visual change. This is a restyle, not a
  rewrite. If a visual goal appears to need a behaviour change, say so and stop.
- Reuse the existing component library. Theme and extend it. Do not replace it, and do
  not add a competing UI dependency without asking.
- Semantic tokens only in components. A value you need that has no token is a gap in
  the design system — report it rather than inventing a literal.
- All eight interaction states: default, hover, focus-visible, active, disabled (with
  a visible reason), loading, selected, error.
- All seven data states: first-run empty, filtered-empty (a DIFFERENT message),
  initial loading, refresh (keeps existing data visible), partial data, error with
  retry, permission denied.
- Accessibility is a constraint on the plan, not a later phase: body text >=4.5:1,
  large text and meaningful UI boundaries >=3:1, visible focus always, >=44px touch
  targets, full keyboard operation, never colour alone.
- If the UI is translated, do not fix widths to one language's text length. Assume
  ~30% expansion.
- Preserve every existing test. A broken test means the change is wrong until proven
  otherwise.

════════════════════════════════════════════════════════════════════════
IF THE STANDARD IS UNREACHABLE — apply at least this, and tell me
════════════════════════════════════════════════════════════════════════
4px spacing grid, 8px increments · 16px body text, never below 14px (16px on mobile) ·
prose measure 60-70 characters regardless of container width · type steps 1.15x-1.35x
apart, line-height falls as size rises · breakpoints 480/768/1024/1280/1440 · ONE
accent reserved for primary action, brand mark and focus · 40px default control
height, 44px minimum on touch, input height matches button height · 24px card
padding · 8px control radius, one radius character throughout · border-first
elevation, lightness steps rather than shadow on dark canvases · display ceiling by
surface: marketing 56-80px, docs 36-56px, application 24-32px, dashboard 20-28px.

Start with the source resolution, then Step 1. Work through to Step 8.
```

---

## Notes on using this

### It takes no project arguments

Everything about the project is discovered in Step 1 — name, surfaces, stack, translation, existing
guidance. That is deliberate: describing the project by hand is where these prompts go stale, and an
agent already sitting in the workspace can see more than a hand-written summary would say.

The only line you might ever edit is the source list at the top, and it already ends in a public
fallback that works from anywhere.

### Why precedence is split three ways

A blanket "the external standard always wins" throws away the one thing an external standard cannot
know: **facts about your product.** Brand colours, user research, compliance obligations, and the
existing component library are project facts. Scales, state coverage, and the accessibility floor
are methodology. The split keeps the standard authoritative where it has authority and defers where
it does not.

The carve-out for synthesized guidance is not a loophole — it is what
[`AGENT-ENTRY.md`](../AGENT-ENTRY.md) §5 already instructs. Five of eleven category guides are
reasoning rather than evidence. An agent that overrode measured project evidence with synthesized
reasoning would be following the letter of the instruction and breaking its intent.

### Multi-surface repositories

Step 1 asks for *every* UI surface, and Step 2 asks for one category guide per surface. A repository
holding a chat client and an admin console contains **two different categories**, and the expected
outcome is one shared token foundation with per-surface density and navigation — the layering model
in [`CATEGORY-SELECTION.md`](../CATEGORY-SELECTION.md) Part 4.

A chat UI at dashboard density is wrong. An admin console at chat density is also wrong. One token
set serves both.

### Component libraries

Where a project already uses Material, PrimeNG, Ant, shadcn or similar, the instruction to *reuse*
matters more than anywhere else. The realistic outcome is theming the library to the derived tokens,
not replacing its components. Step 8 asks the agent to name where the library constrains the
standard — which surfaces that tension rather than letting the agent quietly fight the library.

### Getting an implementation afterwards

This prompt produces a plan. To execute a phase:

> Implement Phase 1 only. Report every file changed, the visual effect of each change, and confirm
> no behaviour changed. Stop at the end of the phase.

For token work specifically, [`10-refactor-to-tokens.md`](10-refactor-to-tokens.md) is more thorough
— it inventories before substituting and separates exact matches from approximations.
