---
title: Research
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}Research

Our research focuses on “biointelligence” i.e. the study of artificial intelligence on the basis of biological and bio-inspired information technologies, and its application to real world problems.

{% include search-box.html %}

{% include search-info.html %}

<!-- Group publications by type and year -->
{% assign preprints = site.data.publications | where: "publisher", "preprint" | sort: "year" | reverse %}
{% assign publications = site.data.publications | where_exp: "item", "item.publisher != 'preprint'" %}
{% assign publications_by_year = publications | group_by: "year" | sort: "name" | reverse %}
{% assign all_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}
{% assign latest_year = all_by_year | first %}
{% assign publication_count = site.data.publications | size %}
{% assign accepted_count = publications | size %}
{% assign preprint_count = preprints | size %}

<div class="publication-overview" aria-label="Publication overview">
  <div class="publication-stat">
    <span class="publication-stat-value">{{ publication_count }}</span>
    <span class="publication-stat-label">total works</span>
  </div>
  <div class="publication-stat">
    <span class="publication-stat-value">{{ accepted_count }}</span>
    <span class="publication-stat-label">published or accepted</span>
  </div>
  <div class="publication-stat">
    <span class="publication-stat-value">{{ preprint_count }}</span>
    <span class="publication-stat-label">preprints</span>
  </div>
  <div class="publication-stat">
    <span class="publication-stat-value">{{ latest_year.items.size }}</span>
    <span class="publication-stat-label">{{ latest_year.name }} works</span>
  </div>
  <div class="publication-year-links" aria-label="Jump to publication year">
    {% for year_group in all_by_year limit: 6 %}
      <a class="publication-year-link" href="#year-{{ year_group.name }}">
        <span>{{ year_group.name }}</span>
        <strong>{{ year_group.items.size }}</strong>
      </a>
    {% endfor %}
  </div>
</div>

<!-- Display preprints first -->
{% if preprints.size > 0 %}
  <h3 class="year-heading" id="preprints">Preprint</h3>
  
  {% for publication in preprints %}
    {% include citation.html lookup=publication.id style="rich" %}
  {% endfor %}
{% endif %}

<!-- Display publications by year -->
{% for year_group in publications_by_year %}
  {% assign year = year_group.name %}
  {% assign year_publications = year_group.items %}
  
  <h3 class="year-heading" id="year-{{ year }}">{{ year }}</h3>
  
  {% for publication in year_publications %}
    {% include citation.html lookup=publication.id style="rich" %}
  {% endfor %}
  
{% endfor %}

{% include section.html %}

## {% include icon.html icon="fa-solid fa-clock-rotate-left" %}Historical Research Records

Recovered materials from the former `bi.snu.ac.kr` site show the lab's earlier research programs in probabilistic learning, molecular computing, bioinformatics, cognitive robotics, multimodal learning, and human-level AI.

### Legacy Research Overview

The older BI research page framed the lab's work as biointelligence: brain-inspired computational intelligence built through mathematical modeling, computer simulation, cognitive experiments, and molecular, neural, and whole-brain models of information processing.

- **Cognitive Computation**: Language-Vision Translation, Cognitive Memory Games, Learning to Talk.
- **Learning and Evolution**: Hypernetworks for Learning and Memory, Probabilistic Graphical Models, Bayesian Evolutionary Computation.
- **Molecular Inference**: Molecular Machine Learning In Vitro, Molecular Theorem Proving, Molecular Evolutionary Computing.

### Research Threads

- **Probabilistic learning and hypernetworks**: earlier BI pages describe hypernetwork models, probabilistic learning, higher-order interaction discovery, and cognitive machine learning. [Learning research page]({{ "/files/legacy/bi.snu.ac.kr/Research/Learning/index.html" | relative_url }})
- **Bioinformatics and molecular AI**: historical work covered DNA computing, molecular evolutionary computation, microarray analysis, biochip design, and gene/protein sequence modeling. [Bioinformatics overview]({{ "/files/legacy/bi.snu.ac.kr/Research/Bioinformatics/bi_bio.html" | relative_url }})
- **Cognitive robotics and video understanding**: recovered pages document projects around learning from digital video, cognitive HRI, activity understanding, and embodied perception-action learning. [Videome page]({{ "/files/legacy/bi.snu.ac.kr/Research/Videome/Videome.html" | relative_url }})
- **Human-level and bio-inspired machine learning**: BIMML and Molecular AI records connect the lab's bio-inspired machine learning agenda to later cognitive AI and embodied AI work. [BIMML page]({{ "/files/legacy/bi.snu.ac.kr/Research/BIMML/BIMML.html" | relative_url }})

### Seminars and Talks

- **BioNetwork Seminar**: recovered seminar records for biological networks and bioinformatics discussions. [BioNetwork materials]({{ "/files/legacy/bi.snu.ac.kr/SEMINAR/BioNetwork.html" | relative_url }})
- **ECBIO Seminar**: evolutionary computation and bioinformatics seminar materials. [ECBIO 2003 materials]({{ "/files/legacy/bi.snu.ac.kr/SEMINAR/ECBIO/ecbio0302.html" | relative_url }})
- **PRML Reading Group**: 2007 Bishop PRML seminar schedule and reading materials. [PRML seminar page]({{ "/files/legacy/bi.snu.ac.kr/SEMINAR/ML/Bishop_PRML/PRML_Bishop_2007Spring.html" | relative_url }})
- **Byoung-Tak Zhang talks and tutorials**: recovered domestic and international talk lists have been folded into the PI profile, including AI, cognitive robotics, DNA computing, hypernetworks, and human-level machine learning topics. [International talks]({{ "/files/legacy/bi.snu.ac.kr/btzhang/Talks_and_Tutorials_Offered_inter.html" | relative_url }}), [domestic talks]({{ "/files/legacy/bi.snu.ac.kr/btzhang/Talks_and_Tutorials_Offered_dome.html" | relative_url }})
