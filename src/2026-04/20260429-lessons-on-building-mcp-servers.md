# Lessons on Building MCP Servers

**Source**: https://taoofmac.com/space/blog/2026/04/29/2341
**Date**: April 29, 2026
**Author**: Rui Carmo
**Keywords**: agents,ai,architecture,mcp,python,tools

## Elevator pitch
I’ve been building MCP servers for a while now–I wrote about the general approach last year, started out by creating umcp, and I’ve recently

## Takeaways
- Apr 29 th 2026 · 5 min read · #agents #ai #architecture #mcp #python #tools Lessons on Building MCP Servers I’ve been building MCP servers for a while now–I wrote about the general approach last year, started out by creating umcp , and I’ve recently opened up an Office server that’s been battered by enough models against enough real documents that the patterns have settled.
- I’m still not a fan of MCP , but what follows is what I’ve learned about making tool chains actually work, condensed from swearing at logs rather than reading papers.
- Disclaimer: This is a condensed version of CHAINING.md , which was itself stapled together from a bunch of notes in my Obsidian vault.
- The full version has more code examples and a techniques inventory table that Opus just _had to add, and I’ve since beaten that out of it and restored most of the original text (minus typos).
- The short version: the MCP servers I design do most of the work, while the model walks breadcrumbs.

## Synthesis
Apr 29 th 2026 · 5 min read · #agents #ai #architecture #mcp #python #tools Lessons on Building MCP Servers I’ve been building MCP servers for a while now–I wrote about the general approach last year, started out by creating umcp , and I’ve recently opened up an Office server that’s been battered by enough models against enough real documents that the patterns have settled. I’m still not a fan of MCP , but what follows is what I’ve learned about making tool chains actually work, condensed from swearing at logs rather than reading papers. Disclaimer: This is a condensed version of CHAINING.md , which was itself stapled together from a bunch of notes in my Obsidian vault. The full version has more code examples and a techniques inventory table that Opus just _had to add, and I’ve since beaten that out of it and restored most of the original text (minus typos). The short version: the MCP servers I design do most of the work, while the model walks breadcrumbs. Models don’t plan They look at the conversation, scan the tool list, and grab whatever looks more probable. If you want chains that finish somewhere sensible, the server has to make the next call blindingly obvious at every step. After a year or so, I have pared down my approach into these three things, roughly in order of how much pain they save you: A small named core verb set covering most intents Output that suggests the next call An addressing scheme that survives between calls–anchors, IDs, paths, anything but line numbers. Core verbs beat surface area The Office server exposes over 100 tools. Its get_instructions() funnels models toward eight: …start with office_help , then prefer office_read , office_inspect , office_patch , office_table , office_template , office_audit , and word_insert_at_anchor .
