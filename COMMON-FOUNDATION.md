# Common Design Foundation

A starting design system for a new digital product. Not a style — a set of defaults,
alternatives, and the conditions that decide between them.

**Evidence:** token structure, type scales, spacing, radius, breakpoints, and elevation are
grounded in the 74-source corpus; distributions are in
[research/VALUE-DISTRIBUTIONS.md](research/VALUE-DISTRIBUTIONS.md). Interaction states,
semantic status colours, and the primitive/semantic token model are **synthesized** — the
corpus documents marketing surfaces and rarely specifies states. Synthesized sections are
marked inline.

**How to use:** apply this foundation first, then layer the relevant guide from
[categories/](categories/). The foundation decides *scales and structure*; the category
decides *density, navigation, and component emphasis*. Neither decides your brand.

---

## 1. Reading the recommendations

Every measurement below ships in three variants plus a condition:

- **Default** — use this unless something specific says otherwise.
- **Compact** — for high-frequency, information-dense, expert-user surfaces.
- **Spacious** — for low-frequency, persuasion-led, or reading-led surfaces.

Nothing here is a law. The corpus contains a 0px-radius system and a 40px-radius system,
both excellent, both correct for their product. Ranges are guardrails against arbitrariness,
not against judgment.

---

## 2. Token architecture *(synthesized)*

Two layers. This is the single most consequential structural decision in the document,
because everything downstream depends on it.

**Primitive tokens** — raw values with no meaning attached:

```
color.slate.50 … color.slate.950      space.1 … space.16
color.blue.500                        radius.sm … radius.xl
font.size.16                          shadow.1 … shadow.4
```

**Semantic tokens** — intent, referencing primitives:

```
surface.canvas        → color.slate.50
text.primary          → color.slate.900
border.subtle         → color.slate.200
action.primary        → color.blue.600
status.danger         → color.red.600
focus.ring            → color.blue.500
```

**Components consume semantic tokens only.** A button referencing `action.primary` keeps
working when the brand hue changes, when dark mode is added, and when a theme is introduced.
A button referencing `color.blue.600` has to be found and edited every time — and it will be
missed somewhere.

The corpus supports this indirectly and consistently: 64 files use `{colors.x}` reference
syntax, and the most common token names across the whole corpus are role names, not colour
names — `primary` (64 files), `ink` (64), `on-primary` (63), `canvas` (58), `hairline` (53).
The two-layer model is not stated as a rule by any source; the naming discipline is
everywhere.

**Minimum semantic set.** Anything less produces arbitrary decisions later:

| Group | Tokens |
|---|---|
| Surface | `canvas`, `raised`, `sunken`, `overlay`, `inverse` |
| Text | `primary`, `secondary`, `tertiary`, `disabled`, `on-accent`, `on-inverse`, `link` |
| Border | `subtle`, `default`, `strong`, `focus` |
| Action | `primary`, `primary-hover`, `primary-active`, `primary-disabled`, `secondary`, `secondary-hover`, `ghost-hover`, `destructive`, `destructive-hover` |
| Status | `success`, `success-surface`, `warning`, `warning-surface`, `danger`, `danger-surface`, `info`, `info-surface` |
| Utility | `focus.ring`, `selected`, `selected-surface`, `scrim`, `skeleton` |

Status *surface* variants matter more than they look. A warning needs a background tint for
banners and table rows, and it cannot be the same value as the warning text — that fails
contrast immediately. The corpus documents `info` in only 4 of 74 files, which is why the
full set here is synthesized rather than extracted.

---

## 3. Spacing

**Base unit: 4px, with 8px as the preferred increment.**

The corpus splits 29/28 between declaring 8px and 4px as base, but nearly every
8px-declared system still uses 4px and 12px steps. A 4px grid with 8px habits describes
actual practice.

| Token | Value | Use |
|---|---|---|
| `space.0` | 0 | Reset |
| `space.px` | 1px | Hairlines |
| `space.1` | 4px | Icon-to-label gaps, tight inline spacing |
| `space.2` | 8px | Control interiors, tight stacks |
| `space.3` | 12px | Related-element gaps, compact padding |
| `space.4` | 16px | Default gap; standard padding |
| `space.5` | 20px | Intermediate step |
| `space.6` | 24px | Card padding; component separation |
| `space.8` | 32px | Group separation |
| `space.10` | 40px | Large group separation |
| `space.12` | 48px | Subsection separation |
| `space.16` | 64px | Section separation (compact) |
| `space.20` | 80px | Section separation (default) |
| `space.24` | 96px | Section separation (spacious) |

