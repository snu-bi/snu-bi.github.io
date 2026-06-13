#!/usr/bin/env python3
"""Update stub pages: replace old legacy archive links with links to files now in courses/ dirs."""

import re
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")

# Map: (course_dir, old_legacy_dir_fragment) → list of (label, relative_path)
UPDATES = {
    "courses/2008-2/artificial-intelligence/index.md": (
        "4ai08f",
        [
            ("AI Chapter 13 slides", "AI_Chap13.ppt"),
            ("Action & Control (Ch.11)", "Ch11_Action_Control.pdf"),
            ("History of AI (Ch.1)", "Ch1_History_bw.pdf"),
            ("Learning & Memory (Ch.8)", "Ch8_Learning_Memory_bw.pdf"),
            ("Language (Ch.9)", "Ch9_Language.pdf"),
        ]
    ),
    "courses/2009-2/artificial-intelligence/index.md": (
        "4ai09f",
        [
            ("AI Chapter 3 slides", "AI_Chap3.ppt"),
            ("CNS Chapter 2", "CNS_Ch2.pdf"),
            ("History of AI", "Ch1_History.pdf"),
            ("Project 1 slides (zip)", "project1/Project1_AI_2009Fall_Slides.zip"),
            ("Project 1 dataset (zip)", "project1/project1_dataset.zip"),
            ("Project 2 data (zip)", "project2/AI09f_project2_tool_data.zip"),
        ]
    ),
    "courses/2010-1/artificial-intelligence/index.md": (
        "4ai10s",
        [
            ("AI Introduction slides", "AI_Introduction.pdf"),
        ]
    ),
    "courses/2010-2/artificial-intelligence/index.md": (
        "4ai10f",
        [
            ("Student presentation papers", "PresentationPaper.html"),
            ("Take-home exam", "ex2010f-bi-cns-Take-Home_Exam.pdf"),
            ("Bayesian Networks reference", "References/AI_Chap19_Bayesian_Networks.pdf"),
            ("CNS Ch.8 reference", "References/CNS_Ch8.pdf"),
        ]
    ),
    "courses/2011-2/artificial-intelligence/index.md": (
        "4ai11f",
        [
            ("Lecture 3 slides", "slides/Lecture3_0908.pdf"),
            ("SVM lecture", "slides/svm.pdf"),
        ]
    ),
    "courses/2012-1/artificial-intelligence/index.md": (
        "4ai12s",
        [
            ("Project 1: MLP", "Projects/AI_MLP.pdf"),
            ("Project 2 spec", "Projects/SpecProject2.pdf"),
            ("Reference: AI Ch.8", "References/ai12s_ch8.pdf"),
        ]
    ),
    "courses/2012-2/artificial-intelligence/index.md": (
        "4ai12f",
        [
            ("Question set 11", "Questions/Q11.pdf"),
            ("Reference Ch.6", "References/ch6.pdf"),
        ]
    ),
    "courses/2013-2/artificial-neural-networks/index.md": (
        "ann13",
        [
            ("Project 2: Lifelog behavior analysis", "Project2.html"),
        ]
    ),
    "courses/2013-2/machine-learning/index.md": (
        "ann13",
        None  # ann13 was ANN, not ML — remove the wrong link
    ),
    "courses/2014-1/artificial-intelligence/index.md": (
        "4ai14s",
        [
            ("Constraint propagation & planning", "cpt.pdf"),
            ("Lecture notes", "0401_19.pdf"),
        ]
    ),
    "courses/2015-2/artificial-neural-networks/index.md": (
        "ann15f",
        [
            ("Archived course page", "archive-ann15f.html"),
        ]
    ),
    "courses/2015-2/machine-learning/index.md": (
        "ML2015f",
        [
            ("Project poster", "projects/poster.pdf"),
            ("RBFN reference", "projects/RBFN.pdf"),
            ("Project 2 writeup", "projects/project_2.pdf"),
        ]
    ),
    "courses/2016-1/artificial-intelligence/index.md": (
        "4ai16s",
        [
            ("NLP slides (Ch.7)", "slides/NLP-ch7.pdf"),
        ]
    ),
    "courses/2019-2/artificial-neural-networks/index.md": (
        "ann19f",
        [
            ("Midterm reference (2017)", "suppl/midterm_2017.pdf"),
        ]
    ),
    "courses/2021-1/artificial-intelligence/index.md": (
        "4ai21s",
        [
            ("Lecture 2 slides", "slides/Lec2.pdf"),
            ("Lecture 11 slides", "slides/Lec11.pdf"),
            ("Lecture 22 slides", "slides/Lec22.pdf"),
        ]
    ),
    "courses/2022-1/artificial-intelligence/index.md": (
        "4ai22s",
        [
            ("Deep Learning lecture (Lec.16)", "slides/Lecture_16_Deep_Learning.pdf"),
        ]
    ),
    "courses/2010-2/artificial-neural-networks/index.md": (
        "4ai10f",
        None  # 4ai10f was AI course, not ANN — remove wrong link
    ),
    "courses/2011-2/artificial-neural-networks/index.md": (
        "4ai11f",
        None  # 4ai11f was AI course, not ANN — remove wrong link
    ),
    "courses/2010-1/brain-and-computation/index.md": (
        None,
        [
            ("Slides: Topic 4", "slide_4_new.ppt"),
            ("Slides: Topic 8", "slide_8_new.ppt"),
        ]
    ),
    "courses/2008-2/ai-and-cognitive-process/index.md": (
        None,
        [
            ("Seminar 2 slides", "seminar2.ppt/sblee.ppt"),
            ("Seminar 2 page", "seminar2.html"),
        ]
    ),
}

PATTERN = re.compile(
    r'\*Lecture slides and course materials for this semester are available in the \[legacy archive\]\([^)]+\)\.\*'
)

def make_materials_block(files, course_rel_path):
    """Build a ## Course Materials section with links."""
    lines = [
        "",
        "## {% include icon.html icon=\"fa-solid fa-folder-open\" %}Course Materials",
        ""
    ]
    for label, rel in files:
        url = f"/{course_rel_path}/{rel}"
        lines.append(f"- [{label}]({url})")
    return "\n".join(lines)

changed = []
for rel_path, (legacy_frag, files) in UPDATES.items():
    abs_path = os.path.join(ROOT, rel_path)
    if not os.path.exists(abs_path):
        print(f"MISSING: {rel_path}")
        continue

    with open(abs_path, encoding="utf-8") as f:
        content = f.read()

    # Determine the base URL path for this course
    course_url_base = os.path.dirname(rel_path).replace("\\", "/")

    if files is None:
        # Remove the wrong/stale legacy archive link entirely
        new_content = PATTERN.sub("", content).strip() + "\n"
    else:
        materials_block = make_materials_block(files, course_url_base)
        if PATTERN.search(content):
            new_content = PATTERN.sub(materials_block.strip(), content)
        else:
            # Legacy link already gone — append materials block at end
            new_content = content.rstrip() + "\n" + materials_block + "\n"

    if new_content != content:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"UPDATED: {rel_path}")
        changed.append(rel_path)
    else:
        print(f"NO CHANGE: {rel_path}")

print(f"\nUpdated {len(changed)} files.")
