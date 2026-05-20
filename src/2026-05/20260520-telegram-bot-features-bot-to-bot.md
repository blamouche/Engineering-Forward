# Telegram Bot Features (Bot-to-Bot Communication)
**Source**: https://core.telegram.org/bots/features#bot-to-bot-communication
**Date**: Unknown
**Author**: Telegram
**Keywords**: Telegram bots, bot-to-bot communication, Bot API, mini apps, monetization, Telegram Stars, inline mode, deep linking, managed bots, guest bots

## Elevator pitch
Telegram has evolved its bot platform into a comprehensive ecosystem featuring bot-to-bot communication, managed bots, guest bots, a full monetization stack (Stars, subscriptions, ads revenue sharing), and Mini Apps reaching 500M+ monthly users — positioning bots as first-class applications within the messenger.

## Takeaways
- Bot-to-bot communication is now a documented feature alongside managed bots and guest bots, signaling Telegram's move toward inter-bot ecosystems where bots can interact with each other, not just with humans
- Telegram Stars power all digital transactions: users buy Stars via Apple/Google, bots use them to increase message limits, send gifts, or convert to Toncoin rewards — creating a closed-loop economy
- Mini Apps have become a major platform: 500M+ monthly users interact with them, they support full-screen mode, home screen shortcuts, customizable loading screens, and are featured in an in-app Mini App Store
- Bots can now handle business accounts, post paid media (users pay Stars to unlock), offer subscription plans with multiple tiers, and participate in 50% revenue sharing from Telegram Ads
- The platform provides deep integration hooks: inline mode (from any chat), attachment menu, deep linking with parameter passing, chat/user selection interfaces, and Web Apps that can access device features like QR codes and biometrics

## Synthesis
The Telegram Bot Features page, while a reference document rather than a narrative article, reveals the remarkable evolution of Telegram's bot platform into something approaching an operating system for lightweight applications. What started as simple command-response bots has become a multi-layered ecosystem spanning communication, commerce, and content.

The most significant architectural shift is the emergence of inter-bot primitives. The documentation now includes sections for "Bot-to-Bot Communication," "Managed Bots," and "Guest Bots" — all pointing toward a future where bots form mesh networks rather than just hub-and-spoke relationships with human users. Managed bots suggest administrative hierarchies where one bot can control others; guest bots imply cross-domain bot interaction within shared contexts. While the specific API details for these features are still evolving, the taxonomy itself signals Telegram's intent to treat bots as composable components.

The monetization infrastructure is equally mature. Telegram Stars function as the platform's universal micropayment currency, creating a closed loop: users purchase Stars through in-app purchases (with Apple/Google taking their cut), then spend Stars on digital products, paid media, or subscription plans. Bots receive Stars and can either reinvest them (boosting message limits, sending gifts to users) or cash out via Toncoin rewards. The 50% ad revenue sharing model extends this further, letting popular bots earn from Telegram's ad network. For developers, this means a bot can generate revenue through multiple channels without needing to integrate external payment processors.

The Mini Apps ecosystem is the third pillar. With 500 million monthly active users (out of Telegram's 950 million total), Mini Apps have achieved critical mass. The platform provides deep device integration — theme awareness, QR code scanning, biometric authentication, geolocation — plus distribution through the Mini App Store, home screen shortcuts, and inline mode (launching from any chat's message field). The full-screen mode and customizable loading screens push Mini Apps toward feeling like native applications rather than embedded web views.

For developers, the feature surface is extensive: inline queries let bots respond from any chat without being added; deep linking passes parameters at startup (useful for auth tokens or referral tracking); attachment menu integration puts bots one tap away in every conversation; chat/user selection interfaces create admin workflows without typing; and Web Apps provide the escape hatch for any custom JavaScript interface. Commands, keyboards, inline keyboards, and menu buttons give developers a gradient of UI complexity — from simple slash commands to full interactive applications.

The platform's evolution reflects a philosophy of "bots as native Telegram citizens" rather than second-class API consumers. By combining communication features (bot-to-bot), distribution (Mini App Store, inline mode), monetization (Stars, subscriptions, ads), and rich interfaces (Mini Apps, keyboards, deep linking), Telegram has built what is essentially an application platform that happens to live inside a messenger.
