---
title: MEC
subtitle: Molecular Evolutionary Computing (Phases I, II, III)
group: completed
period: "2000~2009"
image: images/photo.jpg
external_link: "http://bi.snu.ac.kr/Research/MEC/"
funding: "Korea Science and Engineering Foundation (KOSEF)"
tags:
  - dna-computing
  - evolutionary-computation
  - molecular-computing
  - bioinformatics
  - machine-learning
  - combinatorial-optimization
---

The MEC project investigated **evolutionary algorithms operating at the molecular level**, using DNA molecules as the primary computational substrate. Running across three phases over nearly a decade, it was one of the lab's foundational long-term programmes and among the earliest sustained international efforts to implement practical machine learning algorithms using DNA molecules.

## Overview

Molecular Evolutionary Computing (MEC) explored a radical question: can the molecular machinery of life serve as a computing medium for learning and optimization? The project operated at the intersection of computer science, molecular biology, and biochemistry, implementing computational concepts — from evolutionary search and version-space learning to combinatorial optimization — directly in DNA strands processed through standard molecular biology operations such as PCR, gel electrophoresis, and hybridization.

The long-term vision was to build **bio-based inference machines** that exploit the inherent parallelism of molecular populations, potentially enabling computations that are intractable on silicon architectures. MEC also pursued the complementary direction of applying DNA computing to biomedical problems, particularly molecular-level gene expression diagnosis.

## Research Phases

### Phase I (2000–2002): Foundations of Molecular Evolutionary Search

- Developed DNA-based solution strategies for the **Travelling Salesman Problem (TSP)** using strand encoding and selection
- Investigated **multiobjective optimization of DNA sequence design** to minimize cross-hybridization and secondary-structure artifacts — a prerequisite for reliable computation
- Designed the first in-vitro protocols for **evolutionary search using molecular biology operations** (ligation, PCR amplification, gel separation)
- Initiated internal seminars reviewing the DNA Based Computing conference series (DNA6 proceedings, 2001) to track the international state of the art

### Phase II (2002–2006): Machine Learning with DNA Molecules

- Implemented **version-space learning with DNA molecules**: a classical machine learning framework (elimination of hypothesis space inconsistent with training examples) encoded and executed in molecular populations
- Explored molecular theorem proving, splicing systems, and hairpin-structure-based logical inference
- Designed and studied the **NACST (Nucleic Acid Computing Simulation Toolbox)** for in silico validation of molecular computing protocols before wet-lab implementation
- Investigated chip-based and microreactor-based DNA computing architectures
- Continued weekly MEC seminars covering international research on DNA self-assembly, aqueous computing, and biomolecular logic gates; participants included D.-Y. Cho, D. Kim, S.-Y. Shin, H.-W. Lim, I.-H. Lee, J.-E. Yun, J.-Y. Lee, J.-Y. Park, and H.-M. Jang

### Phase III (2006–2009): DNA Computing for Molecular Diagnosis

- Shifted the application domain toward **molecular diagnosis**: using DNA computing algorithms to classify gene expression profiles
- Developed methods for **microRNA biomarker detection** using DNA-based computing systems
- Bridged molecular computing and biomedical informatics, establishing the conceptual and experimental foundation for later projects such as ProMiR and HyperSNP

## Research Team

| Role | Name | Affiliation |
|------|------|-------------|
| Principal Investigator | Prof. Byoung-Tak Zhang | Seoul National University, Dept. of Computer Science and Engineering |
| Contact | btzhang@scai.snu.ac.kr | — |

**Researchers and seminar participants (representative):**
- Soo-Yong Shin (S.-Y. Shin) — page maintainer, 2001
- In-hee Lee (I.-H. Lee) — page maintainer, 2002–2004
- Dong-Yeon Cho (D.-Y. Cho)
- Jae-Young Lee (J.-Y. Lee)
- Ji-Young Park (J.-Y. Park)
- Hyun-Woo Lim (H.-W. Lim)
- Hyun-Moon Jang (H.-M. Jang)
- Dong-Min Kim (D. Kim)
- Ji-Eun Yun (J.-E. Yun)
- Se-Jin Lee (S.-E. Lee), Seong-Jun Augh (S.-J. Augh), Hyun-Wook Lee (H.-W. Lee), Jae-Hoon Eom (J.-H. Eom), Sang-Jun Lee (S.-J. Lee), Jae-Eun Youn (J.-E. Youn), Yoon-Kyung Noh (Y.-K. Noh) (2001 cohort)

## Technical Approach

The MEC methodology combined algorithmic design with wet-lab molecular biology:

1. **Encoding**: computational states (candidate solutions, hypotheses) were encoded as specific DNA oligonucleotide sequences
2. **Selection / Fitness evaluation**: hybridization affinity or PCR amplification biased the population toward fitter strands
3. **Variation / Crossover**: ligation, strand displacement, and restriction digestion introduced variation analogous to genetic operators
4. **Readout**: gel electrophoresis, fluorescence labeling, or microarray scanning decoded the final molecular population into a computational answer

Complementary simulation work (NACST toolbox) allowed iterative refinement of protocols in silico before committing resources to in vitro experiments.

## Collaboration

The lab was an active participant in the international DNA computing community. The DNAC_researcher network page maintained by the group lists collaborating researchers at:
- University of Southern California (Leonard Adleman)
- University of Tokyo (Masami Hagiya)
- Duke University (John H. Reif)
- Caltech (Erik Winfree, Paul Rothemund)
- University of Memphis (Max H. Garzon, Russell J. Deaton)
- New York University (Nadrian C. Seeman)
- National Institutes of Health (Tom Schneider)
- GMD / Fraunhofer (John Simpson McCaskill)
- Leiden University (Grzegorz Rozenberg)
- University of Western Ontario (Lila Kari)

## Key Publications

Representative publications from the MEC project (exact citation details for Phase I–II papers should be verified against the lab publication list):

- S.-Y. Shin, I.-H. Lee, D. Kim, and B.-T. Zhang, "Multiobjective evolutionary optimization of DNA sequences for reliable DNA computing," *IEEE Transactions on Evolutionary Computation*, 9(2), pp. 143–158, 2005.
- B.-T. Zhang, "Molecular evolutionary computing (MEC)," invited talk / survey, presented at DNA computing workshops, 2001–2004.
- I.-H. Lee, S.-Y. Shin, and B.-T. Zhang, "DNA-based version space learning for gene expression profile diagnosis," internal MEC report / conference contribution, 2002–2004.
- (See also the lab's journal publication list at `dnac_journal.html` for the full set of DNA computing publications from this project period.)

## Significance

MEC established the lab's unique interdisciplinary identity at the boundary of computer science and molecular biology. The techniques and insights developed — particularly around DNA sequence design, molecular machine learning, and biomedical informatics — directly seeded later projects including **ProMiR**, **HyperSNP**, **DNAChipBench**, and **Molecular ML**. The project also cultivated a generation of researchers fluent in both algorithmic thinking and wet-lab molecular biology, an unusual combination that shaped the lab's subsequent research directions.
