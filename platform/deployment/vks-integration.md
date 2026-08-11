# VKS integration (DEPRECATED)

**Status:** deprecated in hub v2. **Use MyMeet MCP instead:** [mymeet-integration.md](./mymeet-integration.md).

This file and `tools/vks_export_to_repo.py` remain only for legacy spokes that still call a private VKS Processing Service. New projects must set `integrations.mymeet.enabled: true` and keep `integrations.vks.enabled: false`.

## Until removed

- Prefer `/mymeet-meeting-pipeline` for all meeting ingest.
- Manual file drop into `docs/05-communications/transcripts/` remains valid without VKS.
