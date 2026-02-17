# Présentation de GPT‑5.3‑Codex‑Spark
**Source**: https://openai.com/fr-FR/index/introducing-gpt-5-3-codex-spark/
**Date**: Unknown
**Author**: OpenAI
**Keywords**: low-latency inference, Codex, Cerebras, realtime coding, WebSocket

## Elevator pitch
OpenAI lance GPT‑5.3‑Codex‑Spark, une version allégée orientée “programmation en temps réel” : >1 000 tokens/s sur une voie faible latence Cerebras, avec un comportement par défaut plus léger (modifs ciblées) et des optimisations de pipeline qui réduisent fortement le time‑to‑first‑token.

## Takeaways
- Modèle “petit” optimisé latence, 128k de contexte, text‑only, distribué en preview via ChatGPT Pro/Codex app/CLI/VS Code.
- Trade‑off: moins performant que GPT‑5.3‑Codex sur des benchmarks agentiques, mais exécute les tâches bien plus vite.
- Style de travail par défaut: changements minimaux et ciblés; exécution de tests uniquement sur demande.
- Optimisations infra (WebSocket persistant, API Responses): -80% overhead par round‑trip, -30% overhead par token, -50% temps avant premier token.
- Positionnement: deux modes complémentaires à terme (long‑horizon + temps réel), potentiellement combinés via sous‑agents et parallélisation.

## Synthesis
L’annonce présente Codex‑Spark comme une réponse à un problème de plus en plus visible: quand les modèles deviennent suffisamment capables, la latence d’interaction devient le goulot d’étranglement. OpenAI introduit donc une variante de GPT‑5.3‑Codex explicitement optimisée pour l’itération “en direct” dans Codex: modifier une portion de logique, ajuster une UI, et voir le résultat immédiatement.

Le texte insiste sur le compromis fondamental vitesse vs intelligence. Codex‑Spark reste “très performant” sur la programmation réelle, mais sacrifie une partie des capacités de raisonnement/agentique d’un modèle plus lourd. Pour compenser, il adopte un style de travail plus conservateur: interventions minimales et ciblées, et pas de tests automatiques sans instruction explicite. Le message implicite est UX: à haute vitesse, l’utilisateur veut une collaboration interactive qu’il peut interrompre et rediriger.

Une part importante de l’annonce concerne l’infrastructure. OpenAI explique que la vitesse “modèle” n’est qu’une composante; ils ont optimisé toute la chaîne requête‑réponse, notamment via une connexion WebSocket persistante et des améliorations de l’API Responses. Les chiffres donnés (réduction de surcharge et amélioration du time‑to‑first‑token) signalent que l’expérience temps réel est autant un sujet réseau/serving qu’un sujet modèle.

Côté hardware, Codex‑Spark tourne sur le Wafer‑Scale Engine 3 de Cerebras, utilisé comme un chemin de service à faible latence complémentaire aux GPU (qui restent centraux pour l’entraînement et de nombreuses charges). L’annonce positionne Cerebras comme un accélérateur spécialisé pour des workflows où chaque milliseconde compte.

Enfin, OpenAI décrit une trajectoire produit: un Codex à deux modes (raisonnement long‑horizon et collaboration temps réel) qui, à terme, pourrait combiner les deux — rester réactif dans l’échange tout en déléguant en arrière‑plan des travaux plus longs à des sous‑agents ou à plusieurs modèles en parallèle. L’objectif est de ne plus forcer l’utilisateur à choisir “un mode” dès le départ, tout en tirant parti de l’inférence ultrarapide pour rendre le développement assisté plus naturel.
