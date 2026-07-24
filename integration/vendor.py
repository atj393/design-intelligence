#!/usr/bin/env python3
"""Vendor the design-intelligence layer into a target repository.

Copies the layer to <target>/.design-intelligence/ so it travels with the repo — works in
cloud sessions, on CI, on a teammate's machine, with no network and no configuration.

Usage:
    vendor.py <target-repo> [options]

Options:
    --with-skill    also install <target>/.claude/skills/design-intelligence/SKILL.md
    --with-agents   also write/append <target>/AGENTS.md  (Codex, Cursor, Copilot, Aider)
    --check         report what would change; write nothing
    --force         overwrite an existing vendored copy without prompting

Examples:
    vendor.py ../my-app --with-skill --with-agents
    vendor.py ../my-app --check
"""
import os
import shutil
import sys

SRC_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../design-intelligence
VENDOR_DIRNAME = ".design-intelligence"
MARKER = "AGENT-ENTRY.md"

# Excluded from the vendored copy: build-log and provenance files that are about how the layer
# was made, not how to use it. Keeps the vendored footprint about usage.
EXCLUDE_FILES = {"PROGRESS.md"}
EXCLUDE_DIRS = {"integration"}          # the target does not need to re-vendor onward


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


UPSTREAM = "https://github.com/VoltAgent/awesome-design-md"

# Links that point OUT of the layer into its parent repo. They resolve in the source checkout
# and break in a vendored copy, so rewrite them to absolute upstream URLs.
PARENT_LINK_REWRITES = {
    "](../design-md/)": f"]({UPSTREAM}/tree/main/design-md)",
    "](../README.md)": f"]({UPSTREAM}/blob/main/README.md)",
    "](../LICENSE)": f"]({UPSTREAM}/blob/main/LICENSE)",
}

PROVENANCE = """<!-- Vendored copy of the design-intelligence layer.
     Source: {upstream}
     Do not edit here — edit upstream and re-run integration/vendor.py.
     Citations of the form `design-md/<name>/DESIGN.md` refer to:
     {upstream}/tree/main/design-md
-->
"""


def rewrite(text, rel):
    """Fix parent-repo links and stamp provenance on the entry point."""
    for old, new in PARENT_LINK_REWRITES.items():
        text = text.replace(old, new)
    if rel == MARKER:
        text = PROVENANCE.format(upstream=UPSTREAM) + "\n" + text
    return text


def collect():
    """Return list of (abs_src, rel_dest) markdown files to vendor."""
    out = []
    for dirpath, dirnames, filenames in os.walk(SRC_ROOT):
        rel_dir = os.path.relpath(dirpath, SRC_ROOT)
        top = rel_dir.split(os.sep)[0] if rel_dir != "." else "."
        if top in EXCLUDE_DIRS:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            if rel_dir == "." and fn in EXCLUDE_FILES:
                continue
            src = os.path.join(dirpath, fn)
            rel = os.path.normpath(os.path.join(rel_dir, fn)) if rel_dir != "." else fn
            out.append((src, rel))
    return sorted(out, key=lambda x: x[1])


SKILL_TEMPLATE = """---
name: design-intelligence
description: Design system guidance for this repository — category-based design decisions, DESIGN.md templates, and UI review checklists, vendored into .design-intelligence/. Use this skill whenever the user asks to build, design, restyle, or review any user interface in this project; create or update a DESIGN.md; choose colours, typography, spacing, or density; or audit UI for accessibility, responsive behaviour, or design-token compliance.
---

# Design Intelligence (vendored)

This repository carries its own copy of the design-intelligence layer at
`.design-intelligence/`. No network or external setup is needed.

## Start here

Read **`.design-intelligence/AGENT-ENTRY.md`** first. It routes by task and by product type, and
carries the ten non-negotiables. Read it, then read only the two or three files it points you to —
the layer is large and most of it will not be about your task.

## Reading order (strict — later overrides earlier)

1. This project's own code — existing components, tokens, conventions
2. `.design-intelligence/COMMON-FOUNDATION.md`
3. One category guide from `.design-intelligence/categories/`
4. Supporting category guides, if this product has several surfaces
5. **This project's `DESIGN.md`** — authoritative, wins every conflict

## Non-negotiables

1. Inspect before generating; report what already exists
2. Reuse before creating; extend a near-miss rather than duplicating
3. Never break working functionality for a visual change
4. Semantic tokens only — a value with no token is a `DESIGN.md` gap, report it
5. All eight interaction states: default, hover, focus-visible, active, disabled, loading,
   selected, error
6. All seven data states: first-run empty, filtered-empty, initial loading, refresh (keeps data),
   partial, error with retry, permission denied
7. Accessibility floor: body >=4.5:1, large/UI >=3:1, visible focus, >=44px touch, keyboard
   operable, never colour alone
8. Dark mode is derived, not inverted. Never lighten a button fill while keeping a white label
9. Category sets density, navigation, and components — not visual tone
10. Report assumptions, deviations, invented values, and unresolved decisions

## Evidence honesty

Every category guide states its evidence strength at the top. The source corpus is ~90% marketing
websites, so dashboard, conversational, multi-role, analytics, and spatial guidance is **reasoning,
not evidence**. Relay that to the user when it applies to their product.
"""


