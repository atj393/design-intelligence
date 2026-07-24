---
# Informational / documentation / editorial website DESIGN.md
# Copy to project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md.
# Guides: categories/general-website.md — and for publications, categories/content-editorial.md
#         (apply its typography section: body 18-19px, line-height 1.6-1.75)

version: 1
name: [[SET: product-name]]-design-system
category: "[[CHOOSE: general-website | documentation | editorial]]"
density: default
mode: [[CHOOSE: light | dark | both (developers expect both) ]]
description: >
  [[SET: What readers come here to find, and how they arrive (search, link, navigation).
  Success here is measured in comprehension, not time on page — a reader who leaves quickly
  and satisfied is a success.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { note: "[[SET]]", tip: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]" }
  # Four callout types maximum. Six types of callout means readers skip all of them.

semantic:
  light:
    surface-canvas: "#ffffff"
    surface-raised: "{primitives.neutral.50}"
    surface-sunken: "{primitives.neutral.100}"    # code blocks, inline code
    surface-sidebar: "{primitives.neutral.50}"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    text-link: "{primitives.accent.600}"
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    nav-active: "{primitives.accent.600}"
    nav-active-surface: "[[SET: accent tint ~8%]]"
    focus-ring: "{primitives.accent.500}"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-raised: "{primitives.neutral.900}"
    surface-sunken: "#000000"
    surface-sidebar: "{primitives.neutral.900}"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    text-link: "{primitives.accent.400}"
    border-subtle: "rgba(255,255,255,0.08)"
    border-default: "rgba(255,255,255,0.14)"
    nav-active: "{primitives.accent.400}"
    nav-active-surface: "[[SET: accent tint ~14%]]"
    focus-ring: "{primitives.accent.400}"

typography:
  families:
    display: "[[SET]]"
    body: "[[SET: for editorial, a serif body face is a legitimate, evidenced choice]]"
    mono: "[[SET]]"
  substitutes: { display: "[[SET: if proprietary]]", body: "[[SET]]" }
  scale:
    # Documentation ceiling. NOT marketing scale — headings here are wayfinding.
    # For editorial, raise page-title to 40px and body to 18-19px.
    page-title: { size: 36px, weight: 600, lineHeight: 1.15, tracking: -0.8px }
    h2:        { size: 28px, weight: 600, lineHeight: 1.25, tracking: -0.4px }
    h3:        { size: 22px, weight: 600, lineHeight: 1.35, tracking: -0.2px }
    h4:        { size: 18px, weight: 600, lineHeight: 1.40, tracking: 0 }
    lead:      { size: 18px, weight: 400, lineHeight: 1.60, tracking: 0 }
    body:      { size: 16px, weight: 400, lineHeight: 1.60, tracking: 0 }
    body-sm:   { size: 14px, weight: 400, lineHeight: 1.55, tracking: 0 }
    caption:   { size: 13px, weight: 400, lineHeight: 1.45, tracking: 0 }
    label:     { size: 14px, weight: 500, lineHeight: 1.20, tracking: 0 }
    code:      { size: 14px, weight: 400, lineHeight: 1.55, tracking: 0, family: mono }
    code-inline: { size: 14px, weight: 400, tracking: 0, family: mono, surface: surface-sunken }
    nav-item:  { size: 14px, weight: 400, lineHeight: 1.40, tracking: 0 }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px, 16: 64px }
  section: 48px             # tighter than marketing — this is reference material
  heading-above: 40px       # ~2x the space below, so headings group with what follows
  heading-below: 16px
  paragraph: 16px
  page-padding: { mobile: 20px, tablet: 24px, desktop: 32px }

radius: { none: 0, xs: 4px, sm: 6px, md: 8px, lg: 12px, full: 9999px }

layout:
  container: 1280px
  prose: 680px              # NON-NEGOTIABLE. 60-70 characters.
  sidebar-nav: 260px
  toc: 220px
  # Three-column: nav | prose | TOC. Collapse TOC first, then nav. NEVER the prose measure.
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation:
  0: "none"
  1: "1px solid {semantic.border-subtle}"
  2: "0 2px 8px rgba(0,0,0,0.06)"
  strategy: border-first

motion:
  fast: 150ms
  base: 200ms
  reduced-motion: "instant; state preserved"

components:
  code-block:   { surface: surface-sunken, padding: 16px, radius: md, type: code, overflow: "horizontal scroll, NEVER wrap", header: "language label + copy button with confirmation" }
  code-inline:  { surface: surface-sunken, padding: "2px 5px", radius: xs, size: 0.9em }
  callout:      { padding: 16px, radius: md, border-left: "3px solid <status colour>", icon: required, label: required }
  table:        { width: prose, row-border: border-subtle, header: surface-raised, overflow: "scroll in bounded container" }
  nav-item:     { height: 32px, padding: "6px 12px", radius: sm, type: nav-item }
  nav-item-active: { surface: nav-active-surface, text: nav-active, indicator: "3px left bar" }
  toc-item:     { height: 28px, padding: "4px 8px", type: caption }
  search-input: { height: 40px, padding: "10px 14px", radius: md, border: border-default, shortcut: "/ or Cmd+K" }
  tabs:         { height: 40px, border-bottom: border-subtle, persist-selection: "site-wide" }
  steps:        { number-size: 24px, gap: 24px }
  feedback:     { placement: "page end", type: body-sm }
  version-selector: { height: 32px, prominent: true }
---

# [[SET: Site name]] — Design System

## 1. Product context

- **What readers look for:** [[SET]]
- **How they arrive:** [[CHOOSE: mostly search | mostly internal links | mostly navigation]]
- **Content volume:** [[SET: page count]] — **above ~200, search becomes primary navigation**
- **Hierarchy depth:** [[SET: levels]] — 3+ requires breadcrumbs
- **Versioned content:** [[CHOOSE: no | yes]]
- **Multi-language examples:** [[CHOOSE: no | yes — [[SET: languages]]]]
- **Success signal:** time to answer ↓, not time on page ↑

## 2. Users

| Segment | Expertise | Arrives from | Needs |
|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET]] |

