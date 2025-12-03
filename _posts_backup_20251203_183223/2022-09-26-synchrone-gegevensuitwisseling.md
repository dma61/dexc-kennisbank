---
layout: post
title: "Synchrone gegevensuitwisseling"
date: 2022-09-26
categories: ["Bouwstenen/Principes"]
question_id: 1533650
---

# Synchrone gegevensuitwisseling

Processen die directe response op de vraag vereisen of die plaatsvinden tussen mens en machine zijn altijd synchroon. De brede inzet van portalen is hier de invulling van. Verder zijn er synchrone machine to machine processen die een directe response vereisen, denk aan services voor pensioenberekeningen ten behoeve van deelnemers. In de sector worden die bij voorkeur ondersteund met gestandaardiseerde webservice protocollen om branchebreed op dezelfde manier met elkaar te communiceren en tegelijkertijd de implementatielast te beperken. 

### Screen scraping
Schermschrapen is het verzamelen van schermgegevens van een applicatie of gegevens getoond in een webbrowser zodat een andere applicatie deze kan weergeven/verwerken. Bij screen scraping is geen sprake van waarmerking vanuit de data aanbieder, bij correcte scraping is de kwaliteit van de data gelijk aan die in de applicatie.

Enkele leveranciers van regie op gegevensdiensten verzamelen op dit moment al gegevens voor hun klanten bij (overheids-)bronnen, met behulp van zogenaamde [scraping-technologie](https://vng.nl/media/46468). Omdat in dit geval geen afspraken bestaan tussen de gegevenshouder en de leveranciers van regie op gegevensdiensten, is dit een suboptimale oplossing voor alle partijen. Met name voor de burger geldt er geen borging is dat alleen de benodigde informatie wordt opgehaald, of dat de gegevens niet worden aangepast of bewerkt. Het vergaren van gegevens middels scraping, vindt vaak plaats wanneer de gegevenshouder deze niet op een gestructureerde manier aanbiedt, zoals met een API.

### Extranet
Koppelingen waarbij de gebruiker rechtstreeks via een browser op het extranet van de verzekeringsmaatschappij werkt en waarbij de dialoog en navigatie door de (web)applicatie van de verzekeraar wordt verzorgd.

 Kenmerken van een extranet zijn de look en feel die bepaald worden door de verzekeraar en dat wel of geen koppeling is met de software die geïnstalleerd is in de omgeving van de financiële adviseur. De backoffice systemen van de maatschappij zijn veelal wel gekoppeld. 

### API
**Inleiding**

[API](https://dev.to/decipherzonesoft/types-of-apis-what-are-apis-different-types-of-apis-3mjm) is een afkorting voor Application Programming Interface. Via een API komt een reeks functies en procedures ter beschikking waarmee toegang mogelijk is tot de functies of gegevens van andere applicaties, services of een besturingssysteem.

#### **SOAP (Simple Object Access Protocol)**
[SOAP](https://www.w3.org/TR/soap/) is een gestandaardiseerde specificatie van het World Wide Web Consortium en die wordt gebruikt voor het uitwisselen van gestructureerde informatie in de vorm van goed gedefinieerde, beveiligde berichten. SOAP was lange tijd het favoriete berichtenprotocol dat bijna elke API gebruikte.

 SOAP kan werken met elk applicatie-laag protocol, zoals HTTP, SMTP, TCP of UDP. Het retourneert gegevens naar de ontvanger in XML-formaat. Beveiliging, autorisatie en foutafhandeling zijn ingebouwd in het protocol. SOAP volgt een formele en gestandaardiseerde aanpak die specificeert hoe we XML-bestanden coderen die door de API’s retourneren. Een SOAP-bericht is in feite een gewoon XML-bestand dat uit de volgende onderdelen bestaat:

- Envelop (vereist) – Dit zijn de begin- en eindtags van het bericht.

- Header (optioneel) – Het bevat de optionele attributen van het bericht. Hiermee kunt u een SOAP-bericht modulair en decentraal uitbreiden.

- Body (vereist) – Het bevat de XML-gegevens die de server naar de ontvanger verzendt.

- Fout (optioneel) - Het bevat informatie over fouten die optreden tijdens het verwerken van het bericht.

Aangezien SOAP berichten alleen als XML-bestanden kan overbrengen, zal een SOAP-API minder presteren, aangezien XML een uitgebreid formaat is in vergelijking met JSON. API-aanroepen naar een server hebben meer bandbreedte nodig en het zal meer tijd kosten om het verzoek te verwerken en het antwoord terug naar de client te sturen. SOAP heeft ook een hogere leercurve, is moeilijker te coderen en kan niet worden getest in de webbrowser (in tegenstelling tot REST). 

#### **REST (Representational State Transfer)**
[REST](https://restfulapi.net/) is gemaakt om de problemen van SOAP aan te pakken. Daarom heeft het een flexibelere architectuur. Het bestaat uit slechts losse richtlijnen en laat ontwikkelaars de aanbevelingen op hun eigen manier implementeren. Het staat verschillende berichtformaten toe, zoals HTML, JSON, XML en platte tekst, terwijl SOAP alleen XML toestaat. REST is ook een lichtere architectuur, dus RESTful-webservices presteren beter. Daarom is het populair geworden in het mobiele tijdperk waar zelfs een paar seconden er veel toe doen.

Tegenwoordig is REST de meest populaire keuze van ontwikkelaars om openbare API's te bouwen. Je kunt overal op internet veel voorbeelden vinden, vooral omdat alle grote sociale-mediasites REST API's bieden, zodat ontwikkelaars hun apps naadloos kunnen integreren met het platform. Deze openbare API's worden ook geleverd met gedetailleerde documentatie

De REST-architectuur stelt API-providers in staat om gegevens in meerdere formaten te leveren, zoals platte tekst, HTML, XML, YAML en JSON, wat een van de meest geliefde functies is. Dankzij de toenemende populariteit van REST heeft het lichtgewicht en voor mensen leesbare [JSON-formaat](https://www.json.org/json-en.html) ook snel aan populariteit gewonnen, omdat het super geschikt is voor snelle gegevensuitwisseling. JSON staat voor JavaScript Object Notation. Het is een gemakkelijk te ontleden en lichtgewicht formaat voor gegevensuitwisseling. Ondanks zijn naam is JSON volledig taalonafhankelijk, dus het kan met elke programmeertaal worden gebruikt, niet alleen met JavaScript. 

**Vergelijking SOAP en REST**

Hier is veel materiaal beschikbaar, zie [voorbeeld-1](https://www.soapui.org/learn/api/soap-vs-rest-api/) en [voorbeeld-2](https://www.researchgate.net/publication/323456206_Web_Services_A_Comparison_of_Soap_and_Rest_Services).

#### **Raamwerken/Standaarden**

- SIVI ontwikkelt het SIVI AFS API-raamwerk.

- De [Nederlandse API-strategie](https://geonovum.github.io/KP-APIs/API-strategie-algemeen/#architectuur) voorziet in overheid breed ontwerp en standaarden.

De Open Insurance Think Tank (OPIN) kondigt in mei 2022 de publicatie aan van de eerste versie van de open insurance API-specificatie. Het is gebaseerd op de Swagger 2.0 en is bedoeld om een standaardformaat te bieden voor het specificeren RESTful API’s in de verzekeringssector. De specificatie is toegankelijk via [GitHub](https://github.com/The-Open-Insurance-Initiative/API-spec?mc_cid=42c51fc99e&mc_eid=5680ca7cf7).

---

[← Terug naar home]({{ site.baseurl }}/)
