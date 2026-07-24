# Value Distributions

Observed numeric distributions across the corpus. Counts are files, not occurrences.
Extraction was section-scoped (see [../METHODOLOGY.md](../METHODOLOGY.md) §2) — a
document-wide regex would report `9999` as a breakpoint by catching pill-radius tokens.

**These are observations, not recommendations.** The population is ~90% marketing websites
(see [CATEGORY-INVENTORY.md](CATEGORY-INVENTORY.md)). A modal value here describes what
brand websites do. [../COMMON-FOUNDATION.md](../COMMON-FOUNDATION.md) converts these into
guidance, and where the population is wrong for a use case it says so.

---

## 1. Base grid unit

| Value | Files |
|---|---|
| 8px | 29 |
| 4px | 28 |
| 5px | 1 |
| not stated | 16 |

Effectively a tie, and the tie dissolves on inspection: nearly every 8px-declared system
still uses 4px and 12px steps. The corpus operates a **4px grid with 8px preferred
increments**, which is what the foundation adopts. The single 5px system is an outlier tied
to one brand's proprietary ladder.

## 2. Spacing ladders

Ladder length ranges from 3 steps (`design-md/bugatti/`) to 14 (`design-md/meta/`).

**Step-value frequency across all ladders:**

| Step | Files using it |
|---|---|
| 4px | 71 |
| 8px | 73 |
| 12px | 68 |
| 16px | 70 |
| 24px | 64 |
| 32px | 61 |
| 2px | 34 |
| 20px | 26 |
| 48px | 41 |
| 64px | 22 |
| 40px | 12 |
| 96px | 12 |
| 128px | 4 |

The core `4 · 8 · 12 · 16 · 24 · 32` sequence is near-universal (61–73 files each). Above
32px, ladders diverge by category — marketing sites extend to 96–192px, documentation and
retro surfaces stop at 48px.

**Section-spacing token values:**

| Value | Files |
|---|---|
| 96px | 61 |
| 80px | 24 |
| 64px | 22 |
| 88px | 5 |
| 48px | 9 |
| 120px | 2 |
| 192px | 1 |

96px is the corpus's dominant section rhythm and the clearest example of a value that must
**not** be transplanted blindly. On a scroll-once acquisition page it is correct pacing. In
a tool someone opens forty times a day it is forty scroll costs.

## 3. Border radius

Aggregating every published radius scale:

| Value | Files | Typical role |
|---|---|---|
| 9999px (`full`) | 68 | Avatars, pills, toggles |
| 8px | 47 | Buttons, inputs — the corpus's default control radius |
| 4px | 45 | Chips, badges, small surfaces |
| 12px | 42 | Cards |
| 6px | 38 | Inline tags, small controls |
| 16px | 34 | Large cards, media frames |
| 0px (`none`) | 33 | Explicit square position |
| 2px | 20 | Near-square systems |
| 24px | 15 | Oversized feature cards |
| 20px | 8 | |
| 32px+ | 7 | Expressive/oversized systems |

**Distinct schools, not a spectrum.** Averaging these produces ~10px, a value that
satisfies none of the three positions actually held:

| School | Files | Character | Examples |
|---|---|---|---|
| **Square / near-square** (0–4px) | ~18 | Engineered, dense, technical, or austere | ibm (0–4), nvidia (1–2), warp (1–6), bmw-m (0–6), opencode.ai (0/4), renault (0–4), hp (2–8) |
| **Moderate** (6–16px) | ~40 | Contemporary product default | linear.app, claude, stripe, supabase, vercel, sentry, mintlify |
| **Soft / expressive** (20–40px+, or pill-dominant) | ~16 | Consumer warmth, approachability | mastercard (40px heroes), figma (24–32), pinterest (32), cohere (22–30), airbnb (14–32), nike (18–30) |

Two systems reject mid-radius entirely — `design-md/bugatti/` and `design-md/wired/`
publish only `0px` and `9999px`. That is an editorial position, not missing data.

## 4. Typography — display sizes

Largest display step per file:

| Range | Files | Notes |
|---|---|---|
| 20–40px | 8 | Documentation-first and utility-minimal surfaces (ollama 36, opencode.ai 38, posthog 36, cursor 72 but body-led) |
| 44–56px | 15 | Restrained marketing |
| 60–72px | 20 | Common marketing hero range |
| 76–96px | 18 | Confident brand statement |
| 100–144px | 6 | framer 110, replicate 128, revolut 136, vodafone 144, wise 126, theverge 107 |

Median largest display sits at **64–72px**. Documentation surfaces belonging to the *same*
companies cap at 36–56px.

## 5. Typography — body sizes

| Value | Files | Notes |
|---|---|---|
| 16px | 61 | Overwhelming default |
| 14px | 9 | Dense/compact systems, and secondary body everywhere |
| 17–18px | 6 | apple (17), playstation (18), zapier (18), vodafone (18) |
| 15px | 3 | framer, elevenlabs, posthog |
| 12–13px | 2 | Retro reconstructions only |

