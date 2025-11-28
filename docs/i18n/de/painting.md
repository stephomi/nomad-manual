# ![](/icons/paint.webp) Malen {#painting}

Steuern Sie Farbe, Rauheit und Metallizität von Pinselstrichen, ermöglichen Sie Flutfüllungen von Malattributen und legen Sie fest, wie Malwerkzeuge mit Ebenen, Masken und versteckten Auswahlen interagieren.

![](/images/paint_overview.webp)  

## Übersicht {#overview}

Nomad verwendet PBR-Vertex-Painting. Was bedeutet das?

### PBR {#pbr}
PBR, oder Physically Based Rendering, ist eine beliebte Computergrafik-Technik für Film, Fernsehen, Spiele und Mobile. Durch die physikalische Grundlage der Beleuchtung und die Definition von Oberflächen über Farbe, Rauheit und Metallizität kann eine große Bandbreite fotorealistischer Looks erzielt werden.

### Vertex-Malerei {#vertex-painting}

Vertex-Painting bedeutet, dass die Malinformationen in den Vertices des Modells gespeichert werden, anstatt in Texturen. Da Nomad Modelle mit Hunderttausenden, oft Millionen von Vertices verarbeiten kann, sollten Ihre Modelle sehr detaillierte Oberflächenbemalung haben können; wenn Sie ein Detail modellieren können, können Sie dieses Detail auch bemalen.

Das bedeutet auch, dass Malen in Nomad kein UV-Mapping erfordert, was in anderen 3D-Anwendungen oft ein langsamer und technischer Prozess ist. Viele andere 3D-Anwendungen unterstützen nicht die hohen Vertex-Anzahlen, die Nomad verarbeiten kann, allerdings verfügt Nomad auch über gute Werkzeuge zum Textur-Backen und zur Reduktion (Decimation).

### Texturierung {#texturing}

Nomad unterstützt Texturen, aber sie müssen in einem importierten Modell vorhanden sein oder über das Backen von Vertex-Painting in Texturen erzeugt werden. 

Eine Textur ist einfach ein Bild, aber im 3D-Kontext bezieht sie sich üblicherweise auf ein Bild, das einem Objekt zugewiesen ist.
Um ein Bild um ein Modell zu legen, benötigt das Modell Texturkoordinaten (UV).

