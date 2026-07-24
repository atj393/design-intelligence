# E-commerce and Transactional Experiences

Product discovery, comparison, and purchase: catalogues, product pages, baskets, checkout,
order history, subscription management.

> **Evidence strength: moderate.** Six sources document commerce surfaces
> (`design-md/meta/` includes a product-detail page and buy-now configurator;
> `design-md/nike/` documents retail chrome; `design-md/shopify/`, `design-md/starbucks/`,
> `design-md/apple/`, `design-md/dell-1996/` contribute discovery and merchandising
> patterns). **Checkout is entirely synthesized** — no source documents a checkout flow, and
> checkout is where the money is lost.

---

## 1. Two jobs, two registers

Commerce interfaces do two incompatible things, and the corpus shows the answer is to switch
register deliberately rather than compromise.

| | Merchandising | Transactional |
|---|---|---|
| Job | Create desire, aid comparison | Complete the purchase without error |
| Surfaces | Home, category, campaign, PDP hero | Basket, checkout, account, order status |
| Register | Expressive, photographic, editorial | Plain, dense, unambiguous |
| Type | Large display permitted | Functional, small |
| Decoration | Moderate | **None** |
| Density | Moderate | Dense |
| Colour | Brand-led | Semantic-led |
| Motion | Permitted | Minimal |

`design-md/nike/DESIGN.md` documents this split explicitly within one page: towering uppercase
campaign type sitting above a dense, neutral retail chrome of pill CTAs, grey filter pills, and
tight product cards. Two registers, one system, deliberately.

**In checkout, clarity beats brand every time.** Every decorative element in a checkout is a
risk to conversion.

## 2. Discovery and catalogue

### Product grid

| Property | Default | Compact |
|---|---|---|
| Columns (desktop) | 4 | 5–6 |
| Columns (tablet) | 3 | 4 |
| Columns (mobile) | 2 | 2 |
| Gap | 24px | 16px |
| Card padding | 0 (image-led) or 16px | 12px |
| Image aspect | Consistent across the grid — 1:1 or 4:5 | |

**Product card contents, in priority order:**

1. Image — consistent aspect ratio, consistent crop treatment
2. Name — 2 lines maximum, truncated with the full name available
3. Price — prominent; original and discounted where applicable
4. Key differentiator — colour swatches, size availability, rating
5. Availability — only when it is not "in stock"
6. Secondary action — wishlist, quick view

**Do not** put every attribute on the card. A card is a decision to click, not a specification
sheet.

**Aspect-ratio consistency matters more than the ratio you pick.** Mixed ratios make a grid
read as broken. Where source imagery varies, crop or letterbox to a fixed frame.

### Masonry for mixed-aspect content

`design-md/pinterest/DESIGN.md` documents column-based masonry for genuinely mixed-aspect
content. Use it when imagery variety *is* the value; use a uniform grid when comparison is the
value. Masonry makes comparison harder because items do not align horizontally.

### Filtering and faceting

| Requirement | Detail |
|---|---|
| Placement | Left sidebar (desktop), drawer (mobile) |
| Result count | Always: "248 products" — updates live |
| Per-facet counts | "Blue (12)" — shows what filtering will do before it happens |
| Active filters | Chips above the grid, individually removable |
| Zero results | Explain and offer to relax the narrowest filter |
| URL state | Filters in the URL — shareable and reload-safe |
| Price filter | Two inputs plus a histogram if the distribution is uneven |
| Sort | Separate from filters; relevance default |
| Apply behaviour | Live on desktop; explicit "Show 248 results" on mobile drawer |

**Per-facet counts prevent dead ends.** Showing "Blue (0)" as disabled is better than letting
the user select it and land on an empty grid.

### Search

Critical for any catalogue above ~50 items.

- Autocomplete with product suggestions, not just query completions.
- Handle typos and synonyms — search failure is a lost sale.
- Zero-results state must offer alternatives, popular items, or a category path. Never a dead
  end.
- Show the interpreted query: "Showing results for *running shoes*".
- Scope indicator when search is limited to a category.

## 3. Product detail page

Structure, in order:

| # | Element | Notes |
|---|---|---|
| 1 | Breadcrumb | Category path — supports back-navigation and SEO |
| 2 | Image gallery | Multiple views, zoom, thumbnails, consistent framing |
| 3 | Name | `heading-1` scale, 28–36px |
| 4 | Price | Prominent, tabular figures. Original + discount + saving |
| 5 | Rating summary | Score + count, linked to reviews |
| 6 | Variant selection | Colour, size — with availability per variant |
| 7 | Primary CTA | Add to basket. **Sticky on mobile** |
| 8 | Availability + delivery | Concrete: "In stock — delivered 12–14 March" |
| 9 | Short description | Scannable, 2–3 sentences |
| 10 | Specification | Table, expandable |
| 11 | Trust signals | Returns, warranty, secure payment |
| 12 | Reviews | Distribution, sorting, verified indicator |
| 13 | Related items | Complementary, not just similar |

### Variant selection

The most error-prone part of a PDP.

