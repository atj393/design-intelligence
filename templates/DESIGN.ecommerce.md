---
# E-commerce / transactional DESIGN.md
# Copy to project root as DESIGN.md. Resolve every [[SET]] and [[CHOOSE]].
# Extends DESIGN.foundation.md. Guide: categories/ecommerce.md
#   Discovery and PDP guidance is corpus-backed. CHECKOUT IS SYNTHESIZED — and checkout is
#   where the money is lost. Test it with real users.

version: 1
name: [[SET: brand]]-design-system
category: ecommerce
mode: [[CHOOSE: light | dark | dual-track (expressive marketing / plain transactional) ]]
description: >
  [[SET: What is sold, to whom, and whether the purchase is considered or impulsive. Note the
  two registers this system must carry: merchandising creates desire; transactional surfaces
  complete the purchase without error. They are deliberately different.]]

primitives:
  neutral: { 50: "[[SET]]", 100: "[[SET]]", 200: "[[SET]]", 300: "[[SET]]", 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]", 800: "[[SET]]", 900: "[[SET]]", 950: "[[SET]]" }
  accent: { 400: "[[SET]]", 500: "[[SET]]", 600: "[[SET]]", 700: "[[SET]]" }
  status: { success: "[[SET]]", warning: "[[SET]]", danger: "[[SET]]", info: "[[SET]]" }
  commerce:
    sale: "[[SET: semantic discount colour — reserved for pricing signal, never decoration]]"
    in-stock: "[[SET]]"
    low-stock: "[[SET]]"
    out-of-stock: "[[SET]]"

semantic:
  light:
    surface-canvas: "#ffffff"
    surface-raised: "{primitives.neutral.50}"
    surface-band: "{primitives.neutral.100}"
    surface-checkout: "#ffffff"          # plain. No decoration.
    surface-overlay: "#ffffff"
    text-primary: "{primitives.neutral.900}"
    text-secondary: "{primitives.neutral.600}"
    text-tertiary: "{primitives.neutral.500}"
    text-price: "{primitives.neutral.900}"
    text-price-sale: "{primitives.commerce.sale}"
    text-price-was: "{primitives.neutral.500}"
    border-subtle: "{primitives.neutral.200}"
    border-default: "{primitives.neutral.300}"
    action-primary: "{primitives.accent.600}"
    action-hover: "{primitives.accent.700}"
    focus-ring: "{primitives.accent.500}"
    scrim: "rgba(0,0,0,0.40)"
  dark:
    surface-canvas: "{primitives.neutral.950}"
    surface-raised: "{primitives.neutral.900}"
    surface-band: "{primitives.neutral.900}"
    surface-checkout: "{primitives.neutral.950}"
    surface-overlay: "{primitives.neutral.800}"
    text-primary: "[[SET: not #ffffff]]"
    text-secondary: "{primitives.neutral.400}"
    text-tertiary: "{primitives.neutral.500}"
    text-price: "[[SET]]"
    text-price-sale: "[[SET: lightened]]"
    text-price-was: "{primitives.neutral.500}"
    border-subtle: "rgba(255,255,255,0.08)"
    border-default: "rgba(255,255,255,0.14)"
    action-primary: "{primitives.accent.500}"
    action-hover: "{primitives.accent.400}"
    focus-ring: "{primitives.accent.400}"
    scrim: "rgba(0,0,0,0.60)"

