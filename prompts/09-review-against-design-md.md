# Prompt 09 — Review generated code against DESIGN.md

Review only. No changes without a separate instruction.

---

```
Review <PATHS> against this project's DESIGN.md.

DO NOT CHANGE ANY CODE. Produce findings only. I will decide what to fix.

STEP 1 — READ
- The project DESIGN.md, in full
- design-intelligence/COMMON-FOUNDATION.md
- The relevant category guide
- The code in scope

STEP 2 — REPORT FINDINGS, grouped and ordered by severity within each group.

A. TOKEN COMPLIANCE
- Every hard-coded colour (hex, rgb, hsl, named) that has a token
- Every hard-coded spacing value, and whether it is on the 4px grid
- Every hard-coded font size, weight, line-height, radius, duration
- Values used that exist in NO token — these are DESIGN.md gaps, not just code defects
- Primitive tokens referenced directly where a semantic token exists

B. INTERACTION STATES — per interactive component, which of the eight are missing:
default, hover, focus-visible, active, disabled, loading, selected, error
Flag specifically: any `outline: none` without a replacement; any disabled state with no
explanation of why; hover and focus that look identical; selected indistinguishable from hover.

C. DATA STATES — per data-bearing view, which are missing:
first-run empty, filtered-empty (distinct from first-run), initial loading, refresh loading
(does it blank existing data?), partial data, error with retry, permission denied
This is the most commonly missing category. Check it carefully.

D. ACCESSIBILITY
- Contrast failures, with computed ratios and the pair involved, in BOTH themes
- Missing or invisible focus indicators
- Anything unreachable or unusable by keyboard; focus traps
- Touch targets below 44px, or adjacent targets closer than 8px
- Status or meaning conveyed by colour alone
- Form fields without programmatic labels; errors not associated with fields
- Placeholder used as a label
- Heading structure: multiple h1, skipped levels
- Missing or unhelpful alt text
- Async changes not announced (live regions)
- prefers-reduced-motion not honoured
- Charts without a data alternative; map-only information

E. DESIGN.md CONFORMANCE
- Type sizes outside the documented scale
- Display type above the category ceiling for this surface
- Density inconsistency: does spacing, control height, and type size agree on one density?
- Radius values outside the documented ladder; nesting rule violated
- Elevation mechanisms mixed at one level (border + shadow + surface lift)
- More accents in use than DESIGN.md permits, or accents used decoratively
- Prose running wider than the documented measure
- Navigation destinations duplicated across two systems

F. RESPONSIVE
- Elements with no defined behaviour at a breakpoint
- Wide tables that shrink rather than scroll-with-pinned-column or transform
- Hover-only interactions with no touch equivalent
- Layout shift sources: media without intrinsic dimensions, unreserved async content
- Sticky chrome exceeding ~20% of viewport height
- Capabilities hidden on small screens without an explanatory message

G. CONSISTENCY
- Duplicate components serving the same purpose, with counts and locations
- Adjacent controls of mismatched heights
- Inconsistent naming against existing conventions

FOR EACH FINDING, give:
  file:line
  what it is
  why it matters (user impact, not just rule violation)
  the specific fix
  severity: BLOCKER (accessibility failure or broken state) /
            HIGH (system violation users will notice) /
            MEDIUM (inconsistency) /
            LOW (polish)

ALSO REPORT
DESIGN.md GAPS   - values the code needed that DESIGN.md does not specify. These are the most
                   valuable findings: fix them in DESIGN.md, not in the code.
FALSE POSITIVES  - things that look like violations but are justified; say why
NOT CHECKED      - what you could not verify, and why
```

---

## Notes

- The **DESIGN.md GAPS** section is the highest-value output. A code violation is one defect; a
  specification gap will be re-violated by every future implementer.
- Ask for fixes as a separate follow-up, one severity band at a time. A single "fix everything"
  pass tends to produce a large unreviewable diff.
- Findings with computed contrast ratios are actionable; "contrast looks low" is not. The prompt
  asks for the ratio and the pair.
