# ![](/icons/pencil.webp) Trait    

---
![](/images/stroke_overview.webp) 

## Vue d’ensemble 

Vous pouvez personnaliser le comportement du trait pour la plupart des brosses d’outils.
Les réglages sont similaires à ceux présents dans les applications de peinture 2D, mais certaines options sont spécifiques à la sculpture et à la 3D.

Les options sont réparties dans 5 sous-menus :

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Contrôle la façon dont le trait est appliqué sur le modèle         |
| Alpha    | ![](/icons/alpha.webp)      | Comment une texture en niveaux de gris est utilisée pour l’empreinte de la brosse |
| Falloff  | ![](/icons/falloff.webp)    | Contrôle la façon dont la force de la brosse varie du centre vers le bord |
| Filter   | ![](/icons/filter.webp)     | Comment la brosse est affectée par la géométrie du modèle          |
| Pressure | ![](/icons/pressure.webp)   | Contrôle la réponse à la pression du stylet                        |

::: tip
Toutes les options de trait ne s’appliquent pas à tous les outils. Les options de trait qui ne sont pas utilisées par l’outil courant seront désactivées ou masquées. 
:::


## Stroke

### Radius

![](/images/stroke_radius.webp)

#### Share radius

Lorsque cette option est activée, tous les outils utilisent le même rayon ; par défaut, chaque outil possède son propre rayon.

#### Size

* Screen - le rayon est défini en unités écran. Si vous définissez le rayon à 100 pixels de large, il restera à 100 pixels quelle que soit la valeur du zoom.
* Constant (3d) - le rayon est défini en unités 3D. Par exemple, si vous créez une sphère et définissez le rayon à la même taille que la sphère, le rayon restera de la même taille que la sphère lorsque vous zoomez en avant ou en arrière.


### Stroke

![](/images/stroke_strokemode.webp)

Les traits peuvent fonctionner selon plusieurs modes :

### ![](/icons/stroke_dot.webp) Dot
Faites glisser comme un trait de peinture classique. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
L’alpha de la brosse sera tourné pour suivre la direction du trait, ce qui est utile pour créer des coutures de tissu. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
 Tamponne un trait de brosse avec une **_hauteur_** fixe. Le glisser-déposer définit l’échelle et la rotation.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Tamponne un trait de brosse avec un **_rayon_** fixe. Le glisser-déposer définit la hauteur et la rotation.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Les outils `Move` et `Drag` ont leurs propres 3 options :

### ![](/icons/snake.webp) Drag

