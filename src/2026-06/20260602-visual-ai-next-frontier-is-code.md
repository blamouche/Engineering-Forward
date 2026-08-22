# The Next Frontier of Visual AI Is Code
**Source**: https://a16z.com/the-next-frontier-of-visual-ai-is-code/
**Date**: 2026-06-02
**Author**: Yoko Li (Andreessen Horowitz)
**Keywords**: visual AI, code generation, pixel-native, code-native, SVG, HTML, Blender, Lottie, 3D, test-time compute, editability, design

## Elevator pitch
Visual AI is shifting from generating final pixel outputs to creating source code for editable artifacts—transforming design, UI, and 3D workflows by enabling continuous iteration and feedback loops that pixel-native diffusion models can't match.

## Takeaways
- Two stacks of visual generation: pixel-native (diffusion models generating images/videos directly) and code-native (generating source code that is then rendered by an engine)
- Code-native generation produces structured representations (SVG, HTML/CSS, React, Lottie JSON, Blender scripts, USD scenes) that can be edited, reused, versioned, and validated—unlike flat pixel outputs
- Code enables a precise feedback loop: Code → Render → Inspect → Revise, where each iteration improves the underlying artifact, not just the rendered output
- Visual code generation is especially interesting for test-time compute because the model debugs a visual program in a closed-loop, verifiable environment—not just sampling more images
- The market is organizing around runtimes (browser, SVG renderer, Lottie player, Blender, game engine), each creating a different wedge with its own source representation and production workflow

## Synthesis
Yoko Li's analysis identifies a fundamental shift in visual AI: the most interesting tools have stopped trying to generate the final pixel output and are instead generating the source code behind it. This shift from pixel-native to code-native generation unlocks editability, iteration, and feedback loops that diffusion models alone can't match.

The distinction matters because production workflows care about what happens after generation. If a model generates a logo as a raster image and one curve is wrong, the user has to mask it, inpaint it, regenerate it, or manually redraw it. If the output is SVG, the user can edit the path, the primitive, the gradient, or the stroke. If a UI design comes as a screenshot, it's mostly inspiration. If it comes as HTML/CSS or React, designers can inspect the DOM, swap real components, test responsive states, check accessibility, and wire it into the application.

The key technical insight is about test-time compute. In pixel-native generation, more inference means sampling more outputs—generate twenty images, pick the best one. Every attempt is a new roll of the dice. In code-native generation, the loop is Code → Render → Inspect → Revise. The model produces the artifact, renders it, sees what broke, and patches the source. If the spacing is wrong, change the CSS. If a logo curve is off, edit the SVG path. Every iteration improves the underlying artifact, not just the rendered output. The model is debugging a visual program in a closed-loop, verifiable environment.

The market map organizes around the runtime where the artifact is rendered: browsers for UI/graphics, SVG renderers for logos, Lottie players for animation, Blender for 3D. Each runtime creates a different wedge because each has its own source representation, feedback loop, and production workflow. 3D is identified as the next important frontier because 3D assets have the richest underlying structure—geometry, materials, lighting, cameras, scene hierarchy—and the most complex production workflows where editability matters most.