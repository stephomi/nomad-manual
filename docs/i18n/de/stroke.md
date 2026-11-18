# ![](/icons/brush.webp) Strich {#stroke}

---
![](/images/stroke_overview.webp) 

## Überblick {#overview}

Bei den meisten Werkzeugpinseln können Sie anpassen, wie sich der Strich verhält.
Die Einstellungen ähneln denen aus 2d-Malprogrammen, einige Optionen sind aber speziell auf das Sculpting und 3d zugeschnitten.

Die Optionen sind auf 5 Untermenüs verteilt:

| Name     | Symbol                       | Beschreibung                                                       |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Strich   | ![](/icons/brush.webp)      | Steuert, wie der Strich auf das Modell aufgetragen wird            |
| Alpha    | ![](/icons/alpha.webp)      | Wie eine Graustufentextur als Pinselabdruck verwendet wird         |
| Falloff  | ![](/icons/falloff.webp)    | Steuert, wie die Pinselstärke von der Mitte zum Rand hin abnimmt   |
| Filter   | ![](/icons/filter.webp)     | Wie der Pinsel von der Geometrie des Modells beeinflusst wird      |
| Druck    | ![](/icons/pressure.webp)   | Steuert, wie auf den Druck des Stifts reagiert wird                |

::: tip
Nicht jede Strichoption gilt für jedes Werkzeug. Optionen, die das aktuelle Werkzeug nicht nutzt, sind deaktiviert oder ausgeblendet. 
:::


## ![](/icons/brush.webp) Strich {#stroke-1}

### ![](/icons/radius.webp) Radius {#radius}

![](/images/stroke_radius.webp)

Die Radiusoptionen sind globale Einstellungen: Sie gelten für alle Werkzeuge.

#### Raum {#size}

* `Bildschirm` - der Radius wird in Bildschirmeinheiten festgelegt. Stellen Sie den Radius auf 100 Pixel ein, bleibt er 100 Pixel breit, egal ob Sie hinein- oder herauszoomen.
* `Welt (3D)` - der Radius wird in 3d-Einheiten festgelegt. Erstellen Sie zum Beispiel eine Kugel und machen den Radius genauso groß wie die Kugel, bleibt er beim Hinein- und Herauszoomen immer so groß wie die Kugel.

#### ![](/icons/link.webp) Shortcut synchronisieren {#sync-shortcut}

Ist diese Option aktiv, werden Radius und Silhouette-Einstellungen übernommen, wenn Sie zu den Shortcut-Pinseln wechseln (`Glätten`, `Maske` oder `Ausblenden`). So nutzt ein schnelles Glätten oder Maskieren dieselbe Pinselgröße wie das Werkzeug, mit dem Sie gerade gearbeitet haben.

#### ![](/icons/link.webp) Radius teilen {#share-radius}

Ist diese Option aktiv, nutzen alle Werkzeuge denselben Radius. Standardmäßig hat jedes Werkzeug seinen eigenen.


### Strichtyp {#stroke-type}

![](/images/stroke_strokemode.webp)

Striche können in mehreren Modi arbeiten:

