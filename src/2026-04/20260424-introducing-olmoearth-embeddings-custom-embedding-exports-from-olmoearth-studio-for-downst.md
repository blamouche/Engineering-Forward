# Introducing OlmoEarth embeddings: Custom embedding exports from OlmoEarth Studio for downstream analysis

**Source**: https://allenai.org/blog/olmoearth-embeddings
**Date**: April 24, 2026
**Author**: Unknown
**Keywords**: allenai, introducing, olmoearth, embeddings, custom, embedding, exports, from

## Elevator pitch
OlmoEarth Studio now lets users export custom Earth-observation embeddings from our OlmoEarth foundation models and use them for tasks like similarity search, few-shot mapping, change detection, and unsupervised exploration

## Takeaways
- Introducing OlmoEarth embeddings: Custom embedding exports from OlmoEarth Studio for downstream analysis April 23, 2026 Patrick Johnson, Favyen Bastani, Gabriel Tseng, Chris Wilhelm, Joseph Redmon, Hunter Pitelka, Patrick Beukema, Mike Jacobi, and Hadrien Sablon - Ai2 Share Tech Report Documentation Learn more about OlmoEarth OlmoEarth Studio , our platform for building Earth observation models, now lets you compute and export embedding vectors —compact numerical representations of Earth-observation data produced by our open source OlmoEarth foundation models.
- The source code and model weights are publicly available alongside the research paper , so the community can inspect exactly how these embeddings are generated.
- Embeddings are a fast, cost-effective entry point for leveraging OlmoEarth: they support a wide range of downstream tasks, from similarity search to segmentation to unsupervised exploration.
- Locations with similar surface characteristics end up with similar vectors; locations that differ land far apart.
- OlmoEarth embeddings have shown strong performance in our own benchmarking and in independent evaluations .

## Synthesis
Introducing OlmoEarth embeddings: Custom embedding exports from OlmoEarth Studio for downstream analysis April 23, 2026 Patrick Johnson, Favyen Bastani, Gabriel Tseng, Chris Wilhelm, Joseph Redmon, Hunter Pitelka, Patrick Beukema, Mike Jacobi, and Hadrien Sablon - Ai2 Share Tech Report Documentation Learn more about OlmoEarth OlmoEarth Studio , our platform for building Earth observation models, now lets you compute and export embedding vectors —compact numerical representations of Earth-observation data produced by our open source OlmoEarth foundation models. The source code and model weights are publicly available alongside the research paper , so the community can inspect exactly how these embeddings are generated. Embeddings are a fast, cost-effective entry point for leveraging OlmoEarth: they support a wide range of downstream tasks, from similarity search to segmentation to unsupervised exploration. Locations with similar surface characteristics end up with similar vectors; locations that differ land far apart. OlmoEarth embeddings have shown strong performance in our own benchmarking and in independent evaluations . The exported Cloud-Optimized GeoTIFFs (COGs) are lightweight and easy to share. Choose your area of interest, time range, encoder variant, resolution, and imagery sources via the Studio UI or API, and get back a COG you can use however you like. If your application requires higher performance, Studio also supports supervised fine-tuning (SFT) . Custom-computed embeddings are now available for users of OlmoEarth Studio. Reach out if you're interested in gaining access.
