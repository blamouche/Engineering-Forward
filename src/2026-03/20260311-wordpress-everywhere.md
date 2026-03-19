# WordPress Everywhere
**Source**: https://ma.tt/2026/03/wordpress-everywhere/
**Date**: 2026-03-11
**Author**: Matt Mullenweg
**Keywords**: WordPress, WebAssembly, WASM, browser-based, digital ownership, open source, my.wordpress.net, SQLite, MariaDB

## Elevator pitch
my.wordpress.net uses WebAssembly to spin up a full WordPress installation inside any browser in 30 seconds, moving toward Mullenweg's vision of "billions of WordPresses" where everyone owns a piece of the internet.

## Takeaways
- WebAssembly enables spinning up a web server, database (SQLite or MariaDB), and full WordPress installation inside any browser in about 30 seconds.
- my.wordpress.net is the new service enabling browser-based WordPress without traditional hosting requirements.
- Scale vision: from "millions of WordPresses in the world to billions," driven by easier deployment and AI integration.
- Long-term commitment: backward compatibility, data portability, and 100-year plans on WordPress.com differentiate from lock-in competitors.
- Upcoming features: peer-to-peer sync, version control integration, and cloud publishing capabilities.
- Digital ownership philosophy: "Everyone will have a domain and a WordPress. A part of the internet that you own."

## Synthesis
The WASM-powered browser WordPress is a significant technical achievement that changes the deployment economics. Hosting a WordPress site requires a server, a domain, and ongoing maintenance—a meaningful barrier for personal publishing. Running WordPress in a browser requires none of those things for initial use. The path from "I want to try WordPress" to "I have a working WordPress" collapses from days (set up hosting, install WordPress, configure domain) to 30 seconds.

The digital ownership framing connects to a broader concern about the internet's architecture. The web has consolidated significantly: most publishing happens on platforms owned by a small number of companies, with correspondingly centralized control over content distribution, moderation, and monetization. Mullenweg's vision of browser-based personal WordPress is a technical argument for the original web architecture—distributed publishing with individual ownership.

The 100-year compatibility commitment is an unusual and potentially valuable differentiator. Most software products implicitly prioritize current users and current features; backward compatibility creates constraints on future development and is usually sacrificed when it creates friction. Explicitly committing to long-term compatibility addresses a real concern for anyone building on WordPress: will the investment in content, customization, and integration survive the next platform pivot?

The AI integration mention is brief but significant. WordPress sitting inside browsers as a lightweight, always-available publication substrate could become infrastructure for AI-assisted content workflows—the kind of output layer that complements tools like Proof for AI-human collaborative writing. The combination of local-first architecture and AI integration is a coherent vision for personal publishing infrastructure in an AI-era internet.
