# Clawdmeter: ESP32 desk dashboard that shows Claude Code usage
**Source**: https://github.com/HermannBjorgvin/Clawdmeter
**Date**: Unknown
**Author**: HermannBjorgvin
**Keywords**: ESP32, Claude Code, BLE, dashboard, IoT, hardware, usage monitoring

## Elevator pitch
A physical ESP32 desktop dashboard that tracks Claude Code usage in real-time via Bluetooth and displays it on a 2.16-inch AMOLED screen with pixel-art Clawd animations.

## Takeaways
- Pairs with a laptop over Bluetooth Low Energy (BLE) to display Claude Code session and weekly utilization rates
- Features pixel-art Clawd animations from claudepix that change intensity based on usage rate
- Includes physical buttons that send Space (voice mode push-to-talk) and Shift+Tab (mode toggle) as BLE HID keyboard input
- Runs a Python daemon that polls Claude API usage via the OAuth token and pushes data to the ESP32
- Open-source with install scripts for both macOS and Linux, including LaunchAgent/systemd support

## Synthesis
Clawdmeter is a hardware companion for heavy Claude Code users, built on a Waveshare ESP32-S3-Touch-AMOLED-2.16 board. It connects to the host machine over Bluetooth Low Energy and shows real-time session and weekly usage percentages on a high-resolution AMOLED screen.

The device has three physical buttons: left sends Space (voice mode push-to-talk), right sends Shift+Tab (mode toggle) as BLE HID keyboard reports, and the middle button cycles through display screens. The splash screen features animated pixel-art Clawd sprites from the claudepix library, which become more active as usage rates increase.

On the host side, a Python daemon reads the Claude OAuth token, makes a minimal API call to retrieve rate-limit headers (session and weekly utilization), and pushes the data to the ESP32 over BLE GATT characteristics. Install scripts for macOS (homebrew-compatible, with LaunchAgent) and Linux (systemd user unit) handle setup. The project demonstrates the growing ecosystem of physical companion devices for AI coding tools, bridging the gap between terminal-first workflows and tangible feedback.
