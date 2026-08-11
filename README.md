# AI Project Template (Hub) v2

**Универсальный hub-шаблон** для AI-assisted работы в Cursor.

Отчуждаемый репозиторий: копируйте каталог или клонируйте с GitHub, открывайте как отдельный workspace.

---

## Возможности

- Rules, Agents, Skills, Slash-commands
- Документационный каркас `docs/00`–`06` + `engineering/`
- Модель **Hub → Spoke**
- Встречи через **MCP mymeet.ai** (primary)
- Образец lifecycle: `platform/samples/document-lifecycle/`
- RU-зеркала в `.meta/mirrors/`

---

## Быстрый старт

```powershell
git clone https://github.com/tb2boris/ai-project-template-v2.git мой-проект
cd мой-проект
```

1. Заполните `project.manifest.yaml`
2. Задайте `MYMEET_API_KEY` (см. `.env.example`)
3. Откройте папку в Cursor → проверьте MCP `mymeet`
4. `/project-init-pipeline`
5. Встречи: `/mymeet-meeting-pipeline`

Полное описание структуры и миграций документов:  
[`platform/samples/document-lifecycle/STRUCTURE-AND-DOCUMENT-WORKFLOW.md`](platform/samples/document-lifecycle/STRUCTURE-AND-DOCUMENT-WORKFLOW.md)

---

## Skills / commands (ядро)

| Skill | Command |
|------|---------|
| `plan-gate` | `/plan-gate` |
| `project-init-pipeline` | `/project-init-pipeline` |
| `mymeet-meeting-pipeline` | `/mymeet-meeting-pipeline` |
| `mymeet-meeting-import` | `/mymeet-meeting-import` |
| `meeting-transcript-pipeline` | `/meeting-transcript-pipeline` |
| `requirements-from-meeting` | `/requirements-from-meeting` |
| `compliance-check-pipeline` | `/compliance-check-pipeline` |
| `context-search-report` | `/context-search-report` |
| `spec-to-code-pipeline` | `/spec-to-code-pipeline` |

Настройка MyMeet: [`platform/deployment/mymeet-integration.md`](platform/deployment/mymeet-integration.md)

---

## Структура

```
ai-project-template/
├── .cursor/           # rules, agents, skills, commands, mcp.json
├── platform/          # architecture, deployment, templates, samples
├── docs/              # documentation skeleton
├── engineering/
├── tools/
├── .meta/mirrors/
├── project.manifest.yaml
├── .env.example
├── CONTRIBUTING.md
└── README.md
```

---

## Обновление spoke из hub

```powershell
git remote add hub https://github.com/tb2boris/ai-project-template-v2.git
git fetch hub
git merge hub/main --allow-unrelated-histories
```

Подтягивайте преимущественно `.cursor/`, `platform/`, `tools/`.

---

## Версия

- **Hub:** v2.0.0 (clean export; MyMeet primary)
- **Модель:** Hub → Spoke
- **Встречи:** mymeet.ai MCP

См. также [CONTRIBUTING.md](CONTRIBUTING.md), [STATUS](platform/architecture/STATUS.md).
