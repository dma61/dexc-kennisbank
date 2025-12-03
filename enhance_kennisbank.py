# enhance_kennisbank.py
# Scaffolding timestamp: 2025-12-03
"""
Verbetert de dexc-kennisbank met zoekfunctie, navigatie en interne links.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(r"C:\MINISFORUMNAB6\DEV\dexc-kennisbank")
POSTS_DIR = BASE_DIR / "_posts"
ASSETS_DIR = BASE_DIR / "assets" / "js"
INCLUDES_DIR = BASE_DIR / "_includes"
LAYOUTS_DIR = BASE_DIR / "_layouts"


def create_directories():
    """Maak benodigde mappen aan."""
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    INCLUDES_DIR.mkdir(exist_ok=True)
    LAYOUTS_DIR.mkdir(exist_ok=True)
    print("✓ Mappen aangemaakt")


def create_search_index():
    """Genereer search-data.json template voor Lunr.js."""
    # Jekyll genereert dit dynamisch, we maken het template
    search_data_template = """{%- assign posts = site.posts -%}
[
{%- for post in posts -%}
  {
    "title": {{ post.title | jsonify }},
    "url": "{{ post.url | relative_url }}",
    "date": "{{ post.date | date: '%Y-%m-%d' }}",
    "categories": {{ post.categories | jsonify }},
    "content": {{ post.content | strip_html | truncatewords: 200 | jsonify }}
  }{%- unless forloop.last -%},{%- endunless -%}
{%- endfor -%}
]"""
    
    search_data_path = BASE_DIR / "search-data.json"
    with open(search_data_path, 'w', encoding='utf-8') as f:
        f.write("---\nlayout: null\n---\n" + search_data_template)
    print("✓ search-data.json template aangemaakt")


def create_search_js():
    """Maak Lunr.js zoekscript."""
    search_js = """// Lunr.js zoekfunctionaliteit voor dexc-kennisbank
(function() {
  let searchIndex = null;
  let searchData = null;

  // Laad zoekdata
  async function loadSearchData() {
    if (searchData) return searchData;
    const response = await fetch('/dexc-kennisbank/search-data.json');
    searchData = await response.json();
    return searchData;
  }

  // Bouw Lunr index
  async function buildIndex() {
    if (searchIndex) return searchIndex;
    const data = await loadSearchData();
    
    searchIndex = lunr(function() {
      this.ref('url');
      this.field('title', { boost: 10 });
      this.field('categories', { boost: 5 });
      this.field('content');
      
      data.forEach(doc => this.add(doc));
    });
    
    return searchIndex;
  }

  // Zoekfunctie
  async function search(query) {
    const index = await buildIndex();
    const data = await loadSearchData();
    const results = index.search(query);
    
    return results.map(result => {
      const doc = data.find(d => d.url === result.ref);
      return { ...doc, score: result.score };
    });
  }

  // Render resultaten
  function renderResults(results, container) {
    if (results.length === 0) {
      container.innerHTML = '<p class="no-results">Geen resultaten gevonden.</p>';
      return;
    }
    
    const html = results.map(r => `
      <div class="search-result">
        <h3><a href="${r.url}">${r.title}</a></h3>
        <p class="meta">${r.date} | ${r.categories.join(', ')}</p>
        <p class="excerpt">${r.content.substring(0, 150)}...</p>
      </div>
    `).join('');
    
    container.innerHTML = html;
  }

  // Init
  document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput || !searchResults) return;
    
    let debounceTimer;
    searchInput.addEventListener('input', function() {
      clearTimeout(debounceTimer);
      const query = this.value.trim();
      
      if (query.length < 2) {
        searchResults.innerHTML = '';
        return;
      }
      
      debounceTimer = setTimeout(async () => {
        const results = await search(query);
        renderResults(results, searchResults);
      }, 300);
    });

    // Check URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const q = urlParams.get('q');
    if (q) {
      searchInput.value = q;
      searchInput.dispatchEvent(new Event('input'));
    }
  });
})();
"""
    
    search_js_path = ASSETS_DIR / "search.js"
    with open(search_js_path, 'w', encoding='utf-8') as f:
        f.write(search_js)
    print("✓ search.js aangemaakt")


def create_search_page():
    """Maak zoekpagina."""
    search_page = """---
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
"""
    
    search_page_path = BASE_DIR / "zoeken.md"
    with open(search_page_path, 'w', encoding='utf-8') as f:
        f.write(search_page)
    print("✓ zoeken.md pagina aangemaakt")


def create_categories_page():
    """Maak categorieën overzichtspagina."""
    categories_page = """---
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
"""
    
    categories_path = BASE_DIR / "categorieen.md"
    with open(categories_path, 'w', encoding='utf-8') as f:
        f.write(categories_page)
    print("✓ categorieen.md pagina aangemaakt")


def create_issues_page():
    """Maak GitHub Issues contact pagina."""
    issues_page = """---
layout: default
title: Contact & Feedback
permalink: /contact/
---

