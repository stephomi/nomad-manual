# ![](/icons/scene.webp) Scène {#scene}

In dit menu beheer je de objecten, lichten, camera's en repeaters in Nomad. Het toont de hiërarchie van de scène als boomstructuur, waarmee je veel eigenschappen van je objecten kunt aanpassen. Je kunt er ook nieuwe objecten maken, en objecten op allerlei manieren samenvoegen en splitsen.


![](/images/scene_menu_summary.webp)


## Snelkoppelingsbalk {#shortcut-bar}
| Actie                  | Pictogram                         | Beschrijving                                                                                                        |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Toevoegen...](#add-menu) | ![](/icons/plus.webp)          | Toon het [menu Toevoegen](#add-menu) om een object aan de scène toe te voegen                                       |
| Verwijderen            | ![](/icons/trash.webp)           | Verwijder de geselecteerde objecten. Hun kinderen blijven behouden.                                                 |
| Vergrendelen           | ![](/icons/lock.webp)            | Maak de geselecteerde objecten onselecteerbaar in de viewport. Je kunt ze nog wel in de boomstructuur selecteren. Vergrendel je een groep, dan wordt alles eronder vergrendeld. Tik nog eens om te ontgrendelen. |
| [Samenvoegen](#join)   | ![](/icons/merge.webp)           | Voeg de geselecteerde objecten samen tot één object, zonder de geometrie te veranderen                              |
| [Splitsen...](#separate) | ![](/icons/separate.webp)      | Toon het venster [Splitsen](#separate) om een object in meerdere objecten op te delen. Het omgekeerde van samenvoegen |
| [Booleaans...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Toon het venster [Booleaans](#boolean)                                                                     |
| Klonen                 | ![](/icons/clone.webp)           | Dupliceer de geselecteerde objecten als nieuwe objecten                                                             |
| Instantie              | ![](/icons/link.webp)            | Dupliceer de geselecteerde objecten als instanties: wijzigingen aan de vorm van de ene gelden dan voor alle instanties. |
| Instantie opheffen     | ![](/icons/unlink.webp)          | Maak van een instantie een unieke vorm, zodat wijzigingen aan de vorm niet meer naar de andere instanties worden gekopieerd |
| Synchroniseren         | ![](/icons/checked.webp)         | Als dit is aangevinkt, gelden bewerkingen voor alle instanties van de geselecteerde objecten, niet alleen voor de geselecteerde. Alleen beschikbaar als de selectie instanties bevat. In het [tabblad Synchroniseren](#sync) van het venster `Geavanceerd` stel je in welke bewerkingen dit vakje volgen. |

::: tip
Heeft een bewerking ook invloed op de andere instanties, dan staat er een klein koppelingspictogram op de knop.
:::


## Boomstructuur {#tree-view}
![](/images/scene_treeview.webp) 

De boomstructuur toont de objecten, groepen, repeaters, lichten en camera's van de scène. Naast de naam van een mesh zie je het aantal vertices, met een gekleurd laagpictogram als de mesh lagen heeft. Elke rij heeft deze knoppen:

| Actie        | Pictogram                  | Beschrijving             |
| :----------: | :------------------------: | :----------------------: |
| Naam         | ![](/icons/pencil.webp)   | Geef het object een andere naam. Is het geselecteerd, dan krijgen alle geselecteerde objecten tegelijk een nieuwe naam, met een nummer erachter. Houd lang ingedrukt om ook de kinderen een nieuwe naam te geven. |
| Selecteren   | ![](/icons/checked.webp)  | Selectie aan/uit         |
| Zichtbaar    | ![](/icons/eye_open.webp) | Zichtbaarheid aan/uit    |
| Menu         | ![](/icons/more.webp)     | Toon het [objectmenu](#object-menu) |

::: tip TIP: Snel veel objecten selecteren of verbergen

Tik op het selectiepictogram om één object te (de)selecteren, of sleep verticaal over de selectiekolom om veel objecten te selecteren. Met de zichtbaarheidskolom werkt het net zo.

Houd het selectie- of zichtbaarheidspictogram lang ingedrukt om ook de kinderen mee te nemen.

:::

### Kop van de boomstructuur {#tree-view-header}

De rij boven de lijst heeft een paar hulpmiddelen:

* ![](/icons/sort_down.webp) - alle groepen in één keer in- of uitklappen.
* ![](/icons/preview.webp) - de `Objectvoorbeelden` aan/uit: een kleine gerenderde miniatuur voor elk object in de lijst.
* ![](/icons/search.webp) - de lijst filteren op naam.

### Werken met de boomstructuur {#tree-view-manipulation}

Houd een item in de boomstructuur lang ingedrukt tot het oplicht. Je kunt het dan omhoog of omlaag verplaatsen in de boomstructuur, of het op een ander item slepen om het een kind van dat item te maken.

Als er veel items geselecteerd zijn, is er één de hoofdselectie; die wordt helderder weergegeven. Houd een van de items lang ingedrukt en sleep om alle geselecteerde objecten tegelijk te verplaatsen.

Selecteer je een ouder, dan worden standaard ook alle kinderen geselecteerd. Tik je nog eens op de ouder, dan wissel je tussen alleen de ouder selecteren en de ouder met zijn kinderen.

Dubbeltik op een item om de camera erop te richten (zie [Geavanceerd](#focus-on-item)).

### Objectmenu {#object-menu}

Tik in de boomstructuur op de knop met de drie puntjes (...) van een object om het objectmenu te openen. 
Veel van deze opties staan ook in de snelkoppelingsbalk bovenaan; ze zijn hier herhaald voor het gemak.

|       Actie         |                     Pictogram                      | Beschrijving                                                                                                                                                            |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Naam         |              ![](/icons/pencil.webp)           | Wijzig de naam van het object                                                                                                                                           |
| Instantie opheffen  |              ![](/icons/unlink.webp)           | Maak van een instantie een unieke vorm, zodat wijzigingen aan de vorm niet meer naar de andere instanties worden gekopieerd.                                            |
|      Instantie      |               ![](/icons/link.webp)            | Dupliceer het object als instantie: wijzigingen aan de vorm van de ene gelden dan voor alle instanties.                                                                 |
|       Klonen        |              ![](/icons/clone.webp)            | Dupliceer het object als nieuw object                                                                                                                                   |
|     Verwijderen     |              ![](/icons/trash.webp)            | Verwijder het object. Zijn kinderen blijven behouden, tenzij `Kinderen` is aangevinkt.                                                                                  |
|      Kinderen       |            ![](/icons/hierarchy.webp)          | Als dit is aangevinkt, werken `Instantie`, `Klonen` en `Verwijderen` ook op de kinderen van het object.                                                                 |
|  Splitsen op Delen  |             ![](/icons/separate.webp)          | Bestaat een object uit losse delen, dan wordt er voor elk deel een apart object gemaakt. Het omgekeerde van samenvoegen.                                               |
| Splitsen op Groepen |            ![](/icons/group.webp)          | Heeft een object meerdere vlakkengroepen, dan wordt er voor elke vlakkengroep een apart object gemaakt.                                                                     |
| Splitsen op Lagen   |              ![](/icons/layer.webp)            | Heeft een object lagen, dan worden er aparte objecten gemaakt voor de basismesh en voor elke laag. Handig om blendshapes naar andere apps te sturen.                   |
| Samenvoegen → Lagen | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Als er meerdere objecten met dezelfde topologie geselecteerd zijn, worden ze samengevoegd tot lagen van het hoofdobject (de andere objecten worden verwijderd). Ook dit is handig voor blendshapes die UIT andere apps komen.<br><br> Let op: de lagen zijn standaard uitgeschakeld. Schakel ze in als je hun schuifregelaars wilt aanpassen. |
|  Kromme (Repeater)  |              ![](/icons/curve.webp)            | Alleen voor een buis of een draaibank: voeg een [Kromme](#curve)-repeater toe die dezelfde curve volgt, als kind van het object.                                       |
|        Buis         |             ![](/icons/tube.webp)              | Bij een draaibank: voeg een [buis](tools.md#tube) toe die het profiel volgt, als kind. Bij een cilinder, kegel of torus: zet hem om naar een buis met dezelfde vorm, zodat je hem langs een curve kunt buigen. |




### Meervoudige selectie {#multiselection}
Je kunt meerdere objecten selecteren voor twee dingen:
- met het Gizmo-gereedschap meerdere objecten tegelijk verplaatsen
- objecten samenvoegen met samenvoegen en booleaanse bewerkingen.

Tik in de boomstructuur op het selectiepictogram van elk object, of sleep over de selectiekolom. Tik je op namen, houd dan de snelkoppeling `Masker` (of `Ctrl` op een toetsenbord) ingedrukt om één object toe te voegen of weg te halen, of de snelkoppeling `Gladstrijken` (of `Shift`) om alle objecten tussen het huidige en het aangetikte object te selecteren.

::: tip Snel meerdere objecten selecteren
Je kunt ook in de viewport meerdere objecten selecteren door de snelkoppeling `Gladstrijken` (of `Shift`) ingedrukt te houden en op een andere mesh te tikken.

Tik nog eens op een object om het te deselecteren (alleen als je selectie meer dan één object bevat).
:::

De gizmo verplaatst alle geselecteerde objecten samen, zie [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Samenvoegen {#join}
Deze optie maakt van meerdere geselecteerde objecten simpelweg één object.
Punten en UV's die dichter bij elkaar liggen dan de [lasradius](#weld-radius) worden samengevoegd.

Een voorbeeld in video vind je bij [Splitsen](#separate).

## ![](/icons/bool_subtract_circle.webp) Booleaans {#boolean}
![](/images/scene_boolean_menu.webp) 
Voeg objecten samen tot één oppervlak.

`Voxel samenvoegen` behoudt het volume van de objecten en berekent nieuwe, gelijkmatig verdeelde polygonen op het oppervlak. Dankzij die rekenstap kan voxel samenvoegen ook complexe geometrie aan, maar je kunt fijn detail verliezen als de gekozen resolutie niet hoog genoeg is.

`Booleaans` probeert de polygonen in hun oorspronkelijke indeling te laten en naait ze aan elkaar waar de objecten overlappen. Dat geeft vaak veel nettere en scherpere resultaten dan voxel samenvoegen, maar het vereist 'waterdichte' meshes: de objecten mogen geen gaten of misvormingen hebben. Lukt het niet, dan werkt voxel samenvoegen meestal wel.

### Booleaanse bewerkingen {#boolean-operations}
Zowel Voxel samenvoegen als Booleaans gebruiken de zichtbaarheid van de objecten om de bewerking te bepalen, zoals de geheugensteuntjes onderaan het venster aangeven:

#### Vereniging {#union}
Beide objecten zichtbaar geeft een booleaanse **vereniging**: de buitenhuid van de objecten wordt samengevoegd, zonder oppervlakken aan de binnenkant. ![](/images/boolean_union.webp)

#### Aftrekken {#subtract}
Eén object onzichtbaar = booleaans **aftrekken**: het onzichtbare object wordt van het zichtbare object afgetrokken. ![](/images/boolean_subtract.webp)

#### Intersectie {#intersect}
Beide objecten onzichtbaar = booleaanse **intersectie**: er ontstaat alleen een nieuwe vorm waar de twee objecten overlappen. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Voxel samenvoegen {#voxel-merge-button}
Deze knop voert een voxel-samenvoeging uit op de geselecteerde objecten. Doe je het op één object, dan krijgt het een nieuwe topologie met gelijkmatig verdeelde polygonen; handig als een object uitgerekte polygonen heeft. De opties hieronder werken net als die van de [Voxel-remesh](topology.md#voxel-remesher).

### Resolutie {#resolution}
De resolutie van het 3d-voxelraster dat voor de berekening wordt gebruikt. Verander je deze waarde, dan verschijnt er een dambordpatroon op het object als voorbeeld van de grootte van de polygonen.

De pipet naast de schuifregelaar neemt het detail over van de dichtheid van de mesh onder je vinger. Met de knop daarnaast zet je de schuifregelaar om naar `Randlengte`, een maat in de wereld: dezelfde waarde geeft dan hetzelfde detail op elk object.

### Multiresolutie opbouwen {#build-multiresolution}
Maak multiresolutieniveaus aan onder de gekozen resolutie. Is je resolutie bijvoorbeeld 400 en Multiresolutie opbouwen 3, dan krijg je een nieuwe mesh met zo'n 296.000 polygonen, maar daaronder 3 subdivisieniveaus met ongeveer 74.000, 18.500 en 4.600.

### Dunne delen verdikken {#thicken-thin-parts}
Maakt delen die te dun zijn voor het voxelraster dikker, zodat ze niet uit elkaar vallen. Niet beschikbaar in combinatie met `Scherpe randen` of `Scherpe grens`.

### Gaten {#holes}
Hoe gaten in open objecten vóór het samenvoegen worden gesloten:
* `Vullen` - elk gat wordt apart gesloten, vanaf de rand.
* `Vorm` - gaten worden gesloten door het omliggende oppervlak te volgen, en open stukken die elkaar overlappen worden samengevoegd.

### ![](/icons/angle.webp) Scherpe randen behouden {#keep-sharp-edges}
De knop `Scherpe randen` legt de voxelmesh op de scherpe randen van de objecten. Dit werkt het best bij eenvoudige vormen, en kan op sommige plekken vervorming geven.

### ![](/icons/group.webp) Scherpe grens {#sharp-border}
De nieuwe vlakken volgen de grenzen van de vlakkengroepen, en een grens blijft scherp waar het oppervlak erlangs een knik maakt.

### ![](/icons/group_separate.webp) Groepen gescheiden houden {#keep-groups-separate}
Elke vlakkengroep wordt apart geremesht: groepen smelten nooit samen, en elke groep blijft een gesloten stuk in zijn eigen groep. In deze modus wordt geen multiresolutie opgebouwd.

### ![](/icons/bool_subtract_circle.webp) Knop Booleaans {#boolean-button}
Deze knop voert een booleaanse bewerking op de polygonen uit met de Manifold-bibliotheek van Emmett Lalish. 

### ![](/icons/bool_unite_circle.webp) Overlapping opschonen {#clean-overlaps}
Is er maar één object geselecteerd, dan wordt de knop `Booleaans` de knop `Overlapping opschonen`: die voegt de delen van het object die elkaar doorsnijden samen tot een net oppervlak.


## ![](/icons/separate.webp) Splitsen {#separate}
Bestaat één object uit meerdere losse delen, dan kun je het opsplitsen in meerdere objecten. 
Je kunt dit zien als het omgekeerde van [Samenvoegen](#join).

Het venster `Splitsen...` biedt drie manieren om de geselecteerde objecten te splitsen:
* `Splitsen op Delen` - maak een apart object voor elk los deel.
* `Splitsen op Groepen` - maak een apart object voor elke vlakkengroep.
* `Splitsen op Lagen` - maak aparte objecten voor de basismesh en voor elke laag.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Toevoegen {#add-menu}

![](/images/scene_addmenu_overview.webp)

Met dit menu maak je primitieven, groepen, camera's, repeaters en lichten.

Primitieven zijn basisvormen die je met parameters kunt aanpassen. Is het primitief naar wens, dan 'voltooi' je het: de parameters worden dan vastgelegd in een polygoonmesh die je kunt boetseren en beschilderen. Na het voltooien kun je de parameters van een primitief niet meer aanpassen.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Op de Gizmo {#on-gizmo}
Plaats het nieuwe primitief op de plek van de geselecteerde vorm of van de gizmo. Staat dit uit, dan komt het primitief in het midden van de scène.

### ![](/icons/gizmo.webp) Selecteer Gizmo {#select-gizmo}
Schakel automatisch over naar het Gizmo-gereedschap als er een nieuw primitief is gemaakt. 

### ![](/icons/cog.webp) Geavanceerd {#add-advanced}

In dit menu stel je in waar nieuwe primitieven, groepen en repeaters worden aangemaakt: op het geselecteerde object, in de oorsprong van de wereld, of op de plek van de gizmo.


### UV's {#uvs}
Met de schakelaar `UVs` naast de titel Primitief krijgen primitieven UV's. UV's (vaak textuurcoördinaten genoemd) zijn extra gegevens die in 3d worden gebruikt om texturen op oppervlakken aan te brengen. Ze kosten meer geheugen, maar op de meeste apparaten hoef je je daar geen zorgen over te maken, tenzij je met heel veel polygonen werkt (bijvoorbeeld 10 miljoen of meer). 

### Primitieven {#primitives}

| Primitief      | Pictogram                                 | Beschrijving                                                                                                    |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Doos           | ![](/icons/cube.webp)                    | Een eenvoudige kubus; je bepaalt de verdeling in X, Y en Z                                                      |
| Quadbol        | ![](/icons/circle.webp)                  | Een onderverdeelde doos met de optie `Bol` geforceerd, dus met een gelijkmatige indeling van quads die goed is om te boetseren |
| Cilinder       | ![](/icons/cylinder.webp)                | Je kunt de cilinder een gat in het midden geven, bijvoorbeeld om een holle buis te maken                        |
| Torus          | ![](/icons/torus.webp)                   | De torus is een goed beginpunt voor ringen                                                                      |
| Kegel          | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosaëder      | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-bol         | ![](/icons/circle.webp)                  | Een bol met een ongelijkmatige indeling van polygonen, zie de [waarschuwing hieronder](#uv-sphere)              |
| Vlak           | ![](/icons/rectangle.webp)               | Een eenvoudig vlak; let op: dit is het enige primitief dat niet gesloten is                                     |
| Tekst          | ![](/icons/text.webp)                    | 3d-tekst, met een lettertype, een stijl, een uitlijning, een diepte en een buiging. `Letters samenvoegen` laat letters die elkaar raken samensmelten |
| Buis           | ![](/icons/tube.webp)                    | zie [Buis](tools#tube)                                                                                          |
| Draaibank      | ![](/icons/lathe.webp)                   | zie [Draaibank](tools#lathe)                                                                                    |
| Triplanar      | ![](/icons/triplanar.webp)               | zie [Triplanar](#triplanar)                                                                                     |
| VDM            | ![](/icons/vdm.webp)                     | Een vlak dat klaarstaat om een vector-displacementstempel te boetseren: het heeft UV's en staat naar de camera gericht |
| Schaduw Vanger | ![](/icons/material_shadow_catcher.webp) | zie [Schaduw Vanger](#shadow-catcher)                                                                           |
| Hoofd          | ![](/icons/face.webp)                    | Een eenvoudig hoofd met een laag om te mengen tussen man en vrouw                                               |

::: tip
Vraag je je af wat de basismesh is waarmee Nomad opstart? Dat is ook een onderverdeelde doos.
De basismesh van Nomad gebruikt echter geen `Bol`, en is dus niet perfect rond.
:::

### Werkbalk van het primitief {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Zodra je een primitief hebt gemaakt, verschijnt er een werkbalk om de parameters ervan te regelen.

* `Voltooien` Zet het primitief om naar een gewoon object, zodat je het kunt boetseren en beschilderen.
* `Spiegel` Plaats een spiegel-repeater boven het primitief, of haal hem weg.
* `Alle` (oogpictogram) Kies welke grepen direct op het primitief worden getoond om de parameters te regelen, bijvoorbeeld de breedte van de kubus of de straal van het gat in een cilinder: `Geen`, `Alle`, of maar één soort (straal, gat, profiel...), afhankelijk van het primitief.
* `Verdeling` Het aantal verdelingen van het primitief, hier langs X voor een doos.
* `Constante dichtheid` Rek je het primitief met de gizmo langs één as uit, dan groeien de grootte en de verdelingen mee in plaats van dat de polygonen worden uitgerekt, zodat de vlakken vierkant blijven. Beschikbaar voor dozen, vlakken en cilinders.
* `...` Toont het menu van het primitief.

Sommige primitieven hebben extra opties op de werkbalk:

* `Bol` De bol is opgebouwd als onderverdeelde kubus, omdat dat beter boetseert, maar daardoor is hij niet perfect rond. Deze optie brengt de vorm dichter bij een perfecte bol. De icosaëder heeft deze optie ook.
* `Deksel` Zet eindkappen op een vorm aan of uit; een cilinder kan bijvoorbeeld een kap aan de boven- of onderkant hebben, aan beide kanten, of geen.
* `Gat` Maak een gat door het midden van een vorm. Je wisselt tussen geen gat, een gat met één straal, of een gat met een andere straal boven en onder.
* `Radius` Kies of een cilinder één straal heeft, of een andere straal aan de boven- en onderkant.
* `Schijf` Kies of een vlak vierhoekig of rond is.

Met de kleine werkbalk onder de hoofdwerkbalk wissel je tussen de gizmo van het primitief en de transformatie-gizmo.

::: tip

Tik op de titel van de werkbalk om hem naar de boven- of onderkant van het scherm te verplaatsen. Tik op het pijltje in de hoek om hem in te klappen.

:::


### Menu van het primitief {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Dit bevat alle parameters van het geselecteerde primitief. Parameters zijn de basisbeschrijving van een vorm. Een ring beschrijf je bijvoorbeeld met zijn buitenstraal, zijn binnenstraal en het aantal polygonen.

De meeste parameters van primitieven spreken voor zich, en een paar zijn voor alle primitieven gelijk:

* `UVs` Met de kleine knop UVs bovenaan het menu zet je het aanmaken van UV-coördinaten aan of uit
* `Voltooien` Met de kleine knop Voltooien zet je het primitief om naar een gewoon object, zodat je het kunt boetseren en beschilderen.
* `Max. vlakken` Stel een bovengrens in voor het aantal polygonen in het object, zodat je apparaat niet vastloopt.
* `Naderhand onderverdelen` Pas het gekozen aantal subdivisies toe uit het onderdeel Multiresolutie van het topologiemenu. Samen met een lage verdeling in de topologie kun je zo gladde primitieven met zachte hoeken maken. Zet je bijvoorbeeld de topologieverdeling van een doos op 2 en het naderhand onderverdelen op 4, dan krijg je een doos met afgeronde hoeken.
* `Lineaire subdivisie` Stel in hoeveel lineaire subdivisieniveaus er worden gebruikt vóór de gewone, gladde subdivisie. Zo bepaal je hoe scherp of zacht de hoeken van het onderverdeelde oppervlak worden. Zet bijvoorbeeld de topologieverdeling van een doos op 2 en het naderhand onderverdelen op 4, en verander dan de lineaire subdivisie tussen 0 en 4. De hoeken van de doos gaan van zacht naar scherp.

### Topologie {#topology}

Dit regelt het aantal polygonen van een primitief. Meestal zijn de regelaars gekoppeld, zodat één actieve schuifregelaar alle polygonen gelijkmatig aanpast. Tik op de ontkoppelknop om de verdelingen in X/Y/Z van een vorm apart te regelen.

### Geometrie {#geometry}

Dit regelt de totale grootte van een primitief: in X/Y/Z-eenheden voor hoekige vormen, en als straal voor ronde vormen.


### ![](/icons/circle.webp) UV-bol {#uv-sphere}
::: warning
De UV-bol is niet zo geschikt om te boetseren, vooral niet bij de polen.

Kies liever het [primitief](#primitives) Quadbol, Doos of Icosaëder, samen met de optie `Bol`.

Let op: de topologie kan wel geschikt zijn om te boetseren als je de schuifregelaars `Verdeling` op een heel lage waarde zet.
Daarna kun je met de schuifregelaar `Naderhand onderverdelen` het aantal polygonen verhogen.

Al is hij niet geschikt om in het algemeen te boetseren, voor ogen is hij wel handig: draai je de bol zo dat de polen bij de pupil liggen, dan past de indeling van de polygonen vanzelf goed bij het schilderen en boetseren van iris en pupil.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Dit primitief is bijzonder: je gebruikt het [Masker-gereedschap](tools.md#mask) erop om de geometrie vorm te geven.

![](/videos/triplanar.mp4)


::: tip
Dubbeltik op een vlak en de camera richt zich op dat vlak.
Dat werkt echter niet als je het primitief met de gizmo hebt gedraaid.
:::

Triplanar gebruikt de maskerinformatie van 3 vlakken om een voxelraster te vullen, dat daarna wordt omgezet naar polygonen (dankzij de [Voxel-remesh](topology.md#voxel-remesher)).

Elk vlak heeft zijn eigen symmetrievlak.

::: warning
Elke keer dat je de grootte van het Triplanar-primitief verandert, gaat de kwaliteit van het geschilderde masker achteruit.

Voorlopig kun je het schilderen niet tot één vlak 'beperken', maar misschien komt dat in de toekomst.
De optie [Verbonden topologie](stroke.md#connected-topology) helpt een beetje: als je cursor precies op één vlak ligt, heeft hij geen invloed op de andere vlakken.
:::

### ![](/icons/material_shadow_catcher.webp) Schaduw Vanger {#shadow-catcher}
Voeg een vlak toe met het materiaal Schaduw Vanger. Zie [Materiaal Schaduw Vanger](material.md#shadow-catcher) voor meer details. 


## Groep/Camera {#groupcamera}
### ![](/icons/share.webp) Groep {#group}
Maak een 'leeg' object waaronder je andere objecten kunt hangen. Zo kun je de hiërarchie overzichtelijk houden door veel objecten onder een groep te zetten en die dan in te klappen. Een groep is ook handig om objecten te verplaatsen: zet veel objecten onder een groep, en verplaats, draai of schaal dan de groep met het Gizmo-gereedschap.

### ![](/icons/camera.webp) Camera {#add-view}
Maak een camera.

## Repeaters {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeaters zijn knooppunten die instanties maken van de objecten eronder. 

### ![](/icons/array.webp) Array {#array}
![](/images/scene_primitive_array.webp)

Objecten die je als kind onder dit knooppunt zet, kunnen als instanties in een raster worden geplaatst. Als het geselecteerd is, heeft het regelaars voor:
* `Binnen inpassen` - staat dit aan, dan worden alle kopieën binnen de grenzen van de array geplaatst; staat het uit, dan bepalen de schuifregelaars de ruimte tussen de kopieën
* `Aantal X/Y/Z` - het aantal instanties op elke as
* `Grootte X/Y/Z` - de grootte van het raster langs elke as, of de afstand tussen de kopieën als `Binnen inpassen` uit staat
* `Willekeurig...` - voegt willekeurige variaties toe aan de kopieën, zie [Willekeurig](#curve) hieronder.

### ![](/icons/curve.webp) Kromme {#curve}
![](/images/scene_primitive_curve.webp)
Dit maakt een curve; de kinderen van dit knooppunt worden langs de curve herhaald. Als het geselecteerd is, heeft het regelaars voor:
* `Kromme` - bewerk de curve: voeg punten toe aan de curve en verplaats punten op de curve.
* `Tonen` - toon of verberg de curve en haar punten.
* `Snap` - laat de punten van de curve vastklikken aan andere geometrie.
* `Sym` - bewerk de curve symmetrisch.
* `Gesloten` - verbind het begin en het einde van de curve, of laat haar open.
* `B-spline` - laat de instanties de curve precies volgen, of gebruik B-spline-interpolatie voor een vloeiender resultaat.
* `Vervormen` - buig elke kopie langs de curve, zodat de kopieën op hun buren aansluiten (`Vloeiend` buigt hun zijkanten zodat ze zonder hoek op elkaar aansluiten).
* `Uitlijnen` - draai de kopieën mee met de richting van de curve.
* `Draaipunt` - het draaipunt van de kopieën: de curve zelf (`Zelf`) of haar kinderen.
* `Aantal` - het aantal instanties. Met de modusknop ernaast schakel je over naar `Afstand`: een vaste ruimte tussen de kopieën, waarbij het aantal de lengte van de curve volgt.
* `Radius` - regelaars op elk punt van de curve om de schaal van de instanties in te stellen.
* `Draai` - regelaars op elk punt van de curve om de draaiing van de instanties in te stellen.
* `Afwisselen` - draai om de andere kopie rond de curve: 90° voor kettingschakels, 180° voor bladeren of ritstanden, rond de `As` die je kiest.
* `Spiraal...` - wind de kopieën rond de curve, in meerdere strengen (touw, vlecht, lint...).
* `Willekeurig...` - voeg willekeurige variaties toe aan de kopieën; elke rij kan in plaats daarvan bij elke kopie dezelfde hoeveelheid toevoegen.

Onder de werkbalk voegt de schakelaar `(samenvoegen)` een punt samen met een ander punt als je het erop sleept. Met `IK` (inverse kinematica) kun je de curve poseren: sleep een punt en de verbonden punten volgen. Tik op een punt om het te vergrendelen of te ontgrendelen, of houd lang ingedrukt om ze allemaal te vergrendelen of ontgrendelen; vergrendelde punten blijven op hun plek.

### ![](/icons/radial.webp) Radiaal {#radial}
![](/images/scene_primitive_radial.webp)

De kinderen van dit knooppunt worden als instanties in een cirkel geplaatst. Verplaats het kindobject om de straal van deze repeater te veranderen. Als het geselecteerd is, heeft het regelaars voor:
* Radiaal X/Y/Z - met deze knoppen kies je de as van de cirkel en stel je het aantal instanties in.



### ![](/icons/mirror.webp) Spiegelen {#mirror}
![](/images/scene_primitive_mirror.webp)

De kinderen van dit knooppunt worden gespiegeld langs een as. Als het geselecteerd is, heeft het regelaars voor:
* Gizmo - zet de transformatie-gizmo aan om het midden van de spiegeling in te stellen. Je kunt hem ook draaien en schalen. Ben je klaar, tik dan nog eens op Gizmo om de gewone regelaars terug te krijgen.
* X/Y/Z - kies het spiegelvlak

### ![](/icons/surface.webp) Oppervlak {#surface}

De kinderen van dit knooppunt worden op het oppervlak van een object gekopieerd: één kopie per vlak, per rand of per vertex, of willekeurig verspreid. Als het geselecteerd is, heeft het regelaars voor:
* Modus - plaats de kopieën op de `Vlakken`, de `Randen` of de vertices, of `Verspreiden` ze.
* Elke - één kopie per N vlakken, randen of vertices. `Willekeurig` kiest ze in plaats daarvan willekeurig, en `Herschikken` trekt een nieuwe willekeurige set.
* Tussenruimte - bij het verspreiden de minimale afstand tussen twee kopieën.
* Uitlijnen - de kopieën staan op het oppervlak en volgen de normaal ervan, in plaats van de oriëntatie van het origineel te behouden.
* Vastklikken - projecteer het origineel op het dichtstbijzijnde punt van het oppervlak; de kopieën volgen.
* Grootte aanpassen, Scheef - schaal de kopieën en rek ze uit naar de vorm van elk vlak.
* Vervormen - buig elke kopie op haar vlak, of langs haar rand, zodat naburige kopieën zonder kieren op elkaar aansluiten.

Alle repeaters hebben een regelaar `Voltooien`, die het resultaat van de repeater vastlegt en vraagt hoe dat moet:
* Kinderen samenvoegen - de instanties worden samengevoegd tot één object
* Instanties behouden - de instanties blijven instanties, maar hebben de repeater niet meer als 'ouder'
* Instantie opheffen - de instanties worden omgezet naar unieke objecten

`Alles afvlakken` legt ook de repeaters vast die in deze repeater genest zijn, zodat elke kopie een gewoon object wordt.

::: tip Tip: Repeaters combineren
Repeaters kun je onder elkaar hangen, en je kunt meerdere objecten kind van repeaters maken. Zo krijg je complexe effecten.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Draaipunten van repeaters

Sommige repeaters proberen het draaipunt van de kindobjecten automatisch in te stellen, zodat ze niet bewegen, ook niet als je ze met het Gizmo-gereedschap verplaatst of draait. Wil je dat omzeilen, zet dan een groep tussen de repeater en het kind. Nu kun je de kindvorm los van de repeater verplaatsen.
:::

## Licht {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Directioneel {#directional}
Maak een directioneel licht: een oneindig ver weg gelegen lichtbron, zoals de zon.

### ![](/icons/panorama.webp) Omgeving {#environment}
Maak een omgevingslicht, dat de scène belicht met een afbeelding die er helemaal omheen ligt (beeldgebaseerde belichting, zoals een HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Maak een spotlicht, met regelaars voor de breedte en de zachtheid van de lichtkegel

### ![](/icons/light.webp) Punt {#point}
Maak een puntlicht

## ![](/icons/cog.webp) Geavanceerd {#advanced}
De knop `Geavanceerd` linksonder in het paneel opent een venster met twee tabbladen: `Algemeen` en `Synchroniseren`.

### ![](/icons/focus.webp) UI: Focus op item bij dubbele tik {#focus-on-item}
Dubbeltik op een item in de scènelijst om de camera in de 3d-weergave op dat item te richten.

### ![](/icons/eye_open.webp) Synchroniseer zichtbaarheid {#sync-visibility}
Staat dit aan, dan werkt het oogpictogram van een geselecteerd item op alle geselecteerde items. 

### ![](/icons/bang.webp) Markering {#highlight}
Markeert de geselecteerde objecten in de viewport als de selectie verandert.

### ![](/icons/link.webp) Tonen (Instantie) {#instance-show}
Toon een gekleurd capsuletje links in de scènelijst om instanties aan te geven.

### ![](/icons/preview.webp) Objectvoorbeelden {#object-previews}
Toon een gerenderde miniatuur voor elk object in de scènelijst. Hetzelfde als de voorbeeldknop boven de lijst.

### Lasradius {#weld-radius}
Onder de titel `Samenvoegen`: `Positie-lasradius` en `UV-lasradius`. Punten en UV's die dichter bij elkaar liggen dan deze straal, worden samengevoegd. Elk kun je uitzetten met het selectievakje. Dit geldt voor Samenvoegen, Booleaans, Trim, Decimeren, remeshen en het importeren van bestanden.

### Iconen {#icons}
Stel de minimale en maximale `Grootte` en de `Dekking` in van de pictogrammen van groepen, lichten, camera's en repeaters in de viewport.

### ![](/icons/hierarchy.webp) Hiërarchische lijnen {#hierarchy-lines}
Toon in de viewport een lijn tussen een ouder en zijn kinderen. Staat dit aan, dan kun je ook instellen:
* `Gebruik Nomad pivot` - de lijnen beginnen bij het draaipunt dat de gereedschappen Transformeren en Gizmo gebruiken. Staat dit uit, dan gebruiken ze het natuurlijke basisdraaipunt, dat ver van het midden van het object kan liggen.
* `Dikte` - de breedte van de lijnen. De knop naast de schuifregelaar geeft ze een contour.
* De kleur van de lijnen.

### ![](/icons/link.webp) Synchroniseren {#sync}
In het tabblad `Synchroniseren` stel je per bewerking (`Toevoegen`, `Verwijderen`, `Vergrendelen`, `Klonen`, `Instantie`, `Instantie opheffen`, `Samenvoegen`, `Splitsen` en `Booleaans`) in of ze voor alle instanties van de selectie geldt:
* `Auto` - volg het vakje `Synchroniseren` bovenaan het scènemenu.
* `Nee` - alleen de geselecteerde objecten.
* `Ja` - altijd alle instanties.

Standaard staan `Samenvoegen`, `Splitsen` en `Booleaans` op `Ja` en de andere op `Auto`. Met `Herstellen` zet je deze standaardwaarden terug.

## Onderste werkbalk {#bottom-toolbar}
Met deze pictogrammen zet je de weergave van groepen, lichten, camera's, repeaters en hiërarchische lijnen in de viewport aan of uit. Pictogrammen op het canvas kun je aantikken om ze direct te selecteren en te bewerken.
