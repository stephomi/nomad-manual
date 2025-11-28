# ![](/icons/material.webp) Material {#material}

Dieses Menü ermöglicht es, das Material des aktuellen Objekts zu ändern, Rendereigenschaften des Objekts/Materials zu steuern und Texturen dem Material zuzuweisen.

![](/images/material_overview.webp)

Materialien definieren, wie ein Objekt aussieht, indem sie steuern, wie es auf Licht und andere Objekte reagiert. Das Aussehen eines Objekts wird durch diese Eigenschaften bestimmt:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Kombinationen dieser Eigenschaften können eine große Bandbreite an Ergebnissen erzielen – von fotorealistisch über cartoonhaft bis hin zu experimentell.

Farbe, Rauheit, Metallizität und Deckkraft können bemalt werden, siehe [Vertex Paint options](painting.md) für weitere Informationen.

Materialtyp, Reflektanz, Emissiv/Unlit sind Materialeigenschaften, die unten erklärt werden.

Die Kopieren/Einfügen-Schaltflächen oben in diesem Menü ermöglichen es, Materialien von einem Objekt auf ein anderes zu kopieren.

Beachte, dass der Renderer von Nomad ein Echtzeit-Renderer ist; er ist leistungsfähig, bevorzugt aber für bestimmte Effekte Geschwindigkeit gegenüber Genauigkeit. 

## Materialtypen {#material-types}

![](/images/material_types.webp)