The core `4 · 8 · 12 · 16 · 24 · 32` sequence appears in 61–73 of 74 files. Above 32px,
ladders diverge by category, which is exactly where your category guide takes over.

### Section rhythm — the value most often transplanted wrongly

| Variant | Value | When |
|---|---|---|
| **Default** | 64–80px | Most products |
| **Compact** | 32–48px | Documentation, dashboards, daily-use tools, editorial density |
| **Spacious** | 96–120px | Marketing pages, brand surfaces, low-frequency visits |

61 of 74 sources use 96px. **Do not read that as a recommendation.** The population is
marketing sites, where a user scrolls once and generosity reads as confidence. In a tool
opened forty times a day, that same 96px is a scroll cost paid forty times. The corpus's own
documentation surfaces — same companies, same brands — drop to 48–64px the moment the
surface's job changes from persuading to explaining.

**Decision rule:** how often will one person see this surface? Rarely → spacious. Daily →
compact.

### Page padding

| Viewport | Default | Compact | Spacious |
|---|---|---|---|
| Mobile (<640px) | 16px | 12px | 20px |
| Tablet (640–1024px) | 24px | 16px | 32px |
| Desktop (>1024px) | 32px | 24px | 48–64px |

Never let page padding drop below 16px on mobile — text touching the screen edge reads as
broken, and on curved-edge devices it can be clipped.

### Grid gaps

| Context | Default | Compact | Spacious |
|---|---|---|---|
| Card grid | 24px | 16px | 32px |
| Form fields (vertical) | 16px | 12px | 24px |
| Form label → input | 8px | 4px | 8px |
| Dense table rows | — | 0 (borders separate) | — |
| Inline controls | 8px | 4px | 12px |

---

## 4. Typography

### Families

Three roles. Two are usually enough.

| Role | Purpose | Notes |
|---|---|---|
| **Display/heading** | Headlines, titles | May differ from body, or may be the same family at different weights |
| **Body/UI** | Paragraphs, labels, controls | Prioritise legibility at 14–16px and a real range of weights |
| **Mono** | Code, IDs, technical values, tabular numerics | Required if your product shows any of those |

**If your product uses a proprietary or licensed typeface, document a substitute.** 59 of 74
sources publish a `Note on Font Substitutes`, and it is what makes those systems usable at
all. A system whose type nobody can license is decoration.

**Do not use monospace for general interface text.** One corpus source sets an entire page in
monospace (`design-md/opencode.ai/`). It is coherent and deliberate and it is an exception —
it reduces reading speed and eliminates the visual distinction that makes code *read* as
code. See [categories/developer-tools.md](categories/developer-tools.md) §Monospace.

### Type scale

Sizes in px. Line-height unitless. Tracking in px at the stated size.

| Token | Default | Compact | Spacious | Weight | LH | Tracking | Use |
|---|---|---|---|---|---|---|---|
| `display-1` | 56 | 40 | 72 | 500–700 | 1.05 | −1.5 | Page hero, once per page |
| `display-2` | 44 | 32 | 56 | 500–700 | 1.10 | −1.0 | Major section opener |
| `display-3` | 36 | 28 | 44 | 500–600 | 1.15 | −0.6 | Sub-section opener |
| `heading-1` | 28 | 24 | 32 | 500–600 | 1.20 | −0.4 | Page title in-app |
| `heading-2` | 22 | 20 | 24 | 500–600 | 1.30 | −0.2 | Card title, panel title |
| `heading-3` | 18 | 16 | 20 | 500–600 | 1.40 | 0 | Group label |
| `subtitle` | 18 | 16 | 20 | 400 | 1.50 | 0 | Lead paragraph, hero subhead |
| `body-lg` | 18 | 16 | 20 | 400 | 1.55 | 0 | Long-form reading |
| `body` | **16** | 14 | 16 | 400 | 1.50 | 0 | **Default body — do not go below 14** |
| `body-sm` | 14 | 13 | 14 | 400 | 1.45 | 0 | Secondary text, table cells, help text |
| `caption` | 12 | 12 | 13 | 400 | 1.40 | +0.1 | Metadata, timestamps |
| `overline` | 12 | 11 | 12 | 500–600 | 1.30 | +0.8 | Uppercase eyebrow labels |
| `label` | 14 | 13 | 14 | 500 | 1.20 | 0 | Buttons, form labels |
| `code` | 14 | 13 | 14 | 400 | 1.50 | 0 | Inline and block code |
| `numeric` | 16 | 14 | 16 | 400–500 | 1.40 | 0 | **Tabular figures on** |

