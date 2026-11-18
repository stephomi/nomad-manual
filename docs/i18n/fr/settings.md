# ![](/icons/cog.webp) Réglages {#reset-to-default}

Le menu Réglages contient de nombreuses options pour régler l'apparence et le comportement de Nomad.

![](/images/settings_overview.webp)

La rangée de boutons en haut du menu mène directement à une section : `Curseur`, `Indicateur`, `Fil`, `Grille`, `Recto verso`, `Contour`, `Surbrillance`, `Cube d'alignement`, `Statistiques`, `Poignées`, `Forme`, `Répéteurs` et `Multirésolution`.

## Réglages d'affichage {#display-settings}
Cette section contient des raccourcis rapides vers la plupart des réglages situés plus bas dans ce menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Ombrage lisse {#smooth-shading}
Bascule entre l'ombrage lisse et l'ombrage à facettes. Avec les facettes, chaque polygone est ombré indépendamment, ce qui vous laisse voir la topologie sous-jacente.
Il peut être utile de voir les facettes pendant la sculpture, puis de passer à l'ombrage lisse pour le rendu.

Désactiver l'ombrage lisse améliore un peu les performances.

### ![](/icons/outline.webp) Contour {#outline-quick}
Affiche ou masque un contour autour de la sélection actuelle.

C'est utile pour bien voir le ou les maillages sélectionnés si [Assombrir les objets non sélectionnés](#darken-unselected-objects) est désactivé.

Côté performances, [Assombrir les objets non sélectionnés](#darken-unselected-objects) est bien plus efficace que le contour.

### ![](/icons/grid.webp) Grille {#grid-quick}
Affiche ou masque une grille en arrière-plan, utile pour comprendre la position et l'échelle des objets.

### ![](/icons/culling.webp) Recto verso {#two-sided-quick}
Active ou désactive l'affichage des polygones des deux côtés. Toutes les faces sont orientées dans une certaine direction.
Les faces considérées comme *arrière* sont celles qui sont tournées « dos » au point de vue de la caméra.

Par exemple, la sphère simple du démarrage a ses faces tournées vers l'extérieur.
Si vous placez la caméra à l'intérieur de la sphère, vous voyez alors l'arrière de ces faces.

La plupart du temps, vous ne devriez pas voir l'arrière des faces : les colorer peut donc vous aider à repérer d'éventuels problèmes ou une topologie incorrecte.

Désactiver le rendu `Recto verso` peut améliorer un peu les performances de rendu.


### ![](/icons/wireframe.webp) Filaire {#wireframe-quick}
Affiche ou masque le maillage en filaire par-dessus le modèle. 

Notez qu'activer le filaire réduit les performances.

### ![](/icons/snap_cube.webp) Cube d'alignement {#snap-cube-quick}
Affiche ou masque une icône d'aide dans le coin de la scène, utile pour vous repérer dans l'espace et passer rapidement d'une vue de face, de dos, de gauche, de droite, de dessus ou de dessous à l'autre.

### ![](/icons/palette.webp) Afficher la peinture {#show-painting}
Affiche ou masque la peinture. Quand elle est masquée, les objets sont affichés avec un matériau blanc non métallique, à 25 % de rugosité, au lieu de leur peinture.

### ![](/icons/tool_hide.webp) Utiliser Masquer {#use-hide}
Active ou désactive le masquage. Quand il est désactivé, il est toujours là, simplement inactif. Ce bouton est désactivé si vous utilisez actuellement l'outil Masquer.

### ![](/icons/shield.webp) Afficher le masque {#show-mask}
Active ou désactive le masque. Quand il est désactivé, il est toujours là, simplement inactif. Touchez à nouveau ce bouton pour le réactiver.

Si vous voulez cacher le masque TOUT EN le gardant actif, réglez la couleur du masque ci-dessous sur blanc. Pensez à la remettre en gris une fois terminé !

Notez que ce bouton est désactivé si vous utilisez actuellement un outil de masque. 

### ![](/icons/shield.webp) Masque → Opaque {#mask-opaque}
`Masque → Opaque` ignore les sommets transparents pour le masque. Cela ne concerne que l'opacité des sommets et des textures : les faces cachées par « Masquer » restent cachées. L'option n'est disponible que lorsque `Afficher le masque` est activé.

### ![](/icons/bang.webp) Surbrillance {#highlight-quick}
Active ou désactive le flash de surbrillance de la sélection. Quand vous sélectionnez des objets, l'objet sélectionné clignote brièvement pendant 500 millisecondes. La couleur et la durée du flash se règlent plus bas.

### ![](/icons/list.webp) Statistiques {#stats-quick}
Affiche ou masque le texte d'état dans la vue 3d. Il donne des informations sur la mémoire du système, le nombre total de sommets de la scène, et le nombre de sommets de la sélection actuelle.

----- 

### ![](/icons/cube.webp) Assombrir les objets non sélectionnés {#darken-unselected-objects}
Les objets non sélectionnés sont assombris pour faire ressortir la sélection actuelle.

### ![](/icons/shield.webp) Masque {#mask}
La couleur utilisée pour le masque, un gris moyen par défaut, multipliée avec la couleur de votre objet. Réglez-la sur blanc pour rendre le masque invisible, mais pensez à la remettre en gris une fois terminé !

## ![](/icons/cursor.webp) Curseur {#cursor}

### Cercle {#show-circle-while-sculpting}
Quand afficher le cercle du rayon du pinceau :

* `Auto` - affiche le cercle, mais le cache pendant que vous sculptez.
* `Non` - n'affiche jamais le cercle.
* `Oui` - affiche toujours le cercle, même pendant la sculpture.

### Afficher le petit point {#show-small-dot}
Affiche un point au centre du trait pendant la sculpture, ou quand le pivot de la caméra change.

### Afficher le stabilisateur de corde {#show-rope-stabilizer}
Trace une ligne qui indique la longueur de la corde quand le [Stabilisateur à corde](stroke.md#lazy-rope-stabilizer) est actif dans les réglages du trait.

### Afficher l’indicateur de roulis {#show-roll-hint}
Affiche le guide de direction du roulis pendant que vous utilisez un raccourci clavier de roulis.

### ![](/icons/radius.webp) Taille {#dot-size}
La taille du petit point.

### Couleurs {#cursor-colors}
Le curseur change de couleur selon ce que vous faites : `Sculpter`, `Arrière-plan` (au survol de l'arrière-plan), `Masque`, `Lisser`, `Caméra` et `Rayon`. Chaque couleur peut être personnalisée ici.

## ![](/icons/cursor.webp) Indicateur {#indicator}
![](/images/settings_indicator.webp)

Affiche un ou plusieurs indicateurs visuels pour les tutoriels et les captures d'écran. Réglez-le sur `Oui` pour l'activer (sur iOS, il existe aussi une option `Auto`).

Les boutons `Doigt`, `Stylet` et `Souris` affichent une icône quand ce type de saisie est détecté.

### Couleur {#indicator-color}
La couleur de l'indicateur.

### Taille/Icône/Cercle {#indicator-shape}
Des réglages pour ajuster la taille de l'indicateur, et l'opacité de l'icône et du cercle qui le composent.

## ![](/icons/wireframe.webp) Filaire {#wireframe}
![](/images/settings_wireframe.webp)
Active l'affichage du maillage en filaire.

### Cible {#target}
Indique si le filaire s'affiche sur les objets non sélectionnés, uniquement sur les objets sélectionnés, ou sur tous les objets.

### Masquer {#hide}
Indique si le filaire reste affiché sur les polygones cachés.

### Multirésolution : Niveau 0 uniquement {#multiresolution-level-0-only}
En multirésolution, le filaire du niveau 0 est plus foncé, et celui des niveaux supérieurs de plus en plus clair. Quand cette option est activée, seul le filaire du niveau 0 est affiché.

### Couleur {#wireframe-color}
Règle la couleur et l'opacité du filaire.

## ![](/icons/grid.webp) Grille {#grid}
![](/images/settings_grid.webp)
Active la grille.

### Accrochage {#snap}
Ces options font s'accrocher les points des outils à base de courbes et de formes (`Tour`, `Tube`, formes polygone et tracé...) pendant que vous les dessinez :

* `Accrocher à la grille` - s'accroche à la grille.
* `Accrocher aux points (vue alignée)` - s'accroche aux points existants proches quand la caméra est alignée sur un axe.
* `Accrocher aux points (vue libre)` - s'accroche aux points existants proches quand la caméra n'est pas alignée.

### Couleur {#grid-color}
Règle la couleur et l'opacité de la grille. Ces options apparaissent quand la grille est visible.

`Vignettage` estompe la grille vers ses bords. `Seuil de division` règle, en pixels, la densité que peuvent atteindre les lignes de la grille à l'écran avant que la grille passe à un autre niveau de subdivision.

## ![](/icons/culling.webp)Recto verso {#two-sided}
Permet de voir les faces des polygones des deux côtés.

### Couleur de la face arrière {#backface-color}
`Face arrière colorée` active la teinte des faces arrière, et `Couleur de la face arrière` règle la couleur de cette teinte.

## ![](/icons/outline.webp)Contour {#outline}
Active un contour autour des objets sélectionnés.

### Couleur du contour, Épaisseur {#outline-color-thickness}
Règle la couleur et l'`Épaisseur` du contour.


## ![](/icons/bang.webp) Surbrillance {#highlight}
Active un bref flash quand la sélection change.
### Couleur, Durée {#color-duration}
Règle la couleur et la durée du flash, en millisecondes.

## ![](/icons/snap_cube.webp) Cube d'alignement {#snap-cube}
![](/images/settings_snapcube.webp)

Affiche une icône d'aide dans le coin de la scène, utile pour passer rapidement d'une vue de face, de dos, de gauche, de droite, de dessus ou de dessous à l'autre. Touchez les côtés du cube pour passer d'une vue orthographique à l'autre.

### Forme {#shape}
Choisissez une sphère, un cube ou un trièdre comme forme du cube d'alignement.

### Restreindre l'alignement {#restrict-alignment}
Aligne les vues d'alignement sur les axes du monde. Quand cette option est activée, seules les 6 vues principales sont possibles. Sur `Auto`, cette restriction ne s'applique que lorsque la caméra est en mode `Plateau tournant`.

### Taille {#size}
Règle la taille du cube d'alignement.

### Retourner 180° {#flip-180}
Active un comportement au toucher : si la vue est alignée, toucher le centre du cube fait pivoter la vue de 180 degrés. Par exemple, si la vue est alignée de face, toucher le cube passe à la vue de dos.

### Arêtes et coins {#edges-corners}
Ajoute des vues d'alignement sur les arêtes et les coins du cube (les zones ambrées). Non disponible avec la forme trièdre.

### Glissement en mode plateau tournant {#turntable-drag}
Faire glisser le cube le fait tourner sans faire rouler la caméra, et marque un arrêt sur chaque vue d'alignement. Désactivez cette option pour faire glisser le cube avec la rotation `Trackball` à la place. Dans les deux cas, le glissement reste horizontal ou vertical. Avec une caméra en `Plateau tournant`, le cube se fait toujours glisser de cette façon.

### Position {#snap-position}
Choisit dans quel coin se trouve le cube d'alignement.


## ![](/icons/list.webp) Statistiques {#stats}
![](/images/settings_stats.webp)

Affiche des informations sur la mémoire du système, le nombre total de sommets de la scène, et le nombre de sommets de la sélection actuelle.

### Position {#stats-position}
Choisit dans quel coin se trouvent les statistiques.

## ![](/icons/edit_radius.webp) Poignée {#handle}
Les réglages des poignées que vous faites glisser dans la vue, comme le gizmo.

### Saisie numérique {#gizmo-input}
Permet de saisir une valeur numérique en touchant l'une des commandes du gizmo.

### Masquer pendant l'action {#hide-on-interaction}
Estompe le gizmo pendant que vous le manipulez, pour qu'il ne vous gêne pas.

### ![](/icons/opacity.webp) Opacité {#handle-opacity}
L'opacité des poignées.

## ![](/icons/shape_lasso.webp) Forme {#shape-settings}
L'apparence à l'écran des formes que vous dessinez avec les traits de forme (lasso, rectangle, courbe...).

### ![](/icons/opacity.webp) Remplissage, Contour {#shape-fill-outline}
L'opacité de l'intérieur de la forme et de la ligne qui l'entoure.

### Couleurs {#shape-colors}
La couleur de la forme pour chaque type d'outil : `Masque`, `Masquer`, `Groupe de faces` et `Découper`.

## ![](/icons/array.webp) Répéteurs {#primitive-repeaters}
Des limites pour les copies créées par les [répéteurs](scene#repeaters) (réseau, radial, courbe, surface). Elles gardent Nomad réactif quand un répéteur s'emballe.

### ![](/icons/cube.webp) Copies max. {#repeater-max-copies}
Le nombre maximal de copies créées par un seul répéteur. Nomad peine avec beaucoup d'objets, quelle que soit leur taille.

### ![](/icons/cube.webp) Copies dans la scène {#repeater-scene-copies}
Le budget de copies pour toute la scène. Une copie low poly coûte peu de géométrie mais reste un objet à part entière : c'est donc la limite que les petites copies atteignent en premier.

### ![](/icons/triangle.webp) Nombre max. de faces {#repeater-max-faces}
Le budget de faces pour toutes les copies de la scène. Au-delà, ce sont les objets les plus lourds qui perdent des copies en premier.

## ![](/icons/multires.webp) Multirésolution {#multires}
### Nombre max. de sommets {#multires-lowres-count}
Fixe un seuil au-delà duquel une subdivision multirésolution n'est pas autorisée, car elle ferait probablement planter Nomad : Nomad ne vérifie pas la mémoire disponible avant de subdiviser. La valeur par défaut est de 10 millions.
### Seuil de basse résolution {#multires-lowres-threshold}
Une version moins détaillée du maillage peut s'afficher quand vous déplacez la caméra. Augmentez cette valeur si vous voulez afficher une version plus détaillée du maillage.

## Réglages {#advanced}
### ![](/icons/reset.webp) Rétablir les valeurs par défaut {#reset}
Remet toutes les préférences de l'application à leurs valeurs par défaut.

Certaines ressources sont enregistrées à part et ne sont PAS réinitialisées : les projets, les raccourcis clavier, les préréglages d'outils, les environnements HDR, les MatCaps, les alphas, les textures de pinceau et les images de référence. Tout ce qui est enregistré avec le projet, comme l'éclairage, le post-traitement ou les vues de caméra, est aussi conservé.
