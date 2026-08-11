# Инструкция: требования из материалов встречи

Справочник для skill **`requirements-from-meeting`**. Пути — по `project.manifest.yaml`.

Субагенты: `@doc-consistency-guard` (обязательно на предлагаемый diff).  
Связанные: `@meeting-terminology-normalizer` (если транскрипт ещё сырой), пайплайн встречи — `STARTER_PROMPT_MEETING_PIPELINE.md`.

Slash: `/requirements-from-meeting`.

---

## Когда использовать

| Задача | Как запускать |
|--------|----------------|
| Решения встречи → правки требований | **`requirements-from-meeting`** |
| Сначала нормализовать термины в транскрипте | `@meeting-terminology-normalizer` или полный meeting pipeline |
| После diff — полная compliance перед deliverable | `/compliance-check-pipeline` |

**Нельзя:** переписывать файлы в `docs/01-intake/`. Только черновики в `docs/02-domains/**/drafts/` или предложение diff к spec (согласование BA).

---

## Шаблон запуска

```
/requirements-from-meeting

файл_встречи: @docs/05-communications/transcripts/<встреча>.md
цель: @docs/02-domains/<домен>/drafts/<документ>.md
(или сверка с references.primary_spec из манифеста)

режим: предложить diff + список гэпов
```

---

## Ожидаемый результат

1. Список requirement-level решений со ссылками на фрагменты транскрипта (rules **015**, **016**).
2. Diff markdown (что добавить/изменить в черновике или spec-проекции).
3. Протокол `@doc-consistency-guard`.
4. При несогласуемых пунктах — файлы в `paths.gaps`.

Утверждает **BA / PM** до миграции черновика в `docs/03-deliverables/`.
