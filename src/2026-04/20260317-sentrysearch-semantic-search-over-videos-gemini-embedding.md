# SentrySearch: Semantic search over videos using Gemini Embedding 2 or Qwen3-VL
**Source**: https://github.com/ssrajadh/sentrysearch
**Date**: March 17, 2026
**Author**: ssrajadh
**Keywords**: semantic search, video search, Gemini Embedding 2, Qwen3-VL, ChromaDB, dashcam, Tesla, MP4

## Elevator pitch
SentrySearch enables semantic search over video content (dashcam/Tesla footage) using Gemini Embedding 2 or Qwen3-VL multimodal models with ChromaDB for vector storage.

## Takeaways
- Supports semantic search over MP4 video files using multimodal embeddings
- Integrates with Gemini Embedding 2 and Qwen3-VL vision-language models for frame understanding
- Uses ChromaDB for vector storage and retrieval of video frame embeddings
- Specifically designed for dashcam and Tesla Sentry Mode footage use cases
- Demonstrates multimodal search patterns applicable to any video corpus

## Synthesis
SentrySearch demonstrates the practical application of multimodal embeddings to the video search problem, using dashcam footage as a concrete and relatable domain. The use case is well-chosen: owners of dashcam-equipped vehicles (particularly Tesla's Sentry Mode, which continuously records surroundings) accumulate large volumes of video footage that is currently searchable only by manually scrubbing through recordings or by exact timestamp.

The system's approach — embedding video frames using multimodal models (Gemini Embedding 2 or Qwen3-VL) and storing the resulting vectors in ChromaDB — converts the temporal search problem into a vector similarity problem. Instead of "find the footage from Tuesday afternoon," users can query "find footage of a car cutting me off" or "find clips where someone approached the vehicle at night."

The choice to support both Gemini Embedding 2 and Qwen3-VL as embedding backends is pragmatic: these represent two different capability profiles. Gemini Embedding 2 offers Google's latest multimodal embedding technology with API access, while Qwen3-VL enables fully local processing for users concerned about uploading sensitive dashcam footage to external APIs. The ability to choose between cloud and local processing is meaningful for a use case that involves footage of private locations and activities.

ChromaDB's selection as the vector store reflects the project's focus on accessibility: ChromaDB is embeddable, requires no separate infrastructure to run, and is well-documented for Python developers. This keeps the deployment model simple — the entire system runs locally without requiring Kubernetes or cloud database services.

The broader pattern demonstrated here — multimodal embeddings + vector search over video — is generalizable to many domains beyond dashcam footage: surveillance footage, sports analytics, manufacturing quality control, medical imaging video, and any domain where the question "show me frames similar to this description" provides value. SentrySearch packages this pattern in a specific, useful application that also serves as a reference implementation.
