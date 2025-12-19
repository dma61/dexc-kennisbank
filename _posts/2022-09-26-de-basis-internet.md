---
layout: post
title: "De basis: Internet"
date: 2022-09-26
categories: ["Bouwstenen/Principes"]
question_id: 1533617
---

Digitale datadragers zijn onder meer cd’s, data-tapes, diskettes, Dvd’s, geheugenkaarten en USB sticks. Digitaal transport van data loopt echter veelal via Internet. Daarom loont het de moeite dit uit te leggen door de belangrijkste protocollen en standaarden kort te bespreken.

**Wat is het Internet**

Het Internet is een netwerk dat computers wereldwijd met elkaar verbindt, en bedrijven, overheden, personen met elkaar laat communiceren en informatie laat delen. Dit is mogelijk door een groot aantal protocollen en standaarden. Een protocol is in dit verband een beschrijving van de wijze waarop apparaten en computerprogramma's onderling communiceren. Standaarden zijn afspraken over informatie of over een proces, dit kan zowel op het niveau van semantische als technische standaarden. Veelal worden de afspraken vastgelegd in documenten met een erkende status. In feite is Internet gebaseerd op de beproefde implementatie van tientallen standaarden.

**Strategische betekenis (Internet) standaarden**

In “Information Rules” uit 1998 gaan Carl Shapiro en Hal R. Varian al uitgebreid in op de strategische betekenis van standaarden: 

- Standaarden vergroten de interoperabiliteit. Hierdoor wordt het netwerk voor de gebruikers groter. De grotere mogelijkheid om informatie te delen trekt meer gebruikers waardoor de waarde nog meer stijgt. 

- Standaarden verminderen het technologisch risico voor gebruikers. Dit versnelt de acceptatie van nieuwe technologie.

- Als werkelijk sprake is van een open standaard, zullen gebruikers zich minder zorgen maken over insluiting. Bedrijven gaan binnen de markt concurreren, waarbij ze gebruik maken van de gemeenschappelijke normen.

- Standaarden verschuiven de concurrentie van die op het gebied van kenmerken naar die op het gebied van de prijzen. Hoe meer specifiek de standaard, hoe moeilijker het is voor een producent om zijn product te differentiëren en toch aan de standaard te voldoen.

- Standaarden verschuiven het gebied waarop geconcurreerd wordt van systemen naar componenten. Specialisten gedijen vervolgens in de door de interface-normen gecreëerde omgeving.

Standaarden zijn het meest van belang als zij algemeen erkend worden en ook door software worden ondersteund. 

**Modellen om de Internet standaarden te groeperen**

**![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9209/direct/1664174636940-1664174636940.png)**

De figuur toont twee modellen om de diverse Internet protocollen/standaarden te groeperen:

- [OSI-model](https://osi-model.com/)

- [TCP/IP hiërarchie](https://en.wikipedia.org/wiki/Internet_protocol_suite)

 Het voert hier te ver om alle lagen/protocollen uitputtend te behandelen. We richten ons immers vooral op de toepassing van transportprotocollen in de financiële sector en beperken ons daarom tot de hoofdzaken.

**(1) OSI-model**

Het model Open Systems Interconnection (OSI-model) is een door de International Organization for Standardization (ISO) gestandaardiseerd referentiemodel voor datacommunicatiestandaarden, ter bevordering van de interoperabiliteit tussen heterogene netwerktypologieën. Een netwerktopologie beschrijft fysieke verbindingen tussen netwerkcomponenten onderling.

| Laag | Functie |
| --- | --- |
| 7. Applicatie laag | Protocollen voor directe uitwisseling met de applicatie. |
| 6. Presentatie laag | Formatteert en structureert data ten behoeve van applicatie-interpretatie. |
| 5. Sessie laag | Start, onderhoudt en beëindigt sessies tussen applicaties. |
| 4. Transport laag | Segmentatie, volgordelijkheid van de data-segmenten en foutcorrectie. |
| 3. Netwerk laag | Logische adressering, routeinformatie. |
| 2. Link laag | Protocol multiplexing, mediumtoegang, fysieke adressering en foutdetectie. |
| 1. Fysieke laag | Binaire transmissie, elektrische, elektromagnetische of optische specificaties van het signaal en fysieke specificaties van het medium. |

| Laag | Functie/protocollen (niet uitputtend) |
| --- | --- |
| Applicatie laag | In de applicatie laag bevinden zich de internettoepassingen. Deze toepassingen hebben meestal een client-server structuur.Finger, Gopher, HTTP, HTTPS, IMAP, IRC, NNTP, NTP, POP3, QOTD, RTP, RTSP, S... |
| Transport laag | De transport laag zorgt voor de communicatie tussen processen die zich op de hosts bevinden. Elke internetapplicatie is voor wat betreft de transport laag gebouwd op ofwel TCP- ofwel UDP-protocol. ... |
| Netwerk laag | De bedoeling van deze laag is om de aangeboden data van bron naar doel te versturen ongeacht het protocol of type data, enkel ervoor zorgen dat alles netjes toekomt op de plaats van bestemming. Via... |
| Link laag (inclusief fysieke laag) | Deze laag maakt tevens de fysieke connectie tussen de netwerken mogelijk, zij bevat alle gegevens van een LAN- en WAN-netwerk die nodig zijn om een connectie te verwezenlijken.Point-to-Point Protoc... |

| Standaard | Beschrijving |
| --- | --- |
| FTP | Het File Transfer Protocol (FTP) is een protocol dat uitwisseling van bestanden over het internet tussen computers vergemakkelijkt. Het standaardiseert een aantal handelingen die tussen besturingss... |
| HTTPS | HyperText Transfer Protocol Securewordt toegepast op de communicatie tussen clients (zoals webbrowsers) en servers voor alle websites en webservices.HTTPS zorgt voor het gebruik van HTTP over een m... |
| IMAP | De Internet Message Access Protocol (IMAP) beschrijft een protocol voor het synchroniseren van e-mail tussen een e-mail server en eindgebruikers e-mailapplicatie. E-mail wordt daarbij niet van de s... |
| POP3 | Post Office Protocol 3 (POP3) is een internetstandaard voor het ophalen van e-mail van een server naar een cliënt over een TCP/IP-verbinding. POP3 servers houden inkomende e‑mailberichten vast totd... |
| S/MIME | Secure Multipurpose Internet Mail Extensions (S/MIME) is een standaard voor de ondertekening en versleuteling van e-mail tussen gebruikersapplicaties ('end-to-end'). De verzender ondertekent en/of ... |
| SMTP | Simple Mail Transfer Protocol is een relatief simpel, tekst gebaseerd, protocol voor het versturen van e-mail over het internet: eerst wordt de afzender van het bericht gespecificeerd, daarna één o... |
| TCP/IP | Transmission Control Protocol / Internetprotocol is niet één standaard, maar bestaat uit een serie standaarden die in samenhang werken.De IP standaarden zorgen ervoor dat gegevens over het Internet... |
| TLS | Transport Layer Security moet worden toegepast op de uitwisseling van gegevens tussen clients en servers, inclusief machine-to-machine communicatie.TLS zorgt door middel van de uitwisseling van cer... |
| WSDL | Web Services Description Language (WSDL) beschrijft de interfaces van webservices en hoe de service gebruik maakt van een berichtenprotocol, met name SOAP. Over het algemeen zullen WSDL documenten ... |**(2) TCP/IP hiërarchie**

Voorbeelden van [transport gerelateerde standaarden](https://www.forumstandaardisatie.nl/open-standaarden/x509):



---

[← Terug naar home]({{ site.baseurl }}/)
