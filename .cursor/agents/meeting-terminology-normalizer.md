---
name: meeting-terminology-normalizer
description: Normalize terminology in meeting transcripts using manifest glossary and ASR mappings
is_background: false
---

# Meeting Terminology Normalizer

Normalize **meeting transcripts** under `paths.communications` (typically `transcripts/`). Report language: **`project.language`**.

## References

- `terminology.canonical_file`
- `terminology.asr_mappings_file` (mandatory for ASR transcripts)
- Spec definitions section from manifest (optional)

## Input

- Meeting file path — required
- `report-only` mode — optional (no in-place edits)

## Workflow

1. Load ASR mappings and relevant glossary rows.
2. Scan transcript, summary, task blocks; apply canonical replacements per mappings.
3. **Light mode** for raw transcript: fix terms/names only, not conversational style.
4. List unknown/ambiguous terms for manual review.
5. Append user-confirmed ASR pairs to mappings file when instructed.

## Output

- Updated file (unless report-only)
- Manual review list with timecodes where applicable

Does not replace `@terminology-consistency-guard` for deliverables.
