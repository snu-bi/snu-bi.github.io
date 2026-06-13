---
title: MMG
subtitle: Cognitive Learning and the Multimodal Memory Game Platform
group: completed
period: "2007.11 ~ 2010"
image: images/photo.jpg
funding: "N/A (internal research)"
external_link: "https://bi.snu.ac.kr/Research/MMG/MMG.html"
tags:
  - cognitive-computing
  - multimodal
  - machine-learning
  - human-computer-interaction
  - memory
  - nlp
  - computer-vision
  - hypernetworks
---

The MMG project built a **game-based research platform** to investigate cognitive learning through the integration of text, speech, and image data drawn from the TV drama *Friends*. The platform was designed to study how multimodal memory forms and improves over time — in both humans and machines — and to develop computational models capable of human-level learning from naturalistic, continuously arriving experience.

## Overview

The Multimodal Memory Game (MMG) is centered on a simple but powerful idea: use a structured game interaction between human players and a machine learner to collect naturalistic data and measure learning progress. After watching video clips from *Friends*, players and the system engage in question-and-answer sessions about scenes, dialogue, and characters. The game makes data collection natural and scalable while providing ground truth for evaluating machine recall.

The project explored three modalities independently and in combination:

- **Text**: Training on subtitle/script data from *Friends* episodes to handle next-sentence and scene-level reasoning
- **Speech**: Learning from audio streams to handle spoken language understanding
- **Images**: Learning from visual frames to handle scene-level image description

The integration goal was to train a combined system using all three modalities simultaneously, building an associative neural network that reflects how human memory integrates sensory streams. The architecture is conceptually described as a network where text, speech, and image modules are connected into a globally coherent structure.

Two core principles for **human-level machine learning** motivated the theoretical framework:

1. **Continuity**: Memory forms incrementally and lifelong, rather than from a fixed, static dataset loaded at training time
2. **Glocality**: Locally specialized micromodules are organized within a globally connected network, mirroring the structure of biological memory systems

An empirical finding confirmed that human recall accuracy **improves steadily** with the number of game sessions, validating the game format as a tool for studying and enhancing long-term memory in humans and as a benchmark for machine learners.

## Key Figures

The legacy project page includes three illustrative figures:

- **Concept diagram**: Shows text, speech, and image streams converging into an associative neural network forming the Multimodal Memory Game
- **ImageToText example**: Demonstrates MMG generating text descriptions from image inputs
- **ExImageToText example**: Shows further results of image-to-text generation in action

## Methodology

The MMG platform combined ideas from cognitive science, natural language processing, computer vision, and machine learning:

- **Associative hypernetworks** that self-assemble to represent cross-modal memories
- **Incremental / continual learning** to avoid catastrophic forgetting over repeated game sessions
- **Question answering** over video-derived multimodal content as the core evaluation task
- Use of real-world TV drama data (*Friends*) to ensure naturalistic language, visual variety, and emotional range

## Research Team

**Principal Investigator**: Prof. Byoung-Tak Zhang (Seoul National University)

**Researchers**:
- Ho-Sik Seok
- Sun Kim
- Chan-Hoon Park
- Eun-Seok Lee
- Won-Jin Shin
- Young-Kil Ko
- Ha-Young Jang
- Kwon-ill Kim
- Min-Oh Heo
- Joo-Kyung Kim
- Bon-Woong Ku
- Sang-Yoon Yi
- Young-Jin Park
- Seong-Bae Lee

**Contact**: Min-Oh Heo — moheo (at) bi.snu.ac.kr

## Publications

- **Self-assembling hypernetworks for cognitive learning of linguistic memory**, B.-T. Zhang and C.-H. Park, *Proceedings of World Academy of Science, Engineering and Technology (WASET)*, p. 134, 2008.
- **Multimodal Memory Game** (conference paper), B.-T. Zhang et al., *Proceedings of the IEEE World Congress on Computational Intelligence (WCCI)*, 2008.
