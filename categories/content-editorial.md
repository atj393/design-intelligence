# Content and Editorial Products

Products whose primary job is being read at volume: publications, magazines, news, blogs,
long-form documentation-as-product, knowledge collections.

> **Evidence strength: moderate / partly corpus-backed.**
> Two sources document **real editorial products** rather than marketing surfaces —
> `design-md/theverge/DESIGN.md` and `design-md/wired/DESIGN.md`. That is a small sample but
> unusually direct evidence, and it is reinforced by strong typographic documentation across the
> corpus. Personalisation, feeds, and subscription flows are synthesized.

---

## 1. What distinguishes this category

The interface's job is to **disappear**. Every element competes with the text for attention, and
the text is the product.

| Editorial | Marketing |
|---|---|
| Success = article finished | Success = action taken |
| Type is the voice | Type is the pitch |
| Density serves scanning many stories | Density serves one message |
| Long sessions, deep reading | Short sessions, single decision |
| Return visits, habitual | First visits, evaluative |
| Chrome recedes | Chrome directs |

Both corpus editorial sources push **display type harder than most marketing sites** (up to
107px) while keeping the reading surface calm. The display type is brand voice on index and
opener surfaces; the article body is quiet.

## 2. Typography — the category's core competency

| Token | Default | Compact | Spacious |
|---|---|---|---|
| Headline (article) | 40px | 32px | 56px |
| Headline (index feature) | 48px | 36px | 72px |
| Deck / standfirst | 22px | 20px | 24px |
| Body | 18px | 16px | 19px |
| Body (serif) | 19px | 17px | 20px |
| Pull quote | 28px | 24px | 32px |
| Caption | 14px | 13px | 14px |
| Byline / metadata | 14px | 13px | 14px |
| Section label | 12px uppercase +1.0px | | |

**Body text runs larger here than anywhere else** — 18–19px against the 16px foundation
default. `design-md/wired/DESIGN.md` documents a 19px serif body face for long-form reading.
When someone reads 2,000 words, the extra size and leading are the difference between finishing
and leaving.

**Requirements:**

| Property | Value |
|---|---|
| Body line-height | **1.6–1.75** — the highest of any category |
| Measure | 60–70 characters (~640–720px at 18–19px) |
| Paragraph spacing | 1em, or a first-line indent — never both |
| Hyphenation | Off for ragged-right; acceptable when justified |
| Justification | Avoid on the web; it produces rivers without proper H&J |
| Widow/orphan control | Worth the effort on headlines |
| Serif vs. sans body | Serif is a legitimate, evidenced choice for long-form |

**Serif body text is well supported here.** One corpus editorial source uses a humanist serif
body face with a custom display serif for headlines; the other uses a brutally heavy display
sans. Both work — the choice is voice, not correctness.

**Display type is where editorial brands express themselves.** The corpus's editorial sources
run 64–107px display with distinctive faces. This is one of the few categories where an
unusual, high-personality typeface is an asset rather than a liability — because the display
type appears in isolation, at scale, on index pages, where legibility risk is low.

## 3. Article layout

```
┌──────────────────────────────────────┐
│  section label · date                │
│                                      │
│  HEADLINE                            │  ← 40–56px
│  Deck / standfirst                   │  ← 22px
│                                      │
│  byline · read time · share          │
│  ┌────────────────────────────────┐  │
│  │ lead image                     │  │
│  └────────────────────────────────┘  │
│  caption                             │
│                                      │
│  Body text at 640–720px measure      │
│  ...                                 │
└──────────────────────────────────────┘
```

| Element | Requirement |
|---|---|
| Measure | 640–720px, centred. **Non-negotiable** |
| Full-bleed elements | Images and pull quotes may exceed the measure; body text never does |
| Lead image | Consistent aspect ratio, with a caption and credit |
| Byline | Author (linked), date, read time |
| Reading progress | Subtle indicator for long pieces |
| In-article navigation | For very long pieces, a jump-to-section control |
| Related content | At the end, and optionally mid-article — but never mid-sentence |
| Sticky chrome | Minimal. A 64px sticky header on a reading surface costs a line of text per screen |

**Do not interrupt the reading flow with inserted content mid-paragraph.** Between sections is
acceptable; mid-paragraph is not.

