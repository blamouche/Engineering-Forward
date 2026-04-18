# Write broken commits for better review

**Source**: https://huonw.github.io/blog/2026/04/broken-commits/
**Date**: April 19, 2026
**Author**: Unknown
**Keywords**: huonw, write, broken, commits, better, review

## Elevator pitch
Building an atomic code change from a series of tastefully broken commits can make for easier review, especially by separating mechanical from non-mechanical changes

## Takeaways
- Write broken commits for better review By Huon Wilson — 17 Apr 2026 I spend a lot of time reviewing code, and I think it’d be easier if I saw more tastefully broken commits.
- Commits construct a story about a change: “first this happened, then that, that another thing” is a good narrative; “first everything happened, the end”… not so much.
- Sometimes, telling that story is impossible without having a commit that breaks tests or doesn’t compile!
- The principle that usually drives me to commit broken code is making mechanical changes obviously mechanical and mechanically obvious : reformatting, renaming a function or file, re-indenting, … are not “real” changes like adding new code or optimising a loop, and intermixing mechanical & real changes all at once makes verifying either of them hard.
- If mechanical changes are separate, it’s easy to be sure of huge changes: “yes, this commit is solely running a code formatter on 3k files”.

## Synthesis
Write broken commits for better review By Huon Wilson — 17 Apr 2026 I spend a lot of time reviewing code, and I think it’d be easier if I saw more tastefully broken commits. Commits construct a story about a change: “first this happened, then that, that another thing” is a good narrative; “first everything happened, the end”… not so much. Sometimes, telling that story is impossible without having a commit that breaks tests or doesn’t compile! The principle that usually drives me to commit broken code is making mechanical changes obviously mechanical and mechanically obvious : reformatting, renaming a function or file, re-indenting, … are not “real” changes like adding new code or optimising a loop, and intermixing mechanical & real changes all at once makes verifying either of them hard. If mechanical changes are separate, it’s easy to be sure of huge changes: “yes, this commit is solely running a code formatter on 3k files”. I can literally check out the parent commit, and run the same formatting command, and get the same result. I’m feeling acute pressure on my ability to review code as I use more AI. I’m personally accountable for code that I’ve only reviewed, so it better be a damn good review. Any trick that makes that review easier is a good one. The technique is unlocked by separating commits into two buckets, “units of review” and “units of persistence”, via squash merges: we can be deliberate about nice commits for a reviewer now, without cluttering the long-term history.
