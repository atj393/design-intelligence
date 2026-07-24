# Project Initialization Guide

How to go from "we are building a product" to a working design system, in order.

Six stages. Do not skip discovery — a design system derived from guesses needs rebuilding, and
rebuilding one after code exists is expensive.

---

## Stage 1 — Product discovery

Answer these before making a single visual decision. The full 23-question set is in
[CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) Part 1; this is the minimum.

### Purpose

| Question | Answer |
|---|---|
| What does the product do, in one sentence? | |
| What is the single most important thing the interface must accomplish? | |
| How will you know the design succeeded? | |

### Users

| Question | Answer |
|---|---|
| Who is the primary user? (role, environment, device — be specific) | |
| How many distinct roles? | |
| Expertise you can assume? | |
| **How often does one person use it?** | |
| Typical session length? | |

That fourth question drives density and section rhythm more than anything else. "Once" and "eight
hours a day" produce different products from the same requirements.

### Work

| Question | Answer |
|---|---|
| Core workflows (top 3–5)? | |
| Information density on screen at once? | |
| How many distinct workflows total? | |
| Navigation depth? | |

### Constraints

| Question | Answer |
|---|---|
| Primary devices, with split if known? | |
| Public, authenticated, or both? | |
| Consequence of a user error? | |
| Accessibility requirement? | |
| Brand maturity? | |
| Existing component library or framework? | |
| Localisation or RTL needed? | |

**If you cannot answer a question, mark it as an open question rather than guessing.** An assumption
recorded is recoverable; an assumption forgotten becomes a defect.

---

## Stage 2 — Category selection

Work through [CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) Parts 2 and 3. Output the
recommendation block:

```
PRIMARY CATEGORY:     <one>
SUPPORTING:           <zero or more, with the surface each applies to>
DENSITY MODE:         compact | default | spacious
VISUAL TONE:          <cluster> + <decoration budget>
CANVAS POLARITY:      light | dark | dual-track
NAVIGATION MODEL:     <pattern> (+ secondary)
ACCENT COUNT:         0 | 1 | 2+ (if 2+, state the structural mapping)
CONTAINER / MEASURE:  <container px> / <prose px>
SECTION RHYTHM:       <px>
DESIGN RISKS:         <ranked>
EVIDENCE STRENGTH:    <from the category guide's banner>
OPEN QUESTIONS:       <needing a human>
```

**Note the evidence strength.** If your primary category is dashboard, conversational,
multi-role, or spatial, the guidance is reasoning rather than corpus evidence — plan to validate
with real users earlier and harder.

**If you have three or more roles**, also complete
[templates/ROLE-EXPERIENCE-MAP.md](templates/ROLE-EXPERIENCE-MAP.md) now, not later. The
shared-versus-varied boundary is the main design decision in that category, and discovering it
after two role surfaces exist means reworking both.

---

## Stage 3 — Core decisions

Ten decisions, in this order. Each constrains the next.

| # | Decision | Derive from | Reference |
|---|---|---|---|
| 1 | **Density mode** | Visit frequency + information density + device | [Handbook §11](DESIGN-DECISION-HANDBOOK.md) |
| 2 | **Navigation model** | Destination count + role count + depth + device | [Handbook §4](DESIGN-DECISION-HANDBOOK.md) |
| 3 | **Type families** | Content type + localisation + brand + licensing | [Handbook §1](DESIGN-DECISION-HANDBOOK.md) |
| 4 | **Type scale** | Surface type + hierarchy depth | [Foundation §4](COMMON-FOUNDATION.md) |
| 5 | **Colour strategy** | Brand + semantic needs + data viz + trust | [Handbook §2](DESIGN-DECISION-HANDBOOK.md) |
| 6 | **Spacing scale** | Density mode | [Foundation §3](COMMON-FOUNDATION.md) |
| 7 | **Radius character** | Tone + density + audience | [Handbook §7](DESIGN-DECISION-HANDBOOK.md) |
| 8 | **Elevation strategy** | Canvas polarity + density | [Handbook §6](DESIGN-DECISION-HANDBOOK.md) |
| 9 | **Responsive approach** | Device split + capability-by-capability | [Handbook §9](DESIGN-DECISION-HANDBOOK.md) |
| 10 | **Component priorities** | Category component table | [Comparison §5](CATEGORY-COMPARISON.md) |

