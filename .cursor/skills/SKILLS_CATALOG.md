# Skills Catalog

**Version:** 2.0  
**Location:** `.cursor/skills/<name>/SKILL.md`  
**Commands:** `.cursor/commands/`

## Core

| ID | Skill | Chain | Stage | Command |
|----|-------|-------|-------|---------|
| S-000 | `plan-gate` | understand → plan → register team → wait signal | 0 | `/plan-gate` |
| S-030 | `project-init-pipeline` | manifest → glossary → @structure-indexer | 1 | `/project-init-pipeline` |
| S-010 | `compliance-check-pipeline` | terminology → doc → gost (≤3) | 2 | `/compliance-check-pipeline` |
| S-011 | `context-search-report` | @context-search-analyst | 2 | `/context-search-report` |
| S-050 | `mymeet-meeting-import` | MCP mymeet → transcripts/_imports | 3 | `/mymeet-meeting-import` |
| S-051 | `mymeet-meeting-pipeline` | import → meeting-transcript-pipeline | 3 | `/mymeet-meeting-pipeline` |
| S-001 | `meeting-transcript-pipeline` | normalize → Excel (file on disk) | 3 | `/meeting-transcript-pipeline` |
| S-040 | `requirements-from-meeting` | segments → diff → @doc-consistency-guard | 3 | `/requirements-from-meeting` |
| S-020 | `spec-to-code-pipeline` | plan → code → test → @code-reviewer | 4 | `/spec-to-code-pipeline` |

**Meeting ingest:** MyMeet MCP is primary (`/mymeet-meeting-pipeline`). See `platform/deployment/mymeet-integration.md`. VKS is deprecated.

Optional spoke ports: `platform/samples/document-lifecycle/UNIVERSAL-PACK.md`.

Status: see `platform/architecture/STATUS.md`.
