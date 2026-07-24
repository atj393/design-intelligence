---
# Marketing / conversion website DESIGN.md
# Copy to project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md. Category guide: categories/marketing-website.md
#   This is the one category with STRONG corpus evidence (55 of 74 sources).

version: 1
name: [[SET: product-name]]-marketing-design-system
category: marketing-website
density: spacious
mode: [[CHOOSE: light | dark | alternating-bands | both]]
description: >
  [[SET: Who the visitor is, what they are evaluating, what one action you want, and what
  objection most often stops them. Every section below should answer to this.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", danger: "[[SET]]" }   # forms only

semantic:
  light:
    surface-canvas: "#ffffff"
    surface-band-soft: "{primitives.neutral.50}"     # alternating band
    surface-band-inverse: "{primitives.neutral.950}" # dark chapter band
    surface-raised: "#ffffff"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-on-inverse: "{primitives.neutral.50}"
    text-on-inverse-muted: "{primitives.neutral.400}"
    border-subtle: "{primitives.neutral.200}"
    action-primary: "{primitives.accent.600}"
    action-hover: "{primitives.accent.700}"
    action-on-inverse: "#ffffff"
    focus-ring: "{primitives.accent.500}"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-band-soft: "{primitives.neutral.900}"
    surface-band-inverse: "{primitives.neutral.50}"
    surface-raised: "{primitives.neutral.900}"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-on-inverse: "{primitives.neutral.900}"
    text-on-inverse-muted: "{primitives.neutral.600}"
    border-subtle: "rgba(255,255,255,0.10)"
    action-primary: "{primitives.accent.500}"
    action-hover: "{primitives.accent.400}"
    action-on-inverse: "{primitives.neutral.900}"
    focus-ring: "{primitives.accent.400}"

typography:
  families:
    display: "[[SET]]"
    body: "[[SET]]"
  substitutes: { display: "[[SET: REQUIRED if proprietary]]", body: "[[SET]]" }
  scale:
    display-1: { size: 56px, weight: "[[CHOOSE: 300 | 400 | 500 | 600 | 700]]", lineHeight: 1.05, tracking: -1.5px }
    display-2: { size: 40px, weight: "[[SET: match display-1]]", lineHeight: 1.10, tracking: -1.0px }
    display-3: { size: 32px, weight: "[[SET]]", lineHeight: 1.15, tracking: -0.6px }
    card-title: { size: 22px, weight: 500, lineHeight: 1.30, tracking: -0.2px }
    lead:      { size: 20px, weight: 400, lineHeight: 1.50, tracking: 0 }
    body:      { size: 16px, weight: 400, lineHeight: 1.60, tracking: 0 }
    body-sm:   { size: 14px, weight: 400, lineHeight: 1.50, tracking: 0 }
    caption:   { size: 13px, weight: 400, lineHeight: 1.45, tracking: 0 }
    overline:  { size: 12px, weight: 600, lineHeight: 1.30, tracking: 0.8px, transform: uppercase }
    label:     { size: 15px, weight: 500, lineHeight: 1.20, tracking: 0 }
    price:     { size: 44px, weight: 600, lineHeight: 1.05, tracking: -1.0px, features: "tabular-nums" }
    metric:    { size: 40px, weight: 600, lineHeight: 1.05, tracking: -0.8px, features: "tabular-nums" }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px, 16: 64px, 20: 80px, 24: 96px }
  section: 80px           # 96px is corpus-modal; 80px is the safer default
  section-mobile: 48px
  page-padding: { mobile: 20px, tablet: 32px, desktop: 32px }

radius:
  character: "[[CHOOSE: squared | default | soft]]"
  none: 0
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  full: 9999px

layout:
  container: 1280px
  prose: 680px            # holds even inside a full-bleed band
  hero-max-height: 85vh   # never 100vh — the page edge must be visible
  nav-height: 64px
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation:
  0: "none"
  1: "1px solid {semantic.border-subtle}"
  2: "0 2px 8px rgba(0,0,0,0.06)"
  3: "0 8px 24px rgba(0,0,0,0.10)"
  strategy: "[[CHOOSE: border-first | shadow-first]]"

motion:
  fast: 150ms
  base: 250ms
  reveal: { duration: 250ms, offset: 16px, easing: "ease-out", trigger: "first view ONLY" }
  reduced-motion: "no movement; content and state preserved"

components:
  cta-primary:   { height: 48px, padding: "14px 24px", radius: md, surface: action-primary, text: "#ffffff", type: label }
  cta-secondary: { height: 48px, padding: "14px 24px", radius: md, surface: transparent, border: border-subtle, type: label }
  nav-bar:       { height: 64px, sticky: true, border-bottom-on-scroll: border-subtle }
  feature-card:  { padding: 28px, radius: lg, border: border-subtle }
  pricing-card:  { padding: 32px, radius: lg, border: border-subtle }
  pricing-card-featured: { padding: 32px, radius: lg, surface: surface-band-soft, note: "lifted by SURFACE, not by scale" }
  testimonial:   { padding: 32px, radius: lg, quote-type: lead }
  logo-tile:     { padding: 16px, treatment: "monochrome or single-tint for consistency", logo-height: 28px }
  faq-row:       { padding: "20px 0", border-bottom: border-subtle }
  cta-band:      { padding: "96px 32px", surface: surface-band-inverse }
  footer:        { padding: "64px 32px", type: caption }
  text-input:    { height: 48px, padding: "14px 16px", radius: md, border: border-subtle }
---

# [[SET: Product name]] — Marketing Design System

## 1. Product context

- **Visitor:** [[SET: who, and what they already know]]
- **What they are evaluating:** [[SET]]
- **Primary conversion action:** [[SET: exactly one]]
- **Secondary action:** [[SET: or none]]
- **Main objection to overcome:** [[SET]]
- **Proof available:** [[SET: logos, metrics, testimonials, case studies]]
- **Traffic split:** [[SET: mobile/desktop]]

## 2. Users

| Segment | Knowledge | Decision role | What convinces them |
|---|---|---|---|
| [[SET]] | [[SET]] | [[SET: evaluator / buyer / influencer]] | [[SET]] |

## 3. Experience principles

1. **Every claim is supported.** An unsupported superlative costs credibility for the claims that
   are true.
2. **One primary action per view.**
3. **[[SET: your third, and what it rules out]]**

## 4. Visual theme

- **Polarity strategy:** [[CHOOSE: light throughout | dark throughout | alternating chapter bands]]
- **What carries visual interest:** [[CHOOSE: typography | photography | product screenshots |
  illustration | colour blocking | data]]
- **Decoration budget:** [[CHOOSE: minimal | moderate | expressive]] — **one** decorative device,
  used consistently. Not several.
- **Display weight rationale:** [[SET: light reads institutional/premium; heavy reads confident/
  accessible. Both are evidenced. State which you chose and why.]]

## 5. Colour discipline

- Accent count: [[CHOOSE: 1 | 2]]. If 2, state the structural mapping: [[SET]]
- The accent carries the primary CTA, brand mark, and focus ring. Nothing decorative.
- Text over imagery: contrast verified against the **lightest region the text can overlap**, not
  the average. Use a scrim or safe area.

## 6. Layout

- Container `{layout.container}` · prose `{layout.prose}` (holds inside full-bleed bands)
- Section rhythm `{spacing.section}` desktop, `{spacing.section-mobile}` mobile
- **Full-bleed bands with contained content** — lets sections change polarity without breaking
  alignment
- **Alternate surface polarity between sections** so the reader perceives chapters

## 7. Section sequence

State each section and what it does for the reader. **Cut any section you cannot justify.**

| # | Section | Job | Surface |
|---|---|---|---|
| 1 | Hero | [[SET]] | [[SET]] |
| 2 | [[SET]] | [[SET]] | [[SET]] |
| 3 | [[SET]] | [[SET]] | [[SET]] |

Eight well-chosen sections beat fourteen.

## 8. Hero

- **Pattern:** [[CHOOSE: centred type | split type/product | full-bleed photography |
  full-bleed video | product screenshot | device mockup | illustration]]
- Height ≤ `{layout.hero-max-height}`
- Value proposition readable without scrolling at 375px
- One primary CTA; secondary visually subordinate
- Video: muted, `playsinline`, poster frame, visible pause control, disabled under reduced motion
- **One hero display scale per page** — do not repeat it in later sections

## 9. Pricing

- Tiers: [[SET: 3 or 4]]
- Featured tier lifted by **surface step**, not scale change
- Billing toggle with the saving stated explicitly
- Currency, period, and tax basis shown: [[SET]]
- A CTA in every tier including free and enterprise
- Comparison table below; per-tier accordion below 768px

## 10. Social proof

| Element | Treatment |
|---|---|
| Logo wall | Monochrome/single-tint, 28px height, [[SET]]-up desktop |
| Metrics | `metric` token, tabular figures, **timeframe stated** |
| Testimonials | Quote in `lead`, name, role, company |
| Ratings | Score **with count**: "4.8 (2,341)" |

## 11. Interaction states

All eight on every interactive element: default, hover, focus-visible, active, disabled,
loading, selected, error. Forms follow the foundation's form rules exactly.

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav | Drawer; CTA stays visible outside it | Condensed | Full bar |
| Hero display | 36px | 44px | 56px |
| Card grid | 1-up | 2-up | [[SET]]-up |
| Pricing | Accordion or stacked | 2-up | [[SET]]-up |
| Comparison table | Per-tier accordion | Scroll | Full |
| Logo wall | 3-up | 4-up | [[SET]]-up |
| Section rhythm | 48px | 64px | 80px |
| Footer | Accordion | 2-column | [[SET]]-column |

**Test the hero at 375px before anything else.**

## 13. Accessibility commitments

- [ ] Contrast ≥4.5:1 body, ≥3:1 large and UI, in both modes
- [ ] Text over imagery verified against worst-case region
- [ ] Visible focus on every interactive element
- [ ] Link text meaningful in isolation — not "Learn more" ×12
- [ ] One `h1`; heading structure matches the section sequence
- [ ] Video muted with a visible pause control; captions provided
- [ ] Animated statistics readable in final state without motion
- [ ] `prefers-reduced-motion` removes movement, preserves content
- [ ] Forms: visible labels, associated errors, correct `autocomplete`
- [ ] Logo `alt` names the company, or `alt=""` if the wall is decorative and labelled

## 14. Content guidance

- Every quantitative claim states its comparison basis
- CTA text names the outcome: [[SET: e.g. "Start free trial"]]
- Sentence case; uppercase only for `overline`
- Tabular figures on all prices and metrics
- Terminology: [[SET: the words you use, and the ones you avoid]]

## 15. Do

- Alternate polarity to mark the section sequence
- Support every claim
- Reserve hero scale for the hero
- Constrain body copy to the measure inside wide bands
- Lift the featured tier with surface
- Show currency, period, and tax basis
- Animate once per element on first view only
- Keep logo walls visually consistent by tinting

## 16. Do not

- Do not use a 100vh hero
- Do not add sections without an editorial reason
- Do not repeat hero type scale later
- Do not animate on every scroll pass
- Do not place text over imagery without verified contrast
- Do not use "Learn more" as the only link text
- Do not hide pricing for a self-serve product
- Do not use more than one decorative device
- Do not carry this file's display scale or 80px rhythm into a product surface

## 17. Implementation notes

- **Token delivery:** [[SET]]
- **CMS / content source:** [[SET]]
- **Image optimisation:** [[SET: and how intrinsic dimensions are set to prevent layout shift]]
- **Analytics events on CTAs:** [[SET]]
- **Shared with the product surface:** [[SET: which tokens; what deliberately differs]]

## 18. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/marketing-website.md`, then this file. This file
wins.

**Before generating:** inspect existing marketing components (hero, band, feature card, pricing
card, testimonial, logo wall, FAQ, footer, CTA band) and report them. Do not build a fourth hero.

**Then propose the section sequence and justify each section before writing code.**

**While generating:** semantic tokens only; one decorative device; all interaction states;
contrast verified over imagery; reduced motion honoured.

**Then report:** section sequence with justifications, components reused vs. created,
assumptions, deviations, invented values, unresolved decisions, **and any claim in the copy that
lacks supporting evidence**.

**Review checklist:** `design-intelligence/checklists/website-review.md`
