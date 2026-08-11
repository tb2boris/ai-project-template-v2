# Настройка AI-контура (Cursor / Windsurf)

**Версия:** 0.2  
**Для:** spoke-проект, клонированный из hub-шаблона

---

## 1. Открыть проект

1. Клонировать hub-шаблон в каталог проекта заказчика.
2. Заполнить `project.manifest.yaml`.
3. В Cursor: **File → Open Folder** → корень репозитория (каталог с `project.manifest.yaml`).
4. Убедиться, что видны `.cursor/rules/`, `project.manifest.yaml`, `docs/`.

---

## 2. Проверка rules

Rules подхватываются из `.cursor/rules/` автоматически.

| Проверка | Ожидание |
|----------|----------|
| Scope | Пути из манифеста |
| Язык `.cursor` | EN в rules/agents; RU в `.meta/mirrors/` |
| Anti-hallucination | Цитаты `[source: path § ...]` |

---

## 3. MCP — mymeet.ai (обязательно для встреч)

1. Задать `MYMEET_API_KEY` (см. `.env.example`, ключ: https://app.mymeet.ai/settings).
2. В репозитории есть `.cursor/mcp.json` с сервером `mymeet`.
3. Перезагрузить Cursor → Customize → MCP → `mymeet` connected.
4. Документация: [mymeet-integration.md](./mymeet-integration.md).

**Не коммитить** секреты.

Дополнительные MCP (filesystem/git и т.д.) — по политике ИБ spoke.

---

## 4. Python tools

```powershell
cd <корень-spoke>
python -m pip install -r tools/requirements-tools.txt
```

---

## 5. Первые сценарии

| Шаг | Действие |
|-----|----------|
| Init | `/project-init-pipeline` |
| План | `/plan-gate` |
| Индекс | `@structure-indexer` |
| Совещание из mymeet | [STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md](../../.cursor/STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md) |
| Compliance | [STARTER_PROMPT_COMPLIANCE.md](../../.cursor/STARTER_PROMPT_COMPLIANCE.md) |
| Поиск | [STARTER_PROMPT_CONTEXT_SEARCH.md](../../.cursor/STARTER_PROMPT_CONTEXT_SEARCH.md) |
| Spec → code | [STARTER_PROMPT_SPEC_TO_CODE.md](../../.cursor/STARTER_PROMPT_SPEC_TO_CODE.md) |

---

## 6. Ограничения

- PII — не во внешние модели без политики (rule **025**).
- Финальное согласование с заказчиком — человек.
- Изменения hub — через PR в hub-repo, затем sync на spoke.

---

## 7. Поддержка

- Lifecycle: `platform/samples/document-lifecycle/`
- Hub vs spoke: `platform/architecture/hub-vs-spoke.md`
- Smart-routing: `platform/architecture/smart-routing-matrix.md`
