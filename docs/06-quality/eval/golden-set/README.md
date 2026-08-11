# Golden set (eval)

Структура по § 4.4 плана внедрения. Каждый сценарий — каталог с кейсами:

```
<scenario>/
  case-NN-input.*
  case-NN-expected.md
  case-NN-rubric.yaml
```

## Сценарии

| ID | Каталог | Метрика (пилот) |
|----|---------|-----------------|
| compliance | `compliance/` | source_citation_rate ≥ 95% |
| search | `search/` | source_citation_rate ≥ 90% |
| terminology | `terminology/` | user_acceptance ≥ 80% |
| meeting | `meeting/` | user_acceptance ≥ 75% |
| init | `init/` | file-registry + terms exist |

Процедура: baseline → change rule/skill → eval → compare → release.
