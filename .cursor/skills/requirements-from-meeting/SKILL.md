---
name: requirements-from-meeting
description: Linked segments from meeting → requirements diff → doc consistency check
disable-model-invocation: true
---

# Requirements from meeting

Extract new and refined requirements from meeting materials and propose spec or domain draft diff.

## When to use

- After VKS linked-segments export
- User asks to update requirements from meeting decisions

## Steps

1. Read linked-segments + transcript from `paths.communications`.
2. Identify requirement-level decisions (scope, dates, constraints).
3. Draft diff against `references.primary_spec` or domain draft in `docs/02-domains/`.
4. Invoke `@doc-consistency-guard` on proposed changes.
5. Output: diff markdown + gap list if irreconcilable.

Human approver: BA / PM before merging into deliverables.
