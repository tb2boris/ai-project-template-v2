---
name: meeting-demo-task-report-builder
description: Excel-отчёт задач из транскрипта; блок транскрипта — источник истины
is_background: false
---

# Meeting Demo Task Report Builder (сборщик Excel задач)

Извлечение задач и поручений из **транскрипта совещания** в Excel по шаблону `platform/templates/meeting-tasks.xlsx`.

Язык отчёта: **`project.language`**. Каталог выхода: **`paths.meetings_registry`**.

## Схема колонок (7 колонок)

См. `platform/templates/meeting-tasks.columns.yaml`:

| Колонка | JSON key |
|---------|----------|
| № | `task_num` |
| Задача | `task` |
| Ответственный | `responsible` |
| Срок | `deadline` |
| Основание (тайм-код) | `timecode_basis` |
| Выполнение. | `completion_status` |
| Примечание | `notes` |

Заголовки — корпоративный шаблон статусного совещания + **Примечание**.

## Источник истины

| Раздел | Роль |
|--------|------|
| **Блок транскрипта** (`Транскрипт:` или аналог) | **Авторитетный** для задач, ответственных, сроков |
| Саммари / темы | Только справочно |
| Блок **Задачи:** | Подсказки — каждая строка сверяется с транскриптом |

При противоречии саммари и транскрипта — **приоритет у транскрипта**.

## Вход

- Путь к файлу встречи — обязательно
- Опционально: папка скриншотов для **Примечание**

## Workflow

1. Разбор транскрипта с тайм-кодами.
2. JSON `{ "rows": [ { task_num, task, ... notes } ] }`.
3. `python tools/build_meeting_task_report_xlsx.py --json <path> --out <path>`.
4. Аудит: число строк, неоднозначные пункты, тайм-коды источников.

После `@meeting-terminology-normalizer`, если в транскрипте шум ASR.

*Зеркало: `.cursor/agents/meeting-demo-task-report-builder.md`*
