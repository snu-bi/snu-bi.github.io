---
title: StarLab
subtitle: Cognitive Agents That Learn Everyday Life
group: completed
period: "2015~2020"
image: images/photo.jpg
external_link: "https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO201600002509"
funding: "IITP (SW Star Lab, Ministry of Science, ICT and Future Planning, Korea)"
tags:
  - cognitive-agents
  - wearable-computing
  - lifelogging
  - lifelong-learning
  - multimodal
  - deep-learning
  - human-activity-recognition
  - complementary-learning-systems
---

The **SW StarLab** project developed cognitive software agents capable of continuously learning from human daily activities captured through multimodal wearable sensors. Under Korea's SW Star Lab program, the SNU Biointelligence Lab built a full pipeline from real-world lifelogging data collection to behavioral prediction and memory-based anticipation of future activities.

## Overview

A central challenge in building human-aware intelligent systems is learning continuously from the unstructured flow of everyday life — a stream of sensory experiences, routines, and events that is too vast and variable for conventional batch learning. The StarLab project addressed this challenge by deploying wearable devices (Google Glass and smartwatch) on human participants over extended periods, collecting egocentric visual, motion, and physiological signals in the wild.

From this real-world lifelog data, the team designed three interconnected cognitive architectures:

- **LifeMap**: a visualization and indexing system that converts raw sensor streams into structured behavioral maps, enabling navigation and retrieval of past experiences.
- **CogMap**: an episodic memory architecture built on deep recurrent neural networks that stores sequential event representations as "stories" of daily activity.
- **ActMap**: a predictive model, based on POMDP (Partially Observable Markov Decision Process) frameworks, that anticipates future user activities given current perceptual context and stored memory.

The project was inspired by neurocognitive **Complementary Learning Systems (CLS)** theory, which posits that biological memory relies on two interacting systems: a fast hippocampal episodic store and a slower neocortical semantic store. The dual-memory deep learning architectures developed in StarLab directly embody this principle, allowing the agent to retain long-term behavioral regularities while adapting rapidly to new episodic observations without catastrophic forgetting.

A 46-day real-world lifelogging experiment was conducted to validate the systems. Participants wore Google Glass and Microsoft Band smartwatches continuously, generating first-person video and motion/physiological sensor streams. On this dataset the system achieved approximately **82% accuracy** in predicting future user behaviors from wearable sensor patterns.

## Research Team

**Principal Investigator**
- Prof. Byoung-Tak Zhang (Seoul National University)

**Researchers**
- Sang-Woo Lee
- Chung-Yeon Lee
- Dong-Hyun Kwak
- Jeong-Woo Ha
- Jiwon Kim
- Jeonghee Kim
- Eun-Sol Kim
- Kyoung-Woon On

**Host Institution:** Seoul National University Industry-University Cooperation Foundation

## Technical Approach

### Data Collection & Sensors

| Device | Modality |
|--------|----------|
| Google Glass | First-person (egocentric) video and images |
| Microsoft Band (smartwatch) | Accelerometer, gyroscope, heart rate, EDA |

Two software applications were developed and registered for the data collection pipeline:
- Android LifeLogging sensor data collector (Software Registration C-2016-001315)
- Google Glass lifelogging application (Software Registration C-2016-001434)

### Learning Architecture

The dual-memory deep learning framework separates fast episodic learning from slow semantic consolidation:

- **Fast memory (episodic)**: an online-learning module that tracks rapidly changing local behaviors using incremental updates and weight transfer
- **Slow memory (semantic)**: a deep network that accumulates stable global patterns over extended time horizons

The CogMap component uses deep recurrent networks (LSTMs) to encode activity sequences as narrative "stories," while ActMap feeds these memory representations into POMDP-based decision frameworks for activity prediction. Emotion recognition was also explored by combining voice signals and electrodermal activity (EDA) data.

### Key Results

- ~82% accuracy in predicting user behavior on a 46-day real-world lifelog
- Demonstrated lifelong learning without catastrophic forgetting on CIFAR-10 and the lab's own Lifelog dataset
- Systems for emotion recognition combining voice and EDA signals
- Deep recurrent neural networks for story learning from first-person video

## Publications

- Sang-Woo Lee, Chung-Yeon Lee, Dong-Hyun Kwak, Jiwon Kim, Jeonghee Kim, Byoung-Tak Zhang. **"Dual-Memory Deep Learning Architectures for Lifelong Learning of Everyday Human Behaviors."** *IJCAI 2016*, pp. 1669–1675.
- Sang-Woo Lee, Chung-Yeon Lee, Dong-Hyun Kwak, Jeong-Woo Ha, Jiwon Kim, Byoung-Tak Zhang. **"Dual-Memory Neural Networks for Modeling Cognitive Activities of Humans via Wearable Sensors."** *Neural Networks*, Elsevier, 2017.
- Eun-Sol Kim, Kyoung-Woon On, Byoung-Tak Zhang. **"DeepSchema: Automatic Schema Acquisition from Wearable Sensor Data in Restaurant Situations."** *IJCAI 2016*, p. 834.
- Sang-Woo Lee, Chung-Yeon Lee, Dong-Hyun Kwak, Byoung-Tak Zhang. **"Glassbot: Personalized Wearable Agents Learning from Everyday Human Behaviors."** 2016.
