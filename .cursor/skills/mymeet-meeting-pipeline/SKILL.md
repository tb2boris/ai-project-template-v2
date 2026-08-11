---
name: mymeet-meeting-pipeline
description: >-
  End-to-end: fetch meeting from mymeet.ai (MCP) → import markdown →
  meeting-transcript-pipeline (terminology + Excel tasks). Use for
  /mymeet-meeting-pipeline or «забери встречу из mymeet и обработай».
disable-model-invocation: true
---

# MyMeet meeting pipeline (end-to-end)

Single entry: **mymeet.ai → repo transcript → normalize → Excel task report**.

**Prerequisite:** MCP `mymeet` (`.cursor/mcp.json`, `MYMEET_API_KEY`).

**Related:** [mymeet-meeting-import](../mymeet-meeting-import/SKILL.md), [meeting-transcript-pipeline](../meeting-transcript-pipeline/SKILL.md), [.cursor/STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md](../../STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md), [.cursor/commands/mymeet-meeting-pipeline.md](../../commands/mymeet-meeting-pipeline.md).

## When to use

- New meeting in mymeet → process in one pass.
- Slash: `/mymeet-meeting-pipeline`.
- Phrases: «забери из mymeet», «mymeet → транскрипт → Excel».

If `.md` already on disk → call `meeting-transcript-pipeline` directly.

## Required prompt fields

| Field | Required | Notes |
|-------|----------|-------|
| `meeting_id` **or** `встреча_mymeet` **or** `дата_встречи` | **Yes** (one of) | Identify meeting in mymeet |
| `нормализация_терминов` | No | Default: yes |
| `отчет_excel` | No | Default: yes |
| `папка_скриншотов` | No | Local media folder if any |

## Progress checklist

```
mymeet-meeting-pipeline
- [ ] 1. MCP mymeet: find meeting, status processed
- [ ] 2. Import JSON + markdown (mymeet-meeting-import)
- [ ] 3. meeting-transcript-pipeline on файл_встречи
- [ ] 4. Summary (paths, row counts)
```

## Steps

1. Confirm MCP `mymeet` available.
2. Resolve meeting (ID / search / list).
3. Run **mymeet-meeting-import** layout writes.
4. Invoke **meeting-transcript-pipeline** with `файл_встречи` = imported `.md`.
5. Do **not** treat mymeet «Задачи» block as sole source for Excel — report builder uses **Транскрипт:**.

## Gate

```
If none of (meeting_id, встреча_mymeet, дата_встречи) and no файл_встречи:
  → checklist + STOP

If MCP unavailable:
  → point to .env.example + mymeet-integration.md + STOP
```

Human approver: PM / BA.
