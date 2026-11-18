# ![](/icons/cog.webp) Inställningar {#reset-to-default}

Inställningsmenyn innehåller många alternativ för att styra hur Nomad ser ut och beter sig.

![](/images/settings_overview.webp)

Raden med knappar högst upp i menyn hoppar direkt till ett avsnitt: `Markör`, `Indikator`, `Tråd`, `Rutnät`, `Två sidor`, `Kontur`, `Markering`, `Snap-kub`, `Statistik`, `Handtag`, `Form`, `Repeterare` och `Multiresolution`.

## Visningsinställningar {#display-settings}
Det här avsnittet innehåller snabbgenvägar till de flesta inställningarna längre ned i menyn.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Jämn skuggning {#smooth-shading}
Växlar mellan jämn och fasetterad skuggning. Med fasetterad skuggning skuggas polygonerna var för sig, så att du ser den underliggande topologin.
Det kan vara användbart att ha fasetterad skuggning medan du skulpterar, och sedan byta till jämn skuggning för rendering.

Att stänga av jämn skuggning förbättrar prestandan lite.

### ![](/icons/outline.webp) Kontur {#outline-quick}
Slår på/av en kontur runt din nuvarande markering.

Det är användbart för att se vilka nät som är valda om [Mörka ej valda objekt](#darken-unselected-objects) är avstängt.

Prestandamässigt är [Mörka ej valda objekt](#darken-unselected-objects) mycket bättre än konturen.

### ![](/icons/grid.webp) Rutnät {#grid-quick}
Slår på/av ett rutnät i bakgrunden, användbart för att förstå objektens placering och skala.

### ![](/icons/culling.webp) Två sidor {#two-sided-quick}
Slår på/av visning av polygoner från båda sidor. Alla ytor pekar åt ett visst håll.
Ytor som räknas som *baksida* är de som pekar "bort" från kamerans synvinkel.

Till exempel pekar ytorna på den enkla startsfären utåt.
Om du flyttar in kameran i sfären ser du baksidan av de ytorna.

För det mesta ska du inte se ytornas baksida, så att färga dem kan hjälpa dig att upptäcka möjliga problem eller felaktig topologi.

Att stänga av renderingen `Två sidor` kan förbättra renderingsprestandan lite.


### ![](/icons/wireframe.webp) Wireframe {#wireframe-quick}
Slår på/av en wireframe-överlagring.

Observera att wireframe sänker prestandan.

### ![](/icons/snap_cube.webp) Snap-kub {#snap-cube-quick}
Slår på/av en hjälpikon i scenens hörn, användbar för att orientera dig i rummet och snabbt växla mellan vyerna framifrån/bakifrån/från vänster/från höger/ovanifrån/underifrån.

### ![](/icons/palette.webp) Visa måleri {#show-painting}
Slår på/av visningen av målningen. När den är av visas objekten med ett vitt, icke-metalliskt material med 25% grovhet i stället för sin målning.

### ![](/icons/tool_hide.webp) Använd Dölj {#use-hide}
Slår på/av döljläget. När det är avstängt finns det kvar, det är bara inaktiverat. Knappen är inaktiverad om du just nu använder verktyget Dölj.

### ![](/icons/shield.webp) Visa mask {#show-mask}
Slår på/av maskläget. När det är avstängt finns masken kvar, den är bara inaktiverad. Tryck på knappen igen för att aktivera den på nytt.

Om du behöver dölja masken OCH ändå ha den aktiv, använd maskfärgen nedan och ställ in den på vitt. Kom ihåg att ändra tillbaka den till grått när du är klar!

Observera att knappen är inaktiverad om du just nu använder ett maskverktyg.

### ![](/icons/shield.webp) Mask → Oopakt {#mask-opaque}
`Mask → Oopakt` ignorerar genomskinliga vertexar för den maskerade masken. Det gäller bara opacitet i vertexar och texturer; ytor som är dolda med “dölj” förblir dolda. Det är bara tillgängligt medan `Visa mask` är på.

### ![](/icons/bang.webp) Markering {#highlight-quick}
Slår på/av blinkningen som markerar valet. När du väljer objekt blinkar det valda objektet till i 500 millisekunder. Blinkningens färg och längd kan anpassas nedan.

### ![](/icons/list.webp) Statistik {#stats-quick}
Slår på/av statustexten i 3d-vyn. Den visar information om systemets minne, scenens totala antal vertexar och antalet vertexar i den aktuella markeringen.

----- 

### ![](/icons/cube.webp) Mörka ej valda objekt {#darken-unselected-objects}
Objekten som inte är valda mörkas ned så att den aktuella markeringen sticker ut.

### ![](/icons/shield.webp) Mask {#mask}
Färgen som används för maskering, som standard ett mellangrått som multipliceras med objektets färg. Ställ in den på vitt för att göra masken osynlig, men kom ihåg att ändra tillbaka den till grått när du är klar!

## ![](/icons/cursor.webp) Markör {#cursor}

### Cirkel {#show-circle-while-sculpting}
När cirkeln för penselns radie visas:

* `Auto` - visar cirkeln, men döljer den medan du skulpterar.
* `Nej` - visar aldrig cirkeln.
* `Ja` - visar alltid cirkeln, även medan du skulpterar.

### Visa liten prick {#show-small-dot}
Visar en prick i mitten av penseldraget medan du skulpterar, eller när kamerans pivot ändras.

### Visa repstabilisator {#show-rope-stabilizer}
Ritar en linje som visar repets längd när [Slö repsstabilisator](stroke.md#lazy-rope-stabilizer) är aktiv i penseldragsinställningarna.

### Visa rullningstips {#show-roll-hint}
Visar en guide för rullningsriktningen medan du använder en tangentbindning för rullning.

### ![](/icons/radius.webp) Storlek {#dot-size}
Storleken på den lilla pricken.

### Färger {#cursor-colors}
Markören byter färg beroende på vad du gör: `Skulptera`, `Bakgrund` (när du hovrar över bakgrunden), `Mask`, `Jämna ut`, `Kamera` och `Radie`. Varje färg kan anpassas här.

## ![](/icons/cursor.webp) Indikator {#indicator}
![](/images/settings_indicator.webp)

Visar visuella indikatorer för guider och skärminspelningar. Ställ in den på `Ja` för att slå på den (på iOS finns även alternativet `Auto`).

Knapparna `Finger`, `Stylus` och `Mus` visar en ikon när den typen av inmatning upptäcks.

### Färg {#indicator-color}
Indikatorns färg.

### Storlek/Ikon/Cirkel {#indicator-shape}
Kontroller för att justera indikatorns storlek, och opaciteten för ikonen och cirkeln i indikatorn.

## ![](/icons/wireframe.webp) Wireframe {#wireframe}
![](/images/settings_wireframe.webp)
Aktiverar wireframe-överlagringen.

### Mål {#target}
Bestämmer om icke valda objekt visar wireframe, eller bara valda objekt, eller alla objekt.

### Dölj {#hide}
Bestämmer om wireframe fortfarande visas för dolda polygoner.

### Multiresolution: Endast nivå 0 {#multiresolution-level-0-only}
Multiresolution visar wireframe för nivå 0 mörkare, och högre nivåer allt ljusare. När det här alternativet är aktiverat visas bara wireframe för nivå 0.

### Färg {#wireframe-color}
Ställer in färg och opacitet för wireframe.

## ![](/icons/grid.webp) Rutnät {#grid}
![](/images/settings_grid.webp)
Aktiverar rutnätet.

### Fäst {#snap}
De här alternativen gör att punkterna i kurv- och formbaserade verktyg (`Svarv`, `Rör`, polygon- och banformer...) fästs medan du ritar dem:

* `Fäst vid rutnät` - fäster vid rutnätet.
* `Fäst vid punkter (justerad vy)` - fäster vid befintliga punkter i närheten när kameran är justerad mot en axel.
* `Fäst vid punkter (fri vy)` - fäster vid befintliga punkter i närheten när kameran inte är justerad.

### Färg {#grid-color}
Ställer in rutnätets färg och opacitet. De här alternativen visas när rutnätet syns.

`Vinjett` tonar ut rutnätet mot kanterna. `Fästgräns för indelningar` ställer in, i pixlar, hur tätt rutnätets linjer får bli på skärmen innan rutnätet byter till en annan indelningsnivå.

## ![](/icons/culling.webp)Två sidor {#two-sided}
Gör att polygonernas ytor syns från båda sidor.

### Baksidans färg {#backface-color}
`Färgad baksida` tonar baksidorna, och `Baksidans färg` ställer in tonens färg.

## ![](/icons/outline.webp)Kontur {#outline}
Aktiverar en kontur runt de valda objekten.

### Konturfärg, Tjocklek {#outline-color-thickness}
Ställer in konturens färg och `Tjocklek`.


## ![](/icons/bang.webp) Markering {#highlight}
Aktiverar en kort blinkning när markeringen ändras.
### Färg, Varaktighet {#color-duration}
Ställer in blinkningens färg och längd i millisekunder.

## ![](/icons/snap_cube.webp) Snap-kub {#snap-cube}
![](/images/settings_snapcube.webp)

Visar en hjälpikon i scenens hörn, användbar för att snabbt växla mellan vyerna framifrån/bakifrån/från vänster/från höger/ovanifrån/underifrån. Tryck på kubens sidor för att växla mellan ortografiska vyer.

### Form {#shape}
Välj mellan en sfär, en kub eller en gnomon som form för snap-kuben.

### Begränsa justering {#restrict-alignment}
Justerar fästvyerna efter världens axlar. När det är aktiverat är bara de 6 huvudvyerna möjliga. På `Auto` gäller begränsningen bara när kameran är i läget `Vändskiva`.

### Storlek {#size}
Ställer in snap-kubens storlek.

### Vänd 180° {#flip-180}
Gör att ett tryck på kubens mitt roterar vyn 180 grader när vyn är fäst. Om vyn till exempel är fäst framifrån roterar ett tryck på vykuben till vyn bakifrån.

### Kanter och hörn {#edges-corners}
Lägger till fästvyer på kubens kanter och hörn (de bärnstensfärgade zonerna). Inte tillgängligt med gnomonformen.

### Dragning med vändskiva {#turntable-drag}
När du drar i kuben roterar vyn utan att kameran rullar, och stannar vid varje fästvy. Avaktivera det för att dra kuben med rotationen `Trackball` i stället. Oavsett vilket förblir draget vågrätt eller lodrätt. Med en kamera i läget `Vändskiva` dras kuben alltid på det här sättet.

### Position {#snap-position}
Ställer in i vilket hörn snap-kuben ligger.


## ![](/icons/list.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Visar information om systemets minne, scenens totala antal vertexar och antalet vertexar i den aktuella markeringen.

### Position {#stats-position}
Ställer in i vilket hörn statistiken visas.

## ![](/icons/edit_radius.webp) Handtag {#handle}
Inställningar för handtagen som du drar i vyn, som gizmon.

### Numerisk inmatning {#gizmo-input}
Tillåter numerisk inmatning när du trycker på en av gizmons kontroller.

### Dölj vid interaktion {#hide-on-interaction}
Tonar ut gizmon medan du interagerar med den, så att den inte är i vägen.

### ![](/icons/opacity.webp) Opacitet {#handle-opacity}
Handtagens opacitet.

## ![](/icons/shape_lasso.webp) Form {#shape-settings}
Hur formerna som du ritar med formbaserade penseldrag (lasso, rektangel, kurva...) ser ut på skärmen.

### ![](/icons/opacity.webp) Fyllning, Kontur {#shape-fill-outline}
Opaciteten för formens insida och för linjen runt den.

### Färger {#shape-colors}
Formens färg för varje typ av verktyg: `Mask`, `Dölj`, `Ytgrupp` och `Beskär`.

## ![](/icons/array.webp) Repeterare {#primitive-repeaters}
Gränser för kopiorna som görs av [repeterare](scene#repeaters) (array, radiell, kurva, yta). De gör att Nomad förblir responsivt när en repeterare spårar ur.

### ![](/icons/cube.webp) Max kopior {#repeater-max-copies}
Det högsta antalet kopior som en enskild repeterare gör. Nomad har svårt med många objekt, oavsett deras storlek.

### ![](/icons/cube.webp) Kopior i scenen {#repeater-scene-copies}
Kopiebudgeten för hela scenen. En lågpolygonkopia kostar lite geometri men förblir ett fullständigt objekt, så det är den här gränsen som små kopior når först.

### ![](/icons/triangle.webp) Max. ytor {#repeater-max-faces}
Ytbudgeten för alla kopior i scenen. När den överskrids förlorar de tyngsta objekten kopior först.

## ![](/icons/multires.webp) Multiresolution {#multires}
### Max antal vertiser {#multires-lowres-count}
Ställer in en gräns så att en multires-indelning inte kan överstiga det här antalet vertexar, vilket troligen skulle få Nomad att krascha: Nomad kontrollerar inte det tillgängliga minnet innan indelningen. Standardvärdet är 10 miljoner.
### Låg upplösningströskel {#multires-lowres-threshold}
En lägre upplösning av nätet kan visas när du flyttar kameran. Du kan öka det här värdet om du vill visa en högre upplösning av nätet.

## Inställningar {#advanced}
### ![](/icons/reset.webp) Återställ till standard {#reset}
Återställer alla appens inställningar till standardvärdena.

Vissa resurser sparas separat och återställs INTE: projekt, tangentbindningar, verktygsförinställningar, HDR-miljöer, MatCaps, alfor, penseltexturer och referensbilder. Allt som sparas med projektet, som belysning, efterbehandling eller kameravyer, lämnas också orört.
