---
name: mymeet-meeting-import
description: >-
  Import meeting transcripts from mymeet.ai via MCP into docs/05-communications/,
  then optionally run meeting-transcript-pipeline. Use when the user asks to
  fetch, download, or import a meeting from mymeet.
disable-model-invocation: true
---

# MyMeet meeting import (MCP)

Fetches meeting data from **mymeet.ai** through the project MCP server (`mymeet` in `.cursor/mcp.json`) and saves artifacts for downstream meeting pipelines.

**Prerequisite:** `MYMEET_API_KEY` set; MCP server `mymeet` enabled in Cursor (Customize → MCP).

**Primary ingest path for meetings in this hub.** Prefer MyMeet over manual drops when the recording lives in mymeet.ai.

## When to use

- User asks to import / download a meeting from mymeet.ai.
- User provides a mymeet meeting ID or asks to search by title/date.
- Bridge step before `meeting-transcript-pipeline` or skill `mymeet-meeting-pipeline`.

## MCP tools (mymeet server)

Typical flow (adapt if tool names differ — list tools from Customize → MCP → mymeet):

1. **Search / list** — find meeting by title, date, or keyword (`mymeet_search_meetings`, `mymeet_list_meetings`).
2. **Status** — ensure meeting is `processed`.
3. **Transcript** — `mymeet_get_transcript` (speaker-tagged text).
4. **Report** (optional) — `mymeet_get_meeting_report` for metadata/chapters (not sole source for tasks).

## Output layout

| Artifact | Default path |
|----------|--------------|
| Raw import (JSON/metadata) | `docs/05-communications/_imports/mymeet/<meeting-id>.json` |
| Markdown for pipelines | `docs/05-communications/transcripts/<YYYY-MM-DD>_<title>.md` |

See [artifact-paths.md](artifact-paths.md).

## Markdown template for pipelines

```markdown
# <Meeting title>

**Дата:** <YYYY-MM-DD>
**Источник:** mymeet.ai (meeting ID: <id>)

## Транскрипт:

<speaker-tagged transcript body>

## Задачи:

<action items from mymeet summary, if any — pipelines re-derive from Транскрипт:>
```

## Orchestrator behaviour

1. Confirm MCP `mymeet` is connected (MCP Logs on failure).
2. Resolve meeting: user ID **or** search via MCP.
3. Fetch transcript (+ optional report).
4. Write files per table; normalize date in filename.
5. If user asked for full processing → continue with `meeting-transcript-pipeline` / `mymeet-meeting-pipeline` using `файл_встречи` = saved `.md`.
6. Otherwise summarize paths and offer next step.

## Gate

```
If MYMEET_API_KEY not set or MCP mymeet unavailable:
  → instruct: set env from .env.example, reload Cursor
  → STOP

If meeting not found and no search criteria:
  → ask for meeting ID, title fragment, or date
  → STOP
```

## Related

- MCP: `.cursor/mcp.json`
- End-to-end: `mymeet-meeting-pipeline` (`/mymeet-meeting-pipeline`)
- Downstream: `meeting-transcript-pipeline`
- Setup: `platform/deployment/mymeet-integration.md`
