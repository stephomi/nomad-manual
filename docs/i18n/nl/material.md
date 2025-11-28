# ![](/icons/material.webp) Materiaal {#material}

Met dit menu kun je het materiaal van het huidige object wijzigen, de render‑eigenschappen van het object/materiaal aanpassen en texturen aan het materiaal toewijzen.

![](/images/material_overview.webp)

Materialen bepalen hoe een object eruitziet, door te regelen hoe het reageert op licht en op andere objecten. Het uiterlijk van een object wordt bepaald door deze eigenschappen:

* `Materiaaltype`
* `Kleur`
* `Ruwheid`
* `Metaalheid`
* `Ondoorzichtigheid`
* `Reflectie`
* `Emissief/unlit`

Combinaties van deze eigenschappen kunnen een grote verscheidenheid aan resultaten opleveren, van fotorealistisch tot cartoonesk tot experimenteel.

Kleur, ruwheid, metaalheid en ondoorzichtigheid kunnen worden geschilderd, zie [Vertex Paint‑opties](painting.md) voor meer informatie.

Materiaaltype, reflectie, emissief/unlit zijn materiaaleigenschappen die hieronder worden uitgelegd.

Met de kopieer/plak‑knoppen bovenaan dit menu kun je materialen van het ene object naar het andere kopiëren.

Houd er rekening mee dat de renderer van Nomad een realtime‑renderer is; hoewel krachtig, geeft hij voor bepaalde effecten de voorkeur aan snelheid boven nauwkeurigheid. 

## Materiaaltypen {#material-types}

![](/images/material_types.webp)

