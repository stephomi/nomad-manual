# ![](/icons/camera.webp) Kamera {#camera}

Dieses Menü ermöglicht es dir, Kameras zu erstellen und zu bearbeiten sowie zu steuern, wie du mit Kameras interagierst.

![](/images/camera_overview2.webp)

Kameras in Nomad haben mehrere Verwendungszwecke:

* Ansichten für das Sculpting aus präzisen Winkeln einrichten
* Wie eine Fotokamera verwenden, um deine Objekte zu rahmen
* Als Ego-Perspektiv-Kamera, um in deiner Szene zu navigieren
* Als orthografische Kamera für isometrische Spiele oder industrielle Renderings.

## Steuerung der Kamera {#control}

### Drehung {#rotation}
Du drehst die Kamera, indem du *einen* Finger auf dem Hintergrund ziehst.  
Wenn du den Finger auf deinem Modell ziehst, wird stattdessen die Sculpting-Operation gestartet.

::: tip Kann ich die Kamera drehen, wenn ich den Hintergrund nicht erreichen kann?
Ja, du kannst *zwei* Finger auf den Bildschirm legen – so als wolltest du eine Schwenk-/Zoom-Geste starten – und dann *einen* Finger loslassen.
:::

### Fokussieren / Zurücksetzen {#focus}
*Doppeltippe* auf das Modell, um auf den gewählten Punkt zu fokussieren.  
Wenn du *doppeltippst* auf den Hintergrund, fokussiert die Kamera stattdessen auf das ausgewählte Mesh.

### Verschiebung {#translation}
Durch Bewegen von *zwei* Fingern kannst du die Kamera schwenken.

### Zoomen {#zooming}
Mit der Pinch-Geste kannst du hinein- und herauszoomen.

### Rollen {#rolling}
Du kannst die Ansicht *rollen*, indem du *zwei* Finger drehst.
::: warning
Diese Geste ist nur im Rotationsmodus `Trackball` verfügbar.
:::

### Desktop‑Steuerung {#desktop}

Auf dem Desktop wird die Alt/Opt-Taste zur Steuerung der Kamera verwendet:

* Tippen und Ziehen im leeren Raum = Kamera drehen
* Alt+Tippen und Ziehen = schwenken
* Alt+Tippen und Ziehen, dann Alt loslassen = zoomen (wie in ZBrush)

Bei Wacom-Tablets mit 2 oder mehr Tasten am Stift kannst du in den Wacom-Einstellungen Spitze und Tasten wie folgt konfigurieren:

* Spitze = Linksklick
* unterer Wipptaster = Mittelklick
* oberer Wipptaster = Rechtsklick

Mit diesen Einstellungen kannst du die Kamera ausschließlich mit dem Stift steuern:

* oberer Wipptaster und Bewegen in der Schwebe = Kamera drehen
* unterer Wipptaster und Bewegen in der Schwebe = schwenken

## Kamerasteuerung {#camera-controls}

![](/images/camera_list.webp)

### Ansichten {#views}
Du kannst Kameraansichten mit `Add View` speichern.  
Wenn du auf den Namen der Ansicht klickst, stellt die Kamera diese Ansicht wieder her.