Nomad kann [sie automatisch berechnen](topology.md#uv-unwrap), aber Sie haben nicht viel Kontrolle über die Gesamtqualität.

::: tip
Ein Beispiel-Workflow:
- In Nomad modellieren, dann [UV-Unwrap](topology.md#uv-unwrap)
- Wenn Sie in Nomad bereits mit dem Malen begonnen haben, können Sie [das Vertex-Painting auf Texturen übertragen](topology.md#bake-vertex-colors-to-texture)
- Export nach Procreate
- Texturieren in Procreate
- Export zurück nach Nomad zum Rendern
:::

Das ist die Übersicht, nun sehen wir uns die Bereiche des Malmenüs an:


## Pinselstrich-Malerei {#stroke-painting}
![](/images/paint_intensity.webp)  

Aktiviert das Malen für dieses Werkzeug, nützlich, wenn Sie gleichzeitig modellieren und malen müssen.

Für Werkzeuge, bei denen Malen die Hauptfunktion ist (z. B. Paint, Smudge, Mask), existiert dieses Kontrollkästchen nicht.

### Malintensität {#paint-intensity}

Ein Schieberegler, mit dem Sie eine andere Intensität als die primäre Werkzeugintensität verwenden können.

Die Kontrollkästchen `Alpha`, `Falloff` und `Randomize` bestimmen, ob diese Funktionen das Malen beeinflussen. Sie könnten z. B. Randomize für das Clay-Werkzeug aktiviert haben, aber die Farbe wird nicht zufällig verändert.


## Material {#material}
![](/images/paint_material.webp) 

Das erste Symbol ist eine Materialvorschauform. Durch Ziehen an der 3D-Materialvorschau drehen Sie diese. 

Das zweite Symbol ist eine Vorschau des Pinselstrichs mit den ausgewählten Alpha- und Falloff-Optionen.

Die Vorschau-Schaltfläche neben dem Titel „Material“ lässt Sie zwischen None, Material oder Triplanar umschalten. Dies bestimmt, was passiert, wenn Sie Mal-Eigenschaften interaktiv ändern:

* `None` – Auf dem Modell wird keine Vorschau angezeigt, wenn Sie Eigenschaften anpassen.
* `Material` – Die Materialwerte werden auf dem Objekt in der Vorschau angezeigt, wenn Sie Eigenschaften anpassen. Wenn Sie Texturen verwenden und das Modell UVs hat, werden die UVs verwendet.
* `Triplanar` – Das Material wird als Triplanar-Projektion in der Vorschau angezeigt. 

Die Pipette kann verwendet werden, um alle Eigenschaften von einem Objekt in Ihrer Szene zu übernehmen.

## Material-Voreinstellungen {#material-presets}
Durch Tippen auf die 3D-Vorschauform wird ein Preset-Menü mit Materialien geöffnet, die geklont werden können, um eigene Presets zu definieren.

![](/images/paint_presets.webp) 

Die Umschalter `Embed Textures` und `Alpha` speichern bei Aktivierung alle von diesem Material verwendeten Texturen innerhalb des Presets. Dies wird weiter unten näher erläutert.

## PBR-Regler {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr)-Malen verwendet 4 Kanäle:
- `Color` Die Farbe, die gemalt wird. Die Pipette kann verwendet werden, um Farbe von anderen Teilen des Modells oder von Referenzbildern auszuwählen.
- `Roughness` Gibt an, wie „rau“ oder „glatt“ eine Oberfläche ist. Ein niedriger Rauheitswert bedeutet, dass die Spiegelungen scharf sind.
- `Metalness` Gibt einfach an, ob die Oberfläche metallisch ist oder nicht. Der Wert sollte die meiste Zeit entweder 0 % oder 100 % betragen, Zwischenwerte sollten die Ausnahme sein.
- `Opacity` Wie stark das Material durchscheinend ist. Streng genommen ist es nicht Teil der PBR-Spezifikation, aber in vielen Situationen nützlich. 1 ist vollständig deckend, 0 ist transparent. Beachten Sie, dass Deckkraft und Brechung unterschiedliche Dinge sind; Brechung wird in Nomad über das Refraction-Material gehandhabt. 

Wenn Sie ein Material-Preset auswählen, werden 3 Kanäle gleichzeitig gemalt (Deckkraft wird oft absichtlich ausgeschlossen). Das bedeutet, dass Sie statt nur „Rot“ zu malen, z. B. „ein rotes raues Metall“ oder „einen weißen glatten Kunststoff“ malen können.

Das Quadrat ist ein Textur-Slot, klicken Sie darauf, um für diese Eigenschaft eine Textur anstelle eines festen Werts zu verwenden.

Das Pinselsymbol neben den Schiebereglern füllt diese Eigenschaft über Ihr Objekt hinweg.

Das Kontrollkästchen aktiviert oder deaktiviert diese bestimmte Eigenschaft, sodass Sie z. B. nur Farbe oder nur Rauheit und Deckkraft malen könnten. 

Hier einige Beispiele für unterschiedliche Rauheits- und Metallizitäts-Eigenschaften:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Im [Matcap-Rendering](shading.md#matcap)-Modus wird nur Farbe unterstützt, Metallizität und Rauheit werden ignoriert.
:::

::: tip
Wenn Sie Texturen für PBR-Malen verwenden, ist es oft hilfreich, auf ein Werkzeug wie `Stamp` zu wechseln oder im Stroke-Menü einen anderen Modus als Dot zu verwenden, der die Textur verschmieren kann.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Sie sollten in Erwägung ziehen, `Smooth Shading` [global](settings.md#smooth-shading) oder [pro Objekt](material.md#smooth-shading) zu aktivieren, wenn Sie eine metallische Oberfläche auf einem Objekt mit niedriger Polygonanzahl bemalen.
:::

## Alles malen {#paint-all}

![](/images/paint_paint_all.webp)

Wendet das aktuelle Material auf das Objekt an, entweder im Standardmodus mit „Paint All“ oder als Triplanar-Projektion.

Die Kontrollkästchen neben den Color-/Metalness-/Roughness-/Opacity-Schiebereglern werden berücksichtigt, deaktivierte Eigenschaften werden nicht gefüllt.

Die zusätzlichen Schaltflächen steuern, wie „Paint All“ weiter beeinflusst werden kann:

| Icon                        | Beschreibung                                   |
| :-------------------------: | :--------------------------------------------: |
| ![](/icons/tool_mask.webp) | Maskierte Bereiche werden nicht beeinflusst.   |
| ![](/icons/tool_hide.webp) | Versteckte Bereiche werden nicht beeinflusst.  |
| ![](/icons/opacity.webp)   | Verwendet den obenstehenden Werkzeug-Malfaktor.|
| ![](/icons/layer.webp)     | Unbemalte Bereiche einer Ebene werden nicht beeinflusst. |
| ![](/icons/triplanar.webp) | Indikator für Triplanar-Einstellungen          |
| ![](/icons/cog.webp)       | Öffnet die Triplanar-Einstellungen             |

### Triplanare Einstellungen {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Ähnlich wie die [Triplanar-Einstellungen im Materialmenü](material.md#triplanar) können Sie das Blending der Projektionen, das Tiling und die Offsets steuern. 

Verwenden Sie das Vorschau-Kontrollkästchen oben in diesem Menü, um eine dauerhafte Vorschau beim Anpassen der Werte zu aktivieren.

## Globales Material {#global-material}
Wenn diese Option aktiviert ist, ist das ausgewählte Material dasselbe wie bei den anderen Werkzeugen. Beachten Sie, dass dabei nur Rauheits-, Metallizitäts- und Farbeinstellungen berücksichtigt werden.