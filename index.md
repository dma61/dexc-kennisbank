---
layout: default
title: Home
---

# Data Exchange Kennisbank

Welkom bij de kennisbank voor ICT-professionals werkzaam aan Data Exchange binnen de financiële sector.

---

## Categorieën

- [(Sample) Internal Category]({{ site.baseurl }}/categorie/sample-internal-category/) (1 artikelen)
- [(Sample) Using Helpjuice]({{ site.baseurl }}/categorie/sample-using-helpjuice/) (2 artikelen)
- [Afsprakenstelsel]({{ site.baseurl }}/categorie/afsprakenstelsel/) (2 artikelen)
- [Algemene Verordening Gegevensbescherming (AVG)]({{ site.baseurl }}/categorie/algemene-verordening-gegevensbescherming-avg/) (4 artikelen)
- [Basic koppelingsvarianten]({{ site.baseurl }}/categorie/basic-koppelingsvarianten/) (6 artikelen)
- [Bouwstenen/Principes]({{ site.baseurl }}/categorie/bouwstenenprincipes/) (68 artikelen)
- [Databronnen]({{ site.baseurl }}/categorie/databronnen/) (6 artikelen)
- [Gegevensstandaarden]({{ site.baseurl }}/categorie/gegevensstandaarden/) (3 artikelen)
- [Huishoudboekjes]({{ site.baseurl }}/categorie/huishoudboekjes/) (9 artikelen)
- [Intern]({{ site.baseurl }}/categorie/intern/) (6 artikelen)
- [Jaarlijks checken! (januari)]({{ site.baseurl }}/categorie/jaarlijks-checken-januari/) (4 artikelen)
- [Kennisbank algemeen]({{ site.baseurl }}/categorie/kennisbank-algemeen/) (14 artikelen)
- [Klantmappen]({{ site.baseurl }}/categorie/klantmappen/) (1 artikelen)
- [Onduidelijk wat hier de bedoeing van was]({{ site.baseurl }}/categorie/onduidelijk-wat-hier-de-bedoeing-van-was/) (6 artikelen)
- [Operators (regietoepassingen)]({{ site.baseurl }}/categorie/operators-regietoepassingen/) (13 artikelen)
- [Oplossingen  ► particuliere klant]({{ site.baseurl }}/categorie/oplossingen-particuliere-klant/) (2 artikelen)
- [Oplossingen  ► zakelijke klant]({{ site.baseurl }}/categorie/oplossingen-zakelijke-klant/) (4 artikelen)
- [Oplossingen ► B2B (keten)]({{ site.baseurl }}/categorie/oplossingen-b2b-keten/) (41 artikelen)
- [Oplossingen ► Particuliere klant]({{ site.baseurl }}/categorie/oplossingen-particuliere-klant/) (5 artikelen)
- [Oplossingen ► Zakelijke klant]({{ site.baseurl }}/categorie/oplossingen-zakelijke-klant/) (6 artikelen)
- [Oplossingen ► particuliere klant]({{ site.baseurl }}/categorie/oplossingen-particuliere-klant/) (16 artikelen)
- [Oplossingen ► zakelijke klant]({{ site.baseurl }}/categorie/oplossingen-zakelijke-klant/) (7 artikelen)
- [Overig]({{ site.baseurl }}/categorie/overig/) (40 artikelen)
- [Planningstools]({{ site.baseurl }}/categorie/planningstools/) (13 artikelen)
- [Services]({{ site.baseurl }}/categorie/services/) (3 artikelen)
- [Standaarden ► B2B (keten)]({{ site.baseurl }}/categorie/standaarden-b2b-keten/) (10 artikelen)
- [Standaarden ► particuliere klant]({{ site.baseurl }}/categorie/standaarden-particuliere-klant/) (3 artikelen)
- [Standaarden ►zakelijke klant]({{ site.baseurl }}/categorie/standaarden-zakelijke-klant/) (9 artikelen)
- [Toegang]({{ site.baseurl }}/categorie/toegang/) (2 artikelen)
- [Toegang tot gegevens bij financiële dienstverleners]({{ site.baseurl }}/categorie/toegang-tot-gegevens-bij-financiele-dienstverlener/) (1 artikelen)
- [Tools bij schuldhulpverlening en voorkomen van schulden]({{ site.baseurl }}/categorie/tools-bij-schuldhulpverlening-en-voorkomen-van-sch/) (8 artikelen)
- [Transport]({{ site.baseurl }}/categorie/transport/) (5 artikelen)
- [Wetgeving]({{ site.baseurl }}/categorie/wetgeving/) (27 artikelen)
- [eHerkenning]({{ site.baseurl }}/categorie/eherkenning/) (7 artikelen)
- [iDIN]({{ site.baseurl }}/categorie/idin/) (2 artikelen)

---

## Alle artikelen

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>({{ post.date | date: "%d-%m-%Y" }})</small>
  </li>
{% endfor %}
</ul>
