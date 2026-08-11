# docs/05-communications — коммуникации и встречи

## Назначение

| Подпапка | Назначение |
|----------|------------|
| `_imports/mymeet/` | Сырой JSON импорт из mymeet.ai (MCP) |
| `transcripts/` | Транскрипты (pipeline-ready `.md`) |
| `media/` | Скриншоты и вложения |
| `protocols/` | Краткие протоколы / мемо |

## Пайплайны (primary = MyMeet)

- `/mymeet-meeting-pipeline` — MCP mymeet → import → термины → Excel
- `/mymeet-meeting-import` — только импорт
- `/meeting-transcript-pipeline` — если `.md` уже на диске
- `/requirements-from-meeting` — решения → drafts

Настройка: `platform/deployment/mymeet-integration.md`

## Миграция

| Из | В | Триггер |
|----|---|---------|
| mymeet.ai (MCP) | `_imports/mymeet/` + `transcripts/` | `/mymeet-meeting-import` |
| `transcripts/` | `04-registry/meetings/` | Excel задач |
| `transcripts/` | `02-domains/**/drafts/` | Выжимка требований |

Сырой транскрипт **не** публикуется как `03-deliverables` без согласованного формата.
