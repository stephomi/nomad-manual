# ![](/icons/open.webp) Dateien {#files}

Im Menü Dateien speichern und laden Sie Nomad-Projekte, importieren und exportieren 3d-Modelle, exportieren gerenderte Bilder und verbinden Nomad mit anderen Apps. Es hat drei Tabs: `Dateien`, `Rendern` und `Verbindung`.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

Das Vorschaubild oben zeigt das aktuelle Projekt, daneben die Dateigröße, das automatische Speichern und den gespeicherten Verlauf. Tippen Sie auf das Vorschaubild, um einen kleinen Browser mit Ihren Projekten zu öffnen. Tippen Sie dann auf ein Projekt, um es über ein Menü zu öffnen, hinzuzufügen, zu überschreiben, zu duplizieren, umzubenennen oder zu löschen.

Hat das Projekt noch nicht gespeicherte Änderungen, steht unter dem Vorschaubild `Nicht gespeicherte Änderungen!`.

### Bereich {#scope}
Auf dem Desktop wählen Sie, wo Ihre Projekte gespeichert werden:
* `Intern` - Die Standardeinstellung, wie auf Mobilgeräten. Projekte werden nur im Nomad-Hauptordner gespeichert.
* `Originaldatei` - Öffnen Sie ein Projekt von außerhalb des Nomad-Ordners, überschreibt das Speichern die Originaldatei. Das automatische Speichern funktioniert für diese externen Projekte nicht.

