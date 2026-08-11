# MyMeet import — artifact paths

Paths relative to workspace root. Prefer values from `project.manifest.yaml` → `integrations.mymeet.export_paths` when set.

## Import staging

```
docs/05-communications/_imports/mymeet/
  <meeting-id>.json          # raw MCP response (metadata + payload refs)
```

## Pipeline-ready Markdown

```
docs/05-communications/transcripts/
  <YYYY-MM-DD>_<short-title>.md
```

**Filename:** `<YYYY-MM-DD>_<short-title>.md` (Cyrillic allowed; avoid `/\:*?"<>|`).

Optional track subfolders under `transcripts/` are allowed in spoke projects.

## Downstream

| Pipeline skill | Input field |
|----------------|-------------|
| `meeting-transcript-pipeline` | `файл_встречи` / `meeting_file` |
| `mymeet-meeting-pipeline` | resolves meeting then sets `файл_встречи` |
| `requirements-from-meeting` | same transcript path after import |
