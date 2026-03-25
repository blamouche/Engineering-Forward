# This week on How I AI: How Microsoft’s AI VP automates everything with Warp
**Source**: https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-how-microsofts
**Date**: March 25, 2026
**Author**: Lenny Rachitsky
**Keywords**: micro‑agents, automation, Warp, Microsoft 365 Copilot, workflows

## Elevator pitch
A podcast recap showing how Microsoft’s AI VP uses Warp and Copilot to spin up ad‑hoc “micro‑agents” for everyday tasks like scanning, PDF merging, and video compression.

## Takeaways
- Ad‑hoc micro‑agents handle specific tasks and then disappear.
- Warp + CLI tools can automate hardware workflows like document scanning.
- AI‑assisted file manipulation can shrink workflows from hours to minutes.
- Automation frees attention for higher‑value work instead of tool wrangling.
- The episode links to detailed ChatPRD workflows for replicating the tasks.

## Synthesis
This week’s How I AI episode features Marco Casalaina, Microsoft’s VP of Core AI Products, describing how he uses Warp, Microsoft 365 Copilot, and ChatGPT to automate day‑to‑day work. The theme is “micro‑agents”: ad‑hoc, unnamed agents created on the fly to solve a single problem—scan a document, compress a video, or manipulate files—without building a permanent workflow.

Casalaina argues that this kind of automation is most powerful when it removes friction from mundane tasks. A simple example is scanning two‑sided homework. Instead of wrestling with scanner software, he uses Warp to control a scanner via the NAPS2 CLI, flipping pages and merging PDFs automatically. The result is that he can focus on helping his daughter with math rather than dealing with device UI. The lesson is that AI plus command‑line tools can outperform complex GUIs by abstracting away operational steps.

Another example is video compression. Faced with a 1.7GB video file, Casalaina asks Warp to analyze the file, identify why it is large, and re‑encode it with FFmpeg. The AI narrows the cause to excessive bitrate and resolution, then compresses the file to 13MB while maintaining quality. This shows how AI‑driven file manipulation can turn a specialized media task into a quick, guided workflow.

The episode highlights how these micro‑agents differ from traditional automation. Instead of building a persistent script or workflow, Casalaina creates short‑lived agents tailored to the problem at hand. This keeps automation lightweight and flexible, and lowers the cost of experimentation. He describes this as a growing pattern: ad‑hoc agents are blurring the line between “using” AI and “building” AI because everyday users can orchestrate tools without formal engineering effort.

The recap also points to linked resources hosted on ChatPRD that provide step‑by‑step workflows: automating Azure role management, creating a meeting scheduler with Microsoft 365 Copilot, and scanning/merging documents. These links imply the episode is not just narrative but a gateway to reproducible workflows.

Overall, the episode positions micro‑agent automation as a practical, near‑term use case for AI: remove tool friction, encapsulate a task in a temporary agent, and move on. It’s less about building autonomous systems and more about leveraging AI to turn everyday operational chores into fast, repeatable actions.
