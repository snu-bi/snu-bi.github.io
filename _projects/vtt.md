---
title: Video Turing Test (VTT)
subtitle: Toward Human-Level Video Story Understanding
group: completed
period: "2017~2021"
image: images/dramaqa.png
external_link: "https://videoturingtest.github.io/"
funding: "IITP, grant No. 2017-0-01772-VTT, funded by Korea MSIT"
tags:
  - computer-vision
  - nlp
  - multimodal
  - video-understanding
  - question-answering
  - ai-evaluation
  - scene-graph
  - character-identification
---

The Video Turing Test (VTT) project pursued a grand challenge: building AI systems capable of **human-level comprehension of video narratives**. Inspired by the Turing Test concept applied to video story understanding, the project proposed a blind evaluation framework in which an AI agent's video comprehension ability is assessed by its indistinguishability from that of a human viewer. TV drama and movie content served as the primary testbed, demanding that machines extract events, analyse causal relationships, resolve characters across scenes, and engage in open-ended dialogue about video content.

## Overview

Story comprehension is widely regarded as a robust proxy for measuring intelligence. Understanding a video story requires integrating visual perception, natural language processing, and multimodal reasoning over long temporal spans — tasks that remain far beyond the reach of standard video recognition systems.

The VTT project addressed this challenge by developing:

- A **blind evaluation methodology** (the Video Turing Test framework) to measure AI human-likeness in video comprehension
- Large-scale **multimodal benchmarks** combining video clips, subtitles, scene descriptions, and rich character annotations
- Deep learning architectures for **hierarchical story understanding**, including character re-identification, causal reasoning, and open-ended question answering
- Scene graph-based and hypergraph-based methods for **structured multimodal representation**

The flagship benchmark produced by the project is **DramaQA**, a character-centered video question-answering dataset built from the Korean TV drama *Another Miss Oh*. DramaQA provides 17,983 QA pairs across 23,928 video clips at four hierarchical difficulty levels aligned to human cognitive developmental stages, together with 217,308 annotated images containing character bounding boxes, behaviors, emotions, and coreference-resolved scripts.

A culminating system called **VINCENT** (Video INtelligence CENter Toolkit) was proposed to operationalise the VTT evaluation, demonstrating end-to-end multimodal video comprehension and dialogue.

## Research Team

**Principal Investigator**
- Byoung-Tak Zhang (Seoul National University, SNU Biointelligence Lab)

**Researchers**
- Seongho Choi
- Kyoung-Woon On
- Yu-Jung Heo
- Ahjeong Seo
- Youwon Jang
- Minsu Lee
- Wooseok Choi
- Woo Suk Choi
- Minjung Shin
- Minjoon Jung
- Donggeon Lee
- Eun-Sol Kim
- Björn Bebensee

**Affiliation:** Video Intelligence Center @ Seoul National University (SNU AIIS)

## Technical Approach

The VTT project tackled video story understanding across several complementary research thrusts:

**Benchmark Construction and Evaluation**
- Hierarchical QA difficulty levels (L1–L4) grounded in cognitive development theory
- Character-centered annotation: bounding boxes, behavior labels, emotion tags, coreference-resolved dialogue
- The VTT blind test protocol for comparing AI and human video comprehension

**Multimodal Representation Learning**
- Hypergraph Attention Networks (HAN) for joint modeling of visual, audio, and textual modalities
- Cut-based graph learning networks to discover compositional structure in sequential video
- Co-attentional Transformers for cross-modal story-level reasoning

**Character Understanding and Re-identification**
- Character grounding across video clips using visual and linguistic cues
- Scene-level and narrative-level character state tracking

**Scene Graph and Structured Reasoning**
- Scene graph parsing methods (SGRAM, AMR-based) for extracting structured event representations
- Hypergraph Transformer for weakly-supervised multi-hop reasoning in knowledge-based VQA
- Causal and temporal inference over long-form narrative content

**Open-ended Video Question Answering**
- Multi-level Context Matching model for hierarchical answer selection
- Motion-appearance synergistic networks for video QA (MASN)
- Transformer-based video metadata integration for open-ended QA

## Workshop and Community Building

