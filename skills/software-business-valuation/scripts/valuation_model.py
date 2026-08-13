#!/usr/bin/env python3
"""
valuation_model.py — deterministic arithmetic backbone for the software-business-valuation skill.

WHY THIS EXISTS
---------------
The judgment in a valuation is yours: which methods apply, which multiple band, which adjustments,
how to score sellability. This script does none of that. It exists because three mechanical things
go wrong when the four-price model is computed by hand:

  1. The price-ordering invariants break (expected transaction ends up above the asking price, or
     fast-sale above expected).
  2. Adjustment ledgers silently compound to +120% without anyone noticing.
  3. Scores get re-derived inconsistently between the summary and the body of the report.

Feed it your inputs, use its output as the arithmetic backbone, and keep owning the judgment. If the
output contradicts your intuition, revisit an input — do not quietly override the arithmetic.

USAGE
-----
    python valuation_model.py profile.json          # human-readable report
    python valuation_model.py profile.json --json   # machine-readable
    python valuation_model.py profile.json --md     # markdown tables for pasting into the report
    python valuation_model.py --selftest            # verify the engine

INPUT SCHEMA (JSON)
-------------------
{
  "product": "Acme Forms",
  "currency": "EUR",                      // symbol/code used in output; default "EUR"
  "classification": "B2B SaaS, small",

  "methods": [                            // 1..n valuation methods to triangulate
    {
      "name": "ARR multiple",
      "metric_label": "ARR",
      "metric_value": 50400,              // the normalized metric (recurring revenue only, etc.)
      "base_multiple": 3.0,               // from references/03, before adjustments
      "evidence_level": "L5",             // L1..L6 — what the base multiple rests on
      "weight": 0.6,                      // relative weight; normalized automatically
      "adjustments": [                    // from the adjustment engine; pct as decimals
        {"factor": "Growth +40% YoY", "pct": 0.20, "evidence": "KNOWN"},
        {"factor": "No test suite",   "pct": -0.08, "evidence": "INFERRED"}
      ]
    }
  ],

  // Fixed-value methods (replacement cost, asset value) that aren't metric x multiple:
  // give "value" instead of metric/base_multiple. "role": "primary" | "floor" | "ceiling".
  // floor/ceiling methods bound the FMV range instead of contributing to the weighted center.

  "sellability": {                        // 0-10 each; all ten required
    "market_demand": 7, "buyer_pool": 7, "revenue_quality": 8, "traction": 6,
    "technical_transferability": 7, "documentation": 5, "founder_independence": 8,
    "competitive_position": 6, "growth_potential": 7, "exit_readiness": 6
  },

  "exit_readiness": {                     // 1.0 ready / 0.5 partial / 0 absent / null = N/A
    "financial_records": 1.0, "analytics": 0.5, "technical_documentation": 0.5,
    "infrastructure_transferability": 1.0, "source_code_organization": 1.0,
    "ip_ownership": 1.0, "domain_ownership": 1.0, "app_store_ownership": null,
    "google_play_ownership": null, "database_transfer": 0.5, "deployment_documentation": 0.5,
    "customer_documentation": 0.5, "contracts": 0.0, "privacy_legal": 0.5,
    "security_documentation": 0.0, "operational_independence": 0.5
  },

  "confidence": {                         // component scores, capped at their maxima
    "financial_evidence": 20,             // max 30
    "retention_metrics": 12,              // max 20
    "comparables": 3,                     // max 25
    "technical_verification": 9,          // max 15
    "model_clarity": 10                   // max 10
  },
  "confidence_caps": ["no_verified_comparables"],
      // any of: no_revenue_data (40), retention_unknown (55), no_verified_comparables (55),
      //         code_not_inspected (60), model_or_ownership_unclear (45)

  "range_width_override": 0.30            // optional; else derived from confidence
}

All numeric outputs are rounded to defensible precision — the script will not emit EUR 47,350.
"""

from __future__ import annotations

import argparse
import json
import sys

# --------------------------------------------------------------------------------------
# Constants — these mirror references/04-scoring.md and references/05-buyers-and-pricing.md.
# Change them there and here together, or the report and the arithmetic will disagree.
# --------------------------------------------------------------------------------------

