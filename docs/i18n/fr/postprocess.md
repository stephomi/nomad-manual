# ![](/icons/postprocess.webp) Post-traitement {#post-process}

Ce menu règle de nombreux aspects de Nomad qui influencent l'apparence du rendu.

![](/images/postprocess_overview_drac.webp)

Le post-traitement peut changer considérablement l'aspect final de votre scène.

![](/images/postprocess_overview.webp)
*La même scène avant et après post-traitement, sans lumière supplémentaire ni changement de matériau.*

Selon votre appareil, le post-traitement peut beaucoup peser sur les performances.
Une case `Post-traitement` globale désactive tout le post-traitement, pour revenir rapidement à la sculpture ou à la modélisation sans perdre vos préréglages.
Pour le rendu PBR, l'[Occlusion ambiante](#ambient-occlusion-ssao), la [Réflexion](#reflection-ssr) et le [Mappage tonal](#tone-mapping) devraient être activés.

Cependant, la plupart du temps, mieux vaut désactiver le post-traitement quand vous sculptez, pour vous concentrer sur la forme elle-même plutôt que sur le rendu.


## Qualité {#quality}

![](/images/postprocess_quality.webp)

Ces options améliorent la qualité du rendu, au détriment des performances.

### Max. d'images accumulées {#max-frame-sampling}
Pour le rendu d'une seule image, Nomad ne calcule qu'une partie du post-traitement, ce qui peut donner un résultat bruité. Ce réglage détermine combien d'images sont rendues puis fondues ensemble pour supprimer la plupart des artefacts de bruit. Certains effets n'ont besoin d'aucun échantillon supplémentaire (par exemple l'étalonnage), tandis que d'autres, comme les ombres douces et l'illumination globale, peuvent demander des centaines d'échantillons pour ne plus être bruités. 

Dans la vue, vous le voyez dès que vous laissez Nomad tranquille : la qualité de l'image s'affine progressivement jusqu'au maximum d'échantillons, puis s'arrête. Une fois arrêté, Nomad ne fait plus rien, ce qui économise la batterie. Ce nombre de calculs est aussi utilisé dans la section rendu du [menu Fichiers](files) quand vous exportez en PNG.

La case à côté du curseur active ou désactive l'accumulation d'images.

### Résolution de rendu {#resolution-multiplier}
Ce curseur règle la résolution du rendu. Une valeur de x1.0 signifie que le rendu se fait à la résolution en pixels de l'appareil. Une valeur de x0.5 rend à mi-résolution, ce qui est rapide mais de faible qualité. Une valeur supérieure à 1 rend à une taille plus grande, puis réduit l'image. Le résultat est de meilleure qualité et moins bruité, mais le rendu prend plus de temps.

