# ![](/icons/multires.webp) Topologie {#topology}

Ce menu contrôle la topologie des objets dans Nomad, ainsi que les outils pour cuire (baker) et transférer les détails entre objets, et entre textures.

![](/images/topology_overview.webp)

Nomad est basé sur des polygones, il utilise des triangles et des quads pour gérer la géométrie.
Par topologie, on entend à la fois le nombre de faces mais aussi la façon dont les points (sommets) sont connectés.

Il est important de garder un œil sur la topologie, surtout si vous voulez sculpter ou peindre des détails fins.

::: tip Comment suivre votre topologie ?
Vous pouvez afficher le [Wireframe](settings.md#wireframe) ou simplement désactiver le [Lissage des ombres](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Le menu de topologie de Nomad comporte plusieurs sections :

| Méthode                               | Icône                        | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multirésolution](#multiresolution)   | ![](/icons/multires.webp)   | Éditer plusieurs niveaux de détail à l’aide de la subdivision    |
| [Remesh Voxel](#voxel-remesher)       | ![](/icons/voxel.webp)      | Recalculer une nouvelle topologie avec une densité uniforme      |
| [Topologie dynamique](#dynamic-topology) | ![](/icons/dynamic.webp) | Ajouter/Supprimer des faces localement en temps réel lors de la sculpture ou de la peinture |
| [Divers](#misc)                       | ![](/icons/topo_extra.webp) | Décimation, UV, baking, remeshing, reprojection                  |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Options de primitive                                             |


## Statistiques de polygones {#polygon-stats}

![](/images/topology_stats.webp)

La partie supérieure du menu de topologie affiche les informations de polygones pour l’objet sélectionné et pour toute la scène. Les nombres indiquent le nombre total de sommets, le nombre total de triangles et le nombre total de quads (polygones à 4 côtés).

Un appui sur cette section fera apparaître une liste de statistiques de polygones pour tous les objets polygonaux de la scène.

## ![](/icons/multires.webp) Multirésolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### Qu’est-ce que la multirésolution ? {#what-is-multiresolution}
La fonction de multirésolution est utile dans deux cas principaux :
- L’algorithme de subdivision lissée pour augmenter le nombre de polygones de votre objet
- Gérer plusieurs niveaux de résolution afin de pouvoir alterner entre des modifications à grande et à petite échelle

![](/videos/multiresolution.mp4)

#### Flux de travail de multirésolution {#multiresolution-workflow}
Un aspect important de la multirésolution est que vous pouvez revenir à une résolution plus basse, faire des modifications sur votre objet puis revenir à la résolution la plus élevée sans perdre les détails haute résolution. Tous les détails haute résolution seront projetés automatiquement.

::: warning
Si vous utilisez un outil qui modifie la topologie de votre objet, vous perdrez tous les autres niveaux de résolution de votre objet !
Vous devriez toujours obtenir un avertissement si cela doit arriver, par exemple lorsque vous utilisez :
- le [Remesh Voxel](#voxel-remesher)
- la [Topologie dynamique](#dynamic-topology)
- l’outil [Trim](tools.md#trim)
- l’outil [Split](tools.md#split)
:::


### Curseur de multirésolution {#multiresolution-slider}
Ce curseur indique le nombre de niveaux de subdivision de l’objet courant. S’il y a 6 barres verticales, il y a 6 niveaux de subdivision. Le cercle indique le niveau de subdivision actuellement affiché. 

### Inverser {#reverse}
Au niveau de subdivision le plus bas, le bouton Reverse tentera de créer un niveau en dessous du niveau actuel. Notez que cela n’est généralement possible que si l’objet a été créé avec subdivision au départ, par exemple dans Nomad ou dans d’autres applications 3D qui utilisent des surfaces de subdivision multirésolution.

### Subdiviser {#subdivide}
Le bouton *Subdivide* multipliera le nombre de polygones par 4, surveillez donc bien le nombre de polygones car il peut augmenter très rapidement !
Un aspect important des *Surfaces de subdivision* est qu’elles convergent vers une *Surface lisse*.
Pour comprendre comment cela fonctionne, vous pouvez essayer le bouton *Subdivide* sur un objet avec seulement quelques polygones.

Vous pouvez désactiver ce comportement *Smooth* en cochant l’option `Linear subdivision`.

### Supprimer les niveaux inférieurs {#delete-lower}
S’il existe des subdivisions en dessous du niveau actuellement affiché, elles seront supprimées. Si vous faites cela par accident, vous pouvez les recréer avec le bouton Reverse.

### Supprimer les niveaux supérieurs {#delete-higher}
S’il existe des subdivisions au-dessus du niveau actuellement affiché, elles seront supprimées.

### Subdivision linéaire {#linear-subdivision}
Subdivise le maillage sans appliquer de lissage.

### Bord net {#sharp-border}
Si votre objet possède des facegroups, l’activation de cette option conservera les bords de facegroup nets. Cela peut être défini à chaque niveau de subdivision (le curseur de subdivision aura une petite icône au-dessus du niveau pour l’indiquer).

### Conserver les triangles {#keep-triangles}
La plupart des systèmes standard de surfaces de subdivision tenteront de convertir tous les polygones en quads lors d’une opération de subdivision. Ce bouton forcera la subdivision à utiliser des triangles à la place.

### Verrouiller (LV0) {#lock-lv0}

Empêche la modification du niveau de subdivision le plus bas. Cela peut être important si votre objet a été généré dans une autre application et que l’objet de base doit rester inchangé. Lorsque cette option est désactivée, de grands changements effectués à des niveaux de subdivision plus élevés déplaceront le niveau 0.

::: tip 

La subdivision lisse tous les bords vifs par défaut. Pour garder des arêtes légèrement nettes, essayez d’utiliser la subdivision linéaire ou Sharp border sur les 2 premiers niveaux de subdivision, puis désactivez-la pour les niveaux supérieurs. Cela créera un maillage subdivisé semi-net.

:::


## ![](/icons/voxel.webp) Remesh voxel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Lorsque vous utilisez le `Remesh Voxel`, tout le maillage forcera la topologie à avoir une résolution uniforme, ce qui signifie que tous les polygones ont plus ou moins la même taille. C’est très utile lorsque vous ne voulez pas penser à la topologie et simplement faire de la sculpture libre.

Un flux de travail de sculpture typique peut commencer par l’utilisation du `Remesh Voxel` pour bloquer une forme grossière avec une faible résolution.
Appuyez simplement sur le bouton *Remesh* de temps en temps lorsque vous étirez trop le maillage afin d’éviter trop de distorsion.

![](/videos/voxel_remesher.mp4)


::: tip Voxel ?
Comme indiqué ci-dessus, Nomad est un logiciel polygonal, mais le `Remesh Voxel` est une exception où une autre approche est utilisée (temporairement) pour effectuer le remeshing.

Une grande différence est que l’approche voxel n’accepte pas les auto-intersections, elles seront donc résolues.
De plus, elle ne supporte pas les maillages avec des trous.

Par trous, on ne parle pas du `trou de genre` (le `trou` d’un donut), mais plutôt de maillages qui ne sont pas `étanches`/`fermés`.
Concrètement, cela signifie qu’avant d’appliquer le remeshing, tous les trous seront comblés, de manière similaire à l’outil [Trim](tools.md#trim) ou à la [fonction de remplissage de trous](scene.md#hole-filling).
:::

### Remesh {#voxel-remesh}
Exécuter le remesh voxel.

### Résolution {#voxel-resolution}
La taille des voxels utilisés pendant le calcul. Lors de la modification de ce paramètre, un motif en damier sera superposé sur le maillage pour donner un aperçu du résultat.

### Construire la multirésolution {#build-multiresolution}
Créer des niveaux de multirésolution inférieurs pour le remesh voxel. Si vous utilisez le motif en damier pour définir une résolution, et que vous réglez Build multiresolution sur 2, le résultat final aura un niveau de détail correspondant au curseur de résolution, et si vous allez dans l’onglet multires, il sera au niveau 2, ce qui signifie que vous avez des maillages multirésolution de plus faible résolution aux niveaux 1 et 0. C’est un bon moyen à la fois de générer un maillage propre avec des polygones réguliers, et d’avoir un maillage de contrôle de plus faible résolution.

::: tip Astuce : Build multiresolution et lissage stable

Cette option peut parfois provoquer des « boucles » dans la géométrie qui peuvent être difficiles à lisser, causant de petites bosses. Si cela arrive, activez le `Stable smoothing` dans les options de l’outil Smooth. 

:::

### Conserver les arêtes nettes {#keep-sharp-edges}
Active l’accrochage des nouveaux points aux arêtes vives du maillage original. Cela peut introduire de la distorsion.

## ![](/icons/dynamic.webp) Topologie dynamique {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
La multirésolution et le remesh voxel sont des méthodes industrielles courantes pour contrôler la topologie, mais toutes deux exigent que vous surveilliez que vous n’étirez pas trop les polygones, ou que vous ne les serrez pas trop.

La Topologie dynamique est une méthode alternative. Pendant que vous sculptez, Nomad ajoutera et supprimera de manière adaptative des polygones pendant le coup de pinceau, de sorte que graver de petits détails ajoutera de nombreux petits polygones là où vous en avez besoin, et le lissage ailleurs supprimera des polygones.

Notez que la topologie dynamique utilisera des polygones triangulaires plutôt que des quads. Cela peut paraître un peu désordonné, mais il est presque préférable de ne pas regarder le wireframe, concentrez-vous simplement sur la création d’une belle sculpture sans vous soucier de la topologie, puis plus tard vous pourrez utiliser l’un des autres outils de remeshing de Nomad pour générer un maillage quad propre.

Voir la vidéo ci-dessous en action.

![](/videos/dynamic.mp4)

### Activé {#enabled}
Activer la topologie dynamique. Une icône DynTopo sera placée sous les curseurs de rayon et d’intensité du pinceau pour vous permettre d’activer/désactiver la Dyntopo par outil.

### Détail {#dyn-detail}
Contrôle la quantité de détail, son comportement change en fonction de la sélection « Detail based on... », voir ci-dessous.

### Détail basé sur... {#detail-based-on}
| Méthode | Description                                                     |
| :-----: | :-------------------------------------------------------------: |
| Screen  | Le niveau de détail dépend de la taille de l’objet à l’écran. Le curseur de détail est à 100 % ou plus pour un détail fin, produisant de petits triangles, ou à 1 % pour un faible détail, produisant de grands triangles.  |
| Radius  | Le rayon de l’outil définit la quantité de détail. Utilisez un petit rayon d’outil pour un détail fin, un grand rayon d’outil pour un faible détail. Le curseur de détail est un multiplicateur sur ce ratio.                     |
| Constant | Le curseur de détail définit la quantité de détail, et n’est pas affecté par la taille de l’écran ou de l’outil.             |

::: tip ASTUCE : mode Radius

Pour mieux comprendre le fonctionnement du mode Radius, commencez à déplacer le curseur de détail avec un doigt, puis en même temps changez le rayon de l’outil avec un autre doigt. Vous verrez comment ils sont liés.

:::

### Préférer... {#prefer}
| Méthode | Description        |
| :-----: | :----------------: |
| Speed   | Favoriser la vitesse |
| Quality | Favoriser la qualité |

Lorsque vous favorisez la `Quality`, les 2 principales différences sont :
- le raffinement est appliqué avant la sculpture, vous aurez donc moins d’artefacts d’interpolation lors de la peinture ou de la sculpture de très petits détails
- le raffinement s’exécute jusqu’à ce qu’il converge vers le bon niveau de détail, par opposition à un comportement incrémental.
 
Ainsi, si vous sculptez de très petits détails ou faites des traits rapides, la topologie sera toujours affinée comme prévu.


### Utiliser la pression sur le rayon {#use-pressure-on-radius}
Pertinent uniquement si `Radius` est activé. Lorsqu’il est activé, le niveau de détail reflétera toujours la taille du pinceau, même lorsque la taille du pinceau est affectée par la pression du stylet.

### Utiliser la retombée du trait {#use-stroke-falloff}

Inclut également la courbe de dégressivité (falloff) du pinceau et l’alpha dans les calculs de dyntopo.

### Méthode {#method}
Que vous utilisiez la `Topologie dynamique` sur votre [Brush](#brush) ou [Globalement](#global), vous pouvez choisir dans quel mode elle fonctionne :

| Méthode        | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Peut ajouter et supprimer des faces, c’est le mode utilisé dans la vidéo ci-dessus |
| Subdivision    | Ajoute uniquement de nouvelles faces, ne peut pas en supprimer        |
| Decimation     | Supprime uniquement des faces, ne peut pas en ajouter                 |

### Protéger la zone masquée {#protect-masked-area}
Active la protection des zones masquées pour empêcher la modification de la topologie.

### Extrapolation des sommets {#vertex-extrapolation}


### Détail {#all-detail}
La résolution utilisée pour l’opération de remesh. Si Dyntopo est en mode `Constant`, ce sera la même valeur que le curseur Detail en haut de ce menu.

### Remesh {#dyn-remesh}
Exécuter un remesh global en utilisant l’algorithme de dyntopo. En général, vous devriez utiliser le [Remesh Voxel](#voxel-remesher) pour un remeshing complet.

Cependant, un avantage par rapport aux voxels est que la zone masquée sera protégée, vous pouvez donc mieux contrôler où mettre plus ou moins de densité.



## ![](/icons/topo_extra.webp) Divers {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu engrenage {#gear-menu}
De nombreux outils de ce menu ont des options supplémentaires. Elles sont accessibles via l’icône d’engrenage à côté du titre de la section.

### Décimation {#decimation}

![](/images/topology_decimation.webp)

Réduire le nombre de polygones en essayant de conserver autant de détails que possible, en utilisant des polygones triangulaires.

Cette fonction peut être utile si vous souhaitez exporter pour l’impression 3D.
Cependant, vous ne devriez probablement pas l’utiliser si vous voulez continuer à sculpter dessus, car elle peut produire des triangles irréguliers.

Notez que les zones masquées ne seront pas décimées.

![](/videos/decimate.mp4)

::: tip

L’utilisation de l’outil [Quadremesh](tools.md#quad-remesher) sur des objets très haute résolution peut prendre beaucoup de temps à calculer et donner des résultats difficiles à contrôler. Le prétraitement du maillage avec des [facegroups](tools.md#facegroup-1) et la décimation rendront Quadremesh beaucoup plus rapide, et permettront un contrôle bien plus fin de la topologie.

* Créez des facegroups sur le maillage pour définir votre flux de quads idéal.
* Utilisez Facegroup relax pour obtenir des bords de facegroup lisses.
* Décimez. Cela garantira que vous n’avez pas de faces fines ou déformées sur les bords de facegroup. Dans les paramètres de décimation, assurez-vous que facegroup est activé. Cela fera suivre les arêtes de triangles exactement les bords de vos facegroups.
* Dans les options de Quadremesh, assurez-vous que relax est désactivé (puisque vous avez déjà relaxé le maillage) et vous devriez obtenir de bons résultats.

:::

#### Décimer {#decimate}
Lancer l’opération de décimation.

Les icônes à côté du bouton Decimate vous permettent d’activer/désactiver des options qui affectent la décimation. Le pourcentage indique la force de cette option, et peut être défini dans le menu avancé (engrenage).

* ![](/icons/palette.webp)  `Preserve Painting` - Place plus de triangles là où il y a des détails de peinture.
* ![](/icons/triforce.webp) `Uniform Faces` - Préfère créer des triangles de taille homogène.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - La décimation essaiera de conserver les bords proches de la géométrie ouverte et des trous.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - La décimation essaiera de conserver les bords de facegroup.
* ![](/icons/uv.webp) `Preserve UV Borders` - La décimation essaiera de conserver les bords d’UV.

#### ![](/icons/cog.webp) Menu engrenage de décimation {#decimate-gear-menu}
Le menu engrenage contient ces options avancées :
##### Préserver la peinture {#preserve-painting}
La case à cocher active/désactive ce mode, la valeur détermine à quel point les détails de peinture seront préservés. Des valeurs plus élevées préserveront davantage la peinture. Mettez 0 si vous ne vous souciez pas de la peinture.


##### Faces uniformes {#uniform-faces}
La case à cocher active/désactive ce mode. Des valeurs plus élevées produiront des triangles de taille similaire.

##### Préserver les bordures {#preserve-borders}
Active pour empêcher la décimation des bords. Les poids de bord peuvent être sélectionnés pour les bords de `Geometry`, de `Face Group` ou d’`UV`.

#### Triangles cibles {#target-triangles}
Définir le nombre cible de triangles. La valeur par défaut est 50 %, le bouton percent/target permet de basculer entre un pourcentage ou un nombre de polygones cible exact.



### Dépliage UV - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Calculer les coordonnées de texture (UV) pour le maillage courant, en préférant généralement créer plus d’îlots avec des coupures, afin de minimiser la distorsion.

La petite icône d’œil entre le titre du menu et le menu engrenage permet d’activer/désactiver l’aperçu des UV sur l’objet.

![](/videos/unwrap.mp4)

#### Déplier {#unwrap}
Calculer les UV pour l’objet sélectionné, qui seront affichés en arrière-plan.

#### Supprimer les UV {#delete-uvs}
Supprimer les UV de l’objet.

#### ![](/icons/cog.webp) Menu engrenage UVAtlas {#uvatlas-gear-menu}
Le menu engrenage contient ces options avancées :

#### Groupe de faces {#atlas-face-group}

Utiliser les facegroups pour définir les coupures des UV.

##### Étirement max {#max-stretch}
Des valeurs faibles créent moins de distorsion et plus d’îlots, des valeurs élevées créent plus de distorsion et moins d’îlots. 

##### Espacement des îlots {#island-spacing}
La quantité d’espace (padding) entre les îlots. Des valeurs faibles gaspillent moins d’espace, mais augmentent le risque de bavures de textures entre les îlots. 

::: warning
Le calcul des UV peut prendre du temps, il est préférable d’avoir un maillage avec moins de 100k sommets.
:::

::: tip UV ?
Une analogie courante pour les UV est l’emballage d’un cadeau : quelle est la meilleure façon de découper le papier cadeau pour recouvrir complètement un objet, sans chevauchements ? 

Les UV sont similaires, mais au lieu de découper le papier, vous découpez l’objet. Imaginez que votre modèle soit fait de plastique fin, comment le découperiez-vous pour le déplier à plat, le peindre dans cet état plat, puis le réassembler ?

Imaginez maintenant que la surface de votre modèle soit faite de lycra extensible. Vous pourriez étirer le modèle à plat, ou le découper, ou une combinaison des deux. Mais si vous peignez un damier sur l’objet une fois aplati, le damier sera déformé lorsque vous le réassemblerez. Quelle est la meilleure méthode, plus de coupures avec moins de distorsion, ou moins de coupures avec plus de distorsion ?

Les UV sont des instructions qui indiquent aux logiciels 3D comment « découper et étirer » l’objet lors de l’application des textures. L’outil UV Atlas utilise généralement une approche « plus de coupures, moins de distorsion ».


:::

::: tip UV et Nomad et autres applications

La plupart des modèles texturés que vous trouverez en ligne seront texturés avec des UV. Nomad peut les importer et les afficher via le panneau [material](material#textures).

Lorsque les modèles sont créés dans Nomad, vous pouvez peindre directement sur les objets sans UV. Si vous devez les exporter vers d’autres applications, par exemple [Procreate](https://procreate.art/), vous pouvez « baker » les informations de couleur de Nomad dans des textures via les UV. 

:::

### Dépliage UV - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

Les UV BFF privilégient une approche « moins de coupures, plus de distorsion ». 

#### ![](/icons/cog.webp) Menu engrenage UV BFF {#uv-bff-gear-menu}

#### Groupe de faces {#bff-face-group}

Utiliser les facegroups pour définir les coupures des UV.

##### Nombre de cônes {#cone-count}
Définir le nombre de projections principales utilisées. Des valeurs plus faibles produiront moins d’îlots, mais plus de distorsion.

##### Patches sans couture {#seamless-patches}
Affecte la disposition des patches UV, fonctionne mieux avec des facegroups soigneusement créés.

### Bake -> texture {#bake-texture}
![](/images/topology_bake_menu.webp)

Le baking de texture créera des textures en projetant les autres objets visibles de la scène dans les UV de l’objet sélectionné.

Voici le flux de travail typique pour le baking :
- Vous avez un maillage avec des détails fins et de la peinture
- Dupliquez-le
- Décimez-le (mettez `Preserve painting` à 0)
- Faites un UV unwrap
- Bakez !

Par défaut, Nomad prendra en compte tous les maillages visibles dans la scène.
Vous pouvez également utiliser le mode Solo pour masquer rapidement la plupart des autres maillages.
S’il n’y a pas d’autres objets visibles, alors il prendra toute la scène en compte.

Vous devriez maintenant avoir un maillage de faible résolution qui conserve la plupart de la peinture et des détails de votre objet précédent.

Après l’opération, les couleurs de sommets seront déplacées dans une nouvelle couche désactivée, afin qu’elles n’interfèrent pas avec les textures.

#### À partir de lui-même {#tex-from-itself}
Baker le niveau de multirésolution le plus élevé vers le niveau le plus bas sur l’objet courant. C’est simple à configurer, mais souvent vous aurez besoin de plus de contrôle, auquel cas l’option suivante est plus utile.

#### À partir de la haute résolution () {#tex-from-high-res}
Baker à partir des autres objets visibles de la scène vers l’objet sélectionné. Le nombre entre parenthèses indique le nombre d’autres objets visibles qui seront utilisés comme cibles haute résolution, et bakés dans l’objet basse résolution courant avec UV. Les autres objets n’ont pas besoin d’être similaires en disposition ou en topologie à l’objet baké, ce qui permet des flux de travail de baking très flexibles.

#### Résolution {#tex-bake-resolution}
La résolution de la texture bakée. Les textures de baking sont toujours carrées, donc 1024 créera une image 1024x1024. 

Les boutons ci-dessous sont des raccourcis pour des résolutions couramment utilisées. À titre de référence, 512x512 est relativement petit, par exemple pour des graphismes web et une géométrie simple. 4096x4096 (4k pour faire court) est destiné aux rendus de haute qualité.

#### ![](/icons/cog.webp) Menu engrenage de bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Le menu engrenage contient ces options avancées :

##### Normale, Rugosité, Métallicité, Couleur, Émissif, Opacité {#tex-normal-roughness-metalness-color-emissive-opacity}
Ces cases à cocher déterminent quelles propriétés seront bakées, chacune dans une carte séparée. Une fois le baking terminé, elles seront ajoutées comme textures au matériau de l’objet courant.

##### Sauvegarde {#tex-backup}
Pour prévisualiser les textures bakées, les informations de peinture de l’objet doivent être désactivées. Cette option transférera toute information de peinture vers une nouvelle couche en tant que sauvegarde afin qu’elle puisse être facilement activée/désactivée.

#### Rayon de cage {#tex-cage-radius}
Ajuste la distance à partir de l’objet de baking à laquelle les rayons sont envoyés pour rechercher les objets cibles. Par défaut, cette distance est maintenue faible pour éviter les artefacts, mais peut être augmentée si les objets cibles sont éloignés de l’objet de baking.

##### Décalage de rayon {#tex-ray-offset}
Ajuste l’endroit d’où commencent les calculs de baking sur l’objet de baking. Par défaut, ils commencent à 5 % au-dessus de la surface, ce qui évite la plupart des artefacts courants. Si les objets cibles sont très éloignés de l’objet de baking, ce décalage peut devoir être augmenté.


### Reprojeter vers sommet {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projeter les détails sculptés, la peinture, les couches, les textures dans des valeurs de sommets.

On peut le considérer comme l’inverse du baking ; si le baking transfère les propriétés de sommets vers des textures, la reprojection transfère les textures (et autres propriétés)
 de nouveau vers les sommets.

::: tip
Lorsque vous utilisez `Bake to texture` ou `Reproject to vertex`, à la fois les couleurs de sommets et les textures de matériau seront prises en compte.
:::

#### À partir de lui-même {#vertex-from-itself}
Convertir les textures du matériau en valeurs de sommets. Ce bouton ne sera actif que si l’objet possède des UV et que des textures sont actives dans le matériau.

::: tip ASTUCE : peinture de texture
Nomad ne supporte pas directement la peinture et l’édition de textures, mais des résultats très similaires peuvent être obtenus en projetant les textures -> valeurs de sommets, en peignant sur les sommets, puis en bakant sommets -> textures :

1. Configurez un objet low poly avec des UV
1. Chargez des textures dans son matériau
1. Subdivisez-le suffisamment pour pouvoir peindre dessus
1. `Reproject to vertex` en mode `From itself`, la texture est maintenant convertie en valeurs de sommets
1. Peignez, lissez, estompez, tamponnez, faites toutes les modifications dont vous avez besoin
1. `Bake to texture`, en mode `From itself`. Ces modifications sont reconverties en textures.
:::

#### À partir de la haute résolution () {#vertex-from-high-res}
Convertir tous les objets visibles en valeurs de sommets sur l’objet sélectionné. Le nombre sur ce bouton indique le nombre d’objets visibles.

::: tip
La reprojection d’autres objets peut être utilisée non seulement pour transférer des informations de couleur depuis d’autres objets, mais aussi pour projeter des sommets sur d’autres objets, par exemple des bandages peuvent être projetés sur un personnage.
:::

#### ![](/icons/cog.webp) Menu engrenage de reprojection {#vertex-reproject-gear-menu}
Le menu engrenage contient ces options avancées :

#### Sommets, Rugosité, Métallicité, Couleur, Opacité, Opacité->Masque, Masque, Couches, Groupe de faces {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Ces cases à cocher déterminent quelles propriétés seront projetées sur l’objet sélectionné. 

#### Relaxer {#vertex-relax}
Le maillage sélectionné peut voir sa disposition lissée ou relaxée dans une certaine mesure pour mieux s’adapter aux cibles de reprojection. Smooth est préférable pour les maillages haute résolution. Relax est préférable pour les maillages low poly. Auto laissera Nomad déterminer la meilleure méthode.

#### Itérations {#vertex-iterations}
Combien de fois l’opération de relax doit être appliquée pendant la reprojection.

#### Rayon de cage {#vertex-cage-radius}
Ajuste la distance à partir de l’objet sélectionné à laquelle les rayons sont envoyés pour rechercher les objets cibles. Par défaut, cette distance est maintenue faible pour éviter les artefacts, mais peut être augmentée si les objets cibles sont éloignés de l’objet de baking.

#### Biais de rayon {#vertex-ray-bias}
Des valeurs plus faibles favoriseront la projection vers le point le plus proche sur la surface cible. Des valeurs plus élevées favoriseront un point d’intersection utilisant la normale de surface. 

#### Décalage de rayon {#ray-vertex-offset}
Ajuste l’endroit d’où commencent les calculs de baking sur l’objet sélectionné. Par défaut, ils commencent à 5 % au-dessus de la surface, ce qui évite certains artefacts. Si les objets cibles sont très éloignés de l’objet de baking, ce décalage peut devoir être augmenté.


### Quad Remesh - Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remesher en utilisant l’[algorithme Instant Meshes de Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Il analysera le flux d’un maillage et créera une topologie quad propre.

::: tip
Sur iOS et desktop, l’outil [Quad remesher](tools#quad-remesher) donne de meilleurs résultats et plus de contrôle.
:::

#### Remesh {#instant-remesh}
Lancer l’opération Instant Meshes.

#### Quads cibles {#target-quads}
Le nombre de polygones quads que Quad Remesh tentera de créer.

#### ![](/icons/cog.webp) Menu engrenage Quad Remesh Instant {#quad-remesh-instant-gear-menu}
Le menu engrenage contient ces options avancées :

##### Angle de plis {#crease-angle}
Un seuil d’angles vifs qui aidera à guider l’opération de remesh.

#### Remplissage max des trous {#max-fill-hole}
L’algorithme peut parfois produire des trous indésirables. Si un trou a moins de sommets que cette valeur, il sera comblé.

### Trous {#holes}
![](/images/topology_holes_menu.webp)
La plupart du temps, votre objet sera probablement étanche, ce qui signifie que le maillage est « fermé ».

Si votre objet a des trous, vous pouvez les combler. Notez que cela ne fonctionne que sur des trous « naïfs », il ne peut donc pas « souder » deux bords séparés.

![](/videos/hole_filling.mp4)

::: tip
Lorsque vous lancez le Remesh Voxel, tous les trous sont automatiquement fermés, que vous l’utilisiez sur un ou plusieurs maillages.
:::

#### Fermer les trous {#close-holes}
Exécuter l’action de fermeture des trous.

#### ![](/icons/cog.webp) Menu engrenage des trous {#holes-gear-menu}
Le menu engrenage contient ces options avancées :

##### Détail {#fill-detail}
La densité de polygones utilisée pour combler le trou. Pendant le déplacement de ce curseur, un motif en damier sera affiché sur le modèle, ce qui donnera une indication de la taille des triangles à utiliser. La case à cocher désactivera cela et utilisera uniquement les points existants, ce qui créera généralement de longs triangles fins au-dessus du trou, difficiles à sculpter.

##### Remplir les non-manifold {#fill-non-manifold}
Essayer de combler les trous non manifold.

##### Groupe de faces {#fill-face-group}

Lors du remplissage des trous, chaque trou doit-il obtenir son propre facegroup (Auto), doivent-ils tous partager un facegroup (Off), ou ne pas créer de facegroups (On).

### Forcer manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Essayer de nettoyer les arêtes non manifold. Cela peut être utile pour les logiciels externes qui ne supportent pas les arêtes ayant plus de 2 faces en commun.

#### Nettoyer {#clean}
Exécuter l’action de nettoyage.
#### ![](/icons/cog.webp) Menu engrenage Forcer manifold {#force-manifold-gear-menu}
Le menu engrenage contient ces options avancées :

#### Supprimer les petites faces {#delete-small-faces}
Un seuil utilisé pour supprimer et fusionner les petits polygones.


### Triplanaire {#triplanar}
![](/images/topology_triplanar_menu.webp)
Convertit le maillage en primitive [triplanar](scene.md#triplanar).
Vous perdrez probablement beaucoup de détails au passage.

#### Forcer cubique {#force-cubic}
Forcer le triplanar à être un cube. Sinon, le triplanar s’ajustera à la boîte englobante la plus proche autour de votre objet.

#### Convertir {#convert}
Exécuter l’action triplanar.

#### Résolution {#triplanar-resolution}
La taille de voxel utilisée dans l’opération triplanar.

## ![](/icons/dot.webp) Primitive {#primitive}
Paramètres pour la primitive sélectionnée. Ils sont également disponibles dans la barre d’outils de la vue des primitives.

![](/images/topology_primitive_screenshot.webp)