typography:
  families: { display: "[[SET]]", body: "[[SET]]" }
  substitutes: { display: "[[SET: if proprietary]]", body: "[[SET]]" }
  scale:
    display-1:    { size: 48px, weight: "[[SET]]", lineHeight: 1.05, tracking: -1.2px }  # campaign only
    display-2:    { size: 36px, weight: "[[SET]]", lineHeight: 1.10, tracking: -0.8px }
    product-name: { size: 30px, weight: 600, lineHeight: 1.20, tracking: -0.4px }        # PDP
    heading-2:    { size: 22px, weight: 600, lineHeight: 1.30, tracking: -0.2px }
    heading-3:    { size: 17px, weight: 600, lineHeight: 1.40, tracking: 0 }
    body:         { size: 16px, weight: 400, lineHeight: 1.55, tracking: 0 }
    body-sm:      { size: 14px, weight: 400, lineHeight: 1.45, tracking: 0 }
    caption:      { size: 13px, weight: 400, lineHeight: 1.40, tracking: 0 }
    overline:     { size: 12px, weight: 600, lineHeight: 1.30, tracking: 0.7px, transform: uppercase }
    label:        { size: 15px, weight: 500, lineHeight: 1.20, tracking: 0 }
    price-lg:     { size: 30px, weight: 600, lineHeight: 1.10, tracking: -0.4px, features: "tabular-nums" }
    price:        { size: 18px, weight: 600, lineHeight: 1.30, tracking: 0, features: "tabular-nums" }
    price-sm:     { size: 15px, weight: 500, lineHeight: 1.30, tracking: 0, features: "tabular-nums" }
    price-was:    { size: 15px, weight: 400, lineHeight: 1.30, tracking: 0, features: "tabular-nums", decoration: line-through }

spacing:
  base: 4px
  scale: { 1: 4px, 2: 8px, 3: 12px, 4: 16px, 6: 24px, 8: 32px, 12: 48px, 16: 64px }
  section: { merchandising: 64px, transactional: 24px }
  page-padding: { mobile: 16px, tablet: 24px, desktop: 32px }

radius:
  character: "[[CHOOSE: squared | default | soft]]"
  none: 0
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px

layout:
  merchandising: { container: 1280px, prose: 680px, density: default }
  pdp:           { container: 1280px, gallery-ratio: "[[CHOOSE: 1:1 | 4:5 | 3:4]]", detail-column: 480px }
  checkout:      { container: 720px, summary-sidebar: 360px, density: dense-but-comfortable }
  grid: { desktop: 4, tablet: 3, mobile: 2, gap: 24px }
  breakpoints: { sm: 480px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1440px }

elevation: { 0: "none", 1: "1px solid {semantic.border-subtle}", 2: "0 2px 8px rgba(0,0,0,0.06)", 3: "0 4px 12px rgba(0,0,0,0.10)", 4: "0 12px 32px rgba(0,0,0,0.14)", strategy: "[[CHOOSE: border-first | shadow-first]]" }

motion: { fast: 150ms, base: 200ms, reduced-motion: "instant, state preserved" }

components:
  product-card:    { padding: 0, radius: lg, image-ratio: "{layout.pdp.gallery-ratio}", name-lines: 2 }
  cta-add-to-cart: { height: 48px, padding: "14px 24px", radius: md, surface: action-primary, text: "#ffffff", type: label, full-width-mobile: true }
  cta-checkout:    { height: 48px, padding: "14px 24px", radius: md, surface: action-primary, text: "#ffffff", type: label }
  variant-swatch:  { size: 36px, radius: full, label: "REQUIRED — colour alone excludes colour-blind users from choosing a colour" }
  variant-chip:    { height: 40px, padding: "10px 14px", radius: md, border: border-default, disabled-shows-reason: true }
  quantity-stepper:{ height: 40px, radius: md, numeric-entry: true }
  price-block:     { type: price-lg, includes: "current + was + saving + tax basis" }
  stock-badge:     { height: 22px, padding: "3px 8px", radius: full, type: caption, content: "icon + text + colour" }
  filter-facet:    { row-height: 36px, shows-count: true, disables-zero: true }
  filter-chip:     { height: 30px, padding: "5px 10px", radius: full, removable: true }
  basket-line:     { padding: "16px 0", border-bottom: border-subtle, includes: "image, name, variant, unit price, qty, line total, remove" }
  checkout-step:   { padding: 24px, radius: lg, border: border-subtle }
  order-summary:   { padding: 20px, radius: lg, surface: surface-raised, sticky-desktop: true }
  sticky-mobile-cta: { height: 64px, content: "price + selected variant + add to cart", safe-area-aware: true }
  trust-line:      { type: caption, content: "concrete policy text, not a padlock icon" }
---

# [[SET: Brand]] — Commerce Design System

## 1. Product context