## 3. Experience principles

1. **The answer comes first.** Background before answer is this category's most common failure.
2. **The measure is fixed.** Reading width does not follow container width.
3. **[[SET: your third, and what it rules out]]**

## 4. Visual theme

- **Polarity:** [[SET]] — both modes if the audience is technical
- **Decoration budget: minimal.** The content is the product.
- **Type ceiling `{typography.page-title}`** — headings are wayfinding, not persuasion. Marketing
  display sizes are a category error here.

## 5. Colour discipline

- One accent, on links, active navigation, and focus.
- Four callout types maximum, each with a distinct icon **and** text label. Colour is never the
  only severity channel.
- Inline code gets a surface tint so it reads as a token without breaking the line.

## 6. Layout

```
[ nav 260px ] [ prose 680px ] [ TOC 220px ]
```

- Collapse order: TOC first (a convenience), then nav to a drawer.
- **Never narrow the prose column below its measure** — narrow to viewport minus padding and stop.
- Section rhythm `{spacing.section}`.
- Heading space: `{spacing.heading-above}` above, `{spacing.heading-below}` below.

## 7. Navigation and findability

- Current location visible in the sidebar at all times, via an active indicator not just colour.
- **Never collapse the section the user is inside.**
- Persist sidebar scroll position across page navigation.
- Search: `[[SET: / or Cmd+K]]`, results as you type, **section context shown per result**,
  matched term highlighted, empty results offer alternatives and a support path.
- Breadcrumbs: [[CHOOSE: yes | no]]
- Related links at page end: 3–5, not exhaustive.
- Previous/next for sequential content.
- **Never open internal links in a new tab.**

## 8. Page structure

Every page follows:

1. Title matching what the reader searched for
2. One-sentence summary
3. Prerequisites, briefly, if any
4. **The answer**
5. Detail and variations
6. Complete, runnable examples
7. Related links
8. **Last-updated date** + feedback control

## 9. Content components

- **Code blocks:** horizontal scroll (never wrap — wrapping destroys indentation semantics),
  language label, copy button with a confirmed state, syntax colours **contrast-verified in both
  themes** (comment colours are the usual failure).
