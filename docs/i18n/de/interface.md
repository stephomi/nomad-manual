# ![](/icons/interface.webp) Interface-Menü 

Dieses Menü steuert viele Optionen zur Anpassung der Nomad-Oberfläche. 

![](/images/interface_overview2.webp)

Nomad kann sehr tiefgehend angepasst werden, dieses Menü ist in 4 Bereiche aufgeteilt: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Diese Seite beschreibt das Interface-Menü, nicht die Oberfläche selbst! Die gesamte Oberfläche wird in [Erste Schritte](gettingstarted.md) beschrieben.
:::

## Interface 

Im Interface-Bereich kannst du Shortcuts hinzufügen, schwebende Werkzeugleisten erstellen sowie Farbe, Größe und Erscheinungsbild der Nomad-Benutzeroberfläche steuern.

![](/images/interface_overview3.webp)

### Shortcuts hinzufügen (unten)...
![](/images/interface_shortcuts.webp)

In der unteren Werkzeugleiste sind standardmäßig diese Shortcuts aktiviert:
* `Undo` – macht die letzte Aktion rückgängig
* `Redo` – stellt die zuletzt rückgängig gemachte Aktion wieder her
* `Solo` – blendet vorübergehend alle anderen Objekte aus, sodass nur das ausgewählte sichtbar bleibt. Erneutes Drücken stellt alle Objekte wieder her.
* `X-ray` – macht vorübergehend alle anderen Objekte halbtransparent, sodass nur das ausgewählte Objekt voll sichtbar bleibt. Erneutes Drücken stellt die Standardmaterialien wieder her.
* `Voxel remesh` – Remesht das aktuelle Objekt mit der zuletzt verwendeten Voxelauflösung. Ein langer Tipp oder Wischen nach oben blendet einen Auflösungsslider und einen Schalter für scharfe Kanten ein.
* `Grid` – Schaltet das Raster ein/aus. Ein langer Tipp oder Wischen nach oben ermöglicht es, Farbe und Deckkraft des Rasters zu ändern.
* `Wireframe` – Schaltet ein Wireframe-Overlay ein/aus. Ein langer Tipp oder Wischen nach oben ermöglicht es, Farbe und Deckkraft des Wireframes zu ändern.
* `Inspector` – ermöglicht es, Eigenschaften deines Meshes wie UVs, gebackene Texturen und andere Eigenschaften im Hintergrund von Nomad anzuzeigen.
* `Face Group` – Schaltet das Facegroup-Overlay ein/aus, mehr Infos unter [Tools->FaceGroup](tools.md#facegroup) 

Weitere häufig verwendete Shortcuts sind in diesem Menü verfügbar, viele weitere findest du über die Schaltfläche „Bindings“.

#### ![](/icons/more.webp) Bindings

Fast jede Funktion von Nomad kann über die Bindings-Schaltfläche zur Shortcut-Leiste hinzugefügt werden. Beim Klick auf die Schaltfläche wird ein Bindings-Menü angezeigt:

![](/images/interface_bindings_search.webp)

Du kannst über die Symbole oben nach Kategorien suchen oder das Suchfeld verwenden, um Funktionen nach Namen zu finden. Klicke auf eine Funktion, um sie zur Werkzeugleiste hinzuzufügen. Klicke erneut, um sie zu entfernen.

#### ![](/icons/list.webp) Reihenfolge

Dies zeigt eine Liste der Shortcuts an. Lange drücken und dann ziehen, um die Shortcuts neu anzuordnen.

#### ![](/icons/reset.webp) Zurücksetzen

„Reset“ stellt die untere Werkzeugleiste auf ihre Standardeinstellungen zurück.

### Shortcuts hinzufügen (Fenster)... +
![](/images/interface_add_shortcuts_window.webp)

Durch Klicken auf das + wird eine schwebende Werkzeugleiste hinzugefügt. Sie ist erst sichtbar, wenn du über die Bindings-Schaltfläche Shortcuts hinzufügst und sie dann sichtbar machst. 

Du kannst mehrere Werkzeugleisten erstellen, jede Werkzeugleiste hat in diesem Menü folgende Optionen:

* ![](/icons/checked.webp) `Visible` – Sichtbarkeit der Werkzeugleiste umschalten
* ![](/icons/more.webp)`Bindings` – Bindings-Fenster anzeigen, um Funktionen zur Werkzeugleiste hinzuzufügen oder daraus zu entfernen.
* ![](/icons/list.webp)`Order` – Ein Menü anzeigen, um die Werkzeugleiste neu zu ordnen.
* ![](/icons/reset.webp) `Reset` – Die Werkzeugleiste auf ihren Standardzustand zurücksetzen.
* ![](/icons/resize_bottom_right.webp) `Resize corner` – Einen Größenänderungsgriff in der unteren rechten Ecke der Werkzeugleiste ein-/ausblenden.
* ![](/icons/sort_down.webp) `Collapsable` – Einen Einklapp-Button in der oberen rechten Ecke ein-/ausblenden.
* ![](/icons/trash.webp) `Delete` – Die Werkzeugleiste löschen.

### Toolbox

Optionen für das Werkzeugmenü auf der rechten Seite der Nomad-Oberfläche.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

Einen Größenänderungsgriff in der unteren Ecke der Werkzeugleiste ein-/ausblenden.

#### Hidden
Normalerweise schaltet das Toolbox-Symbol in der oberen Leiste zwischen einer langen einspaltigen oder einer mehrspaltigen Werkzeugliste um. Diese Option schaltet zwischen der mehrspaltigen Liste und „ausgeblendet“ um.

#### Colored
Farbcodierung der Symbole nach Kategorie, z. B. alle Masken-Tools braun, Split-Tools rot, Flatten-Tools grün usw.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
Setzt die Standardwerkzeuge in der Toolbox auf die Standardreihenfolge zurück. Benutzerdefinierte Symbole bleiben in der Toolbox am Ende der Liste erhalten.


### Presets

![](/images/interface_presets.webp)

Eine Sammlung von Farbpresets für die Oberfläche.

#### High-contrast button
Ein alternativer Stil für Buttons, der sie bei aktiviertem Zustand besser sichtbar macht. Wenn auf Auto gesetzt, verwendet Nomad diesen Modus, wenn der UI-Farbkontrast zwischen aktiviert/deaktiviert gering ist.

#### Color widget/Color base
Die Hauptfarben, die in der Oberfläche verwendet werden.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
Wenn aktiviert, erscheinen zusätzliche Optionen zur Steuerung des Aussehens von Menüs und Panels in Nomad. Deren Farbe, Transparenz und Unschärfegrad können angepasst werden.

::: tip
Auf kleinen Geräten kann es hilfreich sein, das Farbpanel fast weiß, transparent und mit geringer Unschärfe zu gestalten, damit Menüs die Szene nicht verdecken.
:::

----

### Mirror top bar
Die Reihenfolge der Menüs in der oberen Leiste umkehren.

### Mirror side bars
Die Seitenleisten vertauschen, sodass die Toolbox links und die Werkzeugoptionen rechts sind.

### Mirror bottom bar
Die untere Leiste in die untere rechte Ecke verschieben und die Button-Reihenfolge umkehren.

### Material color preview
Wenn du eine Farbe für ein Material auswählst, wird eine Vorschau dieses Materials auf dem aktuell ausgewählten Objekt angezeigt.

----
### Help popup on hover

Für Geräte, die Hover unterstützen: Legt fest, ob die kontextbezogene Hilfe in Nomad, dargestellt durch das ![](/icons/help.webp)-Symbol, beim Hover oder nur beim Klicken erscheint.

----

### Overall scale
Ein Größenmultiplikator für alle UI-Elemente.
### Panel width
Die Breite der Menüs und Panels.
### Font scale
Skalierung der Schriftarten.
### Vertical spacing
Der Abstand zwischen Elementen in Menüs und Panels.
### Vertical spacing (left)
Der Abstand zwischen Elementen in der linken Werkzeugleiste.

----

### Edge offset
Du solltest diese Werte nur ändern, wenn du Probleme bei der Interaktion mit Buttons an den Bildschirmrändern hast. Wenn diese Slider deaktiviert sind, verwendet Nomad die vom Gerät selbst zurückgegebenen Safe-Area-Werte.

::: tip
Wenn du Nomad auf ein neues Gerät überträgst (z. B. Austausch eines iPhone 12 durch ein iPhone 15), setze die Randoptionen unbedingt auf die Standardwerte zurück!
:::

### Reset style
Setzt alle UI-Elemente auf ihre Standardwerte zurück.


## Gesture
Das Gesture-Menü steuert, wie Stift- und Finger-Eingaben Nomad steuern.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad kann Aktionen basierend auf dem Eingabegerät einschränken. Beispielsweise kann ein Finger-Drag nur die Kamera bewegen, während ein Stift-Drag nur skulptiert. Wenn du eine Maus oder ein Trackpad hast, können diese ebenfalls bestimmten Aktionen zugewiesen werden.

Nomad erlaubt es derzeit, diese Modi für beliebige Kombinationen aus Finger-, Stift- oder Maus-Gesten festzulegen:

* Camera
* Sculpt
* Gizmo
* Material picking (per langem Druck)
* Select object


`Finger always smooths` – Smooth kann so eingestellt werden, dass es nur bei Finger-Drags funktioniert.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` – Aktiviert die folgenden One-Tap-Shortcuts, ohne dass du die Masken-Schaltfläche halten musst. Es erlaubt folgende Gesten:
* Tipp auf den Hintergrund, um die Maske zu invertieren
* Tipp auf einen maskierten Bereich, um die Maske zu verwischen
* Tipp auf einen unmaskierten Bereich, um die Maske zu schärfen

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` – Langes Drücken schaltet zwischen Mask und SelMask um und startet einen neuen Strich. Am Ende des Strichs wird das vorherige Tool wieder ausgewählt. 
* `Tool` – Langes Drücken und Loslassen ohne Bewegung, um zwischen Mask und SelMask zu wechseln. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` aktiviert die folgenden Shortcuts mit dem Hide-Tool:
* Tipp auf eine Face Group, um sie zu verstecken
* Tipp in den leeren Raum, um die versteckten Polygone zu invertieren

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

Wenn dein Gerät 3-Finger-Gesten unterstützt, kannst du hier Shortcuts für diese Geste konfigurieren. 

Die Optionsmatrix erlaubt es, vertikale und horizontale Drags als separate Shortcuts zu definieren. Beachte, dass wenn dieselbe Geste für 2 Optionen gewählt wird, eine davon deaktiviert wird.

* `Rotate lighting` – Dreht Environment, Lichter und Matcap.
* `Tool Radius` – Bearbeitet den Werkzeugradius.
* `Tool Intensity` – Bearbeitet die Werkzeugintensität. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` – wenn aktiviert, sind folgende Gesten aktiv:
* Undo – Tipp mit 2 Fingern
* Redo – Tipp mit 3 Fingern

`Long press` – wenn aktiviert, führt das Halten von 2/3 Fingern ein schnelles Undo/Redo aus.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` blendet eine schwebende Werkzeugleiste ein, um Drag-, Pinch-, Roll- und Kameraaktionen zu steuern.

### Camera
Ein Shortcut zum `Camera`-Menü (Kameraoptionen befanden sich früher hier, wurden aber ins Kamera-Menü verschoben).

### Pencil double tap -> Bindings 

Ein Shortcut zum `Bindings`-Menü (Pencil-Tap- und Doppeltipp-Optionen befanden sich früher hier, wurden aber ins Bindings-Menü verschoben).


## Bindings
Tastatur- und Button-Shortcuts können im Bindings-Menü definiert werden:

![](/images/interface_bindings.webp)
Nahezu alle Funktionen in Nomad können an Tastaturkürzel (falls dein Gerät eine Tastatur hat), an zusätzliche Buttons deines Stifts oder sogar an Gamepad-Controller gebunden werden.

Um ein Binding zu erstellen, klicke auf das Rechteck neben der Funktion und drücke die Taste/den Button. 

Finde Funktionen über die Kategoriesymbole oben oder über die Suchleiste nach Namen. 

Einzelne Bindings können über das Kontrollkästchen neben dem Binding-Namen deaktiviert werden.

### ![](/icons/more.webp) Kontextmenü
Das ![](/icons/more.webp)-Symbol hinter jedem Binding öffnet ein Kontextmenü:

![](/images/interface_bindings_context.webp)

* `Clone` – Binding duplizieren
* `Reset` – Binding zurücksetzen
* `Delete` – Binding löschen
* `Toggle shortcut on key tap` – Konfigurieren, ob Tipp vs. langes Drücken unterschiedlich behandelt werden. Wenn aktiviert, schaltet ein Tipp das Tool ein. Ein langes Drücken aktiviert das Tool nur, solange die Taste gedrückt wird; beim Loslassen wird zum vorherigen Tool zurückgekehrt. In anderen 3D-Apps oft „Sticky Keys“ genannt.

### Advanced
Am unteren Rand des Bindings-Menüs befindet sich ein Zahnradmenü für erweiterte Optionen:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` – Ein Tipp auf die Standard-Shortcuts für Mask, Smooth, Gizmo, Hide, Sub schaltet in diesen Modus, aber das Halten der Taste wechselt in diesen Modus und beim Loslassen wird zum vorherigen Modus zurückgekehrt. In anderen 3D-Apps oft „Sticky Keys“ genannt.
* `Toggle tool shortcuts` – Wenn du einen der Tool-Shortcuts verwendest und denselben Shortcut zweimal drückst, wird zum vorherigen Tool umgeschaltet. So kannst du mit demselben Hotkey zwischen zwei Tools hin- und herwechseln.
* `Invert Y (Zooming)` – Invertiert das Zoomen.
* `Reset bindings` – Setzt alle Bindings auf ihre Standardwerte zurück.


## iOS ⌘ Tastaturkürzel-Anzeige

Auf iOS-Geräten mit Tastatur kannst du die ⌘-Taste (cmd) gedrückt halten, um eine Liste der Shortcuts anzuzeigen.

Android-Tastaturunterstützung ist noch etwas experimentell.

![](/images/shortcuts.webp)


## Debug
Einige experimentelle und Debug-Optionen sind in diesem Menü untergebracht. Viele dieser Optionen sollten auf ihren Standardwerten belassen und nur nach Rücksprache mit dem Nomad-Support geändert werden.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` – Nomad normalisiert die UVs innerhalb des [0-1]-Tiles.

### Quad Remesh
* `Instant Mesh` – Aktiviert den Instant-Remesh-Algorithmus
* `Quadriflow` – Eine alternative Quad-Remesh-Methode.

### Render
* `Heightmap` – Ändert den Viewport, um die Tiefe der Szene zu rendern. Dies kann verwendet werden, um Alphamaps für Brushes zu erstellen.
* `Refraction write depth (back)` – Die Rückseite von Refraktionsmeshes wird in den Depth-Buffer geschrieben.
* `Flip Y (normal map)` – Invertiert den Y-Kanal beim Backen von Normalmaps, erforderlich für bestimmte Game- und Render-Engines.
* `Angle weighted smooth normals` – Eine Anpassung der Glättung, die in bestimmten Fällen Falten vermeiden kann.

### Target FPS
Wenn deaktiviert, synchronisiert Nomad seine Frames pro Sekunde mit der Bildwiederholrate deines Displays.

Wenn aktiviert, kannst du die Bildrate einstellen, mit der Nomad rendert.

### Interface
* `Top: layout` 
  * Collapse: Auf kleinen Geräten wird die obere Leiste in weitere Untermenüs eingeklappt. 
  * Scroll: Wenn du Nomad auf großen Displays gewohnt bist und das normale Layout bevorzugst, verwendet diese Option die Standard-Topbar in voller Breite, die scrollbar ist.
  * Multiline: Zeigt das gesamte obere Menü über mehrere Zeilen an.
* `Bottom: draggable popup` – Die untere Werkzeugleiste hat mehrere Buttons, die einen Dialog einblenden. Wenn diese Option aktiviert ist, können diese Dialoge an andere Stellen auf dem Bildschirm verschoben werden.  
* `Toolbox: show all` – Nomad blendet Tools aus, die für die aktuelle Auswahl nicht relevant sind, z. B. werden alle Sculpt-Brushes bei nicht validierten Primitives ausgeblendet. Diese Option dimmt deaktivierte Tools anstatt sie zu verstecken.
* `Toolbox: colored` – Farbcodierung der Toolbox-Symbole basierend auf ihrem Typ.
* `Panel: Drop shadows` – Zeichnet Schlagschatten um Menüs und Panels. Auf manchen älteren Geräten kann dies die Performance beeinträchtigen.
* `Panel: Blending` – Debug-Option
* `Pointer: hovering dot` – Für Geräte mit Stift-Hover-Unterstützung wird ein Punkt angezeigt, wenn der Stift über Menüs und Panels schwebt.

### Gif turntable
Nomad kann ein animiertes GIF-Turntable exportieren. Beachte, dass die Qualität aufgrund von Einschränkungen des GIF-Formats gering ist. Bildschirmaufnahmen sind in der Regel die bessere Methode.

* `Duration` – Wie lange das Turntable in Sekunden dauert
* `Rotation center` – Wo sich der Kamerapivot befindet, also um welchen Teil der Szene die Kamera rotiert
* `Transparent background` – Verwendet die Transparenzoption für GIFs. Beachte, dass GIFs nur 1-Bit-Transparenz unterstützen, wodurch Kanten stark aliasen können.
* `Max frame sampling` – Viele von Nomads hochwertigen Rendereffekten entstehen durch das Kombinieren mehrerer Frames. Dieser Slider legt fest, wie viele Frames kombiniert werden.
* `Export (GIF)` – Startet den GIF-Export.

### Post Process
* `Filtering` – Debug-Option
* `Format` – Debug-Option
* `Buffer reuse` – Debug-Option

### Performance
* `Multicore general` – Debug-Option
* `Multicore sculpting` – Debug-Option
* `Partial Drawing` – Experimentelles Feature! Verwende es, wenn du nur einen relativ kleinen Bereich eines High-Poly-Meshes skulptierst. Es sollte das Sculpting flüssiger machen, du solltest aber kein Wireframe aktivieren! Außerdem kann es während Pinselstrichen zu visuellen Artefakten kommen.

### Feature
* `Flip quad split (on tap)` – Debug-Option
* `Join: merge radius` – Vertices werden beim Zusammenführen von Meshes automatisch verschweißt, wenn sie nah genug beieinander liegen. Du kannst den Radius mit diesem Slider anpassen.

### Debug
* `Logs` – Öffnet ein Log-Fenster
* `App review popup` – Debug-Option
* `FPS` – Fügt den Viewport-Statistiken einen FPS-Zähler hinzu.
