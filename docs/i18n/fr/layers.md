# ![](/icons/layer.webp) Couches 

Ce menu contient la pile de couches, un moyen de stocker les modifications apportées à votre objet de manière non destructive, ainsi que de nombreuses façons de combiner et de réutiliser les couches.

![](/images/layers_overview.webp) 

## Vue d’ensemble

Les couches de Nomad ont plusieurs usages.

Les informations de peinture (Couleur, Rugosité, Métallicité, Opacité) fonctionnent avec les couches de manière similaire aux applications de peinture 2D. Une couche peut être créée et de la peinture appliquée sur un modèle. La couche peut être activée ou désactivée, son opacité ajustée, la couche peut être dupliquée, son ordre peut être modifié dans la pile de couches, son mode de fusion ajusté.

Nomad utilise également les couches pour la sculpture. Une couche peut stocker de fins détails comme des rides, ou de grands changements, ce qui leur permet de fonctionner comme des blendshapes/shape keys/morph targets dans d’autres applications 3D. Par exemple, vous pouvez sculpter différentes expressions faciales sur différentes couches, puis ajuster les curseurs de couches pour les combiner en de nouvelles expressions.

Dans ce cas, les changements stockés dans une couche sont purement additifs, l’ordre des couches n’a pas d’importance comme c’est le cas pour la peinture.

