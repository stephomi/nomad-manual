# ![](/icons/camera.webp) Caméra {#camera}

Ce menu vous permet de créer et de modifier des caméras, ainsi que de contrôler la façon dont vous interagissez avec elles.

![](/images/camera_overview2.webp)

Les caméras dans Nomad ont plusieurs usages :

* Configurer des vues pour sculpter sous des angles précis
* Les utiliser comme un appareil photo pour cadrer vos objets
* Les utiliser comme caméra à la première personne pour naviguer dans votre scène
* Les utiliser comme caméra orthographique pour des jeux isométriques ou un rendu de type industriel.

## Contrôler la caméra {#control}

### Rotation {#rotation}
Vous faites pivoter la caméra en faisant glisser *un* doigt sur l’arrière-plan.  
Si vous faites glisser le doigt sur votre modèle, cela lancera à la place l’opération de sculpture.

::: tip Puis-je faire pivoter la caméra si je ne peux pas accéder à l’arrière-plan ?
Oui, vous pouvez poser *deux* doigts sur l’écran – comme si vous vouliez commencer un geste de panoramique/zoom – puis relâcher *un* doigt.
:::

### Mise au point / Réinitialiser {#focus}
*Tapez deux fois* sur le modèle pour faire la mise au point sur le point sélectionné.  
Si vous *tapez deux fois* sur l’arrière-plan, la caméra fera la mise au point sur le maillage sélectionné à la place.

### Translation {#translation}
En déplaçant *deux* doigts, vous pouvez effectuer un panoramique de la caméra.

### Zoom {#zooming}
En utilisant le geste de pincement, vous pouvez zoomer/dézoomer.

### Rotation de l’horizon {#rolling}
Vous pouvez *faire rouler* la vue en faisant pivoter *deux* doigts.  
::: warning
Ce geste n’est disponible que pour le mode de rotation `trackball`.
:::

### Commandes de bureau {#desktop}

Sur ordinateur, la touche alt/opt est utilisée pour contrôler la caméra :

* clic du stylet et glisser dans l’espace vide = rotation de la caméra
* alt+clic du stylet et glisser = panoramique
* alt+clic du stylet et glisser, puis relâcher alt = zoom (comme dans ZBrush)

Avec les tablettes Wacom qui ont 2 boutons ou plus sur le stylet, utilisez les paramètres Wacom pour configurer la pointe et les boutons comme ceci :

* pointe = clic gauche
* bas du basculeur = clic du milieu
* haut du basculeur = clic droit

Avec ces paramètres, vous pouvez manipuler la caméra uniquement avec le stylet :

* haut du basculeur et déplacement en survol = rotation de la caméra
* bas du basculeur et déplacement en survol = panoramique

## Commandes de la caméra {#camera-controls}

![](/images/camera_list.webp)

### Vues {#views}
Vous pouvez enregistrer des points de vue de caméra en utilisant `Add View`.  
Si vous cliquez sur le nom de la vue, la caméra restaurera ce point de vue.

