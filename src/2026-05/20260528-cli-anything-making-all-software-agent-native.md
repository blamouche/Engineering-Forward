# CLI-Anything: Making All Software Agent-Native
**Source**: https://github.com/HKUDS/CLI-Anything
**Date**: 2026-05-28
**Author**: HKUDS Lab (Hong Kong University)
**Keywords**: cli-anything, agent-native, cli-harness, software-automation, agent-tools, llm-agents

## Elevator pitch
CLI-Anything from the HKUDS lab generates full CLI harnesses for any software, turning GUI-only apps like Blender, GIMP, and OBS into agent-controllable tools — one command analyzes source code, architects a CLI, implements it with tests, and publishes it to PATH, with a growing registry of 50+ ready-made CLIs.

## Takeaways
- CLI-Anything automatically generates CLI harnesses for GUI-only software, making the entire software ecosystem accessible to AI agents overnight
- One command analyzes the target app's source code, architects a CLI, implements it with tests, and publishes it to PATH — no manual wrapper writing required
- Ships with a growing registry of 50+ ready-made CLIs covering GIMP, Blender, LibreOffice, OBS, Obsidian, Kdenlive, QGIS, and more
- The CLI Hub (`pip install cli-anything-hub`) lets users browse, install, and manage community-built CLIs, with instant updates when new harnesses are merged
- The thesis is simple: if CLI is the universal interface both humans and LLMs already speak, wrapping every piece of software in a CLI makes the entire software ecosystem agent-accessible
- Community-driven: contributors can build new CLI harnesses, submit wishlist requests for specific software, and join as community contributors once reviewed
- Includes a tech report on arXiv (2606.03854) documenting the approach, architecture, and evaluation

## Synthesis
CLI-Anything addresses a fundamental gap in the AI agent ecosystem: agents can write code, search the web, and manage files, but ask one to edit a Blender scene, export a MuseScore sheet, or automate Rekordbox, and it hits a wall. The software doesn't speak agent. CLI-Anything from the HKUDS lab at Hong Kong University fixes this by generating full CLI harnesses for any software, turning GUI-only applications into agent-controllable tools.

The approach is elegantly simple. One command analyzes the target application's source code, architects a CLI interface, implements it with tests, and publishes it to PATH. The project ships with a growing registry of 50+ ready-made CLIs covering GIMP, Blender, LibreOffice, OBS, Obsidian, Kdenlive, QGIS, and more — all installable via the CLI Hub package manager (`pip install cli-anything-hub`). The hub updates instantly when new community-built harnesses are merged, creating a living registry of agent-accessible software.

The thesis underlying the project is that CLI is the universal interface that both humans and LLMs already speak. If that's the case, wrapping every piece of software in a CLI makes the entire software ecosystem agent-accessible overnight — not through new protocols or frameworks, but through the oldest interface in computing. The demos are compelling: agents producing CAD builds, 3D scenes, diagrams, gameplay, subtitles, and more using generated CLIs. The community is actively contributing new harnesses, with recent additions including a Joplin CLI with 134-test validation, a Rekordbox CLI with guarded SQLCipher write paths, and an ArcGIS Pro MCP bridge for live agent-driven cartography. The project also includes a tech report on arXiv documenting the generation approach, testing methodology (100% passing, 46% coverage), and evaluation framework.