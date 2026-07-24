# Prompt 02 — Design a new page inside an existing application

---

```
Build <PAGE OR VIEW NAME> in this application.

WHAT IT DOES
- Purpose: <what the user accomplishes here>
- Primary user / role: <who>
- Primary action: <the one thing they most need to do>
- Data shown: <entities, roughly how many, which fields matter>
- Entry points: <how users arrive>
- Exit points: <where they go next>

STEP 1 — INSPECT FIRST. Report before writing code:
- The project DESIGN.md (read it fully; it overrides the design-intelligence layer)
- Existing components that could serve this page, by name
- The closest existing page — I want this to look like it belongs
- Layout primitives available (page shell, grid, panel, section components)
- How tokens are referenced in this codebase
- Routing and data-fetching conventions
Tell me what you found and what you plan to reuse before generating anything.

STEP 2 — BUILD
Follow, in order: the project DESIGN.md, then the primary category guide, then
COMMON-FOUNDATION.md. Match the existing code's conventions, naming, and structure.

Required:
- Reuse existing components. Extend them if close. Create new ones only if nothing fits,
  and say why.
- Reference semantic tokens by name. No hard-coded colours, spacing, radii, or font sizes.
- All eight interaction states on every interactive element: default, hover, focus-visible,
  active, disabled, loading, selected, error.
- All data states: first-run empty (with a primary action), filtered-empty (distinct message,
  offer to clear filters), initial loading (skeleton matching final layout), refresh loading
  (keep existing data visible), partial data, error (with retry), permission denied
  (say what is needed and who grants it).
- One primary action, visually dominant. Everything else subordinate.
- Responsive: state per element which behaviour applies (resize, reflow, collapse, stack,
  scroll, drawer, transform, defer, omit). Wide tables scroll with a pinned identifying
  column, or transform to cards — never squeeze.
- Keyboard operable end to end; visible focus everywhere.
- Contrast met on any new colour pairing, in both themes if the project has both.

CONSTRAINTS
- Do not modify existing components unless the change is required and additive. If a shared
  component needs changing, tell me before doing it.
- Do not change data models, API calls, or business logic.
- Do not introduce a new dependency without asking.
- Do not refactor unrelated code.
- Do not invent a spacing, colour, or size value that is not in the token set. If you need one
  that does not exist, report it as a DESIGN.md gap.

REPORT
REUSED           - components used as-is
EXTENDED         - components given a new variant, and what changed
CREATED          - new components, with justification for each
ASSUMPTIONS      - what you assumed about data, permissions, or behaviour
DEVIATIONS       - departures from DESIGN.md, with reasons
INVENTED VALUES  - anything not covered by tokens or DESIGN.md
UNRESOLVED       - decisions needing a human
VERIFIED         - what you actually checked, and what you could not check
```

---

## Notes

- The "closest existing page" instruction does a lot of work — it is the fastest way to get output
  that belongs in the codebase rather than merely satisfying the spec.
- If the agent reports that no `DESIGN.md` exists, consider running
  [01-new-design-system.md](01-new-design-system.md) first. Building pages without a system means
  the next page disagrees with this one.
