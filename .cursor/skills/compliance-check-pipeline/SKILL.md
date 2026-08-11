---
name: compliance-check-pipeline
description: Orchestrator — terminology guard → doc guard → gost guard (max 3 cycles)
disable-model-invocation: true
---

# Compliance check pipeline

Full documentation compliance pass on target file(s).

## When to use

- Before deliverable release
- SC-D-01 scenarios

## Chain

```
Loop (max 3):
  1. @terminology-consistency-guard
  2. @doc-consistency-guard
  3. @gost-compliance-guard (if normative_check applies)
  Stop if PASS WITH GAPS (irreconcilable) — do not auto-edit target
  Stop if PASS or PASS WITH FIXES only resolvable items
```

## Input

- Target file path(s) — required
- Focus sections — optional

## Output

Combined report with citations (**016-source-citation-format**).  
Compliance reports → `paths.compliance_reports`.

Human approver: BA / QA.

## User guide

- [.cursor/STARTER_PROMPT_COMPLIANCE.md](../../STARTER_PROMPT_COMPLIANCE.md) — user guide (RU)
