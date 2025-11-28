# ![](/icons/sun.webp) Shading {#shading}

Dieses Menü steuert die von Nomad verwendeten Schattierungsmodi, die Lichteigenschaften sowie die Eigenschaften des Umgebungslichts/Matcaps.

![](/images/shading_overview.webp)



Du kannst zwischen mehreren Render-Modi wählen:

| Mode                        | Meaning                    | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | Malen mit Metallizität/Rauigkeit                               |
| [Matcap](#matcap)           | Material Capture           | Wird beim Sculpting verwendet, mit geringerer GPU/CPU‑Last als PBR |
| [Unlit](#unlit)             | Surface Color              | Nur Oberflächenfarbe, ohne Schattierung oder Beleuchtung       |
| [Object Id](#object-id)      | Object ID                  | Eine Zufallsfarbe pro Objekt, nützlich für Mal‑Workflows       |
| [Instance Id](#instance-id)  | Instance ID                | Eine Zufallsfarbe pro Instanz, nützlich zum Erkennen geteilter Meshes |

Wenn du mehr über Metallizität und Rauigkeit erfahren möchtest, siehe den Abschnitt [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Flächengruppe {#face-group}
Überlagert Facegroup‑Farben. Facegroups sind farbige Polygon‑Auswahlen, die mit dem Werkzeug [Face group](tools#facegroup) erstellt werden können und bei den meisten Primitives automatisch erzeugt werden.

Einige Werkzeuge filtern automatisch nach Facegroups, wenn Facegroups sichtbar sind.

### Farbe anzeigen {#show-paint}
Nomad kann Farbe, Rauigkeit und Metallizität in den Vertices deiner Skulptur speichern. Mit dieser Checkbox kannst du die Anzeige dieser Eigenschaften global ein‑ oder ausschalten.

Beachte: Wenn du sowohl Vertex‑Eigenschaften als auch Texturen hast und beide aktiviert sind, werden die Werte miteinander multipliziert.

### Maske anzeigen {#show-mask}
Schaltet die Graustufen‑Maskenüberlagerung der [Maskenwerkzeuge](tools#mask) ein oder aus. Wenn dies deaktiviert ist, ist die Maske ebenfalls deaktiviert – nützlich, um schnell Änderungen ohne Maske vorzunehmen und sie danach wieder zu aktivieren, ohne die Maske zu verlieren.

### Verstecken verwenden {#use-hide}

Schaltet versteckte Flächen ein/aus. Beachte, dass dies nur funktioniert, wenn du NICHT im Hide‑Werkzeug bist!

### Texturen verwenden {#use-textures}

Nomad erlaubt es, Objekten Texturen über das [Material](material)‑Menü zuzuweisen. Wenn Texturen zugewiesen sind, können sie mit dieser Checkbox global ein‑ oder ausgeschaltet werden.







### Übersicht PBR und Lichter {#pbr}
Dieses Handbuch geht nicht ins Detail von Physically Based Rendering.

Wichtig ist: Beleuchtung und Material sind vollständig voneinander getrennt.
Das bedeutet, du kannst die Objektfarbe, Rauigkeit und Metallizität malen, während die Beleuchtung unabhängig davon gehandhabt wird.
So kannst du dein Objekt bemalen und die Beleuchtung später anpassen, ohne den Gesamteindruck deines Modells zu zerstören.

Lichter sind nur im [PBR‑Modus](#pbr) verfügbar.
Aus Performance‑Gründen bist du auf maximal 4 Lichter beschränkt.

::: tip
Du kannst eine glTF‑Datei mit mehr als 4 Lichtern laden und Nomad wird alle behalten.
Allerdings ist die Performance dann möglicherweise schlecht.
:::

::: tip
Du kannst viele Lichter faken, indem du Objekte unbeleuchtet/emissiv machst und dann Global Illumination im [Post‑Process](postprocess)‑Menü aktivierst.
:::

### Übersicht Lichttypen {#light-types-overview}

Folgende Lichttypen werden derzeit unterstützt:

| Mode                        | Description                                             | Can cast shadows                                       |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Unendlich weit entferntes Sonnenlicht                  | yes                                                    |
| [Environment](#environment) | Entferntes Licht, das an die Umgebungs‑HDR angepasst ist | yes                                                 |
| [Spot](#spot)               | Kegelförmige Lichter				                    | Yes                                                    |
| [Point](#point)             | Rundum abstrahlender Punkt                             | Yes, but only through less robust screen-space shadows |

#### Gerichtet {#directional}
Sendet Licht aus unendlicher Entfernung mit gleichmäßiger Intensität.
Seine 3D‑Position in der Szene ist egal, nur seine Ausrichtung zählt.

Du kannst dieses Licht an die Kamera anhängen, sodass die Beleuchtung konsistent bleibt.  
Zum Beispiel kannst du es als Rim Light verwenden (ein starkes Licht, das von hinten auf dein Modell scheint, in Richtung Kamera), das immer die Rückseite deines Modells beleuchtet.

#### Umgebungslicht {#env-light}
Die Verwendung einer [Umgebungs‑HDR](#environment) eignet sich gut für weiche Gesamtbeleuchtung. Wenn jedoch in der HDR eine starke, scharfe Lichtquelle sichtbar ist, wird der von ihr erzeugte Schatten sehr weich und oft kaum sichtbar sein. Die Kombination eines Directional‑Lichts mit der Umgebungs‑HDR kann helfen, ist aber schwer exakt auszurichten.

Dieses Licht übernimmt die Arbeit für dich. Es wird automatisch so rotiert, dass es sich an der hellsten Stelle der HDR ausrichtet; anschließend kannst du seine Intensität und den Winkel (Schattenweichheit) separat steuern. 

#### Spot {#spot}
Spot‑Licht strahlt in eine einzige Richtung, begrenzt durch einen Kegel.

#### Punkt {#point}
Point‑Licht strahlt in alle Richtungen.  
Momentan unterstützt Point‑Licht keine Schatten.

#### Schatten {#shadows}
Die Option `normal bias` kann verwendet werden, um typische Schattenartefakte (Acne/Peter‑Panning) zu reduzieren.

Die Schattenqualität hängt von der Größe der Objekte im Verhältnis zur gesamten Szene ab.  
Wenn du ein großes Objekt in deiner Szene hast, das keine Schatten werfen muss (z. B. eine große Ebene), deaktiviere das Schattenwerfen in seinen [Materialeinstellungen](material.md#cast-shadows).

## Lichter {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Lichter-Checkbox {#lights-checkbox}

Schaltet alle direkten Lichter in der Szene ein oder aus.



### Licht hinzufügen {#add-light}

Fügt der Szene ein Licht hinzu, bis maximal 4. Wenn ein Licht hinzugefügt wird, erscheint die Lichtliste mit Schaltflächen, und eine Licht‑Toolbar wird oben im Viewport eingeblendet.

![](/images/shading_lights_icons.webp)

* Der Text zeigt den Namen des Lichts und die Helligkeit.
* Das Augen‑Symbol schaltet die Sichtbarkeit um.
* Das Stift‑Symbol erlaubt das Umbenennen des Lichts.
* Das Papierkorb‑Symbol löscht ein Licht.
* Das Kopier‑Symbol dupliziert ein Licht. 
* Das Symbol mit den 3 Punkten öffnet einen vollständigen Licht‑Editor. Das meiste davon ist auch über die Toolbar im Viewport erreichbar. 

### ![](/icons/spotlight.webp)  Icons {#icons}

Schaltet die Anzeige der Licht‑Icons im Viewport ein/aus.

### Licht-Werkzeugleiste {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Diese Toolbar erscheint oben im Viewport, wenn ein Licht ausgewählt ist.

* Show schaltet die Sichtbarkeit des Lichts um.
* Directional/Environment/Spot/Point ändert den Lichttyp. Tippen zum Durchschalten, lang drücken für ein Menü.
* Intensity steuert die Lichtstärke; Werte können über 1,0 hinausgehen für sehr intensive Lichter, nützlich in Kombination mit Global Illumination im Post‑Process.
* Der Farbfleck öffnet bei Klick einen Farbwähler. Nomad bietet mehrere Methoden zur Farbauswahl. Die Kelvin‑Steuerung bietet eine natürliche Art, warmes/kaltes Licht zu wählen.
* Shadow schaltet Schatten ein/aus.
* Size legt die Breite eines Lichts fest. Breitere Lichter erzeugen weichere Schatten, weicheres Licht und weichere Glanzlichter auf Objekten.
* ... öffnet zusätzliche Einstellungen.

### Zusätzliche Lichtsteuerungen {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Beachte, dass einige Optionen nur für bestimmte Lichttypen verfügbar sind.

* `Clone` dupliziert das Licht.
* `Recenter` verschiebt das Licht zurück zum Ursprung.
* `Delete` löscht das Licht.
* `Directional/Environment/Spot/Point` ändern den Lichttyp.
* Der `colour swatch` öffnet bei Klick einen Farbwähler. 
* `Intensity` steuert die Lichtstärke.
* `Attachment` (_nur Directional_) legt fest, ob das Licht an die Welt oder an die Kamera angehängt ist. Wenn du z. B. ein Directional‑Licht hinter deiner Figur als Rim Light verwendest, bleibt das Licht bei „Attachment: Camera“ beim Drehen der Kamera immer hinter der Figur.
* `Angle` (_nur Directional und Environment_) ist die scheinbare Größe des Lichts, vergleichbar damit, wie groß die Sonne am Himmel wirkt. Größere Winkel erzeugen weichere Schatten und breitere Glanzlichter.
* `Softness` (_nur Spotlight_) steuert die Schärfe des Randes des Lichtkegels. 0 ist ein sehr scharfer Rand. 1 ist sehr weich, mit einem Verlauf zur Mitte des Lichtkegels. Im Viewport kann der kleine blaue Punkt am Spotlight‑Kegel verwendet werden, um Softness interaktiv einzustellen.
* `Cone angle` (_nur Spotlight_) steuert den Öffnungswinkel des Spotlights. Ein kleiner Winkel ist ein sehr dünner Lichtstrahl, 170 ist eine sehr breite Lichtstreuung. Im Viewport kann der orange Punkt verwendet werden, um den Kegelwinkel interaktiv einzustellen.
* `Shadow` schaltet Schatten für das aktuelle Licht ein/aus.
* `Shadow map` und `screenspace` sind unterschiedliche Verfahren zur Schattenberechnung; im Allgemeinen ist Shadow Map zuverlässiger.
* `Contact` beeinflusst, wie Schatten berechnet werden. Schatten sind ein schwieriges Problem in der Computergrafik und können Artefakte verursachen. Für das wichtigste Licht in einer Szene können genauere Schatten gewählt werden; diese Einstellung legt fest, ob Nomad dieses Licht automatisch auswählt oder der Benutzer.
* `Tolerance` hilft, sichtbare Schattenartefakte (z. B. wenn Schatten nicht korrekt an Oberflächen anliegen oder Rauschen/Muster in Schatten auftreten) zu beheben.

## Umgebung {#environment}

![](/images/shading_environment.webp)

Licht in der realen Welt kommt aus allen Richtungen; das Blau des Himmels, das Grün des Grases, das Rot eines Gebäudes – all dieses Licht aus der „Umgebung“ kann mit einer Environment Map simuliert werden. 

Nomad enthält mehrere Beispiel‑Environment‑Maps für Innen‑ und Außenbereiche mit unterschiedlichen Farbstichen und Helligkeiten. Probiere verschiedene Maps aus, um zu sehen, welche die meisten Details in deinen Skulpturen hervorhebt.

Tippe auf das Bild, um die verfügbaren Environment‑Maps zu sehen. Wähle in diesem Dialog „Import...“, um eigene Maps zu laden. Am besten verwendest du High Dynamic Range (HDR)‑Bilder im Latlong‑ oder Equirectangular‑Format als .hdr‑ oder .exr‑Dateien. [www.polyhaven.com](https://polyhaven.com/hdris) bietet eine gute Sammlung kostenloser Environment‑Maps; in der Regel sind 1k‑HDR‑Maps eine gute Größe mit guter Qualität.

### Belichtung {#env-exposure}
Passt die Helligkeit der Environment Map an. Oft sind die Maps zu hell, wenn sie zusammen mit regulären Lichtern verwendet werden; das Absenken der Exposure kann helfen, sie auszugleichen, besonders in Kombination mit Global Illumination in den [Post‑Process](postprocess)‑Einstellungen.

### Rotation {#env-rotation}

Da Environment‑Maps Licht aus allen Richtungen erfassen, kannst du sie rotieren, um Reflexionen und Gesamtbeleuchtung optimal mit deiner Skulptur zu kombinieren.

### An Kamera angehängt {#env-attached}
Hängt die Environment Map an die Kamera.

Dadurch wird die Beleuchtung erzwungen konsistent, was beim Sculpting hilfreich sein kann.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Wie der Name schon sagt (MATerial CAPture), übernimmt ein Matcap sowohl die Beleuchtungs‑ als auch die Materialinformation in einem einzigen Bild.
Da das Material bereits im Matcap enthalten ist, werden die Mal‑Kanäle Rauigkeit und Metallizität ignoriert.
Die Malfarbe wird mit dem Matcap multipliziert, d. h. wenn du ein schwarzes/graues Matcap hast, wird weißer Farbauftrag es nicht heller machen.

Künstler bevorzugen diesen Modus häufig zum Sculpting, da er ihnen erlaubt, sich auf Form und Geometrie zu konzentrieren.

Ein Tipp auf die Kugel öffnet einen Bildbrowser. Du kannst auch eigene Matcaps hinzufügen; im Allgemeinen kann jedes Foto, Rendering oder sogar eine gemalte Kugel, die eng quadratisch zugeschnitten ist, verwendet werden. Viele Matcap‑Bibliotheken sind online verfügbar; eine nützliche Ressource ist die [nidorx Matcap‑Bibliothek](https://github.com/nidorx/matcaps).

### Globales Matcap verwenden {#matcap-global}

Normalerweise verwenden Künstler ein einziges Matcap für die gesamte Skulptur, aber wenn dieser Schalter deaktiviert ist, kann jedes Objekt sein eigenes Matcap haben. Das kann künstlerisch für eindrucksvolle Ergebnisse genutzt werden.

::: tip
Deaktiviere diese Option und verwende ein Bild eines Augapfels für die Augen deiner Figuren!
:::

### Rotation {#matcap-rotation}
Ein Matcap ist eine spezialisierte Form einer Environment Map und kann daher ebenfalls rotiert werden. Du kannst dies jederzeit im Viewport tun, indem du mit drei Fingern nach links und rechts ziehst.



## ![](/icons/circle_fill.webp) Unbeleuchtet {#unlit}

In diesem Modus wird nur die Oberflächenfarbe angezeigt. Er ist nützlich, um zu prüfen, ob die Oberflächenfarben deiner Objekte deinen Erwartungen entsprechen, ohne von Licht, Schatten, Reflexionen oder Transparenz abgelenkt zu werden. 

Dieser Modus kann auch für nicht‑fotorealistische Renderings verwendet werden, um einen flachen, cartoonartigen Look zu erzielen.

## ![](/icons/cube.webp) Objekt-ID {#object-id}

Alle Beleuchtungs‑ und Oberflächeninformationen werden ignoriert, und jedes Objekt wird mit einer einzigartigen, flachen Farbe schattiert. Wenn dies zusammen mit einem PBR‑Render ausgegeben wird, kann es in einem Malprogramm zur Farbauswahl verwendet werden, um Farbkorrekturen an bestimmten Objekten vorzunehmen.

Beachte, dass diese Farben auch in der [Baumansicht des Szenenmenüs](scene#tree-view) erscheinen.

### ID zufällig zuweisen {#object-random}

Erzeugt einen neuen Satz zufälliger Farben. 

## ![](/icons/link.webp) Instanz-ID {#instance-id}

Wie Object ID, aber Instanzen haben dieselbe Farbe. 

### ID zufällig zuweisen {#instance-random}

Erzeugt einen neuen Satz zufälliger Farben.