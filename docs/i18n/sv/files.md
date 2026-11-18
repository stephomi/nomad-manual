# ![](/icons/open.webp) Filer {#files}

I menyn Filer kan du spara och öppna Nomad-projekt, importera och exportera 3d-modeller, exportera renderade bilder och länka Nomad till andra appar. Den har tre flikar: `Filer`, `Rendera` och `Länk`.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

Miniatyren högst upp visar det aktuella projektet, med filstorlek, automatisk sparning och sparad historik bredvid. Tryck på miniatyren för att öppna en liten bläddrare med dina projekt, och tryck sedan på ett projekt för att få en meny där du kan öppna, lägga till, skriva över, klona, byta namn på eller radera det.

När projektet har ändringar som inte sparats än visas `Osparade ändringar!` under miniatyren.

### Omfång {#scope}
På datorn väljer du var dina projekt sparas:
* `Intern` - Standardvalet, samma som på mobilen. Projekten sparas bara i Nomads huvudmapp.
* `På plats` - När du öppnar ett projekt utanför Nomad-mappen skriver sparningen över originalfilen. Automatisk sparning fungerar inte för de här externa projekten.

### ![](/icons/nomad.webp) Förinställning {#preset}
Ger tillgång till en samling demor och karaktärsdelar. Välj en, och välj den sedan igen för att antingen `Öppna` den eller `Lägg till i scenen`. Från den här bläddraren kan du också ladda ner gratis modeller från Poly Haven.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Historik... {#history}
Snabb tillgång till projektets historikalternativ, till exempel `Spara historik`, som behåller din ångra-historik när projektet sparas. En grön markering på knappen visar att historiken sparas med projektet. Se [Historik](history.md#save-history) för mer information.

### ![](/icons/save.webp) Spara {#save}
Sparar Nomad-projektet. Om projektet aldrig har sparats får du ange ett namn.

### ![](/icons/save_as.webp) Spara som... {#save-as}
Sparar projektet under ett nytt namn, som ett nytt projekt.

### ![](/icons/save_as.webp) Skriv över... {#overwrite}
Visar projektbläddraren så att du kan spara den aktuella scenen över ett annat projekt. Aktivera `Inkludera endast valda objekt` för att bara spara de valda objekten i stället för hela scenen. Bläddraren har också knappen `Spara som...` om du hellre vill spara som ett nytt projekt.

### ![](/icons/pencil.webp) Byt namn {#rename}
Visar en textruta där du kan byta namn på det aktuella projektet.

### ![](/icons/open.webp) Öppna... {#open}
Visar projektbläddraren så att du kan öppna ett projekt.

### ![](/icons/add_file.webp) Lägg till i scenen... {#add}
Visar projektbläddraren. När du väljer ett projekt slås dess innehåll ihop med den aktuella scenen.

### ![](/icons/trash.webp) Radera... {#delete}
Visar projektbläddraren. De projekt du väljer raderas från filsystemet.

### ![](/icons/new_file.webp) Ny {#new}
Startar ett nytt projekt. Om det finns osparade ändringar får du bekräfta. I bekräftelsen kan du välja att `Behåll` eller `Återställ` inställningarna för `Bakgrund`, `Miljö`, `MatCap` och `Röntgen`, och välja om det nya projektet ska använda `Spara historik`.

### ![](/icons/autosave.webp) Automatisk spara... {#auto-save}
Meny för alternativen för automatisk sparning. Aktivera `Automatisk spara` för att spara ditt projekt i en separat fil med jämna mellanrum. Markeringen på knappen visar om den är påslagen.

Anledningen till att Nomad inte sparar i bakgrunden är att 3d-filer kan vara ganska stora, vilket kan ge en märkbar fördröjning medan du skulpterar.

För att undvika att minnet tar slut komprimeras dessutom scenen oftast innan den sparas.
Den här komprimeringen och dekomprimeringen gör också att sparningen tar längre tid.

### Sparintervall {#timer-pop-up}
Hur många minuter Nomad väntar mellan de automatiska sparningarna.

### Visa nedräkning {#popup-timeout}
Visar en nedräkning före varje automatisk sparning, så att du kan avbryta den om du är mitt i något. När det är avaktiverat sparar Nomad så fort du slutar skulptera.

### ![](/icons/trash.webp) Kassera Auto Spara {#discard-autosave}
Om det finns en automatiskt sparad fil för ett projekt läses den in automatiskt i stället för originalprojektet. Om du inte vill det raderar den här knappen den automatiskt sparade filen. När du sedan öppnar filen läses projektets senaste manuella sparning in.

### ![](/icons/open.webp) Öppna föråldrad sparning {#open-outdated-save}
När ett projekt har både en automatisk och en manuell sparning öppnar den här knappen den äldre av de två (`Öppna föråldrad automatisk sparning` eller `Öppna föråldrad manuell sparning`), med dess datum. Praktiskt om den senaste sparningen inte är den du ville ha.

### ![](/icons/storage.webp) Nyligen raderade... {#recently-deleted}
Nomad behåller data från projekt som har lämnat projektmappen, och filer som ersatts vid en import, i ett antal dagar innan de raderas för gott. Filer som inte gick att importera ligger kvar tills du raderar dem. Listan visar dem med storlek och datum, så att du kan radera dem en i taget eller med `Radera alla`.

## Importera {#import}

### ![](/icons/add_file.webp) Importera {#import-button}
För att importera 3d-filer som inte är Nomad-projekt.

När du importerar en extern scenfil till Nomad kan du antingen *lägga till* den eller starta ett *nytt* projekt med den.

Om du lägger till en fil läggs objekten helt enkelt till i den aktuella scenen.
Om du väljer `Ny` skapas ett nytt Nomad-projekt med de nya objekten i.

Importfönstret listar varje fil du har valt, med sina egna importalternativ. Bilder kan också importeras på det här sättet: välj för var och en om den ska bli en `HDRI`, en `MatCap`, en `Referensbild`, en `Alpha`, `Texturer` eller en `VDM`.

Nomad kan importera de här formaten:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), på plattformar som har stöd för det

### ![](/icons/cog.webp) Inställningar {#advanced}
Knappen `Inställningar...` bredvid projektminiatyren visar de viktigaste importalternativen. De här inställningarna sparas inte, och importfönstret visar de alternativ som gäller för filerna du importerar.

### Alla format {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Behåll topologi {#keep-topology}
Som standard försöker Nomad rätta till problematisk geometri vid inläsning. Om du aktiverar det här slutar Nomad att ändra ordningen på vertices och ytor, slå ihop dubbletter och ta bort oanvända vertices.

::: warning
Med `Behåll topologi` kanske operationer som Boolean, Foga ihop, Decimera eller Manifold inte slår ihop dubbla vertices.
:::

#### ![](/icons/image.webp) Hoppa över texturer {#skip-textures}
Läser inte in texturerna som är inbäddade i filen, för format som har stöd för det, som glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Läs in UI-inställningar {#keep-gui-settings}
När du öppnar eller importerar en projektfil läses alla gränssnittsinställningar som sparats i den in.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Dela upp OBJ efter grupper {#split-obj-by-groups}
Delar upp OBJ-grupper i separata objekt.

#### ![](/icons/vertex.webp) Slå samman dubbletter av positioner {#merge-duplicate-positions}
Slår ihop vertices som har samma position.

#### ![](/icons/uv.webp) Slå samman dubbletter av UV {#merge-duplicate-uvs}
Slår ihop texturkoordinater som har samma UV.

#### ![](/icons/paint.webp) Färgrymd {#color-space}
Anger hur färgerna i filen tolkas: `Auto`, `Linjär` eller `sRGB`. Prova att växla det här alternativet om färgerna ser fel ut.

#### ![](/icons/image.webp) Format {#normal-format}
Texturernas format för normal maps: `Auto`, `OpenGL (+Y)` eller `DirectX (-Y)`. Prova det andra om detaljerna i normal mapen ser inverterade ut.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Färgrymd {#color-space-ply}
Anger hur färgerna i filen tolkas: `Auto`, `Linjär` eller `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Slå samman dubbletter av UV {#merge-duplicate-uvs-fbx}
Slår ihop texturkoordinater som har samma UV.

#### ![](/icons/paint.webp) Färgrymd {#color-space-fbx}
Anger hur färgerna i filen tolkas: `Auto`, `Linjär` eller `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Texturernas format för normal maps: `Auto`, `OpenGL (+Y)` eller `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Färgrymd {#color-space-usd}
Anger hur färgerna i filen tolkas: `Auto`, `Linjär` eller `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Texturernas format för normal maps: `Auto`, `OpenGL (+Y)` eller `DirectX (-Y)`.



## Exportera {#export}
Sparar till ett 3d-geometriformat som kan användas i andra program.

![](/images/file_export.webp)

Olika filformat har stöd för olika funktioner, så de tillgängliga alternativen ändras beroende på vilken filtyp du väljer.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertexfärger](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex-PBR](#pbr-paint)        | ✅     | Nomad ✅<br>Andra ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Andra ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Lager](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objekt                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Ytgrupp                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarki                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Ljuskällor                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Texturer                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitiver, efterbehandling osv.    | ✅     | Nomad ✅<br>Andra ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Exportknapp {#export-button}
Klicka här för att exportera geometrin med de valda inställningarna. Knappen visar det valda formatet och en uppskattning av filstorleken. På Android finns knappen `Dela` bredvid, som skickar filen direkt till en annan app.

### Filformat {#file-format}
Välj vilket format du vill exportera till: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` eller `USD`. NOMAD är Nomads eget format och kan inte öppnas i andra program, så det är främst till för att importera tillbaka till Nomad.

### Inkludera {#allvisibleselected}
Välj vilka objekt som ska exporteras: `Alla`, `Synlig` eller `Vald`. Siffran bredvid varje alternativ visar hur många objekt som kommer att exporteras.

### En fil per objekt {#one-file-per-object}
Exporterar varje objekt till en egen fil. Siffran visar hur många filer som kommer att skrivas.

### Typ {#type}
När exporten skriver flera filer (en fil per objekt, eller OBJ med texturer), spara dem i en `Mapp` eller en `Zip`. Vissa appar (Google Drive, One Drive, osv.) har inte stöd för att importera mappar, så då kan du använda Zip i stället.

### Bädda in historik {#embed-history}
Bara NOMAD. Tar med ångra-historiken i filen, och den återställs när filen öppnas i Nomad. Det gör filen större och kräver att hela scenen exporteras som en enda fil.

### Bädda in resurser {#embed-assets}
Bara NOMAD. Tar med dina egna matcaps, miljöer och typsnitt i filen. Inbyggda resurser bäddas inte in.

### Vertexfärger {#vertex-colors}
Exporterar vertexfärger om filformatet har stöd för det. En del 3d-program kan läsa dem, men inte alla.

För OBJ kan du välja:
* `Ingen` - Inga färger.
* `RGB` - Färgerna läggs till efter vertexpositionerna.
* `MRGB (ZBrush)` - Ett annat sätt att koda färg, som också har stöd för maskdata.

### Färgrymd {#color-space-export}
Bara OBJ, med vertexfärger i `RGB`. Skriver färgerna som `Linjär` eller `sRGB`.

### PBR målarfärg {#pbr-paint}
Exporterar målning av grovhet, metallitet och mask. Andra program kan ignorera den här datan.
PBR-vertexfärger exporteras som sekundära vertexfärgattribut.
Kanalerna packas på följande sätt:

|           | Kanal  |
| :-------: | :------: |
| Grovhet | R        |
| Metallitet | G        |
| Maskering   | B        |


### Skikt {#layers}
Lager stöds genom morph targets i glTF. Det har officiellt stöd i glTF, så det bör fungera i andra program också.
Nomad exporterar även färg, grovhet och metallitet per lager, men det ignoreras av andra program.

### Skiktmålning {#layer-painting}
Exporterar målning i lager, som oftast ignoreras av andra program.

### Ytgrupp {#face-group}
Exporterar ytgrupper. Exporten kan ibland ställa till det i andra program.

### Skriv objekt {#write-objects}
Bara OBJ. Håller isär objekten. Avaktivera det för att exportera allt som ett enda objekt, till exempel för att använda funktionen "Mesh ID / Polygroup" i Substance Painter.

### Normals {#normals}
Exporterar normalinformation. Observera att Nomad alltid beräknar sina egna normaler när andra filformat importeras.

### Tangenter {#tangents}
Exporterar tangentinformation, som används om modellen har normal maps.

### Texturer {#textures}
Om texturer har lagts till i materialet exporteras de. Observera att texturerna inte bakas här, det görs med bakningsalternativen under Topologi.

### Format {#fbx-format}
Bara FBX. `Binär` är mindre men fungerar kanske inte i alla program, `Ascii` är en textfil.

### Komprimerad {#compressed}
Bara FBX. Minskar filstorleken, men exporten och importen blir långsammare.

### Förinställning {#usd-preset}
Bara USD. Välj vilken app du exporterar till: `OpenUSD`, `Apple`, `Procreate` eller `Zbrush`. Vissa alternativ finns bara för vissa förinställningar.

### Instans {#instance}
Bara USD. Exporterar instansierade objekt som instanser, i stället för att duplicera deras geometri.

### Tillåt skev {#allow-skew}
Bara USD. Tillåter skjuvning (skew) i transformationsmatriserna. När det är avaktiverat delar Nomad upp skjuvade transformationer i separata skal- och rotationstransformationer.

### Repeater {#repeater}
Bara USD. Exporterar kopiorna som skapats av repeaters som instanser.

### Slå ihop kopior {#join-copies}
Varje objekt och dess repeater-kopior blir ett enda objekt.

::: tip Tips: Importera grovhet och metallitet i Blender

Blender kan importera glTF/glb, men förstår inte automatiskt vertexattributen för metallitet och grovhet. För att använda dem skapar du en Vertex Color-nod i materialredigeraren och ställer in dess egenskap på nästa färgattribut (oftast Col.001). Anslut en "Separate XYZ"-nod, skicka X till roughness och Y till Metallic.

Den här videon visar hur det går till:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tips: Stöd för USD-funktioner

USD är ett komplext format. Specifikationen har stöd för många funktioner, men alla 3d-program stöder dem inte. OSX/iOS har till exempel inte stöd för vertexfärger. Förinställningarna i USD-exporten gör sitt bästa för att vara kompatibla med OpenUSD, Apple, Procreate och Zbrush.

::: 

## ![](/icons/screen.webp) Rendera {#render}

Exporterar en bild som kombinerar alla inställningar i projektet (ljus, material, efterbehandling osv.).

![](/images/file_render.webp)
### ![](/icons/preview.webp) Förhandsgranska {#preview}

Knappen `Förhandsgranska` bredvid menyns rubrik gör gränssnittet genomskinligt, så att du lättare ser hur slutresultatet kommer att beskäras.

### ![](/icons/home.webp) Fokus {#focus}
Ramar in scenen eller markeringen så att den passar renderingsstorleken. Tryck igen för att växla mellan de två.

### ![](/icons/map.webp) Höjdkarta {#heightmap}
Renderar scenen som en höjdkarta i gråskala sedd från kameran, där de närmaste delarna är ljusast. När du aktiverar den byts storleken till `Kvadrat` och markeringen ramas in. En liten list i vyn låter dig justera gradientens `Fokus`.

När `Höjdkarta` är påslagen visas knappen `Spara som alfa` bredvid exportknappen, så att du kan spara renderingen som en ny penselalfa i stället för att exportera en fil.

### ![](/icons/opacity.webp) Transparent bakgrund {#transparent-background}
Aktiverar en alfakanal för renderingen, användbart för att kombinera renderingen med andra bilder i 2d-program. Observera att delvis transparens inte stöds.

### ![](/icons/sliders.webp) Visa gränssnitt {#show-interface}
Tar med Nomads gränssnitt i renderingen.

### Slutlig storlek {#final-size}
Upplösningen som renderingen ska använda: `Skärm`, `720`, `1080`, `4096`, `Kvadrat` eller `Anpassad`.

När menyn Filer är aktiv ritas en streckad ram i vyn som visar renderingsområdet, om det inte stämmer med skärmens upplösning.

### Bredd / Höjd {#render-ratio}
Med `Anpassad` ställer du in bildens bredd och höjd. Länkknappen mellan de två reglagen behåller proportionerna när du ändrar ett av dem. Med `Kvadrat` kan bara bredden ställas in.

### ![](/icons/export.webp) Exportera → PNG {#export-png}
Klicka på den här knappen för att starta renderingen. När den är klar kan du välja hur du vill spara eller dela bilden. För mycket stora storlekar får du bekräfta först: spara ditt projekt innan, ifall enheten får slut på minne.

## ![](/icons/network.webp) Länk {#link}

Anslut Nomad till en annan enhet eller app, för att skicka och ta emot objekt eller synkronisera dina ändringar direkt. En enhet är värd för sessionen och de andra ansluter till den.

### Aktivera GoZ {#enable-goz}
Bara på dator. Utbyter mesher med ZBrush på den här datorn. `Skicka` importerar dem till ZBrush, `Hämta` importerar från det ZBrush som körs: `Val` tar det aktiva subverktyget (subtool), `Scen` tar alla subverktyg. Du kan också trycka på GoZ i ZBrush när som helst.

### Läge {#link-mode}
* `Av` - Ingen länk.
* `Värd` - Den här enheten är värd för sessionen och väntar på att andra ansluter.
* `Anslut` - Söker efter enheter i närheten. Tryck sedan på värdens namn för att ansluta till den.

För att länka två Nomad väljer du `Värd` på en enhet och `Anslut` på de andra. För att länka med Blender ska Nomad vara värd: hjälpknappen bredvid rubriken `Länk` visar hur du installerar tillägget Nomad Blender Link.

### ![](/icons/network.webp) Nätverksport {#network-port}
Nätverksporten som länken använder. Ändra den bara om en annan app redan använder den.

### Skicka / Hämta {#send-get}
När du är ansluten kan du `Skicka` ditt `Val` eller hela `Scen` till den andra enheten, eller `Hämta` dem från den. `Ersätt` raderar den aktuella scenen och hämtar sedan den andra enhetens scen.

### ![](/icons/link.webp) Direktsynkronisering {#live-sync}
Strömmar dina ändringar till den andra enheten medan du arbetar. `Arbetsvy` synkroniserar även kameran. `Scenändringar` anger vilken enhet som skickar ändringarna: `Auto` ger riktningen till den enhet som senast var aktiv. Välj sedan vad som synkroniseras: `Objekt och geometri`, `Material`, `Ljuskällor`, `Kameror` och, när den andra sidan har stöd för det, `Skuggning` och `Efterbehandling`.

::: tip
Befintliga objekt behöver först ett `Skicka` eller `Hämta` för att länkas, innan direktsynkroniseringen kan uppdatera dem.
:::
