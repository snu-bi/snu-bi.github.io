---
title: E-Learn
subtitle: Personalized e-Learning with Bayesian Networks
group: completed
period: "2009~2010"
image: images/photo.jpg
external_link: "https://bi.snu.ac.kr/Research/e_learn/e_learn.html"
funding: "NRF (National Research Foundation of Korea)"
tags:
  - machine-learning
  - bayesian-networks
  - e-learning
  - intelligent-tutoring
  - adaptive-systems
  - probabilistic-graphical-models
---

The E-Learn project investigated using **Bayesian networks** to build probabilistic learner models that represent and reason about individual student knowledge states and learning styles, enabling adaptive personalized instructional content to be delivered by inferring learner understanding from interaction data.

## Overview

A central challenge in e-learning is that different students differ dramatically in what they already know, how quickly they absorb new material, and which presentation styles suit them best. Static courseware delivers the same content to everyone, leaving advanced learners unchallenged and struggling learners unsupported.

E-Learn addressed this challenge by treating learner knowledge as a **probability distribution** rather than a fixed profile. The system maintained a dynamic Bayesian network over the learner's knowledge state — a graph where each node represents a concept or skill, and edges encode prerequisite relationships and dependencies between topics. As the learner interacted with the system, the network was updated incrementally using Bayesian inference: each response, correct or incorrect, shifted the probability estimates for related concepts throughout the graph.

This probabilistic representation enabled the system to:

- **Reason under uncertainty**: the system never assumed it knew exactly what a student understood; it maintained calibrated uncertainty and used it to drive decision-making
- **Propagate belief**: a correct answer on one topic raised confidence not only in that topic but in related prerequisite skills; an incorrect answer triggered targeted review suggestions for underlying gaps
- **Select optimal content**: at each step, the system chose the learning activity expected to most efficiently reduce uncertainty about the learner's weakest areas — a form of active learning applied to curriculum delivery

The project extended the Biointelligence Lab's core expertise in hierarchical Bayesian networks and probabilistic graphical models — developed originally for biological data analysis — to the domain of intelligent tutoring and adaptive e-learning.

## Technical Approach

- **Probabilistic learner modeling**: a Bayesian network encodes knowledge prerequisites as a directed graph, with each node carrying a probability reflecting the learner's estimated mastery
- **Bayesian inference for belief updating**: observed learner responses update node posteriors using exact or approximate inference, propagating new evidence through the dependency graph
- **Adaptive content selection**: the system selects the next learning item by computing expected information gain — choosing the item that will most reduce uncertainty about the learner's knowledge state
- **Learning style modeling**: individual differences in preferred presentation modality (text, diagram, example-based) are incorporated as additional latent variables in the learner model
- **Hypernetwork extensions**: higher-order associations among knowledge concepts, characteristic of the lab's hypernetwork framework, allow the system to represent and exploit complex multi-concept dependencies that pairwise Bayesian models miss

## Research Team

**Principal Investigator**: Prof. Byoung-Tak Zhang, Biointelligence Lab, Seoul National University

The project was carried out by graduate researchers in the Biointelligence Lab as part of the lab's broader investigation into cognitive computing and intelligent adaptive systems during 2009–2010.

## Connection to Lab Research

E-Learn belongs to the lab's sustained interest in applying machine learning to human-centered domains. It draws directly on techniques developed in the MMG (Multimodal Memory Game) platform — which also modeled human cognitive state — and anticipates later work on cognitive analytics (CogAnalytics) and human-robot interaction (CogHRI). The probabilistic learner modeling approach shares methodology with the lab's bioinformatics work, where Bayesian networks were used to infer hidden biological states from observed experimental data.

## Impact

E-Learn anticipated the modern wave of AI in education — adaptive learning platforms, AI tutors, personalized curricula — by grounding educational adaptation in principled probabilistic reasoning. The project demonstrated that the same Bayesian inference machinery effective for biological discovery could be repurposed for modeling the internal cognitive states of human learners, offering a rigorous probabilistic foundation for intelligent tutoring that rules-based expert systems of the era lacked.
