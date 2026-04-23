# Building eval systems that improve your AI product

**Source**: https://www.lennysnewsletter.com/p/building-eval-systems-that-improve
**Date**: April 22, 2026
**Author**: Hamel Husain and Shreya Shankar
**Keywords**: AI evals, error analysis, product quality, observability, human labels

## Elevator pitch
Hamel Husain and Shreya Shankar outline an eval methodology built around rigorous error analysis, arguing that the only useful evals are the ones directly tied to real user failure modes.

## Takeaways
- The process starts with open coding and axial coding of real user traces, not with off-the-shelf metrics.
- A single trusted domain expert can be a strong source of quality labels in many products.
- The goal is to build a manageable taxonomy of the most important failure modes.
- Ready-made metrics are useful mainly as discovery aids, not as product dashboards.
- The end state is an eval suite that creates a continuous improvement loop rather than vanity reporting.

## Synthesis
This article is strong because it attacks one of the easiest traps in AI product work: building evaluation dashboards that look sophisticated but do not help the product improve. Hamel Husain and Shreya Shankar argue that teams often start with generic metrics because they are easy to obtain, then discover that those scores do not line up with what users actually care about. Their alternative is much more grounded. Before you can automate evaluation, you need to understand how the product fails in its own domain.

The methodology begins with human review of real traces. Open coding captures what feels wrong in free-form notes, and axial coding groups those notes into recurring categories. That may sound qualitative, but it is exactly how a useful eval taxonomy gets built. Once the failure modes are concrete and prioritized, teams can then automate checks against them. This is a far more plausible route to trustworthy evals than starting from fashionable categories and hoping they correlate with user pain.

Another useful idea is the “benevolent dictator” approach to quality. For many products, one strong domain expert can provide more coherent evaluation than a loose crowd of annotators with inconsistent standards. That highlights how much evaluation is a product question, not just a statistical one.

The broader takeaway is that good eval systems are extensions of product understanding. They are not generic model scores pasted onto an application. They emerge from studying real user interactions, finding recurring failures, and building measurement around those specifics. That is slower at first, but it is much more likely to create a flywheel where each evaluation signal points to work that can actually make the product better.
