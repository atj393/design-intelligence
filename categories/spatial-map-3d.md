# Spatial, Map-Based and 3D Products

Interfaces where a geographic or spatial canvas is the primary surface: mapping, GIS, roof and
site analysis, route planning, asset tracking, simulation, 3D model inspection, BIM, planning
tools.

> **Evidence strength: none / fully synthesized.**
> The source corpus contains **nothing** on this category. No map controls, no layers, no
> legends, no drawing tools, no 2D/3D transitions. Grep confirms it: the sources that mention
> "map" do so in unrelated senses. Everything below is general interface reasoning from
> established spatial-interface practice. It is the least evidence-backed guide in this layer.
> **Validate every recommendation with real users before committing.**
>
> What the corpus *does* legitimately contribute is the token and elevation model: how to build
> a floating-panel hierarchy over a busy background (see §Source inspiration).

---

## 1. The governing constraint

**The canvas is the content. Every pixel of chrome hides data the user came to see.**

This inverts normal layout thinking. In most categories, chrome frames content. Here, chrome
*occludes* content, and the design problem is delivering full capability while covering as
little canvas as possible.

Consequences:

- Panels float over the canvas rather than displacing it — but must be collapsible.
- Controls cluster at edges and corners, not through the middle.
- The map must remain interactive while panels are open.
- Panel state persists, because a user who re-opens the layer panel forty times a session should
  not re-position it each time.
- Never cover the canvas centre. That is where the user is looking.

## 2. Layout

```
┌─────────────────────────────────────────────────────┐
│ [logo] [search──────────]        [account] [help]   │ ← 48px floating bar
│ ┌──────────┐                            ┌─────┐    │
│ │ layers   │                            │ +   │    │ ← zoom, top-right
│ │ panel    │        MAP CANVAS          │ −   │    │
│ │ 280px    │                            │ ⌖   │    │
│ │ (toggle) │                            └─────┘    │
│ └──────────┘                                       │
│ ┌────────┐                        ┌──────────────┐ │
│ │ tools  │                        │ inspector    │ │
│ │ 48px   │                        │ 360px        │ │
│ └────────┘                        │ (contextual) │ │
│  [legend]                         └──────────────┘ │
│  © attribution                          [scale]    │
└─────────────────────────────────────────────────────┘
```

| Element | Size | Position | Behaviour |
|---|---|---|---|
| Top bar | 48px | Floating, translucent | Always visible |
| Layer panel | 280–320px | Left | Collapsible; state persists |
| Tool palette | 48px rail or 48px row | Left below panel, or bottom-centre | Always visible |
| Inspector | 360–400px | Right | Appears on selection |
| Legend | Auto, max 240px | Bottom-left | Collapsible; required when colour encodes data |
| Zoom / orientation | 40px buttons | Right, vertically stacked | Always visible |
| Scale bar | Auto | Bottom-right | Always visible on geographic maps |
| Attribution | Auto | Bottom | **Always visible — usually a licence requirement** |
| Basemap switcher | 64px thumbnail | Bottom-right | Collapsed to a single swatch |

**Total chrome budget: keep occlusion under ~30% of the viewport with all panels open.** Beyond
that the user is working through a keyhole.

**Attribution is non-negotiable.** Map tile providers require visible attribution as a licence
term. It is a legal requirement, not a design choice, and it must not be hidden behind a toggle.

## 3. Panel behaviour

| Property | Requirement |
|---|---|
| Surface | Elevated, with a scrim or backdrop treatment so text stays legible over any basemap |
| Opacity | **The requirement is contrast, not opacity.** See the note below |
| Collapse | Every panel collapsible to a labelled icon |
| Persistence | Open/closed state and width remembered per user |
| Resize | Layer and inspector panels resizable |
| Canvas interaction | Map remains pannable and zoomable with panels open |
| Recentre on open | When a panel would cover the selected feature, pan the map — do not leave the selection hidden |

**That last point is the difference between a usable and an infuriating spatial tool.** Selecting
a feature and having the inspector cover it is the category's most common defect. Pan the canvas
so the selection stays visible beside the panel.

> **Restated after adversarial review** (see
> [research/WEAK-GUIDE-REVIEW.md](../research/WEAK-GUIDE-REVIEW.md) A-04). An earlier draft
> required panels to be "opaque or ≥90% opaque". That confused the mechanism with the goal.
> **The actual requirement is that panel text meets its contrast floor over the worst-case
> basemap** — and a translucent panel with a sufficient blur plus a darkening or lightening
> layer can meet it. Several capable map tools do exactly that.
>
> So the rule is: **verify contrast against the worst case, not against the average.** For a
> satellite basemap that means the brightest region the panel can overlap. If you cannot
> guarantee it — because the user can switch basemaps or load arbitrary imagery — fall back to an
> opaque panel, because guaranteeing it is the whole point.
>
> The occlusion budget below (~30%) is a **synthesized heuristic, not a measured threshold.**
> It is a starting point for keeping the canvas usable; treat it as a prompt to measure your own
> occlusion, not as a number with evidence behind it.

