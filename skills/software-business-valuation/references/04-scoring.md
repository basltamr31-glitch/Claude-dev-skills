# 04 — Scoring: Sellability, Exit Readiness, Confidence

Three scores, three different questions. Keeping them separate is the point.

| Score | Question | Common confusion |
|---|---|---|
| **Sellability** | How easily does this sell, and to how many buyers? | Not "how much is it worth" — a €15k micro-SaaS can be far more sellable than a €400k one |
| **Exit Readiness** | Could a transfer actually complete tomorrow? | Not sellability — a desirable asset can be totally unprepared |
| **Valuation Confidence** | How much does the evidence support the number? | Not quality — a bad business can be valued with high confidence |

Always show the sub-scores, not just the total. The sub-scores are what the founder acts on.

---

## Sellability Score (0–100)

Ten dimensions, 0–10 each, summed. Score against what a *buyer in this category* expects, not against
an abstract ideal.

### 1. Market Demand (0–10)
Is there active buyer appetite for this category right now?
- 9–10: hot category, buyers actively hunting (currently: AI tooling, B2B vertical SaaS, profitable micro-SaaS)
- 6–8: steady demand, sells with normal marketing
- 3–5: niche, needs the right buyer to appear
- 0–2: category buyers avoid (ad-supported consumer apps with declining installs, single-client tools)

### 2. Buyer Pool (0–10)
How many distinct buyers could plausibly transact?
- 9–10: hundreds of credible buyers (small profitable SaaS at accessible ticket sizes)
- 6–8: dozens
- 3–5: a handful — mostly strategic, mostly needing to be found
- 0–2: essentially one plausible buyer, or none

### 3. Revenue Quality (0–10)
- 9–10: recurring, annual contracts, low churn, diversified, verifiable in a payment processor
- 6–8: recurring monthly, moderate churn, reasonably diversified
- 3–5: recurring but high churn, or concentrated, or partly one-off
- 1–2: one-off/services revenue only
- 0: no revenue

### 4. Traction (0–10)
Actual demonstrated usage and its trend.
- 9–10: strong, growing, instrumented, verifiable
- 6–8: solid and stable
- 3–5: modest, or flat, or measurable only anecdotally
- 0–2: negligible usage, or usage that cannot be evidenced at all

### 5. Technical Transferability (0–10)
Could a new owner take this over without the founder?
- 9–10: IaC, documented, tested, standard mainstream stack, no personal accounts in the path
- 6–8: mostly documented, some manual steps, a competent dev could take it on
- 3–5: significant tribal knowledge; transfer needs a long handover
- 0–2: only the founder can deploy or operate it

### 6. Documentation (0–10)
Setup, architecture, ops runbook, customer-facing docs, financial records.
- 9–10: a buyer could self-onboard from the repo
- 6–8: good technical docs, thin ops/business docs
- 3–5: a README and hope
- 0–2: nothing

### 7. Founder Independence (0–10)
- 9–10: <5 hrs/week, no personal-relationship revenue, no founder-branded identity
- 6–8: 5–15 hrs/week, routine and documentable
- 3–5: 15–30 hrs/week, or sales depends on the founder personally
- 0–2: the founder *is* the product (personal brand, bespoke consulting, hand-held customers)

### 8. Competitive Position (0–10)
- 9–10: clear differentiation, defensible niche, real switching cost
- 6–8: solid position in a competitive market
- 3–5: undifferentiated, competing on price or luck
- 0–2: dominated by a free or better-funded alternative

### 9. Growth Potential (0–10)
Credible headroom a buyer can act on — the story that justifies paying today for tomorrow.
- 9–10: obvious, cheap levers (pricing power, untapped channel, adjacent segment)
- 6–8: real but requires investment
- 3–5: unclear or requires a strategic pivot
- 0–2: declining market or structural ceiling

### 10. Exit Readiness (0–10)
Map the Exit Readiness Score below: `round(exit_readiness / 10)`.

### Bands

| Score | Classification | What it means practically |
|---|---|---|
| 80–100 | Highly Sellable | Multiple interested buyers likely; competitive process possible; 1–3 months |
| 65–79 | Sellable | Sells on a marketplace or via broker with normal effort; 2–5 months |
| 50–64 | Sellable With Preparation | Fixable gaps must be closed first, or accept a discount; 4–8 months |
| 35–49 | Difficult to Sell | Narrow buyer pool; likely asset sale; expect a long search and a low price |
| 0–34 | Very Difficult to Sell | Not realistically sellable as a business today; recommend building or shelving |

