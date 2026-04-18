# AI Installer & CLI – AuthKit – WorkOS Docs

**Source**: https://workos.com/docs/authkit/cli-installer
**Date**: April 19, 2026
**Author**: Unknown
**Keywords**: workos, installer, authkit, docs

## Elevator pitch
Integrate AuthKit with one command, manage resources, provision environments, and equip your coding agents — all from the WorkOS CLI

## Takeaways
- Integrate AuthKit with one command, manage resources, provision environments, and equip your coding agents — all from the WorkOS CLI.
- AI Installer What the installer handles Supported frameworks How the installer works Install options  Workflow commands Declarative provisioning with seed Other workflow commands  Troubleshooting The installer didn’t detect my framework Build validation failed I want to see what changed Something else went wrong  The WorkOS CLI is a comprehensive tool for integrating and managing WorkOS from the terminal.
- Its headline feature is the AI Installer – run one command and it handles framework detection, SDK installation, route creation, environment setup, and build validation.
- Beyond the installer, the CLI also manages resources, provisions environments, and equips your coding agents with WorkOS knowledge.
- Run one command, the CLI handles the rest.

## Synthesis
Integrate AuthKit with one command, manage resources, provision environments, and equip your coding agents — all from the WorkOS CLI. AI Installer What the installer handles Supported frameworks How the installer works Install options  Workflow commands Declarative provisioning with seed Other workflow commands  Troubleshooting The installer didn’t detect my framework Build validation failed I want to see what changed Something else went wrong  The WorkOS CLI is a comprehensive tool for integrating and managing WorkOS from the terminal. Its headline feature is the AI Installer – run one command and it handles framework detection, SDK installation, route creation, environment setup, and build validation. Beyond the installer, the CLI also manages resources, provisions environments, and equips your coding agents with WorkOS knowledge. Run one command, the CLI handles the rest. Your app goes from zero auth to full AuthKit integration in about two minutes. The installer takes care of everything you would normally do manually:  Detects your framework – Identifies your framework and version from your project’s dependencies and file structure  Authenticates your account – Opens your browser for secure WorkOS sign-in  Configures your dashboard – Sets redirect URIs, CORS origins, and homepage URL automatically  Installs the right SDK – Adds the correct AuthKit package for your framework  Analyzes your project – Reads your project structure to understand routing, existing middleware, and configuration  Creates routes and middleware – Writes OAuth callback routes, auth middleware/proxy, and provider wrappers  Sets up environment variables – Writes API keys and configuration to .env.local  Validates the integration – Runs your build to verify everything compiles without errors  The installer understands framework-specific nuances – like Next.js App Router vs Pages Router, Vite vs Create React App, and React Router nuances – and generates the appropriate code for your setup. If you have existing middleware or configuration, it composes with it rather than replacing it. The CLI uses an AI agent with restricted permissions to integrate AuthKit into your project:  Local analysis – The agent reads your project files locally to detect frameworks and understand your project structure. Restricted execution – The agent can only run a limited set of commands: package installation, builds, type-checking, and formatting.
