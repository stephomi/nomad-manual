# ![](/icons/material.webp) Materiaal {#material}

In dit menu verander je het materiaal van het huidige object, stel je de renderinstellingen van het object en materiaal in, en koppel je texturen aan het materiaal.

![](/images/material_overview.webp)

Een materiaal bepaalt hoe een object eruitziet: hoe het reageert op licht en op andere objecten. Het uiterlijk van een object hangt af van deze eigenschappen:

* `Materiaaltype`
* `Kleur`
* `Ruwheid`
* `Metaalheid`
* `Dekking`
* `Reflectantie`
* `Lichtgevend/onverlicht`

Door ze te combineren kom je tot heel uiteenlopende resultaten, van fotorealistisch tot cartoonachtig of experimenteel.

Kleur, ruwheid, metaalheid en dekking kun je schilderen, zie de [opties voor vertex-schilderen](painting.md) voor meer informatie.

Materiaaltype, reflectantie en lichtgevend/onverlicht zijn materiaaleigenschappen die hieronder worden uitgelegd.

Met de knoppen `Kopiëren` en `Plakken` bovenaan dit menu kopieer je een materiaal van het ene object naar het andere.

Houd er rekening mee dat de renderer van Nomad een realtime renderer is: hij is krachtig, maar kiest bij sommige effecten voor snelheid boven nauwkeurigheid.

## Materiaaltypes {#material-types}

![](/images/material_types.webp)

De materiaaltypes van Nomad zijn Ondoorzichtig, Suboppervlak, Mengmodus, Additief, Breking, Dithering en Schaduw Vanger.

### ![](/icons/material_opaque.webp) Ondoorzichtig {#opaque}
De standaardmodus, die het oppervlak behandelt als een eenvoudig materiaal met geschilderde kleur, ruwheid, metaalheid en dekking. Geschilderde dekking, een dekkingstextuur of het alfakanaal van de kleurtextuur maken het object nog steeds doorzichtig, via dithering. Alleen de algemene dekkingsschuifregelaar wordt genegeerd.

### ![](/icons/material_subsurface.webp) Suboppervlak {#subsurface}
Deze modus bootst materialen na waarin licht zich binnenin verspreidt en vervaagt, zoals huid, was of jade.

Hij vereist de PBR-shadingmodus. Voor het beste resultaat gebruik je minstens één gericht licht of spotlicht, het liefst met een gedimde omgeving.

Het kleurvakje bepaalt de kleur van het verstrooide licht.

`Diepte` bepaalt hoe ver het licht vanaf de voorkant onder het oppervlak doordringt en daarna weer naar buiten komt aan de voorkant. Zo worden harde schaduwen zachter en vervagen de details van het oppervlak.

`Translucentie` bepaalt hoe het licht zich van de voorkant naar de achterkant van een vorm verspreidt, zoals licht dat door de onderkant van een blad schijnt, of oren met sterk tegenlicht. Je hebt een licht nodig dat schaduwen werpt om dit te zien.

### ![](/icons/material_blending.webp) Mengmodus {#blending}

Lijkt op Ondoorzichtig, maar werkt met de dekkingsschuifregelaar, zodat het materiaal kan overgaan van massief naar doorzichtig. Het is één eenvoudige schuifregelaar voor de dekking, in plaats van de schilderbare dekking van het ondoorzichtige materiaal.

::: warning
De mengmodus kan flikkeren en verspringen bij complexe of elkaar snijdende vormen.
:::

### ![](/icons/material_additive.webp) Additief {#additive}
Met dit materiaal maak je je mesh halfdoorzichtig. Het lijkt op de mengmodus, maar waar die mengt met de omgeving, is additief altijd lichter dan de objecten erachter. Ideaal voor felle effecten zoals lichtstralen, vuur of explosies.

