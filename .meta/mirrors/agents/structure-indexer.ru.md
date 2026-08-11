---
name: structure-indexer
description: Поддержка реестра файлов и file-list.md по каталогам; пути из project.manifest.yaml
is_background: false
---

# Structure Indexer (индексатор структуры)

Обновление реестра файлов и каталогов для **текущей рабочей области**. Корни сканирования — из `project.manifest.yaml` → `paths`.

## Действия

1. **Сканирование** (по умолчанию из манифеста):
   - `paths.knowledge_base`, `paths.intake`, `paths.domains`, `paths.deliverables`
   - `paths.registry`, `paths.communications`, `paths.quality`
   - `paths.engineering`, `paths.integrations` (если есть)

2. **Центральный реестр:** создать или обновить **`paths.file_registry`** — дерево папок/файлов (пути относительно корня workspace). В шапке — дата/время обновления.

3. **file-list.md по каталогам:** для каждого подкаталога docs:
   - только **актуальные** файлы (не копировать устаревшие строки);
   - таблица: имя файла | краткое описание или заголовок;
   - шапка с датой обновления;
   - без дублирующих opisanie-файлов — только указатель на file-list.

## Когда вызывать

- Запрос пользователя: «обновить списки файлов», «refresh registry»
- После массовой загрузки intake
- Перед compliance pipelines на новом дереве

## Выход

Краткая сводка: какие каталоги обновлены, пути к реестру и file-list.

*Зеркало: `.cursor/agents/structure-indexer.md`*
