# Category Inventory

Category rollups over the 74 sources. Built from each file's own content — its description,
component vocabulary, and documented surfaces — not from company name or industry label
(see [../ASSUMPTIONS.md](../ASSUMPTIONS.md) D-07).

Per-source detail is in [../SOURCE-INVENTORY.md](../SOURCE-INVENTORY.md).

---

## 1. Documented surface — what the corpus actually measured

| Surface type | Count | Share |
|---|---|---|
| Public marketing / brand website (only) | 55 | 74% |
| Marketing + transactional surfaces | 6 | 8% |
| Marketing + documentation surfaces | 5 | 7% |
| Period reconstruction (retro series) | 2 | 3% |
| Editorial publication (real product surface) | 2 | 3% |
| Authenticated application UI | 1 | 1% |
| Thin/partial (structural outlier) | 1 | 1% |
| Mixed marketing + configurator | 2 | 3% |

**Reading this honestly:** ~90% of the corpus documents acquisition surfaces. That is a
strength for anything about brand expression, type hierarchy, section rhythm, and
token structure, and it is a hard ceiling on anything about sustained task work.

The exceptions are worth naming because they carry disproportionate weight later:

- `design-md/spotify/` — authenticated app UI (dark surface ladder, content-supplies-colour)
- `design-md/theverge/`, `design-md/wired/` — real editorial products (reading density,
  serif body, tile systems)
- `design-md/binance/`, `design-md/shopify/` — documented **dual-track** systems where the
  transactional surface deliberately inverts the marketing surface
- `design-md/mintlify/`, `design-md/minimax/`, `design-md/mongodb/` — 3-column
  documentation layouts
- `design-md/meta/`, `design-md/nike/` — product-detail and retail-chrome surfaces
- `design-md/tesla/` — a persistent chat-bar component

## 2. Product domain — what the organisations build

| Domain | Count | Sources |
|---|---|---|
| Developer tools & infrastructure | 20 | clickhouse, composio, cursor, expo, hashicorp, lovable, mintlify, mongodb, nvidia, ollama, opencode.ai, replicate, resend, sanity, sentry, supabase, vercel, voltagent, warp, cohere |
| Productivity / business SaaS | 12 | airtable, cal, figma, framer, ibm, intercom, linear.app, miro, notion, slack, superhuman, webflow, zapier |
| Financial & high-trust | 8 | binance, coinbase, kraken, mastercard, revolut, stripe, wise, (starbucks payments adjacency) |
| Commerce & retail | 8 | airbnb, apple, dell-1996, hp, meta, nike, shopify, starbucks |
| Automotive | 7 | bmw, bmw-m, bugatti, ferrari, lamborghini, renault, tesla |
| AI / LLM platforms | 7 | claude, elevenlabs, minimax, mistral.ai, together.ai, x.ai, runwayml |
| Media & publishing | 4 | pinterest, theverge, wired, runwayml |
| Consumer brand | 4 | nintendo-2001, playstation, spacex, spotify |
| Analytics / operations product | 1 | posthog |
| Multi-role platform | 1 | uber |
| Telecom | 1 | vodafone |

Counts overlap slightly where a source spans domains (runwayml is both AI and media).

## 3. Evidence strength per derived category

The number that matters. For each derived category guide: how many sources contribute
usable evidence, and what kind.

| Derived category | Direct surface evidence | Adjacent evidence | Strength | Basis of guidance |
|---|---|---|---|---|
| **Marketing website** | 55 | — | **Strong** | Corpus-backed throughout |
| **General informational website** | 5 (docs surfaces) | 20 dev-domain marketing sites | **Moderate** | Corpus-backed structure; synthesized navigation depth |
| **Content & editorial** | 2 (theverge, wired) | pinterest, apple, elevenlabs | **Moderate** | Two real products + strong typographic evidence |
| **Developer tools** | 5 docs + 20 domain | monospace usage in 56 files | **Moderate-strong** | Corpus-backed tone/type; synthesized log, key, config patterns |
| **E-commerce & transactional** | 6 (meta, nike, shopify, starbucks, apple, dell-1996) | airbnb, pinterest | **Moderate** | Corpus-backed discovery/PDP; **synthesized checkout** |
| **Financial & high-trust** | 8 domain, 1 dual-track (binance) | stripe tabular figures | **Moderate** | Corpus-backed trust expression; synthesized verification/audit flows |
| **Dashboard & administration** | **0** | 1 app UI (spotify), 3 with `Tables`, 13 auto-generated | **Weak** | **Predominantly synthesized** |
| **Data-intensive analytics** | **0** | posthog (marketing only), stat-display tokens in 6 files | **Weak** | **Predominantly synthesized** |
| **Conversational AI** | **0** | tesla chat bar; claude/intercom as AI-brand marketing | **Very weak** | **Predominantly synthesized** |
| **Commercial multi-role platform** | **0** | uber (multi-audience marketing), hashicorp (multi-product colour) | **Weak** | **Predominantly synthesized** |
| **Spatial / map / 3D** | **0** | none | **None** | **Fully synthesized** |
| **Mobile-first** | **0** | responsive sections, self-declared as synthesized by source authors | **None** | Merged into other guides — see D-05 |