SELLABILITY_DIMENSIONS = [
    "market_demand", "buyer_pool", "revenue_quality", "traction",
    "technical_transferability", "documentation", "founder_independence",
    "competitive_position", "growth_potential", "exit_readiness",
]

EXIT_READINESS_ITEMS = [
    "financial_records", "analytics", "technical_documentation",
    "infrastructure_transferability", "source_code_organization", "ip_ownership",
    "domain_ownership", "app_store_ownership", "google_play_ownership",
    "database_transfer", "deployment_documentation", "customer_documentation",
    "contracts", "privacy_legal", "security_documentation", "operational_independence",
]

CONFIDENCE_MAXIMA = {
    "financial_evidence": 30,
    "retention_metrics": 20,
    "comparables": 25,
    "technical_verification": 15,
    "model_clarity": 10,
}

CONFIDENCE_CAPS = {
    "no_revenue_data": 40,
    "retention_unknown": 55,
    "no_verified_comparables": 55,
    "code_not_inspected": 60,
    "model_or_ownership_unclear": 45,
}

SELLABILITY_BANDS = [
    (80, 100, "Highly Sellable"),
    (65, 79, "Sellable"),
    (50, 64, "Sellable With Preparation"),
    (35, 49, "Difficult to Sell"),
    (0, 34, "Very Difficult to Sell"),
]

# All three derived prices are expressed as multiples of the FMV *centre*, not of each other.
# Chaining them (expected as a % of asking, asking as a % of FMV high) compounds the uncertainty
# width into the outcome, which produced expected transaction prices above the FMV centre on
# low-confidence valuations — the opposite of reality. Anchoring everything to the centre keeps a
# wide range meaning "we're unsure", not "it's worth more".
PRICING_BY_SELLABILITY = [
    (80, {"ask_factor": 1.20, "expected_pct": (1.00, 1.12), "fast_pct": (0.65, 0.80)}),
    (65, {"ask_factor": 1.25, "expected_pct": (0.88, 1.02), "fast_pct": (0.55, 0.70)}),
    (50, {"ask_factor": 1.30, "expected_pct": (0.75, 0.92), "fast_pct": (0.45, 0.60)}),
    (35, {"ask_factor": 1.30, "expected_pct": (0.60, 0.80), "fast_pct": (0.30, 0.50)}),
    (0,  {"ask_factor": 1.25, "expected_pct": (0.42, 0.65), "fast_pct": (0.20, 0.40)}),
]

# The ask must clear FMV high (you never market below your own valuation ceiling) but must not run
# away on very wide ranges.
ASK_MIN_CUSHION_OVER_FMV_HIGH = 1.05
ASK_MAX_MULTIPLE_OF_CENTRE = 1.75

# Confidence -> half-width of the FMV range. Thin evidence must produce wide ranges; that is the
# honest output, not a defect.
CONFIDENCE_RANGE_WIDTH = [(75, 0.175), (55, 0.30), (35, 0.475), (0, 0.55)]

# Beyond this, the adjustment ledger is doing work the base multiple should have done.
ADJUSTMENT_SOFT_CAP = 0.50


# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------

def round_money(value: float) -> int:
    """Round to a precision that doesn't imply knowledge we don't have."""
    v = abs(value)
    if v < 2_000:
        step = 100
    elif v < 10_000:
        step = 500
    elif v < 100_000:
        step = 1_000
    elif v < 1_000_000:
        step = 5_000
    else:
        step = 25_000
    return int(round(value / step) * step)


def fmt(value: float, currency: str) -> str:
    return f"{currency}{round_money(value):,}"


def band_for(score: float, table):
    for threshold, payload in table:
        if score >= threshold:
            return payload
    return table[-1][1]


# --------------------------------------------------------------------------------------
# Scoring
# --------------------------------------------------------------------------------------

def score_sellability(raw: dict, warnings: list) -> dict:
    scores, missing = {}, []
    for dim in SELLABILITY_DIMENSIONS:
        if dim not in raw or raw[dim] is None:
            missing.append(dim)
            scores[dim] = 0
        else:
            val = float(raw[dim])
            if not 0 <= val <= 10:
                warnings.append(f"Sellability '{dim}' = {val} is outside 0-10; clamped.")
                val = max(0.0, min(10.0, val))
            scores[dim] = val
    if missing:
        warnings.append(
            "Sellability dimensions missing and scored 0: " + ", ".join(missing)
            + ". A buyer treats unassessed as absent — supply a score or justify the zero."
        )
    total = sum(scores.values())
    classification = next(c for lo, hi, c in SELLABILITY_BANDS if lo <= total <= hi)
    return {"dimensions": scores, "total": round(total, 1), "classification": classification}


