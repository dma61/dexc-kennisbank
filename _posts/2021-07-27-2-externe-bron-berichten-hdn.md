---
layout: post
title: "Externe Bron Berichten HDN"
date: 2021-07-27
categories: ["Standaarden ► particuliere klant"]
question_id: 992900
---

Voor een koppeling met externe bronnen biedt HDN een standaard berichtenset (EA/EX), waarmee diverse bronnen geraadpleegd kunnen worden.  

- De HDN partij kan met het EA bericht een verzoek indienen bij de dienstenserver. De dienstenserver vertaald vervolgens het verzoek naar de specifieke bronservice. Het EA bericht is altijd voorzien van de noodzakelijke vraaggegevens.

- De dienstenserver verzendt een EX bericht retour. Dit EX bericht is enerzijds voorzien van brondata in de HDN standaard. Anderzijds in base 64 codering is het originele bronbericht hieraan toegevoegd. 

HDN biedt twee mogelijke procesinrichting voor externe bronnen, die complementair kunnen zijn. Te weten: 

- Directe aanroep: De aanbieder heeft zelf afspraken gemaakt met de bron en kan, voor de verrijking / controle van het dossier, een directe aanroep verrichten via het EA/ EX bericht.  

- Brondata door de keten: Ketenpartners hebben met elkaar afgesproken dat het intermediair / consument brontoetsingen uitvoert (met inzicht). Dit kan uit naam van de aanbieder, maar ook uit eigen naam zijn. Vervolgens wordt data, in de vorm van het EX bericht, doorgestuurd naar de aanbieder.

---

[← Terug naar home]({{ site.baseurl }}/)
