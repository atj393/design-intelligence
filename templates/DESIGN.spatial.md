---
# Spatial / map / 3D DESIGN.md
# Copy to project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md. Guide: categories/spatial-map-3d.md
#   WARNING: that guide is FULLY SYNTHESIZED. The source corpus contains no spatial interface
#   evidence at all. Treat every specific below as a hypothesis and validate with real users.

version: 1
name: [[SET: product-name]]-design-system
category: spatial
density: compact
mode: [[CHOOSE: light | dark | both]]
description: >
  [[SET: What users analyse spatially, what decisions they make from it, and what a wrong
  reading costs. The governing constraint here is that every pixel of chrome hides data the
  user came to see.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]", info: "[[SET]]" }
  # Layer palette — 6-8 hues, greyscale-distinguishable, no collision with status hues,
  # assigned deterministically per layer key so a colour never moves when a layer is toggled.
  layers: [ "[[SET]]", "[[SET]]", "[[SET]]", "[[SET]]", "[[SET]]", "[[SET]]" ]
  # Sequential and diverging ramps for magnitude and deviation
  sequential: [ "[[SET: lightest]]", "[[SET]]", "[[SET]]", "[[SET]]", "[[SET: darkest]]" ]
  diverging: { low: "[[SET]]", mid: "[[SET: meaningful midpoint]]", high: "[[SET]]" }
  confidence: { high: "[[SET]]", medium: "[[SET]]", low: "[[SET: e.g. hatched or reduced opacity]]" }

semantic:
  light:
    surface-panel: "#ffffff"              # OPAQUE. Translucency over imagery is unreadable.
    surface-panel-header: "{primitives.neutral.50}"
    surface-control: "#ffffff"
    surface-canvas-fallback: "{primitives.neutral.100}"   # before tiles load
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    action-primary: "{primitives.accent.600}"
    selection-outline: "[[SET: high-contrast against any basemap]]"
    selection-fill: "[[SET: translucent tint]]"
    label-halo: "#ffffff"                 # makes map labels legible over any imagery
    focus-ring: "{primitives.accent.500}"
  dark:
    surface-panel: "{primitives.neutral.900}"
    surface-panel-header: "{primitives.neutral.800}"
    surface-control: "{primitives.neutral.900}"
    surface-canvas-fallback: "{primitives.neutral.950}"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    border-subtle: "rgba(255,255,255,0.10)"
    border-default: "rgba(255,255,255,0.16)"
    action-primary: "{primitives.accent.500}"
    selection-outline: "[[SET]]"
    selection-fill: "[[SET]]"
    label-halo: "{primitives.neutral.950}"
    focus-ring: "{primitives.accent.400}"

basemaps:
  # A muted or greyscale basemap is the single highest-value feature for data legibility.
  - { id: "[[SET: street]]", label: "[[SET]]", muted-variant: "[[SET]]" }
  - { id: "[[SET: satellite]]", label: "[[SET]]", muted-variant: "[[SET: required]]" }
  - { id: "[[SET: terrain]]", label: "[[SET]]", muted-variant: "[[SET]]" }
  default: "[[SET]]"

typography:
  families: { body: "[[SET]]", mono: "[[SET: for coordinates, measurements, IDs]]" }
  substitutes: { body: "[[SET: if proprietary]]" }
  scale:
    # Very low ceiling. Chrome must not compete with the canvas.
    heading-1: { size: 20px, weight: 600, lineHeight: 1.25, tracking: -0.2px }
    heading-2: { size: 16px, weight: 600, lineHeight: 1.35, tracking: 0 }
    heading-3: { size: 14px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:      { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }
    body-sm:   { size: 13px, weight: 400, lineHeight: 1.40, tracking: 0 }
    caption:   { size: 12px, weight: 400, lineHeight: 1.35, tracking: 0.1px }
    overline:  { size: 11px, weight: 600, lineHeight: 1.30, tracking: 0.6px, transform: uppercase }
    label:     { size: 13px, weight: 500, lineHeight: 1.20, tracking: 0 }
    measurement:{ size: 14px, weight: 500, lineHeight: 1.30, tracking: 0, family: mono, features: "tabular-nums" }
    coordinate: { size: 12px, weight: 400, lineHeight: 1.30, tracking: 0, family: mono }
    map-label: { size: 12px, weight: 500, halo: "2px label-halo" }
    attribution:{ size: 11px, weight: 400, lineHeight: 1.20, tracking: 0 }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px }
  panel-padding: 16px
  control-gap: 8px
  edge-inset: 16px          # distance of floating controls from viewport edges

radius: { none: 0, xs: 3px, sm: 4px, md: 6px, lg: 8px, full: 9999px }

layout:
  top-bar: 48px
  layer-panel: 300px
  inspector: 380px
  tool-rail: 48px
  legend-max-width: 240px
  zoom-control: 40px
  # HARD BUDGET: total chrome occlusion <= 30% of viewport with all panels open.
  occlusion-budget: "30%"
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation:
  0: "none"
  1: "1px solid {semantic.border-subtle}"
  2: "0 2px 8px rgba(0,0,0,0.12)"      # floating panels need to separate from the canvas
  3: "0 4px 16px rgba(0,0,0,0.16)"
  strategy: "elevated panels over canvas; borders inside panels"

motion:
  fast: 150ms
  base: 200ms
  camera: 400ms          # 2D<->3D transition. The ONE place animation genuinely helps here.
  reduced-motion: "instant camera switch; mode indicator retained"

components:
  top-bar:        { height: 48px, surface: surface-panel, floating: true, elevation: 2 }
  layer-panel:    { width: 300px, padding: 16px, surface: surface-panel, opaque: true, collapsible: true, resizable: true, state-persisted: true }
  layer-row:      { height: 36px, includes: "visibility toggle, name, opacity slider, drag handle, count" }
  inspector:      { width: 380px, padding: 16px, surface: surface-panel, opaque: true, pans-map-on-open: true }
  tool-rail:      { width: 48px, button: 40px, active-state: "unmistakable + cursor change" }
  legend:         { max-width: 240px, padding: 12px, collapsible: true, required-when-colour-encodes-data: true }
  zoom-control:   { size: 40px, stacked: true, includes: "in, out, recentre, compass" }
  scale-bar:      { type: caption, always-visible: true }
  attribution:    { type: attribution, always-visible: true, never-behind-toggle: true }
  basemap-switcher:{ thumbnail: 56px, collapsed-to: "single swatch" }
  measurement-readout: { type: measurement, live-while-drawing: true, unit-toggle: true }
  disambiguation-list: { max-height: 240px, shown-when: "click hits overlapping features" }
  confidence-badge:{ height: 20px, padding: "2px 8px", radius: full, type: caption }
  data-quality-note:{ type: caption, shows: "currency, resolution, derived-vs-measured" }
  feature-list:   { note: "the accessible alternative to the map — a real product surface, not a fallback" }
---

# [[SET: Product name]] — Spatial Design System

## 1. Product context

- **What users analyse:** [[SET]]
- **Decisions made from it:** [[SET]]
- **Cost of a wrong reading:** [[SET]]
- **Layers:** [[SET: list, with approximate feature counts]]
- **Drawing / measurement tools:** [[SET: which]]
- **2D only, or 2D + 3D:** [[SET]]
- **Map library:** [[SET]]
- **Tile provider and its attribution terms:** [[SET]]
- **Is any information available only on the map?** [[SET]] — if yes, §11 is mandatory scope

## 2. Experience principles

1. **The canvas is the content.** Chrome must justify every pixel it occludes.
2. **Never let the user act on data they cannot see.** Feature limits and coverage gaps are stated.
3. **[[SET: your third, and what it rules out]]**

## 3. Chrome budget

| Element | Size | Position | Behaviour |
|---|---|---|---|
| Top bar | 48px | Floating | Always visible |
| Layer panel | 300px | Left | Collapsible, resizable, state persisted |
| Tool rail | 48px | Left, below panel | Always visible |
| Inspector | 380px | Right | On selection; **pans the map so the selection stays visible** |
| Legend | ≤240px | Bottom-left | Collapsible; required when colour encodes data |
| Zoom / compass | 40px | Right | Always visible |
| Scale bar | auto | Bottom-right | Always visible |
| Attribution | auto | Bottom | **Always visible — a licence requirement** |

**Total occlusion ≤ `{layout.occlusion-budget}` with all panels open.** Cluster controls at edges
and corners; **never cover the canvas centre.**

## 4. Panels

- **Opaque, or ≥90% opaque.** Translucent panels over satellite imagery are unreadable.
- Every panel collapses to a labelled icon.
- The map stays pannable and zoomable with panels open.
- **When a panel would cover the selected feature, pan the map.** Selecting a feature and having
  the inspector hide it is this category's most common defect.
- Panel open state and width persisted per user.

## 5. Layers

`layer-row` provides: visibility toggle, name, **opacity slider** (essential for comparing
overlays), drag reorder, feature count. Groups collapsible. Per-layer loading state — **one slow
layer must not block the others.** Reset to default configuration.

**When a layer renders nothing, state which reason applies:**

| Reason | Message |
|---|---|
| Outside zoom range | [[SET: "Visible from zoom 12" ]] |
| No data in this extent | [[SET]] |
| Load failure | [[SET: with retry]] |
| Permission | [[SET]] |
| Hidden by ordering | [[SET]] |

A silent no-op teaches users the tool is broken.

## 6. Selection

- Hover highlights with a minimal tooltip; click selects and opens the inspector.
- Selection shown by `selection-outline` **and** `selection-fill` — not colour alone.
- `Esc` deselects; selection survives pan and zoom.
- **Overlapping features → `disambiguation-list`.** Never silently select the topmost; the user
  believes they inspected one thing and inspected another.
- Inspector: identity, key attributes, geometry summary, actions, related records, zoom-to-feature.

## 7. Drawing and measurement

[[If not applicable, state that and delete this section.]]

- Active tool unmistakable: rail state **and** cursor change.
- **Per-vertex undo.** Undoing an entire shape for one misplaced point is unacceptable.
- `Esc` cancels in-progress geometry without destroying prior work; `Backspace` removes the last
  vertex; double-click or `Enter` finishes.
- **`measurement-readout` live while drawing**, with a unit toggle: [[SET: metric / imperial]].
  **Never assume units** — that causes real errors.
- Snapping with a visible indicator and a disable modifier.
- Warn on self-intersecting geometry rather than accepting and failing later.
- **Numeric coordinate entry** as a keyboard alternative to clicking.

## 8. 2D / 3D

[[If 2D only, state that and delete this section.]]

- Mode indicator always visible.
- **Animate the transition at `{motion.camera}`.** This is the one place animation genuinely helps —
  it preserves spatial orientation. An instant cut disorients.
- Preserve selection, layers, and extent across the transition.
- Compass resets north on click.
- Tools unavailable in 3D: [[SET: list, with the reason shown]]
- Performance: offer a quality setting rather than failing.
- Under reduced motion: instant switch, mode indicator retained.

## 9. Data quality

`data-quality-note` and `confidence-badge` communicate:

- **Currency** — when captured or last updated
- **Resolution** — imagery or model resolution where it affects conclusions
- **Confidence** — with an explanation of what the levels mean
- **Derived vs. measured** — **visually distinguished and labelled.** In roof, site, or solar
  analysis this difference has financial consequences for the user
- **Coverage gaps** — distinct from zero values
- **Source** — per layer, not only globally
- **Uncertainty** — ranges, error bars, or hatching; never a single confident number

## 10. Loading, limits, comparison

- Progressive tiles: show lower-resolution rather than blank space.
- Failed tiles indicated in place with retry.
- **Feature limits stated explicitly:** [[SET: "Showing 5,000 of 42,000 features" ]]. Silently
  dropping features means users draw conclusions from partial data.
- Long computations: progress, elapsed time, **cancel**.
- Cached/offline extent shown with its age.
- Comparison views (if applicable): [[CHOOSE: swipe curtain | synced side-by-side | opacity blend |
  time slider | computed difference layer]] — both sides labelled; extent locked when synced.

## 11. Accessibility commitments

The hardest category. The first item is the one that matters most.

- [ ] **Any information available only on the map also exists as `feature-list` or a table.** A
      map-only interface is inaccessible by construction. This is a product surface, not a fallback.
- [ ] Keyboard pan (arrows) and zoom (`+`/`−`), documented in a help surface
- [ ] Tab through features in the current extent, or a searchable list as the entry point
- [ ] Selected feature identity and key values announced
- [ ] Visible focus on canvas features, not just chrome
- [ ] Legend colour scales described in text
- [ ] Map labels have an accessible equivalent where canvas-rendered
- [ ] Drawing tools have numeric coordinate entry
- [ ] Screen-reader summary of the current view: [[SET: e.g. "42 sites shown, 8 flagged" ]]
- [ ] Colour never the only channel — pattern or texture added
- [ ] Reduced motion: instant mode switch, indicator retained
- [ ] Chrome usable at 200% zoom
- [ ] Contrast ≥4.5:1 panel text, ≥3:1 controls, both modes and over every basemap

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Canvas | Full viewport | Full | Full |
| Layer panel | Bottom sheet | Overlay drawer | Docked 300px |
| Inspector | Bottom sheet, drag to expand | Overlay | Docked 380px |
| Tools | Bottom row, essential only | Rail | Rail |
| Drawing | [[SET: point + simple line only]] | Most | All |
| Measurement | View only | Basic | Full |
| Legend | Icon-collapsed | Collapsible | Visible |
| 3D | [[SET: often unavailable]] | Available | Full |
| Comparison views | Unavailable | Limited | Full |

**Mobile is for consumption, not creation.** Viewing, searching, geolocating, inspecting, and
sharing are achievable. Precise polygon drawing at 375px is not.

**Capabilities unavailable on mobile:** [[SET: list]] — **stated in the interface.** "Drawing tools
require a larger screen" is respectful; a hidden control is not.

Mobile specifics: bottom sheets not side panels · feature hit areas padded to ~44px · notch and
home-indicator safe areas respected · geolocation control provided · pinch-zoom must not conflict
with page zoom.

## 13. Do

- Keep occlusion within budget
- Keep panels opaque
- Pan the map so selections stay visible
- Persist panel state and width
- Show attribution always
- Provide a muted basemap option
- Halo map labels and markers
- Distinguish "no data" from zero, and derived from measured
- State feature limits
- Give per-vertex undo
- Show live measurements with a unit toggle
- Animate 2D/3D transitions
- Disambiguate overlapping features
- Ship the non-map alternative

## 14. Do not

- Do not cover the canvas centre
- Do not use translucent panels over imagery
- Do not let the inspector hide its own subject
- Do not hide attribution
- Do not silently drop features
- Do not silently select the topmost overlapping feature
- Do not assume units
- Do not accept invalid geometry silently
- Do not destroy a whole drawing on undo
- Do not cut instantly between 2D and 3D
- Do not present derived values as measured
- Do not encode map data by colour alone
- Do not claim mobile parity for drawing or comparison
- Do not ship a map-only interface

## 15. Implementation notes

- **Map library and version:** [[SET]]
- **Tile provider and attribution string:** [[SET: exact required text]]
- **Coordinate system / projection:** [[SET]]
- **Feature render cap and how truncation is surfaced:** [[SET]]
- **Layer opacity implementation:** [[SET]]
- **3D engine:** [[SET]]
- **Accessible feature-list source:** [[SET: same data source as the map layer]]
- **Existing components to reuse:** [[SET]]

## 16. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/spatial-map-3d.md` — **note its evidence banner: it
is fully synthesized** — then this file. This file wins.

**Before generating:** inspect the map library's control primitives, existing panel/inspector/
toolbar components, tokens for elevated surfaces, and the tile provider's attribution requirements.
Report findings.

**While generating:** respect the occlusion budget. Opaque panels. Pan on inspector open. Per-layer
loading and explicit empty reasons. Disambiguation for overlaps. Per-vertex undo. Unit toggle.
Stated feature limits. Build the `feature-list` alternative as part of the work, not afterwards.

**Then report:** measured occlusion with all panels open · how data currency, confidence, and
derived-vs-measured are communicated · the non-map accessible alternative you built · assumptions,
deviations, invented values, unresolved decisions · reused vs. created components · capabilities
unavailable on mobile and how that is communicated.
