# Pattern Clusters, Co-occurrences and Incompatibilities

Which design decisions travel together, which contradict each other, and where the corpus
genuinely disagrees with itself. This is the analysis that feeds
[../DESIGN-DECISION-HANDBOOK.md](../DESIGN-DECISION-HANDBOOK.md).

---

## 1. Co-occurring decision sets

A cluster is a set of choices that appear together across multiple sources and that
reinforce each other. These are the corpus's recurring, coherent "kits".

### C1 — Dark technical surface ladder

**Observed in ~14 sources** — linear.app, raycast, voltagent, warp, sanity, resend,
composio, clickhouse, x.ai, framer, together.ai, spotify, supabase (dark tier),
opencode.ai (partial)

| Decision | Value |
|---|---|
| Canvas | Near-black, rarely pure black (`#010102`–`#121212`) |
| Hierarchy | 3–5 step lightness ladder, **not** shadow |
| Borders | 1px hairline, often translucent white |
| Accent | Exactly one chromatic colour, scarce |
| Radius | 4–12px |
| Typography | Sans display 500–600, negative tracking; mono for code only |
| Elevation | Surface step + border; shadow rejected or minimal |

**Why it holds together:** shadow requires a light background to read against. On a dark
canvas, lightness steps *are* the elevation vocabulary, so the border does the edge
definition shadow would otherwise provide. Remove the ladder and a dark UI flattens into
mud; add shadows and it looks smudged.

`design-md/linear.app/` documents this most completely — a four-step ladder plus three
hairline weights, with shadows explicitly avoided.

### C2 — Warm editorial calm

**Observed in ~11 sources** — claude, cursor, lovable, posthog, replicate, zapier,
elevenlabs, intercom, mastercard, starbucks, wired

| Decision | Value |
|---|---|
| Canvas | Cream / parchment / bone, never pure white |
| Ink | Warm near-black, never `#000000` |
| Display | Serif or humanist sans at 300–500 |
| Line height | Generous (1.5–1.7 body) |
| Accent | One warm hue (coral, orange, terracotta), scarce |
| Elevation | Hairline borders, minimal shadow |
| Imagery | Illustration or atmospheric photography over product screenshots |

**Why it holds together:** every element lowers contrast and temperature in the same
direction. A tinted canvas reduces the harshness that light display weights cannot survive
on pure white, and warm ink keeps the whole surface on one temperature axis.

**Notable:** four of these are developer tools. The cluster is a deliberate rejection of the
dark-technical default, and it is where `design-md/cursor/` and `design-md/lovable/`
explicitly position themselves.

### C3 — Photographic cinema

**Observed in ~9 sources** — tesla, spacex, bugatti, lamborghini, ferrari, bmw-m, runwayml,
playstation, nike (campaign tier)

| Decision | Value |
|---|---|
| Imagery | Full-bleed photo/video as the primary interface element |
| Chrome | Near-absent; one CTA per band |
| Display | Uppercase, **positive** tracking, light-to-medium weight |
| Radius | 0px or pill only |
| Colour | Monochrome plus at most one brand hue |
| Elevation | None — imagery provides depth |

**Why it holds together:** the imagery carries all visual interest, so any chrome competes
with it. Positive-tracked uppercase reads as a caption *over* an image rather than a
headline *on a page*.

**Where it fails:** this kit cannot carry information density. It has no vocabulary for
tables, forms, or repeated content. Sources using it document very few components.

### C4 — Documentation density

**Observed in ~6 sources** — mintlify, minimax, mongodb (docs tier), ollama, nvidia,
voltagent

| Decision | Value |
|---|---|
| Layout | 3-column: nav sidebar / prose / table of contents |
| Prose measure | 640–960px, far narrower than the page container |
| Section rhythm | 48–64px, roughly half the marketing value |
| Display cap | 36–56px, well below the same brands' marketing pages |
| Code | Monospace, dedicated surface treatment |
| Radius | 4–8px |

**Why it holds together:** the surface's job is comprehension per unit of effort. Every
value moves toward scannability — narrow measure for reading speed, tight rhythm to keep
related content on-screen, small display type because the heading's job is navigation and
not persuasion.

**Most useful cluster in the corpus** for deriving general principles, because several
sources document *both* their marketing and documentation surfaces. Same brand, same
tokens, deliberately different density. That is category logic isolated from brand
variables.

### C5 — Clinical single-signal

**Observed in ~10 sources** — apple, ibm, hp, coinbase, vercel, expo, cal, uber, nvidia
(body tier), supabase

| Decision | Value |
|---|---|
| Canvas | White or near-white |
| Accent | One "signal" colour, used only for the primary action |
| Radius | 0–8px |
| Display weight | 300–400 (restraint as premium signal) |
| Borders | Hairline; shadow rare |
| Colour count | Minimal — often under 25 tokens |

