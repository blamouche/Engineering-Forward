# Scaling Uber with Thuan Pham (Uber's First CTO)

**Source**: https://newsletter.pragmaticengineer.com/p/scaling-uber-with-thuan-pham-ubers
**Date**: Unknown
**Author**: Gergely Orosz (Pragmatic Engineer interview)
**Keywords**: Uber, CTO, scaling, microservices, platform engineering, program/platform split, engineering leadership

## Elevator pitch
Uber's first CTO Thuan Pham shares how he led three distinct "tours of duty" to stabilize, re-architect, and scale Uber's engineering, including the origin of the influential program/platform split and how they launched Uber in China in five months instead of 18.

## Takeaways
- Thuan divided his Uber tenure into three tours: stabilizing a fragile system, re-architecting it from monolith to microservices, and scaling the engineering organization
- The program/platform split originated before microservices—it was an org structure innovation that became necessary as the team grew past the point where independent teams could function
- Professional reputation compounds unpredictably: Thuan was recruited to Uber based on a prior relationship from a decade earlier, and built his teams by calling on engineers he'd worked with before
- Uber launched in China in just five months against an original 18-month estimate by accepting more risk and running systems in parallel
- AI is already changing how Faire (his current company) operates software development, though Thuan sees the biggest impacts coming in the next few years

## Synthesis
Thuan Pham's career is a case study in engineering leadership at scale. Joining Uber when it had 40 engineers and 30,000 rides per day—with the system crashing multiple times a week—he spent seven years rebuilding the company's technical foundation while the business grew orders of magnitude around him.

His framing of three "tours of duty" is pedagogically useful. The first tour focused on stabilization: getting the system reliable enough to trust. You can't architect for scale if the system is too fragile to reason about. The second tour was re-architecture: moving from a monolith to microservices, which at Uber eventually meant hundreds of services in multiple languages. The third tour was organizational scaling: building teams that could operate this increasingly complex system autonomously.

The program/platform split deserves its reputation as one of the more influential org innovations in modern engineering. What Pham explains that adds texture to the documented story: the split came before microservices, not after. It was an org structure solution to a coordination problem—teams organized by function (frontend, backend, mobile) couldn't ship cross-functionally without constant coordination overhead. Program teams (organized around user-facing missions) and platform teams (owned shared infrastructure) provided the structure needed to scale independently.

The China launch story illustrates the relationship between risk tolerance and speed. The standard estimate was 18 months; they did it in five by accepting higher risk, running systems in parallel that would normally be sequential, and accepting that some things would need to be fixed post-launch rather than pre-launch. This is a recurring pattern in high-growth tech: deliberate risk-taking as a competitive strategy.

The professional reputation point is underappreciated. Bill Gurley recruited Pham to Uber based on knowing him from a startup a decade earlier. Pham built his critical infrastructure teams by calling engineers he'd worked with at VMware who trusted him enough to follow him to Uber. The ROI on professional relationships in tech is enormous and unpredictable—you can't know which relationship will matter most, so maintaining all of them matters.

For engineering leaders building or scaling platforms, Pham's interviews across the Pragmatic Engineer series constitute one of the best documented case studies of what large-scale engineering transformation actually looks like from the inside.
