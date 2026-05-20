# Introducing the OSSCAR Index
**Source**: https://supabase.com/blog/introducing-osscar-index
**Date**: 2026-04-28
**Author**: prashant
**Keywords**: open-source, ranking, OSSCAR, GitHub, growth metrics, community, Supabase, commit.fund

## Elevator pitch
The OSSCAR Index is a quarterly ranking of the fastest-growing open-source organizations, measured by GitHub stars, contributors, and package downloads using a transparent, reproducible methodology — with all code, data, and scoring open-source.

## Takeaways
- Most "top open source" lists rank by accumulated totals (stars, downloads) that reflect past success; OSSCAR measures growth rate to surface who is rising now, not who was big yesterday.
- The index uses three normalized signals (net new stars, unique contributors, package downloads from npm/PyPI/Cargo) combined via an L² norm, rewarding standout growth on a single signal while not penalizing projects missing certain metrics.
- Projects are split into two divisions — Emerging (<1,000 stars at quarter-start) and Scaling (≥1,000 stars) — with divisions locked at quarter-start to prevent gaming.
- Q1 2026 observations: Openclaw was the breakout story (365K stars, 1,383 contributors, 16.7M downloads); AI agents dominated Emerging; the rankings are genuinely global with Chinese universities and hardware platforms in the top 100.
- The full methodology, data pipeline, and scoring code are on GitHub at commitvc/osscar, with an RFC process for methodology changes planned by end of 2026.

## Synthesis
Supabase, in collaboration with >commit (a venture fund focused on open-source), has launched the OSSCAR Index — the Open Source Supabase Commit Analytical Ranking. This isn't just another vanity metric or marketing project; it's an attempt to solve a genuine information problem in the open-source ecosystem. Most existing rankings — GitHub trending, "top open source" lists, star counts — measure accumulated success. They tell you who won yesterday. OSSCAR measures who is winning today.

The methodology is deliberately transparent and designed to surface momentum rather than mass. Three signals are tracked quarterly: net new GitHub stars, unique contributors, and package downloads from npm, PyPI, and Cargo. Each signal is normalized within a division so that a 200-person team and a 5-person team can be compared fairly. The normalized scores are combined using an L² norm (square root of sum of squares), which rewards standout performance on a single signal rather than requiring balanced growth across all three. Importantly, projects missing certain signals (like a library without a published package) aren't penalized — they're scored only on what applies to them.

The two-division structure is a critical design choice. Ranking a new AI agent framework against Kubernetes makes no sense, so organizations are split into Emerging (<1,000 stars at quarter-start) and Scaling (≥1,000 stars). Divisions lock at the start of the quarter, so crossing the threshold mid-quarter doesn't change your bracket until the next cycle. This prevents the kind of division-hopping that would undermine the ranking's integrity.

Q1 2026's data tells a compelling story. Openclaw was the undeniable breakout — crossing the Scaling threshold by 236 stars on January 1 and finishing at 365,000 stars with 1,383 contributors and 16.7 million package downloads. Growth like that at that scale is almost unprecedented. In Emerging, AI agents dominated: Paperclip took #1, and the majority of the top 10 are autonomous agent frameworks or AI-native developer tools. But the index also surfaced non-AI projects like Craft Docs and npmx, proving the methodology catches momentum wherever it appears. Most notably, the rankings are genuinely global — Tsinghua University's MAIC, Sipeed, Tencent Connect, and BIT-DataLab all appear in the top 100, something most Western-centric rankings miss entirely.

Supabase's motivation is strategic but aligned with its identity as an open-source company. The platform itself runs on open-source infrastructure (Postgres, PostgREST, pg_vector, Deno), and the company's thesis is that a healthier, more visible ecosystem benefits everyone — including Supabase. Discovery drives contributors, contributors ship features, features create users. The OSSCAR Index is infrastructure for that flywheel. With quarterly updates, plans for more package managers (Go modules, container images), a public RFC process for methodology changes, and historical rankings that will reveal which projects sustain growth versus flash and fade, OSSCAR has the potential to become the definitive growth ranking for open source.
