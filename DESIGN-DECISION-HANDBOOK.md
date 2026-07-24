# Design Decision Handbook

Rules for deriving design decisions from product requirements. Not a style guide — a set of
"if the requirement is X, the design consequence is Y" derivations.

Use when a template or guide says "choose", or when you need to justify a decision to someone
who will ask why.

---

## 1. Typography

### Choosing families

| Requirement | Consequence |
|---|---|
| Long-form reading (>800 words typical) | Body at 18–19px, line-height 1.6–1.75. Serif is a legitimate choice |
| Dense UI, many small labels | A sans with good small-size legibility and a real weight range. Avoid geometric faces with ambiguous `l`/`I`/`1` |
| Code or technical identifiers present | A mono family is mandatory, not optional |
| Numeric comparison | Tabular figures required — check the family supports them |
| Non-Latin scripts needed | Verify glyph coverage before committing. This kills more type choices than aesthetics |
| Strong existing brand | Brand face for display; a legible workhorse for body if the brand face is weak below 24px |
| Small display sizes only (in-app) | One family at multiple weights is sufficient. Two families is overhead |
| Proprietary or licensed face | **A documented substitute is mandatory.** 59 of 74 corpus sources publish one — it is what makes those systems usable |

**Two families is usually the right answer. Three is the maximum.** Display + body + mono. A
fourth family is almost always an unresolved decision rather than a design choice.

### Choosing the scale

| Requirement | Consequence |
|---|---|
| Marketing surface | Display ceiling 56–80px; ratio 1.25–1.35 between steps |
| Application surface | Display ceiling 24–32px; ratio 1.15–1.25 — tighter, because the range is narrower |
| Documentation | Display ceiling 36–56px; headings are wayfinding, not persuasion |
| Editorial | Display ceiling 48–72px on openers; body larger than elsewhere |
| Dense operational | Display ceiling 20–28px; body 13–14px |
| Deep heading hierarchy (4+ levels) | Tighter ratio (1.15) so you do not run out of distinguishable sizes |
| Shallow hierarchy | Wider ratio (1.35) for clearer contrast |

**Coherence test:** every adjacent pair should differ by 1.15×–1.35×. Closer than 1.1× and the
steps are indistinguishable — you have created false precision. Wider than 1.5× and you will
need a size you do not have, and someone will invent one.

### Localisation effects on type

| Factor | Consequence |
|---|---|
| German, Finnish | Words run 30–40% longer. Do not fix button or label widths |
| CJK | Needs larger minimum sizes; line-height rules differ; letter-spacing is usually wrong |
| RTL (Arabic, Hebrew) | Mirror the layout, not the content. Numbers and code stay LTR |
| Multi-script | Verify weight availability across scripts — a face with 5 Latin weights may have 2 for others |
| Any translation | Reserve ~30% expansion room in constrained UI |

### Reading length and measure

| Content | Measure | Body size |
|---|---|---|
| Long-form article | 640–720px | 18–19px |
| Documentation | 680px | 16px |
| Marketing body | 680px | 16–18px |
| In-app descriptive text | 560–640px | 14–16px |
| Table cell content | Column width | 13–14px |
| Chat / assistant output | 680–760px | 16px |

**The measure rule holds regardless of container width.** A 1440px container with 1440px-wide
paragraphs is a layout defect. The corpus's documentation surfaces demonstrate this: the same
brands use 1280–1440px containers for marketing and 720–960px measures for reading.

---

## 2. Colour

### Deriving the palette

| Requirement | Consequence |
|---|---|
| Brand recognition matters | One brand hue as `action.primary`; keep it scarce |
| Many statuses to communicate | Invest in a full semantic set before adding brand colour variety |
| Data visualisation needed | A separate categorical palette, 6–8 hues, isolated from semantic colours |
| Multiple products or tenants | One mapped token per product/tenant; everything else shared |
| High-trust context | Restraint. Semantic clarity beats brand expression |
| Dark mode required | Design it separately; the brand hue usually needs a lighter variant |
| Regulated accessibility | Compute every foreground/background pair; do not rely on eyeballing |
| Print or greyscale output | Verify every distinction survives desaturation |

### How many accents

| Accents | When | Requirement |
|---|---|---|
| 0 | Photography, typography, or data carries all interest | Neutrals must be genuinely well-tuned; nothing hides a weak ramp |
| **1** | **Default. 44 of 74 corpus sources** | Reserved for primary action, brand mark, focus, active state |
| 2 | Brand hue plus a distinct link or secondary-action colour | Both must be distinguishable from every semantic colour |
| 3–5 | Multi-product, multi-category, or data-series needs | **Each must map to something structural** — never decoration |
| 6+ | Illustration palettes only | Confine to illustration; never let them into chrome |

