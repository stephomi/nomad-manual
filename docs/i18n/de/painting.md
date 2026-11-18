# ![](/icons/paint.webp) Zeichnen {#painting}

Hier steuern Sie Farbe, Rauheit und Metallizität der Malstriche, füllen Malattribute flächig auf und legen fest, wie Malwerkzeuge mit Ebenen, Masken und ausgeblendeten Bereichen zusammenspielen.

![](/images/paint_overview.webp)  

## Überblick {#overview}

Nomad verwendet PBR-Vertex-Painting. Was bedeutet das?

### PBR {#pbr}
PBR (Physically Based Rendering, physikalisch basiertes Rendering) ist eine verbreitete Computergrafik-Technik für Film, Fernsehen, Spiele und Mobilgeräte. Indem das Licht auf physikalischen Eigenschaften beruht und Oberflächen über Farbe, Rauheit und Metallizität beschrieben werden, lässt sich eine große Vielfalt fotorealistischer Looks erzielen.

### Vertex-Painting {#vertex-painting}

Vertex-Painting bedeutet, dass die Malinformationen in den Vertices des Modells gespeichert werden statt in Texturen. Da Nomad Modelle mit Hunderttausenden, oft Millionen von Vertices verarbeiten kann, können Ihre Modelle sehr detailreich bemalt sein: Was Sie an Details sculpten können, können Sie auch malen.

Das bedeutet auch, dass Sie zum Malen in Nomad kein UV-Mapping brauchen, das in anderen 3d-Programmen oft ein langsamer und technischer Vorgang ist. Viele andere 3d-Programme kommen nicht mit so hohen Vertex-Zahlen zurecht wie Nomad, doch Nomad bietet auch gute Werkzeuge zum Backen von Texturen und zum Dezimieren, die dabei helfen.

### Texturierung {#texturing}

Nomad unterstützt Texturen, allerdings müssen sie in einem importierten Modell enthalten sein oder durch Backen des Vertex-Paintings in Texturen entstehen.

Eine Textur ist einfach ein Bild, aber im 3d-Kontext meint man damit meist ein Bild, das einem Objekt zugewiesen ist.
Damit sich ein Bild um ein Modell legen lässt, braucht das Modell Texturkoordinaten (UV).

