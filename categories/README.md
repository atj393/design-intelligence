# Category Guides

Eleven guides. Each covers one product category's density, navigation, component set,
interaction patterns, responsive strategy, accessibility pressures, and anti-patterns.

**Read [../COMMON-FOUNDATION.md](../COMMON-FOUNDATION.md) first.** These guides override the
foundation's density, navigation, and component emphasis. They do not override its scales,
token architecture, or accessibility floor.

**Do not read a category guide as a visual style.** Category determines *how dense, how
navigated, which components*. It does not determine tone, palette, or typeface — the corpus
shows the same product category rendered in four incompatible visual registers. Tone comes from
your brand, via [../CATEGORY-SELECTION.md](../CATEGORY-SELECTION.md) Part 2.

---

## The guides

| Guide | Choose when | Evidence |
|---|---|---|
| [conversational-ai.md](conversational-ai.md) | Conversation is the primary interface | **Very weak — synthesized** |
| [general-website.md](general-website.md) | Public site optimising for comprehension | Moderate |
| [marketing-website.md](marketing-website.md) | Public site optimising for conversion | **Strong** |
| [commercial-multi-role-platform.md](commercial-multi-role-platform.md) | Three or more materially different roles | Weak — synthesized |
| [dashboard-admin.md](dashboard-admin.md) | Dense, authenticated, daily-use operations | Weak — synthesized |
| [developer-tools.md](developer-tools.md) | Technical product for a technical audience | Moderate-strong |
| [ecommerce.md](ecommerce.md) | Discovery, comparison, purchase | Moderate |
| [financial-high-trust.md](financial-high-trust.md) | Money, security, legal, irreversible actions | Moderate |
| [content-editorial.md](content-editorial.md) | Long-form reading at volume | Moderate |
| [data-analytics.md](data-analytics.md) | Exploring data rather than monitoring it | Weak — synthesized |
| [spatial-map-3d.md](spatial-map-3d.md) | Map or 3D canvas is the primary surface | **None — fully synthesized** |

## Reading the evidence banners

Every guide opens with an evidence banner. It is the most important paragraph in the file.

| Banner | Meaning | How to use it |
|---|---|---|
| **Strong** | Many sources document this exact surface type | Trust the numbers |
| **Moderate** | Real sources exist but are few, or cover part of the category | Trust the structure; verify the specifics |
| **Weak — synthesized** | No direct sources; general interface reasoning | Treat as a considered starting position; validate with users early |
| **None — fully synthesized** | Corpus is silent | Treat as a hypothesis; test before committing |

The uncomfortable pattern: **the categories most in demand for new software are the ones the
source corpus supports least.** The corpus is ~90% marketing websites, so marketing guidance is
authoritative while dashboard, conversational, multi-role, and spatial guidance is reasoning.
Both are useful. Only one is evidence. Full analysis:
[../research/CATEGORY-INVENTORY.md](../research/CATEGORY-INVENTORY.md) §3.

## Not given a standalone guide

**Mobile-first.** Merged deliberately rather than dropped. The corpus's responsive sections are
frequently declared *by their own authors* as synthesized from desktop evidence — several source
files state that mobile screenshots were not captured. Building a mobile-native guide on top of
already-synthesized responsive claims would stack invention on invention. Mobile requirements
are instead mandatory in every guide above, plus a dedicated section in
[../DESIGN-DECISION-HANDBOOK.md](../DESIGN-DECISION-HANDBOOK.md). Rationale:
[../ASSUMPTIONS.md](../ASSUMPTIONS.md) D-05.

## Combining guides

Most real products need two or three. The pattern is one token foundation with several
experience layers, each setting its own density and navigation:

| Product | Primary | Supporting |
|---|---|---|
| SaaS with a public site | Dashboard | Marketing, General Website |
| API product | Developer Tools | General Website (docs), Dashboard (console) |
| Marketplace | E-commerce | Multi-Role Platform, Marketing |
| Banking app | Financial/High-Trust | Dashboard, Marketing |
| Ops platform with an assistant | Multi-Role Platform | Dashboard, Conversational AI |
| Site-analysis product | Spatial | Data Analytics, Dashboard |
| Publication with subscriptions | Content/Editorial | Marketing, E-commerce |

Layering model: [../CATEGORY-SELECTION.md](../CATEGORY-SELECTION.md) Part 4.
Side-by-side comparison: [../CATEGORY-COMPARISON.md](../CATEGORY-COMPARISON.md).
