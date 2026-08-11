# Интеграция mymeet.ai (MCP) — основной контур встреч

**Статус:** primary ingest для совещаний в hub v2  
**Сервис:** [mymeet.ai](https://app.mymeet.ai)  
**MCP endpoint:** `https://mcp.mymeet.ai/mcp`

## 1. Настройка

1. Получить API key: https://app.mymeet.ai/settings  
2. Задать переменную окружения (не коммитить):

```powershell
# пример для текущей сессии
$env:MYMEET_API_KEY = "your-api-key-here"
```

Постоянно: системные/пользовательские env vars или профиль shell. Образец: `.env.example`.

3. В репозитории уже есть `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "mymeet": {
      "url": "https://mcp.mymeet.ai/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MYMEET_API_KEY}"
      }
    }
  }
}
```

4. Перезагрузить Cursor → Customize → MCP → `mymeet` connected.

## 2. Поток

1. Запись/транскрипт готовится в mymeet.ai до статуса `processed`.
2. В Cursor: `/mymeet-meeting-pipeline` (или только `/mymeet-meeting-import`).
3. Артефакты:
   - raw: `docs/05-communications/_imports/mymeet/<id>.json`
   - markdown: `docs/05-communications/transcripts/<YYYY-MM-DD>_<title>.md`
4. Downstream: нормализация терминов + Excel задач (`meeting-transcript-pipeline`).

## 3. Манифест

`project.manifest.yaml` → `integrations.mymeet`:

```yaml
integrations:
  mymeet:
    enabled: true
    mcp_server: mymeet
    export_paths:
      imports: docs/05-communications/_imports/mymeet
      transcripts: docs/05-communications/transcripts
      media: docs/05-communications/media
      meetings_registry: docs/04-registry/meetings
```

## 4. Безопасность

- Не класть API key в git, screenshots чата, README.
- Rule **025-mcp-and-security-boundary** — не отдавать PII во внешние MCP без политики проекта.
- Raw JSON импортов может содержать персональные данные — ограничивайте доступ к `_imports/`.

## 5. Legacy VKS

VKS Processing Service **не является** основным путём в этом шаблоне. Файлы `vks-integration.md` / `tools/vks_export_to_repo.py` сохранены только как deprecated optional stub для spoke, где VKS ещё используется. Новые проекты настраивают **MyMeet**.
