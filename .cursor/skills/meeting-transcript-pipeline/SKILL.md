---
name: meeting-transcript-pipeline
description: >-
  Meeting file on disk → terminology normalizer → demo task Excel report.
  Prefer ingest via mymeet-meeting-import / mymeet-meeting-pipeline (MCP mymeet.ai).
disable-model-invocation: true
---

# Meeting transcript pipeline

Downstream orchestrator for a **transcript already in the repo** (usually imported from **mymeet.ai**).

**Primary ingest:** skill `mymeet-meeting-import` / `mymeet-meeting-pipeline` (MCP).  
Manual drop of `.md` into `docs/05-communications/transcripts/` is supported.  
VKS export stub is **deprecated** — do not use for new projects.

## When to use

- Full meeting processing: transcript → normalized → Excel tasks
- Explicit invoke: `/meeting-transcript-pipeline`
- After MyMeet import when user already has `файл_встречи`

## Required input

| Field | Required |
|-------|----------|
| `meeting_file` / `файл_встречи` **OR** `части_встречи` | Yes |
| `normalize_terminology` | Default: yes |
| `excel_report` | Default: yes |
| `screenshot_folder` | Optional |

If the meeting is only in mymeet and not yet on disk → run **`mymeet-meeting-pipeline`** instead.

## Steps

```
- [ ] 0. Validate inputs (file or parts); reject vks_meeting_id for new work — redirect to MyMeet
- [ ] 1. Optional merge: tools/merge_meeting_transcript_parts.py
- [ ] 2. @meeting-terminology-normalizer (if enabled)
- [ ] 3. @meeting-demo-task-report-builder → tools/build_meeting_task_report_xlsx.py (if enabled)
- [ ] 4. Summary for user (paths, row counts)
```

## Related files

- [prompt-template.md](prompt-template.md)
- [artifact-paths.md](artifact-paths.md)
- [.cursor/STARTER_PROMPT_MEETING_PIPELINE.md](../../STARTER_PROMPT_MEETING_PIPELINE.md)
- [.cursor/STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md](../../STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md)

## Paths (from manifest)

- Transcripts: `paths.communications` / `integrations.mymeet.export_paths.transcripts`
- Tasks JSON/Excel: `paths.meetings_registry`
- Builder: `meeting_tasks.builder_script`

## Merge command (when `части_встречи`)

```bash
python tools/merge_meeting_transcript_parts.py \
  --parts <part1> <part2> ... \
  --out <merged.md> \
  --title "<title>"
```

Human approver: PM / BA.
