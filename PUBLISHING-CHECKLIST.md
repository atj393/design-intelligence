# Publishing Checklist

For extracting this layer into an independent public repository.

**Nothing has been published, pushed, or committed.** No remote was created. That was outside the
scope of the work that produced this layer and requires a separate, explicit instruction.

---

## 1. Attribution and sources

- [ ] Source collection identified prominently in the README, with a link
- [ ] [ATTRIBUTION.md](ATTRIBUTION.md) included, unmodified in substance
- [ ] [SOURCES.md](SOURCES.md) included
- [ ] Relative `design-md/…` citations converted to links to the source repository, **or** a clear
      statement that they refer to it
- [ ] A note that citations reflect a specific state of the source repository, with the date or
      commit
- [ ] No claim that this layer supersedes or replaces the source collection

## 2. Licence

- [ ] MIT licence file present
- [ ] Original copyright notice preserved (2026 VoltAgent)
- [ ] Any additional contributors' copyright added without removing the original
- [ ] [LICENSING-CONSIDERATIONS.md](LICENSING-CONSIDERATIONS.md) included
- [ ] The MIT-covers-text-not-trademarks distinction stated where a reader will see it

## 3. Trademarks and non-affiliation

- [ ] No-affiliation statement in the README, not only in a sub-document
- [ ] Trademark acknowledgement present
- [ ] Brand names used **nominatively only** — in citations and research tables
- [ ] **No brand name in any normative rule.** Grep for it:

```bash
# Should return nothing outside citations, research/, and inventory files
grep -rn -iE '\b(stripe|linear|vercel|apple|nike|tesla|figma|notion)\b' \
  --include='*.md' . \
  | grep -v 'design-md/' | grep -v '^./research/' \
  | grep -v 'SOURCE-INVENTORY' | grep -v 'REPOSITORY-DISCREPANCIES'
```

- [ ] No brand name in the repository name, description, or topics
- [ ] No implication that any brand contributed, approved, or reviewed the material

## 4. Assets

- [ ] **No logos, wordmarks, or brand marks**
- [ ] **No screenshots of any website or product**
- [ ] **No font files**
- [ ] **No images at all** — verify:

```bash
find . -type f \( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' -o -name '*.gif' \
  -o -name '*.svg' -o -name '*.webp' -o -name '*.woff*' -o -name '*.ttf' -o -name '*.otf' \) \
  -not -path './.git/*'
```

- [ ] Markdown text only

## 5. Evidence integrity

**The most important section. Do not skip it.**

- [ ] Every category guide retains its **evidence-strength banner**
- [ ] The README's honest-limits section retained
- [ ] Synthesized guidance still labelled as synthesized throughout
- [ ] [VALIDATION-REPORT.md](VALIDATION-REPORT.md) included
- [ ] [REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) included, or its findings
      summarised with a pointer
- [ ] No recommendation upgraded from "reasoning" to "evidence" during editing

Four of eleven category guides are reasoning rather than corpus evidence. Published without that
stated, they become four confident documents making claims they cannot support — the exact failure
this layer was built to avoid.

## 6. Documentation completeness

- [ ] README explains purpose, audience, structure, workflow, and limits
- [ ] Every folder has a README index
- [ ] No unresolved `[[SET: ...]]` or `[[CHOOSE: ...]]` markers **outside** `templates/` (they are
      intentional there):

```bash
grep -rn '\[\[SET:\|\[\[CHOOSE:' --include='*.md' . | grep -v '/templates/'
```

- [ ] No `TODO`, `TBD`, `FIXME`, or "future work" placeholders
- [ ] No empty files
- [ ] No file consisting only of headings

## 7. Link integrity

- [ ] Every relative link resolves. Run:

```bash
python - <<'PY'
import os, re, glob
broken = []
for f in glob.glob('**/*.md', recursive=True):
    txt = open(f, encoding='utf-8', errors='replace').read()
    for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', txt):
        if target.startswith(('http', 'mailto:')):
            continue
        p = target.split('#')[0]
        if p and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), p))):
            broken.append((f, label, target))
print(f'{len(broken)} broken')
for b in broken:
    print(' ', b)
PY
```

- [ ] External links checked for reachability
- [ ] No links to local absolute paths (`d:\`, `/Users/`, `C:\`)
- [ ] No links into a private repository or internal system

## 8. Consistency

- [ ] Filenames are lowercase-kebab or CONSISTENT-CAPS, applied uniformly per folder
- [ ] Heading levels consistent across comparable documents
- [ ] Table column ordering consistent across comparable tables
- [ ] Terminology consistent: one name per concept
- [ ] Numeric values agree across the foundation, category guides, comparison matrix, and templates

The last item is the one that drifts. Spot-check density values for one category across all four
document types before publishing.

## 9. Temporary and working files

- [ ] No extraction or analysis scripts (they were intentionally never committed)
- [ ] No `scratchpad/`, `tmp/`, `notes/`, or `.remember/` directories
- [ ] No editor directories (`.vscode/`, `.idea/`) unless deliberate, in which case add a
      `.gitignore` entry
- [ ] `PROGRESS.md` — keep it (it documents method honestly) or remove it deliberately, but do not
      leave it half-updated
- [ ] No personal paths, usernames, hostnames, or email addresses:

```bash
grep -rn -iE "$USER|C:\\\\Users|/Users/|@[a-z0-9.-]+\.(com|de|org|net)" --include='*.md' .
```

## 10. Repository setup

- [ ] Name does not include a brand name
- [ ] Description states it is a derived synthesis
- [ ] Topics relevant and free of brand names
- [ ] `LICENSE` at the root
- [ ] `CONTRIBUTING.md` explaining the evidence discipline — state your evidence, distinguish
      observation from reasoning, do not promote a single source's choice to a universal rule
- [ ] Issue templates, if used, ask for evidence
- [ ] `.gitignore` covering editor and OS files

## 11. Final read-through

- [ ] Read the README as a first-time visitor. Is the purpose clear in thirty seconds?
- [ ] Read one weak-evidence category guide. Is its limitation unmissable?
- [ ] Read one template. Could someone actually use it?
- [ ] Read one prompt. Would it produce reviewable output?
- [ ] Confirm nothing reads as an official brand design system
- [ ] Confirm no marketing language crept in

## 12. Before pushing

- [ ] `git status` — only intended files
- [ ] `git diff --stat` — reviewed
- [ ] No secrets, tokens, or credentials anywhere
- [ ] Commit message describes the work accurately
- [ ] **Explicit authorization to publish obtained** — publishing is outward-facing and
      irreversible in effect; a link, once indexed, may persist after deletion

---

## Deliberately out of scope

These were not done and require separate instructions:

- Creating a remote repository
- Pushing any commit
- Publishing to any package registry
- Creating a website or documentation site
- Announcing or submitting the work anywhere
- Contacting any referenced brand

## If publishing is declined

The layer remains fully usable in place. It is self-contained inside
[`design-intelligence/`](.), links only within this repository, and requires no build step.
Nothing here depends on being published.
