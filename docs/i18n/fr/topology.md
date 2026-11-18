# ![](/icons/multires.webp) Topologie {#topology}

Ce menu gère la topologie des objets dans Nomad, et regroupe aussi les outils pour transférer (baker) les détails d'un objet à l'autre, ou entre sommets et textures.

![](/images/topology_overview.webp)

Nomad travaille avec des polygones : la géométrie est faite de triangles et de quads.
Par topologie, on désigne à la fois le nombre de faces et la façon dont les points (sommets) sont reliés entre eux.

Il est important de garder un œil sur la topologie, surtout si vous voulez sculpter ou peindre des détails fins.

::: tip Comment surveiller votre topologie ?
Vous pouvez afficher le [Filaire](settings.md#wireframe), ou simplement désactiver l'[Ombrage lisse](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Le menu Topologie de Nomad compte plusieurs onglets, répartis sur deux lignes :

| Méthode                               | Icône                        | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multirésolution](#multiresolution)   | ![](/icons/multires.webp)   | Travailler sur plusieurs niveaux de détail grâce à la subdivision |
| [Remaillage voxel](#voxel-remesher)   | ![](/icons/voxel.webp)      | Recalculer une nouvelle topologie de densité uniforme            |
| [Topologie dynamique](#dynamic-topology) | ![](/icons/dynamic.webp) | Ajouter ou retirer des faces localement, en temps réel, pendant que vous sculptez ou peignez |
| [Divers](#misc)                       | ![](/icons/topo_extra.webp) | Boucher les trous, forcer le manifold et convertir en triplanaire |
| [Primitive](#primitive)               | ![](/icons/dot.webp)        | Options de la primitive                                          |
| [Décimer](#decimation)                | ![](/icons/decimate.webp)   | Réduire le nombre de faces en conservant la forme                |
| [Remaillage en quads](#quad-remesh)   | ![](/icons/quad.webp)       | Reconstruire l'objet avec une répartition propre de quads        |
| [Dépliage UV](#uv-unwrap)             | ![](/icons/uv.webp)         | Créer des UV pour le texturage                                   |
| [Baking](#bake)                       | ![](/icons/bake.webp)       | Baker les détails et la peinture vers des textures, des sommets ou des tampons VDM |


## Statistiques des polygones {#polygon-stats}

![](/images/topology_stats.webp)

En haut de chaque onglet, vous trouvez le nombre de polygones de l'objet sélectionné, et celui de toute la scène quand elle contient plusieurs objets. Les colonnes indiquent le nombre de sommets, de triangles, de quads (polygones à 4 côtés) et de coordonnées UV (0 si l'objet n'a pas d'UV).

Touchez cette zone pour afficher la liste de tous les objets de la scène avec leurs chiffres exacts, y compris leur nombre de groupes de faces.

## ![](/icons/cog.webp) Menu engrenage {#gear-menu}
Certaines sections, comme celles des onglets [Remaillage en quads](#quad-remesh) et [Baking](#bake), ont des options supplémentaires. Ouvrez-les avec l'icône d'engrenage à côté du titre de la section.

## ![](/icons/multires.webp) Multirésolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### Qu'est-ce que la multirésolution ? {#what-is-multiresolution}
La multirésolution sert surtout dans deux cas :
- La subdivision lissée, pour augmenter le nombre de polygones de votre objet
- La gestion de plusieurs niveaux de résolution, pour alterner entre les retouches de détail et les modifications à grande échelle

![](/videos/multiresolution.mp4)

#### Travailler en multirésolution {#multiresolution-workflow}
Le gros avantage de la multirésolution, c'est que vous pouvez revenir à une résolution plus basse, modifier votre objet, puis remonter à la résolution la plus haute sans perdre les détails fins. Tous les détails haute résolution sont reprojetés automatiquement.

Les [Calques](layers.md#layers) sont disponibles à toutes les résolutions.

::: warning
Si vous utilisez un outil qui modifie la topologie de votre objet, vous perdrez toutes les autres résolutions de l'objet !
Nomad devrait toujours vous prévenir avant, par exemple quand vous utilisez :
- le [Remaillage voxel](#voxel-remesher)
- la [Topologie dynamique](#dynamic-topology)
- l'[outil Découper](tools.md#trim)
- l'[outil Scinder](tools.md#split)
:::


### Curseur de multirésolution {#multiresolution-slider}
Ce curseur indique le nombre de niveaux de subdivision de l'objet courant. S'il y a 6 barres verticales, il y a 6 niveaux de subdivision. Le cercle indique le niveau de subdivision actuellement affiché.

De petites icônes au-dessus du curseur rappellent les options (`Verrouiller le niveau 0`, `Linéaire`, `Bordure vive`, `Conserver les triangles`) utilisées pour chaque niveau.

### Inverser {#reverse}
Quand vous êtes sur le niveau de subdivision le plus bas, le bouton `Inverser` tente de créer un niveau en dessous. En général, cela ne marche que si l'objet a été créé par subdivision au départ, que ce soit dans Nomad ou dans une autre application 3d qui gère les surfaces de subdivision multirésolution.

### Subdiviser {#subdivide}
Le bouton *Subdiviser* multiplie le nombre de polygones par 4 : surveillez bien le compte de polygones, il grimpe très vite ! Nomad demande une confirmation quand le résultat risque d'être très lourd.
Une propriété importante des *surfaces de subdivision* est qu'elles tendent vers une *surface lisse*.
Pour bien comprendre le principe, essayez le bouton *Subdiviser* sur un objet qui n'a que quelques polygones.

Vous pouvez désactiver ce lissage avec l'option `Linéaire`.

### Supprimer les niveaux inférieurs {#delete-lower}
S'il existe des subdivisions sous le niveau affiché, elles sont supprimées. Si vous le faites par erreur, vous pouvez les recréer avec le bouton `Inverser`.

### Supprimer les niveaux supérieurs {#delete-higher}
S'il existe des subdivisions au-dessus du niveau affiché, elles sont supprimées.

### ![](/icons/lock.webp) Verrouiller le niveau 0 {#lock-lv0}
Conserve la forme du niveau de subdivision le plus bas quand vous sculptez sur les niveaux supérieurs. La peinture, elle, est quand même transmise au niveau 0. C'est utile si votre objet vient d'une autre application et que le maillage de base doit rester intact.

Cette option n'est disponible qu'avant la première subdivision. Quand elle est désactivée, les grosses modifications faites aux niveaux supérieurs déplacent aussi le niveau 0.

### ![](/icons/linear.webp) Linéaire {#linear-subdivision}
Subdivise le maillage sans aucun lissage.

### ![](/icons/group.webp) Bordure vive {#sharp-border}
Si votre objet a des groupes de faces, cette option garde les bordures entre groupes de faces bien nettes. Elle peut être réglée à chaque niveau de subdivision (une petite icône au-dessus du niveau, sur le curseur de subdivision, l'indique).

### ![](/icons/triangle.webp) Conserver les triangles {#keep-triangles}
La plupart des systèmes de subdivision classiques essaient de tout convertir en quads lors de la subdivision. Cette option force la subdivision à garder des triangles.

::: tip

Par défaut, la subdivision adoucit toutes les arêtes vives. Pour garder des arêtes légèrement marquées, essayez `Linéaire` ou `Bordure vive` sur les 2 premiers niveaux de subdivision, puis désactivez-les pour les niveaux supérieurs. Vous obtiendrez un maillage subdivisé semi-vif.

:::

### Afficher le niveau le plus haut {#show-highest-level}
Affiche le niveau le plus haut, avec tous ses détails, pendant que vous sculptez un niveau plus bas. Pratique pour voir le résultat final pendant les grosses modifications.

### Filaire : niveau 0 uniquement {#wireframe-level-0-only}
Quand le [Filaire](settings.md#wireframe) est activé, seul le filaire du niveau le plus bas est affiché. Le filaire très dense des niveaux élevés peut masquer la forme.


## ![](/icons/voxel.webp) Remaillage voxel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Le `Remaillage voxel` impose à tout le maillage une résolution uniforme : tous les polygones ont à peu près la même taille. C'est très pratique quand vous ne voulez pas vous soucier de la topologie et simplement sculpter librement.

Une méthode courante consiste à commencer par dégrossir une forme en basse résolution avec le `Remaillage voxel`.
Appuyez simplement sur le bouton *Remailler* de temps en temps, quand vous étirez trop le maillage, pour éviter les déformations.

![](/videos/voxel_remesher.mp4)


::: tip Voxel ?
Comme dit plus haut, Nomad est un logiciel polygonal, mais le `Remaillage voxel` est une exception : il passe (temporairement) par une autre approche pour refaire le maillage.

Une grosse différence est que l'approche voxel n'accepte pas les auto-intersections : elles seront donc résolues.
Elle ne gère pas non plus les maillages troués.

Par trous, on ne parle pas du `genre` topologique (le `trou` d'un donut), mais des maillages qui ne sont pas `étanches`/`fermés`.
Concrètement, avant le remaillage, tous les trous sont bouchés, comme avec l'[outil Découper](tools.md#trim) ou la fonction [Trous](#holes). L'option [Trous](#voxel-holes) ci-dessous choisit comment.
:::

### ![](/icons/voxel.webp) Remailler {#voxel-remesh}
Lance le remaillage voxel. De petites icônes sur le bouton rappellent quelles options ci-dessous sont activées.

### Résolution {#voxel-resolution}
La taille des voxels utilisés pour le calcul : plus la valeur est élevée, plus il y a de détails. Pendant que vous modifiez ce paramètre, un damier s'affiche sur le maillage pour prévisualiser le résultat.

La pipette reprend la résolution à partir de la densité du maillage là où vous touchez. Le bouton cube à côté passe la valeur en `Longueur d’arête`, en unités du monde : la même valeur donne alors le même niveau de détail sur n'importe quel objet.

### Construire une multirésolution {#build-multiresolution}
Crée des niveaux de multirésolution inférieurs lors du remaillage voxel. Si vous réglez la résolution avec le damier et mettez `Construire une multirésolution` à 2, le résultat final aura le niveau de détail du curseur de résolution, et dans l'onglet Multirésolution il sera au niveau 2 : vous aurez donc des maillages de plus basse résolution aux niveaux 1 et 0. C'est une bonne façon d'obtenir à la fois un maillage propre aux polygones réguliers et un maillage de contrôle en basse résolution.

C'est aussi plus rapide et moins gourmand en mémoire à haute résolution. Mais avec une résolution basse et beaucoup de niveaux, vous perdrez des détails.

::: tip Astuce : Construire une multirésolution et lissage stable

Cette option crée parfois des « boucles » dans la géométrie, difficiles à lisser, qui forment de petits boutons. Dans ce cas, activez `Lissage stable` dans les options de l'outil Lisser.

:::

### Épaissir les parties fines {#thicken-thin-parts}
Les parties plus fines que les voxels peuvent se casser ou disparaître pendant le remaillage. Cette option les épaissit pour qu'elles survivent : plus la valeur est élevée, plus elles sont épaissies. Elle n'est pas disponible avec `Arêtes vives` ou `Bordure vive`.

### Trous {#voxel-holes}
La façon dont les trous sont bouchés avant le remaillage :

* `Remplir` - Chaque trou est bouché séparément, à partir de son bord.
* `Forme` - Les trous sont bouchés en suivant la surface environnante, et les morceaux ouverts qui se chevauchent sont réunis.

### ![](/icons/angle.webp) Arêtes vives {#keep-sharp-edges}
Aligne les nouveaux points sur les arêtes vives du maillage d'origine. C'est surtout utile pour des opérations booléennes simples sur des primitives, et cela peut introduire des déformations.

### ![](/icons/group.webp) Bordure vive {#voxel-sharp-border}
Les nouvelles faces suivent les bordures des groupes de faces, et une bordure reste nette là où la surface forme un pli le long de celle-ci.

### ![](/icons/group_separate.webp) Séparer les groupes {#keep-groups-separate}
Chaque groupe de faces est remaillé séparément : les groupes ne fusionnent jamais, et chacun reste un morceau fermé dans son propre groupe. La multirésolution n'est pas construite dans ce mode. L'option est disponible quand l'objet a plusieurs groupes de faces.

## ![](/icons/dynamic.webp) Topologie dynamique {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
La multirésolution et le remaillage voxel sont des méthodes classiques pour contrôler la topologie, mais toutes deux vous obligent à surveiller que vous n'étirez pas trop les polygones, ou que vous ne les tassez pas trop.

La topologie dynamique est une autre approche. Pendant que vous sculptez, Nomad ajoute et retire des polygones au fil du trait : creuser de petits détails ajoute plein de petits polygones là où vous en avez besoin, et lisser ailleurs en retire.

Notez que la topologie dynamique utilise des triangles et non des quads. Ça peut sembler un peu brouillon, mais le mieux est presque de ne pas regarder le filaire : concentrez-vous sur une belle sculpture sans vous soucier de la topologie, puis utilisez plus tard un des autres outils de remaillage de Nomad pour obtenir un maillage propre en quads.

Voyez-la en action dans la vidéo ci-dessous.

![](/videos/dynamic.mp4)

### Activée {#enabled}
Active la topologie dynamique. Une icône DynTopo apparaît sous les curseurs de rayon et d'intensité de l'outil, pour activer ou désactiver la DynTopo outil par outil. Elle peut avoir un impact notable sur les performances, et les calques sont correctement mis à jour.

### Détail {#dyn-detail}
Règle la quantité de détail ; son comportement dépend du choix fait dans « Détail basé sur… », voir ci-dessous. En mode `Écran`, le libellé indique la taille visée des triangles en pixels. En mode `Constant`, une pipette vous permet de reprendre le détail à partir de la densité du maillage là où vous touchez.

### Détail basé sur… {#detail-based-on}
| Méthode  | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Écran    | Le niveau de détail dépend de la taille de l'objet à l'écran. Le curseur de détail à 100 % ou plus donne des détails fins (petits triangles), à 1 % peu de détail (grands triangles). |
| Rayon    | Le rayon de l'outil définit la quantité de détail : un petit rayon pour des détails fins, un grand rayon pour peu de détail. Le curseur de détail est un multiplicateur de ce rapport. |
| Constant | Le curseur de détail définit la quantité de détail, indépendamment de la taille à l'écran ou de la taille de l'outil. C'est la même valeur que le curseur [Détail](#all-detail) de `Remailler`. |

::: tip ASTUCE : le mode Rayon

Pour bien sentir comment fonctionne le mode Rayon, commencez à déplacer le curseur de détail avec un doigt, et changez en même temps le rayon de l'outil avec un autre doigt. Vous verrez comment ils sont liés.

:::

### Préférer… {#prefer}
| Méthode | Description                |
| :-----: | :------------------------: |
| Vitesse | Privilégier les performances |
| Qualité | Privilégier la qualité     |

Quand vous privilégiez la `Qualité`, il y a 2 grandes différences :
- le raffinement est appliqué avant la sculpture, ce qui réduit les artefacts d'interpolation quand vous peignez ou sculptez de très petits détails
- le raffinement se poursuit jusqu'à atteindre le bon niveau de détail, au lieu de progresser par petites étapes.

Ainsi, même si vous sculptez de très petits détails ou faites des traits rapides, la topologie sera toujours raffinée comme prévu.


### ![](/icons/pressure.webp) Pression sur le rayon {#use-pressure-on-radius}
Ne sert que si le mode `Rayon` est activé. Quand cette option est active, le niveau de détail suit toujours la taille de la brosse, même quand celle-ci varie avec la pression du stylet.

### Atténuation du trait {#use-stroke-falloff}

Prend aussi en compte la courbe d'atténuation et l'alpha de la brosse dans les calculs de la DynTopo.

### Méthode {#method}
Choisit comment la topologie dynamique modifie le maillage, aussi bien pendant que vous sculptez que lorsque vous utilisez [Remailler](#dyn-remesh) :

| Méthode        | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Peut ajouter et retirer des faces ; c'est le mode utilisé dans la vidéo ci-dessus |
| Subdivision    | Ajoute uniquement des faces, ne peut pas en retirer                   |
| Décimation     | Retire uniquement des faces, ne peut pas en ajouter                   |

### ![](/icons/shield.webp) Protéger la zone masquée {#protect-masked-area}
Les zones masquées protègent la topologie : elle n'y est pas modifiée.

### ![](/icons/normal.webp) Extrapolation des sommets {#vertex-extrapolation}
Place les points sur une surface lisse qui suit la courbure environnante, au lieu de les poser à plat sur les faces existantes.

### Détail {#all-detail}
La résolution utilisée pour le remaillage. Si la DynTopo est en mode `Constant`, c'est la même valeur que le curseur Détail en haut de ce menu. La pipette reprend le détail à partir de la densité du maillage là où vous touchez.

### Remailler {#dyn-remesh}
Lance un remaillage global avec l'algorithme de la DynTopo. En général, mieux vaut utiliser le [Remaillage voxel](#voxel-remesher) pour remailler entièrement un objet.

Cela dit, il a un avantage sur les voxels : le maillage n'a pas besoin d'être fermé, et la zone masquée est protégée, ce qui vous permet de mieux contrôler où mettre plus ou moins de densité.



## ![](/icons/topo_extra.webp) Divers {#misc}

![](/images/topology_misc_menu.webp)

Cet onglet regroupe des outils pour nettoyer ou convertir le maillage : boucher ses trous, le forcer à être manifold, ou le transformer en triplanaire.

### ![](/icons/hole.webp) Trous {#holes}
![](/images/topology_holes_menu.webp)
La plupart du temps, votre objet sera étanche, c'est-à-dire que le maillage est « fermé ».

Si votre objet a des trous, vous pouvez les boucher.

![](/videos/hole_filling.mp4)

::: tip
Quand vous lancez le Remaillage voxel, tous les trous sont bouchés automatiquement, que vous l'utilisiez sur un ou plusieurs maillages.
:::

#### Boucher les trous {#close-holes}
Lance le bouchage des trous.

#### Options {#holes-gear-menu}
Ces options changent la façon dont les trous sont bouchés :

##### Groupe de faces {#fill-face-group}
Choisit le groupe de faces des nouvelles faces :

* `Mixte` - Un trou entouré d'un seul groupe de faces le réutilise ; un trou qui touche plusieurs groupes en reçoit un nouveau.
* `Nouveau` - Les trous bouchés reçoivent un nouveau groupe de faces.
* `Réutiliser` - Chaque trou prend le groupe de faces qui l'entoure le plus.

##### Détail {#fill-detail}
La densité de polygones utilisée pour boucher le trou. Pendant que vous faites glisser ce curseur, un damier s'affiche sur le modèle pour donner une idée de la taille des triangles. La case à cocher le désactive pour n'utiliser que les points existants, ce qui crée en général de longs triangles fins au-dessus du trou, difficiles à sculpter.

##### Pont {#fill-non-manifold}
Bouche un trou et les îlots qu'il contient en une seule surface, au lieu de boucher chaque bord séparément. Un angle plus grand permet de relier des trous plus courbés. La case à cocher désactive l'option.

### ![](/icons/cog.webp) Forcer manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Tente de nettoyer les arêtes non manifold. Utile pour les logiciels externes qui ne gèrent pas les arêtes partagées par plus de 2 faces.

#### Nettoyer {#clean}
Lance le nettoyage.

#### Options {#force-manifold-gear-menu}
Cette option change la façon dont le maillage est nettoyé :

##### Supprimer les petites faces {#delete-small-faces}
Un seuil en dessous duquel les petits polygones sont supprimés et fusionnés. Activez-le avec sa case à cocher.


### ![](/icons/triplanar.webp) Triplanaire {#triplanar}
![](/images/topology_triplanar_menu.webp)
Convertit le maillage en primitive [triplanaire](scene.md#triplanar).
Vous perdrez sans doute beaucoup de détails au passage : les calques, la peinture et la multirésolution sont perdus aussi.

#### Forcer le cube {#force-cubic}
Fait du triplanaire un cube. Sinon, le triplanaire s'ajuste à la boîte englobante la plus proche de votre objet.

#### Convertir {#convert}
Lance la conversion en triplanaire.

#### Résolution {#triplanar-resolution}
La résolution de la grille du triplanaire : plus la valeur est élevée, plus les détails sont conservés.

## ![](/icons/decimate.webp) Décimer {#decimation}

![](/images/topology_decimation.webp)

Réduit le nombre de polygones en essayant de garder le plus de détails possible, avec des triangles.

Cette fonction est utile si vous voulez exporter pour l'impression 3d.
En revanche, mieux vaut l'éviter si vous comptez continuer à sculpter dessus, car elle peut produire des triangles irréguliers.

Notez que les zones masquées ne sont pas décimées.

![](/videos/decimate.mp4)

::: tip

Utiliser l'[outil Quad Remesher](tools.md#quad-remesher) sur des objets très denses peut prendre beaucoup de temps de calcul, et donner des résultats difficiles à maîtriser. Préparer le maillage avec les [groupes de faces](tools.md#facegroup) et la décimation rend Quad Remesher bien plus rapide, et vous donne beaucoup plus de contrôle sur la topologie.

* Découpez le maillage en groupes de faces pour définir le flux de quads idéal.
* Relâchez les groupes de faces pour obtenir des bordures de groupes bien lisses.
* Décimez. Vous n'aurez ainsi aucune face fine ou déformée le long des bordures de groupes. Sous `Préserver les bordures`, vérifiez que `Groupe de faces` est activé : les arêtes des triangles suivront alors précisément les bordures de vos groupes de faces.
* Dans les options de Quad Remesher, vérifiez que le relâchement est désactivé (vous avez déjà relâché le maillage) : vous devriez obtenir de bons résultats.

:::

### Décimer {#decimate}
Lance la décimation.

Les icônes à côté du bouton `Décimer` reprennent les options ci-dessous et permettent de les activer ou les désactiver. Le pourcentage indique la force de chaque option.

* ![](/icons/palette.webp)  `Préserver la peinture` - Place plus de triangles là où il y a des détails de peinture.
* ![](/icons/triforce.webp) `Faces uniformes` - Privilégie des triangles de taille régulière.
* ![](/icons/hole.webp)  `Trou` - La décimation essaie de laisser intactes les bordures près de la géométrie ouverte et des trous.
* ![](/icons/group.webp) `Groupe de faces` - La décimation essaie de laisser intactes les bordures des groupes de faces.
* ![](/icons/uv.webp) `UV` - La décimation essaie de laisser intactes les bordures des UV.

### Triangles cibles {#target-triangles}
Définit le nombre de triangles visé. La valeur par défaut est 50 % ; le bouton pourcentage/cible bascule entre un pourcentage et un nombre exact de polygones.

### Options {#decimate-gear-menu}
Chaque option a une case à cocher pour l'activer, et une valeur pour sa force :

#### ![](/icons/palette.webp) Préserver la peinture {#preserve-painting}
Cette valeur détermine la précision avec laquelle les détails de peinture sont conservés. Plus elle est élevée, mieux la peinture est préservée. Mettez 0 si la peinture ne vous importe pas.

#### ![](/icons/triforce.webp) Faces uniformes {#uniform-faces}
Plus la valeur est élevée, plus les triangles obtenus ont une taille similaire.

#### Préserver les bordures {#preserve-borders}
Empêche les bordures d'être décimées. Des poids peuvent être réglés pour les bordures de `Trou`, de `Groupe de faces` ou d'`UV` (`UV` demande un objet qui a des UV).

## ![](/icons/quad.webp) Remaillage en quads {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Reconstruit l'objet avec une répartition propre de quads. Cet onglet propose plusieurs remailleurs, chacun avec son bouton `Remailler`, son curseur `Quads cibles` et son menu engrenage. Essayez-les sur votre objet : leurs résultats sont assez différents !

### Quad Remesher {#quad-remesher}
Le même remailleur que l'outil [Quad Remesher](tools.md#quad-remesher), développé par [Exoside](https://exoside.com/). Il n'est disponible que sur certaines plateformes et nécessite un achat : en attendant, le bouton `Remailler` affiche un chariot.

`Sélectionner l’outil` passe à l'outil Quad Remesher, pour dessiner des guides et peindre la densité. Le menu engrenage contient `Nombre de quads adaptatif`, `Taille adaptative` (à 100 %, la taille des quads suit la courbure ; à 0 %, les quads sont uniformes), `Détecter les arêtes dures` et `Reprojeter le sommet`.

::: tip
Là où il est disponible, Quad Remesher donne en général les meilleurs résultats et le plus de contrôle.
:::

### AutoRemesher {#autoremesher}
Un autre remailleur en quads, avec des options pour adapter la taille et la forme des quads à la surface.

#### ![](/icons/cog.webp) Menu engrenage d'AutoRemesher {#autoremesher-gear-menu}
Le menu engrenage propose ces options avancées :

##### Échelle des arêtes {#edge-scaling}
Change la taille des quads : plus la valeur est élevée, plus les quads sont grands.

##### Adaptativité {#adaptivity}
Adapte la densité de quads à la courbure. 0 donne des quads uniformes, 1 donne des quads plus petits dans les zones courbes.

##### Anisotropie {#anisotropy}
Étire les quads dans la direction la plus plate de la surface. 0 donne des quads carrés, 1 donne des quads allongés sur les tubes et les arêtes saillantes.

##### Arête vive {#sharp-edge}
Les arêtes pliées au-delà de cet angle sont conservées comme arêtes vives.

##### Lissage des normales {#smooth-normal}
0 garde la surface facettée pendant le remaillage. Des valeurs plus élevées lissent la surface en tenant compte des normales des sommets.

##### Trou max. à remplir {#autoremesher-max-fill-hole}
L'algorithme produit parfois des trous indésirables. Si un trou a moins de sommets que cette valeur, il est bouché.

### Instant Mesh {#quad-remesh-instant}
Remaille avec l'[algorithme Instant Meshes de Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Il analyse le flux du maillage et crée une topologie propre en quads.

#### Remailler {#instant-remesh}
Lance le remaillage.

#### Quads cibles {#target-quads}
Le nombre de quads que le remailleur essaiera de créer.

#### ![](/icons/cog.webp) Menu engrenage d'Instant Mesh {#quad-remesh-instant-gear-menu}
Le menu engrenage propose ces options avancées :

##### Angle de pli {#crease-angle}
Un seuil d'angles vifs qui aide à guider le remaillage. Activez-le avec sa case à cocher.

##### Trou max. à remplir {#max-fill-hole}
L'algorithme produit parfois des trous indésirables. Si un trou a moins de sommets que cette valeur, il est bouché.

### QuadriFlow {#quadriflow}
Remaille avec l'algorithme QuadriFlow, une autre façon d'obtenir une répartition propre de quads.

#### ![](/icons/cog.webp) Menu engrenage de QuadriFlow {#quadriflow-gear-menu}
Le menu engrenage propose ces options avancées :

##### Préserver les bordures {#quadriflow-preserve-boundary}
Protège les bords des trous.

##### Préserver les arêtes vives {#keep-sharp}
Aligne les quads sur les arêtes vives de la surface.

##### Flot de coût minimal {#min-cost-flow}
Utilise un solveur de flot de coût minimal pour la répartition des quads. Plus lent, mais peut donner une topologie plus régulière.

## ![](/icons/uv.webp) Dépliage UV {#uv-unwrap}
Calcule les coordonnées de texture (UV) de l'objet sélectionné. Nomad propose deux méthodes, `UVAtlas` et `BFF`, chacune avec son bouton `Déplier`.

![](/videos/unwrap.mp4)

::: tip Des UV ?
On compare souvent les UV à l'emballage d'un cadeau : comment découper au mieux le papier pour couvrir entièrement un objet, sans chevauchement ?

Les UV, c'est pareil, sauf qu'au lieu de découper le papier, on découpe l'objet. Imaginez que votre modèle soit en plastique fin : comment le découperiez-vous pour le déplier à plat, peindre dessus dans cet état, puis le remonter ?

Imaginez maintenant que la surface de votre modèle soit en lycra extensible. Vous pourriez l'étirer à plat, le découper, ou combiner les deux. Mais si vous peigniez un damier sur l'objet aplati, ce damier serait déformé une fois l'objet remonté. Quelle est la meilleure méthode : plus de découpes avec moins de déformation, ou moins de découpes avec plus de déformation ?

Les UV sont des instructions qui disent au logiciel 3d comment « découper et étirer » l'objet pour y appliquer des textures. L'outil UVAtlas suit en général l'approche « plus de découpes, moins de déformation ».


:::

::: tip Les UV, Nomad et les autres applications

La plupart des modèles texturés que vous trouverez en ligne sont texturés via des UV. Nomad peut les importer et les afficher depuis le panneau [Matériau](material.md#textures).

Quand vous créez un modèle dans Nomad, vous pouvez peindre directement sur l'objet sans UV. Si vous devez l'exporter vers d'autres applications, comme [Procreate](https://procreate.art/), vous pouvez « baker » les couleurs de Nomad dans des textures grâce aux UV.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas préfère en général créer plus d'îlots avec des découpes, pour limiter la déformation.

#### Déplier {#unwrap}
Calcule les UV de l'objet sélectionné.

#### Options {#uvatlas-gear-menu}
Les boutons à côté de `Déplier` :

##### Groupe de faces {#atlas-face-group}
Quand il affiche `Oui`, les groupes de faces définissent les découpes des UV. Ce réglage est partagé avec BFF.

##### Supprimer les UV {#delete-uvs}
Le bouton corbeille supprime les UV de l'objet.

##### Inspecter {#uv-inspect}
Affiche les UV de l'objet en arrière-plan.

#### Étirement max. {#max-stretch}
Des valeurs basses donnent moins de déformation et plus d'îlots, des valeurs hautes plus de déformation et moins d'îlots.

#### Espacement des îlots {#island-spacing}
La marge entre les îlots. Des valeurs basses gaspillent moins de place, mais les textures risquent de déborder d'un îlot à l'autre.

::: warning
Le calcul des UV peut prendre du temps : l'idéal est un maillage de moins de 100 000 sommets.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

Les UV de BFF privilégient l'approche « moins de découpes, plus de déformation ».

#### Options {#uv-bff-gear-menu}
Les mêmes boutons `Groupe de faces`, suppression et `Inspecter` que pour [UVAtlas](#uvatlas-gear-menu) se trouvent à côté de `Déplier`.

##### Groupe de faces {#bff-face-group}

Utilise les groupes de faces pour définir les découpes des UV.

#### Nombre de cônes {#cone-count}
Définit le nombre de projections principales utilisées. Des valeurs basses donnent moins d'îlots, mais plus de déformation. Des valeurs hautes prennent plus de temps de calcul.

#### Patchs sans couture {#seamless-patches}
Influe sur la disposition des patchs UV, et peut introduire une forte déformation. Fonctionne mieux avec des groupes de faces soigneusement préparés.

::: warning
BFF peut créer des UV qui se chevauchent si le maillage a des anses (comme le trou d'un donut).
:::

### ![](/icons/preview.webp) Afficher les UV après le dépliage {#show-uv-after-unwrap}
Ouvre l'inspecteur d'UV après le dépliage, pour vérifier le résultat tout de suite.

### ![](/icons/bake.webp) Baking : Texture → Texture {#unwrap-bake-texture}
Disponible uniquement quand le matériau de l'objet a des textures. Quand vous dépliez à nouveau l'objet, les textures sont transférées sur les nouveaux UV, et restent donc bien en place. Sa résolution est `Auto` par défaut (celle de la plus grande texture), mais vous pouvez la régler vous-même.

## ![](/icons/bake.webp) Baking {#bake}
Cet onglet transfère les détails et la peinture d'un objet à l'autre, et entre sommets et textures.

`Depuis la haute résolution` utilise d'autres objets comme source ; le nombre entre parenthèses indique combien. Nomad les choisit ainsi :

- tous les objets sélectionnés sont utilisés, et l'objet sélectionné principal est la cible (celui qui est le plus mis en évidence dans le menu [Scène](scene.md))
- si un seul objet est sélectionné, Nomad utilise à la place tous les objets visibles
- si tous les autres objets sont cachés (par exemple avec Solo), toute la scène est utilisée

### ![](/icons/bake.webp) Baking → Texture {#bake-texture}
![](/images/topology_bake_menu.webp)

Le baking de textures crée des textures en projetant les autres objets visibles de la scène dans les UV de l'objet sélectionné. L'objet doit avoir des UV.

Voici la marche à suivre typique :
- Vous avez un maillage avec des détails fins et de la peinture
- Clonez-le
- Décimez-le (mettez `Préserver la peinture` à 0)
- Dépliez ses UV
- Bakez !

Vous avez maintenant un maillage basse résolution qui conserve l'essentiel de la peinture et des détails de l'objet d'origine.

Après l'opération, les couleurs des sommets sont déplacées dans un nouveau calque désactivé, pour ne pas interférer avec les textures.

#### Depuis lui-même {#tex-from-itself}
Bake l'objet sur ses propres UV : sa peinture devient des textures, et s'il a des niveaux de multirésolution, les détails du niveau le plus haut sont bakés sur le niveau courant (une icône multirésolution apparaît alors sur le bouton). C'est simple à mettre en place, mais vous aurez souvent besoin de plus de contrôle : l'option suivante est alors plus utile.

#### Depuis la haute résolution {#tex-from-high-res}
Bake les autres objets sur l'objet sélectionné. Le nombre entre parenthèses indique combien d'autres objets serviront de sources haute résolution, bakées dans l'objet basse résolution courant qui a des UV. Les autres objets n'ont pas besoin d'avoir la même disposition ni la même topologie que l'objet baké, ce qui permet des méthodes de baking très variées.

#### Résolution {#tex-bake-resolution}
La résolution de la texture bakée. Les textures bakées sont toujours carrées : 1024 crée une image de 1024x1024.

Les boutons en dessous sont des raccourcis vers les résolutions les plus courantes. Pour vous donner une idée, 512x512 est plutôt petit, pour des images web et une géométrie simple. 4096x4096 (4k en abrégé) convient à des rendus de haute qualité.

#### Couleur, Rugosité, Métallité, Normale, Déplacement, Émissif, Opacité {#tex-normal-roughness-metalness-color-emissive-opacity}
Ces boutons déterminent quelles propriétés seront bakées, chacune dans une texture séparée. Une fois le baking terminé, elles sont ajoutées comme textures au matériau de l'objet courant. `Déplacement` bake la hauteur des détails dans une carte de déplacement.

#### ![](/icons/cog.webp) Menu engrenage du baking {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Le menu engrenage propose ces options avancées :

##### Sauvegarde {#tex-backup}
Pour prévisualiser les textures bakées, la peinture de l'objet doit être désactivée. `Sauvegarde (Peinture → Calque)` transfère toute la peinture dans un nouveau calque de sauvegarde, que vous pouvez facilement activer ou désactiver.

##### Utiliser le multirés {#tex-use-multires}
Pour `Depuis lui-même` sur un objet qui a des niveaux de multirésolution. Nomad lit la haute résolution à travers les niveaux de subdivision au lieu de lancer des rayons : c'est plus rapide et sans erreurs de projection. Désactivez-le pour baker avec les options ci-dessous.

##### Base lissée {#tex-smooth-base}
Pour `Déplacement` sur un objet qui a des niveaux de multirésolution. Mesure le déplacement depuis la base subdivisée plutôt que depuis ses faces plates. Laissez-le activé quand la carte de déplacement est destinée à un maillage subdivisé, comme la subdivision adaptative de Blender.

##### Distance de recherche {#tex-cage-radius}
La distance maximale utilisée pour trouver la surface source. Par défaut, elle est faible pour éviter les artefacts, mais vous pouvez l'augmenter si les objets sources sont loin de l'objet baké.

##### Projection {#tex-projection}
La façon dont la surface source est trouvée :

* `Rayon` - Projette le long de la normale de la surface.
* `Rayon + au plus proche` - Utilise le rayon le long de la normale, puis la surface la plus proche si le rayon ne touche rien.
* `Au plus proche` - Projette sur le point le plus proche de la surface source.

##### Décalage des rayons {#tex-ray-offset}
Ajuste le point de départ des calculs de baking sur l'objet baké. Un petit décalage par rapport à la surface évite la plupart des artefacts courants. Si les objets sources sont très loin de l'objet baké, il faudra peut-être augmenter ce décalage. Il n'est pas utilisé par `Au plus proche`.


### ![](/icons/bake.webp) Reprojeter → Sommet {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projette les détails sculptés, la peinture, les calques et les textures dans les valeurs des sommets.

On peut le voir comme l'inverse du baking : si le baking transfère les propriétés des sommets vers des textures, la reprojection transfère les textures (et d'autres propriétés)
 vers les sommets.

::: tip
Avec `Baking → Texture` comme avec `Reprojeter → Sommet`, les couleurs des sommets et les textures du matériau sont toutes deux prises en compte.
:::

#### Depuis lui-même {#vertex-from-itself}
Convertit les textures du matériau en valeurs de sommets. Ce bouton n'est actif que si l'objet a des UV et que des textures sont actives dans le matériau.

::: tip ASTUCE : peindre des textures
Nomad ne permet pas de peindre ou de modifier directement des textures, mais on obtient un résultat très proche en projetant les textures vers les sommets, en peignant sur les sommets, puis en bakant les sommets vers des textures :

1. Préparez un objet low poly avec des UV
1. Chargez des textures dans son matériau
1. Subdivisez-le assez pour pouvoir peindre dessus
1. `Reprojeter → Sommet` en mode `Depuis lui-même` : la texture est maintenant convertie en valeurs de sommets
1. Peignez, lissez, estompez, tamponnez, faites toutes les retouches dont vous avez besoin
1. `Baking → Texture` en mode `Depuis lui-même` : vos retouches sont reconverties en textures.
:::

#### Depuis la haute résolution {#vertex-from-high-res}
Convertit les autres objets en valeurs de sommets sur l'objet sélectionné. Le nombre sur ce bouton indique le nombre d'objets sources. C'est surtout prévu pour un maillage lui aussi en haute résolution, en général avec une topologie propre.

::: tip
La reprojection d'autres objets ne sert pas qu'à transférer des couleurs : elle permet aussi de projeter des sommets sur d'autres objets, par exemple pour plaquer des bandages sur un personnage.
:::

#### Sommets, Couleur, Rugosité, Métallité, Opacité, Masque, Calques, Groupe de faces {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Ces boutons déterminent quelles propriétés seront projetées sur l'objet sélectionné. `Calques` transfère les calques des autres objets sur le maillage sélectionné.

#### ![](/icons/cog.webp) Menu engrenage de la reprojection {#vertex-reproject-gear-menu}
Le menu engrenage propose ces options avancées :

##### Opacité → Masque {#vertex-opacity-to-mask}
Transforme l'opacité de la source en masque sur l'objet sélectionné.

##### Itérations {#vertex-iterations}
Le nombre de fois que le relâchement est appliqué pendant la reprojection. Utilisé uniquement quand `Sommets` est activé.

##### Relâcher {#vertex-relax}
La disposition du maillage sélectionné peut être lissée ou relâchée, plus ou moins, pour mieux épouser les cibles de la reprojection. `Lisser` convient mieux aux maillages denses, `Relâcher` aux maillages légers. `Auto` laisse Nomad choisir la meilleure méthode.

##### Distance de recherche {#vertex-cage-radius}
La distance maximale utilisée pour trouver la surface source. Par défaut, elle est faible pour éviter les artefacts, mais vous pouvez l'augmenter si les objets sources sont loin de l'objet sélectionné.

##### Projection {#vertex-projection}
La façon dont la surface source est trouvée :

* `Rayon` - Projette le long de la normale de la surface.
* `Mélange adaptatif` - Mélange le rayon le long de la normale et la surface la plus proche selon la distance et la `Préférence du rayon`. Si l'un ne touche rien, l'autre est utilisé.
* `Au plus proche` - Projette sur le point le plus proche de la surface source.

##### Préférence du rayon {#vertex-ray-bias}
Uniquement pour `Mélange adaptatif`. Des valeurs élevées font pencher le mélange vers le résultat du rayon le long de la normale, des valeurs basses vers le point le plus proche.

##### Décalage des rayons {#ray-vertex-offset}
Ajuste le point de départ des calculs sur l'objet sélectionné. Un petit décalage par rapport à la surface évite certains artefacts. Si les objets sources sont très loin de l'objet baké, il faudra peut-être augmenter ce décalage. Il n'est pas utilisé par `Au plus proche`.

### ![](/icons/bake.webp) Baking → VDM {#bake-vdm}
Crée un tampon VDM (vector displacement, déplacement vectoriel) à partir de l'objet sélectionné et l'ajoute à la bibliothèque VDM. Un nom vous sera demandé.

Voici la marche à suivre typique :
- Ajoutez un plan, ou choisissez `Nouveau VDM` dans le sélecteur de VDM pour en ajouter un déjà configuré (la primitive [VDM](scene.md#add-menu))
- Sculptez votre forme dessus, en gardant le bord à plat
- Bakez !

Les UV du plan définissent le carré qui est baké : l'objet doit donc avoir des UV. Choisissez la taille du tampon avec `Résolution`, et avec `Couleur`, `Rugosité`, `Métallité` et `Opacité` ce que le tampon contient en plus du déplacement.

::: tip
Évitez la DynTopo sur le plan : elle abîme ses UV et le tampon ressort déformé. Sculpter dans un calque donne le résultat le plus précis, puisque le plan plat est toujours là en dessous. La peinture demande aussi un calque, sinon le matériau est tamponné sur tout le carré au lieu de seulement là où vous avez peint.
:::

## ![](/icons/dot.webp) Primitive {#primitive}
Les paramètres de la primitive sélectionnée. La plupart sont aussi accessibles depuis le bouton `…` de la barre d'outils de la primitive dans la vue 3d.

![](/images/topology_primitive_screenshot.webp)
