# Source Inventory

All 74 source design systems, inventoried by direct file inspection. Companion to
[research/CATEGORY-INVENTORY.md](research/CATEGORY-INVENTORY.md) (category rollups) and
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) (what does not match the
README).

---

## How to read this

Two separate columns describe each source, because conflating them is the most common way
to misread this corpus:

- **Surface** — what the file actually documents. For nearly every source this is a
  **public marketing / brand website**, which is where its evidence is trustworthy.
- **Domain** — what the organisation builds. This is what makes a source *relevant* to a
  product category, but it is not what the file measured.

A file whose Surface is `MKT` and whose Domain is `DASH` tells you a great deal about how
dashboard companies present themselves and almost nothing about how their dashboards work.
Treating those as the same thing would invent evidence.

**Surface codes** — `MKT` marketing/brand site · `DOCS` documentation surface ·
`TXN` transactional/checkout surface · `APP` authenticated product UI ·
`EDIT` editorial publication · `RETRO` period reconstruction

**Domain codes** — `AI` AI/LLM platform · `CHAT` conversational product · `DEV` developer
tool/infrastructure · `SAAS` productivity/business software · `DASH` analytics or
operations product · `FIN` financial/high-trust · `COM` commerce/retail ·
`AUTO` automotive · `MEDIA` media/publishing · `CONS` consumer/brand ·
`TELCO` telecom · `PLAT` multi-role platform

**Format codes** (see D4 in the discrepancy report) — `A11` 11-section YAML ·
`A10` 10-section YAML · `A8` 8-section YAML + auto-generated examples ·
`A8b` airbnb-only variant · `B9` Stitch 9-section, no frontmatter

---

## Inventory

