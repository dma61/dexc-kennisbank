---
layout: default
title: Alle artikelen
permalink: /artikelen/
---

# 📚 Alle artikelen

{% assign published_posts = site.posts | where_exp: "post", "post.published != false" %}
{% for post in published_posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d-%m-%Y" }}
{% endfor %}
