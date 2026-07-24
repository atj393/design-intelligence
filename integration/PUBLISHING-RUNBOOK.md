# Publishing Runbook

Exact commands to publish this layer as its own repository, so cloud sessions and other machines can
reach it.

**Read [../PUBLISHING-CHECKLIST.md](../PUBLISHING-CHECKLIST.md) first.** It is the pre-flight check;
this file is the procedure.

---

## The constraint you need to know first

This layer currently lives inside a **checkout of someone else's repository**:

```
$ git remote -v
origin  https://github.com/VoltAgent/awesome-design-md.git
```

**You cannot push here.** Publishing means one of three things:

| Option | What it is | When to choose it |
|---|---|---|
| **1. New standalone repo** | Extract `design-intelligence/` into its own repo under your account | **Recommended.** Clean history, clean licence story, independent versioning |
| **2. Fork + branch** | Fork the upstream repo, push the layer to a branch on your fork | You intend to open a pull request upstream |
| **3. Don't publish** | Keep it local; vendor into repos that need it | Solo work, or the content is not for public consumption |

Option 3 is a legitimate answer. Vendoring (mode B in
[README.md](README.md)) already solves cloud access without publishing anything.

---

## Option 1 — New standalone repo (recommended)

### Step 1 — Pre-flight

```bash
cd <this-repo>/design-intelligence

# All automatable publishing checks
python - <<'PY'
import os, re, glob
bad = []
n = 0
for f in glob.glob('**/*.md', recursive=True):
    t = open(f, encoding='utf-8', errors='replace').read()
    for label, tgt in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', t):
        if tgt.startswith(('http', 'mailto:')):
            continue
        p = tgt.split('#')[0]
        n += 1
        if p and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), p))):
            bad.append((f, tgt))
print(f'links: {n} checked, {len(bad)} broken')
for b in bad:
    print('  BROKEN', b)
PY

# No binary assets, no non-markdown files
find . -type f ! -name '*.md' | grep -v integration/ || echo "assets: none"

# No unresolved template markers outside templates/
grep -rn '\[\[SET:\|\[\[CHOOSE:' --include='*.md' . | grep -v '/templates/' \
  | grep -vE 'marker|placeholder|Resolve every|Unresolved' || echo "markers: clean"

# No personal paths
grep -rniE "$USER|C:\\\\Users|/Users/|AppData" --include='*.md' . \
  | grep -v PUBLISHING || echo "paths: clean"
```

All four must come back clean. Fix anything that does not.

### Step 2 — Stage the content

Copy to a fresh directory outside both repos. Do **not** `git init` inside the existing checkout —
that creates a nested repo and confuses everything.

```bash
STAGE="$HOME/design-intelligence-publish"
rm -rf "$STAGE" && mkdir -p "$STAGE"
cp -r <this-repo>/design-intelligence/. "$STAGE/"
cd "$STAGE"

# Build-log and session provenance are not useful to consumers
rm -f PROGRESS.md

ls -la
```

Decide on `PROGRESS.md`. Keeping it is honest about method; removing it makes the repo about
*using* the layer rather than how it was built. Either is defensible — just be deliberate.

### Step 3 — Licence and attribution

**Required.** The upstream repo is MIT, copyright VoltAgent, and this is derived work.

```bash
# Carry the upstream licence forward, unmodified
cp <this-repo>/LICENSE "$STAGE/LICENSE"
```

Then append your own copyright line **without removing the original**:

```
MIT License

Copyright (c) 2026 VoltAgent
Copyright (c) 2026 Alexis Toby Johnson
```

Verify `ATTRIBUTION.md` and `LICENSING-CONSIDERATIONS.md` came across — they carry the
no-affiliation and trademark statements that make nominative brand use defensible. **Do not remove
them.**

### Step 4 — Rewrite source citations

This is the step people forget. The layer cites sources as `design-md/<name>/DESIGN.md` — relative
paths that resolve in the upstream repo and **point at nothing** in a standalone one.

```bash
cd "$STAGE"
python - <<'PY'
import glob, re
UP = "https://github.com/VoltAgent/awesome-design-md/blob/main/design-md"
n = 0
for f in glob.glob('**/*.md', recursive=True):
    s = open(f, encoding='utf-8').read()
    # `design-md/foo/DESIGN.md` -> markdown link to the upstream file
    def link(m):
        name = m.group(1)
        label = '`design-md/' + name + '/DESIGN.md`'
        href = UP + '/' + name + '/DESIGN.md'
        return '[' + label + ']' + '(' + href + ')'
    new = re.sub(r'`design-md/([a-z0-9._-]+)/DESIGN\.md`', link, s)
    if new != s:
        open(f, 'w', encoding='utf-8').write(new)
        n += 1
print(f'rewrote citations in {n} files')
PY
```

