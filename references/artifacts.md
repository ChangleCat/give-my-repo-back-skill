# Ownership artifacts

All templates below are structural examples. Translate headings, prose, table labels, questions, hints, and human-readable metadata values into the user's output language before generating documents. Keep identifiers, paths, schema keys, and status tokens unchanged. English templates do not prescribe English output.

Use these artifacts when persistent documentation will help across sessions. Follow an established repository documentation convention when one exists. Otherwise use:

```text
docs/repo-ownership/
├── ownership-brief.md
├── requirements.md
├── roadmap.md
├── ledger.md
├── maps/
│   └── GMRB-002-create-task.md
└── cards/
    ├── GMRB-001.md
    └── GMRB-002.md
```

Do not create empty files for ceremony. A small session may keep the brief, roadmap, ledger, and active card in one document or in the conversation.

## Ownership brief

Keep it accurate enough to navigate and small enough to maintain.

```markdown
# Ownership brief: <target>

## Target and motivation
<What the person wants to own and why>

## Repository snapshot
- Revision:
- Working tree state:
- Evidence checked at:

## Verified working model
- Entry points:
- Representative control flow:
- Representative data or event flow:
- Important data and state:
- External boundaries:
- Validation path:
- Human-made system map, when used:

## Design decisions visible in the repository
| Decision | Evidence | Likely rationale | Confidence |
| --- | --- | --- | --- |

## Vocabulary
| Term | Meaning in this repository |
| --- | --- |

## Unknowns and risks
- <Clearly distinguish unknowns from defects>

## Why this learning route
<How the selected work traverses the target concepts>
```

Use direct file and symbol references for important evidence. Do not write speculative history as fact.

When a task card uses a system map, read [system-map.md](system-map.md). Save a persistent map under `docs/repo-ownership/maps/` only when it helps the current route; do not create the directory or empty map files for ceremony. Prefer a filename that connects the map to its originating card and behavior, such as `GMRB-002-create-task.md`. Preserve the person's prediction and revision history rather than replacing it with a polished agent-authored artifact.

## Requirements

Create this before splitting a real need into cards. Include enough detail for the person to reason about the work without hiding implementation answers in the specification.

```markdown
# Requirement: <name>

## Need and evidence
<User request or observed behavior, with repository references>

## Current and desired behavior
<Concrete before/after scenarios>

## Acceptance scenarios
- Given <state>, when <action>, then <observable outcome>.
- <Relevant edge or failure case>

## Scope and non-goals
<Bounded change and what is deferred>

## Constraints and dependencies
<Interfaces, compatibility, data, and existing behavior to preserve>

## Decisions for the person
<Alternatives to investigate; do not pre-answer the learning objective>

## Open questions
<What evidence or decision resolves each unknown>
```

For understanding-only work, use capability demonstrations and explanation scenarios as acceptance criteria. Link roadmap cards back to these criteria.

## Roadmap

The roadmap is a dependency-aware outline, not a queue of generic tickets.

```markdown
# Ownership roadmap

## Demonstration target
<What the person should be able to do and explain>

## Route
| Card | Capability built | Depends on | Observable proof | Status |
| --- | --- | --- | --- | --- |
| GMRB-001 | ... | — | ... | active |

## Adaptation notes
- <Why cards were added, split, reordered, or retired>
```

Allowed status values are `backlog`, `active`, `blocked`, `review`, and `complete`. Keep at most one active card unless the user explicitly wants parallel work. If awaiting evidence review or blocked, record that next action rather than activating unrelated work. Translate status explanations for the person, but preserve these tokens.

## Atomic task card

Write to the person in direct language. Reveal enough context to start, but do not include the final implementation.

```markdown
---
id: GMRB-001
title: <Outcome-oriented title>
status: active
depends_on: []
learning_objective: <One primary concept>
---

# GMRB-001 — <title>

## Why this card exists
<Connection to repository ownership and the larger request>

## Outcome
<One observable result>

## Boundaries
- In scope:
- Out of scope:
- Preserve:

## Inspect first
- `<file or symbol>` — <what question it can answer>

## Suggested session
- Estimated effort: <A rough, user-language range or number of focused sessions, adjusted for the stated prerequisites>
- First five minutes: <One concrete action that creates momentum without revealing the solution>

<State that the estimate is for planning, not a deadline or a completion criterion.>

## Before you edit
In your own words:
1. <prediction about current behavior or flow>
2. <decision or risk to identify>

## Your task
<Steps expressed as goals and checkpoints, not a paste-ready solution>

## Constraints
- <Relevant repository or design invariant>

## Validation
Record every check as `pass`, `fail`, or `not_run`.

| Check | What it proves | Result | Limits |
| --- | --- | --- | --- |
| Automated | | `not_run` | |
| Manual or observational | | `not_run` | |
| Regression signal | | `not_run` | |

A `not_run` result does not prove code correctness. Recording why a check could not run keeps the limitation visible but does not turn the result into `pass`.

## Evidence to bring back
- Repository revision or other stable artifact identity:
- Relevant working-tree state:
- Applicable behavior, path, or subsystem:
- <Diff, command output, trace, human-made map with its evidence index, or explanation>

## Understanding gate
Be ready to explain:
1. <how the relevant path works>
2. <why this approach was chosen>
3. <a failure mode or alternative>

## Hints
<By default, say hints are available on request and generate each rung when asked. If the person requests hints inside a document, label them clearly; use collapsible sections only when the viewer supports them. Never rely on a particular UI to hide answers.>

## Stop conditions
- <When to pause rather than improvise, such as encountering secrets, production state, or a wider-than-expected migration>
```

### Atomicity check

Before activating a card, confirm:

- Its title describes one result rather than joining several with “and.”
- One mental model is central; incidental syntax does not count as another objective.
- The person can gather proof without completing a later card.
- The likely edit or investigation surface is bounded.
- Its prerequisites appear in `depends_on` or inside `Inspect first`.
- Its estimate fits within one focused session for someone with those prerequisites, or the card explains why it cannot be split without losing independent validation.
- Its first-five-minutes action is concrete and does not contain the implementation answer.
- Completion requires judgment or understanding, not mechanical copying.

## Ownership ledger

Record demonstrated evidence, not impressions.

```markdown
# Ownership ledger

## Demonstrated
| Capability | Evidence | Repository revision | Validity | Assistance level | Applicable scope |
| --- | --- | --- | --- | --- | --- |

## Learning debt
| Concept or change | What AI supplied | Recovery card |
| --- | --- | --- |

## Open questions
- ...

## Next active card
- ...

## Session handoff
- Output language:
- Current card and state:
- Last reviewed evidence, repository revision, relevant working-tree state, and applicable scope:
- Evidence marked `needs_recheck` and the material change that affected it:
- Unverified claims or blockers:
- Next human action:
```

Use assistance descriptions such as `independent`, `directional hint`, `diagnostic coaching`, `pseudocode`, or `AI implementation`. Do not turn them into a grade or an artificial percentage.

Use `current` when an evidence record still matches the repository inputs and `needs_recheck` when a material change affects the behavior, path, contract, configuration, test, or other input it relied on. Preserve the old row and its original result; add later evidence as a new row after rechecking. Do not mark unrelated evidence `needs_recheck` merely because the repository changed elsewhere.
