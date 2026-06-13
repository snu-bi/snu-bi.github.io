---
title: DNAChipBench
subtitle: Intelligent Design and Analysis Technology for DNA Chips (NRL Project)
group: completed
period: "June 2002 - June 2007"
image: images/photo.jpg
funding: "Korean Ministry of Science and Technology (National Research Laboratory Program)"
tags:
  - bioinformatics
  - machine-learning
  - genomics
  - dna-microarray
  - gene-expression
  - text-mining
---

DNAChipBench was an **integrated computational platform** for intelligent design and analysis of DNA chips (microarrays), developed under Korea's National Research Laboratory (NRL) program. The project aimed to develop intelligent bioinformatics technologies and a unified DNAChipBench platform covering the full pipeline of DNA chip design, fabrication, analysis, and application.

## Overview

The central goal of the NRL project was to build both a body of **intelligent bioinformatics methods** and a unified software platform — **DNAChipBench** — that could support every stage of the DNA chip workflow: target selection, probe design, expression data analysis, biomedical literature mining, and disease diagnostic applications.

The DNAChipBench system was composed of five integrated subsystems: **TargetBench**, **ProbeBench**, **ExpressBench**, **BiblioBench**, and **DiagBench**. Each subsystem addressed a distinct stage of the DNA chip pipeline, and all shared a common machine-learning infrastructure developed at the SNU Biointelligence Lab.

The project ran in two phases:

| Phase | Period | Focus |
|-------|--------|-------|
| Phase 1 | June 2002 - June 2004 | Development of DNA chip informatics base algorithms |
| Phase 2 | June 2004 - June 2007 | Integrated platform for DNA chip design and analysis |

## Platform Modules

### TargetBench

TargetBench identifies the DNA chip contents and target genes required for a given application. It integrates target selection from clinical databases (e.g., OMIM) and public expression databases using expression DB filtering. Algorithmically, it combines information from BiblioBench and ExpressBench with sequence analysis and transcription factor binding site prediction, using naive Bayes classifiers, hidden Markov models, and machine learning methods.

### ProbeBench

ProbeBench designs optimal oligonucleotide and cDNA probes based on virtual hybridization modeling. It performs assay parameter optimization and fabrication parameter optimization. Probe quality is assessed using naive Bayes and probabilistic machine learning methods; evolutionary algorithms are used for optimization.

### ExpressBench

ExpressBench analyzes gene expression data from DNA chips. The subsystem covers preprocessing, expression profiling, genotyping, and integration with gene databases. It applies probabilistic machine learning methods for clustering gene expression patterns, Bayesian network-based dependency analysis, latent variable models for time-series analysis, and generative topographic mapping for visualization.

### BiblioBench

BiblioBench extracts biological knowledge from biomedical literature databases such as MEDLINE and PubMed. It incorporates information retrieval for searching and filtering relevant literature, information extraction for pulling key facts from text, and natural language processing methods. Hidden Markov models and latent variable models are the primary machine learning methods employed.

### DiagBench

DiagBench was developed in the later phase of the project (introduced from Year 5, 2006) and focuses on DNA chip applications for disease diagnostics, including novel biochip development, biochip data analysis for knowledge discovery, and bioinformatics commercialization.

## Annual Research Milestones

| Year | Focus | Key Deliverables |
|------|-------|-----------------|
| Year 1 (2002) | Core algorithms for DNA chip design and analysis | Target selection algorithms; probe design algorithms; expression profiling algorithms; text mining prototypes; HPV diagnostic oligo chip DB |
| Year 2 (2003) | Prototype systems for all subsystems | TargetBench prototype; ProbeBench prototype system; ExpressBench prototype system; BiblioBench prototype system |
| Year 3 (2004) | DNA chip design — TargetBench and ProbeBench integration | Literature mining for target selection; target selection using DNA chip analysis data; virtual hybridization-based probe design; assay parameter optimization |
| Year 4 (2005) | DNA chip analysis — ExpressBench and BiblioBench integration | Biotext and chip data interface; ~30,000 gene promoter DB and visualization; bioinformatics database optimization and visualization; web-based bioinformatics database |
| Year 5 (2006) | DNA chip informatics — full system integration (DiagBench introduction) | Integrated DNAChipBench system; novel biochip development; biochip data analysis for knowledge discovery; bioinformatics application development |

## Research Team

**Principal Investigator:** Prof. Byoung-Tak Zhang (Seoul National University, Biointelligence Lab)

**TargetBench Team**
- Je-Gun Joung
- Sirk June Augh
- Seong-Wook Chi
- Jin-Woo Nam

**ProbeBench Team**
- Sun Kim
- Jang-Min Oh
- Seung-Joon Lee
- Ha-Young Jang
- In-Hee Lee

**ExpressBench Team**
- Kyu-Baek Hwang
- Jin-San Yang
- Jeong-Ho Chang
- Jeong-Moon Lee
- Dong-Min Kim

**BiblioBench Team**
- Seong-Bae Park
- Jae-Hong Eom
- Jeong-Ho Chang
- So-Hyun Hwang

## Publications

Selected international conference papers produced under this project:

- **DNA Sequence Optimization Using Constrained Multi-Objective Evolutionary Algorithm**, Lee, I.-H., Shin, S.-Y., and Zhang, B.-T., *2003 Congress on Evolutionary Computation (CEC 2003)*.
- **Molecular Immunocomputing with Application to Alphabetical Pattern Recognition Mimics the Characterization of ABO Blood Type**, Kim, S.D., Shin, K.-R., and Zhang, B.-T., *2003 Congress on Evolutionary Computation (CEC 2003)*.
- **Mining the Risk Types of Human Papillomavirus (HPV) by Cost-Sensitive Learning**, Hwang, S., Park, S.-B., and Zhang, B.-T., *Proceedings of PAKDD2003 Workshop on Biological Data Mining*, pp. 107-118, 2003.
- **Text Chunking by Combining Hand-Crafted Rules and Memory-Based Learning**, Park, S.-B. and Zhang, B.-T., *Proceedings of the 41st Annual Meeting of the Association for Computational Linguistics (ACL 2003)*, pp. 497-504, 2003.
- **DNA Computing Complexity Analysis Using DNA/DNA Hybridization Kinetics**, Shin, S.-Y., Lee, E.J., Park, T.H., and Zhang, B.-T., *Preliminary Proceedings of the Ninth International Meeting on DNA Based Computers (DNA9)*, p. 207, 2003.

The project produced approximately **40 SCI-level publications** over its five-year duration.

## Key Figures

- **DNAChipBench.JPG** — System architecture diagram showing the five integrated subsystems (TargetBench, ProbeBench, ExpressBench, BiblioBench, DiagBench) and their interconnections.
- **TargetBench.JPG** — Workflow diagram for the TargetBench target selection subsystem.
- **ProbeBench.JPG** — Architecture diagram for the ProbeBench probe design subsystem.
- **ExpressBench.JPG** — Workflow diagram for the ExpressBench gene expression analysis subsystem.
- **BiblioBench.JPG** — Architecture diagram for the BiblioBench biomedical literature mining subsystem.
- **ResearchPropulsion.JPG** — Research momentum and knowledge transfer diagram illustrating the project's broader impact.

## Contact

| Field | Detail |
|-------|--------|
| Contact person | Kyu-Baek Hwang |
| Email | kbhwang@bi.snu.ac.kr |
| Institution | Biointelligence Laboratory, School of Computer Science and Engineering, Seoul National University |
