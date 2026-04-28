# How Stripe Detects Fraudulent Transactions Within 100 ms
**Source**: https://blog.bytebytego.com/p/how-stripe-detects-fraudulent-transactions
**Date**: Unknown
**Author**: ByteByteGo
**Keywords**: stripe, detects, fraudulent, transactions, within

## Elevator pitch
Most teams pick a search provider by running a few test queries and hoping for the best – a recipe for hallucinations and unpredictable failures.

## Takeaways
- Most teams pick a search provider by running a few test queries and hoping for the best – a recipe for hallucinations and unpredictable…
- How to build a golden set of queries that predicts real-world performance
- Every time you buy something online from a Stripe-powered business, a machine learning model evaluates over 1,000 signals about your transaction and decides in…
- Across billions of legitimate payments, it reaches the correct verdict 99.9% of the time.
- The architecture has been overhauled multiple times, and one of the most important upgrades required removing a component the team knew was actively improving…

## Synthesis
Most teams pick a search provider by running a few test queries and hoping for the best – a recipe for hallucinations and unpredictable failures. This technical guide from You.com gives you access to an exact framework to evaluate AI search and retrieval.

How to build a golden set of queries that predicts real-world performance

Every time you buy something online from a Stripe-powered business, a machine learning model evaluates over 1,000 signals about your transaction and decides in under 100 milliseconds whether to let it through.

Across billions of legitimate payments, it reaches the correct verdict 99.9% of the time. The system that delivers those numbers, however, looks entirely different from what Stripe originally built.

The architecture has been overhauled multiple times, and one of the most important upgrades required removing a component the team knew was actively improving accuracy, because keeping it was holding back everything else the team wanted to do.

For reference, online payment fraud occurs in roughly 1 out of every 1,000 transactions. That rarity makes fraud detection a difficult machine learning problem because the system has to surface a small number of fraudulent payments from a massive volume of legitimate ones, and it has to do this quickly and cheaply on every single transaction.

In this article, we will look at how Stripe’s Radar does this effectively and the architectural decisions the team took while building it.

Disclaimer: This post is based on publicly shared details from the Stripe Engineering Team. Please comment if you notice any inaccuracies.
