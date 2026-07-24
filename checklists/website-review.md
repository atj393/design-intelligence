# Website Review Checklist

Covers marketing, informational/documentation, and editorial surfaces. Run
[foundation-review.md](foundation-review.md) first.

Reference: [../categories/marketing-website.md](../categories/marketing-website.md) ·
[../categories/general-website.md](../categories/general-website.md) ·
[../categories/content-editorial.md](../categories/content-editorial.md)

Sections are marked **[M]** marketing, **[I]** informational/docs, **[E]** editorial, or **[All]**.

---

## 1. Surface identity [All]

- [ ] The surface's job is clear: persuasion, comprehension, or reading
- [ ] Type scale, section rhythm, and density match that job
- [ ] A marketing page has not inherited documentation density, or vice versa
- [ ] Documentation has not inherited marketing display sizes (ceiling 36–56px)
- [ ] Editorial body text is 18–19px with 1.6–1.75 line-height

## 2. Layout [All]

- [ ] Container matches the category (1280–1440px marketing · 1024–1280px docs · 1200–1400px editorial)
- [ ] **Prose measure 60–70 characters regardless of container width**
- [ ] Full-bleed bands contain their content to the container
- [ ] Section rhythm matches the category (80–96px M · 48–64px I · 32–48px E)
- [ ] Page padding ≥16px on mobile
- [ ] Space above a heading is ~2× the space below it

## 3. Hero [M]

- [ ] One primary CTA; secondary visually subordinate
- [ ] Height ≤85vh — the page edge is visible
- [ ] Value proposition readable without scrolling at 375px
- [ ] Text over imagery: contrast verified against the **worst-case region**, not the average
- [ ] Video muted, `playsinline`, poster frame, visible pause control
- [ ] Video disabled or paused under `prefers-reduced-motion`
- [ ] Hero display scale appears **once** on the page

## 4. Section sequence [M]

- [ ] Every section has a stated job for the reader
- [ ] No section exists without an editorial reason
- [ ] Surface polarity alternates so the reader perceives chapters
- [ ] Not eight consecutive identical card grids
- [ ] Section structure varies, not just content
- [ ] Closing CTA present

## 5. Claims and content [M]

- [ ] **Every quantitative claim states its comparison basis**
- [ ] No unsupported superlatives
- [ ] CTA text names the outcome — not "Learn more" ×12
- [ ] Link text meaningful in isolation
- [ ] Ratings shown with counts: "4.8 (2,341)"
- [ ] Metrics have timeframes
- [ ] Logo wall visually consistent (tinted or monochrome)

## 6. Pricing [M]

- [ ] 3–4 tiers
- [ ] Featured tier lifted by **surface step**, not scale change
- [ ] Currency, period, and tax basis stated
- [ ] CTA present in every tier including free and enterprise
- [ ] Billing toggle states the saving
- [ ] Tabular figures on all prices
- [ ] Comparison table below; per-tier accordion below 768px
- [ ] Pricing not hidden behind a contact form for a self-serve product

## 7. Page structure [I]

- [ ] **The answer appears near the top** — not after paragraphs of background
- [ ] Title matches what a reader would search for
- [ ] One-sentence summary present
- [ ] Examples are complete and runnable — no `"string"` placeholders, no omitted auth
- [ ] Related links at the end: 3–5, not exhaustive
- [ ] **Last-updated date on every page**
- [ ] Feedback control present

## 8. Navigation and findability [I]

- [ ] Current location visible in the sidebar at all times
- [ ] The section the reader is inside is **not** collapsed
- [ ] Sidebar scroll position persists across navigation
- [ ] Search prominent; `/` or `Cmd+K` focuses it
- [ ] Results appear as you type — no submit-and-wait
- [ ] Search results show section context, not just page titles
- [ ] Empty search results offer alternatives and a support path
- [ ] Breadcrumbs present if hierarchy is 3+ levels
- [ ] **Internal links do not open in new tabs**
- [ ] Version selector prominent; a banner shows when viewing outdated docs

