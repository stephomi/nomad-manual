# ![](/icons/material.webp) Material {#material}

I den här menyn kan du ändra det aktuella objektets material, objektets och materialets renderingsegenskaper, och koppla texturer till materialet.

![](/images/material_overview.webp)

Material bestämmer hur ett objekt ser ut, genom att styra hur det reagerar på ljus och på andra objekt. Ett objekts utseende styrs av de här egenskaperna:

* `Materialtyp`
* `Färg`
* `Grovhet`
* `Metallitet`
* `Opacitet`
* `Reflekterande förmåga`
* `Emissiv/obelyst`

Med kombinationer av de här egenskaperna kan du få fram en stor variation av resultat, från fotorealistiskt till tecknat till experimentellt.

Färg, grovhet, metallitet och opacitet kan målas, se [alternativen för vertexmålning](painting.md) för mer information.

Materialtyp, reflekterande förmåga och emissiv/obelyst är materialegenskaper som förklaras nedan.

Med knapparna `Kopiera` och `Klistra in` högst upp i menyn kan du kopiera material från ett objekt till ett annat.

Observera att Nomads renderare är en realtidsrenderare: den är kraftfull, men prioriterar hastighet framför precision för vissa effekter.

## Materialtyper {#material-types}

![](/images/material_types.webp)

Nomads materialtyper är Oopakt, Subyta, Blandning, Additiv, Brytning, Dithering och Skuggfångare.

### ![](/icons/material_opaque.webp) Oopakt {#opaque}
Standardläget, som behandlar ytor som ett enkelt material med stöd för målad färg, grovhet, metallitet och opacitet. Målad opacitet, en opacitetstextur eller färgtexturens alfakanal gör fortfarande objektet genomskinligt, med hjälp av dithering. Bara huvudreglaget för opacitet ignoreras.

### ![](/icons/material_subsurface.webp) Subyta {#subsurface}
Det här läget kan simulera material där ljuset sprids och suddas ut inuti materialet, som hud, vax och jade.

Det kräver skuggningsläget PBR. För bästa resultat, använd minst ett riktat ljus eller en spotlight, helst med en dämpad miljö.

Färgrutan ställer in färgen på det spridda ljuset.

`Djup` styr hur långt ljuset sprids från framsidan, in under ytan och sedan ut genom framsidan igen. Det mjukar upp hårda skuggor och suddar ut detaljer på ytan.

`Translucens` styr hur ljuset sprids från framsidan till baksidan av en form, som när ljus tränger igenom undersidan av ett löv, eller när öron har starkt motljus. Du behöver ett ljus som kastar skuggor för att se det.

### ![](/icons/material_blending.webp) Blandning {#blending}

Liknar Oopakt, men stöder opacitetsreglaget så att materialet kan blandas mellan solitt och genomskinligt. Det är ett enkelt enda reglage för opaciteten, till skillnad från den målningsbara opacitet som det opaka materialet stöder.

::: warning
Läget Blandning kan orsaka flimmer och objekt som hoppar fram i komplexa eller korsande former.
:::

### ![](/icons/material_additive.webp) Additiv {#additive}
Med det här materialet kan du göra ditt nät halvgenomskinligt. Det liknar materialet Blandning, men medan Blandning blandas med omgivningen blir Additiv alltid ljusare än objekten bakom, bra för ljusa effekter som ljusstrålar, eld och explosioner.

