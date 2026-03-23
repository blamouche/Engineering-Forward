# Hocuspocus Collaboration Overview
**Source**: https://tiptap.dev/docs/hocuspocus/getting-started/overview
**Date**: March 23, 2026
**Author**: Unknown
**Keywords**: Hocuspocus, Tiptap, Y.js, collaboration, CRDT, WebSocket

## Elevator pitch
Hocuspocus is Tiptap’s collaboration stack built on Y.js, providing conflict‑free real‑time sync with WebSocket infrastructure and offline‑first support.

## Takeaways
- Hocuspocus is a collaboration toolkit built on Y.js CRDTs.
- It supports real‑time sync and offline‑first workflows.
- The server provides a WebSocket backend to scale collaboration.
- Integrations cover common editors (Tiptap, ProseMirror, Monaco, etc.).
- The platform is designed for conflict‑free merges and high‑scale use.

## Synthesis
The Hocuspocus overview introduces a collaboration stack designed to bring real‑time multi‑user editing to applications. Built on Y.js, it inherits the properties of CRDTs: conflict‑free merges, order‑independent updates, and consistent state across clients. This foundation allows developers to add collaboration without designing custom merge logic or dealing with complex conflict resolution.

Hocuspocus positions itself as more than a library. It includes a server component that provides a WebSocket backend for syncing changes between clients. This makes it suitable for production collaboration systems that need a centralized service to relay updates. The server is presented as scalable, with features like Redis support and integrations that allow developers to sync broader application state beyond just text editing.

The overview also emphasizes offline‑first behavior. Because Y.js can merge changes regardless of update order, applications can accept edits while offline and reconcile them later. This is a practical advantage for collaborative products used in environments with intermittent connectivity and aligns with the goal of providing a seamless user experience even when network conditions vary.

Integration is another selling point. Hocuspocus supports a wide range of editor frameworks and can embed into existing application architectures. The toolkit is positioned as a practical path to collaboration rather than a theoretical CRDT demo. Developers can combine it with their existing stack while relying on Y.js for the heavy‑lifting of synchronization.

In short, Hocuspocus is presented as a production‑oriented collaboration stack: a CRDT‑backed sync engine, a WebSocket server for scaling, and editor integrations that let teams ship collaborative features with less infrastructure work. It complements the broader trend of building rich, real‑time workflows without reinventing synchronization logic.
