# ![](/icons/multires.webp) Topologie 

Dit menu beheert de topologie van objecten in Nomad, evenals tools om details te bakken en over te dragen tussen objecten en tussen textures.

![](/images/topology_overview.webp)

Nomad is gebaseerd op polygonen, het gebruikt driehoeken en quads om de geometrie te verwerken.
Met topologie bedoelen we zowel het aantal vlakken als de manier waarop punten (vertices) met elkaar verbonden zijn.

Het is belangrijk om de topologie in de gaten te houden, vooral als je fijne details wilt beeldhouwen of schilderen.

::: tip Hoe houd je je topologie in de gaten?
Je kunt de [Wireframe](settings.md#wireframe) weergeven of eenvoudigweg [Smooth Shading](settings.md#smooth-shading) uitschakelen.
:::

![](/images/topology_top.webp)

Het topologiemenu van Nomad heeft verschillende secties:

| Methode                                | Icoon                         | Beschrijving                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Bewerk meerdere detailniveaus met behulp van subdivisie          |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Bereken een nieuwe topologie met uniforme dichtheid              |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Voeg lokaal vlakken toe of verwijder ze in real-time tijdens sculpten of schilderen |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimatie, UV’s, baking, remeshen, reprojection                  |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Primitive-opties                                                 |


## Polygonstatistieken

![](/images/topology_stats.webp)

Het bovenste gedeelte van het topologiemenu toont polygoninformatie voor het geselecteerde object en de volledige scène. De getallen tonen het totale aantal vertices, het totale aantal driehoeken en het totale aantal quads (4-zijdige polygonen).

Tik op dit gedeelte om een lijst met polygonstatistieken voor alle polygonobjecten in de scène weer te geven.

## ![](/icons/multires.webp) Multiresolution

![](/images/topology_multires_menu.webp)

### Wat is multiresolution?
De multiresolutionfunctie is nuttig voor twee hoofdscenario’s:
- Het smooth-subdivisie-algoritme om het polycount van je object te verhogen
- Meerdere resolutieniveaus beheren zodat je kunt afwisselen tussen kleine en grootschalige bewerkingen

![](/videos/multiresolution.mp4)

#### Multiresolution-workflow
Een belangrijk aspect van multiresolution is dat je kunt teruggaan naar een lagere resolutie, wijzigingen aanbrengen aan je object en vervolgens teruggaan naar de hoogste resolutie zonder de hoge-resolutiedetails te verliezen. Alle hoge-resolutiedetails worden automatisch geprojecteerd.

::: warning
Als je een tool gebruikt die de topologie van je object wijzigt, verlies je alle andere resolutieniveaus van je object!
Je zou altijd een waarschuwing moeten krijgen als dit zou gebeuren, bijvoorbeeld wanneer je:
- de [Voxel Remesher](#voxel-remesher) gebruikt
- de [Dynamic Topology](#dynamic-topology) gebruikt
- de [Trim-tool](tools.md#trim) gebruikt
- de [Split-tool](tools.md#split) gebruikt
:::


### Multiresolution-slider
Deze slider geeft het aantal subdivisieniveaus in het huidige object aan. Als er 6 verticale balken zijn, zijn er 6 subdivisieniveaus. De cirkel geeft het momenteel weergegeven subdivisieniveau aan. 

### Reverse
Wanneer je op het laagste subdivisieniveau zit, zal de reverse-knop proberen een niveau onder het huidige te creëren. Merk op dat dit over het algemeen alleen kan als het object oorspronkelijk met subdivisie is gemaakt, bijvoorbeeld in Nomad of in andere 3D-applicaties die multiresolution-subdivision surfaces gebruiken.

### Subdivide
De *Subdivide*-knop zal het aantal polygonen met 4 vermenigvuldigen, houd dus het polycount in de gaten, want dit kan heel snel toenemen!
Een belangrijk aspect van *Subdivision Surface* is dat deze zullen convergeren naar een *Smooth Surface*.
Om te begrijpen hoe dit werkt, kun je de *Subdivide*-knop proberen op een object met slechts een paar polygonen.

Je kunt dit *Smooth*-gedrag uitschakelen door de optie `Linear subdivision` aan te vinken.

### Delete lower
Als er subdivisies onder het momenteel weergegeven niveau zijn, verwijder deze dan. Als je dit per ongeluk doet, kun je ze opnieuw aanmaken met de Reverse-knop.

### Delete higher
Als er subdivisies boven het momenteel weergegeven niveau zijn, verwijder deze dan.

### Linear subdivision
Subdivide de mesh zonder smoothing toe te passen.

### Sharp border
Als je object facegroups heeft, zal het inschakelen van deze optie de facegroup-randen scherp houden. Dit kan op elk subdivisieniveau worden ingesteld (de subdivisieslider zal een klein icoon boven het niveau hebben om dit aan te geven).

### Keep triangles
De meeste standaard subdivision-surface-systemen zullen proberen alle polygonen naar quads om te zetten tijdens een subdivisieoperatie. Deze schakelaar zal afdwingen dat de subdivisie driehoeken gebruikt in plaats daarvan.

### Lock (LV0)

Voorkom dat het laagste subdivisieniveau wordt gewijzigd. Dit kan belangrijk zijn als je object in een andere applicatie is gegenereerd en het basisobject ongewijzigd moet blijven. Wanneer deze optie is uitgeschakeld, zullen grote wijzigingen op hogere subdivisieniveaus niveau 0 verplaatsen.

::: tip 

Subdivision zal standaard alle scherpe randen verzachten. Om randen enigszins scherp te houden, kun je experimenteren met het gebruik van linear subdivision of Sharp border op de eerste 2 subdivideniveaus, en het vervolgens uitschakelen voor de hogere niveaus. Dit creëert een half-scherpe gesubdivideerde mesh.

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
Bij gebruik van de `Voxel Remesher` zal de volledige mesh worden gedwongen een uniforme resolutie te hebben, wat betekent dat alle polygonen min of meer dezelfde grootte hebben. Dit is erg handig wanneer je niet over topologie wilt nadenken en gewoon vrij wilt sculpten.

Een typische sculptworkflow kan beginnen met het gebruik van de `Voxel Remesher` om met een lage resolutie een ruwe vorm te blokkeren.
Druk af en toe op de *Remesh*-knop wanneer je de mesh te veel uitrekt om te veel vervorming te voorkomen.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Zoals hierboven vermeld, is Nomad polygonale software, maar de `Voxel Remesher` is een uitzondering waarbij tijdelijk een andere benadering wordt gebruikt om het remeshen uit te voeren.

Een groot verschil is dat de voxelbenadering geen zelf-intersecties accepteert, dus deze zullen worden opgelost.
Ook ondersteunt het geen meshes met gaten.

Met gaten bedoelen we niet de `genus hole` (`gat` van een donut), maar meshes die niet `waterdicht`/`gesloten` zijn.
Typisch betekent dit dat vóór het toepassen van het remeshen alle gaten worden gevuld, vergelijkbaar met de [Trim-tool](tools.md#trim) of de [Hole filling-functie](scene.md#hole-filling).
:::

### Remesh
Voer de voxel-remesh uit.

### Resolution
De grootte van de voxels die tijdens de berekening worden gebruikt. Tijdens het wijzigen van deze parameter wordt een schaakbordpatroon over de mesh gelegd om een voorbeeld van het resultaat te geven.

### Build multiresolution
Maak lagere multiresolutionniveaus voor de voxel-remesh. Als je het schaakbordpatroon gebruikt om een resolutie in te stellen en build multiresolution op 2 zet, zal het eindresultaat details hebben die overeenkomen met de resolutieslider, en als je naar het multires-tabblad gaat, zal het op niveau 2 staan, wat betekent dat je lagere resolutie-multimeshes hebt op niveau 1 en niveau 0. Dit kan een goede manier zijn om zowel een schone mesh met gelijkmatige polygonen te genereren als een low-res control mesh te hebben.

::: tip Tip: Build multiresolution en stable smoothing

Deze optie kan soms ‘loops’ in de geometrie veroorzaken die moeilijk glad te strijken zijn, wat kleine puistjes veroorzaakt. Als dit gebeurt, schakel dan ‘Stable smoothing’ in de smooth-toolopties in. 

:::

### Keep sharp edges
Schakel het snappen van de nieuwe punten naar scherpe randen op de originele mesh in. Dit kan vervorming introduceren.

## ![](/icons/dynamic.webp) Dynamic Topology

![](/images/topology_dyntopo_menu.webp)
Multiresolution en voxel-remeshen zijn gangbare industriemethoden om topologie te beheren, maar beide vereisen dat je oplet dat je polygonen niet te ver uitrekt of te strak samenperst. 

Dynamic Topology is een alternatieve methode. Terwijl je sculpt, zal Nomad adaptief polygonen toevoegen en verwijderen tijdens de penseelstreek, zodat het uitsnijden van kleine details veel kleine polygonen toevoegt waar je ze nodig hebt, en smoothing elders polygonen verwijdert.

Merk op dat dynamic topology driehoekspolygonen zal gebruiken in plaats van quads. Dit kan er wat rommelig uitzien, maar het is bijna beter om niet naar de wireframe te kijken en je gewoon te concentreren op het maken van een mooi ogende sculpt zonder je zorgen te maken over topologie; later kun je een van Nomads andere remeshingtools gebruiken om een schone quadmesh te genereren.

Zie de onderstaande video in actie.

![](/videos/dynamic.mp4)

### Enabled
Schakel dynamic topology in. Er wordt een DynTopo-icoon onder de sliders voor penseelradius en intensiteit geplaatst om Dyntopo per tool te kunnen in- of uitschakelen.

### Detail
Bepaalt de hoeveelheid detail; het gedrag verandert op basis van de selectie ‘Detail based on...’, zie hieronder.

### Detail based on...
| Methode   | Beschrijving                                                     |
| :-------: | :--------------------------------------------------------------: |
| Screen    | Het detailniveau hangt af van hoe groot het object op het scherm is. De detailslider is 100% of hoger voor fijn detail (kleine driehoeken) of 1% voor laag detail (grote driehoeken).  |
| Radius    | De toolradius bepaalt de hoeveelheid detail. Gebruik een kleine toolradius voor fijn detail, een grote toolradius voor laag detail. De detailslider is een vermenigvuldigingsfactor op deze verhouding.                     |
| Constant  | De detailslider bepaalt de hoeveelheid detail en wordt niet beïnvloed door schermgrootte of toolgrootte.             |

::: tip TIP: Radius-modus

Om beter te begrijpen hoe de radius-modus werkt, begin je de detailslider met één vinger te bewegen en verander je tegelijkertijd de toolradius met een andere vinger. Je zult zien hoe ze gekoppeld zijn.

:::

### Prefer...
| Methode | Beschrijving        |
| :-----: | :-----------------: |
| Speed   | Geef performance voorrang |
| Quality | Geef kwaliteit voorrang   |

Wanneer je `Quality` verkiest, zijn de 2 belangrijkste verschillen:
- verfijning wordt toegepast vóór het sculpten, zodat je minder interpolatie-artefacten krijgt bij het schilderen of sculpten van zeer kleine details
- verfijning wordt uitgevoerd totdat deze convergeert naar het juiste detailniveau, in tegenstelling tot een incrementeel gedrag.
 
Op die manier zal, als je zeer kleine details sculpt of snelle streken maakt, de topologie altijd worden verfijnd zoals verwacht.


### Use pressure on radius
Alleen relevant als `Radius` is geactiveerd. Indien ingeschakeld, zal het detailniveau altijd de penseelgrootte weerspiegelen, zelfs wanneer de penseelgrootte wordt beïnvloed door pen-druk.

### Use stroke falloff

Neem ook de penseel-falloffcurve en alpha op in de dyntopo-berekeningen.

### Method
Of je nu `Dynamic Topology` gebruikt op je [Brush](#brush) of [Globally](#global), je kunt kiezen in welke modus deze werkt:

| Methode        | Beschrijving                                                           |
| :------------: | :--------------------------------------------------------------------: |
| Uniformisation | Kan vlakken toevoegen en verwijderen, dit is de modus die in de video hierboven wordt gebruikt |
| Subdivision    | Voegt alleen nieuwe vlakken toe, kan geen vlakken verwijderen         |
| Decimation     | Verwijdert alleen vlakken, kan geen vlakken toevoegen                 |

### Protect masked area
Schakel in dat gemaskeerde gebieden worden beschermd tegen wijzigingen in de topologie.

### Vertex extrapolation


### Detail
De resolutie die wordt gebruikt voor de remesh-operatie. Als Dyntopo in ‘Constant’-modus staat, zal dit dezelfde waarde zijn als de detailslider bovenaan dit menu.

### Remesh
Voer een globale remesh uit met behulp van het dyntopo-algoritme. Meestal zou je de [Voxel Remesher](#voxel-remesher) moeten gebruiken voor volledig remeshen.

Een voordeel ten opzichte van voxels is echter dat het gemaskeerde gebied wordt beschermd, zodat je beter kunt bepalen waar je meer of minder dichtheid wilt.



## ![](/icons/topo_extra.webp) Misc

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Tandwielmenu
Veel van de tools in dit menu hebben extra opties. Ze zijn toegankelijk via het tandwielicoon naast de sectietitel.

### Decimation

![](/images/topology_decimation.webp)

Verminder het aantal polygonen door te proberen zoveel mogelijk details te behouden, met gebruik van driehoekspolygonen.

Deze functie kan nuttig zijn als je wilt exporteren voor 3D-printen.
Je zou het echter waarschijnlijk niet moeten gebruiken als je verder wilt sculpten, omdat het oneffen driehoeken kan produceren.

Merk op dat de gemaskeerde gebieden niet worden gedecimeerd.

![](/videos/decimate.mp4)

::: tip

Het gebruik van de [Quadremesh-tool](tools.md#quad-remesher) op high-poly-objecten kan lang duren om te berekenen en resultaten opleveren die moeilijk te controleren zijn. Voorbewerking van de mesh met [facegroups](tools.md#facegroup-1) en decimate zal Quadremesh veel sneller laten draaien en veel meer controle over de topologie geven.

* Maak facegroups op de mesh om je ideale quad-flow te definiëren.
* Facegroup relax om gladde facegroup-randen te krijgen.
* Decimate. Dit zorgt ervoor dat je geen dunne of vervormde vlakken op de facegroup-rand hebt. Zorg er in de decimate-instellingen voor dat facegroup is ingeschakeld. Dit zorgt ervoor dat driehoeksranden je facegroup-randen precies volgen.
* Zorg er in de Quadremesh-opties voor dat relax is uitgeschakeld (omdat je de mesh al hebt relaxed) en je zou goede resultaten moeten krijgen.

:::

#### Decimate
Start de decimate-operatie.

De iconen naast de decimate-knop laten je opties in- of uitschakelen die de decimatie beïnvloeden. Het percentage geeft aan hoe sterk die optie is en kan worden ingesteld in het geavanceerde tandwielmenu.

* ![](/icons/palette.webp)  `Preserve Painting` - Plaats meer driehoeken waar er schilderdetails zijn.
* ![](/icons/triforce.webp) `Uniform Faces` - Geef de voorkeur aan gelijkmatig grote driehoeken.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate zal proberen randen nabij open geometrie en gaten ongewijzigd te laten.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate zal proberen facegroup-randen ongewijzigd te laten.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Decimate zal proberen UV-randen ongewijzigd te laten.

#### ![](/icons/cog.webp) Decimate-tandwielmenu
Het tandwielmenu heeft deze geavanceerde opties:
##### Preserve painting
Het selectievakje schakelt deze modus in of uit; de waarde bepaalt hoe nauwkeurig schilderdetails behouden blijven. Hogere waarden behouden meer schilderwerk. Stel in op 0 als je niet om schilderwerk geeft.


##### Uniform faces
Het selectievakje schakelt deze modus in of uit. Hogere waarden leveren driehoeken op met vergelijkbare grootte.

##### Preserve borders
Schakel in om te voorkomen dat randen worden gedecimeerd. Randgewichten kunnen worden geselecteerd voor `Geometry`-, `Face Group`- of `UV`-randen.

#### Target triangles
Stel het gewenste aantal driehoeken in. De standaardwaarde is 50%; de procent/target-knop schakelt tussen een percentage of een exact doelpolycount.



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
Bereken texturecoördinaten (UV’s) voor de huidige mesh, waarbij over het algemeen de voorkeur wordt gegeven aan meer eilanden met sneden om vervorming te minimaliseren.

Het kleine oogicoon tussen de menutitel en het tandwielmenu schakelt het voorvertonen van UV’s op het object in of uit.

![](/videos/unwrap.mp4)

#### Unwrap
Bereken UV’s voor het geselecteerde object, die op de achtergrond worden weergegeven.

#### Delete UVs
Verwijder UV’s op het object.

#### ![](/icons/cog.webp) UVAtlas-tandwielmenu
Het tandwielmenu heeft deze geavanceerde opties:

#### Face Group

Gebruik facegroups om de sneden voor de UV’s te definiëren.

##### Max Stretch
Lage waarden creëren minder vervorming en meer eilanden, hoge waarden creëren meer vervorming en minder eilanden. 

##### Island spacing
De hoeveelheid ruimte tussen de eilanden. Lage waarden verspillen minder ruimte, maar vergroten het risico dat textures tussen eilanden doorbloeden. 

::: warning
Het berekenen van UV’s kan enige tijd duren; het is het beste om een mesh met minder dan 100k vertices te hebben.
:::

::: tip UVs?
Een veelgebruikte analogie voor UV’s is het inpakken van een cadeau; wat is de beste manier om inpakpapier te snijden om een object volledig te bedekken, zonder overlappingen? 

UV’s zijn vergelijkbaar, maar in plaats van het papier te snijden, snij je het object. Stel je voor dat je model van dun plastic is gemaakt: hoe zou je je model in stukken snijden om het plat te vouwen, het in die platte toestand te beschilderen en het vervolgens weer in elkaar te zetten?

Stel je nu voor dat het oppervlak van je model van rekbare lycra is gemaakt. Je zou het model plat kunnen trekken, of snijden, of een combinatie van beide. Maar als je een schaakbord op het object zou schilderen wanneer het plat is, zou het schaakbord vervormd zijn wanneer je het weer in elkaar zet. Welke methode is beter: meer sneden met minder vervorming, of minder sneden met meer vervorming?

UV’s zijn instructies om 3D-software te vertellen hoe het object moet worden ‘gesneden en uitgerekt’ bij het toepassen van textures. De UV Atlas-tool gebruikt over het algemeen een benadering van ‘meer sneden, minder vervorming’.


:::

::: tip UV’s en Nomad en andere apps

De meeste getextureerde modellen die je online vindt, zijn getextureerd met UV’s. Nomad kan dit importeren en weergeven via het [material](material#textures)-paneel.

Wanneer modellen in Nomad worden gemaakt, kun je direct op objecten schilderen zonder UV’s. Als je ze moet exporteren naar andere apps, bijvoorbeeld [Procreate](https://procreate.art/), kun je Nomad-kleureninformatie in textures ‘bakken’ via UV’s. 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

BFF-UV’s geven de voorkeur aan een benadering van ‘minder sneden, meer vervorming’. 

#### ![](/icons/cog.webp) UV BFF-tandwielmenu

#### Face Group

Gebruik facegroups om de sneden voor de UV’s te definiëren.

##### Cone count
Bepaal het aantal hoofdprojecties dat wordt gebruikt. Lagere waarden produceren minder eilanden, maar meer vervorming.

##### Seamless patches
Beïnvloedt de lay-out van de UV-patches, werkt het best met zorgvuldig gemaakte facegroups.

### Bake -> texture 
![](/images/topology_bake_menu.webp)

Texture baking zal textures creëren door andere zichtbare objecten in de scène te projecteren in de UV’s van het geselecteerde object.

Hier is de typische workflow voor baking:
- Je hebt een mesh met fijne details en schilderwerk
- Clone deze
- Decimate deze (zet `Preserve painting` op 0)
- UV unwrap deze
- Bake!

Nomad zal standaard elk zichtbaar mesh in de scène in aanmerking nemen.
Je kunt ook de Solo-modus gebruiken om snel de meeste andere meshes te verbergen.
Als er geen andere zichtbare objecten zijn, dan wordt de volledige scène in aanmerking genomen.

Je zou nu een low-res mesh moeten hebben die het grootste deel van de verf en details van je vorige object behoudt.

Na de operatie worden vertexkleuren verplaatst naar een nieuwe uitgeschakelde laag, zodat ze niet interfereren met de textures.

#### From itself
Bake het hoogste multiresolutionniveau naar het laagste niveau op het huidige object. Dit is eenvoudig in te stellen, maar vaak heb je meer controle nodig; in dat geval is de volgende optie nuttiger.

#### From high-res ()
Bake van de andere zichtbare objecten in de scène naar het geselecteerde object. Het getal tussen haakjes geeft het aantal andere zichtbare objecten aan dat als high-res-doel wordt gebruikt en in het huidige low-res-object met UV’s wordt gebakken. De andere objecten hoeven niet vergelijkbaar te zijn in lay-out of topologie met het object dat wordt gebakken, wat veelzijdige bake-workflows mogelijk maakt.

#### Resolution
De resolutie van de gebakken texture. Bake-textures zijn altijd vierkant, dus 1024 zal een afbeelding van 1024x1024 maken. 

De knoppen hieronder zijn snelkoppelingen voor veelgebruikte resoluties. Ter referentie: 512x512 is relatief klein, bijvoorbeeld voor webgraphics en eenvoudige geometrie. 4096x4096 (afgekort 4k) is voor hoogwaardige renders.

#### ![](/icons/cog.webp) Bake-tandwielmenu
![](/images/topology_bake_gear_menu.webp)
Het tandwielmenu heeft deze geavanceerde opties:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
Deze selectievakjes bepalen welke eigenschappen worden gebakken, elk in aparte maps. Nadat de bake is voltooid, worden deze als textures toegevoegd aan het materiaal van het huidige object.

##### Backup
Om de gebakken textures te kunnen voorvertonen, moet de verfinformatie van het object worden uitgeschakeld. Deze optie verplaatst alle verfinformatie naar een nieuwe laag als back-up, zodat deze eenvoudig kan worden in- of uitgeschakeld.

#### Cage radius
Pas aan hoe ver van het bake-object stralen worden verzonden om doelobjecten te zoeken. Standaard wordt deze afstand laag gehouden om artefacten te vermijden, maar kan worden vergroot als de doelobjecten ver van het bake-object verwijderd zijn.

##### Ray offset
Pas aan waar de bake-berekeningen op het bake-object beginnen. Standaard beginnen ze 5% van het oppervlak af, wat de meeste veelvoorkomende artefacten voorkomt. Als de doelobjecten erg ver van het bake-object verwijderd zijn, moet deze offset mogelijk worden vergroot.


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

Project gesculpteerde details, schilderwerk, lagen en textures naar vertexwaarden.

Je kunt het zien als het omgekeerde van baking; als baking vertexeigenschappen naar textures overdraagt, draagt reproject textures (en andere eigenschappen)
 terug naar vertices over.

::: tip
Bij gebruik van `Bake to texture` of `Reproject to vertex` worden zowel de vertexkleuren als de materiaaltextures in aanmerking genomen.
:::

#### From itself
Zet textures van het materiaal om in vertexwaarden. Deze knop is alleen actief als het object UV’s heeft en textures actief zijn in het materiaal.

::: tip TIP: Texture painting
Nomad ondersteunt niet direct het schilderen en bewerken van textures, maar zeer vergelijkbare resultaten kunnen worden bereikt door textures -> vertexwaarden te projecteren, op vertices te schilderen en vervolgens vertex -> textures te bakken:

1. Stel een low-poly-object met UV’s in
1. Laad textures in het materiaal
1. Subdivideer het genoeg om op te kunnen schilderen
1. `Reproject to vertex` in de modus `From itself`; nu is de texture omgezet in vertexwaarden
1. Schilder, smooth, smudge, stempel, doe alle bewerkingen die je nodig hebt
1. `Bake to texture`, in de modus `From itself`. Die bewerkingen worden terug omgezet in textures.
:::

#### From high-res ()
Zet alle zichtbare objecten om in vertexwaarden op het geselecteerde object. Het getal op deze knop geeft het aantal zichtbare objecten aan.

::: tip
Het reprojection van andere objecten kan niet alleen worden gebruikt om kleurinformatie van andere objecten over te dragen, maar ook om vertices op andere objecten te projecteren, bijvoorbeeld verbanden die op een personage worden geprojecteerd.
:::

#### ![](/icons/cog.webp) Reproject-tandwielmenu
Het tandwielmenu heeft deze geavanceerde opties:

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
Deze selectievakjes bepalen welke eigenschappen naar het geselecteerde object worden geprojecteerd. 

#### Relax
De geselecteerde mesh kan in zekere mate worden gladgestreken of ‘relaxed’ om beter bij de reprojection-doelen te passen. Smooth is beter voor high-poly-meshes. Relax is beter voor low-poly-meshes. Auto laat Nomad de beste methode bepalen.

#### Iterations
Hoe vaak de relax-operatie moet worden toegepast tijdens de reprojection.

#### Cage radius
Pas aan hoe ver van het geselecteerde object stralen worden verzonden om doelobjecten te zoeken. Standaard wordt deze afstand laag gehouden om artefacten te vermijden, maar kan worden vergroot als de doelobjecten ver van het bake-object verwijderd zijn.

#### Ray bias
Lagere waarden geven de voorkeur aan projectie naar het dichtstbijzijnde punt op het doeloppervlak. Hogere waarden geven de voorkeur aan een snijpunt met gebruik van de oppervlaknormaal. 

#### Ray offset
Pas aan waar de bake-berekeningen op het geselecteerde object beginnen. Standaard beginnen ze 5% van het oppervlak af, wat bepaalde artefacten voorkomt. Als de doelobjecten erg ver van het geselecteerde object verwijderd zijn, moet deze offset mogelijk worden vergroot.


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
Remesh met behulp van het [Instant Meshes-algoritme van Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Het zal de flow van een mesh analyseren en een schone quadtopologie creëren.

::: tip
Op iOS en desktop geeft de [Quad remesher](tools#quad-remesher)-tool betere resultaten en meer controle.
:::

#### Remesh
Start de instant-meshes-operatie.

#### Target quads
Het aantal quadpolygonen dat quad remesh zal proberen te creëren.

#### ![](/icons/cog.webp) Quad Remesh Instant-tandwielmenu
Het tandwielmenu heeft deze geavanceerde opties:

##### Crease angle
Een drempel voor scherpe hoeken die zal proberen de remesh-operatie te sturen.

#### Max fill hole
Het algoritme kan soms ongewenste gaten produceren. Als een gat minder vertices heeft dan deze waarde, dan wordt het gevuld.

### Holes
![](/images/topology_holes_menu.webp)
Meestal zal je object waarschijnlijk waterdicht zijn, wat betekent dat de mesh ‘gesloten’ is.

Als je object gaten heeft, kun je deze vullen. Merk op dat dit alleen werkt op ‘naïeve’ gaten; het kan dus geen twee afzonderlijke randen ‘lassen’.

![](/videos/hole_filling.mp4)

::: tip
Wanneer je de Voxel Remesher uitvoert, worden alle gaten automatisch gesloten, of je deze nu op 1 of meerdere meshes gebruikt.
:::

#### Close holes
Voer de hole-close-actie uit.

#### ![](/icons/cog.webp) Holes-tandwielmenu
Het tandwielmenu heeft deze geavanceerde opties:

##### Detail
De polygondichtheid die wordt gebruikt om het gat te vullen. Tijdens het slepen van deze slider wordt een schaakbordpatroon op het model weergegeven; dit geeft een indicatie van de driehoeksgrootte die moet worden gebruikt. Het selectievakje schakelt dit uit en gebruikt alleen de bestaande punten, wat meestal lange dunne driehoeken over het gat creëert, die moeilijk te sculpten zijn.

##### Fill non-manifold
Probeer non-manifold-gaten te vullen.

##### Face Group

Bij het vullen van gaten: moet elk gat zijn eigen facegroup krijgen (Auto), moeten ze allemaal een facegroup delen (Off), of moeten er geen facegroups worden gemaakt (On).

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
Probeer non-manifold-randen op te schonen. Dit kan nuttig zijn voor externe software die geen randen ondersteunt die meer dan 2 vlakken gemeen hebben.

#### Clean
Voer de clean-actie uit.
#### ![](/icons/cog.webp) Force manifold-tandwielmenu
Het tandwielmenu heeft deze geavanceerde opties:

#### Delete small faces
Een drempel die wordt gebruikt om kleine polygonen te verwijderen en samen te voegen.


### Triplanar
![](/images/topology_triplanar_menu.webp)
Zet de mesh om in een [triplanar](scene.md#triplanar)-primitive.
Je zult waarschijnlijk veel detail verliezen in het proces.

#### Force cubic
Zorg ervoor dat de triplanar een kubus is. Anders zal de triplanar worden aangepast aan de dichtstbijzijnde bounding box rond je object.

#### Convert
Voer de triplanar-actie uit.

#### Resolution
De voxelgrootte die wordt gebruikt in de triplanar-operatie.

## ![](/icons/dot.webp) Primitive
Parameters voor de geselecteerde primitive. Deze zijn ook beschikbaar in de primitive-viewporttoolbar.

![](/images/topology_primitive_screenshot.webp)
