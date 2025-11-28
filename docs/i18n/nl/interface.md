# ![](/icons/interface.webp) Interfacemenu {#interface-menu}

Dit menu beheert veel opties om de interface van Nomad aan te passen. 

![](/images/interface_overview2.webp)

Nomad kan tot op een vrij diep niveau worden aangepast, dit menu is verdeeld in 4 secties: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Deze pagina gaat over het interfacemenu, niet over de interface zelf! De algemene interface wordt beschreven in [Getting Started](gettingstarted.md).
:::

## Interface {#interface}

In de sectie Interface kun je snelkoppelingen toevoegen, zwevende werkbalken maken en de kleur, grootte en het uiterlijk van de gebruikersinterface van Nomad regelen.

![](/images/interface_overview3.webp)

### Snelkoppelingen toevoegen (onder)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

De onderste werkbalk heeft standaard deze snelkoppelingen ingeschakeld:
* `Undo` - maak de vorige bewerking ongedaan
* `Redo` - herstel de eerder ongedaan gemaakte bewerking
* `Solo` - Verberg tijdelijk alle andere objecten, zodat alleen het geselecteerde zichtbaar blijft. Nogmaals drukken om alle objecten te herstellen.
* `X-ray` - Maak tijdelijk alle andere objecten half transparant, zodat alleen het geselecteerde object massief blijft. Nogmaals drukken om de standaardmaterialen te herstellen.
* `Voxel remesh` - Remesh het huidige object met de laatst gebruikte voxelresolutie. Een lange tik of een veeg omhoog opent een resolutieschuifregelaar en een schakelaar voor scherpe randen.
* `Grid` - Schakel het raster in de weergave in/uit. Een lange tik of een veeg omhoog maakt het mogelijk de kleur en dekking van het raster aan te passen.
* `Wireframe` - Schakel een wireframe-overlay in/uit. Een lange tik of veeg omhoog maakt het mogelijk de kleur en dekking van de wireframe aan te passen.
* `Inspector` - hiermee kun je eigenschappen van je mesh bekijken, zoals uv’s, gebakken textures en andere eigenschappen, over de achtergrond van Nomad heen.
* `Face Group` - Schakel de facegroup-overlay in/uit, meer info onder [Tools->FaceGroup](tools.md#facegroup) 

Andere veelgebruikte snelkoppelingen zijn beschikbaar via dit menu, veel meer zijn te vinden via de bindings-knop.

#### ![](/icons/more.webp) Koppelingen {#bindings-list}

Bijna elke functie van Nomad kan via de bindings-knop aan de snelkoppelingswerkbalk worden toegevoegd. Wanneer je op de knop klikt, verschijnt een bindingsmenu:

![](/images/interface_bindings_search.webp)

Je kunt per categorie zoeken via de pictogrammen bovenaan, of via het zoekveld functies op naam vinden. Klik op een functie om deze aan de werkbalk toe te voegen. Klik nogmaals om hem te verwijderen.

#### ![](/icons/list.webp) Volgorde {#order}

Dit toont een lijst van de snelkoppelingen. Lang indrukken en slepen om de snelkoppelingen te herschikken.

#### ![](/icons/reset.webp) Reset {#reset}

Reset herstelt de onderste werkbalk naar de standaardinstellingen.

### Snelkoppelingen toevoegen (venster)... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Door op de + te klikken voeg je een zwevende werkbalk toe. Deze is niet zichtbaar totdat je op de bindings-knop klikt en er snelkoppelingen aan toevoegt; daarna kun je hem zichtbaar maken. 

Je kunt meerdere werkbalken maken, elke werkbalk heeft in dit menu de volgende opties:

* ![](/icons/checked.webp) `Visible` - Schakel de zichtbaarheid van de werkbalk in/uit
* ![](/icons/more.webp)`Bindings` - Toon het bindingsvenster om functies aan de werkbalk toe te voegen of eruit te verwijderen.
* ![](/icons/list.webp)`Order` - Toon een menu om de werkbalk te herschikken.
* ![](/icons/reset.webp) `Reset` - Reset de werkbalk naar de standaardstatus.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Schakel een resize-hendel in de rechterbenedenhoek van de werkbalk in/uit.
* ![](/icons/sort_down.webp) `Collapsable` - Schakel een inklaphendel in de rechterbovenhoek in/uit.
* ![](/icons/trash.webp) `Delete` - Verwijder de werkbalk.

### Gereedschapskist {#toolbox}

Opties voor het toolmenu aan de rechterkant van de Nomad-interface.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) UI-hoek voor formaat wijzigen {#ui-resize-corner}

Schakel een resize-hendel in de onderste hoek van de werkbalk in/uit.

#### Verborgen {#hidden}
Normaal gesproken schakelt het toolbox-pictogram in de bovenbalk tussen een lange enkele kolom of een lijst met meerdere kolommen met tools. Deze optie schakelt tussen de lijst met meerdere kolommen of volledig verborgen.

#### Gekleurd {#colored}
Kleurcodeer de pictogrammen per categorie, bv. alle mask-tools zijn bruin, split-tools rood, flatten-tools groen, enz.

#### Rijen: Auto (>1) {#rows-auto-1}

#### Volgorde resetten {#reset-order}
Herstel de standaardtools in de toolbox naar de standaardvolgorde. Aangepaste pictogrammen blijven in de toolbox aan het einde van de lijst staan.


### Presets {#presets}

![](/images/interface_presets.webp)

Een verzameling kleurpresets voor de interface.

#### Hoog-contrastknop {#high-contrast-button}
Een alternatieve stijl voor knoppen die ze beter zichtbaar maakt wanneer ze zijn ingeschakeld. Als deze op Auto staat, gebruikt Nomad deze modus wanneer het UI-kleurcontrast tussen ingeschakeld/uitgeschakeld laag is.

#### Kleurwidget/Kleurbasis {#color-widgetcolor-base}
De primaire kleuren die in de interface worden gebruikt.

#### Transparant paneel, Kleurpaneel, Vervagingssterkte {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Wanneer ingeschakeld, verschijnen extra opties om te bepalen hoe menu’s en panelen er in Nomad uitzien. Hun kleur, transparantie en hoeveelheid vervaging kunnen worden aangepast.

::: tip
Op kleine apparaten kan het nuttig zijn om het kleurpaneel bijna wit, transparant en met een lage blur strength te maken, zodat menu’s de scène niet bedekken.
:::

----

### Bovenbalk spiegelen {#mirror-top-bar}
Keer de volgorde van de menu’s in de bovenbalk om.

### Zijbalken spiegelen {#mirror-side-bars}
Wissel de zijbalken zodat de toolbox links staat en de toolopties rechts.

### Onderbalk spiegelen {#mirror-bottom-bar}
Verplaats de onderbalk naar de rechterbenedenhoek en keer de volgorde van de knoppen om.

### Materiaalkleurvoorbeeld {#material-color-preview}
Wanneer je een kleur voor een materiaal selecteert, wordt een voorbeeld van dit materiaal weergegeven op het momenteel geselecteerde object.

----
### Hulp-pop-up bij hover {#help-popup-on-hover}

Voor apparaten die hover ondersteunen: bepaal of de contexthelp in Nomad, weergegeven met het ![](/icons/help.webp)-pictogram, bij hover verschijnt of alleen wanneer erop wordt geklikt.

----

### Totale schaal {#overall-scale}
Een schaalfactor voor alle UI-elementen.
### Paneelbreedte {#panel-width}
De breedte van de menu’s en panelen.
### Lettertypeschaal {#font-scale}
Schaal de lettertypen.
### Verticale afstand {#vertical-spacing}
De afstand tussen elementen in menu’s en panelen.
### Verticale afstand (links) {#vertical-spacing-left}
De afstand tussen elementen in de linker werkbalk.

----

### Randmarge {#edge-offset}
Je zou deze waarden alleen moeten wijzigen als je problemen hebt met het bedienen van knoppen aan de schermranden. Als deze schuifregelaars zijn uitgeschakeld, gebruikt Nomad de veilige-gebied-waarden die door het apparaat zelf worden teruggegeven.

::: tip
Wanneer je Nomad naar een nieuw apparaat migreert (bijv. een iPhone 12 vervangen door een iPhone 15), zorg er dan voor dat je de edge-opties naar de standaardwaarden reset!
:::

### Stijl resetten {#reset-style}
Reset alle UI-elementen naar hun standaardwaarden.


## Gebaar {#gesture}
Het gesture-menu bepaalt hoe stylus- en vingerinvoer Nomad aanstuurt.

![](/images/interface_gesture.webp)

### Gebaaropties {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad kan bewerkingen beperken op basis van het invoerapparaat. Zo kan een vinger-sleep alleen de camera bewegen, terwijl een stylus-sleep alleen sculpt. Als je een muis of trackpad hebt, kan die ook worden toegewezen aan specifieke bewerkingen.

Nomad laat je momenteel deze modi instellen voor elke combinatie van vinger-, stylus- of muis-gesture:

* Camera
* Sculpt
* Gizmo
* Material picking (via een lange tik)
* Select object


`Finger always smooths` - Smooth kan zo worden ingesteld dat het alleen werkt met een vinger-sleep.

### ![](/icons/tool_mask.webp) Masker {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Schakel de volgende one-tap-snelkoppelingen in zonder de mask-knop ingedrukt te hoeven houden. Dit maakt de volgende gestures mogelijk:
* tik op de achtergrond om de mask te inverteren
* tik op een gemaskeerd gebied om de mask te vervagen (blur)
* tik op een ongemaskeerd gebied om de mask te verscherpen (sharpen)

### Masker <-> SelMask wisselen {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Lang indrukken schakelt tussen Mask en SelMask en start een nieuwe stroke. Aan het einde van de stroke wordt de vorige tool opnieuw geselecteerd. 
* `Tool` - Lang indrukken en loslaten zonder te bewegen om tussen Mask en SelMask te wisselen. 

### ![](/icons/tool_hide.webp) Verbergen {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` schakelt de volgende snelkoppelingen in bij gebruik van de hide-tool:
* Tik op een face group om deze te verbergen
* Tik in lege ruimte om de verborgen polygonen te inverteren

### ![](/icons/finger3.webp) Drie vingers {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Als je apparaat 3-vinger-gestures ondersteunt, kun je hier snelkoppelingen voor dat gebaar configureren. 

De optiematrix laat je verticale en horizontale sleepbewegingen als aparte snelkoppelingen definiëren. Merk op dat als hetzelfde gebaar voor 2 opties wordt gekozen, één ervan wordt uitgeschakeld.

* `Rotate lighting` - Draai de environment, lichten en Matcap.
* `Tool Radius` - Pas de toolradius aan.
* `Tool Intensity` - Pas de toolintensiteit aan. 

### ![](/icons/fingerprint.webp) Geschiedenis 2/3 {#history-23}
`History shortcuts` - wanneer ingeschakeld, zijn de volgende gestures actief:
* Undo - tik met 2 vingers
* Redo - tik met 3 vingers

`Long press` - wanneer ingeschakeld, zorgt het ingedrukt houden van 2/3 vingers voor snel herhaald undo/redo.

### Toegankelijkheid {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` opent een zwevende werkbalk om drag-, pinch-, roll- en camera-bewerkingen te bedienen.

### Camera {#camera}
Een snelkoppeling naar het `Camera`-menu (cameraopties stonden vroeger hier, maar zijn naar het cameramenu verplaatst).

### Pencil dubbel tikken -> Koppelingen {#pencil-tap}

Een snelkoppeling naar het `Bindings`-menu (Pencil tap- en double tap-opties stonden vroeger hier, maar zijn naar het bindingsmenu verplaatst).


## Koppelingen {#bindings}
Toetsenbord- en knopsnelkoppelingen kunnen worden gedefinieerd in het bindingsmenu:

![](/images/interface_bindings.webp)
Bijna alle functies in Nomad kunnen worden gekoppeld aan toetsenbordsnelkoppelingen als je apparaat een toetsenbord heeft, of aan extra knoppen op je stylus, of zelfs gamepad-controllers.

Om een binding te maken, klik je op het rechthoekje naast de functie en druk je op de toets/knop. 

Zoek functies via de categoriepictogrammen bovenaan, of via de zoekbalk op naam. 

Individuele bindings kunnen worden uitgeschakeld via het selectievakje naast de naam van de binding.

### ![](/icons/more.webp) Contextmenu {#context-menu}
Het ![](/icons/more.webp)-pictogram achter elke binding opent een contextmenu:

![](/images/interface_bindings_context.webp)

* `Clone` - Dupliceer de binding
* `Reset` - Reset de binding
* `Delete` - Verwijder de binding
* `Toggle shortcut on key tap` - Stel in of een tik versus lang indrukken verschillend worden behandeld. Wanneer ingeschakeld, activeert een tik de tool. Een lange druk activeert de tool alleen zolang de toets is ingedrukt; bij loslaten wordt teruggekeerd naar de vorige tool. Dit wordt in andere 3D-apps soms ‘sticky keys’ genoemd.

### Geavanceerd {#advanced}
Onderaan het bindingsmenu staat een tandwielmenu voor geavanceerde opties:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Een tik op de standaard-snelkoppelingen voor mask, smooth, gizmo, hide, sub schakelt naar die modus, maar het ingedrukt houden van de toets schakelt tijdelijk naar die modus; wanneer de toets wordt losgelaten, keert de modus terug naar de vorige. Dit wordt in andere 3D-apps soms ‘sticky keys’ genoemd.
* `Toggle tool shortcuts` - Wanneer je een van de tool-snelkoppelingen gebruikt en dezelfde snelkoppeling twee keer indrukt, wordt er teruggeschakeld naar de vorige tool. Zo kun je met dezelfde hotkey blijven wisselen tussen twee tools.
* `Invert Y (Zooming)` - Keert de zoomrichting om.
* `Reset bindings` - reset alle bindings naar de standaardwaarden.


## iOS ⌘ Sneltoetsweergave toetsenbord {#ios-keyboard-shortcuts-display}

Op iOS-apparaten met een toetsenbord kun je de ⌘ (cmd)-toets ingedrukt houden om een lijst met snelkoppelingen weer te geven.

Android-toetsenbordondersteuning is nog wat experimenteel.

![](/images/shortcuts.webp)


## Debug {#debug}
Enkele experimentele en debug-opties zijn in dit menu ondergebracht. Veel van deze opties zouden op de standaardwaarden moeten blijven en alleen gewijzigd moeten worden na contact met Nomad-support.

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad normaliseert de UV’s binnen de [0-1]-tile.

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Schakel het instant remesh-algoritme in
* `Quadriflow` - Een alternatieve quad-remesh-methode.

### Renderen {#render}
* `Heightmap` - Verander de viewport zodat de diepte van de scène wordt gerenderd. Dit kan worden gebruikt om alpha maps te maken voor brushes.
* `Refraction write depth (back)` - De achterkant van refractie-meshes wordt in de depth buffer geschreven.
* `Flip Y (normal map)` - Inverteer het y-kanaal bij het bakken van normal maps, vereist voor bepaalde game- en render-engines.
* `Angle weighted smooth normals` - Een aanpassing van hoe smooth shading werkt, die in bepaalde gevallen vouwen kan voorkomen.

### Doel-FPS {#target-fps}
Wanneer uitgeschakeld, synchroniseert Nomad zijn frames-per-second met de verversingssnelheid van je scherm.

Wanneer ingeschakeld, kun je het aantal frames per seconde instellen dat Nomad rendert.

### Interface {#debug-interface}
* `Top: layout` 
  * Collapse: Op kleine apparaten wordt de bovenbalk samengevouwen in meer submenu’s. 
  * Scroll: Als je Nomad op grote schermen gewend bent en de normale lay-out verkiest, kun je hiermee de standaard brede bovenbalk gebruiken, die dan scrollbaar is.
  * Multiline: Toon het volledige bovenmenu over meerdere regels.
* `Bottom: draggable popup` - De onderste werkbalk heeft verschillende knoppen die een dialoogvenster openen. Als deze optie is ingeschakeld, kunnen die dialogen naar een andere plek op het scherm worden verplaatst.  
* `Toolbox: show all` - Nomad verbergt tools die niet relevant zijn voor de huidige selectie, bv. alle sculpt-brushes worden verborgen op primitieve objecten die nog niet gevalideerd zijn. Met deze optie worden niet-relevante tools gedimd in plaats van verborgen.
* `Toolbox: colored` - Kleurcodeer de toolbox-pictogrammen op basis van hun type.
* `Panel: Drop shadows` - Teken slagschaduwen rond menu’s en panelen. Op sommige oudere apparaten kan dit de prestaties beïnvloeden.
* `Panel: Blending` - Debug-optie
* `Pointer: hovering dot` - Voor apparaten die stylus-hover ondersteunen: toon een punt wanneer de stylus boven menu’s en panelen zweeft.

### Gif-turntable {#gif-turntable}
Nomad kan een geanimeerde gif-turntable exporteren. Let op: door beperkingen van het gif-formaat is de kwaliteit laag. Schermopname is meestal een betere methode.

* `Duration` - hoe lang de turntable in seconden duurt
* `Rotation center` - waar het camerapivot zich bevindt, dus rond welk deel van de scène de camera draait
* `Transparent background` - Gebruik de transparante optie voor gifs. Let op: gifs ondersteunen slechts 1-bit-transparantie, waardoor randen sterk gealiasd kunnen zijn.
* `Max frame sampling` - Veel van Nomads hoogwaardige rendereffecten komen voort uit het combineren van meerdere frames. Deze schuifregelaar bepaalt hoeveel frames worden gecombineerd.
* `Export (GIF)` - start het gif-exportproces.

### Nabewerking {#post-process}
* `Filtering` - Debug-optie
* `Format` - Debug-optie
* `Buffer reuse` - Debug-optie

### Prestaties {#performance}
* `Multicore general` - Debug-optie
* `Multicore sculpting` - Debug-optie
* `Partial Drawing` - Experimentele functie! Gebruik dit als je een relatief klein deel van een high-poly mesh aan het sculpten bent. Het zou het sculpten vloeiender moeten maken, maar je moet geen wireframe inschakelen! Ook kan het visuele artefacten veroorzaken tijdens brush-strokes.

### Functie {#feature}
* `Flip quad split (on tap)` -  Debug-optie
* `Join: merge radius` - Vertexen worden automatisch gelast als ze dicht genoeg bij elkaar liggen wanneer meshes worden samengevoegd. Je kunt de radius met deze schuifregelaar aanpassen.

### Debug {#dev}
* `Logs` - Toon een logvenster
* `App review popup` - Debug-optie
* `FPS` - voeg een frames-per-second-teller toe aan de viewport-statistieken.