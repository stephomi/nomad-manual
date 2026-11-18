# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Plattform {#platform}
### Wo liegen meine Projekte auf meinem Gerät? {#locate}
Die Projekte liegen im Ordner `projects` innerhalb des Nomad-Hauptordners.

Unter iOS erreichen Sie den Nomad-Ordner über die App Dateien.

Unter Android liegt der Nomad-Ordner in `Android/data/com.stephaneginier.nomad/files/`.  
Bei neueren Android-Versionen (10/11) haben Sie keinen Zugriff mehr auf den Ordner `Android/data`.
Sie erreichen ihn über eine separate App, zum Beispiel [diese hier](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Kann ich Betaversionen testen? {#beta}
Für Windows & MacOS gibt es eventuell eine Beta auf der [Homepage](https://nomadsculpt.com).
<br>
Für iOS gibt es ein privates TestFlight, schauen Sie dazu auf dem [Discord](https://discord.com/invite/8h7BwpRz29) im Kanal #beta-ios vorbei.
<br>
Die [Web-Demo](https://nomadsculpt.com/demo) wird meist mit den neuesten Funktionen aktualisiert.

### Warum gibt es unter Android eine kostenlose Testversion, unter iOS aber nicht? {#android-trial}
Weil alte Android-Geräte furchtbar sind (und manche neuere auch...) und ich nicht wollte, dass jemand die App kauft und dann von einem schwarzen Bildschirm begrüßt wird.
Der Hauptgrund ist aber, dass kostenpflichtige Apps unter Android meinem Gefühl nach nicht wirklich die Regel sind.

### Welches Tablet eignet sich am besten für Nomad? {#best-tablet}

Kurz gesagt: ein iPad.

Die etwas längere Antwort lautet: 

> „Das neueste iPad, _das Sie sich leisten können_. Außer Sie können Apple wirklich nicht ausstehen, dann das neueste Samsung-Tablet, das Sie sich leisten können. Alles andere vorher testen.“ 

Die Leute wollen immer mehr wissen, daher hier eine Zusammenfassung.

Am besten läuft Nomad auf neueren iPads:

* iPads und iPhones haben Zugriff auf das Plugin [Quad Remesher](tools#quad-remesher) von [Exoside](https://exoside.com/)
* neuere iPads mit dem neuesten Pencil unterstützen [Barrel Roll](https://www.youtube.com/watch?v=XcDQazDYpo0): Bei bestimmten Werkzeugen in Nomad können Sie den Pencil drehen. 
* die neuesten Chips der M-Serie sind sehr schnell. 

Das neueste und teuerste iPad rendert finale Bilder sehr schnell und lässt Sie sehr viele Details sculpten.

Bei günstigeren und älteren iPads fällt die Leistung aber weniger stark ab, als man erwarten würde. Jedes iPad, das einen Apple Pencil unterstützt, führt Nomad recht gut aus. Zum Beispiel:

* Ein iPad Pro von 2023 kommt mit Modellen aus 5 Millionen Polygonen flüssig zurecht und rendert ein Bild in finaler Qualität in 5 Sekunden.
* Ein iPad Pro von 2015 schafft ein Objekt mit 1,2 Millionen Polygonen mit leichter Verzögerung und rendert ein Bild in finaler Qualität in 20 Sekunden.

Das ist ein großer Leistungsunterschied, aber Sie müssen auch den Preis berücksichtigen:

* Das iPad Pro von 2025 kostet neu mit allen Optionen *2500 USD*. 
* Das iPad Pro von 2023 kostet derzeit *400 USD* auf eBay.
* Das iPad Pro von 2015 kostet *250 USD* auf eBay.

Sind 4 Millionen Polygone mehr und 15 Sekunden Zeitersparnis 2100 USD wert? Das entscheiden Sie.

Modelle ohne „Pro“ sind noch günstiger und bieten eine große Auswahl an Größen und Leistungsstufen. Das aktuelle iPad Air unterstützt den Pencil der 2. Generation mit Barrel Roll und ist deutlich günstiger als das Pro. Gebrauchte und generalüberholte Geräte bieten noch mehr Auswahl. 

Egal wie groß Ihr Budget ist, Sie sollten also ein passendes iPad finden. Und denken Sie daran: Die meisten Modelle haben keine Millionen Polygone! Bleiben Sie unter 500.000 Polygonen, sculpten Sie selbst auf alten iPads flott.

`Und Android?`

Die Grafikleistung von Android liegt unter der von iPads. Laut dem Entwickler von Nomad „läuft Nomad auf einem Samsung Galaxy Tab S9 eine Größenordnung langsamer als auf einem iPad Air“. Trotzdem sind viele Nutzer mit ihren Samsung-Tablets sehr zufrieden, für die meisten Sculpting-Aufgaben läuft Nomad gut. 

Bei anderen Android-Tablets ist Vorsicht geboten. Die Leistung von Android-Hardware schwankt stark, es ist schwer vorherzusagen, wie Nomad darauf läuft.

Testen Sie bitte zuerst mit der kostenlosen Version von Nomad, bei der das Speichern deaktiviert ist. 

`Und Arbeitsspeicher und Speicherplatz?`

Die meisten Nomad-Dateien sind 100 MB groß oder kleiner. Fast jedes Tablet, das Sie heute kaufen, ob iPad oder Android, hat also reichlich Platz für Ihre Nomad-Projekte.


### Ich habe Nomad für ein Gerät gekauft. Kann ich es auf einem anderen Gerät verwenden? {#multi-devices}
Ja, solange es denselben App Store und dasselbe Konto nutzt.

Haben Sie Nomad zum Beispiel im iOS App Store gekauft, können Sie es auf Ihren anderen iOS-Geräten verwenden.

Haben Sie es für Ihr Android-Tablet bei Google Play gekauft, können Sie es auf Ihren anderen Android-Geräten verwenden.

Haben Sie Nomad aber unter Android gekauft und bekommen dann ein iPad, müssen Sie es erneut kaufen.

Das liegt daran, dass Nomad keinen eigenen Lizenzserver und kein Abo-Modell hat. Es gibt keine Vereinbarung zwischen Apple, Google und AppGallery, um Lizenzen zu teilen. 


### Wie stelle ich meinen Kauf wieder her? {#restore}
Google Play und AppGallery übernehmen die Synchronisierung beide automatisch.

- Öffnen Sie das Menü Über (Nomad-Symbol oben links) und tippen Sie auf `Kauf wiederherstellen`
- Prüfen Sie, ob Sie mit demselben Konto angemeldet sind, mit dem Sie Nomad gekauft haben (bei Google Play).
- Starten Sie das Gerät neu
- Manchmal muss man ein paar Stunden warten
- Stellen Sie sicher, dass die App Google Play auf dem neuesten Stand ist
- Installieren Sie Nomad neu (denken Sie daran, [Ihre Dateien zu sichern](#locate), wenn Sie nichts verlieren möchten)
- Sie können versuchen, die App erneut zu kaufen, und sehen, was passiert (Hinweis: Mit demselben Konto kann man denselben Artikel nicht zweimal kaufen)

:::tip
Sie können mich unter <support@nomadsculpt.com> erreichen, aber das *Einzige*, was ich tun kann, ist zu bestätigen, ob zu einer E-Mail-Adresse ein Kauf gehört.

Ich erhalte regelmäßig Meldungen über Lizenzen, die nach dem Kauf eines neuen Geräts nicht richtig übernommen werden.
Auf die Zahlung und die Kontosynchronisierung habe ich keinerlei Einfluss, das läuft alles über Google/AppGallery!

Am Ende wird der Kauf immer wiederhergestellt, aber welche Schritte das beschleunigen, ist unklar.
:::

::: warning
Neuere Huawei-Geräte haben keinen Zugriff auf die Google-Dienste.
In diesem Fall müssen Sie die App erneut in der AppGallery (dem App Store von Huawei) kaufen.
:::

### Können Sie [meine Sprache] übersetzen oder korrigieren? {#locale}
Ich kann relativ einfach eine weitere Sprache hinzufügen, setze aber auf KI-Übersetzung, da sie sich bei regelmäßigen Updates viel leichter handhaben lässt.
Die Übersetzungsdateien finden Sie [hier](https://github.com/stephomi/nomad-translation).

## Funktionen {#features}

### Warum bewegt sich das Gizmo nicht? {#gizmo-not-moving}
Möglicherweise ist [Fixieren in der linken Werkzeugleiste aktiviert](tools#left-menu-toolbar). 

### Kann man in Nomad animieren? {#animate}
Derzeit nicht. Eine Zeitleiste, mit der sich die Layer animieren lassen, wäre interessant, ist aber im Moment nicht wirklich geplant.  

Rigging/Skinning würde ich in Zukunft gern unterstützen, das bringt aber einige Herausforderungen mit sich (vor allem das Zusammenspiel mit den Sculpting-Werkzeugen...), daher ist vorerst nichts sicher.


### Kann man richtiges Low-Poly-Modeling betreiben? {#lowpoly}
Derzeit nicht.
Das gehört nicht wirklich zum Umfang von Nomad *Sculpt*, aber vielleicht biete ich in Zukunft ein paar Werkzeuge dafür an.


### Kann man mit UVs und Texturen arbeiten? {#texturing}
Kurz gesagt: Ja. Ausführlich: Nicht direkt, aber es gibt mehrere Wege, die hervorragenden Vertex-Malwerkzeuge von Nomad mit UVs und Texturen zu kombinieren.

* In Nomad malen Sie Farbe, Rauheit und Materialeigenschaften direkt in die Vertices Ihres Modells.
* Nomad erlaubt sehr hohe Vertex-Zahlen, sodass Sie malen können, ohne sich um UVs zu kümmern.
* Nomad kann Texturen für Pinsel laden, sodass Sie mit Texturen stempeln und malen können.
* Nomad kann Objekte mit bereits zugewiesenen Texturen laden, um sie zu rendern.
* Nomad kann Objekte mit wenigen Polygonen per [UV-Unwrapping](topology.md#uv-unwrap-uvatlas) abwickeln.
* Farbe, Rauheit und Metallizität lassen sich über [die Projektionsoptionen](topology.md#reproject-to-vertex) von Texturen auf Vertices übertragen.
* Farbe, Rauheit, Metallizität und Normalen lassen sich über [die Backoptionen](topology.md#bake-texture) von Vertices in Texturen backen
* Backen und Projizieren funktioniert zwischen einzelnen oder vielen Objekten oder zwischen der höchsten und der niedrigsten Unterteilungsstufe eines Objekts, was viele verschiedene Back- und Projektions-Workflows ermöglicht.
* Nach dem Backen werden beim Export als OBJ auch die Texturen exportiert, die Sie dann in eine App wie Procreate übernehmen können, um direkt auf die Texturen zu malen.

### Kann ich ein Drehscheiben-Video aufnehmen? {#video}
Vorerst nicht geplant. iOS hat eine [Bildschirmaufnahme-Funktion](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados), die sehr einfach zu bedienen ist.

Unter iOS wischen Sie dazu von oben links nach unten und tippen auf den Aufnahme-Button. Es folgt ein 3-Sekunden-Countdown: Wischen Sie das Menü weg, damit Nomad zu sehen ist, und nutzen Sie die Drehscheiben-Funktion. Wenn Sie fertig sind, wischen Sie wieder von oben rechts nach unten und tippen erneut auf den Aufnahme-Button. Kürzen Sie den Film anschließend in der Fotomediathek, um überflüssiges Material am Anfang und Ende zu entfernen.

### Können Sie [Lieblingsfunktion einfügen] als eigenen Button hinzufügen? {#interface}
Ja, die untere Werkzeugleiste lässt sich jetzt im Menü [Oberfläche](interface.md#shortcuts) anpassen, und es lassen sich schwebende Werkzeugleisten erstellen.

### Was sind die nächsten Funktionen? {#next-features}
Für die mittel- und langfristige Planung habe ich viele Ideen, aber noch nichts Konkretes.  

Fehlerbehebungen und die Verbesserung bestehender Funktionen haben immer Vorrang vor neuen Funktionen.


### Kann man in Nomad riggen? {#rigging}
Nein, aber es ist geplant. Vorerst können Sie Formen einander unterordnen und Drehpunkte verändern, um einfache, posierbare Modelle zu erstellen.

### Kann man mehr als 4 Lichter verwenden? {#lights}
Sie können auf Mobilgeräten bis zu 4 Lichter verwenden und auf dem Desktop bis zu 6. Das ist eine Einschränkung der Echtzeit-Render-Engine von Nomad. Mit leuchtenden Objekten und globaler Illumination in der Nachbearbeitung lässt sich das vortäuschen, wie [dieses Tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA) zeigt

### Kann man ZBrush-Werkzeuge importieren? {#zbrush-import}
Nein, ZBrush verwendet ein proprietäres Format. Die Alpha-Maps sollten Sie aber extrahieren und in Nomad verwenden können. 

### Warum stimmen die Farben nicht mit dem überein, was ich gemalt habe? Warum bekomme ich kein Weiß im Rendering? {#paint-pbr}
Stellen Sie sich vor, Sie fotografieren ein Blatt Papier, eine Schreibtischlampe und die Sonne. Ältere Kameras und Bildschirme machen alles einfach „weiß“. Modernere Systeme können einen Unterschied zeigen zwischen dem reflektierten Weiß des Papiers, dem ausgestrahlten Licht einer Lampe und der extremen Helligkeit der Sonne.

Moderne Computergrafik versucht, ähnlich zu arbeiten, und bildet die Physik von Licht und Oberflächen nach. Das nennt sich `Physically Based Rendering` oder PBR, und darauf basiert der PBR-Renderer von Nomad. Das wirkt realistisch und ausgewogen, hell gemalte Farben erscheinen dabei aber oft dunkler.

Soll das Rendering den gemalten Farben näher kommen, lässt sich das sowohl auf nicht physikalisch basierte als auch auf physikalisch basierte Weise lösen:

Ohne PBR:
* `Den Modus „Unbeleuchtet“ im Menü Shading verwenden`. Die Farben werden genau so angezeigt, wie sie gemalt wurden, dafür geht aber jegliches Shading verloren. Praktisch für schnelle Kontrollen und grafischere Ergebnisse.
* `Den Modus „MatCap“ im Menü Shading verwenden`. Wählen Sie ein helleres, überwiegend weißes MatCap ohne Farbstich.

Mit PBR:
* `Eine neutrale Umgebung verwenden`. Sie können [die Umgebung](shading.md#environment) gegen eine neutralere austauschen. Meiden Sie Innenraum-Umgebungen, da sie meist farbiger sind. Besser eignen sich eine Außenumgebung bei Tageslicht oder eine Studio-Umgebung.
* `Die Beleuchtung verstärken`. Würden Sie ein weißes Blatt Papier in einem dunklen Raum fotografieren, würden Sie einfach mehr Licht hinzufügen. Erhöhen Sie beim Umgebungslicht den Regler Belichtung, bis die Farben für Sie stimmig wirken, oder fügen Sie weitere einzelne Lichter mit höherer Stärke hinzu.
* `Die Belichtung der Kamera erhöhen`. Gäbe es im dunklen Raum keine zusätzlichen Lichter, könnten Sie den Verschluss der Kamera länger offen lassen oder einen empfindlicheren ISO-Wert nutzen. In Nomad erreichen Sie Ähnliches mit der Nachbearbeitung. Öffnen Sie die Nachbearbeitung, aktivieren Sie sie, gehen Sie nach unten zu Tone-Mapping, aktivieren Sie es und erhöhen Sie den Regler Belichtung, bis die Farben stimmen.
* `Leuchtende Farbe verwenden`. Im Menü Material können Sie unter den Texturen „Leuchten“ aktivieren, damit ein Objekt wie eine Lichtquelle wirkt. Schalten Sie in den Einstellungen der Nachbearbeitung die globale Illumination ein, wirft es Licht auf andere Objekte der Szene. Sie können für dieses Material auch „Immer unbeleuchtet“ aktivieren, was ohne Textur ein ähnliches Ergebnis erzielt.

## Abstürze {#crashes}

### Nomad stürzt ab, wenn ich mein Modell speichere oder neu vernetze! {#crash-remesh}
Ihrem Gerät geht der Arbeitsspeicher (RAM) aus.  
Um den Speicherbedarf Ihrer Szene zu senken, können Sie mit einigen Optionen unter [Topologie](topology.md) die Anzahl der Polygone verringern.

::: tip RAM/Speicherplatz
Entscheidend ist die Menge an RAM, nicht der Speicherplatz (der meist viel größer ist).
:::


### Nomad stürzt ab, wenn ich mein Projekt lade! {#crash-load}
Ist die Datei klein, können Sie sie mir schicken, und ich sehe sie mir an (per E-Mail an <support@nomadsculpt.com>).

Andernfalls geht dem Gerät wahrscheinlich der Arbeitsspeicher (RAM) aus.

- Schließen Sie alle anderen geöffneten Apps auf Ihrem Gerät.
- Beginnen Sie in Nomad ein neues Projekt, statt ein Projekt geöffnet zu haben.
- Stürzt es weiterhin ab, bleibt nur, [Ihre Projektdatei](#locate) auf einem Gerät mit mehr Arbeitsspeicher zu laden.

::: tip
Kann Ihr Mobilgerät das Projekt nicht laden, probieren Sie die [Desktop-Version](https://nomadsculpt.com). Im Demo-Modus können Sie damit kostenlos Projekte importieren und exportieren, allerdings stehen nur wenige Bearbeitungswerkzeuge zur Verfügung.

Nutzt Ihr Projekt [Layer](layers.md), sollten Sie sie eventuell zusammenführen, um den Speicherbedarf zu senken.
:::

### Nomad stürzt beim Start ab! {#crash-start}
Stürzt Nomad beim Laden ab, hat es Probleme mit einer bestimmten Datei im Nomad-Ordner.

Meist liegt es daran, dass das Projekt sehr groß ist und leider die RAM-Grenze überschreitet.

Öffnen Sie den [Nomad-Ordner](#locate) und benennen Sie einige Dateien um oder verschieben Sie sie, um den Übeltäter zu finden.

Benennen Sie zuerst `settings.json` um. Dann wird das letzte Projekt nicht mehr geladen.

Hilft das nicht, verschieben Sie einige neuere Dateien aus ihren jeweiligen Ressourcenordnern (`projects`, `matcaps`, `environments` usw.).

Sie können auch die Ordner selbst umbenennen, damit Nomad sie vollständig ignoriert.
Benennen Sie alle Dateien im Nomad-Ordner um oder verschieben Sie sie, entspricht das einer Neuinstallation.

::: tip
Lädt Nomad beim Start eine Datei, verschiebt es diese immer zuerst in den Ordner `can_be_deleted/`.
Ist das Laden erfolgreich, wird sie wieder in ihren ursprünglichen Ordner verschoben.

Stürzt Nomad ab, bevor das Laden abgeschlossen ist, startet es beim nächsten Mal erfolgreich, da es den Ordner `can_be_deleted/` ignoriert.

Sie können einfach versuchen, diese Datei erneut zu laden, wenn Sie glauben, dass es klappen könnte.
:::
