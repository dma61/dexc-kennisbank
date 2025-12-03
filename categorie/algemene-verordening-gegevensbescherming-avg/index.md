---
layout: default
title: "Algemene Verordening Gegevensbescherming (AVG)"
---

# Algemene Verordening Gegevensbescherming (AVG)

<ul>
{% for post in site.posts %}
  {% if post.categories contains "Algemene Verordening Gegevensbescherming (AVG)" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
