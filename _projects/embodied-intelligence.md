---
title: Embodied Intelligence (EI)
subtitle: Embodied Artificial Intelligence that Interacts with the Real World
group: completed
period: "2021~2023"
image: images/photo.jpg
funding: "IITP (Institute of Information & Communications Technology Planning & Evaluation), Ministry of Science and ICT, Korea"
tags:
  - robotics
  - embodied-ai
  - computer-vision
  - multimodal
  - reinforcement-learning
  - natural-language-processing
  - robot-manipulation
  - mobile-robots
  - lifelong-learning
---

The Embodied Intelligence (EI) project developed **AI systems with physical embodiment** capable of perceiving, reasoning, and acting in the real world. The project spanned the full perception-to-action pipeline: from visual grounding and multi-agent map fusion for mobile robots to language-conditioned lifelong learning and safe manipulation for robotic arms. A key objective was building agents that can continually adapt — not only learning to see and understand their environment, but doing so sustainably across changing tasks and conditions.

## Overview

Physical embodiment changes the nature of intelligence. Unlike disembodied AI that operates on static datasets, embodied agents must handle sensor noise, dynamic environments, partial observability, and the physical consequences of their actions. The EI project addressed this challenge across two complementary platforms:

1. **Mobile robot navigation and multi-agent coordination** — developing robust visual perception and cooperative map-building strategies that allow multiple agents to rendezvous and share spatial understanding of their environment.

2. **Robotic arm manipulation** — combining natural language understanding with continual learning so that a robot arm can follow human instructions across a stream of novel objects and manipulation tasks, without catastrophically forgetting prior capabilities.

Both tracks required tight integration of computer vision, natural language processing, and reinforcement learning, reflecting the lab's broader commitment to multimodal AI.

## Research Team

**Principal Investigator**
- Prof. Byoung-Tak Zhang (Seoul National University)

**Researchers (Mobile Perception)**
- Jaein Kim
- Dong-Sig Han

**Researchers (Language-Conditioned Manipulation)**
- Junghyun Kim
- Gi-Cheon Kang
- Suyeon Shin

**Researchers (Safe Manipulation & Tracking)**
- Hyunseo Kim
- Hye-Jung Yoon
- Minji Kim

**Researchers (Inverse Reinforcement Learning)**
- Hyundo Lee
- Je-Hwan Ryu

## Technical Approach

### Multimodal Perception for Mobile Robots

- **Visual attention-based map fusion**: a multi-agent rendezvous framework that enables robots to merge independently built occupancy maps using visual attention, enabling cooperative localization even when agents have explored disjoint areas.
- **Object detection and visual grounding** for task-relevant perception in cluttered real-world scenes.

### Language-Conditioned Lifelong Manipulation

- **GVCCI** (Grounded Visual Concept Continual Instance learning): a continual contrastive learning framework that allows a robotic arm to learn visual groundings of language-referred object instances over an open-ended stream of tasks, without forgetting previously acquired concepts.
- **ROS-based real-world control pipeline**: end-to-end system connecting natural language commands to robot arm joint control via a ROS middleware stack.

### Safe and Adaptive Object Tracking

- **EXOT** (Exit-Aware Object Tracker): a real-time tracker that detects when a target object is about to exit the robot's reachable workspace or camera field-of-view, enabling the robot to abort or adapt its grasp strategy before a collision or failure occurs.

### Imitation and Inverse Reinforcement Learning

- Mirror-descent inverse reinforcement learning (**Mirror-Descent IRL**) for robust imitation from suboptimal or noisy human demonstrations — supporting safe transfer of human-demonstrated manipulation skills to robotic systems.

## Publications

- **Junghyun Kim**, Gi-Cheon Kang, Jaein Kim, Suyeon Shin, Byoung-Tak Zhang. "GVCCI: Lifelong Learning of Visual Grounding for Language-Guided Robotic Manipulation." *IROS 2023.* [arXiv:2307.05963](https://arxiv.org/abs/2307.05963)

- **Hyunseo Kim**, Hye-Jung Yoon, Minji Kim, Dong-Sig Han, Byoung-Tak Zhang. "EXOT: Exit-Aware Object Tracker for Safe Robotic Manipulation of Moving Object." *ICRA 2023.* [arXiv:2306.05262](https://arxiv.org/abs/2306.05262)

- **Jaein Kim**, Dong-Sig Han, Byoung-Tak Zhang. "Robust Map Fusion with Visual Attention Utilizing Multi-Agent Rendezvous." *ICRA 2023.* [DOI:10.1109/ICRA48891.2023.10161072](https://doi.org/10.1109/ICRA48891.2023.10161072)

- **Dong-Sig Han**, Hyunseo Kim, Hyundo Lee, Je-Hwan Ryu, Byoung-Tak Zhang. "Robust Imitation via Mirror-Descent Inverse Reinforcement Learning." *NeurIPS 2022.* [arXiv:2210.11201](https://arxiv.org/abs/2210.11201)

- **Junghyun Kim**, Gi-Cheon Kang, Jaein Kim, Seoyun Yang, Minjoon Jung, Byoung-Tak Zhang. "PGA: Personalizing Grasping Agents with Single Human-Robot Interaction." *IROS 2024.* [arXiv:2310.12547](https://arxiv.org/abs/2310.12547)

- **Gi-Cheon Kang**, Junghyun Kim, Jaein Kim, Byoung-Tak Zhang. "PROGrasp: Pragmatic Human-Robot Communication for Object Grasping." *ICRA 2024.* [arXiv:2309.07759](https://arxiv.org/abs/2309.07759)

- **Hye-Jung Yoon**, Juno Kim, Yesol Park, Byoung-Tak Zhang. "Visual Perception-Based Assistive Mobile Robot System for Manipulation Tasks." *ICRA 2023 Workshop on Assistive Manipulation.*

- Dongwoon Song, Taewoong Kang, et al., Byoung-Tak Zhang, Jae-Bok Song, Seung-Joon Yi. "RoboCup@Home 2021 Domestic Standard Platform League Winner." *RoboCup 2021.* [DOI:10.1007/978-3-030-98682-7_24](https://doi.org/10.1007/978-3-030-98682-7_24)

## Collaboration

The robotic manipulation work was developed in close collaboration with the **Intelligent Robotic Systems Lab** at Seoul National University (Prof. Jae-Bok Song, PI: Seung-Joon Yi), co-fielding a joint team for the **RoboCup@Home Domestic Standard Platform League** (2021 winners). The home-service robotics platform (Team Tidyboy) served as a real-world testbed for integrated perception, navigation, and manipulation capabilities developed across both labs.
