---
title: FACT
subtitle: Text Filtering and Classification from Large-Scale Document Collections
group: completed
period: "1998~2001"
image: images/photo.jpg
funding: "Korea Research Foundation (KRF)"
tags:
  - natural-language-processing
  - information-retrieval
  - text-classification
  - machine-learning
  - information-filtering
  - boosting
  - text-mining
---

The FACT project investigated **machine learning methods for automatically filtering and classifying text** from large-scale document collections — foundational work in what we now call information retrieval and natural language processing. The lab built and evaluated its own text retrieval and filtering engine, SCAIR (SNU Cognitive AI Research), which was submitted to multiple tracks of the internationally competitive **Text REtrieval Conference (TREC)**.

## Overview

As the web exploded with text content in the late 1990s, the ability to automatically identify and surface relevant documents from massive collections became a critical challenge. The FACT project addressed this by developing principled probabilistic and ensemble learning methods for two related problems: **adaptive text filtering** (continuously deciding whether incoming documents are relevant to a user profile) and **text classification** (assigning documents to predefined categories).

A central contribution was the application of **boosting** — particularly AdaBoost with Naïve Bayes classifiers as weak learners — to the text filtering problem. This approach leveraged term frequency statistics with probabilistically accurate confidence ratios, yielding strong empirical performance on the TREC filtering track benchmarks. The project also explored boosting linear perceptrons, reinforcement learning for personalized filtering, and semi-supervised methods that exploited large quantities of unlabeled documents.

Results were validated through repeated participation in TREC (TREC-7 through TREC-9), covering the **ad hoc retrieval**, **adaptive filtering**, and **question answering** tracks. TREC is a major annual evaluation campaign organized by NIST that enables large-scale, standardized comparison of information retrieval systems across participating research groups worldwide.

## Research Team

- **Principal Investigator:** Prof. Byoung-Tak Zhang
- **Researchers:**
  - Dong-Hyun Shin — ad hoc retrieval, two-stage retrieval model (TREC-7, TREC-8)
  - Young-Hoon Kim — text filtering, TREC-8, TREC-9, SIGIR-2000
  - Sungwon Kim — TREC-8, TREC-9 web track experiments
  - Jong-Hyeok Eom — TREC-8, TREC-9 experiments
  - Ho-Jin Shin — TREC-8 classification experiments
  - Sung-Yong Hahn — text filtering by boosting (SIGIR-2000)
  - Sang-Bum Park — document filtering with unlabeled data
  - Jang-Min Oh — text filtering by boosting linear perceptrons

## Technical Approach

- **Boosting-based filtering:** AdaBoost combining Naïve Bayes weak classifiers, exploiting term confidence ratios for reliable relevance scoring
- **Boosting linear perceptrons:** An alternative boosting framework applied to adaptive filtering with linear models
- **Semi-supervised filtering:** Leveraging large pools of unlabeled documents to improve adaptive filtering under limited labeled training data
- **Two-stage ad hoc retrieval:** A two-pass retrieval model tuned for TREC ad hoc tasks, separating initial candidate retrieval from re-ranking
- **SCAIR engine:** The lab's custom retrieval and filtering system used for all TREC submissions, covering ad hoc retrieval, adaptive filtering, web search, and question answering tracks

## Publications

- **Text Filtering by Boosting Naive Bayes Classifiers**, Kim, Y.-H., Hahn, S.-Y., and Zhang, B.-T., *Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR-2000)*, pp. 168–175, 2000. [[Full Paper]](http://bi.snu.ac.kr/Publications/Conferences/International/SIGIR2000.pdf)
- **SCAI Experiments on TREC-9**, Kim, Y.-H., Kim, S., Eom, J.-H., and Zhang, B.-T., *Proceedings of the Ninth Text REtrieval Conference (TREC-9)*, pp. 392–399, 2000. [[Full Paper]](http://bi.snu.ac.kr/Publications/Conferences/International/TREC9.ps)
- **Document Filtering Boosted by Unlabeled Data**, Park, S.-B. and Zhang, B.-T., *Proceedings of the 2001 IEEE International Symposium on Industrial Electronics (ISIE2001)*, vol. 1, pp. 328–333, 2001. [[Full Paper]](http://bi.snu.ac.kr/Publications/Conferences/International/ISIE2001.pdf)
- **SCAI TREC-8 Experiments**, Shin, D.-H., Kim, Y.-H., Kim, S., Eom, J.-H., Shin, H.-J., and Zhang, B.-T., *Proceedings of the Eighth Text REtrieval Conference (TREC-8)*, pp. 511–518, 1999. [[Full Paper]](http://bi.snu.ac.kr/Publications/Conferences/International/TREC8.ps)
- **A Two-Stage Retrieval Model for the TREC-7 Ad Hoc Task**, Shin, D.-H. and Zhang, B.-T., *Proceedings of the Seventh Text REtrieval Conference (TREC-7)*, pp. 501–507, 1998.
- **Text Filtering by Boosting Linear Perceptrons**, Oh, J.-M. and Zhang, B.-T., *Journal of Fuzzy Logic and Intelligent Systems*, vol. 10, no. 6, pp. 373–378, 2000.
- **Building Software Agents for Information Filtering on the Internet: A Genetic Programming Approach**, Zhang, B.-T., Kwak, J.-H., and Lee, C.-H., *Late Breaking Papers at the Genetic Programming 1996 Conference (GP-96)*, p. 196, 1996.

## Historical Context

FACT was conducted at a pivotal moment when the web was growing faster than human curation could manage. The lab's sustained participation across TREC-7, TREC-8, and TREC-9 (1998–2000) placed it alongside leading international information retrieval groups, and the boosting-based filtering methods produced results that influenced the broader community's adoption of ensemble methods for text tasks. This work laid the groundwork for the lab's later research in text mining, bioinformatics text analysis, and multimodal learning.
