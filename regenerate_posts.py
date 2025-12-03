# regenerate_posts.py
# Scaffolding timestamp: 2025-12-03
"""
Converteert Helpjuice CSV-export naar Jekyll _posts met correcte tabelconversie.
"""

import csv
import re
import sys
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

# Verhoog CSV field size limit
csv.field_size_limit(2147483647)

BASE_DIR = Path(r"C:\MINISFORUMNAB6\DEV\dexc-kennisbank")
CSV_DIR = BASE_DIR / "csv"
POSTS_DIR = BASE_DIR / "_posts"

def html_table_to_markdown(table_soup):
    """Converteer HTML <table> naar Markdown tabel."""
    rows = []
    
    # Header rij (thead of eerste tr)
    header_row = table_soup.find('thead')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
    else:
        first_row = table_soup.find('tr')
        if first_row:
            headers = [cell.get_text(strip=True) for cell in first_row.find_all(['th', 'td'])]
        else:
            return ""
    
    if not headers:
        return ""
    
    # Markdown header
    rows.append("| " + " | ".join(headers) + " |")
    rows.append("| " + " | ".join(["---"] * len(headers)) + " |")
    
    # Data rijen
    tbody = table_soup.find('tbody')
    data_rows = tbody.find_all('tr') if tbody else table_soup.find_all('tr')[1:]
    
    for tr in data_rows:
        cells = tr.find_all(['td', 'th'])
        # Behoud links in cellen
        cell_contents = []
        for cell in cells:
            # Check voor links
            link = cell.find('a')
            if link and link.get('href'):
                text = link.get_text(strip=True)
                href = link['href']
                cell_contents.append(f"[{text}]({href})")
            else:
                # Gewone tekst, verwijder newlines en extra spaties
                text = cell.get_text(strip=True)
                text = re.sub(r'\s+', ' ', text)
                # Escape pipe characters
                text = text.replace('|', '\\|')
                cell_contents.append(text)
        
        if cell_contents:
            rows.append("| " + " | ".join(cell_contents) + " |")
    
    return "\n".join(rows)

def html_to_markdown(html_content):
    """Converteer HTML naar Markdown met tabelondersteuning."""
    if not html_content:
        return ""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Converteer tabellen EERST (voordat we andere HTML verwerken)
    for table in soup.find_all('table'):
        md_table = html_table_to_markdown(table)
        table.replace_with(BeautifulSoup(f"\n\n{md_table}\n\n", 'html.parser'))
    
    # Converteer links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        if href and text:
            a.replace_with(f"[{text}]({href})")
    
    # Converteer bold/strong
    for tag in soup.find_all(['strong', 'b']):
        text = tag.get_text()
        tag.replace_with(f"**{text}**")
    
    # Converteer italic/em
    for tag in soup.find_all(['em', 'i']):
        text = tag.get_text()
        tag.replace_with(f"*{text}*")
    
    # Converteer headers
    for i in range(1, 7):
        for tag in soup.find_all(f'h{i}'):
            text = tag.get_text(strip=True)
            tag.replace_with(f"\n\n{'#' * i} {text}\n\n")
    
    # Converteer lijsten
    for ul in soup.find_all('ul'):
        items = []
        for li in ul.find_all('li', recursive=False):
            items.append(f"- {li.get_text(strip=True)}")
        ul.replace_with("\n" + "\n".join(items) + "\n")
    
    for ol in soup.find_all('ol'):
        items = []
        for idx, li in enumerate(ol.find_all('li', recursive=False), 1):
            items.append(f"{idx}. {li.get_text(strip=True)}")
        ol.replace_with("\n" + "\n".join(items) + "\n")
    
    # Converteer paragrafen
    for p in soup.find_all('p'):
        text = p.get_text()
        p.replace_with(f"\n\n{text}\n\n")
    
    # Converteer line breaks
    for br in soup.find_all('br'):
        br.replace_with("\n")
    
    # Haal tekst op en clean up
    text = soup.get_text()
    
    # Verwijder Helpjuice glossary spans (data-definition etc.)
    text = re.sub(r'\s+', ' ', text)
    
    # Fix multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Herstel markdown tabellen (die zijn al correct geformatteerd)
    # Ze kunnen platgeslagen zijn door get_text()
    
    return text.strip()

def regenerate_posts_from_html():
    """Regenereer posts met originele HTML uit answers.csv."""
    
    # Laad answers (bevat HTML content)
    answers = {}
    answers_file = list(CSV_DIR.glob("*answers.csv"))[0]
    with open(answers_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('question_id', '')
            html = row.get('body', '')
            if qid and html:
                answers[qid] = html
    
    # Laad questions (metadata)
    questions = {}
    questions_file = list(CSV_DIR.glob("*questions.csv"))[0]
    with open(questions_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('id', '')
            if qid:
                questions[qid] = {
                    'title': row.get('name', ''),
                    'slug': row.get('codename', ''),
                    'published_at': row.get('published_at', ''),
                    'accessibility': row.get('accessibility', '')
                }
    
    # Laad categorieën
    categories = {}
    categories_file = list(CSV_DIR.glob("*categories.csv"))[0]
    with open(categories_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = row.get('id', '')
            name = row.get('name', '')
            if cid and name:
                categories[cid] = name
    
    # Laad categorizations (question -> category mapping)
    categorizations = {}
    cat_file = list(CSV_DIR.glob("*categorizations.csv"))[0]
    with open(cat_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('question_id', '')
            cid = row.get('category_id', '')
            if qid and cid:
                if qid not in categorizations:
                    categorizations[qid] = []
                if cid in categories:
                    categorizations[qid].append(categories[cid])
    
    # Genereer posts
    POSTS_DIR.mkdir(exist_ok=True)
    
    generated = 0
    skipped = 0
    
    for qid, meta in questions.items():
        title = meta['title']
        slug = meta['slug']
        published = meta['published_at']
        
        # Skip samples/tests
        if any(x in title.lower() for x in ['sample', 'test', 'example']):
            skipped += 1
            continue
        
        # Parse datum
        if published:
            try:
                dt = datetime.fromisoformat(published.replace('Z', '+00:00'))
                date_str = dt.strftime('%Y-%m-%d')
            except:
                date_str = datetime.now().strftime('%Y-%m-%d')
        else:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        # Haal HTML content
        html_content = answers.get(qid, '')
        
        # Converteer naar Markdown
        md_content = html_to_markdown(html_content)
        
        # Haal categorieën
        cats = categorizations.get(qid, ['Algemeen'])
        
        # Bouw frontmatter
        frontmatter = f"""---
layout: post
title: "{title.replace('"', '\\"')}"
date: {date_str}
categories: {cats}
question_id: {qid}
---
"""
        
        # Schrijf bestand
        filename = f"{date_str}-{slug}.md"
        filepath = POSTS_DIR / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write("\n")
            f.write(f"# {title}\n\n")
            f.write(md_content)
        
        generated += 1
    
    print(f"=== Regenerate Posts Complete ===")
    print(f"✓ {generated} posts gegenereerd")
    print(f"⊘ {skipped} posts overgeslagen (sample/test)")

if __name__ == "__main__":
    regenerate_posts_from_html()