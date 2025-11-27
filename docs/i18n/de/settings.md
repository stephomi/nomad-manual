# ![](/icons/cog.webp) Einstellungen 

Das Einstellungsmenü enthält viele Optionen zur Steuerung des Erscheinungsbilds und des Verhaltens von Nomad.

![](/images/settings_overview.webp)

## Anzeigeeinstellungen
Dieser Abschnitt enthält Schnellzugriffe für die meisten Einstellungen weiter unten in diesem Menü.

![](/images/settings_display_settings.webp)

### Glatte Schattierung 
Zwischen glatter und facettierter Schattierung umschalten. Bei facettierter Schattierung werden die Polygone unabhängig voneinander schattiert, sodass du die zugrunde liegende Topologie sehen kannst.
Es kann nützlich sein, während der Sculpting-Phase die facettierte Schattierung zu verwenden und dann für das Rendering auf glatte Schattierung zu wechseln.

Das Deaktivieren der glatten Schattierung verbessert die Leistung ein wenig.

### Kontur
Eine Kontur um deine aktuelle Auswahl ein- oder ausschalten.

Dies ist nützlich, um visuelles Feedback zu deiner aktuell ausgewählten Mesh(es) zu erhalten, falls [Nicht ausgewählte abdunkeln](#darken-unselected-objects) deaktiviert ist.

Aus Leistungssicht ist die Verwendung von [Nicht ausgewählte abdunkeln](#darken-unselected-objects) deutlich besser als die Kontur-Lösung.

### Gitter
Ein Hintergrundgitter ein- oder ausschalten, nützlich zum Verständnis von Objektplatzierung und Maßstab.

### Zweiseitig
Zweiseitige Polygonanzeige ein- oder ausschalten. Alle Flächen zeigen in eine bestimmte Richtung.
Flächen, die als *Rückseite* gelten, sind diejenigen, die „von“ der Kameraposition „weg“ zeigen.

Zum Beispiel zeigen beim Start die Flächen der einfachen Kugel nach außen.
Wenn du die Kamera in die Kugel hineinbewegst, siehst du dann die Rückseite dieser Flächen.

Meistens solltest du die Rückseite von Flächen nicht sehen, daher kann das Einfärben helfen, potenzielle Probleme oder fehlerhafte Topologie zu erkennen.

Das Deaktivieren des `zweiseitigen` Renderings kann die Renderleistung etwas verbessern.


### Drahtgitter
Ein Drahtgitter-Overlay ein- oder ausschalten. 

Beachte, dass das Aktivieren des Drahtgitters die Leistung verringert.

### Snap-Würfel
Ein Hilfssymbol in der Ecke der Szene ein- oder ausschalten, nützlich zur Orientierung im Raum und zum schnellen Wechsel zwischen Vorder-/Rück-/Links-/Rechts-/Oben-/Unten-Ansichten.

### Malen anzeigen
Die Farbdarstellung ein- oder ausschalten. Die standardmäßig verwendete Farbe ist ein weißes, nichtmetallisches Material mit 25 % Rauheit.

### Verbergen verwenden
Den Verbergen-Modus ein- oder ausschalten. Wenn er ausgeschaltet ist, ist er weiterhin vorhanden, nur deaktiviert. Diese Schaltfläche ist deaktiviert, wenn du aktuell das Verbergen-Werkzeug verwendest.

### Maske anzeigen
Den Maskenmodus ein- oder ausschalten. Wenn er ausgeschaltet ist, ist er weiterhin vorhanden, nur deaktiviert. Drücke diese Schaltfläche erneut, um ihn wieder zu aktivieren.

Wenn du die Maske ausblenden UND trotzdem aktiv haben möchtest, verwende die Maskenfarbe unten und setze sie auf Weiß. Denk daran, sie wieder auf ein Grau zu stellen, wenn du fertig bist!

Beachte, dass diese Schaltfläche deaktiviert ist, wenn du aktuell ein Maskenwerkzeug verwendest. 

### Maske -> Deckend
Maske -> deckend ignoriert transparente Vertices für maskierte Masken. Dies ist nur für Vertex- und Textur-Deckkraft relevant, durch „Verbergen“ ausgeblendete Flächen bleiben weiterhin verborgen.

### Hervorhebung
Das Aufblitzen der Auswahlhervorhebung ein- oder ausschalten. Beim Auswählen von Objekten wird das ausgewählte Objekt für 500 Millisekunden kurz in kräftigem Pink aufblitzen. Farbe und Dauer des Aufblitzens können unten angepasst werden.

### Statistiken
Die Statusanzeige im 3D-Viewport ein- oder ausschalten. Sie zeigt Informationen über deinen Systemspeicher, die Gesamtanzahl der Vertices in der Szene und die Vertexanzahl der aktuellen Auswahl an.

----- 

### Nicht ausgewählte Objekte abdunkeln
Objekte, die nicht ausgewählt sind, werden abgedunkelt, sodass die aktuelle Auswahl hervorsticht.

### Maske
Die für Maskierung verwendete Farbe, standardmäßig ein mittleres Grau, das mit deiner Objektfarbe multipliziert wird. Setze dies auf Weiß, um die Maske unsichtbar zu machen, aber denk daran, sie wieder auf ein Grau zu stellen, wenn du fertig bist!

## ![](/icons/cursor.webp) Cursor

### Kreis beim Sculpten anzeigen
Den Pinselradius während des Sculptens weiterhin anzeigen.

### Kleinen Punkt anzeigen
Einen Punkt im Zentrum des Pinselstrichs während des Sculptens oder wenn der Kamerapivot geändert wird anzeigen.

### Seil-Stabilisator anzeigen
Eine Linie zeichnen, um die Seillänge anzuzeigen, wenn der Lazy-Rope-Stabilisator in den Stricheinstellungen aktiv ist.

## ![](/icons/cursor.webp) Indikator
![](/images/settings_indicator.webp)

Visuelle Indikator(en) für Tutorials und Bildschirmaufnahmen anzeigen.

Die Schaltflächen `Finger`, `Stift` und `Maus` aktivieren die Anzeige eines Symbols, wenn diese Art von Eingabe erkannt wird.

### Farbe
Die Farbe des Indikators.

### Größe/Icon/Kreis
Steuerelemente zur Anpassung der Größe des Indikators und der Formen innerhalb des Indikators.

## ![](/icons/wireframe.webp) Drahtgitter
![](/images/settings_wireframe.webp)
Das Drahtgitter-Overlay aktivieren.

### Ziel
Festlegen, ob nicht ausgewählte Objekte ein Drahtgitter anzeigen, oder nur ausgewählte Objekte, oder alle Objekte.

### Verbergen
Festlegen, ob das Drahtgitter auch für verborgene Polygone angezeigt wird.

### Multiresolution: Nur Level 0
Multiresolution zeigt Drahtgitter für Level 0 dunkler und höhere Level schrittweise heller an. Wenn aktiviert, zeigt diese Option nur das Drahtgitter von Level 0 an.

### Farbe
Farbe und Deckkraft für das Drahtgitter festlegen.

## ![](/icons/grid.webp) Gitter
![](/images/settings_grid.webp)
Das Gitter aktivieren.

### Farbe
Gitterfarbe und Deckkraft festlegen.

### Einrasten
Einrasten für kurvenbasierte Werkzeuge am Gitter aktivieren.

## ![](/icons/culling.webp)Two sided
Das Anzeigen von Polygonflächen von beiden Seiten aktivieren.

### Rückseite einfärben, Rückseitenfarbe
Einfärben der Rückseiten aktivieren und die Einfärbefarbe festlegen.

## ![](/icons/outline.webp)Outline
Eine Kontur um das aktive Objekt aktivieren.

### Konturfarbe, Dicke
Farbe und Dicke der Kontur festlegen.


## ![](/icons/bang.webp) Hervorhebung
Ein kurzes Aufblitzen aktivieren, wenn das aktive Objekt geändert wird.
### Farbe, Dauer
Farbe und Dauer des Aufblitzens in Millisekunden festlegen.

## ![](/icons/snap_cube.webp) Snap-Würfel
![](/images/settings_snapcube.webp)

Ein Hilfssymbol in der Ecke der Szene anzeigen, nützlich zum schnellen Wechsel zwischen Vorder-/Rück-/Links-/Rechts-/Oben-/Unten-Ansichten. Tippe auf die Seiten des Würfels, um zwischen orthografischen Ansichten zu wechseln.

### Form
Zwischen einem Würfel, einer Kugel oder einer Gnomon-Form für den Snap-Würfel wählen.

### Ausrichtung beschränken
Sperren der Kamerarotation beim Ziehen am Snap-Würfel aktivieren. Wenn aktiv, wird eine Ziehbewegung am Snap-Würfel nur nach links/rechts oder oben/unten ausgeführt.

### Größe
Die Größe des Snap-Würfels festlegen.

### 180° drehen
Ein Tippverhalten aktivieren, sodass bei eingerasteter Ansicht ein Tippen auf die Mitte des Würfels die Ansicht um 180 Grad dreht. Wenn zum Beispiel die Ansicht auf „Vorne“ eingerastet ist, dreht ein Tippen auf den Würfel zur Rückansicht.

### Position
Festlegen, in welcher Ecke sich der Snap-Würfel befindet.


## ![](/icons/edit_radius_n.webp) Statistiken
![](/images/settings_stats.webp)

Informationen über deinen Systemspeicher, die Gesamtanzahl der Vertices in der Szene und die Vertexanzahl der aktuellen Auswahl anzeigen.

### Position
Festlegen, in welcher Ecke die Statistiken angezeigt werden.

## Primitive/Wiederholer
## Numerische Eingabe
Numerische Eingabe beim Tippen auf die Gizmo-Widgets erlauben.

## Multiresolution
### Maximale Vertexanzahl
Einen Schwellenwert festlegen, um eine Multires-Subdivide-Operation oberhalb dieser Polygonanzahl zu verhindern, da dies Nomad wahrscheinlich zum Absturz bringen würde. Der Standardwert ist 10 Millionen.
### Niedrigauflösungs-Schwellenwert
Eine niedrigere Auflösung des Meshes kann angezeigt werden, wenn du die Kamera bewegst. Du kannst diesen Wert erhöhen, wenn du eine höhere Auflösung des Meshes anzeigen möchtest.

## Einstellungen
### Auf Standard zurücksetzen
Alle Einstellungen auf ihre Standardwerte zurücksetzen.
