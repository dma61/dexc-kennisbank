---
layout: default
title: "Afsprakenstelsel"
---

# Afsprakenstelsel

<ul>
{% for post in site.posts %}
  {% if post.categories contains "Afsprakenstelsel" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