**Order matters.** Density constrains spacing and control sizes. Navigation constrains layout.
Choosing a radius before a density produces a soft system that cannot render a compact control.

**Record the reason for each.** A decision without a recorded reason gets re-litigated every
quarter.

### The one thing not derived here

**Visual tone.** It comes from brand and audience, not from category — the source corpus shows the
same product category rendered in four incompatible tones. Decide it separately, via
[CATEGORY-SELECTION.md](CATEGORY-SELECTION.md) Part 2, and then hold it.

---

## Stage 4 — Write the DESIGN.md

Copy the template for your primary category from [templates/](templates/). Resolve **every**
`[[SET: ...]]` and `[[CHOOSE: ...]]` marker — an unresolved marker will be read as literal text by
an agent.

Non-negotiable content:

- Two-layer tokens: primitives and semantics; components consume semantics only
- Complete semantic set: surface, text, border, action, status, focus, utility
- **Light and dark specified separately** — derived, not inverted
- Type scale with size, weight, line-height, tracking, and use per step
- Spacing on a 4px grid
- One radius character with the nesting rule stated
- Component specs with **all eight interaction states**
- **All seven data states** per data-bearing view
- Per-element responsive behaviour, named
- Accessibility commitments as checkable statements
- A substitution note for any proprietary typeface
- Agent prompt guidance

Prompt: [prompts/01-new-design-system.md](prompts/01-new-design-system.md).

---

## Stage 5 — Validate against real screens

**Before building anything, walk the two or three most important screens through the `DESIGN.md`.**

For each screen, ask:

- [ ] Does the `DESIGN.md` specify every colour this screen needs?
- [ ] Every type size?
- [ ] Every spacing value?
- [ ] Every component, with all its states?
- [ ] The empty, loading, error, and permission-denied states?
- [ ] What happens at 375px?
- [ ] How the primary action is emphasised?
- [ ] Which existing components are reused?

**Every "no" is a gap. Fix it in the `DESIGN.md`, not in the screen.** This stage typically finds
five to fifteen gaps, and finding them here costs minutes rather than weeks.

Then build one screen end to end — including every state — and review it with
[checklists/foundation-review.md](checklists/foundation-review.md) plus your category checklist.
That first screen is the reference implementation; get it right before scaling.

---

## Stage 6 — Establish ongoing review

| Cadence | Activity |
|---|---|
| Every PR with UI | Foundation checklist fast pass (8 checks, ~10 min) |
| New component | Full foundation checklist; all eight states specified |
| New surface | Category checklist |
| Monthly | Token audit — search for hard-coded values |
| Quarterly | Accessibility audit ([prompts/12](prompts/12-test-accessibility.md)) |
| Quarterly | Component duplication audit |
| On deviation | Record it in `DESIGN.md` with its reason |

**The deviation-recording rule is what keeps a system alive.** An undocumented exception is
indistinguishable from a mistake six months later, and nobody will know whether to fix it or
preserve it.

---

## Worked example — a hybrid commercial platform

A field-services company builds one platform with five surfaces.

### Discovery

- **Product:** scheduling, dispatch, and job management for a commercial installation business
- **Roles:** 5 — prospect (public), customer, field technician, dispatcher, platform admin
- **Frequency:** prospect once · customer monthly · technician all day (mobile) · dispatcher all
  day (desktop) · admin weekly
- **Density on screen:** low (prospect) → very high (dispatcher)
- **Error consequence:** financial (invoicing) and safety (job instructions)
- **Devices:** technician is mobile-only; dispatcher is desktop-only; others both
- **Brand:** guidelines exist for marketing; nothing for product
- **Accessibility:** WCAG AA, procurement requirement

### Category selection

