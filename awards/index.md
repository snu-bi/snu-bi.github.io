---
title: Awards
nav:
  order: 4
  tooltip: Awards and achievements
---

# {% include icon.html icon="fa-solid fa-trophy" %}Awards & Achievements

The Biointelligence Lab has a distinguished record of recognition across international competitions, academic honors, and national awards. From RoboCup victories to government honors, our team continuously pushes the frontier of AI research.

{% include section.html %}

## {% include icon.html icon="fa-solid fa-robot" %}Competition Wins

{% assign competitions = site.data.awards | where: "category", "competition" | sort: "year" | reverse %}
{% for award in competitions %}
<div class="award-card">
  <div class="award-year">{{ award.year }}</div>
  <div class="award-content">
    <div class="award-title">{{ award.title }}</div>
    <div class="award-event">{{ award.event }}{% if award.location %} &mdash; {{ award.location }}{% endif %}</div>
    <div class="award-description">{{ award.description }}</div>
    {% if award.links.size > 0 %}
    <div class="award-links">
      {% for link in award.links %}
        <a href="{{ link.url }}" target="_blank" rel="noopener" class="button" data-style="bare">
          {% include icon.html icon="fa-solid fa-arrow-up-right-from-square" %}
          {{ link.text }}
        </a>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}

{% include section.html %}

## {% include icon.html icon="fa-solid fa-medal" %}Academic & National Awards

{% assign awards_list = site.data.awards | where: "category", "award" | sort: "year" | reverse %}
{% for award in awards_list %}
<div class="award-card">
  <div class="award-year">{{ award.year }}</div>
  <div class="award-content">
    <div class="award-title">{{ award.title }}</div>
    <div class="award-event">{{ award.event }}{% if award.location %} &mdash; {{ award.location }}{% endif %}</div>
    <div class="award-description">{{ award.description }}</div>
    {% if award.links.size > 0 %}
    <div class="award-links">
      {% for link in award.links %}
        <a href="{{ link.url }}" target="_blank" rel="noopener" class="button" data-style="bare">
          {% include icon.html icon="fa-solid fa-arrow-up-right-from-square" %}
          {{ link.text }}
        </a>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}
