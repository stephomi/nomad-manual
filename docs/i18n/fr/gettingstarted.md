# ![](/icons/play.webp) Prise en main {#getting-started}

## Bienvenue dans Nomad ! {#welcome-to-nomad}

Nomad est une application de sculpture 3d qui fonctionne sur de nombreux appareils, et qui donne le meilleur d'elle-même sur une tablette avec un stylet sensible à la pression, par exemple un iPad avec l'Apple Pencil, ou une Samsung Galaxy Tab avec son stylet.

Elle s'inspire des logiciels de sculpture sur ordinateur comme ZBrush et Blender, avec une interface facile à comprendre, sans rien sacrifier des fonctionnalités. Si vous avez déjà utilisé des applications de sculpture 3d, vous vous sentirez vite chez vous dans Nomad.

Si c'est votre première expérience de sculpture 3d, il est bon de connaître quelques bases.

::: tip Vous préférez la vidéo ?
YouTube regorge désormais de tutoriels vidéo pour débutants, en voici quelques excellents :

* [Nomad Sculpt Crash Course par Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial par Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [La série NOMAD FOR BEGINNERS par SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

N'hésitez pas à parcourir les chaînes de ces créateurs, ils publient régulièrement de nouveaux tutoriels.
:::

## Votre première sculpture {#your-first-sculpt}

Au premier lancement de Nomad, une sphère apparaît à l'écran. Faites simplement glisser votre stylet sur la sphère pour commencer à sculpter. La symétrie est activée par défaut pour faciliter la sculpture.

![](/videos/gettingstarted_01.mp4)

Pour agrandir ou réduire le pinceau, utilisez le curseur de rayon à gauche.

![](/videos/gettingstarted_02.mp4)

Pour rendre le pinceau plus fort ou plus doux, utilisez le curseur d'intensité à gauche.

![](/videos/gettingstarted_03.mp4)

L'outil par défaut est l'outil `Argile`, qui ajoute de la matière à la surface. Pour en retirer, touchez le bouton `Soustr.` à gauche. Pour revenir à l'ajout, touchez à nouveau le bouton `Soustr.`.

![](/videos/gettingstarted_04.mp4)

Pour lisser la surface, touchez le bouton `Lisser`. Pour revenir à la sculpture normale, touchez à nouveau le bouton `Lisser`.

![](/videos/gettingstarted_05.mp4)

Pour tourner autour du modèle, faites glisser dans le vide, en dehors du modèle.

![](/videos/gettingstarted_06.mp4)

Pour zoomer, pincez avec deux doigts.

![](/videos/gettingstarted_07.mp4)

Pour déplacer la caméra, posez 2 doigts sur l'écran et faites-les glisser.

![](/videos/gettingstarted_08.mp4)

Si vous faites une erreur, touchez l'écran avec 2 doigts pour annuler, ou utilisez le bouton d'annulation en bas à gauche. 

![](/videos/gettingstarted_09.mp4)

::: tip Version ordinateur
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
:::

## Ajouter de la couleur {#add-color}

Nomad vous permet de peindre la surface de votre sculpture. Dans le menu des outils à droite, trouvez l'outil `Peindre` et touchez-le. Une sphère colorée apparaît dans la barre d'outils de gauche. Touchez-la pour ouvrir le sélecteur de couleur. Choisissez une couleur, puis peignez sur votre modèle.

![](/videos/gettingstarted_10.mp4)

Pour effacer, touchez le bouton `Effacer` dans la barre d'outils de gauche, puis effacez sur la surface. Touchez à nouveau le bouton `Effacer` pour revenir en mode peinture.

![](/videos/gettingstarted_11.mp4)

Avec le pinceau Argile en mode ajout et soustraction, le lissage et la peinture, essayez de faire une tête toute simple de style cartoon :

![](/images/gettingstarted_head1.webp)

## Les autres outils {#other-tools}

La palette d'outils contient de nombreux outils pour vous aider à sculpter. Jusqu'ici, vous avez utilisé le pinceau Argile (l'outil de départ par défaut), le lissage et la peinture. Comme le lissage sert très souvent, il a un raccourci supplémentaire dans la barre d'outils de gauche.

Les outils de Nomad font des choses très variées, des outils de sculpture comme Déplacer, Pli ou Gonfler, jusqu'à des outils comme Scinder et Découper, plus proches de la menuiserie ou de la métallerie. La page [Outils](tools.md) vous en dit plus.

Essayez d'utiliser les outils Déplacer, Pli, Gonfler et Lisser pour ajouter des détails à votre tête et changer sa forme :

![](/images/gettingstarted_head2.webp)

Maintenant que vous connaissez les bases de Nomad, voyons le reste de l'interface.

## Interface {#interface}

![](/images/interface_overview1.webp)

* `Menus du haut` - Les menus qui donnent accès à la plupart des fonctionnalités de Nomad. Les menus en haut à gauche concernent surtout la scène et les objets, ceux en haut à droite sont liés aux outils. Sur les petits écrans, ces menus se regroupent pour gagner de la place.
* `Statistiques` - Des informations sur la scène, l'objet actuel, l'état du masque, l'utilisation de la mémoire.
* `Cube de navigation` - Une aide qui montre de quel côté vous regardez la sculpture, et un raccourci pour passer d'une vue à l'autre. Toucher le cube amène la vue sur le côté touché. Faire glisser le cube fait tourner la vue. Touchez les petites icônes à côté du cube pour cadrer l'objet actuel, revenir à la vue d'accueil par défaut, verrouiller la caméra, ou afficher ou masquer la grille. Dans l'application, il s'appelle le `Cube d'alignement`, et son apparence et sa position se règlent dans les [Réglages](settings.md#snap-cube).
* `Boîte à outils` - Les outils de Nomad sont accessibles depuis cette zone qui défile.
* `Barre d'outils de gauche` - Les curseurs de rayon et d'intensité pour la plupart des outils, des boutons propres à certains outils, et des raccourcis pour la symétrie, le mode alternatif/soustraction de l'outil, le lissage, le masque, le masquage, les groupes de faces, le gizmo et les options de peinture. Vous pouvez réorganiser les raccourcis dans le menu [Interface](interface.md#side-bar).
* `Barre d'outils du bas` - Des raccourcis vers des fonctionnalités courantes, expliqués ci-dessous.

::: tip Vous êtes gaucher ?
Vous pouvez inverser la position et l'ordre de toutes les barres d'outils, voir [Inverser la barre supérieure](interface.md#mirror-top-bar) et les options associées.
:::

## Barre d'outils du bas {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Annuler` - annule la dernière opération
* `Rétablir` - rétablit la dernière opération annulée
* `Historique` - donne accès aux options de l'historique, expliquées dans le menu [Historique](history.md).
* `Solo` - Affiche uniquement l'objet actuel, ou tous les objets
* `Rayons X` - Affiche tous les autres objets en mode rayons X, et l'objet actuel en plein. Un appui long ou un glissement vers le haut vous permet de choisir la matcap et la couleur des rayons X, et les objets concernés.
* `Voxel` - Un raccourci vers le bouton de remaillage du [Remaillage voxel](topology.md#voxel-remesher). Un appui long ou un glissement vers le haut affiche les options du remaillage voxel, comme la résolution.
* `Grille` - Affiche ou masque la grille. Un appui long ou un glissement vers le haut affiche les options de la grille, comme sa couleur et le magnétisme.
* `Filaire` - Affiche ou masque le maillage en filaire par-dessus le modèle. Un appui long ou un glissement vers le haut affiche les options du filaire.
* `Inspecteur` - Affiche des données supplémentaires sur le maillage actuel. Par défaut, il montre les UV, mais un appui long ou un glissement vers le haut vous permet d'inspecter d'autres propriétés si elles existent, et de choisir si elles s'affichent en arrière-plan ou sur le maillage.
* `Logs` - Affiche ou masque une fenêtre avec les journaux de débogage de Nomad.
* `Groupe de faces` - Affiche ou masque les groupes de faces par-dessus le modèle, voir l'outil [Groupe de faces](tools.md#facegroup).

Vous pouvez ajouter, retirer et réorganiser ces raccourcis dans le menu [Interface](interface.md#add-shortcuts-bottom).

## Et ensuite ? {#next-steps}

À vous de choisir ce que vous voulez apprendre ensuite, selon ce qui vous intéresse ! Voici quelques suggestions :

Vous voulez en savoir plus sur les outils de sculpture ? Rendez-vous dans la section [Outils](tools.md).

Vous voulez exporter vos modèles ? Ou importer des modèles pour sculpter dessus ? Ou créer des images de vos sculptures ? Rendez-vous dans la section [Fichiers](files.md).

Vous voulez mieux maîtriser le niveau de détail de votre sculpture ? Rendez-vous dans la section [Topologie](topology.md) pour découvrir la multirésolution et la décimation.

Vous voulez travailler avec plusieurs objets ? Assembler des objets simples et des primitives en une scène plus grande ? Rendez-vous dans la section [Scène](scene.md).

Vous voulez *tout* savoir sur Nomad ? Bon choix ! Ce manuel couvre tout Nomad, contient plein d'astuces et dispose d'une excellente recherche en haut de la page. Utilisez la navigation à gauche pour en apprendre davantage.

Si vous préférez la vidéo, Holger Schönischka a réalisé une énorme collection d'astuces pour Nomad sur YouTube : https://www.youtube.com/@ProcreateFX/videos


## Obtenir de l'aide {#getting-help}

Si vous avez encore des questions après avoir lu le manuel et regardé les tutoriels vidéo, il y a trois moyens principaux d'échanger avec d'autres utilisateurs de Nomad ou avec son développeur :

* Rendez-vous sur le forum : [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Rejoignez le serveur Discord de Nomad : [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Contactez directement le développeur à support@nomadsculpt.com
