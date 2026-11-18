# ![](/icons/symmetry.webp) Symmetrie {#symmetry}

Dit menu bepaalt hoe streken worden herhaald over een spiegelvlak, radiaal of als tegels, en hoe je de symmetrie herstelt op objecten die niet symmetrisch zijn.

![](/images/symmetry_overview.webp) 

## Overzicht {#overview}
Je kunt symmetrie op verschillende manieren gebruiken:

* Als spiegel, waarbij je werk wordt gespiegeld over X (links/rechts), Y (boven/onder), Z (achter/voor) of een combinatie daarvan.
* Radiale symmetrie stel je in op X, Y of Z met een aantal herhalingen, bijvoorbeeld om een zeester te sculpten.
* Tegels herhalen je streken over het object, zodat de sculpt naadloos aansluit.
* Spiegels kunnen werken rond de oorsprong (de wereldmodus) of rond het midden van een object (de lokale modus).
* Sculpts die niet symmetrisch zijn begonnen, kun je alsnog symmetrisch maken.

Een snelkoppeling om symmetrie aan of uit te zetten vind je ook in het linker snelpaneel (*"Sym"*). De kleine 'L/W' geeft aan of Nomad in de lokale (Local) of wereldsymmetrie (World) staat. Je kunt ook lang indrukken of naar het midden van het scherm vegen om een menu te openen.

![](/images/symmetry_button.webp) 

