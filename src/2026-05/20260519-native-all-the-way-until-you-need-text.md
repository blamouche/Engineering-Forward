# Native all the way, until you need text

**Source:** https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text
**Date:** 2026-05-17

## Summary

Artem Loenko, a native macOS/iOS developer of nearly 20 years, shares a candid account of attempting to build a chat app with Markdown support in pure Swift/SwiftUI — and ultimately finding Electron to be the superior choice. His journey:

- SwiftUI: jumpy scrolling, lags, inability to select entire Markdown document by design
- NSTextView + TextKit 2: loses SwiftUI testing/performance benefits, CPU spikes during text streaming
- NSCollectionView: cells blink by design
- Pure TextKit 2: streaming is terrible, doesn't play well with modern tools
- WebKit: works reasonably well for Markdown rendering
- Electron: text operations, Markdown rendering, good typography all work out of the box with better performance than his pure TextKit 2 implementation

His conclusion: For chat-heavy apps with rich text and flexible typography, Apple's native SDKs are not an advantage — they're constraints. This explains why most modern chat-heavy apps are web-based.

**Tags:** #swiftui #appkit #electron #mobile-dev #rich-text #markdown
