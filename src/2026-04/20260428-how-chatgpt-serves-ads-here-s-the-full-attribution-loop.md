# How ChatGPT serves ads. Here's the full attribution loop.

**Source**: https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop
**Date**: April 28, 2026
**Author**: Unknown
**Keywords**: ChatGPT ads, attribution, tracking, adtech, OpenAI

## Elevator pitch
This reverse-engineering report suggests OpenAI's ad system is not a light sponsorship overlay but a fairly standard performance-marketing stack, with in-stream ad objects, encrypted click tokens, and merchant-side browser tracking stitched into a closed attribution loop.

## Takeaways
- The observed ChatGPT response stream contains structured ad units injected alongside ordinary model output.
- OpenAI appears to use multiple encrypted tokens to connect ad delivery, click integrity, and downstream attribution.
- Merchant pages load an OpenAI tracking SDK that stores attribution state in first-party cookies and posts event data back to OpenAI.
- Opening ads inside ChatGPT's webview increases OpenAI's visibility into post-click behavior beyond the merchant pixel alone.
- The article frames ChatGPT advertising as converging on familiar adtech mechanics rather than inventing a radically new measurement model.

## Synthesis
This article offers an observational teardown of what OpenAI's emerging advertising stack may look like in production. Based on captured traffic from a consented research setup, it describes two linked components: structured advertisement objects inserted directly into ChatGPT's server-sent event stream, and a merchant-side tracking SDK that reports subsequent user actions back to OpenAI. The reporting is technical rather than normative, but the practical implication is clear. Advertising inside conversational interfaces is quickly adopting the same attribution logic that already governs much of performance marketing on the web.

The first part of the system is ad delivery. According to the article, the model response stream can include typed ad payloads that specify the advertiser, creative, click target, and several encrypted tokens. That matters because it suggests ads are not being improvised by the model in free text. They are likely being inserted as a separate, structured layer in the response pipeline. This architectural distinction is important for both policy and product analysis. It implies an ad system with its own schemas, account identifiers, and integrity controls operating alongside generation.

The second part is attribution. The article argues that click URLs carry multiple Fernet-encrypted parameters, and that merchant pages load an OpenAI SDK that stores at least one of those values in a first-party cookie before sending event data back to OpenAI. If accurate, that means OpenAI can connect conversation context, click events, and downstream merchant activity in a way that looks familiar to existing ad platforms. The use of ChatGPT's in-app webview could strengthen that loop by giving OpenAI additional visibility into what happens after a user taps an ad.

What makes the piece notable is not only the technical detail but the market signal. Many early discussions of conversational advertising assumed either crude sponsorship or a radically new commerce flow. This report points instead to continuity with incumbent adtech: contextual selection, click identifiers, browser-side measurement, and merchant instrumentation. The interface changes, but the commercial logic remains recognizable. That could make the system easier for advertisers to adopt because it maps onto established attribution expectations.

Overall, the article suggests that conversational AI monetization may develop through familiar infrastructure rather than through a clean break from web advertising. If the findings hold more broadly, then questions about privacy, consent, measurement, and market power in chat interfaces will increasingly resemble the debates already associated with ad platforms, just translated into a conversational surface where the recommendation and the ad can feel much closer together.