| Requirement | Detail |
|---|---|
| Unavailable variants | Visible but disabled, with the reason. **Do not hide them** |
| Selection state | Clear, and distinct from hover |
| Colour swatches | Actual colours + accessible text label. Never colour alone |
| Size | Include a size guide; link it adjacent to the selector |
| Price change | Update immediately and visibly when a variant changes it |
| Image change | Gallery follows the variant selection |
| Required selection | Do not allow add-to-basket until required variants are chosen — and say what is missing |

**Hiding unavailable variants makes users think the product does not come in their size.**
Showing it disabled with "Out of stock — notify me" retains the customer.

### Price presentation

| Requirement | Detail |
|---|---|
| Currency | Explicit; no ambiguous symbols in multi-currency contexts |
| Tabular figures | Always |
| Discount | Original struck through, new price prominent, saving stated |
| Unit price | Where relevant by law or comparison ("£2.40 / 100ml") |
| Tax | State whether included |
| Subscription | Full period cost, renewal date, and cancellation terms |
| Shipping | Say early, not at the final step |

**Surprise costs at the final checkout step are the single largest cause of abandonment.**
Surface shipping and tax as early as you can compute them.

## 4. Basket

| Requirement | Detail |
|---|---|
| Access | Persistent header indicator with item count |
| Form | Drawer for quick review; a full page for editing |
| Line item | Image, name, variant, unit price, quantity, line total, remove |
| Quantity | Stepper with direct numeric entry; validate against stock |
| Removal | Undo, not a confirmation dialog |
| Totals | Itemised: subtotal, shipping, tax, discount, total |
| Promo code | Present but not prominent — a large empty code field prompts users to leave and hunt for one |
| Stock change | Flag it clearly if something became unavailable while in the basket |
| Persistence | Survive sessions for signed-in users; survive reload for guests |
| Empty basket | Route back into the catalogue; show recently viewed |

## 5. Checkout

Entirely synthesized. Also the highest-stakes flow in the category.

### Structure

| Step | Content |
|---|---|
| 1 | Contact — email, and guest-or-account choice |
| 2 | Delivery — address, method, date |
| 3 | Payment — method and details |
| 4 | Review — full order, then confirm |

**Rules:**

- **Guest checkout must be available.** Forced account creation is a major abandonment cause.
  Offer account creation *after* purchase.
- One step per screen on mobile; a single page with sections is acceptable on desktop.
- Progress indicator showing current step and total.
- Order summary visible throughout — collapsed on mobile, sidebar on desktop.
- Remove all navigation that leads out of checkout except a logo link back to the store and a
  clear exit.
- **No decoration.** No hero imagery, no promotional banners, no cross-sells that navigate away.

### Forms in checkout

Every foundation form rule applies, plus:

| Requirement | Detail |
|---|---|
| Autofill | Correct `autocomplete` attributes on every field. This alone materially improves completion |
| Input types | `email`, `tel`, `numeric` — so mobile keyboards are right |
| Address lookup | Postcode or address search where available |
| Card fields | Auto-detect card type; format the number as typed; never block paste |
| Validation | On blur; inline; never clear the field |
| Error summary | At the top on submit, with links to each field |
| Field count | Ruthlessly minimal. Every field costs completion |
| Optional fields | Marked, or removed entirely |
| Save progress | Never lose entered data on error or back-navigation |

**Never block paste in card or code fields.** Users paste from password managers; blocking it
causes errors and abandonment.

### Payment state

| State | Requirement |
|---|---|
| Submitting | Disable the button, show progress, **prevent double submission** |
| Processing | Explain that it may take a moment; do not let the user navigate away silently |
| 3DS / redirect | Explain before redirecting; handle the return cleanly |
| Declined | State it plainly, keep the order intact, offer another method |
| Failed (technical) | Distinguish from declined; state whether they were charged |
| Success | Confirmation page with order number, summary, and next steps |

**Double submission is a real financial bug.** Disable on submit and guard server-side.

**A declined payment must not lose the order.** The user should be one action from retrying
with a different method.

### Post-purchase

- Confirmation page: order number (copyable), items, total, delivery estimate, next steps.
- Confirmation email restating everything.
- Order status with a visible state machine: confirmed → packed → shipped → delivered.
- Tracking link when available.
- Returns process discoverable from the order, not buried in a help centre.

## 6. Trust communication

| Signal | Placement |
|---|---|
| Returns policy | PDP and checkout |
| Delivery estimate | PDP, basket, checkout |
| Secure payment | Checkout payment step |
| Accepted methods | Checkout, and footer |
| Contact route | Footer, and checkout |
| Reviews | PDP |
| Stock accuracy | PDP and basket |

**Specific beats reassuring.** "Free returns within 30 days" works; a padlock icon with no text
does not.

## 7. Layout and typography

| Property | Merchandising | Transactional |
|---|---|---|
| Container | 1280–1440px | 1024px (checkout: 720px single-column) |
| Section rhythm | 64–80px | 24–32px |
| Max display | 40–56px | 28px |
| Body | 16px | 16px |
| Control height | 44–48px | 44px |
| Card padding | 16–24px | 16px |
| Density | default | dense but comfortable |

