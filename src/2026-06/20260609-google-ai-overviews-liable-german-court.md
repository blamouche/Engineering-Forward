# Landmark German Ruling: Google Is Liable for False AI Overview Answers
**Source**: https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/
**Date**: 2026-06-09
**Author**: The Decoder
**Keywords**: Google, AI Overviews, liability, German court, Munich, defamation, AI-generated content, Digital Services Act, search engine liability, free speech

## Elevator pitch
A German regional court in Munich ruled that Google is directly liable for false claims in its AI-generated search overviews, treating them as Google's own content rather than third-party search results—a landmark decision that rejects the liability shield traditional search engines have enjoyed.

## Takeaways
- The Regional Court of Munich issued a temporary injunction (case no. 26 O 869/26) classifying Google as a direct infringer because AI overviews generate "independent, new, and substantive statements" rather than listing search results
- Google's AI overviews had falsely linked two Munich-based publishers to scams, subscription traps, and shady business practices—claims that appeared in none of the linked sources
- The court rejected Google's "users can check for themselves" defense, noting that AI overviews are "understandable on their own" with no reference to unreliable content; studies show only 1% of users click source links from AI overviews
- AI-generated opinions receive less free speech protection: an AI's opinion is "the result of an algorithm," not "the expression of an acquired conviction"—Google's business interests took a back seat to plaintiffs' privacy rights
- An Oumi analysis found Gemini 3 AI Overviews answer correctly 91% of the time—but at Google's scale, that still means millions of wrong answers per hour, and 56% of correct answers couldn't be backed up by cited sources

## Synthesis
The Munich court's ruling is a landmark in AI liability law. The core legal reasoning is that AI overviews are fundamentally different from traditional search results. A regular search engine points to outside websites and merely makes third-party content findable, which gave search engines limited liability under German case law. But AI overviews generate new content by evaluating and combining information from multiple sources "in its own words and according to its own structure." The court called these "the defendant's own statements" because Google built the AI, offers it to users, and "alone has influence over the AI's offering and the algorithms with which the AI operates."

The "users can verify" defense was central to Google's argument and the court's rejection is sweeping. Google claimed users knew AI-generated information shouldn't be blindly trusted and could check linked sources themselves. The court found that the possibility of disproving a statement through further research doesn't exempt the speaker from liability, drawing a parallel to press law where publishers are liable for teasers that are understandable on their own—even if readers never read the full article. Google's own argument would "significantly diminish" the feature's benefit if the overview were "generally recognized as unreliable."

The free speech ruling has broader implications. The court determined that an AI's opinion is "not the expression of an acquired conviction of the persons expressing it, but the result of an algorithm." Offering AI-powered research is "above all an expression of Google's business activities" and "at most a secondary expression of an interest in being able to freely express one's opinion." This hierarchy—business interests below privacy rights, algorithmic output below human conviction—could shape how other jurisdictions treat AI-generated content.

For the engineering community, the 91% accuracy statistic from Oumi's analysis is the most actionable data point. It sounds high, but at Google's query volume it translates to millions of incorrect answers every hour. More concerning: 56% of correct answers couldn't be backed up by the sources Google linked, meaning the AI is generating claims whose origins users can't trace. If this ruling's reasoning gains international traction, every AI provider whose systems paraphrase web content—ChatGPT, Claude, Perplexity—faces similar liability exposure. The ruling potentially reshapes the product architecture of AI search: providers may need to ensure generated claims are directly traceable to cited sources, or accept publisher-level liability for defamatory output.