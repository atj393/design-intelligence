# Prompt 05 — Build a marketing or conversion page

---

```
Build <PAGE> for <PRODUCT>.

CONTEXT
- Audience: <who, and how much they already know>
- Primary conversion action: <the one thing>
- Secondary action: <or none>
- Proof available: <customer logos, metrics, testimonials, case studies>
- Brand assets: <typeface, colours, imagery, or "none — derive from DESIGN.md">
- Existing marketing pages to match: <paths, or "this is the first">

STEP 1 — INSPECT. Report before writing code:
- The project DESIGN.md
- Existing marketing components: hero, section band, feature card, pricing card, testimonial,
  logo wall, FAQ accordion, footer, CTA band
- Whether marketing and product surfaces share one token foundation
- How imagery and video are handled (CMS, static, optimisation)
Tell me what exists so we do not build a fourth hero component.

STEP 2 — PLAN THE SECTION SEQUENCE
Before building, propose the section sequence and justify each one. Every section costs scroll
and attention. If you cannot say what a section does for the reader, cut it.
Typical shape: hero, social proof, problem/outcome, features, demonstration, testimonial,
pricing, FAQ, closing CTA. Eight well-chosen sections beat fourteen.

STEP 3 — BUILD

Layout:
- Container 1280px (1440px if the design calls for it); prose measure 680px even inside a
  full-bleed band
- Section rhythm 80px desktop, 48px mobile
- Full-bleed bands with contained content — this lets sections change polarity without
  breaking alignment
- ALTERNATE surface polarity between sections so the reader perceives chapters. A page of
  fourteen identical white card sections is undifferentiated.

Hero:
- ONE primary CTA. A secondary is permitted and must be visually subordinate.
- Value proposition readable without scrolling at 375px
- Height <=85vh so the page edge is visible
- Text over imagery: verify contrast against the LIGHTEST pixel the text can overlap, not the
  average. Use a scrim or a dedicated safe area.
- Video: muted, playsinline, poster frame, visible pause control, disabled under
  prefers-reduced-motion

Typography:
- Hero display 56-72px. ONE hero scale per page — do not repeat it in later sections.
- Negative tracking scaling with size (roughly -2% to -4% above 40px)
- Overlines take POSITIVE tracking (+0.8px), uppercase, 12px
- Body 16-18px at 1.5-1.6

Content:
- Every quantitative claim states its comparison basis, or is cut
- CTA text names the outcome: "Start free trial", never "Learn more"
- Link text meaningful in isolation
- Tabular figures on all prices and metrics

Pricing (if present):
- 3-4 tiers; featured tier lifted by SURFACE STEP, not by scale change
- Currency, period, and tax basis stated
- A CTA in every tier including free and enterprise
- Comparison table below; per-tier accordion on mobile

Motion:
- Scroll-triggered fade/rise ONCE per element on first view, 200-300ms, <=16px offset
- Nothing loops. No parallax decoupling text from background. No entrance delays before
  content is readable.
- prefers-reduced-motion removes movement and preserves all content

Responsive:
- Card grids 3-4up -> 2up at 1024 -> 1up at 768
- Nav collapses to a drawer; primary CTA stays visible outside the drawer
- Test the hero at 375px FIRST, before anything else

CONSTRAINTS
- Do not reproduce another brand's identity. Adopt structural techniques; derive your own values.
- One decorative device maximum (one gradient surface, or one illustration style, or one
  atmospheric treatment). Not several.
- Do not use marketing display scale or 96px rhythm anywhere that is a product surface.
- Do not add a section without an editorial reason.
- Reuse existing components.

REPORT
SECTION SEQUENCE - each section and what it does for the reader
REUSED / CREATED
ASSUMPTIONS / DEVIATIONS / INVENTED VALUES / UNRESOLVED
CLAIMS FLAGGED   - any claim in the copy lacking supporting evidence
VERIFIED         - contrast over imagery, 375px hero, reduced-motion behaviour
```
