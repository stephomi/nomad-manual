# ![](/icons/brush.webp) Penseldrag {#stroke}

---
![](/images/stroke_overview.webp) 

## Översikt {#overview}

Du kan anpassa hur penseldraget beter sig för de flesta verktyg.
Inställningarna liknar dem du hittar i 2d-målarprogram, men en del alternativ är specifika för skulptering och 3d.

Alternativen är uppdelade på 5 undermenyer:

| Namn     | Ikon                         | Beskrivning                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Penseldrag | ![](/icons/brush.webp)      | Styr hur penseldraget läggs på modellen                   |
| Alpha    | ![](/icons/alpha.webp)      | Hur en gråskaletextur används som penselns stämpel               |
| Avmattning  | ![](/icons/falloff.webp)    | Styr hur penselns styrka ändras från mitten ut mot kanten |
| Filter   | ![](/icons/filter.webp)     | Hur penseln påverkas av modellens geometri                    |
| Tryck | ![](/icons/pressure.webp)   | Styr hur penseln reagerar på pennans tryck                                   |

::: tip
Alla alternativ för penseldrag gäller inte för alla verktyg. De alternativ som det aktuella verktyget inte använder är inaktiverade eller dolda.
:::


## ![](/icons/brush.webp) Penseldrag {#stroke-1}

### ![](/icons/radius.webp) Radie {#radius}

![](/images/stroke_radius.webp)

Radieinställningarna är globala: de gäller för alla verktyg.

#### Rymd {#size}

* `Skärm` - radien anges i skärmenheter. Om du gör radien 100 pixlar bred förblir den 100 pixlar bred, oavsett om du zoomar in eller ut.
* `Värld (3D)` - radien anges i 3d-enheter. Om du till exempel skapar en sfär och gör radien lika stor som sfären, behåller radien samma storlek som sfären när du zoomar in och ut.

#### ![](/icons/link.webp) Synka genväg {#sync-shortcut}

När det här är aktiverat hålls inställningarna för radie och silhuett synkroniserade när du byter till genvägspenslarna (`Jämna ut`, `Mask` eller `Dölj`). På så sätt använder en snabb utjämning eller maskering samma penselstorlek som verktyget du arbetade med.

#### ![](/icons/link.webp) Dela radie {#share-radius}

När det här är aktiverat använder alla verktyg samma radie. Som standard har varje verktyg sin egen radie.


### Typ av penseldrag {#stroke-type}

![](/images/stroke_strokemode.webp)

Penseldrag kan fungera på flera sätt:

