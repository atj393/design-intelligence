# Prompt 11 — Verify responsive behaviour

---

```
Verify the responsive behaviour of <PATHS / ROUTES>.

Test at these widths: 375, 480, 768, 1024, 1280, 1440.
Also test 375px at 200% zoom, and 1280px with a 320px-wide window.

For each element in scope, state which behaviour is IMPLEMENTED and whether it is CORRECT:
resize | reflow | collapse | stack | scroll | drawer | transform | defer | omit
An element with no defined behaviour at a breakpoint is a finding.

CHECK, at every width:

Layout
- Does the page scroll horizontally? (It must not. Bounded containers may scroll internally.)
- Does any content overflow its container or get clipped?
- Is page padding at least 16px on mobile?
- Does text touch or approach the viewport edge?
- Does prose exceed its documented measure at wide widths?
- Do grids reflow at sensible points, or do items become too narrow to read?

Navigation
- Does it collapse to a drawer or bottom nav below 768px?
- Is the primary action still reachable when nav is collapsed?
- Are destinations duplicated across two systems at any width?
- Is the current location still identifiable in a collapsed state?

Tables
- Does a wide table SHRINK (wrong), scroll with a pinned identifying column (right), or
  transform to cards (right)?
- If scrolling: is the scroll container bounded, and is the pinned column actually pinned?
- If transforming: are the key fields present, and is the detail reachable?
- Are horizontal scroll affordances visible, so users know there is more?

Controls
- Are all touch targets >=44x44px below 1024px?
- Is there >=8px between adjacent targets?
- Is any interaction hover-only? (Every hover affordance needs a tap equivalent.)
- Do adjacent controls still align at every width?
- Do form fields reach at least 16px font size on mobile? (Below that, iOS zooms on focus.)

Sticky elements
- Total sticky chrome height as a percentage of viewport at 768px and at 375px.
  Over ~20% is a finding.
- Does sticky chrome obscure content when the on-screen keyboard opens?
- Does a sticky footer or bar cover the last row of content?

Layout stability
- Reload with a slow network. Does content jump?
- Do images have intrinsic dimensions?
- Is space reserved for async content?
- Does font loading shift text?
- Does streaming or polling content shift the layout?

Modals, drawers, sheets
- Do modals fit at 375px, or do they overflow?
- Is a full-screen sheet used on mobile rather than a squeezed dialog?
- Is the close control reachable without scrolling?
- Is focus trapped correctly inside, and returned on close?

Omitted capabilities
- List anything unavailable at narrow widths.
- For each: is the limitation COMMUNICATED in the interface, or silently hidden?
  Silent omission is a finding.

Zoom
- At 200% zoom on desktop: does the layout reflow, or does it break?
- Is all content still reachable?

REPORT
Per finding: route | width | element | expected behaviour | actual behaviour | severity
  BLOCKER - content unreachable, unusable, or clipped
  HIGH    - significantly degraded usability
  MEDIUM  - awkward but usable
  LOW     - cosmetic

PLUS
BEHAVIOUR MAP    - a table of element x breakpoint x behaviour, so gaps are visible
UNDEFINED        - elements with no specified behaviour at some breakpoint
SILENT OMISSIONS - capabilities hidden without explanation
NOT TESTED       - what you could not verify, and why

Do not fix anything in this pass. Report only.
```

---

## Notes

- The **BEHAVIOUR MAP** is the deliverable to keep. It shows which responsive decisions were made
  deliberately versus which were left to whatever the CSS happened to do.
- Testing 1280px in a 320px window catches container-query and layout assumptions that pure
  viewport testing misses.
- "Silent omissions" is a common and invisible failure: the desktop user and the mobile user
  believe they are looking at the same product.
