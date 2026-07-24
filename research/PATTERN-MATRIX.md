# Normalized Pattern Matrix

The extraction model applied to the corpus, plus the vocabulary mapping used to make 74
differently-named systems comparable. Numeric distributions live in
[VALUE-DISTRIBUTIONS.md](VALUE-DISTRIBUTIONS.md); co-occurrence analysis lives in
[PATTERN-CLUSTERS.md](PATTERN-CLUSTERS.md).

---

## 1. Vocabulary normalization

The corpus has no enforced token vocabulary (discrepancy D10). Every extracted value was
mapped onto these canonical names, which are also the names
[../COMMON-FOUNDATION.md](../COMMON-FOUNDATION.md) publishes.

### Colour

| Canonical | Observed source names |
|---|---|
| `surface/canvas` | `canvas`, `canvas-soft`, `canvas-light`, `canvas-dark`, `canvas-cream`, `canvas-night`, `bg`, `base`, `surface` |
| `surface/raised` | `surface-soft`, `surface-1`, `surface-elevated`, `surface-card`, `canvas-soft`, `stone`, `ash` |
| `surface/sunken` | `surface-strong`, `surface-deep`, `surface-2` |
| `surface/inverse` | `surface-dark`, `inverse-canvas`, `canvas-dark`, `charcoal` |
| `text/primary` | `ink`, `ink-deep`, `ink-strong`, `body-strong`, `text` |
| `text/secondary` | `body`, `ink-muted`, `ink-soft`, `muted`, `mute` |
| `text/tertiary` | `ink-subtle`, `ink-tertiary`, `muted-soft`, `ink-mute` |
| `text/on-accent` | `on-primary` |
| `text/on-inverse` | `on-dark`, `on-dark-soft`, `on-dark-muted`, `on-dark-mute`, `inverse-ink` |
| `border/subtle` | `hairline`, `hairline-soft`, `divider-soft`, `hairline-light` |
| `border/strong` | `hairline-strong`, `border-strong`, `hairline-tertiary` |
| `action/primary` | `primary` |
| `action/primary-hover` | `primary-hover`, `primary-soft` |
| `action/primary-active` | `primary-active`, `primary-pressed`, `primary-deep`, `primary-focus` |
| `action/disabled` | `primary-disabled` |
| `status/success` | `success`, `semantic-success`, `brand-green` (where semantic) |
| `status/warning` | `warning`, `semantic-warning` |
| `status/danger` | `error`, `semantic-error`, `error-deep` |
| `status/info` | `info`, `accent-blue`, `link-blue` |
| `focus/ring` | `primary-focus`, `ring-focus`, `hairline-strong` (where used for focus) |

### Typography

| Canonical | Observed source names |
|---|---|
| `display-1` | `display-xl`, `display-xxl`, `display-mega`, `hero-display`, `display-hero`, `display-campaign` |
| `display-2` | `display-lg`, `display-xl` (in shorter ladders), `product-display` |
| `display-3` | `display-md`, `heading-1`, `section-display` |
| `heading-1` | `heading-lg`, `heading-xl`, `display-sm`, `headline`, `section-heading` |
| `heading-2` | `heading-md`, `title-lg`, `card-heading` |
| `heading-3` | `heading-sm`, `title-md`, `card-title`, `feature-heading` |
| `subtitle` | `subhead`, `subtitle`, `subtitle-lg`, `lead`, `tagline` |
| `body-lg` | `body-lg`, `body-large`, `body-serif-lg` |
| `body` | `body`, `body-md` |
| `body-sm` | `body-sm`, `body-xs` |
| `caption` | `caption`, `caption-md`, `caption-sm`, `micro` |
| `overline` | `eyebrow`, `overline`, `micro-cap`, `micro-uppercase`, `caption-uppercase`, `mono-caps-eyebrow`, `uppercase-tag` |
| `code` | `code`, `code-md`, `code-sm`, `code-inline`, `mono` |
| `numeric` | `number-display`, `number-md`, `stat-display`, `body-tabular`, `price-md`, `rating-display` |
| `label/button` | `button`, `button-md`, `button-lg`, `button-sm`, `button-cap` |

### Scale steps

