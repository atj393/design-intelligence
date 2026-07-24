# Financial and High-Trust Products

Interfaces where an error costs money, breaks a legal obligation, exposes private data, or
cannot be undone: banking, payments, trading, insurance, healthcare records, identity,
security settings, legal agreements, compliance systems.

> **Evidence strength: moderate for visual expression, synthesized for flows.** Eight sources
> are financial-domain and one (`design-md/binance/`) documents a light transactional theme
> alongside its dark marketing surface. `design-md/stripe/` contributes the tabular-figure
> decision. **Verification, confirmation, audit, and irreversible-action flows are entirely
> synthesized** — no source documents them.

---

## 1. What the corpus actually shows about "looking trustworthy"

The corpus refutes the two most common assumptions in this category.

**Assumption 1: high-trust products must look conservative and squared.** Refuted.
`design-md/mastercard/DESIGN.md` documents a payments brand whose dominant gesture is an
*oversized* radius — 40px hero corners, fully pill-shaped cards, circular image crops, almost
no sharp corner anywhere. It coexists with `design-md/ibm/DESIGN.md` at 0–4px corners.

**Assumption 2: heavier type reads as more authoritative.** Refuted in both directions.
`design-md/stripe/` and `design-md/coinbase/` use display weight 300–400; `design-md/wise/`
uses 900. All four are trusted brands.

**What the corpus does consistently show:**

| Consistent across financial sources | Not consistent |
|---|---|
| Restrained accent use — one brand colour | Radius character |
| Tabular figures where numbers matter | Display weight |
| Directional semantic colour for value change | Canvas polarity |
| Clear separation of marketing and transactional surfaces | Decoration budget |

**Conclusion: trust is produced by behaviour, not by aesthetic.** Clarity, confirmation,
traceability, and error prevention build trust. A conservative palette does not.

## 2. The governing principle

**Prevent errors first. Confirm second. Recover third.**

| Priority | Mechanism |
|---|---|
| 1. Prevention | Constrain input, validate early, show consequences before commitment |
| 2. Confirmation | Explicit review of exactly what will happen |
| 3. Recovery | Undo, cancel windows, reversal paths, support access |
| 4. Traceability | A complete record of what happened and who did it |

WCAG 3.3.4 (Error Prevention) applies to legal, financial, and data-modifying transactions:
they must be **reversible, checked, or confirmed**. This is a specification requirement in this
category, not a nice-to-have.

## 3. Displaying money and values

| Requirement | Detail |
|---|---|
| **Tabular figures** | Always. Non-negotiable. Proportional digits make columns jitter and comparison harder |
| Currency | Explicit code or unambiguous symbol. Never a bare `$` in a multi-currency product |
| Decimal places | Consistent within a context. Never truncate silently |
| Alignment | Right-aligned in tables and lists |
| Negatives | Minus sign **and** colour. Parentheses in accounting contexts. Never colour alone |
| Large numbers | Thousands separators, localised |
| Rounding | State it if a displayed value is rounded |
| Pending vs. settled | Visually distinguished; both labelled |
| Exchange rate | Show the rate, the timestamp, and any fee separately |
| Balance types | Available, pending, and total are different numbers — label each |

**Never show a single "balance" when multiple balance concepts exist.** Available versus
pending versus total is the most common source of financial confusion, and the interface either
resolves it or causes it.

### Directional value change

`design-md/binance/DESIGN.md` documents up/down semantic colour for price direction. Required
addition: **direction must also be conveyed by sign or arrow**, because red/green is precisely
the pair colour-blind users cannot distinguish.

```
+2.41%  ▲   (green + plus sign + arrow)
−1.08%  ▼   (red + minus sign + arrow)
```

Three channels. Any one alone is insufficient.

## 4. Transactions and records

| Element | Requirement |
|---|---|
| List row | Date, description, counterparty, amount, status, balance-after |
| Status | Pending / completed / failed / reversed — colour + icon + text |
| Timestamps | **Absolute with timezone.** Relative time is for recency, never for records |
| Reference | Copyable transaction ID on every record |
| Detail view | Full breakdown: fees, exchange rate, timestamps for each state change |
| Receipt | Downloadable or printable |
| Search / filter | By date range, amount range, type, counterparty, status |
| Export | CSV or equivalent; state which fields are included |
| Immutability | Corrections appear as new entries, never as edits |

**Corrections must be additive.** A financial record that silently changes is not a record. Show
the original and the correction, linked.

## 5. Verification and authentication

| Situation | Requirement |
|---|---|
| Identity verification | Explain what is needed, why, and how long it takes, before starting |
| Document upload | Show requirements clearly, validate before submission, allow retry |
| Verification pending | Show state and expected duration; do not leave the user guessing |
| Verification failed | State the reason and the remedy |
| MFA setup | Explain the method; **provide and confirm recovery codes** |
| MFA challenge | Say which method is being used and offer alternatives |
| Step-up auth | Explain why it is required for this specific action |
| Session timeout | **Warn before** it happens; allow extension; preserve form data |
| Session expired | Return the user to where they were, with their input intact |

