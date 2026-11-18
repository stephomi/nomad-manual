# ![](/icons/camera.webp) Caméra {#camera}

Ce menu vous permet de créer et de modifier des caméras, et de régler la façon dont vous interagissez avec elles.

![](/images/camera_overview2.webp)

Dans Nomad, les caméras ont plusieurs usages :

* Préparer des vues pour sculpter sous des angles précis
* Cadrer vos objets, comme avec un appareil photo
* Naviguer dans votre scène avec une caméra à la première personne
* Servir de caméra orthographique pour des jeux isométriques ou des rendus de style industriel.

## Contrôler la caméra {#control}

### Rotation {#rotation}
Pour faire tourner la caméra, faites glisser *un* doigt sur l'arrière-plan.
Si vous faites glisser le doigt sur votre modèle, c'est la sculpture qui commence à la place.

::: tip Puis-je faire tourner la caméra si je n'ai pas accès à l'arrière-plan ?
Oui : posez *deux* doigts sur l'écran, comme pour commencer un geste de translation ou de zoom, puis relâchez *un* doigt.
:::

### Mise au point / Réinitialisation {#focus}
*Touchez deux fois* le modèle pour centrer la vue sur le point touché.
Si vous *touchez deux fois* l'arrière-plan, la caméra se centre plutôt sur le maillage sélectionné ou sur toute la scène, voir [Double appui sur l'arrière-plan](#dtap-tap-background).


### Translation {#translation}
Déplacez *deux* doigts pour faire glisser la caméra.


### Zoom {#zooming}
Pincez pour zoomer ou dézoomer.


### Roulis {#rolling}
Vous pouvez faire *rouler* la vue en tournant *deux* doigts.
::: warning
Ce geste n'est disponible qu'avec les modes de rotation `Trackball`.
:::

### Contrôles sur ordinateur {#desktop}

Sur ordinateur, la touche Alt/Option sert à contrôler la caméra :

* glisser avec la pointe dans le vide = rotation de la caméra
* Alt + glisser avec la pointe = translation
* Alt + glisser avec la pointe, puis relâcher Alt = zoom (comme dans ZBrush)

Avec les tablettes Wacom dont le stylet a 2 boutons ou plus, configurez la pointe et les boutons dans les réglages Wacom comme ceci :

* pointe = clic gauche
* bouton inférieur = clic du milieu
* bouton supérieur = clic droit

Avec ces réglages, vous pouvez manipuler la caméra uniquement avec le stylet :

* bouton supérieur et déplacement en survol = rotation de la caméra
* bouton inférieur et déplacement en survol = translation

## Contrôles des caméras {#camera-controls}

![](/images/camera_list.webp)

### Vues {#views}
Vous pouvez enregistrer des points de vue de caméra avec `Ajouter une vue`.
Touchez le nom d'une vue pour que la caméra revienne à cette vue.


::: tip
Une vue enregistrée garde aussi le réglage [Projection](#projection) et l'[image de référence](background.md).  
C'est pratique pour passer d'une vue de référence de face, de gauche ou de dos à l'autre, chacune avec son arrière-plan.
:::

| Action      | Icône                         | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilité  | ![](/icons/eye_open.webp)    | Active ou désactive la caméra. Les caméras cachées sont ignorées par les boutons précédent/suivant |
| Nom         |                               | Sélectionne la caméra                                                       |
| Image       | ![](/icons/image.webp)       | Une miniature de l'image de référence, si elle est liée à la caméra         |
| Projection  | ![](/icons/perspective.webp) | La projection de la caméra, avec son champ de vision en perspective         |
| Mettre à jour la vue | ![](/icons/update_view.webp) | Met à jour la vue enregistrée avec le point de vue actuel         |
| Renommer    | ![](/icons/pencil.webp)      | Modifie le nom de la caméra                                                 |
| Supprimer   | ![](/icons/trash.webp)       | Supprime la caméra                                                          |

### ![](/icons/camera_add.webp) Ajouter une vue {#add}
Crée une nouvelle caméra à partir de la vue actuelle.

### ![](/icons/camera.webp) Icônes {#icons-test}

Affiche ou masque les icônes des caméras dans la vue. Le bouton apparaît à côté de `Ajouter une vue` dès que vous avez une caméra. L'icône de la caméra sélectionnée est toujours visible.

### Projection {#projection}
Choisissez entre `Perspective` et `Orthographique`.

En perspective, vous pouvez régler le `Champ de vision vertical` de votre caméra. La focale équivalente pour un appareil 35 mm s'affiche au-dessus du curseur, pratique si vous avez l'habitude de la photo.
Pour sculpter, on conseille généralement un champ de vision faible, qui aide à juger les proportions.  
Le mode `Orthographique` revient plus ou moins à un champ de vision égal à 0.

### Première personne {#fps}
En perspective uniquement. Place le pivot directement sur la caméra plutôt que sur la sculpture. Faire glisser un doigt sur l'arrière-plan garde la position de la caméra fixe et change seulement sa rotation, comme dans les jeux à la première personne. Utile pour sculpter des décors plutôt que des objets isolés.

![](/images/camera_rotation_ortho_view.webp)

### Type de rotation {#rotation-type}
Par défaut, la caméra utilise le mode de rotation `Plateau tournant`.
Vous n'avez alors que deux degrés de liberté : c'est plus intuitif, mais dans certains cas vous voudrez plus de souplesse.  
Vous pouvez passer en `Trackball` : vous pourrez alors faire *rouler* la vue en tournant *deux* doigts dans la vue. Il existe deux modes `Trackball` : le premier fait rouler la vue comme une boule sous votre doigt, tandis que le second (avec l'icône de flèches) tourne la vue d'après les mouvements horizontaux et verticaux de votre glissement, ce qui peut sembler plus familier à certains utilisateurs.

### Alignement orthographique {#orthographic}

Si vous avez un clavier et que cette option est activée, maintenir Shift pendant que vous tournez la vue aligne la caméra sur la vue de face, de dos, de dessus, de dessous, de gauche ou de droite la plus proche, et rend la caméra orthographique. La caméra devient aussi orthographique quand vous touchez le navigateur pour vous aligner sur l'une de ces vues.

### Réinitialiser la vue {#reset}

Place la caméra de face et cadre toute la scène dans la vue.

### Vue alignée {#snap}
Aligne la caméra sur la vue de face, de dos, de gauche, de droite, de dessus ou de dessous la plus proche. Si vous êtes déjà dans l'une de ces vues, toucher à nouveau le bouton fait pivoter la vue de 180 degrés vers le côté opposé.

### Vitesse {#speed}

Si la caméra vous semble trop lente ou trop rapide, vous pouvez régler un multiplicateur de vitesse pour `Rotation`, `Zoom` et `Translation`. Utile si votre sculpture est très grande ou très petite.

### Le pivot {#pivot}

Quand vous tournez la caméra, vous voyez un petit point rose : c'est le point de pivot de la caméra.  
Il est très important de comprendre où se trouve votre pivot, pour ne pas vous perdre ni vous agacer avec la caméra.

Par défaut, le pivot est mis à jour par ces actions :
- un double appui sur le modèle
- un double appui sur l'arrière-plan (le nouveau pivot sera au centre de votre maillage)
- poser *deux* doigts sur l'écran (translation, zoom, roulis) place le pivot au centre des *deux* doigts

### Mettre à jour le pivot... {#update-pivot}

Vous pouvez affiner la mise à jour du pivot avec ces options :

* `Au mouvement de caméra` - Met à jour le pivot quand vous commencez à manipuler la caméra.
* `Pivot hors surface` - Autorise un nouveau pivot même quand vous zoomez en dehors de la surface de l'objet. Nécessite `Au mouvement de caméra`.
* `Mettre à jour lors du double appui` - Met à jour le pivot de rotation quand vous touchez deux fois la surface de l'objet.
* `Sculpter (Trait)` - Met à jour le pivot quand vous sculptez.

::: tip
Une fois que vous êtes habitué, vous pouvez masquer le point rose (indicateur) dans le menu [Réglages](settings.md).
:::

### Centrer la vue lors du zoom arrière {#center-view-when-zooming-out}
Quand vous dézoomez, la caméra ne glisse pas sur le côté : elle ne fait que reculer, et la vue reste centrée.

### Double appui sur l'objet {#dtap-object}
Si cette option est activée, toucher deux fois un objet centre la caméra sur le point touché.

### Double appui sur l'arrière-plan {#dtap-tap-background}
Si cette option est activée, toucher deux fois l'arrière-plan centre la caméra sur :
* `Sélection` - Les objets sélectionnés.
* `Scène` - Toute la scène.
* `Basculer` - Alterne entre les deux à chaque double appui. Il existe deux options `Basculer`, qui diffèrent par celle qui vient en premier, comme le montrent leurs icônes.
