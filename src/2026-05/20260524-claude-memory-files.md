# Anthropic plans Claude memory update with new Memory Files
**Source**: https://www.testingcatalog.com/anthropic-plans-claude-memory-update-with-new-memory-files/
**Date**: May 24, 2026
**Author**: Alexey Shabanov
**Keywords**: Anthropic, Claude, memory, Memory Files, Dreams, user context, persistent memory, Claude Conway

## Elevator pitch
Anthropic is testing a dual-mode memory system for Claude that replaces the current single-note summary with structured "Memory Files" organized by topic, potentially paired with a "Dreams" consolidation feature that asynchronously deduplicates and reconciles memory across sessions.

## Takeaways
- The new "Memory Files" system distributes user information across multiple structured documents organized by topic, project, or context, rather than a single summarized note.
- This architecture mirrors what always-on agentic solutions like OpenClaw and Hermes already use, allowing far larger and more durable user records without overwhelming the context window.
- "Dreams" is a related feature that runs scheduled, asynchronous passes over memory files to merge duplicates, replace stale entries, resolve contradictions, and surface missed patterns.
- Dreams is currently in limited beta on the developer platform, scoped to Opus 4.7 and Sonnet 4.6, with no confirmed timeline for consumer release.
- The Memory Files feature may be preparation for the rumored Claude Conway always-on agent, expected to debut soon.

## Synthesis
Anthropic is preparing a significant architectural change to how Claude maintains context across sessions. The current system condenses everything Claude learns about a user into a single summarized note — functional but limited in both capacity and organization. The forthcoming "Memory Files" approach would instead distribute this information across multiple structured documents, organized by topic, project, or context. This is likely an evolution of previously discovered "Knowledge Bases" work.

The file-based architecture represents a meaningful shift in capability. Instead of a single rolling summary that must fit within tight context window constraints, Claude could maintain a personal wiki of user information, selectively loading only the relevant files for a given conversation. This mirrors the approach that always-on agentic systems like OpenClaw and Hermes have already adopted, where filesystem-style memory enables persistent operation across sessions without context window bloat.

The companion feature, "Dreams," adds a layer of automated memory maintenance. Running as a scheduled, asynchronous process (Anthropic explicitly compares it to REM sleep consolidation), Dreams merges duplicate entries, replaces stale information, resolves contradictions, and surfaces patterns the model missed during live interaction. The original memory store remains untouched while a reorganized version is produced for review, preserving user control over what's retained.

The timing is suggestive. Claude Conway, an always-on agent rumored to be in development, would benefit enormously from a robust memory architecture. Memory Files may be foundational infrastructure for Conway, enabling the persistent context an always-on agent requires. Dreams remains in limited beta on the developer platform, and Memory Files has no firm timeline, but the pieces are coming together for a more stateful, persistent Claude experience.

This positions Anthropic more competitively against rivals building persistent-memory architectures while maintaining the company's stated emphasis on user control. Users can browse and edit their Memory Files anytime, and Dreams' non-destructive consolidation process keeps users in the loop. It's a thoughtful approach to the memory problem that balances capability with transparency — a different philosophy than the opaque "the model just remembers" approach some competitors take.