::: tip
Eine gespeicherte Ansicht speichert die Einstellungen des [Projektionstyps](#projection-type) sowie das [Referenzbild](background.md).  
Das ist nützlich, wenn du zwischen Vorder-/Links-/Rückansichten mit unterschiedlichen Hintergründen wechseln möchtest.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Toggle the camera. Hidden cameras will be skipped from previous/next button |
| Name        |                               | Select the camera                                                           |
| Image       | ![](/icons/image.webp)       | A thumbnail of a reference image if it is linked to the camera              |
| Update View | ![](/icons/update_view.webp) | Update the saved view with the current view point                           |
| Edit Name   | ![](/icons/pencil.webp)      | Edit the camera name                                                        |
| Delete      | ![](/icons/trash.webp)       | Delete the camera                                                           |

### ![](/icons/tool_view.webp) Ansicht hinzufügen {#add}
Erstellt eine neue Kamera basierend auf der aktuellen Ansicht.

### ![](/icons/camera.webp) Symbole {#icons-test}

Legt fest, ob Kamera-Icons im Viewport sichtbar sind. Wenn eine Kamera ausgewählt ist, ist ihr Icon immer sichtbar.

### Projektionsart {#projection}
Du kannst das `Field of View` (FOV / Brennweite) deiner Kamera ändern.  
Für Sculpting-Zwecke wird in der Regel ein niedriger FOV empfohlen, da dies bei den Proportionen helfen kann.  
Du kannst auch den `Orthographic`-Modus verwenden, der in etwa einem FOV von 0 entspricht.

### Ego-Perspektive {#fps}
Aktiviert das Setzen des Pivots direkt auf die Kamera anstatt auf die Skulptur. Das Ziehen eines Fingers auf dem Hintergrund hält die Kameraposition fest, ändert aber die Rotation – ähnlich wie in Ego-Shooter-Spielen. Nützlich beim Sculpting von Umgebungen statt einzelnen Objekten.

![](/images/camera_rotation_ortho_view.webp)

### Rotationsart {#rotation-type}
Standardmäßig verwendet die Kamera den Rotationsmodus `Turntable`.  
Das bedeutet, du hast nur zwei Freiheitsgrade; es ist intuitiver, aber in manchen Fällen möchtest du mehr Flexibilität.  
Du kannst auf `Trackball` umschalten; dann kannst du die Ansicht *rollen*, indem du *zwei* Finger im Viewport drehst. Auf dem Desktop gibt es einen alternativen Trackball-Modus, der einigen Nutzern vertrauter sein könnte.

### Orthogonales Einrasten {#orthographic}

Wenn aktiviert, wird beim Drehen der Ansicht mit gedrückter Umschalttaste (Shift) auf der Tastatur die Kamera auf die nächstgelegene Vorder-/Rück-/Ober-/Unter-/Links-/Rechtsansicht eingerastet und orthografisch gemacht.  
Die Kamera wird ebenfalls orthografisch, wenn der View-Würfel angeklickt wird, um auf Vorder-/Rück-/Links-/Rechts-/Ober-/Unteransicht einzurasten.

### Ansicht zurücksetzen {#reset}

Bewegt die Kamera nach vorne und passt die Szene in die Ansicht ein.

### Ansicht einrasten {#snap}
Rastet auf die nächstgelegene Vorder-/Rück-/Links-/Rechts-/Ober-/Unteransicht ein.  
Wenn du dich bereits in einer dieser Ansichten befindest, rastet ein erneuter Klick um 180 Grad auf die gegenüberliegende Seite ein.

### Geschwindigkeit {#speed}

Wenn dir die Kamera zu langsam oder zu schnell erscheint, kannst du einen Geschwindigkeitsmultiplikator für `rotation`, `translation` und `zooming` einstellen.  
Nützlich, wenn deine Skulptur sehr groß oder sehr klein ist.

### Pivot-Übersicht {#pivot}

Wenn du die Kamera drehst, siehst du einen kleinen pinken Punkt – das ist dein Kamera-Pivot-Punkt.  
Es ist sehr wichtig zu verstehen, wo sich dein Pivot befindet, damit du dich nicht verirrst oder von der Kamera frustriert wirst.

Standardmäßig wird der Pivot durch folgende Aktionen aktualisiert:
- Doppeltippen auf das Modell
- Doppeltippen auf den Hintergrund (der neue Pivot befindet sich im Zentrum deines Meshes)
- das Auflegen von *zwei* Fingern auf den Bildschirm (Schwenken/Zoomen/Rollen) aktualisiert den Pivot auf das Zentrum der *zwei* Finger

### Pivot aktualisieren... {#update-pivot}

Du kannst das Aktualisieren des Pivots mit diesen Optionen weiter anpassen:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Wenn du dich daran gewöhnt hast, kannst du den (Hinweis-)Punkt in Pink ausblenden, indem du in die [Einstellungen](settings.md) gehst.
:::

### Doppeltippen auf Objekt {#dtap-object}
Wenn `Focus` aktiviert ist, verschiebt Doppeltippen den Pivot auf das angetippte Objekt.

### Doppeltippen auf Hintergrund {#dtap-tap-background}
Wenn aktiviert, setzt dies den Pivot auf eine der Optionen Selection, Scene oder wechselt zwischen ihnen.