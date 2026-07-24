# Prompt 01 — Create a design system for a new application

Use when a project has no `DESIGN.md`. Produces the design system, not UI code.

---

```
I need a DESIGN.md for <PRODUCT NAME>.

CONTEXT
- What it does: <one or two sentences>
- Primary users: <be specific: role, environment, device>
- User roles: <count and names>
- Public, authenticated, or both: <answer>
- How often one person uses it: <once | rarely | weekly | daily | all day>
- Core workflows: <top 3-5>
- Primary devices: <desktop | mobile | both, with split if known>
- Information density: <sparse | moderate | dense | very dense>
- Consequence of a user error: <trivial | recoverable | data loss | financial | regulatory>
- Accessibility requirement: <WCAG AA minimum | AAA | regulated procurement>
- Brand maturity: <none | guidelines exist | strong and enforced>
- Technical constraints: <framework, existing component library, SSR, performance budget>

STEP 1 — INSPECT THE PROJECT
Before writing anything, examine the codebase and report:
- Existing component library or design system, if any
- Components already available, and their names
- How styling and tokens are delivered (CSS variables, Tailwind config, token JSON, theme object)
- Existing naming and file conventions
- Any existing colour, spacing, or type values already in use
- Whether light/dark theming exists and how it switches
Report what you found before proceeding. If the project already has an implicit system,
document it rather than replacing it.

STEP 2 — SELECT THE CATEGORY
Work through design-intelligence/CATEGORY-SELECTION.md. Output the recommendation block:
primary category, supporting categories, density mode, visual tone, canvas polarity,
navigation model, accent count, container and measure, section rhythm, design risks,
evidence strength, open questions.
State your reasoning for the primary category in two or three sentences.

STEP 3 — PRODUCE THE DESIGN.md
Start from design-intelligence/templates/DESIGN.<category>.md, or
templates/DESIGN.foundation.md if no category template fits.
Resolve every [[SET: ...]] and [[CHOOSE: ...]] marker. Do not leave placeholders.

Requirements:
- Two-layer tokens: primitives (raw values) and semantics (intent). Components consume
  semantics only.
- Complete semantic set: surface, text, border, action, status, focus, utility.
- Light and dark specified SEPARATELY. Do not invert one to produce the other.
- Type scale with size, weight, line-height, tracking, and intended use per step.
  Adjacent steps 1.15x-1.35x apart.
- Spacing on a 4px grid, 8px increments preferred.
- One radius character, applied consistently, with the nesting rule stated.
- Component specs including ALL EIGHT interaction states: default, hover, focus-visible,
  active, disabled, loading, selected, error.
- Data states: first-run empty, filtered-empty, initial loading, refresh loading,
  partial data, error, permission denied.
- Responsive behaviour per element, naming which applies: resize, reflow, collapse, stack,
  scroll, drawer, transform, defer, omit.
- Accessibility commitments, checkable.
- A substitution note for any proprietary typeface. Without it the system is unusable
  by anyone who cannot license the font.
- An agent prompt guidance section.

CONSTRAINTS
- Do not reproduce any brand's identity. The source files in design-md/ are evidence of
  technique, not templates to copy. Adopt structural principles; derive your own values.
- One accent colour unless you can state what each additional colour maps to structurally.
- Every measurement must be defensible against the context above. If you cannot justify a
  value from the requirements, say so rather than picking one.
- Do not write UI code in this task.

STEP 4 — VALIDATE
Pick the two most important screens in this product. Walk through each using only the
DESIGN.md and confirm it specifies everything needed. List what was missing and add it.

REPORT
ASSUMPTIONS      - what you assumed and why
DEVIATIONS       - where you departed from the foundation or category guide, and why
INVENTED VALUES  - values the requirements did not determine (these need human confirmation)
UNRESOLVED       - decisions needing a human
CATEGORY BASIS   - why this primary category, and its evidence strength
```

---

## Notes

- If the answers to CONTEXT are thin, ask for the missing ones before starting. A design system
  derived from guesses will need rebuilding.
- The STEP 4 validation catches most specification gaps — do not skip it.
- Category guides with weak evidence (dashboard, conversational, multi-role, spatial) should be
  validated with real users early. The prompt asks the agent to state evidence strength so this
  is visible.