**The mapping requirement is the whole discipline.** Every multi-accent system in the corpus maps
colours to product lines, content categories, or object types. Unmapped accents dilute your
semantic colours until a warning no longer reads as a warning.

### Semantic colour construction

Each status needs three tokens, not one:

```
status.success        text and icons        ≥4.5:1 on its surface
status.success-surface  background tint     ≥3:1 against page canvas
status.success-border   border              ≥3:1
```

Using one value for all three fails: a fill light enough to sit behind text is too light to *be*
text.

| Constraint | Consequence |
|---|---|
| Brand hue is red | Danger needs a distinctly different red, or a different hue entirely |
| Brand hue is green | Success needs differentiation, or use a checkmark as the primary channel |
| Brand hue is blue | `status.info` must differ from `action.primary`, or drop `info` and use neutral |
| Amber warning on white | Amber text rarely reaches 4.5:1 — darken the text token, keep amber for the fill |

### Dark mode derivation

**Never invert.** Derive:

| Light value | Dark equivalent | Why not inversion |
|---|---|---|
| Canvas L* 98 | Canvas L* 8–12 | Pure black causes halation with bright text |
| Text L* 15 | Text L* 85–92 | Pure white over-contrasts and vibrates |
| Raised = lighter | Raised = **lighter** | Light comes from above in both modes |
| Border darker than surface | Border **lighter** than surface | Direction reverses; relationship does not |
| Shadow for elevation | Lightness steps for elevation | Shadow does not read on dark |
| Brand hue as-is | Brand hue lightened, desaturated 10–20% | Saturated colour vibrates against dark |

The one rule that surprises people: **raised surfaces get lighter in both modes.** Darkening a
card to make it "recede into" a dark page inverts the light model and reads as a hole.

---

## 3. Spacing

| Requirement | Consequence |
|---|---|
| Daily or all-day use | Compact: 32–48px section rhythm, 12–16px card padding |
| Occasional use | Default: 48–80px rhythm, 24px padding |
| Single-visit persuasion | Spacious: 80–96px rhythm, 32px padding |
| Touch-primary | Never compact spacing between targets — 8px minimum separation, 44px targets |
| High information density | Tighten space; **never tighten contrast**. Those are different levers |
| Deep hierarchy | Space must encode grouping: 2× between groups vs. within |
| Long forms | 32px between field groups, 16px within, 8px label-to-input |

**The grouping ratio does more work than absolute values.** If related items sit 16px apart and
groups sit 32px apart, the structure reads without borders or headings. Uniform spacing
everywhere means the user has to read to find structure.

**Space above a heading should be ~2× the space below it.** Otherwise headings float between
blocks rather than introducing the one that follows.

---

## 4. Navigation

### Choosing the pattern

Decision order — first match wins:

```
Is the primary device mobile?
  → bottom nav (3-5 destinations) or drawer

How many top-level destinations?
  ≤ 7  → top bar
  8-20 → side nav 240px
  20+  → side nav with groups + search + command palette

Is canvas space scarce (map, editor, analytics)?
  → collapsed rail 56px

Are these views of the SAME object?
  → tabs (2-6), not navigation

Are users expert and keyboard-driven?
  → add a command palette (in addition, never instead)

Is the hierarchy 3+ levels deep?
  → add breadcrumbs
```

| Factor | Effect |
|---|---|
| Role count ≥3 | Per-role navigation, built from one component |
| Workflow depth ≥3 levels | Breadcrumbs mandatory |
| Application breadth 20+ destinations | Search becomes primary; grouping mandatory |
| Visit frequency daily | Optimise for switching speed — persistent nav, keyboard shortcuts |
| Visit frequency rare | Optimise for orientation — labels, descriptions, clear IA |
| Content volume 200+ items | Search is primary navigation, not a convenience |

**Never duplicate destinations across two navigation systems.** Top bar and side nav listing the
same items forces the user to learn which is authoritative — and they will pick wrong.

**A command palette is always additive.** It must never be the only route to a feature; most
users never discover it.

---

## 5. Cards

Cards are over-used. They group, and grouping is not always needed.

