---
name: project-init-pipeline
description: Initialize spoke project — manifest check, intake layout, glossary draft, structure index
disable-model-invocation: true
---

# Project init pipeline

Orchestrates new spoke setup after cloning template.

## When to use

- PM/analyst starts new project
- Explicit invoke: `/project-init-pipeline`

## Steps (sequential)

```
- [ ] 0. Verify project.manifest.yaml filled (required fields)
- [ ] 1. Confirm docs/01-intake/ has primary spec (or list missing)
- [ ] 2. Create draft glossary at terminology.canonical_file from spec definitions
- [ ] 3. Invoke @structure-indexer → file-registry.md
- [ ] 4. Optional: @terminology-consistency-guard on intake index doc
- [ ] 5. Print init summary + remaining manual steps (MCP, optional project extensions)
```

## Gate

If manifest missing or invalid → stop with checklist referencing **046-project-init-checklist**.

Human approver: PM / BA.