Met continuellement à jour ce qui se trouve dans le rayon de la brosse pendant le trait. Un trait rapide laissera la surface derrière lui, tandis qu’un trait lent retiendra la matière, créant des formes plus longues. C’est le mode par défaut de l’outil `Drag`. Avec la `Dynamic Topology`, cela peut être utilisé pour créer des extrusions en forme de serpent. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Sélectionne ce qui se trouve dans le rayon de la brosse au début du trait, puis conserve cette sélection. C’est utile pour des opérations de déplacement plus précises, car vous pouvez ajuster soigneusement la distance du déplacement sans déplacer accidentellement plus que ce que vous aviez initialement sélectionné. C’est le mode par défaut de l’outil `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
Le rayon défini par l’utilisateur est ignoré et est défini dynamiquement en fonction de la distance à laquelle le trait est tiré à partir du point de départ. Petite distance = petit rayon, grande distance = grand rayon. Utilisez le curseur d’intensité pour contrôler la forme de l’atténuation. Utile pour bloquer des formes organiques et caoutchouteuses.
![](/videos/stroke_lockradius_drag.mp4) 



### Adjust spacing intensity
![](/images/stroke_space_smooth.webp)

Les traits avec un espacement faible (inférieur à 50 %) peuvent s’accumuler rapidement, produisant des traits plus intenses que des valeurs d’espacement plus élevées. Cette option compensera cela, de sorte que les traits auront approximativement la même intensité quel que soit l’espacement.

### Stroke spacing
Distance entre chaque application de la brosse lors d’un glisser-déposer. Des valeurs inférieures à 100 % se chevauchent, donnant l’apparence d’un trait continu. Des valeurs supérieures à 100 % commenceront à laisser des espaces, ce qui est utile pour sculpter des détails comme des coutures ou des fermetures éclair.

### Lazy rope stabilizer
Les traits seront en retard par rapport à la position du pointeur d’une certaine distance. Cela peut être utilisé pour dessiner des lignes lisses.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke smoothing
Moyenne plusieurs positions du pointeur pour obtenir un trait plus lisse.
Avec des valeurs élevées, le trait sera en retard par rapport au pointeur mais finira par le rattraper.
C’est utile pour dessiner des lignes lisses.

### Snap radius
Accroche le début du trait à la fin du trait précédent. Le rayon détermine à quelle distance chercher la fin du trait précédent. Cela peut être utile pour dessiner de longues lignes continues tout en faisant des pauses fréquentes.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Par défaut, les traits n’affectent que la surface du modèle à l’intérieur du rayon de la brosse. Lorsque la silhouette est activée, le trait est projeté à travers l’ensemble du modèle. Cela peut être très utile lors du blocage initial d’un modèle, ou pour des formes qui nécessitent que les côtés restent perpendiculaires.

La direction de projection peut être définie explicitement ; la méthode par défaut « Closest » détectera le meilleur angle par rapport à la vue. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

L’intensité, la translation, la rotation et l’échelle du trait peuvent chacune être randomisées. Cela peut être utilisé pour créer une variété d’effets ; par exemple, la randomisation avec l’outil de peinture peut créer une couleur mouchetée, ou la randomisation avec l’outil de pli peut être utilisée pour créer des détails de peau.

![](/videos/stroke_randomize.mp4) 

### Stroke Offset

Applique un décalage constant sur le trait. C’est utile pour les petits écrans où votre doigt couvrirait le trait. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

L’`Alpha` est une texture qui module le comportement de votre brosse.
C’est une image en niveaux de gris, où les pixels noirs signifient aucune déformation et les pixels blancs une déformation maximale.

Cliquez sur l’image alpha pour la changer.

Cliquez sur l’aperçu du matériau pour charger un alpha à partir d’un préréglage de matériau. Vous pouvez également enregistrer des préréglages de matériau ici, et choisir d’intégrer les textures avec l’outil.

::: tip
La texture n’est jamais redimensionnée, donc les grandes textures peuvent ralentir les performances.
:::

### Invert pixels
Inverse les valeurs de l’image : les pixels noirs deviennent blancs et les pixels blancs deviennent noirs.

::: tip

Les alphas intégrés fournis avec Nomad ne peuvent pas être inversés.

:::

### Scaling

La taille de la brosse dans Nomad est un cercle avec un rayon défini par l’utilisateur. Les textures sont souvent carrées ou rectangulaires ; les paramètres de `Scaling` vous permettent de décider comment la texture doit s’adapter à l’intérieur du cercle. Pour une texture carrée, une valeur de 0,7 s’adaptera à l’intérieur du cercle. Une valeur de 1 agrandira la texture de sorte que le cercle tienne à l’intérieur, rognant les bords.

![](/images/alpha_scaling.webp) 

L’activation de `Scaling - Y` vous permet d’étirer l’alpha verticalement.

![](/images/alpha_scaling_y.webp) 

### Rotation

La texture alpha sera tournée pour suivre la direction du trait. Vous pouvez ajouter un décalage de rotation, et si l’icône de verrouillage est activée, la texture restera verrouillée à cette rotation par rapport à l’écran.

### Tiling
![](/images/stroke_tiling.webp) 

Fréquence de répétition de la texture à l’intérieur du profil de la brosse. Les modes de répétition vous permettent de limiter à une seule texture dans le trait, ou à des textures répétées, ou en miroir où une texture sur deux est inversée pour créer des motifs ou aider à produire des textures sans couture.

![](/videos/alpha_tiling.mp4) 



### Mid value

Par défaut, les pixels noirs signifient aucune déformation et les pixels blancs une déformation positive maximale ; par exemple, une brosse d’argile avec une texture alpha de rochers ne tirera la surface vers l’extérieur que là où l’alpha n’est pas noir.

Si vous voulez que la brosse pousse la surface vers l’intérieur, ou à la fois pousse vers l’intérieur ET tire vers l’extérieur, vous pouvez modifier la valeur médiane. Ainsi, si vous définissez la valeur à 0,5, un gris moyen dans l’alpha ne fera rien, une valeur noire poussera vers l’intérieur, le blanc tirera vers l’extérieur.




## Falloff

![](/images/falloff_menu.webp) 

C’est similaire à l’[Alpha](#alpha), sauf que vous contrôlez l’intensité avec une seule courbe. Celle-ci est combinée avec l’alpha afin que vous puissiez utiliser une texture pour les détails, et l’atténuation pour contrôler le fondu des bords et l’intensité au centre de l’outil.

Lorsque la courbe est en haut, il s’agit d’une déformation maximale ; lorsqu’elle est en bas, la brosse n’a aucun effet.

Vous pouvez considérer la courbe comme une coupe transversale de la pointe de la brosse. La section inférieure donne un aperçu de ce à quoi ressemblerait une seule « empreinte » de la brosse sur la surface du modèle, et si une texture alpha est définie pour la brosse, elle sera également affichée pour prévisualiser la façon dont l’atténuation et l’alpha interagiront.

### Preset
Avec cette option sélectionnée, cliquer sur le graphique de la courbe fera apparaître un menu de préréglages. Les courbes arrondies donneront des résultats plus doux, les courbes anguleuses auront des résultats plus nets. Le bouton `Sub` dans la barre d’outils de gauche inversera effectivement l’atténuation, de sorte que le haut de la courbe poussera dans la surface au lieu de la tirer vers l’extérieur, ou inversement.

### Catmull-Rom
Lorsque cette option est sélectionnée, l’utilisateur peut dessiner ses propres courbes d’atténuation. L’éditeur de courbe fonctionne comme les courbes dans le reste de Nomad :

* Cliquez sur la courbe pour créer un nouveau point
* Faites glisser un point pour le repositionner
* Cliquez sur un point pour basculer entre net et lisse
* Faites glisser un point sur un point voisin pour le supprimer

### B-spline
Lorsque cette option est sélectionnée, l’utilisateur peut dessiner ses propres courbes d’atténuation. L’éditeur fonctionne comme pour Catmull-Rom, mais les points de courbe influencent la courbe au lieu d’être directement dessus, ce qui peut aider à créer des formes de courbe plus lisses.

L’éditeur de courbe possède 3 boutons :

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Agrandir l’éditeur de courbe                 |
| Reset    | ![](/icons/reset.webp)     | Rétablir la courbe à son état par défaut     |
| Symmetry | ![](/icons/symmetric.webp) | Afficher la courbe comme une « pointe de brosse » symétrique |


### Influence

* Sphere (3d) - L’influence est calculée en prenant la distance entre le sommet et le centre de la brosse.
* Circle (2d) - Le sommet est d’abord projeté sur le plan de la zone, avant de prendre sa distance par rapport au centre de la brosse. C’est similaire à la façon dont les alphas sont échantillonnés. 
* Cylinder - L’influence est projetée à travers la zone sous forme de cylindre, utilisée par le mode Silhouette ci-dessous.

### Silhouette
Par défaut, les traits n’affectent que la surface du modèle à l’intérieur du rayon de la brosse. Lorsque la silhouette est activée, le trait est projeté à travers l’ensemble du modèle. Cela peut être très utile lors du blocage initial d’un modèle, ou pour des formes qui nécessitent que les côtés restent perpendiculaires.



## Filter

![](/images/filter_menu.webp) 

### Accumulate stroke
Permet de ne pas limiter la quantité de matière pouvant être ajoutée/supprimée par trait. Par exemple, l’outil `Clay` a cette option activée, de sorte que la matière peut continuer à s’accumuler, tandis que l’outil `Brush` a cette option désactivée, de sorte que les traits cessent d’ajouter de la matière si vous continuez à passer le même trait sur la même zone du maillage. 

### Front-facing vertex only
Cette option ignore les sommets orientés vers l’arrière.
Elle peut être utile si vous voulez peindre une partie d’une géométrie fine sans affecter l’autre côté.
Elle fonctionne également pour la sculpture, mais vous pourriez rencontrer certains artefacts.

### Allow dynamic topology
Cette option n’est disponible que si votre maillage est en mode [Dynamic Topology](topology.md#dynamic-topology). Vous pouvez activer ou désactiver la topologie dynamique par outil.

### Connected topology
N’autorise la sculpture que sur les sommets qui sont reliés à la surface que vous touchez avec l’outil. Par exemple, lorsqu’elle est utilisée avec l’outil `Move`, cette option vous permet de déplacer une partie même si elle intersecte une autre partie.
![](/videos/connected_topology.mp4)

### Protect Area
![](/images/filter_protect_area.webp) 

Ces options empêchent les outils d’affecter certaines parties de votre maillage dans diverses conditions. 

L’option « Auto » signifie que si vous avez un masquage, un masquage de faces ou un masquage par groupes de faces visible dans le menu [Shading](shading), ils seront protégés, mais s’ils sont désactivés dans ce menu, la protection est désactivée.

* `All` - Bascule pour définir si les filtres de protection sont globaux ou par outil.
* `Hide` - Si des parties du maillage sont masquées avec l’outil de masquage, définit si elles doivent être protégées.
* `Mask` - Si des parties du maillage sont masquées, définit si elles doivent être protégées.
* `Facegroup` - Définit si vous ne pouvez utiliser un outil qu’à l’intérieur du premier groupe de faces touché.


### Keep sharp edges
Exclut les points dont les normales diffèrent trop de la normale de surface.

Cela modifie la façon dont la zone plane est calculée (Area sampling).

Cette option peut être utile pour les outils basés sur le lissage/flatten, ou si vous voulez colorer une surface principalement plane sans débordement.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Certains pinceaux ou options de trait nécessitent une normale de plan et une position de plan par rapport à la surface pour fonctionner.

Vous pouvez contrôler la façon de calculer ce plan moyen en définissant la zone d’échantillonnage comme un ratio du rayon de l’outil.

À 100 %, chaque point à l’intérieur du cercle de sélection est pris en compte.

À 0 %, seul le sommet ou le triangle le plus proche est pris en compte. Ces valeurs peuvent être liées pour `Normal radius` et `Position radius`, ou déverrouillées et définies indépendamment.


### Depth masking
![](/images/stroke_depthmask.webp)

Exclut les points qui se trouvent au-dessus ou en dessous d’une certaine distance du plan calculé (Area sampling).

Cela peut être utilisé pour peindre uniquement sur les zones bosselées, ou uniquement dans les cavités.

Le graphique représente une coupe transversale de la surface ; la ligne horizontale est l’endroit où se trouve la surface, le cercle représente le rayon de l’atténuation de la peinture au-dessus et au-dessous de la surface. `Height offset` est un pourcentage au-dessus ou au-dessous de la surface pour commencer le calcul du masquage. `Top area` et `Bottom area` vous permettent de mettre à l’échelle l’atténuation au-dessus et au-dessous du point de décalage.

#### Exemple : Peindre dans les cavités
Pour peindre uniquement les zones en cavité, définissez le décalage de hauteur à -100 %, et ajustez le curseur de la zone supérieure de sorte qu’il soit éloigné de la ligne horizontale. Cela signifie que le premier clic définit la profondeur « zéro », puis seules les zones en dessous de cette profondeur seront affectées.

![](/videos/stroke_depth_cavity.mp4)

#### Exemple : Peindre sur les bosses
Pour ne peindre que les zones en relief, définissez le décalage de hauteur à +90 %, de sorte que le bas du cercle croise légèrement la ligne horizontale. Lorsque vous cliquez sur le sommet d’une zone « haute », cela définit la profondeur, de sorte que tout ce qui se trouve à cette profondeur, plus un peu en dessous, et tout ce qui est plus haut, sera peint. Les cavités profondes seront ignorées.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Contrôle la façon dont la pression du stylet/de la plume affecte les brosses.

Par défaut, `Use global settings` est activé, ce qui signifie que toutes les brosses partagent les mêmes valeurs de pression.

### Pressure - Radius

Cette courbe contrôle la façon dont le rayon de la brosse est affecté par la pression. Par défaut, la relation est linéaire ; si votre stylet a une réponse fluide, alors le changement de rayon devrait également paraître fluide. Cela dit, de nombreux stylets ont une réponse non linéaire, que vous pouvez compenser avec cette courbe. Par exemple, si le rayon ne semble pas atteindre sa valeur maximale à forte pression, utilisez un préréglage de courbe comme « out-pow3 », avec une courbe qui se cambre vers le haut, pour augmenter le rayon plus tôt.

Cette boîte de dialogue est similaire à l’affichage de la courbe d’atténuation ; vous pouvez utiliser un préréglage en appuyant sur la fenêtre de courbe, ou dessiner vos propres courbes avec les modes Catmull-Rom et B-Spline.

Si vous voulez un rayon constant, désactivez cette section.

### Pressure - Intensity

Similaire au curseur de rayon, mais pour contrôler l’intensité. Si vous voulez une intensité constante, désactivez cette section.

### Pressure smoothing

Moyenne les événements de pression du stylet pour des résultats plus réguliers.
