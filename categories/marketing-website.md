# Marketing and Conversion Websites

> **Evidence strength: strong / corpus-backed.**
> 55 of 74 sources document exactly this surface type. Every numeric recommendation here is
> grounded in the distributions in
> [research/VALUE-DISTRIBUTIONS.md](../research/VALUE-DISTRIBUTIONS.md). This is the one
> category where the corpus is authoritative rather than adjacent.

---

## 1. Distinguishing marketing from informational

Both are public websites. They optimise for different things, and mixing them produces pages
that persuade nobody and explain nothing.

| | Marketing website | General informational website |
|---|---|---|
| Success measured by | Conversion | Comprehension |
| User's state | Evaluating, sceptical | Looking for something specific |
| Content shape | Narrative sequence | Reference structure |
| Type scale | Large display, high contrast | Moderate, wayfinding-oriented |
| Section rhythm | 80–96px | 48–64px |
| Navigation | Few destinations, prominent CTA | Many destinations, search-forward |
| Decoration budget | Moderate to expressive | Minimal |
| Page length | Long-scroll, sectioned | As long as the content needs |

Use [general-website.md](general-website.md) for documentation, support, and reference. Most
companies need both, sharing one token foundation.

## 2. Layout

| Property | Default | Compact | Spacious |
|---|---|---|---|
| Container | 1280px | 1200px | 1440px |
| Prose measure | 680px | 640px | 720px |
| Section rhythm | 80px | 64px | 96–120px |
| Page padding (desktop) | 32px | 24px | 48px |
| Grid | 12 column, 24px gutters | | |
| Card grid gap | 24px | 16px | 32px |

Container distribution: 1280px in 27 sources, 1200px in 19, 1440px in 10. Section rhythm of
96px appears in 61 — this is the one category where that value is genuinely appropriate,
because the surface is scrolled once by each visitor.

**Full-bleed bands with contained content** is the dominant structure. The band spans the
viewport; the content inside it respects the container. This lets sections change canvas
polarity without breaking alignment — the corpus's most common page-rhythm device.

## 3. Typography

| Token | Default | Compact | Spacious |
|---|---|---|---|
| Hero display | 56px | 44px | 72–80px |
| Section display | 40px | 32px | 48px |
| Sub-section | 32px | 28px | 36px |
| Card title | 22px | 20px | 24px |
| Lead paragraph | 20px | 18px | 20px |
| Body | 16px | 16px | 18px |
| Caption | 13px | 12px | 14px |
| Overline | 12px uppercase +0.8px | | |

Corpus median for the largest display step is 64–72px, with the full range 44–144px. **Above
about 80px, display type is a brand statement rather than a communication choice** — it works
when photography or a strong identity supports it, and looks unmoored otherwise.

**Rules from the corpus:**

- Negative tracking scales with size: roughly −2% to −4% of font size above 40px.
- Overlines take positive tracking (+0.4 to +1.5px). The contrast between negatively-tracked
  display and positively-tracked overline is what marks the overline as taxonomy.
- Display weight has no convergence — 300 through 900 all appear and all work. Light reads
  premium and institutional; heavy reads confident and accessible. Choose from brand and
  audience, not from genre.
- One display size per page for the hero. Repeating hero scale in later sections destroys the
  hierarchy that makes the hero work.

## 4. Hero layouts

| Pattern | Use when | Notes |
|---|---|---|
| **Centred type** | The proposition is the message | Cheapest to execute well; needs strong copy |
| **Split (type / product)** | The product is visually explicable | Most common in the corpus for software |
| **Full-bleed photography** | Brand or emotion leads | Requires contrast management for overlaid text |
| **Full-bleed video** | Motion is intrinsic to the product | Needs a poster frame, mute default, and pause control |
| **Product screenshot** | The interface *is* the argument | Corpus-common for tools; needs real, legible UI |
| **Device mockup** | Cross-platform is the point | Risks dating quickly |
| **Illustration** | Abstract or infrastructure product | Expensive; must be consistent across the site |

**Hero requirements regardless of pattern:**

- One primary CTA. A secondary is permitted and must be visually subordinate.
- The value proposition must be readable without scrolling on a 375px screen.
- Text over imagery needs a scrim, gradient, or dedicated safe area — verify ≥4.5:1 against
  the *lightest* pixel the text can overlap, not the average.
- Hero height should not exceed ~85vh. A full 100vh hero hides the fact that the page
  continues.
