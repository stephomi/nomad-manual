# ![](/icons/pencil.webp) Strich    

---
![](/images/stroke_overview.webp) 

## Übersicht 

Du kannst das Strichverhalten der meisten Werkzeugpinsel anpassen.
Die Einstellungen ähneln denen in 2D-Malprogrammen, einige Optionen sind jedoch speziell für Sculpting und 3D.

Die Optionen sind auf 5 Untermenüs aufgeteilt:

| Name     | Icon                         | Beschreibung                                                      |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Steuert, wie der Strich auf das Modell angewendet wird            |
| Alpha    | ![](/icons/alpha.webp)      | Wie eine Graustufen-Textur für den Pinselabdruck verwendet wird   |
| Falloff  | ![](/icons/falloff.webp)    | Steuert, wie sich die Pinselstärke vom Zentrum zum Rand ändert    |
| Filter   | ![](/icons/filter.webp)     | Wie der Pinsel von der Modellgeometrie beeinflusst wird           |
| Pressure | ![](/icons/pressure.webp)   | Steuert die Reaktion auf Stiftdruck                               |

::: tip
Nicht alle Strichoptionen gelten für alle Werkzeuge. Strichoptionen, die vom aktuellen Werkzeug nicht verwendet werden, werden deaktiviert oder ausgeblendet. 
:::


## Stroke

### Radius

![](/images/stroke_radius.webp)

#### Radius teilen

Wenn aktiviert, verwenden alle Werkzeuge denselben Radius; standardmäßig hat jedes Werkzeug seinen eigenen Radius.

#### Größe

* Screen – der Radius wird in Bildschirmeinheiten festgelegt. Wenn du den Radius auf 100 Pixel Breite einstellst, bleibt er 100 Pixel breit, unabhängig davon, ob du hinein- oder herauszoomst.
* Constant (3d) – der Radius wird in 3D-Einheiten festgelegt. Wenn du zum Beispiel eine Kugel erstellst und den Radius auf die gleiche Größe wie die Kugel setzt, bleibt der Radius gleich groß wie die Kugel, während du hinein- und herauszoomst.


### Stroke

![](/images/stroke_strokemode.webp)

Striche können in mehreren Modi arbeiten:

### ![](/icons/stroke_dot.webp) Dot
Ziehen wie ein normaler Malstrich. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
Das Pinsel-Alpha wird so rotiert, dass es der Richtung des Strichs folgt – nützlich für Stoffnähte. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
Einen Pinselstrich mit fester **_Höhe_** stempeln. Ziehen legt Skalierung und Rotation fest.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Einen Pinselstrich mit festem **_Radius_** stempeln. Ziehen legt Höhe und Rotation fest.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Die Werkzeuge `Move` und `Drag` haben ihre eigenen 3 Optionen:

### ![](/icons/snake.webp) Drag

