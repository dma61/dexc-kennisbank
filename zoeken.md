---
layout: default
title: Zoeken
permalink: /zoeken/
---

<div class="search-container">
  <h1>🔍 Zoeken in de kennisbank</h1>
  <input type="text" id="search-input" placeholder="Typ om te zoeken..." autofocus>
  <div id="search-results"></div>
</div>

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script src="{{ '/assets/js/search.js' | relative_url }}"></script>

<style>
.search-container { max-width: 800px; margin: 0 auto; padding: 20px; }
#search-input { 
  width: 100%; padding: 12px; font-size: 18px; 
  border: 2px solid #ddd; border-radius: 8px; margin-bottom: 20px;
}
#search-input:focus { border-color: #0066cc; outline: none; }
.search-result { 
  padding: 15px; margin-bottom: 15px; 
  border: 1px solid #eee; border-radius: 8px;
}
.search-result:hover { background: #f9f9f9; }
.search-result h3 { margin: 0 0 5px 0; }
.search-result .meta { color: #666; font-size: 0.9em; margin: 5px 0; }
.search-result .excerpt { color: #333; }
.no-results { color: #666; font-style: italic; }
</style>
