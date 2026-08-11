# Domain extensions (optional)

Hub ships **core** rules, agents, skills, and commands only.

When a spoke needs specialized agents/skills/rules (customer letters, BPMN, industry forms, status-meeting carry-over, docx indexes), add them **in that project** under `.cursor/` or package as a domain-pack. List enabled extensions in `project.manifest.yaml` → `features.domain_packs`.

**Recommended optional universal ports** (not bundled in hub): see  
`platform/samples/document-lifecycle/UNIVERSAL-PACK.md` (section OPTIONAL_SPOKE).

There are **no pre-built packs** in this template release.
