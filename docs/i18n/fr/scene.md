# ![](/icons/scene.webp) Scène {#scene}

Ce menu vous permet de gérer les objets, lumières, caméras et répéteurs dans Nomad. Il affiche la hiérarchie de la scène sous forme d’arborescence, ce qui vous permet de modifier de nombreux aspects de vos objets. Il permet également de créer de nouveaux objets, ainsi que de combiner et de séparer des objets de différentes manières.


![](/images/scene_menu_summary.webp)


## Barre de raccourcis {#shortcut-bar}
| Action                 | Icône                              | Description                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Ajouter...](#add-menu)    | ![](/icons/plus.webp)            | Affiche le [menu Ajouter](#add-menu) pour ajouter un objet à la scène                                                     |
| Supprimer                 | ![](/icons/trash.webp)           | Supprime l’objet                                                                                                   |
| Verrouiller                   | ![](/icons/lock.webp)            | Rend l’objet impossible à sélectionner dans la vue 3D. Il peut toujours être sélectionné depuis l’arborescence.                          |
| Fusionner                   | ![](/icons/merge.webp)           | Fusionne les objets sélectionnés en un seul objet sans modification de la géométrie                                             |
| Séparer               | ![](/icons/diagonal.webp)        | Si un objet est composé de coques de polygones distinctes, les sépare en plusieurs objets. L’inverse de l’opération de fusion |
| [Booléen...](#boolean) | ![](/icons/subtract_circle.webp) | Affiche le menu [Booléen](#boolean)                                                                                |
| Cloner                  | ![](/icons/clone.webp)           | Duplique l’objet dans un nouvel objet                                                                              |
| Instance               | ![](/icons/link.webp)            | Duplique l’objet en tant qu’instance, de sorte que les modifications de modélisation faites sur l’un soient répercutées sur toutes les instances.                         |
| Dés-instancier            | ![](/icons/unlink.webp)          | Convertit une instance en forme unique, de sorte que les modifications de modélisation ne soient plus copiées sur les autres instances                 |
| Synchroniser                   | ![](/icons/link.webp)            | Si les instances ont des enfants, s’assure que toutes les instances partagent la même hiérarchie d’enfants                                     |


## Vue arborescente {#tree-view}
![](/images/scene_treeview.webp) 

| Action       | Icône                       | Description              |
| :----------: | :------------------------: | :----------------------: |
| Sélectionner       | ![](/icons/checked.webp)  | Bascule sélection/non sélection |
| Visible      | ![](/icons/eye_open.webp) | Bascule la visibilité        |
| Menu         | ![](/icons/more.webp)     | Affiche le menu de l’objet      |

::: tip ASTUCE : Sélectionner ou masquer rapidement de nombreux objets

Touchez l’icône de sélection pour basculer un seul objet, ou faites glisser verticalement sur la colonne de sélection pour sélectionner plusieurs objets. Il est possible de faire la même chose avec la colonne de visibilité.

:::

### Manipulation de la vue arborescente {#tree-view-manipulation}

Effectuez un appui long sur un élément de l’arborescence jusqu’à ce qu’il devienne jaune. Vous pouvez ensuite le déplacer vers le haut ou vers le bas dans l’arborescence, ainsi que le faire glisser sur un autre élément pour en faire un enfant de cet élément.

Lorsque plusieurs éléments sont sélectionnés, la plupart seront d’un jaune foncé, un sera d’un jaune plus clair. Faites un appui long et faites glisser l’élément plus clair pour déplacer tous les objets en même temps.

Lorsque vous sélectionnez un élément parent, par défaut tous les éléments enfants seront également sélectionnés. Taper sur l’icône du parent basculera entre la sélection du seul parent, ou du parent et de ses enfants.

### Menu Objet {#object-menu}

Cliquer sur le bouton avec les points de suspension (...) pour un objet dans l’arborescence affichera le menu de l’objet. 
Beaucoup de ces options sont similaires à la barre de raccourcis en haut, répétées pour plus de commodité.

|       Action        |                        Icône                        | Description                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instance       |               ![](/icons/link.webp)            | Duplique l’objet en tant qu’instance, de sorte que les modifications de modélisation faites sur l’un soient répercutées sur toutes les instances.                                                                             |
|        Cloner        |              ![](/icons/clone.webp)            | Duplique l’objet dans un nouvel objet                                                                                                                                  |
|        Nom         |              ![](/icons/pencil.webp)           | Modifie le nom de l’objet                                                                                                                                           |
|       Supprimer        |              ![](/icons/trash.webp)            | Supprime l’objet                                                                                                                                                       |
|       Supprimer+       |            ![](/icons/removeNode.webp)         | Supprime l’objet et ses enfants                                                                                                                                      |
|     Dés-instancier     |              ![](/icons/unlink.webp)           | Convertit une instance en forme unique, de sorte que les modifications de modélisation ne soient plus copiées sur les autres instances.                                                                    |
|  Séparer la topologie  |             ![](/icons/separate.webp)          | Si un objet est composé de coques de polygones distinctes, les sépare en plusieurs objets. L’inverse de l’opération de fusion.                                                    |
| Séparer par groupe de faces |            ![](/icons/faceGroup.webp)          | Si un objet possède plusieurs groupes de faces, sépare le maillage en plusieurs objets.                                                                                            |
|   Séparer par calques   |              ![](/icons/layer.webp)            | Si un objet possède des calques, sépare chaque calque en un objet distinct. Utile pour envoyer des blendshapes vers d’autres applications.                                                 |
|   Fusionner -> Calques    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Si plusieurs objets sont sélectionnés et ont une topologie correspondante, fusionne ces objets en calques pour l’objet principal (les autres objets seront supprimés). À nouveau utile pour des blendshapes provenant D’AUTRES applications.<br><br> Notez que les calques seront désactivés par défaut. Activez-les si vous devez ajuster leurs curseurs. |




### Multisélection {#multiselection}
Vous pouvez sélectionner plusieurs objets pour deux raisons :
- utiliser l’outil de gizmo pour déplacer plusieurs objets à la fois
- fusionner des objets à l’aide des opérations de fusion et booléennes.

Vous pouvez le faire en utilisant la case à cocher `Multiselection`, puis en cliquant sur l’objet dans la liste.

::: tip Multisélection rapide
Vous pouvez également faire une multisélection dans la vue 3D en maintenant le raccourci `Smooth` et en touchant un autre maillage.

Vous pouvez désélectionner un objet en le touchant à nouveau (uniquement si votre sélection contient plus d’un objet).
:::

::: warning Fonctionnalité limitée du gizmo
Lors de l’utilisation de la multisélection, l’outil de gizmo ignorera toujours le masquage.
De plus, l’échelle X/Y/Z est désactivée.

La raison est que la multisélection ne permet que la transformation de maillages entiers, pas la transformation par sommet.
Cela pourrait être amélioré à l’avenir.
:::


## Fusionner {#join}
Cette option créera simplement une seule entrée d’objet à partir de plusieurs objets sélectionnés.

Vous pouvez voir un exemple en vidéo dans la section [Séparer](#separate).

## Booléen {#boolean}
![](/images/scene_boolean_menu.webp) 
Combine des objets en une seule surface.

`Voxel merge` conservera le volume des objets et calculera de nouveaux polygones régulièrement espacés sur la surface. En raison de l’étape de calcul, une fusion voxel peut gérer une géométrie complexe, mais peut perdre des détails fins si la résolution cible n’est pas suffisamment élevée.

`Boolean` tentera de conserver la disposition d’origine des polygones et de recoudre les polygones là où les objets se chevauchent. Cela peut produire des résultats beaucoup plus propres et plus nets qu’une fusion voxel, cependant cela nécessite des maillages « étanches » ; il ne peut pas y avoir de trous ou de formes mal formées dans les objets. Si cela échoue, une fusion voxel fonctionnera généralement.

### Opérations booléennes {#boolean-operations}
La fusion voxel et le booléen utiliseront toutes deux la visibilité des objets pour contrôler l’opération :

#### Union {#union}
Les deux objets visibles créeront une **union** booléenne, la peau extérieure des objets est combinée, sans surfaces intérieures. ![](/images/boolean_union.webp)

#### Soustraire {#subtract}
Un objet invisible = **soustraction** booléenne, l’objet invisible sera soustrait de l’objet visible. ![](/images/boolean_subtract.webp)

#### Intersection {#intersect}
Les deux objets invisibles = **intersection** booléenne, crée une nouvelle forme uniquement là où les deux objets se chevauchent. ![](/images/boolean_intersect.webp)


### Bouton Fusion Voxel {#voxel-merge-button}
Appuyer sur ce bouton effectuera une opération de fusion voxel sur les objets sélectionnés. Lorsqu’elle est effectuée sur un seul objet, elle le retopologise en polygones régulièrement espacés, ce qui est utile lorsqu’un objet possède des polygones étirés.

### Résolution {#resolution}
La résolution de la grille 3D voxel utilisée pour effectuer le calcul. Lorsque cette valeur est modifiée, un motif en damier est superposé sur l’objet pour prévisualiser la taille des polygones.

### Construire une multirésolution {#build-multiresolution}
Crée des niveaux de multi-résolution en dessous de votre résolution cible. Ainsi, si votre résolution est de 400 et que « build multiresolution » est à 3, vous obtiendrez un nouveau maillage avec, disons, 296 000 polygones, mais il y aura 3 niveaux de subdivision inférieurs à 74 000, 18 000, 4 000.

### Conserver les arêtes vives {#keep-sharp-edges}
Active l’alignement du maillage voxel sur les arêtes. Cela fonctionne mieux sur des formes simples.

### Bouton Booléen {#boolean-button}
Appuyer sur ce bouton effectuera une opération booléenne polygonale en utilisant la bibliothèque Manifold d’Emmett Lalish. 


## Séparer {#separate}
Si vous avez un seul objet basé sur plusieurs parties non connectées, vous pouvez scinder cet objet en plusieurs objets. 
Cela peut être vu comme l’opposé de la [fusion simple](#simple-merge).

![](/videos/merge_separate.mp4)


## Menu Ajouter {#add-menu}

![](/images/scene_addmenu_overview.webp)

Ce menu permet de créer des primitives, groupes, caméras, répéteurs et lumières.

Les primitives sont des types de formes de base qui peuvent être ajustées à l’aide de paramètres. Une fois que vous avez ajusté la primitive selon vos besoins, vous la « validez », ce qui convertit ces paramètres en un maillage polygonal qui peut être sculpté et peint. Une primitive ne peut plus voir ses paramètres ajustés après avoir été validée.


![](/images/scene_addmenu_top.webp)

### Sur le gizmo {#on-gizmo}
Active le placement de la nouvelle primitive à l’endroit de la forme ou du gizmo actuellement sélectionné. Lorsque cette option est désactivée, la primitive est placée au centre de la scène.

### Sélection du gizmo {#select-gizmo}
Active le passage automatique à l’outil de gizmo lorsqu’une nouvelle primitive est créée. 

### Avancé {#add-advanced}

Ce menu vous permet de définir votre préférence pour l’endroit où les nouvelles primitives, groupes et répéteurs seront créés. Ils peuvent être créés sur l’objet sélectionné, à l’origine du monde, ou à l’emplacement du gizmo.


### UV {#uvs}
Active les UV sur les primitives. Les UV (souvent appelées coordonnées de texture) sont des données supplémentaires utilisées en 3D pour permettre l’application de textures sur les surfaces. Elles consomment plus de mémoire, mais pour la plupart des appareils cela ne devrait pas être un problème, sauf si vous atteignez des nombres de polygones très élevés (par ex. 10 millions de polygones ou plus). 

### Primitives {#primitives}

| Primitive      | Icône                                      | Description                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | C’est un simple cube, vous pouvez contrôler la division en X, Y et Z                                                  |
| Sphere         | ![](/icons/circle.webp)                  | Par commodité, elle est appelée Sphere mais il s’agit en réalité d’un cube subdivisé, avec `Project on sphere` forcé |
| Cylinder       | ![](/icons/cylinder.webp)                | Vous pouvez ajouter un trou central pour la primitive cylindre, par exemple pour faire un tuyau creux                        |
| Torus          | ![](/icons/torus.webp)                   | Le tore peut être un bon point de départ pour des anneaux                                                                |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-sphere      | ![](/icons/circle.webp)                  | Une sphère avec une topologie de polygones irrégulière, voir [avertissement ci-dessous](#uv-sphere)                                               |
| Plane          | ![](/icons/rectangle.webp)               | C’est un simple plan, notez que c’est la seule primitive qui n’est pas fermée                                    |
| Tube           | ![](/icons/tool_tube.webp)               | voir [Tube](tools#tube)                                                                                          |
| Lathe          | ![](/icons/tool_lathe.webp)              | voir [Lathe](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | voir [Triplanar](#triplanar)                                                                                     |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | voir [Shadow Catcher](#shadow-catcher)                                                                           |
| Head           | ![](/icons/face.webp)                    | Une tête simple avec un calque pour faire la transition entre masculin/féminin                                                         |

::: tip
Si vous vous demandez quelle est la base mesh au lancement de Nomad : il s’agit également d’un cube subdivisé.
Cependant, la base mesh de Nomad n’utilise pas `Project on sphere`, ce qui signifie qu’elle n’est pas parfaitement ronde.
:::

### Barre d’outils des primitives {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Une fois une primitive créée, une barre d’outils apparaît pour contrôler ses paramètres.

* `Validate` Convertit la primitive en objet standard afin qu’elle puisse être sculptée et peinte.
* `Edit` Bascule l’affichage du gizmo de la primitive. Celui-ci est affiché directement sur la primitive pour contrôler ses paramètres, par ex. la largeur du cube ou le rayon du trou d’un cylindre.
* `Mirror` Bascule la mise en place d’un répéteur miroir au-dessus de la primitive.
* `...` Affiche le menu de la primitive.

Différentes primitives auront des options supplémentaires sur la barre d’outils :

* `Project` La sphère est construite comme un cube subdivisé, ce qui est meilleur pour la sculpture, mais cela signifie qu’elle n’est pas parfaitement ronde. Cette option forcera la forme à se rapprocher d’une sphère parfaite. L’icosahedron partage cette option.
* `Cap` Bascule les capuchons d’extrémité sur une forme, par ex. un cylindre peut avoir des capuchons en haut, en bas, les deux, ou aucun.
* `Hole` Bascule la création d’un trou au centre d’une forme. Cela fera défiler : pas de trou, trou avec un seul rayon, ou trou avec des rayons différents en haut et en bas.
* `Radius` Bascule si un cylindre doit avoir un seul rayon, ou un rayon différent en haut et en bas.
* `Disk` Bascule si un plan doit être une forme à 4 côtés ou une forme circulaire.

La petite barre d’outils sous la barre principale vous permet de basculer entre le gizmo de primitive et le gizmo de transformation.

::: tip

Cliquer sur le titre de la barre d’outils la basculera en haut ou en bas de l’écran. Cliquer sur la flèche dans le coin la réduira.

:::


### Menu des primitives {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Il contient tous les paramètres de la primitive sélectionnée. Les paramètres sont les descriptions de base d’une forme. Pour décrire un anneau, par exemple, vous décririez son rayon extérieur, son rayon intérieur et le nombre de polygones.

La plupart des paramètres de primitives devraient être explicites, et certains paramètres sont communs à toutes les primitives :

* `UVs` Le petit bouton UVs en haut du menu bascule la création des coordonnées UV
* `Validate` Le petit bouton Validate convertit la primitive en objet standard afin qu’elle puisse être sculptée et peinte.
* `Max faces` Définit une limite supérieure au nombre de polygones de l’objet pour éviter de faire planter votre appareil.
* `Post subdivision` Active le nombre de subdivisions choisi dans la section multi-résolution du menu de topologie. Cela peut être utilisé pour créer des primitives aux coins adoucis en combinaison avec de faibles divisions de topologie. Par exemple, définir les divisions de topologie d’un cube à 2 et les subdivisions post à 4 créera un cube aux coins arrondis.
* `Linear subdivision` Définit combien de niveaux de subdivision linéaire utiliser avant d’utiliser la subdivision lissée classique. Cela peut être utilisé pour contrôler à quel point les coins des surfaces subdivisées sont nets ou doux. Par ex., définissez les divisions de topologie d’un cube à 2, les subdivisions post à 4, puis essayez de changer les subdivisions linéaires entre 0 et 4. Les coins du cube passeront de doux à nets.

### Topologie {#topology}

Cela contrôle le nombre de polygones d’une primitive. En général, les contrôles sont liés, donc la modification du seul curseur actif ajustera tous les polygones de manière uniforme. Vous pouvez toucher le bouton de déliaison et contrôler séparément les divisions X/Y/Z d’une forme.

### Géométrie {#geometry}

Cela contrôle la taille globale d’une primitive, en unités X/Y/Z pour les formes carrées, et en rayon pour les formes rondes.


### Sphère UV {#uv-sphere}
::: warning
La UV Sphere n’est pas bien adaptée à la sculpture, en particulier aux pôles.

Veuillez privilégier les primitives [Sphere](#sphere), [Box](#box) ou [Icosahedron](#icosahedron), avec l’option `Project on sphere`.

Notez que la topologie peut être acceptable pour la sculpture si vous utilisez une valeur très faible pour les curseurs `Division`.
Vous pouvez ensuite utiliser le curseur `Overall Subdivision` pour augmenter le nombre de polygones.

Bien qu’elle ne soit pas adaptée à la sculpture générale, elle est utile pour les yeux ; si vous faites pivoter la sphère de sorte que les pôles se trouvent au niveau de la pupille, la disposition des polygones s’adaptera naturellement à la peinture et à la sculpture de l’iris et de la pupille.
:::


### Triplanaire {#triplanar}
Cette primitive est particulière en ce sens que vous devez utiliser l’[outil de masquage](tools.md#mask) dessus pour façonner la géométrie.

![](/videos/triplanar.mp4)


::: tip
Double-tapez sur un plan et la caméra se focalisera sur ce plan en particulier.
Cela ne fonctionnera pas si vous faites pivoter la primitive avec le gizmo.
:::

Triplanar utilise les informations de masque de 3 plans pour remplir une grille voxel qui est ensuite polygonisée (grâce au [Voxel Remesher](topology.md#voxel-remeshere)).

Chaque plan possède son propre plan de symétrie.

::: warning
Chaque fois que vous mettez à jour la taille de la primitive Triplanar, la qualité de la peinture de masque se dégrade.

Pour l’instant, il n’y a pas d’option pour « verrouiller » la peinture sur un seul plan, mais cela pourrait arriver à l’avenir.
Vous pouvez utiliser la [Connected Topology](stroke.md#connected-topology) pour aider un peu, dans le sens où si votre curseur se trouve précisément sur un plan, il n’affectera pas les autres plans.
:::

### Capteur d’ombre {#shadow-catcher}
Ajoute un plan avec le matériau Shadow Catcher. Voir [matériau Shadow Catcher](material.md#shadow-catcher) pour plus de détails. 


## Groupe/Appareil photo {#groupcamera}
### Groupe {#group}
Crée un objet « vide » sous lequel vous pouvez placer d’autres objets en tant qu’enfants. Cela peut être utilisé simplement pour organiser la hiérarchie en plaçant de nombreux objets sous un groupe, puis en le repliant. Un groupe peut également servir d’aide pour déplacer des objets ; de nombreux objets peuvent être placés sous un groupe, puis le groupe peut être déplacé, pivoté, mis à l’échelle avec l’outil de gizmo.

### Ajouter une vue {#add-view}
Crée une caméra.

## Répéteurs {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Les répéteurs sont des nœuds qui créent des instances des objets placés en dessous.

### Tableau {#array}
![](/images/scene_primitive_array.webp)

Lorsque des objets sont rendus enfants de ce nœud, ils peuvent être instanciés dans une disposition en grille. Lorsqu’il est sélectionné, il possède des contrôles pour :
* Fit inside – bascule entre le contrôle de la taille de la grille/boîte de l’array, ou le contrôle de l’espace entre les instances de l’array
* CountX/Y/Z – le nombre d’instances sur chaque axe
* OffsetX/Y/Z – la distance entre les instances lorsque Fit inside est activé
* SizeX/Y/Z – la largeur/hauteur/profondeur de la grille totale de l’array lorsque Fit inside est activé.

### Courbe {#curve}
![](/images/scene_primitive_curve.webp)
Cela crée une courbe, les enfants de ce nœud seront répétés le long de la courbe. Lorsqu’il est sélectionné, il possède des contrôles pour :
* Edit – permet d’ajouter des points à la courbe et de déplacer les points sur la courbe.
* Snap – aligne les points de la courbe sur d’autres géométries
* Align – fait pivoter les formes enfants pour les aligner dans la direction de la courbe
* Count – le nombre d’instances
* Closed – bascule la courbe entre fermée (début et fin reliés) ou ouverte
* Radius – active des contrôles sur chaque point de la courbe pour contrôler l’échelle des instances
* Twist – active des contrôles sur chaque point de la courbe pour contrôler la rotation de torsion des instances 
* B-spline – bascule entre le suivi exact de la courbe par les instances, ou l’utilisation d’une interpolation B-spline qui donne des résultats plus doux. 

### Radial {#radial}
![](/images/scene_primitive_radial.webp)

Les enfants de ce nœud seront instanciés en cercle. Déplacez l’objet enfant pour modifier le rayon de ce répéteur. Lorsqu’il est sélectionné, il possède des contrôles pour :
* RadialX/Y/Z – sélectionner ces boutons définira l’axe radial et le nombre d’instances.



### Miroir {#mirror}
![](/images/scene_primitive_mirror.webp)

Les enfants de ce nœud seront mis en miroir à travers un axe. Lorsqu’il est sélectionné, il possède des contrôles pour :
* Gizmo – active le gizmo de transformation pour définir le centre du miroir. Celui-ci peut également être pivoté et mis à l’échelle. Une fois terminé, touchez à nouveau Gizmo pour afficher les contrôles standard.
* X/Y/Z – définit le plan de symétrie

Tous les répéteurs possèdent un contrôle `Validate`, qui convertit le résultat du répéteur en géométrie, et demande comment effectuer cette conversion :
* Join children – les instances sont fusionnées en un seul objet
* Keep instances – les instances restent des instances, mais n’ont plus le répéteur comme « parent »
* Un-instances – les instances sont converties en objets uniques

::: tip Astuce : Combiner les répéteurs
Les répéteurs peuvent être imbriqués les uns sous les autres, et plusieurs objets peuvent être rendus enfants de répéteurs, ce qui permet d’obtenir des effets complexes.

![](/images/scene_repeater_combine.webp)
:::

::: tip Astuce : Pivots des répéteurs

Certains répéteurs tenteront d’ajuster automatiquement le pivot des objets enfants, de sorte que même si vous les déplacez ou les faites pivoter avec l’outil de gizmo, ils ne bougeront pas. Si vous devez remplacer ce comportement, insérez un groupe entre le répéteur et l’enfant. Vous pourrez alors déplacer la forme enfant indépendamment du répéteur.
:::

## Lumière {#light}

![](/images/scene_primitive_light.webp)

### Directionnelle {#directional}
Crée une lumière directionnelle, une source lumineuse infiniment éloignée comme le soleil.

### Spot {#spot}
Crée un spot, avec des contrôles sur la largeur du cône et la douceur

### Point {#point}
Crée une lumière ponctuelle

## Avancé {#advanced}
### Focus sur l’élément {#focus-on-item}
Un double-clic sur un élément dans la liste de scène centrera la caméra sur cet élément dans la vue 3D.

### Synchroniser la visibilité {#sync-visibility}
L’utilisation de l’icône en forme d’œil affectera tous les éléments sélectionnés. 

### Instance : Afficher {#instance-show}
Affiche une capsule de couleur à gauche de la liste de scène pour indiquer les instances.


### Icônes {#icons}
Définit la taille et l’opacité des icônes de groupe, lumière, caméra, miroir dans la vue 3D

### Lignes de hiérarchie {#hierarchy-lines}
Affiche une ligne entre le parent et ses enfants dans la vue 3D

## Barre d’outils inférieure {#bottom-toolbar}
Ces icônes basculent la visibilité des groupes, lumières, caméras, répéteurs et lignes de hiérarchie dans la vue 3D.