---
layout: post
title: "Gegevenstandaarden Introductie"
date: 2022-09-15
categories: ["Gegevensstandaarden"]
question_id: 1513945
---

**Waarom zijn gegevensstandaarden nodig**

Financiële dienstverleners wisselen gegevens uit met hun klanten, met andere (financiële) dienstverleners en databronnen. Berichten bestaan uit een set gegevens die we bij digitale communicatie uitwisselen. Een bericht heeft de bedoeling bepaalde informatie over te dragen van een zender naar een ontvanger. Om deze gegevens uit berichten - zonder menselijke tussenkomst - te verwerken zijn afspraken nodig:

- Afspraken over de **betekenis** van gegevens. Wat bedoel je met een Arbeidscontract, Inkomstenverhouding, Dienstverband 

- Afspraken over het **formaat**. Hoe lang mag een gegeven zijn. Is het numeriek, alfabetisch of alfanumeriek Mag een kenteken streepjes bevatten

- Afspraken over de **tekenset**. Hoe coderen we grafische tekens en symbolen

- Afspraken over toegestane **coderingen/codelijsten**. Bijvoorbeeld de landencode of de codering voor de branchecodes

- Afspraken over het **verband** met andere **gegevens**. De premie die we bij een klant in rekening brengen is de optelsom van andere bedragen. Dit kunnen we vastleggen in een rekenregel.

- Afspraken over alle aspecten van gegevens die voor de afnemer van belang zijn, bijvoorbeeld **actualiteit, juistheid of detail**, op het niveau dat de afnemer verwacht.

- Afspraken over het **groeperen** van gegevens. Gegevens die bij elkaar horen stoppen we in dezelfde groep (entiteit). Bijvoorbeeld Werkgever, Dienstverband, Verzuim.

- Afspraken over **frequentie**; het aantal keren dat een groep gegevens mag voorkomen in een bericht. Hoeveel auto’s kunnen op een particuliere polis gesloten worden

- Afspraken over de **structuur** van gegevens die we uitwisselen in berichten. Wissel je gegevens uit over één Werknemer dan kunnen we het Dienstverband, het Verzuim op hetzelfde niveau doorgeven. Wisselen we gegevens uit over alle Werknemers van een Werkgever dan moeten we Dienstverband en Verzuim nesten onder de Werknemer. Heeft een Werknemer meerdere dienstverbanden bij dezelfde Werkgever dan moeten we ook het Verzuim nesten onder het bijbehorende Dienstverband.

        Werkgever
                Werknemer-1
                        Dienstverband-1
                                      Verzuim
                        Dienstverband-2                                      Verzuim
                Werknemer-2                        Dienstverband-2
                                      Verzuim

- Afspraken over het gegevensformaat, ook bestandsformaat of syntax genoemd. Bijvoorbeeld JSON of XML. 
**Gegevenswoordenboek**

In diverse domeinen van de financiële sector maken organisaties afspraken om te komen tot eenduidige gegevensbeschrijvingen. Deze sets met eenduidige beschrijvingen vallen onder de brede noemer 'gegevenswoordenboek.' Andere termen voor gegevenswoordenboeken zijn: informatiemodellen, vocabulaires, thesauri, taxonomieën, tabellenboeken, ontologieën en registers. Duidelijk moet zijn wat we bedoelen als het over bepaald gegevenswoordenboek gaat : wat staat er wel in, wat niet Voor welk doel is het samengesteld, op welk detailniveau en wat kunnen we er dus wel en niet mee Een voorbeeld van een gegevenswoordenboek is de All Finance Datacatalogus van SIVI.

---

[← Terug naar home]({{ site.baseurl }}/)
