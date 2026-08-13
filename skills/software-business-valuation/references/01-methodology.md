# 01 — Methodology: Evidence, Extraction, and Honest Uncertainty

Contents:
- [Evidence hierarchy](#evidence-hierarchy)
- [Labeling every data point](#labeling-every-data-point)
- [Minimum viable input](#minimum-viable-input)
- [Context extraction: reading a project like a buyer](#context-extraction-reading-a-project-like-a-buyer)
- [Inference rules: what code can and cannot tell you](#inference-rules-what-code-can-and-cannot-tell-you)
- [Normalizing financials](#normalizing-financials)
- [Common seller distortions to correct](#common-seller-distortions-to-correct)

---

## Evidence hierarchy

Every valuation input carries an evidence level. Report it. The whole point is that a reader can see
which parts of your number rest on rock and which rest on sand.

| Level | Kind of evidence | Example | Weight |
|---|---|---|---|
| **L1** | Actual completed transaction, verified | Closed deal with disclosed price and metrics for a directly comparable business | Highest |
| **L2** | Public acquisition / valuation disclosure | Announced acquisition with reported price; public company multiple | High |
| **L3** | Reliable industry dataset / broker report | Published multiple studies from marketplaces or M&A advisories, with methodology | Medium-high |
| **L4** | Current listings (asking prices) | A live marketplace listing at €X | Medium-low — **wants, not results** |
| **L5** | Expert or marketplace benchmark bands | The prior bands in `03-multiples-and-comps.md` | Low |
| **L6** | Model inference | Your own reasoning with no external anchor | Lowest |

Rules:

1. **Never present L4–L6 with the visual authority of L1–L2.** No confident bolded single number
   sourced from your own inference.
2. **Listings are not transactions.** Marketplace asking prices systematically overstate outcomes;
   listings that don't sell stay visible while ones that do disappear, so the visible pool skews high.
   When you cite a listing, write "asking price, unsold" next to it.
3. If your entire multiple rests on L5 priors, confidence cannot exceed ~55/100 regardless of how
   complete the business data is.
4. Cite the source for anything L1–L4: name, date retrieved, and what was actually disclosed
   (many announcements disclose no price — say "price undisclosed" rather than inferring one).

## Labeling every data point

Use these inline tags in the report. They are the reader's trust mechanism.

- `[KNOWN]` — from the user's materials or a source you retrieved. Point at it.
  > MRR: €2,050 `[KNOWN — financials.md, June figures]`
- `[ESTIMATED]` — derived arithmetically from known inputs. Show the work.
  > ARR: €24,600 `[ESTIMATED — MRR €2,050 × 12; assumes no seasonality]`
- `[INFERRED]` — reasoned from indirect signals. Name the signal and the uncertainty.
  > Founder dependency: high `[INFERRED — deploy steps in README are manual and reference the
  > founder's personal AWS account]`
- `[UNKNOWN]` — absent. Say so; do not substitute.
  > Churn: `[UNKNOWN]` — no cohort or cancellation data provided. This is the single largest driver
  > of the valuation range below.
- `[REQUIRES VERIFICATION]` — a buyer's diligence will test this and you could not.
  > Stripe revenue as reported `[REQUIRES VERIFICATION — needs raw Stripe export, not a summary]`

If more than a third of the profile is `[UNKNOWN]`, lead the executive summary with that fact. The
most valuable thing you can tell some founders is "you cannot sell this until you can answer six
questions, and here they are."

## Minimum viable input

You can produce something useful from very little, but be honest about which tier you are in.

**Tier A — full context** (code + docs + financials + analytics): full report, confidence up to 75–85.

**Tier B — business metrics only** (revenue, users, churn, costs, no code access): full report minus
technical due diligence; flag technical risk as `[UNKNOWN]` and note that a buyer will discount for
un-inspected code. Confidence up to ~70.

**Tier C — code and docs only, no financials**: valuation must run on replacement cost / asset value /
comparable-listing logic, not revenue multiples. Confidence rarely above 45. Say clearly: *"This is an
asset valuation, not a business valuation."*

**Tier D — a sentence** ("I built a habit tracker, what's it worth?"): do not refuse and do not
fabricate. Give the honest structural answer (what drives value for this category, what the plausible
range is across scenarios) and ask for the highest-leverage facts:

1. Monthly revenue, and how much is recurring vs one-off
2. Paying customers and total active users (with the definition of "active")
3. Retention or churn — even roughly, even anecdotally
4. Monthly running costs (infra, tools, contractors)
5. Time you personally spend on it each week, and what breaks without you
6. Who owns the code, domain, store listings, and any third-party accounts
7. Platform dependencies (App Store, a single API vendor, one big customer)
8. How long it has been live and the trend over the last 6 months

Present these as "the eight facts that would let me halve this range," not as a form to fill in.

## Context extraction: reading a project like a buyer

Build **one model of the business**. The classic failure is summarizing each file separately; the
value is in the cross-references.

What each artifact actually tells you:

| Artifact | What a buyer reads out of it |
|---|---|
| `README.md` | Positioning, target user, setup friction. A README a stranger can't follow = transfer risk. |
| `PLAN.md` / roadmap | What the founder believes creates value — often diagnostic of misallocation |
| Source tree | Maturity, test coverage, coupling, whether one person could take it over |
| DB schema / migrations | The real data model, the actual entities, multi-tenancy or not, data moat |
| Migration history | Development velocity and stability over time; churn in core tables = instability |
| API docs | Integration surface, whether third parties depend on you (switching cost = moat) |
| Deploy config / IaC | Reproducibility. IaC = transferable. Manual steps in someone's head = founder-locked. |
| CI config | Engineering discipline; absence isn't fatal at this size but is a diligence flag |
| `package.json` / deps | Stack liquidity (how many buyers can maintain it), abandoned dependency risk |
| Auth / billing code | Whether revenue is genuinely recurring and how hard billing transfer will be |
| Analytics wiring | Whether retention claims can ever be substantiated |
| Store listings | Ratings, review volume, download trend, ranking — and *who owns the account* |
| Financials | The core, but see "seller distortions" below |
| `.env.example`, config | Vendor lock-in, cost drivers, secrets hygiene |
| Test suite | The single best proxy for how safely a new owner can change things |

Cross-reference deliberately. Examples of the reasoning that makes this feel like a real advisor:

- Roadmap promises enterprise SSO, but the schema has no organization/tenant table → the roadmap item
  is far larger than the founder thinks; discount the timeline and flag it in the roadmap analysis.
- README claims "thousands of users," schema has no analytics/events table and no third-party
  analytics dependency → the claim is unverifiable; mark `[REQUIRES VERIFICATION]`, not `[KNOWN]`.
- Billing code implements one-off Stripe charges, but the founder describes "subscribers" → revenue
  is not recurring; this changes the valuation method entirely.
- Deployment doc says "ssh into the box and run the script" → founder dependency and transfer risk,
  worth a real discount, and it's cheap to fix (high ROI in the value creation roadmap).

Record the profile using `assets/profile-template.md`.

## Inference rules: what code can and cannot tell you

Code is strong evidence about **technical risk and transferability**. It is weak-to-zero evidence
about **demand**. Keep the two separate; conflating them is how technically impressive, commercially
worthless products get overvalued.

Legitimate inferences from code:
- Architecture quality, coupling, test coverage, dependency health
- Whether the product is genuinely multi-tenant (schema-level)
- Whether billing is subscription or one-off
- Deployment reproducibility and infrastructure cost shape
- Presence of instrumentation (can retention ever be proven?)
- Rough build effort (see replacement cost in `02-valuation-methods.md`)

Illegitimate inferences from code — never do these:
- Revenue, MRR, or ARR from schema or pricing constants (a `price` column is not revenue)
- User counts from anything other than actual data (seed data is not users)
- Retention or churn from anything but cohort data
- Market size, demand, or competitive position from feature lists
- That a feature works, is used, or is wanted, because it exists

When a user's claim conflicts with code evidence, report both and side with the code on technical
matters and with data on commercial matters — then flag the conflict. Buyers find these conflicts.
Finding them first is the entire value of pre-sale diligence.

## Normalizing financials

Before applying any multiple, normalize.

**Revenue quality ladder** (highest to lowest value per euro):
1. Annual contracts, auto-renew, multi-year, low churn, B2B
2. Monthly subscriptions, low churn, diversified
3. Monthly subscriptions, high churn or concentrated
4. Usage-based revenue with stable accounts
5. In-app purchases / consumer subscriptions with app-store dependency
6. Ad revenue (platform-dependent, volatile)
7. One-off sales, services, consulting (often valued at a fraction, or excluded entirely)

Separate them. A business with €5k "revenue" that is €1.5k subscriptions and €3.5k founder consulting
is a €1.5k-MRR SaaS with a job attached. Buyers pay a SaaS multiple for the first and near-nothing
for the second, because the consulting leaves with the founder.

**Earnings normalization (SDE)**: Seller's Discretionary Earnings = net profit
+ owner's salary/draw
+ genuinely one-off costs
+ non-business personal expenses run through the entity
− a realistic cost to replace the owner's actual working hours (this last one is the honest step
  most sellers skip)

That last subtraction matters: if the founder works 25 hrs/week on support and the SDE calculation
assumes a buyer inherits zero labor cost, the SDE is fiction. State the replacement-labor assumption.

**Costs to include that founders routinely omit**: infrastructure at current scale (not free-tier),
third-party API costs (especially LLM inference), app store commission (15–30%), payment processing
(~3%), support time, domain/SSL/tooling, and any contractor spend.

**Gross margin** must be computed after variable cost of service. AI products with heavy inference
cost can run 40–60% gross margin, not the 80–90% buyers assume for SaaS — this is a first-order
valuation issue, not a footnote.

## Common seller distortions to correct

Correct these silently in the analysis and name them in the report. They are the difference between
a valuation and a wish.

| Distortion | Correction |
|---|---|
| "Users" meaning signups | Ask for actives on a stated definition (e.g. WAU with a real action). Absent that, treat signups as low-value. |
| Best month presented as run-rate | Use trailing 3–6 month average; note volatility explicitly. |
| Development hours valued at agency rates | Replacement cost uses realistic rebuild cost, not sunk hours. See `02`. |
| Gross revenue before store/processor cut | Net it out. 30% App Store commission is real. |
| Founder labor costed at zero | Subtract a market rate for the hours actually worked. |
| Pipeline/LOIs counted as revenue | Excluded from valuation; mention as upside narrative only. |
| One-off spike (a launch, a press hit) annualized | Strip it; show the underlying baseline. |
| "Profitable" without owner comp | Restate as SDE with the replacement-labor line visible. |
| Total addressable market cited as if capturable | TAM is context, never a valuation input at this size. |