### ![](/icons/nomad.webp) Preset {#preset}
Zugriff auf eine Sammlung von Demos und Charakterbausteinen. Wählen Sie eines aus und tippen Sie erneut darauf, um es zu öffnen (`Öffnen`) oder der Szene hinzuzufügen (`Hinzufügen`). In diesem Browser können Sie auch kostenlose Modelle von Poly Haven herunterladen.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Verlauf... {#history}
Schneller Zugriff auf die Verlaufsoptionen des Projekts, etwa `Verlauf speichern`, womit Ihr Rückgängig-Verlauf beim Speichern des Projekts erhalten bleibt. Ein grünes Abzeichen auf dem Button zeigt an, dass der Verlauf mit dem Projekt gespeichert wird. Details finden Sie unter [Verlauf](history.md#save-history).

### ![](/icons/save.webp) Speichern {#save}
Speichert das Nomad-Projekt. Wurde das Projekt noch nie gespeichert, werden Sie nach einem Namen gefragt.

### ![](/icons/save_as.webp) Speichern als... {#save-as}
Speichert das Projekt unter einem neuen Namen als neues Projekt.

### ![](/icons/save_as.webp) Projekt überschreiben... {#overwrite}
Zeigt den Projektbrowser an, um die aktuelle Szene über ein anderes Projekt zu speichern. Aktivieren Sie `Nur Auswahl exportieren`, um statt der ganzen Szene nur die ausgewählten Objekte zu speichern. Der Browser hat außerdem einen Button `Speichern als...`, um stattdessen als neues Projekt zu speichern.

### ![](/icons/pencil.webp) Umbenennen {#rename}
Zeigt ein Textfeld an, um das aktuelle Projekt umzubenennen.

### ![](/icons/open.webp) Öffnen... {#open}
Zeigt den Projektbrowser an, um ein Projekt zu öffnen.

### ![](/icons/add_file.webp) Hinzufügen... {#add}
Zeigt den Projektbrowser an. Wählen Sie ein Projekt aus, wird sein Inhalt mit der aktuellen Szene zusammengeführt.

### ![](/icons/trash.webp) Löschen... {#delete}
Zeigt den Projektbrowser an. Die ausgewählten Projekte werden aus dem Dateisystem gelöscht.

### ![](/icons/new_file.webp) Neu {#new}
Beginnt ein neues Projekt. Gibt es nicht gespeicherte Änderungen, werden Sie um Bestätigung gebeten. Dabei können Sie die Einstellungen `Hintergrund`, `Umgebung`, `MatCap` und `Röntgen` beibehalten (`Beibehalten`) oder zurücksetzen (`Zurücksetzen`) und festlegen, ob das neue Projekt `Verlauf speichern` nutzt.

### ![](/icons/autosave.webp) Auto-Speichern... {#auto-save}
Menü mit den Optionen zum automatischen Speichern. Aktivieren Sie `Auto-Speichern`, um Ihr Projekt in regelmäßigen Abständen in einer separaten Datei zu sichern. Das Abzeichen auf dem Button zeigt, ob es eingeschaltet ist.

Nomad speichert nicht im Hintergrund, weil 3d-Dateien ziemlich groß sein können und das Speichern beim Sculpten spürbar ruckeln würde.

Außerdem wird die Szene vor dem Speichern in der Regel komprimiert, damit der Speicher nicht knapp wird.
Dieses Komprimieren und Dekomprimieren verlangsamt das Speichern zusätzlich.

### Speicherintervall {#timer-pop-up}
Wie viele Minuten Nomad zwischen zwei automatischen Speicherungen wartet.

### Countdown anzeigen {#popup-timeout}
Zeigt vor jedem automatischen Speichern einen Countdown, damit Sie es abbrechen können, wenn Sie gerade mitten in etwas sind. Ist die Option aus, speichert Nomad, sobald Sie mit dem Sculpten innehalten.

### ![](/icons/trash.webp) AutoSave löschen {#discard-autosave}
Gibt es zu einem Projekt eine automatisch gespeicherte Datei, wird diese statt des Originalprojekts geladen. Wollen Sie das nicht, löscht dieser Button die automatische Sicherung. Beim Laden wird dann der letzte manuell gespeicherte Stand des Projekts geöffnet.

### ![](/icons/open.webp) Veraltete Speicherung öffnen {#open-outdated-save}
Hat ein Projekt sowohl eine automatische als auch eine manuelle Speicherung, öffnet dieser Button die ältere der beiden (`Veralteten Autosave öffnen` oder `Veralteten manuellen Speicherstand öffnen`) und zeigt ihr Datum an. Praktisch, wenn die neueste Speicherung nicht die gewünschte ist.

### ![](/icons/storage.webp) Zuletzt gelöscht... {#recently-deleted}
Nomad bewahrt die Daten von Projekten, die den Projektordner verlassen haben, und Dateien, die durch einen Import ersetzt wurden, einige Tage lang auf, bevor sie endgültig gelöscht werden. Dateien, deren Import fehlgeschlagen ist, bleiben erhalten, bis Sie sie löschen. Diese Liste zeigt sie mit Größe und Datum an, sodass Sie sie einzeln oder mit `Alle löschen` entfernen können.

## Importieren {#import}

### ![](/icons/add_file.webp) Importieren {#import-button}
Zum Importieren von 3d-Dateien, die keine Nomad-Projekte sind.

Beim Importieren einer externen Szenendatei in Nomad können Sie sie entweder *hinzufügen* oder damit ein *neues* Projekt beginnen.

Beim Hinzufügen werden die Objekte einfach in die aktuelle Szene eingefügt.
Mit `Neu` entsteht ein neues Nomad-Projekt, das die neuen Objekte enthält.

Das Importfenster listet jede ausgewählte Datei mit ihren eigenen Importoptionen auf. Auch Bilder lassen sich so importieren: Legen Sie für jedes fest, ob es zu einem `HDRI`, einem `MatCap`, einer `Referenz`, einem `Alpha`, zu `Texturen` oder zu einem `VDM` wird.

Nomad kann diese Formate importieren:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), auf Plattformen, die es unterstützen

### ![](/icons/cog.webp) Einstellungen {#advanced}
Der Button `Einstellungen...` neben dem Projekt-Vorschaubild zeigt die wichtigsten Importoptionen. Diese Einstellungen werden nicht gespeichert, und das Importfenster zeigt die Optionen, die für die zu importierenden Dateien gelten.

### Alle Formate {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Topologie beibehalten {#keep-topology}
Standardmäßig versucht Nomad beim Laden, problematische Geometrie zu reparieren. Ist diese Option aktiv, sortiert Nomad Vertices und Faces nicht um, führt keine Duplikate zusammen und entfernt keine ungenutzten Vertices.

::: warning
Mit `Topologie beibehalten` führen Operationen wie Boolean, Kombinieren, Dezimieren oder Manifold doppelte Vertices möglicherweise nicht zusammen.
:::

#### ![](/icons/image.webp) Texturen überspringen {#skip-textures}
Lädt die in der Datei eingebetteten Texturen nicht, bei Formaten, die das unterstützen, wie glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) GUI-Einstellungen mitladen {#keep-gui-settings}
Lädt beim Öffnen oder Importieren einer Projektdatei alle darin gespeicherten Oberflächeneinstellungen.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) OBJ-Gruppen beibehalten {#split-obj-by-groups}
Teilt OBJ-Gruppen in separate Objekte auf.

#### ![](/icons/vertex.webp) Doppelte Positionen zusammenführen {#merge-duplicate-positions}
Führt Vertices zusammen, die dieselbe Position haben.

#### ![](/icons/uv.webp) Doppelte UVs zusammenführen {#merge-duplicate-uvs}
Führt Texturkoordinaten zusammen, die dieselbe UV haben.

#### ![](/icons/paint.webp) Farbraum {#color-space}
Legt fest, wie die Farben aus der Datei interpretiert werden: `Auto`, `Linear` oder `sRGB`. Wirken die Farben falsch, probieren Sie eine andere Einstellung.

#### ![](/icons/image.webp) Format {#normal-format}
Das Normal-Map-Format der Texturen: `Auto`, `OpenGL (+Y)` oder `DirectX (-Y)`. Wirken die Details der Normal Map invertiert, probieren Sie das andere.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Farbraum {#color-space-ply}
Legt fest, wie die Farben aus der Datei interpretiert werden: `Auto`, `Linear` oder `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Doppelte UVs zusammenführen {#merge-duplicate-uvs-fbx}
Führt Texturkoordinaten zusammen, die dieselbe UV haben.

#### ![](/icons/paint.webp) Farbraum {#color-space-fbx}
Legt fest, wie die Farben aus der Datei interpretiert werden: `Auto`, `Linear` oder `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Das Normal-Map-Format der Texturen: `Auto`, `OpenGL (+Y)` oder `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Farbraum {#color-space-usd}
Legt fest, wie die Farben aus der Datei interpretiert werden: `Auto`, `Linear` oder `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Das Normal-Map-Format der Texturen: `Auto`, `OpenGL (+Y)` oder `DirectX (-Y)`.



## Exportieren {#export}
Speichert in einem 3d-Geometrieformat, das sich in anderer Software verwenden lässt. 

![](/images/file_export.webp)

Die Dateiformate unterstützen unterschiedliche Funktionen, daher ändern sich die verfügbaren Optionen je nach gewähltem Dateityp.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex-Farben](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex-PBR](#pbr-paint)        | ✅     | Nomad ✅<br>Andere ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quads                           | ✅     | Nomad ✅<br>Andere ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layer](#layers)                | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objekte                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face-Gruppe                     | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchie                      | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lichter                         | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Texturen                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Grundformen, Nachbearbeitung usw. | ✅   | Nomad ✅<br>Andere ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Export-Button {#export-button}
Tippen Sie hierauf, um die Geometrie mit den gewählten Einstellungen zu exportieren. Der Button zeigt das gewählte Format und eine Schätzung der Dateigröße. Unter Android sendet ein Button `Teilen` daneben die Datei direkt an eine andere App.

### Dateiformat {#file-format}
Wählen Sie das Exportformat: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` oder `USD`. NOMAD ist das eigene Format von Nomad und lässt sich in anderer Software nicht öffnen. Es dient also vor allem dazu, wieder in Nomad zu importieren.

### Beinhalten {#allvisibleselected}
Legt fest, welche Objekte exportiert werden: `Alle`, `Sichtbar` oder `Ausgewählt`. Die Zahl neben jeder Option zeigt, wie viele Objekte exportiert werden.

### Eine Datei pro Objekt {#one-file-per-object}
Exportiert jedes Objekt in eine eigene Datei. Die Zahl zeigt, wie viele Dateien geschrieben werden.

### Typ {#type}
Schreibt der Export mehrere Dateien (eine Datei pro Objekt oder OBJ mit Texturen), werden sie in einem `Ordner` oder einer `Zip`-Datei gespeichert. Einige Apps (Google Drive, One Drive usw.) unterstützen keinen Ordnerimport, dann verwenden Sie stattdessen Zip.

### Verlauf einbetten {#embed-history}
Nur NOMAD. Speichert den Rückgängig-Verlauf in der Datei, er wird beim Öffnen der Datei in Nomad wiederhergestellt. Das vergrößert die Datei, und die ganze Szene muss als einzelne Datei exportiert werden.

### Ressourcen einbetten {#embed-assets}
Nur NOMAD. Speichert Ihre eigenen MatCaps, Umgebungen und Schriftarten in der Datei. Mitgelieferte Ressourcen werden nicht eingebettet.

### Vertex-Farben {#vertex-colors}
Exportiert die Vertex-Farben, sofern das Dateiformat sie unterstützt. Manche 3d-Software kann sie lesen, aber nicht jede.

Bei OBJ haben Sie die Wahl:
* `Keine` - Keine Farben.
* `RGB` - Die Farben werden hinter den Vertices angehängt.
* `MRGB (ZBrush)` - Eine andere Art, Farben zu speichern, die auch Maskendaten unterstützt.

### Farbraum {#color-space-export}
Nur OBJ mit `RGB`-Vertex-Farben. Schreibt die Farben als `Linear` oder `sRGB`.

### PBR-Bemalung {#pbr-paint}
Exportiert die Bemalung von Rauheit, Metallizität und Maskierung. Andere Software ignoriert diese Daten unter Umständen.
PBR-Vertex-Farben werden als zusätzliche Vertex-Farbattribute exportiert.
Die Kanäle sind folgendermaßen belegt:

|           | Kanal    |
| :-------: | :------: |
| Rauheit   | R        |
| Metallizität | G     |
| Maskierung | B       |


### Layer {#layers}
Layer werden über glTF-Morph-Targets unterstützt. Das ist offiziell Teil von glTF und sollte daher auch in anderer Software funktionieren.
Nomad exportiert außerdem Farben, Rauheit und Metallizität pro Layer, diese werden von anderer Software aber ignoriert.

### Zusätzliche Material-Layer {#layer-painting}
Exportiert die Bemalung der Layer, wird von anderer Software meist ignoriert.

### Face-Gruppe {#face-group}
Exportiert die Face-Gruppen. Das kann in anderer Software manchmal zu Problemen führen.

### Objekte schreiben {#write-objects}
Nur OBJ. Hält die Objekte getrennt. Deaktivieren Sie die Option, um alles als ein einziges Objekt zu exportieren, zum Beispiel für die Funktion „Mesh ID / Polygroup“ von Substance Painter.

### Normale {#normals}
Exportiert die Normaleninformationen. Beachten Sie, dass Nomad beim Import anderer Dateiformate seine Normalen immer selbst berechnet.

### Tangenten {#tangents}
Exportiert die Tangenteninformationen, die verwendet werden, wenn das Modell Normal Maps hat. 

### Texturen {#textures}
Wurden dem Material Texturen hinzugefügt, werden sie mit exportiert. Beachten Sie, dass dabei keine Texturen gebacken werden, das geschieht über die Backoptionen unter Topologie.

### Format {#fbx-format}
Nur FBX. `Binär` ist kleiner, funktioniert aber vielleicht nicht in jeder Anwendung, `ASCII` ist eine Textdatei.

### Komprimiert {#compressed}
Nur FBX. Verkleinert die Datei, dafür dauern Export und Import länger.

### Preset {#usd-preset}
Nur USD. Wählen Sie die App, für die Sie exportieren: `OpenUSD`, `Apple`, `Procreate` oder `Zbrush`. Manche Optionen gibt es nur bei bestimmten Presets.

### Instanz {#instance}
Nur USD. Exportiert instanzierte Objekte als Instanzen, statt ihre Geometrie zu duplizieren.

### Neigung erlauben {#allow-skew}
Nur USD. Erlaubt Scherungen in den Transformationsmatrizen. Ist die Option aus, teilt Nomad gescherte Transformationen in separate Skalierungs- und Rotationstransformationen auf.

### Repeater {#repeater}
Nur USD. Exportiert die von Repeatern erzeugten Kopien als Instanzen.

### Kopien vereinen {#join-copies}
Jedes Objekt wird mit seinen Repeater-Kopien zu einem einzigen Objekt.

::: tip Tipp: Rauheit und Metallizität in Blender importieren

Blender kann glTF/glb importieren, versteht aber die Vertex-Attribute für Metallizität und Rauheit nicht automatisch. Um sie zu nutzen, erstellen Sie im Material-Editor einen Vertex-Color-Node und stellen seine Eigenschaft auf das nächste Farbattribut (meist Col.001). Verbinden Sie ihn mit einem Node „Separate XYZ“ und leiten Sie X zu Roughness und Y zu Metallic.

Dieses Video zeigt den Ablauf:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tipp: Unterstützte USD-Funktionen

USD ist ein komplexes Format. Seine Spezifikation unterstützt viele Funktionen, aber nicht jede 3d-Software unterstützt sie alle. OSX/iOS unterstützen zum Beispiel keine Vertex-Farben. Die Presets im USD-Exporter versuchen, die bestmögliche Kompatibilität mit OpenUSD, Apple, Procreate und Zbrush zu erreichen.

::: 

## ![](/icons/screen.webp) Rendern {#render}

Exportiert ein Bild, das alle Einstellungen des Projekts vereint (Lichter, Materialien, Nachbearbeitung usw.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Vorschau {#preview}

Der Button `Vorschau` neben dem Menütitel macht die Oberfläche durchsichtig, damit Sie den Bildausschnitt des Endergebnisses besser beurteilen können.

### ![](/icons/home.webp) Fokus {#focus}
Rahmt die Szene oder die Auswahl so ein, dass sie in die Rendergröße passt. Tippen Sie erneut, um zwischen beiden zu wechseln.

### ![](/icons/map.webp) Höhenkarte {#heightmap}
Rendert die Szene als Graustufen-Höhenkarte aus Sicht der Kamera, die nächstgelegenen Teile am hellsten. Beim Aktivieren wird auf die Größe `Quadrat` umgeschaltet und die Auswahl eingerahmt. Mit einer kleinen Leiste im Viewport passen Sie den `Fokus` des Verlaufs an.

Ist `Höhenkarte` aktiv, erscheint neben dem Export-Button ein Button `Als Alpha speichern`, um das Rendering als neues Pinselalpha zu speichern, statt eine Datei zu exportieren.

### ![](/icons/opacity.webp) Transparenter Hintergrund {#transparent-background}
Fügt dem Rendering einen Alphakanal hinzu, praktisch, um es in 2d-Programmen mit anderen Bildern zu kombinieren. Teiltransparenz wird nicht unterstützt.

### ![](/icons/sliders.webp) Interface anzeigen {#show-interface}
Nimmt die Oberfläche von Nomad mit in das Rendering auf.

### Endgültige Größe {#final-size}
Die Auflösung des Renderings: `Bildschirm`, `720`, `1080`, `4096`, `Quadrat` oder `Benutzerdefiniert`.

Ist das Menü Dateien aktiv, zeigt eine gestrichelte Überlagerung im Viewport den Renderbereich an, falls er nicht der Bildschirmauflösung entspricht.

### Breite / Höhe {#render-ratio}
Mit `Benutzerdefiniert` legen Sie Breite und Höhe des Bildes fest. Der Verknüpfungsbutton zwischen den beiden Reglern behält das Seitenverhältnis bei, wenn Sie einen davon ändern. Mit `Quadrat` lässt sich nur die Breite einstellen.

### ![](/icons/export.webp) Exportieren → PNG {#export-png}
Tippen Sie auf diesen Button, um das Rendern zu starten. Ist es fertig, wählen Sie, wie Sie das Bild speichern oder teilen möchten. Bei sehr großen Formaten wird zuerst eine Bestätigung abgefragt: Speichern Sie vorher Ihr Projekt, falls Ihrem Gerät der Speicher ausgeht.

## ![](/icons/network.webp) Verbindung {#link}

Verbindet Nomad mit einem anderen Gerät oder einer anderen App, um Objekte zu senden und zu empfangen oder Ihre Änderungen live zu synchronisieren. Ein Gerät stellt die Sitzung bereit, die anderen treten ihr bei.

### GoZ aktivieren {#enable-goz}
Nur Desktop. Tauscht Meshes mit ZBrush auf diesem Computer aus. `Senden` importiert sie in ZBrush, `Abrufen` importiert aus dem laufenden ZBrush: `Auswahl` übernimmt das aktive Subtool, `Szene` alle Subtools. Sie können in ZBrush auch jederzeit GoZ drücken.

### Modus {#link-mode}
* `Aus` - Keine Verbindung.
* `Host` - Dieses Gerät stellt die Sitzung bereit und wartet, bis andere beitreten.
* `Beitreten` - Sucht nach Geräten in der Nähe. Tippen Sie dann auf den Namen des Hosts, um beizutreten.

Um zwei Nomad zu verbinden, wählen Sie auf einem Gerät `Host` und auf den anderen `Beitreten`. Für eine Verbindung mit Blender muss Nomad der Host sein: Der Hilfe-Button neben dem Titel `Verbindung` zeigt, wie Sie die Erweiterung Nomad Blender Link installieren.

### ![](/icons/network.webp) Netzwerkport {#network-port}
Der Netzwerkport, den die Verbindung nutzt. Ändern Sie ihn nur, wenn eine andere App ihn bereits belegt.

### Senden / Abrufen {#send-get}
Sobald die Verbindung steht, senden Sie (`Senden`) Ihre `Auswahl` oder die ganze `Szene` an das andere Gerät oder rufen sie von dort ab (`Abrufen`). `Ersetzen` löscht die aktuelle Szene und ruft dann die Szene des anderen Geräts ab.

### ![](/icons/link.webp) Live-Synchronisierung {#live-sync}
Überträgt Ihre Änderungen während der Arbeit an das andere Gerät. `Arbeitsansicht` synchronisiert auch die Kamera. `Szenenänderungen` legt fest, welches Gerät die Änderungen sendet: `Auto` richtet die Richtung nach der jüngsten Aktivität aus. Wählen Sie dann, was synchronisiert wird: `Objekte und Geometrie`, `Materialien`, `Lichter`, `Kameras` und, wenn die Gegenseite es unterstützt, `Shading` und `Nachbearbeitung`.

::: tip
Bestehende Objekte brauchen zuerst einmal `Senden` oder `Abrufen`, damit sie verknüpft sind, bevor die Live-Synchronisierung sie aktualisieren kann.
:::