**Rules that hold across the entire corpus:**

1. **16px body is the strongest single convergence** — 61 of 74 files. 14px is the secondary
   step, not the primary one. Going below 14px for body text fails readability for a
   meaningful share of users.
2. **Line-height falls as size rises.** 1.5 at body, 1.05–1.15 at display. No source sets
   display type at body leading.
3. **Negative tracking scales with display size** — roughly 2–4% of font size above 40px.
   Default letter-spacing looks loose at hero scale.
4. **Small uppercase text takes positive tracking** — +0.2 to +1.5px. Capitals need air.
5. **Tabular figures wherever numbers are compared vertically.** `design-md/stripe/`
   documents a dedicated tabular body token. Proportional digits make columns jitter and
   make numbers genuinely harder to compare.

**Scale coherence:** each step should be 1.15×–1.35× its neighbour. Steps closer than 1.1×
are indistinguishable and create false precision; gaps above 1.5× leave you without a size
when you need one.

### Display size ceiling by category

| Surface | Largest display |
|---|---|
| Marketing / brand | 56–80px |
| Documentation | 36–56px |
| Application (in-product) | 24–32px |
| Editorial | 40–72px |
| Dashboard | 20–28px |

Marketing display sizes inside an application are the most recognisable symptom of a
foundation applied without a category. A 72px heading above a data table is not confident,
it is misfiled.

### Measure (line length)

**45–75 characters for body text; 60–70 is the target.**

This produces:

| Body size | Prose column |
|---|---|
| 14px | 480–560px |
| 16px | 560–680px |
| 18px | 640–760px |

The corpus confirms the distinction: files documenting both a page container and a prose
column show 1200–1440px for the container and 640–960px for reading. Full-width paragraphs
on a 1440px display are a layout bug, not a stylistic choice.

---

## 5. Colour

### Structure

| Group | Count | Purpose |
|---|---|---|
| Neutral ramp | 10–12 steps | Surfaces, text, borders — the workhorse |
| Brand/accent | **1** primary, plus hover/active/disabled | Action and identity |
| Semantic | 4 hues × (text + surface + border) | Success, warning, danger, info |
| Extended accent | 0–4, optional | Only if mapped to structure |

Target **25–44 semantic tokens**. That is the corpus's modal range. Below ~20 you are
missing states; above ~50 you are usually documenting per-illustration colours rather than
interface roles.

### Accent discipline — the corpus's strongest qualitative finding

**50 of 74 sources use zero or one chromatic accent**, reserved for the primary action, the
brand mark, and the focus state.

**Default: one accent.** Colour is your clearest instruction to a user; when exactly one
thing is coloured, that instruction is unambiguous. A second decorative accent halves the
first one's value.

**If you need more than one, each additional colour must map to something structural** —
product lines, content categories, object types, or data series. Every multi-accent system
in the corpus does this: one maps five stops to product categories, another maps accents to
individual products, others echo colours users already see inside the product. None uses
multiple accents as decoration.

### Neutral ramp

Build one ramp and derive surfaces, text, and borders from it. Approximate lightness
targets:

| Step | L* | Light-mode role | Dark-mode role |
|---|---|---|---|
| 50 | 98 | Canvas | — |
| 100 | 96 | Raised surface | — |
| 200 | 90 | Subtle border | — |
| 300 | 83 | Default border | Tertiary text |
| 400 | 70 | Disabled text | Secondary text |
| 500 | 57 | Tertiary text | — |
| 600 | 45 | Secondary text | Strong border |
| 700 | 35 | — | Default border |
| 800 | 25 | Inverse surface | Raised surface |
| 900 | 15 | Primary text | Canvas (near-black) |
| 950 | 8 | — | Deep canvas |

**Tint your neutrals or don't — but be consistent.** Pure grey is neutral and slightly
clinical. A tinted ramp (warm or cool) reads more intentional. The corpus's warm-editorial
cluster tints canvas *and* ink together; mixing a warm canvas with pure-black ink produces
the muddiness that a consistent temperature avoids.

