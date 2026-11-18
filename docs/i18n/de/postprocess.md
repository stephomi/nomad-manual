# ![](/icons/postprocess.webp) Nachbearbeitung {#post-process}

Dieses Menü steuert viele Aspekte von Nomad, die das Aussehen des Renderings beeinflussen.

![](/images/postprocess_overview_drac.webp)

Mit der Nachbearbeitung können Sie das endgültige Aussehen Ihrer Szene erheblich verändern.

![](/images/postprocess_overview.webp)
*Dieselbe Szene vor und nach der Nachbearbeitung, ohne zusätzliche Lichter oder Materialänderungen.*

Je nach Gerät kann die Nachbearbeitung die Leistung stark beeinträchtigen.
Mit dem globalen Kontrollkästchen `Nachbearbeitung (Post)` schalten Sie die gesamte Nachbearbeitung aus, sodass Sie schnell zum Sculpten/Modellieren zurückkehren können, ohne Ihre Presets zu verlieren.
Für PBR-Renderings sollten [Ambient Occlusion](#ambient-occlusion-ssao), [Reflexion](#reflection-ssr) und [Tone-Mapping](#tone-mapping) aktiviert sein.

Beim Sculpten werden Sie die Nachbearbeitung aber meist ausschalten wollen, um sich auf die Form selbst statt auf das Rendering zu konzentrieren.


## Qualität {#quality}

![](/images/postprocess_quality.webp)

Diese Optionen verbessern die Qualität des Renderings auf Kosten der Leistung.

### Max. Frame Sampling {#max-frame-sampling}
Nomad berechnet für ein einzelnes Frame nur einen Teil der Nachbearbeitung, was verrauscht aussehen kann. Diese Einstellung legt fest, wie viele Frames gerendert und dann miteinander verrechnet werden, um die meisten Rauschartefakte zu entfernen. Manche Effekte brauchen keine zusätzlichen Samples (z. B. Color-Grading), andere wie weiche Schatten und globale Beleuchtung können Hunderte Samples brauchen, um rauschfrei zu sein.

Im Viewport sehen Sie das immer dann, wenn Sie Nomad nicht bedienen: Die Bildqualität verfeinert sich nach und nach bis zur maximalen Sample-Zahl und hört dann auf. Danach tut Nomad nichts mehr, was Akku spart. Diese Anzahl an Berechnungen wird auch im Render-Bereich des [Dateien-Menüs](files) verwendet, wenn Sie auf „PNG exportieren“ tippen.

Das Kontrollkästchen neben dem Regler schaltet das Frame Sampling ein oder aus.

### Render-Auflösung {#resolution-multiplier}
Dieser Regler steuert die Auflösung des Renderings. Bei x1.0 wird in der Pixelauflösung des Geräts gerendert. Bei x0.5 wird in halber Auflösung gerendert, was schnell geht, aber eine niedrige Qualität ergibt. Ein Wert über 1 rendert in einer größeren Auflösung und skaliert dann herunter. Das ergibt eine höhere Qualität und weniger Rauschen, aber längere Renderzeiten.

Die Einstellung wirkt sich stark auf die Leistung aus, halten Sie sie also möglichst bei x1.25 oder darunter. Dieser Wert wird nicht in den Einstellungen gespeichert, und der Effekt [Pixel-Art](#pixel-art) setzt ihn außer Kraft.

### ![](/icons/intensity.webp) Max. Samples {#max-samples}

Verbessert die Qualität der Nachbearbeitungseffekte auf Kosten der Leistung.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Rastert die Pixel, um Streifenbildung zu verringern (zum Beispiel in Verläufen oder in der Vignette). Normalerweise sollte diese Option aktiviert sein; für bestimmte Vorgänge können Sie sie ausschalten (z. B. beim Export von Tiefenkarten oder anderen datenbezogenen Vorgängen).

### ![](/icons/denoise.webp) Rauschunterdrücker (oidn) {#oidn}

Wendet einen Rauschunterdrücker auf das Bild an, sobald alle Frames verrechnet sind. So kommen Sie mit deutlich weniger Samples aus. Die Rauschunterdrückung belastet den Prozessor stark; aktivieren Sie sie also nur, wenn Ihr Bild verrauscht ist. Sie ist nicht auf jedem Gerät verfügbar.

## Preset-Browser {#preset-browser}
![](/images/postprocess_presets.webp)
Tippen Sie auf das Bild unter dem Titel `Nachbearbeitung (Post)`, um eine Sammlung von Nachbearbeitungs-Presets anzuzeigen. Mit `Neu` erstellen Sie ein Preset aus Ihren aktuellen Einstellungen. Die mitgelieferten Presets können nur geklont werden: Um ein eigenes anzulegen, wählen Sie eines aus, tippen auf `Klonen` und nehmen Ihre Änderungen vor. Hat ein Preset noch nicht gespeicherte Änderungen, zeigt es `Nicht gespeicherte Änderungen!` an. Zum Speichern tippen Sie auf das Preset-Bild, tippen im Preset-Browser erneut darauf und wählen `Speichern`.

## Verknüpfungsleiste {#shortcut-bar}
Ist die Nachbearbeitung aktiviert, listet eine Leiste unten im Menü alle Effekte auf (`SSR`, `SSGI`, `SSAO`, `DoF`, `Leuchten (Bloom)`...). Tippen Sie auf einen, um zu seinem Abschnitt zu springen. Ausgeschaltete Effekte sind ausgegraut, sodass die Leiste auch eine schnelle Übersicht darüber gibt, was das aktuelle Preset bewirkt.

## ![](/icons/postprocess_ssr.webp) Reflexion (SSR) {#reflection-ssr}
Mit dieser Option können Objekte andere Objekte der Szene spiegeln, solange diese auf dem Bildschirm sichtbar sind.
Wenn Sie metallische und glänzende Objekte in Ihrer Szene haben, sollten Sie diese Option wahrscheinlich verwenden.
Sie erfordert den Shading-Modus [PBR](shading.md#pbr).


| SSR aus                    | SSR an                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Globale Illumination (SSGI) {#global-illumination-ssgi}

Die globale Illumination simuliert, wie Licht zwischen Oberflächen hin- und hergeworfen wird: Eine rote Wand wirft zum Beispiel einen roten Schimmer auf ein weißes Objekt in ihrer Nähe. Zusammen mit Ambient Occlusion und Reflexionen kann das den Realismus eines Renderings enorm steigern. Wie die Reflexionen erfordert sie den Shading-Modus [PBR](shading.md#pbr).

`Stärke` - Die Intensität der globalen Illumination.



| SSGI aus                   | SSGI an                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Ein Spotlicht befindet sich hinter der Kugel und ist auf die Decke gerichtet. Ohne SSGI ist nur die Decke beleuchtet. Mit SSGI wird das Licht von der Decke auf die Wände und von dort auf die Kugel geworfen._

## ![](/icons/postprocess_ssao.webp) Ambient Occlusion (SSAO) {#ambient-occlusion-ssao}
Ambient Occlusion dunkelt Bereiche ab, die das Licht weniger gut erreicht (Ecken usw.).
Der Effekt hängt nur von der Geometrie des Modells ab.

* `Stärke` - Intensität des Effekts.
* `Größe` - Wie weit sich der Effekt ausbreitet.
* `Stärke` - Welche Tiefe für verdeckende Objekte angenommen wird, als Prozentsatz der `Größe`.
* `Tönung` - Eine Farbe, die mit der Verdeckung multipliziert wird, für kreative Effekte.


| SSAO aus                    | SSAO an                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO ist vor allem in Bereichen sichtbar, die hauptsächlich vom Umgebungslicht beleuchtet werden. Bereiche unter starkem direktem Licht erhalten einen deutlich schwächeren AO-Effekt.

:::

## ![](/icons/postprocess_dof.webp) Depth Of Field (DoF) {#depth-of-field-dof}
Zeichnet den Bereich außerhalb des Fokus unscharf.

Tippen Sie einfach auf Ihr Modell, um den Fokuspunkt zu ändern.

* `Blendenmodus` - Steuert die Unschärfe über eine einzige Kamerablende statt über die beiden Unschärfe-Regler darunter.
* `Blende` (_nur im Blendenmodus_) - Die Blendenzahl des Objektivs, wie bei einer echten Kamera. Ein niedrigerer Wert öffnet das Objektiv weiter und erzeugt mehr Unschärfe.
* `Ferne Unschärfe` - Wie stark hinter dem Fokuspunkt weichgezeichnet wird.
* `Nahe Unschärfe` - Wie stark zwischen Fokuspunkt und Kamera weichgezeichnet wird.


| DoF aus                   | DoF-Fokus auf hinterem Ring | DoF-Fokus auf vorderem Ring |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Leuchten (Bloom) {#bloom}
Bloom lässt die hellen Bereiche Ihrer Szene leuchten.

* `Stärke` - Stärke des Effekts.
* `Radius` - Die Ausbreitung des Effekts.
* `Schwellenwert` - Wie hell Pixel in der Szene sein müssen, damit sie zu leuchten beginnen. Bei 0 leuchtet alles; bei einem hohen Wert leuchten nur die hellsten Pixel.
* `Tönung` - Eine Farbe, die dem Bloom für kreative Effekte hinzugefügt werden kann.

| Bloom aus                    | Bloom mit Radius 0          | Bloom mit Radius 1          |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Tone-Mapping {#tone-mapping}
Tone-Mapping ist eine Operation, die HDR-Werte auf den Bereich `[0, 1]` umrechnet.
Wenn Sie es nicht verwenden (oder `Nichts` wählen), wird jeder Farbanteil über 1 abgeschnitten.
Alle Farbabstufungen oberhalb dieses Bereichs gehen dann verloren.

* `Nichts/Neutral/Agx/ACES` - welcher Tonemapper verwendet wird. `Nichts` rechnet nichts um (die anderen Regler funktionieren aber weiterhin). Die anderen Optionen sind vergleichbar mit der Wahl verschiedener Filmmaterialien: Sie gehen auf unterschiedliche Weise mit überbelichteten Werten und Farben um. Das ist ein sehr tiefgehendes Thema; suchen Sie nach Tone-Mapping, Agx und ACES, um mehr zu erfahren!
* `Belichtung` - Gesamthelligkeit des Bildes, ähnlich wie das Einstellen der Blende an einer Kamera. So können Sie ein Bild schnell insgesamt aufhellen oder abdunkeln.
* `Sättigung` - Farbintensität. 1 ist neutral, 0 ist einfarbig, Werte über 1 sind zunehmend gesättigt.
* `Kontrast` - Macht Dunkles dunkler und Helles heller. Gehen Sie vorsichtig damit um, denn hohe Werte können Artefakte erzeugen.

Beachten Sie, dass bei deaktiviertem `Tone-Mapping` einige Details verschwinden, weil die Pixel zu hell sind.

| Tone-Mapping aus            | Tone-Mapping an            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone-Mapping kann den Effekt der globalen Illumination verstärken. Wenn Sie die Intensität der Environment-Map verringern und die Hauptlichtquelle verstärken, können Sie die `Belichtung` des Tone-Mappings erhöhen, um mehr vom indirekten Licht zu sehen.
:::

## ![](/icons/postprocess_tone_curve.webp) Color-Grading {#color-grading}
Ähnlich wie das Gradationskurven-Werkzeug in Photoshop steuern Sie hiermit Balance und Verteilung der Farben im Bild. Die Kurve `Luminanz` wirkt auf die gesamte Farbbalance, die Kurven `Rot`/`Grün`/`Blau` erlauben eine Feinabstimmung.

| Color-Grading aus             | Color-Grading an             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Krümmung {#curvature}
Erkennt Stellen, an denen sich die Krümmung schnell ändert, und färbt diese Bereiche ein.

* `Faktor` - Gesamtintensität des Effekts
* `Ausbeulung` - wie stark scharfe konvexe Änderungen erkannt und dort mit der gewählten Farbe versehen werden (standardmäßig weiß)
* `Hohlraum` - wie stark konkave Änderungen erkannt und dort mit der gewählten Farbe versehen werden (standardmäßig schwarz)
* `Stärke` - wie breit die erkannten Kanten sind.

Neben `Ausbeulung` und `Hohlraum` wählen Sie mit einem Farbfeld die Farbe und mit einer kleinen Schaltfläche, wie sich diese Farbe mit dem Bild mischt.


| Krümmung aus                     | Krümmung an                    |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Chromatische Aberration {#chromatic-aberration}
Simuliert den Linsenfehler, bei dem das Licht zu den Bildschirmrändern hin in seine Farben zerlegt wird.

* `Stärke` - wie stark die roten, grünen und blauen Anteile des Bildes zu den Bildschirmrändern hin auseinanderlaufen

| Chromatische Aberration aus   | Chromatische Aberration an   |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vignette {#vignette}
Simuliert den Linseneffekt, bei dem die Bildschirmränder abgedunkelt werden.

* `Größe` - Die Größe einer umgekehrten Ellipse, die über das Bild gelegt wird
* `Ausprägung` - Wie weich oder scharf die Ellipse über das Bild geblendet wird.
* `Tönung` - Die Farbe der Vignette, standardmäßig schwarz.


| Vignette aus                    | Vignette an                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Körnung (Grain) {#grain}
Fügt eine Körnung hinzu, die das Bild etwas weniger künstlich wirken lassen kann.

* `Stärke` - wie viel Körnung bzw. Rauschen dem Bild hinzugefügt wird.


| Körnung aus                  | Körnung an                 |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Schärfe {#sharpness}
Ein Schärfungseffekt, ähnlich wie in Photoshop oder in Fotobearbeitungs-Apps.

* `Stärke` - wie stark das Bild geschärft wird.


| Schärfe aus                    | Schärfe an                   |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel-Art {#pixel-art}
Simuliert die Pixel-Art alter Videospiele. Dieser Effekt setzt die [Render-Auflösung](#resolution-multiplier) außer Kraft.

* `Regler` - Größe der Pixel
* `Frame Sampling zulassen` - wenn Sie viele schwarze Pixel erhalten, schalten Sie diese Option ein. Ohne sie schaltet der Pixel-Art-Effekt das [Frame Sampling](#max-frame-sampling) aus.

| Pixel-Art aus               | Pixel-Art an               |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Bildzeilen {#scanline}
Simuliert das Aussehen alter Röhrenmonitore.

* `Faktor` - Stärke der Linien
* `Abstand` - Größe der Linien

| Bildzeilen aus                 | Bildzeilen an                 |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
