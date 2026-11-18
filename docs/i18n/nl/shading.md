# ![](/icons/sun.webp) Shading {#shading}

In dit menu regel je de shadingmodi van Nomad, de eigenschappen van de verlichting, de omgeving en de matcap, en de mist.

![](/images/shading_overview.webp)



Je kunt kiezen uit verschillende rendermodi:

| Modus                       | Betekenis                  | Beschrijving                                                    |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Verlicht (PBR)](#pbr)      | Physically Based Rendering | Lichten, schaduwen, omgeving, en geschilderde metaalheid/ruwheid |
| [MatCap](#matcap)           | Material Capture           | Snelle modus om te sculpten, met minder gpu-/cpu-gebruik dan PBR |
| [Onbelicht](#unlit)         | Oppervlaktekleur           | Alleen de oppervlaktekleur, zonder shading of verlichting       |
| [Object-ID](#object-id)     | Object-ID                  | Een willekeurige kleur per object, handig voor schilderprogramma's. |
| [Instantie-ID](#instance-id) | Instantie-ID              | Een willekeurige kleur per instantie, handig om gedeelde meshes te herkennen |

Wil je meer weten over metaalheid en ruwheid, kijk dan bij het onderdeel [Vertex schilderen](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Vlakkengroep {#face-group}
Toont de kleuren van de vlakkengroepen over het model. Vlakkengroepen zijn gekleurde selecties van polygonen die je kunt maken met de tool [Vlakkengroep](tools#facegroup), en die bij de meeste primitieven automatisch worden aangemaakt.

Sommige tools filteren automatisch op vlakkengroep als vlakkengroepen zichtbaar zijn.

### ![](/icons/palette.webp) Toon schilderen {#show-paint}
Nomad kan kleur, ruwheid en metaalheid opslaan in de vertices van je sculpt. Met dit vinkje zet je de weergave van deze eigenschappen overal tegelijk aan of uit.

Let op: heb je zowel vertex-eigenschappen als texturen, en staan ze allebei aan, dan worden de waarden met elkaar vermenigvuldigd.

### ![](/icons/shield.webp) Toon masker {#show-mask}
Zet de grijze maskerlaag van de [maskertools](tools#mask) aan of uit. Staat dit uit, dan is het masker ook uitgeschakeld. Handig om snel iets aan te passen zonder masker: zet het daarna weer aan en je masker is er nog.

### ![](/icons/tool_hide.webp) Gebruik Verberg {#use-hide}

Zet verborgen vlakken aan of uit. Let op: dit werkt alleen als je NIET in de verbergtool zit!

### ![](/icons/image.webp) Gebruik texturen {#use-textures}

In Nomad kun je via het menu [Materiaal](material) texturen aan objecten toewijzen. Zijn er texturen toegewezen, dan zet je ze met dit vinkje overal tegelijk aan of uit.

Je kunt in Nomad zelf geen texturen maken of bewerken, maar texturen uit geïmporteerde bestanden werken wel. Dekkingstexturen werken in Verlicht, MatCap en Onbelicht, normal maps in Verlicht en MatCap, kleur in Verlicht en Onbelicht, en lichtgevend, ruwheid en metaalheid alleen in Verlicht. De knop is grijs als de scène geen textuur heeft.

### PBR en lichten: overzicht {#pbr}
Deze handleiding gaat niet diep in op Physically Based Rendering.

Belangrijk om te onthouden is dat verlichting en materiaal volledig gescheiden zijn.
Je kunt dus de kleur, ruwheid en metaalheid van je object schilderen terwijl de verlichting los daarvan wordt geregeld.
Zo kun je je object eerst beschilderen en later de verlichting bijstellen, zonder dat het totaalbeeld van je model verloren gaat.

Lichten, de omgeving en de mist zijn alleen beschikbaar in de [PBR-modus](#pbr).
Om prestatieredenen kun je maximaal 4 lichten gebruiken op mobiel en 6 op desktop.

::: tip
Je kunt een glTF-bestand met meer lichten laden, en Nomad houdt ze dan allemaal.
Dat presteert alleen niet per se goed.
:::

::: tip
Je kunt veel lichten nabootsen door objecten onbelicht/lichtgevend te maken en daarna globale verlichting aan te zetten in het menu [Nabewerking](postprocess).
:::

### Soorten lichten {#light-types-overview}

Dit zijn de soorten lichten die op dit moment worden ondersteund:

| Modus                       | Beschrijving                                            | Kan schaduw werpen |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Directioneel](#directional) | Zonlicht van oneindig ver weg                          | Ja               |
| [Omgeving](#env-light)      | Een ver licht dat wordt afgestemd op de HDR van de omgeving | Ja           |
| [Spot](#spot)               | Kegelvormige lichten                                    | Ja               |
| [Punt](#point)              | Puntlicht dat in alle richtingen straalt                | Ja               |

#### ![](/icons/sun.webp) Directioneel {#directional}
Straalt licht uit van oneindig ver weg, met een gelijkmatige intensiteit.
Zijn 3d-positie in de scène doet er niet toe, alleen zijn oriëntatie.

Je kunt dit licht aan de camera vastmaken, zodat de verlichting altijd hetzelfde blijft.
Zo kun je er bijvoorbeeld een strijklicht (rim light) mee maken: een sterk licht dat van achter je model richting de camera schijnt en de achterkant van je model altijd belicht.

#### ![](/icons/panorama.webp) Omgevingslicht {#env-light}
Een [HDR-omgeving](#environment) werkt goed voor zachte algemene verlichting, maar zit er een sterk, scherp licht in de HDR, dan is de schaduw die het geeft erg zacht en vaak helemaal niet zichtbaar. Een directioneel licht samen met de HDR-omgeving kan helpen, maar het is lastig om ze goed op elkaar uit te lijnen.

Dit licht doet dat werk voor je. Het draait automatisch mee naar het helderste deel van de HDR, en daarna regel je de intensiteit en de hoek (de zachtheid van de schaduw) los van elkaar.

#### ![](/icons/spotlight.webp) Spot {#spot}
Een spotlicht straalt in één richting, begrensd door een kegelvorm.

#### ![](/icons/light.webp) Punt {#point}
Een puntlicht straalt in alle richtingen en kan ook schaduw werpen.

#### Schaduwen {#shadows}
Elk licht kan schaduw werpen, en in zijn [instellingen](#light-extra-controls) kies je hoe die wordt berekend. Zie je artefacten in de schaduw, dan kunnen de schuiven voor `Tolerantie` daar helpen.

De kwaliteit van de schaduwen hangt af van de grootte van de objecten ten opzichte van de hele scène.
Heb je een groot object in je scène dat geen schaduw hoeft te werpen (bijvoorbeeld een groot vlak), zet het werpen van schaduw dan uit in de [materiaalinstellingen](material.md#casts-shadows) ervan.

## ![](/icons/sun.webp) Lichten {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Vinkje Lichten {#lights-checkbox}

Zet alle directe lichten in de scène aan of uit.



### Licht toevoegen {#add-light}

Voegt een licht toe aan de scène, tot 4 lichten op mobiel en 6 op desktop. Zodra je een licht toevoegt, verschijnt de lichtenlijst met knoppen, en komt er bovenaan de viewport een lichtwerkbalk bij.

![](/images/shading_lights_icons.webp)

* De tekst toont de naam van het licht en de helderheid. Tik erop om het licht te selecteren.
* Het oogje zet de zichtbaarheid aan of uit.
* Met het potloodje geef je het licht een andere naam.
* Het prullenbakje verwijdert een licht.
* Het kopieericoon dupliceert een licht.
* Het icoon met de 3 puntjes opent een volledige lichteditor. De meeste functies daarvan vind je ook in de werkbalk die in de viewport verschijnt.

Je kunt een licht in de lijst ook verslepen om de volgorde te veranderen.

### ![](/icons/spotlight.webp)  Iconen {#icons}

Zet de weergave van de lichticonen in de viewport aan of uit.

### Lichtwerkbalk {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Deze werkbalk verschijnt bovenaan de viewport als er een licht is geselecteerd.

* `Zichtbaar` zet het licht aan of uit.
* Directioneel/Omgeving/Spot/Punt verandert het soort licht. Tik om erdoor te bladeren, of houd lang ingedrukt voor een menu.
* Intensiteit bepaalt de sterkte van het licht. De waarde kan boven 1,0 gaan voor heel felle lichten, handig samen met globale verlichting in Nabewerking.
* Tik op het kleurvlak om een kleurkiezer te openen. Nomad biedt verschillende manieren om een kleur te kiezen. Met de Kelvin-regeling kies je op een natuurlijke manier tussen warm en koel licht.
* Schaduw zet schaduwen aan of uit.
* Hoek (_directioneel en omgeving_) of Grootte (_spot en punt_) bepaalt de breedte van een licht. Bredere lichten geven zachtere schaduwen, zachter licht en een zachtere glans op objecten.
* Koppeling (_alleen directioneel_), Conushoek en Zachtheid (_alleen spot_) worden hieronder bij de [lichteditor](#light-extra-controls) beschreven.
* ... toont `Klonen`, `Centreren` en `Verwijderen`, samen met de schaduwinstellingen.

### Extra lichtinstellingen {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Het icoon met de 3 puntjes bij een licht in de lijst opent de volledige editor ervan. Sommige opties gelden alleen voor bepaalde soorten lichten.

* Met `Directioneel/Omgeving/Spot/Punt` verander je het soort licht.
* Tik op het `kleurvlak` om een kleurkiezer te openen.
* `Intensiteit` bepaalt de sterkte van het licht.
* `Koppeling` (_alleen directioneel_) koppelt het licht aan de wereld (`Vast`) of aan de camera (`Camera`). Gebruik je bijvoorbeeld een directioneel licht achter je personage als strijklicht, dan blijft het licht met koppeling aan de camera altijd achter het personage, hoe je de camera ook draait.
* `Zachtheid` (_alleen spot_) bepaalt hoe scherp de rand van de lichtkegel is. 0 is een heel scherpe rand. 1 is heel zacht, met een overgang naar het midden van de lichtkegel. In de viewport kun je met het kleine blauwe puntje op de kegel de zachtheid direct instellen.
* `Conushoek` (_alleen spot_) bepaalt hoe wijd het spotlicht uitwaaiert. Een kleine hoek geeft een heel smalle lichtbundel, 170 een heel brede. In de viewport kun je met het oranje puntje de conushoek direct instellen.
* `Hoek` (_alleen directioneel en omgeving_) is de schijnbare grootte van het licht: zie het als hoe groot de zon aan de hemel lijkt. Grotere hoeken geven zachtere schaduwen en bredere glansplekken.
* `Grootte` (_alleen spot en punt_) is de breedte van het licht. Grotere lichten geven zachtere schaduwen.
* `Schaduw` zet de schaduwen van het huidige licht aan of uit.
* Het schaduwtype bepaalt hoe schaduwen worden berekend. Een `Schaduwmap` rendert de scène vanuit het licht, en geeft dus ook schaduw van geometrie die de camera niet ziet. `Schermruimte` gebruikt alleen wat al op het scherm zichtbaar is: dat is lichter, maar experimenteel. Over het algemeen is de schaduwmap betrouwbaarder.
* `Tolerantie` (_alleen schermruimte_): zie je artefacten in de schaduw (schaduwen lijken het oppervlak niet te raken, of er zit ruis of een patroon in), dan kan het bijstellen van de tolerantie helpen.
* `Contact` voegt preciezere schaduwen toe over korte afstanden, waar objecten elkaar raken. Met `Auto` krijgt alleen het sterkste licht in de scène contactschaduwen; `Nee` en `Ja` zetten ze geforceerd uit of aan voor dit licht. De schuif `Tolerantie` ervan werkt net als die hierboven.

De knop `...` van de werkbalk in de viewport bevat dezelfde schaduwinstellingen, plus:

* `Klonen` dupliceert het licht.
* `Centreren` zet het licht voor de camera, met behoud van zijn oriëntatie.
* `Verwijderen` verwijdert het licht.


## ![](/icons/panorama.webp) Omgeving {#environment}

![](/images/shading_environment.webp)

In het echt komt licht uit alle richtingen: het blauw van de lucht, het groen van het gras, het rood van een gebouw. Al dat licht uit de 'omgeving' kun je nabootsen met een omgevingsmap.

Met het vinkje naast de titel zet je de omgevingsverlichting aan of uit.

Nomad heeft een aantal voorbeeldomgevingen voor binnen en buiten, met verschillende tinten en helderheden. Probeer er een paar uit om te zien welke de meeste details van je sculpt laat zien.

Tik op de afbeelding om de beschikbare omgevingsmaps te zien. Kies in dat venster `Importeer...` om je eigen te laden. Gebruik het liefst High Dynamic Range-afbeeldingen (HDR) in latlong- of equirectangulair formaat, als .hdr- of .exr-bestand. De browser kan omgevingen ook direct downloaden van [Poly Haven](https://polyhaven.com/hdris), dat een mooie verzameling gratis omgevingsmaps heeft.

### Belichting {#env-exposure}
Past de helderheid van de omgevingsmap aan. Samen met gewone lichten zijn de maps vaak te fel; de belichting omlaag zetten helpt dan om alles in balans te brengen, vooral samen met globale verlichting in de instellingen voor [Nabewerking](postprocess).

### Rotatie {#env-rotation}

Omdat omgevingsmaps licht uit alle richtingen vastleggen, kun je ze draaien zodat de reflecties en de algehele verlichting goed bij je sculpt passen. Je kunt de omgeving ook draaien door met 3 vingers horizontaal over de viewport te slepen.

### Gehecht aan camera {#env-attached}
Maakt de omgeving vast aan de camera.

Zo blijft de verlichting altijd hetzelfde, wat handig kan zijn tijdens het sculpten.

### Vervaging (achtergrond) {#env-background-blur}
Deze schuif verschijnt alleen als de [achtergrond](background.md) op de omgeving staat. Hij vervaagt de omgevingsafbeelding achter je model, zonder de verlichting te veranderen.


## ![](/icons/fog.webp) Mist {#fog}

Mist geeft je scène atmosferische diepte en maakt lichtbundels zichtbaar. Zet hem aan met het vinkje naast de titel. Net als lichten en de omgeving is mist alleen beschikbaar in de modus [Verlicht (PBR)](#pbr).

::: tip Sterkere lichtbundels
Zet de `Omgeving` van de mist lager en gebruik een fel spot- of puntlicht. Verhoog de `Dichtheid` tot de mist duidelijk zichtbaar is. Voor zichtbare bundels in dunnere mist zet je de `Verstrooiingsrichting` op een hoge positieve waarde en richt je de camera naar het licht.
:::

### Kleur {#fog-color}
De kleur van de mist en van het licht dat hij verstrooit.

### Dichtheid {#fog-density}
Hoe snel de mist dikker wordt met de afstand.

### Maximale dekking {#fog-opacity}
Beperkt hoeveel de mist de scène kan bedekken, ook bij een hoge dichtheid.

### Verstrooiingsrichting {#fog-scattering}
De richting waarin de mist het licht verstrooit (ook wel anisotropie genoemd). Positieve waarden maken de mist helderder als je naar een licht kijkt, negatieve waarden als je ervan wegkijkt, en bij nul wordt het licht gelijkmatig in alle richtingen verstrooid.

### ![](/icons/panorama.webp) Omgeving {#fog-environment}
Hoeveel de [omgeving](#environment) de mist verlicht. Deze optie is grijs als de omgeving uit staat.

### Ruis {#fog-noise}
Mengt ruis door de mist om hem in plukken op te breken, zonder de algehele dichtheid te veranderen. Staat de ruis boven 0, dan bepaalt een schuif `Grootte` hoe groot het patroon is.

### Vorm {#fog-shape}
Waar de mist de scène vult:

* `Gelijkmatig` - vult de hele scène.
* `Verticaal` - houdt de mist binnen een verticale band met zachte randen. De schuiven `Onder` en `Boven` bepalen de hoogte van de onder- en bovenrand, en met hun oogknop zie je de band in de viewport terwijl je ze bijstelt.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Zoals de naam al zegt (MATerial CAPture), legt een matcap zowel de verlichting als de materiaalinformatie vast in één afbeelding.
Omdat het materiaal al in de matcap zit, worden de schilderkanalen voor ruwheid en metaalheid genegeerd.
De verfkleur wordt met de matcap vermenigvuldigd: heb je een zwarte of grijze matcap, dan wordt het met witte verf niet lichter.

Kunstenaars gebruiken deze modus graag om te sculpten, omdat ze zich dan volledig op de vorm en de geometrie kunnen richten.

Tik op de bol om een afbeeldingenbrowser te openen. Je kunt ook je eigen matcap toevoegen: eigenlijk elke foto, render of zelfs schildering van een bol die strak tot een vierkant is bijgesneden, is bruikbaar. Online vind je veel matcapbibliotheken; een handige bron is de [nidorx matcap library](https://github.com/nidorx/matcaps).

### Gebruik globale MatCap {#matcap-global}

Meestal gebruiken kunstenaars één matcap voor de hele sculpt, maar zet je deze schakelaar uit, dan kan het geselecteerde object een eigen matcap krijgen. Artistiek kun je daar opvallende resultaten mee halen.

::: tip
Zet deze optie uit en gebruik een afbeelding van een oogbol voor de ogen van je personages!
:::

### Rotatie {#matcap-rotation}
Een matcap is een speciaal soort omgevingsmap, en net als een omgevingsmap kun je hem draaien. Dat kan ook op elk moment in de viewport door met 3 vingers naar links en rechts te slepen.

De slotknop naast de schuif vergrendelt de rotatie, zodat een sleepbeweging met 3 vingers de matcap niet per ongeluk draait.



## ![](/icons/circle_fill.webp) Onbelicht {#unlit}

Deze modus toont alleen de oppervlaktekleur. Handig om te controleren of de oppervlaktekleur van je objecten is wat je verwacht, zonder afleiding van lichten, schaduwen, reflecties of transparantie.

Je kunt deze modus ook gebruiken voor niet-fotorealistische renders, met een vlakke, cartoonachtige look.

## ![](/icons/cube.webp) Object-ID {#object-id}

Alle verlichting en oppervlakte-informatie wordt genegeerd, en elk object krijgt een eigen egale kleur. Render je dit naast een PBR-render, dan kun je in een tekenprogramma op kleur selecteren en zo kleurcorrecties op specifieke objecten doen.

Deze kleuren verschijnen ook in de [boomweergave van het menu Scène](scene#tree-view).

### ID willekeurig maken {#object-random}

Maakt een nieuwe set willekeurige kleuren.

## ![](/icons/link.webp) Instantie-ID {#instance-id}

Hetzelfde als Object-ID, maar instanties krijgen dezelfde kleur.

### ID willekeurig maken {#instance-random}

Maakt een nieuwe set willekeurige kleuren.