### ![](/icons/stroke_dot.webp) Punkt {#dot}
Dra som med ett vanligt penseldrag.
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rulla {#roll}
Penselns alfa roteras för att följa penseldragets riktning, användbart för att göra stygn i tyg.
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Lås + radie {#lock-radius}
Stämpla ett penseldrag med fast **_höjd_**. Genom att dra ställer du in skala och rotation.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Lås + intensitet {#lock-intensity}
Stämpla ett penseldrag med fast **_radie_**. Genom att dra ställer du in höjd och rotation.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Lägena `Lås + radie` och `Lås + intensitet` bortser från inställningarna under [Tryck](#pressure), eftersom dragningen redan bestämmer storlek och styrka.
:::

![](/images/stroke_strokemodemove.webp)

Verktygen `Flytta` och `Dra` har sina egna 3 alternativ:

### ![](/icons/snake.webp) Dra {#drag}

Uppdaterar hela tiden det som finns inom penselns radie under draget. Ett snabbt drag lämnar ytan efter sig, medan ett långsamt drag håller kvar materialet och ger längre former. Det här är standardläget för verktyget `Dra`. Med `Dynamisk topologi` kan du använda det för att göra ormliknande utdragningar.
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Greppa {#grab}
Väljer det som finns inom penselns radie när draget börjar och håller fast vid det valet. Det är användbart för mer exakta förflyttningar, eftersom du kan justera hur långt du flyttar utan att råka flytta mer än du valde från början. Det här är standardläget för verktyget `Flytta`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lås + radie (dra) {#lock-radius-drag}
Den radie du har ställt in ignoreras, och radien bestäms i stället av hur långt du drar från startpunkten. Kort avstånd ger liten radie, längre avstånd ger större radie. Använd intensitetsreglaget för att styra avmattningens form. Användbart för att blocka ut organiska, gummiaktiga former.
![](/videos/stroke_lockradius_drag.mp4) 

En del andra verktyg visar sina egna typer av penseldrag här, till exempel `Slappna av`, `Jämna ut` och `Smeta ut` för utjämningsverktygen, eller former som `Lasso` och `Kurva` för de markeringsbaserade verktygen. De beskrivs under respektive [verktyg](tools.md).


### Justera avståndsintensitet {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Penseldrag med litet avstånd (under 50 %) kan byggas upp snabbt och bli kraftigare än penseldrag med större avstånd. Det här alternativet kompenserar för det, så att penseldragen får ungefär samma intensitet oavsett avstånd.

### Penseldragsavstånd {#stroke-spacing}
Hur långt isär varje penselstämpel läggs när du drar. Värden under 100 % överlappar och ger intrycket av ett sammanhängande penseldrag. Värden över 100 % börjar lämna mellanrum, vilket är användbart för detaljer som stygn eller blixtlås.

### Slö repsstabilisator {#lazy-rope-stabilizer}
Penseldraget släpar efter pekaren med ett visst avstånd. Det kan användas för att rita mjuka linjer.
![](/videos/stroke_lazy_rope.mp4) 

### Penselslätning {#stroke-smoothing}
Tar medelvärdet av flera pekarpositioner för att få ett jämnare penseldrag.
Med höga värden släpar penseldraget efter pekaren, men kommer till slut ikapp.
Det är användbart för att rita mjuka linjer.

### Fäst radie {#snap-radius}
Fäster penseldraget vid det föregående när pekaren börjar nära där det senaste penseldraget slutade. Radien bestämmer hur långt bort Nomad letar efter slutet på det föregående penseldraget. Det kan vara användbart när du ritar långa sammanhängande linjer och ofta pausar.

### ![](/icons/trail.webp) Spårning bakom penseldraget {#trail}

När det här är aktiverat lägger varje ny stämpel också på nytt de senaste punkterna i penseldraget bakom den. `Antal spår` anger hur många punkter som läggs på igen, `Spårintensitet` hur starka de är och `Spårradie` hur mycket större de blir.

Spårningen fungerar bara med penseldragstypen `Punkt`, och inte med [påverkan](#influence) `Ås` för avmattningen.

### ![](/icons/silhouette.webp) Silhuett {#silhouette}
![](/images/stroke_silhouette.webp)
Som standard påverkar penseldragen bara modellens yta inom penselns radie. När silhuett är aktiverat projiceras penseldraget genom hela modellen. Det kan vara mycket användbart när du blockar ut en modell i början, eller för former där sidorna ska förbli vinkelräta.

Projektionsriktningen kan anges uttryckligen:

* `X`, `Y`, `Z` - projicera längs en fast axel.
* `Visa` - projicera längs kamerans riktning.
* `Om fäst` - projicera längs kamerans riktning, men bara medan kameran är fäst vid en vy. Annars förblir det ett vanligt penseldrag.
* `Närmaste` - projicera längs den axel som ligger närmast kamerans riktning. Det här är standardvalet.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomisera {#randomize}

![](/images/stroke_randomize.webp)

Penseldragets `Intensitet`, `Förskjutning`, `Rotation` och `Skala` kan slumpas var för sig. Använd kryssrutan på en rad för att slå på eller av den. Det ger en rad olika effekter, till exempel kan slumpning med målningsverktyget ge en fläckig färg, och slumpning med veckverktyget kan användas för att skapa hudstruktur.

`Period (långsammare)` anger längden på den slumpmässiga cykeln: öka den för långsamma, böljande variationer, minska den för snabbt brus. Den lilla knappen bredvid varje rad skalar perioden för just den raden.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Randomisera - HSV {#randomize-hsv}

För verktyg som målar kan även målarfärgens `Färgton`, `Mättnad` och `Värde` slumpas, med en egen period. Perfekt för att ge hud eller sten en subtil färgvariation.

### Penseldragsförskjutning {#stroke-offset}

Lägger en konstant förskjutning på penseldraget, så att fingret inte skymmer det. Det är användbart på små skärmar. Det är en global inställning: aktivera den med dess kryssruta, så gäller den för alla verktyg.


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` är en textur som styr hur penseln beter sig.
Det är en gråskalebild, där svarta pixlar betyder ingen deformation och vita pixlar full deformation.

Klicka på alfabilden för att byta den. Förutom de inbyggda alfabilderna och dina egna importerade kan alfalistan också ladda ner förskjutningskartor (displacement maps) från Poly Haven.

Klicka på materialförhandsvisningen för att läsa in en alfa från en materialförinställning. Här kan du också spara materialförinställningar och välja att bädda in texturer i verktyget.

::: tip
Texturen skalas aldrig om, så stora texturer kan göra Nomad långsammare.
:::

### ![](/icons/blend_contrast.webp) Korrigera alfa {#invert-pixels}
Knappen `Korrigera...` på en importerad alfa öppnar ett fönster som korrigerar själva bilden: dess mellanvärde, inverterade pixlar (svart blir vitt och vitt blir svart), en rotation på 90° och en vågrät eller lodrät vändning. Bildfilen skrivs om, så andra appar ser också den korrigerade bilden.

::: tip

De inbyggda alfabilderna som följer med Nomad kan inte korrigeras.

:::

### Projektion {#projection}

Hur alfan projiceras på modellen:

* `Yta` - alfan ligger på ytan under penseln och följer dess orientering.
* `Skärm` - alfan projiceras rakt från vyn.
* `Platta` - alfan projiceras från vyn och ligger kvar på plats medan du målar över den, som en schablon, så att ett upprepat mönster fogas ihop sömlöst. Rotationen är låst, och penntrycket ändrar inte mönstrets storlek.
* `Triplanar` - alfan projiceras längs de 3 axlarna. Alternativen för skalning, rotation och tile nedan ersätts av inställningarna för den triplanara texturen.

### ![](/icons/diagonal.webp) Skalning {#scaling}

Penseln i Nomad är en cirkel med en radie som du bestämmer. Texturer är ofta kvadratiska eller rektangulära, och parametrarna för `Skalning` låter dig bestämma hur texturen ska passa in i cirkeln. För en kvadratisk textur får den plats inuti cirkeln med värdet 0,7. Med värdet 1 skalas texturen upp så att cirkeln får plats inuti den, och kanterna klipps bort.

![](/images/alpha_scaling.webp) 

Om du aktiverar `Skalning Y` kan du sträcka alfan lodrätt. Det första reglaget blir då `Skalning X`.

![](/images/alpha_scaling_y.webp) 

`Vänd vågrätt` spegelvänder alfan från vänster till höger.

### Rotation {#rotation}

Alfatexturen roteras för att följa penseldragets riktning. Du kan lägga till en rotationsförskjutning, och om låsikonen är aktiverad förblir texturen låst i den rotationen i förhållande till skärmen.

Pennknappen bredvid roterar alfan när du vrider pennan (barrel roll), med penseldragen `Lås + radie` och `Lås + intensitet` medan rotationen är olåst. Det fungerar bara med pennor som har stöd för det.

### Tile {#tiling}
![](/images/stroke_tiling.webp) 

Hur ofta texturen upprepas inom penselns profil. Med lägena `Tile - X` och `Tile - Y` kan du begränsa till en enda textur i penseldraget (`Ingen`), upprepade texturer (`Upprepa`), eller speglade, där varannan textur vänds för att skapa mönster eller hjälpa till att göra sömlösa texturer (`Spegel`). De finns med penseldraget `Rulla`, projektionen `Platta` eller en `Tile` över 1.

`Åtsittande passform (icke fyrkantiga bilder)` spelar bara roll för alfa- och penseltexturer som inte är kvadratiska. När det är aktiverat upprepas varje bild för sig, utan mellanrum. Avaktivera det för att hålla alfan och de andra bilderna synkroniserade när deras proportioner skiljer sig åt.

![](/videos/alpha_tiling.mp4) 



### Mellanvärde {#mid-value}

Som standard betyder svarta pixlar ingen deformation och vita pixlar full positiv deformation. En lerpensel med en alfatextur av stenar drar alltså bara ut ytan där alfan inte är svart.

Om du vill att penseln ska trycka in ytan, eller både trycka in OCH dra ut den, kan du ändra mellanvärdet. Om du sätter värdet till 0,5 gör en mellangrå ton i alfan ingenting, svart trycker in och vitt drar ut.

Två knappar hjälper dig att hitta rätt värde: den fyrkantiga knappen läser mellanvärdet från bildens kant, och pipetten låter dig välja det direkt på alfan.



## ![](/icons/falloff.webp) Avmattning {#falloff}

![](/images/falloff_menu.webp) 

Det här liknar [Alpha](#alpha), förutom att du styr intensiteten med en enda kurva. Den kombineras med alfan, så att du kan använda en textur för detaljer och avmattningen för att styra hur kanten tonas ut och hur stark intensiteten är i verktygets mitt.

När kurvan ligger högst upp ger den full deformation, och när den ligger längst ner har penseln ingen effekt.

Du kan se kurvan som ett tvärsnitt genom penselns spets. Den nedre delen visar en förhandsvisning av hur en enda "stämpel" av penseln skulle se ut på modellens yta, och om penseln har en alfatextur visas den också, så att du ser hur avmattningen och alfan samverkar.

### ![](/icons/fx.webp) Förinställning {#preset}
Med `Förinställning...` valt öppnar ett klick på kurvdiagrammet en meny med förinställningar. Rundade kurvor ger mjukare resultat, kantiga kurvor skarpare resultat. Knappen `Sub` i det vänstra verktygsfältet vänder i praktiken på avmattningen, så att kurvans topp trycker in ytan i stället för att dra ut den, eller tvärtom.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
När det här är valt kan du rita dina egna avmattningskurvor. Kurvredigeraren fungerar likadant som kurvor i resten av Nomad:

* Klicka på kurvan för att skapa en ny punkt
* Dra en punkt för att flytta den
* Klicka på en punkt för att växla mellan skarp och mjuk
* Dra en punkt in i en granne för att ta bort den

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
När det här är valt kan du rita dina egna avmattningskurvor. Redigeraren fungerar som med Catmull-Rom, men kurvpunkterna påverkar kurvan i stället för att ligga direkt på den, vilket kan hjälpa dig att skapa mjukare kurvformer.

### ![](/icons/curve_bevel.webp) Fasning {#bevel}
Punkterna förbinds med raka linjer, med rundade hörn vars storlek beror på varje punkts skärpa. Praktiskt för penslar med platt topp och en ren fasning vid kanten.

Kurvredigeraren har 3 knappar:

| Objekt     | Ikon                        | Beskrivning                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximera | ![](/icons/maximize.webp)  | Förstora kurvredigeraren                      |
| Återställ    | ![](/icons/reset.webp)     | Återställ kurvan till standardläget        |
| Symmetri | ![](/icons/symmetric.webp) | Visa kurvan som en symmetrisk "penselspets" |


### Påverkan {#influence}

* `Sfär` (3d) - Påverkan beräknas utifrån avståndet från vertexen till penselns mitt.
* `Cirkel` (2d) - Vertexen projiceras först på områdets plan, innan avståndet till penselns mitt mäts. Det liknar hur alfor samplas.
* `Cylinder` - Påverkan projiceras genom området som en cylinder. Det är samma sak som att aktivera [Silhuett](#silhouette-1) nedan.
* `Ås` - Avmattningen mäts tvärs över penseldraget, så kurvan blir tvärsnittet av hela penseldraget. Knappen `Sym` speglar då profilen över penseldraget: redigera ena sidan så följer den andra med. När den är avstängd går kurvan från penseldragets vänstra sida till dess högra. Finns inte för de utplattningsbaserade verktygen.

### ![](/icons/silhouette.webp) Silhuett {#silhouette-1}
Som standard påverkar penseldragen bara modellens yta inom penselns radie. När silhuett är aktiverat projiceras penseldraget genom hela modellen. Det kan vara mycket användbart när du blockar ut en modell i början, eller för former där sidorna ska förbli vinkelräta. Den har samma projektionsalternativ som [Silhuett](#silhouette) under fliken Penseldrag.



## ![](/icons/filter.webp) Filter {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Akkumulera penseldrag {#accumulate-stroke}
Tar bort gränsen för hur mycket material som kan läggas till eller tas bort per penseldrag. Verktyget `Lera` har till exempel detta aktiverat, så att materialet kan fortsätta byggas upp, medan verktyget `Pensel` har det avaktiverat, så att penseldraget slutar lägga till material om du fortsätter att dra över samma område av meshen.

### ![](/icons/culling.webp) Endast framåtvända vertex {#front-facing-vertex-only}
Det här alternativet ignorerar bakåtvända vertices.
Det kan vara användbart om du vill måla en del av en tunn geometri utan att påverka andra sidan.
Det fungerar också vid skulptering, men du kan få en del artefakter.

### ![](/icons/eye_open.webp) Endast synliga vertices {#visible-vertex-only}
Ignorerar vertices som döljs bakom andra ytor, sett från kameran. Det här alternativet visas för formbaserade penseldrag (lasso, rektangel...) i maskerings- och målningsverktygen samt verktygen `Ytgrupp` och `Dölj`.

### ![](/icons/dynamic.webp) Tillåt dynamisk topologi {#allow-dynamic-topology}
Det här alternativet finns bara om din mesh är i läget [Dynamisk topologi](topology.md#dynamic-topology). Du kan aktivera eller avaktivera dynamisk topologi per verktyg.

### ![](/icons/connect.webp) Ansluten topologi {#connected-topology}
Skulpterar bara de vertices som hänger ihop med ytan du rör vid med verktyget. Med verktyget `Flytta` kan du till exempel flytta en del även om den skär igenom en annan del.
![](/videos/connected_topology.mp4)

### Skyddsområde {#protect-area}
![](/images/filter_protect_area.webp) 

De här alternativen hindrar verktygen från att påverka delar av meshen under olika förhållanden. Var och en kan ställas in på `Auto`, `Nej` eller `Ja`, och den lilla pilen visar vad `Auto` motsvarar just nu.

* `Dölj` - Om delar av meshen är dolda med döljverktyget, ställ in om de ska skyddas. Med `Auto` skyddas dolda ytor, om inte deras wireframe är synlig (se inställningarna för [Wireframe](settings.md#wireframe)).
* `Mask` - Om delar av meshen är maskerade, ställ in om de ska skyddas. Med `Auto` skyddas maskerade delar så länge masken är synlig i menyn [Skuggning](shading).
* `Ytgrupp` - Ställ in om du bara kan använda ett verktyg inom den första ytgruppen du rör vid. Med `Auto` följer det om ytgrupperna är synliga i menyn [Skuggning](shading).

Knappen `(Alla)` anger om skydden är globala, delade av alla verktyg, eller inställda per verktyg.


### Områdesprovtagning {#area-sampling}
En del penslar eller alternativ för penseldrag behöver ett plan, med en normal och en position, mot ytan för att fungera.

Du kan styra hur det här genomsnittsplanet beräknas genom att ange provtagningsområdet som en andel av verktygets radie.

Vid 100 % räknas varje punkt inuti markeringscirkeln med.

Vid 0 % räknas bara den närmaste vertexen eller triangeln med. Värdena kan länkas för både `Normalradie` och `Positionsradie`, eller låsas upp och ställas in var för sig.

### Områdes-normalfilter {#keep-sharp-edges}
Utesluter punkter vars normaler avviker för mycket från ytans normal.

Det ändrar hur planet beräknas (Områdesprovtagning), så det är mest användbart för ler- eller utplattningsbaserade verktyg, eller om du vill färglägga en mestadels plan yta utan att färgen spiller över.

Vinklarna `Min` och `Max` styr övergången mellan uteslutna och helt påverkade punkter, som den lilla färgade skivan bredvid dem visar.

![](/videos/filter_keep_sharp_edges.mp4)

### Avtonings-normalfilter {#falloff-normal-filter}
Precis som [Områdes-normalfilter](#keep-sharp-edges) utesluter det punkter vars normaler avviker för mycket från ytans normal, men det verkar på penselns avmattning i stället för på planberäkningen. Det är användbart för att måla veck eller upphöjningar.


### Djupmaskering {#depth-masking}
![](/images/stroke_depthmask.webp)

Utesluter punkter som ligger över eller under ett visst avstånd från det beräknade planet (Områdesprovtagning).

Det kan användas för att bara måla på upphöjda partier, eller bara i fördjupningar.

Diagrammet visar ett tvärsnitt av ytan: den vågräta linjen är där ytan ligger, och cirkeln visar målningens avmattningsradie ovanför och under ytan. `Höjdkompensation` är en procentandel ovanför eller under ytan där maskeringsberäkningen börjar. Med `Djupavmattning` aktiverat kan du med `Övre området` och `Nedre området` skala avmattningen ovanför och under förskjutningspunkten.

#### Exempel: Måla i fördjupningar {#example-paint-in-cavities}
För att bara måla i fördjupningar, sätt höjdkompensationen till -100 % och justera reglaget för det övre området så att det ligger en bit från den vågräta linjen. Det betyder att det första klicket bestämmer "noll"-djupet, och därefter påverkas bara områden under det djupet.

![](/videos/stroke_depth_cavity.mp4)

#### Exempel: Måla på upphöjningar {#example-paint-on-bumps}
För att bara måla på höga partier, sätt höjdkompensationen till +90 %, så att cirkelns underkant skär den vågräta linjen en liten bit. När du klickar på toppen av en "hög" zon bestäms djupet, så att allt på det djupet, plus lite under det, och allt som ligger högre målas. Djupa fördjupningar hoppas över.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Tryck {#pressure}
![](/images/pressure_menu.webp) 

Styr hur pennans tryck påverkar penslarna.

### Använd globala inställningar {#use-global-settings}

Som standard är `Använd globala inställningar` aktiverat, vilket betyder att alla penslar delar samma tryckvärden. Avmarkera det för att ge det aktuella verktyget egna tryckinställningar.

### ![](/icons/radius.webp) Radie {#pressure-radius}

Den här kurvan styr hur penselns radie påverkas av trycket. Standard är ett linjärt förhållande, så om din penna har en jämn respons bör även radieändringen kännas jämn. Många pennor har dock en icke-linjär respons, som du kan kompensera för med den här kurvan. Om radien till exempel inte känns som att den når sitt maxvärde vid högt tryck, använd en förinställd kurva som "out-pow3", med en böj uppåt, så att radien ökar tidigare.

Den här dialogen liknar visningen av avmattningskurvan: du kan använda en förinställning genom att trycka i kurvfönstret, eller rita dina egna kurvor med lägena `Catmull-Rom`, `B-spline` och `Fasning`.

Om du vill ha konstant radie, avaktivera den här sektionen.

### ![](/icons/intensity.webp) Intensitet {#pressure-intensity}

Fungerar som radiekurvan, men styr intensiteten. Om du vill ha konstant intensitet, avaktivera den här sektionen.

### Begränsa trycket till 100% {#limit-pressure}

Ser till att pennans tryck aldrig går över 100 %. Det här är en global inställning.

### Tryckutjämning {#pressure-smoothing}

Tar medelvärdet av pennans tryckhändelser för jämnare resultat.
