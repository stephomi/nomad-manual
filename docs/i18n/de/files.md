# ![](/icons/open.webp) Dateien {#files}

Das Dateimenü ermöglicht es dir, Nomad-Projekte zu speichern und zu laden, 3D-Modelle zu importieren und zu exportieren sowie gerenderte Bilder zu exportieren.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

Oben in diesem Menü wird ein Thumbnail des letzten Speichervorgangs angezeigt. Wenn du auf dieses Thumbnail klickst, erscheint ein Mini-Browser. Tippe zweimal auf ein anderes Projekt, um ein Mini-Menü zum Öffnen, Hinzufügen, Speichern, Klonen, Umbenennen oder Löschen dieses Projekts aufzurufen.

### ![](/icons/nomad.webp) Voreinstellung {#preset}
Greife auf eine Sammlung von Demos und Charakterkomponenten zu. Wähle eines aus und wähle es dann erneut, um zu entscheiden, ob du den Eintrag Öffnen, Zur Szene hinzufügen oder In deinen Projektordner klonen möchtest.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Speichern {#save}
Speichere das Nomad-Projekt.

### ![](/icons/save_as.webp) Speichern unter... {#save-as}
Zeigt den Projektbrowser an, damit du das Nomad-Projekt unter einem neuen Namen speichern kannst.

### ![](/icons/pencil.webp) Umbenennen {#rename}
Zeigt ein Textfeld an, um das aktuelle Projekt umzubenennen.

### ![](/icons/open.webp) Öffnen... {#open}
Zeigt den Projektbrowser an, um ein Projekt zu öffnen.

### ![](/icons/add_file.webp) Zur Szene hinzufügen... {#add}
Zeigt den Projektbrowser an; wenn ein Projekt ausgewählt wird, wird dessen Inhalt mit der aktuellen Szene zusammengeführt.

### ![](/icons/trash.webp) Löschen... {#delete}
Zeigt den Projektbrowser an; alle ausgewählten Projekte werden aus dem Dateisystem gelöscht.

### ![](/icons/new_file.webp) Neu {#new}
Starte ein neues Projekt. Wenn es ungespeicherte Änderungen gibt, wirst du gefragt, ob du speichern möchtest.

### ![](/icons/autosave.webp) Automatisches Speichern... {#auto-save}
Menü zur Steuerung der Optionen für das automatische Speichern.

Wenn du das automatische Speichern aktivierst, kannst du einen Timer einrichten, sodass in regelmäßigen Abständen ein Popup erscheint.  
Nomad speichert nicht im Hintergrund, da 3D-Dateien sehr groß sein können und dies während des Sculptings zu spürbaren Verzögerungen führen kann.

Zusätzlich wird die Szene zur Vermeidung von Speicherproblemen in der Regel vor dem Speichervorgang komprimiert.  
Diese Komprimierung/Dekomprimierung verlangsamt den Speichervorgang ebenfalls.

### Timer-Popup {#timer-pop-up}
Legt fest, wie häufig das Timer-Popup erscheint.

### Popup-Timeout {#popup-timeout}
Aktiviere das Timeout für das Popup.

### Autospeicherung verwerfen {#discard-autosave}
Wenn für ein Projekt eine Autosave-Datei existiert, wird diese automatisch anstelle des Originalprojekts geladen. Wenn das nicht gewünscht ist, löscht diese Schaltfläche den Autosave. Beim Laden der Datei wird dann der letzte manuelle Speicherstand des Projekts geladen.


## Import {#import}

### ![](/icons/add_file.webp) Importieren {#import-button}
Zum Importieren von 3D-Dateien, die keine Nomad-Projekte sind.

Wenn du eine externe Szenendatei in Nomad importierst, kannst du sie entweder *importieren* oder *hinzufügen*.

Das Hinzufügen einer Datei fügt die Objekte einfach in die aktuelle Szene ein.  
Das Importieren einer Datei erstellt ein neues Nomad-Projekt mit den neuen Objekten.

Nomad kann folgende Formate importieren:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimentell)

### ![](/icons/cog.webp) Erweitert {#advanced}
Zeigt erweiterte Importoptionen an:

### Projekt/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Topologie beibehalten {#keep-topology}
Nomad versucht standardmäßig, problematische Geometrie beim Laden zu korrigieren. Wenn du dies aktivierst, verhindert es, dass Nomad Vertices/Flächen neu anordnet, doppelte Vertices/Flächen entfernt oder unbenutzte Vertices löscht.

#### Texturen überspringen {#skip-textures}
Überspringt das Laden von Texturen für Formate, die dies unterstützen, wie glTF.

### Projekt / glTF {#project-gltf}
#### GUI-Einstellungen beibehalten {#keep-gui-settings}
Aktiviert das Speichern der GUI- und Projekteinstellungen innerhalb der Nomad-.nom- oder glTF-Datei.

### OBJ {#obj}
#### OBJ nach Gruppen aufteilen {#split-obj-by-groups}
Aktiviert das Aufteilen von OBJ-Gruppen in separate Objekte.

