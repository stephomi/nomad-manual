# ![](/icons/symmetry.webp) Symmetrie {#symmetry}

Dieses Menü steuert, wie Striche über eine Spiegelachse oder radial wiederholt werden, sowie Möglichkeiten, Symmetrie bei nicht-symmetrischen Objekten wiederherzustellen.

![](/images/symmetry_overview.webp) 

## Übersicht {#overview}
Du kannst Symmetrie auf mehrere Arten verwenden:

* Als Spiegel, der die Arbeit über X (links/rechts), Y (oben/unten), Z (hinten/vorne) oder eine Kombination davon spiegelt. 
* Radialsymmetrie kann auf X, Y, Z mit einer Anzahl von Wiederholungen eingestellt werden, z. B. beim Modellieren eines Seesterns. 
* Spiegel können um den Ursprung (genannt Weltmodus) oder um das Zentrum eines Objekts (genannt Lokalmode) arbeiten.
* Skulpturen, die nicht symmetrisch begonnen wurden, können zur Symmetrie gezwungen werden.

Eine Abkürzung zum Aktivieren/Deaktivieren der Symmetrie findest du auch im linken Schnellpanel (*„Sym“*). Das kleine „L/W“ zeigt an, ob Nomad im lokalen oder weltbezogenen Symmetriemodus ist. Du kannst außerdem lange drücken oder zur Bildschirmmitte wischen, um ein Menü aufzurufen.

![](/images/symmetry_button.webp) 

Dies ist eine globale Option, daher wird der Zustand zwischen den verschiedenen Werkzeugen beibehalten.
Die einzigen Ausnahmen sind die Transformationswerkzeuge ([Verschieben](#translate), [Drehen](#rotate), [Skalieren](#scale) und [Gizmo](#gizmo)), die ihren eigenen Symmetriezustand haben.

::: tip
Das Symmetriemenü dient hauptsächlich zur Steuerung der Strichsymmetrie. Du kannst Objekte auch über [Replikatoren im Szenenmenü](scene#repeaters) spiegeln und wiederholen. 
:::

## Aktiviert {#enabled}
Schaltet den Spiegelmodus um, dies entspricht der `Sym`-Schaltfläche im linken Schnellpanel. 

## Ebenen {#planes}

Aktiviere Symmetrieebene(n) und die Anzahl der Wiederholungen für Radialsymmetrie. Beachte, dass du nicht nur eine einzelne Ebene wählen musst – du kannst 1, 2 oder alle 3 Ebenen für komplexe Symmetrie aktivieren.

Die Achse und Wiederholungsanzahl für Radialsymmetrie. Beachte, dass diese ebenfalls nicht auf eine einzelne Achse beschränkt sind und sogar in Kombination mit Ebenensymmetrie funktionieren können, um sehr schnell detaillierte Ergebnisse zu erzeugen. (Die Gesamtanzahl der Wiederholungen ist auf 150 begrenzt.)

![](/videos/symmetry_demo.mp4) 

## Methode {#method}
Der Spiegel kann entweder „Lokal“ sein und sich mit dem Objekt bewegen oder „Welt“ und sich nicht bewegen. Wenn du nicht sicher bist, welchen Modus du brauchst, beobachte die Spiegel- und Radialsymmetrie-Anzeigen, die über dem Objekt eingeblendet werden. Im lokalen Modus bewegen sich die Spiegelindikatoren mit, wenn du das Modell mit dem Transformationsgizmo verschiebst. Im Weltmodus bleiben die Spiegelindikatoren fixiert und das Objekt gleitet durch sie hindurch.

## Spiegelung {#mirroring}
![](/images/symmetry_mirroring.webp)

Beim Modellieren in der Nähe der Symmetrieebenen zeigen einige Pinsel ein unvollkommenes Symmetrieverhalten. Dieser Abschnitt ermöglicht es dir, die Symmetrie wiederherzustellen, indem du eine Seite deiner Skulptur auf die andere kopierst. 

`Richtung` – Die Schaltflächen `<<` und `>>` bestimmen, welche Seite auf die andere kopiert wird. Nomad berechnet dies aus deiner aktuellen Ansicht, sodass z. B. `<<` immer von rechts nach links auf dem Bildschirm kopiert.

![](/icons/shield.webp) `Maske` – Mit der Masken-Schaltfläche kannst du festlegen, was gespiegelt wird; das Maskieren der Zielseite schützt diesen Bereich, das Maskieren der Quellseite verhindert, dass dieser Bereich auf das Ziel gespiegelt wird. 

![](/icons/tool_hide.webp) `Verbergen` – Wenn aktiv, werden Bereiche, die auf der Quellseite verborgen sind, nicht auf das Ziel gespiegelt. 

`Spiegeln` versucht zu erkennen, ob die Topologie auf beiden Seiten des Spiegels gleich ist, und verschiebt in diesem Fall nur die Vertices. Dies ist das häufigere Szenario.

`Teilen & Spiegeln` schneidet das Objekt im Grunde entlang des Spiegels, kopiert eine Seite, spiegelt sie auf die andere und verschweißt die Vertices entlang des Spiegels. Es ist eine destruktivere Option und löscht Multiresolution, ist aber manchmal erforderlich, wenn das Modell über den Spiegel hinweg sehr unterschiedlich ist.

### Objekt spiegeln {#flip-object}
![](/images/symmetry_flip.webp)
Macht aus der linken Seite die rechte Seite und umgekehrt. Ähnelt optisch dem Ergebnis, wenn du im Gizmo-Werkzeugmenü die Skalierung auf -1 auf X setzt.

## Zurücksetzen und Bearbeiten {#reset-and-edit}

![](/images/symmetry_edit.webp)

Es ist möglich, die Position und Ausrichtung der Symmetrie zu bearbeiten (aber nicht empfohlen!). Falls nötig, setzen `Weltzentrum` und `Ausrichtung` die Symmetrieposition und -ausrichtung auf ihre Standardwerte zurück.

Nomad weiß normalerweise, wo die Symmetrieebene platziert werden soll. Es wird nicht empfohlen, dies manuell anzupassen, aber die Schaltfläche `Gizmo (Bearbeiten)` erlaubt dies für fortgeschrittene Nutzer. Wenn diese Schaltfläche angeklickt wird, erscheint ein Gizmo, mit dem du die Symmetrieebene verschieben und drehen kannst. Wenn du das Standardzentrum und die Standardausrichtung wiederherstellen möchtest, erledigen dies die Schaltflächen `Objektzentrum` und `Ausrichtung`.

Das Verhalten dieser Optionen ändert sich je nachdem, in welchem Raum (*Lokal/Welt*) du dich befindest.
Wenn es also nicht wie erwartet funktioniert, überprüfe, ob du im richtigen Raum bist.

::: tip
Die Schaltfläche `Gizmo (Bearbeiten)` ist absichtlich ausgegraut, als Erinnerung daran, dass du sie wahrscheinlich nicht verwenden solltest!
:::

## Optionen anzeigen {#show-options}
![](/images/symmetry_show.webp)


`Linie anzeigen` und `Ebene anzeigen` schalten eine Viewport-Überlagerung der Symmetriepositionen ein oder aus. Beachte, dass das Deaktivieren dieser Optionen erst wirksam wird, wenn das Symmetriemenü geschlossen wird.