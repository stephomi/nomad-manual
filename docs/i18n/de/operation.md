# ![](/icons/operation.webp) Aktion {#operation}

Dieses Menü wendet eine Operation auf einen Schlag auf die gesamte Oberfläche der ausgewählten Objekte an: glätten, entspannen, polieren, aufblähen, Farben anpassen, die Bemalung und die Maske weichzeichnen oder schärfen.

![](/images/operation_overview.webp)

## Überblick {#overview}

Während ein Pinsel nur dort wirkt, wo Sie einen Strich ziehen, wirkt eine Operation in einem Durchgang auf jeden Vertex der ausgewählten Objekte. Der Titel zeigt den Namen des Objekts an, oder die Anzahl der Objekte, wenn mehrere ausgewählt sind.

Jede Operation ist ein Schieberegler: Ziehen Sie ihn nach rechts, um mehr anzuwenden, nach links, um weniger anzuwenden (oder die gegenteilige Operation, bei Reglern mit einem Pfeil auf beiden Seiten). Der Regler springt zurück auf null, sobald Sie ihn loslassen, und jedes Ziehen ist ein einzelner Schritt im [Verlauf](history.md). So können Sie eine Operation mehrmals in kleinen Dosen anwenden.

::: tip
Die Operationen sind ein schneller Weg, ein ganzes Mesh nach einem Voxel-Remeshing oder einem Boolean aufzuräumen: Ein wenig `Entspannen` gleicht die Dreiecke aus, ein wenig `Glätten` entfernt das Rauschen, ohne dass Sie jede Stelle mit einem Pinsel suchen müssen.
:::

## Filter {#filters}

Die Schaltflächen oben schränken ein, wo die Operationen wirken:

* `Maske` - Maskierte Bereiche bleiben unverändert.
* `Ausblenden` - Ausgeblendete Bereiche bleiben unverändert.
* `Versatz` - (Wenn eine [Ebene](layers.md) ausgewählt ist) Nur die Bereiche, in denen die aktive Ebene Sculpting enthält, sind betroffen. So können Sie den Inhalt einer Ebene glätten oder aufblähen, ohne den Rest anzutasten.

## Glättung {#smoothing}

* `Volumen bewahren` - Glättet, ohne dass die Oberfläche schrumpft. Die Zahnrad-Schaltfläche enthält die dafür verwendeten Werte `Schrumpfen` und `Aufblähen`.
* `Grenzen bewahren` - Vertices am Rand des Meshes (dem Rand eines Lochs) bleiben unbewegt.
* `Stabiles Glätten` - Versucht, die Glättung unabhängig von der Topologie zu machen. Das funktioniert am besten, wenn die Polygondichte stark schwankt.
* `Glätten` - Glättet die Oberfläche. Ziehen Sie nach links, um sie stattdessen zu `Schärfen`.
* ![](/icons/group.webp) `Glätten` - Glättet die Grenzen zwischen [Face-Gruppen](tools.md#facegroup) und begradigt so gezackte Gruppenumrisse. Ziehen Sie nach links, um sie zu schärfen.
* `Entspannen` - Gleicht die Polygone aus, ohne die Form zu verändern.
* ![](/icons/group.webp) `Entspannen` - Entspannt die Polygone entlang der Grenzen der Face-Gruppen.
* `Ecken bewahren` - Beim `Glätten` und `Entspannen` der Face-Gruppen bleiben die Grenzen dort fixiert, wo sie stärker als dieser Winkel abknicken. So bleiben die Ecken scharf, während die Seiten geglättet werden. Aktivieren Sie es über sein Kontrollkästchen.

## Polieren {#polish}

Plättet die Oberfläche zu sauberen Facetten, wie das Werkzeug [Polieren](tools.md#polish). `Winkel` legt fest, welche Flächen gemeinsam geplättet werden: Flächen, die weniger als dieser Winkel abknicken, werden zu einer Facette. Ein kleinerer Winkel erhält mehr Kanten und kleinere Facetten.

## Aufblähen {#inflate}

Drückt die Oberfläche entlang ihrer Normalen nach außen, oder nach innen, wenn Sie nach links ziehen. `Normal (Entspannen)` entspannt dabei gleichzeitig die Polygone, damit sie sich nicht verzerren; über sein Kontrollkästchen können Sie es ausschalten.

## Farbanpassungen {#color-adjustments}

Wählen Sie den Kanal, den Sie anpassen möchten: `Farbe`, `Matt`, `Metallisch`, `Deckkraft`, `Dichte` (das Dichte-Painting für den [Quad Remesher](tools.md#quad-remesher), sofern das Objekt welches hat) oder `Maske`. Dann:

* `Belichtung` - Hellt die Werte auf oder dunkelt sie ab.
* `Sättigung` - (Nur `Farbe`) Mehr oder weniger kräftige Farben.
* `Kontrast` - Spreizt die Werte auseinander oder rückt sie näher zusammen.
* `Farbton` - Verschiebt die Farben auf dem Farbkreis.

## Unschärfe {#blur}

Zeichnet die ausgewählten Kanäle über die Oberfläche weich: Schalten Sie `Farbe`, `Matt`, `Metallisch`, `Deckkraft`, `Dichte` oder `Maske` ein und ziehen Sie dann `Unschärfe`. Ziehen Sie nach links, um stattdessen zu `Schärfen`.

Für die Maske entspricht das dem Regler `Unschärfe` des Werkzeugs [Maske](tools.md#mask). Hier können Sie zusätzlich die Malkanäle weichzeichnen.