**16px is the strongest single convergence in the corpus.** 14px appears almost universally
as the *secondary* body step, not as primary body.

## 6. Typography — line height

| Role | Observed range | Modal |
|---|---|---|
| Display (48px+) | 0.85–1.20 | 1.05–1.15 |
| Headings (24–40px) | 1.10–1.33 | 1.20 |
| Body | 1.40–1.71 | 1.50 |
| Captions | 1.20–1.50 | 1.40 |
| Buttons | 1.00–1.60 | 1.20 |

The inverse relationship between size and line-height is universal here — no source sets
display type at body leading. `design-md/framer/` at 0.85 for 110px display is the extreme.

## 7. Typography — letter spacing

| Size band | Typical tracking | Direction |
|---|---|---|
| 80–144px | −0.8 to −5.5px | Negative, roughly 2–4% of size |
| 40–72px | −0.5 to −2.5px | Negative |
| 24–36px | −0.3 to −1.0px | Negative |
| 16px body | −0.16 to +0.24px | Near zero |
| 10–13px captions/eyebrows | +0.2 to +1.5px | **Positive** |
| Uppercase display | +1.0 to +6.0px | **Strongly positive** |

Two clean rules emerge, both near-universal: **negative tracking scales with display size**,
and **small uppercase text takes positive tracking**. The counter-cluster is deliberate —
automotive and austere brands (bugatti +4px at 64px, spacex, bmw-m) use positive tracking on
large uppercase display for a spaced, engineered character.

## 8. Typography — display weight

| Weight | Files | Character |
|---|---|---|
| 300 or lighter | 9 | ibm, stripe, playstation, elevenlabs, shopify — "premium restraint" |
| 400 | 12 | claude, coinbase, cursor, bugatti, resend, mistral.ai |
| 500 | 18 | Most common — confident but not shouting |
| 600 | 16 | linear.app, cal, expo, notion, mintlify, minimax |
| 700+ | 12 | binance, clickhouse, hashicorp, replicate, pinterest, spacex, slack |
| 800–900 | 3 | vodafone (800), wise (900), posthog (800) |
| Non-standard variable | 3 | figma (320–540), superhuman (460–540) |

No convergence, and the spread is category-correlated in an interesting way: heavy display
weights cluster in *retail, telecom, and trading* brands; light weights cluster in
*enterprise and premium* brands. Both are trust strategies pointing in opposite directions.

## 9. Breakpoints

Section-scoped to `Responsive Behavior › Breakpoints`:

| Value | Files |
|---|---|
| 1440px | 37 |
| 1280px | 35 |
| 1024px | 34 |
| 768px | 33 |
| 1023px | 21 |
| 480px | 20 |
| 767px | 17 |
| 640px | 14 |
| 1279px | 12 |
| 1200px | 10 |
| 1920px | 7 |
| 320px | 7 |
| 425px | 8 |

The `1023/767/1279/1439` values are max-width expressions of the same boundaries as
`1024/768/1280/1440`. Collapsing those, the corpus converges on:

**480 · 768 · 1024 · 1280 · 1440** — with 640px as a common extra small-tablet step and
1920px for extra-wide.

This is the corpus's second-strongest convergence after 16px body text.

## 10. Content / container widths

Section-scoped to `Layout › Grid & Container`:

| Value | Files | Role |
|---|---|---|
| 1280px | 27 | Dominant max content width |
| 1200px | 19 | Second most common |
| 1440px | 10 | Wide layouts |
| 1024px | 7 | Narrow/dense |
| 720px | 5 | Prose measure |
| 768px | 5 | Prose measure |
| 960px | 4 | Narrow content |
| 1400px | 3 | |
| 1600px+ | 3 | |
| 980px | 1 | apple — tightest in corpus |

**Two distinct widths per system.** Files documenting both a page container and a prose
column show 1200–1440px for the container and 640–960px for the reading measure. Systems
with documentation surfaces make this explicit: `design-md/ollama/` publishes 720px and
960px; `design-md/together.ai/` publishes 1280px and 900px.

## 11. Touch targets

Section-scoped to `Responsive Behavior › Touch Targets`:

| Value | Files |
|---|---|
| 44px | 48 |
| 40px | 33 |
| 48px | 18 |
| 32px | 17 |
| 36px | 13 |
| 24–28px | 10 |
| 56px | 6 |

**44px is the clearest accessibility convergence in the corpus** — consistent with the
platform guidance it presumably derives from. Values below 40px appear as *desktop
pointer* minimums, with the same files stating they grow to 44px on touch. Where a file
gives both, the pattern is explicit: e.g. `design-md/linear.app/` documents pills at ≥36px
that "grow to ≥44px" on touch viewports.

## 12. Component heights

From component specifications:

| Value | Files | Typical role |
|---|---|---|
| 40px | 22 | Standard control height |
| 64px | 22 | Navigation bar |
| 44px | 19 | Comfortable control / touch control |
| 56px | 14 | Navigation bar (compact) |
| 48px | 14 | Large control / small nav |
| 36px | 12 | Compact control |
| 32px | 4 | Dense control |
| 28px | 2 | Very dense |

