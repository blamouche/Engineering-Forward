# GLM-5: From Vibe Coding to Agentic Engineering
**Source**: https://simonwillison.net/2026/Feb/11/glm-5/
**Date**: 2026-02-11
**Author**: Simon Willison
**Keywords**: open-source LLM, GLM-5, agentic engineering, model weights

## Elevator pitch
Z.ai publie GLM‑5 (754B, licence MIT) et en profite pour pousser le terme “agentic engineering” comme nouveau label pour les développeurs pro qui construisent avec des LLMs.

## Takeaways
- GLM‑5 est annoncé comme un très gros modèle open-source (754B paramètres) avec des poids massifs.
- La licence MIT le rend réutilisable commercialement (sous réserve des détails du release).
- “Agentic engineering” émerge comme vocabulaire pour désigner le métier de construire des systèmes avec agents/LLMs.
- Le post pointe des références (Karpathy, Addy Osmani) qui popularisent ce framing.
- Petit test qualitatif via OpenRouter (prompt SVG) pour donner une intuition de capacité.

## Synthesis
Ce billet très court sert surtout de “signal” dans la veille: Z.ai annonce GLM‑5, un modèle particulièrement volumineux (754B paramètres) et distribué à grande échelle, et Simon Willison note deux choses.

D’abord, l’ordre de grandeur: c’est un release qui se distingue par le poids des artefacts (poids/empreinte disque) et donc par ses implications pratiques — hébergement, téléchargement, déploiement, inférence — autant d’éléments qui conditionnent l’adoption réelle d’un modèle open-source. Ensuite, le framing culturel: Z.ai revendique et promeut le terme “agentic engineering” pour parler des pratiques pro autour des LLMs (au-delà du “vibe coding”).

L’intérêt n’est pas uniquement sémantique: nommer le métier, c’est souvent clarifier les compétences attendues (spécifier, orchestrer, mettre des garde-fous, évaluer, itérer, outiller) et déplacer l’attention du code “écrit à la main” vers les systèmes et les boucles de feedback.

Enfin, Willison illustre le tout par un micro-test (génération d’un SVG) via OpenRouter — un rappel utile: dans cette période, les releases se multiplient, et un sanity-check rapide, même anecdotique, aide à calibrer attentes et comparaisons.
