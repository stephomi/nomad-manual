# ![](/icons/sliders.webp) Menu Interface {#interface-menu}

Ce menu regroupe de nombreuses options pour personnaliser l'interface de Nomad.

![](/images/interface_overview2.webp)

Nomad se personnalise en profondeur : ce menu est réparti sur 5 onglets, Interface, Raccourcis, Geste, Raccourcis clavier et Débogage.

![](/images/interface_menu.webp)


::: tip
Cette page décrit le menu Interface, pas l'interface elle-même ! L'interface générale est décrite dans [Prise en main](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interface {#interface}

L'onglet Interface règle les couleurs, la taille et la disposition de l'interface de Nomad. Il a deux sous-onglets, `Apparence` et `Disposition`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Couleurs {#presets}

![](/images/interface_presets.webp)

Le sous-onglet `Apparence` commence par une collection de préréglages de couleurs pour l'interface. Touchez-en un pour l'appliquer, puis affinez-le avec les options ci-dessous.

#### Accent et Base {#color-widgetcolor-base}
Les couleurs principales de l'interface : `Accent` pour les boutons sélectionnés et les barres des curseurs, `Base` pour les panneaux.

#### Opacité du texte {#text-opacity}
Adoucit le texte et les icônes sur le fond des panneaux.

#### Boutons à bascule, Case à cocher, Onglets {#high-contrast-button}
Le style des boutons à bascule (`Doux` ou `Plein`), des cases à cocher (`Contour`, `Accent` ou `Remplissage`) et des onglets (`Soulignement`, `Doux` ou `Plein`).

#### Outils colorés {#colored}
Colore les icônes par catégorie : par exemple, tous les outils de masque sont marron, les outils de découpe rouges, les outils d'aplatissement verts, etc.

#### Ombre des panneaux {#material-color-preview}
Les panneaux projettent une ombre pour se détacher de la scène.

#### Panneau transparent {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Quand cette option est activée, d'autres options apparaissent pour régler l'aspect des menus et des panneaux de Nomad : `Teinte des panneaux` définit leur couleur, `Intensité du flou` le flou appliqué à la scène derrière eux, et `Verre` ajoute une réfraction et des reflets sur les bords, surtout visibles avec un flou faible.

::: tip
Sur les petits écrans, il peut être utile de choisir une teinte de panneau presque blanche, transparente, avec un flou faible, pour que les menus ne cachent pas la scène.
:::

#### ![](/icons/reset.webp) Réinitialiser l’apparence {#reset-style}
Remet toutes les options d'apparence à leurs valeurs par défaut.

### ![](/icons/panel_detach.webp) Disposition {#layout}

Le sous-onglet `Disposition` règle l'emplacement et la taille des éléments.

#### Boîte à outils {#toolbox}

Les options de la boîte à outils, à droite de l'interface de Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Redimensionner {#ui-resize-corner}

Affiche ou cache une poignée de redimensionnement dans le coin inférieur de la boîte à outils.

##### Cachée {#hidden}
Normalement, l'icône de la boîte à outils dans la barre supérieure bascule entre une longue colonne unique et une liste d'outils sur plusieurs colonnes. Avec cette option, elle bascule entre la liste sur plusieurs colonnes et une boîte à outils cachée.

##### Réinitialiser l'ordre {#reset-order}
Remet les outils par défaut de la boîte à outils dans leur ordre d'origine. Les icônes personnalisées restent dans la boîte à outils, à la fin de la liste.

#### Barre supérieure {#rows-auto-1}
`Adaptatif` choisit ce que fait la barre supérieure quand elle ne tient pas à l'écran, ce qui concerne surtout les petits écrans : `Multiligne` répartit les menus sur plusieurs lignes, `Défilement` garde une seule ligne que vous pouvez faire défiler.

#### Inverser la barre supérieure {#mirror-top-bar}
Inverse l'ordre des menus dans la barre supérieure.

#### Inverser les barres latérales {#mirror-side-bars}
Échange les barres latérales : la boîte à outils passe à gauche et les options de l'outil à droite.

#### Inverser la barre inférieure {#mirror-bottom-bar}
Déplace la barre inférieure dans le coin inférieur droit et inverse l'ordre des boutons.

#### ![](/icons/move.webp) Glisser le panneau {#drag-panel}
Un panneau flottant se déplace toujours en faisant glisser sa barre ; cette option permet aussi de le faire glisser par son contenu. En `Auto`, un doigt ou un stylet ne déplace le panneau que si le glissement est plus horizontal que vertical, pour qu'un glissement vertical fasse toujours défiler le contenu. Réglez-la sur `Oui` pour pouvoir aussi le faire glisser à la souris, dans n'importe quelle direction.

#### ![](/icons/pencil.webp) Boîte de dialogue Nomad {#use-nomad-dialog}
Affiche la boîte de dialogue de texte de Nomad au lieu de celle du système quand vous saisissez un nom ou une valeur.

#### ![](/icons/stylus.webp) Point de survol {#hover-dot}
Affiche un petit point dans l'interface quand un stylet en survol est détecté.

#### ![](/icons/help.webp) Aide contextuelle au survol {#help-popup-on-hover}

Sur les appareils qui gèrent le survol, choisit si l'aide contextuelle de Nomad, représentée par l'icône ![](/icons/help.webp), apparaît au survol ou seulement quand vous la touchez.

#### Échelle globale {#overall-scale}
Un multiplicateur de taille appliqué à tous les éléments de l'interface.
#### Largeur des menus {#panel-width}
La largeur des menus et des panneaux.
#### Échelle du texte {#font-scale}
Change la taille du texte.
#### Espacement vertical {#vertical-spacing}
L'espacement entre les éléments des menus et des panneaux.
#### Espacement vertical (gauche) {#vertical-spacing-left}
L'espacement entre les éléments de la barre d'outils de gauche.

#### Décalages des bords {#edge-offset}
Ne modifiez ces valeurs que si vous avez du mal à utiliser les boutons situés sur les bords de l'écran. Si ces curseurs sont désactivés, Nomad utilise les valeurs de zone de sécurité fournies par l'appareil lui-même.

::: tip
Quand vous passez Nomad sur un nouvel appareil (par exemple d'un iPhone 12 à un iPhone 15), pensez à réinitialiser les décalages des bords à leurs valeurs par défaut !
:::

#### ![](/icons/reset.webp) Réinitialiser la disposition {#reset-layout}
Remet toutes les options de disposition à leurs valeurs par défaut.

## ![](/icons/window.webp) Raccourcis {#shortcuts}

L'onglet Raccourcis choisit quels boutons rapides apparaissent autour de la vue 3d, et vous permet de créer vos propres barres d'outils flottantes.

### Barre latérale {#side-bar}
Les boutons d'outils rapides en bas de la barre latérale gauche : `Lisser`, `Masque`, `Masquer`, `Groupe de faces` et `Gizmo`. Faites-les glisser pour changer leur ordre.

### Barre inférieure {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Touchez un raccourci pour l'ajouter à la barre inférieure, ou pour l'en retirer. Ceux-ci sont activés par défaut :
* `Annuler` - annule la dernière opération
* `Rétablir` - rétablit la dernière opération annulée
* `Solo` - Cache temporairement tous les autres objets, pour ne laisser visible que l'objet sélectionné. Appuyez à nouveau pour réafficher tous les objets.
* `Rayons X` - Rend temporairement tous les autres objets semi-transparents, seul l'objet sélectionné restant opaque. Appuyez à nouveau pour rétablir les matériaux par défaut.
* `Voxel` - Remaille l'objet courant avec la dernière résolution voxel utilisée. Un appui long ou un glissement vers le haut fait apparaître un curseur de résolution et un bouton pour les arêtes vives.
* `Grille` - Affiche ou cache la grille de la vue. Un appui long ou un glissement vers le haut vous permet de changer la couleur et l'opacité de la grille.
* `Filaire` - Affiche ou cache le filaire par-dessus le modèle. Un appui long ou un glissement vers le haut vous permet de changer la couleur et l'opacité du filaire.
* `Inspecter` - vous permet de voir des propriétés de votre maillage, comme les UV, les textures bakées ou d'autres propriétés, en surimpression sur l'arrière-plan de Nomad.
* `Groupe de faces` - Affiche ou cache les groupes de faces, plus d'infos dans [Outils->Groupe de faces](tools.md#facegroup)

D'autres raccourcis courants sont aussi disponibles : `Contour`, `Projection` (perspective ou orthographique), `MatCap`, `DynTopo`, ainsi que les boutons `Subdiviser`, `Inverser` et de niveaux de la [Multirésolution](topology.md#multiresolution).

#### ![](/icons/more.webp) Raccourcis clavier {#bindings-list}

Presque toutes les fonctions de Nomad peuvent être ajoutées à la barre inférieure grâce au bouton `Raccourcis`, qui indique combien de raccourcis contient la barre. Un menu de raccourcis s'affiche quand vous le touchez :

![](/images/interface_bindings_search.webp)

Vous pouvez chercher par catégorie avec les icônes du haut, ou utiliser le champ de recherche pour trouver une fonction par son nom. Touchez une fonction pour l'ajouter à la barre d'outils. Touchez-la à nouveau pour la retirer.

#### ![](/icons/eye_open.webp) Visible {#order}

Affiche ou cache toute la barre inférieure.

#### ![](/icons/reset.webp) Réinitialiser {#reset}

Remet la barre inférieure dans sa configuration par défaut.

### Fenêtres flottantes {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Le bouton + ajoute une barre d'outils flottante. Elle reste invisible tant que vous n'avez pas touché le bouton des raccourcis pour y ajouter des raccourcis ; vous pouvez ensuite la rendre visible.

Vous pouvez créer autant de barres d'outils que vous voulez, chacune ayant une ligne avec ces options :

* Faites glisser la poignée à gauche d'une ligne pour réordonner les barres d'outils.
* `Nom` - Le nom de la barre d'outils.
* `Visible` - Affiche ou cache la barre d'outils.
* `Barre` - Affiche une barre de titre sur la barre d'outils.
* `Interface réduite` - Garde la barre d'outils à l'écran quand l'interface est réduite.
* `Raccourcis` - Affiche la fenêtre des raccourcis pour choisir les fonctions à ajouter à la barre d'outils ou à en retirer.
* `Supprimer` - Supprime la barre d'outils.


## ![](/icons/gesture.webp) Geste {#gesture}
Le menu Geste règle la façon dont votre doigt, votre stylet, votre souris et votre pavé tactile contrôlent Nomad.

![](/images/interface_gesture.webp)

### Options des gestes {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad peut limiter les opérations selon le périphérique d'entrée. Par exemple, un glissement au doigt peut ne servir qu'à déplacer la caméra, tandis qu'un glissement au stylet ne sert qu'à sculpter. Si vous avez une souris ou un pavé tactile, vous pouvez aussi leur attribuer des opérations précises.

Chaque ligne est une opération : activez `Doigt`, `Stylet` et `Souris` pour choisir quelles entrées peuvent l'effectuer.

* `Caméra` - Déplacer la caméra.
* `Modification des nœuds` - Faire glisser les poignées dessinées dans la vue, par exemple pour modifier une primitive, une courbe, un répéteur ou une lumière.
* `Sculpter` - Sculpter avec les brosses. Les outils qui ont leur propre ligne plus bas suivent cette ligne à la place.
* `Sélectionner l'objet` - Toucher un objet pour le sélectionner.
* `Sélection de matériau` - Appui long dans la vue pour prélever la couleur ou le matériau sous le curseur. Ne fonctionne que si la peinture est activée sur la brosse courante.
* `Au toucher` - Les raccourcis au toucher d'outils comme Masque, Masquer et Groupe de faces (voir plus bas).
* `Peinture` - Les outils Peindre et Estomper.
* `Masque` - L'outil Masque.
* `Face` - Les outils Masquer et Groupe de faces.
* `Créer` - Les outils Tube, Tour et Insérer.
* `Couper` - Les outils Découper, Scinder et Projeter.
* `Sélectionner` - Les outils Sélectionner et Mesurer.
* `Gizmo` - Les outils Gizmo et Treillis.
* `Transformation` - Les outils Transformation et Disposer.

::: tip
Sur tablette, une configuration courante consiste à réserver la sculpture et la peinture au stylet, et à garder les doigts pour la caméra. Ainsi, votre paume ou un doigt égaré ne laisse jamais de trait sur votre modèle.
:::

### ![](/icons/tool_smooth.webp) Doigt : toujours lisser {#finger-always-smooths}
Quand cette option est activée, votre doigt lisse toujours tant qu'un outil de sculpture est actif, quelle que soit la brosse. L'activer retire `Doigt` de la ligne `Sculpter` : le stylet sculpte et le doigt lisse.

### Trait hors surface {#allow-air-stroke}
Permet de commencer un trait même si le curseur se pose d'abord à côté du maillage. Choisissez les outils concernés : `Outil` (toutes les autres brosses), `Lisser`, `Masque` et `Masquer`. Ne fonctionne que pour les entrées qui peuvent sculpter mais pas déplacer la caméra : ces boutons restent donc désactivés tant qu'aucune de vos entrées n'est réglée ainsi.

### ![](/icons/stroke.webp) Accrochage du trait {#stroke-snap}
Gardez le pointeur immobile à la fin d'un trait pour le transformer en ligne droite ou en courbe lisse. Continuez à glisser pour faire pivoter et redimensionner le trait accroché autour de son point de départ.

`Délai de maintien` définit combien de temps vous devez rester immobile avant que le trait ne s'accroche, ou avant qu'une forme ne passe en mode édition.

### ![](/icons/stylus.webp) Utiliser des échantillons d'entrée supplémentaires {#use-extra-input-samples}
Utilise les échantillons d'entrée supplémentaires fournis par l'appareil. Désactivez-la si vos traits sont saccadés ou si la pression se comporte mal. Cette option n'apparaît pas sur iOS.

### ![](/icons/tool_mask.webp) Masque {#mask}

![](/images/interface_gesture_mask.webp)

`Raccourcis en un appui` - Active les raccourcis en un appui suivants, sans avoir à maintenir le bouton Masque. Ils permettent ces gestes :
* toucher l'arrière-plan pour inverser le masque
* toucher une zone masquée pour flouter le masque
* toucher une zone non masquée pour rendre le masque plus net

#### Appui long {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Un appui long avec l'outil Masque bascule entre la brosse de masque et le lasso (SelMasque) :
* `Appui long - Sculpter` - Appui long, puis continuez à glisser : le trait est tracé avec l'autre mode, et le mode précédent revient à la fin du trait.
* `Appui long - Basculer` - Appui long puis relâchez sans bouger pour passer de l'un à l'autre.

### ![](/icons/tool_smooth.webp) Lisser {#smooth}
`Appui long - Lasso` - Un appui long avec l'outil Lisser passe à l'outil Sélectionner le temps du trait de sélection.

### ![](/icons/tool_hide.webp) Masquer {#hide}
![](/images/interface_gesture_hide.webp)

`Raccourcis en un appui` active les raccourcis suivants avec l'outil Masquer :
* Toucher un groupe de faces pour le cacher
* Toucher un espace vide pour inverser les polygones cachés

### ![](/icons/finger3.webp) Trois doigts {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Si votre appareil gère les gestes à 3 doigts, configurez ici les raccourcis de ce geste.

La grille d'options vous permet d'attribuer des raccourcis distincts aux glissements verticaux et horizontaux, ou `Non` pour ne rien leur attribuer. Notez que si le même geste est choisi pour 2 options, l'une est désactivée et son nom est barré.

* `Faire pivoter l'éclairage` - Fait pivoter l'environnement, les lumières et le MatCap.
* `Rayon de l'outil` - Modifie le rayon de l'outil.
* `Intensité de l'outil` - Modifie l'intensité de l'outil.

### ![](/icons/fingerprint.webp) Historique 2/3 {#history-23}
`Raccourcis de l'historique` - quand cette option est activée, les gestes suivants sont actifs :
* Annuler - toucher avec 2 doigts
* Rétablir - toucher avec 3 doigts

`Appui long` - quand cette option est activée, maintenir 2 ou 3 doigts posés annule ou rétablit en rafale.

### ![](/icons/mouse.webp) Molette de la souris {#mouse-wheel}
`Vitesse (zoom 3D)` règle la vitesse à laquelle la molette zoome dans la vue, et `Vitesse (interface 2D)` celle à laquelle elle fait défiler les menus et les panneaux. Le bouton moins à côté de chaque curseur inverse le sens.

### ![](/icons/fingerprint.webp) Pavé tactile {#trackpad}
Sur Mac, `Deux doigts` choisit ce que font deux doigts sur le pavé tactile. Le pincement zoome toujours et la rotation des doigts fait toujours pivoter la vue sur elle-même.
* `Désactivé` - Le défilement à deux doigts zoome, comme la molette de la souris. Les doigts ne sont pas suivis individuellement.
* `Panoramique` - Deux doigts déplacent la vue, et en lever un fait orbiter la vue. Comme sur une tablette.
* `Orbite` - Deux doigts font orbiter la vue, et en lever un la déplace.

### Accessibilité {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Fenêtre d'assistance` affiche une barre d'outils flottante pour contrôler le glissement, le pincement, la rotation et la caméra.

### Caméra {#camera}
Un raccourci vers le menu `Caméra` (les options de caméra étaient auparavant ici, mais ont été déplacées dans le menu Caméra).

### Double appui avec le stylet -> Raccourcis {#pencil-tap}

Un raccourci vers le menu `Raccourcis`, où vous définissez l'action du double appui avec le Pencil. En dehors d'iOS, il s'intitule `Bouton du stylet → Raccourcis`, pour le bouton du stylet.

### Ignorer la paume {#palm-rejection}
Sur téléphone et tablette, ignore les contacts dont la surface dépasse le `Seuil de taille max.`, comme la paume de votre main posée sur l'écran. Cela ne fonctionne pas forcément sur tous les appareils : désactivez-la si vous avez du mal à interagir avec la vue.


## ![](/icons/keyboard.webp) Raccourcis clavier {#bindings}
Les raccourcis clavier et de boutons se définissent dans ce menu :

![](/images/interface_bindings.webp)
Presque toutes les fonctions de Nomad peuvent être associées à des raccourcis clavier si votre appareil a un clavier, aux boutons supplémentaires de votre stylet, ou même à des manettes de jeu.

Pour créer un raccourci, touchez le rectangle à côté de la fonction, puis appuyez sur la touche ou le bouton voulu.

Trouvez les fonctions grâce aux icônes de catégorie en haut, ou avec la barre de recherche pour chercher par nom.

Chaque raccourci peut être désactivé avec la case à cocher à côté de son nom. Faites un appui long sur la case et faites glisser pour réordonner la liste.

Quand deux raccourcis activés utilisent la même combinaison, une icône ![](/icons/help.webp) apparaît à côté d'eux, avec la liste des fonctions en conflit.

### ![](/icons/more.webp) Menu contextuel {#context-menu}
L'icône ![](/icons/more.webp) après chaque raccourci ouvre un menu contextuel :

![](/images/interface_bindings_context.webp)

* `Cloner` - Clone le raccourci, par exemple pour donner un second raccourci à une fonction.
* `Réinitialiser` - Réinitialise le raccourci
* `Supprimer` - Supprime le raccourci. Possible seulement quand la fonction a plus d'un raccourci.

En dessous, certains raccourcis ont des options supplémentaires :

* `Touches rémanentes` - Pour les raccourcis d'outils et les raccourcis rapides (Masque, Lisser, Gizmo, Masquer, Groupe de faces, Ajouter/Soustraire), choisit comment un appui sur la touche change d'outil. `Auto` utilise la valeur par défaut définie dans les options [Avancé](#advanced).
  * `Maintenir` - Maintenez la touche pour utiliser l'outil, relâchez-la pour revenir à l'outil précédent.
  * `Basculer` - Appuyez une fois pour changer d'outil.
  * `Appui rapide` - Maintenez pour utiliser l'outil temporairement, ou appuyez brièvement pour passer à cet outil.
* `Retour au relâchement` - Pour les raccourcis rapides, choisit si relâcher une touche maintenue revient toujours à l'outil précédent, même quand cet outil était déjà actif.
* `Basculer vers l'outil précédent` - Pour les raccourcis d'outils, appuyer sur le raccourci de l'outil courant revient au dernier outil. Nécessite `Touches rémanentes` sur `Basculer` ou `Appui rapide`.
* `Position` - Pour les raccourcis de fenêtres flottantes, ouvre la fenêtre là où elle était (`Conserver`) ou sous le curseur (`Sur le curseur`).
* `Translation (au relâchement)` / `Zoom (au relâchement)` - Pour les raccourcis de zoom et de déplacement de la caméra, passe à l'autre mode quand vous relâchez la touche.
* Direction du glissement - Pour `Faire pivoter l'éclairage`, `Rayon de l'outil` et `Intensité de l'outil`, choisit un glissement horizontal ou vertical.
* `Synchroniser` - Pour les fonctions qui ajoutent, clonent ou instancient des objets, choisit si le résultat est synchronisé. Par défaut, c'est la valeur de synchronisation définie dans le menu Scène qui s'applique.
* `Sur l'arrière-plan` - Pour les raccourcis rapides Lisser et Masque, glissez sur l'arrière-plan en maintenant la touche pour tracer un lasso : un lasso de sélection pour Lisser, un lasso de masque pour Masque.
* `Forcer la caméra` - Pour les raccourcis de caméra, déplace la caméra même si la même combinaison est aussi utilisée par un autre raccourci, typiquement un raccourci d'outil ou Ajouter/Soustraire.
* `Rotation linéaire` - Pour le raccourci de rotation de la vue sur elle-même, la fait pivoter avec un glissement horizontal, vertical ou diagonal au lieu d'un mouvement autour du pivot.

::: tip
Avec `Appui rapide`, une seule touche fait les deux : maintenez-la pour lisser ou masquer rapidement et vous retrouvez votre brosse en la relâchant, ou appuyez brièvement pour rester sur cet outil.
:::

### ![](/icons/cog.webp) Avancé {#advanced}
En bas du menu des raccourcis clavier se trouve un menu engrenage pour les options avancées :

![](/images/interface_bindings_advanced.webp)

* `Raccourcis rapides` - Les valeurs par défaut de `Touches rémanentes` et `Retour au relâchement` pour les raccourcis Masque, Lisser, Gizmo, Masquer, Groupe de faces et Ajouter/Soustraire.
* `Raccourcis d'outils` - Les valeurs par défaut de `Touches rémanentes` et `Basculer vers l'outil précédent` pour les raccourcis d'outils. Avec `Basculer vers l'outil précédent`, vous pouvez alterner entre deux outils avec la même touche.
* `Fenêtre de raccourci` - Le mode `Touches rémanentes` des raccourcis qui affichent les fenêtres flottantes.
* `Inverser zoom Y` - Inverse le sens du glissement vertical quand vous zoomez avec un raccourci.
* `Rotation linéaire` - Fait pivoter la vue sur elle-même avec un glissement horizontal, vertical ou diagonal au lieu d'un mouvement autour du pivot.
* `SpaceMouse` - Active la prise en charge de la SpaceMouse de 3Dconnexion. Sur certains systèmes, des options supplémentaires apparaissent : ce qu'elle déplace (`Objet`, `Caméra`, `Première personne`, `Drone`), `Mise à jour auto du pivot` pour placer le pivot sur la surface sous le curseur quand elle commence à bouger, et ses vitesses de `Translation`, de `Zoom` et de `Rotation`.
* `Zones mortes (dérive)` - Pour les contrôleurs `Manette de jeu`, `Joystick` et `Bouton`. Augmentez ces valeurs si la caméra bouge alors que le contrôleur est au repos.
* `Rayon de l'outil` - Comment un glissement avec le raccourci de rayon redimensionne la brosse (`Cercle`, `Centre` ou `dx`), puis de combien les raccourcis de rayon augmentent (en pixels) ou multiplient le rayon à chaque appui.
* `Intensité de l'outil` - De combien les raccourcis d'intensité augmentent ou multiplient l'intensité à chaque appui.
* `Caméra - Vitesse` - La vitesse de `Translation` et de `Rotation` des raccourcis qui déplacent et font pivoter la vue.
* `Réinitialiser les raccourcis` - remet tous les raccourcis à leurs valeurs par défaut.
* `Réinitialiser l'ordre` - rétablit l'ordre par défaut de la liste des raccourcis.


## Affichage des raccourcis clavier ⌘ sur iOS {#ios-keyboard-shortcuts-display}

Sur les appareils iOS avec un clavier, maintenez la touche ⌘ (cmd) pour afficher la liste des raccourcis.

La prise en charge du clavier sur Android est encore un peu expérimentale.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Débogage {#debug}
Ce menu rassemble des options expérimentales et de débogage. Il vaut mieux laisser la plupart d'entre elles à leurs valeurs par défaut, et ne les modifier qu'après avoir contacté le support de Nomad. Les icônes du haut mènent directement à chaque section.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normaliser les UV` - Nomad normalise les UV du maillage sélectionné dans la tuile [0-1].

### ![](/icons/sun.webp) Ombrage {#render}
* `Écrire la profondeur de réfraction (arrière)` - La face arrière des maillages réfractifs est écrite dans le tampon de profondeur.
* `Normales lisses pondérées par l’angle` - Un ajustement du calcul de l'ombrage lisse qui peut éviter des plis dans certains cas.

### ![](/icons/speed.webp) IPS cible {#target-fps}
Quand cette option est désactivée, Nomad synchronise ses images par seconde avec la fréquence de rafraîchissement de votre écran.

Quand elle est activée, vous pouvez choisir le nombre d'images par seconde rendues par Nomad.

### ![](/icons/window.webp) Interface {#debug-interface}
* `Boîte à outils : tout afficher` - Nomad cache les outils qui ne servent pas pour la sélection courante : par exemple, toutes les brosses de sculpture sont cachées sur les primitives non validées. Cette option grise les outils désactivés au lieu de les cacher.

Les autres options d'interface qui se trouvaient ici sont maintenant dans l'onglet [Interface](#interface).

### ![](/icons/turntable.webp) Plateau tournant {#gif-turntable}
Nomad peut exporter un plateau tournant en GIF animé. Notez qu'à cause des limites du format GIF, la qualité est faible. Un enregistrement d'écran est en général une meilleure solution.

* `Durée` - la durée du plateau tournant, en secondes
* `Max. d'images accumulées` - Beaucoup des effets de rendu haute qualité de Nomad viennent de la combinaison de plusieurs images. Ce curseur règle combien d'images combiner, et sa case à cocher l'active ou le désactive.
* `Centre de rotation` - autour de quoi tourne la caméra : `Conserver` garde le pivot actuel, `(0, 0, 0)` utilise le centre du monde, `Scène` le centre de la scène.
* `Arrière-plan transparent` - Utilise la transparence pour les GIF. Notez que le GIF ne gère qu'une transparence sur 1 bit : les bords peuvent être fortement crénelés.
* `Exporter (GIF)` - lance l'export du GIF.

### ![](/icons/postprocess.webp) Post-traitement {#post-process}
* `Filtrage` - Option de débogage
* `Format` - Option de débogage
* `Réutiliser les tampons` - Option de débogage

### ![](/icons/ram.webp) Performances {#performance}
* `Multithread : général` - Option de débogage
* `Multithread : sculpture` - Option de débogage
* `Rendu des répétitions par instances` - Dessine toutes les copies d'un répéteur en un seul appel de rendu. Option de débogage.

### ![](/icons/star.webp) Fonctionnalité {#feature}
* `nom : compresser le multirés` - Réduit la taille des projets et des exports Nomad qui utilisent la multirésolution. Ces fichiers ne peuvent pas être ouverts par d'anciennes versions de Nomad. Cette option pourrait disparaître et être activée par défaut à l'avenir.
* `Inverser la diagonale des quads (au toucher)` - Option de débogage

### ![](/icons/bug.webp) Débogage {#dev}
* `Logs` - Ouvre une fenêtre de journal
* `Journaliser les événements` - Écrit vos événements de pointeur (doigt, stylet, souris) dans la fenêtre de journal, pour étudier les problèmes de saisie.
* `FPS` - ajoute un compteur d'images par seconde aux statistiques de la vue.
* `Fenêtre d’évaluation de l’app` - Option de débogage, sur iOS et Android.

### ![](/icons/image.webp) Icônes personnalisées {#custom-icons}
Remplace les icônes de Nomad par vos propres fichiers png.
* `Importer des icônes` - Importe des fichiers png dans `tmp_session/icons`. Chacun remplace l'icône de base du même nom. Ils sont abandonnés au redémarrage de Nomad.
* `Exporter les icônes d’outils` - Copie les icônes de base `tool_<tool>.png` dans `tmp_session/icons`, sans écraser les fichiers existants. Vous pouvez les y modifier puis les appliquer avec `Recharger les icônes`.
* `Recharger les icônes` - Applique les icônes de `tmp_session/icons`.

### Remaillage en quads {#quad-remesh}
Les options de remaillage en quads ne sont plus dans ce menu : voir [Remaillage en quads](topology.md#quad-remesh-instant) dans le menu Topologie et l'outil [Quad Remesher](tools.md#quad-remesher).

### Miniatures de boutique {#make-store-thumbnails}
Génère des captures d'écran aux tailles adaptées à l'App Store d'iOS.
