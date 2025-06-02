---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

The Biointelligence Lab at Seoul National University is a leading research group focused on understanding biological intelligence and developing advanced artificial intelligence systems. Under the direction of Professor Byoung-Tak Zhang, our team explores fundamental questions about how the biological mind works and how we can build intelligent machines that learn and think like the human brain.

Our interdisciplinary team consists of researchers at various academic levels, from master's students to postdoctoral researchers, all working collaboratively on cutting-edge projects in cognitive modeling, computational neuroscience, robotics, and artificial intelligence. We are particularly interested in developing deep learning architectures and algorithms that can help us better understand and replicate human-like intelligence.

Located in the School of Computer Science and Engineering at Seoul National University, our lab provides an dynamic environment for innovative research and academic excellence in the field of artificial intelligence and cognitive science.

{% include section.html %}

# {% include icon.html icon="fa-solid fa-flask" %}Professor
{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

{% include section.html %}
## {% include icon.html icon="fa-solid fa-user-tie" %}Research Professor
{% include list.html data="members" component="portrait" filter="role == 'research-professor'" %}

## PHD Students
{% include list.html data="members" component="portrait" filter="role == 'lab-manager'" %}
{% include list.html data="members" component="portrait" filter="role == 'deputy-lab-manager'" %}
{% include list.html data="members" component="portrait" filter="role == 'phd-candidate' and status != '휴학'" %}
{% include list.html data="members" component="portrait" filter="role == 'phd-student' and status != '휴학'" %}

## Master Students
{% include list.html data="members" component="portrait" filter="role == 'master-student'" %}

## Alumni
{% include list.html data="members" component="portrait" filter="role == 'phd'" %}
{% include list.html data="members" component="portrait" filter="role == 'master'" %}


<!-- ## Undergraduate Students
{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %} -->

<!-- {% include list.html data="members" component="portrait" filter="role == 'phd'" %} -->
<!-- {% include list.html data="members" component="portrait" filter="role == 'master'" %} -->


{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}
