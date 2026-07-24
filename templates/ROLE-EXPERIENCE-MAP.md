# Role Experience Map — [[SET: Platform name]]

Companion to [DESIGN.multi-role-platform.md](DESIGN.multi-role-platform.md). Complete this
**before** designing any role's surface. It is the artefact that decides how much layers may
diverge.

---

## 1. Role census

| # | Role | Internal or external | Approx. user count | Layer |
|---|---|---|---|---|
| 1 | [[SET]] | [[SET]] | [[SET]] | [[customer / operator / admin]] |
| 2 | [[SET]] | [[SET]] | [[SET]] | [[SET]] |
| 3 | [[SET]] | [[SET]] | [[SET]] | [[SET]] |

**Does one person hold more than one role?** [[CHOOSE: no | yes — which combinations]]

This is the single most important answer here. If yes, cross-role consistency is critical and
role identity must be unmissable at all times. If no, layers may diverge further.

---

## 2. Per-role profile

Duplicate this block per role.

### Role: [[SET: name]]

| Dimension | Value | Design consequence |
|---|---|---|
| **Top 3 tasks** | 1. [[SET]] 2. [[SET]] 3. [[SET]] | Determines the default landing view |
| **Expertise** | [[none / learnable / trained / expert]] | Guidance depth and density |
| **Frequency** | [[rare / weekly / daily / all day]] | Density and section rhythm |
| **Session length** | [[seconds / minutes / hours]] | Fatigue tolerance |
| **Primary device** | [[desktop / mobile / both]] | **Touch forces 44px — compact becomes illegal** |
| **Environment** | [[office / warehouse / field / shared terminal]] | Contrast, target size, polarity |
| **Data scope** | [[own / team / organisation / platform]] | Filtering defaults and permission surface |
| **Can affect others' data** | [[yes / no]] | Audit trail requirement |
| **Destructive capability** | [[SET: what they can irreversibly do]] | Confirmation pattern |
| **Error consequence** | [[trivial / recoverable / data loss / financial / regulatory]] | Error-prevention investment |
| **Keyboard importance** | [[standard / valued / essential]] | Shortcuts, command palette |
| **Accessibility needs known** | [[SET]] | Specific commitments |
| **Onboarding needed** | [[none / minimal / guided]] | First-run experience |
| **Sees other roles' work** | [[yes / no]] | Cross-role visibility design |

**Default landing view:** [[SET: what answers this role's first question of the day. Must not be
a copy of another role's dashboard.]]

**Density:** [[compact / default / comfortable]] — [[SET: justified by frequency + device]]

**Navigation:** [[SET: pattern + destination count]]

**Permissions this role lacks that it will encounter:** [[SET: list — each needs a
disable-and-explain treatment]]

---

## 3. Task and permission matrix

`✓` full · `R` read-only · `A` requires approval · `—` no access

| Task / object | [[Role 1]] | [[Role 2]] | [[Role 3]] |
|---|---|---|---|
| [[SET]] | ✓ | R | — |
| [[SET]] | R | ✓ | ✓ |
| [[SET]] | — | A | ✓ |

**For every `—` cell, decide:** hidden, or disabled-with-explanation?

- Disable + explain when the permission is plausibly gettable — this teaches the permission model.
- Hide only when the feature is irrelevant to the role, or when its existence is confidential.

| Task | Role | Hidden or disabled | Explanation shown |
|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET: what is needed + who grants it]] |

---

## 4. Shared object terminology

One canonical name per shared object. Map genuine role-specific vocabulary rather than letting a
third term appear.

| Object | Canonical | [[Role 1]] says | [[Role 2]] says | [[Role 3]] says |
|---|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET]] | [[SET]] |

**Terms we do not use:** [[SET: rejected synonyms, so nobody reintroduces them]]

---

## 5. Status vocabulary — one set, platform-wide

This must match `status-vocabulary` in the `DESIGN.md` frontmatter exactly. Divergence here causes
real operational errors.

| Status | Meaning | Colour token | Icon | Terminal? | Visible to |
|---|---|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET]] | [[yes/no]] | [[roles]] |

**Check:** does any role use one of these words to mean something different? If so, resolve it
now — this is the most common multi-role defect.

---

## 6. Handoffs between roles

Where work passes from one role to another. Each handoff needs a visible state change, a
notification, and a clear owner.

| From | To | Trigger | State change | Notification | New owner visible? |
|---|---|---|---|---|---|
| [[SET]] | [[SET]] | [[SET]] | [[SET]] | [[SET]] | [[SET]] |

**For each handoff, confirm:**

- [ ] The sending role sees confirmation it was sent
- [ ] The receiving role is notified in a channel they actually watch
- [ ] The current owner and time-in-state are visible to both
- [ ] Rejection or return has a required reason
- [ ] The history records the transition

---

## 7. Shared versus varied — sign-off

Confirm each item explicitly. Unconfirmed items become inconsistencies.

### Must be identical across all roles

- [ ] Primitive and semantic tokens
- [ ] Type families and scale ratios
- [ ] Radius character
- [ ] Spacing base unit
- [ ] **Status colour meanings**
- [ ] Core component behaviour and all eight interaction states
- [ ] Form conventions (label position, validation timing, error presentation)
- [ ] Feedback semantics (toast vs. banner vs. modal)
- [ ] Destructive-action pattern
- [ ] Accessibility floor
- [ ] Terminology for shared objects
- [ ] Keyboard conventions

### Varies, and documented above

- [ ] Density mode
- [ ] Navigation pattern and destinations
- [ ] Section rhythm and page padding
- [ ] Information density
- [ ] Available actions
- [ ] Workflow depth
- [ ] Data visibility
- [ ] Default landing view
- [ ] Onboarding depth
- [ ] Role-specific terminology

---

## 8. Risk register

| Risk | Roles affected | Mitigation |
|---|---|---|
| Status drift between surfaces | All | Single vocabulary in §5, enforced in review |
| Role layers diverging into separate products | All | Shared foundation in §7; one component library |
| Admin complexity leaking to customers | [[SET]] | Surface scoping; permission checks |
| Novice role given expert density | [[SET]] | Density justified per role in §2 |
| Expert role obstructed by novice flow | [[SET]] | Expert path alongside guided path |
| Impersonation used without visibility | [[SET]] | Non-dismissible banner |
| Compact density shipped to a touch device | [[SET]] | Device recorded in §2; touch forces comfortable |
| [[SET]] | [[SET]] | [[SET]] |

---

## 9. Validation

Before building, walk these through with a real user of each role:

- [ ] Each role's landing view answers their actual first question of the day
- [ ] Each role can complete their top 3 tasks without encountering another role's complexity
- [ ] A user holding two roles can tell which one they are in, at a glance, at all times
- [ ] Every `—` in the permission matrix behaves as decided in §3
- [ ] Every handoff in §6 is visible to both parties
- [ ] Status words mean the same thing to every role
- [ ] Nothing in the shared list of §7 differs between surfaces

**The guide behind this template is predominantly synthesized** — the source corpus documents no
role-based application. Validate with real users of each role earlier than you would for a
corpus-backed category.