**Why it holds together:** when exactly one thing is coloured, colour becomes unambiguous
instruction. Adding a second accent halves the signal value of the first.

### C6 — Expressive colour blocking

**Observed in ~9 sources** — figma, miro, notion, clay, webflow, theverge, sentry,
pinterest, slack

| Decision | Value |
|---|---|
| Base | Monochrome or neutral frame |
| Interruption | Full-panel saturated colour blocks between neutral sections |
| Accent mapping | Colours map to **structure** — product categories, content types, object types |
| Radius | Moderate-to-soft, 8–32px |
| Illustration | Present and load-bearing |

**Why it holds together:** the neutral frame is what makes the colour blocks read as
deliberate. Colour is used at *panel* scale rather than sprinkled across components, so the
page stays legible while feeling energetic.

**Critical detail:** in every member, multiple accents map to something real.
`design-md/webflow/` maps five stops to product categories; `design-md/hashicorp/` maps
accents to individual products; `design-md/notion/` and `design-md/miro/` echo colours users
actually see inside the product. None uses multiple accents decoratively. This is the
difference between a multi-colour system and a colour mess.

### C7 — Dual-track polarity

**Observed in 2 sources explicitly, 4 partially** — binance, shopify; partially stripe,
mongodb, nvidia, supabase

| Decision | Value |
|---|---|
| Marketing surface | Dark, cinematic, expressive |
| Transactional / product surface | Light, dense, functional |
| Shared | Typography family, radius scale, button vocabulary, spacing ladder |
| Different | Canvas polarity, information density, decoration budget |

**Why this matters more than its file count.** These two sources independently arrived at
the answer to the hybrid-product question: one token foundation, two surface treatments,
switching on the surface's *job* rather than its brand. It is the empirical basis for the
shared-foundation model in
[../categories/commercial-multi-role-platform.md](../categories/commercial-multi-role-platform.md).

`design-md/binance/` states it directly: marketing and product default to dark; buy,
deposit, and exchange flip to light while keeping the same CTA colour and hairlines.

## 2. Reliable pairwise correlations

| If a system has… | It reliably also has… | Files | Mechanism |
|---|---|---|---|
| Dark canvas | Surface ladder instead of shadow | ~14/14 | Shadow needs light to read against |
| Display >80px | Negative tracking ≥1px | ~24/26 | Default spacing looks loose at scale |
| Uppercase display | **Positive** tracking | ~12/12 | Capitals need air to stay legible |
| Small caps / eyebrow text | Positive tracking +0.2–1.5px | ~40/45 | Same mechanism at small size |
| One accent only | Accent reserved for primary CTA + focus | ~44/44 | Scarcity is the whole point |
| Multiple accents | Accents mapped to structure | ~11/13 | Otherwise colour stops meaning anything |
| Tinted (non-white) canvas | Warm ink instead of pure black | ~11/12 | Temperature consistency |
| Documentation surface | Narrow prose measure + tighter rhythm | 6/6 | Reading beats impressing |
| Photography-led | Near-zero chrome, minimal component set | ~9/9 | Chrome competes with imagery |
| Squared radius (0–4px) | Flat elevation, no shadow | ~14/18 | Both signal engineered precision |
| Proprietary typeface | Documented substitution guidance | 59/~62 | Without it the system is unusable |
| Financial / trading domain | Tabular figures + directional colour | 4/8 | Numeric comparison and price direction |

The proprietary-typeface row is the most practically important. 59 files publish a
`Note on Font Substitutes`. A design system built on a font nobody can license is
decoration; the substitution note is what makes it a reusable system. Any template derived
from this corpus must carry the same requirement — and
[../templates/](../templates/) does.

## 3. Incompatible combinations

Combinations no source uses, where the incompatibility is mechanical rather than
stylistic. These become the enforcement rules in
[../ANTI-PATTERNS.md](../ANTI-PATTERNS.md).

| Incompatible pair | Why it breaks | Corpus evidence |
|---|---|---|
| Enterprise-density layout **+** 96px section rhythm | Density exists to reduce scrolling; marketing rhythm reintroduces it. Contradictory goals in one surface | Documentation surfaces of the same brands drop to 48–64px |
| Heavy shadows **+** flat minimal system | Flatness communicates precision; shadow communicates physicality. Reads as inconsistency, not richness | ~12 flat systems publish no shadow at all |
| Decorative display typeface **+** data-dense operational UI | Display faces sacrifice legibility at small size and repetition; tables are nothing but small repeated text | No source applies display type to tabular content; `design-md/stripe/` moves to tabular figures for numerics |
| Multiple unmapped accents **+** semantic status colours | If five accents are decorative, users cannot tell decoration from a warning | All multi-accent systems map accents to structure |
| Dark canvas **+** shadow-based elevation | Shadow is invisible on dark; hierarchy silently disappears | ~14/14 dark systems use ladders |
| Pill radius on everything **+** dense data rows | Pills consume horizontal space and blur row alignment | Pill-heavy systems are low-density marketing pages |
| Light display weight (300) **+** small sizes on tinted canvas | Contrast collapses; weight 300 needs scale to survive | Light-weight systems confine 300 to display sizes and shift to 400–600 for body |
| Uppercase display **+** long body text | Uppercase reduces reading speed materially at paragraph length | Every uppercase system confines it to short labels and headlines |
| Full-bleed imagery hero **+** dense form immediately below | Imagery demands a viewport; forms demand focus. Both fight | Photographic systems keep forms on separate light surfaces |
| Zero elevation vocabulary **+** overlays and modals | Overlays need to read as above the page; without shadow, border, or scrim there is no mechanism | Flat systems that do document modals add a scrim |

