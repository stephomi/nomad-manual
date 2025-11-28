# ![](/icons/open.webp) Bestanden {#files}

Het menu Bestanden stelt je in staat om Nomad‑projecten op te slaan en te laden, 3D‑modellen te importeren en exporteren, en gerenderde afbeeldingen te exporteren.

![](/images/file_menu.webp)

## Project {#project}
![](/images/file_project.webp)

Bovenaan dit menu wordt een miniatuur weergegeven van de laatste keer dat is opgeslagen. Door op deze miniatuur te klikken verschijnt een mini‑browser; tik tweemaal op een ander project om een mini‑menu te openen waarmee je dat project kunt openen, toevoegen, opslaan, klonen, hernoemen of verwijderen.

### ![](/icons/nomad.webp) Voorinstelling {#preset}
Toegang tot een verzameling demo’s en karaktercomponenten. Selecteer er één en selecteer vervolgens opnieuw om te kiezen of je het item wilt Openen, Aan scène toevoegen of Klonen naar je projectmap.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Opslaan {#save}
Sla het Nomad‑project op.

### ![](/icons/save_as.webp) Opslaan als... {#save-as}
Toon de projectbrowser zodat je het Nomad‑project onder een nieuwe naam kunt opslaan.

### ![](/icons/pencil.webp) Hernoemen {#rename}
Toon een tekstvak om het huidige project te hernoemen.

### ![](/icons/open.webp) Openen... {#open}
Toon de projectbrowser om een project te openen.

### ![](/icons/add_file.webp) Aan scène toevoegen... {#add}
Toon de projectbrowser; wanneer een project is geselecteerd, wordt de inhoud ervan samengevoegd met de huidige scène.

### ![](/icons/trash.webp) Verwijderen... {#delete}
Toon de projectbrowser; alle geselecteerde projecten worden van het bestandssysteem verwijderd.

### ![](/icons/new_file.webp) Nieuw {#new}
Start een nieuw project; als er niet‑opgeslagen wijzigingen zijn, wordt gevraagd of je wilt opslaan.

### ![](/icons/autosave.webp) Automatisch opslaan... {#auto-save}
Menu om de opties voor automatisch opslaan te beheren.

Als je automatisch opslaan inschakelt, kun je een timer instellen zodat er op regelmatige intervallen een pop‑up verschijnt.
De reden dat Nomad niet op de achtergrond opslaat, is dat 3D‑bestanden behoorlijk groot kunnen zijn, wat merkbare vertraging kan veroorzaken tijdens het beeldhouwen.

Bovendien wordt de scène doorgaans gecomprimeerd vóór de opslagbewerking om problemen met onvoldoende geheugen te voorkomen.
Deze compressie/decompressie zal de opslagbewerking ook vertragen.

### Timer pop up {#timer-pop-up}
Hoe vaak de timer‑pop‑up verschijnt.

### Pop-up time-out {#popup-timeout}
Schakel time‑out voor de pop‑up in.

### Automatisch opgeslagen bestand verwerpen {#discard-autosave}
Als er een automatisch opgeslagen bestand voor een project bestaat, wordt dit automatisch geladen in plaats van het oorspronkelijke project. Als dit niet gewenst is, verwijdert deze knop het automatisch opgeslagen bestand. Het laden van het bestand zal dan de laatste handmatige opslag van het project laden.


## Importeren {#import}

### ![](/icons/add_file.webp) Importeren {#import-button}
Voor het importeren van 3D‑bestanden die geen Nomad‑projecten zijn.

Wanneer je een extern scenebestand in Nomad importeert, kun je het *importeren* of *toevoegen*.

Een bestand toevoegen zal de objecten simpelweg aan de huidige scène toevoegen.
Een bestand importeren zal een nieuw Nomad‑project aanmaken met de nieuwe objecten erin.

Nomad kan de volgende formaten importeren:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimenteel)

### ![](/icons/cog.webp) Geavanceerd {#advanced}
Toon geavanceerde importopties:

### Project/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Topologie behouden {#keep-topology}
Nomad zal standaard proberen problematische geometrie bij het laden te herstellen. Als je dit inschakelt, voorkomt het dat Nomad vertices/faces herordent, dubbele vertices/faces verwijdert en ongebruikte vertices verwijdert.

#### Texturen overslaan {#skip-textures}
Sla het laden van texturen over voor formaten die dit ondersteunen, zoals glTF.

### Project / glTF {#project-gltf}
#### GUI-instellingen behouden {#keep-gui-settings}
Schakel het opslaan van de GUI‑ en projectinstellingen in het Nomad .nom‑ of glTF‑bestand in.

### OBJ {#obj}
#### OBJ splitsen per groep {#split-obj-by-groups}
Schakel het splitsen van OBJ‑groepen in afzonderlijke objecten in.

