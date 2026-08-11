---
name: doc-consistency-guard
description: Check documents against primary spec, normative library, and decisions catalog; gap registry for irreconcilable issues
is_background: false
---

# Doc Consistency Guard

Cross-check **provided file(s)** against project reference documents. Report language: **`project.language`**.

## References (from manifest)

| Priority | Source |
|----------|--------|
| 1 | `references.primary_spec` |
| 2 | `paths.normative` |
| 3 | `references.decisions_catalog` |
| 4 | User-provided @-files in request |

Do not edit intake or normative **contents** without explicit instruction.

## Input

- Target path(s) — required
- Focus — sections, topics (optional)

## Workflow

1. Selectively read relevant spec/normative/decision fragments.
2. For each material claim in target: coverage, contradiction, internal consistency.
3. Classify: **resolvable** (wording fix) vs **irreconcilable** (needs customer decision).
4. Irreconcilable → gap in `paths.gaps/`; **do not** auto-edit target until gap resolved.
5. Resolvable → list fixes; may hand off to editing skill.

## Output

Status: **PASS** | **PASS WITH FIXES** | **PASS WITH GAPS**

Include citation table per **016-source-citation-format**.
