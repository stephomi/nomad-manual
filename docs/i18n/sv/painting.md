# ![](/icons/paint.webp) Målning {#painting}

Styr färg, grovhet och metallitet för dina penseldrag med målning, fyll hela objekt med målningsegenskaper, och bestäm hur målningsverktygen samspelar med lager, masker och dolda områden.

![](/images/paint_overview.webp)  

## Översikt {#overview}

Nomad använder PBR-vertexmålning. Vad betyder det?

### PBR {#pbr}
PBR, eller Physically Based Rendering (fysikaliskt baserad rendering), är en populär datorgrafikteknik inom film, tv, spel och mobil. Genom att basera ljuset på fysikaliska egenskaper och beskriva ytor med färg, grovhet och metallitet kan man få fram en stor variation av fotorealistiska utseenden.

### Vertexmålning {#vertex-painting}

Vertexmålning betyder att målningsinformationen lagras i modellens vertexar i stället för i texturer. Eftersom Nomad klarar modeller med hundratusentals, ofta miljontals vertexar, kan dina modeller ha väldigt detaljrik målning på ytan: kan du skulptera detaljen kan du också måla den.

Det betyder också att målning i Nomad inte kräver UV-mappning, som ofta är en långsam och teknisk process i andra 3d-program. Många andra 3d-program klarar inte lika höga vertexantal som Nomad, men Nomad har också bra verktyg för texturbakning och decimering som hjälp.

### Texturering {#texturing}

Nomad stöder texturer, men de måste finnas i en importerad modell, eller skapas genom att baka vertexmålningen till texturer.

En textur är helt enkelt en bild, men i 3d-sammanhang menar man oftast en bild som är kopplad till ett objekt.
För att kunna svepa en bild runt en modell behöver modellen texturkoordinater (UV).

