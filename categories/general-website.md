# General Informational Websites

Public sites whose success is measured in comprehension and findability: documentation,
support centres, help systems, corporate information, knowledge bases, reference sites.

> **Evidence strength: moderate / partly corpus-backed.**
> Five sources document real documentation surfaces
> (`design-md/mintlify/`, `design-md/minimax/`, `design-md/mongodb/`, `design-md/ollama/`,
> `design-md/nvidia/`), and several of these belong to companies whose marketing pages are
> documented in the *same file* — a direct, brand-controlled comparison of how the same design
> system changes when the surface's job changes. That comparison is unusually good evidence.
> Navigation depth, search behaviour, and versioning guidance are synthesized.

---

## 1. What makes this category distinct

The user arrives **already knowing what they want** and needs to get it with minimum effort.
That inverts almost every marketing assumption.

| | Marketing | Informational |
|---|---|---|
| User state | Being convinced | Looking something up |
| Best outcome | They act | They leave quickly, satisfied |
| Type scale | Persuasion | Wayfinding |
| Rhythm | Generous | Tight |
| Nav | Few destinations | Many destinations |
| Search | Convenience | **Primary navigation** |
| Success signal | Time on page ↑ | Time to answer ↓ |

**Time on page is a failure signal here.** If someone spends four minutes on a
troubleshooting page, they did not find the answer in the first paragraph.

## 2. Layout

| Property | Default | Compact | Spacious |
|---|---|---|---|
| Container | 1280px | 1024px | 1440px |
| Prose measure | 680px | 640px | 720px |
| Section rhythm | 48px | 32px | 64px |
| Page padding (desktop) | 32px | 24px | 40px |
| Nav sidebar | 260px | 240px | 300px |
| TOC (right rail) | 220px | 200px | 240px |

### The three-column documentation layout

The corpus's clearest structural pattern for this category, documented by five sources:

```
┌──────────┬────────────────────────┬──────────┐
│ nav      │ prose                  │ TOC      │
│ 260px    │ 680px measure          │ 220px    │
│ sections │ content                │ h2/h3    │
│ + pages  │                        │ anchors  │
└──────────┴────────────────────────┴──────────┘
```

- **Left:** site structure. Current section expanded, siblings visible, others collapsed.
- **Centre:** the prose column at a real reading measure — this is the whole point.
- **Right:** in-page table of contents with the current position indicated.

Collapse order as width decreases: TOC first (it is a convenience), then the nav sidebar into
a drawer. **Never collapse the prose column below its measure** — narrow it to the viewport
minus padding, and stop.

**The measure is the non-negotiable part.** The corpus's documentation surfaces publish
narrow content widths — 720px and 960px in one source, 900px in another — against the
1280–1440px containers those same brands use for marketing. Same design system, deliberately
different measure, because the job changed.

## 3. Typography

| Token | Default | Compact | Spacious |
|---|---|---|---|
| Page title | 36px | 32px | 40px |
| `h2` | 28px | 24px | 32px |
| `h3` | 22px | 20px | 24px |
| `h4` | 18px | 16px | 18px |
| Body | 16px | 16px | 18px |
| Body small | 14px | 14px | 14px |
| Code inline | 14px | 13px | 14px |
| Code block | 14px | 13px | 14px |
| Caption | 13px | 12px | 13px |

Corpus documentation surfaces cap display at 36–56px against 56–144px on their marketing
counterparts. **Headings here are navigation, not persuasion.** A 72px page title in a help
centre is a category error.

**Requirements:**

- Body line-height 1.55–1.65 — higher than a marketing page, because people actually read
  this.
- Heading levels must be visually distinguishable at a glance in a scroll-past. If `h2` and
  `h3` look similar, scanning fails.
- Inline code needs a surface tint and a slightly smaller size than body so it reads as a
  distinct token without breaking the line.
- Space above a heading should be roughly 2× the space below it, so headings group with the
  content they introduce rather than floating between blocks.

## 4. Navigation and findability

### Structure

| Depth | Requirement |
|---|---|
| 1–2 levels | Sidebar list is sufficient |
| 3 levels | Sidebar with expand/collapse + breadcrumbs |
| 4+ levels | Reconsider the information architecture. Also: breadcrumbs mandatory |

- Current location must be visible in the sidebar at all times — an active indicator, not just
  a colour change.
- Never collapse the section the user is currently inside.
- Persist scroll position in the sidebar across page navigation. Losing it in a 200-item nav
  is genuinely disorienting.

### Search

**At 200+ pages, search becomes the primary navigation mechanism.** Below that it is a
convenience.

| Requirement | Detail |
|---|---|
| Placement | Top of the page, visible without scrolling; also in the sidebar header |
| Keyboard | `/` or `Cmd/Ctrl+K` to focus |
| Results | Show section context per result, not just the page title |
| Snippets | Highlight the matched term in context |
| Empty results | Suggest alternatives; offer a support path |
| Recent searches | Useful in repeat-visit reference sites |
| Speed | Results as you type; a search that requires submit-and-wait gets abandoned |

### Cross-linking

- Link related pages at the end of each article — 3–5, not an exhaustive list.
- Link the *first* occurrence of a term to its definition, not every occurrence.
- Previous / next navigation for sequential content (tutorials, guides).
- Never open internal links in a new tab.

## 5. Content components

