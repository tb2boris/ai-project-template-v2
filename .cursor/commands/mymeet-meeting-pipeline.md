# /mymeet-meeting-pipeline

Fetch a meeting from **mymeet.ai** (MCP) → save transcript under `docs/05-communications/` → run `meeting-transcript-pipeline` (terminology + Excel).

**Skills:** `.cursor/skills/mymeet-meeting-pipeline/SKILL.md`, `.cursor/skills/mymeet-meeting-import/SKILL.md`  
**Starter:** `.cursor/STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md`  
**Setup:** `platform/deployment/mymeet-integration.md`

---

## Input (one of)

- `meeting_id: <uuid>`
- `встреча_mymeet: <title fragment>`
- `дата_встречи: <YYYY-MM-DD>`

Optional: `нормализация_терминов`, `отчет_excel`, `папка_скриншотов`.

---

## Progress checklist

```
mymeet-meeting-pipeline
- [ ] 1. MCP mymeet: find + processed
- [ ] 2. Import JSON + markdown
- [ ] 3. meeting-transcript-pipeline
- [ ] 4. Summary
```

Requires `MYMEET_API_KEY` and MCP server `mymeet` in `.cursor/mcp.json`.