Checkout stays at 44px controls even though it is dense — it is frequently completed on mobile,
often in a hurry, and touch accuracy matters more there than anywhere else in the product.

## 8. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Product grid | 2-up | 3-up | 4-up |
| Filters | Drawer + explicit apply | Drawer | Sidebar, live |
| PDP gallery | Swipeable carousel | Side-by-side | Thumbnails + main |
| PDP CTA | **Sticky bottom bar** | In-flow | In-flow |
| Basket | Full page | Drawer | Drawer |
| Checkout | One step per screen | One step per screen | Sections + summary sidebar |
| Order summary | Collapsible at top | Collapsible | Sticky sidebar |
| Specification table | Accordion | Full | Full |

**Full mobile parity is required.** Mobile is a majority channel for commerce; there is no
capability that may be desktop-only.

The sticky mobile add-to-basket bar should show price and the selected variant, so the user
does not have to scroll back to check what they are buying.

## 9. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- Price, availability, and variant state programmatically associated with the product, not
  merely nearby.
- Colour swatches have text labels — colour alone excludes colour-blind users from choosing a
  colour, which is a particularly avoidable failure.
- Basket count announced on change.
- Checkout errors announced and focus moved to the summary.
- Every form field has correct `autocomplete` — this is an accessibility feature as much as a
  convenience one.
- Image galleries keyboard-navigable; `alt` text describing the product, not "product image".
- Rating summaries have a text equivalent: "4.6 out of 5, 231 reviews".
- Countdown timers and stock-urgency indicators must be pausable or dismissible.
- Sticky mobile bars must not obscure content or form fields when the keyboard opens.

## 10. Do

- Switch register deliberately between merchandising and transactional surfaces
- Keep a consistent image aspect ratio across a grid
- Show per-facet counts and a live result count
- Show unavailable variants disabled, with a reason
- Use tabular figures for all prices
- Surface shipping and tax as early as possible
- Offer guest checkout
- Set correct `autocomplete` on every checkout field
- Allow paste in card and promo fields
- Disable the submit button on payment submission
- Keep the order intact on a declined payment
- Make the PDP CTA sticky on mobile with price and variant visible
- Give colour swatches text labels

## 11. Do not

- Do not decorate the checkout
- Do not force account creation before purchase
- Do not hide unavailable variants
- Do not reveal shipping cost only at the final step
- Do not put every attribute on a product card
- Do not mix image aspect ratios in one grid
- Do not use masonry when comparison is the user's goal
- Do not leave a zero-results search as a dead end
- Do not allow double payment submission
- Do not clear form fields on validation error
- Do not use a padlock icon in place of a stated policy
- Do not put unavoidable cross-sells inside the checkout flow
- Do not use urgency timers that cannot be dismissed

## 12. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/nike/DESIGN.md` § *Typography*, § *Components* | Two registers on one page: campaign display type above dense neutral retail chrome. Semantic sale-red reserved for pricing signal, never decoration. The clearest corpus evidence for the merchandising/transactional split |
| `design-md/meta/DESIGN.md` § *Components* | Documented PDP and buy-now configurator surfaces; dual-CTA hero (solid primary + outlined secondary); a saturated colour reserved specifically for purchase actions |
| `design-md/apple/DESIGN.md` § *Layout* | Narrow content width with full-bleed alternating bands; a single interactive colour; one signature shadow reserved for product imagery |
| `design-md/shopify/DESIGN.md` § *Overview* | Explicit dual-track: dark cinematic marketing, light transactional. Shared type DNA, opposite polarity |
| `design-md/starbucks/DESIGN.md` § *Color Palette & Roles* | Four calibrated brand-green shades each mapped to a distinct surface role — differentiating surfaces without adding hues |
| `design-md/pinterest/DESIGN.md` § *Layout*, § *Components* | Column-based masonry for mixed-aspect content; a persistent sticky primary CTA |
| `design-md/airbnb/DESIGN.md` § *Layout* | Narrower content width on detail pages (≈1080px) than on browse pages (≈1280px) — the detail page optimises for a reservation decision, not for browsing |
| `design-md/dell-1996/DESIGN.md` § *Layout* | A period catalogue structure: dense, compressed spacing ladder capped at 48px. Useful as a reminder that commerce density long predates current convention |

## 13. Common mistakes

| Mistake | Correction |
|---|---|
| Decorated checkout | Strip to plain and functional |
| Forced account creation | Guest checkout; offer account after |
| Surprise shipping costs | Show early |
| Hidden out-of-stock variants | Show disabled with a reason |
| Proportional digits in prices | Tabular figures |
| Mixed grid aspect ratios | Fixed frame, crop or letterbox |
| No per-facet counts | Add counts; disable zero facets |
| Dead-end search | Alternatives and category paths |
| Missing `autocomplete` | Add to every field |
| Blocked paste in card fields | Allow paste |
| Double-submittable payment | Disable on submit; guard server-side |
| Non-sticky mobile CTA | Sticky bar with price and variant |

## 14. Template

[templates/DESIGN.ecommerce.md](../templates/DESIGN.ecommerce.md)
