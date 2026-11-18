# ![](/icons/layer.webp) Layer {#layers}

Dieses Menü enthält den Ebenenstapel, mit dem Sie Änderungen an Ihrem Objekt nicht-destruktiv speichern, und bietet viele Möglichkeiten, Ebenen zu kombinieren und weiterzuverwenden.

![](/images/layers_overview.webp) 

## Überblick {#overview}

Ebenen erfüllen in Nomad mehrere Aufgaben.

Malinformationen (Farbe, Rauheit, Metallizität, Deckkraft) funktionieren mit Ebenen ähnlich wie in 2d-Malprogrammen. Sie können eine Ebene anlegen und darauf ein Modell bemalen. Die Ebene lässt sich ein- und ausblenden, ihre Deckkraft anpassen, sie lässt sich duplizieren, im Ebenenstapel verschieben, und ihr Mischmodus lässt sich ändern.

Nomad nutzt Ebenen auch zum Sculpten. Eine Ebene kann feine Details wie Falten speichern oder auch große Änderungen, sodass sie wie Blendshapes/Shape Keys/Morph Targets in anderen 3d-Programmen funktioniert. Sie könnten zum Beispiel verschiedene Gesichtsausdrücke auf verschiedenen Ebenen sculpten und sie über die Ebenenregler zu neuen Ausdrücken kombinieren.

In diesem Fall wirken die in einer Ebene gespeicherten Änderungen rein additiv: Anders als beim Malen spielt die Reihenfolge der Ebenen keine Rolle.