Ce réglage a un fort impact sur les performances, essayez donc de rester à x1.25 ou moins. Cette valeur n'est pas enregistrée dans les réglages, et l'effet [Pixel Art](#pixel-art) la remplace.

### ![](/icons/intensity.webp) Nombre max. d'échantillons {#max-samples}

Améliore la qualité des effets de post-traitement, au détriment des performances.

### ![](/icons/material_dithering.webp) Tramage {#dithering}

Trame les pixels pour réduire les effets de bandes (dans les dégradés ou le vignettage, par exemple). Il est généralement activé, mais vous pouvez le désactiver pour certaines opérations précises (par exemple l'export de cartes de profondeur ou d'autres données).

### ![](/icons/denoise.webp) Filtre anti-bruit (oidn) {#oidn}

Applique un filtre anti-bruit à l'image une fois toutes les images accumulées. Cela vous permet d'utiliser beaucoup moins d'échantillons. Le débruitage sollicite beaucoup le processeur : ne l'activez que si votre image est bruitée. Il n'est pas disponible sur tous les appareils.

## Navigateur de préréglages {#preset-browser}
![](/images/postprocess_presets.webp)
Toucher l'image sous le titre `Post-traitement` affiche une collection de préréglages de post-traitement. Utilisez `Nouveau` pour créer un préréglage à partir de vos réglages actuels. Les préréglages intégrés peuvent seulement être clonés : pour créer le vôtre, sélectionnez-en un, touchez `Cloner`, puis faites vos modifications. Quand un préréglage a des modifications pas encore enregistrées, il affiche `Modifications non enregistrées !` ; pour l'enregistrer, touchez l'image du préréglage, touchez à nouveau à l'intérieur du navigateur de préréglages, et choisissez `Enregistrer`.

## Barre de raccourcis {#shortcut-bar}
Quand le post-traitement est activé, une barre en bas du menu liste tous les effets (`SSR`, `SSGI`, `SSAO`, `DoF`, `Éclat`...). Touchez-en un pour aller à sa section. Les effets désactivés sont grisés : la barre résume donc aussi en un coup d'œil ce que fait le préréglage actuel.

## ![](/icons/postprocess_ssr.webp) Réflexion (SSR) {#reflection-ssr}
Avec cette option, les objets peuvent refléter les autres objets de la scène, à condition que ceux-ci soient visibles à l'écran.
Si votre scène contient des objets métalliques et brillants, il vaut sans doute mieux l'activer.
Cette option nécessite le mode d'ombrage [Éclairé (PBR)](shading.md#pbr).


| SSR désactivé              | SSR activé                |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Illumination globale (SSGI) {#global-illumination-ssgi}

L'illumination globale simule le rebond de la lumière d'une surface à l'autre : par exemple, un mur rouge projette du rouge sur un objet blanc proche. Associée à l'occlusion ambiante et aux réflexions, elle peut énormément renforcer le réalisme d'un rendu. Comme les réflexions, elle nécessite le mode d'ombrage [Éclairé (PBR)](shading.md#pbr).

`Force` - L'intensité de l'illumination globale. 



| SSGI désactivé             | SSGI activé               |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Un spot est placé derrière la sphère, dirigé vers le plafond. Sans SSGI, seul le plafond est éclairé. Avec SSGI, la lumière rebondit du plafond sur les murs, puis sur la sphère._

## ![](/icons/postprocess_ssao.webp) Occlusion ambiante (SSAO) {#ambient-occlusion-ssao}
L'occlusion ambiante assombrit les zones que la lumière a moins de chances d'atteindre (les coins, etc.).
L'effet ne dépend que de la géométrie du modèle.

* `Force` - L'intensité de l'effet.
* `Taille` - L'étendue de l'effet.
* `Épaisseur` - L'épaisseur supposée des objets qui font de l'ombre, en pourcentage de la `Taille`.
* `Teinte` - Une couleur multipliée avec l'occlusion, pour des effets créatifs.


| SSAO désactivé              | SSAO activé                |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
L'occlusion ambiante est surtout visible dans les zones éclairées principalement par la lumière de l'environnement. Les zones sous une forte lumière directe reçoivent un effet beaucoup plus faible.

:::

## ![](/icons/postprocess_dof.webp) Profondeur de champ {#depth-of-field-dof}
Ajoute un flou sur les zones en dehors de la mise au point.

Touchez simplement votre modèle pour changer le point de mise au point.

* `Mode d’ouverture` - Pilote le flou avec une seule ouverture d'objectif, au lieu des deux curseurs de flou ci-dessous.
* `Ouverture` (_mode d'ouverture uniquement_) - Le nombre f de l'objectif, comme sur un vrai appareil photo. Une valeur plus faible ouvre l'objectif et floute davantage.
* `Flou lointain` - La quantité de flou appliquée au-delà du point de mise au point.
* `Flou proche` - La quantité de flou appliquée entre le point de mise au point et la caméra.


| Profondeur de champ désactivée | Mise au point sur l'anneau lointain | Mise au point sur l'anneau proche |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Éclat {#bloom}
L'éclat fait briller les zones lumineuses de votre scène.

* `Intensité` - la force de l'effet.
* `Rayon` - l'étendue de l'effet.
* `Seuil` - la luminosité que doivent atteindre les pixels de la scène pour commencer à briller. À 0, tout brille ; une valeur élevée ne fait briller que les pixels les plus lumineux.
* `Teinte` - une couleur ajoutée à l'éclat pour des effets créatifs.

| Éclat désactivé              | Éclat avec un rayon de 0    | Éclat avec un rayon de 1    |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Mappage tonal {#tone-mapping}
Le mappage tonal ramène les valeurs HDR dans l'intervalle `[0, 1]`.
Si vous ne l'utilisez pas (ou choisissez `Aucun`), toute composante de couleur supérieure à 1 est écrêtée.
Toutes les variations de couleur au-delà de cet intervalle sont alors perdues.

* `Aucun/Neutre/Agx/ACES` - le tonemapper à utiliser. `Aucun` ne fait aucune conversion (mais les autres réglages fonctionnent toujours). Les autres options reviennent à choisir différentes pellicules : elles traitent les valeurs surexposées et les couleurs de manières différentes. C'est un sujet très vaste, cherchez « tone mapping », Agx ou ACES pour en savoir plus !
* `Exposition` - la luminosité globale de l'image, comme quand on règle l'ouverture d'un appareil photo. C'est un moyen rapide d'éclaircir ou d'assombrir toute l'image.
* `Saturation` - la force des couleurs. 1 est neutre, 0 est monochrome, les valeurs au-dessus de 1 sont de plus en plus saturées.
* `Contraste` - Rend les sombres plus sombres et les clairs plus clairs. À utiliser avec prudence : des valeurs élevées peuvent créer des artefacts.

Remarquez qu'avec le `Mappage tonal` désactivé, certains détails disparaissent car les pixels sont trop lumineux.

| Mappage tonal désactivé     | Mappage tonal activé       |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Le mappage tonal peut renforcer l'effet de l'illumination globale. Si vous baissez l'intensité de la carte d'environnement et augmentez celle de la source de lumière principale, vous pouvez augmenter l'`Exposition` du mappage tonal pour mieux voir les effets de lumière rebondie.
:::

## ![](/icons/postprocess_tone_curve.webp) Étalonnage {#color-grading}
Comme l'outil Courbes de Photoshop, il vous permet de régler l'équilibre et la répartition des couleurs de l'image. La courbe `Principale` agit sur l'équilibre global des couleurs, les courbes `Rouge`/`Vert`/`Bleu` permettent un réglage fin. 

| Étalonnage désactivé          | Étalonnage activé            |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Courbure {#curvature}
Détecte les endroits où la courbure change brusquement, et y applique une couleur.

* `Facteur` - l'intensité globale de l'effet
* `Bosse` - à quel point l'effet détecte les changements convexes marqués, pour y placer la couleur choisie (blanc par défaut)
* `Creux` - à quel point l'effet détecte les changements concaves, pour y placer la couleur choisie (noir par défaut)
* `Épaisseur` - la largeur des arêtes détectées.

À côté de `Bosse` et de `Creux`, une pastille de couleur choisit la couleur, et un petit bouton choisit comment cette couleur se fond avec l'image.


| Courbure désactivée              | Courbure activée               |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberration chromatique {#chromatic-aberration}
Simule un défaut d'objectif qui décompose la lumière vers les bords de l'écran.

* `Force` - à quel point les composantes rouge, verte et bleue de l'image se séparent vers les bords de l'écran

| Aberration désactivée         | Aberration activée           |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vignettage {#vignette}
Simule un défaut d'objectif en assombrissant les bords de l'écran.

* `Taille` - La taille d'une ellipse inversée placée sur l'image
* `Dureté` - À quel point l'ellipse se fond de façon floue ou nette sur l'image.
* `Teinte` - La couleur du vignettage, noire par défaut.


| Vignettage désactivé            | Vignettage activé              |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Grain {#grain}
Ajoute un effet de grain, qui peut rendre l'image un peu moins artificielle.

* `Force` - la quantité de grain (de bruit) ajoutée à l'image.


| Grain désactivé              | Grain activé               |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Netteté {#sharpness}
Un effet de netteté semblable à celui de Photoshop ou des applications de retouche photo.

* `Force` - la quantité de netteté appliquée à l'image.


| Netteté désactivée             | Netteté activée              |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Simule le pixel art des jeux rétro. Cet effet remplace la [Résolution de rendu](#resolution-multiplier).

* `Curseur` - la taille des pixels
* `Autoriser l'accumulation` - si vous obtenez beaucoup de pixels noirs, essayez d'activer cette option. Sans elle, l'effet Pixel Art désactive l'[accumulation d'images](#max-frame-sampling).

| Pixel Art désactivé         | Pixel Art activé           |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Scanline {#scanline}
Simule l'aspect des vieux écrans cathodiques.

* `Facteur` - la force des lignes
* `Espacement` - la taille des lignes

| Scanline désactivé             | Scanline activé               |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
