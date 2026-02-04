# ![](/icons/toolbox.webp) Werkzeuge {#tools}

![](/images/tools_menu.webp)

::: tip
Springe zu [Werkzeuge](#tools-1) für Beschreibungen der einzelnen Werkzeuge.
:::

## Übersicht {#overview}

Werkzeuge werden aus der `Toolbox` auf der rechten Seite ausgewählt und mit den `Tool Controls` auf der linken Seite gesteuert. Zusätzliche Einstellungen befinden sich im Menü `Settings`, dem ersten Symbol im Menü oben rechts.

Pinselwerkzeuge haben Regler für Größe und Intensität. Auswahlwerkzeuge haben Regler für verschiedene Auswahlstile. Am unteren Ende der Werkzeugsteuerung befinden sich Kurzbefehle für häufig verwendete Operationen (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Die Werkzeuge von Nomad sind in der Toolbox farbcodiert:

* <span class=brush>**Pinselwerkzeuge**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Move-Werkzeuge**</span> (Move, Drag)
* <span class=mask>**Maskenwerkzeuge**</span> (Mask, SelMask)
* <span class=paint>**Malwerkzeuge**</span> (Paint, Smudge)
* <span class=flatten>**Flatten-Werkzeuge**</span> (Flatten, Planar)
* <span class=pinch>**Pinch-Werkzeuge**</span> (Crease, Pinch)
* <span class=selection>**Auswahlbasierte Werkzeuge**</span>, bei denen zuerst eine 2D-Maske gezeichnet wird und anschließend eine Operation erfolgt (Trim, Split, Project)
* <span class=creation>**Erstellungswerkzeuge**</span> (Tube, Lathe, Insert)
* <span class=transform>**Transformationswerkzeuge**</span> (Transform, Gizmo)
* <span class=misc>**Sonstige Werkzeuge**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Ansichtswerkzeug**</span>



Viele dieser Werkzeuge können über das [Stroke](stroke.md)-Menü mit unterschiedlichem Pinselverhalten, Druck, Texturen usw. angepasst werden. 


### Pinselsteuerung {#brush-controls}

Die linke Werkzeugleiste hat Schieberegler für Radius und Intensität sowie werkzeugkategoriespezifische Regler, die unten erklärt werden.

![](/images/tool_left_panel.webp)

::: tip
Der Intensitätsregler kann bei vielen Werkzeugen über 100 % hinausgehen – es lohnt sich, damit zu experimentieren!
:::

### Sub‑Modus {#sub-mode}
Die Schaltfläche direkt unter dem Intensitätsregler ist die `Sub`-Schaltfläche. Ihre Beschriftung und Funktion ändert sich mit jedem Werkzeug, und wenn sie gedrückt wird, wird ein alternatives, meist entgegengesetztes Verhalten aufgerufen. Z. B. ruft sie bei [Paint](#paint) einen Löschmodus auf, bei [Crease](#crease) erzeugt sie erhabene Kanten statt Furchen usw.

Standardmäßig funktioniert sie als „Sticky Button“; d. h. du kannst sie gedrückt halten, um sie vorübergehend zu aktivieren, und wenn du loslässt, wird sie wieder deaktiviert. Wenn du sie antippst, wird der Sub-Modus dauerhaft aktiviert.

### Kurzbefehle {#shortcuts}
Am unteren Ende der linken Werkzeugleiste befinden sich Kurzbefehle für [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Standardmäßig funktionieren diese alle als „Sticky Buttons“; d. h. du kannst sie gedrückt halten, um sie vorübergehend zu aktivieren, und wenn du loslässt, werden sie wieder deaktiviert. Wenn du sie antippst, wird dieser Shortcut-Modus dauerhaft aktiviert.

### Auswahlsteuerung {#selection-controls}

Die Werkzeuge [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) und [Hide](#hide) verwenden ähnliche Steuerungen, um Bereiche des Meshes auszuwählen.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` – Eine freihändig gezeichnete Form
* `Polygon` – Eine geschlossene Form, die durch eine Kombination aus Kurven und/oder geraden Linien definiert ist. Siehe [Shape editing](#shape-editing) unten für weitere Informationen.
* `Curve` – (nur Project) – Eine freihändige Kurve für die Projektion
* `Path` – (nur Project) – Eine durch Punkte definierte Kurve. Siehe [Shape editing](#shape-editing) unten für weitere Informationen.
* `Line` – Ziehe eine Linie, um ein planeres Segment zu definieren. Standardmäßig wird sofort auf das Mesh angewendet; deaktiviere Auto Validate, wenn du das nicht möchtest (lange auf das Liniensymbol drücken oder darüber wischen).
* `Rect` – Ziehe eine Diagonale, um die Ecken einer Rechteckform zu definieren. Langes Drücken oder Wischen zeigt Optionen für Auto Validate, Erzwingen einer quadratischen Form und dafür, dass der erste Klick das Zentrum des Rechtecks ist.
* `Ellipse` – Ziehe eine Diagonale, um die Größe einer Ellipse zu definieren. Langes Drücken oder Wischen zeigt Optionen für Auto Validate, Erzwingen einer Kreisform und dafür, dass der erste Klick das Zentrum der Ellipse ist.
* `Flip` – Invertiert die Formmaske oder die Richtung des Project-Werkzeugs.

Die meisten Werkzeuge haben eine Option für Auto Validate, was bedeutet, dass die Operation ausgeführt wird, sobald du die Form fertig gezeichnet hast. Wenn Auto Validate deaktiviert ist, wird neben der Form eine grüne Schaltfläche angezeigt, die die Operation ausführt. So kannst du die Form bearbeiten, die Ansicht anpassen und, wenn du bereit bist, die Form zu verwenden, die grüne Schaltfläche drücken.

### Formbearbeitung {#shape-editing}
Polygon- und Kurvenbearbeitung verhalten sich ähnlich:

* Zu Beginn ziehst du eine Linie, um 2 Punkte zu definieren, dann ziehst du aus der Mitte der Linie heraus, um ein Polygon oder eine Kurve zu definieren.
* Klicke auf die Punkte, um zwischen weich und scharf umzuschalten. 
* Klicke und ziehe auf Kurven- oder Linienabschnitten, um neue Punkte zu erzeugen.
* Um einen Punkt zu löschen, ziehe ihn in seinen Nachbar, bis er rot wird.
* Das Papierkorbsymbol in der Ecke des Polygon- oder Pfadsymbols löscht die Form.

### Einstellungsmenü {#settings-menu}

Viele Werkzeuge haben zusätzliche Einstellungen, die im Einstellungsmenü zu finden sind, dem ersten Symbol im Menü oben rechts:

![](/images/tools_settings_menu.webp)

## Werkzeuge {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Ton {#clay}
Das Clay-Werkzeug ist nützlich, um deine Skulptur aufzubauen. `Sub` entfernt Material von deiner Skulptur.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pinsel {#brush}
Der Standardpinsel. `Sub` entfernt Material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Verschieben {#move}
Der Bereich unter dem Pinsel bleibt am Pinsel „kleben“ und ermöglicht elastische Deformation. Die Auswahl bleibt während der Bewegung erhalten, sodass, wenn du den Pinsel wegbewegst und dann wieder an die Ausgangsposition zurückbewegst, keine Deformation sichtbar ist.

Der Sub-Modus ist `Normal` und bewegt den Bereich unter dem Pinsel entlang der Flächennormale.

Dieser Pinsel eignet sich sowohl für großflächige Deformationen als auch für sorgfältige kleine Verformungen.

#### Verschieben‑Einstellungen {#move-settings}

* `Radius (Background)` – Wie weit du vom Rand eines Modells entfernt sein kannst und trotzdem noch modellieren kannst; nützlich beim Arbeiten an der Silhouette eines Objekts. 
* `Same-side vertex only` – Ignoriere Vertices, die in die entgegengesetzte Richtung der Deformation zeigen.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Ziehen {#drag}
Der Bereich unter dem Pinsel bleibt am Pinsel „kleben“ und ermöglicht elastische Deformation. Im Gegensatz zum Move-Pinsel wird die Auswahl während des Strichs kontinuierlich aktualisiert, sodass es möglich ist, längere, schlangenartige Objekte zu erzeugen, insbesondere wenn Dynamic Topology aktiviert ist.

Der Sub-Modus ist `Normal` und bewegt den Bereich unter dem Pinsel entlang der Flächennormale.

Dieser Pinsel eignet sich gut für lockerere, gestische Formänderungen.

#### Ziehen‑Einstellungen {#drag-settings}

* `Radius (Background)` – Wie weit du vom Rand eines Modells entfernt sein kannst und trotzdem noch modellieren kannst; nützlich beim Arbeiten an der Silhouette eines Objekts. 
* `Same-side vertex only` – Ignoriere Vertices, die in die entgegengesetzte Richtung der Deformation zeigen.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Glätten {#smooth}
Glättet den Bereich, indem die Punktpositionen gemittelt werden. Dieses Werkzeug ist stark von der Polygonanzahl abhängig.
Wenn du viele Polygone hast, ist die Glättung weniger effektiv.

Der Sub-Modus ist `Relax`, der nur das Drahtgitter glättet, aber versucht, die geometrischen Details zu erhalten.

#### Glätten‑Einstellungen {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Flächengruppe {#smooth-facegroup}

* `Relax` – Glättet die Ränder von Facegroups. Verwende Intensitäten über 100 %, um Ränder schnell zu glätten. `Auto` glättet nur, wenn die Facegroup-Vorschau aktiviert ist, `Off` deaktiviert, `On` aktiviert.

##### Vertex {#vertex}
* `Sticky vertex on border` – Bei Meshes mit offenen Kanten, z. B. einer Ebene, ist es möglich, die Ecken zu glätten. Wenn diese Option aktiviert ist, werden die offenen Kanten fixiert.
* `Relax` – Dasselbe wie der Relax-Alternativmodus in der linken Werkzeugleiste.
* `Stable smoothing` – Versucht, die Glättung topologieunabhängig zu machen. Dies funktioniert am besten bei variierender Topologiedichte und mit einem hohen Glättungsintensitätswert.

##### Malen {#painting}
* `Screen Smoothing` – Verwende diese Option, um topologieunabhängige Glättung zu erhalten, selbst bei hoher Polygonanzahl.
* `Screen samples` – Die Qualität der Glättung; höhere Werte sind glatter, aber langsamer.

::: tip
Höhere Polygonanzahlen können erfordern, die Intensität über 100 % zu erhöhen. Sehr hohe Werte (300 %, 500 %) können auch gut als Modellierwerkzeug funktionieren, indem Bereiche schnell flach und glatt unter dem Pinsel werden – wie ein Schlag mit einem Holzhammer auf Ton!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maske {#mask}
Dieses Werkzeug ermöglicht es dir, Vertices zu maskieren. Maskierte Vertices sind vor Sculpting oder Painting geschützt. 

Der Sub-Modus ist `Unmask` und löscht die Bereiche, in denen die Maske gemalt wurde.

Ähnlich wie Auswahlen in 2D-Malprogrammen können Masken mit einem Pinsel gemalt oder mit Formauswahlen erstellt, weichgezeichnet oder geschärft werden. 

Im Gegensatz zu 2D-Malprogrammen können sie auch über Facegroups erstellt werden, und Masken können verwendet werden, um neue Geometrie über Extrusions-/Extraktions-Operationen zu erzeugen. 

![](/videos/tool_mask1.mp4)

 Eine Werkzeugleiste erscheint oben im Viewport mit zusätzlichen Steuerungen. 

![](/images/tool_mask_toolbar.webp)

Der Titel der Leiste kann angetippt werden, um sie ein- oder auszuklappen, oder der Pfeil oben rechts kann angetippt werden, um sie an den oberen oder unteren Rand der UI zu verschieben.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Clear              | Maske löschen                                                                              |
| ![](/icons/invert.webp)        Invert             | Maske invertieren                                                                          |
| ![](/icons/sharpen.webp)       Sharpen            | Maskenkante schärfen                                                                       |
| ![](/icons/blur.webp)          Blur               | Maskenkante weichzeichnen                                                                  |
|                                 Blur ->            | Nach links/rechts ziehen, um die Maske interaktiv zu weichzeichnen                        |
| ![](/icons/culling.webp)       Front              | Umschalten, um nur frontseitige Vertices zu maskieren                                     |
|                                 Convert            | Maske in eine Facegroup umwandeln                                                          |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Wenn aktiviert, werden Facegroups angezeigt; Tippen auf eine Facegroup maskiert sie       |
|                                 On tap (mask)      | Wenn aktiviert, füllt das Tippen auf eine „Insel“ maskierter oder unmaskierter Polygone diese Insel |
| ![](/icons/vertex.webp)        Connected          | Wenn aktiviert, dürfen Maskenstriche nur zusammenhängende Topologie beeinflussen          |

##### Masken‑Schnellgeste {#mask-quick-gesture}
Du kannst ZBrush-ähnliche Gesten ausführen, während du die Quick-Masking-Schaltfläche in der linken Werkzeugleiste gedrückt hältst:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Auf den Hintergrund tippen         |
| Clear   | Auf dem Hintergrund ziehen         |
| Blur    | Auf maskierten Bereich tippen      |
| Sharpen | Auf unmaskierten Bereich tippen    |


#### Masken‑Einstellungen {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` – Das Masken-Einstellungsmenü wird hauptsächlich verwendet, um Geometrie aus der Maske zu erzeugen. Daher ist das Standardverhalten, eine Vorschau der neuen Geometrie anzuzeigen. Du kannst wählen, ob keine Vorschau, eine Extract-Vorschau, eine Split-Vorschau und ob diese Geometrie im X-Ray-Modus angezeigt werden soll.

##### Dicke {#thickness}
* `Height` – Die Höhe der extrahierten Form. Mit dem Plus/Minus-Symbol kannst du zwischen einer nach außen gerichteten Extrusion, einer nach innen gerichteten oder einer zentrierten Extrusion wechseln. 
* `Height/Height+Mask` – Umschalten, ob die Höhe konstant sein soll oder ob weichgezeichnete Teile der Maske die Höhe beeinflussen sollen, sodass weiche und variierende Höhenformen möglich sind. 

##### Glätte {#smoothness}
Wenn aktiv, werden die Ränder der extrahierten Form geglättet; dies funktioniert besser bei höherer Polygonanzahl. 
* `Iterations` – Die Menge der angewendeten Glättung. Hohe Werte erzeugen sehr glatte, gekrümmte Kanten, können aber dazu führen, dass sich die Form von der Maskenform entfernt.
* `All/Sharp border/Borders only` – Die Glättung kann in alle Richtungen wirken und sowohl die Seiten als auch die Oberseite der extrahierten Form glätten, oder die Oberseite und Seiten glätten, aber eine scharfe Kante beibehalten, oder nur den Rand glätten und die Oberseite unverändert lassen.

##### Kantenloop (Seite) {#edge-loop-side}
* `Auto Edge-loop (side)` – Berechnet die Anzahl der Unterteilungen an den Seiten der extrahierten Form, um quadratische Polygone zu erzeugen, die zu den Polygonen des maskierten Bereichs passen. Wenn deaktiviert, kannst du die Anzahl der Edge-Loops selbst mit dem Edge-Loop-Schieberegler einstellen.

----

##### Extrahieren {#extract}
* `Extract` – Erzeugt die extrahierte Geometrie.
* `Closing action` – Wie sich Extract verhalten soll. „None“ dupliziert die maskierten Polys in eine neue Form. „Fill“ macht dasselbe und versucht, die Rückseite zu schließen. „Shell“ extrudiert um den in „thickness“ eingestellten Betrag und ist die Standardeinstellung.

::: tip

Wenn die Vorschau auf „Extract“ mit aktiviertem „X-ray“ steht, kann das Klicken auf die Schaltfläche Extract anfangs verwirrend sein. Da das Menü aktiv ist, versucht es, eine Vorschau einer Extraktion auf deiner neuen Form zu erstellen und die ursprüngliche Oberfläche im X-Ray-Modus anzuzeigen. Da du jedoch keine Maske auf der neuen Oberfläche hast, kann Nomad die Extraktion nicht vorschauen und warnt dich mit „Nothing to Extract!“. 

Das ist normal. Schließe das Masken-Einstellungsmenü, um die neue Form und das Original zu sehen, und wähle die ursprüngliche Oberfläche erneut aus, wenn du die Maske löschen oder neue Masken zeichnen musst.
:::

##### Aufteilen {#split-mask}
* `Split` – Extrahiert sowohl die maskierten als auch die unmaskierten Bereiche in neue Formen. 
* `Closing action (masked)` – Wie sich die Maskenextraktion verhalten soll. „None“ dupliziert die maskierten Polys in eine neue Form. „Fill“ macht dasselbe und versucht, die Rückseite zu schließen. „Shell“ extrudiert um den in „thickness“ eingestellten Betrag und ist die Standardeinstellung.
* `Closing action (unmasked)` – Wie sich die unmaskierte Extraktion verhalten soll. „None“ dupliziert die maskierten Polys in eine neue Form. „Fill“ macht dasselbe und versucht, die Rückseite zu schließen. „Shell“ extrudiert um den in „thickness“ eingestellten Betrag und ist die Standardeinstellung.
* `Sync border` – Stellt sicher, dass der Rand zwischen den maskierten und unmaskierten extrahierten Formen nahe beieinander bleibt. Wenn deaktiviert, kann sich aufgrund der Shell-Operation, die jede Fläche entlang ihrer Normalen extrudiert, ein Spalt zwischen den Formen bilden.

##### Schnitzen {#carve}
* `Carve` – Im Standardmodus verhält es sich so, als hättest du die Oberfläche um den Betrag „thickness“ getrimmt, wie das Ausschneiden eines Stücks Orangenschale. 



### ![](/icons/tool_maskSelector.webp) Auswahlmaske {#selection-mask}
Dieses Werkzeug ähnelt größtenteils dem [Masking-Werkzeug](#mask). Der Hauptunterschied besteht darin, dass du keine Striche zum Malen der Maske verwendest, sondern die [Selection Controls](#selection-controls).

Der Sub-Modus ist `Unmask` und löscht die Maske mithilfe der Auswahlsteuerung.

Selection Mask verwendet dieselben Werkzeugeinstellungen wie das `Mask`-Werkzeug.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Farbe {#paint}
Wendet Farbe und Materialeigenschaften an. Um mehr über Materialien zu erfahren, kannst du den Abschnitt [Painting](painting.md) besuchen.

Der Sub-Modus ist `Erase` und entfernt Farbe.

#### Farbeinstellungen {#paint-settings}
* `Layer fitering` – Funktioniert wie die Ebenen-Alpha-Sperre in Photoshop oder Procreate. Wenn du auf einer Ebene malst, kannst du bei aktivierter Option nur dort ändern, wo bereits Farbe vorhanden ist; unbemalte Bereiche sind geschützt.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Verwischen {#smudge}
Verschmiert Farbe und Materialeigenschaften. Das Smudge-Einstellungsmenü enthält einen `Quality`-Schieberegler; niedrigere Werte bedeuten schnellere Striche.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Abflachen {#flatten}
Flacht den Bereich ab, indem die Punkte auf eine Durchschnittsebene projiziert werden.

Der Sub-Modus ist `Fill` und definiert eine Ebene, die durch den höchsten Punkt festgelegt wird, und zieht Punkte tendenziell nach oben.

#### Abflach‑Einstellungen {#flatten-settings}

* `Lock plane direction` – Verwendet die beim ersten Klick berechnete Ebenenrichtung. Standardmäßig deaktiviert.
* `Lock plane origin` – Verwendet den ersten Klick als Zentrum der Ebene. Standardmäßig deaktiviert.

Wenn eine oder beide Optionen deaktiviert sind, kann Flatten durch lange Striche, die sich über unterschiedliche Tiefen und Krümmungen bewegen, schrittweise vertieft oder der Ebenenwinkel verändert werden. Dies bietet in Verbindung mit den Bereichsabtastungsoptionen des Pinselmenüs eine sehr präzise Kontrolle.

::: tip
Wenn du in Bereichen mit hoher Krümmung arbeitest, z. B. die Wangen abflachen möchtest, das Werkzeug aber ständig die Seiten der Nase beeinflusst, versuche, eine Maske zu erstellen, um Bereiche zu schützen, die der Flatten-Pinsel nicht beeinflussen soll.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Macht Punkte plan, indem sie auf eine Durchschnittsebene projiziert werden, jedoch mit weniger Aufbau als beim Flatten-Pinsel. Dies erzeugt sauberere Hard-Surface-Flächen. Schnelle Striche drücken und ziehen stärker an der Oberfläche, langsamere Striche, die von bereits planen Bereichen ausgehen und sich nach außen bewegen, erhalten die Ebene besser.

Der Sub-Modus ist `Fill` und definiert eine Ebene, die durch den höchsten Punkt festgelegt wird, und zieht Punkte tendenziell nach oben.

Planar ist tatsächlich dasselbe Werkzeug wie `Flatten`, jedoch mit aktiviertem `Lock plane direction`, was dazu führt, dass stabilere, harte Flächen entstehen, während Flatten eher skulptural ist und verwendet werden kann, um halbflache Bereiche zu erzeugen.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Falte {#crease}
Crease-Werkzeuge sind nützlich, um kleine Schnitte oder Dellen zu modellieren.

Der Sub-Modus ist `Invert` und erzeugt eine erhabene Falte.

#### Falten‑Einstellungen {#crease-settings}

* `Pinch factor` – Wie stark Vertices seitlich in Richtung des Pinsels gezogen werden. Wenn Pinch auf 1 und Offset auf 0 steht, ändert sich die Oberfläche nicht in der Tiefe, nur die Topologie, indem Kanten in Richtung des Strichs gezogen werden.
* `Offset factor` – Wie stark Vertices in der Tiefe gedrückt/gezogen werden. Wenn Pinch auf 0 und Offset auf 1 steht, werden tiefe Furchen oder erhabene Dellen erzeugt, die jedoch gezackt aussehen können, weil nicht genug Geometrie in Richtung der Falte gezogen wird, um die Seiten oder den Boden der Falte sauber zu definieren.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Kneifen {#pinch}
Dieses Werkzeug kann verwendet werden, um Kanten zu schärfen.

Der Sub-Modus ist `Invert` und spreizt Vertices auseinander.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Zuschneiden {#trim}
Das Trim-Werkzeug arbeitet, indem es ein Stück deines Meshes entfernt und Optionen bietet, wie die entstehende Lücke verarbeitet werden soll. Es verwendet die [Selection controls](#selection-controls), um den Trim-Bereich zu definieren.

::: tip
Da dieses Werkzeug von der Kamera aus projiziert, erhältst du eine Warnung, wenn sich die Kamera im Perspektivmodus befindet.

Im orthografischen Modus ist der Schnitt durch das Mesh parallel zur Ansicht, was in der Regel erwartet wird. Im Perspektivmodus sieht der Schnitt auf der dem Betrachter zugewandten Seite des Objekts anders aus als auf der abgewandten Seite.
:::

#### Zuschneide‑Einstellungen {#trim-settings}

* `Stroke painting` – Wenn Painting im Paint-Menü aktiviert ist, wird der gepatchte Bereich mit der aktuell ausgewählten Farbe gefüllt.
* `Boolean` – Füllt das Loch des Trims mit einem Quad-Polygonbereich. Der gefüllte Bereich ist flach.
* `Legacy` – Füllt das Loch des Trims mit einem triangulierten Bereich. Der gefüllte Bereich ist flach.
* `Fill` – Füllt das Loch mit einem triangulierten Bereich. Der gefüllte Bereich ist eine gekrümmte Oberfläche, ähnlich einem Seifenfilm.
* `None` – Füllt das Loch nicht.
* `Boolean Detail Shape` – Die ungefähre Größe der Quads und Dreiecke, die auf der Formseite des Trims verwendet werden.
* `Boolean Detail Hole` – Die ungefähre Größe der Dreiecke oder Polys, die auf dem gefüllten Loch des Trims verwendet werden. 
* `Legacy Detail` – Die ungefähre Größe der Dreiecke, die beim Trim verwendet werden.
* `Legacy Hole smoothing` – Wie stark die Dreiecke im gefüllten Bereich entspannt werden.
* `Legacy Threshold espilon` – Ein Wert, der angepasst werden kann, um den Legacy-Lochfüllalgorithmus zu verbessern.
* `Fill Detail` – Die ungefähre Größe der Dreiecke, die beim Trim verwendet werden.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Teilen {#split}
Ähnlich wie das [Trim](#trim)-Werkzeug, mit dem Unterschied, dass Trim die Auswahl verwirft, während Split die Auswahl als neues Objekt beibehält.

#### Teilungs‑Einstellungen {#split-settings}

* `Stroke painting` – Wenn Painting im Paint-Menü aktiviert ist, wird der gepatchte Bereich mit der aktuell ausgewählten Farbe gefüllt.
* `Boolean` – Füllt das Loch des Splits mit einem Quad-Polygonbereich. Die gefüllten Bereiche sind flach.
* `Legacy` – Füllt das Loch des Splits mit einem triangulierten Bereich. Die gefüllten Bereiche sind flach.
* `Fill` – Füllt die Löcher mit einem triangulierten Bereich. Die gefüllten Bereiche sind gekrümmte Oberflächen, ähnlich einem Seifenfilm.
* `None` – Füllt die Löcher nicht.
* `Boolean Detail Shape` – Die ungefähre Größe der Quads und Dreiecke, die auf der Formseite des Splits verwendet werden.
* `Boolean Detail Hole` – Die ungefähre Größe der Dreiecke oder Polys, die auf dem gefüllten Loch des Splits verwendet werden. 
* `Legacy Detail` – Die ungefähre Größe der Dreiecke, die beim Split verwendet werden.
* `Legacy Hole smoothing` – Wie stark die Dreiecke im gefüllten Bereich entspannt werden.
* `Legacy Threshold espilon` – Ein Wert, der angepasst werden kann, um den Legacy-Lochfüllalgorithmus zu verbessern.
* `Fill Detail` – Die ungefähre Größe der Dreiecke, die beim Split verwendet werden.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projizieren {#project}
Das Project-Werkzeug sieht aus wie das [Trim](#trim)-Werkzeug, löscht oder erzeugt jedoch keine Geometrie, sondern verschiebt nur Vertices, um der Auswahl zu entsprechen.

![](/videos/tool_project.mp4)

::: tip
Wenn du Project innerhalb einer Ebene verwendest, kannst du mit dem Ebenenregler zwischen der ursprünglichen und der projizierten Form überblenden.
:::

### ![](/icons/tool_layer.webp) Ebene {#layer}
Hebt die Oberfläche an, begrenzt jedoch die Höhe.

Wenn du den Stift unten hältst und weiter über einen Bereich malst, hebt Layer bis zu einer bestimmten Höhe an und geht nicht weiter, im Gegensatz zu anderen Werkzeugen, die die Höhe weiter akkumulieren.

Beachte, dass die Begrenzung standardmäßig nur pro Strich gilt! Wenn du einen neuen Strich beginnst, baut er von der neuen Oberflächenhöhe aus weiter auf.

Um eine konstante maximale Höhe über viele Striche hinweg festzulegen, verwende das Layer-Werkzeug mit Nomads [Layers](layers.md)-System.

Erstelle eine Ebene und verwende dieses Werkzeug. Die maximale Höhe wird nun von der Ebene festgelegt, sodass du viele Pinselstriche anwenden kannst und die Höhe immer gleich bleibt.

`Sub` verwendet eine Mindesttiefe und erzeugt Rillen.

#### Ebenen‑Einstellungen {#layer-settings}

* `Use layer data` – Wenn aktiv und eine Ebene ausgewählt ist, werden die Ebenendaten verwendet, um die maximale Höhe festzulegen.
* `Inflate` – Wenn aktiv, wird die Richtung, in der Layer arbeitet, angepasst, um glattere Ergebnisse zu erzielen.
* `Relax (Normal)` – Die Menge der auf die Normalen angewendeten Glättung.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Aufblasen {#inflate}
Verschiebt die Vertices entlang ihrer eigenen Normalen. `Sub` verschiebt Vertices entlang ihrer invertierten Normalen.

#### Aufblas‑Einstellungen {#inflate-setings}
* `Relax (Normal)` – Die Menge der auf die Normalen angewendeten Glättung.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Schieben {#nudge}
Verschiebt oder „verschmiert“ Punkte in Richtung des Strichs.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stempel {#stamp}

Klicke und ziehe, um einen Bereich der Skulptur in Form des ausgewählten Alphas anzuheben.

Dies ist einfach das [Brush-Werkzeug](#brush) mit einem Stroke-Typ, der auf `Lock + radius` gesetzt ist. 

`Sub` drückt den Stempel hinein, anstatt ihn aus der Oberfläche herauszuziehen.

::: tip
Stamp funktioniert in der Regel am besten mit hochauflösender Geometrie. Wenn du online nach „wrinkles alpha“, „pores alpha“, „scales alpha“ usw. suchst, können diese Alpha-Texturen zusammen mit Stamp eine großartige Möglichkeit sein, organische Details zu einer Charakterskulptur hinzuzufügen.

Die beiden Stroke-Modi sind für unterschiedliche Dinge nützlich. 

* `Lock + radius` hat eine feste *Höhe*, das Ziehen passt die Breite und Rotation des Stempels an. Gut für Hauttexturen, bei denen sie dieselbe Tiefe/Höhe haben sollen, aber unterschiedliche Rotationen und Maßstäbe, um Wiederholungsmuster zu verbergen.
* `Lock + intensity` hat eine feste *Breite*, das Ziehen passt die Rotation und Höhe des Stempels an. Gut für Nieten, die alle dieselbe Größe, aber unterschiedliche Rotationen und Höhen haben sollen. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Ebene löschen {#delete-layer}
Dieses Werkzeug kann Ebenen lokal zurücksetzen; du benötigst eine aktive Ebene, sonst passiert nichts.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Röhre {#tube}
Erstellt eine Röhre, indem du eine Kurve zeichnest. 
![](/images/tool_tube_new.webp)

Sobald die Röhre erstellt ist, kann der Pfad im 3D-Raum mit ähnlichen Steuerungen wie bei den Standardwerkzeugen [Shape editing](#shape-editing) und Kurvenbearbeitung bearbeitet werden. 

![](/videos/tool_tube.mp4)

#### Röhre linke Werkzeugleiste {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Die linke Werkzeugleiste hat folgende Optionen:

* `Sync` – Wenn die aktuelle Röhre instanziert ist und es Kindknoten der Röhre gibt, die sich zwischen den Instanzen unterscheiden, werden diese damit neu synchronisiert.
* `Snap` – Wenn aktiv, werden die Curve- und Path-Modi beim Zeichnen auf andere Objekte einrasten. Wenn inaktiv, rastet der erste Punkt ein, dann wird der Rest der Röhre in dieser Tiefe gezeichnet. Es gibt ein kleines Flyout-Menü:
    * `Offset` – Legt die Tiefe des Snap fest; 0 % lässt die Mitte des Röhrenquerschnitts auf der Oberfläche einrasten, positive Werte heben sie von der Oberfläche ab, negative Werte senken sie ab.
* `Curve` – Zeichne eine Röhre freihändig. Es gibt ein kleines Flyout-Menü:
    * `Auto-validate` – Erstellt die Röhre, sobald der Strich abgeschlossen ist. Wenn deaktiviert, ist neben dem Kurvenpfad ein grüner Validierungskreis sichtbar; drücke ihn zum Validieren oder verwende den `Reset`-Link, der in diesem Menü erscheint, um den Pfad zu entfernen.
    * `Closed` – Macht die Röhre zu einer Schleife.
    * `Screen` – Nur verfügbar, wenn Auto-validate deaktiviert ist. Wenn aktiv, ist der Pfad an den Bildschirm „gepinnt“, sodass du Ansicht und Objekt bewegen kannst, während der Pfad an Ort und Stelle bleibt. Wenn inaktiv, ist der Pfad Teil der 3D-Szene und bewegt sich mit Kamera und Objekten.
    * `Accuracy` – Wie viele Kurvenpunkte verwendet werden, um den gezeichneten Pfad in eine Röhre umzuwandeln. 0 % verwendet die geringste Anzahl an Punkten, verpasst aber kleine Krümmungsänderungen. 100 % ist sehr genau und verwendet viele Punkte.
* `Path` – Erstelle eine Röhre, indem du durch Klicken Kurvenpunkte definierst. Tippe auf den grünen Kreis, um den Pfad zu validieren. Es gibt ein kleines Flyout-Menü:
    * `B-spline` – Eine alternative Kurvenzeichnungsmethode, bei der Kurvenpunkte in der Regel nicht direkt auf der Kurve liegen, aber glattere Ergebnisse als die Standardmethode liefern können.
    * `Closed` – Macht die Röhre zu einer Schleife.
    * `Screen` – Wenn aktiv, ist der Pfad an den Bildschirm „gepinnt“, sodass du Ansicht und Objekt bewegen kannst, während der Pfad an Ort und Stelle bleibt. Wenn inaktiv, ist der Pfad Teil der 3D-Szene und bewegt sich mit Kamera und Objekten.

##### Röhre obere Werkzeugleiste {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Wenn eine Röhre ausgewählt ist, erscheint oben im Viewport eine Werkzeugleiste mit zusätzlichen Steuerungen. Klicke auf den Titel der Werkzeugleiste, um sie ein- oder auszuklappen, und klicke auf den Pfeil oben rechts, um die Werkzeugleiste an den oberen oder unteren Rand des Viewports zu verschieben.

* `Validate` – Bäckt die Röhre in reguläre Polygone, sodass sie modelliert werden kann.
* `Edit` – Zeigt die Kurvenpunkte an, damit sie bearbeitet werden können.
* `Mirror` – Fügt einen Mirror-Repeater als Eltern dieser Kurve hinzu.
* `Snap` – Lässt Kurvenpunkte auf nahegelegene Oberflächen einrasten.
* `Closed` – Verbindet Anfang und Ende der Kurve zu einer Schleife.
* `B-spline` – Umschalten zwischen Catmull-Rom- und B-Spline-Interpolation.
* `Cap` – Wechselt zwischen Kappen an beiden Enden der Röhre, nur am Anfang oder Ende oder ohne Kappen.
* `Hole` – Fügt der Röhre Dicke hinzu und macht daraus ein Rohr. Wechselt zwischen einem Loch an beiden Enden, nur am Ende oder ohne Löcher. 
* `Radius` – Wechselt zwischen einem einheitlichen Radius, einem Radius am Anfang und Ende oder einem Radius pro Kurvenpunkt. Diese werden mit orangefarbenen Griffen an der Kurve bearbeitet.
* `Twist` – Wechselt zwischen keinem Twist, einem einheitlichen Twist, einem Twist am Anfang und Ende oder einem Twist pro Kurvenpunkt. Diese werden mit pinken Griffen an der Kurve bearbeitet.
* `Profile` – Wechselt zwischen keinem Profil (also einem Kreisprofil), einem einheitlichen Profil, einem Profil am Anfang und Ende oder einem Profil pro Punkt.
* `Profile edit` – Zeigt einen Profil-Editor an. Dieser funktioniert ähnlich wie die [Shape editing](#shape-editing)-Werkzeuge, kann Profil-Presets speichern und laden und hat einen Schalter, mit dem du das Profil im 3D-Raum bearbeiten kannst.
* `Spiral` – Blendet ein Menü ein, um der Röhre einen Spiral-Twist hinzuzufügen. Dieses Menü hat Optionen für `Twist Angle`, `Offset`, `Scale` und `Angle offset`.
* `X Divisions` – Die Anzahl der Unterteilungen um die Röhre herum; 4 Unterteilungen erzeugen z. B. eine quadratische Röhre. 
* `Constant density` – Wenn aktiv, bleiben die Polygone quadratisch. Wenn deaktiviert, kannst du `Y divisions` entlang der Länge der Röhre einstellen.
* `...` – Tube-Einstellungsmenü.

#### Kurvenpunkt‑Löschen‑Umschalter {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Unter der Werkzeugleiste befindet sich ein Kurvenpunkt-Löschschalter. Wenn du einen Kurvenpunkt in die Nähe eines anderen ziehst, wird er rot, was anzeigt, dass der Punkt gelöscht wird, wenn du loslässt. Wenn du kleine Bearbeitungen vornimmst und keine Punkte löschen möchtest, deaktiviert diese Schaltfläche das Löschverhalten für Punkte.



#### Röhren‑Einstellungen {#tube-settings}
* `Primitive` – Schaltflächen, mit denen du UVs aktivieren/deaktivieren oder die Röhre validieren kannst.
* `Post subdivision` – Ein Shortcut, um das Multiresolution-Level vor dem Validieren festzulegen.
* `Linear subdivision` – Shortcut, um das lineare Unterteilungslevel vor dem Validieren festzulegen. 
* `Division X` – Dasselbe wie X Divisions in der Werkzeugleiste.
* `Division Y` – Dasselbe wie Y Divisions in der Werkzeugleiste.
* `Curve (Repeater)` – Konvertiert die Röhre in einen [Curve Repeater](scene.md#curve).

::: tip
Divisions auf 4 und Post subdivision auf 3 erzeugen glatte, rund zulaufende Röhren – gut für Würmer, Schlangen, Körperteile.
:::


### ![](/icons/tool_lathe.webp) Drechseln {#lathe}
Erstellt eine Rotationsfläche, indem du eine Kurve zeichnest.

Dieses Werkzeug ist ideal für Formen wie Vasen oder Weingläser.

![](/videos/tool_lathe.mp4)

#### Drechseln linke Werkzeugleiste {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Die linke Werkzeugleiste hat folgende Optionen:

* `Sync` – Wenn das aktuelle Lathe instanziert ist und es Kindknoten des Lathes gibt, die sich zwischen den Instanzen unterscheiden, werden diese damit neu synchronisiert.
* `Fixed` – Wenn aktiviert, ist das Zentrum des Lathes fixiert und auf dem Bildschirm sichtbar. Diese Mittellinie hat Bearbeitungspunkte, die angepasst werden können. Wenn deaktiviert, aktualisiert sich das Zentrum des Lathes dynamisch, um zum Anfang und Ende der gezeichneten Kurve zu passen.
* `Curve` – Zeichne das Lathe-Profil in einem Strich. Es gibt ein kleines Flyout-Menü:
    * `Auto-validate` – Wenn aktiviert, wird das Lathe erstellt, sobald der Stift vom Bildschirm genommen wird. Wenn deaktiviert, kann ein grüner Kreis neben der Kurve gedrückt werden, um das Lathe zu erstellen. Die Kurve kann mit der Schaltfläche `Reset` gelöscht werden.
    * `Closed` – Verbindet Anfang und Ende der Kurve zu einer Schleife.
    * `Screen` – Nur verfügbar, wenn Auto-validate deaktiviert ist. Wenn aktiv, ist der Pfad an den Bildschirm „gepinnt“, sodass du Ansicht und Objekt bewegen kannst, während der Pfad an Ort und Stelle bleibt. Wenn inaktiv, ist der Pfad Teil der 3D-Szene und bewegt sich mit Kamera und Objekten.
    * `Accuracy` – Wie viele Kurvenpunkte verwendet werden, um den gezeichneten Pfad in eine Röhre umzuwandeln. 0 % verwendet die geringste Anzahl an Punkten, verpasst aber kleine Krümmungsänderungen. 100 % ist sehr genau und verwendet viele Punkte.
* `Path` – Erstelle ein Lathe, indem du durch Klicken Kurvenpunkte definierst. Tippe auf den grünen Kreis, um den Pfad zu validieren. Es gibt ein kleines Flyout-Menü:
    * `B-spline` – Eine alternative Kurvenzeichnungsmethode, bei der Kurvenpunkte in der Regel nicht direkt auf der Kurve liegen, aber glattere Ergebnisse als die Standardmethode liefern können.
    * `Closed` – Macht die Röhre zu einer Schleife.
    * `Screen` – Wenn aktiv, ist der Pfad an den Bildschirm „gepinnt“, sodass du Ansicht und Objekt bewegen kannst, während der Pfad an Ort und Stelle bleibt. Wenn inaktiv, ist der Pfad Teil der 3D-Szene und bewegt sich mit Kamera und Objekten.

#### Drechseln obere Werkzeugleiste {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Wenn ein Lathe ausgewählt ist, erscheint oben im Viewport eine Werkzeugleiste mit zusätzlichen Steuerungen. Klicke auf den Titel der Werkzeugleiste, um sie ein- oder auszuklappen, und klicke auf den Pfeil oben rechts, um die Werkzeugleiste an den oberen oder unteren Rand des Viewports zu verschieben.

* `Validate` – Bäckt das Lathe in reguläre Polygone, sodass es modelliert werden kann.
* `Edit` – Zeigt die Kurvenpunkte an, damit sie bearbeitet werden können.
* `Mirror` – Fügt einen Mirror-Repeater als Eltern dieses Lathes hinzu.
* `Snap` – Lässt Kurvenpunkte auf nahegelegene Oberflächen einrasten.
* `Stable` – Wenn aktiviert, wird das Kurvenprofil an der Mittellinie des Lathes verankert. Wenn deaktiviert, kann die Mittellinie bearbeitet werden, ohne die Kurve zu bewegen, was komplexere Formen ermöglicht.
* `Focus` – Dreht die Ansicht so, dass das Kurvenprofil perfekt flach zur Kamera sichtbar ist.
* `Closed` – Verbindet Anfang und Ende der Kurve zu einer Schleife.
* `Cap` – Wenn Closed deaktiviert ist, wechselt zwischen Kappen an beiden Enden der Röhre, nur am Anfang oder Ende oder ohne Kappen.
* `Hole` – Fügt dem Lathe Dicke hinzu und macht daraus ein Rohr. Wechselt zwischen einem Loch an beiden Enden, nur am Ende oder ohne Löcher. 
* `B-spline` – Umschalten zwischen Catmull-Rom- und B-Spline-Interpolation.
* `X Divisions` – Die Anzahl der Unterteilungen um das Lathe herum; 4 Unterteilungen erzeugen z. B. ein Lathe mit quadratischem Profil. 
* `Constant density` – Wenn aktiv, bleiben die Polygone quadratisch. Wenn deaktiviert, kannst du `Y divisions` entlang der Länge der Röhre einstellen.
* `...` – Lathe-Einstellungsmenü.

#### Drechsel‑Einstellungen {#lathe-settings}
* `Primitive` – Schaltflächen, mit denen du UVs aktivieren/deaktivieren oder das Lathe validieren kannst.
* `Post subdivision` – Ein Shortcut, um das Multiresolution-Level vor dem Validieren festzulegen.
* `Linear subdivision` – Shortcut, um das lineare Unterteilungslevel vor dem Validieren festzulegen. 
* `Division X` – Dasselbe wie X Divisions in der Werkzeugleiste.
* `Division Y` – Dasselbe wie Y Divisions in der Werkzeugleiste.
* `Curve (Repeater)` – Konvertiert das Kurvenprofil in einen [Curve Repeater](scene.md#curve).

### ![](/icons/tool_insert.webp) Einfügen {#insert}
Platziert ein Objekt auf der Oberfläche eines anderen. In der Anwendung ähnelt es dem Stamp-Werkzeug, jedoch für vollständige 3D-Formen.

Wenn du ein Primitive aus der linken Werkzeugleiste auswählst, platziert ein Klick-Ziehen auf eine beliebige Oberfläche ein Primitive an der Klickposition; das Ziehen legt die Größe fest. Sobald du das Ziehen beendest, wechselt Insert in den [Transform](#transform)-Modus.

Im Instance-Modus erzeugt das Ziehen eine neue Instanz und lässt sie über die Oberfläche gleiten. Die Größe wird vom ersten Objekt übernommen; auf diese Weise kannst du viele gleich große Instanzen eines Objekts über andere Oberflächen platzieren.

Du musst nicht nur Primitives einfügen! Wähle *beliebige* Form im Outliner; wenn Insert im Instance- oder Clone-Modus ist, kannst du Kopien des ausgewählten Objekts über beliebige andere Oberflächen ziehen.

Wenn ein Objekt einen benutzerdefinierten Pivot hat, wird dieser als Ankerpunkt verwendet. Siehe Video unten.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformieren {#transform}
Bewegt/rotiert/skaliert ein Modell direkt mit einem oder zwei Fingern, normalerweise über die Oberfläche eines anderen Objekts.

Das Werkzeug wird über die linke Werkzeugleiste gesteuert und hat 5 Schaltflächen:

* `Snap` – Lässt das Modell auf andere Oberflächen einrasten.
* `Group` – Wenn das ausgewählte Objekt eine Kombination aus Objekten und Instanzen hat, kannst du hier das Verhalten des Werkzeugs festlegen.
* `Move` – Ein Ein-Finger-Ziehen bewegt das Objekt. Wenn Snap aktiv ist, gleitet das Objekt entlang der Oberfläche unter deinem Finger.
* `Rotate` – Ein Ein-Finger-Ziehen rotiert das Objekt. Wenn Snap aktiv ist, rotiert es um die Normale der Oberfläche unter deinem Finger.
* `Scale` – Ein Ein-Finger-Ziehen skaliert das Objekt.

Transform kann zwei dieser Modi schnell mit zwei Fingern verwenden:

* Ziehe ein Objekt, um es zu platzieren. Bewege deinen ersten Finger nicht mehr, lasse ihn aber auf dem Bildschirm.
* Berühre mit deinem zweiten Finger den Bildschirm, während der erste Finger unten bleibt. Wenn du den zweiten Finger ziehst, wird das Objekt skaliert.
* Hebe den zweiten Finger an und ziehe den ersten Finger weiter; das Objekt befindet sich wieder im Move-Modus.

Du kannst den zweiten Modus auch mit einer Tippgeste des zweiten Fingers ändern:

* Ziehe das Objekt, um es zu platzieren, halte an, aber hebe deinen Finger nicht an.
* Tippe mit deinem zweiten Finger, während du den ersten Finger gedrückt hältst.
* Das Werkzeug wechselt in den Rotationsmodus. Ziehe mit deinem ersten Finger, um die Rotation festzulegen.
* Tippe erneut mit dem zweiten Finger; das Werkzeug wechselt zurück in den Move-Modus.

Dies ermöglicht einen schnellen Workflow zum Klonen von Objekten über ein anderes, z. B. Felsen über eine Landschaft. Beachte, dass die Clone-Schaltfläche ebenfalls in der linken Werkzeugleiste für einfachen Zugriff vorhanden ist:

* Verwende das Transform-Werkzeug, um einen Felsen zu platzieren.
* Lass los, drücke die Clone-Schaltfläche.
* Bewege diesen Felsen, rotiere/skaliere nach Bedarf.
* Lass los, drücke die Clone-Schaltfläche.
* Bewege diesen Felsen, wiederhole.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Dieses Werkzeug ermöglicht es dir, Objekte zu bewegen, zu rotieren und zu skalieren sowie deren Pivot zu verändern.

Das Viewport-Handle hat folgende Funktionen:

* `Move` – Ziehe an der Linie mit Pfeil, um auf X/Y/Z zu bewegen. Ziehe am pfirsichfarbenen Punkt in der Mitte des Gizmos, um frei im Bildschirmraum zu verschieben. Klicke auf die roten, grünen, blauen Quadrate, um in den X/Y/Z-Ebenen zu verschieben.
* `Rotate` – Ziehe an den roten/grünen/blauen Kreisen, um um X/Y/Z zu rotieren. Ziehe an der Kugel innerhalb der Kreise, um frei zu rotieren.
* `Scale` – Ziehe an den äußeren roten/grünen/blauen Punkten, um auf X/Y/Z zu skalieren. Ziehe an den äußeren roten/grünen/blauen Kegeln, um in den X/Y/Z-Ebenen zu skalieren. Ziehe am äußeren pfirsichfarbenen Kreis, um gleichmäßig zu skalieren.

![](/images/tool_gizmo.webp)

#### Knoten und Vertices {#nodes-and-vertices}

Jedes Objekt in Nomad besteht aus einem Node und Vertices:

* `Node` – Der „Griff“ des Objekts, der seine Translation, Rotation und Skalierung speichert, die sogenannte Transformationsmatrix.
* `Vertices` – Die Punkte, die die Oberfläche eines Objekts definieren; sie speichern Positions- und Farbinformationen.

Wenn du eine einfache Box aus 8 Vertices hast, könntest du sie verschieben, indem du ihre Transformationsmatrix änderst oder indem du die Vertex-Positionen änderst. Beim Sculpting möchtest du normalerweise die Vertices ändern, beim Bewegen von Objekten mit dem Gizmo normalerweise den Node. Nomad erlaubt beides. 

#### Linke Menü‑Werkzeugleiste {#left-menu-toolbar}

Die linke Werkzeugleiste steuert, ob das Gizmo auf den Node oder die Vertices eines Objekts wirkt, sowie andere Funktionen:

* `Clone` – Erstellt eine eigenständige Kopie des aktuellen Objekts, die mit dem Gizmo weggezogen werden kann.
* `Instance` – Erstellt eine Instanzkopie des aktuellen Objekts. Die Objekte sind verknüpft, sodass Sculpting-Änderungen an einem Objekt bei allen Instanzen erscheinen.
* `Group/Object/Vertex/Auto` – Legt fest, ob das Gizmo den Node oder die Vertices eines Objekts beeinflusst. Der Standardmodus „Auto“ versucht eine sinnvolle Schätzung. Wenn mehrere Objekte in einer Hierarchie miteinander verknüpft sind, bewegt „Object“ nur das aktuelle Objekt, Kindobjekte bleiben stationär. Das Gizmo kann auch Maskierung und Symmetrie berücksichtigen.
* `Pin` – Standardmäßig bewegt sich das Gizmo zum Pivot des ausgewählten Objekts. Wenn Pin aktiviert ist, bleibt das Gizmo an seiner aktuellen Position.
* `Align` – Schaltet um, ob der Pivot am aktuellen Objekt oder an der Welt ausgerichtet ist.
* `Snap rotation` – Aktiviert das Einrasten von Rotationswerten in Inkrementen; der Snap-Wert wird angezeigt und kann bei aktivem Snap bearbeitet werden.
* `Snap translation` – Aktiviert das Einrasten von Translationswerten in Inkrementen; der Snap-Wert wird angezeigt und kann bei aktivem Snap bearbeitet werden.
* `Pivot` – Wenn aktiviert, kann das Gizmo bewegt und rotiert werden, ohne das Objekt zu bewegen. Es hat ein zusätzliches Menü, das unten erklärt wird.

#### Pivot {#pivot}
Wenn der Pivot-Modus aktiv ist, wird ein Menü angezeigt, um schnelle Pivot-Änderungen zu ermöglichen:

**Reset** 
* `Center` – Verschiebt den Pivot in die Mitte des Objekts.
* `Bottom` – Verschiebt den Pivot an die Unterseite des Objekts.
* `Align` – Setzt die Rotationen zurück, sodass sie an der Welt ausgerichtet sind.
* `Mask` – Verschiebt den Pivot in die Mitte des unmaskierten Bereichs.

**On Tap**
* `None` – Beim Antippen des Objekts passiert nichts.
* `Normal` – Verschiebt und rotiert den Pivot, um sich an der angetippten Oberfläche auszurichten.
* `First` – Verschiebt (aber rotiert nicht) den Pivot an die angetippte Stelle auf der Oberfläche.
* `Medial` – Verschiebt den Pivot in die Mitte des Objekts unterhalb der angetippten Oberfläche.

#### Gizmo‑Einstellungen {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Matrix {#matrix}
* ![](/icons/target.webp) `Move origin` – Verschiebt das Objekt so, dass sich sein Pivot im Zentrum der Szene (Origin) befindet.
* ![](/icons/bake.webp)  `Bake` – Friert das Objekt an seiner aktuellen Position ein und setzt die Translate-/Rotate-Werte auf 0, Scale auf 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` – Lässt die Matrixwerte der Position des Gizmo-Handles in der Welt entsprechen.
* ![](/icons/reset.webp) `Reset` – Ein Shortcut, der die Translate-Werte auf 0, die Rotate-Werte auf 0 und Scale auf 1 setzt und das Objekt entsprechend verschiebt und rotiert.

::: tip Bake vs Bake to Pivot
Erstelle eine Box, wähle das Gizmo-Werkzeug, öffne und pinne das Einstellungsmenü. Standardmäßig sind Translation und Rotation 0, Scale ist 1.

Aktiviere den Pivot-Modus, verschiebe das Handle auf eine Seite, deaktiviere den Pivot-Modus. Der Pivot hat sich geändert, aber beachte, dass die Translate-Werte immer noch 0 sind. 

Wenn du sehen möchtest, wo der Pivot *wirklich* ist, klicke auf `Bake Pivot`. Jetzt aktualisieren sich die Translate-Werte. Beachte, dass sich die Box während dieser Operation nicht bewegt, ebenso wenig im Pivot-Modus.

Bewege und rotiere die Box irgendwohin und tippe dann auf `Move Origin`. Das Objekt wird so verschoben, dass sich sein Pivot im Zentrum der Welt befindet, die Rotation bleibt jedoch unverändert.

Klicke auf `Reset`, und die Rotation wird ebenfalls auf 0 gesetzt.

Bewege und rotiere die Box erneut, klicke diesmal auf `Bake`. Der Pivot bleibt, wo er ist, die Box bleibt, wo sie ist, aber die Translate- und Rotate-Werte werden auf 0 gesetzt.

Übe dies ein paar Mal! Verstehe, dass die Pivot-Werte verborgen sind – Nomad kümmert sich darum –, aber wenn du den Pivot auf reale Positionen im Raum setzen musst, erledigt Bake Pivot das für dich.

:::

* `Translation` – Die Translate-Werte X, Y, Z.
* `Rotation` – Die Rotate-Werte X, Y, Z.
* `Scale` – Die einheitliche Skalierung, falls aktiviert, oder die Scale-Werte X, Y, Z, falls deaktiviert.
* `Uniform scale` – Schaltet die Möglichkeit um, einheitlich oder unabhängig auf jeder Achse zu skalieren.

-----

* `Compact` – Schaltet das Gizmo-Layout um, sodass die zusätzlichen Griffe außerhalb oder innerhalb der Rotationskugel liegen.
* `Widget size` – Die Größe des Gizmos.
* `Thickness` – Die Linienstärke des Gizmos.
* `Opacity` – Die Deckkraft des Gizmos.
* `Hide on interaction` – Schaltet um, ob das Gizmo beim Ziehen vorübergehend ausgeblendet wird.

-----

* `Tangent roll threshold` – Steuert, wie sich die Rotations-UI verhält, wenn du an den Kreishandles ziehst, um um X/Y/Z zu rotieren. Wenn dieser Wert 0 ist, funktioniert das Rotieren wie ein Drehknopf – ziehe das Gizmo im Kreis. Wenn dieser Wert 90 ist, funktioniert das Rotieren wie das Ziehen an einer Jo-Jo-Schnur – ziehe in einer geraden Linie auf den Punkt zu oder von ihm weg, an dem du zuerst geklickt hast. Werte zwischen 0 und 90 bewirken eine Kombination aus beidem; unterhalb des Werts ist die Bewegung linear, oberhalb ist sie kreisförmig.
* `Numerical input` – Wenn aktiviert, öffnet ein einfacher Tipp auf das Gizmo ein Fenster, um einen exakten Wert für die angetippte Widget-Achse einzugeben.

::: warning
Das [Gizmo](#gizmo) sowie [Translate](#translate), [Rotate](#rotate) und [Scale](#scale) verwenden ihre eigene Symmetrie-Checkbox!

Standardmäßig ist diese Symmetrie deaktiviert.
:::

Links kannst du den Gizmo-Pivot verschieben; im folgenden Video siehst du dies in Aktion.
Dies ist besonders nützlich für die Rotation, da es die Translation nicht verändert.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Flächengruppe {#facegroup}

Facegroups ermöglichen es dir, dein Objekt in unterschiedlich gefärbte Flächen zu organisieren. Du kannst diese Gruppen in Nomad auf viele Arten verwenden:

* Schnellauswahlmethode für Masken
* Teile deines Objekts aus- oder einblenden
* Dein Objekt organisieren, ohne es in separate Teile aufteilen zu müssen
* UV-Bereiche definieren
* Den Quad Remesher steuern
* Zusätzliche Kontrolle für Werkzeuge wie Smooth

#### Flächengruppe linke Werkzeugleiste {#facegroup-left-toolbar}

* `Patch ` – Zeigt die verfügbaren Facegroups als Patches an. Nicht verwendete Patches können gelöscht werden. Tippe auf einen Patch, um ihn umzubenennen oder seine Farbe zu ändern. Mit dem Plus-Symbol kannst du neue Patches erstellen.
* `Dot` – Male auf dem Objekt, um Facegroups zu definieren. Wenn „+ Face Group“ aktiviert ist, erstellt jeder neue Strich automatisch eine neue Facegroup – nützlich, um schnell Bereiche zu definieren. Ein Tipp füllt die ausgewählte Region vollständig. Der Schieberegler legt den Radius des Punkts fest.
* `Relax` – Glättet die Ränder von Facegroups. Sehr nützlich, um saubere Kanten für Quad-Remeshing zu definieren oder Paneele für Hard-Surface-Modelling zu erstellen. Die Schieberegler steuern Radius und Intensität der Relax-Operation.
* `Shape selector` – Erstellt Facegroups mit Formen statt mit einem Pinsel, über `Lock+Radius`, `Lasso`, `Polygon`, `Rect` und `Ellipse`. Siehe [Shape Selector](#shape-selector) für weitere Informationen.
* `Auto-pick` – Wenn aktiviert, wird der Patch ausgewählt, auf dem der Strich beginnt, und dieser Patch für den Rest des Strichs angewendet. Sehr nützlich, um Facegroup-Bereiche aufzuräumen; wenn eine Facegroup zu weit ausgedehnt ist, aktiviere Auto-pick, beginne einen Strich dort, wo der Facegroup-Patch korrekt ist, und ziehe bis zum Rand, um den korrekten Patch neu zuzuweisen.

### ![](/icons/tool_hide.webp) Verbergen {#hide}
Blendet Teile des Objekts aus oder isoliert sie. 

Die Hauptmodi werden über das linke Menü gesteuert:

* `Dot` – Male mit einem Pinsel auf dem Objekt, um Teile des Objekts auszublenden.
* `Shape selector` – Blendet mit Formen statt mit einem Pinsel aus, über `Lasso`, `Polygon`, `Line`, `Rect` und `Ellipse`. Siehe [Shape Selector](#shape-selector) für weitere Informationen.
* `Show` – Kehrt die Operation um, sodass der ausgewählte Modus Teile des Objekts einblendet statt ausblendet.

Oben im Viewport erscheint eine Werkzeugleiste mit zusätzlichen Steuerungen:

* `Clear` – Stellt das Objekt wieder her; alle ausgeblendeten Teile werden eingeblendet.
* `Invert` – Tauscht die ausgeblendeten und eingeblendeten Teile.
* `Facegroup` – Verwendet Facegroups, um Bereiche schnell auszublenden; Tippen auf eine Facegroup blendet die gesamte Facegroup aus.
* `Mask` – Wenn eine Maske aktiv ist, blendet das Tippen auf diese Schaltfläche den maskierten Bereich aus.
* `Delete` – Löscht den ausgeblendeten Teil des Objekts.
* `Split` – Teilt den ausgeblendeten Teil des Objekts in eine neue Form auf.

### ![](/icons/tool_measure.webp) Messen {#measure}
Ziehen, um den Abstand zwischen zwei Punkten zu messen.

### ![](/icons/tool_remesh.webp) Quad‑Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Dieses Werkzeug konvertiert das ausgewählte Objekt in eine saubere Quad-Topologie mit Steuerungen für Dichte, Kantenfluss und Symmetrie. 

::: tip
Quad Remesher wird von [Exoside](https://exoside.com/) für iOS und Desktop entwickelt. 

Für iOS ist es ein In-App-Kauf innerhalb von Nomad, eine einmalige Zahlung von 16 USD.

Für Desktop erwirbst du eine Lizenz bei [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Du kannst es nur für Nomad Desktop oder als Cross-Lizenz für alle unterstützten Desktop-Apps kaufen.

Wenn du Quad Remesher bereits für eine andere Desktop-App besitzt, kannst du [ein Upgrade auf alle Plattformen zu geringeren Kosten erwerben.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher ist nicht für Android verfügbar. Android kann das kostenlose Open-Source-Tool „Quad Remesh – Instant“ verwenden, das unter Topology -> Misc verfügbar ist, aber beachte, dass dessen Funktionsumfang sehr begrenzt ist.
:::

When dieses Werkzeug zum ersten Mal aktiviert wird, fragt es, ob du es als In‑App‑Kauf freischalten möchtest. Sobald es aktiv ist, werden die linke und obere Werkzeugleiste aktiviert.

* `Dot` - Dieser Pinsel legt die Zieldichte fest. Eine Intensität von 100 % malt in Rot, wodurch in diesen Bereichen die doppelte Ziel-Quad-Dichte verwendet wird. Eine Intensität von 0 % malt in Cyan, wodurch in diesen Bereichen die halbe Ziel-Quad-Dichte verwendet wird. Eine Intensität von 50 % malt in Grau, wodurch die standardmäßige Ziel-Quad-Dichte verwendet wird.
* `Smooth` - Glättet die Übergänge zwischen roter/grauer/cyanfarbener Dichte.
* `Curve` - Skizziere Kurven auf der Oberfläche der Skulptur, Quad Remesher verwendet diese als Leitlinien für den Kantenfluss. Tippe auf eine Kurve, um sie zu löschen.
* `Path` - Zeichne Pfade auf der Oberfläche der Skulptur, Quad Remesher verwendet diese als Leitlinien für den Kantenfluss. Tippe auf einen Pfad, um ihn zu löschen. 
* `Rect` - Zeichne Rechtecke auf der Oberfläche der Skulptur, Quad Remesher verwendet diese als Leitlinien für den Kantenfluss. Tippe auf einen Pfad, um ihn zu löschen.
* `Ellipse` - Zeichne Ellipsen auf der Oberfläche der Skulptur, Quad Remesher verwendet diese als Leitlinien für den Kantenfluss. Tippe auf einen Pfad, um ihn zu löschen.

#### Quad‑Remesher obere Werkzeugleiste {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Am oberen Rand des Viewports erscheint eine Werkzeugleiste mit zusätzlichen Bedienelementen:


* `<Count>` - Klicke hier, um den Quad-Remesher-Prozess zu starten; diese Zahl gibt an, wie hoch die Zielanzahl der Quad-Remeshes sein wird.
* `Quads` - Lege die Ziel-Quad-Anzahl fest, indem du nach links und rechts schiebst oder tippst, um eine exakte Zahl einzugeben. Beachte, dass dies eher eine Richtlinie als eine feste Zahl ist; die verschiedenen Einstellungen des Quad Remeshers führen oft dazu, dass das Ergebnis nicht exakt diesem Ziel entspricht.
* `Half` - Eine Abkürzung, um die Zielanzahl auf die Hälfte der aktuellen Polygonanzahl zu setzen.
* `Same` - Eine Abkürzung, um die Zielanzahl auf die aktuelle Polygonanzahl zu setzen.
* `Guides` - Zeigt die Gesamtzahl der Guides an oder tippe, um alle Guides zu löschen.
* `Density X` - Tippe, um alle Dichte-Malereien zu entfernen.
* `Density (painting)` - Umschalten, um Dichte-Malerei zu verwenden oder zu ignorieren.
* `Face Group` - Umschalten, um Facegroups zu verwenden oder zu ignorieren, um den Quad Remesher zu steuern.
* `Relax` - Umschalten, um Facegroup-Grenzen während des Quad-Remeshings automatisch zu entspannen. Wenn du deine Facegroup-Grenzen bereits entspannt/geglättet hast, deaktiviere diese Option.
* `Relax Slider` - Ein Schnellzugriffsregler zum Entspannen der Facegroup-Grenzen.
* `Hard Edges` - Umschalten, um zu versuchen, harte Kanten beizubehalten.
* `Reproject Vertex` - Umschalten, um das neue Layout auf das Eingabemesh zu reprojizieren.
* `Symmetry` - Umschalten, um ein symmetrisches Ergebnis zu erhalten. Beachte, dass Symmetrie immer um die Welt‑X‑Achse berechnet wird; stelle also sicher, dass sich dein Modell im Ursprung befindet, wenn du ein symmetrisches Ergebnis erwartest.
* `...` - Quadremesher-Einstellungsmenü. 

#### Quad‑Remesher Einstellungsmenü {#quad-remesher-settings-menu}

Die meisten dieser Einstellungen sind in der oberen Werkzeugleiste verfügbar.

* `<Count>, Half, Same` - Entspricht den Schaltflächen Remesh, Half, Same in der oberen Werkzeugleiste.
* `Target Quads` - Entspricht der Schaltfläche `Quads` in der oberen Werkzeugleiste.
* `Adaptive quad count` - Umschalten, um kleinere Quads in Bereichen mit hoher Krümmung und größere Quads in Bereichen mit geringerer Krümmung zu verwenden.
* `Adaptive size` - Lege den Grad der Adaptivität fest. 100 % erlaubt maximale adaptive Größe, bei 0 % sind die Quads einheitlich.
* `Auto-Detect Hard Edges` - Umschalten, um das Quad-Remesh-Layout besser an scharfe Oberflächen anzupassen.
* `Density (painting)` - Entspricht der Schaltfläche `Density (painting)` in der oberen Werkzeugleiste.
* `Reproject Vertex` - Umschalten, um das neue Layout auf das Eingabemesh zu reprojizieren.
* `Face Group` - Entspricht der Schaltfläche `Face Group` in der oberen Werkzeugleiste.
* `Relax Slider` - Ein Schnellzugriffsregler zum Entspannen der Facegroup-Grenzen.

::: tip

Ein Rezept, um ein gutes Quad-Remesh mit minimalen Artefakten zu erhalten:

* Facegroup für das Mesh anlegen, um deinen idealen Quad-Fluss zu definieren.
* Facegroup-Relax, um glatte Facegroup-Grenzen zu erhalten.
* Decimate. Dies stellt sicher, dass du keine dünnen oder verzerrten Flächen an der Facegroup-Grenze hast. Stelle in den Decimate-Einstellungen sicher, dass Facegroup aktiviert ist. Dadurch folgen die Dreieckskanten deinen Facegroup-Kanten exakt. 

Stelle in den Quad-Remesh-Optionen sicher, dass Relax deaktiviert ist (da du das Mesh bereits entspannt hast), und du solltest gute Ergebnisse erhalten.

:::

### ![](/icons/tool_select.webp) Auswahl {#select}
Verwende die Formmodi, um Objekte in der Szene auszuwählen. `Unselect` entfernt Objekte aus der Auswahl.

### ![](/icons/tool_view.webp) Ansicht {#view}
Dieses „Werkzeug“ macht nichts Besonderes; es ist lediglich eine Möglichkeit, das Modell zu betrachten, ohne deine Szene zu verändern.


## Kontextmenü der Werkzeugleiste {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Ein Rechtsklick oder langes Drücken auf ein Werkzeug in der Toolbox öffnet ein Kontextmenü. Dieses Menü hat die folgenden Optionen:

* `Save` - Speichere alle Änderungen, die du an dem Werkzeug vorgenommen hast
* `Clone` - Dupliziere das Werkzeug in eine neue Werkzeugverknüpfung
* `Last save` - Zurückkehren zur zuletzt gespeicherten Version des Werkzeugs
* `Icon` - Ändere das Symbol für das Werkzeug
* `Reset` - Setze das Werkzeug auf seine Standardwerte zurück