## 4. Index and feed layouts

| Pattern | Use |
|---|---|
| **Hierarchical grid** | A lead story at feature scale, secondary stories smaller. Communicates editorial judgment |
| **Uniform grid** | Equal-weight items; chronological or topical |
| **List** | Dense, scannable, many items — best for archives and search results |
| **Timeline** | Chronological with date markers, for news |
| **Masonry** | Mixed-aspect visual content |

`design-md/theverge/DESIGN.md` documents saturated full-bleed colour story tiles arranged into
a timeline — the tiles themselves carry the editorial signal rather than a uniform card
treatment. This is a strong example of using colour at *panel* scale to encode section or
importance.

**Story card contents:**

1. Section or category label
2. Headline — 2–3 lines maximum
3. Image (or a colour block, per the above)
4. Deck — optional, feature items only
5. Byline and date
6. Read time — genuinely useful; it sets expectations

**Hierarchy must be visible.** If every story is the same size, the reader gets no editorial
guidance and the index becomes a wall. Vary scale deliberately.

## 5. Colour

| Approach | Notes |
|---|---|
| Neutral reading surface + accent for chrome | Safest and most common |
| Section-coded colour | Each section gets a hue — maps colour to structure, which the corpus supports |
| Full-bleed colour tiles | Story tiles as saturated panels; strong personality |
| Monochrome + one accent | Classic newspaper register |

Requirements:

- **The reading surface stays calm.** Colour lives in chrome, labels, and tiles, not behind body
  text.
- Link colour must be distinguishable from body text by more than colour — underline, or a
  significant weight difference.
- Section colours must be distinguishable from semantic colours, and must not be the only
  indicator of section.
- On tinted canvases, keep ink temperature consistent with the canvas.

## 6. Images and media

| Element | Requirement |
|---|---|
| Aspect ratio | Consistent per role — leads one ratio, inline another |
| Captions | Below the image, `caption` size, distinct from body |
| Credits | Present; may be combined with the caption |
| Full-bleed | May exceed the measure; captions align to the measure |
| Galleries | Keyboard-navigable, with position indication |
| Video | Poster frame, no autoplay with sound, visible controls |
| Embeds | Constrained to the measure or full-bleed; never a width between the two |
| Lazy loading | With reserved space, so text does not reflow as images arrive |

**Reserve image space.** Layout shift as images load is the most disruptive thing that happens
on a reading surface, and it is entirely preventable with intrinsic dimensions.

## 7. Navigation

- Top bar with section navigation; 5–8 sections maximum before grouping.
- Search matters — archives are large.
- Section landing pages, not only a global feed.
- Author pages linked from bylines.
- Tag or topic navigation for lateral discovery.
- Breadcrumb or section label on every article so the reader knows where they are.

**Do not put a large sticky header on a reading surface.** Every sticky pixel is a permanently
lost line of text. If sticky is needed, keep it under 48px and consider hiding it on scroll-down.

## 8. Monetisation and subscription surfaces

Synthesized. The design tension here is real and worth naming.

| Element | Requirement |
|---|---|
| Metered paywall | State the count clearly and early: "2 of 3 free articles this month" |
| Hard paywall | Show enough to establish value; do not fake a full article |
| Subscription prompt | One per article maximum; dismissible; must not obscure content |
| Newsletter signup | Inline between sections, or at the article end — not a modal on arrival |
| Advertising | Reserve space to prevent shift; never between paragraphs; never obscuring text |
| Sponsored content | Labelled unambiguously, visually distinct from editorial |

**A modal on arrival, before the reader has seen anything, is the most reliable way to lose
them.** Let them read first.

**Cumulative interruption is the real problem.** One newsletter prompt, one subscription banner,
one ad, and one cookie notice individually seem reasonable; together they make the article
unreadable. Budget interruptions as a total, not individually.

## 9. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Measure | Full width − 32px | 640px | 680–720px |
| Body size | 17–18px | 18px | 18–19px |
| Headline | 28–32px | 36px | 40–56px |
| Index grid | 1-up list | 2-up | Hierarchical multi-column |
| Nav | Drawer | Condensed | Full |
| Sticky chrome | Minimal or none | Minimal | Minimal |
| Full-bleed images | Edge to edge | Edge to edge | Edge to edge |
| Pull quotes | Inline, not offset | Offset | Offset |
| Sidebar / related | Below content | Below | Beside or below |

