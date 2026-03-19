# Vite 8.0 is out!
**Source**: https://vite.dev/blog/announcing-vite8
**Date**: 2026-03-12
**Author**: Vite Team (sapphi-red)
**Keywords**: Vite, Rolldown, Rust bundler, build performance, Rollup, esbuild, Module Federation, developer tools, frontend build

## Elevator pitch
Vite 8 replaces the dual esbuild/Rollup bundler system with Rolldown—a unified Rust-based bundler delivering 10-30x faster builds, with Linear dropping from 46s to 6s and Beehiiv achieving 64% build time reduction.

## Takeaways
- Core change: replaces the dual-bundler system (esbuild for dev, Rollup for production) with Rolldown, a unified Rust-based bundler maintaining Rollup plugin ecosystem compatibility.
- Performance: 10-30x faster builds; Linear: 46s → 6s; Beehiiv: 64% improvement.
- The dual-bundler problem: esbuild/Rollup inconsistencies created edge cases in module handling that accumulated into significant maintenance debt.
- Rolldown's three pillars: performance (Rust), compatibility (Rollup plugin ecosystem), new capabilities (module-level persistent caching, Module Federation).
- New features: integrated Devtools, TypeScript `paths` support, automatic `emitDecoratorMetadata` handling, browser console forwarding to CLI.
- Tradeoff: Vite 8 is ~15MB larger than v7 due to lightningcss and Rolldown binary inclusion.

## Synthesis
The dual-bundler architecture was a pragmatic choice when Vite launched: esbuild's Rust/Go performance was necessary for the development experience, but Rollup's mature plugin ecosystem was necessary for production builds. Over time, the inconsistencies between how two different bundlers handle edge cases accumulated into a maintenance problem that limited Vite's ability to add new capabilities without introducing subtle behavioral differences between development and production.

Rolldown solves this architecturally by being a Rust-native bundler with explicit Rollup compatibility as a design goal. Rather than maintaining two codepaths, the framework maintains one—with consistent behavior across dev and prod, and a plugin API that existing Rollup plugins can target without modification. The 10-30x performance improvement is substantial but secondary to the architectural correctness benefit.

The 46s → 6s Linear result represents a real-world threshold crossing. Build times over 30 seconds are disruptive to development flow—they're long enough that developers stop waiting and switch context, making incremental development feel slow. Six seconds is fast enough to run without breaking focus. This threshold difference is more impactful than the raw ratio suggests.

Module Federation support is significant for enterprise adoption. Large organizations increasingly build micro-frontend architectures where different teams own different portions of the UI, deployed independently and composed at runtime. Module Federation—popularized by Webpack 5—enables this pattern. Vite lacking native support was a blocker for teams wanting Vite's development experience with enterprise micro-frontend architectures; Vite 8 removes that blocker.
