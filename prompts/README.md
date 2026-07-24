# Agent Prompt Library

Twelve reusable prompts. Copy one, fill the `<>` placeholders, paste it to your agent.

Read [../AI-AGENT-GUIDE.md](../AI-AGENT-GUIDE.md) first — it defines the reading order and the
non-negotiable behaviours every prompt below assumes.

---

## Creation

| Prompt | Use for |
|---|---|
| [01-new-design-system.md](01-new-design-system.md) | Deriving a `DESIGN.md` for a new product |
| [02-new-page.md](02-new-page.md) | Adding a page or view to an existing application |
| [04-chatbot-interface.md](04-chatbot-interface.md) | Conversational or assistant interface |
| [05-marketing-website.md](05-marketing-website.md) | Marketing or conversion pages |
| [06-multi-role-platform.md](06-multi-role-platform.md) | Role-based commercial platform |
| [07-admin-dashboard.md](07-admin-dashboard.md) | Dashboard or administration surface |
| [08-spatial-interface.md](08-spatial-interface.md) | Map, spatial, or 3D interface |

## Correction

| Prompt | Use for |
|---|---|
| [03-redesign-inconsistent-ui.md](03-redesign-inconsistent-ui.md) | Bringing an inconsistent interface onto a system |
| [10-refactor-to-tokens.md](10-refactor-to-tokens.md) | Replacing hard-coded values with tokens |

## Verification

| Prompt | Use for |
|---|---|
| [09-review-against-design-md.md](09-review-against-design-md.md) | Auditing code against `DESIGN.md` |
| [11-test-responsive.md](11-test-responsive.md) | Verifying responsive behaviour |
| [12-test-accessibility.md](12-test-accessibility.md) | Verifying accessibility |

---

## What every prompt enforces

Each prompt contains all five of these, because omitting any one is a known failure mode:

1. **Inspect first, report what you found** — before generating anything.
2. **Reuse existing components** — extend rather than duplicate.
3. **Never break working functionality** for a visual change.
4. **Implement all states** — interaction states and data states, not just the happy path.
5. **Report assumptions, deviations, invented values, and unresolved decisions.**

## Adapting these

Add project specifics — framework, component library, file paths, naming conventions. Do not
remove the inspect step or the report requirement; they are what make the output reviewable.

For repeated use, paste the prompt into your project's `CLAUDE.md`, `AGENTS.md`, or equivalent so
it applies by default.
