# ![](/icons/material.webp) Material {#material}

In diesem Menü ändern Sie das Material des aktuellen Objekts und die Render-Eigenschaften von Objekt und Material und weisen dem Material Texturen zu.

![](/images/material_overview.webp)

Materialien bestimmen, wie ein Objekt aussieht, indem sie steuern, wie es auf Licht und auf andere Objekte reagiert. Das Aussehen eines Objekts wird durch diese Eigenschaften gesteuert:

* `Typ`
* `Farbe`
* `Matt`
* `Metallisch`
* `Deckkraft`
* `Reflexionsgrad`
* `Leuchten/Unbeleuchtet`

Durch Kombination dieser Eigenschaften erreichen Sie eine große Bandbreite an Ergebnissen, von fotorealistisch über cartoonhaft bis experimentell.

Farbe, Rauheit, Metallizität und Deckkraft lassen sich malen; mehr dazu unter [Optionen für Vertex-Painting](painting.md).

Materialtyp, Reflexionsgrad und Leuchten/Unbeleuchtet sind Materialeigenschaften, die unten erklärt werden.

Mit den Schaltflächen `Kopieren` und `Einfügen` oben in diesem Menü können Sie Materialien von einem Objekt auf ein anderes übertragen.

Beachten Sie, dass Nomad einen Echtzeit-Renderer verwendet: Er ist leistungsstark, setzt bei manchen Effekten aber eher auf Geschwindigkeit als auf Genauigkeit.

## Materialtypen {#material-types}

![](/images/material_types.webp)

Die Materialtypen von Nomad sind Opak, Unter Oberfläche, Überblenden, Additiv, Refraktion, Dithering und Schattenfänger.

### ![](/icons/material_opaque.webp) Opak {#opaque}
Der Standardmodus, der Oberflächen als einfaches Material behandelt und gemalte Farbe, Rauheit, Metallizität und Deckkraft unterstützt. Gemalte Deckkraft, eine Deckkraft-Textur oder der Alphakanal der Farbtextur machen das Objekt trotzdem durchsichtig, und zwar per Dithering. Nur der Hauptregler für die Deckkraft wird ignoriert.

### ![](/icons/material_subsurface.webp) Unter Oberfläche {#subsurface}
Dieser Modus simuliert Materialien, in denen das Licht im Inneren gestreut und weichgezeichnet wird, wie Haut, Wachs oder Jade.

Er erfordert den Shading-Modus PBR. Die besten Ergebnisse erzielen Sie mit mindestens einem Richtungs- oder Spotlicht, idealerweise in einer eher dunklen Umgebung.

Das Farbfeld legt die Farbe des gestreuten Lichts fest.

`Tiefe` steuert, wie weit das Licht von der Vorderseite unter die Oberfläche und dann wieder aus der Vorderseite heraus gestreut wird. Das macht harte Schatten weicher und lässt Oberflächendetails verschwimmen.

`Durchscheinend` steuert, wie das Licht von der Vorderseite zur Rückseite einer Form gestreut wird, etwa wenn Licht durch die Unterseite eines Blatts scheint oder Ohren stark von hinten beleuchtet werden. Um diesen Effekt zu sehen, brauchen Sie ein Licht, das Schatten wirft.

### ![](/icons/material_blending.webp) Überblenden {#blending}

Ähnlich wie Opak, unterstützt aber den Deckkraft-Regler, sodass das Material zwischen massiv und transparent überblenden kann. Hier gibt es einen einfachen Regler für die Deckkraft, während das opake Material malbare Deckkraft unterstützt.

::: warning
Der Modus Überblenden kann bei komplexen oder sich überschneidenden Formen zu Flackern und Springen führen.
:::

### ![](/icons/material_additive.webp) Additiv {#additive}
Mit diesem Material machen Sie Ihr Mesh halbtransparent. Es ähnelt dem Material Überblenden, doch während Überblenden sich mit seiner Umgebung mischt, ist Additiv immer heller als die Objekte dahinter. Gut geeignet für helle Effekte wie Lichtstrahlen, Feuer oder Explosionen.

