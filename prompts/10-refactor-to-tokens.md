# Prompt 10 — Refactor components to use shared tokens

A mechanical, verifiable refactor. Intended to produce **no visual change**.

---

```
Refactor <PATHS> to consume design tokens instead of hard-coded values.

GOAL: zero visual change. This is a substitution, not a redesign.

STEP 1 — INVENTORY. Write no code yet.
Read the project DESIGN.md and the token definitions. Then list every hard-coded value in scope:

  file:line | current value | property | proposed token | exact match?

Classify each as:
  EXACT     - a token has this precise value -> substitute directly
  NEAR      - a token is within 1px or an imperceptible colour delta -> substitute, note the
              delta
  OFF-GRID  - the value is not on the spacing scale (e.g. 13px, 22px) -> propose the nearest
              scale value and flag the visual change
  NO TOKEN  - no token exists -> DO NOT invent one. Report it as a DESIGN.md gap.
  DELIBERATE- an intentional optical adjustment -> leave it, add a comment explaining why

Report the inventory and STOP. I will confirm before you change anything.

STEP 2 — SUBSTITUTE (after I confirm)
Order the work: EXACT first, then NEAR, then OFF-GRID. Do them as separate commits or separate
passes so each is independently reviewable.

Rules:
- Reference SEMANTIC tokens, not primitives. `text.secondary`, not `neutral.600`.
- If only a primitive fits, that indicates a missing semantic token — report it.
- One property type per pass (all colours, then all spacing, then all radii, then all type).
  Mixed passes are hard to review.
- Preserve the exact selector structure and specificity. Do not restructure CSS.
- Do not rename classes, props, or exports.
- Do not merge or split components.
- Do not "tidy" adjacent code.

STEP 3 — VERIFY
For each changed file, confirm:
- Computed styles are identical, or state precisely what changed and by how much
- Both light and dark themes still render correctly
- Hover, focus, active, and disabled states still render correctly
- No visual regression at 375px and 1280px
- Existing tests still pass

ABSOLUTE CONSTRAINTS
- Do NOT change behaviour, markup structure, or logic
- Do NOT invent token values. A missing token is a DESIGN.md gap for a human to fill.
- Do NOT change a value to make it "better". Off-grid values get flagged, not silently improved
  beyond the nearest scale step.
- If a substitution would visibly change appearance, report it rather than applying it.

REPORT
SUBSTITUTED      - count by category (exact / near / off-grid)
VISUAL DELTAS    - every change users could perceive, with before/after values
DESIGN.md GAPS   - values needing a token that does not exist
MISSING SEMANTICS- places where only a primitive fit, indicating an absent semantic token
LEFT ALONE       - deliberate values preserved, with reasons
VERIFIED         - what you actually checked; what you could not
```

---

## Notes

- **The inventory-then-stop structure matters.** An agent given "use tokens" in one pass will
  round values freely and produce dozens of small unintended visual changes.
- One property type per pass keeps diffs reviewable. A mixed colour-and-spacing diff across forty
  files cannot be verified by eye.
- The **MISSING SEMANTICS** output is often the most useful result: it reveals which parts of the
  design system were never actually defined.
