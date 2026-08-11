---
name: spec-to-code-pipeline
description: Фрагмент spec → plan → implement → test → @code-reviewer
disable-model-invocation: true
---

# Spec to code pipeline (от спецификации к коду)

Инженерный поток от спецификации до предложения PR после review.

## Когда использовать

- Smart-route: реализация фрагмента по spec / OpenAPI
- Dev-контур этапа 4

## Шаги

```
- [ ] 0. Прочитать раздел spec + engineering/contracts/
- [ ] 1. Plan (малый scope) — файлы для изменения
- [ ] 2. Implement + tests (правила dev-tests, dev-security)
- [ ] 3. Обновить contract при изменении API (dev-docs-sync)
- [ ] 4. @code-reviewer read-only pass
- [ ] 5. Представить сводку diff — human merge
```

## Ограничения

- Без merge/push/deploy (dev-core, R-025)
- Цитировать разделы spec для утверждений о поведении

Human approver: Tech lead.

## Руководство пользователя

- [.cursor/STARTER_PROMPT_SPEC_TO_CODE.md](../../STARTER_PROMPT_SPEC_TO_CODE.md) — руководство пользователя (RU)

*Зеркало: `.cursor/skills/spec-to-code-pipeline/SKILL.md`*
