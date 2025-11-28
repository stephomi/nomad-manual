# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Plattform {#platform}
### Wo befinden sich meine Projekte auf meinem Gerät? {#locate}
Die Projekte befinden sich im Ordner `projects` innerhalb des Hauptordners von Nomad.

Unter iOS kannst du mit der iOS‑Dateien‑App auf den Nomad‑Ordner zugreifen.

Unter Android befindet sich der Nomad‑Ordner in `Android/data/com.stephaneginier.nomad/files/`.  
Unter den neueren Android‑Versionen (10/11) hast du keinen Zugriff mehr auf den Ordner `Android/data`.
Du kannst über eine separate App darauf zugreifen, zum Beispiel [diese hier](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Gibt es eine Möglichkeit, die Beta zu testen? {#beta}
Für Windows & MacOS ist eventuell eine Beta auf der [Homepage](https://nomadsculpt.com) verfügbar.
<br>
Für iOS gibt es ein privates TestFlight, besuche den [Discord](https://discord.com/invite/8h7BwpRz29) im Kanal #beta-ios.
<br>
Die [Web‑Demo](https://nomadsculpt.com/demo) wird in der Regel mit den neuesten Funktionen aktualisiert.

### Warum gibt es auf Android eine kostenlose Testversion, aber nicht auf iOS? {#android-trial}
Weil alte Android‑Geräte schlecht sind (und einige neue auch …), und ich nicht wollte, dass Leute die App kaufen und dann nur einen schwarzen Bildschirm sehen.
Der Hauptgrund ist aber, dass kostenpflichtige Android‑Apps meiner Meinung nach nicht wirklich die Norm sind.

### Welches ist das beste Tablet, um Nomad auszuführen? {#best-tablet}

Kurzfassung: Ein iPad.

Die etwas längere Antwort ist: 

> „Das neueste iPad, _das du dir leisten kannst_, außer du hasst Apple wirklich, dann das neueste Samsung‑Tablet, das du dir leisten kannst. Alles andere: erst testen.“ 

Viele wollen mehr Informationen, daher hier eine Zusammenfassung.

Nomad läuft am besten auf neueren iPads:

* iPads und iPhones können auf das [Quad Remesher](tools#quad-remesher)‑Plugin von [Exoside](https://exoside.com/) zugreifen.
* Neuere iPads mit dem aktuellen Pencil unterstützen [Barrel Roll](https://www.youtube.com/watch?v=XcDQazDYpo0), du kannst den Stift in bestimmten Nomad‑Werkzeugen drehen.
* Die Leistung der neuesten M‑Serie‑Chips ist sehr hoch. 

Das neueste, teuerste verfügbare iPad kann finale Bilder sehr schnell rendern und erlaubt dir, mit sehr vielen Details zu sculpten.

Der Leistungsabfall bei günstigeren und älteren iPads ist jedoch nicht so stark, wie viele erwarten. Jedes iPad, das einen Apple Pencil unterstützt, führt Nomad recht gut aus. Zum Beispiel:

* Ein iPad Pro von 2023 kann 5‑Millionen‑Poly‑Sculpts flüssig handhaben, ein finales Bild rendert in 5 Sekunden.
* Ein iPad Pro von 2015 kann ein Objekt mit 1,2 Millionen Polygonen mit etwas Verzögerung handhaben, ein finales Bild rendert in 20 Sekunden.

Das ist ein großer Leistungsunterschied, aber du musst auch den Preis berücksichtigen:

* Das iPad Pro 2025 kostet *2500 USD* neu mit allen Optionen. 
* Das iPad Pro 2023 kostet derzeit *400 USD* auf eBay.
* Das iPad Pro 2015 kostet *250 USD* auf eBay.

Sind zusätzliche 4 Millionen Polys und 15 gesparte Sekunden 2100 Dollar wert? Das musst du entscheiden.

Nicht‑Pro‑Modelle können noch günstiger sein und bieten eine große Auswahl an Größen und Leistungen. Das aktuelle iPad Air unterstützt den Pencil der 2. Generation mit Barrel Roll und ist deutlich günstiger als das Pro. Der Gebraucht‑ und Refurbished‑Markt bietet noch mehr Optionen. 

Das bedeutet: Egal welches Budget du hast, du solltest ein passendes iPad finden können. Und denk daran, dass die meisten Sculpts keine Millionen von Polys haben! Wenn du unter 500.000 Polys bleibst, kannst du selbst auf alten iPads schnell sculpten.

`Wie sieht es mit Android aus?`

Die Grafikleistung von Android liegt unter der von iPads. Laut dem Entwickler von Nomad „läuft Nomad auf einem Samsung Galaxy Tab S9 um eine Größenordnung langsamer als auf einem iPad Air“. Trotzdem sind viele Nutzer mit ihren Samsung‑Tablets sehr zufrieden, Nomad läuft für die meisten Sculpting‑Aufgaben gut. 

Bei anderen Android‑Tablets ist Vorsicht geboten. Die Leistung der Android‑Hardware kann stark variieren, es ist schwer vorherzusagen, wie gut Nomad laufen wird.

Bitte nutze zuerst die kostenlose Version von Nomad ohne Speicherfunktion zum Testen. 

`Wie sieht es mit Speicher und Speicherplatz aus?`

Die meisten Nomad‑Dateien sind 100 MB oder kleiner. Das bedeutet, dass praktisch jedes aktuelle Tablet, egal ob iPad oder Android, genügend Platz für deine Nomad‑Projekte hat.


### Ich habe Nomad für ein Gerät gekauft, kann ich es auf einem anderen Gerät verwenden? {#multi-devices}
Solange derselbe App‑Store und dasselbe Konto verwendet werden, ja.

Wenn du es zum Beispiel im iOS‑App‑Store gekauft hast, kannst du es auf deinen anderen iOS‑Geräten nutzen.

Wenn du es für dein Android‑Tablet bei Google Play gekauft hast, kannst du es auf deinen anderen Android‑Geräten nutzen.

Wenn du Nomad jedoch auf Android gekauft hast und dir dann ein iPad zulegst, musst du es erneut kaufen.

Das liegt daran, dass Nomad keinen eigenen Lizenzserver oder ein Abomodell hat. Es gibt keine Vereinbarung zwischen Apple/Google/AppGallery zur gemeinsamen Lizenzverwaltung. 


### Wie stelle ich meinen Kauf wieder her? {#restore}
Google Play und AppGallery synchronisieren automatisch.

- Gehe ins About‑Menü (Nomad‑Icon oben links) und tippe auf `restore purchase`
- Überprüfe, ob du mit demselben Konto angemeldet bist, mit dem du Nomad gekauft hast (bei Google Play).
- Starte das Gerät neu
- Manchmal musst du ein paar Stunden warten
- Stelle sicher, dass die Google‑Play‑App auf dem neuesten Stand ist
- Installiere Nomad neu (denk daran, vorher [deine Dateien zu sichern](#where-are-my-projects-located-on-my-device), wenn du nichts verlieren willst)
- Du kannst versuchen, erneut zu kaufen, um zu sehen, was passiert (Hinweis: Du kannst denselben Artikel nicht zweimal mit demselben Konto kaufen)

:::tip
Du kannst mich unter <support@nomadsculpt.com> kontaktieren, aber das *Einzige*, was ich tun kann, ist zu bestätigen, ob zu einer E‑Mail ein Kauf gehört.

Ich erhalte regelmäßig Berichte, dass Lizenzen nach dem Kauf eines neuen Geräts nicht korrekt aktualisiert werden.
Ich habe keinerlei Kontrolle über Zahlung und Kontosynchronisation, das wird komplett von Google/AppGallery gehandhabt!

Letztlich wird der Kauf immer wiederhergestellt, aber die nötigen Schritte zur Beschleunigung des Prozesses sind unklar.
:::

::: warning
Neuere Huawei‑Geräte haben keinen Zugriff auf Google‑Dienste.
In diesem Fall musst du die App erneut in der AppGallery (Huawei‑App‑Store) kaufen.
:::

### Können Sie [meine-Sprache] übersetzen oder korrigieren? {#locale}
Ich kann relativ einfach eine weitere Sprache hinzufügen, aber ich verlasse mich auf KI‑Übersetzung, da dies für regelmäßige Updates viel einfacher zu handhaben ist.
Die Übersetzungsdateien findest du [hier](https://github.com/stephomi/nomad-translation).

## Funktionen {#features}

### Warum bewegt sich das Gizmo nicht? {#gizmo-not-moving}
Möglicherweise hast du [Pin in der linken Menü‑Toolbar](tools#left-menu-toolbar) aktiviert. 

### Können wir in Nomad animieren? {#animate}
Im Moment nicht. Eine Timeline‑Funktion, mit der sich Ebenen animieren lassen, wäre interessant, ist aber derzeit nicht wirklich geplant.  

Ich würde in Zukunft gerne Rigging/Skinning unterstützen, aber das bringt einige Herausforderungen mit sich (insbesondere die Interaktion mit den Sculpting‑Werkzeugen …), daher ist noch nichts sicher.


### Können wir richtiges Low-Poly-Modeling machen? {#lowpoly}
Im Moment nicht.
Das gehört nicht wirklich zum Umfang von Nomad *Sculpt*, aber vielleicht werde ich in Zukunft ein paar Werkzeuge dafür bereitstellen.


### Können wir UVs und Texturen erstellen? {#texturing}
Kurz: Ja. Lang: Nicht direkt, aber es gibt mehrere Möglichkeiten, Nomads hervorragende Vertex‑Paint‑Werkzeuge mit UVs und Texturen zu kombinieren.

* Nomad erlaubt dir, Farbe, Rauheit und Materialeigenschaften direkt in die Vertices deines Sculpts zu malen.
* Nomad erlaubt sehr hohe Vertex‑Anzahlen, sodass du malen kannst, ohne dir Gedanken über UVs zu machen.
* Nomad kann Texturen in Pinseln laden, sodass du mit Texturen stempeln und malen kannst.
* Nomad kann Objekte laden, denen bereits Texturen zugewiesen sind, zum Rendern.
* Nomad kann Low‑Poly‑Objekte [UV‑unwrappen](topology.md#uv-unwrap).
* Farbe/Rauheit/Metallizität können über [die Projektoptionen](topology.md#reproject-to-vertex) von Texturen auf Vertices übertragen werden.
* Farbe/Rauheit/Metallizität/Normalen können über [die Bake‑Optionen](topology.md#bake-to-texture) von Vertices auf Texturen gebacken werden.
* Baking und Projektion können zwischen einzelnen Objekten oder vielen Objekten erfolgen oder zwischen der höchsten und niedrigsten Unterteilungsstufe eines einzelnen Objekts, was verschiedene Bake‑ und Projekt‑Workflows ermöglicht.
* Nach dem Backen exportiert ein OBJ‑Export auch die Texturen, die du dann in eine App wie Procreate bringen kannst, um direkt auf Texturen zu malen.

### Kann ich ein Turntable-Video aufnehmen? {#video}
Derzeit nicht geplant, iOS hat eine [Videoaufnahme‑Funktion](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados), die sehr einfach zu benutzen ist.

Unter iOS wischst du von oben links nach unten und tippst auf den Aufnahme‑Button. Es gibt einen 3‑Sekunden‑Countdown, wische das Menü weg, um Nomad anzuzeigen, und nutze die Turntable‑Funktion. Wenn du fertig bist, wische erneut von oben rechts nach unten und tippe wieder auf den Aufnahme‑Button. Bearbeite den Film in der Fotomediathek, um überflüssiges Material am Anfang und Ende zu entfernen.

### Können Sie [Lieblingsfunktion-einfügen] als Schaltfläche auf oberster Ebene hinzufügen? {#interface}
Ja, die untere Toolbar kann jetzt über das [Interface](interface.md)‑Menü angepasst werden, und schwebende Toolbars können erstellt werden.

### Was sind die nächsten Funktionen? {#next-features}
Für die mittlere/lange Roadmap habe ich viele Ideen, aber ich weiß es noch nicht genau.  

Bugfixes und die Verbesserung bestehender Funktionen haben immer höhere Priorität als neue Funktionen.


### Können wir in Nomad riggen? {#rigging}
Nein, aber es ist geplant. Im Moment kannst du Formen miteinander verknüpfen (parenten) und Pivot‑Punkte verändern, was einfache posierbare Sculpts ermöglicht.

### Können wir mehr als 4 Lichter verwenden? {#lights}
Nein, das ist eine Einschränkung der Echtzeit‑Render‑Engine in Nomad. Man kann dies mit Emissive‑Objekten und Global Illumination im Post‑Processing faken, wie in [diesem Tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA) gezeigt.

### Können wir ZBrush-Tools importieren? {#zbrush-import}
Nein, ZBrush verwendet ein proprietäres Format. Du solltest jedoch die Alpha‑Maps extrahieren und in Nomad verwenden können. 

### Warum stimmen die Farben nicht mit dem überein, was ich gemalt habe? Warum bekomme ich im Render kein Weiß? {#paint-pbr}
Stell dir ein Foto von einem Blatt Papier, einem Schreibtischlampe und der Sonne vor. Ältere Kameras und Bildschirme machen daraus einfach alle „weiß“. Moderne Systeme können den Unterschied zwischen reflektiertem Weiß des Papiers, emittiertem Licht der Lampe und dem extrem hellen Licht der Sonne darstellen.

Moderne Computergrafik versucht ähnlich zu arbeiten, indem sie die Physik von Licht und Oberflächen emuliert. Das nennt sich `Physically Based Rendering` oder PBR, und Nomads PBR‑Renderer basiert darauf. Das sieht realistisch und ausgewogen aus, aber oft wirken kräftig gemalte Farben dunkler.

Wenn der Render näher an den gemalten Farben liegen soll, kannst du das sowohl auf nicht‑physikalische als auch physikalisch basierte Weise anpassen:

Nicht PBR:
* `Verwende den „Unlit“-Modus im Beleuchtungsmenü`. Farben werden exakt so angezeigt, wie sie gemalt wurden, aber du verlierst jegliche Schattierung. Praktisch für schnelle Kontrollen und grafischere Ausgaben.
* `Verwende den „Matcap“-Modus im Beleuchtungsmenü`. Wähle ein helleres Matcap, das überwiegend weiß ist und keinen Farbstich hat.

PBR:
* `Verwende eine neutrale Umgebung`. Du kannst [die Umgebung](shading.md#environment) auf eine neutralere ändern. Vermeide Innenraum‑Umgebungen, da sie meist stärker eingefärbt sind. Bevorzuge stattdessen Tageslicht‑Außen‑ oder Studio‑Umgebungen.
* `Erhöhe die Beleuchtung`. Wenn du ein Foto von weißem Papier in einem dunklen Raum machst, würdest du einfach mehr Licht hinzufügen. Erhöhe bei der Umgebungsbeleuchtung den Exposure‑Regler, bis die Farben für dich richtig wirken, oder füge weitere Lichter mit höherer Intensität hinzu.
* `Erhöhe die Kamera‑Belichtung`. Wenn es im dunklen Raum keine zusätzlichen Lichter gäbe, könntest du die Kamera länger belichten oder eine höhere ISO verwenden. In Nomad erreichst du ein ähnliches Ergebnis über Post‑Processing. Gehe zu Post Process, aktiviere es, scrolle zu Tone Mapping, aktiviere es und erhöhe den Exposure‑Regler, bis die Farben für dich stimmen.
* `Verwende Emissive Color`. Im Materialmenü kannst du unter Textures „emissive“ aktivieren, wodurch ein Objekt wie eine Lichtquelle erscheint. Wenn du in den Post‑Processing‑Einstellungen Global Illumination aktivierst, wirft es Licht auf andere Objekte in der Szene. Du kannst auch „unlit“ für dieses Material aktivieren, was einen ähnlichen Look ohne Textur erzielt.

## Abstürze {#crashes}

### Es stürzt ab, wenn ich mein Modell speichere oder remeshe! {#crash-remesh}
Dein Gerät geht der Speicher (RAM) aus.  
Um die Speichernutzung in deiner Szene zu reduzieren, kannst du einige der [Topologie](topology.md)‑Optionen verwenden, um die Polygonanzahl zu verringern.

::: tip RAM/Speicherplatz
Wichtig ist die Menge an RAM, nicht der Speicherplatz (der in der Regel viel größer ist).
:::


### Es stürzt ab, wenn ich mein Projekt lade! {#crash-load}
Wenn die Datei klein ist, kannst du sie mir schicken und ich schaue sie mir an (per E‑Mail <support@nomadsculpt.com>).

Andernfalls geht dem Gerät wahrscheinlich der RAM‑Speicher aus.

- Schließe alle anderen geöffneten Apps auf deinem Gerät.
- Starte ein neues Projekt in Nomad, anstatt ein Projekt bereits geöffnet zu haben.
- Wenn es immer noch abstürzt, ist die einzige Lösung, [deine Projektdatei](#where-are-my-projects-located-on-my-device) auf einem Gerät mit mehr Speicher zu laden.

::: tip
In einem Desktop‑Browser kannst du versuchen, deine Datei [unter dieser URL](https://nomadsculpt.com/demo_save/) zu laden und sie nach dem Vereinfachen deiner Szene wieder zu exportieren.

Einige Browser begrenzen die Menge an RAM, die ein einzelner Tab verwenden darf, daher ist es möglich, dass diese Technik nicht funktioniert.

Wenn dein Projekt [Ebenen](layers.md) verwendet, solltest du sie eventuell zusammenführen, um den Speicherverbrauch zu reduzieren.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Es stürzt ab, wenn ich Nomad starte! {#crash-start}
Wenn es beim Laden abstürzt, bedeutet das, dass Nomad mit einer bestimmten Datei im Nomad‑Ordner Probleme hat.

Meistens passiert das, weil das Projekt sehr groß ist und leider das RAM‑Limit überschreitet.

Suche den [Nomad‑Ordner](#where-are-my-projects-located-on-my-device) und benenne dann einige Dateien um oder verschiebe sie, um den Übeltäter zu finden.

Versuche zuerst, `settings.json` umzubenennen. Dadurch wird das zuletzt geladene Projekt nicht mehr geöffnet.

Wenn das nicht hilft, verschiebe einige der zuletzt verwendeten Dateien aus ihren jeweiligen Ressourcenordnern (`projects`, `matcaps`, `environments` usw.) heraus.

Du kannst auch die Ordner selbst umbenennen, damit Nomad sie komplett ignoriert.
Wenn du alle Dateien im Nomad‑Ordner umbenennst oder verschiebst, entspricht das einer Neuinstallation.

::: tip
Wenn Nomad beim Start eine Datei lädt, verschiebt es die Datei immer in den Ordner `can_be_deleted/`.
Wenn der Vorgang erfolgreich ist, wird sie wieder in ihren ursprünglichen Ordner zurückverschoben.

Wenn es abstürzt, bevor das Laden abgeschlossen ist, startet Nomad beim nächsten Mal erfolgreich, da der Ordner `can_be_deleted/` ignoriert wird.

Du kannst einfach versuchen, diese Datei erneut zu laden, wenn du glaubst, dass es diesmal klappen könnte.
:::