### Semantic colour

| Status | Hue family | Requirement |
|---|---|---|
| Success | Green | Text ≥4.5:1 on its surface |
| Warning | Amber/orange | Amber is hard on white — darken the text token, don't reuse the fill |
| Danger | Red | Must be distinguishable from your brand hue if the brand is red |
| Info | Blue | Must be distinguishable from `action.primary` if that is blue |

**Never encode meaning in colour alone.** Every status needs a second channel — icon,
label, shape, or position. This is non-negotiable and applies to every category. Roughly 8%
of men have a colour-vision deficiency; a red/green success/failure pair with no icon is
unreadable to them.

### Focus

**A visible focus indicator is mandatory.** Specification:

- 2px ring, offset 2px from the element edge
- ≥3:1 contrast against **both** the element and the surrounding surface
- `:focus-visible`, so pointer users don't see rings on click but keyboard users always do
- Never `outline: none` without a replacement

Only 14 of 74 sources document a focus ring. That is a corpus gap, not permission to skip
it — this requirement comes from WCAG, not from the corpus.

---

## 6. Light and dark mode

**Dark mode is not inverted light mode.** No source in the corpus describes it as one, and
the two that document both polarities describe them as separate surface systems.

| Property | Light mode | Dark mode | Why they differ |
|---|---|---|---|
| Canvas | Near-white (L* 96–99) | Near-black (L* 8–14), **not** `#000000` | Pure black + bright text causes halation; a slight lift reduces eye strain |
| Elevation direction | Raised surfaces get **lighter** | Raised surfaces get **lighter** | Light comes from above in both; do not darken to raise |
| Elevation mechanism | Shadow works | **Shadow barely reads** — use lightness steps + hairlines | This is the biggest structural difference |
| Body text | L* 15–25 on light canvas | L* 85–92, **not** pure white | Pure white on near-black over-contrasts and vibrates |
| Secondary text | ~4.6:1 | Needs *more* lightness headroom | Contrast perception compresses at the dark end |
| Borders | Darker than surface | **Lighter** than surface, often translucent white | Same relationship, opposite direction |
| Saturated colour | Works as-is | Desaturate 10–20% and lighten — **for text, icons, borders only** | Saturated hues vibrate against dark and lose legibility |
| Brand accent (as text/icon/link) | Brand value | Lighter variant | The hue tuned for white text frequently fails as text on near-black |
| Brand accent (as a **filled** background) | Brand value | **Do not lighten** — keep it dark enough for its white label | See the warning below |

> **The lightening rule has one hard exception, and it is easy to get wrong.**
> "Lighten saturated colours for dark mode" and "filled buttons use white labels" are
> contradictory instructions. Lightening a fill while keeping a white label *always* reduces
> contrast. A build test of this layer's own dashboard template measured **3.68:1** for white on a
> lightened accent and **2.92:1** for white on a lightened danger colour — both failing the 4.5:1
> floor.
>
> **So split each action colour into two dark-mode tokens:**
>
> | Token | Use | Constraint |
> |---|---|---|
> | `action.primary` | Filled button/badge background | ≥4.5:1 against its own label. Usually means *not* lightening it |
> | `action.primary-on-dark` | Text, icons, links, borders on a dark surface | ≥4.5:1 against the dark surface |
>
> Never use an `-on-dark` value as a filled background. Compute both pairs; do not eyeball them.
| Imagery | As authored | Consider a 5–10% overlay | Bright images glare against a dark surface |

**Dark surface ladder** — the corpus's clearest model, documented most completely by
`design-md/linear.app/`:

```
canvas    L* 8–12    page background
raised-1  L* 14–17   cards, panels
raised-2  L* 19–22   hovered cards, featured panels
raised-3  L* 24–28   menus, popovers, dropdowns
overlay   L* 28–32   modals, dialogs
```

Plus 1–3 hairline weights at L* 25–40. Four to five steps is enough; more become
indistinguishable.

**Test both modes at every step.** A palette that passes contrast in light mode frequently
fails in dark — most often on secondary text and on the brand accent.

---

## 7. Elevation and depth

Elevation communicates one of three things: **grouping**, **interactivity**, or
**layering**. Decide which before reaching for a shadow.

