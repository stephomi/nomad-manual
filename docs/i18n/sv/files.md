# ![](/icons/open.webp) Filer

Filmenyn låter dig spara och ladda Nomad‑projekt, importera och exportera 3D‑modeller samt exportera renderade bilder.

![](/images/file_menu.webp)

## Projekt
![](/images/file_project.webp)

En miniatyrbild av den senaste sparningen visas högst upp i denna meny. Genom att klicka på denna miniatyr öppnas en minibläddrare, tryck två gånger på ett annat projekt för att få upp en minimeny för att öppna, lägga till, spara, klona, byta namn på eller ta bort det projektet.

### ![](/icons/nomad.webp) Förinställning 
Få åtkomst till en samling demoprojekt och karaktärskomponenter. Välj en, välj sedan igen för att välja att Öppna, Lägga till i scenen eller Klona posten till din projektmapp.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Spara
Spara Nomad‑projektet.

### ![](/icons/save_as.webp) Spara som...
Visa projektbläddraren så att du kan spara Nomad‑projektet med ett nytt namn.

### ![](/icons/pencil.webp) Byt namn
Visa en textruta för att byta namn på det aktuella projektet.

### ![](/icons/open.webp) Öppna...
Visa projektbläddraren för att öppna ett projekt.

### ![](/icons/add_file.webp) Lägg till i scen...
Visa projektbläddraren, när ett projekt väljs kommer dess innehåll att slås samman med den aktuella scenen.

### ![](/icons/trash.webp) Ta bort...
Visa projektbläddraren, alla markerade projekt kommer att tas bort från filsystemet.

### ![](/icons/new_file.webp) Nytt
Starta ett nytt projekt, om det finns osparade ändringar kommer du att bli tillfrågad om du vill spara.

### ![](/icons/autosave.webp) Autospara...
Meny för att styra alternativ för autosparning.

Om du aktiverar autosparning kan du ställa in en timer så att en popup visas med jämna mellanrum.
Anledningen till att Nomad inte sparar i bakgrunden är att 3D‑filer kan vara ganska stora, vilket kan orsaka märkbar fördröjning medan du skulpterar.

Dessutom, för att undvika minnesbrist komprimeras scenen vanligtvis innan sparningsoperationen.
Denna komprimering/dekomprimering kommer också att göra sparningen långsammare.

### Timer‑popup
Hur ofta timer‑popupen ska visas.

### Popup‑timeout
Aktivera timeout för popup.

### Kassera autosparning
Om en autosparfil finns för ett projekt kommer den automatiskt att laddas i stället för det ursprungliga projektet. Om detta inte önskas kommer denna knapp att ta bort autosparningen. Att ladda filen kommer då att ladda projektets senaste manuella sparning.


## Importera

### ![](/icons/add_file.webp) Importera
För att importera 3D‑filer som inte är Nomad‑projekt.

När du importerar en extern scenfil till Nomad kan du antingen *importera* eller *lägga till* den.

Att lägga till en fil kommer helt enkelt att lägga till objekten i den aktuella scenen.
Att importera en fil kommer att skapa ett nytt Nomad‑projekt med de nya objekten i.

Nomad kan importera följande format:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimentellt)

### ![](/icons/cog.webp) Avancerat
Visa avancerade importalternativ:

### Projekt/ glTF / OBJ / STL / FBX
#### Behåll topologi
Nomad försöker som standard åtgärda problemgeometri vid inläsning. Om du aktiverar detta förhindrar du Nomad från att ändra ordningen på vertexer/ytor, ta bort dubbletter av vertexer/ytor och ta bort oanvända vertexer.

#### Hoppa över texturer
Hoppa över inläsning av texturer för format som stöder det, som glTF.

### Projekt / glTF
#### Behåll GUI‑inställningar
Aktivera sparning av GUI‑ och projektinställningar i Nomad‑filen .nom eller glTF‑filen.

### OBJ
#### Dela upp OBJ efter grupper
Aktivera uppdelning av OBJ‑grupper i separata objekt.

