---
name: requirements-from-meeting
description: Linked segments совещания → diff требований → проверка doc consistency
disable-model-invocation: true
---

# Requirements from meeting (требования из совещания)

Извлечь из материалов совещания новые и уточнённые требования и предложить правки к ТЗ или черновику домена.

## Когда использовать

- После экспорта linked-segments из VKS
- Пользователь просит обновить требования по решениям совещания

## Шаги

1. Прочитать linked-segments + транскрипт из `paths.communications`.
2. Выявить решения уровня требований (scope, сроки, ограничения).
3. Подготовить diff относительно `references.primary_spec` или domain draft в `docs/02-domains/`.
4. Вызвать `@doc-consistency-guard` для предложенных изменений.
5. Выход: diff markdown + список гэпов при неустранимых расхождениях.

Human approver: BA / PM перед слиянием в deliverables.

*Зеркало: `.cursor/skills/requirements-from-meeting/SKILL.md`*
