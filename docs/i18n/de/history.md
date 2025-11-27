# ![](/icons/history.webp) Verlauf
![](/images/history_overview.webp)

Wie bei den meisten Content-Erstellungstools kannst du in Nomad alle Bearbeitungsschritte rückgängig machen bzw. wiederholen.
Es gibt ein Limit dafür, wie viele Operationen rückgängig gemacht werden können, aber du kannst dieses Verhalten steuern.

::: tip
Du kannst Schnellgesten zum Rückgängig/Wiederholen verwenden:
- Mit 2 Fingern tippen, um rückgängig zu machen
- Mit 3 Fingern tippen, um zu wiederholen
:::

## Verlauf
![](/images/history_history.webp)

Dieses Panel zeigt den Verlauf-Stack an, mit der Anzahl der Schritte, dem Namen der Operation und der Menge an Speicher, die dieser Schritt verwendet.

## Einstellungen
![](/images/history_settings.webp)

### Verlaufsgrenze (Mb)
Wenn der Verlauf-Stack diesen Wert überschreitet, werden ältere Operationen entfernt, sodass das Speicherkontingent in dieses Limit passt.


### Maximal rückgängig machbar
Du kannst die maximale Anzahl an Operationen steuern.

## Kamera wiederherstellen
Für jede Operation wird der Kamerablickpunkt gespeichert.
Wenn du diese Option aktivierst, setzt das Rückgängig- oder Wiederholen einer Operation die Kamera auf den gespeicherten Blickpunkt zurück.

## Aktionen einbeziehen

* `Lichter` - Wenn deaktiviert, werden Licht-Operationen (abgesehen von Gizmo-Bewegungen) vom Verlauf-Stack ignoriert
* `Matcaps & HDRIs` - Wenn deaktiviert, werden Änderungen an Matcaps und HDRIs vom Verlauf-Stack ignoriert
* `PostProcess` - Wenn deaktiviert, werden Änderungen an den Postprocess-Optionen vom Verlauf-Stack ignoriert

## Speicherstatistiken

Dieser Abschnitt gibt eine Aufschlüsselung des von Nomad verwendeten Speichers.
