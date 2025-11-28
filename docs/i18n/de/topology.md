# ![](/icons/multires.webp) Topologie {#topology}

Dieses Menü steuert die Topologie von Objekten in Nomad sowie Werkzeuge zum Baken und Übertragen von Details zwischen Objekten und zwischen Texturen.

![](/images/topology_overview.webp)

Nomad basiert auf Polygonen, es verwendet Dreiecke und Quads zur Darstellung der Geometrie.
Mit Topologie meinen wir sowohl die Anzahl der Flächen als auch die Art, wie Punkte (Vertices) verbunden sind.

Es ist wichtig, die Topologie im Blick zu behalten, insbesondere wenn du feine Details modellieren oder malen möchtest.

::: tip Wie behältst du deine Topologie im Blick?
Du kannst das [Wireframe](settings.md#wireframe) anzeigen oder einfach [Smooth Shading](settings.md#smooth-shading) deaktivieren.
:::

![](/images/topology_top.webp)

Das Topologie-Menü von Nomad hat mehrere Abschnitte:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Mehrere Detailstufen mit Subdivision bearbeiten                  |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Neue Topologie mit gleichmäßiger Dichte berechnen                |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Lokal in Echtzeit beim Sculpten oder Malen Flächen hinzufügen/entfernen |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Reduktion, UVs, Baking, Remeshing, Reprojektion                  |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Primitive-Optionen                                               |


## Polygonstatistik {#polygon-stats}

![](/images/topology_stats.webp)

Der obere Abschnitt des Topologie-Menüs zeigt Polygoninformationen für das ausgewählte Objekt und die gesamte Szene. Die Zahlen zeigen die Gesamtanzahl der Vertices, die Gesamtanzahl der Dreiecke und die Gesamtanzahl der Quads (4-seitige Polygone).

Ein Tippen auf diesen Abschnitt öffnet eine Liste mit Polygonstatistiken für alle Polygonobjekte in der Szene.

## ![](/icons/multires.webp) Multiresolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### Was ist Multiresolution? {#what-is-multiresolution}
Die Multiresolution-Funktion ist für zwei Hauptszenarien nützlich:
- Der glättende Subdivision-Algorithmus, um die Polygonanzahl deines Objekts zu erhöhen
- Umgang mit mehreren Auflösungsstufen, sodass du zwischen kleinen und großen Bearbeitungen wechseln kannst

![](/videos/multiresolution.mp4)

#### Multiresolution-Workflow {#multiresolution-workflow}
Ein wichtiger Aspekt der Multiresolution ist, dass du zu einer niedrigeren Auflösung zurückkehren, Änderungen an deinem Objekt vornehmen und dann zur höchsten Auflösung zurückkehren kannst, ohne die hochauflösenden Details zu verlieren. Alle hochauflösenden Details werden automatisch projiziert.

::: warning
Wenn du ein Werkzeug verwendest, das die Topologie deines Objekts verändert, verlierst du alle anderen Auflösungsstufen deines Objekts!
Du solltest immer eine Warnung erhalten, falls dies passieren könnte, zum Beispiel wenn du verwendest:
- den [Voxel Remesher](#voxel-remesher)
- die [Dynamic Topology](#dynamic-topology)
- das [Trim-Werkzeug](tools.md#trim)
- das [Split-Werkzeug](tools.md#split)
:::


### Multiresolution-Schieberegler {#multiresolution-slider}
Dieser Slider zeigt die Anzahl der Subdivision-Stufen im aktuellen Objekt an. Wenn es 6 vertikale Balken gibt, gibt es 6 Subdivision-Stufen. Der Kreis zeigt die aktuell angezeigte Subdivision-Stufe an. 

### Umkehren {#reverse}
Wenn du dich auf der niedrigsten Subdivision-Stufe befindest, versucht die Reverse-Schaltfläche, eine Stufe unterhalb der aktuellen zu erzeugen. Beachte, dass dies im Allgemeinen nur möglich ist, wenn das Objekt ursprünglich mit Subdivision erstellt wurde, etwa in Nomad oder in anderen 3D-Anwendungen mit Multiresolution-Subdivision-Surfaces.

### Unterteilen {#subdivide}
Die Schaltfläche *Subdivide* vervierfacht die Anzahl der Polygone, achte also auf die Polygonanzahl, da sie sehr schnell steigen kann!
Ein wichtiger Aspekt von *Subdivision Surface* ist, dass sie gegen eine *Smooth Surface* konvergieren.
Um zu verstehen, wie das funktioniert, kannst du die *Subdivide*-Schaltfläche an einem Objekt mit nur wenigen Polygonen ausprobieren.

Du kannst dieses *Smooth*-Verhalten deaktivieren, indem du die Option `Linear subdivision` aktivierst.

### Untere löschen {#delete-lower}
Wenn es Subdivision-Stufen unterhalb der aktuell angezeigten Stufe gibt, werden diese gelöscht. Falls du das versehentlich tust, kannst du sie mit der Reverse-Schaltfläche wiederherstellen.

### Obere löschen {#delete-higher}
Wenn es Subdivision-Stufen oberhalb der aktuell angezeigten Stufe gibt, werden diese gelöscht.

### Lineare Unterteilung {#linear-subdivision}
Unterteilt das Mesh, ohne Glättung anzuwenden.

### Scharfe Kante {#sharp-border}
Wenn dein Objekt Facegroups hat, sorgt das Aktivieren dieser Option dafür, dass die Facegroup-Grenzen scharf bleiben. Dies kann für jede Subdivision-Stufe separat eingestellt werden (der Subdivision-Slider zeigt ein kleines Symbol über der Stufe an, um dies zu kennzeichnen).

### Dreiecke beibehalten {#keep-triangles}
Die meisten Standard-Subdivision-Systeme versuchen, während einer Subdivision-Operation alle Polygone in Quads umzuwandeln. Dieser Schalter erzwingt, dass die Subdivision Dreiecke verwendet.

### Sperren (LV0) {#lock-lv0}

Verhindert, dass die niedrigste Subdivision-Stufe verändert wird. Das kann wichtig sein, wenn dein Objekt in einer anderen Anwendung erzeugt wurde und das Basisobjekt unverändert bleiben muss. Wenn diese Option deaktiviert ist, werden große Änderungen auf höheren Subdivision-Stufen auch Level 0 verschieben.

::: tip 

Subdivision glättet standardmäßig alle scharfen Kanten. Um Kanten leicht scharf zu halten, experimentiere damit, auf den ersten 2 Subdivide-Stufen Linear subdivision oder Sharp border zu verwenden und es dann für höhere Stufen zu deaktivieren. So entsteht ein halb-scharfes, unterteiltes Mesh.

:::


## ![](/icons/voxel.webp) Voxel-Remesher {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Bei Verwendung des `Voxel Remesher` wird die gesamte Mesh-Topologie auf eine einheitliche Auflösung gezwungen, was bedeutet, dass alle Polygone mehr oder weniger die gleiche Größe haben. Das ist sehr nützlich, wenn du nicht über Topologie nachdenken und einfach frei modellieren möchtest.

Ein typischer Sculpting-Workflow kann damit beginnen, den `Voxel Remesher` zu verwenden, um mit niedriger Auflösung eine grobe Form zu blocken.
Drücke einfach hin und wieder die *Remesh*-Schaltfläche, wenn du das Mesh zu stark dehnst, um zu starke Verzerrungen zu vermeiden.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Wie oben erwähnt, ist Nomad eine polygonale Software, aber der `Voxel Remesher` ist eine Ausnahme, bei der (temporär) ein anderer Ansatz verwendet wird, um das Remeshing durchzuführen.

Ein großer Unterschied ist, dass der Voxel-Ansatz keine Selbstüberschneidungen akzeptiert, diese werden also aufgelöst.
Außerdem unterstützt er keine Meshes mit Löchern.

Mit Löchern meinen wir nicht das `Genus-Loch` (das `Loch` eines Donuts), sondern Meshes, die nicht `wasserdicht`/`geschlossen` sind.
Typischerweise bedeutet das, dass vor dem Remeshing alle Löcher gefüllt werden, ähnlich wie beim [Trim-Werkzeug](tools.md#trim) oder der [Hole-filling-Funktion](scene.md#hole-filling).
:::

### Remeshen {#voxel-remesh}
Führt das Voxel-Remesh aus.

### Auflösung {#voxel-resolution}
Die Größe der Voxel, die während der Berechnung verwendet werden. Beim Ändern dieses Parameters wird ein Schachbrettmuster über dem Mesh eingeblendet, um eine Vorschau des Ergebnisses zu geben.

### Multiresolution erzeugen {#build-multiresolution}
Erzeugt niedrigere Multiresolution-Stufen für das Voxel-Remesh. Wenn du das Schachbrettmuster verwendest, um eine Auflösung einzustellen, und Build multiresolution auf 2 setzt, wird das Endergebnis Details haben, die der Resolution-Slider-Einstellung entsprechen, und im Multires-Tab wird es auf Level 2 sein, d. h. du hast niedrigere Multires-Meshes auf Level 1 und Level 0. Das kann ein guter Weg sein, um sowohl ein sauberes Mesh mit gleichmäßigen Polygonen zu erzeugen als auch ein Low-Poly-Kontrollmesh zu erhalten.

::: tip Tipp: Build multiresolution und Stable smoothing

Diese Option kann manchmal „Schleifen“ in der Geometrie verursachen, die schwer zu glätten sind und kleine Pickel erzeugen. Wenn das passiert, aktiviere „Stable smoothing“ in den Optionen des Smooth-Werkzeugs. 

:::

### Scharfe Kanten beibehalten {#keep-sharp-edges}
Aktiviert das Snapping der neuen Punkte an scharfe Kanten des ursprünglichen Meshes. Das kann Verzerrungen einführen.

## ![](/icons/dynamic.webp) Dynamische Topologie {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution und Voxel-Remeshing sind gängige Methoden in der Branche, um Topologie zu kontrollieren, aber beide erfordern, dass du darauf achtest, Polygone nicht zu weit zu dehnen oder zu stark zu stauchen. 

Dynamic Topology ist eine alternative Methode. Während du modellierst, fügt Nomad adaptiv Polygone hinzu oder entfernt sie während des Pinselstrichs. Das Einritzen kleiner Details fügt viele kleine Polygone dort hinzu, wo du sie brauchst, und Glätten entfernt anderswo Polygone.

Beachte, dass Dynamic Topology Dreiecke statt Quads verwendet. Das kann etwas unordentlich aussehen, aber es ist fast besser, das Wireframe nicht anzusehen und dich einfach darauf zu konzentrieren, eine gut aussehende Skulptur zu erstellen, ohne dir Sorgen um die Topologie zu machen. Später kannst du eines der anderen Remeshing-Werkzeuge von Nomad verwenden, um ein sauberes Quad-Mesh zu erzeugen.

Sieh dir das Video unten in Aktion an.

![](/videos/dynamic.mp4)

### Aktiviert {#enabled}
Aktiviert Dynamic Topology. Ein DynTopo-Symbol wird unter den Slidern für Pinselradius und -intensität platziert, damit du Dyntopo pro Werkzeug umschalten kannst.

### Detail {#dyn-detail}
Steuert die Detailmenge, das Verhalten ändert sich je nach Auswahl von „Detail based on...“, siehe unten.

### Detail basierend auf... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Das Detailniveau hängt davon ab, wie groß das Objekt auf dem Bildschirm ist. Der Detail-Slider ist bei 100 % oder höher für feine Details (kleine Dreiecke) oder bei 1 % für grobe Details (große Dreiecke).  |
| Radius   | Der Werkzeugradius definiert die Detailmenge. Verwende einen kleinen Werkzeugradius für feine Details, einen großen für grobe Details. Der Detail-Slider ist ein Multiplikator für dieses Verhältnis.                     |
| Constant | Der Detail-Slider definiert die Detailmenge und wird nicht von Bildschirmgröße oder Werkzeuggröße beeinflusst.             |

::: tip TIPP: Radius-Modus

Um ein besseres Gefühl dafür zu bekommen, wie der Radius-Modus funktioniert, bewege den Detail-Slider mit einem Finger und ändere gleichzeitig den Werkzeugradius mit einem anderen Finger. Du wirst sehen, wie sie miteinander verknüpft sind.

:::

### Bevorzugen... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Performance bevorzugen |
| Quality | Qualität bevorzugen     |

Wenn du `Quality` bevorzugst, sind die zwei Hauptunterschiede:
- Verfeinerung wird vor dem Sculpting angewendet, sodass du weniger Interpolationsartefakte beim Malen oder Modellieren sehr kleiner Details bekommst
- Verfeinerung läuft, bis sie zum korrekten Detailniveau konvergiert, im Gegensatz zu einem inkrementellen Verhalten.
 
So wird bei sehr kleinen Details oder schnellen Strichen die Topologie immer wie erwartet verfeinert.


### Druck auf Radius verwenden {#use-pressure-on-radius}
Nur relevant, wenn `Radius` aktiviert ist. Wenn aktiviert, spiegelt die Detailmenge immer die Pinselgröße wider, selbst wenn die Pinselgröße durch Stiftdruck beeinflusst wird.

### Pinselabfall verwenden {#use-stroke-falloff}

Bezieht auch die Pinsel-Falloff-Kurve und das Alpha in die Dyntopo-Berechnungen ein.

### Methode {#method}
Egal, ob du `Dynamic Topology` auf deinem [Brush](#brush) oder [Global](#global) verwendest, du kannst wählen, in welchem Modus sie arbeitet:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Kann Flächen hinzufügen und entfernen, dies ist der Modus im obigen Video |
| Subdivision    | Fügt nur neue Flächen hinzu, kann keine entfernen                     |
| Decimation     | Entfernt nur Flächen, kann keine hinzufügen                           |

### Maskierten Bereich schützen {#protect-masked-area}
Aktiviert, dass maskierte Bereiche vor Topologieänderungen geschützt werden.

### Vertex-Extrapolation {#vertex-extrapolation}


### Detail {#all-detail}
Die Auflösung, die für die Remesh-Operation verwendet wird. Wenn Dyntopo im „Constant“-Modus ist, entspricht sie dem Wert des Detail-Sliders oben in diesem Menü.

### Remeshen {#dyn-remesh}
Führt ein globales Remesh mit dem Dyntopo-Algorithmus aus. Normalerweise solltest du für ein vollständiges Remeshing den [Voxel Remesher](#voxel-remesher) verwenden.

Ein Vorteil gegenüber Voxeln ist jedoch, dass der maskierte Bereich geschützt wird, sodass du besser kontrollieren kannst, wo du mehr oder weniger Dichte haben möchtest.



## ![](/icons/topo_extra.webp) Verschiedenes {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Zahnrad-Menü {#gear-menu}
Viele Werkzeuge in diesem Menü haben zusätzliche Optionen. Sie sind über das Zahnrad-Symbol neben dem Abschnittstitel zugänglich.

### Reduzierung {#decimation}

![](/images/topology_decimation.webp)

Reduziert die Anzahl der Polygone, indem versucht wird, so viele Details wie möglich zu erhalten, unter Verwendung von Dreiecks-Polygonen.

Diese Funktion kann nützlich sein, wenn du für 3D-Druck exportieren möchtest.
Du solltest sie jedoch wahrscheinlich nicht verwenden, wenn du weiter daran modellieren willst, da sie ungleichmäßige Dreiecke erzeugen kann.

Beachte, dass maskierte Bereiche nicht reduziert werden.

![](/videos/decimate.mp4)

::: tip

Die Verwendung des [Quadremesh-Werkzeugs](tools.md#quad-remesher) auf hochauflösenden Objekten kann lange Berechnungszeiten verursachen und schwer kontrollierbare Ergebnisse liefern. Eine Vorverarbeitung des Meshes mit [Facegroups](tools.md#facegroup-1) und Decimate macht Quadremesh deutlich schneller und erlaubt wesentlich mehr Kontrolle über die Topologie.

* Erstelle Facegroups im Mesh, um deinen idealen Quad-Flow zu definieren.
* Facegroup relax, um glatte Facegroup-Grenzen zu erhalten.
* Decimate. Das stellt sicher, dass du keine dünnen oder verzerrten Flächen an den Facegroup-Kanten hast. Stelle in den Decimate-Einstellungen sicher, dass Facegroup aktiviert ist. Dadurch folgen Dreieckskanten deinen Facegroup-Kanten exakt.
* Deaktiviere in den Quadremesh-Optionen Relax (da du das Mesh bereits entspannt hast), und du solltest gute Ergebnisse erhalten.

:::

#### Reduzieren {#decimate}
Startet die Decimate-Operation.

Die Symbole neben der Decimate-Schaltfläche erlauben dir, Optionen umzuschalten, die die Reduktion beeinflussen. Der Prozentwert gibt an, wie stark diese Option wirkt, und kann im erweiterten Gear-Menü eingestellt werden.

* ![](/icons/palette.webp)  `Preserve Painting` – Platziert mehr Dreiecke dort, wo es Maldetails gibt.
* ![](/icons/triforce.webp) `Uniform Faces` – Bevorzugt gleichmäßig große Dreiecke.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` – Decimate versucht, Ränder an offener Geometrie und Löchern unverändert zu lassen.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` – Decimate versucht, Facegroup-Grenzen unverändert zu lassen.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` – Decimate versucht, UV-Grenzen unverändert zu lassen.

#### ![](/icons/cog.webp) Zahnrad-Menü Reduzierung {#decimate-gear-menu}
Das Gear-Menü hat diese erweiterten Optionen:
##### Malerei erhalten {#preserve-painting}
Die Checkbox schaltet diesen Modus ein oder aus, der Wert bestimmt, wie genau Maldetails erhalten werden. Höhere Werte erhalten mehr Malerei. Setze auf 0, wenn dir Malerei egal ist.


##### Gleichmäßige Flächen {#uniform-faces}
Die Checkbox schaltet diesen Modus ein oder aus. Höhere Werte erzeugen Dreiecke mit ähnlicher Größe.

##### Ränder erhalten {#preserve-borders}
Aktivieren, um zu verhindern, dass Ränder reduziert werden. Randgewichte können für `Geometry`-, `Face Group`- oder `UV`-Ränder ausgewählt werden.

#### Ziel-Dreiecke {#target-triangles}
Legt die Zielanzahl der Dreiecke fest. Der Standardwert ist 50 %, die Prozent/Ziel-Schaltfläche wechselt zwischen einem Prozentsatz oder einer exakten Ziel-Polygonanzahl.



### UV Unwrap - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Berechnet Texturkoordinaten (UVs) für das aktuelle Mesh und bevorzugt dabei im Allgemeinen mehr Inseln mit Schnitten, um Verzerrungen zu minimieren.

Das kleine Augensymbol zwischen dem Menütitel und dem Gear-Menü schaltet die Vorschau der UVs auf dem Objekt ein oder aus.

![](/videos/unwrap.mp4)

#### Abwickeln {#unwrap}
Berechnet UVs für das ausgewählte Objekt, die im Hintergrund angezeigt werden.

#### UVs löschen {#delete-uvs}
Löscht die UVs des Objekts.

#### ![](/icons/cog.webp) Zahnrad-Menü UVAtlas {#uvatlas-gear-menu}
Das Gear-Menü hat diese erweiterten Optionen:

#### Flächengruppe {#atlas-face-group}

Verwendet Facegroups, um die Schnitte für die UVs zu definieren.

##### Maximale Dehnung {#max-stretch}
Niedrige Werte erzeugen weniger Verzerrung und mehr Inseln, hohe Werte erzeugen mehr Verzerrung und weniger Inseln. 

##### Inselabstand {#island-spacing}
Die Menge an Abstand zwischen den Inseln. Niedrige Werte verschwenden weniger Platz, bergen aber das Risiko, dass Texturen zwischen Inseln ausbluten. 

::: warning
Das Berechnen von UVs kann einige Zeit dauern, es ist am besten, ein Mesh mit weniger als 100k Vertices zu verwenden.
:::

::: tip UVs?
Eine gängige Analogie für UVs ist das Einpacken eines Geschenks: Was ist die beste Art, Geschenkpapier zu schneiden, um ein Objekt vollständig zu bedecken, ohne Überlappungen? 

UVs sind ähnlich, aber anstatt das Papier zu schneiden, schneidest du das Objekt. Stell dir vor, dein Modell wäre aus dünnem Plastik – wie würdest du es zerschneiden, um es flach auszubreiten, im flachen Zustand zu bemalen und dann wieder zusammenzusetzen?

Stell dir nun vor, die Oberfläche deines Modells besteht aus dehnbarem Lycra. Du könntest das Modell flach ziehen, es schneiden oder eine Kombination aus beidem. Aber wenn du im flachen Zustand ein Schachbrettmuster aufmalst, wäre das Schachbrett beim Wiederzusammenbau verzerrt. Was ist besser: mehr Schnitte mit weniger Verzerrung oder weniger Schnitte mit mehr Verzerrung?

UVs sind Anweisungen für 3D-Software, wie das Objekt beim Anwenden von Texturen „geschnitten und gedehnt“ werden soll. Das UV-Atlas-Werkzeug verwendet im Allgemeinen einen Ansatz „mehr Schnitte, weniger Verzerrung“.


:::

::: tip UVs, Nomad und andere Apps

Die meisten texturierten Modelle, die du online findest, sind mit UVs texturiert. Nomad kann dies über das [Material-Panel](material#textures) importieren und anzeigen.

Wenn Modelle in Nomad erstellt werden, kannst du direkt auf Objekte ohne UVs malen. Wenn du sie in andere Apps exportieren musst, z. B. nach [Procreate](https://procreate.art/), kannst du Nomad-Farbinformationen über UVs in Texturen „baken“. 

:::

### UV Unwrap - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF-UVs bevorzugen einen Ansatz „weniger Schnitte, mehr Verzerrung“. 

#### ![](/icons/cog.webp) Zahnrad-Menü UV BFF {#uv-bff-gear-menu}

#### Flächengruppe {#bff-face-group}

Verwendet Facegroups, um die Schnitte für die UVs zu definieren.

##### Kegelanzahl {#cone-count}
Definiert die Anzahl der Hauptprojektionen. Niedrigere Werte erzeugen weniger Inseln, aber mehr Verzerrung.

##### Nahtlose Patches {#seamless-patches}
Beeinflusst das Layout der UV-Patches, funktioniert am besten mit sorgfältig erstellten Facegroups.

### Backen -> Textur {#bake-texture}
![](/images/topology_bake_menu.webp)

Texture Baking erstellt Texturen, indem andere sichtbare Objekte in der Szene in die UVs des ausgewählten Objekts projiziert werden.

Typischer Workflow für Baking:
- Du hast ein Mesh mit feinen Details und Malerei
- Du klonst es
- Du reduzierst es (setze `Preserve painting` auf 0)
- Du erstellst UVs
- Du bakst!

Nomad berücksichtigt standardmäßig alle sichtbaren Meshes in der Szene.
Du kannst auch den Solo-Modus verwenden, um die meisten anderen Meshes schnell zu verstecken.
Wenn keine anderen Objekte sichtbar sind, wird die gesamte Szene berücksichtigt.

Du solltest nun ein niedrig aufgelöstes Mesh haben, das die meisten Farben und Details deines vorherigen Objekts beibehält.

Nach der Operation werden Vertexfarben in eine neue, deaktivierte Ebene verschoben, damit sie nicht mit den Texturen interferieren.

#### Von sich selbst {#tex-from-itself}
Bakt die höchste Multiresolution-Stufe auf die niedrigste Stufe des aktuellen Objekts. Das ist einfach einzurichten, aber oft benötigst du mehr Kontrolle, in diesem Fall ist die nächste Option nützlicher.

#### Von High-Res () {#tex-from-high-res}
Bakt von den anderen sichtbaren Objekten in der Szene auf das ausgewählte Objekt. Die Zahl in Klammern gibt die Anzahl der anderen sichtbaren Objekte an, die als High-Res-Ziele verwendet und in das aktuelle Low-Res-Objekt mit UVs gebakt werden. Die anderen Objekte müssen im Layout oder in der Topologie nicht dem zu bakenden Objekt ähneln, was vielseitige Bake-Workflows ermöglicht.

#### Auflösung {#tex-bake-resolution}
Die Auflösung der gebackenen Textur. Bake-Texturen sind immer quadratisch, also erzeugt 1024 ein 1024x1024-Bild. 

Die Schaltflächen darunter sind Abkürzungen für häufig verwendete Auflösungen. Zum Vergleich: 512x512 ist relativ klein, z. B. für Webgrafiken und einfache Geometrie. 4096x4096 (kurz 4k) ist für hochwertige Renderings.

#### ![](/icons/cog.webp) Zahnrad-Menü Backen {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Das Gear-Menü hat diese erweiterten Optionen:

##### Normal, Rauheit, Metallizität, Farbe, Emissiv, Deckkraft {#tex-normal-roughness-metalness-color-emissive-opacity}
Diese Checkboxen bestimmen, welche Eigenschaften gebakt werden, jeweils in separate Maps. Nach Abschluss des Bakens werden diese als Texturen dem Material des aktuellen Objekts hinzugefügt.

##### Sicherung {#tex-backup}
Um die gebackenen Texturen zu betrachten, sollten die Malinformationen des Objekts deaktiviert werden. Diese Option überträgt alle Malinformationen in eine neue Ebene als Backup, sodass sie leicht ein- und ausgeschaltet werden können.

#### Käfigradius {#tex-cage-radius}
Legt fest, wie weit vom Bake-Objekt entfernt Strahlen ausgesendet werden, um Zielobjekte zu finden. Standardmäßig ist diese Distanz niedrig, um Artefakte zu vermeiden, kann aber erhöht werden, wenn die Zielobjekte weit vom Bake-Objekt entfernt sind.

##### Strahlenversatz {#tex-ray-offset}
Legt fest, wo die Bake-Berechnungen auf dem Bake-Objekt beginnen. Standardmäßig starten sie 5 % von der Oberfläche entfernt, was die meisten gängigen Artefakte vermeidet. Wenn die Zielobjekte sehr weit vom Bake-Objekt entfernt sind, muss dieser Offset möglicherweise erhöht werden.


### Auf Vertex reprojizieren {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projiziert modellierte Details, Malerei, Ebenen und Texturen in Vertex-Werte.

Man kann es als das Gegenteil von Baking betrachten: Wenn Baking Vertex-Eigenschaften in Texturen überträgt, überträgt Reproject Texturen (und andere Eigenschaften)
 zurück in Vertices.

::: tip
Bei Verwendung von `Bake to texture` oder `Reproject to vertex` werden sowohl Vertexfarben als auch Materialtexturen berücksichtigt.
:::

#### Von sich selbst {#vertex-from-itself}
Konvertiert Texturen aus dem Material in Vertex-Werte. Diese Schaltfläche ist nur aktiv, wenn das Objekt UVs hat und Texturen im Material aktiv sind.

::: tip TIPP: Texture Painting
Nomad unterstützt kein direktes Malen und Bearbeiten von Texturen, aber sehr ähnliche Ergebnisse können erzielt werden, indem Texturen -> Vertex-Werte projiziert, auf Vertices gemalt und dann Vertex -> Texturen gebakt wird:

1. Richte ein Low-Poly-Objekt mit UVs ein
1. Lade Texturen in sein Material
1. Unterteile es ausreichend, um darauf malen zu können
1. `Reproject to vertex` im Modus `From itself`, jetzt wurde die Textur in Vertex-Werte umgewandelt
1. Male, glätte, verwische, stemple, führe alle gewünschten Bearbeitungen durch
1. `Bake to texture` im Modus `From itself`. Diese Bearbeitungen werden zurück in Texturen umgewandelt.
:::

#### Von High-Res () {#vertex-from-high-res}
Konvertiert alle sichtbaren Objekte in Vertex-Werte auf dem ausgewählten Objekt. Die Zahl auf dieser Schaltfläche gibt die Anzahl der sichtbaren Objekte an.

::: tip
Das Reprojizieren anderer Objekte kann nicht nur zum Übertragen von Farbinformationen verwendet werden, sondern auch, um Vertices auf andere Objekte zu projizieren, z. B. können Bandagen auf eine Figur projiziert werden.
:::

#### ![](/icons/cog.webp) Zahnrad-Menü Reprojektion {#vertex-reproject-gear-menu}
Das Gear-Menü hat diese erweiterten Optionen:

#### Vertices, Rauheit, Metallizität, Farbe, Deckkraft, Deckkraft->Maske, Maske, Ebenen, Flächengruppe {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Diese Checkboxen bestimmen, welche Eigenschaften auf das ausgewählte Objekt projiziert werden. 

#### Glätten {#vertex-relax}
Das ausgewählte Mesh kann in seinem Layout geglättet oder in gewissem Maß entspannt werden, um besser zu den Reprojektionszielen zu passen. Smooth ist besser für hochauflösende Meshes. Relax ist besser für Low-Poly-Meshes. Auto überlässt Nomad die Wahl der besten Methode.

#### Iterationen {#vertex-iterations}
Wie oft die Relax-Operation während der Reprojektion angewendet werden soll.

#### Käfigradius {#vertex-cage-radius}
Legt fest, wie weit vom ausgewählten Objekt entfernt Strahlen ausgesendet werden, um Zielobjekte zu finden. Standardmäßig ist diese Distanz niedrig, um Artefakte zu vermeiden, kann aber erhöht werden, wenn die Zielobjekte weit vom Bake-Objekt entfernt sind.

#### Strahlen-Bias {#vertex-ray-bias}
Niedrige Werte bevorzugen die Projektion auf den nächstgelegenen Punkt der Zieloberfläche. Höhere Werte bevorzugen einen Schnittpunkt unter Verwendung der Oberflächennormale. 

#### Strahlenversatz {#ray-vertex-offset}
Legt fest, wo die Bake-Berechnungen auf dem ausgewählten Objekt beginnen. Standardmäßig starten sie 5 % von der Oberfläche entfernt, was bestimmte Artefakte vermeidet. Wenn die Zielobjekte sehr weit vom Bake-Objekt entfernt sind, muss dieser Offset möglicherweise erhöht werden.


### Quad-Remesh - Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remesht mit dem [Instant-Meshes-Algorithmus von Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Er analysiert den Flow eines Meshes und erzeugt eine saubere Quad-Topologie.

::: tip
Unter iOS und auf dem Desktop liefert das [Quad remesher](tools#quad-remesher)-Werkzeug bessere Ergebnisse und mehr Kontrolle.
:::

#### Remeshen {#instant-remesh}
Startet die Instant-Meshes-Operation.

#### Ziel-Quads {#target-quads}
Die Anzahl der Quad-Polygone, die Quad Remesh zu erzeugen versucht.

#### ![](/icons/cog.webp) Zahnrad-Menü Quad-Remesh Instant {#quad-remesh-instant-gear-menu}
Das Gear-Menü hat diese erweiterten Optionen:

##### Faltwinkel {#crease-angle}
Ein Schwellenwert für scharfe Ecken, der versucht, die Remesh-Operation zu unterstützen.

#### Max. Lochfüllung {#max-fill-hole}
Der Algorithmus kann manchmal unerwünschte Löcher erzeugen. Wenn ein Loch weniger Vertices als diesen Wert hat, wird es gefüllt.

### Löcher {#holes}
![](/images/topology_holes_menu.webp)
Die meiste Zeit wird dein Objekt wahrscheinlich wasserdicht sein, d. h. das Mesh ist „geschlossen“.

Wenn dein Objekt Löcher hat, kannst du sie füllen. Beachte, dass dies nur bei „naiven“ Löchern funktioniert, es kann also nicht zwei separate Ränder „verschweißen“.

![](/videos/hole_filling.mp4)

::: tip
Wenn du den Voxel Remesher ausführst, werden alle Löcher automatisch geschlossen, egal ob du ihn auf ein oder mehrere Meshes anwendest.
:::

#### Löcher schließen {#close-holes}
Führt die Hole-Close-Aktion aus.

#### ![](/icons/cog.webp) Zahnrad-Menü Löcher {#holes-gear-menu}
Das Gear-Menü hat diese erweiterten Optionen:

##### Detail {#fill-detail}
Die Polygon-Dichte, die zum Füllen des Lochs verwendet wird. Während du diesen Slider ziehst, wird ein Schachbrettmuster auf dem Modell angezeigt, das einen Hinweis auf die zu verwendende Dreiecksgröße gibt. Die Checkbox deaktiviert dies und verwendet nur die vorhandenen Punkte, was normalerweise lange, dünne Dreiecke über dem Loch erzeugt, die schwer zu modellieren sind.

##### Nicht-manifold füllen {#fill-non-manifold}
Versucht, nicht-manifold Löcher zu füllen.

##### Flächengruppe {#fill-face-group}

Beim Füllen von Löchern: Soll jedes Loch seine eigene Facegroup erhalten (Auto), sollen sie sich eine Facegroup teilen (Off) oder sollen keine Facegroups erstellt werden (On)?

### Manifold erzwingen {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Versucht, nicht-manifold Kanten zu bereinigen. Das kann für externe Software nützlich sein, die keine Kanten unterstützt, die mehr als 2 Flächen gemeinsam haben.

#### Bereinigen {#clean}
Führt die Clean-Aktion aus.
#### ![](/icons/cog.webp) Zahnrad-Menü Manifold erzwingen {#force-manifold-gear-menu}
Das Gear-Menü hat diese erweiterten Optionen:

#### Kleine Flächen löschen {#delete-small-faces}
Ein Schwellenwert, um kleine Polygone zu entfernen und zu verbinden.


### Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Konvertiert das Mesh in ein [Triplanar](scene.md#triplanar)-Primitive.
Du wirst dabei wahrscheinlich viele Details verlieren.

#### Kubisch erzwingen {#force-cubic}
Erzwingt, dass das Triplanar ein Würfel ist. Andernfalls passt sich das Triplanar der engsten Bounding Box um dein Objekt an.

#### Konvertieren {#convert}
Führt die Triplanar-Aktion aus.

#### Auflösung {#triplanar-resolution}
Die Voxelgröße, die in der Triplanar-Operation verwendet wird.

## ![](/icons/dot.webp) Primitive {#primitive}
Parameter für das ausgewählte Primitive. Diese sind auch in der Primitive-Toolbar im Viewport verfügbar.

![](/images/topology_primitive_screenshot.webp)