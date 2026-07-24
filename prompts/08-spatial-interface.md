# Prompt 08 — Build a map, spatial, or 3D interface

> The category guide behind this prompt is **fully synthesized** — the source corpus contains no
> spatial interface evidence at all. Treat its specifics as a starting hypothesis and validate
> with real users.

---

```
Build <SURFACE> — a map/spatial interface for <PRODUCT>.

CONTEXT
- What users analyse: <geographic data, roofs, sites, routes, assets, models>
- Primary tasks: <top 3>
- Data layers: <list, and roughly how many features each>
- Drawing or measurement needed: <which tools>
- 2D only, or 2D + 3D: <answer>
- Map provider / rendering library: <name>
- Device: <desktop primary | desktop + mobile consumption>
- Is any information available ONLY on the map? <this determines the accessibility work>

STEP 1 — INSPECT. Report before writing code:
- The project DESIGN.md
- Map library in use and its control primitives
- Existing panel, inspector, and toolbar components
- Existing tokens for elevated surfaces
- Attribution requirements of the tile provider — these are licence terms, not preferences
Report what you found.

STEP 2 — BUILD

Governing constraint: the canvas is the content. Every pixel of chrome hides data the user came
to see. Total occlusion with all panels open: <=30% of the viewport.

Layout:
- Top bar 48px, floating
- Layer panel 280-320px left, collapsible, state persisted per user
- Tool palette 48px rail
- Inspector 360-400px right, appears on selection
- Legend bottom-left, collapsible — REQUIRED whenever colour encodes data
- Zoom/orientation controls 40px, right side
- Scale bar bottom-right on geographic maps
- Attribution ALWAYS visible — never behind a toggle
- Cluster controls at edges and corners. Never cover the canvas centre.

Panels:
- OPAQUE or >=90% opaque. Translucent panels over satellite imagery are unreadable.
- Every panel collapsible to a labelled icon
- Map stays pannable and zoomable with panels open
- When a panel would cover the selected feature, PAN THE MAP so the selection stays visible.
  Selecting a feature and having the inspector hide it is this category's most common defect.

Layers:
- Per-layer visibility, opacity slider, drag reorder, collapsible groups
- Per-layer loading state — one slow layer must not block the others
- When a layer shows nothing, SAY WHY: outside zoom range, no data in this extent, load
  failure, permission, or wrong ordering. A silent no-op teaches users the tool is broken.
- Feature counts where meaningful; reset-to-default control

Selection:
- Hover highlights with a minimal tooltip; click selects and opens the inspector
- Selection indicated by outline AND fill change, not colour alone
- Esc deselects; selection survives pan and zoom
- OVERLAPPING FEATURES: show a disambiguation list. Never silently select the topmost —
  the user thinks they inspected one thing and inspected another.

Drawing and measurement (if applicable):
- Active tool unmistakable: palette state + cursor change
- Per-vertex UNDO. Undoing an entire shape because of one misplaced point is unacceptable.
- Esc cancels the in-progress geometry without destroying prior work; Backspace removes the
  last vertex
- Live measurements WHILE drawing, with a unit toggle (metric/imperial). Never assume units.
- Snapping with a visible indicator and a disable modifier
- Warn on self-intersecting geometry rather than accepting and failing later
- Numeric coordinate entry as a keyboard alternative to clicking

2D/3D (if applicable):
- Mode indicator always visible
- ANIMATE the transition, 300-500ms. This is one of the few places animation genuinely helps —
  it preserves spatial orientation. An instant cut disorients.
- Preserve selection, layers, and extent across the transition
- Compass that resets north on click; state which tools are unavailable in 3D and why
- Instant switch under prefers-reduced-motion, retaining the mode indicator

Data quality — routinely omitted and important:
- Show data currency, resolution, and confidence
- DISTINGUISH derived values from measured ones. In roof, site, or solar analysis this
  difference has financial consequences for the user.
- Show coverage gaps as distinct from zero values
- Per-layer source attribution

Loading and limits:
- Progressive tiles; show lower-resolution rather than blank space
- Failed tiles indicated in place, with retry
- FEATURE LIMITS: if the renderer caps output, say so — "Showing 5,000 of 42,000 features".
  Silently dropping features means users draw conclusions from partial data.
- Long computations: progress, elapsed time, CANCEL

Colour on a map:
- Provide a MUTED or greyscale basemap option — the highest-value feature for data legibility
- Overlay colours must work over satellite, street, and terrain basemaps
- Outlines/halos on labels and markers so text survives unpredictable imagery
- Sequential (single hue) for magnitude; diverging (two hues, stated midpoint) for deviation;
  categorical 6-8 max
- Colour never the only channel — add pattern or texture
- Label collision avoidance: hide rather than overlap

Accessibility — the central requirement:
- Any information available ONLY on the map must ALSO exist as a list or table. A map-only
  interface is inaccessible by construction.
- Keyboard pan (arrows) and zoom (+/-), documented
- Tab through features in the current extent, or provide a searchable list as the entry point
- Announce selected feature identity and key values
- Visible focus on canvas features, not just chrome
- Legend colour scales described in text
- Screen-reader summary of the current view: "42 sites shown, 8 flagged"

Responsive:
- Mobile is for CONSUMPTION, not creation. Viewing, searching, geolocating, inspecting, and
  sharing are achievable. Precise polygon drawing at 375px is not.
- Bottom sheets rather than side panels
- Feature hit areas padded to ~44px for touch
- Respect notch and home-indicator areas
- STATE in the interface what requires a larger screen. Do not hide controls silently.

CONSTRAINTS
- Do not exceed the 30% occlusion budget
- Do not use translucent panels over imagery
- Do not hide attribution
- Reuse existing components

REPORT
OCCLUSION        - measured chrome coverage with all panels open
REUSED / CREATED
DATA QUALITY     - how currency, confidence, and derived-vs-measured are communicated
ACCESSIBILITY    - the non-map alternative you built
ASSUMPTIONS / DEVIATIONS / INVENTED VALUES / UNRESOLVED
MOBILE LIMITS    - what is unavailable and how it is communicated
```
