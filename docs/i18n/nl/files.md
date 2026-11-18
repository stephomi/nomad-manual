# ![](/icons/open.webp) Bestanden {#files}

In het menu Bestanden sla je Nomad-projecten op en open je ze, importeer en exporteer je 3d-modellen, exporteer je gerenderde afbeeldingen en koppel je Nomad aan andere apps. Het heeft drie tabbladen: `Bestanden`, `Render` en `Koppeling`.

![](/images/file_menu.webp)

## Project {#project}
![](/images/file_project.webp)

De miniatuur bovenaan toont het huidige project, met daarnaast de bestandsgrootte, de automatische opslag en de opgeslagen geschiedenis. Tik op de miniatuur om een kleine browser met je projecten te openen, en tik dan op een project voor een menu waarmee je het kunt openen, toevoegen, overschrijven, klonen, hernoemen of verwijderen.

Heeft het project wijzigingen die nog niet zijn opgeslagen, dan staat `Niet-opgeslagen wijzigingen!` onder de miniatuur.

### Bereik {#scope}
Op desktop kies je waar je projecten worden opgeslagen:
* `Intern` - De standaard, net als op mobiel. Projecten worden alleen in de hoofdmap van Nomad opgeslagen.
* `Oorspronkelijk bestand` - Als je een project van buiten de Nomad-map opent, overschrijft opslaan het originele bestand. Automatisch opslaan werkt niet voor deze externe projecten.

### ![](/icons/nomad.webp) Preset {#preset}
Een verzameling demo's en onderdelen voor personages. Selecteer er een en selecteer hem nog eens om te kiezen tussen `Openen` en `Toevoegen aan scène`. Vanuit deze browser kun je ook gratis modellen van Poly Haven downloaden.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Geschiedenis... {#history}
Snel naar de geschiedenisopties van het project, zoals `Geschiedenis opslaan`, dat je geschiedenis voor ongedaan maken bewaart wanneer het project wordt opgeslagen. Een groene badge op de knop laat zien dat de geschiedenis met het project wordt opgeslagen. Zie [Geschiedenis](history.md#save-history) voor meer details.

### ![](/icons/save.webp) Opslaan {#save}
Slaat het Nomad-project op. Is het project nog nooit opgeslagen, dan word je om een naam gevraagd.

### ![](/icons/save_as.webp) Opslaan als... {#save-as}
Slaat het project onder een nieuwe naam op, als nieuw project.

### ![](/icons/save_as.webp) Overschrijven... {#overwrite}
Opent de projectbrowser om de huidige scène over een ander project heen op te slaan. Zet `Alleen geselecteerde objecten opnemen` aan om alleen de geselecteerde objecten op te slaan in plaats van de hele scène. De browser heeft ook een knop `Opslaan als...` om in plaats daarvan als nieuw project op te slaan.

### ![](/icons/pencil.webp) Hernoem {#rename}
Toont een tekstvak om het huidige project een andere naam te geven.

### ![](/icons/open.webp) Openen... {#open}
Opent de projectbrowser om een project te openen.

### ![](/icons/add_file.webp) Toevoegen aan scène... {#add}
Opent de projectbrowser; als je een project selecteert, wordt de inhoud ervan samengevoegd met de huidige scène.

### ![](/icons/trash.webp) Verwijderen... {#delete}
Opent de projectbrowser; de projecten die je selecteert, worden van het bestandssysteem verwijderd.

### ![](/icons/new_file.webp) Nieuw {#new}
Begint een nieuw project. Zijn er niet-opgeslagen wijzigingen, dan word je om bevestiging gevraagd. In die bevestiging kun je de instellingen voor `Achtergrond`, `Omgeving`, `MatCap` en `X-Ray` `Behouden` of `Herstellen`, en kiezen of het nieuwe project `Geschiedenis opslaan` gebruikt.

### ![](/icons/autosave.webp) Automatisch opslaan... {#auto-save}
Menu met de opties voor automatisch opslaan. Zet `Automatisch opslaan` aan om je project op vaste tijden in een apart bestand op te slaan. De badge op de knop laat zien of het aan staat.

Nomad slaat niet op de achtergrond op, omdat 3d-bestanden behoorlijk groot kunnen zijn en dat flinke vertraging kan geven terwijl je aan het sculpten bent.

Daarnaast wordt de scène meestal eerst gecomprimeerd voordat hij wordt opgeslagen, om geheugenproblemen te voorkomen.
Ook dat comprimeren en decomprimeren maakt het opslaan trager.

### Opslaginterval {#timer-pop-up}
Hoeveel minuten Nomad wacht tussen twee automatische opslagen.

### Aftellen tonen {#popup-timeout}
Toont een aftelling vóór elke automatische opslag, zodat je die kunt annuleren als je ergens middenin zit. Staat dit uit, dan slaat Nomad op zodra je stopt met sculpten.

### ![](/icons/trash.webp) Automatisch opslaan verwijderen {#discard-autosave}
Bestaat er een automatisch opgeslagen bestand voor een project, dan wordt dat automatisch geladen in plaats van het oorspronkelijke project. Heb je dat niet nodig, dan verwijdert deze knop de automatische opslag. Bij het laden krijg je dan de laatste handmatige opslag van het project.

### ![](/icons/open.webp) Verouderde opslag openen {#open-outdated-save}
Heeft een project zowel een automatische als een handmatige opslag, dan opent deze knop de oudste van de twee (`Verouderde automatische opslag openen` of `Verouderde handmatige opslag openen`), met de datum erbij. Handig als de laatste opslag niet de versie is die je wilde.

### ![](/icons/storage.webp) Recent verwijderd... {#recently-deleted}
Nomad bewaart de gegevens van projecten die uit de projectenmap zijn verdwenen, en van bestanden die door een import zijn vervangen, een aantal dagen voordat ze definitief worden verwijderd. Bestanden waarvan de import is mislukt, blijven staan tot je ze zelf verwijdert. Deze lijst toont ze met hun grootte en datum, zodat je ze een voor een kunt verwijderen of allemaal tegelijk met `Alles verwijderen`.

## Importeren {#import}

### ![](/icons/add_file.webp) Importeren {#import-button}
Om 3d-bestanden te importeren die geen Nomad-project zijn.

Als je een extern scènebestand in Nomad importeert, kun je het *toevoegen* of er een *nieuw* project mee beginnen.

Bij toevoegen komen de objecten gewoon in de huidige scène erbij.
Kies je `Nieuw`, dan wordt er een nieuw Nomad-project gemaakt met de nieuwe objecten erin.

Het importvenster toont elk bestand dat je hebt gekozen, met zijn eigen importopties. Ook afbeeldingen kun je zo importeren: kies voor elke afbeelding of het een `HDRI`, een `MatCap`, een `Referentiebeeld`, een `Alpha`, `Texturen` of een `VDM` wordt.

Nomad kan deze formaten importeren:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), op platforms die het ondersteunen

