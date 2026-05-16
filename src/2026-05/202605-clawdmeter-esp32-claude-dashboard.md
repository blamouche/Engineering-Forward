# Clawdmeter: ESP32 Desk Dashboard for Claude Code Usage
**Source**: https://github.com/HermannBjorgvin/Clawdmeter
**Date**: 2026 (repository active, 991 stars as of May 2026)
**Author**: HermannBjorgvin (macOS port by Chris Davidson @lorddavidson)
**Keywords**: Claude Code, ESP32, hardware dashboard, BLE, usage tracker, open source, maker, Anthropic

## Elevator pitch
Clawdmeter is an open-source ESP32 desk gadget that displays real-time Claude Code usage stats on a tiny AMOLED screen and doubles as a Bluetooth keyboard for Claude Code shortcuts, built by a developer for his own workflow.

## Takeaways
- The device runs on a Waveshare ESP32-S3-Touch-AMOLED-2.16 board with a 480×480 AMOLED display, capacitive touch, and optional Li-Po battery, connecting to the host computer over Bluetooth Low Energy.
- A Python daemon reads Claude Code OAuth credentials, polls the Anthropic API for rate-limit utilization headers every 60 seconds, and pushes usage data (session %, weekly %, status) to the ESP32 over BLE.
- The splash screen plays pixel-art Clawd (Anthropic's mascot) animations that get busier as usage rate climbs, with animations sourced from claudepix.vercel.app by @amaanbuilds.
- Physical buttons serve as BLE HID keyboard: left button sends Space for Claude Code voice mode push-to-talk, right button sends Shift+Tab for mode toggle.
- The project gained significant community traction (991 stars, 86 forks) and includes both Linux and macOS installation scripts with LaunchAgent/systemd daemon setup.

## Synthesis
Clawdmeter is a delightfully excessive maker project that embodies the current AI developer zeitgeist. Built by HermannBjorgvin, it's an ESP32-powered desk dashboard dedicated to tracking Claude Code usage — not because it's strictly necessary, but because it's fun and useful in exactly the way that makes personal hardware projects compelling.

The hardware is the Waveshare ESP32-S3-Touch-AMOLED-2.16, a $20-30 board with a sharp 480×480 AMOLED display and capacitive touch. The firmware, written in C using LVGL for the UI, implements three screens: a splash screen with animated pixel-art Clawd (Anthropic's mascot), a usage dashboard showing session and weekly utilization as percentages, and a Bluetooth status screen. The splash animations are organized by "mood groups" — the busier your Claude Code usage rate (measured by how fast your session utilization percentage is climbing), the more energetic the Clawd animations become. The firmware auto-rotates animations within each mood group every 20 seconds.

The data pipeline is clever in its simplicity. A Python daemon reads the Claude OAuth token from the macOS Keychain or Linux credentials file, makes a minimal API call to Anthropic (one token of Haiku, essentially free), and extracts usage data from the response headers: `anthropic-ratelimit-unified-5h-utilization` and similar fields. This data is pushed to the ESP32 over BLE as a JSON payload. The daemon runs as a LaunchAgent on macOS or a systemd user service on Linux, polling every 60 seconds.

Beyond monitoring, the device doubles as a Bluetooth HID keyboard for Claude Code shortcuts. The left button sends Space (for Claude Code's voice mode push-to-talk), and the right button sends Shift+Tab (mode toggle). These are standard BLE HID keyboard reports, so they work in whatever window has focus.

The project's README is unusually thorough and honest. It documents every aspect from firmware flashing to font recompilation (with LVGL 9 compatibility patches), includes a licensing gray area warning about Anthropic's proprietary fonts and copyrighted Clawd mascot, and credits all sources including the claudepix sprite library. The project has attracted 991 stars and 86 forks, with a macOS port contributed by Chris Davidson.

Clawdmeter represents a genre of AI-adjacent maker projects that treat API dashboards as physical artifacts. It's simultaneously a practical tool (at-a-glance quota awareness), a playful object (pixel-art mascot reacting to your usage), and a statement about how deeply AI coding tools are embedding into developers' daily workflows — deep enough to warrant dedicated hardware.
