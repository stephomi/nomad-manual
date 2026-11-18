# ![](/icons/brush.webp) Trait {#stroke}

---
![](/images/stroke_overview.webp) 

## Présentation {#overview}

Vous pouvez personnaliser le comportement du trait de la plupart des outils.
Les réglages ressemblent à ceux des applications de peinture 2d, mais certaines options sont propres à la sculpture et à la 3d.

Les options sont réparties dans 5 sous-menus :

| Nom      | Icône                        | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Trait       | ![](/icons/brush.webp)      | Contrôle la façon dont le trait s'applique au modèle               |
| Alpha       | ![](/icons/alpha.webp)      | Comment une texture en niveaux de gris sert d'empreinte au pinceau |
| Atténuation | ![](/icons/falloff.webp)    | Contrôle comment la force du pinceau varie du centre vers le bord  |
| Filtre      | ![](/icons/filter.webp)     | Comment la géométrie du modèle influence le pinceau                |
| Pression    | ![](/icons/pressure.webp)   | Contrôle la réponse à la pression du stylet                        |

::: tip
Toutes les options de trait ne s'appliquent pas à tous les outils. Celles que l'outil actif n'utilise pas sont désactivées ou masquées. 
:::


## ![](/icons/brush.webp) Trait {#stroke-1}

### ![](/icons/radius.webp) Rayon {#radius}

![](/images/stroke_radius.webp)

Les options du rayon sont des réglages globaux : elles s'appliquent à tous les outils.

#### Espace {#size}

* `Écran` - le rayon est défini en unités de l'écran. Si vous lui donnez une largeur de 100 pixels, il garde ces 100 pixels, que vous zoomiez ou dézoomiez.
* `Monde (3D)` - le rayon est défini en unités 3d. Par exemple, si vous créez une sphère et donnez au rayon la taille de cette sphère, le rayon garde la taille de la sphère quand vous zoomez ou dézoomez.

#### ![](/icons/link.webp) Synchroniser les raccourcis {#sync-shortcut}

Une fois activé, le rayon et les réglages de silhouette restent synchronisés quand vous passez aux pinceaux de raccourci (`Lisser`, `Masque` ou `Masquer`). Ainsi, un rapide passage de lissage ou de masque se fait avec la même taille de pinceau que l'outil que vous utilisiez.

#### ![](/icons/link.webp) Partager le rayon {#share-radius}

Une fois activé, tous les outils utilisent le même rayon. Par défaut, chaque outil a son propre rayon.


### Type de trait {#stroke-type}

![](/images/stroke_strokemode.webp)

Les traits peuvent fonctionner selon plusieurs modes :

