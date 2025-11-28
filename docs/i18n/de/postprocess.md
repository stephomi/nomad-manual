# ![](/icons/postprocess.webp) Nachbearbeitung {#post-process}

Dieses Menü steuert viele Aspekte von Nomad, die das Aussehen des Renderings beeinflussen.

![](/images/postprocess_overview_drac.webp)

Die Verwendung der Nachbearbeitung kann das endgültige Aussehen deiner Szene erheblich verändern.

![](/images/postprocess_overview.webp)
*Dieselbe Szene vor und nach der Nachbearbeitung, ohne zusätzliche Lichter oder Materialänderungen.*

Die Nachbearbeitung kann die Leistung je nach Gerät stark beeinflussen.
Es gibt ein globales Kontrollkästchen, um die gesamte Nachbearbeitung zu deaktivieren, sodass du schnell zum Sculpting/Modellieren zurückkehren kannst, ohne deine Voreinstellungen zu verlieren.
Für PBR-Rendering sollten [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) und [Tone Mapping](#tone-mapping) aktiviert sein.

In den meisten Fällen möchtest du die Nachbearbeitung beim Sculpting deaktiviert haben, um dich auf die Form des Renderings selbst zu konzentrieren.


## Qualität {#quality}

![](/images/postprocess_quality.webp)
### Maximale Frame‑Abtastung {#max-frame-sampling}
Nomad berechnet eine bestimmte Menge an Nachbearbeitung für ein einzelnes Frame-Rendering, was körnig aussehen kann. Diese Einstellung bestimmt, wie viele Frames gerendert und anschließend miteinander verrechnet werden, um die meisten Rausch-Artefakte zu entfernen. Einige Effekte benötigen keine zusätzlichen Samples (z. B. Color Grading), während andere wie Global Illumination Hunderte von Samples benötigen können, um rauschfrei zu sein. 

Im Viewport ist dies zu sehen, wenn Nomad in Ruhe gelassen wird: Die Bildqualität verfeinert sich nach und nach bis zur maximalen Sample-Anzahl und stoppt dann. Diese Anzahl an Berechnungen wird auch im Render-Bereich des [Datei-Menüs](files) verwendet, wenn „export png“ angeklickt wird.

### Auflösungs‑Multiplikator {#resolution-multiplier}
Dieser Regler steuert die Auflösung der Nachbearbeitung. Ein Wert von x1.0 bedeutet, dass das Rendering in der Pixelauflösung des Geräts erfolgt. Ein Wert von x0.5 rendert in halber Auflösung, was schnell, aber von geringerer Qualität ist. Ein Wert größer als 1 rendert in höherer Auflösung und skaliert dann herunter. Das führt zu höherer Qualität, weniger Rauschen, aber längeren Renderzeiten.

### Maximale Samples {#max-samples}

Dies erhöht die Qualität der Nachbearbeitung, aber im Allgemeinen hat `Full resolution` mehr Einfluss. 

### Denoiser (oidn) {#oidn}

Wendet einen Denoiser auf das Bild an. Dadurch kannst du deutlich weniger Samples verwenden. Dies funktioniert nur, wenn `Full Resolution` aktiviert ist. Beachte, dass das Denoising erst nach der Berechnung aller Samples erfolgt und prozessorintensiv sein kann.

## Preset‑Browser {#preset-browser}
![](/images/postprocess_presets.webp)
Ein Klick auf das Bild zeigt eine Sammlung von Nachbearbeitungs-Presets an. Um eigene Presets zu definieren, wähle eines aus, klicke auf „clone“ und nimm Änderungen vor. Zum Speichern klicke auf das Preset-Bild, klicke erneut im Preset-Browser und wähle „save“.

## Reflexion (SSR) {#reflection-ssr}
Mit dieser Option können Objekte andere Objekte in der Szene reflektieren, solange die Objekte auf dem Bildschirm sichtbar sind.
Wenn du metallische und glänzende Objekte in deiner Szene hast, sollte diese Option wahrscheinlich verwendet werden.
Diese Option ist nur im PBR-Modus wirksam.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Globale Beleuchtung (SSGI) {#global-illumination-ssgi}

Global Illumination simuliert, wie Licht zwischen Oberflächen hin- und herreflektiert, z. B. wirft eine rote Wand Rotlicht auf ein nahegelegenes weißes Objekt. Dies kann die Realismuswirkung eines Renderings enorm steigern, insbesondere in Kombination mit Ambient Occlusion und Reflections. 

`Strength` – Die Intensität der Global Illumination. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Ein Spotlight befindet sich hinter der Kugel und ist auf die Decke gerichtet. Mit SSGI aus ist nur die Decke beleuchtet. Mit SSGI an reflektiert Licht von der Decke auf die Wände und dann auf die Kugel._

## Umgebungsokklusion (SSAO) {#ambient-occlusion-ssao}
Ambient Occlusion verdunkelt Bereiche, in die Licht weniger gut eindringen kann (Ecken usw.).
Der Effekt hängt nur von der Modellgeometrie ab.

* `Strength` – Intensität des Effekts.
* `Size` – Wie weitreichend der Effekt ist.
* `Curvature bias` – Wie empfindlich der Effekt auf Oberflächenveränderungen reagiert.
* `Color` – Ein Farbton, der in die Occlusion multipliziert wird und für kreative Effekte genutzt werden kann.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO ist am sichtbarsten in Bereichen, die hauptsächlich durch Umgebungslicht beleuchtet werden. Bereiche mit starkem direktem Licht erhalten einen deutlich schwächeren AO-Effekt.

:::

## Tiefenschärfe (DOF) {#depth-of-field-dof}
Fügt einen Unschärfeeffekt in Bereichen hinzu, die außerhalb der Fokusebene liegen.

Tippe einfach auf dein Modell, um den Fokuspunkt zu ändern.

* `Far blur` – Stärke der Unschärfe auf der vom Fokuspunkt weiter entfernten Seite.
* `Near blur` – Stärke der Unschärfe zwischen Fokuspunkt und Kamera.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Bloom {#bloom}
Bloom lässt die hellen Bereiche deiner Szene leuchten.

* `Intensity` – Stärke des Effekts.
* `Radius` – Ausbreitung des Effekts.
* `Threshold` – Wie hell Pixel in der Szene sein müssen, bevor sie zu leuchten beginnen. Ein niedriger Wert lässt fast alles leuchten, ein hoher Wert nur die hellsten Pixel.
* `Color` – Ein Farbton, der für kreative Effekte zum Bloom hinzugefügt werden kann.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Tone‑Mapping {#tone-mapping}
Tone Mapping ist ein Vorgang, der HDR-Werte in den Bereich `[0, 1]` abbildet.
Wenn du es nicht verwendest (oder `none` auswählst), wird jede Farbkomponente über 1 abgeschnitten.
Jegliche Farbnuancen oberhalb dieses Bereichs gehen dann verloren.

* `None/Neutral/Agx/ACES` – Welcher Tonemapper verwendet wird. `None` führt keine Umabbildung durch (aber die anderen Regler funktionieren weiterhin). Die anderen Optionen sind vergleichbar mit der Wahl unterschiedlicher Filmtypen; sie gehen unterschiedlich mit überbelichteten Werten und Farben um. Dies ist ein sehr komplexes Thema – recherchiere zu Tone Mapping, Agx, ACES für mehr Informationen!
* `Exposure` – Gesamthelligkeit des Bildes, ähnlich der Blendenanpassung einer Kamera. Dies kann ein schneller Weg sein, ein Bild global aufzuhellen oder abzudunkeln.
* `Saturation` – Farbintensität. 1 ist neutral, 0 ist monochrom, Werte über 1 sind zunehmend gesättigt.
* `Contrast` – Macht Dunkles dunkler und Helles heller. Vorsichtig verwenden, da bei hohen Werten Artefakte entstehen können.

Beachte, dass bei deaktiviertem `Tone Mapping` einige Details verschwinden, weil die Pixel zu hell sind.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone Mapping kann den Effekt von Global Illumination verstärken. Wenn du die Intensität der Environment-Map reduzierst, die primäre Lichtquelle erhöhst und dann die `exposure` des Tone Mappings anhebst, kannst du mehr der Bounce-Lighting-Effekte sichtbar machen.
:::

## Farbkorrektur {#color-grading}
Ähnlich wie das Kurven-Werkzeug in Photoshop ermöglicht dies die Kontrolle über Balance und Verteilung der Farben im Bild. Die `main`-Kurve beeinflusst die gesamte Farbbalance, die `red`/`green`/`blue`-Kurven erlauben eine Feinabstimmung. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Krümmung {#curvature}
Erkennt Bereiche mit schnellen Krümmungsänderungen und wendet dort eine Farbe an.

* `Factor` – Gesamtintensität des Effekts
* `Bump` – Wie stark scharfe konvexe Änderungen erkannt und mit der gewählten Farbe versehen werden (standardmäßig Weiß)
* `Cavity` – Wie stark konkave Änderungen erkannt und mit der gewählten Farbe versehen werden (standardmäßig Schwarz)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Chromatische Aberration {#chromatic-aberration}
Simuliert Linsenartefakte, bei denen Licht an den Bildschirmrändern in seine Bestandteile zerlegt wird.

* `Strength` – Wie stark die roten/grünen/blauen Bildanteile zu den Bildschirmrändern hin aufgespalten werden

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignettierung {#vignette}
Simuliert Linsenartefakte, indem die Bildschirmränder abgedunkelt werden.

* `Size` – Die Größe einer invertierten Ellipse, die über das Bild gelegt wird
* `Hardness` – Wie weich oder hart die Ellipse mit dem Bild überblendet wird.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Filmkorn {#grain}
Fügt einen Körnungseffekt hinzu; dies kann helfen, das Bild etwas weniger künstlich wirken zu lassen.

* `Strength` – Die Menge an Körnung/Rauschen, die dem Bild hinzugefügt wird.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Schärfe {#sharpness}
Ein Schärfeeffekt ähnlich dem in Photoshop oder Foto-Apps.

* `Strength` – Die Stärke der auf das Bild angewendeten Schärfung.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel‑Art {#pixel-art}
Simuliert Retro-Game-Pixelgrafik.

* `Slider` – Größe der Pixel
* `Allow frame sampling` – Wenn du viele schwarze Pixel bekommst, versuche dies zu aktivieren; es überschreibt das Standard-Sampling.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline {#scanline}
Simuliert das Aussehen alter CRT-Monitore.

* `Factor` – Stärke der Linien
* `Spacing` – Größe/Abstand der Linien

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering {#dithering}

Dithert Pixel, um Banding-Artefakte zu reduzieren. Normalerweise sollte dies aktiviert sein, kann aber für spezielle Vorgänge deaktiviert werden (z. B. beim Export von Tiefenmaps oder anderen datenspezifischen Operationen).