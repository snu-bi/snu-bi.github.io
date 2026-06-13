---
title: RoboMotion
subtitle: Learning to Generate Robot Motions from Human Activity Sequences
group: completed
period: "2011~2013"
image: images/photo.jpg
funding: "National Research Foundation of Korea (NRF)"
tags:
  - robotics
  - motion-generation
  - human-robot-interaction
  - machine-learning
  - computer-vision
  - imitation-learning
  - activity-recognition
---

RoboMotion investigated **machine learning approaches for enabling robots to watch, understand, and imitate human manipulation activities** — learning to generate flexible robot arm motions directly from observed human activity sequences.

## Overview

A central challenge in robotics is endowing robots with the ability to acquire new manipulation skills without explicit programming. RoboMotion addressed this by developing a two-stage learning framework: first extracting rich spatio-temporal features from video observations of human activities, then automatically generating high-level semantic rules that capture the structure of those activities and can be transferred to a robotic system.

The core technical innovation was the application of **Independent Subspace Analysis (ISA)** — an unsupervised deep learning method — to learn invariant spatio-temporal feature representations directly from unlabeled video data. These learned features are robust to dynamic backgrounds, camera jitter, illumination changes, and scale variations. In the second stage, the system automatically infers symbolic semantic rules from the learned features, enabling high-level reasoning about what the human is doing and how those actions should be reproduced by a robot arm.

The framework was evaluated on complex real-world cooking scenarios (pancake making and sandwich making), where a humanoid robot must recognize and replicate the sequential manipulation steps performed by a human demonstrator. Results demonstrated action recognition accuracy above 87%, significantly outperforming single-stage baselines, and showed successful skill transfer to the humanoid platform.

## Research Team

| Role | Name | Affiliation |
|------|------|-------------|
| Principal Investigator | Prof. Byoung-Tak Zhang | SNU Biointelligence Lab |
| Researcher | Eun-Sol Kim | SNU Biointelligence Lab |
| Researcher | Jiseob Kim | SNU Biointelligence Lab |
| Collaborator | Karinne Ramirez-Amaro | TUM, Chair of Cognitive Systems |
| Collaborator | Prof. Michael Beetz | TUM / Uni Bremen, IAS Group |
| Collaborator | Prof. Gordon Cheng | TUM, Chair of Cognitive Systems |

## Technical Approach

- **Independent Subspace Analysis (ISA)**: unsupervised learning of invariant spatio-temporal features from raw video without manual labels
- **Two-stage pipeline**: (1) low-level feature learning from video streams; (2) automatic semantic rule extraction for high-level activity understanding
- **Robustness**: feature representations immune to dynamic backgrounds, noise, camera jitter, illumination, and size variation
- **Skill transfer**: mapping recognized semantic activity structure onto robot joint trajectories for humanoid arm motion generation
- **Evaluation scenarios**: pancake making and sandwich making, requiring recognition of sequential fine-grained manipulation steps

## Collaboration

The project was conducted in collaboration with the **Chair of Cognitive Systems and the Intelligent Autonomous Systems (IAS) Group at Technische Universität München (TUM)**, Germany. The collaboration combined SNU's expertise in machine learning and deep feature representations with TUM's robotics engineering and semantic reasoning capabilities for humanoid platforms.

## Publications

- K. Ramirez-Amaro, E.-S. Kim, J. Kim, B.-T. Zhang, M. Beetz, and G. Cheng, "Enhancing Human Action Recognition through Spatio-temporal Feature Learning and Semantic Rules," *13th IEEE-RAS International Conference on Humanoid Robots (Humanoids 2013)*, 2013.

- K. Ramirez-Amaro, E.-S. Kim, J. Kim, B.-T. Zhang, M. Beetz, and G. Cheng, "Human Cooking Action Recognition via Spatio-temporal Feature Learning based on ISA," 2012.

- K. Ramirez-Amaro, M. Beetz, and G. Cheng, "Transferring skills to humanoid robots by extracting semantic representations from observations of human activities," *Artificial Intelligence*, 2015. DOI: 10.1016/j.artint.2015.08.009
