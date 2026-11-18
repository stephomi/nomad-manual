# ![](/icons/sliders.webp) Menu Interface {#interface-menu}

Met dit menu pas je de interface van Nomad op allerlei manieren aan. 

![](/images/interface_overview2.webp)

Je kunt Nomad tot in detail naar je hand zetten. Dit menu is verdeeld over 5 tabbladen: Interface, Snelkoppelingen, Gebaar, Toetsbindingen en Debug.

![](/images/interface_menu.webp)


::: tip
Deze pagina gaat over het menu Interface, niet over de interface zelf! De interface in het algemeen wordt beschreven in [Aan de slag](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interface {#interface}

Het tabblad Interface regelt de kleur, de grootte en de indeling van de gebruikersinterface van Nomad. Het heeft twee subtabbladen: `Uiterlijk` en `Indeling`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Kleuren {#presets}

![](/images/interface_presets.webp)

Het subtabblad `Uiterlijk` begint met een verzameling kleurvoorinstellingen voor de interface. Tik op een voorinstelling om haar toe te passen, en verfijn haar daarna met de opties hieronder.

#### Accent en Basis {#color-widgetcolor-base}
De hoofdkleuren van de interface: `Accent` voor geselecteerde knoppen en de balken van schuifregelaars, `Basis` voor de panelen.

#### Tekstdekking {#text-opacity}
Maak tekst en pictogrammen zachter ten opzichte van de panelen.

#### Schakelaars, Selectievakje, Tabbladen {#high-contrast-button}
De stijl van de schakelknoppen (`Zacht` of `Vol`), van de selectievakjes (`Omlijning`, `Accent` of `Vulling`) en van de tabbladen (`Onderstreping`, `Zacht` of `Vol`).

#### Gekleurde gereedschappen {#colored}
Geef de pictogrammen een kleur per categorie: alle maskergereedschappen zijn bijvoorbeeld bruin, de snijgereedschappen rood, de afvlakgereedschappen groen enzovoort.

#### Paneelschaduw {#material-color-preview}
Panelen werpen een schaduw, zodat ze loskomen van de scène.

#### Transparant paneel {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Staat dit aan, dan verschijnen er extra opties voor het uiterlijk van menu's en panelen in Nomad: `Paneeltint` bepaalt hun kleur, `Vervagingssterkte` hoeveel de scène erachter vervaagd wordt, en `Glas` voegt breking en glanslichten aan de randen toe, het best zichtbaar bij weinig vervaging.

::: tip
Op kleine apparaten kan het handig zijn de paneeltint bijna wit en transparant te maken, met een lage vervagingssterkte, zodat de menu's de scène niet verbergen.
:::

#### ![](/icons/reset.webp) Uiterlijk herstellen {#reset-style}
Zet alle opties voor het uiterlijk terug op hun standaardwaarden.

### ![](/icons/panel_detach.webp) Indeling {#layout}

Het subtabblad `Indeling` bepaalt waar alles staat en hoe groot het is.

#### Gereedschapskist {#toolbox}

Opties voor het gereedschapsmenu rechts in de interface van Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Formaat aanpassen {#ui-resize-corner}

Toon of verberg een greep in de onderhoek van de gereedschapskist om het formaat aan te passen.

##### Verborgen {#hidden}
Normaal wisselt het pictogram van de gereedschapskist in de bovenbalk tussen één lange kolom en een lijst van gereedschappen in meerdere kolommen. Met deze optie wissel je in plaats daarvan tussen de lijst in meerdere kolommen en een verborgen gereedschapskist.

##### Volgorde herstellen {#reset-order}
Zet de standaardgereedschappen in de gereedschapskist terug in hun standaardvolgorde. Aangepaste pictogrammen blijven in de gereedschapskist, aan het einde van de lijst.

#### Bovenbalk {#rows-auto-1}
`Responsief` bepaalt wat de bovenbalk doet als hij niet op het scherm past, vooral van belang op kleine schermen: `Meerdere lijnen` verdeelt de menu's over meerdere regels, `Scroll` houdt één regel aan waar je doorheen kunt scrollen.

#### Spiegel bovenste balk {#mirror-top-bar}
Draai de volgorde van de menu's in de bovenbalk om.

#### Spiegel zijbalken {#mirror-side-bars}
Verwissel de zijbalken, zodat de gereedschapskist links staat en de gereedschapsopties rechts.

#### Spiegel onderste balk {#mirror-bottom-bar}
Verplaats de onderste balk naar de rechterbenedenhoek en draai de volgorde van de knoppen om.

#### ![](/icons/move.webp) Paneel slepen {#drag-panel}
Een zwevend paneel verplaats je altijd door aan de balk te slepen; met deze optie kun je ook aan de inhoud ervan slepen. Op `Auto` verplaatst een vinger of stylus het paneel alleen als je meer horizontaal dan verticaal sleept, zodat je met een verticale sleepbeweging nog steeds door de inhoud scrolt. Zet het op `Ja` om ook met de muis te slepen, in elke richting.

#### ![](/icons/pencil.webp) Nomad-dialoog gebruiken {#use-nomad-dialog}
Toon het eigen tekstvenster van Nomad in plaats van dat van het systeem als je een naam of een waarde typt.

#### ![](/icons/stylus.webp) Zwevende punt {#hover-dot}
Toon een puntje in de interface als er een zwevende stylus wordt herkend.

#### ![](/icons/help.webp) Hulp pop-up bij zweven {#help-popup-on-hover}

Op apparaten die zweven ondersteunen bepaal je hiermee of de contexthulp van Nomad (het pictogram ![](/icons/help.webp)) verschijnt als je erboven zweeft, of alleen als je erop klikt.

#### Algemene schaal {#overall-scale}
Een vermenigvuldiger voor de grootte van alle interface-elementen.
#### Paneelbreedte {#panel-width}
De breedte van de menu's en panelen.
#### Lettertypeschaal {#font-scale}
Schaal de lettertypen.
#### Verticale afstand {#vertical-spacing}
De ruimte tussen de elementen in menu's en panelen.
#### Verticale afstand (links) {#vertical-spacing-left}
De ruimte tussen de elementen in de linkerwerkbalk.

#### Randafstanden {#edge-offset}
Pas deze waarden alleen aan als je moeite hebt met de knoppen aan de randen van het scherm. Zijn deze schuifregelaars uitgeschakeld, dan gebruikt Nomad de waarden voor het veilige gebied die het apparaat zelf doorgeeft.

::: tip
Zet je Nomad over naar een nieuw apparaat (bijvoorbeeld een iPhone 15 in plaats van een iPhone 12), zet de randopties dan terug op de standaardwaarden!
:::

#### ![](/icons/reset.webp) Indeling herstellen {#reset-layout}
Zet alle opties voor de indeling terug op hun standaardwaarden.

## ![](/icons/window.webp) Snelkoppelingen {#shortcuts}

In het tabblad Snelkoppelingen kies je welke snelknoppen rond de viewport verschijnen, en kun je je eigen zwevende werkbalken maken.

### Zijbalk {#side-bar}
De snelknoppen voor gereedschappen onderaan de linkerzijbalk: `Gladstrijken`, `Masker`, `Verbergen`, `Vlakkengroep` en `Gizmo`. Sleep ze om hun volgorde te veranderen.

### Onderste balk {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Tik op een snelkoppeling om haar aan de onderste balk toe te voegen, of om haar weg te halen. Deze staan standaard aan:
* `Ongedaan maken` - maak de vorige bewerking ongedaan
* `Opnieuw doen` - herstel de bewerking die je net ongedaan hebt gemaakt
* `Solo` - Verberg tijdelijk alle andere objecten, zodat alleen het geselecteerde zichtbaar is. Druk nog eens om alle objecten terug te halen.
* `X-Ray` - Maak tijdelijk alle andere objecten half doorzichtig, zodat alleen het geselecteerde massief blijft. Druk nog eens om de standaardmaterialen terug te zetten.
* `Voxel` - Remesh het huidige object met de laatst gebruikte voxelresolutie. Houd lang ingedrukt of veeg omhoog voor een resolutie-schuifregelaar en een schakelaar voor scherpe randen.
* `Raster` - Zet het raster in de weergave aan of uit. Houd lang ingedrukt of veeg omhoog om de kleur en de dekking van het raster te veranderen.
* `Draadmodel` - Zet een draadmodel over het object aan of uit. Houd lang ingedrukt of veeg omhoog om de kleur en de dekking van het draadmodel te veranderen.
* `Inspecteren` - bekijk eigenschappen van je mesh, zoals UV's, gebakken texturen en andere eigenschappen, over de achtergrond van Nomad heen.
* `Vlakkengroep` - Zet de weergave van de vlakkengroepen aan of uit; meer info bij [Gereedschappen->Vlakkengroep](tools.md#facegroup)

Andere veelgebruikte snelkoppelingen zijn ook beschikbaar: `Omlijning`, `Projectie` (perspectief of orthografisch), `MatCap`, `DynTopo`, en de knoppen `Subdivisie`, `Omgekeerd` en de niveauknoppen van [Multiresolutie](topology.md#multiresolution).

#### ![](/icons/more.webp) Toetsbindingen {#bindings-list}

Bijna elke functie van Nomad kun je aan de onderste balk toevoegen via de knop Toetsbindingen, die laat zien hoeveel snelkoppelingen de balk bevat. Klik je op de knop, dan verschijnt er een menu met toetsbindingen:

![](/images/interface_bindings_search.webp)

Je kunt per categorie zoeken via de pictogrammen bovenaan, of in het zoekveld functies op naam zoeken. Klik op een functie om haar aan de werkbalk toe te voegen. Klik nog eens om haar weg te halen.

#### ![](/icons/eye_open.webp) Zichtbaar {#order}

Toon of verberg de hele onderste balk.

#### ![](/icons/reset.webp) Herstellen {#reset}

Zet de onderste balk terug op de standaardinstellingen.

### Zwevende vensters {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Klik op de + om een zwevende werkbalk toe te voegen. Die is pas zichtbaar als je via de knop Toetsbindingen snelkoppelingen hebt toegevoegd; daarna kun je hem zichtbaar maken.

Je kunt veel werkbalken maken; elke werkbalk heeft een rij met deze opties:

* Sleep de greep links van een rij om de volgorde van de werkbalken te veranderen.
* `Naam` - De naam van de werkbalk.
* `Zichtbaar` - Toon of verberg de werkbalk.
* `Balk` - Toon een titelbalk op de werkbalk.
* `Verkleind` - Houd de werkbalk op het scherm als de interface verkleind is.
* `Toetsbindingen` - Open het venster met toetsbindingen om functies aan de werkbalk toe te voegen of eruit te halen.
* `Verwijderen` - Verwijder de werkbalk.


## ![](/icons/gesture.webp) Gebaar {#gesture}
Het menu Gebaar bepaalt hoe je Nomad bedient met je vinger, stylus, muis en trackpad.

![](/images/interface_gesture.webp)

### Gebaaropties {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad kan bewerkingen beperken tot bepaalde invoerapparaten. Zo kan slepen met een vinger bijvoorbeeld alleen de camera bewegen, terwijl slepen met een stylus alleen boetseert. Heb je een muis of trackpad, dan kun je ook die aan bepaalde bewerkingen toewijzen.

Elke rij is een bewerking: zet `Vinger`, `Stylus` en `Muis` aan of uit om te kiezen welke invoer haar mag uitvoeren.

* `Camera` - Beweeg de camera.
* `Bewerken van knooppunten` - Versleep de grepen op het canvas, bijvoorbeeld om een primitief, een curve, een repeater of een licht te bewerken.
* `Beeldhouwen` - Boetseer met de penselen. Gereedschappen met een eigen rij hieronder volgen die rij.
* `Selecteer object` - Tik op een object om het te selecteren.
* `Materiaal kiezer` - Houd lang ingedrukt op het canvas om de kleur of het materiaal onder de cursor over te nemen. Werkt alleen als schilderen aan staat voor het huidige penseel.
* `Bij tikken` - De tiksnelkoppelingen van gereedschappen zoals Masker, Verbergen en Vlakkengroep (zie hieronder).
* `Schilderen` - De gereedschappen Schilderen en Vlekken.
* `Masker` - Het Masker-gereedschap.
* `Vlak` - De gereedschappen Verbergen en Vlakkengroep.
* `Creëer` - De gereedschappen Buis, Draaibank en Invoegen.
* `Snij` - De gereedschappen Trimmen, Splitsen en Projecteren.
* `Selecteren` - De gereedschappen Selecteren en Meten.
* `Gizmo` - De gereedschappen Gizmo en Rooster.
* `Transformeren` - De gereedschappen Transformeren en Rangschikken.

::: tip
Een veelgebruikte instelling op een tablet: laat alleen de stylus boetseren en schilderen, en gebruik je vingers voor de camera. Zo laten je handpalm of een verdwaalde vinger nooit een streek op je model achter.
:::

### ![](/icons/tool_smooth.webp) Vinger verzacht altijd {#finger-always-smooths}
Staat dit aan, dan strijkt je vinger altijd glad zolang er een boetseergereedschap actief is, welk penseel het ook is. Zet je het aan, dan verdwijnt `Vinger` uit de rij `Beeldhouwen`, zodat de stylus boetseert en de vinger gladstrijkt.

### Streek buiten object {#allow-air-stroke}
Laat een streek ook beginnen als de cursor eerst naast de mesh terechtkomt. Kies de gereedschappen waarvoor het geldt: `Gereedschap` (alle andere penselen), `Gladstrijken`, `Masker` en `Verbergen`. Het werkt alleen voor invoer die wel kan boetseren maar niet de camera beweegt, dus deze knoppen zijn uitgeschakeld tot een van je invoerapparaten zo is ingesteld.

### ![](/icons/stroke.webp) Lijn-uitlijning {#stroke-snap}
Houd de aanwijzer aan het einde van een streek stil om hem om te zetten in een rechte lijn of een vloeiende curve. Blijf slepen om de aangepaste streek rond zijn beginpunt te draaien en te schalen.

`Vasthoudtijd` bepaalt hoe lang je stil moet houden voordat de streek wordt aangepast, of voordat een vorm overgaat naar bewerken.

### ![](/icons/stylus.webp) Extra invoersamples gebruiken {#use-extra-input-samples}
Gebruik de extra invoersamples die het apparaat doorgeeft. Schakel dit uit als je streken hoekig zijn of de druk niet goed werkt. Deze optie wordt niet getoond op iOS.

### ![](/icons/tool_mask.webp) Masker {#mask}

![](/images/interface_gesture_mask.webp)

`Snelle toetsen` - Zet de volgende tiksnelkoppelingen aan zonder dat je de maskerknop ingedrukt hoeft te houden. Je kunt dan:
* op de achtergrond tikken om het masker om te keren
* op een gemaskeerd gebied tikken om het masker te vervagen
* op een niet-gemaskeerd gebied tikken om het masker te verscherpen

#### Lang indrukken {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Lang indrukken met het Masker-gereedschap wisselt tussen het maskerpenseel en de lasso (SelMask):
* `Lang indrukken - Beeldhouwen` - Houd lang ingedrukt en blijf slepen: de streek wordt in de andere modus getekend, en aan het einde van de streek komt de vorige modus terug.
* `Lang indrukken - Wisselen` - Houd lang ingedrukt en laat los zonder te bewegen om tussen de twee te wisselen.

### ![](/icons/tool_smooth.webp) Gladstrijken {#smooth}
`Lang indrukken - Lasso` - Lang indrukken met het Gladstrijken-gereedschap schakelt over naar het Selecteren-gereedschap zolang de selectiestreek duurt.

### ![](/icons/tool_hide.webp) Verbergen {#hide}
![](/images/interface_gesture_hide.webp)

`Snelle toetsen` zet de volgende snelkoppelingen aan voor het Verbergen-gereedschap:
* Tik op een vlakkengroep om haar te verbergen
* Tik in een lege ruimte om de verborgen polygonen om te keren

### ![](/icons/finger3.webp) Drie vingers {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Ondersteunt je apparaat gebaren met 3 vingers, dan kun je daar snelkoppelingen aan toewijzen. 

In de optietabel kun je verticaal en horizontaal slepen aan aparte snelkoppelingen koppelen, of `Nee` kiezen om het uit te laten. Let op: kies je hetzelfde gebaar voor 2 opties, dan wordt er één uitgeschakeld en is de naam doorgestreept.

* `Draai verlichting` - Draai de omgeving, de lichten en de MatCap.
* `Gereedschapsradius` - Pas de straal van het gereedschap aan.
* `Tool Intensiteit` - Pas de intensiteit van het gereedschap aan. 

### ![](/icons/fingerprint.webp) Geschiedenis 2/3 {#history-23}
`Historiegebaren` - als dit aan staat, werken de volgende gebaren:
* Ongedaan maken - tik met 2 vingers
* Opnieuw doen - tik met 3 vingers

`Lang indrukken` - als dit aan staat, maak je snel achter elkaar ongedaan of opnieuw door 2 of 3 vingers op het scherm te houden.

### ![](/icons/mouse.webp) Muiswiel {#mouse-wheel}
`Snelheid (3d zoomen)` bepaalt hoe snel het wiel in de weergave zoomt, en `Snelheid (2d interface)` hoe snel het door de menu's en panelen scrolt. Met de minknop naast elke schuifregelaar draai je de richting om.

### ![](/icons/fingerprint.webp) Trackpad {#trackpad}
Op een Mac bepaal je met `Twee vingers` wat twee vingers op het trackpad doen. Knijpen zoomt altijd en draaien rolt altijd de weergave.
* `Uit` - Scrollen met twee vingers zoomt, zoals het muiswiel. De vingers worden niet afzonderlijk gelezen.
* `Verschuiven` - Twee vingers verschuiven de weergave, en als je er één optilt, draai je eromheen. Net als op een tablet.
* `Draaien` - Twee vingers draaien om de weergave heen, en als je er één optilt, verschuif je.

### Toegankelijkheid {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Hulpscherm` toont een zwevende werkbalk om slepen, knijpen, rollen en de camera te bedienen.

### Camera {#camera}
Een snelkoppeling naar het menu `Camera` (de camera-opties stonden vroeger hier, maar zijn naar het cameramenu verhuisd).

### Potlood dubbele tik -> Toetsbindingen {#pencil-tap}

Een snelkoppeling naar het menu `Toetsbindingen`, waar je instelt wat dubbeltikken met de Pencil doet. Buiten iOS staat er `Potloodknop → Toetsbindingen`, voor de knop van de stylus.

### Handpalm negeren {#palm-rejection}
Op telefoons en tablets worden aanrakingen genegeerd waarvan het contactoppervlak groter is dan `Maximale contactgrootte`, zoals je handpalm die op het scherm rust. Dit werkt misschien niet op elk apparaat; zet het dus uit als je moeite hebt met het bedienen van het canvas.


## ![](/icons/keyboard.webp) Toetsbindingen {#bindings}
In het menu Toetsbindingen stel je sneltoetsen voor het toetsenbord en voor knoppen in:

![](/images/interface_bindings.webp)
Bijna alle functies van Nomad kun je aan een sneltoets koppelen als je apparaat een toetsenbord heeft, of aan extra knoppen op je stylus, of zelfs aan een gamecontroller.

Om een toetsbinding te maken, klik je op het rechthoekje naast de functie en druk je op de toets of knop. 

Je vindt functies via de categoriepictogrammen bovenaan, of op naam via de zoekbalk. 

Je kunt afzonderlijke toetsbindingen uitschakelen met het selectievakje naast de naam. Houd het selectievakje lang ingedrukt en sleep om de volgorde van de lijst te veranderen.

Gebruiken twee ingeschakelde toetsbindingen dezelfde sneltoets, dan verschijnt er een pictogram ![](/icons/help.webp) naast, met de functies die met elkaar botsen.

### ![](/icons/more.webp) Contextmenu {#context-menu}
Het pictogram ![](/icons/more.webp) achter elke toetsbinding opent een contextmenu:

![](/images/interface_bindings_context.webp)

* `Klonen` - Kloon de toetsbinding, bijvoorbeeld om een functie een tweede sneltoets te geven.
* `Herstellen` - Zet de toetsbinding terug
* `Verwijderen` - Verwijder de toetsbinding. Alleen mogelijk als de functie meer dan één toetsbinding heeft.

Daaronder hebben sommige toetsbindingen extra opties:

* `Vaste toetsen` - Voor gereedschapssneltoetsen en de snelle sneltoetsen (Masker, Gladstrijken, Gizmo, Verbergen, Vlakkengroep, Toevoegen/Aftrekken): kies hoe een toetsdruk van gereedschap wisselt. `Auto` gebruikt de standaardinstelling uit de [Geavanceerde](#advanced) opties.
  * `Vasthouden` - Houd de toets ingedrukt om het gereedschap te gebruiken, en laat los om terug te gaan naar het vorige gereedschap.
  * `Wisselen` - Druk één keer om van gereedschap te wisselen.
  * `Kort indrukken` - Houd ingedrukt om het gereedschap tijdelijk te gebruiken, of druk kort om ernaar over te schakelen.
* `Terug bij loslaten` - Voor snelle sneltoetsen: kies of je bij het loslaten van een ingedrukte toets altijd teruggaat naar het vorige gereedschap, ook als dat gereedschap al actief was.
* `Vorig gereedschap wisselen` - Voor gereedschapssneltoetsen: druk je op de sneltoets van het huidige gereedschap, dan ga je terug naar het laatste gereedschap. Vereist `Vaste toetsen` op `Wisselen` of `Kort indrukken`.
* `Positie` - Voor sneltoetsen van zwevende vensters: open het venster waar het was (`Vorige behouden`) of onder de cursor (`Op cursor`).
* `Verplaatsen (bij loslaten)` / `Zoomen (bij loslaten)` - Voor de toetsbindingen voor zoomen en verschuiven van de camera: schakel over naar de andere als je de toets loslaat.
* Sleeprichting - Voor `Verlichting roteren`, `Gereedschapsradius` en `Gereedschapsintensiteit`: kies horizontaal of verticaal slepen.
* `Synchroniseren` - Voor functies die objecten toevoegen, klonen of instantiëren: kies of het resultaat gesynchroniseerd wordt. Standaard wordt de synchronisatiewaarde uit het menu Scène gebruikt.
* `Op achtergrond` - Voor de snelle sneltoetsen Gladstrijken en Masker: sleep op de achtergrond terwijl je de toets ingedrukt houdt om een lasso te tekenen: een selectielasso voor Gladstrijken, een maskerlasso voor Masker.
* `Camera forceren` - Voor de cameratoetsbindingen: beweeg de camera, ook als dezelfde sneltoets door een andere toetsbinding wordt gebruikt, meestal een gereedschapssneltoets of Toevoegen/Aftrekken.
* `Lineaire rolbeweging` - Voor de toetsbinding om te rollen: rol met een horizontale, verticale of diagonale sleepbeweging in plaats van rond het draaipunt te bewegen.

::: tip
Met `Kort indrukken` doet één toets allebei: houd hem ingedrukt om even glad te strijken of te maskeren en je bent terug bij je penseel zodra je loslaat, of tik erop om bij dat gereedschap te blijven.
:::

### ![](/icons/cog.webp) Geavanceerd {#advanced}
Onderaan het menu Toetsbindingen staat een tandwielmenu met geavanceerde opties:

![](/images/interface_bindings_advanced.webp)

* `Snelle sneltoetsen` - De standaardinstelling van `Vaste toetsen` en `Terug bij loslaten` voor de sneltoetsen Masker, Gladstrijken, Gizmo, Verbergen, Vlakkengroep en Toevoegen/Aftrekken.
* `Gereedschapssneltoetsen` - De standaardinstelling van `Vaste toetsen` en `Vorig gereedschap wisselen` voor de gereedschapssneltoetsen. Met `Vorig gereedschap wisselen` kun je met dezelfde sneltoets steeds tussen twee gereedschappen wisselen.
* `Sneltoetsvenster` - De modus van `Vaste toetsen` voor de sneltoetsen die de zwevende vensters tonen.
* `Draai zoom Y om` - Draai de verticale sleeprichting om bij het zoomen met een toetsbinding.
* `Lineaire rolbeweging` - Rol de weergave met een horizontale, verticale of diagonale sleepbeweging in plaats van rond het draaipunt te bewegen.
* `SpaceMouse` - Schakel ondersteuning voor de 3Dconnexion SpaceMouse in. Op sommige systemen verschijnen extra opties: wat hij beweegt (`Object`, `Camera`, `Eerste Persoon`, `Drone`), `Draaipunt automatisch bijwerken` om het draaipunt naar het oppervlak onder de cursor te verplaatsen zodra hij begint te bewegen, en zijn snelheden voor `Verplaatsen`, `Inzoomen` en `Rotatie`.
* `Dode zones (drift)` - Voor controllers van het type `Gamepad`, `Joystick` en `Knop`. Verhoog deze waarden als de camera beweegt terwijl je de controller niet aanraakt.
* `Gereedschapsradius` - Hoe slepen met de toetsbinding voor de straal het penseel van grootte verandert (`Cirkel`, `Midden` of `dx`), en daarna hoeveel de straaltoetsbindingen bij elke druk optellen (in pixels) of vermenigvuldigen.
* `Gereedschapsintensiteit` - Hoeveel de intensiteitstoetsbindingen bij elke druk optellen of vermenigvuldigen.
* `Camera - Snelheid` - De snelheid voor `Verplaatsen` en `Rotatie` van de toetsbindingen die de weergave verschuiven en draaien.
* `Toetsbindingen herstellen` - zet alle toetsbindingen terug op hun standaardwaarden.
* `Volgorde herstellen` - zet de standaardvolgorde van de lijst met toetsbindingen terug.


## iOS ⌘ Weergave van sneltoetsen {#ios-keyboard-shortcuts-display}

Op iOS-apparaten met een toetsenbord houd je de toets ⌘ (cmd) ingedrukt om een lijst met sneltoetsen te zien.

De toetsenbordondersteuning op Android is nog een beetje experimenteel.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debug {#debug}
In dit menu staan een aantal experimentele opties en debugopties. Laat de meeste op hun standaardwaarde staan, en verander ze alleen na contact met de ondersteuning van Nomad. Met de pictogrammen bovenaan spring je naar elk onderdeel.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normaliseer UV's` - Nomad normaliseert de UV's van de geselecteerde mesh binnen de [0-1]-tegel.

### ![](/icons/sun.webp) Shading {#render}
* `Brekingdiepte schrijven (achter)` - De achterkant van brekende meshes wordt in de dieptebuffer geschreven.
* `Hoekgewogen gladde normalen` - Een aanpassing aan de werking van vloeiende shading die in bepaalde gevallen vouwen kan voorkomen.

### ![](/icons/speed.webp) Doel FPS {#target-fps}
Staat dit uit, dan stemt Nomad het aantal beelden per seconde af op de verversingssnelheid van je scherm.

Staat het aan, dan stel je zelf in hoeveel beelden per seconde Nomad rendert.

### ![](/icons/window.webp) Interface {#debug-interface}
* `Gereedschapskist: alles tonen` - Nomad verbergt gereedschappen die niet relevant zijn voor de huidige selectie; zo zijn bijvoorbeeld alle boetseerpenselen verborgen op primitieven die nog niet voltooid zijn. Met deze optie worden uitgeschakelde gereedschappen gedimd in plaats van verborgen.

De andere interface-opties die hier vroeger stonden, vind je nu in het tabblad [Interface](#interface).

### ![](/icons/turntable.webp) Draaitafel {#gif-turntable}
Nomad kan een geanimeerde gif van een draaitafel exporteren. Door de beperkingen van het gif-formaat is de kwaliteit laag. Een schermopname is meestal een betere methode.

* `Duur` - hoeveel seconden de draaitafel duurt
* `Max frame sampling` - Veel van de renderingeffecten van hoge kwaliteit in Nomad ontstaan door meerdere beelden te combineren. Deze schuifregelaar bepaalt hoeveel beelden er worden gecombineerd, en het selectievakje zet het aan of uit.
* `Rotatiecentrum` - waar de camera omheen draait: `Huidige behouden` behoudt het huidige draaipunt, `(0, 0, 0)` gebruikt het midden van de wereld, `Scène` het midden van de scène.
* `Transparante achtergrond` - Gebruik de transparante optie voor gifs. Let op: gifs ondersteunen alleen 1-bit transparantie, dus de randen kunnen flink gekarteld zijn.
* `Export (GIF)` - start het exporteren van de gif.

### ![](/icons/postprocess.webp) Nabewerking {#post-process}
* `Filtering` - Debugoptie
* `Formaat` - Debugoptie
* `Buffers hergebruiken` - Debugoptie

### ![](/icons/ram.webp) Prestaties {#performance}
* `Multithreading: algemeen` - Debugoptie
* `Multithreading: beeldhouwen` - Debugoptie
* `Herhalingen als instanties tekenen` - Teken alle kopieën van een repeater in één draw call. Debugoptie.

### ![](/icons/star.webp) Functie {#feature}
* `nom: multires comprimeren` - Maak projecten en Nomad-exports die multiresolutie gebruiken kleiner. Deze bestanden kunnen niet worden geopend door oudere versies van Nomad. Deze optie verdwijnt in de toekomst misschien en staat dan standaard aan.
* `Quad-diagonaal omkeren (bij tikken)` -  Debugoptie

### ![](/icons/bug.webp) Debug {#dev}
* `Logboeken` - Open een logboekvenster
* `Gebeurtenissen loggen` - Schrijf je aanwijzergebeurtenissen (vinger, stylus, muis) naar het logboekvenster, om problemen met invoer te onderzoeken.
* `FPS` - voeg een teller voor beelden per seconde toe aan de statistieken in de viewport.
* `Appbeoordelingsvenster` - Debugoptie, op iOS en Android.

### ![](/icons/image.webp) Aangepaste iconen {#custom-icons}
Vervang de pictogrammen van Nomad door je eigen png-bestanden.
* `Iconen importeren` - Importeer png-bestanden naar `tmp_session/icons`. Elk bestand vervangt het basispictogram met dezelfde naam. Ze verdwijnen als Nomad opnieuw opstart.
* `Gereedschapsiconen exporteren` - Kopieer de basispictogrammen `tool_<tool>.png` naar `tmp_session/icons`, zonder iets te overschrijven. Je kunt ze daar bewerken en toepassen met `Iconen opnieuw laden`.
* `Iconen opnieuw laden` - Pas de pictogrammen uit `tmp_session/icons` toe.

### Quad-remesh {#quad-remesh}
De opties voor quad-remesh staan niet meer in dit menu: zie [Quad-remesh](topology.md#quad-remesh-instant) in het menu Topologie en het gereedschap [Quad Remesher](tools.md#quad-remesher).

### Maak winkelminiaturen {#make-store-thumbnails}
Render schermafbeeldingen in formaten die passen bij de App Store van iOS.
