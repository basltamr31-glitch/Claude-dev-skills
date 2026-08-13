# 07 — Due Diligence: Question Bank, Technical Review, Evidence Gaps

The purpose of this section in the report is not to educate the founder about diligence. It is to
**surface, before listing, the questions that will otherwise surface during negotiation** — because
a question answered in the prospectus costs nothing, and the same question answered under pressure
in week three costs 10–20% of the price.

Structure the output as: the questions → what evidence exists → what's missing → what to do about it.

---

## Technical due diligence

What a competent technical buyer checks, and what each finding means for price.

| Area | What they check | Red flag → price effect |
|---|---|---|
| Architecture | Coherence, coupling, whether one dev can hold it in their head | Sprawling microservices for a 60-customer product → maintenance cost, discount |
| Code quality | Consistency, dead code, TODO density, obvious hacks | High debt → buyer prices in rewrite time |
| Tests | Existence, coverage of critical paths, CI green | No tests → buyer can't safely change anything → real discount |
| Dependencies | Abandoned packages, security advisories, licence conflicts | GPL in a proprietary product → potentially deal-ending |
| Data model | Multi-tenancy, integrity constraints, migration history | No tenant isolation in a "B2B SaaS" → the product isn't what it claims |
| Secrets | Committed credentials, key rotation, access control | Secrets in git history → security incident risk transfers to buyer |
| Infrastructure | Reproducibility, IaC, cost at current scale, single points of failure | Hand-built server → transfer may fail outright |
| Deployment | Can a stranger deploy from docs? | Undocumented → founder must stay; discount + transition obligation |
| Monitoring | Errors, uptime, alerting | None → buyer inherits unknown reliability |
| Scalability | Headroom relative to realistic growth | Usually less important than founders think at this size |
| Security | Auth model, PII handling, encryption, incident history | PII without a compliance basis → inherited liability |
| Platform deps | Store policies, API vendor terms, model provider terms | One vendor can end the business → structural discount |

Two things to state plainly whenever they apply:

- **"The code exists" ≠ "the asset is transferable."** Transferability is about accounts, docs, and
  operational knowledge at least as much as source.
- **Vendor lock-in is a valuation input.** A product that only runs on one founder's Firebase project
  with hardcoded project IDs is worth measurably less than the same product on portable infra.

## The question bank

Present the ones relevant to this business, with the current answer state.

### Financial
- 12–24 months of revenue by month, split recurring vs one-off?
- Raw processor exports (Stripe/Paddle/App Store Connect), not summaries?
- Full cost breakdown including infra, APIs, tools, contractors, support?
- Gross margin after all variable costs (including inference/API costs)?
- Refund and chargeback rates?
- Revenue concentration: top 5 customers as % of revenue?
- Any revenue that depends on the founder personally?
- Pricing history and any grandfathered plans?

### Customers
- Customer count, definition of active, and the trend over 12 months?
- Monthly churn (logo and revenue), and cohort retention curves?
- Net revenue retention?
- Acquisition channels and their proportions — how much is organic vs paid?
- CAC and payback period, if paid acquisition exists?
- Support volume and average response burden?
- Any contractual commitments, SLAs, or custom terms?

### Product
- What do users actually do, measured — not intended?
- Feature usage distribution (what fraction of the product is dead weight)?
- Known bugs, outstanding issues, incident history?
- Roadmap and the demand evidence behind it?
- Competitive landscape and why customers pick this?

### Technical
- Repository access, commit history, contributor list?
- Test coverage and CI status?
- Architecture and deployment documentation?
- Infrastructure inventory and monthly cost at current usage?
- Third-party services, their terms, and their transferability?
- Known technical debt with rough remediation cost?

### Legal / IP
- Who wrote every line, and is it assigned? (Contractors, employees, employer-time work.)
- Open-source licence audit — anything copyleft in a proprietary product?
- Trademark status, and any naming conflicts?
- Domain ownership and registrar access?
- App Store / Play developer account ownership and transfer eligibility?
- Terms of Service and Privacy Policy in force?
- Any disputes, claims, or outstanding obligations?

### Security & compliance
- What PII is stored, where, and under what legal basis?
- GDPR/CCPA posture: DPAs, data deletion, processing records?
- Auth implementation, password/session handling, MFA?
- Secret management and access-control inventory?
- Any past incidents or breaches?

### Operations
- Hours per week the owner works, by activity?
- What breaks if the owner disappears for two weeks?
- Runbook for routine and emergency operations?
- Any staff, contractors, or agencies, and do they stay?
- Vendor accounts and who controls billing?

### Transfer mechanics
- Full inventory of transferable assets (repos, domains, accounts, service subscriptions, social)?
- Which accounts *cannot* be transferred and must be recreated?
- Customer notification and migration plan?
- Payment processor transfer path (often the hardest single step — new owner, new account, customer
  re-authorization; this can cause real churn and buyers know it)?
- Transition support: how long, how many hours, at what compensation?

## Evidence gap analysis

For each area, produce:

```
Question area:        [e.g. Retention]
Buyer will ask:       [the specific question]
Current evidence:     [what exists] [KNOWN / INFERRED / UNKNOWN]
Gap:                  [what's missing]
Severity:             [DEAL-BLOCKING / PRICE-AFFECTING / MINOR]
Cost to close:        [hours/€]
Recommended action:   [specific]
```

**DEAL-BLOCKING** gaps get their own callout in the executive summary. Typical ones: unclear IP
ownership, non-transferable platform accounts, unverifiable revenue, copyleft licence contamination,
PII handled without a legal basis. These don't reduce the price — they end the process, often after
the founder has spent two months on it.

**PRICE-AFFECTING** gaps are the retrade ammunition: no cohort data, no deployment docs, no test
coverage, thin financial records. Each one is a lever the buyer pulls in week three. Closing them
before listing is why the value creation roadmap usually beats feature work.

Rank the gaps by `(severity × likelihood of being asked) ÷ cost to close`. That ordering is directly
usable as the founder's task list, which is the whole point.
