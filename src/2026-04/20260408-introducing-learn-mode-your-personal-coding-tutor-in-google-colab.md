# Introducing Learn Mode: your personal coding tutor in Google Colab

**Source**: https://blog.google/innovation-and-ai/technology/developers-tools/colab-updates/
**Date**: April 8, 2026
**Author**: Spencer Shumway and Mae LaPresta
**Keywords**: Google Colab, Gemini, learn mode, coding tutor, custom instructions, notebooks, developer education

## Elevator pitch
Google is turning Colab’s Gemini assistant into a configurable notebook-native tutor, combining custom instructions with a Learn Mode that optimizes for explanation over code generation.

## Takeaways
- Colab now supports notebook-level Custom Instructions that shape how Gemini helps within a given project or class context.
- Learn Mode pushes Gemini to teach step by step instead of jumping straight to a code answer.
- The new settings travel with shared notebooks, so authors can distribute a tailored assistant experience.
- Google is aiming the feature at students, educators, and developers learning new frameworks or languages.
- The launch shows Colab evolving from hosted notebook environment toward an AI-mediated learning workspace.

## Synthesis
The interesting part of this update is not that Colab got another AI feature. It is that Google is explicitly differentiating between an assistant that completes work for you and one that helps you build capability. Learn Mode is a product decision about pedagogy, not only productivity. Instead of treating the best AI experience as the fastest path to a working code block, Google is acknowledging that many users open Colab to learn concepts, frameworks, or techniques and that a pure answer machine can short-circuit that goal.

The notebook-level Custom Instructions are a quiet but important complement. They turn the assistant from a generic chat overlay into something that can inherit local norms: preferred libraries, teaching style, syllabus context, coding conventions, or project constraints. That matters because educational usefulness often depends more on context than on raw model quality. A decent model with the right local framing can feel much more helpful than a stronger model that answers in a vacuum.

There is also a distribution angle here. Because the instructions live in the notebook, the tailored assistant can be shared with the artifact itself. That means a course, tutorial, or team notebook can carry its own AI behavior along with its content. Over time, that could make notebooks feel more like packaged interactive experiences than passive documents. The assistant becomes part of the medium.

More broadly, this is another sign that the AI tooling market is splitting into at least two modes: automation mode and teaching mode. Many products still blur those together, but they serve different user goals. For experienced developers, instant code generation is often the point. For students, onboarding engineers, and people switching stacks, explanation quality matters more. Google is smart to make that distinction explicit inside Colab, because Colab sits right at the intersection of experimentation, education, and hands-on development.