| Use a card when | Do not use a card when |
|---|---|
| Items are independent and comparable | Items are rows in a sequence — use a table or list |
| Each item has mixed content (image, text, actions) | Each item is one line of text |
| Items are individually actionable as a whole | The page has one topic — the page *is* the container |
| The set is browsed rather than scanned | The set is scanned for a specific value |
| Items appear in a responsive grid | Content is a form — use grouped fieldsets |

**Symptoms of card overuse:**

- Nested cards. A card inside a card inside a panel has three borders doing one job.
- A card containing exactly one paragraph. That is a paragraph.
- Every section of a page in its own card. The page is already the container.
- A card grid where users are comparing values — cards break horizontal alignment, and comparison
  needs alignment. Use a table.

**Card padding derivation:** 16px compact, 24px default, 32px spacious. If content needs more
than 32px, the card is probably a page section rather than a card.

---

## 6. Elevation

| Requirement | Mechanism |
|---|---|
| Group related content | **Border**, or a one-step surface change. Not shadow |
| Signal interactivity | Shadow, or a hover surface change |
| Layer above the page (menu, popover) | Shadow on light; surface step + border on dark |
| Block the page (modal) | Shadow + scrim, both modes |
| Convey physical lift (media, product) | Shadow — the one place it is unambiguously right |
| Dense information | Borders. Shadows create visual noise at density |
| Dark canvas | Lightness steps. Shadow does not read |

**Border-first is the corpus's dominant answer** — ~38 of 74 sources carry hierarchy with surface
steps and hairlines. Borders are sharper, cheaper, mode-agnostic, and do not imply
interactivity.

**Shadow implies clickability to users.** A static card with a heavy shadow reads as a button. If
it is not interactive, use a border.

**Never stack mechanisms at one level.** Border + shadow + surface lift on the same card is three
decisions where one was needed, and it looks like it.

---

## 7. Border radius

| Signal to send | Radius |
|---|---|
| Precision, engineering, density, gravitas | 0–4px |
| Contemporary, neutral, broadly safe | 6–16px |
| Approachable, consumer, anxiety-reducing | 20–40px |
| Interactive pill (toggle, tag, avatar) | `full` |

The corpus holds three distinct positions, not a spectrum — and their average (~10px) satisfies
none of them. Pick a position.

**Two structural rules:**

1. **Radius scales with component size.** 16px on a 32px control is nearly a pill; 4px on a 400px
   panel is invisible. A soft system still uses `radius.sm` on compact controls.
2. **Nesting: inner radius = outer radius − gap.** A 12px card with 8px padding wants ~4px inside.
   Equal radii leave a visible gap at the corner.

**Radius does not affect usability much, and inconsistent radius affects perception a lot.** It is
the cheapest place to look careless.

---

## 8. Motion

**Motion must communicate causality, hierarchy, progress, or spatial change. If it does none of
those, it is decoration and costs the user time.**

| Requirement | Consequence |
|---|---|
| High-frequency interaction | ≤100ms, or none. Animation is a tax paid per repetition |
| Spatial change (2D↔3D, drill-in) | 300–500ms — **here motion genuinely helps orientation** |
| Something appeared | 150–200ms ease-out |
| Something is loading | Indicate; do not animate the wait |
| Attention needed | One brief change, then stop. Never loop |
| Reduced motion set | Cross-fade or instant; **preserve the state change** |
| Blocking interaction | **No animation.** Never delay the user's next action |

| Property | Animate? |
|---|---|
| `transform`, `opacity` | Yes — compositor-only, cheap |
| `width`, `height`, `top`, `margin` | **No** — triggers layout every frame |
| `color`, `background-color` | Yes, briefly (≤150ms) |
| `box-shadow` | Sparingly — expensive |
| `filter`, `backdrop-filter` | Avoid on large surfaces |

**Frequency is the deciding factor.** A 300ms panel transition is elegant once and irritating on
the fortieth open. Dashboard and analytics interfaces should be nearly motionless.

---

## 9. Responsive behaviour

Decide **per element** which behaviour applies. Skipping this decision is why so many "responsive"
interfaces are just compressed desktop ones.

| Behaviour | Use for |
|---|---|
| Resize | Type, padding, images |
| Reflow | Card grids, feature rows |
| Collapse | Nav → hamburger; tabs → select |
| Stack | Side-by-side → vertical |
| Scroll | Wide tables, toolbars, tab strips — in a **bounded** container |
| Drawer | Sidebars, filters, secondary nav |
| Transform | Table → card list; dropdown → bottom sheet |
| Defer | Bulk actions, advanced options — available, not primary |
| Omit | Genuinely impossible on the device — **and said so in the interface** |

### Deciding what to omit

