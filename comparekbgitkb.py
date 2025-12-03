# compare_kennisbank.py
"""
Vergelijkt GitHub Pages export met originele Helpjuice kennisbank.
"""

import csv
import requests
from pathlib import Path
from bs4 import BeautifulSoup

csv.field_size_limit(10_000_000)

BASE_DIR = Path(r"C:\MINISFORUMNAB6\DEV\dexc-kennisbank")
POSTS_DIR = BASE_DIR / "_posts"
QUESTIONS_CSV = BASE_DIR / "csv" / "u1108114919_questions.csv"

def get_exported_articles():
    """Haal alle geëxporteerde question_ids op."""
    ids = set()
    for post in POSTS_DIR.glob("*.md"):
        with open(post, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('question_id:'):
                    ids.add(line.split(':')[1].strip())
                    break
    return ids

def get_csv_articles():
    """Haal alle articles uit questions.csv."""
    articles = {}
    with open(QUESTIONS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row.get('id', '').strip()
            name = row.get('name', '').strip()
            is_published = row.get('is_published', '').strip().lower() == 'true'
            codename = row.get('codename', '').strip()
            
            if qid:
                articles[qid] = {
                    'title': name,
                    'is_published': is_published,
                    'slug': codename,
                    'url': f"https://kennisbank.dexc.nl/{codename}" if codename else None
                }
    return articles

def main():
    print("=== DEXC Kennisbank Vergelijking ===\n")
    
    exported = get_exported_articles()
    csv_articles = get_csv_articles()
    
    print(f"Totaal in CSV: {len(csv_articles)}")
    print(f"Geëxporteerd naar GitHub: {len(exported)}")
    
    # Gepubliceerde artikelen in CSV
    published = {k: v for k, v in csv_articles.items() if v['is_published']}
    unpublished = {k: v for k, v in csv_articles.items() if not v['is_published']}
    
    print(f"Gepubliceerd in CSV: {len(published)}")
    print(f"Niet gepubliceerd: {len(unpublished)}")
    
    # Wat mist er?
    missing_from_export = set(csv_articles.keys()) - exported
    extra_in_export = exported - set(csv_articles.keys())
    
    print(f"\n--- Niet geëxporteerd ({len(missing_from_export)}) ---")
    for qid in sorted(missing_from_export)[:20]:
        art = csv_articles.get(qid, {})
        status = "✓ pub" if art.get('is_published') else "✗ draft"
        print(f"  [{status}] {qid}: {art.get('title', '?')[:50]}")
    
    if len(missing_from_export) > 20:
        print(f"  ... en {len(missing_from_export) - 20} meer")
    
    # Wat ontbreekt in de CSV maar staat wel online?
    print(f"\n--- Helpjuice features die ontbreken in export ---")
    print("  • Zoekfunctie (##search_query=...)")
    print("  • Contact formulier (/contact-us)")
    print("  • Dynamische categorieën/navigatie")
    print("  • Interne links tussen artikelen")
    print("  • Statistieken/analytics")

if __name__ == "__main__":
    main()