#### Kleur­ruimte {#color-space}
Stel de kleurmodus in die uit het OBJ wordt geïnterpreteerd als Linear, sRGB of Auto.

### PLY {#ply}
#### Kleur­ruimte {#color-space-ply}
Stel de kleurmodus in die uit het PLY wordt geïnterpreteerd als Linear, sRGB of Auto.


### FBX {#fbx}
#### Kleur­ruimte {#color-space-fbx}
Stel de kleurmodus in die uit het FBX wordt geïnterpreteerd als Linear, sRGB of Auto.



## Exporteren {#export}
Opslaan naar een 3D‑geometrieformaat dat in andere software kan worden gebruikt. 

![](/images/file_export.webp)

Verschillende bestandsformaten ondersteunen verschillende functies; de beschikbare opties veranderen op basis van het geselecteerde bestandstype.

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


### Alles/Zichtbaar/Geselecteerd {#allvisibleselected}
De actieve knopstatus bepaalt welke objecten worden geëxporteerd. Het getal naast de pictogrammen geeft aan hoeveel objecten voor die optie worden geëxporteerd.

### Vertexkleuren {#vertex-colors}
Exporteer vertexkleuren indien ondersteund door het bestandsformaat.

### PBR-verf {#pbr-paint}
PBR‑vertexkleuren worden geëxporteerd als secundaire vertexkleur‑attributen.
De kanalen worden als volgt verpakt:

|           | Kanaal  |
| :-------: | :-----: |
| Roughness | R       |
| Metalness | G       |
| Masking   | B       |


### Lagen {#layers}
Lagen worden ondersteund via glTF‑morph‑targets.
Nomad exporteert ook per‑laag kleuren, roughness en metalness, maar dit wordt door andere software genegeerd.

### Laagverf {#layer-painting}
Exporteer laagverf; dit wordt meestal door andere software genegeerd.

### Vlakgroep {#face-group}
Exporteer facegroups; exporteren kan soms conflicteren met andere software.

### Normaal­vectoren {#normals}
Exporteer normal‑informatie. Merk op dat Nomad bij het importeren van andere bestandsformaten altijd zijn eigen normals zal berekenen.

### Tangenten {#tangents}
Exporteer tangent‑informatie, gebruikt als het model normal maps heeft. 

### Texturen {#textures}
Als er texturen aan het materiaal zijn toegevoegd, worden deze geëxporteerd. Merk op dat dit geen texturen bakt; dat gebeurt via de bake‑opties in Topology.

### Exportknop {#export-button}
Klik hierop om de geometrie te exporteren met de geselecteerde instellingen.

::: tip Tip: Roughness en metalness in Blender importeren

Blender kan glTF/glb importeren, maar begrijpt niet automatisch vertexattributen voor metalness en roughness. Om ze te gebruiken, maak je in de materiaaleditor een Vertex Color‑node, stel je de eigenschap in op het volgende kleurattribuut (meestal Col.001). Verbind een ‘Separate XYZ’‑node, stuur X naar Roughness en Y naar Metallic.

Deze video toont het proces:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: Ondersteuning van USD‑functies

USD is een complex formaat; de specificatie ondersteunt veel functies, maar niet alle 3D‑software ondersteunt ze. macOS/iOS ondersteunen bijvoorbeeld geen vertexkleur. De preset‑modi binnen de USD‑exporteur proberen een zo goed mogelijke compatibiliteit te bieden met OpenUSD, Apple, Procreate en ZBrush.

::: 

## Renderen {#render}

Exporteer een afbeelding die de combinatie is van alle instellingen in het project (lichten, materialen, nabewerking enz.). 

![](/images/file_render.webp)
### Voorbeeld {#preview}

De kleine voorbeeldknop naast de menutitel dimt de werkbalken om het eindresultaat beter te kunnen bekijken.

### Transparante achtergrond {#transparent-background}
Schakel een alfakanaal in voor de render; handig om de render te combineren met andere afbeeldingen in 2D‑programma’s. Merk op dat gedeeltelijke transparantie niet wordt ondersteund.

### Interface tonen {#show-interface}
Schakel het opnemen van de Nomad‑UI in de render in.

### Renderverhouding {#render-ratio}
Een vermenigvuldigingsfactor voor de beeldresolutie.

### Eindformaat {#final-size}
De resolutie die voor de render wordt gebruikt. Wanneer `Custom` is geselecteerd, worden de schuifregelaars voor breedte en hoogte ingeschakeld. 

Wanneer het menu Bestanden actief is, wordt er een gestreepte overlay in het viewport getekend om het rendergebied aan te geven als dit niet overeenkomt met de schermresolutie (merk op dat je in liggende modus moet zijn voor een correcte weergave).

### PNG exporteren {#export-png}
Klik op deze knop om het renderproces te starten. Wanneer het voltooid is, kun je kiezen hoe je de afbeelding wilt opslaan of delen.