# The Intl API: The best browser API you're not using

**Source**: https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/
**Date**: April 9, 2026
**Author**: Kilian Valkhof
**Keywords**: JavaScript, Intl API, browser APIs, i18n, formatting, performance, frontend

## Elevator pitch
Kilian Valkhof makes the case that modern frontend teams can replace a surprising amount of date, number, list, and text-formatting library baggage by leaning on the browser’s built-in Intl APIs.

## Takeaways
- Intl covers far more than translation: it provides native formatting for dates, times, relative time, durations, numbers, currencies, lists, pluralization, segmentation, and sorting.
- Because Intl is built into the browser, it reduces bundle weight and runtime parsing compared with common formatting libraries.
- Locale awareness matters even for single-language products because regional conventions for dates, numbers, and currencies still vary widely.
- The main performance pattern is to instantiate formatters once and reuse them rather than rebuilding them repeatedly in hot paths.
- Intl is a formatting layer, not a calculation layer, so developers still need separate logic for date diffs, unit conversion, and data wrangling.

## Synthesis
This article is a good reminder that a lot of frontend complexity persists by inertia. Developers reach for Moment, date-fns, or bespoke formatting utilities because those habits are old and familiar, not always because the browser is missing the capability. Kilian Valkhof’s argument is that the Intl family has quietly become rich enough to cover most mainstream formatting needs directly in the platform. That means less JavaScript shipped, less parsing overhead, and fewer dependencies maintained for problems the browser already knows how to solve.

The important nuance is that Intl is not just about translation. Even a product written entirely in English still serves users in different locales, each with different conventions for dates, decimals, currencies, and list formatting. When teams ignore that, they often build interfaces that feel subtly wrong or untrustworthy outside their home market. Intl solves a lot of that by making locale-sensitive output the default instead of an afterthought. In practice, that shifts internationalization from ‘big enterprise requirement’ to ‘basic frontend correctness.’

The article also exposes a common engineering tradeoff. The cost of native APIs is often up-front unfamiliarity rather than missing power. Intl has a broad surface area and many constructors, but the pattern is consistent: choose locale, choose options, create formatter, reuse it. That reuse point matters because the expensive part is initialization, not formatting itself. Once teams internalize that pattern, the API becomes much less intimidating and much more obviously useful in performance-sensitive code.

The broader lesson is about browser maturity. There are many places where frontend stacks still carry polyfills and utility libraries that made sense years ago but are no longer the best default. Intl is a concrete example of how platform capabilities have caught up. Teams that revisit those assumptions can simplify their bundles, reduce dependency risk, and get more correct user-facing behavior at the same time.
