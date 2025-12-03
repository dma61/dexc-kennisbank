---
layout: post
title: "AFD Converter"
date: 2023-03-23
categories: ["Oplossingen ► B2B (keten)"]
question_id: 1869808
---

# AFD Converter

### Inleiding
Wie in de verzekeringswereld kijkt naar de keten van intermediairs, serviceproviders en aanbieders, ziet dat de keten een enorme sprong voorwaarts heeft gemaakt in de kwaliteit en de snelheid van de processen door de het gebruik van de **SIVI standaard AFD 1.0**. In 2020 heeft **SIVI de nieuwe SIVI All Finance Standaard (SIVI AFS)** geïntroduceerd. Als onderdeel van SIVI AFS is **AFD 2.0** geïntroduceerd als opvolger van AFD 1.0. Een nieuwe versie brengt altijd voordelen met zich mee, of het nu gaat om functionaliteit dan wel om technische verbeteringen. Maar een migratie van de oude naar de nieuwe wereld vraagt ook altijd een flinke inspanning van een organisatie. Zeker als het om specialistisch werk gaat is het goed om de juiste spelers bij het traject te betrekken. 
 
TJIP heeft vanaf het begin direct het berichtenverkeer met AFD 1.0 toegevoegd aan het verzekeringsplatform **MeetingpointAdvies. ** Inmiddels is er binnen de **TJIP Insurance Gateway** een eigen AFD-conversietool gebouwd (Converter) om het gebruik van AFD 2.0 in een omgeving waar ook nog AFD 1.0 wordt gebruikt volledig te ondersteunen, of juist andersom dat AFD 2.0 berichten voorlopig worden teruggezet naar AFD 1.0. 
De TJIP Insurance Gateway is een universeel schakelpunt tussen enerzijds aanbieders van webservices (zoals verzekeringsmaatschappijen en volmachthouders) en anderzijds gebruikers van die webservices (zoals assurantietussenpersonen en vergelijkingssites). Binnen dit platorm vertaalt de AFD Converter berichten tussen AFD 1.0 en AFD 2.0, maar ook naar andere industriestandaards zoals ACORD of bedrijfseigen berichtformaten.

Natuurlijk biedt SIVI de nodige ondersteuning met documentatie en tools om de implementatie van AFD zo makkelijk mogelijk te maken. Maar de praktijk blijkt toch vaak weerbarstiger. Zo wordt bij AFD 2.0 gebruik gemaakt van volledig uitgeschreven, Engelstalige veldnamen. Iets waar bij AFD 1.0 nog geen sprake van was. Daarnaast zijn in AFD 2.0 datatypes van velden aangepast, zo kan een veld wat een string in AFD 1.0 was, in AFD 2.0 een datum zijn geworden, etc. De verschillen tussen AFD 1.0 en AFD 2.0 zijn goed gedocumenteerd, maar het wordt lastiger als het doelsysteem (mid- of backoffice) een eigen “mapping taal” kent.

Los van de vraag op basis van welke uitgangspunten het doelsysteem (mid- en backoffice) data vastlegt, is het goed aandacht te besteden aan de standaardisatie. Het waar mogelijk toewerken naar de nieuwe SIVI standaard AFD 2.0 is een logische volgende stap. Voor de financiële dienstverlening is SIVI niet voor niets al jaren het kennis- en standaardisatie-instituut. Met alle nieuwe technieken die er tegenwoordig zijn, was het logisch dat er een opvolger zou komen. SIVI noemt dit de SIVI All Finance Standaard (SIVI AFS). Alle gegevens-gerelateerde afspraken zijn gedocumenteerd in de All Finance Datacatalogus (AFD) 2.0.

De TJIP AFD Converter is generiek opgezet en kan in principe gebruikt worden om AFD-berichten van alle producten te converteren. De AFD Converter ondersteunt nu alleen berichten voor een losse polis, maar is uit te breiden naar alle soorten AFD 2.0 berichten (zoals pakketpolissen en schadeclaims). 

### Interne werking van de AFD Converter
Voorbeeld: bij een conversie van AFD 1.0 naar AFD 2.0 doorloopt de AFD Converter een aantal stappen: 

- Het AFD 1.0 XML bericht wordt ingelezen in een interne datastructuur. Deze is zo ontworpen zodat de conversie er gemakkelijk in uitgevoerd kan worden. Attribuutwaarden worden ingelezen en vertaald naar interne datatypes. Attribuutwaarden van codelijsten worden 1 op 1 doorgezet, omdat codelijsten hetzelfde zijn gebleven. 

- De AFD 1.0 attribuut- en entiteitnamen worden vertaald naar AFD 2.0. De bron voor deze vertaling is het Mapping.json document van SIVI. Hierin staan alle entiteiten en attributen met zowel de AFD 1.0 als de AFD 2.0 naam genoemd.  

- De mapping in (2) is op een paar uitzonderingen na één op één. Bijvoorbeeld de BY, DS, NI, VA en VI entiteit mappen allemaal naar *document*, XA- en UR-mappen allebei naar *address*. Bij het mappen van AFD 2.0 naar AFD 1.0 is hier meer complexe logica voor nodig. In alle producten die gebruik maken van de Insurance Gateway worden van bovenstaande entiteiten alleen BY en XA gebruikt. Hier is de pragmatische keuze gemaakt om deze mappings hardcoded op te nemen in de AFD Converter. 

- AFD 2.0 heeft een andere structuur dan AFD 1.0. 
De AL entiteit wordt opgesplits in een commonFunctional en een commonTechnical entiteit. 

- De bijlagen in AL/BY worden verplaatst naar documents. 

- De intermediair in AL/TP wordt verplaatst naar /policy/party 

- Premie attributen staan in het AFD 1.0 direct in de entiteit waar ze betrekking op hebben (zoals een polis of een dekking). Binnen AFD 2.0 kan men ook kiezen deze premie attributen onder te brengen in de subentiteit premiumDetails. Afhankelijk van de structuur van het AFD 2.0 bericht moet we wel of niet attributen groeperen in premiumDetails. Deze stap is dus productspecifiek en kan voor producten verschillend ingeregeld moeten worden. 

- De interne datastructuur wordt omgezet naar een AFD 2.0 JSON structuur. Hierbij worden gelijke entiteiten (zoals de party entiteit) gegroepeerd in 1 lijst en attribuutwaarden waar nodig omgezet naar de JSON-representatie.

---

[← Terug naar home]({{ site.baseurl }}/)
