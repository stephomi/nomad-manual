# ![](/icons/pencil.webp) Lijn    

---
![](/images/stroke_overview.webp) 

## Overzicht 

Je kunt het lijn-/strokegedrag van de meeste gereedschapspenselen aanpassen.
De instellingen lijken op die van 2D‑tekenapplicaties, maar sommige opties zijn specifiek voor sculpting en 3D.

De opties zijn verdeeld over 5 submenu’s:

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Bepaalt hoe de stroke wordt toegepast op het model                 |
| Alpha    | ![](/icons/alpha.webp)      | Hoe een grijswaarden‑textuur wordt gebruikt voor de brush‑stempel  |
| Falloff  | ![](/icons/falloff.webp)    | Bepaalt hoe de brush‑sterkte verandert van het midden naar de rand |
| Filter   | ![](/icons/filter.webp)     | Hoe de brush wordt beïnvloed door de modelgeometrie                |
| Pressure | ![](/icons/pressure.webp)   | Bepaalt de reactie op pen-/stylusdruk                             |

::: tip
Niet alle stroke‑opties zijn van toepassing op alle tools. Stroke‑opties die niet door het huidige gereedschap worden gebruikt, worden uitgeschakeld of verborgen. 
:::


## Stroke

### Radius

![](/images/stroke_radius.webp)

#### Share radius

Indien ingeschakeld gebruiken alle tools dezelfde radius; standaard heeft elk gereedschap zijn eigen radius.

#### Size

* Screen - de radius wordt ingesteld in scherm‑eenheden. Als je de radius 100 pixels breed maakt, blijft hij 100 pixels breed, ongeacht of je in- of uitzoomt.
* Constant (3d) - de radius wordt ingesteld in 3D‑eenheden. Als je bijvoorbeeld een bol maakt en de radius even groot maakt als de bol, blijft de radius even groot als de bol terwijl je in- en uitzoomt.


### Stroke

![](/images/stroke_strokemode.webp)

Strokes kunnen in meerdere modi werken:

### ![](/icons/stroke_dot.webp) Dot
Sleep als een normale verfstroke. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
De brush‑alpha wordt geroteerd zodat hij de richting van de stroke volgt, handig voor het maken van bijvoorbeeld stiknaden in stof. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
 Stempel een brush‑stroke met vaste **_hoogte_**. Slepen bepaalt de schaal en rotatie.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Stempel een brush‑stroke met vaste **_radius_**. Slepen bepaalt hoogte en rotatie.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

De `Move`‑ en `Drag`‑tools hebben hun eigen 3 opties:

### ![](/icons/snake.webp) Drag

Blijft tijdens de stroke alles binnen de brush‑radius updaten. Een snelle stroke laat het oppervlak achter, terwijl een langzame stroke materiaal vasthoudt en langere vormen maakt. Dit is de standaardmodus voor de `Drag`‑tool. Met `Dynamic Topology` kun je hiermee slangachtige extrusies maken. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Selecteert wat zich binnen de brush‑radius bevindt wanneer je de stroke start, en behoudt die selectie. Dit is handig voor preciezere verplaatsingen, omdat je de afstand zorgvuldig kunt aanpassen zonder per ongeluk meer te verplaatsen dan je oorspronkelijk selecteerde. Dit is de standaardmodus voor de `Move`‑tool.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
De gebruikersradius wordt genegeerd en dynamisch ingesteld op basis van hoe ver de stroke van het startpunt wordt weggesleept. Kleine afstand = kleine radius, grotere afstand = grotere radius. Gebruik de intensiteitsschuif om de vorm van de falloff te regelen. Handig voor het blokken van organische, rubberachtige vormen.
![](/videos/stroke_lockradius_drag.mp4) 



### Adjust spacing intensity
![](/images/stroke_space_smooth.webp)

Strokes met een lage spacing (lager dan 50%) kunnen zich snel opstapelen en intensere strokes geven dan hogere spacing‑waarden. Deze schakelaar compenseert dat, zodat strokes ongeveer dezelfde intensiteit hebben ongeacht de spacing.

### Stroke spacing
Hoe ver uit elkaar elke brush‑stempel wordt geplaatst tijdens een sleepbeweging. Waarden lager dan 100% overlappen, wat de indruk van een doorlopende stroke geeft. Waarden hoger dan 100% laten gaten ontstaan, handig voor details zoals stiksels of ritsen.

