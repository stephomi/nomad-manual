# ![](/icons/image.webp) Arrière-plan {#background}

Ce menu contrôle la couleur d’arrière-plan de Nomad, ainsi que les images de référence à utiliser.

![](/images/background_overview.webp)

## Arrière-plan {#type}
![](/images/background_selector.webp)

Il existe trois options pour l’arrière-plan de la vue.

* `Environment` - Affiche la carte d’environnement sélectionnée dans [Shading](shading). Celle-ci peut être contrôlée plus finement avec les réglages de flou (Blur) et d’exposition (brightness). 
* `Color` - Une couleur unie que vous pouvez choisir.
* `Gradient` - Un dégradé de couleur du haut vers le bas. Le curseur Factor vous permet de déterminer le point médian du dégradé.  

## Image de référence {#reference}

![](/images/background_reference.webp)

Vous pouvez ajouter une image de votre choix en arrière-plan pour l’utiliser comme référence.
Vous pouvez en modifier la position et l’échelle, par exemple si vous souhaitez la déplacer dans un coin de l’écran.

### ![](/icons/tool_transform.webp) Transformer {#transform}

Ce bouton vous permet de placer l’image de référence de manière interactive. Utilisez 2 doigts pour déplacer (pan), mettre à l’échelle (scale) et faire pivoter (rotate) l’image de référence. Le placement final sera reflété dans les curseurs ci-dessous :

* `Overlay` - à 0 % l’image de référence sera toujours derrière vos objets, à 100 % elle sera devant. 
* `Opacity` - Le degré de transparence de l’image.
* `Position` - La position X et Y de l’image.
* `Rotation` - La rotation de l’image.
* `Scale` - L’échelle de l’image.


::: tip

Les caméras et les images de référence sont liées. 

Cela signifie que si vous configurez votre image de référence pour qu’elle s’aligne avec votre sculpture, lorsque vous créez une caméra depuis le [menu Camera](camera), la position, la rotation et l’échelle de l’image de référence sont également enregistrées avec la caméra. Vous pouvez désactiver l’image de référence, pivoter vers une autre vue. Si vous regardez à nouveau à travers la caméra, l’image de référence sera réactivée avec les réglages que vous aviez utilisés.

Cela inclut même le choix d’images différentes pour des caméras différentes !

 ![](/videos/reference_camera.mp4)

:::