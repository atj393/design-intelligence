# Prompt 12 — Verify accessibility

---

```
Verify the accessibility of <PATHS / ROUTES>.

Target: WCAG 2.2 Level AA minimum, plus the commitments in this project's DESIGN.md.

Report findings only. Do not fix in this pass.

1. CONTRAST — compute actual ratios; do not estimate
For every text and UI element, in BOTH light and dark themes:
- Body text (<24px, or <19px bold): >=4.5:1
- Large text: >=3:1
- UI component boundaries, icons carrying meaning, form borders: >=3:1
- Focus indicators: >=3:1 against the element AND against the adjacent surface
- Placeholder text, disabled text, captions, secondary text — these fail most often
- Text over images or gradients: compute against the LIGHTEST/DARKEST region it can overlap,
  not the average
- Syntax highlighting tokens, if present — comment colours are the usual failure
- Chart series colours against their background
Report: element | foreground | background | computed ratio | required | theme | PASS/FAIL

2. KEYBOARD — complete a full task using only the keyboard
- Is every interactive element reachable by Tab?
- Is the tab order logical and matching visual order?
- Is focus ALWAYS visible? Any `outline: none` without a replacement?
- Any focus traps outside a modal?
- Do modals trap focus correctly, and return it to the trigger on close?
- Esc closes overlays?
- Enter/Space activate buttons; Enter submits forms?
- Custom controls (dropdowns, tabs, comboboxes, sliders): correct arrow-key behaviour?
- Tables: arrow-key cell navigation? Home/End?
- Is there a skip-to-content link, visible on focus?
- Can anything be reached ONLY by hover or drag?

3. COLOUR INDEPENDENCE — set the OS to greyscale and re-check
- Is every status still distinguishable?
- Are chart series still distinguishable?
- Are links still distinguishable from body text?
- Are required fields, errors, and selected states still identifiable?
- Are diff additions/deletions still distinguishable?
- Are colour swatches or option pickers still usable?

4. TOUCH AND POINTER
- Targets >=44x44px on touch viewports
- >=8px between adjacent targets
- Compact density: are hit areas expanded beyond the visual row height?
- Any drag-only interaction with no alternative?

5. FORMS
- Every field has a programmatic label (not placeholder-only)
- Labels visible, not disappearing on input
- Errors associated with their field (aria-describedby or equivalent)
- Errors announced on submit; focus moved to the summary or first error
- Required fields marked programmatically, not by colour or asterisk alone
- Correct `autocomplete` attributes
- Correct `inputmode` / input types for mobile keyboards
- Fieldsets and legends for grouped inputs
- Is input preserved on validation error?
- Is a disabled submit button explained?

6. STRUCTURE
- Exactly one h1 per page
- No skipped heading levels
- Headings describe content; not used purely for size
- Landmarks present: main, nav, header, footer, and labelled if repeated
- Lists marked up as lists
- Tables: th with scope; caption on complex tables; no layout tables

7. IMAGES AND MEDIA
- Meaningful alt text; alt="" on decorative images
- Icon-only buttons have accessible names
- Complex images (charts, diagrams) have a longer description or data alternative
- Video has captions; audio has a transcript
- No autoplay with sound; visible pause controls

8. DYNAMIC CONTENT
- Async changes announced via live regions
- aria-live="polite" for routine updates, not "assertive"
- Streaming content: start and completion announced, NOT every token
- Toasts announced and dismissible; not the sole channel for anything important
- Loading states announced
- Route changes announced; focus managed on navigation

9. MOTION
- prefers-reduced-motion honoured
- With it enabled: does everything still work, and is every state change still communicated?
- Nothing loops except progress indicators
- No content flashing more than 3 times per second

10. ZOOM AND REFLOW
- Usable at 200% zoom
- Text-only zoom to 200% without loss
- No horizontal page scroll at 320px equivalent
- Content not clipped or overlapping when text spacing is increased

11. CATEGORY-SPECIFIC
- Charts: is a data table or text summary available?
- Maps: is map-only information available as a list or table?
- Dense tables: full keyboard navigation?
- Money flows: is there a confirmation or reversal path (WCAG 3.3.4)?
- Timed processes: is there a warning and an extension (WCAG 2.2.1)?

REPORT
Per finding: file:line or route | issue | WCAG criterion | user impact | fix | severity
  BLOCKER - content or function unavailable to a group of users
  HIGH    - significant barrier
  MEDIUM  - friction
  LOW     - improvement

PLUS
PASSED           - what you verified as compliant
NOT TESTABLE     - what needs a real screen reader, real assistive tech, or a human, and why
FALSE POSITIVES  - automated-tool findings that are not real issues, with reasoning
```

---

## Notes

- **Automated tools catch perhaps a third of real issues.** The greyscale test and the
  keyboard-only task in steps 2 and 3 find more than any scanner.
- Ask for computed ratios, not judgments. "Contrast looks low" is not actionable; "#8a8f98 on
  #010102 = 5.9:1, passes" is.
- **NOT TESTABLE** matters. An agent cannot verify screen-reader behaviour without a screen
  reader; a claim that it did is worse than the gap.
