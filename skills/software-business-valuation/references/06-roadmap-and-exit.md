# 06 — Roadmap Value Analysis, Sell-vs-Build, and Exit Planning

Contents:
- [Roadmap value analysis](#roadmap-value-analysis)
- [The verdict set](#the-verdict-set)
- [Patterns worth knowing](#patterns-worth-knowing)
- [Value creation roadmap](#value-creation-roadmap)
- [Sell now vs build more](#sell-now-vs-build-more)
- [30/60/90 day exit plan](#306090-day-exit-plan)

---

## Roadmap value analysis

The founder's real question is usually: **"If I only have limited time and money, what should I
build before selling?"** This is where the skill earns its keep, because the honest answer is
frequently "almost none of what's on your roadmap."

### The central asymmetry

Buyers pay for **proven, transferable cash flow and reduced risk**. They do not pay for features.
A feature affects the sale price only through one of these channels:

1. **Revenue** — it demonstrably raises MRR/ARR before the sale (multiplied by the multiple, so
   €500 MRR at a 3× ARR multiple = €18k of value)
2. **Retention** — it demonstrably lowers churn (raises the multiple *and* the base)
3. **Risk reduction** — it removes a diligence objection (raises the multiple and reduces retrade)
4. **Transferability** — it makes the asset operable without the founder (raises the multiple)
5. **Buyer appeal / strategic fit** — it makes the asset match what a specific buyer wants
6. **Nothing** — the majority of roadmap items

A feature shipped one month before listing has almost no chance of moving revenue or retention *in
the data a buyer will see*, because there's no trailing history. That timing reality — not the
feature's merit — is what usually decides the verdict. Say this explicitly; it reframes the whole
roadmap for most founders.

### Per-item analysis

For each significant roadmap item:

```
Roadmap item:            [name]
Dev cost / complexity:   [S / M / L / XL + rough weeks]
Business impact:         [what it changes operationally]
Revenue impact:          [None / Indirect / Direct + estimated €, labeled ESTIMATED]
Retention impact:        [None / Weak / Strong + mechanism]
User impact:             [who benefits, how many]
Risk reduction:          [which diligence objection it removes, if any]
Transferability impact:  [does it reduce founder dependency?]
Strategic value:         [does it make a named buyer type want this more?]
Exit value impact:       [HIGH / MEDIUM / LOW / NO MATERIAL EXIT VALUE]
Time-to-evidence:        [how long before a buyer can SEE the effect in data]
Verdict:                 [BUILD / DEFER / REMOVE / OUTSOURCE / BUILD ONLY IF A CUSTOMER REQUIRES IT]
```

`Time-to-evidence` is the field most analyses miss. A retention feature needs 3–6 months of cohort
data to show up in the numbers a buyer trusts. If the founder plans to sell in 3 months, that item
is a DEFER regardless of how good it is.

### Classification

- **HIGH EXIT VALUE** — directly raises revenue or retention with enough runway to evidence it, or
  removes a critical diligence blocker, or materially reduces founder dependency
- **MEDIUM EXIT VALUE** — real but indirect effect, or strong effect on a narrow buyer segment
- **LOW EXIT VALUE** — improves the product but won't visibly change the numbers or the risk profile
  before sale
- **NO MATERIAL EXIT VALUE** — pure feature work with no evidenced path to price

Be willing to classify most of a roadmap as LOW or NO MATERIAL. That is the finding. A roadmap
analysis that grades everything HIGH is flattery, not advice.

## The verdict set

| Verdict | Meaning | Typical trigger |
|---|---|---|
| **BUILD** | Do it before selling; it pays for itself in sale price | HIGH exit value, time-to-evidence fits the timeline |
| **DEFER** | Good idea, wrong time — leave it as upside for the buyer | Good product work whose value can't be evidenced before sale |
| **REMOVE** | Cut it entirely | Adds maintenance surface, complexity, or scope with no exit value |
| **OUTSOURCE** | Worth having but not worth the founder's weeks | Mechanical work (docs, tests, migrations) that a contractor can do cheaply |
| **BUILD ONLY IF A CUSTOMER REQUIRES IT** | Build against a signed commitment, not speculation | Enterprise features (SSO, SLA, audit logs) that are expensive and only valuable when a real customer is paying for them |

DEFER deserves a specific framing that founders find persuasive: **unbuilt roadmap is an asset in
the sale narrative.** "Here is a validated backlog with customer demand attached" is something a
buyer can get excited about. Half-built features are a liability. Selling the roadmap as upside is
often worth more than building it.

## Patterns worth knowing

Things that reliably score HIGH but rarely appear on a founder's roadmap:

- Instrumenting retention/cohort analytics (turns unverifiable claims into evidence; often the single
  highest-ROI item in the entire analysis)
- Writing the deployment runbook and moving infra off personal accounts
- Migrating 3–5 customers to annual prepaid contracts
- Fixing IP/ownership gaps (contractor assignments, licence conflicts)
- Building the financial pack: 12 months of clean processor exports and a normalized P&L
- Reducing owner hours: canned support responses, automating the manual weekly task
- Raising prices on new customers (immediate revenue impact, multiplied by the multiple)

Things that reliably score LOW despite feeling important:

- Redesigns and UI refreshes (buyers rarely pay for aesthetics)
- Rewrites and framework migrations (huge cost, invisible to price, and they *increase* risk pre-sale)
- Speculative new modules for segments you haven't sold to
- Mobile app for a web product with no mobile demand signal
- Integrations nobody has asked for
- "Scalability for 100× users" when you have 60 customers

Say the quiet part: a rewrite before a sale usually *destroys* value, because it consumes the runway,
introduces instability into the exact period the buyer will scrutinize, and resets the stability
history. If the roadmap contains one, address it head-on.

---

## Value creation roadmap

Separate from the product roadmap. This one exists purely to raise the exit price. Phase it, and
attach numbers.

```
CURRENT VALUE:  €X – €Y   (confidence NN/100)

PHASE 1 — Remove deal-blockers        [weeks 0–4]
PHASE 2 — Make the numbers provable   [weeks 2–12]
PHASE 3 — Raise revenue quality       [months 1–6]
PHASE 4 — Reduce founder dependency   [months 1–4]
PHASE 5 — Assemble the diligence pack [weeks before listing]

PROJECTED VALUE: €X – €Y   (confidence NN/100)
```

Order matters: blockers first (an IP problem makes everything else moot), then evidence (because
evidence is what lets the other improvements be *priced*), then substance.

Per action:

```
Action:               [specific and verifiable]
Cost:                 [€ and/or hours]
Difficulty:           [Low / Medium / High]
Time:                 [weeks]
Expected value impact:[€ range or multiple points, labeled ESTIMATED]
Confidence:           [High / Medium / Low]
Leverage:             [value impact ÷ effort]
```

Rank by **leverage**, not by size of impact. The founder has limited weeks; a €15k value gain from
two days of documentation beats a €40k gain from five months of building, both in ROI and in risk.

Be honest about the ceiling. If the projected value after six months of work is €95k–€130k versus
€70k–€90k today, state whether that €30k delta is worth six months of the founder's life — and
compare it to what six months of their time is worth elsewhere. That comparison is the actual advice.

---

## Sell now vs build more

Answer this explicitly. "It depends on your goals" is a non-answer; the founder hired you for a view.

### Structure

```
OPTION A — SELL NOW
Advantages:      [certainty, time freed, risk transferred, capital released]
Disadvantages:   [value left on the table, specific to this asset]
Expected value:  €X – €Y (today's expected transaction price)
Risks:           [may not find a buyer; long process; retrade]
Timeline:        [realistic months to close]

OPTION B — BUILD THEN SELL
Advantages:      [specific value increases, with the mechanism]
Disadvantages:   [opportunity cost, execution risk, market risk]
Expected value:  €X – €Y at [horizon], probability-weighted
Risks:           [growth may not materialize; category may cool; burnout; competitor entry]
Timeline:        [build period + sale process]
Required work:   [the specific BUILD items, not "keep improving"]

OPTION C — PREPARE THEN SELL   (usually the right answer)
The middle path: 4–12 weeks of exit-readiness work, no new features, then list.
Expected value:  €X – €Y
Why it usually wins: readiness work has the highest leverage and the shortest time-to-evidence.
```

### Deciding

Compare **probability-weighted** outcomes, not best cases:

```
Sell now:      expected transaction price × P(closing within horizon)
Build then sell: projected transaction price × P(the improvement lands) × P(closing)
                 − opportunity cost of the founder's time
                 − runway/cash cost of the build period
```

Lean **SELL NOW** when: growth is flat or declining; the founder is burned out (a real and material
input — a disengaged owner degrades the asset weekly); the category is currently in favor; the main
value drivers are already maxed; or the founder needs the capital.

Lean **BUILD MORE** when: growth is strong and verifiable (each month of growth compounds through
the multiple); a specific, near-term, high-confidence lever exists; the asset is below the size
threshold where serious buyers engage (roughly: under €1–2k MRR, the buyer pool thins dramatically,
so growing to €3k+ can more than double the price); or a named strategic buyer's interest is
plausible but the product isn't yet a fit.

Lean **PREPARE THEN SELL** when: the fundamentals are fine but exit readiness is weak — which is the
most common real-world situation, because founders build products and not diligence packs.

Give a specific recommendation with a horizon: **"Prepare for 8 weeks, then list."** Not "consider
your options." Then name the primary reason in one sentence, and the condition that would change
your mind (e.g. "if churn turns out to be above 6%/month, sell immediately instead").

---

## 30/60/90 day exit plan

Concrete, assignable actions with owners and outputs. No "explore" or "consider" verbs.

**Days 1–30 — Remove blockers and build evidence**
- Resolve IP/ownership gaps (contractor assignments, licence audit)
- Export 12 months of financial data; build the normalized P&L and revenue-quality split
- Instrument or reconstruct retention/cohort data
- Write the deployment runbook; move infra off personal accounts
- Inventory every asset to transfer (domains, store accounts, repos, third-party services, secrets)
- Decide venue and price strategy

**Days 31–60 — Package and prepare**
- Assemble the diligence pack (see `07-due-diligence.md`)
- Write the sale prospectus: what it is, who uses it, why it makes money, why you're selling
- Pre-answer the top 20 diligence questions in writing
- Execute the highest-leverage value actions from the value creation roadmap
- Build the strategic-buyer outbound list (5–15 named targets)
- Reduce owner hours; document support workflows

**Days 61–90 — Go to market**
- List on the chosen venue at the recommended asking price
- Run outbound to the strategic list in parallel
- Qualify buyers (funds available, ability to operate) before opening the data room
- Run diligence; expect a retrade attempt and know your walk-away number in advance
- Negotiate structure as well as price; agree the transition period explicitly
- Close: escrow, asset transfer checklist, customer communication plan

Adapt the plan to the recommendation. If the verdict is "build for 6 months," the 30/60/90 covers the
*preparation and build* period and the sale plan starts after. Don't hand a founder a listing plan
that contradicts your own recommendation — that inconsistency is a tell for a report assembled from
templates rather than reasoned through.
