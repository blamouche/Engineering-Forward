# Browsers Treat Big Sites Differently
**Source**: https://denodell.com/blog/browsers-treat-big-sites-differently
**Date**: May 14, 2026
**Author**: Den Odell
**Keywords**: browser quirks, WebKit, Firefox about:compat, Chrome dominance, web standards, user agent spoofing, domain-specific fixes, browser market share, web compatibility, Internet Explorer parallel

## Elevator pitch
Safari and Firefox ship domain-specific rendering fixes for sites ranging from TikTok to SeatGuru — literal "if site == X, do Y" code baked into browser executables — while Chrome doesn't need a quirks file because the web is already built for Chrome.

## Takeaways
- Firefox's about:compat page lists site-specific interventions with toggle switches, injecting custom CSS/JS and changing user agent strings for broken sites
- Safari's Quirks.cpp contains thousands of lines of domain-checked fixes covering scrolling, touch events, viewport calculations, video PiP, and user agent spoofing
- Chrome doesn't maintain a quirks file because it doesn't need one: with 80%+ market share, developers build for Chrome first and Chrome's behavior becomes the de facto standard
- The pattern mirrors the IE era: when one browser dominates, site-specific workarounds concentrate in competing browsers rather than disappearing
- Developers who test primarily in Chrome are most exposed — their site may work not because of good code but because Chrome's behavior aligns with their assumptions

## Synthesis
Den Odell's May 14, 2026 piece explores a hidden layer of the modern web: the domain-specific fixes that Safari and Firefox ship to make popular sites work. The revelation that browsers contain literal "if site == X, do Y" logic — shipped to billions of devices — is the entry point to a deeper analysis of browser market dynamics and standards compliance.

Odell opens with concrete examples from WebKit's publicly available Quirks.cpp. Facebook, X (Twitter), and Reddit naively pause video elements that have scrolled out of viewport regardless of PiP mode — so Safari detects these domains and changes how Picture-in-Picture video is handled. TikTok shows "please upgrade your browser" messages, requiring a domain-specific fix. Instagram Reels resize erratically during playback. Netflix's "Episodes and Info" button dismisses popovers incorrectly. Amazon Prime Video blocks Safari users entirely. Each gets a targeted workaround compiled into the browser executable.

The SeatGuru example is particularly telling. A code comment reads: "FIXME: Remove this quirk if seatguru decides to adjust their site" — implying outreach was attempted and the site never fixed their code, so the browser fixed it for them, invisibly to users. The fix never shows up in error logs; there's no console warning. The browser silently compensates.

Firefox's equivalent is about:compat, a page listing site-specific interventions with toggle switches. Mozilla's WebCompat system injects custom CSS and JavaScript into specific domains, changes user agent strings for sites that sniff browsers incorrectly, and papers over bugs tracked in Bugzilla. Many interventions are user agent spoofs telling sites "yes, I'm Chrome" because those sites actively block or break on non-Chrome browsers.

This is where the analysis deepens. Odell argues these quirks aren't just fixing broken sites — they're compensating for Chrome's control over what "working" means. The pattern: Chrome ships a feature, developers adopt it because Chrome dominates, and other browsers either implement the feature or add site-specific quirks to paper over the difference. By the time Safari or Firefox catches up, the quirk has already shipped to millions.

WebKit literally ships with a fake Chrome user agent string ready to deploy when sites refuse to work otherwise: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36". Firefox does the same. This creates a feedback loop: developers build for Chrome, sites work best in Chrome, users who hit bugs elsewhere blame the browser and switch to Chrome, reinforcing its dominance.

The historical parallel is explicit and sobering. Odell draws a direct line to the Internet Explorer era of the 2000s, when developers built for IE, sites broke elsewhere, and standards compliance became secondary to just making things "work in IE." The hope a decade ago was that quirks would disappear as the web became more standards-compliant. They didn't disappear — they just moved to the browsers that aren't Chrome.

The practical advice is straightforward: test regularly in Firefox and Safari, not occasionally and not just before a big launch. If your domain appears in a quirks file, audit what was worked around. The quirks exist because developers didn't cross-test, and browser engineers somewhere solved a problem you didn't know you had.
