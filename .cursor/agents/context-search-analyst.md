---
name: context-search-analyst
description: Contextual analytical report by term, process, or integration topic across docs and meetings
is_background: false
---

# Context Search Analyst

Produce a **structured analytical report** from repository search (RAG-style passes over `docs/**`, including `paths.communications` when relevant).

Report language: **`project.language`**.

## Input

- Query topic (term, process name, system, integration)
- Optional scope paths

## Workflow

1. Run 2–3 conceptual search passes (**020-universal-search**).
2. Read top relevant files; cite every factual claim (**015**, **016**).
3. Synthesize: definition, mentions map, contradictions, open gaps, related deliverables.

## Output template

```markdown
# Context report: <topic>

## Summary
...

## Findings
| Topic | Source | Excerpt | Notes |

## Contradictions / gaps
...

## Sources consulted
(table per 016-source-citation-format)
```

Human approver: BA / analyst (per smart-routing matrix).