def score_exit_readiness(raw: dict, warnings: list) -> dict:
    applicable, items = {}, {}
    for item in EXIT_READINESS_ITEMS:
        val = raw.get(item, 0.0)
        items[item] = val
        if val is None:
            continue  # N/A — rescale over the rest
        v = float(val)
        if v not in (0.0, 0.5, 1.0):
            warnings.append(f"Exit readiness '{item}' = {v}; expected 0, 0.5, 1.0 or null.")
            v = max(0.0, min(1.0, v))
        applicable[item] = v
    if not applicable:
        warnings.append("No applicable exit-readiness items; score set to 0.")
        return {"items": items, "score": 0.0, "applicable_count": 0}
    score = sum(applicable.values()) / len(applicable) * 100
    return {"items": items, "score": round(score, 1), "applicable_count": len(applicable)}


def score_confidence(raw: dict, caps: list, warnings: list) -> dict:
    components, total = {}, 0.0
    for key, maximum in CONFIDENCE_MAXIMA.items():
        val = float(raw.get(key, 0) or 0)
        if val > maximum:
            warnings.append(f"Confidence '{key}' = {val} exceeds max {maximum}; clamped.")
            val = maximum
        components[key] = val
        total += val
    raw_total = total
    applied = []
    for cap_name in caps or []:
        if cap_name not in CONFIDENCE_CAPS:
            warnings.append(f"Unknown confidence cap '{cap_name}' ignored.")
            continue
        ceiling = CONFIDENCE_CAPS[cap_name]
        if total > ceiling:
            applied.append({"cap": cap_name, "ceiling": ceiling})
            total = ceiling
    return {
        "components": components,
        "raw_total": round(raw_total, 1),
        "caps_applied": applied,
        "total": round(total, 1),
    }


# --------------------------------------------------------------------------------------
# Valuation
# --------------------------------------------------------------------------------------

def compute_methods(methods: list, warnings: list) -> list:
    results = []
    for m in methods:
        name = m.get("name", "unnamed method")
        role = m.get("role", "primary")
        adjustments = m.get("adjustments", []) or []
        net = sum(float(a.get("pct", 0)) for a in adjustments)
        capped = net
        if abs(net) > ADJUSTMENT_SOFT_CAP:
            capped = ADJUSTMENT_SOFT_CAP if net > 0 else -ADJUSTMENT_SOFT_CAP
            warnings.append(
                f"Method '{name}': net adjustment {net:+.0%} exceeds the +/-{ADJUSTMENT_SOFT_CAP:.0%} "
                f"soft cap and was applied at {capped:+.0%}. An adjustment ledger this large usually "
                f"means the base multiple or the business classification is wrong — re-check those "
                f"before accepting this result."
            )

        if "value" in m and m["value"] is not None:
            value = float(m["value"]) * (1 + capped)
            adjusted_multiple = None
        else:
            metric = float(m.get("metric_value", 0) or 0)
            base = float(m.get("base_multiple", 0) or 0)
            if metric <= 0 or base <= 0:
                warnings.append(f"Method '{name}' has no usable metric x multiple and no fixed value; skipped.")
                continue
            adjusted_multiple = base * (1 + capped)
            value = metric * adjusted_multiple

        results.append({
            "name": name,
            "role": role,
            "metric_label": m.get("metric_label"),
            "metric_value": m.get("metric_value"),
            "base_multiple": m.get("base_multiple"),
            "evidence_level": m.get("evidence_level", "L6"),
            "net_adjustment": round(net, 4),
            "applied_adjustment": round(capped, 4),
            "adjusted_multiple": round(adjusted_multiple, 3) if adjusted_multiple else None,
            "value": value,
            "weight": float(m.get("weight", 1.0)),
            "adjustments": adjustments,
        })
    if not results:
        raise ValueError("No usable valuation methods. Provide at least one method.")
    return results


