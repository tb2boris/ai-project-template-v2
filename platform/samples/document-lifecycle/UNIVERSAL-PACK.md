# Универсальная компоновка Cursor (отбор)

**Дата отбора:** 2026-08-11  
**Источники:** `project-template` (hub) + референс `rosset2` + `platform/templates/`  
**Цель:** оставить в hub только переносимые между проектами механики.

---

## 1. Статус относительно hub

| Вердикт | Смысл |
|---------|--------|
| **IN_HUB** | Уже в шаблоне / добавлено в этом обновлении |
| **OPTIONAL_SPOKE** | Универсально, но тяжеловесно или редко — подключать в spoke / domain-pack |
| **SKIP** | Домен Rosseti / отраслевая специфика — не тащить в hub |

---

## 2. Rules

| Артефакт (rosset2 или hub) | Вердикт | Комментарий |
|-----------------------------|---------|-------------|
| Manifest-driven / project-core / anti-hallucination / citation / search / MCP / cursor-artifacts | **IN_HUB** | Уже были |
| `040-docs-layout` + миграции | **IN_HUB** | Усилен; layout hub сохранён |
| `045-docs-file-index` | **IN_HUB** | file-list + structure-indexer |
| `046-project-init-checklist` | **IN_HUB** | |
| Normative compliance + technical writing RU | **IN_HUB** | Универсальные рамки |
| Dev-core/tests/security/docs-sync | **IN_HUB** | |
| rosset `075-docs-file-lists` chat-start | **SKIP** | Агрессивный auto на старте чата; в hub — по запросу (045) |
| rosset `046-docx-derived-index` | **OPTIONAL_SPOKE** | Нужен поток docx; в hub — каталог `_derived/README` как задел |
| Customer letter naming / greeting / reglament style / OPE topic | **SKIP** | Домен / локальный стиль |
| `071-approved-terminology` (жёсткий список) | **OPTIONAL_SPOKE** | В hub — terminology.* манифеста |

---

## 3. Agents

| Агент | Вердикт | Комментарий |
|-------|---------|-------------|
| `@structure-indexer` | **IN_HUB** | |
| `@terminology-consistency-guard` | **IN_HUB** | |
| `@doc-consistency-guard` | **IN_HUB** | |
| `@gost-compliance-guard` | **IN_HUB** | Имя «gost» историческое; packs из манифеста |
| `@question-dedup-guard` | **IN_HUB** | |
| `@context-search-analyst` | **IN_HUB** | |
| `@meeting-terminology-normalizer` | **IN_HUB** | |
| `@meeting-demo-task-report-builder` | **IN_HUB** | |
| `@code-reviewer` | **IN_HUB** | |
| `@meeting-status-task-report-builder` | **OPTIONAL_SPOKE** | Универсален для статус-встреч с carry-over |
| `@meeting-screenshot-enrichment-builder` | **OPTIONAL_SPOKE** | OCR/привязка скринов; tool timecode уже в hub |
| `@missing-info-detector` | **OPTIONAL_SPOKE** | Полезен на старте spoke |
| `@customer-response-processor` | **OPTIONAL_SPOKE** | Нужен поток писем |
| `@domain-source-mapper`, BPMN builders, minenergo/ope/migration-* | **SKIP** | Домен |

---

## 4. Skills

| Skill | Вердикт | Комментарий |
|-------|---------|-------------|
| `project-init-pipeline` | **IN_HUB** | |
| `compliance-check-pipeline` | **IN_HUB** | |
| `context-search-report` | **IN_HUB** | |
| `meeting-transcript-pipeline` | **IN_HUB** | файл на диске |
| `mymeet-meeting-import` | **IN_HUB** | MCP mymeet.ai — primary ingest |
| `mymeet-meeting-pipeline` | **IN_HUB** | import → meeting-transcript-pipeline |
| `requirements-from-meeting` | **IN_HUB** | + STARTER/command |
| `spec-to-code-pipeline` | **IN_HUB** | |
| `plan-gate` | **IN_HUB** | Портирован из rosset2 |
| `meeting-status-transcript-pipeline` | **OPTIONAL_SPOKE** | |
| `meeting-screenshot-enrichment` | **OPTIONAL_SPOKE** | |
| `docx-to-agent-index` | **OPTIONAL_SPOKE** | |
| `mymeet-status-pipeline` (rosset status+memo) | **OPTIONAL_SPOKE** | узкий статусный Excel+мемо |
| `ope-briefing-*`, `analyst-onboarding-*`, `detailed-process-to-bpmn`, `minenergo-*`, `test-migration-*` | **SKIP** | Домен |

---

## 5. Commands

| Command | Вердикт |
|---------|---------|
| `/plan-gate` | **IN_HUB** (порт) |
| `/project-init-pipeline` | **IN_HUB** |
| `/compliance-check-pipeline` | **IN_HUB** |
| `/meeting-transcript-pipeline` | **IN_HUB** |
| `/mymeet-meeting-pipeline` | **IN_HUB** |
| `/mymeet-meeting-import` | **IN_HUB** |
| `/context-search-report` | **IN_HUB** |
| `/spec-to-code-pipeline` | **IN_HUB** |
| `/requirements-from-meeting` | **IN_HUB** |
| rosset `/ope-*`, `/mymeet-status-pipeline`, `/test-migration-*`, `/analyst-onboarding-*` | **SKIP** / optional spoke |

---

## 6. Templates (`platform/templates/`)

| Шаблон | Вердикт |
|--------|---------|
| terms, gap, compliance-report | **IN_HUB** |
| meeting-tasks (xlsx/json/yaml) | **IN_HUB** |
| meeting-transcript-part examples | **IN_HUB** |

Доменные шаблоны писем/BPMN из rosset2 — **SKIP**.

---

## 7. Рекомендация по наращиванию spoke

Порядок подключения OPTIONAL_SPOKE при необходимости:

1. `meeting-screenshot-enrichment` (+ agent) — если много PNG со таймкодами  
2. `meeting-status-transcript-pipeline` — если регулярные статус-встречи с переносом задач  
3. `docx-to-agent-index` + rule 046 — если нормативка в docx  
4. `missing-info-detector` — на онбординге аналитика  

Не смешивать OPTIONAL с SKIP: отраслевые агенты остаются вне hub.
