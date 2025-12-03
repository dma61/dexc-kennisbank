# Scaffolding timestamp: 2025-01-03
"""
DEXC Kennisbank Regenerator
Regenereert _posts met correcte titels uit questions.csv
"""

import csv
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime
from html import unescape

csv.field_size_limit(10_000_000)

# === CONFIGURATIE ===
BASE_DIR = Path(r"C:\MINISFORUMNAB6\DEV\dexc-kennisbank")
CSV_DIR = BASE_DIR / "csv"
POSTS_DIR = BASE_DIR / "_posts"

QUESTIONS_CSV = CSV_DIR / "u1108114919_questions.csv"
ANSWERS_CSV = CSV_DIR / "u1108114919_answers.csv"
CATEGORIES_CSV = CSV_DIR / "u1108114919_categories.csv"
CATEGORIZATIONS_CSV = CSV_DIR / "u1108114919_categorizations.csv"


def load_questions(csv_path):
    questions = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('id', '').strip()
            name = row.get('name', '').strip()
            codename = row.get('codename', '').strip()
            created = row.get('created_at', '').strip()
            is_published = row.get('is_published', '').strip().lower() == 'true'
            
            if qid and name:
                questions[qid] = {
                    'title': name,
                    'slug': codename or f"artikel-{qid}",
                    'created_at': created,
                    'is_published': is_published
                }
    return questions


def load_answers(csv_path):
    answers = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('question_id', '').strip()
            body_txt = row.get('body_txt', '').strip()
            body = row.get('body', '').strip()
            created = row.get('created_at', '').strip()
            
            if qid:
                answers[qid] = {
                    'body_txt': body_txt,
                    'body_html': body,
                    'created_at': created
                }
    return answers


def load_categories(csv_path):
    categories = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat_id = row.get('id', '').strip()
            name = row.get('name', '').strip()
            if cat_id and name:
                categories[cat_id] = name
    return categories


def load_categorizations(csv_path):
    categorizations = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('question_id', '').strip()
            cat_id = row.get('category_id', '').strip()
            if qid and cat_id:
                if qid not in categorizations:
                    categorizations[qid] = []
                categorizations[qid].append(cat_id)
    return categorizations


def html_to_markdown(html_content):
    if not html_content:
        return ""
    
    text = html_content
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',r'![](\1)', text, flags=re.DOTALL)
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL)
    text = re.sub(r'</?[ou]l[^>]*>', '', text)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<hr\s*/?>', '\n---\n', text)
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<table[^>]*>.*?</table>', '[Tabel - zie origineel]', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:50]


def parse_date(date_str):
    if not date_str:
        return datetime.now()
    try:
        return datetime.strptime(date_str.replace(' UTC', ''), '%Y-%m-%d %H:%M:%S')
    except:
        return datetime.now()


def generate_posts():
    print("Laden van CSV bestanden...")
    questions = load_questions(QUESTIONS_CSV)
    answers = load_answers(ANSWERS_CSV)
    categories = load_categories(CATEGORIES_CSV)
    categorizations = load_categorizations(CATEGORIZATIONS_CSV)
    
    print(f"  - {len(questions)} questions geladen")
    print(f"  - {len(answers)} answers geladen")
    print(f"  - {len(categories)} categories geladen")
    print(f"  - {len(categorizations)} categorizations geladen")
    
    if POSTS_DIR.exists():
        shutil.rmtree(POSTS_DIR)
    POSTS_DIR.mkdir(exist_ok=True)
    
    print("\nGenereren van posts...")
    generated = 0
    skipped = 0
    
    for qid, q_data in questions.items():
        title = q_data['title']
        slug = q_data['slug']
        created = parse_date(q_data['created_at'])
        
        if title.lower().startswith('(sample)') or title.lower().startswith('helpjuice'):
            skipped += 1
            continue
        if 'untitled article' in title.lower():
            skipped += 1
            continue
        
        answer = answers.get(qid, {})
        body_html = answer.get('body_html', '')
        body_txt = answer.get('body_txt', '')
        
        if body_html:
            content = html_to_markdown(body_html)
        elif body_txt:
            content = body_txt
        else:
            content = "*Geen inhoud beschikbaar.*"
        
        cat_ids = categorizations.get(qid, [])
        cat_names = [categories.get(cid, '') for cid in cat_ids if cid in categories]
        cat_names = [c for c in cat_names if c and not c.startswith('(Sample)')]
        
        date_str = created.strftime('%Y-%m-%d')
        safe_slug = slugify(slug) or slugify(title) or f"artikel-{qid}"
        filename = f"{date_str}-{safe_slug}.md"
        filepath = POSTS_DIR / filename
        
        yaml_categories = str(cat_names).replace("'", '"') if cat_names else '[]'
        
        post_content = f"""---
layout: post
title: "{title.replace('"', '\\"')}"
date: {date_str}
categories: {yaml_categories}
question_id: {qid}
---

# {title}

{content}

---

[← Terug naar home]({{{{ site.baseurl }}}}/)
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_content)
        
        generated += 1
        if generated % 50 == 0:
            print(f"  {generated} posts gegenereerd...")
    
    print(f"\n✅ Klaar!")
    print(f"   - {generated} posts gegenereerd")
    print(f"   - {skipped} overgeslagen")


if __name__ == "__main__":
    generate_posts()