| Canonical | Observed ladder conventions |
|---|---|
| `space-1` … `space-N` | `xxs…xxl`, `xs…3xl`/`6xl`, `xxxs…super`, `hair/xxs…hero`, `sm/md/huge`, `s/m/lg` |
| `radius-*` | `none/xs/sm/md/lg/xl/xxl/pill/full`, `circle`, `feature`, `card`, `pill-sm`, `pill-md`, `pill-tab` |
| `section` | `section`, `section-sm`, `section-lg`, `band`, `block`, `hero`, `huge`, `super` |

## 2. Extraction coverage per dimension

How much of the requested extraction model the corpus can actually answer. Coverage is the
count of files supplying an explicit value.

| Dimension | Coverage | Tag | Note |
|---|---|---|---|
| Visual theme narrative | 74 | explicit | Universal |
| Canvas/background strategy | 74 | explicit | Universal |
| Foreground/text strategy | 74 | explicit | Universal |
| Primary colour | 64 | explicit | Frontmatter files; narrative-only in the other 10 |
| Accent colours | 74 | explicit | |
| Semantic colours | ~30 | partial | `info` in only 4 files |
| Neutral scale | 74 | explicit | Depth varies 3–12 steps |
| Contrast approach | 56 | ambiguous | Asserted, never computed — see D9 |
| Light mode behaviour | ~54 | explicit | |
| Dark mode behaviour | ~44 | explicit | 24 files document both modes |
| Font families | 72 | explicit | |
| Font substitutes | 59 | explicit | Critical for proprietary faces |
| Type scale | 74 | explicit | `Hierarchy` in every file |
| Heading proportions | 74 | explicit | |
| Body sizing | 74 | explicit | |
| Line height | ~70 | explicit | |
| Letter spacing | ~70 | explicit | |
| Font weight | 74 | explicit | |
| Spacing scale | 73 | explicit | |
| Content widths | ~60 | explicit | |
| Grid systems | ~65 | explicit | Column counts per breakpoint |
| Breakpoints | 59 | explicit | |
| Page padding | ~45 | partial | Often only implied by container |
| Section spacing | 73 | explicit | |
| Component density | 74 | inferred | From padding + type, rarely stated as density |
| Button dimensions | ~55 | explicit | Height or padding, seldom both |
| Input dimensions | ~50 | partial | |
| Card padding | ~53 | explicit | |
| Border radius | 71 | explicit | |
| Border treatment | ~65 | explicit | |
| Shadows | ~40 | partial | Many systems explicitly reject shadow |
| Elevation model | 63 | explicit | |
| Navigation structure | 55 | explicit | Top nav dominant |
| Sidebars | 27 | partial | Mostly documentation sidebars |
| Headers | 55 | explicit | |
| Footers | ~50 | explicit | |
| Dialogs / modals | 13 | **auto-generated** | Only via `ex-modal-card` — see D7 |
| Menus | ~20 | partial | |
| Tables | 3 + 13 auto-generated | **weak** | |
| Forms | 61 | partial | Structure yes; validation states no |
| Empty states | 1 + 13 auto-generated | **very weak** | |
| Loading states | 10 | **very weak** | |
| Error states | ~8 | **very weak** | Repeatedly listed as a known gap |
| Responsive behaviour | 61 | ambiguous | Frequently self-declared as synthesized by source authors |
| Motion | 44 | partial | Durations rarely given |
| Interaction feedback | ~25 | **weak** | "Hover states not documented by system policy" recurs |
| Accessibility | 74 mention / 0 verify | ambiguous | See D9 |
| Agent prompt guidance | 10 + 50 iteration guides | partial | |

**Read the bottom of this table, not the top.** Everything a static brand page needs is
richly documented. Everything an *interactive application* needs — states, feedback,
tables, dialogs, empties — is at or near zero. That asymmetry is the shape of the corpus
and the reason four derived category guides carry synthesized-evidence banners.

## 3. Per-source matrix — structural axes

Condensed. `●` strong / `◐` partial / `○` absent.

