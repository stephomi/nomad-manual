# ![](/icons/paint.webp) Peinture {#painting}

Réglez la couleur, la rugosité et la métallité des traits de peinture, remplissez tout un objet avec ces attributs, et choisissez comment les outils de peinture interagissent avec les calques, les masques et les zones cachées.

![](/images/paint_overview.webp)  

## Présentation {#overview}

Nomad utilise la peinture PBR aux sommets. Qu'est-ce que cela veut dire ?

### PBR {#pbr}
Le PBR, ou Physically Based Rendering (rendu basé sur la physique), est une technique d'image de synthèse très répandue au cinéma, à la télévision, dans les jeux vidéo et sur mobile. En basant l'éclairage sur des propriétés physiques, et en définissant les surfaces par leur couleur, leur rugosité et leur métallité, on obtient une grande variété de rendus photoréalistes.

### Peinture aux sommets {#vertex-painting}

La peinture aux sommets signifie que les informations de peinture sont stockées dans les sommets du modèle, plutôt que dans des textures. Comme Nomad sait gérer des modèles de centaines de milliers, souvent de millions de sommets, vos modèles peuvent avoir une peinture très détaillée : si vous pouvez sculpter un détail, vous pouvez aussi le peindre.

Cela veut aussi dire que peindre dans Nomad ne demande pas de dépliage UV, une étape souvent longue et technique dans les autres applications 3d. Beaucoup d'autres applications 3d ne supportent pas autant de sommets que Nomad, mais Nomad dispose aussi de bons outils de baking de textures et de décimation pour vous aider.

### Texturage {#texturing}

Nomad gère les textures, mais elles doivent être présentes dans un modèle importé, ou provenir du baking de la peinture aux sommets dans des textures. 

Une texture est simplement une image, mais dans le contexte de la 3d, le terme désigne généralement une image attribuée à un objet.
Pour envelopper un modèle d'une image, le modèle a besoin de coordonnées de texture (UV).

