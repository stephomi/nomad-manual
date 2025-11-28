# ![](/icons/history.webp) Verlauf {#history}
![](/images/history_overview.webp)

Wie bei den meisten Content-Erstellungstools kannst du in Nomad alle Bearbeitungsschritte rückgängig machen bzw. wiederholen.
Es gibt ein Limit dafür, wie viele Operationen rückgängig gemacht werden können, aber du kannst dieses Verhalten steuern.

::: tip
Du kannst Schnellgesten zum Rückgängig/Wiederholen verwenden:
- Mit 2 Fingern tippen, um rückgängig zu machen
- Mit 3 Fingern tippen, um zu wiederholen
:::

## Verlauf {#history-panel}
![](/images/history_history.webp)

Dieses Panel zeigt den Verlauf-Stack an, mit der Anzahl der Schritte, dem Namen der Operation und der Menge an Speicher, die dieser Schritt verwendet.

## Einstellungen {#settings}
![](/images/history_settings.webp)

### Verlaufsbegrenzung (MB) {#history-limit-mb}
Wenn der Verlauf-Stack diesen Wert überschreitet, werden ältere Operationen entfernt, sodass das Speicherkontingent in dieses Limit passt.


### Maximal rückgängig {#maximum-undoable}
Du kannst die maximale Anzahl an Operationen steuern.

## Kamera wiederherstellen {#restore-camera}
Für jede Operation wird der Kamerablickpunkt gespeichert.
Wenn du diese Option aktivierst, setzt das Rückgängig- oder Wiederholen einer Operation die Kamera auf den gespeicherten Blickpunkt zurück.

## Aktionen einschließen {#include-actions}

* `Lichter` - Wenn deaktiviert, werden Licht-Operationen (abgesehen von Gizmo-Bewegungen) vom Verlauf-Stack ignoriert
* `Matcaps & HDRIs` - Wenn deaktiviert, werden Änderungen an Matcaps und HDRIs vom Verlauf-Stack ignoriert
* `PostProcess` - Wenn deaktiviert, werden Änderungen an den Postprocess-Optionen vom Verlauf-Stack ignoriert

## Speicherauslastung {#memory-stats}

Dieser Abschnitt gibt eine Aufschlüsselung des von Nomad verwendeten Speichers.