```
PRIMARY CATEGORY:     Commercial Multi-Role Platform
SUPPORTING:           Marketing Website (public acquisition)
                      Dashboard & Administration (dispatcher, admin)
                      Financial & High-Trust (invoicing, payments)
                      Conversational AI (support assistant, cross-surface)
DENSITY MODE:         per layer — see table below
VISUAL TONE:          Clinical minimal; decoration budget minimal (marketing) / none (product)
CANVAS POLARITY:      dual-track — expressive light marketing, plain light product
                      (dark mode deferred; technicians work outdoors, so it is a real
                       future requirement, not a nice-to-have)
NAVIGATION MODEL:     top bar (marketing) · side nav (customer, admin) ·
                      rail + command palette (dispatcher) · bottom nav (technician)
ACCENT COUNT:         1 + full semantic set. Job status does the real work here.
DESIGN RISKS:         1. Five surfaces drifting into five products
                      2. Job status meaning differently to technician and dispatcher
                      3. Marketing density leaking into the dispatcher console
                      4. Technician surface designed on a desktop and failing in the field
                      5. Invoicing flows lacking confirmation
EVIDENCE STRENGTH:    Weak — multi-role and dashboard guidance is synthesized
OPEN QUESTIONS:       Does the technician surface need offline capability? (blocks Stage 3 #9)
```

### The five layers

| Layer | Category | Density | Navigation | Rhythm | Container | Body | Devices |
|---|---|---|---|---|---|---|---|
| Public marketing | Marketing | spacious | top bar | 80px | 1280px | 16px | both |
| Customer portal | Dashboard | default | side nav 240px | 48px | 1280px | 16px | both |
| Technician app | Multi-role, mobile | **comfortable** | bottom nav, 4 items | 24px | fluid | 16px | **mobile only** |
| Dispatcher console | Dashboard + Multi-role | **compact** | rail + palette | 24px | fluid | 14px | **desktop only** |
| Platform admin | Multi-role + High-trust | compact | nested side nav | 32px | fluid | 14px | desktop |
| Support assistant | Conversational | inherits host | side panel 400px | n/a | n/a | 16px | inherits |

### What is shared

One colour ramp · one type family · one radius character (`default`, 6–12px) · one 4px spacing
base · **one job-status vocabulary** · one set of form conventions · one destructive-action
pattern · one accessibility floor · identical component behaviour and all eight interaction states ·
one term per shared object.

### What deliberately differs

Density · navigation pattern · section rhythm · container · body size · available actions ·
onboarding depth · decoration budget.

### Two decisions worth studying

**The technician layer uses *comfortable* density despite being an all-day surface.** Frequency
argues for compact; the device and environment override it. Gloved hands, sunlight, and a phone
mean 44px minimum and 16px body — non-negotiable. Frequency loses to device here, and the
[handbook's density rules](DESIGN-DECISION-HANDBOOK.md) say so explicitly: compact is pointer-only.

**The support assistant inherits each host's density and polarity.** It appears in the customer
portal, the technician app, and the dispatcher console. In each, it uses that host's tokens and
density rather than carrying its own. An assistant panel that looks like a separate product inside
the dispatcher console is the most common version of this mistake — and the reason
[categories/conversational-ai.md](categories/conversational-ai.md) makes inheritance a hard rule.

### Delivery order

1. Token foundation + one `DESIGN.md` with per-layer sections
2. `ROLE-EXPERIENCE-MAP.md` for all five roles, including the job-status vocabulary
3. **Dispatcher console first** — highest density, most components, most risk. If the foundation
   survives this, it survives everything.
4. Technician app second — validates the mobile and accessibility constraints on real devices
5. Customer portal third — mostly assembled from components 3 and 4 produced
6. Marketing last — least coupled, and by then the product's real character is known
7. Assistant as a cross-cutting layer once two hosts exist, so inheritance is testable

**Building marketing first is the tempting order and the wrong one.** It sets brand expectations
the product surfaces then have to fight, and it produces components at spacious density that get
rebuilt for compact.

### Risk mitigation

| Risk | Mitigation |
|---|---|
| Five surfaces drifting | One `DESIGN.md`; one component library; cross-layer review each sprint |
| Status meaning drift | Vocabulary defined once in the role map, enforced in checklist review |
| Marketing density leaking | Per-layer density recorded in `DESIGN.md`; checked in review |
| Technician surface failing in the field | Test on real devices, outdoors, with gloves. Not in a simulator |
| Invoicing without confirmation | High-trust checklist applied to every money flow |
| Weak evidence base | Validate dispatcher and technician surfaces with real users in week one |
