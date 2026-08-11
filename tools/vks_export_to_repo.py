#!/usr/bin/env python3
"""DEPRECATED: VKS export stub. Use MyMeet MCP (/mymeet-meeting-pipeline) instead."""

from __future__ import annotations

import sys


def main() -> None:
    print(
        "vks_export_to_repo.py is DEPRECATED.\n"
        "Use MyMeet MCP: /mymeet-meeting-pipeline\n"
        "See platform/deployment/mymeet-integration.md",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
