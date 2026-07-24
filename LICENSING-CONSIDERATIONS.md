# Licensing Considerations

**This is not legal advice.** It is a description of what the licence in this repository does and
does not cover, written so that anyone reusing or republishing this material understands the
distinction. For an actual legal position, consult a qualified professional.

---

## 1. What the licence actually says

Verified by reading [`LICENSE`](../LICENSE) in this repository:

| | |
|---|---|
| Licence | MIT |
| Copyright | 2026 VoltAgent |
| Grants | Use, copy, modify, merge, publish, distribute, sublicense, sell |
| Requires | The copyright and permission notice preserved in copies |
| Provides | No warranty; no liability |

MIT is permissive and short. It is also **only capable of licensing what the licensor owns.**

## 2. The distinction that matters

This is the whole point of this document.

| Covered by the repository's MIT licence | **Not** covered by it |
|---|---|
| The prose of the `DESIGN.md` files | Third-party trademarks and brand names |
| The organisation and structure of the collection | Brand logos and wordmarks |
| The observations and analysis in the text | Proprietary typefaces named in the text |
| This derived layer's text and structure | Copyrighted photography and illustration |
| The templates, checklists, and prompts here | Trade dress and overall visual identity |
| | Any brand's right to control association with its marks |

**MIT cannot license someone else's trademark**, because the licensor does not own it. A permissive
licence on a *description* of a brand's design language grants nothing in respect of the brand
itself.

**Practical consequence:** you may freely use, modify, and redistribute the text of this repository.
That does not grant you permission to use a described brand's name, logo, or identity in a way that
implies association, or to license a typeface you have not licensed.

## 3. Design values, tokens, and functional facts

**Individual measurements are generally not protectable as such.** That a documented interface uses
16px body text, an 8px grid, a 1280px container, or a particular hex value is a functional fact.
Facts are not copyrightable, and this is why the whole `DESIGN.md` concept is workable.

**Where care is warranted:**

| Situation | Concern |
|---|---|
| Reproducing a *complete* system — palette, type, spacing, components, layout together | Aggregate reproduction may implicate trade dress even where each value is unprotectable |
| Combined with brand naming or marks | Substantially raises the risk of confusion and implied association |
| Presented as a brand's official system | Misrepresentation, independent of copyright |
| Using a named proprietary typeface | A **separate licence** is required from the foundry. Naming a font in a document does not license it |

**The safe position, and the one this layer takes:** adopt *structural principles* — how a surface
ladder carries hierarchy, how density relates to visit frequency, how tracking scales with display
size. Derive your own specific values. That is portable, defensible, and produces better design than
copying, because the values then fit your product.

## 4. Typefaces specifically

The most common practical trap.

- **Naming a typeface is not licensing it.** 59 of 74 source files publish a
  `Note on Font Substitutes`, which is the correct handling — it makes the documented system usable
  by someone who cannot license the original.
- Proprietary and custom brand faces are almost never redistributable. Several source files state
  their subject's face is not publicly distributed.
- **If your product uses a licensed face, verify your licence covers your use** — web embedding,
  app embedding, and self-hosting are frequently separate grants with separate fees.
- **Every template in this layer requires a substitution note** for exactly this reason. A design
  system built on a font nobody can license is decoration, not a system.

## 5. Trademark use

The source collection and this layer both use brand names **nominatively** — to identify the subject
of an analysis. That is the narrow, generally-accepted use.

**What keeps nominative use defensible:**

| Do | Do not |
|---|---|
| Use the name only to identify what is being discussed | Use logos, wordmarks, or stylised marks |
| Use no more of the mark than necessary | Suggest sponsorship, endorsement, or affiliation |
| State the absence of affiliation clearly | Present the material as official documentation |
| Keep names out of normative guidance | Use a mark in your own product name or branding |

This layer's practice: brand names appear **only** in source citations and research tables, never in
normative rules. See [ATTRIBUTION.md](ATTRIBUTION.md).

**Note on the source's inconsistency.** Seven source files use altered spellings (e.g. "Stripi",
"Slacc") while thirteen in the same phrasing group use accurate names — and directory names, links,
and typeface names are unaltered throughout. Applied inconsistently, the alteration provides little
protection while making the material harder to verify. Recorded as
[REPOSITORY-DISCREPANCIES.md](REPOSITORY-DISCREPANCIES.md) D8 for a maintainer decision. This layer
uses accurate names consistently, on the view that honest nominative use is clearer than partial
obfuscation.

## 6. Assets: none present, none should be added

Verified: this layer contains **no** logos, screenshots, images, font files, or binary assets of any
kind. It is Markdown text only.

**Do not add them.** Brand assets carry copyright *and* trademark exposure simultaneously, and there
is no design need — this layer describes structure, and structure is describable in text. A logo in
a design-guidance document adds nothing but liability.

## 7. If you extract this layer into its own repository

| Step | Reason |
|---|---|
| Preserve the MIT notice and copyright | Licence requirement |
| Identify the source collection prominently | Attribution to the work this depends on |
| Keep the no-affiliation and trademark statements | They are what makes nominative use defensible |
| Convert `design-md/…` citations to links to the source repository | Otherwise citations point at nothing |
| Add no brand assets | See §6 |
| Keep the evidence-strength banners | Removing them converts honest reasoning into false authority |
| Note that citations reflect a specific state of the source repository | The collection evolves |
| Review your own jurisdiction's position | Trademark and trade dress rules vary materially by country |

Full list: [PUBLISHING-CHECKLIST.md](PUBLISHING-CHECKLIST.md).

## 8. What this layer's own text is

Original synthesis. No passage was copied from a source file. Short quotations appear only where a
source's own words establish a limitation — for instance where a file states that in-product
surfaces were not captured — and are attributed inline with their path.

Under the repository's MIT licence, this text may be used, modified, and redistributed with the
notice preserved.

## 9. Summary

1. **MIT covers the text.** Use it freely, keep the notice.
2. **MIT does not cover trademarks, brand identities, or typefaces.** It cannot.
3. **Individual design values are functional facts.** Complete systems combined with brand naming
   are a different matter.
4. **Naming a font is not licensing it.** Always document a substitute.
5. **No brand assets are present, and none should be added.**
6. **Nominative use requires stated non-affiliation.** Keep those statements.
7. **Adopt principles, derive your own values.** Safer, and better design.
8. **Not legal advice.** For a real position on a real product, ask a professional.
