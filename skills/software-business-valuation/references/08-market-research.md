# 08 — Market Research: Sourcing Real Evidence

## When to research

Research if you have web search or fetch tools **and** the valuation leans on a multiple. The
difference between a Level 5 prior and a retrieved Level 1–3 comparable is roughly 20 points of
confidence and is the difference between "an AI guessed a multiple" and "an advisor checked."

Skip research when the valuation is pure replacement-cost on a pre-revenue asset with no comparable
market — but say that you skipped it and why.

**If you have no research tools**: state it explicitly in the report's Evidence and Sources section:

> No external research tools were available in this session. Multiples are drawn from Level 5
> benchmark bands rather than retrieved transaction evidence. Confidence is capped accordingly.
> Verifying current comparables would be the single highest-value refinement to this valuation.

Never simulate research. Do not produce a plausible-looking comparable table sourced from memory and
present it as retrieved. If you recall general market conditions, label that recall as L5/L6 and note
your knowledge cutoff.

## What to look for, in priority order

1. **Completed transactions** — same type, same size band, with disclosed price and metrics (L1)
2. **Announced acquisitions** — often price-undisclosed; still useful for buyer appetite and who is
   acquisitive in this category (L2)
3. **Multiple studies and marketplace datasets** — published aggregate multiples with stated
   methodology and sample size (L3)
4. **Current listings** — appetite and asking-price levels; explicitly not transaction evidence (L4)
5. **Category signals** — funding activity, consolidation, platform policy shifts that change risk

## Search strategy

Run several angles; a single query gives a single view.

- Valuation benchmarks: `SaaS acquisition multiples <year>`, `micro SaaS sale multiple SDE`,
  `mobile app acquisition multiple <category>`
- Actual deals: `<category> acquired by`, `acquisition price undisclosed <category> SaaS`,
  `sold my SaaS for` (founder write-ups are often unusually detailed and genuinely L1/L2)
- Marketplace data: current listings in the category and size band, plus any published sold-listing
  statistics
- Competitive landscape: who competes, who has been acquiring, what pricing looks like
- Category risk: platform policy changes, model-provider pricing shifts, regulation

For AI products specifically, also check: current inference pricing for the models used (it moves
fast and directly determines gross margin) and any recent provider terms changes.

## Recording what you find

Every retrieved item gets:

```
Claim:          [what it establishes]
Source:         [publication/site + title]
Date:           [of the data, and of retrieval]
Evidence level: [L1–L4]
Sold or listed: [SOLD / LISTED-UNSOLD / ANNOUNCED, price undisclosed / UNKNOWN]
Caveat:         [sample size, self-reporting, staleness, selection bias]
```

The `Sold or listed` field is not optional. Conflating the two is the most common way small-business
valuations get inflated, because unsold high-priced listings persist and accumulate while completed
sales disappear from view.

## Reading market data critically

- **Survivorship and selection bias**: marketplaces publish successes; failed listings are invisible.
  Published "average multiple" figures usually describe sold listings only.
- **Self-reported metrics**: seller-provided revenue in listings is unverified by default.
- **Staleness**: multiples from a different rate environment or a pre-AI-boom period may not hold.
  Note the date of any dataset and whether conditions have shifted since.
- **Aggregate ≠ applicable**: "SaaS trades at 4× ARR" typically reflects businesses far larger than
  the one you're valuing. Scale down for small deals and say you did.
- **Category heat is temporary**: AI assets currently attract more buyer interest than fundamentals
  alone justify. That supports asking price and speed of sale; be careful about treating it as
  durable FMV.

## Using research in the report

In **Comparable Businesses / Transactions**, present the records in a table with evidence level and
sold/listed status visible in the table itself, not in a footnote.

In **Valuation Methodology**, say explicitly how research changed your multiple:

> Base band for small B2B SaaS was 2.0–4.0× ARR (L5 prior). Three retrieved transactions in the
> €3k–€6k MRR range implied 2.8×–3.6× (L2, similarity 65–75), so the base was set at 3.0× rather
> than the band midpoint.

In **Evidence and Sources**, list everything retrieved with dates, plus an explicit statement of
what you could *not* find. "No completed transactions were retrievable for AI-assisted [niche] tools
at this scale" is itself a finding — it tells the founder the buyer pool is thin and price discovery
will be difficult.
