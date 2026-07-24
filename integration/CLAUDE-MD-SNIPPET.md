# CLAUDE.md Snippet

Add this to a project's `CLAUDE.md` when you want the design layer to be **project memory**, not
just a skill that triggers on keywords. Useful when the project has its own `DESIGN.md` that must
win conflicts.

Copy the block below, adjust the path for your deployment mode, and paste into the project's
`CLAUDE.md`.

---

## For a vendored copy (mode B — recommended for team repos)

```markdown
# Design and UI work

This project's design system is defined in `DESIGN.md` at the repo root. **It is authoritative** —
where it conflicts with any general guidance, `DESIGN.md` wins.

For anything it does not cover, use the vendored design-intelligence layer:

- **Entry point:** `.design-intelligence/AGENT-ENTRY.md` — read this first; it routes by task and
  product type
- **Primary category:** `.design-intelligence/categories/<CATEGORY>.md`
- **Review before claiming done:** `.design-intelligence/checklists/foundation-review.md`

Reading order for any UI task: this project's code → `.design-intelligence/COMMON-FOUNDATION.md` →
the category guide → this project's `DESIGN.md`.

Non-negotiable in this project:
- Semantic tokens only. No hard-coded colours, spacing, radii, or font sizes.
- All eight interaction states and all seven data states — including empty, loading, error, and
  permission-denied. Not just the happy path.
- Accessibility floor met as you write, not in a later pass.
- Report any value you had to invent — that is a gap in `DESIGN.md`, and I want it recorded there.
- Never break working functionality to achieve a visual change.
```

## For the local personal skill (mode A — solo work)

```markdown
# Design and UI work

This project's design system is defined in `DESIGN.md` at the repo root. **It is authoritative.**

For anything it does not cover, invoke the `design-intelligence` skill. Its entry point routes by
task and product type; read only what it points you to.

Primary category for this project: **<CATEGORY>**
Density mode: **<compact | default | spacious>**

Non-negotiable: semantic tokens only · all eight interaction states · all seven data states ·
accessibility floor met as you write · report invented values · never break working functionality
for a visual change.
```

## For a published source (mode D — cloud sessions)

```markdown
# Design and UI work

This project's design system is defined in `DESIGN.md` at the repo root. **It is authoritative.**

General design guidance: fetch
`https://raw.githubusercontent.com/atj393/design-intelligence/main/AGENT-ENTRY.md`
and follow its routing. Read only the two or three files it points to.

Primary category for this project: **<CATEGORY>**
Density mode: **<compact | default | spacious>**

Non-negotiable: semantic tokens only · all eight interaction states · all seven data states ·
accessibility floor met as you write · report invented values · never break working functionality
for a visual change.
```

---

## What to fill in

| Placeholder | Get it from |
|---|---|
| `<CATEGORY>` | `di.py route "<your product description>"`, or `CATEGORY-SELECTION.md` |
| `<density>` | Visit frequency: daily → compact, weekly → default, rare → spacious |
| *(published)* | Already live at `atj393/design-intelligence` |

## Why bother, if the skill already triggers?

Three reasons:

1. **It states the precedence order.** The skill does not know that *this* project's `DESIGN.md`
   outranks it. `CLAUDE.md` says so explicitly.
2. **It pins the category and density.** Otherwise every session re-derives them, and may derive
   them differently.
3. **It applies to agents that never load the skill** — a session that goes straight to code without
   a design-flavoured prompt still reads `CLAUDE.md`.

Keep it short. `CLAUDE.md` is loaded into every session in that project, so it competes for
attention with everything else.
