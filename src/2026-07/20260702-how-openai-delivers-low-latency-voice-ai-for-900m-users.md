# How OpenAI Delivers Low-Latency Voice AI for 900M Users
**Source**: https://blog.bytebytego.com/p/how-openai-delivers-low-latency-voice
**Date**: 2026-07-01
**Author**: ByteByteGo (Alex Xu)
**Keywords**: WebRTC, OpenAI, voice AI, low latency, infrastructure, Kubernetes, relay, transceiver, SFU

## Elevator pitch
OpenAI's voice AI architecture splits WebRTC into a stateless relay and stateful transceiver, using the ICE ufrag as a routing key to serve 900M weekly users with minimal latency on Kubernetes.

## Takeaways
- WebRTC was designed for stable servers, but Kubernetes treats compute as disposable — this mismatch creates port exhaustion and state stickiness problems at scale
- OpenAI splits the stack into a stateless relay (packet routing at the edge) and a stateful transceiver (ICE/DTLS/SRTP state management), avoiding the need for an SFU
- The ICE ufrag field is repurposed as a routing key, allowing the relay to direct the first packet of a new session without database lookups
- Global Relay deploys the relay pattern geographically, shortening the first hop for users worldwide; Cloudflare handles signaling-side geo-steering
- Userspace Go with SO_REUSEPORT, runtime.LockOSThread, and pre-allocated buffers proved sufficient — kernel bypass was evaluated and rejected as unnecessary

## Synthesis
OpenAI's voice AI infrastructure serves 900 million weekly users through a carefully designed WebRTC architecture that challenges conventional approaches. The core insight is that standard WebRTC deployment patterns assume stable servers with fixed IP addresses and ports, but Kubernetes operates on the opposite assumption — pods are ephemeral and reschedulable. This fundamental mismatch manifests in two problems: port exhaustion (one UDP port per session at OpenAI's scale means tens of thousands of public ports) and state stickiness (ICE and DTLS sessions must stay pinned to the process that started them).

Rather than adopting the standard SFU architecture — which suits multiparty video calls but adds overhead for OpenAI's overwhelmingly 1:1 traffic pattern — the team split the stack into two components. A stateless relay sits at the geographic edge, presenting a minimal public footprint and routing packets by reading just enough of each STUN binding request to extract the ICE ufrag. The ufrag, generated during signaling, encodes routing metadata that the relay decodes on the first packet, after which a source-address-to-destination mapping takes over for all subsequent packets. A stateful transceiver behind the relay owns all the heavy WebRTC state: ICE connectivity checks, DTLS handshakes, SRTP encryption, and session lifecycle management.

This split solves both the port and state problems. The relay needs only a small, fixed set of public UDP ports. The transceiver can live on any internal address, and because sessions are demultiplexed behind a shared socket using SO_REUSEPORT, Kubernetes can freely reschedule pods without breaking active connections. A Redis cache backs the relay's in-memory flow table, allowing fast recovery after restarts, and the ufrag-based routing means the table can be rebuilt from the protocol itself.

The implementation choices are deliberately conservative. The relay runs as a Go userspace process reading from a regular UDP socket — no kernel bypass, no exotic networking frameworks. SO_REUSEPORT distributes incoming packets across multiple workers, runtime.LockOSThread pins goroutines to OS threads for cache locality, and pre-allocated buffers minimize garbage-collection pressure. The result handles the entire global real-time media traffic on a relatively small relay footprint.

Global Relay extends this pattern worldwide. Each ingress point runs the same packet-forwarding logic, just in a different geographic location. Cloudflare steers the initial HTTP/WebSocket signaling request to a nearby transceiver cluster, and the SDP answer tells the client which relay VIP to send media to. The ufrag carries enough information for the entire routing chain to work — from global relay to cluster relay to individual transceiver — without any out-of-band coordination.

The design tradeoffs are acknowledged: it's built around 1:1 sessions, the custom infrastructure carries a learning burden, and the "stateless" relay still holds soft state. But for OpenAI's specific workload, the architecture delivers low latency, Kubernetes compatibility, and operational simplicity where a standard SFU would have introduced unnecessary overhead.