# ![](/icons/manual.webp) Tipps {#tips}

[[toc]]

## Wie man ein Modell beginnt {#how-to-start-a-model}

Anfänger im 3D-Sculpting fragen oft, was der beste Weg ist, ein Modell zu beginnen. Es gibt keinen besten Weg, verschiedene Leute haben unterschiedliche Vorlieben. Hier sind einige der gängigeren Ansätze.

### Auf Kugel mit Multires skulp­tieren {#sculpt-on-sphere-multires}

Das Standardmodell, das beim Start von Nomad geladen wird, ist der gebräuchlichste Weg. Verwende die Werkzeuge Verschieben, Clay, Crease, um die Kugel in Form zu drücken und zu ziehen. Nutze die niedrigeren Unterteilungsstufen, wenn du schnell große Änderungen machen willst, und höhere Unterteilungsstufen für Detailarbeit.

Ein häufiges Problem ist, dass dir oft dort Polygone ausgehen, wo du sie brauchst, während du anderswo zu viele hast. Wenn du z. B. die Standardkugel zu einem ganzen Körper verformst, wirst du wahrscheinlich nicht genug Details für die Finger haben, während du viele ungenutzte Polygone auf der Rückseite des Kopfes hast. Für überwiegend kugelförmige Formen wie einen Kopf kann das aber in Ordnung sein.

### Dyntopo {#dyntopo}

Wenn du Dyntopo aktivierst, werden beim Sculpten adaptiv Polygone hinzugefügt und entfernt. Diese Polygone sind Dreiecke, und Anfängern gefällt das unordentliche Layout oft nicht im Vergleich zum sauberen Look von Multires. Es lohnt sich, dranzubleiben! Wenn du Glättung aktivierst, das Drahtgitter ausschaltest und aufhörst, dir um das Layout Sorgen zu machen, kann sich dieser Modus sehr tonähnlich anfühlen. Vergiss nicht, dass bei einem großen Pinsel oder beim Glätten in diesem Modus auch Polygone entfernt werden können, sodass sich das Werkzeug immer schnell und reaktionsfreudig anfühlt. Wenn du einen ersten Durchgang des Sculpts fertig hast, kannst du es klonen, durch den Quad Remesher laufen lassen, um ein schönes Layout zu erhalten, und die ursprünglichen Details auf eine hohe Unterteilungsstufe reprojizieren.

### Voxel-Remesh {#voxel-remesh}

Voxel-Remesh wendet eine überwiegend quadbasierte Topologie auf dein Sculpt an. Dieser Vorgang ist bei niedrigen Auflösungen schnell und kann verwendet werden, um gedehnte oder übermäßig dichte Polygone schnell durch ein gleichmäßig verteiltes Layout zu ersetzen. Das kann ein großartiger Weg sein, um einen ganzen Körper aus einer Kugel zu beginnen; wenn du z. B. mit einem Kopf beginnst, kannst du einen Hals herausziehen, Voxel-Remesh. Einen Körper herausziehen, Voxel-Remesh, Arme, Voxel-Remesh und so weiter, bis du die Grundformen hast.

### Mehrere Objekte verwenden {#use-multiple-objects}

Viele Anatomieanleitungen stellen einen Körper aus einfachen Kugeln, Zylindern und Würfeln dar. Du kannst in Nomad auch auf diese Weise sculpten. Das hat den Vorteil, dass du Objekte in der Szenenhierarchie miteinander verknüpfen kannst, sodass du z. B. den Hals drehst und der Kopf folgt. Sehr nützlich ist auch, dass du das Gizmo-Werkzeug für präzises Verschieben/Drehen/Skalieren verwenden kannst, und du kannst pro Form eigene Pivotpunkte setzen, damit sie sich genau so bewegen, wie du es erwartest. Wenn die Grundblöcke an der richtigen Stelle sind, kannst du sie alle auswählen und per Voxel-Remesh oder Boolean zu einer einzigen Oberfläche für detaillierteres Sculpting zusammenfassen.

