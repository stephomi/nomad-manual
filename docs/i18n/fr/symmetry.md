# ![](/icons/symmetry.webp) Symétrie {#symmetry}

Ce menu contrôle la façon dont les traits sont répétés à travers un plan miroir ou radialement, ainsi que les moyens de restaurer la symétrie sur des objets non symétriques.

![](/images/symmetry_overview.webp) 

## Aperçu {#overview}
Vous pouvez utiliser la symétrie de plusieurs façons :

* Comme un miroir, en reflétant le travail selon X (gauche/droite), Y (haut/bas), Z (arrière/avant), ou une combinaison. 
* La symétrie radiale peut être définie sur X Y Z avec un nombre de répétitions, par exemple pour sculpter une étoile de mer. 
* Les miroirs peuvent fonctionner autour de l’origine (appelé mode monde) ou autour du centre d’un objet (appelé mode local).
* Les sculptures qui ont commencé de manière non symétrique peuvent être forcées à devenir symétriques.

Un raccourci pour activer/désactiver la symétrie se trouve également dans le panneau rapide de gauche (*"Sym"*). Le petit « L/W » indique si Nomad est en mode de symétrie Local ou Monde. Vous pouvez aussi effectuer un appui long ou glisser vers le centre de l’écran pour faire apparaître un menu.

![](/images/symmetry_button.webp) 

Il s’agit d’une option globale, donc l’état sera conservé entre les différents outils.
Les seules exceptions sont les outils de transformation ([Move](#translate), [Rotate](#rotate), [Scale](#scale) et [Gizmo](#gizmo)) qui ont leur propre état de symétrie.

::: tip
Le menu de symétrie sert principalement à contrôler la symétrie des traits. Vous pouvez également refléter et répéter des objets via les [répéteurs situés dans le menu de scène](scene#repeaters). 
:::

## Activé {#enabled}
Active ou désactive le mode miroir, c’est la même chose que le bouton `Sym` dans le panneau rapide de gauche. 

## Plans {#planes}

Activez un ou plusieurs plans de symétrie, et le nombre de répétitions pour la symétrie radiale. Notez que vous n’êtes pas obligé de choisir un seul plan, vous pouvez activer 1, 2 ou 3 plans pour une symétrie complexe.

L’axe et le nombre de répétitions pour la symétrie radiale. Notez que ceux-ci ne sont pas non plus limités à un seul axe, et peuvent même fonctionner en combinaison avec la symétrie par plan pour générer des résultats détaillés très rapidement. (Le nombre total de répétitions est limité à 150)

![](/videos/symmetry_demo.mp4) 

## Méthode {#method}
Le miroir peut être soit « Local » et se déplacer avec l’objet, soit « World » et rester fixe. Si vous n’êtes pas sûr du mode dont vous avez besoin, observez le plan miroir et les indicateurs radiaux superposés à l’objet. En mode local, si vous utilisez le gizmo de transformation et déplacez le modèle, les indicateurs de miroir se déplaceront également. En mode monde, les indicateurs de miroir resteront fixes et l’objet glissera à travers eux.

## Miroir {#mirroring}
![](/images/symmetry_mirroring.webp)

Lors de la sculpture près des plans de symétrie, certains pinceaux peuvent avoir un comportement de symétrie imparfait. Cette section vous permet de restaurer la symétrie en copiant un côté de votre sculpture vers l’autre. 

`Direction` - Les boutons `<<` et `>>` déterminent quel côté sera copié vers l’autre. Nomad calcule cela à partir de votre vue actuelle, donc le réglage sur `<<` par exemple copiera toujours de la droite de l’écran vers la gauche de l’écran.

![](/icons/shield.webp) `Mask` - Le bouton de masque vous permet d’isoler ce qui sera mis en miroir ; masquer le côté de destination protégera cette région, masquer le côté source empêchera cette zone d’être reflétée vers la destination. 

![](/icons/tool_hide.webp) `Hide` - Lorsqu’il est actif, les zones masquées sur le côté source ne seront pas reflétées vers la destination. 

`Mirror` essaiera d’identifier si la topologie est la même des deux côtés du miroir et, si c’est le cas, déplacera simplement les sommets. C’est le scénario le plus courant.

`Split & Mirror` va essentiellement couper l’objet le long du miroir, copier un côté, le refléter de l’autre côté, et souder les sommets le long du miroir. C’est une option plus destructive, et elle supprimera la multirésolution, mais parfois cette méthode est nécessaire si le modèle est très différent de part et d’autre du miroir.

### Retourner l'objet {#flip-object}
![](/images/symmetry_flip.webp)
Fait passer le côté gauche à droite, et inversement. Semblable en apparence au fait d’utiliser le menu de l’outil gizmo et de définir l’échelle à -1 sur X.

## Réinitialiser et éditer {#reset-and-edit}

![](/images/symmetry_edit.webp)

Il est possible de modifier la position et l’orientation de la symétrie (mais ce n’est pas recommandé !). Si nécessaire, `World center` et `Orientation` réinitialiseront la position et l’orientation de la symétrie à leurs valeurs par défaut.

Nomad sait généralement où placer le plan de symétrie. Il n’est pas recommandé de l’ajuster manuellement, mais le bouton `Gizmo (Edit)` le permet pour les utilisateurs avancés. Lorsque ce bouton est cliqué, un gizmo apparaît pour vous permettre de translater et de faire pivoter le plan de symétrie. Si vous souhaitez restaurer le centre et l’orientation par défaut, les boutons `object center` et `orientation` le feront.

Le comportement de ces options changera en fonction de l’espace (*Local/World*) dans lequel vous vous trouvez.
Donc si cela ne fonctionne pas comme vous vous y attendez, assurez-vous de vérifier que vous êtes dans le bon espace.

::: tip
Le bouton `Gizmo (Edit)` est intentionnellement grisé pour vous rappeler que vous ne devriez probablement pas l’utiliser !
:::

## Afficher les options {#show-options}
![](/images/symmetry_show.webp)


`Show line` et `Show plane` activent ou désactivent une superposition dans la vue des emplacements de symétrie. Notez que la désactivation de ces options ne prendra effet que lorsque le menu de symétrie sera fermé.