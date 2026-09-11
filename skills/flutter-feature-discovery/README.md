# Flutter Feature Discovery

A Claude Skill for adding **in-app feature discovery** to Flutter apps: coach marks, spotlight tours, contextual hints and new-feature pointers that explain non-obvious features *while the user is already inside the app*.

> **Core principle:** Don't explain everything. Explain only what is not immediately obvious.

This Skill is **not** for onboarding. It leaves any existing first-launch onboarding untouched and waits until onboarding is finished before showing anything.

## What it does

When invoked in a Flutter project, Claude:

1. **Analyzes** the project without changing anything: architecture, navigation, onboarding, state management, storage, localization, theme, existing tooltip or tour code (`scripts/scan_project.sh` gives a quick inventory).
2. **Plans**: produces a prioritized table (HIGH / MEDIUM / LOW / NONE) of the features that actually need guidance, and stops for your approval. Obvious UI gets NONE.
3. **Designs** each approved tip: the lightest pattern that works, copy that fits the app, native look from the app's theme, and accessibility built in.
4. **Sets triggers and audiences**: contextual triggers only, one tip at a time, persisted completion. Existing users aren't flooded with tips after an update; only newly introduced features are announced to them.
5. **Implements** by reusing the app's existing code, packages, storage, DI and localization. With nothing to reuse, it adapts lightweight custom templates (no new dependency). A new package is added only after a compatibility check and your approval.
6. **Tests and verifies** with meaningful unit and widget tests, `flutter analyze` and `flutter test`, plus a manual device checklist.

It also covers edge cases: scrollable targets, bottom sheets, dialogs, async loading, navigation mid-tour, rebuilds, rotation, keyboard, back button, and app lifecycle.

## When to use

- "Analyze this app and identify which features need in-app guidance."
- "Add feature discovery for this screen."
- "Users don't realize they can long-press to reorder — add a hint."
- "Tell existing users about the new feature in this release."
- Working with `showcaseview`, `tutorial_coach_mark` or `feature_discovery`.

## Structure

```
flutter-feature-discovery/
├── SKILL.md                         # Workflow, rules, decision gates
├── references/
│   ├── project-analysis.md          # Inspection checklist, obviousness rubric
│   ├── ux-design.md                 # Patterns, copy, visual matching, accessibility
│   ├── triggers-and-audiences.md    # Triggers, scheduling, new vs existing users
│   ├── implementation.md            # Approach selection, architecture, l10n, DI
│   ├── edge-cases.md                # Graceful handling of tricky situations
│   ├── testing.md                   # Test matrix + manual QA checklist
│   └── examples.md                  # Worked plans
├── scripts/scan_project.sh          # Read-only project inventory
└── assets/templates/                # Dart templates + tests to adapt
```

## Install

- **Claude app / Cowork:** upload `flutter-feature-discovery.skill`.
- **Claude Code:** copy this folder to `~/.claude/skills/flutter-feature-discovery/` (personal) or `.claude/skills/` in
