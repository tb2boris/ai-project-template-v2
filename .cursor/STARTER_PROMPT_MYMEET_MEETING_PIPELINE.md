# Инструкция: пайплайн mymeet → обработка совещания

**Основной способ загрузки встреч в hub-шаблоне** — MCP **mymeet.ai** (не VKS).

| Компонент | Путь |
|-----------|------|
| Slash (полный цикл) | [.cursor/commands/mymeet-meeting-pipeline.md](commands/mymeet-meeting-pipeline.md) |
| Slash (только импорт) | [.cursor/commands/mymeet-meeting-import.md](commands/mymeet-meeting-import.md) |
| Оркестратор | [.cursor/skills/mymeet-meeting-pipeline/SKILL.md](skills/mymeet-meeting-pipeline/SKILL.md) |
| Импорт | [.cursor/skills/mymeet-meeting-import/SKILL.md](skills/mymeet-meeting-import/SKILL.md) |
| MCP | [.cursor/mcp.json](mcp.json) |
| Настройка | [platform/deployment/mymeet-integration.md](../platform/deployment/mymeet-integration.md) |

---

## Когда использовать

| Ситуация | Команда |
|----------|---------|
| Новая встреча в mymeet → нормализация + Excel | **`/mymeet-meeting-pipeline`** |
| Только скачать транскрипт в репо | `/mymeet-meeting-import` |
| `.md` уже в `docs/05-communications/transcripts/` | `/meeting-transcript-pipeline` |
| Решения встречи → diff требований | `/requirements-from-meeting` |

---

## Что делает полный пайплайн

```
MCP mymeet (поиск + транскрипт)
  → docs/05-communications/_imports/mymeet/<id>.json
  → docs/05-communications/transcripts/<дата>_<название>.md
  → @meeting-terminology-normalizer
  → @meeting-demo-task-report-builder → Excel в docs/04-registry/meetings/
```

### Обязательно (или агент спросит один раз)

1. `meeting_id` **или** `встреча_mymeet` **или** `дата_встречи`

### Шаблон запуска

```
/mymeet-meeting-pipeline

meeting_id: <uuid-из-mymeet>
нормализация_терминов: да
отчет_excel: да
```

или

```
/mymeet-meeting-pipeline

встреча_mymeet: статус миграции
дата_встречи: 2026-08-10
```

---

## Предварительные условия

1. Скопировать `.env.example` → задать `MYMEET_API_KEY` в окружении ОС / профиле shell.
2. Ключ: https://app.mymeet.ai/settings
3. Перезагрузить Cursor; в Customize → MCP сервер `mymeet` должен быть зелёным.
4. Не коммитить секреты.

Источник истины для задач Excel — раздел **Транскрипт:** в `.md`, не блок «Задачи» из mymeet.
