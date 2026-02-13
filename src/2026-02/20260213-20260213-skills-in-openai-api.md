# Skills in OpenAI API
**Source**: https://developers.openai.com/cookbook/examples/skills_in_api/
**Date**: Unknown
**Author**: OpenAI
**Keywords**: skills, reusable procedures, packaging, hosted shell, versioning

## Elevator pitch
Les “skills” deviennent un format standard pour packager des procédures réutilisables (instructions + scripts + assets) que les agents peuvent monter dans un environnement d’exécution, versionner, et invoquer au besoin.

## Takeaways
- Une skill = un dossier bundle avec un manifeste `SKILL.md` (frontmatter name/description) + scripts/assets.
- Objectif: sortir les workflows conditionnels et lourds du system prompt, et les rendre versionnables.
- Upload via API (zip ou multipart), puis montage dans l’environnement (hosted shell ou local).
- Bonnes pratiques: discoverability, préférer zip, pin de versions en prod, design type mini-CLI.
- Attention au risque “skills + réseau”: privilégier allowlists et séparation des données qui peuvent sortir.

## Synthesis
Le document clarifie un point de design produit: entre “prompt ad hoc” et “outil” (API side-effect), il manque une couche de **procédures packagées**. Les skills remplissent ce rôle en encapsulant un workflow (avec branching, validations, retries) et du code exécutable, tout en restant optionnelles et versionnées.

La mécanique est simple mais importante: on upload un bundle (souvent en zip), le service extrait les métadonnées depuis le frontmatter du manifeste `SKILL.md`, puis le runtime monte les fichiers dans l’environnement. Le modèle peut alors lire les instructions et exécuter des scripts via la tool shell. Résultat: on peut réutiliser le même “playbook” sur plusieurs agents, et garder les prompts globaux compacts.

Le texte propose une taxonomie utile:
- System prompt = comportement global et contraintes (durables, courtes).
- Tools = actions dans le monde / side effects / accès à des systèmes.
- Skills = procédures reproductibles (instructions + code + assets).

Sur l’opérationnel, plusieurs points reviennent: rendre la skill découvrable (quand l’utiliser / quand ne pas l’utiliser), versionner/pinner en production pour la reproductibilité, et concevoir les scripts comme des CLIs déterministes (stdout stable, erreurs claires, outputs sur chemins connus). Enfin, le doc rappelle que combiner des workflows puissants et de l’accès réseau non borné est risqué — et qu’il faut traiter les sorties de tool comme non fiables, mettre des garde-fous, et limiter les données exfiltrables.