| Component | Spec |
|---|---|
| Code block | Full-width of measure, `surface-sunken`, language label, copy button, no line wrap (scroll) |
| Inline code | `surface-sunken` tint, `radius.xs`, 0.9em, mono |
| Callout / admonition | Left border 3px in status colour + icon + label. Types: note, tip, warning, danger |
| Table | Full measure width, `border-subtle` rows, scroll in a bounded container at narrow widths |
| Image / diagram | Constrained to measure, click to expand, caption below |
| Steps list | Numbered, with clear visual separation per step |
| Tabs (e.g. per-language) | Persist the selection across pages — a user reading Python docs wants Python everywhere |
| Version selector | Prominent; indicate when viewing non-current documentation |
| Feedback control | "Was this helpful?" at page end, low-friction |
| Last updated | Date on every page. Stale documentation is worse than none |

**Callout discipline:** four types maximum, each with a distinct icon and colour. A page with
six callouts of five types has no hierarchy, and readers learn to skip all of them.

## 6. Page structure

Effective reference page shape:

1. **Title** — matches what the user searched for
2. **One-sentence summary** — what this page covers
3. **Prerequisites or context** — if any, and briefly
4. **The answer** — as early as possible
5. **Detail and variations**
6. **Examples** — real, runnable, complete
7. **Related links**
8. **Last-updated date + feedback**

**Put the answer near the top.** Background before answer is the most common documentation
failure. If the page says "How do I reset my password", the reset steps should be visible
without scrolling.

## 7. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Nav sidebar | Drawer | Drawer | Visible 260px |
| TOC | Collapsible accordion at top | Hidden | Visible 220px |
| Prose | Full width − 32px | 640px | 680px |
| Code blocks | Scroll, 13px | Scroll | Full |
| Tables | Scroll in bounded container | Scroll | Full |
| Breadcrumbs | Truncate middle | Full | Full |
| Search | Full-width, prominent | Prominent | In nav |

Documentation is heavily consumed on mobile — often by someone standing in front of the
problem. It must be genuinely usable, not merely responsive.

## 8. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor):

- **Heading structure is the primary navigation mechanism** for screen-reader users. One `h1`,
  no skipped levels, headings that describe content rather than being decorative.
- Skip-to-content link, visible on focus.
- Code blocks reachable by keyboard, scrollable, with labelled copy buttons.
- Callouts need a text label as well as colour and icon — "Warning:" not just an amber border.
- Tables need `<th>` with `scope`; complex tables need a caption.
- 200% zoom must reflow without horizontal scroll of the page (code blocks may scroll
  internally).
- Language switchers and version selectors need accessible names.

## 9. Do

- Put the answer near the top of the page
- Hold the prose measure at 60–70 characters regardless of container width
- Make heading levels visually distinguishable at a glance
- Show the current location in the sidebar at all times
- Make search primary once content exceeds ~200 pages
- Show section context in search results
- Persist tab and language selections across pages
- Date every page
- Keep callout types to four, each visually distinct
- Provide a copy button on every code block
- Keep line-height at 1.55–1.65 for body text

## 10. Do not

- Do not inherit marketing display sizes or section rhythm
- Do not let prose run the full container width
- Do not collapse the section the user is currently in
- Do not lose sidebar scroll position on navigation
- Do not require search submit-and-wait
- Do not put background before the answer
- Do not use more than four callout types
- Do not open internal links in new tabs
- Do not ship undated documentation
- Do not rely on colour alone for callout severity
- Do not hide the version indicator when showing outdated docs

## 11. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/mintlify/DESIGN.md` § *Layout*, § *Components* | The corpus's most complete 3-column documentation model: sidebar / prose / TOC, with a marketing hero on the same site running an entirely different density. The clearest single demonstration that surface job beats brand consistency in deciding density |
| `design-md/minimax/DESIGN.md` § *Layout* | Same 3-column structure, confirming it as a pattern rather than one company's choice |
| `design-md/mongodb/DESIGN.md` § *Layout*, § *Components* | Dark marketing hero against white documentation surfaces; card grids with category tags for large catalogues |
| `design-md/ollama/DESIGN.md` § *Layout* | Narrow 720/960px content widths and a home page treated as a rendered README. Evidence that minimal, content-first structure is a legitimate position for a public site |
| `design-md/nvidia/DESIGN.md` § *Layout*, § *Typography* | Dense multi-column technical content with hairline rules separating it; two-mode canvas where body content sits on the light surface |
| `design-md/ibm/DESIGN.md` § *Typography* | Light display weights and 0–4px corners as an enterprise-information register — restraint as an information-design signal |

## 12. Common mistakes

| Mistake | Correction |
|---|---|
| Marketing type scale on documentation | Cap display at 36–56px |
| Full-width prose | 680px measure, always |
| Answer buried under context | Answer first, detail second |
| Search as an afterthought | Primary nav above ~200 pages |
| Undated pages | Show last-updated on every page |
| Callout overuse | Four types, used sparingly |
| Sidebar losing state | Persist expansion and scroll |
| Documentation unusable on mobile | Test with real content on 375px |
| Version confusion | Prominent selector + a banner when viewing old docs |

## 13. Review checklist

[checklists/website-review.md](../checklists/website-review.md)

## 14. Template

[templates/DESIGN.general-website.md](../templates/DESIGN.general-website.md)