| Level | Light mode | Dark mode | Use |
|---|---|---|---|
| 0 | No treatment | No treatment | Body content, page background |
| 1 | 1px `border.subtle`, or `surface.raised` | `raised-1` + hairline | Cards, panels, grouping |
| 2 | Small shadow (0 1px 3px / 0.08) | `raised-2` + hairline | Hovered/active cards |
| 3 | Medium shadow (0 4px 12px / 0.10) | `raised-3` + hairline | Dropdowns, popovers, menus |
| 4 | Large shadow (0 12px 32px / 0.14) + scrim | `overlay` + hairline + scrim | Modals, dialogs |

**Rules:**

- **Border-first, not shadow-first.** ~38 of 74 sources carry hierarchy with surface steps
  and hairlines. Borders are cheaper, sharper, and mode-agnostic. Use shadow when something
  genuinely floats above the page.
- **On dark canvases, shadow is nearly useless.** Use lightness steps. ~14 of 14 dark
  sources do.
- **Never mix mechanisms at one level.** Cards with borders *and* shadows *and* surface lift
  read as three inconsistent decisions.
- **Shadow implies interactivity to users.** A static card with a heavy shadow reads as
  clickable. If it isn't, use a border.
- **Overlays need a scrim.** Even a flat, shadowless system needs a background dim
  (`rgba(0,0,0,0.4)` light, `0.6` dark) or the layer boundary disappears.

---

## 8. Border radius

**Pick one character and hold it.** Radius is where inconsistency shows fastest, because
mismatched corners are visible side by side.

| Token | Squared | Default | Soft | Applies to |
|---|---|---|---|---|
| `radius.none` | 0 | 0 | 0 | Tables, full-bleed, dividers |
| `radius.xs` | 1–2px | 4px | 6px | Chips, badges, tags |
| `radius.sm` | 2px | 6px | 10px | Small controls, inputs |
| `radius.md` | 4px | 8px | 14px | **Buttons, inputs, selects** |
| `radius.lg` | 4–6px | 12px | 20px | Cards, panels |
| `radius.xl` | 8px | 16px | 28px | Large cards, media frames |
| `radius.2xl` | 8px | 24px | 40px | Feature panels, hero cards |
| `radius.full` | 9999px | 9999px | 9999px | Avatars, pills, toggles |

The corpus holds three distinct positions, not a spectrum — ~18 squared systems (0–4px),
~40 moderate (6–16px), ~16 soft (20–40px+). Their average, ~10px, satisfies none of them.

**Choosing:**

| Signal | Choose |
|---|---|
| Precision, engineering, density, enterprise gravitas | Squared |
| Contemporary, neutral, broadly appropriate | Default |
| Approachability, consumer warmth, reduced anxiety | Soft |

**Nesting rule:** an inner radius should be the outer radius minus the padding between them.
A 12px card with 8px padding wants ~4px on an inner element. Equal inner and outer radii
produce a visible gap at the corner.

**Radius scales with component size.** 16px on a 32px-tall control makes it nearly a pill;
4px on a 400px-wide panel is invisible. If your soft system needs a compact control, use
`radius.sm`, not `radius.2xl`.

---

## 9. Component dimensions

### Control heights

| Control | Default | Compact | Spacious | Notes |
|---|---|---|---|---|
| Button | 40px | 32px | 48px | 44px minimum on touch |
| Text input | 40px | 32px | 48px | Match button height exactly |
| Select | 40px | 32px | 48px | Match input |
| Checkbox / radio | 16–20px | 16px | 20px | Hit area still 44px on touch |
| Icon button | 40px | 32px | 48px | Square |
| Table row | 48px | 36px | 56px | Compact only for expert users |
| Nav bar | 64px | 56px | 72px | Corpus is bimodal at 56/64 |
| Tab | 40px | 36px | 48px | |
| List row | 48px | 40px | 56px | |

The corpus is clearly bimodal — controls cluster at 36–48px (40px most common, 22 files),
navigation at 56–64px (both 22 and 14 files).

**Compact heights are for pointer-driven expert tools only.** A 32px button is unreachable
by touch and marginal for users with motor impairments. If your surface is ever used on a
touch device, 44px is the floor.

### Padding

