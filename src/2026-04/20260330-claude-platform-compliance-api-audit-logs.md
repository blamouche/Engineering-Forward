# Audit Claude Platform Activity with the Compliance API
**Source**: https://claude.com/blog/claude-platform-compliance-api
**Date**: March 30, 2026
**Author**: Anthropic
**Keywords**: Claude Platform, compliance, audit logs, API, enterprise, governance, administrative actions, resource activities

## Elevator pitch
Anthropic launches the Compliance API for Claude Platform, giving organization administrators programmatic access to audit logs covering administrative actions and resource activities for enterprise governance and compliance requirements.

## Takeaways
- Compliance API provides programmatic access to audit logs via admin API key for Claude Platform organizations
- Tracks two categories: administrative actions (workspace membership, API key management) and resource activities (file creation, downloads, deletions)
- Does not log inference activities or model interactions — only administrative and file-level actions
- Historical data prior to API activation is unavailable; enterprise customers can consolidate Claude API and Enterprise audit logs
- Must be enabled by account team; documentation available on Anthropic Trust Center

## Synthesis
The Compliance API addresses a practical barrier to enterprise adoption of Claude Platform: the ability to demonstrate to security, legal, and compliance stakeholders that activity can be audited. For organizations in regulated industries — financial services, healthcare, legal — the question "can you show us who did what and when" is often a prerequisite for approving any new software platform, regardless of its utility.

The two-category approach reflects a deliberate scope decision. Administrative actions (who joined or left the organization, who created or revoked API keys, what configuration changes were made) and resource activities (file operations performed by users) are the categories most relevant to compliance and security investigations. They create an auditable record of human decisions and data handling without requiring Anthropic to log the content of model interactions — which would raise different privacy and confidentiality concerns.

The explicit exclusion of inference activities is significant. It means the Compliance API provides organizational governance visibility without exposing the conversational content of AI interactions to audit infrastructure. For organizations concerned about sensitive information shared in AI conversations, this separation maintains the boundary between governance logging (who accessed what) and content monitoring (what was discussed).

The requirement to enable through account teams rather than through self-serve configuration reflects enterprise deployment norms where features affecting compliance and security posture are gated by commercial relationships rather than enabled unilaterally. This also ensures that organizations are making a deliberate choice to activate audit logging rather than discovering it retroactively.

For engineering teams responsible for deploying Claude Platform in enterprise contexts, the Compliance API is an enabling feature rather than a differentiating one — it doesn't make the platform better, but it removes an objection that would otherwise prevent deployment in compliance-sensitive organizations. The parent organization consolidation feature for enterprise customers addresses the common scenario where organizations operate multiple Claude environments and need unified governance visibility.
