# ![](/icons/pencil.webp) Penseldrag {#stroke}

---
![](/images/stroke_overview.webp) 

## Översikt {#overview}

Du kan anpassa streckbeteendet för de flesta verktygspenslar.
Inställningarna liknar de som finns i 2D-målningsprogram, men vissa alternativ är specifika för skulptering och 3D.

Alternativen är uppdelade i 5 undermenyer:

| Namn     | Ikon                         | Beskrivning                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Styr hur strecket appliceras på modellen                           |
| Alpha    | ![](/icons/alpha.webp)      | Hur en gråskaletextur används för penselstämpeln                   |
| Falloff  | ![](/icons/falloff.webp)    | Styr hur penselstyrkan ändras från mitten till kanten              |
| Filter   | ![](/icons/filter.webp)     | Hur penseln påverkas av modellens geometri                         |
| Pressure | ![](/icons/pressure.webp)   | Styr responsen på penntablettens tryck                             |

::: tip
Alla streckalternativ gäller inte för alla verktyg. Streckalternativ som inte används av det aktuella verktyget kommer att inaktiveras eller döljas. 
:::


## Penseldrag {#stroke-1}

### Radie {#radius}

![](/images/stroke_radius.webp)

#### Dela radie {#share-radius}

När detta är aktiverat kommer alla verktyg att använda samma radie, standardläget är att varje verktyg har sin egen radie.

#### Storlek {#size}

* Skärm - radien anges i skärmenheter. Om du gör radien 100 pixlar bred kommer den att förbli 100 pixlar bred oavsett om du zoomar in eller ut.
* Konstant (3D) - radien anges i 3D-enheter. Om du till exempel skapar en sfär och gör radien lika stor som sfären, kommer radien att förbli lika stor som sfären när du zoomar in och ut.


### Penseldrag {#stroke-type}

![](/images/stroke_strokemode.webp)

Streck kan fungera i flera lägen:

