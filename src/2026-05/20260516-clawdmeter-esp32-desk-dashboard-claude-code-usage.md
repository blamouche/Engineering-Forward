# Clawdmeter: ESP32 desk dashboard for Claude Code usage
**Source**: https://github.com/HermannBjorgvin/Clawdmeter
**Date**: May 2026
**Author**: HermannBjorgvin (with macOS port by Chris Davidson @lorddavidson)
**Keywords**: Claude Code, ESP32, dashboard, BLE, physical interface, usage monitoring, agent tooling

## Elevator pitch
Clawdmeter is an open-source physical dashboard built on an ESP32-S3 AMOLED board that displays Claude Code usage metrics and provides physical buttons for voice-mode push-to-talk and mode switching via Bluetooth—bridging AI coding agents with tangible hardware interfaces.

## Takeaways
- The device polls Claude Code's OAuth API to extract usage statistics from response headers (session %, weekly %, rate limits) and pushes them to an ESP32 display over BLE.
- Physical side buttons send Space (voice-mode push-to-talk) and Shift+Tab (mode toggle) as standard BLE HID keyboard input, working in any focused window.
- Pixel-art "Clawd" animations change dynamically based on usage rate, with faster/busier animations at higher utilization—adding a playful, ambient feedback layer.
- The project supports both macOS (with LaunchAgent daemon) and Linux (systemd user service), with auto-detection scripts and venv setup for Python dependencies.
- At 144 GitHub stars and growing, it demonstrates developer appetite for physical interfaces to AI coding tools beyond screen-based UIs.

## Synthesis
Clawdmeter sits at an interesting intersection of several trends: the rise of AI coding agents, the maker/hardware hacking community, and the growing desire for ambient, glanceable interfaces that reduce screen dependence. It's a niche project—an ESP32 dashboard specifically for Claude Code—but it gestures toward something broader: what happens when AI tooling escapes the terminal and enters the physical world.

The device's architecture is relatively straightforward. A Node.js daemon reads Claude Code's OAuth token from the local keychain, polls Anthropic's API with a minimal (essentially free) one-token request, and extracts usage statistics from response headers like `anthropic-ratelimit-unified-5h-utilization`. These are packaged as JSON and written to the ESP32 over BLE. The firmware parses the payload and updates an LVGL-powered dashboard on a 2.16-inch 480×480 AMOLED display. Meanwhile, two physical buttons function independently as BLE HID keyboards, sending pre-configured keystrokes for Claude Code's voice mode and mode toggle.

The project's attention to user experience stands out. The splash screen plays pixel-art "Clawd" animations that get busier as usage climbs—a form of ambient feedback that makes rate-limit information glanceable rather than intrusive. The firmware auto-rotates animations within usage-rate groups every 20 seconds, so a long session doesn't mean staring at the same sprite. These are thoughtful touches that elevate the device from a simple data display to something approaching a companion object.

The dual-platform support (macOS via LaunchAgent, Linux via systemd) with contributed macOS porting by Chris Davidson suggests a project that has already attracted community contribution beyond the original author. The use of PlatformIO for firmware and bleak/httpx for the Python daemon follows modern embedded development patterns that make the project accessible to contributors.

Technically, the BLE protocol is clean: a custom GATT service alongside standard HID keyboard, with a simple JSON payload format. The hardware choice (Waveshare ESP32-S3-Touch-AMOLED-2.16) is well-documented with exact specifications. The README includes detailed setup instructions for both platforms, font recompilation notes using lv_font_conv, and clear documentation of button mappings and screen states.

What makes Clawdmeter noteworthy beyond its immediate utility is what it represents: the emergence of a hardware ecosystem around AI coding tools. As developers spend increasing time with coding agents, physical interfaces—buttons, dials, dashboards—may prove more ergonomic than keyboard shortcuts and terminal commands for frequently-used interactions. Clawdmeter is a small but evocative proof point that the interface between humans and AI coding agents is not yet settled, and that physical computing has a role to play in shaping it.

The main limitation is the narrow scope: this is a Claude Code-specific device that requires active Claude subscription and OAuth access. But the pattern—BLE-connected physical dashboard polling cloud API usage data—could easily generalize to other AI tools. The open-source nature and permissive structure make it a reference implementation as much as a finished product.
