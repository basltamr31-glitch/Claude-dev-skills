# 05 — Buyer Analysis and the Four-Price Model

Contents:
- [Why buyer analysis comes before pricing](#why-buyer-analysis-comes-before-pricing)
- [Buyer archetypes](#buyer-archetypes)
- [Per-buyer analysis format](#per-buyer-analysis-format)
- [Financial vs strategic value](#financial-vs-strategic-value)
- [The four-price model](#the-four-price-model)
- [Deal structure](#deal-structure)
- [Where to sell](#where-to-sell)

---

## Why buyer analysis comes before pricing

Price is not a property of the asset. It is a property of the asset *and the buyer pool*. The same
codebase is worth €20k to an entrepreneur buying cash flow and €150k to a competitor who wants the
customer list off the market.

So: identify the buyers, understand what each would pay and why, and only then set prices. A four-price
model built without naming the buyer is a guess with decimal places.

## Buyer archetypes

| Archetype | Typical ticket | What they buy on | Objections they raise |
|---|---|---|---|
| **Individual entrepreneur / operator** | €5k–€150k | Cash flow, low owner-hours, simple ops | "Can I run this alone?" "Is the revenue real?" |
| **Developer / technical buyer** | €2k–€60k | Code quality, a head start, a niche they know | "Is this stack maintainable?" "Why are you selling?" |
| **Micro-SaaS investor / portfolio buyer** | €20k–€500k | SDE multiple, repeatability, clean books | "Show me 12 months of Stripe." "What's churn?" |
| **Strategic competitor** | Wide | Removing a competitor, taking the customers | "Will your customers stay after migration?" |
| **Adjacent SaaS company** | Wide | Product gap filled faster than building | "Is this cheaper than building it ourselves?" |
| **Vertical software company** | Medium–large | Deepening an industry offering | "Does this fit our compliance posture?" |
| **Agency / consultancy** | €5k–€100k | Productizing services, tooling for existing clients | "Can we white-label it?" |
| **PE / roll-up / aggregator** | €500k+ | EBITDA, systems, management depth | "Is there a team?" "Is it institutionalizable?" |
| **Product studio / holding co** | €10k–€200k | Portfolio economics, operational leverage | "How much of our operator time does this need?" |
| **Marketplace aggregator (app/plugin)** | Varies | Category consolidation, distribution synergy | "What's the platform risk?" |
| **Existing customer** | Varies | Bringing a critical dependency in-house | "Why should we pay when we could just leave?" |

Underrated in practice: **existing customers** (for B2B tools they depend on) and **competitors who
are already losing deals to you**. Both are strategic buyers hiding in plain sight, and both are
often overlooked because founders think of "buyers" as marketplace strangers.

Also worth naming honestly: for many pre-revenue or sub-€500-MRR products, the realistic buyer pool
is **near zero**, and the deal that closes is an asset sale to a developer for low four figures. Say
that when it's true. It's the most useful sentence in the report.

## Per-buyer analysis format

For each relevant archetype:

```
Buyer type:              [archetype]
Why they might buy:      [specific to this asset, not generic]
Strategic fit:           [High / Medium / Low] + the mechanism
Likely objections:       [the two or three things they will actually push back on]
Price premium potential: [None / +10–25% / +25–100% / transformative] + why
Likelihood of interest:  [High / Medium / Low] + why
Where to reach them:     [channel]
```

The objections field is where the value is. It is a preview of the negotiation, and every objection
you can name is something the founder can fix before listing rather than concede at the table.

## Financial vs strategic value

**Financial buyer value** = what someone pays for the cash flow. Anchored to multiples of SDE or ARR.
This is normally your FMV.

**Strategic buyer value** = financial value + quantified synergy:

```
Strategic value ≈ financial value + (cost avoided by not building) + (revenue gained from synergy)
                  − (integration cost and risk)
```

Discipline:
- Present strategic value **separately and conditionally**: "IF a competitor in [specific category]
  is acquisitive, the range could extend to €X–€Y."
- Name the mechanism. "Synergy" without a mechanism is noise.
- Never fold contingent strategic value into FMV or the expected transaction price. Most small
  processes do not surface a strategic buyer, and building the founder's expectations on one is how
  a sellable asset sits unsold for a year.
- Do state how to *test* for it: a short outbound list of 5–15 named-category acquirers is often the
  single highest-ROI action in the whole exit plan.

---

## The four-price model

The four prices exist because they answer four different questions. Collapsing them destroys the
report's usefulness.

### Fair Market Value (FMV)

The evidence-supported range from `02` triangulation + `03` adjustments. This is the analytical
answer, before any negotiation psychology.

Always a range. Width comes from confidence (`04`): high confidence ±15–20%, low confidence ±40–60%.

### Anchor all three derived prices to the FMV centre

Derive the asking, expected, and fast-sale prices from the **FMV centre**, not from each other.

This matters more than it sounds. If you set the ask as a premium over FMV *high*, and then set the
expected transaction as a percentage of the ask, the uncertainty width leaks into the outcome: a
low-confidence valuation produces a wide range, a wide range produces a high ceiling, and the
expected transaction ends up *above* the FMV centre. That says "we're unsure, therefore it's worth
more," which is backwards. A wide range must mean "we don't know," never "it's worth more."

| Sellability | Asking (× FMV centre) | Expected transaction (× FMV centre) | Fast-sale (× FMV centre) |
|---|---|---|---|
| 80–100 | 1.20 | 1.00 – 1.12 | 0.65 – 0.80 |
| 65–79 | 1.25 | 0.88 – 1.02 | 0.55 – 0.70 |
| 50–64 | 1.30 | 0.75 – 0.92 | 0.45 – 0.60 |
| 35–49 | 1.30 | 0.60 – 0.80 | 0.30 – 0.50 |
| 0–34 | 1.25 | 0.42 – 0.65 | 0.20 – 0.40 |

Two constraints on the ask:
- It must clear FMV high (never market below your own valuation ceiling): `ask ≥ FMV_high × 1.05`
- It must not run away on very wide ranges: `ask ≤ FMV_centre × 1.75`

### Recommended Asking Price

A single number, because buyers expect one. Above FMV to create negotiating room — but not so far
above that credible buyers self-select out before the first conversation.

Context adjustments: marketplaces with visible listing histories reward realistic asks; a private
process with three named strategic buyers can carry a higher anchor; a very thin buyer pool argues
for an ask close to FMV, because you cannot afford to filter anyone out.

Report the **implied expected-as-%-of-ask** alongside it, because that's how founders think. If it
comes out below ~70%, say plainly that the ask is an exploratory anchor rather than a target, and
that the fix is better evidence (narrowing FMV), not a bigger number.

### Expected Transaction Price

What actually closes, as a range. This is the number the founder should plan their life around.

Two forces pull it below the ask: **negotiation** (buyers expect to win something) and **diligence
retrade** (buyers find things and reprice). Weak documentation and unverifiable metrics don't just
lower FMV — they create a second discount at the table, which is why exit-readiness work pays twice.

Sanity check: the expected range should straddle or sit just below the FMV centre. Above FMV high,
your factors are wrong; below FMV low, your FMV is inflated.

Also note **probability of closing at all**. For low-sellability assets, "expected transaction price
€18k–€24k, with maybe a 30% chance of finding any buyer within six months" is the honest framing, and
it changes the founder's decision more than the number does.

### Fast-Sale Price

What clears in roughly 30 days. A genuinely different product: the buyer is being paid (in discount)
to move fast, skip diligence, and absorb risk. Use the fast-sale column above.

Fast-sale discounts widen when: revenue is unverified (buyer can't do quick diligence), transfer is
complex, the category is out of favor, or the ticket is large relative to the buyer pool's typical
cash capacity.

### Invariants

These must hold. The script enforces them; check them by hand too.

```
fast_sale_low ≤ fast_sale_high ≤ expected_low ≤ expected_high ≤ asking_price
fmv_low ≤ fmv_high ≤ asking_price
```

If `expected_high > asking_price`, something is wrong: nobody pays more than the ask in a small
private deal.

Where fast_sale_high would exceed expected_low, present them as an explicitly overlapping band and
say why (usually: very high sellability, where speed costs little).

### Presenting the four prices

```
FAIR MARKET VALUE          €X – €Y      [what the evidence supports]
RECOMMENDED ASKING PRICE   €Z           [listing anchor]
EXPECTED TRANSACTION PRICE €A – €B      [what likely closes]
FAST-SALE PRICE            €C – €D      [~30-day exit]
```

Every one of them gets a one-line "why this number." A four-price block without reasoning is a
horoscope.

---

## Deal structure

Structure moves the effective price as much as the headline does — and small-software buyers are
often more flexible on structure than on price.

| Structure | Effect | When to recommend |
|---|---|---|
| All cash at close | Cleanest; usually the lowest headline | Seller wants certainty; asset is small |
| Cash + earnout (6–24 mo) | Raises headline, defers risk to seller | Buyer doubts retention/growth claims |
| Seller financing (20–40% deferred) | Widens buyer pool a lot at small tickets | Buyer pool is cash-constrained |
| Transition/consulting agreement (1–6 mo) | Bridges founder dependency | High founder dependency — often *required*, not optional |
| Asset sale vs entity sale | Asset sale is simpler and typical below ~€500k | Default to asset sale for micro deals |

If founder dependency is high, expect a transition period to be a condition of any deal. Price that
in as an obligation on the founder's time, not a bonus.

**Escrow / holdback** (10–20% for 3–6 months) is common where metrics need post-close verification.
If your report flagged `[REQUIRES VERIFICATION]` on revenue, expect a holdback and say so.

## Where to sell

Match the venue to the asset — the wrong venue is a slow "no."

| Venue | Best for | Notes |
|---|---|---|
| Micro-acquisition marketplaces | €1k–€100k, self-serve, small SaaS and apps | Fast, broad, price-competitive; listing fees/commissions apply |
| Broker (specialist software) | €100k–€5M | 10–15% commission; worth it above ~€150k for buyer access and process |
| Direct outbound to strategics | Any size with a named acquirer thesis | Highest price potential, slowest, needs a real target list |
| Community / niche channels | Developer tools, niche B2B | Cheap and effective when the audience overlaps the buyer pool |
| App-specific marketplaces | Mobile apps, plugins, extensions | Platform transfer mechanics dominate the process |
| Existing customers / partners | B2B with dependent customers | Underused; often the fastest close |

Recommend a **primary and a fallback** venue, with the reason. And note the time cost: a broker
process on a €40k asset usually isn't worth it, while listing a €400k B2B SaaS on a self-serve
marketplace leaves money on the table.