**Losing a half-completed form to a session timeout is unacceptable in this category.** WCAG
2.2.1 requires warning and extension for timed processes; the practical requirement is to
preserve the data as well.

## 6. Confirmation and irreversible actions

The most important interaction design in the category.

| Consequence | Pattern |
|---|---|
| Reversible, low value | Direct action + toast with undo |
| Reversible, high value | Confirmation stating the amount and recipient |
| Delayed execution | Show a cancellation window and how to use it |
| **Irreversible** | Full review step + typed confirmation + explicit acknowledgement |
| Affects others | State exactly who is affected and how |
| Legally binding | Show the full terms; require deliberate affirmative action; record consent |

### Review step requirements

For any money movement or binding commitment, show before commitment:

- Exact amount, in the source currency **and** the destination currency
- All fees, itemised — never a single opaque "total"
- Exchange rate and its timestamp
- Recipient, with enough detail to verify identity (masked account, name)
- Expected arrival time
- Whether it can be cancelled, and until when
- A clear route back to edit

**The confirmation button names the action and the amount:** "Send £2,400 to J. Okafor". Not
"Confirm".

**Never make the destructive or committing action the default focus.** Never place it adjacent
to a cancel or back control.

### Typed confirmation

For irreversible, high-consequence actions — closing an account, deleting all records,
transferring a large sum to a new recipient — require the user to type the resource name or
amount. The friction is the feature: it forces the user to read what they are about to do.

## 7. Security settings

| Element | Requirement |
|---|---|
| Current state visible | Which factors are active, which devices are trusted, which sessions are open |
| Session list | Device, location, last active — with individual and bulk revoke |
| Password change | Requires current password; states requirements up front; never blocks paste |
| Recovery codes | Generated, displayed once, confirmed as saved, regenerable |
| Security events | A visible log of logins, changes, and failures |
| Notifications | For security-relevant changes, out-of-band |
| Dangerous settings | Separated from routine settings; individually confirmed |
| Downgrade warnings | State the consequence of disabling a protection |

**Never block paste in password fields.** It defeats password managers and produces weaker
passwords.

## 8. Warnings and errors

| Type | Treatment |
|---|---|
| Informational | Banner, `status-info`, dismissible |
| Advisory | Banner, `status-warning`, dismissible, states the implication |
| Blocking | Inline at the point of failure, `status-danger`, not dismissible until resolved |
| Consequence warning | In the confirmation flow, stating precisely what will happen |
| Regulatory notice | Persistent where required; do not allow dismissal of legally required text |

**Error message requirements:**

1. What happened, in plain language
2. Why, if known
3. What to do next
4. A reference identifier for support
5. Whether anything was charged, changed, or committed

That last point is specific to this category and frequently omitted. "Payment failed" leaves the
user not knowing whether they were charged. "Payment failed — you have not been charged. Try
another card." resolves it.

**Never use a generic error in a money flow.** "Something went wrong" in a payment context
generates a support call and destroys confidence.

## 9. Legal and regulatory content

| Requirement | Detail |
|---|---|
| Readability | Body text at 16px minimum. Small print is a dark pattern when it is legally material |
| Structure | Headings, sections, a table of contents for long documents |
| Consent | Unchecked by default; specific rather than bundled; recorded with timestamp and version |
| Versioning | Show the version and effective date; keep previous versions accessible |
| Changes | Notify; summarise what changed rather than only linking the new document |
| Disclosure placement | At the point of decision, not only in a footer |
| Downloadable | Terms and agreements available as a file |

**Legally required information set in 10px grey text is a design failure**, and increasingly a
compliance failure. If it matters enough to be required, it matters enough to be legible.

## 10. Support access

High-consequence products need visible help. A user who cannot resolve a problem loses trust
permanently.

- Contact route visible on every transactional surface — not buried in a help centre.
- Show expected response time.
- Provide the reference identifier the user needs before they ask for it.
- Never make support a dead end: if a channel is closed, say when it opens.
- For urgent matters (suspected fraud, card loss), provide an immediate path.

## 11. Layout and typography

| Property | Marketing | Product |
|---|---|---|
| Container | 1280px | 1024–1280px |
| Prose measure | 680px | 680px |
| Section rhythm | 64–80px | 32–48px |
| Max display | 40–56px | 28–32px |
| Body | 16px | 16px |
| Numeric | 16px tabular | 16px tabular |
| Control height | 48px | 44px |
| Density | default | default — **not compact** |

**Do not use compact density in high-consequence flows.** Denser targets mean more mis-clicks,
and a mis-click here costs money. 44px minimum, 16px body, generous spacing between a
destructive and a safe action.

## 12. Responsive behaviour

| Element | <768px | 768–1024px | >1024px |
|---|---|---|---|
| Transaction list | Card rows | Table, scroll | Full table |
| Transaction detail | Full-screen route | Overlay | Panel or route |
| Confirmation flow | One step per screen | One step per screen | Steps or single review |
| Amount entry | Large, numeric keyboard | Standard | Standard |
| Security settings | Stacked sections | Sections | Sections |
| Legal documents | Full width − 32px, 16px body | 680px | 680px |
| Charts | Simplified | Full | Full |

