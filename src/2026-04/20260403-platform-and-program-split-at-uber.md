# The Platform and Program Split at Uber

**Source**: https://newsletter.pragmaticengineer.com/p/the-platform-and-program-split-at
**Date**: 2022
**Author**: Gergely Orosz (Pragmatic Engineer)
**Keywords**: Uber, platform engineering, program teams, org design, engineering culture, scaling, team structure

## Elevator pitch
Uber's 2014 reorganization into platform and program teams is one of the most influential engineering org design decisions in tech history, and this detailed account explains why it worked and how it shaped Uber's culture for a decade.

## Takeaways
- In spring 2014, Uber CPO Jeff Holden announced a complete org reorganization into 16 program teams and 11 platform teams, replacing independent functional teams
- Program teams (60-70% of engineering) organize around user-facing missions and are optimized for rapid iteration on specific products
- Platform teams (30-40%) own shared infrastructure and are optimized for reliability, performance, and enabling other teams to move faster
- Teams were stack-ranked by importance—supply-side (driver) teams ranked higher than demand-side (rider) teams at the time, reflecting business priorities
- This structure became Uber's defining engineering culture and remains the foundation of how it operates today

## Synthesis
The platform/program split is one of those organizational innovations that, in retrospect, seems obvious—but took genuine insight to implement at the right time and in the right way. By spring 2014, Uber had grown to over 100 engineers with 10 PMs and 15 designers. Teams were operating independently, each owning their roadmap. This worked when the company was small, but coordination costs were compounding as the team grew.

The core problem with functional org structures at scale: a feature requires backend engineers, frontend engineers, and mobile engineers—but they all report to different managers with different roadmaps and different priorities. Getting anything substantial done requires negotiating across three different chains of command. The program/program split cuts through this by creating cross-functional teams aligned to missions.

Program teams are the product teams. They own specific user-facing missions—"grow driver supply," "improve rider experience"—and have all the disciplines needed to execute: engineers, PM, designer, sometimes data science. They can ship without negotiating with other teams for resources. The optimization target is speed.

Platform teams are the infrastructure teams. They own shared services, tooling, and infrastructure that multiple program teams depend on. Their job is to make program teams move faster by providing reliable, well-designed foundations. The optimization target is reliability and reusability.

The stack-ranking of teams by importance was strategically transparent. In 2014, supply (drivers) was the bottleneck for Uber's growth—you can't grow rides if there aren't enough drivers. So supply-side teams ranked higher than demand-side teams, which ranked higher than internal tooling teams. Every engineer could see where the company's priorities lay.

The 100-person transition moment Uber experienced is common. Many companies reach a size where independent team autonomy starts creating coordination failures, but haven't yet developed the cross-functional structures that enable independent execution at scale. The platform/program split is a proven solution, and Uber's implementation became the reference case that other companies studied.

The lasting lesson is architectural: good org design mirrors good system design. Platform teams are like shared libraries—provide clean APIs, maintain backward compatibility, enable other teams to build on them without understanding the internals. Program teams are like applications—move fast, own their full stack, ship to users. The same principles that make software systems scalable make engineering organizations scalable.
