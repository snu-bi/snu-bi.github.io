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
  - time-series
---

LEONN investigated the **joint optimization of neural network architectures and connection weights** through Bayesian evolutionary algorithms — a forerunner of modern neuroevolution research conducted at SNU Biointelligence Lab with support from the Korea Science and Engineering Foundation (KOSEF).

## Overview

A central challenge in machine learning is deciding not just what a neural network should learn, but what shape it should take. Traditional approaches fix the architecture first and then train the weights — but the best architecture for a given problem is rarely known in advance. LEONN attacked this challenge head-on by co-evolving both structure and parameters simultaneously.

The project developed a family of methods under the umbrella of **Evolving Neural Trees (ENTs)**: tree-structured neural network representations that can be searched and optimized using genetic programming. By encoding networks as trees, LEONN enabled principled application of evolutionary operators — crossover, mutation, and selection — to both the topology (which nodes connect to which) and the numerical weights of a network.

A distinguishing feature of LEONN was its use of **Bayesian model selection** to guide the evolutionary search. Rather than relying solely on training accuracy, the Bayesian criterion penalizes complexity, implementing a form of Occam's Razor that naturally favors compact, generalizable solutions. This prevented the evolutionary process from converging on overfitted, bloated networks — a problem endemic to unconstrained neuroevolution at the time.

LEONN also pioneered **incremental data inheritance**: a mechanism for transferring learned weights when the network structure changes during evolution. This substantially reduced wasted computation and accelerated convergence, allowing the evolutionary search to build on partial solutions rather than restarting from scratch each generation.

Finally, LEONN explored **committee machines** — ensembles of evolved neural trees whose predictions are combined to improve generalization. By maintaining a diverse population and aggregating their outputs, committee-based ENTs achieved lower variance than any single evolved network.

## Research Team

- **Principal Investigator**: Byoung-Tak Zhang (Seoul National University)
- **Researchers**: Dong-Yeon Cho, Je-Gun Joung, Peter Ohm (collaborator, Heinz Mühlenbein's group)

## Technical Approach

- **Evolving Neural Trees (ENTs)**: neural networks encoded as tree structures amenable to genetic programming operators; each tree node represents a neuron or activation unit, and the tree branching encodes connectivity
- **Bayesian evolutionary learning**: the evolutionary fitness function incorporates a Bayesian posterior — rewarding accuracy while penalizing model complexity via a prior over network size (MDL / Occam's Razor criterion)
- **Incremental data inheritance**: when a network's topology changes during a genetic operation, previously learned weights are inherited and fine-tuned rather than discarded, accelerating convergence
- **Committee machines of ENTs**: maintaining a diverse population and combining predictions of multiple evolved trees via majority vote or weighted averaging, reducing prediction variance
- **Applications to time-series forecasting**: ENT committee machines demonstrated strong performance on financial and chaotic time-series benchmarks, including high-frequency stock index data

## Publications

- Zhang, B.-T., Ohm, P., and Mühlenbein, H. (1997). "Evolutionary Induction of Sparse Neural Trees." *Evolutionary Computation*, 5(2). — Foundational journal paper introducing the sparse ENT framework with Occam's Razor regularization.
- Zhang, B.-T. and Joung, J.-G. (1999). "Time Series Prediction Using Committee Machines of Evolutionary Neural Trees." *Proceedings of the Congress on Evolutionary Computation (CEC 1999)*.
- Chen, S.-H., Wang, H.-S., and Zhang, B.-T. (1999). "Forecasting High-Frequency Financial Time Series with Evolutionary Neural Trees: The Case of Heng-Sheng Stock Index." *Proceedings of IC-AI 1999*.
- Cho, D.-Y. and Zhang, B.-T. (2000). "Bayesian Evolutionary Algorithms for Evolving Neural Tree Models of Time Series Data." *Proceedings of the Congress on Evolutionary Computation (CEC 2000)*.
- Zhang, B.-T. (2002). "A Bayesian Evolutionary Approach to the Design and Learning of Heterogeneous Neural Trees." *Integrated Computer-Aided Engineering*, 9(1).

## Legacy

LEONN established foundational principles — co-evolution of structure and weights, Bayesian regularization, and ensemble combination — that prefigure modern **neural architecture search (NAS)** and **AutoML**. The Bayesian ENT framework directly influenced subsequent lab projects combining evolutionary algorithms with probabilistic inference, including the **HyperSNP** and **BrainGene** projects in bioinformatics.
