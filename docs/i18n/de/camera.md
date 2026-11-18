# ![](/icons/camera.webp) Kamera {#camera}

In diesem Menü können Sie Kameras erstellen und bearbeiten und festlegen, wie Sie mit ihnen interagieren.

![](/images/camera_overview2.webp)

Kameras haben in Nomad mehrere Verwendungszwecke:

* Ansichten einrichten, um aus genauen Blickwinkeln zu sculpten
* wie ein Fotoapparat, um Ihre Objekte ins Bild zu setzen
* als Kamera aus der Ego-Perspektive, um sich durch Ihre Szene zu bewegen
* als orthographische Kamera für isometrische Spiele oder Renderings im Stil technischer Zeichnungen.

## Die Kamera steuern {#control}

### Rotation {#rotation}
Sie drehen die Kamera, indem Sie *einen* Finger über den Hintergrund ziehen.
Ziehen Sie den Finger stattdessen über Ihr Modell, beginnen Sie damit zu sculpten.

::: tip Kann ich die Kamera drehen, wenn ich den Hintergrund nicht erreiche?
Ja: Legen Sie *zwei* Finger auf den Bildschirm, als wollten Sie verschieben oder zoomen, und heben Sie dann *einen* Finger an.
:::

### Fokus / Zurücksetzen {#focus}
*Doppeltippen* Sie auf das Modell, um auf den angetippten Punkt zu fokussieren.
Wenn Sie auf den Hintergrund *doppeltippen*, fokussiert die Kamera stattdessen auf das ausgewählte Mesh oder die ganze Szene, siehe [Auf Hintergrund doppeltippen](#dtap-tap-background).


### Schwenken {#translation}
Indem Sie *zwei* Finger bewegen, schwenken Sie die Kamera.


### Zoomen {#zooming}
Mit der Zwei-Finger-Geste (Zusammen- und Auseinanderziehen) zoomen Sie hinein und heraus.


### Rollen {#rolling}
Sie können die Ansicht *rollen*, indem Sie *zwei* Finger drehen.
::: warning
Diese Geste ist nur in den Rotationsmodi `Trackball` verfügbar.
:::

### Steuerung am Desktop {#desktop}

Am Desktop steuern Sie die Kamera mit der Alt-/Wahltaste:

* mit der Stiftspitze in einen leeren Bereich ziehen = Kamera drehen
* Alt + mit der Stiftspitze ziehen = schwenken
* Alt + mit der Stiftspitze ziehen, dann Alt loslassen = zoomen (wie in ZBrush)

Bei Wacom-Tablets mit 2 oder mehr Tasten am Stift richten Sie Spitze und Tasten in den Wacom-Einstellungen so ein:

* Spitze = Linksklick
* untere Wipptaste = Mittelklick
* obere Wipptaste = Rechtsklick

Mit diesen Einstellungen können Sie die Kamera allein mit dem Stift bedienen:

* obere Wipptaste und Stift schwebend bewegen = Kamera drehen
* untere Wipptaste und Stift schwebend bewegen = schwenken

## Kamerasteuerung {#camera-controls}

![](/images/camera_list.webp)

### Ansichten {#views}
Mit `Ansicht hinzufügen` können Sie Kamerablickwinkel speichern.
Wenn Sie auf den Namen der Ansicht tippen, stellt die Kamera diese Ansicht wieder her.


::: tip
Eine gespeicherte Ansicht speichert die Einstellungen der [Projektion](#projection) und auch das [Referenzbild](background.md).  
Das ist praktisch, wenn Sie zwischen Referenzansichten von vorne, links und hinten mit unterschiedlichen Hintergründen wechseln möchten.
:::

| Aktion      | Symbol                        | Beschreibung                                                                |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Sichtbarkeit | ![](/icons/eye_open.webp)    | Schaltet die Kamera ein und aus. Ausgeblendete Kameras werden von den Schaltflächen Zurück/Weiter übersprungen |
| Name        |                               | Wählt die Kamera aus                                                        |
| Bild        | ![](/icons/image.webp)       | Eine Miniatur des Referenzbilds, falls eines mit der Kamera verknüpft ist   |
| Projektion  | ![](/icons/perspective.webp) | Die Projektion der Kamera, in der Perspektive mit ihrem Sichtfeld          |
| Ansicht aktualisieren | ![](/icons/update_view.webp) | Aktualisiert die gespeicherte Ansicht mit dem aktuellen Blickwinkel |
| Name bearbeiten | ![](/icons/pencil.webp)  | Bearbeitet den Namen der Kamera                                             |
| Löschen     | ![](/icons/trash.webp)       | Löscht die Kamera                                                           |

### ![](/icons/camera_add.webp) Ansicht hinzufügen {#add}
Erstellt eine neue Kamera aus der aktuellen Ansicht.

### ![](/icons/camera.webp) Icons {#icons-test}

Legt fest, ob die Kamera-Icons im Viewport sichtbar sind. Die Schaltfläche erscheint neben `Ansicht hinzufügen`, sobald Sie eine Kamera haben. Das Icon einer ausgewählten Kamera ist immer sichtbar.

### Projektion {#projection}
Wählen Sie zwischen `Perspektivisch` und `Orthographisch`.

In der Perspektive können Sie das `Vertikales FoV` (Sichtfeld) Ihrer Kamera ändern. Über dem Regler wird die entsprechende Brennweite einer 35-mm-Kamera angezeigt, praktisch, wenn Sie aus der Fotografie kommen.
Zum Sculpten empfiehlt sich meist ein kleines Sichtfeld, weil es hilft, die Proportionen richtig einzuschätzen.  
Der Modus `Orthographisch` entspricht ungefähr einem Sichtfeld von 0.

### Erste Person {#fps}
Nur in der Perspektive. Legt den Drehpunkt direkt auf die Kamera statt auf das Modell. Wenn Sie einen Finger über den Hintergrund ziehen, bleibt die Position der Kamera fest und nur ihre Drehung ändert sich, ähnlich wie in Ego-Shootern. Nützlich, wenn Sie ganze Umgebungen statt einzelner Objekte sculpten.

![](/images/camera_rotation_ortho_view.webp)

### Rotationsmodus {#rotation-type}
Standardmäßig verwendet die Kamera den Rotationsmodus `Drehscheibe`.
Dabei haben Sie nur zwei Freiheitsgrade; das ist intuitiver, aber manchmal braucht man mehr Flexibilität.  
Sie können zu `Trackball` wechseln; dann können Sie die Ansicht *rollen*, indem Sie *zwei* Finger auf dem Viewport drehen. Es gibt zwei `Trackball`-Modi: Der erste rollt die Ansicht wie eine Kugel unter Ihrem Finger, der zweite (mit dem Pfeil-Icon) dreht die Ansicht anhand der waagerechten und senkrechten Bewegung Ihres Ziehens, was manchen Nutzern vertrauter sein dürfte.

### Orthografisch ausrichten {#orthographic}

Ist diese Option aktiviert und haben Sie eine Tastatur, rastet die Kamera beim Drehen der Ansicht mit gedrückter Umschalttaste auf die nächstgelegene Ansicht von vorne/hinten/oben/unten/links/rechts ein und wird orthographisch. Die Kamera wird auch orthographisch, wenn Sie auf den Navigator tippen, um auf eine Ansicht von vorne/hinten/links/rechts/oben/unten zu springen.

### Ansicht zurücksetzen {#reset}

Bewegt die Kamera nach vorne und passt die Szene in die Ansicht ein.

### Ansicht ausrichten {#snap}
Springt zur nächstgelegenen Ansicht von vorne/hinten/links/rechts/oben/unten. Wenn Sie sich bereits in einer dieser Ansichten befinden, springt ein erneutes Tippen um 180 Grad auf die gegenüberliegende Seite.

### Geschwindigkeit {#speed}

Wenn Ihnen die Kamera zu langsam oder zu schnell vorkommt, können Sie einen Geschwindigkeitsfaktor für `Rotation`, `Zoomen` und `Schwenken (Pan)` einstellen. Nützlich, wenn Ihr Modell sehr groß oder sehr klein ist.

### Der Drehpunkt im Überblick {#pivot}

Wenn Sie die Kamera drehen, sehen Sie einen kleinen rosa Punkt: Das ist der Drehpunkt Ihrer Kamera.  
Es ist sehr wichtig zu verstehen, wo Ihr Drehpunkt liegt, damit Sie sich nicht verirren oder sich über die Kamera ärgern.

Standardmäßig wird der Drehpunkt durch diese Aktionen aktualisiert:
- Doppeltippen auf das Modell
- Doppeltippen auf den Hintergrund (der neue Drehpunkt liegt dann in der Mitte Ihres Meshes)
- *zwei* Finger auf den Bildschirm legen (schwenken/zoomen/rollen) setzt den Drehpunkt in die Mitte zwischen den *zwei* Fingern

### Drehpunkt aktualisieren… {#update-pivot}

Mit diesen Optionen können Sie genauer festlegen, wann der Drehpunkt aktualisiert wird:

* `Bei Kamerabewegung` - Aktualisiert den Drehpunkt, sobald Sie mit der Kamera interagieren.
* `Drehpunkt außerhalb` - Erlaubt einen neuen Drehpunkt auch dann, wenn Sie außerhalb der Objektoberfläche zoomen. Erfordert `Bei Kamerabewegung`.
* `Beim Doppeltippen` - Aktualisiert den Rotations-Drehpunkt, wenn Sie auf die Objektoberfläche doppeltippen.
* `Bearbeiten (Strich)` - Aktualisiert den Drehpunkt beim Sculpten.

::: tip
Wenn Sie sich daran gewöhnt haben, können Sie den rosa Hinweispunkt im Menü [Einstellungen](settings.md) ausblenden.
:::

### Ansicht zentrieren beim Herauszoomen {#center-view-when-zooming-out}
Beim Herauszoomen schwenkt die Kamera nicht zur Seite: Sie bewegt sich nur zurück, sodass die Ansicht zentriert bleibt.

### Doppelt auf Objekt tippen {#dtap-object}
Ist diese Option aktiviert, fokussiert ein Doppeltippen auf ein Objekt die Kamera auf den angetippten Punkt.

### Auf Hintergrund doppeltippen {#dtap-tap-background}
Ist diese Option aktiviert, fokussiert ein Doppeltippen auf den Hintergrund die Kamera auf:
* `Auswahl` - Die ausgewählten Objekte.
* `Szene` - Die ganze Szene.
* `Umschalten` - Wechselt bei jedem Doppeltippen zwischen beidem. Es gibt zwei `Umschalten`-Optionen; sie unterscheiden sich darin, welche zuerst kommt, wie ihre Icons zeigen.