Ein praktischer Tipp für diese Arbeitsweise ist, mit einer Kugel zu beginnen, sie zu einer gestreckten Wurst zu skalieren, Pivot zu drücken, auf „Bottom“ zu klicken, Pivot erneut zu drücken. Du hast nun ein Körperteil, das du klonen, entlang der Länge der ersten Kugel verschieben, klonen, drehen, klonen, verschieben, klonen usw. kannst, um schnell einen Körper zu layouten.

### Röhren {#tubes}

Das Tube-Werkzeug ist ein großartiger Weg, ein Sculpt zu beginnen. Reptilienschwänze, Arme, Beine, Finger, Augenbrauen – all das kann mit dem Tube-Werkzeug schnell skizziert und anschließend leicht bearbeitet werden. Es erlaubt dir außerdem, das Querschnittsprofil zu verändern, was schnelle Formänderungen ermöglicht. Du kannst die Form validieren, um darauf zu sculpten, und sie zusammen mit anderen Objekten per Voxel-Remesh zu einem vollständigen Körpermesh verbinden.

### Andere Apps verwenden {#use-other-apps}

Manche Leute beginnen ein Modell lieber in anderen Apps, das ist ebenfalls in Ordnung. Tools wie Blender oder Valence erlauben es, Modelle mit Low-Poly-Techniken zu starten, die dann in Nomad zum Sculpten importiert werden können.

### Die eingebauten Presets verwenden {#use-the-built-in-presets}

Im Projektmenü klicke oben rechts auf `Preset...`. Hier findest du mehrere Kopf- und Körper-Presets von der Blender Foundation. Wähle eines aus, das dir gefällt, tippe erneut darauf und füge es deiner Szene hinzu. 

### Online-Modelle verwenden {#use-online-models}

Es gibt viele kostenlose Modelle online, z. B. bei Polyhaven, Sketchfab, Turbosquid. Diese Modelle können in der Regel in Nomad importiert und entweder direkt bearbeitet oder als Referenz verwendet werden.

### Keine Regeln! {#no-rules}

Letztendlich kannst du jede Kombination dieser Techniken verwenden – oder keine davon! Nomad ist in dieser Hinsicht sehr flexibel. Fortgeschrittene Nutzer beginnen vielleicht mit Tubes, verwenden dann Dyntopo, kombinieren das mit einem heruntergeladenen Fuß, machen dann einen Quad-Remesh über alles und nutzen Multires für die finalen Details. Was auch immer für dich funktioniert.

## Facegroups {#facegroups}

Das Facegroup-Werkzeug kann für viele Dinge verwendet werden, wie in diesem YouTube-Video erklärt wird: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Dies ist eine textliche Zusammenfassung der in diesem Video behandelten Funktionen.

### Warum Facegroups? {#why-facegroups}

Facegroups ermöglichen es dir, Flächen zu organisieren und auszuwählen („faces“ und „polygons“ werden in diesem Handbuch austauschbar verwendet). Das ist leichter zu erklären als Nomads andere Auswahl- und Organisationstools. In Nomad kannst du Objekte erstellen, benennen, parenten; es ist einfach, eine Struktur von Objekten zu erstellen, um einen Raum aus Boden, Wänden, Stuhl, Tisch usw. zu definieren.

Für eine Figur kannst du ein erstes Blockout mit separaten Objekten für Kopf, Arm, Bein machen, aber sobald du alle Teile zu einem einzigen Mesh zusammenfügst, geht diese Struktur verloren. Du kannst mit Masken an Teilbereichen einer Figur arbeiten, aber es kann ermüdend sein, immer wieder eine Maske für die Hände, dann die Nase, dann wieder die Hände zu malen.

Hier kommen Facegroups ins Spiel. Sie ermöglichen es dir, Polygonflächen mit einer Farbe zu markieren und dann Polygone mit derselben Farbe auszuwählen und zu bearbeiten. Beachte, dass Facegroup-Farbe und Vertex-Farbe unterschiedliche Dinge sind.

Die nächstliegende Analogie wäre, Farben auf eine Landkarte zu malen und später Länder oder Regionen anhand der Farbe auswählen zu können.

Für Charakterköpfe könntest du Zonen für Augenhöhlen, Nase, Lippen, Kinn, Ohren markieren und diese Zonen später leicht auswählen. Für Hard-Surface- und mechanisches Sculpting kann es nützlich sein, Paneele und Sektionen zu definieren.

