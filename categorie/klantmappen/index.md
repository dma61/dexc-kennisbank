---
layout: default
title: "Klantmappen"
---

# Klantmappen

<ul>
{% for post in site.posts %}
  {% if post.categories contains "Klantmappen" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