def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    target = os.path.abspath(args[0])
    with_skill = "--with-skill" in args
    with_agents = "--with-agents" in args
    check_only = "--check" in args
    force = "--force" in args

    if not os.path.isdir(target):
        die(f"target is not a directory: {target}")
    if not os.path.isfile(os.path.join(SRC_ROOT, MARKER)):
        die(f"source does not look like the layer (no {MARKER}): {SRC_ROOT}")
    if os.path.abspath(target) == os.path.abspath(os.path.dirname(SRC_ROOT)):
        die("target is the source repository; nothing to vendor")

    files = collect()
    dest_root = os.path.join(target, VENDOR_DIRNAME)
    existed = os.path.isdir(dest_root)

    print(f"source: {SRC_ROOT}")
    print(f"target: {dest_root}")
    print(f"files:  {len(files)} markdown")
    if existed:
        print("note:   vendored copy already exists — it will be replaced")

    if check_only:
        print("\n--check: nothing written. Would copy:")
        for _, rel in files[:12]:
            print(f"  {VENDOR_DIRNAME}/{rel}")
        if len(files) > 12:
            print(f"  ... and {len(files) - 12} more")
        if with_skill:
            print(f"  .claude/skills/design-intelligence/SKILL.md")
        if with_agents:
            print(f"  AGENTS.md  (append)")
        return 0

    if existed and not force:
        reply = input("Replace existing vendored copy? [y/N] ").strip().lower()
        if reply != "y":
            print("aborted")
            return 1

    if existed:
        shutil.rmtree(dest_root)
    rewritten = 0
    for src, rel in files:
        dst = os.path.join(dest_root, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, encoding="utf-8") as f:
            text = f.read()
        new = rewrite(text, rel)
        if new != text:
            rewritten += 1
        with open(dst, "w", encoding="utf-8", newline="") as f:
            f.write(new)
    print(f"\nwrote {len(files)} files to {VENDOR_DIRNAME}/")
    print(f"rewrote parent-repo links in {rewritten} files")

    if with_skill:
        sk_dir = os.path.join(target, ".claude", "skills", "design-intelligence")
        os.makedirs(sk_dir, exist_ok=True)
        with open(os.path.join(sk_dir, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(SKILL_TEMPLATE)
        print("wrote .claude/skills/design-intelligence/SKILL.md")

    if with_agents:
        agents_src = os.path.join(SRC_ROOT, "integration", "AGENTS.design-intelligence.md")
        if not os.path.isfile(agents_src):
            print("warn: AGENTS.design-intelligence.md not found; skipped", file=sys.stderr)
        else:
            with open(agents_src, encoding="utf-8") as f:
                block = f.read()
            agents_dst = os.path.join(target, "AGENTS.md")
            if os.path.isfile(agents_dst):
                with open(agents_dst, encoding="utf-8") as f:
                    current = f.read()
                if "design-intelligence" in current:
                    print("AGENTS.md already references design-intelligence; left unchanged")
                else:
                    with open(agents_dst, "a", encoding="utf-8") as f:
                        f.write("\n\n" + block)
                    print("appended to AGENTS.md")
            else:
                with open(agents_dst, "w", encoding="utf-8") as f:
                    f.write(block)
                print("wrote AGENTS.md")

    print("\nNext:")
    print(f"  1. Verify:  cd {target} && python -c \"import os;print(os.path.isfile('.design-intelligence/{MARKER}'))\"")
    print("  2. Commit the vendored files so they travel with the repo.")
    print("  3. In a fresh session, ask for something design-related and confirm the agent reads")
    print(f"     .design-intelligence/{MARKER} and states the evidence strength of its category.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
