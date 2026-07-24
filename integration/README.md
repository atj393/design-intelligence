# Integration

How to use this layer from other projects, other machines, cloud sessions, and other agents.

---

## Pick your deployment mode

| Mode | Works in | Setup | Travels with repo | Needs network |
|---|---|---|---|---|
| **A. Personal skill** | Every project on one machine | Once | No | No |
| **B. Vendored copy** | The repo it is copied into, anywhere | Per repo | **Yes** | No |
| **C. Project skill** | The repo it is copied into, anywhere | Per repo | **Yes** | No |
| **D. Published repo** | Anywhere, incl. cloud sessions | Once | No | Yes |

**Recommended combination: A + C.** Personal skill for day-to-day local work; project skill
committed into repos that need it in cloud sessions or by teammates.

B and C are usually done together — C is the skill, B is the content it reads.

---

## Mode A — Personal skill (local, all projects)

Already installed if you ran the setup:

```
~/.claude/skills/design-intelligence/
├── SKILL.md
└── scripts/
    ├── di.py
    └── di_config.json
```

Verify from any directory:

```bash
python "$HOME/.claude/skills/design-intelligence/scripts/di.py" check
```

**Entry point:** the skill. From any project, just describe the work — "build an admin table",
"review this UI", "set up a design system" — and it loads. Or invoke it explicitly:
`/design-intelligence`.

**Limitation:** `~/.claude/skills/` is local to one machine. It does not reach cloud sessions or
teammates. Use B/C/D for those.

---

## Mode B — Vendor into a repo (cloud-safe, offline, no network)

Copies the layer into the target repo as `.design-intelligence/` and commits it. The most robust
option: it works in cloud sessions, on CI, on a teammate's machine, and with no network.

```bash
python <source>/design-intelligence/integration/vendor.py /path/to/target-repo
```

Adds:

```
target-repo/
├── .design-intelligence/          the layer (markdown only, ~1 MB)
└── .claude/skills/design-intelligence/SKILL.md    (with --with-skill)
```

`di.py` finds `.design-intelligence/` automatically — resolution step 3 — so no configuration is
needed in the target repo.

**Cost:** ~70 markdown files in the repo. **Benefit:** zero-dependency, works everywhere, and the
version is pinned to whatever you vendored, so guidance does not shift under a project mid-build.

Re-run the same command to update. Use `--check` first to see what would change.

---

## Mode C — Project-level skill (travels with the repo)

Put the skill inside the repo so it auto-loads for anyone working in it, including cloud sessions:

```
target-repo/.claude/skills/design-intelligence/SKILL.md
```

`vendor.py --with-skill` does this and rewrites the paths to point at the vendored copy.

Commit it. Anyone opening that repo in Claude Code — local or cloud — gets the skill without
installing anything.

---

## Mode D — Publish and fetch (cloud, no vendoring)

Publish the layer as its own public repository, then point `di.py` at the raw URL.

Step-by-step: [PUBLISHING-RUNBOOK.md](PUBLISHING-RUNBOOK.md).

After publishing, set the URL once:

```jsonc
// ~/.claude/skills/design-intelligence/scripts/di_config.json
{ "url": "https://raw.githubusercontent.com/atj393/design-intelligence/main" }
```

Then `di.py` falls back to the URL whenever no local copy is found, and the agent fetches
individual files with its own web-fetch tool.

**Tradeoff:** no repo bloat, always current — but needs network, and guidance can change under a
project between sessions. Vendor (B) when you want reproducibility; publish (D) when you want
currency.

---

## Other agents

### ChatGPT Codex, Cursor, Copilot, Gemini CLI, Aider

These read `AGENTS.md` (or an equivalent instruction file) rather than Claude skills. Use:

```bash
cp <source>/design-intelligence/integration/AGENTS.design-intelligence.md /path/to/repo/AGENTS.md
# or append to an existing AGENTS.md
cat <source>/design-intelligence/integration/AGENTS.design-intelligence.md >> /path/to/repo/AGENTS.md
```

`vendor.py --with-agents` does this and points the paths at the vendored copy.

That file is self-contained: it carries the non-negotiables and the routing table inline, so an
agent that never opens another file still gets the critical rules.

### Any agent with no file convention

Paste [PROMPT-BOOTSTRAP.md](PROMPT-BOOTSTRAP.md) at the start of the conversation. It is one
screen, designed to be pasted.

---

## Project CLAUDE.md snippet

To make the layer authoritative in a specific project — beyond skill triggering — add
[CLAUDE-MD-SNIPPET.md](CLAUDE-MD-SNIPPET.md) to that project's `CLAUDE.md`. Useful when a project
has its own `DESIGN.md` that must win conflicts, and you want that stated in project memory rather
than relying on the skill alone.

---

## Which mode for which situation

| Situation | Mode |
|---|---|
| Solo, one machine, many projects | **A** |
| Team repo, everyone should get it | **B + C**, committed |
| Cloud sessions on claude.ai/code | **B + C**, or **D** |
| Regulated project needing reproducible guidance | **B** — pin the version |
| Many repos, want one source of truth | **A** locally, **D** for cloud |
| Using Codex or Cursor | **B** + `AGENTS.md` |
| One-off conversation, any agent | **PROMPT-BOOTSTRAP.md** |

---

## Verifying an integration

Whatever the mode, confirm it works before relying on it:

```bash
# 1. Does the layer resolve?
python <di.py> where

# 2. Is it complete?
python <di.py> check          # expects 11+ categories, 10+ templates

# 3. Does routing work?
python <di.py> route "your product description"
```

Then, in a fresh session in the target project, ask for something design-related and check that the
agent (a) loads the skill, (b) reads `AGENT-ENTRY.md`, and (c) **states the evidence strength** of
whichever category it routes to. If it skips (c), it is not reading carefully — the evidence banner
is the part that keeps synthesized guidance from being mistaken for fact.