::: tip
Une vue enregistrée sauvegardera les paramètres de [Type de projection](#projection-type) ainsi que l’[image de référence](background.md).  
Cela peut être utile si vous voulez alterner entre des vues de référence avant/gauche/arrière avec des arrière-plans différents.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Activer/désactiver la caméra. Les caméras masquées seront ignorées par les boutons précédent/suivant |
| Name        |                               | Sélectionner la caméra                                                      |
| Image       | ![](/icons/image.webp)       | Une vignette d’une image de référence si elle est liée à la caméra         |
| Update View | ![](/icons/update_view.webp) | Mettre à jour la vue enregistrée avec le point de vue actuel               |
| Edit Name   | ![](/icons/pencil.webp)      | Modifier le nom de la caméra                                                |
| Delete      | ![](/icons/trash.webp)       | Supprimer la caméra                                                         |

### ![](/icons/tool_view.webp) Ajouter une vue {#add}
Créer une nouvelle caméra basée sur la vue actuelle.

### ![](/icons/camera.webp) Icônes {#icons-test}

Activer/désactiver l’affichage des icônes de caméra dans la vue. Si une caméra est sélectionnée, son icône est toujours visible.

### Type de projection {#projection}
Vous pouvez modifier le `Field of View` (FOV / longueur focale) de votre caméra.  
Il est généralement conseillé d’utiliser un FOV faible pour la sculpture, car cela peut aider pour les proportions.  
Vous pouvez également utiliser le mode `Orthographic`, qui est plus ou moins similaire à un FOV égal à 0.

### Première personne {#fps}
Active le réglage du pivot directement sur la caméra, plutôt que sur la sculpture. Faire glisser un doigt sur l’arrière-plan gardera la position de la caméra verrouillée, mais changera la rotation, de manière similaire au fonctionnement des jeux à la première personne. Utile pour sculpter des environnements plutôt que des objets uniques.

![](/images/camera_rotation_ortho_view.webp)

### Type de rotation {#rotation-type}
Par défaut, la caméra utilise le mode de rotation `Turntable`.  
Cela signifie que vous n’avez que deux degrés de liberté ; c’est plus intuitif mais dans certains cas vous voudrez plus de flexibilité.  
Vous pouvez passer à `Trackball`, vous pourrez alors *faire rouler* la vue en faisant pivoter *deux* doigts sur la vue. Sur ordinateur, il existe un mode trackball alternatif qui pourra être plus familier pour certains utilisateurs.

### Alignement orthographique {#orthographic}

Lorsqu’il est activé, si vous avez un clavier, maintenir la touche majuscule enfoncée pendant la rotation de la vue alignera la caméra sur la vue avant/arrière/haut/bas/gauche/droite la plus proche et rendra la caméra orthographique. La caméra sera également rendue orthographique lorsque le cube de vue est cliqué pour s’aligner sur avant/arrière/gauche/droite/haut/bas.

### Réinitialiser la vue {#reset}

Déplace la caméra vers l’avant et ajuste la scène pour qu’elle tienne dans la vue.

### Aligner la vue {#snap}
S’aligne sur la vue avant/arrière/gauche/droite/haut/bas la plus proche. Si vous êtes déjà dans l’une de ces vues, cliquer à nouveau effectuera une rotation de 180 degrés vers le côté opposé.

### Vitesse {#speed}

Si vous trouvez que la caméra se déplace trop lentement ou trop rapidement, vous pouvez définir un multiplicateur de vitesse pour la `rotation`, la `translation` et le `zoom`. Utile si votre sculpture est très grande ou très petite.

### Aperçu du pivot {#pivot}

Lorsque vous faites pivoter la caméra, vous pouvez voir un petit point rose : c’est votre point de pivot de caméra.  
Il est très important de comprendre où se trouve votre pivot afin de ne pas être perdu ou frustré par la caméra.

Par défaut, le pivot est mis à jour via ces opérations :
- double tape sur le modèle
- double tape sur l’arrière-plan (le nouveau pivot sera au centre de votre maillage)
- poser *deux* doigts sur l’écran (panoramique/zoom/roulis) mettra à jour le pivot au centre des *deux* doigts

### Mettre à jour le pivot… {#update-pivot}

Vous pouvez personnaliser davantage la mise à jour du pivot avec ces options :

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Quand vous y êtes habitué, vous pouvez masquer le point rose (indice) en allant dans les menus [Settings](settings.md).
:::

### Double‑taper sur l’objet {#dtap-object}
Lorsque `Focus` est activé, un double tape déplacera le pivot vers l’objet tapé.

### Double‑taper sur l’arrière‑plan {#dtap-tap-background}
Lorsqu’il est activé, définit le pivot sur l’un des éléments suivants : Sélection, Scène, ou bascule entre les deux.