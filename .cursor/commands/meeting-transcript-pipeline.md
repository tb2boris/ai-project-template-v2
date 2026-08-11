# /meeting-transcript-pipeline

Process a meeting **file already in the repo**: optional merge → `@meeting-terminology-normalizer` → `@meeting-demo-task-report-builder` (Excel).

**If the meeting is still only in mymeet.ai** → use `/mymeet-meeting-pipeline` instead.

**Skill:** `.cursor/skills/meeting-transcript-pipeline/SKILL.md`  
**Starter:** `.cursor/STARTER_PROMPT_MEETING_PIPELINE.md`  
**Tools:** `tools/merge_meeting_transcript_parts.py`, `tools/parse_screenshot_timecode.py`, `tools/build_meeting_task_report_xlsx.py`

---

## Required

- `файл_встречи` **or** `части_встречи` (+ merge title)
- Optional: screenshot folder, Excel on/off, terminology on/off

Outputs under `docs/05-communications/` and `docs/04-registry/meetings/`.
