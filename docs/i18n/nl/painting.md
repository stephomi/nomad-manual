# ![](/icons/paint.webp) Schilderen {#painting}

Regelt de kleur, ruwheid en metaalheid van schilderstreken, laat je eigenschappen over het hele object vullen, en bepaalt hoe schildergereedschappen omgaan met lagen, maskers en verborgen delen.

![](/images/paint_overview.webp)  

## Overzicht {#overview}

Nomad gebruikt PBR-vertex-schilderen. Wat betekent dat?

### PBR {#pbr}
PBR, of Physically Based Rendering, is een populaire techniek in computergraphics voor film, televisie, games en mobiel. Door lichten te baseren op fysieke eigenschappen en oppervlakken te beschrijven met kleur, ruwheid en metaalheid, kun je een grote verscheidenheid aan fotorealistische looks bereiken.

### Vertex-schilderen {#vertex-painting}

Bij vertex-schilderen wordt de verfinformatie in de vertices van het model opgeslagen, in plaats van in texturen. Omdat Nomad modellen aankan met honderdduizenden en vaak miljoenen vertices, kunnen je modellen heel gedetailleerd beschilderd worden: kun je een detail sculpten, dan kun je het ook schilderen.

Het betekent ook dat schilderen in Nomad geen UV-mapping nodig heeft, in andere 3d-programma's vaak een traag en technisch proces. Veel andere 3d-programma's kunnen niet zo veel vertices aan als Nomad, maar Nomad heeft ook goede gereedschappen om texturen te bakken en te decimeren.

### Texturen {#texturing}

Nomad ondersteunt texturen, maar die moeten al in een geïmporteerd model zitten, of ontstaan door vertex-schilderwerk naar texturen te bakken.

Een textuur is gewoon een afbeelding, maar in een 3d-context bedoelen we meestal een afbeelding die aan een object is gekoppeld.
Om een afbeelding rond een model te wikkelen, heeft het model textuurcoördinaten (UV) nodig.

