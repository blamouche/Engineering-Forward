# Obsidian Work Assistant

Single entry point containing all instructions for Obsidian prompts.

## Usage
```bash
/agents <prompt> [arguments]
```

## Registry
- `add-tags`

## Obsidian Work Assistant Routing
1. Verify that `<prompt>` exists in the registry.
2. Apply only the matching instruction section.
3. Use the paths/files defined directly in each instruction.
4. If the prompt is unknown, return the registry list.

## Prompt: add-tags
### Usage
```bash
/add-tags <X>
```

### Instructions
1. Identify the target Obsidian vault (current directory unless the user states otherwise).
2. List Markdown notes (`.md`) and select the `X` most recent notes (sorted by modification date descending), excluding any path inside folders whose names start with `.`.
3. For each selected note, analyze content and propose relevant tags in Obsidian format:
   - maximum 5 tags total per note,
   - tags must be in English,
   - lowercase tags,
   - `kebab-case` format (example: `project-management`),
   - no duplicates.
4. Insert or update the YAML frontmatter header with the `tags` key:
```yaml
---
tags:
  - tag-1
  - tag-2
---
```
5. If a note already contains tags, keep existing tags and add only missing relevant tags without exceeding 5 tags total.
6. Modify only the frontmatter section (do not change note body content).
7. Provide a final note-by-note summary: added tags, preserved tags, or skipped note (if no relevant tag is found).

### Notes
- `X` must be a strictly positive integer.
- If the vault contains fewer than `X` notes, process all available notes.
- Always normalize inferred tags to English, even when note content is in another language.
- Never scan hidden folders (names starting with `.`), including nested hidden paths.
- Never modify non-note files (technical files, prompt files, databases, configuration files, binaries, or any file that is not a Markdown note).
- Never create generic low-signal tags (`note`, `todo`, `misc`, etc.) unless explicitly requested.