def triangulate(method_results: list, confidence_total: float,
                width_override, warnings: list) -> dict:
    primary = [m for m in method_results if m["role"] == "primary"]
    if not primary:
        warnings.append("No method marked 'primary'; using all methods for the weighted centre.")
        primary = method_results

    total_weight = sum(m["weight"] for m in primary)
    if total_weight <= 0:
        raise ValueError("Primary method weights sum to zero.")
    center = sum(m["value"] * m["weight"] for m in primary) / total_weight

    values = [m["value"] for m in primary]
    if len(values) > 1 and min(values) > 0:
        dispersion = (max(values) - min(values)) / min(values)
        if dispersion > 0.8:
            warnings.append(
                f"Primary methods disagree by {dispersion:.0%} "
                f"({fmt(min(values), '')} vs {fmt(max(values), '')}). Do not present the weighted "
                f"average as the answer — explain the divergence and say which method a buyer will "
                f"actually use (usually the demand-based one)."
            )

    width = float(width_override) if width_override is not None else band_for(
        confidence_total, CONFIDENCE_RANGE_WIDTH)
    low, high = center * (1 - width), center * (1 + width)

    # Floors and ceilings bound the range rather than shifting the centre.
    for m in method_results:
        if m["role"] == "floor" and m["value"] > low:
            warnings.append(
                f"Floor method '{m['name']}' ({fmt(m['value'], '')}) sits above the computed FMV low; "
                f"raised the floor. Check this is genuinely a floor — replacement cost is a ceiling "
                f"for pre-revenue assets, not a floor."
            )
            low = m["value"]
        if m["role"] == "ceiling" and m["value"] < high:
            warnings.append(
                f"Ceiling method '{m['name']}' ({fmt(m['value'], '')}) sits below the computed FMV "
                f"high; lowered the ceiling."
            )
            high = m["value"]

    if low > high:
        warnings.append("Floor exceeded ceiling; collapsed to a point estimate — inputs conflict.")
        low = high = (low + high) / 2

    return {
        "center": center,
        "low": low,
        "high": high,
        "half_width": width,
        "weights_normalized": {m["name"]: round(m["weight"] / total_weight, 3) for m in primary},
    }


def four_prices(fmv: dict, sellability_total: float, warnings: list) -> dict:
    params = band_for(sellability_total, PRICING_BY_SELLABILITY)
    fmv_low, fmv_high = fmv["low"], fmv["high"]
    fmv_mid = (fmv_low + fmv_high) / 2

    asking = max(fmv_mid * params["ask_factor"], fmv_high * ASK_MIN_CUSHION_OVER_FMV_HIGH)
    ask_cap = fmv_mid * ASK_MAX_MULTIPLE_OF_CENTRE
    if asking > ask_cap:
        asking = ask_cap
        warnings.append(
            "Asking price was capped relative to the FMV centre. This fires when the FMV range is "
            "very wide — the honest read is that the evidence is too thin to justify anchoring the "
            "ask at the top of the band. Narrow the range before listing."
        )
    exp_low = fmv_mid * params["expected_pct"][0]
    exp_high = fmv_mid * params["expected_pct"][1]
    fast_low = fmv_mid * params["fast_pct"][0]
    fast_high = fmv_mid * params["fast_pct"][1]

    # Invariants. Nobody pays more than the ask in a small private deal, and a fast sale is by
    # definition not better than a patient one.
    if exp_high > asking:
        exp_high = asking
        warnings.append("Expected transaction high exceeded the asking price; clamped to the ask.")
    if fast_high > exp_high:
        fast_high = exp_high
        warnings.append("Fast-sale high exceeded expected transaction high; clamped.")
    if fast_low > fast_high:
        fast_low = fast_high
    if exp_low > exp_high:
        exp_low = exp_high

    if exp_high / asking < 0.70:
        warnings.append(
            f"Expected transaction tops out at {exp_high / asking:.0%} of the asking price. A gap "
            f"that large means the ask is an exploratory anchor, not a realistic target — either "
            f"narrow the FMV range with better evidence, or tell the seller plainly that the listed "
            f"price is a starting position they should not expect to achieve."
        )

    overlap = fast_high > exp_low
    if overlap:
        warnings.append(
            "Fast-sale and expected-transaction ranges overlap. This is legitimate at high "
            "sellability (speed costs little) — present them as overlapping bands and say why."
        )

    return {
        "fair_market_value": {"low": fmv_low, "high": fmv_high, "mid": fmv_mid},
        "asking_price": asking,
        "expected_transaction": {"low": exp_low, "high": exp_high},
        "fast_sale": {"low": fast_low, "high": fast_high},
        "parameters": params,
        "ranges_overlap": overlap,
        # Reported because founders think in "what % of my ask will I get" — but it is a derived
        # figure, not an input to the model.
        "implied_expected_pct_of_ask": (round(exp_low / asking, 3), round(exp_high / asking, 3)),
    }


