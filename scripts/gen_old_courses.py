#!/usr/bin/env python3
"""Generate Jekyll course pages for old courses (1997-2006) and migrate their files."""

import os, shutil, subprocess

ROOT = os.path.join(os.path.dirname(__file__), "..")
LEGACY = os.path.join(ROOT, "legacy/raw/bi.snu.ac.kr/Courses")

PAGES = {}

# ───────────────────── 1997 ─────────────────────

PAGES["courses/1997-1/introduction-to-computers/index.md"] = """\
---
title: Introduction to Computers — Spring 1997
---

# {% include icon.html icon="fa-solid fa-computer" %}419.017 Introduction to Computers (Spring 1997)

*Department of Computer Engineering, Seoul National University*

- **Instructor**: Prof. Byoung-Tak Zhang
- **Classroom**: 301-203
- **Time**: Mon 1–3 pm, Thu 11 am–noon

## {% include icon.html icon="fa-solid fa-calendar-alt" %}Course Schedule

| Week | Topic |
|------|-------|
| 1 | Overview of a Computer System |
| 2 | The Central Processing Unit |
| 3 | Input and Output Devices |
| 4 | Storage Devices |
| 5 | Computer Communications |
| 6 | Programming and Languages |
| 7 | **Midterm Exam** |
| 8 | Operating Systems |
| 9 | Software Engineering |
| 10 | Management Information Systems |
| 11 | Computer Crime and Security |
| 12 | Artificial Intelligence |
| 13 | Computers in Business |
| 14 | Database Systems |
| 15 | **Final Exam** |
"""

PAGES["courses/1997-1/data-structures/index.md"] = """\
---
title: Data Structures — Spring 1997
---

# {% include icon.html icon="fa-solid fa-sitemap" %}419.206 Data Structures (Spring 1997)

*Department of Computer Engineering, Seoul National University*

- **Instructor**: Prof. Byoung-Tak Zhang
- **Classroom**: 301-203
- **Time**: Mon / Wed / Fri 9–10 am

## {% include icon.html icon="fa-solid fa-book" %}Textbook

- **Fundamentals of Data Structures in C++** — E. Horowitz, S. Sahni & D. Mehta — Freeman and Company — 1995

## {% include icon.html icon="fa-solid fa-calendar-alt" %}Course Schedule

| Week | Topic |
|------|-------|
| 1 | Introduction |
| 2 | Analysis of Algorithms |
| 3 | Arrays, Polynomials |
| 4 | Sparse Matrices, Strings |
| 5 | Stacks and Queues |
| 6 | Evaluation of Expressions |
| 7 | Multiple Stacks and Queues |
| 8 | **Midterm Exam** |
| 9 | Singly Linked Lists, Circular Lists |
| 10 | Doubly Linked Lists, Generalized Lists |
| 11 | Binary Trees, Tree Traversal |
| 12 | Threaded Binary Trees, Heaps |
| 13 | Selection Trees, Forests |
| 14 | Graphs, Minimum Spanning Trees |
| 15 | Shortest Paths, Activity Networks |
| 16 | **Final Exam** |
"""

# ───────────────────── 1998 ─────────────────────

PAGES["courses/1998-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — 1998
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence (1998)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Breast cancer dataset](breast.dat)
"""

PAGES["courses/1998-1/unix-and-internet/index.md"] = """\
---
title: Unix and Internet — 1998
---

# {% include icon.html icon="fa-solid fa-terminal" %}Unix and Internet (1998)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 3 slides](chap3.ppt)
- [Chapter 8 slides](chap8.ppt)
"""

# ───────────────────── 1999 ─────────────────────

PAGES["courses/1999-1/statistical-learning-theory/index.md"] = """\
---
title: Statistical Learning Theory — Spring 1999
---

# {% include icon.html icon="fa-solid fa-chart-line" %}Statistical Learning Theory: Data Mining Workshop (Spring 1999)

*SCAI (School of Computer Science and Artificial Intelligence), Seoul National University*

- **Instructor**: Prof. Byoung-Tak Zhang
- **Semester**: Spring 1999

## {% include icon.html icon="fa-solid fa-book" %}Textbook

- **Data Mining with Neural Networks** — Joseph P. Bigus — 1996

## {% include icon.html icon="fa-solid fa-calendar-alt" %}Workshop Schedule

Student presentation seminar covering chapters of Bigus (1996):

