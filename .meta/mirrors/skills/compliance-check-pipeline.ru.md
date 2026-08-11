---
name: compliance-check-pipeline
description: Оркестратор — terminology guard → doc guard → gost guard (макс. 3 цикла)
disable-model-invocation: true
---

# Compliance check pipeline (проверка соответствия)

Полный проход compliance по целевому файлу (файлам) документации.

## Когда использовать

- Перед выпуском deliverable
- Сценарии SC-D-01

## Цепочка

```
Loop (max 3):
  1. @terminology-consistency-guard
  2. @doc-consistency-guard
  3. @gost-compliance-guard (если применим normative_check)
  Stop if PASS WITH GAPS (irreconcilable) — не редактировать целевой файл автоматически
  Stop if PASS or PASS WITH FIXES только для устранимых пунктов
```

## Вход

- Путь(и) к целевому файлу — обязательно
- Фокусные разделы — опционально

## Выход

Сводный отчёт с цитатами (**016-source-citation-format**).  
Отчёты compliance → `paths.compliance_reports`.

Human approver: BA / QA.

## Руководство пользователя

- [.cursor/STARTER_PROMPT_COMPLIANCE.md](../../STARTER_PROMPT_COMPLIANCE.md) — руководство пользователя (RU)

*Зеркало: `.cursor/skills/compliance-check-pipeline/SKILL.md`*
