# ![](/icons/manual.webp) Tipps {#tips}

[[toc]]

## Wie man ein Modell beginnt {#how-to-start-a-model}

Einsteiger im 3d-Sculpting fragen oft, wie man ein Modell am besten beginnt. Den einen besten Weg gibt es nicht, jeder hat andere Vorlieben. Hier sind einige der gängigsten Ansätze.

### Auf einer Kugel sculpten, Multiauflösung {#sculpt-on-sphere-multires}

Das Standardmodell beim Start von Nomad ist der gängigste Weg. Formen Sie die Kugel mit den Werkzeugen Bewegen, Ton und Falte durch Drücken und Ziehen. Nutzen Sie die niedrigeren Unterteilungsstufen für schnelle, große Änderungen und die höheren für Detailarbeit.

Ein häufiges Problem: Dort, wo Sie Polygone brauchen, gehen sie Ihnen aus, während anderswo viel zu viele sind. Formen Sie die Standardkugel zum Beispiel zu einem ganzen Körper, reichen die Details wahrscheinlich nicht für die Finger, während am Hinterkopf viele Polygone verschwendet werden. Für überwiegend runde Formen wie einen Kopf kann das aber gut funktionieren.

### Dyntopo {#dyntopo}

Mit Dyntopo werden beim Sculpten je nach Bedarf Polygone hinzugefügt und entfernt. Diese Polygone sind Dreiecke, und Einsteiger mögen das unordentliche Netz oft nicht so sehr wie das saubere Bild der Multiauflösung. Dranbleiben lohnt sich! Schalten Sie Smooth Shading ein, das Drahtgitter aus und machen Sie sich keine Gedanken über das Netz, dann fühlt sich dieser Modus sehr nach Ton an. Denken Sie daran: Mit einem großen Pinsel oder einem Glätten-Pinsel kann dieser Modus auch Polygone entfernen, sodass sich das Werkzeug immer schnell und reaktionsfreudig anfühlt. Steht ein erster Entwurf, können Sie ihn klonen, mit Quad Remesher ein sauberes Netz erzeugen und die ursprünglichen Details auf eine hohe Unterteilungsstufe reprojizieren.

### Voxel Remesh {#voxel-remesh}

Voxel Remesh legt eine überwiegend aus Quads bestehende Topologie über Ihr Modell. Bei niedrigen Auflösungen geht das schnell, und so ersetzen Sie gestreckte oder zu dichte Polygone rasch durch ein gleichmäßiges Netz. Ein toller Weg, um aus einer Kugel einen ganzen Körper zu formen: Beginnen Sie etwa mit einem Kopf, ziehen Sie einen Hals heraus, Voxel Remesh. Einen Körper herausziehen, Voxel Remesh, Arme, Voxel Remesh und so weiter, bis die Grundformen stehen.

### Mehrere Objekte verwenden {#use-multiple-objects}

Viele Anatomie-Ratgeber stellen einen Körper aus einfachen Kugeln, Zylindern und Würfeln dar. So können Sie auch in Nomad sculpten. Der Vorteil: Sie können Objekte in der Szenenhierarchie einander unterordnen, sodass zum Beispiel der Kopf folgt, wenn Sie den Hals drehen. Sehr nützlich ist auch das Gizmo-Werkzeug für präzises Verschieben, Drehen und Skalieren, und Sie können für jede Form einen eigenen Drehpunkt festlegen, damit sie sich genau wie erwartet bewegt. Sitzen die Grundblöcke an der richtigen Stelle, wählen Sie alle aus und verbinden sie per Voxel Remesh oder Boolean zu einer einzigen Oberfläche, um weiter ins Detail zu gehen.

Ein praktischer Tipp für diese Arbeitsweise: Beginnen Sie mit einer Kugel, skalieren Sie sie zu einer langgezogenen Wurst, drücken Sie auf Drehpunkt, tippen Sie auf „Unten“ und drücken Sie erneut auf Drehpunkt. Jetzt haben Sie ein Körperteil, das Sie klonen, entlang der ersten Kugel verschieben, klonen, drehen, klonen, verschieben, klonen usw. können, um schnell einen Körper anzulegen.

### Röhren {#tubes}

