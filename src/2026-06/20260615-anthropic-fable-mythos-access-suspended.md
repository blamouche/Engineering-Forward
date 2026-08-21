# Anthropic Statement on US Government Directive to Suspend Access to Fable 5 and Mythos 5
**Source**: https://www.anthropic.com/news/fable-mythos-access
**Date**: 2026-06-15
**Author**: Anthropic
**Keywords**: Anthropic, Fable 5, Mythos 5, export controls, national security, US government, AI safety, data retention

## Elevator pitch
Anthropic issued a formal statement confirming it had disabled Fable 5 and Mythos 5 for all users after receiving a US government export-control directive tied to national security, marking the first time a frontier AI model was forcibly suspended by government action.

## Takeaways
- The US government issued an export-control directive that required Anthropic to suspend access to Fable 5 and Mythos 5 for all users, effective immediately
- Anthropic could not implement real-time nationality verification at the required granularity, making a blanket suspension the only compliant option
- The 30-day customer data retention policy for Fable-class models was introduced specifically to support government safety review requirements, carrying real costs in customer trust
- Anthropic reiterated its position that government should have statutory authority to block unsafe deployments, while calling for a structured due-process framework
- The directive represents an unprecedented intersection of national security law and frontier AI governance, with implications for how all frontier labs operate

## Synthesis
Anthropic's statement on the Fable 5 and Mythos 5 suspension is a landmark document in AI governance—it represents the first confirmed instance of a government using export-control authority to force a frontier AI lab to halt model access. The statement is notable for its restraint: Anthropic confirms compliance, explains the technical reason (inability to perform real-time nationality verification), and frames the event as consistent with its publicly stated policy that government should have the ability to block unsafe deployments.

The data retention requirement is a critical detail. Anthropic's 30-day retention policy for Fable-class models was not a product decision but a compliance measure—a cost the company absorbed with customers to meet government review needs. This creates a precedent: frontier models with national-security-relevant capabilities may need to accept permanent surveillance overhead, changing the economics and privacy profile of frontier AI products.

The statement's tone suggests Anthropic is walking a tightrope: cooperating fully with the directive while signaling to the AI community and its customers that this is a structured, legal process rather than arbitrary government overreach. The call for a statutory framework with due process implies Anthropic wants the rules to be predictable, not ad hoc—a position that benefits incumbents who can afford compliance infrastructure but raises barriers for new entrants.

For the engineering community, the suspension underscores that frontier model access is no longer guaranteed. Teams building on Fable 5 or Mythos-class APIs need contingency plans for government-mandated outages. The event also validates the strategic value of open-weight alternatives like GLM-5.2 (released under MIT license with no regional restrictions), which became more attractive precisely because they sit outside US export control jurisdiction.