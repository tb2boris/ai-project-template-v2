# Hub template status

**Version:** v2.0.0  
**Last updated:** 2026-08-11  
**Repository:** `ai-project-template-v2` (clean export)

## Summary

| Item | Status |
|------|--------|
| Core rules, agents, skills, commands | Ready |
| MyMeet MCP meeting ingest | Primary — ready |
| VKS integration | Deprecated stub only |
| Documentation structure (`docs/`) | Ready + lifecycle sample |
| Golden set eval cases | Not yet |
| Sign-off platform-v1.0 naming | Pending (hub marketed as v2 export) |

## Meeting path

`MYMEET_API_KEY` + `.cursor/mcp.json` → `/mymeet-meeting-pipeline` → `docs/05-communications/` → Excel in `docs/04-registry/meetings/`.

## Architecture

- [hub-vs-spoke.md](./hub-vs-spoke.md)
- [mymeet-integration.md](../deployment/mymeet-integration.md)
- [document-lifecycle](../samples/document-lifecycle/)
