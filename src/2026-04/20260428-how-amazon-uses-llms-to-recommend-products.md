# How Amazon Uses LLMs to Recommend Products
**Source**: https://blog.bytebytego.com/p/how-amazon-uses-llms-to-recommend
**Date**: Unknown
**Author**: ByteByteGo
**Keywords**: amazon, uses, llms, recommend, products

## Elevator pitch
Most AI agents don’t fail because the model is bad.

## Takeaways
- Most AI agents don’t fail because the model is bad.
- Simba Khadder, Head of Engineering at Redis, lays out a 4 pillar framework for building context systems that hold up in production—plus an architectural…
- Search “shoes for pregnant women” on Amazon, and the best results you get might be slip-resistant shoes.
- In other words, there is zero keyword overlap between the query and the product.
- Traditional recommendation systems match text to text and purchase history to purchase history.

## Synthesis
Most AI agents don’t fail because the model is bad. They fail because the model doesn’t have the proper infrastructure to reason well.

Simba Khadder, Head of Engineering at Redis, lays out a 4 pillar framework for building context systems that hold up in production—plus an architectural self-audit checklist you can run against your stack today.

Search “shoes for pregnant women” on Amazon, and the best results you get might be slip-resistant shoes. This is even though the word “pregnant” appears nowhere in those product listings.

In other words, there is zero keyword overlap between the query and the product. The search engine has to reason that pregnant women need stability, that stability means slip-resistance, and that slip-resistant shoes are the right match.

Traditional recommendation systems match text to text and purchase history to purchase history. They handle keyword overlap quite well. However, when a shopper’s intent requires a reasoning step that lives entirely in human common sense, those systems hit a wall.

Amazon’s search team recognized this blind spot and built a commonsense knowledge graph called COSMO that teaches the recommendation engine to think the way a human shopper would.

In this article, we will look at how COSMO works and the challenges the engineering team faced.

Disclaimer: This post is based on publicly shared details from the Amazon Engineering Team. Please comment if you notice any inaccuracies.
