# A Visual Introduction to Machine Learning
**Source**: https://r2d3.us/visual-intro-to-machine-learning-part-1/
**Date**: 2026-03-20
**Author**: Stephanie Yee and Tony Chu
**Keywords**: machine learning, decision trees, visualization, education, overfitting, classification, interactive

## Elevator pitch
An interactive visual explanation of machine learning fundamentals using decision trees and a concrete real estate classification task, making abstract statistical concepts tangible through animated data visualization.

## Takeaways
- Uses the concrete task of classifying homes as San Francisco or New York to explain abstract ML concepts
- Decision trees work through sequential if-then statements that create data boundaries (split points)
- The piece explains overfitting clearly: models that memorize training data too precisely perform poorly on new examples
- Combines statistical explanation (Stephanie Yee, MS Statistics Stanford) with interaction design (Tony Chu, MFA interaction design)
- Interactive format enables readers to explore how different split points affect classification outcomes

## Synthesis
"A Visual Introduction to Machine Learning" by Stephanie Yee and Tony Chu has become one of the most widely cited educational resources in the field, and its longevity reflects a genuine pedagogical insight: the abstract statistical concepts underlying machine learning become intuitive when rendered as interactive visual experiences rather than mathematical notation.

The choice to explain machine learning through real estate classification—deciding whether a given home is in San Francisco or New York based on observable features—is pedagogically excellent. The domain is familiar, the features are concrete (elevation, price per square foot, number of bedrooms), and the classification question is legible to anyone who has considered the differences between the two cities. This familiarity allows readers to evaluate whether the model's decisions make intuitive sense, grounding the abstract statistics in embodied knowledge.

Decision trees are the ideal teaching vehicle for this piece. They implement a genuinely human-understandable decision process—a series of yes/no questions—that maps naturally to interactive visualization. Each split point in the tree is a threshold value on a single feature; the interactive format allows readers to see how moving that threshold changes which examples fall into which category. This immediate visual feedback makes the relationship between model parameters and classification behavior viscerally clear in a way that equations cannot achieve.

The overfitting section is where the educational value peaks. By showing a tree that achieves perfect accuracy on training data by memorizing each example—and then demonstrating its poor performance on new examples—the piece makes concrete a concept that confuses many beginning practitioners. "The model has learned to treat every detail in the training data as important, even details that turned out to be irrelevant" is a clearer explanation than any bias-variance decomposition formula.

The collaboration between a statistician and an interaction designer is the structural insight behind the piece's effectiveness. Statistical correctness without visual clarity produces textbooks; visual appeal without statistical rigor produces misleading infographics. The combination produces something genuinely educational at scale.
