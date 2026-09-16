# Do LLMs Have the Memory of a Goldfish?
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-15
**Author**: ByteByteGo
**Keywords**: LLM memory, context window, persistent memory, sliding window, summarization, entity extraction, context rot, prompt caching

## Elevator pitch
LLMs don't actually remember conversations — the application around the model does. ByteByteGo's deep dive into LLM memory explains the distinction between trained memory (model weights), working memory (the context window), and persistent application memory (external storage). The piece walks through how chat applications reconstruct conversation history, why long conversations become expensive, what happens when the context window fills up, and the techniques — sliding windows, summarization, structured entity extraction — that extend memory in production systems.

## Takeaways
- LLMs have no personal or persistent memory of previous interactions; the surrounding application maintains and re-injects conversation history
- The context window is a "working-memory budget" that must fit system instructions, tool definitions, conversation history, retrieved documents, and output space
- Long conversations become increasingly expensive: across 10 requests, ~55K tokens of input are processed despite the visible conversation containing only ~10K tokens
- "Context rot" degrades recall as the context window fills — more information makes it harder for the model to differentiate important facts from noise
- Prompt caching is an optimization, not a memory architecture — it reduces cost for repeated prefixes but doesn't give the model unlimited memory
- When the context window fills, applications may remove oldest messages, use a rolling window, replace old material with summaries, or trigger server-side compaction
- Sliding-window memory keeps only the most recent N turns — simple and fast but loses old facts
- Conversation summarization compresses older messages into a summary — preserves direction but is lossy and can distort meaning over repeated summarization
- Structured entity extraction stores specific facts in structured fields (e.g., preferred_language, database, framework) — more reliable than searching through summaries
- The key insight: "the model doesn't possess persistent memory; it receives persistent information from another system"

## Synthesis
ByteByteGo's article is a clear, technically precise explanation of a topic that confuses many developers: how LLMs "remember" things. The central distinction — that the model itself has no persistent memory and that the surrounding application is doing the remembering — is the foundation for understanding every memory technique that follows.

The piece is particularly strong in explaining the economics of long conversations. The compounding cost model (request 1 processes ~1K tokens, request 10 processes ~10K tokens, totaling ~55K across 10 requests) makes it obvious why context management is a production concern, not just an academic one. The "context rot" problem — where more information in the context window degrades the model's ability to distinguish important facts — is an important counterargument to the "just use a bigger context window" approach.

The memory techniques section is practical and well-organized. Sliding-window memory is the simplest approach but loses old facts. Conversation summarization preserves the conversation's direction but is lossy and can distort meaning through repeated summarization ("like repeatedly copying a photocopy"). Structured entity extraction — storing facts in structured fields rather than prose — is presented as the most reliable for exact project state, though it requires more engineering effort.

The article also covers server-managed conversation state, prompt caching (an optimization, not memory), and compaction mechanisms. The overarching message is that memory in LLM applications is an engineering problem solved by the application layer, not a property of the model itself.