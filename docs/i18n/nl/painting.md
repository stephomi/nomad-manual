# ![](/icons/paint.webp) Schilderen  

Beheer de kleur, ruwheid, metallicheid van verfstreken, maak het mogelijk om verf‑eigenschappen te vullen (flood fill), en bepaal hoe verf‑tools omgaan met lagen, maskers en verborgen selecties.

![](/images/paint_overview.webp)  

## Overzicht

Nomad gebruikt PBR‑vertexpainting. Wat betekent dit?

### PBR
PBR, of Physically Based Rendering, is een populaire computer­grafiek‑techniek voor film, televisie, games en mobiel. Door licht te baseren op fysieke eigenschappen, en oppervlakken te definiëren via kleur, ruwheid en metallicheid, kan een grote variëteit aan fotorealistische looks worden bereikt.

### Vertexpainting

Vertexpainting betekent dat de verfinformatie wordt opgeslagen in de vertices van het model, in plaats van in textures. Omdat Nomad modellen met honderdduizenden, vaak miljoenen vertices aankan, zouden je modellen zeer gedetailleerde oppervlakteverf moeten kunnen hebben; als je het detail kunt beeldhouwen, kun je dat detail ook schilderen.

Dit betekent ook dat schilderen in Nomad geen UV‑mapping vereist, vaak een traag en technisch proces in andere 3D‑applicaties. Veel andere 3D‑applicaties ondersteunen niet de hoge vertex‑aantallen die Nomad wel aankan, maar Nomad heeft ook goede texture‑baking‑ en decimation‑tools om te helpen.

### Texturing

Nomad ondersteunt textures, maar die moeten aanwezig zijn in een geïmporteerd model, of via het bakken van vertexpainting naar textures. 

Een texture is simpelweg een afbeelding, maar in de 3D‑context verwijst het meestal naar een afbeelding die aan een object is toegewezen.
Om een afbeelding om een model heen te wikkelen, heeft het model texture‑coördinaten (UV) nodig.

