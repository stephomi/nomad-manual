# ![](/icons/postprocess.webp) Nabewerking {#post-process}

Dit menu regelt allerlei aspecten van Nomad die het uiterlijk van de render beïnvloeden.

![](/images/postprocess_overview_drac.webp)

Met nabewerking kun je de uiteindelijke look van je scène flink veranderen.

![](/images/postprocess_overview.webp)
*Dezelfde scène voor en na de nabewerking, zonder extra lichten of aangepaste materialen.*

Afhankelijk van je apparaat kan de nabewerking de prestaties sterk beïnvloeden.
Met het algemene vinkje `Nabewerking` zet je alle nabewerking in één keer uit, zodat je snel verder kunt met sculpten of modelleren zonder je presets kwijt te raken.
Voor PBR-rendering kun je het beste [Omgevingsocclusie](#ambient-occlusion-ssao), [Reflectie](#reflection-ssr) en [Toonmapping](#tone-mapping) aanzetten.

Toch wil je de nabewerking meestal uitzetten tijdens het sculpten, zodat je je op de vorm zelf concentreert in plaats van op de rendering.


## Kwaliteit {#quality}

![](/images/postprocess_quality.webp)

Deze opties verbeteren de kwaliteit van de render, ten koste van de prestaties.

### Max. frame-sampling {#max-frame-sampling}
Voor een render van één frame berekent Nomad een bepaalde hoeveelheid nabewerking, en dat kan er korrelig uitzien. Deze regelaar bepaalt hoeveel frames er worden gerenderd en daarna samengevoegd om de meeste ruis weg te werken. Sommige effecten hebben geen extra samples nodig (bijvoorbeeld kleurbewerking), terwijl andere, zoals zachte schaduwen en globale verlichting, honderden samples nodig kunnen hebben om ruisvrij te zijn.

In de viewport zie je dit zodra je Nomad met rust laat: de beeldkwaliteit wordt geleidelijk beter tot het maximale aantal samples, en dan stopt het. Daarna doet Nomad niets meer, wat de batterij spaart. Hetzelfde aantal berekeningen wordt gebruikt in het rendergedeelte van het [menu Bestanden](files) wanneer je op 'export png' klikt.

Met het vinkje naast de schuifregelaar zet je frame-sampling aan of uit.

### Renderresolutie {#resolution-multiplier}
Deze schuifregelaar bepaalt de resolutie van de render. Bij x1.0 wordt gerenderd op de pixelresolutie van het apparaat. Bij x0.5 wordt op halve resolutie gerenderd: snel, maar van lage kwaliteit. Een waarde groter dan 1 rendert op een groter formaat en schaalt daarna terug. Dat geeft een hogere kwaliteit en minder ruis, maar het renderen duurt langer.

Dit heeft grote invloed op de prestaties, dus houd het bij voorkeur op x1.25 of lager. Deze waarde wordt niet opgeslagen in de instellingen, en het effect [Pixelart](#pixel-art) overschrijft hem.

### ![](/icons/intensity.webp) Max. samples {#max-samples}

Verbetert de kwaliteit van de nabewerkingseffecten, ten koste van de prestaties.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Verspreidt pixels om kleurbanden te verminderen (bijvoorbeeld in verlopen of in het vignet). Meestal laat je dit aanstaan, maar je kunt het uitzetten voor specifieke handelingen (bijvoorbeeld bij het exporteren van dieptemaps of andere gegevensspecifieke bewerkingen).

### ![](/icons/denoise.webp) Ruisonderdrukking (oidn) {#oidn}

Past ruisonderdrukking toe op het beeld zodra alle frames zijn verzameld. Zo kun je met veel minder samples werken. Ruisonderdrukking vraagt veel van de processor, dus zet het alleen aan als je beeld korrelig is. Het is niet op elk apparaat beschikbaar.

## Presetbrowser {#preset-browser}
![](/images/postprocess_presets.webp)
Klik op de afbeelding onder de titel `Nabewerking` om een verzameling nabewerkingspresets te tonen. Met `Nieuw` maak je een preset van je huidige instellingen. De ingebouwde presets kun je alleen klonen: wil je je eigen preset, kies er dan een, klik op `Klonen` en pas hem aan. Heeft een preset wijzigingen die nog niet zijn opgeslagen, dan staat er `Niet-opgeslagen wijzigingen!`; om op te slaan klik je op de presetafbeelding, klik je nogmaals in de presetbrowser en kies je `Opslaan`.

## Snelkoppelingsbalk {#shortcut-bar}
Staat de nabewerking aan, dan toont een balk onderaan het menu alle effecten (`SSR`, `SSGI`, `SSAO`, `DoF`, `Bloom`...). Tik op een effect om naar zijn sectie te springen. Uitgeschakelde effecten zijn grijs, dus de balk geeft ook in één oogopslag weer wat de huidige preset doet.

## ![](/icons/postprocess_ssr.webp) Reflectie (SSR) {#reflection-ssr}
Met deze optie kunnen objecten andere objecten in de scène weerspiegelen, zolang die objecten op het scherm zichtbaar zijn.
Heb je metalen en glanzende objecten in je scène, dan is deze optie waarschijnlijk een goed idee.
Deze optie vereist de shadingmodus [Verlicht (PBR)](shading.md#pbr).


| SSR uit                    | SSR aan                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Globale verlichting (SSGI) {#global-illumination-ssgi}

Globale verlichting bootst na hoe licht tussen oppervlakken weerkaatst: een rode muur kleurt bijvoorbeeld een wit object ernaast rood. In combinatie met omgevingsocclusie en reflecties kan dit een render veel realistischer maken. Net als reflecties vereist het de shadingmodus [Verlicht (PBR)](shading.md#pbr).

`Sterkte` - De intensiteit van de globale verlichting.



| SSGI uit                   | SSGI aan                  |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Een spotlicht staat achter de bol, gericht op het plafond. Met SSGI uit is alleen het plafond verlicht. Met SSGI aan weerkaatst het licht van het plafond naar de muren en naar de bol._

## ![](/icons/postprocess_ssao.webp) Omgevingsocclusie (SSAO) {#ambient-occlusion-ssao}
Omgevingsocclusie maakt plekken donkerder waar het licht minder makkelijk komt (hoeken enzovoort).
Het effect hangt alleen af van de geometrie van het model.

* `Sterkte` - Intensiteit van het effect.
* `Grootte` - Hoe ver het effect zich uitstrekt.
* `Dikte` - Welke dikte wordt aangenomen voor de afdekkende delen, als percentage van de `Grootte`.
* `Tint` - Een kleur die met de occlusie wordt vermenigvuldigd, voor creatieve effecten.


| SSAO uit                    | SSAO aan                   |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO is het best zichtbaar op plekken die vooral door omgevingslicht worden verlicht. Plekken onder sterk direct licht krijgen een veel zwakker AO-effect.

:::

## ![](/icons/postprocess_dof.webp) Scherptediepte {#depth-of-field-dof}
Voegt vervaging toe aan het gebied buiten de focus.

Tik gewoon op je model om het focuspunt te verplaatsen.

* `Diafragmamodus` - Stuurt de vervaging aan met één camera-diafragma, in plaats van met de twee vervagingsregelaars hieronder.
* `Diafragma` (_alleen in diafragmamodus_) - Het f-getal van de lens, zoals op een echte camera. Een lagere waarde opent de lens en geeft meer vervaging.
* `Verre vervaging` - Hoeveel vervaging er wordt toegepast achter het focuspunt.
* `Nabije vervaging` - Hoeveel vervaging er wordt toegepast tussen het focuspunt en de camera.


| DOF uit                   | DOF focus op verre ring     | DOF focus op nabije ring   |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Bloom {#bloom}
Bloom laat de heldere delen van je scène gloeien.

* `Intensiteit` - sterkte van het effect.
* `Radius` - hoe ver het effect zich verspreidt.
* `Drempel` - Hoe helder pixels in de scène moeten zijn voordat ze gaan gloeien. Bij 0 gloeit alles; bij een hoge waarde gloeien alleen de helderste pixels.
* `Tint` - een kleur die je aan de bloom kunt toevoegen voor creatieve effecten.

| Bloom uit                    | Bloom met radius 0          | Bloom met radius 1          |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Toonmapping {#tone-mapping}
Toonmapping zet HDR-waarden om naar het bereik `[0, 1]`.
Gebruik je het niet (of kies je `Geen`), dan wordt elke kleurcomponent boven 1 afgekapt.
Alle kleurvariaties boven dat bereik gaan dan verloren.

* `Geen/Neutraal/Agx/ACES` - welke tonemapper je gebruikt. `Geen` past niets aan (maar de andere regelaars werken nog wel). De andere opties zijn te vergelijken met verschillende soorten film: ze gaan elk op hun eigen manier om met overbelichte waarden en kleuren. Dit is een heel diep onderwerp: zoek op toonmapping, Agx en ACES voor meer informatie!
* `Belichting` - de algemene helderheid van het beeld, te vergelijken met het diafragma van een camera. Een snelle manier om een beeld in zijn geheel lichter of donkerder te maken.
* `Verzadiging` - kleursterkte. 1 is neutraal, 0 is zwart-wit, waarden boven 1 worden steeds verzadigder.
* `Contrast` - Maakt donkere delen donkerder en lichte delen lichter. Gebruik het voorzichtig: bij hoge waarden kan het artefacten geven.

Merk op dat met `Toonmapping` uit sommige details verdwijnen omdat de pixels te helder zijn.

| Toonmapping uit             | Toonmapping aan            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Toonmapping kan het effect van globale verlichting versterken. Zet je de intensiteit van de omgevingsmap lager en de belangrijkste lichtbron hoger, dan kun je de `Belichting` van de toonmapping verhogen om meer van het weerkaatste licht te zien.
:::

## ![](/icons/postprocess_tone_curve.webp) Kleurbewerking {#color-grading}
Net als het curvengereedschap in Photoshop regel je hiermee de balans en verdeling van de kleuren in het beeld. De regelaar `Hoofd` beïnvloedt de totale kleurbalans, met `Rood`/`Groen`/`Blauw` stel je het nauwkeuriger af.

| Kleurbewerking uit            | Kleurbewerking aan           |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Kromming {#curvature}
Spoort plekken op waar de kromming snel verandert en geeft die een kleur.

* `Factor` - algemene intensiteit van het effect
* `Uitstulping` - hoe sterk scherpe bolle overgangen worden opgespoord en in de gekozen kleur worden gezet (standaard wit)
* `Holte` - hoe sterk holle overgangen worden opgespoord en in de gekozen kleur worden gezet (standaard zwart)
* `Dikte` - hoe breed de opgespoorde randen zijn.

Naast `Uitstulping` en `Holte` kies je met een kleurvakje de kleur, en met een klein knopje hoe die kleur met het beeld mengt.


| Kromming uit                     | Kromming aan                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Chromatische Aberratie {#chromatic-aberration}
Bootst lensfouten na waarbij het licht aan de randen van het scherm uiteenvalt.

* `Sterkte` - hoe ver de rode, groene en blauwe delen van het beeld naar de schermranden toe uit elkaar gaan

| Chromatisch uit               | Chromatisch aan              |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vignet {#vignette}
Bootst lensfouten na door de randen van het scherm donkerder te maken.

* `Grootte` - De grootte van een omgekeerde ellips over het beeld
* `Hardheid` - Hoe wazig of scherp de ellips over het beeld wordt gemengd.
* `Tint` - De kleur van het vignet, standaard zwart.


| Vignet uit                      | Vignet aan                     |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Korrel {#grain}
Voegt een korreleffect toe, waardoor het beeld wat minder kunstmatig kan ogen.

* `Sterkte` - hoeveel korrel of ruis aan het beeld wordt toegevoegd.


| Korrel uit                   | Korrel aan                 |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Scherpte {#sharpness}
Een verscherpingseffect zoals in Photoshop of in fotobewerkingsapps.

* `Sterkte` - hoeveel het beeld wordt verscherpt.


| Scherpte uit                   | Scherpte aan                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixelart {#pixel-art}
Bootst de pixelart van retrogames na. Dit effect overschrijft de [Renderresolutie](#resolution-multiplier).

* `Schuifregelaar` - grootte van de pixels
* `Frame-sampling toestaan` - krijg je veel zwarte pixels, zet dit dan aan. Zonder deze optie schakelt het pixelart-effect de [frame-sampling](#max-frame-sampling) uit.

| Pixels uit                  | Pixels aan                 |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Scanlijn {#scanline}
Bootst het uiterlijk van oude CRT-monitoren na.

* `Factor` - sterkte van de lijnen
* `Tussenruimte` - grootte van de lijnen

| Scanlijn uit                   | Scanlijn aan                  |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
