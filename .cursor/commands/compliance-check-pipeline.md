# /compliance-check-pipeline

Run terminology → doc-consistency → gost-compliance (≤3 agents) on a target draft or deliverable. Write report under `paths.compliance_reports`; gaps under `paths.gaps`.

**Skill:** `.cursor/skills/compliance-check-pipeline/SKILL.md`  
**Starter:** `.cursor/STARTER_PROMPT_COMPLIANCE.md`

---

## Required

- Target file path under `docs/02-domains/**/drafts/` or `docs/03-deliverables/`
- Manifest `compliance.enabled` and packs

Human approver: BA / QA. Do not auto-edit the target on PASS WITH GAPS.
