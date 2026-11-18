# ![](/icons/multires.webp) Topologie {#topology}

Dit menu regelt de topologie van objecten in Nomad, en bevat ook gereedschappen om details te bakken en over te zetten tussen objecten en tussen texturen.

![](/images/topology_overview.webp)

Nomad werkt met polygonen: de geometrie bestaat uit driehoeken en quads.
Met topologie bedoelen we zowel het aantal vlakken als de manier waarop de punten (vertices) met elkaar verbonden zijn.

Het is belangrijk om je topologie in de gaten te houden, zeker als je fijne details wilt boetseren of schilderen.

::: tip Hoe houd je je topologie in de gaten?
Zet het [Draadmodel](settings.md#wireframe) aan, of schakel gewoon [Vloeiende shading](settings.md#smooth-shading) uit.
:::

![](/images/topology_top.webp)

Het topologiemenu van Nomad heeft meerdere tabbladen, verdeeld over twee rijen:

| Methode                               | Pictogram                    | Beschrijving                                                     |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolutie](#multiresolution)    | ![](/icons/multires.webp)   | Werk op meerdere detailniveaus met behulp van subdivisie         |
| [Voxel-remesh](#voxel-remesher)       | ![](/icons/voxel.webp)      | Bereken een nieuwe topologie met een gelijkmatige dichtheid      |
| [Dynamische topologie](#dynamic-topology) | ![](/icons/dynamic.webp) | Voeg tijdens het boetseren of schilderen ter plekke vlakken toe of haal ze weg |
| [Overige](#misc)                      | ![](/icons/topo_extra.webp) | Gaten sluiten, manifold afdwingen en omzetten naar triplanar     |
| [Primitieven](#primitive)             | ![](/icons/dot.webp)        | Opties van het primitief                                         |
| [Decimeren](#decimation)              | ![](/icons/decimate.webp)   | Verminder het aantal vlakken en behoud daarbij de vorm           |
| [Quad-remesh](#quad-remesh)           | ![](/icons/quad.webp)       | Bouw het object opnieuw op met een nette indeling van quads      |
| [UV-ontvouwen](#uv-unwrap)            | ![](/icons/uv.webp)         | Maak UV's aan om te kunnen textureren                            |
| [Bakken](#bake)                       | ![](/icons/bake.webp)       | Bak details en schilderwerk naar texturen, vertices of VDM-stempels |


## Polygoonstatistieken {#polygon-stats}

![](/images/topology_stats.webp)

Bovenaan elk tabblad zie je het aantal polygonen van het geselecteerde object, en van de hele scène als die meer dan één object bevat. De kolommen tonen het aantal vertices, driehoeken, quads (vierzijdige polygonen) en UV-coördinaten (0 als het object geen UV's heeft).

Tik op dit gedeelte om alle objecten van de scène te zien met hun exacte aantallen, inclusief hun aantal vlakkengroepen.

## ![](/icons/cog.webp) Tandwielmenu {#gear-menu}
Sommige onderdelen, zoals die in de tabbladen [Quad-remesh](#quad-remesh) en [Bakken](#bake), hebben extra opties. Je opent ze met het tandwielpictogram naast de titel van het onderdeel.

## ![](/icons/multires.webp) Multiresolutie {#multiresolution}

![](/images/topology_multires_menu.webp)

### Wat is multiresolutie? {#what-is-multiresolution}
Multiresolutie is vooral handig in twee situaties:
- Het vloeiende subdivisie-algoritme, om het aantal polygonen van je object te verhogen
- Meerdere resolutieniveaus beheren, zodat je kunt wisselen tussen kleine en grote aanpassingen

![](/videos/multiresolution.mp4)

#### Werken met multiresolutie {#multiresolution-workflow}
Een belangrijk voordeel van multiresolutie is dat je terug kunt gaan naar een lagere resolutie, daar je object kunt aanpassen en dan weer naar de hoogste resolutie kunt gaan zonder de fijne details te verliezen. Alle details van de hoge resolutie worden automatisch teruggeprojecteerd.

[Lagen](layers.md#layers) zijn op elke resolutie beschikbaar.

::: warning
Gebruik je een gereedschap dat de topologie van je object verandert, dan verlies je alle andere resolutieniveaus van je object!
Je krijgt in dat geval altijd een waarschuwing, bijvoorbeeld als je het volgende gebruikt:
- de [Voxel-remesh](#voxel-remesher)
- de [Dynamische topologie](#dynamic-topology)
- het [Trim-gereedschap](tools.md#trim)
- het [Split-gereedschap](tools.md#split)
:::


### Multiresolutie-schuifregelaar {#multiresolution-slider}
Deze schuifregelaar toont het aantal subdivisieniveaus van het huidige object. Zie je 6 verticale streepjes, dan zijn er 6 subdivisieniveaus. Het rondje geeft aan welk subdivisieniveau op dit moment wordt weergegeven.

Kleine pictogrammen boven de schuifregelaar laten zien welke opties (`Niveau 0 vergrendelen`, `Lineair`, `Scherpe rand`, `Behoud driehoeken`) bij elk niveau zijn gebruikt.

### Omgekeerd {#reverse}
Sta je op het laagste subdivisieniveau, dan probeert de knop Omgekeerd een niveau onder het huidige aan te maken. Dit lukt meestal alleen als het object oorspronkelijk met subdivisie is gemaakt, bijvoorbeeld in Nomad of in een andere 3d-app die multiresolutie-subdivisieoppervlakken ondersteunt.

### Subdivisie {#subdivide}
De knop *Subdivisie* verviervoudigt het aantal polygonen, dus houd het aantal goed in de gaten: het loopt heel snel op! Nomad vraagt om bevestiging als het resultaat erg zwaar zou worden.
Een belangrijke eigenschap van *subdivisieoppervlakken* is dat ze naar een *glad oppervlak* toe groeien.
Wil je zien hoe dat werkt, probeer dan de knop *Subdivisie* op een object met maar een paar polygonen.

Met de optie `Lineair` schakel je dit *gladde* gedrag uit.

### Lager verwijderen {#delete-lower}
Verwijdert de subdivisieniveaus onder het niveau dat nu wordt weergegeven. Heb je dit per ongeluk gedaan, dan kun je ze opnieuw aanmaken met de knop Omgekeerd.

### Hoger verwijderen {#delete-higher}
Verwijdert de subdivisieniveaus boven het niveau dat nu wordt weergegeven.

### ![](/icons/lock.webp) Niveau 0 vergrendelen {#lock-lv0}
Behoud de vorm van het laagste subdivisieniveau terwijl je op hogere niveaus boetseert. Schilderwerk wordt nog wel doorgegeven aan niveau 0. Dit kan belangrijk zijn als je object in een andere app is gemaakt en het basisobject ongewijzigd moet blijven.

Deze optie is alleen beschikbaar vóór de eerste subdivisie. Staat ze uit, dan verplaatsen grote aanpassingen op hogere subdivisieniveaus ook niveau 0.

### ![](/icons/linear.webp) Lineair {#linear-subdivision}
Onderverdeel de mesh zonder hem glad te maken.

### ![](/icons/group.webp) Scherpe rand {#sharp-border}
Heeft je object vlakkengroepen, dan houdt deze optie de grenzen tussen de vlakkengroepen scherp. Je kunt dit per subdivisieniveau instellen (de subdivisie-schuifregelaar toont dan een klein pictogram boven dat niveau).

### ![](/icons/triangle.webp) Behoud driehoeken {#keep-triangles}
De meeste gangbare subdivisiesystemen proberen bij het onderverdelen alle polygonen om te zetten naar quads. Met deze schakelaar gebruikt de subdivisie in plaats daarvan driehoeken.

::: tip

Subdivisie maakt standaard alle scherpe randen glad. Wil je randen een beetje scherp houden, experimenteer dan met `Lineair` of `Scherpe rand` op de eerste 2 subdivisieniveaus, en zet ze uit voor de hogere niveaus. Zo krijg je een half-scherpe onderverdeelde mesh.

:::

### Hoogste niveau tonen {#show-highest-level}
Toon het hoogste niveau met al zijn details terwijl je op een lager niveau boetseert. Handig om het eindresultaat te zien terwijl je grote aanpassingen maakt.

### Draadmodel: Alleen niveau 0 {#wireframe-level-0-only}
Als het [Draadmodel](settings.md#wireframe) aan staat, toon dan alleen het draadmodel van het laagste niveau. Het dichte draadmodel van de hoge niveaus kan de vorm anders verbergen.


## ![](/icons/voxel.webp) Voxel-remesh {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
De `Voxel-remesh` dwingt de hele mesh tot een gelijkmatige resolutie: alle polygonen worden ongeveer even groot. Dat is heel handig als je niet over topologie wilt nadenken en gewoon vrij wilt boetseren.

Een typische werkwijze begint met de `Voxel-remesh` om een ruwe vorm op lage resolutie neer te zetten.
Druk af en toe op de knop *Remesh* als je de mesh te ver uitrekt, zodat er niet te veel vervorming ontstaat.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Zoals hierboven gezegd werkt Nomad met polygonen, maar de `Voxel-remesh` is een uitzondering: daar wordt (tijdelijk) een andere aanpak gebruikt om de mesh opnieuw op te bouwen.

Een groot verschil is dat de voxelaanpak geen zelfdoorsnijdingen toestaat; die worden dus opgelost.
Ook kan hij niet overweg met meshes met gaten.

Met gaten bedoelen we niet het `genus-gat` (het `gat` van een donut), maar meshes die niet `waterdicht`/`gesloten` zijn.
In de praktijk betekent dit dat vóór het remeshen alle gaten worden gevuld, net als bij het [Trim-gereedschap](tools.md#trim) of de functie [Gaten vullen](#holes). Met de optie [Gaten](#voxel-holes) hieronder kies je hoe.
:::

### ![](/icons/voxel.webp) Remesh {#voxel-remesh}
Voer de voxel-remesh uit. Kleine pictogrammen op de knop herinneren je eraan welke van de opties hieronder aan staan.

### Resolutie {#voxel-resolution}
De grootte van de voxels die voor de berekening worden gebruikt; hogere waarden geven meer detail. Terwijl je deze waarde aanpast, verschijnt er een dambordpatroon op de mesh als voorbeeld van het resultaat.

De pipet neemt de resolutie over van de dichtheid van de mesh op de plek waar je tikt. Met de kubusknop ernaast wordt de waarde een `Randlengte` in wereldeenheden: dezelfde waarde geeft dan hetzelfde detail op elk object.

### Multiresolutie opbouwen {#build-multiresolution}
Maak lagere multiresolutieniveaus aan bij de voxel-remesh. Stel je met het dambordpatroon een resolutie in en zet je Multiresolutie opbouwen op 2, dan heeft het eindresultaat het detail van de resolutie-schuifregelaar. In het tabblad Multiresolutie sta je dan op niveau 2, met daaronder lagere resoluties op niveau 1 en niveau 0. Zo krijg je in één keer een nette mesh met gelijkmatige polygonen én een controlemesh met een lagere resolutie.

Het gaat bovendien sneller en gebruikt minder geheugen bij hoge resoluties. Maar met een lage resolutie en veel niveaus verlies je details.

::: tip Tip: Multiresolutie opbouwen en stabiel gladstrijken

Deze optie kan soms 'lussen' in de geometrie veroorzaken die lastig glad te strijken zijn en kleine puistjes geven. Gebeurt dat, zet dan 'Stabiel gladstrijken' aan in de opties van het Gladstrijken-gereedschap. 

:::

### Dunne delen verdikken {#thicken-thin-parts}
Delen die dunner zijn dan de voxels kunnen bij het remeshen breken of verdwijnen. Deze optie maakt ze dikker zodat ze heel blijven; hogere waarden maken ze dikker. Niet beschikbaar in combinatie met `Scherpe randen` of `Scherpe grens`.

### Gaten {#voxel-holes}
Hoe gaten vóór het remeshen worden gesloten:

* `Vullen` - Elk gat wordt apart gesloten, vanaf de rand.
* `Vorm` - Gaten worden gesloten door het omliggende oppervlak te volgen, en open stukken die elkaar overlappen worden samengevoegd.

### ![](/icons/angle.webp) Scherpe randen {#keep-sharp-edges}
Leg de nieuwe punten op de scherpe randen van de oorspronkelijke mesh. Vooral nuttig bij eenvoudige booleaanse bewerkingen met primitieven, en het kan vervorming veroorzaken.

### ![](/icons/group.webp) Scherpe grens {#voxel-sharp-border}
De nieuwe vlakken volgen de grenzen van de vlakkengroepen, en een grens blijft scherp waar het oppervlak erlangs een knik maakt.

### ![](/icons/group_separate.webp) Groepen gescheiden houden {#keep-groups-separate}
Elke vlakkengroep wordt apart geremesht: groepen smelten nooit samen, en elke groep blijft een gesloten stuk in zijn eigen groep. In deze modus wordt geen multiresolutie opgebouwd. De optie is beschikbaar als het object meerdere vlakkengroepen heeft.

## ![](/icons/dynamic.webp) Dynamische topologie {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolutie en voxel-remeshing zijn in de industrie gangbare methoden om de topologie te beheersen, maar bij allebei moet je opletten dat je polygonen niet te ver uitrekt of te dicht in elkaar drukt. 

Dynamische topologie is een alternatief. Terwijl je boetseert, voegt Nomad tijdens de penseelstreek polygonen toe en haalt ze weg waar nodig: kerf je kleine details in, dan komen er veel kleine polygonen precies waar je ze nodig hebt, en strijk je elders glad, dan verdwijnen er polygonen.

Let op: dynamische topologie gebruikt driehoeken in plaats van quads. Dat kan er wat rommelig uitzien, maar je kijkt eigenlijk beter niet naar het draadmodel. Concentreer je op een mooi beeld zonder je zorgen te maken over de topologie; later kun je met een van de andere remesh-gereedschappen van Nomad een nette quad-mesh maken.

Bekijk het in actie in de video hieronder.

![](/videos/dynamic.mp4)

### Ingeschakeld {#enabled}
Zet dynamische topologie aan. Onder de schuifregelaars voor straal en intensiteit van het penseel verschijnt dan een DynTopo-pictogram, waarmee je DynTopo per gereedschap aan of uit zet. Het kan merkbaar ten koste gaan van de prestaties, en lagen worden correct bijgewerkt.

### Details {#dyn-detail}
Bepaalt de hoeveelheid detail; hoe het werkt hangt af van de keuze bij 'Detail gebaseerd op...', zie hieronder. In de modus `Scherm` toont het label de gewenste grootte van de driehoeken in pixels. In de modus `Constant` kun je met een pipet het detail overnemen van de dichtheid van de mesh op de plek waar je tikt.

### Detail gebaseerd op... {#detail-based-on}
| Methode  | Beschrijving                                                    |
| :------: | :-------------------------------------------------------------: |
| Scherm   | Het detailniveau hangt af van hoe groot het object op het scherm is. Met de detail-schuifregelaar op 100% of hoger krijg je fijn detail met kleine driehoeken, op 1% weinig detail met grote driehoeken.  |
| Radius   | De straal van het gereedschap bepaalt de hoeveelheid detail: een kleine straal voor fijn detail, een grote straal voor weinig detail. De detail-schuifregelaar is een vermenigvuldiger op deze verhouding.                     |
| Constant | De detail-schuifregelaar bepaalt de hoeveelheid detail, los van de schermgrootte of de grootte van het gereedschap. Het is dezelfde waarde als de schuifregelaar [Detail](#all-detail) van `Remesh`.             |

::: tip TIP: de modus Radius

Om goed te voelen hoe de modus Radius werkt, verschuif je de detail-schuifregelaar met één vinger en verander je tegelijk de straal van het gereedschap met een andere vinger. Je ziet dan hoe ze met elkaar samenhangen.

:::

### Voorkeur... {#prefer}
| Methode    | Beschrijving        |
| :--------: | :-----------------: |
| Snelheid   | Voorrang aan prestaties |
| Kwaliteit  | Voorrang aan kwaliteit  |

Geef je voorrang aan `Kwaliteit`, dan zijn er 2 belangrijke verschillen:
- de verfijning gebeurt vóór het boetseren, dus je krijgt minder interpolatiefouten als je heel kleine details schildert of boetseert
- de verfijning gaat door tot het juiste detailniveau bereikt is, in plaats van stap voor stap.
 
Zo wordt de topologie altijd verfijnd zoals verwacht, ook als je heel kleine details boetseert of snelle streken zet


### ![](/icons/pressure.webp) Druk op straal gebruiken {#use-pressure-on-radius}
Alleen van toepassing als `Radius` actief is. Staat deze optie aan, dan volgt het detailniveau altijd de grootte van het penseel, ook als die door de druk van de stylus verandert.

### Streekfalloff gebruiken {#use-stroke-falloff}

Neem ook de afnamecurve en de alpha van het penseel mee in de DynTopo-berekeningen.

### Methode {#method}
Kies hoe dynamische topologie de mesh aanpast, zowel tijdens het boetseren als bij [Remesh](#dyn-remesh):

| Methode        | Beschrijving                                                          |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisatie  | Kan vlakken toevoegen en weghalen; dit is de modus uit de video hierboven |
| Onderverdeling | Voegt alleen nieuwe vlakken toe, kan geen vlakken weghalen            |
| Decimering     | Haalt alleen vlakken weg, kan geen nieuwe vlakken toevoegen           |

### ![](/icons/shield.webp) Gemaskeerd gebied beschermen {#protect-masked-area}
Gemaskeerde gebieden beschermen de topologie tegen wijzigingen.

### ![](/icons/normal.webp) Vertex extrapolatie {#vertex-extrapolation}
Plaats de punten op een glad oppervlak dat de kromming eromheen volgt, in plaats van plat op de bestaande vlakken.

### Detail {#all-detail}
De resolutie die bij het remeshen wordt gebruikt. Staat DynTopo in de modus 'Constant', dan is dit dezelfde waarde als de schuifregelaar Details bovenaan dit menu. De pipet neemt het detail over van de dichtheid van de mesh op de plek waar je tikt.

### Remesh {#dyn-remesh}
Voer een volledige remesh uit met het DynTopo-algoritme. Meestal gebruik je voor een volledige remesh beter de [Voxel-remesh](#voxel-remesher).

Een voordeel ten opzichte van voxels is wel dat de mesh niet gesloten hoeft te zijn en dat het gemaskeerde gebied beschermd wordt, zodat je beter kunt bepalen waar je meer of minder dichtheid wilt.



## ![](/icons/topo_extra.webp) Overige {#misc}

![](/images/topology_misc_menu.webp)

Dit tabblad bundelt gereedschappen om de mesh op te schonen of om te zetten: de gaten sluiten, hem manifold maken of er een triplanar van maken.

### ![](/icons/hole.webp) Gaten {#holes}
![](/images/topology_holes_menu.webp)
Meestal is je object waterdicht, wat betekent dat de mesh 'gesloten' is.

Heeft je object toch gaten, dan kun je ze vullen.

![](/videos/hole_filling.mp4)

::: tip
Als je de Voxel-remesh gebruikt, worden alle gaten automatisch gesloten, of je hem nu op 1 of op meerdere meshes toepast.
:::

#### Sluit gaten {#close-holes}
Sluit de gaten.

#### Opties {#holes-gear-menu}
Deze opties bepalen hoe de gaten worden gevuld:

##### Vlakkengroep {#fill-face-group}
Kies de vlakkengroep van de nieuwe vlakken:

* `Gemengd` - Een gat dat door één vlakkengroep wordt omringd, krijgt die groep; een gat dat meerdere groepen raakt, krijgt een nieuwe.
* `Nieuw` - De gevulde gaten krijgen een nieuwe vlakkengroep.
* `Hergebruiken` - Elk gat krijgt de vlakkengroep die het het meest omringt.

##### Detail {#fill-detail}
De polygoondichtheid waarmee het gat wordt gevuld. Terwijl je deze schuifregelaar versleept, verschijnt er een dambordpatroon op het model dat aangeeft hoe groot de driehoeken worden. Met het selectievakje schakel je dit uit en worden alleen de bestaande punten gebruikt. Dat geeft meestal lange, dunne driehoeken over het gat, die lastig te boetseren zijn.

##### Overbruggen {#fill-non-manifold}
Vul een gat en de eilanden erin als één oppervlak, in plaats van elke rand apart te vullen. Met een grotere hoek worden ook sterker gekromde gaten overbrugd. Het selectievakje zet het uit.

### ![](/icons/cog.webp) Manifold afdwingen {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Probeer non-manifold randen op te schonen. Handig voor externe software die geen randen ondersteunt die door meer dan 2 vlakken gedeeld worden.

#### Schoonmaken {#clean}
Voer het opschonen uit.

#### Opties {#force-manifold-gear-menu}
Deze optie bepaalt hoe de mesh wordt opgeschoond:

##### Verwijder kleine vlakken {#delete-small-faces}
Een drempelwaarde om kleine polygonen te verwijderen en samen te voegen. Zet het aan met het selectievakje.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Zet de mesh om naar een [triplanar](scene.md#triplanar)-primitief.
Je verliest daarbij waarschijnlijk veel detail: ook lagen, schilderwerk en multiresolutie gaan verloren.

#### Forceer kubus {#force-cubic}
Maak van de triplanar een kubus. Anders past de triplanar zich aan de dichtstbijzijnde omhullende doos rond je object aan.

#### Converteer {#convert}
Voer de omzetting naar triplanar uit.

#### Resolutie {#triplanar-resolution}
De resolutie van het triplanar-raster; hogere waarden behouden meer detail.

## ![](/icons/decimate.webp) Decimeren {#decimation}

![](/images/topology_decimation.webp)

Verminder het aantal polygonen en probeer daarbij zoveel mogelijk details te behouden, met driehoeken.

Dit is handig als je wilt exporteren voor 3d-printen.
Wil je daarna verder boetseren, dan kun je het beter niet gebruiken, omdat het ongelijke driehoeken kan opleveren.

Let op: gemaskeerde gebieden worden niet gedecimeerd.

![](/videos/decimate.mp4)

::: tip

Het [Quad Remesher-gereedschap](tools.md#quad-remesher) kan op objecten met veel polygonen lang rekenen en resultaten geven die moeilijk te sturen zijn. Bereid je de mesh voor met [vlakkengroepen](tools.md#facegroup) en decimeren, dan werkt Quad Remesher veel sneller en heb je veel meer controle over de topologie.

* Verdeel de mesh in vlakkengroepen die de gewenste quad-flow aangeven.
* Ontspan de vlakkengroepen voor gladde grenzen.
* Decimeer. Zo heb je geen dunne of vervormde vlakken langs de grenzen van de vlakkengroepen. Zorg dat onder `Randen behouden` de optie `Vlakkengroep` aan staat. Dan volgen de randen van de driehoeken precies de grenzen van je vlakkengroepen.
* Zet in de opties van Quad Remesher het ontspannen uit (je hebt de mesh immers al ontspannen), dan krijg je goede resultaten.

:::

### Decimeren {#decimate}
Start het decimeren.

De pictogrammen naast de knop Decimeren tonen de opties hieronder, en je kunt ze er aan- en uitzetten. Het percentage geeft aan hoe sterk die optie is.

* ![](/icons/palette.webp)  `Schildering behouden` - Plaats meer driehoeken waar er geschilderd detail is.
* ![](/icons/triforce.webp) `Uniforme vlakken` - Maak bij voorkeur driehoeken van gelijke grootte.
* ![](/icons/hole.webp)  `Gat` - Decimeren probeert randen bij open geometrie en gaten ongewijzigd te laten.
* ![](/icons/group.webp) `Vlakkengroep` - Decimeren probeert de grenzen van vlakkengroepen ongewijzigd te laten.
* ![](/icons/uv.webp) `UV` - Decimeren probeert de UV-grenzen ongewijzigd te laten.

### Doeldriehoeken {#target-triangles}
Stel het gewenste aantal driehoeken in. De standaardwaarde is 50%; met de knop procent/doel wissel je tussen een percentage en een exact aantal polygonen.

### Opties {#decimate-gear-menu}
Elke optie heeft een selectievakje om haar aan of uit te zetten, en een waarde voor de sterkte:

#### ![](/icons/palette.webp) Schildering behouden {#preserve-painting}
Deze waarde bepaalt hoe nauwkeurig geschilderd detail behouden blijft. Hogere waarden behouden meer schilderwerk. Zet hem op 0 als het schilderwerk je niet uitmaakt.

#### ![](/icons/triforce.webp) Uniforme vlakken {#uniform-faces}
Hogere waarden geven driehoeken van vergelijkbare grootte.

#### Randen behouden {#preserve-borders}
Voorkom dat randen worden gedecimeerd. Je kunt een gewicht instellen voor de randen bij `Gat`, `Vlakkengroep` of `UV` (`UV` vereist een object met UV's).

## ![](/icons/quad.webp) Quad-remesh {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Bouw het object opnieuw op met een nette indeling van quads. Dit tabblad heeft meerdere remeshers, elk met een eigen knop `Remesh`, schuifregelaar `Doelquads` en tandwielmenu. Probeer ze uit op je object: de resultaten verschillen flink!

### Quad Remesher {#quad-remesher}
Dezelfde remesher als het gereedschap [Quad Remesher](tools.md#quad-remesher), ontwikkeld door [Exoside](https://exoside.com/). Hij is alleen op sommige platformen beschikbaar en moet apart gekocht worden: tot die tijd toont de knop `Remesh` een winkelwagentje.

`Gereedschap selecteren` schakelt over naar het Quad Remesher-gereedschap, om geleiders te tekenen en de dichtheid te schilderen. Het tandwielmenu bevat `Adaptief aantal quads`, `Adaptieve grootte` (op 100% volgt de grootte van de quads de kromming, op 0% zijn de quads overal even groot), `Harde randen automatisch detecteren` en `Vertex herprojecteren`.

::: tip
Waar hij beschikbaar is, geeft Quad Remesher meestal de beste resultaten en de meeste controle.
:::

### AutoRemesher {#autoremesher}
Een alternatieve quad-remesher, met opties om de grootte en vorm van de quads aan het oppervlak aan te passen.

#### ![](/icons/cog.webp) Tandwielmenu van AutoRemesher {#autoremesher-gear-menu}
Het tandwielmenu bevat deze geavanceerde opties:

##### Randschaling {#edge-scaling}
Schaal de grootte van de quads; hogere waarden geven grotere quads.

##### Aanpassingsvermogen {#adaptivity}
Pas de dichtheid van de quads aan de kromming aan. 0 geeft quads van gelijke grootte, 1 geeft kleinere quads in gekromde gebieden.

##### Anisotropie {#anisotropy}
Rek de quads uit in de vlakste richting van het oppervlak. 0 geeft vierkante quads, 1 geeft langgerekte quads op buizen en ruggen.

##### Scherpe rand {#sharp-edge}
Randen die verder geknikt zijn dan deze hoek, blijven behouden als scherpe kenmerken.

##### Normalen vloeiend maken {#smooth-normal}
Op 0 blijft het oppervlak tijdens het remeshen facetachtig. Hogere waarden maken het oppervlak gladder door rekening te houden met de vertexnormalen.

##### Maximale vulling van gaten {#autoremesher-max-fill-hole}
Het algoritme kan soms ongewenste gaten maken. Heeft een gat minder vertices dan deze waarde, dan wordt het gevuld.

### Instant Mesh {#quad-remesh-instant}
Remesh met het [Instant Meshes-algoritme van Wenzel Jakob, Marco Tarini, Daniele Panozzo en Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Het analyseert de flow van een mesh en maakt een nette quad-topologie.

#### Remesh {#instant-remesh}
Start het remeshen.

#### Doelquads {#target-quads}
Het aantal quads dat de remesher probeert te maken.

#### ![](/icons/cog.webp) Tandwielmenu van Instant Mesh {#quad-remesh-instant-gear-menu}
Het tandwielmenu bevat deze geavanceerde opties:

##### Vouwhoek {#crease-angle}
Een drempelwaarde voor scherpe hoeken die het remeshen helpt te sturen. Zet het aan met het selectievakje.

##### Maximale vulling van gaten {#max-fill-hole}
Het algoritme kan soms ongewenste gaten maken. Heeft een gat minder vertices dan deze waarde, dan wordt het gevuld.

### QuadriFlow {#quadriflow}
Remesh met het QuadriFlow-algoritme, nog een manier om een nette indeling van quads te krijgen.

#### ![](/icons/cog.webp) Tandwielmenu van QuadriFlow {#quadriflow-gear-menu}
Het tandwielmenu bevat deze geavanceerde opties:

##### Randen behouden {#quadriflow-preserve-boundary}
Bescherm de randen van gaten.

##### Scherpe randen behouden {#keep-sharp}
Lijn de quads uit met de scherpe randen van het oppervlak.

##### Minimale-kostenstroom {#min-cost-flow}
Gebruik een minimale-kostenstroom-solver voor de indeling van de quads. Langzamer, maar kan een regelmatigere topologie opleveren.

## ![](/icons/uv.webp) UV-ontvouwen {#uv-unwrap}
Bereken textuurcoördinaten (UV's) voor het geselecteerde object. Nomad heeft twee methoden, `UVAtlas` en `BFF`, elk met een eigen knop `Ontvouwen`.

![](/videos/unwrap.mp4)

::: tip UV's?
Een bekende vergelijking voor UV's is het inpakken van een cadeau: hoe knip je het inpakpapier zo dat het een voorwerp helemaal bedekt, zonder overlappingen? 

UV's werken net zo, maar in plaats van het papier knip je het object. Stel je voor dat je model van dun plastic is: hoe zou je het opensnijden zodat je het plat kunt neerleggen, het in die platte toestand kunt beschilderen en het daarna weer in elkaar kunt zetten?

Stel je nu voor dat het oppervlak van je model van rekbare lycra is. Je kunt het model plat uitrekken, het opensnijden, of allebei. Maar als je op het platte model een dambordpatroon schildert, is dat dambord vervormd zodra je het weer in elkaar zet. Wat is beter: meer sneden met minder vervorming, of minder sneden met meer vervorming?

UV's zijn instructies die 3d-software vertellen hoe het object 'geknipt en uitgerekt' moet worden bij het aanbrengen van texturen. UVAtlas kiest meestal voor 'meer sneden, minder vervorming'.


:::

::: tip UV's, Nomad en andere apps

De meeste getextureerde modellen die je online vindt, gebruiken UV's voor hun texturen. Nomad kan die importeren en weergeven via het paneel [materiaal](material.md#textures).

Modellen die je in Nomad maakt, kun je rechtstreeks beschilderen, zonder UV's. Moet je ze naar andere apps exporteren, bijvoorbeeld [Procreate](https://procreate.art/), dan kun je de kleurinformatie van Nomad via UV's in texturen 'bakken'. 

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas maakt meestal liever meer eilanden met sneden, om de vervorming zo klein mogelijk te houden.

#### Ontvouwen {#unwrap}
Bereken UV's voor het geselecteerde object.

#### Opties {#uvatlas-gear-menu}
De knoppen naast `Ontvouwen`:

##### Vlakkengroep {#atlas-face-group}
Toont de knop `Ja`, dan bepalen de vlakkengroepen waar de UV's worden opengesneden. Deze instelling wordt gedeeld met BFF.

##### Verwijder UVs {#delete-uvs}
De prullenbakknop verwijdert de UV's van het object.

##### Inspecteren {#uv-inspect}
Toon de UV's van het object op de achtergrond.

#### Maximale rek {#max-stretch}
Lage waarden geven minder vervorming en meer eilanden, hoge waarden meer vervorming en minder eilanden. 

#### Eilandafstand {#island-spacing}
De ruimte tussen de eilanden. Lage waarden verspillen minder ruimte, maar dan kunnen texturen van het ene eiland in het andere doorlopen. 

::: warning
Het berekenen van UV's kan even duren; gebruik het liefst een mesh met minder dan 100k vertices.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF-UV's kiezen voor 'minder sneden, meer vervorming'. 

#### Opties {#uv-bff-gear-menu}
Naast `Ontvouwen` staan dezelfde knoppen `Vlakkengroep`, verwijderen en `Inspecteren` als bij [UVAtlas](#uvatlas-gear-menu).

##### Vlakkengroep {#bff-face-group}

Gebruik vlakkengroepen om te bepalen waar de UV's worden opengesneden.

#### Aantal kegels {#cone-count}
Het aantal hoofdprojecties dat wordt gebruikt. Lagere waarden geven minder eilanden, maar meer vervorming. Hogere waarden kosten meer rekentijd.

#### Naadloze patches {#seamless-patches}
Beïnvloedt de indeling van de UV-patches en kan flinke vervorming geven. Werkt het best met zorgvuldig gemaakte vlakkengroepen.

::: warning
BFF kan overlappende UV's maken als de mesh handvatten heeft (zoals het gat van een donut).
:::

### ![](/icons/preview.webp) UV weergeven na unwrappen {#show-uv-after-unwrap}
Open na het ontvouwen de UV-inspector, zodat je het resultaat meteen kunt controleren.

### ![](/icons/bake.webp) Bakken: Textuur → Textuur {#unwrap-bake-texture}
Alleen beschikbaar als het materiaal van het object texturen heeft. Ontvouw je het object opnieuw, dan worden de texturen overgezet naar de nieuwe UV's, zodat ze nog steeds passen. De resolutie staat standaard op `Auto`, gelijk aan de grootste textuur, maar je kunt hem ook zelf instellen.

## ![](/icons/bake.webp) Bakken {#bake}
Dit tabblad zet details en schilderwerk over tussen objecten, en tussen vertices en texturen.

`Van hoge-resolutie` gebruikt andere objecten als bron; het getal tussen haakjes geeft aan hoeveel. Nomad kiest ze zo:

- alle geselecteerde objecten worden gebruikt, en het hoofdobject van de selectie is het doel (het sterkst gemarkeerde in het menu [Scène](scene.md))
- is er maar één object geselecteerd, dan gebruikt Nomad in plaats daarvan alle zichtbare objecten
- zijn alle andere objecten verborgen (bijvoorbeeld met Solo), dan wordt de hele scène gebruikt

### ![](/icons/bake.webp) Bakken → Textuur {#bake-texture}
![](/images/topology_bake_menu.webp)

Bij het bakken naar texturen worden andere zichtbare objecten in de scène op de UV's van het geselecteerde object geprojecteerd, zodat er texturen ontstaan. Het object moet UV's hebben.

Zo ziet een typische werkwijze voor het bakken eruit:
- Je hebt een mesh met fijne details en schilderwerk
- Kloon hem
- Decimeer hem (zet `Schildering behouden` op 0)
- Ontvouw de UV's
- Bak hem!

Je hebt nu een mesh met een lage resolutie die het meeste schilderwerk en de meeste details van je vorige object behoudt.

Na afloop worden de vertexkleuren naar een nieuwe, uitgeschakelde laag verplaatst, zodat ze de texturen niet in de weg zitten.

#### Van het object zelf {#tex-from-itself}
Bak het object op zijn eigen UV's: zijn schilderwerk wordt textuur, en heeft het multiresolutieniveaus, dan worden de details van het hoogste niveau op het huidige niveau gebakken (er staat dan een multires-pictogram op de knop). Dit is eenvoudig in te stellen, maar vaak wil je meer controle; dan is de volgende optie handiger.

#### Van hoge-resolutie {#tex-from-high-res}
Bak de andere objecten op het geselecteerde object. Het getal tussen haakjes geeft aan hoeveel andere objecten als bron met hoge resolutie worden gebruikt en op het huidige object met lage resolutie en UV's worden gebakken. De andere objecten hoeven qua indeling of topologie niet op het te bakken object te lijken, wat veel verschillende werkwijzen mogelijk maakt.

#### Resolutie {#tex-bake-resolution}
De resolutie van de gebakken textuur. Gebakken texturen zijn altijd vierkant, dus 1024 geeft een afbeelding van 1024x1024. 

De knoppen eronder zijn snelkoppelingen voor veelgebruikte resoluties. Ter vergelijking: 512x512 is vrij klein, bijvoorbeeld voor webafbeeldingen en eenvoudige geometrie. 4096x4096 (kortweg 4k) is voor renders van hoge kwaliteit.

#### Kleur, Ruwheid, Metaalheid, Normaal, Verplaatsing, Lichtgevend, Dekking {#tex-normal-roughness-metalness-color-emissive-opacity}
Met deze knoppen kies je welke eigenschappen worden gebakken, elk in een aparte map. Na het bakken worden ze als texturen aan het materiaal van het huidige object toegevoegd. `Verplaatsing` bakt de hoogte van de details als displacementmap.

#### ![](/icons/cog.webp) Tandwielmenu van Bakken {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Het tandwielmenu bevat deze geavanceerde opties:

##### Back-up {#tex-backup}
Om de gebakken texturen goed te kunnen bekijken, moet het schilderwerk van het object uitgeschakeld zijn. `Back-up (Schilderen → Laag)` zet al het schilderwerk als back-up over naar een nieuwe laag, zodat je het makkelijk aan en uit kunt zetten.

##### Multires gebruiken {#tex-use-multires}
Voor `Van het object zelf` op een object met multiresolutieniveaus. Nomad leest de hoge resolutie via de subdivisieniveaus in plaats van stralen te werpen: dat is sneller en vrij van projectiefouten. Zet het uit om te bakken met de opties hieronder.

##### Gladde basis {#tex-smooth-base}
Voor `Verplaatsing` op een object met multiresolutieniveaus. Meet de verplaatsing vanaf de onderverdeelde basis in plaats van vanaf de platte vlakken. Laat het aan staan als de displacementmap op een onderverdeelde mesh komt, zoals bij adaptieve subdivisie in Blender.

##### Zoek afstand {#tex-cage-radius}
De maximale afstand waarbinnen naar het bronoppervlak wordt gezocht. Standaard is deze afstand klein om artefacten te voorkomen, maar je kunt hem vergroten als de bronobjecten ver van het te bakken object af liggen.

##### Projectie {#tex-projection}
Hoe het bronoppervlak wordt gevonden:

* `Straal` - Projecteer langs de normaal van het oppervlak.
* `Straal + dichtstbijzijnd` - Gebruik de normaalstraal, en het dichtstbijzijnde oppervlak als de straal niets raakt.
* `Dichtstbijzijnd` - Projecteer op het dichtstbijzijnde punt van het bronoppervlak.

##### Straal offset {#tex-ray-offset}
Bepaalt waar de bakberekeningen op het te bakken object beginnen. Een kleine afstand tot het oppervlak voorkomt de meest voorkomende artefacten. Liggen de bronobjecten heel ver van het te bakken object af, dan moet je deze offset misschien vergroten. Wordt niet gebruikt door `Dichtstbijzijnd`.


### ![](/icons/bake.webp) Herprojecteer → Vertex {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projecteer geboetseerde details, schilderwerk, lagen en texturen naar vertexwaarden.

Je kunt het zien als het omgekeerde van bakken: waar bakken vertexeigenschappen naar texturen overzet, zet herprojecteren texturen (en andere eigenschappen)
 terug naar vertices.

::: tip
Bij `Bakken → Textuur` en `Herprojecteer → Vertex` wordt rekening gehouden met zowel de vertexkleuren als de texturen van het materiaal.
:::

#### Van het object zelf {#vertex-from-itself}
Zet de texturen van het materiaal om naar vertexwaarden. Deze knop is alleen actief als het object UV's heeft en er texturen actief zijn in het materiaal.

::: tip TIP: Texturen schilderen
Nomad ondersteunt niet rechtstreeks het schilderen en bewerken van texturen, maar je kunt een vergelijkbaar resultaat bereiken door texturen naar vertexwaarden te projecteren, op de vertices te schilderen en daarna de vertices weer naar texturen te bakken:

1. Maak een object met weinig polygonen en UV's
1. Laad texturen in het materiaal
1. Onderverdeel het genoeg om erop te kunnen schilderen
1. Gebruik `Herprojecteer → Vertex` in de modus `Van het object zelf`: de textuur is nu omgezet naar vertexwaarden
1. Schilder, strijk glad, smeer uit, stempel: doe alle bewerkingen die je nodig hebt
1. Gebruik `Bakken → Textuur` in de modus `Van het object zelf`. Je bewerkingen worden weer omgezet naar texturen.
:::

#### Van hoge-resolutie {#vertex-from-high-res}
Zet de andere objecten om naar vertexwaarden op het geselecteerde object. Het getal op deze knop geeft het aantal bronobjecten aan. Dit is vooral bedoeld voor een mesh die ook een hoge resolutie heeft, meestal met een nette topologie.

::: tip
Met het herprojecteren van andere objecten kun je niet alleen kleurinformatie overzetten, maar ook vertices op andere objecten projecteren: zo kun je bijvoorbeeld verband op een personage projecteren.
:::

#### Hoekpunten, Kleur, Ruwheid, Metaalheid, Dekking, Masker, Lagen, Vlakkengroep {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Met deze knoppen kies je welke eigenschappen op het geselecteerde object worden geprojecteerd. `Lagen` zet de andere lagen over naar de geselecteerde mesh.

#### ![](/icons/cog.webp) Tandwielmenu van Herprojecteer {#vertex-reproject-gear-menu}
Het tandwielmenu bevat deze geavanceerde opties:

##### Dekking → Masker {#vertex-opacity-to-mask}
Zet de dekking van de bron om naar een masker op het geselecteerde object.

##### Iteraties {#vertex-iterations}
Hoe vaak het ontspannen tijdens het herprojecteren wordt toegepast. Wordt alleen gebruikt als `Hoekpunten` aan staat.

##### Ontspan {#vertex-relax}
De indeling van de geselecteerde mesh kan een beetje gladgestreken of ontspannen worden, zodat hij beter aansluit op de bronobjecten. `Vloeiend` werkt beter voor meshes met veel polygonen, `Ontspan` voor meshes met weinig polygonen. Met `Automatisch` kiest Nomad zelf de beste methode.

##### Zoek afstand {#vertex-cage-radius}
De maximale afstand waarbinnen naar het bronoppervlak wordt gezocht. Standaard is deze afstand klein om artefacten te voorkomen, maar je kunt hem vergroten als de bronobjecten ver van het geselecteerde object af liggen.

##### Projectie {#vertex-projection}
Hoe het bronoppervlak wordt gevonden:

* `Straal` - Projecteer langs de normaal van het oppervlak.
* `Adaptieve mix` - Meng de normaalstraal en het dichtstbijzijnde oppervlak op basis van de afstand en de `Straalvoorkeur`. Mist de een, dan wordt de ander gebruikt.
* `Dichtstbijzijnd` - Projecteer op het dichtstbijzijnde punt van het bronoppervlak.

##### Straalvoorkeur {#vertex-ray-bias}
Alleen voor `Adaptieve mix`. Hogere waarden laten de mix meer naar het resultaat van de normaalstraal neigen, lagere waarden meer naar het dichtstbijzijnde punt.

##### Straal offset {#ray-vertex-offset}
Bepaalt waar de berekeningen op het geselecteerde object beginnen. Een kleine afstand tot het oppervlak voorkomt bepaalde artefacten. Liggen de bronobjecten heel ver van het te bakken object af, dan moet je deze offset misschien vergroten. Wordt niet gebruikt door `Dichtstbijzijnd`.

### ![](/icons/bake.webp) Bakken → VDM {#bake-vdm}
Maak een VDM-stempel (vector displacement) van het geselecteerde object en voeg hem toe aan de VDM-bibliotheek. Je wordt om een naam gevraagd.

Zo ziet een typische werkwijze eruit:
- Voeg een vlak toe, of kies `Nieuwe VDM` in de VDM-kiezer om een kant-en-klaar vlak toe te voegen (het primitief [VDM](scene.md#add-menu))
- Boetseer je vorm erop en houd de rand plat
- Bak het!

De UV's van het vlak bepalen welk vierkant wordt gebakken, dus het object moet UV's hebben. Kies de grootte van de stempel met `Resolutie`, en kies met `Kleur`, `Ruwheid`, `Metaalheid` en `Dekking` wat de stempel naast de verplaatsing meeneemt.

::: tip
Gebruik geen DynTopo op het vlak: dat beschadigt de UV's en de stempel wordt vervormd. Boetseren in een laag geeft het nauwkeurigste resultaat, omdat het platte vlak er dan nog onder ligt. Ook schilderen moet in een laag, anders wordt het materiaal over het hele vierkant gestempeld in plaats van alleen waar je geschilderd hebt.
:::

## ![](/icons/dot.webp) Primitieven {#primitive}
Parameters van het geselecteerde primitief. De meeste zijn ook bereikbaar via de knop `…` van de werkbalk van het primitief in de viewport.

![](/images/topology_primitive_screenshot.webp)