| Chapter | Topic |
|---------|-------|
| 1 | Introduction to Data Mining |
| 2 | Introduction to Neural Networks |
| 3 | Data Preparation |
| 4 | Neural Network Models and Architectures |
| 5 | Training and Testing Neural Networks |
| 6 | Supervised and Unsupervised Learning |
| 7 | Prediction and Forecasting |
| 8 | Neural Network Classification |
| 9 | Natural Language Processing |
| 10 | Advanced Topics |

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Seminar page (archived)](seminar.html)
"""

PAGES["courses/1999-2/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — Fall 1999
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence: Softbot Soccer (Fall 1999)

- **Instructor**: Prof. Byoung-Tak Zhang
- **Semester**: Fall 1999 (1999년 2학기)

## {% include icon.html icon="fa-solid fa-flask" %}Project

**Softbot Soccer Games** — Students implemented GP-based agents (clients) that play simulated soccer against each other on a server using a RoboCup-style framework.

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Server & project info (archived)](server-comments.html)
- [Project slides (T6)](project/T6.ppt)
"""

PAGES["courses/1999-1/data-structures/index.md"] = """\
---
title: Data Structures — 1999
---

# {% include icon.html icon="fa-solid fa-sitemap" %}419.206 Data Structures (1999)

- **Instructor**: Prof. Byoung-Tak Zhang
"""

# ───────────────────── 2000 ─────────────────────

PAGES["courses/2000-1/introduction-to-computers/index.md"] = """\
---
title: Introduction to Computers — 2000
---

# {% include icon.html icon="fa-solid fa-computer" %}Introduction to Computers (2000)

- **Instructor**: Prof. Byoung-Tak Zhang

*Student homepage project course hosted at comphw.snu.ac.kr.*
"""

PAGES["courses/2000-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — 2000
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence (2000)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 9 slides](chap9.pdf)
"""

# ───────────────────── 2001 ─────────────────────

PAGES["courses/2001-1/introduction-to-computers/index.md"] = """\
---
title: Introduction to Computers — 2001
---

# {% include icon.html icon="fa-solid fa-computer" %}Introduction to Computers (2001)

- **Instructor**: Prof. Byoung-Tak Zhang
"""

PAGES["courses/2001-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — 2001
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence (2001)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 3 slides](Chap3.ppt)
- [Chapter 8 slides](Chap8.ppt)
- [Chapter 22 slides](Chap22.ppt)
- [Chapter 23 slides](Chap23.ppt)
- [Bayesian Network Learning software](bnsoftware.msi)
"""

# ───────────────────── 2002 ─────────────────────

PAGES["courses/2002-1/introduction-to-computers/index.md"] = """\
---
title: Introduction to Computers — 2002
---

# {% include icon.html icon="fa-solid fa-computer" %}Introduction to Computers (2002)

- **Instructor**: Prof. Byoung-Tak Zhang

*C programming exercises (ytkimC).*
"""

PAGES["courses/2002-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — 2002
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence (2002)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-flask" %}Projects

**Project 2**: Function Optimization with Genetic Algorithms — students implemented GAs to maximize/minimize benchmark functions (Rastrigin, Ackley, Schwefel) and solved TSP instances.

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 3 slides](Chap3.ppt)
- [Intelligent Agents slides](IntAgent.ppt)
- [Biodiversity Decision Trees](BioDT.ppt)
- [Project 2 page (archived)](project2.html)
- [TSP instance 43-city](43.tsp)
- [TSP instance 48-city](48.tsp)
- [TSP instance 100-city](100.tsp)
"""

PAGES["courses/2002-1/bioinformatics/index.md"] = """\
---
title: Bioinformatics — 2002
---

# {% include icon.html icon="fa-solid fa-dna" %}Bioinformatics (2002)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 1](bio02_chapter1_bw.pdf)
- [Chapter 3](bio02_chapter3_2.pdf)
- [Chapter 5 slides](bio02_chapter5.ppt)
- [Sequence Analysis](bio02_seqanalysis.pdf)
- [Bioinformatics Ch.6 (part 1)](bioinfor-chap6-1.pdf)
- [Bioinformatics Ch.6 (full)](bioinfor-chap6-full.pdf)
- [Project writeup](project.pdf)
"""

# ───────────────────── 2004 ─────────────────────

PAGES["courses/2004-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — 2004
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence (2004)

- **Instructor**: Prof. Byoung-Tak Zhang

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 8 slides](Chap8.ppt)
- [Chapter 13 slides](Chap13.ppt)
- [Chapter 17-1 slides](Chap17-1.ppt)
- [Challenge dataset (zip)](challenge.zip)
"""

PAGES["courses/2004-2/biotechnology-and-computing/index.md"] = """\
---
title: Biotechnology and Computing — Fall 2004
---

# {% include icon.html icon="fa-solid fa-flask" %}4190.419 Biotechnology and Computing (Fall 2004)

- **Instructor**: Prof. Byoung-Tak Zhang / Danny van Noort
- **Semester**: Fall 2004

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Neural networks reference](nn.ppt)
- [CIMTEC 1998 reference paper](CIMTEC98.pdf)
"""

