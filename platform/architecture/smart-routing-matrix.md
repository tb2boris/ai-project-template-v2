# Smart routing matrix (template)

| Task type | Input | Chain / Command | Output | Approver |
|-----------|-------|-----------------|--------|----------|
| Plan before work | Any non-trivial task | `plan-gate` `/plan-gate` | Approved plan + team roster | User |
| Init project | Filled manifest + intake | `project-init-pipeline` `/project-init-pipeline` | registry, glossary draft | PM |
| Compliance check | Draft in domains | `compliance-check-pipeline` `/compliance-check-pipeline` | compliance report, gaps | BA/QA |
| Context search | Query | `context-search-report` `/context-search-report` | registry report | BA |
| Meeting from mymeet | meeting id / title / date | `mymeet-meeting-pipeline` `/mymeet-meeting-pipeline` | transcript + Excel | PM/BA |
| Meeting import only | mymeet id | `mymeet-meeting-import` `/mymeet-meeting-import` | md + json | PM/BA |
| Meeting file on disk | transcript path | `meeting-transcript-pipeline` `/meeting-transcript-pipeline` | Excel, protocol | PM/BA |
| Requirements from meeting | Linked segments | `requirements-from-meeting` `/requirements-from-meeting` | spec/draft diff | BA/PM |
| Spec to code | OpenAPI / spec section | `spec-to-code-pipeline` `/spec-to-code-pipeline` | PR suggestion | Tech lead |
| Refresh indexes | Doc tree changes | `@structure-indexer` | file-registry + file-list.md | — |

Document placement & migrations: `platform/samples/document-lifecycle/STRUCTURE-AND-DOCUMENT-WORKFLOW.md`.

Customize per spoke project; keep in sync with **012-smart-routing-hints**.
