# Perplexity Is Open-Sourcing Bumblebee
**Source**: https://www.perplexity.ai/hub/blog/perplexity-is-open-sourcing-bumblebee
**Date**: May 22, 2026
**Author**: Perplexity Team
**Keywords**: Perplexity, Bumblebee, open source, supply chain security, developer security, scanner, Go, endpoint security

## Elevator pitch
Perplexity open-sources Bumblebee, a read-only supply-chain scanner for developer endpoints that checks on-disk package, extension, and AI tool metadata against known compromises without ever executing install scripts.

## Takeaways
- Bumblebee is a zero-dependency Go binary that performs read-only scans of developer machines, covering package managers (npm, PyPI, Go, RubyGems, Composer), MCP configs, editor extensions, and browser extensions.
- The tool deliberately never runs npm, pip, or any package manager to avoid triggering postinstall scripts that could execute compromised code during scanning.
- It was built internally at Perplexity to protect developer systems behind its search product, Comet browser, and Computer agent, and maps to recent supply-chain campaigns including the Mini Shai-Hulud series.
- Three scan profiles (baseline, project, deep) support routine inventory and active incident response, with structured NDJSON output and configurable exposure catalogs.
- Licensed under Apache 2.0, with 2,300+ GitHub stars and maintained threat intel catalogs for known campaigns.

## Synthesis
Perplexity's release of Bumblebee addresses a specific security blind spot that has grown more dangerous as AI development toolchains expand: the gap between traditional vulnerability scanners and the actual state of developer machines. SBOMs and EDR products cover build artifacts and process monitoring, but neither checks the scattered metadata across package lockfiles, editor extension manifests, MCP config files, and browser extensions that live on every developer's laptop.

Bumblebee is intentionally minimal. Written in Go with zero non-standard library dependencies, it's a one-shot scanner that reads on-disk metadata and exits — no daemon, no network monitoring, no process inspection. The read-only design is deliberate: npm packages can carry postinstall scripts that execute automatically on install, so a scanner that invokes npm to check exposure has already triggered the attack it was looking for. Bumblebee reads lockfiles and installed package metadata directly.

The ecosystem coverage maps to real threats. Bumblebee covers the package managers targeted in the Mini Shai-Hulud supply-chain campaign series (npm, PyPI, RubyGems, Go modules, Composer), the editor extensions used by AI developers (VS Code, Cursor, Windsurf, VSCodium), browser extensions (Chrome, Comet, Edge, Brave, Arc, Firefox), and MCP config files from multiple hosts. This last category is increasingly important as MCP servers become vectors for tool poisoning — compromising a developer's MCP config can give an attacker access to file systems, APIs, and databases.

Perplexity's internal workflow provides a practical model for how to use the tool. When a threat signal arrives from public disclosures or intel feeds, Perplexity Computer drafts a catalog update as a GitHub PR with ecosystem, package name, and version. A human reviews and merges. Bumblebee then scans endpoints against the updated catalog, and findings go to the security team. This semi-automated pipeline turns disclosure-to-detection from hours to minutes.

The tool's confidence scoring (high/medium/low) adds nuance often missing from security scanners. High confidence means exact identity and version from canonical metadata; low means only a config path reference. This helps security teams triage findings without chasing false positives from ambiguous matches. The included threat_intel/ directory with maintained exposure catalogs makes Bumblebee useful out of the box, without requiring teams to build their own catalogs from scratch.
