# Hub vs Spoke

**Version:** 1.0  
**Date:** 2026-06-10

## Model

```
Hub (this template)  ──clone──►  Spoke (customer project repo)
         │                                    │
         │ PR / tag sync                      │ project.manifest.yaml
         └────────────────────────────────────┘
```

- **Hub** — maintained centrally; contains universal rules, agents, skills, platform templates.
- **Spoke** — one repo per customer project; PM fills manifest; team works in `docs/` and `engineering/`.

## What lives in the hub (core)

### Rules (`.cursor/rules/`)

| Tier | Rules | Notes |
|------|-------|-------|
| core | 005, 010, 015, 016, 020, 025, 030, 040, 045, 046, 050, 070, 012 | Read paths from manifest |
| core | dev-core, dev-tests, dev-security, dev-docs-sync | Engineering contour |

### Agents (`.cursor/agents/`)

| Tier | Agents |
|------|--------|
| core | `@structure-indexer`, `@terminology-consistency-guard`, `@doc-consistency-guard`, `@gost-compliance-guard`, `@question-dedup-guard` (optional), `@context-search-analyst`, `@meeting-terminology-normalizer`, `@meeting-demo-task-report-builder`, `@code-reviewer` |

### Skills (`.cursor/skills/`)

| Tier | Skills |
|------|--------|
| core | `project-init-pipeline`, `compliance-check-pipeline`, `context-search-report`, `meeting-transcript-pipeline`, `requirements-from-meeting`, `spec-to-code-pipeline` |

## What is configured in the spoke

Single source of truth: **`project.manifest.yaml`** at repository root.

| Section | Purpose |
|---------|---------|
| `project` | Name, customer, language |
| `paths` | All canonical directory paths |
| `references` | Primary spec, charter, decisions |
| `terminology` | Glossary and ASR mappings |
| `compliance.packs` | Normative clause packs (project-specific) |
| `scope_matrix` | Which paths are editable, style level, compliance |
| `integrations` | VKS, question tracker, etc. |
| `boundary` | Forbidden external paths |

Core rules and agents **must not** hardcode customer names, spec file names, or legacy path layouts.

## Optional domain extensions

Hub v0.1 does **not** include ready-made domain packs. Spoke projects may add project-specific agents, skills, and rules when scope requires it. Register extensions in `features.domain_packs` in the manifest. See `platform/domain-packs/README.md`.

## Sync hub → spoke

1. Hub release tagged (e.g. `platform-v1.0`).
2. Spokes cherry-pick or merge `.cursor/`, `platform/`, `tools/` changes.
3. Do **not** overwrite spoke `project.manifest.yaml` or `docs/01-intake/` without review.
4. Run eval smoke on spoke after sync.

## Russian mirrors

Human-readable RU copies: `.meta/mirrors/{rules,agents,skills}/` — not mixed with project documents.