Aktualisiert während des Strichs fortlaufend, was sich innerhalb des Pinselradius befindet. Ein schneller Strich lässt die Oberfläche zurück, während ein langsamer Strich Material „festhält“ und längere Formen erzeugt. Dies ist der Standardmodus für das Werkzeug `Drag`. Mit `Dynamic Topology` kann dies verwendet werden, um schlangenartige Extrusionen zu erzeugen. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Wählt beim Start des Pinsels, was sich innerhalb des Pinselradius befindet, und behält diese Auswahl bei. Das ist nützlich für präzisere Verschiebevorgänge, da du den Verschiebeabstand sorgfältig anpassen kannst, ohne versehentlich mehr zu bewegen als ursprünglich ausgewählt. Dies ist der Standardmodus für das Werkzeug `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
Der Benutzer-Radius wird ignoriert und dynamisch basierend darauf gesetzt, wie weit der Strich vom Startpunkt weggezogen wird. Kleine Distanz = kleiner Radius, größere Distanz = größerer Radius. Verwende den Intensitätsregler, um die Form des Falloffs zu steuern. Nützlich zum Blocken organischer, gummiartiger Formen.
![](/videos/stroke_lockradius_drag.mp4) 



### Abstand-Intensität anpassen
![](/images/stroke_space_smooth.webp)

Striche mit geringem Abstand (unter 50 %) können sich schnell aufbauen und intensivere Striche erzeugen als höhere Abstands­werte. Diese Umschaltoption kompensiert das, sodass Striche ungefähr die gleiche Intensität haben, unabhängig vom Abstand.

### Strichabstand
Legt fest, wie weit auseinander jeder Pinselabdruck während eines Ziehvorgangs angewendet wird. Werte unter 100 % überlappen sich und erzeugen den Eindruck eines kontinuierlichen Strichs. Werte über 100 % beginnen Lücken zu lassen – nützlich für Details wie Nähte oder Reißverschlüsse.

### Lazy-Rope-Stabilisator
Striche hinken der Zeigerposition um eine bestimmte Distanz hinterher. Dies kann verwendet werden, um glatte Linien zu zeichnen.
![](/videos/stroke_lazy_rope.mp4) 

### Strichglättung
Mittelt mehrere Zeigerpositionen, um einen glatteren Strich zu erhalten.
Bei hohen Werten hinkt der Strich dem Zeiger hinterher, holt aber schließlich auf.
Dies ist nützlich, um glatte Linien zu zeichnen.

### Snap-Radius
Den Beginn des Strichs an das Ende des vorherigen Strichs schnappen. Der Radius bestimmt, wie weit nach dem Ende des vorherigen Strichs gesucht wird. Dies kann nützlich sein, wenn du lange, durchgehende Linien mit häufigen Pausen zeichnest.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Standardmäßig beeinflussen Striche nur die Modelloberfläche innerhalb des Pinselradius. Wenn Silhouette aktiviert ist, wird der Strich durch das gesamte Modell projiziert. Das ist sehr nützlich beim ersten Blocken eines Modells oder für Formen, bei denen die Seiten senkrecht bleiben sollen.

Die Projektionsrichtung kann explizit gesetzt werden; die Standardmethode „Closest“ erkennt den besten Winkel relativ zur Ansicht. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

Intensität, Translation, Rotation und Skalierung des Strichs können jeweils zufällig variiert werden. Damit lassen sich verschiedene Effekte erzeugen, z. B. kann Randomize mit dem Paint-Werkzeug gesprenkelte Farben erzeugen oder mit dem Crease-Werkzeug Hautdetails.

![](/videos/stroke_randomize.mp4) 

### Strichversatz

Einen konstanten Versatz auf den Strich anwenden. Das ist nützlich bei kleinen Bildschirmen, auf denen dein Finger den Strich verdecken würde. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

Das `Alpha` ist eine Textur, die das Pinselverhalten moduliert.
Es ist ein Graustufenbild, bei dem schwarze Pixel keine Deformation und weiße Pixel volle Deformation bedeuten.

Klicke auf das Alpha-Bild, um es zu ändern.

Klicke auf die Materialvorschau, um ein Alpha aus einem Material-Preset zu laden. Du kannst hier auch Material-Presets speichern und wählen, ob Texturen mit dem Werkzeug eingebettet werden sollen.

::: tip
Die Textur wird nie in der Größe geändert, daher können große Texturen die Performance verlangsamen.
:::

### Pixel invertieren
Dies kehrt die Werte des Bildes um, sodass schwarze Pixel weiß und weiße Pixel schwarz werden.

::: tip

Die integrierten Alphas, die mit Nomad ausgeliefert werden, können nicht invertiert werden.

:::

### Skalierung

Die Pinselgröße in Nomad ist ein Kreis mit einem benutzerdefinierten Radius. Texturen sind oft quadratisch oder rechteckig; die Parameter `Scaling` legen fest, wie die Textur in den Kreis eingepasst wird. Für eine quadratische Textur passt ein Wert von 0,7 in den Kreis. Ein Wert von 1 skaliert die Textur größer, sodass der Kreis hineinpasst und die Ränder abgeschnitten werden.

![](/images/alpha_scaling.webp) 

Wenn `Scaling - Y` aktiviert ist, kannst du das Alpha vertikal strecken.

![](/images/alpha_scaling_y.webp) 

### Rotation

Die Alpha-Textur wird so rotiert, dass sie der Richtung des Strichs folgt. Du kannst einen Rotationsoffset hinzufügen, und wenn das Schloss-Symbol aktiviert ist, bleibt die Textur relativ zum Bildschirm in dieser Rotation gesperrt.

### Tiling
![](/images/stroke_tiling.webp) 

Legt fest, wie oft die Textur innerhalb des Pinselprofils wiederholt wird. Die Tiling-Modi erlauben es, auf einen einzelnen Texturabdruck pro Strich zu begrenzen, wiederholte Texturen zu verwenden oder gespiegelt zu kacheln, wobei jede zweite Textur gespiegelt wird, um Muster zu erzeugen oder nahtlose Texturen zu erleichtern.

![](/videos/alpha_tiling.mp4) 



### Mittelwert

Standardmäßig bedeuten schwarze Pixel keine Deformation und weiße Pixel volle positive Deformation. Eine Clay-Bürste mit einer Alpha-Textur aus Felsen zieht die Oberfläche also nur dort heraus, wo das Alpha nicht schwarz ist.

Wenn du möchtest, dass der Pinsel die Oberfläche hineindrückt oder sowohl hinein- als auch herausdrückt, kannst du den Mittelwert anpassen. Wenn du den Wert z. B. auf 0,5 setzt, bewirkt ein mittleres Grau im Alpha nichts, Schwarz drückt hinein, Weiß zieht heraus.




## Falloff

![](/images/falloff_menu.webp) 

Dies ähnelt dem [Alpha](#alpha), außer dass du die Intensität mit einer einzelnen Kurve steuerst. Diese wird mit dem Alpha kombiniert, sodass du eine Textur für Details und Falloff zur Steuerung des Rand-Ausblendens und der Intensität im Zentrum des Werkzeugs verwenden kannst.

Wenn die Kurve oben ist, bedeutet das volle Deformation; wenn sie unten ist, hat der Pinsel keinen Effekt.

Du kannst dir die Kurve als Querschnitt durch die Spitze des Pinsels vorstellen. Der untere Bereich zeigt eine Vorschau, wie ein einzelner „Stempel“ des Pinsels auf der Modelloberfläche aussehen würde; wenn es eine Alpha-Textur für den Pinsel gibt, wird diese ebenfalls angezeigt, um zu zeigen, wie Falloff und Alpha zusammenwirken.

### Preset
Wenn dies ausgewählt ist, öffnet ein Klick auf die Kurvengrafik ein Menü mit Presets. Abgerundete Kurven ergeben weichere Ergebnisse, eckige Kurven schärfere. Die Schaltfläche `Sub` in der linken Werkzeugleiste kehrt den Falloff effektiv um, sodass die Oberseite der Kurve in die Oberfläche hineindrückt statt herauszuziehen – oder umgekehrt.

### Catmull-Rom
Wenn ausgewählt, kann der Benutzer eigene Falloff-Kurven zeichnen. Der Kurveneditor funktioniert wie die Kurven im restlichen Nomad:

* Auf die Kurve klicken, um einen neuen Punkt zu erstellen
* Einen Punkt ziehen, um ihn zu verschieben
* Auf einen Punkt klicken, um zwischen scharf und weich umzuschalten
* Einen Punkt in einen benachbarten Punkt ziehen, um ihn zu entfernen

### B-spline
Wenn ausgewählt, kann der Benutzer eigene Falloff-Kurven zeichnen. Der Editor funktioniert wie bei Catmull-Rom, aber die Kurvenpunkte beeinflussen die Kurve, statt direkt auf ihr zu liegen, was beim Erstellen glatter Kurvenformen helfen kann.

Der Kurveneditor hat 3 Schaltflächen:

| Element  | Icon                        | Beschreibung                                 |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Kurveneditor maximieren                      |
| Reset    | ![](/icons/reset.webp)     | Kurve auf den Standardzustand zurücksetzen   |
| Symmetry | ![](/icons/symmetric.webp) | Kurve als symmetrische „Pinselspitze“ anzeigen |


### Einfluss

* Sphere (3d) – Der Einfluss wird berechnet, indem der Abstand vom Vertex zum Pinselzentrum genommen wird.
* Circle (2d) – Der Vertex wird zuerst auf die Flächenebene projiziert, bevor sein Abstand zum Pinselzentrum genommen wird. Dies ähnelt der Art, wie Alphas abgetastet werden. 
* Cylinder – Der Einfluss wird als Zylinder durch die Fläche projiziert, wie im Silhouette-Modus unten.

### Silhouette
Standardmäßig beeinflussen Striche nur die Modelloberfläche innerhalb des Pinselradius. Wenn Silhouette aktiviert ist, wird der Strich durch das gesamte Modell projiziert. Das ist sehr nützlich beim ersten Blocken eines Modells oder für Formen, bei denen die Seiten senkrecht bleiben sollen.



## Filter

![](/images/filter_menu.webp) 

### Strich akkumulieren
Kein Limit dafür aktivieren, wie viel Material pro Strich hinzugefügt/entfernt werden kann. Z. B. hat das Werkzeug `Clay` dies aktiviert, sodass Material sich weiter aufbauen kann, während das Werkzeug `Brush` dies deaktiviert hat, sodass Striche aufhören, Material hinzuzufügen, wenn du denselben Strich über dieselbe Region des Meshes bewegst. 

### Nur frontseitige Vertices
Diese Option ignoriert rückseitige Vertices.
Sie kann nützlich sein, wenn du nur einen Teil einer dünnen Geometrie bemalen willst, ohne die andere Seite zu beeinflussen.
Sie funktioniert auch beim Sculpting, kann aber zu Artefakten führen.

### Dynamische Topologie erlauben
Diese Option ist nur verfügbar, wenn dein Mesh im Modus [Dynamic Topology](topology.md#dynamic-topology) ist. Du kannst dynamische Topologie pro Werkzeug deaktivieren oder aktivieren.

### Verbundene Topologie
Nur die Vertices bearbeiten, die mit der Oberfläche verbunden sind, die du mit dem Werkzeug berührst. Zum Beispiel kannst du mit dem Werkzeug `Move` so einen Teil verschieben, auch wenn er sich mit einem anderen Teil überschneidet.
![](/videos/connected_topology.mp4)

### Bereich schützen
![](/images/filter_protect_area.webp) 

Diese Optionen verhindern, dass Werkzeuge Teile deines Meshes unter bestimmten Bedingungen beeinflussen. 

Die Option „Auto“ bedeutet: Wenn du Hide, Mask oder Facegroup im Menü [Shading](shading) sichtbar hast, werden sie geschützt; wenn sie in diesem Menü deaktiviert sind, ist der Schutz ausgeschaltet.

* `All` – Umschalter, ob die Schutzfilter global oder pro Werkzeug gelten.
* `Hide` – Wenn Teile des Meshes mit dem Hide-Werkzeug versteckt sind, legt fest, ob sie geschützt werden sollen.
* `Mask` – Wenn Teile des Meshes maskiert sind, legt fest, ob sie geschützt werden sollen.
* `Facegroup` – Legt fest, ob du ein Werkzeug nur innerhalb der zuerst berührten Facegroup verwenden kannst.


### Scharfe Kanten beibehalten
Punkte ausschließen, deren Normalen zu stark von der Flächennormale abweichen.

Dadurch ändert sich, wie die Flächenebene berechnet wird (Area sampling).

Diese Option kann für Flatten-basierte Werkzeuge nützlich sein oder wenn du eine überwiegend flache Oberfläche ohne Überlauf einfärben möchtest.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Einige Pinsel oder Strichoptionen benötigen eine Flächennormale und eine Flächenposition auf der Oberfläche, um zu funktionieren.

Du kannst steuern, wie diese durchschnittliche Ebene berechnet wird, indem du den Abtastbereich als Verhältnis des Werkzeugradius festlegst.

Bei 100 % wird jeder Punkt innerhalb des Auswahlkreises berücksichtigt.

Bei 0 % wird nur der nächste Vertex oder das nächste Dreieck berücksichtigt. Diese Werte können sowohl für `Normal radius` als auch für `Position radius` gekoppelt oder getrennt und unabhängig gesetzt werden.


### Tiefenmaskierung
![](/images/stroke_depthmask.webp)

Punkte ausschließen, die über oder unter einer bestimmten Distanz zur berechneten Ebene (Area sampling) liegen.

Damit kannst du nur auf Erhöhungen oder nur in Vertiefungen malen.

Die Grafik stellt einen Querschnitt der Oberfläche dar; die horizontale Linie ist die Oberfläche, der Kreis repräsentiert den Radius des Farb-Falloffs relativ über und unter der Oberfläche. `Height offset` ist ein Prozentsatz über oder unter der Oberfläche, ab dem die Maskierungsberechnung beginnt. `Top area` und `Bottom area` erlauben es dir, den Falloff oberhalb und unterhalb des Offset-Punkts zu skalieren.

#### Beispiel: In Vertiefungen malen
Um nur in Vertiefungen zu malen, setze den Height Offset auf -100 % und passe den Top-Area-Schieberegler so an, dass er von der horizontalen Linie entfernt ist. Das bedeutet, dass der erste Klick die „Null“-Tiefe festlegt und dann nur Bereiche unterhalb dieser Tiefe beeinflusst werden.

![](/videos/stroke_depth_cavity.mp4)

#### Beispiel: Auf Erhöhungen malen
Um nur auf hohen Bereichen zu malen, setze den Height Offset auf +90 %, sodass der untere Teil des Kreises die horizontale Linie nur leicht schneidet. Wenn du auf die Spitze einer „hohen“ Zone klickst, legt dies die Tiefe fest, sodass alles in dieser Tiefe, etwas darunter und alles darüber bemalt wird. Tiefe Vertiefungen werden übersprungen.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Steuert, wie der Stift-/Stylus-Druck die Pinsel beeinflusst.

Standardmäßig ist `Use global settings` aktiviert, d. h. alle Pinsel teilen sich dieselben Druckwerte.

### Pressure – Radius

Diese Kurve steuert, wie der Pinselradius vom Druck beeinflusst wird. Standard ist eine lineare Beziehung, sodass sich die Radiusänderung glatt anfühlen sollte, wenn dein Stylus eine gleichmäßige Reaktion hat. Viele Stifte haben jedoch eine nichtlineare Reaktion, die du mit dieser Kurve kompensieren kannst. Wenn sich der Radius z. B. nicht so anfühlt, als würde er bei hohem Druck seinen Maximalwert erreichen, verwende ein Kurvenpreset wie „out-pow3“ mit einer nach oben gebogenen Form, um den Radius früher zu erhöhen.

Dieser Dialog ähnelt der Falloff-Kurvenanzeige; du kannst ein Preset verwenden, indem du auf das Kurvenfenster tippst, oder deine eigenen Kurven mit den Modi Catmull-Rom und B-Spline zeichnen.

Wenn du einen konstanten Radius möchtest, deaktiviere diesen Abschnitt.

### Pressure – Intensity

Ähnlich wie beim Radiusregler, aber zur Steuerung der Intensität. Wenn du eine konstante Intensität möchtest, deaktiviere diesen Abschnitt.

### Druckglättung

Stiftdruck-Ereignisse mitteln, um glattere Ergebnisse zu erhalten.