De symmetrie-instellingen worden per object opgeslagen, en de titel van het menu toont de naam van het object dat je bewerkt.
De sculptgereedschappen delen dezelfde aan/uit-status, terwijl de transformatiegereedschappen ([Transformeren](tools.md#transform) en [Gizmo](tools.md#gizmo)) hun eigen status hebben.

::: tip
Het menu Symmetrie is vooral bedoeld voor de symmetrie van streken. Je kunt objecten ook spiegelen en herhalen met de [repeaters in het menu Scène](scene#repeaters).
:::

## ![](/icons/symmetry.webp) Ingeschakeld {#enabled}
Zet de spiegelmodus aan of uit, hetzelfde als de knop `Sym` in het linker snelpaneel. Een waarschuwingsicoon herinnert je eraan wanneer het uitstaat, en het menu laat ook weten wanneer het huidige gereedschap symmetrie negeert.

## Vlakken {#planes}

Zet symmetrievlak(ken) aan en stel het aantal herhalingen voor radiale symmetrie in. Je hoeft niet maar één vlak te kiezen: je kunt 1, 2 of alle 3 de vlakken aanzetten voor complexe symmetrie.

De rij `Radiaal` stelt het aantal herhalingen in voor radiale symmetrie rond elke as. Ook die zijn niet beperkt tot één as, en ze werken zelfs samen met vlaksymmetrie, zodat je heel snel gedetailleerde resultaten krijgt. (Het totale aantal herhalingen is beperkt tot 200.)

![](/videos/symmetry_demo.mp4) 

## Tegel {#tile}

Herhaalt je streken langs een as, op een vaste afstand, zodat de sculpt naadloos aansluit. Handig voor patronen, bakstenen of een textuur die je wilt herhalen.

Zet tegels aan per as met de knoppen `Tegel`, en stel dan een `Aantal` in (hoeveel herhalingen het object beslaan) of een `Afstand` (de ruimte tussen twee herhalingen). Tik op de schakelaar links om tussen de twee te wisselen.

## Methode {#method}
De spiegel kan `Lokaal` zijn en met het object meebewegen, of `Wereld` zijn en blijven staan. Weet je niet zeker welke modus je nodig hebt, kijk dan naar de aanwijzers voor het spiegelvlak en de radiale symmetrie die over het object worden getoond. In de lokale modus bewegen de spiegelaanwijzers mee als je het model verplaatst met de transformatiegereedschappen (`Gizmo` of `Transformeren`). In de wereldmodus blijven de spiegelaanwijzers op hun plek en schuift het object erdoorheen.

## Spiegel {#mirroring}
![](/images/symmetry_mirroring.webp)

Als je vlak bij de symmetrievlakken sculpt, gedragen sommige penselen zich niet helemaal symmetrisch. In deze sectie herstel je de symmetrie door de ene kant van je sculpt naar de andere te kopiëren.

`Richting` - De twee pijlknoppen naast de titel `Spiegel` bepalen welke kant naar de andere wordt gekopieerd. Nomad berekent dit op basis van je huidige viewport, dus de kant blijft op het scherm dezelfde, van welke kant je ook naar het model kijkt.

![](/icons/shield.webp) `Masker` - Met de maskerknop bepaal je wat er wordt gespiegeld: maskeer je de doelkant, dan wordt dat gebied beschermd; maskeer je de bronkant, dan wordt dat gebied niet naar de doelkant gespiegeld.

![](/icons/tool_hide.webp) `Verbergen` - Staat dit aan, dan worden verborgen gebieden aan de bronkant niet naar de doelkant gespiegeld.

`Spiegel` (behoud topologie) probeert te herkennen of de topologie aan beide kanten van de spiegel hetzelfde is, en verplaatst in dat geval alleen vertices. Dit is het meest voorkomende geval. Radiale symmetrie wordt genegeerd. Is de topologie niet symmetrisch, dan biedt Nomad aan om het spiegelen af te dwingen met `Snij • Spiegel`.

De knoppen `Snij` snijden het object door langs het symmetrievlak of de symmetrievlakken. Ze veranderen de topologie en zijn dus destructiever dan `Spiegel`. Het getal op elke knop geeft aan hoeveel objecten je krijgt:

* `Snij` - verwijdert één kant van het object.
* `Snij • Spiegel` - snijdt het object door, kopieert één kant, spiegelt die naar de andere en last de vertices langs de spiegel aan elkaar. Soms is deze methode nodig als het model aan beide kanten van de spiegel heel verschillend is.
* `Snij • Splitsen` - snijdt het object door en houdt elke kant als apart object.
* `Snij • Spiegel • Splitsen` - zoals `Snij • Spiegel`, maar elke kant wordt een apart object.

Zijn er meerdere objecten geselecteerd, dan gelden `Spiegel` en [Object omkeren](#flip-object) voor allemaal.

### Object omkeren {#flip-object}
![](/images/symmetry_flip.webp)
Maakt van de linkerkant de rechterkant en omgekeerd, langs `X`, `Y` of `Z`. Het resultaat lijkt op wat je krijgt als je in het menu van het gereedschap Gizmo de schaal op X op -1 zet.

## Herstellen en bewerken {#reset-and-edit}

![](/images/symmetry_edit.webp)

Je kunt de positie en oriëntatie van de symmetrie bewerken (maar dat raden we niet aan!). Indien nodig zetten `Wereldcentrum` (`Objectcentrum` in de lokale modus) en `Oriëntatie` de positie en oriëntatie van de symmetrie terug op hun standaardwaarden.

Nomad weet meestal goed waar het symmetrievlak hoort. Handmatig aanpassen is niet aan te raden, maar met de knop `Gizmo bewerken` kunnen gevorderde gebruikers het toch doen. Klik je op deze knop, dan verschijnt een gizmo waarmee je het symmetrievlak verplaatst en draait. Wil je het standaardmidden en de standaardoriëntatie terug, gebruik dan de herstelknoppen hierboven.

`Van draaipunt` plaatst het symmetrievlak op het draaipunt van het gereedschap [Gizmo](tools.md#gizmo). Het is alleen beschikbaar zolang het gereedschap `Gizmo` actief is.

Hoe deze opties zich gedragen, hangt af van de ruimte (*Lokaal/Wereld*) waarin je werkt.
Werkt het niet zoals je verwacht, controleer dan of je in de juiste ruimte zit.

::: tip
Het symmetrievlak bewerken met de gizmo is een beetje experimenteel: waarschijnlijk heb je het niet nodig!
:::

## Weergaveopties {#show-options}
![](/images/symmetry_show.webp)


`Lijn tonen` en `Vlak tonen` zetten een weergave van de symmetriepositie in de viewport aan of uit. Let op: het uitzetten van deze opties wordt pas zichtbaar wanneer het menu Symmetrie gesloten is.