Bimodal, as expected: a **control cluster at 36–48px** and a **navigation cluster at
56–64px**.

## 13. Control padding

| Buttons (v × h) | Files |
|---|---|
| 10 × 18 | 11 |
| 8 × 14 | 5 |
| 12 × 16 | 5 |
| 10 × 15 | 2 |
| 10 × 20, 8 × 18, 12 × 20, 4 × 16 | 1 each |

| Inputs (v × h) | Files |
|---|---|
| 10 × 14 | 3 |
| 6 × 12 | 2 |
| 11 × 16 | 2 |
| 12 × 14, 8 × 12, 12 × 24 | 1 each |

Sparser data than other measurements — many files specify height instead of padding. The
consistent relationship is **horizontal padding ≈ 1.5–2× vertical**, which is what produces
a control that reads as a control rather than a square.

## 14. Card padding

| Value | Files |
|---|---|
| 24px | 20 |
| 32px | 12 |
| 16px | 7 |
| 48px | 5 |
| 20px | 4 |
| 12px | 3 |
| 28px | 1 |
| 96px | 1 |

**24px is the modal card padding.** 16px reads as compact, 32px as generous, 48px+ as
feature-panel treatment rather than card padding.

## 15. Colour system size

| Token count | Files |
|---|---|
| under 25 | 11 |
| 25–34 | 26 |
| 35–44 | 18 |
| 45–60 | 7 |
| 60+ | 2 |

Modal range **25–44 semantic colour tokens** per system. Below ~20 the system typically
lacks documented semantic states; above ~50 the extra tokens are usually per-product or
per-illustration accents rather than interface roles.

**Token-name frequency** — the corpus's de facto vocabulary:

| Token | Files | Role |
|---|---|---|
| `primary` | 64 | Brand action colour |
| `ink` | 64 | Primary text |
| `on-primary` | 63 | Text on primary fill |
| `canvas` | 58 | Page background |
| `hairline` | 53 | 1px border |
| `body` | 38 | Body text |
| `on-dark` | 38 | Text on dark surface |
| `hairline-soft` / `-strong` | 26 each | Border hierarchy |
| `surface-soft` | 25 | One step above canvas |
| `surface-card` | 24 | Card fill |
| `muted` / `mute` | 43 combined | Secondary text |
| `warning` | 14 | Semantic |
| `success` / `semantic-success` | 26 combined | Semantic |
| `error` / `semantic-error` | 21 combined | Semantic |
| `info` | 4 | Semantic |

**Notable asymmetry:** brand and surface tokens are near-universal; semantic status tokens
are documented in roughly a third of files, and `info` in only 4. Consistent with a corpus
of marketing surfaces — a brochure page rarely needs a validation error. The derived
foundation therefore specifies a full semantic set as a **synthesized** requirement.

## 16. Number of accent colours

| Accents | Files | Pattern |
|---|---|---|
| 0 | 6 | Monochrome; photography or type carries all voltage |
| 1 | 44 | **Dominant: one brand colour, used scarcely** |
| 2 | 9 | Brand + one secondary |
| 3–5 | 11 | Multi-product or expressive systems |
| 6+ | 4 | Illustration-scoped palettes |

**The single strongest qualitative finding in the corpus.** 50 of 74 systems operate on
zero or one chromatic accent, and the files repeatedly state the accent is reserved for the
primary action, brand mark, and focus state. Multi-accent systems almost always map colours
to *something structural* — product lines (`design-md/hashicorp/`), product categories
(`design-md/webflow/`), or illustration only (`design-md/revolut/`) — never to decoration.

## 17. Dark mode handling

| Approach | Files |
|---|---|
| Dark-only surface | ~20 |
| Light-only surface | ~30 |
| Both modes documented | 24 |
| Explicit dual-track (different polarity per surface purpose) | 2 |

**No source in the corpus describes dark mode as an inversion of light mode.** Where both
are documented, they are described as separate surface systems with their own ladders. The
dual-track files are the clearest statement: `design-md/binance/` runs dark marketing and
light transactional; `design-md/shopify/` runs dark cinematic marketing and light
transactional. Both keep type and radius constant while flipping canvas polarity.

## 18. Elevation strategy

| Strategy | Files | Notes |
|---|---|---|
| Surface ladder + hairline borders, minimal shadow | ~38 | Dominant, and near-total on dark systems |
| Shadow-based elevation | ~14 | Mostly light consumer systems |
| Flat, no elevation | ~12 | Squared/austere systems |
| Mixed by context | ~10 | Shadow on media, borders on chrome |

`design-md/linear.app/` documents the clearest model: a four-step surface ladder plus
hairline borders, with shadows almost entirely rejected on dark. `design-md/ibm/` documents
thin-bordered tiles with no shadow at all. `design-md/apple/` keeps chrome shadowless and
reserves a single signature shadow for product imagery.

**Rule visible in the data:** shadow works on light canvases; on dark canvases, lightness
steps and hairlines do the work that shadow cannot.