Nomad kan räkna ut [dem automatiskt](topology.md#uv-unwrap), men du har inte mycket kontroll över den övergripande kvaliteten.

::: tip
Ett exempel på arbetsflöde:
- Skulptera i Nomad och gör sedan en [UV-utvikning](topology.md#uv-unwrap)
- Om du redan har börjat måla i Nomad kan du [överföra vertexmålningen till texturer](topology.md#bake-texture)
- Exportera till Procreate
- Texturera i Procreate
- Exportera tillbaka till Nomad för att rendera
:::

Det var översikten, nu tar vi en titt på de olika delarna av målningsmenyn:


## Streckmålning {#stroke-painting}
![](/images/paint_intensity.webp)  

Aktiverar målning för det här verktyget, användbart om du behöver skulptera och måla samtidigt. När ett verktyg kan måla men den här kryssrutan är avstängd påminner en varningsikon bredvid rubriken dig om det.

För verktyg där målning är huvudfunktionen (t.ex. Måla, Smeta ut, Mask) finns inte den här kryssrutan.

### ![](/icons/opacity.webp) Målningsintensitet {#paint-intensity}

Ett reglage som låter dig använda en annan intensitet än verktygets huvudintensitet.

Reglageknappen bredvid lägger till ett snabbreglage för målningsintensiteten i sidofältet, för verktyg som skulpterar och målar samtidigt.

Knapparna `Alpha`, `Avmattning` och `Randomisera intensitet` bestämmer om de funktionerna påverkar målningen. Du kan till exempel ha slumpvariation aktiverad för verktyget Lera utan att färgen varieras slumpmässigt.

* `Alpha` - när den är avstängd ignorerar målningen alfan och täcker hela penselns yta. Med verktyget VDM ersätts den här knappen av `Stämpelmaterial`, som slår på eller av materialet som är lagrat i stämpeln.
* `Avmattning` - när den är avstängd behåller målningen full intensitet ända ut till penselns kant.
* `Randomisera intensitet` - om intensitetsdelen av penseldragets slumpvariation påverkar målningen. Slumpvariation av position, rotation och skala flyttar alltid hela stämpeln.

De här alternativen ignoreras av [Måla allt](#paint-all), men alfan används av dess triplanara variant.

### ![](/icons/link.webp) Globalt material {#global-material}
Om det här alternativet är aktiverat är det valda materialet detsamma som för de andra verktygen. Observera att bara inställningarna för grovhet, metallitet och färg tas med. Avaktivera det för att ge det här verktyget ett eget material.


## Material {#material}
![](/images/paint_material.webp) 

Den första ikonen är en form som förhandsvisar materialet. Om du drar på 3d-förhandsvisningen av materialet roterar den.

Den andra ikonen är en förhandsvisning av penseldraget med de valda alternativen för alfa och avmattning.

### ![](/icons/falloff.webp) Kurvor {#curves}

Öppnar en kurvredigerare för texturplatserna i [PBR-reglagen](#pbr-sliders). Den mappar om texturvärdena innan de målas, utan att röra bildfilen. En liten kurvikon på en texturplats visar att dess kurva har redigerats.

### ![](/icons/cog.webp) Materialalternativ {#material-options}

Knappen `Material` bredvid rubriken innehåller två inställningar.

`Materialförhandsvisning` bestämmer vad som händer på det valda objektet medan du ändrar reglagen för färg, grovhet, metallitet, opacitet och intensitet:

* `Ingen` - Ingen förhandsvisning visas på modellen när du justerar egenskaperna
* `Material` - Materialvärdena förhandsvisas på objektet när du justerar egenskaperna.
* `Triplanar` - Materialet förhandsvisas som en triplanar projektion.

Kryssrutorna för färg, grovhet, metallitet och opacitet nedanför väljer vilka kanaler som [Materialpipett](#material-picker) ersätter.

### ![](/icons/dropper.webp) Materialpipett {#material-picker}

Pipetten hämtar materialet under markören, från vilket objekt som helst i scenen. Bara de kanaler som är ikryssade i [Materialalternativ](#material-options) ersätts.

## Materialförinställningar {#material-presets}
Om du trycker på 3d-förhandsvisningens form öppnas en meny med förinställda material. De kan klonas så att du kan skapa dina egna förinställningar.

![](/images/paint_presets.webp) 

Reglaget `Bädda in texturer` sparar en kopia av texturerna som materialet använder inuti förinställningen. Utan det refererar förinställningen bara till texturerna i Nomads mapp textures/. Slå på det när du vill dela en texturerad förinställning utan att skicka texturerna separat.

`Inkludera alfa` sparar även penselns alfa i materialförinställningen.

## PBR-reglage {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr)-målning använder 4 kanaler:
- `Färg` Färgen som målas. Pipetten kan användas för att hämta färg från andra delar av modellen eller från referensbilder.
- `Grovhet` Anger hur "grov" eller "slät" en yta är. Ett lågt värde på grovheten betyder att reflektionerna blir skarpa.
- `Metallitet` Anger helt enkelt om ytan är metallisk eller inte. Värdet bör för det mesta vara antingen 0% eller 100%, värden däremellan bör vara undantag.
- `Opacitet` Hur mycket man kan se genom materialet. Strikt taget ingår den inte i PBR-specifikationen, men den är användbar i många situationer. 1 är helt ogenomskinligt, 0 är genomskinligt. Observera att opacitet och refraktion är olika saker: refraktion hanteras i nomad med refraktionsmaterialet.

Om du väljer en materialförinställning målas 3 kanaler samtidigt (opaciteten utesluts ofta avsiktligt). Det betyder att du i stället för att bara måla 'rött' kan måla 'en röd, grov metall' eller 'en vit, slät plast'.

Rutan är en texturplats: klicka på den för att använda en textur för den egenskapen i stället för ett fast värde. En färgtextur tonar färgen, medan en textur för grovhet, metallitet eller opacitet ersätter reglagets värde (dess etikett stryks över för att visa det). För opacitetstexturen läser `Använd alfa som värde` texturens alfakanal i stället för dess gråskalevärde.

Med verktyget VDM visas en extra plats bredvid texturplatsen när stämpeln har ett eget material. Tryck på den för att använda eller ignorera den kanalen i stämpeln.

Penselikonen bredvid reglagen fyller hela objektet med den egenskapen.

Kryssrutan aktiverar eller avaktiverar just den egenskapen, så att du till exempel kan måla bara färg, eller bara grovhet och opacitet.

Här är några exempel på olika värden för grovhet och metallitet:

|                | Metallitet 0%                     | Metallitet 100%              |
| :------------: | :-------------------------------: | :--------------------------: |
| Grovhet 0%     | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Grovhet 50%    | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Grovhet 100%   | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Grovhet och metallitet kräver skuggningsläget [Upplyst (PBR)](shading.md#pbr). I läget [MatCap](shading.md#matcap) eller [Obelyst](shading.md#unlit) ignoreras de, och menyn visar en varning.
:::

::: tip
När du använder texturer för PBR-målning är det ofta bra att byta till ett verktyg som `Stämpel`, eller att välja ett annat läge än punkt i penseldragsmenyn, eftersom det kan smeta ut texturen.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Du kan överväga att slå på `Jämn skuggning` [globalt](settings.md#smooth-shading) eller [per objekt](material.md#smooth-shading) om du målar en metallisk yta på ett objekt med lägre polygonantal.
:::

## ![](/icons/paint.webp) Måla allt {#paint-all}

![](/images/paint_paint_all.webp)

Tillämpa det aktuella materialet på de valda objekten, antingen i standardläget med `Måla allt`, eller som en triplanar projektion med `Måla allt + Triplanar`. Den triplanara varianten är inte tillgänglig på grundformer som inte har validerats.

Kryssrutorna bredvid reglagen för färg/metallitet/grovhet/opacitet respekteras: avaktiverade egenskaper fylls inte.

De extra knapparna styr hur Måla allt kan påverkas ytterligare. De flesta visar en procentsats, och de är gråade när de inte skulle ha någon effekt:

| Ikon                        | Beskrivning                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Maskerade områden påverkas inte.              |
| ![](/icons/tool_hide.webp) | Dolda områden påverkas inte.                  |
| ![](/icons/opacity.webp)   | Använd verktygets målningsfaktor ovan.        |
| ![](/icons/layer.webp)     | Omålade områden i ett lager påverkas inte.    |
| ![](/icons/triplanar.webp) | `Vertex`: den triplanara varianten förskjuter också ytan med alfan, med den visade verktygsintensiteten. |
| ![](/icons/cog.webp)       | Öppna Triplanar-inställningarna               |

### ![](/icons/cog.webp) Triplanar-inställningar {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Precis som med [triplanar-inställningarna i materialmenyn](material.md#triplanar) kan du styra hur projektionerna blandas, plattsättningen och förskjutningarna.

Använd förhandsgranskningskryssrutan högst upp i den här menyn för att få en bestående förhandsvisning medan du justerar värdena.