| Element | Default | Compact | Spacious |
|---|---|---|---|
| Button | 10px 18px | 6px 12px | 14px 24px |
| Text input | 10px 14px | 6px 10px | 14px 16px |
| Card | 24px | 16px | 32px |
| Modal body | 24px | 16px | 32px |
| Panel | 24px | 16px | 32px |
| Table cell | 12px 16px | 8px 12px | 16px 20px |
| Section band | 64px 32px | 32px 24px | 96px 48px |

Button padding of 10×18 is the corpus mode (11 files). **Horizontal padding runs 1.5–2×
vertical** — that ratio is what makes a control read as a control.

### Widths

| Element | Default | Compact | Spacious | Notes |
|---|---|---|---|---|
| Page container | 1280px | 1024px | 1440px | 1280 in 27 files, 1200 in 19 |
| Prose column | 680px | 560px | 760px | Follow measure, not container |
| Sidebar (nav) | 240px | 200px | 280px | Collapsed rail: 56–64px |
| Sidebar (detail/inspector) | 320px | 280px | 400px | |
| Modal — confirm | 400px | 360px | 480px | |
| Modal — form | 560px | 480px | 640px | |
| Modal — complex | 800px | 720px | 960px | Reconsider: this may be a page |
| Drawer (side) | 400px | 320px | 480px | |
| Dropdown menu | 200–280px | 180px | 320px | |
| Toast | 360px | 320px | 400px | |

**Two widths, always.** A page container and a reading measure are different numbers. The
corpus makes this explicit wherever a source documents both.

### Icons

| Size | Use |
|---|---|
| 16px | Inline with 14px text, dense table cells |
| 20px | Inline with 16px text, standard buttons — **default** |
| 24px | Navigation, standalone actions, toolbars |
| 32px | Feature icons, empty-state glyphs |
| 48px+ | Illustration territory, not iconography |

Match icon size to the text it sits beside: 16px icon with 14px text, 20px with 16px. Use
one stroke weight throughout — mixing 1.5px and 2px strokes is visible and reads as
carelessness.

---

## 10. Responsive model

### Breakpoints

| Name | Min-width | Layout |
|---|---|---|
| `xs` | 0 | Single column, stacked, drawer navigation |
| `sm` | 480px | Single column, larger type |
| `md` | 768px | 2-column grids, tablet navigation |
| `lg` | 1024px | Multi-column, sidebar appears |
| `xl` | 1280px | Full desktop, max container engages |
| `2xl` | 1440px | Wide desktop, optional extra column |

The corpus's second-strongest convergence after 16px body: 1440px (37 files), 1280px (35),
1024px (34), 768px (33), 480px (20), with 640px common as an extra step.

**Design at 1280px and 375px first.** Those cover the majority of real traffic. The others
are interpolation.

### What happens at each boundary

Choose deliberately per element — this is the part most often skipped:

| Behaviour | Meaning | Good for |
|---|---|---|
| **Resize** | Same layout, smaller values | Type, padding, images |
| **Reflow** | Columns reduce | Card grids, feature rows |
| **Collapse** | Multiple elements become one | Nav → hamburger, tabs → select |
| **Stack** | Side-by-side becomes vertical | Two-column layouts, form rows |
| **Scroll** | Content overflows in a bounded container | Wide tables, toolbars, tab strips |
| **Drawer** | Content moves off-canvas | Sidebars, filters, secondary nav |
| **Transform** | Different component, same job | Table → card list; dropdown → bottom sheet |
| **Defer** | Available but not primary | Bulk actions, advanced filters |
| **Omit** | Genuinely unavailable | Only when the task is impossible on the device — say so |

**A wide data table must not simply shrink.** Either scroll it horizontally in a bounded
container with the identifying column pinned, or transform each row into a card. Squeezing
twelve columns into 375px produces something no one can read.

**Omit is a legitimate choice, but it must be honest.** If a capability genuinely does not
work on a phone, say so in the interface. Silently hiding it is worse than a clear message.

### Mobile requirements *(partly synthesized)*

The corpus cannot support these — many sources state their responsive guidance is
synthesized from desktop evidence. These come from platform guidance and general practice:

- Touch targets ≥44px, with ≥8px between adjacent targets
- Primary action reachable in the lower two-thirds of the screen
- No hover-only interactions — every hover affordance needs a tap equivalent
- Respect safe-area insets on notched and curved devices
- Body text ≥16px (also prevents iOS zoom-on-focus)
- Sticky elements must not consume more than ~20% of viewport height