### Facegroups erstellen und bearbeiten {#creating-and-editing-facegroups}

Facegroups können mit einem Pinsel angewendet werden, wobei jeder neue Strich eine neue Facegroup erzeugt, oder sie können die Facegroup unter dem Cursor auswählen und erweitern. Sie können auch mit Formen erstellt werden.

* Dot, Auto-Pick aktiviert – ein einzelnes Ziehen definiert eine neue Facegroup-Farbe und weist sie den Flächen zu, über die du ziehst. Jeder neue Zug definiert eine neue Facegroup. Ein Tippen füllt eine neue Facegroup flächendeckend.
* Dot, Auto-Pick deaktiviert – wenn die Auto-Pick-Schaltfläche in ihrem „sub“-Modus ist, wählt Nomad die Facegroup unter dem Cursor aus und wendet sie während des restlichen Strichs an. Das ist nützlich, um Facegroups zu verfeinern, ohne sie manuell auswählen zu müssen.

### Maskierung {#masking}

Wenn das Maskenwerkzeug aktiv ist und die Facegroup-Schaltfläche in seiner Werkzeugleiste aktiv ist, wird durch Tippen auf eine Facegroup diese maskiert.

### Ausblenden {#hiding}

Wenn das Hide-Werkzeug aktiv ist und die Facegroup-Schaltfläche in seiner Werkzeugleiste aktiv ist, wird durch Tippen auf eine Facegroup diese ausgeblendet.

### Organisieren {#organizing}

Wie bereits erwähnt, können Facegroups verwendet werden, um dein Mesh zu organisieren, ohne dass du separate Objekte erstellen musst. Du möchtest einen Kopf vielleicht nicht in separate Objekte für Nase, Kinn, Ohren aufteilen, aber es ist sehr nützlich, sie über Facegroups definiert zu haben.

### UV-Bereiche {#uv-regions}

Das UV-Atlas-Werkzeug versucht, Nähte automatisch zu definieren, setzt sie aber manchmal an Stellen, an denen du sie nicht haben willst. Wenn auf einem Objekt Facegroups existieren und die Facegroup-Option in den UV-Atlas-Optionen aktiv ist, werden stattdessen die Facegroup-Grenzen als UV-Nähte verwendet.

### Quad-Remesher {#quad-remesher}

Das Quad-Remesher-Plugin lässt Kanten auf deinem Modell normalerweise schön fließen, aber du kannst Facegroups verwenden, um es zu steuern, wenn die Facegroup-Option aktiviert ist. So lässt sich z. B. ein sauberer Edgeflow um Augen, Augenbrauenwulst, Lippen, Wangenfalte definieren.

### Mit anderen Werkzeugen filtern {#filter-with-other-tools}

Viele Werkzeuge haben Optionen, Facegroup-bewusst zu sein, entweder über ihr primäres Werkzeugmenü oder über das Menü Stroke -> Filtering. Zum Beispiel kann das Smooth-Werkzeug bei Stärken über 100 % Details innerhalb einer Facegroup aggressiv glätten, während die Facegroup-Grenze relativ intakt bleibt.

### Facegroup-Ränder entspannen und glätten {#relax-and-smooth-facegroup-borders}

Die Relax-Option innerhalb des Facegroup-Werkzeugs leistet hervorragende Arbeit beim Glätten von Facegroup-Grenzen, während andere Merkmale intakt bleiben. Das kann ein großartiger Weg sein, um glatte Facegroup-Grenzbereiche zu definieren, bevor du einen Quad-Remesh durchführst.

## Einschränkungen auf Tablet/Mobile {#limitations-on-tabletmobile}

Aktuelle Tablets und Mobilgeräte sind sehr leistungsfähig, haben aber wichtige Unterschiede zu Desktop-Computern und Laptops:

### Keine aktive Kühlung {#no-active-cooling}

Computer haben Lüfter und/oder große Kühlkörper, um sie kühl zu halten, und sind dafür ausgelegt, bei hohen Temperaturen zu laufen. Mobile Hardware ist in der Regel in erster Linie auf Dünnheit ausgelegt, nicht darauf, die Innereien kühl zu halten. Wenn Nomad mit den höchsten Qualitätseinstellungen betrieben wird (PBR-Lichtmodus, komplexe Materialien, viele Objekte, viele aktivierte Post-Processing-Optionen), kann dies das Gerät überhitzen und den Akku sehr schnell entladen. 