Also fix the relative links that pointed at the parent repo — `../design-md/` and `../README.md`
and `../LICENSE`:

```bash
grep -rn '\](\.\./' --include='*.md' . | head -20
```

Repoint each to the upstream GitHub URL, then re-run the Step 1 link check. It must come back
`0 broken`.

### Step 5 — Add a note about the source snapshot

Citations now reference a moving target. Add this near the top of `SOURCES.md`:

```markdown
> **Snapshot note.** Source citations refer to the upstream collection as of
> commit `<SHA>` (`<DATE>`). The upstream collection evolves; a cited section may have
> moved or changed since.
```

Get the SHA:

```bash
cd <this-repo> && git rev-parse --short HEAD && git log -1 --format=%cs
```

### Step 6 — Initialise and push

```bash
cd "$STAGE"
git init -b main
git add -A
git commit -m "Design intelligence: derived design guidance layer

Category-based design systems, decision frameworks, DESIGN.md templates,
agent prompts and review checklists, synthesized from the Awesome DESIGN.md
collection (74 source analyses).

Derived work. Not affiliated with or endorsed by any brand referenced in the
source research. See ATTRIBUTION.md and LICENSING-CONSIDERATIONS.md."
```

Create the empty repo on GitHub first — **no README, no licence, no .gitignore**, or the first push
will conflict. Then:

```bash
git remote add origin https://github.com/<you>/design-intelligence.git
git push -u origin main
```

If `gh` is installed it is one command instead:

```bash
gh repo create design-intelligence --public --source=. --remote=origin --push \
  --description "Category-based design guidance for AI-assisted product development"
```

`gh` is **not currently installed on this machine** — use the web UI plus `git push`.

### Step 7 — Wire it up

```bash
# Point the local skill at the published copy as a fallback
cat > "$HOME/.claude/skills/design-intelligence/scripts/di_config.json" <<'JSON'
{
  "local_paths": [],
  "url": "https://raw.githubusercontent.com/<you>/design-intelligence/main"
}
JSON

python "$HOME/.claude/skills/design-intelligence/scripts/di.py" where
```

Local still wins; the URL is the fallback when no local copy exists — which is exactly the cloud-
session case.

### Step 8 — Verify from a cloud session

The only test that matters. In a cloud session with no local checkout, ask an agent to fetch:

```
https://raw.githubusercontent.com/<you>/design-intelligence/main/AGENT-ENTRY.md
```

Confirm it (a) fetches, (b) follows the routing table, and (c) **states the evidence strength** of
whichever category it lands on. If (c) fails, the banner is not surviving the trip and cloud users
will mistake reasoning for evidence.

---

## Option 2 — Fork and branch

For contributing upstream rather than running an independent copy.

```bash
# Fork via the GitHub web UI, then:
cd <this-repo>
git remote add mine https://github.com/<you>/awesome-design-md.git
git checkout -b design-intelligence
git add design-intelligence README.md
git commit -m "Add design-intelligence: derived design guidance layer"
git push -u mine design-intelligence
```

Raw URLs then look like:

```
https://raw.githubusercontent.com/<you>/awesome-design-md/design-intelligence/design-intelligence/AGENT-ENTRY.md
```

**Advantages:** citations keep working unchanged (`design-md/` is right there); no licence
restructuring needed.
**Disadvantages:** awkward URLs; the layer is tied to upstream's history; and if you intend a pull
request, note that upstream's `CONTRIBUTING.md` asks for an issue first and states that
`DESIGN.md` pull requests are not accepted — so discuss before investing in it.

---

## Post-publication maintenance

| Trigger | Action |
|---|---|
| Upstream adds sources | Re-run the analysis; update distributions and the source inventory |
| A template gets build-tested | Update `research/TEMPLATE-VALIDATION.md`, then the template |
| User validation happens | Add `§3` to `research/WEAK-GUIDE-REVIEW.md`; **upgrade the evidence banner** |
| Guidance found wrong in practice | Fix the guide, and record why in the validation report |

**Version deliberately.** Tag releases so a project can pin guidance:

```bash
git tag -a v1.0.0 -m "Initial release: 11 categories, 10 templates, 12 prompts"
git push --tags
```

Then a project can vendor from a tag rather than `main`, and guidance will not shift mid-build.

---

## Do not publish if

- Any category guide has lost its evidence banner. Four of eleven guides are reasoning rather than
  evidence; published without that stated, they become four confident documents making claims they
  cannot support. This is the single most important thing to preserve.
- The link check does not return `0 broken`.
- `ATTRIBUTION.md` or `LICENSING-CONSIDERATIONS.md` are missing.
- Any brand logo, screenshot, or font file has crept in.
- You have not decided what to do about `PROGRESS.md`.
