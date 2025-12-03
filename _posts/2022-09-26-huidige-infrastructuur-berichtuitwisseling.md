---
layout: post
title: "Huidige infrastructuur berichtuitwisseling"
date: 2022-09-26
categories: ["Oplossingen ► B2B (keten)"]
question_id: 1533830
---

# Huidige infrastructuur berichtuitwisseling

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1664186960212-1664186960212.png)

In de figuur hierboven een overzicht op hoofdlijnen van variatie in de huidige NL-infrastructuur voor berichtenuitwisseling binnen de financiële dienstverlening rond verzekeringen. De figuur gaat in op de setting rond verzekeraars, serviceproviders en adviseurs. Merk echter op dat ook andere actoren in de keten berichtenuitwisseling gebruiken. Er is binnen de varianten in de figuur een grotere diversiteit rond zowel ontvangers als verzenders met partijen als CIS, Market Scan, Schadeherstellers, Infofolio, Adviessoftwareleveranciers, etc. Voor een deel gaan deze berichtenstromen ook via Solera en Aplaza. Onderstaand een toelichting bij de nummers in de figuur:

- Berichtenuitwisseling via e-mail is nog steeds een belangrijkrijke route. Vaak meer voor ad hoc uitwisseling, echter voor met name kleinere aanbieders ook een structurele route voor bijvoorbeeld prolongatie borderellen.

- Berichtenuitwisseling via een SFTP-locatie (file transfer) wordt nog steeds breed gebruikt om met name grote of veel bestanden uit te wisselen. Gebeurt dit structureel dan krijgen partijen een vaste locatie om bestanden op te halen of neer te zetten.

- Vanwege de veiligheidsrisico’s van (1) of (2) en/of van wege de omvang/diversiteit van het aantal bestanden richten partijen op hun extranet een loket in om bestanden op te halen of aan te leveren. Daarnaast ziet een groep aanbieders dit als een alternatief voor het verzenden van papieren post. Deze vorm van distributie kan t.o.v. papieren aanlevering of GRS Documentberichten tot veel extra arbeid bij ontvangers leiden; dit is onderwerp van een nu lopend SIVI-onderzoek rond zelf incasserende adviseurs.

- Er zijn meerdere leveranciers voor postvak omgevingen ten behoeve van het GRS Protocol: Solera (ex Colimbra), ANVA en Keylane. Daarnaast zijn er een aantal aanbieders die zelf deze software hebben ontwikkeld.

- Een beperkt aantal leveranciers van administratiesoftware leest op basis van het GRS Protocol zelf de postvakken uit van aanbieders van documenten (bijv. Online, Invice).

- Er zijn ongeveer 150 aanbieders die ADN berichten versturen via Solera. Een beperkt aantal (onbekend) aanbieders verstuurt ook GRS-documentberichten via Solera. Ongeveer 50 aanbieders versturen GRS-documentberichten via Aplaza. Ruim 20 van deze aanbieders versturen ook ADN-berichten via het GRS Protocol. Soms alleen via Aplaza en anders via Aplaza voor ontvangers waar dat kan en voor de resterende ontvangers via Solera.

- Aplaza geeft een andere invulling aan de uitvoering van het GRS Protocol. Bij het GRS Protocol is het uitgangspunt dat systemen van gebruikers van postvakken direct koppelen met de postvakken die ze gebruiken. Aplaza neemt de noodzaak voor het faciliteren van een reeks van koppelingen weg door de GRS-postvak architectuur te transformeren naar een variant van een postbus architectuur. 
In de Aplaza setting hebben verzenders een overeenkomst voor de postvakkensoftware (of verzenders ontwikkelen dit zelf) en voor de routering van de GRS-berichten. Dit kan beide bij Aplaza of gesplitst zijn over een leverancier voor de postvakkensoftware en Aplaza voor de routering. Voor de ontvangers verzorgt Aplaza de routering van de GRS-berichten.

- De Solera postbus volgt de postbus structuur zoals eerder beschreven.

- Er zijn 5 leveranciers van administratiesoftware of CRM-software die alleen berichten ontvangen vanuit de Solera postbus. Totaal 10 leveranciers ontvangen berichten via Solera en Aplaza. Er is 1 leverancier die alleen berichten via Aplaza ontvangt.

---

[← Terug naar home]({{ site.baseurl }}/)
