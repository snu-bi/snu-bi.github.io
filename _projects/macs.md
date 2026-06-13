---
title: MACS
subtitle: Evolving Homing and Herding Behaviors of Multiple Robotic Agents
group: completed
period: "1996~1999"
image: images/photo.jpg
funding: "Korea Science and Engineering Foundation (KOSEF)"
tags:
  - evolutionary-robotics
  - multi-agent-systems
  - swarm-robotics
  - genetic-programming
  - neural-networks
  - reinforcement-learning
  - cooperative-behavior
---

MACS investigated how **cooperative behaviors such as homing and herding** could be automatically evolved for teams of autonomous mobile robots — a foundational project in the lab's evolutionary robotics research, conducted with support from the Korea Science and Engineering Foundation (KOSEF).

## Overview

A central challenge in multi-robot systems is enabling teams of robots to cooperate effectively without hard-coding every rule of interaction. MACS addressed this by asking a deceptively simple question: rather than programming cooperation, can we *evolve* it?

The project focused on two archetypal collective behaviors. **Homing** requires all members of a robot team to converge on a target location — a task that demands coordinated movement without collisions and without explicit communication about the goal. **Herding** requires the team to collectively shepherd a set of objects (or simulated animals) toward a designated region, demanding even more sophisticated distributed decision-making because the "herd" reacts dynamically to the robots' own actions.

Both tasks were tackled using **evolutionary algorithms**, specifically genetic programming and evolved neural network controllers. Individual robots were equipped with sensorimotor neural networks whose architectures and weights were shaped by an evolutionary process operating on a population of candidate controllers. Fitness was evaluated by running candidate controllers in simulation and measuring how effectively the robot team accomplished the collective task — no hand-crafted reward shaping, no explicit communication protocol.

A key technical contribution was the **Multinet architecture**: a multi-module neural system combining recurrent networks (for temporal memory) with self-organizing maps (for adaptive sensory clustering). This allowed individual robots to develop local response policies that, when deployed as a homogeneous team, gave rise to coherent group behaviors. The emergent herding and homing patterns were not pre-programmed — they arose from the interaction of individually evolved controllers with the physical and social dynamics of the robot team.

The project demonstrated that competitive collective intelligence could be evolved for multi-robot systems without centralized coordination, laying conceptual groundwork for what would later be called *swarm robotics*.

## Research Team

| Role | Name | Affiliation |
|------|------|-------------|
| Principal Investigator | Prof. Byoung-Tak Zhang | SNU Biointelligence Lab |
| Researcher | Byoung-Hoon Hong | SNU Biointelligence Lab |

## Technical Approach

- **Genetic programming for controller evolution**: robot control policies are encoded as programs and evolved over generations using selection, crossover, and mutation operators; no hand-designed control logic required
- **Multinet neural architecture**: a multi-module neural system pairing recurrent networks (for short-term memory of past sensor readings) with self-organizing maps (for unsupervised clustering of sensory inputs), enabling adaptive and context-sensitive robot responses
- **Homogeneous team policy**: all robots in the team share the same evolved controller — simplifying the evolutionary search while still enabling emergent differentiation of roles through local sensory differences
- **Multi-objective fitness evaluation**: candidate controllers are scored on both individual task completion and team-level collective performance, balancing local and global objectives
- **Emergent cooperation**: group behaviors (formation-keeping, herding, convergence to a goal) arise from interactions among individually evolved policies rather than from explicit programming of group rules
- **Simulation-based evolution**: evolutionary evaluation conducted in physics-based robot simulations, with results transferred to real robot platforms

## Publications

- B.-T. Zhang and B.-H. Hong (1997). "Multinet Neural Architecture for Evolving Collective Robotic Intelligence." *Proceedings of the International Conference on Neural Information Processing (ICONIP 1997)*. — Introduced the Multinet architecture combining recurrent networks with self-organizing maps for goal-directed group motion in evolved multi-robot teams.

## Legacy

MACS established the lab's early commitment to **evolutionary approaches to robot intelligence** — the insight that collective behaviors need not be programmed but can emerge from selection pressure on individual controllers. This thread continued through the **LEONN** project (evolving neural network architectures), the **RoboMotion** project (learning robot motions from human demonstrations), and **CogHRI** (cognitive human-robot interaction), and remains central to the lab's current Embodied AI research.
