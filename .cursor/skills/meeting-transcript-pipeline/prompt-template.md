# Prompt template — meeting-transcript-pipeline

Copy the block below into chat. Mark `[x]` on required checklist lines before sending.

Paths follow `project.manifest.yaml` (default: `docs/05-communications/`, `docs/04-registry/meetings/`).

---

```
## Параметры пайплайна

# Один из двух вариантов (обязательно):

# Вариант A — уже объединённый файл:
файл_встречи: docs/05-communications/transcripts/YYYY-MM-DD-meeting.md

# Вариант B — части для объединения:
# части_встречи:
#   - docs/05-communications/transcripts/meeting-ч1.md
#   - docs/05-communications/transcripts/meeting-ч2.md
# заголовок_объединения: "**YYYY-MM-DD. Тема встречи**"

нормализация_терминов: да
отчет_excel: да

# Явно, если есть скриншоты:
папка_скриншотов: docs/05-communications/media/YYYY-MM-DD/screenshots/

# Опционально (для колонки Примечание):
# release: 2
# demo_date: DD.MM.YYYY

## Чеклист

- [x] Задан файл_встречи ИЛИ части_встречи (+ заголовок_объединения)
- [x] Указано нормализация_терминов (да/нет)
- [x] Указано отчет_excel (да/нет)
- [ ] папка_скриншотов — если есть скрины

Запусти навык meeting-transcript-pipeline по .cursor/skills/meeting-transcript-pipeline/SKILL.md.
Не запрашивай подтверждений между шагами, кроме сбоя или нехватки обязательных параметров.
```

---

## Minimal full pipeline

```
части_встречи:
  - docs/05-communications/transcripts/demo-ч1.md
  - docs/05-communications/transcripts/demo-ч2.md
заголовок_объединения: "**2026-05-28. Статусное совещание**"
нормализация_терминов: да
отчет_excel: да
папка_скриншотов: docs/05-communications/media/demo-screens/

/meeting-transcript-pipeline
```

---

## Flags reference

| Parameter | Values | Default (full pipeline) |
|-----------|--------|-------------------------|
| `нормализация_терминов` | `да` / `нет` | `да` |
| `отчет_excel` | `да` / `нет` | `да` |
| `папка_скриншотов` | path | — (omit if none) |
