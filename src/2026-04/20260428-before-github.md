# Before GitHub

**Source**: https://lucumr.pocoo.org/2026/4/28/before-github
**Date**: April 28, 2026
**Author**: Armin Ronacher
**Keywords**: GitHub, open source infrastructure, software commons, decentralization, dependencies

## Elevator pitch
Armin Ronacher's retrospective argues that GitHub solved real discovery and archival problems for open source, but in doing so also normalized a low-friction dependency culture whose trust model becomes fragile once confidence in the central platform starts to erode.

## Takeaways
- Before GitHub, many projects ran on self-hosted infrastructure with more friction and stronger awareness of provenance.
- GitHub dramatically improved discoverability, collaboration, and long-term visibility for open-source projects.
- The same low-friction environment helped accelerate micro-dependencies and a much denser package ecosystem.
- As trust in GitHub declines, the consequences extend beyond hosting into package discovery, supply-chain assurance, and community memory.
- A more decentralized future may restore autonomy, but it also risks renewed fragmentation and link rot.

## Synthesis
This essay looks backward in order to explain why current unease around GitHub feels larger than dissatisfaction with an ordinary software product. Ronacher recalls a pre-GitHub open-source world of self-hosted Trac instances, Subversion servers, tarballs, mailing lists, and project-specific infrastructure. That world had more friction and more fragmentation, but it also forced a closer relationship between a dependency and the people, history, and infrastructure behind it. You rarely adopted software without seeing where it lived, who maintained it, and how stable its home seemed.

GitHub changed that. The essay is generous about what the platform made possible. It lowered the cost of publishing, collaboration, and discovery. It made issue tracking and pull requests legible to many more contributors. It also became a kind of public memory for the software commons, preserving discussions, forks, and abandoned projects in a searchable place. That archival function matters in Ronacher's telling because the pre-platform web often lost software when a maintainer's server disappeared or a domain expired.

At the same time, the article argues that GitHub's success helped create a different dependency culture. When publishing and discovering code became nearly frictionless, ecosystems such as npm encouraged much larger and more opaque package graphs. Micro-dependencies were not only a packaging habit, but a consequence of infrastructure that made creating and consuming tiny projects feel almost costless. GitHub then became part of the trust layer that made that system tolerable. Users could inspect a repository, gauge activity, and infer some legitimacy from its visible history.

That is why a decline in trust around GitHub has broader implications than repository hosting alone. If developers begin to doubt the reliability, governance, or community orientation of the platform, the impact reaches package selection, provenance heuristics, and long-term discoverability. The platform sits inside the software supply chain and inside the social infrastructure of open source. Weakening it changes both the technical and communal environment.

Overall, the essay is less a call to nostalgia than a warning about tradeoffs. Decentralization may recover autonomy and reduce dependence on one corporate platform, but it will also reintroduce fragmentation, archival loss, and coordination cost. The article's strongest point is that GitHub was not just a convenient forge. It became the memory and trust scaffolding for a much larger software ecosystem, which makes its current instability a systemic question rather than a matter of product taste.