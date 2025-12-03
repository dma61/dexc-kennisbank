---
layout: default
title: "Kennisbank algemeen"
---

# Kennisbank algemeen

<ul>
{% for post in site.posts %}
  {% if post.categories contains "Kennisbank algemeen" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
