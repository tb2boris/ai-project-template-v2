# Repository setup

This repository is **self-contained**. Clone it to use as a hub template or to bootstrap a spoke project.

## First-time publish (maintainers)

From the repository root:

```powershell
git init
git add .
git commit -m "Initial hub template platform-v0.1"
git remote add origin <URL-of-empty-remote-repo>
git push -u origin main
```

## Creating a spoke

```powershell
git clone <hub-repo-url> customer-project-x
cd customer-project-x
# Edit project.manifest.yaml, add intake to docs/01-intake/
```

See `platform/deployment/AI-contour-setup.md` for Cursor setup.

## Release tagging

After smoke tests and acceptance (see `platform/architecture/STATUS.md`):

```powershell
git tag -a platform-v1.0 -m "Hub template v1.0"
git push origin platform-v1.0
```

Intermediate draft tag after initial smoke:

```powershell
git tag -a platform-v0.1 -m "Hub template v0.1 (draft)"
git push origin platform-v0.1
```

## Updating a spoke from hub

```powershell
git remote add hub <hub-repo-url>
git fetch hub
git merge hub/main
```

Merge only shared folders when possible: `.cursor/`, `platform/`, `tools/`. Do not overwrite `project.manifest.yaml` or `docs/01-intake/` without review.

Optional project extensions: see `platform/domain-packs/README.md`.
