# Инструкция: проверка документа на соответствие

Краткий справочник: **отдельные агенты** и **полный пайплайн compliance**. Пути — по `project.manifest.yaml` (эталоны: `references.primary_spec`, `compliance.packs`, `paths.compliance_reports`).

Субагенты: [AGENTS_CATALOG.md](agents/AGENTS_CATALOG.md) — `@terminology-consistency-guard`, `@doc-consistency-guard`, `@gost-compliance-guard`.  
Навык-оркестратор: **`compliance-check-pipeline`** — [SKILL.md](skills/compliance-check-pipeline/SKILL.md).

Шаблон отчёта: [platform/templates/compliance-report-template.md](../platform/templates/compliance-report-template.md).

---

## Когда что использовать

| Задача | Как запускать |
|--------|----------------|
| Только термины | `@terminology-consistency-guard` + файл |
| Сверка с ТЗ и решениями | `@doc-consistency-guard` + файл |
| Нормативное соответствие (ГОСТ / packs) | `@gost-compliance-guard` + файл |
| Полная проверка перед релизом (SC-D-01) | **`compliance-check-pipeline`** |
| Пакет писем / однотипных документов (SC-D-02) | Пайплайн по каждому файлу или списку |

**Human-in-the-loop:** при статусе **PASS WITH GAPS** агент **не** правит целевой документ автоматически — гэпы фиксируются в `paths.gaps`, отчёт — в `paths.compliance_reports`. Утверждает **BA / QA**.

**Цитаты:** обязательны по rules **015-anti-hallucination**, **016-source-citation-format**.

---

## A. Только терминология

```
@terminology-consistency-guard

Файл: @docs/02-domains/<домен>/drafts/<документ>.md

Эталон: terminology.canonical_file из project.manifest.yaml
Режим: отчёт + предлагаемые правки (согласовать с BA)
```

---

## B. Сверка с ТЗ и каталогом решений

```
@doc-consistency-guard

Файл: @docs/03-deliverables/<путь>/<документ>.md

Эталоны:
- references.primary_spec
- references.decisions_catalog (если указан)
Фокус: разделы 1–3 (опционально)
```

---

## C. Нормативное соответствие

```
@gost-compliance-guard

Файл: @<проверяемый-документ>.md

Пакеты: compliance.packs из project.manifest.yaml
Нормативка: paths.normative
```

---

## D. Полный пайплайн (оркестратор)

```
/compliance-check-pipeline

Файл: @docs/02-domains/<домен>/drafts/<документ>.md
Фокус: разделы 3–5   # опционально; пусто = весь документ

Эталоны — из project.manifest.yaml:
- references.primary_spec
- paths.normative (для gost guard)

Сохранить сводный отчёт:
docs/04-registry/compliance-reports/<документ>-YYYY-MM-DD.md

Цепочка (до 3 циклов): terminology → doc → gost.
Остановиться на PASS / PASS WITH FIXES / PASS WITH GAPS.
```

**Порядок шагов skill:**

1. `@terminology-consistency-guard`
2. `@doc-consistency-guard`
3. `@gost-compliance-guard` (если включён compliance в manifest)
4. Сводный отчёт по шаблону compliance-report-template

---

## Результаты

| Артефакт | Путь |
|----------|------|
| Отчёт compliance | `paths.compliance_reports` |
| Неустранимые гэпы | `paths.gaps/<id>.md` |

Утверждающий: **BA / QA**.
