# ![](/icons/paint.webp) Peinture {#painting}

Contrôler la couleur, la rugosité, la métallité des coups de pinceau, permettre le remplissage global des attributs de peinture, et définir la façon dont les outils de peinture interagissent avec les calques, masques et sélections masquées.

![](/images/paint_overview.webp)  

## Vue d’ensemble {#overview}

Nomad utilise la peinture de sommets PBR. Qu’est‑ce que cela signifie ?

### PBR {#pbr}
PBR, ou Physically Based Rendering (rendu physiquement réaliste), est une technique de graphisme très répandue pour le cinéma, la télévision, les jeux et le mobile. En basant les lumières sur des propriétés physiques et en définissant les surfaces via la couleur, la rugosité et la métallité, on peut obtenir une grande variété de rendus photoréalistes.

### Peinture de sommets {#vertex-painting}

La peinture de sommets signifie que les informations de peinture sont stockées dans les sommets du modèle, plutôt que dans des textures. Comme Nomad peut gérer des modèles comportant des centaines de milliers, voire souvent des millions de sommets, vos modèles devraient pouvoir avoir une peinture de surface très détaillée ; si vous pouvez sculpter le détail, vous pouvez aussi le peindre.

Cela signifie également que peindre dans Nomad ne nécessite pas de dépliage UV, souvent un processus lent et technique dans d’autres applications 3D. Beaucoup d’autres applications 3D ne prennent pas en charge les nombres de sommets élevés que Nomad peut gérer, cependant Nomad dispose aussi de bons outils de cuisson de textures et de décimation pour aider.

### Texturation {#texturing}

Nomad prend en charge les textures, mais elles doivent être présentes dans un modèle importé, ou via la cuisson de la peinture de sommets vers des textures. 

Une texture est simplement une image, mais dans le contexte 3D elle fait généralement référence à une image assignée à un objet.
Pour enrouler une image autour d’un modèle, le modèle a besoin de coordonnées de texture (UV).

