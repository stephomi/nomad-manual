# ![](/icons/postprocess.webp) Nabewerking 

Dit menu bepaalt veel aspecten van Nomad die het uiterlijk van de render beïnvloeden.

![](/images/postprocess_overview_drac.webp)

Het gebruik van nabewerking kan het uiteindelijke uiterlijk van je scène aanzienlijk veranderen.

![](/images/postprocess_overview.webp)
*Dezelfde scène vóór en na nabewerking, zonder extra lichten of materiaalwijzigingen.*

Nabewerking kan de prestaties sterk beïnvloeden, afhankelijk van je apparaat.
Er is een globale checkbox om alle nabewerking uit te schakelen, zodat je snel kunt terugkeren naar sculpten/modelleren zonder je presets te verliezen.
Voor PBR-rendering moeten [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) en [Tone Mapping](#tone-mapping) ingeschakeld zijn.

Meestal wil je nabewerking echter uitgeschakeld hebben tijdens het sculpten, om je te concentreren op de vorm zelf van de render.

## Kwaliteit

![](/images/postprocess_quality.webp)
### Max frame sampling
Nomad zal een bepaalde hoeveelheid nabewerking voor een enkel frame berekenen, wat er korrelig/ruisachtig uit kan zien. Deze instelling bepaalt hoeveel frames er gerenderd en vervolgens samengevoegd worden om de meeste ruisartefacten te verwijderen. Sommige effecten hebben geen extra samples nodig (bijv. color grading), terwijl andere, zoals global illumination, honderden samples kunnen vereisen om ruisvrij te zijn. 

In de viewport is dit te zien wanneer Nomad met rust wordt gelaten: de beeldkwaliteit verfijnt geleidelijk tot aan het maximum aantal samples en stopt dan. Dit aantal berekeningen wordt ook gebruikt in het rendergedeelte van het [Bestanden-menu](files) wanneer op 'export png' wordt geklikt.

### Resolutiemultiplier
Deze schuifregelaar bepaalt de resolutie van de nabewerking. Een waarde van x1.0 betekent dat de renders worden gedaan op de pixelresolutie van het apparaat. Een waarde van x0.5 rendert op halve resolutie, wat snel maar van lage kwaliteit is. Een waarde groter dan 1 rendert op een grotere resolutie en schaalt dan terug. Dit resulteert in hogere kwaliteit, minder ruis, maar langere rendertijden.

### Max samples

Dit verhoogt de kwaliteit van de nabewerking, maar over het algemeen heeft `Full resolution` meer impact. 

### Full resolution
Indien ingeschakeld, wordt de resolutiemultiplier geforceerd naar x1.0

### Denoiser (oidn)

Past een denoiser toe op het beeld. Hierdoor kun je veel lagere aantallen samples gebruiken. Dit werkt alleen als `Full Resolution` is ingeschakeld. Merk op dat de denoising gebeurt nadat alle samples zijn berekend, en dat dit processorintensief kan zijn.

## Presetbrowser
![](/images/postprocess_presets.webp)
Door op de afbeelding te klikken wordt een verzameling nabewerkingspresets weergegeven. Om je eigen presets te definiëren, selecteer er één, klik op 'clone', breng wijzigingen aan. Om op te slaan, klik op de presetafbeelding, klik opnieuw in de presetbrowser en kies 'save'.

## Reflectie (SSR)
Met deze optie kunnen objecten andere objecten in de scène reflecteren, zolang de objecten zichtbaar zijn op het scherm.
Als je metalen en glanzende objecten in je scène hebt, dan zou je deze optie waarschijnlijk moeten gebruiken.
Deze optie is alleen effectief in PBR-modus.

| SSR uit                     | SSR aan                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Global Illumination (SSGI)

Global illumination simuleert hoe licht tussen oppervlakken weerkaatst, bijv. een rode muur zal rood licht werpen op een nabijgelegen wit object. Dit kan de realiteit van een render enorm vergroten wanneer het wordt gebruikt met ambient occlusion en reflecties. 

`Strength` - De intensiteit van de global illumination. 

| SSGI uit                    | SSGI aan                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Een spotlight staat achter de bol, gericht op het plafond. Met SSGI uit is alleen het plafond verlicht. Met SSGI aan weerkaatst licht van het plafond naar de muren naar de bol._

## Ambient Occlusion (SSAO)
Ambient occlusion zal gebieden donkerder maken waar licht minder kans heeft om te komen (hoeken, enz.).
Het effect hangt alleen af van de modelgeometrie.

* `Strength`- Intensiteit van het effect.
* `Size`- Hoe wijdverspreid het effect is.
* `Curvature bias` - Hoe gevoelig het effect is ten opzichte van variaties in het oppervlak.
* `Color` - Een tint die met de occlusion wordt vermenigvuldigd, gebruikt voor creatieve effecten.

| SSAO uit                     | SSAO aan                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO zal het meest zichtbaar zijn in gebieden die voornamelijk door omgevingslicht worden verlicht. Gebieden die onder sterk direct licht staan, krijgen een veel zwakker AO-effect.

:::

## Depth of Field (DOF)
Voegt een vervagingseffect toe aan het gebied dat zich buiten het focuspunt bevindt.

Tik eenvoudig op je model om het focuspunt te wijzigen.

* `Far blur` - De hoeveelheid vervaging die wordt toegepast aan de verre zijde van het focuspunt.
* `Near blur` - De hoeveelheid vervaging die wordt toegepast tussen het focuspunt en de camera.

| DOF uit                    | DOF focus op verre ring     | DOF focus op dichte ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |

## Bloom
Bloom laat de heldere gebieden van je scène gloeien.

* `Intensity` - sterkte van het effect.
* `Radius` - De spreiding van het effect.
* `Threshold` - Hoe helder pixels in de scène moeten zijn voordat ze beginnen te bloomen. Een lage waarde zorgt ervoor dat alles bloomt, een hoge waarde zorgt ervoor dat alleen de helderste pixels bloomen.
* `Color` - een tint die aan bloom kan worden toegevoegd voor creatieve effecten.

| Bloom uit                     | Bloom met radius 0          | Bloom met radius 1          |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |

## Tone Mapping
Tone Mapping is een bewerking die HDR-waarden opnieuw toewijst naar het `[0, 1]`-bereik.
Als je het niet gebruikt (of `none` selecteert), wordt elke kleurcomponent hoger dan 1 afgeknipt.
Alle kleurvariaties boven dit bereik gaan dan verloren.

* `None/Neutral/Agx/ACES` - welke tonemapper te gebruiken. `None` doet geen remapping (maar de andere instellingen werken nog steeds). De andere opties zijn vergelijkbaar met het kiezen van verschillende filmtypes; ze gaan op verschillende manieren om met overbelichte waarden en kleuren. Dit is een zeer diepgaand onderwerp, zoek naar tone mapping, Agx, ACES voor meer info!
* `Exposure` - algemene helderheid van de beelden, vergelijkbaar met het aanpassen van het diafragma van een camera. Dit kan een snelle manier zijn om een beeld globaal lichter of donkerder te maken.
* `Saturation` - kleursterkte. 1 is neutraal, 0 is monochroom, waarden boven 1 zijn steeds meer verzadigd.
* `Contrast` - Maakt donkere delen donkerder en lichte delen lichter. Gebruik voorzichtig, bij hoge waarden kunnen artefacten ontstaan.

Merk op dat met `Tone Mapping` uit sommige details verdwijnen omdat de pixels te helder zijn.

| Tone Mapping uit             | Tone Mapping aan            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping kan het effect van global illumination versterken. Als je de intensiteit van de environment map omlaag zet, de primaire lichtbron omhoog, kun je de `exposure` van tone mapping verhogen om meer van de bounce lighting-effecten te zien.
:::

## Color Grading
Vergelijkbaar met het curves-gereedschap in Photoshop, hiermee kun je de balans en verdeling van kleur in het beeld regelen. De `main`-regeling beïnvloedt de volledige kleurbalans, de `red`/`green`/`blue`-regelingen bieden fijne controle. 

| Color Grading uit              | Color Grading aan             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Detecteert waar er snelle veranderingen in kromming zijn en past een kleur toe op die gebieden.

* `Factor` - algemene intensiteit van het effect
* `Bump` - in welke mate scherpe convexe veranderingen worden gevonden en de geselecteerde kleur daar wordt geplaatst (standaard wit)
* `Cavity` - in welke mate concave veranderingen worden gedetecteerd en de geselecteerde kleur daar wordt geplaatst (standaard zwart)

| Curvature uit                   | Curvature aan                  |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |

## Chromatic Aberration
Simuleert lensartefacten waarbij licht rond de schermranden wordt opgesplitst.

* `Strength` - in welke mate de rode/groene/blauwe delen van het beeld naar de schermranden toe uit elkaar worden getrokken

| Chromatic uit                | Chromatic aan                |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |

## Vignet
Simuleert lensartefacten door de schermranden te verdonkeren.

* `Size` - De grootte van een omgekeerde ellips die over het beeld wordt geplaatst
* `Hardness` - Hoe wazig of scherp de ellips boven op het beeld wordt gemengd.

| Vignet uit                     | Vignet aan                     |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Voegt een korrel-/ruiseffect toe; dit kan helpen om het beeld wat minder kunstmatig te laten lijken.

* `Strength` - de hoeveelheid korrel/ruis die aan het beeld wordt toegevoegd.

| Grain uit                     | Grain aan                    |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |

## Sharpness
Een verscherpingseffect vergelijkbaar met dat in Photoshop of fotobewerkingsapps.

* `Strength` - de hoeveelheid verscherping die op het beeld wordt toegepast.

| Sharpness uit                   | Sharpness aan                  |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Simuleert retro game pixel art.

* `Slider` - grootte van de pixels
* `Allow frame sampling` - als je veel zwarte pixels krijgt, probeer dit dan in te schakelen; dit overschrijft de standaard sampling.

| Pixel uit                    | Pixel aan                    |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Simuleert het uiterlijk van oude CRT-monitoren.

* `Factor` - sterkte van de lijnen
* `Spacing` - grootte van de lijnen

| Scanline uit                    | Scanline aan                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

## Dithering

Past dithering toe op pixels om banding-artefacten te verminderen. Meestal zou dit ingeschakeld moeten zijn, maar het kan worden uitgeschakeld voor specifieke bewerkingen (bijv. het exporteren van depth maps of andere dataspecifieke bewerkingen).
