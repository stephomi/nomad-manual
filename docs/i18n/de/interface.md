# ![](/icons/sliders.webp) Menü Oberfläche {#interface-menu}

In diesem Menü passen Sie viele Einstellungen der Oberfläche von Nomad an.

![](/images/interface_overview2.webp)

Nomad lässt sich sehr weitgehend anpassen. Das Menü ist auf 5 Tabs verteilt: Oberfläche, Shortcut, Gesten, Tastenbelegung und Debug.

![](/images/interface_menu.webp)


::: tip
Diese Seite beschreibt das Menü Oberfläche, nicht die Oberfläche selbst! Die Oberfläche als Ganzes wird unter [Erste Schritte](gettingstarted.md) erklärt.
:::

## ![](/icons/sliders.webp) Oberfläche {#interface}

Der Tab Oberfläche bestimmt Farbe, Größe und Anordnung der Benutzeroberfläche von Nomad. Er hat zwei Unter-Tabs, `Aussehen` und `Anordnung`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Farben {#presets}

![](/images/interface_presets.webp)

Der Unter-Tab `Aussehen` beginnt mit einer Sammlung von Farbvorlagen für die Oberfläche. Tippen Sie auf eine, um sie anzuwenden, und verfeinern Sie sie dann mit den Optionen darunter.

#### Akzent und Basis {#color-widgetcolor-base}
Die Hauptfarben der Oberfläche: `Akzent` für ausgewählte Schaltflächen und Reglerbalken, `Basis` für die Panels.

#### Textdeckkraft {#text-opacity}
Lässt Text und Icons vor den Panels etwas zurücktreten.

#### Umschalter, Kontrollkästchen, Tabs {#high-contrast-button}
Der Stil der Umschaltflächen (`Weich` oder `Voll`), der Kontrollkästchen (`Umriss`, `Akzent` oder `Füllung`) und der Tabs (`Unterstrichen`, `Weich` oder `Voll`).

#### Farbige Werkzeuge {#colored}
Färbt die Icons nach Kategorie ein, z. B. sind alle Maskenwerkzeuge braun, die Werkzeuge zum Teilen rot, die Werkzeuge zum Abflachen grün usw.

#### Panel-Schatten {#material-color-preview}
Die Panels werfen einen Schatten, damit sie sich von der Szene abheben.

#### Panel transparent {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Ist diese Option aktiv, erscheinen zusätzliche Einstellungen für das Aussehen der Menüs und Panels in Nomad: `Panel-Färbung` legt ihre Farbe fest, `Unschärfe` wie stark die Szene dahinter verschwommen ist, und `Glas` fügt Lichtbrechung und Glanzlichter an den Rändern hinzu, am deutlichsten bei geringer Unschärfe.

::: tip
Auf kleinen Geräten kann es sinnvoll sein, die Panel-Färbung fast weiß, transparent und mit wenig Unschärfe einzustellen, damit die Menüs die Szene nicht verdecken.
:::

#### ![](/icons/reset.webp) Aussehen zurücksetzen {#reset-style}
Setzt alle Optionen des Aussehens auf ihre Standardwerte zurück.

### ![](/icons/panel_detach.webp) Anordnung {#layout}

Der Unter-Tab `Anordnung` bestimmt, wo sich die Elemente befinden und wie groß sie sind.

#### Toolbox {#toolbox}

Optionen für das Werkzeugmenü rechts in der Oberfläche von Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Größe ändern {#ui-resize-corner}

Blendet einen Griff zum Ändern der Größe in der unteren Ecke der Toolbox ein oder aus.

##### Ausgeblendet {#hidden}
Normalerweise wechselt das Toolbox-Icon in der oberen Leiste zwischen einer langen, einspaltigen und einer mehrspaltigen Werkzeugliste. Mit dieser Option wechselt es stattdessen zwischen der mehrspaltigen Liste und einer ausgeblendeten Toolbox.

##### Reihenfolge zurücksetzen {#reset-order}
Bringt die Standardwerkzeuge der Toolbox wieder in ihre ursprüngliche Reihenfolge. Eigene Icons bleiben am Ende der Liste in der Toolbox.

#### Obere Leiste {#rows-auto-1}
`Responsive` legt fest, was die obere Leiste tut, wenn sie nicht auf den Bildschirm passt, vor allem auf kleinen Bildschirmen: `Mehrzeilig` verteilt die Menüs auf mehrere Zeilen, `Scrollen` behält eine einzige Zeile, die Sie scrollen können.

#### Oben spiegeln {#mirror-top-bar}
Kehrt die Reihenfolge der Menüs in der oberen Leiste um.

#### Seitenleisten spiegeln {#mirror-side-bars}
Vertauscht die Seitenleisten, sodass die Toolbox links und die Werkzeugoptionen rechts liegen.

#### Unten spiegeln {#mirror-bottom-bar}
Verschiebt die untere Leiste in die rechte untere Ecke und kehrt die Reihenfolge der Schaltflächen um.

#### ![](/icons/move.webp) Panel ziehen {#drag-panel}
Ein schwebendes Panel verschieben Sie immer, indem Sie an seiner Leiste ziehen. Mit dieser Option können Sie es auch an seinem Inhalt ziehen. Bei `Auto` verschiebt ein Finger oder Stift das Panel nur, wenn die Bewegung eher waagerecht als senkrecht ist, sodass ein senkrechtes Ziehen weiterhin den Inhalt scrollt. Stellen Sie `Ja` ein, um auch mit der Maus in jede Richtung zu ziehen.

#### ![](/icons/pencil.webp) Nomad-Dialog verwenden {#use-nomad-dialog}
Zeigt den eigenen Textdialog von Nomad statt des Systemdialogs an, wenn Sie einen Namen oder einen Wert eingeben.

#### ![](/icons/stylus.webp) Hover-Punkt {#hover-dot}
Zeigt einen kleinen Punkt in der Oberfläche an, wenn ein schwebender Stift erkannt wird.

#### ![](/icons/help.webp) Hilfs-Popup bei Hover {#help-popup-on-hover}

Auf Geräten, die Hover unterstützen, legt diese Option fest, ob die Kontexthilfe von Nomad (das Icon ![](/icons/help.webp)) schon beim Darüberfahren erscheint oder erst beim Antippen.

#### Gesamt-Skalierung {#overall-scale}
Ein Größenfaktor für alle Elemente der Oberfläche.
#### Panel-Breite {#panel-width}
Die Breite der Menüs und Panels.
#### Schriftgröße {#font-scale}
Skaliert die Schriften.
#### Vertikale Abstände {#vertical-spacing}
Der Abstand zwischen den Elementen in Menüs und Panels.
#### Vertikale Abstände (links) {#vertical-spacing-left}
Der Abstand zwischen den Elementen in der linken Werkzeugleiste.

#### Randabstand {#edge-offset}
Ändern Sie diese Werte nur, wenn Sie Probleme haben, die Schaltflächen am Bildschirmrand zu bedienen. Sind diese Regler deaktiviert, verwendet Nomad die sicheren Bereiche, die das Gerät selbst meldet.

::: tip
Wenn Sie Nomad auf ein neues Gerät übertragen (z. B. von einem iPhone 12 auf ein iPhone 15), setzen Sie die Randabstände unbedingt auf die Standardwerte zurück!
:::

#### ![](/icons/reset.webp) Anordnung zurücksetzen {#reset-layout}
Setzt alle Optionen der Anordnung auf ihre Standardwerte zurück.

## ![](/icons/window.webp) Shortcut {#shortcuts}

Im Tab Shortcut wählen Sie aus, welche Schnellzugriffe rund um den Viewport erscheinen, und Sie können eigene schwebende Werkzeugleisten zusammenstellen.

### Seitenleiste {#side-bar}
Die Schnellzugriffe für Werkzeuge unten in der linken Seitenleiste: `Glätten`, `Maske`, `Ausblenden`, `Face-Gruppe` und `Gizmo`. Ziehen Sie sie, um ihre Reihenfolge zu ändern.

### Untere Leiste {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Tippen Sie auf einen Shortcut, um ihn zur unteren Leiste hinzuzufügen oder daraus zu entfernen. Diese sind standardmäßig aktiv:
* `Rückgängig` - macht den letzten Vorgang rückgängig
* `Wiederholen` - stellt den zuletzt rückgängig gemachten Vorgang wieder her
* `Solo` - Blendet vorübergehend alle anderen Objekte aus, sodass nur das ausgewählte sichtbar bleibt. Tippen Sie erneut, um alle Objekte wiederherzustellen.
* `Röntgen` - Macht vorübergehend alle anderen Objekte halbtransparent, nur das ausgewählte bleibt deckend. Tippen Sie erneut, um die normalen Materialien wiederherzustellen.
* `Voxel` - Berechnet das Netz des aktuellen Objekts mit der zuletzt verwendeten Voxel-Auflösung neu. Lange drücken oder nach oben wischen zeigt einen Regler für die Auflösung und einen Schalter für scharfe Kanten.
* `Raster` - Blendet das Raster der Ansicht ein oder aus. Lange drücken oder nach oben wischen lässt Sie Farbe und Deckkraft des Rasters ändern.
* `Drahtgitter` - Blendet ein Drahtgitter über dem Modell ein oder aus. Lange drücken oder nach oben wischen lässt Sie Farbe und Deckkraft des Drahtgitters ändern.
* `Inspektion` - zeigt Eigenschaften Ihres Meshes wie die UVs, gebackene Texturen und weitere Eigenschaften über dem Hintergrund von Nomad an.
* `Face-Gruppe` - Blendet die Anzeige der Face-Gruppen ein oder aus, mehr dazu unter [Werkzeuge->Face-Gruppe](tools.md#facegroup)

Weitere häufig genutzte Shortcuts stehen ebenfalls zur Verfügung: `Umriss`, `Projektion` (perspektivisch oder orthografisch), `MatCap`, `Dyntopo` sowie die Schaltflächen `Unterteilen`, `Umkehren` und die Stufen der [Multiauflösung](topology.md#multiresolution).

#### ![](/icons/more.webp) Tastenbelegung {#bindings-list}

Fast jede Funktion von Nomad lässt sich über die Schaltfläche Tastenbelegung zur unteren Leiste hinzufügen; die Schaltfläche zeigt auch, wie viele Shortcuts die Leiste enthält. Wenn Sie darauf tippen, öffnet sich ein Menü mit den Belegungen:

![](/images/interface_bindings_search.webp)

Sie können über die Icons oben nach Kategorie suchen oder Funktionen über das Suchfeld nach Namen finden. Tippen Sie auf eine Funktion, um sie zur Leiste hinzuzufügen, und erneut, um sie zu entfernen.

#### ![](/icons/eye_open.webp) Sichtbar {#order}

Blendet die gesamte untere Leiste ein oder aus.

#### ![](/icons/reset.webp) Zurücksetzen {#reset}

Stellt die Standardeinstellungen der unteren Leiste wieder her.

### Schwebende Fenster {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Mit dem + fügen Sie eine schwebende Werkzeugleiste hinzu. Sie ist erst sichtbar, wenn Sie über die Schaltfläche Tastenbelegung einige Shortcuts hinzugefügt haben; danach können Sie sie einblenden.

Sie können beliebig viele Werkzeugleisten anlegen. Jede hat eine Zeile mit diesen Optionen:

* Ziehen Sie den Griff links an einer Zeile, um die Werkzeugleisten neu anzuordnen.
* `Name` - Der Name der Werkzeugleiste.
* `Sichtbar` - Blendet die Werkzeugleiste ein oder aus.
* `Leiste` - Zeigt eine Titelleiste an der Werkzeugleiste an.
* `Ohne Menüs` - Lässt die Werkzeugleiste auf dem Bildschirm, wenn die Oberfläche minimiert ist.
* `Tastenbelegung` - Öffnet das Fenster mit den Belegungen, um Funktionen zur Werkzeugleiste hinzuzufügen oder daraus zu entfernen.
* `Löschen` - Löscht die Werkzeugleiste.


## ![](/icons/gesture.webp) Gesten {#gesture}
Das Menü Gesten legt fest, wie Sie Nomad mit Finger, Stift, Maus und Touchpad steuern.

![](/images/interface_gesture.webp)

### Gestenoptionen {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad kann Aktionen auf bestimmte Eingabegeräte beschränken. So kann zum Beispiel das Ziehen mit dem Finger nur die Kamera bewegen, während das Ziehen mit dem Stift nur modelliert. Wenn Sie eine Maus oder ein Touchpad haben, können Sie auch diesen bestimmte Aktionen zuweisen.

Jede Zeile ist eine Aktion: Schalten Sie `Finger`, `Stylus` und `Maus` ein oder aus, um festzulegen, welche Eingaben sie ausführen dürfen.

* `Kamera` - Bewegt die Kamera.
* `Knotenbearbeitung` - Zieht die Griffe, die im Viewport angezeigt werden, zum Beispiel um eine Grundform, eine Kurve, einen Repeater oder ein Licht zu bearbeiten.
* `Bearbeiten` - Modelliert mit den Pinseln. Werkzeuge mit einer eigenen Zeile weiter unten folgen stattdessen dieser Zeile.
* `Objekt auswählen` - Tippen Sie auf ein Objekt, um es auszuwählen.
* `Materialauswahl` - Lange auf den Viewport drücken übernimmt die Farbe oder das Material unter dem Cursor. Das funktioniert nur, wenn beim aktuellen Pinsel das Malen aktiviert ist.
* `Tap` - Die Tipp-Shortcuts von Werkzeugen wie Maske, Ausblenden und Face-Gruppe (siehe unten).
* `Zeichnen` - Die Werkzeuge Zeichnen und Wischfinger.
* `Maskieren` - Das Werkzeug Maske.
* `Fläche` - Die Werkzeuge Ausblenden und Face-Gruppe.
* `Erstellen` - Die Werkzeuge Röhre, Drehbank und Einfügen.
* `Ausschneiden` - Die Werkzeuge Trimmen, Teilen und Projizieren.
* `Auswählen` - Die Werkzeuge Auswählen und Messen.
* `Gizmo` - Die Werkzeuge Gizmo und Gitter.
* `Transformieren` - Die Werkzeuge Transformieren und Anordnen.

::: tip
Auf einem Tablet ist es üblich, nur den Stift modellieren und malen zu lassen und die Finger für die Kamera zu behalten. So hinterlässt Ihr Handballen oder ein versehentlich aufgelegter Finger nie einen Strich auf Ihrem Modell.
:::

### ![](/icons/tool_smooth.webp) Finger glättet immer {#finger-always-smooths}
Ist diese Option aktiv, glättet Ihr Finger immer, solange ein Modellierwerkzeug aktiv ist, egal welcher Pinsel. Beim Einschalten wird `Finger` aus der Zeile `Bearbeiten` entfernt: Der Stift modelliert, der Finger glättet.

### Strich außerhalb zulassen {#allow-air-stroke}
Erlaubt es, einen Strich zu beginnen, auch wenn der Cursor zuerst neben dem Mesh aufsetzt. Wählen Sie die Werkzeuge aus, für die das gilt: `Werkzeug` (alle anderen Pinsel), `Glätten`, `Maske` und `Ausblenden`. Es funktioniert nur für Eingaben, die modellieren, aber nicht die Kamera bewegen können. Daher sind diese Schaltflächen deaktiviert, bis eine Ihrer Eingaben so eingestellt ist.

### ![](/icons/stroke.webp) Strich einrasten {#stroke-snap}
Halten Sie den Zeiger am Ende eines Strichs still, damit der Strich zu einer geraden Linie oder einer glatten Kurve einrastet. Ziehen Sie weiter, um den eingerasteten Strich um seinen Anfangspunkt zu drehen und zu skalieren.

`Haltedauer` legt fest, wie lange Sie stillhalten müssen, bevor der Strich einrastet oder eine Form in den Bearbeitungsmodus wechselt.

### ![](/icons/stylus.webp) Zusätzliche Eingabe-Samples verwenden {#use-extra-input-samples}
Verwendet die zusätzlichen Eingabewerte, die das Gerät meldet. Deaktivieren Sie die Option, wenn Ihre Striche zackig sind oder der Druck nicht richtig funktioniert. Unter iOS wird diese Option nicht angezeigt.

### ![](/icons/tool_mask.webp) Maske {#mask}

![](/images/interface_gesture_mask.webp)

`Shortcuts mit einem Tippen` - Aktiviert die folgenden Shortcuts mit einem einzigen Tippen, ohne dass Sie die Masken-Schaltfläche gedrückt halten müssen. Damit sind diese Gesten möglich:
* auf den Hintergrund tippen, um die Maske umzukehren
* auf einen maskierten Bereich tippen, um die Maske weichzuzeichnen
* auf einen nicht maskierten Bereich tippen, um die Maske zu schärfen

#### Lange drücken {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Lange drücken mit dem Werkzeug Maske wechselt zwischen dem Maskenpinsel und dem Lasso (SelMask):
* `Lange drücken - Bearbeiten` - Lange drücken und dann weiterziehen: Der Strich wird im anderen Modus gezeichnet, und am Ende des Strichs kehrt der vorherige Modus zurück.
* `Lange drücken - Umschalten` - Lange drücken und loslassen, ohne sich zu bewegen, um zwischen beiden zu wechseln.

### ![](/icons/tool_smooth.webp) Glätten {#smooth}
`Lange drücken - Lasso` - Lange drücken mit dem Werkzeug Glätten wechselt für die Dauer des Auswahlstrichs zum Werkzeug Auswählen.

### ![](/icons/tool_hide.webp) Ausblenden {#hide}
![](/images/interface_gesture_hide.webp)

`Shortcuts mit einem Tippen` aktiviert diese Shortcuts für das Werkzeug Ausblenden:
* Tippen Sie auf eine Face-Gruppe, um sie auszublenden
* Tippen Sie in einen leeren Bereich, um die ausgeblendeten Polygone umzukehren

### ![](/icons/finger3.webp) Drei Finger {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Wenn Ihr Gerät Gesten mit 3 Fingern unterstützt, können Sie hier Shortcuts für diese Geste festlegen.

In der Optionsmatrix können Sie waagerechtes und senkrechtes Ziehen als getrennte Shortcuts festlegen, oder `Nein` wählen, um die Geste auszuschalten. Wird dieselbe Geste für 2 Optionen gewählt, wird eine davon deaktiviert und ihr Name durchgestrichen.

* `Beleuchtung drehen` - Dreht die Umgebung, die Lichter und das MatCap.
* `Werkzeugradius` - Ändert den Radius des Werkzeugs.
* `Werkzeugintensität` - Ändert die Intensität des Werkzeugs.

### ![](/icons/fingerprint.webp) Verlauf 2/3 {#history-23}
`Verlaufsgesten` - wenn aktiv, stehen diese Gesten zur Verfügung:
* Rückgängig - mit 2 Fingern tippen
* Wiederholen - mit 3 Fingern tippen

`Lange drücken` - wenn aktiv, macht das Gedrückthalten von 2/3 Fingern schnell hintereinander rückgängig bzw. wiederholt.

### ![](/icons/mouse.webp) Mausrad {#mouse-wheel}
`Geschwindigkeit (3D Zoom)` legt fest, wie schnell das Mausrad die Ansicht zoomt, und `Geschwindigkeit (2D-Schnittstelle)`, wie schnell es durch Menüs und Panels scrollt. Die Minus-Schaltfläche neben jedem Regler kehrt die Richtung um.

### ![](/icons/fingerprint.webp) Touchpad {#trackpad}
Auf einem Mac legt `Zwei Finger` fest, was zwei Finger auf dem Touchpad tun. Auf- und Zuziehen zoomt immer, und Drehen rollt immer die Ansicht.
* `Aus` - Scrollen mit zwei Fingern zoomt, wie das Mausrad. Die Finger werden nicht einzeln erfasst.
* `Schwenken` - Zwei Finger schwenken die Ansicht, und wenn Sie einen davon anheben, kreist sie. Wie auf einem Tablet.
* `Orbit` - Zwei Finger kreisen um die Ansicht, und wenn Sie einen davon anheben, schwenkt sie.

### Barrierefreiheit {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Hilfsfenster` öffnet eine schwebende Werkzeugleiste, mit der Sie Ziehen, Auf-/Zuziehen, Rollen und Kamerabewegungen steuern.

### Kamera {#camera}
Ein Shortcut zum Menü `Kamera` (die Kameraoptionen waren früher hier, wurden aber ins Kameramenü verschoben).

### Stift: Doppel-Tap -> Tastenbelegung {#pencil-tap}

Ein Shortcut zum Menü `Tastenbelegung`, in dem Sie festlegen, was der Doppel-Tap auf den Pencil bewirkt. Außerhalb von iOS heißt er `Stift: Taste → Tastenbelegung` und betrifft die Taste am Stift.

### Handballenfilter {#palm-rejection}
Ignoriert auf Smartphones und Tablets Berührungen, deren Kontaktfläche größer als `Schwelle für maximale Größe` ist, etwa den Handballen, der auf dem Bildschirm aufliegt. Das funktioniert möglicherweise nicht auf jedem Gerät. Schalten Sie die Option also aus, wenn Sie Probleme mit Eingaben im Viewport haben.


## ![](/icons/keyboard.webp) Tastenbelegung {#bindings}
Im Menü Tastenbelegung legen Sie Tastatur- und Tasten-Shortcuts fest:

![](/images/interface_bindings.webp)
Fast alle Funktionen von Nomad lassen sich auf Tastatur-Shortcuts legen, wenn Ihr Gerät eine Tastatur hat, oder auf zusätzliche Tasten Ihres Stifts, sogar auf Gamepads.

Um eine Belegung zu erstellen, tippen Sie auf das Rechteck neben der Funktion und drücken die gewünschte Taste.

Funktionen finden Sie über die Kategorie-Icons oben oder über die Suchleiste nach Namen.

Einzelne Belegungen lassen sich über das Kontrollkästchen neben ihrem Namen deaktivieren. Drücken Sie lange auf das Kontrollkästchen und ziehen Sie, um die Liste neu anzuordnen.

Wenn zwei aktive Belegungen denselben Shortcut verwenden, erscheint neben ihnen ein Icon ![](/icons/help.webp), das die betroffenen Funktionen auflistet.

### ![](/icons/more.webp) Kontextmenü {#context-menu}
Das Icon ![](/icons/more.webp) hinter jeder Belegung öffnet ein Kontextmenü:

![](/images/interface_bindings_context.webp)

* `Klonen` - Klont die Belegung, zum Beispiel um einer Funktion einen zweiten Shortcut zu geben.
* `Zurücksetzen` - Setzt die Belegung zurück
* `Löschen` - Löscht die Belegung. Nur möglich, wenn die Funktion mehr als eine Belegung hat.

Darunter haben manche Belegungen zusätzliche Optionen:

* `Haftende Tasten` - Für Werkzeug-Shortcuts und die Schnell-Shortcuts (Maske, Glätten, Gizmo, Ausblenden, Face-Gruppe, Add/Sub) legen Sie fest, wie ein Tastendruck das Werkzeug wechselt. `Auto` übernimmt den Standard aus den Optionen unter [Erweitert](#advanced).
  * `Halten` - Halten Sie die Taste gedrückt, um das Werkzeug zu verwenden, und lassen Sie sie los, um zum vorherigen Werkzeug zurückzukehren.
  * `Umschalten` - Einmal drücken wechselt das Werkzeug.
  * `Schnelles Drücken` - Gedrückt halten, um das Werkzeug vorübergehend zu verwenden, oder kurz drücken, um zu ihm zu wechseln.
* `Nach Halten zurück` - Für Schnell-Shortcuts legen Sie fest, ob das Loslassen einer gehaltenen Taste immer zum vorherigen Werkzeug zurückkehrt, auch wenn dieses Werkzeug bereits aktiv war.
* `Vorheriges Werkzeug umschalten` - Bei Werkzeug-Shortcuts wechselt das Drücken des Shortcuts des aktuellen Werkzeugs zurück zum zuletzt verwendeten Werkzeug. Dafür muss `Haftende Tasten` auf `Umschalten` oder `Schnelles Drücken` stehen.
* `Position` - Bei Shortcuts für schwebende Fenster öffnet sich das Fenster dort, wo es zuletzt war (`Vorherige beibehalten`), oder unter dem Cursor (`Am Cursor`).
* `Verschieben (bei Loslassen)` / `Zoomen (bei Loslassen)` - Bei den Belegungen zum Zoomen und Schwenken der Kamera wechselt das Loslassen der Taste zur jeweils anderen.
* Ziehrichtung - Für `Beleuchtung drehen`, `Werkzeugradius` und `Werkzeugintensität` wählen Sie waagerechtes oder senkrechtes Ziehen.
* `Synchronisieren` - Bei Funktionen, die Objekte hinzufügen, klonen oder instanziieren, legen Sie fest, ob das Ergebnis synchronisiert wird. Standardmäßig gilt der Sync-Wert aus dem Menü Szene.
* `Auf Hintergrund` - Bei den Schnell-Shortcuts Glätten und Maske ziehen Sie bei gehaltener Taste über den Hintergrund, um ein Lasso zu zeichnen: ein Auswahl-Lasso für Glätten, ein Masken-Lasso für Maske.
* `Kamera erzwingen` - Bei den Kamera-Belegungen bewegt sich die Kamera, auch wenn derselbe Shortcut von einer anderen Belegung genutzt wird, typischerweise einem Werkzeug-Shortcut oder Add/Sub.
* `Lineares Rollen` - Bei der Belegung zum Rollen rollen Sie die Ansicht durch waagerechtes, senkrechtes oder diagonales Ziehen, statt um den Drehpunkt herum zu bewegen.

::: tip
Mit `Schnelles Drücken` erledigt eine Taste beides: Halten Sie sie für ein schnelles Glätten oder Maskieren gedrückt, und beim Loslassen sind Sie wieder bei Ihrem Pinsel. Oder tippen Sie kurz, um bei diesem Werkzeug zu bleiben.
:::

### ![](/icons/cog.webp) Erweitert {#advanced}
Unten im Menü Tastenbelegung befindet sich ein Zahnradmenü mit erweiterten Optionen:

![](/images/interface_bindings_advanced.webp)

* `Schnell-Shortcuts` - Die Standardwerte von `Haftende Tasten` und `Nach Halten zurück` für die Shortcuts Maske, Glätten, Gizmo, Ausblenden, Face-Gruppe und Add/Sub.
* `Werkzeug-Shortcuts` - Die Standardwerte von `Haftende Tasten` und `Vorheriges Werkzeug umschalten` für die Werkzeug-Shortcuts. Mit `Vorheriges Werkzeug umschalten` können Sie mit derselben Taste immer wieder zwischen zwei Werkzeugen wechseln.
* `Tastenkombinationsfenster` - Der Modus von `Haftende Tasten` für die Shortcuts, die schwebende Fenster öffnen.
* `Zoom-Y umkehren` - Kehrt die senkrechte Ziehrichtung beim Zoomen mit einer Belegung um.
* `Lineares Rollen` - Rollt die Ansicht durch waagerechtes, senkrechtes oder diagonales Ziehen, statt um den Drehpunkt herum zu bewegen.
* `SpaceMouse` - Aktiviert die Unterstützung für die SpaceMouse von 3Dconnexion. Auf manchen Systemen erscheinen weitere Optionen: was sie bewegt (`Objekt`, `Kamera`, `Erste Person`, `Drohne`), `Drehpunkt automatisch aktualisieren`, um den Drehpunkt auf die Oberfläche unter dem Cursor zu setzen, wenn die Bewegung beginnt, sowie ihre Geschwindigkeiten für `Schwenken (Pan)`, `Zoomen` und `Rotation`.
* `Totzonen (Drift)` - Für die Controller `Gamepad`, `Joystick` und `Taste`. Erhöhen Sie diese Werte, wenn sich die Kamera bewegt, obwohl Sie den Controller nicht berühren.
* `Werkzeugradius` - Wie Ziehen mit der Radius-Belegung die Pinselgröße ändert (`Kreis`, `Zentriert` oder `dx`), und dann, wie viel die Radius-Belegungen bei jedem Drücken hinzufügen (in Pixeln) oder multiplizieren.
* `Werkzeugintensität` - Wie viel die Intensitäts-Belegungen bei jedem Drücken hinzufügen oder multiplizieren.
* `Kamera - Geschwindigkeit` - Die Geschwindigkeit für `Schwenken (Pan)` und `Rotation` der Belegungen, die die Ansicht schwenken und drehen.
* `Tastenbelegung zurücksetzen` - setzt alle Belegungen auf ihre Standardwerte zurück.
* `Reihenfolge zurücksetzen` - stellt die Standardreihenfolge der Belegungsliste wieder her.


## iOS ⌘ Anzeige der Tastatur-Shortcuts {#ios-keyboard-shortcuts-display}

Auf iOS-Geräten mit Tastatur halten Sie die Taste ⌘ (cmd) gedrückt, um eine Liste der Shortcuts anzuzeigen.

Die Tastaturunterstützung unter Android ist noch etwas experimentell.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debug {#debug}
In diesem Menü finden Sie einige experimentelle Optionen und Debug-Optionen. Viele davon sollten Sie auf ihren Standardwerten lassen und nur nach Rücksprache mit dem Nomad-Support ändern. Die Icons oben springen zu den einzelnen Abschnitten.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `UVs normalisieren` - Nomad normalisiert die UVs des ausgewählten Meshes in die Kachel [0-1].

### ![](/icons/sun.webp) Shading {#render}
* `Brechungstiefe schreiben (hinten)` - Die Rückseite von Meshes mit Lichtbrechung wird in den Tiefenpuffer geschrieben.
* `Winkelgewichtete geglättete Normalen` - Eine Anpassung des Smooth Shadings, die in manchen Fällen Knicke vermeiden kann.

### ![](/icons/speed.webp) Ziel-FPS {#target-fps}
Ist diese Option deaktiviert, gleicht Nomad seine Bildrate an die Bildwiederholrate Ihres Displays an.

Ist sie aktiviert, können Sie die Bildrate festlegen, mit der Nomad rendert.

### ![](/icons/window.webp) Oberfläche {#debug-interface}
* `Werkzeugleiste: alle anzeigen` - Nomad blendet Werkzeuge aus, die für die aktuelle Auswahl nicht relevant sind, z. B. sind alle Modellierpinsel bei Grundformen ausgeblendet, die noch nicht abgeschlossen wurden. Mit dieser Option werden deaktivierte Werkzeuge abgedunkelt statt ausgeblendet.

Die anderen Optionen zur Oberfläche, die früher hier waren, befinden sich jetzt im Tab [Oberfläche](#interface).

### ![](/icons/turntable.webp) Drehscheibe {#gif-turntable}
Nomad kann eine animierte GIF-Drehscheibe exportieren. Wegen der Grenzen des GIF-Formats ist die Qualität allerdings gering. Eine Bildschirmaufnahme ist meist die bessere Methode.

* `Dauer` - wie lange die Drehscheibe in Sekunden dauert
* `Max. Frame Sampling` - Viele der hochwertigen Rendereffekte von Nomad entstehen durch das Kombinieren mehrerer Frames. Dieser Regler legt fest, wie viele Frames kombiniert werden, und sein Kontrollkästchen schaltet das ein oder aus.
* `Rotationszentrum` - worum sich die Kamera dreht: `Aktuelle beibehalten` behält den aktuellen Drehpunkt, `(0, 0, 0)` verwendet den Mittelpunkt der Welt, `Szene` den Mittelpunkt der Szene.
* `Transparenter Hintergrund` - Verwendet die Transparenzoption für GIFs. GIFs unterstützen nur 1-Bit-Transparenz, die Kanten können also stark gezackt sein.
* `Exportieren (GIF)` - startet den GIF-Export.

### ![](/icons/postprocess.webp) Nachbearbeitung {#post-process}
* `Filterung` - Debug-Option
* `Format` - Debug-Option
* `Puffer wiederverwenden` - Debug-Option

### ![](/icons/ram.webp) Leistung {#performance}
* `Multithreading: allgemein` - Debug-Option
* `Multithreading: Modellieren` - Debug-Option
* `Wiederholungen instanziert zeichnen` - Zeichnet alle Kopien eines Repeaters in einem einzigen Draw Call. Debug-Option.

### ![](/icons/star.webp) Funktion {#feature}
* `nom: Multires komprimieren` - Verkleinert Projekte und Nomad-Exporte, die Multiauflösung verwenden. Diese Dateien lassen sich mit älteren Versionen von Nomad nicht öffnen. Diese Option wird in Zukunft eventuell entfernt und standardmäßig aktiviert.
* `Quad-Diagonale umkehren (beim Tippen)` - Debug-Option

### ![](/icons/bug.webp) Debug {#dev}
* `Logs` - Öffnet ein Log-Fenster
* `Log events` - Schreibt Ihre Zeigerereignisse (Finger, Stift, Maus) in das Log-Fenster, um Probleme mit der Eingabe zu untersuchen.
* `FPS` - fügt den Statistiken im Viewport einen Bildraten-Zähler hinzu.
* `App-Bewertungsfenster` - Debug-Option, unter iOS und Android.

### ![](/icons/image.webp) Eigene Icons {#custom-icons}
Ersetzen Sie die Icons von Nomad durch eigene PNG-Dateien.
* `Symbole importieren` - Importiert PNG-Dateien nach `tmp_session/icons`. Jede ersetzt das Standard-Icon mit demselben Namen. Beim Neustart von Nomad werden sie verworfen.
* `Werkzeugsymbole exportieren` - Kopiert die Standard-Icons `tool_<tool>.png` nach `tmp_session/icons`, ohne vorhandene Dateien zu überschreiben. Dort können Sie sie bearbeiten und mit `Symbole neu laden` anwenden.
* `Symbole neu laden` - Wendet die Icons aus `tmp_session/icons` an.

### Quad-Neuvernetzung {#quad-remesh}
Die Optionen zur Quad-Neuvernetzung sind nicht mehr in diesem Menü: siehe [Quad-Neuvernetzung](topology.md#quad-remesh-instant) im Menü Topologie und das Werkzeug [Quad Remesher](tools.md#quad-remesher).

### Vorschaubilder erstellen {#make-store-thumbnails}
Rendert Screenshots in Größen, die für den iOS App Store passen.
