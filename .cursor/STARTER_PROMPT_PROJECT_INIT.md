# Инструкция: инициализация нового spoke-проекта

После клонирования hub-шаблона. Чек-лист: rule **046-project-init-checklist**.

---

## Быстрый старт

```
/project-init-pipeline

Проект: <имя из manifest>
Intake: docs/01-intake/ (уже загружен: да/нет)
Создать черновик глоссария из ТЗ: да
Запустить @structure-indexer: да
```

---

## Ручной чек-лист

1. [ ] `project.manifest.yaml` заполнен
2. [ ] `docs/01-intake/specification.md` (или путь из `references.primary_spec`)
3. [ ] `docs/04-registry/terminology/terms.md` — черновик из § определений ТЗ
4. [ ] `@structure-indexer` → `docs/04-registry/file-registry.md`
5. [ ] `.cursor/mcp.json` — по `platform/deployment/AI-contour-setup.md`

---

## Следующие сценарии

- Compliance: [STARTER_PROMPT_COMPLIANCE.md](STARTER_PROMPT_COMPLIANCE.md)
- Поиск / аналитика: [STARTER_PROMPT_CONTEXT_SEARCH.md](STARTER_PROMPT_CONTEXT_SEARCH.md)
- Совещание: [STARTER_PROMPT_MEETING_PIPELINE.md](STARTER_PROMPT_MEETING_PIPELINE.md)
- Реализация по ТЗ: [STARTER_PROMPT_SPEC_TO_CODE.md](STARTER_PROMPT_SPEC_TO_CODE.md)
