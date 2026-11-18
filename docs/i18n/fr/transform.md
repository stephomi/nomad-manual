# ![](/icons/transform.webp) Transformation {#transform}

Ce menu affiche la transformation de l'objet sélectionné sous forme de nombres : où il se trouve, comment il est tourné et mis à l'échelle, et quelle est sa taille. Saisissez des valeurs exactes, réinitialisez-les, ou appliquez-les au maillage.

![](/images/transform_overview.webp)

## Présentation {#overview}

En plus de ses sommets, chaque objet a un nœud qui stocke sa translation, sa rotation et son échelle (sa matrice). Les outils [Gizmo](tools.md#gizmo) et [Transformation](tools.md#transform) modifient cette matrice quand vous faites glisser dans la vue ; ce menu vous permet de la lire et de saisir les valeurs à la place. Consultez [Nœuds et sommets](tools.md#nodes-and-vertices) pour la différence entre déplacer le nœud et déplacer les sommets.

Faites glisser une valeur vers la gauche ou la droite pour la modifier, ou touchez-la pour saisir un nombre. Les valeurs X, Y et Z sont teintées en rouge, vert et bleu, comme les axes du gizmo.

::: tip
Saisir des valeurs est pratique pour placer des objets avec précision, par exemple pour mettre plusieurs pièces exactement à la même hauteur, ou pour ramener une rotation à un chiffre rond après une rotation libre au gizmo.
:::

## Matrice {#matrix}

Le titre indique dans quel espace les valeurs sont exprimées : `local` (par rapport à l'objet parent) ou `global`.

### Objet et Pivot {#object-pivot}

* `Objet` - Les valeurs sont la transformation propre de l'objet.
* `Pivot` - Les valeurs pilotent la sélection depuis son [pivot](tools.md#pivot), de la même manière que les poignées du gizmo : les lignes affichent zéro, et les modifier déplace, tourne ou met à l'échelle la sélection autour du pivot. Activez `Modifier` (l'icône de cadenas) pour déplacer le pivot seul, sans que les objets bougent.

### Local et Global {#local-world}

Quand l'objet a un parent ou des enfants, ou que plusieurs objets sont sélectionnés, vous pouvez choisir dans quel espace afficher les valeurs : `Local` (par rapport au parent) ou `Global`.

### Actions {#actions}

| Action        | Icône                         | Description |
| :-----------: | :---------------------------: | :---------- |
| Déplacer l'origine | ![](/icons/target.webp)  | Déplace l'objet à l'origine du monde. |
| Appliquer     | ![](/icons/bake.webp)        | Applique la matrice aux sommets et réinitialise la matrice. Visuellement, rien ne change, mais l'origine de l'objet est désormais l'origine du monde. |
| Pivot         | ![](/icons/gizmo.webp)       | Applique le pivot à l'objet : l'origine et l'orientation de l'objet deviennent celles du pivot. Visuellement, rien ne change. |
| Modifier      | ![](/icons/lock.webp)        | (Mode `Pivot`) Déplace le pivot seul. |
| Réinitialiser | ![](/icons/reset.webp)       | Ramène la transformation à l'identité. En mode `Pivot`, remet plutôt le pivot à sa place. |

Quand l'objet sélectionné a des instances, l'application de la matrice demande une confirmation, avec une option `Désinstancier` : appliquer la matrice modifie les sommets, que les instances partagent.

### Translation, Rotation, Échelle {#translation-rotation-scale}

La position, la rotation (en degrés) et l'échelle de l'objet, sur X, Y et Z. Les deux boutons au bout de chaque ligne appliquent aux sommets uniquement cette partie de la transformation, ou la réinitialisent.

Une ligne `Cisaillement` apparaît aussi quand l'objet est cisaillé, par exemple après une mise à l'échelle non uniforme d'un parent tourné.

### Échelle uniforme {#uniform-scale}

Quand cette option est activée, l'échelle est une seule valeur, identique sur les trois axes. Désactivez-la pour mettre à l'échelle X, Y et Z séparément.

## Dimension {#dimension}

La taille et le centre de la boîte englobante de la sélection, en unités du monde. Si plusieurs objets sont sélectionnés, elle les englobe tous.

* `Taille` - La largeur, la hauteur et la profondeur. Avec le bouton de lien activé, modifier une taille met les deux autres à l'échelle dans la même proportion, ce qui conserve les proportions.
* `Centre` - Le centre de la boîte englobante. Le bouton cible déplace la sélection pour que son centre soit à l'origine du monde.

::: tip
`Taille` est le moyen le plus rapide de donner à un objet une taille réelle, par exemple avant une impression 3d : entrez la hauteur voulue et le lien conserve les proportions.
:::
