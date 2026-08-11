---
name: context-search-report
description: RAG-style search across docs → structured report via @context-search-analyst
disable-model-invocation: true
---

# Context search report

## When to use

- Analytical question about term, process, integration
- Search for a topic across project docs, including meeting materials after export to the repo

## Steps

1. Validate query topic from user message.
2. Invoke **@context-search-analyst** with scope `docs/**` (+ communications if meeting-related).
3. Save report to `docs/04-registry/` or user-specified path.
4. Return summary + path.

Requires **015-anti-hallucination** citation density for eval.

Human approver: BA.

## User guide

- [.cursor/STARTER_PROMPT_CONTEXT_SEARCH.md](../../STARTER_PROMPT_CONTEXT_SEARCH.md) — user guide (RU)
