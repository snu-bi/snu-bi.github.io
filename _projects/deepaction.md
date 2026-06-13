---
title: DeepAction
subtitle: Deep Learning of TV Viewer Activities
group: completed
image: images/photo.jpg
funding: "NRF (National Research Foundation of Korea)"
tags:
  - deep-learning
  - activity-recognition
  - computer-vision
  - human-activity-recognition
  - video-understanding
  - multimodal
---

DeepAction applied **deep learning** techniques to recognize and analyze the activities of television viewers, automatically modeling what people are doing — cooking, exercising, relaxing, working — while watching TV.

## Overview

Understanding viewer behavior during TV watching enables a new generation of intelligent, interactive television experiences. DeepAction addressed this challenge by building deep learning models that could infer viewer activities from multimodal sensor streams in a naturalistic home environment.

The project extended the lab's prior expertise in two complementary directions:

- **mLife** (2010–2015) demonstrated that smartphones could passively capture rich behavioral signals from daily life — GPS traces, accelerometer readings, audio snippets — and that machine learning could recognize context-dependent human activities from these streams.
- **Videome** (2011–2015) showed that deep cognitive architectures could learn structured knowledge incrementally from continuous video, mirroring how the human brain builds episodic memory.

DeepAction combined these threads: it treated the TV-watching context as a sensing environment, capturing what the viewer *is doing* rather than just what is *on screen*, and used deep neural networks to bridge low-level sensor signals with high-level activity semantics.

## Technical Approach

- **Multimodal sensory input**: fusion of visual (camera or depth sensor), motion (accelerometer/IMU), and contextual (program metadata, time-of-day) signals to characterize viewer state
- **Temporal activity modeling**: recurrent and convolutional neural network architectures to capture the sequential and periodic structure of household behaviors during TV viewing sessions
- **Hierarchical representation learning**: coarse-to-fine activity hierarchies distinguishing stationary postures (sitting, lying) from concurrent fine-grained activities (eating, using a smartphone, exercising)
- **Lifelong adaptation**: incremental learning mechanisms inspired by complementary learning systems theory, allowing the model to update viewer profiles over time without catastrophic forgetting

## Context and Motivation

Television remains one of the most prevalent household activities, yet most broadcast and streaming systems treat the viewer as a passive recipient. DeepAction's vision was of a system that *knows* its audience — adapting recommendations, interaction modalities, and ambient assistance based on real-time inference of viewer behavior.

This problem is technically demanding: viewer activities are diverse, their boundaries are fuzzy, and sensor data collected in realistic home settings is noisy and unlabeled. DeepAction developed models robust to these challenges, contributing to the lab's broader program of building AI that learns from everyday human life.

## Research Team

- **Principal Investigator**: Prof. Byoung-Tak Zhang (Seoul National University, Biointelligence Lab)

## Relation to Adjacent Projects

| Project | Period | Connection |
|---------|--------|------------|
| **mLife** | 2010–2015 | Behavioral recognition from mobile sensors; methodological foundation |
| **Videome** | 2011–2015 | Cognitive video understanding; architectural heritage |
| **StarLab** | 2015– | Lifelogging with wearable sensors; extended sensing modalities |
| **VTT** | 2017–2021 | Human-level video intelligence; downstream application |
