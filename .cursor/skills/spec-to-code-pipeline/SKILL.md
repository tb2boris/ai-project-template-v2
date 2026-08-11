---
name: spec-to-code-pipeline
description: Spec fragment → plan → implement → test → @code-reviewer
disable-model-invocation: true
---

# Spec to code pipeline

Engineering flow from specification to reviewed PR suggestion.

## When to use

- Smart-route: implement fragment per spec / OpenAPI
- Stage 4 dev contour

## Steps

```
- [ ] 0. Read spec section + engineering/contracts/
- [ ] 1. Plan (small scope) — files to touch
- [ ] 2. Implement + tests (dev-tests, dev-security rules)
- [ ] 3. Update contract if API changed (dev-docs-sync)
- [ ] 4. @code-reviewer read-only pass
- [ ] 5. Present diff summary — human merge
```

## Limits

- No merge/push/deploy (dev-core, R-025)
- Cite spec sections for behavioral claims

Human approver: Tech lead.

## User guide

- [.cursor/STARTER_PROMPT_SPEC_TO_CODE.md](../../STARTER_PROMPT_SPEC_TO_CODE.md) — user guide (RU)
