# ![](/icons/material.webp) Material {#material}

Den här menyn låter dig ändra materialet på det aktuella objektet, renderings­egenskaperna för objektet/materialet och tilldela texturer till materialet.

![](/images/material_overview.webp)

Material definierar hur ett objekt ser ut genom att styra hur det reagerar på ljus och på andra objekt. Utseendet på ett objekt styrs av dessa egenskaper:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Kombinationer av dessa egenskaper kan uppnå ett brett spektrum av resultat, från fotorealistiskt till tecknat till experimentellt.

Färg, roughness, metalness och opacity kan målas, se [Vertex Paint options](painting.md) för mer information.

Material type, reflectance, emssive/unlit är materialegenskaper som förklaras nedan.

Kopiera/klistra in-knapparna högst upp i den här menyn låter dig kopiera material från ett objekt till ett annat.

Observera att Nomads renderer är en realtidsrenderer; även om den är kraftfull prioriterar den hastighet framför exakthet för vissa effekter. 

## Materialtyper {#material-types}

![](/images/material_types.webp)

Nomads materialtyper är Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Ogenomskinlig {#opaque}
Standardläget som behandlar ytor som ett enkelt material som stöder målad färg, roughness, metalness, opacity.

### ![](/icons/material_subsurface.webp) Under-yta {#subsurface}
Detta läge kan simulera material som låter ljus suddas ut och spridas internt, som hud, vax, jade.

För bästa resultat, växla till PBR-shading-läge och använd minst en riktad ljuskälla eller spot­ljus, helst med en svag omgivningsbelysning.

`Depth` styr hur långt ljuset sprids från framsidan, in under ytan och sedan ut genom framsidan igen. Detta har effekten att mjuka upp hårda skuggor och sudda ut ytdetaljer.

`Translucency` styr hur ljus sprids från framsidan till baksidan av en form, som ljusspridning genom undersidan av ett löv eller när öron är starkt bakbelysta. 

### ![](/icons/material_blending.webp) Blandning {#blending}

Liknar Opaque, men stöder opacitetsreglaget för att låta materialet blandas mellan solitt och transparent. Detta är ett enkelt enskilt reglage för opacitet, jämfört med den målningsbara opaciteten som stöds av det opaka materialet. 

::: warning
Blending-läget kan orsaka flimrande och hopp i komplexa eller skärande former.
:::

### ![](/icons/material_additive.webp) Additiv {#additive}
Du kan göra ditt mesh halvtransparent med detta material. Det liknar blending-materialet, men medan blending blandas med sin omgivning kommer additive alltid att vara ljusare än objekten bakom, bra för ljusa effekter som ljusstrålar, eld, explosioner.

Du kan ställa in ett opacitetsvärde högre än 1, vilket innebär att objektet blir ljusare.  
Det kan vara användbart om du vill använda [bloom](postprocess.md#bloom) och `threshold parameter` för att bara få detta objekt att glöda som ett emissivt objekt.

Detta läge tenderar att ha färre artefakter än [Blending](#blending) (ordningsoberoende transparens).

### ![](/icons/material_refraction.webp) Brytning {#refraction}
Detta läge kan användas för att simulera glasmaterial. På grund av realtidsbegränsningar är själv­brytning och flerskiktsbrytning något begränsad.

Roughness-målningen på modellen påverkar hur suddig brytningen är.
Som standard har varje objekt som skapas i Nomad en roughness på ungefär 25 %, därför kommer brytningen inte att vara perfekt utan lite suddig.
Du kan använda knappen `paint glossy` för att måla om din modell med roughness och metalness 0 (färgerna påverkas inte).

Det finns två olika roughness i spel, den som styr hur suddig reflektionen är på ytan, och den andra som styr insidan (brytningen).  
Eftersom det bara finns en målningsbar roughness-kanal i Nomad kommer dock både inre och yttre roughness att dela samma värde.  
För att få olika värden (till exempel en klubba med skarp yta men suddig insida) använder du reglagen `Surface glossiness` och `Interior roughness` för att åsidosätta den målade roughnessen.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Gör objektet halvtransparent genom att kasta bort vissa pixlar på ett slumpmässigt sätt.

### ![](/icons/material_shadow_catcher.webp) Skuggfångare {#shadow-catcher}

Gör objektet osynligt och ta bara emot skuggor. Användbart för att kombinera Nomad-renderingar med andra bilder. 

::: tip

Mer information om transparens och blending-lägen finns på https://support.fab.com/s/article/Transparency-Opacity

:::

## Kontroller {#controls}

![](/images/material_controls.webp)

### Alltid ej belyst {#always-unlit}
Om aktiverat kommer objektet att ignorera PBR och Matcap och helt enkelt visa sin färgmålning utan skuggning.
Observera att om du använder [Additive](#additive) kan du måla transparens direkt genom att använda svart färg.

### Opacitet {#opacity}
Hur solid eller opak ett objekt kommer att se ut; 100 % är solitt, 0 % är transparent. Du kan också måla opacitet för finare kontroll.

### Reflektans {#reflectance}
Styr mängden reflektion som materialet får för icke-metalliska material. För det mesta bör standardvärdet användas (vilket motsvarar standard 4 % reflekterat ljus vid normal vinkel), men kan ökas för att förstärka reflektioner och högdagrar i till exempel en karaktärs ögon.

### Inverterad culling {#inverse-culling}
Vänd normalerna på en yta. Vanligtvis inte nödvändigt, men kan användas om en modell verkar vara ut och in, eller i kombination med `Two sided` avstängt, kan användas för att göra interiörer där väggen närmast kameran alltid är dold.

### Mjuk skuggning {#smooth-shading}
Se [global option](settings.md#smooth-shading).  
Värdet `Auto` använder det globala alternativet.

### Tvåsidig {#two-sided}
Se [global option](settings.md#two-sided).  
Värdet `Auto` använder det globala alternativet.

### Färgad baksida {#coloured-backface}
Se [global option](settings#two-sided).
Värdet `Auto` använder det globala alternativet.

### Kastar skuggor {#casts-shadows}
För närvarande är `Auto` samma som `On`.
Transparenta objekt kastar också skuggor (i ett dithering-mönster för att efterlikna blandade skuggor).  
Se till att inaktivera skuggkastning om du har ett stort objekt i din scen som inte behöver kasta skuggor (till exempel ett stort golv).

### Tar emot skuggor {#recieve-shadows}
För närvarande är `Auto` samma som `On`.

### Trådram {#wireframe}
Se [global option](settings.md#wireframe).  
Värdet `Auto` använder det globala alternativet.


## Texturer {#textures}

![](/images/material_textures.webp)

Om ett objekt har UV:n kan texturer appliceras på materialet utöver vertex color/roughness/metalness/opacity. Vanligtvis är dessa resultatet av en texture bake, men bilder skapade utanför Nomad kan också användas.

Texturer kan appliceras på

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Att klicka på en texturplats öppnar en väljare. När en textur har tilldelats en materialplats kommer ett nytt klick att öppna en texturpanel:

### Texturpanelalternativ {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Öppna {#open}
Välj en annan textur

### Ingen {#none}
Ta bort texturen

### Opacitet {#texture-opacity}

Om bilden har en alfakanal låter detta dig använda den för Opacity eller ignorera den.

### ![](/icons/link.webp) Kedja/Länk-ikon {#chainlink-icon}

Länksymbolen i följande avsnitt, när den är aktiverad, innebär att vilka alternativ som än används kommer att delas med de andra texturerna (color, normal, roughness, metalness, opacity, emissive) som också har sin länksymbol aktiverad. 

Detta låter dig säkerställa att om du har linjerade texturer kommer de att förbli linjerade även när du ändrar parametrar eller projektionstyper.


### Projektion {#projection}
![](/images/material_projection.webp)

Ställ in hur texturen ska appliceras på objektet.

* `Auto` - Om objektet har uv:n, UV, annars Triplanar
* `UV` - Använd meshens uv-koordinater för att applicera texturen. Om mesh och textur kommer från utanför Nomad, eller ska exporteras från Nomad för att användas någon annanstans, är UV det korrekta alternativet.
* `Triplanar` - Projektera texturen längs X-, Y-, Z-axlarna och blanda sömmarna. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanära projektioner är ett kraftfullt men enkelt sätt att applicera texturer på objekt.

Triplanar är som att ha 6 videoprojektorer alla med samma bild, som lyser på fram-, bak-, vänster-, höger-, topp- och botten­sidan av ditt objekt.

Detta kan sedan bakas in i UV:n eller vertexfärger vid behov.


![](/images/material_triplanar_example.webp)

#### Metod {#method}

* `Local` - Projektionen kommer att röra sig med objektets transform
* `World` - Projektionen förblir fast, att flytta objektet kommer att skjuta det genom projektionen.

#### Hårdhet {#hardness}

Hur projektionerna blandas. 100 % gör ingen blandning och kanterna på projektionerna blir skarpa. 0 % blandar kanterna över en bred vinkel. Standard är 90 %, tillräckligt med blandning för att dölja kanterna och låta resten av projektionerna förbli skarpa.

### Enhetlig {#uniform}

När ikryssad används samma hardness för alla projektioner. När den inte är ikryssad visas extra hardness-kontroller för X-, Y-, Z-projektioner.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filtrering {#filtering}
Texturfiltreringsmetoden som ska användas, `Auto` är standard, metoderna är `Nearest`, `Linear`, `Mipmap`. Nearest gör ingen filtrering, så texturer kan få kantiga artefakter när de visas på nära håll. Linear och Mipmap gör bättre filtrering, så texturer verkar suddiga snarare än kantiga på nära håll.

#### Tile-X {#tiling-x}
Om parametern Scale är större än 1, vilket gör texturen mindre än objektets UV:n, hur texturen ska upprepas längs X-axeln. `None` betyder inga upprepningar. `Repeat` gör kopior av texturen. `Mirror` gör kopior av texturen där varannan kopia är spegelvänd, vilket kan hjälpa till att dölja upprepningsartefakter.

#### Tile-Y {#tiling-y}
Samma som Tiling-X, men för Y-axeln.

### Transformera {#transform}
![](/images/material_transform.webp)

Extra 2D-transformationer som appliceras på texturen i UV-utrymme. Återställningsknappen återställer till standardvärden, länksymbolen (när andra texturer än color är valda) länkar eller avlänkar transformen så att den blir densamma som color-texturens.

#### Translatering {#translation}
X- och Y-förskjutningen för texturen

#### Rotation {#rotation}
Rotationen på texturen

#### Skalning {#scale}
Skalan på texturen, större tal gör texturen mindre på objektet, använd reglagen Tiling-X och Tiling-Y för att styra vad som händer.

### Enhetlig skalning {#uniform-scale}
När den är avstängd visar Nomad separata kontroller för Scale-X och Scale-Y.