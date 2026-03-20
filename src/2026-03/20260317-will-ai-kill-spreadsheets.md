# Will AI Kill Spreadsheets?
**Source**: https://speedrun.substack.com/p/will-ai-kill-spreadsheets
**Date**: 2026-03-17
**Author**: a16z speedrun (Andrew Chen)
**Keywords**: spreadsheets, AI, code generation, software, productivity tools, business applications, migration

## Elevator pitch
Andrew Chen sparked debate by claiming AI-enabled code generation will replace spreadsheets as the default business logic tool, while critics argue that the grid visualization and iterative modeling use cases remain stickier than Chen acknowledges.

## Takeaways
- Chen argues spreadsheets are "business logic trapped in a grid" lacking version control, testing, and modularity—gaps AI-generated code fills
- With ~1 billion spreadsheet users, even 10% migration to code-based solutions would create substantial market opportunity
- Critics counter that grid-based visualization is essential for human understanding and that finance modeling requires the "95% right is 0% useful" standard
- Dan Hockenmaier's distinction is most useful: "mini software" use cases (dashboards, trackers) will migrate; analytical modeling tools are stickier
- The IDE experience problem—making code-based solutions as accessible as spreadsheets—remains unsolved and is the real barrier

## Synthesis
Andrew Chen's argument that AI will kill spreadsheets surfaced one of the most substantive debates in the enterprise software discussion of 2026. His core claim: spreadsheets represent a form of software development that was adopted by non-developers because writing actual software was too hard. AI code generation eliminates that barrier, making proper software—with version control, testing, modularity, and debugging—accessible to the billion spreadsheet users worldwide.

The economic math supports taking the argument seriously. Even if only 10% of spreadsheet use cases migrate to code-based alternatives, the market displacement would be substantial. Applications currently built in Excel—financial models, operational trackers, data pipelines, reporting tools—would shift to maintained software artifacts rather than fragile grid-based documents that break when a formula is accidentally overwritten.

The most cogent counter-argument comes from the finance domain. Richard Pham defended grid visualization as essential for human understanding of data relationships—the two-dimensional structure of a spreadsheet maps naturally to how analysts think about multivariable problems. Robert Peters articulated the financial modeling standard more precisely: models used for real business decisions must be 100% correct because "95% right is 0% useful" when the output drives a capital allocation decision. AI-generated code, however capable, introduces correctness uncertainty that spreadsheets—where every formula is visible and traceable—do not.

Dan Hockenmaier's segmentation is the most analytically useful contribution to the thread. He distinguishes between spreadsheet use as "mini software" (dashboards, operational trackers, repeating calculations) and spreadsheet use as analytical tool (understanding business dynamics through ad-hoc exploration). The former category will migrate to code because the maintenance and reliability benefits are clear. The latter will be stickier because the interactive, visual, exploratory nature of grid-based analysis serves different cognitive needs than structured software artifacts.

The unresolved question is the development experience: can AI-assisted coding environments become genuinely accessible to Excel power users, or does software development impose enough conceptual overhead that most spreadsheet users remain in spreadsheets? The answer determines the timeline and magnitude of any migration.