Nomad peut les [calculer automatiquement](topology.md#uv-unwrap), mais vous n'avez alors pas beaucoup de contrôle sur la qualité globale.

::: tip
Un exemple de méthode de travail :
- Sculptez dans Nomad, puis faites le [dépliage UV](topology.md#uv-unwrap)
- Si vous avez déjà commencé à peindre dans Nomad, vous pouvez [transférer la peinture aux sommets dans des textures](topology.md#bake-texture)
- Exportez vers Procreate
- Texturez dans Procreate
- Réimportez dans Nomad pour le rendu
:::

Voilà pour la présentation ; voyons maintenant les sections du menu Peinture :


## Peinture du trait {#stroke-painting}
![](/images/paint_intensity.webp)  

Active la peinture pour cet outil, pratique si vous voulez sculpter et peindre en même temps. Quand un outil peut peindre mais que cette case est décochée, une icône d'avertissement à côté du titre vous le rappelle.

Pour les outils dont la fonction principale est de peindre (par exemple Peindre, Estomper, Masque), cette case n'existe pas.

### ![](/icons/opacity.webp) Intensité de la peinture {#paint-intensity}

Un curseur qui vous permet d'utiliser une intensité différente de l'intensité principale de l'outil.

Le bouton de curseurs à côté ajoute un curseur rapide d'intensité de la peinture dans la barre latérale, pour les outils qui sculptent et peignent en même temps.

Les boutons `Alpha`, `Atténuation` et `Intensité aléatoire` déterminent si ces fonctions s'appliquent à la peinture. Par exemple, l'aléatoire peut être activé pour l'outil Argile sans que la couleur soit rendue aléatoire.

* `Alpha` - désactivé, la peinture ignore l'alpha et couvre toute la zone du pinceau. Avec l'outil VDM, ce bouton est remplacé par `Matériau du tampon`, qui active ou désactive le matériau stocké dans le tampon.
* `Atténuation` - désactivé, la peinture reste à pleine intensité jusqu'au bord du pinceau.
* `Intensité aléatoire` - indique si la partie intensité de l'aléatoire du trait s'applique à la peinture. L'aléatoire de position, de rotation et d'échelle déplace toujours le tampon entier.

Ces options sont ignorées par [Tout peindre](#paint-all), mais sa variante triplanaire utilise l'alpha.

### ![](/icons/link.webp) Matériau global {#global-material}
Si cette option est activée, le matériau sélectionné est le même que pour les autres outils. Notez qu'elle ne prend en compte que les réglages de rugosité, de métallité et de couleur. Désactivez-la pour donner à cet outil son propre matériau.


## Matériau {#material}
![](/images/paint_material.webp) 

La première icône est une forme d'aperçu du matériau. Faites glisser sur cet aperçu 3d pour le faire tourner. 

La deuxième icône est un aperçu du trait de peinture avec les options d'alpha et d'atténuation sélectionnées.

### ![](/icons/falloff.webp) Courbes {#curves}

Ouvre un éditeur de courbes pour les emplacements de texture des [curseurs PBR](#pbr-sliders). Il modifie les valeurs de la texture avant qu'elles soient peintes, sans toucher au fichier image. Une petite icône de courbe sur un emplacement de texture vous indique que sa courbe a été modifiée.

### ![](/icons/cog.webp) Options du matériau {#material-options}

Le bouton `Matériau` à côté du titre contient deux réglages.

`Aperçu du matériau` détermine ce qui se passe sur l'objet sélectionné pendant que vous modifiez les curseurs de couleur, de rugosité, de métallité, d'opacité et d'intensité :

* `Aucun` - Aucun aperçu n'est affiché sur le modèle quand vous ajustez les propriétés
* `Matériau` - Les valeurs du matériau sont prévisualisées sur l'objet quand vous ajustez les propriétés.
* `Triplanaire` - Le matériau est prévisualisé en projection triplanaire. 

Les cases de couleur, de rugosité, de métallité et d'opacité en dessous choisissent les canaux que remplace la [Pipette de matériau](#material-picker).

### ![](/icons/dropper.webp) Pipette de matériau {#material-picker}

La pipette prélève le matériau sous le curseur, sur n'importe quel objet de votre scène. Seuls les canaux cochés dans les [Options du matériau](#material-options) sont remplacés.

## Préréglages de matériau {#material-presets}
Toucher la forme d'aperçu 3d ouvre un menu de préréglages de matériaux, que vous pouvez cloner pour créer vos propres préréglages.

![](/images/paint_presets.webp) 

L'interrupteur `Incorporer les textures` enregistre une copie des textures utilisées par ce matériau dans le préréglage. Sans lui, le préréglage ne fait que référencer les textures du dossier textures/ de Nomad. Activez-le pour partager un préréglage texturé sans avoir à envoyer ses textures à part.

`Inclure l’alpha` enregistre aussi l'alpha du pinceau dans le préréglage de matériau.

## Curseurs PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

La peinture [PBR](shading.md#pbr) utilise 4 canaux :
- `Couleur` La couleur qui sera peinte. La pipette permet de prélever une couleur ailleurs sur le modèle, ou sur des images de référence.
- `Rugosité` Indique à quel point une surface est « rugueuse » ou « lisse ». Une rugosité faible donne des reflets nets.
- `Métallité` Indique simplement si la surface est métallique ou non. La valeur devrait être 0 % ou 100 % la plupart du temps ; les valeurs intermédiaires devraient rester exceptionnelles.
- `Opacité` À quel point on voit à travers le matériau. À proprement parler, elle ne fait pas partie de la spécification PBR, mais elle est utile dans bien des situations. 1 est totalement opaque, 0 est transparent. Notez que l'opacité et la réfraction sont deux choses différentes : dans Nomad, la réfraction passe par le matériau de réfraction. 

Si vous sélectionnez un préréglage de matériau, 3 canaux sont peints en même temps (l'opacité est souvent volontairement exclue). Ainsi, au lieu de peindre simplement du « rouge », vous pouvez peindre « un métal rouge rugueux » ou « un plastique blanc lisse ».

Le carré est un emplacement de texture : touchez-le pour utiliser une texture pour cette propriété au lieu d'une valeur unie. Une texture de couleur teinte la couleur, tandis qu'une texture de rugosité, de métallité ou d'opacité remplace la valeur du curseur (son libellé est alors barré pour l'indiquer). Pour la texture d'opacité, `Utiliser l’alpha comme valeur` lit le canal alpha de la texture au lieu de sa valeur en niveaux de gris.

Avec l'outil VDM, quand le tampon contient son propre matériau, un emplacement supplémentaire l'affiche à côté de l'emplacement de texture. Touchez-le pour utiliser ou ignorer ce canal du tampon.

L'icône de pinceau à côté des curseurs remplit tout votre objet avec cette propriété.

La case à cocher active ou désactive la propriété correspondante : vous pouvez par exemple ne peindre que la couleur, ou seulement la rugosité et l'opacité. 

Voici quelques exemples de différentes valeurs de rugosité et de métallité :

|                | Métallité 0 %                     | Métallité 100 %              |
| :------------: | :-------------------------------: | :--------------------------: |
| Rugosité 0 %   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Rugosité 50 %  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Rugosité 100 % | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
La rugosité et la métallité nécessitent le mode d'ombrage [Éclairé (PBR)](shading.md#pbr). En mode [MatCap](shading.md#matcap) ou [Sans éclairage](shading.md#unlit), elles sont ignorées et le menu affiche un avertissement.
:::

::: tip
Quand vous utilisez des textures pour la peinture PBR, il est souvent utile de passer à un outil comme `Tampon`, ou d'utiliser le menu Trait pour choisir un autre mode que le point, qui peut étaler la texture.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Pensez à activer l'`Ombrage lisse` [globalement](settings.md#smooth-shading) ou [par objet](material.md#smooth-shading) si vous peignez une surface métallique sur un objet qui a peu de polygones.
:::

## ![](/icons/paint.webp) Tout peindre {#paint-all}

![](/images/paint_paint_all.webp)

Applique le matériau actuel aux objets sélectionnés, soit en mode standard avec `Tout peindre`, soit en projection triplanaire avec `Tout peindre + Triplanaire`. La variante triplanaire n'est pas disponible sur les primitives qui n'ont pas été validées.

Les cases à côté des curseurs de couleur, de métallité, de rugosité et d'opacité sont respectées : les propriétés désactivées ne sont pas remplies.

Les boutons supplémentaires règlent ce qui peut encore influencer le remplissage. La plupart affichent un pourcentage, et ils sont grisés quand ils n'auraient aucun effet :

| Icône                       | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Les zones masquées ne sont pas affectées.     |
| ![](/icons/tool_hide.webp) | Les zones cachées ne sont pas affectées.      |
| ![](/icons/opacity.webp)   | Utilise le facteur de peinture de l'outil ci-dessus. |
| ![](/icons/layer.webp)     | Les zones non peintes d'un calque ne sont pas affectées. |
| ![](/icons/triplanar.webp) | `Sommet` : la variante triplanaire décale aussi la surface avec l'alpha, selon l'intensité de l'outil affichée. |
| ![](/icons/cog.webp)       | Ouvre les réglages triplanaires               |

### ![](/icons/cog.webp) Réglages triplanaires {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Comme pour les [réglages triplanaires du menu Matériau](material.md#triplanar), vous pouvez régler le fondu entre les projections, la répétition et les décalages. 

Cochez la case d'aperçu en haut de ce menu pour garder un aperçu affiché pendant que vous ajustez les valeurs.