Ein besserer Ansatz ist, einen Matcap-Lichtmodus zu verwenden und den Render-Multiplikator zu verringern (oben im Post-Process-Menü). Diese Einstellungen halten das Gerät kühl und ermöglichen längeres Sculpten.

### Begrenzter Speicher {#limited-memory}

Nomad kann Ergebnisse erzielen, die den meisten Desktop-Sculpting-Apps ebenbürtig sind, aber es kann die Naturgesetze nicht aushebeln! Die meisten Desktop-Computer haben doppelt so viel Speicher wie Mobilgeräte, Workstations für 3D-Animation haben oft das 4- bis 8-fache an Speicher. Daher ist es gut, sich bewusst zu sein, wie viele Polygone du verwendest, und auf deinem Gerät zu testen, ab wann es träge wird. Fast alle Geräte, auf denen Nomad läuft, kommen mit 1 Million Polygonen problemlos zurecht. Ein M2 iPad Pro kann 8 Millionen komfortabel handhaben, und auf den neuesten iPads wurden in Tests deutlich höhere Werte erreicht.

Das heißt: Nur die detailliertesten Sculpts benötigen mehr als 4 Millionen Polys; wenn du relativ einfache Objekte erstellst und dich oft über 500.000, 1 Million, 4 Millionen wiederfindest, verwendest du zu viele Polygone! Stelle sicher, dass im Optionen-Menü der Smooth-Shaded-Modus aktiviert ist.

### OS ist bei intensiven Apps weniger fehlertolerant {#os-is-less-forgiving-with-intensive-apps}

Apple und Android erwarten, dass Apps kleine Dateien sehr schnell speichern und laden. Sie gehen außerdem davon aus, dass Apps sehr schnell zwischen Aufgaben wechseln können. Nomad nutzt zwar clevere Tricks, um Dateigrößen relativ klein zu halten und sie sehr schnell zu speichern, aber wenn das mobile Betriebssystem entscheidet, dass Nomad zu lange braucht, wird es die App einfach beenden, bevor sie ihre Aufgabe abgeschlossen hat. Das ist ein weiterer Grund, Dateien eher klein zu halten; es ist möglich, mit 37-Millionen-Poly-Sculpts zu arbeiten, wie ein Nutzer auf Discord berichtete, aber es ist nicht empfehlenswert!

## Arbeiten auf kleinen Bildschirmen {#working-on-small-screens}

Nomad ist für Tablets ausgelegt, funktioniert aber auch gut auf Telefonen. Sculpting auf einem kleinen Bildschirm wie einem Handy kann mit ein paar UI- und Workflow-Anpassungen erleichtert werden:

* Ein 4-Finger-Tap blendet die gesamte UI ein/aus und gibt dir mehr Platz zum Sculpten.
* Ein 3-Finger-Drag nach oben/unten ändert den Pinselradius.
* Die UI-Skalierung kann verkleinert werden, um mehr Buttons unterzubringen, wenn du gute Augen hast, oder vergrößert, wenn du schlecht siehst.
* Die breiteren Menüs können manchmal das Sculpt verdecken; du kannst sie transparent und ohne Unschärfe machen, damit du das Sculpt unter dem Menü sehen kannst.
* Wenn du mit dem Finger sculptest, verwende die Offset-Option, um das Pinselzentrum etwas von deinem Finger weg zu verschieben.
* Diese und viele weitere Optionen findest du im [Interface-Menü](./interface.md). 

## Aufblas- oder Peak-Deformer {#inflate-or-peak-deformer}

Viele 3D-Apps verfügen über einen Inflate-Deformer, der alle Vertices entlang ihrer Normalen um einen steuerbaren Betrag verschiebt. Obwohl Nomad derzeit keine Deformer besitzt, lässt sich dieses Verhalten mit dem Inflate-Pinsel emulieren:

* Wähle den Inflate-Pinsel.
* Ändere im [Stroke-Menü](./stroke.md#stroke) die Stroke-Methode auf `Lock + Radius`.
* Mache den Pinselradius größer als dein Sculpt, zoome die Kamera bei Bedarf vom Sculpt weg.
* Klicke und ziehe einen Strich auf der Oberfläche deines Objekts; wenn der Radius größer als das Objekt ist, wird die gesamte Form gleichmäßig um einen festen Betrag aufgeblasen.
* Passe die Pinselintensität an, um die Stärke der Aufblähung zu steuern.
* Verwende Maskierung, um bestimmte Bereiche zu schützen oder die Wirkung von Inflate dort zu reduzieren.

## Beulen oder „Pickel“ nach einem Voxel-Remesh entfernen {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel-Remesh ist großartig, um gleichmäßig verteilte Polygone zu erzeugen, erzeugt aber manchmal eine Topologie, die beim Glätten kleine Beulen oder Pickel verursacht. Zum Beispiel:

* Verwende den Crease-Pinsel auf der Standardkugel und mache eine Spirale.
* Voxel-Remesh mit „Build Multiresolution at 3“.
* Glätten mit hoher Intensität.
* Artefakte erscheinen (leichter mit einem kontrastreichen Matcap-Material zu sehen):

![](/videos/tip_pimples_before.mp4)

Um dies per Sculpting zu beheben, probiere die Option `Stable smoothing` in den Smooth-Einstellungen. Diese kann mit dem ungleichmäßigen Topologie-Layout des Voxel-Remesh umgehen und saubere Ergebnisse liefern.

![](/videos/tip_pimples_stable_smooth.mp4)

Um die Topologie selbst zu beheben, verwende ein neues Primitive, die Quad-Remesh-Tools oder einen externen 3D-Modeler und projiziere Details vom ursprünglichen Mesh auf das neue über `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Tageslicht-Beleuchtung {#daylight-lighting}

Das standardmäßige PBR-Rendering ist, wie der Name schon sagt, physikalisch basiert und kann wie ein unbearbeitetes Digitalfoto etwas ausgewaschen und flach wirken. Nomads Lichter und Post-Processing können verwendet werden, um Renderings lebendiger aussehen zu lassen.

Hier ist ein Standard-Render, sehen wir, ob wir ihn verbessern können:
![](/images/tips_lighting_default.webp)

Das Aktivieren von Post-Processing und Tonemapping kann Helligkeit und Kontrast erhöhen:

![](/images/tips_lighting_tonemap.webp)

Um sich auf die Lichter zu konzentrieren: Das Standard-Umgebungslicht ist gut zum Sculpten, kann aber für ein finales Rendering verbessert werden. Eine Möglichkeit, darüber nachzudenken, ist die Trennung von direktem Licht (z. B. die Sonne) und Umgebungslicht (z. B. Licht vom Blau des Himmels, vom Boden). Wenn du das Umgebungslicht reduzierst und drehst, fängst du ein, wie die Beleuchtung aussehen sollte, wenn das Motiv sich in einem schattigen Bereich befindet:

![](/images/tips_lighting_env.webp)

Ein direktes Licht kann hinzugefügt und seine Intensität erhöht werden, um harte Sonneneinstrahlung zu simulieren. Durch das Ausbalancieren mit dem Umgebungslicht lässt sich ein ansprechendes Ergebnis erzielen:

![](/images/tips_lighting_sunlight.webp)

Charaktere profitieren davon, wenn ihr Material auf Subsurface umgestellt wird und ein Spotlight hinter der Figur platziert wird, das auf die Ohren zielt, damit diese leuchten:

![](/images/tips_lighting_sss.webp)

Experimentiere anschließend mit den restlichen Post-Process-Einstellungen! Global Illumination und Ambient Occlusion helfen bei realistischeren Lichtverhältnissen. Curvature und Sharpen können mehr Details im Sculpt hervorheben. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette helfen, Kameraeffekte zu simulieren. Beachte, dass beim Aktivieren von Features die Beleuchtung und andere Post-Processing-Werte angepasst werden müssen, um das auszugleichen.

Hier ist das Rendering mit einem vollständigen Satz an Post-Processing-Anpassungen:
![](/images/tips_lighting_final.webp)