def verify_invariants(prices: dict) -> list:
    """Returns a list of violated invariants. Should always be empty after four_prices()."""
    v = []
    fmv, ask = prices["fair_market_value"], prices["asking_price"]
    exp, fast = prices["expected_transaction"], prices["fast_sale"]
    if fmv["low"] > fmv["high"]:
        v.append("fmv_low > fmv_high")
    if fmv["high"] > ask + 1e-6:
        v.append("fmv_high > asking_price")
    if exp["high"] > ask + 1e-6:
        v.append("expected_high > asking_price")
    if exp["low"] > exp["high"]:
        v.append("expected_low > expected_high")
    if fast["low"] > fast["high"]:
        v.append("fast_low > fast_high")
    if fast["high"] > exp["high"] + 1e-6:
        v.append("fast_high > expected_high")
    return v


# --------------------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------------------

def run(profile: dict) -> dict:
    warnings: list = []
    currency = profile.get("currency", "EUR")

    sellability = score_sellability(profile.get("sellability", {}) or {}, warnings)
    readiness = score_exit_readiness(profile.get("exit_readiness", {}) or {}, warnings)
    confidence = score_confidence(profile.get("confidence", {}) or {},
                                  profile.get("confidence_caps", []) or [], warnings)

    # Cross-check: the sellability rubric maps its tenth dimension from exit readiness.
    if readiness["applicable_count"]:
        implied = round(readiness["score"] / 10)
        actual = sellability["dimensions"].get("exit_readiness", 0)
        if abs(implied - actual) > 1:
            warnings.append(
                f"Sellability 'exit_readiness' = {actual} but the exit-readiness score "
                f"({readiness['score']}/100) implies {implied}. Reconcile these — the report should "
                f"not contain two different readings of the same thing."
            )

    methods = compute_methods(profile.get("methods", []) or [], warnings)
    fmv = triangulate(methods, confidence["total"], profile.get("range_width_override"), warnings)
    prices = four_prices(fmv, sellability["total"], warnings)

    violations = verify_invariants(prices)
    if violations:
        warnings.append("INVARIANT VIOLATION (engine bug or contradictory input): " + ", ".join(violations))

    return {
        "product": profile.get("product", "Unnamed product"),
        "classification": profile.get("classification", "[UNKNOWN]"),
        "currency": currency,
        "methods": methods,
        "fmv": fmv,
        "prices": prices,
        "sellability": sellability,
        "exit_readiness": readiness,
        "confidence": confidence,
        "invariant_violations": violations,
        "warnings": warnings,
    }


# --------------------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------------------

