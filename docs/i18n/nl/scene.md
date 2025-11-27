# ![](/icons/scene.webp) Scène 

Met dit menu kun je objecten, lichten, camera’s en repeaters beheren in Nomad. Het toont de scène-hiërarchie als een boomstructuur, zodat je veel aspecten van je objecten kunt aanpassen. Je kunt er ook nieuwe objecten mee maken, en objecten op verschillende manieren samenvoegen en splitsen.


![](/images/scene_menu_summary.webp)


## Snelkoppelingenbalk
| Actie                 | Icoon                             | Beschrijving                                                                                                       |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Toevoegen...](#add-menu)    | ![](/icons/plus.webp)            | Toon het [Toevoegen-menu](#add-menu) om een object aan de scène toe te voegen                                      |
| Verwijderen           | ![](/icons/trash.webp)           | Verwijder het object                                                                                               |
| Vergrendelen          | ![](/icons/lock.webp)            | Maak het object niet-selecteerbaar in de viewport. Het kan nog steeds geselecteerd worden in de boomweergave.     |
| Samenvoegen           | ![](/icons/merge.webp)           | Voeg de geselecteerde objecten samen tot één object zonder geometrie te wijzigen                                   |
| Splitsen              | ![](/icons/diagonal.webp)        | Als een object uit unieke polygoonschillen bestaat, splits het dan in afzonderlijke objecten. Het omgekeerde van samenvoegen |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | Toon het [Boolean](#boolean)-menu                                                                                  |
| Kloon                 | ![](/icons/clone.webp)           | Dupliceer het object naar een nieuw object                                                                         |
| Instantie             | ![](/icons/link.webp)            | Dupliceer het object als een instantie, zodat modelleerwijzigingen op één instantie op alle instanties worden toegepast. |
| De-instantiëren       | ![](/icons/unlink.webp)          | Zet een instantie om in een unieke vorm, zodat modelleerwijzigingen niet langer naar andere instanties worden gekopieerd |
| Sync                  | ![](/icons/link.webp)            | Als instanties kinderen hebben, zorg ervoor dat alle instanties dezelfde kind-hiërarchie delen                     |


## Boomweergave
![](/images/scene_treeview.webp) 

| Actie        | Icoon                      | Beschrijving              |
| :----------: | :------------------------: | :----------------------: |
| Selecteren   | ![](/icons/checked.webp)  | Schakel geselecteerd/niet-geselecteerd |
| Zichtbaar    | ![](/icons/eye_open.webp) | Schakel zichtbaarheid    |
| Menu         | ![](/icons/more.webp)     | Toon objectmenu          |

::: tip TIP: Snel veel objecten selecteren of verbergen

Tik op het selecteericoon om één object te schakelen, of sleep verticaal over de selectiekolom om veel objecten te selecteren. Hetzelfde kan met de zichtbaarheidkolom.

:::

### Manipulatie van de boomweergave

Houd een item in de boomweergave lang ingedrukt tot het geel wordt. Je kunt het dan omhoog of omlaag verplaatsen in de boomweergave, en het over een ander item slepen om er een kind van te maken.

Wanneer veel items geselecteerd zijn, zullen de meeste donkergeel zijn en één lichtgeel. Houd het lichte item lang ingedrukt en sleep om alle objecten tegelijk te verplaatsen.

Wanneer je een ouderitem selecteert, worden standaard alle kinditems ook geselecteerd. Tikken op het oudericoon schakelt tussen alleen de ouder selecteren, of de ouder plus kinderen.

### Objectmenu

Klikken op de ellipsknop (...) voor een object in de boomweergave toont het objectmenu. 
Veel van deze opties lijken op de snelkoppelingenbalk bovenaan, herhaald voor het gemak.

|       Actie        |                        Icoon                        | Beschrijving                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instantie      |               ![](/icons/link.webp)            | Dupliceer het object als een instantie, zodat modelleerwijzigingen op één instantie op alle instanties worden toegepast.                                                |
|        Kloon        |              ![](/icons/clone.webp)            | Dupliceer het object naar een nieuw object                                                                                                                              |
|        Naam         |              ![](/icons/pencil.webp)           | Wijzig de naam van het object                                                                                                                                           |
|       Verwijderen   |              ![](/icons/trash.webp)            | Verwijder het object                                                                                                                                                    |
|       Verwijderen+  |            ![](/icons/removeNode.webp)         | Verwijder het object en zijn kinderen                                                                                                                                   |
|     De-instantiëren |              ![](/icons/unlink.webp)           | Zet een instantie om in een unieke vorm, zodat modelleerwijzigingen niet langer naar andere instanties worden gekopieerd.                                              |
|  Topologie splitsen |             ![](/icons/separate.webp)          | Als een object uit unieke polygoonschillen bestaat, splits het dan in afzonderlijke objecten. Het omgekeerde van de samenvoegbewerking.                                |
| Face Group splitsen |            ![](/icons/faceGroup.webp)          | Als een object meerdere face groups heeft, splits het mesh dan in afzonderlijke objecten.                                                                               |
|   Lagen splitsen    |              ![](/icons/layer.webp)            | Als een object lagen heeft, splits elke laag in een afzonderlijk object. Handig om blendshapes naar andere applicaties te sturen.                                      |
|   Samenvoegen -> Lagen   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Als meerdere objecten geselecteerd zijn en overeenkomende topologie hebben, voeg die objecten samen als lagen van het primaire object (de andere objecten worden verwijderd). Opnieuw handig voor blendshapes die VANUIT andere applicaties komen.<br><br> Merk op dat de lagen standaard uitgeschakeld zijn. Schakel ze in als je hun schuifregelaars wilt aanpassen. |




### Meervoudige selectie
Je kunt meerdere objecten selecteren om twee dingen te doen:
- het gizmo-gereedschap gebruiken om meerdere objecten tegelijk te verplaatsen
- objecten samenvoegen met join- en boolean-bewerkingen.

Dit kun je doen door het selectievakje `Multiselection` te gebruiken en vervolgens op het object in de lijst te klikken.

::: tip Snelle meervoudige selectie
Je kunt ook in de viewport multiselecteren door de `Smooth`-snelkoppeling ingedrukt te houden en op een andere mesh te tikken.

Je kunt een object deselecteren door er opnieuw op te tikken (alleen als je selectie meer dan één object bevat).
:::

::: warning Beperkte gizmo-functionaliteit
Bij meervoudige selectie negeert het gizmo-gereedschap altijd masking.
Ook X/Y/Z-scaling is uitgeschakeld.

De reden is dat meervoudige selectie alleen transformatie van de volledige mesh toestaat, niet per vertex.
Dit kan in de toekomst verbeterd worden.
:::


## Samenvoegen
Deze optie maakt simpelweg één enkel objectitem van meerdere geselecteerde objecten.

Je kunt een voorbeeld in video zien in de sectie [Splitsen](#separate).

## Boolean
![](/images/scene_boolean_menu.webp) 
Combineer objecten tot één oppervlak.

`Voxel merge` behoudt het volume van de objecten en berekent nieuwe gelijkmatig verdeelde polygonen op het oppervlak. Door de berekeningsstap kan een voxel merge complexe geometrie aan, maar kan fijne details verliezen als de doelresolutie niet hoog genoeg is.

`Boolean` probeert de polygonen in hun oorspronkelijke indeling te laten en de polygonen aan elkaar te hechten waar objecten overlappen. Dit kan veel schonere en scherpere resultaten geven dan een voxel merge, maar vereist ‘waterdichte’ meshes; er mogen geen gaten of misvormde vormen in de objecten zitten. Als dit faalt, werkt een voxel merge meestal wel.

### Boolean-bewerkingen
Zowel Voxel Merge als Boolean gebruiken de zichtbaarheid van objecten om de bewerking te bepalen:

#### Unie
Beide objecten zichtbaar resulteert in een boolean-**unie**, de buitenste huid van de objecten wordt gecombineerd, zonder binnenste oppervlakken. ![](/images/boolean_union.webp)

#### Aftrekken
Eén object onzichtbaar = boolean-**aftrekken**, het onzichtbare object wordt afgetrokken van het zichtbare object. ![](/images/boolean_subtract.webp)

#### Doorsnede
Beide objecten onzichtbaar = boolean-**doorsnede**, maak een nieuwe vorm alleen waar de twee objecten overlappen. ![](/images/boolean_intersect.webp)


### Voxel Merge-knop
Op deze knop drukken voert een voxel merge-bewerking uit op de geselecteerde objecten. Bij één enkel object wordt het geretopologiseerd naar gelijkmatig verdeelde polygonen, handig wanneer een object uitgerekte polygonen heeft.

### Resolutie
De resolutie van het voxel-3D-raster dat voor de berekening wordt gebruikt. Wanneer deze waarde wordt gewijzigd, wordt een dambordpatroon over het object gelegd om de grootte van de polygonen te tonen.

### Multiresolution opbouwen
Maak multiresolutieniveaus onder je doelresolutie. Dus als je resolutie 400 is en multiresolution opbouwen is 3, krijg je een nieuwe mesh met bijvoorbeeld 296.000 polygonen, maar er zullen 3 lagere subdiv-niveaus zijn op 74.000, 18.000, 4.000k.

### Scherpe randen behouden
Schakel het vastklikken van het voxelmesh op randen in. Dit werkt het best op eenvoudige vormen.

### Boolean-knop
Op deze knop drukken voert een polygon-boolean-bewerking uit met behulp van de Manifold-bibliotheek van Emmett Lalish. 


## Splitsen
Als je één object hebt dat uit meerdere niet-verbonden delen bestaat, kun je dit object splitsen in meerdere objecten. 
Dit kan worden gezien als het tegenovergestelde van [Eenvoudig samenvoegen](#simple-merge).

![](/videos/merge_separate.mp4)


## Toevoegen-menu

![](/images/scene_addmenu_overview.webp)

Dit menu maakt primitieven, groepen, camera’s, repeaters en lichten.

Primitieven zijn basisvormen die met parameters kunnen worden aangepast. Zodra je de primitieve naar wens hebt ingesteld, ‘valideer’ je hem, wat die parameters omzet naar een polygonmesh dat gesculpt en geverfd kan worden. Een primitieve kan niet meer via parameters worden aangepast nadat hij is gevalideerd.


![](/images/scene_addmenu_top.webp)

### Op gizmo
Schakel in om de nieuwe primitieve te plaatsen waar de huidige geselecteerde vorm of het gizmo zich bevindt. Wanneer uitgeschakeld, wordt de primitieve in het midden van de scène geplaatst.

### Gizmo selecteren
Schakel automatisch overschakelen naar het gizmo-gereedschap in wanneer een nieuwe primitieve wordt gemaakt. 

### Geavanceerd

Met dit menu kun je je voorkeur instellen voor waar nieuwe primitieven, groepen en repeaters worden gemaakt. Ze kunnen op het geselecteerde object, op de wereldorigin of op de locatie van het gizmo worden geplaatst.


### UV’s
Schakel UV’s in op primitieven. UV’s (vaak textuurcoördinaten genoemd) zijn extra gegevens die in 3D worden gebruikt om texturen op oppervlakken toe te passen. Ze nemen meer geheugen in, maar voor de meeste apparaten is dit geen probleem, tenzij je in zeer hoge poly-aantallen komt (bijv. 10 miljoen polys of meer). 

### Primitieven

| Primitief      | Icoon                                     | Beschrijving                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Een eenvoudige kubus; je kunt de verdeling in X, Y en Z regelen                                                 |
| Sphere         | ![](/icons/circle.webp)                  | Voor het gemak Sphere genoemd, maar het is eigenlijk een gesubdivideerde box, met `Project on sphere` geforceerd |
| Cylinder       | ![](/icons/cylinder.webp)                | Je kunt een gat in het midden toevoegen aan de cylinder-primitieve, bijvoorbeeld om een holle pijp te maken     |
| Torus          | ![](/icons/torus.webp)                   | De torus kan een goed startpunt zijn voor ringen                                                                |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-sphere      | ![](/icons/circle.webp)                  | Een sphere met ongelijke poly-indeling, zie [Waarschuwing hieronder](#uv-sphere)                                |
| Plane          | ![](/icons/rectangle.webp)               | Een eenvoudige plane; dit is de enige primitieve die niet gesloten is                                           |
| Tube           | ![](/icons/tool_tube.webp)               | zie [Tube](tools#tube)                                                                                          |
| Lathe          | ![](/icons/tool_lathe.webp)              | zie [Lathe](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | zie [Triplanar](#triplanar)                                                                                     |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | zie [Shadow Catcher](#shadow-catcher)                                                                           |
| Head           | ![](/icons/face.webp)                    | Een eenvoudige kop met een laag om tussen mannelijk/vrouwelijk te blenden                                       |

::: tip
Als je je afvraagt wat de basismesh is wanneer je Nomad start: dit is ook een gesubdivideerde box.
De basismesh in Nomad gebruikt echter geen `Project on sphere`, wat betekent dat hij niet perfect rond is.
:::

### Primitieve werkbalk

![](/images/scene_primitive_toolbar.gif)

Zodra een primitieve is gemaakt, verschijnt er een werkbalk om de parameters te regelen.

* `Validate` Bak de primitieve om tot een standaardobject zodat het gesculpt en geverfd kan worden.
* `Edit` Schakel het tonen van het primitieve-gizmo. Dit wordt direct op de primitieve getoond om de parameters te regelen, bijvoorbeeld de breedte van de kubus of de straal van een cilinderopening.
* `Mirror` Schakel het plaatsen van een mirror-repeater boven de primitieve.
* `...` Toont het primitieve-menu.

Verschillende primitieven hebben extra opties op de werkbalk:

* `Project` De sphere is geconstrueerd als een gesubdivideerde kubus, wat beter is om op te sculpten, maar betekent dat hij niet perfect rond is. Deze optie dwingt de vorm dichter naar een perfecte sphere. De icosahedron deelt deze optie.
* `Cap` Schakel eindkappen op een vorm, bijvoorbeeld een cilinder kan kappen hebben boven, onder, beide of geen.
* `Hole` Schakel een gat door het midden van een vorm. Dit doorloopt geen gat, gat met één straal, of gat met verschillende straal boven en onder.
* `Radius` Schakel of een cilinder één straal moet hebben, of een andere straal boven en onder.
* `Disk` Schakel of een plane een 4-zijdige vorm moet zijn, of een cirkelvorm.

De kleine werkbalk onder de hoofdwerkbalk laat je schakelen tussen het primitieve-gizmo en het transform-gizmo.

::: tip

Klikken op de titel van de werkbalk schakelt hem naar de boven- of onderkant van het scherm. Klikken op de pijl in de hoek klapt hem in.

:::


### Primitieve-menu

![](/images/scene_primitive_menu.webp)

Dit bevat alle parameters voor de geselecteerde primitieve. Parameters zijn de basisbeschrijvingen van een vorm. Om bijvoorbeeld een ring te beschrijven, zou je de buitenstraal, de binnenstraal en het aantal polygonen beschrijven.

De meeste primitieveparameters spreken voor zich, en er zijn enkele gemeenschappelijke parameters die alle primitieven delen:

* `UVs` De kleine UVs-knop bovenaan het menu schakelt het aanmaken van UV-coördinaten
* `Validate` De kleine validate-knop bakt de primitieve om tot een standaardobject zodat het gesculpt en geverfd kan worden.
* `Max faces` Stel een bovengrens in voor het aantal polygonen in het object om te voorkomen dat je apparaat crasht.
* `Post subdivision` Schakel het gekozen aantal subdivisieniveaus in uit de multiresolution-sectie van het topologiemenu. Dit kan worden gebruikt om gladde, zacht afgeronde primitieven te maken in combinatie met lage topologieverdelingen. Bijvoorbeeld: zet de box-topologieverdelingen op 2 en post subdivisions op 4 om een box met zachte hoeken te maken.
* `Linear subdivision` Stel in hoeveel niveaus lineaire subdivisie moeten worden gebruikt voordat reguliere smooth-subdivisie wordt toegepast. Dit kan worden gebruikt om te bepalen hoe scherp of zacht de hoeken zijn op de gesubdivideerde oppervlakken. Zet bijvoorbeeld de box-topologieverdelingen op 2, post subdivisions op 4, en probeer vervolgens de lineaire subdivisies tussen 0 en 4 te veranderen. De hoeken van de box gaan van zacht naar scherp.

### Topologie

Dit regelt het aantal polygonen in een primitieve. Meestal zijn de regelaars gekoppeld, zodat het wijzigen van de actieve schuifregelaar alle polygonen gelijkmatig aanpast. Je kunt op de ontkoppelknop tikken en de X/Y/Z-verdelingen van een vorm afzonderlijk regelen.

### Geometrie

Dit regelt de algehele grootte van een primitieve, in X/Y/Z-eenheden voor vierkante vormen en in straal voor ronde vormen.


### UV Sphere
::: warning
De UV Sphere is niet goed geschikt om op te sculpten, vooral niet op de polen.

Gebruik liever de primitieve [Sphere](#sphere), [Box](#box) of [Icosahedron](#icosahedron), samen met de optie `Project on sphere`.

Merk op dat de topologie acceptabel kan zijn om op te sculpten als je een zeer lage waarde gebruikt voor de schuifregelaars `Division`.
Je kunt dan de schuifregelaar `Overall Subdivision` gebruiken om het aantal polygonen te verhogen.

Hoewel hij niet geschikt is voor algemeen sculpten, is hij wel nuttig voor ogen; als je de sphere zo roteert dat de polen bij de pupil liggen, zal de polygoonindeling zich van nature lenen om de iris en pupil te schilderen en te sculpten.
:::


### Triplanar
Deze primitieve is speciaal in die zin dat je de [Masking tool](tools.md#mask) erop moet gebruiken om de geometrie te vormen.

![](/videos/triplanar.mp4)


::: tip
Dubbel tik op een vlak en de camera focust op dat specifieke vlak.
Dit werkt echter niet als je de primitieve met het gizmo roteert.
:::

Triplanar gebruikt de mask-informatie van 3 vlakken om een voxelraster te vullen dat vervolgens wordt gepolygoniseerd (dankzij de [Voxel Remesher](topology.md#voxel-remeshere)).

Elk vlak heeft zijn eigen symmetrievlak.

::: warning
Elke keer dat je de grootte van de Triplanar-primitieve bijwerkt, zal de kwaliteit van het mask-schilderen achteruitgaan.

Voorlopig is er geen optie om het schilderen op één vlak te ‘vergrendelen’, maar dat komt misschien in de toekomst.
Je kunt [Connected Topology](stroke.md#connected-topology) gebruiken om een beetje te helpen; als je cursor precies op één vlak ligt, zal dat de andere vlakken niet beïnvloeden.
:::

### Shadow Catcher
Voeg een vlak toe met het shadow catcher-materiaal. Zie [Shadow Catcher-materiaal](material.md#shadow-catcher) voor meer details. 


## Groep/Camera
### Groep
Maak een ‘leeg’ object waar je andere objecten onder kunt hangen. Dit kan worden gebruikt om de hiërarchie eenvoudig te organiseren door veel objecten onder een groep te plaatsen en die vervolgens te sluiten. Een groep kan ook worden gebruikt als hulpmiddel om objecten te verplaatsen; veel objecten kunnen onder een groep worden geplaatst en vervolgens kan de groep met het gizmo-gereedschap worden verplaatst, geroteerd en geschaald.

### View toevoegen
Maak een camera.

## Repeaters
![](/images/scene_primitive_repeaters.webp)

Repeaters zijn nodes die instanties maken van de objecten eronder. 

### Array
![](/images/scene_primitive_array.webp)

Wanneer objecten kinderen van deze node worden, kunnen ze als instanties in een rasterindeling worden geplaatst. Wanneer geselecteerd, heeft hij regelaars voor:
* Fit inside - schakel tussen het regelen van de grootte van het raster/de box van de array, of het regelen van de ruimte tussen de array-instanties
* CountX/Y/Z - het aantal instanties op elke as
* OffsetX/Y/Z - afstand tussen de instanties wanneer fit inside is ingeschakeld
* SizeX/Y/Z - de breedte/hoogte/diepte van het totale arrayraster wanneer fit inside is ingeschakeld.

### Curve
![](/images/scene_primitive_curve.webp)
Dit maakt een curve; kinderen van deze node worden langs de curve herhaald. Wanneer geselecteerd, heeft hij regelaars voor:
* Edit - sta toe dat punten aan de curve worden toegevoegd en dat punten op de curve worden verplaatst.
* Snap - zal curvepunten vastklikken op andere geometrie
* Align - roteert kindvormen zodat ze uitgelijnd zijn in de richting van de curve
* Count - het aantal instanties
* Closed - schakel de curve om het begin en einde te verbinden, of om een open curve te zijn
* Radius - schakel regelaars op elk curvepunt om de schaal van de instanties te regelen
* Twist - schakel regelaars op elk curvepunt om de twist-rotatie van de instanties te regelen 
* B-spline - schakel of de instanties de curve exact volgen, of B-spline-interpolatie gebruiken die gladdere resultaten geeft. 

### Radial
![](/images/scene_primitive_radial.webp)

Kinderen van deze node worden als instanties in een cirkel geplaatst. Verplaats het kindobject om de straal van deze repeater te wijzigen. Wanneer geselecteerd, heeft hij regelaars voor:
* RadialX/Y/Z - deze knoppen selecteren stelt de radiale as in en het aantal instanties.



### Mirror
![](/images/scene_primitive_mirror.webp)

Kinderen van deze node worden gespiegeld over een as. Wanneer geselecteerd, heeft hij regelaars voor:
* Gizmo - schakel het transform-gizmo in om het midden van de spiegeling in te stellen. Dit kan ook worden geroteerd en geschaald. Wanneer je klaar bent, tik opnieuw op gizmo om de standaardregelaars weer te geven.
* X/Y/Z - stel het spiegelvlak in

Alle repeaters hebben een `Validate`-regelaar, die de resultaten van de repeater bakt en vraagt hoe de bake moet worden uitgevoerd:
* Join children - de instanties worden samengevoegd tot één object
* Keep instances - de instanties blijven instanties, maar hebben niet langer de repeater als ‘ouder’
* Un-instances - de instanties worden omgezet in unieke objecten

::: tip Tip: Repeaters combineren
Repeaters kunnen onder elkaar worden geparent en meerdere objecten kunnen kinderen van repeaters worden, wat tot complexe effecten kan leiden.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Repeater-pivots

Sommige repeaters proberen het pivotpunt van de kindobjecten automatisch in te stellen, zodat ze niet bewegen, zelfs als je ze met het gizmo-gereedschap verplaatst of roteert. Als je dit gedrag moet overschrijven, voeg dan een groep in tussen de repeater en het kind. Nu kun je de kindvorm onafhankelijk van de repeater verplaatsen.
:::

## Licht

![](/images/scene_primitive_light.webp)

### Directional
Maak een directioneel licht, een oneindig ver weg lichtbron zoals de zon.

### Spot
Maak een spotlicht, met regelaars voor de conusbreedte en zachtheid

### Point
Maak een puntlicht

## Geavanceerd
### Focus op item
Dubbelklikken op een item in de Scène-lijst centreert de camera op dat item in de 3D-weergave.

### Zichtbaarheid synchroniseren
Het gebruik van het oogicoon heeft effect op alle geselecteerde items. 

### Instantie: tonen
Toon een gekleurde capsule links van de scenelijst om instanties weer te geven.


### Iconen
Stel de grootte en dekking in van de groep-, licht-, camera- en mirror-iconen in de viewport

### Hiërarchielijnen
Toon een lijn tussen ouder en kinderen in de viewport

## Onderste werkbalk
Deze iconen schakelen de zichtbaarheid van Groep, Licht, Camera, Repeater en Hiërarchielijnen in de viewport.