| Source | Tokens | Type scale | Space | Radius | Elev | Resp | States | App UI |
|---|---|---|---|---|---|---|---|---|
| airbnb | ● | ● | ● | ○ | ◐ | ● | ○ | ○ |
| airtable | ● | ● | ● | ● | ● | ● | ○ | ○ |
| apple | ● | ● | ● | ● | ● | ● | ○ | ○ |
| binance | ● | ● | ● | ● | ● | ● | ◐ | ◐ |
| bmw / bmw-m | ● | ● | ● | ● | ● | ● | ○ | ○ |
| bugatti | ● | ● | ● | ◐ | ● | ● | ○ | ○ |
| cal | ● | ● | ● | ● | ● | ● | ○ | ○ |
| claude | ● | ● | ● | ● | ● | ● | ○ | ○ |
| clay / clickhouse / cohere | ● | ● | ● | ● | ● | ● | ○ | ○ |
| coinbase | ● | ● | ● | ● | ● | ● | ○ | ○ |
| composio / cursor | ● | ● | ● | ● | ● | ● | ○ | ○ |
| dell-1996 | ● | ● | ● | ◐ | ● | ◐ | ○ | auto |
| elevenlabs / expo | ● | ● | ● | ● | ● | ● | ○ | ○ |
| ferrari / figma / framer | ● | ● | ● | ● | ● | ● | ○ | ○ |
| hashicorp | ● | ● | ● | ● | ● | ● | ○ | ○ |
| hp / ibm / intercom | ● | ● | ● | ● | ● | ● | ○ | ○ |
| kraken | ◐ | ◐ | ◐ | ◐ | ◐ | ○ | ○ | ○ |
| lamborghini | ● | ● | ● | ● | ● | ● | ○ | ○ |
| linear.app | ● | ● | ● | ● | ● | ● | ◐ | ○ |
| lovable | ● | ● | ◐ | ● | ● | ● | ○ | ○ |
| mastercard | ● | ● | ● | ● | ● | ● | ○ | ○ |
| meta | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| minimax / mintlify | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| miro / mistral.ai / mongodb | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| nike | ● | ● | ● | ● | ● | ● | ◐ | ◐ |
| nintendo-2001 | ● | ● | ● | ● | ● | ◐ | ○ | auto |
| notion / nvidia | ● | ● | ● | ● | ● | ● | ○ | ○ |
| ollama / opencode.ai | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| pinterest / playstation | ● | ● | ● | ● | ● | ● | ○ | ○ |
| posthog / raycast | ● | ● | ● | ● | ● | ● | ○ | ○ |
| renault / replicate / resend | ● | ● | ● | ● | ● | ● | ◐ | ○ |
| revolut / runwayml / sanity | ● | ● | ● | ● | ● | ● | ○ | ○ |
| sentry / shopify | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| slack / spacex | ● | ● | ● | ● | ● | ● | ○ | ○ |
| spotify | ● | ● | ◐ | ● | ● | ◐ | ◐ | **●** |
| starbucks | ● | ● | ● | ● | ● | ● | ◐ | ◐ |
| stripe / supabase / superhuman | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| tesla | ● | ● | ● | ● | ● | ● | ○ | ◐ |
| theverge | ● | ● | ● | ◐ | ● | ● | ○ | **●** |
| together.ai / uber | ● | ● | ● | ● | ● | ◐ | ○ | auto |
| vercel / vodafone / voltagent | ● | ● | ● | ● | ● | ◐ | ○ | auto |
| warp / webflow / wired | ● | ● | ● | ● | ● | ◐ | ○ | auto |
| wise / x.ai / zapier | ● | ● | ● | ● | ● | ◐ | ○ | auto |

`auto` = application-surface components present but machine-generated rather than observed
(discrepancy D7). They are not counted as evidence of application design.

**The `States` column is almost entirely `○`.** That is the corpus's defining limitation
for anyone trying to build an interactive product from it.

## 4. Values recorded as deliberate absences

Not missing data — stated positions. Preserving the distinction was a methodology
requirement, and these are the cases where it bites.

| Source | Absence | Why it is a position |
|---|---|---|
| `design-md/bugatti/` | No mid-radius; no accent colour | Radius scale published as `none`/`pill`/`full` only; the file states there is no accent, no decorative element, no chrome |
| `design-md/wired/` | No mid-radius | Published radius scale is `0px` and `9999px` |
| `design-md/opencode.ai/` | No proportional typeface | Entire page is monospaced by design |
| `design-md/linear.app/` | No light mode; no shadows | File states a light-mode marketing page should not ship, and that the brand resists drop shadows on dark |
| `design-md/raycast/` | No light mode | Dark is the only documented mode |
| `design-md/ibm/` | No shadows | Thin-bordered tiles, flat by system policy |
| `design-md/spacex/` | No filled buttons | One ghost outlined button per band |
| Many files | No hover states | Explicitly "not documented by system policy" — absent from the documentation, not from the product |

Treating any of these as `0` or as a recommendation would misrepresent the source. Treating
the hover-state absence as "hover doesn't matter" would be the worst of the available
misreadings.