Ebenen lassen sich mit dem Werkzeug [EbeneEntf](tools.md#delete-layer) teilweise radieren, und Sie können aus den verschiedenen in einer Ebene gespeicherten Informationen auch Masken erzeugen.

![](/videos/layer.mp4)

::: tip
Anders als in den meisten Sculpting-Programmen gehen die Ebenen nicht verloren, wenn Sie die Topologie eines Meshes ändern. Sie können das [Voxel-Remeshing](topology.md#voxel-remesher), die [Multiauflösung](topology.md#multiresolution) oder die Werkzeuge [Trimmen](tools.md#trim)/[Teilen](tools.md#split) verwenden. Beachten Sie aber, dass beim [Voxel-Remeshing](topology.md#voxel-remesher) die Qualität der Ebene leidet.
:::

::: tip
Wenn Sie Ebenen für Blendshapes/Morph Targets verwenden, finden Sie im [Szene-Menü](scene.md#object-menu) zusätzliche Ebenenfunktionen: Sie können Ebenen in Objekte aufteilen und passende Objekte zu Ebenen zusammenfassen.
:::
----

## Layer-Menü {#layer-menu}

![](/images/layers_menu.webp)

Der Titel zeigt den Namen des ausgewählten Objekts. Für Grundformen sind keine Ebenen verfügbar; validieren Sie die Grundform also zuerst.

Tippen Sie auf `Layer hinzufügen`, um eine neue Ebene anzulegen. `Layer zusammenführen` führt alle Ebenen in das Basis-Mesh zusammen; die Zahl neben dem Icon gibt an, wie viele Ebenen es gibt.

Jede Ebene hat einen Namen, einen Regler für ihre Stärke bzw. ihren Faktor und Optionsschaltflächen. Tippen Sie auf eine Ebene, um sie zur aktiven Ebene zu machen: Sculpting und Bemalung landen dann in dieser Ebene. Tippen Sie auf `Basis`, um wieder am Basis-Mesh zu arbeiten.

### ![](/icons/sort_right.webp) Liste aufklappen {#ui-expand-list}

Standardmäßig zeigt die Ebenenliste nur Sichtbarkeit, Mischmodus und Stärke jeder Ebene; die aktive Ebene ist mit allen Steuerelementen aufgeklappt. Der Pfeil links neben dem Titel klappt die vollständigen Steuerelemente für alle Ebenen auf.

![](/images/layers_expand.webp)

### Optionen {#options}

| Aktion       | Symbol                       | Beschreibung                                        |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Sichtbar     | ![](/icons/eye_open.webp)   | Blendet die Ebene ein/aus                           |
| Mischmodus   | ![](/icons/opacity.webp)    | Der Mischmodus wie in Photoshop. Die 4 Icons zeigen die Modi für Farbe, Rauheit, Metallizität und Deckkraft. |
| Name bearbeiten | ![](/icons/pencil.webp)  | Bearbeitet den Namen der Ebene                      |
| Löschen      | ![](/icons/trash.webp)      | Löscht die Ebene                                    |
| Duplizieren  | ![](/icons/clone.webp)      | Dupliziert die Ebene                                |
| Abwärts zusammenfügen | ![](/icons/merge_down.webp) | Führt die Ebene mit der darunterliegenden Ebene (oder dem Basis-Mesh) zusammen |
| Mehr         | ![](/icons/more.webp)       | Optionen unter [Mehr…](#more)                       |

Ist eine Ebene nicht aufgeklappt, finden Sie `Name bearbeiten`, `Löschen`, `Duplizieren` und `Abwärts zusammenfügen` in ihrem Menü [Mehr…](#more).

Um eine Ebene an eine andere Stelle im Ebenenstapel zu verschieben, halten Sie ihren Namen gedrückt und ziehen Sie sie.

### Basis {#base}

Die Schaltfläche mit den 3 Punkten in der Zeile `Basis` verschiebt die Bemalung des Basis-Meshes über die Schaltfläche `Basis → Ebene` in eine neue Ebene. Die Basis wird dann auf das Hintergrundmaterial zurückgesetzt. Das ist praktisch, wenn Sie schon viel gemalt haben, bevor Sie überhaupt eine Ebene angelegt haben.

* Die Masken- und Ausblenden-Schaltflächen daneben lassen maskierte und ausgeblendete Bereiche unverändert.
* `Extrahieren` - die zu verschiebenden Kanäle: `Farbe`, `Deckkraft`, `Matt` und `Metallisch`.
* `Hintergrundmaterial` - wenn aktiviert, werden nur die Werte verschoben, die von diesem Material abweichen. Stellen Sie es mit den Reglern ein oder nehmen Sie es mit der Pipette vom Modell auf.

### ![](/icons/more.webp) Mehr… {#more}

Die Schaltfläche „Mehr…“ zeigt zusätzliche Optionen für die aktuelle Ebene, verteilt auf zwei Tabs: die Einstellungen (Zahnrad-Icon) und die Extraktion (Würfel-Icon).

![](/images/layers_more.webp) 

#### Kanalfaktoren {#channel-factors}

Mit diesen Steuerelementen skalieren Sie den Anteil von Sculpting, Farbe, Rauheit, Metallizität und Deckkraft der Ebene. Diese Werte werden mit dem Faktor-Regler der Ebene multipliziert: Ist die Stärke der Ebene zum Beispiel 1, der Faktor des Farbkanals aber 0,5, wird die Farbe mit der Stärke 0,5 angezeigt.

`Versatz` steuert die Sculpting-Stärke der Ebene. Während Farbe, Rauheit und Metallizität auf Werte zwischen 0 und 1 begrenzt sind, kann der Versatz jeden beliebigen positiven oder negativen Wert annehmen.

::: tip
Mit dem Versatz können Sie aus einer Ebene mit Beulen eine Ebene mit Vertiefungen machen, oder aus einem Lächeln ein Stirnrunzeln:
![](/videos/layer_happysad.mp4)


Eine symmetrische Ebene lässt sich klonen und dann mit EbeneEntf in eine linke und eine rechte Form aufteilen:
![](/videos/layer_leftright.mp4)

Ebenen mit negativem Versatzfaktor lassen sich in leere Ebenen einbacken, um neue positive Formen zu erhalten.

Ebenen mit positivem Versatzfaktor über 1 eignen sich, um mit extremeren Blendshapes zu experimentieren.
:::

::: warning
Derzeit teilen sich Ebenen einen einzigen Deckkraftkanal für alle 3 Kanäle (Farbe/Metallizität/Rauheit).
Wenn Sie mehrere Ebenen mit kanalweiser Stärke zusammenführen, die nicht auf voller Stärke stehen, kann das Endergebnis anders aussehen.

Vielleicht erhält in Zukunft jeder Kanal seinen eigenen Alphakanal, um diese Einschränkung aufzuheben.
:::


#### ![](/icons/shield.webp) Maske {#mask}
Die Masken-Schaltfläche neben jedem Regler erzeugt aus diesem Kanal eine Maske. Ähnlich wie Sie in Malprogrammen Ebenen für Auswahlen nutzen, können Sie so die Arbeit in einer Ebene für andere Operationen weiterverwenden.

#### ![](/icons/preview.webp) Vorschau {#preview}
![](/images/layers_preview.webp) 

Die folgenden Optionen befinden sich im Extraktions-Tab des Menüs „Mehr…“.

Ist diese Option aktiviert, zeigt sie eine Vorschau der Extraktionseinstellungen für diese Ebene (siehe nächster Abschnitt).

`Röntgen` wählt, welche Objekte während der Vorschau transparent dargestellt werden (`Keine`, `Nicht ausgewählt`, `Ausgewählt` oder `Alle`), damit die extrahierte Form massiv bleibt. Das ist nützlich, wenn Sie negative Extraktionshöhen verwenden.

#### ![](/icons/mask_extract.webp) Extrahieren {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Die Schaltfläche `Extrahieren` dupliziert den Inhalt der Ebene in ein neues Objekt, meist mit einer selbst gewählten Stärke, die Sie im nächsten Abschnitt festlegen.

`Schließen` bestimmt, wie die Duplizierung erfolgt:

* `Keine` - Extrahiert einfach den Teil, ohne Seiten zu erzeugen oder Löcher zu füllen.
* `Füllen` - Das Loch wird mit Dreiecken gefüllt und geglättet. Verwenden Sie diese Option nicht für flache Oberflächen.
* `Hülle` - Schließt die extrahierte Form mit den Optionen für Stärke und Richtung.
* `Ebene` - Extrahiert die Differenz der Ebene.

#### ![](/icons/height.webp) Höhe {#thickness}
![](/images/layers_thickness.webp) 

Die Tiefe der Extrusion der Hülle. Positive Werte wachsen aus der Oberfläche heraus, negative Werte in die Oberfläche hinein. Diese Option ist ausgeblendet, wenn `Ebene` als Abschluss gewählt ist.

Plus/Minus neben diesem Wert legt die Richtung der Extrusion fest:
* Minus ( - ) beginnt an der aktuellen Oberfläche und extrudiert nach unten.
* Plus ( + ) beginnt an der aktuellen Oberfläche und extrudiert nach oben.
* PlusMinus ( ± ) schiebt Ober- und Unterseite der Extrusion gleich weit auseinander, sodass sie zur Hälfte in der ursprünglichen Oberfläche steckt.

#### Seiten {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Dieser Abschnitt ist sichtbar, wenn `Hülle` als Abschluss gewählt ist.

`Wandunterteilungen` legt die Anzahl der Unterteilungen entlang der Seiten der Hülle fest. Ist der Schalter `Auto` aktiviert, berechnet Nomad die Anzahl der Kantenschleifen so, dass quadratische Polygone entstehen.

#### Glätte {#smoothness}
![](/images/layers_smoothness.webp) 

Wenn die Ränder des zu extrahierenden Bereichs gezackt sind, aktivieren Sie diese Option, um sie zu einer schöneren Form zu glätten. `Alle` glättet die gesamte extrahierte Oberfläche, `Nur Kanten` glättet ihre Ränder. `Iterationen` legt fest, wie stark geglättet wird.

_Hier endet das Untermenü „Mehr…“._

### ![](/icons/cog.webp) Erweitert {#advanced}
![](/images/layers_advanced.webp)

Die Schaltfläche `Erweitert` unten im Menü erscheint, sobald das Objekt Ebenen hat.

#### Details der oberen Ebenen erhalten {#keep-top-layers-details}

Sorgt dafür, dass kleine Details auf höheren Ebenen sichtbar bleiben, wenn Sie große Änderungen auf tieferen Ebenen vornehmen. Während Sie sculpten, wird die Verformung durch die oberen Ebenen ignoriert, ihre Details bleiben aber sichtbar. Das funktioniert nur gut, wenn diese oberen Ebenen relativ kleine Details enthalten.

Wenn Sie standardmäßig kleine Falten auf einer Ebene sculpten und danach große Änderungen an der Basis vornehmen, gehen die Falten verloren. Mit dieser Option schweben diese kleinen Details stets über den großen Änderungen darunter. Im folgenden Video sehen Sie, wie die Falten standardmäßig verschwinden, aber sichtbar bleiben, wenn „Details der oberen Ebenen erhalten“ aktiviert ist:

![](/videos/layers_details.mp4)


#### Transformation synchronisieren {#sync-transform}

Ist diese Option aktiviert, werden alle nicht ausgewählten Ebenen an Rotation, Skalierung und Scherung der Transformation angepasst, wenn Sie die Werkzeuge Gizmo oder Transformieren verwenden. Mögliche Werte sind `Auto`, `Nein` oder `Ja`.

Deaktivieren Sie diese Option, wenn die anderen Ebenen ohne die neue Transformation verwendet werden sollen, die Sie gerade anwenden.

Bei `Auto` werden nur die sichtbaren Ebenen angepasst.
