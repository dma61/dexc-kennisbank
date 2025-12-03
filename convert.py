#!/usr/bin/env python3
"""
Helpjuice kennisbank.dexc.nl → GitHub Pages Converter
"""

import csv
import re
import html
from pathlib import Path
from datetime import datetime
from collections import defaultdict

csv.field_size_limit(2147483647)

# =============================================================================
# CONFIGURATIE
# =============================================================================

REPO_NAME = "dexc-kennisbank"
GITHUB_USER = "dma61"
PROJECT_NAME = "Data Exchange Kennisbank"

CSV_DIR = Path("csv")
OUTPUT_DIR = Path(".")

# =============================================================================
# HTML → MARKDOWN CONVERTER
# =============================================================================

def html_to_markdown(html_content):
    """Simpele HTML naar Markdown conversie."""
    if not html_content:
        return ""
    
    text = html_content
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Headers
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', text, flags=re.DOTALL)
    
    # Bold en italic
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)
    
    # Links
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)
    
    # Images
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?\s*>', r'![\2](\1)', text)
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?\s*>', r'![](\1)', text)
    
    # Lists
    text = re.sub(r'<ul[^>]*>', '\n', text)
    text = re.sub(r'</ul>', '\n', text)
    text = re.sub(r'<ol[^>]*>', '\n', text)
    text = re.sub(r'</ol>', '\n', text)
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL)
    
    # Code blocks
    text = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', text, flags=re.DOTALL)
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
    
    # Paragraphs en line breaks
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<hr\s*/?>', '\n---\n', text)
    
    # Tables (basis)
    text = re.sub(r'<table[^>]*>', '\n', text)
    text = re.sub(r'</table>', '\n', text)
    text = re.sub(r'<tr[^>]*>', '', text)
    text = re.sub(r'</tr>', ' |\n', text)
    text = re.sub(r'<t[hd][^>]*>(.*?)</t[hd]>', r'| \1 ', text, flags=re.DOTALL)
    
    # Verwijder overige HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text

# =============================================================================
# GITHUB PAGES BESTANDEN
# =============================================================================

def get_config_yml():
    return f'''title: "{PROJECT_NAME}"
description: "Kennisbank voor ICT-professionals in financiële Data Exchange"
baseurl: "/{REPO_NAME}"
url: "https://{GITHUB_USER}.github.io"

remote_theme: pages-themes/minimal@v0.2.0
plugins:
  - jekyll-remote-theme

markdown: kramdown
kramdown:
  input: GFM

defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "default"
'''

def get_index_md(categories_with_counts):
    cat_list = "\n".join([
        f'- [{name}]({{{{ site.baseurl }}}}/categorie/{slugify(name)}/) ({count} artikelen)'
        for name, count in sorted(categories_with_counts.items())
    ])
    
    return f'''---
layout: default
title: Home
---

# {PROJECT_NAME}

Welkom bij de kennisbank voor ICT-professionals werkzaam aan Data Exchange binnen de financiële sector.

---

## Categorieën

{cat_list}

---

## Alle artikelen

<ul>
{{% for post in site.posts %}}
  <li>
    <a href="{{{{ post.url | relative_url }}}}">{{{{ post.title }}}}</a>
    <small>({{{{ post.date | date: "%d-%m-%Y" }}}})</small>
  </li>
{{% endfor %}}
</ul>
'''

def get_category_page(cat_name):
    return f'''---
layout: default
title: "{cat_name}"
---

# {cat_name}

<ul>
{{% for post in site.posts %}}
  {{% if post.categories contains "{cat_name}" %}}
  <li>
    <a href="{{{{ post.url | relative_url }}}}">{{{{ post.title }}}}</a>
    <small>({{{{ post.date | date: "%d-%m-%Y" }}}})</small>
  </li>
  {{% endif %}}
{{% endfor %}}
</ul>

[← Terug naar home]({{{{ site.baseurl }}}}/)
'''

# =============================================================================
# HELPERS
# =============================================================================

def slugify(text):
    if not text:
        return "untitled"
    text = text.lower()
    text = text.replace('é', 'e').replace('ë', 'e').replace('ï', 'i')
    text = text.replace('ö', 'o').replace('ü', 'u').replace('ä', 'a')
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:50] or "untitled"

def load_csv(filename):
    filepath = CSV_DIR / filename
    if not filepath.exists():
        print(f"⚠️  Niet gevonden: {filepath}")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    print(f"✓ {filename}: {len(data)} rijen")
    return data

# =============================================================================
# MAIN
# =============================================================================

