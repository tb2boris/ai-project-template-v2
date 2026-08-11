# engineering — инженерный контур

| Каталог | Назначение |
|---------|------------|
| `integrations/` | Описание интеграций с внешними системами |
| `contracts/` | API-контракты (OpenAPI и др.) |
| `adr/` | Architecture Decision Records |
| `src/` | Исходный код (если репозиторий включает разработку) |

Связь с docs: customer-facing выжимки решений — в `docs/03-deliverables/` или доменных drafts; технические детали остаются здесь.

Пайплайн: `/spec-to-code-pipeline` (при крупных задачах сначала `/plan-gate`).