### Lazy rope stabilizer
Strokes lopen een bepaalde afstand achter op de cursorpositie. Dit kan worden gebruikt om vloeiende lijnen te tekenen.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke smoothing
Meerdere cursorposities middelen om een vloeiendere stroke te krijgen.
Bij hoge waarden loopt de stroke achter op de cursor, maar haalt uiteindelijk weer in.
Dit is handig voor het tekenen van strakke, vloeiende lijnen.

### Snap radius
Laat het begin van de stroke vastklikken aan het einde van de vorige stroke. De radius bepaalt hoe ver er wordt gezocht naar het einde van de vorige stroke. Dit kan nuttig zijn bij het tekenen van lange doorlopende lijnen met frequente pauzes.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Standaard beïnvloeden strokes alleen het modeloppervlak binnen de brush‑radius. Wanneer Silhouette is ingeschakeld, wordt de stroke door het hele model heen geprojecteerd. Dit is erg handig bij het eerste blokken van een model, of voor vormen waarbij de zijkanten loodrecht moeten blijven.

De projectierichting kan expliciet worden ingesteld; de standaardmethode ‘Closest’ detecteert de beste hoek ten opzichte van het camerastandpunt. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

De intensiteit, translatie, rotatie en schaal van de stroke kunnen afzonderlijk worden gerandomiseerd. Dit kan worden gebruikt om allerlei effecten te creëren; bijvoorbeeld randomize met de paint‑tool kan gevlekte kleur maken, of randomize met de crease‑tool kan worden gebruikt om huiddetails te creëren.

![](/videos/stroke_randomize.mp4) 

### Stroke Offset

Pas een constante offset toe op de stroke. Dit is handig op kleine schermen waar je vinger de stroke zou bedekken. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

De `Alpha` is een textuur die het gedrag van je brush moduleert.
Het is een grijswaardenafbeelding, waarbij zwarte pixels geen vervorming betekenen en witte pixels maximale vervorming.

Klik op de alpha‑afbeelding om deze te wijzigen.

Klik op de materiaalpreview om een alpha uit een materiaalpreset te laden. Je kunt hier ook materiaalpresets opslaan en ervoor kiezen om texturen met het gereedschap in te sluiten.

::: tip
De textuur wordt nooit herschaald, dus grote texturen kunnen de prestaties vertragen.
:::

### Invert pixels
Dit keert de waarden van de afbeelding om, zodat zwarte pixels wit worden en witte pixels zwart.

::: tip

De ingebouwde alphas die met Nomad worden meegeleverd, kunnen niet worden geïnverteerd.

:::

### Scaling

De brushgrootte in Nomad is een cirkel met een door de gebruiker gedefinieerde radius. Texturen zijn vaak vierkant of rechthoekig; met de `Scaling`‑parameters bepaal je hoe de textuur in de cirkel past. Voor een vierkante textuur past een waarde van 0,7 binnen de cirkel. Een waarde van 1 schaalt de textuur groter zodat de cirkel erin past, waarbij de randen worden afgeknipt.

![](/images/alpha_scaling.webp) 

Als je `Scaling - Y` inschakelt, kun je de alpha verticaal uitrekken.

![](/images/alpha_scaling_y.webp) 

### Rotation

De alpha‑textuur wordt geroteerd zodat hij de richting van de stroke volgt. Je kunt een rotatie‑offset toevoegen, en als het slot‑icoon is ingeschakeld, blijft de textuur vergrendeld op deze rotatie ten opzichte van het scherm.

### Tiling
![](/images/stroke_tiling.webp) 

Hoe vaak de textuur zich binnen het brushprofiel herhaalt. De tiling‑modi laten je kiezen tussen één enkele textuur binnen de stroke, herhaalde texturen, of gespiegeld, waarbij elke tweede textuur wordt omgedraaid om patronen te maken of te helpen naadloze texturen te creëren.

![](/videos/alpha_tiling.mp4) 



### Mid value

Standaard betekent zwart geen vervorming en wit volledige positieve vervorming; een clay‑brush met een alpha‑textuur van rotsen zal dus alleen het oppervlak naar buiten trekken waar de alpha niet zwart is.

Als je wilt dat de brush het oppervlak naar binnen duwt, of zowel naar binnen als naar buiten duwt, kun je de mid value aanpassen. Als je de waarde bijvoorbeeld op 0,5 zet, doet een middengrijze waarde in de alpha niets, zwart duwt naar binnen en wit trekt naar buiten.




## Falloff

![](/images/falloff_menu.webp) 

