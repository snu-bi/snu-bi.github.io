---
title: CogHRI
subtitle: Cognitive Communication as Moving Target Tracking
group: completed
period: "Dec 2012 – Nov 2017"
image: images/photo.jpg
funding: "Korea Evaluation Institute of Industrial Technology (KEIT)"
tags:
  - human-robot-interaction
  - cognitive-computing
  - natural-language-processing
  - dialogue-systems
  - bayesian-inference
  - affective-computing
  - robotics
---

CogHRI developed **self-improving, bidirectional human-robot interaction** technology capable of understanding users' complex emotional states and transactional intent through continuous interactions — targeting a 95% successful response rate.

## Overview

The core objective of CogHRI was to develop autonomous, bidirectional HRI technology that progressively understands and learns a user's combined cognitive and emotional states, as well as their transactional intent (current intent, future sequential intent, and intent transitions) through sustained robot-user interaction. The system aimed to respond appropriately in 95% or more of such interactions.

Cognitive communication is framed as a **moving target tracking problem**: the user's intent and emotional state are constantly shifting, and the robot must continuously update its model through a perception-action-learning cycle with dynamic Bayesian inference.

The project addressed this challenge through five core HRI element technologies, collectively named **MESSI**:

| Sub-task | Domain |
|----------|--------|
| **HRI.Map** | Robot spatial mapping and navigation |
| **HRI.Emotion** | User emotion recognition |
| **HRI.Service** | Service planning and execution |
| **HRI.System** | Full system integration |
| **HRI.Intention** | Dialogue (linguistic) intent understanding |

SNU Biointelligence Lab led the **HRI.Intention** sub-task (Sub-task 3), focusing on dialogue understanding and generation based on a perception-action-learning cycle, and developing real-time conversation models backed by hierarchical probabilistic inference to verify and support transactional intent recognition.

## Research Team

**Principal Investigator:** Prof. Byoung-Tak Zhang (HRI.Intention sub-task)

**Researchers:**
- Ha-Young Jang
- Beom-Jin Lee
- Jin-Hwa Kim
- Chung-Yeon Lee
- Kyung-Min Kim

## Technical Approach

The HRI.Intention sub-task pursued four lines of technical development:

1. **Dialogue corpus collection and machine-learning-based dialogue modeling** — building annotated corpora of human-robot dialogue and training statistical models of conversational structure.
2. **Real-time dialogue understanding with dynamic model refinement** — applying learned dialogue models to live interactions and updating the model incrementally as new exchanges occur.
3. **Linguistic intent recognition using nonverbal transactional cues and complex emotion** — integrating body language and affective signals to improve interpretation of spoken intent.
4. **Support module for nonverbal transactional intent verification** — providing auxiliary inference to cross-validate cues from non-linguistic channels.

The overall goal was to maximize transactional-intent accuracy while improving dialogue coherence, comprehension depth, and processing speed through real-time dialogue understanding and generation models.

## Collaboration

| Partner | Role |
|---------|------|
| Hanyang University (Prof. Il-Hong Suh) | HRI.Map, HRI.Service — overall project PI |
| Kyungpook National University (Prof. Min-Ho Lee) | HRI.Intention support |
| KAIST (Prof. Dong-Soo Kwon) | HRI.Emotion |
| KIST (Dr. Seung-Jong Kim) | HRI.System integration |

## Publications

- J.-H. Oh, H.-S. Chun, and B.-T. Zhang, "Generating cafeteria conversations with a hypernetwork dialogue model," in *Proceedings of the 14th International Symposium on Advanced Intelligent Systems (ISIS 2013)*, pp. 1424–1435, 2013.

## Contact

**Contact:** Ha-Young Jang
**Email:** hyjang at bi.snu.ac.kr
