# Инструкция: контекстный поиск и аналитический отчёт

Краткий справочник: аналитический поиск по документам проекта и материалам совещаний (после экспорта в репозиторий). Scope по умолчанию: `docs/**`, включая `paths.communications`.

Субагент: [AGENTS_CATALOG.md](agents/AGENTS_CATALOG.md) — `@context-search-analyst`.  
Навык-оркестратор: **`context-search-report`** — [SKILL.md](skills/context-search-report/SKILL.md).

---

## Когда что использовать

| Задача | Как запускать |
|--------|----------------|
| Определение термина / процесса по всему проекту | **`context-search-report`** или `@context-search-analyst` |
| Карта упоминаний интеграции (SC-E-02) | Отчёт с таблицей источников |
| Поиск по материалам совещаний (UC-3) | Scope `paths.communications` |
| Быстрый вопрос без сохранения файла | `@context-search-analyst` в чате |

**Требования:** каждое фактическое утверждение — с цитатой (**015**, **016**). Для eval: `source_citation_rate` ≥ 90% (пилот).

Утверждающий: **BA**.

---

## A. Быстрый запрос в чате

```
@context-search-analyst

Тема: <термин, процесс, система, интеграция>

Scope: docs/**
Язык отчёта: project.language из manifest

Нужны: определение, карта упоминаний, противоречия, открытые гэпы, список источников.
```

---

## B. Отчёт по доменной документации (SC-E-01)

```
/context-search-report

Тема: процесс закупок / учёт договоров / <ваша тема>
Scope: docs/02-domains/** , docs/03-deliverables/**

Сохранить отчёт:
docs/04-registry/context-report-<тема>-YYYY-MM-DD.md
```

---

## C. Поиск по совещаниям (UC-3)

После экспорта транскриптов в `docs/05-communications/`:

```
/context-search-report

Тема: обсуждения интеграции с <система> на статусных совещаниях
Scope: docs/05-communications/**

Включить: даты встреч, цитаты из транскриптов, связанные задачи из registry/meetings.
Сохранить: docs/04-registry/context-report-meetings-<тема>.md
```

Или:

```
@context-search-analyst

Найди все обсуждения темы «<тема>» в @docs/05-communications/
Структура отчёта — по шаблону агента context-search-analyst.
```

---

## D. Полный пайплайн (оркестратор)

```
/context-search-report

Запрос: <формулировка вопроса пользователя>
Scope: docs/**   # или явный список каталогов

Сохранить отчёт в paths.registry (по умолчанию docs/04-registry/).
Верни краткое резюме + путь к файлу.
```

**Порядок шагов skill:**

1. Уточнить тему из сообщения пользователя
2. `@context-search-analyst` — 2–3 прохода поиска (**020-universal-search**)
3. Сохранить структурированный отчёт
4. Краткое резюме в ответе чата

---

## Структура отчёта

См. шаблон в [context-search-analyst.md](agents/context-search-analyst.md): Summary, Findings (таблица), Contradictions/gaps, Sources consulted.

---

## Результаты

| Артефакт | Путь |
|----------|------|
| Аналитический отчёт | `docs/04-registry/context-report-*.md` (или путь из запроса) |

Утверждающий: **BA**.