Dit lijkt op de [Alpha](#alpha), behalve dat je de intensiteit met één curve aanstuurt. Deze wordt gecombineerd met de alpha, zodat je een textuur kunt gebruiken voor detail en falloff om de randvervaging en intensiteit in het midden van de tool te regelen.

Wanneer de curve bovenaan staat, is dat volledige vervorming; wanneer hij onderaan staat, heeft de brush geen effect.

Je kunt de curve zien als een dwarsdoorsnede door de punt van de brush. Het onderste gedeelte geeft een voorbeeld van hoe een enkele ‘stempel’ van de brush eruit zou zien op het modeloppervlak, en als er een alpha‑textuur voor de brush is, wordt die ook getoond om te laten zien hoe falloff en alpha samen werken.

### Preset
Met deze optie geselecteerd, opent een tik op de curvegrafiek een menu met presets. Afgeronde curves geven zachtere resultaten, hoekige curves scherpere resultaten. De knop `Sub` in de linkertoolbar keert de falloff in feite om, zodat de bovenkant van de curve in het oppervlak duwt in plaats van eruit te trekken, of andersom.

### Catmull-Rom
Indien geselecteerd kan de gebruiker eigen falloff‑curves tekenen. De curve‑editor werkt hetzelfde als curves in de rest van Nomad:

* Klik op de curve om een nieuw punt te maken
* Sleep een punt om het te verplaatsen
* Klik op een punt om te wisselen tussen scherp en vloeiend
* Sleep een punt in een naburig punt om het te verwijderen

### B-spline
Indien geselecteerd kan de gebruiker eigen falloff‑curves tekenen. De editor werkt hetzelfde als bij Catmull‑Rom, maar de punten beïnvloeden de curve in plaats van er precies op te liggen, wat kan helpen om vloeiendere curven te maken.

De curve‑editor heeft 3 knoppen:

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | De curve‑editor uitvouwen                    |
| Reset    | ![](/icons/reset.webp)     | De curve terugzetten naar de standaardstaat  |
| Symmetry | ![](/icons/symmetric.webp) | De curve tonen als een symmetrische ‘brush’  |


### Influence

* Sphere (3d) - De invloed wordt berekend door de afstand van de vertex tot het midden van de brush te nemen.
* Circle (2d) - De vertex wordt eerst op het vlak van het gebied geprojecteerd, waarna de afstand tot het midden van de brush wordt genomen. Dit lijkt op hoe alphas worden gesampled. 
* Cylinder - De invloed wordt als een cilinder door het gebied heen geprojecteerd, gebruikt door de Silhouette‑modus hieronder.

### Silhouette
Standaard beïnvloeden strokes alleen het modeloppervlak binnen de brush‑radius. Wanneer Silhouette is ingeschakeld, wordt de stroke door het hele model heen geprojecteerd. Dit is erg handig bij het eerste blokken van een model, of voor vormen waarbij de zijkanten loodrecht moeten blijven.



## Filter

![](/images/filter_menu.webp) 

### Accumulate stroke
Schakel de limiet uit op hoeveel materiaal per stroke kan worden toegevoegd of verwijderd. De `Clay`‑tool heeft dit bijvoorbeeld ingeschakeld, zodat materiaal kan blijven opbouwen, terwijl de `Brush`‑tool dit uitgeschakeld heeft, zodat strokes stoppen met materiaal toevoegen als je herhaaldelijk over hetzelfde gebied gaat. 

### Front-facing vertex only
Deze optie negeert naar achteren gerichte vertices.
Dit kan handig zijn als je een deel van een dunne geometrie wilt schilderen zonder de andere kant te beïnvloeden.
Het werkt ook voor sculpting, maar je kunt soms artefacten ervaren.

### Allow dynamic topology
Deze optie is alleen beschikbaar als je mesh in de [Dynamic Topology](topology.md#dynamic-topology)‑modus staat. Je kunt dynamic topology per tool in- of uitschakelen.

### Connected topology
Schakel in om alleen vertices te sculpten die verbonden zijn met het oppervlak dat je met de tool aanraakt. Bijvoorbeeld: in combinatie met de `Move`‑tool kun je hiermee een deel verplaatsen, zelfs als het een ander deel kruist.
![](/videos/connected_topology.mp4)

### Protect Area
![](/images/filter_protect_area.webp) 

Deze opties voorkomen dat tools bepaalde delen van je mesh beïnvloeden onder verschillende voorwaarden. 

De optie ‘Auto’ betekent dat als je hide, mask of facegroup zichtbaar hebt in het [Shading](shading)‑menu, ze worden beschermd; maar als ze daar zijn uitgeschakeld, is de bescherming ook uit.

* `All` - Schakelaar om in te stellen of de protect‑filters globaal zijn of per tool.
* `Hide` - Als delen van de mesh met het hide‑gereedschap zijn verborgen, stel je hiermee in of ze beschermd moeten worden.
* `Mask` - Als delen van de mesh gemaskeerd zijn, stel je hiermee in of ze beschermd moeten worden.
* `Facegroup` - Stel in of je een tool alleen binnen de eerst aangeraakte facegroup kunt gebruiken.


### Keep sharp edges
Sluit punten uit waarvan de normaal te veel afwijkt van de oppervlaknormaal.

Dit verandert hoe het vlakgebied wordt berekend (Area sampling).

Deze optie kan nuttig zijn voor op vlak gebaseerde tools, of als je een grotendeels vlak oppervlak wilt kleuren zonder overspill.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Sommige brushes of stroke‑opties hebben een vlaknoraal en een vlakpositie ten opzichte van het oppervlak nodig om te kunnen werken.

Je kunt bepalen hoe dit gemiddelde vlak wordt berekend door het samplegebied als een verhouding van de toolradius in te stellen.

Bij 100% wordt elk punt binnen de selectiecirkel meegenomen.

Bij 0% wordt alleen de dichtstbijzijnde vertex of driehoek meegenomen. Deze waarden kunnen gekoppeld worden voor zowel `Normal radius` als `Position radius`, of ontgrendeld en onafhankelijk ingesteld.


### Depth masking
![](/images/stroke_depthmask.webp)

Sluit punten uit die zich boven of onder een bepaalde afstand van het berekende vlak bevinden (Area sampling).

Dit kan worden gebruikt om alleen op hobbelige gebieden te schilderen, of alleen in holtes.

De grafiek stelt een dwarsdoorsnede van het oppervlak voor; de horizontale lijn is waar het oppervlak zich bevindt, de cirkel geeft de paint‑falloffradius weer ten opzichte van boven en onder het oppervlak. `Height offset` is een percentage boven of onder het oppervlak om de masking‑berekening te starten. Met `Top area` en `Bottom area` kun je de falloff boven en onder het offsetpunt schalen.

#### Voorbeeld: In holtes schilderen
Om alleen in holtes te schilderen, zet je de height offset op -100% en stel je de top area‑schuif zo in dat hij van de horizontale lijn afligt. Dit betekent dat de eerste klik de ‘nul’‑diepte instelt en dat alleen gebieden onder deze diepte worden beïnvloed.

![](/videos/stroke_depth_cavity.mp4)

#### Voorbeeld: Op bulten schilderen
Om alleen op hoge gebieden te schilderen, zet je de height offset op +90%, zodat de onderkant van de cirkel de horizontale lijn net een beetje kruist. Wanneer je op de top van een ‘hoog’ gebied klikt, stelt dit de diepte in, zodat alles op die diepte, plus een beetje eronder, en alles daarboven, wordt geschilderd. Diepe holtes worden overgeslagen.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Bepaal hoe pen-/stylusdruk de brushes beïnvloedt.

Standaard is `Use global settings` ingeschakeld, wat betekent dat alle brushes dezelfde drukinstellingen delen.

### Pressure - Radius

Deze curve bepaalt hoe de brushradius door druk wordt beïnvloed. Standaard is de relatie lineair, dus als je stylus een vloeiende respons heeft, zou de radiusverandering ook vloeiend moeten aanvoelen. Veel styli hebben echter een niet‑lineaire respons, die je met deze curve kunt compenseren. Als de radius bijvoorbeeld niet lijkt zijn maximale waarde te bereiken bij hoge druk, kun je een curvepreset zoals ‘out-pow3’ gebruiken, met een bocht omhoog, om de radius eerder te laten toenemen.

Deze dialoog lijkt op de falloff‑curvedisplay; je kunt een preset gebruiken door op het curvevenster te tikken, of je eigen curves tekenen met de Catmull‑Rom‑ en B‑Spline‑modi.

Als je een constante radius wilt, schakel je deze sectie uit.

### Pressure - Intensity

Vergelijkbaar met de radius‑curve, maar dan voor de intensiteit. Als je een constante intensiteit wilt, schakel je deze sectie uit.

### Pressure smoothing

Middelt de stylusdruk‑events voor vloeiendere resultaten.
