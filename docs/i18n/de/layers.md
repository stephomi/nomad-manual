# ![](/icons/layer.webp) Ebenen 

Dieses Menü enthält den Ebenenstapel – eine Möglichkeit, Bearbeitungen an deinem Objekt nicht-destruktiv zu speichern – sowie viele Möglichkeiten, Ebenen zu kombinieren und wiederzuverwenden.

![](/images/layers_overview.webp) 

## Übersicht

Nomad-Ebenen erfüllen mehrere Zwecke.

Mal-Informationen (Farbe, Rauigkeit, Metallizität, Deckkraft) funktionieren mit Ebenen ähnlich wie in 2D-Malprogrammen. Eine Ebene kann erstellt und auf ein Modell bemalt werden. Die Ebene kann ein- oder ausgeschaltet werden, ihre Deckkraft kann angepasst werden, die Ebene kann dupliziert werden, ihre Reihenfolge im Ebenenstapel kann geändert und ihr Mischmodus angepasst werden.

Nomad verwendet Ebenen auch für das Sculpting. Eine Ebene kann feine Details wie Falten speichern oder große Änderungen, sodass sie wie Blendshapes/Shape Keys/Morph Targets in anderen 3D-Anwendungen funktionieren. Du könntest zum Beispiel verschiedene Gesichtsausdrücke auf unterschiedlichen Ebenen modellieren und dann die Ebenenregler anpassen, um sie zu neuen Ausdrücken zu kombinieren.

In diesem Fall sind die in einer Ebene gespeicherten Änderungen rein additiv, die Ebenenreihenfolge spielt – anders als bei Farbe – keine Rolle.