Nomad‑materiaaltypes zijn Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaak {#opaque}
De standaardmodus die oppervlakken behandelt als een eenvoudig materiaal dat geschilderde kleur, ruwheid, metaalheid en ondoorzichtigheid ondersteunt.

### ![](/icons/material_subsurface.webp) Ondiepe doorschijning {#subsurface}
Deze modus kan materiaal simuleren dat licht intern laat vervagen en verstrooien, zoals huid, was, jade.

Voor het beste resultaat schakel je over naar PBR‑schaduwmodus en gebruik je ten minste één directionele of spot‑light, bij voorkeur met een gedimde omgeving.

`Depth` bepaalt hoe ver licht verstrooit van de voorkant, onder het oppervlak, en dan weer uit het vooroppervlak. Dit verzacht harde schaduwen en vervaagt oppervlakdetails.

`Translucency` bepaalt hoe licht verstrooit van de voorkant naar de achterkant van een vorm, zoals licht dat door de onderkant van een blad schijnt, of wanneer oren sterk van achteren worden belicht. 

### ![](/icons/material_blending.webp) Mengen {#blending}

Vergelijkbaar met Opaque, maar ondersteunt de ondoorzichtigheids‑slider om het materiaal te laten variëren tussen solide en transparant. Dit is een eenvoudige enkele slider voor ondoorzichtigheid, in tegenstelling tot de schilderbare ondoorzichtigheid die door het opaque‑materiaal wordt ondersteund. 

::: warning
Blending‑modus kan flikkeren en popping veroorzaken bij complexe of elkaar snijdende vormen.
:::

### ![](/icons/material_additive.webp) Additief {#additive}
Je kunt je mesh half‑transparant maken met dit materiaal. Het lijkt op het blending‑materiaal, maar terwijl blending zich met de omgeving mengt, zal additive altijd helderder zijn dan de objecten erachter, goed voor heldere effecten zoals lichtstralen, vuur, explosies.

Je kunt een ondoorzichtigheidswaarde hoger dan 1 instellen, wat betekent dat het object helderder zal zijn.  
Dit kan handig zijn als je [bloom](postprocess.md#bloom) en de `threshold‑parameter` wilt gebruiken om alleen dit object te laten gloeien als een emissief object.

Deze modus heeft de neiging minder artefacten te hebben dan [Blending](#blending) (order independent transparency).

### ![](/icons/material_refraction.webp) Refractie {#refraction}
Deze modus kan worden gebruikt om glasachtig materiaal te simuleren. Vanwege realtime‑beperkingen zijn zelf‑refractie en meerlaagse refractie enigszins beperkt.

De ruwheidsschildering van het model beïnvloedt hoe wazig de refractie is.
Standaard heeft elk object dat in Nomad wordt gemaakt een ruwheid van iets rond de 25%, waardoor de refractie niet perfect maar een beetje wazig is.
Je kunt de knop `paint glossy` gebruiken om je model opnieuw te schilderen met een ruwheid en metaalheid van 0 (de kleuren worden niet beïnvloed).

Er zijn 2 verschillende ruwheden in het spel: de ene stuurt hoe wazig de reflectie is op het oppervlak, en de andere stuurt het interieur (refractie).  
Omdat er echter maar één schilderbaar ruwheidskanaal in Nomad is, delen zowel de binnen‑ als buitenruwheid dezelfde waarde.  
Om verschillende waarden te hebben (bijvoorbeeld een lolly met een scherp oppervlak maar een wazig interieur) gebruik je de sliders `Surface glossiness` en `Interior roughness` om de geschilderde ruwheid te overschrijven.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Maakt het object half‑transparant door sommige pixels willekeurig te verwijderen.

### ![](/icons/material_shadow_catcher.webp) Schaduwontvanger {#shadow-catcher}

Maakt het object onzichtbaar en laat het alleen schaduwen ontvangen. Handig om Nomad‑renders met andere afbeeldingen te combineren. 

::: tip

Meer informatie over transparantie en blending‑modi is te vinden op https://support.fab.com/s/article/Transparency-Opacity

:::

## Bediening {#controls}

![](/images/material_controls.webp)

### Altijd onverlicht {#always-unlit}
Indien ingeschakeld, negeert het object PBR en Matcap en wordt alleen de kleur‑schildering zonder shading weergegeven.
Merk op dat als je [Additive](#additive) gebruikt, je transparantie direct kunt schilderen door zwarte kleur te gebruiken.

### Opaciteit {#opacity}
Hoe solide of ondoorzichtig een object zal lijken; 100% is solide, 0% is transparant. Je kunt ook ondoorzichtigheid schilderen voor fijnere controle.

### Reflectie {#reflectance}
Bepaalt de hoeveelheid reflectie die het materiaal ontvangt voor niet‑metallische materialen. Meestal moet de standaardwaarde worden gebruikt (die overeenkomt met de standaard 4% gereflecteerd licht bij normale invalshoek), maar deze kan worden verhoogd om bijvoorbeeld reflecties en highlights in de ogen van een personage te versterken.

### Omgekeerde culling {#inverse-culling}
Keert de normalen van een oppervlak om. Meestal niet nodig, maar kan worden gebruikt als een model binnenstebuiten lijkt, of in combinatie met uitgeschakelde `Two sided` om interieurs te maken waarbij de wand het dichtst bij de camera altijd verborgen is.

### Gladde schaduw {#smooth-shading}
Zie de [globale optie](settings.md#smooth-shading).  
De waarde `Auto` gebruikt de globale optie.

### Dubbelzijdig {#two-sided}
Zie de [globale optie](settings.md#two-sided).  
De waarde `Auto` gebruikt de globale optie.

### Gekleurde achterkant {#coloured-backface}
Zie de [globale optie](settings#two-sided).
De waarde `Auto` gebruikt de globale optie.

### Werpt schaduw {#casts-shadows}
Voor nu is `Auto` hetzelfde als `On`.
Transparante objecten werpen ook schaduwen (in een dithering‑patroon om gemengde schaduwen te emuleren).  
Zorg dat je het werpen van schaduwen uitschakelt als je een groot object in je scène hebt dat geen schaduwen hoeft te werpen (bijvoorbeeld een grote vloer).

### Ontvangt schaduw {#recieve-shadows}
Voor nu is `Auto` hetzelfde als `On`.

### Draadmodel {#wireframe}
Zie de [globale optie](settings.md#wireframe).  
De waarde `Auto` gebruikt de globale optie.


## Texturen {#textures}

![](/images/material_textures.webp)

Als een object UV’s heeft, kunnen texturen op het materiaal worden toegepast naast de vertex‑kleur/ruwheid/metaalheid/ondoorzichtigheid. Meestal zijn dit het resultaat van een texture bake, maar afbeeldingen die buiten Nomad zijn gemaakt, kunnen ook worden gebruikt.

Texturen kunnen worden toegepast op

* Kleur
* Normaal
* Ruwheid
* Metaalheid
* Ondoorzichtigheid
* Emissief

Als je op een textureslot klikt, verschijnt er een selector. Nadat een texture aan een materiaalslot is toegewezen, verschijnt bij opnieuw klikken een texture‑paneel:

### Opties tekstuurpaneel {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Openen {#open}
Een andere texture selecteren

### Geen {#none}
De texture verwijderen

### Opaciteit {#texture-opacity}

Als de afbeelding een alfakanaal heeft, kun je hiermee bepalen of je dit voor Opacity gebruikt of negeert.

### ![](/icons/link.webp) Ketting/Link-icoon {#chainlink-icon}

Het link‑icoon in de volgende secties betekent, wanneer ingeschakeld, dat welke opties ook worden gebruikt, deze worden gedeeld met de andere texturen (kleur, normaal, ruwheid, metaalheid, ondoorzichtigheid, emissief) die hun link‑icoon ook ingeschakeld hebben. 

Dit zorgt ervoor dat als je uitgelijnde texturen hebt, ze uitgelijnd blijven, zelfs als je parameters of projectietypes wijzigt.


### Projectie {#projection}
![](/images/material_projection.webp)

Stel in hoe de texture op het object moet worden toegepast.

* `Auto` - Als het object uv’s heeft, UV, anders Triplanar
* `UV` - Gebruik de uv‑coördinaten van de mesh om de texture toe te passen. Als de mesh en texture van buiten Nomad komen, of vanuit Nomad worden geëxporteerd om elders te gebruiken, is UV de juiste optie.
* `Triplanar` - Projecteer de texture langs de X‑, Y‑, Z‑assen en meng de naden. 

### Triplanair {#triplanar}
![](/images/material_triplanar.webp)

Triplanar‑projecties zijn een krachtige maar eenvoudige manier om texturen op objecten toe te passen.

Triplanar is alsof je 6 videoprojectoren hebt met allemaal hetzelfde beeld, die op de voor‑, achter‑, linker‑, rechter‑, boven‑ en onderkant van je object schijnen.

Dit kan vervolgens indien nodig in UV’s of vertex‑kleuren worden gebakken.


![](/images/material_triplanar_example.webp)

#### Methode {#method}

* `Local` - De projectie beweegt mee met de object‑transform
* `World` - De projectie blijft vast, het object verplaatsen schuift het door de projectie heen.

#### Hardheid {#hardness}

Hoe de projecties mengen. 100% doet geen blending en de randen van de projecties zijn scherp. 0% mengt de randen over een brede hoek. De standaard is 90%, genoeg menging om de randen te verbergen en de rest van de projecties scherp te houden.

### Uniform {#uniform}

Indien aangevinkt wordt dezelfde hardness voor alle projecties gebruikt. Indien uitgevinkt worden extra hardness‑regelaars voor X‑, Y‑, Z‑projecties zichtbaar.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filtering {#filtering}
De texture‑filtermethode die moet worden gebruikt, `Auto` is de standaard, methoden zijn `Nearest`, `Linear`, `Mipmap`. Nearest doet geen filtering, waardoor texturen gekartelde artefacten kunnen krijgen wanneer ze van dichtbij worden bekeken. Linear en Mipmap doen betere filtering, zodat texturen van dichtbij eerder wazig dan gekarteld lijken.

#### Herhaling-X {#tiling-x}
Als de Scale‑parameter groter is dan 1, waardoor de texture kleiner wordt dan de object‑UV’s, hoe wordt de texture dan langs de X‑as getiled. `None` betekent geen herhalingen. `Repeat` maakt kopieën van de texture. `Mirror` maakt kopieën van de texture, waarbij elke tweede kopie gespiegeld is, wat kan helpen om tiling‑artefacten te verbergen.

#### Herhaling-Y {#tiling-y}
Hetzelfde als Tiling‑X, maar voor de Y‑as.

### Transformatie {#transform}
![](/images/material_transform.webp)

Extra 2D‑transformaties die op de texture in UV‑ruimte worden toegepast. De reset‑knop zet alles terug naar de standaardwaarden, het ketting‑icoon (wanneer andere texturen dan kleur zijn geselecteerd) koppelt of ontkoppelt de transform zodat deze gelijk is aan de kleur‑texture.

#### Translatie {#translation}
De X‑ en Y‑verschuiving van de texture

#### Rotatie {#rotation}
De rotatie van de texture

#### Schaal {#scale}
De schaal van de texture; grotere getallen maken de texture kleiner op het object, gebruik de sliders Tiling‑X en Tiling‑Y om te bepalen wat er gebeurt.

### Uniforme schaal {#uniform-scale}
Wanneer uitgeschakeld toont Nomad aparte regelaars voor Scale‑X en Scale‑Y.