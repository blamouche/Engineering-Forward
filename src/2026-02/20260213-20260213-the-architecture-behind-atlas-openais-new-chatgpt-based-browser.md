# The Architecture Behind Atlas: OpenAI’s New ChatGPT-based Browser
**Source**: https://blog.bytebytego.com/p/the-architecture-behind-atlas-openais
**Date**: Unknown
**Author**: ByteByteGo
**Keywords**: browser architecture, Chromium, IPC, Mojo, CALayerHost, agent mode

## Elevator pitch
Atlas (navigateur OpenAI) isole Chromium dans un process séparé via une couche OWL, pour obtenir un UI natif rapide, un démarrage quasi-instantané, et des sessions agentiques isolées — sans forker Chromium lourdement.

## Takeaways
- Problème: intégrer Chromium “embed” rend difficile un UI natif (SwiftUI/Metal), un boot instantané, et la perf à 100s d’onglets.
- Solution: OWL (OpenAI Web Layer) = Atlas (client) + Chromium (host) en process séparés.
- Communication via Mojo (IPC), avec bindings Swift/TypeScript.
- Rendering cross-process via layer hosting (CALayer context IDs + CALayerHost côté app).
- Agent mode: screenshots composités (incl. popups), events agent routés directement vers le renderer (pas de shortcuts privilégiés), sessions éphémères via StoragePartition.

## Synthesis
L’article explique un choix d’architecture peu commun pour un navigateur: au lieu d’embarquer Chromium dans le process principal, OpenAI l’exécute comme un “host” séparé. Atlas devient un client OWL qui pilote Chromium via IPC (Mojo) et récupère des surfaces de rendu via des primitives macOS (CALayer) projetées dans l’UI.

Ce découplage répond à plusieurs objectifs pratiques. D’abord, **startup time**: l’UI peut apparaître immédiatement pendant que le moteur web boot en arrière-plan. Ensuite, l’ergonomie dev: si Chromium reste upstream, l’équipe évite un patch-set géant et peut garder une culture d’itération rapide (“shipping on day one”), car tous les devs n’ont pas besoin de builder Chromium localement.

La partie la plus intéressante est le rendu: Chromium rend dans un CALayer identifié; Atlas affiche ce layer via CALayerHost, ce qui permet de partager la mémoire GPU et de swapper rapidement la tab visible. L’input traverse aussi la frontière: Atlas traduit NSEvent → WebInputEvent, envoie à Chromium, et récupère les events non consommés pour laisser passer les shortcuts browser.

Enfin, l’article relie l’architecture à l’agentic browsing: pour que le modèle voie une capture cohérente, Atlas recompose certaines surfaces (popups) dans une seule image. Et pour la sécurité, les événements générés par l’agent ne doivent pas passer par des chemins privilégiés (pas de shortcuts “browser-level”), préservant le sandboxing. Au total, OWL est présenté comme un “socle” qui rend le navigateur plus résilient (crash/hang du host) et mieux adapté à des sessions agentiques multiples et isolées.
