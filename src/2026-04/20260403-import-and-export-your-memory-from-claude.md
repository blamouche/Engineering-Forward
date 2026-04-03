# Import and Export Your Memory from Claude

**Source**: https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
**Date**: Unknown
**Author**: Anthropic Support
**Keywords**: Claude, memory, import, export, AI portability, personal context, memory management

## Elevator pitch
Claude now supports importing and exporting your personal memory, enabling portability between AI providers and giving users explicit control over the context their AI assistants carry about them.

## Takeaways
- Claude supports memory import from other AI providers using a standardized prompt to extract and transfer stored memories and personal context
- Users can export their Claude memory verbatim from Settings > Capabilities, enabling backup and portability to other AI services
- The import flow processes pasted memory exports and stores them as individual editable memory entries, reviewable within 24 hours
- Claude's memory is intentionally focused on work-related topics—personal details unrelated to work may not be retained automatically but can be added manually
- This represents a significant step toward AI memory portability, reducing switching costs between AI providers

## Synthesis
Memory portability has been a missing piece in the AI assistant ecosystem. Until recently, every AI assistant's accumulated knowledge about you—your preferences, work context, communication style, ongoing projects—was locked into that specific service. Switching providers meant starting from scratch. Claude's new import/export functionality begins to address this problem.

The export mechanism is elegantly simple: a carefully crafted prompt that asks your current AI provider to output all stored memories in a standardized format. The prompt is designed to capture everything—instructions you've given about tone and format, personal details, ongoing projects, tool preferences, and corrections you've made to the AI's behavior. The output is a single code block you can copy, save as a Markdown file, and import elsewhere.

The import flow on Claude's end processes this pasted text and converts it into individual memory entries that can be reviewed, edited, or deleted. The 24-hour processing window suggests some backend processing happens asynchronously rather than immediately.

The design choice to focus Claude's memory on work-related topics reflects a product philosophy: Claude is positioned primarily as a professional collaborator rather than a general personal assistant. Personal details unrelated to work may not be retained by default, though users can manually add specific items through the Settings interface.

The portability story matters beyond just switching providers. It creates a backup mechanism for users worried about service disruptions, enables users to audit what their AI assistant knows about them, and establishes a norm of memory transparency. If you can read exactly what Claude remembers about you, you can correct errors, remove outdated information, and understand why it behaves the way it does.

For enterprise users and teams, this also raises governance questions: what personal context should AI assistants carry, who can review it, and how should it be managed when employees leave an organization? The ability to export and audit memory is the foundation for answering those questions.

The implicit competitive dynamic is interesting: Claude providing a standard prompt to extract memories from other AI providers is a direct invitation to switch. But it also establishes an industry norm—if users expect memory portability, all providers will eventually need to support it. That's a net positive for users regardless of which provider they choose.