Ebenen können teilweise über das Werkzeug [Delete Layer](tools.md#delete-layer) gelöscht werden, und Ebenen können auch verwendet werden, um Masken basierend auf den verschiedenen in der Ebene gespeicherten Informationen zu erstellen.

![](/videos/layer.mp4)

::: tip
Anders als bei den meisten Sculpting-Programmen gehen Ebenen beim Ändern der Topologie eines Meshes nicht verloren. Du kannst den [Voxel Remesher](topology.md#voxel-remesher), die [Multiresolution](topology.md#multiresolution) oder die Werkzeuge [Trim](tools.md#trim)/[Split](tools.md#split) verwenden, beachte aber, dass bei Verwendung des [Voxel Remesher](topology.md#voxel-remesher) die Qualität der Ebene beeinträchtigt wird.
:::

::: tip
Wenn du Ebenen für Blendshapes/Morph Targets verwendest, gibt es zusätzliche Ebenenfunktionen im [Szenenmenü](scene.md#object-menu). Du kannst Ebenen in Objekte aufteilen und passende Objekte wieder in Ebenen kombinieren.
:::
----

## Ebenenmenü 

![](/images/layers_menu.webp)

Drücke `Add layer`, um eine neue Ebene zu erstellen.

Jede Ebene hat einen Namen, einen Schieberegler zur Steuerung ihrer Stärke/Faktors und Optionsschaltflächen.

### Optionen

| Action       | Icon                         | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Show/hide the layer                                 |
| Blend Mode   | ![](/icons/opacity.webp)    | The photoshop style blending mode. The 4 icons display the modes for Color, Roughness, Metalness, Opacity.                                 |
| Edit Name    | ![](/icons/pencil.webp)     | Edit the layer name                                 |
| Delete       | ![](/icons/trash.webp)      | Delete the layer                                    |
| Duplicate    | ![](/icons/clone.webp)      | Duplicate the layer                                 |
| Merge Down   | ![](/icons/merge_down.webp) | Merge the layer with the lower layer (or base mesh) |
| More         | ![](/icons/more.webp)       | [More...](#more) options                            |

Um eine Ebene an eine andere Stelle im Ebenenstapel zu verschieben, drücke und halte ihren Namen und ziehe sie dann.

### More...

Die Schaltfläche „More...“ zeigt zusätzliche Optionen für die aktuelle Ebene an:

![](/images/layers_more.webp) 

#### Channel factors

Mit diesen Reglern kannst du die Menge an Sculpt/Farbe/Rauigkeit/Metallizität/Deckkraft für die Ebene skalieren. Diese Werte werden mit dem Ebenenfaktor-Schieberegler multipliziert. Wenn zum Beispiel die Ebenenstärke 1 beträgt, der Farbkanalfaktor aber 0,5, wird die angezeigte Farbe mit einer Stärke von 0,5 dargestellt.

`Offset` steuert die Sculpt-Stärke der Ebene. Während Farbe/Rauigkeit/Metallizität zwischen 0 und 1 begrenzt sind, kann Offset jeden Wert annehmen, sowohl positiv als auch negativ. 

::: tip
Offset kann verwendet werden, um eine Ebene mit Erhebungen in eine Ebene mit Vertiefungen zu verwandeln oder ein Lächeln in ein Stirnrunzeln:
![](/videos/layer_happysad.mp4)


Eine symmetrische Ebene kann geklont und dann mit Del Layer in linke/rechte Formen aufgeteilt werden:
![](/videos/layer_leftright.mp4)

Ebenen mit negativen Offset-Faktoren können auf leere Ebenen gebacken werden, um neue positive Formen zu erzeugen.

Ebenen mit positiven Offset-Faktoren über 1 können verwendet werden, um mit extremeren Blendshapes zu experimentieren.
:::

::: warning
Im Moment teilen sich Ebenen nur einen einzigen Deckkraftkanal für alle 3 Kanäle (Farbe/Metallizität/Rauigkeit).
Wenn du mehrere Ebenen mit kanalweiser Intensität zusammenführst, die nicht auf voller Intensität stehen, kann es sein, dass das Endergebnis anders aussieht.

Möglicherweise wird in Zukunft jeder Kanal seinen eigenen Alphakanal haben, um diese Einschränkung zu beseitigen.
:::


#### ![](/icons/tool_mask.webp) Mask
Die Masken-Schaltfläche neben jedem Schieberegler erstellt eine Maske aus diesem Kanal. Ähnlich wie die Verwendung von Ebenen zur Auswahl in Malprogrammen ermöglicht dies, Arbeiten, die du in einer Ebene erledigt hast, für andere Operationen wiederzuverwenden.

#### ![](/icons/preview.webp) Preview
![](/images/layers_preview.webp) 

Wenn aktiviert, werden die Extraktions-Einstellungen für diese Ebene in der Vorschau angezeigt (siehe nächsten Abschnitt).

Wenn X-Ray aktiviert ist, wird nur die extrahierte Form solide dargestellt, der Rest der Form wird transparent gemacht – nützlich, wenn du negative Extraktionshöhen verwendest.

#### Extract
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Die Schaltfläche `Extract` dupliziert den Inhalt der Ebene in ein neues Objekt, normalerweise mit einer vom Benutzer festgelegten Dicke, die im nächsten Abschnitt eingestellt wird.

`Closing action` bestimmt, wie die Duplizierung durchgeführt wird:

* None - Extrahiert einfach den Teil, ohne zu versuchen, Seiten zu erzeugen oder Löcher zu füllen.
* Fill - Das Loch wird mit Dreiecken gefüllt und geglättet. Verwende diese Option nicht für flache Oberflächen.
* Shell - Schließt die extrahierte Form mit den Optionen für Dicke und Richtung.
* Layer - Extrahiert die Ebenendifferenz.

#### ![](/icons/height.webp) Thickness
![](/images/layers_thickness.webp) 

Die Tiefe der Shell-Extrusion. Positive Werte wachsen aus der Oberfläche heraus, negative Werte wachsen in die Oberfläche hinein.

Das Plus/Minus neben diesem Wert legt die Richtung der Extrusion fest:
* Minus ( - ) beginnt an der aktuellen Oberfläche und extrudiert nach unten. 
* Plus ( + ) beginnt an der aktuellen Oberfläche und extrudiert nach oben.
* PlusMinus ( ± ) verschiebt Ober- und Unterseite der Extrusion gleichermaßen nach außen, sodass sie zur Hälfte in der ursprünglichen Oberfläche eingebettet ist.

#### Smoothness
![](/images/layers_smoothness.webp) 

Wenn die Kanten des zu extrahierenden Bereichs ausgefranst sind, versucht dieser Schieberegler, die Kante in eine glattere Form zu verwischen. 

#### ![](/icons/height.webp) Edge loop (side)
![](/images/layers_edgeloop.webp) 

Dieser Abschnitt ist sichtbar, wenn die Closing Action „Shell“ ist. 

`Auto Edge-loop (side)` berechnet die Anzahl der Edge-Loops entlang der Shell-Seiten, um quadratische Polygone zu erzeugen. 

Wenn deaktiviert, legt der `Division`-Schieberegler die Anzahl der Unterteilungen an den Seiten fest.

_Dies ist das Ende des „More...“-Untermenüs._

### Advanced
![](/images/layers_advanced.webp)

#### Keep top layers details

Stellt sicher, dass kleine Details auf höheren Ebenen sichtbar bleiben, wenn große Änderungen an unteren Ebenen vorgenommen werden.

Standardmäßig gehen kleine Faltendetails auf einer Ebene verloren, wenn du anschließend große Änderungen an der Basisebene vornimmst. Durch Aktivieren dieser Option bleiben diese kleinen Details immer über den großen Änderungen der unteren Ebenen „schwebend“. Im folgenden Video siehst du, wie die Faltendetails standardmäßig entfernt werden, aber sichtbar bleiben, wenn „keep top layers details“ aktiviert ist:

![](/videos/layers_details.mp4)


#### UI: Expand list

Das Standard-Ebenenmenü ermöglicht es dir, die Ebenensichtbarkeit und die Ebenendeckkraft umzuschalten. Wenn du diese Option aktivierst, werden die vollständigen Bedienelemente für jede Ebene eingeblendet.

![](/images/layers_expand.webp)

#### Sync transform

Wenn aktiviert, werden alle nicht ausgewählten Ebenen entsprechend der Transformationsrotation, -skalierung und -schrägung angepasst. 

Deaktiviere diese Option, wenn die anderen Ebenen ohne die neue Transformation verwendet werden sollen, die du anwendest.

Wenn auf `Auto` gesetzt, werden nur die sichtbaren Ebenen angepasst.
