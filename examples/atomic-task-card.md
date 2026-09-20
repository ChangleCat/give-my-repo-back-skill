# Example: preserve an HTTP not-found response

[简体中文](atomic-task-card.zh-CN.md)

This is a fictional teaching example, not a diagnosis of this repository. Assume a small task API with `src/routes/tasks.ts`, `src/services/tasks.ts`, and `tests/tasks.test.ts`. Earlier cards established the route-to-service flow and test setup. The agreed requirement is: requesting a missing task returns HTTP 404 without changing the successful response contract.

---

**ID:** `GMRB-003`  
**Status:** `active`  
**Depends on:** `GMRB-001`, `GMRB-002`  
**Learning objective:** Understand how a missing service result becomes an HTTP response.

## Why this card exists

A boundary can turn an expected missing record into an unexpected server error. Working through one failure path will teach you where this API converts domain outcomes into HTTP behavior.

## Outcome

Make `GET /tasks/:id` return the agreed 404 response for an absent task, backed by a regression test.

## Boundaries

- Work within the existing task lookup path and its tests.
- Preserve the status and response body for an existing task.
- Defer database schema changes, new dependencies, and shared error-system redesign.

## Inspect first

- `src/routes/tasks.ts`: Where does the route choose the response status?
- `src/services/tasks.ts`: How does the service represent “not found”?
- `tests/tasks.test.ts`: How do existing tests create data and call the endpoint?

## Suggested session

- Estimated effort: about 30–60 minutes after completing the prerequisite cards.
- First five minutes: open the route and its nearest existing test, then write your predicted route-to-service flow before running anything.

This estimate helps you plan; it is not a deadline or a completion criterion.

## Before you edit

Predict the current status for a missing task. Trace the value that leaves the service and explain what the route will do with it. Identify which layer you think should translate that outcome into HTTP behavior, and why.

## Your task

1. Reproduce the missing-task behavior using the existing test setup.
2. Add one regression case expressing the agreed response. Observe its failure before changing the implementation.
3. Make a bounded change at the layer you chose, using repository conventions.
4. Run the focused tests and check the existing-task case.

## Constraints

Use the repository's existing response-body convention. Do not turn every exception into 404: unexpected failures must remain distinguishable from missing records.

## Validation

Record every check as `pass`, `fail`, or `not_run`. A `not_run` result does not prove that the code is correct.

| Check | What it proves | Result | Limits |
| --- | --- | --- | --- |
| The new test fails on the old implementation for the expected reason and passes on your change. | The regression is reproduced and fixed. | `not_run` | Complete after running. |
| The existing-task test still passes without weakening its assertions. | Existing success behavior is preserved. | `not_run` | Complete after running. |
| Inspect whether the change could misclassify an unexpected service failure. | Unexpected failures remain distinguishable from missing records. | `not_run` | Record the inspected path and conclusion. |

Use the test command documented by the actual project; no executable command is assumed by this fictional example.

## Evidence to bring back

- Repository revision or other stable artifact identity.
- A non-secret summary of relevant working-tree changes.
- Applicable scope: the `GET /tasks/:id` missing-task and existing-task paths.
- The diff, before/after test output, and a short route-to-service trace.
- Why your edit belongs at the selected boundary.

If a later change materially affects this route, its response contract, or the tests used here, preserve this evidence and mark it `needs_recheck`. Do not invalidate it for unrelated repository changes.

## Understanding gate

- How does “not found” travel from the service to the response?
- Why would mapping all errors to 404 hide a real failure?
- If the service changed its missing-result representation, what would need to change?

## Hints

Ask for an orientation hint first. Diagnostic hints and solution-shape guidance are available if needed; the implementation is yours to write.

## Stop conditions

Pause if the only available reproduction touches production data or requires a wider contract change. Bring that finding back so the card can be revised.