### ![](/icons/stroke_dot.webp) Point {#dot}
Faites glisser comme pour un trait de peinture classique. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rouleau {#roll}
L'alpha du pinceau pivote pour suivre la direction du trait, pratique pour faire des coutures sur du tissu. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Saisie + rayon {#lock-radius}
Applique une empreinte de pinceau à **_hauteur_** fixe. Le glisser règle l'échelle et la rotation.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Saisie + intensité {#lock-intensity}
Applique une empreinte de pinceau à **_rayon_** fixe. Le glisser règle la hauteur et la rotation.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Les modes `Saisie + rayon` et `Saisie + intensité` ignorent les réglages de [Pression](#pressure), puisque le glisser définit déjà la taille et la force.
:::

![](/images/stroke_strokemodemove.webp)

Les outils `Déplacer` et `Glisser` ont leurs 3 options à eux :

### ![](/icons/snake.webp) Glisser {#drag}

Met à jour en continu ce qui se trouve dans le rayon du pinceau pendant le trait. Un trait rapide laisse la surface derrière lui, alors qu'un trait lent garde la matière accrochée et crée des formes plus longues. C'est le mode par défaut de l'outil `Glisser`. Avec la `Topologie dynamique`, il permet de faire des extrusions en forme de serpent. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Saisir {#grab}
Sélectionne ce qui se trouve dans le rayon du pinceau au début du trait, et garde cette sélection. C'est utile pour des déplacements plus précis : vous pouvez ajuster soigneusement la distance du déplacement sans emporter par accident plus que ce que vous aviez sélectionné. C'est le mode par défaut de l'outil `Déplacer`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Saisie + rayon (glisser) {#lock-radius-drag}
Le rayon choisi est ignoré : il est défini à la volée selon la distance entre le point de départ et l'endroit où vous avez fait glisser le trait. Petite distance = petit rayon, grande distance = grand rayon. Le curseur d'intensité contrôle la forme de l'atténuation. Pratique pour ébaucher des formes organiques et caoutchouteuses.
![](/videos/stroke_lockradius_drag.mp4) 

D'autres outils affichent ici leurs propres types de trait, par exemple `Relâcher`, `Lisser` et `Estomper` pour les outils de lissage, ou des formes comme `Lasso` et `Courbe` pour les outils basés sur une sélection. Ils sont décrits avec chaque [outil](tools.md).


### Compenser l'espacement {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Les traits avec un faible espacement (moins de 50 %) s'accumulent vite et deviennent plus intenses qu'avec un espacement plus grand. Cette option compense cet effet, pour que les traits aient à peu près la même intensité quel que soit l'espacement.

### Espacement des traits {#stroke-spacing}
L'écart entre chaque empreinte du pinceau pendant un glisser. En dessous de 100 %, les empreintes se chevauchent et donnent l'impression d'un trait continu. Au-dessus de 100 %, des espaces apparaissent, ce qui est utile pour sculpter des détails comme des coutures ou des fermetures éclair.

### Stabilisateur à corde {#lazy-rope-stabilizer}
Le trait suit le pointeur avec un certain retard, à une distance donnée. Cela permet de tracer des lignes bien régulières.
![](/videos/stroke_lazy_rope.mp4) 

### Lissage du trait {#stroke-smoothing}
Fait la moyenne de plusieurs positions du pointeur pour obtenir un trait plus lisse.
Avec des valeurs élevées, le trait prend du retard sur le pointeur, mais finit par le rattraper.
C'est pratique pour tracer des lignes régulières.

### Rayon d'accrochage {#snap-radius}
Raccroche le trait au précédent quand le pointeur démarre près de l'endroit où le dernier trait s'est arrêté. Le rayon détermine jusqu'où chercher la fin du trait précédent. C'est utile pour tracer de longues lignes continues en faisant des pauses fréquentes.

### ![](/icons/trail.webp) Traînée {#trail}

Une fois activée, chaque nouvelle empreinte réapplique aussi les derniers points du trait derrière elle. `Nombre de traînées` règle combien de points sont réappliqués, `Intensité de la traînée` leur force, et `Rayon de la traînée` de combien ils grossissent.

La traînée ne fonctionne qu'avec le type de trait `Point`, et pas avec l'[influence](#influence) d'atténuation `Crête`.

### ![](/icons/silhouette.webp) Silhouette {#silhouette}
![](/images/stroke_silhouette.webp)
Par défaut, les traits n'affectent que la surface du modèle comprise dans le rayon du pinceau. Avec la silhouette activée, le trait est projeté à travers tout le modèle. C'est très utile pour ébaucher un modèle au début, ou pour des formes dont les côtés doivent rester perpendiculaires.

La direction de projection peut être choisie explicitement :

* `X`, `Y`, `Z` - projette selon un axe fixe.
* `Vue` - projette selon la direction de la caméra.
* `Si accroché` - projette selon la direction de la caméra, mais seulement quand la caméra est accrochée à une vue. Sinon, le trait reste un trait normal.
* `Le plus proche` - projette selon l'axe le plus proche de la direction de la caméra. C'est le réglage par défaut.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Aléatoire {#randomize}

![](/images/stroke_randomize.webp)

L'`Intensité`, le `Décalage`, la `Rotation` et l'`Échelle` du trait peuvent chacun varier aléatoirement. La case à cocher de chaque ligne l'active ou la désactive. Cela permet toute une gamme d'effets : par exemple, l'aléatoire avec l'outil de peinture donne une couleur marbrée, et avec l'outil de pli, il peut créer des détails de peau.

`Période (plus lent)` règle la durée du cycle aléatoire : augmentez-la pour des variations lentes et douces, baissez-la pour un bruit rapide. Le petit bouton à côté de chaque ligne ajuste la période de cette ligne seulement.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Aléatoire - TSV {#randomize-hsv}

Pour les outils qui peignent, la `Teinte`, la `Saturation` et la `Valeur` de la couleur de peinture peuvent aussi varier aléatoirement, avec leur propre période. Idéal pour ajouter de subtiles variations de couleur à de la peau ou de la pierre.

### Décalage de trait {#stroke-offset}

Applique un décalage constant au trait, pour que votre doigt ne le cache pas. C'est utile sur les petits écrans. C'est un réglage global : activez-le avec sa case à cocher, et il s'applique à tous les outils.

## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

L'`Alpha` est une texture qui module le comportement de votre pinceau.
C'est une image en niveaux de gris : les pixels noirs ne déforment pas du tout, les pixels blancs déforment à fond.

Touchez l'image de l'alpha pour la changer. En plus des alphas fournis et de ceux que vous importez, la liste des alphas peut aussi télécharger des cartes de déplacement depuis Poly Haven.

Touchez l'aperçu du matériau pour charger un alpha depuis un préréglage de matériau. Vous pouvez aussi enregistrer des préréglages de matériau ici, et choisir d'intégrer les textures à l'outil.

::: tip
La texture n'est jamais redimensionnée : une grande texture peut donc ralentir l'application.
:::

### ![](/icons/blend_contrast.webp) Corriger l’alpha {#invert-pixels}
Le bouton `Corriger...` d'un alpha importé ouvre une fenêtre qui corrige l'image elle-même : sa valeur médiane, l'inversion des pixels (le noir devient blanc et le blanc devient noir), une rotation de 90° et un retournement horizontal ou vertical. Le fichier image est réécrit, donc les autres applications voient aussi l'image corrigée.

::: tip

Les alphas fournis avec Nomad ne peuvent pas être corrigés.

:::

### Projection {#projection}

La façon dont l'alpha est projeté sur le modèle :

* `Surface` - l'alpha se pose sur la surface sous le pinceau, en suivant son orientation.
* `Écran` - l'alpha est projeté directement depuis la vue.
* `Pavage` - l'alpha est projeté depuis la vue et reste en place pendant que vous peignez par-dessus, comme un pochoir : un motif répété se raccorde donc sans couture. La rotation est verrouillée, et la pression du stylet ne change pas la taille du motif.
* `Triplanaire` - l'alpha est projeté selon les 3 axes. Les options d'échelle, de rotation et de pavage ci-dessous sont remplacées par les réglages de texture triplanaire.

### ![](/icons/diagonal.webp) Échelle {#scaling}

Dans Nomad, le pinceau est un cercle dont vous choisissez le rayon. Les textures sont souvent carrées ou rectangulaires : les paramètres d'`Échelle` vous laissent décider comment la texture s'inscrit dans le cercle. Pour une texture carrée, une valeur de 0,7 la fait tenir dans le cercle. Une valeur de 1 l'agrandit pour que le cercle tienne à l'intérieur, ce qui rogne les bords.

![](/images/alpha_scaling.webp) 

Activer `Échelle Y` vous permet d'étirer l'alpha verticalement. Le premier curseur devient alors `Échelle X`.

![](/images/alpha_scaling_y.webp) 

`Retourner horizontalement` inverse l'alpha de gauche à droite.

### Rotation {#rotation}

La texture alpha pivote pour suivre la direction du trait. Vous pouvez ajouter un décalage de rotation, et si l'icône de cadenas est activée, la texture reste verrouillée sur cette rotation par rapport à l'écran.

Le bouton en forme de stylet à côté fait pivoter l'alpha quand vous faites tourner votre stylet sur lui-même (barrel roll), avec les traits `Saisie + rayon` et `Saisie + intensité`, tant que la rotation n'est pas verrouillée. Cela ne fonctionne qu'avec les stylets qui le gèrent.

### Pavage {#tiling}
![](/images/stroke_tiling.webp) 

Le nombre de fois que la texture se répète dans le profil du pinceau. Les modes `Recouvrement - X` et `Recouvrement - Y` permettent de se limiter à une seule texture dans le trait (`Aucun`), de répéter la texture (`Répéter`), ou de la répéter en miroir, une texture sur deux étant retournée, pour créer des motifs ou aider à obtenir des textures sans raccord (`Miroir`). Ils sont disponibles avec le trait `Rouleau`, la projection `Pavage`, ou un `Pavage` supérieur à 1.

`Sans marge` ne compte que pour les alphas et textures de pinceau non carrés. Une fois activé, chaque image se répète de son côté, sans espacement. Désactivez-le pour garder l'alpha et les autres images synchronisés quand leurs proportions diffèrent.

![](/videos/alpha_tiling.mp4) 



### Valeur médiane {#mid-value}

Par défaut, les pixels noirs ne déforment pas et les pixels blancs déforment à fond vers l'extérieur. Par exemple, un pinceau argile avec une texture alpha de rochers ne fait ressortir la surface que là où l'alpha n'est pas noir.

Si vous voulez que le pinceau enfonce la surface, ou qu'il enfonce ET fasse ressortir, modifiez la valeur médiane. Avec une valeur de 0,5, un gris moyen dans l'alpha ne fait rien, le noir enfonce et le blanc fait ressortir.

Deux boutons vous aident à trouver la bonne valeur : le bouton carré lit la valeur médiane sur le bord de l'image, et la pipette vous permet de la prélever sur l'alpha lui-même.




## ![](/icons/falloff.webp) Atténuation {#falloff}

![](/images/falloff_menu.webp) 

C'est semblable à l'[Alpha](#alpha), sauf que l'intensité est pilotée par une simple courbe. Elle se combine avec l'alpha : vous pouvez ainsi utiliser une texture pour le détail, et l'atténuation pour contrôler le fondu sur les bords et l'intensité au centre de l'outil.

Quand la courbe est en haut, la déformation est maximale ; quand elle est en bas, le pinceau n'a aucun effet.

Voyez la courbe comme une coupe de la pointe du pinceau. La partie du bas montre un aperçu d'une seule « empreinte » du pinceau sur la surface du modèle ; si le pinceau a une texture alpha, elle y apparaît aussi, pour voir comment l'atténuation et l'alpha se combinent.

### ![](/icons/fx.webp) Préréglage {#preset}
Avec `Préréglage...` sélectionné, toucher le graphique de la courbe ouvre un menu de préréglages. Les courbes arrondies donnent des résultats plus doux, les courbes anguleuses des résultats plus nets. Le bouton `Soustr.` de la barre d'outils de gauche inverse en pratique l'atténuation : le haut de la courbe enfonce la surface au lieu de la faire ressortir, ou l'inverse.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Une fois sélectionné, vous pouvez dessiner vos propres courbes d'atténuation. L'éditeur de courbe fonctionne comme les courbes ailleurs dans Nomad :

* Touchez la courbe pour créer un nouveau point
* Faites glisser un point pour le déplacer
* Touchez un point pour le faire passer de net à lisse
* Faites glisser un point sur un point voisin pour le supprimer

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Une fois sélectionné, vous pouvez dessiner vos propres courbes d'atténuation. L'éditeur fonctionne comme Catmull-Rom, mais les points attirent la courbe au lieu de se trouver dessus, ce qui aide à créer des formes de courbe plus douces.

### ![](/icons/curve_bevel.webp) Biseau {#bevel}
Les points sont reliés par des segments droits, avec des coins arrondis dont la taille dépend de la netteté de chaque point. Pratique pour des pinceaux à sommet plat avec un biseau propre sur le bord.

L'éditeur de courbe a 3 boutons :

| Élément       | Icône                       | Description                                         |
| :-----------: | :-------------------------: | :-------------------------------------------------: |
| Agrandir      | ![](/icons/maximize.webp)  | Agrandit l'éditeur de courbe                        |
| Réinitialiser | ![](/icons/reset.webp)     | Remet la courbe dans son état par défaut            |
| Symétrie      | ![](/icons/symmetric.webp) | Affiche la courbe comme une « pointe de pinceau » symétrique |


### Influence {#influence}

* `Sphère` (3d) - l'influence est calculée d'après la distance entre le sommet et le centre du pinceau.
* `Cercle` (2d) - le sommet est d'abord projeté sur le plan de la zone, puis on mesure sa distance au centre du pinceau. C'est ainsi que les alphas sont échantillonnés. 
* `Cylindre` - l'influence est projetée à travers la zone sous forme de cylindre. Cela revient à activer la [Silhouette](#silhouette-1) ci-dessous.
* `Crête` - l'atténuation est mesurée en travers du trait : la courbe devient la coupe transversale de tout le trait. Le bouton `Sym` reproduit alors le profil en miroir de part et d'autre du trait : modifiez un côté, l'autre suit. Quand il est désactivé, la courbe va du bord gauche du trait à son bord droit. Non disponible pour les outils de type aplatir.

### ![](/icons/silhouette.webp) Silhouette {#silhouette-1}
Par défaut, les traits n'affectent que la surface du modèle comprise dans le rayon du pinceau. Avec la silhouette activée, le trait est projeté à travers tout le modèle. C'est très utile pour ébaucher un modèle au début, ou pour des formes dont les côtés doivent rester perpendiculaires. Elle a les mêmes options de projection que la [Silhouette](#silhouette) de l'onglet Trait.

## ![](/icons/filter.webp) Filtre {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Accumuler les traits {#accumulate-stroke}
Supprime toute limite à la quantité de matière ajoutée ou retirée par trait. Par exemple, l'outil `Argile` a cette option activée, donc la matière peut continuer à s'accumuler, alors que l'outil `Pinceau` l'a désactivée : le trait cesse d'ajouter de la matière si vous repassez sans cesse sur la même zone du maillage pendant un même trait. 

### ![](/icons/culling.webp) Sommets face caméra {#front-facing-vertex-only}
Cette option ignore les sommets orientés vers l'arrière.
Elle est utile pour peindre une partie d'une géométrie fine sans toucher l'autre face.
Elle fonctionne aussi en sculpture, mais vous risquez d'avoir quelques artefacts.

### ![](/icons/eye_open.webp) Sommets visibles uniquement {#visible-vertex-only}
Ignore les sommets cachés derrière d'autres surfaces, vus depuis la caméra. Cette option apparaît pour les traits en forme (lasso, rectangle...) des outils de masque, de peinture, `Groupe de faces` et `Masquer`.

### ![](/icons/dynamic.webp) Autoriser la topologie dynamique {#allow-dynamic-topology}
Cette option n'est disponible que si votre maillage est en mode [Topologie dynamique](topology.md#dynamic-topology). Vous pouvez activer ou désactiver la topologie dynamique outil par outil.

### ![](/icons/connect.webp) Topologie connectée {#connected-topology}
Ne sculpte que les sommets reliés à la surface que vous touchez avec l'outil. Par exemple, avec l'outil `Déplacer`, cela vous permet de déplacer une partie même si elle en croise une autre.
![](/videos/connected_topology.mp4)

### Protéger la zone {#protect-area}
![](/images/filter_protect_area.webp) 

Ces options empêchent les outils d'affecter certaines parties de votre maillage selon différentes conditions. Chacune peut être réglée sur `Auto`, `Non` ou `Oui`, et la petite flèche indique ce que vaut `Auto` en ce moment.

* `Masquer` - si des parties du maillage sont cachées avec l'outil Masquer, indique si elles doivent être protégées. Sur `Auto`, les faces cachées sont protégées, sauf si leur filaire est visible (voir les réglages [Filaire](settings.md#wireframe)).
* `Masque` - si des parties du maillage sont masquées, indique si elles doivent être protégées. Sur `Auto`, les parties masquées sont protégées tant que le masque est visible dans le menu [Ombrage](shading).
* `Groupe de faces` - indique si l'outil ne peut agir que dans le premier groupe de faces touché. Sur `Auto`, cela suit la visibilité des groupes de faces dans le menu [Ombrage](shading).

Le bouton `(Tout)` indique si ces protections sont globales, partagées par tous les outils, ou réglées outil par outil.


### Échantillonnage de zone {#area-sampling}
Certains pinceaux ou options de trait ont besoin d'une normale et d'une position de plan sur la surface pour fonctionner.

Vous pouvez contrôler le calcul de ce plan moyen en réglant la zone d'échantillonnage, en proportion du rayon de l'outil.

À 100 %, tous les points dans le cercle de sélection sont pris en compte.

À 0 %, seul le sommet ou le triangle le plus proche est pris en compte. Ces valeurs peuvent être liées pour `Rayon des normales` et `Rayon de position`, ou déverrouillées et réglées séparément.

### Filtre de normale de zone {#keep-sharp-edges}
Exclut les points dont la normale s'écarte trop de la normale de la surface.

Cela change le calcul du plan de la zone (échantillonnage de zone) : c'est donc surtout utile pour les outils de type argile ou aplatir, ou pour colorer une surface à peu près plane sans déborder.

Les angles `Min` et `Max` contrôlent la transition entre les points exclus et ceux pleinement affectés, comme le montre le petit disque coloré à côté.

![](/videos/filter_keep_sharp_edges.mp4)

### Filtre de normale d'atténuation {#falloff-normal-filter}
Comme le [Filtre de normale de zone](#keep-sharp-edges), il exclut les points dont la normale s'écarte trop de la normale de la surface, mais il agit sur l'atténuation du pinceau plutôt que sur le calcul du plan. Il est utile pour peindre des creux ou des bosses.


### Filtre de profondeur {#depth-masking}
![](/images/stroke_depthmask.webp)

Exclut les points situés au-dessus ou en dessous d'une certaine distance du plan calculé (échantillonnage de zone).

Cela permet de peindre seulement sur les zones en relief, ou seulement dans les creux.

Le graphique représente une coupe de la surface : la ligne horizontale correspond à la surface, et le cercle représente le rayon d'atténuation de la peinture au-dessus et en dessous de la surface. `Décalage en hauteur` est un pourcentage au-dessus ou en dessous de la surface à partir duquel commence le calcul du masquage. Avec `Atténuation de la profondeur` activé, `Zone supérieure` et `Zone inférieure` permettent d'ajuster l'atténuation au-dessus et en dessous du point de décalage.

#### Exemple : peindre dans les creux {#example-paint-in-cavities}
Pour ne peindre que les creux, réglez le décalage en hauteur à -100 %, et ajustez le curseur de la zone supérieure pour l'éloigner de la ligne horizontale. Le premier contact définit alors la profondeur « zéro », et seules les zones situées sous cette profondeur sont affectées.

![](/videos/stroke_depth_cavity.mp4)

#### Exemple : peindre sur les reliefs {#example-paint-on-bumps}
Pour ne peindre que les zones hautes, réglez le décalage en hauteur à +90 %, de sorte que le bas du cercle croise légèrement la ligne horizontale. Quand vous touchez le haut d'une zone « haute », cela définit la profondeur : tout ce qui est à cette profondeur, un peu en dessous, ou plus haut, sera peint. Les creux profonds sont ignorés.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Pression {#pressure}
![](/images/pressure_menu.webp) 

Contrôle comment la pression du stylet agit sur les pinceaux.

### Réglages globaux {#use-global-settings}

Par défaut, `Réglages globaux` est activé : tous les pinceaux partagent les mêmes valeurs de pression. Décochez-le pour donner à l'outil actif ses propres réglages de pression.

### ![](/icons/radius.webp) Rayon {#pressure-radius}

Cette courbe contrôle comment la pression agit sur le rayon du pinceau. Par défaut, la relation est linéaire : si votre stylet a une réponse régulière, la variation du rayon doit l'être aussi. Cela dit, beaucoup de stylets ont une réponse non linéaire, que vous pouvez compenser avec cette courbe. Par exemple, si le rayon ne semble pas atteindre son maximum à forte pression, prenez un préréglage comme 'out-pow3', dont la courbure monte, pour augmenter le rayon plus tôt.

Cette fenêtre ressemble à l'affichage de la courbe d'atténuation : vous pouvez choisir un préréglage en touchant la courbe, ou dessiner vos propres courbes avec les modes `Catmull-Rom`, `B-spline` et `Biseau`.

Si vous voulez un rayon constant, désactivez cette section.

### ![](/icons/intensity.webp) Intensité {#pressure-intensity}

Comme la courbe du rayon, mais pour l'intensité. Si vous voulez une intensité constante, désactivez cette section.

### Limiter la pression à 100% {#limit-pressure}

Garantit que la pression du stylet ne dépasse jamais 100 %. C'est un réglage global.

### Lissage de la pression {#pressure-smoothing}

Fait la moyenne des valeurs de pression du stylet pour un résultat plus lisse.
