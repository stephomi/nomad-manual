# ![](/icons/cog.webp) Paramètres 

Le menu des paramètres contient de nombreuses options pour contrôler l’apparence et le comportement de Nomad.

![](/images/settings_overview.webp)

## Paramètres d’affichage
Cette section contient des raccourcis de lancement rapide pour la plupart des paramètres plus bas dans ce menu.

![](/images/settings_display_settings.webp)

### Lissage (Smooth Shading) 
Active ou désactive le lissage ou l’ombrage facetté. En mode facetté, les polygones sont ombrés indépendamment, ce qui permet de voir la topologie sous-jacente.  
Il peut être utile de voir l’ombrage facetté pendant la phase de sculpture, puis de passer au lissage pour le rendu.

Désactiver le lissage améliore légèrement les performances.

### Contour (Outline)
Active ou désactive un contour sur votre sélection actuelle.

C’est utile pour obtenir un retour visuel sur le ou les maillages actuellement sélectionnés au cas où [Assombrir les objets non sélectionnés](#darken-unselected-objects) est désactivé.

D’un point de vue performance, utiliser [Assombrir les objets non sélectionnés](#darken-unselected-objects) est bien meilleur que la solution de contour.

### Grille
Active ou désactive une grille d’arrière-plan, utile pour comprendre le placement et l’échelle des objets.

### Double face (Two sided)
Active ou désactive l’affichage double face des polygones. Toutes les faces pointent dans une certaine direction.  
Les faces considérées comme *dos de face* (backface) sont celles qui pointent « à l’opposé » du point de vue de la caméra.

Par exemple, la sphère simple au démarrage aura ses faces orientées vers l’extérieur.  
Si vous déplacez la caméra à l’intérieur de la sphère, vous verrez alors le dos de ces faces.

La plupart du temps, vous ne devriez pas voir le dos des faces, donc les colorer peut vous aider à détecter des problèmes potentiels ou une topologie incorrecte.

Désactiver le rendu `double face` peut améliorer un peu les performances de rendu.


### Fil de fer (Wireframe)
Active ou désactive une superposition en fil de fer.

Notez que l’activation du fil de fer réduit les performances.

### Cube de capture (Snap cube)
Active ou désactive une icône d’aide dans le coin de la scène, utile pour vous orienter dans l’espace et passer rapidement entre les vues avant/arrière/gauche/droite/haut/bas.

### Afficher la peinture (Show Painting)
Active ou désactive l’affichage de la peinture. La peinture par défaut est un matériau blanc non métallique, avec 25 % de rugosité.

### Utiliser le masquage de géométrie (Use Hide)
Active ou désactive le mode de masquage de géométrie. Lorsqu’il est désactivé, il reste disponible mais inactif. Ce bouton est désactivé si vous utilisez actuellement l’outil de masquage de géométrie (hide).

### Afficher le masque (Show Mask)
Active ou désactive le mode masque. Lorsqu’il est désactivé, il reste disponible mais inactif. Appuyez à nouveau sur ce bouton pour le réactiver.

Si vous avez besoin de cacher le masque TOUT en le gardant actif, utilisez la couleur de masque ci‑dessous et réglez‑la sur blanc. N’oubliez pas de la remettre sur un gris lorsque vous avez terminé !

Notez que ce bouton est désactivé si vous utilisez actuellement un outil de masque. 

### Masque -> Opaque
Masque -> opaque ignorera les sommets transparents pour les masques. Ceci n’est pertinent que pour l’opacité par sommets ou par texture ; les faces cachées par « hide » resteront cachées.

### Surlignage (Highlight)
Active ou désactive le flash de surbrillance de la sélection. Lors de la sélection d’objets, l’objet sélectionné clignote temporairement en rose vif pendant 500 millisecondes. La couleur et la durée du flash peuvent être personnalisées ci‑dessous.

### Statistiques (Stats)
Active ou désactive l’affichage du texte d’état dans la vue 3D. Cela affiche des informations sur la mémoire de votre système, le nombre total de sommets de la scène, et le nombre de sommets de la sélection actuelle.

----- 

### Assombrir les objets non sélectionnés
Les objets qui ne sont pas sélectionnés seront assombris afin que la sélection actuelle ressorte davantage.

### Masque
La couleur utilisée pour le masquage, par défaut un gris moyen, multipliée par la couleur de votre objet. Réglez‑la sur blanc pour rendre le masque invisible, mais n’oubliez pas de la remettre sur un gris lorsque vous avez terminé !

## ![](/icons/cursor.webp) Curseur

### Afficher le cercle pendant la sculpture
Continue d’afficher le rayon du pinceau pendant la sculpture.

### Afficher le petit point
Affiche un point au centre du trait de pinceau pendant la sculpture, ou lorsque le pivot de la caméra est modifié.

### Afficher le stabilisateur corde
Trace une ligne pour indiquer la longueur de la corde lorsque le stabilisateur « lazy rope » est actif dans les paramètres de trait.

## ![](/icons/cursor.webp) Indicateur
![](/images/settings_indicator.webp)

Affiche un ou plusieurs indicateurs visuels pour les tutoriels et les captures d’écran.

Les boutons `Finger`, `Stylus` et `Mouse` permettent d’afficher une icône lorsque ce type d’entrée est détecté.

### Couleur
La couleur de l’indicateur.

### Taille/Icône/Cercle
Contrôles pour ajuster la taille de l’indicateur et les formes à l’intérieur de l’indicateur.

## ![](/icons/wireframe.webp) Fil de fer
![](/images/settings_wireframe.webp)
Active la superposition en fil de fer.

### Cible (Target)
Définit si les objets non sélectionnés afficheront le fil de fer, ou seulement les objets sélectionnés, ou tous les objets.

### Masqué (Hide)
Définit si le fil de fer sera toujours affiché pour les polygones masqués.

### Multirésolution : niveau 0 uniquement
La multirésolution affichera les fils de fer pour le niveau 0 plus foncés, et les niveaux supérieurs progressivement plus clairs. Lorsqu’elle est activée, cette option n’affichera que le fil de fer du niveau 0.

### Couleur
Définit la couleur et l’opacité du fil de fer.

## ![](/icons/grid.webp) Grille
![](/images/settings_grid.webp)
Active la grille.

### Couleur
Définit la couleur et l’opacité de la grille.

### Accrochage (Snap)
Active l’accrochage à la grille pour les outils basés sur les courbes.

## ![](/icons/culling.webp)Two sided
Active la visibilité des faces de polygones des deux côtés.

### Colorer le dos des faces, Couleur du dos des faces (Backface Color)
Active la teinte des dos de faces, et la couleur de cette teinte.

## ![](/icons/outline.webp)Outline
Active un contour autour de l’objet actif.

### Couleur du contour, Épaisseur
Définit la couleur et l’épaisseur du contour.


## ![](/icons/bang.webp) Surlignage
Active un court flash lorsque l’objet actif est modifié.
### Couleur, Durée
Définit la couleur et la durée du flash en millisecondes.

## ![](/icons/snap_cube.webp) Cube de capture
![](/images/settings_snapcube.webp)

Affiche une icône d’aide dans le coin de la scène, utile pour passer rapidement entre les vues avant/arrière/gauche/droite/haut/bas. Touchez les faces du cube pour passer entre les vues orthographiques.

### Forme
Choisissez entre une forme de cube, de sphère ou de gnomon pour le cube de capture.

### Restreindre l’alignement
Active le verrouillage de la rotation de la caméra lors du glisser sur le cube de capture. Lorsqu’il est actif, un mouvement de glisser sur le cube de capture ne se fera qu’à gauche/droite ou haut/bas.

### Taille
Définit la taille du cube de capture.

### Rotation 180 (Flip 180)
Active un comportement au toucher de sorte que si la vue est verrouillée, toucher le centre du cube fera pivoter la vue de 180 degrés. Par exemple, si la vue est verrouillée sur l’avant, toucher le cube de vue fera pivoter vers la vue arrière.

### Position
Définit dans quel coin se trouvera le cube de capture.


## ![](/icons/edit_radius_n.webp) Statistiques
![](/images/settings_stats.webp)

Affiche des informations sur la mémoire de votre système, le nombre total de sommets de la scène, et le nombre de sommets de la sélection actuelle.

### Position
Définit dans quel coin les statistiques seront affichées.

## Primitif/Répétiteurs
## Saisie numérique
Autorise la saisie numérique en touchant les widgets du gizmo.

## Multirésolution
### Nombre maximal de sommets
Définit un seuil pour ne pas autoriser une opération de subdivision multirésolution au‑delà de ce nombre de polygones, ce qui risquerait de faire planter Nomad. La valeur par défaut est de 10 millions.
### Seuil de basse résolution
Une résolution plus basse du maillage peut être affichée lorsque vous déplacez la caméra. Vous pouvez augmenter cette valeur si vous souhaitez afficher une résolution plus élevée du maillage.

## Paramètres
### Réinitialiser par défaut
Réinitialise tous les paramètres à leurs valeurs par défaut.