## 9. Content components [I]

- [ ] Code blocks scroll horizontally, never wrap
- [ ] Copy button on every code block, with a **confirmed state**
- [ ] Syntax colours pass contrast in **both** themes — check comment colours specifically
- [ ] Language-tab selection persists **site-wide**
- [ ] **Four callout types maximum**, each with icon **and** text label
- [ ] Inline code has a surface tint
- [ ] Tables scroll in a bounded container at narrow widths
- [ ] Images have intrinsic dimensions and captions

## 10. Reading experience [E]

- [ ] Measure 640–720px
- [ ] Body 18–19px, line-height 1.6–1.75
- [ ] Serif or sans body chosen deliberately
- [ ] Paragraph spacing **or** first-line indent — not both
- [ ] Body text not justified
- [ ] Display face used for headlines only, never body
- [ ] Read time shown
- [ ] Sticky header ≤48px, or hides on scroll-down
- [ ] **No content inserted mid-paragraph**
- [ ] Index stories vary in scale to communicate hierarchy
- [ ] Full-bleed images may exceed the measure; body text never does

## 11. Interruptions [E] [M]

- [ ] **No modal before the reader has read anything**
- [ ] One subscription prompt maximum per article
- [ ] Newsletter signup inline or at the end, not a modal on arrival
- [ ] Advertising space reserved to prevent shift
- [ ] No advertising between paragraphs
- [ ] **Cumulative interruption budgeted** — count all prompts, banners, ads, and notices together
- [ ] Sponsored content unambiguously labelled and visually distinct
- [ ] Paywall count stated clearly and early

## 12. Motion [M]

- [ ] Scroll reveals fire **once per element, on first view only**
- [ ] Offsets ≤16px, durations 200–300ms
- [ ] No parallax decoupling text from background
- [ ] No entrance delay before content is readable
- [ ] Nothing loops
- [ ] `prefers-reduced-motion` removes movement, preserves all content
- [ ] Animated statistics readable in their final state without motion

## 13. Responsive [All]

- [ ] Nav collapses to a drawer below 768px; primary CTA stays visible outside it
- [ ] Card grids reflow sensibly
- [ ] Pricing becomes an accordion or stacks
- [ ] Comparison tables become per-tier accordions
- [ ] Docs sidebar and TOC collapse in the right order (TOC first)
- [ ] **The prose measure is never collapsed below its minimum** — narrow to viewport minus padding
- [ ] Code blocks scroll with copy buttons reachable
- [ ] Footer collapses to accordion or fewer columns
- [ ] **Hero tested at 375px first** [M]
- [ ] Article tested at 375px with real content [E]

## 14. Layout stability [All]

- [ ] Images have intrinsic dimensions
- [ ] Space reserved for ads and embeds
- [ ] Font loading does not shift text
- [ ] Nothing jumps on a slow-network reload

## 15. Accessibility [All]

- [ ] One `h1`; heading structure reflects content structure; no skipped levels
- [ ] Skip-to-content link, visible on focus
- [ ] Links distinguishable from body text by **more than colour**
- [ ] Link purpose clear from the link text alone
- [ ] Contrast met over imagery and gradients, at worst case
- [ ] Meaningful `alt`; `alt=""` on decorative images; captions are not a substitute for `alt`
- [ ] Video captioned; audio transcribed
- [ ] Callouts carry text labels, not only colour and icon [I]
- [ ] Tables use `<th scope>`; complex tables captioned
- [ ] 200% zoom reflows without page-level horizontal scroll
- [ ] Paywall and subscription prompts keyboard-dismissible; no focus trap [E]
- [ ] Reading order matches visual order [E]
- [ ] Forms: visible labels, associated errors, correct `autocomplete`

## 16. The category test

- [ ] **[M]** If success is measured in conversion, does every section move the reader toward one
      action?
- [ ] **[I]** If success is measured in time-to-answer, can a reader find the answer without
      scrolling past background?
- [ ] **[E]** If success is measured in articles finished, is anything on the page competing with
      the text?
