# ![](/icons/operation.webp) Opération {#operation}

Ce menu applique une opération à toute la surface des objets sélectionnés d'un seul coup : lisser, relâcher, polir, gonfler, ajuster les couleurs, flouter ou renforcer la netteté de la peinture et du masque.

![](/images/operation_overview.webp)

## Présentation {#overview}

Là où un pinceau agit uniquement où vous tracez, une opération agit sur tous les sommets des objets sélectionnés en une seule fois. Le titre affiche le nom de l'objet, ou le nombre d'objets si plusieurs sont sélectionnés.

Chaque opération est un curseur : faites-le glisser vers la droite pour en appliquer plus, vers la gauche pour en appliquer moins (ou l'opération inverse, pour les curseurs qui ont une flèche de chaque côté). Le curseur revient à zéro dès que vous le relâchez, et chaque glissement compte pour une seule étape dans l'[Historique](history.md) : vous pouvez donc appliquer une opération plusieurs fois, par petites doses.

::: tip
Les opérations sont un moyen rapide de nettoyer tout un maillage après un remaillage voxel ou une opération booléenne : un peu de `Relâcher` régularise les triangles, un peu de `Lisser` enlève le bruit, sans avoir à chercher chaque zone au pinceau.
:::

## Filtres {#filters}

Les boutons du haut limitent les zones où s'appliquent les opérations :

* `Masque` - Les zones masquées restent intactes.
* `Masquer` - Les zones cachées restent intactes.
* `Décalage` - (Quand un [calque](layers.md) est sélectionné) Seules les zones où le calque actif contient de la sculpture sont affectées : vous pouvez ainsi lisser ou gonfler le contenu d'un calque sans toucher au reste.

## Lissage {#smoothing}

* `Préserver le volume` - Lisse sans faire rétrécir la surface. Le bouton en forme de roue dentée contient les valeurs de `Réduire` et `Gonfler` utilisées pour cela.
* `Préserver les bordures` - Les sommets situés sur la bordure du maillage (le bord d'un trou) ne bougent pas.
* `Lissage stable` - Essaie de rendre le lissage indépendant de la topologie. Il fonctionne le mieux quand la densité de polygones varie beaucoup.
* `Lisser` - Lisse la surface. Faites glisser vers la gauche pour appliquer `Netteté` à la place.
* ![](/icons/group.webp) `Lisser` - Lisse les frontières entre [groupes de faces](tools.md#facegroup), ce qui redresse les contours irréguliers des groupes. Faites glisser vers la gauche pour les accentuer.
* `Relâcher` - Régularise les polygones tout en gardant la forme.
* ![](/icons/group.webp) `Relâcher` - Relâche les polygones le long des frontières des groupes de faces.
* `Préserver les coins` - Avec `Lisser` et `Relâcher` sur les groupes de faces, les frontières restent fixes là où elles tournent de plus que cet angle : les coins restent nets pendant que les côtés se lissent. Cochez sa case pour l'activer.

## Polir {#polish}

Aplatit la surface en facettes nettes, comme l'outil [Polir](tools.md#polish). `Angle` détermine quelles faces s'aplatissent ensemble : les faces dont la courbure est inférieure à cet angle forment une seule facette. Un angle plus faible conserve davantage d'arêtes vives et des facettes plus petites.

## Gonfler {#inflate}

Pousse la surface vers l'extérieur le long de ses normales, ou vers l'intérieur quand vous faites glisser vers la gauche. `Normale (Relâcher)` relâche les polygones en même temps, pour qu'ils ne s'étirent pas ; décochez sa case pour le désactiver.

## Ajustements de couleur {#color-adjustments}

Choisissez le canal à ajuster, `Couleur`, `Rugosité`, `Métallité`, `Opacité`, `Densité` (la peinture de densité du [Quad Remesher](tools.md#quad-remesher), si l'objet en a) ou `Masque`, puis :

* `Exposition` - Éclaircit ou assombrit les valeurs.
* `Saturation` - (`Couleur` uniquement) Des couleurs plus ou moins vives.
* `Contraste` - Écarte les valeurs les unes des autres, ou les rapproche.
* `Teinte` - Fait tourner les couleurs sur le cercle chromatique.

## Flou {#blur}

Floute les canaux sélectionnés sur toute la surface : activez `Couleur`, `Rugosité`, `Métallité`, `Opacité`, `Densité` ou `Masque`, puis faites glisser `Flou`. Faites glisser vers la gauche pour appliquer `Netteté` à la place.

Pour le masque, c'est la même chose que le curseur `Flou` de l'outil [Masque](tools.md#mask). Ici, vous pouvez aussi flouter les canaux de peinture.
