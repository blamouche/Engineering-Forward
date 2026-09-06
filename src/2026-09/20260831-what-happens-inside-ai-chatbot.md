# What Happens Inside an AI Chatbot Between Enter and the First Word?
**Source**: https://blog.bytebytego.com/p/what-happens-inside-an-ai-chatbot
**Date**: 2026-08-31
**Author**: ByteByteGo
**Keywords**: LLM, inference pipeline, tokenization, prefill, decode, KV cache, batching, safety checks, streaming, guardrails

## Elevator pitch
ByteByteGo traces the ~dozen distinct stages a single message passes through in a typical LLM between pressing Enter and seeing the first word — from system prompt assembly and safety checks through tokenization, shared batching with other users, prefill and decode, KV caching, streaming, and tool execution — revealing that the model never sees your message as typed, has no memory of the conversation, and shares a machine with strangers.

## Takeaways
- The model never receives the message as typed — a document is assembled around it (system prompt, conversation history, safety instructions) before the request is sent
- The model has no memory of the conversation; the history on screen is rebuilt from scratch every turn from the client side
- The model shares a machine with strangers — the batch group it lands in can affect the reply due to continuous batching and resource contention
- Once a word has been sent (streamed), the model cannot take it back — there's no undo for tokens already emitted to the client
- Key stages include: input assembly, safety checks on input, tokenization, shared/batched inference, prefill (processing the prompt), decode (generating tokens one at a time), KV cache reuse, streaming with guardrails, and tool execution

## Synthesis
ByteByteGo provides a detailed walkthrough of the LLM inference pipeline, from the moment a user presses Enter to the first word appearing on screen. The central insight is that the pause between Enter and the first token is not dead time — it's a complex sequence of processing stages, and the apparent speed of subsequent tokens is a result of work done during that pause.

The first stage is input assembly. The sentence typed into the chat box is not what reaches the model. What reaches the model is a document assembled around that sentence, containing a system prompt (instructions written by the LLM provider), the conversation history (rebuilt from scratch each turn — the model has no memory), and safety instructions. The model processes this assembled document, not the raw user input.

Safety checks run on the input before it reaches the model. The model itself is shared across multiple conversations through continuous batching — the group of requests it's batched with can affect the response. The tokenization step converts text into token IDs. Then the prefill step processes the entire prompt to build the KV cache, and the decode step generates tokens one at a time. KV caching allows reuse of computations from previous tokens in the same conversation, which is why follow-up questions can be faster than the first. Streaming sends tokens to the client as they're generated, with guardrails checking output in real time. Tool execution — when the model calls external functions — adds another round trip. The article emphasizes that once a token is streamed, it cannot be taken back, making output guardrails critical for safety.