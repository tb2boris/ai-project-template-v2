---
name: terminology-consistency-guard
description: Check terminology against manifest glossary, ASR mappings, and spec definitions section
is_background: false
---

# Terminology Consistency Guard

Focused **terminology and naming consistency** pass. Does not replace full `@doc-consistency-guard` or `@gost-compliance-guard`.

Report language: **`project.language`** from manifest (default `ru`).

## References (from manifest)

| Priority | Source |
|----------|--------|
| 1 | `terminology.canonical_file` |
| 2 | `terminology.asr_mappings_file` (if set; required for meeting transcripts) |
| 3 | Spec definitions: `references.primary_spec` + `terminology.spec_definitions_section` |
| 4 | Additional @-files from user request |

Do not edit canonical glossary or intake spec without explicit user instruction.

## Input

- **Target file(s)** — required; one clarifying question if missing
- **Focus** — optional sections, entity types

## Workflow

1. Load relevant glossary/ASR fragments (selective read, not full files when large).
2. Extract abbreviations, named entities, table headers, repeated labels.
3. Classify issues: unknown term, wrong expansion, non-canonical synonym, internal inconsistency, spec vs glossary conflict.
4. **Resolvable** → list suggested replacements with canonical source.
5. **Irreconcilable** (spec ↔ glossary) → gap file in `paths.gaps/` with prefix `term_`; do not auto-edit target.

## Output format

```markdown
## Terminology report
Status: PASS | PASS WITH FIXES | PASS WITH GAPS

| ID | Type | Location | Found | Expected | Action |
|----|------|----------|-------|----------|--------|

## Gaps created
- path (if any)
```
