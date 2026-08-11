# /project-init-pipeline

Initialize a spoke project after cloning the hub template: validate manifest, check intake, draft glossary, run `@structure-indexer`.

**Skill:** `.cursor/skills/project-init-pipeline/SKILL.md`  
**Starter:** `.cursor/STARTER_PROMPT_PROJECT_INIT.md`

---

## Progress checklist

```
project-init-pipeline
- [ ] 0. Verify project.manifest.yaml
- [ ] 1. Confirm docs/01-intake/ primary materials
- [ ] 2. Draft glossary at terminology.canonical_file
- [ ] 3. @structure-indexer → file-registry.md + file-list.md
- [ ] 4. Optional terminology guard on intake index
- [ ] 5. Init summary + remaining manual steps
```

If manifest invalid → stop (rule **046-project-init-checklist**).
