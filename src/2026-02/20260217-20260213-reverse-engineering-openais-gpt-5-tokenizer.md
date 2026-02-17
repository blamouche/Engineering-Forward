# Reverse-Engineering the OpenAI’s GPT-5 Tokenizer: What 200,000 Tokens Reveal About AEO/GEO
**Source**: https://metehan.ai/blog/reverse-engineering-the-gpt-5-tokenizer-aeo-geo/
**Date**: 2026-02-13
**Author**: Metehan Yesilyurt
**Keywords**: tokenization, tiktoken, o200k_base, multilinguality, AEO/GEO

## Elevator pitch
En disséquant le vocabulaire et la regex de o200k_base (200k tokens) via tiktoken, l’auteur montre comment les choix de tokenisation reflètent les priorités d’OpenAI (code, URLs, multilingue) et propose des implications concrètes pour le coût, la précision et l’optimisation de contenu pour les moteurs de réponse.

## Takeaways
- o200k_base double la taille de vocabulaire vs cl100k et améliore surtout le code, les URLs et les scripts non latins (pas l’anglais “prose”).
- La pré‑tokenisation regex est une partie majeure du comportement: o200k introduit un découpage camelCase/PascalCase (utile pour le code).
- Les “special tokens” racontent l’évolution produit: du simple endoftext à un protocole orienté tool‑use (o200k_harmony) avec de nombreux slots réservés.
- Le rang/ID BPE est un signal corrélé à la fréquence, mais pas une mesure de fréquence exacte (limites méthodologiques).
- Pour l’AEO/GEO: densité informationnelle par token, structure, attribution et gestion des URLs influencent ce qui tient dans les fenêtres de contexte et la fiabilité des citations.

## Synthesis
Le billet est une exploration “forensic” d’un composant souvent invisible: le tokenizer. Avant toute compréhension, le texte est compressé en IDs; cette couche conditionne coût, latence, performance multilingue et même certains types d’erreurs (p. ex. génération d’URLs plausibles mais fausses). En s’appuyant sur le caractère open source de tiktoken et la disponibilité publique du fichier o200k_base, l’auteur extrait et inspecte les ~200 000 tokens, ainsi que la configuration (regex, tokens spéciaux, mapping modèles).

Une première conclusion est que les gains ne sont pas uniformes: l’anglais “prose” bénéficie peu, alors que le code, les URLs et de nombreux scripts non latins gagnent fortement en compression (moins de tokens pour la même information). Cela suggère une priorisation de cas d’usage modernes: programmation, données structurées, web, et usage mondial.

Le cœur technique porte sur la regex de pré‑tokenisation. Là où les générations précédentes découpaient de façon assez grossière, o200k introduit des branches qui reconnaissent mieux les conventions de nommage logiciel. Par exemple, un identifiant camelCase peut être séparé en morceaux sémantiquement utiles avant même le BPE. Cette décision “en amont” façonne ensuite tout: coût par message, granularité d’apprentissage et facilité à manipuler du code.

Le billet analyse aussi l’“archéologie” des tokens spéciaux. Leur évolution illustre la transformation d’un modèle de texte en assistant structuré: fin de document, séparation prompt/réponse, tokens liés au fill‑in‑the‑middle (ère Codex), puis expansion orientée tool‑use (harmony) avec des emplacements réservés pour des outils futurs. L’idée implicite: le protocole (contrôle, délimiteurs, appels d’outils) devient presque aussi important que le vocabulaire.

Enfin, l’auteur translate ces observations vers l’Answer Engine Optimization / Generative Engine Optimization. Si la majorité du budget est consommée par le contexte récupéré (RAG), tout ce qui augmente la densité “chars/token” et réduit la surcharge de format aide à faire tenir plus de contenu utile. Il recommande des structures qui privilégient des réponses tôt, des listes, des chiffres en numéral, des abréviations communes, et des signaux d’attribution réguliers, tout en évitant les URLs longues ou la mise en forme inutile. Le texte reste prudent: comprendre le tokenizer ne suffit pas à expliquer le comportement du modèle, mais fournit un prisme actionnable sur les coûts et certaines limites structurelles.
