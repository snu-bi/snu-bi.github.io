---
title: Self-learning Neural Algorithms — Fall 2017
---

# {% include icon.html icon="fa-solid fa-brain" %}4190.676 Self-learning Neural Algorithms (Fall 2017)

*(a.k.a. Artificial Neural Networks)*

**2017 Fall Graduate Course in Computer Science and Engineering and Brain Science**
- 컴퓨터공학부: Artificial Neural Networks
- 뇌과학협동과정: Computational Neuroscience

| | |
|---|---|
| **Instructor** | Prof. Byoung-Tak Zhang |
| **Main TA** | Jiseob Kim (jkim@bi.snu.ac.kr) |
| **Sub TA** | Je-Hwan Ryu (jhryu@bi.snu.ac.kr) |
| **Classroom** | 302-107 (originally 302-209) |
| **Time** | Tue & Thu, 14:00–15:15 |

## {% include icon.html icon="fa-solid fa-bullseye" %}Course Objectives

We study "self-learning" networks, i.e. models that learn in an unsupervised and "self-supervised" way without the help of an explicit teacher. These models are neuro-biologically inspired and, usually, self-organizing, dynamic, recurrent, and auto-encoding networks. We examine the principles of neural learning algorithms from the historical models, such as Willshaw-von der Malsburg feature maps, Linsker models, Kohonen's self-organizing maps, Grossberg models, recurrent networks, Anderson's brain-state-in-a-box, actor-critic networks, Hopfield's associative memory, Boltzmann machines, and deep belief networks.

We study mathematical tools for approximation and optimization of the neural learning models. These include information-theoretic algorithms, such as maximum entropy, mutual information, and KL divergence as well as the statistical-mechanical methods, such as Markov chains, Metropolis algorithms, Gibbs sampling, and simulated annealing. We also examine the neurodynamic models of self-supervised, end-to-end learning to solve the challenging problems, such as time series prediction and reconstruction. These include Markov decision processes, approximate dynamic programming, reinforcement learning, sequential Bayesian estimation, Kalman filtering, particle filtering, real-time recurrent learning, dynamic reconstruction of a chaotic process.

## {% include icon.html icon="fa-solid fa-book" %}Textbooks

- Haykin, S. (2009). *Neural Networks and Learning Machines*, 3rd Ed., Pearson.
- 장병탁 (2017). *딥러닝*, 홍릉출판사.

## {% include icon.html icon="fa-solid fa-chart-pie" %}Evaluation

| Component | Weight |
|---|---|
| Two exams (midterm + final) | 80% |
| Homework | 10% |
| Participation and discussion | 10% |

## {% include icon.html icon="fa-solid fa-calendar-alt" %}Lecture Schedule

