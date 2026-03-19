# Your Data Agents Need Context
**Source**: https://a16z.com/your-data-agents-need-context/
**Date**: 2026-03-10
**Author**: Jason Cui, Jennifer Li
**Keywords**: data agents, enterprise AI, context layer, semantic layer, business context, data governance, ontology, Databricks, Snowflake

## Elevator pitch
Enterprise AI data agents fail not because models can't write SQL, but because they lack the business context—metric definitions, data hierarchies, tribal knowledge—needed to answer questions that actually matter to the organization.

## Takeaways
- Simple-seeming queries like "What was revenue growth last quarter?" require business definitions (how revenue is calculated, what constitutes a fiscal quarter, which data source is authoritative) that agents currently lack.
- A modern context layer must unify: business metric definitions, data source identification and truth hierarchies, tribal knowledge and conditional instructions, and governance guidelines.
- Traditional semantic layers (BI tool connectors) are too narrow: they define specific metrics for specific tools rather than providing the autonomous, continuously evolving context that independent agents need.
- Three emerging solution categories: data gravity platforms (Databricks, Snowflake) expanding into context, existing AI data analyst companies pivoting, and new dedicated context layer startups.
- Building a proper data agent requires both technical infrastructure and systematic organizational knowledge management—it is "no small feat."

## Synthesis
The data agent failure mode described here is precise and important: models can generate syntactically correct queries against well-specified schemas, but enterprise data is rarely well-specified in the ways agents need. Revenue might be calculated differently across business units. "Last quarter" might mean fiscal or calendar depending on context. The authoritative source for a metric might be one of three competing systems depending on the reporting purpose.

Human analysts navigate this through accumulated institutional knowledge—years of onboarding, informal conversations, and hard-learned lessons about which numbers to trust and when. That knowledge exists in human heads, Slack conversations, and tribal memory, not in database schemas or documentation. Agents can't access it because it hasn't been structured in a form they can consume.

The context layer concept described here is essentially an attempt to make that institutional knowledge machine-readable. The comparison to traditional semantic layers is useful: semantic layers like dbt metrics definitions or Looker LookML solve a subset of the problem (metric calculation) but not the full context problem (source hierarchy, conditional logic, governance rules, exceptions). The emerging context layer tools aim for broader coverage.

The market structure analysis—incumbents expanding, pivots from adjacent tools, dedicated startups—reflects a genuine opportunity space that hasn't been won yet. Data gravity platforms like Databricks and Snowflake have the distribution advantage but may move slowly given their existing product priorities. The open question is whether this is a standalone product category or a feature that consolidates into data platform tooling.
