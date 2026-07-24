# Prompt 03 — Bring an inconsistent interface onto a system

The highest-risk prompt in the library. A redesign that breaks functionality is worse than the
inconsistency it fixed.

---

```
Bring <AREA / PATHS> onto a consistent design system.

SCOPE
- Files or routes in scope: <be explicit>
- Explicitly out of scope: <anything that must not be touched>
- Known problems: <what prompted this>

STEP 1 — AUDIT ONLY. Write no code in this step.
Produce an inventory of the actual inconsistency:
- Every distinct button style, with locations and a count of each
- Every distinct card or panel treatment
- Every colour value in use, and whether it is a token or a literal
- Every spacing value in use, and which are off-grid
- Every font size and weight in use
- Every radius value in use
- Control heights, and where adjacent controls do not align
- Missing interaction states, per component
- Missing data states (empty, loading, error), per view
- Accessibility failures: contrast, focus, keyboard, colour-only status
- Hard-coded values that should be tokens

Then identify the DOMINANT pattern for each category by count, and tell me which patterns are
genuine variants with distinct meanings versus accidental duplicates.

Present this as a report and STOP. I will confirm the direction before you change anything.

STEP 2 — PLAN (after I confirm)
Propose an ordered plan, lowest-risk first:
1. Token extraction — replace literals with existing tokens, no visual change intended
2. Consolidation — reduce variants to the dominant pattern
3. Missing states — add absent interaction and data states
4. Accessibility fixes
5. Remaining visual alignment
For each step, state what visual change users will notice, and what carries functional risk.

STEP 3 — EXECUTE (one step at a time, pausing between)

ABSOLUTE CONSTRAINTS
- Do NOT change behaviour. This is a restyle, not a rewrite.
- Do NOT alter data flow, API calls, state management, event handling, or business logic.
- Do NOT remove any feature, however odd it looks.
- Do NOT rename props, exports, or files unless I ask.
- Do NOT "improve" anything outside the audit findings.
- If a visual fix appears to require a functional change, STOP and tell me.
- Preserve every existing test. If a test breaks, the change is wrong until proven otherwise.

For each change, report: file, what changed visually, and confirmation that behaviour is
unchanged.

REPORT PER STEP
CHANGED          - file-by-file, with the visual effect of each
VISUAL DELTAS    - what users will notice
BEHAVIOUR        - explicit confirmation that nothing functional changed
DEFERRED         - findings not addressed, and why
RISKS            - anything you are unsure about
UNRESOLVED       - decisions needing a human
```

---

## Notes

- **The audit-then-stop structure is the point.** An agent given "make this consistent" in one pass
  will restructure components and break things. Separating audit from execution keeps a human in
  the loop at the moment of highest risk.
- "Dominant pattern by count" avoids the agent imposing its own preference. The codebase usually
  already contains the answer.
- Expect the audit to find more than you asked about. Fix scope creep by deferring explicitly
  rather than absorbing it.