### ![](/icons/stroke_dot.webp) Punkt {#dot}
Dra som ett vanligt målarstreck. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rulla {#roll}
Penselns alpha roteras för att följa streckets riktning, användbart för att göra tygstygn. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lås + radie
 Stämpla ett penseldrag med fast **_höjd_**. Drag bestämmer skala och rotation.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lås + intensitet {#lock-intensity}
Stämpla ett penseldrag med fast **_radie_**. Drag bestämmer höjd och rotation.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Verktygen `Move` och `Drag` har sina egna 3 alternativ:

### ![](/icons/snake.webp) Dra {#drag}

Kommer att fortsätta uppdatera det som finns inom penselradien under strecket. Ett snabbt streck lämnar ytan bakom sig, medan ett långsamt streck håller fast vid materialet och skapar längre former. Detta är standardläget för verktyget `Drag`. Med `Dynamic Topology` kan detta användas för att göra ormliknande extruderingar. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Greppa {#grab}
Kommer att välja det som finns inom penselradien när penseln startas, och behålla det urvalet. Detta är användbart för mer precisa förflyttningar, eftersom du noggrant kan justera flyttavståndet utan att oavsiktligt flytta mer än du ursprungligen valde. Detta är standardläget för verktyget `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lås + radie (dra) {#lock-radius-drag}
Användarens radie ignoreras och ställs in dynamiskt baserat på hur långt strecket dras bort från startpunkten. Kort avstånd = liten radie, längre avstånd = större radie. Använd intensitetsreglaget för att styra falloff-formen. Användbart för att blocka upp organiska, gummiaktiga former.
![](/videos/stroke_lockradius_drag.mp4) 



### Justera mellanrummets intensitet {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Streck med litet mellanrum (lägre än 50 %) kan snabbt ackumuleras och ge mer intensiva streck än högre värden. Denna växel kompenserar för detta, så att streck får ungefär samma intensitet oavsett mellanrum.

### Penseldragets mellanrum {#stroke-spacing}
Hur långt ifrån varandra varje penselstämpel appliceras under en dragning. Värden under 100 % överlappar, vilket ger intrycket av ett kontinuerligt streck. Värden över 100 % börjar lämna mellanrum, användbart för att skulptera detaljer som sömmar eller dragkedjor.

### Tröghetsstabilisator (rep) {#lazy-rope-stabilizer}
Streck kommer att släpa efter pekarens position med ett visst avstånd. Detta kan användas för att rita mjuka linjer.
![](/videos/stroke_lazy_rope.mp4) 

### Penseldragets utjämning {#stroke-smoothing}
Medelvärdesbildar flera pekarpositioner för att få ett mjukare streck.
Vid höga värden släpar strecket efter pekaren men kommer så småningom ikapp.
Detta är användbart för att rita mjuka linjer.

### Fånga radie {#snap-radius}
Snäpper början av strecket till slutet av föregående streck. Radien avgör hur långt man letar efter slutet på föregående streck. Detta kan vara användbart när du ritar långa kontinuerliga linjer men gör frekventa pauser.

### ![](/icons/silhouette.webp) Siluett {#silhouette}
![](/images/stroke_silhouette.webp)
Som standard påverkar streck bara modellens yta inom penselradien. När silhuett är aktiverat projiceras strecket genom hela modellen. Detta kan vara mycket användbart vid den första blockningen av en modell, eller för former där sidorna måste förbli vinkelräta.

Projekteringsriktningen kan ställas in explicit, standardmetoden ”Closest” kommer att hitta den bästa vinkeln relativt vyn. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) Slumpa {#randomize}

![](/images/stroke_randomize.webp)

Intensitet, förskjutning, rotation och skala för strecket kan var och en slumpas. Detta kan användas för att skapa en rad effekter, t.ex. kan randomisering med målarverktyget skapa fläckiga färger, eller randomisering med crease-verktyget användas för att skapa huddeta ljer.

![](/videos/stroke_randomize.mp4) 

### Penseldragsoffset {#stroke-offset}

Applicera en konstant förskjutning på strecket. Detta är användbart på små skärmar där ditt finger skulle täcka strecket. 


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` är en textur som modulerar ditt penselbeteende.
Det är en gråskale-bild där svarta pixlar betyder ingen deformation och vita pixlar full deformation.

Klicka på alpha-bilden för att ändra den.

Klicka på materialförhandsvisningen för att ladda en alpha från en materialpreset. Du kan också spara materialpresets här och välja att bädda in texturer med verktyget.

::: tip
Texturen ändrar aldrig storlek, så stora texturer kan försämra prestandan.
:::

### Invertera pixlar {#invert-pixels}
Detta vänder bildens värden, så att svarta pixlar blir vita och vita pixlar blir svarta.

::: tip

De inbyggda alphas som levereras med Nomad kan inte inverteras.

:::

### Skalning {#scaling}

Penselstorleken i Nomad är en cirkel med en användardefinierad radie. Texturer är ofta kvadratiska eller rektangulära, parametrarna för `Scaling` låter dig bestämma hur texturen ska passa in i cirkeln. För en kvadratisk textur kommer ett värde på 0,7 att få plats i cirkeln. Ett värde på 1 skalar texturen större så att cirkeln får plats inuti, vilket klipper kanterna.

![](/images/alpha_scaling.webp) 

Om du aktiverar `Scaling - Y` kan du sträcka alpha vertikalt.

![](/images/alpha_scaling_y.webp) 

### Rotation {#rotation}

Alpha-texturen roteras för att följa streckets riktning. Du kan lägga till en rotationsförskjutning, och om låsikonen är aktiverad kommer texturen att förbli låst till denna rotation relativt skärmen.

### Upprepning {#tiling}
![](/images/stroke_tiling.webp) 

Hur ofta texturen upprepas inom penselprofilen. Tiling-lägena låter dig begränsa till en enda textur inom strecket, eller upprepade texturer, eller speglade där varannan textur vänds för att skapa mönster eller hjälpa till att göra sömlösa texturer.

![](/videos/alpha_tiling.mp4) 



### Mellanvärde {#mid-value}

Som standard betyder svarta pixlar ingen deformation och vita pixlar full positiv deformation, så till exempel kommer en clay-pensel med en alpha-textur av stenar bara att dra ut ytan där alphan inte är svart.

Om du vill att penseln ska trycka in ytan, eller både trycka in OCH dra ut, kan du ändra mittvärdet. Om du till exempel ställer in värdet på 0,5 kommer en mellangrå i alphan inte göra något, ett svart värde trycker in, vitt drar ut.




## Avtoning {#falloff}

![](/images/falloff_menu.webp) 

Detta liknar [Alpha](#alpha), förutom att du styr intensiteten med en enda kurva. Detta kombineras med alphan så att du kan använda en textur för detalj och falloff för att styra kanttoning och intensitet i mitten av verktyget.

När kurvan är högst upp är detta full deformation, när den är längst ner har penseln ingen effekt.

Du kan tänka på kurvan som ett tvärsnitt genom penselspetsen. Den nedre delen ger en förhandsvisning av hur en enskild ”stämpel” av penseln skulle se ut på modellytan, och om det finns en alpha-textur för penseln visas den också för att förhandsgranska hur falloff och alpha samverkar.

### Förinställning {#preset}
Med detta valt kommer ett klick på kurvdiagrammet att visa en meny med presets. Rundade kurvor ger mjukare resultat, kantiga kurvor ger skarpare resultat. Knappen `Sub` i vänster verktygsfält vänder i praktiken falloffen, så att toppen av kurvan trycker in i ytan istället för att dra ut, eller tvärtom.

### Catmull-Rom {#catmull-rom}
När detta är valt kan användaren rita egna falloff-kurvor. Kurvredigeraren fungerar på samma sätt som kurvor i resten av Nomad:

* Klicka på kurvan för att skapa en ny punkt
* Dra en punkt för att flytta den
* Klicka på en punkt för att växla mellan skarp och mjuk
* Dra en punkt in i en grannpunkt för att ta bort den

### B-spline {#b-spline}
När detta är valt kan användaren rita egna falloff-kurvor. Editorn fungerar på samma sätt som Catmull-Rom, men kurvpunkterna påverkar kurvan istället för att ligga direkt på den, vilket kan hjälpa till att skapa mjukare kurvformer.

Kurvredigeraren har 3 knappar:

| Objekt   | Ikon                        | Beskrivning                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Expandera kurvredigeraren                    |
| Reset    | ![](/icons/reset.webp)     | Återställ kurvan till standardläget          |
| Symmetry | ![](/icons/symmetric.webp) | Visa kurvan som en symmetrisk ”penselspets”  |


### Inverkan {#influence}

* Sfär (3D) - Påverkan beräknas genom att ta avståndet från vertex till penselns centrum.
* Cirkel (2D) - Vertex projiceras först på ytplanet innan dess avstånd till penselns centrum tas. Detta liknar hur alphas samplas. 
* Cylinder - Påverkan projiceras genom ytan som en cylinder, används av Silhouette-läget nedan.

### Siluett {#silhouette-1}
Som standard påverkar streck bara modellens yta inom penselradien. När silhuett är aktiverat projiceras strecket genom hela modellen. Detta kan vara mycket användbart vid den första blockningen av en modell, eller för former där sidorna måste förbli vinkelräta.



## Filter {#filter}

![](/images/filter_menu.webp) 

### Ackumulera penseldrag {#accumulate-stroke}
Aktivera obegränsad mängd material som kan läggas till/tas bort per streck. T.ex. har verktyget `Clay` detta aktiverat, så material kan fortsätta byggas upp, medan verktyget `Brush` har detta inaktiverat, så streck slutar lägga till material om du fortsätter dra samma streck över samma område på meshen. 

### Endast framåtvända verticer {#front-facing-vertex-only}
Detta alternativ ignorerar bakåtvända vertexar.
Det kan vara användbart om du vill måla en del av en tunn geometri utan att påverka andra sidan.
Det fungerar också för skulptering men du kan uppleva vissa artefakter.

### Tillåt dynamisk topologi {#allow-dynamic-topology}
Detta alternativ är endast tillgängligt om din mesh är i läget [Dynamic Topology](topology.md#dynamic-topology). Du kan inaktivera eller aktivera dynamisk topologi per verktyg.

### Sammanhängande topologi {#connected-topology}
Aktivera så att endast vertexar som är länkade till ytan du rör vid med verktyget skulpteras. Till exempel, när det används med verktyget `Move`, låter detta dig flytta en del även om den skär igenom en annan del.
![](/videos/connected_topology.mp4)

### Skydda område {#protect-area}
![](/images/filter_protect_area.webp) 

Dessa alternativ stoppar verktyg från att påverka delar av din mesh under olika villkor. 

Alternativet ”Auto” betyder att om du har hide, mask eller facegroup synlig i menyn [Shading](shading) kommer de att skyddas, men om de är avstängda i den menyn är skyddet inaktiverat.

* `All` - Växla för att ställa in om skyddsfiltren är globala eller per verktyg.
* `Hide` - Om delar av meshen är dolda med hide-verktyget, ställ in om de ska skyddas.
* `Mask` - Om delar av meshen är maskade, ställ in om de ska skyddas.
* `Facegroup` - Ställ in om du bara kan använda ett verktyg inom den först berörda facegruppen.


### Behåll skarpa kanter {#keep-sharp-edges}
Exkludera punkter vars normaler skiljer sig för mycket från ytnormalen.

Detta ändrar hur ytplaneområdet beräknas (Area sampling).

Detta alternativ kan vara användbart för flatten-baserade verktyg, eller om du vill färgsätta en mestadels platt yta utan överspill.

![](/videos/filter_keep_sharp_edges.mp4)

### Områdessampling {#area-sampling}
Vissa penslar eller streckalternativ kräver en planet normal och en planposition mot ytan för att fungera.

Du kan styra hur detta genomsnittliga plan beräknas genom att ställa in samplingsområdet som en andel av verktygsradien.

Vid 100 % tas varje punkt inom markeringscirkeln med i beräkningen.

Vid 0 % tas endast närmaste vertex eller triangel med i beräkningen. Dessa värden kan länkas för både `Normal radius` och `Position radius`, eller låsas upp och ställas in oberoende.


### Djupmaskning {#depth-masking}
![](/images/stroke_depthmask.webp)

Exkludera punkter som ligger över eller under ett visst avstånd från det beräknade planet (Area sampling).

Detta kan användas för att måla endast på buckliga områden, eller endast i håligheter.

Grafen representerar ett tvärsnitt av ytan; den horisontella linjen är där ytan är, cirkeln representerar penselns falloff-radie relativt ovanför och under ytan. `Height offset` är en procent över eller under ytan där maskningsberäkningen börjar. `Top area` och `Bottom area` låter dig skala falloff ovanför och under offset-punkten.

#### Exempel: Måla i håligheter {#example-paint-in-cavities}
För att bara måla i håligheter, ställ in height offset till -100 % och justera reglaget för top area så att det är en bit från den horisontella linjen. Detta betyder att första klicket sätter ”noll”-djupet, och sedan kommer endast områden under detta djup att påverkas.

![](/videos/stroke_depth_cavity.mp4)

#### Exempel: Måla på upphöjningar {#example-paint-on-bumps}
För att bara måla på höga områden, ställ in height offset till +90 %, så att cirkelns botten skär den horisontella linjen med en liten marginal. När du klickar på toppen av en ”hög” zon sätter detta djupet, så att allt på det djupet, plus lite under, och allt över, kommer att målas. Djupa håligheter hoppas över.
![](/videos/stroke_depth_bump.mp4)


## Tryck {#pressure}
![](/images/pressure_menu.webp) 

Styr hur penntablettens tryck påverkar penslarna.

Som standard är `Use global settings` aktiverat, vilket innebär att alla penslar delar samma tryckvärden.

### Tryck – Radie {#pressure-radius}

Denna kurva styr hur penselradien påverkas av tryck. Standard är ett linjärt förhållande, så om din penna har en jämn respons bör radieförändringen också kännas jämn. Många pennor har dock en icke-linjär respons, vilket du kan kompensera för med denna kurva. Om radien till exempel inte känns som att den når sitt maxvärde vid högt tryck, använd en kurv-preset som ”out-pow3”, med en böj uppåt, för att öka radien tidigare.

Denna dialog liknar falloff-kurvans visning, du kan använda en preset genom att trycka på kurvfönstret, eller rita egna kurvor med lägena Catmull-Rom och B-Spline.

Om du vill ha konstant radie, inaktivera detta avsnitt.

### Tryck – Intensitet {#pressure-intensity}

Liknar radie-kurvan, men för att styra intensitet. Om du vill ha konstant intensitet, inaktivera detta avsnitt.

### Tryckutjämning {#pressure-smoothing}

Medelvärdesbildar penntablettens tryckhändelser för mjukare resultat.