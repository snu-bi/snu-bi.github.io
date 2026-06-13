---
title: LEONN
subtitle: Learning and Evolution of Neural Networks
group: completed
period: "1998~2001"
image: images/photo.jpg
external_link: "http://bi.snu.ac.kr/Research/leonn.html"
funding: "KOSEF"
tags:
  - neuroevolution
  - evolutionary-computation
  - neural-networks
  - genetic-programming
  - bayesian-methods
  - machine-learning
---

LEONN investigated the **joint optimization of neural network architectures and connection weights** through Bayesian evolutionary algorithms — a forerunner of modern neuroevolution research.

## Core Approach

Rather than fixing a network architecture and training weights, LEONN simultaneously evolved:
- **Network topology** (which nodes connect to which)
- **Connection weights** (strength of each connection)
- **Training data selection** (which examples to learn from)

## Key Techniques

- **Bayesian evolutionary learning**: combining Bayesian model selection with evolutionary search
- **Evolving Neural Trees (ENTs)**: tree-structured neural architectures evolved via genetic programming
- **Incremental data inheritance**: transferring learned knowledge when the network structure changes
- **Committee-based ensembles**: combining multiple evolved neural trees for better generalization

## Publications

Results appeared at **Evolutionary Computation**, **CEC**, **GECCO**, and **PPSN** — the leading venues for evolutionary computation research.