The project organised the **VTT Workshop at ICCV 2019** (November 2, 2019, Seoul), a half-day workshop that brought together leading researchers in video understanding from institutions including UC Berkeley, University of British Columbia, and University of Amsterdam. Nine papers were presented, spanning video stabilisation, character identification in dramatic content, and novel video understanding benchmarks.

The DramaQA challenge was also hosted at **ECCV 2020**, further establishing the benchmark as a standard for the community.

## Publications

- Minsu Lee, Yu-Jung Heo, Seongho Choi, Wooseok Choi, Byoung-Tak Zhang. **"Video Turing Test: A First Step Towards Human-Level AI."** *AI Magazine* 44(4), 2023. <https://doi.org/10.1002/aaai.12128>
- Seongho Choi, Kyoung-Woon On, Yu-Jung Heo, Ahjeong Seo, Youwon Jang, Minsu Lee, Byoung-Tak Zhang. **"DramaQA: Character-Centered Video Story Understanding with Hierarchical QA."** *AAAI 2021*. <https://arxiv.org/abs/2005.03356>
- Yu-Jung Heo, Minsu Lee, Seongho Choi, Woo Suk Choi, Minjung Shin, Minjoon Jung, Jeh-Kwang Ryu, Byoung-Tak Zhang. **"Toward a Human-Level Video Understanding Intelligence."** *AAAI FSS 2021*. <https://arxiv.org/abs/2110.04203>
- Ahjeong Seo, Gi-Cheon Kang, Joonhan Park, Byoung-Tak Zhang. **"Attend What You Need: Motion-Appearance Synergistic Networks for Video Question Answering."** *ACL 2021*. <https://aclanthology.org/2021.acl-long.481/>
- Björn Bebensee, Byoung-Tak Zhang. **"Co-Attentional Transformers for Story-Based Video Understanding."** *ICASSP 2021*. <https://arxiv.org/abs/2010.14104>
- Donggeon Lee, Seongho Choi, Youwon Jang, Byoung-Tak Zhang. **"Mounting Video Metadata on Transformer-based Language Model for Open-ended Video Question Answering."** *Preprint*, 2021. <https://arxiv.org/abs/2108.05158>
- Yu-Jung Heo, Eunsol Kim, Wooseok Choi, Byoung-Tak Zhang. **"Hypergraph Transformer: Weakly-Supervised Multi-hop Reasoning for Knowledge-Based Visual Question Answering."** *ACL 2022*. <https://aclanthology.org/2022.acl-long.29/>
- Wooseok Choi, Yu-Jung Heo, Dharani Perumal, Byoung-Tak Zhang. **"Scene Graph Parsing via Abstract Meaning Representation in Pre-trained Language Models."** *NAACL 2022 DLG4NLP Workshop*. <https://arxiv.org/abs/2208.04832>
- Woo Suk Choi, Yu-Jung Heo, Byoung-Tak Zhang. **"SGRAM: Improving Scene Graph Parsing via Abstract Meaning Representation."** *Preprint*, 2022. <https://arxiv.org/abs/2210.08675>
- Kyoung-Woon On, Eun-Sol Kim, Yu-Jung Heo, Byoung-Tak Zhang. **"Cut-Based Graph Learning Networks to Discover Compositional Structure of Sequential Video Data."** *AAAI 2020*. <https://doi.org/10.1609/aaai.v34i04.5978>
- Eun-Sol Kim, Woo-Young Kang, Kyoung-Woon On, Yu-Jung Heo, Byoung-Tak Zhang. **"Hypergraph Attention Networks for Multimodal Learning."** *CVPR 2020*. <https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Hypergraph_Attention_Networks_for_Multimodal_Learning_CVPR_2020_paper.html>
- Minjung Shin, Seongho Choi, Yu-Jung Heo, Minsu Lee, Byoung-Tak Zhang, Jeh-Kwang Ryu. **"CogME: A Cognition-Inspired Multi-Dimensional Evaluation Metric for Story Understanding."** *CogSci 2024*. <https://escholarship.org/uc/item/8p3137gd>

## Funding

This project was funded by the **Institute for Information & Communications Technology Promotion (IITP)**, grant No. **2017-0-01772-VTT**, under the Korean Ministry of Science and ICT (MSIT). Additional related support was provided under IITP grants 2015-0-00310 (SW StarLab), 2018-0-00622 (RMI), and 2019-0-01367 (BabyMind).
