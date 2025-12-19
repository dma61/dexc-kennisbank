---
layout: post
title: "Personal Datamanagement"
date: 2022-09-21
categories: ["Bouwstenen/Principes"]
question_id: 1525680
---

**PDM**

Persoonlijk data management, ofwel PDM, betekent dat mensen (persoonlijke) gegevens kunnen gebruiken om hun leven, werk of bedrijf te organiseren, terwijl belangrijke waarden als veiligheid en privacy geborgd zijn. Persoonlijk data management gaat over toegang, corrigeren en delen van persoonlijke data, maar ook inzicht hebben in wie deze persoonlijke gegevens gebruikt, onder controle van het individu.

**De basis van PDM omvat vier rollen **

- De persoon is een individu die zeggenschap heeft over het delen van zijn over haar data, voor eigen doeleinden, en heeft een relatie met de andere drie rollen.

- Een data aanbieder verzamelt en verwerkt persoonlijke data die de andere rollen (inclusief de persoon) willen inzien of gebruiken.

- Een data afnemer kan geautoriseerd zijn om persoonlijke data van een of meerdere aanbieders te gebruiken.

- Een operator/regietoepassing maakt het mogelijk voor het individu om veilig persoonlijke data in te zien, te gebruiken en te managen. Daarnaast maakt de operator het mogelijk om de uitwisseling van persoonlijke data met en tussen data aanbieders en afnemers te controleren. Buiten deze rollen kan er nog een rol of entiteit zijn die het beheer van de afspraken en toezicht op het systeem regelt (governance). De operator acteert als ‘broker’ van gegevens: de operator maakt persoonlijke gegevens inzichtelijk, faciliteert gegevensuitwisseling en voorziet in consentmanagement. Functioneel kan een operator verschillende vormen aannemen: niet elke operator voorziet bijvoorbeeld in het wijzigen van consent. Sommige operators fungeren als ‘datakluis’ terwijl andere puur gegevens uitwisselen, maar niet zelf bewaren. Dit maakt het lastig om te bepalen wat we kunnen verwachten van een operator.

Organisaties kunnen meerdere van de hierboven beschreven rollen op zich nemen.
Bijvoorbeeld: IRMA is een applicatie die gewaarmerkte attributen van personen verzamelt bij data aanbieders, zoals geboortedatum en adres bij een gemeente, onder toestemming van de burger. Op dat moment is IRMA een operator. Zodra IRMA een ‘afgeleid attribuut’ maakt met de geboortedatum zoals ‘deze persoon is 18+’ en dit attribuut doorgeeft, functioneert IRMA zelf als een data aanbieder.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1663787871987-1663787871987.png)

**Functionele componenten PDM**![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1663787891460-1663787891460.png)[Belangrijke functionele componenten](https://rog.pleio.nl/file/download/8f483e75-ae39-47df-a30d-e74dcd58376a/158565514620200122-%20pdm%20landschap%20v1.4a%20def%20publiek.pdf) zijn volgens InnoValor:

- Identity & access management
Functionaliteit ten behoeve van authenticatie en autorisatie van de persoon.

- Consent management
Het managen van (tijdelijke) toestemming voor het delen van gegevens tussen data aanbieders en data afnemers.

- Datadiensten
Een PDM-Dienst kan zelf waarde toevoegen door ondertekening, analyseren, filteren en vertalen van de gegevens. Dit kan ook gaan om het in rekening brengen van kosten voor het gebruik van data.

- Servicemanagement 
Maakt het koppelen van data afnemers en data aanbieders mogelijk. Data kan op meerdere plekken beschikbaar zijn en diverse afnemers kunnen deze data gebruiken. In een omgeving met meerdere operators is het een belangrijke beslissing om te bepalen of de operators een gedeeld diensten register gebruiken (mogelijk gedistribueerd) of dat elke operator zijn dienstenregistratie zelf onderhoudt.

- Opslag 
De dienst kan zelf zorgen voor opslag van data ten behoeve van (her-)gebruik. Denk aan de opslag van medische gegevens of het bewaren van gewaarmerkte data. Let op: veel diensten slaan ten behoeve van de gegevensuitwisseling data kortstondig op. Dat valt hier niet onder opslag, maar kan wel leiden tot een rol als verwerker onder de AVG.

- Logging 
Het bijhouden van gegevensuitwisseling die heeft plaatsgevonden, waardoor het zichtbaar is wie wanneer tot wat toegang had. Experts pleiten voor decentrale oplossingen, zodat geen centrale monitoring mogelijk is (= privacy onvriendelijk).

- Gegevensuitwisseling 
Interface die data uitwisseling mogelijk maakt op een veilige en gestandaardiseerde manier, tussen de persoon, afnemer, aanbieder en operator. Dit kan middels gestructureerde data, ondersteunende automatische transactie of ongestructureerde data (zoals een pdf). Informatie kan zowel brondata zijn als afgeleide attributen. 
Brondata zijn gegevens die we rechtstreeks ontsluiten uit de plek waar de originele informatie is opgeslagen, zonder dat we deze informatie verder bewerken. 

- Afgeleide attributen zijn attributen waarvan we de waarde berekenen op basis van waarden van gerelateerde attributen.

- Governance – het besturen van het gebruik en de ontwikkeling van de onderliggende principes van het ecosysteem, inclusief management van het businessmodel is buiten de figuur gehouden.

---

[← Terug naar home]({{ site.baseurl }}/)