| Week | Dates | Topics | Slides |
|---|---|---|---|
| Week 1 | 9/5, 9/7 | **Learning in Neurodynamic Self-organizing Systems** — Neural Networks, Unsupervised / Self-supervised Learning; Mathematics for Neural Learning; Principal-Components Analysis (Ch. 8): PCA, Hebbian-Based Maximum Eigenfilter, Hebbian-Based PCA, Generalized Hebbian Algorithm, Kernel PCA | [Ch8\_PCA](./slides/Ch8_PCA.pdf) |
| Week 2 | 9/12, 9/14 | **Self-organizing Maps (Ch. 9)** — Willshaw-von der Malsburg Model; Kohonen's SOM Model | [Ch9\_SOM](./slides/Ch9_SOM.pdf) |
| Week 3 | 9/19, 9/21 | **Information-Theoretic Learning Models (Ch. 10)** — Maximum Entropy, Kullback-Leibler Divergence; Mutual Information, Infomax, ICA | [Ch10\_ITLM](./slides/Ch10_ITLM.pdf) |
| Week 4 | 9/26, 9/28 | *No Class* — **Statistical-Mechanical Learning Methods (Ch. 11)**: Statistical Mechanics, Markov Chains; Metropolis, Gibbs Sampling, Simulated Annealing | [Ch11\_SM](./slides/Ch11_SM.pdf) |
| Week 5 | 10/3, 10/5 | *Korean Thanksgiving Holiday* | |
| Week 6 | 10/10, 10/12 | *Makeup Class (10/12 at 19:30)* — **Deep Neural Networks (Ch. 11)**: Boltzmann Machines; Deep Belief Networks | [Ch11\_SM](./slides/Ch11_SM.pdf) |
| Week 7 | 10/17, 10/19 | **Dynamic Programming (Ch. 12)** (10/17); Problem Solving Session by TA (10/19) | [Ch12\_DP](./slides/Ch12_DP.pdf) |
| Week 8 | 10/24, 10/26 | Summary (10/24); **Mid-term Exam (10/26)** | |
| Week 9 | 10/31, 11/2 | **Dynamic Programming (Ch. 12)** — Markov Decision Process, DP, Bellman Equation; ADP, Reinforcement Learning, TD, Q; (11/2) PACS-2017 conference (see announcements) | [Ch12\_DP](./slides/Ch12_DP.pdf) |
| Week 10 | 11/7, 11/9 | **Neurodynamic Models (Ch. 13)** — Dynamic Systems, Attractors, Chaos; Hopfield Models, Dynamic Reconstruction | [Ch13\_ND](./slides/Ch13_ND.pdf) |
| Week 11 | 11/14, 11/16 | *Classroom Change (Mogam Hall, Bldg 500 on 11/16)* — **Bayesian Filtering (Ch. 14)**: State Space Models; Kalman Filters, EKF, CKF | [Ch14\_BF](./slides/Ch14_BF.pdf) |
| Week 12 | 11/21, 11/23 | *Makeup Class (11/21 at 19:00)* — **Particle Filters (Ch. 14)**: Approximate Bayesian Filtering, Particle Filters, SIR Algorithm; **Dynamic Recurrent Networks (Ch. 15)**: Recurrent Network Architectures, Backpropagation through Time | [Ch14\_Suppl](./suppl/Ch14_Suppl.pdf) / [Ch15\_RN](./slides/Ch15_RN.pdf) |
| Week 13 | 11/28, 11/30 | **Real-Time Recurrent Learning (Ch. 15)** — RTRL Algorithm, Vanishing Gradients; EKF Algorithm for Training RMLP; **Final Exam (11/30)** | [Ch15\_RN](./slides/Ch15_RN.pdf) |
| Week 14 | 12/5, 12/7 | Review and discussion | |

## {% include icon.html icon="fa-solid fa-bullhorn" %}Announcements

- **(07/25)** Welcome to the class!
- **(09/13)** If you cannot attend class due to a conference, email both TAs at least one week in advance with documentation (e.g., registration invoice).
- **(09/13)** The schedule has been updated.
- **(09/19)** Mid-term Exam date fixed: **Oct. 26**.
- **(09/19)** No classes in Week 4 (09/26, 09/28). Makeup class on **Oct. 12 at 19:30** in the same classroom.
- **(09/28)** Newer version of Ch. 11 slides uploaded.
- **(10/09)** Homework #1 announced.
- **(10/09)** Problem Solving Session by TA on Oct. 19. Regular lecture on Oct. 17.
- **(10/17)** Late submissions of HW#1 accepted at the start of class on Oct. 19 (80% credit).
- **(10/17)** Mid-term Exam scope: up to Ch. 11.
- **(10/19)** Solution for HW#1 uploaded.
- **(10/27)** Class on Nov. 2 replaced by PACS-2017 conference. Students required to attend session **14:00–15:30 "The Neural Code at the Base of Perception, Action, and Cognition"** by Christoph von der Malsburg (no registration needed for this session; attendance check in the lobby of Engineering House).
- **(11/01)** Students may attend the whole PACS-2017 conference (Thu & Fri) without registration — tell the registration desk you are in Prof. Zhang's class.
- **(11/13)** Nov. 16 lecture moved to **Mogam Hall, Building #500**.
- **(11/14)** Final Exam fixed: **Nov. 30**. Makeup class on **Nov. 21 at 19:00** in the same classroom.
- **(11/22)** Homework #2 announced.
- **(11/28)** Solution for HW#2 uploaded.
- **(12/15)** Attendance, mid-term, and final exam scores uploaded. Score claims: TA office (Room 417, Building 138), Dec. 18 (Mon) and Dec. 19 (Tue), 1PM–4PM.
