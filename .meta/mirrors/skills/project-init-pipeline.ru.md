---
name: project-init-pipeline
description: Инициализация spoke-проекта — проверка манифеста, intake, черновик глоссария, индекс структуры
disable-model-invocation: true
---

# Project init pipeline (инициализация проекта)

Оркестратор настройки нового spoke после клонирования шаблона.

## Когда использовать

- PM/аналитик запускает новый проект
- Явный вызов: `/project-init-pipeline`

## Шаги (последовательно)

```
- [ ] 0. Проверить заполнение project.manifest.yaml (обязательные поля)
- [ ] 1. Убедиться, что docs/01-intake/ содержит основное ТЗ (или перечислить отсутствующее)
- [ ] 2. Создать черновик глоссария в terminology.canonical_file из определений ТЗ
- [ ] 3. Вызвать @structure-indexer → file-registry.md
- [ ] 4. Опционально: @terminology-consistency-guard для intake index doc
- [ ] 5. Вывести сводку init + оставшиеся ручные шаги (MCP, опциональные расширения проекта)
```

## Gate

Если манифест отсутствует или невалиден → остановиться с чек-листом, ссылаясь на **046-project-init-checklist**.

Human approver: PM / BA.

*Зеркало: `.cursor/skills/project-init-pipeline/SKILL.md`*
