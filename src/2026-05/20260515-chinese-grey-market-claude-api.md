# Chinese Grey Market Sells Claude API Access at 90% Off Through Proxy Networks That Harvest User Data
**Source**: https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data
**Date**: 2026-05-15
**Author**: Unknown
**Keywords**: Claude API, grey market, China, proxy networks, data harvesting, model substitution, stolen credentials, AI security, API abuse

## Elevator pitch
Chinese grey-market operators are selling Claude API access at 90% discounts through "transfer station" proxy networks that harvest user prompts and outputs for resale as AI training data, using stolen credentials and model substitution.

## Takeaways
- Chinese grey-market vendors sell Claude API access at up to 90% off official pricing through proxy-based "transfer station" networks that intercept all traffic.
- The proxy networks harvest users' prompts and model outputs, repackaging and reselling them as AI training data to third parties — turning users into unwitting data suppliers.
- Operators use a combination of stolen API credentials and model substitution, meaning users may not actually be receiving Claude responses but cheaper alternative models.
- The scheme represents a significant security risk for businesses that use these grey-market services, as sensitive data passes through uncontrolled intermediary servers.
- This grey market highlights the growing gap between official AI API pricing and the underground economy's ability to undercut it through credential theft and data monetization.

## Synthesis
Tom's Hardware reports on an emerging grey market for Claude API access operating out of China, where intermediaries known as "transfer stations" act as proxy networks offering API access at discounts of up to 90% off Anthropic's official pricing. These operations function as man-in-the-middle services: users' API requests pass through the transfer station servers, which forward them to Claude's API (or substitute cheaper models), then return the responses to the user.

The business model is multilayered and exploitative. The operators acquire Claude API credentials through theft or fraudulent accounts. They then resell access at steep discounts, but the real monetization comes from harvesting all traffic passing through their proxies. User prompts and AI outputs — potentially containing sensitive business data, proprietary code, personal information, and strategic documents — are captured, aggregated, and resold as AI training data to other parties. Users of these services are unknowingly providing free training data to unknown third parties.

Compounding the security concerns is the practice of model substitution. Users believing they are receiving Claude's frontier model responses may actually be getting outputs from cheaper, less capable models with different safety characteristics and output quality. This undermines any reliability assumptions businesses might make about the AI's performance.

The existence of this grey market at 90% discounts reveals broader tensions in the AI API economy. The official pricing creates significant arbitrage opportunities, and the underground economy has developed sophisticated infrastructure to exploit them — combining credential theft, proxy networks, and data monetization into a single operation. For enterprises, the lesson is clear: discounted API access through unofficial channels carries hidden costs that far exceed the apparent savings.
