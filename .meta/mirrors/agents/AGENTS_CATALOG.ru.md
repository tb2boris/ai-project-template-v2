# Справочник агентов (зеркало)

**Версия:** 1.1  
**Расположение основных файлов:** `.cursor/agents/*.md`  
**Русские копии:** `.meta/mirrors/agents/*.ru.md`

**Tier:** `core` = hub-шаблон  
**Lifecycle:** `platform/samples/document-lifecycle/`  
**Опциональные агенты (не в hub):** `UNIVERSAL-PACK.md` в том каталоге.

## Core (hub-шаблон)

| ID | Вызов | Назначение | Этап |
|----|-------|------------|------|
| A-008 | `@structure-indexer` | Реестр файлов и file-list.md | 1 |
| A-012 | `@terminology-consistency-guard` | Согласованность терминов | 1 |
| A-011 | `@doc-consistency-guard` | Сверка с ТЗ/нормативкой/решениями | 2 |
| A-002 | `@gost-compliance-guard` | Таблица нормативного соответствия | 2 |
| A-009 | `@question-dedup-guard` | Дедуп вопросов заказчику (опционально) | 2 |
| A-E01 | `@context-search-analyst` | Контекстный аналитический отчёт | 2 |
| A-015 | `@meeting-terminology-normalizer` | Термины в транскрипте | 3 |
| A-016 | `@meeting-demo-task-report-builder` | Excel задач совещания | 3 |
| A-SUB-02 | `@code-reviewer` | Code review перед merge | 4 |

Hub v0.1 включает **только core-агентов**. Специализированные агенты добавляются в spoke-проекте по необходимости; см. `platform/domain-packs/README.md`.

*Зеркало: `.cursor/agents/AGENTS_CATALOG.md`*