| Source path | Surface | Domain | Fmt | Bytes | Lines | Notable for synthesis |
|---|---|---|---|---|---|---|
| `design-md/airbnb/` | MKT | COM | A8b | 31,062 | 545 | Only file with no `Do's and Don'ts`; no `Shapes` section. Modest display sizes (22–28px) against a photography-led layout — counter-example to hero-scale type |
| `design-md/airtable/` | MKT | SAAS | A11 | 35,820 | 554 | Near-black pill CTA + white outlined secondary; signature full-bleed colour cards as section punctuation |
| `design-md/apple/` | MKT | COM | A11 | 37,658 | 562 | Narrow 980px content width — the tightest container in the corpus. Alternating light/dark canvas bands. Single interactive colour |
| `design-md/binance/` | MKT+TXN | FIN | A11 | 40,552 | 634 | Documents **two themes for two purposes**: dark marketing, light transactional. Directional semantic colour (up/down) |
| `design-md/bmw-m/` | MKT | AUTO | A11 | 31,200 | 503 | Uppercase display, positive tracking, light weights. Brand-signature stripe used only as identity marker |
| `design-md/bmw/` | MKT | AUTO | A11 | 28,451 | 544 | Two-weight system (300 body / 700 display). 4-up card grid for configuration entry |
| `design-md/bugatti/` | MKT | AUTO | A11 | 28,989 | 454 | Radius scale is `0px` and `9999px` only — no mid-radius exists. Zero accent colour. Deliberate extreme |
| `design-md/cal/` | MKT | SAAS | A11 | 31,718 | 542 | Product UI fragments embedded inside cards; dark footer closing a long light page |
| `design-md/claude/` | MKT | CHAT | A11 | 34,175 | 589 | **Closest source to a conversational product.** Serif display + warm canvas; dark product surfaces for code/model mockups |
| `design-md/clay/` | MKT | SAAS | A11 | 26,246 | 541 | Saturated single-colour feature cards; 3D illustration as hero artifact |
| `design-md/clickhouse/` | MKT | DEV | A11 | 26,530 | 544 | Black canvas + one electric accent used on CTA and stat numerals. Code blocks embedded in dark cards |
| `design-md/cohere/` | MKT | AI | A11 | 20,471 | 451 | Only source whose spacing scale starts at 2px and tops at 32px + 80px section — unusually compressed ladder |
| `design-md/coinbase/` | MKT | FIN | A11 | 26,423 | 570 | Display at weight **400**, not 700 — editorial calm as a trust signal in finance |
| `design-md/composio/` | MKT | DEV | A11 | 21,112 | 506 | 2×2 terminal-pane mockup as hero anchor. Near-black floor, cards lifted on grey-tinted surfaces |
| `design-md/cursor/` | MKT | DEV | A11 | 22,308 | 537 | Warm cream canvas for a developer tool — inverts the genre default. Pastel state palette used **only** inside product timeline visualisations |
| `design-md/dell-1996/` | RETRO | COM | A8 | 35,224 | 632 | Period reconstruction. Full 12-step spacing ladder topping out at 48px — compression as a period trait. Contains auto-generated example block |
| `design-md/elevenlabs/` | MKT | AI | A11 | 21,447 | 504 | Display weight 300. Brand voltage is atmospheric/photographic rather than chromatic |
| `design-md/expo/` | MKT | DEV | A11 | 22,186 | 526 | Pure-black CTA with a separate small blue reserved for inline links — action colour and link colour deliberately separated |
| `design-md/ferrari/` | MKT | AUTO | A11 | 24,896 | 531 | Explicit 8px ladder from 4px to 128px. Near-black canvas with white bands only for pricing/listing content |
| `design-md/figma/` | MKT | SAAS | A11 | 32,894 | 578 | Variable-font weights at non-standard values (320–540). Monochrome frame interrupted by saturated full-panel colour |
| `design-md/framer/` | MKT | SAAS | A11 | 29,663 | 544 | Largest display in corpus at 110px with −5.5px tracking and 0.85 line-height. Blue reserved for links/selection, not CTAs |
| `design-md/hashicorp/` | MKT | DEV | A11 | 28,598 | 575 | **Per-product accent colours as identity tokens** — the corpus's clearest multi-product colour model |
| `design-md/hp/` | MKT | COM | A10 | 37,005 | 670 | Single "signal" CTA colour on white paper. Radius ladder concentrated at 2–8px |
| `design-md/ibm/` | MKT | SAAS | A11 | 27,031 | 550 | Only source explicitly tied to a **published public design system** (Carbon). 0–4px corners; display at weight 300 |
| `design-md/intercom/` | MKT | SAAS | A11 | 23,824 | 546 | Accent colour scoped to the AI sub-brand only — a useful pattern for AI features inside a larger product |
| `design-md/kraken/` | MKT | FIN | B9 | 4,475 | 125 | **Thinnest file in corpus** (~1/10 median). Structural group of one. Weak comparative value |
| `design-md/lamborghini/` | MKT | AUTO | B9 | 21,407 | 288 | True `#000000` canvas + single gold accent. Full-viewport video hero |
| `design-md/linear.app/` | MKT | SAAS | A11 | 24,902 | 548 | **Four-step surface ladder carrying hierarchy with no shadows** — the corpus's best dark-elevation model. Deepest canvas (`#010102`) |
| `design-md/lovable/` | MKT | DEV | B9 | 17,682 | 298 | Warm parchment canvas as an explicit rejection of cold-white developer convention |
| `design-md/mastercard/` | MKT | FIN | B9 | 27,360 | 365 | Oversized radius as the dominant gesture (40px heroes, pill cards, circular crops). High-trust brand at maximum softness — refutes "finance must be square" |
| `design-md/meta/` | MKT+TXN | COM | A11 | 38,669 | 683 | Documents **PDP and buy-now configurator** surfaces. 14-step spacing ladder to 120px hero |
| `design-md/minimax/` | MKT+DOCS | AI | A11 | 38,666 | 746 | 3-column documentation layout (sidebar / prose / TOC) alongside marketing |
| `design-md/mintlify/` | MKT+DOCS | DEV | A11 | 44,935 | 852 | **Largest file.** Dual-mode: atmospheric marketing hero vs. dense docs surface. Strongest docs-layout evidence |
| `design-md/miro/` | MKT | SAAS | A11 | 37,367 | 825 | Pricing comparison table + feature tints echoing in-product object colours |
| `design-md/mistral.ai/` | MKT | AI | A11 | 36,281 | 773 | Signature gradient band as a page-closing device |
| `design-md/mongodb/` | MKT+DOCS | DEV | A11 | 32,844 | 767 | Dark hero / white docs polarity split; 3-tier pricing; course-catalogue card grids with category tags |
| `design-md/nike/` | MKT+TXN | COM | A11 | 37,272 | 575 | **Best commerce-chrome evidence.** Extreme contrast between campaign display type and dense neutral retail chrome. Semantic sale-red |
| `design-md/nintendo-2001/` | RETRO | CONS | A8 | 39,626 | 649 | Period reconstruction: skeuomorphic bevelled panels. Contains auto-generated example block |
| `design-md/notion/` | MKT | SAAS | A11 | 35,997 | 821 | 4-tier pricing comparison; live workspace mockup inside hero; pastel feature cards echoing product data colours |
| `design-md/nvidia/` | MKT | DEV | A11 | 36,231 | 640 | Two-mode canvas (black chapters / white body) with one saturated accent. 2px radius everywhere; dense multi-column technical content |
| `design-md/ollama/` | MKT+DOCS | DEV | A11 | 33,286 | 539 | **Minimal extreme**: home page as a rendered README. 720/960px content widths — narrow by corpus standards |
| `design-md/opencode.ai/` | MKT | DEV | A11 | 33,168 | 521 | **Entirely monospaced page.** Radius scale is `0px` and `4px` only. Documented as an exception, not a pattern |
| `design-md/pinterest/` | MKT | MEDIA | A11 | 36,989 | 597 | **Masonry grid evidence** — column-based tiling for mixed-aspect content. Sticky primary CTA |
| `design-md/playstation/` | MKT | CONS | A11 | 40,427 | 661 | Three-surface chapter system (black / white / brand-blue). Display weight 300 for a gaming brand |
| `design-md/posthog/` | MKT | DASH | A11 | 41,188 | 690 | Analytics company, marketing surface only — gaps section states the product interface is not captured. Illustration-led warmth against genre convention |
| `design-md/raycast/` | MKT | DEV | A11 | 41,944 | 669 | **Marketing chrome deliberately mirroring in-product chrome** (command-palette-style cards, hairline borders). Dark-only |
| `design-md/renault/` | MKT | AUTO | A11 | 30,665 | 589 | Configurator surface documented. Near-zero radius; `button-primary-pressed` is the only pressed state promoted to tokens |
| `design-md/replicate/` | MKT | DEV | A11 | 32,111 | 616 | 128px display. Monospace code wells; cream/bone surfaces for an ML tool |
| `design-md/resend/` | MKT | DEV | A11 | 32,046 | 585 | Serif display in a developer brand. Translucent-white hairlines + low-opacity glows on near-black |
| `design-md/revolut/` | MKT | FIN | A11 | 32,670 | 636 | 136px display — largest single value in corpus. Wide product-colour accent palette scoped to illustration, not chrome |
| `design-md/runwayml/` | MKT | MEDIA | B9 | 14,597 | 244 | Full-bleed video/photography as primary UI. Single-typeface system |
| `design-md/sanity/` | MKT | DEV | B9 | 21,588 | 357 | Dark-first content platform; 112px display with mono technical eyebrows; one accent reserved for the top-priority CTA |
| `design-md/sentry/` | MKT | DEV | A10 | 35,995 | 551 | Dark-on-light polarity flip for pricing surfaces; mascot illustration as brand voice in a monitoring tool |
| `design-md/shopify/` | MKT+TXN | COM | A10 | 27,583 | 516 | **Two explicit tracks**: dark cinematic marketing vs. light transactional (pricing/signup/dashboard). Shared type DNA, opposite canvas polarity |
| `design-md/slack/` | MKT | SAAS | A10 | 25,011 | 482 | **Not listed in the root README; no stub README** (see D2/D3). Product mockups inside pastel mesh composites |
| `design-md/spacex/` | MKT | CONS | A10 | 20,042 | 363 | Austerity extreme: one ghost outlined button per band. Positive tracking, uppercase, tight leading |
| `design-md/spotify/` | **APP** | CONS | B9 | 13,201 | 246 | **Rare: documents an actual authenticated product UI.** Charcoal surface ladder (`#121212`/`#181818`/`#1f1f1f`) with content art supplying all colour |
| `design-md/starbucks/` | MKT+TXN | COM | B9 | 37,909 | 580 | Four calibrated brand-colour shades each mapped to a distinct surface role — best evidence for tiered single-hue systems |
| `design-md/stripe/` | MKT | FIN | A10 | 25,093 | 487 | Display at weight 300 with negative tracking; **tabular figures where numerics matter**; notes a dashboard track flipping polarity |
| `design-md/supabase/` | MKT | DEV | A10 | 21,777 | 462 | Near-monochrome with a single accent as "the only chromatic event"; dense product mockups above the fold |
| `design-md/superhuman/` | MKT | SAAS | A10 | 22,325 | 448 | Variable weights 460–540. Dark editorial hero → quiet white body → dark closing band |
| `design-md/tesla/` | MKT | AUTO | B9 | 22,498 | 286 | **Documents a persistent chat bar component** — the corpus's only observed always-available assistant entry point. Radical subtraction elsewhere |
| `design-md/theverge/` | **EDIT** | MEDIA | B9 | 28,707 | 339 | **Real editorial product surface.** Saturated full-bleed story tiles; hazard-tape accent pair; display type to 107px |
| `design-md/together.ai/` | MKT | AI | A8 | 38,976 | 633 | Alternating dark hero / white content bands; uppercase mono eyebrows. Auto-generated example block |
| `design-md/uber/` | MKT | PLAT | A8 | 35,396 | 636 | **Multi-audience platform** (riders / drivers / business) on one visual system. Pill radius on every interactive element. Auto-generated example block |
| `design-md/vercel/` | MKT | DEV | A8 | 42,141 | 736 | Widest spacing ladder in corpus: 4px → 128px with a 192px section step. Auto-generated example block |
| `design-md/vodafone/` | MKT | TELCO | A8 | 28,644 | 538 | 144px display at weight 800. Brand-red chapter bands. Auto-generated example block |
| `design-md/voltagent/` | MKT | DEV | A8 | 26,436 | 521 | Code-editor mockup in hero; "documentation site dressed as marketing". Auto-generated example block |
| `design-md/warp/` | MKT | DEV | A8 | 24,964 | 526 | Tight radius ladder (1–6px) — unusually restrained geometry. Terminal mockups. Auto-generated example block |
| `design-md/webflow/` | MKT | SAAS | A8 | 28,767 | 588 | Five-stop accent system mapped to product categories. Auto-generated example block |
| `design-md/wired/` | **EDIT** | MEDIA | A8 | 24,158 | 497 | **Real editorial product surface.** Serif body face for long-form reading; magazine-density layout; minimal marketing chrome. Auto-generated example block |
| `design-md/wise/` | MKT | FIN | A8 | 25,130 | 544 | Display weight 900 at 64–126px — heaviest in corpus. Tinted (not white) canvas for a financial brand. Auto-generated example block |
| `design-md/x.ai/` | MKT | AI | A8 | 22,246 | 465 | White pill outlines on near-black; uppercase tracked mono captions. Auto-generated example block |
| `design-md/zapier/` | MKT | SAAS | A8 | 23,532 | 537 | Warm cream neutrals + coffee ink + one saturated CTA. Auto-generated example block |