Das Werkzeug Röhre ist ein toller Einstieg in ein Modell. Reptilienschwänze, Arme, Beine, Finger, Augenbrauen: All das lässt sich mit dem Werkzeug Röhre schnell skizzieren und danach leicht bearbeiten. Sie können auch das Querschnittsprofil ändern und so die Form rasch anpassen. Bestätigen Sie die Form, um darauf zu sculpten, und verbinden Sie sie per Voxel Remesh mit anderen Objekten zu einem Mesh für den ganzen Körper.

### Andere Apps verwenden {#use-other-apps}

Manche beginnen ein Modell lieber in anderen Apps, auch das ist in Ordnung. In Programmen wie Blender oder Valence lassen sich Modelle mit Low-Poly-Techniken beginnen und dann zum Sculpten in Nomad importieren.

### Die mitgelieferten Presets verwenden {#use-the-built-in-presets}

Tippen Sie im Menü [Dateien](files.md) links im Projektbereich auf `Preset…`. Dort finden Sie mehrere Kopf- und Körper-Presets der Blender Foundation. Wählen Sie eines aus, das Ihnen gefällt, tippen Sie erneut darauf und fügen Sie es Ihrer Szene hinzu. 

### Modelle aus dem Internet verwenden {#use-online-models}

Online gibt es viele kostenlose Modelle, etwa bei Poly Haven, Sketchfab oder TurboSquid. Meist lassen sich diese Modelle in Nomad importieren und dann entweder direkt bearbeiten oder als Referenz nutzen.

### Keine Regeln! {#no-rules}

Letztlich können Sie diese Techniken beliebig kombinieren oder ganz darauf verzichten! Nomad ist hier sehr flexibel: Fortgeschrittene beginnen vielleicht mit Röhren, wechseln dann zu Dyntopo, kombinieren das mit einem heruntergeladenen Fuß, wenden auf alles Quad Remesh an und nutzen am Ende Multiauflösung für die feinen Details. Was immer für Sie funktioniert.

## Face-Gruppen {#facegroups}

Das Werkzeug Face-Gruppe lässt sich für vieles nutzen, wie dieses YouTube-Video zeigt: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Hier ist eine schriftliche Zusammenfassung der im Video gezeigten Funktionen.

### Wozu Face-Gruppen? {#why-facegroups}

Mit Face-Gruppen ordnen Sie Faces und wählen sie aus („Faces“ und „Polygone“ werden in diesem Handbuch gleichbedeutend verwendet). Am einfachsten lässt sich das im Vergleich zu den anderen Auswahl- und Ordnungswerkzeugen von Nomad erklären. In Nomad können Sie Objekte erstellen, benennen und einander unterordnen. So bauen Sie leicht eine Struktur auf, etwa einen Raum aus Boden, Wänden, Stuhl, Tisch und so weiter.

Bei einer Figur legen Sie die Grundform vielleicht mit separaten Objekten für Kopf, Arm und Bein an. Sobald Sie aber alle Teile zu einem einzigen Mesh zusammenführen, geht diese Struktur verloren. Mit Masken können Sie an Teilbereichen einer Figur arbeiten, aber ständig eine Maske für die Hände, dann für die Nase und dann wieder für die Hände zu malen, wird schnell mühsam.

Hier sind Face-Gruppen nützlich. Damit markieren Sie Polygone mit einer Farbe und können dann Polygone derselben Farbe auswählen und bearbeiten. Die Farbe einer Face-Gruppe und die Vertex-Farbe sind übrigens zwei verschiedene Dinge.

Am ehesten lässt sich das mit dem Einfärben einer Landkarte vergleichen, auf der Sie später Länder oder Regionen anhand ihrer Farbe auswählen können.

Bei Köpfen von Figuren könnten Sie Zonen für Augenhöhlen, Nase, Lippen, Kinn und Ohren malen und diese Zonen später leicht auswählen. Beim Hard-Surface- und mechanischen Sculpting lassen sich damit Platten und Abschnitte festlegen.

### Face-Gruppen erstellen und bearbeiten {#creating-and-editing-facegroups}