This table is the reason the derived layer labels evidence strength on every guide. Four
categories the instruction asked for cannot be grounded in this corpus, and saying so is
more useful than pretending otherwise.

## 4. Visual-tone clusters

Tone clusters cut across product domain, which is itself a finding: domain does not
determine visual character nearly as much as one might assume.

| Cluster | Count | Characteristics | Representative sources |
|---|---|---|---|
| **Dark technical** | 14 | Near-black canvas, surface ladder over shadow, hairline borders, single accent, monospace details | linear.app, raycast, voltagent, warp, sanity, resend, composio, clickhouse, supabase(dark tier), x.ai, framer, together.ai, opencode.ai, spotify |
| **Warm editorial** | 11 | Cream/parchment canvas, serif or humanist display, generous leading, low chroma | claude, cursor, lovable, posthog, replicate, zapier, elevenlabs, intercom, mastercard, starbucks, wired |
| **Clinical minimal** | 10 | White canvas, one signal colour, tight radius, restrained weights | apple, ibm, hp, coinbase, vercel, expo, supabase, cal, nvidia(body mode), uber |
| **Cinematic monochrome** | 9 | Full-bleed imagery as primary UI, near-zero chrome, uppercase tracked display | tesla, spacex, bugatti, lamborghini, ferrari, bmw-m, runwayml, nike, playstation |
| **Expressive multi-colour** | 9 | Multiple saturated accents, colour-blocked panels, illustration | figma, miro, notion, clay, webflow, theverge, sentry, pinterest, slack |
| **Corporate confident** | 8 | Photography + one brand colour, chapter bands, mid-weight type | bmw, renault, vodafone, meta, mongodb, hashicorp, shopify, wise |
| **Documentation-first** | 6 | Content density over atmosphere, 3-column layouts, mono code | mintlify, ollama, minimax, mongodb(docs), nvidia, voltagent |
| **Fintech precision** | 5 | Tabular numerics, directional semantics, restrained display weight | stripe, binance, revolut, kraken, wise |
| **Period reconstruction** | 2 | Historically-specific idioms; not general guidance | dell-1996, nintendo-2001 |

Note the crossings. Developer tools appear in *dark technical*, *warm editorial*,
*clinical minimal*, and *documentation-first* — four incompatible tones for one domain. Any
claim that a product type dictates a visual tone is refuted by this corpus. Tone is a brand
decision; the category determines **density, navigation, and component set**, not
atmosphere. This is the single most load-bearing finding behind
[../CATEGORY-SELECTION.md](../CATEGORY-SELECTION.md).

## 5. Category-correlated measurements

Where category *does* show up in the numbers.

| Measurement | Marketing sites | Documentation surfaces | Editorial products | Retro reconstructions |
|---|---|---|---|---|
| Max display size | 56–144px | 36–72px | 64–107px | 36–44px |
| Section rhythm | 80–96px modal | 48–64px | 32–48px | 40–48px |
| Content width | 1200–1440px | 720–960px prose column | 1400px multi-column | not stated |
| Body size | 16px | 16px | 16–19px (serif) | 12–14px |
| Radius character | wide spread, 0–40px | 4–12px | 0px | 0px |

The documentation column is the most useful comparison in this table: same companies, same
brands, deliberately narrower measure and tighter rhythm the moment the surface's job
changes from persuading to explaining. That is category logic visible in the data, and it
generalises — see [../DESIGN-DECISION-HANDBOOK.md](../DESIGN-DECISION-HANDBOOK.md).
