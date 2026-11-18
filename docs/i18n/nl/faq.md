# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Platform {#platform}
### Waar staan mijn projecten op mijn apparaat? {#locate}
De projecten staan in de map `projects` in de hoofdmap van Nomad.

Op iOS kun je de Nomad-map openen met de app Bestanden van iOS.

Op Android staat de Nomad-map in `Android/data/com.stephaneginier.nomad/files/`.  
Op recente Android-versies (10/11) heb je geen toegang meer tot de map `Android/data`.
Je kunt er wel bij via een aparte app, bijvoorbeeld [deze](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Kan ik een bètaversie testen? {#beta}
Voor Windows en MacOS is er soms een bètaversie beschikbaar op de [Homepage](https://nomadsculpt.com).
<br>
Voor iOS is er een besloten TestFlight; kijk op de [Discord](https://discord.com/invite/8h7BwpRz29) in het kanaal #beta-ios.
<br>
De [Webdemo](https://nomadsculpt.com/demo) wordt meestal bijgewerkt met de nieuwste functies.

### Waarom is er een gratis proefversie op Android, maar niet op iOS? {#android-trial}
Omdat oude Android-apparaten slecht presteren (en sommige recente ook...), en ik niet wilde dat mensen de app kochten en dan een zwart scherm te zien kregen.
Maar de belangrijkste reden is dat ik het gevoel had dat betaalde Android-apps niet echt gebruikelijk zijn.

### Wat is de beste tablet voor Nomad? {#best-tablet}

Kort gezegd: een iPad.

Het iets langere antwoord is

> "De nieuwste iPad _die je kunt betalen_, tenzij je echt een hekel hebt aan Apple: dan de nieuwste Samsung-tablet die je kunt betalen. Al het andere: eerst testen."

Mensen willen altijd meer weten, dus hier een samenvatting.

Nomad draait het best op nieuwere iPads:

* iPads en iPhones hebben toegang tot de plugin [Quad Remesher](tools#quad-remesher) van [Exoside](https://exoside.com/)
* recente iPads met de nieuwste pencil ondersteunen [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0): bij bepaalde tools in Nomad kun je de pencil om zijn as draaien.
* de nieuwste chips uit de M-serie zijn erg snel.

De nieuwste en duurste iPad rendert eindbeelden heel snel en laat je heel veel detail sculpten.

De prestaties van goedkopere en oudere iPads vallen echter minder tegen dan mensen denken. Elke iPad die een Apple Pencil ondersteunt, draait Nomad behoorlijk goed. Bijvoorbeeld:

* Een iPad Pro uit 2023 kan sculpts van 5 miljoen polygonen aan en blijft vlot reageren; een eindbeeld in volle kwaliteit rendert in 5 seconden.
* Een iPad Pro uit 2015 kan een object van 1,2 miljoen polygonen aan met een beetje vertraging; een eindbeeld in volle kwaliteit rendert in 20 seconden.

Dat is een groot verschil in prestaties, maar je moet ook naar de prijs kijken:

* De iPad Pro uit 2025 kost nieuw, met alle opties, *$2500 USD*.
* De iPad Pro uit 2023 kost op dit moment *$400 USD* op eBay.
* De iPad Pro uit 2015 kost *$250 USD* op eBay.

Zijn 4 miljoen extra polygonen en 15 seconden tijdwinst $2100 waard? Dat mag je zelf bepalen.

Modellen zonder Pro kunnen nog goedkoper zijn en bieden een ruime keuze aan formaten en prestaties. De huidige iPad Air ondersteunt de pencil van de 2e generatie met barrel roll en is flink goedkoper dan de Pro. Op de tweedehands- en refurbished-markt is er nog meer keuze.

Wat je budget ook is, je zou dus een iPad moeten kunnen vinden die bij je past. En onthoud dat de meeste sculpts geen miljoenen polygonen hebben! Blijf je onder de 500.000 polygonen, dan kun je zelfs op oude iPads vlot sculpten.

`En Android?`

De grafische prestaties van Android liggen onder die van iPads. Volgens de ontwikkelaar van Nomad "draait een Samsung Galaxy Tab S9 Nomad een orde van grootte langzamer dan een iPad Air". Toch zijn veel gebruikers erg tevreden met hun Samsung-tablet; voor het meeste sculptwerk draait Nomad prima.

Wees voorzichtig met andere Android-tablets. De prestaties van Android-hardware lopen sterk uiteen, en het is lastig te voorspellen hoe Nomad erop draait.

Test daarom eerst met de gratis versie van Nomad, waarin opslaan is uitgeschakeld.

`En geheugen en opslag?`

De meeste Nomad-bestanden zijn 100 MB of kleiner. Bijna elke tablet die je tegenwoordig koopt, iPad of Android, heeft dus ruim genoeg plek voor je Nomad-projecten.


### Ik heb Nomad voor één apparaat gekocht, kan ik het ook op een ander apparaat gebruiken? {#multi-devices}
Ja, zolang dat apparaat dezelfde appwinkel en hetzelfde account gebruikt.

Heb je het bijvoorbeeld in de iOS App Store gekocht, dan kun je het op je andere iOS-apparaten gebruiken.

Heb je het voor je Android-tablet op Google Play gekocht, dan kun je het op je andere Android-apparaten gebruiken.

Heb je Nomad echter op Android gekocht en neem je daarna een iPad, dan moet je het opnieuw kopen.

Dat komt doordat Nomad geen eigen licentieserver of abonnementsmodel heeft. Er is geen afspraak tussen Apple, Google en AppGallery om licenties te delen.


### Hoe herstel ik mijn aankoop? {#restore}
Google Play en AppGallery regelen de synchronisatie allebei automatisch.

- Ga naar het menu Over (het Nomad-icoon linksboven) en tik op `Herstel aankoop`
- Controleer of je bent ingelogd met hetzelfde account waarmee je Nomad hebt gekocht (op Google Play).
- Start het apparaat opnieuw op
- Soms moet je een paar uur wachten
- Zorg dat de app Google Play up-to-date is
- Installeer Nomad opnieuw (maak eerst een [back-up van je bestanden](#locate) als je niets kwijt wilt raken)
- Je kunt proberen het opnieuw te kopen om te zien wat er gebeurt (let op: je kunt hetzelfde item niet twee keer kopen met hetzelfde account)

:::tip
Je kunt contact met me opnemen via <support@nomadsculpt.com>, maar het *enige* wat ik kan doen, is bevestigen of er een aankoop aan een e-mailadres gekoppeld is.

Ik krijg regelmatig meldingen dat licenties niet goed worden bijgewerkt na de aanschaf van een nieuw apparaat.
Ik heb geen enkele invloed op de betaling en de synchronisatie van accounts; dat wordt allemaal door Google/AppGallery geregeld!

Uiteindelijk wordt de aankoop altijd hersteld, maar wat je precies moet doen om dat te versnellen, is niet duidelijk.
:::

::: warning
Recente apparaten van Huawei hebben geen toegang tot de diensten van Google.
In dat geval moet je de app opnieuw kopen in AppGallery (de appwinkel van Huawei).
:::

### Kun je [mijn-taal] vertalen of verbeteren? {#locale}
Ik kan vrij makkelijk een nieuwe taal toevoegen, maar ik gebruik AI-vertaling, omdat dat bij regelmatige updates veel makkelijker is.
De vertaalbestanden vind je [hier](https://github.com/stephomi/nomad-translation).

## Functies {#features}

### Waarom beweegt de gizmo niet? {#gizmo-not-moving}
Misschien staat [vastzetten aan in de werkbalk van het linkermenu](tools#left-menu-toolbar).

### Kunnen we in Nomad animeren? {#animate}
Voorlopig niet. Een tijdlijn waarmee je de lagen kunt animeren zou interessant kunnen zijn, maar staat op dit moment niet echt op de planning.

Ik zou in de toekomst graag rigging/skinning ondersteunen, maar dat brengt een paar uitdagingen met zich mee (vooral de wisselwerking met de sculpttools...), dus voorlopig is er nog niets zeker.


### Kunnen we echt low-poly modelleren? {#lowpoly}
Voorlopig niet.
Dat valt eigenlijk buiten het doel van Nomad *Sculpt*, maar misschien voeg ik in de toekomst een paar tools toe.


### Kunnen we UV's maken en texturen? {#texturing}
Kort antwoord: ja. Lang antwoord: niet direct, maar er zijn verschillende manieren om de uitstekende vertex-schildertools van Nomad te combineren met UV's en texturen.

* In Nomad kun je kleur, ruwheid en materiaaleigenschappen direct in de vertices van je sculpt schilderen.
* Nomad kan heel veel vertices aan, zodat je kunt schilderen zonder je druk te maken over UV's.
* Nomad kan texturen laden om in penselen te gebruiken, zodat je met texturen kunt stempelen en schilderen.
* Nomad kan objecten laden waaraan al texturen zijn toegewezen, om ze te renderen.
* Nomad kan objecten met minder polygonen [UV-ontvouwen](topology.md#uv-unwrap-uvatlas).
* Kleur/ruwheid/metaalheid kun je van texturen naar vertices overzetten via [de projectieopties](topology.md#reproject-to-vertex).
* Kleur/ruwheid/metaalheid/normalen kun je van vertices naar texturen bakken via [de bakopties](topology.md#bake-texture)
* Bakken en projecteren kan tussen losse objecten of veel objecten, of tussen het hoogste en laagste onderverdelingsniveau van één object, zodat je verschillende bak- en projectieworkflows kunt gebruiken.
* Exporteer je na het bakken een OBJ, dan worden ook de texturen geëxporteerd. Die kun je meenemen naar een app als Procreate om direct op de texturen te schilderen.

### Kan ik een draaitafelvideo opnemen? {#video}
Dat staat voorlopig niet op de planning, maar iOS heeft een [functie voor schermopname](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) die heel makkelijk te gebruiken is.

Op iOS veeg je daarvoor omlaag vanaf de linkerbovenhoek en tik je op de opnameknop. Je krijgt een aftelling van 3 seconden: veeg het menu weg om Nomad te zien en gebruik de draaitafelfunctie. Als het klaar is, veeg je weer omlaag vanaf rechtsboven en tik je nog eens op de opnameknop. Bewerk de video in de fotobibliotheek om het overbodige stuk aan het begin en eind weg te knippen.

### Kun je [favoriete-functie] als knop op het hoogste niveau toevoegen? {#interface}
Ja, de onderste werkbalk kun je nu aanpassen in het menu [Interface](interface.md#shortcuts), en je kunt nu ook zwevende werkbalken maken.

### Wat zijn de volgende functies? {#next-features}
Voor de roadmap op middellange en lange termijn heb ik veel ideeën, maar ik weet het nog niet.

Bugs oplossen en bestaande functies verbeteren heeft altijd voorrang op nieuwe functies toevoegen.


### Kunnen we in Nomad riggen? {#rigging}
Nee, maar het staat op de planning. Voorlopig kun je vormen aan elkaar koppelen en draaipunten aanpassen, zodat je eenvoudige poseerbare sculpts kunt maken.

### Kunnen we meer dan 4 lichten gebruiken? {#lights}
Je kunt maximaal 4 lichten gebruiken op mobiel, en maximaal 6 op desktop. Dat is een beperking van de realtime render-engine van Nomad. Je kunt meer lichten nabootsen met lichtgevende objecten en globale verlichting in de nabewerking, zoals in [deze tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Kunnen we ZBrush-tools importeren? {#zbrush-import}
Nee, Zbrush gebruikt een eigen, gesloten formaat. Je zou wel de alpha maps moeten kunnen exporteren en die in Nomad gebruiken.

### Waarom kloppen de kleuren niet met wat ik heb geschilderd? Waarom krijg ik geen wit in de render? {#paint-pbr}
Stel je voor dat je een foto maakt van een vel papier, van een bureaulamp en van de zon. Oudere camera's en schermen maken die allemaal gewoon 'wit'. Modernere systemen kunnen laten zien dat er verschil is tussen het teruggekaatste wit van papier, het uitgestraalde licht van een lamp en het felle licht van de zon.

Moderne computergraphics proberen op een vergelijkbare manier te werken, door de natuurkunde van licht en oppervlakken na te bootsen. Dat heet `Physically Based Rendering`, of PBR, en de PBR-renderer van Nomad is daarop gebaseerd. Dat ziet er realistisch en evenwichtig uit, maar fel geschilderde kleuren lijken vaak donkerder.

Wil je dat de render beter overeenkomt met de geschilderde kleuren, dan kun je dat op een niet-fysieke en op een fysieke manier oplossen:

Zonder PBR:
* `Gebruik de modus 'Onbelicht' in het menu Shading`. De kleuren worden precies getoond zoals je ze hebt geschilderd, maar je verliest ook alle shading. Handig voor snelle controles en voor een meer grafische look.
* `Gebruik de modus 'MatCap' in het menu Shading`. Kies een lichtere matcap die vooral wit is, zonder kleurtint.

Met PBR:
* `Gebruik een neutrale omgeving`. Je kunt [de omgeving veranderen](shading.md#environment) in een neutralere. Vermijd binnenomgevingen, want die zijn vaak sterker gekleurd. Kies liever een omgeving buiten bij daglicht of een studio.
* `Geef de verlichting een boost`. Maak je een foto van wit papier in een donkere kamer, dan zou je gewoon meer licht toevoegen. Zet bij het omgevingslicht de belichtingsschuif hoger tot de kleuren goed aanvoelen, of voeg meer losse lichten toe met een hogere intensiteit.
* `Geef de belichting van de camera een boost`. Als er in de donkere kamer geen extra lampen waren, zou je de sluiter van de camera langer open kunnen laten, of een gevoeligere ISO kunnen gebruiken. In Nomad krijg je iets vergelijkbaars met nabewerking. Ga naar Nabewerking, zet het aan, ga omlaag naar toonmapping, zet dat aan, en verhoog de belichtingsschuif tot de kleuren goed aanvoelen.
* `Gebruik een lichtgevende kleur`. In het materiaalmenu kun je 'Lichtgevend' aanzetten onder texturen; daardoor lijkt een object een lichtbron. Zet je globale verlichting aan in de nabewerkingsinstellingen, dan werpt het licht op andere objecten in de scène. Je kunt voor dat materiaal ook 'Altijd onverlicht' aanzetten; dat geeft een vergelijkbare look zonder textuur.

## Crashes {#crashes}

### Het crasht als ik mijn model opsla of remesh! {#crash-remesh}
Je apparaat heeft te weinig geheugen (RAM).  
Om het geheugengebruik van je scène te verminderen, kun je een paar opties van [Topologie](topology.md) gebruiken om het aantal polygonen te verlagen.

::: tip RAM/opslag
Het gaat om de hoeveelheid RAM, niet om de opslag (die meestal veel groter is).
:::


### Het crasht als ik mijn project laad! {#crash-load}
Is het bestand klein, dan kun je het naar me opsturen en kijk ik ernaar (per e-mail naar <support@nomadsculpt.com>).

Anders heeft het apparaat waarschijnlijk te weinig RAM-geheugen.

- Sluit alle andere geopende apps op je apparaat.
- Begin een nieuw project in Nomad, zodat er niet al een project open staat.
- Crasht het nog steeds, dan is de enige oplossing om [je projectbestand](#locate) te laden op een apparaat met meer geheugen.

::: tip
Kan je mobiele apparaat het project niet laden, probeer dan de [desktopversie](https://nomadsculpt.com). Die kun je gratis gebruiken in de demomodus om projecten te importeren en te exporteren, al zijn er maar een paar bewerkingstools beschikbaar.

Gebruikt je project [Lagen](layers.md), dan kun je ze samenvoegen om minder geheugen te gebruiken.
:::

### Het crasht als ik Nomad start! {#crash-start}
Crasht het tijdens het laden, dan heeft Nomad moeite met een bepaald bestand in de Nomad-map.

Meestal komt dat doordat het project zwaar is en helaas over de RAM-limiet gaat.

Zoek de [Nomad-map](#locate) op en hernoem of verplaats een paar bestanden om de boosdoener te vinden.

Probeer eerst `settings.json` te hernoemen. Dan wordt het laatste project niet meer geladen.

Werkt dat niet, verplaats dan een paar recente bestanden uit hun bronmap (`projects`, `matcaps`, `environments`, enz.).

Je kunt ook de mappen zelf hernoemen, zodat Nomad ze helemaal negeert.
Hernoem of verplaats je alle bestanden in de Nomad-map, dan is het resultaat hetzelfde als bij een schone installatie.

::: tip
Als Nomad bij het opstarten een bestand laadt, verplaatst het dat bestand altijd naar de map `can_be_deleted/`.
Lukt het laden, dan wordt het teruggezet naar de oorspronkelijke map.

Crasht het voordat het laden klaar is, dan start Nomad de volgende keer gewoon op, omdat het de map `can_be_deleted/` negeert.

Denk je dat het laden wel kan lukken, dan kun je dit bestand gewoon opnieuw proberen te laden.
:::
