# ![](/icons/scene.webp) Scène {#scene}

Ce menu vous permet de gérer les objets, les lumières, les caméras et les répéteurs dans Nomad. Il affiche la hiérarchie de la scène sous forme d'arborescence, d'où vous pouvez modifier de nombreux aspects de vos objets. Il sert aussi à créer de nouveaux objets, ainsi qu'à combiner et séparer des objets de différentes façons.


![](/images/scene_menu_summary.webp)


## Barre de raccourcis {#shortcut-bar}
| Action                 | Icône                             | Description                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Ajouter...](#add-menu) | ![](/icons/plus.webp)           | Affiche le [menu Ajouter](#add-menu) pour ajouter un objet à la scène                                               |
| Supprimer              | ![](/icons/trash.webp)           | Supprime les objets sélectionnés. Leurs enfants sont conservés.                                                     |
| Verrouiller            | ![](/icons/lock.webp)            | Rend les objets sélectionnés impossibles à sélectionner dans la vue 3d. Ils restent sélectionnables depuis l'arborescence. Verrouiller un groupe verrouille tout ce qu'il contient. Touchez à nouveau pour déverrouiller. |
| [Joindre](#join)       | ![](/icons/merge.webp)           | Réunit les objets sélectionnés en un seul objet, sans modifier la géométrie                                         |
| [Séparer...](#separate) | ![](/icons/separate.webp)       | Affiche la fenêtre [Séparer](#separate), pour diviser un objet en plusieurs objets. L'inverse de l'opération Joindre |
| [Booléen...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Affiche la fenêtre [Booléen](#boolean)                                                                         |
| Cloner                 | ![](/icons/clone.webp)           | Duplique les objets sélectionnés en nouveaux objets                                                                 |
| Instancier             | ![](/icons/link.webp)            | Duplique les objets sélectionnés sous forme d'instances : toute modification de forme sur l'une s'applique à toutes les instances. |
| Désinstancier          | ![](/icons/unlink.webp)          | Convertit une instance en forme unique : les modifications de forme ne sont plus copiées sur les autres instances   |
| Synchroniser           | ![](/icons/checked.webp)         | Quand cette case est cochée, les opérations s'appliquent à toutes les instances des objets sélectionnés, et pas seulement à ceux qui sont sélectionnés. Disponible uniquement quand la sélection contient des instances. L'[onglet Synchroniser](#sync) de la fenêtre `Avancé` définit quelles opérations suivent cette case. |

::: tip
Quand une opération affectera aussi les autres instances, une petite icône de lien s'affiche sur son bouton.
:::


## Arborescence {#tree-view}
![](/images/scene_treeview.webp) 

L'arborescence liste les objets, groupes, répéteurs, lumières et caméras de la scène. À côté du nom d'un maillage s'affiche son nombre de sommets, avec une icône de calque colorée s'il a des calques. Chaque ligne a ces boutons :

| Action       | Icône                      | Description              |
| :----------: | :------------------------: | :----------------------: |
| Nom          | ![](/icons/pencil.webp)   | Renomme l'objet. S'il est sélectionné, tous les objets sélectionnés sont renommés d'un coup, avec un numéro ajouté. Appui long pour le renommer avec ses enfants. |
| Sélectionner | ![](/icons/checked.webp)  | Sélectionne/désélectionne |
| Visible      | ![](/icons/eye_open.webp) | Affiche/cache            |
| Menu         | ![](/icons/more.webp)     | Affiche le [menu de l'objet](#object-menu) |

::: tip ASTUCE : sélectionner ou cacher rapidement de nombreux objets

Touchez l'icône de sélection pour basculer un seul objet, ou faites glisser verticalement sur la colonne de sélection pour sélectionner de nombreux objets. Vous pouvez faire de même avec la colonne de visibilité.

Un appui long sur l'icône de sélection ou de visibilité agit aussi sur les enfants.

:::

### En-tête de l'arborescence {#tree-view-header}

La ligne au-dessus de la liste propose quelques aides :

* ![](/icons/sort_down.webp) - replie ou déplie tous les groupes d'un coup.
* ![](/icons/preview.webp) - active ou désactive les `Aperçus des objets`, une petite vignette rendue pour chaque objet de la liste.
* ![](/icons/search.webp) - filtre la liste par nom.

### Manipuler l'arborescence {#tree-view-manipulation}

Faites un appui long sur un élément de l'arborescence jusqu'à ce qu'il soit mis en évidence. Vous pouvez alors le déplacer vers le haut ou vers le bas, ou le faire glisser sur un autre élément pour en faire un enfant de celui-ci.

Quand plusieurs éléments sont sélectionnés, l'un d'eux est la sélection principale et apparaît plus clair. Faites un appui long sur l'un d'eux puis faites-le glisser pour déplacer d'un coup tous les objets sélectionnés.

Quand vous sélectionnez un élément parent, tous ses enfants sont aussi sélectionnés par défaut. Toucher à nouveau le parent bascule entre la sélection du parent seul, ou du parent et de ses enfants.

Touchez deux fois un élément pour centrer la caméra dessus (voir [Avancé](#focus-on-item)).

### Menu de l'objet {#object-menu}

Toucher le bouton points de suspension (...) d'un objet dans l'arborescence affiche le menu de l'objet.
Beaucoup de ces options reprennent celles de la barre de raccourcis du haut, par commodité.

|       Action        |                        Icône                       | Description                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         Nom         |              ![](/icons/pencil.webp)           | Change le nom de l'objet                                                                                                                                                |
|    Désinstancier    |              ![](/icons/unlink.webp)           | Convertit une instance en forme unique : les modifications de forme ne sont plus copiées sur les autres instances.                                                     |
|     Instancier      |               ![](/icons/link.webp)            | Duplique l'objet sous forme d'instance : toute modification de forme sur l'une s'applique à toutes les instances.                                                      |
|       Cloner        |              ![](/icons/clone.webp)            | Duplique l'objet en un nouvel objet                                                                                                                                     |
|      Supprimer      |              ![](/icons/trash.webp)            | Supprime l'objet. Ses enfants sont conservés, sauf si `Enfants` est coché.                                                                                              |
|       Enfants       |            ![](/icons/hierarchy.webp)          | Quand cette case est cochée, `Instancier`, `Cloner` et `Supprimer` agissent aussi sur les enfants de l'objet.                                                           |
| Séparer par Parties |             ![](/icons/separate.webp)          | Si un objet est composé de parties non connectées, crée un objet séparé pour chacune d'elles. L'inverse de l'opération Joindre.                                         |
| Séparer par Groupes |            ![](/icons/group.webp)          | Si un objet a plusieurs groupes de faces, crée un objet séparé pour chaque groupe de faces.                                                                                 |
| Séparer par Calques |              ![](/icons/layer.webp)            | Si un objet a des calques, crée des objets séparés pour le maillage de base et pour chaque calque. Utile pour envoyer des blendshapes vers d'autres applications.       |
|  Joindre → Calques  | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Si plusieurs objets sont sélectionnés et ont la même topologie, les fusionne en calques de l'objet principal (les autres objets sont supprimés). Là encore, utile pour les blendshapes qui VIENNENT d'autres applications.<br><br> Notez que les calques sont désactivés par défaut. Activez-les si vous devez régler leurs curseurs. |
|  Courbe (Répéteur)  |              ![](/icons/curve.webp)            | Uniquement pour un tube ou un tour : ajoute un répéteur [Courbe](#curve) qui suit la même courbe, en enfant de l'objet.                                                  |
|        Tube         |             ![](/icons/tube.webp)              | Pour un tour, ajoute en enfant un [tube](tools.md#tube) qui suit son profil. Pour un cylindre, un cône ou un tore, le convertit en tube de même forme, pour pouvoir le courber le long d'une courbe. |




### Sélection multiple {#multiselection}
Sélectionner plusieurs objets permet deux choses :
- déplacer plusieurs objets à la fois avec l'outil Gizmo
- fusionner des objets avec les opérations Joindre et Booléen.

Dans l'arborescence, touchez l'icône de sélection de chaque objet, ou faites glisser le long de la colonne de sélection. Quand vous touchez les noms, maintenez le raccourci `Masque` (ou `Ctrl` sur un clavier) pour ajouter ou retirer un seul objet, ou maintenez le raccourci `Lisser` (ou `Shift`) pour sélectionner tous les objets entre l'objet courant et celui que vous touchez.

::: tip Sélection multiple rapide
Vous pouvez aussi faire une sélection multiple dans la vue 3d en maintenant le raccourci `Lisser` (ou `Shift`) et en touchant un autre maillage.

Vous pouvez désélectionner un objet en le touchant à nouveau (seulement si votre sélection contient plus d'un objet).
:::

Le Gizmo déplace tous les objets sélectionnés ensemble, voir [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Joindre {#join}
Cette option réunit simplement plusieurs objets sélectionnés en une seule entrée.
Les points et les UV plus proches que le [rayon de soudure](#weld-radius) sont fusionnés.

Vous trouverez un exemple en vidéo dans la section [Séparer](#separate).

## ![](/icons/bool_subtract_circle.webp) Booléen {#boolean}
![](/images/scene_boolean_menu.webp) 
Combine des objets en une seule surface.

`Fusion voxel` conserve le volume des objets et calcule de nouveaux polygones régulièrement répartis sur la surface. Grâce à cette étape de calcul, une fusion voxel s'en sort avec des géométries complexes, mais peut perdre les détails fins si la résolution visée n'est pas assez élevée.

`Booléen` essaie de laisser les polygones dans leur disposition d'origine, et les raccorde là où les objets se chevauchent. Le résultat peut être bien plus propre et net qu'une fusion voxel, mais il faut des maillages « étanches » : les objets ne doivent avoir ni trous ni formes défectueuses. Si ça échoue, une fusion voxel marche en général.

### Opérations booléennes {#boolean-operations}
La fusion voxel comme le booléen se basent sur la visibilité des objets pour choisir l'opération, comme le rappellent les indications en bas de la fenêtre :

#### Union {#union}
Les deux objets visibles donnent une **union** booléenne : les enveloppes extérieures des objets sont combinées, sans surfaces intérieures. ![](/images/boolean_union.webp)

#### Soustraction {#subtract}
Un objet caché = **soustraction** booléenne : l'objet caché est soustrait de l'objet visible. ![](/images/boolean_subtract.webp)

#### Intersection {#intersect}
Les deux objets cachés = **intersection** booléenne : crée une nouvelle forme uniquement là où les deux objets se chevauchent. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Fusion voxel {#voxel-merge-button}
Ce bouton lance une fusion voxel sur les objets sélectionnés. Sur un seul objet, il refait la topologie avec des polygones régulièrement répartis, ce qui est utile quand un objet a des polygones étirés. Les options ci-dessous fonctionnent comme celles du [Remaillage voxel](topology.md#voxel-remesher).

### Résolution {#resolution}
La résolution de la grille 3d de voxels utilisée pour le calcul. Quand vous changez cette valeur, un damier s'affiche sur l'objet pour prévisualiser la taille des polygones.

La pipette à côté du curseur reprend le détail à partir de la densité du maillage sous votre doigt. Le bouton à côté passe le curseur en `Longueur d’arête`, une taille dans le monde : la même valeur donne le même niveau de détail sur n'importe quel objet.

### Construire une multirésolution {#build-multiresolution}
Crée des niveaux de multirésolution sous votre résolution cible. Si votre résolution est de 400 et `Construire une multirésolution` est à 3, vous obtiendrez par exemple un nouveau maillage de 296 000 polygones, avec 3 niveaux de subdivision plus bas d'environ 74 000, 18 500 et 4 600 polygones.

### Épaissir les parties fines {#thicken-thin-parts}
Épaissit les parties trop fines pour la grille de voxels, pour qu'elles ne se cassent pas. Pas disponible avec `Arêtes vives` ou `Bordure vive`.

### Trous {#holes}
La façon dont les trous des objets ouverts sont bouchés avant la fusion :
* `Remplir` - chaque trou est bouché séparément, à partir de son bord.
* `Forme` - les trous sont bouchés en suivant la surface environnante, et les morceaux ouverts qui se chevauchent sont réunis.

### ![](/icons/angle.webp) Conserver les arêtes vives {#keep-sharp-edges}
Le bouton `Arêtes vives` aligne le maillage voxel sur les arêtes vives des objets. Ça fonctionne mieux sur des formes simples, et ça peut introduire des déformations par endroits.

### ![](/icons/group.webp) Bordure vive {#sharp-border}
Les nouvelles faces suivent les bordures des groupes de faces, et une bordure reste nette là où la surface forme un pli le long de celle-ci.

### ![](/icons/group_separate.webp) Séparer les groupes {#keep-groups-separate}
Chaque groupe de faces est remaillé séparément : les groupes ne fusionnent jamais, et chacun reste un morceau fermé dans son propre groupe. La multirésolution n'est pas construite dans ce mode.

### ![](/icons/bool_subtract_circle.webp) Bouton Booléen {#boolean-button}
Ce bouton lance une opération booléenne sur les polygones, avec la bibliothèque Manifold d'Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Nettoyer les chevauchements {#clean-overlaps}
Quand un seul objet est sélectionné, le bouton `Booléen` devient `Nettoyer les chevauchements` : il fusionne les parties de l'objet qui se croisent en une surface propre.


## ![](/icons/separate.webp) Séparer {#separate}
Si vous avez un seul objet composé de plusieurs parties non connectées, vous pouvez le séparer en plusieurs objets.
C'est l'opération inverse de [Joindre](#join).

La fenêtre `Séparer...` propose trois façons de séparer les objets sélectionnés :
* `Séparer par Parties` - crée un objet séparé pour chaque partie non connectée.
* `Séparer par Groupes` - crée un objet séparé pour chaque groupe de faces.
* `Séparer par Calques` - crée des objets séparés pour le maillage de base et pour chaque calque.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Ajouter {#add-menu}

![](/images/scene_addmenu_overview.webp)

Ce menu crée des primitives, des groupes, des caméras, des répéteurs et des lumières.

Les primitives sont des formes de base que vous pouvez ajuster avec des paramètres. Une fois la primitive réglée comme vous le souhaitez, vous la « validez » : ses paramètres sont alors figés dans un maillage polygonal que vous pouvez sculpter et peindre. Une fois validée, une primitive ne peut plus être réglée par ses paramètres.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Sur le Gizmo {#on-gizmo}
Place la nouvelle primitive là où se trouve la forme sélectionnée ou le Gizmo. Si l'option est désactivée, la primitive est placée au centre de la scène.

### ![](/icons/gizmo.webp) Sélectionner le Gizmo {#select-gizmo}
Passe automatiquement à l'outil Gizmo quand une nouvelle primitive est créée.

### ![](/icons/cog.webp) Avancé {#add-advanced}

Ce menu vous permet de choisir où créer les nouvelles primitives, les groupes et les répéteurs : sur l'objet sélectionné, à l'origine du monde, ou à l'emplacement du Gizmo.


### UV {#uvs}
Le bouton `UV` à côté du titre Primitive active les UV sur les primitives. Les UV (souvent appelés coordonnées de texture) sont des données supplémentaires utilisées en 3d pour appliquer des textures sur des surfaces. Ils prennent plus de mémoire, mais sur la plupart des appareils ce n'est pas un problème, sauf si vous montez à des nombres de polygones très élevés (par exemple 10 millions de polygones ou plus).

### Primitives {#primitives}

| Primitive          | Icône                                     | Description                                                                                                     |
| :----------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Boîte              | ![](/icons/cube.webp)                    | Un simple cube, dont vous réglez les divisions en X, Y et Z                                                     |
| Sphère quad        | ![](/icons/circle.webp)                  | Une boîte subdivisée avec l'option `Sphère` (projection sur une sphère) forcée : sa répartition de quads régulière est idéale pour sculpter |
| Cylindre           | ![](/icons/cylinder.webp)                | Vous pouvez ajouter un trou central au cylindre, par exemple pour faire un tuyau creux                         |
| Tore               | ![](/icons/torus.webp)                   | Le tore est un bon point de départ pour des anneaux                                                             |
| Cône               | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosaèdre          | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Sphère UV          | ![](/icons/circle.webp)                  | Une sphère à la répartition de polygones irrégulière, voir l'[avertissement plus bas](#uv-sphere)               |
| Plan               | ![](/icons/rectangle.webp)               | Un simple plan ; c'est la seule primitive qui n'est pas fermée                                                  |
| Texte              | ![](/icons/text.webp)                    | Du texte 3d, avec une police, un style, un alignement, une profondeur et une courbure. `Fusionner les lettres` soude les lettres qui se touchent |
| Tube               | ![](/icons/tube.webp)                    | voir [Tube](tools#tube)                                                                                         |
| Tour               | ![](/icons/lathe.webp)                   | voir [Tour](tools#lathe)                                                                                        |
| Triplanaire        | ![](/icons/triplanar.webp)               | voir [Triplanaire](#triplanar)                                                                                  |
| VDM                | ![](/icons/vdm.webp)                     | Un plan préparé pour sculpter un tampon de déplacement vectoriel : il a des UV et fait face à la caméra         |
| Capteur d'ombres   | ![](/icons/material_shadow_catcher.webp) | voir [Capteur d'ombres](#shadow-catcher)                                                                        |
| Tête               | ![](/icons/face.webp)                    | Une tête simple, avec un calque pour passer d'un visage masculin à féminin                                      |

::: tip
Si vous vous demandez ce qu'est le maillage de base au lancement de Nomad : c'est aussi une boîte subdivisée.
En revanche, le maillage de base de Nomad n'utilise pas l'option `Sphère`, il n'est donc pas parfaitement rond.
:::

### Barre d'outils de la primitive {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Une fois la primitive créée, une barre d'outils apparaît pour régler ses paramètres.

* `Valider` Fige la primitive en objet standard, pour pouvoir la sculpter et la peindre.
* `Miroir` Place ou retire un répéteur miroir au-dessus de la primitive.
* `Tout` (icône d'œil) Choisit quelles poignées sont affichées directement sur la primitive pour régler ses paramètres, comme la largeur du cube ou le rayon du trou d'un cylindre : `Aucun`, `Tout`, ou un seul type (rayon, trou, profil...) selon la primitive.
* `Division` Le nombre de divisions de la primitive, ici le long de X pour une boîte.
* `Densité constante` Quand vous étirez la primitive le long d'un axe avec le Gizmo, sa taille et ses divisions augmentent au lieu d'étirer les polygones : les faces restent carrées. Disponible sur les boîtes, les plans et les cylindres.
* `...` Affiche le menu de la primitive.

Selon la primitive, la barre d'outils propose des options supplémentaires :

* `Sphère` La sphère est construite à partir d'un cube subdivisé, plus adapté à la sculpture, mais du coup pas parfaitement rond. Cette option rapproche la forme d'une sphère parfaite. L'icosaèdre a aussi cette option.
* `Capuchon` Active ou désactive les extrémités fermées d'une forme : un cylindre peut par exemple être fermé en haut, en bas, des deux côtés ou pas du tout.
* `Trou` Crée un trou au centre d'une forme. Le bouton passe successivement de aucun trou, à un trou d'un seul rayon, puis à un trou de rayons différents en haut et en bas.
* `Rayon` Choisit si un cylindre a un seul rayon, ou un rayon différent en haut et en bas.
* `Disque` Choisit si un plan est une forme à 4 côtés ou un cercle.

La petite barre d'outils sous la barre principale permet de basculer entre le Gizmo de la primitive et le Gizmo de transformation.

::: tip

Toucher le titre de la barre d'outils la déplace en haut ou en bas de l'écran. Toucher la flèche dans le coin la replie.

:::


### Menu de la primitive {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Il contient tous les paramètres de la primitive sélectionnée. Les paramètres sont la description de base d'une forme. Pour décrire un anneau, par exemple, vous donneriez son rayon extérieur, son rayon intérieur et son nombre de polygones.

La plupart des paramètres de primitive parlent d'eux-mêmes, et certains sont communs à toutes les primitives :

* `UV` Le petit bouton UV en haut du menu active ou désactive la création des coordonnées UV
* `Valider` Le petit bouton Valider fige la primitive en objet standard, pour pouvoir la sculpter et la peindre.
* `Nombre max. de faces` Fixe une limite au nombre de polygones de l'objet, pour éviter de faire planter votre appareil.
* `Subdivision secondaire` Applique le nombre de subdivisions choisi, comme dans la section Multirésolution du menu Topologie. Associé à peu de divisions de topologie, cela donne des primitives lissées aux coins arrondis. Par exemple, une boîte avec 2 divisions de topologie et 4 subdivisions secondaires donne une boîte aux coins arrondis.
* `Subdivision linéaire` Définit combien de niveaux de subdivision linéaire utiliser avant de passer à la subdivision lissée classique. Cela permet de régler la netteté ou la douceur des coins des surfaces subdivisées. Par exemple, réglez une boîte sur 2 divisions de topologie et 4 subdivisions secondaires, puis faites varier la subdivision linéaire entre 0 et 4 : les coins de la boîte passent de doux à vifs.

### Topologie {#topology}

Règle le nombre de polygones d'une primitive. En général, les réglages sont liés : modifier le seul curseur actif ajuste tous les polygones de façon égale. Vous pouvez toucher le bouton de déliaison pour régler séparément les divisions X/Y/Z d'une forme.

### Géométrie {#geometry}

Règle la taille globale d'une primitive, en unités X/Y/Z pour les formes carrées, et en rayon pour les formes rondes.


### ![](/icons/circle.webp) Sphère UV {#uv-sphere}
::: warning
La Sphère UV n'est pas bien adaptée à la sculpture, surtout au niveau des pôles.

Préférez la [primitive](#primitives) Sphère quad, Boîte ou Icosaèdre, avec l'option `Sphère`.

Notez que la topologie peut être acceptable pour sculpter si vous utilisez une valeur très basse pour les curseurs `Division`.
Vous pouvez ensuite utiliser le curseur `Subdivision secondaire` pour augmenter le nombre de polygones.

Même si elle ne convient pas à la sculpture en général, elle est utile pour les yeux : si vous tournez la sphère pour que les pôles soient au niveau de la pupille, la répartition des polygones se prête naturellement à la peinture et à la sculpture de l'iris et de la pupille.
:::


### ![](/icons/triplanar.webp) Triplanaire {#triplanar}
Cette primitive est particulière : c'est avec l'[outil Masque](tools.md#mask) que vous façonnez sa géométrie.

![](/videos/triplanar.mp4)


::: tip
Touchez deux fois un plan et la caméra se centrera sur ce plan.
Cela ne fonctionne plus si vous faites pivoter la primitive avec le Gizmo.
:::

Le triplanaire utilise les informations de masque de 3 plans pour remplir une grille de voxels, qui est ensuite convertie en polygones (grâce au [Remaillage voxel](topology.md#voxel-remesher)).

Chaque plan a son propre plan de symétrie.

::: warning
Chaque fois que vous changez la taille de la primitive Triplanaire, la qualité du masque peint se dégrade.

Pour l'instant, il n'y a pas d'option pour « verrouiller » la peinture sur un seul plan, mais cela viendra peut-être.
Vous pouvez utiliser la [Topologie connectée](stroke.md#connected-topology) pour vous aider un peu : si votre curseur est précisément sur un plan, il n'affectera pas les autres.
:::

### ![](/icons/material_shadow_catcher.webp) Capteur d'ombres {#shadow-catcher}
Ajoute un plan avec le matériau capteur d'ombres. Voir [Matériau Capteur d'ombres](material.md#shadow-catcher) pour plus de détails.


## Groupe/Caméra {#groupcamera}
### ![](/icons/share.webp) Groupe {#group}
Crée un objet « vide », sous lequel vous pouvez placer d'autres objets. Cela sert simplement à organiser la hiérarchie, en rangeant de nombreux objets dans un groupe que vous refermez ensuite. Un groupe peut aussi aider à déplacer des objets : placez-en plusieurs sous un groupe, puis déplacez, faites pivoter ou redimensionnez le groupe avec l'outil Gizmo.

### ![](/icons/camera.webp) Caméra {#add-view}
Crée une caméra.

## Répéteurs {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Les répéteurs sont des nœuds qui créent des instances des objets placés sous eux.

### ![](/icons/array.webp) Réseau {#array}
![](/images/scene_primitive_array.webp)

Les objets placés en enfants de ce nœud peuvent être instanciés selon une grille. Quand il est sélectionné, il propose ces réglages :
* `Ajuster à l'intérieur` - activé, toutes les copies sont placées à l'intérieur des limites du réseau ; désactivé, les curseurs règlent l'espace entre les copies
* `Nombre X/Y/Z` - le nombre d'instances sur chaque axe
* `Taille X/Y/Z` - la taille de la grille sur chaque axe, ou la distance entre les copies quand `Ajuster à l'intérieur` est désactivé
* `Aléatoire...` - ajoute des variations aléatoires aux copies, voir [Aléatoire](#curve) plus bas.

### ![](/icons/curve.webp) Courbe {#curve}
![](/images/scene_primitive_curve.webp)
Crée une courbe : les enfants de ce nœud sont répétés le long de la courbe. Quand il est sélectionné, il propose ces réglages :
* `Courbe` - modifie la courbe : ajoutez des points à la courbe et déplacez ses points.
* `Afficher` - affiche ou cache la courbe et ses points.
* `Aligner` - accroche les points de la courbe à d'autres géométries.
* `Sym` - modifie la courbe de façon symétrique.
* `Fermé` - relie le début et la fin de la courbe, ou la laisse ouverte.
* `B-spline` - fait suivre exactement la courbe aux instances, ou utilise une interpolation B-spline, plus douce.
* `Déformer` - courbe chaque copie le long de la courbe, pour que les copies se rejoignent (`Lisse` courbe leurs côtés pour qu'elles se rejoignent sans angle).
* `Aligner` - fait pivoter les copies pour qu'elles suivent la direction de la courbe.
* `Pivot` - le pivot des copies : la courbe elle-même (`Elle-même`) ou ses enfants.
* `Nombre` - le nombre d'instances. Le bouton de mode à côté passe en `Distance` : un espacement fixe entre les copies, le nombre suivant la longueur de la courbe.
* `Rayon` - des réglages sur chaque point de la courbe pour définir l'échelle des instances.
* `Torsion` - des réglages sur chaque point de la courbe pour définir la rotation en torsion des instances.
* `Alterner` - fait tourner une copie sur deux autour de la courbe : 90° pour des maillons de chaîne, 180° pour des feuilles ou des dents de fermeture éclair, autour de l'`Axe` que vous choisissez.
* `Spirale...` - enroule les copies autour de la courbe, en plusieurs brins (corde, tresse, ruban...).
* `Aléatoire...` - ajoute des variations aléatoires aux copies ; chaque ligne peut à la place ajouter la même quantité à chaque copie.

Sous la barre d'outils, le bouton `(fusionner)` fusionne un point avec un autre quand vous le faites glisser dessus. `IK` (cinématique inverse) vous permet de poser la courbe : faites glisser un point et les points connectés suivent. Touchez un point pour le verrouiller ou le déverrouiller, faites un appui long pour les verrouiller ou déverrouiller tous ; les points verrouillés restent en place.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Les enfants de ce nœud sont instanciés en cercle. Déplacez l'objet enfant pour modifier le rayon de ce répéteur. Quand il est sélectionné, il propose ces réglages :
* Radial X/Y/Z - ces boutons définissent l'axe radial et le nombre d'instances.



### ![](/icons/mirror.webp) Miroir {#mirror}
![](/images/scene_primitive_mirror.webp)

Les enfants de ce nœud sont reflétés par rapport à un axe. Quand il est sélectionné, il propose ces réglages :
* Gizmo - active le Gizmo de transformation pour placer le centre du miroir. Vous pouvez aussi le faire pivoter et le redimensionner. Quand vous avez terminé, touchez à nouveau Gizmo pour retrouver les réglages habituels.
* X/Y/Z - définit le plan du miroir

### ![](/icons/surface.webp) Surface {#surface}

Les enfants de ce nœud sont copiés sur la surface d'un objet : une copie par face, par arête ou par sommet, ou dispersées au hasard. Quand il est sélectionné, il propose ces réglages :
* Mode - place les copies sur les `Faces`, les `Arêtes` ou les sommets, ou les `Disperser`.
* Tous les - une copie toutes les N faces, arêtes ou sommets. `Aléatoire` les choisit au hasard, et `Redistribuer` tire un autre ensemble aléatoire.
* Espacement - en mode dispersion, la distance minimale entre deux copies.
* Aligner - les copies se dressent sur la surface en suivant sa normale, au lieu de garder l'orientation de l'original.
* Accrocher - projette l'original sur le point de surface le plus proche ; les copies suivent.
* Adapter la taille, Cisaillement - redimensionne et étire les copies selon la forme de chaque face.
* Déformer - courbe chaque copie sur sa face, ou le long de son arête, pour que les copies voisines se rejoignent sans espace.

Tous les répéteurs ont un réglage `Valider`, qui fige le résultat du répéteur et vous demande comment procéder :
* Joindre les enfants - les instances sont réunies en un seul objet
* Conserver les instances - les instances restent des instances, mais n'ont plus le répéteur comme « parent »
* Désinstancier - les instances sont converties en objets uniques

`Tout aplatir` fige aussi les répéteurs imbriqués dans celui-ci, pour que chaque copie devienne un objet ordinaire.

::: tip Astuce : combiner les répéteurs
Les répéteurs peuvent être placés les uns sous les autres, et plusieurs objets peuvent être enfants d'un répéteur, ce qui permet des effets complexes.

![](/images/scene_repeater_combine.webp)
:::

::: tip Astuce : pivots des répéteurs

Certains répéteurs essaient de pivoter automatiquement les objets enfants : même si vous les déplacez ou les faites pivoter avec l'outil Gizmo, ils ne bougent pas. Pour passer outre, insérez un groupe entre le répéteur et l'enfant. Vous pouvez alors déplacer la forme enfant indépendamment du répéteur.
:::

## Lumière {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Directionnel {#directional}
Crée une lumière directionnelle, une source lumineuse infiniment éloignée, comme le soleil.

### ![](/icons/panorama.webp) Environnement {#environment}
Crée une lumière d'environnement, qui éclaire la scène à partir d'une image qui l'entoure entièrement (éclairage basé sur une image, comme une HDRI).

### ![](/icons/spotlight.webp) Projecteur {#spot}
Crée un projecteur, avec des réglages pour la largeur du cône et la douceur

### ![](/icons/light.webp) Point {#point}
Crée une lumière ponctuelle

## ![](/icons/cog.webp) Avancé {#advanced}
Le bouton `Avancé` en bas à gauche du panneau ouvre une fenêtre à deux onglets : `Général` et `Synchroniser`.

### ![](/icons/focus.webp) UI : focus au double appui {#focus-on-item}
Toucher deux fois un élément de la liste de la scène centre la caméra sur cet élément dans la vue 3d.

### ![](/icons/eye_open.webp) Synchroniser la visibilité {#sync-visibility}
Quand cette option est activée, l'icône d'œil d'un élément sélectionné agit sur tous les éléments sélectionnés.

### ![](/icons/bang.webp) Surbrillance {#highlight}
Met en surbrillance les objets sélectionnés dans la vue 3d quand la sélection change.

### ![](/icons/link.webp) Afficher (Instance) {#instance-show}
Affiche une capsule de couleur à gauche de la liste de la scène pour repérer les instances.

### ![](/icons/preview.webp) Aperçus des objets {#object-previews}
Affiche une vignette rendue pour chaque objet de la liste de la scène. C'est la même chose que le bouton d'aperçu au-dessus de la liste.

### Rayon de soudure {#weld-radius}
Sous le titre `Joindre`, `Rayon de soudure de position` et `Rayon de soudure UV` : les points et les UV plus proches que ces rayons sont fusionnés. Chacun peut être désactivé avec sa case à cocher. Cela s'applique à Joindre, Booléen, Découper, Décimer, aux remaillages et à l'import de fichiers.

### Icônes {#icons}
Règle la `Taille d'icône` min et max, et l'`Opacité` des icônes des groupes, lumières, caméras et répéteurs dans la vue 3d.

### ![](/icons/hierarchy.webp) Lignes hiérarchiques {#hierarchy-lines}
Affiche une ligne entre un parent et ses enfants dans la vue 3d. Quand l'option est activée, vous pouvez aussi régler :
* `Utiliser le pivot Nomad` - les lignes partent du pivot utilisé par les outils Transformation et Gizmo. Désactivé, elles utilisent le pivot de base naturel, qui peut être loin du centre de l'objet.
* `Épaisseur` - la largeur des lignes. Le bouton à côté du curseur leur ajoute un contour.
* La couleur des lignes.

### ![](/icons/link.webp) Synchroniser {#sync}
L'onglet `Synchroniser` définit, pour chaque opération (`Ajouter`, `Supprimer`, `Verrouiller`, `Cloner`, `Instancier`, `Désinstancier`, `Joindre`, `Séparer` et `Booléen`), si elle s'applique à toutes les instances de la sélection :
* `Auto` - suit la case `Synchroniser` en haut du menu Scène.
* `Non` - uniquement les objets sélectionnés.
* `Oui` - toujours toutes les instances.

Par défaut, `Joindre`, `Séparer` et `Booléen` sont sur `Oui` et les autres sur `Auto`. `Réinitialiser` rétablit ces valeurs par défaut.

## Barre d'outils du bas {#bottom-toolbar}
Ces icônes affichent ou cachent les groupes, lumières, caméras, répéteurs et lignes hiérarchiques dans la vue 3d. Les icônes affichées dans la vue peuvent être touchées pour les sélectionner et les modifier directement.