- **Multi-language tabs:** selection persisted **site-wide**. A reader on Python wants Python
  everywhere, permanently.
- **Tables:** at prose width, scroll in a bounded container at narrow widths.
- **Images/diagrams:** constrained to measure, click to expand, caption below, intrinsic
  dimensions set so text does not reflow on load.
- **Version selector:** prominent, with a banner when viewing non-current documentation.

## 10. States

| State | Treatment |
|---|---|
| Search empty results | [[SET: alternatives + support path]] |
| Page not found | [[SET: search + section index, not a dead end]] |
| Loading (client-side nav) | [[SET]] |
| Outdated version | Persistent banner + link to current |
| Content gap | [[SET: "This page is in progress" beats a broken link]] |

## 11. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav sidebar | Drawer | Drawer | 260px visible |
| TOC | Accordion at top | Hidden | 220px visible |
| Prose | Full − 40px | 640px | 680px |
| Code blocks | Scroll, 13px | Scroll | Full |
| Tables | Scroll in bounded container | Scroll | Full |
| Language tabs | Select | Tabs | Tabs |
| Breadcrumbs | Truncate middle | Full | Full |
| Search | Full-width, prominent | Prominent | In nav |

Documentation is heavily read on mobile, often by someone standing in front of the problem. Test
with real content at 375px.

## 12. Accessibility commitments

- [ ] Contrast ≥4.5:1 body, ≥3:1 UI, both modes — including every syntax-highlighting token
- [ ] **Heading structure is the primary screen-reader navigation:** one `h1`, no skipped levels,
      headings that describe content
- [ ] Skip-to-content link, visible on focus
- [ ] Code blocks keyboard-reachable and scrollable; copy buttons named, success announced
- [ ] Callouts carry a text label ("Warning:"), not only colour and icon
- [ ] Tables use `<th scope>`; complex tables have captions
- [ ] 200% zoom reflows without page-level horizontal scroll
- [ ] Links distinguishable from body text by more than colour
- [ ] Language and version selectors have accessible names; changes announced
- [ ] Images have meaningful `alt`; decorative ones `alt=""`

## 13. Content guidance

- Put the answer near the top.
- Examples are complete and runnable — never `"string"` placeholders, never omitted auth headers.
- Sentence case for headings.
- **Date every page.** Stale documentation is worse than none.
- One canonical term per concept: [[SET: glossary]]
- Link the *first* occurrence of a term to its definition, not every occurrence.

## 14. Do

- Hold the prose measure at `{layout.prose}` regardless of container width
- Make heading levels distinguishable at a glance in a scroll-past
- Show current location in the sidebar always
- Persist sidebar expansion and scroll
- Persist language-tab selection site-wide
- Give every code block a copy button with confirmation
- Show last-updated on every page
- Keep body line-height at 1.6+

## 15. Do not

- Do not inherit marketing display sizes or section rhythm
- Do not let prose run the full container width
- Do not collapse the section the reader is inside
- Do not lose sidebar scroll position on navigation
- Do not require search submit-and-wait
- Do not put background before the answer
- Do not exceed four callout types
- Do not open internal links in new tabs
- Do not ship undated pages
- Do not wrap code blocks
- Do not use an unusual display face for body text

## 16. Implementation notes

- **Platform:** [[SET: static generator, docs platform, CMS]]
- **Search:** [[SET: implementation, and what it indexes]]
- **Syntax highlighting:** [[SET: library — verify every token colour]]
- **Tab-selection persistence:** [[SET: mechanism]]
- **Versioning:** [[SET: how versions are built and switched]]
- **Existing components to reuse:** [[SET]]

## 17. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/general-website.md` (plus
`categories/content-editorial.md` for publications), then this file. This file wins.

**Before generating:** inspect the existing docs shell, code-block component, callout component,
navigation, and search. Report what exists.

**While generating:** hold the prose measure; keep the display ceiling; four callout types
maximum; contrast-verify syntax colours; copy buttons with confirmation; intrinsic image
dimensions.

**Then report:** assumptions, deviations, invented values, unresolved decisions, reused vs.
created components, and confirm the prose measure and heading-level distinguishability.

**Review checklist:** `design-intelligence/checklists/website-review.md`
