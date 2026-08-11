# Artifact paths — meeting-transcript-pipeline

Resolve from `project.manifest.yaml` when present.

| Artifact | Default path |
|----------|--------------|
| MyMeet raw imports | `docs/05-communications/_imports/mymeet/` |
| Transcripts | `docs/05-communications/transcripts/` |
| Screenshots | `docs/05-communications/media/<meeting>/screenshots/` |
| Tasks JSON (audit) | `docs/04-registry/meetings/<basename>.tasks.json` |
| Tasks Excel | `docs/04-registry/meetings/<basename>-tasks.xlsx` |
| Excel template | `platform/templates/meeting-tasks.xlsx` |
| Column schema | `platform/templates/meeting-tasks.columns.yaml` |

## Scripts

| Step | Command |
|------|---------|
| Merge parts | `python tools/merge_meeting_transcript_parts.py --parts ... --out ... --title "..."` |
| Build Excel | `python tools/build_meeting_task_report_xlsx.py --json ... --out ...` |
| Screenshot times | `python tools/parse_screenshot_timecode.py --dir <folder>` |

Ingest from mymeet.ai is via MCP skills (`mymeet-meeting-import`), not a local export script.

## Excel columns (7)

№ | Задача | Ответственный | Срок | Основание (тайм-код) | Выполнение. | Примечание

JSON keys: `task_num`, `task`, `responsible`, `deadline`, `timecode_basis`, `completion_status`, `notes`
