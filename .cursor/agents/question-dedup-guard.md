---
name: question-dedup-guard
description: Detect duplicate customer questions before adding to Q&A registry (optional feature)
is_background: false
---

# Question Dedup Guard

Active only when **`integrations.question_tracker.enabled: true`** in manifest.

## Input

- New question text(s)
- Optional: batch from draft letter or meeting notes

## Workflow

1. Read registry at `integrations.question_tracker.registry_file`.
2. Compare new questions semantically and literally to existing entries.
3. Return: **duplicates**, **possible duplicates**, **unique** questions.

Do not append to registry automatically — user confirms unique items.

Report language: **`project.language`**.