**Mobile is the dominant reading device for this category.** Design the mobile article first —
measure, body size, leading, and interruption budget all matter more there.

Note the body size *rises* rather than falls on mobile relative to a 16px baseline: reading on a
phone at arm's length needs the size.

## 10. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- Reading order matches visual order — critical with multi-column and offset elements.
- 200% zoom must reflow without horizontal page scroll.
- Links distinguishable from body text without colour — underline or weight.
- Images have meaningful `alt`; decorative images `alt=""`; captions are not a substitute for
  `alt`.
- Heading structure reflects article structure; one `h1`.
- Pull quotes must not be duplicated in the accessibility tree if they repeat body text.
- Video has captions; audio has transcripts.
- Paywall and subscription prompts are keyboard-dismissible and do not trap focus.
- Reading-progress indicators are decorative — do not announce them.
- Line length and leading are themselves accessibility features: WCAG recommends ≤80
  characters and ≥1.5 line-height for body text.

## 11. Do

- Hold the measure at 60–70 characters
- Run body text at 18–19px with 1.6–1.75 line-height
- Let display type carry brand voice on index and opener surfaces
- Vary story scale to communicate editorial hierarchy
- Reserve space for images so text does not reflow
- Keep the reading surface calm; put colour in chrome and tiles
- Underline links, or distinguish them by more than colour
- Show read time
- Label sponsored content unambiguously
- Budget interruptions as a cumulative total
- Design the mobile article first

## 12. Do not

- Do not let body text run the full container width
- Do not use a large sticky header on a reading surface
- Do not insert content mid-paragraph
- Do not show a subscription modal before the reader has read anything
- Do not justify body text on the web
- Do not use both paragraph spacing and first-line indents
- Do not give every index story equal weight
- Do not let images load without reserved space
- Do not place advertising between paragraphs
- Do not rely on colour alone to mark links
- Do not use an unusual display face for body text

## 13. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/wired/DESIGN.md` § *Typography*, § *Layout* | A real editorial product: humanist serif body face for long-form reading, tall narrow custom display serif for headlines, magazine-density layout with very little marketing chrome. A radius scale of only 0px and 9999px — an editorial position, not missing data |
| `design-md/theverge/DESIGN.md` § *Visual Theme*, § *Component Stylings* | Saturated full-bleed colour story tiles arranged into a timeline; a paired accent duo behaving as signal rather than brand decoration; display type to 107px. Colour at panel scale encoding section and importance |
| `design-md/pinterest/DESIGN.md` § *Layout* | Column-based masonry for mixed-aspect visual content, with a soft warm chrome that recedes behind imagery |
| `design-md/apple/DESIGN.md` § *Layout* | Narrow content width, alternating full-bleed bands, chrome that recedes — editorial technique applied to a commercial surface |
| `design-md/elevenlabs/DESIGN.md` § *Typography* | Display weight 300 with atmospheric rather than chromatic brand voltage — an editorial-print register in a technology brand |
| `design-md/claude/DESIGN.md` § *Typography* | Serif display paired with a humanist sans body on a tinted cream canvas — a warm editorial type voice with a clear display/body division of labour |
| `design-md/sanity/DESIGN.md` § *Typography* | 112px display with monospaced technical eyebrows; one accent reserved for the highest-priority action only |

## 14. Common mistakes

| Mistake | Correction |
|---|---|
| Full-width body text | 640–720px measure |
| 16px body on long-form | 18–19px with 1.6+ leading |
| Large sticky header | ≤48px, or hide on scroll |
| Uniform index grid | Vary scale for hierarchy |
| Modal before first read | Let them read |
| Cumulative interruption overload | Budget total interruptions |
| Layout shift from images | Reserve space with intrinsic dimensions |
| Colour-only links | Underline or weight |
| Display face used for body | Display for headlines only |
| Sponsored content indistinguishable from editorial | Unambiguous labelling |

## 15. Template

Use [templates/DESIGN.general-website.md](../templates/DESIGN.general-website.md) as the base
and apply this guide's typography and layout sections — the two share structure, and editorial
differs primarily in type scale, measure, leading, and interruption policy.
