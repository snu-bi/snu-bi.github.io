---
title: Xtran
subtitle: Crossmodal Translation of Language and Vision
group: completed
period: "2008~2012"
image: images/photo.jpg
external_link: "https://bi.snu.ac.kr/Research/Xtran/Xtran.html"
funding: "NRF (Korea)"
tags:
  - multimodal
  - computer-vision
  - nlp
  - cross-modal-retrieval
  - hypernetworks
  - machine-learning
---

Xtran investigated **bidirectional translation between language and visual modalities** using hypernetwork-based machine learning — an early precursor to today's vision-language models. Just as machine translation converts sentences between human languages, Xtran aimed to convert representations between sensory modalities: generating relevant keywords from images and retrieving matching images from text descriptions.

## Overview

The central premise of Xtran is that language and vision are two different encodings of a shared semantic reality. A magazine article about a mountain landscape, for example, contains both images and text that mutually describe and reinforce each other. Xtran exploited this co-occurrence structure in multimodal magazine corpora to learn bidirectional associations between visual features and textual keywords.

The project employed **layered hypernetwork architectures** — probabilistic graphical models capable of encoding higher-order associations among multiple variables — to capture complex cross-modal correspondences that flat pairwise models would miss. By recalling higher-order patterns involving both image regions and text tokens simultaneously, the system was able to substantially outperform single-modality keyword generation baselines.

Key tasks addressed by Xtran include:

- **Text-to-image retrieval**: given a keyword query or phrase, retrieve the most semantically relevant images from a large archive
- **Image-to-text keyword generation**: given an image, automatically generate descriptive textual keywords
- **Visual query expansion**: incrementally expanding a user's image query using associated textual context learned by the hypernetwork

## Research Team

**Principal Investigator**
- Byoung-Tak Zhang (Seoul National University)

**Researchers**
- Jong-Wook Ha (PhD student, primary researcher)
- Byoung-Hak Kim
- Hyo-Woo Kim
- Moon-Ok Heo
- Byeong-Jae Lee
- M. Kang
- W. Yoon
- J. H. Eom

## Technical Approach

The core technical innovation of Xtran is the use of **hypernetworks** — a generalization of neural networks and Bayesian networks that can represent higher-order dependencies among many variables at once. Rather than modeling only pairwise co-occurrences between image patches and words, hypernetwork units encode associations among entire groups of visual and linguistic features.

The system architecture evolved across the project period:

- **Early phase (2008–2009)**: Higher-order pattern recall by hypernetworks for cross-modal retrieval from magazine article corpora; evaluation on text-to-image matching tasks
- **Mid phase (2010)**: Layered hypernetwork models for cross-modal associative keyword generation; incremental visual query expansion using multimodal hypernetworks
- **Late phase (2011–2012)**: Hierarchical hypergraph representations for text-to-image generation; incremental association mechanisms enabling more flexible retrieval

Training data consisted of paired text-image content from Korean magazine articles, where natural co-occurrence between editorial images and accompanying text provided implicit supervision for learning cross-modal mappings.

## Publications

- Jong-Wook Ha, Byoung-Hak Kim, Hyo-Woo Kim, W. Yoon, J. H. Eom, Byoung-Tak Zhang. "Text-to-image cross-modal retrieval of magazine articles based on higher-order pattern recall by hypernetworks." *Brain*, 2009.
- Moon-Ok Heo, Jong-Wook Ha, Byoung-Tak Zhang. "Extraction Analysis for Crossmodal Association Information using Hypernetwork Models." *Korean HCI Society Academic Conference*, 2009.
- Jong-Wook Ha, Byoung-Hak Kim, B. Lee, Byoung-Tak Zhang. "Layered hypernetwork models for cross-modal associative text and image keyword generation in multimodal information retrieval." *Pacific Rim International Conference on Artificial Intelligence (PRICAI)*, 2010.
- Moon-Ok Heo, M. Kang, Byoung-Tak Zhang. "Visual query expansion via incremental hypernetwork models of image and text." *Pacific Rim International Conference on Artificial Intelligence (PRICAI)*, 2010.
- Jong-Wook Ha, Byoung-Tak Zhang. "Text-to-image generation based on crossmodal association with hierarchical hypergraphs." *NIPS 2011 Workshop on Integrating Vision and Language*, 2011.
- Jong-Wook Ha, Byeong-Jae Lee, Byoung-Tak Zhang. "Text-to-image retrieval based on incremental association via multimodal hypernetworks." *IEEE International Conference*, 2012.

## Historical Context

Xtran was a pioneering effort in cross-modal learning at a time when such problems were considered extremely difficult, with most retrieval systems operating within a single modality. Its hypernetwork-based approach to cross-modal alignment anticipated ideas that later became central to landmark models such as CLIP, DALL-E, and modern vision-language transformers. The project demonstrated that higher-order co-occurrence patterns — captured by hypernetworks rather than simple pairwise co-occurrence statistics — are key to faithful cross-modal translation.
