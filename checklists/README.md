# Review Checklists

Working checklists for reviewing an implementation. Designed to be worked down in order, not read.

**Folder note:** the prescribed documentation architecture named `categories/`, `templates/`,
`prompts/`, and `research/`. Checklists were required deliverables with no named home. Inlining
five of them into their guides would make the guides harder to use as a review instrument — a
reviewer wants a page they can work down. Rationale:
[../ASSUMPTIONS.md](../ASSUMPTIONS.md) D-06.

---

| Checklist | Covers |
|---|---|
| [foundation-review.md](foundation-review.md) | Any product — tokens, scales, states, accessibility |
| [conversational-ai-review.md](conversational-ai-review.md) | Chat and assistant interfaces |
| [dashboard-review.md](dashboard-review.md) | Dashboards, admin, analytics |
| [commercial-platform-review.md](commercial-platform-review.md) | Multi-role platforms |
| [website-review.md](website-review.md) | Marketing, informational, editorial |

**Run [foundation-review.md](foundation-review.md) first, always.** Category checklists cover what
is specific to their category and assume the foundation has been checked.

## The fast pass

If you have ten minutes, these eight checks find most real problems. Full detail in
[../ANTI-PATTERNS.md](../ANTI-PATTERNS.md) Part 4.

1. **Greyscale the OS.** Is every status still distinguishable? Secondary text still visible?
2. **Complete one task with the keyboard only.** Focus always visible? Any traps?
3. **Force empty, loading, error, and permission-denied.** Are they designed?
4. **Open at 375px.** Re-ranked, or just compressed?
5. **Search the diff** for hex values and literal spacing numbers.
6. **Count** button variants, card treatments, and radius values in use.
7. **Check density coherence** — do spacing, control height, and type size agree?
8. **Enable `prefers-reduced-motion`.** Does everything still work and still communicate?

## Using these with an agent

Pair a checklist with the matching prompt:

| Checklist | Prompt |
|---|---|
| foundation-review | [09-review-against-design-md.md](../prompts/09-review-against-design-md.md) |
| Any, accessibility section | [12-test-accessibility.md](../prompts/12-test-accessibility.md) |
| Any, responsive section | [11-test-responsive.md](../prompts/11-test-responsive.md) |

Ask for findings first, fixes second. A single "fix everything" pass produces an unreviewable diff.

## Severity

| Level | Meaning | Action |
|---|---|---|
| **Blocker** | Accessibility failure, broken state, data risk | Fix before merge |
| **High** | System violation users will notice | Fix before release |
| **Medium** | Inconsistency | Schedule |
| **Low** | Polish | Backlog |

Any unchecked accessibility box is a **blocker**, not a medium.
