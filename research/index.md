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

<!-- Group publications by year -->
{% assign publications_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% for year_group in publications_by_year %}
  {% assign year = year_group.name %}
  {% assign publications = year_group.items %}
  
  <h3 class="year-heading">{{ year }}</h3>
  
  {% for publication in publications %}
    {% include citation.html lookup=publication.id style="rich" %}
  {% endfor %}
  
{% endfor %}
