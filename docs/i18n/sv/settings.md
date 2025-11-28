# ![](/icons/cog.webp) Inställningar {#reset-to-default}

Menyn Inställningar innehåller många alternativ för att styra utseende och beteende i Nomad.

![](/images/settings_overview.webp)

## Visningsinställningar {#display-settings}
Detta avsnitt innehåller snabbstartgenvägar för de flesta inställningar längre ned i denna meny.

![](/images/settings_display_settings.webp)

### Mjuk skuggning {#smooth-shading}
Växla mellan mjuk och fasetterad skuggning. När fasetterad är aktiverad skuggas polygonerna oberoende av varandra, så att du kan se den underliggande topologin.
Det kan vara användbart att se fasetterad skuggning under skulpteringsstadiet och sedan byta till mjuk skuggning för rendering.

Att inaktivera mjuk skuggning förbättrar prestandan en aning.

### Kontur {#outline-quick}
Slå på/av en kontur runt din aktuella markering.

Detta är användbart för att få visuell återkoppling på ditt nuvarande valda mesh om [Mörklägg icke markerade](#darken-unselected-objects) är inaktiverat.

Ur prestandasynpunkt är det mycket bättre att använda [Mörklägg icke markerade](#darken-unselected-objects) än att använda konturlösningen.

### Rutnät {#grid-quick}
Slå på/av ett bakgrundsrutnät, användbart för att förstå objektplacering och skala.

### Dubbelsidig {#two-sided-quick}
Slå på/av tvåsidig polygonvisning. Alla ytor pekar i en viss riktning.
Ytor som betraktas som *baksida* är de som pekar ”bort” från kamerans synvinkel.

Till exempel kommer den enkla startkulan ha sina ytor pekande utåt.
Om du flyttar kameran inuti kulan kommer du då att se baksidan av dessa ytor.

För det mesta bör du inte se baksidan av ytor, så att färglägga dem kan hjälpa dig att upptäcka potentiella problem eller felaktig topologi.

Att inaktivera `tvåsidig` rendering kan förbättra renderingsprestandan något.


### Trådram {#wireframe-quick}
Slå på/av ett trådramsöverlägg. 

Observera att aktivering av trådram kommer att sänka prestandan.

### Snappkub {#snap-cube-quick}
Slå på/av en hjälpikonen i hörnet av scenen, användbar för att orientera sig i rymden och snabbt växla mellan vyerna fram/bak/vänster/höger/topp/botten.

### Visa målning {#show-painting}
Slå på/av visning av målning. Standardmaterialet som används är ett vitt icke-metalliskt material med 25 % råhet.

### Använd göm {#use-hide}
Slå på/av dölj-läget. När det är avstängt finns det fortfarande kvar, bara inaktiverat. Denna knapp är inaktiverad om du för närvarande använder dölj-verktyget.

### Visa mask {#show-mask}
Slå på/av maskläget. När det är avstängt finns det fortfarande kvar, bara inaktiverat. Tryck på denna knapp igen för att återaktivera det.

Om du behöver dölja masken OCH ändå ha den aktiv, använd maskfärgen nedan och ställ in den på vitt. Kom ihåg att ändra tillbaka den till en grå när du är klar!

Observera att denna knapp är inaktiverad om du för närvarande använder ett maskverktyg. 

### Mask -> Opaque {#mask-opaque}
Mask -> opaque kommer att ignorera transparenta verticer för maskad mask. Detta är endast relevant för vertex- och texturopacitet, ytor som är dolda med ”dölj” kommer fortfarande att vara dolda.

### Markering {#highlight-quick}
Slå på/av markeringsblinkningen. När objekt väljs blinkar det valda objektet tillfälligt i starkt rosa i 500 millisekunder. Färgen och längden på blinkningen kan anpassas nedan.

### Statistik {#stats-quick}
Slå på/av statusvisningstexten i 3D-vyn. Den visar information om ditt systemminne, totalt antal verticer i scenen och antal verticer i den aktuella markeringen.

----- 

### Mörka ej markerade objekt {#darken-unselected-objects}
Objekt som inte är markerade kommer att mörkläggas så att den aktuella markeringen kan framträda tydligare.

### Mask {#mask}
Färgen som används för maskning, som standard en mellangrå, multipliceras mot objektets färg. Sätt denna till vitt för att göra masken osynlig, men kom ihåg att ändra tillbaka den till grå när du är klar!

## ![](/icons/cursor.webp) Markör {#cursor}

### Visa cirkel vid skulptering {#show-circle-while-sculpting}
Fortsätt visa penselradien när du skulpterar.

### Visa liten punkt {#show-small-dot}
Visa en punkt i mitten av penseldraget när du skulpterar, eller när kamerapivoten ändras.

### Visa rep-stabilisering {#show-rope-stabilizer}
Rita en linje som visar replängden när lazy rope-stabilisatorn är aktiv i penseldragsinställningarna.

## ![](/icons/cursor.webp) Indikator {#indicator}
![](/images/settings_indicator.webp)

Visa visuella indikator(er) för handledningar och skärminspelningar.

Knapparna `Finger`, `Stylus` och `Mouse` aktiverar visning av en ikon när den typen av inmatning upptäcks.

### Färg {#indicator-color}
Indikatorns färg.

### Storlek/Ikon/Cirkel {#indicator-shape}
Reglage för att justera indikatorns storlek och formerna i indikatorn.

## ![](/icons/wireframe.webp) Trådram {#wireframe}
![](/images/settings_wireframe.webp)
Aktivera trådramsöverlägget.

### Mål {#target}
Ställ in om icke markerade objekt ska visa trådram, eller endast markerade objekt, eller alla objekt.

### Göm {#hide}
Ställ in om trådramen fortfarande ska visas för dolda polygoner.

### Multiresolution: Endast nivå 0 {#multiresolution-level-0-only}
Multiresolution kommer att visa trådramar för nivå 0 mörkare och högre nivåer successivt ljusare. När detta är aktiverat visas endast trådramen för nivå 0.

### Färg {#wireframe-color}
Ställ in färg och opacitet för trådramen.

## ![](/icons/grid.webp) Rutnät {#grid}
![](/images/settings_grid.webp)
Aktivera rutnätet.

### Färg {#grid-color}
Ställ in rutnätets färg och opacitet.

### Snapp {#snap}
Aktivera snäppning mot rutnätet för kurvbaserade verktyg.

## ![](/icons/culling.webp)Two sided {#two-sided}
Aktivera visning av polygonytor från båda sidor.

### Färga baksida, baksidesfärg {#backface-color}
Aktivera toning av baksidorna och välj toningsfärg.

## ![](/icons/outline.webp)Outline {#outline}
Aktivera en kontur runt det aktiva objektet.

### Konturfärg, tjocklek {#outline-color-thickness}
Ställ in färg och tjocklek för konturen.


## ![](/icons/bang.webp) Markering {#highlight}
Aktivera en kort blinkning när det aktiva objektet ändras.
### Färg, varaktighet {#color-duration}
Ställ in färg och tidslängd för blinkningen i millisekunder.

## ![](/icons/snap_cube.webp) Snappkub {#snap-cube}
![](/images/settings_snapcube.webp)

Visa en hjälpikonen i hörnet av scenen, användbar för att snabbt växla mellan vyerna fram/bak/vänster/höger/topp/botten. Tryck på sidorna av tärningen för att byta mellan ortografiska vyer.

### Form {#shape}
Välj mellan en kub, en sfär eller en gnomon-form för snaptärningen.

### Begränsa riktning {#restrict-alignment}
Aktivera låsning av kamerarotation när du drar på snaptärningen. När detta är aktivt kommer en dragrörelse på snaptärningen endast gå vänster/höger eller upp/ner.

### Storlek {#size}
Ställ in storleken på snaptärningen.

### Vänd 180 {#flip-180}
Aktivera ett tryckbeteende så att om vyn är snäppad, kommer ett tryck på mitten av tärningen att rotera vyn 180 grader. Till exempel, om vyn är snäppad till framifrån, kommer ett tryck på vykuben att rotera till bakifrån-vy.

### Position {#snap-position}
Ställ in i vilket hörn snaptärningen ska vara.

## ![](/icons/edit_radius_n.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Visa information om ditt systemminne, totalt antal verticer i scenen och antal verticer i den aktuella markeringen.

### Position {#stats-position}
Ställ in i vilket hörn statistiken ska visas.

## Primitive/Upprepningar {#primitive-repeaters}
## Numerisk inmatning {#gizmo-input}
Tillåt numerisk inmatning när du trycker på gizmo-widgetarna.

## Multiresolution {#multires}
### Max antal vertex {#multires-lowres-count}
Ställ in en gräns för att inte tillåta en multires-subdivide-operation högre än detta polygonantal, vilket sannolikt skulle krascha Nomad. Standardvärdet är 10 miljoner.
### Lågupplöst tröskel {#multires-lowres-threshold}
En lägre upplösning av meshen kan visas när du flyttar kameran. Du kan öka detta värde om du vill visa en högre upplösning av meshen.

## Inställningar {#advanced}
### Återställ till standard {#reset}
Återställ alla inställningar till deras standardvärden.