Sie können einen Deckkraftwert über 1 einstellen, wodurch das Objekt heller wird.  
Das ist nützlich, wenn Sie mit [Leuchten (Bloom)](postprocess.md#bloom) und dem Parameter `Schwellenwert` nur dieses Objekt wie ein leuchtendes Objekt strahlen lassen möchten.

Dieser Modus erzeugt meist weniger Artefakte als [Überblenden](#blending) (reihenfolgeunabhängige Transparenz).

### ![](/icons/material_refraction.webp) Refraktion {#refraction}
Mit diesem Modus simulieren Sie Glas. Er erfordert den Shading-Modus PBR. Wegen der Echtzeit-Beschränkungen sind Selbstbrechung und mehrschichtige Brechung nur eingeschränkt möglich.

Die gemalte Rauheit des Modells beeinflusst, wie unscharf die Brechung ist.
Standardmäßig hat jedes in Nomad erstellte Objekt eine Rauheit von etwa 25 %, daher ist die Brechung nicht perfekt, sondern etwas unscharf.
Mit der Schaltfläche `Glänzend bemalen` übermalen Sie Ihr Modell mit einer Rauheit und Metallizität von 0 (die Farben bleiben unverändert).

Es spielen 2 verschiedene Rauheiten eine Rolle: Die eine bestimmt, wie unscharf die Spiegelung an der Oberfläche ist, die andere das Innere (die Brechung).  
Da es in Nomad aber nur einen gemalten Rauheitskanal gibt, teilen sich innere und äußere Rauheit denselben Wert.  
Um unterschiedliche Werte zu erhalten (zum Beispiel einen Lutscher mit scharfer Oberfläche, aber unscharfem Inneren), überschreiben Sie die gemalte Rauheit mit den Reglern `Oberfläche` und `Innen` unter `Rauheit überschreiben`.

![](/videos/refraction.mp4)

#### Lichtbrechungsindex {#index-of-refraction}
Wie stark das Licht gebrochen wird, wenn es in das Objekt eintritt. Höhere Werte brechen es stärker, wie eine dicke Linse.

#### Absorption {#absorption}
Simuliert, wie das Licht auf seinem Weg durch das Volumen absorbiert wird, eingefärbt durch das Farbfeld; `Faktor` legt die Stärke fest. Dünne Stellen sind heller, weil sie mehr Licht durchlassen, dicke Bereiche dunkler. Es wird nur eine Annäherung an die Dicke des Objekts verwendet, daher hängt der Effekt stark von der Form ab.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Macht das Objekt halbtransparent, indem zufällig einige Pixel verworfen werden.

### ![](/icons/material_shadow_catcher.webp) Schattenfänger {#shadow-catcher}

Macht das Objekt unsichtbar, sodass es nur noch die Schatten von Lichtern empfängt. Nützlich, um Nomad-Renderings mit anderen Bildern zu kombinieren, meist auf einer Ebene. Das Farbfeld legt die Farbe des Schattens fest.

In der Szene muss ein Licht Schatten werfen, sonst bewirkt der Schattenfänger nichts. Die Schaltflächen `Metallisch → 0%` und `Metallisch → 100%` übermalen das Objekt: Vollständig metallisch kann der Schattenfänger auch die Szene spiegeln, wenn die Nachbearbeitung [Reflexion (SSR)](postprocess.md#reflection-ssr) aktiviert ist.

::: tip

Weitere Informationen zu Transparenz und Überblendungsmodi finden Sie unter https://support.fab.com/s/article/Transparency-Opacity

:::

## Steuerelemente {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Immer unbeleuchtet {#always-unlit}
Ist diese Option aktiviert, ignoriert das Objekt PBR und Matcap und zeigt einfach seine gemalte Farbe ohne Schattierung an.
Wenn Sie [Additiv](#additive) verwenden, können Sie Transparenz direkt mit schwarzer Farbe malen.

### Deckkraft {#opacity}
Wie massiv oder deckend ein Objekt erscheint: 100 % ist massiv, 0 % ist transparent. Der Regler wird bei den Typen Überblenden, Additiv, Dithering und Schattenfänger angezeigt. Für eine feinere Kontrolle können Sie die Deckkraft auch malen.

### Pre-Refraction-Pass {#pre-refract-pass}
Nur Überblenden und Additiv. Zeichnet dieses transparente Objekt vor dem Refraktions-Pass. Nützlich, wenn sich ein lichtbrechendes Objekt vor anderen transparenten Oberflächen befindet.

### Reflexionsgrad {#reflectance}
Steuert, wie viel Spiegelung ein nicht-metallisches Material erhält. Meist sollten Sie den Standardwert verwenden (er entspricht den üblichen 4 % reflektierten Lichts bei senkrechtem Einfall), Sie können ihn aber erhöhen, um zum Beispiel Spiegelungen und Glanzlichter in den Augen einer Figur zu verstärken. Erfordert den Shading-Modus PBR.

### ![](/icons/culling.webp) Umgekehrtes Culling {#inverse-culling}
Kehrt die Normalen einer Oberfläche um. Normalerweise nicht nötig, aber hilfreich, wenn ein Modell von innen nach außen gestülpt erscheint. Zusammen mit deaktiviertem `Backface` können Sie damit auch Innenräume darstellen, bei denen die Wand, die der Kamera am nächsten ist, immer ausgeblendet ist.

Die folgenden Optionen lassen sich auf `Auto`, `Nein` oder `Ja` stellen. Bei `Auto` zeigt der Pfeil den Wert, der tatsächlich verwendet wird.

### ![](/icons/sphere_smooth.webp) Smooth Shading {#smooth-shading}
Siehe die [globale Option](settings.md#smooth-shading).  
Der Wert `Auto` verwendet die globale Option.

### ![](/icons/culling.webp) Backface {#two-sided}
Flächen sind von beiden Seiten sichtbar. Siehe die [globale Option](settings.md#two-sided-quick).  
Der Wert `Auto` verwendet die globale Option.

### ![](/icons/culling.webp) Backfaces einfärben {#coloured-backface}
Siehe die [globale Option](settings.md#two-sided-quick).
Der Wert `Auto` verwendet die globale Option.

### ![](/icons/shadow_cast.webp) Wirft Schatten {#casts-shadows}
Auch transparente Objekte werfen Schatten (in einem Dithering-Muster, um überblendete Schatten nachzuahmen).  
Deaktivieren Sie den Schattenwurf unbedingt, wenn sich in Ihrer Szene ein großes Objekt befindet, das keine Schatten werfen muss (zum Beispiel ein großer Boden).

### ![](/icons/shadow_receive.webp) Empfängt Schatten {#recieve-shadows}
Legt fest, ob Schatten anderer Objekte auf diesem Objekt dargestellt werden.

### ![](/icons/wireframe.webp) Drahtgitter {#wireframe}
Siehe die [globale Option](settings.md#wireframe).  
Der Wert `Auto` verwendet die globale Option.

### ![](/icons/trash.webp) Normalen zurücksetzen {#reset-normals}
Wird nur angezeigt, wenn ein importiertes Objekt eigene Normalen mitbringt (zum Beispiel mit `Topologie beibehalten`). Entfernt sie, sodass das Shading die aus der Oberfläche berechneten Normalen verwendet.


## Texturen {#textures}

![](/images/material_textures.webp)

Hat ein Objekt UVs, können Sie dem Material zusätzlich zu Vertex-Farbe/-Rauheit/-Metallizität/-Deckkraft Texturen zuweisen. Meist stammen diese aus einem Textur-Bake, Sie können aber auch außerhalb von Nomad erstellte Bilder verwenden. `UV:✓` oder `UV:✗` neben dem Titel zeigt Ihnen, ob das Objekt UVs hat.

Texturen lassen sich zuweisen für

* Farbe
* Normal
* Rauheit
* Metallizität
* Deckkraft
* Verschiebung
* Leuchten

Eine Zeile `Verdeckung` erscheint außerdem, wenn ein importiertes Objekt eine Occlusion-Textur hat; Nomad verwendet sie aber nicht.

Der Regler jeder Zeile legt fest, wie stark ihre Textur angewendet wird, von gar nicht bis vollständig. `Farbe` und `Leuchten` haben zusätzlich ein Farbfeld, das die Textur einfärbt, und bei `Leuchten` legt es die Leuchtstärke fest.

`Verschiebung` legt fest, wie weit die Displacement-Map die Oberfläche verschiebt. Die Schaltfläche `Anwenden` verschiebt die Vertices um das Displacement und entfernt anschließend die Map. Das Ergebnis landet in der aktiven Ebene.

Die Paletten-Schaltfläche neben dem Titel öffnet die Material-Presets des Menüs [Zeichnen](painting.md): Tippen Sie auf eines, um seine Texturen auf das Objekt zu übertragen. Am Desktop werden importierte Bilder mit ihrer Originaldatei synchronisiert, wenn Sie zu Nomad zurückwechseln, und eine Synchronisierungs-Schaltfläche neben dem Titel lädt sie neu.

Tippen Sie auf einen Textur-Slot, um eine Auswahl zu öffnen. Ist einem Material-Slot bereits eine Textur zugewiesen, öffnet ein erneutes Tippen ein Texturfeld:

### Optionen im Texturfeld {#texture-panel-options}

![](/images/material_texture_panel.webp)

Das Feld zeigt die Bildgröße und eine Vorschau der Textur.

### ![](/icons/open.webp) Öffnen {#open}
Wählt eine andere Textur. Am Desktop zeigt `Durchsuchen` die Bilddatei in Ihrem Dateibrowser an.

### ![](/icons/circle_cross.webp) Keine {#none}
Entfernt die Textur

### Deckkraft {#texture-opacity}

Nur bei der Farbtextur. Hat das Bild einen Alphakanal, können Sie ihn hiermit für die Deckkraft verwenden oder ignorieren.

### Format {#normal-format}
Nur bei der Normal-Textur. Normal-Maps gibt es in zwei Varianten, `OpenGL (+Y)` und `DirectX (-Y)`. Wenn die Details umgekehrt aussehen, probieren Sie die andere.

### Höhe {#displacement-height}
Nur bei der Displacement-Textur.
* `Lokal` - Die Höhe wächst und schrumpft mit der Skalierung des Objekts.
* `Welt` - Die Höhe bleibt gleich, unabhängig von der Skalierung des Objekts.

### Multiplizieren {#multiply}
Nur bei Texturen für Rauheit, Metallizität und Deckkraft. Multipliziert die Werte der Textur. Ist der Wert nicht 100 %, wird er auf dem Textur-Slot angezeigt.

### ![](/icons/link.webp) Ketten-/Verknüpfungs-Icon {#chainlink-icon}

Ist das Verknüpfungs-Icon in den folgenden Abschnitten aktiviert, werden die gewählten Optionen mit den anderen Texturen (Farbe, Normal, Rauheit, Metallizität, Deckkraft, Leuchten) geteilt, deren Verknüpfungs-Icon ebenfalls aktiviert ist.

So stellen Sie sicher, dass aufeinander ausgerichtete Texturen ausgerichtet bleiben, auch wenn Sie Parameter oder Projektionsarten ändern.


### Projektion {#projection}
![](/images/material_projection.webp)

Legt fest, wie die Textur auf das Objekt aufgebracht wird.

* `Auto` - UV, wenn das Objekt UVs hat, sonst Triplanar
* `UV` - Verwendet die UV-Koordinaten des Meshes, um die Textur aufzubringen. Wenn Mesh und Textur von außerhalb von Nomad stammen oder aus Nomad exportiert und anderswo verwendet werden sollen, ist UV die richtige Wahl.
* `Triplanar` - Projiziert die Textur entlang der Achsen X, Y und Z und blendet die Nähte ineinander.

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanare Projektionen sind eine leistungsstarke und zugleich einfache Methode, Objekte zu texturieren.

Triplanar ist, als hätten Sie 6 Videoprojektoren mit demselben Bild, die von vorne, hinten, links, rechts, oben und unten auf Ihr Objekt strahlen.

Das Ergebnis lässt sich bei Bedarf anschließend in UVs oder Vertex-Farben einbacken.


![](/images/material_triplanar_example.webp)

#### Methode {#method}

* `Lokal` - Die Projektion bewegt sich mit der Transformation des Objekts
* `Welt` - Die Projektionen bleiben fest; bewegen Sie das Objekt, gleitet es durch die Projektion.

#### Ausprägung {#hardness}

Wie sich die Projektionen mischen. Bei 100 % wird nicht überblendet, und die Ränder der Projektionen sind scharf. Bei 0 % werden die Ränder über einen weiten Winkel überblendet. Der Standardwert ist 90 %: genug Überblendung, um die Ränder zu verbergen, während der Rest der Projektionen scharf bleibt.

### Einheitlich {#uniform}

Ist diese Option angehakt, gilt dieselbe Ausprägung für alle Projektionen. Ist sie nicht angehakt, erscheinen zusätzliche Regler für die Ausprägung der Projektionen X, Y und Z.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filterung {#filtering}
Die Filtermethode für die Textur. Standard ist `Auto`, die Methoden sind `Nächster`, `Linear` und `Mipmap`. Nächster filtert nicht, daher können Texturen aus der Nähe betrachtet gezackte Artefakte zeigen. Linear und Mipmap filtern besser, sodass Texturen aus der Nähe eher unscharf als gezackt wirken.

#### Kacheln - X {#tiling-x}
Wenn der Skalierungsparameter größer als 1 ist und die Textur damit kleiner als die UVs des Objekts wird: wie die Textur entlang der X-Achse gekachelt wird. `Kein` bedeutet keine Wiederholung. `Wiederholen` erzeugt Kopien der Textur. `Spiegeln` erzeugt Kopien der Textur, wobei jede zweite Kopie gespiegelt ist; das kann helfen, Kachel-Artefakte zu verbergen.

#### Kacheln - Y {#tiling-y}
Wie Kacheln - X, aber für die Y-Achse.

### Transformieren {#transform}
![](/images/material_transform.webp)

Zusätzliche 2d-Transformationen, die im UV-Raum auf die Textur angewendet werden. Die Schaltfläche zum Zurücksetzen stellt die Standardwerte wieder her. Das Ketten-Icon (wenn andere Texturen als die Farbtextur ausgewählt sind) verknüpft die Transformation mit der der Farbtextur oder hebt die Verknüpfung auf.

#### Verschiebung {#translation}
Der Versatz der Textur auf X und Y

#### Rotation {#rotation}
Die Drehung der Textur

#### Skalierung {#scale}
Die Skalierung der Textur. Größere Werte machen die Textur auf dem Objekt kleiner; mit den Optionen Kacheln - X und Kacheln - Y steuern Sie, was dann passiert.

### Gleichmäßige Skalierung {#uniform-scale}
Ist diese Option ausgeschaltet, zeigt Nomad getrennte Regler für Skalierung X und Skalierung Y.
