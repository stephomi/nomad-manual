# ![](/icons/interface.webp) Menu Interface 

Ce menu contrôle de nombreuses options pour personnaliser l’interface de Nomad. 

![](/images/interface_overview2.webp)

Nomad peut être personnalisé de manière très poussée, ce menu est divisé en 4 sections : Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Cette page concerne le menu d’interface, pas l’interface elle‑même ! L’interface générale est décrite dans [Getting Started](gettingstarted.md).
:::

## Interface 

La section Interface vous permet d’ajouter des raccourcis, de créer des barres d’outils flottantes et de contrôler la couleur, la taille et l’apparence de l’interface utilisateur de Nomad.

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

La barre d’outils du bas a ces raccourcis activés par défaut :
* `Undo` - annuler l’opération précédente
* `Redo` - restaurer l’opération précédemment annulée
* `Solo` - Masquer temporairement tous les autres objets, en ne laissant visible que l’objet sélectionné. Appuyez à nouveau pour restaurer tous les objets.
* `X-ray` - Rendre temporairement tous les autres objets semi‑transparents, en ne laissant que l’objet sélectionné en solide. Appuyez à nouveau pour restaurer les matériaux par défaut.
* `Voxel remesh` - Remesher l’objet courant en utilisant la dernière résolution de voxels utilisée. Un appui long ou un balayage vers le haut fera apparaître un curseur de résolution et une option pour les arêtes vives.
* `Grid` - Activer/désactiver la grille de vue. Un appui long ou un balayage vers le haut permet de changer la couleur et l’opacité de la grille.
* `Wireframe` - Activer/désactiver une superposition en fil de fer. Un appui long ou un balayage vers le haut permet de changer la couleur et l’opacité du fil de fer.
* `Inspector` - vous permet de voir les propriétés de votre maillage comme les UV, les textures « baked », et d’autres propriétés, superposées sur l’arrière‑plan de Nomad.
* `Face Group` - Activer/désactiver la superposition des facegroups, plus d’infos sous [Tools->FaceGroup](tools.md#facegroup) 

D’autres raccourcis couramment utilisés sont disponibles depuis ce menu, et beaucoup d’autres peuvent être trouvés dans le bouton Bindings.

#### ![](/icons/more.webp) Bindings

Presque toutes les fonctions de Nomad peuvent être ajoutées à la barre de raccourcis via le bouton Bindings. Un menu de bindings s’affiche lorsque le bouton est cliqué :

![](/images/interface_bindings_search.webp)

Vous pouvez rechercher par catégorie via les icônes en haut, ou utiliser le champ de recherche pour trouver des fonctions par nom. Cliquez sur une fonction pour l’ajouter à la barre d’outils. Cliquez à nouveau pour la retirer.

#### ![](/icons/list.webp) Order

Cela affichera une liste des raccourcis. Appui long puis glisser pour réorganiser les raccourcis.

#### ![](/icons/reset.webp) Reset

Reset restaurera la barre d’outils du bas à ses paramètres par défaut.

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

Cliquer sur le + ajoutera une barre d’outils flottante. Elle ne sera pas visible tant que vous n’aurez pas cliqué sur le bouton Bindings et ajouté des raccourcis, puis vous pourrez la rendre visible. 

Vous pouvez créer plusieurs barres d’outils, chacune dispose des options suivantes dans ce menu :

* ![](/icons/checked.webp) `Visible` - Activer/désactiver la visibilité de la barre d’outils
* ![](/icons/more.webp)`Bindings` - Afficher la fenêtre de bindings pour sélectionner les fonctions à ajouter ou retirer de la barre d’outils.
* ![](/icons/list.webp)`Order` - Afficher un menu pour réorganiser la barre d’outils.
* ![](/icons/reset.webp) `Reset` - Réinitialiser la barre d’outils à son état par défaut.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Activer une poignée de redimensionnement dans le coin inférieur droit de la barre d’outils.
* ![](/icons/sort_down.webp) `Collapsable` - Activer une poignée de repli dans le coin supérieur droit.
* ![](/icons/trash.webp) `Delete` - Supprimer la barre d’outils.

### Toolbox

Options pour le menu des outils à droite de l’interface de Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

Activer une poignée de redimensionnement dans le coin inférieur de la barre d’outils.

#### Hidden
Normalement, l’icône de toolbox dans la barre du haut bascule entre une longue colonne unique ou une liste multi‑colonnes d’outils. Cette option basculera entre la liste multi‑colonnes ou être masquée.

#### Colored
Colorer les icônes par catégorie, par ex. tous les outils de masque sont marron, les outils de découpe sont rouges, les outils de flatten sont verts, etc.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
Réinitialiser l’ordre des outils par défaut dans la toolbox. Les icônes personnalisées resteront dans la toolbox à la fin de la liste.


### Presets

![](/images/interface_presets.webp)

Une collection de préréglages de couleurs pour l’interface.

#### High-contrast button
Un style alternatif pour les boutons qui les rend plus visibles lorsqu’ils sont activés. Si réglé sur Auto, Nomad utilisera ce mode lorsque le contraste de couleur de l’UI entre activé/désactivé est faible.

#### Color widget/Color base
Les couleurs principales utilisées dans l’interface.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
Lorsqu’il est activé, des options supplémentaires apparaissent pour contrôler l’apparence des menus et panneaux dans Nomad. Leur couleur, transparence et quantité de flou peuvent être ajustées.

::: tip
Sur les petits appareils, il peut être utile de rendre le panneau de couleur presque blanc, transparent, et avec un flou faible, afin que les menus n’obstruent pas la scène.
:::

----

### Mirror top bar
Inverser l’ordre des menus dans la barre du haut.

### Mirror side bars
Inverser les barres latérales pour que la toolbox soit à gauche et les options d’outils à droite.

### Mirror bottom bar
Déplacer la barre du bas dans le coin inférieur droit et inverser l’ordre des boutons.

### Material color preview
Lorsque vous sélectionnez une couleur pour un matériau, un aperçu de ce matériau est affiché sur l’objet actuellement sélectionné.

----
### Help popup on hover

Pour les appareils qui prennent en charge le survol, permet de choisir si l’aide contextuelle de Nomad représentée par l’icône ![](/icons/help.webp) apparaît au survol ou seulement au clic.

----

### Overall scale
Un multiplicateur de taille pour tous les éléments de l’UI.
### Panel width
La largeur des menus et panneaux.
### Font scale
Échelle des polices.
### Vertical spacing
L’espacement entre les éléments dans les menus et panneaux.
### Vertical spacing (left)
L’espacement entre les éléments dans la barre d’outils de gauche.

----

### Edge offset
Vous ne devriez modifier ces valeurs que si vous avez des problèmes pour interagir avec les boutons sur les bords de l’écran. Si ces curseurs sont désactivés, Nomad utilisera les valeurs de zone sûre renvoyées par l’appareil lui‑même.

::: tip
Lors de la migration de Nomad vers un nouvel appareil (par ex. remplacement d’un iPhone 12 par un iPhone 15), assurez‑vous de réinitialiser les options de bord aux valeurs par défaut !
:::

### Reset style
Réinitialiser tous les éléments de l’UI à leurs valeurs par défaut.


## Gesture
Le menu Gesture contrôle la façon dont les pressions du stylet et des doigts contrôlent Nomad.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad peut limiter les opérations en fonction du périphérique d’entrée. Par exemple, un glisser du doigt peut uniquement déplacer la caméra, tandis qu’un glisser au stylet peut uniquement sculpter. Si vous avez une souris ou un trackpad, ils peuvent également être assignés pour contrôler des opérations spécifiques.

Nomad vous permet actuellement de définir ces modes pour être contrôlés par n’importe quelle combinaison de gestes au doigt, au stylet ou à la souris :

* Camera
* Sculpt
* Gizmo
* Material picking (via un appui long)
* Select object


`Finger always smooths` - Smooth peut être réglé pour ne fonctionner qu’avec un glisser du doigt.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Activer les raccourcis suivants en un seul tap sans avoir à maintenir le bouton Mask. Cela permet les gestes suivants :
* tap sur l’arrière‑plan pour inverser le masque
* tap sur une zone masquée pour flouter le masque
* tap sur une zone non masquée pour affûter le masque

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Un appui long basculera entre Mask et SelMask et commencera un nouveau trait. À la fin du trait, l’outil précédent est re‑sélectionné. 
* `Tool` - Appui long et relâchement sans bouger pour basculer entre Mask et SelMask. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` activera les raccourcis suivants avec l’outil Hide :
* Tap sur un face group pour le masquer
* Tap dans un espace vide pour inverser les polygones masqués

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

Si votre appareil prend en charge les gestes à 3 doigts, configurez des raccourcis pour ce geste. 

La matrice d’options vous permet de définir les glissements verticaux et horizontaux comme des raccourcis distincts. Notez que si le même geste est choisi pour 2 options, l’une sera désactivée.

* `Rotate lighting` - Faire tourner l’environnement, les lumières et le Matcap.
* `Tool Radius` - Modifier le rayon de l’outil.
* `Tool Intensity` - Modifier l’intensité de l’outil. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - lorsqu’il est activé, les gestes suivants sont actifs :
* Undo - tap avec 2 doigts
* Redo - tap avec 3 doigts

`Long press` - lorsqu’il est activé, maintenir 2/3 doigts enfoncés annulera/rétablira rapidement.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` fera apparaître une barre d’outils flottante pour contrôler les opérations de glisser, pincer, rouler et caméra.

### Camera
Un raccourci pour aller au menu `Camera` (les options de caméra se trouvaient ici auparavant, mais ont été déplacées dans le menu Camera).

### Pencil double tap -> Bindings 

Un raccourci pour aller au menu `Bindings` (les options de tap et double tap du Pencil se trouvaient ici auparavant, mais ont été déplacées dans le menu Bindings).


## Bindings
Les raccourcis clavier et boutons peuvent être définis depuis le menu Bindings :

![](/images/interface_bindings.webp)
Presque toutes les fonctions de Nomad peuvent être associées à des raccourcis clavier si votre appareil dispose d’un clavier, ou à des boutons supplémentaires sur votre stylet, ou même à des manettes de jeu.

Pour créer un binding, cliquez sur le rectangle à côté de la fonction, puis appuyez sur la touche/bouton. 

Trouvez des fonctions via les icônes de catégorie en haut, ou via la barre de recherche pour les trouver par nom. 

Les bindings individuels peuvent être désactivés via la case à cocher à côté du nom du binding.

### ![](/icons/more.webp) Context menu
L’icône ![](/icons/more.webp) après chaque binding ouvre un menu contextuel :

![](/images/interface_bindings_context.webp)

* `Clone` - Cloner le binding
* `Reset` - Réinitialiser le binding
* `Delete` - Supprimer le binding
* `Toggle shortcut on key tap` - Configurer si un tap vs un appui long sont traités différemment. Lorsqu’il est activé, un tap activera l’outil. Un appui long activera l’outil uniquement tant que la touche est enfoncée, puis au relâchement reviendra à l’outil précédent. Parfois appelé « sticky keys » dans d’autres applications 3D.

### Advanced
En bas du menu Bindings se trouve une icône d’engrenage pour les options avancées :

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Un tap des raccourcis standard pour mask, smooth, gizmo, hide, sub basculera vers ce mode, mais maintenir la touche enfoncée passera dans ce mode, puis au relâchement reviendra au mode précédent. Parfois appelé « sticky keys » dans d’autres applications 3D.
* `Toggle tool shortcuts` - Lors de l’utilisation d’un des raccourcis d’outils, si le même raccourci est pressé deux fois, il basculera vers l’outil précédent. De cette façon, vous pouvez continuer à échanger entre deux outils avec la même touche de raccourci.
* `Invert Y (Zooming)` - Inversera le zoom
* `Reset bindings` - réinitialiser tous les bindings à leurs valeurs par défaut.


## iOS ⌘ Keyboard shortcuts display

Sur les appareils iOS avec clavier, maintenez la touche ⌘ (cmd) pour afficher une liste de raccourcis.

La prise en charge des claviers sur Android est encore un peu expérimentale.

![](/images/shortcuts.webp)


## Debug
Certaines options expérimentales et de débogage sont stockées dans ce menu. Beaucoup de ces options devraient être laissées à leurs valeurs par défaut et ne modifiées qu’après avoir contacté le support Nomad.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - Nomad normalisera les UVs à l’intérieur de la tuile [0-1].

### Quad Remesh
* `Instant Mesh` - Activer l’algorithme de remesh instantané
* `Quadriflow` - Une méthode alternative de quad remesh.

### Render
* `Heightmap` - Changer le viewport pour rendre la profondeur de la scène. Cela peut être utilisé pour créer des alpha maps à utiliser pour les brosses.
* `Refraction write depth (back)` - La face arrière des maillages à réfraction sera écrite dans le depth buffer.
* `Flip Y (normal map)` - Inverser le canal y lors du baking des normal maps, requis pour certains moteurs de jeu et de rendu.
* `Angle weighted smooth normals` - Un ajustement de la façon dont l’ombrage lissé fonctionne, qui peut éviter des plis dans certains cas.

### Target FPS
Lorsqu’il est désactivé, Nomad synchronisera ses images par seconde avec le taux de rafraîchissement de votre écran.

Lorsqu’il est activé, vous pouvez définir le nombre d’images par seconde que Nomad rendra.

### Interface
* `Top: layout` 
  * Collapse: Sur les petits appareils, la barre du haut se repliera en sous‑menus supplémentaires. 
  * Scroll: Si vous êtes habitué à Nomad sur de grands écrans et préférez la disposition normale, activer ceci utilisera la barre du haut standard large, et elle pourra défiler.
  * Multiline: Afficher l’intégralité du menu du haut sur plusieurs lignes.
* `Bottom: draggable popup` - La barre d’outils du bas possède plusieurs boutons qui font apparaître une boîte de dialogue. Si cette option est activée, ces boîtes de dialogue peuvent être déplacées ailleurs à l’écran.  
* `Toolbox: show all` - Nomad masquera les outils qui ne sont pas pertinents pour la sélection actuelle, par ex. toutes les brosses de sculpture sont masquées sur les primitives qui ne sont pas validées. Cette option atténuera les outils désactivés plutôt que de les masquer.
* `Toolbox: colored` - Colorer les icônes de la toolbox en fonction de leur type.
* `Panel: Drop shadows` - Dessiner des ombres portées autour des menus et panneaux. Sur certains anciens appareils, cela peut impacter les performances.
* `Panel: Blending` - Option de débogage
* `Pointer: hovering dot` - Pour les appareils qui prennent en charge le survol du stylet, afficher un point lorsque le stylet survole les menus et panneaux.

### Gif turntable
Nomad peut exporter un turntable animé au format gif. Notez qu’en raison des limitations du format gif, la qualité est faible. L’enregistrement d’écran est généralement une meilleure méthode.

* `Duration` - durée en secondes du turntable
* `Rotation center` - où se trouve le pivot de la caméra, donc la partie de la scène autour de laquelle la caméra tournera
* `Transparent background` - Utiliser l’option de transparence pour les gifs. Notez que les gifs ne prennent en charge qu’une transparence 1 bit, donc les bords peuvent être fortement crénelés.
* `Max frame sampling` - Beaucoup des effets de rendu haute qualité de Nomad proviennent de la combinaison de plusieurs images. Ce curseur définit combien d’images combiner.
* `Export (GIF)` - démarrer le processus d’export gif.

### Post Process
* `Filtering` - Option de débogage
* `Format` - Option de débogage
* `Buffer reuse` - Option de débogage

### Performance
* `Multicore general` - Option de débogage
* `Multicore sculpting` - Option de débogage
* `Partial Drawing` - Fonction expérimentale ! À utiliser si vous sculptez une partie relativement petite d’un maillage haute‑poly. Cela devrait rendre la sculpture plus fluide, mais vous ne devez pas activer le wireframe ! Cela peut également ajouter des artefacts visuels pendant les coups de brosse.

### Feature
* `Flip quad split (on tap)` -  Option de débogage
* `Join: merge radius` - Les sommets seront automatiquement soudés s’ils sont suffisamment proches lorsque les maillages sont joints. Vous pouvez ajuster le rayon avec ce curseur.

### Debug
* `Logs` - Afficher une vue des logs
* `App review popup` - Option de débogage
* `FPS` - ajouter un compteur d’images par seconde aux statistiques du viewport.
