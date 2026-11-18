# ![](/icons/scene.webp) Szene {#scene}

In diesem Menü verwalten Sie Objekte, Lichter, Kameras und Repeater in Nomad. Es zeigt die Hierarchie der Szene als Baumansicht, in der Sie viele Eigenschaften Ihrer Objekte ändern können. Außerdem können Sie hier neue Objekte erstellen sowie Objekte auf verschiedene Arten kombinieren und trennen.


![](/images/scene_menu_summary.webp)


## Shortcut-Leiste {#shortcut-bar}
| Aktion                      | Icon                              | Beschreibung                                                                                                        |
| :-------------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Hinzufügen...](#add-menu)  | ![](/icons/plus.webp)            | Öffnet das [Menü Hinzufügen](#add-menu), um der Szene ein Objekt hinzuzufügen                                        |
| Löschen                     | ![](/icons/trash.webp)           | Löscht die ausgewählten Objekte. Ihre Unterknoten bleiben erhalten.                                                  |
| Sperren                     | ![](/icons/lock.webp)            | Die ausgewählten Objekte lassen sich im Viewport nicht mehr auswählen, in der Baumansicht aber weiterhin schon. Das Sperren einer Gruppe sperrt alles darunter. Tippen Sie erneut, um die Sperre aufzuheben. |
| [Kombinieren](#join)        | ![](/icons/merge.webp)           | Fasst die ausgewählten Objekte zu einem einzigen Objekt zusammen, ohne die Geometrie zu verändern                    |
| [Trennen...](#separate)     | ![](/icons/separate.webp)        | Öffnet das Popup [Trennen](#separate), um ein Objekt in mehrere Objekte aufzuteilen. Das Gegenteil von Kombinieren  |
| [Boolean...](#boolean)      | ![](/icons/bool_subtract_circle.webp) | Öffnet das Popup [Boolean](#boolean)                                                                           |
| Klonen                      | ![](/icons/clone.webp)           | Dupliziert die ausgewählten Objekte als neue Objekte                                                                 |
| Instanz                     | ![](/icons/link.webp)            | Dupliziert die ausgewählten Objekte als Instanzen, sodass Änderungen am Modell einer Instanz in allen Instanzen übernommen werden. |
| Instanz aufheben            | ![](/icons/unlink.webp)          | Wandelt eine Instanz in eine eigenständige Form um, sodass Änderungen am Modell nicht mehr auf andere Instanzen übertragen werden |
| Synchronisieren             | ![](/icons/checked.webp)         | Wenn aktiviert, wirken Aktionen auf alle Instanzen der ausgewählten Objekte, nicht nur auf die ausgewählten. Nur verfügbar, wenn die Auswahl Instanzen enthält. Im [Tab Synchronisieren](#sync) des Popups `Erweitert` legen Sie fest, welche Aktionen diesem Kontrollkästchen folgen. |

::: tip
Wenn eine Aktion auch die anderen Instanzen betrifft, erscheint auf ihrer Schaltfläche ein kleines Ketten-Icon.
:::


## Baumansicht {#tree-view}
![](/images/scene_treeview.webp) 

Die Baumansicht listet die Objekte, Gruppen, Repeater, Lichter und Kameras der Szene auf. Neben dem Namen eines Meshes sehen Sie seine Anzahl an Vertices und, wenn es Layer hat, ein farbiges Layer-Icon. Jede Zeile hat diese Schaltflächen:

| Aktion       | Icon                       | Beschreibung             |
| :----------: | :------------------------: | :----------------------: |
| Name         | ![](/icons/pencil.webp)   | Benennt das Objekt um. Ist es ausgewählt, werden alle ausgewählten Objekte auf einmal umbenannt, jeweils mit einer angehängten Nummer. Lange drücken benennt es zusammen mit seinen Unterknoten um. |
| Auswählen    | ![](/icons/checked.webp)  | Auswahl ein/aus          |
| Sichtbar     | ![](/icons/eye_open.webp) | Sichtbarkeit ein/aus     |
| Menü         | ![](/icons/more.webp)     | Öffnet das [Objektmenü](#object-menu) |

::: tip TIPP: Schnell viele Objekte auswählen oder ausblenden

Tippen Sie auf das Auswahl-Icon, um ein einzelnes Objekt umzuschalten, oder ziehen Sie senkrecht über die Auswahlspalte, um viele Objekte auszuwählen. Mit der Spalte für die Sichtbarkeit geht das genauso.

Drücken Sie lange auf das Auswahl- oder Sichtbarkeits-Icon, um auch die Unterknoten einzubeziehen.

:::

### Kopfzeile der Baumansicht {#tree-view-header}

Die Zeile über der Liste bietet ein paar Hilfen:

* ![](/icons/sort_down.webp) - klappt alle Gruppen auf einmal zu oder auf.
* ![](/icons/preview.webp) - schaltet die `Objektvorschauen` ein oder aus, ein kleines gerendertes Vorschaubild für jedes Objekt der Liste.
* ![](/icons/search.webp) - filtert die Liste nach Namen.

### Arbeiten mit der Baumansicht {#tree-view-manipulation}

Drücken Sie lange auf einen Eintrag in der Baumansicht, bis er hervorgehoben ist. Dann können Sie ihn in der Baumansicht nach oben oder unten verschieben oder ihn auf einen anderen Eintrag ziehen, um ihn zu dessen Unterknoten zu machen.

Wenn mehrere Einträge ausgewählt sind, ist einer davon die Hauptauswahl und wird heller dargestellt. Drücken Sie lange auf einen von ihnen und ziehen Sie, um alle ausgewählten Objekte auf einmal zu verschieben.

Wenn Sie einen übergeordneten Eintrag auswählen, werden standardmäßig auch alle seine Unterknoten ausgewählt. Tippen Sie erneut auf den übergeordneten Eintrag, um zwischen der Auswahl nur dieses Eintrags und der Auswahl mit seinen Unterknoten zu wechseln.

Tippen Sie doppelt auf einen Eintrag, um die Kamera darauf auszurichten (siehe [Erweitert](#focus-on-item)).

### Objektmenü {#object-menu}

Ein Tipp auf die Schaltfläche mit den drei Punkten (...) eines Objekts in der Baumansicht öffnet das Objektmenü.
Viele dieser Optionen entsprechen der Shortcut-Leiste oben und sind hier der Einfachheit halber wiederholt.

|       Aktion        |                        Icon                        | Beschreibung                                                                                                                                                            |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Name         |              ![](/icons/pencil.webp)           | Ändert den Namen des Objekts                                                                                                                                            |
|  Instanz aufheben   |              ![](/icons/unlink.webp)           | Wandelt eine Instanz in eine eigenständige Form um, sodass Änderungen am Modell nicht mehr auf andere Instanzen übertragen werden.                                     |
|      Instanz        |               ![](/icons/link.webp)            | Dupliziert das Objekt als Instanz, sodass Änderungen am Modell einer Instanz in allen Instanzen übernommen werden.                                                     |
|       Klonen        |              ![](/icons/clone.webp)            | Dupliziert das Objekt als neues Objekt                                                                                                                                  |
|       Löschen       |              ![](/icons/trash.webp)            | Löscht das Objekt. Seine Unterknoten bleiben erhalten, außer `Unterknoten` ist aktiviert.                                                                               |
|     Unterknoten     |            ![](/icons/hierarchy.webp)          | Wenn aktiviert, wirken `Instanz`, `Klonen` und `Löschen` auch auf die Unterknoten des Objekts.                                                                         |
| Nach Teilen trennen |             ![](/icons/separate.webp)          | Besteht ein Objekt aus nicht verbundenen Teilen, wird für jedes davon ein eigenes Objekt erstellt. Das Gegenteil von Kombinieren.                                      |
| Nach Gruppen trennen |            ![](/icons/group.webp)          | Hat ein Objekt mehrere Face-Gruppen, wird für jede Face-Gruppe ein eigenes Objekt erstellt.                                                                                |
| Nach Ebenen trennen |              ![](/icons/layer.webp)            | Hat ein Objekt Layer, werden eigene Objekte für das Basis-Mesh und für jeden Layer erstellt. Nützlich, um Blendshapes an andere Anwendungen zu übergeben.               |
| Kombinieren → Layer | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Sind mehrere Objekte mit gleicher Topologie ausgewählt, werden sie als Layer im Hauptobjekt zusammengeführt (die anderen Objekte werden gelöscht). Auch das ist nützlich für Blendshapes, die AUS anderen Anwendungen kommen.<br><br> Die Layer sind standardmäßig deaktiviert. Aktivieren Sie sie, wenn Sie ihre Regler einstellen möchten. |
|  Kurve (Repeater)   |              ![](/icons/curve.webp)            | Nur für eine Röhre oder eine Drehbank: fügt als Unterknoten des Objekts einen [Kurven](#curve)-Repeater hinzu, der derselben Kurve folgt.                              |
|       Röhre         |             ![](/icons/tube.webp)              | Fügt bei einer Drehbank als Unterknoten eine [Röhre](tools.md#tube) hinzu, die ihrem Profil folgt. Wandelt einen Zylinder, einen Kegel oder einen Torus in eine Röhre derselben Form um, sodass Sie ihn entlang einer Kurve biegen können. |




### Mehrfachauswahl {#multiselection}
Sie können mehrere Objekte auswählen, um vor allem zwei Dinge zu tun:
- mehrere Objekte auf einmal mit dem Werkzeug Gizmo bewegen
- Objekte mit Kombinieren und Boolean-Operationen zusammenführen.

Tippen Sie in der Baumansicht auf das Auswahl-Icon jedes Objekts oder ziehen Sie entlang der Auswahlspalte. Wenn Sie auf Namen tippen, halten Sie den Shortcut `Maske` (oder `Ctrl` auf einer Tastatur) gedrückt, um ein einzelnes Objekt hinzuzufügen oder zu entfernen, oder den Shortcut `Glätten` (oder `Shift`), um alle Objekte zwischen dem aktuellen und dem angetippten auszuwählen.

::: tip Schnelle Mehrfachauswahl
Sie können auch im Viewport mehrere Objekte auswählen, indem Sie den Shortcut `Glätten` (oder `Shift`) gedrückt halten und auf ein anderes Mesh tippen.

Ein erneuter Tipp auf ein Objekt hebt seine Auswahl wieder auf (nur wenn Ihre Auswahl mehr als ein Objekt umfasst).
:::

Das Gizmo bewegt alle ausgewählten Objekte gemeinsam, siehe [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Kombinieren {#join}
Diese Option fasst einfach mehrere ausgewählte Objekte zu einem einzigen Objekteintrag zusammen.
Punkte und UVs, die näher beieinanderliegen als der [Schweißradius](#weld-radius), werden verschmolzen.

Ein Beispiel als Video finden Sie im Abschnitt [Trennen](#separate).

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Fügt Objekte zu einer einzigen Oberfläche zusammen.

`Voxel Merge` erhält das Volumen der Objekte und berechnet neue, gleichmäßig verteilte Polygone auf der Oberfläche. Dank dieses Berechnungsschritts kommt ein Voxel Merge mit komplexer Geometrie zurecht, kann aber feine Details verlieren, wenn die Zielauflösung nicht hoch genug ist.

`Boolean` versucht, die Polygone in ihrer ursprünglichen Anordnung zu lassen, und vernäht sie dort, wo sich die Objekte überschneiden. Das kann viel sauberere und schärfere Ergebnisse liefern als ein Voxel Merge, setzt aber „wasserdichte“ Meshes voraus: Die Objekte dürfen keine Löcher und keine fehlerhaften Formen haben. Wenn das scheitert, funktioniert meist ein Voxel Merge.

### Boolean-Operationen {#boolean-operations}
Voxel Merge und Boolean steuern die Operation beide über die Sichtbarkeit der Objekte, wie die Hinweise unten im Popup zeigen:

#### Vereinigung {#union}
Beide Objekte sichtbar ergibt eine boolesche **Vereinigung**: Die Außenhüllen der Objekte werden zusammengefügt, ohne innere Flächen. ![](/images/boolean_union.webp)

#### Subtraktion {#subtract}
Ein Objekt ausgeblendet = boolesche **Subtraktion**: Das ausgeblendete Objekt wird vom sichtbaren Objekt abgezogen. ![](/images/boolean_subtract.webp)

#### Schnittmenge {#intersect}
Beide Objekte ausgeblendet = boolesche **Schnittmenge**: Es entsteht eine neue Form nur dort, wo sich die beiden Objekte überschneiden. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Voxel Merge {#voxel-merge-button}
Diese Schaltfläche führt einen Voxel Merge mit den ausgewählten Objekten aus. Bei einem einzelnen Objekt wird dessen Topologie in gleichmäßig verteilte Polygone neu berechnet, praktisch, wenn ein Objekt verzerrte Polygone hat. Die Optionen darunter funktionieren wie die des [Voxel Remeshings](topology.md#voxel-remesher).

### Auflösung {#resolution}
Die Auflösung des 3d-Voxelrasters, mit dem gerechnet wird. Wenn Sie diesen Wert ändern, wird ein Schachbrettmuster über das Objekt gelegt, das die Größe der Polygone vorab zeigt.

Die Pipette neben dem Regler übernimmt den Detailgrad aus der Dichte des Meshes unter Ihrem Finger. Die Schaltfläche daneben stellt den Regler auf `Kantenlänge` um, eine Größe in Welteinheiten: Derselbe Wert ergibt dann auf jedem Objekt denselben Detailgrad.

### Multiresolution erstellen {#build-multiresolution}
Erstellt Multiauflösungs-Stufen unterhalb Ihrer Zielauflösung. Bei einer Auflösung von 400 und einem Wert von 3 für Multiresolution erstellen erhalten Sie zum Beispiel ein neues Mesh mit etwa 296.000 Polygonen, darunter aber 3 niedrigere Unterteilungsstufen mit etwa 74.000, 18.500 und 4.600.

### Dünne Teile verdicken {#thicken-thin-parts}
Verdickt Teile, die für das Voxelraster zu dünn sind, damit sie nicht zerbrechen. Nicht verfügbar mit `Scharfe Kanten` oder `Scharfe Grenze`.

### Löcher {#holes}
Wie Löcher in offenen Objekten vor dem Zusammenführen geschlossen werden:
* `Füllen` - jedes Loch wird für sich von seinem Rand aus geschlossen.
* `Form` - Löcher werden geschlossen, indem sie der umgebenden Oberfläche folgen, und offene Teile, die sich überschneiden, werden verbunden.

### ![](/icons/angle.webp) Scharfe Kanten beibehalten {#keep-sharp-edges}
Die Schaltfläche `Scharfe Kanten` richtet das Voxel-Mesh an den scharfen Kanten der Objekte aus. Das funktioniert am besten bei einfachen Formen und kann stellenweise Verzerrungen erzeugen.

### ![](/icons/group.webp) Scharfe Grenze {#sharp-border}
Die neuen Flächen folgen den Grenzen der Face-Gruppen, und eine Grenze bleibt scharf, wo die Oberfläche entlang dieser Grenze einen Knick hat.

### ![](/icons/group_separate.webp) Gruppen getrennt halten {#keep-groups-separate}
Jede Face-Gruppe wird für sich neu vernetzt: Gruppen verschmelzen nie, und jede bleibt ein geschlossenes Stück in ihrer eigenen Gruppe. In diesem Modus wird keine Multiauflösung erstellt.

### ![](/icons/bool_subtract_circle.webp) Schaltfläche Boolean {#boolean-button}
Diese Schaltfläche führt eine boolesche Operation auf Polygonbasis aus, mit der Bibliothek Manifold von Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Überlappungen bereinigen {#clean-overlaps}
Ist nur ein Objekt ausgewählt, wird aus der Schaltfläche `Boolean` die Schaltfläche `Überlappungen bereinigen`: Sie verschmilzt die Teile des Objekts, die sich gegenseitig durchdringen, zu einer sauberen Oberfläche.


## ![](/icons/separate.webp) Trennen {#separate}
Wenn Sie ein einzelnes Objekt haben, das aus mehreren nicht verbundenen Teilen besteht, können Sie es in mehrere Objekte aufteilen.
Das ist das Gegenteil von [Kombinieren](#join).

Das Popup `Trennen...` bietet drei Möglichkeiten, die ausgewählten Objekte zu trennen:
* `Nach Teilen trennen` - erstellt für jedes nicht verbundene Teil ein eigenes Objekt.
* `Nach Gruppen trennen` - erstellt für jede Face-Gruppe ein eigenes Objekt.
* `Nach Ebenen trennen` - erstellt eigene Objekte für das Basis-Mesh und jeden Layer.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menü Hinzufügen {#add-menu}

![](/images/scene_addmenu_overview.webp)

Mit diesem Menü erstellen Sie Grundformen, Gruppen, Kameras, Repeater und Lichter.

Grundformen sind einfache Formen, die sich über Parameter anpassen lassen. Wenn die Grundform Ihren Vorstellungen entspricht, schließen Sie sie ab („Abschließen“). Dabei werden die Parameter in ein Polygon-Mesh umgewandelt, das Sie modellieren und bemalen können. Nach dem Abschließen lassen sich die Parameter einer Grundform nicht mehr ändern.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Am Gizmo {#on-gizmo}
Platziert die neue Grundform dort, wo sich die aktuell ausgewählte Form oder das Gizmo befindet. Ist die Option deaktiviert, wird die Grundform in der Mitte der Szene platziert.

### ![](/icons/gizmo.webp) Gizmo auswählen {#select-gizmo}
Wechselt automatisch zum Werkzeug Gizmo, wenn eine neue Grundform erstellt wird.

### ![](/icons/cog.webp) Erweitert {#add-advanced}

Hier legen Sie fest, wo neue Grundformen, Gruppen und Repeater erstellt werden: am ausgewählten Objekt, im Ursprung der Welt oder an der Position des Gizmos.


### UVs {#uvs}
Der Schalter `UVs` neben dem Titel Grundformen aktiviert UVs für Grundformen. UVs (oft Texturkoordinaten genannt) sind zusätzliche Daten, mit denen in 3d Texturen auf Oberflächen gelegt werden. Sie belegen mehr Speicher, aber auf den meisten Geräten spielt das erst bei sehr hohen Polygonzahlen eine Rolle (z. B. ab 10 Millionen Polygonen).

### Grundformen {#primitives}

| Grundform      | Icon                                      | Beschreibung                                                                                                    |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Ein einfacher Würfel, dessen Unterteilung in X, Y und Z Sie einstellen können                                   |
| Quad-Kugel     | ![](/icons/circle.webp)                  | Eine unterteilte Box mit fest aktivierter Option `Kugel`, sodass sie eine gleichmäßige Quad-Anordnung hat, die sich gut zum Modellieren eignet |
| Zylinder       | ![](/icons/cylinder.webp)                | Beim Zylinder können Sie ein Loch in der Mitte hinzufügen, zum Beispiel für ein hohles Rohr                     |
| Torus          | ![](/icons/torus.webp)                   | Der Torus ist ein guter Ausgangspunkt für Ringe                                                                 |
| Kegel          | ![](/icons/cone.webp)                    | -                                                                                                               |
| Ikosaeder      | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-Kugel       | ![](/icons/circle.webp)                  | Eine Kugel mit ungleichmäßiger Polygonverteilung, siehe [Warnung unten](#uv-sphere)                             |
| Ebene          | ![](/icons/rectangle.webp)               | Eine einfache Ebene. Sie ist die einzige Grundform, die nicht geschlossen ist                                   |
| Text           | ![](/icons/text.webp)                    | 3d-Text mit Schriftart, Stil, Ausrichtung, Tiefe und Biegung. `Buchstaben verschmelzen` verbindet Buchstaben, die sich berühren |
| Röhre          | ![](/icons/tube.webp)                    | siehe [Röhre](tools#tube)                                                                                       |
| Drehbank       | ![](/icons/lathe.webp)                   | siehe [Drehbank](tools#lathe)                                                                                   |
| Triplanar      | ![](/icons/triplanar.webp)               | siehe [Triplanar](#triplanar)                                                                                   |
| VDM            | ![](/icons/vdm.webp)                     | Eine Ebene, die zum Modellieren eines Vector-Displacement-Stempels eingerichtet ist: mit UVs und zur Kamera ausgerichtet |
| Schattenfänger | ![](/icons/material_shadow_catcher.webp) | siehe [Schattenfänger](#shadow-catcher)                                                                         |
| Kopf           | ![](/icons/face.webp)                    | Ein einfacher Kopf mit einem Layer, um zwischen männlich und weiblich zu überblenden                            |

::: tip
Falls Sie sich fragen, was das Basis-Mesh beim Start von Nomad ist: Auch das ist eine unterteilte Box.
Das Basis-Mesh von Nomad verwendet allerdings nicht die Option `Kugel`, es ist also nicht perfekt rund.
:::

### Werkzeugleiste der Grundform {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Sobald eine Grundform erstellt ist, erscheint eine Werkzeugleiste, mit der Sie ihre Parameter steuern.

* `Abschließen` Wandelt die Grundform in ein normales Objekt um, damit Sie es modellieren und bemalen können.
* `Spiegeln` Setzt einen Spiegel-Repeater über die Grundform oder entfernt ihn.
* `Alle` (Augen-Icon) Legt fest, welche Griffe direkt auf der Grundform angezeigt werden, um ihre Parameter zu steuern, z. B. die Breite des Würfels oder den Lochradius eines Zylinders: `Keine`, `Alle` oder je nach Grundform nur eine Art (Radius, Loch, Profil...).
* `Unterteilung` Die Anzahl der Unterteilungen der Grundform, hier entlang X für eine Box.
* `Konstante Dichte` Wenn Sie die Grundform mit dem Gizmo entlang einer Achse strecken, wachsen ihre Größe und ihre Unterteilungen mit, statt dass sich die Polygone verzerren, sodass die Flächen quadratisch bleiben. Verfügbar für Boxen, Ebenen und Zylinder.
* `...` Öffnet das Menü der Grundform.

Je nach Grundform bietet die Werkzeugleiste zusätzliche Optionen:

* `Kugel` Die Kugel wird als unterteilter Würfel aufgebaut, weil das zum Modellieren besser ist, sie ist dadurch aber nicht perfekt rund. Diese Option zwingt die Form näher an eine perfekte Kugel. Das Ikosaeder hat diese Option ebenfalls.
* `Kappe` Schaltet Abschlusskappen einer Form ein oder aus, z. B. kann ein Zylinder oben, unten, an beiden Enden oder gar keine Kappe haben.
* `Loch` Erzeugt ein Loch durch die Mitte einer Form. Die Option wechselt zwischen keinem Loch, einem Loch mit einem einzigen Radius und einem Loch mit unterschiedlichem Radius oben und unten.
* `Radius` Legt fest, ob ein Zylinder einen einzigen Radius oder oben und unten unterschiedliche Radien hat.
* `Scheibe` Legt fest, ob eine Ebene viereckig oder kreisförmig ist.

Mit der kleinen Werkzeugleiste unter der Hauptleiste wechseln Sie zwischen dem Gizmo der Grundform und dem Transformations-Gizmo.

::: tip

Ein Tipp auf den Titel der Werkzeugleiste verschiebt sie an den oberen oder unteren Bildschirmrand. Ein Tipp auf den Pfeil in der Ecke klappt sie ein.

:::


### Menü der Grundform {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Hier finden Sie alle Parameter der ausgewählten Grundform. Parameter sind die grundlegende Beschreibung einer Form. Einen Ring beschreiben Sie zum Beispiel über seinen Außenradius, seinen Innenradius und die Anzahl der Polygone.

Die meisten Parameter erklären sich von selbst, und einige sind allen Grundformen gemeinsam:

* `UVs` Die kleine Schaltfläche UVs oben im Menü schaltet die Erzeugung von UV-Koordinaten ein oder aus.
* `Abschließen` Die kleine Schaltfläche zum Abschließen wandelt die Grundform in ein normales Objekt um, damit Sie es modellieren und bemalen können.
* `Max. Faces` Legt eine Obergrenze für die Anzahl der Polygone des Objekts fest, damit Ihr Gerät nicht abstürzt.
* `Nachträgliche Unterteilung` Wendet die gewählte Anzahl an Unterteilungen aus dem Bereich Multiauflösung des Menüs Topologie an. Zusammen mit einer niedrigen Unterteilung der Topologie lassen sich so geglättete Grundformen mit weichen Ecken erzeugen. Stellen Sie zum Beispiel die Unterteilung der Topologie einer Box auf 2 und die nachträgliche Unterteilung auf 4, erhalten Sie eine Box mit abgerundeten Ecken.
* `Lineare Unterteilung` Legt fest, wie viele Stufen linearer Unterteilung vor der normalen, glättenden Unterteilung angewendet werden. Damit steuern Sie, wie scharf oder weich die Ecken der unterteilten Oberfläche sind. Stellen Sie z. B. die Unterteilung der Topologie einer Box auf 2 und die nachträgliche Unterteilung auf 4, und ändern Sie dann die lineare Unterteilung zwischen 0 und 4. Die Ecken der Box werden dabei von weich zu scharf.

### Topologie {#topology}

Hier steuern Sie die Anzahl der Polygone einer Grundform. Normalerweise sind die Regler verknüpft, sodass der eine aktive Regler alle Polygone gleichmäßig anpasst. Tippen Sie auf die Schaltfläche zum Entkoppeln, um die Unterteilungen in X/Y/Z einer Form getrennt einzustellen.

### Geometrie {#geometry}

Hier steuern Sie die Gesamtgröße einer Grundform, in X/Y/Z-Einheiten bei eckigen Formen und über den Radius bei runden Formen.


### ![](/icons/circle.webp) UV-Kugel {#uv-sphere}
::: warning
Die UV-Kugel eignet sich nicht gut zum Modellieren, vor allem an den Polen.

Verwenden Sie lieber die [Grundformen](#primitives) Quad-Kugel, Box oder Ikosaeder mit der Option `Kugel`.

Die Topologie kann zum Modellieren akzeptabel sein, wenn Sie für die Regler `Unterteilung` einen sehr niedrigen Wert verwenden.
Mit dem Regler `Gesamtunterteilung` können Sie dann die Anzahl der Polygone erhöhen.

Für das allgemeine Modellieren ist sie zwar ungeeignet, für Augen aber nützlich: Wenn Sie die Kugel so drehen, dass die Pole auf der Pupille liegen, eignet sich die Polygonanordnung von Natur aus gut, um Iris und Pupille zu bemalen und zu modellieren.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Das Besondere an dieser Grundform ist, dass Sie ihre Geometrie mit dem [Werkzeug Maske](tools.md#mask) formen.

![](/videos/triplanar.mp4)


::: tip
Tippen Sie doppelt auf eine Ebene, und die Kamera richtet sich auf genau diese Ebene aus.
Das funktioniert allerdings nicht, wenn Sie die Grundform mit dem Gizmo gedreht haben.
:::

Triplanar nutzt die Maskeninformation von 3 Ebenen, um ein Voxelraster zu füllen, das dann in Polygone umgewandelt wird (dank des [Voxel Remeshings](topology.md#voxel-remesher)).

Jede Ebene hat ihre eigene Symmetrieebene.

::: warning
Jedes Mal, wenn Sie die Größe der Grundform Triplanar ändern, verschlechtert sich die Qualität der gemalten Maske.

Derzeit gibt es keine Option, das Malen auf eine einzige Ebene zu „sperren“, vielleicht kommt das in Zukunft.
Die Option [Connected Topology](stroke.md#connected-topology) hilft ein wenig: Liegt Ihr Cursor genau auf einer Ebene, wirkt er sich nicht auf die anderen Ebenen aus.
:::

### ![](/icons/material_shadow_catcher.webp) Schattenfänger {#shadow-catcher}
Fügt eine Ebene mit dem Material Schattenfänger hinzu. Mehr dazu unter [Material Schattenfänger](material.md#shadow-catcher).


## Gruppe/Kamera {#groupcamera}
### ![](/icons/share.webp) Gruppe {#group}
Erstellt ein „leeres“ Objekt, unter dem Sie andere Objekte einordnen können. So können Sie die Hierarchie ganz einfach ordnen, indem Sie viele Objekte unter einer Gruppe zusammenfassen und diese dann zuklappen. Eine Gruppe ist auch eine Hilfe beim Bewegen von Objekten: Ordnen Sie viele Objekte unter einer Gruppe ein, und verschieben, drehen oder skalieren Sie dann die Gruppe mit dem Werkzeug Gizmo.

### ![](/icons/camera.webp) Kamera {#add-view}
Erstellt eine Kamera.

## Repeater {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeater sind Knoten, die Instanzen der Objekte unter ihnen erzeugen.

### ![](/icons/array.webp) Raster {#array}
![](/images/scene_primitive_array.webp)

Objekte, die Sie zu Unterknoten dieses Knotens machen, werden in einem Raster instanziiert. Ist der Knoten ausgewählt, bietet er diese Einstellungen:
* `Innerhalb einpassen` - wenn aktiv, werden alle Kopien innerhalb der Grenzen des Rasters platziert; wenn nicht, legen die Regler den Abstand zwischen den Kopien fest
* `Anzahl X/Y/Z` - die Anzahl der Instanzen auf jeder Achse
* `Größe X/Y/Z` - die Größe des Rasters entlang jeder Achse, oder der Abstand zwischen den Kopien, wenn `Innerhalb einpassen` aus ist
* `Randomisieren...` - fügt den Kopien zufällige Variationen hinzu, siehe [Randomisieren](#curve) unten.

### ![](/icons/curve.webp) Kurve {#curve}
![](/images/scene_primitive_curve.webp)
Erstellt eine Kurve; die Unterknoten dieses Knotens werden entlang der Kurve wiederholt. Ist der Knoten ausgewählt, bietet er diese Einstellungen:
* `Kurve` - bearbeitet die Kurve: Punkte hinzufügen und Punkte auf der Kurve verschieben.
* `Einblenden` - blendet die Kurve und ihre Punkte ein oder aus.
* `Einrasten` - lässt die Kurvenpunkte an anderer Geometrie einrasten.
* `Sym` - bearbeitet die Kurve symmetrisch.
* `Geschl.` - verbindet Anfang und Ende der Kurve, oder lässt sie offen.
* `B-Spline` - legt fest, ob die Instanzen der Kurve exakt folgen oder eine B-Spline-Interpolation mit glatteren Ergebnissen verwenden.
* `Verformen` - biegt jede Kopie entlang der Kurve, sodass die Kopien an ihre Nachbarn anschließen (`Glatt` biegt ihre Seiten so, dass sie ohne Knick aneinanderstoßen).
* `Ausrichten` - dreht die Kopien so, dass sie der Richtung der Kurve folgen.
* `Drehpunkt` - der Drehpunkt der Kopien: die Kurve selbst (`Kurve`) oder ihre Unterknoten.
* `Anzahl` - die Anzahl der Instanzen. Die Modus-Schaltfläche daneben wechselt zu `Abstand`: ein fester Abstand zwischen den Kopien, die Anzahl richtet sich dann nach der Länge der Kurve.
* `Radius` - Steuerelemente an jedem Kurvenpunkt, um die Skalierung der Instanzen festzulegen.
* `Verdrehen` - Steuerelemente an jedem Kurvenpunkt, um die Verdrehung der Instanzen festzulegen.
* `Abwechselnd` - dreht jede zweite Kopie um die Kurve: um 90° für Kettenglieder, um 180° für Blätter oder Reißverschlusszähne, um die gewählte `Achse`.
* `Spirale...` - windet die Kopien in mehreren Strängen um die Kurve (Seil, Zopf, Band...).
* `Randomisieren...` - fügt den Kopien zufällige Variationen hinzu; jede Zeile kann stattdessen bei jeder Kopie denselben Betrag hinzufügen.

Unter der Werkzeugleiste verschmilzt der Schalter `(Zusammenführen)` einen Punkt mit einem anderen, wenn Sie ihn darauf ziehen. `IK` (inverse Kinematik) lässt Sie die Kurve in Pose bringen: Ziehen Sie einen Punkt, und die verbundenen Punkte folgen. Tippen Sie auf einen Punkt, um ihn zu sperren oder zu entsperren, und drücken Sie lange, um alle zu sperren oder zu entsperren; gesperrte Punkte bleiben an ihrem Platz.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Die Unterknoten dieses Knotens werden kreisförmig instanziiert. Verschieben Sie das Unterobjekt, um den Radius dieses Repeaters zu ändern. Ist der Knoten ausgewählt, bietet er diese Einstellungen:
* RadialX/Y/Z - diese Schaltflächen legen die Achse des Kreises und die Anzahl der Instanzen fest.



### ![](/icons/mirror.webp) Spiegeln {#mirror}
![](/images/scene_primitive_mirror.webp)

Die Unterknoten dieses Knotens werden an einer Achse gespiegelt. Ist der Knoten ausgewählt, bietet er diese Einstellungen:
* Gizmo - aktiviert das Transformations-Gizmo, um den Mittelpunkt der Spiegelung festzulegen. Sie können ihn auch drehen und skalieren. Wenn Sie fertig sind, tippen Sie erneut auf Gizmo, um wieder die normalen Einstellungen zu sehen.
* X/Y/Z - legt die Spiegelebene fest

### ![](/icons/surface.webp) Oberfläche {#surface}

Die Unterknoten dieses Knotens werden auf die Oberfläche eines Objekts kopiert: eine Kopie pro Fläche, pro Kante oder pro Vertex, oder zufällig verstreut. Ist der Knoten ausgewählt, bietet er diese Einstellungen:
* Modus - setzt die Kopien auf die `Flächen`, die `Kanten` oder die Vertices, oder verteilt sie mit `Streuen`.
* Alle - eine Kopie alle N Flächen, Kanten oder Vertices. `Zufällig` wählt sie stattdessen zufällig aus, und `Neu verteilen` zieht eine neue zufällige Auswahl.
* Abstand - beim Streuen der Mindestabstand zwischen zwei Kopien.
* Ausrichten - die Kopien stehen auf der Oberfläche und folgen ihrer Normale, statt die Ausrichtung des Originals beizubehalten.
* Einrasten - projiziert das Original auf den nächstgelegenen Punkt der Oberfläche, die Kopien folgen.
* Größe anpassen, Scherung - skaliert und streckt die Kopien passend zur Form jeder Fläche.
* Verformen - biegt jede Kopie auf ihre Fläche oder entlang ihrer Kante, sodass benachbarte Kopien lückenlos aneinanderstoßen.

Alle Repeater haben die Schaltfläche `Abschließen`, die das Ergebnis des Repeaters festschreibt und fragt, wie das geschehen soll:
* Unterknoten kombinieren - die Instanzen werden zu einem einzigen Objekt zusammengefügt
* Instanzen beibehalten - die Instanzen bleiben Instanzen, haben aber keinen übergeordneten Repeater mehr
* Instanz aufheben - die Instanzen werden in eigenständige Objekte umgewandelt

`Alles auflösen` schreibt auch die in diesem Repeater verschachtelten Repeater fest, sodass jede Kopie zu einem einfachen Objekt wird.

::: tip Tipp: Repeater kombinieren
Repeater lassen sich untereinander verschachteln, und mehrere Objekte können Unterknoten von Repeatern sein. So entstehen komplexe Effekte.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tipp: Drehpunkte von Repeatern

Manche Repeater versuchen, den Drehpunkt der Unterobjekte automatisch zu setzen. Auch wenn Sie diese mit dem Werkzeug Gizmo verschieben oder drehen, bewegen sie sich dann nicht. Wenn Sie dieses Verhalten umgehen möchten, fügen Sie zwischen dem Repeater und dem Unterobjekt eine Gruppe ein. Nun können Sie die Form unabhängig vom Repeater bewegen.
:::

## Licht {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Gerichtet {#directional}
Erstellt ein gerichtetes Licht, eine unendlich weit entfernte Lichtquelle wie die Sonne.

### ![](/icons/panorama.webp) Umgebung {#environment}
Erstellt ein Umgebungslicht, das die Szene aus einem Bild rundherum beleuchtet (bildbasierte Beleuchtung, wie ein HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Erstellt ein Spotlicht, bei dem Sie Breite und Weichheit des Lichtkegels einstellen können

### ![](/icons/light.webp) Punkt {#point}
Erstellt ein Punktlicht

## ![](/icons/cog.webp) Erweitert {#advanced}
Die Schaltfläche `Erweitert` unten links im Panel öffnet ein Popup mit zwei Tabs: `Allgemein` und `Synchronisieren`.

### ![](/icons/focus.webp) UI: Element bei Doppeltippen fokussieren {#focus-on-item}
Ein Doppeltipp auf einen Eintrag in der Liste der Szene richtet die Kamera in der 3d-Ansicht auf diesen Eintrag aus.

### ![](/icons/eye_open.webp) Sichtbarkeit synchronisieren {#sync-visibility}
Wenn aktiv, wirkt das Augen-Icon eines ausgewählten Eintrags auf alle ausgewählten Einträge.

### ![](/icons/bang.webp) Hervorheben {#highlight}
Hebt die ausgewählten Objekte im Viewport hervor, wenn sich die Auswahl ändert.

### ![](/icons/link.webp) Einblenden (Instanz) {#instance-show}
Zeigt links in der Liste der Szene eine farbige Kapsel an, die Instanzen kennzeichnet.

### ![](/icons/preview.webp) Objektvorschauen {#object-previews}
Zeigt für jedes Objekt in der Liste der Szene ein gerendertes Vorschaubild an. Das entspricht der Vorschau-Schaltfläche über der Liste.

### Schweißradius {#weld-radius}
Unter dem Titel `Kombinieren` stehen `Positions-Schweißradius` und `UV-Schweißradius`: Punkte und UVs, die näher beieinanderliegen als diese Radien, werden verschmolzen. Beide lassen sich über ihr Kontrollkästchen abschalten. Das gilt für Kombinieren, Boolean, Trimmen, Dezimieren, das Neuvernetzen und den Dateiimport.

### Icons {#icons}
Legt die minimale und maximale `Größe` sowie die `Deckkraft` der Icons für Gruppen, Lichter, Kameras und Repeater im Viewport fest.

### ![](/icons/hierarchy.webp) Hierarchielinien {#hierarchy-lines}
Zeigt im Viewport eine Linie zwischen einem übergeordneten Objekt und seinen Unterknoten an. Wenn aktiv, können Sie außerdem einstellen:
* `Nomad-Pivot verwenden` - die Linien beginnen am Drehpunkt, den die Werkzeuge Transformieren und Gizmo verwenden. Ist die Option deaktiviert, nutzen sie den ursprünglichen Basis-Drehpunkt, der weit vom Mittelpunkt des Objekts entfernt liegen kann.
* `Stärke` - die Breite der Linien. Die Schaltfläche neben dem Regler fügt ihnen eine Kontur hinzu.
* Die Farbe der Linien.

### ![](/icons/link.webp) Synchronisieren {#sync}
Im Tab `Synchronisieren` legen Sie für jede Aktion (`Hinzufügen`, `Löschen`, `Sperren`, `Klonen`, `Instanz`, `Instanz aufheben`, `Kombinieren`, `Trennen` und `Boolean`) fest, ob sie auf alle Instanzen der Auswahl wirkt:
* `Auto` - folgt dem Kontrollkästchen `Synchronisieren` oben im Menü Szene.
* `Nein` - nur die ausgewählten Objekte.
* `Ja` - immer alle Instanzen.

Standardmäßig stehen `Kombinieren`, `Trennen` und `Boolean` auf `Ja` und die anderen auf `Auto`. `Zurücksetzen` stellt diese Standardwerte wieder her.

## Untere Werkzeugleiste {#bottom-toolbar}
Diese Icons blenden Gruppen, Lichter, Kameras, Repeater und Hierarchielinien im Viewport ein oder aus. Icons, die im Viewport angezeigt werden, können Sie antippen, um das jeweilige Element direkt auszuwählen und zu bearbeiten.
