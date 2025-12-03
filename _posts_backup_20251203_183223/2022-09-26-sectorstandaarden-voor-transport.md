---
layout: post
title: "Sectorstandaarden voor transport"
date: 2022-09-26
categories: ["Bouwstenen/Principes"]
question_id: 1533669
---

# Sectorstandaarden voor transport

#### ADN-berichtenverkeer
Dit - Store & Forward via Elektronisch Postbussen - systeem is een koppelingsvorm waarbij elektronische berichten worden verstuurd en/of opgehaald. Het ADN berichtenverkeer maakt van oudsher gebruik van een postbussensysteem. Berichten worden in het postvak van de ontvanger geplaatst. De ontvanger kan dan – op een later moment - de gegevens ophalen en verwerken. Dit mechanisme staat bekend als Store & Forward.

#### GIM Resultaten Service Protocol (GRS Protocol)
Het GRS Protocol is geschikt voor het uitwisselen van digitale output van verzekeraar/serviceprovider naar assurantiesoftware van intermediair.

GRS biedt het intermediair de mogelijkheid om bestanden bij een verzekeraar/serviceprovider op te halen. Deze bestanden kunnen prolongaties, offertes en dergelijke bevatten. De resultaten worden door de verzekeraar/serviceprovider beschikbaar gesteld. Dit kan door de verzekeraar/serviceprovider zelf worden gedaan of door een derde partij die GRS ondersteunt.

GRS kent meerdere functies; de verzekeraar/serviceprovider is vrij in de keuze welke functies hij wil ondersteunen.

