# Today's harness is Tomorrow's Prompt
**Source**: https://tanay.co.in/blog/todays-harness-is-tomorrows-prompt
**Date**: 2026-04-25T18:49:24.591Z
**Author**: Tanay Sai
**Keywords**: today's, harness, tomorrow's, prompt

## Elevator pitch
In 2023, I spent two weeks wiring up a RAG pipeline so a sales team could ask questions about a folder of PDFs.

## Takeaways
- In 2023, I spent two weeks wiring up a RAG pipeline so a sales team could ask questions about a folder of PDFs.
- A harness is the scaffolding you build around a model to make it do something it can't quite do on its own.
- In the 2023 RAG pipeline, the harness was everything between the PDF and the answer: the chunker splitting documents because the context window was…
- Harnesses have a short shelf life, and it's getting shorter.
- If you're building on AI, the question isn't how clever your harness is.

## Synthesis
In 2023, I spent two weeks wiring up a RAG pipeline so a sales team could ask questions about a folder of PDFs. Chunking, embeddings, a vector store, a reranker. Today, a user drops twenty 100-page PDFs into a 1M-token context window and the model handles it.

A harness is the scaffolding you build around a model to make it do something it can't quite do on its own. More than a wrapper; something that measurably lifts what the model can do.

In the 2023 RAG pipeline, the harness was everything between the PDF and the answer: the chunker splitting documents because the context window was too small, the embedding model and vector store because the LLM couldn't search, the reranker because retrieval was noisy. Parsers exist because the output is slightly wrong. Vector stores exist because the context window is too small. Agent frameworks exist because the model can't plan. Every harness is a workaround for a model limitation, dressed up as architecture.

Harnesses have a short shelf life, and it's getting shorter. What took an engineering team a quarter last year is a flag on Gemini call today. What needs a multi-agent framework today is a single call next year.

If you're building on AI, the question isn't how clever your harness is. It's how long until the model eats it.

Chat with your PDF. The old version: chunk the doc, pick an embedding model, stand up Pinecone or Milvus, write retrieval logic, tune the reranker, hope the chunks contained the answer. The new version: a file upload and a question. Long context didn't improve RAG so much as make a lot of RAG unnecessary.

Structured output. I used to write prompts that begged the model to return JSON. "You are a JSON generating machine. Output only JSON. No markdown. No prose." Then a regex parser. Then a retry loop for trailing commas and stray backticks. It's a parameter on any LLM API call now, and it works.

Reading an image. The old pipeline ran a receipt through on OCR like Tesseract, got back a smeared wall of characters, and asked an LLM to guess at the line items. It failed on anything curved, rotated, or handwritten. Vision models don't need the harness with OCR today. They just work!
