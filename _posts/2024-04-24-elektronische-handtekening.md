---
layout: post
title: "Elektronische Handtekening"
date: 2024-04-24
categories: ["Bouwstenen/Principes"]
question_id: 2529501
---

# Inleiding
Elektronische handtekeningen worden vaak geïntegreerd in elektronische gegevensuitwisselingssystemen om de juridische geldigheid en beveiliging van digitale documenten te waarborgen. Door elektronische handtekeningen te gebruiken bij het elektronisch uitwisselen van gegevens, kunnen partijen vertrouwen hebben in de identiteit van de afzender en de integriteit van de ontvangen informatie. Elektronische handtekeningen vormen dus en aanvullende laag van beveiliging en vertrouwen in het proces van elektronische gegevensuitwisseling, waardoor organisaties efficiënter kunnen werken in een digitale omgeving.

We volgen de definitie uit de [Handreiking Elektronische handtekening](https://vng.nl/sites/default/files/2021-02/electronische-handtekening_20210127.pdf), VNG, Den Haag2021:

‘’Een elektronische handtekening is een verzameling gegevens in elektronische vorm, die gehecht zijn aan of logisch verbonden zijn met andere gegevens in elektronische vorm en die door de ondertekenaar worden gebruikt om te ondertekenen’’.

Dit sluit aan bij de definitie in de [eIDAS verordening](https://eur-lex.europa.eu/legal-content/NL/TXT/uri=celex:32014R0910). Kort gezegd komt dit op het volgende neer:

(1) een elektronische handtekening bestaat uit een verzameling digitale gegevens, zoals een afbeelding of een cryptografische codereeks, die (2) verbonden is met andere digitale gegevens, zoals een pdf-document of afbeelding, en die (3) door de ondertekenaar gebruikt wordt om die digitale gegevens te ondertekenen.

# Verschil met digitale handtekening
Een [digitale handtekening ](https://nl.wikipedia.org/wiki/Digitale_handtekening)is volgens Wikipedia een methode voor het bevestigen van de juistheid van [digitale](https://nl.wikipedia.org/wiki/Digitaal) [informatie](https://nl.wikipedia.org/wiki/Informatie) door middel van bijvoorbeeld technieken van de [asymmetrische cryptografie](https://nl.wikipedia.org/wiki/Asymmetrische_cryptografie), op een wijze vergelijkbaar met het [ondertekenen](https://nl.wikipedia.org/wiki/Ondertekenen) van papieren documenten aan de hand van een geschreven handtekening. Over het algemeen bestaat een digitale handtekening uit twee algoritmen: één om te bevestigen dat de informatie niet door derden veranderd is, de andere om de [identiteit](https://nl.wikipedia.org/wiki/Identificatie_(recht)) te bevestigen van degene die de informatie "ondertekent". De combinatie van de resultaten van deze twee [algoritmen](https://nl.wikipedia.org/wiki/Algoritme) vormt de digitale handtekening. De technieken worden toegepast met behulp van een [PublicKey Infrastructure](https://nl.wikipedia.org/wiki/Public_Key_Infrastructure).

Het enige onderscheid tussen elektronische handtekeningen en digitale handtekeningen is dat digitale handtekeningen het gebruik van een code of algoritme vereisen om de authenticiteit van een document te ondertekenen en te authenticeren. [Digitale handtekeningen zijn een subset van elektronische handtekeningen](https://de-electronische-signatuur.nl/is-er-een-duidelijk-verschil-tussen-elektronische-en-digitale-handtekeningen/). Hier geven we daarom de voorkeur aan de term elektronische handtekening ook al omdat we hiermee aansluiten bij eIDAS.

# Soorten handtekeningen vanuit juridisch perspectief
Vanuit juridisch perspectief kunnen we drie soorten elektronische handtekeningen onderscheiden:

- “Gewone” elektronische handtekening (SES);

- Geavanceerde elektronische handtekening (AES);

- Gekwalificeerde elektronische handtekening(QES).

In de onderstaande tabel – ontleend aan [DOCCO](https://www.ondertekenwijzer.nl/uitleg-ondertekenen) op ondertekenwijzer.nl - volgt uitleg.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1714128630490-image.png)

1] de betrouwbaarheid hangt zeer sterk af van de wijze waarop de software bepaalde maatregelen voor bewijslast geïmplementeerd heeft.

2] een rechter kan de handtekening bijvoorbeeld niet weigeren, enkel en alleen omdat deze in een digitale vorm is. Dit wordt soms vertaald door aanbieders in de term ‘100% rechtsgeldig’.

# DigiD en ondertekenen
In de huidige praktijk bevestigen klanten steeds vaker gemaakte keuzes in een portaal van de dienstverlener. Dit nadat ze met DigiD zij ingelogd. Is dit een verantwoorde werkwijze

DigiD is ontworpen om een bepaald niveau van betrouwbaarheid te bieden bij het verifiëren van de identiteit van gebruikers voor veel online transacties. Echter, de mate van betrouwbaarheid kan variëren afhankelijk van het specifieke gebruik en de context.

Hoewel DigiD geen elektronische handtekening is, kan het worden gebruikt als een methode om te bevestigen wie een handeling heeft uitgevoerd. Het niveau van authenticatie met DigiD is op zich voldoende voor een geavanceerde elektronische handtekening. Maar omdat de handtekening niet wordt vastgehecht aan de ondertekende gegevens is er geen sprake van een elektronische handtekening, zoals bedoeld in het Burgerlijk Wetboek (3:15a). Het is in feite een authenticatie plus een akkoordverklaring. DigiD kan na overlijden van een persoon nog 1 jaar gebruikt worden door naasten en andere direct betrokkenen.

Geadviseerd wordt DigiD op minstens niveau substantieel af te dwingen, de gemaakte keuzes te bevestigen en de klant te vragen om binnen een bepaalde termijn te reageren als het niet in orde is. De financiële dienstverlener moet hierbij rekeninghouden met de wetgeving rond elektronische informatieverstrekking.

---

[← Terug naar home]({{ site.baseurl }}/)
