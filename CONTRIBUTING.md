# Contributing to AI Project Template (Hub v2)

## Репозиторий

- GitHub: `https://github.com/tb2boris/ai-project-template-v2`
- Ветка по умолчанию: `main`
- Рабочие изменения — через feature-ветки и Pull Request

## Ветки

| Ветка | Назначение |
|-------|------------|
| `main` | Стабильный hub |
| `feature/<topic>` | Разработка |
| `docs/<topic>` | Только документация |

## Что менять в hub

| Разрешено в PR в hub | Лучше в spoke / domain-pack |
|----------------------|-----------------------------|
| `.cursor/` core rules/agents/skills/commands | Отраслевые агенты, письма заказчику |
| `platform/`, `tools/` | Контент `docs/01-intake` заказчика |
| Образцы в `platform/samples/` | Локальные MCP кроме mymeet |
| Универсальные правки MyMeet-контура | Секреты, API keys |

## Локальный цикл

1. Fork или clone
2. `git checkout -b feature/...`
3. Правки + обновление каталогов (`SKILLS_CATALOG`, `AGENTS_CATALOG`, `RULES_REGISTRY` при необходимости)
4. RU-зеркало в `.meta/mirrors/` для изменённых EN-артефактов
5. PR → review → merge

## Секреты

- Никогда не коммитить `MYMEET_API_KEY` и `.env`
- В PR проверяйте `.cursor/mcp.json` — только `${env:...}` placeholders

## Документы

- Lifecycle: `platform/samples/document-lifecycle/`
- MyMeet: `platform/deployment/mymeet-integration.md`
