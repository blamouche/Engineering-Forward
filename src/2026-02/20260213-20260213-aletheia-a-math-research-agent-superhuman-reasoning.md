# Aletheia: a math research agent (Superhuman Reasoning)
**Source**: https://github.com/google-deepmind/superhuman/blob/main/aletheia/Aletheia.pdf
**Date**: Unknown
**Author**: Google DeepMind Superhuman Reasoning team
**Keywords**: math research agent, Gemini Deep Think, verification, iterative solving, datasets

## Elevator pitch
DeepMind publie “Aletheia”, un agent de recherche en maths (Gemini Deep Think) conçu pour itérer: générer des pistes, vérifier, réviser — et ils partagent prompts + sorties sur des problèmes de niveau recherche.

## Takeaways
- Le repo “superhuman” regroupe projets/datasets du groupe Superhuman Reasoning (AlphaGeometry, IMO Bench, etc.).
- Aletheia est présenté comme un **agent**: itération + vérification + révision, plutôt qu’une réponse unique.
- Le release inclut des traces (prompts/réponses) sur des problèmes de maths “research-level”.
- Les artefacts pointent vers des tex/pdf et, dans plusieurs cas, vers des papiers arXiv associés.
- Intérêt: montrer des workflows d’agent mathématique et des résultats reproductibles (et auditables) via artefacts.

## Synthesis
Cette entrée est moins un article “narratif” qu’une publication de matériel: Google DeepMind met à disposition une partie des travaux de son équipe “Superhuman Reasoning”, et en particulier Aletheia — un agent orienté recherche mathématique, construit autour de Gemini Deep Think.

Le point clé est la boucle: la résolution de problèmes de maths avancée n’est pas un simple “completion”, mais un processus où l’on explore des pistes, on vérifie des sous-énoncés, on corrige, et on itère. Aletheia est décrit comme un système capable de **générer, vérifier et réviser** de manière répétée.

Le dépôt fournit ensuite des sorties structurées sur plusieurs cas: généralisation d’un problème d’Erdős, études semi-autonomes sur des problèmes ouverts, calculs d’eigenweights, contributions à des papiers (liens arXiv). Les artefacts (tex/pdf) matérialisent un avantage important pour la recherche assistée: les résultats ne restent pas dans une conversation, ils deviennent des documents vérifiables et partageables.

Pour une veille “engineering”, l’intérêt est double: (1) démonstration d’un pattern agentique pour des domaines très contraints (où la vérification est centrale) et (2) exemple de publication de traces et d’outputs comme “data produit” — utile pour l’évaluation, la reproductibilité, et l’amélioration continue des systèmes.
