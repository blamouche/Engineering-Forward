# Proof of Human: How to Verify a Person Is Real and Unique
**Source**: https://blog.bytebytego.com/p/proof-of-human-how-to-verify-a-person
**Date**: 2026-07-04
**Author**: ByteByteGo
**Keywords**: proof-of-human, identity verification, biometrics, iris scanning, zero-knowledge proofs, World ID, uniqueness, anonymity

## Elevator pitch
A deep technical exploration of the five pillars required to build a proof-of-human system that can verify a real, unique person across the internet without knowing who they are.

## Takeaways
- Uniqueness verification (one-to-many matching) is fundamentally harder than authentication (one-to-one matching); at billion-person scale, per-comparison error rates must be on the order of one in a hundred billion
- Anonymity is achievable through secret-shared biometrics: iris readings are split across independent organizations in different jurisdictions via secure multi-party computation (AMPC), so no single party ever sees the full biometric
- Recovery is handled by treating verified humans as abstract accounts in a public registry (WorldIDRegistry), with multiple Authenticators (phone, browser, hardware token) and Recovery Agents that can re-authenticate via fresh biometric checks
- Verification uses nullifiers—numbers derived from credentials, a relying party identifier, and an action—so services can enforce one-per-human rules without learning identity; an Oblivious Nullifier Pool prevents reuse and cross-service tracking
- Delegation allows AI agents to register against a human's credentials via AgentBook, so agents can act on behalf of verified humans while the human's quota limits abuse

## Synthesis
The article makes a compelling case that the identity infrastructure we have—authentication systems like OAuth, passkeys, and biometric unlocks—solves a fundamentally different problem than what the internet needs now. Authentication verifies that a returning user is who they claim to be (a one-to-one match). What online services increasingly need is uniqueness verification: ensuring each person is different from every other person who has interacted with the system (a one-to-many match). This distinction becomes critical at internet scale, where the probability of false matches scales with the size of the comparison population.

The technical architecture described centers on World ID's implementation. The iris biometric is chosen specifically for its entropy properties—two unrelated humans have essentially zero chance of producing matching iris patterns, even accounting for noise. The Orb device captures the iris using multispectral imaging, runs neural networks locally for liveness detection, and transmits only derived cryptographic material, never the original image. The iris reading is then split into three pieces of statistically random noise, each held by a different organization in a different jurisdiction, enabling duplicate checking without any party ever reconstructing the full biometric.

The verification layer introduces a clever cryptographic primitive: the nullifier. Derived from three inputs (user credentials, relying party identifier, and action context), nullifiers allow services to detect repeat visits by the same human without being able to link activity across different services or actions. An on-chain Oblivious Nullifier Pool prevents reuse, and IDKit wraps the entire flow into two zero-knowledge proofs that applications can verify.

The most forward-looking section addresses delegation—the question of what happens when AI agents act on behalf of humans. The design allows agents to register in AgentBook, tying their activity to a verified human's credentials while maintaining the human's privacy. Each human gets a quota (currently defaulting to three uses per service), preventing a single person from scaling into many parallel agents.

The article honestly acknowledges open questions: hardware decentralization of the Orb, unlinkability under adversarial pressure, scaling delegation to massive agent volumes, and the bootstrap problem of reaching critical adoption. This is an engineering-rich exploration of a problem class that the identity stack has so far left alone, and the techniques described—secret-shared biometrics, scoped nullifiers, account-style key rotation, and delegated quotas—represent the current frontier of the proof-of-human design space.