def render_text(r: dict) -> str:
    c = r["currency"]
    p, fmv = r["prices"], r["fmv"]
    out = []
    a = out.append

    a("=" * 78)
    a(f"VALUATION MODEL — {r['product']}")
    a(f"Classification: {r['classification']}")
    a("=" * 78)

    a("\nMETHODS")
    for m in r["methods"]:
        line = f"  {m['name']} [{m['role']}, evidence {m['evidence_level']}]"
        a(line)
        if m["adjusted_multiple"]:
            a(f"    {m['metric_label']} {fmt(m['metric_value'], c)} x {m['adjusted_multiple']}"
              f"  (base {m['base_multiple']} adj {m['applied_adjustment']:+.0%})")
        a(f"    -> {fmt(m['value'], c)}   weight {m['weight']}")
        for adj in m["adjustments"]:
            a(f"       {float(adj.get('pct', 0)):+.0%}  {adj.get('factor', '')} "
              f"[{adj.get('evidence', 'UNLABELLED')}]")

    a(f"\nWeighted centre: {fmt(fmv['center'], c)}   (+/-{fmv['half_width']:.0%} from confidence)")

    a("\n" + "-" * 78)
    a("FOUR-PRICE MODEL")
    a("-" * 78)
    a(f"  FAIR MARKET VALUE           {fmt(fmv['low'], c)} - {fmt(fmv['high'], c)}")
    a(f"  RECOMMENDED ASKING PRICE    {fmt(p['asking_price'], c)}"
      f"   ({p['asking_price'] / fmv['center']:.2f}x FMV centre)")
    imp = p["implied_expected_pct_of_ask"]
    a(f"  EXPECTED TRANSACTION PRICE  {fmt(p['expected_transaction']['low'], c)} - "
      f"{fmt(p['expected_transaction']['high'], c)}"
      f"   ({p['parameters']['expected_pct'][0]:.0%}-{p['parameters']['expected_pct'][1]:.0%} of FMV "
      f"centre = {imp[0]:.0%}-{imp[1]:.0%} of ask)")
    a(f"  FAST-SALE PRICE             {fmt(p['fast_sale']['low'], c)} - "
      f"{fmt(p['fast_sale']['high'], c)}"
      f"   ({p['parameters']['fast_pct'][0]:.0%}-{p['parameters']['fast_pct'][1]:.0%} of FMV centre)")

    s = r["sellability"]
    a(f"\nSELLABILITY  {s['total']:.0f}/100  —  {s['classification']}")
    for dim, val in s["dimensions"].items():
        a(f"    {dim.replace('_', ' '):<28} {val:>4}/10")

    e = r["exit_readiness"]
    a(f"\nEXIT READINESS  {e['score']:.0f}/100  ({e['applicable_count']} applicable items)")

    cf = r["confidence"]
    a(f"\nVALUATION CONFIDENCE  {cf['total']:.0f}/100  (raw {cf['raw_total']:.0f})")
    for k, v in cf["components"].items():
        a(f"    {k.replace('_', ' '):<28} {v:>4}/{CONFIDENCE_MAXIMA[k]}")
    for cap in cf["caps_applied"]:
        a(f"    CAP APPLIED: {cap['cap']} -> ceiling {cap['ceiling']}")

    if r["warnings"]:
        a("\n" + "-" * 78)
        a("WARNINGS — resolve these before publishing the report")
        a("-" * 78)
        for w in r["warnings"]:
            a(f"  * {w}")

    a("")
    return "\n".join(out)


def render_markdown(r: dict) -> str:
    c = r["currency"]
    p, fmv = r["prices"], r["fmv"]
    out = []
    a = out.append

    a("| | |")
    a("|---|---|")
    a(f"| Fair market value | {fmt(fmv['low'], c)} – {fmt(fmv['high'], c)} |")
    a(f"| Recommended asking price | {fmt(p['asking_price'], c)} |")
    a(f"| Expected transaction price | {fmt(p['expected_transaction']['low'], c)} – "
      f"{fmt(p['expected_transaction']['high'], c)} |")
    a(f"| Fast-sale price | {fmt(p['fast_sale']['low'], c)} – {fmt(p['fast_sale']['high'], c)} |")
    a(f"| Sellability | {r['sellability']['total']:.0f}/100 — {r['sellability']['classification']} |")
    a(f"| Exit readiness | {r['exit_readiness']['score']:.0f}/100 |")
    a(f"| Valuation confidence | {r['confidence']['total']:.0f}/100 |")

    a("\n**Valuation calculation**\n")
    a("| Method | Base | Net adj. | Adjusted | Value | Weight | Evidence |")
    a("|---|---|---|---|---|---|---|")
    for m in r["methods"]:
        base = f"{m['metric_label']} {fmt(m['metric_value'], c)} × {m['base_multiple']}" \
            if m["adjusted_multiple"] else "fixed"
        adjm = f"{m['adjusted_multiple']}×" if m["adjusted_multiple"] else "—"
        a(f"| {m['name']} | {base} | {m['applied_adjustment']:+.0%} | {adjm} | "
          f"{fmt(m['value'], c)} | {m['weight']} | {m['evidence_level']} |")

    a("\n**Sellability**\n")
    a("| Dimension | Score |")
    a("|---|---|")
    for dim, val in r["sellability"]["dimensions"].items():
        a(f"| {dim.replace('_', ' ').title()} | {val}/10 |")
    a(f"| **Total** | **{r['sellability']['total']:.0f}/100** |")

    if r["warnings"]:
        a("\n**Engine warnings**\n")
        for w in r["warnings"]:
            a(f"- {w}")
    return "\n".join(out)


