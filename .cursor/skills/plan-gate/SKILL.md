---
name: plan-gate
description: >-
  Plan-first gate before implementation: confirm task understanding, draft a plan,
  assemble and register a subagent team if needed, show the intended approach, and
  wait for an explicit user go-signal. Use when the user invokes /plan-gate or asks
  for plan confirmation before starting work.
disable-model-invocation: true
---

# plan-gate

Meta-workflow for the **orchestrating agent**. Slash: `/plan-gate`.

## Hard stop

Until the user gives an explicit go-signal (`go`, `start`, `proceed`, `ok`, `поехали`, `старт`, or equivalent):

- Do **not** implement, edit project files, or create commits.
- Do **not** launch Task/subagents to perform the real work.
- Do **not** run mutating shell commands.
- Read-only exploration is allowed **only** if required to make the plan credible. Prefer planning from known catalogs first.

## Steps (mandatory order)

### 1. Confirm understanding

Restate the task: goal, in-scope / out-of-scope, key constraints, expected deliverables. If something critical is unclear, ask **one** clarifying question before the rest of the gate.

### 2. Implementation plan

Ordered steps, artifacts to touch or create, risks/dependencies, success checks.

### 3. Subagent team and registration

If specialized subagents help:

1. Select from `.cursor/agents/AGENTS_CATALOG.md` and `.cursor/agents/*.md`.
2. Prefer existing agents and skills over inventing new ones.
3. **Register** the team in the reply as a table:

| Role in this run | Agent / skill | Why | Parallel? |
|------------------|---------------|-----|-----------|
| … | `@name` or skill `name` | … | yes/no |

4. If a **new** agent or skill is required, propose name, purpose, and file path — do **not** create it until the go-signal.
5. If no subagents are needed, say so explicitly.

### 4. Show the full approach

Sequence after the signal, handoffs, gates/reviews, final deliverable. Short checklist for approval.

### 5. Wait for signal

End with an explicit stop, e.g. «Plan ready. Waiting for your go-signal before any execution.»

## After the go-signal

Execute the approved plan (or as amended). If scope changes, re-run the gate briefly for the delta.

## Anti-patterns

- Starting implementation before the signal.
- Registering agents that do not exist, then inventing them mid-run without approval.
- Vague plans without named steps or owners.
