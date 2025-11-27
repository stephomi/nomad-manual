# ![](/icons/toolbox.webp) Gereedschap

![](/images/tools_menu.webp)

::: tip
Spring naar beneden naar [Gereedschap](#tools-1) voor beschrijvingen van de individuele tools.
:::

## Overzicht

Gereedschap wordt geselecteerd uit de `Toolbox` rechts, en bediend met de `Tool Controls` links. Extra instellingen zijn te vinden in het `Settings`-menu, het eerste icoon in het menu rechtsboven.

Brush‑tools hebben instellingen voor grootte en intensiteit. Selectietools hebben instellingen voor verschillende selectiestijlen. Onderaan de tool‑instellingen staan snelkoppelingen voor veelgebruikte bewerkingen (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Nomads tools zijn kleurgecodeerd in de toolbox:

* <span class=brush>**Brush tools**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Move tools**</span> (Move, Drag)
* <span class=mask>**Mask tools**</span> (Mask, SelMask)
* <span class=paint>**Paint tools**</span> (Paint, Smudge)
* <span class=flatten>**Flatten tools**</span> (Flatten, Planar)
* <span class=pinch>**Pinch tools**</span> (Crease, Pinch)
* <span class=selection>**Selection based tools**</span> waarbij eerst een 2D‑masker wordt getekend en daarna een bewerking plaatsvindt (Trim, Split, Project)
* <span class=creation>**Creation tools**</span> (Tube, Lathe, Insert)
* <span class=transform>**Transform tools**</span> (Transform, Gizmo)
* <span class=misc>**Misc tools**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**View tool**</span>



Veel van deze tools kunnen worden aangepast met verschillend brush‑gedrag, druk, texturen enz. via het [Stroke](stroke.md)-menu. 


### Brush‑instellingen

De linker toolbar heeft schuifregelaars voor radius en intensiteit, en daarna toolspecifieke instellingen per categorie, hieronder uitgelegd.

![](/images/tool_left_panel.webp)

::: tip
De intensiteitsschuif voor veel tools kan boven 100% gaan, het is de moeite waard om hiermee te experimenteren!
:::

### Sub‑modus
De knop direct onder de intensiteitsschuif is de `Sub`‑knop. Het label en de functie veranderen per tool, en wanneer hij is ingedrukt wordt een alternatieve, meestal tegenovergestelde werking geactiveerd. Voor [Paint](#paint) wordt bijvoorbeeld een Erase‑modus geactiveerd, voor [Crease](#crease) worden opstaande randen gemaakt in plaats van groeven, enz.

Standaard werkt hij als een “sticky” knop; je kunt hem ingedrukt houden om hem tijdelijk te activeren, en zodra je loslaat wordt hij weer uitgeschakeld. Als je tikt, wordt de sub‑modus permanent geactiveerd.

### Snelkoppelingen
Onderaan de linker toolbar staan snelkoppelingen voor [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Standaard werken deze allemaal als “sticky” knoppen; je kunt ze ingedrukt houden om ze tijdelijk te activeren, en zodra je loslaat worden ze weer uitgeschakeld. Als je tikt, wordt die snelkoppelingsmodus permanent geactiveerd.

### Selectie‑instellingen

De tools [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) en [Hide](#hide) gebruiken vergelijkbare bediening om gebieden van de mesh te selecteren.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Een vrij getekende vorm
* `Polygon` - Een gesloten vorm gedefinieerd door een combinatie van krommen en/of rechte lijnen. Zie [Shape editing](#shape-editing) hieronder voor meer info.
* `Curve` - (alleen Project) - Een vrij getekende curve voor de projectie
* `Path` - (alleen Project) - Een curve gedefinieerd door punten. Zie [Shape editing](#shape-editing) hieronder voor meer info.
* `Line` - Sleep een lijn om een vlak segment te definiëren. Standaard wordt direct op de mesh gewerkt; schakel auto validate uit als je dit niet wilt (lang drukken of vegen op het lijn‑icoon)
* `Rect` - Sleep een diagonale lijn, dit definieert de hoeken van een rechthoek. Lang drukken of vegen om opties te tonen voor auto validate, forceren naar een vierkant, en om de eerste klik als middelpunt van de rechthoek te gebruiken.
* `Ellipse` - Sleep een diagonale lijn, dit definieert de grootte van een ellips. Lang drukken of vegen om opties te tonen voor auto validate, forceren naar een cirkel, en om de eerste klik als middelpunt van de ellips te gebruiken.
* `Flip` - Inverteer het vormmasker, of de richting van de project‑tool.

De meeste tools hebben een optie voor auto validate, wat betekent dat de bewerking wordt uitgevoerd zodra je klaar bent met het tekenen van de vorm. Wanneer auto validate uit staat, wordt er een groene knop naast de vorm getekend die de bewerking uitvoert. Dit stelt je in staat de vorm te bewerken, het zicht aan te passen, en wanneer je klaar bent druk je op de groene knop om de vorm te gebruiken.

### Shape editing
Polygon‑bewerking en curve‑bewerking gedragen zich op vergelijkbare wijze:

* Begin met het slepen van een lijn om 2 punten te definiëren, sleep dan vanuit het midden van de lijn om een polygoon of curve te definiëren.
* Klik op de punten om te wisselen tussen smooth en sharp. 
* Klik en sleep op de curve‑ of lijnsegmenten om nieuwe punten te maken.
* Om een punt te verwijderen, sleep je een punt naar zijn buur totdat hij rood wordt.
* Het prullenbak‑icoon in de hoek van het polygon‑ of path‑icoon verwijdert de vorm.

### Settings‑menu

Veel tools hebben extra instellingen die te vinden zijn in het settings‑menu, het eerste icoon in het menu rechtsboven:

![](/images/tools_settings_menu.webp)

## Tools

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
De Clay‑tool is handig om je sculptuur op te bouwen. `Sub` verwijdert materiaal van je sculptuur.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
De standaard brush. `Sub` verwijdert materiaal.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
Het gebied onder de brush blijft aan de brush “plakken”, wat elastische vervorming mogelijk maakt. De selectie wordt behouden tijdens het verplaatsen, dus als je de brush weghaalt en weer terugbrengt naar het beginpunt, zie je geen vervorming.

De sub‑modus is `Normal`, en verplaatst het gebied onder de brush langs de oppervlaknormaal.

Deze brush is geschikt voor zowel grootschalige vervorming als nauwkeurige kleine vervormingen.

#### Move‑instellingen

* `Radius (Background)` - Hoe ver je van de rand van een model kunt zijn en nog steeds kunt sculpten, handig bij het werken aan de silhouet van een object. 
* `Same-side vertex only` - Negeer vertices die in de tegenovergestelde richting van de vervorming wijzen.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
Het gebied onder de brush blijft aan de brush “plakken”, wat elastische vervorming mogelijk maakt. In tegenstelling tot de Move‑brush wordt de selectie continu bijgewerkt tijdens de stroke, zodat het mogelijk is langere, slangachtige vormen te maken, vooral wanneer Dynamic Topology is geactiveerd.

De sub‑modus is `Normal`, en verplaatst het gebied onder de brush langs de oppervlaknormaal.

Deze brush is goed voor lossere, meer gebarige vormveranderingen.

#### Drag‑instellingen

* `Radius (Background)` - Hoe ver je van de rand van een model kunt zijn en nog steeds kunt sculpten, handig bij het werken aan de silhouet van een object. 
* `Same-side vertex only` - Negeer vertices die in de tegenovergestelde richting van de vervorming wijzen.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
Maak het gebied glad door de puntposities te middelen. Deze tool is sterk afhankelijk van de polygoondichtheid.
Als je veel polygonen hebt, is het gladmaken minder effectief.

De sub‑modus is `Relax`, die alleen het wireframe gladmaakt maar probeert de geometrische details te behouden.

#### Smooth‑instellingen

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - Maakt de randen van facegroups glad. Gebruik een intensiteit groter dan 100% om randen snel glad te maken. `Auto` maakt alleen glad als facegroup‑preview is ingeschakeld, `Off` schakelt uit, `On` schakelt in. 

##### Vertex
* `Sticky vertex on border` - Voor meshes met open randen, bv. een vlak, is het mogelijk de hoeken uit te vlakken. Door deze optie in te schakelen worden de open randen vergrendeld.
* `Relax` - hetzelfde als de relax‑alternatieve modus in de toolbar links.
* `Stable smoothing` - Probeert het gladmaken topologie‑onafhankelijk te maken. Dit werkt het best bij variërende topologiedichtheid en met een hoge smoothing‑intensiteit.

##### Painting
* `Screen Smoothing` - Gebruik deze optie om topologie‑onafhankelijk gladmaken te krijgen, zelfs bij hoge polycounts.
* `Screen samples` - De kwaliteit van het gladmaken; hogere waarden zijn gladder maar trager.

::: tip
Hogere polygoondichtheden kunnen vereisen dat je de intensiteit boven 100% verhoogt. Zeer hoge waarden (300%, 500%) kunnen ook goed werken als sculpting‑tool, waarbij gebieden snel vlak en glad worden onder de brush, alsof je klei met een hamer slaat!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
Met deze tool kun je vertices maskeren. Gemaskerde vertices zijn beschermd tegen sculpten of schilderen. 

De sub‑modus is `Unmask`, en wist waar het masker is geschilderd.

Net als selecties in 2D‑tekenprogramma’s kunnen maskers met een brush worden geschilderd, of met vormselecties worden gemaakt, vervaagd of verscherpt. 

In tegenstelling tot 2D‑programma’s kunnen ze ook via facegroups worden gemaakt, en maskers kunnen worden gebruikt om nieuwe geometrie te maken via extrusie/extractie‑achtige bewerkingen. 

![](/videos/tool_mask1.mp4)

 Er verschijnt een toolbar bovenaan de viewport met extra bediening. 

![](/images/tool_mask_toolbar.webp)

De titel van de balk kan worden aangetikt om in/uit te klappen, of de pijl rechtsboven kan worden aangetikt om hem naar de boven- of onderkant van de UI te verplaatsen.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | Clear the mask                                                                             |
| ![](/icons/invert.webp)        Invert             | Invert the mask                                                                            |
| ![](/icons/sharpen.webp)       Sharpen            | Sharpen the mask edge                                                                      |
| ![](/icons/blur.webp)          Blur               | Blur the mask edge                                                                         |
|                                 Blur ->            | Drag left/right to interactively blur the mask                                             |
| ![](/icons/culling.webp)       Front              | Toggle to only mask front facing vertices                                                  |
|                                 Convert            | Convert the mask to a facegroup                                                            |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | When enabled facegroups will be shown, tapping a facegroup will mask it                    |
|                                 On tap (mask)      | When enabled tapping an 'island' of mask or unmasked polygons will flood fill that island. |
| ![](/icons/vertex.webp)        Connected          | When enabled only allow mask strokes to affect connected topology.                         |

##### Mask Quick gesture
Je kunt ZBrush‑achtige gebaren uitvoeren terwijl je de quick‑maskingknop in de linker toolbar ingedrukt houdt:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Tap on the background              |
| Clear   | Drag on the background             |
| Blur    | Tap on masked area                 |
| Sharpen | Tap on unmasked area               |


#### Mask‑instellingen
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Het Mask‑instellingenmenu wordt vooral gebruikt om geometrie uit het masker te maken. Daarom is het standaardgedrag om een preview te tonen van hoe de nieuwe geometrie eruit zal zien. Je kunt kiezen voor geen preview, een extract‑preview, een split‑preview, en of deze geometrie in x‑ray‑modus wordt getoond.

##### Thickness
* `Height` - De hoogte van de geëxtraheerde vorm. Met het Plus/Minus‑icoon kun je wisselen tussen een naar buiten gerichte extrusie, naar binnen, of gecentreerd. 
* `Height/Height+Mask` - Schakel tussen een constante hoogte, of dat vervaagde delen van het masker de hoogte beïnvloeden, zodat zachte en variërende hoogtes mogelijk zijn. 

##### Smoothness
Wanneer actief, worden de randen van de geëxtraheerde vorm gladgemaakt; dit werkt beter bij hogere polygoonaantallen. 
* `Iterations` - De hoeveelheid smoothing die wordt toegepast. Hoge waarden produceren zeer gladde gebogen randen, maar zullen beginnen af te wijken van de maskervorm.
* `All/Sharp border/Borders only` - Smoothing kan in alle richtingen werken (zijkanten en bovenkant), of de bovenkant en zijkanten gladmaken maar een scherpe rand behouden, of alleen de rand gladmaken en het bovenvlak ongemoeid laten.

##### Edge loop (side)
* `Auto Edge-loop (side)` - Berekent het aantal verdelingen aan de zijkanten van de geëxtraheerde vorm om vierkante polygonen te maken die overeenkomen met de polygonen van het gemaskerde gebied. Wanneer uitgeschakeld kun je zelf het aantal edge‑loops instellen met de edge‑loop‑schuif.

----

##### Extract
* `Extract` - Maak de geëxtraheerde geometrie.
* `Closing action` - Hoe Extract zich moet gedragen. 'None' dupliceert de gemaskerde polygons in een nieuwe vorm. 'Fill' doet hetzelfde en probeert het achtervlak te dichten. 'Shell' extrudeert met de hoeveelheid ingesteld bij 'thickness', en is de standaard.

::: tip

Als de preview in 'Extract'‑modus staat met 'X-ray' ingeschakeld, kan het klikken op de Extract‑knop in het begin verwarrend zijn. Omdat het menu actief is, probeert het een preview van een extractie op je nieuwe vorm te maken en het oorspronkelijke oppervlak in x‑ray te tonen. Maar omdat je geen masker op het nieuwe oppervlak hebt, kan het de extractie niet previewen en zal Nomad waarschuwen met 'Nothing to Extract!'. 

Dit is normaal; sluit het Mask‑instellingenmenu om de nieuwe vorm en het origineel te bekijken, en selecteer het oorspronkelijke oppervlak opnieuw als je het masker moet wissen of nieuwe maskers wilt tekenen.
:::

##### Split
* `Split` - Extraheert zowel de gemaskerde ALS de ongemaskerde gebieden in nieuwe vormen. 
* `Closing action (masked)` - Hoe de extractie van het masker zich moet gedragen. 'None' dupliceert de gemaskerde polygons in een nieuwe vorm. 'Fill' doet hetzelfde en probeert het achtervlak te dichten. 'Shell' extrudeert met de hoeveelheid ingesteld bij 'thickness', en is de standaard.
* `Closing action (unmasked)` - Hoe de extractie van het ongemaskerde deel zich moet gedragen. 'None' dupliceert de gemaskerde polygons in een nieuwe vorm. 'Fill' doet hetzelfde en probeert het achtervlak te dichten. 'Shell' extrudeert met de hoeveelheid ingesteld bij 'thickness', en is de standaard.
* `Sync border` - Zorgt dat de rand tussen de gemaskerde en ongemaskerde geëxtraheerde vormen dicht bij elkaar blijft. Wanneer uitgeschakeld kan er een opening ontstaan tussen de vormen, omdat de shell‑bewerking elk vlak langs zijn normaal extrudeert.

##### Carve
* `Carve` - Gedraagt zich in de standaardmodus alsof je in het oppervlak hebt getrimd met de hoeveelheid 'thickness', zoals het uitsnijden van een stuk sinaasappelschil. 



### ![](/icons/tool_maskSelector.webp) Selection Mask
Deze tool lijkt grotendeels op de [Masking‑tool](#mask); het belangrijkste verschil is dat je geen stroke gebruikt om een masker te schilderen, maar de [Selection Controls](#selection-controls).

De sub‑modus is `Unmask`, en wist het masker met behulp van de selectie‑bediening.

Selection Mask deelt dezelfde toolinstellingen als de `Mask`‑tool.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
Breng kleur en materiaaleigenschappen aan. Voor meer informatie over materiaal kun je de sectie [Painting](painting.md) bekijken.

De sub‑modus is `Erase` en verwijdert verf.

#### Paint‑instellingen
* `Layer fitering` - Dit werkt als de layer alpha lock in Photoshop of Procreate. Als je op een layer schildert, kun je met deze optie alleen gebieden wijzigen waar al verf aanwezig is; onbeschilderde gebieden worden beschermd.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
Vervaag kleur en materiaaleigenschappen. Het Smudge‑instellingenmenu bevat een `Quality`‑schuif; lagere waarden betekenen snellere strokes.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
Maak het gebied vlak door de punten op het gemiddelde vlak te projecteren.

De sub‑modus is `Fill` en definieert een vlak dat wordt bepaald door het hoogste punt, en trekt punten eerder omhoog.

#### Flatten‑instellingen

* `Lock plane direction` - Gebruik de vlakrichting die bij de eerste klik is berekend. Standaard is dit uitgeschakeld.
* `Lock plane origin`- Gebruik de eerste klik als middelpunt van het vlak. Standaard is dit uitgeschakeld.

Wanneer een of beide zijn uitgeschakeld, kan Flatten geleidelijk worden verdiept of kan de vlakhoek worden gewijzigd door lange strokes te gebruiken die over verschillende dieptes en krommingen bewegen. Dit, in combinatie met de gebieds‑sample‑opties van het Brush‑menu, kan zeer precieze controle bieden.

::: tip
Wanneer je werkt in gebieden met hoge kromming, bijvoorbeeld bij het vlakmaken van de wangen maar de tool blijft de zijkanten van de neus beïnvloeden, probeer dan een masker te maken om gebieden te beschermen die de Flatten‑brush niet mag raken.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
Maak punten vlak door ze op het gemiddelde vlak te projecteren, maar met minder opbouw dan de Flatten‑brush. Dit creëert schonere hard‑edge oppervlakken. Snelle strokes duwen en trekken meer aan het oppervlak, langzamere strokes die vanuit al vlakke gebieden naar buiten werken behouden het vlak beter.

De sub‑modus is `Fill` en definieert een vlak dat wordt bepaald door het hoogste punt, en trekt punten eerder omhoog.

Planar is in feite dezelfde tool als `Flatten`, maar met `Lock plane direction` ingeschakeld, wat betekent dat hij eerder stabiele, harde oppervlakken maakt, terwijl Flatten meer sculpturaal kan zijn en gebruikt kan worden om semi‑vlakke gebieden te creëren.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Crease‑tools zijn handig om kleine sneden of deuken te sculpten.

De sub‑modus is `Invert`, en maakt een opstaande groef.

#### Crease‑instellingen

* `Pinch factor` - Hoeveel vertices zijwaarts naar de stroke worden getrokken. Als pinch op 1 staat en offset op 0, verandert het oppervlak niet in diepte, alleen in topologie, waarbij randen naar de stroke worden getrokken.
* `Offset factor` - Hoeveel vertices in de diepte worden geduwd/getrokken. Als pinch op 0 staat en offset op 1, worden diepe groeven of opstaande deuken gemaakt, maar die zien er hoekig uit omdat er niet genoeg geo naar de groef wordt getrokken om de zijkanten of bodem nauwkeurig te definiëren.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
Deze tool kan worden gebruikt om randen te verscherpen.

De sub‑modus is `Invert` en duwt vertices uit elkaar.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
De Trim‑tool werkt door een stuk van je mesh te verwijderen, en geeft opties voor hoe het overgebleven gat moet worden verwerkt. Hij gebruikt de [Selection controls](#selection-controls) om de trim te definiëren.

::: tip
Omdat deze tool vanuit de camera projecteert, krijg je een waarschuwing als de camera in perspectiefmodus staat.

In orthografische modus is de snede door de mesh parallel aan de view, wat meestal is wat men verwacht. In perspectiefmodus ziet de snede er anders uit aan de verre kant van het object dan aan de nabije kant.
:::

#### Trim‑instellingen

* `Stroke painting` - Als paint is ingeschakeld in het Paint‑menu, wordt het gepatchte gebied gevuld met de momenteel geselecteerde kleur.
* `Boolean` - Vul het gat van de trim met een quad‑polygebied. Het gevulde gebied is vlak.
* `Legacy` - Vul het gat van de trim met een getrianguleerd gebied. Het gevulde gebied is vlak.
* `Fill` - Vul het gat met een getrianguleerd gebied. Het gevulde gebied is een gebogen oppervlak, zoals het vlies van een zeepbel.
* `None` - Vul het gat niet.
* `Boolean Detail Shape` - De geschatte grootte van de quads en triangles aan de vormzijde van de trim.
* `Boolean Detail Hole` - De geschatte grootte van de triangles of polys in het gevulde gat van de trim. 
* `Legacy Detail` - De geschatte grootte van de triangles in de trim.
* `Legacy Hole smoothing` - Hoeveel de triangles in het gevulde gebied worden ontspannen.
* `Legacy Threshold espilon` - Een waarde die kan worden aangepast om het legacy‑gatvulalgoritme te verbeteren.
* `Fill Detail` - De geschatte grootte van de triangles in de trim.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
Vergelijkbaar met de [Trim](#trim)‑tool, behalve dat Trim de selectie weggooit, terwijl Split de selectie bewaart als een nieuw object.

#### Split‑instellingen

* `Stroke painting` - Als paint is ingeschakeld in het Paint‑menu, wordt het gepatchte gebied gevuld met de momenteel geselecteerde kleur.
* `Boolean` - Vul het gat van de split met een quad‑polygebied. De gevulde gebieden zijn vlak.
* `Legacy` - Vul het gat van de split met een getrianguleerd gebied. De gevulde gebieden zijn vlak.
* `Fill` - Vul de gaten met een getrianguleerd gebied. De gevulde gebieden zijn gebogen oppervlakken, zoals het vlies van een zeepbel.
* `None` - Vul de gaten niet.
* `Boolean Detail Shape` - De geschatte grootte van de quads en triangles aan de vormzijde van de split.
* `Boolean Detail Hole` - De geschatte grootte van de triangles of polys in het gevulde gat van de split. 
* `Legacy Detail` - De geschatte grootte van de triangles in de split.
* `Legacy Hole smoothing` - Hoeveel de triangles in het gevulde gebied worden ontspannen.
* `Legacy Threshold espilon` - Een waarde die kan worden aangepast om het legacy‑gatvulalgoritme te verbeteren.
* `Fill Detail` - De geschatte grootte van de triangles in de split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
De Project‑tool lijkt op de [Trim](#trim)‑tool, maar verwijdert of maakt geen geometrie; hij verplaatst alleen vertices zodat ze overeenkomen met de selectie.

![](/videos/tool_project.mp4)

::: tip
Als je Project gebruikt terwijl je in een layer werkt, kun je met de layer‑slider tussen de oorspronkelijke en de geprojecteerde vorm blenden.
:::

### ![](/icons/tool_layer.webp) Layer
Verhoog het oppervlak, maar beperk de hoogte.

Als je de pen omlaag houdt en over een gebied blijft brushen, zal Layer tot een bepaalde hoogte verhogen en niet verder gaan, in tegenstelling tot andere tools die hoogte blijven opstapelen.

Merk op dat de limiet standaard alleen per stroke wordt ingesteld! Als je een nieuwe stroke begint, wordt er verder opgebouwd vanaf de nieuwe oppervlaktehoogte.

Om een constante maximale hoogte over meerdere strokes te zetten, gebruik je de Layer‑tool met Nomads [Layers](layers.md)-systeem.

Maak een layer en gebruik deze tool. De maximale hoogte wordt nu ingesteld vanuit de layer, zodat je veel brush‑strokes kunt toepassen en de hoogte altijd hetzelfde blijft.

`Sub` gebruikt een minimale diepte en maakt groeven.

#### Layer‑instellingen

* `Use layer data` - Wanneer actief, en wanneer een layer is geselecteerd, gebruik de layer‑data om de maximale hoogte in te stellen.
* `Inflate`- Wanneer actief wordt de richting waarin Layer werkt aangepast om gladdere resultaten te krijgen.
* `Relax (Normal)` - De hoeveelheid smoothing die op de normals wordt toegepast.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
Verplaats de vertices langs hun eigen normals. `Sub` verplaatst vertices langs hun omgekeerde normaal.

#### Inflate‑instellingen
* `Relax (Normal)` - De hoeveelheid smoothing die op de normals wordt toegepast.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
Verplaats of “smeer” punten in de richting van de stroke.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

Klik en sleep om een gebied van de sculpt omhoog te halen in de vorm van de geselecteerde Alpha.

Dit is simpelweg de [Brush‑tool](#brush) met een stroke‑type ingesteld op `Lock + radius`. 

`Sub` duwt de stempel naar binnen in plaats van hem uit het oppervlak te trekken.

::: tip
Stamp werkt meestal het best met hoge resolutie‑geometrie. Als je online zoekt naar 'wrinkles alpha', 'pores alpha', 'scales alpha' enz., kunnen deze alpha‑texturen samen met Stamp een geweldige manier zijn om organische details aan een charactersculpt toe te voegen.

De twee stroke‑modi zijn nuttig voor verschillende dingen. 

* `Lock + radius` heeft een vaste *hoogte*; slepen past de breedte en rotatie van de stempel aan. Goed voor huidtexturen die dezelfde diepte/hoogte moeten hebben, maar verschillende rotaties en schalen om herhalingspatronen te verbergen.
* `Lock + intensity` heeft een vaste *breedte*; slepen past de rotatie en hoogte van de stempel aan. Goed voor klinknagels, die allemaal dezelfde grootte moeten hebben, maar verschillende rotaties en hoogtes. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
Deze tool kan layers lokaal resetten; je hebt een actieve layer nodig, anders gebeurt er niets.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
Maak een tube door een curve te tekenen. 
![](/images/tool_tube_new.webp)

Zodra de tube is gemaakt, kan het pad in 3D‑ruimte worden bewerkt met vergelijkbare bediening als de standaard [Shape editing](#shape-editing) en curve‑editing‑tools. 

![](/videos/tool_tube.mp4)

#### Tube‑linker toolbar

![](/images/tool_tube_left_toolbar.webp)

De linker toolbar heeft de volgende opties:

* `Sync` - Als de huidige tube een instance is en er child‑nodes van de tube zijn die verschillen tussen de instances, worden deze hiermee opnieuw gesynchroniseerd.
* `Snap` - Wanneer actief, zullen de Curve‑ en Path‑modi op andere objecten snappen terwijl je tekent. Wanneer inactief, snapt alleen het eerste punt, daarna wordt de rest van de tube op die diepte getekend. Er is een klein fly‑out‑menu:
    * `Offset` - Stel de diepte van de snap in; 0% laat het midden van de tube‑doorsnede op het oppervlak snappen, positieve waarden tillen hem van het oppervlak, negatieve waarden duwen hem erin.
* `Curve` - Schets vrij een tube. Er is een klein fly‑out‑menu:
    * `Auto-validate` - Maakt de tube zodra de stroke is voltooid. Wanneer uitgeschakeld, is er een groene validate‑cirkel zichtbaar naast het curve‑pad; druk hierop om te valideren, of gebruik de `Reset`‑link die in dit menu verschijnt om het pad te verwijderen.
    * `Closed` - Maak van de tube een lus.
    * `Screen` - Alleen beschikbaar wanneer Auto‑validate is uitgeschakeld. Wanneer actief, wordt het pad aan het scherm “vastgepind”, zodat je de view en het object kunt verplaatsen terwijl het pad op zijn plaats blijft. Wanneer inactief, maakt het pad deel uit van de 3D‑scene en beweegt het mee met camera en objecten.
    * `Accuracy` - Hoeveel curvepunten worden gebruikt om het getekende pad in een tube om te zetten. 0% gebruikt het laagste aantal punten maar mist kleine krommingsveranderingen; 100% is zeer nauwkeurig en gebruikt veel punten.
* `Path` - Maak een tube door te klikken om curvepunten te definiëren. Tik op de groene cirkel om het pad te valideren. Er is een klein fly‑out‑menu:
    * `B-spline` - Een alternatieve curvetekenmethode waarbij curvepunten meestal niet direct op de curve liggen, maar gladdere resultaten kan geven dan de standaardmethode.
    * `Closed` - Maak van de tube een lus
    * `Screen` - Wanneer actief, wordt het pad aan het scherm “vastgepind”, zodat je de view en het object kunt verplaatsen terwijl het pad op zijn plaats blijft. Wanneer inactief, maakt het pad deel uit van de 3D‑scene en beweegt het mee met camera en objecten.

##### Tube‑toptoolbar
![](/images/tool_tube_toolbar.webp)
Wanneer een tube is geselecteerd, verschijnt er een toolbar bovenaan de viewport met extra bediening. Klik op de titel van de toolbar om hem in/uit te klappen, en klik op de pijl rechtsboven om de toolbar naar de boven- of onderkant van de viewport te verplaatsen.

* `Validate` - Bak de tube om in gewone polygonen zodat hij gesculpt kan worden.
* `Edit` - Toon de curvepunten zodat ze kunnen worden gemanipuleerd
* `Mirror` - Voeg een mirror‑repeater toe als parent van deze curve
* `Snap` - Laat curvepunten naar nabije oppervlakken snappen
* `Closed` - Verbind het begin en einde van de curve tot een lus
* `B-spline` - Schakel tussen Catmull‑Rom en B‑spline‑interpolatie.
* `Cap` - Wissel tussen caps aan beide uiteinden van de tube, alleen aan het begin of einde, of geen caps.
* `Hole` - Voeg dikte toe aan de tube en maak er een pijp van. Wissel tussen een gat aan beide uiteinden, alleen aan het einde, of geen gaten. 
* `Radius` - Wissel tussen een uniforme radius, een radius aan begin en einde, of een radius per curvepunt. Deze worden bewerkt met oranje handles op de curve.
* `Twist` - Wissel tussen geen twist, een uniforme twist, een twist aan begin en einde, of een twist per curvepunt. Deze worden bewerkt met roze handles op de curve.
* `Profile` - Wissel tussen geen profiel (dus een cirkelprofiel), een uniform profiel, een profiel aan begin en einde, of een profiel per punt.
* `Profile edit` - Toon een profile‑editor. Deze werkt vergelijkbaar met de [Shape editing](#shape-editing)‑tools, kan profielpresets opslaan en laden, en heeft een toggle om het profiel in 3D‑ruimte te bewerken.
* `Spiral` - Toon een menu om een spiraalvormige twist aan de tube toe te voegen. Dit menu heeft opties voor `Twist Angle`, `Offset`, `Scale` en `Angle offset`.
* `X Divisions` - Het aantal verdelingen rond de tube; 4 verdelingen maken bijvoorbeeld een vierkante tube. 
* `Constant density` - Wanneer actief, blijven de polygonen vierkant. Wanneer uitgeschakeld, kun je `Y divisions` langs de lengte van de tube instellen.
* `...` - Tube‑instellingenmenu.

#### Curve point delete‑toggle

![](/images/tool_tube_delete_toggle.webp)

Onder de toolbar staat een curve point delete‑toggle. Wanneer je een curvepunt dicht bij een ander sleept, wordt het rood, wat aangeeft dat het punt wordt verwijderd als je loslaat. Als je kleine bewerkingen doet en geen punten wilt verwijderen, schakelt deze knop het verwijdergedrag uit.



#### Tube‑instellingen
* `Primitive` - Knoppen om UV’s in/uit te schakelen, of om de tube te valideren.
* `Post subdivision` - Een snelkoppeling om het multiresolution‑niveau in te stellen vóór het valideren.
* `Linear subdivision` - Snelkoppeling om het lineaire subdivisie‑niveau in te stellen vóór het valideren. 
* `Division X` - Zelfde als X Divisions in de toolbar.
* `Division Y` - Zelfde als Y Divisions in de toolbar.
* `Curve (Repeater)` - Converteer de tube naar een [Curve Repeater](scene.md#curve)

::: tip
Divisions op 4 en Post subdivision op 3 maken gladde, rond‑afgeronde tubes, goed voor wormen, slangen, lichaamsdelen.
:::


### ![](/icons/tool_lathe.webp) Lathe
Maak een rotatieoppervlak door een curve te tekenen.

Deze tool is ideaal voor vormen zoals vazen en wijnglazen.

![](/videos/tool_lathe.mp4)

#### Lathe‑linker toolbar

![](/images/tool_lathe_left_toolbar.webp)

De linker toolbar heeft de volgende opties:

* `Sync` - Als de huidige lathe een instance is en er child‑nodes van de lathe zijn die verschillen tussen de instances, worden deze hiermee opnieuw gesynchroniseerd.
* `Fixed` - Wanneer ingeschakeld is het middelpunt van de lathe vast en zichtbaar op het scherm. Deze middellijn heeft edit‑punten die kunnen worden aangepast. Wanneer uitgeschakeld, wordt het middelpunt van de lathe dynamisch bijgewerkt zodat het overeenkomt met het begin en einde van de getekende curve.
* `Curve` - Teken het lathe‑profiel in één stroke. Er is een klein fly‑out‑menu:
    * `Auto-validate` - Wanneer ingeschakeld wordt de lathe gemaakt zodra de pen van het scherm wordt gehaald. Wanneer uitgeschakeld, kan op een groene cirkel naast de curve worden gedrukt om de lathe te maken. De curve kan met de `Reset`‑knop worden verwijderd.
    * `Closed` - Verbind het begin en einde van de curve tot een lus
    * `Screen` - Alleen beschikbaar wanneer Auto‑validate is uitgeschakeld. Wanneer actief, wordt het pad aan het scherm “vastgepind”, zodat je de view en het object kunt verplaatsen terwijl het pad op zijn plaats blijft. Wanneer inactief, maakt het pad deel uit van de 3D‑scene en beweegt het mee met camera en objecten.
    * `Accuracy` - Hoeveel curvepunten worden gebruikt om het getekende pad in een tube om te zetten. 0% gebruikt het laagste aantal punten maar mist kleine krommingsveranderingen; 100% is zeer nauwkeurig en gebruikt veel punten.
* `Path` - Maak een lathe door te klikken om curvepunten te definiëren. Tik op de groene cirkel om het pad te valideren. Er is een klein fly‑out‑menu:
    * `B-spline` - Een alternatieve curvetekenmethode waarbij curvepunten meestal niet direct op de curve liggen, maar gladdere resultaten kan geven dan de standaardmethode.
    * `Closed` - Maak van de tube een lus
    * `Screen` - Wanneer actief, wordt het pad aan het scherm “vastgepind”, zodat je de view en het object kunt verplaatsen terwijl het pad op zijn plaats blijft. Wanneer inactief, maakt het pad deel uit van de 3D‑scene en beweegt het mee met camera en objecten.

#### Lathe‑toptoolbar
![](/images/tool_lathe_top_toolbar.webp)

Wanneer een lathe is geselecteerd, verschijnt er een toolbar bovenaan de viewport met extra bediening. Klik op de titel van de toolbar om hem in/uit te klappen, en klik op de pijl rechtsboven om de toolbar naar de boven- of onderkant van de viewport te verplaatsen.

* `Validate` - Bak de lathe om in gewone polygonen zodat hij gesculpt kan worden.
* `Edit` - Toon de curvepunten zodat ze kunnen worden gemanipuleerd
* `Mirror` - Voeg een mirror‑repeater toe als parent van deze lathe
* `Snap` - Laat curvepunten naar nabije oppervlakken snappen
* `Stable` - Wanneer ingeschakeld wordt het curveprofiel geparent aan de middellijn van de lathe. Wanneer uitgeschakeld kan de middellijn worden bewerkt zonder de curve te verplaatsen, wat complexere vormen mogelijk maakt.
* `Focus` - Draait de view zodat je het curveprofiel perfect vlak in beeld ziet.
* `Closed` - Verbind het begin en einde van de curve tot een lus
* `Cap` - Als Closed is uitgeschakeld, wissel tussen caps aan beide uiteinden van de tube, alleen aan het begin of einde, of geen caps.
* `Hole` - Voeg dikte toe aan de lathe en maak er een pijp van. Wissel tussen een gat aan beide uiteinden, alleen aan het einde, of geen gaten. 
* `B-spline` - Schakel tussen Catmull‑Rom en B‑spline‑interpolatie.
* `X Divisions` - Het aantal verdelingen rond de lathe; 4 verdelingen maken bijvoorbeeld een lathe met vierkant profiel. 
* `Constant density` - Wanneer actief, blijven de polygonen vierkant. Wanneer uitgeschakeld, kun je `Y divisions` langs de lengte van de tube instellen.
* `...` - Lathe‑instellingenmenu.

#### Lathe‑instellingen
* `Primitive` - Knoppen om UV’s in/uit te schakelen, of om de tube te valideren.
* `Post subdivision` - Een snelkoppeling om het multiresolution‑niveau in te stellen vóór het valideren.
* `Linear subdivision` - Snelkoppeling om het lineaire subdivisie‑niveau in te stellen vóór het valideren. 
* `Division X` - Zelfde als X Divisions in de toolbar.
* `Division Y` - Zelfde als Y Divisions in de toolbar.
* `Curve (Repeater)` - Converteer het curveprofiel naar een [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Insert
Plaats een object op het oppervlak van een ander. In gebruik lijkt het op de Stamp‑tool, maar dan voor volledige 3D‑vormen.

Als je een primitive uit de linker toolbar selecteert, plaatst een klik‑sleep op een oppervlak een primitive waar je klikt; de sleep bepaalt de grootte. Zodra je klaar bent met slepen, schakelt Insert over naar de [Transform](#transform)‑modus.

In Instance‑modus maakt slepen een nieuwe instance en schuift die over het oppervlak. De grootte wordt gedupliceerd van de eerste vorm; zo kun je veel instances van hetzelfde formaat over andere oppervlakken plaatsen.

Je hoeft niet alleen primitives te inserten! Selecteer *elk* object in de outliner; als Insert in Instance‑ of Clone‑modus staat, kun je kopieën van het geselecteerde object over andere oppervlakken slepen.

Als een object een aangepaste pivot heeft, wordt die gebruikt als ankerpunt. Zie de video hieronder.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
Verplaats/roteer/scale een model direct met 1 en 2 vingers, meestal over het oppervlak van een ander object.

De tool wordt bediend met de linker toolbar en heeft 5 knoppen:

* `Snap` - Laat het model op andere oppervlakken snappen
* `Group` - Als het geselecteerde object een combinatie van objecten en instances heeft, kun je hiermee het gedrag van de tool bepalen.
* `Move` - Sleep met één vinger om het object te verplaatsen. Wanneer Snap actief is, schuift dit het object over het oppervlak onder je vinger.
* `Rotate` - Sleep met één vinger om het object te roteren. Wanneer Snap actief is, roteert het rond de normaal van het oppervlak onder je vinger.
* `Scale` - Sleep met één vinger om het object te schalen.

Transform kan snel twee van deze modi gebruiken met twee vingers:

* Sleep een object om het te plaatsen. Stop met het bewegen van je eerste vinger, maar laat hem op het scherm.
* Raak met je tweede vinger het scherm aan terwijl je de eerste vinger neerhoudt. Terwijl de tweede vinger wordt gesleept, wordt het object geschaald.
* Til de tweede vinger op en sleep verder met de eerste vinger; het object staat weer in Move‑modus.

Je kunt de tweede modus ook wijzigen met een tik‑gebaar met de tweede vinger:

* Sleep het object om het te plaatsen, stop met bewegen maar laat je vinger op het scherm.
* Tik met je tweede vinger terwijl je de eerste vinger neerhoudt.
* De tool wordt naar Rotate‑modus gewisseld. Sleep met je eerste vinger om de rotatie in te stellen.
* Tik opnieuw met de tweede vinger; de tool wisselt terug naar Move‑modus.

Dit levert een snelle workflow op om objecten over een ander te klonen, bijvoorbeeld rotsen over een landschap. Merk op dat de Clone‑knop ook in de linker toolbar staat voor snelle toegang:

* Gebruik de Transform‑tool om een rots op zijn plaats te zetten.
* Laat los, druk op de Clone‑knop
* Verplaats deze rots, roteer/scale indien nodig
* Laat los, druk op de Clone‑knop
* Verplaats deze rots, herhaal.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
Met deze tool kun je objecten verplaatsen, roteren en schalen, en pivots van objecten aanpassen.

De viewport‑handle heeft de volgende functies:

* `Move` - Sleep op de lijn+ pijl om op X/Y/Z te verplaatsen. Sleep op de perzikkleurige stip in het midden van de gizmo om vrij in schermruimte te verplaatsen. Klik op de rode, groene, blauwe vierkanten om op de X/Y/Z‑vlakken te verplaatsen.
* `Rotate` - Sleep op de rode/groene/blauwe cirkels om op X/Y/Z te roteren. Sleep op de bol binnen de cirkels om vrij te roteren.
* `Scale`- Sleep op de buitenste rode/groene/blauwe stippen om op X/Y/Z te schalen. Sleep op de buitenste rode/groene/blauwe kegels om op de X/Y/Z‑vlakken te schalen. Sleep op de buitenste perzikkleurige cirkel om uniform te schalen.

![](/images/tool_gizmo.webp)

#### Nodes en vertices 

Elk object in Nomad bestaat uit een node en vertices:

* `Node` - De “handle” van het object, die zijn translatie, rotatie en schaal opslaat, samen de transformation matrix genoemd.
* `Vertices` - De punten die het oppervlak van een object definiëren; ze slaan positie‑ en verfinformatie op.

Als je een eenvoudige box hebt die uit 8 vertices bestaat, kun je hem verplaatsen door zijn transformation matrix te wijzigen, of door de vertexposities te wijzigen. Bij sculpten wil je meestal de vertices aanpassen; bij het verplaatsen van objecten met de gizmo wil je meestal de node aanpassen. Nomad laat je beide doen. 

#### Linker menu‑toolbar

De linker toolbar bepaalt of de gizmo op de node of de vertices werkt, evenals andere functies:

* `Clone` - Maak een zelfstandige kopie van het huidige object, die met de gizmo kan worden weggesleept.
* `Instance` - Maak een instance‑kopie van het huidige object. De objecten zijn gelinkt, dus sculpt‑wijzigingen op één object verschijnen op alle instances.
* `Group/Object/Vertex/Auto` - Bepaalt of de gizmo de node of de vertices van een object beïnvloedt. De standaard 'Auto'‑modus probeert een beste gok te doen. Als er meerdere objecten in een hiërarchie zijn geparent, verplaatst 'Object' alleen het huidige object en blijven child‑objecten op hun plaats. De gizmo kan ook rekening houden met masking en symmetrie.
* `Pin` - Standaard verplaatst de gizmo naar de pivot van het geselecteerde object. Wanneer Pin is ingeschakeld, blijft de gizmo waar hij nu is.
* `Align` - Schakel tussen een pivot die is uitgelijnd met het huidige object of met de wereld.
* `Snap rotation` - Schakel het snappen van rotatiewaarden naar stappen in; de snapwaarde wordt weergegeven en kan worden aangepast wanneer Snap actief is.
* `Snap translation` - Schakel het snappen van translatie‑waarden naar stappen in; de snapwaarde wordt weergegeven en kan worden aangepast wanneer Snap actief is.
* `Pivot` - Wanneer ingeschakeld kan de gizmo worden verplaatst en geroteerd zonder het object te verplaatsen. Er is een extra menu dat hieronder wordt uitgelegd.

#### Pivot
Wanneer Pivot‑modus actief is, wordt een menu weergegeven om snel pivots te wijzigen:

**Reset** 
* `Center` - Verplaats de pivot naar het midden van het object
* `Bottom` - Verplaats de pivot naar de onderkant van het object
* `Align` - Reset de rotaties zodat ze met de wereld zijn uitgelijnd.
* `Mask` - Verplaats de pivot naar het midden van het ongemaskerde gebied.

**On Tap**
* `None` - Doe niets wanneer op het object wordt getikt
* `Normal` - Verplaats en roteer de pivot zodat hij uitgelijnd is met het oppervlak waar wordt getikt
* `First` - Verplaats (maar roteer niet) de pivot naar het oppervlak waar wordt getikt
* `Medial` - Verplaats de pivot naar het midden van het object, onder het oppervlak waar wordt getikt.

#### Gizmo‑instellingen

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - Verplaats het object zodat zijn pivot in het midden van de scene staat, de origin.
* ![](/icons/bake.webp)  `Bake` - “Vries” het object waar het nu staat en zet de translate/rotate‑waarden op 0, scale op 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Laat de matrixwaarden overeenkomen met de positie van de gizmo‑handle in de wereld.
* ![](/icons/reset.webp) `Reset` - Een snelkoppeling die de translatie op 0, rotatie op 0 en schaal op 1 zet, en het object verplaatst en roteert.

::: tip Bake vs bake to pivot
Maak een box, selecteer de Gizmo‑tool, open en pin het instellingenmenu. Standaard zijn de translatie en rotatie 0, schaal is 1.

Schakel Pivot‑modus in, verplaats de handle naar één kant, schakel Pivot‑modus uit. De pivot is veranderd, maar let op dat de translatie‑waarden nog steeds 0 zijn. 

Als je wilt zien waar de pivot *echt* is, klik dan op `Bake Pivot`. Nu worden de translatie‑waarden bijgewerkt. Merk op dat de box tijdens deze bewerking niet beweegt, net als in Pivot‑modus.

Verplaats en roteer de box ergens heen en tik dan op `Move Origin`. Het object wordt verplaatst zodat zijn pivot in het midden van de wereld staat, maar de rotatie blijft ongewijzigd.

Klik op `Reset`, en de rotatie wordt ook op 0 gezet.

Verplaats en roteer de box opnieuw en klik deze keer op `Bake`. De pivot blijft waar hij is, de box blijft waar hij is, maar de translatie‑ en rotatie‑waarden worden op 0 gezet.

Oefen dit een paar keer! Krijg gevoel voor het feit dat de pivot‑waarden verborgen zijn; Nomad regelt het voor je, maar als je de pivot op echte locaties in de ruimte moet zetten, doet Bake Pivot dat voor je.

:::

* `Translation` - De translate X‑, Y‑, Z‑waarden
* `Rotation` - De rotate X‑, Y‑, Z‑waarden
* `Scale` - De uniforme schaal als die is ingeschakeld, of de schaal X‑, Y‑, Z‑ als dat niet zo is.
* `Uniform scale` - Schakel de mogelijkheid om uniform of onafhankelijk per as te schalen

-----

* `Compact` - Schakel de gizmo‑layout om de extra handles buiten of binnen de rotatiebol te plaatsen
* `Widget size` - De grootte van de gizmo
* `Thickness` - De lijndikte van de gizmo
* `Opacity` - De dekking van de gizmo
* `Hide on interaction` - Schakel of de gizmo tijdelijk verborgen moet worden tijdens het slepen

-----

* `Tangent roll threshold` - Bepaalt hoe de rotatie‑UI zich gedraagt bij het slepen op de cirkelhandles om op X/Y/Z te roteren. Als deze waarde 0 is, werkt roteren als een draaiknop: sleep de gizmo in cirkels. Als deze waarde 90 is, werkt roteren als het trekken aan een jojo‑touwtje: sleep in een rechte lijn naar of van het punt waar je eerst klikte. Waarden tussen 0 en 90 doen een combinatie van beide; onder de waarde is het een lineaire beweging, boven de waarde een cirkelvormige beweging.
* `Numerical input` - Wanneer ingeschakeld, toont een enkele tik op de gizmo een venster om een exacte waarde voor de aangetikte widget‑as in te voeren.

::: warning
De [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) en [Scale](#scale) gebruiken hun eigen symmetrie‑checkbox!

Standaard staat deze symmetrie uit.
:::

Links kun je de gizmo‑pivot verplaatsen; je kunt de video hieronder in actie zien.
Dit is vooral nuttig voor rotatie, omdat het niets verandert voor translatie.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

Met Facegroups kun je je object in verschillend gekleurde vlakken organiseren. Je kunt deze groepen op veel manieren in Nomad gebruiken:

* Een snelle selectiemethode voor maskers
* Delen van je object verbergen/tonen
* Je object organiseren zonder het in losse delen te hoeven splitsen
* UV‑regio’s definiëren
* De quad remesher sturen
* Extra controle voor tools zoals Smooth.

#### Facegroup‑linker toolbar

* `Patch ` - Toon de beschikbare facegroups als patches. Ongebruikte patches kunnen worden verwijderd. Tik op een patch om hem te hernoemen of de kleur te wijzigen. Met het plus‑icoon kun je nieuwe patches maken.
* `Dot` - Schilder op het object om facegroups te definiëren. Wanneer '+ Face Group' is ingeschakeld, maakt elke nieuwe stroke automatisch een nieuwe facegroup, handig om snel regio’s te definiëren. Een tik vult de geselecteerde regio. De schuif stelt de radius van de dot in.
* `Relax` - Maak de randen van facegroups glad. Zeer nuttig om schone randen voor quad‑remeshing te definiëren, of om panelen voor hard‑surface‑modellering te definiëren. De schuiven regelen de radius en intensiteit van de relax‑bewerking.
* `Shape selector` - Maak facegroups met vormen in plaats van een brush, via `Lock+Radius`, `Lasso`, `Polygon`, `Rect` en `Ellipse`. Zie [Shape Selector](#shape-selector) voor meer info.
* `Auto-pick` - Wanneer ingeschakeld, wordt de patch geselecteerd waar de stroke begint en wordt die patch voor de rest van de stroke toegepast. Zeer handig om facegroup‑regio’s op te schonen; als een facegroup te ver is doorgetrokken, schakel Auto‑pick in, begin een stroke waar de facegroup‑patch correct is en sleep naar de rand om de juiste patch opnieuw toe te wijzen.

### ![](/icons/tool_hide.webp) Hide
Verberg of isoleer delen van het object. 

De primaire modi worden bediend vanuit het linker menu:

* `Dot` - Brush op het object om delen van het object te verbergen.
* `Shape selector` -  Verberg met vormen in plaats van een brush, via `Lasso`, `Polygon`, `Line`, `Rect` en `Ellipse`. Zie [Shape Selector](#shape-selector) voor meer info.
* `Show` - Keer de bewerking om, zodat de geselecteerde modus delen van het object toont in plaats van verbergt.

Er verschijnt een toolbar bovenaan de viewport met extra bediening:

* `Clear` - Herstel het object; alle verborgen delen worden weer zichtbaar.
* `Invert` - Wissel de verborgen en zichtbare delen om.
* `Facegroup` - Gebruik facegroups om snel secties te verbergen; tikken op een facegroup verbergt de hele facegroup.
* `Mask` - Als er een masker actief is, verbergt het tikken op deze knop het gemaskerde deel.
* `Delete` - Verwijder het verborgen deel van het object
* `Split` - Splits het verborgen deel van het object in een nieuwe vorm.

### ![](/icons/tool_measure.webp) Measure
Sleep om de afstand tussen 2 punten te meten.

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

Deze tool zet het geselecteerde object om in een schone quad‑topologielay‑out, met instellingen voor dichtheid, edge‑flow en symmetrie. 

::: tip
Quad Remesher wordt ontwikkeld door [Exoside](https://exoside.com/) voor iOS en desktop. 

Voor iOS is het een in‑app‑aankoop binnen Nomad, een eenmalige betaling van $16 USD.

Voor desktop koop je een licentie bij [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Je kunt het alleen voor Nomad Desktop kopen, of een cross‑licentie voor alle ondersteunde desktop‑apps.

Als je Quad Remesher al voor een andere desktop‑app bezit, kun je [een upgrade naar alle platforms met korting kopen.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher is niet beschikbaar voor Android. Android kan de gratis open‑source 'Quad Remesh - Instant' gebruiken, beschikbaar onder het Topology -> Misc‑menu, maar begrijp dat de functionaliteit daarvan zeer beperkt is.
:::

Wanneer deze tool voor de eerste keer wordt geactiveerd, wordt gevraagd of je deze als in-app-aankoop wilt inschakelen. Zodra hij actief is, worden de linker- en bovenste werkbalken ingeschakeld.

* `Dot` - Deze brush stelt de doeldichtheid in. Intensiteit op 100% schildert in rood, wat op die gebieden tweemaal de doel-quad-dichtheid zal gebruiken. Intensiteit op 0% schildert in cyaan, wat op die gebieden de helft van de doel-quad-dichtheid zal gebruiken. Intensiteit op 50% schildert in grijs, wat de standaard doel-quad-dichtheid zal gebruiken.
* `Smooth` - Vloei de rood/grijs/cyaan-dichtheidsovergangen.
* `Curve` - Schets curves op het oppervlak van het sculpt; quad remesher zal deze gebruiken als gidsen voor de edge flow. Tik op een curve om deze te verwijderen.
* `Path` - Teken paden op het oppervlak van het sculpt; quad remesher zal deze gebruiken als gidsen voor de edge flow. Tik op een pad om het te verwijderen. 
* `Rect` - Teken rechthoeken op het oppervlak van het sculpt; quad remesher zal deze gebruiken als gidsen voor de edge flow. Tik op een pad om het te verwijderen.
* `Ellipse` - Teken ellipsen op het oppervlak van het sculpt; quad remesher zal deze gebruiken als gidsen voor de edge flow. Tik op een pad om het te verwijderen.

#### Quad remesher bovenste werkbalk
![](/images/tool_quadremesher_toolbar.webp)

Er verschijnt een werkbalk bovenaan de viewport met extra bedieningselementen:


* `<Count>` - Klik hierop om het quad-remesherproces te starten; dit getal geeft aan wat de doel-quad-remesh-telling zal zijn.
* `Quads` - Stel het doel-aantal quads in door naar links en rechts te schuiven, of tik om een exact getal in te stellen. Merk op dat dit meer een richtlijn is dan een vast getal; de verschillende instellingen van de quad remesher zullen er vaak voor zorgen dat het resultaat niet exact overeenkomt met dit doel.
* `Half` - Een snelkoppeling om de doeltelling in te stellen op de helft van het huidige poly-aantal.
* `Same` - Een snelkoppeling om de doeltelling in te stellen op het huidige poly-aantal.
* `Guides` - geeft het totale aantal gidsen aan, of tik om alle gidsen te verwijderen.
* `Density X` - tik om alle dichtheidsschildering te verwijderen.
* `Density (painting)` - schakelaar om dichtheidsschildering te gebruiken of te negeren.
* `Face Group` - schakelaar om facegroups te gebruiken of te negeren om de quad remesher te sturen.
* `Relax` - schakelaar om facegroup-randen automatisch te ontspannen tijdens quad remeshing. Als je je facegroup-randen al hebt ontspannen/gevloeiend, schakel deze optie dan uit.
* `Relax Slider` - Een snelkoppelingsslider om de facegroup-randen te ontspannen.
* `Hard Edges` - schakelaar om te proberen harde randen te behouden.
* `Reproject Vertex` - schakelaar om de nieuwe layout terug te projecteren op de inputmesh.
* `Symmetry` - Schakelaar om een symmetrisch resultaat in te schakelen. Merk op dat symmetrie altijd rond de wereld-x-as wordt berekend, dus zorg dat je model zich op de oorsprong bevindt als je een symmetrisch resultaat verwacht.
* `...` - Quadremesher-instellingenmenu. 

#### Quad remesher-instellingenmenu

De meeste van deze instellingen zijn beschikbaar in de bovenste werkbalk.

* `<Count>, Half, Same` - Hetzelfde als de Remesh-, Half-, Same-knoppen in de bovenste werkbalk.
* `Target Quads` - Hetzelfde als de `Quads`-knop in de bovenste werkbalk
* `Adaptive quad count` - schakelaar om kleinere quads te gebruiken in gebieden met hoge kromming, en grotere quads in gebieden met lagere kromming.
* `Adaptive size` - Stel de hoeveelheid adaptiviteit in. 100% staat maximale adaptieve grootte toe; bij 0% zullen quads uniform zijn.
* `Auto-Detect Hard Edges` - schakelaar om de quad-remesh-layout aan te passen zodat deze beter scherpe oppervlakken volgt.
* `Density (painting)` - Hetzelfde als de `Density (painting)`-knop in de bovenste werkbalk
* `Reproject Vertex` - schakelaar om de nieuwe layout terug te projecteren op de inputmesh.
* `Face Group` - Hetzelfde als de `Face Group`-knop in de bovenste werkbalk
* `Relax Slider` - Een snelkoppelingsslider om de facegroup-randen te ontspannen.

::: tip

Een recept om een goede quad-remesh met minimale artefacten te krijgen:

* Maak facegroups op de mesh om je ideale quad-flow te definiëren.
* Facegroup relax om vloeiende facegroup-randen te krijgen.
* Decimate. Dit zorgt ervoor dat je geen dunne of vervormde vlakken op de facegroup-rand hebt. Zorg er in de decimate-instellingen voor dat facegroup is ingeschakeld. Dit zorgt ervoor dat driehoeksranden je facegroup-randen precies volgen. 

Zorg er in de quad-remesh-opties voor dat relax is uitgeschakeld (aangezien je de mesh al hebt ontspannen) en je zou goede resultaten moeten krijgen.

:::

### ![](/icons/tool_select.webp) Select
Gebruik de vormmodi om objecten in de scène te selecteren. `Unselect` zal objecten uit de selectie verwijderen.

### ![](/icons/tool_view.webp) View
Deze "tool" doet op zichzelf niets bijzonders; dit is simpelweg een manier om het model te bekijken zonder je scène te wijzigen.


## Toolbox-contextmenu

![](/images/tools_context_menu.webp)

Een rechtermuisklik of lange druk op een tool in de toolbox opent een contextmenu. Dit menu heeft de volgende opties:

* `Save` - sla alle wijzigingen op die je aan de tool hebt aangebracht
* `Clone` - dupliceer de tool naar een nieuwe tool-snelkoppeling
* `Last save` - herstel de eerder opgeslagen versie van de tool
* `Icon` - wijzig het pictogram voor de tool
* `Reset` - reset de tool naar de standaardinstellingen