#### Färgrymd
Ställ in färgläget som tolkas från OBJ som Linear, sRGB eller Auto.

### PLY
#### Färgrymd
Ställ in färgläget som tolkas från PLY som Linear, sRGB eller Auto.


### FBX
#### Färgrymd
Ställ in färgläget som tolkas från OBJ som Linear, sRGB eller Auto.



## Exportera
Spara till ett 3D‑geometriformat som kan användas i annan programvara. 

![](/images/file_export.webp)

Olika filformat stöder olika funktioner, de tillgängliga alternativen ändras beroende på valt filformat.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Alla/Synliga/Markerade
Den aktiva knappens läge avgör vilka objekt som kommer att exporteras. Siffran bredvid ikonerna anger hur många objekt som kommer att exporteras för det alternativet.

### Vertexfärger
Exportera vertexfärger om filformatet stöder det.

### PBR‑målning
PBR‑vertexfärger exporteras som sekundära vertexfärgsattribut.
Kanalerna packas på följande sätt:

|           | Kanal   |
| :-------: | :-----: |
| Roughness | R       |
| Metalness | G       |
| Masking   | B       |


### Lager
Lager stöds via glTF‑morfmål (morph targets).
Nomad exporterar också färg, roughness och metalness per lager, men detta ignoreras av annan programvara.

### Lagermålning
Exportera lagermålning, ignoreras vanligtvis av annan programvara.

### Face Group
Exportera facegrupper, export kan ibland störa annan programvara.

### Normaler
Exportera normalinformation. Observera att Nomad alltid beräknar sina egna normaler vid import av andra filformat.

### Tangenter
Exportera tangentinformation, används om modellen har normalmappar. 

### Texturer
Om texturer har lagts till i materialet kommer de att exporteras. Observera att detta inte bakar texturer, det görs via bake‑alternativen i topologi.

### Exportknapp
Klicka här för att exportera geometrin med de valda inställningarna.

::: tip Tips: Importera roughness och metalness till Blender

Blender kan importera glTF/glb, men förstår inte automatiskt vertexattribut för metalness och roughness. För att använda dem, skapa en Vertex Color‑nod i materialeditorn, ställ in dess egenskap till nästa färgattribut (vanligtvis Col.001). Anslut en ”Separate XYZ”‑nod, skicka X till Roughness och Y till Metallic.

Den här videon visar processen:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tips: Stöd för USD‑funktioner

USD är ett komplext format, dess specifikation stöder många funktioner, men all 3D‑programvara stöder dem inte. macOS/iOS stöder till exempel inte vertexfärg. Förinställningslägena i USD‑exportören försöker göra en kvalificerad gissning på kompatibilitet med OpenUSD, Apple, Procreate, ZBrush.

::: 

## Rendera

Exportera en bild som är kombinationen av alla inställningar i projektet (ljus, material, efterbearbetning osv). 

![](/images/file_render.webp)
### Förhandsvisning

Den lilla förhandsvisningsknappen bredvid menytiteln tonar ned verktygsraderna för att hjälpa till att förhandsgranska slutresultatet.

### Transparent bakgrund
Aktivera en alfakanal för renderingen, användbart för att kombinera renderingen med andra bilder i 2D‑program. Observera att partiell transparens inte stöds.

### Visa gränssnitt
Aktivera inkludering av Nomads gränssnitt i renderingen.

### Renderingsförhållande
En multiplikator på bildens upplösning.

### Slutlig storlek
Upplösningen som ska användas för renderingen. När `Custom` är valt aktiveras reglagen för bredd och höjd. 

När filmat är aktivt ritas en streckad markering i vyn för att indikera renderingsområdet om det inte matchar skärmupplösningen (observera att du måste vara i liggande läge för att detta ska stämma).

### Exportera PNG
Klicka på denna knapp för att starta renderingsprocessen. När den är klar kan du välja hur du vill spara eller dela bilden.
