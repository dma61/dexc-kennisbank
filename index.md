---
layout: default
title: DEXC Kennisbank
---

<div class="home-container">
  <h1>📚 DEXC Kennisbank</h1>
  
  <div class="nav-cards">
    <a href="{{ '/zoeken/' | relative_url }}" class="nav-card">
      <span class="icon">🔍</span>
      <span class="label">Zoeken</span>
    </a>
    <a href="{{ '/categorieen/' | relative_url }}" class="nav-card">
      <span class="icon">📂</span>
      <span class="label">Categorieën</span>
    </a>
    <a href="{{ '/contact/' | relative_url }}" class="nav-card">
      <span class="icon">💬</span>
      <span class="label">Contact</span>
    </a>
  </div>
  
  <h2>Recente artikelen</h2>
  <ul class="post-list">
  {% for post in site.posts limit: 20 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="meta">{{ post.date | date: "%Y-%m-%d" }} | {{ post.categories | join: ", " }}</span>
    </li>
  {% endfor %}
  </ul>
  
  <p><a href="{{ '/categorieen/' | relative_url }}">Bekijk alle {{ site.posts.size }} artikelen →</a></p>
</div>

<style>
.home-container { max-width: 900px; margin: 0 auto; padding: 20px; }
.nav-cards { display: flex; gap: 20px; margin: 30px 0; flex-wrap: wrap; }
.nav-card { 
  flex: 1; min-width: 150px; padding: 30px 20px; 
  background: #f5f5f5; border-radius: 12px; 
  text-align: center; text-decoration: none; color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
}
.nav-card:hover { transform: translateY(-3px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.nav-card .icon { display: block; font-size: 2.5em; margin-bottom: 10px; }
.nav-card .label { font-weight: bold; }
.post-list { list-style: none; padding: 0; }
.post-list li { padding: 12px 0; border-bottom: 1px solid #eee; }
.post-list .meta { display: block; color: #666; font-size: 0.85em; margin-top: 3px; }
</style>
