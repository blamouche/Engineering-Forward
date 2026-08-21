# Redeploying Fable 5: Export Controls Lifted, Safety Framework Proposed
**Source**: https://www.anthropic.com/news/redeploying-fable-5
**Date**: 2026-06-30
**Author**: Anthropic
**Keywords**: Anthropic, Fable 5, export controls, AI safety, jailbreak, cybersecurity, government collaboration

## Elevator pitch
Anthropic redeployed Claude Fable 5 after US export controls were lifted, revealing a detailed account of the suspension, new safety classifiers, and a proposed industry framework for categorizing AI jailbreak severity.

## Takeaways
- The US government imposed export controls on Fable 5 and Mythos 5 on June 12, 2026, forcing Anthropic to suspend access for all users because real-time nationality verification was not feasible.
- Amazon researchers found a jailbreak that let Fable 5 identify software vulnerabilities and produce exploitation code; Anthropic's testing showed all frontier models (GPT-5.5, Opus 4.8, Kimi K2.7) could produce the same output.
- Anthropic trained an improved safety classifier that blocks the reported bypass in over 99% of cases, though it increases false positives on benign coding tasks.
- Anthropic, Amazon, Microsoft, and Google are drafting a consensus industry framework for assessing jailbreak severity (minor, narrow harmful, universal) to standardize how AI developers respond to safety findings.
- Anthropic committed to four areas of deeper government collaboration: pre-release evaluation, rapid information sharing, dedicated joint research resources, and a common industry security bar.

## Synthesis
Anthropic's redeployment of Fable 5 marks a watershed moment in the intersection of AI capability, government regulation, and industry self-governance. The two-week suspension — triggered when an Amazon research team found Fable 5 could be prompted into identifying software vulnerabilities and producing exploitation code — exposed a fundamental tension: the same cybersecurity capabilities that make frontier models valuable for defensive work also make them attractive to malicious actors.

The incident revealed something Anthropic had suspected but now demonstrated empirically: the reported jailbreak did not expose unique Mythos-level capabilities. Every frontier model tested, from Claude Haiku 4.5 to GPT-5.5 to Kimi K2.7, could produce the same vulnerability identification and exploitation code. This finding reframes the export control debate: restricting one model while leaving others equally capable creates a false sense of security.

Anthropic's response included a new safety classifier with a deliberately enlarged "safety margin" — blocking requests that are probably benign but have a small chance of being harmful. The tradeoff is more false positives during routine coding, which Anthropic acknowledges and plans to refine. More significantly, they proposed a consensus industry framework for categorizing jailbreak severity across three levels: minor (within safety margin), narrow harmful (specific harmful behavior), and universal (wide range of harmful behaviors). This framework, developed with Amazon, Microsoft, and Google, aims to give the industry a shared vocabulary for triaging safety findings.

The deeper government collaboration commitments — pre-release evaluation access, rapid safeguard information sharing, dedicated joint research teams, and a common security standard — represent a structural shift in how frontier AI companies operate. Anthropic is effectively proposing that government involvement in AI releases should become a durable, transparent process rather than an ad hoc intervention. Whether this becomes an industry standard or a competitive liability remains the central question.