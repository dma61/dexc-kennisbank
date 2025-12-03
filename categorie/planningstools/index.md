---
layout: default
title: "Planningstools"
---

# Planningstools

<ul>
{% for post in site.posts %}
  {% if post.categories contains "Planningstools" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