#### Farbraum {#color-space}
Legt den aus der OBJ-Datei interpretierten Farbmodus als Linear, sRGB oder Auto fest.

### PLY {#ply}
#### Farbraum {#color-space-ply}
Legt den aus der PLY-Datei interpretierten Farbmodus als Linear, sRGB oder Auto fest.


### FBX {#fbx}
#### Farbraum {#color-space-fbx}
Legt den aus der OBJ-Datei interpretierten Farbmodus als Linear, sRGB oder Auto fest.



## Export {#export}
Speichere in ein 3D-Geometrieformat, das in anderer Software verwendet werden kann. 

![](/images/file_export.webp)

Verschiedene Dateiformate unterstützen unterschiedliche Funktionen; die verfügbaren Optionen ändern sich je nach ausgewähltem Dateityp.

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


### Alle/Sichtbar/Ausgewählt {#allvisibleselected}
Der aktive Button legt fest, welche Objekte exportiert werden. Die Zahl neben den Symbolen gibt an, wie viele Objekte für diese Option exportiert werden.

### Vertex-Farben {#vertex-colors}
Exportiert Vertex-Farben, sofern vom Dateiformat unterstützt.

### PBR-Malerei {#pbr-paint}
PBR-Vertex-Farben werden als sekundäre Vertex-Color-Attribute exportiert.  
Die Kanäle sind wie folgt gepackt:

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Ebenen {#layers}
Ebenen werden über glTF-Morph-Targets unterstützt.  
Nomad exportiert außerdem pro Ebene Farben, Roughness und Metalness, diese werden jedoch von anderer Software ignoriert.

### Ebenenmalerei {#layer-painting}
Exportiert Ebenenmalerei, wird in der Regel von anderer Software ignoriert.

### Flächengruppe {#face-group}
Exportiert Facegroups; der Export kann manchmal mit anderer Software kollidieren.

### Normalen {#normals}
Exportiert Normaleninformationen. Beachte, dass Nomad beim Import anderer Dateiformate immer eigene Normalen berechnet.

### Tangenten {#tangents}
Exportiert Tangenteninformationen, die verwendet werden, wenn das Modell Normalmaps besitzt. 

### Texturen {#textures}
Wenn dem Material Texturen hinzugefügt wurden, werden sie exportiert. Beachte, dass dies kein Baking von Texturen durchführt; das geschieht über die Bake-Optionen in der Topologie.

### Export-Schaltfläche {#export-button}
Klicke hier, um die Geometrie mit den ausgewählten Einstellungen zu exportieren.

::: tip Tipp: Roughness und Metalness in Blender importieren

Blender kann glTF/glb importieren, versteht aber Vertex-Attribute für Metalness und Roughness nicht automatisch. Um sie zu verwenden, erstelle im Material-Editor einen Vertex-Color-Node und setze seine Eigenschaft auf das nächste Farb-Attribut (normalerweise Col.001). Verbinde einen „Separate XYZ“-Node, leite X an Roughness und Y an Metallic weiter.

Dieses Video zeigt den Ablauf:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tipp: USD-Funktionsunterstützung

USD ist ein komplexes Format; seine Spezifikation unterstützt viele Funktionen, aber nicht alle 3D-Programme unterstützen diese. macOS/iOS unterstützen zum Beispiel keine Vertex-Farben. Die Voreinstellungsmodi im USD-Exporter versuchen eine möglichst gute Kompatibilität mit OpenUSD, Apple, Procreate und ZBrush zu erreichen.

::: 

## Rendern {#render}

Exportiere ein Bild, das die Kombination aller Einstellungen im Projekt darstellt (Lichter, Materialien, Post-Processing usw.). 

![](/images/file_render.webp)
### Vorschau {#preview}

Die kleine Vorschau-Schaltfläche neben dem Menütitel blendet die Werkzeugleisten ab, um die Vorschau des Endergebnisses zu erleichtern.

### Transparenter Hintergrund {#transparent-background}
Aktiviert einen Alphakanal für das Rendering, nützlich, um das Rendering in 2D-Programmen mit anderen Bildern zu kombinieren. Beachte, dass partielle Transparenz nicht unterstützt wird.

### Oberfläche anzeigen {#show-interface}
Aktiviert das Einblenden der Nomad-Benutzeroberfläche im Rendering.

### Renderverhältnis {#render-ratio}
Ein Multiplikator für die Bildauflösung.

### Endgröße {#final-size}
Die für das Rendering zu verwendende Auflösung. Wenn `Benutzerdefiniert` ausgewählt ist, werden die Regler für Breite und Höhe aktiviert. 

Wenn das Dateimenü aktiv ist, wird im Viewport eine gestrichelte Überlagerung gezeichnet, um den Renderbereich anzuzeigen, falls er nicht der Bildschirmauflösung entspricht (du musst dafür im Querformat sein, damit dies korrekt ist).

### PNG exportieren {#export-png}
Klicke auf diese Schaltfläche, um den Renderprozess zu starten. Wenn er abgeschlossen ist, kannst du auswählen, wie du das Bild speichern oder teilen möchtest.