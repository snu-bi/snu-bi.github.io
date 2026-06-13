---
title: DeepClone
subtitle: Cloning Humans for Scheduling Personal Service Robots
group: completed
image: images/photo.jpg
funding: "IITP (Institute of Information & Communications Technology Planning & Evaluation), Ministry of Science and ICT, Korea"
tags:
  - robotics
  - deep-learning
  - lifelogging
  - multimodal
  - human-robot-interaction
  - scheduling
  - wearable-sensing
---

## Overview

DeepClone aimed to create **deep-learning-based digital clones of humans** by capturing behavioral patterns through long-term lifelogging with wearable sensors, enabling a personal service robot to anticipate and autonomously schedule tasks on the user's behalf.

The central idea was that a robot does not need to be told what to do if it has already learned — from continuous, real-world observation — the user's routines, preferences, and habits in sufficient detail. By constructing a computational clone of the user's behavioral self, the robot can proactively plan, prioritize, and execute domestic service tasks without explicit instruction.

This approach extended the lab's prior work on mobile lifelogging (mLife) and cognitive video learning (Videome) into the personal robotics domain, combining long-term data collection from heterogeneous wearable devices with deep learning models capable of predicting future user behavior.

## Research Team

**Principal Investigator**
- Prof. Byoung-Tak Zhang (Seoul National University, Biointelligence Lab)

## Sensing Modalities

DeepClone relied on a multimodal wearable sensing suite to build rich, continuous behavioral records:

| Sensor | Signal Type | Purpose |
|--------|-------------|---------|
| Smart glasses | First-person RGB video | Visual context of daily activities |
| Smartwatch | Motion (IMU), biometrics | Activity and physiological state |
| Brain scanner (EEG) | Neural signals | Cognitive and attentional state |
| Body sensors | Physiological signals | Health and arousal context |

This multimodal combination allowed the system to capture not just what the user was doing, but the cognitive and physical context surrounding each activity — forming the basis for a behavioral model that was both rich and personalized.

## Technical Approach

### Lifelogging as Training Data

Unlike most machine learning pipelines that rely on curated, annotated datasets, DeepClone used **long-term real-world lifelogging** as its primary data source. Continuous sensor streams were collected from participants over extended periods — capturing the natural rhythms and variability of everyday life rather than staged scenarios.

### Behavioral Pattern Learning

Deep learning models were applied to reverse-engineer individual-level behavioral patterns from the raw multimodal sensor streams. The system learned:

- **Temporal structure** of daily routines (when activities occur, how long they last, how they sequence)
- **Activity preferences** (what the user tends to do in specific contexts or times of day)
- **Context dependencies** (how environmental factors, physiological state, or social context influence behavior)

### Future Task Scheduling

The behavioral clone served as a predictive model: given the current context (time, location, recent activity, physiological state), it forecast the user's upcoming needs and generated a ranked schedule of service robot tasks — from fetching items to environmental adjustments — before the user made any explicit request.

### Relationship to StarLab

DeepClone was closely related to the IITP-funded **StarLab** project (Cognitive Agents That Learn Everyday Life), which developed parallel infrastructure for lifelong learning from wearable sensor data. StarLab's core systems — including **LifeMap** (behavioral visualization), **CogMap** (episodic memory), and **ActMap** (activity prediction) — provided complementary foundations that informed DeepClone's architecture.

## Context Within the Lab's Research Program

DeepClone represented one of several "former flagship projects" in the lab's research on agents that learn from human life experience:

- **mLife** (2010–2015): mobile behavior identification from smartphone sensors
- **Videome** (2011–2015): cognitive learning from digital video streams
- **StarLab** (2015~): cognitive agents learning everyday life via wearable sensors
- **DeepAction**: deep learning of TV viewer activities
- **DeepClone**: cloning human behavior for personal robot scheduling
- **BabyMind** (2020~): infant-mimic neurocognitive AI from real-world interaction

These projects collectively built toward the vision of AI agents that learn continuously from the texture of real human life, rather than from bounded, curated datasets.
