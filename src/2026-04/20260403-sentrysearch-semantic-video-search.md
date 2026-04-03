# SentrySearch: Semantic Search Over Video Footage
**Source**: https://github.com/ssrajadh/sentrysearch
**Date**: April 3, 2026
**Author**: ssrajadh
**Keywords**: video search, semantic search, computer vision, dashcam, ChromaDB, embeddings

## Elevator pitch
SentrySearch enables natural language queries over video files, automatically extracting and delivering trimmed clips matching the description using either Gemini embeddings or local Qwen3-VL for privacy-focused deployments.

## Takeaways
- Supports dual backends: Google Gemini Embedding API (cloud) or Qwen3-VL-Embedding (local/private)
- Videos are split into overlapping segments converted to vector embeddings for semantic matching
- Top search results are automatically extracted and saved as trimmed video files using FFmpeg
- Optional Tesla dashcam integration displays speed, location, and time metadata overlays
- Built-in still-frame detection skips redundant chunks, reducing API costs to approximately $2.84/hour with Gemini

## Synthesis
SentrySearch addresses a practical problem in video analysis: finding specific moments in long recordings without manual scrubbing. By applying semantic search to video footage, the tool enables users to describe what they are looking for in natural language and receive automatically extracted clips in return.

The dual backend design reflects thoughtful attention to deployment contexts. Cloud-based Gemini embeddings offer convenience and cost efficiency at approximately $2.84 per hour of footage, while the local Qwen3-VL-Embedding option preserves privacy for sensitive recordings such as dashcam footage containing location data or faces. This flexibility makes the tool viable for both personal and enterprise contexts.

The technical approach treats video as a collection of overlapping segments, converting each to vector embeddings that capture semantic content. ChromaDB provides the vector storage layer, enabling fast similarity search across large video collections. The automatic trimming feature delivers a completed, usable clip rather than merely a timestamp, reducing the friction between search and consumption.

Tesla dashcam integration adds domain-specific value for automotive security use cases. The optional metadata overlay combining speed, location, and timestamp data transforms raw footage into richer evidence suitable for insurance claims or incident documentation.

The still-frame detection optimization addresses cost management at scale. Video contains many redundant frames, particularly in static scenes. By identifying and skipping these duplicate chunks, the system reduces both processing time and API costs without sacrificing search coverage.

This type of semantic video search has broad applicability beyond dashcams: security camera archives, sports recordings, training footage, and any domain where video libraries accumulate faster than manual review capacity. The open-source nature of the project enables adaptation to specialized embedding models for domain-specific search quality improvements.
