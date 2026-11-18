# ![](/icons/symmetry.webp) Symmetrie {#symmetry}

Dieses Menü legt fest, wie Striche an einer Spiegelebene, radial oder als Kacheln wiederholt werden, und bietet Möglichkeiten, die Symmetrie bei nicht symmetrischen Objekten wiederherzustellen.

![](/images/symmetry_overview.webp) 

## Überblick {#overview}
Sie können die Symmetrie auf verschiedene Arten nutzen:

* Als Spiegel, der Ihre Arbeit an X (links/rechts), Y (oben/unten), Z (hinten/vorne) oder einer Kombination davon spiegelt.
* Radiale Symmetrie lässt sich auf X, Y und Z mit einer bestimmten Anzahl an Wiederholungen einstellen, etwa um einen Seestern zu modellieren.
* Kacheln wiederholt Ihre Striche über das Objekt hinweg, sodass sich das Modell nahtlos kacheln lässt.
* Spiegel können um den Ursprung (Welt-Modus genannt) oder um die Mitte eines Objekts (lokaler Modus genannt) arbeiten.
* Modelle, die nicht symmetrisch begonnen wurden, können nachträglich symmetrisch gemacht werden.

Eine Verknüpfung zum Ein- und Ausschalten der Symmetrie finden Sie auch in der linken Schnellleiste (*„Sym“*). Das kleine „L/W“ zeigt an, ob sich Nomad im lokalen oder im Welt-Symmetriemodus befindet. Sie können die Schaltfläche auch lange gedrückt halten oder zur Bildschirmmitte wischen, um ein Menü aufzurufen.

![](/images/symmetry_button.webp) 

