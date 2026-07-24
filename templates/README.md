# DESIGN.md Templates

Eleven templates on one shared skeleton. Copy one into your project root as `DESIGN.md` and
resolve every marker.

---

## The templates

| Template | For |
|---|---|
| [DESIGN.foundation.md](DESIGN.foundation.md) | Any product; the base all others extend |
| [DESIGN.conversational-ai.md](DESIGN.conversational-ai.md) | Chat and assistant interfaces |
| [DESIGN.general-website.md](DESIGN.general-website.md) | Documentation, support, informational, editorial |
| [DESIGN.marketing-website.md](DESIGN.marketing-website.md) | Marketing and conversion pages |
| [DESIGN.multi-role-platform.md](DESIGN.multi-role-platform.md) | Three or more user roles |
| [DESIGN.dashboard-admin.md](DESIGN.dashboard-admin.md) | Dashboards, admin, analytics |
| [DESIGN.developer-tool.md](DESIGN.developer-tool.md) | Developer products |
| [DESIGN.ecommerce.md](DESIGN.ecommerce.md) | Catalogue, PDP, checkout |
| [DESIGN.high-trust.md](DESIGN.high-trust.md) | Financial, security, legal, irreversible |
| [DESIGN.spatial.md](DESIGN.spatial.md) | Map, spatial, 3D |
| [ROLE-EXPERIENCE-MAP.md](ROLE-EXPERIENCE-MAP.md) | Companion to the multi-role template |

Content/editorial uses `DESIGN.general-website.md` with the typography section from
[../categories/content-editorial.md](../categories/content-editorial.md). Data analytics uses
`DESIGN.dashboard-admin.md` plus the chart and query sections from
[../categories/data-analytics.md](../categories/data-analytics.md). Both are documented in their
guides.

## Markers

| Marker | Meaning |
|---|---|
| `[[SET: description]]` | You must supply a value. No default exists. |
| `[[CHOOSE: a \| b \| c]]` | Pick one. The first option is usually the safe default. |
| Plain values | Researched defaults. Change with a reason you can state. |

**Resolve every marker before shipping.** An unresolved `[[SET: ...]]` in a `DESIGN.md` is worse
than a missing section — an agent will treat it as literal text.

## Shared structure

Every template follows the same order, so a reader who knows one knows them all:

1. Frontmatter — primitive tokens, semantic tokens (light and dark), typography, spacing, radius,
   layout, elevation, motion, components
2. Product context
3. Users and roles
4. Experience principles
5. Visual theme
6. Colour discipline
7. Layout
8. Navigation
9. Components and interaction states
10. States, feedback, edge cases
11. Responsive behaviour
12. Accessibility commitments
13. Content guidance
14. Category-specific rules
15. Do / Do not
16. Implementation notes
17. Agent prompt guidance

## Choosing and combining

Pick your primary category with
[../CATEGORY-SELECTION.md](../CATEGORY-SELECTION.md). Use that template as your base.

For hybrid products with several surfaces, **one `DESIGN.md`** with per-layer sections beats
several competing files. The frontmatter tokens are shared; each layer states its own density,
navigation, rhythm, and polarity. See
[../PROJECT-INITIALIZATION.md](../PROJECT-INITIALIZATION.md) §Worked example.

## What every template requires

Non-negotiable across all eleven — these are the sections most often skipped:

- **Two-layer tokens.** Primitives and semantics. Components consume semantics only.
- **Light and dark specified separately.** Never derive one by inverting the other.
- **All eight interaction states** per interactive component: default, hover, focus-visible,
  active, disabled, loading, selected, error.
- **All data states:** first-run empty, filtered-empty, initial loading, refresh loading, partial,
  error, permission denied.
- **Per-element responsive behaviour**, named: resize, reflow, collapse, stack, scroll, drawer,
  transform, defer, omit.
- **Accessibility commitments**, written as checkable statements.
- **A typeface substitution note** if any family is proprietary. 59 of 74 corpus sources publish
  one; without it your system is unusable by anyone who cannot license the font.
- **Agent prompt guidance**, including the reading order and the required report format.

## Do not

- Do not fill a template with vague statements. "Use clean, modern design" tells an implementer
  nothing and licenses arbitrary choices.
- Do not copy a brand's `DESIGN.md` from `design-md/` into your project. Those document other
  companies' identities. See [../LICENSING-CONSIDERATIONS.md](../LICENSING-CONSIDERATIONS.md).
- Do not leave a decision implicit because it feels obvious. Whatever is unspecified will be
  invented, differently, by each person and each agent that touches the code.
