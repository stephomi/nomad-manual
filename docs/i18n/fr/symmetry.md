# ![](/icons/symmetry.webp) Symétrie {#symmetry}

Ce menu détermine comment les traits sont répétés de l'autre côté d'un plan miroir, en radial ou en pavage, et propose des moyens de rétablir la symétrie sur des objets qui ne sont pas symétriques.

![](/images/symmetry_overview.webp) 

## Présentation {#overview}
Vous pouvez utiliser la symétrie de plusieurs façons :

* En miroir, en reproduisant votre travail selon X (gauche/droite), Y (haut/bas), Z (arrière/avant), ou une combinaison des trois. 
* La symétrie radiale peut être réglée sur X, Y et Z avec un nombre de répétitions, par exemple pour sculpter une étoile de mer. 
* Le pavage répète vos traits sur l'objet, pour que la sculpture se raccorde sans couture.
* Les miroirs peuvent fonctionner autour de l'origine (mode global) ou autour du centre d'un objet (mode local).
* Une sculpture commencée sans symétrie peut être rendue symétrique de force.

Un raccourci pour activer ou désactiver la symétrie se trouve aussi dans le panneau rapide de gauche (*« Sym »*). Le petit « L/W » indique si Nomad est en mode de symétrie Local ou Global. Vous pouvez aussi appuyer longuement ou glisser vers le centre de l'écran pour faire apparaître un menu.

![](/images/symmetry_button.webp) 