Nomad kann [sie automatisch berechnen](topology.md#uv-unwrap), aber Sie haben dabei wenig Einfluss auf die Gesamtqualität.

::: tip
Ein Beispiel für einen Arbeitsablauf:
- In Nomad sculpten, dann ein [UV-Unwrapping](topology.md#uv-unwrap) durchführen
- Wenn Sie in Nomad schon zu malen begonnen haben, können Sie [das Vertex-Painting in Texturen übertragen](topology.md#bake-texture)
- Nach Procreate exportieren
- In Procreate texturieren
- Zurück nach Nomad exportieren, um zu rendern
:::

So viel zum Überblick; sehen wir uns nun die Bereiche des Malmenüs an:


## Striche malen {#stroke-painting}
![](/images/paint_intensity.webp)  

Aktiviert das Malen für dieses Werkzeug; nützlich, wenn Sie gleichzeitig sculpten und malen möchten. Kann ein Werkzeug malen, ist dieses Kontrollkästchen aber ausgeschaltet, erinnert Sie ein Warnsymbol neben dem Titel daran.

Bei Werkzeugen, deren Hauptaufgabe das Malen ist (z. B. Zeichnen, Wischfinger, Maske), gibt es dieses Kontrollkästchen nicht.

### ![](/icons/opacity.webp) Malintensität {#paint-intensity}

Ein Regler, mit dem Sie beim Malen eine andere Intensität als die Hauptintensität des Werkzeugs verwenden können.

Die Regler-Schaltfläche daneben fügt der Seitenleiste einen Schnellregler für die Malintensität hinzu, für Werkzeuge, die gleichzeitig sculpten und malen.

Die Schaltflächen `Alpha`, `Falloff` und `Intensität randomisieren` legen fest, ob diese Funktionen das Malen beeinflussen. So können Sie zum Beispiel beim Werkzeug Ton die Zufallsvariation aktivieren, ohne dass die Farbe zufällig variiert.

* `Alpha` - ist diese Option deaktiviert, ignoriert das Malen das Alpha und deckt die gesamte Pinselfläche ab. Beim Werkzeug VDM wird diese Schaltfläche durch `Stempelmaterial` ersetzt, das das im Stempel gespeicherte Material ein- oder ausschaltet.
* `Falloff` - ist diese Option deaktiviert, bleibt die Malintensität bis zum Pinselrand voll erhalten.
* `Intensität randomisieren` - legt fest, ob der Intensitätsanteil der Zufallsvariation des Strichs das Malen beeinflusst. Die Zufallsvariation von Position, Rotation und Skalierung bewegt immer den ganzen Stempel.

[Füllen](#paint-all) ignoriert diese Optionen, seine Triplanar-Variante verwendet aber das Alpha.

### ![](/icons/link.webp) Globales Material {#global-material}
Ist diese Option aktiviert, ist das ausgewählte Material dasselbe wie bei den anderen Werkzeugen. Beachten Sie, dass dabei nur die Einstellungen für Rauheit, Metallizität und Farbe berücksichtigt werden. Deaktivieren Sie die Option, um diesem Werkzeug ein eigenes Material zu geben.


## Material {#material}
![](/images/paint_material.webp) 

Das erste Icon ist eine Vorschauform des Materials. Ziehen Sie auf der 3d-Materialvorschau, um sie zu drehen.

Das zweite Icon ist eine Vorschau des Malstrichs mit den gewählten Alpha- und Falloff-Optionen.

### ![](/icons/falloff.webp) Kurven {#curves}

Öffnet einen Kurveneditor für die Textur-Slots der [PBR-Regler](#pbr-sliders). Er rechnet die Texturwerte um, bevor sie gemalt werden, ohne die Bilddatei anzutasten. Ein kleines Kurven-Icon auf einem Textur-Slot zeigt Ihnen, dass seine Kurve bearbeitet wurde.

### ![](/icons/cog.webp) Materialoptionen {#material-options}

Die Schaltfläche `Material` neben dem Titel enthält zwei Einstellungen.

`Materialvorschau im Viewport` legt fest, was auf dem ausgewählten Objekt geschieht, während Sie die Regler für Farbe, Rauheit, Metallizität, Deckkraft und Intensität verändern:

* `Keine` - Beim Anpassen der Eigenschaften wird keine Vorschau auf dem Modell angezeigt
* `Material` - Beim Anpassen der Eigenschaften werden die Materialwerte als Vorschau auf dem Objekt angezeigt.
* `Triplanar` - Das Material wird als Triplanar-Projektion in der Vorschau angezeigt.

Mit den Kontrollkästchen für Farbe, Rauheit, Metallizität und Deckkraft darunter wählen Sie, welche Kanäle die [Materialpipette](#material-picker) ersetzt.

### ![](/icons/dropper.webp) Materialpipette {#material-picker}

Die Pipette nimmt das Material unter dem Cursor auf, von jedem Objekt in Ihrer Szene. Ersetzt werden nur die Kanäle, die in den [Materialoptionen](#material-options) angehakt sind.

## Material-Presets {#material-presets}
Tippen Sie auf die 3d-Vorschauform, um ein Preset-Menü mit Materialien zu öffnen. Diese können Sie klonen, um eigene Presets anzulegen.

![](/images/paint_presets.webp) 

Der Schalter `Texturen einbetten` speichert eine Kopie der von diesem Material verwendeten Texturen im Preset. Ohne ihn verweist das Preset nur auf die Texturen im Nomad-Ordner textures/. Aktivieren Sie ihn, wenn Sie ein texturiertes Preset weitergeben möchten, ohne seine Texturen separat zu verschicken.

`Alpha einbeziehen` speichert außerdem das Pinsel-Alpha im Material-Preset.

## PBR-Regler {#pbr-sliders}
![](/images/paint_sliders.webp) 

Das [PBR](shading.md#pbr)-Malen verwendet 4 Kanäle:
- `Farbe` Die Farbe, die gemalt wird. Mit der Pipette können Sie Farben von anderen Stellen des Modells oder aus Referenzbildern aufnehmen.
- `Matt` Gibt an, wie „rau“ oder „glatt“ eine Oberfläche ist. Ein niedriger Rauheitswert bedeutet scharfe Spiegelungen.
- `Metallisch` Gibt schlicht an, ob die Oberfläche metallisch ist oder nicht. Meist sollte der Wert entweder 0 % oder 100 % betragen; Zwischenwerte sollten die Ausnahme sein.
- `Deckkraft` Wie stark man durch das Material hindurchsehen kann. Streng genommen gehört sie nicht zur PBR-Spezifikation, ist aber in vielen Situationen nützlich. 1 ist vollständig deckend, 0 ist transparent. Beachten Sie, dass Deckkraft und Refraktion zwei verschiedene Dinge sind: Die Refraktion wird in Nomad über das Refraktionsmaterial gesteuert.

Wenn Sie ein Material-Preset auswählen, werden 3 Kanäle gleichzeitig gemalt (die Deckkraft ist oft absichtlich ausgenommen). Statt einfach nur „Rot“ malen Sie so zum Beispiel „ein rotes, raues Metall“ oder „einen weißen, glatten Kunststoff“.

Das Quadrat ist ein Textur-Slot: Tippen Sie darauf, um für diese Eigenschaft eine Textur statt eines festen Werts zu verwenden. Eine Farbtextur färbt die Farbe ein, während eine Textur für Rauheit, Metallizität oder Deckkraft den Reglerwert ersetzt (sein Label wird dann durchgestrichen). Bei der Deckkraft-Textur liest `Alpha als Wert verwenden` den Alphakanal der Textur statt ihres Graustufenwerts.

Wenn beim Werkzeug VDM der Stempel sein eigenes Material mitbringt, zeigt ein zusätzlicher Slot neben dem Textur-Slot dieses Material an. Tippen Sie darauf, um diesen Kanal des Stempels zu verwenden oder zu ignorieren.

Das Pinsel-Icon neben den Reglern füllt Ihr Objekt flächig mit dieser Eigenschaft.

Das Kontrollkästchen aktiviert oder deaktiviert die jeweilige Eigenschaft. So können Sie zum Beispiel nur Farbe malen oder nur Rauheit und Deckkraft.

Hier einige Beispiele für verschiedene Werte von Rauheit und Metallizität:

|                | Metallizität 0 %                  | Metallizität 100 %           |
| :------------: | :-------------------------------: | :--------------------------: |
| Rauheit 0 %    | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Rauheit 50 %   | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Rauheit 100 %  | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Rauheit und Metallizität erfordern den Shading-Modus [PBR](shading.md#pbr). Im Modus [MatCap](shading.md#matcap) oder [Unbeleuchtet](shading.md#unlit) werden sie ignoriert, und das Menü zeigt eine Warnung an.
:::

::: tip
Wenn Sie Texturen für das PBR-Malen verwenden, ist es oft sinnvoll, zu einem Werkzeug wie `Stempel` zu wechseln oder im Strich-Menü einen anderen Modus als Punkt zu wählen, da dieser die Textur verschmieren kann.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Wenn Sie eine metallische Oberfläche auf ein Objekt mit eher wenigen Polygonen malen, lohnt es sich, `Smooth Shading` [global](settings.md#smooth-shading) oder [pro Objekt](material.md#smooth-shading) zu aktivieren.
:::

## ![](/icons/paint.webp) Füllen {#paint-all}

![](/images/paint_paint_all.webp)

Wendet das aktuelle Material auf die ausgewählten Objekte an, entweder im Standardmodus mit `Füllen` oder als Triplanar-Projektion mit `Füllen + Triplanar`. Die Triplanar-Variante ist bei nicht validierten Grundformen nicht verfügbar.

Die Kontrollkästchen neben den Reglern für Farbe/Metallizität/Rauheit/Deckkraft werden berücksichtigt: Deaktivierte Eigenschaften werden nicht gefüllt.

Mit den zusätzlichen Schaltflächen können Sie das Füllen weiter beeinflussen. Die meisten zeigen einen Prozentwert und sind ausgegraut, wenn sie keine Wirkung hätten:

| Symbol                      | Beschreibung                                  |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Maskierte Bereiche bleiben unverändert.       |
| ![](/icons/tool_hide.webp) | Ausgeblendete Bereiche bleiben unverändert.   |
| ![](/icons/opacity.webp)   | Verwendet den Malfaktor des Werkzeugs von oben. |
| ![](/icons/layer.webp)     | Unbemalte Bereiche einer Ebene bleiben unverändert. |
| ![](/icons/triplanar.webp) | `Vertex`: Die Triplanar-Variante verschiebt die Oberfläche zusätzlich mit dem Alpha, um die angezeigte Werkzeugintensität. |
| ![](/icons/cog.webp)       | Öffnet die Triplanar-Einstellungen            |

### ![](/icons/cog.webp) Triplanar-Einstellungen {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Wie bei den [Triplanar-Einstellungen im Material-Menü](material.md#triplanar) können Sie die Überblendung der Projektionen, die Kachelung und die Versätze steuern.

Mit dem Vorschau-Kontrollkästchen oben in diesem Menü aktivieren Sie eine dauerhafte Vorschau, während Sie die Werte anpassen.
