---
title: DietAdvisor
subtitle: A Personalized eHealth Agent in a Mobile Computing Environment
group: completed
period: "2011~2012"
image: images/photo.jpg
funding: "NRF"
tags:
  - mobile-health
  - intelligent-agents
  - personalized-recommendation
  - mhealth
  - ubiquitous-computing
  - ehealth
  - context-awareness
---

DietAdvisor was a **smartphone-based personalized eHealth agent** that recommended meals and exercises to individual users by combining intelligent agent reasoning with mobile context sensing. The project explored how agent-based architectures running on mobile devices could deliver timely, contextually appropriate dietary and fitness guidance — an early foray into what is now the mainstream domain of AI-powered health and wellness applications.

The project was presented by Prof. Byoung-Tak Zhang at Microsoft Research Asia (MSRA) in Beijing in April 2012, reflecting the lab's international engagement with mobile intelligence research at the time.

## Overview

As smartphones proliferated in the early 2010s, they created a new opportunity for delivering intelligent, always-available health guidance. DietAdvisor addressed a core challenge in personal health management: how to provide recommendations that are both nutritionally sound and adapted to the user's immediate context — location, time of day, activity level, and personal preference.

The system operated as an **intelligent agent** on the smartphone, continuously monitoring contextual signals from the device's sensors and applying personalized reasoning to suggest suitable meals and exercise routines. Unlike static diet planners or lookup tables, DietAdvisor's agent-based design allowed it to reason goal-directedly: tracking user health objectives, adapting to changing situations, and refining recommendations over time.

Key characteristics of the system included:

- **Personalization**: recommendations tailored to each user's nutritional profile, dietary history, and health goals
- **Context-awareness**: integrating location (e.g., nearby restaurants vs. home), time, and activity data from smartphone sensors
- **Agent-based reasoning**: applying structured, goal-directed inference rather than simple lookup or rule filtering
- **Mobile deployment**: designed to run efficiently within the resource constraints of contemporary Android or iOS devices

## Research Team

**Principal Investigator**
- Prof. Byoung-Tak Zhang, Biointelligence Lab, Seoul National University

**Researchers**
- Ji-Seob Kim (jkim@bi.snu.ac.kr), Biointelligence Lab, SNU
- Jun Hee Yoo (jhyoo@bi.snu.ac.kr), Biointelligence Lab, SNU

## Technical Approach

DietAdvisor combined several technical threads active in the lab during this period:

- **Intelligent agent architecture**: the system embodied a deliberative agent model with goal management, belief updating, and action selection modules running on-device
- **Mobile sensing integration**: sensor data (GPS, accelerometer, clock) provided the situational context that shaped which recommendations were offered at each moment
- **Probabilistic user modeling**: the agent maintained a probabilistic model of the user's preferences, nutritional state, and activity patterns, updated incrementally as new data arrived
- **Evolutionary optimization**: optimization techniques (reflected in the CEC 2012 contribution by Yoo et al.) were applied to tune recommendation parameters and balance competing health objectives

The project contributed to the lab's broader interest in **ubiquitous computing and cognitive analytics** — applying machine intelligence to continuous streams of real-world data gathered from everyday devices.

## Significance

DietAdvisor was an early demonstration that agent-based AI could be embedded meaningfully in the mobile health domain, well before the current proliferation of health apps and AI nutrition coaches. The project illustrated how combining symbolic agent reasoning with data-driven mobile sensing could yield personalized guidance beyond what rule-based systems could achieve.

The MSRA presentation in April 2012 reflects the visibility of this work in the international research community at the time. The methodology developed here informed subsequent lab research on mobile behavior modeling (mLife) and personalized recommendation systems.