**A mobile layout is not a compressed desktop layout.** Priority changes: navigation
collapses, secondary content moves below, dense tables become lists, multi-step forms gain
progress indication. Same content, re-ranked.

---

## 11. Interaction states *(synthesized)*

The corpus's largest gap — many files state "hover states not documented by system policy",
and validation states are repeatedly listed as unobserved. Everything here comes from
general interface practice.

**Every interactive element needs all of these:**

| State | Requirement |
|---|---|
| Default | Resting appearance |
| Hover | Visible change (surface, border, or text). Pointer devices only |
| Focus-visible | 2px ring, ≥3:1 contrast, offset 2px. Keyboard-triggered |
| Active/pressed | Distinct from hover — usually darker or slightly inset |
| Disabled | Reduced contrast, `cursor: not-allowed`, still ≥3:1 for legibility, and communicate **why** |
| Loading | In-place indicator, preserved dimensions, disabled interaction |
| Selected | Distinct from hover and from focus — three different meanings |
| Error | Border + icon + message. Never colour alone |

**Design tokens for state changes** rather than ad-hoc values:

```
Light mode: hover  = surface darkens ~4%   Dark mode: hover  = surface lightens ~6%
            active = surface darkens ~8%               active = surface lightens ~10%
```

**Loading must not shift layout.** Reserve the space. A spinner that replaces a button label
and changes its width makes the page jump — and users click the wrong thing.

**Three states, three meanings, three appearances:** hover (pointer is here), focus (keyboard
is here), selected (this is chosen). Collapsing any two makes keyboard navigation
ambiguous.

---

## 12. Motion

**Motion communicates causality, hierarchy, progress, or spatial relationship. If it does
none of those, remove it.**

| Duration | Use |
|---|---|
| 100ms | Colour and opacity changes, hover feedback |
| 150–200ms | Small transitions — dropdowns, tooltips, toggles |
| 250–300ms | Panels, drawers, modals |
| 400ms+ | Large spatial transitions. Rarely justified |

| Easing | Use |
|---|---|
| `ease-out` | Entering. Fast start, gentle settle — feels responsive |
| `ease-in` | Exiting. Accelerates away |
| `ease-in-out` | Moving within the viewport |
| `linear` | Progress indicators and spinners only |

**Rules:**

- **Never animate a blocking interaction.** A 300ms delay before a menu opens is 300ms of
  the user waiting.
- **Animate `transform` and `opacity`.** Animating `width`, `height`, or `top` triggers
  layout on every frame and drops frames on cheap hardware.
- **Honour `prefers-reduced-motion`.** Replace movement with a cross-fade; never remove the
  state change itself.
- **Nothing loops except progress indicators.** A perpetually animating decorative element
  is a permanent distraction and a battery cost.
- **Entrance animations on page load delay content.** Skip them on repeat-visit surfaces.

---

## 13. Accessibility floor

**Non-negotiable in every category.** Taken from the WCAG specification, not inherited from
the corpus — 56 sources assert conformance but none demonstrates a computed ratio, so no
source's self-assessment was adopted (see
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D9).

| Requirement | Threshold |
|---|---|
| Body text contrast | ≥4.5:1 |
| Large text (≥24px, or ≥19px bold) | ≥3:1 |
| UI component boundaries and states | ≥3:1 |
| Focus indicator | ≥3:1 against element **and** adjacent surface |
| Touch target | ≥44×44px, ≥8px separation |
| Text resize | Usable to 200% without loss of content |
| Colour independence | Never the sole carrier of meaning |
| Keyboard | Every action reachable; visible focus; no traps |
| Motion | `prefers-reduced-motion` respected |
| Form fields | Programmatic label; error text tied to the field |
| Headings | One `h1`; no skipped levels |
| Images | Meaningful alt text; `alt=""` for decoration |
| Live regions | Announce async changes (toasts, validation, streaming) |

**Where accessibility conflicts with an aesthetic preference, accessibility wins.** Light
grey placeholder text at 2:1 is a defect regardless of how clean it looks.

**Two checks that catch most real failures:**

1. Navigate a complete task using only the keyboard.
2. Set the OS to greyscale and verify every status is still distinguishable.

---

## 14. Content and hierarchy

Content design is design. A well-styled interface with unclear labels fails.