**Full mobile parity is expected.** Money is managed on phones. Nothing may be desktop-only,
and confirmation flows must be *more* careful on mobile, not less — smaller targets, more
distraction, higher error rates.

## 13. Accessibility

Beyond the [foundation floor](../COMMON-FOUNDATION.md#13-accessibility-floor). This category
carries the strictest additional requirements.

| Requirement | Reference |
|---|---|
| Error prevention: reversible, checked, or confirmed | WCAG 3.3.4 |
| Timeout warning with extension | WCAG 2.2.1 |
| Value direction not by colour alone | WCAG 1.4.1 |
| Amounts programmatically associated with their labels | — |
| Errors announced and focused | WCAG 3.3.1 |
| Consent controls fully keyboard-operable and clearly labelled | — |
| Legal text at 200% zoom without loss | WCAG 1.4.4 |
| Numeric input with `inputmode` for correct keyboards | — |
| Status announced on change (pending → completed) | — |
| Never rely on hover to reveal financially material information | — |

**Amount entry deserves specific care:** large text, numeric keyboard, clear currency
indication, and an unambiguous echo of the parsed value ("You are sending £1,200.00") before
confirmation. Ambiguity between `1,200` and `1.200` is a real, expensive failure across locales.

## 14. Do

- Use tabular figures everywhere numbers appear
- Show available, pending, and total as separate labelled values
- Convey value direction with sign, arrow, **and** colour
- Use absolute timestamps with timezone in all records
- Make corrections additive, never destructive
- Itemise every fee
- Show the exchange rate with its timestamp
- Name the action and amount in the confirmation button
- Require typed confirmation for irreversible high-consequence actions
- Warn before session timeout and preserve form data
- State whether the user was charged when a payment fails
- Provide a copyable reference on every transaction and every error
- Keep legal text at 16px minimum
- Make support visible on transactional surfaces
- Allow paste in password fields

## 15. Do not

- Do not use compact density in money flows
- Do not use relative timestamps in records
- Do not show a single ambiguous "balance"
- Do not convey gain/loss by colour alone
- Do not use generic error messages in payment flows
- Do not place a committing action adjacent to cancel
- Do not make the committing action the default focus
- Do not set legally material text below 16px
- Do not pre-check consent boxes or bundle consents
- Do not lose form data on timeout or error
- Do not block paste in password or card fields
- Do not bury support behind a help-centre search
- Do not let decoration reduce clarity in a transactional surface
- Do not assume a conservative palette substitutes for confirmation design

## 16. Source inspiration

| Source | Structural lesson |
|---|---|
| `design-md/stripe/DESIGN.md` § *Typography* | A dedicated tabular-figure body token for numerics, alongside light display weight with negative tracking. The clearest corpus evidence that numeric legibility is a system-level decision |
| `design-md/binance/DESIGN.md` § *Overview*, § *Colors* | Dark marketing / light transactional dual-track, and directional up/down semantic colour. Transactional surfaces deliberately flip polarity for density |
| `design-md/mastercard/DESIGN.md` § *Visual Theme*, § *Component Stylings* | A payments brand at maximum softness — 40px hero radius, pill cards, circular crops. Refutes the assumption that high-trust requires squared geometry |
| `design-md/coinbase/DESIGN.md` § *Typography* | Display at weight 400 rather than 700 — editorial calm as an institutional trust signal |
| `design-md/wise/DESIGN.md` § *Typography* | Display weight 900 on a tinted canvas — confident accessibility as the opposite trust strategy. Both work; the audience decides |
| `design-md/revolut/DESIGN.md` § *Colors* | A wide accent palette confined to product illustration while chrome stays restrained — how to have brand colour without letting it into semantic space |
| `design-md/ibm/DESIGN.md` § *Shapes*, § *Typography* | 0–4px corners and light display weight as enterprise gravitas — the far end of the radius disagreement |
| `design-md/kraken/DESIGN.md` § *Color Palette & Roles* | Purple brand identity on white with a cool neutral scale. Thin file, but confirms the single-accent discipline holds in this domain |

## 17. Common mistakes

| Mistake | Consequence | Correction |
|---|---|---|
| Proportional digits | Columns jitter; comparison is harder | Tabular figures |
| One ambiguous balance | User misjudges available funds | Separate labelled values |
| Colour-only gain/loss | Excludes colour-blind users from core information | Sign + arrow + colour |
| Relative timestamps in records | Records become unverifiable | Absolute + timezone |
| Generic payment errors | Support calls; lost trust | State cause and charge status |
| Session timeout losing data | Abandonment and anger | Warn, extend, preserve |
| Unstated fees | Perceived deception | Itemise everything |
| Committing action beside cancel | Costly mis-clicks | Separate them |
| Compact density in money flows | More mis-clicks | 44px, default density |
| Small-print legal text | Compliance and ethical failure | 16px minimum |
| Blocked paste in password fields | Weaker passwords | Allow paste |
| Conservative palette as the trust strategy | Looks safe, behaves unsafely | Invest in confirmation and traceability |

## 18. Template

[templates/DESIGN.high-trust.md](../templates/DESIGN.high-trust.md)
