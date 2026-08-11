# /plan-gate

Plan-first gate for any implementation task. Confirm understanding, produce a plan, assemble and register the subagent team if needed, show the full approach — **do not start execution until the user signals**.

**Skill:** `.cursor/skills/plan-gate/SKILL.md`

---

## Input

The user message after `/plan-gate` is the **task**. If missing or ambiguous, ask one clarifying question, then continue the gate.

---

## Progress checklist

```
plan-gate
- [ ] 1. Confirm understanding of the task
- [ ] 2. Implementation plan
- [ ] 3. Subagent team (if needed) + registration
- [ ] 4. Show the full approach
- [ ] 5. Stop — wait for user signal before any execution
```

Follow the skill. End with an explicit wait for the go-signal. Do **not** edit files, launch Task/subagents for real work, or run mutating shell commands until the user signals.
