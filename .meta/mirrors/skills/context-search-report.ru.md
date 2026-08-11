---
name: context-search-report
description: RAG-поиск по docs → структурированный отчёт через @context-search-analyst
disable-model-invocation: true
---

# Context search report (контекстный отчёт)

## Когда использовать

- Аналитический вопрос о термине, процессе, интеграции
- Поиск упоминаний темы по документам проекта, в том числе по материалам совещаний после экспорта в репозиторий

## Шаги

1. Уточнить тему запроса из сообщения пользователя.
2. Вызвать **@context-search-analyst** с scope `docs/**` (+ communications, если связано с совещанием).
3. Сохранить отчёт в `docs/04-registry/` или указанный пользователем путь.
4. Вернуть сводку + путь.

Требуется плотность цитирования **015-anti-hallucination** для eval.

Human approver: BA.

## Руководство пользователя

- [.cursor/STARTER_PROMPT_CONTEXT_SEARCH.md](../../STARTER_PROMPT_CONTEXT_SEARCH.md) — руководство пользователя (RU)

*Зеркало: `.cursor/skills/context-search-report/SKILL.md`*