### ![](/icons/cog.webp) Instellingen {#advanced}
De knop `Instellingen...` naast de projectminiatuur toont de belangrijkste importopties. Deze instellingen worden niet bewaard, en het importvenster toont de opties die gelden voor de bestanden die je importeert.

### Alle formaten {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Behoud topologie {#keep-topology}
Standaard probeert Nomad bij het laden probleemgeometrie te herstellen. Zet je dit aan, dan ordent Nomad vertices en vlakken niet opnieuw, voegt het geen duplicaten samen en verwijdert het geen ongebruikte vertices.

::: warning
Met `Behoud topologie` worden bij bewerkingen zoals Booleaans, Samenvoegen, Decimeren of Manifold dubbele vertices mogelijk niet samengevoegd.
:::

#### ![](/icons/image.webp) Sla texturen over {#skip-textures}
Laadt de texturen die in het bestand zijn ingesloten niet, bij formaten die dat ondersteunen, zoals glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) UI-instellingen laden {#keep-gui-settings}
Laadt bij het openen of importeren van een projectbestand alle interface-instellingen die erin zijn opgeslagen.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Splits OBJ per groepen {#split-obj-by-groups}
Splitst OBJ-groepen op in aparte objecten.

#### ![](/icons/vertex.webp) Dubbele posities samenvoegen {#merge-duplicate-positions}
Voegt vertices samen die op dezelfde positie liggen.

#### ![](/icons/uv.webp) Voeg dubbele UV's samen {#merge-duplicate-uvs}
Voegt textuurcoördinaten samen die dezelfde UV delen.

#### ![](/icons/paint.webp) Kleurruimte {#color-space}
Bepaalt hoe de kleuren uit het bestand worden gelezen: `Auto`, `Lineair` of `sRGB`. Kloppen de kleuren niet, probeer dan een andere optie.

#### ![](/icons/image.webp) Formaat {#normal-format}
Het formaat van de normal maps in de texturen: `Auto`, `OpenGL (+Y)` of `DirectX (-Y)`. Lijken de details van de normal map omgekeerd, probeer dan de andere.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Kleurruimte {#color-space-ply}
Bepaalt hoe de kleuren uit het bestand worden gelezen: `Auto`, `Lineair` of `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Voeg dubbele UV's samen {#merge-duplicate-uvs-fbx}
Voegt textuurcoördinaten samen die dezelfde UV delen.

#### ![](/icons/paint.webp) Kleurruimte {#color-space-fbx}
Bepaalt hoe de kleuren uit het bestand worden gelezen: `Auto`, `Lineair` of `sRGB`.

#### ![](/icons/image.webp) Formaat {#normal-format-fbx}
Het formaat van de normal maps in de texturen: `Auto`, `OpenGL (+Y)` of `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Kleurruimte {#color-space-usd}
Bepaalt hoe de kleuren uit het bestand worden gelezen: `Auto`, `Lineair` of `sRGB`.

#### ![](/icons/image.webp) Formaat {#normal-format-usd}
Het formaat van de normal maps in de texturen: `Auto`, `OpenGL (+Y)` of `DirectX (-Y)`.



## Exporteren {#export}
Slaat op in een 3d-geometrieformaat dat je in andere software kunt gebruiken.

![](/images/file_export.webp)

Elk bestandsformaat ondersteunt andere functies, dus welke opties beschikbaar zijn, hangt af van het gekozen bestandstype.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertexkleuren](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex-PBR](#pbr-paint)        | ✅     | Nomad ✅<br>Overige ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quads                           | ✅     | Nomad ✅<br>Overige ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Lagen](#layers)                | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objecten                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Vlakkengroep                    | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hiërarchie                      | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lichten                         | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Texturen                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitieven, nabewerking, enz.  | ✅     | Nomad ✅<br>Overige ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Exportknop {#export-button}
Tik hierop om de geometrie met de gekozen instellingen te exporteren. De knop toont het gekozen formaat en een schatting van de bestandsgrootte. Op Android stuurt een knop `Delen` ernaast het bestand direct naar een andere app.

### Bestandsformaat {#file-format}
Kies het exportformaat: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` of `USD`. NOMAD is het eigen formaat van Nomad; het laadt niet in andere software en is dus vooral bedoeld om weer in Nomad te importeren.

### Inclusief {#allvisibleselected}
Kies welke objecten worden geëxporteerd: `Alles`, `Zichtbaar` of `Geselecteerd`. Het getal naast elke optie laat zien hoeveel objecten er worden geëxporteerd.

### Eén bestand per object {#one-file-per-object}
Exporteert elk object naar een eigen bestand. Het getal laat zien hoeveel bestanden er worden geschreven.

### Type {#type}
Schrijft de export meerdere bestanden weg (één bestand per object, of OBJ met texturen), dan sla je ze op in een `Map` of een `Zip`. Sommige apps (Google Drive, One Drive, enz.) kunnen geen mappen importeren; gebruik dan Zip.

### Geschiedenis insluiten {#embed-history}
Alleen NOMAD. Neemt de ongedaan-maakgeschiedenis op in het bestand; die wordt hersteld als je het bestand in Nomad opent. Het bestand wordt er groter van, en de hele scène moet als één bestand worden geëxporteerd.

### Bronnen insluiten {#embed-assets}
Alleen NOMAD. Neemt je eigen matcaps, omgevingen en lettertypen op in het bestand. Ingebouwde bronnen worden niet ingesloten.

### Vertexkleuren {#vertex-colors}
Exporteert vertexkleuren als het bestandsformaat dat ondersteunt. Sommige 3d-software kan ze lezen, maar niet alle.

Voor OBJ kun je kiezen:
* `Geen` - Geen kleuren.
* `RGB` - De kleuren worden na de vertices toegevoegd.
* `MRGB (ZBrush)` - Een andere manier om kleur te coderen, die ook maskergegevens ondersteunt.

### Kleurruimte {#color-space-export}
Alleen OBJ, met `RGB`-vertexkleuren. Schrijft de kleuren als `Lineair` of `sRGB`.

### PBR verf {#pbr-paint}
Exporteert het schilderwerk voor ruwheid, metaalheid en masker. Andere software negeert deze gegevens mogelijk.
PBR-vertexkleuren worden geëxporteerd als secundaire vertexkleurattributen.
De kanalen zijn als volgt samengevoegd:

|           | Kanaal   |
| :-------: | :------: |
| Ruwheid   | R        |
| Metaalheid | G       |
| Masker    | B        |


### Lagen {#layers}
Lagen worden ondersteund via glTF-morph targets. Dat is officieel onderdeel van glTF, dus het zou ook in andere software moeten werken.
Nomad exporteert ook kleur, ruwheid en metaalheid per laag, maar andere software negeert dat.

### Laag schilderen {#layer-painting}
Exporteert het schilderwerk van lagen; andere software negeert dit meestal.

### Vlakkengroep {#face-group}
Exporteert vlakkengroepen; dat kan soms problemen geven in andere software.

### Objecten Schrijven {#write-objects}
Alleen OBJ. Houdt objecten gescheiden. Zet het uit om alles als één object te exporteren, bijvoorbeeld om de functie 'Mesh ID / Polygroup' van Substance Painter te gebruiken.

### Normalen {#normals}
Exporteert de normaalinformatie. Let op: Nomad berekent bij het importeren van andere bestandsformaten altijd zijn eigen normalen.

### Tangenten {#tangents}
Exporteert de tangentinformatie, die wordt gebruikt als het model normal maps heeft.

### Texturen {#textures}
Zijn er texturen aan het materiaal toegevoegd, dan worden ze geëxporteerd. Let op: dit bakt geen texturen; dat doe je met de bakopties onder topologie.

### Formaat {#fbx-format}
Alleen FBX. `Binair` is kleiner maar werkt misschien niet in elke applicatie, `ASCII` is een tekstbestand.

### Gecomprimeerd {#compressed}
Alleen FBX. Maakt het bestand kleiner, maar exporteren en importeren worden trager.

### Preset {#usd-preset}
Alleen USD. Kies de app waarvoor je exporteert: `OpenUSD`, `Apple`, `Procreate` of `Zbrush`. Sommige opties zijn alleen bij bepaalde presets beschikbaar.

### Instantie {#instance}
Alleen USD. Exporteert geïnstantieerde objecten als instanties, in plaats van hun geometrie te dupliceren.

### Scheeftrekken toestaan {#allow-skew}
Alleen USD. Staat scheeftrekken toe in de transformatiematrices. Staat dit uit, dan splitst Nomad scheefgetrokken transformaties op in aparte schaal- en rotatietransformaties.

### Repeater {#repeater}
Alleen USD. Exporteert de kopieën die repeaters maken als instanties.

### Kopieën samenvoegen {#join-copies}
Elk object en zijn repeaterkopieën worden samen één object.

::: tip Tip: ruwheid en metaalheid in Blender importeren

Blender kan glTF/glb importeren, maar begrijpt de vertexattributen voor metaalheid en ruwheid niet vanzelf. Om ze te gebruiken maak je in de materiaaleditor een Vertex Color-node aan en zet je de eigenschap ervan op het volgende kleurattribuut (meestal Col.001). Verbind die met een 'Separate XYZ'-node, stuur X naar Roughness en Y naar Metallic.

Deze video laat zien hoe dat gaat:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: ondersteuning van USD-functies

USD is een complex formaat: de specificatie ondersteunt veel functies, maar niet alle 3d-software ondersteunt ze allemaal. OSX/iOS ondersteunen bijvoorbeeld geen vertexkleuren. De presetmodi in de USD-exporter doen een zo goed mogelijke gok naar compatibiliteit met OpenUSD, Apple, Procreate en Zbrush.

::: 

## ![](/icons/screen.webp) Render {#render}

Exporteert een afbeelding die alle instellingen van het project combineert (lichten, materialen, nabewerking enz.).

![](/images/file_render.webp)
### ![](/icons/preview.webp) Voorbeeld {#preview}

De knop `Voorbeeld` naast de menutitel maakt de interface doorzichtig, zodat je de kadrering van het eindresultaat beter kunt beoordelen.

### ![](/icons/home.webp) Focus {#focus}
Kadreert de scène of de selectie zodat die in het renderformaat past. Tik nog eens om tussen de twee te wisselen.

### ![](/icons/map.webp) Hoogtekaart {#heightmap}
Rendert de scène als een grijswaarden-hoogtekaart, gezien vanuit de camera, waarbij de dichtstbijzijnde delen het helderst zijn. Zet je dit aan, dan schakelt het formaat naar `Vierkant` en wordt de selectie gekadreerd. Met een balkje in de viewport stel je de `Focus` van de overgang bij.

Staat `Hoogtekaart` aan, dan verschijnt naast de exportknop een knop `Opslaan als alfa`, waarmee je de render als nieuwe penseel-alpha opslaat in plaats van een bestand te exporteren.

### ![](/icons/opacity.webp) Transparante achtergrond {#transparent-background}
Geeft de render een alfakanaal, handig om de render in 2d-programma's met andere afbeeldingen te combineren. Let op: gedeeltelijke transparantie wordt niet ondersteund.

### ![](/icons/sliders.webp) Interface tonen {#show-interface}
Neemt de interface van Nomad op in de render.

### Definitieve grootte {#final-size}
De resolutie van de render: `Scherm`, `720`, `1080`, `4096`, `Vierkant` of `Aangepast`.

Als het menu Bestanden actief is, toont de viewport een gestippeld kader om het rendergebied aan te geven als dat niet overeenkomt met de schermresolutie.

### Breedte / Hoogte {#render-ratio}
Met `Aangepast` stel je de breedte en hoogte van de afbeelding in. De koppelknop tussen de twee schuiven behoudt de verhouding als je er een van verandert. Met `Vierkant` kun je alleen de breedte instellen.

### ![](/icons/export.webp) Exporteren → PNG {#export-png}
Tik op deze knop om het renderen te starten. Als het klaar is, kies je hoe je de afbeelding opslaat of deelt. Bij heel grote formaten wordt eerst om bevestiging gevraagd: sla je project vooraf op, voor het geval je apparaat zonder geheugen komt te zitten.

## ![](/icons/network.webp) Koppeling {#link}

Verbind Nomad met een ander apparaat of een andere app om objecten te verzenden en te ontvangen, of om je bewerkingen live te synchroniseren. Eén apparaat host de sessie, de andere nemen eraan deel.

### GoZ inschakelen {#enable-goz}
Alleen op desktop. Wisselt meshes uit met ZBrush op deze computer. `Verzenden` importeert ze in ZBrush, `Ophalen` importeert vanuit de ZBrush die draait: `Selectie` neemt de actieve subtool, `Scène` neemt alle subtools. Je kunt ook op elk moment in ZBrush op GoZ drukken.

### Modus {#link-mode}
* `Uit` - Geen koppeling.
* `Host` - Dit apparaat host de sessie en wacht tot anderen deelnemen.
* `Deelnemen` - Zoekt naar apparaten in de buurt; tik dan op de naam van de host om deel te nemen.

Om twee keer Nomad te koppelen, kies je `Host` op het ene apparaat en `Deelnemen` op de andere. Om met Blender te koppelen moet Nomad de host zijn: de helpknop naast de titel `Koppeling` laat zien hoe je de extensie Nomad Blender Link installeert.

### ![](/icons/network.webp) Netwerkpoort {#network-port}
De netwerkpoort die de koppeling gebruikt. Verander hem alleen als een andere app hem al gebruikt.

### Verzenden / Ophalen {#send-get}
Zodra je verbonden bent, kun je je `Selectie` of de hele `Scène` `Verzenden` naar het andere apparaat, of ze ervan `Ophalen`. `Vervangen` verwijdert de huidige scène en haalt dan de scène van het andere apparaat op.

### ![](/icons/link.webp) Live synchronisatie {#live-sync}
Stuurt je bewerkingen tijdens het werken door naar het andere apparaat. `Werkweergave` synchroniseert ook de camera. `Scènebewerkingen` bepaalt welk apparaat de bewerkingen verstuurt: `Auto` geeft de richting aan de laatste activiteit. Kies daarna wat er wordt gesynchroniseerd: `Objecten en geometrie`, `Materialen`, `Lichten`, `Camera’s` en, als de andere kant het ondersteunt, `Shading` en `Nabewerking`.

::: tip
Bestaande objecten moeten eerst één keer worden verzonden met `Verzenden` of opgehaald met `Ophalen`, zodat ze gekoppeld zijn voordat live synchronisatie ze kan bijwerken.
:::