### ![](/icons/stroke_dot.webp) Punkt {#dot}
Ziehen Sie wie bei einem normalen Malstrich. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rollen {#roll}
Das Pinselalpha dreht sich mit der Richtung des Strichs mit, praktisch für Nähte auf Stoff. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Grab • Dynamischer Radius {#lock-radius}
Setzt einen Pinselabdruck mit fester **_Höhe_**. Durch Ziehen legen Sie Größe und Drehung fest.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Grab • Dynamische Intensität {#lock-intensity}
Setzt einen Pinselabdruck mit festem **_Radius_**. Durch Ziehen legen Sie Höhe und Drehung fest.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Die Modi `Grab • Dynamischer Radius` und `Grab • Dynamische Intensität` ignorieren die [Druck](#pressure)-Einstellungen, da das Ziehen bereits Größe und Stärke bestimmt.
:::

![](/images/stroke_strokemodemove.webp)

Die Werkzeuge `Bewegen` und `Ziehen` haben ihre eigenen 3 Optionen:

### ![](/icons/snake.webp) Ziehen {#drag}

Aktualisiert während des Strichs ständig, was sich im Pinselradius befindet. Ein schneller Strich lässt die Oberfläche hinter sich, ein langsamer hält das Material fest und zieht so längere Formen heraus. Das ist der Standardmodus des Werkzeugs `Ziehen`. Zusammen mit `Dynamische Topologie` lassen sich damit schlangenartige Extrusionen formen. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Greifen {#grab}
Wählt zu Beginn des Strichs aus, was sich im Pinselradius befindet, und behält diese Auswahl bei. Das eignet sich für genauere Verschiebungen: Sie können die Strecke sorgfältig einstellen, ohne versehentlich mehr zu bewegen, als Sie anfangs erfasst haben. Das ist der Standardmodus des Werkzeugs `Bewegen`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Grab • Dynamischer Radius (Ziehen) {#lock-radius-drag}
Der eingestellte Radius wird ignoriert und stattdessen dynamisch danach bestimmt, wie weit Sie den Strich vom Startpunkt wegziehen. Kurze Strecke = kleiner Radius, längere Strecke = größerer Radius. Mit dem Stärke-Regler steuern Sie die Form des Falloffs. Praktisch, um organische, gummiartige Formen grob anzulegen.
![](/videos/stroke_lockradius_drag.mp4) 

Einige andere Werkzeuge zeigen hier ihre eigenen Strichtypen, zum Beispiel `Entspannen`, `Glätten` und `Wischfinger` bei den Glättungswerkzeugen oder Formen wie `Lasso` und `Kurve` bei den auswahlbasierten Werkzeugen. Sie werden beim jeweiligen [Werkzeug](tools.md) beschrieben.


### Intensität der Abstände anpassen {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Striche mit geringem Abstand (unter 50 %) überlagern sich schnell und wirken dadurch stärker als Striche mit größerem Abstand. Diese Option gleicht das aus, sodass Striche unabhängig vom Abstand ungefähr gleich stark sind.

### Strichabstand {#stroke-spacing}
Wie weit die einzelnen Pinselabdrücke beim Ziehen auseinanderliegen. Werte unter 100 % überlappen sich und ergeben einen durchgehenden Strich. Werte über 100 % lassen Lücken, nützlich für Details wie Nähte oder Reißverschlüsse.

### Lazy Rope Stabilisator {#lazy-rope-stabilizer}
Der Strich folgt dem Zeiger mit einem gewissen Abstand. So lassen sich saubere, glatte Linien zeichnen.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke Smoothing {#stroke-smoothing}
Mittelt mehrere Zeigerpositionen, um einen glatteren Strich zu erhalten.
Bei hohen Werten hinkt der Strich dem Zeiger hinterher, holt ihn aber schließlich ein.
Praktisch, um glatte Linien zu zeichnen.

### Einrastradius {#snap-radius}
Setzt den Strich am vorherigen fort, wenn der Zeiger nahe an dessen Ende ansetzt. Der Radius bestimmt, wie weit nach dem Ende des vorherigen Strichs gesucht wird. Nützlich, wenn Sie lange durchgehende Linien zeichnen und dabei immer wieder absetzen.

### ![](/icons/trail.webp) Spur {#trail}

Ist diese Option aktiv, trägt jeder neue Abdruck auch die letzten Punkte des Strichs dahinter erneut auf. `Spuranzahl` legt fest, wie viele Punkte erneut aufgetragen werden, `Spurintensität`, wie stark sie sind, und `Spurradius`, wie viel größer sie werden.

Die Spur funktioniert nur mit dem Strichtyp `Punkt` und nicht mit dem [Falloff-Einfluss](#influence) `Grat`.

### ![](/icons/silhouette.webp) Silhouette {#silhouette}
![](/images/stroke_silhouette.webp)
Standardmäßig wirken Striche nur auf die Oberfläche des Modells innerhalb des Pinselradius. Mit aktivierter Silhouette wird der Strich durch das gesamte Modell projiziert. Das ist sehr nützlich, um ein Modell anfangs grob anzulegen, oder für Formen, deren Seiten senkrecht bleiben sollen.

Die Projektionsrichtung lässt sich gezielt festlegen:

* `X`, `Y`, `Z` - entlang einer festen Achse projizieren.
* `Ansicht` - entlang der Blickrichtung der Kamera projizieren.
* `Wenn ausgerichtet` - entlang der Blickrichtung der Kamera projizieren, aber nur, solange die Kamera an einer Ansicht ausgerichtet ist. Andernfalls bleibt es ein normaler Strich.
* `Nächste` - entlang der Achse projizieren, die der Blickrichtung der Kamera am nächsten liegt. Das ist die Standardeinstellung.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomisieren {#randomize}

![](/images/stroke_randomize.webp)

`Stärke`, `Versatz`, `Rotation` und `Skalierung` des Strichs lassen sich jeweils zufällig variieren. Mit dem Kontrollkästchen einer Zeile schalten Sie sie ein oder aus. Damit erzielen Sie verschiedenste Effekte: Mit dem Werkzeug Zeichnen entsteht zum Beispiel eine fleckige Färbung, mit dem Werkzeug Falte feine Hautdetails.

`Periode (langsamer)` legt die Länge des Zufallszyklus fest: Erhöhen Sie sie für langsame, sanfte Schwankungen, verringern Sie sie für schnelles Rauschen. Der kleine Button neben jeder Zeile skaliert die Periode nur für diese Zeile.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Randomisieren - HSV {#randomize-hsv}

Bei Werkzeugen, die malen, lassen sich auch `Farbton`, `Sättigung` und `Wert` der Malfarbe zufällig variieren, mit einer eigenen Periode. Ideal für dezente Farbvariationen auf Haut oder Stein.

### Strichversatz {#stroke-offset}

Verschiebt den Strich um einen festen Abstand, damit Ihr Finger ihn nicht verdeckt. Das ist auf kleinen Bildschirmen nützlich. Es handelt sich um eine globale Einstellung: Aktivieren Sie sie über ihr Kontrollkästchen, dann gilt sie für alle Werkzeuge.

## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

Das `Alpha` ist eine Textur, die das Verhalten Ihres Pinsels moduliert.
Es ist ein Graustufenbild: Schwarze Pixel bedeuten keine Verformung, weiße Pixel volle Verformung.

Tippen Sie auf das Alphabild, um es zu wechseln. Neben den mitgelieferten Alphas und Ihren eigenen Importen kann die Alphaliste auch Displacement-Maps von Poly Haven herunterladen.

Tippen Sie auf die Materialvorschau, um ein Alpha aus einem Material-Preset zu laden. Hier können Sie auch Material-Presets speichern und festlegen, ob die Texturen mit dem Werkzeug eingebettet werden.

::: tip
Die Textur wird nie verkleinert, große Texturen können daher die Leistung bremsen.
:::

### ![](/icons/blend_contrast.webp) Alpha korrigieren {#invert-pixels}
Der Button `Korrigieren...` eines importierten Alphas öffnet ein Popup, das das Bild selbst korrigiert: seinen Mittelwert, das Invertieren der Pixel (Schwarz wird Weiß und Weiß wird Schwarz), eine Drehung um 90° sowie eine horizontale oder vertikale Spiegelung. Die Bilddatei wird überschrieben, sodass auch andere Apps das korrigierte Bild sehen.

::: tip

Die mit Nomad mitgelieferten Alphas lassen sich nicht korrigieren.

:::

### Projektion {#projection}

Wie das Alpha auf das Modell projiziert wird:

* `Oberfläche` - das Alpha liegt auf der Oberfläche unter dem Pinsel und folgt ihrer Ausrichtung.
* `Bildschirm` - das Alpha wird direkt aus der Ansicht projiziert.
* `Kachel` - das Alpha wird aus der Ansicht projiziert und bleibt an seinem Platz, während Sie darüber malen, wie eine Schablone. So fügt sich ein sich wiederholendes Muster nahtlos zusammen. Die Drehung ist gesperrt, und der Stiftdruck ändert die Mustergröße nicht.
* `Triplanar` - das Alpha wird entlang der 3 Achsen projiziert. Die Optionen für Skalierung, Drehung und Kacheln darunter werden durch die Einstellungen der Triplanar-Textur ersetzt.

### ![](/icons/diagonal.webp) Skalierung {#scaling}

Der Pinsel in Nomad ist ein Kreis mit einem von Ihnen festgelegten Radius. Texturen sind oft quadratisch oder rechteckig, und mit den Parametern unter `Skalierung` bestimmen Sie, wie die Textur in den Kreis passt. Bei einer quadratischen Textur passt sie mit einem Wert von 0,7 in den Kreis. Ein Wert von 1 vergrößert die Textur so weit, dass der Kreis in sie hineinpasst, und schneidet dabei die Ränder ab.

![](/images/alpha_scaling.webp) 

Mit `Skalierung Y` können Sie das Alpha vertikal strecken. Der erste Regler wird dann zu `Skalierung X`.

![](/images/alpha_scaling_y.webp) 

`Horizontal spiegeln` spiegelt das Alpha von links nach rechts.

### Rotation {#rotation}

Die Alphatextur dreht sich mit der Richtung des Strichs mit. Sie können einen Drehversatz hinzufügen. Ist das Schloss-Symbol aktiv, bleibt die Textur in dieser Drehung relativ zum Bildschirm fixiert.

Der Stift-Button daneben dreht das Alpha, wenn Sie Ihren Stift um die eigene Achse rollen (Barrel Roll), bei den Strichen `Grab • Dynamischer Radius` und `Grab • Dynamische Intensität`, solange die Drehung nicht gesperrt ist. Das funktioniert nur mit Stiften, die das unterstützen.

### Kacheln {#tiling}
![](/images/stroke_tiling.webp) 

Wie oft sich die Textur innerhalb des Pinselprofils wiederholt. Mit den Modi `Kacheln - X` und `Kacheln - Y` beschränken Sie den Strich auf eine einzelne Textur (`Kein`), wiederholen sie (`Wiederholen`) oder spiegeln jede zweite Textur, um Muster zu erzeugen oder nahtlose Texturen zu erleichtern (`Spiegeln`). Sie stehen beim Strich `Rollen`, bei der Projektion `Kachel` oder bei `Kacheln` über 1 zur Verfügung.

`Innerhalb einpassen` spielt nur bei nicht quadratischen Alphas und Pinseltexturen eine Rolle. Ist die Option aktiv, wird jedes Bild für sich ohne Abstand gekachelt. Deaktivieren Sie sie, damit das Alpha und die anderen Bilder synchron bleiben, wenn ihre Seitenverhältnisse unterschiedlich sind.

![](/videos/alpha_tiling.mp4) 



### Mittelwert {#mid-value}

Standardmäßig bedeuten schwarze Pixel keine Verformung und weiße Pixel volle positive Verformung. Ein Ton-Pinsel mit einer Felsen-Alphatextur zieht die Oberfläche also nur dort heraus, wo das Alpha nicht schwarz ist.

Soll der Pinsel die Oberfläche hineindrücken oder sowohl hineindrücken ALS AUCH herausziehen, ändern Sie den Mittelwert. Bei einem Wert von 0,5 bewirkt ein mittleres Grau im Alpha nichts, Schwarz drückt hinein und Weiß zieht heraus.

Zwei Buttons helfen Ihnen, den richtigen Wert zu finden: Der quadratische Button liest den Mittelwert am Rand des Bildes ab, und mit der Pipette wählen Sie ihn direkt auf dem Alpha aus.




## ![](/icons/falloff.webp) Falloff {#falloff}

![](/images/falloff_menu.webp) 

Das funktioniert ähnlich wie das [Alpha](#alpha), nur dass Sie die Stärke mit einer einzigen Kurve steuern. Falloff und Alpha werden kombiniert: Die Textur liefert die Details, der Falloff steuert das Ausblenden am Rand und die Stärke in der Mitte des Werkzeugs.

Liegt die Kurve oben, ist das volle Verformung, liegt sie unten, hat der Pinsel keine Wirkung.

Stellen Sie sich die Kurve als Querschnitt durch die Pinselspitze vor. Der untere Bereich zeigt eine Vorschau, wie ein einzelner „Abdruck“ des Pinsels auf der Oberfläche des Modells aussehen würde. Hat der Pinsel eine Alphatextur, wird sie ebenfalls angezeigt, damit Sie sehen, wie Falloff und Alpha zusammenwirken.

### ![](/icons/fx.webp) Preset {#preset}
Ist `Preset...` ausgewählt, öffnet ein Tippen auf das Kurvendiagramm ein Menü mit Presets. Runde Kurven ergeben weichere Ergebnisse, eckige Kurven schärfere. Der Button `Sub` in der linken Werkzeugleiste kehrt den Falloff praktisch um: Die Kurvenspitze drückt dann in die Oberfläche hinein, statt herauszuziehen, oder umgekehrt.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
In diesem Modus zeichnen Sie Ihre eigenen Falloff-Kurven. Der Kurveneditor funktioniert wie die Kurven im Rest von Nomad:

* Tippen Sie auf die Kurve, um einen neuen Punkt zu erstellen
* Ziehen Sie einen Punkt, um ihn zu verschieben
* Tippen Sie auf einen Punkt, um zwischen scharf und weich zu wechseln
* Ziehen Sie einen Punkt auf einen benachbarten Punkt, um ihn zu entfernen

### ![](/icons/curve_bspline.webp) B-Spline {#b-spline}
In diesem Modus zeichnen Sie Ihre eigenen Falloff-Kurven. Der Editor funktioniert wie bei Catmull-Rom, die Punkte beeinflussen die Kurve aber nur, statt direkt auf ihr zu liegen. So lassen sich leichter weichere Kurvenformen erstellen.

### ![](/icons/curve_bevel.webp) Fase {#bevel}
Die Punkte werden durch gerade Linien verbunden, mit abgerundeten Ecken, deren Größe von der Schärfe des jeweiligen Punkts abhängt. Praktisch für Pinsel mit flacher Spitze und einer sauberen Fase am Rand.

Der Kurveneditor hat 3 Buttons:

| Element      | Symbol                      | Beschreibung                                         |
| :----------: | :-------------------------: | :--------------------------------------------------: |
| Maximieren   | ![](/icons/maximize.webp)  | Vergrößert den Kurveneditor                          |
| Zurücksetzen | ![](/icons/reset.webp)     | Setzt die Kurve auf den Standard zurück              |
| Symmetrie    | ![](/icons/symmetric.webp) | Zeigt die Kurve als symmetrische „Pinselspitze“ an   |


### Einfluss {#influence}

* `Kugel` (3d) - Der Einfluss wird aus dem Abstand des Vertex zur Pinselmitte berechnet.
* `Kreis` (2d) - Der Vertex wird zuerst auf die Bereichsebene projiziert, bevor sein Abstand zur Pinselmitte gemessen wird. Das entspricht in etwa der Art, wie Alphas abgetastet werden. 
* `Zylinder` - Der Einfluss wird als Zylinder durch den Bereich projiziert. Das entspricht dem Aktivieren der [Silhouette](#silhouette-1) weiter unten.
* `Grat` - Der Falloff wird quer zum Strich gemessen, die Kurve wird also zum Querschnitt des gesamten Strichs. Der Button `Sym` spiegelt das Profil dann quer zum Strich: Bearbeiten Sie eine Seite, folgt die andere. Ist er aus, verläuft die Kurve von der linken zur rechten Seite des Strichs. Nicht verfügbar für die auf Abflachen basierenden Werkzeuge.

### ![](/icons/silhouette.webp) Silhouette {#silhouette-1}
Standardmäßig wirken Striche nur auf die Oberfläche des Modells innerhalb des Pinselradius. Mit aktivierter Silhouette wird der Strich durch das gesamte Modell projiziert. Das ist sehr nützlich, um ein Modell anfangs grob anzulegen, oder für Formen, deren Seiten senkrecht bleiben sollen. Es gibt dieselben Projektionsoptionen wie bei der [Silhouette](#silhouette) im Tab Strich.



## ![](/icons/filter.webp) Filter {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Strokes kumulieren {#accumulate-stroke}
Hebt die Grenze auf, wie viel Material pro Strich hinzugefügt oder entfernt werden kann. Beim Werkzeug `Ton` ist das zum Beispiel aktiv, sodass sich Material immer weiter aufbaut, beim Werkzeug `Pinsel` dagegen nicht: Fahren Sie mit demselben Strich mehrmals über denselben Bereich des Meshs, kommt kein Material mehr hinzu. 

### ![](/icons/culling.webp) Nur Front-Facing Vertex {#front-facing-vertex-only}
Diese Option ignoriert Vertices, die von Ihnen abgewandt sind.
Das ist nützlich, wenn Sie einen Teil einer dünnen Geometrie bemalen möchten, ohne die andere Seite zu treffen.
Beim Sculpten funktioniert es ebenfalls, kann dort aber Artefakte verursachen.

### ![](/icons/eye_open.webp) Nur sichtbare Vertices {#visible-vertex-only}
Ignoriert Vertices, die aus Sicht der Kamera hinter anderen Oberflächen verborgen sind. Diese Option erscheint bei den Formstrichen (Lasso, Rechteck...) der Werkzeuge zum Maskieren und Malen sowie von `Face-Gruppe` und `Ausblenden`.

### ![](/icons/dynamic.webp) Dynamische Topologie zulassen {#allow-dynamic-topology}
Diese Option ist nur verfügbar, wenn sich Ihr Mesh im Modus [Dynamische Topologie](topology.md#dynamic-topology) befindet. Sie können die dynamische Topologie für jedes Werkzeug einzeln aktivieren oder deaktivieren.

### ![](/icons/connect.webp) Connected Topology {#connected-topology}
Bearbeitet nur die Vertices, die mit der vom Werkzeug berührten Oberfläche verbunden sind. Mit dem Werkzeug `Bewegen` können Sie so zum Beispiel ein Teil verschieben, auch wenn es ein anderes Teil durchdringt.
![](/videos/connected_topology.mp4)

### Maskierten Bereich schützen {#protect-area}
![](/images/filter_protect_area.webp) 

Diese Optionen verhindern unter verschiedenen Bedingungen, dass Werkzeuge Teile Ihres Meshs verändern. Jede lässt sich auf `Auto`, `Nein` oder `Ja` stellen, und der kleine Pfeil zeigt, was `Auto` gerade bedeutet.

* `Ausblenden` - Legt fest, ob mit dem Werkzeug Ausblenden versteckte Teile des Meshs geschützt werden. Bei `Auto` sind ausgeblendete Faces geschützt, außer ihr Drahtgitter ist sichtbar (siehe die Einstellungen zum [Drahtgitter](settings.md#wireframe)).
* `Maske` - Legt fest, ob maskierte Teile des Meshs geschützt werden. Bei `Auto` sind maskierte Teile geschützt, solange die Maske im Menü [Shading](shading) sichtbar ist.
* `Face-Gruppe` - Legt fest, ob ein Werkzeug nur innerhalb der zuerst berührten Face-Gruppe wirkt. Bei `Auto` richtet sich das danach, ob Face-Gruppen im Menü [Shading](shading) sichtbar sind.

Der Button `(Alle)` legt fest, ob diese Schutzeinstellungen global für alle Werkzeuge gelten oder für jedes Werkzeug einzeln.


### Bereichssampling {#area-sampling}
Manche Pinsel oder Strichoptionen benötigen eine Ebenennormale und eine Ebenenposition auf der Oberfläche, um zu funktionieren.

Wie diese gemittelte Ebene berechnet wird, steuern Sie, indem Sie den Sampling-Bereich als Verhältnis zum Werkzeugradius festlegen.

Bei 100 % wird jeder Punkt innerhalb des Auswahlkreises berücksichtigt.

Bei 0 % wird nur der nächstgelegene Vertex bzw. das nächstgelegene Dreieck berücksichtigt. Die Werte für `Normalenradius` und `Positionsradius` lassen sich koppeln oder entsperren und getrennt einstellen.

### Normalenfilter (Bereich) {#keep-sharp-edges}
Schließt Punkte aus, deren Normalen zu stark von der Oberflächennormale abweichen.

Das verändert, wie die Ebene berechnet wird (Bereichssampling). Es ist daher vor allem für Ton- oder Abflachen-Werkzeuge nützlich, oder wenn Sie eine weitgehend flache Fläche einfärben möchten, ohne darüber hinauszumalen.

Die Winkel `Min.` und `Max.` steuern den Übergang zwischen ausgeschlossenen und voll betroffenen Punkten, wie die kleine farbige Scheibe daneben zeigt.

![](/videos/filter_keep_sharp_edges.mp4)

### Normalenfilter (Verlauf) {#falloff-normal-filter}
Wie der [Normalenfilter (Bereich)](#keep-sharp-edges) schließt er Punkte aus, deren Normalen zu stark von der Oberflächennormale abweichen, wirkt aber auf den Pinsel-Falloff statt auf die Ebenenberechnung. Nützlich, um Falten oder Erhebungen zu bemalen.


### Tiefenmaskierung {#depth-masking}
![](/images/stroke_depthmask.webp)

Schließt Punkte aus, die mehr als einen bestimmten Abstand über oder unter der berechneten Ebene (Bereichssampling) liegen.

So können Sie nur erhabene Bereiche oder nur Vertiefungen bemalen.

Das Diagramm zeigt einen Querschnitt der Oberfläche: Die waagerechte Linie ist die Oberfläche, der Kreis stellt den Falloff-Radius der Farbe über und unter der Oberfläche dar. `Höhenversatz` ist ein Prozentwert über oder unter der Oberfläche, ab dem die Maskierung berechnet wird. Mit aktiviertem `Tiefenabfall` skalieren Sie mit `Oberer Bereich` und `Unterer Bereich` den Falloff über und unter dem Versatzpunkt.

#### Beispiel: In Vertiefungen malen {#example-paint-in-cavities}
Um nur in Vertiefungen zu malen, stellen Sie den Höhenversatz auf -100 % und den Regler für den oberen Bereich so ein, dass er von der waagerechten Linie entfernt ist. Der erste Tipper legt dann die „Null“-Tiefe fest, und nur Bereiche unterhalb dieser Tiefe werden bemalt.

![](/videos/stroke_depth_cavity.mp4)

#### Beispiel: Auf Erhebungen malen {#example-paint-on-bumps}
Um nur auf hohen Bereichen zu malen, stellen Sie den Höhenversatz auf +90 %, sodass die Unterseite des Kreises die waagerechte Linie ein kleines Stück schneidet. Tippen Sie oben auf einen „hohen“ Bereich, legt das die Tiefe fest: Alles auf dieser Tiefe, etwas darunter und alles darüber wird bemalt. Tiefe Vertiefungen werden ausgelassen.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Druck {#pressure}
![](/images/pressure_menu.webp) 

Steuert, wie sich der Druck des Stifts auf die Pinsel auswirkt.

### Globale Vorgabe nutzen {#use-global-settings}

Standardmäßig ist `Globale Vorgabe nutzen` aktiv, alle Pinsel teilen sich also dieselben Druckwerte. Deaktivieren Sie die Option, um dem aktuellen Werkzeug eigene Druckeinstellungen zu geben.

### ![](/icons/radius.webp) Radius {#pressure-radius}

Diese Kurve steuert, wie sich der Druck auf den Pinselradius auswirkt. Standardmäßig ist der Zusammenhang linear: Reagiert Ihr Stift gleichmäßig, sollte sich auch der Radius gleichmäßig ändern. Viele Stifte reagieren allerdings nicht linear, was Sie mit dieser Kurve ausgleichen können. Erreicht der Radius bei hohem Druck zum Beispiel nicht ganz seinen Maximalwert, wählen Sie ein Kurven-Preset wie „out-pow3“, dessen Biegung nach oben zeigt, damit der Radius früher zunimmt.

Dieser Dialog ähnelt der Anzeige der Falloff-Kurve: Tippen Sie auf das Kurvenfenster, um ein Preset zu wählen, oder zeichnen Sie Ihre eigenen Kurven mit den Modi `Catmull-Rom`, `B-Spline` und `Fase`.

Möchten Sie einen konstanten Radius, deaktivieren Sie diesen Abschnitt.

### ![](/icons/intensity.webp) Stärke {#pressure-intensity}

Wie die Radiuskurve, nur für die Stärke. Möchten Sie eine konstante Stärke, deaktivieren Sie diesen Abschnitt.

### Druck auf 100% begrenzen {#limit-pressure}

Sorgt dafür, dass der Stiftdruck nie über 100 % geht. Das ist eine globale Einstellung.

### Druckglättung {#pressure-smoothing}

Mittelt die Druckwerte des Stifts für gleichmäßigere Ergebnisse.