Zie verder: [**https://www.sivi.org/grs-protocol/**](https://www.sivi.org/grs-protocol/)

**Digitale documenten verwerken**

Het proces van ophalen en verwerken bij ontvangers van digitale documenten met het [GRS Protocol](https://www.sivi.org/wp-content/uploads/2021/02/Actie-digitale-aanlevering-van-documenten-v1.1.pdf) bestaat uit 3 stappen:

- De ontvanger kan op basis van het GRS Protocol direct of via een leverancier GRS-berichten ophalen bij een verzender. Afhankelijk van hoe de ontvanger zijn werkprocessen inricht en afhankelijk van welke verzenders de ontvanger de GRS-berichten afneemt kan dit in een frequentie van éénmaal per dag tot meerdere malen per uur.

- De meta-data in het GRS-bericht maakt het mogelijk de documenten in een GRS-bericht te koppelen aan het juiste klantdossier bij de ontvanger.

- De ontvanger verwerkt op basis van de meta-data de documenten automatisch in een ingerichte workflow binnen de administratiesoftware of verwerkt deze handmatig als dit niet kan. 

De achilleshiel in dit proces is de koppeling van het digitale document aan het juiste klantdossier bij de ontvanger. Als dit volledig automatisch kan, dan zijn de belangrijkste baten: 

- Besparing in behandel- en doorlooptijden. 

- Werkverdeling: documenten komen direct op de juiste plek in de organisatie. 

- Kleinere kans dat documenten zoek raken.

- Automatische behandeling vanuit de werkvoorraad. 

- Verhoging van de service richting de eindklant. 

#### SIVI Koppelingsprotocol (SKP)
Het [SIVI Koppelingsprotocol](https://www.sivi.org/standaarden/sivi-koppelingsprotocol-skp/) is de doorontwikkeling van de GIM-protocollen die nog stammen uit 2006. Het nieuwe SIVI Koppelingsprotocol regelt en vergemakkelijkt de uitwisseling van gegevens en documenten tussen ketenpartijen in de verzekeringsindustrie. Daarbij gaat het niet alleen om koppelingen tussen verzekeraars, serviceproviders en intermediairs, maar bijvoorbeeld ook met vergelijkingssoftware, schadeherstellers en expertisediensten.

SKP is gericht op het doorgeven van de output van een toepassing met als doel het informeren over een status (ruit van wagen is hersteld) en/of de vastlegging in een dossier (als aangemaakt advies of opgemaakte offerte). Het toepassingsgebied van het SIVI Koppelingsprotocol is alle toepassingen in de keten. Het doel is zowel verticaal (tussen ketenpartijen) als horizontaal (tussen toepassingen van ketenpartij) ketenoptimalisatie te ondersteunen.

Het gebruik van het SIVI Koppelingsprotocol levert een bijdrage op meerdere punten:

- Klantdossier (minder arbeid bij inboeken stukken en data);

- Zorgplicht (kwaliteit klantdossier);

- Verzenden (veilig transport van data);

- Voor de gebruiker van SKP-koppelingen zijn de voordelen (1) en (2) goed te vertalen in euro's. Voordeel (3) is meer kwalitatief. Voor de aanbieder van SKP-koppelingen zijn de voordelen meer kwalitatief: het mogelijk maken van kostenbesparingen voor een ketenpartner (1) en het leveren van een bijdrage aan de kwaliteit (2) en veiligheid (3) van een gezamenlijk ketenproces.

Het SIVI-Koppelingsprotocol kent drie koppelingsvarianten:

- Basis: bijvoorbeeld koppeling vanuit extranet met alleen PDF-document retour naar assurantiesoftware.

- Uitgebreid: bijvoorbeeld vanuit extranet met XML-bericht met data (en optioneel PDF-document) retour naar assurantiesoftware.

- Compleet: bijvoorbeeld vanuit assurantiesoftware naar extranet waarbij initiële data vanuit de assurantiesoftware wordt doorgegeven aan het extranet en waarbij een XML met data (en optioneel PDF-document) retour gaat naar de assurantiesoftware.

Overigens hoeft het niet altijd om een PDF-document te gaan, het kan bijvoorbeeld evengoed een Word-, Excel- of JPG-formaat zijn. In de praktijk zal meestal het PDF-formaat gebruikt worden.

 

[Tabel - zie origineel]De variant ‘SKP-*Basis*’ is geheel nieuw. Het uitgangspunt is dat met beperkte technische complexiteit en zeer geringe inspanning altijd een koppeling mogelijk is. Dit creëert ruimte voor een nieuwe toonzetting rond het ondersteunen van koppelingen binnen de keten. De minimale complexiteit en kosten van de variant ‘SKP-Basis’ maken dat dit niveau van koppelen als de norm gezien kan worden. Het ontbreken van een koppeling op niveau ‘SKP-Basis’ zal uiteindelijk als ondermijning van de kostenstructuur binnen de keten gezien worden.

#### SIVI All Finance API-raamwerk
Binnen het digitale ecosysteem speelt het gebruik van webservices een essentiële rol, of het nu gaat om gegevensuitwisseling, het uitvoeren van functies of het volgen van een workflow binnen de keten. Het kenmerk van een webservice is dat twee machines direct met elkaar communiceren (synchrone communicatie) om een service (functie) uit te voeren. Bijvoorbeeld het uitvoeren van een tariefberekening of het doorgeven van een mutatie. De communicatie vindt inmiddels vrijwel altijd plaats via een (beveiligde) internetverbinding. Het aan derden ter beschikking stellen van een of meer webservices heet een API (Application Programming Interface). Voor veel organisaties zijn API's essentieel voor digitaal zakendoen. Ze maken het mogelijk om transacties aan te bieden (zoals tarief, offerte en aanvraag) en inhoud te publiceren (zoals objectgegevens en weergegevens). 

Het [SIVI All Finance API-raamwerk](https://www.manula.com/manuals/sivi/sivi-all-finance-standard/1/en/topic/introduction-all-finance-api-framework):

- geeft inzicht in welke functies/diensten op dit moment zijn gedefinieerd in de financiële dienstverlening;

- zorgt waar mogelijk voor eenduidige processen tussen partijen;

- zorgt voor een goede toegankelijkheid/inpasbaarheid van online diensten binnen de distributieketen;

- maakt co-creatie mogelijk waarbij derden applicaties kunnen ontwikkelen.

#### HDN-API
In haar platform maakt HDN gebruik van een REST architectuurconcept en RESTful API’s.

#### NextGenPSD2 Raamwerk
Het [NextGenPSD2 Framework](https://www.berlin-group.org/nextgenpsd2-downloads) biedt een open, geharmoniseerde en interoperabele set Application Programming Interfaces (API's) als de veiligste en meest efficiënte manier om gegevens veilig te verstrekken. 

Kenmerken zijn onder meer:

- Moderne "RESTful" API-set die HTTP/1.1 gebruikt met TLS 1.2 (of hoger) als transportprotocol

- TPP-identificatie door ETSI-gedefinieerde eIDAS-certificaten: QWACS verplicht gesteld (eenvoudige maatregel ter bescherming, bijv. Tegen DDOS-aanvallen), QSEALS optioneel voor banken (TPP volgt instructies van bank).

- Volledige ondersteuning voor meerdere valuta's van accounts.

- Vier architectuurmodellen voor Strong Customer Authentication (SCA): omleiding, OAuth2, ontkoppeld en ingebed, met invloed van de TPP op omleidingsvoorkeur.

- Multilevel SCA-benadering voor bedrijven, bijv. ter ondersteuning van een 4-ogen-principe

- Toegewijde toestemmings-API die toestemmingsafhandeling scheidt van accounttoegang, in overeenstemming met zowel PSD2- als AVG-vereisten.

- Optionele sessieondersteuning (reeks opeenvolgend uitgevoerde transacties), onder voorbehoud van de juiste toestemming van de klant.

- Datastructuren ofwel als JSON of XML.

---

[← Terug naar home]({{ site.baseurl }}/)