Nomad-Materialtypen sind Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Deckend {#opaque}
Der Standardmodus, der Oberflächen als einfaches Material behandelt, das bemalte Farbe, Rauheit, Metallizität und Deckkraft unterstützt.

### ![](/icons/material_subsurface.webp) Subsurface {#subsurface}
Dieser Modus kann Materialien simulieren, die Licht intern verwischen und streuen, wie Haut, Wachs oder Jade.

Für das beste Ergebnis wechsle in den PBR-Shading-Modus und verwende mindestens ein Richtungs- oder Spot-Licht, idealerweise mit einer gedimmten Umgebung.

`Depth` steuert, wie weit Licht von vorne unter die Oberfläche und dann wieder aus der Vorderseite heraus gestreut wird. Dies hat den Effekt, harte Schatten zu weichzeichnen und Oberflächendetails zu verwischen.

`Translucency` steuert, wie Licht von der Vorder- zur Rückseite einer Form gestreut wird, etwa wie Licht durch die Unterseite eines Blattes oder stark von hinten beleuchtete Ohren scheint. 

### ![](/icons/material_blending.webp) Blending {#blending}

Ähnlich wie Opaque, unterstützt aber den Opacity-Schieberegler, um das Material zwischen fest und transparent zu mischen. Dies ist ein einfacher einzelner Schieberegler für Deckkraft, im Gegensatz zur bemalbaren Deckkraft, die vom Opaque-Material unterstützt wird. 

::: warning
Der Blending-Modus kann bei komplexen oder sich überschneidenden Formen Flackern und Poppen verursachen.
:::

### ![](/icons/material_additive.webp) Additiv {#additive}
Mit diesem Material kannst du dein Mesh halbtransparent machen. Es ist dem Blending-Material ähnlich, aber während Blending sich mit seiner Umgebung mischt, ist Additive immer heller als die Objekte dahinter – gut für helle Effekte wie Lichtstrahlen, Feuer oder Explosionen.

Du kannst einen Opacity-Wert größer als 1 setzen, was bedeutet, dass das Objekt heller wird.  
Das kann nützlich sein, wenn du [bloom](postprocess.md#bloom) und den `threshold parameter` verwenden möchtest, um nur dieses Objekt wie ein emissives Objekt leuchten zu lassen.

Dieser Modus neigt zu weniger Artefakten als [Blending](#blending) (reihenfolgeunabhängige Transparenz).

### ![](/icons/material_refraction.webp) Brechung {#refraction}
Dieser Modus kann verwendet werden, um Glasmaterial zu simulieren. Aufgrund von Echtzeit-Beschränkungen sind Selbstbrechung und mehrschichtige Brechung etwas eingeschränkt.

Die Rauheitsbemalung des Modells beeinflusst, wie unscharf die Brechung ist.
Standardmäßig hat jedes in Nomad erstellte Objekt eine Rauheit von etwa 25 %, daher ist die Brechung nicht perfekt, sondern etwas unscharf.
Du kannst die Schaltfläche `paint glossy` verwenden, um dein Modell mit einer Rauheit und Metallizität von 0 zu übermalen (die Farben werden nicht beeinflusst).

Es gibt zwei verschiedene Rauheiten im Spiel: die eine steuert, wie unscharf die Reflexion auf der Oberfläche ist, und die andere steuert das Innere (Brechung).  
Da es in Nomad jedoch nur einen bemalbaren Rauheitskanal gibt, teilen sich Innen- und Außenrauheit denselben Wert.  
Um unterschiedliche Werte zu erhalten (zum Beispiel einen Lutscher mit scharfer Oberfläche, aber unscharfem Inneren), kannst du die Schieberegler `Surface glossiness` und `Interior roughness` verwenden, um die bemalte Rauheit zu überschreiben.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Macht das Objekt halbtransparent, indem einige Pixel zufällig verworfen werden.

### ![](/icons/material_shadow_catcher.webp) Schattenfänger {#shadow-catcher}

Macht das Objekt unsichtbar und empfängt nur Schatten. Nützlich, um Nomad-Renderings mit anderen Bildern zu kombinieren. 

::: tip

Weitere Informationen zu Transparenz und Blending-Modi findest du unter https://support.fab.com/s/article/Transparency-Opacity

:::

## Steuerungen {#controls}

![](/images/material_controls.webp)

### Immer unbeleuchtet {#always-unlit}
Wenn aktiviert, ignoriert das Objekt PBR und Matcap und zeigt einfach seine Farbbemalung ohne Schattierung an.
Beachte, dass du bei Verwendung von [Additive](#additive) Transparenz direkt durch Malen mit schwarzer Farbe erzeugen kannst.

### Deckkraft {#opacity}
Wie fest oder undurchsichtig ein Objekt erscheint; 100 % ist fest, 0 % ist transparent. Du kannst die Deckkraft auch bemalen, um feinere Kontrolle zu haben.

### Reflektanz {#reflectance}
Steuert die Menge an Reflexion, die das Material für nichtmetallische Materialien erhält. Meistens sollte der Standardwert verwendet werden (dies entspricht den üblichen 4 % reflektiertem Licht im Normalwinkel), kann aber erhöht werden, um Reflexionen und Glanzlichter z. B. in den Augen einer Figur zu verstärken.

### Invertiertes Culling {#inverse-culling}
Kehrt die Normalen einer Oberfläche um. Normalerweise nicht erforderlich, kann aber verwendet werden, wenn ein Modell von innen nach außen erscheint oder – in Kombination mit deaktiviertem `Two sided` – um Innenräume zu erstellen, bei denen die der Kamera nächstgelegene Wand immer ausgeblendet ist.

### Glatte Schattierung {#smooth-shading}
Siehe die [global option](settings.md#smooth-shading).  
Der Wert `Auto` verwendet die globale Option.

### Beidseitig {#two-sided}
Siehe die [global option](settings.md#two-sided).  
Der Wert `Auto` verwendet die globale Option.

### Farbige Rückseite {#coloured-backface}
Siehe die [global option](settings#two-sided).
Der Wert `Auto` verwendet die globale Option.

### Wirft Schatten {#casts-shadows}
Derzeit ist `Auto` dasselbe wie `On`.
Transparente Objekte werfen ebenfalls Schatten (in einem Dithering-Muster, um gemischte Schatten zu emulieren).  
Stelle sicher, dass du das Werfen von Schatten deaktivierst, wenn du ein großes Objekt in deiner Szene hast, das keine Schatten werfen muss (zum Beispiel einen großen Boden).

### Empfängt Schatten {#recieve-shadows}
Derzeit ist `Auto` dasselbe wie `On`.

### Drahtgitter {#wireframe}
Siehe die [global option](settings.md#wireframe).  
Der Wert `Auto` verwendet die globale Option.


## Texturen {#textures}

![](/images/material_textures.webp)

Wenn ein Objekt UVs hat, können dem Material zusätzlich zur Vertex-Farbe/Rauheit/Metallizität/Deckkraft Texturen zugewiesen werden. Üblicherweise sind dies die Ergebnisse eines Texture-Bakes, aber auch außerhalb von Nomad erstellte Bilder können verwendet werden.

Texturen können angewendet werden auf

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Ein Klick auf einen Textur-Slot öffnet einen Auswahldialog. Nachdem eine Textur einem Material-Slot zugewiesen wurde, öffnet ein weiterer Klick ein Textur-Panel:

### Optionen des Texturfensters {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Öffnen {#open}
Eine andere Textur auswählen

### Keine {#none}
Die Textur entfernen

### Deckkraft {#texture-opacity}

Wenn das Bild einen Alphakanal hat, kannst du damit steuern, ob dieser für die Deckkraft verwendet oder ignoriert wird.

### ![](/icons/link.webp) Ketten/Verknüpfungssymbol {#chainlink-icon}

Das Link-Symbol in den folgenden Abschnitten bedeutet, dass – wenn es aktiviert ist – die verwendeten Optionen mit den anderen Texturen (Color, Normal, Roughness, Metalness, Opacity, Emissive) geteilt werden, deren Link-Symbol ebenfalls aktiviert ist. 

So kannst du sicherstellen, dass ausgerichtete Texturen auch dann ausgerichtet bleiben, wenn du Parameter oder Projektionstypen änderst.


### Projektion {#projection}
![](/images/material_projection.webp)

Legt fest, wie die Textur auf das Objekt angewendet werden soll.

* `Auto` - Wenn das Objekt UVs hat, UV, andernfalls Triplanar
* `UV` - Verwendet die UV-Koordinaten des Meshes, um die Textur anzuwenden. Wenn Mesh und Textur von außerhalb von Nomad stammen oder aus Nomad exportiert werden sollen, um anderswo verwendet zu werden, ist UV die richtige Option.
* `Triplanar` - Projiziert die Textur entlang der X-, Y- und Z-Achse und mischt die Nähte. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanare Projektionen sind eine leistungsstarke und dennoch einfache Methode, Texturen auf Objekte anzuwenden.

Triplanar ist, als hättest du 6 Videoprojektoren mit demselben Bild, die auf die Vorder-, Rück-, Links-, Rechts-, Ober- und Unterseite deines Objekts scheinen.

Dies kann bei Bedarf in UVs oder Vertex-Farben gebacken werden.


![](/images/material_triplanar_example.webp)

#### Methode {#method}

* `Local` - Die Projektion bewegt sich mit der Objekttransformation
* `World` - Die Projektion bleibt fixiert, das Bewegen des Objekts schiebt es durch die Projektion.

#### Härte {#hardness}

Wie die Projektionen sich mischen. 100 % bedeutet kein Blending, und die Kanten der Projektionen sind scharf. 0 % mischt die Kanten über einen weiten Winkel. Der Standardwert ist 90 %, genug Mischung, um die Kanten zu verbergen und den Rest der Projektionen scharf zu lassen.

### Gleichmäßig {#uniform}

Wenn aktiviert, wird dieselbe Hardness für alle Projektionen verwendet. Wenn deaktiviert, werden zusätzliche Hardness-Regler für die X-, Y- und Z-Projektionen angezeigt.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filterung {#filtering}
Die zu verwendende Texturfilter-Methode, `Auto` ist der Standard. Methoden sind `Nearest`, `Linear`, `Mipmap`. Nearest führt kein Filtering durch, sodass Texturen aus der Nähe gezackte Artefakte bekommen können. Linear und Mipmap bieten besseres Filtering, sodass Texturen aus der Nähe eher weichgezeichnet als gezackt erscheinen.

#### Kachelung-X {#tiling-x}
Wenn der Scale-Parameter größer als 1 ist und die Textur dadurch kleiner als die Objekt-UVs wird, legt dies fest, wie die Textur entlang der X-Achse gekachelt wird. `None` bedeutet keine Wiederholungen. `Repeat` erstellt Kopien der Textur. `Mirror` erstellt Kopien der Textur, wobei jede zweite Kopie gespiegelt wird, was helfen kann, Kachel-Artefakte zu verbergen.

#### Kachelung-Y {#tiling-y}
Dasselbe wie Tiling-X, aber für die Y-Achse.

### Transformieren {#transform}
![](/images/material_transform.webp)

Zusätzliche 2D-Transformationen, die in UV-Raum auf die Textur angewendet werden. Die Reset-Schaltfläche setzt auf Standardwerte zurück, das Kettensymbol (wenn andere Texturen als Color ausgewählt sind) verknüpft oder entkoppelt die Transformation, sodass sie mit der Color-Textur übereinstimmt.

#### Verschiebung {#translation}
Der X- und Y-Versatz der Textur

#### Drehung {#rotation}
Die Rotation der Textur

#### Skalierung {#scale}
Die Skalierung der Textur; größere Zahlen machen die Textur auf dem Objekt kleiner. Verwende die Schieberegler Tiling-X und Tiling-Y, um zu steuern, was passiert.

### Gleichmäßige Skalierung {#uniform-scale}
Wenn deaktiviert, zeigt Nomad separate Regler für Scale-X und Scale-Y an.