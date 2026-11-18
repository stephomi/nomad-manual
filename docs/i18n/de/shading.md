# ![](/icons/sun.webp) Shading {#shading}

Dieses Menü steuert die Shading-Modi von Nomad, die Eigenschaften der Beleuchtung, die Umgebung und das MatCap sowie den Nebel.

![](/images/shading_overview.webp)



Sie können zwischen mehreren Darstellungsmodi wählen:

| Modus                       | Bedeutung                  | Beschreibung                                                    |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [PBR](#pbr)                 | Physically Based Rendering | Lichter, Schatten, Umgebung sowie gemalte Metallizität/Rauheit  |
| [MatCap](#matcap)           | Material Capture           | Schneller Modus zum Sculpten, belastet GPU/CPU weniger als PBR  |
| [Unbeleuchtet](#unlit)      | Oberflächenfarbe           | Nur die Oberflächenfarbe, ohne Shading oder Beleuchtung         |
| [Objekt-ID](#object-id)     | Objekt-ID                  | Eine zufällige Farbe pro Objekt, nützlich für Malprogramme.     |
| [Instanz-ID](#instance-id)  | Instanz-ID                 | Eine zufällige Farbe pro Instanz, um gemeinsame Meshes zu erkennen |

Mehr über Metallizität und Rauheit erfahren Sie im Abschnitt [Malen](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Face-Gruppe {#face-group}
Blendet die Farben der Face-Gruppen ein. Face-Gruppen sind farbige Auswahlen von Polygonen, die Sie mit dem Werkzeug [Face-Gruppe](tools#facegroup) erstellen und die bei den meisten Grundformen automatisch angelegt werden.

Manche Werkzeuge filtern automatisch nach Face-Gruppen, wenn diese sichtbar sind.

### ![](/icons/palette.webp) Painting anzeigen {#show-paint}
Nomad kann Farbe, Rauheit und Metallizität in den Vertices Ihres Modells speichern. Mit diesem Kontrollkästchen schalten Sie die Anzeige dieser Eigenschaften global ein oder aus.

Haben Sie sowohl Vertex-Eigenschaften als auch Texturen und ist beides aktiv, werden die Werte miteinander multipliziert.

### ![](/icons/shield.webp) Maske anzeigen {#show-mask}
Schaltet die graue Maskenüberlagerung der [Maskenwerkzeuge](tools#mask) ein oder aus. Ist sie deaktiviert, ist auch die Maske selbst deaktiviert. Praktisch für schnelle Änderungen ohne Maske: Danach aktivieren Sie sie wieder, ohne Ihre Maske zu verlieren.

### ![](/icons/tool_hide.webp) Ausblenden verwenden {#use-hide}

Schaltet ausgeblendete Faces ein oder aus. Das funktioniert nur, wenn Sie sich NICHT im Werkzeug Ausblenden befinden!

### ![](/icons/image.webp) Texturen verwenden {#use-textures}

In Nomad lassen sich Objekten im Menü [Material](material) Texturen zuweisen. Sind Texturen zugewiesen, können Sie sie mit diesem Kontrollkästchen global ein- oder ausschalten.

In Nomad können Sie keine Texturen erstellen oder bearbeiten, Texturen aus importierten Dateien funktionieren aber. Deckkraft-Texturen wirken in PBR, MatCap und Unbeleuchtet, Normal Maps in PBR und MatCap, Farbe in PBR und Unbeleuchtet, Leuchten, Rauheit und Metallizität nur in PBR. Hat die Szene keine Textur, ist der Button ausgegraut.

### Überblick über PBR und Lichter {#pbr}
Dieses Handbuch geht nicht im Detail auf Physically Based Rendering ein.

Wichtig ist vor allem: Beleuchtung und Material sind vollständig voneinander getrennt.
Sie können also Farbe, Rauheit und Metallizität Ihres Objekts malen, während die Beleuchtung unabhängig davon gesteuert wird.
So bemalen Sie Ihr Objekt und passen die Beleuchtung später an, ohne den Gesamteindruck Ihres Modells zu zerstören.

Lichter, die Umgebung und der Nebel sind nur im [PBR-Modus](#pbr) verfügbar.
Aus Leistungsgründen sind Sie auf Mobilgeräten auf 4 Lichter und auf dem Desktop auf 6 beschränkt.

::: tip
Sie können eine glTF-Datei mit mehr Lichtern laden, Nomad behält dann alle.
Die Leistung kann darunter aber leiden.
:::

::: tip
Viele Lichter lassen sich vortäuschen, indem Sie Objekte unbeleuchtet oder leuchtend machen und dann im Menü [Nachbearbeitung](postprocess) die globale Illumination aktivieren.
:::

### Überblick über die Lichttypen {#light-types-overview}

Diese Lichttypen werden derzeit unterstützt:

| Modus                       | Beschreibung                                            | Kann Schatten werfen |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Gerichtet](#directional)   | Unendlich weit entferntes Sonnenlicht                   | Ja               |
| [Umgebung](#env-light)      | Ein entferntes Licht, das an das Umgebungs-HDR angepasst wird | Ja         |
| [Spot](#spot)               | Kegelförmige Lichter                                    | Ja               |
| [Punkt](#point)             | Punktlicht, das in alle Richtungen strahlt              | Ja               |

#### ![](/icons/sun.webp) Gerichtet {#directional}
Strahlt Licht aus unendlicher Entfernung mit gleichmäßiger Stärke aus.
Seine 3d-Position in der Szene spielt keine Rolle, nur seine Ausrichtung.

Sie können dieses Licht an die Kamera binden, so bleibt die Beleuchtung immer gleich.  
Damit lässt sich zum Beispiel ein Kantenlicht (ein starkes Licht, das von hinten auf Ihr Modell in Richtung Kamera strahlt) erzeugen, das die Rückseite Ihres Modells immer beleuchtet.

#### ![](/icons/panorama.webp) Umgebungslicht {#env-light}
Eine [Umgebungs-HDR](#environment) eignet sich gut für eine weiche Gesamtbeleuchtung. Ist im HDR aber ein starkes, scharfes Licht zu sehen, wird der Schatten, den es erzeugt, sehr weich und ist oft gar nicht sichtbar. Ein gerichtetes Licht zusätzlich zum Umgebungs-HDR kann helfen, es ist aber oft schwierig, beide aufeinander auszurichten.

Dieses Licht übernimmt das für Sie. Es wird automatisch auf den hellsten Teil des HDR ausgerichtet, und Sie steuern seine Stärke und seinen Winkel (die Weichheit der Schatten) getrennt. 

#### ![](/icons/spotlight.webp) Spot {#spot}
Ein Spotlicht strahlt in eine einzige Richtung, begrenzt durch einen Kegel.

#### ![](/icons/light.webp) Punkt {#point}
Ein Punktlicht strahlt in alle Richtungen und kann ebenfalls Schatten werfen.

#### Schatten {#shadows}
Jedes Licht kann Schatten werfen, und in seinen [Einstellungen](#light-extra-controls) wählen Sie, wie sie berechnet werden. Sehen Sie Schattenartefakte, können die Regler `Toleranz` dort helfen.

Die Qualität der Schatten hängt davon ab, wie groß die Objekte im Verhältnis zur gesamten Szene sind.  
Haben Sie ein großes Objekt in der Szene, das keine Schatten werfen muss (zum Beispiel eine große Ebene), deaktivieren Sie den Schattenwurf in seinen [Materialeinstellungen](material.md#casts-shadows).

## ![](/icons/sun.webp) Lichter {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Kontrollkästchen Lichter {#lights-checkbox}

Schaltet alle direkten Lichter der Szene ein oder aus.



### Licht hinzufügen {#add-light}

Fügt der Szene ein Licht hinzu, bis zu 4 Lichter auf Mobilgeräten und 6 auf dem Desktop. Sobald ein Licht hinzugefügt ist, erscheint die Lichterliste mit Buttons, und oben im Viewport wird eine Lichtleiste eingeblendet.

![](/images/shading_lights_icons.webp)

* Der Text zeigt den Namen des Lichts und seine Helligkeit. Tippen Sie darauf, um das Licht auszuwählen.
* Das Augensymbol schaltet die Sichtbarkeit um.
* Mit dem Stiftsymbol benennen Sie das Licht um.
* Das Papierkorbsymbol löscht ein Licht.
* Das Kopiersymbol dupliziert ein Licht. 
* Das Symbol mit den 3 Punkten öffnet einen vollständigen Lichteditor. Die meisten dieser Funktionen sind auch über die Leiste im Viewport erreichbar. 

Sie können ein Licht in der Liste auch ziehen, um die Reihenfolge zu ändern.

### ![](/icons/spotlight.webp)  Symbole {#icons}

Schaltet die Anzeige der Lichtsymbole im Viewport ein oder aus

### Lichtleiste {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Diese Leiste erscheint oben im Viewport, wenn ein Licht ausgewählt ist.

* `Sichtbar` schaltet die Sichtbarkeit des Lichts um.
* Gerichtet/Umgebung/Spot/Punkt ändert den Lichttyp. Tippen Sie, um durchzuschalten, oder halten Sie gedrückt, um ein Menü zu sehen.
* Stärke steuert, wie hell das Licht ist. Der Wert kann für sehr intensive Lichter über 1,0 gehen, nützlich zusammen mit der globalen Illumination in der Nachbearbeitung.
* Ein Tippen auf das Farbfeld öffnet eine Farbauswahl. Nomad bietet mehrere Möglichkeiten, eine Farbe zu wählen. Mit der Kelvin-Steuerung wählen Sie ganz natürlich warmes oder kühles Licht.
* Schatten schaltet die Schatten um.
* Winkel (_gerichtet und Umgebung_) bzw. Größe (_Spot und Punkt_) legt die Breite eines Lichts fest. Breitere Lichter werfen weiche Schatten, beleuchten weicher und erzeugen sanftere Glanzlichter auf Objekten.
* Anordnung (_nur gerichtet_), Kegelwinkel und Sanftheit (_nur Spot_) werden unten beim [Lichteditor](#light-extra-controls) beschrieben.
* ... öffnet `Klonen`, `Zentrieren` und `Löschen` sowie die Schatteneinstellungen.

### Erweiterte Lichteinstellungen {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Das Symbol mit den 3 Punkten bei einem Licht in der Liste öffnet seinen vollständigen Editor. Manche Optionen gibt es nur bei bestimmten Lichttypen.

* `Gerichtet/Umgebung/Spot/Punkt` ändert den Lichttyp.
* Ein Tippen auf das `Farbfeld` öffnet eine Farbauswahl. 
* `Stärke` steuert, wie hell das Licht ist.
* `Anordnung` (_nur gerichtet_) bindet das Licht an die Welt (`Fixiert`) oder an die Kamera (`Kamera`). Nutzen Sie zum Beispiel ein gerichtetes Licht hinter Ihrer Figur als Kantenlicht, bleibt es mit der Anordnung an der Kamera beim Drehen der Kamera immer hinter der Figur.
* `Sanftheit` (_nur Spotlicht_) steuert die Schärfe des Rands des Lichtkegels. 0 ist ein sehr scharfer Rand, 1 ist sehr weich, mit einem Verlauf zur Mitte des Lichtkegels. Im Viewport können Sie die Sanftheit mit dem kleinen blauen Punkt am Lichtkegel direkt einstellen.
* `Kegelwinkel` (_nur Spotlicht_) steuert den Öffnungswinkel des Spotlichts. Ein kleiner Winkel ergibt einen sehr schmalen Lichtstrahl, 170 einen sehr breiten Lichtkegel. Im Viewport können Sie den Kegelwinkel mit dem orangen Punkt direkt einstellen.
* `Winkel` (_nur gerichtet und Umgebung_) ist die scheinbare Größe des Lichts, stellen Sie es sich so vor, wie groß die Sonne am Himmel erscheint. Größere Winkel werfen weichere Schatten und breitere Glanzlichter.
* `Größe` (_nur Spot und Punkt_) ist die Breite des Lichts. Größere Lichter werfen weichere Schatten.
* `Schatten` schaltet die Schatten des aktuellen Lichts um.
* Der Schattentyp legt fest, wie Schatten berechnet werden. Eine `Schattenkarte` rendert die Szene aus Sicht des Lichts und erzeugt so auch Schatten von Geometrie, die die Kamera nicht sieht. `Bildschirmbereich` nutzt nur, was bereits auf dem Bildschirm zu sehen ist: Das ist sparsamer, aber experimentell. Im Allgemeinen ist die Schattenkarte zuverlässiger.
* `Toleranz` (_nur Bildschirmbereich_): Sind Schattenartefakte zu sehen (Schatten scheinen die Oberflächen nicht zu berühren, oder es gibt Rauschen und Muster in den Schatten), kann eine Anpassung der Toleranz helfen.
* `Kontakt` fügt präzisere Schatten auf kurze Distanzen hinzu, dort wo sich Objekte berühren. Mit `Auto` erhält nur das dominanteste Licht der Szene Kontaktschatten, `Nein` und `Ja` schalten sie für dieses Licht fest aus oder ein. Sein Regler `Toleranz` funktioniert wie der oben.

Der Button `...` der Viewport-Leiste enthält dieselben Schatteneinstellungen und zusätzlich:

* `Klonen` dupliziert das Licht.
* `Zentrieren` setzt das Licht vor die Kamera und behält seine Ausrichtung bei.
* `Löschen` löscht das Licht.


## ![](/icons/panorama.webp) Umgebung {#environment}

![](/images/shading_environment.webp)

In der realen Welt kommt Licht aus allen Richtungen: das Blau des Himmels, das Grün des Rasens, das Rot eines Gebäudes. All dieses Licht aus der „Umgebung“ lässt sich mit einer Umgebungs-Map simulieren. 

Mit dem Kontrollkästchen neben dem Titel schalten Sie die Umgebungsbeleuchtung ein oder aus.

Nomad bringt mehrere Beispiel-Umgebungs-Maps für Innen- und Außenbereiche mit, in unterschiedlichen Farbtönen und Helligkeiten. Probieren Sie verschiedene aus, um zu sehen, welche die meisten Details Ihres Modells hervorhebt.

Tippen Sie auf das Bild, um die verfügbaren Umgebungs-Maps zu sehen. In diesem Dialog laden Sie mit `Import` Ihre eigenen. Am besten eignen sich High-Dynamic-Range-Bilder (HDR) im Latlong- bzw. equirektangularen Format, als .hdr- oder .exr-Datei. Der Browser kann Umgebungen auch direkt von [Poly Haven](https://polyhaven.com/hdris) herunterladen, das eine gute Sammlung kostenloser Umgebungs-Maps bietet.

### Belichtung {#env-exposure}
Passt die Helligkeit der Umgebungs-Map an. Zusammen mit normalen Lichtern sind die Maps oft zu hell. Eine niedrigere Belichtung hilft dann beim Ausbalancieren, besonders zusammen mit der globalen Illumination in den Einstellungen der [Nachbearbeitung](postprocess).

### Rotation {#env-rotation}

Da Umgebungs-Maps Licht aus allen Richtungen erfassen, können Sie sie drehen, damit Spiegelungen und Gesamtbeleuchtung gut zu Ihrem Modell passen. Sie können die Umgebung auch drehen, indem Sie mit 3 Fingern waagerecht über den Viewport ziehen.

### Mit der Kamera verbunden {#env-attached}
Bindet die Umgebung an die Kamera.

Dadurch bleibt die Beleuchtung immer gleich, was beim Sculpten nützlich sein kann.

### Unschärfe (Hintergrund) {#env-background-blur}
Dieser Regler erscheint nur, wenn der [Hintergrund](background.md) auf die Umgebung eingestellt ist. Er zeichnet das Umgebungsbild hinter Ihrem Modell weich, ohne die Beleuchtung zu verändern.


## ![](/icons/fog.webp) Nebel {#fog}

Nebel verleiht Ihrer Szene atmosphärische Tiefe und macht Lichtstrahlen sichtbar. Aktivieren Sie ihn mit dem Kontrollkästchen neben dem Titel. Wie Lichter und Umgebung ist er nur im Modus [PBR](#pbr) verfügbar.

::: tip Stärkere Lichtstrahlen
Senken Sie die `Umgebung` des Nebels und verwenden Sie ein helles Spot- oder Punktlicht. Erhöhen Sie die `Dichte`, bis der Nebel deutlich sichtbar ist. Für sichtbare Strahlen in dünnerem Nebel stellen Sie die `Streurichtung` auf einen hohen positiven Wert und richten die Kamera auf das Licht.
:::

### Farbe {#fog-color}
Die Farbe des Nebels und des Lichts, das er streut.

### Dichte {#fog-density}
Wie schnell der Nebel mit der Entfernung dichter wird.

### Maximale Deckkraft {#fog-opacity}
Begrenzt, wie stark der Nebel die Szene verdecken kann, auch bei hoher Dichte.

### Streurichtung {#fog-scattering}
Die Richtung, in die der Nebel das Licht streut (auch Anisotropie genannt). Positive Werte hellen den Nebel auf, wenn Sie in Richtung eines Lichts blicken, negative Werte, wenn Sie wegblicken, und null streut das Licht gleichmäßig in alle Richtungen.

### ![](/icons/panorama.webp) Umgebung {#fog-environment}
Wie stark die [Umgebung](#environment) den Nebel beleuchtet. Ist die Umgebung ausgeschaltet, ist die Option ausgegraut.

### Rauschen {#fog-noise}
Mischt Rauschen in den Nebel, um ihn in Schwaden aufzuteilen, ohne seine Gesamtdichte zu ändern. Ist das Rauschen über 0, legt ein Regler `Größe` die Größe des Musters fest.

### Form {#fog-shape}
Wo der Nebel die Szene füllt:

* `Gleichmäßig` - füllt die ganze Szene.
* `Vertikal` - hält den Nebel in einem senkrechten Band mit weichen Rändern. Die Regler `Unten` und `Oben` legen die Höhe der unteren und oberen Kante fest, und ihr Augen-Button zeigt das Band im Viewport an, während Sie sie einstellen.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Wie der Name schon sagt (MATerial CAPture), vereint ein MatCap Beleuchtung und Materialinformationen in einem einzigen Bild.
Da das Material bereits im MatCap steckt, werden die gemalten Kanäle für Rauheit und Metallizität ignoriert.
Die gemalte Farbe wird mit dem MatCap multipliziert: Bei einem schwarzen oder grauen MatCap wird es mit weißer Farbe also nicht heller.

Viele Künstler bevorzugen diesen Modus zum Sculpten, weil sie sich damit ganz auf Form und Geometrie konzentrieren können.

Ein Tippen auf die Kugel öffnet einen Bildbrowser. Sie können auch eigene MatCaps hinzufügen: Im Grunde eignet sich jedes Foto, jedes Rendering, sogar ein Gemälde einer Kugel, das eng auf ein Quadrat zugeschnitten ist. Online gibt es viele MatCap-Bibliotheken, eine nützliche Quelle ist die [MatCap-Bibliothek von nidorx](https://github.com/nidorx/matcaps).

### Globales MatCap verwenden {#matcap-global}

Meist verwenden Künstler ein einziges MatCap für das gesamte Modell. Ist diese Option aber deaktiviert, kann das ausgewählte Objekt sein eigenes MatCap haben. Das lässt sich künstlerisch für eindrucksvolle Ergebnisse nutzen.

::: tip
Deaktivieren Sie diese Option und verwenden Sie das Bild eines Augapfels für die Augen Ihrer Figuren!
:::

### Rotation {#matcap-rotation}
Ein MatCap ist eine spezielle Form der Umgebungs-Map und lässt sich daher ebenso drehen. Das geht auch jederzeit im Viewport, indem Sie mit 3 Fingern nach links und rechts ziehen.

Der Schloss-Button neben dem Regler sperrt die Drehung, damit ein Ziehen mit 3 Fingern das MatCap nicht versehentlich dreht.



## ![](/icons/circle_fill.webp) Unbeleuchtet {#unlit}

Dieser Modus zeigt nur die Oberflächenfarbe. So prüfen Sie, ob die Oberflächenfarben Ihrer Objekte stimmen, ohne von Lichtern, Schatten, Spiegelungen oder Transparenz abgelenkt zu werden. 

Der Modus eignet sich auch für nicht fotorealistische Renderings mit flachem, Cartoon-artigem Look.

## ![](/icons/cube.webp) Objekt-ID {#object-id}

Alle Beleuchtungs- und Oberflächeninformationen werden ignoriert, und jedes Objekt erhält eine eigene, flache Farbe. Rendern Sie das zusätzlich zu einem PBR-Rendering, können Sie in einem Malprogramm nach Farbe auswählen und so gezielt einzelne Objekte farblich korrigieren.

Diese Farben erscheinen auch in der [Baumansicht des Menüs Szene](scene#tree-view).

### ID randomisieren {#object-random}

Erzeugt einen neuen Satz zufälliger Farben. 

## ![](/icons/link.webp) Instanz-ID {#instance-id}

Wie Objekt-ID, nur haben Instanzen dieselbe Farbe. 

### ID randomisieren {#instance-random}

Erzeugt einen neuen Satz zufälliger Farben.