Nomad peut [les calculer automatiquement](topology.md#uv-unwrap) mais vous n’avez pas beaucoup de contrôle sur la qualité globale.

::: tip
Exemple de flux de travail :
- Sculpter dans Nomad, puis faire un [dépliage UV](topology.md#uv-unwrap)
- Si vous avez déjà commencé à peindre dans Nomad, vous pouvez [transférer la peinture de sommets vers des textures](topology.md#bake-vertex-colors-to-texture)
- Exporter vers Procreate
- Texturer dans Procreate
- Ré‑exporter vers Nomad pour le rendu
:::

Voilà pour la vue d’ensemble, explorons maintenant les sections du menu de peinture :


## Peinture par traits {#stroke-painting}
![](/images/paint_intensity.webp)  

Active la peinture pour cet outil, utile si vous avez besoin de sculpter et peindre en même temps.

Pour les outils dont la fonction principale est la peinture (par ex. Paint, Smudge, Mask), cette case à cocher n’existe pas.

### Intensité de la peinture {#paint-intensity}

Un curseur vous permet d’utiliser une intensité différente de l’intensité principale de l’outil.

Les cases `Alpha`, `Falloff` et `Randomize` déterminent si ces fonctions affecteront la peinture. Par exemple, vous pouvez avoir l’aléatoire activé pour l’outil Clay, mais la couleur ne sera pas randomisée.


## Matériau {#material}
![](/images/paint_material.webp) 

La première icône est une forme d’aperçu de matériau. En faisant glisser sur l’aperçu 3D du matériau, vous le faites pivoter. 

La deuxième icône est un aperçu du trait de peinture avec l’alpha et le falloff sélectionnés.

Le bouton d’aperçu à côté du titre Material permet d’alterner entre None, Material ou Triplanar. Cela détermine ce qui se passe lorsque vous modifiez interactivement les propriétés de peinture :

* `None` - Aucun aperçu ne sera affiché sur le modèle lorsque vous ajustez les propriétés
* `Material` - Les valeurs du matériau seront prévisualisées sur l’objet lorsque vous ajustez les propriétés. Si vous utilisez des textures et que le modèle possède des UV, les UV seront utilisés.
* `Triplanar` - Le matériau sera prévisualisé en projection triplanaire. 

La pipette peut être utilisée pour échantillonner toutes les propriétés d’un objet dans votre scène.

## Préréglages de matériau {#material-presets}
Un appui sur la forme d’aperçu 3D ouvre un menu de presets de matériaux, qui peuvent être clonés pour définir vos propres presets.

![](/images/paint_presets.webp) 

Les bascules `Embed Textures` et `Alpha`, lorsqu’elles sont activées, stockent toutes les textures utilisées par ce matériau dans le preset. Ceci est expliqué plus en détail ci‑dessous.

## Curseurs PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

La peinture [PBR](shading.md#pbr) utilise 4 canaux :
- `Color` La couleur qui sera peinte. La pipette peut être utilisée pour sélectionner une couleur à partir d’autres parties du modèle ou d’images de référence.
- `Roughness` Indique à quel point une surface est « rugueuse » ou « lisse ». Une valeur faible de rugosité signifie que les reflets seront nets.
- `Metalness` Indique simplement si la surface est métallique ou non. La valeur devrait être soit 0 % soit 100 % la plupart du temps, les valeurs intermédiaires devraient rester exceptionnelles.
- `Opacity` À quel point le matériau est transparent. Strictement parlant, cela ne fait pas partie de la spécification PBR, mais c’est utile dans de nombreuses situations. 1 est totalement opaque, 0 est transparent. Notez que l’opacité et la réfraction sont des choses différentes, la réfraction dans Nomad est gérée via le matériau de réfraction. 

Si vous sélectionnez un preset de matériau, 3 canaux sont peints simultanément (l’opacité est souvent volontairement exclue). Cela signifie qu’au lieu de simplement peindre du « rouge », vous pouvez peindre « un métal rouge rugueux » ou « un plastique blanc lisse ».

Le carré est un emplacement de texture, cliquez dessus pour utiliser une texture pour cette propriété au lieu d’une valeur unie.

L’icône de pinceau à côté des curseurs remplira cette propriété sur tout votre objet.

La case à cocher active ou désactive cette propriété particulière, vous pouvez donc ne peindre que la couleur, ou seulement la rugosité et l’opacité, par exemple. 

Voici quelques exemples de différentes propriétés de rugosité et de métallité :

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Seule la couleur est prise en charge en mode [Matcap rendering](shading.md#matcap), la métallité et la rugosité sont ignorées.
:::

::: tip
Lorsque vous utilisez des textures pour la peinture PBR, il est souvent utile de passer à un outil comme `Stamp`, ou d’utiliser le menu Stroke pour choisir un mode autre que Dot, qui peut étaler la texture.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Vous pouvez envisager d’activer le `Smooth Shading` [globalement](settings.md#smooth-shading) ou [par objet](material.md#smooth-shading) si vous peignez une surface métallique sur un objet avec un faible nombre de polygones.
:::

## Tout peindre {#paint-all}

![](/images/paint_paint_all.webp)

Applique le matériau actuel à l’objet, soit en mode standard avec « Paint All », soit en projection triplanaire.

Les cases à cocher à côté des curseurs de couleur/métallité/rugosité/opacité sont respectées, toute propriété désactivée ne sera pas remplie.

Les boutons supplémentaires contrôlent la façon dont le Paint All peut être encore modifié :

| Icône                        | Description                                      |
| :-------------------------: | :----------------------------------------------: |
| ![](/icons/tool_mask.webp) | Les zones masquées ne seront pas affectées.      |
| ![](/icons/tool_hide.webp) | Les zones cachées ne seront pas affectées.       |
| ![](/icons/opacity.webp)   | Utiliser le facteur de peinture de l’outil ci‑dessus. |
| ![](/icons/layer.webp)     | Les zones non peintes d’un calque ne seront pas affectées. |
| ![](/icons/triplanar.webp) | Indicateur des paramètres triplanaires          |
| ![](/icons/cog.webp)       | Ouvrir les paramètres Triplanar                 |

### Paramètres triplanaires {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Similaire aux [paramètres triplanaires du menu Material](material.md#triplanar), vous pouvez contrôler le mélange des projections, le tiling et les décalages. 

Utilisez la case d’aperçu en haut de ce menu pour activer un aperçu persistant pendant l’ajustement des valeurs.

## Matériau global {#global-material}
Si cette option est activée, le matériau sélectionné sera le même que pour les autres outils. Notez qu’elle ne prend en compte que les réglages de rugosité, métallité et couleur.