# ───────────────────── 2005 ─────────────────────

PAGES["courses/2005-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — Spring 2005
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence: Biointelligence (Spring 2005)

- **Instructor**: Prof. Byoung-Tak Zhang
- **Semester**: Spring 2005 (2005년 1학기)

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

**Lecture slides:**

- [Chapter 2](Chap2.ppt) · [Chapter 4](Chap4.ppt) · [Chapter 7](Chap7.ppt) · [Chapter 8](Chap8.ppt)
- [Chapter 13](Chap13.ppt) · [Chapter 14](Chap14.ppt) · [Chapter 16](Chap16.ppt)
- [Chapter 17-1](Chap17-1.ppt) · [Chapter 17-2](Chap17-2.ppt) · [Chapter 19](Chap19.ppt)
- [Chapter 20](Chap20.ppt) · [Chapter 22](Chap22.ppt) · [Chapter 23](Chap23.ppt)
- [Chapter 24](Chap24.ppt) · [Chapter 25](Chap25.ppt)

**Project 1:**

- [Project 1 page](Proj1/project1.html) · [T6 slides](Proj1/T6.ppt)
- [Standard 3 dataset](Proj1/standard3.txt) · [Chapter 15-1 ref](Proj1/15_1.pdf) · [Chapter 19-1 ref](Proj1/19_1.pdf)

**Essays:**

- [Essay list](Essay/list.html) · [Essay 1-03](Essay/1-03.pdf) · [Essay 1-12](Essay/1-12.pdf)
- [Essay 1-23](Essay/1-23.pdf) · [Essay 1-30](Essay/1-30.pdf) · [Essay 2-02](Essay/2-02.pdf) · [Essay 3-02](Essay/3-02.pdf)
"""

PAGES["courses/2005-2/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — Fall 2005
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence: Biointelligence (Fall 2005)

- **Instructor**: Prof. Byoung-Tak Zhang
- **Semester**: Fall 2005

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 15 slides](Chap15.ppt)
- [Chapter 24 slides](Chap24.ppt)
"""

PAGES["courses/2005-2/biotechnology-and-computing/index.md"] = """\
---
title: Biotechnology and Computing — Fall 2005
---

# {% include icon.html icon="fa-solid fa-flask" %}4190.419 Biotechnology and Computing (Fall 2005)

*School of Computer Science and Engineering, Seoul National University*

- **Instructor**: Danny van Noort
- **TA**: Ho-Sik Seok (Tel: 872-5127)
- **Classroom**: 301-101
- **Time**: Mon / Wed / Fri 10:00–11:00

## {% include icon.html icon="fa-solid fa-bullseye" %}Course Objectives

- Getting insights in the role computers can play in biology
- Giving an introduction to the upcoming fields in engineering and biology

## {% include icon.html icon="fa-solid fa-book" %}Textbook

- **New Biology: For Engineers and Computer Scientists** — Pearson Education, Inc. — 2004

## {% include icon.html icon="fa-solid fa-chart-pie" %}Grading Policy

| 구분 | 비율 |
|------|------|
| Examination | 40% |
| Two essays | 30% |
| Presentation (in English) | 20% |
| Participation | 10% |

## {% include icon.html icon="fa-solid fa-calendar-alt" %}Course Schedule

| # | Topic | Reference |
|---|-------|-----------|
| 1 | Introduction | |
| 2 | Molecular biology | New Biology Ch. 2–3 |
| 3 | Biotechnology | New Biology Ch. 5 |
| 4 | Bio-MEMS | Papers 1–2 |
| 5 | Bio-informatics | New Biology Ch. 9 |
| 6 | Bio-modeling | |
| 7 | Cells and E-cells | New Biology Ch. 4, 7 |
| 8 | Transcription and regulation | New Biology Ch. 6 |
| 9 | Cell communication | |
| 10 | Neural networks | |
| 11 | DNA computing | Papers 3–4 |
| 12 | Fractals and patterns / Birds, bees and ants | |
"""

# ───────────────────── 2006 ─────────────────────

PAGES["courses/2006-1/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — Spring 2006
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence: Biointelligence (Spring 2006)

- **Instructor**: Prof. Byoung-Tak Zhang
- **Semester**: Spring 2006

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Chapter 3 slides](Chap3_g.pdf)
- [Chapter 5 slides](Chap5.ppt)
- [PYJ presentation slides](15_PYJ.ppt)
"""

PAGES["courses/2006-2/artificial-intelligence/index.md"] = """\
---
title: Artificial Intelligence — Fall 2006
---

# {% include icon.html icon="fa-solid fa-robot" %}4190.408 Artificial Intelligence: Biointelligence (Fall 2006)

- **Instructor**: Prof. Byoung-Tak Zhang
- **Semester**: Fall 2006 (2006년 2학기)

## {% include icon.html icon="fa-solid fa-flask" %}Project 1

**Text Classification by Neural Networks** — students trained MLP classifiers on the CLASSIC3 dataset (MED/CISI/CRAN, 3,830 examples, 100 features) and analysed the effect of epochs and hidden nodes on generalisation.

## {% include icon.html icon="fa-solid fa-folder-open" %}Course Materials

- [Project 1 page (archived)](project1.html)
- [Chapter 1: History of AI](Ch1_History_bw.pdf)
- [Chapter 6: Higher Perception](Ch6_Higher_Perception.pdf)
- [Chapter 1 slides](Chap1.ppt)
- [Chapter 17-1 slides](Chap17-1.ppt)
- [Chapter 19 slides](Chap19.ppt)
- [Introduction to Bayesian Networks](introBN.pdf)
- [NCC 2005 reference](NCC2005.pdf)
"""

# ──────────────────────────────────────────────────────────────
# MOVE FILES: (legacy_dir, jekyll_dir, skip_html)
# ──────────────────────────────────────────────────────────────

MOVES = [
    ("1ce97",        "courses/1997-1/introduction-to-computers",   True),
    ("2ds97",        "courses/1997-1/data-structures",             True),
    ("4ai98",        "courses/1998-1/artificial-intelligence",     False),
    ("2unix98",      "courses/1998-1/unix-and-internet",           False),
    ("g-slt99",      "courses/1999-1/statistical-learning-theory", True),
    ("2ds99",        "courses/1999-1/data-structures",             True),
    ("4ai99",        "courses/1999-2/artificial-intelligence",     True),
    ("1ce00",        "courses/2000-1/introduction-to-computers",   True),
    ("4ai00",        "courses/2000-1/artificial-intelligence",     False),
    ("1ce01",        "courses/2001-1/introduction-to-computers",   True),
    ("4ai01",        "courses/2001-1/artificial-intelligence",     False),
    ("1ce02",        "courses/2002-1/introduction-to-computers",   False),
    ("4ai02",        "courses/2002-1/artificial-intelligence",     True),
    ("bio02",        "courses/2002-1/bioinformatics",              False),
    ("4ai04",        "courses/2004-1/artificial-intelligence",     False),
    ("4Biotech04_2", "courses/2004-2/biotechnology-and-computing", False),
    ("4ai05s",       "courses/2005-1/artificial-intelligence",     False),
    ("4ai05f",       "courses/2005-2/artificial-intelligence",     False),
    ("5Biotech05_2", "courses/2005-2/biotechnology-and-computing", True),
    ("4ai06s",       "courses/2006-1/artificial-intelligence",     False),
    ("4ai06f",       "courses/2006-2/artificial-intelligence",     True),
]


def move_dir_contents(src, dst, skip_html):
    os.makedirs(os.path.join(ROOT, dst), exist_ok=True)
    for item in os.listdir(os.path.join(ROOT, src)):
        src_path = os.path.join(ROOT, src, item)
        dst_path = os.path.join(ROOT, dst, item)
        ext = item.rsplit(".", 1)[-1].lower() if "." in item else ""
        if skip_html and ext in ("html", "htm"):
            print(f"  skip HTML: {item}")
            continue
        if os.path.isdir(src_path):
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)


if __name__ == "__main__":
    # 1. Write Jekyll pages
    print("=== Writing Jekyll pages ===")
    for rel_path, content in PAGES.items():
        abs_path = os.path.join(ROOT, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  WROTE: {rel_path}")

    # 2. Move files from legacy to courses
    print("\n=== Moving files ===")
    for src_dir, dst_dir, skip_html in MOVES:
        src = os.path.join(LEGACY, src_dir)
        if not os.path.isdir(src):
            print(f"  SKIP (no dir): {src_dir}")
            continue
        print(f"  {src_dir} → {dst_dir}")
        move_dir_contents(src, dst_dir, skip_html)

    # 3. git rm the legacy dirs
    print("\n=== git rm legacy dirs ===")
    for src_dir, _, _ in MOVES:
        src = os.path.join(LEGACY, src_dir)
        if os.path.isdir(src):
            rel = os.path.relpath(src, ROOT).replace("\\", "/")
            result = subprocess.run(
                ["git", "rm", "-r", rel],
                capture_output=True, text=True, cwd=ROOT
            )
            print(result.stdout.strip() or f"  rm {rel}: {result.returncode}")

    # 4. git add new files
    print("\n=== git add ===")
    result = subprocess.run(
        ["git", "add", "-A"],
        capture_output=True, text=True, cwd=ROOT
    )
    print(result.stdout or "(staged)")

    print("\nDone.")
