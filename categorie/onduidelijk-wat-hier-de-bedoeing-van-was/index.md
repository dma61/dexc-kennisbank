---
layout: default
title: "Onduidelijk wat hier de bedoeing van was"
---

# Onduidelijk wat hier de bedoeing van was

<ul>
{% for post in site.posts %}
  {% if post.categories contains "Onduidelijk wat hier de bedoeing van was" %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
  {% endif %}
{% endfor %}
</ul>

[← Terug naar home]({{ site.baseurl }}/)
