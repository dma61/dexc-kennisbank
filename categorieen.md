---
layout: default
title: Categorieën
permalink: /categorieen/
---

<h1>📂 Categorieën</h1>

{% assign categories = site.posts | map: "categories" | flatten | uniq | sort %}

<div class="category-list">
{% for category in categories %}
  {% assign cat_posts = site.posts | where_exp: "post", "post.categories contains category" %}
  <div class="category-item">
    <h2 id="{{ category | slugify }}">{{ category }} ({{ cat_posts.size }})</h2>
    <ul>
    {% for post in cat_posts limit: 10 %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="date">{{ post.date | date: "%Y-%m-%d" }}</span></li>
    {% endfor %}
    {% if cat_posts.size > 10 %}
      <li><em>... en {{ cat_posts.size | minus: 10 }} meer</em></li>
    {% endif %}
    </ul>
  </div>
{% endfor %}
</div>

<style>
.category-list { max-width: 800px; }
.category-item { margin-bottom: 30px; padding: 20px; background: #f9f9f9; border-radius: 8px; }
.category-item h2 { margin-top: 0; color: #0066cc; }
.category-item ul { list-style: none; padding: 0; }
.category-item li { padding: 5px 0; border-bottom: 1px solid #eee; }
.category-item li:last-child { border-bottom: none; }
.category-item .date { color: #999; font-size: 0.85em; }
</style>