Face-Gruppen lassen sich mit einem Pinsel auftragen, wobei jeder neue Strich eine neue Face-Gruppe erzeugt. Sie können aber auch die Face-Gruppe unter dem Cursor auswählen und erweitern. Außerdem lassen sie sich mit Formen erstellen.

* Punkt, Standardmodus - ein einzelnes Ziehen legt eine neue Face-Gruppen-Farbe fest und weist sie den überstrichenen Faces zu. Jedes neue Ziehen legt eine neue Face-Gruppe an. Ein Tippen füllt einen Bereich mit einer neuen Face-Gruppe.
* Punkt, Modus `Wählen` - ist der Button `Wählen` in der linken Werkzeugleiste aktiv, übernimmt Nomad die Face-Gruppe unter dem Cursor und trägt sie für den Rest des Ziehens auf. So verfeinern Sie Face-Gruppen, ohne sie von Hand auswählen zu müssen.

### Maskieren {#masking}

Ist das Werkzeug Maske aktiv und in seiner Werkzeugleiste der Face-Gruppen-Button eingeschaltet, maskiert ein Tippen auf eine Face-Gruppe diese.


### Ausblenden {#hiding}

Ist das Werkzeug Ausblenden aktiv und in seiner Werkzeugleiste der Face-Gruppen-Button eingeschaltet, blendet ein Tippen auf eine Face-Gruppe diese aus.

### Ordnen {#organizing}

Wie schon erwähnt, ordnen Sie mit Face-Gruppen Ihr Mesh, ohne separate Objekte anlegen zu müssen. Einen Kopf wollen Sie vielleicht nicht in einzelne Objekte für Nase, Kinn und Ohren aufteilen, es ist aber sehr nützlich, diese Bereiche als Face-Gruppen festzulegen.

### UV-Bereiche {#uv-regions}

Das Werkzeug UV Atlas versucht, Nähte automatisch zu setzen, legt sie aber manchmal dorthin, wo Sie sie nicht haben möchten. Hat ein Objekt Face-Gruppen und ist die Face-Gruppen-Option in den Einstellungen von UV Atlas aktiv, nutzt es stattdessen die Grenzen der Face-Gruppen als UV-Nähte.

### Quad Remesher {#quad-remesher}

Das Plugin Quad Remesher lässt die Kanten auf Ihrem Modell meist schön fließen, doch mit aktivierter Face-Gruppen-Option können Sie es mit Face-Gruppen gezielt lenken. So legen Sie leicht einen sauberen Kantenfluss fest, zum Beispiel um die Augen, einen Brauenbogen, die Lippen oder eine Wangenfalte.

### Mit anderen Werkzeugen filtern {#filter-with-other-tools}

Viele Werkzeuge haben Optionen, um Face-Gruppen zu berücksichtigen, entweder in ihrem eigenen Werkzeugmenü oder über das Menü Strich -> Filter. Das Werkzeug Glätten kann zum Beispiel bei Stärken über 100 % Details innerhalb einer Face-Gruppe kräftig wegglätten, die Grenze der Face-Gruppe aber weitgehend erhalten.

### Grenzen von Face-Gruppen entspannen und glätten {#relax-and-smooth-facegroup-borders}

Die Option `Entspannen` im Werkzeug Face-Gruppe glättet die Grenzen von Face-Gruppen hervorragend und lässt andere Merkmale dabei unverändert. So legen Sie vor einem Quad Remesh saubere, glatte Grenzbereiche fest.

## Einschränkungen auf Tablet/Smartphone {#limitations-on-tabletmobile}

Aktuelle Tablets und Smartphones sind sehr leistungsstark, unterscheiden sich aber in wichtigen Punkten von Desktop-Computern und Laptops:

### Keine aktive Kühlung {#no-active-cooling}

Computer haben Lüfter und/oder große Kühlkörper und sind dafür gebaut, bei hohen Temperaturen zu laufen. Mobile Geräte sind meist vor allem auf geringe Dicke ausgelegt, nicht auf die Kühlung ihres Innenlebens. Wird Nomad auf die höchsten Qualitätseinstellungen getrieben (PBR-Beleuchtung, komplexe Materialien, viele Objekte, viele aktive Nachbearbeitungsoptionen), kann das Gerät überhitzen und der Akku sehr schnell leer werden. 