Je kunt een dekking hoger dan 1 instellen, waardoor het object helderder wordt.  
Dat is handig als je [bloom](postprocess.md#bloom) en de parameter `Drempel` gebruikt om alleen dit object te laten gloeien, zoals een lichtgevend object.

Deze modus geeft meestal minder artefacten dan de [Mengmodus](#blending) (transparantie die niet afhangt van de volgorde).

### ![](/icons/material_refraction.webp) Breking {#refraction}
Met deze modus boots je glas na. Hij vereist de PBR-shadingmodus. Omdat alles in realtime moet gebeuren, zijn breking binnen hetzelfde object en breking door meerdere lagen enigszins beperkt.

De geschilderde ruwheid van het model bepaalt hoe wazig de breking is.
Standaard heeft elk object dat je in Nomad maakt een ruwheid van ongeveer 25%, dus de breking is niet perfect maar wat wazig.
Met de knop `Glanzend schilderen` schilder je je model opnieuw met een ruwheid en metaalheid van 0 (de kleuren blijven ongewijzigd).

Er spelen twee soorten ruwheid mee: de ene bepaalt hoe wazig de reflectie op het oppervlak is, de andere hoe wazig de binnenkant is (de breking).  
Omdat Nomad maar één geschilderd ruwheidskanaal heeft, delen de binnen- en buitenkant dezelfde waarde.  
Wil je verschillende waarden (bijvoorbeeld een lolly met een scherp oppervlak maar een wazige binnenkant), gebruik dan de schuifregelaars `Oppervlak` en `Interieur` onder `Ruwheid overschrijven` om de geschilderde ruwheid te vervangen.

![](/videos/refraction.mp4)

#### Refractie-index {#index-of-refraction}
Hoe sterk het licht afbuigt wanneer het het object binnengaat. Hogere waarden buigen het meer af, zoals een dikke lens.

#### Absorptie {#absorption}
Bootst na dat het licht wordt geabsorbeerd terwijl het door het volume reist, gekleurd door het kleurvakje, met `Factor` voor de sterkte. Dunne delen zijn lichter omdat ze meer licht doorlaten, dikke delen zijn donkerder. Nomad gebruikt alleen een benadering van de dikte van het object, dus het effect hangt sterk af van de vorm.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Maakt het object halfdoorzichtig door willekeurig een deel van de pixels weg te laten.

### ![](/icons/material_shadow_catcher.webp) Schaduw Vanger {#shadow-catcher}

Maakt het object onzichtbaar, zodat het alleen nog schaduwen van lichten ontvangt. Handig om renders uit Nomad te combineren met andere afbeeldingen, meestal op een vlak. Het kleurvakje bepaalt de kleur van de schaduw.

Er moet een licht met schaduwen in de scène staan, anders doet de schaduwvanger niets. De knoppen `Metaalheid → 0%` en `Metaalheid → 100%` schilderen het object opnieuw: volledig metallisch kan de schaduwvanger ook de scène weerspiegelen wanneer de nabewerking [Reflectie (SSR)](postprocess.md#reflection-ssr) aanstaat.

::: tip

Meer informatie over transparantie en mengmodi vind je op https://support.fab.com/s/article/Transparency-Opacity

:::

## Bediening {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Altijd onverlicht {#always-unlit}
Als dit aanstaat, negeert het object PBR en MatCap en toont het gewoon de geschilderde kleur, zonder shading.
Gebruik je [Additief](#additive), dan kun je transparantie rechtstreeks schilderen met zwart.

### Dekking {#opacity}
Hoe massief of ondoorzichtig een object eruitziet: 100% is massief, 0% is doorzichtig. De schuifregelaar verschijnt bij de types Mengmodus, Additief, Dithering en Schaduw Vanger. Voor meer controle kun je de dekking ook schilderen.

### Pre-refractie-pass {#pre-refract-pass}
Alleen voor Mengmodus en Additief. Tekent dit transparante object vóór de brekingspass. Handig wanneer een brekend object vóór andere transparante oppervlakken staat.

### Reflectantie {#reflectance}
Bepaalt hoeveel reflectie een niet-metallisch materiaal krijgt. Meestal is de standaardwaarde goed (die komt overeen met de gebruikelijke 4% gereflecteerd licht bij loodrechte inval), maar je kunt hem verhogen om bijvoorbeeld reflecties en glanspunten in de ogen van een personage te versterken. Dit vereist de PBR-shadingmodus.

### ![](/icons/culling.webp) Omgekeerde culling {#inverse-culling}
Keert de normalen van een oppervlak om. Meestal niet nodig, maar handig als een model binnenstebuiten lijkt. In combinatie met `Twee zijden` uitgeschakeld kun je er interieurs mee maken waarbij de muur die het dichtst bij de camera staat altijd verborgen is.

De volgende opties kun je op `Auto`, `Nee` of `Ja` zetten. Bij `Auto` toont de pijl welke waarde echt wordt gebruikt.

### ![](/icons/sphere_smooth.webp) Vloeiende shading {#smooth-shading}
Zie de [algemene optie](settings.md#smooth-shading).  
Met `Auto` wordt de algemene optie gebruikt.

### ![](/icons/culling.webp) Twee zijden {#two-sided}
Vlakken zijn van beide kanten zichtbaar. Zie de [algemene optie](settings.md#two-sided-quick).  
Met `Auto` wordt de algemene optie gebruikt.

### ![](/icons/culling.webp) Gekleurde achterzijde {#coloured-backface}
Zie de [algemene optie](settings.md#two-sided-quick).
Met `Auto` wordt de algemene optie gebruikt.

### ![](/icons/shadow_cast.webp) Schaduwen werpen {#casts-shadows}
Ook transparante objecten werpen schaduwen (in een ditheringpatroon, om gemengde schaduwen na te bootsen).  
Zet het werpen van schaduwen uit bij grote objecten in je scène die geen schaduw hoeven te werpen (bijvoorbeeld een grote vloer).

### ![](/icons/shadow_receive.webp) Schaduwen ontvangen {#recieve-shadows}
Of schaduwen van andere objecten op dit object worden getekend.

### ![](/icons/wireframe.webp) Draadmodel {#wireframe}
Zie de [algemene optie](settings.md#wireframe).  
Met `Auto` wordt de algemene optie gebruikt.

### ![](/icons/trash.webp) Normalen herstellen {#reset-normals}
Verschijnt alleen wanneer een geïmporteerd object zijn eigen normalen meebrengt (bijvoorbeeld met `Behoud topologie`). Deze knop verwijdert ze, zodat de shading de normalen gebruikt die uit het oppervlak worden berekend.


## Texturen {#textures}

![](/images/material_textures.webp)

Heeft een object UV's, dan kun je naast de vertexkleur, -ruwheid, -metaalheid en -dekking ook texturen aan het materiaal koppelen. Meestal komen die uit het bakken van texturen, maar je kunt ook afbeeldingen gebruiken die buiten Nomad zijn gemaakt. `UV:✓` of `UV:✗` naast de titel laat zien of het object UV's heeft.

Texturen kun je toepassen op

* Kleur
* Normaal
* Ruwheid
* Metaalheid
* Dekking
* Verplaatsing
* Lichtgevend

Er verschijnt ook een rij `Occlusie` wanneer een geïmporteerd object een occlusietextuur heeft, maar Nomad gebruikt die niet.

De schuifregelaar van elke rij bepaalt hoe sterk de textuur wordt toegepast, van helemaal niet tot volledig. `Kleur` en `Lichtgevend` hebben ook een kleurvakje dat de textuur inkleurt, en bij `Lichtgevend` stelt het de sterkte van de gloed in.

`Verplaatsing` bepaalt hoe ver de verplaatsingsmap het oppervlak verschuift. De knop `Toepassen` verplaatst de vertices volgens de verplaatsing en verwijdert daarna de map. Het resultaat komt in de actieve laag.

De paletknop naast de titel opent de materiaalpresets van het menu [Schilderen](painting.md): tik op een preset om de texturen ervan naar het object te kopiëren. Op desktop worden geïmporteerde afbeeldingen gesynchroniseerd met hun originele bestand zodra je terugschakelt naar Nomad, en een synchronisatieknop naast de titel laadt ze opnieuw.

Tik je op een textuurvak, dan verschijnt een kiezer. Is er al een textuur aan het vak gekoppeld, dan opent een nieuwe tik het textuurpaneel:

### Opties van het textuurpaneel {#texture-panel-options}

![](/images/material_texture_panel.webp)

Het paneel toont de afmetingen van de afbeelding en een voorbeeld van de textuur.

### ![](/icons/open.webp) Openen {#open}
Kies een andere textuur. Op desktop toont `Verken` het afbeeldingsbestand in je bestandsbeheerder.

### ![](/icons/circle_cross.webp) Geen {#none}
Verwijdert de textuur.

### Dekking {#texture-opacity}

Alleen voor de kleurtextuur. Heeft de afbeelding een alfakanaal, dan kun je het gebruiken voor de dekking, of het negeren.

### Formaat {#normal-format}
Alleen voor de normaaltextuur. Normal maps bestaan in twee varianten, `OpenGL (+Y)` en `DirectX (-Y)`. Lijken de details omgekeerd, probeer dan de andere.

### Hoogte {#displacement-height}
Alleen voor de verplaatsingstextuur.
* `Lokaal` - De hoogte groeit en krimpt mee met de schaal van het object.
* `Wereld` - De hoogte blijft gelijk, wat de schaal van het object ook is.

### Vermenigvuldigen {#multiply}
Alleen voor ruwheids-, metaalheids- en dekkingstexturen. Vermenigvuldigt de waarden van de textuur. Staat het niet op 100%, dan wordt de waarde op het textuurvak getoond.

### ![](/icons/link.webp) Ketting-/koppelingsicoon {#chainlink-icon}

Staat het koppelingsicoon in de volgende secties aan, dan worden de gekozen opties gedeeld met de andere texturen (kleur, normaal, ruwheid, metaalheid, dekking, lichtgevend) waarvan het koppelingsicoon ook aanstaat.

Zo blijven op elkaar uitgelijnde texturen uitgelijnd, ook als je de parameters of het projectietype aanpast.


### Projectie {#projection}
![](/images/material_projection.webp)

Bepaalt hoe de textuur op het object wordt aangebracht.

* `Auto` - UV als het object UV's heeft, anders Triplanar
* `UV` - Gebruikt de UV-coördinaten van de mesh om de textuur aan te brengen. Komen de mesh en de textuur van buiten Nomad, of ga je ze vanuit Nomad exporteren om elders te gebruiken, dan is UV de juiste keuze.
* `Triplanar` - Projecteert de textuur langs de X-, Y- en Z-as en laat de naden in elkaar overlopen.

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanaire projectie is een krachtige en toch eenvoudige manier om texturen op objecten aan te brengen.

Het is alsof zes projectoren met hetzelfde beeld op de voorkant, achterkant, linkerkant, rechterkant, bovenkant en onderkant van je object schijnen.

Indien nodig kun je het resultaat daarna bakken naar UV's of vertexkleuren.


![](/images/material_triplanar_example.webp)

#### Methode {#method}

* `Lokaal` - De projectie beweegt mee met de transformatie van het object.
* `Wereld` - De projecties blijven op hun plek: verplaats je het object, dan schuift het door de projectie.

#### Hardheid {#hardness}

Hoe de projecties in elkaar overlopen. Bij 100% is er geen overgang en zijn de randen van de projecties scherp. Bij 0% lopen de randen over een brede hoek in elkaar over. De standaardwaarde is 90%: genoeg menging om de randen te verbergen, terwijl de rest van de projecties scherp blijft.

### Uniform {#uniform}

Aangevinkt geldt dezelfde hardheid voor alle projecties. Uitgevinkt verschijnen extra hardheidsregelaars voor de X-, Y- en Z-projecties.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filteren {#filtering}
De filtermethode voor de textuur. `Auto` is de standaard, de methodes zijn `Dichtstbijzijnd`, `Lineair` en `Mipmap`. Dichtstbijzijnd filtert niet, dus van dichtbij kunnen texturen kartelig worden. Lineair en Mipmap filteren beter, zodat texturen van dichtbij wazig lijken in plaats van kartelig.

#### Patroontegels - X {#tiling-x}
Als de parameter Schaal groter is dan 1, wordt de textuur kleiner dan de UV's van het object. Deze optie bepaalt dan hoe de textuur zich herhaalt langs de X-as. `Geen` herhaalt niet. `Herhaal` maakt kopieën van de textuur. `Spiegeling` maakt ook kopieën, maar elke tweede kopie is gespiegeld, wat helpt om de herhaling minder op te laten vallen.

#### Patroontegels - Y {#tiling-y}
Hetzelfde als Patroontegels - X, maar voor de Y-as.

### Transformeren {#transform}
![](/images/material_transform.webp)

Extra 2d-transformaties die in de UV-ruimte op de textuur worden toegepast. De resetknop zet alles terug op de standaardwaarden. Het kettingicoon (wanneer een andere textuur dan kleur is gekozen) koppelt de transformatie aan die van de kleurtextuur, of ontkoppelt hem.

#### Verschuiving {#translation}
De verschuiving van de textuur in X en Y.

#### Rotatie {#rotation}
De rotatie van de textuur.

#### Schaal {#scale}
De schaal van de textuur. Hoe groter het getal, hoe kleiner de textuur op het object. Met de opties Patroontegels - X en Patroontegels - Y bepaal je wat er dan gebeurt.

### Uniforme schaal {#uniform-scale}
Staat dit uit, dan toont Nomad aparte regelaars voor Schaal-X en Schaal-Y.