## 4. Documented disagreements

Where sources genuinely conflict. In each case both positions are defensible, and the
condition that decides between them is what matters.

### Disagreement 1 — Display weight in high-trust products

- **Light (300–400):** stripe (300), coinbase (400), ibm (300), playstation (300)
- **Heavy (700–900):** binance (700), wise (900), revolut (500 at 136px), vodafone (800)

Both claim trust. Light weight signals *institutional composure* — nothing to prove. Heavy
weight signals *confident accessibility* — clear, loud, unambiguous.

**Deciding condition:** audience sophistication and channel. Light weight suits
institutional and B2B audiences reading on large screens. Heavy weight suits mass-consumer
audiences, mobile-first reading, and markets where the brand is still establishing
recognition. Neither is more trustworthy in the abstract.

### Disagreement 2 — Radius character in finance

- **Squared:** ibm (0–4px), nvidia (1–2px), hp (2–8px)
- **Soft:** mastercard (40px heroes, pill cards, circular crops), revolut (12–28px),
  wise (8–24px)

**Deciding condition:** whether the product is *infrastructure* or *consumer-facing*.
Infrastructure and enterprise tooling read as precise when squared. Consumer money apps
read as approachable when soft, which matters more when the user is anxious about money.
`design-md/mastercard/` is proof that a maximally soft, pill-dominant system is compatible
with a payments brand.

### Disagreement 3 — Canvas polarity for developer tools

- **Dark:** linear.app, raycast, voltagent, warp, sanity, resend, composio, clickhouse
- **Light/cream:** cursor, lovable, posthog, replicate, expo, supabase, vercel, ollama

An even split in the same domain — which by itself disproves any claim that developer tools
must be dark.

**Deciding condition:** whether the tool's surface should feel continuous with an IDE or
terminal (dark), or continuous with documentation and reading (light). `design-md/cursor/`
sells an editor and chose cream *because* the genre default is dark.

### Disagreement 4 — Section rhythm

- **Generous (96px+):** 61 files
- **Compressed (32–64px):** documentation surfaces, editorial products, retro
  reconstructions

**Deciding condition:** visit frequency. Rhythm that feels considered on first visit feels
obstructive on the fortieth. Not a disagreement about taste — a disagreement about how often
the user comes back, and both sides are right for their own case.

### Disagreement 5 — Shadow versus border for elevation

- **Border-only:** ~38 files, near-total among dark systems
- **Shadow-based:** ~14 files, all light consumer systems
- **Contextual:** ~10 files — shadow on media, borders on chrome (`design-md/apple/` is the
  clearest: shadowless chrome, one signature shadow under product imagery)

**Deciding condition:** canvas lightness first (shadow needs light), then whether elevation
must communicate *physical* lift (media, overlays) or merely *grouping* (cards, panels).
Borders are sufficient for grouping and cheaper visually.

## 5. What generalises and what does not

| Finding | Class | Portable? |
|---|---|---|
| 4px base grid, 8px increments | Universal | Yes |
| 16px default body | Universal | Yes |
| 480/768/1024/1280/1440 breakpoints | Universal | Yes |
| 44px touch minimum | Universal | Yes |
| Negative tracking scales with display size | Universal | Yes |
| Positive tracking on small uppercase | Universal | Yes |
| One accent, used scarcely | Universal (strong) | Yes |
| Multiple accents must map to structure | Universal | Yes |
| Proprietary faces need substitution guidance | Universal | Yes |
| Dark canvas → ladder not shadow | Universal | Yes |
| Prose measure narrower than page container | Universal | Yes |
| 24px card padding | Category-dependent | With density adjustment |
| 96px section rhythm | Context-dependent | **No** — visit-frequency dependent |
| 1280px container | Context-dependent | With content-type adjustment |
| 64–72px hero display | Category-dependent | Marketing only |
| Uppercase tracked display | Brand-specific | As a structural idea only |
| Light display weight as premium signal | Brand-specific | Conditionally |
| All-monospace page | Exception | **No** |
| Radius scale of only 0 and 9999 | Exception | **No** |
| 136–144px display type | Exception | **No** |
| Skeuomorphic bevelled panels | Exception (period) | **No** |
