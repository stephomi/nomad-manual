# ![](/icons/postprocess.webp) Post-traitement {#post-process}

Ce menu contrôle de nombreux aspects de Nomad qui affectent l’apparence du rendu.

![](/images/postprocess_overview_drac.webp)

L’utilisation du post-traitement peut modifier considérablement le rendu final de votre scène.

![](/images/postprocess_overview.webp)
*La même scène avant et après post-traitement, sans éclairages supplémentaires ni changements de matériaux.*

Le post-traitement peut avoir un impact important sur les performances selon votre appareil.
Il existe une case à cocher globale pour désactiver tout le post-traitement, afin que vous puissiez rapidement revenir à la sculpture/modélisation sans perdre vos préréglages.
Pour le rendu PBR, [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) et [Tone Mapping](#tone-mapping) doivent être activés.

Cependant, la plupart du temps, vous voudrez que le post-traitement soit désactivé lorsque vous sculptez, afin de vous concentrer sur la forme même du rendu.


## Qualité {#quality}

![](/images/postprocess_quality.webp)
### Échantillonnage maximal par image {#max-frame-sampling}
Nomad calculera une certaine quantité de post-traitement pour un rendu d’image unique, ce qui peut paraître bruité. Ce contrôle détermine combien d’images seront rendues puis fusionnées pour supprimer la plupart des artefacts de bruit. Certains effets ne nécessitent aucun échantillon supplémentaire (par ex. le color grading), tandis que d’autres comme l’illumination globale peuvent nécessiter des centaines d’échantillons pour être sans bruit. 

Dans la vue 3D, cela se voit lorsque Nomad est laissé au repos : la qualité de l’image se raffine progressivement jusqu’au nombre maximal d’échantillons, puis s’arrête. Ce nombre de calculs est également utilisé dans la section de rendu du [menu Files](files) lorsque « export png » est cliqué.

### Multiplicateur de résolution {#resolution-multiplier}
Ce curseur contrôle la résolution du post-traitement. Une valeur de x1.0 signifie que les rendus sont effectués à la résolution en pixels de l’appareil. Une valeur de x0.5 rendra à une demi-résolution, ce qui sera rapide mais de faible qualité. Une valeur supérieure à 1 rendra à une taille plus grande, puis réduira l’image. Il en résulte une qualité plus élevée, moins de bruit, mais des temps de rendu plus longs.

### Échantillons maximum {#max-samples}

Cela augmentera la qualité du post-traitement, mais en général `Full resolution` aura plus d’impact. 

### Denoiser (oidn) {#oidn}

Applique un débruiteur à l’image. Cela peut vous permettre d’utiliser un nombre d’échantillons bien plus faible. Cela ne fonctionne que si `Full Resolution` est activé. Notez que le débruitage se produit après que tous les échantillons ont été calculés, et peut être exigeant pour le processeur.

## Navigateur de préréglages {#preset-browser}
![](/images/postprocess_presets.webp)
Cliquer sur l’image affichera une collection de préréglages de post-traitement. Pour définir vos propres préréglages, sélectionnez-en un, cliquez sur « clone », faites vos modifications. Pour enregistrer, cliquez sur l’image du préréglage, cliquez à nouveau dans le navigateur de préréglages, puis choisissez « save ».


## Réflexion (SSR) {#reflection-ssr}
Avec cette option, les objets peuvent refléter d’autres objets de la scène, tant que ces objets sont visibles à l’écran.
Si vous avez des objets métalliques et brillants dans votre scène, cette option devrait probablement être utilisée.
Cette option n’est efficace qu’en mode PBR.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Illumination globale (SSGI) {#global-illumination-ssgi}

L’illumination globale simule la façon dont la lumière rebondit entre les surfaces, par ex. un mur rouge projettera du rouge sur un objet blanc proche. Cela peut grandement améliorer le réalisme d’un rendu lorsqu’il est utilisé avec l’occlusion ambiante et les réflexions. 

`Strength` - L’intensité de l’illumination globale. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Un projecteur est placé derrière la sphère, dirigé vers le plafond. Avec SSGI désactivé, seul le plafond est éclairé. Avec SSGI activé, la lumière rebondit du plafond vers les murs puis vers la sphère._

## Occlusion ambiante (SSAO) {#ambient-occlusion-ssao}
L’occlusion ambiante assombrit les zones où la lumière a moins de chances d’atteindre (coins, etc.).
L’effet ne dépend que de la géométrie du modèle.

* `Strength`- Intensité de l’effet.
* `Size`- Ampleur de l’effet.
* `Curvature bias` - Sensibilité de l’effet par rapport aux variations de surface.
* `Color` - Une teinte multipliée dans l’occlusion, utilisée pour des effets créatifs.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
L’AO sera la plus visible dans les zones principalement éclairées par la lumière d’environnement. Les zones sous une lumière directe forte recevront un effet d’AO beaucoup plus faible.

:::

## Profondeur de champ (DOF) {#depth-of-field-dof}
Ajoute un effet de flou sur les régions situées en dehors de la zone de mise au point.

Touchez simplement votre modèle pour changer le point de focus.

* `Far blur` - Quantité de flou appliquée au-delà du point de focus.
* `Near blur` - Quantité de flou appliquée entre le point de focus et la caméra.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Bloom {#bloom}
Le bloom fera briller les zones lumineuses de votre scène.

* `Intensity` - Intensité de l’effet.
* `Radius` - L’étendue de l’effet.
* `Threshold` - À quel point les pixels doivent être lumineux dans la scène avant de commencer à produire du bloom. Une valeur basse fera tout briller, une valeur élevée ne laissera briller que les pixels les plus lumineux.
* `Color` - Une teinte qui peut être ajoutée au bloom pour des effets créatifs.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Mappage de ton {#tone-mapping}
Le Tone Mapping est une opération qui remappe les valeurs HDR dans l’intervalle `[0, 1]`.
Si vous ne l’utilisez pas (ou sélectionnez `none`), toute composante de couleur supérieure à 1 sera écrêtée.
Toute variation de couleur au-dessus de cette plage sera alors perdue.

* `None/Neutral/Agx/ACES` - quel tonemapper utiliser. `None` ne fait aucun remappage (mais les autres contrôles fonctionnent toujours). Les autres options sont similaires au choix d’une pellicule différente : elles gèrent les valeurs et couleurs surexposées de différentes manières. C’est un sujet très vaste, recherchez tone mapping, Agx, ACES pour plus d’informations !
* `Exposure` - Luminosité globale de l’image, similaire au réglage de l’ouverture sur un appareil photo. Cela peut être un moyen rapide d’éclaircir ou d’assombrir globalement une image.
* `Saturation` - Force des couleurs. 1 est neutre, 0 est monochrome, des valeurs supérieures à 1 sont de plus en plus saturées.
* `Contrast` - Rend les zones sombres plus sombres et les zones claires plus claires. À utiliser avec précaution, car il peut introduire des artefacts à des valeurs élevées.

Remarquez qu’avec le `Tone Mapping` désactivé, certains détails disparaissent parce que les pixels sont trop lumineux.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Le tone mapping peut renforcer l’effet de l’illumination globale. Si vous baissez l’intensité de la carte d’environnement, augmentez la source de lumière principale, puis augmentez l’`exposure` du tone mapping pour voir davantage les effets de lumière rebondie.
:::

## Étallonage des couleurs {#color-grading}
Similaire à l’outil de courbes dans Photoshop, cela vous permet de contrôler l’équilibre et la répartition des couleurs dans l’image. Le contrôle `main` affecte l’équilibre global des couleurs, les contrôles `red`/`green`/`blue` permettent un réglage fin. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Courbure {#curvature}
Détecte les zones où la courbure change rapidement et applique une couleur à ces régions.

* `Factor` - Intensité globale de l’effet
* `Bump` - À quel point il détectera les changements convexes marqués et placera la couleur sélectionnée à ces endroits (blanc par défaut)
* `Cavity` - À quel point il détectera les changements concaves et placera la couleur sélectionnée à ces endroits (noir par défaut)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Aberration chromatique {#chromatic-aberration}
Simule les artefacts d’optique avec la lumière décomposée autour des bords de l’écran.

* `Strength` - À quel point les parties rouge/vert/bleu de l’image sont séparées vers les bords de l’écran

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignettage {#vignette}
Simule les artefacts d’optique en assombrissant les bords de l’écran.

* `Size` - La taille d’une ellipse inversée placée sur l’image
* `Hardness` - À quel point l’ellipse est floue ou nette lorsqu’elle est mélangée par-dessus l’image.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain {#grain}
Ajoute un effet de grain, ce qui peut aider à rendre l’image un peu moins artificielle.

* `Strength` - La quantité de grain/bruit ajoutée à l’image.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Netteté {#sharpness}
Un effet de netteté similaire à celui de Photoshop ou des applications de traitement photo.

* `Strength` - La quantité de netteté appliquée à l’image.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel art {#pixel-art}
Simule le pixel art des jeux rétro.

* `Slider` - Taille des pixels
* `Allow frame sampling` - si vous obtenez beaucoup de pixels noirs, essayez d’activer cette option, qui remplacera l’échantillonnage par défaut.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Ligne de balayage {#scanline}
Simule l’apparence des anciens moniteurs CRT.

* `Factor` - Intensité des lignes
* `Spacing` - Taille des lignes

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Tramage {#dithering}

Trame les pixels pour réduire les artefacts de banding. En général, cela devrait être activé, mais peut être désactivé pour des opérations spécifiques (par ex. l’export de cartes de profondeur ou d’autres opérations spécifiques aux données).