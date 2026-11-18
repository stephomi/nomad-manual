# ![](/icons/history.webp) Verlauf {#history}
![](/images/history_overview.webp)

Wie in den meisten Kreativ-Apps können Sie in Nomad jede Bearbeitung rückgängig machen und wiederherstellen.
Der Verlauf kann sehr groß werden. Deshalb legen Sie selbst fest, wie viel davon im Arbeitsspeicher bleibt, wie viel auf dem Gerätespeicher abgelegt wird und ob er mit Ihrem Projekt gespeichert wird.

::: tip
Mit schnellen Gesten können Sie rückgängig machen und wiederherstellen:
- Mit 2 Fingern tippen, um rückgängig zu machen
- Mit 3 Fingern tippen, um wiederherzustellen
:::

## ![](/icons/history.webp) Verlauf {#history-panel}
![](/images/history_history.webp)

Dieses Panel zeigt den Verlauf an: die Anzahl der Schritte, den Namen der Aktion, das betroffene Objekt und wie viel Speicher jeder Schritt belegt.

Tippen Sie auf einen Eintrag, um zu diesem Zustand zurück- (oder vor-)zuspringen. Halten Sie einen Eintrag gedrückt, um ihn und den gesamten älteren Verlauf endgültig zu löschen. So geben Sie schnell Speicher frei, wenn Sie mit Ihrer Skulptur zufrieden sind.

### ![](/icons/speed.webp) Wiedergeben {#replay}
Die Wiedergabetaste unten links springt zum Anfang zurück und wiederholt dann die Aktionen eine nach der anderen. So können Sie zusehen, wie Ihre Skulptur entsteht. Der Regler legt die Geschwindigkeit in Aktionen pro Sekunde fest. Tippen Sie erneut auf die Taste, um anzuhalten. Auch Rückgängig/Wiederherstellen oder ein Tippen auf einen Eintrag beendet die Wiedergabe.

Vor dem Start können Sie in einem Popup wählen:
* `Umkehren` - Macht die Schritte vom aktuellen Zustand bis zum Anfang rückgängig, statt sie ab dem Anfang abzuspielen.
* `Kamera wiederherstellen` - Die Kamera folgt den wiedergegebenen Aktionen, auch wenn [Kamera wiederherstellen](#restore-camera) ausgeschaltet ist.
* `Kameraglättung` - Die Kamera gleitet sanft zwischen den Ansichten, statt zu jeder zu springen. Höhere Werte ergeben eine ruhigere Kamera.

::: warning
Die Wiedergabe ist experimentell.
:::

## Aktionen einschließen {#include-actions}

Mit den Symbolen unten im Verlauf-Panel wählen Sie, welche Arten von Bearbeitungen im Verlauf aufgezeichnet werden:

| Aktion      | Symbol                        | Beschreibung                                                                        |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Lichter     | ![](/icons/light.webp)        | Änderungen an Lichtern. Das Verschieben eines Lichts mit dem Gizmo wird immer aufgezeichnet, da es sich auf andere Objekte in der Szenenhierarchie auswirken kann |
| Shading     | ![](/icons/sun.webp)          | Der Modus PBR, MatCap oder Unbeleuchtet, MatCaps und HDRIs                          |
| Nachbearbeitung | ![](/icons/postprocess.webp)  | Änderungen an der Nachbearbeitung                                               |
| Auswahl     | ![](/icons/tool_lattice.webp) | Änderungen an der Gitter-Auswahl, etwa Klicks, Lasso-Auswahlen und das Aufheben der Auswahl |

## Einstellungen {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Kamera wiederherstellen {#restore-camera}
Bei jeder Aktion wird der Blickwinkel der Kamera gespeichert.
Wenn Sie diese Option aktivieren, setzt das Rückgängigmachen oder Wiederherstellen einer Aktion die Kamera auf diesen gespeicherten Blickwinkel zurück.

### ![](/icons/history.webp) Verlauf speichern {#save-history}
Behält den Verlauf beim Speichern des Projekts, sodass er auch nach dem erneuten Öffnen noch da ist. Schalten Sie die Option aus, damit Ihre Projektdateien kleiner bleiben.

### ![](/icons/ram.webp) RAM-Limit {#history-limit-mb}
Die maximale Größe des Verlaufs im Arbeitsspeicher (RAM). Ältere Zustände werden auf den Gerätespeicher ausgelagert und bei Bedarf wieder geladen, sie werden nicht gelöscht.

### ![](/icons/save.webp) Speicherplatzlimit {#storage-limit}
Der maximale Speicherplatz, den der Verlauf dieses Projekts belegen darf. Ist das Limit erreicht, werden die ältesten Aktionen endgültig gelöscht.

::: tip
Ein neues Limit greift nach der nächsten Bearbeitung, dem nächsten Rückgängigmachen oder Wiederherstellen.
:::

### ![](/icons/undo.webp) Rückgängig-Warnung {#maximum-undoable}
Wenn Sie auf einmal um mehr als diese Anzahl von Aktionen zurückspringen, fragt Nomad zuerst nach einer Bestätigung. Bearbeiten Sie danach etwas, gehen alle Aktionen nach diesem Punkt verloren. Die Warnung schützt Sie also vor einem versehentlichen Tippen weit unten in der Liste.

## Speicherstatistik {#memory-stats}

Dieser Abschnitt zeigt eine Aufschlüsselung des von Nomad belegten Speichers.