- **One primary action per view.** If everything is emphasised, nothing is.
- **Buttons name their outcome.** "Save changes", "Delete project" — not "OK", "Submit".
- **Destructive actions name the target**, in the button and the confirmation: "Delete
  3 invoices".
- **Errors state what happened and what to do next.** "Card declined — try another payment
  method" beats "Transaction failed".
- **Empty states explain and offer an action.** An empty table with no explanation reads as
  a bug.
- **Loading states say what is loading** when it exceeds ~1 second.
- **Sentence case for UI text.** Easier to scan than Title Case; reserve caps for short
  overline labels.
- **Numbers get units and context.** "1,284 requests (last 24h)", not "1284".
- **Dates: absolute for records, relative for recency.** "12 Mar 2026" in an audit log;
  "3 minutes ago" in a feed.

---

## 15. Navigation

Full derivation logic is in
[DESIGN-DECISION-HANDBOOK.md](DESIGN-DECISION-HANDBOOK.md) §Navigation. Defaults:

| Pattern | Height/Width | Use when |
|---|---|---|
| Top bar | 64px | ≤7 destinations; public sites; shallow apps |
| Side nav | 240px | >7 destinations; app with sections; frequent switching |
| Collapsed rail | 56–64px | Side nav where canvas space is scarce |
| Tabs | 40px | 2–6 views of the *same* object |
| Breadcrumbs | — | Hierarchy ≥3 levels deep |
| Command palette | — | Expert users, many destinations, keyboard-driven |
| Bottom nav | 56px + safe area | Mobile, 3–5 top destinations |
| Contextual/inline | — | Actions on the current object |

**Never duplicate the same destinations in two navigation systems.** Top bar *and* side nav
listing the same items forces the user to learn which one to trust.

---

## 16. Forms

| Rule | Reason |
|---|---|
| Labels above fields | Fastest scanning; survives narrow viewports; never truncates |
| Never use placeholder as label | Disappears on input; fails contrast; breaks screen readers |
| Single column | Two-column forms cause skipped fields and ambiguous tab order |
| Group related fields | 32px between groups, 16px within |
| Mark optional, not required | If most fields are required, marking each is noise |
| Validate on blur, not on keystroke | Errors while typing are interruptions |
| Errors adjacent to the field | Icon + text + border; not colour alone |
| Summarise errors on submit | With links to each field, for long forms |
| Preserve input on error | Never clear a form the user just filled in |
| Full-width submit on mobile | Reachable, unambiguous |
| Input height matches button height | Adjacent controls must align |
| Never disable submit silently | Explain what is missing |

---

## 17. Feedback

| Mechanism | Use | Duration |
|---|---|---|
| Inline validation | Field-level problems | Until resolved |
| Toast | Transient confirmation | 4–6s, dismissible |
| Banner | Page-level state needing acknowledgement | Until dismissed |
| Modal | Blocking confirmation only | Until answered |
| Inline spinner | Local loading | Until complete |
| Skeleton | Initial content load with known shape | Until loaded |
| Progress bar | Multi-step or long operations with known progress | Until complete |
| Empty state | No data yet | Persistent |

**Match severity to mechanism.** A modal for a successful save is an interruption. A toast
for a failed payment is too quiet — it will be missed. Destructive and irreversible actions
get a modal; everything routine gets a toast.

**Never confirm success with a modal.** The user's next action already tells them it worked.

---

## 18. Applying this foundation

1. Copy [templates/DESIGN.foundation.md](templates/DESIGN.foundation.md) into your project
   as `DESIGN.md`.
2. Identify your product category using
   [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md).
3. Apply the relevant guide from [categories/](categories/) — it overrides density,
   navigation, and component emphasis, **not** the scales.
4. Choose a density mode (compact / default / spacious) and apply it consistently.
5. Set brand values: typeface, accent hue, radius character.
6. Validate against a real screen using
   [checklists/foundation-review.md](checklists/foundation-review.md).

**What is yours to decide and what is not:**

| Yours | Foundation's |
|---|---|
| Typeface | Scale ratios and hierarchy |
| Accent hue | Accent discipline (one, scarce) |
| Radius character | Radius consistency and nesting |
| Density mode | Available modes |
| Canvas polarity | That both modes are designed separately |
| Voice and imagery | Accessibility floor |

Change the scales only with a reason you can state. Arbitrary values are the thing this
document exists to prevent.
