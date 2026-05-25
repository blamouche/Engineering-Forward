# How I AI: Felix Rieseberg's Claude Workflows for 3D House Design and a $20 Hardware Buddy
**Source**: https://www.chatprd.ai/how-i-ai/felix-rieseberg-claude-code-cowork-workflows-for-3d-house-design-and-hardware-buddy
**Date**: May 25, 2026
**Author**: Claire Vo
**Keywords**: Claude Cowork, Claude Code, Felix Rieseberg, 3D modeling, hardware, dashboard, Live Artifacts, Anthropic

## Elevator pitch
Anthropic's Felix Rieseberg demonstrates three inventive Claude workflows: transforming a floor plan into an interactive 3D walkthrough with furniture parsed from email receipts, building auto-updating Live Artifact dashboards, and programming a $20 hardware "Claude buddy" using natural language.

## Takeaways
- Felix's "abstraction ladder" philosophy: instead of automating one step, automate the entire outcome — from "make a floor plan with units" to "build an interactive 3D walkthrough with my actual furniture."
- Claude extracted furniture dimensions from years of Gmail purchase receipts, turning an unstructured email archive into a structured personal inventory database for the 3D house planner.
- Live Artifacts enable auto-refreshing personal dashboards fed by connected services (Spotify, Gmail, Calendar, Notion); the key phrase is "make this a live artifact."
- A $19 ESP32-like device with LCD, Wi-Fi, and Bluetooth was programmed entirely through natural language description — Felix wrote zero lines of low-level code.
- The hardware buddy feature is now integrated directly into Claude Desktop (Help > Troubleshooting), making physical AI interaction accessible to non-developers.

## Synthesis
Claire Vo's interview with Felix Rieseberg is a showcase of what happens when an experienced engineer applies the "stop doing tedious work" philosophy systematically. The three workflows demonstrate an escalating scale of ambition, each building on the pattern of progressively offloading more of the problem to Claude.

The 3D house planner workflow is the most impressive. Starting from a realtor's marketing floor plan with no measurements, Felix pointed Claude Cowork at a folder containing the plan and all associated documents (disclosures, permits, mortgage info). Claude found a building permit for the garage with actual dimensions and used it as a reference to calculate the rest. Instead of stopping at a dimensioned 2D plan, Felix went up the abstraction ladder: Claude analyzed the floor plan image, identified walls, extruded them into 3D, and created an interactive walkthrough. Then another layer: connecting Gmail, Claude parsed years of furniture purchase receipts, extracted dimensions, and populated the 3D model with actual furniture. Felix admitted he's a good software engineer but "would have no idea how to do this himself."

The Live Artifacts workflow shows the product vision: create something once, have it stay relevant forever. With OAuth-style Connectors to Gmail, Spotify, Calendar, and Notion, a simple open-ended prompt ("whatever else you find that's relevant to my life") produces a personal dashboard that auto-refreshes. The creative potential is demonstrated by asking Claude to redesign the dashboard in "early 2000s software" style — complete with Winamp references and pixelated aesthetics.

The $20 hardware buddy is the most tangible bridge between AI and the physical world. A small device with LCD, Wi-Fi, and Bluetooth was programmed entirely through natural language: "I want my little Claude to live on this thing, and I want it to cheer me on every single time I do a good job." Claude figured out the Bluetooth protocol and wrote all the code. The feature is now integrated into Claude Desktop's troubleshooting menu, making hardware interaction accessible without embedded systems knowledge.
