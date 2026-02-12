# Claude Opus 4.6
**Source**: https://www.anthropic.com/news/claude-opus-4-6?utm_source=it&utm_medium=email&utm_campaign=model-launch&utm_term=api_users
**Date**: Unknown
**Author**: Unknown
**Keywords**: LLMs, agentic coding, long-context, benchmarks, safety, API

## Elevator pitch
Anthropic annonce Claude Opus 4.6, un modèle orienté « agentic work » (planification, codebases larges, revues/débogage) avec une fenêtre de contexte 1M tokens (beta) et des améliorations produit/API (effort controls, compaction, adaptive thinking).

## Takeaways
- Focus explicite sur les tâches longues et complexes (agentic coding) : meilleure planification, moins d’erreurs, meilleure endurance.
- Ajout d’un contexte 1M tokens (beta) pour Opus (avec tarification premium au-delà de 200k tokens).
- Mise en avant de performances « SOTA » sur plusieurs benchmarks (Terminal-Bench, HLE, etc.) et sur des tâches de knowledge work.
- Renforcement de la boîte à outils développeurs côté API : compaction, adaptive thinking, effort controls.
- Message marketing « safety non dégradée » : profil global comparable ou meilleur que la génération précédente selon leurs évaluations.

## Synthesis
Ce billet de lancement positionne Claude Opus 4.6 comme une itération pensée pour les usages où les modèles tombent souvent : les projets de code réels, les tâches multi-étapes, et les sessions longues où il faut maintenir une stratégie plutôt que répondre au coup par coup. Anthropic insiste sur une amélioration qualitative de la planification et de la « discipline » du modèle : Opus 4.6 passerait plus vite sur les étapes triviales, consacrerait davantage d’attention aux points durs, et revisiterait plus fréquemment son raisonnement avant de conclure. L’idée est de réduire les retours en arrière coûteux et les erreurs en chaîne, très visibles dans les workflows agentiques (tests, refactors, navigation de codebases, revue).

Le marqueur produit le plus notable est l’introduction d’une fenêtre de contexte de 1 million de tokens (beta) — une première pour la classe Opus — présentée comme un levier direct contre la dégradation de performance liée à la longueur des conversations (« context rot »). Anthropic utilise des benchmarks de type needle-in-a-haystack pour argumenter que l’augmentation de contexte n’est pas seulement quantitative : la capacité à récupérer des détails « enfouis » resterait élevée. Cette promesse vise des scénarios où l’agent doit rester cohérent sur des centaines de milliers de tokens, p.ex. un audit ou une migration sur un gros monorepo.

Le billet sert aussi de vitrine pour un ensemble de primitives API qui encadrent mieux l’usage réel : (1) la compaction, pour permettre au modèle de résumer lui‑même son contexte quand on approche des limites ; (2) l’adaptive thinking, pour décider quand investir du raisonnement étendu ; (3) des niveaux d’effort explicites, qui mettent un « curseur » sur le compromis qualité/latence/coût. Ensemble, ces contrôles s’inscrivent dans une tendance : rendre l’agent plus configurable et prévisible en production.

Enfin, l’annonce mélange performances et sécurité. Anthropic revendique des gains importants sur des évaluations agentiques et de knowledge work, tout en affirmant que le profil de sûreté est au moins aussi bon que les versions précédentes (faible taux de comportements misalignés et moins d’over-refusal). Pour un lecteur produit/engineering, la lecture utile est moins la comparaison brute des benchmarks que la direction : pousser la fiabilité sur des tâches longues, donner des contrôles de coût/raisonnement, et soutenir des workflows multi-outils où l’agent doit tenir un plan sur la durée.
