# ![](/icons/symmetry.webp) Symmetrie

Dit menu bepaalt hoe streken worden herhaald over een spiegelvlak of radiaal, en manieren om symmetrie te herstellen op niet-symmetrische objecten.

![](/images/symmetry_overview.webp) 

## Overzicht 
Je kunt symmetrie op verschillende manieren gebruiken:

* Als een spiegel, waarbij werk wordt gespiegeld over X (links/rechts), Y (boven/onder), Z (achter/voor), of een combinatie daarvan. 
* Radiale symmetrie kan worden ingesteld op X Y Z met een aantal herhalingen, bijvoorbeeld bij het sculpteren van een zeester. 
* Spiegels kunnen werken rond de oorsprong (wereldmodus genoemd) of rond het midden van een object (lokale modus genoemd).
* Sculpts die niet-symmetrisch zijn begonnen, kunnen gedwongen symmetrisch worden gemaakt.

Een snelkoppeling om symmetrie in/uit te schakelen is ook te vinden in het snelle linkerpaneel (*"Sym"*). De kleine 'L/W' geeft aan of Nomad in lokale of wereld-symmetriemodus staat. Je kunt ook lang drukken of naar het midden van het scherm vegen om een menu te openen.

![](/images/symmetry_button.webp) 

Dit is een globale optie, dus de status wordt overgenomen door de verschillende tools.
De enige uitzonderingen zijn de transformtools ([Verplaatsen](#translate), [Roteren](#rotate), [Schalen](#scale) en [Gizmo](#gizmo)) die hun eigen symmetrie-instelling hebben.

::: tip
Het symmetriemenu is voornamelijk bedoeld om streek-symmetrie te regelen. Je kunt ook objecten spiegelen en herhalen via [repeaters in het scenemenu](scene#repeaters). 
:::

## Ingeschakeld
Schakel de spiegelmodus in of uit, dit is hetzelfde als de `Sym`-knop in het snelle linkerpaneel. 

## Vlakken

Schakel symmetrievlak(ken) in, en stel het aantal herhalingen in voor radiale symmetrie. Merk op dat je niet slechts één vlak hoeft te kiezen; je kunt 1, 2 of 3 vlakken tegelijk inschakelen voor complexe symmetrie.

De as en het aantal herhalingen voor radiale symmetrie. Merk op dat deze ook niet beperkt zijn tot één as, en zelfs in combinatie met vlak-symmetrie kunnen werken om zeer snel gedetailleerde resultaten te genereren. (Het totale aantal herhalingen is beperkt tot 150)

![](/videos/symmetry_demo.mp4) 

## Methode
De spiegel kan ofwel ‘Lokaal’ zijn, en meebewegen met het object, of ‘Wereld’, en niet meebewegen. Als je niet zeker weet welke modus je nodig hebt, let dan op het spiegelvlak en de radiale indicatoren die over het object worden gelegd. In de lokale modus zullen, als je de transform-gizmo gebruikt en het model verplaatst, de spiegelindicatoren ook meebewegen. In de wereldmodus blijven de spiegelindicatoren vast staan en schuift het object erdoorheen.

## Spiegelen
![](/images/symmetry_mirroring.webp)

Bij het sculpteren in de buurt van de symmetrievlakken zullen sommige brushes een onvolmaakt symmetriegedrag vertonen. In deze sectie kun je symmetrie herstellen door één kant van je sculpt naar de andere te kopiëren. 

`Richting` - De knoppen `<<` en `>>` bepalen welke kant naar de andere wordt gekopieerd. Nomad berekent dit vanuit je huidige viewport, dus als je het bijvoorbeeld op `<<` zet, wordt altijd van schermrechts naar schermlinks gekopieerd.

![](/icons/shield.webp) `Masker` - Met de maskerknop kun je bepalen wat gespiegeld wordt; het maskeren van de doelzijde beschermt dat gebied, het maskeren van de bronzijde voorkomt dat dat gebied naar de doelzijde wordt gespiegeld. 

![](/icons/tool_hide.webp) `Verbergen` - Wanneer dit actief is, worden gebieden die aan de bronzijde verborgen zijn niet naar de doelzijde gespiegeld. 

`Spiegelen` zal proberen te bepalen of de topologie aan beide zijden van de spiegel hetzelfde is en, zo ja, alleen vertices verplaatsen. Dit is het meest voorkomende scenario.

`Splitsen & Spiegelen` zal het object in feite langs de spiegel doorsnijden, één kant kopiëren, die naar de andere kant spiegelen en vertices langs de spiegel lassen. Dit is een destructievere optie en verwijdert multiresolutie, maar soms is deze methode nodig als het model sterk verschilt over de spiegel.

### Object omkeren
![](/images/symmetry_flip.webp)
Maak de linkerkant tot de rechterkant en omgekeerd. Dit lijkt op het gebruik van het gizmo-toolmenu en het instellen van de schaal op -1 op X.

## Reset en bewerken

![](/images/symmetry_edit.webp)

Het is mogelijk om de locatie en oriëntatie van de symmetrie te bewerken (maar niet aanbevolen!). Indien nodig zullen `Wereldcentrum` en `Oriëntatie` de symmetrielocatie en -oriëntatie terugzetten naar hun standaardwaarden.

Nomad weet meestal waar het symmetrievlak moet komen. Het wordt niet aanbevolen dit handmatig aan te passen, maar de knop `Gizmo (Bewerken)` maakt dit mogelijk voor gevorderde gebruikers. Wanneer op deze knop wordt geklikt, verschijnt een gizmo waarmee je het symmetrievlak kunt verplaatsen en roteren. Als je het standaardcentrum en de standaardoriëntatie wilt herstellen, doen de knoppen `objectcentrum` en `oriëntatie` dit.

Het gedrag van deze opties verandert afhankelijk van in welke ruimte (*Lokaal/Wereld*) je je bevindt.
Als het dus niet werkt zoals je verwacht, controleer dan of je je in de juiste ruimte bevindt.

::: tip
De knop `Gizmo (Bewerken)` is expres grijs gemaakt als herinnering dat je deze waarschijnlijk niet zou moeten gebruiken!
:::

## Weergave-opties
![](/images/symmetry_show.webp)


`Lijn tonen` en `Vlak tonen` schakelen een viewport-overlay van de symmetrielocaties in of uit. Merk op dat het uitschakelen van deze opties pas effect heeft wanneer het symmetriemenu wordt gesloten.