## 4. Layers

| Element | Requirement |
|---|---|
| Visibility toggle | Per layer, immediate |
| Opacity | Per layer, slider — essential for comparing overlays |
| Ordering | Drag to reorder, with clear z-order indication |
| Grouping | Collapsible groups for many layers |
| Legend link | Each layer's symbology visible in or from the panel |
| Loading state | Per layer — one slow layer must not block the others |
| Unavailable layer | Say why: out of zoom range, no data for this area, permission, failed |
| Zoom dependency | Show when a layer only renders at certain zooms, and at which |
| Count | Show feature counts where meaningful |
| Reset | Return to the default layer configuration |

**"Nothing appeared" is the most common layer confusion**, and it has several distinct causes —
outside zoom range, no data in this extent, load failure, or wrong ordering. The panel must
distinguish them. A silent no-op teaches users the tool is broken.

## 5. Selection and inspection

| Interaction | Behaviour |
|---|---|
| Hover | Highlight the feature; show a minimal tooltip (name or key value) |
| Click | Select; open inspector; keep the feature visible |
| Multi-select | Modifier-click, or box/lasso select |
| Selection indicator | Outline **and** fill change — not colour alone |
| Deselect | `Esc`, click empty canvas, and an explicit close control |
| Ambiguous click | Overlapping features: show a disambiguation list, do not guess |
| Inspector content | Identity, key attributes, geometry summary, actions, related records |
| Zoom to feature | Available from the inspector |
| Selection persistence | Survives pan and zoom |

**Overlapping features need a disambiguation list.** Silently selecting the topmost feature when
three overlap is a correctness problem — the user thinks they inspected one thing and inspected
another.

## 6. Drawing and measurement

| Tool | Requirements |
|---|---|
| Point | Click to place; drag to move; snap where useful |
| Line / path | Click per vertex, double-click or `Enter` to finish, `Esc` to cancel, `Backspace` to remove the last vertex |
| Polygon | As above, with auto-close and self-intersection warning |
| Rectangle / circle | Drag; show dimensions live while dragging |
| Freehand | Drag; simplify on release |
| Measure distance | Live readout, segment and cumulative totals, unit toggle |
| Measure area | Live readout with unit toggle |
| Edit | Select and drag vertices; add and delete vertices |
| Snapping | To existing geometry, with a visible snap indicator and a disable modifier |
| Undo | **Per vertex.** Undoing an entire shape because of one misplaced point is unacceptable |
| Precision | Allow numeric coordinate entry as an alternative to clicking |

**Requirements that apply to all drawing tools:**

- Active tool must be unmistakable — the palette shows it, and the cursor changes.
- Show units and let users switch (metric / imperial). Assuming units causes real errors.
- Show live measurements while drawing, not only on completion.
- Warn on invalid geometry (self-intersecting polygons) rather than accepting and failing later.
- `Esc` always cancels the in-progress geometry without destroying prior work.

## 7. 2D / 3D transitions

| Requirement | Detail |
|---|---|
| Mode indicator | Current mode always visible |
| Transition | Animated, 300–500ms — **this is one place animation genuinely helps**, because it preserves the user's spatial orientation |
| State preservation | Selection, layers, and extent survive the transition |
| Camera reset | Return to a known orientation — north-up, top-down |
| Pitch / bearing | Visible controls plus a compass; clicking the compass resets north |
| Capability differences | State which tools are unavailable in 3D and why |
| Performance | Degrade gracefully; offer a quality setting rather than failing |
| Lighting / shadows | Where they encode information (solar analysis), show time and date controls |

Animation is usually a cost. Here it is a benefit: an instant cut from top-down to oblique
disorients the user, while a 400ms camera move preserves the mental model. This is the exception
that proves the rule — motion is justified when it communicates spatial change.

## 8. Data quality and confidence

Critical for analysis products and routinely omitted.

| Requirement | Detail |
|---|---|
| Data currency | When was this captured or last updated? Show it |
| Resolution | Imagery or model resolution, where it affects conclusions |
| Confidence | Where the system estimates, show the confidence and what it means |
| Derived vs. measured | Distinguish computed values from observed ones |
| Coverage gaps | Show where data does not exist — distinct from where a value is zero |
| Source | Attribute per layer, not only globally |
| Uncertainty display | Ranges, error bars, or hatching — not a single confident number |