# --------------------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------------------

SELFTEST_PROFILE = {
    "product": "Selftest B2B micro-SaaS",
    "currency": "EUR",
    "classification": "B2B SaaS, small",
    "methods": [
        {"name": "ARR multiple", "metric_label": "ARR", "metric_value": 50400,
         "base_multiple": 3.0, "evidence_level": "L5", "weight": 0.6, "role": "primary",
         "adjustments": [
             {"factor": "Growth +40% YoY", "pct": 0.20, "evidence": "KNOWN"},
             {"factor": "Churn 2.1%/mo", "pct": 0.10, "evidence": "KNOWN"},
             {"factor": "Diversified customers", "pct": 0.10, "evidence": "KNOWN"},
             {"factor": "Organic acquisition", "pct": 0.15, "evidence": "INFERRED"},
             {"factor": "Low founder hours, documented", "pct": 0.10, "evidence": "KNOWN"},
             {"factor": "No test suite", "pct": -0.08, "evidence": "KNOWN"},
         ]},
        {"name": "SDE multiple", "metric_label": "SDE", "metric_value": 38000,
         "base_multiple": 4.0, "evidence_level": "L5", "weight": 0.4, "role": "primary",
         "adjustments": [{"factor": "Low owner hours", "pct": 0.10, "evidence": "KNOWN"}]},
    ],
    "sellability": {
        "market_demand": 7, "buyer_pool": 8, "revenue_quality": 8, "traction": 7,
        "technical_transferability": 7, "documentation": 6, "founder_independence": 8,
        "competitive_position": 6, "growth_potential": 7, "exit_readiness": 6,
    },
    "exit_readiness": {
        "financial_records": 1.0, "analytics": 0.5, "technical_documentation": 1.0,
        "infrastructure_transferability": 1.0, "source_code_organization": 1.0,
        "ip_ownership": 1.0, "domain_ownership": 1.0, "app_store_ownership": None,
        "google_play_ownership": None, "database_transfer": 0.5,
        "deployment_documentation": 1.0, "customer_documentation": 0.5, "contracts": 0.0,
        "privacy_legal": 0.5, "security_documentation": 0.0, "operational_independence": 0.5,
    },
    "confidence": {"financial_evidence": 20, "retention_metrics": 12, "comparables": 3,
                   "technical_verification": 9, "model_clarity": 10},
    "confidence_caps": ["no_verified_comparables"],
}


