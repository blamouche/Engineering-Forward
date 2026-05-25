# Don't Roll Your Own ...
**Source**: https://susam.net/do-not-roll-your-own.html
**Date**: May 23, 2026
**Author**: Susam Pal
**Keywords**: web design, UX, browser defaults, custom UI, accessibility, software engineering

## Elevator pitch
Drawing a parallel to the "don't roll your own crypto" maxim, Susam Pal argues that web developers should stop reimplementing browser-native features — scrolling, link navigation, text selection, password fields, date pickers — because custom implementations almost invariably produce worse, less accessible, and less reliable user experiences than what browsers already provide.

## Takeaways
- Custom page scrolling is the worst offender: it breaks muscle memory, keyboard scrolling, and accessibility by overriding behaviors users don't even think about
- GitHub's custom link navigation via JavaScript is cited as the most egregious example — "it is often faster to open the link in a new tab than to wait for GitHub's JavaScript code to handle the navigation"
- Custom password fields break password managers, autofill, strong password generation, mobile keyboards, accessibility tools, and can accidentally expose passwords as plain text
- Custom date pickers force users to learn ten different calendar widgets across ten different websites, with some requiring 40 clicks on "previous year" to select a birth year
- Continuous UI redesigns disproportionately harm older users and people who rely on muscle memory — "imagine how you would feel if the buttons of your washing machine were rearranged every morning"
- The principle mirrors crypto: the browser is the vetted, peer-reviewed implementation that's stood the test of time — override it only when absolutely necessary

## Synthesis
Susam Pal's essay is deceptively simple but cuts to a fundamental tension in web development: the gap between what developers find technically interesting and what users actually need. The "don't roll your own crypto" analogy is apt — both domains involve replacing battle-tested, peer-reviewed infrastructure with a private implementation that inevitably misses edge cases the community has spent decades discovering and fixing.

The examples are specific and relatable. GitHub's JavaScript link handling, which intercepts native browser navigation and replaces it with a slower custom implementation, is a particularly damning case study. Custom scroll behavior — smooth scrolling, parallax effects, scroll-jacking — breaks the most fundamental interaction users have with web pages. Custom form controls break the entire ecosystem of password managers, accessibility tools, and mobile keyboard integrations that have developed around native browser elements.

What makes this argument timely is the AI coding agent wave. If agents are producing 10x the code, as George Hotz warns, we should expect 10x the custom implementations of things browsers already do well. The "slop" problem Hotz describes will manifest not just as buggy business logic but as broken UI fundamentals — scroll behaviors that don't quite work, password fields that confuse password managers, date pickers with subtle off-by-one errors.

Pal's closing point about continuous redesign is the emotional core. The web's constant churn — rearranging washing machine buttons every morning — is a tax paid disproportionately by users who can least afford it: older people, non-technical users, anyone who relies on learned patterns to navigate digital spaces. In an era of AI-generated interfaces that can be redesigned at will, the discipline to leave well enough alone becomes a form of respect for users.
