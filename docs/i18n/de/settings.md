# ![](/icons/cog.webp) Einstellungen {#reset-to-default}

Das Einstellungsmenü enthält viele Optionen, mit denen Sie Aussehen und Verhalten von Nomad steuern.

![](/images/settings_overview.webp)

Die Reihe von Schaltflächen oben im Menü springt direkt zu einem Abschnitt: `Cursor`, `Indikator`, `Draht`, `Raster`, `Backface`, `Umriss`, `Hervorheben`, `Ansichten-Würfel`, `Statistik`, `Griffe`, `Form`, `Repeater` und `Multiaufl.`.

## Anzeigeeinstellungen {#display-settings}
Dieser Abschnitt enthält Schnellzugriffe auf die meisten Einstellungen weiter unten in diesem Menü.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Smooth Shading {#smooth-shading}
Wechselt zwischen glattem und facettiertem Shading. Im facettierten Modus werden die Polygone einzeln schattiert, sodass Sie die zugrunde liegende Topologie sehen.
Es kann nützlich sein, beim Sculpten das facettierte Shading zu verwenden und für das Rendering auf glattes Shading umzuschalten.

Das Deaktivieren von Smooth Shading verbessert die Leistung ein wenig.

### ![](/icons/outline.webp) Umriss {#outline-quick}
Blendet einen Umriss um Ihre aktuelle Auswahl ein und aus.

Das ist nützlich, um zu sehen, welche Meshes gerade ausgewählt sind, falls [Nicht gewählte Meshes abdunkeln](#darken-unselected-objects) deaktiviert ist.

Was die Leistung angeht, ist [Nicht gewählte Meshes abdunkeln](#darken-unselected-objects) deutlich besser als der Umriss.

### ![](/icons/grid.webp) Raster {#grid-quick}
Blendet ein Hintergrundraster ein und aus; nützlich, um Platzierung und Größe von Objekten einzuschätzen.

### ![](/icons/culling.webp) Backface {#two-sided-quick}
Schaltet die beidseitige Darstellung der Polygone ein und aus. Jede Fläche zeigt in eine bestimmte Richtung.
Als *Rückseite* (Backface) gelten Flächen, die vom Blickpunkt der Kamera „weg“ zeigen.

Bei der einfachen Kugel beim Start zeigen die Flächen zum Beispiel nach außen.
Wenn Sie die Kamera in die Kugel hineinbewegen, sehen Sie die Rückseiten dieser Flächen.

Normalerweise sollten Sie keine Rückseiten sehen. Wenn Sie sie einfärben, erkennen Sie also leichter mögliche Probleme oder fehlerhafte Topologie.

Das Deaktivieren der Darstellung `Backface` kann die Render-Leistung etwas verbessern.


### ![](/icons/wireframe.webp) Drahtgitter {#wireframe-quick}
Blendet eine Drahtgitter-Überlagerung ein und aus.

Beachten Sie, dass das Drahtgitter die Leistung verringert.

### ![](/icons/snap_cube.webp) Ansichten-Würfel {#snap-cube-quick}
Blendet ein Hilfs-Icon in der Ecke der Szene ein und aus; nützlich, um sich im Raum zu orientieren und schnell zwischen den Ansichten von vorne/hinten/links/rechts/oben/unten zu wechseln.

### ![](/icons/palette.webp) Painting anzeigen {#show-painting}
Schaltet die Anzeige der Bemalung ein und aus. Ist sie ausgeschaltet, werden die Objekte statt mit ihrer Bemalung mit einem weißen, nicht-metallischen Material mit 25 % Rauheit angezeigt.

### ![](/icons/tool_hide.webp) Ausblenden verwenden {#use-hide}
Schaltet den Ausblendmodus ein und aus. Ausgeschaltet bleibt die Ausblendung erhalten, ist aber deaktiviert. Diese Schaltfläche ist deaktiviert, wenn Sie gerade das Ausblenden-Werkzeug verwenden.

### ![](/icons/shield.webp) Maske anzeigen {#show-mask}
Schaltet den Maskenmodus ein und aus. Ausgeschaltet bleibt die Maske erhalten, ist aber deaktiviert. Tippen Sie erneut auf die Schaltfläche, um sie wieder zu aktivieren.

Wenn Sie die Maske ausblenden möchten, sie aber trotzdem aktiv bleiben soll, stellen Sie die Maskenfarbe weiter unten auf Weiß. Denken Sie daran, sie danach wieder auf ein Grau zurückzustellen!

Beachten Sie, dass diese Schaltfläche deaktiviert ist, wenn Sie gerade ein Maskenwerkzeug verwenden.

### ![](/icons/shield.webp) Maske → Opak {#mask-opaque}
`Maske → Opak` ignoriert transparente Vertices für die maskierte Maske. Das betrifft nur die Vertex- und Textur-Deckkraft; Flächen, die mit „Ausblenden“ verborgen wurden, bleiben weiterhin verborgen. Die Option ist nur verfügbar, solange `Maske anzeigen` aktiviert ist.

### ![](/icons/bang.webp) Hervorheben {#highlight-quick}
Schaltet das kurze Aufblitzen der Auswahl ein und aus. Beim Auswählen von Objekten blitzt das ausgewählte Objekt kurz für 500 Millisekunden auf. Farbe und Dauer des Aufblitzens können Sie weiter unten anpassen.

### ![](/icons/list.webp) Statistik {#stats-quick}
Blendet die Statusanzeige im 3d-Viewport ein und aus. Sie zeigt Informationen über Ihren Arbeitsspeicher, die Gesamtzahl der Vertices in der Szene und die Vertex-Anzahl der aktuellen Auswahl.

----- 

### ![](/icons/cube.webp) Nicht gewählte Meshes abdunkeln {#darken-unselected-objects}
Nicht ausgewählte Objekte werden abgedunkelt, damit die aktuelle Auswahl hervorsticht.

### ![](/icons/shield.webp) Maske {#mask}
Die Farbe für die Maskierung, standardmäßig ein mittleres Grau, das mit der Farbe Ihres Objekts multipliziert wird. Stellen Sie sie auf Weiß, um die Maske unsichtbar zu machen, aber denken Sie daran, sie danach wieder auf ein Grau zurückzustellen!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Kreis {#show-circle-while-sculpting}
Wann der Kreis für den Pinselradius angezeigt wird:

* `Auto` - zeigt den Kreis an, blendet ihn aber beim Sculpten aus.
* `Nein` - zeigt den Kreis nie an.
* `Ja` - zeigt den Kreis immer an, auch beim Sculpten.

### Kleinen Punkt anzeigen {#show-small-dot}
Zeigt beim Sculpten einen Punkt in der Mitte des Pinselstrichs an, oder wenn sich der Drehpunkt der Kamera ändert.

### Rope-Stabilisator anzeigen {#show-rope-stabilizer}
Zeichnet eine Linie, die die Seillänge anzeigt, wenn in den Strich-Einstellungen der [Lazy Rope Stabilisator](stroke.md#lazy-rope-stabilizer) aktiv ist.

### Rollhinweis anzeigen {#show-roll-hint}
Zeigt die Hilfslinie für die Rollrichtung an, während Sie eine Tastenbelegung zum Rollen verwenden.

### ![](/icons/radius.webp) Größe {#dot-size}
Die Größe des kleinen Punkts.

### Farben {#cursor-colors}
Der Cursor ändert seine Farbe je nachdem, was Sie gerade tun: `Bearbeiten`, `Hintergrund` (über dem Hintergrund schweben), `Maske`, `Glätten`, `Kamera` und `Radius`. Jede Farbe lässt sich hier anpassen.

## ![](/icons/cursor.webp) Indikator {#indicator}
![](/images/settings_indicator.webp)

Zeigt visuelle Indikatoren für Tutorials und Bildschirmaufnahmen an. Stellen Sie die Option auf `Ja`, um sie einzuschalten (unter iOS gibt es außerdem die Option `Auto`).

Die Schaltflächen `Finger`, `Stylus` und `Maus` lassen ein Icon erscheinen, sobald diese Art von Eingabe erkannt wird.

### Farbe {#indicator-color}
Die Farbe des Indikators.

### Größe/Icon/Kreis {#indicator-shape}
Regler für die Größe des Indikators und für die Deckkraft von Icon und Kreis im Indikator.

## ![](/icons/wireframe.webp) Drahtgitter {#wireframe}
![](/images/settings_wireframe.webp)
Aktiviert die Drahtgitter-Überlagerung.

### Ziel {#target}
Legt fest, ob das Drahtgitter bei nicht ausgewählten Objekten, nur bei ausgewählten Objekten oder bei allen Objekten angezeigt wird.

### Ausblenden {#hide}
Legt fest, ob das Drahtgitter auch für ausgeblendete Polygone angezeigt wird.

### Multiauflösung: Nur Ebene 0 {#multiresolution-level-0-only}
Bei der Multiauflösung wird das Drahtgitter der Stufe 0 dunkler angezeigt und das der höheren Stufen zunehmend heller. Ist diese Option aktiviert, wird nur das Drahtgitter der Stufe 0 angezeigt.

### Farbe {#wireframe-color}
Legt Farbe und Deckkraft des Drahtgitters fest.

## ![](/icons/grid.webp) Raster {#grid}
![](/images/settings_grid.webp)
Aktiviert das Raster.

### Einrasten {#snap}
Mit diesen Optionen rasten die Punkte von kurven- und formbasierten Werkzeugen (`Drehbank`, `Röhre`, Polygon- und Pfadformen...) beim Zeichnen ein:

* `Am Raster einrasten` - rastet am Raster ein.
* `An Punkten einrasten (ausgerichtete Ansicht)` - rastet an nahe gelegenen vorhandenen Punkten ein, wenn die Kamera an einer Achse ausgerichtet ist.
* `An Punkten einrasten (freie Ansicht)` - rastet an nahe gelegenen vorhandenen Punkten ein, wenn die Kamera nicht ausgerichtet ist.

### Farbe {#grid-color}
Legt Farbe und Deckkraft des Rasters fest. Diese Optionen erscheinen, wenn das Raster sichtbar ist.

`Vignette` lässt das Raster zu seinen Rändern hin ausblenden. `Einrastschwelle für Unterteilungen` legt in Pixeln fest, wie dicht die Rasterlinien auf dem Bildschirm werden dürfen, bevor das Raster zu einer anderen Unterteilungsstufe wechselt.

## ![](/icons/culling.webp)Backface {#two-sided}
Macht Polygonflächen von beiden Seiten sichtbar.

### Backface-Farbe {#backface-color}
`Backfaces einfärben` aktiviert das Einfärben der Rückseiten, und `Backface-Farbe` legt die Farbe dafür fest.

## ![](/icons/outline.webp)Umriss {#outline}
Aktiviert einen Umriss um die ausgewählten Objekte.

### Umrissfarbe, Stärke {#outline-color-thickness}
Legt Farbe und `Stärke` des Umrisses fest.


## ![](/icons/bang.webp) Hervorheben {#highlight}
Aktiviert ein kurzes Aufblitzen, wenn sich die Auswahl ändert.
### Farbe, Dauer {#color-duration}
Legt Farbe und Dauer des Aufblitzens in Millisekunden fest.

## ![](/icons/snap_cube.webp) Ansichten-Würfel {#snap-cube}
![](/images/settings_snapcube.webp)

Zeigt ein Hilfs-Icon in der Ecke der Szene an; nützlich, um schnell zwischen den Ansichten von vorne/hinten/links/rechts/oben/unten zu wechseln. Tippen Sie auf die Seiten des Würfels, um zwischen den orthographischen Ansichten zu wechseln.

### Form {#shape}
Wählen Sie für den Ansichten-Würfel zwischen einer Kugel, einem Würfel oder einem Achsenkreuz.

### Ausrichtung einschränken {#restrict-alignment}
Richtet die Einrast-Ansichten an den Weltachsen aus. Ist die Option aktiviert, sind nur die 6 Hauptansichten möglich. Bei `Auto` gilt diese Einschränkung nur, wenn sich die Kamera im Modus `Orbit` befindet.

### Größe {#size}
Legt die Größe des Ansichten-Würfels fest.

### 180° umdrehen {#flip-180}
Aktiviert ein Tippverhalten: Ist die Ansicht eingerastet, dreht ein Tippen auf die Mitte des Würfels die Ansicht um 180 Grad. Ist die Ansicht zum Beispiel auf vorne eingerastet, springt sie durch Tippen auf den Würfel zur Ansicht von hinten.

### Kanten und Ecken {#edges-corners}
Fügt an den Kanten und Ecken des Würfels zusätzliche Einrast-Ansichten hinzu (die bernsteinfarbenen Zonen). Nicht verfügbar mit dem Achsenkreuz.

### Ziehen mit Drehscheibe {#turntable-drag}
Ziehen am Würfel dreht die Ansicht, ohne die Kamera zu rollen, und hält bei jeder Einrast-Ansicht an. Deaktivieren Sie die Option, um den Würfel stattdessen mit der Rotation `Trackball` zu ziehen. In beiden Fällen bleibt das Ziehen waagerecht oder senkrecht. Bei einer Kamera im Modus `Orbit` wird der Würfel immer auf diese Weise gezogen.

### Position {#snap-position}
Legt fest, in welcher Ecke sich der Ansichten-Würfel befindet.


## ![](/icons/list.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Zeigt Informationen über Ihren Arbeitsspeicher, die Gesamtzahl der Vertices in der Szene und die Vertex-Anzahl der aktuellen Auswahl an.

### Position {#stats-position}
Legt fest, in welcher Ecke die Statistik angezeigt wird.

## ![](/icons/edit_radius.webp) Griff {#handle}
Einstellungen für die Griffe, die Sie im Viewport ziehen, etwa das Gizmo.

### Numerische Eingabe {#gizmo-input}
Erlaubt die Eingabe von Zahlen, wenn Sie auf eines der Steuerelemente des Gizmos tippen.

### Ausblenden bei Interaktion {#hide-on-interaction}
Blendet das Gizmo aus, während Sie damit arbeiten, damit es nicht im Weg ist.

### ![](/icons/opacity.webp) Deckkraft {#handle-opacity}
Die Deckkraft der Griffe.

## ![](/icons/shape_lasso.webp) Form {#shape-settings}
Wie die Formen, die Sie mit Formstrichen zeichnen (Lasso, Rechteck, Kurve...), auf dem Bildschirm aussehen.

### ![](/icons/opacity.webp) Füllung, Umriss {#shape-fill-outline}
Die Deckkraft des Inneren der Form und der Linie um sie herum.

### Farben {#shape-colors}
Die Farbe der Form für jede Art von Werkzeug: `Maske`, `Ausblenden`, `Face-Gruppe` und `Trimmen`.

## ![](/icons/array.webp) Repeater {#primitive-repeaters}
Grenzen für die Kopien, die [Repeater](scene#repeaters) erzeugen (Array, radial, Kurve, Oberfläche). Sie sorgen dafür, dass Nomad reaktionsschnell bleibt, wenn ein Repeater aus dem Ruder läuft.

### ![](/icons/cube.webp) Max. Kopien {#repeater-max-copies}
Die maximale Anzahl an Kopien, die ein einzelner Repeater erzeugt. Viele Objekte machen Nomad zu schaffen, egal wie groß sie sind.

### ![](/icons/cube.webp) Kopien in der Szene {#repeater-scene-copies}
Das Kopienbudget für die gesamte Szene. Eine Low-Poly-Kopie kostet wenig Geometrie, bleibt aber ein vollwertiges Objekt; diese Grenze erreichen kleine Kopien also zuerst.

### ![](/icons/triangle.webp) Max. Faces {#repeater-max-faces}
Das Flächenbudget für alle Kopien in der Szene. Wird es überschritten, verlieren die schwersten Objekte zuerst Kopien.

## ![](/icons/multires.webp) Multiauflösung {#multires}
### Max. Anzahl an Vertices {#multires-lowres-count}
Legt eine Schwelle fest, oberhalb derer keine Multiauflösungs-Unterteilung erlaubt ist, weil Nomad sonst wahrscheinlich abstürzen würde: Nomad prüft vor dem Unterteilen nicht den verfügbaren Speicher. Der Standardwert ist 10 Millionen.
### Schwelle für niedrige Auflösung {#multires-lowres-threshold}
Während Sie die Kamera bewegen, kann eine niedrigere Auflösung des Meshes angezeigt werden. Erhöhen Sie diesen Wert, wenn eine höhere Auflösung des Meshes angezeigt werden soll.

## Einstellungen {#advanced}
### ![](/icons/reset.webp) Zurücksetzen {#reset}
Setzt alle Einstellungen der App auf ihre Standardwerte zurück.

Einige Ressourcen werden separat gespeichert und NICHT zurückgesetzt: Projekte, Tastenbelegungen, Werkzeug-Presets, HDR-Umgebungen, MatCaps, Alphas, Pinseltexturen und Referenzbilder. Alles, was mit dem Projekt gespeichert wird, etwa Beleuchtung, Nachbearbeitung oder Kameraansichten, bleibt ebenfalls erhalten.
