---
title: ProMiR
subtitle: Probabilistic Prediction of microRNA
group: completed
period: "2004 - 2007"
image: images/photo.jpg
external_link: "https://academic.oup.com/nar/article/34/suppl_2/W455/2505724"
funding: "The Ministry of Science and Technology of Korea (NRL)"
tags:
  - bioinformatics
  - computational-biology
  - microrna
  - gene-prediction
  - probabilistic-models
  - genomics
---

## Overview

ProMiR is a computational framework for **multi-species microRNA and target gene prediction** using machine learning algorithms. The central goal of the project was to develop an efficient prediction algorithm and an integrated web-based system, and to lay the foundation for functional studies and the artificial design of RNA interference systems.

MicroRNAs (miRNAs) are small non-coding RNA molecules that regulate gene expression by binding to messenger RNAs. Identifying miRNA genes in the genome is computationally challenging because they are short, numerous, and structurally diverse. Prior approaches that detected only close homologs risked missing novel miRNA genes that lack detectable homology. ProMiR addresses this by implementing a probabilistic co-learning model that combines both sequential and structural characteristics, enabling the detection of both closely and distantly homologous miRNA precursors.

The project produced two major systems — **ProMiR I** and **ProMiR II** — as well as related tools for microRNA target prediction.

## Research Team

| Role | Name |
|------|------|
| Principal Investigator | Prof. Byoung-Tak Zhang |
| Researcher | Jin-Wu Nam |
| Researcher | Je-Keun Rhee |
| Researcher | Soo-Jin Kim |

**Contact:** Jin-Wu Nam (jwnam@bi.snu.ac.kr)

## Methodology

### ProMiR I — Probabilistic Co-learning Model

ProMiR I implements a probabilistic co-learning model that jointly models sequential and structural characteristics of miRNA genes in a unified probabilistic framework. The model simultaneously determines (1) whether a genomic region contains a miRNA gene, and (2) where the mature miRNA cleavage site by Drosha is located on the precursor.

Key capabilities and results:

- Development of the **probabilistic co-learning model** of sequence and RNA secondary structure
- Human pre-miRNA and mature miRNA prediction
- Experimental validation via **real-time quantitative PCR** and **Drosha knockdown** assays in HeLa cells
- **9 new miRNA genes identified** and confirmed experimentally

### ProMiR II — Extended Multi-species Prediction Server

ProMiR II is an improved, more general version of ProMiR composed of three sub-programs:

- **ProMiR-v**: searches for both conserved and non-conserved miRNAs in the vicinity of a known miRNA
- **ProMiR-c**: predicts both conserved and non-conserved miRNAs near a candidate sequence (70–150 nt)
- **ProMiR-g**: provides genome-scale miRNA gene prediction in long sequences (70 nt – 10 kb) across various species

Additional features in ProMiR II:

- Conserved, non-conserved, clustered, and non-clustered miRNA prediction
- Stem-loop filter and conservation score filter integration
- Prediction output visualized on a Genome Browser annotated with known genes and conservation scores
- Support for unrelated species including **virus miRNA prediction**

## Collaboration

| Field | Detail |
|-------|--------|
| Cooperative Research Institute | School of Biological Sciences, Seoul National University |

## Publications

- B.-T. Zhang and J.-W. Nam. "Supervised learning methods for microRNA studies." *Machine Learning for Bioinformatics*, chapter 9, John Wiley & Sons, 2007.
- J.-G. Joung, K.-B. Hwang, J.-W. Nam, S.-J. Kim, and B.-T. Zhang. "Discovery of microRNA-mRNA modules via population-based probabilistic learning." *Bioinformatics*, 2007.
- J.-W. Nam, I.-H. Lee, K.-B. Hwang, S.-B. Park, and B.-T. Zhang. "Dinucleotide step parameterization of pre-miRNAs using multi-objective evolutionary algorithms." *Lecture Notes in Computer Science*, EvoBio 2007.
- S.-K. Kim\*, J.-W. Nam\*, J.-K. Rhee, W.-J. Lee, and B.-T. Zhang. "miTarget: microRNA target-gene prediction using a Support Vector Machine." *BMC Bioinformatics*, 7(1):411, 2006. (**Highlight paper**)
- J.-W. Nam\*, J. H. Kim\*, S. K. Kim, and B.-T. Zhang. "ProMiR II: a web server for clustered, nonclustered, conserved, nonconserved microRNA prediction." *Nucleic Acids Research*, 34:W455–W458, 2006.
- J. Han, Y. T. Kim, K.-H. Yeom, J.-W. Nam, I. H. Hur, J.-K. Rhee, B.-T. Zhang, and V. N. Kim. "Molecular basis for the recognition and processing of primary microRNA by Drosha." *Cell*, 2006.
- V. N. Kim and J.-W. Nam. "Genomics of microRNA." *Trends in Genetics*, 22(3):165–173, 2006. (**Most downloaded paper**)
- J.-W. Nam, K. R. Shin, J. Han, Y. Lee, V. N. Kim, and B.-T. Zhang. "Human microRNA prediction through a probabilistic co-learning model of sequence and structure." *Nucleic Acids Research*, 33(11):3570–3581, 2005. (**Hottest Paper**)
- S. K. Kim, J.-W. Nam, W. J. Lee, and B. T. Zhang. "A Kernel Method for MicroRNA Target Prediction Using Sensible Data and Position-Based Features." *IEEE Symposium on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB 2005)*, pp. 46–52, 2005.
- W.-J. Lee, J.-W. Nam, S.-K. Kim, and B.-T. Zhang. "Identification of C. elegans MicroRNA Targets Using a Kernel Method." *Genomics and Informatics*, 3(1):15–23, 2005.
- J.-W. Nam, W. J. Lee, and B. T. Zhang. "Computational Methods for Identification of Human microRNA Precursors." *Lecture Notes in Artificial Intelligence*, vol. 3157, pp. 732–741, 2004.
- J.-W. Nam, J.-G. Joung, Y. S. Ahn, and B.-T. Zhang. "Two-Step Genetic Programming for Optimization of RNA Common-Structure." *Lecture Notes in Computer Science*, vol. 3005, pp. 73–83, 2004.
