# ![](/icons/sun.webp) Shading {#shading}

Dit menu bepaalt de schaduw-/weergavemodi die door Nomad worden gebruikt, de licht­eigenschappen en de eigenschappen van omgevingslicht/matcap.

![](/images/shading_overview.webp)



Je kunt kiezen uit verschillende render­modi:

| Mode                        | Betekenis                  | Beschrijving                                                   |
| :-------------------------: | :------------------------: | :------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | Schilderen met metalness/roughness                            |
| [Matcap](#matcap)           | Material Capture           | Te gebruiken tijdens het beeldhouwen met minder gpu/cpu‑gebruik dan PBR |
| [Unlit](#unlit)             | Oppervlakkleur             | Alleen oppervlakkleur, zonder shading of belichting           |
| [Object Id](#object-id)      | Object‑ID                  | Een willekeurige kleur per object, handig voor paint‑apps     |
| [Instance Id](#instance-id)  | Instance‑ID                | Een willekeurige kleur per instantie, handig om gedeelde meshes te herkennen |

Als je meer wilt leren over metalness en roughness, zie de sectie [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Vlakkengroep {#face-group}
Overlay van facegroup‑kleuren. Facegroups zijn gekleurde selecties van polygonen die kunnen worden gemaakt met de tool [Face group](tools#facegroup), en automatisch worden aangemaakt bij de meeste primitieve vormen.

Sommige tools filteren automatisch op facegroups wanneer facegroups zichtbaar zijn.

### Verf tonen {#show-paint}
Nomad kan kleur, roughness en metalness opslaan in de vertices van je sculpt. Je kunt de weergave van deze eigenschappen globaal aan‑ of uitzetten met dit selectievakje.

Let op: als je zowel vertex‑eigenschappen als textures hebt, en beide zijn ingeschakeld, dan worden de waarden met elkaar vermenigvuldigd.

### Masker tonen {#show-mask}
Schakel de grijswaardenmasker‑overlay van de [mask tools](tools#mask) in of uit. Wanneer dit is uitgeschakeld, is het masker ook uitgeschakeld; dit is handig om snel wijzigingen te maken zonder masker, waarna je het masker weer kunt inschakelen zonder het kwijt te raken.

### Verbergen gebruiken {#use-hide}

Schakel verborgen vlakken in of uit. Let op: dit werkt alleen als je NIET in de hide‑tool zit!

### Texturen gebruiken {#use-textures}

Nomad maakt het mogelijk om textures toe te wijzen aan objecten via het [material](material)‑menu. Als er textures zijn toegewezen, kunnen ze globaal worden in‑ of uitgeschakeld met dit selectievakje.







### PBR- en lichtoverzicht {#pbr}
Deze handleiding gaat niet in op de details van Physically Based Rendering.

Belangrijk om te onthouden is dat belichting en materiaal volledig gescheiden zijn.
Dat betekent dat je de kleur, roughness en metalness van je object kunt schilderen terwijl de belichting onafhankelijk wordt geregeld.
Zo kun je je object schilderen en later de belichting aanpassen zonder de algehele look van je model te verstoren.

Lichten zijn alleen beschikbaar in de [PBR‑modus](#pbr).
Om prestatie­redenen ben je beperkt tot slechts 4 lichten.

::: tip
Je kunt een glTF‑bestand laden met meer dan 4 lichten en Nomad zal ze allemaal behouden.
Het zal echter niet per se goed presteren.
:::

::: tip
Je kunt veel lichten faken door objecten unlit/emissive te maken en vervolgens global illumination in te schakelen in het [post process](postprocess)‑menu.
:::

### Overzicht van lichttypen {#light-types-overview}

Dit zijn de lichttypes die momenteel worden ondersteund:

| Mode                        | Beschrijving                                           | Kan schaduwen werpen                                  |
| :-------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Zonlicht op oneindige afstand                         | ja                                                     |
| [Environment](#environment) | Een ver licht dat overeenkomt met de omgeving‑HDR     | ja                                                     |
| [Spot](#spot)               | Kegelvormige lichten                                  | Ja                                                     |
| [Point](#point)             | Omni‑directioneel puntlicht                           | Ja, maar alleen via minder robuuste screen‑space‑schaduwen |

#### Richtinggevend {#directional}
Dit licht straalt vanaf oneindige afstand met een uniforme intensiteit.
De 3D‑positie in de scène maakt niet uit, alleen de oriëntatie.

Je kunt dit licht aan de camera koppelen, zodat de belichting consistent blijft.  
Je kunt het bijvoorbeeld gebruiken als rim light (een sterk licht dat van achter je model komt en naar de camera wijst) dat altijd de achterkant van je model belicht.

#### Omgevingslicht {#env-light}
Een [environment‑HDR](#environment) werkt goed voor algemene zachte belichting, maar als er een sterke, scherpe lichtbron in de HDR zichtbaar is, zal de schaduw daarvan erg zacht zijn en vaak nauwelijks zichtbaar. Een directioneel licht in combinatie met de environment‑HDR kan helpen, maar het kan lastig zijn om ze goed uit te lijnen.

Dit licht doet dat werk voor je. Het licht wordt automatisch geroteerd zodat het uitgelijnd is met het helderste deel van de HDR; vervolgens kun je de intensiteit en hoek (schaduw­zachtheid) afzonderlijk regelen. 

#### Spot {#spot}
Een spot‑light straalt licht in één richting uit, begrensd door een kegelvorm.

#### Punt {#point}
Een point‑light straalt licht in alle richtingen uit.  
Op dit moment ondersteunt point‑light geen schaduwen.

#### Schaduwen {#shadows}
De optie `normal bias` kan worden gebruikt om veelvoorkomende schaduw­artefacten (acne/peter‑panning) te verminderen.

De kwaliteit van de schaduwen hangt af van de grootte van de objecten ten opzichte van de hele scène.  
Als je een groot object in je scène hebt dat geen schaduwen hoeft te werpen (bijvoorbeeld een groot vlak), zorg er dan voor dat je het werpen van schaduwen uitschakelt in de [materiaalinstellingen](material.md#cast-shadows).

## Lichten {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Lichten-checkbox {#lights-checkbox}

Schakel alle directe lichten in de scène in of uit.



### Licht toevoegen {#add-light}

Voeg een licht toe aan de scène, tot een maximum van 4. Wanneer een licht wordt toegevoegd, verschijnt de lichtlijst met knoppen en wordt er een licht‑toolbar bovenaan de viewport toegevoegd.

![](/images/shading_lights_icons.webp)

* De tekst toont de naam van het licht en de helderheid.
* Het oog‑icoon schakelt de zichtbaarheid.
* Het potlood‑icoon laat je het licht hernoemen.
* Het prullenbak‑icoon verwijdert een licht.
* Het kopie‑icoon dupliceert een licht. 
* Het icoon met 3 puntjes opent een volledige lichteditor. Het meeste van deze functionaliteit is ook beschikbaar via de toolbar die in de viewport verschijnt. 

### ![](/icons/spotlight.webp)  Pictogrammen {#icons}

Schakel de weergave van lichticonen in de viewport in of uit.

### Lichtwerkbalk {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Deze toolbar verschijnt bovenaan de viewport wanneer een licht is geselecteerd.

* Show schakelt de zichtbaarheid van het licht.
* Directional/Environment/Spot/Point verandert het lichttype. Tik om te cyclen, of houd ingedrukt voor een menu.
* Intensity regelt de lichtsterkte; de waarde kan boven 1,0 gaan voor zeer intense lichten, handig in combinatie met Global Illumination in Post Process.
* De kleurstaal opent bij aanklikken een kleurkiezer. Nomad biedt verschillende manieren om kleur te kiezen. Kelvin‑regeling biedt een natuurlijke manier om warm/koud licht te selecteren.
* Shadow schakelt schaduwen.
* Size bepaalt de breedte van een licht. Brede lichten werpen zachte schaduwen, zachte belichting en een zachtere highlight op objecten.
* ... opent extra instellingen.

### Extra lichtbediening {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Let op: sommige opties zijn specifiek voor bepaalde lichttypes.

* `Clone` dupliceert het licht.
* `Recenter` verplaatst het licht terug naar de oorsprong.
* `Delete` verwijdert het licht.
* `Directional/Environment/Spot/Point` laten je het lichttype wijzigen.
* De `colour swatch` opent bij aanklikken een kleurkiezer. 
* `Intensity` regelt de lichtsterkte.
* `Attachment` (_alleen directional_) bepaalt of het licht aan de wereld of aan de camera wordt gekoppeld. Als je bijvoorbeeld een directioneel licht achter je personage gebruikt als rim light, dan zal bij attachment op camera het licht altijd achter het personage blijven wanneer je de camera draait.
* `Angle` (_alleen directional en environment_) is de schijnbare grootte van het licht; denk aan hoe groot de zon aan de hemel lijkt. Grotere hoeken geven zachtere schaduwen en bredere highlights.
* `Softness` (_alleen spotlight_) regelt de scherpte van de rand van de spotlichtkegel. 0 is een zeer scherpe rand. 1 is zeer zacht, met een verloop naar het midden van de lichtkegel. In de viewport kan het kleine blauwe punt op de spotlichtkegel worden gebruikt om softness interactief in te stellen.
* `Cone angle` (_alleen spotlight_) regelt de spreidingshoek van het spotlicht. Een kleine hoek is een zeer smalle lichtbundel, 170 is een zeer brede lichtspreiding. In de viewport kan het oranje punt worden gebruikt om de cone angle interactief in te stellen.
* `Shadow` schakelt schaduwen voor het huidige licht.
* `Shadow map` en `screenspace` zijn verschillende manieren om schaduwen te berekenen; doorgaans is shadow map betrouwbaarder.
* `Contact` bepaalt hoe schaduwen worden berekend. Schaduwen zijn een lastig probleem in computergraphics en kunnen artefacten veroorzaken in de render. Nauwkeurigere schaduwen kunnen worden gekozen voor het belangrijkste licht in een scène; met deze instelling bepaal je of Nomad dat licht automatisch kiest of dat de gebruiker het selecteert.
* `Tolerance` kan helpen schaduw­artefacten op te lossen (bijvoorbeeld wanneer schaduwen geen contact lijken te maken met oppervlakken, of wanneer er ruis en patronen in schaduwen zichtbaar zijn) door de tolerantie aan te passen.


## Omgeving {#environment}

![](/images/shading_environment.webp)

Licht in de echte wereld komt uit alle richtingen; het blauw van de lucht, het groen van het gras, het rood van een gebouw – al dat licht uit de ‘omgeving’ kan worden gesimuleerd met een environment map. 

Nomad wordt geleverd met verschillende voorbeeld‑environment maps voor binnen‑ en buitenlocaties, met verschillende tinten en helderheids­niveaus. Probeer verschillende maps om te zien welke het meeste detail in je sculpts naar voren brengt.

Tik op de afbeelding om de beschikbare environment maps te zien. Kies in dat dialoogvenster ‘Import...’ om je eigen map te laden. Het is het beste om High Dynamic Range (HDR)‑afbeeldingen te gebruiken in latlong‑ of equirectangular‑formaat, als .hdr‑ of .exr‑bestand. [www.polyhaven.com](https://polyhaven.com/hdris) heeft een goede collectie gratis environment maps; meestal zijn de 1k‑hdr‑maps een goede maat en kwaliteit.

### Belichting {#env-exposure}
Pas de helderheid van de environment map aan. Vaak kunnen de maps te helder zijn in combinatie met gewone lichten; het verlagen van de exposure kan helpen om dit in balans te brengen, vooral in combinatie met Global Illumination in de [Post Process](postprocess)‑instellingen.

### Rotatie {#env-rotation}

Omdat environment maps licht uit alle richtingen vastleggen, kun je ze roteren om de reflecties en algemene belichting goed te laten samenwerken met je sculpt.

### Aan camera gekoppeld {#env-attached}
Koppel de environment aan de camera.

Dit zorgt voor consistente belichting, wat handig kan zijn tijdens het beeldhouwen.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Zoals de naam al aangeeft (MATerial CAPture) bevat een matcap zowel de belichtings‑ als de materiaalinformatie in één afbeelding.
Omdat het materiaal zelf al in de matcap aanwezig is, worden de schilderkanalen roughness en metalness genegeerd.
De schilderkleur wordt met de matcap vermenigvuldigd; dat betekent dat als je een zwarte/grijze matcap hebt, wit schilderen het beeld niet helderder maakt.

Artiesten geven vaak de voorkeur aan deze modus voor beeldhouwen, omdat ze zich zo kunnen concentreren op de vorm en geometrie zelf.

Tik op de bol om een afbeeldingsbrowser te openen. Je kunt ook je eigen matcap toevoegen; in het algemeen kan elke foto, render of zelfs een schilderij van een bol die strak tot een vierkant is uitgesneden, worden gebruikt. Er zijn veel matcap‑bibliotheken online beschikbaar; een nuttige bron is de [nidorx matcap library](https://github.com/nidorx/matcaps).

### Globale Matcap gebruiken {#matcap-global}

Meestal gebruiken artiesten één enkele matcap voor het hele sculpt, maar als deze schakelaar is uitgeschakeld, kan elk object zijn eigen matcap hebben. Dit kan artistiek worden ingezet voor opvallende resultaten.

::: tip
Schakel deze optie uit en gebruik een afbeelding van een oogbal voor de ogen van je personage!
:::

### Rotatie {#matcap-rotation}
Een matcap is een gespecialiseerde vorm van een environment map, dus net als een environment map kan hij worden geroteerd. Je kunt dit ook op elk moment in de viewport doen door met drie vingers naar links en rechts te slepen.



## ![](/icons/circle_fill.webp) Onbelicht {#unlit}

In deze modus wordt alleen de oppervlakkleur weergegeven. Dit kan handig zijn om te controleren of de oppervlakkleur van je objecten is wat je verwacht, zonder afgeleid te worden door lichten, schaduwen, reflectie of transparantie. 

Deze modus kan ook worden gebruikt voor niet‑fotorealistische renders, om een vlakke, cartooneske look te bereiken.

## ![](/icons/cube.webp) Object-ID {#object-id}

Alle belichtings‑ en oppervlakte‑informatie wordt genegeerd en elk object wordt weergegeven met een unieke vlakke kleur. Als dit naast een PBR‑render wordt gerenderd, kan dit in een paint‑programma worden gebruikt om op kleur te selecteren en zo kleurcorrecties op specifieke objecten uit te voeren.

Let op: deze kleuren verschijnen ook in de [Scene‑menuboomstructuur](scene#tree-view).

### ID willekeurig maken {#object-random}

Genereer een nieuwe set willekeurige kleuren. 

## ![](/icons/link.webp) Instantie-ID {#instance-id}

Hetzelfde als Object ID, maar instanties krijgen dezelfde kleur. 

### ID willekeurig maken {#instance-random}

Genereer een nieuwe set willekeurige kleuren.