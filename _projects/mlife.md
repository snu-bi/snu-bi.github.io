---
title: mLife
subtitle: Identifying Human Mobile Behaviors in Context
group: completed
period: "2010~2015"
image: images/photo.jpg
funding: "National Research Foundation of Korea (NRF)"
tags:
  - mobile-sensing
  - context-awareness
  - activity-recognition
  - life-logging
  - machine-learning
  - ubiquitous-computing
  - human-behavior-modeling
---

The mLife project investigated how to automatically **identify and model human behaviors** from mobile life-log data collected via smartphone sensors, enabling intelligent personalized mobile applications. As one of the Biointelligence Lab's flagship projects of the early 2010s, mLife established the lab's expertise in mobile context sensing that would later evolve into the wearable-based StarLab project.

## Overview

The proliferation of smartphones gave researchers for the first time a continuous, unobtrusive window into human daily life through embedded sensors: GPS receivers, accelerometers, gyroscopes, microphones, and cameras. mLife asked a deceptively simple question: can we mine these sensor streams to understand who a person is, what they do, and why?

Unlike controlled laboratory activity-recognition studies, mLife addressed the unconstrained real-world setting — people walking, commuting, working, socializing — where context is ambiguous, sensor readings are noisy, and activities interleave unpredictably. The project developed machine learning methods capable of discovering behavioral patterns in this messy, continuous stream of mobile data and using those patterns to power context-aware personalized services.

The core challenge was building models that could simultaneously recognize **what** a user is doing (physical activity), **where** they are doing it (semantic location context), and **why** their behavior is changing over time (higher-level routine and intent modeling). These three layers — activity, context, and routine — required fusing heterogeneous sensor modalities and reasoning across multiple time scales, from seconds (gesture and motion) to hours and days (routine and life pattern).

## Research Team

**Principal Investigator**
- Prof. Byoung-Tak Zhang (Seoul National University)

**Researchers**
- Jung-Woo Ha
- Min-Oh Heo
- Ha-Young Jang
- Ho-Sik Seok
- Hyunwoo Kim
- Bado Lee

## Technical Approach

### Multimodal Mobile Sensing

mLife fused heterogeneous sensor modalities available on commodity smartphones:

- **GPS and Wi-Fi positioning**: semantic place detection (home, office, transit, retail)
- **Accelerometer and gyroscope**: motion classification (walking, running, cycling, stationary)
- **Microphone**: acoustic context (indoor/outdoor, meeting, commuting)
- **Call and app logs**: social and digital behavioral signatures

Sensor fusion operated at multiple time granularities — raw signal windows for motion primitives, and longer temporal windows for routine and place modeling.

### Context-Aware Activity Recognition

Rather than treating activity recognition as a flat classification problem, mLife adopted a **hierarchical context model**: low-level sensor features were first mapped to physical activities and semantic locations; these intermediate representations were then combined with temporal context (time of day, day of week) to infer higher-level behavioral states and user intent.

Probabilistic graphical models — including Dynamic Bayesian Networks and Hidden Markov Models — were used to capture the sequential and temporal dependencies in mobile behavior streams.

### Behavioral Pattern Discovery

A key goal of mLife was unsupervised and semi-supervised discovery of behavioral patterns across users:

- **Routine mining**: identifying recurring daily behavioral templates (e.g., morning commute → office work → gym → home) without requiring explicit labels
- **Anomaly detection**: flagging deviations from learned routines as potentially significant events
- **Personalization**: adapting generic activity models to individual users through online learning from real-world mobile logs

### Intelligent Mobile Applications

The technical contributions were motivated by and demonstrated in the context of **proactive, context-aware mobile services**: applications that anticipate user needs based on behavioral context rather than waiting for explicit commands. This included location-based recommendations, context-sensitive notification management, and activity-aware scheduling assistance.

## Connection to Lab Research

mLife was the lab's primary effort in **mobile and ubiquitous computing** during 2010–2015, running in parallel with the Videome project (cognitive machine learning from digital video) and the CogHRI project (cognitive human-robot interaction). Where Videome addressed learning from passively consumed video content and Videome used IPTV as its sensing medium, mLife used the smartphone as a ubiquitous personal sensor platform.

The insights and methods from mLife directly informed the subsequent **StarLab** project (2015–), which extended the lifelogging paradigm to richer multimodal wearable sensors (smart glasses, smartwatches, brain scanners) and built deeper neurocognitive models of everyday life. The **DeepAction** project on TV viewer activity recognition also built directly on mLife's mobile behavior modeling foundations.