def selftest() -> int:
    failures = []

    def check(label, cond):
        if not cond:
            failures.append(label)

    r = run(SELFTEST_PROFILE)
    p = r["prices"]

    check("no invariant violations", not r["invariant_violations"])
    check("adjustment soft cap warned", any("soft cap" in w for w in r["warnings"]))
    check("ARR method capped at +50%", abs(r["methods"][0]["applied_adjustment"] - 0.50) < 1e-9)
    check("ARR adjusted multiple 4.5x", abs(r["methods"][0]["adjusted_multiple"] - 4.5) < 1e-9)
    # Raw confidence is 54, below the 55 ceiling — the cap must NOT silently fire.
    check("confidence raw total 54", r["confidence"]["raw_total"] == 54)
    check("cap not applied below its ceiling", r["confidence"]["caps_applied"] == [])
    check("sellability total 70", r["sellability"]["total"] == 70)
    check("sellability band", r["sellability"]["classification"] == "Sellable")
    check("fmv low < high", p["fair_market_value"]["low"] < p["fair_market_value"]["high"])
    check("ask above fmv high", p["asking_price"] > p["fair_market_value"]["high"])
    check("expected <= ask", p["expected_transaction"]["high"] <= p["asking_price"] + 1e-6)
    check("fast <= expected high", p["fast_sale"]["high"] <= p["expected_transaction"]["high"] + 1e-6)
    # The bug this engine exists to prevent: a wide (low-confidence) range must not push the
    # expected transaction price above the FMV centre.
    mid = p["fair_market_value"]["mid"]
    check("expected low at or below FMV centre", p["expected_transaction"]["low"] <= mid + 1e-6)
    check("expected high within reach of FMV centre",
          p["expected_transaction"]["high"] <= mid * 1.15)

    # Exit readiness: 14 applicable items, sum = 9.5 -> 67.9
    check("exit readiness rescaled over applicable items",
          r["exit_readiness"]["applicable_count"] == 14
          and abs(r["exit_readiness"]["score"] - 67.9) < 0.15)

    # Very-low sellability must widen the ask-to-fast spread dramatically.
    weak = json.loads(json.dumps(SELFTEST_PROFILE))
    weak["sellability"] = {d: 2 for d in SELLABILITY_DIMENSIONS}
    rw = run(weak)
    strong_spread = p["fast_sale"]["low"] / p["asking_price"]
    weak_spread = rw["prices"]["fast_sale"]["low"] / rw["prices"]["asking_price"]
    check("weak sellability widens the four-price spread", weak_spread < strong_spread)
    check("weak profile still invariant-clean", not rw["invariant_violations"])

    # Missing revenue path: fixed-value replacement cost only.
    prerev = {
        "product": "Selftest pre-revenue",
        "methods": [{"name": "Replacement cost (discounted)", "value": 60000,
                     "role": "primary", "weight": 1.0, "evidence_level": "L6",
                     "adjustments": [{"factor": "No demand evidence", "pct": -0.45}]}],
        "sellability": {d: 3 for d in SELLABILITY_DIMENSIONS},
        "exit_readiness": {i: 0.0 for i in EXIT_READINESS_ITEMS},
        "confidence": {"financial_evidence": 0, "retention_metrics": 0, "comparables": 3,
                       "technical_verification": 9, "model_clarity": 8},
        "confidence_caps": ["no_revenue_data"],
    }
    rp = run(prerev)
    check("pre-revenue confidence total 20", rp["confidence"]["total"] == 20)
    check("pre-revenue wide range", rp["fmv"]["half_width"] >= 0.475)
    check("pre-revenue invariant-clean", not rp["invariant_violations"])
    check("fixed-value method applies adjustment", abs(rp["methods"][0]["value"] - 33000) < 1e-6)

    # A cap must actually bite when the raw score exceeds its ceiling.
    capped = json.loads(json.dumps(SELFTEST_PROFILE))
    capped["confidence"] = {"financial_evidence": 30, "retention_metrics": 20, "comparables": 8,
                            "technical_verification": 15, "model_clarity": 10}  # raw 83
    rc = run(capped)
    check("cap fires above its ceiling", rc["confidence"]["raw_total"] == 83
          and rc["confidence"]["total"] == 55
          and rc["confidence"]["caps_applied"][0]["cap"] == "no_verified_comparables")

    # Divergent methods must trigger the "don't average" warning.
    diverge = json.loads(json.dumps(SELFTEST_PROFILE))
    diverge["methods"][1]["metric_value"] = 5000
    rd = run(diverge)
    check("divergence warning fires", any("disagree by" in w for w in rd["warnings"]))

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST PASSED — all checks green.")
    print(render_text(r))
    return 0


# --------------------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Valuation arithmetic and four-price engine.")
    ap.add_argument("profile", nargs="?", help="Path to the profile JSON")
    ap.add_argument("--json", action="store_true", help="Emit JSON")
    ap.add_argument("--md", action="store_true", help="Emit markdown tables")
    ap.add_argument("--selftest", action="store_true", help="Run the built-in tests")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.profile:
        ap.print_help()
        return 2

    with open(args.profile, "r", encoding="utf-8") as fh:
        profile = json.load(fh)

    result = run(profile)
    if args.json:
        print(json.dumps(result, indent=2, default=str))
    elif args.md:
        print(render_markdown(result))
    else:
        print(render_text(result))
    return 1 if result["invariant_violations"] else 0


if __name__ == "__main__":
    sys.exit(main())