Nomad kan [die automatisch berekenen](topology.md#uv-unwrap), maar je hebt niet veel controle over de algehele kwaliteit.

::: tip
Een voorbeeld van workflow:
- Beeldhouw in Nomad, daarna [UV‑unwrap](topology.md#uv-unwrap)
- Als je al bent begonnen met schilderen in Nomad kun je [de vertexpainting naar textures overzetten](topology.md#bake-vertex-colors-to-texture)
- Exporteer naar Procreate
- Texture in Procreate
- Exporteer terug naar Nomad voor render‑doeleinden
:::

Dat is het overzicht, nu bekijken we de onderdelen van het schildermenu:


## Stroke painting
![](/images/paint_intensity.webp)  

Schilderen inschakelen voor deze tool, handig als je tegelijk wilt beeldhouwen en schilderen.

Voor tools waar schilderen de primaire functie is (bijv. Paint, Smudge, Mask), bestaat dit selectievakje niet.

### Paint intensity

Een schuifregelaar waarmee je een andere intensiteit kunt gebruiken dan de primaire tool‑intensiteit.

De selectievakjes `Alpha`, `Falloff` en `Randomize` bepalen of die functies het schilderen beïnvloeden. Je kunt bijvoorbeeld randomize inschakelen voor de Clay‑tool, maar de kleur niet laten randomizen.


## Materiaal
![](/images/paint_material.webp) 

Het eerste pictogram is een materiaalvoorbeeld‑vorm. Door te slepen op de 3D‑materiaalpreview roteer je deze. 

Het tweede pictogram is een voorbeeld van de verfstreek met de geselecteerde alpha‑ en falloff‑opties.

Met de previewknop naast de titel Material kun je wisselen tussen none, Material of Triplanar. Dit bepaalt wat er gebeurt wanneer je verf‑eigenschappen interactief wijzigt:

* `None` - Er wordt geen preview op het model getoond wanneer je eigenschappen aanpast
* `Material` - De materiaalwaarden worden op het object gepreviewd wanneer je eigenschappen aanpast. Als je textures gebruikt en het model UV’s heeft, worden de UV’s gebruikt.
* `Triplanar` - Het materiaal wordt gepreviewd als een Triplanar‑projectie. 

De pipet kan worden gebruikt om alle eigenschappen van een object in je scène te samplen.

## Materiaalpresets
Tik op de 3D‑voorbeeldvorm om een preset‑menu met materialen te openen; deze kunnen worden gekloond om je eigen presets te definiëren.

![](/images/paint_presets.webp) 

De schakelaars `Embed Textures` en `Alpha` slaan, indien ingeschakeld, alle textures op die door dit materiaal worden gebruikt binnen de preset. Dit wordt hieronder verder uitgelegd.

## PBR‑schuifregelaars
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr)‑schilderen gebruikt 4 kanalen:
- `Color` De kleur die zal worden geschilderd. De pipet kan worden gebruikt om kleur te selecteren van andere delen van het model of van referentie‑afbeeldingen.
- `Roughness` Geeft aan hoe “ruw” of “glad” een oppervlak is. Een lage waarde voor roughness betekent dat de reflecties scherp zullen zijn.
- `Metalness` Geeft simpelweg aan of het oppervlak metallisch is of niet. De waarde zou meestal ofwel 0% of 100% moeten zijn; tussenliggende waarden zouden uitzonderlijk moeten zijn.
- `Opacity` Hoeveel van het materiaal je erdoorheen kunt zien. Strikt genomen maakt het geen deel uit van de PBR‑specificatie, maar het is in veel situaties nuttig. 1 is volledig ondoorzichtig, 0 is transparant. Merk op dat opacity en breking (refractie) verschillende dingen zijn; refractie in Nomad wordt afgehandeld via het refractie‑materiaal. 

Als je een materiaalpreset selecteert, worden 3 kanalen gelijktijdig geschilderd (opacity wordt vaak bewust uitgesloten). Dit betekent dat je in plaats van alleen ‘rood’ te schilderen, ‘een rood ruw metaal’ of ‘een wit glad plastic’ kunt schilderen.

Het vierkant is een texture‑slot; klik erop om een texture voor die eigenschap te gebruiken in plaats van een vaste waarde.

Het penseelpictogram naast de schuifregelaars zal die eigenschap over je object vullen (flood fill).

Het selectievakje schakelt die specifieke eigenschap in of uit, zodat je bijvoorbeeld alleen kleur kunt schilderen, of alleen roughness en opacity. 

Hier zijn enkele voorbeelden van verschillende roughness‑ en metalness‑eigenschappen:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Alleen kleur wordt ondersteund in [Matcap‑rendering](shading.md#matcap)‑modus; metalness en roughness worden genegeerd.
:::

::: tip
Wanneer je textures gebruikt voor PBR‑schilderen, is het vaak handig om over te schakelen naar bijvoorbeeld de `Stamp`‑tool, of het stroke‑menu te gebruiken om een andere modus dan dot te kiezen, die de texture kan uitsmeren.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Je kunt overwegen om `Smooth Shading` [globaal](settings.md#smooth-shading) of [per object](material.md#smooth-shading) in te schakelen als je een metalen oppervlak schildert op een object met een lagere polycount.
:::

## Paint all

![](/images/paint_paint_all.webp)

Pas het huidige materiaal toe op het object, ofwel in standaardmodus met ‘Paint All’, of als een Triplanar‑projectie.

De selectievakjes naast de color/metalness/roughness/opacity‑schuifregelaars worden gerespecteerd; uitgeschakelde eigenschappen worden niet gevuld.

De extra knoppen bepalen hoe Paint All verder kan worden beïnvloed:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Gemaskerde gebieden worden niet beïnvloed.    |
| ![](/icons/tool_hide.webp) | Verborgen gebieden worden niet beïnvloed.     |
| ![](/icons/opacity.webp)   | gebruik de tool‑schilderfactor hierboven.     |
| ![](/icons/layer.webp)     | Ongeschilderde gebieden van een laag worden niet beïnvloed. |
| ![](/icons/triplanar.webp) | Indicator van triplanar‑instellingen          |
| ![](/icons/cog.webp)       | Open de Triplanar‑instellingen                |

### Triplanar‑instellingen
![](/images/paint_triplanar_settings.webp)

Vergelijkbaar met de [triplanar‑instellingen in het materiaalmenu](material.md#triplanar) kun je de blending van de projecties, tiling en offsets regelen. 

Gebruik het preview‑selectievakje bovenaan dit menu om een blijvende preview in te schakelen terwijl je waarden aanpast.

## Globaal materiaal
Als deze optie is ingeschakeld, zal het geselecteerde materiaal hetzelfde zijn als bij de andere tools. Merk op dat alleen roughness‑, metalness‑ en kleurinstellingen in aanmerking worden genomen.