Die Symmetrie-Einstellungen werden mit jedem Objekt gespeichert, und der Menütitel zeigt den Namen des Objekts, das Sie gerade bearbeiten.
Die Sculpting-Werkzeuge teilen sich denselben Ein/Aus-Zustand, während die Transformationswerkzeuge ([Transformieren](tools.md#transform) und [Gizmo](tools.md#gizmo)) ihren eigenen haben.

::: tip
Das Symmetrie-Menü dient hauptsächlich dazu, die Symmetrie der Striche zu steuern. Objekte können Sie auch über die [Repeater im Szene-Menü](scene#repeaters) spiegeln und wiederholen.
:::

## ![](/icons/symmetry.webp) Aktiviert {#enabled}
Schaltet den Spiegelmodus ein und aus; das entspricht der Schaltfläche `Sym` in der linken Schnellleiste. Ein Warnsymbol erinnert Sie daran, wenn sie ausgeschaltet ist, und das Menü weist Sie auch darauf hin, wenn das aktuelle Werkzeug die Symmetrie ignoriert.

## Ebenen {#planes}

Aktivieren Sie hier die Symmetrieebene(n) und die Anzahl der Wiederholungen für die radiale Symmetrie. Sie müssen sich nicht auf eine einzige Ebene beschränken: Für komplexe Symmetrien können Sie 1, 2 oder alle 3 Ebenen gleichzeitig aktivieren.

Die Zeile `Radial` legt die Anzahl der Wiederholungen für die radiale Symmetrie um jede Achse fest. Auch diese sind nicht auf eine einzige Achse beschränkt und lassen sich sogar mit der Ebenensymmetrie kombinieren, um sehr schnell detaillierte Ergebnisse zu erzielen. (Die Gesamtzahl der Wiederholungen ist auf 200 begrenzt.)

![](/videos/symmetry_demo.mp4) 

## Kachel {#tile}

Wiederholt Ihre Striche entlang einer Achse in regelmäßigem Abstand, sodass sich das Modell nahtlos kacheln lässt. Praktisch für Muster, Ziegelsteine oder eine Textur, die Sie wiederholen möchten.

Schalten Sie das Kacheln für jede Achse mit den Schaltflächen `Kachel` ein und legen Sie dann entweder eine `Anzahl` (wie viele Wiederholungen das Objekt überspannen) oder einen `Abstand` (den Raum zwischen zwei Wiederholungen) fest. Tippen Sie auf den Schalter links, um zwischen beiden zu wechseln.

## Methode {#method}
Der Spiegel kann entweder `Lokal` sein und sich mit dem Objekt bewegen, oder `Welt` und sich nicht bewegen. Wenn Sie nicht sicher sind, welchen Modus Sie brauchen, achten Sie auf die Anzeigen für Spiegelebene und radiale Symmetrie, die über dem Objekt eingeblendet werden. Im lokalen Modus bewegen sich die Spiegelanzeigen mit, wenn Sie das Modell mit den Transformationswerkzeugen (`Gizmo` oder `Transformieren`) verschieben. Im Welt-Modus bleiben die Spiegelanzeigen fest stehen, und das Objekt gleitet durch sie hindurch.

## Spiegel {#mirroring}
![](/images/symmetry_mirroring.webp)

Beim Sculpten nahe den Symmetrieebenen verhalten sich manche Pinsel nicht ganz symmetrisch. In diesem Bereich können Sie die Symmetrie wiederherstellen, indem Sie eine Seite Ihres Modells auf die andere kopieren.

`Richtung` - Die beiden Pfeilschaltflächen neben dem Titel `Spiegel` bestimmen, welche Seite auf die andere kopiert wird. Nomad berechnet dies aus Ihrem aktuellen Viewport, sodass die Seite auf dem Bildschirm dieselbe bleibt, egal aus welcher Richtung Sie das Modell betrachten.

![](/icons/shield.webp) `Maske` - Mit der Masken-Schaltfläche können Sie eingrenzen, was gespiegelt wird: Maskieren Sie die Zielseite, wird dieser Bereich geschützt; maskieren Sie die Quellseite, wird dieser Bereich nicht auf die Zielseite gespiegelt.

![](/icons/tool_hide.webp) `Ausblenden` - Ist diese Option aktiv, werden auf der Quellseite ausgeblendete Bereiche nicht auf die Zielseite gespiegelt.

`Spiegel` (Topologie beibehalten) versucht zu erkennen, ob die Topologie auf beiden Seiten des Spiegels gleich ist, und verschiebt in diesem Fall einfach die Vertices. Das ist der häufigste Fall. Radiale Symmetrie wird dabei ignoriert. Ist die Topologie nicht symmetrisch, bietet Nomad an, die Spiegelung stattdessen mit `Ausschneiden • Spiegel` zu erzwingen.

Die Schaltflächen `Ausschneiden` schneiden das Objekt entlang der Symmetrieebene(n) auf. Sie verändern die Topologie und greifen daher stärker ein als `Spiegel`. Die Zahl auf jeder Schaltfläche gibt an, wie viele Objekte Sie erhalten:

* `Ausschneiden` - entfernt eine Seite des Objekts.
* `Ausschneiden • Spiegel` - schneidet das Objekt auf, kopiert eine Seite, spiegelt sie auf die andere und verschweißt die Vertices entlang des Spiegels. Diese Methode ist manchmal nötig, wenn sich das Modell auf beiden Seiten des Spiegels stark unterscheidet.
* `Ausschneiden • Teilen` - schneidet das Objekt auf und behält jede Seite als eigenes Objekt.
* `Ausschneiden • Spiegel • Teilen` - wie `Ausschneiden • Spiegel`, aber jede Seite wird zu einem eigenen Objekt.

Sind mehrere Objekte ausgewählt, wirken `Spiegel` und [Objekt umdrehen](#flip-object) auf alle.

### Objekt umdrehen {#flip-object}
![](/images/symmetry_flip.webp)
Macht die linke Seite zur rechten und umgekehrt, entlang `X`, `Y` oder `Z`. Das Ergebnis sieht so aus, als hätten Sie im Gizmo-Werkzeugmenü die Skalierung auf X auf -1 gesetzt.

## Zurücksetzen und Bearbeiten {#reset-and-edit}

![](/images/symmetry_edit.webp)

Sie können Position und Ausrichtung der Symmetrie bearbeiten (das wird aber nicht empfohlen!). Bei Bedarf setzen `Weltzentrum` (`Objektzentrum` im lokalen Modus) und `Orientierung` Position und Ausrichtung der Symmetrie auf ihre Standardwerte zurück.

Nomad weiß normalerweise, wo die Symmetrieebene hingehört. Es wird nicht empfohlen, sie von Hand anzupassen, aber die Schaltfläche `Gizmo bearbeiten` erlaubt dies fortgeschrittenen Nutzern. Wenn Sie darauf tippen, erscheint ein Gizmo, mit dem Sie die Symmetrieebene verschieben und drehen können. Um wieder die Standardmitte und -ausrichtung herzustellen, verwenden Sie die Schaltflächen zum Zurücksetzen oben.

`Vom Drehpunkt` legt die Symmetrieebene auf den Drehpunkt des Werkzeugs [Gizmo](tools.md#gizmo). Diese Option ist nur verfügbar, solange das Werkzeug `Gizmo` aktiv ist.

Wie sich diese Optionen verhalten, hängt davon ab, in welchem Raum (*Lokal/Welt*) Sie sich befinden.
Wenn also etwas nicht wie erwartet funktioniert, prüfen Sie, ob Sie im richtigen Raum sind.

::: tip
Das Bearbeiten der Symmetrieebene mit dem Gizmo ist noch etwas experimentell; Sie werden es wahrscheinlich nicht brauchen!
:::

## Anzeigeoptionen {#show-options}
![](/images/symmetry_show.webp)


`Linie anzeigen` und `Ebene anzeigen` schalten eine Viewport-Einblendung der Symmetrieposition ein und aus. Das Ausschalten dieser Optionen wird erst wirksam, wenn das Symmetrie-Menü geschlossen ist.
