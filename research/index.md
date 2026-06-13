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

<div class="publication-overview" aria-label="Publication overview">
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