Les réglages de symétrie sont enregistrés avec chaque objet, et le titre du menu affiche le nom de l'objet que vous modifiez.
Les outils de sculpture partagent le même état activé/désactivé, tandis que les outils de transformation ([Transformation](tools.md#transform) et [Gizmo](tools.md#gizmo)) ont le leur.

::: tip
Le menu Symétrie sert surtout à contrôler la symétrie des traits. Vous pouvez aussi mettre en miroir et répéter des objets grâce aux [répéteurs du menu Scène](scene#repeaters). 
:::

## ![](/icons/symmetry.webp) Activée {#enabled}
Active ou désactive le mode miroir ; c'est la même chose que le bouton `Sym` du panneau rapide de gauche. Une icône d'avertissement vous rappelle quand il est désactivé, et le menu vous indique aussi quand l'outil actuel ignore la symétrie.

## Plans {#planes}

Activez un ou plusieurs plans de symétrie, et le nombre de répétitions pour la symétrie radiale. Vous n'êtes pas obligé de choisir un seul plan : vous pouvez en activer 1, 2 ou 3 pour une symétrie complexe.

La ligne `Radial` règle le nombre de répétitions de la symétrie radiale autour de chaque axe. Là non plus, vous n'êtes pas limité à un seul axe, et vous pouvez même les combiner avec la symétrie plane pour obtenir très vite des résultats détaillés. (Le nombre total de répétitions est limité à 200.)

![](/videos/symmetry_demo.mp4) 

## Pavage {#tile}

Répète vos traits le long d'un axe, à intervalle régulier, pour que la sculpture se raccorde sans couture. Pratique pour des motifs, des briques, ou une texture que vous comptez répéter.

Activez le pavage sur chaque axe avec les boutons `Pavage`, puis réglez soit un `Nombre` (combien de répétitions couvrent l'objet), soit une `Distance` (l'espace entre deux répétitions). Touchez l'interrupteur à gauche pour passer de l'un à l'autre.

## Méthode {#method}
Le miroir peut être `Local`, et suivre l'objet, ou `Global`, et rester immobile. Si vous ne savez pas quel mode choisir, observez les indicateurs de plan miroir et de symétrie radiale affichés sur l'objet. En mode local, si vous utilisez les outils de transformation (`Gizmo` ou `Transformation`) pour déplacer le modèle, les indicateurs du miroir se déplacent avec lui. En mode global, les indicateurs restent fixes et l'objet glisse à travers eux.

## Miroir {#mirroring}
![](/images/symmetry_mirroring.webp)

Quand vous sculptez près des plans de symétrie, certains pinceaux n'ont pas une symétrie parfaite. Cette section vous permet de rétablir la symétrie en copiant un côté de votre sculpture sur l'autre. 

`Direction` - Les deux boutons fléchés à côté du titre `Miroir` déterminent quel côté sera copié sur l'autre. Nomad le calcule à partir de la vue actuelle : le côté reste donc le même à l'écran, quel que soit l'angle sous lequel vous regardez le modèle.

![](/icons/shield.webp) `Masque` - Le bouton de masque vous permet d'isoler ce qui sera mis en miroir : masquer le côté de destination protège cette zone, masquer le côté source empêche cette zone d'être copiée vers la destination. 

![](/icons/tool_hide.webp) `Masquer` - Quand il est actif, les zones cachées du côté source ne sont pas copiées vers la destination. 

`Miroir` (Conserver la topologie) essaie de déterminer si la topologie est la même des deux côtés du miroir et, si c'est le cas, se contente de déplacer les sommets. C'est le cas le plus courant. La symétrie radiale est ignorée. Si la topologie n'est pas symétrique, Nomad propose de forcer la mise en miroir avec `Couper • Miroir` à la place.

Les boutons `Couper` coupent l'objet le long du ou des plans de symétrie. Ils modifient la topologie, ils sont donc plus destructifs que `Miroir`. Le nombre sur chaque bouton indique combien d'objets vous obtenez :

* `Couper` - supprime un côté de l'objet.
* `Couper • Miroir` - coupe l'objet, copie un côté, le reproduit en miroir de l'autre côté et soude les sommets le long du miroir. Cette méthode est parfois nécessaire si le modèle est très différent d'un côté à l'autre.
* `Couper • Scinder` - coupe l'objet et garde chaque côté comme un objet séparé.
* `Couper • Miroir • Scinder` - comme `Couper • Miroir`, mais chaque côté devient un objet séparé.

Si plusieurs objets sont sélectionnés, `Miroir` et [Inverser l'objet](#flip-object) s'appliquent à tous.

### Inverser l'objet {#flip-object}
![](/images/symmetry_flip.webp)
Fait passer le côté gauche à droite, et inversement, selon `X`, `Y` ou `Z`. Le résultat ressemble à ce que vous obtiendriez en réglant l'échelle à -1 sur X dans le menu de l'outil Gizmo.

## Réinitialiser et modifier {#reset-and-edit}

![](/images/symmetry_edit.webp)

Il est possible de modifier la position et l'orientation de la symétrie (mais ce n'est pas recommandé !). Si besoin, `Centre de la scène` (`Centre de l'objet` en mode local) et `Orientation` remettent la position et l'orientation de la symétrie à leurs valeurs par défaut.

Nomad sait généralement où placer le plan de symétrie. Il n'est pas recommandé de l'ajuster à la main, mais le bouton `Éditer au Gizmo` le permet aux utilisateurs avancés. Quand vous touchez ce bouton, un gizmo apparaît pour déplacer et tourner le plan de symétrie. Pour revenir au centre et à l'orientation par défaut, utilisez les boutons de réinitialisation ci-dessus.

`Depuis le pivot` place le plan de symétrie sur le pivot de l'outil [Gizmo](tools.md#gizmo). Il n'est disponible que lorsque l'outil `Gizmo` est actif.

Le comportement de ces options change selon l'espace (*Local/Global*) dans lequel vous êtes.
Donc si le résultat n'est pas celui attendu, vérifiez que vous êtes dans le bon espace.

::: tip
La modification du plan de symétrie au gizmo est un peu expérimentale, vous ne devriez normalement pas en avoir besoin !
:::

## Options d'affichage {#show-options}
![](/images/symmetry_show.webp)


`Afficher la ligne` et `Afficher le plan` affichent ou masquent dans la vue un repère des emplacements de symétrie. Notez que la désactivation de ces options ne prend effet qu'une fois le menu Symétrie fermé.
