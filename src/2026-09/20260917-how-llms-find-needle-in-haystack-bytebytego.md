# How LLMs Can Find a Needle in a Haystack
**Source**: ByteByteGo (bytebytego@substack.com) — https://blog.bytebytego.com/p/how-llms-can-find-a-needle-in-a-haystack
**Date**: 2026-09-16
**Author**: ByteByteGo
**Keywords**: RAG, retrieval-augmented generation, embeddings, vector search, HNSW, IVF, chunking, metadata filtering, reranking, hybrid search

## Elevator pitch
A comprehensive technical walkthrough of how LLMs retrieve relevant information from large document collections, covering the entire RAG pipeline from chunking and embeddings to vector indexing, metadata filtering, and reranking.

## Takeaways
- **Chunking is a precision-context tradeoff**: Small chunks focus tightly on the question but may drop exceptions; large chunks preserve context but include irrelevant material. Section headings and overlap between neighboring chunks help retain meaning.
- **Embeddings map meaning, not keywords**: An embedding model converts passages into vectors where related meanings occupy nearby positions, enabling semantic search even when wording differs ("cancelled flight" vs "involuntary travel disruption").
- **Index choice depends on scale, not just size**: Flat search (O(n)) gives exact results but scales linearly. IVF groups vectors into clusters with nprobe controlling recall. HNSW builds a navigable graph with layers, trading memory for speed. No single choice is universally best.
- **Similarity ≠ correctness**: A cosine score of 0.85 doesn't mean 85% answer probability. Metadata filtering (region, date, version) is essential to ensure retrieved passages are actually eligible evidence, not just semantically close.
- **Updates and versioning are a systems problem**: When policies change, both old and new chunks may be searchable. Version identifiers, explicit active-version rules, and coordinated transitions prevent contradictory evidence from reaching the LLM.

## Synthesis
The article frames the retrieval problem through a concrete scenario: an employee stranded at an airport asks whether they can expense a hotel after a cancelled flight. The answer exists somewhere in thousands of company documents, but the question uses different language than the policy, other documents discuss hotels for different countries, and an older policy may contain outdated limits. This framing illustrates why retrieval—not generation—is the bottleneck in most RAG applications.

The pipeline begins with chunking, which breaks documents into searchable units. The article emphasizes that chunk size is a balance between precision and context: a small chunk might capture the reimbursement rule but miss the exception ("This applies only when accommodation is not provided by the airline"). Section headings and limited overlap between neighboring chunks help preserve complete ideas.

Embeddings then convert chunks and queries into vectors in the same space, allowing semantic matching even when wording differs. The article carefully explains that individual vector dimensions don't have simple labels like "hotel" or "flight"—meaning emerges from patterns across the full vector. The choice of distance metric (cosine, Euclidean, dot product) should follow the embedding model's design, not popularity.

For scale, the article compares three indexing approaches. Flat search compares every vector (O(n)), producing exact results but growing linearly with collection size. IVF organizes vectors into clusters, trading exactness for speed by searching only promising groups. HNSW builds a layered graph where search starts at sparse upper layers and descends to the detailed bottom, like navigating a road network from highways to local streets. The article notes that HNSW is a strong candidate when memory permits but is not automatically best for every workload.

The most important insight is that similarity alone cannot establish whether a passage is suitable evidence. Metadata filtering—by region, document type, effective date, version—defines which documents are eligible. Pre-filtering identifies eligible records before similarity ranking; post-filtering retrieves candidates first then removes ineligible ones. Graph search adds complexity: disallowed points may still provide useful navigation routes, so blocking them during traversal can make eligible neighbors harder to reach.

The article concludes with versioning and updates. When a reimbursement limit changes from ₹5,000 to ₹7,000, both versions must not remain eligible simultaneously. A sensible design prepares the new version's chunks, verifies availability, then switches which version is active. Older versions stay accessible for historical queries. Changing the embedding model itself requires similar planning but at much larger scale—every document needs new embeddings.

The final step is reranking and hybrid search. A reranker compares passage text with the question to select the most useful few from 30+ candidates. Hybrid search combines semantic retrieval with keyword matching, preserving exact matches for policy identifiers and unusual technical terms. The application must also handle unanswered questions gracefully—every collection has nearest vectors, even when none contain useful information.