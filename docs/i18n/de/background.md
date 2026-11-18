# ![](/icons/image.webp) Hintergrund {#background}

In diesem Menü legen Sie die Hintergrundfarbe von Nomad fest und fügen Referenzbilder hinzu.

![](/images/background_overview.webp)

## Typ {#type}
![](/images/background_selector.webp)

Für den Hintergrund des Ansichtsfensters gibt es drei Möglichkeiten.

* `Umgebung` - Zeigt die Umgebungstextur an, die unter [Shading](shading.md) gewählt ist. Mit den Reglern `Unschärfe` und `Belichtung` (Helligkeit) können Sie sie weiter anpassen. 
* `Farbe` - Eine einheitliche Farbe Ihrer Wahl
* `Farbverlauf` - Ein Übergang zwischen zwei Farben. Mit dem Regler `Faktor` verschieben Sie die Mitte des Verlaufs.  

### Art des Verlaufs {#gradient-type}
Bei `Farbverlauf` wählen Sie seine Form:
* `Linear` - Ein gerader Verlauf, dessen Richtung Sie mit dem Regler `Winkel` festlegen.
* `Radial` - Ein kreisförmiger Verlauf, der von der Bildschirmmitte ausgeht.
* `Himmel` - Ein Verlauf, der am Horizont der Welt ausgerichtet ist und daher der Kamera folgt, wenn Sie nach oben oder unten schauen.

Jede Farbe hat eine Schaltfläche zum Zurücksetzen und eine Pipette, mit der Sie eine Farbe vom Bildschirm aufnehmen.

## ![](/icons/lock.webp) Mit Kameralock synchronisieren {#sync-on-camera-lock}
Wenn die Kamera mit dem [Navigator](settings.md#snap-cube) gesperrt ist, folgt das Referenzbild der Kamerabewegung und bleibt so deckungsgleich mit Ihrer Skulptur.

* `Rollen erlauben` - Erlaubt der Kamera zu rollen, sobald Sie die Kamerasperre verlassen.
* `Beim Entsperren zurücksetzen` - Setzt die Ansicht zurück, sobald Sie die Kamerasperre verlassen.

## Referenzbild {#reference}

![](/images/background_reference.webp)

Sie können ein beliebiges Bild als Referenz in den Hintergrund legen. Tippen Sie auf `Import`, um eines hinzuzufügen, und aktivieren Sie dann `Referenzbild`, um es anzuzeigen.
Position und Größe lassen sich ändern, zum Beispiel wenn Sie das Bild in eine Ecke des Bildschirms schieben möchten.

### ![](/icons/tool_transform.webp) Transformieren {#transform}

Mit dieser Schaltfläche platzieren Sie das Referenzbild direkt auf dem Bildschirm. Verschieben, skalieren und drehen Sie es mit 2 Fingern an die gewünschte Stelle. `Einstellungen zurücksetzen` bringt das Bild an seine ursprüngliche Position zurück. Die endgültige Platzierung wird in den Reglern darunter übernommen:

* `Überlagern` - Bei 0 % liegt das Referenzbild immer hinter Ihren Objekten, bei 100 % davor. 
* `Deckkraft` - Wie durchsichtig das Bild ist.
* `Nachbearbeitung` - Wendet die Effekte der Nachbearbeitung auch auf das Referenzbild an. Schalten Sie es aus, um die Originalfarben zu behalten.
* `X-Position` / `Y-Position` - Die X- und Y-Position des Bildes.
* `Skalierung` - Größe des Bildes.
* `Rotation` - Drehung des Bildes.


::: tip

Kameras und Referenzbilder sind miteinander verknüpft. 

Wenn Sie also Ihr Referenzbild passend zu Ihrer Skulptur ausgerichtet haben und dann im [Kamera-Menü](camera.md) eine Kamera erstellen, werden Position, Rotation und Größe des Referenzbilds mit der Kamera gespeichert. Sie können das Referenzbild ausschalten und in eine andere Ansicht drehen. Sobald Sie wieder durch die Kamera schauen, wird das Referenzbild mit Ihren Einstellungen wieder eingeblendet.

Sie können sogar für jede Kamera ein anderes Bild verwenden!

 ![](/videos/reference_camera.mp4)

:::
