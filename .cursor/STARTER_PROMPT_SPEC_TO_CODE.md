# Инструкция: реализация по спецификации (инженерный контур)

Краткий справочник для **этапа 4**: фрагмент ТЗ / OpenAPI → план → код → тесты → review. Рабочая зона: `paths.engineering`, `paths.contracts`, `paths.src`.

Субагент: [AGENTS_CATALOG.md](agents/AGENTS_CATALOG.md) — `@code-reviewer`.  
Навык-оркестратор: **`spec-to-code-pipeline`** — [SKILL.md](skills/spec-to-code-pipeline/SKILL.md).

Rules: `dev-core`, `dev-tests`, `dev-security`, `dev-docs-sync` (см. `.cursor/rules/`).

---

## Когда что использовать

| Задача | Как запускать |
|--------|----------------|
| Реализовать фрагмент по разделу ТЗ | **`spec-to-code-pipeline`** |
| Только code review перед merge | `@code-reviewer` + diff / файлы |
| Изменение API | Пайплайн + обновление `engineering/contracts/` в том же PR |

**Ограничения (dev-core, R-025):** без merge, push, deploy; small diffs; секреты не в коде.

Утверждающий: **Tech lead** (merge в репозиторий — только человек).

---

## A. Полный пайплайн

```
/spec-to-code-pipeline

Spec: @docs/01-intake/specification.md
Раздел: § <номер> — <название>

Контракт (если есть): @engineering/contracts/<api>.yaml
Целевые файлы: engineering/src/<модуль>/   # подсказка, не жёстко

Требования:
- План перед кодом (краткий список файлов)
- Тесты как контракт (dev-tests)
- Без секретов и hardcoded credentials (dev-security)
- При изменении API — обновить contract + spec в том же изменении (dev-docs-sync)
- В конце: @code-reviewer (read-only), сводка diff для Tech lead
```

---

## B. Только план (без реализации)

```
/spec-to-code-pipeline

Режим: только план

Spec: @<путь-к-spec> § <раздел>
Опиши: файлы, интерфейсы, тест-кейсы, риски.
Не пиши код до подтверждения Tech lead.
```

---

## C. Code review (отдельный шаг)

```
@code-reviewer

Изменения: @engineering/src/<файлы>
Spec: references.primary_spec § <релевантный раздел>

Чек-лист: security, edge cases, соответствие ТЗ, тесты.
Формат: таблица замечаний + severity; без автоматического merge.
```

---

## D. Порядок шагов skill

1. Прочитать раздел spec + `engineering/contracts/`
2. План (scope, файлы)
3. Реализация + тесты
4. Синхронизация контракта/документации при изменении API
5. `@code-reviewer` — второй проход
6. Сводка diff — ожидание решения Tech lead

---

## Результаты

| Артефакт | Где |
|----------|-----|
| Код и тесты | `engineering/src/`, тесты рядом или `**/*test*` |
| Обновлённый контракт | `engineering/contracts/` |
| Замечания review | Ответ агента в чате (не коммит без человека) |

Утверждающий: **Tech lead**.