---

## What every file contains

Uniform across all 74, and therefore the corpus's dependable seams:

- A **visual theme narrative** (`Overview` or `Visual Theme & Atmosphere`).
- A **named colour system with roles**, not just hex lists. 64 files express it as
  frontmatter tokens; token counts run from 23 to 60+ per system.
- A **typography hierarchy table** — `Hierarchy` appears in all 74 — usually with size,
  weight, line-height, letter-spacing, and intended use per step.
- A **spacing ladder** — `Spacing System` in 73 files.
- A **radius scale** — `Border Radius Scale` in 71 files.
- **Component specifications** with surface, text, type token, radius, and padding.
- **Guardrails** — `Do's and Don'ts` in 73 files, the single richest seam for
  [ANTI-PATTERNS.md](ANTI-PATTERNS.md).
- **Font substitution guidance** — `Note on Font Substitutes` in 59 files, which is what
  makes proprietary-typeface systems reusable at all.

## What the corpus does not contain

Stated plainly, because these gaps decide which derived guides can claim corpus backing.
Most are acknowledged by the source files themselves.

| Missing | Evidence |
|---|---|
| **Authenticated application interfaces** | Only `design-md/spotify/` documents one directly. Many gaps sections say the product UI is out of scope, e.g. `design-md/raycast/DESIGN.md`: "the in-product app surface is its own design system" |
| **Dashboards and analytics interfaces** | Zero documented. `design-md/posthog/` is an analytics company whose gaps section excludes its own product interface |
| **Conversational / chat interfaces** | Effectively absent. The strongest single match, `design-md/tesla/`, contributes one component (`Persistent Chat Bar`). `design-md/claude/` documents a chat company's marketing page, not its chat UI |
| **Maps, geospatial, 3D** | Nothing. No map controls, layers, legends, drawing tools, or 2D/3D transitions anywhere in the corpus |
| **Role-based and multi-tenant structures** | No permission models, role switching, or organisation switching. `design-md/uber/` shows multi-*audience* marketing, not multi-role application structure |
| **Data tables at working density** | `Tables` appears as a subsection in 3 files. The `ex-data-table-cell` entries in 13 files are auto-generated, not observed (see D7) |
| **Empty / loading / error states** | `empty state` appears in 1 file; 10 mention loading or skeletons. Many gaps sections list form-validation states as not captured |
| **Hover and pressed states** | Numerous files state "Hover states not documented by system policy". Pressed state is usually only `button-primary-pressed` |
| **Verified light+dark pairs** | 24 files mention modes at all. Several state a light theme does not exist for their surface |
| **Keyboard interaction** | 9 files mention keyboard or shortcuts, mostly as a product feature being marketed rather than an interaction spec |

**Consequence.** The derived layer's token, typography, spacing, elevation, and layout
guidance rests on strong corpus evidence. Its interaction-state, dashboard, conversational,
and spatial guidance is predominantly **synthesized from general interface-design
reasoning**, is labelled as such at the top of each affected guide, and carries its
reasoning inline so it can be argued with. See
[VALIDATION-REPORT.md](VALIDATION-REPORT.md).
