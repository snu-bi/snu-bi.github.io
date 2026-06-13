---
title: LaText
subtitle: Text Mining Based on Latent Variable Models
group: completed
period: "2001~2004"
image: images/photo.jpg
tags:
  - text-mining
  - nlp
  - latent-variable-models
  - probabilistic-models
  - machine-learning
  - document-clustering
  - topic-modeling
  - bayesian-inference
---

The LaText project investigated the application of **latent variable models to text mining**, developing probabilistic frameworks that could automatically uncover hidden semantic structure in large document collections — work conducted at a pivotal moment when the web was generating document corpora at unprecedented scale.

## Overview

The central problem LaText addressed was how to make sense of massive, unlabeled text corpora. Traditional keyword-based approaches could retrieve documents but failed to capture the underlying *semantics*: the same concept can appear under many different surface forms, and the same word can mean different things in different contexts. Latent variable models offered a principled probabilistic solution by positing that each document is generated from a mixture of hidden topics, and that inferring those topics reveals the true semantic structure of the corpus.

LaText built on the then-emerging Probabilistic Latent Semantic Analysis (PLSA) framework introduced by Hofmann (1999), extending it in a Bayesian direction and applying it to practical text mining tasks including document clustering, topic discovery, and dimensionality reduction for large Korean and English document collections.

## Technical Approach

- **Probabilistic Latent Semantic Analysis (PLSA)**: modeling the joint distribution of documents and terms via a mixture of latent topic factors, estimated through Expectation-Maximization (EM)
- **Bayesian mixture models**: placing Dirichlet priors over topic mixing proportions to prevent overfitting and enable principled model selection; an early precursor to the LDA framework (Blei et al., 2003)
- **EM-based and variational Bayesian inference**: scalable parameter estimation for models with tens of thousands of vocabulary terms and large document sets
- **Dimensionality reduction**: mapping high-dimensional term-frequency vectors to compact latent topic representations for downstream retrieval and classification tasks

## Research Tasks

- **Document clustering**: grouping documents by latent topic membership rather than surface-form keyword overlap
- **Topic discovery**: automatically inducing interpretable themes from unlabeled corpora without human-defined category systems
- **Semantic similarity**: computing document similarity in the reduced latent space for improved information retrieval
- **Cross-lingual analysis**: exploring whether shared latent structure could bridge Korean and English document collections

## Research Team

- **Principal Investigator**: Prof. Byoung-Tak Zhang (Seoul National University, Biointelligence Lab)
- Graduate researchers in the Natural Language Processing and Machine Learning group at the SNU Biointelligence Lab

## Historical Context

LaText was conducted at a time when probabilistic topic models were an active research frontier. It predates the publication of Latent Dirichlet Allocation (Blei, Ng, and Jordan, 2003) and represents the lab's early engagement with fully generative Bayesian models for text. The project ran concurrently with the lab's bioinformatics work (BrainGene, DNAChipBench) and drew on the same Bayesian probabilistic inference infrastructure developed for those projects.

The text-mining methods developed in LaText contributed to later biomedical NLP work, including the PubMiner system (2004) for machine learning-based mining of biomedical literature. The lab's interest in discovering latent structure in high-dimensional data traces a continuous thread from LaText through hypernetwork models and into the modern multimodal learning era.

## Connection to Related Projects

- **FACT (1998–2001)**: the preceding lab project on text filtering and classification, which established the NLP foundation LaText built upon
- **BrainGene (2001–2003)**: concurrent bioinformatics project applying similar unsupervised clustering methods to gene expression data
- **SKT Hypernetwork (later)**: the lab's subsequent development of hypernetwork architectures, which generalized the idea of learning distributed representations over structured collections
