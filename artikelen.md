---
layout: default
title: Alle artikelen
permalink: /artikelen/
---

# 📚 Alle artikelen

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d-%m-%Y" }}
{% endfor %}
