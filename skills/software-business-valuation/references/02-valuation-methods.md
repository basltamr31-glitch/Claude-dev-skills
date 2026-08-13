# 02 — Classification and Valuation Methods

Contents:
- [Classification](#classification)
- [Method selection matrix](#method-selection-matrix)
- [The methods](#the-methods)
- [Triangulating multiple methods](#triangulating-multiple-methods)
- [Type playbooks](#type-playbooks)

---

## Classification

Classify before you calculate. Type determines method; using an ARR multiple on a pre-revenue app or
replacement cost on a profitable B2B SaaS produces a number that is not merely imprecise but wrong in
kind.

Assign a **primary** class and, where the business genuinely straddles, a **secondary** class.

**By revenue stage** (dominant axis — decides which methods are even legal):

| Stage | Definition | Valuation center of gravity |
|---|---|---|
| Pre-revenue | No paying customers | Asset / replacement cost; heavily discounted |
| Pre-product-market-fit | Some revenue, unstable, high churn | Blend of asset value and a low revenue multiple |
| Early revenue | Roughly < €5k MRR, some stability | Revenue/ARR multiple, low band; SDE if profitable |
| Established small | ~€5k–€50k MRR | ARR or SDE multiple, main band; comparables meaningful |
| Lower mid-market | > ~€50k MRR / >€600k ARR | ARR/EBITDA multiples; institutional buyers appear |

**By model:**

| Class | Marker | Notes for valuation |
|---|---|---|
| Micro-SaaS | Solo/tiny team, niche, low-touch subscription | SDE multiples dominate; buyer pool is individuals |
| B2B SaaS | Business customers, contracts, higher ACV | Best multiples; retention and concentration decide the band |
| B2C SaaS / consumer subscription | Individual subscribers | Higher churn structurally → lower multiple |
| Mobile app (paid/IAP/subscription) | Store-distributed | Platform dependency and store-account transfer are central |
| Mobile app (ad-supported) | Ad revenue | Volatile; lowest multiples; downloads trend is the key metric |
| Marketplace | Two-sided, take rate | Liquidity and repeat rate matter more than GMV |
| AI product / AI SaaS | LLM/ML core | Gross margin and model-provider dependency are the crux |
| Developer tool | Devs as users | Open-source dynamics, monetization conversion, community as asset |
| API business | Programmatic consumption | Switching cost is high = strong retention; usage concentration risk |
| Web app / utility | Browser-based, often freemium | Depends heavily on organic acquisition durability |
| Content/software hybrid | Software + SEO/audience | Traffic asset valued partly on content-site logic |
| Internal tool / bespoke | Built for one org | Usually near-zero market value unless the customer buys it |

**Cross-cutting flags** that change everything: single-customer concentration (>25%), platform
dependency (App Store, one API vendor, one traffic source), regulatory exposure, open-source licence
constraints, unclear IP ownership (contractors without assignment, employer-time development).

State the classification and *why it changes the method* — that sentence is what separates analysis
from output.

## Method selection matrix

| Situation | Primary methods | Secondary / sanity check | Explicitly reject |
|---|---|---|---|
| Pre-revenue, code only | Replacement cost, asset value | Comparable listings (L4, discounted) | Revenue/ARR/SDE multiples, DCF |
| Pre-revenue with real users | Asset value + per-user value | Replacement cost | ARR multiple, DCF |
| Early revenue, unprofitable | Revenue/ARR multiple (low band) | Replacement cost as a floor | EBITDA, DCF |
| Early revenue, profitable | SDE multiple | ARR multiple as cross-check | EBITDA (too small), DCF |
| Established, profitable, low growth | SDE multiple | Comparable transactions | ARR multiple alone |
| Established, high growth, thin profit | ARR multiple | SDE as a floor; comparables | Pure SDE (undervalues growth) |
| Mature, >€1M ARR, real team | EBITDA / ARR multiple | Comparable transactions, DCF | Replacement cost |
| Strategic fit with an identified acquirer | All of the above **plus** strategic value | — | Presenting strategic value as FMV |
| Marketplace | Revenue (take-rate) multiple, SDE | GMV as context only | Valuing on GMV |
| Declining business | SDE multiple, discounted | Asset value as a floor | Any growth-based method |

Always state the rejections. "We did not use a DCF because forward revenue cannot be projected with
any reliability at this stage" is a finding a buyer will respect.

## The methods

### 1. Revenue / ARR multiple

`Value = ARR × multiple`, where ARR = normalized recurring revenue only (see `01` §Normalizing).

Use when revenue is genuinely recurring and reasonably stable. The multiple comes from
`03-multiples-and-comps.md` and must be justified factor by factor. Exclude non-recurring revenue
from ARR entirely (or value it separately at a much lower multiple).

Failure modes: applying it to one-off revenue; using ARR from a single good month; ignoring that
churn makes "annual" recurring revenue not actually annual.

### 2. MRR multiple (small deals)

`Value = MRR × multiple`, common in small marketplace deals where multiples are quoted as
"×monthly profit" or "×MRR". Mostly a restatement of the ARR multiple (ARR multiple ≈ MRR
multiple ÷ 12); use whichever framing matches the comparable evidence you actually have, and be
explicit which you are quoting so you never accidentally mix the two.

### 3. SDE multiple

`Value = SDE × multiple`. SDE per `01` §Normalizing (crucially, net of realistic replacement labor).

The workhorse for profitable small software businesses, because the buyer pool is individuals buying
a cash-flowing asset. If profitable and under ~€500k ARR, this is usually the primary method.

### 4. EBITDA multiple

`Value = EBITDA × multiple`. Only meaningful when there is a real team, real management separation,
and enough scale that EBITDA ≠ SDE. Below roughly €1M revenue, EBITDA is usually a fiction dressed up
as rigor — use SDE instead and say why.

### 5. Comparable transactions

Find businesses of the same type, scale, and quality that **actually sold**, extract the implied
multiple, and apply it with a similarity adjustment. This is the strongest method when good
comparables exist. See `03-multiples-and-comps.md` §Comparable analysis.

### 6. Comparable listings

Same, but with live asking prices. Level 4 evidence. Useful for reading the *market's current
appetite* and for setting the asking price, weak for FMV. Discount listing prices materially when
inferring transaction value, and never call a listing a comparable "sale."

### 7. Replacement cost (build cost)

What it would cost a competent buyer to rebuild the product to its current state.

`Replacement cost = realistic engineering months × blended monthly rate × complexity factor`

Key discipline: this is *rebuild cost with hindsight*, not the founder's sunk hours. A rebuild skips
the dead ends, the abandoned features, and the learning. Typically **40–70% of original effort** for
a well-understood product.

Then apply the **buyer's discount**: buyers do not pay full replacement cost for unproven software,
because the alternative to buying is not only building — it's *not doing this at all*. In practice,
pre-revenue code with no traction transacts at a fraction of replacement cost. Replacement cost sets
a ceiling for pre-revenue assets, rarely a floor.

Use it for: pre-revenue products, technically substantial assets, acqui-hire-adjacent situations, and
as a sanity floor for revenue-generating businesses (a business rarely sells below the cost of
rebuilding it *if* it has proven demand).

Never use it as the primary method when revenue exists. "It took me 2,000 hours" is not a valuation
argument, and telling the founder this plainly is part of the job.

### 8. User / customer asset value

`Value = paying customers × value per customer`, or active users × per-user value for consumer apps.

Per-customer value is derived, not assumed — from the comparable evidence or from LTV logic
(ARPU × gross margin × expected lifetime), then discounted for transfer risk. Useful when revenue is
small but the customer base is strategically attractive, or for pre-revenue products with genuine
engaged usage.

Be brutal about what a "user" is. Free users of a consumer app with 5% D30 retention are worth
approximately nothing to an acquirer. Engaged users in a niche a competitor wants are worth real money.

### 9. Strategic value

What a specific acquirer would pay because the asset creates synergy: eliminates a competitor, fills
a product gap faster than building, delivers a customer list they want, or provides a team.

Rules:
- Strategic value is **always a separate number** from FMV. Never merge it in.
- It requires a *named, plausible* acquirer type with a stated synergy mechanism. Generic "a
  strategic buyer might pay more" is not analysis.
- It is contingent: no strategic buyer materializes in most small deals. Present as "if X, then Y."

### 10. DCF

Almost never appropriate below lower-mid-market. Requires defensible multi-year projections that
small software businesses cannot supply. If you use it, show the assumptions and treat it as a
sanity check only. Rejecting it explicitly is usually the right move — say why.

## Triangulating multiple methods

Run 2–4 methods. Do not average blindly — weight by evidence quality and method appropriateness.

```
Weighted FMV = Σ (method value × method weight)
```

Weight guidance:
- A method with strong L1–L3 evidence behind its multiple: weight it heavily
- A method used as a floor or ceiling (replacement cost, asset value): low weight, or use as a bound
- A method whose input is `[UNKNOWN]`-heavy: low weight, and say so

Then set the **range**, not just the point:
- Strong evidence, tight comparables → range ≈ ±15–20% around the weighted center
- Moderate evidence → ±25–35%
- Thin evidence, several unknowns → ±40–60%, or present scenario-based ranges instead

If methods disagree wildly (e.g. replacement cost €120k, ARR multiple €25k), **do not average them
into €72k**. That number describes nothing. Explain the divergence — it is usually the finding: "this
product cost far more to build than the market will pay, because demand is unproven." Then pick the
method the buyer will actually use, which is nearly always the demand-based one.

## Type playbooks

### Pre-revenue software (any form factor)

Center of gravity: asset sale, not business sale. Say this explicitly and early — it reframes the
founder's expectations correctly.

- Primary: replacement cost (heavily discounted) + asset value
- Buyer pool: small — entrepreneurs wanting a head start, competitors, occasionally a strategic buyer
- Value is dominated by: whether *anyone* wants this, code quality, niche attractiveness, any
  distribution asset (domain, SEO, waitlist, store presence)
- Typical outcome: a fraction of build cost. Set expectations honestly.
- The highest-value advice is almost always: get to first revenue before selling. Even €500 MRR
  moves the asset from "speculative" to "validated," and that reclassification usually beats months
  of further feature work.

### Mobile app

- Store account and listing transfer is a *precondition*, not a detail. Bundle IDs, developer
  accounts, and review history transfer awkwardly; a transferred listing can lose ranking.
- Ad-supported apps: lowest multiples, valued on trailing net ad revenue with a volatility discount.
- Subscription apps: better, but net of the 15–30% store commission — always value on net proceeds.
- Download trend over 6–12 months matters more than cumulative downloads. Cumulative downloads is a
  vanity metric; a buyer looks at the last 90 days.
- Platform-policy risk is a real, nameable discount (a policy change can end the business).
- Check: ASO position, rating and review volume, organic vs paid installs, D1/D7/D30 retention.

### Micro-SaaS

- SDE multiple is the primary method; the buyer is an individual operator buying a job-plus-asset.
- Owner hours are the crux: 5 hrs/week is attractive, 30 hrs/week is a job with a bad salary.
- Low churn and organic acquisition (SEO, directories, integrations marketplace) are the two things
  that most raise the multiple.
- Buyer pool is broad and liquid at small tickets — that's good for speed of sale, neutral for price.

### B2B SaaS

- The best multiples, but earned: net revenue retention, contract terms, and customer concentration
  drive the band far more than raw ARR.
- Concentration is the classic killer: one customer at 40% of revenue can cut the multiple in half,
  because the buyer is really buying one contract.
- Annual prepaid contracts materially raise value over monthly.
- Check: contract assignability on change of control (a non-assignable contract may not survive the
  sale — this is a diligence landmine worth flagging early).

### Marketplace

- Value on **net revenue (take rate)**, never GMV. Note GMV as context only.
- Liquidity is the asset: repeat rate, match rate, time-to-fill, supply/demand balance.
- Chicken-and-egg risk means a marketplace with thin liquidity is much closer to a pre-revenue asset
  than its revenue suggests.
- Disintermediation (users transacting off-platform) is a specific, checkable risk.

### AI product / AI SaaS

- Gross margin is the headline issue. Inference cost can make a "SaaS" a 45%-margin business, and
  buyers now check this first. Compute margin after model API costs at current usage.
- Model-provider dependency: pricing changes, deprecations, and terms shifts are outside the owner's
  control. A product that is a thin wrapper on one provider carries a defensibility discount.
- Ask what the actual moat is: proprietary data, evaluation infrastructure, workflow integration,
  distribution, or switching cost. "We use a good prompt" is not a moat, and saying so plainly is
  more useful to the founder than a polite hedge.
- Growth in this category can be genuine or hype-driven — test retention, not signups. High growth
  with weak retention is the signature pattern of AI products that later collapse.
- Counterweight: buyer appetite for AI assets is currently strong, which supports the *asking price*
  and speed of sale even where fundamentals are thin. Distinguish appetite from value.

### Developer tools

- Open-source core: check the licence. A permissive licence means a buyer can fork the value away;
  the asset is the brand, community, and hosted service, not the code.
- Conversion from free to paid is the key metric; community size alone is weakly monetizable.
- Buyer pool skews strategic (companies selling to the same developers).

### API business

- High switching cost = strong retention = strong multiple, if usage is diversified.
- Usage concentration (top 3 consumers > 50% of calls) is the equivalent of customer concentration.
- Check rate limits, SLA commitments, and whether the API depends on an upstream data source that
  could revoke access — that upstream dependency is often the real risk.

### Content/software hybrid

- Split the valuation: software business (multiple on recurring revenue) + content/traffic asset
  (valued on content-site logic, typically a monthly-profit multiple).
- Organic search dependency is a concentration risk in disguise — a single algorithm update is a
  single point of failure. Check traffic trend over 12+ months, not 3.
