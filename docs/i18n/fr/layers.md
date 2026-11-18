# ![](/icons/layer.webp) Calques {#layers}

Ce menu contient la pile de calques, un moyen de stocker les modifications de votre objet de manière non destructive, avec de nombreuses façons de combiner et de réutiliser les calques.

![](/images/layers_overview.webp) 

## Présentation {#overview}

Les calques de Nomad servent à plusieurs choses.

Pour la peinture (couleur, rugosité, métallité, opacité), les calques fonctionnent comme dans les applications de peinture 2d. Vous pouvez créer un calque et peindre le modèle dessus. Le calque peut être activé ou désactivé, son opacité ajustée, il peut être dupliqué, déplacé dans la pile de calques, et son mode de fusion modifié.

Nomad utilise aussi les calques pour la sculpture. Un calque peut contenir de fins détails comme des rides, ou de grands changements de forme, ce qui lui permet de fonctionner comme les blendshapes, shape keys ou morph targets d'autres applications 3d. Vous pouvez par exemple sculpter différentes expressions du visage sur différents calques, puis ajuster les curseurs des calques pour les combiner en de nouvelles expressions.

Dans ce cas, les changements stockés dans un calque s'additionnent simplement : l'ordre des calques n'a pas d'importance, contrairement à la peinture.

Les calques peuvent être effacés en partie avec l'outil [SupprCalque](tools.md#delete-layer), et ils peuvent aussi servir à créer des masques à partir des différentes informations qu'ils contiennent.

![](/videos/layer.mp4)

