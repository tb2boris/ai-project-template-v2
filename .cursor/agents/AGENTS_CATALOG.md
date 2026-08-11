# Agents Catalog

**Version:** 1.1  
**Location:** `.cursor/agents/*.md`

**Tier:** `core` = hub template  
**Lifecycle guide:** `platform/samples/document-lifecycle/`  
**Optional agents (not in hub):** see `UNIVERSAL-PACK.md` in that folder.

## Core (hub template)

| ID | Invoke | Purpose | Stage |
|----|--------|---------|-------|
| A-008 | `@structure-indexer` | File registry and file-list.md | 1 |
| A-012 | `@terminology-consistency-guard` | Glossary consistency | 1 |
| A-011 | `@doc-consistency-guard` | Spec/normative/decisions check | 2 |
| A-002 | `@gost-compliance-guard` | Normative compliance table | 2 |
| A-009 | `@question-dedup-guard` | Customer Q&A dedup (optional) | 2 |
| A-E01 | `@context-search-analyst` | Contextual analytical report | 2 |
| A-015 | `@meeting-terminology-normalizer` | Transcript terminology | 3 |
| A-016 | `@meeting-demo-task-report-builder` | Meeting tasks Excel | 3 |
| A-SUB-02 | `@code-reviewer` | Pre-merge code review | 4 |

Hub v0.1 includes **core agents only**. Project-specific agents are added in spoke repos when needed; see `platform/domain-packs/README.md`.

## Status legend

`planned` | `in progress` | `done` | `deprecated`

Current hub status: see `platform/architecture/STATUS.md`.
