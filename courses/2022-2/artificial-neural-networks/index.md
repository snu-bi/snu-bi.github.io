---
title: Artificial Neural Networks — Fall 2022
---

# {% include icon.html icon="fa-solid fa-brain" %}4190.676 Artificial Neural Networks (Fall 2022)

*(Artificial Neural Networks, Computational Neuroscience, Computational Models of Intelligence)*

- **Instructor**: Prof. Byoung-Tak Zhang
- **Main TA**: Yoonsung Kim (yskim@bi.snu.ac.kr)
- **Sub TA**: Hyunseo Kim (hskim@bi.snu.ac.kr)
- **Classroom**: 302동 105호
- **Time**: Tue & Thu, 11:00–12:15
- **Semester**: 2022 Fall Graduate Course in Computer Science and Engineering

## {% include icon.html icon="fa-solid fa-bullseye" %}Course Objectives

We study "self-learning" networks, i.e. models that learn in an unsupervised and "self-supervised" way without the help of an explicit teacher. These models are neuro-biologically inspired and, usually, self-organizing, dynamic, recurrent, and auto-encoding networks. We examine the principles of neural learning algorithms from the historical models, such as Willshaw-von der Malsburg feature maps, Linsker models, Kohonen's self-organizing maps, Grossberg models, recurrent networks, Anderson's brain-state-in-a-box, actor-critic networks, Hopfield's associative memory, Boltzmann machines, and deep belief networks.

We study mathematical tools for approximation and optimization of the neural learning models. These include information-theoretic algorithms, such as maximum entropy, mutual information, and KL divergence as well as the statistical-mechanical methods, such as Markov chains, Metropolis algorithms, Gibbs sampling, and simulated annealing. We also examine the neurodynamic models of self-supervised, end-to-end learning to solve the challenging problems, such as time series prediction and reconstruction. These include Markov decision processes, approximate dynamic programming, reinforcement learning, sequential Bayesian estimation, Kalman filtering, particle filtering, real-time recurrent learning, dynamic reconstruction of a chaotic process.

## {% include icon.html icon="fa-solid fa-book" %}Textbooks

- Haykin, S. (2009). *Neural Networks and Learning Machines*, 3rd Ed., Pearson.
- 장병탁 (2017). *장교수의 딥러닝*, 홍릉출판사.

## {% include icon.html icon="fa-solid fa-chart-pie" %}Evaluation

| Component | Weight |
|-----------|--------|
| Two Exams (Midterm + Final) | 80% |
| Homework | 10% |
| Participation and Discussion | 10% |

## {% include icon.html icon="fa-solid fa-calendar-alt" %}Lecture Schedule

| Week | Dates | Topics | Slides |
|------|-------|--------|--------|
| Week 1 | 9/1 | **Learning in Neurodynamic Self-organizing Systems** — Neural Networks, Unsupervised / Self-supervised Learning; Mathematics for Neural Learning | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch0_Introduction.pdf) |
| Week 2 | 9/6, 9/8 | **Principal-Components Analysis (Ch. 8)** — Principal Component Analysis; Hebbian-Based Maximum Eigenfilter; **Hebbian-Based PCA (Ch. 8)** — Generalized Hebbian Algorithm; Kernel PCA | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch8_PCA.pdf) |
| Week 3 | 9/13, 9/15 | **Self-organizing Maps (Ch. 9)** — Willshaw-von der Malsburg Model; Kohonen's SOM Model | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch9_SOM.pdf) |
| Week 4 | 9/20, 9/22 | **Information-Theoretic Learning Models (Ch. 10)** — Maximum Entropy, Kullback-Leibler Divergence; Mutual Information (MI) | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch10_ITLM.pdf) |
| Week 5 | 9/27, 9/29 | **Information-Theoretic Learning Models (Ch. 10)** — Infomax, Imax, Imin; Independent Component Analysis (ICA); **Statistical-Mechanical Learning Methods (Ch. 11)** — Statistical Mechanics, Markov Chains; Metropolis, Gibbs Sampling, Simulated Annealing | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch11_SM.pdf) |
| Week 6 | 10/4, 10/6 | **Deep Neural Networks (Ch. 11)** — Boltzmann Machines; Deep Belief Networks | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch11_SM.pdf) |
| Week 7 | 10/11, 10/13 | **Assignment 1 Solving Class**; **Deep Neural Networks (Ch. 11)** — Boltzmann Machines; Deep Belief Networks | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch11_SM.pdf) |
| Week 8 | 10/18, 10/20 | Summary (10/18); ***Mid-term Exam (10/20)*** | — |
| Week 9 | 10/25, 10/27 | **No Lecture** | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch12_DP.pdf) |
| Week 10 | 11/1, 11/3 | **Dynamic Programming (Ch. 12)** — Markov Decision Process, DP, Bellman Equation; ADP, Reinforcement Learning, TD, Q | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch12_DP.pdf) |
| Week 11 | 11/8, 11/10 | **Neurodynamic Models (Ch. 13)** — Dynamic Systems, Attractors, Chaos; Hopfield Models, Dynamic Reconstruction | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch13_ND.pdf) |
| Week 12 | 11/15, 11/17 | **Bayesian Filtering (Ch. 14)** — State Space Models; Kalman Filters, EKF, CKF | [PDF](https://bi.snu.ac.kr/Courses/ann22f/slides/Ch14_BF.pdf) |
| Week 13 | 11/22, 11/24 | **Particle Filters (Ch. 14)** — Approximate Bayesian Filtering; Particle Filters, SIR Algorithm; **Dynamic Recurrent Networks (Ch. 15)** — Recurrent Network Architectures; Backpropagation through Time | — |
| Week 14 | 11/29, 12/1 | **Real-Time Recurrent Learning (Ch. 15)** — RTRL Algorithm, Vanishing Gradients; EKF Algorithm for Training RMLP | — |
| Week 15 | 12/6, 12/8 | ***Final Exam (12/8)*** | — |
| Week 16 | 12/13 | Review and Discussion | — |
