---
layout: default
title: "(Sample) Using Helpjuice"
---

# (Sample) Using Helpjuice

<ul>
{% for post in site.posts %}
  {% if post.categories contains "(Sample) Using Helpjuice" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