Les couches peuvent être partiellement effacées via l’outil [Delete Layer](tools.md#delete-layer), et les couches peuvent également être utilisées pour créer des masques basés sur les différentes informations stockées dans la couche.

![](/videos/layer.mp4)

::: tip
Contrairement à la plupart des logiciels de sculpture, modifier la topologie d’un maillage ne supprimera pas les couches. Vous pouvez utiliser le [Voxel Remesher](topology.md#voxel-remesher), le [Multiresolution](topology.md#multiresolution) ou les outils [Trim](tools.md#trim)/[Split](tools.md#split), mais notez qu’en utilisant le [Voxel Remesher](topology.md#voxel-remesher), la qualité de la couche sera impactée.
:::

::: tip
Si vous utilisez les couches pour des blendshapes/morph targets, il existe des fonctionnalités supplémentaires liées aux couches dans le [menu de scène](scene.md#object-menu). Vous pouvez séparer les couches en objets, et combiner des objets correspondants en couches.
:::
----

## Menu des couches 

![](/images/layers_menu.webp)

Appuyez sur `Add layer` pour créer une nouvelle couche.

Chaque couche possède un nom, un curseur pour contrôler sa force/facteur, et des boutons d’options.

### Options

| Action       | Icône                        | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Afficher/masquer la couche                         |
| Mode de fusion | ![](/icons/opacity.webp)  | Le mode de fusion de type Photoshop. Les 4 icônes affichent les modes pour Couleur, Rugosité, Métallicité, Opacité. |
| Modifier le nom | ![](/icons/pencil.webp)  | Modifier le nom de la couche                       |
| Supprimer    | ![](/icons/trash.webp)      | Supprimer la couche                                |
| Dupliquer    | ![](/icons/clone.webp)      | Dupliquer la couche                                |
| Fusionner vers le bas | ![](/icons/merge_down.webp) | Fusionner la couche avec la couche inférieure (ou le maillage de base) |
| Plus         | ![](/icons/more.webp)       | Options [Plus...](#more)                           |

Pour déplacer une couche vers une autre partie de la pile, appuyez et maintenez sur son nom, puis faites-la glisser.

### Plus...

Le bouton « More... » affichera des options supplémentaires pour la couche actuelle :

![](/images/layers_more.webp) 

#### Facteurs de canal

Ces contrôles vous permettent de mettre à l’échelle la quantité de sculpture/couleur/rugosité/métallicité/opacité pour la couche. Ces valeurs sont multipliées par le curseur de facteur de couche, donc par exemple si la force de la couche est 1, mais que le facteur du canal couleur est 0,5, alors la couleur affichée sera à une force de 0,5.

`Offset` contrôle la force de sculpture de la couche. Alors que couleur/rugosité/métallicité sont limitées entre 0 et 1, l’offset peut être n’importe quelle valeur, positive ou négative. 

::: tip
Offset peut être utilisé pour transformer une couche de bosses en couche de creux, ou un sourire en grimace :
![](/videos/layer_happysad.mp4)


Une couche symétrique peut être clonée puis séparée en formes gauche/droite avec del layer :
![](/videos/layer_leftright.mp4)

Les couches avec des facteurs d’offset négatifs peuvent être cuites vers des couches vides pour créer de nouvelles formes positives.

Les couches avec des facteurs d’offset positifs supérieurs à 1 peuvent être utilisées pour expérimenter des blendshapes plus extrêmes.
:::

::: warning
Pour le moment, les couches ne partagent qu’un seul canal d’opacité pour les 3 canaux (couleur/métallicité/rugosité).
Si vous fusionnez plusieurs couches avec une intensité par canal qui n’est pas à pleine intensité, il est possible que le résultat final soit différent.

Peut-être qu’à l’avenir, chaque canal aura son propre canal alpha pour supprimer cette limitation.
:::


#### ![](/icons/tool_mask.webp) Masque
Le bouton de masque à côté de chaque curseur créera un masque à partir de ce canal. De manière similaire à l’utilisation de couches pour faire des sélections dans les applications de peinture, cela vous permet de réutiliser le travail effectué dans une couche pour d’autres opérations.

#### ![](/icons/preview.webp) Aperçu
![](/images/layers_preview.webp) 

Lorsqu’il est activé, prévisualise les paramètres d’extraction pour cette couche (voir la section suivante).

Lorsque le mode rayon X est activé, seule la forme extraite sera solide, le reste de la forme sera rendu transparent, ce qui est utile si vous utilisez des hauteurs d’extraction négatives.

#### Extraire
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Le bouton `Extract` dupliquera le contenu de la couche dans un nouvel objet, généralement avec une épaisseur spécifiée par l’utilisateur définie dans la section suivante.

`Closing action` détermine la façon dont la duplication est effectuée :

* None - Extraire simplement la partie, sans tenter de générer des côtés ni de remplir les trous.
* Fill - Le trou est rempli et lissé avec des triangles. N’utilisez pas cette option pour des surfaces planes.
* Shell - Fermer la forme extraite avec les options d’épaisseur et de direction.
* Layer - Extraire la différence de couche.

#### ![](/icons/height.webp) Épaisseur
![](/images/layers_thickness.webp) 

La profondeur de l’extrusion de coque. Les valeurs positives se développent hors de la surface, les valeurs négatives vers l’intérieur de la surface.

Le plus/moins à côté de cette valeur définit la direction de l’extrusion :
* Minus ( - ) commencera à partir de la surface actuelle et extrudera vers le bas. 
* Plus ( + ) commencera à partir de la surface actuelle et extrudera vers le haut.
* PlusMinus ( ± ) poussera le haut et le bas de l’extrusion dans des directions opposées de manière égale, de sorte qu’elle sera à moitié intégrée dans la surface d’origine.

#### Lissage
![](/images/layers_smoothness.webp) 

Si les bords de la région à extraire sont irréguliers, ce curseur tentera de flouter le bord pour obtenir une forme plus lisse. 

#### ![](/icons/height.webp) Boucle de bord (côté)
![](/images/layers_edgeloop.webp) 

Cette section est visible lorsque l’action de fermeture est « Shell ». 

`Auto Edge-loop (side)` calculera le nombre de boucles de bord le long des côtés de la coque pour créer des polygones carrés. 

Si désactivé, le curseur `Division` définira le nombre de divisions sur les côtés.

_Ceci est la fin du sous-menu « More... ». _

### Avancé
![](/images/layers_advanced.webp)

#### Conserver les détails des couches supérieures

Garantit que les petits détails sur les couches supérieures restent visibles lorsque de grands changements sont effectués sur les couches inférieures.

Par défaut, si vous sculptez de petites rides sur une couche, puis effectuez de grands changements sur la couche de base, les rides seront perdues. L’activation de ce bouton permettra à ces petits détails de toujours flotter au-dessus des grands changements inférieurs. Dans la vidéo suivante, voyez comment le détail de la ride est supprimé par défaut, mais reste visible lorsque « keep top layers details » est activé :

![](/videos/layers_details.mp4)


#### UI: Développer la liste

Le menu de couches par défaut vous permet d’activer/désactiver la visibilité des couches et l’opacité de la couche. L’activation de cette option développe les contrôles complets pour chaque couche.

![](/images/layers_expand.webp)

#### Synchroniser la transformation

Si activé, toutes les couches non sélectionnées seront ajustées en fonction de la rotation, de l’échelle et du cisaillement de la transformation. 

Désactivez cette option si les autres couches sont destinées à être utilisées sans la nouvelle transformation que vous appliquez.

Lorsque réglé sur `Auto`, seules les couches visibles seront ajustées.
