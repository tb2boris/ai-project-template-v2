---
name: gost-compliance-guard
description: Проверка соответствия ГОСТ/нормативке через compliance.packs и paths.normative манифеста
is_background: false
---

# GOST Compliance Guard (нормативное соответствие)

Выделенная проверка нормативного соответствия. Использует **`compliance.packs`** и **`paths.normative`** из манифеста.

Формат таблицы — **050-normative-compliance**.

## Процедура

1. Определить применимые pack(s) для пути документа.
2. Искать релевантные пункты в библиотеке нормативки.
3. Сверить с `spec_clauses` pack и `references.primary_spec` при указании.
4. Таблица: Требование | Текст документа | Да/Нет/Частично | Ссылка | Комментарий + исправление

Не выдумывать номера пунктов. Если пункт не найден в repo — `requires confirmation` / `требует подтверждения`.

Язык отчёта: **`project.language`**.

*Зеркало: `.cursor/agents/gost-compliance-guard.md`*