def main():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  Helpjuice → GitHub Pages Converter                          ║
║  Bron: kennisbank.dexc.nl                                    ║
║  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                                        ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    if not CSV_DIR.exists():
        print(f"❌ CSV map niet gevonden: {CSV_DIR.absolute()}")
        return
    
    print("📥 Data laden...")
    
    categories = {}
    for c in load_csv('u1108114919_categories.csv'):
        cid = c.get('id', '').strip()
        name = c.get('name', '').strip()
        if cid and name:
            categories[cid] = name
    
    q_to_cats = defaultdict(list)
    for c in load_csv('u1108114919_categorizations.csv'):
        qid = c.get('question_id', '').strip()
        cid = c.get('category_id', '').strip()
        if qid and cid:
            q_to_cats[qid].append(cid)
    
    questions = {}
    for q in load_csv('u1108114919_questions.csv'):
        qid = q.get('id', '').strip()
        if qid:
            questions[qid] = {
                'title': q.get('title', '').strip() or f'Artikel {qid}',
                'slug': q.get('slug', '').strip(),
                'created_at': q.get('created_at', '').strip()
            }
    
    answers = load_csv('u1108114919_answers.csv')
    
    if not answers:
        print("❌ Geen answers data. Stop.")
        return
    
    posts_dir = OUTPUT_DIR / '_posts'
    posts_dir.mkdir(exist_ok=True)
    
    cat_dir = OUTPUT_DIR / 'categorie'
    cat_dir.mkdir(exist_ok=True)
    
    print(f"\n📝 Artikelen converteren (HTML → Markdown)...")
    
    success = 0
    failed = 0
    skipped = 0
    used_filenames = set()
    category_counts = defaultdict(int)
    
    for answer in answers:
        try:
            aid = answer.get('id', '').strip()
            qid = answer.get('question_id', '').strip()
            
            # Gebruik 'body' (HTML) als bron
            body_html = answer.get('body', '')
            
            if not body_html or not body_html.strip():
                skipped += 1
                continue
            
            # Converteer HTML naar Markdown
            body_md = html_to_markdown(body_html)
            
            q_info = questions.get(qid, {})
            title = q_info.get('title') or f'Artikel {aid}'
            created = q_info.get('created_at') or answer.get('created_at', '').strip()
            
            cat_ids = q_to_cats.get(qid, [])
            cat_names = [categories.get(cid, 'Overig') for cid in cat_ids]
            if not cat_names:
                cat_names = ['Overig']
            
            for cn in cat_names:
                category_counts[cn] += 1
            
            if created and len(created) >= 10:
                date_str = created[:10]
            else:
                date_str = '2024-01-01'
            
            slug = slugify(title)
            base_filename = f"{date_str}-{slug}"
            filename = f"{base_filename}.md"
            counter = 1
            while filename in used_filenames:
                filename = f"{base_filename}-{counter}.md"
                counter += 1
            used_filenames.add(filename)
            
            title_safe = title.replace('"', '\\"')
            cats_yaml = ', '.join(f'"{c}"' for c in cat_names)
            
            content = f'''---
layout: default
title: "{title_safe}"
date: {date_str}
categories: [{cats_yaml}]
question_id: {qid}
answer_id: {aid}
---

# {title}

{body_md}

---

[← Terug naar home]({{{{ site.baseurl }}}}/)
'''
            
            (posts_dir / filename).write_text(content, encoding='utf-8')
            success += 1
            
        except Exception as e:
            failed += 1
            print(f"  ⚠️ Fout bij {answer.get('id', '?')}: {e}")
    
    print(f"✓ {success} artikelen, {skipped} overgeslagen (leeg), {failed} fouten")
    
    print(f"\n📁 Categorie pagina's...")
    
    for cat_name in category_counts.keys():
        cat_slug = slugify(cat_name)
        cat_page_dir = cat_dir / cat_slug
        cat_page_dir.mkdir(exist_ok=True)
        (cat_page_dir / 'index.md').write_text(get_category_page(cat_name), encoding='utf-8')
    
    print(f"✓ {len(category_counts)} categorie pagina's")
    
    print(f"\n📄 Config bestanden...")
    
    (OUTPUT_DIR / '_config.yml').write_text(get_config_yml(), encoding='utf-8')
    print("✓ _config.yml")
    
    (OUTPUT_DIR / 'index.md').write_text(get_index_md(category_counts), encoding='utf-8')
    print("✓ index.md")
    
    (OUTPUT_DIR / 'Gemfile').write_text('source "https://rubygems.org"\ngem "github-pages", group: :jekyll_plugins\n', encoding='utf-8')
    print("✓ Gemfile")
    
    (OUTPUT_DIR / '.gitignore').write_text('_site/\n.jekyll-cache/\n.bundle/\nvendor/\n*.log\ncsv/\n', encoding='utf-8')
    print("✓ .gitignore")
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  ✅ CONVERSIE VOLTOOID!                                      ║
╠══════════════════════════════════════════════════════════════╣
║  {success:>4} artikelen in _posts/                                ║
║  {len(category_counts):>4} categorieën in categorie/                           ║
╠══════════════════════════════════════════════════════════════╣
║  Nu doen:                                                    ║
║  1. git init                                                 ║
║  2. git add .                                                ║
║  3. git commit -m "Helpjuice import"                         ║
║  4. git branch -M main                                       ║
║  5. git remote add origin                                    ║
║       https://github.com/{GITHUB_USER}/{REPO_NAME}.git            ║
║  6. git push -u origin main                                  ║
║  7. Settings → Pages → main branch                           ║
║  8. https://{GITHUB_USER}.github.io/{REPO_NAME}/                  ║
╚══════════════════════════════════════════════════════════════╝
    """)

if __name__ == '__main__':
    main()