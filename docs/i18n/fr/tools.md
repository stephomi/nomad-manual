# ![](/icons/toolbox.webp) Outils

![](/images/tools_menu.webp)

::: tip
Allez directement à [Outils](#tools-1) pour les descriptions de chaque outil.
:::

## Vue d’ensemble

Les outils sont sélectionnés dans la `Boîte à outils` à droite, et contrôlés avec les `Contrôles d’outil` à gauche. Des réglages supplémentaires se trouvent dans le menu `Settings`, la première icône dans le menu en haut à droite.

Les outils de brosse ont des contrôles pour la taille et l’intensité. Les outils de sélection ont des contrôles pour plusieurs styles de sélection. En bas des contrôles d’outil se trouvent des raccourcis pour les opérations fréquemment utilisées (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Les outils de Nomad sont codés par couleur dans la boîte à outils :

* <span class=brush>**Outils de brosse**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Outils de déplacement**</span> (Move, Drag)
* <span class=mask>**Outils de masque**</span> (Mask, SelMask)
* <span class=paint>**Outils de peinture**</span> (Paint, Smudge)
* <span class=flatten>**Outils d’aplatissement**</span> (Flatten, Planar)
* <span class=pinch>**Outils de pincement**</span> (Crease, Pinch)
* <span class=selection>**Outils basés sur la sélection**</span> où un masque 2D est d’abord dessiné, puis une opération est appliquée (Trim, Split, Project)
* <span class=creation>**Outils de création**</span> (Tube, Lathe, Insert)
* <span class=transform>**Outils de transformation**</span> (Transform, Gizmo)
* <span class=misc>**Outils divers**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Outil de vue**</span>



Beaucoup de ces outils peuvent être personnalisés avec différents comportements de brosse, pression, textures, etc. via le menu [Stroke](stroke.md). 


### Contrôles de brosse

La barre d’outils de gauche comporte des curseurs pour le rayon et l’intensité, puis des contrôles spécifiques à la catégorie d’outil, expliqués ci‑dessous.

![](/images/tool_left_panel.webp)

::: tip
Le curseur d’intensité pour de nombreux outils peut dépasser 100 %, cela vaut la peine d’expérimenter !
:::

### Sous‑mode
Le bouton directement sous le curseur d’intensité est le bouton `Sub`. Son libellé et sa fonction changent avec chaque outil, et lorsqu’il est pressé il invoque un comportement alternatif, généralement opposé. Par exemple pour [Paint](#paint) il active un mode Gomme, pour [Crease](#crease) il crée des arêtes en relief plutôt que des creux, etc.

Par défaut il fonctionne comme un bouton « collant » : c’est‑à‑dire que vous pouvez le maintenir enfoncé pour l’activer temporairement, et lorsque vous relâchez il se désactive. Si vous tapez dessus, le sous‑mode sera activé de façon permanente.

### Raccourcis
En bas de la barre d’outils de gauche se trouvent des raccourcis pour [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Par défaut ils fonctionnent tous comme des boutons « collants » : vous pouvez les maintenir enfoncés pour les activer temporairement, et lorsque vous relâchez ils se désactivent. Si vous tapez dessus, ce mode de raccourci sera activé de façon permanente.

### Contrôles de sélection

Les outils [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) et [Hide](#hide) utilisent tous des contrôles similaires pour sélectionner des zones du maillage.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Une forme dessinée à main levée
* `Polygon` - Une forme fermée définie par une combinaison de courbes et/ou de lignes droites. Voir [Édition de forme](#shape-editing) ci‑dessous pour plus d’informations.
* `Curve` - (Project uniquement) - Une courbe dessinée à main levée pour la projection
* `Path` - (Project uniquement) - Une courbe définie par des points. Voir [Édition de forme](#shape-editing) ci‑dessous pour plus d’informations.
* `Line` - Faites glisser une ligne pour définir un segment planaire. Par défaut, elle agit immédiatement sur le maillage ; désactivez l’auto‑validation si vous ne voulez pas cela (appui long ou balayage sur l’icône de ligne)
* `Rect` -  Faites glisser une ligne diagonale, cela définira les coins d’un rectangle. Appui long ou balayage pour afficher les options d’auto‑validation, de forçage en carré, et pour que le premier clic soit le centre du rectangle.
* `Ellipse` - Faites glisser une ligne diagonale, cela définira la taille d’une ellipse. Appui long ou balayage pour afficher les options d’auto‑validation, de forçage en cercle, et pour que le premier clic soit le centre de l’ellipse.
* `Flip` - Inverser le masque de forme, ou la direction de l’outil Project.

La plupart des outils ont une option d’auto‑validation, ce qui signifie que l’opération se produira dès que vous aurez fini de dessiner la forme. Lorsque l’auto‑validation est désactivée, un bouton vert est dessiné à côté de la forme et exécutera l’opération. Cela vous permet de modifier la forme, d’ajuster la vue, puis, lorsque vous êtes prêt à utiliser la forme, d’appuyer sur le bouton vert.

### Édition de forme
L’édition de polygone et l’édition de courbe se comportent de manière similaire :

* Pour commencer, faites glisser une ligne pour définir 2 points, puis faites glisser depuis le milieu de la ligne pour définir un polygone ou une courbe.
* Cliquez sur les points pour basculer entre lisse et anguleux. 
* Cliquez‑glissez sur les sections de courbe ou de ligne pour créer de nouveaux points.
* Pour supprimer un point, faites‑le glisser dans son voisin jusqu’à ce qu’il devienne rouge.
* L’icône de corbeille dans le coin de l’icône de polygone ou de chemin supprimera la forme.

### Menu Settings

De nombreux outils ont des réglages supplémentaires qui se trouvent dans le menu Settings, la première icône dans le menu en haut à droite :

![](/images/tools_settings_menu.webp)

## Outils

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
L’outil Clay est utile pour construire votre sculpture. `Sub` enlèvera de la matière de votre sculpture.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
La brosse standard. `Sub` enlèvera de la matière.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
La zone sous la brosse collera à la brosse, permettant une déformation élastique. La sélection est conservée pendant le déplacement, donc si vous éloignez la brosse puis la ramenez à son point de départ, vous ne verrez aucune déformation.

Le sous‑mode est `Normal`, et déplacera la zone sous la brosse le long de la normale de surface.

Cette brosse est adaptée à la fois aux déformations à grande échelle et aux petites déformations précises.

#### Réglages de Move

* `Radius (Background)` - À quelle distance du bord d’un modèle vous pouvez être tout en sculptant, utile lorsque vous travaillez sur la silhouette d’un objet. 
* `Same-side vertex only` - Ignorer les sommets qui pointent dans la direction opposée à la déformation.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
La zone sous la brosse collera à la brosse, permettant une déformation élastique. Contrairement à la brosse Move, la sélection est continuellement mise à jour pendant le trait, il est donc possible de créer des objets longs et serpentins, en particulier lorsque la topologie dynamique est activée.

Le sous‑mode est `Normal`, et déplacera la zone sous la brosse le long de la normale de surface.

Cette brosse est adaptée aux modifications de forme plus libres et gestuelles.

#### Réglages de Drag

* `Radius (Background)` - À quelle distance du bord d’un modèle vous pouvez être tout en sculptant, utile lorsque vous travaillez sur la silhouette d’un objet. 
* `Same-side vertex only` - Ignorer les sommets qui pointent dans la direction opposée à la déformation.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
Lisse la zone en moyennant les positions des points. Cet outil dépend fortement de la densité de polygones.
Ainsi, si vous avez beaucoup de polygones, le lissage sera moins efficace.

Le sous‑mode est `Relax`, qui ne lisse que le maillage (wireframe) mais essaie de conserver les détails géométriques.

#### Réglages de Smooth

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - Lissera les bords des facegroups. Utilisez une intensité supérieure à 100 % pour lisser rapidement les bords. `Auto` ne lissera que si l’aperçu des facegroups est activé, `Off` désactivera, `On` activera. 

##### Vertex
* `Sticky vertex on border` - Pour les maillages avec des bords ouverts, par ex. un plan, il est possible de lisser les coins. Activer cette option verrouillera les bords ouverts.
* `Relax` - identique au mode alternatif Relax dans la barre d’outils de gauche.
* `Stable smoothing` - Essaie de rendre le lissage indépendant de la topologie. Cela fonctionne mieux avec une densité de topologie variable et une valeur d’intensité de lissage élevée.

##### Painting
* `Screen Smoothing` - Utilisez cette option pour obtenir un lissage indépendant de la topologie, même à des nombres de polygones élevés.
* `Screen samples` - La qualité du lissage, des valeurs plus élevées seront plus lisses mais plus lentes.

::: tip
Des densités de polygones plus élevées peuvent nécessiter de pousser l’intensité au‑delà de 100 %. Des valeurs très élevées (300 %, 500 %) peuvent aussi bien fonctionner comme outil de sculpture, forçant les zones à devenir plates et lisses rapidement sous la brosse, comme frapper de l’argile avec un maillet !
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
Cet outil vous permet de masquer des sommets. Les sommets masqués sont protégés de la sculpture ou de la peinture. 

Le sous‑mode est `Unmask`, et effacera là où le masque a été peint.

Comme les sélections dans les logiciels de peinture 2D, les masques peuvent être peints avec une brosse, ou créés avec des sélections de forme, floutés ou accentués. 

Contrairement aux logiciels 2D, ils peuvent aussi être créés via des facegroups, et les masques peuvent être utilisés pour créer de la nouvelle géométrie via des opérations de type extrusion/extraction. 

![](/videos/tool_mask1.mp4)

 Une barre d’outils apparaîtra en haut de la vue avec des contrôles supplémentaires. 

![](/images/tool_mask_toolbar.webp)

Le titre de la barre peut être tapé pour l’agrandir/la réduire, ou la flèche en haut à droite peut être tapée pour la déplacer en haut ou en bas de l’interface.

| Action                                             | Description                                                                                 |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| ![](/icons/cross_circle2.webp) Clear              | Effacer le masque                                                                           |
| ![](/icons/invert.webp)        Invert             | Inverser le masque                                                                          |
| ![](/icons/sharpen.webp)       Sharpen            | Accentuer le bord du masque                                                                 |
| ![](/icons/blur.webp)          Blur               | Flouter le bord du masque                                                                   |
|                                 Blur ->            | Glisser gauche/droite pour flouter le masque de manière interactive                        |
| ![](/icons/culling.webp)       Front              | Basculer pour ne masquer que les sommets faisant face à la caméra                          |
|                                 Convert            | Convertir le masque en facegroup                                                            |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Quand activé, les facegroups seront affichés, taper sur un facegroup le masquera           |
|                                 On tap (mask)      | Quand activé, taper sur une « île » masquée ou non masquée remplira cette île par diffusion |
| ![](/icons/vertex.webp)        Connected          | Quand activé, seules les parties topologiquement connectées seront affectées par le masque |

##### Geste rapide Mask
Vous pouvez effectuer des gestes à la ZBrush en maintenant le bouton de masquage rapide dans la barre de gauche :
| Action  | Geste (maintenir le raccourci en bas à gauche) |
| :-----: | :---------------------------------------------: |
| Invert  | Taper sur l’arrière‑plan                        |
| Clear   | Glisser sur l’arrière‑plan                      |
| Blur    | Taper sur une zone masquée                      |
| Sharpen | Taper sur une zone non masquée                  |


#### Réglages de Mask
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Le menu des réglages de Mask est principalement utilisé pour créer de la géométrie à partir du masque. Pour cette raison, le comportement par défaut est de prévisualiser à quoi ressemblera la nouvelle géométrie. Vous pouvez choisir de ne pas avoir d’aperçu, un aperçu Extract, un aperçu Split, et si cette géométrie sera affichée en mode rayons X.

##### Thickness
* `Height` - La hauteur de la forme extraite. L’icône Plus/Moins vous permet d’alterner entre une extrusion vers l’extérieur, vers l’intérieur, ou centrée. 
* `Height/Height+Mask` - Basculer entre une hauteur constante, ou laisser les parties floutées du masque affecter la hauteur, ce qui permet des formes douces et de hauteur variable. 

##### Smoothness
Lorsqu’il est actif, lisse le bord de la forme extraite, cela fonctionne mieux avec des nombres de polygones élevés. 
* `Iterations` - La quantité de lissage appliquée. Des valeurs élevées produiront des bords très lisses et courbes, mais s’éloigneront de la forme du masque.
* `All/Sharp border/Borders only` - Le lissage peut agir dans toutes les directions, lissant à la fois les côtés et le dessus de la forme extraite, ou lisser le dessus et les côtés mais conserver un bord net, ou ne lisser que le bord, en laissant la surface supérieure intacte.

##### Edge loop (side)
* `Auto Edge-loop (side)` - Calculera le nombre de divisions sur les côtés de la forme extraite pour obtenir des polygones carrés qui correspondent aux polygones de la zone masquée. Lorsque désactivé, vous pouvez définir vous‑même le nombre de boucles d’arêtes avec le curseur Edge loop.

----

##### Extract
* `Extract` - Créer la géométrie extraite.
* `Closing action` - Comment Extract doit se comporter. « None » dupliquera les polygones masqués dans une nouvelle forme. « Fill » fera la même chose et tentera de refermer la surface arrière. « Shell » extrudera selon la valeur définie dans « thickness », et est le mode par défaut.

::: tip

Si l’aperçu est en mode « Extract » avec « X-ray » activé, cliquer sur le bouton Extract peut être déroutant au début. Comme le menu est actif, il essaiera de prévisualiser une extraction sur votre nouvelle forme, et de passer l’original en rayons X. Cependant, comme vous n’avez pas de masque sur la nouvelle surface, il ne peut pas prévisualiser l’extraction, et Nomad vous avertira « Nothing to Extract! ». 

C’est normal, fermez le menu des réglages de Mask pour voir la nouvelle forme et l’original, et sélectionnez à nouveau la surface originale si vous devez effacer le masque ou dessiner de nouveaux masques.
:::

##### Split
* `Split` - Extraira les régions masquées ET non masquées dans de nouvelles formes. 
* `Closing action (masked)` - Comment l’extraction de la zone masquée doit se comporter. « None » dupliquera les polygones masqués dans une nouvelle forme. « Fill » fera la même chose et tentera de refermer la surface arrière. « Shell » extrudera selon la valeur définie dans « thickness », et est le mode par défaut.
* `Closing action (unmasked)` - Comment l’extraction de la zone non masquée doit se comporter. « None » dupliquera les polygones masqués dans une nouvelle forme. « Fill » fera la même chose et tentera de refermer la surface arrière. « Shell » extrudera selon la valeur définie dans « thickness », et est le mode par défaut.
* `Sync border` - S’assurer que la bordure entre les formes extraites masquées et non masquées reste proche. Lorsque désactivé, comme l’opération Shell extrudera chaque face le long de sa normale, un espace peut se former entre les formes.

##### Carve
* `Carve` - En mode par défaut, se comporte comme si vous aviez découpé dans la surface de la valeur « thickness », comme couper une section d’écorce d’orange. 



### ![](/icons/tool_maskSelector.webp) Selection Mask
Cet outil est très similaire à l’outil [Mask](#mask), la principale différence étant que vous n’utilisez pas de trait pour peindre le masque, mais les [Contrôles de sélection](#selection-controls).

Le sous‑mode est `Unmask`, et effacera le masque en utilisant les contrôles de sélection.

Selection Mask partage les mêmes réglages d’outil que l’outil `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
Applique la couleur et les propriétés de matériau. Pour en savoir plus sur les matériaux, consultez la section [Painting](painting.md).

Le sous‑mode est `Erase` et supprimera la peinture.

#### Réglages de Paint
* `Layer fitering` - Fonctionne comme le verrouillage d’alpha de calque dans Photoshop ou Procreate. Si vous peignez sur un calque, lorsqu’il est activé, vous ne pouvez modifier que là où de la peinture existe déjà ; les zones non peintes seront protégées.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
Estompe la couleur et les propriétés de matériau. Le menu des réglages de Smudge contient un curseur `Quality`, des valeurs plus faibles signifient des traits plus rapides.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
Aplatis la zone en projetant les points sur le plan moyen.

Le sous‑mode est `Fill` et définira un plan basé sur le point le plus haut, et aura tendance à tirer les points vers le haut.

#### Réglages de Flatten

* `Lock plane direction` - Utiliser la direction du plan calculée au premier clic. Par défaut, ceci est désactivé.
* `Lock plane origin`- Utiliser le premier clic comme centre du plan. Par défaut, ceci est désactivé.

Lorsque l’un ou l’autre (ou les deux) est désactivé, Flatten peut être progressivement approfondi ou l’angle du plan modifié en utilisant de longs traits qui se déplacent sur différentes profondeurs et courbures. Ceci, en conjonction avec les options d’échantillonnage de zone du menu Brush, peut offrir un contrôle très précis.

::: tip
Lorsque vous travaillez dans des zones de forte courbure, par ex. essayer d’aplatir les joues mais l’outil affecte constamment les côtés du nez, essayez de créer un masque pour protéger les zones que la brosse Flatten ne doit pas affecter.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
Rend les points plans en les projetant sur le plan moyen, mais avec moins d’accumulation que la brosse Flatten. Cela crée des surfaces nettes plus propres. Des traits rapides pousseront et tireront davantage sur la surface, des traits plus lents qui commencent sur des zones déjà planes et s’étendent vers l’extérieur maintiendront mieux le plan.

Le sous‑mode est `Fill` et définira un plan basé sur le point le plus haut, et aura tendance à tirer les points vers le haut.

Planar est en fait le même outil que `Flatten`, mais avec `Lock plane direction` activé, ce qui signifie qu’il aura tendance à créer des surfaces plus stables et à arêtes vives, tandis que Flatten peut être plus sculptural et utilisé pour créer des zones semi‑plates.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Les outils Crease sont utiles pour sculpter de petites coupures ou entailles.

Le sous‑mode est `Invert`, et créera une arête en relief.

#### Réglages de Crease

* `Pinch factor` - À quel point tirer les sommets latéralement vers le trait. Si Pinch est à 1 et Offset à 0, la surface n’aura aucun changement de profondeur, seulement des changements de topologie, tirant les arêtes vers le trait.
* `Offset factor` - À quel point pousser/tirer les sommets en profondeur. Si Pinch est à 0 et Offset à 1, des creux profonds ou des bosses en relief seront créés, mais paraîtront irréguliers car pas assez de géométrie n’est tirée vers la crevasse pour définir correctement les côtés ou le fond.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
Cet outil peut être utilisé pour affûter les arêtes.

Le sous‑mode est `Invert` et écartera les sommets.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
L’outil Trim fonctionne en supprimant une partie de votre maillage, et propose des options pour traiter le vide laissé derrière. Il utilise les [Contrôles de sélection](#selection-controls) pour définir la découpe.

::: tip
Comme cet outil projette depuis la caméra, vous obtiendrez un avertissement si la caméra est en mode perspective.

En mode orthographique, la coupe effectuée à travers le maillage est parallèle à la vue, ce que les utilisateurs attendent généralement. En perspective, la coupe sera différente sur la face éloignée de l’objet par rapport à la face proche.
:::

#### Réglages de Trim

* `Stroke painting` - Si la peinture est activée dans le menu Paint, la zone refermée sera remplie avec la couleur actuellement sélectionnée.
* `Boolean` - Remplir le trou du Trim avec une région en quads. La région remplie sera plate.
* `Legacy` - Remplir le trou du Trim avec une région triangulée. La région remplie sera plate.
* `Fill` - Remplir le trou avec une région triangulée. La région remplie sera une surface courbe, comme le film d’une bulle de savon.
* `None` - Ne pas remplir le trou.
* `Boolean Detail Shape` - Taille approximative des quads et triangles utilisés sur le côté « forme » du Trim.
* `Boolean Detail Hole` - Taille approximative des triangles ou polygones utilisés sur le trou rempli du Trim. 
* `Legacy Detail` - Taille approximative des triangles utilisés sur le Trim.
* `Legacy Hole smoothing` - Degré de relaxation des triangles dans la zone remplie.
* `Legacy Threshold espilon` - Valeur pouvant être ajustée pour améliorer l’algorithme de remplissage Legacy.
* `Fill Detail` - Taille approximative des triangles utilisés sur le Trim.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
Similaire à l’outil [Trim](#trim), sauf que Trim supprime la sélection, tandis que Split conserve la sélection comme nouvel objet.

#### Réglages de Split

* `Stroke painting` - Si la peinture est activée dans le menu Paint, la zone refermée sera remplie avec la couleur actuellement sélectionnée.
* `Boolean` - Remplir le trou du Split avec une région en quads. Les régions remplies seront plates.
* `Legacy` - Remplir le trou du Split avec une région triangulée. Les régions remplies seront plates.
* `Fill` - Remplir les trous avec une région triangulée. Les régions remplies seront des surfaces courbes, comme le film d’une bulle de savon.
* `None` - Ne pas remplir les trous.
* `Boolean Detail Shape` - Taille approximative des quads et triangles utilisés sur le côté « forme » du Split.
* `Boolean Detail Hole` - Taille approximative des triangles ou polygones utilisés sur le trou rempli du Split. 
* `Legacy Detail` - Taille approximative des triangles utilisés sur le Split.
* `Legacy Hole smoothing` - Degré de relaxation des triangles dans la zone remplie.
* `Legacy Threshold espilon` - Valeur pouvant être ajustée pour améliorer l’algorithme de remplissage Legacy.
* `Fill Detail` - Taille approximative des triangles utilisés sur le Split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
L’outil Project ressemble à l’outil [Trim](#trim), mais il ne supprime ni ne crée de géométrie, il déplace simplement les sommets pour les conformer à la sélection.

![](/videos/tool_project.mp4)

::: tip
Si vous utilisez Project dans un calque, vous pouvez mélanger entre la forme originale et la forme projetée avec le curseur du calque.
:::

### ![](/icons/tool_layer.webp) Layer
Relève la surface, mais limite la hauteur.

Si vous gardez le stylet posé et continuez à brosser sur une zone, Layer montera jusqu’à une certaine hauteur puis n’ira pas plus loin, contrairement aux autres outils qui continueront à accumuler de la hauteur.

Notez que par défaut la limite n’est définie que par trait ! Si vous commencez un nouveau trait, il se construira à partir de la nouvelle hauteur de surface.

Pour définir une hauteur maximale constante sur plusieurs traits, utilisez l’outil Layer avec le système de [Layers](layers.md) de Nomad.

Créez un calque et utilisez cet outil. La hauteur maximale est maintenant définie par le calque, vous pouvez donc appliquer de nombreux traits de brosse et la hauteur sera toujours la même.

`Sub` utilisera une profondeur minimale, créant des rainures.

#### Réglages de Layer

* `Use layer data` - Lorsqu’il est actif, et lorsqu’un calque est sélectionné, utilise les données du calque pour définir la hauteur maximale.
* `Inflate`- Lorsqu’il est actif, ajuste la direction de travail de Layer pour obtenir des résultats plus lisses.
* `Relax (Normal)` - Quantité de lissage appliquée aux normales.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
Déplace les sommets le long de leurs propres normales. `Sub` déplacera les sommets le long de leur normale inversée.

#### Réglages d’Inflate
* `Relax (Normal)` - Quantité de lissage appliquée aux normales.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
Déplace ou « étale » les points dans la direction du trait.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

Cliquez‑glissez pour relever une zone de la sculpture selon la forme de l’Alpha sélectionné.

C’est simplement l’outil [Brush](#brush) avec un type de trait réglé sur `Lock + radius`. 

`Sub` enfoncera le stamp dans la surface plutôt que de le faire ressortir.

::: tip
Stamp fonctionne généralement mieux avec une géométrie de haute résolution. Si vous cherchez en ligne « wrinkles alpha », « pores alpha », « scales alpha », etc., ces textures d’alpha et Stamp peuvent être un excellent moyen d’ajouter des détails organiques à une sculpture de personnage.

Les deux modes de trait sont utiles pour des choses différentes. 

* `Lock + radius` a une *hauteur* fixe, le glisser ajuste la largeur et la rotation du stamp. Bon pour les textures de peau qui doivent avoir la même profondeur/hauteur, mais des rotations et échelles différentes pour masquer les motifs répétitifs.
* `Lock + intensity` a une *largeur* fixe, le glisser ajuste la rotation et la hauteur du stamp. Bon pour les rivets, qui doivent tous avoir la même taille, mais des rotations et hauteurs différentes. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
Cet outil peut réinitialiser les calques localement, vous avez besoin d’un calque actif sinon rien ne se produira.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
Créez un tube en dessinant une courbe. 
![](/images/tool_tube_new.webp)

Une fois le tube créé, le chemin peut être édité dans l’espace 3D en utilisant des contrôles similaires aux outils standard d’[Édition de forme](#shape-editing) et d’édition de courbe. 

![](/videos/tool_tube.mp4)

#### Barre de gauche de Tube

![](/images/tool_tube_left_toolbar.webp)

La barre de gauche comporte les options suivantes :

* `Sync` - Si le tube actuel est instancié et qu’il existe des nœuds enfants du tube qui diffèrent entre les instances, cela les resynchronisera.
* `Snap` - Lorsqu’il est actif, les modes Curve et Path s’accrocheront aux autres objets pendant le dessin. Lorsqu’il est inactif, le premier point s’accrochera, puis le reste du tube sera dessiné à cette profondeur. Il possède un petit menu déroulant :
    * `Offset` - Définit la profondeur du snap ; 0 % fera en sorte que le milieu de la section du tube s’accroche à la surface, des valeurs positives le soulèveront de la surface, des valeurs négatives l’enfonceront.
* `Curve` - Esquissez librement un tube. Il possède un petit menu déroulant :
    * `Auto-validate` - Créera le tube dès que le trait sera terminé. Lorsque désactivé, un cercle vert de validation sera visible à côté du chemin de la courbe, appuyez dessus pour valider, ou utilisez le lien `Reset` qui apparaît dans ce menu pour supprimer le chemin.
    * `Closed` - Fermer le tube en boucle.
    * `Screen` - Disponible uniquement lorsque Auto‑validate est désactivé. Lorsqu’il est actif, le chemin est « épinglé » à l’écran, ce qui vous permet de déplacer la vue et l’objet, le chemin restant en place. Lorsqu’il est inactif, le chemin fait partie de la scène 3D et se déplacera avec la caméra et les objets.
    * `Accuracy` - Nombre de points de courbe utilisés pour convertir le chemin dessiné en tube. 0 % utilisera le nombre minimal de points, mais manquera les petites variations de courbure. 100 % sera très précis et utilisera de nombreux points.
* `Path` - Créez un tube en cliquant pour définir des points de courbe. Tapez sur le cercle vert pour valider le chemin. Il possède un petit menu déroulant :
    * `B-spline` - Méthode alternative de dessin de courbe où les points de courbe ne se trouvent généralement pas directement sur la courbe, mais peuvent produire des résultats plus lisses que la méthode par défaut.
    * `Closed` - Fermer le tube en boucle
    * `Screen` - Lorsqu’il est actif, le chemin est « épinglé » à l’écran, ce qui vous permet de déplacer la vue et l’objet, le chemin restant en place. Lorsqu’il est inactif, le chemin fait partie de la scène 3D et se déplacera avec la caméra et les objets.

##### Barre supérieure de Tube
![](/images/tool_tube_toolbar.webp)
Lorsqu’un tube est sélectionné, une barre d’outils apparaît en haut de la vue avec des contrôles supplémentaires. Cliquez sur le titre de la barre pour la réduire/l’agrandir, et cliquez sur la flèche en haut à droite pour déplacer la barre en haut ou en bas de la vue.

* `Validate` - Convertir le tube en polygones réguliers pour qu’il puisse être sculpté.
* `Edit` - Afficher les points de courbe pour qu’ils puissent être manipulés
* `Mirror` - Ajouter un répéteur de miroir comme parent de cette courbe
* `Snap` - Accrocher les points de courbe aux surfaces proches
* `Closed` - Relier le début et la fin de la courbe pour former une boucle
* `B-spline` - Basculer entre les interpolations Catmull‑Rom et B‑spline.
* `Cap` - Alterner entre des bouchons aux deux extrémités du tube, seulement au début ou à la fin, ou aucun bouchon.
* `Hole` - Ajouter de l’épaisseur au tube, le transformant en tuyau. Alterner entre un trou aux deux extrémités, seulement à la fin, ou aucun trou. 
* `Radius` - Alterner entre un rayon uniforme, un rayon au début et à la fin, ou un rayon par point de courbe. Ceux‑ci sont édités avec des poignées orange sur la courbe.
* `Twist` - Alterner entre aucun twist, un twist uniforme, un twist au début et à la fin, ou un twist par point de courbe. Ceux‑ci sont édités avec des poignées roses sur la courbe.
* `Profile` - Alterner entre aucun profil (donc un profil circulaire), un profil uniforme, un profil au début et à la fin, ou un profil par point.
* `Profile edit` - Afficher un éditeur de profil. Il fonctionne de manière similaire aux outils d’[Édition de forme](#shape-editing), peut enregistrer et charger des préréglages de profil, et possède un interrupteur pour vous permettre d’éditer le profil dans l’espace 3D.
* `Spiral` - Afficher un menu pour ajouter une torsion en spirale au tube. Ce menu comporte des options pour `Twist Angle`, `Offset`, `Scale` et `Angle offset`.
* `X Divisions` - Nombre de divisions autour du tube, 4 divisions feront par exemple un tube carré. 
* `Constant density` - Lorsqu’il est actif, maintient les polygones carrés. Lorsqu’il est désactivé, permet de définir les `Y divisions` le long de la longueur du tube.
* `...` - Menu des réglages de Tube.

#### Bascule de suppression de point de courbe

![](/images/tool_tube_delete_toggle.webp)

Sous la barre d’outils se trouve un interrupteur de suppression de point de courbe. Lorsque vous faites glisser un point de courbe près d’un autre, il devient rouge, indiquant que si vous relâchez, le point sera supprimé. Si vous effectuez de petites modifications et ne souhaitez pas supprimer de points, ce bouton désactivera ce comportement.

#### Réglages de Tube
* `Primitive` - Boutons permettant d’activer/désactiver les UV, ou de valider le tube.
* `Post subdivision` - Raccourci pour définir le niveau de multirésolution avant validation.
* `Linear subdivision` - Raccourci pour définir le niveau de subdivision linéaire avant validation. 
* `Division X` - Identique à X Divisions dans la barre d’outils.
* `Division Y` - Identique à Y Divisions dans la barre d’outils.
* `Curve (Repeater)` - Convertir le tube en [Curve Repeater](scene.md#curve)

::: tip
Des Divisions à 4 et Post subdivision à 3 produiront des tubes à extrémités arrondies lisses, adaptés pour des vers, serpents, parties de corps.
:::


### ![](/icons/tool_lathe.webp) Lathe
Créez une surface de révolution en dessinant une courbe.

Cet outil est idéal pour des formes comme des vases, verres à vin.

![](/videos/tool_lathe.mp4)

#### Barre de gauche de Lathe

![](/images/tool_lathe_left_toolbar.webp)

La barre de gauche comporte les options suivantes :

* `Sync` - Si le Lathe actuel est instancié et qu’il existe des nœuds enfants du Lathe qui diffèrent entre les instances, cela les resynchronisera.
* `Fixed` - Lorsqu’il est activé, le centre du Lathe est fixe et affiché à l’écran. Cette ligne centrale possède des points d’édition qui peuvent être ajustés. Lorsqu’il est désactivé, le centre du Lathe sera mis à jour dynamiquement pour correspondre au début et à la fin de la courbe dessinée.
* `Curve` - Dessinez le profil du Lathe en un seul trait. Il possède un petit menu déroulant :
    * `Auto-validate` - Lorsqu’il est activé, le Lathe sera créé lorsque le stylet sera levé de l’écran. Lorsqu’il est désactivé, un cercle vert à côté de la courbe peut être pressé pour créer le Lathe. La courbe peut être supprimée avec le bouton `Reset`.
    * `Closed` - Relier le début et la fin de la courbe pour former une boucle
    * `Screen` - Disponible uniquement lorsque Auto‑validate est désactivé. Lorsqu’il est actif, le chemin est « épinglé » à l’écran, ce qui vous permet de déplacer la vue et l’objet, le chemin restant en place. Lorsqu’il est inactif, le chemin fait partie de la scène 3D et se déplacera avec la caméra et les objets.
    * `Accuracy` - Nombre de points de courbe utilisés pour convertir le chemin dessiné en tube. 0 % utilisera le nombre minimal de points, mais manquera les petites variations de courbure. 100 % sera très précis et utilisera de nombreux points.
* `Path` - Créez un Lathe en cliquant pour définir des points de courbe. Tapez sur le cercle vert pour valider le chemin. Il possède un petit menu déroulant :
    * `B-spline` - Méthode alternative de dessin de courbe où les points de courbe ne se trouvent généralement pas directement sur la courbe, mais peuvent produire des résultats plus lisses que la méthode par défaut.
    * `Closed` - Faire du tube une boucle
    * `Screen` - Lorsqu’il est actif, le chemin est « épinglé » à l’écran, ce qui vous permet de déplacer la vue et l’objet, le chemin restant en place. Lorsqu’il est inactif, le chemin fait partie de la scène 3D et se déplacera avec la caméra et les objets.

#### Barre supérieure de Lathe
![](/images/tool_lathe_top_toolbar.webp)

Lorsqu’un Lathe est sélectionné, une barre d’outils apparaît en haut de la vue avec des contrôles supplémentaires. Cliquez sur le titre de la barre pour la réduire/l’agrandir, et cliquez sur la flèche en haut à droite pour déplacer la barre en haut ou en bas de la vue.

* `Validate` - Convertir le Lathe en polygones réguliers pour qu’il puisse être sculpté.
* `Edit` - Afficher les points de courbe pour qu’ils puissent être manipulés
* `Mirror` - Ajouter un répéteur de miroir comme parent de ce Lathe
* `Snap` - Accrocher les points de courbe aux surfaces proches
* `Stable` - Lorsqu’il est activé, le profil de courbe sera parenté à la ligne centrale du Lathe. Lorsqu’il est désactivé, la ligne centrale peut être éditée sans déplacer la courbe, ce qui permet des formes plus complexes.
* `Focus` - Fera pivoter la vue pour voir le profil de courbe parfaitement à plat face à la caméra.
* `Closed` - Relier le début et la fin de la courbe pour former une boucle
* `Cap` - Si Closed est désactivé, alterner entre des bouchons aux deux extrémités du tube, seulement au début ou à la fin, ou aucun bouchon.
* `Hole` - Ajouter de l’épaisseur au Lathe, le transformant en tuyau. Alterner entre un trou aux deux extrémités, seulement à la fin, ou aucun trou. 
* `B-spline` - Basculer entre les interpolations Catmull‑Rom et B‑spline.
* `X Divisions` - Nombre de divisions autour du Lathe, 4 divisions feront par exemple un profil carré. 
* `Constant density` - Lorsqu’il est actif, maintient les polygones carrés. Lorsqu’il est désactivé, permet de définir les `Y divisions` le long de la longueur du tube.
* `...` - Menu des réglages de Lathe.

#### Réglages de Lathe
* `Primitive` - Boutons permettant d’activer/désactiver les UV, ou de valider le tube.
* `Post subdivision` - Raccourci pour définir le niveau de multirésolution avant validation.
* `Linear subdivision` - Raccourci pour définir le niveau de subdivision linéaire avant validation. 
* `Division X` - Identique à X Divisions dans la barre d’outils.
* `Division Y` - Identique à Y Divisions dans la barre d’outils.
* `Curve (Repeater)` - Convertir le profil de courbe en [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Insert
Place un objet sur la surface d’un autre. À l’usage, il est similaire à l’outil Stamp, mais pour des formes 3D complètes.

Si vous sélectionnez une primitive dans la barre de gauche, un clic‑glissé sur n’importe quelle surface placera une primitive à l’endroit du clic, le glisser définira la taille. Une fois le glisser terminé, Insert passera en mode [Transform](#transform).

En mode Instance, le glisser créera et fera glisser une nouvelle instance sur la surface. La taille sera dupliquée à partir de la première forme, de cette façon vous pouvez placer de nombreuses instances de même taille d’un objet sur d’autres surfaces.

Vous n’êtes pas obligé d’insérer uniquement des primitives ! Sélectionnez *n’importe* quelle forme dans l’outliner, si Insert est en mode Instance ou Clone, vous pouvez faire glisser des copies de l’objet sélectionné sur n’importe quelle autre surface.

Si un objet a un pivot personnalisé, il sera utilisé comme point d’ancrage. Voir la vidéo ci‑dessous.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
Déplace/Rotate/Scale un modèle directement avec 1 ou 2 doigts, généralement sur la surface d’un autre objet.

L’outil est contrôlé avec la barre de gauche, et possède 5 boutons :

* `Snap` - Accrocher le modèle aux autres surfaces
* `Group` - Si l’objet sélectionné est une combinaison d’objets et d’instances, cela permet de déterminer le comportement de l’outil.
* `Move` - Un glisser à un doigt déplacera l’objet. Lorsque Snap est actif, cela fera glisser l’objet le long de la surface sous votre doigt.
* `Rotate` - Un glisser à un doigt fera pivoter l’objet. Lorsque Snap est actif, la rotation se fera autour de la normale de la surface sous votre doigt.
* `Scale` - Un glisser à un doigt mettra l’objet à l’échelle.

Transform peut être utilisé pour exploiter rapidement 2 de ces modes en utilisant 2 doigts :

* Faites glisser un objet pour le placer. Arrêtez de bouger votre premier doigt, mais ne le levez pas de l’écran.
* Touchez l’écran avec votre deuxième doigt tout en gardant le premier doigt posé. Lorsque le deuxième doigt est glissé, l’objet sera mis à l’échelle.
* Levez le deuxième doigt, et continuez à glisser le premier doigt, l’objet sera à nouveau en mode Move.

Vous pouvez également changer le second mode avec un geste de tap à deux doigts :

* Faites glisser l’objet pour le placer, arrêtez de bouger, mais ne levez pas votre doigt de l’écran.
* Tapez avec votre deuxième doigt tout en maintenant le premier doigt posé
* L’outil est basculé en mode rotation. Faites glisser votre premier doigt pour régler la rotation.
* Tapez à nouveau avec le deuxième doigt, l’outil revient en mode Move.

Cela offre un flux de travail rapide pour cloner des objets sur un autre, par ex. des rochers sur un paysage. Notez que le bouton Clone se trouve également dans la barre de gauche pour un accès facile :

* Utilisez l’outil Transform pour placer un rocher.
* Relâchez, appuyez sur le bouton Clone
* Déplacez ce rocher, faites‑le pivoter/mettre à l’échelle selon les besoins
* Relâchez, appuyez sur le bouton Clone
* Déplacez ce rocher, répétez.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
Cet outil vous permet de déplacer, faire pivoter et mettre à l’échelle des objets, et de modifier les pivots des objets.

La poignée dans la vue possède les fonctionnalités suivantes :

* `Move` - Faites glisser sur la ligne+flèche pour déplacer sur X/Y/Z. Faites glisser sur le point pêche au centre du Gizmo pour une translation libre dans l’espace écran. Cliquez sur les carrés rouge, vert, bleu pour une translation sur les plans X/Y/Z.
* `Rotate` - Faites glisser sur les cercles rouge/vert/bleu pour une rotation sur X/Y/Z. Faites glisser la sphère à l’intérieur des cercles pour une rotation libre.
* `Scale`- Faites glisser sur les points extérieurs rouge/vert/bleu pour une mise à l’échelle sur X/Y/Z. Faites glisser sur les cônes extérieurs rouge/vert/bleu pour une mise à l’échelle sur les plans X/Y/Z. Faites glisser sur le cercle extérieur pêche pour une mise à l’échelle uniforme.

![](/images/tool_gizmo.webp)

#### Nœuds et sommets 

Chaque objet dans Nomad est composé d’un nœud et de sommets :

* `Node` - La « poignée » de l’objet, qui stocke sa translation, rotation, échelle, appelée matrice de transformation.
* `Vertices` - Les points qui définissent la surface d’un objet, ils stockent la position et les informations de peinture.

Si vous avez un simple cube composé de 8 sommets, vous pouvez le translater en modifiant sa matrice de transformation, ou en modifiant les positions des sommets. Lors de la sculpture, vous voulez généralement modifier les sommets, lors du déplacement d’objets avec le Gizmo, vous voulez généralement modifier le nœud. Nomad vous permet de faire les deux. 

#### Barre de gauche

La barre de gauche contrôle si le Gizmo agira sur le nœud ou les sommets, ainsi que d’autres fonctions :

* `Clone` - Faire une copie indépendante de l’objet courant, qui peut être déplacée avec le Gizmo.
* `Instance` - Faire une copie instanciée de l’objet courant. Les objets sont liés, donc les modifications de sculpture sur un objet apparaîtront sur tous les objets instanciés.
* `Group/Object/Vertex/Auto` - Définit si le Gizmo affectera le nœud ou les sommets d’un objet. Le mode par défaut « Auto » tentera de deviner au mieux. S’il y a plusieurs objets parentés ensemble dans une hiérarchie, « Object » ne déplacera que l’objet courant, les objets enfants resteront immobiles. Le Gizmo peut également tenir compte du masquage et de la symétrie.
* `Pin` - Par défaut, le Gizmo se déplacera vers le pivot de l’objet sélectionné. Lorsque Pin est activé, le Gizmo restera là où il se trouve actuellement.
* `Align` - Basculer entre un pivot aligné sur l’objet courant, ou aligné sur le monde.
* `Snap rotation` - Activer l’accrochage des valeurs de rotation à des incréments, la valeur de snap est affichée et peut être modifiée lorsque Snap est actif.
* `Snap translation` - Activer l’accrochage des valeurs de translation à des incréments, la valeur de snap est affichée et peut être modifiée lorsque Snap est actif.
* `Pivot` - Lorsqu’il est activé, le Gizmo peut être déplacé et pivoté sans déplacer l’objet. Il possède un menu supplémentaire expliqué ci‑dessous.

#### Pivot
Lorsque le mode Pivot est actif, un menu est affiché pour permettre des changements rapides de pivot :

**Reset** 
* `Center` - Déplacer le pivot au centre de l’objet
* `Bottom` - Déplacer le pivot au bas de l’objet
* `Align` - Réinitialiser les rotations pour les aligner sur le monde.
* `Mask` - Déplacer le pivot au centre de la région non masquée.

**On Tap**
* `None` - Ne rien faire lorsque l’objet est tapé
* `Normal` - Déplacer et faire pivoter le pivot pour l’aligner là où la surface est tapée
* `First` - Déplacer (mais ne pas faire pivoter) le pivot là où la surface est tapée
* `Medial` - Déplacer le pivot au milieu de l’objet, sous l’endroit où la surface est tapée.

#### Réglages de Gizmo

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - Déplacer l’objet pour que son pivot soit au centre de la scène, appelé l’origine.
* ![](/icons/bake.webp)  `Bake` - Figera l’objet là où il se trouve actuellement, et définira les valeurs de translation/rotation à 0, l’échelle à 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Faire correspondre les valeurs de matrice à la position réelle de la poignée du Gizmo dans le monde.
* ![](/icons/reset.webp) `Reset` - Raccourci qui définit les valeurs de translation à 0, de rotation à 0, d’échelle à 1, en déplaçant et faisant pivoter l’objet.

::: tip Bake vs bake to pivot
Créez un cube, sélectionnez l’outil Gizmo, ouvrez et épinglez le menu des réglages. Par défaut, la translation et la rotation sont à 0, l’échelle à 1.

Activez le mode Pivot, déplacez la poignée sur un côté, désactivez le mode Pivot. Le pivot a changé, mais notez que les valeurs de translation sont toujours à 0. 

Si vous voulez voir où se trouve *vraiment* le pivot, cliquez sur `Bake Pivot`. Les valeurs de translation se mettent maintenant à jour. Notez que le cube ne bouge pas pendant cette opération, ni en mode Pivot.

Déplacez et faites pivoter le cube quelque part, puis tapez sur `Move Origin`. Il déplace l’objet pour que son pivot soit au centre du monde, mais laisse la rotation inchangée.

Cliquez sur `Reset`, et la rotation sera également remise à 0.

Déplacez et faites pivoter le cube à nouveau, cette fois cliquez sur `Bake`. Le pivot reste où il est, le cube reste où il est, mais les valeurs de translation et de rotation sont mises à 0.

Entraînez‑vous quelques fois ! Comprenez que les valeurs de pivot sont cachées, Nomad s’en occupe pour vous, mais si vous devez définir le pivot à des emplacements réels dans l’espace, Bake Pivot le fera pour vous.

:::

* `Translation` - Les valeurs de translation X, Y, Z
* `Rotation` - Les valeurs de rotation X, Y, Z
* `Scale` - L’échelle uniforme si elle est activée, ou l’échelle X, Y, Z si elle est désactivée.
* `Uniform scale` - Basculer la possibilité de mettre à l’échelle uniformément ou indépendamment sur chaque axe

-----

* `Compact` - Basculer la disposition du Gizmo pour placer les poignées supplémentaires à l’extérieur ou à l’intérieur de la sphère de rotation
* `Widget size` - Taille du Gizmo
* `Thickness` - Épaisseur des lignes du Gizmo
* `Opacity` - Opacité du Gizmo
* `Hide on interaction` - Basculer si le Gizmo doit être temporairement masqué pendant le glisser

-----

* `Tangent roll threshold` - Contrôle le comportement de l’interface de rotation lors du glisser sur les cercles pour faire pivoter sur X/Y/Z. Si cette valeur est 0, la rotation fonctionne comme un cadran, faites glisser le Gizmo en cercles. Si cette valeur est 90, la rotation fonctionne comme tirer la ficelle d’un yo‑yo ; faites glisser en ligne droite vers ou loin de l’endroit où vous avez cliqué. Les valeurs entre 0 et 90 feront une combinaison des deux ; en dessous de la valeur ce sera le mouvement linéaire, au‑dessus ce sera le mouvement circulaire.
* `Numerical input` - Lorsqu’il est activé, un simple tap sur le Gizmo fera apparaître une fenêtre pour entrer une valeur exacte pour l’axe du widget tapé.

::: warning
Les outils [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) et [Scale](#scale) utilisent leur propre case à cocher de symétrie !

Par défaut, cette symétrie est désactivée.
:::

Sur la gauche, vous pouvez déplacer le pivot du Gizmo, vous pouvez voir la vidéo ci‑dessous en action.
Ceci est particulièrement utile pour la rotation, car cela ne change rien pour la translation.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

Les facegroups vous permettent d’organiser votre objet en faces de couleurs différentes. Vous pouvez utiliser ces groupes de nombreuses façons dans Nomad :

* Méthode de sélection rapide pour les masques
* Masquer/afficher des sections de votre objet
* Organiser votre objet sans avoir à le découper en parties séparées
* Définir des régions d’UV
* Guider le Quad Remesher
* Contrôle supplémentaire pour des outils comme Smooth.

#### Barre de gauche de Facegroup

* `Patch ` - Affiche les facegroups disponibles sous forme de patchs. Les patchs inutilisés peuvent être supprimés. Tapez sur un patch pour le renommer ou changer sa couleur. L’icône plus permet de créer de nouveaux patchs.
* `Dot` - Peignez sur l’objet pour définir des facegroups. Lorsque « + Face Group » est activé, chaque nouveau trait créera automatiquement un nouveau facegroup, utile pour définir rapidement des régions. Un tap remplira la région sélectionnée. Le curseur définit le rayon du point.
* `Relax` - Lisse les bords des facegroups. Très utile pour définir des arêtes propres pour le Quad Remeshing, ou pour définir des panneaux pour la modélisation hard‑surface. Les curseurs contrôlent le rayon et l’intensité de l’opération Relax.
* `Shape selector` - Créez des facegroups avec des formes plutôt qu’avec une brosse, via `Lock+Radius`, `Lasso`, `Polygon`, `Rect` et `Ellipse`. Voir [Shape Selector](#shape-selector) pour plus d’informations.
* `Auto-pick` - Lorsqu’il est activé, sélectionnera le patch là où le trait commence, et appliquera ce patch pour le reste du trait. Très utile pour nettoyer les régions de facegroup ; si un facegroup s’est étendu trop loin, activez Auto‑pick, commencez un trait là où le patch de facegroup est correct, et faites glisser jusqu’à la bordure pour réassigner le patch correct.

### ![](/icons/tool_hide.webp) Hide
Masquer ou isoler des parties de l’objet. 

Les modes principaux sont contrôlés depuis le menu de gauche :

* `Dot` - Brossez sur l’objet pour masquer des parties de l’objet.
* `Shape selector` -  Masquer avec des formes plutôt qu’avec une brosse, via `Lasso`, `Polygon`, `Line`, `Rect` et `Ellipse`. Voir [Shape Selector](#shape-selector) pour plus d’informations.
* `Show` - Inverser l’opération, de sorte que le mode sélectionné affiche au lieu de masquer des parties de l’objet.

Une barre d’outils apparaîtra en haut de la vue avec des contrôles supplémentaires :

* `Clear` - Restaurer l’objet, toutes les parties masquées seront réaffichées.
* `Invert` - Inverser les parties masquées et visibles.
* `Facegroup` - Utiliser les facegroups pour masquer rapidement des sections, taper sur un facegroup masquera tout le facegroup.
* `Mask` - Si un masque est actif, taper sur ce bouton masquera la section masquée.
* `Delete` - Supprimer la partie masquée de l’objet
* `Split` - Scinder la partie masquée de l’objet dans une nouvelle forme.

### ![](/icons/tool_measure.webp) Measure
Faites glisser pour mesurer la distance entre 2 points.

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

Cet outil convertira l’objet sélectionné en une topologie propre en quads, avec des contrôles pour la densité, le flux d’arêtes, la symétrie. 

::: tip
Quad Remesher est développé par [Exoside](https://exoside.com/) pour iOS et desktop. 

Pour iOS, c’est un achat intégré dans Nomad, un paiement unique de 16 USD.

Pour desktop, achetez une licence auprès de [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Vous pouvez l’acheter uniquement pour Nomad desktop, ou une licence croisée pour toutes les applications desktop prises en charge.

Si vous possédez déjà Quad Remesher pour une autre application desktop, vous pouvez [acheter une mise à niveau vers toutes les plateformes à moindre coût.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher n’est pas disponible pour Android.  Android peut utiliser le « Quad Remesh - Instant » gratuit et open source disponible sous le menu Topology -> Misc, mais comprenez que son ensemble de fonctionnalités est très limité.
:::

When this tool is activated for the first time, it will ask if you want to enable it as an in-app purchase. Once active, the left and top toolbars will be enabled.

* `Dot` - Ce pinceau définit la densité cible. Une intensité à 100 % peindra en rouge, ce qui utilisera deux fois la densité de quads cible dans ces zones. Une intensité à 0 % peindra en cyan, ce qui utilisera la moitié de la densité de quads cible dans ces zones. Une intensité à 50 % peindra en gris, ce qui utilisera la densité de quads cible par défaut.
* `Smooth` - Lisse les transitions de densité rouge/gris/cyan.
* `Curve` - Esquissez des courbes sur la surface du sculpt, Quad Remesher les utilisera comme guides pour le flux des arêtes. Touchez une courbe pour la supprimer.
* `Path` - Dessinez des chemins sur la surface du sculpt, Quad Remesher les utilisera comme guides pour le flux des arêtes. Touchez un chemin pour le supprimer. 
* `Rect` - Dessinez des rectangles sur la surface du sculpt, Quad Remesher les utilisera comme guides pour le flux des arêtes. Touchez un chemin pour le supprimer.
* `Ellipse` - Dessinez des ellipses sur la surface du sculpt, Quad Remesher les utilisera comme guides pour le flux des arêtes. Touchez un chemin pour le supprimer.

#### Quad remesher top toolbar
![](/images/tool_quadremesher_toolbar.webp)

A toolbar will appear at the top of the viewport with extra controls:


* `<Count>` - Cliquez ici pour lancer le processus de Quad Remesher, ce nombre indique le nombre cible de quads du remesh.
* `Quads` - Définissez le nombre cible de quads en faisant glisser vers la gauche ou la droite, ou touchez pour définir un nombre exact. Notez qu’il s’agit davantage d’un guide que d’un nombre fixe, les différents réglages de Quad Remesher font que le résultat ne correspondra pas toujours exactement à cette cible.
* `Half` - Raccourci pour définir le nombre cible à la moitié du nombre actuel de polygones.
* `Same` - Raccourci pour définir le nombre cible au nombre actuel de polygones.
* `Guides` - Indique le nombre total de guides, ou touchez pour supprimer tous les guides.
* `Density X` - Touchez pour supprimer toute la peinture de densité.
* `Density (painting)` - Bascule pour utiliser ou ignorer la peinture de densité.
* `Face Group` - Bascule pour utiliser ou ignorer les facegroups pour orienter Quad Remesher.
* `Relax` - Bascule pour détendre automatiquement les bordures de facegroups pendant le quad remeshing. Si vous avez déjà détendu/lissé les bordures de vos facegroups, désactivez cette option.
* `Relax Slider` - Curseur raccourci pour détendre les bordures de facegroups.
* `Hard Edges` - Bascule pour tenter de conserver les arêtes dures.
* `Reproject Vertex` - Bascule pour reprojeter la nouvelle topologie sur le maillage d’entrée.
* `Symmetry` - Bascule pour obtenir un résultat symétrique. Notez que la symétrie est toujours calculée autour de l’axe X du monde, assurez-vous donc que votre modèle est à l’origine si vous attendez un résultat symétrique.
* `...` - Menu des paramètres de Quad Remesher. 

#### Quad remesher settings menu

Most of these settings are available in the top toolbar.

* `<Count>, Half, Same` - Identiques aux boutons Remesh, Half, Same dans la barre d’outils supérieure.
* `Target Quads` - Identique au bouton `Quads` dans la barre d’outils supérieure.
* `Adaptive quad count` - Bascule pour utiliser des quads plus petits dans les zones à forte courbure, et des quads plus grands dans les zones à faible courbure.
* `Adaptive size` - Définit le niveau d’adaptativité. 100 % permet une taille adaptative maximale, à 0 % les quads seront uniformes.
* `Auto-Detect Hard Edges` - Bascule pour adapter la disposition du quad remesh afin de mieux suivre les surfaces nettes.
* `Density (painting)` - Identique au bouton `Density (painting)` dans la barre d’outils supérieure.
* `Reproject Vertex` - Bascule pour reprojeter la nouvelle topologie sur le maillage d’entrée.
* `Face Group` - Identique au bouton `Face Group` dans la barre d’outils supérieure.
* `Relax Slider` - Curseur raccourci pour détendre les bordures de facegroups.

::: tip

A recipie to get a good quad remesh with minimal artifacts:

* Créez des facegroups sur le maillage pour définir votre flux de quads idéal.
* Utilisez Facegroup Relax pour obtenir des bordures de facegroups lisses.
* Décimez. Cela garantit l’absence de faces fines ou déformées sur les bords de facegroups. Dans les paramètres de décimation, assurez-vous que Facegroup est activé. Cela fera suivre les arêtes de triangles précisément aux bords de vos facegroups. 

Dans les options de Quad Remesher, assurez-vous que Relax est désactivé (puisque vous avez déjà détendu le maillage) et vous devriez obtenir de bons résultats.

:::

### ![](/icons/tool_select.webp) Select
Utilisez les modes de forme pour sélectionner des objets dans la scène. `Unselect` supprimera des objets de la sélection.

### ![](/icons/tool_view.webp) View
Cet « outil » ne fait rien de particulier, c’est simplement un moyen de visualiser le modèle sans modifier votre scène.


## Toolbox context menu

![](/images/tools_context_menu.webp)

Un clic droit ou un appui long sur un outil dans la toolbox fera apparaître un menu contextuel. Ce menu propose les options suivantes :

* `Save` - Enregistrer les modifications apportées à l’outil
* `Clone` - Dupliquer l’outil dans un nouveau raccourci d’outil
* `Last save` - Revenir à la version précédemment enregistrée de l’outil
* `Icon` - Changer l’icône de l’outil
* `Reset` - Réinitialiser l’outil à ses valeurs par défaut
