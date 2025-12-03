---
layout: post
title: "Bouwstenen gegevensstandaard AFD 1.0"
date: 2022-09-15
categories: ["Bouwstenen/Principes"]
question_id: 1513979
---

# Bouwstenen gegevensstandaard AFD 1.0

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1663245552349-20220915%20Bouwstenen%20gegevensstandaard%20AFD%201.0p.png) **Entiteiten/attributen**

Het AFD bestaat uit een verzameling entiteiten. In een entiteit worden bij elkaar horende gegevenselementen (attributen) vastgelegd. Een entiteit beschrijft op die manier een object of zaak uit de werkelijkheid. Voorbeelden: Verzekeringnemer (VP), Verzekerde, Motorrijtuig. Een attribuut beschrijft één eigenschap van één entiteit, bijvoorbeeld geboortedatum Verzekeringnemer (VP). Aan iedere entiteit en aan ieder attribuut wordt een uniek label toegekend van respectievelijk 2 en maximaal 7 posities. Deze labels worden in het berichtenverkeer gebruikt om de gegevens te duiden. Door een label te interpreteren is het bijbehorende gegeven (bijvoorbeeld een verzekerd bedrag) automatisch te verwerken. De labels worden in XML-berichten als XML tags toegepast. 

<PP>
            <PP_NUMMER>123455667</PP_NUMMER>
</PP> 
Het bovenstaande voorbeeld geeft weer hoe de AFD-entiteit Polis (PP) en het AFD-attribuut Contractnummer (NUMMER) in een XML-bericht worden opgenomen. 

De labels worden in INSLBW berichten gebruikt voor het communiceren van de gegevens van prolongaties (PPR-berichten) en mutatiebevestigingen (PMB-berichten).

Domein

Een domein beschrijft een klasse waarden met een gemeenschappelijk toepassingsgebied en gelijke structuur. Een voorbeeld is het domein datum dat gekoppeld is aan alle ‘datum attributen’ in het AFD. Aan een domein kan een codelijst met codewaarden gekoppeld zijn.
Een domein heeft een naam, een formaat en een beschrijving. Een domein kan verwijzen naar meerdere attributen uit verschillende entiteiten.

Codelijst 

Een codelijst kan een codetabel zijn die we onderhouden bij SIVI, maar ook andere partijen kunnen codelijsten onderhouden. 

Voorbeelden

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1663246475586-20220915%20bericht%20AFD%201.0%201.pptx.png)Hierboven een klein gedeelte van een aantal bouwstenen van het AFD:

- De entiteit Bericht Algemeen (AL) bevat een aantal attributen. Aan het attribuut ‘Berichtfunctie, code’ (FUNCTIE) is een codelijst gekoppeld. 

- De entiteit Polis/Onderdeel (PP) bevat een aantal attributen. Aan het attribuut ‘Sectorcode’ (SECTOR) is een codelijst gekoppeld.

Onderstaand een gedeelte van AFD-bericht. Duidelijk herkenbaar is hoe tussen de labels uit AFD-waarden zijn opgenomen. De UN-labels zijn geen onderdeel van het AFD.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1663246714751-20220915%20bericht%20AFD%201.0%202.pptx.png)

---

[← Terug naar home]({{ site.baseurl }}/)
