# Voortgangsrapport: dexc-kennisbank Jekyll Migratie

**Datum:** 19 december 2025
**Project:** GitHub Pages kennisbank (dma61/dexc-kennisbank)

---

## ✅ Opgeloste Problemen

| # | Probleem | Oplossing | Status |
|---|----------|-----------|--------|
| 1 | Mojibake karakters (â†, â–º, Â, etc.) | Python script voor 66 bestanden + PowerShell fix breadcrumbs | ✅ Opgelost |
| 2 | UTF-8 BOM encoding errors | Bestanden herschreven als UTF-8 zonder BOM | ✅ Opgelost |
| 3 | Liquid Exception invalid byte sequence | post.html en breadcrumbs.html schoon herschreven | ✅ Opgelost |
| 4 | Titel/content overlap op categoriepagina's | Dubbele # Titel verwijderd uit 6 categorie-bestanden | ✅ Opgelost |

---

## 🔄 In Behandeling

| # | Probleem | Status |
|---|----------|--------|
| 1 | Post layout spacing (breadcrumbs/titel/footer door elkaar) | CSS update gepusht, wacht op build |
| 2 | published: false werkt niet (posts blijven zichtbaar) | Nog niet aangepakt |

---

## 📊 Statistieken

- **Bestanden gefixt (mojibake):** 66
- **Categorie-bestanden gefixt (dubbele titels):** 6
- **Commits vandaag:** ~8

---

## 🏗️ Architectuur

dexc-kennisbank/
├── _layouts/
│   └── post.html          # Custom post layout
├── _includes/
│   └── breadcrumbs.html   # Breadcrumb navigatie
├── _posts/                # 280+ artikelen
├── categorieen/           # 6 categorie-pagina's
├── assets/css/
│   └── style.scss         # Custom CSS overrides
└── _config.yml            # Jekyll config (minimal theme)

---

## ⏭️ Volgende Stappen

1. **Verifieer** dat de CSS spacing fix werkt na GitHub Pages build
2. **Fix** published: false probleem indien nog relevant
3. **Overweeg** of het minimal theme voldoende is of dat een custom theme nodig is

---

## 💡 Root Cause Analyse

Het meeste gepruts kwam door:

1. **Theme mismatch:** Het minimal theme verwacht geen h1 in content (titel hoort in sidebar), maar de content had wél # Titel headers
2. **Legacy encoding:** Oude Helpjuice export had mixed encodings en BOM-issues
3. **Iteratief debuggen:** Elke fix onthulde een nieuwe laag problemen (mojibake → BOM → Liquid → overlap)