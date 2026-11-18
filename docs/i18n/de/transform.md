# ![](/icons/transform.webp) Transformieren {#transform}

Dieses Menü zeigt die Transformation des ausgewählten Objekts als Zahlen: wo es sich befindet, wie es gedreht und skaliert ist und wie groß es ist. Sie können exakte Werte eingeben, sie zurücksetzen oder in das Mesh einbacken.

![](/images/transform_overview.webp)

## Überblick {#overview}

Jedes Objekt hat zusätzlich zu seinen Vertices einen Knoten, der seine Verschiebung, Rotation und Skalierung speichert (seine Matrix). Die Werkzeuge [Gizmo](tools.md#gizmo) und [Transformieren](tools.md#transform) ändern diese Matrix, wenn Sie im Viewport ziehen; mit diesem Menü können Sie sie ablesen und die Werte stattdessen eintippen. Unter [Knoten und Vertices](tools.md#nodes-and-vertices) erfahren Sie, worin der Unterschied zwischen dem Verschieben des Knotens und dem Verschieben der Vertices besteht.

Ziehen Sie einen Wert nach links oder rechts, um ihn zu ändern, oder tippen Sie darauf, um eine Zahl einzugeben. Die Werte für X, Y und Z sind wie die Achsen des Gizmos rot, grün und blau eingefärbt.

::: tip
Werte einzutippen ist praktisch, um Objekte genau zu platzieren, zum Beispiel um mehrere Teile auf exakt dieselbe Höhe zu bringen oder um eine Rotation nach freiem Drehen mit dem Gizmo wieder auf eine runde Zahl zu setzen.
:::

## Matrix {#matrix}

Der Titel zeigt Ihnen, in welchem Raum die Werte angegeben sind: `Lokal` (relativ zum übergeordneten Objekt) oder `Welt`.

### Objekt und Drehpunkt {#object-pivot}

* `Objekt` - Die Werte sind die eigene Transformation des Objekts.
* `Drehpunkt` - Die Werte steuern die Auswahl von ihrem [Drehpunkt](tools.md#pivot) aus, so wie es die Griffe des Gizmos tun: Die Zeilen zeigen null an, und wenn Sie sie ändern, wird die Auswahl um den Drehpunkt verschoben, gedreht oder skaliert. Aktivieren Sie `Bearbeiten` (das Schloss-Symbol), um nur den Drehpunkt zu verschieben, während die Objekte stehen bleiben.

### Lokal und Welt {#local-world}

Wenn das Objekt ein übergeordnetes Objekt oder untergeordnete Objekte hat oder mehrere Objekte ausgewählt sind, können Sie wählen, in welchem Raum die Werte angezeigt werden: `Lokal` (relativ zum übergeordneten Objekt) oder `Welt`.

### Aktionen {#actions}

| Aktion        | Symbol                        | Beschreibung |
| :-----------: | :---------------------------: | :---------- |
| Zum Ursprung  | ![](/icons/target.webp)      | Verschiebt das Objekt zum Weltursprung. |
| Anwenden      | ![](/icons/bake.webp)        | Wendet die Matrix auf die Vertices an und setzt die Matrix zurück. Optisch ändert sich nichts, aber der Ursprung des Objekts ist jetzt der Weltursprung. |
| Drehpunkt     | ![](/icons/gizmo.webp)       | Backt den Drehpunkt in das Objekt ein: Ursprung und Ausrichtung des Objekts werden zu denen des Drehpunkts. Optisch ändert sich nichts. |
| Bearbeiten    | ![](/icons/lock.webp)        | (Modus `Drehpunkt`) Verschiebt nur den Drehpunkt. |
| Zurücksetzen  | ![](/icons/reset.webp)       | Setzt die Transformation auf die Identität zurück. Im Modus `Drehpunkt` wird stattdessen der Drehpunkt wieder an seinen Platz gesetzt. |

Hat das ausgewählte Objekt Instanzen, fragt das Einbacken nach einer Bestätigung und bietet die Option `Instanz aufheben` an: Das Einbacken ändert die Vertices, und die teilen sich alle Instanzen.

### Verschiebung, Rotation, Skalierung {#translation-rotation-scale}

Position, Rotation (in Grad) und Skalierung des Objekts auf X, Y und Z. Die beiden Schaltflächen am Ende jeder Zeile backen nur diesen Teil der Transformation in die Vertices ein oder setzen ihn zurück.

Eine Zeile `Scherung` erscheint außerdem, wenn das Objekt geschert ist, zum Beispiel nach einer ungleichmäßigen Skalierung eines gedrehten übergeordneten Objekts.

### Gleichmäßige Skalierung {#uniform-scale}

Ist diese Option aktiviert, ist die Skalierung ein einziger Wert, der auf allen drei Achsen gleich ist. Deaktivieren Sie sie, um X, Y und Z getrennt zu skalieren.

## Abmessungen {#dimension}

Größe und Mittelpunkt der Bounding Box der Auswahl, in Welteinheiten. Sind mehrere Objekte ausgewählt, umfasst sie alle.

* `Größe` - Breite, Höhe und Tiefe. Ist die Verknüpfungsschaltfläche aktiv, skaliert das Ändern einer Größe die beiden anderen um denselben Faktor, sodass die Proportionen erhalten bleiben.
* `Zentriert` - Der Mittelpunkt der Bounding Box. Die Zielschaltfläche verschiebt die Auswahl so, dass ihr Mittelpunkt im Weltursprung liegt.

::: tip
Mit `Größe` geben Sie einem Objekt am schnellsten eine reale Größe, zum Beispiel vor einem 3d-Druck: Stellen Sie die gewünschte Höhe ein, und die Verknüpfung behält die Proportionen bei.
:::
