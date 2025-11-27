# Bien démarrer

## Bienvenue dans Nomad !

Nomad est une application de sculpture 3D qui fonctionne sur de nombreux appareils, et qui donne les meilleurs résultats sur les tablettes avec stylet sensible à la pression, par exemple un iPad avec Apple Pencil, ou une Samsung Galaxy Tab avec stylet.

Elle est inspirée par des applications de sculpture sur ordinateur comme ZBrush et Blender, avec un accent sur une interface simple à comprendre, sans sacrifier les fonctionnalités. Si vous avez déjà utilisé des applications de sculpture 3D, Nomad vous semblera très familier.

Si c’est votre première expérience de sculpture 3D, il est utile de connaître quelques bases.

::: tip Vous préférez la vidéo ?
YouTube propose désormais BEAUCOUP de tutoriels vidéo pour débutants, voici quelques excellents liens :

* [Nomad Sculpt Crash Course par Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Tutoriel débutant Nomad Sculpt par Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Série NOMAD FOR BEGINNERS par SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Cela vaut la peine de consulter la chaîne principale de ces créateurs, ils publient fréquemment de nouveaux tutoriels.
:::

## Votre première sculpture

Lorsque vous lancez Nomad pour la première fois, vous verrez une sphère à l’écran. Faites simplement glisser votre stylet sur la sphère pour commencer à sculpter. La symétrie est activée par défaut pour faciliter la sculpture.

![](/videos/gettingstarted_01.mp4)

Pour agrandir ou réduire la brosse, utilisez le curseur de rayon sur la gauche.

![](/videos/gettingstarted_02.mp4)

Pour rendre la brosse plus forte ou plus faible, utilisez le curseur d’intensité sur la gauche.

![](/videos/gettingstarted_03.mp4)

L’outil par défaut est l’`outil Clay`, et il ajoute de la matière à la surface. Pour soustraire de la matière, touchez le bouton `Sub` sur la gauche. Pour ajouter de nouveau à la surface, touchez encore une fois le bouton Sub.

![](/videos/gettingstarted_04.mp4)

Pour lisser la surface, touchez le bouton `Smooth`. Pour revenir à la sculpture normale, touchez à nouveau le bouton Smooth.

![](/videos/gettingstarted_05.mp4)

Pour tourner autour du modèle, faites glisser dans l’espace vide en dehors du modèle.

![](/videos/gettingstarted_06.mp4)

Pour zoomer, utilisez le geste de pincement/zoom à deux doigts.

![](/videos/gettingstarted_07.mp4)

Pour déplacer la caméra (pan), posez 2 doigts sur l’écran et faites glisser.

![](/videos/gettingstarted_08.mp4)

Si vous faites une erreur, un tap à 2 doigts annulera l’action, ou utilisez le bouton d’annulation en bas à gauche. 

![](/videos/gettingstarted_09.mp4)

::: tip Version bureau
Sur ordinateur, la touche alt/opt est utilisée pour contrôler la caméra :

* clic dans l’espace vide = rotation de la caméra
* alt+clic et glisser = déplacement (pan)
* alt+clic et glisser, puis relâcher alt = zoom (comme dans ZBrush)

Avec les tablettes Wacom qui ont 2 boutons ou plus sur le stylet, utilisez les paramètres Wacom pour configurer la pointe et les boutons comme ceci :

* pointe = clic gauche
* bas du rocker = clic du milieu
* haut du rocker = clic droit

Avec ces réglages, vous pouvez manipuler la caméra uniquement avec le stylet :

* haut du rocker et déplacement en survol = rotation de la caméra
* bas du rocker et déplacement en survol = déplacement (pan)
:::

## Ajouter de la couleur

Nomad vous permet de peindre la surface de votre sculpture. Dans le menu des outils à droite, trouvez l’outil `Paint` et cliquez dessus. Sur la barre d’outils de gauche, une sphère colorée apparaîtra. Cliquez dessus, cela fera apparaître un sélecteur de couleur. Choisissez une couleur et peignez sur votre modèle.

![](/videos/gettingstarted_10.mp4)

Pour effacer, touchez le bouton `Erase` sur la barre d’outils de gauche, puis effacez sur la surface. Touchez à nouveau le bouton Erase pour revenir en mode peinture.

![](/videos/gettingstarted_11.mp4)

En utilisant la brosse clay en modes add/sub, smooth, paint, voyez si vous pouvez réaliser une simple tête de cartoon :

![](/images/gettingstarted_head1.webp)

## Autres outils

La palette d’outils contient de nombreux outils pour aider à la sculpture. Jusqu’ici vous avez utilisé la brosse clay (l’outil de départ par défaut), smooth et paint. Comme smooth est utilisé fréquemment, il dispose d’un raccourci supplémentaire dans la barre d’outils de gauche.

Les outils de Nomad peuvent faire une grande variété de choses, des outils liés à la sculpture comme move, crease, inflate, à des outils comme split et trim qui s’apparentent davantage à des outils de menuiserie ou de métallurgie. La page [Tools](tools.md) contient plus d’informations.

Voyez si vous pouvez utiliser les outils move, crease, inflate et smooth pour ajouter plus de détails à votre tête, changer sa forme :

![](/images/gettingstarted_head2.webp)

Maintenant que vous connaissez les bases de Nomad, regardons le reste de l’interface.

## Interface

![](/images/interface_overview1.webp)

* `Menus du haut` - Les menus pour accéder à la plupart des fonctionnalités de Nomad. Les menus en haut à gauche couvrent principalement les fonctionnalités de scène et d’objet, les menus en haut à droite sont liés aux outils. Sur les petits écrans, ces menus se replient ensemble pour gagner de la place.
* `Stats` - Informations sur la scène, l’objet courant, l’état du masque, l’utilisation de la mémoire.
* `Nav Cube` - Une aide pour montrer de quel côté de la sculpture vous regardez, ainsi qu’un raccourci pour passer à différentes vues. Taper sur le cube fera passer la vue au côté tapé. Faire glisser le cube le fera tourner. Touchez les petites icônes à côté du cube pour cadrer l’objet courant, ou réinitialiser à la vue d’accueil par défaut.
* `Boîte à outils` - Les outils de Nomad sont disponibles dans cette zone défilable.
* `Barre d’outils gauche` - Curseurs pour le rayon et l’intensité pour la plupart des outils, boutons contextuels pour d’autres outils, et raccourcis pour la symétrie, le mode alt/sub de l’outil, le masquage, le lissage, le gizmo et les options de peinture.
* `Barre d’outils du bas` - Raccourcis pour les fonctionnalités couramment utilisées, expliquées ci‑dessous.

::: tip Gaucher ?
Vous pouvez inverser l’emplacement et l’ordre de toutes les barres d’outils, voir [Mirror top bar](interface.md#mirror-top-bar) et d’autres options associées.
:::

## Barre d’outils du bas

![](/images/interface_bottom_toolbar.webp)

* `Undo` - annule la dernière opération
* `Redo` - rétablit la dernière opération annulée
* `History` - accéder aux options d’historique, expliquées dans le menu [History](history.md).
* `Solo` - Bascule entre l’affichage du seul objet courant, ou de tous les objets
* `X-Ray` - Fait apparaître tous les autres objets en mode rayons X, et l’objet courant en solide. Un appui long ou un balayage vers le haut vous permettra de définir la couleur et l’opacité du mode rayons X.
* `Voxel` - Un raccourci vers le bouton de [Voxel Remesher](topology.md#voxel-remesher) (remesh voxel). Un appui long ou un balayage vers le haut révélera des raccourcis pour définir la qualité du remesh voxel.
* `Grid` - Bascule l’affichage de la grille. Un appui long ou un balayage vers le haut révélera les options de la grille.
* `Wire` - Bascule une superposition en fil de fer (wireframe). Un appui long ou un balayage vers le haut révélera les options du wireframe.
* `Inspect` - Bascule l’affichage de données supplémentaires sur le maillage courant. Par défaut, il affichera les UV, mais un appui long ou un balayage vers le haut vous permettra d’inspecter d’autres propriétés si elles existent, et de choisir si cela s’affiche en arrière‑plan ou sur le maillage.

## Prochaines étapes

Ce que vous devriez apprendre ensuite dépend de vous, et de ce que vous trouvez intéressant ! Voici quelques suggestions :

Vous voulez en savoir plus sur les outils de sculpture ? Rendez‑vous dans la section [Tools](tools.md).

Vous voulez exporter vos modèles ? Ou importer des modèles à sculpter ? Ou créer des images de vos sculptures ? Rendez‑vous dans la section [Files](files.md).

Vous voulez en savoir plus sur le contrôle du niveau de détail de votre sculpture ? Rendez‑vous dans la section [Topology](topology.md) et découvrez le multires et la décimation.

Vous voulez travailler avec plus d’objets ? Combiner des objets simples et des primitives dans une scène plus grande ? Rendez‑vous dans la section [Scene](scene.md).

Vous voulez apprendre *tout* sur Nomad ? Bon choix ! Ce manuel couvre l’ensemble de Nomad, inclut de nombreux conseils et astuces, et dispose d’une excellente fonction de recherche en haut. Utilisez la navigation à gauche pour en apprendre davantage.

Si vous préférez la vidéo, Holger Schönischka a réalisé une énorme collection d’astuces pour Nomad sur YouTube : https://www.youtube.com/@ProcreateFX/videos


## Obtenir de l’aide

Si vous avez encore des questions après avoir lu le manuel et regardé les tutoriels vidéo, il existe trois principaux moyens de parler à d’autres utilisateurs de Nomad ou au développeur de Nomad :

* Visitez les forums : [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Rejoignez le chat Discord de Nomad : [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Contactez directement le développeur à l’adresse support@nomadsculpt.com