| Capability | Mobile |
|---|---|
| Reading, viewing, searching | Always available |
| Simple creation and editing | Always available |
| Purchase and payment | **Always available** — mobile is the majority channel |
| Multi-column comparison | Transform or defer |
| Bulk operations on many items | Defer or omit |
| Precise drawing or spatial editing | Omit — state it |
| Complex query building | Omit — state it |
| Wide multi-series analysis | Simplify, then omit — state it |

**Omission must be visible.** A message explaining that a capability needs a larger screen is
respectful. A control that silently does not exist reads as a broken product.

### Mobile is a re-ranking, not a compression

| Desktop | Mobile |
|---|---|
| Persistent nav | Collapsed; primary action stays visible |
| Sidebar filters | Drawer with explicit apply |
| Hover reveals actions | Actions visible or long-press |
| Dense table | Cards, or scroll with a pinned column |
| Multi-step form on one page | One step per screen with progress |
| Secondary content in a sidebar | Below primary content |
| Small controls | 44px minimum, 8px separation |

---

## 10. Accessibility as a derivation

Not a checklist item — a set of constraints that shape decisions upstream.

| Design decision | Accessibility constraint it must satisfy |
|---|---|
| Palette | Every foreground/background pair ≥4.5:1 body, ≥3:1 large and UI |
| Accent choice | Focus ring must reach ≥3:1 against element *and* surface |
| Status colour | Never the sole channel — icon or text required |
| Control size | ≥44px on touch, ≥8px separation |
| Density mode | Compact must still meet 44px hit areas on touch |
| Type scale | Body ≥14px, ≥16px on mobile; usable at 200% zoom |
| Motion | `prefers-reduced-motion` honoured without losing state |
| Navigation | Fully keyboard-operable, visible focus, no traps |
| Forms | Programmatic labels; errors tied to fields |
| Charts | Data available in a non-visual form |
| Maps | Information available in a list or table |
| Layout | Reading order matches visual order |
| Live updates | Announced via live regions, `polite` not `assertive` |

**Where accessibility conflicts with an aesthetic preference, accessibility wins.** Light grey
placeholder text at 2:1 is a defect no matter how clean it looks. The corpus is not a guide here —
56 sources assert conformance and none demonstrates a computed ratio.

---

## 11. Density derivation

| Input | Compact | Default | Spacious |
|---|---|---|---|
| Visit frequency | daily / all-day | weekly | rare / once |
| Session length | hours | minutes | seconds |
| Information density | dense | moderate | sparse |
| Expertise | expert / trained | mixed | none |
| Device | pointer | both | both |
| Error consequence | low–medium | medium | any |
| Primary task | scanning, comparing | completing | deciding |

**Two hard constraints:**

1. **Compact is pointer-only.** Touch overrides it — 44px targets, always.
2. **High-consequence flows are never compact.** Money movement, deletion, and irreversible
   actions get default density and generous separation between destructive and safe controls.
   Mis-clicks are the failure mode, and density increases them.

---

## 12. Choosing a visual tone

Tone is **not** derived from category. The corpus is unambiguous: developer tools appear in four
incompatible tone clusters; financial products appear both maximally squared and maximally soft.

Derive tone from these instead:

| Input | Effect |
|---|---|
| Existing brand strength | Strong brand leads; the foundation fills gaps |
| Audience expertise | Experts tolerate — and often prefer — density and restraint |
| Environment | A tool used beside an IDE benefits from dark continuity |
| Genre convention | Consider **breaking** it deliberately, as several corpus sources do |
| Emotional context | Anxious users (money, health) benefit from softer geometry and warmer neutrals |
| Content type | Photography-led wants recessive chrome; data-led wants neutral chrome |
| Longevity | Trend-heavy treatments date fast; restrained systems age slowly |

**Then hold it.** The failure is not choosing the wrong tone — it is choosing several and applying
them inconsistently.

---

## 13. Deciding when to break a rule

Every rule here has legitimate exceptions. A defensible break has all four:

1. **A stated reason** tied to a product requirement, not a preference.
2. **A named cost** — you can say what you are giving up.
3. **Consistency** — the exception applies system-wide, not to one screen.
4. **A record** — written in the project `DESIGN.md` so the next person inherits the reasoning
   rather than the anomaly.

The corpus supports this. An all-monospace page, a radius scale of only 0 and 9999, a 144px
display size — each is coherent within its own system, documented in its own file, and applied
consistently. They are positions, not accidents.

**An undocumented exception is indistinguishable from a mistake**, and six months later nobody
can tell which it was.