**A derived measurement presented identically to a measured one invites misplaced confidence.**
In roof, site, or solar analysis, that difference has financial consequences for the user.
Distinguish them visually and label them.

## 9. Comparison views

| Pattern | Use |
|---|---|
| Swipe / curtain | Two layers, same extent, draggable divider — best for before/after imagery |
| Side-by-side, synced | Two maps, linked pan and zoom |
| Opacity blend | Slider between two layers |
| Time slider | Same layer across time, with playback |
| Difference layer | Computed change, with a diverging colour scale and a legend |

Requirements: both sides labelled unambiguously; extent and zoom locked together when synced;
timestamps shown for temporal comparison.

## 10. Loading and performance states

Spatial data is heavy. These states are the normal case, not the exception.

| State | Treatment |
|---|---|
| Tiles loading | Progressive; show lower-resolution tiles rather than blank space |
| Vector data loading | Per-layer indicator in the layer panel |
| Slow layer | Named in the panel; does not block others |
| Failed tiles | Visible indication in the affected area, plus retry |
| Too much data | Suggest zooming in or filtering — do not silently drop features |
| Feature limit reached | Say so explicitly: "Showing 5,000 of 42,000 features" |
| Computing | Progress with elapsed time and cancel for long analyses |
| Offline / cached | Show which extent is cached and how old it is |

**Silently dropping features is a correctness failure.** If the renderer caps at 5,000 features,
the user must know they are not seeing everything — otherwise they draw conclusions from partial
data.

## 11. Colour on a map

Harder than in any other category, because the basemap is uncontrolled.

| Requirement | Detail |
|---|---|
| Contrast against basemap | Overlay colours must work over satellite, street, and terrain basemaps |
| Basemap dimming | Offer a muted or greyscale basemap so data overlays read clearly |
| Sequential scales | Single hue, light-to-dark, for magnitude |
| Diverging scales | Two hues with a meaningful, stated midpoint |
| Categorical | 6–8 hues maximum; group beyond that |
| Legend | **Required** whenever colour encodes data |
| Colour-blind safe | Verify against common deficiencies; add pattern or texture as a second channel |
| Halos / outlines | White or dark outlines on markers and labels so they survive any background |
| Label collision | Automatic label placement with collision avoidance; hide rather than overlap |

**A muted basemap option is the single highest-value feature for data legibility on a map.** Full
satellite imagery beneath a choropleth makes both unreadable.

**Outlines on labels and markers are essential**, not decorative — they are what makes text
legible over unpredictable imagery.

## 12. Responsive behaviour

**This category cannot deliver full parity on small screens, and should say so.**

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Canvas | Full viewport | Full | Full |
| Top bar | 48px, search collapses to icon | 48px | 48px |
| Layer panel | Bottom sheet | Overlay drawer | Docked 280px |
| Inspector | Bottom sheet, drag to expand | Overlay | Docked 360px |
| Tools | Bottom row, essential tools only | Rail | Rail |
| Drawing | Point and simple line only | Most tools | All tools |
| Measurement | View only | Basic | Full |
| Legend | Collapsed to an icon | Collapsible | Visible |
| 3D | Often unavailable — state it | Available | Full |
| Comparison views | Unavailable — state it | Limited | Full |

**Design mobile for consumption, not creation.** Viewing, searching, locating yourself,
inspecting a feature, and sharing a view are achievable. Precise polygon drawing on a 375px touch
screen is not, and pretending otherwise produces a tool that fails at its job.

**State limitations in the interface.** "Drawing tools require a larger screen" is respectful.
A hidden control the user cannot find is not.

Mobile-specific requirements:

- Bottom sheets rather than side panels — reachability.
- Larger hit targets on the canvas: touch selection needs ~44px, so feature hit areas must be
  padded beyond their visual size.
- Account for the notch and home indicator; controls must not sit under system gestures.
- Provide a geolocation control — on mobile, "where am I" is a primary task.
- Pinch-zoom must not conflict with page zoom.

## 13. Accessibility

The hardest category for accessibility, and the reason a non-visual alternative is mandatory.

| Requirement | Implementation |
|---|---|
| **Non-map alternative** | Any information available *only* on the map must also be available as a list or table. This is the central requirement |
| Keyboard pan / zoom | Arrow keys pan, `+`/`−` zoom, documented in a help surface |
| Keyboard feature selection | `Tab` through features in the current extent, or a searchable list as the entry point |
| Selection announcement | Announce the selected feature's identity and key values |
| Focus visibility | Visible focus on canvas features, not just on chrome |
| Legend as text | Colour scales described in text as well as swatches |
| Labels | Real text where possible; canvas-rendered labels need an accessible equivalent |
| Drawing tools | Numeric coordinate entry as a keyboard alternative to clicking |
| Reduced motion | Instant 2D/3D switch when reduced motion is set — but retain the mode indicator |
| Zoom to 200% | Chrome must remain usable; the canvas may scale independently |
| Colour independence | Pattern, texture, or label in addition to colour |
| Screen-reader summary | A text summary of what is currently displayed: "42 sites shown in the current view, 8 flagged" |