Nomad kan [ze automatisch berekenen](topology.md#uv-unwrap), maar je hebt dan weinig controle over de algehele kwaliteit.

::: tip
Een voorbeeld van een workflow:
- Sculpt in Nomad en doe daarna een [UV-ontvouwen](topology.md#uv-unwrap)
- Ben je al begonnen met schilderen in Nomad, dan kun je [het vertex-schilderwerk naar texturen overbrengen](topology.md#bake-texture)
- Exporteer naar Procreate
- Maak de texturen in Procreate
- Exporteer terug naar Nomad om te renderen
:::

Tot zover het overzicht. Laten we nu de secties van het menu Schilderen bekijken:


## Penseelschilderen {#stroke-painting}
![](/images/paint_intensity.webp)  

Zet schilderen aan voor dit gereedschap, handig als je tegelijk wilt sculpten en schilderen. Kan een gereedschap schilderen maar staat dit vinkje uit, dan herinnert een waarschuwingsicoon naast de titel je daaraan.

Bij gereedschappen waarvan schilderen de hoofdfunctie is (bijv. Verf, Vlekken, Masker), bestaat dit vinkje niet.

### ![](/icons/opacity.webp) Schilderintensiteit {#paint-intensity}

Een schuifregelaar waarmee je een andere intensiteit gebruikt dan de hoofdintensiteit van het gereedschap.

De schuifregelaarknop ernaast zet een snelle schuifregelaar voor de schilderintensiteit in de zijbalk, voor gereedschappen die tegelijk sculpten en schilderen.

De knoppen `Alpha`, `Afname` en `Intensiteit variëren` bepalen of die functies invloed hebben op het schilderen. Je kunt bijvoorbeeld variatie aanzetten voor het gereedschap Klei, zonder dat de kleur varieert.

* `Alpha` - staat dit uit, dan negeert het schilderen de alpha en bedekt het het hele penseeloppervlak. Bij het gereedschap VDM wordt deze knop vervangen door `Stempelmateriaal`, waarmee je het materiaal dat in de stempel is opgeslagen aan- of uitzet.
* `Afname` - staat dit uit, dan blijft het schilderen op volle intensiteit tot aan de rand van het penseel.
* `Intensiteit variëren` - of het intensiteitsdeel van de streekvariatie invloed heeft op het schilderen. Variatie in positie, rotatie en schaal verplaatst altijd de hele stempel.

Deze opties worden genegeerd door [Alles verven](#paint-all), maar de triplanaire variant ervan gebruikt wel de alpha.

### ![](/icons/link.webp) Globaal materiaal {#global-material}
Staat deze optie aan, dan is het gekozen materiaal hetzelfde als bij de andere gereedschappen. Alleen de instellingen voor ruwheid, metaalheid en kleur tellen mee. Zet het uit om dit gereedschap een eigen materiaal te geven.


## Materiaal {#material}
![](/images/paint_material.webp) 

Het eerste icoon is een voorbeeldvorm van het materiaal. Sleep over het 3d-materiaalvoorbeeld om het te draaien.

Het tweede icoon is een voorbeeld van de schilderstreek met de gekozen alpha- en afname-opties.

### ![](/icons/falloff.webp) Curven {#curves}

Opent een curve-editor voor de textuurvakken van de [PBR-schuifregelaars](#pbr-sliders). Die past de waarden van de textuur aan voordat ze worden geschilderd, zonder het afbeeldingsbestand te wijzigen. Een klein curve-icoon op een textuurvak laat zien dat de curve ervan is aangepast.

### ![](/icons/cog.webp) Materiaalopties {#material-options}

De knop `Materiaal` naast de titel bevat twee instellingen.

`Materiaalviewportvoorbeeld` bepaalt wat er op het geselecteerde object gebeurt terwijl je de schuifregelaars voor kleur, ruwheid, metaalheid, dekking en intensiteit aanpast:

* `Geen` - Er wordt geen voorbeeld op het model getoond als je eigenschappen aanpast.
* `Materiaal` - De materiaalwaarden worden als voorbeeld op het object getoond als je eigenschappen aanpast.
* `Triplanar` - Het materiaal wordt als voorbeeld getoond als triplanaire projectie.

Met de vinkjes voor kleur, ruwheid, metaalheid en dekking eronder kies je welke kanalen de [Materiaalpipet](#material-picker) vervangt.

### ![](/icons/dropper.webp) Materiaalpipet {#material-picker}

De pipet neemt het materiaal onder de cursor over, van elk object in je scène. Alleen de kanalen die in de [Materiaalopties](#material-options) zijn aangevinkt, worden vervangen.

## Materiaalpresets {#material-presets}
Tik op de 3d-voorbeeldvorm om een presetmenu met materialen te openen. Je kunt ze klonen om je eigen presets te maken.

![](/images/paint_presets.webp) 

De schakelaar `Texturen insluiten` bewaart een kopie van de texturen die dit materiaal gebruikt in de preset zelf. Zonder deze optie verwijst de preset alleen naar de texturen in de map textures/ van Nomad. Zet hem aan als je een preset met texturen wilt delen zonder de texturen apart te versturen.

`Alpha opnemen` slaat ook de penseel-alpha op in de materiaalpreset.

## PBR-schuifregelaars {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr)-schilderen gebruikt 4 kanalen:
- `Kleur` De kleur die wordt geschilderd. Met de pipet kun je een kleur overnemen van andere delen van het model of van referentieafbeeldingen.
- `Ruwheid` Geeft aan hoe "ruw" of "glad" een oppervlak is. Een lage ruwheid betekent scherpe reflecties.
- `Metaalheid` Geeft gewoon aan of het oppervlak metallisch is of niet. Meestal hoort de waarde 0% of 100% te zijn; waarden daartussen zouden een uitzondering moeten zijn.
- `Dekking` Hoeveel je door het materiaal heen kunt kijken. Strikt genomen hoort het niet bij de PBR-specificatie, maar het is in veel situaties handig. 1 is volledig ondoorzichtig, 0 is doorzichtig. Let op: dekking en breking zijn twee verschillende dingen; breking regel je in Nomad met het materiaaltype Breking.

Kies je een materiaalpreset, dan worden 3 kanalen tegelijk geschilderd (dekking wordt vaak bewust weggelaten). In plaats van alleen 'rood' schilder je dan bijvoorbeeld 'een rood, ruw metaal' of 'een wit, glad plastic'.

Het vierkantje is een textuurvak: klik erop om voor die eigenschap een textuur te gebruiken in plaats van een vaste waarde. Een kleurtextuur kleurt de kleur in, terwijl een ruwheids-, metaalheids- of dekkingstextuur de waarde van de schuifregelaar vervangt (het label wordt dan doorgestreept). Bij de dekkingstextuur leest `Alfa als waarde gebruiken` het alfakanaal van de textuur in plaats van de grijswaarde.

Bij het gereedschap VDM verschijnt, als de stempel een eigen materiaal heeft, een extra vak naast het textuurvak. Tik erop om dat kanaal van de stempel te gebruiken of te negeren.

Het penseelicoon naast de schuifregelaars vult je object met die eigenschap.

Met het vinkje zet je een eigenschap aan of uit, zodat je bijvoorbeeld alleen kleur schildert, of alleen ruwheid en dekking.

Hier zijn een paar voorbeelden van verschillende waarden voor ruwheid en metaalheid:

|                | Metaalheid 0%                     | Metaalheid 100%              |
| :------------: | :-------------------------------: | :--------------------------: |
| Ruwheid 0%     | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Ruwheid 50%    | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Ruwheid 100%   | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Ruwheid en metaalheid vereisen de shadingmodus [Verlicht (PBR)](shading.md#pbr). In de modus [MatCap](shading.md#matcap) of [Onbelicht](shading.md#unlit) worden ze genegeerd, en het menu toont een waarschuwing.
:::

::: tip
Gebruik je texturen voor PBR-schilderen, dan is het vaak handig om over te stappen op bijvoorbeeld het gereedschap `Stempel`, of in het menu Streek een andere modus dan dot te kiezen, want die kan de textuur uitsmeren.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Overweeg om `Vloeiende shading` [globaal](settings.md#smooth-shading) of [per object](material.md#smooth-shading) aan te zetten als je een metallisch oppervlak schildert op een object met weinig polygonen.
:::

## ![](/icons/paint.webp) Alles verven {#paint-all}

![](/images/paint_paint_all.webp)

Brengt het huidige materiaal aan op de geselecteerde objecten, ofwel in de standaardmodus met `Alles verven`, ofwel als triplanaire projectie met `Alles verven + Triplanar`. De triplanaire variant is niet beschikbaar voor primitieven die nog niet zijn gevalideerd.

De vinkjes naast de schuifregelaars voor kleur, metaalheid, ruwheid en dekking worden gerespecteerd: uitgeschakelde eigenschappen worden niet gevuld.

De extra knoppen bepalen verder hoe Alles verven werkt. De meeste tonen een percentage, en ze zijn grijs wanneer ze geen effect zouden hebben:

| Icoon                       | Beschrijving                                  |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Gemaskerde gebieden worden niet beïnvloed.    |
| ![](/icons/tool_hide.webp) | Verborgen gebieden worden niet beïnvloed.     |
| ![](/icons/opacity.webp)   | Gebruikt de schilderfactor van het gereedschap hierboven. |
| ![](/icons/layer.webp)     | Onbeschilderde delen van een laag worden niet beïnvloed. |
| ![](/icons/triplanar.webp) | `Vertex`: de triplanaire variant verschuift ook het oppervlak met de alpha, met de getoonde intensiteit van het gereedschap. |
| ![](/icons/cog.webp)       | Opent de triplanaire instellingen             |

### ![](/icons/cog.webp) Triplanaire instellingen {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Net als bij de [triplanaire instellingen in het menu Materiaal](material.md#triplanar) regel je hier hoe de projecties in elkaar overlopen, de herhaling en de verschuivingen.

Met het voorbeeldvinkje bovenaan dit menu zet je een blijvend voorbeeld aan terwijl je waarden aanpast.