- **What is sold:** [[SET]]
- **Purchase type:** [[CHOOSE: impulsive | considered | high-value considered | subscription]]
- **Catalogue size:** [[SET]] — above ~50 items search becomes critical
- **Variants:** [[SET: colour, size, configuration]]
- **Guest checkout:** [[CHOOSE: yes (recommended) | no — [[SET: justify]]]]
- **Traffic split:** [[SET: mobile/desktop]] — mobile is usually the majority
- **Markets / currencies:** [[SET]]

## 2. Experience principles

1. **Merchandising creates desire; checkout removes doubt.** Two registers, one system.
2. **No surprises.** Costs, availability, and delivery are stated as early as they are known.
3. **[[SET: your third, and what it rules out]]**

## 3. The two registers

| | Merchandising | Transactional |
|---|---|---|
| Surfaces | Home, category, campaign, PDP hero | Basket, checkout, account, order status |
| Register | Expressive, photographic | Plain, dense, unambiguous |
| Max display | `display-1` 48px | `heading-2` 22px |
| Section rhythm | 64px | 24px |
| Decoration | [[CHOOSE: minimal | moderate]] | **none** |
| Motion | Permitted | Minimal |

**In checkout, clarity beats brand every time.** Every decorative element there is a conversion
risk.

## 4. Colour discipline

- One brand accent for primary actions.
- **`commerce.sale` is a semantic signal** reserved for pricing. Never decoration.
- Stock states carry icon + text + colour.
- **Variant swatches require text labels.** Colour alone excludes colour-blind users from choosing
  a colour — a particularly avoidable failure.

## 5. Catalogue and discovery

- Grid: `{layout.grid}`. **Consistent image aspect ratio across the whole grid** — mixed ratios
  read as broken. Crop or letterbox to a fixed frame.
- Card contents, in priority order: image · name (2 lines max) · price · key differentiator ·
  availability (only when not in stock) · secondary action.
  **Not every attribute.** A card is a decision to click.
- Masonry only when mixed-aspect imagery *is* the value. It makes comparison harder.
- Filters: `filter-facet` with **per-facet counts**, zero facets disabled. Live result count.
  Active filters as removable chips. **Filter state in the URL.**
- Search: autocomplete with product suggestions, typo and synonym handling, interpreted query
  shown, **never a dead-end zero-results state**.

## 6. Product detail page

Order: breadcrumb · gallery · name · price · rating · variants · **CTA** · availability and
delivery · short description · specification · trust signals · reviews · related.

**Variant selection** — the most error-prone part:

- **Unavailable variants visible but disabled, with the reason.** Hiding them makes users think
  the product does not come in their size.
- Selection state distinct from hover.
- Price updates immediately and visibly when a variant changes it.
- Gallery follows the variant selection.
- Block add-to-basket until required variants are chosen — **and say what is missing.**

**Price block:** currency explicit, tabular figures, original struck through, saving stated, unit
price where relevant, tax basis stated, shipping surfaced as early as computable.

## 7. Basket

`basket-line` items with image, name, variant, unit price, quantity stepper, line total, remove.
Itemised totals: subtotal, shipping, tax, discount, total. Removal offers **undo**, not a
confirmation. Promo code present but not prominent — a large empty code field sends users off to
hunt for one. Flag stock changes that occurred while items were in the basket. Persist across
sessions for signed-in users, across reload for guests.

## 8. Checkout

**Synthesized guidance. Test with real users.**

Steps: contact · delivery · payment · review.

- **Guest checkout available.** Offer account creation *after* purchase.
- One step per screen on mobile; sections on desktop with a sticky `order-summary`.
- Progress indicator with current step and total.
- **Remove all navigation out of checkout** except a logo link and a clear exit.
- **No decoration, no promotional banners, no cross-sells that navigate away.**

Forms: correct `autocomplete` on **every** field · correct input types for mobile keyboards ·
address lookup where available · card type auto-detected · number formatted as typed ·
**never block paste** · validate on blur · error summary at top on submit with links to fields ·
minimal field count · **never lose entered data**.

Payment state: disable on submit and **prevent double submission** (a real financial bug) ·
explain processing delays · explain before any 3DS redirect and handle the return · a declined
payment **keeps the order intact** and offers another method · distinguish declined from technical
failure and **state whether the user was charged** · success page with copyable order number.

## 9. Post-purchase