::: tip
Contrairement à la plupart des logiciels de sculpture, modifier la topologie d'un maillage ne supprime pas les calques. Vous pouvez utiliser le [Remaillage voxel](topology.md#voxel-remesher), la [Multirésolution](topology.md#multiresolution) ou les outils [Découper](tools.md#trim)/[Scinder](tools.md#split), mais sachez qu'avec le [Remaillage voxel](topology.md#voxel-remesher), la qualité du calque en pâtit.
:::

::: tip
Si vous utilisez les calques comme blendshapes ou morph targets, le [menu Scène](scene.md#object-menu) offre des fonctions supplémentaires : vous pouvez séparer des calques en objets, et combiner des objets correspondants en calques.
:::
----

## Menu Calques {#layer-menu}

![](/images/layers_menu.webp)

Le titre affiche le nom de l'objet sélectionné. Les calques ne sont pas disponibles sur les primitives : validez d'abord la primitive.

Touchez `Ajouter un calque` pour créer un nouveau calque. `Fusionner les calques` fusionne tous les calques dans le maillage de base ; le nombre à côté de son icône indique combien il y a de calques.

Chaque calque a un nom, un curseur qui règle sa force (son facteur), et des boutons d'options. Touchez un calque pour en faire le calque actif : la sculpture et la peinture vont dans ce calque. Touchez `Base` pour retravailler le maillage de base.

### ![](/icons/sort_right.webp) Déplier la liste {#ui-expand-list}

Par défaut, la liste des calques n'affiche que la visibilité, le mode de fusion et la force de chaque calque, et seul le calque actif est déplié avec toutes ses commandes. La flèche à gauche du titre déplie toutes les commandes de chaque calque.

![](/images/layers_expand.webp)

### Options {#options}

| Action       | Icône                        | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Affiche ou masque le calque                         |
| Mode de fusion | ![](/icons/opacity.webp)  | Le mode de fusion, comme dans Photoshop. Les 4 icônes indiquent les modes pour la couleur, la rugosité, la métallité et l'opacité. |
| Renommer     | ![](/icons/pencil.webp)     | Modifie le nom du calque                            |
| Supprimer    | ![](/icons/trash.webp)      | Supprime le calque                                  |
| Dupliquer    | ![](/icons/clone.webp)      | Duplique le calque                                  |
| Fusionner vers le bas | ![](/icons/merge_down.webp) | Fusionne le calque avec le calque du dessous (ou le maillage de base) |
| Plus         | ![](/icons/more.webp)       | Options [Plus...](#more)                            |

Quand un calque n'est pas déplié, `Renommer`, `Supprimer`, `Dupliquer` et `Fusionner vers le bas` se trouvent dans son menu [Plus...](#more).

Pour déplacer un calque ailleurs dans la pile, appuyez longuement sur son nom, puis faites-le glisser.

### Base {#base}

Le bouton à 3 points de la ligne `Base` déplace la peinture du maillage de base dans un nouveau calque, avec le bouton `Base → Calque`. La base est ensuite remise au matériau d'arrière-plan. C'est pratique si vous avez beaucoup peint avant de créer le moindre calque.

* Les boutons de masque et de masquage à côté laissent intactes les zones masquées et cachées.
* `Extraire` - les canaux à déplacer : `Couleur`, `Opacité`, `Rugosité` et `Métallité`.
* `Matériau d'arrière-plan` - si cette option est activée, seules les valeurs qui diffèrent de ce matériau sont déplacées. Réglez-le avec les curseurs, ou prélevez-le sur le modèle avec la pipette.

### ![](/icons/more.webp) Plus... {#more}

Le bouton « Plus... » affiche des options supplémentaires pour le calque actuel, dans deux onglets : les réglages (icône de roue dentée) et l'extraction (icône de cube).

![](/images/layers_more.webp) 

#### Facteurs des canaux {#channel-factors}

Ces commandes vous permettent de doser la quantité de sculpture, de couleur, de rugosité, de métallité et d'opacité du calque. Ces valeurs sont multipliées par le curseur de facteur du calque : par exemple, si la force du calque est de 1 mais que le facteur du canal couleur est de 0,5, la couleur s'affiche à une force de 0,5.

`Décalage` règle la force de la sculpture du calque. Alors que la couleur, la rugosité et la métallité sont limitées entre 0 et 1, le décalage peut prendre n'importe quelle valeur, positive ou négative. 

::: tip
Le décalage permet de transformer un calque de bosses en un calque de creux, ou un sourire en une moue :
![](/videos/layer_happysad.mp4)


Un calque symétrique peut être cloné puis séparé en formes gauche et droite avec SupprCalque :
![](/videos/layer_leftright.mp4)

Des calques au facteur de décalage négatif peuvent être appliqués dans des calques vides pour créer de nouvelles formes positives.

Des calques au facteur de décalage positif supérieur à 1 permettent d'expérimenter des blendshapes plus extrêmes.
:::

::: warning
Pour l'instant, les calques n'ont qu'un seul canal d'opacité partagé par les 3 canaux (couleur, métallité, rugosité).
Si vous fusionnez plusieurs calques dont l'intensité par canal n'est pas au maximum, le résultat final peut avoir un aspect différent.

Peut-être qu'à l'avenir, chaque canal aura son propre canal alpha pour lever cette limitation.
:::


#### ![](/icons/shield.webp) Masque {#mask}
Le bouton de masque à côté de chaque curseur crée un masque à partir de ce canal. Comme lorsqu'on utilise des calques pour faire des sélections dans les applications de peinture, cela vous permet de réutiliser le travail fait dans un calque pour d'autres opérations.

#### ![](/icons/preview.webp) Aperçu {#preview}
![](/images/layers_preview.webp) 

Les options suivantes se trouvent dans l'onglet d'extraction du menu « Plus... ».

Quand cette option est activée, elle affiche un aperçu des réglages d'extraction de ce calque (voir la section suivante).

`Rayons X` choisit quels objets deviennent transparents pendant l'aperçu (`Aucun`, `Non sélectionné`, `Sélectionné` ou `Tout`), pour que la forme extraite reste opaque. C'est utile si vous utilisez des hauteurs d'extraction négatives.

#### ![](/icons/mask_extract.webp) Extraire {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Le bouton `Extraire` duplique le contenu du calque dans un nouvel objet, généralement avec une épaisseur choisie par vous dans la section suivante.

`Fermeture` détermine comment la duplication est faite :

* `Aucune` - Extrait simplement la partie, sans essayer de créer des côtés ni de boucher les trous.
* `Remplir` - Le trou est bouché avec des triangles, puis lissé. N'utilisez pas cette option pour des surfaces planes.
* `Coque` - Ferme la forme extraite avec la valeur d'épaisseur et les options de direction.
* `Calque` - Extrait la différence apportée par le calque.

#### ![](/icons/height.webp) Hauteur {#thickness}
![](/images/layers_thickness.webp) 

La profondeur de l'extrusion de la coque. Les valeurs positives sortent de la surface, les valeurs négatives rentrent dans la surface. Ce réglage est masqué quand la fermeture est `Calque`.

Le plus/moins à côté de cette valeur règle la direction de l'extrusion :
* Moins ( - ) part de la surface actuelle et extrude vers l'intérieur. 
* Plus ( + ) part de la surface actuelle et extrude vers l'extérieur.
* Plus-moins ( ± ) écarte le dessus et le dessous de l'extrusion de façon égale, si bien qu'elle est à moitié enfoncée dans la surface d'origine.

#### Côtés {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Cette section est visible quand la fermeture est `Coque`. 

`Divisions de la paroi` règle le nombre de divisions le long des côtés de la coque. Avec son interrupteur `Auto` activé, Nomad calcule le nombre de boucles d'arêtes pour obtenir des polygones carrés.

#### Lissage {#smoothness}
![](/images/layers_smoothness.webp) 

Si les bords de la zone à extraire sont irréguliers, activez cette option pour les lisser en une forme plus propre. `Tout` lisse toute la surface extraite, `Uniquement les bords` lisse ses bords. `Itérations` règle la force du lissage.

_Fin du sous-menu « Plus... »._

### ![](/icons/cog.webp) Avancé {#advanced}
![](/images/layers_advanced.webp)

Le bouton `Avancé` en bas du menu apparaît dès que l'objet a des calques.

#### Garder les détails des calques du haut {#keep-top-layers-details}

Garantit que les petits détails des calques supérieurs restent visibles quand vous faites de grands changements sur les calques inférieurs. Pendant que vous sculptez, la déformation provenant des calques du haut est ignorée, mais leurs détails restent visibles. Cela ne fonctionne bien que si ces calques du haut contiennent des détails relativement petits.

Par défaut, si vous sculptez de petites rides sur un calque, puis faites de grands changements sur le calque de base, les rides sont perdues. Activer cette option permet à ces petits détails de toujours flotter au-dessus des grands changements du dessous. Dans la vidéo suivante, voyez comment les rides disparaissent par défaut, mais restent visibles quand « Garder les détails des calques du haut » est activé :

![](/videos/layers_details.mp4)


#### Synchroniser la transformation {#sync-transform}

Quand cette option est activée, tous les calques non sélectionnés sont ajustés selon la rotation, l'échelle et le cisaillement de la transformation, quand vous utilisez les outils Gizmo ou Transformation. Elle peut valoir `Auto`, `Non` ou `Oui`.

Désactivez cette option si les autres calques doivent être utilisés sans la nouvelle transformation que vous appliquez.

Sur `Auto`, seuls les calques visibles sont ajustés.
