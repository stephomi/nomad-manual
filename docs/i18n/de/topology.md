# ![](/icons/multires.webp) Topologie {#topology}

Dieses Menü steuert die Topologie der Objekte in Nomad und enthält Werkzeuge, um Details zwischen Objekten sowie zwischen Texturen zu backen und zu übertragen.

![](/images/topology_overview.webp)

Nomad arbeitet mit Polygonen: Die Geometrie besteht aus Dreiecken und Vierecken (Quads).
Mit Topologie meinen wir sowohl die Anzahl der Flächen als auch die Art, wie die Punkte (Vertices) miteinander verbunden sind.

Es ist wichtig, die Topologie im Blick zu behalten, besonders wenn Sie feine Details modellieren oder malen möchten.

::: tip Wie behalte ich die Topologie im Blick?
Sie können das [Drahtgitter](settings.md#wireframe) einblenden oder einfach das [Smooth Shading](settings.md#smooth-shading) ausschalten.
:::

![](/images/topology_top.webp)

Das Menü Topologie von Nomad hat mehrere Tabs in zwei Reihen:

| Methode                                     | Icon                         | Beschreibung                                                      |
| :-----------------------------------------: | :--------------------------: | :---------------------------------------------------------------: |
| [Multiauflösung](#multiresolution)          | ![](/icons/multires.webp)   | Mehrere Detailstufen über Unterteilung bearbeiten                 |
| [Voxel Remeshing](#voxel-remesher)          | ![](/icons/voxel.webp)      | Eine neue Topologie mit gleichmäßiger Dichte berechnen            |
| [Dynamische Topologie](#dynamic-topology)   | ![](/icons/dynamic.webp)    | Beim Modellieren oder Malen in Echtzeit lokal Flächen hinzufügen oder entfernen |
| [Verschiedenes](#misc)                      | ![](/icons/topo_extra.webp) | Löcher schließen, Manifold erzwingen und in Triplanar umwandeln   |
| [Grundformen](#primitive)                   | ![](/icons/dot.webp)        | Optionen der Grundform                                            |
| [Dezimieren](#decimation)                   | ![](/icons/decimate.webp)      | Die Anzahl der Flächen verringern und dabei die Form erhalten  |
| [Quad-Neuvernetzung](#quad-remesh)          | ![](/icons/quad.webp)       | Das Objekt mit einer sauberen Quad-Anordnung neu aufbauen         |
| [UV-Unwrapping](#uv-unwrap)                 | ![](/icons/uv.webp)         | UVs zum Texturieren erstellen                                     |
| [Backen](#bake)                             | ![](/icons/bake.webp)       | Details und Bemalung in Texturen, Vertices oder VDM-Stempel backen |


## Polygonstatistik {#polygon-stats}

![](/images/topology_stats.webp)

Der obere Bereich jedes Tabs zeigt die Polygonzahlen des ausgewählten Objekts und, wenn die Szene mehr als ein Objekt hat, der gesamten Szene. Die Spalten sind die Anzahl der Vertices, Dreiecke, Vierecke (Polygone mit 4 Seiten) und UV-Koordinaten (0, wenn das Objekt keine UVs hat).

Tippen Sie auf diesen Bereich, um alle Objekte der Szene mit ihren genauen Zahlen aufzulisten, einschließlich ihrer Anzahl an Face-Gruppen.

## ![](/icons/cog.webp) Zahnradmenü {#gear-menu}
Manche Bereiche, etwa in den Tabs [Quad-Neuvernetzung](#quad-remesh) und [Backen](#bake), haben zusätzliche Optionen. Öffnen Sie sie über das Zahnrad-Icon neben dem Titel des Bereichs.

## ![](/icons/multires.webp) Multiauflösung {#multiresolution}

![](/images/topology_multires_menu.webp)

### Was ist Multiauflösung? {#what-is-multiresolution}
Die Multiauflösung ist vor allem in zwei Situationen nützlich:
- Der glättende Unterteilungsalgorithmus erhöht die Polygonzahl Ihres Objekts
- Mehrere Auflösungsstufen erlauben es Ihnen, zwischen kleinen und großen Änderungen zu wechseln

![](/videos/multiresolution.mp4)

#### Arbeiten mit Multiauflösung {#multiresolution-workflow}
Ein wichtiger Vorteil der Multiauflösung: Sie können zu einer niedrigeren Auflösung zurückgehen, Ihr Objekt dort ändern und dann zur höchsten Auflösung zurückkehren, ohne die hochaufgelösten Details zu verlieren. Alle hochaufgelösten Details werden automatisch übertragen.

[Layer](layers.md#layers) stehen auf jeder Auflösungsstufe zur Verfügung.

::: warning
Wenn Sie ein Werkzeug verwenden, das die Topologie Ihres Objekts verändert, verlieren Sie alle anderen Auflösungsstufen Ihres Objekts!
In diesem Fall sollten Sie immer eine Warnung erhalten, zum Beispiel wenn Sie Folgendes verwenden:
- das [Voxel Remeshing](#voxel-remesher)
- die [Dynamische Topologie](#dynamic-topology)
- das [Werkzeug Trimmen](tools.md#trim)
- das [Werkzeug Teilen](tools.md#split)
:::


### Regler der Multiauflösung {#multiresolution-slider}
Dieser Regler zeigt die Anzahl der Unterteilungsstufen des aktuellen Objekts. Bei 6 senkrechten Balken gibt es 6 Unterteilungsstufen. Der Kreis zeigt die aktuell angezeigte Unterteilungsstufe.

Kleine Icons über dem Regler zeigen, welche Optionen (`Ebene 0 sperren`, `Linear`, `Scharfe Kante`, `Dreiecke behalten`) bei jeder Stufe verwendet wurden.

### Umkehren {#reverse}
Auf der niedrigsten Unterteilungsstufe versucht die Schaltfläche Umkehren, eine Stufe unterhalb der aktuellen zu erzeugen. Das gelingt in der Regel nur, wenn das Objekt ursprünglich durch Unterteilung entstanden ist, etwa in Nomad oder in anderen 3d-Anwendungen mit Multiresolution-Subdivision-Surfaces.

### Unterteilen {#subdivide}
Die Schaltfläche *Unterteilen* vervierfacht die Anzahl der Polygone. Behalten Sie also die Polygonzahl im Auge, denn sie kann sehr schnell wachsen! Nomad fragt nach einer Bestätigung, wenn das Ergebnis sehr schwer würde.
Eine wichtige Eigenschaft von *Subdivision Surfaces* ist, dass sie sich einer *glatten Oberfläche* annähern.
Um zu verstehen, wie das funktioniert, probieren Sie die Schaltfläche *Unterteilen* an einem Objekt mit nur wenigen Polygonen aus.

Mit der Option `Linear` können Sie dieses *glättende* Verhalten abschalten.

### Niedrigere löschen {#delete-lower}
Löscht die Unterteilungsstufen unterhalb der aktuell angezeigten Stufe, falls vorhanden. Wenn Ihnen das versehentlich passiert, können Sie sie mit der Schaltfläche Umkehren wiederherstellen.

### Höhere löschen {#delete-higher}
Löscht die Unterteilungsstufen oberhalb der aktuell angezeigten Stufe, falls vorhanden.

### ![](/icons/lock.webp) Ebene 0 sperren {#lock-lv0}
Erhält die Form der niedrigsten Unterteilungsstufe, wenn Sie auf höheren Stufen modellieren. Bemalung wird weiterhin bis auf Stufe 0 übertragen. Das kann wichtig sein, wenn Ihr Objekt in einer anderen Anwendung erstellt wurde und das Basisobjekt unverändert bleiben muss.

Diese Option ist nur vor der ersten Unterteilung verfügbar. Ist sie aus, verschieben große Änderungen auf höheren Unterteilungsstufen auch die Stufe 0.

### ![](/icons/linear.webp) Linear {#linear-subdivision}
Unterteilt das Mesh, ohne es zu glätten.

### ![](/icons/group.webp) Scharfe Kante {#sharp-border}
Wenn Ihr Objekt Face-Gruppen hat, bleiben mit dieser Option die Grenzen der Face-Gruppen scharf. Die Option lässt sich für jede Unterteilungsstufe einzeln setzen (der Unterteilungsregler zeigt dann ein kleines Icon über der Stufe an).

### ![](/icons/triangle.webp) Dreiecke behalten {#keep-triangles}
Die meisten üblichen Subdivision-Surface-Systeme versuchen, bei der Unterteilung alle Polygone in Vierecke umzuwandeln. Dieser Schalter zwingt die Unterteilung, stattdessen Dreiecke zu verwenden.

::: tip

Die Unterteilung glättet standardmäßig alle scharfen Kanten. Um Kanten etwas scharf zu halten, experimentieren Sie mit `Linear` oder `Scharfe Kante` auf den ersten 2 Unterteilungsstufen, und schalten Sie die Option für die höheren Stufen wieder aus. So entsteht ein halbscharfes, unterteiltes Mesh.

:::

### Höchste Stufe zeigen {#show-highest-level}
Zeigt die höchste Stufe mit allen Details an, während Sie auf einer niedrigeren Stufe modellieren. Praktisch, um das Endergebnis zu sehen, während Sie große Änderungen vornehmen.

### Drahtgitter: Nur Ebene 0 {#wireframe-level-0-only}
Wenn das [Drahtgitter](settings.md#wireframe) eingeschaltet ist, wird nur das Drahtgitter der niedrigsten Stufe angezeigt. Das dichte Drahtgitter der hohen Stufen kann die Form verdecken.


## ![](/icons/voxel.webp) Voxel Remeshing {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Das `Voxel Remeshing` gibt dem gesamten Mesh eine gleichmäßige Auflösung, das heißt, alle Polygone haben ungefähr dieselbe Größe. Das ist sehr nützlich, wenn Sie sich keine Gedanken über die Topologie machen und einfach frei modellieren möchten.

Ein typischer Arbeitsablauf beginnt damit, mit dem `Voxel Remeshing` bei niedriger Auflösung eine grobe Form aufzubauen.
Tippen Sie einfach ab und zu auf *Netz neu berechnen*, wenn Sie das Mesh stark dehnen, um zu große Verzerrungen zu vermeiden.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Wie oben erwähnt, arbeitet Nomad mit Polygonen. Das `Voxel Remeshing` ist eine Ausnahme, bei der (vorübergehend) ein anderer Ansatz für die Neuvernetzung verwendet wird.

Ein großer Unterschied ist, dass der Voxel-Ansatz keine Selbstüberschneidungen zulässt; diese werden aufgelöst.
Außerdem unterstützt er keine Meshes mit Löchern.

Mit Löchern meinen wir nicht das `genus hole` (das „Loch“ eines Donuts), sondern Meshes, die nicht `watertight`/`closed` sind.
Das bedeutet in der Regel, dass vor dem Neuvernetzen alle Löcher gefüllt werden, ähnlich wie beim [Werkzeug Trimmen](tools.md#trim) oder der Funktion [Löcher füllen](#holes). Die Option [Löcher](#voxel-holes) weiter unten legt fest, wie.
:::

### ![](/icons/voxel.webp) Netz neu berechnen {#voxel-remesh}
Führt das Voxel Remeshing aus. Kleine Icons auf der Schaltfläche erinnern Sie daran, welche der folgenden Optionen aktiv sind.

### Auflösung {#voxel-resolution}
Die Größe der Voxel, mit denen gerechnet wird; höhere Werte ergeben mehr Details. Während Sie diesen Parameter ändern, wird ein Schachbrettmuster über das Mesh gelegt, das eine Vorschau des Ergebnisses gibt.

Die Pipette übernimmt die Auflösung aus der Dichte des Meshes an der Stelle, auf die Sie tippen. Die Würfel-Schaltfläche daneben stellt den Wert auf eine `Kantenlänge` in Welteinheiten um: Derselbe Wert ergibt dann auf jedem Objekt denselben Detailgrad.

### Multiresolution erstellen {#build-multiresolution}
Erstellt beim Voxel Remeshing niedrigere Multiauflösungs-Stufen. Wenn Sie die Auflösung mithilfe des Schachbrettmusters festlegen und Multiresolution erstellen auf 2 setzen, entspricht das Ergebnis im Detail dem Auflösungsregler, und im Tab Multiauflösung befindet es sich auf Stufe 2. Darunter liegen also Meshes mit niedrigerer Auflösung auf Stufe 1 und Stufe 0. So erhalten Sie gleichzeitig ein sauberes Mesh mit gleichmäßigen Polygonen und ein niedrig aufgelöstes Steuer-Mesh.

Bei hohen Auflösungen geht es außerdem schneller und braucht weniger Speicher. Bei niedriger Auflösung und vielen Stufen verlieren Sie aber Details.

::: tip Tipp: Multiresolution erstellen und Stabiles Glätten

Diese Option kann manchmal „Schleifen“ in der Geometrie erzeugen, die sich nur schwer glätten lassen und kleine Pickel verursachen. Wenn das passiert, aktivieren Sie „Stabiles Glätten“ in den Optionen des Werkzeugs Glätten.

:::

### Dünne Teile verdicken {#thicken-thin-parts}
Teile, die dünner als die Voxel sind, können beim Neuvernetzen zerbrechen oder verschwinden. Diese Option verdickt sie, damit sie erhalten bleiben; höhere Werte verdicken stärker. Nicht verfügbar mit `Scharfe Kanten` oder `Scharfe Grenze`.

### Löcher {#voxel-holes}
Wie Löcher vor dem Neuvernetzen geschlossen werden:

* `Füllen` - Jedes Loch wird für sich von seinem Rand aus geschlossen.
* `Form` - Löcher werden geschlossen, indem sie der umgebenden Oberfläche folgen, und offene Teile, die sich überschneiden, werden verbunden.

### ![](/icons/angle.webp) Scharfe Kanten {#keep-sharp-edges}
Richtet die neuen Punkte an scharfen Kanten des ursprünglichen Meshes aus. Das ist vor allem bei einfachen booleschen Operationen mit Grundformen nützlich und kann Verzerrungen erzeugen.

### ![](/icons/group.webp) Scharfe Grenze {#voxel-sharp-border}
Die neuen Flächen folgen den Grenzen der Face-Gruppen, und eine Grenze bleibt scharf, wo die Oberfläche entlang dieser Grenze einen Knick hat.

### ![](/icons/group_separate.webp) Gruppen getrennt halten {#keep-groups-separate}
Jede Face-Gruppe wird für sich neu vernetzt: Gruppen verschmelzen nie, und jede bleibt ein geschlossenes Stück in ihrer eigenen Gruppe. In diesem Modus wird keine Multiauflösung erstellt. Die Option ist verfügbar, wenn das Objekt mehrere Face-Gruppen hat.

## ![](/icons/dynamic.webp) Dynamische Topologie {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiauflösung und Voxel Remeshing sind in der Branche übliche Methoden, um die Topologie zu steuern. Bei beiden müssen Sie aber darauf achten, die Polygone nicht zu stark zu dehnen oder zu sehr zusammenzudrücken.

Die dynamische Topologie ist eine Alternative. Während Sie modellieren, fügt Nomad während des Pinselstrichs bei Bedarf Polygone hinzu oder entfernt sie: Wenn Sie kleine Details einarbeiten, entstehen genau dort viele kleine Polygone, und wenn Sie an anderer Stelle glätten, werden Polygone entfernt.

Beachten Sie, dass die dynamische Topologie Dreiecke statt Vierecke verwendet. Das kann etwas unordentlich aussehen, aber am besten schauen Sie sich das Drahtgitter gar nicht an: Konzentrieren Sie sich darauf, eine schöne Skulptur zu erstellen, ohne sich um die Topologie zu sorgen. Später können Sie mit einem der anderen Neuvernetzungswerkzeuge von Nomad ein sauberes Quad-Mesh erzeugen.

Im Video unten sehen Sie sie in Aktion.

![](/videos/dynamic.mp4)

### Aktiviert {#enabled}
Schaltet die dynamische Topologie ein. Unter den Reglern für Radius und Intensität des Pinsels erscheint ein Dyntopo-Icon, mit dem Sie Dyntopo für jedes Werkzeug einzeln ein- und ausschalten können. Das kann sich spürbar auf die Leistung auswirken, und Layer werden korrekt aktualisiert.

### Detail {#dyn-detail}
Steuert den Detailgrad. Wie er wirkt, hängt von der Auswahl unter „Detailgrad basierend auf...“ ab, siehe unten. Im Modus `Bildschirm` zeigt die Beschriftung die angestrebte Dreiecksgröße in Pixeln. Im Modus `Konstant` können Sie mit einer Pipette den Detailgrad aus der Dichte des Meshes an der Stelle übernehmen, auf die Sie tippen.

### Detailgrad basierend auf... {#detail-based-on}
| Methode    | Beschreibung                                                    |
| :--------: | :-------------------------------------------------------------: |
| Bildschirm | Der Detailgrad hängt davon ab, wie groß das Objekt auf dem Bildschirm ist. Der Detail-Regler steht bei 100 % oder höher für feine Details mit kleinen Dreiecken, oder bei 1 % für wenig Details mit großen Dreiecken. |
| Radius     | Der Radius des Werkzeugs bestimmt den Detailgrad. Verwenden Sie einen kleinen Radius für feine Details und einen großen Radius für wenig Details. Der Detail-Regler ist ein Multiplikator für dieses Verhältnis. |
| Konstant   | Der Detail-Regler bestimmt den Detailgrad, unabhängig von der Bildschirmgröße oder der Werkzeuggröße. Es ist derselbe Wert wie der Regler [Detail](#all-detail) von `Netz neu berechnen`. |

::: tip TIPP: Modus Radius

Um ein Gefühl dafür zu bekommen, wie der Modus Radius funktioniert, bewegen Sie den Detail-Regler mit einem Finger und ändern gleichzeitig mit einem anderen Finger den Radius des Werkzeugs. Sie sehen dann, wie beide zusammenhängen.

:::

### Bevorzuge... {#prefer}
| Methode         | Beschreibung          |
| :-------------: | :-------------------: |
| Geschwindigkeit | Bevorzugt die Leistung |
| Qualität        | Bevorzugt die Qualität |

Wenn Sie `Qualität` bevorzugen, gibt es zwei wesentliche Unterschiede:
- die Verfeinerung wird vor dem Modellieren angewendet, sodass beim Malen oder Modellieren sehr kleiner Details weniger Interpolationsartefakte entstehen
- die Verfeinerung läuft, bis sie den richtigen Detailgrad erreicht hat, statt schrittweise vorzugehen.

So wird die Topologie immer wie erwartet verfeinert, auch wenn Sie sehr kleine Details modellieren oder schnelle Striche ziehen.


### ![](/icons/pressure.webp) Druck auf Radius anwenden {#use-pressure-on-radius}
Nur relevant, wenn `Radius` aktiviert ist. Ist diese Option aktiv, entspricht der Detailgrad immer der Pinselgröße, auch wenn die Pinselgröße vom Stiftdruck abhängt.

### Strich-Falloff verwenden {#use-stroke-falloff}

Bezieht auch die Falloff-Kurve und das Alpha des Pinsels in die Dyntopo-Berechnung ein.

### Methode {#method}
Legt fest, wie die dynamische Topologie das Mesh verändert, sowohl beim Modellieren als auch bei [Netz neu berechnen](#dyn-remesh):

| Methode           | Beschreibung                                                          |
| :---------------: | :-------------------------------------------------------------------: |
| Vereinheitlichung | Kann Flächen hinzufügen und entfernen; dieser Modus wird im Video oben verwendet |
| Unterteilung      | Fügt nur neue Flächen hinzu, kann keine Flächen entfernen             |
| Dezimierung       | Entfernt nur Flächen, kann keine neuen Flächen hinzufügen             |

### ![](/icons/shield.webp) Maskierte Bereiche schützen {#protect-masked-area}
Maskierte Bereiche schützen die Topologie vor Änderungen.

### ![](/icons/normal.webp) Vertex-Extrapolation {#vertex-extrapolation}
Setzt die Punkte auf eine glatte Oberfläche, die der Krümmung in ihrer Umgebung folgt, statt flach auf die bestehenden Flächen.

### Detail {#all-detail}
Die Auflösung, die beim Neuvernetzen verwendet wird. Steht Dyntopo im Modus „Konstant“, ist es derselbe Wert wie der Detail-Regler oben in diesem Menü. Die Pipette übernimmt den Detailgrad aus der Dichte des Meshes an der Stelle, auf die Sie tippen.

### Netz neu berechnen {#dyn-remesh}
Vernetzt das ganze Objekt mit dem Dyntopo-Algorithmus neu. Für eine vollständige Neuvernetzung sollten Sie normalerweise das [Voxel Remeshing](#voxel-remesher) verwenden.

Ein Vorteil gegenüber den Voxeln ist allerdings, dass das Mesh nicht geschlossen sein muss und maskierte Bereiche geschützt werden. So können Sie besser steuern, wo mehr oder weniger Dichte entsteht.



## ![](/icons/topo_extra.webp) Verschiedenes {#misc}

![](/images/topology_misc_menu.webp)

Dieser Tab vereint Werkzeuge, um das Mesh zu bereinigen oder umzuwandeln: seine Löcher schließen, es zu einem Manifold machen oder es in ein Triplanar umwandeln.

### ![](/icons/hole.webp) Löcher {#holes}
![](/images/topology_holes_menu.webp)
Meistens wird Ihr Objekt wasserdicht sein, das heißt, das Mesh ist „geschlossen“.

Wenn Ihr Objekt Löcher hat, können Sie sie füllen.

![](/videos/hole_filling.mp4)

::: tip
Wenn Sie das Voxel Remeshing ausführen, werden alle Löcher automatisch geschlossen, egal ob Sie es auf 1 oder auf mehrere Meshes anwenden.
:::

#### Löcher schließen {#close-holes}
Schließt die Löcher.

#### Optionen {#holes-gear-menu}
Diese Optionen ändern, wie die Löcher gefüllt werden:

##### Face-Gruppe {#fill-face-group}
Legt die Face-Gruppe der neuen Flächen fest:

* `Gemischt` - Ein Loch, das von einer einzigen Face-Gruppe umgeben ist, übernimmt diese; ein Loch, das an mehrere Gruppen grenzt, erhält eine neue.
* `Neu` - Die gefüllten Löcher erhalten eine neue Face-Gruppe.
* `Wiederverwenden` - Jedes Loch übernimmt die Face-Gruppe, die es am meisten umgibt.

##### Detailgrad {#fill-detail}
Die Polygondichte, mit der das Loch gefüllt wird. Während Sie diesen Regler ziehen, wird ein Schachbrettmuster auf dem Modell angezeigt, das die verwendete Dreiecksgröße andeutet. Das Kontrollkästchen schaltet das ab, und es werden nur die vorhandenen Punkte verwendet. Das erzeugt meist lange, dünne Dreiecke über dem Loch, die sich schwer modellieren lassen.

##### Überbrücken {#fill-non-manifold}
Füllt ein Loch und die Inseln darin als eine einzige Fläche, statt jeden Rand einzeln zu füllen. Ein höherer Winkel überbrückt stärker gekrümmte Löcher. Das Kontrollkästchen schaltet die Option ab.

### ![](/icons/cog.webp) Manifold erzwingen {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Versucht, Non-Manifold-Kanten zu bereinigen. Das kann für externe Software nützlich sein, die keine Kanten unterstützt, an denen mehr als 2 Flächen hängen.

#### Reinigen {#clean}
Führt die Bereinigung aus.

#### Optionen {#force-manifold-gear-menu}
Diese Option ändert, wie das Mesh bereinigt wird:

##### Kleine Flächen löschen {#delete-small-faces}
Ein Schwellenwert, mit dem kleine Polygone entfernt und zusammengefügt werden. Aktivieren Sie ihn über sein Kontrollkästchen.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Wandelt das Mesh in eine [Triplanar](scene.md#triplanar)-Grundform um.
Dabei gehen wahrscheinlich viele Details verloren: Auch Layer, Bemalung und Multiauflösung gehen verloren.

#### Würfelform erzwingen {#force-cubic}
Macht das Triplanar zu einem Würfel. Andernfalls passt sich das Triplanar dem nächstliegenden Begrenzungsrahmen um Ihr Objekt an.

#### Konvertieren {#convert}
Führt die Umwandlung in Triplanar aus.

#### Auflösung {#triplanar-resolution}
Die Auflösung des Triplanar-Rasters; höhere Werte erhalten mehr Details.

## ![](/icons/decimate.webp) Dezimieren {#decimation}

![](/images/topology_decimation.webp)

Verringert die Anzahl der Polygone und versucht dabei, so viele Details wie möglich zu erhalten. Dabei werden Dreiecke verwendet.

Diese Funktion kann nützlich sein, wenn Sie für den 3d-Druck exportieren möchten.
Wenn Sie danach weiter modellieren möchten, sollten Sie sie aber eher nicht verwenden, da sie ungleichmäßige Dreiecke erzeugen kann.

Maskierte Bereiche werden nicht dezimiert.

![](/videos/decimate.mp4)

::: tip

Der [Quad Remesher](tools.md#quad-remesher) kann bei Objekten mit vielen Polygonen lange rechnen und schwer kontrollierbare Ergebnisse liefern. Wenn Sie das Mesh vorher mit [Face-Gruppen](tools.md#facegroup) und Dezimieren vorbereiten, läuft der Quad Remesher viel schneller, und Sie haben deutlich mehr Kontrolle über die Topologie.

* Teilen Sie das Mesh in Face-Gruppen auf, um Ihren idealen Quad-Fluss festzulegen.
* Entspannen Sie die Face-Gruppen, um glatte Grenzen zu erhalten.
* Dezimieren Sie. So entstehen an den Grenzen der Face-Gruppen keine dünnen oder verzerrten Flächen. Achten Sie darauf, dass unter `Grenzen bewahren` die Option `Face-Gruppe` aktiviert ist. Dann folgen die Dreieckskanten genau den Grenzen Ihrer Face-Gruppen.
* Achten Sie in den Optionen des Quad Remeshers darauf, dass Relax deaktiviert ist (Sie haben das Mesh ja bereits entspannt), dann sollten Sie gute Ergebnisse erhalten.

:::

### Dezimieren {#decimate}
Startet das Dezimieren.

Die Icons neben der Schaltfläche Dezimieren zeigen die folgenden Optionen und lassen Sie sie ein- und ausschalten. Der Prozentwert gibt an, wie stark die jeweilige Option wirkt.

* ![](/icons/palette.webp)  `Painting erhalten` - Setzt mehr Dreiecke dorthin, wo es Details in der Bemalung gibt.
* ![](/icons/triforce.webp) `Einheitliche Flächen` - Bevorzugt gleich große Dreiecke.
* ![](/icons/hole.webp)  `Loch` - Das Dezimieren versucht, Ränder an offener Geometrie und an Löchern unverändert zu lassen.
* ![](/icons/group.webp) `Face-Gruppe` - Das Dezimieren versucht, die Grenzen der Face-Gruppen unverändert zu lassen.
* ![](/icons/uv.webp) `UV` - Das Dezimieren versucht, die UV-Grenzen unverändert zu lassen.

### Zieldreiecke {#target-triangles}
Legt die angestrebte Anzahl an Dreiecken fest. Der Standardwert ist 50 %. Die Schaltfläche Prozent/Ziel wechselt zwischen einem Prozentwert und einer genauen Polygonzahl.

### Optionen {#decimate-gear-menu}
Jede Option hat ein Kontrollkästchen zum Ein- und Ausschalten und einen Wert für ihre Stärke:

#### ![](/icons/palette.webp) Painting erhalten {#preserve-painting}
Der Wert bestimmt, wie genau Details der Bemalung erhalten bleiben. Höhere Werte erhalten mehr von der Bemalung. Stellen Sie 0 ein, wenn Ihnen die Bemalung egal ist.

#### ![](/icons/triforce.webp) Einheitliche Flächen {#uniform-faces}
Höhere Werte erzeugen Dreiecke ähnlicher Größe.

#### Grenzen bewahren {#preserve-borders}
Verhindert, dass Ränder dezimiert werden. Gewichte lassen sich für die Ränder `Loch`, `Face-Gruppe` oder `UV` festlegen (`UV` erfordert ein Objekt mit UVs).

## ![](/icons/quad.webp) Quad-Neuvernetzung {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Baut das Objekt mit einer sauberen Quad-Anordnung neu auf. Dieser Tab bietet mehrere Remesher, jeder mit eigener Schaltfläche `Netz neu berechnen`, eigenem Regler `Zielvierecke` und eigenem Zahnradmenü. Probieren Sie sie an Ihrem Objekt aus, die Ergebnisse unterscheiden sich deutlich!

### Quad Remesher {#quad-remesher}
Derselbe Remesher wie das Werkzeug [Quad Remesher](tools.md#quad-remesher), entwickelt von [Exoside](https://exoside.com/). Er ist nur auf manchen Plattformen verfügbar und muss gekauft werden: Bis dahin zeigt die Schaltfläche `Netz neu berechnen` einen Einkaufswagen.

`Werkzeug auswählen` wechselt zum Werkzeug Quad Remesher, um Führungslinien zu zeichnen und die Dichte zu malen. Das Zahnradmenü enthält `Adaptive Quad-Anzahl`, `Adaptive Größe` (bei 100 % folgt die Quad-Größe der Krümmung, bei 0 % sind die Quads gleichmäßig), `Harte Kanten automatisch erkennen` und `Vertex umprojizieren`.

::: tip
Wo er verfügbar ist, liefert der Quad Remesher in der Regel die besten Ergebnisse und die meiste Kontrolle.
:::

### AutoRemesher {#autoremesher}
Ein alternativer Quad-Remesher mit Optionen, um Größe und Form der Quads an die Oberfläche anzupassen.

#### ![](/icons/cog.webp) Zahnradmenü des AutoRemesher {#autoremesher-gear-menu}
Das Zahnradmenü enthält diese erweiterten Optionen:

##### Kantenskalierung {#edge-scaling}
Skaliert die Größe der Quads; höhere Werte erzeugen größere Quads.

##### Adaptivität {#adaptivity}
Passt die Dichte der Quads an die Krümmung an. 0 erzeugt gleichmäßige Quads, 1 erzeugt in gekrümmten Bereichen kleinere Quads.

##### Anisotropie {#anisotropy}
Streckt die Quads entlang der flachsten Richtung der Oberfläche. 0 erzeugt quadratische Quads, 1 erzeugt längliche Quads an Röhren und Graten.

##### Scharfe Kante {#sharp-edge}
Kanten, die stärker als dieser Winkel geknickt sind, bleiben als scharfe Merkmale erhalten.

##### Normalen glätten {#smooth-normal}
Bei 0 bleibt die Oberfläche während der Neuvernetzung facettiert. Höhere Werte glätten die Oberfläche, indem sie die Vertex-Normalen berücksichtigen.

##### Maximale Lochfüllung {#autoremesher-max-fill-hole}
Der Algorithmus kann manchmal unerwünschte Löcher erzeugen. Hat ein Loch weniger Vertices als dieser Wert, wird es gefüllt.

### Instant Mesh {#quad-remesh-instant}
Vernetzt neu mit dem [Instant-Meshes-Algorithmus von Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Er analysiert den Fluss eines Meshes und erzeugt eine saubere Quad-Topologie.

#### Netz neu berechnen {#instant-remesh}
Startet die Neuvernetzung.

#### Zielvierecke {#target-quads}
Die Anzahl an Vierecken, die der Remesher zu erzeugen versucht.

#### ![](/icons/cog.webp) Zahnradmenü von Instant Mesh {#quad-remesh-instant-gear-menu}
Das Zahnradmenü enthält diese erweiterten Optionen:

##### Faltenwinkel {#crease-angle}
Ein Schwellenwert für scharfe Ecken, der die Neuvernetzung lenken soll. Aktivieren Sie ihn über sein Kontrollkästchen.

##### Maximale Lochfüllung {#max-fill-hole}
Der Algorithmus kann manchmal unerwünschte Löcher erzeugen. Hat ein Loch weniger Vertices als dieser Wert, wird es gefüllt.

### QuadriFlow {#quadriflow}
Vernetzt neu mit dem Algorithmus QuadriFlow, ein weiterer Weg zu einer sauberen Quad-Anordnung.

#### ![](/icons/cog.webp) Zahnradmenü von QuadriFlow {#quadriflow-gear-menu}
Das Zahnradmenü enthält diese erweiterten Optionen:

##### Grenzen bewahren {#quadriflow-preserve-boundary}
Schützt die Ränder von Löchern.

##### Scharfe Kanten beibehalten {#keep-sharp}
Richtet die Quads an den scharfen Kanten der Oberfläche aus.

##### Minimaler Kostenfluss {#min-cost-flow}
Verwendet für die Quad-Anordnung einen Solver für minimalen Kostenfluss. Langsamer, kann aber eine regelmäßigere Topologie erzeugen.

## ![](/icons/uv.webp) UV-Unwrapping {#uv-unwrap}
Berechnet Texturkoordinaten (UVs) für das ausgewählte Objekt. Nomad bietet zwei Methoden, `UVAtlas` und `BFF`, jede mit ihrer eigenen Schaltfläche `Berechnen`.

![](/videos/unwrap.mp4)

::: tip UVs?
Ein gängiger Vergleich für UVs ist das Einpacken eines Geschenks: Wie schneidet man Geschenkpapier am besten zu, damit es ein Objekt vollständig und ohne Überlappungen bedeckt?

UVs funktionieren ähnlich, nur schneiden Sie statt des Papiers das Objekt auf. Stellen Sie sich vor, Ihr Modell wäre aus dünnem Kunststoff: Wie würden Sie es aufschneiden, um es flach auszubreiten, im flachen Zustand zu bemalen und dann wieder zusammenzusetzen?

Stellen Sie sich nun vor, die Oberfläche Ihres Modells bestünde aus dehnbarem Lycra. Sie könnten das Modell flach dehnen, es aufschneiden oder beides kombinieren. Wenn Sie aber auf das flach ausgebreitete Objekt ein Schachbrettmuster malen, wäre es nach dem Zusammensetzen verzerrt. Was ist besser: mehr Schnitte mit weniger Verzerrung oder weniger Schnitte mit mehr Verzerrung?

UVs sind Anweisungen, die einer 3d-Software sagen, wie sie das Objekt beim Aufbringen von Texturen „zerschneiden und dehnen“ soll. Das Werkzeug UV Atlas verfolgt in der Regel den Ansatz „mehr Schnitte, weniger Verzerrung“.


:::

::: tip UVs, Nomad und andere Apps

Die meisten texturierten Modelle, die Sie online finden, sind mit UVs texturiert. Nomad kann diese importieren und über das Panel [Material](material.md#textures) anzeigen.

Modelle, die Sie in Nomad erstellen, können Sie auch ohne UVs direkt bemalen. Wenn Sie sie in andere Apps exportieren müssen, z. B. nach [Procreate](https://procreate.art/), können Sie die Farbinformationen von Nomad über UVs in Texturen „backen“.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas erzeugt in der Regel lieber mehr Inseln mit Schnitten, um Verzerrungen gering zu halten.

#### Berechnen {#unwrap}
Berechnet die UVs für das ausgewählte Objekt.

#### Optionen {#uvatlas-gear-menu}
Die Schaltflächen neben `Berechnen`:

##### Face-Gruppe {#atlas-face-group}
Steht hier `Ja`, legen die Face-Gruppen die Schnitte der UVs fest. Diese Einstellung gilt auch für BFF.

##### UVs löschen {#delete-uvs}
Die Papierkorb-Schaltfläche löscht die UVs des Objekts.

##### Inspektion {#uv-inspect}
Zeigt die UVs des Objekts im Hintergrund an.

#### Max. Dehnung {#max-stretch}
Niedrige Werte erzeugen weniger Verzerrung und mehr Inseln, hohe Werte mehr Verzerrung und weniger Inseln.

#### Inselabstand {#island-spacing}
Der Abstand zwischen den Inseln. Niedrige Werte verschwenden weniger Platz, riskieren aber, dass Texturen zwischen den Inseln ineinanderlaufen.

::: warning
Das Berechnen von UVs kann etwas dauern. Am besten verwenden Sie ein Mesh mit weniger als 100k Vertices.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF-UVs folgen eher dem Ansatz „weniger Schnitte, mehr Verzerrung“.

#### Optionen {#uv-bff-gear-menu}
Neben `Berechnen` befinden sich dieselben Schaltflächen `Face-Gruppe`, Löschen und `Inspektion` wie bei [UVAtlas](#uvatlas-gear-menu).

##### Face-Gruppe {#bff-face-group}

Verwendet die Face-Gruppen, um die Schnitte der UVs festzulegen.

#### Kegel-Anzahl {#cone-count}
Legt die Anzahl der verwendeten Hauptprojektionen fest. Niedrigere Werte erzeugen weniger Inseln, aber mehr Verzerrung. Höhere Werte brauchen länger zum Berechnen.

#### Nahtlose Patches {#seamless-patches}
Beeinflusst die Anordnung der UV-Patches und kann deutliche Verzerrungen erzeugen. Funktioniert am besten mit sorgfältig angelegten Face-Gruppen.

::: warning
BFF kann überlappende UVs erzeugen, wenn das Mesh Henkel hat (wie das Loch eines Donuts).
:::

### ![](/icons/preview.webp) UV nach Unwrap anzeigen {#show-uv-after-unwrap}
Öffnet nach dem Unwrapping die UV-Inspektion, damit Sie das Ergebnis gleich überprüfen können.

### ![](/icons/bake.webp) Backen: Textur → Textur {#unwrap-bake-texture}
Nur verfügbar, wenn das Material des Objekts Texturen hat. Wenn Sie das Objekt erneut unwrappen, werden die Texturen auf die neuen UVs übertragen, sodass sie weiterhin passen. Die Auflösung steht standardmäßig auf `Auto` und entspricht dann der größten Textur, Sie können sie aber auch selbst festlegen.

## ![](/icons/bake.webp) Backen {#bake}
Dieser Tab überträgt Details und Bemalung zwischen Objekten sowie zwischen Vertices und Texturen.

`Von High-Res` verwendet andere Objekte als Quelle; die Zahl in Klammern gibt an, wie viele. Nomad wählt sie so aus:

- alle ausgewählten Objekte werden verwendet, und das Hauptobjekt der Auswahl ist das Ziel (am stärksten hervorgehoben im Menü [Szene](scene.md))
- ist nur ein Objekt ausgewählt, verwendet Nomad stattdessen alle sichtbaren Objekte
- sind alle anderen Objekte ausgeblendet (zum Beispiel mit Solo), wird die gesamte Szene verwendet

### ![](/icons/bake.webp) Backen → Textur {#bake-texture}
![](/images/topology_bake_menu.webp)

Beim Backen von Texturen entstehen Texturen, indem andere sichtbare Objekte der Szene in die UVs des ausgewählten Objekts projiziert werden. Das Objekt braucht dafür UVs.

So sieht ein typischer Ablauf beim Backen aus:
- Sie haben ein Mesh mit feinen Details und Bemalung
- Klonen Sie es
- Dezimieren Sie es (stellen Sie `Painting erhalten` auf 0)
- Erstellen Sie die UVs
- Backen Sie!

Sie haben nun ein niedrig aufgelöstes Mesh, das den Großteil der Bemalung und der Details Ihres vorherigen Objekts behält.

Nach dem Backen werden die Vertex-Farben in einen neuen, deaktivierten Layer verschoben, damit sie die Texturen nicht stören.

#### Vom Objekt selbst {#tex-from-itself}
Backt das Objekt auf seine eigenen UVs: Seine Bemalung wird zu Texturen, und wenn es Multiauflösungs-Stufen hat, werden die Details der höchsten Stufe auf die aktuelle Stufe gebacken (auf der Schaltfläche erscheint dann ein Multires-Icon). Das ist einfach einzurichten, oft brauchen Sie aber mehr Kontrolle; dann ist die nächste Option nützlicher.

#### Von High-Res {#tex-from-high-res}
Backt von den anderen Objekten auf das ausgewählte Objekt. Die Zahl in Klammern gibt an, wie viele andere Objekte als hochaufgelöste Quellen verwendet und in das aktuelle, niedrig aufgelöste Objekt mit UVs gebacken werden. Die anderen Objekte müssen in Aufbau und Topologie nicht dem gebackenen Objekt ähneln, was sehr flexible Abläufe beim Backen ermöglicht.

#### Auflösung {#tex-bake-resolution}
Die Auflösung der gebackenen Textur. Gebackene Texturen sind immer quadratisch, 1024 erzeugt also ein Bild mit 1024x1024.

Die Schaltflächen darunter sind Abkürzungen für häufig verwendete Auflösungen. Zur Orientierung: 512x512 ist relativ klein, etwa für Webgrafiken und einfache Geometrie. 4096x4096 (kurz 4k) ist für hochwertige Renderings gedacht.

#### Farbe, Matt, Metallisch, Normal, Verschiebung, Leuchten, Deckkraft {#tex-normal-roughness-metalness-color-emissive-opacity}
Diese Schaltflächen bestimmen, welche Eigenschaften gebacken werden, jede in eine eigene Map. Nach dem Backen werden sie als Texturen zum Material des aktuellen Objekts hinzugefügt. `Verschiebung` backt die Höhe der Details als Displacement-Map.

#### ![](/icons/cog.webp) Zahnradmenü Backen {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Das Zahnradmenü enthält diese erweiterten Optionen:

##### Sicherung {#tex-backup}
Um die gebackenen Texturen in der Vorschau zu sehen, sollte die Bemalung des Objekts deaktiviert sein. `Sicherung (Malen → Ebene)` überträgt die Bemalung als Sicherung in einen neuen Layer, sodass Sie sie leicht ein- und ausschalten können.

##### Multires verwenden {#tex-use-multires}
Für `Vom Objekt selbst` bei einem Objekt mit Multiauflösungs-Stufen. Nomad liest die hohe Auflösung über die Unterteilungsstufen aus, statt Strahlen zu werfen: Das ist schneller und frei von Projektionsfehlern. Schalten Sie die Option aus, um mit den folgenden Optionen zu backen.

##### Glatte Basis {#tex-smooth-base}
Für `Verschiebung` bei einem Objekt mit Multiauflösungs-Stufen. Misst die Verschiebung von der unterteilten Basis aus statt von ihren flachen Flächen. Lassen Sie die Option an, wenn die Displacement-Map auf einem unterteilten Mesh verwendet wird, etwa mit der adaptiven Unterteilung von Blender.

##### Suchentfernung {#tex-cage-radius}
Die maximale Entfernung, in der nach der Quelloberfläche gesucht wird. Standardmäßig ist diese Entfernung gering, um Artefakte zu vermeiden. Sie kann aber erhöht werden, wenn die Quellobjekte weit vom gebackenen Objekt entfernt sind.

##### Projektion {#tex-projection}
Wie die Quelloberfläche gefunden wird:

* `Strahl` - Projiziert entlang der Oberflächennormale.
* `Strahl + nächster` - Verwendet den Strahl entlang der Normale und dann die nächstgelegene Oberfläche, wenn der Strahl nichts trifft.
* `Nächster` - Projiziert auf den nächstgelegenen Punkt der Quelloberfläche.

##### Strahlenversatz {#tex-ray-offset}
Passt an, von wo auf dem gebackenen Objekt die Berechnung startet. Ein kleiner Abstand zur Oberfläche vermeidet die häufigsten Artefakte. Wenn die Quellobjekte sehr weit vom gebackenen Objekt entfernt sind, muss dieser Versatz eventuell erhöht werden. Bei `Nächster` wird er nicht verwendet.


### ![](/icons/bake.webp) Reprojizieren → Vertex {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projiziert modellierte Details, Bemalung, Layer und Texturen in Vertex-Werte.

Man kann es sich als Umkehrung des Backens vorstellen: Während das Backen Vertex-Eigenschaften in Texturen überträgt, überträgt das Reprojizieren Texturen (und andere Eigenschaften)
 zurück in die Vertices.

::: tip
Bei `Backen → Textur` und `Reprojizieren → Vertex` werden sowohl die Vertex-Farben als auch die Texturen des Materials berücksichtigt.
:::

#### Vom Objekt selbst {#vertex-from-itself}
Wandelt die Texturen des Materials in Vertex-Werte um. Diese Schaltfläche ist nur aktiv, wenn das Objekt UVs hat und im Material Texturen aktiv sind.

::: tip TIPP: Texturen bemalen
Nomad unterstützt das direkte Bemalen und Bearbeiten von Texturen nicht, aber Sie erreichen sehr ähnliche Ergebnisse, indem Sie Texturen in Vertex-Werte projizieren, auf den Vertices malen und dann die Vertices wieder in Texturen backen:

1. Richten Sie ein Low-Poly-Objekt mit UVs ein
1. Laden Sie Texturen in sein Material
1. Unterteilen Sie es so weit, dass Sie darauf malen können
1. `Reprojizieren → Vertex` im Modus `Vom Objekt selbst`: Die Textur ist jetzt in Vertex-Werte umgewandelt
1. Malen, glätten, verwischen, stempeln Sie, ganz wie Sie es brauchen
1. `Backen → Textur` im Modus `Vom Objekt selbst`. Ihre Änderungen werden wieder in Texturen umgewandelt.
:::

#### Von High-Res {#vertex-from-high-res}
Wandelt die anderen Objekte in Vertex-Werte auf dem ausgewählten Objekt um. Die Zahl auf dieser Schaltfläche gibt die Anzahl der Quellobjekte an. Gedacht ist das vor allem für ein ebenfalls hochaufgelöstes Mesh, typischerweise mit sauberer Topologie.

::: tip
Mit dem Reprojizieren anderer Objekte können Sie nicht nur Farbinformationen übertragen, sondern auch Vertices auf andere Objekte projizieren, z. B. Bandagen auf eine Figur.
:::

#### Vertices, Farbe, Matt, Metallisch, Deckkraft, Maske, Layer, Face-Gruppe {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Diese Schaltflächen bestimmen, welche Eigenschaften auf das ausgewählte Objekt projiziert werden. `Layer` überträgt die anderen Layer auf das ausgewählte Mesh.

#### ![](/icons/cog.webp) Zahnradmenü Reprojizieren {#vertex-reproject-gear-menu}
Das Zahnradmenü enthält diese erweiterten Optionen:

##### Deckkraft → Maske {#vertex-opacity-to-mask}
Wandelt die Deckkraft der Quelle in eine Maske auf dem ausgewählten Objekt um.

##### Iterationen {#vertex-iterations}
Wie oft das Entspannen während des Reprojizierens angewendet wird. Nur verwendet, wenn `Vertices` aktiv ist.

##### Entspannen {#vertex-relax}
Die Anordnung des ausgewählten Meshes kann um einen gewissen Betrag geglättet oder entspannt werden, damit sie besser zu den Quellobjekten passt. `Glätten` eignet sich besser für High-Poly-Meshes, `Entspannen` besser für Low-Poly-Meshes. Bei `Auto` wählt Nomad die beste Methode.

##### Suchentfernung {#vertex-cage-radius}
Die maximale Entfernung, in der nach der Quelloberfläche gesucht wird. Standardmäßig ist diese Entfernung gering, um Artefakte zu vermeiden. Sie kann aber erhöht werden, wenn die Quellobjekte weit vom ausgewählten Objekt entfernt sind.

##### Projektion {#vertex-projection}
Wie die Quelloberfläche gefunden wird:

* `Strahl` - Projiziert entlang der Oberflächennormale.
* `Adaptive Mischung` - Mischt den Strahl entlang der Normale und die nächstgelegene Oberfläche abhängig von der Entfernung und von `Strahlpräferenz`. Trifft eines davon nichts, wird das andere verwendet.
* `Nächster` - Projiziert auf den nächstgelegenen Punkt der Quelloberfläche.

##### Strahlpräferenz {#vertex-ray-bias}
Nur für `Adaptive Mischung`. Höhere Werte gewichten die Mischung stärker zum Ergebnis des Strahls, niedrigere Werte zum nächstgelegenen Punkt.

##### Strahlenversatz {#ray-vertex-offset}
Passt an, von wo auf dem ausgewählten Objekt die Berechnung startet. Ein kleiner Abstand zur Oberfläche vermeidet bestimmte Artefakte. Wenn die Quellobjekte sehr weit vom gebackenen Objekt entfernt sind, muss dieser Versatz eventuell erhöht werden. Bei `Nächster` wird er nicht verwendet.

### ![](/icons/bake.webp) Backen → VDM {#bake-vdm}
Erstellt aus dem ausgewählten Objekt einen VDM-Stempel (Vector Displacement) und fügt ihn der VDM-Bibliothek hinzu. Sie werden nach einem Namen gefragt.

So sieht ein typischer Ablauf aus:
- Fügen Sie eine Ebene hinzu, oder wählen Sie `Neues VDM` in der VDM-Auswahl, um eine fertig eingerichtete hinzuzufügen (die Grundform [VDM](scene.md#add-menu))
- Modellieren Sie Ihre Form darauf und lassen Sie den Rand flach
- Backen Sie!

Die UVs der Ebene legen das Quadrat fest, das gebacken wird, das Objekt braucht also UVs. Wählen Sie die Größe des Stempels mit `Auflösung`, und legen Sie mit `Farbe`, `Matt`, `Metallisch` und `Deckkraft` fest, was der Stempel neben der Verschiebung enthält.

::: tip
Verwenden Sie auf der Ebene kein Dyntopo, es beschädigt ihre UVs, und der Stempel wird verzerrt. Das Modellieren in einem Layer liefert das genaueste Ergebnis, da die flache Ebene darunter erhalten bleibt. Auch zum Malen brauchen Sie einen Layer, sonst wird das Material auf das ganze Quadrat gestempelt statt nur dort, wo Sie gemalt haben.
:::

## ![](/icons/dot.webp) Grundformen {#primitive}
Parameter der ausgewählten Grundform. Die meisten davon erreichen Sie auch über die Schaltfläche `…` der Werkzeugleiste der Grundform im Viewport.

![](/images/topology_primitive_screenshot.webp)