Du kan ställa in ett opacitetsvärde högre än 1, vilket gör objektet ljusare.  
Det kan vara användbart om du vill använda [bloom](postprocess.md#bloom) och `tröskelparametern` för att bara få det här objektet att lysa, som ett emissivt objekt.

Det här läget brukar ge färre artefakter än [Blandning](#blending) (ordningsoberoende transparens).

### ![](/icons/material_refraction.webp) Brytning {#refraction}
Det här läget kan användas för att simulera glas. Det kräver skuggningsläget PBR. På grund av begränsningarna i realtid är självbrytning och brytning i flera lager något begränsade.

Modellens målade grovhet påverkar hur suddig brytningen blir.
Som standard har varje objekt som skapas i Nomad en grovhet runt 25%, så brytningen blir inte perfekt utan lite suddig.
Du kan använda knappen `Glansmåla` för att måla om modellen med en grovhet och metallitet på 0 (färgerna påverkas inte).

Det finns 2 olika grovheter inblandade: den ena styr hur suddig reflektionen på ytan är, och den andra styr insidan (brytningen).  
Men eftersom det bara finns en målad grovhetskanal i Nomad delar både insidans och utsidans grovhet samma värde.  
För att få olika värden (till exempel en klubba med skarp yta men suddig insida) använder du reglagen `Yta` och `Inre` under `Åsidosätt grovhetsvärde` för att åsidosätta den målade grovheten.

![](/videos/refraction.mp4)

#### Brytningsindex {#index-of-refraction}
Hur mycket ljuset böjs av när det går in i objektet. Högre värden böjer det mer, som en tjock lins.

#### Absorption {#absorption}
Simulerar att ljuset absorberas när det färdas genom volymen, tonat av färgrutan, där `Faktor` ställer in styrkan. Tunna delar blir ljusare eftersom de släpper igenom mer ljus, medan tjocka områden blir mörkare. Bara en uppskattning av objektets tjocklek används, så effekten beror mycket på formen.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Gör objektet halvgenomskinligt genom att slumpmässigt hoppa över vissa pixlar.

### ![](/icons/material_shadow_catcher.webp) Skuggfångare {#shadow-catcher}

Gör objektet osynligt så att det bara tar emot skuggor från ljusen. Användbart för att kombinera renderingar från nomad med andra bilder, oftast på ett plan. Färgrutan ställer in skuggans färg.

Det måste finnas ett ljus som kastar skuggor i scenen, annars gör skuggfångaren ingenting. Knapparna `Metallitet → 0%` och `Metallitet → 100%` målar om objektet: helt metalliskt kan skuggfångaren även spegla scenen när efterbehandlingen [Reflektion (SSR)](postprocess.md#reflection-ssr) är aktiverad.

::: tip

Mer information om transparens och blandningslägen finns på https://support.fab.com/s/article/Transparency-Opacity

:::

## Kontroller {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Alltid utan belysning {#always-unlit}
Om det är aktiverat ignorerar objektet PBR och Matcap och visar bara sin målade färg utan skuggning.
Observera att om du använder [Additiv](#additive) kan du måla transparens direkt med svart färg.

### Opacitet {#opacity}
Hur solitt eller ogenomskinligt ett objekt ser ut; 100% är solitt, 0% är genomskinligt. Reglaget visas för typerna Blandning, Additiv, Dithering och Skuggfångare. Du kan också måla opacitet för finare kontroll.

### Förbrytningspass {#pre-refract-pass}
Bara Blandning och Additiv. Ritar det här genomskinliga objektet före brytningspasset. Användbart när ett brytande objekt står framför andra genomskinliga ytor.

### Reflekterande förmåga {#reflectance}
Styr hur mycket reflektion materialet får för icke-metalliska material. För det mesta bör standardvärdet användas (som motsvarar standardvärdet 4% reflekterat ljus vid vinkelrät infallsvinkel), men det kan ökas för att förstärka reflektioner och högdagrar i en figurs ögon, till exempel. Det kräver skuggningsläget PBR.

### ![](/icons/culling.webp) Omvänd rensning {#inverse-culling}
Vänder normalerna på en yta. Behövs oftast inte, men kan användas om en modell ser ut att vara ut-och-in, eller tillsammans med avaktiverat `Två sidor` för att göra interiörer där väggen närmast kameran alltid är dold.

Följande alternativ kan ställas in på `Auto`, `Nej` eller `Ja`. Med `Auto` visar pilen vilket värde som faktiskt används.

### ![](/icons/sphere_smooth.webp) Jämn skuggning {#smooth-shading}
Se det [globala alternativet](settings.md#smooth-shading).  
Värdet `Auto` använder det globala alternativet.

### ![](/icons/culling.webp) Två sidor {#two-sided}
Ytorna syns från båda sidor. Se det [globala alternativet](settings.md#two-sided-quick).  
Värdet `Auto` använder det globala alternativet.

### ![](/icons/culling.webp) Färgad baksida {#coloured-backface}
Se det [globala alternativet](settings.md#two-sided-quick).
Värdet `Auto` använder det globala alternativet.

### ![](/icons/shadow_cast.webp) Kasta skuggor {#casts-shadows}
Genomskinliga objekt kastar också skuggor (i ett ditheringmönster som efterliknar blandade skuggor).  
Se till att stänga av skuggkastning om du har ett stort objekt i scenen som inte behöver kasta skuggor (till exempel ett stort golv).

### ![](/icons/shadow_receive.webp) Ta emot skuggor {#recieve-shadows}
Om skuggor från andra objekt ritas på det här objektet.

### ![](/icons/wireframe.webp) Wireframe {#wireframe}
Se det [globala alternativet](settings.md#wireframe).  
Värdet `Auto` använder det globala alternativet.

### ![](/icons/trash.webp) Återställ normaler {#reset-normals}
Visas bara när ett importerat objekt har egna normaler (till exempel med `Behåll topologi`). Det tar bort dem, så att skuggningen använder normalerna som räknas ut från ytan.


## Texturer {#textures}

![](/images/material_textures.webp)

Om ett objekt har UV kan texturer kopplas till materialet utöver vertexfärg/grovhet/metallitet/opacitet. Oftast är de resultatet av en texturbakning, men bilder som skapats utanför Nomad kan också användas. `UV:✓` eller `UV:✗` bredvid rubriken visar om objektet har UV.

Texturer kan kopplas till

* Färg
* Normal
* Grovhet
* Metallitet
* Opacitet
* Förskjutning
* Emissiv

En rad `Ocklusion` visas också när ett importerat objekt har en ocklusionstextur, men Nomad använder den inte.

Reglaget på varje rad ställer in hur starkt dess textur tillämpas, från inte alls till fullt. `Färg` och `Emissiv` har också en färgruta som tonar texturen, och `Emissiv` ställer in hur starkt den lyser.

`Förskjutning` ställer in hur långt förskjutningskartan trycker ut ytan. Dess knapp `Tillämpa` flyttar vertexarna med förskjutningen och tar sedan bort kartan. Resultatet hamnar i det aktiva lagret.

Palettknappen bredvid rubriken öppnar materialförinställningarna i menyn [målning](painting.md): tryck på en för att kopiera dess texturer till objektet. På datorn synkroniseras importerade bilder med originalfilen när du växlar tillbaka till Nomad, och en synkroniseringsknapp bredvid rubriken laddar om dem.

Om du klickar på en texturplats öppnas en väljare. När en textur har kopplats till en materialplats öppnar ett nytt klick en texturpanel:

### Alternativ i texturpanelen {#texture-panel-options}

![](/images/material_texture_panel.webp)

Panelen visar bildens storlek och en förhandsvisning av texturen.

### ![](/icons/open.webp) Öppna {#open}
Välj en annan textur. På datorn visar `Utforska` bildfilen i din filhanterare.

### ![](/icons/circle_cross.webp) Ingen {#none}
Ta bort texturen

### Opacitet {#texture-opacity}

Bara färgtextur. Om bilden har en alfakanal kan du här använda den för opaciteten, eller ignorera den.

### Normalformat {#normal-format}
Bara normaltextur. Normalkartor finns i två varianter, `OpenGL (+Y)` och `DirectX (-Y)`. Om detaljerna ser inverterade ut, prova den andra.

### Höjd {#displacement-height}
Bara förskjutningstextur.
* `Lokal` - Höjden växer och krymper med objektets skala.
* `Värld` - Höjden förblir densamma oavsett objektets skala.

### Multiplicera {#multiply}
Bara texturer för grovhet, metallitet och opacitet. Multiplicerar texturens värden. När den inte är 100% visas värdet på texturplatsen.

### ![](/icons/link.webp) Kedje-/länkikon {#chainlink-icon}

När länkikonen i följande avsnitt är aktiverad delas de alternativ du använder med de andra texturerna (färg, normal, grovhet, metallitet, opacitet, emissiv) som också har sin länkikon aktiverad.

På så sätt kan du se till att texturer som är i linje med varandra förblir det, även när du ändrar parametrar eller projektionstyper.


### Projektion {#projection}
![](/images/material_projection.webp)

Ställ in hur texturen ska läggas på objektet.

* `Auto` - UV om objektet har UV, annars Triplanar
* `UV` - Använd nätets UV-koordinater för att lägga på texturen. Om nätet och texturen kommer från andra program än Nomad, eller ska exporteras från Nomad för att användas någon annanstans, är UV rätt alternativ.
* `Triplanar` - Projicera texturen längs X-, Y- och Z-axlarna och blanda skarvarna.

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanara projektioner är ett kraftfullt men enkelt sätt att lägga texturer på objekt.

Triplanar är som att ha 6 projektorer med samma bild, som lyser på objektets framsida, baksida, vänster och höger sida, ovansida och undersida.

Det kan sedan bakas in i UV eller vertexfärger vid behov.


![](/images/material_triplanar_example.webp)

#### Metod {#method}

* `Lokal` - Projektionen följer med objektets transformation
* `Värld` - Projektionerna står still: om du flyttar objektet glider det genom projektionen.

#### Hårdhet {#hardness}

Hur projektionerna blandas. 100% blandar inte alls, och projektionernas kanter blir skarpa. 0% blandar kanterna över en bred vinkel. Standardvärdet är 90%, tillräckligt mycket blandning för att dölja kanterna medan resten av projektionerna förblir skarpa.

### Enhetlig {#uniform}

När den är ikryssad används samma hårdhet för alla projektioner. När den inte är ikryssad visas extra hårdhetskontroller för projektionerna X, Y och Z.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filtrering {#filtering}
Vilken metod för texturfiltrering som ska användas. `Auto` är standard, metoderna är `Närmaste`, `Linjär` och `Mipmap`. Närmaste filtrerar inte alls, så texturer kan få taggiga artefakter när man ser dem på nära håll. Linjär och Mipmap filtrerar bättre, så texturer ser suddiga i stället för taggiga ut på nära håll.

#### Tile - X {#tiling-x}
Om parametern Skala är större än 1, så att texturen blir mindre än objektets UV, bestämmer det här hur texturen upprepas längs X-axeln. `Ingen` betyder inga upprepningar. `Upprepa` gör kopior av texturen. `Spegel` gör kopior av texturen där varannan kopia är spegelvänd, vilket kan hjälpa till att dölja upprepningsartefakter.

#### Tile - Y {#tiling-y}
Samma som Tile - X, men för Y-axeln.

### Transformera {#transform}
![](/images/material_transform.webp)

Extra 2d-transformationer som tillämpas på texturen i UV-rummet. Återställningsknappen återställer standardvärdena, och kedjeikonen (när andra texturer än färg är valda) länkar eller avlänkar transformationen så att den är densamma som färgtexturens.

#### Förflyttning {#translation}
Texturens förskjutning i X och Y

#### Rotation {#rotation}
Texturens rotation

#### Skala {#scale}
Texturens skala: större tal gör texturen mindre på objektet. Använd alternativen Tile - X och Tile - Y för att styra vad som händer.

### Jamförd skala {#uniform-scale}
När den är avstängd visar Nomad separata kontroller för Skala-X och Skala-Y.
