---
title: ProMiR
subtitle: Probabilistic Prediction of microRNA
group: completed
period: "2004~2007"
image: images/photo.jpg
external_link: "https://academic.oup.com/nar/article/34/suppl_2/W455/2505724"
funding: "Korean Ministry of Science and Technology (National Research Laboratory program, Systems Biology project)"
tags:
  - bioinformatics
  - computational-biology
  - microrna
  - gene-prediction
  - probabilistic-models
  - genomics
external_link: "{{ '/legacy/raw/bi.snu.ac.kr/Research/ProMiR/ProMiR.html' | relative_url }}"
---

ProMiR is a computational framework for **identifying microRNA genes** using a probabilistic co-learning model that jointly analyzes sequence and secondary structure features of pre-miRNA candidates.

## Background

MicroRNAs (miRNAs) are small non-coding RNA molecules that regulate gene expression by binding to messenger RNAs. Identifying miRNA genes in the genome is computationally challenging because they're short, numerous, and structurally diverse.

## ProMiR Approach

- **Probabilistic co-learning**: jointly models sequence features and RNA secondary structure folding
- Achieves **73% sensitivity** and **96% specificity** on known human miRNA datasets
- Identified **23 novel miRNA candidates** on human chromosomes 16–19

## Experimental Validation

- 9 novel candidates experimentally confirmed via **quantitative PCR** and **Drosha knockdown** in HeLa cells

## ProMiR II

The extended ProMiR II web server further integrated:
- Thermodynamic stability scores
- GC ratio and conservation scores
- Sequence entropy measures
- Prediction across **human, mouse, and viral genomes**
