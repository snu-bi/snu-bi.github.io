---
title: BrainNet
subtitle: Uncovering the Hyperedges of Cortical Brain Graphs
group: completed
period: "2010~2013"
image: images/photo.jpg
funding: "National Research Foundation of Korea (NRF)"
tags:
  - computational-neuroscience
  - brain-networks
  - hypergraph
  - neuroimaging
  - machine-learning
  - bioinformatics
---

The BrainNet project investigated **higher-order relational structure in cortical brain networks** by identifying hyperedges — groupings of multiple brain regions that form functionally and structurally meaningful modules beyond what pairwise connections can capture. Using structural MRI data from healthy adults, the project developed information-theoretic evolutionary algorithms to discover cortical modules predictive of cognitive traits such as IQ.

## Overview

Standard brain connectivity analyses represent the brain as a graph of pairwise connections: region A connects to region B, each edge encoding a single relationship between two nodes. While powerful, this representation is fundamentally limited — cognition and behavior emerge from the coordinated activation of many brain regions simultaneously, forming functional assemblies that pairwise edges cannot express.

BrainNet addressed this limitation by modeling the brain as a **hypergraph**, where a single hyperedge can connect three or more cortical regions at once. These multi-regional modules — termed *hyperedges* — represent higher-order structural co-variation patterns across the cortex. The central hypothesis was that such hyperedges encode cognitively meaningful groupings of brain areas: regions whose cortical thickness co-varies in ways that reflect underlying neural development, genetic architecture, or shared functional demands.

The project analyzed cortical thickness measurements from structural MRI scans of healthy adults. Cortical thickness is a sensitive morphological marker of neural integrity, maturation, and cognitive capacity, and is measured at thousands of surface points across the cortex. With over 80,000 measured variables from each participant, the challenge was to identify which combinations of cortical regions — which hyperedges — carry significant signal about individual cognitive differences, such as intelligence (IQ).

To solve this high-dimensional combinatorial search problem, BrainNet developed an **evolutionary hypernetwork** framework. Candidate hyperedges were encoded as populations that evolve over generations using mutual information as a fitness criterion: hyperedges that better capture coordinated variation across brain regions and that better distinguish individuals with high versus low IQ are favored. This evolutionary search navigates the exponentially large space of possible multi-region groupings efficiently, identifying a sparse set of significant cortical modules from complex high-dimensional neuroimaging data.

## Research Team

**Principal Investigator**
- Prof. Byoung-Tak Zhang (Biointelligence Laboratory, Seoul National University)

**Researchers — Biointelligence Laboratory (Computer Science & Engineering)**
- Eun-Sol Kim
- Jung-Woo Ha

**Collaborating Researchers — Department of Psychiatry, SNU College of Medicine**
- Wi Hoon Jung
- Joon Hwan Jang
- Jun Soo Kwon

## Technical Approach

### Data

Structural MRI scans from **62 healthy adults**, yielding cortical thickness measurements at over **80,000 surface points** across the cerebral cortex. Cortical thickness is measured at each vertex of a reconstructed cortical surface mesh, providing fine-grained spatial resolution across all major cortical regions.

### Hypernetwork Model

The brain is represented as a hypergraph where:

- **Vertices** are cortical measurement sites (surface parcels or regions of interest)
- **Hyperedges** are subsets of vertices — groupings of multiple cortical regions — rather than single pairs
- **Edge weights** reflect the strength of co-variation in cortical thickness across participants

A population of candidate hyperedges is maintained and evolved across generations. Each individual in the population represents a potential cortical module (a group of brain regions that covary together).

### Mutual Information-Based Evolution

The evolutionary search is guided by **mutual information** between hyperedge membership and the cognitive outcome (IQ group):

1. Cortical thickness values at the vertices of each candidate hyperedge are summarized into a module-level feature
2. Mutual information between this feature and IQ group labels (high vs. low IQ) is computed as the fitness score
3. High-fitness hyperedges are selected and recombined to form the next generation
4. The process iterates until convergence, yielding a small set of significant cortical modules

This information-theoretic fitness criterion ensures that discovered hyperedges are statistically relevant to the cognitive outcome, not merely low-dimensional projections of high-variance variation.

### Classification

IQ group (high vs. low) is predicted from the features extracted by the evolved hyperedges using standard classifiers. The evolutionary hypernetwork approach improved classification accuracy by **5–15 percentage points** over baseline methods that do not use hyperedge structure.

### Gender Classification Extension

The same framework was applied to gender classification from cortical thickness MRI, demonstrating the generality of evolutionary hypernetworks for brain phenotyping. Feature selection via hyperedge frequency analysis yielded approximately **20% classification accuracy improvement** over baseline approaches.

## Key Results

- Evolutionary hypernetwork search over cortical hyperedges outperforms pairwise-graph baselines for IQ classification (5–15% improvement)
- Discovered hyperedges identify specific multi-regional cortical assemblies whose thickness co-variation is predictive of IQ
- The mutual information criterion efficiently guides evolutionary search in an extremely high-dimensional space (>80,000 variables, 62 subjects)
- Generalization to gender classification confirms the method's utility for brain phenotyping tasks beyond IQ

## Collaboration

BrainNet was an interdisciplinary collaboration between the **Biointelligence Laboratory** (Computer Science & Engineering) and the **Department of Psychiatry** at Seoul National University College of Medicine. The Computer Science team contributed the hypernetwork and evolutionary algorithm methodology; the Psychiatry team (Jung, Jang, Kwon) provided neuroimaging expertise, access to the MRI dataset, and clinical domain knowledge about cortical morphometry and cognitive neuroscience.

Prof. Jun Soo Kwon's group at SNU Psychiatry is a leading Korean research group in MRI-based cognitive neuroscience, with expertise in structural brain abnormalities in psychiatric disorders and cognitive development — a natural partner for this computational brain analysis initiative.

## Publications

- E.-S. Kim, J.-W. Ha, W.H. Jung, J.H. Jang, J.S. Kwon, and B.-T. Zhang, "Mutual information-based evolution of hypernetworks for brain data analysis," *2011 IEEE Congress on Evolutionary Computation (CEC)*, pp. 2611–2617, 2011. DOI: [10.1109/cec.2011.5949944](https://doi.org/10.1109/cec.2011.5949944)

- J.-W. Ha, J.H. Jang, D.-H. Kang, W.H. Jung, J.S. Kwon, and B.-T. Zhang, "Gender classification with cortical thickness measurement from magnetic resonance imaging by using a feature selection method based on evolutionary hypernetworks," *2009 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE)*, 2009. DOI: [10.1109/fuzzy.2009.5277402](https://doi.org/10.1109/fuzzy.2009.5277402)
