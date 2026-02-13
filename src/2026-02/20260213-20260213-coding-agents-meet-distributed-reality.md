# Coding Agents Meet Distributed Reality
**Source**: https://jhellerstein.github.io/blog/codegen-reality/
**Date**: Unknown
**Author**: Joe Hellerstein
**Keywords**: distributed systems, languages, determinism, testing, Hydro

## Elevator pitch
Si l’IA va écrire la majorité du code, alors il faut la faire viser des frameworks/langages où les bugs distribués “classiques” sont impossibles (ou explicitement marqués), plutôt que d’écrire du code impératif et de compenser par du testing héroïque.

## Takeaways
- La plupart des apps sont des systèmes distribués; les pires bugs viennent de l’ordonnancement, retries, state long-lived.
- Les bounded model checkers aident, mais n’offrent pas de garantie: ils explorent un sous-espace.
- Le pire échec vient des contrats implicites entre composants (ordering, delivery, idempotence).
- Proposer des frameworks (ex: Hydro) qui rendent ces choix explicites et typés, et isolent la non-déterminisme (`nondet!`).
- Tester devient “checker autour des zones nondet”, pas partout.

## Synthesis
Hellerstein construit une thèse simple: l’explosion de productivité promise par les agents de code se heurtera de plein fouet à la réalité des systèmes distribués — là où se cachent les bugs les plus coûteux. Les LLMs excellent sur les happy paths; les corner cases distribués (retries, permutations rares, ordres non déterministes) sont une autre histoire.

La réponse réflexe est “test harder” et l’auteur reconnaît les progrès (TLA+, Alloy, Jepsen, Antithesis). Mais il rappelle une vérité mathématique: bounded checking ≠ preuve. Les exécutions non explorées dominent, et la production reste le fuzz-test ultime.

Le pivot est alors: **changer la surface d’expression**. Dans du code impératif, les contrats distribués restent implicites, dans le “gap” entre specs et procédures. Un agent remplira ce gap par des suppositions. À l’inverse, des frameworks comme Hydro forcent l’explicitation: collections unordered ne peuvent pas alimenter du code order-sensitive sans erreur de compilation; les rares endroits où la divergence est possible sont marqués par `nondet!`.

Résultat: on ne “prouve” pas toute la logique business, mais on rend inexpressibles une classe de heisenbugs. Le testing ne disparaît pas, il se concentre sur les zones réellement ambiguës. Le message final est une recommandation stratégique pour l’ère agentique: au lieu de générer du code classique puis d’empiler de l’outillage de validation, choisir des langages/frameworks qui encodent les hypothèses distribuées dans le type system et les interfaces. On déplace l’effort de debug vers la conception de contraintes.
