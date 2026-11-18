# ![](/icons/toolbox.webp) Werkzeuge {#tools}

![](/images/tools_menu.webp)

::: tip
Die Beschreibungen der einzelnen Werkzeuge finden Sie weiter unten unter [Werkzeuge](#tools-1).
:::

## Übersicht {#overview}

Werkzeuge wählen Sie in der `Toolbox` rechts aus und steuern sie mit der `Werkzeugsteuerung` links. Weitere Einstellungen finden Sie im Menü `Werkzeug` oben rechts.

Pinselwerkzeuge haben Regler für Größe und Stärke. Auswahlwerkzeuge bieten verschiedene Arten der Auswahl. Unten in der Werkzeugsteuerung gibt es Kurzbefehle für häufig genutzte Aktionen (Glätten, Maske, Ausblenden, Face-Gruppe, Gizmo, Farbe, Alpha).

Die Werkzeuge von Nomad sind in der Toolbox farbig gekennzeichnet (schalten Sie `Farbige Werkzeuge` im Menü [Oberfläche](interface.md) aus, wenn Sie schlichte Beschriftungen bevorzugen):

* <span class=brush>**Pinselwerkzeuge**</span> (Ton, Pinsel, Glätten, Ebene, Aufblähen, EbeneEntf, Quad Remesher)
* <span class=move>**Bewegungswerkzeuge**</span> (Bewegen, Ziehen, Elastisch, Stupsen)
* <span class=mask>**Maskenwerkzeug**</span> (Maske)
* <span class=paint>**Malwerkzeuge**</span> (Zeichnen, Wischfinger)
* <span class=flatten>**Abflachwerkzeuge**</span> (Abflachen, Planar, Polieren)
* <span class=pinch>**Zusammenziehwerkzeuge**</span> (Falte, Zusammenziehen)
* <span class=stamp>**Stempelwerkzeuge**</span> (Stempel, VDM)
* <span class=selection>**Auswahlbasierte Werkzeuge**</span>, bei denen zuerst eine 2d-Maske gezeichnet wird und dann eine Aktion folgt (Trimmen, Teilen, Projizieren)
* <span class=creation>**Erstellungswerkzeuge**</span> (Röhre, Drehbank, Einfügen)
* <span class=transform>**Transformationswerkzeuge**</span> (Transformieren, Gizmo, Anordnen, Gitter)
* <span class=misc>**Sonstige Werkzeuge**</span> (Face-Gruppe, Ausblenden)
* <span class=view>**Ansichtswerkzeuge**</span> (Ansicht, Messen, Auswählen)



Viele dieser Werkzeuge lassen sich im Menü [Strich](stroke.md) anpassen: Pinselverhalten, Druck, Texturen usw. 


### Pinselsteuerung {#brush-controls}

Die linke Werkzeugleiste hat Regler für Radius und Stärke, darunter folgen die Einstellungen der jeweiligen Werkzeugkategorie, die weiter unten erklärt werden.

![](/images/tool_left_panel.webp)

::: tip
Bei vielen Werkzeugen lässt sich der Stärkeregler über 100 % hinaus ziehen. Probieren Sie es aus!
:::

### Sub-Modus {#sub-mode}
Die Schaltfläche direkt unter dem Stärkeregler ist die Taste `Sub`. Ihre Beschriftung und Funktion ändern sich mit jedem Werkzeug. Wenn Sie sie drücken, wird ein alternatives, meist gegenteiliges Verhalten aktiviert. Beim [Zeichnen](#paint) wird zum Beispiel ein Radiermodus aktiviert, bei [Falte](#crease) entstehen erhabene Kanten statt Falten usw.

Standardmäßig funktioniert sie als „Halte“-Taste: Solange Sie sie gedrückt halten, ist sie aktiv, und wenn Sie loslassen, schaltet sie sich wieder aus. Wenn Sie kurz darauf tippen, bleibt der Sub-Modus dauerhaft aktiv.

### Kurzbefehle {#shortcuts}
Unten in der linken Werkzeugleiste befinden sich Kurzbefehle für [Glätten](#smooth), [Maske](#mask), [Ausblenden](#hide), [Face-Gruppe](#facegroup), [Gizmo](#gizmo), [Farbe](painting.md#pbr-sliders) und [Alpha](stroke.md#alpha). 

Standardmäßig funktionieren sie alle als „Halte“-Tasten: Solange Sie eine davon gedrückt halten, ist sie aktiv, und wenn Sie loslassen, schaltet sie sich wieder aus. Wenn Sie kurz darauf tippen, bleibt der Modus dieses Kurzbefehls dauerhaft aktiv.

### Auswahlsteuerung {#selection-controls}

Die Werkzeuge [Maske](#mask), [Zeichnen](#paint), [Trimmen](#trim), [Teilen](#split), [Projizieren](#project), [Face-Gruppe](#facegroup), [Ausblenden](#hide) und [Auswählen](#select) verwenden alle ähnliche Einstellungen, um Bereiche des Meshes auszuwählen.

![](/images/tools_shape_selector_panel.webp)

Tippen Sie in der linken Werkzeugleiste auf die Formschaltfläche (sie zeigt die aktuelle Form, standardmäßig `Lasso`), um ein Popup mit den Formen zu öffnen. Bei den Werkzeugen, die auch mit einem Pinsel arbeiten (Maske, Zeichnen, Face-Gruppe, Ausblenden), enthält dasselbe Popup auch die Strichtypen.

* `Ansicht` - Keine Form: Das Werkzeug tut nichts Besonderes, wie im Kameramodus.
* `Lasso` - Eine frei gezeichnete Form
* `Polygon` - Eine geschlossene Form aus Kurven und/oder geraden Linien. Mehr dazu unter [Formbearbeitung](#shape-editing) weiter unten.
* `Kurve` - (nur Projizieren) - Eine frei gezeichnete Kurve für die Projektion
* `Pfad` - (nur Projizieren) - Eine durch Punkte festgelegte Kurve. Mehr dazu unter [Formbearbeitung](#shape-editing) weiter unten.
* `Linie` - Ziehen Sie eine Linie, um einen ebenen Schnitt festzulegen. Standardmäßig wird die Aktion sofort auf das Mesh angewendet. Ändern Sie die Option `Bearbeiten`, wenn Sie das nicht möchten (Symbol der Linie gedrückt halten oder darüber wischen).
* `Band` - Ein Streifen zwischen zwei parallelen Führungslinien, mit einem Verlauf quer darüber. `Erweitern` behält den vollen Wert hinter der äußeren Führungslinie bei, statt am Ende des Bands aufzuhören. `Umkehren` tauscht die Führungslinie, an der der Verlauf beginnt.
* `Rechteck` -  Ziehen Sie eine diagonale Linie, die die Ecken eines Rechtecks festlegt. Gedrückt halten oder wischen zeigt die Option `Bearbeiten`, `Quadrat` für eine quadratische Form und `Zentriert`, damit der erste Klick die Mitte des Rechtecks wird.
* `Ellipse` - Ziehen Sie eine diagonale Linie, die die Größe einer Ellipse festlegt. Gedrückt halten oder wischen zeigt die Option `Bearbeiten`, `Kreis` für eine Kreisform und `Zentriert`, damit der erste Klick die Mitte der Ellipse wird.
* `Umdrehen` - Kehrt die Formmaske um, oder die Richtung des Projizieren-Werkzeugs.

Die meisten Werkzeuge haben die Option `Bearbeiten`, die festlegt, was passiert, wenn Sie die Form fertig gezeichnet haben:
* `Bearbeiten: aus` - Die Aktion wird ausgeführt, sobald Sie loslassen.
* `Bearbeiten: ein` - Die Form bleibt bearbeitbar. Neben der Form erscheint eine grüne Schaltfläche, die die Aktion ausführt. So können Sie die Form anpassen und die Ansicht ändern. Wenn Sie bereit sind, drücken Sie die grüne Schaltfläche.
* `Bearbeiten: halten` - Die Aktion wird beim Loslassen ausgeführt, es sei denn, Sie halten am Ende des Strichs inne, um die Form weiter zu bearbeiten.

### Formbearbeitung {#shape-editing}
Polygone und Kurven bearbeiten Sie auf ähnliche Weise:

* Ziehen Sie zuerst eine Linie, um 2 Punkte festzulegen, und ziehen Sie dann von der Mitte der Linie nach außen, um ein Polygon oder eine Kurve zu formen.
* Klicken Sie auf die Punkte, um zwischen weich und scharf zu wechseln. 
* Klicken und ziehen Sie auf Kurven- oder Linienabschnitten, um neue Punkte zu erstellen.
* Um einen Punkt zu löschen, ziehen Sie ihn auf seinen Nachbarn, bis er rot wird.
* Das Papierkorbsymbol in der Ecke des Polygon- oder Pfadsymbols löscht die Form.

### Einstellungsmenü {#settings-menu}

Viele Werkzeuge haben zusätzliche Einstellungen im Menü `Werkzeug` oben rechts. Bei Werkzeugen ohne zusätzliche Einstellungen ist das Menü ausgegraut.

![](/images/tools_settings_menu.webp)

## Werkzeuge {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Ton](#clay)       | ![](/icons/tool_brush.webp)   <br> [Pinsel](#brush)     | ![](/icons/tool_move.webp)       <br> [Bewegen](#move)              | ![](/icons/tool_drag.webp)      <br> [Ziehen](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Elastisch](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Glätten](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Maske](#mask)       | ![](/icons/tool_paint.webp)   <br> [Zeichnen](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Wischfinger](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Abflachen](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Planar](#planar)       | ![](/icons/tool_polish.webp)  <br> [Polieren](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Falte](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Zusammenziehen](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Trimmen](#trim)              | ![](/icons/tool_split.webp)     <br> [Teilen](#split)         | ![](/icons/tool_project.webp)   <br> [Projizieren](#project)     | ![](/icons/tool_layer.webp)   <br> [Ebene](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Aufblähen](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Stupsen](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Stempel](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [EbeneEntf](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Röhre](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Drehbank](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Einfügen](#insert)   | ![](/icons/tool_transform.webp)  <br> [Transformieren](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Face-Gruppe](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Ausblenden](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Messen](#measure) | [Anordnen](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Auswählen](#select)       | ![](/icons/tool_lattice.webp)   <br> [Gitter](#lattice)     | ![](/icons/tool_view.webp)    <br> [Ansicht](#view)       |

------

### ![](/icons/tool_clay.webp) Ton {#clay}
Mit dem Werkzeug Ton bauen Sie Ihre Skulptur nach und nach auf. `Sub` trägt Material von Ihrer Skulptur ab.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pinsel {#brush}
Der Standardpinsel. `Sub` trägt Material ab.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Bewegen {#move}
Der Bereich unter dem Pinsel haftet am Pinsel und lässt sich elastisch verformen. Die Auswahl bleibt während der Bewegung erhalten: Wenn Sie den Pinsel wegbewegen und dann an den Ausgangspunkt zurückführen, ist keine Verformung zu sehen.

Der Sub-Modus ist `Normal` und bewegt den Bereich unter dem Pinsel entlang der Oberflächennormale.

Dieser Pinsel eignet sich sowohl für große Verformungen als auch für vorsichtige kleine Anpassungen.

#### Einstellungen für Bewegen {#move-settings}

* `Radius (Hintergrund)` - Wie weit Sie vom Rand eines Modells entfernt sein dürfen und trotzdem noch modellieren, praktisch beim Arbeiten an der Silhouette eines Objekts. Deaktivieren Sie die Option, um nur dann zu greifen, wenn Sie auf dem Modell beginnen.
* `Vertices gleicher Ausrichtung` - Ignoriert Vertices, die entgegen der Verformungsrichtung zeigen.
* `Richtung` - Wird vom Sub-Modus `Normal` verwendet und entscheidet, ob ein Ziehen die Oberfläche hineindrückt oder herauszieht:
    * `Auto` - Wählt anhand des Winkels der Oberflächennormale eine der beiden folgenden Methoden für Sie aus.
    * `Normal 3D` - Vergleicht die Position des Zeigers auf dem Bildschirm mit der Oberflächennormale, wie sie von der Kamera aus zu sehen ist.
    * `XY` - Entscheidet anhand der Bildschirmposition des Zeigers (oben/unten, links/rechts) über Drücken oder Ziehen.
    * `Schwellenwert` - Bei `Auto` die Winkelgrenze, die bestimmt, welche Methode verwendet wird.
* `Rollgeschwindigkeit` - Sie können den gegriffenen Bereich beim Bewegen verdrehen: Drehen Sie zwei Finger, drehen Sie den Stift um seine Achse, oder halten Sie beim Ziehen mit der Maus eine Zusatztaste gedrückt (Alt, Ctrl, Shift oder Cmd). Es gibt je einen Regler für Finger, Stift und Maus; deaktivieren Sie einen davon, um diese Eingabe auszuschalten.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Ziehen {#drag}
Der Bereich unter dem Pinsel haftet am Pinsel und lässt sich elastisch verformen. Anders als beim Pinsel Bewegen wird die Auswahl während des Strichs ständig aktualisiert. So lassen sich längere, schlangenartige Formen ziehen, besonders wenn die dynamische Topologie aktiv ist.

Der Sub-Modus ist `Normal` und bewegt den Bereich unter dem Pinsel entlang der Oberflächennormale.

Dieser Pinsel eignet sich für lockere, gestische Formänderungen.

#### Einstellungen für Ziehen {#drag-settings}

Ziehen hat dieselben Einstellungen wie [Bewegen](#move-settings): `Radius (Hintergrund)`, `Vertices gleicher Ausrichtung`, `Richtung` und `Rollgeschwindigkeit`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastisch {#elastic}
Greift und zieht die Oberfläche wie [Bewegen](#move), aber mit einer elastischen Verformung: Statt am Rand des Pinsels aufzuhören, lässt der Zug mit der Entfernung über das ganze Objekt sanft nach, ähnlich wie beim Dehnen von Gummi. Der Pinselradius bestimmt, wie weit der Zug reicht.

Der Sub-Modus ist `Normal` und bewegt den Bereich unter dem Pinsel entlang der Oberflächennormale.

Dieser Pinsel eignet sich für große, weiche Änderungen der Proportionen, die glatt bleiben sollen.

#### Einstellungen für Elastisch {#elastic-settings}

Elastisch hat dieselben Einstellungen wie [Bewegen](#move-settings), außer `Vertices gleicher Ausrichtung`. `Radius (Hintergrund)` ist standardmäßig ausgeschaltet.

### ![](/icons/tool_smooth.webp) Glätten {#smooth}
Glättet den Bereich, indem die Positionen der Punkte gemittelt werden. Dieses Werkzeug hängt stark von der Polygondichte ab.
Bei sehr vielen Polygonen wirkt das Glätten also schwächer.

Der Sub-Modus ist `Entspannen`. Er glättet nur das Drahtgitter und versucht dabei, die geometrischen Details zu erhalten.

#### Einstellungen für Glätten {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Face-Gruppe {#smooth-facegroup}

* `Entspannen` - Glättet die Ränder von Face-Gruppen. Mit einer Stärke über 100 % glätten Sie die Ränder schnell. `Auto` glättet nur, wenn die Vorschau der Face-Gruppen aktiv ist, `Nein` schaltet es aus, `Ja` schaltet es ein. 

##### Vertex {#vertex}
* `Volumen bewahren` - Glättet, ohne die Oberfläche schrumpfen zu lassen, sodass wiederholtes Glätten Ihre Formen nicht in sich zusammenfallen lässt. Die Zahnradschaltfläche daneben enthält die dafür verwendeten Werte `Schrumpfen` und `Aufblähen`.
* `Grenzen bewahren` - Bei Meshes mit offenen Kanten, z. B. einer Ebene, können die Ecken weggeglättet werden. Mit dieser Option bleiben die Vertices am Rand des Meshes an ihrem Platz.
* `Stabiles Glätten` - Versucht, das Glätten unabhängig von der Topologie zu machen. Das funktioniert am besten bei unterschiedlich dichter Topologie und mit einer hohen Glättungsstärke.
* `Entspannen` - Dasselbe wie der Sub-Modus Entspannen in der linken Werkzeugleiste.

##### Malen {#painting}
* `Bildschirmglättung` - Mit dieser Option glätten Sie unabhängig von der Topologie, auch bei sehr vielen Polygonen. `Auto`, `Nein` oder `Ja`.
* `Bildschirm-Samples` - Die Qualität der Glättung: Höhere Werte glätten stärker, sind aber langsamer.

::: tip
Bei höherer Polygondichte müssen Sie die Stärke eventuell über 100 % anheben. Sehr hohe Werte (300 %, 500 %) eignen sich auch gut zum Modellieren: Bereiche unter dem Pinsel werden schnell flach und glatt, als würden Sie mit einem Hammer auf Ton schlagen!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maske {#mask}
Mit diesem Werkzeug maskieren Sie Vertices. Maskierte Vertices sind vor Modellieren und Malen geschützt. 

Der Sub-Modus ist `Demaskieren` und entfernt die Maske dort, wo sie aufgetragen wurde.

Ähnlich wie Auswahlen in 2d-Malprogrammen lassen sich Masken mit einem Pinsel malen oder mit Formauswahlen erstellen (`Lasso`, `Rechteck`, `Band`...), weichzeichnen oder schärfen. Pinsel oder Form wählen Sie im Strich-Popup der linken Werkzeugleiste, siehe [Auswahlsteuerung](#selection-controls).

Anders als in 2d-Malprogrammen lassen sich Masken auch aus Face-Gruppen erstellen, und mit Masken können Sie durch Extrudieren oder Extrahieren neue Geometrie erzeugen. 

![](/videos/tool_mask1.mp4)

 Oben im Ansichtsfenster erscheint eine Werkzeugleiste mit weiteren Einstellungen. 

![](/images/tool_mask_toolbar.webp)

Tippen Sie auf den Titel der Leiste, um sie ein- oder auszuklappen, oder auf den Pfeil oben rechts, um sie an den oberen oder unteren Rand der Oberfläche zu verschieben.

| Aktion                                             | Beschreibung                                                                               |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Alles löschen      | Entfernt die Maske auf allen Objekten. Wenn auch andere Objekte maskiert sind, entfernt eine zusätzliche Schaltfläche `Löschen` die Maske nur auf den ausgewählten Objekten |
| ![](/icons/invert.webp)        Umkehren           | Kehrt die Maske um                                                                         |
| ![](/icons/sharpen.webp)       Schärfen           | Schärft den Rand der Maske                                                                 |
| ![](/icons/blur.webp)          Unschärfe          | Zeichnet den Rand der Maske weich                                                          |
| ![](/icons/outline.webp)       Rand               | Maskiert den offenen Rand des Meshes, etwa die Kante einer Ebene oder den Rand eines Lochs |
| ![](/icons/blur.webp)          Unschärfe ->       | Nach rechts ziehen zeichnet die Maske weich, nach links schärft sie                        |
| ![](/icons/circle_plus.webp)   Vergrößern ->      | Nach rechts ziehen vergrößert den maskierten Bereich, nach links verkleinert ihn           |
| ![](/icons/intensity.webp)     Verstärken ->      | Nach rechts ziehen verstärkt die Maske, nach links schwächt sie ab, ohne ihre Form zu ändern |
| ![](/icons/dig.webp)           Hohlraum ->        | Baut die Maske anhand der Oberflächenkrümmung neu auf: Nach rechts ziehen lässt nur die Vertiefungen bemalbar, nach links nur die Erhebungen |
| ![](/icons/culling.webp)       Vorne              | Maskiert nur Vertices, die zur Kamera zeigen                                               |
| ![](/icons/eye_open.webp)      Sichtbar           | Ignoriert bei Formen die Vertices, die hinter anderen Oberflächen verdeckt sind            |
|                                 Konvertieren       | Wandelt die Maske in eine Face-Gruppe um                                                   |
| ![](/icons/group_to_mask.webp) Tap (Face-Gruppe)  | Wenn aktiv, werden die Face-Gruppen angezeigt, und ein Tippen auf eine Face-Gruppe maskiert sie |
|                                 Tap (Maske)        | Wenn aktiv, füllt ein Tippen auf eine „Insel“ aus maskierten oder unmaskierten Polygonen diese Insel |
| ![](/icons/connect.webp)       Verbunden          | Wenn aktiv, wirken Maskenstriche nur auf zusammenhängende Topologie                        |

##### Schnelle Maskengesten {#mask-quick-gesture}
Während Sie die Schnellmaskentaste in der linken Werkzeugleiste gedrückt halten, können Sie Gesten wie in ZBrush ausführen:
| Aktion    | Geste (Kurzbefehl unten links halten) |
| :-------: | :-----------------------------------: |
| Umkehren  | Auf den Hintergrund tippen            |
| Löschen   | Auf dem Hintergrund ziehen            |
| Unschärfe | Auf einen maskierten Bereich tippen   |
| Schärfen  | Auf einen unmaskierten Bereich tippen |


#### Einstellungen für Maske {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Die Einstellungen für Maske dienen vor allem dazu, aus der Maske Geometrie zu erzeugen. Mit den Tabs oben wählen Sie die Aktion: [Extrahieren](#extract), [Teilen](#split-mask) oder [Gravieren](#carve). Die Optionen darunter ändern sich je nach Aktion.

* `Vorschau` - Zeigt, wie die neue Geometrie aussehen wird, während Sie die Einstellungen anpassen.
* `Röntgen` - Welche Objekte während der Vorschau im Röntgenmodus angezeigt werden: `Keine`, `Nicht ausgewählt`, `Ausgewählt` oder `Alle`.

##### Extrahieren {#extract}
* `Extrahieren` - Erstellt die extrahierte Geometrie als neues Objekt.
* `Schließen` - Wie die extrahierte Form geschlossen wird. `Keine` kopiert die maskierten Polygone in eine neue Form und lässt sie offen. `Füllen` tut dasselbe, füllt aber zusätzlich das Loch auf der Rückseite und glättet es (nicht für flache Oberflächen geeignet). `Hülle` schließt die Form mit dem Wert `Höhe` und ist die Standardeinstellung.

::: tip

Wenn die Vorschau mit Röntgen aktiv ist, kann ein Klick auf Extrahieren anfangs verwirren. Da das Menü noch offen ist, versucht Nomad, eine Extraktion auf Ihrer neuen Form als Vorschau anzuzeigen, und stellt die ursprüngliche Oberfläche im Röntgenmodus dar. Auf der neuen Oberfläche gibt es aber keine Maske, also kann keine Vorschau entstehen, und Nomad warnt Sie mit „Nichts zu extrahieren!“. 

Das ist normal: Schließen Sie das Menü der Maskeneinstellungen, um die neue Form und das Original zu sehen, und wählen Sie die ursprüngliche Oberfläche wieder aus, wenn Sie die Maske entfernen oder neue Masken zeichnen möchten.
:::

##### Teilen {#split-mask}
* `Teilen` - Extrahiert sowohl den maskierten als AUCH den unmaskierten Bereich in neue Formen. 
* `Schließen` (maskiert) - Wie der maskierte Teil geschlossen wird, mit denselben Möglichkeiten `Keine`, `Füllen` und `Hülle` wie bei Extrahieren.
* `Schließen` (unmaskiert) - Wie der unmaskierte Teil geschlossen wird, mit denselben Möglichkeiten.

##### Gravieren {#carve}
* `Gravieren` - Wirkt so, als hätten Sie um den Wert `Höhe` in die Oberfläche hineingeschnitten, wie beim Herausschneiden eines Stücks Orangenschale. Die `Höhe` darf nicht 0 sein.

##### Höhe {#thickness}
* `Höhe` - Die Höhe der extrahierten Form. Mit der Plus/Minus-Schaltfläche wechseln Sie zwischen einer Extrusion nach außen, nach innen oder in beide Richtungen. 

##### Glättung {#smoothness}
Wenn aktiv, wird die extrahierte Form geglättet. Das funktioniert besser bei mehr Polygonen. 
* `Alle` / `Nur Kanten` - Glättet die ganze Form oder nur ihre Ränder, die obere Fläche bleibt dann unverändert.
* `Iterationen` - Bei `Alle` die Stärke der Glättung. Hohe Werte ergeben sehr glatte, runde Kanten, entfernen sich aber allmählich von der Form der Maske.
* `Wand` - Bei `Nur Kanten` die Stärke der Glättung an den Wänden. Die Schaltfläche daneben wechselt zwischen Entspannen, das harte Ecken erhält, und Glätten, das sie ebenfalls abrundet.
* `Innen` - Bei `Nur Kanten`, wie stark die obere Fläche ausgeglichen wird. Die Schaltfläche daneben wechselt zwischen Entspannen, das die modellierten Details erhält und nur die Extrusionsrichtung ausgleicht (damit Details keine Spitzen erzeugen), und Glätten, das die Oberfläche selbst glättet.

##### Seiten {#edge-loop-side}
* `Gerade` - Einfache Wände an den Seiten der extrahierten Form.
* `Fase` - (nur Extrahieren mit `Hülle`) Eine abgeschrägte Kante vorne. `Fase` legt ihre Breite fest, in % der `Höhe` oder in Welteinheiten (die Schaltfläche daneben schaltet um), `Fasenunterteilungen` unterteilt sie (standardmäßig `Auto`), und mit einer Kurve formen Sie ihr Profil.
* `Profil` - Formt die Wände mit einer Profilkurve, mit einer `Breite` in % der `Höhe` oder in Welteinheiten.
* `Maske` - Die Höhe folgt der Maske: Weichgezeichnete Bereiche der Maske erhalten eine geringere Höhe, so entstehen weiche Formen mit wechselnder Höhe.
* `Wandunterteilungen` - Die Anzahl der Kantenschleifen an den Seiten. Bei `Auto` wählt Nomad die Anzahl der Unterteilungen so, dass quadratische Polygone entstehen, die zu den Polygonen des maskierten Bereichs passen.



### ![](/icons/tool_maskSelector.webp) Auswahlmaske {#selection-mask}
Das Werkzeug Auswahlmaske (AuswMask) ist jetzt Teil des Werkzeugs [Maske](#mask). Um mit Formen statt mit einem Pinselstrich zu maskieren, wählen Sie im Strich-Popup des Maskenwerkzeugs eine Form (`Lasso`, `Polygon`, `Rechteck`...), siehe [Auswahlsteuerung](#selection-controls).

Der Sub-Modus `Demaskieren` funktioniert auch mit Formen und entfernt die Maske innerhalb der Form.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Zeichnen {#paint}
Trägt Farbe und Materialeigenschaften auf. Mehr über Materialien erfahren Sie im Abschnitt [Malen](painting.md).

Der Sub-Modus ist `Löschen` und entfernt Farbe.

Neben Pinselstrichen kann Zeichnen auch Formen füllen (`Lasso`, `Rechteck`, `Band`...), siehe [Auswahlsteuerung](#selection-controls).

#### Einstellungen für Zeichnen {#paint-settings}
* `Layer Filter` - Funktioniert wie das Fixieren der Layer-Transparenz in Photoshop oder Procreate. Wenn Sie auf einem Layer malen und die Option aktiv ist, können Sie nur dort etwas ändern, wo schon Farbe ist; unbemalte Bereiche sind geschützt. Die Option ist nur verfügbar, wenn ein Layer ausgewählt ist.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Wischfinger {#smudge}
Verwischt Farbe und Materialeigenschaften. Das Einstellungsmenü von Wischfinger enthält einen Regler `Qualität`: Niedrigere Werte ergeben schnellere Striche.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Abflachen {#flatten}
Flacht den Bereich ab, indem die Punkte auf die mittlere Ebene projiziert werden.

Der Sub-Modus ist `Füllen`. Er legt eine Ebene durch den höchsten Punkt fest und zieht Punkte eher nach oben.

#### Einstellungen für Abflachen {#flatten-settings}

* `Ebenenrichtung sperren` - Verwendet die beim ersten Klick berechnete Richtung der Ebene. Standardmäßig ist das ausgeschaltet.
* `Ebenenursprung sperren`- Verwendet den ersten Klick als Mittelpunkt der Ebene. Standardmäßig ist das ausgeschaltet, und es lässt sich nur zusammen mit `Ebenenrichtung sperren` einschalten.

Wenn eine oder beide Optionen ausgeschaltet sind, können Sie mit langen Strichen, die über unterschiedliche Tiefen und Krümmungen laufen, die Abflachung nach und nach vertiefen oder den Winkel der Ebene ändern. Zusammen mit den Optionen zur Flächenabtastung im Pinselmenü lässt sich das sehr präzise steuern.

::: tip
Wenn Sie in stark gekrümmten Bereichen arbeiten, etwa die Wangen abflachen möchten, das Werkzeug aber immer wieder die Seiten der Nase erwischt, erstellen Sie eine Maske, um die Bereiche zu schützen, die der Abflachen-Pinsel nicht verändern soll.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Macht Punkte eben, indem sie auf die mittlere Ebene projiziert werden, aber mit weniger Aufbau als der Pinsel Abflachen. So entstehen sauberere Flächen mit harten Kanten. Schnelle Striche drücken und ziehen stärker an der Oberfläche; langsamere Striche, die in bereits ebenen Bereichen beginnen und sich nach außen arbeiten, halten die Ebene besser.

Der Sub-Modus ist `Füllen`. Er legt eine Ebene durch den höchsten Punkt fest und zieht Punkte eher nach oben.

Planar ist eigentlich dasselbe Werkzeug wie `Abflachen`, aber mit aktivierter Option `Ebenenrichtung sperren`. Es erzeugt daher eher stabile Flächen mit harten Kanten, während Abflachen freier modelliert und sich für halbflache Bereiche eignet.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Polieren {#polish}
Ein weiteres Mitglied der Abflachen-Familie, darauf eingestellt, Oberflächen zu sauberen Ebenen zu polieren. Es ist dasselbe Werkzeug wie `Abflachen`, mit anderen Standardwerten im Menü [Strich](stroke.md): `Spur`, `Normalenfilter (Bereich)` und `Tiefenmaskierung` sind aktiviert.

Der Sub-Modus ist `Füllen`, wie bei Abflachen.

Polieren hat dieselben Einstellungen wie [Abflachen](#flatten-settings): `Ebenenrichtung sperren` und `Ebenenursprung sperren`.

### ![](/icons/tool_crease.webp) Falte {#crease}
Mit dem Werkzeug Falte modellieren Sie kleine Schnitte oder Kerben.

Der Sub-Modus ist `Umkehren` und erzeugt eine erhabene Falte.

#### Einstellungen für Falte {#crease-settings}

* `Pinch-Stärke` - Wie stark Vertices seitlich zum Pinsel hingezogen werden. Bei einer Pinch-Stärke von 1 und einem Versatz von 0 ändert sich die Tiefe der Oberfläche nicht, nur die Topologie: Kanten werden zum Strich hingezogen.
* `Versatzfaktor` - Wie stark Vertices in die Tiefe gedrückt oder herausgezogen werden. Bei einer Pinch-Stärke von 0 und einem Versatz von 1 entstehen tiefe Falten oder erhabene Kerben, die aber zackig aussehen, weil nicht genug Geometrie zur Falte hingezogen wird, um ihre Seiten oder ihren Grund sauber zu formen.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Zusammenziehen {#pinch}
Mit diesem Werkzeug schärfen Sie Kanten.

Der Sub-Modus ist `Umkehren` und schiebt Vertices auseinander.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trimmen {#trim}
Das Werkzeug Trimmen entfernt ein Stück Ihres Meshes und bietet Optionen, wie die entstandene Lücke behandelt wird. Den Schnitt legen Sie mit der [Auswahlsteuerung](#selection-controls) fest.

Der Sub-Modus ist `Umdrehen` und kehrt die Form um, sodass die andere Seite entfernt wird.

::: tip
Da dieses Werkzeug von der Kamera aus projiziert, erhalten Sie eine Warnung, wenn die Kamera im Perspektivmodus ist.

Im orthografischen Modus verläuft der Schnitt durch das Mesh parallel zur Ansicht, so wie man es meistens erwartet. Mit einer perspektivischen Kamera sieht der Schnitt auf der hinteren Seite des Objekts anders aus als auf der vorderen.
:::

#### Einstellungen für Trimmen {#trim-settings}

Die Einstellungen sind unter `Füllen von Löchern` zusammengefasst:

* `Striche malen` - Wenn Malen im Malmenü aktiv ist, wird der geflickte Bereich mit der aktuell gewählten Farbe gefüllt.
* `Boolean` - Füllt das Loch des Schnitts mit einem Bereich aus Quads. Der gefüllte Bereich ist flach.
* `Legacy` - Füllt das Loch des Schnitts mit einem triangulierten Bereich. Der gefüllte Bereich ist flach.
* `Füllen` - Füllt das Loch mit einem triangulierten Bereich. Der gefüllte Bereich ist eine gewölbte Fläche, wie die Haut einer Seifenblase.
* `Keine` - Füllt das Loch nicht.

Bei `Boolean` enthält der Abschnitt `Detailgrad`:

* `Form` - Die ungefähre Größe der Quads und Dreiecke auf der Seite der Form.
* `Löcher` - Die ungefähre Größe der Dreiecke oder Polygone im gefüllten Loch. Die Verknüpfungsschaltfläche neben `Detailgrad` hält den Wert mit `Form` synchron; heben Sie die Verknüpfung auf, um ihn separat einzustellen.
* `Topologie bewahren` - Glättet und vereinfacht den Schnittrand nicht, sodass die ursprüngliche Topologie des Meshes in der Nähe maskierter und ausgeblendeter Flächen erhalten bleibt.

Bei `Legacy`:

* `Detailgrad` - Die ungefähre Größe der Dreiecke im Schnitt.
* `Loch-Glättung` - Wie stark die Dreiecke im gefüllten Bereich entspannt werden.
* `Schwellenwert Epsilon` - Ein Wert, mit dem Sie den alten Algorithmus zum Füllen von Löchern verbessern können.

Bei `Füllen`:

* `Detailgrad` - Die ungefähre Größe der Dreiecke im Schnitt.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Teilen {#split}
Ähnlich wie das Werkzeug [Trimmen](#trim): Während Trimmen die Auswahl verwirft, behält Teilen sie als neues Objekt.

Der Sub-Modus ist `Teilen`: Jedes Stück bleibt ein eigenes Objekt, sodass sich überlappende Formen (zum Beispiel mit Symmetrie) in getrennte Teile geschnitten werden, statt zu einem zusammengefügt zu werden.

#### Einstellungen für Teilen {#split-settings}

Teilen hat dieselben Einstellungen unter `Füllen von Löchern` wie [Trimmen](#trim-settings): `Striche malen`, die Methoden `Boolean`, `Legacy`, `Füllen` und `Keine` sowie deren Optionen für `Detailgrad`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projizieren {#project}
Das Werkzeug Projizieren ähnelt dem Werkzeug [Trimmen](#trim), löscht oder erzeugt aber keine Geometrie. Es verschiebt nur Vertices, damit sie sich der Auswahl anpassen.

![](/videos/tool_project.mp4)

::: tip
Wenn Sie Projizieren auf einem Layer verwenden, können Sie mit dem Layer-Regler zwischen der ursprünglichen und der projizierten Form überblenden.
:::

### ![](/icons/tool_layer.webp) Ebene {#layer}
Hebt die Oberfläche an, aber nur bis zu einer begrenzten Höhe.

Wenn Sie den Stift aufgesetzt lassen und immer wieder über einen Bereich malen, steigt Ebene bis zu einer bestimmten Höhe an und dann nicht weiter, während andere Werkzeuge immer mehr Höhe aufbauen.

Beachten Sie, dass die Begrenzung standardmäßig nur pro Strich gilt! Beginnen Sie einen neuen Strich, baut er auf der neuen Oberflächenhöhe auf.

Um eine gleichbleibende maximale Höhe über viele Striche hinweg festzulegen, verwenden Sie das Werkzeug Ebene zusammen mit dem [Layer](layers.md)-System von Nomad.

Erstellen Sie einen Layer und verwenden Sie dieses Werkzeug. Die maximale Höhe wird nun durch den Layer festgelegt: Sie können beliebig viele Pinselstriche setzen, und die Höhe bleibt immer gleich.

`Sub` verwendet eine minimale Tiefe und erzeugt so Rillen.

#### Einstellungen für Ebene {#layer-settings}

* `Layerdaten verwenden` - Wenn aktiv und ein Layer ausgewählt ist, legen die Daten des Layers die maximale Höhe fest. Eine Warnung erinnert Sie daran, wenn kein Layer ausgewählt ist.
* `Aufblähen`- Wenn aktiv, wird die Richtung angepasst, in der das Werkzeug wirkt, für glattere Ergebnisse.
* `Entspannen (Normal)` - Bei aktiviertem `Aufblähen` die Stärke der Glättung, die auf die Normalen angewendet wird.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Aufblähen {#inflate}
Bewegt die Vertices entlang ihrer eigenen Normalen. `Sub` bewegt Vertices entlang ihrer umgekehrten Normale.

#### Einstellungen für Aufblähen {#inflate-setings}
* `Entspannen (Normal)` - Die Stärke der Glättung, die auf die Normalen angewendet wird.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Stupsen {#nudge}
Verschiebt oder „verschmiert“ Punkte in Richtung des Strichs.

Der Sub-Modus ist `Falte` und schiebt eine Materialfalte entlang des Strichs: eine Wölbung vor dem Pinsel, eine Mulde dahinter.

#### Einstellungen für Stupsen {#nudge-settings}
* `Glätten` - Wie stark der Bereich unter dem Pinsel beim Stupsen geglättet wird, damit die verschmierte Oberfläche sauber bleibt.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stempel {#stamp}

Klicken und ziehen Sie, um einen Bereich der Skulptur in der Form des gewählten Alphas anzuheben.

Das ist einfach das Werkzeug [Pinsel](#brush) mit dem Strichtyp `Grab • Dynamischer Radius`. 

`Sub` drückt den Stempel in die Oberfläche hinein, statt ihn herauszuziehen.

::: tip
Stempel funktioniert meist am besten mit hochaufgelöster Geometrie. Wenn Sie online nach „wrinkles alpha“, „pores alpha“, „scales alpha“ usw. suchen, sind diese Alpha-Texturen zusammen mit Stempel eine großartige Möglichkeit, einer Figur organische Details hinzuzufügen.

Die beiden Strichmodi eignen sich für unterschiedliche Zwecke. 

* `Grab • Dynamischer Radius` hat eine feste *Höhe*, durch Ziehen ändern Sie Breite und Drehung des Stempels. Gut für Hauttexturen, die überall gleich tief/hoch sein sollen, aber mit unterschiedlichen Drehungen und Größen, damit sich wiederholende Muster nicht auffallen.
* `Grab • Dynamische Intensität` hat eine feste *Breite*, durch Ziehen ändern Sie Drehung und Höhe des Stempels. Gut für Nieten, die alle gleich groß sein sollen, aber mit unterschiedlichen Drehungen und Höhen. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Stempelt eine Vector Displacement Map (VDM). Anders als ein Alpha, das die Oberfläche nur nach oben oder unten verschieben kann, speichert eine VDM eine vollständige 3d-Form und kann daher auch Überhänge stempeln, etwa Ohren, Hörner oder eingerollte Blätter. Sie funktioniert wie [Stempel](#stamp), mit denselben Strichmodi `Grab • Dynamischer Radius` und `Grab • Dynamische Intensität`.

`Sub` (`Umkehren`) kehrt die Tiefe des Stempels um, um ihn wie eine Gussform in die Oberfläche zu drücken.

Die VDM selbst wählen Sie im Menü [Alpha](stroke.md#alpha). Dort gibt es auch einen Regler `Höhe`, der nur die Höhe des Stempels skaliert und seine seitliche Verschiebung unverändert lässt.

Mit der Schaltfläche `Erstellen` in der linken Werkzeugleiste erstellen Sie eigene Stempel:

* `Neues VDM...` - Fügt eine Ebene hinzu, die zum Modellieren einer VDM eingerichtet ist. Modellieren Sie Ihre Form darauf und backen Sie sie dann mit `Topologie -> Backen -> VDM`: Nomad fügt den neuen Stempel der VDM-Bibliothek hinzu und wählt ihn aus.
* `VDM erfassen` - (Experimentell) Ziehen Sie über die Oberfläche eines Modells, um diesen Bereich aufzunehmen und daraus einen VDM-Stempel zu machen. `Toleranz` flacht den Rand der Aufnahme sanft ab.

::: tip
Verwenden Sie beim Modellieren einer VDM-Ebene kein Dyntopo: Es beschädigt die UVs der Ebene und verzerrt den Stempel. Halten Sie die Skulptur außerdem vom Rand der Ebene fern, sonst zeigt der Stempel eine harte Kante.
:::


### ![](/icons/tool_clearLayer.webp) Ebene löschen {#delete-layer}
Mit diesem Werkzeug setzen Sie Layer stellenweise zurück. Sie brauchen dafür einen aktiven Layer, sonst passiert nichts. Es löscht die modellierten Daten des Layers und, wenn Malen aktiv ist, auch seine Farbe.

Der Sub-Modus ist `Umkehren` und verstärkt den Layer leicht, statt ihn zu löschen.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Röhre {#tube}
Erstellt eine Röhre, indem Sie eine Kurve zeichnen. 
![](/images/tool_tube_new.webp)

Sobald die Röhre erstellt ist, können Sie den Pfad im 3d-Raum bearbeiten, mit ähnlichen Bedienelementen wie bei der normalen [Formbearbeitung](#shape-editing) und den Kurvenwerkzeugen. 

![](/videos/tool_tube.mp4)

#### Linke Werkzeugleiste von Röhre {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Die linke Werkzeugleiste hat folgende Optionen:

* `Synchronisieren` - Wenn die aktuelle Röhre instanziert ist und sich ihre Unterknoten zwischen den Instanzen unterscheiden, werden sie hiermit wieder synchronisiert.
* `Einrasten` - Wenn aktiv, rasten die Modi Kurve und Pfad beim Zeichnen auf anderen Objekten ein. Wenn inaktiv, rastet nur der erste Punkt ein, und der Rest der Röhre wird in dieser Tiefe gezeichnet.
* `Versatz` - Legt die Tiefe des Einrastens fest: Bei 0 % rastet die Mitte des Röhrenquerschnitts auf der Oberfläche ein, positive Werte heben sie von der Oberfläche ab, negative Werte senken sie ab. 100 % entspricht dem Radius der Röhre.
* `Ansicht` - Kein Zeichenmodus, damit Sie die Kamera frei bewegen können.
* `Kurve` - Skizzieren Sie eine Röhre frei Hand. Ein kleines Ausklappmenü bietet:
    * `Bearbeiten` - Was passiert, wenn Sie den Strich beenden, siehe [Auswahlsteuerung](#selection-controls): Die Röhre sofort erstellen, die Kurve mit einem grünen Bestätigungskreis daneben bearbeitbar lassen, oder am Ende des Strichs `Halten`, um weiter zu bearbeiten.
    * `Geschl.` - Macht die Röhre zu einer Schleife.
    * `Weiterzeichnen` - Bleibt nach dem Bestätigen einer Röhre im Werkzeug, um die nächste zu zeichnen.
    * `Genauigkeit` - Wie viele Kurvenpunkte verwendet werden, um den gezeichneten Pfad in eine Röhre umzuwandeln. 0 % verwendet möglichst wenige Punkte, übersieht aber kleine Änderungen der Krümmung. 100 % ist sehr genau und verwendet viele Punkte.
* `Pfad` - Erstellt eine Röhre, indem Sie Kurvenpunkte per Klick setzen. Tippen Sie auf den grünen Kreis, um den Pfad zu bestätigen. Ein kleines Ausklappmenü bietet:
    * `B-Spline` - Eine andere Methode zum Zeichnen von Kurven, bei der die Kurvenpunkte meist nicht direkt auf der Kurve liegen, die aber glattere Ergebnisse liefern kann als die Standardmethode.
    * `Geschl.` - Macht die Röhre zu einer Schleife
    * `Bildschirm` - Wenn aktiv, ist der Pfad am Bildschirm „angeheftet“: Sie können Ansicht und Objekt bewegen, und der Pfad bleibt an seinem Platz. Wenn inaktiv, gehört der Pfad zur 3d-Szene und bewegt sich mit Kamera und Objekten.
* `Schnitt` - Die Kurve wird zu einem Ring um die Form, geschnitten durch ihre zwei Punkte entlang der Richtung, aus der Sie geschaut haben.

##### Obere Werkzeugleiste von Röhre {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Wenn eine Röhre ausgewählt ist, erscheint oben im Ansichtsfenster eine Werkzeugleiste mit weiteren Einstellungen. Klicken Sie auf ihren Titel, um sie ein- oder auszuklappen, und auf den Pfeil oben rechts, um sie an den oberen oder unteren Rand des Ansichtsfensters zu verschieben.

* `Abschließen` - Wandelt die Röhre in normale Polygone um, damit sie modelliert werden kann.
* `Bearbeiten` - Zeigt die Kurvenpunkte an, damit Sie sie verschieben können
* `Spiegeln` - Fügt einen Spiegel-Repeater als übergeordnetes Element dieser Kurve hinzu
* `Einrasten` - Lässt Kurvenpunkte auf nahen Oberflächen einrasten
* `Geschl.` - Verbindet Anfang und Ende der Kurve zu einer Schleife
* `B-Spline` - Wechselt zwischen Catmull-Rom- und B-Spline-Interpolation.
* `Kappe` - Wechselt zwischen Kappen an beiden Enden der Röhre, nur am Anfang oder Ende, oder keinen Kappen.
* `Loch` - Gibt der Röhre eine Wandstärke und macht sie so zu einem Rohr. Wechselt zwischen einem Loch an beiden Enden, nur am Ende, oder keinen Löchern. 
* `Radius` - Wechselt zwischen einem einheitlichen Radius, einem Radius an Anfang und Ende, oder einem Radius pro Kurvenpunkt. Diese bearbeiten Sie mit orangefarbenen Griffen auf der Kurve.
* `Windung` - Wechselt zwischen keiner Verdrehung, einer einheitlichen Verdrehung, einer Verdrehung an Anfang und Ende, oder einer Verdrehung pro Kurvenpunkt. Diese bearbeiten Sie mit rosafarbenen Griffen auf der Kurve.
* `Profil` - Wechselt zwischen keinem Profil (also einem kreisförmigen Profil), einem einheitlichen Profil, einem Profil an Anfang und Ende, oder einem Profil pro Punkt.
* `Profil bearbeiten` - Zeigt einen Profileditor an. Er funktioniert ähnlich wie die Werkzeuge der [Formbearbeitung](#shape-editing), kann Profilvorlagen speichern und laden und hat einen Schalter, mit dem Sie das Profil im 3d-Raum bearbeiten.
* `Spirale` - Blendet ein Menü ein, um der Röhre eine spiralförmige Verdrehung zu geben. Dieses Menü hat Optionen für `Drehwinkel`, `Versatz`, `Skalierung` und `Winkel-Offset`.
* `Unterteilung X` - Die Anzahl der Unterteilungen rund um die Röhre; 4 Unterteilungen ergeben zum Beispiel eine quadratische Röhre. 
* `Konstante Dichte` - Wenn aktiv, bleiben die Polygone quadratisch. Wenn ausgeschaltet, können Sie `Unterteilung Y` entlang der Röhre einstellen.
* `...` - Menü mit den Einstellungen der Röhre.

#### Kurvenpunkte löschen ein/aus {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Unter der Werkzeugleiste befindet sich ein Schalter zum Löschen von Kurvenpunkten. Wenn Sie einen Kurvenpunkt in die Nähe eines anderen ziehen, wird er rot: Lassen Sie jetzt los, wird der Punkt gelöscht. Wenn Sie kleine Änderungen vornehmen und keine Punkte löschen möchten, schalten Sie dieses Verhalten mit dieser Schaltfläche aus.



#### Einstellungen für Röhre {#tube-settings}
* `Grundformen` - Schaltflächen zum Ein- und Ausschalten der UVs oder zum Abschließen der Röhre.
* `Nachträgliche Unterteilung` - Ein Kurzbefehl, um vor dem Abschließen die Multiauflösungsstufe festzulegen.
* `Lineare Unterteilung` - Ein Kurzbefehl, um vor dem Abschließen die Stufe der linearen Unterteilung festzulegen. 
* `Unterteilung X` - Dasselbe wie Unterteilung X in der Werkzeugleiste.
* `Unterteilung Y` - Dasselbe wie Unterteilung Y in der Werkzeugleiste.
* `Kurve (Repeater)` - Wandelt die Röhre in einen [Kurven-Repeater](scene.md#curve) um

::: tip
Mit 4 Unterteilungen und einer nachträglichen Unterteilung von 3 entstehen glatte Röhren mit runden Enden, gut für Würmer, Schlangen und Körperteile.
:::


### ![](/icons/tool_lathe.webp) Drehbank {#lathe}
Erstellt eine Rotationsfläche, indem Sie eine Kurve zeichnen.

Dieses Werkzeug ist ideal für Formen wie Vasen oder Weingläser.

![](/videos/tool_lathe.mp4)

#### Linke Werkzeugleiste von Drehbank {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Die linke Werkzeugleiste hat folgende Optionen:

* `Synchronisieren` - Wenn die aktuelle Drehform instanziert ist und sich ihre Unterknoten zwischen den Instanzen unterscheiden, werden sie hiermit wieder synchronisiert.
* `Fixiert` - Wenn aktiv, ist die Mittelachse der Drehform fixiert und auf dem Bildschirm sichtbar. Diese Mittellinie hat Bearbeitungspunkte, die Sie verschieben können. Wenn inaktiv, passt sich die Mitte der Drehform automatisch an Anfang und Ende der gezeichneten Kurve an.
* `Ansicht` - Kein Zeichenmodus, damit Sie die Kamera frei bewegen können.
* `Kurve` - Zeichnen Sie das Profil der Drehform in einem Strich. Ein kleines Ausklappmenü bietet:
    * `Bearbeiten` - Was passiert, wenn Sie den Stift anheben, siehe [Auswahlsteuerung](#selection-controls): Die Drehform sofort erstellen, die Kurve mit einem grünen Kreis daneben zum Erstellen bearbeitbar lassen, oder am Ende des Strichs `Halten`, um weiter zu bearbeiten.
    * `Geschl.` - Verbindet Anfang und Ende der Kurve zu einer Schleife
    * `Weiterzeichnen` - Bleibt nach dem Bestätigen einer Drehform im Werkzeug, um die nächste zu zeichnen.
    * `Genauigkeit` - Wie viele Kurvenpunkte verwendet werden, um den gezeichneten Pfad umzuwandeln. 0 % verwendet möglichst wenige Punkte, übersieht aber kleine Änderungen der Krümmung. 100 % ist sehr genau und verwendet viele Punkte.
* `Pfad` - Erstellt eine Drehform, indem Sie Kurvenpunkte per Klick setzen. Tippen Sie auf den grünen Kreis, um den Pfad zu bestätigen. Ein kleines Ausklappmenü bietet:
    * `B-Spline` - Eine andere Methode zum Zeichnen von Kurven, bei der die Kurvenpunkte meist nicht direkt auf der Kurve liegen, die aber glattere Ergebnisse liefern kann als die Standardmethode.
    * `Geschl.` - Macht die Kurve zu einer Schleife
    * `Bildschirm` - Wenn aktiv, ist der Pfad am Bildschirm „angeheftet“: Sie können Ansicht und Objekt bewegen, und der Pfad bleibt an seinem Platz. Wenn inaktiv, gehört der Pfad zur 3d-Szene und bewegt sich mit Kamera und Objekten.

#### Obere Werkzeugleiste von Drehbank {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Wenn eine Drehform ausgewählt ist, erscheint oben im Ansichtsfenster eine Werkzeugleiste mit weiteren Einstellungen. Klicken Sie auf ihren Titel, um sie ein- oder auszuklappen, und auf den Pfeil oben rechts, um sie an den oberen oder unteren Rand des Ansichtsfensters zu verschieben.

* `Abschließen` - Wandelt die Drehform in normale Polygone um, damit sie modelliert werden kann.
* `Bearbeiten` - Zeigt die Kurvenpunkte an, damit Sie sie verschieben können
* `Spiegeln` - Fügt einen Spiegel-Repeater als übergeordnetes Element dieser Drehform hinzu
* `Einrasten` - Lässt Kurvenpunkte auf nahen Oberflächen einrasten
* `Stabil` - Wenn aktiv, ist das Kurvenprofil der Mittellinie der Drehform untergeordnet. Wenn ausgeschaltet, können Sie die Mittellinie bearbeiten, ohne die Kurve zu bewegen, was komplexere Formen ermöglicht.
* `Fokus` - Dreht die Ansicht so, dass das Kurvenprofil genau flach zur Kamera liegt.
* `Geschl.` - Verbindet Anfang und Ende der Kurve zu einer Schleife
* `Kappe` - Wenn Geschl. ausgeschaltet ist, wechselt zwischen Kappen an beiden Enden, nur am Anfang oder Ende, oder keinen Kappen.
* `Loch` - Gibt der Drehform eine Wandstärke und macht sie so zu einem Rohr. Wechselt zwischen einem Loch an beiden Enden, nur am Ende, oder keinen Löchern. 
* `B-Spline` - Wechselt zwischen Catmull-Rom- und B-Spline-Interpolation.
* `Unterteilung X` - Die Anzahl der Unterteilungen rund um die Drehform; 4 Unterteilungen ergeben zum Beispiel eine Drehform mit quadratischem Querschnitt. 
* `Konstante Dichte` - Wenn aktiv, bleiben die Polygone quadratisch. Wenn ausgeschaltet, können Sie `Unterteilung Y` entlang der Form einstellen.
* `...` - Menü mit den Einstellungen der Drehbank.

#### Einstellungen für Drehbank {#lathe-settings}
* `Grundformen` - Schaltflächen zum Ein- und Ausschalten der UVs oder zum Abschließen der Form.
* `Nachträgliche Unterteilung` - Ein Kurzbefehl, um vor dem Abschließen die Multiauflösungsstufe festzulegen.
* `Lineare Unterteilung` - Ein Kurzbefehl, um vor dem Abschließen die Stufe der linearen Unterteilung festzulegen. 
* `Unterteilung X` - Dasselbe wie Unterteilung X in der Werkzeugleiste.
* `Unterteilung Y` - Dasselbe wie Unterteilung Y in der Werkzeugleiste.
* `Kurve (Repeater)` - Wandelt das Kurvenprofil in einen [Kurven-Repeater](scene.md#curve) um

### ![](/icons/tool_insert.webp) Einfügen {#insert}
Platziert ein Objekt auf der Oberfläche eines anderen. In der Bedienung ähnelt es dem Werkzeug Stempel, aber für vollständige 3d-Formen.

Wenn Sie in der linken Werkzeugleiste eine Grundform wählen, platziert ein Klicken und Ziehen auf einer beliebigen Oberfläche die Grundform an der Klickstelle, und das Ziehen bestimmt ihre Größe. Sobald Sie mit dem Ziehen fertig sind, wechselt Einfügen in den Modus [Transformieren](#transform).

Im Modus Instanz erstellt das Ziehen eine neue Instanz und schiebt sie über die Oberfläche. Die Größe wird von der ersten Form übernommen. So können Sie viele gleich große Instanzen eines Objekts über andere Oberflächen verteilen.

Sie müssen nicht nur Grundformen einfügen! Wählen Sie *irgendeine* Form im Outliner aus: Wenn Einfügen im Modus Instanz oder Klonen ist, können Sie Kopien des ausgewählten Objekts über jede andere Oberfläche ziehen.

Hat ein Objekt einen eigenen Drehpunkt, wird dieser als Ankerpunkt verwendet. Siehe Video unten.

Die linke Werkzeugleiste hat außerdem `Ansicht`, um die Kamera zu bewegen, ohne etwas einzufügen, und `Synchronisieren`: Wenn das Zielobjekt instanziert ist, wird das neue Objekt auch allen anderen Instanzen hinzugefügt.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformieren {#transform}
Bewegt, dreht und skaliert ein Modell direkt mit 1 oder 2 Fingern, meist über die Oberfläche eines anderen Objekts.

Die linke Werkzeugleiste hat diese Schaltflächen:

* `Klonen` / `Instanz` - Erstellt eine Kopie oder eine Instanz des Objekts, siehe die Werkzeugleiste von [Gizmo](#left-menu-toolbar).
* `Bewegen` - Ziehen mit einem Finger bewegt das Objekt. Wenn Einrasten aktiv ist, gleitet das Objekt über die Oberfläche unter Ihrem Finger.
* `Drehen` - Ziehen mit einem Finger dreht das Objekt. Wenn Einrasten aktiv ist, dreht es sich um die Normale der Oberfläche unter Ihrem Finger.
* `Skalierung` - Ziehen mit einem Finger skaliert das Objekt.

Eine Werkzeugleiste oben im Ansichtsfenster hat:

* `Ziel` - Ob das Werkzeug das Objekt, seine Gruppe oder seine Vertices bewegt, wie beim [Gizmo](#left-menu-toolbar).
* `Einrasten` - Lässt das Modell auf anderen Oberflächen einrasten.
* `Oberfläche` / `Vertex` - Bei `Einrasten`: auf der Oberfläche oder am nächstgelegenen Vertex einrasten.

Mit 2 Fingern können Sie schnell zwischen zwei dieser Modi wechseln:

* Ziehen Sie ein Objekt, um es zu platzieren. Halten Sie den ersten Finger still, aber heben Sie ihn nicht vom Bildschirm.
* Setzen Sie den zweiten Finger auf den Bildschirm, während der erste aufgesetzt bleibt. Wenn Sie den zweiten Finger ziehen, wird das Objekt skaliert.
* Heben Sie den zweiten Finger an und ziehen Sie mit dem ersten weiter: Das Objekt ist wieder im Bewegungsmodus.

Sie können den zweiten Modus auch mit einem Tippen des zweiten Fingers wechseln:

* Ziehen Sie das Objekt, um es zu platzieren, halten Sie an, aber heben Sie den Finger nicht vom Bildschirm.
* Tippen Sie mit dem zweiten Finger, während der erste aufgesetzt bleibt
* Das Werkzeug wechselt in den Drehmodus. Ziehen Sie mit dem ersten Finger, um die Drehung einzustellen.
* Tippen Sie wie zuvor mit dem zweiten Finger, und das Werkzeug wechselt zurück in den Bewegungsmodus.

So können Sie sehr schnell Objekte über ein anderes klonen, zum Beispiel Felsen über eine Landschaft. Die Klonen-Schaltfläche befindet sich praktischerweise auch in der linken Werkzeugleiste:

* Bewegen Sie mit dem Werkzeug Transformieren einen Felsen an seinen Platz.
* Loslassen, die Klonen-Schaltfläche drücken
* Diesen Felsen bewegen, bei Bedarf drehen/skalieren
* Loslassen, die Klonen-Schaltfläche drücken
* Diesen Felsen bewegen, und so weiter.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Mit diesem Werkzeug bewegen, drehen und skalieren Sie Objekte und ändern ihre Drehpunkte.

Der Griff im Ansichtsfenster bietet Folgendes:

* `Bewegen` - Ziehen Sie an der Linie mit Pfeil, um entlang X/Y/Z zu verschieben. Ziehen Sie am pfirsichfarbenen Punkt in der Mitte des Gizmos, um frei im Bildschirmraum zu verschieben. Klicken Sie auf die roten, grünen und blauen Quadrate, um in den X/Y/Z-Ebenen zu verschieben.
* `Drehen` - Ziehen Sie an den roten/grünen/blauen Kreisen, um um X/Y/Z zu drehen. Ziehen Sie an der Kugel innerhalb der Kreise, um frei zu drehen.
* `Skalierung`- Ziehen Sie an den äußeren roten/grünen/blauen Punkten, um entlang X/Y/Z zu skalieren. Ziehen Sie an den äußeren roten/grünen/blauen Kegeln, um in den X/Y/Z-Ebenen zu skalieren. Ziehen Sie am äußeren pfirsichfarbenen Kreis, um gleichmäßig zu skalieren.

![](/images/tool_gizmo.webp)

#### Knoten und Vertices {#nodes-and-vertices}

Jedes Objekt in Nomad besteht aus einem Knoten und Vertices:

* `Knoten` - Der „Griff“ des Objekts. Er speichert Verschiebung, Rotation und Skalierung, die sogenannte Transformationsmatrix.
* `Vertices` - Die Punkte, die die Oberfläche eines Objekts bilden. Sie speichern Position und Farbinformationen.

Bei einer einfachen Box aus 8 Vertices könnten Sie sie verschieben, indem Sie ihre Transformationsmatrix ändern oder indem Sie die Positionen der Vertices ändern. Beim Modellieren möchten Sie meist die Vertices ändern, beim Bewegen von Objekten mit dem Gizmo meist den Knoten. Nomad erlaubt beides. 

#### Werkzeugleisten von Gizmo {#left-menu-toolbar}

Die linke Werkzeugleiste hat:

* `Klonen` - Erstellt eine eigenständige Kopie des aktuellen Objekts, die Sie mit dem Gizmo wegziehen können.
* `Instanz` - Erstellt eine Instanz des aktuellen Objekts. Die Objekte sind verknüpft: Was Sie an einem Objekt modellieren, erscheint auch an allen Instanzen.
* `Drehpunkt` - (Schlosssymbol anstelle der Taste `Sub`) Wenn aktiv, können Sie das Gizmo bewegen und drehen, ohne das Objekt zu bewegen. Wie bei `Sub` halten Sie die Taste für einen kurzen Wechsel gedrückt oder tippen darauf, damit sie aktiv bleibt.

Eine Werkzeugleiste oben im Ansichtsfenster enthält die übrigen Einstellungen:

* `Ziel` - Legt fest, ob das Gizmo auf den Knoten oder die Vertices eines Objekts wirkt:
    * `Auto` - Die Standardeinstellung. Funktioniert wie `Gruppe`, aber wenn das Mesh maskiert ist oder Symmetrie aktiv ist, wie `Vertex`.
    * `Vertex` - Wendet die Transformation auf die Vertices an und berücksichtigt dabei Maske und Symmetrie. Funktioniert nicht bei nicht abgeschlossenen Grundformen, und Instanzen sind ebenfalls betroffen.
    * `Objekt` - Bewegt nur das aktuelle Objekt und ignoriert Symmetrie und Maske. Untergeordnete Objekte bleiben an ihrem Platz.
    * `Gruppe` - Bewegt das Objekt und den Rest seiner Hierarchie und ignoriert Symmetrie und Maske.
    * `Instanz` - (Objekt und Gruppe) Dasselbe, aber alle Instanzen des Objekts bewegen sich mit.
* `Drehpunkt` - Ein Popup, um den Drehpunkt schnell zu platzieren, [weiter unten](#pivot) erklärt.
* `Alle` / `Bewegen` / `Drehen` / `Skalierung` - Zeigt alle Griffe des Gizmos oder nur die zum Bewegen, Drehen oder Skalieren.
* `Fixieren` - Standardmäßig springt das Gizmo zum Drehpunkt des ausgewählten Objekts. Wenn Fixieren aktiv ist, bleibt das Gizmo, wo es gerade ist.
* `Ausrichten` - Richtet den Drehpunkt am aktuellen Objekt oder an der Welt aus.
* `Ausricht.` (Drehung) - Lässt Drehwerte in festen Schritten einrasten. Der Schrittwert wird angezeigt und lässt sich bearbeiten, wenn das Einrasten aktiv ist. Mit der Option `Magnet` bleibt die Drehung beim Überqueren eines Schritts kurz daran haften und bewegt sich dann wieder frei; schalten Sie sie aus, um von Schritt zu Schritt zu springen.
* `Ausricht.` (Verschiebung) - Lässt Verschiebungswerte in festen Schritten einrasten. Der Schrittwert wird angezeigt und lässt sich bearbeiten, wenn das Einrasten aktiv ist.

#### ![](/icons/reset.webp) Drehpunkt {#pivot}
Mit dem Popup `Drehpunkt` in der oberen Werkzeugleiste ändern Sie den Drehpunkt schnell. Position und Ausrichtung des Drehpunkts bestimmen das Gizmo.

**Zurücksetzen** 
* `Auto` - Mitte des Objekts, ausgerichtet an seiner Transformation.
* `Zentriert` - Setzt den Drehpunkt in die Mitte des Objekts und behält seine Ausrichtung bei.
* `Unten` - Setzt den Drehpunkt unten mittig an das Objekt. Tippen Sie erneut, um stattdessen die Begrenzungsbox in Weltkoordinaten zu verwenden.
* `Oben` - Setzt den Drehpunkt oben mittig an das Objekt. Tippen Sie erneut, um stattdessen die Begrenzungsbox in Weltkoordinaten zu verwenden.
* `Objekt` - Setzt den Drehpunkt auf den Ursprung des Objekts, ausgerichtet an seiner Transformation.
* `Maske` - Setzt den Drehpunkt in die Mitte des unmaskierten Bereichs. Tippen Sie erneut, um zum maskierten Bereich zu wechseln.
* `Ausrichten` - Setzt die Drehungen auf die Ausrichtung der Welt zurück und behält die Position bei.
* `Ansicht` - Richtet den Drehpunkt an der aktuellen Ansicht aus und behält die Position bei. Er folgt der Kamera danach nicht.

**Beim Tippen (Drehpunkt-Modus)**

Nur aktiv, solange `Drehpunkt` eingeschaltet ist. Legt fest, was passiert, wenn Sie einmal auf die Oberfläche des Meshes tippen:
* `Keine` - Beim Tippen auf das Objekt passiert nichts
* `Normal` - Verschiebt und dreht den Drehpunkt, sodass er an der angetippten Stelle der Oberfläche ausgerichtet ist
* `Erster Treffer` - Verschiebt den Drehpunkt an die angetippte Stelle der Oberfläche (ohne ihn zu drehen)
* `Mitte` - Verschiebt den Drehpunkt in die Mitte des Objekts, unterhalb der angetippten Stelle.

#### Einstellungen für Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Kompakt` - Ordnet die zusätzlichen Griffe des Gizmos außerhalb oder innerhalb der Rotationskugel an
* `Widget-Größe` - Die Größe des Gizmos
* `Stärke` - Die Dicke der Linien des Gizmos
* `Deckkraft` - Die Deckkraft des Gizmos
* `Ausblenden bei Interaktion` - Legt fest, ob das Gizmo beim Ziehen vorübergehend ausgeblendet wird

-----

* `Schwelle für tangentiales Rollen` - Steuert, wie sich das Drehen verhält, wenn Sie an den Kreisgriffen ziehen, um um X/Y/Z zu drehen. Bei 0 funktioniert das Drehen wie ein Drehregler: Sie ziehen das Gizmo im Kreis. Bei 90 funktioniert es wie das Ziehen an der Schnur eines Jo-Jos: Sie ziehen in einer geraden Linie auf die Stelle Ihres ersten Klicks zu oder von ihr weg. Werte zwischen 0 und 90 kombinieren beides: Unterhalb des Werts wird linear bewegt, oberhalb kreisförmig.
* `Numerische Eingabe` - Wenn aktiv, öffnet ein einfaches Tippen auf das Gizmo ein Fenster, in dem Sie einen genauen Wert für die angetippte Achse eingeben.

::: warning
Die Werkzeuge [Gizmo](#gizmo) und [Transformieren](#transform) haben ein eigenes Symmetrie-Kontrollkästchen, getrennt von der Symmetrie beim Modellieren!

Standardmäßig ist diese Symmetrie ausgeschaltet.
:::

##### Matrix {#matrix}
Die genauen Transformationswerte des Objekts befinden sich nicht mehr in den Gizmo-Einstellungen: Sie sind in das Menü `Transformieren` oben rechts umgezogen. Sein Abschnitt `Matrix` enthält:

* ![](/icons/target.webp) `Zum Ursprung` - Bewegt das Objekt so, dass sein Drehpunkt in der Mitte der Szene liegt, dem sogenannten Ursprung.
* ![](/icons/bake.webp)  `Anwenden` - Friert das Objekt dort ein, wo es gerade ist, und setzt die Werte für Verschiebung und Drehung auf 0, die Skalierung auf 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Drehpunkt` - Wendet den Drehpunkt an: Die Matrixwerte entsprechen danach der Position des Gizmo-Griffs in der Welt.
* ![](/icons/reset.webp) `Zurücksetzen` - Ein Kurzbefehl, der die Verschiebung auf 0, die Drehung auf 0 und die Skalierung auf 1 setzt und das Objekt dabei bewegt und dreht.

::: tip Anwenden oder Drehpunkt anwenden
Erstellen Sie eine Box, wählen Sie das Werkzeug Gizmo, öffnen Sie das Menü `Transformieren` und heften Sie es an. Standardmäßig sind Verschiebung und Drehung 0, die Skalierung 1.

Aktivieren Sie den Drehpunkt-Modus, verschieben Sie den Griff zur Seite und deaktivieren Sie den Drehpunkt-Modus wieder. Der Drehpunkt hat sich geändert, aber die Verschiebungswerte sind immer noch 0. 


Wenn Sie sehen möchten, wo der Drehpunkt *wirklich* liegt, klicken Sie auf die Schaltfläche `Drehpunkt` zum Anwenden. Jetzt werden die Verschiebungswerte aktualisiert. Beachten Sie, dass sich die Box dabei nicht bewegt, auch nicht im Drehpunkt-Modus.

Bewegen und drehen Sie die Box irgendwohin und tippen Sie dann auf `Zum Ursprung`. Das Objekt wird so verschoben, dass sein Drehpunkt in der Mitte der Welt liegt, die Drehung bleibt aber unverändert.

Klicken Sie auf `Zurücksetzen`, und auch die Drehung wird auf 0 gesetzt.

Bewegen und drehen Sie die Box erneut und klicken Sie diesmal auf `Anwenden`. Der Drehpunkt bleibt, wo er ist, die Box bleibt, wo sie ist, aber Verschiebung und Drehung werden auf 0 gesetzt.

Üben Sie das ein paar Mal! Sie werden sehen, dass die Werte des Drehpunkts verborgen sind und Nomad sich darum kümmert. Wenn Sie den Drehpunkt aber auf echte Positionen im Raum setzen müssen, erledigt das Drehpunkt anwenden für Sie.

:::

* `Verschiebung` - Die Werte für die Verschiebung in X, Y, Z
* `Rotation` - Die Werte für die Drehung um X, Y, Z
* `Skalierung` - Die gleichmäßige Skalierung, wenn diese aktiv ist, sonst die Skalierung in X, Y, Z.
* `Scherung` - Die Werte für die Scherung in X, Y, Z, nur sichtbar, wenn das Objekt bereits geschert ist
* `Gleichmäßige Skalierung` - Legt fest, ob gleichmäßig oder auf jeder Achse einzeln skaliert wird

Links können Sie den Drehpunkt des Gizmos verschieben, im Video unten sehen Sie das in Aktion.
Das ist vor allem für die Drehung nützlich, da es bei der Verschiebung nichts ändert.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Face-Gruppe {#facegroup}

Mit Face-Gruppen teilen Sie Ihr Objekt in verschiedenfarbige Flächen ein. Sie können diese Gruppen in Nomad auf viele Arten nutzen:

* Als schnelle Auswahlmethode für Masken
* Um Teile Ihres Objekts aus- und einzublenden
* Um Ihr Objekt zu ordnen, ohne es in einzelne Teile zerlegen zu müssen
* Um UV-Bereiche festzulegen
* Um den Quad Remesher zu steuern
* Als zusätzliche Steuerung für Werkzeuge wie Glätten.

#### Linke Werkzeugleiste von Face-Gruppe {#facegroup-left-toolbar}

* `Gruppe` - Die Schaltfläche zeigt die aktuelle Face-Gruppe. Tippen Sie darauf, um die vorhandenen Face-Gruppen als Farbfelder anzuzeigen und eine auszuwählen. Tippen Sie auf ein Feld, um es umzubenennen, seine Farbe zu ändern oder es zu löschen. `Ungenutzte entfernen` löscht die nicht verwendeten Felder, `Zurücksetzen` entfernt alle. Mit dem Plus-Symbol erstellen Sie neue Felder.
* `Punkt` - Malen Sie auf das Objekt, um Face-Gruppen festzulegen. Wenn „+ Face-Gruppe“ aktiv ist, erstellt jeder neue Strich automatisch eine neue Face-Gruppe, praktisch, um schnell Bereiche einzuteilen. Ein Tippen füllt den gewählten Bereich. Der Regler legt den Radius des Punkts fest.
* `Entspannen` - Glättet die Ränder von Face-Gruppen. Sehr nützlich, um saubere Kanten für die Quad-Neuvernetzung zu erhalten oder um Paneele für Hard-Surface-Modelle festzulegen. Die Regler steuern Radius und Stärke des Entspannens.
* Formen - Erstellt Face-Gruppen mit Formen statt mit einem Pinsel, über `Grab • Dynamischer Radius`, `Lasso`, `Polygon`, `Linie`, `Rechteck` und `Ellipse`. Mehr dazu unter [Auswahlsteuerung](#selection-controls).
* `Wählen` - Der Sub-Modus. Wenn aktiv, wird das Feld an der Stelle gewählt, an der der Strich beginnt, und für den Rest des Strichs verwendet. Sehr praktisch zum Aufräumen von Face-Gruppen: Wenn eine Face-Gruppe zu weit reicht, aktivieren Sie `Wählen`, beginnen einen Strich dort, wo die Face-Gruppe richtig ist, und ziehen bis zum Rand, um das richtige Feld neu zuzuweisen.

#### Obere Werkzeugleiste von Face-Gruppe {#facegroup-top-toolbar}

Eine Werkzeugleiste oben im Ansichtsfenster hat weitere Einstellungen:

* `Entspannen (Alle)` - Ziehen, um die Ränder aller Face-Gruppen auf einmal zu entspannen.
* `Vorne` / `Sichtbar` / `Verbunden` - Dieselben Strichfilter wie in der Werkzeugleiste von [Maske](#mask).
* `Aus Normalen` - Erstellt Face-Gruppen anhand des Winkels zwischen den Flächen. Das Popup enthält den `Winkel` und lässt Sie kleine Gruppen nach ihrer `Anzahl der Flächen` oder ihrem `Oberflächenbereich` auslassen, mit einer `Vorschau`, bevor Sie bestätigen.
* `Aus Teilen` - Erstellt eine Face-Gruppe für jeden nicht verbundenen Teil.
* `Aus UVs` - Erstellt eine Face-Gruppe für jede UV-Insel.
* `Aus Maske` - Erstellt eine Face-Gruppe aus dem maskierten Bereich.
* `Tap` - Legt fest, was ein Tippen auf eine Face-Gruppe bewirkt: sie mit der aktuellen Face-Gruppe füllen, ausblenden, maskieren oder in `Pose` bringen (die angetippte Gruppe und alles dahinter werden demaskiert, und das Gizmo setzt sich auf das Gelenk, mit einem Regler `Unschärfe` für die Maske). Ein zweiter Schalter `Tap`, verfügbar wenn das Mesh eine Maske hat, beschränkt das Tippen auf die Flächen auf derselben Seite der Maske.
* Schaltflächen `Löschen` für die Werkzeuge [Ausblenden](#hide) und [Maske](#mask), um alles wieder einzublenden oder die Maske zu entfernen, ohne das Werkzeug zu verlassen.

#### Einstellungen für Face-Gruppe {#facegroup-settings}

Das Menü `Werkzeug` extrahiert Face-Gruppen in neue Objekte, mit denselben Optionen wie `Extrahieren` in den [Einstellungen für Maske](#mask-settings). Mit der Schaltfläche `Face-Gruppe` oben wählen Sie, welche Gruppen extrahiert werden, und es gibt zusätzlich einen Regler `Abstand`: Er verschiebt jeden Rand entlang der Oberfläche nach innen, ein negativer Wert verschiebt ihn nach außen, sodass sich die Teile überlappen. Verwenden Sie für benachbarte Paneele die Hälfte des gewünschten Abstands.

### ![](/icons/tool_hide.webp) Ausblenden {#hide}
Blendet Teile des Objekts aus oder isoliert sie. 

Die wichtigsten Modi steuern Sie über das linke Menü:

* `Punkt` - Malen Sie auf das Objekt, um Teile davon auszublenden.
* Formen -  Blendet mit Formen statt mit einem Pinsel aus, über `Lasso`, `Polygon`, `Linie`, `Rechteck` und `Ellipse`. Mehr dazu unter [Auswahlsteuerung](#selection-controls).
* `Einblenden` - Der Sub-Modus kehrt die Aktion um, sodass der gewählte Modus Teile des Objekts einblendet statt ausblendet.

Oben im Ansichtsfenster erscheint eine Werkzeugleiste mit weiteren Einstellungen:

* `Alles löschen` - Stellt die Objekte wieder her, alle ausgeblendeten Teile werden wieder eingeblendet. Wenn auch andere Objekte ausgeblendete Teile haben, stellt eine zusätzliche Schaltfläche `Löschen` nur die ausgewählten Objekte wieder her.
* `Umkehren` - Tauscht ausgeblendete und sichtbare Teile.
* `Löschen` - Löscht den ausgeblendeten Teil des Objekts
* `Teilen` - Trennt den ausgeblendeten Teil des Objekts in eine neue Form ab.
* `Vorne` / `Sichtbar` / `Verbunden` - Dieselben Strichfilter wie in der Werkzeugleiste von [Maske](#mask).
* `Tap` (Face-Gruppe) - Nutzt Face-Gruppen, um schnell Bereiche auszublenden: Ein Tippen auf eine Face-Gruppe blendet die ganze Face-Gruppe aus.
* `Tap` (Maske) - Wenn eine Maske vorhanden ist, blendet ein Tippen den maskierten Bereich aus.

### ![](/icons/tool_measure.webp) Messen {#measure}
Ziehen Sie, um den Abstand zwischen 2 Punkten zu messen. Danach können Sie die Endpunkte verschieben, um die Messung anzupassen.

In der linken Werkzeugleiste wählen Sie, wie der Abstand gemessen wird:

* `Linie` - Eine gerade Linie zwischen den beiden Punkten.
* `Oberfläche` - Der Abstand entlang der Oberfläche, entlang des Schnitts durch die beiden Punkte, wie von der Kamera aus gesehen.
* `Querschnitt` - Der Umfang des Querschnitts durch die beiden Punkte, wie ein Maßband um einen Arm.
* `Vertex` - Lässt die Endpunkte am nächstgelegenen Vertex einrasten.
* `Goldener Schnitt` - Zeigt einen gelben Punkt an der Stelle des Goldenen Schnitts der Messung.
* Die Schaltfläche `?` zeigt Volumen, Oberfläche und Größe der ausgewählten Objekte.

### ![](/icons/tool_arrange.webp) Anordnen {#arrange}
Richtet mehrere Objekte auf einmal aus und verteilt sie, wie die Ausrichtungswerkzeuge einer 2d-Design-App. Wählen Sie zuerst die Objekte aus; bei einem einzelnen Objekt arbeitet Anordnen stattdessen mit seinen getrennten Teilen. Um die Auswahl wird ein Rahmen gezeichnet, dessen Griffe Sie zum Skalieren ziehen können.

Eine Werkzeugleiste oben im Ansichtsfenster enthält die Einstellungen:

* `Welt` / `Bildschirm` - Ordnet entlang der Weltachsen oder entlang des Bildschirms an (links, rechts, oben, unten).
* `Ausrichten` - Richtet die Objekte auf jeder Achse an ihrem Minimum, ihrer Mitte oder ihrem Maximum aus.
* `Verteilen` - Verteilt die Objekte gleichmäßig zwischen den beiden äußeren, nach Minimum, Mitte oder Maximum. Dafür sind mindestens 3 Objekte nötig.
* `Linie` - Ordnet die Objekte in einer Reihe entlang einer Achse an.
* `Raster` - Ordnet die Objekte in einem Raster an, mit einer Anzahl von Objekten auf `X`, `Y` und `Z`.
* `Kreis` - (nur Welt) Ordnet die Objekte in einem Kreis um die Achse `X`, `Y` oder `Z` an.
* `Kugel` - (nur Welt) Ordnet die Objekte auf einer Kugel an.

`Linie`, `Raster`, `Kreis` und `Kugel` haben alle einen Regler `Abstand` für die Lücke zwischen den Objekten.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Dieses Werkzeug wandelt das ausgewählte Objekt in eine saubere Quad-Topologie um, mit Einstellungen für Dichte, Kantenfluss und Symmetrie. 

::: tip
Quad Remesher wird von [Exoside](https://exoside.com/) für iOS und Desktop entwickelt. 

Unter iOS ist er ein In-App-Kauf in Nomad, eine einmalige Zahlung von 16 USD.

Für den Desktop kaufen Sie eine Lizenz bei [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Sie können sie nur für Nomad Desktop kaufen oder als übergreifende Lizenz für alle unterstützten Desktop-Apps.

Wenn Sie Quad Remesher bereits für eine andere Desktop-App besitzen, können Sie [günstiger ein Upgrade auf alle Plattformen kaufen.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher ist für Android nicht verfügbar. Unter Android können Sie die kostenlosen Open-Source-Remesher im Topologie-Tab [Quad-Neuvernetzung](topology.md#quad-remesh) verwenden (AutoRemesher, Instant Mesh, QuadriFlow), deren Funktionsumfang ist aber eingeschränkter.
:::

Solange Quad Remesher nicht freigeschaltet ist, beginnt die obere Werkzeugleiste mit einer Einkaufswagen-Schaltfläche statt der Remesh-Schaltflächen. Unter iOS öffnet sie den In-App-Kauf. Auf dem Desktop zeigt sie `Entsperren (kaufen, wiederherstellen, testen)`, womit Ihre Exoside-Lizenz geprüft (oder die Testversion gestartet) wird. Sobald er aktiv ist, werden die linke und die obere Werkzeugleiste freigegeben.

* `Punkt` - Dieser Pinsel legt die Zieldichte fest. Bei 100 % Stärke malen Sie in Rot, dort wird die doppelte Quad-Zieldichte verwendet. Bei 0 % Stärke malen Sie in Cyan, dort wird die halbe Quad-Zieldichte verwendet. Bei 50 % Stärke malen Sie in Grau, dort wird die normale Quad-Zieldichte verwendet.
* `Glätten` - Glättet die Übergänge der roten/grauen/cyanfarbenen Dichte.
* `Wischfinger` - Verwischt die Dichtebemalung.
* `Kurve` - Skizzieren Sie Kurven auf die Oberfläche der Skulptur; Quad Remesher verwendet sie als Leitlinien für den Kantenfluss. Tippen Sie auf eine Kurve, um sie zu löschen.
* `Pfad` - Zeichnen Sie Pfade auf die Oberfläche der Skulptur; Quad Remesher verwendet sie als Leitlinien für den Kantenfluss. Tippen Sie auf einen Pfad, um ihn zu löschen. 
* `Rechteck` - Zeichnen Sie Rechtecke auf die Oberfläche der Skulptur; Quad Remesher verwendet sie als Leitlinien für den Kantenfluss. Tippen Sie auf einen Pfad, um ihn zu löschen.
* `Ellipse` - Zeichnen Sie Ellipsen auf die Oberfläche der Skulptur; Quad Remesher verwendet sie als Leitlinien für den Kantenfluss. Tippen Sie auf einen Pfad, um ihn zu löschen.

#### Obere Werkzeugleiste von Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Oben im Ansichtsfenster erscheint eine Werkzeugleiste mit weiteren Einstellungen:


* `<Anzahl>` - Klicken Sie hier, um die Quad-Neuvernetzung zu starten. Die Zahl zeigt die angestrebte Anzahl an Quads.
* `Vierecke` - Stellen Sie die angestrebte Anzahl an Quads ein, indem Sie nach links und rechts wischen, oder tippen Sie, um eine genaue Zahl einzugeben. Diese Zahl ist eher ein Richtwert als ein fester Wert: Durch die verschiedenen Einstellungen des Quad Remeshers weicht das Ergebnis oft davon ab.
* `Halb` - Ein Kurzbefehl, der die Zielanzahl auf die Hälfte der aktuellen Polygonanzahl setzt.
* `Identisch` - Ein Kurzbefehl, der die Zielanzahl auf die aktuelle Polygonanzahl setzt.
* `Leitlinien` - Leitlinien verwenden oder ignorieren. Wenn Leitlinien vorhanden sind, zeigt eine zweite Schaltfläche `Leitlinien` ihre Anzahl; tippen Sie darauf, um alle zu löschen.
* `Dichte` - Dichtebemalung verwenden oder ignorieren. Wenn eine Dichtebemalung vorhanden ist, entfernt eine zweite Schaltfläche `Dichte` sie.
* `Face-Gruppe` - Face-Gruppen zur Steuerung des Quad Remeshers verwenden oder ignorieren.
* `Entspannen` - Entspannt die Ränder der Face-Gruppen automatisch während der Quad-Neuvernetzung. Wenn Sie die Ränder Ihrer Face-Gruppen schon entspannt/geglättet haben, schalten Sie diese Option aus.
* Regler `Entspannen` - Ein Kurzbefehl-Regler, um die Ränder der Face-Gruppen zu entspannen.
* `Harte Kanten` - Versucht, harte Kanten zu erhalten.
* `Vertex umprojizieren` - Projiziert das neue Netz zurück auf das ursprüngliche Mesh.
* `Sym` - Erzeugt ein symmetrisches Ergebnis. Die Symmetrie wird immer um die X-Achse der Welt berechnet. Achten Sie also darauf, dass Ihr Modell im Ursprung liegt, wenn Sie ein symmetrisches Ergebnis erwarten.
* `...` - Popup mit den Einstellungen des Quad Remeshers. 

#### Einstellungsmenü von Quad Remesher {#quad-remesher-settings-menu}

Die Schaltfläche `...` am Ende der oberen Werkzeugleiste öffnet ein Popup mit den übrigen Einstellungen:

* `Adaptive Quad-Anzahl` - Verwendet kleinere Quads in stark gekrümmten Bereichen und größere Quads in schwach gekrümmten.
* `Adaptive Größe` - Legt fest, wie stark sich die Größe anpasst. 100 % erlaubt die größte Anpassung, bei 0 % sind die Quads einheitlich.

::: tip

Ein Rezept für eine gute Quad-Neuvernetzung mit möglichst wenigen Fehlern:

* Teilen Sie das Mesh in Face-Gruppen ein, um Ihren idealen Quad-Fluss festzulegen.
* Entspannen Sie die Face-Gruppen, um glatte Ränder zu erhalten.
* Dezimieren Sie. So vermeiden Sie dünne oder verzerrte Flächen an den Rändern der Face-Gruppen. Achten Sie darauf, dass in den Dezimieren-Einstellungen Face-Gruppe aktiviert ist. Dann folgen die Dreieckskanten genau den Rändern Ihrer Face-Gruppen. 

Schalten Sie in den Optionen der Quad-Neuvernetzung Entspannen aus (da Sie das Mesh bereits entspannt haben), und Sie sollten gute Ergebnisse erhalten.

:::

### ![](/icons/tool_select.webp) Auswählen {#select}
Wählen Sie mit den Formmodi (`Lasso`, `Rechteck`, `Ellipse`) Objekte in der Szene aus. `Abwählen` entfernt Objekte aus der Auswahl.

### ![](/icons/tool_lattice.webp) Gitter {#lattice}
Verformt ein Objekt mit einem Käfig aus Kontrollpunkten um es herum, statt seine Oberfläche zu modellieren. Wenn Sie ein paar Punkte des Käfigs verschieben, wird das ganze Objekt sanft gebogen, verdreht oder gestreckt, ideal, um Proportionen anzupassen oder zu posieren, ohne die Topologie anzufassen. Die Verformung bleibt live, bis Sie sie abschließen.

In der linken Werkzeugleiste wählen Sie, wie Sie den Käfig bearbeiten:

* `Punkte` - Ziehen Sie direkt an den Punkten und Kanten des Käfigs. Tippen Sie auf einen Punkt, um ihn auszuwählen.
* `Ansicht` - Bewegt die Kamera, ohne den Käfig zu bearbeiten.
* `Entspannen` - Ein Pinsel, der die Käfigpunkte darunter entspannt.
* `Elastisch` - Ein Pinsel, der die Käfigpunkte mit einem elastischen Falloff zieht, wie das Werkzeug [Elastisch](#elastic).
* `Gizmo` - Bewegt, dreht und skaliert die ausgewählten Punkte mit dem Gizmo. Sein Sub-Modus ist `Drehpunkt`.
* `Lasso` - Wählt Käfigpunkte mit einem Lasso aus, `Abwählen` entfernt sie aus der Auswahl.

Das Form-Popup enthält außerdem `Weicher Radius`, damit beim Ziehen eines Punkts auch die benachbarten Punkte mitbewegt werden (in Rasterzellen, 0 bewegt nur die Auswahl), und `Auswahl umkehren`.

Eine Werkzeugleiste oben im Ansichtsfenster hat:

* `Abschließen` - Wendet die Verformung auf das Objekt an und entfernt den Käfig.
* `Zurücksetzen` - Entfernt den Käfig und seine Verformung.
* `Deckkraft` - Die Deckkraft, mit der der Käfig angezeigt wird.
* `Spiegelseite` - Bei Symmetrie wechselt diese Option, welche Spiegelseite des Käfigs angezeigt wird und ausgewählt werden kann, mit einer eigenen `Deckkraft` für die verborgene Seite.
* `Gitterpunkte` - Welche Punkte des Käfigs sich bewegen lassen: das ganze Raster, die Oberfläche und der Mittelpunkt, oder nur die Oberfläche.
* `Steifigkeit` - Wie steif die Verformung ist, von weich (0 %) bis starr und linear (100 %).
* `Falloff` - Wie weit die Verformung außerhalb des Käfigs ausläuft.
* `Ausrichten` - Richtet den Käfig am Objekt oder an der Welt aus.
* `X`, `Y`, `Z` `Unterteilung` - Die Anzahl der Zellen des Käfigs auf jeder Achse. Die Modus-Schaltfläche daneben legt fest, wie sie zusammenhängen: `x = y = z` verwendet auf allen 3 Achsen dieselbe Anzahl, `Einheitlich` hält den Abstand zwischen den Punkten auf allen Achsen gleich, und mit `Benutzerdefiniert` stellen Sie jede Achse frei ein.

#### Einstellungen für Gitter {#lattice-settings}
* `Rollgeschwindigkeit` - Dieselben Rolloptionen wie beim Werkzeug [Bewegen](#move-settings), verwendet beim Ziehen von Käfigpunkten.

### ![](/icons/tool_view.webp) Ansicht {#view}
Dieses „Werkzeug“ tut nichts Besonderes: Es ist einfach eine Möglichkeit, das Modell zu betrachten, ohne Ihre Szene zu verändern.

#### Einstellungen für Ansicht {#view-settings}
Solange das Werkzeug Ansicht aktiv ist, überschreiben diese Einstellungen einige Anzeigeoptionen, damit Sie eine saubere Ansicht zum Präsentieren oder Prüfen Ihres Modells erhalten:

* `Grundformen (Bearbeiten)`, `Repeater (Bearbeiten)`, `Licht (Bearbeiten)`, `Kamera (Bearbeiten)` - Erlaubt das Bearbeiten von Grundformen, Repeatern, Lichtern und Kameras im Ansichtsfenster, während das Werkzeug Ansicht aktiv ist. Schalten Sie sie aus, um ihre Griffe nicht versehentlich zu verschieben.
* `Kamera-Shortcut (immer)` - Zeigt die Kamera-Kurzbefehle immer im Ansichtsfenster an.
* `Maske anzeigen`, `Umriss`, `Nicht gewählte Meshes abdunkeln` - Zeigt die Maske, den Umriss der ausgewählten Objekte oder dunkelt die nicht ausgewählten Objekte ab. `Auto` folgt Ihrer üblichen Einstellung, `Nein` und `Ja` erzwingen sie.
* `Linie anzeigen (Symmetrie)`, `Ebene anzeigen (Symmetrie)` - Zeigt die Symmetrielinie oder -ebene, mit denselben Möglichkeiten `Auto`, `Nein` und `Ja`.
* `Icon` - Zeigt die Symbole von Gruppen, Repeatern, Lichtern, Kameras und die Hierarchie im Ansichtsfenster, mit denselben Möglichkeiten.


## Kontextmenü der Toolbox {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Ein Rechtsklick oder langes Drücken auf ein Werkzeug in der Toolbox öffnet ein Kontextmenü mit folgenden Optionen:

* `Speichern` - Speichert alle Änderungen, die Sie am Werkzeug vorgenommen haben
* `Klonen` - Dupliziert das Werkzeug als neue Werkzeugverknüpfung
* `Letzte Speicherung` - Kehrt zur zuletzt gespeicherten Version des Werkzeugs zurück
* `Icon` - Ändert das Symbol des Werkzeugs. Wenn das Werkzeug ein eigenes Symbol hat, entfernt diese Schaltfläche es.
* `→ ...` - Verschiebt das Werkzeug in einen anderen Ordner der Toolbox oder in einen neuen
* `Zurücksetzen` - Setzt das Werkzeug auf seine Standardwerte zurück

Geklonte Werkzeuge haben außerdem `Umbenennen` und `Löschen`.