- Autoplaying video: muted, `playsinline`, poster frame, pause control, and disabled under
  `prefers-reduced-motion`.

## 5. Section patterns

An effective marketing page is a sequence of sections each doing one job. Typical order:

| # | Section | Job |
|---|---|---|
| 1 | Hero | Proposition + primary CTA |
| 2 | Social proof | Reduce risk (logos, metrics) |
| 3 | Problem / outcome | Establish relevance |
| 4 | Feature groups | Explain capability, 3–6 blocks |
| 5 | Product demonstration | Make it concrete |
| 6 | Testimonial | Human evidence |
| 7 | Pricing | Enable the decision |
| 8 | FAQ | Remove remaining objections |
| 9 | Closing CTA | Convert |

**Do not include every section by default.** Each one costs scroll and attention. Eight
well-chosen sections beat fourteen. Section count with no editorial argument behind it is the
most common bloat in this category.

**Alternate surface polarity** to mark the sequence. The corpus's dominant device: alternate
canvas / raised / inverse bands so the reader perceives chapters. A page of fourteen
identical white sections with cards reads as undifferentiated.

## 6. Social proof

| Type | Treatment |
|---|---|
| Logo wall | Monochrome or single-tint for consistency; 24–32px logo height; 4–6 per row desktop |
| Metric strip | Large numeric + small label. Tabular figures. State the timeframe |
| Testimonial | Quote, name, role, company. Photo optional but increases credibility |
| Case study card | Outcome in the title, not the customer name |
| Rating / review | Show the count alongside the score — "4.8 (2,341)" |

**Every claim needs support.** "10× faster" without a comparison basis is noise that a
sceptical evaluator discounts, and it costs credibility for the claims that *are* supported.

## 7. Pricing

The highest-intent page on most marketing sites. Design it as a decision tool.

| Property | Value |
|---|---|
| Tier count | 3–4. Five or more forces comparison work onto the user |
| Layout | Equal-width columns; featured tier lifted by surface step, not by size |
| Featured marker | Surface lift + a small label. Not a scale change — that breaks the grid |
| Billing toggle | Pill segmented control; show the saving explicitly |
| Price display | Largest numeric on the page after the hero; tabular figures |
| Feature list | Grouped, consistent order across tiers, with a comparison table below |
| CTA per tier | Present in every tier, including free and enterprise |
| Currency / tax | State it. "From $29" without "per user / month, excl. VAT" invites bounce |

The corpus converges on 3–4 tiers with a lifted featured card and a comparison table below,
collapsing to a per-tier accordion on mobile.

## 8. Components

| Component | Default spec |
|---|---|
| Primary CTA | 48px height, 14px 24px padding, `radius.md`, `action-primary` |
| Secondary CTA | 48px height, bordered or ghost, subordinate |
| Nav bar | 64px, sticky, `border-subtle` bottom on scroll |
| Feature card | 24–32px padding, `radius.lg`, `border-subtle` |
| Pricing card | 32px padding, `radius.lg` |
| Testimonial card | 32px padding, `body-lg` for the quote |
| Logo tile | 16px padding, no border |
| FAQ accordion | 20px vertical padding per row, `border-subtle` between |
| Footer | 64px 32px padding, multi-column link grid |
| Closing CTA band | 96px vertical padding, `surface-inverse` |

CTAs run larger here than in applications — 48px against the foundation's 40px default. The
button is the page's purpose, and marketing surfaces are frequently touch-first.

## 9. Navigation

- **Top bar, 5–7 destinations maximum.** Beyond that, group into a mega-menu or reduce.
- Sticky is standard; add a `border-subtle` or slight surface shift on scroll so it separates
  from content.
- Primary CTA lives in the nav bar and repeats at the page bottom.
- Mobile: hamburger drawer. Keep the CTA visible outside the drawer.
- Anchor navigation for long pages is helpful; do not duplicate the top-bar destinations in
  it.

## 10. Motion

The category with the most licence to move, and the most frequent abuse.

**Acceptable:**

- Scroll-triggered fade/rise on first view, 200–300ms, subtle offset (≤16px), **once**
- Hover feedback on cards and CTAs, ≤150ms
- Product demonstration animation that shows the product working
- Marquee logo strips at slow, uninterrupted speed

**Not acceptable:**

- Every section animating in on every scroll pass
- Parallax that decouples text from its background
- Entrance delays before content is readable
- Perpetual decorative animation
- Motion that cannot be disabled

