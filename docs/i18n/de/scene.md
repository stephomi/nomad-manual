# ![](/icons/scene.webp) Szene 

Dieses Menü ermöglicht es dir, Objekte, Lichter, Kameras und Repeater in Nomad zu verwalten. Es zeigt die Szenenhierarchie als Baumansicht an, sodass du viele Aspekte deiner Objekte ändern kannst. Außerdem kannst du neue Objekte erstellen sowie Objekte auf verschiedene Arten kombinieren und trennen.


![](/images/scene_menu_summary.webp)


## Shortcut-Leiste
| Aktion                | Icon                              | Beschreibung                                                                                                       |
| :-------------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| [Hinzufügen...](#add-menu) | ![](/icons/plus.webp)            | Zeigt das [Hinzufügen-Menü](#add-menu) an, um ein Objekt zur Szene hinzuzufügen                                    |
| Löschen               | ![](/icons/trash.webp)           | Löscht das Objekt                                                                                                  |
| Sperren               | ![](/icons/lock.webp)            | Macht das Objekt im Viewport nicht auswählbar. Es kann weiterhin in der Baumansicht ausgewählt werden.            |
| Verbinden             | ![](/icons/merge.webp)           | Verbindet die ausgewählten Objekte zu einem einzigen Objekt ohne Geometrieänderungen                              |
| Trennen               | ![](/icons/diagonal.webp)        | Wenn ein Objekt aus separaten Polygon-Schalen besteht, wird es in einzelne Objekte aufgeteilt. Umkehrung von Verbinden |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | Zeigt das [Boolean](#boolean)-Menü an                                                                             |
| Klonen                | ![](/icons/clone.webp)           | Dupliziert das Objekt als neues Objekt                                                                            |
| Instanz               | ![](/icons/link.webp)            | Dupliziert das Objekt als Instanz, sodass Modellieränderungen an einem auf alle Instanzen angewendet werden       |
| Instanz auflösen      | ![](/icons/unlink.webp)          | Wandelt eine Instanz in eine einzigartige Form um, sodass Modellieränderungen nicht mehr auf andere Instanzen kopiert werden |
| Sync                  | ![](/icons/link.webp)            | Wenn Instanzen Kinder haben, wird sichergestellt, dass alle Instanzen dieselbe Kind-Hierarchie teilen             |


## Baumansicht
![](/images/scene_treeview.webp) 

| Aktion       | Icon                       | Beschreibung           |
| :----------: | :------------------------: | :--------------------: |
| Auswählen    | ![](/icons/checked.webp)  | Auswahl umschalten     |
| Sichtbar     | ![](/icons/eye_open.webp) | Sichtbarkeit umschalten|
| Menü         | ![](/icons/more.webp)     | Objektmenü anzeigen    |

::: tip TIPP: Viele Objekte schnell auswählen oder ausblenden

Tippe auf das Auswahl-Icon, um ein einzelnes Objekt umzuschalten, oder ziehe vertikal in der Auswahlspalte, um viele Objekte auszuwählen. Dasselbe funktioniert mit der Sichtbarkeits-Spalte.

:::

### Manipulation der Baumansicht

Halte ein Element in der Baumansicht lange gedrückt, bis es gelb wird. Du kannst es dann in der Baumansicht nach oben oder unten verschieben oder über ein anderes Element ziehen, um es zu dessen Kind zu machen.

Wenn viele Elemente ausgewählt sind, sind die meisten dunkelgelb, eines ist heller gelb. Halte das hellere Element lange gedrückt und ziehe es, um alle Objekte auf einmal zu verschieben.

Wenn du ein Eltern-Element auswählst, werden standardmäßig alle Kind-Elemente ebenfalls ausgewählt. Durch Tippen auf das Eltern-Icon wird zwischen „nur Eltern“ und „Eltern + Kinder“ umgeschaltet.

### Objektmenü

Ein Klick auf die Auslassungspunkte (...) eines Objekts in der Baumansicht öffnet das Objektmenü.  
Viele dieser Optionen entsprechen der Shortcut-Leiste oben und werden der Bequemlichkeit halber wiederholt.

|       Aktion        |                        Icon                        | Beschreibung                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       Instanz       |               ![](/icons/link.webp)            | Dupliziert das Objekt als Instanz, sodass Modellieränderungen an einem auf alle Instanzen angewendet werden.                                                            |
|        Klonen       |              ![](/icons/clone.webp)            | Dupliziert das Objekt als neues Objekt                                                                                                                                  |
|        Name         |              ![](/icons/pencil.webp)           | Ändert den Namen des Objekts                                                                                                                                            |
|       Löschen       |              ![](/icons/trash.webp)            | Löscht das Objekt                                                                                                                                                       |
|      Löschen+       |            ![](/icons/removeNode.webp)         | Löscht das Objekt und seine Kinder                                                                                                                                      |
|   Instanz auflösen  |              ![](/icons/unlink.webp)           | Wandelt eine Instanz in eine einzigartige Form um, sodass Modellieränderungen nicht mehr auf andere Instanzen kopiert werden.                                          |
| Topologie trennen   |             ![](/icons/separate.webp)          | Wenn ein Objekt aus separaten Polygon-Schalen besteht, wird es in einzelne Objekte aufgeteilt. Umkehrung der Verbinden-Operation.                                      |
| Face Group trennen  |            ![](/icons/faceGroup.webp)          | Wenn ein Objekt mehrere Face Groups hat, wird das Mesh in separate Objekte aufgeteilt.                                                                                 |
|   Ebenen trennen    |              ![](/icons/layer.webp)            | Wenn ein Objekt Ebenen hat, wird jede Ebene in ein separates Objekt aufgeteilt. Nützlich, um Blendshapes in andere Anwendungen zu exportieren.                         |
|   Verbinden -> Ebenen   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Wenn mehrere Objekte ausgewählt sind und übereinstimmende Topologie haben, werden diese Objekte als Ebenen in das primäre Objekt gemergt (die anderen Objekte werden gelöscht). Ebenfalls nützlich für Blendshapes, die AUS anderen Anwendungen kommen.<br><br> Beachte, dass die Ebenen standardmäßig deaktiviert sind. Aktiviere sie, wenn du ihre Regler anpassen musst. |




### Mehrfachauswahl
Du kannst mehrere Objekte auswählen, um zwei Dinge zu erreichen:
- das Gizmo-Werkzeug verwenden, um mehrere Objekte gleichzeitig zu bewegen
- Objekte mit Verbinden- und Boolean-Operationen zusammenführen.

Das kannst du tun, indem du das Kontrollkästchen `Multiselection` aktivierst und dann auf das Objekt in der Liste klickst.

::: tip Schnelle Mehrfachauswahl
Du kannst auch im Viewport mehrfach auswählen, indem du die `Smooth`-Verknüpfung gedrückt hältst und auf ein anderes Mesh tippst.

Du kannst ein Objekt abwählen, indem du erneut darauf tippst (nur wenn deine Auswahl mehr als ein Objekt enthält).
:::

::: warning Eingeschränkte Gizmo-Funktion
Bei Verwendung der Mehrfachauswahl ignoriert das Gizmo-Werkzeug immer Maskierung.
Außerdem wird X/Y/Z-Skalierung entfernt.

Der Grund ist, dass Mehrfachauswahl nur Transformationen des gesamten Meshs erlaubt, nicht pro Vertex.
Dies könnte in Zukunft verbessert werden.
:::


## Verbinden
Diese Option erstellt aus mehreren ausgewählten Objekten einfach einen einzigen Objekteintrag.

Ein Beispiel dazu findest du im Video im Abschnitt [Trennen](#separate).

## Boolean
![](/images/scene_boolean_menu.webp) 
Kombiniert Objekte zu einer einzigen Oberfläche.

`Voxel merge` erhält das Volumen der Objekte und berechnet neue, gleichmäßig verteilte Polygone auf der Oberfläche. Aufgrund des Berechnungsschritts kann ein Voxel-Merge komplexe Geometrie verarbeiten, kann aber feine Details verlieren, wenn die Zielauflösung nicht hoch genug ist.

`Boolean` versucht, die Polygone in ihrem ursprünglichen Layout zu belassen und die Polygone dort zu vernähen, wo sich Objekte überlappen. Dies kann deutlich sauberere und schärfere Ergebnisse liefern als ein Voxel-Merge, erfordert jedoch „wasserdichte“ Meshes; es darf keine Löcher oder fehlerhaften Formen in den Objekten geben. Wenn dies fehlschlägt, funktioniert in der Regel ein Voxel-Merge.

### Boolean-Operationen
Sowohl Voxel Merge als auch Boolean verwenden die Objektsichtbarkeit zur Steuerung der Operation:

#### Vereinigung
Wenn beide Objekte sichtbar sind, wird eine Boolean-**Vereinigung** erstellt, die äußere Hülle der Objekte wird kombiniert, ohne innere Oberflächen. ![](/images/boolean_union.webp)

#### Subtraktion
Ein Objekt unsichtbar = Boolean-**Subtraktion**, das unsichtbare Objekt wird vom sichtbaren Objekt abgezogen. ![](/images/boolean_subtract.webp)

#### Schnittmenge
Beide Objekte unsichtbar = Boolean-**Schnittmenge**, es wird eine neue Form nur dort erstellt, wo sich die beiden Objekte überlappen. ![](/images/boolean_intersect.webp)


### Voxel Merge-Button
Durch Drücken dieses Buttons wird ein Voxel-Merge auf die ausgewählten Objekte ausgeführt. Bei einem einzelnen Objekt wird es in gleichmäßig verteilte Polygone retopologisiert, was nützlich ist, wenn ein Objekt gestreckte Polygone hat.

### Auflösung
Die Auflösung des voxelbasierten 3D-Rasters, das für die Berechnung verwendet wird. Wenn dieser Wert geändert wird, wird ein Schachbrettmuster über das Objekt gelegt, um die Polygongröße zu visualisieren.

### Multiresolution aufbauen
Erstellt Multiresolution-Stufen unterhalb deiner Zielauflösung. Wenn deine Auflösung also 400 ist und „Build multiresolution“ auf 3 steht, erhältst du ein neues Mesh mit z. B. 296.000 Polygonen, aber es gibt 3 niedrigere Subdiv-Stufen mit 74.000, 18.000, 4.000k.

### Scharfe Kanten beibehalten
Aktiviert das Snapping des Voxel-Meshs an Kanten. Funktioniert am besten bei einfachen Formen.

### Boolean-Button
Durch Drücken dieses Buttons wird eine polygonale Boolean-Operation mit der Manifold-Bibliothek von Emmett Lalish ausgeführt. 


## Trennen
Wenn du ein einzelnes Objekt hast, das aus mehreren nicht verbundenen Teilen besteht, kannst du dieses Objekt in mehrere Objekte aufteilen.  
Dies kann als das Gegenteil von [Simple Merging](#simple-merge) betrachtet werden.

![](/videos/merge_separate.mp4)


## Hinzufügen-Menü

![](/images/scene_addmenu_overview.webp)

Dieses Menü erstellt Primitives, Gruppen, Kameras, Repeater und Lichter.

Primitives sind grundlegende Formtypen, die über Parameter angepasst werden können. Sobald du das Primitive an deine Bedürfnisse angepasst hast, „validierst“ du es, wodurch diese Parameter in ein Polygon-Mesh umgewandelt werden, das skulptiert und bemalt werden kann. Ein Primitive kann nach der Validierung nicht mehr über seine Parameter angepasst werden.


![](/images/scene_addmenu_top.webp)

### Am Gizmo
Aktiviert das Platzieren des neuen Primitives an der Position der aktuell ausgewählten Form oder des Gizmos. Wenn deaktiviert, wird das Primitive im Zentrum der Szene platziert.

### Gizmo auswählen
Aktiviert das automatische Umschalten auf das Gizmo-Werkzeug, wenn ein neues Primitive erstellt wird. 

### Erweitert

Dieses Menü erlaubt dir, deine Präferenz festzulegen, wo neue Primitives, Gruppen und Repeater erstellt werden. Sie können auf dem ausgewählten Objekt, am Weltursprung oder an der Position des Gizmos erstellt werden.


### UVs
Aktiviert UVs auf Primitives. UVs (oft Texturkoordinaten genannt) sind zusätzliche Daten, die in 3D verwendet werden, um Texturen auf Oberflächen anzuwenden. Sie benötigen mehr Speicher, aber für die meisten Geräte sollte dies kein Problem sein, außer du arbeitest mit sehr hohen Polygonzahlen (z. B. 10 Millionen Polys oder mehr). 

### Primitives

| Primitive      | Icon                                      | Beschreibung                                                                                                      |
| :------------: | :---------------------------------------: | :--------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Ein einfacher Würfel, du kannst die Unterteilung in X, Y und Z steuern                                           |
| Sphere         | ![](/icons/circle.webp)                  | Der Einfachheit halber „Sphere“ genannt, tatsächlich aber ein unterteilter Würfel mit erzwungenem `Project on sphere` |
| Cylinder       | ![](/icons/cylinder.webp)                | Du kannst ein zentrales Loch für den Zylinder hinzufügen, z. B. um ein Rohr zu erstellen                         |
| Torus          | ![](/icons/torus.webp)                   | Der Torus ist ein guter Ausgangspunkt für Ringe                                                                  |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                                |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                                |
| UV-sphere      | ![](/icons/circle.webp)                  | Eine Sphere mit ungleichmäßiger Poly-Anordnung, siehe [Warnung unten](#uv-sphere)                                |
| Plane          | ![](/icons/rectangle.webp)               | Eine einfache Ebene, dies ist das einzige Primitive, das nicht geschlossen ist                                   |
| Tube           | ![](/icons/tool_tube.webp)               | siehe [Tube](tools#tube)                                                                                         |
| Lathe          | ![](/icons/tool_lathe.webp)              | siehe [Lathe](tools#lathe)                                                                                       |
| Triplanar      | ![](/icons/triplanar.webp)               | siehe [Triplanar](#triplanar)                                                                                    |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | siehe [Shadow Catcher](#shadow-catcher)                                                                          |
| Head           | ![](/icons/face.webp)                    | Ein einfacher Kopf mit einer Ebene zum Überblenden zwischen männlich/weiblich                                    |

::: tip
Falls du dich fragst, welches das Basismesh beim Start von Nomad ist: Es ist ebenfalls ein unterteilter Würfel.
Allerdings verwendet das Basismesh in Nomad kein `Project on sphere`, es ist also nicht perfekt rund.
:::

### Primitive-Werkzeugleiste

![](/images/scene_primitive_toolbar.gif)

Sobald ein Primitive erstellt wurde, erscheint eine Werkzeugleiste zur Steuerung seiner Parameter.

* `Validate` Backt das Primitive in ein Standardobjekt, sodass es skulptiert und bemalt werden kann.
* `Edit` Schaltet die Anzeige des Primitive-Gizmos um. Dieses wird direkt auf dem Primitive angezeigt, um seine Parameter zu steuern, z. B. die Würfelbreite oder den Lochradius eines Zylinders.
* `Mirror` Platziert einen Mirror-Repeater über dem Primitive.
* `...` Zeigt das Primitive-Menü an.

Verschiedene Primitives haben zusätzliche Optionen in der Werkzeugleiste:

* `Project` Die Sphere wird als unterteilter Würfel konstruiert, was besser zum Skulptieren ist, aber bedeutet, dass sie nicht perfekt rund ist. Diese Option zwingt die Form näher an eine perfekte Kugel. Der Icosahedron teilt diese Option.
* `Cap` Schaltet Endkappen für eine Form um, z. B. kann ein Zylinder Kappen oben, unten, beides oder keine haben.
* `Hole` Schaltet ein Loch durch die Mitte einer Form um. Dies wechselt zwischen keinem Loch, einem Loch mit einfachem Radius oder einem Loch mit unterschiedlichem Radius oben und unten.
* `Radius` Schaltet, ob ein Zylinder einen einzigen Radius oder unterschiedliche Radien oben und unten haben soll.
* `Disk` Schaltet, ob eine Plane eine viereckige Form oder eine Kreisform sein soll.

Die kleine Werkzeugleiste unter der Hauptleiste ermöglicht das Umschalten zwischen dem Primitive-Gizmo und dem Transform-Gizmo.

::: tip

Ein Klick auf den Titel der Werkzeugleiste schaltet sie zwischen oberem und unterem Bildschirmrand um. Ein Klick auf den Pfeil in der Ecke klappt sie ein.

:::


### Primitive-Menü

![](/images/scene_primitive_menu.webp)

Dies enthält alle Parameter für das ausgewählte Primitive. Parameter sind die grundlegende Beschreibung einer Form. Um z. B. einen Ring zu beschreiben, würdest du seinen Außenradius, Innenradius und die Anzahl der Polygone angeben.

Die meisten Primitive-Parameter sollten selbsterklärend sein, und es gibt einige gemeinsame Parameter, die alle Primitives teilen:

* `UVs` Der kleine UVs-Button oben im Menü schaltet die Erstellung von UV-Koordinaten um
* `Validate` Der kleine Validate-Button backt das Primitive in ein Standardobjekt, sodass es skulptiert und bemalt werden kann.
* `Max faces` Legt ein Oberlimit für die Anzahl der Polygone im Objekt fest, um Abstürze deines Geräts zu vermeiden.
* `Post subdivision` Aktiviert die gewählte Anzahl an Subdivision-Stufen aus dem Multiresolution-Abschnitt des Topologie-Menüs. Dies kann verwendet werden, um in Kombination mit niedrigen Topologie-Unterteilungen glatte, weichkantige Primitives zu erzeugen. Wenn du z. B. die Box-Topologie-Unterteilungen auf 2 und Post Subdivisions auf 4 setzt, erhältst du eine Box mit weichen Ecken.
* `Linear subdivision` Legt fest, wie viele Stufen linearer Subdivision vor der regulären glatten Subdivision verwendet werden. Dies kann genutzt werden, um zu steuern, wie scharf oder weich die Ecken auf den unterteilten Oberflächen sind. Setze z. B. die Box-Topologie-Unterteilungen auf 2, Post Subdivisions auf 4, und ändere dann die linearen Subdivisions zwischen 0 und 4. Die Ecken der Box werden von weich zu scharf wechseln.

### Topologie

Dies steuert die Anzahl der Polygone in einem Primitive. Normalerweise sind die Regler gekoppelt, sodass das Ändern des aktiven Sliders alle Polygone gleichmäßig anpasst. Du kannst auf den Entkoppeln-Button tippen und die X/Y/Z-Unterteilungen einer Form separat steuern.

### Geometrie

Dies steuert die Gesamtgröße eines Primitives, in X/Y/Z-Einheiten für eckige Formen und in Radius für runde Formen.


### UV Sphere
::: warning
Die UV Sphere ist zum Skulptieren, insbesondere an den Polen, nicht gut geeignet.

Verwende bevorzugt die Primitives [Sphere](#sphere), [Box](#box) oder [Icosahedron](#icosahedron) zusammen mit der Option `Project on sphere`.

Beachte, dass die Topologie zum Skulptieren akzeptabel sein kann, wenn du einen sehr niedrigen Wert für die `Division`-Slider verwendest.
Du kannst dann den Slider `Overall Subdivision` verwenden, um die Polygonanzahl zu erhöhen.

Auch wenn sie sich nicht für allgemeines Skulptieren eignet, ist sie nützlich für Augen; wenn du die Sphere so drehst, dass die Pole an der Pupille liegen, passt sich die Polygonanordnung natürlich an, um Iris und Pupille zu malen und zu skulptieren.
:::


### Triplanar
Dieses Primitive ist speziell, da du das [Masking-Werkzeug](tools.md#mask) verwenden solltest, um seine Geometrie zu formen.

![](/videos/triplanar.mp4)


::: tip
Doppeltippe auf eine Ebene und die Kamera fokussiert diese bestimmte Ebene.
Dies funktioniert jedoch nicht, wenn du das Primitive mit dem Gizmo drehst.
:::

Triplanar verwendet die Maskeninformationen von 3 Ebenen, um ein Voxelgitter zu füllen, das dann polygonisiert wird (dank des [Voxel Remeshers](topology.md#voxel-remeshere)).

Jede Ebene hat ihre eigene Symmetrieebene.

::: warning
Jedes Mal, wenn du die Größe des Triplanar-Primitives änderst, verschlechtert sich die Qualität der Maskenmalerei.

Derzeit gibt es keine Option, die Malerei auf einer einzelnen Ebene zu „sperren“, aber vielleicht kommt dies in Zukunft.
Du kannst [Connected Topology](stroke.md#connected-topology) verwenden, um ein wenig zu helfen, da dein Cursor, wenn er genau auf einer Ebene liegt, die anderen Ebenen nicht beeinflusst.
:::

### Shadow Catcher
Fügt eine Ebene mit dem Shadow-Catcher-Material hinzu. Siehe [Shadow Catcher-Material](material.md#shadow-catcher) für weitere Details. 


## Gruppe/Kamera
### Gruppe
Erstellt ein „leeres“ Objekt, unter dem du andere Objekte einordnen kannst. Dies kann verwendet werden, um die Hierarchie zu organisieren, indem du viele Objekte unter einer Gruppe sammelst und diese dann zuklappst. Eine Gruppe kann auch als Hilfsobjekt zum Bewegen von Objekten dienen; viele Objekte können unter eine Gruppe gestellt werden, und dann kann die Gruppe mit dem Gizmo-Werkzeug bewegt, rotiert und skaliert werden.

### Ansicht hinzufügen
Erstellt eine Kamera.

## Repeater
![](/images/scene_primitive_repeaters.webp)

Repeater sind Knoten, die Instanzen der Objekte unter ihnen erzeugen. 

### Array
![](/images/scene_primitive_array.webp)

Wenn Objekte zu Kindern dieses Knotens gemacht werden, können sie in einem Gitterlayout instanziert werden. Wenn ausgewählt, hat er folgende Steuerungen:
* Fit inside – Umschalten zwischen der Steuerung der Größe des Gitter-/Box-Arrays oder der Steuerung des Abstands zwischen den Array-Instanzen
* CountX/Y/Z – Anzahl der Instanzen auf jeder Achse
* OffsetX/Y/Z – Abstand zwischen den Instanzen, wenn Fit inside umgeschaltet ist
* SizeX/Y/Z – Breite/Höhe/Tiefe des gesamten Array-Gitters, wenn Fit inside umgeschaltet ist.

### Curve
![](/images/scene_primitive_curve.webp)
Dies erstellt eine Kurve, Kinder dieses Knotens werden entlang der Kurve wiederholt. Wenn ausgewählt, hat er folgende Steuerungen:
* Edit – erlaubt das Hinzufügen von Punkten zur Kurve und das Bewegen von Punkten auf der Kurve.
* Snap – rastet Kurvenpunkte an anderer Geometrie ein
* Align – rotiert Kindformen so, dass sie sich an der Richtung der Kurve ausrichten
* Count – Anzahl der Instanzen
* Closed – schaltet die Kurve zwischen geschlossen (Start und Ende verbunden) und offen um
* Radius – schaltet Steuerungen an jedem Kurvenpunkt, um die Skalierung der Instanzen zu steuern
* Twist – schaltet Steuerungen an jedem Kurvenpunkt, um die Drehung (Twist) der Instanzen zu steuern 
* B-spline – schaltet um, ob die Instanzen der Kurve exakt folgen oder B-Spline-Interpolation verwenden, die glattere Ergebnisse liefert. 

### Radial
![](/images/scene_primitive_radial.webp)

Kinder dieses Knotens werden in einem Kreis instanziert. Bewege das Kindobjekt, um den Radius dieses Repeaters zu ändern. Wenn ausgewählt, hat er folgende Steuerungen:
* RadialX/Y/Z – durch Auswahl dieser Buttons wird die Radialachse festgelegt und die Anzahl der Instanzen bestimmt.



### Mirror
![](/images/scene_primitive_mirror.webp)

Kinder dieses Knotens werden an einer Achse gespiegelt. Wenn ausgewählt, hat er folgende Steuerungen:
* Gizmo – aktiviert das Transform-Gizmo, um das Zentrum des Spiegels festzulegen. Dieses kann auch rotiert und skaliert werden. Wenn du fertig bist, tippe erneut auf Gizmo, um die Standardsteuerungen wieder anzuzeigen.
* X/Y/Z – legt die Spiegel-Ebene fest

Alle Repeater haben eine `Validate`-Steuerung, die die Ergebnisse des Repeaters backt und fragt, wie das Baking durchgeführt werden soll:
* Join children – die Instanzen werden zu einem einzigen Objekt verbunden
* Keep instances – die Instanzen bleiben Instanzen, haben aber keinen Repeater-„Elternteil“ mehr
* Un-instances – die Instanzen werden in einzigartige Objekte umgewandelt

::: tip Tipp: Repeater kombinieren
Repeater können untereinander verschachtelt werden, und mehrere Objekte können zu Kindern von Repeatern gemacht werden, was zu komplexen Effekten führt.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tipp: Repeater-Pivots

Einige Repeater versuchen, die Pivots der Kindobjekte automatisch zu setzen, sodass sie sich nicht bewegen, selbst wenn du sie mit dem Gizmo-Werkzeug verschiebst oder drehst. Wenn du dieses Verhalten überschreiben musst, füge eine Gruppe zwischen Repeater und Kind ein. Jetzt kannst du die Kindform unabhängig vom Repeater bewegen.
:::

## Licht

![](/images/scene_primitive_light.webp)

### Directional
Erstellt ein gerichtetes Licht, eine unendlich weit entfernte Lichtquelle wie die Sonne.

### Spot
Erstellt ein Spot-Licht mit Steuerungen für Kegelbreite und Weichheit.

### Point
Erstellt ein Punktlicht.

## Erweitert
### Auf Element fokussieren
Doppelklick auf ein Element in der Szenenliste zentriert die Kamera im 3D-View auf dieses Element.

### Sichtbarkeit synchronisieren
Die Verwendung des Augen-Icons wirkt sich auf alle ausgewählten Elemente aus. 

### Instanz: Anzeigen
Zeigt eine farbige Kapsel links in der Szenenliste an, um Instanzen zu markieren.


### Icons
Legt Größe und Deckkraft der Gruppen-, Licht-, Kamera- und Mirror-Icons im Viewport fest.

### Hierarchie-Linien
Zeigt eine Linie zwischen Eltern und Kindern im Viewport an.

## Untere Werkzeugleiste
Diese Icons schalten die Sichtbarkeit von Gruppe, Licht, Kamera, Repeater und Hierarchie-Linien im Viewport um.
