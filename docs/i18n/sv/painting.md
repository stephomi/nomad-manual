# ![](/icons/paint.webp) Målning  

Styr färg, råhet, metallhet på penseldrag, möjliggör fyllning (flood fill) av målningsattribut och hur målarverktyg interagerar med lager, masker och dolda markeringar.

![](/images/paint_overview.webp)  

## Översikt

Nomad använder PBR‑vertexmålning. Vad betyder det?

### PBR
PBR, eller Physically Based Rendering, är en populär datorgrafik‑teknik för film, tv, spel och mobil. Genom att basera ljus på fysiska egenskaper och definiera ytor genom färg, råhet och metallhet kan en mängd fotorealistiska utseenden uppnås.

### Vertexmålning

Vertexmålning innebär att målningsinformationen lagras i modellens vertexar, istället för i texturer. Eftersom Nomad kan hantera modeller med hundratusentals, ofta miljontals vertexar, bör dina modeller kunna ha mycket detaljerad yt‑målning; om du kan skulptera detaljen kan du också måla den detaljen.

Detta innebär också att målning i Nomad inte kräver UV‑mappning, som ofta är en långsam och teknisk process i andra 3D‑applikationer. Många andra 3D‑applikationer stödjer inte de höga vertexantal som Nomad kan, men Nomad har också bra verktyg för texturbakning och decimering som hjälp.

### Texturering

Nomad stödjer texturer, men de måste finnas i en importerad modell, eller via bakning av vertexmålning till texturer. 

En textur är helt enkelt en bild, men i 3D‑sammanhang syftar det vanligtvis på en bild som tilldelats ett objekt.
För att kunna linda en bild runt en modell behöver modellen texturkoordinater (UV).

Nomad kan beräkna [dem automatiskt](topology.md#uv-unwrap) men du har inte så mycket kontroll över den övergripande kvaliteten.

::: tip
Ett exempel på arbetsflöde:
- Skulptera i Nomad, sedan [UV‑unwrappa](topology.md#uv-unwrap)
- Om du redan har börjat måla i Nomad kan du [överföra vertexmålningen till texturer](topology.md#bake-vertex-colors-to-texture)
- Exportera till Procreate
- Texturera i Procreate
- Exportera tillbaka till Nomad för rendering
:::

Det var översikten, nu går vi igenom sektionerna i målningsmenyn:


## Penselmålning
![](/images/paint_intensity.webp)  

Aktivera målning för detta verktyg, användbart om du behöver skulptera och måla samtidigt.

För verktyg där målning är huvudfunktionen (t.ex. Paint, Smudge, Mask) finns inte denna kryssruta.

### Målningsintensitet

En slider som låter dig använda en annan intensitet än verktygets primära intensitet.

Kryssrutorna `Alpha`, `Falloff` och `Randomize` avgör om dessa funktioner påverkar målningen. T.ex. kan du ha randomize aktiverat för Clay‑verktyget, men färgen kommer inte att slumpas.

## Material
![](/images/paint_material.webp) 

Den första ikonen är en materialförhandsvisningsform. Genom att dra på 3D‑materialförhandsvisningen roterar du den. 

Den andra ikonen är en förhandsvisning av penseldraget med vald alpha och falloff‑inställning.

Förhandsvisningsknappen bredvid Material‑rubriken låter dig växla mellan None, Material eller Triplanar. Detta avgör vad som händer när du interaktivt ändrar målnings‑egenskaper:

* `None` - Ingen förhandsvisning visas på modellen när du justerar egenskaper
* `Material` - Materialvärdena förhandsvisas på objektet när du justerar egenskaper. Om du använder texturer och modellen har UV:n kommer UV:na att användas.
* `Triplanar` - Materialet förhandsvisas som en triplanar‑projektion. 

Pipetten kan användas för att sampla alla egenskaper från ett objekt i din scen.

## Materialpresets
Genom att trycka på 3D‑förhandsvisningsformen öppnas en preset‑meny med material, dessa kan klonas för att definiera egna presets.

![](/images/paint_presets.webp) 

Växlarna `Embed Textures` och `Alpha` lagrar, när de är aktiverade, alla texturer som används av detta material i preset:en. Detta förklaras mer nedan.

## PBR‑reglage
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr)‑målning använder 4 kanaler:
- `Color` Färgen som kommer att målas. Pipetten kan användas för att välja färg från andra delar av modellen eller från referensbilder.
- `Roughness` Anger hur ”grov” eller ”slät” en yta är. Ett lågt värde för råhet innebär att reflektionerna blir skarpa.
- `Metalness` Anger helt enkelt om ytan är metallisk eller inte. Värdet bör vara antingen 0 % eller 100 % för det mesta, mellanliggande värden bör vara undantag.
- `Opacity` Hur mycket materialet går att se igenom. Strikt taget är det inte en del av PBR‑specifikationen, men det är användbart i många situationer. 1 är helt opakt, 0 är transparent. Notera att opacitet och brytning (refraction) är olika saker, brytning i Nomad hanteras via refraction‑materialet. 

Om du väljer ett materialpreset målas 3 kanaler samtidigt (opacitet utesluts ofta medvetet). Det betyder att istället för att bara måla ”rött” kan du måla ”en röd grov metall” eller ”en vit slät plast”.

Kvadraten är en texturplats, klicka på den för att använda en textur för den egenskapen istället för ett fast värde.

Penselikonen bredvid reglagen flood‑fyller den egenskapen över ditt objekt.

Kryssrutan aktiverar eller inaktiverar just den egenskapen, så du kan till exempel bara måla färg, eller bara måla råhet och opacitet. 

Här är några exempel på olika råhets‑ och metallhets‑egenskaper:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Endast färg stöds i [Matcap‑rendering](shading.md#matcap)‑läge, metallhet och råhet ignoreras.
:::

::: tip
När du använder texturer för PBR‑målning är det ofta användbart att byta till exempelvis `Stamp`‑verktyget, eller använda Stroke‑menyn för att använda ett annat läge än Dot, som kan smeta ut texturen.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Du kan överväga att slå på `Smooth Shading` [globalt](settings.md#smooth-shading) eller [per objekt](material.md#smooth-shading) om du målar en metallisk yta på ett objekt med lägre polyantal.
:::

## Paint all

![](/images/paint_paint_all.webp)

Applicera det aktuella materialet på objektet, antingen i standardläge med ”Paint All” eller som en triplanar‑projektion.

Kryssrutorna bredvid reglagen för color/metalness/roughness/opacity respekteras, alla inaktiverade egenskaper fylls inte.

De extra knapparna styr hur Paint All kan påverkas ytterligare:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Maskerade områden påverkas inte.              |
| ![](/icons/tool_hide.webp) | Dolda områden påverkas inte.                  |
| ![](/icons/opacity.webp)   | använd verktygets målningsfaktor ovan.        |
| ![](/icons/layer.webp)     | Omålade områden i ett lager påverkas inte.    |
| ![](/icons/triplanar.webp) | Indikator för triplanar‑inställningar         |
| ![](/icons/cog.webp)       | Öppna triplanar‑inställningarna               |

### Triplanar‑inställningar
![](/images/paint_triplanar_settings.webp)

Liknande [triplanar‑inställningarna i materialmenyn](material.md#triplanar) kan du styra blandningen av projektionerna, tiling och offsetar. 

Använd förhandsvisningskryssrutan högst upp i denna meny för att aktivera en bestående förhandsvisning medan du justerar värden.

## Globalt material
Om detta alternativ är aktiverat kommer det valda materialet att vara detsamma som för de andra verktygen. Notera att det bara tar hänsyn till inställningarna för roughness, metalness och color.