`prefers-reduced-motion` must remove movement while preserving all content and state.

## 11. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav | Hamburger drawer, CTA visible | Drawer or condensed | Full bar |
| Hero display | 44px→36px | 48px | 56–80px |
| Card grid | 1-up | 2-up | 3–4-up |
| Pricing | Accordion or stacked cards | 2-up | 3–4-up |
| Comparison table | Per-tier accordion | Scroll | Full table |
| Logo wall | 3-up | 4-up | 6-up |
| Section rhythm | 48px | 64px | 80–96px |
| Footer | Accordion sections | 2-column | 4–5-column |

The corpus's typical collapse sequence — 3-up → 2-up at 1024px → 1-up at 768px, with the
pricing comparison becoming an accordion — is well evidenced and works.

## 12. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- Text over imagery: verify contrast against the worst-case pixel region, not the average
- Autoplay video: muted, with a visible pause control
- Link text meaningful in isolation — "Read the case study", not "Learn more" ×12
- Heading structure reflects the section sequence; one `h1`
- Logo walls: `alt` naming the company, or `alt=""` if the wall is decorative and labelled
- Animated statistics must also be readable in their final state without motion
- Forms (contact, demo, signup) follow the foundation's form rules exactly

## 13. Do

- Alternate surface polarity to mark the section sequence
- Keep one primary CTA per view and repeat it at the page end
- Support every quantitative claim
- Reserve hero-scale type for the hero
- Use tabular figures for prices and metrics
- Constrain body copy to a readable measure even inside a wide band
- Lift the featured pricing tier with surface, not with scale
- Show currency, period, and tax basis on prices
- Test the hero on a 375px screen before anything else
- Keep the logo wall visually consistent by tinting

## 14. Do not

- Do not use 100vh heroes that hide the page continuing
- Do not add sections without an editorial reason
- Do not repeat hero type scale in later sections
- Do not animate sections on every scroll pass
- Do not place text over imagery without verified contrast
- Do not use "Learn more" as the only link text
- Do not build a fourteen-section page of identical cards
- Do not hide pricing behind a contact form for self-serve products
- Do not let decoration compete with the product demonstration
- Do not inherit this category's 96px rhythm or 72px display into an application surface

## 15. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/apple/DESIGN.md` § *Layout* | Narrow 980px content width with full-bleed alternating light/dark bands. Chrome recedes so imagery carries the argument |
| `design-md/linear.app/DESIGN.md` § *Overview*, § *Components* | Product screenshots as the protagonist of every section, framed in surface panels. The marketing chrome exists to display the app |
| `design-md/stripe/DESIGN.md` § *Typography* | Light display weight with negative tracking as an editorial-density signal; tabular figures where numerics matter |
| `design-md/nike/DESIGN.md` § *Typography*, § *Components* | Extreme contrast between campaign display type and dense functional chrome — two registers on one page, deliberately |
| `design-md/notion/`, `design-md/miro/`, `design-md/mongodb/` § *Components* | 3–4 tier pricing with a comparison table below; featured tier lifted by surface |
| `design-md/hashicorp/DESIGN.md` § *Colors* | Per-product accent colours as identity tokens — the model for multi-product marketing without colour chaos |
| `design-md/playstation/DESIGN.md` § *Layout* | Three-surface chapter system where each section owns one canvas mode and one editorial purpose |
| `design-md/vercel/DESIGN.md` § *Layout* | The corpus's widest spacing ladder (4→128px with a 192px section step) — evidence that generous rhythm is a deliberate, tuned choice |

## 16. Common mistakes

| Mistake | Correction |
|---|---|
| Section count without editorial argument | Cut to the sequence that actually persuades |
| Unsupported superlatives | Add the comparison basis or delete the claim |
| Hero type repeated throughout | One hero scale per page |
| Undifferentiated white card sections | Alternate polarity; vary section structure |
| Motion on every scroll | Once per element, on first view only |
| Text on imagery failing contrast | Scrim, safe area, or move the text |
| Pricing hidden for a self-serve product | Show it; hiding it filters out buyers, not just tyre-kickers |
| Marketing scale reused in the product | Application surfaces cap display at 24–32px |

## 17. Review checklist

[checklists/website-review.md](../checklists/website-review.md)

## 18. Template

[templates/DESIGN.marketing-website.md](../templates/DESIGN.marketing-website.md)