Confirmation page and email restating order number, items, total, delivery estimate, next steps.
Order status with a visible state machine: confirmed → packed → shipped → delivered. Tracking link.
**Returns discoverable from the order**, not buried in a help centre.

## 10. Trust

| Signal | Placement |
|---|---|
| Returns policy | PDP + checkout |
| Delivery estimate | PDP + basket + checkout |
| Secure payment | Checkout payment step |
| Accepted methods | Checkout + footer |
| Contact route | Footer + checkout |

**Specific beats reassuring.** "Free returns within 30 days" works; a padlock icon does not.

## 11. States

All ten from the foundation, plus: out of stock · low stock · back-order · price changed in basket ·
variant unavailable · payment declined · payment technical failure · order cancelled.

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Product grid | 2-up | 3-up | 4-up |
| Filters | Drawer, explicit apply | Drawer | Sidebar, live |
| PDP gallery | Swipeable carousel | Side-by-side | Thumbnails + main |
| PDP CTA | **`sticky-mobile-cta`** | In-flow | In-flow |
| Basket | Full page | Drawer | Drawer |
| Checkout | One step per screen | One step per screen | Sections + sticky summary |
| Order summary | Collapsible at top | Collapsible | Sticky sidebar |
| Specification | Accordion | Full | Full |

**Full mobile parity required.** No capability may be desktop-only. The sticky mobile CTA shows
price and selected variant so users need not scroll back to check what they are buying.

## 13. Accessibility commitments

- [ ] Price, availability, and variant state programmatically associated with the product
- [ ] **Variant swatches have text labels**
- [ ] Basket count announced on change
- [ ] Checkout errors announced; focus moved to the summary
- [ ] Correct `autocomplete` on every field
- [ ] Galleries keyboard-navigable; `alt` describes the product, not "product image"
- [ ] Rating has a text equivalent: "4.6 out of 5, 231 reviews"
- [ ] Urgency timers and stock countdowns pausable or dismissible
- [ ] Sticky mobile bar does not obscure fields when the keyboard opens
- [ ] Contrast ≥4.5:1 body, ≥3:1 UI, both modes
- [ ] Paste permitted in card and promo fields

## 14. Do

- Switch register deliberately between merchandising and checkout
- Hold one image aspect ratio across a grid
- Show per-facet counts; disable zero facets
- Show unavailable variants disabled with a reason
- Use tabular figures for all prices
- Surface shipping and tax early
- Offer guest checkout
- Disable submit on payment; guard server-side
- Keep the order intact on decline, and say whether they were charged
- Make the mobile CTA sticky with price and variant

## 15. Do not

- Do not decorate the checkout
- Do not force account creation before purchase
- Do not hide unavailable variants
- Do not reveal shipping only at the final step
- Do not put every attribute on a card
- Do not mix image aspect ratios
- Do not leave zero-results search as a dead end
- Do not allow double payment submission
- Do not clear fields on validation error
- Do not substitute a padlock icon for a stated policy
- Do not put navigating cross-sells inside checkout
- Do not use undismissable urgency timers

## 16. Implementation notes

- **Platform:** [[SET]]
- **Payment provider:** [[SET: and how 3DS/redirect returns are handled]]
- **Address lookup:** [[SET]]
- **Image pipeline:** [[SET: how the fixed aspect ratio is enforced; intrinsic dimensions]]
- **Filter state in URL:** [[SET]]
- **Double-submission guard:** [[SET: client and server]]
- **Existing components to reuse:** [[SET]]

## 17. Agent prompt guidance

Read `COMMON-FOUNDATION.md`, then `categories/ecommerce.md`, then this file. This file wins.

**Before generating:** inspect existing product card, gallery, filter, basket, and checkout
components; the payment integration; how prices and currencies are formatted. Report findings.

**While generating:** maintain the two registers — **no decoration in checkout**. Correct
`autocomplete` everywhere. Never block paste. Guard double submission. Tabular figures on all
prices. Text labels on swatches.

**Then report:** assumptions, deviations, invented values, unresolved decisions, reused vs. created
components, and explicitly confirm: (a) guest checkout works, (b) double submission is prevented,
(c) a declined payment preserves the order, (d) no field lacks `autocomplete`.