<div class="contact-container">
  <h1>💬 Contact & Feedback</h1>
  
  <p>Heb je een vraag, suggestie of heb je een fout gevonden? Laat het ons weten via GitHub Issues!</p>
  
  <div class="issue-buttons">
    <a href="https://github.com/dma61/dexc-kennisbank/issues/new?template=vraag.md&title=[Vraag]%20" class="btn btn-question">
      ❓ Stel een vraag
    </a>
    
    <a href="https://github.com/dma61/dexc-kennisbank/issues/new?template=fout.md&title=[Fout]%20" class="btn btn-bug">
      🐛 Meld een fout
    </a>
    
    <a href="https://github.com/dma61/dexc-kennisbank/issues/new?template=suggestie.md&title=[Suggestie]%20" class="btn btn-suggestion">
      💡 Doe een suggestie
    </a>
    
    <a href="https://github.com/dma61/dexc-kennisbank/issues" class="btn btn-view">
      📋 Bekijk alle issues
    </a>
  </div>
  
  <h2>Direct contact</h2>
  <p>Voor urgente zaken kun je ook direct contact opnemen met <a href="https://github.com/dma61">@dma61</a> op GitHub.</p>
</div>

<style>
.contact-container { max-width: 700px; margin: 0 auto; padding: 20px; }
.issue-buttons { display: flex; flex-wrap: wrap; gap: 15px; margin: 30px 0; }
.btn { 
  display: inline-block; padding: 15px 25px; 
  border-radius: 8px; text-decoration: none; 
  font-weight: bold; transition: transform 0.2s;
}
.btn:hover { transform: translateY(-2px); }
.btn-question { background: #0066cc; color: white; }
.btn-bug { background: #dc3545; color: white; }
.btn-suggestion { background: #28a745; color: white; }
.btn-view { background: #6c757d; color: white; }
</style>
"""
    
    contact_path = BASE_DIR / "contact.md"
    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(issues_page)
    print("✓ contact.md pagina aangemaakt (→ GitHub Issues)")


def create_issue_templates():
    """Maak GitHub Issue templates."""
    templates_dir = BASE_DIR / ".github" / "ISSUE_TEMPLATE"
    templates_dir.mkdir(parents=True, exist_ok=True)
    
    vraag_template = """---
name: ❓ Vraag
about: Stel een vraag over de kennisbank
title: '[Vraag] '
labels: question
assignees: dma61
---

**Mijn vraag**
Beschrijf je vraag hier.

**Relevant artikel (indien van toepassing)**
Link naar het artikel waar je vraag over gaat.

**Extra context**
Voeg eventuele extra informatie toe.
"""
    
    fout_template = """---
name: 🐛 Fout melden
about: Meld een fout of onjuiste informatie
title: '[Fout] '
labels: bug
assignees: dma61
---

**Beschrijving van de fout**
Wat klopt er niet?

**Locatie**
In welk artikel of op welke pagina?

**Verwachte informatie**
Wat zou er moeten staan?
"""
    
    suggestie_template = """---
name: 💡 Suggestie
about: Doe een suggestie voor verbetering
title: '[Suggestie] '
labels: enhancement
assignees: dma61
---

**Beschrijving**
Beschrijf je suggestie.

**Waarom?**
Waarom zou dit een verbetering zijn?
"""
    
    with open(templates_dir / "vraag.md", 'w', encoding='utf-8') as f:
        f.write(vraag_template)
    with open(templates_dir / "fout.md", 'w', encoding='utf-8') as f:
        f.write(fout_template)
    with open(templates_dir / "suggestie.md", 'w', encoding='utf-8') as f:
        f.write(suggestie_template)
    
    print("✓ GitHub Issue templates aangemaakt")


def fix_internal_links():
    """Fix interne Helpjuice links naar lokale links."""
    fixed_count = 0
    
    # Verzamel alle slugs
    slug_map = {}
    for post in POSTS_DIR.glob("*.md"):
        with open(post, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Haal slug uit bestandsnaam (YYYY-MM-DD-slug.md)
        slug = post.stem[11:]  # verwijder datum prefix
        slug_map[slug] = post.stem
    
    # Fix links in alle posts
    for post in POSTS_DIR.glob("*.md"):
        with open(post, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix kennisbank.dexc.nl links
        content = re.sub(
            r'https?://kennisbank\.dexc\.nl/([a-z0-9-]+)',
            lambda m: f'{{{{ site.baseurl }}}}/{{% post_url ' + (slug_map.get(m.group(1), m.group(1))) + ' %}}' if m.group(1) in slug_map else m.group(0),
            content
        )
        
        if content != original:
            with open(post, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
    
    print(f"✓ Interne links gefixt in {fixed_count} bestanden")


def update_index_page():
    """Update de index pagina met navigatie."""
    index_path = BASE_DIR / "index.md"
    
    index_content = """---
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
"""
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("✓ index.md bijgewerkt met navigatie")


def main():
    print("=== DEXC Kennisbank Uitbreiding ===\n")
    
    create_directories()
    create_search_index()
    create_search_js()
    create_search_page()
    create_categories_page()
    create_issues_page()
    create_issue_templates()
    fix_internal_links()
    update_index_page()
    
    print("\n✅ Klaar! Voer uit:")
    print("   git add .")
    print('   git commit -m "Add search, categories, navigation and contact page"')
    print("   git push")


if __name__ == "__main__":
    main()