Besser ist es, den MatCap-Modus und eine niedrigere `Render-Auflösung` (oben im Menü Nachbearbeitung) zu verwenden. So bleibt das Gerät kühl und Sie können länger sculpten.

### Begrenzter Speicher {#limited-memory}

Nomad erreicht Ergebnisse wie die meisten Sculpting-Programme auf dem Desktop, kann aber die Gesetze der Physik nicht aushebeln! Die meisten Desktop-Computer haben doppelt so viel Arbeitsspeicher wie mobile Geräte, Workstations für 3d-Animation oft 4- oder 8-mal so viel. Deshalb ist es gut, im Blick zu behalten, wie viele Polygone Sie verwenden. Testen Sie auf Ihrem Gerät, ab wann es zu ruckeln beginnt. Fast alle Geräte, auf denen Nomad läuft, kommen mit 1 Million Polygonen problemlos zurecht. Ein iPad Pro mit M2 schafft bequem 8 Millionen, und auf den neuesten iPads wurde schon deutlich mehr getestet.

Allerdings brauchen nur die detailliertesten Modelle mehr als 4 Millionen Polygone. Wenn Sie eher einfache Objekte gestalten und dabei oft über 500.000, 1 Million oder 4 Millionen kommen, verwenden Sie zu viele Polygone! Achten Sie darauf, dass `Smooth Shading` in den [Einstellungen](settings.md) aktiviert ist.

### Das Betriebssystem ist mit rechenintensiven Apps weniger nachsichtig {#os-is-less-forgiving-with-intensive-apps}

Apple und Android erwarten, dass Apps kleine Dateien sehr schnell speichern und laden. Sie gehen auch davon aus, dass Apps sehr schnell zwischen Aufgaben wechseln können. Nomad nutzt zwar einige clevere Tricks, um Dateien relativ klein zu halten und sehr schnell zu speichern, doch wenn das mobile Betriebssystem meint, dass Nomad zu lange braucht, beendet es die App einfach, bevor sie fertig ist. Ein weiterer Grund, Dateien eher klein zu halten: Mit Modellen aus 37 Millionen Polygonen zu arbeiten ist möglich, wie ein Nutzer auf Discord berichtet hat, wird aber nicht empfohlen!

## Auf kleinen Bildschirmen arbeiten {#working-on-small-screens}

Nomad ist für Tablets gemacht, funktioniert aber auch auf Smartphones gut. Mit ein paar Anpassungen an Oberfläche und Arbeitsweise wird das Sculpten auf einem kleinen Bildschirm wie dem eines Smartphones leichter:

* Ein Tippen mit 4 Fingern blendet die gesamte Oberfläche ein oder aus, so haben Sie mehr Platz zum Sculpten.
* Ein Ziehen mit 3 Fingern nach oben und unten ändert den Pinselradius
* Die Oberfläche lässt sich kleiner skalieren, damit mehr Buttons Platz finden, wenn Sie gute Augen haben, oder größer, wenn nicht!
* Die breiteren Menüs können manchmal das Modell verdecken. Machen Sie sie transparent und ohne Unschärfe, damit Sie das Modell unter dem Menü sehen.
* Sculpten Sie mit dem Finger, verschieben Sie mit der Option [`Strichversatz`](stroke.md#stroke-offset) die Pinselmitte ein Stück von Ihrem Finger weg.
* Diese und viele weitere Optionen finden Sie im [Menü Oberfläche](./interface.md). 


## Aufblähen- oder Spitzen-Deformer {#inflate-or-peak-deformer}

Viele 3d-Apps bieten einen Aufblähen-Deformer, der alle Vertices um einen einstellbaren Betrag entlang ihrer Normale verschiebt. Nomad hat derzeit keine Deformer, das Verhalten lässt sich aber mit dem Pinsel Aufblähen nachbilden:

* Wählen Sie den Pinsel Aufblähen
* Stellen Sie im [Menü Strich](./stroke.md#stroke) den Strichtyp auf `Grab • Dynamischer Radius`
* Machen Sie den Pinselradius größer als Ihr Modell und zoomen Sie die Kamera bei Bedarf vom Modell weg.
* Tippen Sie auf die Oberfläche Ihres Objekts und ziehen Sie einen Strich. Ist der Radius größer als das Objekt, wird die gesamte Form gleichmäßig um einen festen Betrag aufgebläht.
* Mit der Pinselstärke steuern Sie, wie stark aufgebläht wird
* Schützen Sie bestimmte Bereiche bei Bedarf mit einer Maske oder schwächen Sie dort den Effekt ab.

## Beulen oder „Pickel“ nach einem Voxel Remesh entfernen {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel Remesh eignet sich hervorragend für gleichmäßig verteilte Polygone, erzeugt aber manchmal eine Topologie, die beim Glätten kleine Beulen oder Pickel verursacht. Zum Beispiel:

* Ziehen Sie mit dem Pinsel Falte einen Wirbel auf die Standardkugel
* Voxel Remesh mit `Multiresolution erstellen` auf 3
* Mit hoher Stärke glätten
* Artefakte erscheinen (mit einem kontrastreichen MatCap-Material leichter zu sehen):

![](/videos/tip_pimples_before.mp4)

Um das beim Sculpten zu beheben, probieren Sie die Option `Stabiles Glätten` in den Einstellungen von Glätten. Sie kommt mit der ungleichmäßigen Topologie des Voxel Remesh zurecht und liefert saubere Ergebnisse.

![](/videos/tip_pimples_stable_smooth.mp4)

Um die Topologie selbst zu korrigieren, verwenden Sie eine neue Grundform, die Quad-Remesh-Werkzeuge oder ein externes 3d-Modellierprogramm und projizieren die Details des ursprünglichen Meshs über `Topologie -> Backen -> Reprojizieren → Vertex` auf das neue. 

![](/videos/tip_pimples_reproject.mp4)

## Tageslicht-Beleuchtung {#daylight-lighting}

Das Standard-PBR-Rendering ist, wie der Name schon sagt, physikalisch basiert und kann daher wie ein unbearbeitetes Digitalfoto etwas blass und flach wirken. Mit den Lichtern und der Nachbearbeitung von Nomad lassen Sie Renderings lebendiger aussehen.

Hier ein Standard-Rendering. Mal sehen, ob es sich verbessern lässt:
![](/images/tips_lighting_default.webp)

Nachbearbeitung und Tone-Mapping zu aktivieren, kann für mehr Helligkeit und Kontrast sorgen:

![](/images/tips_lighting_tonemap.webp)

Zu den Lichtern: Das Standard-Umgebungslicht eignet sich gut zum Sculpten, lässt sich für ein finales Rendering aber verbessern. Eine Herangehensweise ist, direktes Licht (z. B. die Sonne) und Umgebungslicht (z. B. das Licht vom Blau des Himmels oder vom Boden) getrennt zu betrachten. Verringern und drehen Sie das Umgebungslicht, sieht die Beleuchtung schon so aus, als stünde das Motiv im Schatten:

![](/images/tips_lighting_env.webp)

Fügen Sie ein direktes Licht hinzu und erhöhen Sie seine Stärke, um grelles Sonnenlicht nachzubilden. Im Gleichgewicht mit dem Umgebungslicht ergibt das ein ansprechendes Ergebnis:

![](/images/tips_lighting_sunlight.webp)

Figuren profitieren davon, wenn Sie ihr Material auf Subsurface umstellen und hinter der Figur ein Spotlicht auf die Ohren richten, damit sie leuchten:

![](/images/tips_lighting_sss.webp)

Experimentieren Sie dann mit den übrigen Einstellungen der Nachbearbeitung! Globale Illumination und Ambient Occlusion sorgen für realistischere Beleuchtung. Krümmung und Schärfen holen mehr Details aus dem Modell heraus. Chromatische Aberration, Depth Of Field, Körnung, Bloom und Vignette bilden Kameraeffekte nach. Beachten Sie, dass Sie die Beleuchtung und die übrigen Werte der Nachbearbeitung nachjustieren müssen, sobald Sie Funktionen aktivieren.

Hier das Rendering mit einem kompletten Satz an Anpassungen der Nachbearbeitung:
![](/images/tips_lighting_final.webp)
