# ![](/icons/cog.webp) Instellingen {#reset-to-default}

Het menu Instellingen bevat veel opties voor het uiterlijk en het gedrag van Nomad.

![](/images/settings_overview.webp)

Met de rij knoppen bovenaan het menu spring je meteen naar een sectie: `Cursor`, `Aanwijzer`, `Draad`, `Raster`, `Twee zijden`, `Omlijning`, `Markering`, `Navigator`, `Statistieken`, `Handvatten`, `Vorm`, `Repeaters` en `Multires`.

## Weergave-instellingen {#display-settings}
Deze sectie bevat snelkoppelingen naar de meeste instellingen verderop in dit menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Vloeiende shading {#smooth-shading}
Wisselt tussen vloeiende en facetshading. Bij facetshading krijgt elke polygoon zijn eigen shading, zodat je de onderliggende topologie ziet.
Het kan handig zijn om tijdens het sculpten facetshading te gebruiken en voor het renderen over te schakelen naar vloeiende shading.

Vloeiende shading uitzetten verbetert de prestaties een klein beetje.

### ![](/icons/outline.webp) Omlijning {#outline-quick}
Zet een omlijning rond je huidige selectie aan of uit.

Zo zie je welke mesh(es) geselecteerd zijn, ook als [Verduister niet-geselecteerde objecten](#darken-unselected-objects) uitstaat.

Voor de prestaties is [Verduister niet-geselecteerde objecten](#darken-unselected-objects) veel beter dan de omlijning.

### ![](/icons/grid.webp) Raster {#grid-quick}
Zet een raster op de achtergrond aan of uit, handig om de plaatsing en schaal van objecten te beoordelen.

### ![](/icons/culling.webp) Twee zijden {#two-sided-quick}
Zet de weergave van polygonen van twee kanten aan of uit. Elk vlak wijst in een bepaalde richting.
Vlakken die als *achterzijde* gelden, zijn de vlakken die van het standpunt van de camera "weg" wijzen.

De eenvoudige bol bij het opstarten heeft bijvoorbeeld vlakken die naar buiten wijzen.
Beweeg je de camera in de bol, dan zie je de achterzijde van die vlakken.

Meestal hoort de achterzijde van vlakken niet zichtbaar te zijn, dus door ze een kleur te geven spoor je mogelijke problemen of foute topologie op.

`Twee zijden` uitzetten kan de renderprestaties wat verbeteren.


### ![](/icons/wireframe.webp) Draadmodel {#wireframe-quick}
Zet een draadmodel over het model aan of uit.

Let op: het draadmodel aanzetten verlaagt de prestaties.

### ![](/icons/navigator.webp) Navigator {#snap-cube-quick}
Zet een hulpicoon in de hoek van de scène aan of uit. Handig om je in de ruimte te oriënteren en snel te wisselen tussen voor-, achter-, linker-, rechter-, boven- en onderaanzicht.

### ![](/icons/palette.webp) Toon schilderen {#show-painting}
Zet de weergave van het schilderwerk aan of uit. Staat het uit, dan worden objecten getoond met een wit, niet-metallisch materiaal met 25% ruwheid in plaats van hun schilderwerk.

### ![](/icons/tool_hide.webp) Gebruik Verberg {#use-hide}
Zet de verbergmodus aan of uit. Uitgezet is het verbergen er nog steeds, alleen gedeactiveerd. Deze knop is uitgeschakeld als je het gereedschap Verbergen gebruikt.

### ![](/icons/shield.webp) Toon masker {#show-mask}
Zet de maskermodus aan of uit. Uitgezet is het masker er nog steeds, alleen gedeactiveerd. Druk nogmaals op deze knop om het weer te activeren.

Wil je het masker verbergen terwijl het actief blijft, gebruik dan de maskerkleur hieronder en zet die op wit. Vergeet niet om hem daarna weer grijs te maken!

Let op: deze knop is uitgeschakeld als je een maskergereedschap gebruikt.

### ![](/icons/shield.webp) Masker → Ondoorzichtig {#mask-opaque}
`Masker → Ondoorzichtig` negeert transparante vertices voor het gemaskeerde masker. Dit geldt alleen voor vertex- en textuurdekking: vlakken die met "verbergen" verborgen zijn, blijven verborgen. Het is alleen beschikbaar zolang `Toon masker` aanstaat.

### ![](/icons/bang.webp) Markering {#highlight-quick}
Zet het oplichten van de selectie aan of uit. Bij het selecteren licht het geselecteerde object 500 milliseconden op. De kleur en duur van het oplichten stel je hieronder in.

### ![](/icons/list.webp) Statistieken {#stats-quick}
Zet de statustekst in de 3d-viewport aan of uit. Die toont informatie over het systeemgeheugen, het totale aantal vertices in de scène en het aantal vertices in de huidige selectie.

----- 

### ![](/icons/cube.webp) Verduister niet-geselecteerde objecten {#darken-unselected-objects}
Objecten die niet geselecteerd zijn worden donkerder, zodat de huidige selectie opvalt.

### ![](/icons/shield.webp) Masker {#mask}
De kleur voor het masker, standaard middengrijs, vermenigvuldigd met de kleur van je object. Zet hem op wit om het masker onzichtbaar te maken, maar vergeet niet om hem daarna weer grijs te maken!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Cirkel {#show-circle-while-sculpting}
Wanneer de cirkel van de penseelradius wordt getoond:

* `Auto` - toont de cirkel, maar verbergt hem tijdens het sculpten.
* `Nee` - toont de cirkel nooit.
* `Ja` - toont de cirkel altijd, ook tijdens het sculpten.

### Toon kleine stip {#show-small-dot}
Toont een stip in het midden van de penseelstreek tijdens het sculpten, of wanneer het draaipunt van de camera verandert.

### Toon touwstabilisator {#show-rope-stabilizer}
Tekent een lijn die de lengte van het touw aangeeft wanneer [Trage touwstabilisator](stroke.md#lazy-rope-stabilizer) actief is in de streekinstellingen.

### Rolhint weergeven {#show-roll-hint}
Toont de hulplijn voor de rolrichting terwijl je een toetsbinding voor rollen gebruikt.

### ![](/icons/radius.webp) Grootte {#dot-size}
De grootte van de kleine stip.

### Kleuren {#cursor-colors}
De cursor verandert van kleur afhankelijk van wat je doet: `Beeldhouwen`, `Achtergrond` (boven de achtergrond zweven), `Masker`, `Gladstrijken`, `Camera` en `Straal`. Elke kleur kun je hier aanpassen.

## ![](/icons/cursor.webp) Aanwijzer {#indicator}
![](/images/settings_indicator.webp)

Toont visuele aanwijzer(s) voor tutorials en schermopnames. Zet het op `Ja` om het aan te zetten (op iOS is er ook een optie `Auto`).

Met de knoppen `Vinger`, `Stylus` en `Muis` wordt een icoon getoond wanneer dat type invoer wordt herkend.

### Kleur {#indicator-color}
De kleur van de aanwijzer.

### Grootte/Icoon/Cirkel {#indicator-shape}
Regelaars voor de grootte van de aanwijzer en de dekking van het icoon en de cirkel in de aanwijzer.

## ![](/icons/wireframe.webp) Draadmodel {#wireframe}
![](/images/settings_wireframe.webp)
Zet het draadmodel aan.

### Doel {#target}
Bepaalt of niet-geselecteerde objecten een draadmodel tonen, of alleen geselecteerde objecten, of alle objecten.

### Verbergen {#hide}
Bepaalt of het draadmodel ook getoond wordt voor verborgen polygonen.

### Multiresolutie: Alleen niveau 0 {#multiresolution-level-0-only}
Bij multiresolutie is het draadmodel van niveau 0 donkerder en worden hogere niveaus steeds lichter. Met deze optie wordt alleen het draadmodel van niveau 0 getoond.

### Kleur {#wireframe-color}
Stelt de kleur en dekking van het draadmodel in.

## ![](/icons/grid.webp) Raster {#grid}
![](/images/settings_grid.webp)
Zet het raster aan.

### Snappen {#snap}
Met deze opties snappen de punten van gereedschappen op basis van curves en vormen (`Draaibank`, `Buis`, polygoon- en padvormen...) terwijl je ze tekent:

* `Naar raster snappen` - snapt naar het raster.
* `Uitlijnen op punten (uitgelijnde weergave)` - snapt naar bestaande punten in de buurt wanneer de camera op een as is uitgelijnd.
* `Uitlijnen op punten (vrije weergave)` - snapt naar bestaande punten in de buurt wanneer de camera niet is uitgelijnd.

### Kleur {#grid-color}
Stelt de kleur en dekking van het raster in. Deze opties verschijnen wanneer het raster zichtbaar is.

`Vignet` laat het raster naar de randen toe vervagen. `Snapdrempel voor verdelingen` bepaalt, in pixels, hoe dicht de rasterlijnen op het scherm mogen komen voordat het raster naar een ander onderverdelingsniveau overschakelt.

## ![](/icons/culling.webp)Twee zijden {#two-sided}
Maakt polygoonvlakken van beide kanten zichtbaar.

### Achterzijde kleur {#backface-color}
`Gekleurde achterzijde` geeft de achterzijden een tint, en `Achterzijde kleur` bepaalt die tint.

## ![](/icons/outline.webp)Omlijning {#outline}
Zet een omlijning rond de geselecteerde objecten aan.

### Omlijningskleur, Dikte {#outline-color-thickness}
Stelt de kleur en de `Dikte` van de omlijning in.


## ![](/icons/bang.webp) Markering {#highlight}
Laat de selectie kort oplichten wanneer die verandert.
### Kleur, Duur {#color-duration}
Stelt de kleur en de duur van het oplichten in milliseconden in.

## ![](/icons/navigator.webp) Navigator {#snap-cube}
![](/images/settings_snapcube.webp)

Toont een hulpicoon in de hoek van de scène, handig om snel te wisselen tussen voor-, achter-, linker-, rechter-, boven- en onderaanzicht. Tik op de zijden ervan om tussen de orthografische aanzichten te wisselen.

### Vorm {#shape}
Kies tussen een bol, een kubus of een gnomon als vorm voor de navigator.

### Uitlijning beperken {#restrict-alignment}
Lijnt de aanzichten uit op de wereldassen. Staat dit aan, dan zijn alleen de 6 hoofdaanzichten mogelijk. Op `Auto` geldt deze beperking alleen wanneer de camera in de modus `Draaischijf` staat.

### Grootte {#size}
Stelt de grootte van de navigator in.

### Draai 180° {#flip-180}
Is de weergave uitgelijnd, dan draait een tik op het midden van de navigator de weergave 180 graden. Sta je bijvoorbeeld op het vooraanzicht, dan draait een tik op de navigator naar het achteraanzicht.

### Randen en hoeken {#edges-corners}
Voegt aanzichten toe op de randen en hoeken (de amberkleurige zones). Niet beschikbaar met de gnomonvorm.

### Slepen als draaischijf {#turntable-drag}
Slepen aan de navigator draait de camera zonder te rollen, en blijft even hangen op elk aanzicht. Zet het uit om de navigator te slepen met de rotatie `Trackball`. In beide gevallen blijft het slepen horizontaal of verticaal. Met een camera in `Draaischijf` sleept de navigator altijd op deze manier.

### Positie {#snap-position}
Bepaalt in welke hoek de navigator staat.


## ![](/icons/list.webp) Statistieken {#stats}
![](/images/settings_stats.webp)

Toont informatie over het systeemgeheugen, het totale aantal vertices in de scène en het aantal vertices in de huidige selectie.

### Positie {#stats-position}
Bepaalt in welke hoek de statistieken staan.

## ![](/icons/edit_radius.webp) Handvat {#handle}
Instellingen voor de handvatten die je in de viewport versleept, zoals de gizmo.

### Numerieke invoer {#gizmo-input}
Maakt numerieke invoer mogelijk wanneer je op een van de bedieningselementen van de gizmo tikt.

### Verberg bij interactie {#hide-on-interaction}
Laat de gizmo vervagen terwijl je ermee werkt, zodat hij niet in de weg zit.

### ![](/icons/opacity.webp) Dekking {#handle-opacity}
De dekking van de handvatten.

## ![](/icons/shape_lasso.webp) Vorm {#shape-settings}
Hoe de vormen die je met vormstreken tekent (lasso, rechthoek, curve...) er op het scherm uitzien.

### ![](/icons/opacity.webp) Vulling, Omtrek {#shape-fill-outline}
De dekking van de binnenkant van de vorm en van de lijn eromheen.

### Kleuren {#shape-colors}
De kleur van de vorm voor elk soort gereedschap: `Masker`, `Verbergen`, `Vlakkengroep` en `Trimmen`.

## ![](/icons/array.webp) Repeaters {#primitive-repeaters}
Limieten voor de kopieën die [repeaters](scene#repeaters) maken (array, radiaal, curve, oppervlak). Ze houden Nomad vlot wanneer een repeater uit de hand loopt.

### ![](/icons/cube.webp) Max. kopieën {#repeater-max-copies}
Het maximale aantal kopieën dat één repeater maakt. Nomad heeft moeite met veel objecten, ongeacht hun grootte.

### ![](/icons/cube.webp) Kopieën in de scène {#repeater-scene-copies}
Het kopieënbudget voor de hele scène. Een low-poly kopie kost weinig geometrie maar blijft een volwaardig object, dus kleine kopieën lopen als eerste tegen deze limiet aan.

### ![](/icons/triangle.webp) Max. vlakken {#repeater-max-faces}
Het vlakkenbudget voor alle kopieën in de scène. Wordt het overschreden, dan verliezen de zwaarste objecten als eerste kopieën.

## ![](/icons/multires.webp) Multiresolutie {#multires}
### Maximaal aantal vertices {#multires-lowres-count}
Een drempel die voorkomt dat een multires-subdivisie boven dit aantal vertices uitkomt, wat Nomad waarschijnlijk zou laten crashen: Nomad controleert het beschikbare geheugen niet voordat het onderverdeelt. De standaard is 10 miljoen.
### Drempel lage resolutie {#multires-lowres-threshold}
Terwijl je de camera beweegt, kan een lagere resolutie van de mesh worden getoond. Verhoog deze waarde als je een hogere resolutie van de mesh wilt zien.

## Instellingen {#advanced}
### ![](/icons/reset.webp) Herstel naar standaard {#reset}
Zet alle voorkeursinstellingen van de app terug op hun standaardwaarden.

Sommige bronnen worden apart opgeslagen en worden NIET hersteld: projecten, toetsbindingen, gereedschapspresets, HDR-omgevingen, MatCaps, alpha's, penseeltexturen en referentieafbeeldingen. Alles wat met het project wordt opgeslagen, zoals belichting, nabewerking of camera-aanzichten, blijft ook behouden.
