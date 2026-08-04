# Flutter State Management Decision Engine

> An AI-powered architectural decision engine that helps Flutter developers choose the most appropriate state management solution based on project requirements—not personal preferences.

## Overview

Choosing the right state management solution in Flutter is often subjective. Many recommendations are based on familiarity, trends, or community opinions rather than architectural analysis.

**Flutter State Management Decision Engine** approaches the problem differently.

Instead of asking "Which package do you like?", it behaves like a senior Flutter Software Architect conducting an architecture review.

The Skill analyzes the application's vision, infers architectural requirements, asks only the questions that are truly necessary, evaluates every supported solution using evidence-based decision rules, and produces a transparent recommendation with complete reasoning.

---

## Supported Solutions

* Cubit
* Bloc
* Riverpod
* Provider
* ChangeNotifier
* ValueNotifier
* GetX

---

## Decision Philosophy

The Skill does **not** recommend technologies based on popularity.

Every recommendation is derived from architectural principles synthesized from official documentation.

Its goal is not to teach Flutter.

Its goal is to consistently select the most appropriate solution for the project being analyzed.

---

## Workflow

The decision engine follows a structured multi-stage process:

1. **Understand**

   * Collect the user's vision for the application or feature.

2. **Infer**

   * Extract architectural facts and infer missing information whenever possible.

3. **Discover**

   * Ask only the questions required to reach a confident decision.

4. **Evaluate**

   * Compare every supported state management solution against the project's requirements.

5. **Decision Trace**

   * Explain exactly how each architectural requirement influenced the recommendation.

6. **Recommend**

   * Produce a final recommendation with confidence score, trade-offs, rejected alternatives, scalability analysis, and implementation guidance.

---

## Key Features

* Evidence-based architectural reasoning
* Dynamic questioning (no fixed questionnaire)
* Architectural inference before asking questions
* Transparent decision trace
* Confidence scoring
* Comparative evaluation of all supported solutions
* Anti-pattern detection
* Scalable decision framework
* Reference-driven recommendations

---

## Knowledge Sources

The decision rules are synthesized from the official documentation of:

* Bloc Library (Cubit & Bloc)
* Riverpod Documentation
* Flutter Documentation (Provider, ChangeNotifier, ValueNotifier)
* GetX Documentation

The Skill transforms these references into reusable architectural decision rules instead of quoting them directly.

---

## Example Output

```text
Recommended Solution:
Riverpod

Confidence:
94%

Decision Trace

✓ Shared application state

✓ Multiple asynchronous workflows

✓ Expected long-term scalability

✓ Strong testing requirements

Rejected Alternatives

Cubit
→ Business logic expected to become significantly more complex.

Bloc
→ Event-driven architecture is unnecessary for the current requirements.

Provider
→ Less suitable for the project's expected growth.

GetX
→ Architectural goals prioritize explicit dependency management.
```

---

## Who Is This For?

* Flutter Developers
* Software Architects
* Technical Leads
* Engineering Teams
* AI-assisted development workflows
* Anyone designing a new Flutter application

---

## Project Goal

This project demonstrates how AI can support software architecture decisions by combining structured reasoning with evidence extracted from authoritative technical documentation.

It is designed to be transparent, explainable, and extensible rather than opinionated.

---

## License

MIT License



That's the sentence I would use at the top of the GitHub repository. It clearly tells visitors what the project is and what makes it different.
