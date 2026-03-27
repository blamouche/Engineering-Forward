# Gridland: Terminal apps that run anywhere
**Source**: https://github.com/thoughtfulllc/gridland
**Date**: Unknown
**Author**: thoughtfulllc (Chris Roth & Jessica Cheng)
**Keywords**: TUI, React, terminal apps, OpenTUI, Bun

## Elevator pitch
Gridland is a React‑based framework for building terminal apps that run both in the browser and in the terminal, powered by the OpenTUI rendering engine.

## Takeaways
- Build terminal UIs with React and run them in browser or terminal.
- Uses OpenTUI as the rendering engine with a web plugin for Vite/Next.
- Includes shadcn‑style UI components and demo packages.
- Supports Docker sandbox execution and compilation to standalone binaries.
- Development uses Bun, but production can be a no‑runtime binary.

## Synthesis
Gridland is an open‑source framework aimed at developers who want to build terminal user interfaces with modern React tooling. Its core pitch is portability: the same UI can run in a browser or in a terminal, which can be useful for tools that need both CLI and web surfaces. The project is built on the OpenTUI rendering engine and provides a set of packages for web integration, utilities, UI components, and testing.

The repo positions Gridland as a full stack for terminal apps. You can scaffold a new project via a Bun‑based CLI, run demos in the terminal, and integrate with Vite or Next.js through provided plugins. Components are distributed through a shadcn‑style registry so teams can copy component code into their own project and customize freely. This echoes the modern “own your components” philosophy common in web UI ecosystems.

For development, Gridland currently relies on Bun, but the build process can output a standalone binary, allowing distribution without requiring Bun or Node for end users. The project also includes a containerized runner for executing apps in isolated Docker environments, which can be useful for demos, sandboxing, or CI validation.

In practice, Gridland aims to bridge the gap between web UI ergonomics and terminal UX. By leveraging React and a shared rendering engine, it lets developers reuse patterns, tooling, and component libraries across different interfaces. The value proposition is less about inventing a new UI paradigm and more about reducing friction for teams building modern terminal tools that need to ship across environments.