Bands are guidance. Explain the score: name the two dimensions dragging it down and the two carrying
it, because those four items are the founder's actual to-do list.

---

## Exit Readiness Score (0–100)

Sixteen items. Score each: **1.0** ready, **0.5** partial, **0** absent or unknown. Not applicable
(e.g. Google Play for a web app) → drop the item and rescale over the remaining count.

```
Exit Readiness = (Σ item scores / applicable items) × 100
```

| # | Item | Ready means |
|---|---|---|
| 1 | Financial records | 12+ months of P&L or processor exports a buyer can audit |
| 2 | Analytics | Instrumented usage, retention measurable from real data |
| 3 | Technical documentation | Architecture, setup, dependencies documented |
| 4 | Infrastructure transferability | Accounts transferable, not tied to a personal identity |
| 5 | Source code organization | Version-controlled, coherent, no secrets committed |
| 6 | IP ownership | Clean chain: no unassigned contractor work, no employer conflict, licences compatible |
| 7 | Domain ownership | Held in a transferable registrar account, unlocked, not expiring |
| 8 | App Store ownership | Apple developer account / app transferable, no blockers |
| 9 | Google Play ownership | Play console transfer path understood |
| 10 | Database transfer process | Documented export/import, migration path, data-protection basis |
| 11 | Deployment documentation | A stranger can deploy from docs alone |
| 12 | Customer documentation | Customer list, support history, comms channels documented |
| 13 | Contracts | Written terms; assignability on change of control checked |
| 14 | Privacy / legal documentation | Privacy policy, ToS, GDPR basis, DPAs where needed |
| 15 | Security documentation | Auth model, secret handling, known issues, incident history |
| 16 | Operational independence | Runbook exists; business survives 2 weeks of founder absence |

Two rules that stop this from being a rubber stamp:

- **Source code existing is not transferability.** Item 4 and 11 fail routinely for projects with
  perfect code, because everything runs on the founder's personal cloud account with credentials in
  their head.
- **Unknown scores 0, not 0.5.** A buyer treats undocumented as absent, and so do you. If the user
  later supplies it, revise.

Present as a checklist with `[x] / [~] / [ ]` so the founder sees the gaps as tasks.

---

## Valuation Confidence (0–100)

How much the evidence supports the number. Five components:

| Component | Max | Full marks requires |
|---|---|---|
| **Financial evidence** | 30 | 12+ months verifiable revenue with cost detail, recurring vs one-off separated |
| **Retention & metric completeness** | 20 | Actual churn/NRR/cohorts, not estimates |
| **Comparable evidence quality** | 25 | Several L1–L2 transactions with similarity ≥ 60 |
| **Technical & asset verification** | 15 | Code inspected, infra understood, IP and ownership confirmed |
| **Business model clarity** | 10 | Model, pricing, customer type, maturity unambiguous |

Scoring guide per component:

- Financial evidence: 30 = audited/exported 12mo; 20 = self-reported 12mo; 12 = a few months;
  5 = a single stated figure; 0 = none
- Retention: 20 = cohort data; 12 = stated churn without cohorts; 6 = qualitative only; 0 = unknown
- Comparables: 25 = 3+ verified transactions, high similarity; 15 = 1–2 transactions or strong
  dataset evidence; 8 = listings only; 3 = L5 priors only; 0 = nothing
- Technical: 15 = full code + infra + ownership review; 9 = code reviewed, infra unclear;
  4 = docs only; 0 = nothing seen
- Model clarity: 10 = unambiguous; 5 = partly inferred; 0 = unclear

### Hard caps

Apply whichever is lowest:

- No revenue data at all → cap 40
- Retention completely unknown for a subscription business → cap 55
- No verified comparables (L5 priors only) → cap 55
- Code not inspected for a technology-asset-driven valuation → cap 60
- Business model or ownership materially unclear → cap 45

### Interpreting it

- **75–100**: tight range appropriate (±15–20%). Rare; usually needs real diligence access.
- **55–74**: normal for a well-documented small business. Range ±25–35%.
- **35–54**: directional. Range ±40–60%. Say plainly which 2–3 facts would raise it most.
- **< 35**: this is a framework and a starting point, not a valuation. Say so in the first paragraph
  of the executive summary rather than burying it.

Confidence is never raised by adding assumptions. The only ways up are more evidence and better
comparables — which is exactly the advice the founder needs to hear.
