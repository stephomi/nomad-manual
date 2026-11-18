# ![](/icons/toolbox.webp) Outils {#tools}

![](/images/tools_menu.webp)

::: tip
Rendez-vous plus bas dans la section [Outils](#tools-1) pour la description de chaque outil.
:::

## Présentation {#overview}

Les outils se choisissent dans la `Boîte à outils` à droite, et se contrôlent avec les commandes de l'outil à gauche. Des réglages supplémentaires se trouvent dans le menu `Outil`, dans le menu en haut à droite.

Les outils de type pinceau ont des réglages de taille et d'intensité. Les outils de sélection proposent plusieurs styles de sélection. En bas des commandes de l'outil, des raccourcis donnent accès aux opérations fréquentes (Lisser, Masque, Masquer, Groupe de faces, Gizmo, Couleur, Alpha).

Les outils de Nomad sont classés par couleur dans la boîte à outils (désactivez `Outils colorés` dans le menu [Interface](interface.md) pour des libellés neutres) :

* <span class=brush>**Outils de pinceau**</span> (Argile, Pinceau, Lisser, Calque, Gonfler, SupprCalque, Quad Remesher)
* <span class=move>**Outils de déplacement**</span> (Déplacer, Glisser, Élastique, Décaler)
* <span class=mask>**Outil de masque**</span> (Masque)
* <span class=paint>**Outils de peinture**</span> (Peindre, Estomper)
* <span class=flatten>**Outils d'aplatissement**</span> (Aplatir, Plan, Polir)
* <span class=pinch>**Outils de pincement**</span> (Pli, Pincer)
* <span class=stamp>**Outils de tampon**</span> (Tampon, VDM)
* <span class=selection>**Outils basés sur une sélection**</span>, où l'on dessine d'abord un masque 2d avant qu'une opération ne s'applique (Découper, Scinder, Projeter)
* <span class=creation>**Outils de création**</span> (Tube, Tour, Insérer)
* <span class=transform>**Outils de transformation**</span> (Transformation, Gizmo, Disposer, Treillis)
* <span class=misc>**Outils divers**</span> (Groupe de faces, Masquer)
* <span class=view>**Outils de vue**</span> (Vue, Mesurer, Sélectionner)



Beaucoup de ces outils se personnalisent avec différents comportements de pinceau, la pression, des textures, etc., via le menu [Trait](stroke.md).


### Commandes du pinceau {#brush-controls}

La barre d'outils de gauche contient les curseurs de rayon et d'intensité, puis des commandes propres à chaque catégorie d'outils, détaillées ci-dessous.

![](/images/tool_left_panel.webp)

::: tip
Pour beaucoup d'outils, le curseur d'intensité peut dépasser 100 %, ça vaut le coup d'expérimenter !
:::

### Sous-mode {#sub-mode}
Le bouton situé juste sous le curseur d'intensité est le bouton `Soustr.`. Son libellé et sa fonction changent avec chaque outil ; quand vous l'activez, il déclenche un comportement alternatif, généralement l'inverse. Par exemple, pour [Peindre](#paint) il active un mode Effacer, pour [Pli](#crease) il crée des arêtes en relief plutôt que des creux, etc.

Par défaut, il fonctionne comme un bouton maintenu : gardez-le enfoncé pour l'activer temporairement, il se désactive dès que vous le relâchez. Si vous le touchez brièvement, le sous-mode reste activé.

### Raccourcis {#shortcuts}
En bas de la barre d'outils de gauche se trouvent des raccourcis vers [Lisser](#smooth), [Masque](#mask), [Masquer](#hide), [Groupe de faces](#facegroup), [Gizmo](#gizmo), [Couleur](painting.md#pbr-sliders) et [Alpha](stroke.md#alpha).

Par défaut, ils fonctionnent tous comme des boutons maintenus : gardez-en un enfoncé pour l'activer temporairement, il se désactive dès que vous le relâchez. Si vous le touchez brièvement, ce raccourci reste activé.

### Commandes de sélection {#selection-controls}

Les outils [Masque](#mask), [Peindre](#paint), [Découper](#trim), [Scinder](#split), [Projeter](#project), [Groupe de faces](#facegroup), [Masquer](#hide) et [Sélectionner](#select) utilisent tous des commandes similaires pour sélectionner des zones du maillage.

![](/images/tools_shape_selector_panel.webp)

Touchez le bouton de forme dans la barre d'outils de gauche (il affiche la forme actuelle, `Lasso` par défaut) pour ouvrir une fenêtre avec les formes. Pour les outils qui fonctionnent aussi au pinceau (Masque, Peindre, Groupe de faces, Masquer), cette même fenêtre contient aussi les types de trait.

* `Vue` - Aucune forme : l'outil ne fait rien de particulier, comme en mode caméra.
* `Lasso` - Une forme dessinée à main levée.
* `Polygone` - Une forme fermée, faite de courbes et/ou de segments droits. Voir [Édition de forme](#shape-editing) plus bas.
* `Courbe` - (Projeter uniquement) - Une courbe à main levée pour la projection.
* `Tracé` - (Projeter uniquement) - Une courbe définie par des points. Voir [Édition de forme](#shape-editing) plus bas.
* `Ligne` - Tracez une ligne pour définir un plan de coupe. Par défaut, l'opération s'applique immédiatement au maillage ; changez l'option `Modifier` si vous ne le souhaitez pas (appui long ou glissement sur l'icône de la ligne).
* `Bande` - Une bande entre deux guides parallèles, avec un dégradé d'un guide à l'autre. `Étendre` garde la pleine valeur au-delà du guide le plus éloigné au lieu de s'arrêter à la bande, `Inverser` change le guide de départ du dégradé.
* `Rect` - Tracez une diagonale : elle définit les coins d'un rectangle. Un appui long ou un glissement affiche l'option `Modifier`, `Carré` pour forcer un carré, et `Centré` pour que le premier point soit le centre du rectangle.
* `Ellipse` - Tracez une diagonale : elle définit la taille d'une ellipse. Un appui long ou un glissement affiche l'option `Modifier`, `Cercle` pour forcer un cercle, et `Centrée` pour que le premier point soit le centre de l'ellipse.
* `Inverser` - Inverse le masque de la forme, ou la direction de l'outil Projeter.

La plupart des outils ont une option `Modifier` qui décide de ce qui se passe quand vous finissez de dessiner la forme :
* `Modifier : désactivé` - L'opération s'applique dès que vous relâchez.
* `Modifier : activé` - La forme reste modifiable. Un bouton vert apparaît à côté de la forme pour lancer l'opération. Vous pouvez ainsi retoucher la forme et ajuster la vue ; quand la forme vous convient, touchez le bouton vert.
* `Modifier : maintenir` - L'opération s'applique au relâchement, sauf si vous restez appuyé à la fin du trait pour continuer à modifier la forme.

### Édition de forme {#shape-editing}
L'édition des polygones et celle des courbes fonctionnent de la même façon :

* Pour commencer, tracez une ligne pour définir 2 points, puis tirez depuis le milieu de la ligne pour créer un polygone ou une courbe.
* Touchez un point pour le faire passer de lisse à anguleux, et inversement.
* Touchez et faites glisser un segment de courbe ou de ligne pour créer de nouveaux points.
* Pour supprimer un point, faites-le glisser sur son voisin jusqu'à ce qu'il devienne rouge.
* L'icône de corbeille dans le coin de l'icône du polygone ou du tracé supprime la forme.

### Menu des réglages {#settings-menu}

Beaucoup d'outils ont des réglages supplémentaires dans le menu `Outil`, dans le menu en haut à droite. Ce menu est grisé pour les outils qui n'en ont pas.

![](/images/tools_settings_menu.webp)

## Outils {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Argile](#clay)       | ![](/icons/tool_brush.webp)   <br> [Pinceau](#brush)     | ![](/icons/tool_move.webp)       <br> [Déplacer](#move)              | ![](/icons/tool_drag.webp)      <br> [Glisser](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Élastique](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Lisser](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Masque](#mask)       | ![](/icons/tool_paint.webp)   <br> [Peindre](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Estomper](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Aplatir](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Plan](#planar)       | ![](/icons/tool_polish.webp)  <br> [Polir](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Pli](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Pincer](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Découper](#trim)              | ![](/icons/tool_split.webp)     <br> [Scinder](#split)         | ![](/icons/tool_project.webp)   <br> [Projeter](#project)     | ![](/icons/tool_layer.webp)   <br> [Calque](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Gonfler](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Décaler](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Tampon](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [SupprCalque](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Tour](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insérer](#insert)   | ![](/icons/tool_transform.webp)  <br> [Transformation](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Groupe de faces](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Masquer](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Mesurer](#measure) | [Disposer](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Sélectionner](#select)       | ![](/icons/tool_lattice.webp)   <br> [Treillis](#lattice)     | ![](/icons/tool_view.webp)    <br> [Vue](#view)       |

------

### ![](/icons/tool_clay.webp) Argile {#clay}
L'outil Argile est idéal pour construire les volumes de votre sculpture. `Soustr.` retire de la matière.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pinceau {#brush}
Le pinceau standard. `Soustr.` retire de la matière.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Déplacer {#move}
La zone sous le pinceau colle au pinceau, ce qui permet une déformation élastique. La sélection est conservée pendant tout le déplacement : si vous éloignez le pinceau puis le ramenez à son point de départ, vous ne verrez aucune déformation.

Le sous-mode est `Normale` : il déplace la zone sous le pinceau le long de la normale de la surface.

Ce pinceau convient aussi bien aux grandes déformations qu'aux petits ajustements précis.

#### Réglages de Déplacer {#move-settings}

* `Rayon (Arrière-plan)` - La distance au bord d'un modèle à laquelle vous pouvez encore sculpter, pratique pour travailler la silhouette d'un objet. Décochez-le pour ne saisir la surface que si vous commencez sur le modèle.
* `Sommet du même côté uniquement` - Ignore les sommets orientés dans le sens opposé à la déformation.
* `Direction` - Utilisée par le sous-mode `Normale`, elle décide si un glissement pousse ou tire la surface :
    * `Auto` - Choisit pour vous l'une des deux méthodes ci-dessous, selon l'angle de la normale de la surface.
    * `Normale 3D` - Compare la position du pointeur à l'écran avec la normale de la surface vue depuis la caméra.
    * `XY` - Se sert de la position du pointeur à l'écran (haut/bas, gauche/droite) pour décider de pousser ou de tirer.
    * `Seuil` - Avec `Auto`, l'angle limite qui décide de la méthode utilisée.
* `Vitesse de roulis` - Vous pouvez faire tourner la zone saisie pendant que vous la déplacez : faites rouler deux doigts, faites tourner votre stylet sur lui-même, ou maintenez une touche de modification (Alt, Ctrl, Shift ou Cmd) en faisant glisser la souris. Il y a un curseur pour le doigt, un pour le stylet et un pour la souris ; décochez-en un pour désactiver cette entrée.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Glisser {#drag}
La zone sous le pinceau colle au pinceau, ce qui permet une déformation élastique. Contrairement à Déplacer, la sélection est mise à jour en continu pendant le trait : vous pouvez donc étirer des formes longues, comme des serpents, surtout avec la topologie dynamique activée.

Le sous-mode est `Normale` : il déplace la zone sous le pinceau le long de la normale de la surface.

Ce pinceau convient aux changements de forme plus libres et gestuels.

#### Réglages de Glisser {#drag-settings}

Glisser a les mêmes réglages que [Déplacer](#move-settings) : `Rayon (Arrière-plan)`, `Sommet du même côté uniquement`, `Direction` et `Vitesse de roulis`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Élastique {#elastic}
Saisissez et tirez la surface comme avec [Déplacer](#move), mais avec une déformation élastique : au lieu de s'arrêter au bord du pinceau, la traction s'estompe doucement avec la distance sur tout l'objet, un peu comme du caoutchouc qu'on étire. Le rayon du pinceau règle la largeur de la traction.

Le sous-mode est `Normale` : il déplace la zone sous le pinceau le long de la normale de la surface.

Ce pinceau convient aux grands changements de proportions, doux et qui restent lisses.

#### Réglages d'Élastique {#elastic-settings}

Élastique a les mêmes réglages que [Déplacer](#move-settings), sauf `Sommet du même côté uniquement`. `Rayon (Arrière-plan)` est désactivé par défaut.

### ![](/icons/tool_smooth.webp) Lisser {#smooth}
Lisse la zone en faisant la moyenne de la position des points. Cet outil dépend beaucoup de la densité de polygones :
plus il y a de polygones, moins le lissage est efficace.

Le sous-mode est `Relâcher` : il ne lisse que le maillage filaire en essayant de conserver les détails de la forme.

#### Réglages de Lisser {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Groupe de faces {#smooth-facegroup}

* `Relâcher` - Lisse les bordures des groupes de faces. Utilisez une intensité supérieure à 100 % pour lisser rapidement les bordures. `Auto` ne lisse que si l'aperçu des groupes de faces est activé, `Non` désactive, `Oui` active.

##### Sommet {#vertex}
* `Préserver le volume` - Lisse sans rétrécir la surface, pour que des lissages répétés ne dégonflent pas vos formes. Le bouton en forme de roue dentée à côté contient les quantités `Réduire` et `Gonfler` utilisées pour cela.
* `Préserver les bordures` - Sur les maillages à bords ouverts, comme un plan, les coins peuvent être lissés. Cette option garde immobiles les sommets situés sur le bord du maillage.
* `Lissage stable` - Essaie de rendre le lissage indépendant de la topologie. Fonctionne mieux avec une densité de topologie variable et une forte intensité de lissage.
* `Relâcher` - Identique au mode alternatif Relâcher de la barre d'outils de gauche.

##### Peinture {#painting}
* `Lissage écran` - Utilisez cette option pour obtenir un lissage indépendant de la topologie, même avec beaucoup de polygones. `Auto`, `Non` ou `Oui`.
* `Échantillons écran` - La qualité du lissage : des valeurs élevées lissent mieux, mais plus lentement.

::: tip
Une densité de polygones élevée peut demander une intensité supérieure à 100 %. Des valeurs très hautes (300 %, 500 %) font aussi un bon outil de sculpture, qui force les zones sous le pinceau à devenir vite plates et lisses, comme un coup de maillet sur de l'argile !
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Masque {#mask}
Cet outil vous permet de masquer des sommets. Les sommets masqués sont protégés de la sculpture et de la peinture.

Le sous-mode est `Démasquer` : il efface le masque là où il a été peint.

Comme les sélections des logiciels de peinture 2d, les masques peuvent être peints au pinceau ou créés avec des formes de sélection (`Lasso`, `Rect`, `Bande`...), puis floutés ou rendus plus nets. Choisissez le pinceau ou la forme dans la fenêtre de trait de la barre d'outils de gauche, voir [Commandes de sélection](#selection-controls).

Contrairement aux logiciels de peinture 2d, ils peuvent aussi être créés à partir des groupes de faces, et servir à créer de la nouvelle géométrie par extrusion ou extraction.

![](/videos/tool_mask1.mp4)

 Une barre d'outils apparaît en haut de la vue 3d avec des commandes supplémentaires.

![](/images/tool_mask_toolbar.webp)

Touchez le titre de la barre pour la déplier ou la replier, ou la flèche en haut à droite pour la placer en haut ou en bas de l'interface.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Tout effacer       | Efface le masque de tous les objets. Quand d'autres objets sont aussi masqués, un bouton `Effacer` supplémentaire n'efface que les objets sélectionnés |
| ![](/icons/invert.webp)        Inverser           | Inverse le masque                                                                          |
| ![](/icons/sharpen.webp)       Netteté            | Rend le bord du masque plus net                                                            |
| ![](/icons/blur.webp)          Flou               | Floute le bord du masque                                                                   |
| ![](/icons/outline.webp)       Bordure            | Masque le bord ouvert du maillage, comme le contour d'un plan ou le pourtour d'un trou     |
| ![](/icons/blur.webp)          Flou ->            | Glissez vers la droite pour flouter le masque, vers la gauche pour le rendre plus net      |
| ![](/icons/circle_plus.webp)   Étendre ->         | Glissez vers la droite pour agrandir la zone masquée, vers la gauche pour la réduire       |
| ![](/icons/intensity.webp)     Renforcer ->       | Glissez vers la droite pour renforcer le masque, vers la gauche pour l'atténuer, sans changer sa forme |
| ![](/icons/dig.webp)           Creux ->           | Reconstruit le masque à partir de la courbure de la surface : glissez vers la droite pour que seuls les creux restent modifiables, vers la gauche pour que seules les bosses le restent |
| ![](/icons/culling.webp)       Devant             | Active ou désactive le masquage des seuls sommets orientés vers la caméra                  |
| ![](/icons/eye_open.webp)      Visible            | Avec les formes, active ou désactive l'ignorance des sommets cachés derrière d'autres surfaces |
|                                 Convertir          | Convertit le masque en groupe de faces                                                     |
| ![](/icons/group_to_mask.webp) Au toucher (groupe de faces) | Une fois activé, les groupes de faces sont affichés, et toucher un groupe de faces le masque |
|                                 Au toucher (masque) | Une fois activé, toucher un « îlot » de polygones masqués ou non masqués remplit cet îlot. |
| ![](/icons/connect.webp)       Connectée          | Une fois activé, les traits de masque n'affectent que la topologie connectée.              |

##### Geste rapide de masque {#mask-quick-gesture}
Vous pouvez faire des gestes à la ZBrush en maintenant le bouton de masque rapide de la barre d'outils de gauche :
| Action   | Geste (raccourci en bas à gauche maintenu) |
| :------: | :----------------------------------------: |
| Inverser | Toucher l'arrière-plan                     |
| Effacer  | Glisser sur l'arrière-plan                 |
| Flou     | Toucher une zone masquée                   |
| Netteté  | Toucher une zone non masquée               |


#### Réglages de Masque {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Les réglages de Masque servent surtout à créer de la géométrie à partir du masque. Les onglets en haut choisissent l'opération : [Extraire](#extract), [Scinder](#split-mask) ou [Creuser](#carve). Les options en dessous changent selon l'opération.

* `Aperçu` - Montre à quoi ressemblera la nouvelle géométrie pendant que vous ajustez les réglages.
* `Rayons X` - Quels objets sont affichés en rayons X pendant l'aperçu : `Aucun`, `Non sélectionné`, `Sélectionné` ou `Tout`.

##### Extraire {#extract}
* `Extraire` - Crée la géométrie extraite sous forme de nouvel objet.
* `Fermeture` - Comment la forme extraite est refermée. `Aucune` duplique les polygones masqués dans une nouvelle forme et la laisse ouverte. `Remplir` fait de même, puis remplit et lisse le trou au dos (à éviter sur les surfaces planes). `Coque` referme la forme en utilisant la valeur de `Hauteur` : c'est le choix par défaut.

::: tip

Si l'aperçu est activé avec les rayons X, toucher le bouton Extraire peut d'abord dérouter. Comme le menu est actif, Nomad essaie de prévisualiser une extraction sur votre nouvelle forme et affiche la surface d'origine en rayons X. Mais comme la nouvelle surface n'a aucun masque, il ne peut rien prévisualiser, et Nomad vous avertit « Rien à extraire ! ».

C'est normal : fermez le menu des réglages de masque pour voir la nouvelle forme et l'originale, puis sélectionnez à nouveau la surface d'origine si vous devez effacer le masque ou en dessiner de nouveaux.
:::

##### Scinder {#split-mask}
* `Scinder` - Extrait à la fois les zones masquées ET non masquées dans de nouvelles formes.
* `Fermeture` (masqué) - Comment la partie masquée est refermée, avec les mêmes choix `Aucune`, `Remplir` et `Coque` qu'Extraire.
* `Fermeture` (non masqué) - Comment la partie non masquée est refermée, avec les mêmes choix.

##### Creuser {#carve}
* `Creuser` - Se comporte comme si vous aviez découpé la surface sur une profondeur égale à la `Hauteur`, comme quand on détache un morceau d'écorce d'orange. La `Hauteur` ne peut pas être à 0.

##### Hauteur {#thickness}
* `Hauteur` - La hauteur de la forme extraite. Le bouton Plus/Moins fait alterner entre une extrusion vers l'extérieur, vers l'intérieur, ou des deux côtés.

##### Lissage {#smoothness}
Une fois activé, lisse la forme extraite ; fonctionne mieux avec beaucoup de polygones.
* `Tout` / `Uniquement les bords` - Lisse toute la forme, ou seulement ses bords en laissant intacte la forme de la surface du dessus.
* `Itérations` - Avec `Tout`, la quantité de lissage appliquée. Des valeurs élevées donnent des bords arrondis très lisses, mais la forme commence à s'éloigner de celle du masque.
* `Paroi` - Avec `Uniquement les bords`, la quantité de lissage sur les parois. Son bouton alterne entre Relâcher, qui garde les angles vifs, et Lisser, qui les arrondit aussi.
* `Intérieur` - Avec `Uniquement les bords`, à quel point la surface du dessus est égalisée. Son bouton alterne entre Relâcher, qui garde les détails sculptés et n'égalise que la direction d'extrusion (pour que les détails ne créent plus de pics), et Lisser, qui lisse la surface elle-même.

##### Côtés {#edge-loop-side}
* `Droit` - Des parois simples sur les côtés de la forme extraite.
* `Biseau` - (Extraire avec `Coque` uniquement) Un bord incliné sur l'arête avant. `Biseau` règle sa largeur, en % de la `Hauteur` ou en unités du monde (le bouton à côté permet de basculer), `Divisions du biseau` le subdivise (`Auto` par défaut), et une courbe vous permet de modeler son profil.
* `Profil` - Façonne les parois avec une courbe de profil, avec une `Largeur` en % de la `Hauteur` ou en unités du monde.
* `Masque` - La hauteur suit le masque : les zones floues du masque ont une hauteur plus faible, ce qui permet des formes douces et de hauteur variable.
* `Divisions de la paroi` - Le nombre de boucles d'arêtes sur les côtés. Avec `Auto`, Nomad choisit le nombre de divisions qui donne des polygones carrés, assortis aux polygones de la zone masquée.



### ![](/icons/tool_maskSelector.webp) Masque de sélection {#selection-mask}
L'outil Masque de sélection (SelMasque) fait désormais partie de l'[outil Masque](#mask). Pour masquer avec des formes plutôt qu'avec un trait de pinceau, choisissez une forme (`Lasso`, `Polygone`, `Rect`...) dans la fenêtre de trait de l'outil Masque, voir [Commandes de sélection](#selection-controls).

Le sous-mode `Démasquer` fonctionne aussi avec les formes : il efface le masque à l'intérieur de la forme.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Peindre {#paint}
Applique la couleur et les propriétés du matériau. Pour en savoir plus sur les matériaux, consultez la section [Peinture](painting.md).

Le sous-mode est `Effacer` : il retire la peinture.

En plus des traits de pinceau, Peindre peut aussi remplir des formes (`Lasso`, `Rect`, `Bande`...), voir [Commandes de sélection](#selection-controls).

#### Réglages de Peindre {#paint-settings}
* `Filtrage par calque` - Fonctionne comme le verrouillage de l'alpha d'un calque dans Photoshop ou Procreate. Quand vous peignez sur un calque avec cette option activée, vous ne pouvez modifier que les zones déjà peintes ; les zones non peintes sont protégées. Disponible uniquement quand un calque est sélectionné.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Estomper {#smudge}
Estompe la couleur et les propriétés du matériau. Le menu des réglages d'Estomper contient un curseur `Qualité` : des valeurs basses donnent des traits plus rapides.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Aplatir {#flatten}
Aplatit la zone en projetant les points sur le plan moyen.

Le sous-mode est `Remplir` : il définit un plan à partir du point le plus haut, et a tendance à tirer les points vers le haut.

#### Réglages d'Aplatir {#flatten-settings}

* `Verrouiller la normale` - Utilise la direction du plan calculée au premier contact. Désactivé par défaut.
* `Verrouiller l'origine` - Utilise le premier contact comme centre du plan. Désactivé par défaut, et ne peut être activé qu'avec `Verrouiller la normale`.

Quand l'une de ces options ou les deux sont désactivées, vous pouvez creuser l'aplat progressivement ou changer l'angle du plan avec de longs traits qui passent sur des profondeurs et des courbures différentes. Combiné aux options d'échantillonnage de zone du menu du pinceau, cela offre un contrôle très précis.

::: tip
Dans les zones très courbées, par exemple quand vous voulez aplatir les joues mais que l'outil touche sans cesse les côtés du nez, créez un masque pour protéger les zones que l'outil Aplatir ne doit pas modifier.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Plan {#planar}
Rend les points coplanaires en les projetant sur le plan moyen, mais avec moins d'accumulation qu'Aplatir. On obtient des surfaces plus nettes, aux arêtes franches. Des traits rapides poussent et tirent davantage la surface ; des traits plus lents, qui partent de zones déjà planes vers l'extérieur, conservent mieux le plan.

Le sous-mode est `Remplir` : il définit un plan à partir du point le plus haut, et a tendance à tirer les points vers le haut.

Plan est en fait le même outil qu'`Aplatir`, mais avec `Verrouiller la normale` activé : il tend à créer des surfaces plus stables aux arêtes franches, tandis qu'Aplatir est plus sculptural et sert à créer des zones à demi plates.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Polir {#polish}
Un autre membre de la famille Aplatir, réglé pour polir les surfaces en plans nets. C'est le même outil qu'`Aplatir`, avec d'autres réglages par défaut dans [Trait](stroke.md) : `Traînée`, `Filtre de normale de zone` et `Filtre de profondeur` sont activés.

Le sous-mode est `Remplir`, comme pour Aplatir.

Polir a les mêmes réglages qu'[Aplatir](#flatten-settings) : `Verrouiller la normale` et `Verrouiller l'origine`.

### ![](/icons/tool_crease.webp) Pli {#crease}
L'outil Pli sert à sculpter de petites entailles ou des creux.

Le sous-mode est `Inverser` : il crée un pli en relief.

#### Réglages de Pli {#crease-settings}

* `Force de pincement` - À quel point les sommets sont attirés latéralement vers le pinceau. Avec le pincement à 1 et le décalage à 0, la profondeur de la surface ne change pas, seule la topologie change : les arêtes sont attirées vers le trait.
* `Facteur de décalage` - À quel point les sommets sont poussés ou tirés en profondeur. Avec le pincement à 0 et le décalage à 1, vous obtenez des plis profonds ou des bourrelets en relief, mais d'aspect irrégulier, car trop peu de géométrie est attirée vers le pli pour bien définir ses côtés ou son fond.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pincer {#pinch}
Cet outil sert à affûter les arêtes.

Le sous-mode est `Inverser` : il écarte les sommets.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Découper {#trim}
L'outil Découper retire un morceau de votre maillage et propose plusieurs façons de traiter le trou laissé. Il utilise les [Commandes de sélection](#selection-controls) pour définir la découpe.

Le sous-mode est `Inverser` : il inverse la forme, pour retirer l'autre côté.

::: tip
Comme cet outil projette depuis la caméra, un avertissement s'affiche si la caméra est en mode perspective.

En mode orthographique, la coupe à travers le maillage est parallèle à la vue, ce qui correspond généralement à ce qu'on attend. Avec une caméra en perspective, la coupe paraît différente sur la face éloignée de l'objet et sur la face proche.
:::

#### Réglages de Découper {#trim-settings}

Les réglages sont regroupés sous `Bouchage des trous` :

* `Peinture du trait` - Si la peinture est activée dans le menu Peinture, la zone rebouchée est remplie avec la couleur sélectionnée.
* `Booléen` - Bouche le trou de la découpe avec une zone de quads. La zone remplie est plane.
* `Ancien` - Bouche le trou de la découpe avec une zone triangulée. La zone remplie est plane.
* `Remplir` - Bouche le trou avec une zone triangulée. La zone remplie est une surface courbe, comme le film d'une bulle de savon.
* `Aucun` - Ne bouche pas le trou.

Avec `Booléen`, la section `Détail` contient :

* `Forme` - La taille approximative des quads et des triangles du côté de la forme découpée.
* `Trous` - La taille approximative des triangles ou des polygones sur le trou rebouché. Le bouton de liaison à côté de `Détail` le garde synchronisé avec `Forme` ; déliez-le pour le régler séparément.
* `Préserver la topologie` - Ne lisse pas et ne simplifie pas le bord de la coupe, pour conserver la topologie d'origine près des faces masquées et cachées.

Avec `Ancien` :

* `Détail` - La taille approximative des triangles utilisés pour la découpe.
* `Lissage des trous` - À quel point les triangles sont relâchés sur la zone remplie.
* `Seuil epsilon` - Une valeur à ajuster pour améliorer l'ancien algorithme de bouchage des trous.

Avec `Remplir` :

* `Détail` - La taille approximative des triangles utilisés pour la découpe.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Scinder {#split}
Semblable à l'outil [Découper](#trim), à la différence que Découper supprime la sélection, alors que Scinder la conserve sous forme de nouvel objet.

Le sous-mode est `Diviser` : chaque morceau est conservé comme un objet à part, de sorte que des formes qui se chevauchent (par exemple avec la symétrie) sont coupées en parties séparées au lieu d'être réunies en une seule.

#### Réglages de Scinder {#split-settings}

Scinder a les mêmes réglages de `Bouchage des trous` que [Découper](#trim-settings) : `Peinture du trait`, les méthodes `Booléen`, `Ancien`, `Remplir` et `Aucun`, et leurs options de `Détail`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projeter {#project}
L'outil Projeter ressemble à l'outil [Découper](#trim), mais il ne supprime ni ne crée de géométrie : il déplace simplement les sommets pour qu'ils épousent la sélection.

![](/videos/tool_project.mp4)

::: tip
Si vous utilisez Projeter sur un calque, vous pouvez doser le mélange entre la forme d'origine et la forme projetée avec le curseur du calque.
:::

### ![](/icons/tool_layer.webp) Calque {#layer}
Élève la surface, mais en limitant la hauteur.

Si vous gardez le stylet posé et repassez sur une zone, Calque monte jusqu'à une certaine hauteur puis s'arrête, alors que les autres outils continuent d'accumuler de la hauteur.

Notez que par défaut, la limite n'est définie que par trait ! Si vous commencez un nouveau trait, il part de la nouvelle hauteur de la surface.

Pour fixer une hauteur maximale constante sur de nombreux traits, utilisez l'outil Calque avec le système de [Calques](layers.md) de Nomad.

Créez un calque, puis utilisez cet outil. La hauteur maximale est désormais fixée par le calque : vous pouvez donner autant de coups de pinceau que vous voulez, la hauteur restera toujours la même.

`Soustr.` utilise une profondeur minimale, pour créer des rainures.

#### Réglages de Calque {#layer-settings}

* `Utiliser les données du calque` - Une fois activé, et si un calque est sélectionné, utilise les données du calque pour fixer la hauteur maximale. Un avertissement vous le rappelle quand aucun calque n'est sélectionné.
* `Gonfler` - Une fois activé, ajuste la direction dans laquelle Calque agit, pour des résultats plus lisses.
* `Relâcher (Normale)` - Avec `Gonfler` activé, la quantité de lissage appliquée aux normales.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Gonfler {#inflate}
Déplace les sommets le long de leur propre normale. `Soustr.` les déplace le long de leur normale inversée.

#### Réglages de Gonfler {#inflate-setings}
* `Relâcher (Normale)` - La quantité de lissage appliquée aux normales.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Décaler {#nudge}
Déplace ou « étale » les points dans la direction du trait.

Le sous-mode est `Pli` : il pousse un pli de matière le long du trait, avec un bourrelet devant le pinceau et un creux derrière.

#### Réglages de Décaler {#nudge-settings}
* `Lisser` - À quel point la zone sous le pinceau est lissée pendant que vous la décalez, ce qui garde propre la surface étalée.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Tampon {#stamp}

Touchez et faites glisser pour soulever une zone de la sculpture selon la forme de l'alpha sélectionné.

C'est simplement l'[outil Pinceau](#brush) avec le type de trait `Saisie + rayon`.

`Soustr.` enfonce le tampon dans la surface au lieu de le faire ressortir.

::: tip
Le Tampon donne généralement de meilleurs résultats sur une géométrie haute résolution. Si vous cherchez en ligne « wrinkles alpha », « pores alpha », « scales alpha », etc., ces textures alpha associées au Tampon sont un excellent moyen d'ajouter des détails organiques à la sculpture d'un personnage.

Les deux modes de trait servent à des choses différentes.

* `Saisie + rayon` a une *hauteur* fixe ; le glissement règle la largeur et la rotation du tampon. Idéal pour les textures de peau, qui doivent avoir la même profondeur ou hauteur, mais des rotations et des échelles différentes pour cacher la répétition des motifs.
* `Saisie + intensité` a une *largeur* fixe ; le glissement règle la rotation et la hauteur du tampon. Idéal pour des rivets, qui doivent tous avoir la même taille, mais des rotations et des hauteurs différentes.

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Applique une carte de déplacement vectoriel (VDM). Contrairement à un alpha, qui ne peut que pousser la surface vers le haut ou vers le bas, un VDM contient une vraie forme 3d : il peut donc tamponner des formes en surplomb, comme des oreilles, des cornes ou des feuilles enroulées. Il fonctionne comme le [Tampon](#stamp), avec les mêmes modes de trait `Saisie + rayon` et `Saisie + intensité`.

`Soustr.` (`Inverser`) inverse la profondeur du tampon, pour l'enfoncer dans la surface comme un moule.

Le VDM lui-même se choisit dans le menu [Alpha](stroke.md#alpha), qui a aussi un curseur `Hauteur` pour mettre à l'échelle uniquement la hauteur du tampon, sans changer son déplacement latéral.

Le bouton `Créer` de la barre d'outils de gauche vous permet de fabriquer vos propres tampons :

* `Nouveau VDM…` - Ajoute un plan préparé pour sculpter un VDM. Sculptez votre forme dessus, puis faites-en le baking avec `Topologie -> Baking -> VDM` : Nomad ajoute le nouveau tampon à la bibliothèque de VDM et le sélectionne.
* `Capturer un VDM` - (Expérimental) Faites glisser sur la surface d'un modèle pour saisir cette zone et la transformer en tampon VDM. `Tolérance` aplatit en douceur le bord de la capture.

::: tip
Évitez la DynTopo quand vous sculptez un plan VDM : elle abîme les UV du plan et déforme le tampon. Gardez aussi la sculpture à distance du bord du plan, sinon le tampon aura une arête dure.
:::


### ![](/icons/tool_clearLayer.webp) SupprCalque {#delete-layer}
Cet outil réinitialise localement les calques ; il faut un calque actif, sinon rien ne se passe. Il efface les données sculptées du calque, ainsi que sa peinture quand la peinture est activée.

Le sous-mode est `Inverser` : il renforce légèrement le calque au lieu de l'effacer.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube {#tube}
Crée un tube en dessinant une courbe.
![](/images/tool_tube_new.webp)

Une fois le tube créé, son tracé peut être modifié dans l'espace 3d, avec des commandes semblables à celles de l'[Édition de forme](#shape-editing) standard et des outils d'édition de courbe.

![](/videos/tool_tube.mp4)

#### Barre d'outils de gauche du Tube {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

La barre d'outils de gauche propose les options suivantes :

* `Synchroniser` - Si le tube actuel est instancié et que des nœuds enfants du tube diffèrent d'une instance à l'autre, ce bouton les resynchronise.
* `Aligner` - Une fois activé, les modes Courbe et Tracé s'accrochent aux autres objets pendant que vous dessinez. Désactivé, seul le premier point s'accroche, puis le reste du tube est dessiné à cette profondeur.
* `Décalage` - Règle la profondeur de l'accroche : à 0 %, le centre de la section du tube s'accroche à la surface ; les valeurs positives l'éloignent de la surface, les valeurs négatives l'enfoncent. 100 % correspond au rayon du tube.
* `Vue` - Aucun mode de dessin, pour déplacer librement la caméra.
* `Courbe` - Esquissez un tube à main levée. Il a un petit menu déroulant :
    * `Modifier` - Ce qui se passe quand vous terminez le trait, voir [Commandes de sélection](#selection-controls) : créer le tube aussitôt, garder la courbe modifiable avec un cercle vert de validation à côté, ou `Maintenir` à la fin du trait pour continuer à la modifier.
    * `Fermé` - Transforme le tube en boucle.
    * `Continuer à dessiner` - Après avoir validé un tube, reste dans l'outil pour dessiner le suivant.
    * `Précision` - Le nombre de points de courbe utilisés pour convertir le tracé dessiné en tube. À 0 %, le moins de points possible, mais les petits changements de courbure sont perdus. À 100 %, très précis, avec beaucoup de points.
* `Tracé` - Créez un tube en touchant l'écran pour placer les points de la courbe. Touchez le cercle vert pour valider le tracé. Il a un petit menu déroulant :
    * `B-spline` - Une autre méthode de dessin de courbe, où les points ne sont généralement pas placés sur la courbe elle-même, mais qui peut donner des résultats plus lisses que la méthode par défaut.
    * `Fermé` - Transforme le tube en boucle.
    * `Écran` - Une fois activé, le tracé est « épinglé » à l'écran : vous pouvez déplacer la vue et l'objet, le tracé reste en place. Désactivé, le tracé fait partie de la scène 3d et bouge avec la caméra et les objets.
* `Coupe` - La courbe devient un anneau autour de la forme, coupé à travers ses deux points dans la direction depuis laquelle vous regardiez.

##### Barre d'outils du haut du Tube {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Quand un tube est sélectionné, une barre d'outils apparaît en haut de la vue 3d avec des commandes supplémentaires. Touchez le titre de la barre pour la replier ou la déplier, et la flèche en haut à droite pour la placer en haut ou en bas de la vue 3d.

* `Valider` - Convertit le tube en polygones classiques pour pouvoir le sculpter.
* `Modifier` - Affiche les points de la courbe pour pouvoir les manipuler.
* `Miroir` - Ajoute un répéteur miroir comme parent de cette courbe.
* `Aligner` - Accroche les points de la courbe aux surfaces proches.
* `Fermé` - Relie le début et la fin de la courbe pour former une boucle.
* `B-spline` - Bascule entre l'interpolation Catmull-Rom et B-spline.
* `Capuchon` - Alterne entre des capuchons aux deux extrémités du tube, au début ou à la fin seulement, ou aucun capuchon.
* `Trou` - Donne de l'épaisseur au tube pour en faire un tuyau. Alterne entre un trou aux deux extrémités, à la fin seulement, ou aucun trou.
* `Rayon` - Alterne entre un rayon uniforme, un rayon au début et à la fin, ou un rayon par point de la courbe. Ils se modifient avec des poignées orange sur la courbe.
* `Torsion` - Alterne entre aucune torsion, une torsion uniforme, une torsion au début et à la fin, ou une torsion par point de la courbe. Elles se modifient avec des poignées roses sur la courbe.
* `Profil` - Alterne entre aucun profil (donc un profil circulaire), un profil uniforme, un profil au début et à la fin, ou un profil par point.
* `Éditeur de profil` - Affiche un éditeur de profil. Il fonctionne comme les outils d'[Édition de forme](#shape-editing), peut enregistrer et charger des préréglages de profil, et propose une option pour modifier le profil dans l'espace 3d.
* `Spirale` - Ouvre un menu pour ajouter une torsion en spirale au tube. Ce menu propose `Angle d'enroulement`, `Écart`, `Échelle` et `Décalage d'angle`.
* `Division X` - Le nombre de divisions autour du tube : avec 4 divisions, par exemple, le tube est carré.
* `Densité constante` - Une fois activé, garde des polygones carrés. Désactivé, vous pouvez régler la `Division Y` sur la longueur du tube.
* `...` - Menu des réglages du tube.

#### Option de suppression des points de courbe {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Sous la barre d'outils se trouve une option de suppression des points de courbe. Quand vous faites glisser un point de courbe près d'un autre, il devient rouge pour indiquer qu'il sera supprimé si vous le relâchez. Si vous faites de petites retouches et ne voulez pas supprimer de points, ce bouton désactive ce comportement.



#### Réglages du Tube {#tube-settings}
* `Primitive` - Des boutons pour activer ou désactiver les UV, ou pour valider le tube.
* `Subdivision secondaire` - Un raccourci pour régler le niveau de multirésolution avant la validation.
* `Subdivision linéaire` - Un raccourci pour régler le niveau de subdivision linéaire avant la validation.
* `Division X` - Identique à Division X dans la barre d'outils.
* `Division Y` - Identique à Division Y dans la barre d'outils.
* `Courbe (Répéteur)` - Convertit le tube en [Répéteur de courbe](scene.md#curve).

::: tip
Avec Division à 4 et Subdivision secondaire à 3, vous obtenez des tubes lisses aux extrémités arrondies, parfaits pour des vers, des serpents ou des parties du corps.
:::


### ![](/icons/tool_lathe.webp) Tour {#lathe}
Crée une surface de révolution en dessinant une courbe.

Cet outil est parfait pour des formes comme des vases ou des verres à pied.

![](/videos/tool_lathe.mp4)

#### Barre d'outils de gauche du Tour {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

La barre d'outils de gauche propose les options suivantes :

* `Synchroniser` - Si le tour actuel est instancié et que des nœuds enfants du tour diffèrent d'une instance à l'autre, ce bouton les resynchronise.
* `Fixe` - Une fois activé, l'axe du tour est fixe et affiché à l'écran. Cet axe a des points d'édition ajustables. Désactivé, l'axe du tour se met à jour automatiquement pour correspondre au début et à la fin de la courbe dessinée.
* `Vue` - Aucun mode de dessin, pour déplacer librement la caméra.
* `Courbe` - Dessinez le profil du tour d'un seul trait. Il a un petit menu déroulant :
    * `Modifier` - Ce qui se passe quand vous levez le stylet, voir [Commandes de sélection](#selection-controls) : créer le tour aussitôt, garder la courbe modifiable avec un cercle vert à côté pour créer le tour, ou `Maintenir` à la fin du trait pour continuer à la modifier.
    * `Fermé` - Relie le début et la fin de la courbe pour former une boucle.
    * `Continuer à dessiner` - Après avoir validé un tour, reste dans l'outil pour dessiner le suivant.
    * `Précision` - Le nombre de points de courbe utilisés pour convertir le tracé dessiné en tube. À 0 %, le moins de points possible, mais les petits changements de courbure sont perdus. À 100 %, très précis, avec beaucoup de points.
* `Tracé` - Créez un tour en touchant l'écran pour placer les points de la courbe. Touchez le cercle vert pour valider le tracé. Il a un petit menu déroulant :
    * `B-spline` - Une autre méthode de dessin de courbe, où les points ne sont généralement pas placés sur la courbe elle-même, mais qui peut donner des résultats plus lisses que la méthode par défaut.
    * `Fermé` - Transforme le tube en boucle.
    * `Écran` - Une fois activé, le tracé est « épinglé » à l'écran : vous pouvez déplacer la vue et l'objet, le tracé reste en place. Désactivé, le tracé fait partie de la scène 3d et bouge avec la caméra et les objets.

#### Barre d'outils du haut du Tour {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Quand un tour est sélectionné, une barre d'outils apparaît en haut de la vue 3d avec des commandes supplémentaires. Touchez le titre de la barre pour la replier ou la déplier, et la flèche en haut à droite pour la placer en haut ou en bas de la vue 3d.

* `Valider` - Convertit le tour en polygones classiques pour pouvoir le sculpter.
* `Modifier` - Affiche les points de la courbe pour pouvoir les manipuler.
* `Miroir` - Ajoute un répéteur miroir comme parent de ce tour.
* `Aligner` - Accroche les points de la courbe aux surfaces proches.
* `Stable` - Une fois activé, le profil de la courbe est rattaché à l'axe du tour. Désactivé, l'axe peut être modifié sans déplacer la courbe, ce qui permet des formes plus complexes.
* `Mise au point` - Fait pivoter la vue pour voir le profil de la courbe parfaitement à plat face à la caméra.
* `Fermé` - Relie le début et la fin de la courbe pour former une boucle.
* `Capuchon` - Si Fermé est désactivé, alterne entre des capuchons aux deux extrémités du tube, au début ou à la fin seulement, ou aucun capuchon.
* `Trou` - Donne de l'épaisseur au tour pour en faire un tuyau. Alterne entre un trou aux deux extrémités, à la fin seulement, ou aucun trou.
* `B-spline` - Bascule entre l'interpolation Catmull-Rom et B-spline.
* `Division X` - Le nombre de divisions autour du tour : avec 4 divisions, par exemple, le tour a un profil carré.
* `Densité constante` - Une fois activé, garde des polygones carrés. Désactivé, vous pouvez régler la `Division Y` sur la longueur du tube.
* `...` - Menu des réglages du tour.

#### Réglages du Tour {#lathe-settings}
* `Primitive` - Des boutons pour activer ou désactiver les UV, ou pour valider le tube.
* `Subdivision secondaire` - Un raccourci pour régler le niveau de multirésolution avant la validation.
* `Subdivision linéaire` - Un raccourci pour régler le niveau de subdivision linéaire avant la validation.
* `Division X` - Identique à Division X dans la barre d'outils.
* `Division Y` - Identique à Division Y dans la barre d'outils.
* `Courbe (Répéteur)` - Convertit le profil de la courbe en [Répéteur de courbe](scene.md#curve).

### ![](/icons/tool_insert.webp) Insérer {#insert}
Place un objet sur la surface d'un autre. À l'usage, c'est comparable au Tampon, mais pour des formes 3d complètes.

Si vous choisissez une primitive dans la barre d'outils de gauche, toucher et faire glisser sur n'importe quelle surface place une primitive à l'endroit touché, et le glissement règle sa taille. Une fois le glissement terminé, Insérer passe en mode [Transformation](#transform).

En mode Instance, faire glisser crée une nouvelle instance et la fait glisser sur la surface. Sa taille reprend celle de la première forme : vous pouvez ainsi placer de nombreuses instances de même taille d'un objet sur d'autres surfaces.

Vous n'êtes pas limité aux primitives ! Sélectionnez *n'importe quelle* forme dans la liste des objets : si Insérer est en mode Instance ou Clone, vous pouvez faire glisser des copies de l'objet sélectionné sur n'importe quelle autre surface.

Si un objet a un pivot personnalisé, celui-ci sert de point d'ancrage. Voir la vidéo ci-dessous.

La barre d'outils de gauche propose aussi `Vue`, pour déplacer la caméra sans rien insérer, et `Synchroniser` : quand l'objet cible est instancié, le nouvel objet est aussi ajouté sur toutes les autres instances.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformation {#transform}
Déplacez, faites pivoter et mettez à l'échelle un modèle directement avec 1 ou 2 doigts, généralement sur la surface d'un autre objet.

La barre d'outils de gauche contient ces boutons :

* `Cloner` / `Instancier` - Crée une copie ou une instance de l'objet, voir la barre d'outils du [Gizmo](#left-menu-toolbar).
* `Déplacer` - Un glissement à un doigt déplace l'objet. Quand l'accroche est activée, l'objet glisse le long de la surface sous votre doigt.
* `Pivoter` - Un glissement à un doigt fait pivoter l'objet. Quand l'accroche est activée, la rotation se fait autour de la normale de la surface sous votre doigt.
* `Échelle` - Un glissement à un doigt met l'objet à l'échelle.

Une barre d'outils en haut de la vue 3d contient :

* `Cible` - Si l'outil déplace l'objet, son groupe ou ses sommets, comme pour le [Gizmo](#left-menu-toolbar).
* `Accrocher` - Accroche le modèle sur les autres surfaces.
* `Surface` / `Sommet` - Avec `Accrocher`, accroche sur la surface, ou sur le sommet le plus proche.

L'outil Transformation permet d'utiliser rapidement 2 de ces modes avec 2 doigts :

* Faites glisser un objet pour le placer. Arrêtez de bouger le premier doigt, sans le lever de l'écran.
* Posez le deuxième doigt sur l'écran en gardant le premier appuyé. En faisant glisser le deuxième doigt, vous mettez l'objet à l'échelle.
* Levez le deuxième doigt et continuez à faire glisser le premier : l'objet repasse en mode déplacement.

Vous pouvez aussi changer le second mode en touchant l'écran avec un deuxième doigt :

* Faites glisser l'objet pour le placer, arrêtez de bouger, sans lever le doigt de l'écran.
* Touchez l'écran avec un deuxième doigt en gardant le premier appuyé.
* L'outil passe en mode rotation. Faites glisser le premier doigt pour régler la rotation.
* Touchez à nouveau avec le deuxième doigt : l'outil repasse en mode déplacement.

Cela permet de cloner rapidement des objets sur un autre, par exemple des rochers sur un paysage. Notez que le bouton de clonage est aussi dans la barre d'outils de gauche, à portée de main :

* Utilisez l'outil Transformation pour mettre un rocher en place.
* Relâchez, touchez le bouton de clonage.
* Déplacez ce rocher, faites-le pivoter ou mettez-le à l'échelle au besoin.
* Relâchez, touchez le bouton de clonage.
* Déplacez ce rocher, et ainsi de suite.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Cet outil vous permet de déplacer, faire pivoter et mettre à l'échelle des objets, et de modifier leur pivot.

La poignée affichée dans la vue 3d offre les fonctions suivantes :

* `Déplacer` - Faites glisser une ligne fléchée pour déplacer sur X/Y/Z. Faites glisser le point couleur pêche au centre du gizmo pour déplacer librement dans le plan de l'écran. Faites glisser les carrés rouge, vert et bleu pour déplacer sur les plans X/Y/Z.
* `Pivoter` - Faites glisser les cercles rouge, vert et bleu pour faire pivoter sur X/Y/Z. Faites glisser la sphère à l'intérieur des cercles pour une rotation libre.
* `Échelle` - Faites glisser les points rouge, vert et bleu extérieurs pour mettre à l'échelle sur X/Y/Z. Faites glisser les cônes rouge, vert et bleu extérieurs pour mettre à l'échelle sur les plans X/Y/Z. Faites glisser le cercle extérieur couleur pêche pour une mise à l'échelle uniforme.

![](/images/tool_gizmo.webp)

#### Nœuds et sommets {#nodes-and-vertices}

Dans Nomad, chaque objet est composé d'un nœud et de sommets :

* `Nœud` - La « poignée » de l'objet, qui stocke sa translation, sa rotation et son échelle, ce qu'on appelle sa matrice de transformation.
* `Sommets` - Les points qui définissent la surface d'un objet ; ils stockent la position et les informations de peinture.

Pour une simple boîte de 8 sommets, vous pouvez la déplacer en modifiant sa matrice de transformation, ou en modifiant la position de ses sommets. Quand vous sculptez, vous voulez généralement modifier les sommets ; quand vous déplacez des objets avec le gizmo, vous voulez généralement modifier le nœud. Nomad vous permet de faire les deux.

#### Barres d'outils du Gizmo {#left-menu-toolbar}

La barre d'outils de gauche contient :

* `Cloner` - Crée une copie indépendante de l'objet actuel, que vous pouvez éloigner avec le gizmo.
* `Instancier` - Crée une instance de l'objet actuel. Les objets sont liés : les modifications de sculpture sur l'un apparaissent sur toutes les instances.
* `Pivot` - (Icône de cadenas, à la place du bouton `Soustr.`) Une fois activé, le gizmo peut être déplacé et pivoté sans déplacer l'objet. Comme `Soustr.`, maintenez-le pour un changement rapide, ou touchez-le pour qu'il reste activé.

Une barre d'outils en haut de la vue 3d contient les autres commandes :

* `Cible` - Détermine si le gizmo agit sur le nœud ou sur les sommets d'un objet :
    * `Auto` - Le réglage par défaut. Il fonctionne comme `Groupe`, mais si le maillage a un masque ou si la symétrie est activée, il fonctionne comme `Sommet`.
    * `Sommet` - Applique la transformation aux sommets, en tenant compte du masque et de la symétrie. Ne fonctionne pas sur les primitives non validées, et les instances sont aussi affectées.
    * `Objet` - Ne déplace que l'objet actuel, en ignorant la symétrie et le masque. Les objets enfants restent immobiles.
    * `Groupe` - Déplace l'objet et le reste de sa hiérarchie, en ignorant la symétrie et le masque.
    * `Instance` - (Objet et Groupe) Pareil, mais toutes les instances de l'objet se déplacent aussi.
* `Pivot` - Une fenêtre pour placer rapidement le pivot, expliquée [plus bas](#pivot).
* `Tout` / `Déplacer` / `Pivoter` / `Échelle` - Affiche toutes les poignées du gizmo, ou seulement celles de déplacement, de rotation ou d'échelle.
* `Épingler` - Par défaut, le gizmo se place sur le pivot de l'objet sélectionné. Quand Épingler est activé, le gizmo reste là où il se trouve.
* `Aligner` - Aligne le pivot sur l'objet actuel, ou sur le monde.
* `Accrocher` (rotation) - Arrondit les valeurs de rotation par paliers ; la valeur du palier s'affiche et se modifie quand l'accroche est active. Son option `Aimant` fait coller la rotation à un palier au moment où elle le franchit, puis la laisse repartir librement ; désactivez-la pour sauter d'un palier à l'autre.
* `Accrocher` (translation) - Arrondit les valeurs de translation par paliers ; la valeur du palier s'affiche et se modifie quand l'accroche est active.

#### ![](/icons/reset.webp) Pivot {#pivot}
La fenêtre `Pivot` de la barre d'outils du haut permet de modifier rapidement le pivot. La position et l'orientation du pivot pilotent le gizmo.

**Réinitialiser**
* `Auto` - Centre de l'objet, aligné sur sa transformation.
* `Centre` - Place le pivot au centre de l'objet, en conservant son orientation.
* `Bas` - Place le pivot en bas, au centre de l'objet. Touchez à nouveau pour utiliser plutôt la boîte englobante dans le repère du monde.
* `Haut` - Place le pivot en haut, au centre de l'objet. Touchez à nouveau pour utiliser plutôt la boîte englobante dans le repère du monde.
* `Objet` - Place le pivot à l'origine de l'objet, aligné sur sa transformation.
* `Masque` - Place le pivot au centre de la zone non masquée. Touchez à nouveau pour passer à la zone masquée.
* `Aligner` - Réinitialise les rotations pour les aligner sur le monde, en conservant la position.
* `Vue` - Aligne le pivot sur la vue actuelle, en conservant la position. Il ne suit pas la caméra ensuite.

**Au toucher (mode Pivot)**

Actif uniquement quand `Pivot` est activé, il détermine ce qui se passe quand vous touchez une fois la surface du maillage :
* `Aucun` - Ne fait rien quand l'objet est touché.
* `Normale` - Déplace et fait pivoter le pivot pour l'aligner sur la surface à l'endroit touché.
* `Premier` - Déplace (sans le faire pivoter) le pivot à l'endroit touché.
* `Milieu` - Place le pivot au milieu de l'objet, sous l'endroit touché.

#### Réglages du Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Compact` - Place les poignées supplémentaires du gizmo à l'extérieur ou à l'intérieur de la sphère de rotation.
* `Taille du Gizmo` - La taille du gizmo.
* `Épaisseur` - L'épaisseur des lignes du gizmo.
* `Opacité` - L'opacité du gizmo.
* `Masquer pendant l'action` - Masque temporairement ou non le gizmo pendant que vous le faites glisser.

-----

* `Seuil de roulis tangent` - Règle le comportement de la rotation quand vous faites glisser les cercles pour pivoter sur X/Y/Z. À 0, la rotation fonctionne comme une molette : faites tourner le gizmo en décrivant des cercles. À 90, elle fonctionne comme la ficelle d'un yo-yo : faites glisser en ligne droite en vous rapprochant ou en vous éloignant du point de départ. Les valeurs entre 0 et 90 combinent les deux : en dessous de la valeur, le mouvement est linéaire ; au-dessus, il est circulaire.
* `Saisie numérique` - Une fois activé, toucher une fois le gizmo ouvre une fenêtre pour saisir une valeur exacte sur l'axe touché.

::: warning
Les outils [Gizmo](#gizmo) et [Transformation](#transform) ont leur propre case de symétrie, distincte de la symétrie de sculpture !

Par défaut, cette symétrie est désactivée.
:::

##### Matrice {#matrix}
Les valeurs exactes de transformation de l'objet ne sont plus dans les réglages du Gizmo : elles ont rejoint le menu `Transformation`, dans le menu en haut à droite. Sa section `Matrice` contient :

* ![](/icons/target.webp) `Déplacer l'origine` - Déplace l'objet pour que son pivot soit au centre de la scène, qu'on appelle l'origine.
* ![](/icons/bake.webp)  `Appliquer` - Fige l'objet là où il se trouve, et remet les valeurs de translation et de rotation à 0, l'échelle à 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pivot` - Applique le pivot : les valeurs de la matrice correspondent alors à la position de la poignée du gizmo dans le monde.
* ![](/icons/reset.webp) `Réinitialiser` - Un raccourci qui remet les translations à 0, les rotations à 0 et l'échelle à 1, ce qui déplace et fait pivoter l'objet.

::: tip Appliquer ou appliquer le pivot
Créez une boîte, choisissez l'outil Gizmo, ouvrez et épinglez le menu `Transformation`. Par défaut, la translation et la rotation sont à 0, l'échelle à 1.

Activez le mode pivot, déplacez la poignée sur un côté, puis désactivez le mode pivot. Le pivot a changé, mais remarquez que les valeurs de translation sont toujours à 0.

Pour voir où se trouve *vraiment* le pivot, touchez le bouton `Pivot` d'application. Les valeurs de translation se mettent alors à jour. Notez que la boîte ne bouge pas pendant cette opération, ni en mode pivot.

Déplacez et faites pivoter la boîte, puis touchez `Déplacer l'origine`. L'objet se déplace pour que son pivot soit au centre du monde, mais sa rotation ne change pas.

Touchez `Réinitialiser` : la rotation est à son tour remise à 0.

Déplacez et faites pivoter à nouveau la boîte, puis touchez cette fois `Appliquer`. Le pivot reste en place, la boîte aussi, mais les valeurs de translation et de rotation sont remises à 0.

Entraînez-vous plusieurs fois ! Retenez que les valeurs du pivot sont cachées et que Nomad s'en occupe pour vous, mais que si vous avez besoin de placer le pivot à un endroit précis de l'espace, l'application du pivot le fait pour vous.

:::

* `Translation` - Les valeurs de translation X, Y, Z.
* `Rotation` - Les valeurs de rotation X, Y, Z.
* `Échelle` - L'échelle uniforme si elle est activée, sinon l'échelle X, Y, Z.
* `Cisaillement` - Les valeurs de cisaillement X, Y, Z, affichées uniquement quand l'objet est déjà cisaillé.
* `Échelle uniforme` - Permet de mettre à l'échelle uniformément, ou indépendamment sur chaque axe.

À gauche, vous pouvez déplacer le pivot du gizmo ; la vidéo ci-dessous le montre en action.
C'est surtout utile pour la rotation, car cela ne change rien pour la translation.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Groupe de faces {#facegroup}

Les groupes de faces vous permettent d'organiser votre objet en zones de faces de couleurs différentes. Dans Nomad, ces groupes servent de bien des façons :

* Une méthode de sélection rapide pour les masques
* Masquer ou afficher des parties de votre objet
* Organiser votre objet sans devoir le découper en plusieurs parties
* Définir des zones d'UV
* Guider le Quad Remesher
* Un contrôle supplémentaire pour des outils comme Lisser.

#### Barre d'outils de gauche des Groupes de faces {#facegroup-left-toolbar}

* `Groupe` - Le bouton affiche le groupe de faces actuel. Touchez-le pour afficher les groupes de faces disponibles sous forme de pastilles et en choisir un. Touchez une pastille pour la renommer, changer sa couleur ou la supprimer. `Supprimer les inutilisés` supprime les pastilles inutilisées, `Réinitialiser` les supprime toutes. L'icône plus permet de créer de nouvelles pastilles.
* `Point` - Peignez sur l'objet pour définir des groupes de faces. Quand « + Groupe de faces » est activé, chaque nouveau trait crée automatiquement un nouveau groupe de faces, pratique pour définir rapidement des zones. Un appui remplit la zone sélectionnée. Le curseur règle le rayon du point.
* `Relâcher` - Lisse les bordures des groupes de faces. Très utile pour obtenir des bords nets avant un remaillage en quads, ou pour définir des panneaux en modélisation hard surface. Les curseurs règlent le rayon et l'intensité du relâchement.
* Formes - Créez des groupes de faces avec des formes plutôt qu'au pinceau, via `Saisie + rayon`, `Lasso`, `Polygone`, `Ligne`, `Rect` et `Ellipse`. Voir [Commandes de sélection](#selection-controls) pour plus d'informations.
* `Choisir` - Le sous-mode. Une fois activé, il sélectionne la pastille là où le trait commence, et l'applique pour le reste du trait. Très utile pour nettoyer les zones de groupes de faces : si un groupe de faces déborde, activez `Choisir`, commencez un trait là où la pastille est correcte, et faites glisser jusqu'à la bordure pour réattribuer la bonne pastille.

#### Barre d'outils du haut des Groupes de faces {#facegroup-top-toolbar}

Une barre d'outils en haut de la vue 3d contient des commandes supplémentaires :

* `Relâcher (Tout)` - Faites glisser pour relâcher d'un coup les bordures de tous les groupes de faces.
* `Devant` / `Visible` / `Connectée` - Les mêmes filtres de trait que dans la barre d'outils de [Masque](#mask).
* `Depuis les normales` - Crée des groupes de faces selon l'angle entre les faces. La fenêtre propose l'`Angle`, et permet d'ignorer les petits groupes selon leur `Nombre de faces` ou leur `Surface`, avec un `Aperçu` avant de valider.
* `Depuis les parties` - Crée un groupe de faces pour chaque partie déconnectée.
* `Depuis les UV` - Crée un groupe de faces pour chaque îlot d'UV.
* `Depuis le masque` - Crée un groupe de faces à partir de la zone masquée.
* `Au toucher` - Choisissez ce que fait un appui sur un groupe de faces : le remplir avec le groupe de faces actuel, le cacher, lui appliquer un masque, ou le mettre en `Pose` (le groupe touché et ce qui se trouve au-delà sont démasqués, et le gizmo se place sur l'articulation, avec un curseur `Flou` pour le masque). Une seconde option `Au toucher`, disponible quand le maillage a un masque, limite l'appui aux faces situées du même côté du masque.
* Des boutons `Effacer` pour les outils [Masquer](#hide) et [Masque](#mask), pour tout réafficher ou effacer le masque sans quitter l'outil.

#### Réglages des Groupes de faces {#facegroup-settings}

Le menu `Outil` extrait les groupes de faces en nouveaux objets, avec les mêmes options que l'onglet `Extraire` des [Réglages de Masque](#mask-settings). Le bouton `Groupe de faces` en haut choisit les groupes à extraire, et un curseur `Écart` supplémentaire est proposé : il décale chaque bordure vers l'intérieur le long de la surface ; une valeur négative la décale vers l'extérieur pour créer un chevauchement. Pour des panneaux voisins, utilisez la moitié de l'écart souhaité.

### ![](/icons/tool_hide.webp) Masquer {#hide}
Cache ou isole des parties de l'objet.

Les modes principaux se choisissent dans le menu de gauche :

* `Point` - Peignez sur l'objet pour en cacher des parties.
* Formes - Cachez avec des formes plutôt qu'au pinceau, via `Lasso`, `Polygone`, `Ligne`, `Rect` et `Ellipse`. Voir [Commandes de sélection](#selection-controls) pour plus d'informations.
* `Afficher` - Le sous-mode inverse l'opération : le mode choisi affiche des parties de l'objet au lieu de les cacher.

Une barre d'outils apparaît en haut de la vue 3d avec des commandes supplémentaires :

* `Tout effacer` - Rétablit les objets : toutes les parties cachées sont réaffichées. Quand d'autres objets ont aussi des parties cachées, un bouton `Effacer` supplémentaire ne rétablit que les objets sélectionnés.
* `Inverser` - Échange les parties cachées et visibles.
* `Supprimer` - Supprime la partie cachée de l'objet.
* `Scinder` - Sépare la partie cachée de l'objet dans une nouvelle forme.
* `Devant` / `Visible` / `Connectée` - Les mêmes filtres de trait que dans la barre d'outils de [Masque](#mask).
* `Au toucher` (groupe de faces) - Utilise les groupes de faces pour cacher rapidement des parties : toucher un groupe de faces cache le groupe entier.
* `Au toucher` (masque) - Si un masque est actif, un appui cache la partie masquée.

### ![](/icons/tool_measure.webp) Mesurer {#measure}
Faites glisser pour mesurer la distance entre 2 points. Une fois la mesure placée, vous pouvez faire glisser ses extrémités pour l'ajuster.

La barre d'outils de gauche choisit comment la distance est mesurée :

* `Ligne` - Une ligne droite entre les deux points.
* `Surface` - La distance le long de la surface, en suivant la coupe passant par les deux points, vue depuis la caméra.
* `Coupe` - Le périmètre de la section passant par les deux points, comme un mètre ruban autour d'un bras.
* `Sommet` - Accroche les extrémités au sommet le plus proche.
* `Nombre d'or` - Affiche un point jaune à l'emplacement du nombre d'or sur la mesure.
* Le bouton `?` affiche le volume, l'aire de la surface et la taille des objets sélectionnés.

### ![](/icons/tool_arrange.webp) Disposer {#arrange}
Alignez et disposez plusieurs objets à la fois, comme avec les outils d'alignement d'une application de design 2d. Sélectionnez d'abord les objets ; avec un seul objet, Disposer agit plutôt sur ses parties séparées. Un cadre est dessiné autour de la sélection : faites glisser ses poignées pour la mettre à l'échelle.

Une barre d'outils en haut de la vue 3d contient les commandes :

* `Global` / `Écran` - Dispose selon les axes du monde, ou selon l'écran (gauche, droite, haut, bas).
* `Aligner` - Aligne les objets sur leur minimum, leur centre ou leur maximum, sur chaque axe.
* `Répartir` - Espace régulièrement les objets entre les deux objets extérieurs, selon leur minimum, leur centre ou leur maximum. Il faut au moins 3 objets.
* `Ligne` - Range les objets en ligne le long d'un axe.
* `Grille` - Range les objets en grille, avec un nombre d'objets sur `X`, `Y` et `Z`.
* `Cercle` - (Global uniquement) Range les objets en cercle autour de l'axe `X`, `Y` ou `Z`.
* `Sphère` - (Global uniquement) Répartit les objets sur une sphère.

`Ligne`, `Grille`, `Cercle` et `Sphère` ont tous un curseur `Espacement` pour l'écart entre les objets.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Cet outil convertit l'objet sélectionné en une topologie propre faite de quads, avec des réglages de densité, de flux des arêtes et de symétrie.

::: tip
Quad Remesher est développé par [Exoside](https://exoside.com/) pour iOS et ordinateur.

Sur iOS, c'est un achat intégré dans Nomad, payable une seule fois : 16 $ US.

Sur ordinateur, achetez une licence auprès d'[Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Vous pouvez l'acheter pour Nomad sur ordinateur uniquement, ou prendre une licence croisée pour toutes les applications de bureau prises en charge.

Si vous possédez déjà Quad Remesher pour une autre application de bureau, vous pouvez [acheter une mise à niveau vers toutes les plateformes à moindre coût.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher n'est pas disponible sur Android. Sur Android, vous pouvez utiliser les remailleurs libres et gratuits de l'onglet [Remaillage en quads](topology.md#quad-remesh) de la topologie (AutoRemesher, Instant Mesh, QuadriFlow), mais leurs fonctionnalités sont plus limitées.
:::

Tant que Quad Remesher n'est pas débloqué, la barre d'outils du haut commence par un bouton panier à la place des boutons de remaillage. Sur iOS, il ouvre l'achat intégré. Sur ordinateur, il affiche `Débloquer (acheter, restaurer, essai)`, qui vérifie votre licence Exoside (ou lance l'essai). Une fois l'outil actif, les barres d'outils de gauche et du haut sont disponibles.

* `Point` - Ce pinceau règle la densité cible. Une intensité de 100 % peint en rouge : ces zones utiliseront deux fois la densité de quads cible. Une intensité de 0 % peint en cyan : ces zones utiliseront la moitié de la densité de quads cible. Une intensité de 50 % peint en gris : ces zones utiliseront la densité de quads cible par défaut.
* `Lisser` - Adoucit les transitions de densité rouge/gris/cyan.
* `Estomper` - Estompe la peinture de densité.
* `Courbe` - Esquissez des courbes sur la surface de la sculpture ; le Quad Remesher s'en sert comme guides pour le flux des arêtes. Touchez une courbe pour la supprimer.
* `Tracé` - Dessinez des tracés sur la surface de la sculpture ; le Quad Remesher s'en sert comme guides pour le flux des arêtes. Touchez un tracé pour le supprimer.
* `Rect` - Dessinez des rectangles sur la surface de la sculpture ; le Quad Remesher s'en sert comme guides pour le flux des arêtes. Touchez un tracé pour le supprimer.
* `Ellipse` - Dessinez des ellipses sur la surface de la sculpture ; le Quad Remesher s'en sert comme guides pour le flux des arêtes. Touchez un tracé pour le supprimer.

#### Barre d'outils du haut du Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Une barre d'outils apparaît en haut de la vue 3d avec des commandes supplémentaires :


* `<Count>` - Touchez ce bouton pour lancer le remaillage en quads ; le nombre indique le nombre de quads visé.
* `Quads` - Réglez le nombre de quads cible en glissant vers la gauche ou la droite, ou touchez pour saisir un nombre exact. Ce nombre est une indication plutôt qu'une valeur fixe : avec les différents réglages du Quad Remesher, le résultat ne correspond souvent pas exactement à cette cible.
* `Moitié` - Un raccourci qui règle la cible sur la moitié du nombre actuel de polygones.
* `Identique` - Un raccourci qui règle la cible sur le nombre actuel de polygones.
* `Guides` - Utilise ou ignore les guides. Quand il y a des guides, un second bouton `Guides` affiche leur nombre ; touchez-le pour tous les supprimer.
* `Densité` - Utilise ou ignore la peinture de densité. Quand il y a de la peinture de densité, un second bouton `Densité` la supprime.
* `Groupe de faces` - Utilise ou ignore les groupes de faces pour orienter le Quad Remesher.
* `Relâcher` - Relâche automatiquement les bordures des groupes de faces pendant le remaillage. Si vous avez déjà relâché ou lissé vos bordures de groupes de faces, désactivez cette option.
* `Relâcher (curseur)` - Un curseur raccourci pour relâcher les bordures des groupes de faces.
* `Arêtes dures` - Essaie de conserver les arêtes dures.
* `Reprojeter le sommet` - Reprojette la nouvelle topologie sur le maillage d'origine.
* `Sym` - Active un résultat symétrique. Notez que la symétrie est toujours calculée autour de l'axe X du monde : placez votre modèle à l'origine si vous attendez un résultat symétrique.
* `...` - Fenêtre des réglages du Quad Remesher.

#### Menu des réglages du Quad Remesher {#quad-remesher-settings-menu}

Le bouton `...` au bout de la barre d'outils du haut ouvre une fenêtre avec les réglages restants :

* `Nombre de quads adaptatif` - Utilise des quads plus petits dans les zones très courbées, et plus grands dans les zones peu courbées.
* `Taille adaptative` - Règle le degré d'adaptation. À 100 %, l'adaptation de la taille est maximale ; à 0 %, les quads sont uniformes.

::: tip

Une recette pour obtenir un bon remaillage en quads avec un minimum de défauts :

* Créez des groupes de faces sur le maillage pour définir le flux de quads idéal.
* Relâchez les groupes de faces pour obtenir des bordures lisses.
* Décimez. Cela garantit qu'il n'y a pas de faces fines ou déformées le long des bordures des groupes de faces. Dans les réglages de Décimer, vérifiez que l'option groupe de faces est activée : les arêtes des triangles suivront alors précisément les bordures de vos groupes de faces.

Dans les options du remaillage en quads, vérifiez que Relâcher est désactivé (puisque vous avez déjà relâché le maillage) : vous devriez obtenir de bons résultats.

:::

### ![](/icons/tool_select.webp) Sélectionner {#select}
Utilisez les modes de forme (`Lasso`, `Rect`, `Ellipse`) pour sélectionner des objets dans la scène. `Désélectionner` retire des objets de la sélection.

### ![](/icons/tool_lattice.webp) Treillis {#lattice}
Déformez un objet avec une cage de points de contrôle qui l'entoure, plutôt qu'en sculptant sa surface. Déplacer quelques points de la cage plie, tord ou étire tout l'objet en douceur : idéal pour ajuster les proportions ou poser un personnage sans toucher à la topologie. La déformation reste modifiable tant que vous ne l'avez pas validée.

La barre d'outils de gauche choisit comment vous modifiez la cage :

* `Points` - Faites glisser directement les points et les arêtes de la cage. Touchez un point pour le sélectionner.
* `Vue` - Déplace la caméra sans modifier la cage.
* `Relâcher` - Un pinceau qui relâche les points de la cage situés dessous.
* `Élastique` - Un pinceau qui tire les points de la cage avec une atténuation élastique, comme l'outil [Élastique](#elastic).
* `Gizmo` - Déplacez, faites pivoter et mettez à l'échelle les points sélectionnés avec le gizmo. Son sous-mode est `Pivot`.
* `Lasso` - Sélectionnez des points de la cage au lasso ; `Désélectionner` les retire de la sélection.

La fenêtre des formes contient aussi `Rayon doux`, qui fait suivre les points voisins quand vous déplacez des points (en cellules de la grille ; à 0, seule la sélection bouge), et `Inverser la sélection`.

Une barre d'outils en haut de la vue 3d contient :

* `Valider` - Applique la déformation à l'objet et retire la cage.
* `Réinitialiser` - Retire la cage et sa déformation.
* `Opacité` - L'opacité d'affichage de la cage.
* `Côté miroir` - Avec la symétrie, fait alterner le côté miroir de la cage qui est affiché et sélectionnable, avec sa propre `Opacité` pour le côté caché.
* `Points de la grille` - Les points de la cage qui peuvent être déplacés : toute la grille, la surface et le point central, ou la surface seule.
* `Rigidité` - La raideur de la déformation, de lisse (0 %) à rigide et linéaire (100 %).
* `Atténuation` - Jusqu'où la déformation s'estompe en dehors de la cage.
* `Aligner` - Aligne la cage sur l'objet, ou sur le monde.
* `X`, `Y`, `Z` `Division` - Le nombre de cellules de la cage sur chaque axe. Le bouton de mode à côté règle leur relation : `x = y = z` utilise le même nombre sur les 3 axes, `Uniforme` garde le même espacement entre les points sur tous les axes, et `Personnalisé` vous laisse régler chaque axe librement.

#### Réglages du Treillis {#lattice-settings}
* `Vitesse de roulis` - Les mêmes options de roulis que l'outil [Déplacer](#move-settings), utilisées quand vous faites glisser des points de la cage.

### ![](/icons/tool_view.webp) Vue {#view}
Cet « outil » ne fait rien de particulier : c'est simplement un moyen de regarder le modèle sans modifier votre scène.

#### Réglages de Vue {#view-settings}
Tant que l'outil Vue est actif, ces réglages remplacent certaines options d'affichage, pour obtenir une vue épurée afin de présenter ou de vérifier votre modèle :

* `Primitive (Modifier)`, `Répéteur (Modifier)`, `Lumière (Modifier)`, `Caméra (Modifier)` - Permettent de modifier les primitives, les répéteurs, les lumières et les caméras dans la vue 3d avec l'outil Vue. Désactivez-les pour éviter de déplacer leurs poignées par accident.
* `Raccourci caméra (toujours)` - Affiche toujours les boutons de raccourci caméra dans la vue 3d.
* `Afficher le masque`, `Contour`, `Assombrir les objets non sélectionnés` - Affiche le masque, le contour des objets sélectionnés, ou assombrit les objets non sélectionnés. `Auto` suit votre réglage habituel, `Non` et `Oui` le forcent.
* `Afficher la ligne (Symétrie)`, `Afficher le plan (Symétrie)` - Affiche la ligne ou le plan de symétrie, avec les mêmes choix `Auto`, `Non` et `Oui`.
* `Icône` - Affiche les icônes des groupes, répéteurs, lumières, caméras et de la hiérarchie dans la vue 3d, avec les mêmes choix.


## Menu contextuel de la boîte à outils {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Un clic droit ou un appui long sur un outil de la boîte à outils ouvre un menu contextuel, avec les options suivantes :

* `Enregistrer` - Enregistre les modifications apportées à l'outil.
* `Cloner` - Duplique l'outil dans un nouveau raccourci d'outil.
* `Dernier enregistrement` - Revient à la dernière version enregistrée de l'outil.
* `Icône` - Change l'icône de l'outil. Quand l'outil a une icône personnalisée, ce bouton la retire.
* `→ ...` - Déplace l'outil dans un autre dossier de la boîte à outils, ou dans un nouveau.
* `Réinitialiser` - Rétablit les réglages par défaut de l'outil.

Les outils clonés ont aussi `Renommer` et `Supprimer`.
