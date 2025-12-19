---
layout: post
title: "Formaten voor gegevensuitwisseling"
date: 2022-09-26
categories: ["Bouwstenen/Principes"]
question_id: 1533661
---

De meest algemeen aanvaarde formaten voor gegevensuitwisseling zijn: XML, CSV, JSON. 

Deze formaten bespreken we hierna. Daarna gaan kort in op EDIFACT. Dit formaat is nog steeds in gebruik voor het uitwisselen van ADN-berichten. 

**XML**

Extensible Markup Language ( XML ) is een opmaaktaal die een reeks regels definieert voor het coderen van documenten in een formaat dat zowel door mensen leesbaar als door machines leesbaar is. De XML 1.0-specificatie van het World Wide Web Consortium uit 1998 en verschillende andere gerelateerde specificaties - allemaal vrije open standaarden - definiëren XML.

Een XML-schema is een beschrijving van een type XML - document, doorgaans uitgedrukt in termen van beperkingen op de structuur en inhoud van documenten van dat type, bovenop de syntactische basisbeperkingen die door XML zelf worden opgelegd. Deze beperkingen worden over het algemeen uitgedrukt met behulp van een combinatie van grammaticale regels die de volgorde van elementen bepalen, Booleaanse predicaten waaraan de inhoud moet voldoen, gegevenstypen die de inhoud van elementen en attributen bepalen, en meer gespecialiseerde regels.

De XML-specificaties zijn [hier](https://www.w3.org/TR/REC-xml/) zijn te raadplegen.

**CSV**

Een bestand met door komma's gescheiden waarden (CSV ) is een tekstbestand met scheidingstekens dat een komma gebruikt om waarden te scheiden. Elke regel van het bestand is een gegevensrecord . Elk record bestaat uit een of meer velden , gescheiden door komma's. Het gebruik van de komma als veldscheidingsteken is de bron van de naam voor dit bestandsformaat . Een CSV-bestand slaat meestal tabelgegevens (getallen en tekst) op in platte tekst , in welk geval elke regel hetzelfde aantal velden zal hebben.

Het CSV-bestandsformaat is niet volledig gestandaardiseerd. Het basisidee van het scheiden van velden met een komma is duidelijk, maar dat idee wordt ingewikkeld wanneer de veldgegevens ook komma's of zelfs ingebedde regeleinden kunnen bevatten . 

**JSON**

JavaScript Object Notation ( JSON) is een open-standaard bestandsformaat of data-uitwisselingsformaat. JSON is een taalonafhankelijk gegevensformaat. Het is afgeleid van JavaScript.

Meer details over de JSON-specificatie zijn [hier](https://www.json.org/json-en.html) te vinden. 

**EDIFACT**

EDIFACT is een afkorting van Electronic Data Interchange For Administration, Commerce and Transport. EDIFACT is een computertaal (syntax) om gegevens op een gestructureerde manier elektronisch te communiceren. EDIFACT wordt onderhouden door de United Nations (UN).

EDIFACT maakt gebruik van “segmenten”. Alle voor gedefinieerde en wereldwijd gestandaardiseerde EDIFACT segmenten bevinden zich in een bibliotheek die door de UN wordt onderhouden en uitgebreid.

Binnen de SIVI-standaarden wordt deels gebruik gemaakt van de door de UN gestandaardiseerde segmenten (bv UNH, UNB, DTM, CIF, NAD) en deels gebruik gemaakt van eigen gestandaardiseerde segmenten (bv ENT, LBW). Deze laatste worden alleen gebruikt in het EDIFACT bericht Label/Waardebericht (INSLBW). INSLBW is de drager van prolongaties en mutatiebevestigingen.

---

[← Terug naar home]({{ site.baseurl }}/)