**A map-only interface is inaccessible by construction.** The feature list, the data table, and
the text summary are not fallbacks — they are part of the product, and they are also genuinely
useful to sighted users who want exact values.

## 14. Do

- Keep total chrome occlusion under ~30% of the viewport
- Make panels opaque enough to read over any basemap
- Pan the canvas so a selection stays visible beside the inspector
- Persist panel open state and width per user
- Show attribution at all times
- Provide a muted or greyscale basemap option
- Outline labels and markers so they survive any background
- Distinguish "no data" from zero, and derived values from measured ones
- Show data currency, resolution, and confidence
- Say when a feature limit truncates what is displayed
- Give per-vertex undo in drawing tools
- Show live measurements while drawing, with a unit toggle
- Animate 2D/3D transitions to preserve orientation
- Show a disambiguation list for overlapping features
- Provide a non-map alternative for all map-only information

## 15. Do not

- Do not cover the canvas centre with chrome
- Do not use translucent panels over imagery
- Do not let the inspector hide the feature it describes
- Do not hide attribution
- Do not silently drop features beyond a render limit
- Do not silently select the topmost of overlapping features
- Do not assume units — state and allow switching
- Do not accept invalid geometry without warning
- Do not destroy a whole drawing on undo
- Do not cut instantly between 2D and 3D
- Do not present derived values identically to measured ones
- Do not encode data by colour alone on a map
- Do not claim mobile parity for drawing or comparison
- Do not ship a map-only interface with no list or table alternative
- Do not let one slow layer block all others

## 16. Source inspiration

The corpus contributes **nothing** about spatial interfaces. What follows are transferable
structural lessons only, and the section is deliberately short because inventing citations here
would be worse than admitting the gap.

| Source | Transferable lesson |
|---|---|
| `design-md/linear.app/DESIGN.md` § *Elevation & Depth* | A four-step surface ladder with hairline borders and no shadow. Directly transferable to building a floating-panel hierarchy that reads clearly over a busy canvas |
| `design-md/spotify/DESIGN.md` § *Color Palette & Roles* | A charcoal surface ladder where *content supplies the colour* and the chrome recedes. Exactly the relationship a map interface needs between panels and canvas |
| `design-md/apple/DESIGN.md` § *Elevation & Depth* | Shadowless chrome with one signature shadow reserved for content resting on a surface — a disciplined model for when elevation is worth spending |
| `design-md/nvidia/DESIGN.md` § *Shapes*, § *Layout* | 2px radius and hairline rules supporting dense technical content — appropriate geometry for a control-dense workspace |
| `design-md/binance/DESIGN.md` § *Colors* | Directional and semantic colour in a data-dense context, with a documented light theme for functional surfaces |
| `design-md/hashicorp/DESIGN.md` § *Colors* | Accents mapped to structural identity rather than decoration — the discipline a layer palette requires |

**Everything else in this guide is synthesized.** It is coherent and it follows established
spatial-interface practice, but it is reasoning rather than evidence. Treat it as a starting
hypothesis and test it.

## 17. Common mistakes

| Mistake | Consequence | Correction |
|---|---|---|
| Inspector covering the selection | User cannot see what they selected | Pan the canvas on open |
| Translucent panels over imagery | Unreadable text | Opaque panels |
| Chrome occluding too much canvas | Working through a keyhole | ≤30% budget, collapsible panels |
| Hidden attribution | Licence violation | Always visible |
| Silent feature truncation | Conclusions from partial data | State the limit |
| Topmost-wins on overlap | Wrong feature inspected | Disambiguation list |
| Whole-shape undo | Lost work on a single mis-click | Per-vertex undo |
| Assumed units | Real measurement errors | State and toggle |
| Instant 2D/3D cut | Disorientation | 300–500ms transition |
| Derived shown as measured | Misplaced confidence in financial decisions | Distinguish and label |
| No muted basemap | Data overlays illegible | Provide one |
| Map-only information | Inaccessible by construction | List/table alternative |
| Claimed mobile parity | Unusable cramped tools | State the limits honestly |

## 18. Template

[templates/DESIGN.spatial.md](../templates/DESIGN.spatial.md)
