# 03 — Multiples, Adjustments, and Comparable Analysis

Contents:
- [How to use the bands in this file](#how-to-use-the-bands-in-this-file)
- [Starting bands (Level 5 priors)](#starting-bands-level-5-priors)
- [The adjustment engine](#the-adjustment-engine)
- [Worked example](#worked-example)
- [Comparable analysis](#comparable-analysis)
- [Similarity scoring](#similarity-scoring)

---

## How to use the bands in this file

There is no universal SaaS multiple. Anyone quoting one is selling something.

The bands below are **Level 5 priors** — starting points that reflect how small software assets have
generally been priced, expressed as wide ranges because the true dispersion is wide. They are not
market data and must never be presented as such.

Rules of use:

1. **Research first when you can.** If you have web tools, look for actual completed transactions in
   this type and size band (see `08-market-research.md`). Researched L1–L3 evidence overrides these
   priors, and you should say so in the report.
2. **Label them honestly.** In the report: *"Base multiple derived from Level 5 benchmark bands, not
   from researched transactions; see confidence discussion."*
3. **Cap confidence.** A valuation resting entirely on these bands cannot exceed roughly 55/100
   confidence (see `04-scoring.md`).
4. **Never pick the mid-point by default.** The whole analysis is about *where in the band* this
   business sits and why. Starting at the middle and nudging is lazy; start from the factors.
5. **Market conditions move.** These bands do not know today's date. If your knowledge of current
   conditions or your research suggests the market is materially hotter or colder, adjust and say so.

## Starting bands (Level 5 priors)

**Recurring-revenue businesses — annual multiple of ARR** (net recurring revenue only):

| Profile | Low | Typical | High |
|---|---|---|---|
| B2B SaaS, established, low churn, diversified, growing | 3.0× | 3.5–4.5× | 6×+ |
| B2B SaaS, small (<€10k MRR), moderate churn | 2.0× | 2.5–3.5× | 4× |
| Micro-SaaS, profitable, low owner hours | 2.0× | 2.5–3.5× | 4× |
| B2C subscription, higher churn | 1.5× | 2.0–3.0× | 3.5× |
| Consumer mobile subscription (net of store cut) | 1.0× | 1.5–2.5× | 3× |
| Mobile app, ad-supported | 0.8× | 1.0–2.0× | 2.5× |
| Marketplace (on net take-rate revenue) | 1.5× | 2.0–3.5× | 4.5× |
| AI SaaS, strong margin & retention | 3.0× | 4.0–6.0× | 8×+ |
| AI SaaS, thin margin or wrapper-like | 1.0× | 1.5–2.5× | 3× |
| API business, diversified usage | 2.5× | 3.0–4.5× | 5.5× |
| Developer tool, monetized | 2.0× | 2.5–4.0× | 5× |
| Declining revenue (any type) | 0.5× | 0.8–1.5× | 2× |

**Profitable small businesses — multiple of annual SDE:**

| Profile | Low | Typical | High |
|---|---|---|---|
| Micro-SaaS, owner-operated, stable | 2.0× | 2.5–3.5× | 4.5× |
| Small SaaS with some team, growing | 3.0× | 3.5–4.5× | 5.5× |
| Content/software hybrid | 2.0× | 2.5–3.5× | 4× |
| Mobile app with stable revenue | 1.5× | 2.0–3.0× | 3.5× |
| Declining or highly owner-dependent | 1.0× | 1.5–2.0× | 2.5× |

**Cross-check convention.** Small-deal marketplaces often quote *monthly* profit multiples. A 30–40×
monthly profit multiple ≈ 2.5–3.3× annual SDE. Convert explicitly rather than mixing conventions —
mixing them is a factor-of-12 error, the most common arithmetic failure in this domain.

**Scale effect.** Multiples rise with size, because larger businesses attract larger and more
professional buyer pools. A €500/mo product and a €50k/mo product in the same category do not trade
at the same multiple, and the small one trades toward the bottom of its band or below it — often it
does not trade at all, because the deal is too small to be worth anyone's diligence time.

**Pre-revenue.** There is no multiple. Use replacement cost and asset value (`02`). Do not construct
a pseudo-multiple from projected revenue.

## The adjustment engine

Start from the band, then move within (or outside) it factor by factor. Express each adjustment as a
percentage move on the multiple, and **explain every material one**. An unexplained adjustment is
indistinguishable from a fudge.

Cumulative discipline: adjustments compound but should not run away. If your net adjustment exceeds
about ±50%, you have probably picked the wrong band or the wrong business class — go back to
classification rather than pushing a bad base through a big correction.

### Upward factors

| Factor | Typical move | Why buyers pay for it |
|---|---|---|
| Strong growth (>50% YoY, sustained, verified) | +15% to +40% | Buyer inherits momentum, pays for future not present |
| Net revenue retention > 100% | +15% to +30% | Revenue compounds without acquisition spend |
| Low churn (<3%/mo consumer, <1.5%/mo B2B) | +10% to +25% | Durability of the cash flow being purchased |
| Annual/prepaid contracts | +10% to +20% | Cash flow certainty and lower churn mechanics |
| Gross margin > 85% | +5% to +15% | More of revenue converts to owner earnings |
| Diversified customers (top customer <10%) | +5% to +15% | No single point of revenue failure |
| Low founder dependency (<5 hrs/wk, documented) | +10% to +25% | Buyer gets an asset, not a job |
| Organic/defensible acquisition (SEO, integrations, word-of-mouth) | +10% to +25% | Growth doesn't stop when ad spend stops |
| Strong technical quality, tests, IaC | +5% to +15% | Lower transfer risk, cheaper to maintain |
| Excellent documentation & clean handover | +5% to +10% | Shortens diligence, reduces perceived risk |
| Proprietary data or genuine technical moat | +10% to +30% | Not replicable by a competitor's weekend project |
| Real brand / community / distribution | +5% to +20% | An asset that can't be rebuilt with code |
| Multi-year operating history | +5% to +15% | Survivorship is evidence |

### Downward factors

| Factor | Typical move | Why it scares buyers |
|---|---|---|
| No revenue | Method change, not a % | Not a business yet; see pre-revenue playbook |
| Declining revenue or users | −25% to −50% | Buyer inherits a problem they must solve first |
| High churn (>7%/mo consumer, >4%/mo B2B) | −20% to −40% | The revenue rebuilds itself from zero every year |
| Customer concentration >25% in one account | −20% to −40% | The deal is really one contract, and it can leave |
| High founder dependency | −15% to −35% | Value walks out the door at closing |
| Undocumented deployment / tribal knowledge | −10% to −25% | Transfer may simply fail |
| Significant technical debt | −10% to −25% | Buyer prices in a rewrite |
| Platform dependency (one store, one API, one traffic source) | −10% to −30% | A third party can end the business unilaterally |
| Unclear IP ownership (contractors, employer overlap) | −20% to −50%, or unsellable | Kills deals outright at diligence |
| Thin gross margin (heavy infra/inference) | −15% to −30% | Revenue overstates earnings |
| No analytics / unverifiable metrics | −10% to −25% | Buyer cannot confirm what they're buying |
| Weak differentiation, crowded market | −10% to −25% | Cheap to compete away |
| Security or compliance gaps (esp. with PII) | −10% to −30% | Inherited liability |
| Unresolved legal exposure / trademark risk | −15% to −40% | Uninsurable unknown |
| Revenue partly services/one-off | Exclude that portion | Doesn't transfer with the asset |
| Tiny absolute size (< ~€1k MRR) | −10% to −25% | Too small to be worth diligence for most buyers |

### Applying it

```
Adjusted multiple = base multiple × (1 + Σ adjustments)
Baseline value    = normalized metric × adjusted multiple
```

Then present the adjustment ledger in the report as a table, so the reader can disagree with any
single line without discarding the whole valuation. That transparency is what makes the number
defensible.

## Worked example

*B2B micro-SaaS, €4,200 MRR (€50,400 ARR), 24 months live, 61 customers, largest = 9% of revenue,
2.1%/mo churn, +40% YoY, 88% gross margin, founder ~8 hrs/week, deployment documented and on
Terraform, no test suite, acquisition is 70% organic search.*

| Step | Value | Reasoning |
|---|---|---|
| Class | B2B SaaS, small | <€10k MRR band |
| Base multiple | 3.0× ARR | Band 2.0–4.0×; starting above midpoint because retention and diversification are already strong |
| Growth +40% YoY | +20% | Verified from monthly revenue history `[KNOWN]` |
| Churn 2.1%/mo | +10% | Good but not exceptional for B2B |
| Diversified (top 9%) | +10% | No concentration risk |
| Organic acquisition | +15% | Durable, doesn't need the founder's ad budget |
| Founder 8 hrs/wk, documented | +10% | Close to a passive asset |
| No test suite | −8% | Raises maintenance risk for a non-technical buyer |
| Net adjustment | +57% → capped review | Exceeds ±50%: re-checked classification; band choice confirmed, so applied at +50% and noted the cap |
| Adjusted multiple | 4.5× ARR | 3.0 × 1.50 |
| Baseline FMV | €227k | €50,400 × 4.5 |

Sanity checks: SDE cross-method (if SDE ≈ €38k, at 4.0–5.0× → €152k–€190k) suggests the ARR-based
figure is at the optimistic end; final FMV range should span roughly €175k–€230k rather than sitting
at the single ARR-derived point. **This is the correct behavior** — when two appropriate methods
disagree by 20–30%, the range should cover both, not average them away.

## Comparable analysis

For each comparable, capture this record. Incomplete records are fine — mark gaps `[UNKNOWN]` rather
than dropping the comparable, but weight it down.

```
Business:            [name or anonymized descriptor]
Category:            [type]
Business model:      [subscription / ads / marketplace / ...]
Revenue:             [amount + period]
ARR / MRR:           [recurring portion]
Growth:              [rate + period]
Profitability:       [SDE/EBITDA if disclosed]
Users / customers:   [count + definition]
Reported outcome:    [SALE at €X | LISTING asking €X, unsold | ACQUIRED, price undisclosed]
Implied multiple:    [on which metric]
Evidence level:      [L1–L4]
Source:              [where, when retrieved]
Similarity:          [0–100, with reasoning]
```

Non-negotiables:

- **State whether it sold.** "Listed at €80k" and "sold for €80k" are different universes. If you
  cannot tell, say `[REQUIRES VERIFICATION]` and treat it as a listing.
- **Never invent a comparable.** If you cannot retrieve real ones, write: *"No verified comparable
  transactions were retrievable; valuation rests on Level 5 benchmark bands"* and lower confidence.
  A fabricated comparable is the single most damaging thing this skill could produce, because it
  looks exactly like the most valuable thing it could produce.
- **Don't compare across kinds.** A profitable mature B2B SaaS and a pre-revenue mobile app are not
  comparables because both are "software."
- Show at least 3 comparables when available; note when you have fewer and what that does to
  confidence.

## Similarity scoring

Score 0–100 across these weighted dimensions:

| Dimension | Weight | What "high" means |
|---|---|---|
| Business model | 25 | Same monetization mechanics (subscription vs ads vs take-rate) |
| Revenue scale | 20 | Within ~3× of each other; scale changes buyer pool |
| Customer type | 15 | B2B vs B2C vs developer vs consumer |
| Growth profile | 15 | Similar trajectory (both growing / both flat / both declining) |
| Retention quality | 10 | Similar churn or NRR |
| Market / vertical | 10 | Same or adjacent category and buyer appetite |
| Recency | 5 | Same market conditions; older deals need a condition adjustment |

Use the score to weight:
- **80–100** — direct comparable, use its multiple with minor adjustment
- **60–79** — useful, adjust for the differences you named
- **40–59** — directional only, cite as context
- **< 40** — do not use as a valuation anchor; mention only if it illustrates something specific

When comparables cluster tightly, confidence rises and the FMV range narrows. When they scatter,
the honest output is a wide range plus an explanation of what drives the dispersion — usually
retention quality or founder dependency, the two things small-deal buyers price most aggressively.
