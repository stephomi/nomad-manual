# ![](/icons/image.webp) Arrière-plan {#background}

Ce menu règle la couleur d'arrière-plan de Nomad, ainsi que les éventuelles images de référence.

![](/images/background_overview.webp)

## Type {#type}
![](/images/background_selector.webp)

Trois options sont proposées pour l'arrière-plan de la vue 3d.

* `Environnement` - Affiche la carte d'environnement choisie dans [Ombrage](shading.md). Vous pouvez l'ajuster avec les curseurs `Flou` et `Exposition` (luminosité).
* `Couleur` - Une couleur unie, au choix.
* `Gradient` - Une transition entre deux couleurs. Le curseur `Facteur` déplace le point médian du dégradé.

### Type de gradient {#gradient-type}
Avec `Gradient`, choisissez sa forme :
* `Linéaire` - Un dégradé rectiligne, dont la direction se règle avec le curseur `Angle`.
* `Radial` - Un dégradé circulaire qui part du centre de l'écran.
* `Ciel` - Un dégradé ancré sur l'horizon du monde : il suit la caméra quand vous regardez vers le haut ou vers le bas.

Chaque couleur a un bouton de réinitialisation et une pipette, pour prélever une couleur à l'écran.

## ![](/icons/lock.webp) Suivre la caméra {#sync-on-camera-lock}
Quand la caméra est verrouillée avec le [Cube d'alignement](settings.md#snap-cube), l'image de référence suit les mouvements de la caméra, et reste donc alignée sur votre sculpture.

* `Autoriser le roulis (Trackball)` - Permet à la caméra de rouler quand vous quittez le verrouillage de la caméra.
* `Réinitialiser au déverrouillage` - Réinitialise la vue quand vous quittez le verrouillage de la caméra.

## Image de référence {#reference}

![](/images/background_reference.webp)

Vous pouvez placer l'image de votre choix en arrière-plan pour vous en servir comme référence. Touchez `Importer…` pour en ajouter une, puis cochez `Image de référence` pour l'afficher.
Vous pouvez modifier sa position et son échelle, par exemple pour la déplacer dans un coin de l'écran.

### ![](/icons/tool_transform.webp) Transformation {#transform}

Ce bouton vous permet de placer l'image de référence directement à l'écran. Avec deux doigts, déplacez, mettez à l'échelle et faites pivoter l'image pour la mettre en place. `Réinitialiser les réglages` remet l'image à sa position par défaut. Le placement final se reflète dans les curseurs ci-dessous :

* `Incrustation` - À 0 %, l'image de référence est toujours derrière vos objets ; à 100 %, elle est devant.
* `Opacité` - Le degré de transparence de l'image.
* `Post-traitement` - Applique les effets de post-traitement à l'image de référence. Désactivez-le pour garder les couleurs d'origine.
* `Position X` / `Position Y` - La position X et Y de l'image.
* `Échelle` - L'échelle de l'image.
* `Rotation` - La rotation de l'image.


::: tip

Les caméras et les images de référence sont liées.

Concrètement, si vous avez aligné votre image de référence sur votre sculpture et que vous créez une caméra depuis le [menu Caméra](camera.md), la position, la rotation et l'échelle de l'image de référence sont enregistrées avec la caméra. Vous pouvez ensuite masquer l'image de référence et tourner autour du modèle. Dès que vous repassez par cette caméra, l'image de référence se réactive avec les réglages que vous aviez utilisés.

Vous pouvez même choisir une image différente pour chaque caméra !

 ![](/videos/reference_camera.mp4)

:::
