# Razorpay Vulcan: India's First AI Payments Foundation Model
**Source**: https://linas.substack.com/p/weeklyfintechpulse413
**Date**: 2026-08-23
**Author**: Linas Beliunas
**Keywords**: razorpay, vulcan, foundation-model, payments, ai, india, fintech, upi

## Elevator pitch
Razorpay launched Vulcan, a transformer foundation model trained on 3 trillion data points from 4 billion payments that treats each transaction as an unordered set of fields — boosting payment success rates 8-10% and catching international card fraud 8x more often across 51,000+ businesses.

## Takeaways
- Vulcan is a non-LLM transformer foundation model trained on ~3 trillion data points from 4 billion payments, weighing ~3,000 signals per transaction
- Unlike sequence models (nuFormer, PRAGMA), Vulcan tokenizes each payment as an unordered set of fields, including missing ones — better suited to India's fragmented UPI/card/netbanking/cash landscape
- One self-supervised backbone now feeds routing, cross-merchant fraud detection, risk scoring, and checkout personalization, replacing siloed single-task models
- Beta results across 51,000+ businesses including Blinkit and redBus: payment success up 8-10%, international card fraud caught 8x more often, 100K-200K extra completed purchases per month
- Trained and hosted in India for RBI localization rules, turning compliance into a competitive filter foreign models cannot easily pass
- Confirms industry pattern: Stripe, Adyen, Mastercard, Nubank, and Revolut are all building domain foundation models on proprietary transaction data

## Synthesis
Razorpay's Vulcan represents a significant shift in how fintech companies approach AI: instead of renting general-purpose intelligence from LLM providers, data-rich payments companies are minting their own domain-specific foundation models. Vulcan is trained on roughly 3 trillion data points extracted from 4 billion payments, weighing approximately 3,000 signals per transaction. Crucially, it is not a language model — it treats each payment as an unordered set of fields, tokenizing even missing ones, which makes it better suited to India's messy payment landscape where UPI apps, cards, netbanking, and cash-on-delivery coexist.

The architectural choice is deliberate. Sequence models like Nubank's nuFormer and Revolut's PRAGMA are built for user histories — ordered sequences of behavior. India's payment environment is less sequential and more categorical, so an unordered-set tokenizer fits better. One self-supervised backbone now serves routing, fraud detection, risk scoring, and checkout personalization, eliminating the need for separate single-task models.

The beta numbers across 51,000+ businesses are compelling: 8-10% payment success rate improvements, 8x better international card fraud detection, and 100,000-200,000 additional completed purchases monthly just from showing shoppers their preferred UPI app. In Indian e-commerce where a failed payment sends cash-first shoppers back to cash, these gains are worth more than most product launches. The network effect compounds — patterns invisible to any single merchant (like one stolen card hitting unrelated sellers) become visible across the network.

Vulcan also turns RBI's data localization mandate into a competitive advantage. Being trained and hosted in India means foreign models face a compliance barrier they cannot easily cross. Looking ahead, the key questions are whether gains hold outside the curated beta and whether Razorpay extends the backbone into lending and credit risk where the real margin lives. The second-order effect is agentic commerce: when AI agents initiate payments, they will route through whichever rail decides fastest and fails least.