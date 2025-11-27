# ![](/icons/history.webp) Historique
![](/images/history_overview.webp)

Comme pour la plupart des outils de création de contenu, vous pouvez annuler/rétablir toutes les modifications dans Nomad.
Il existe une limite au nombre d’opérations pouvant être annulées, mais vous pouvez contrôler ce comportement.

::: tip
Vous pouvez utiliser des gestes rapides pour annuler/rétablir :
- Tapez avec 2 doigts pour annuler
- Tapez avec 3 doigts pour rétablir
:::

## Historique
![](/images/history_history.webp)

Ce panneau affiche la pile d’historique, indiquant le nombre d’étapes, le nom de l’opération et la quantité de mémoire utilisée par cette étape.

## Paramètres
![](/images/history_settings.webp)

### Limite d’historique (Mo)
Si la pile d’historique dépasse cette valeur, les opérations les plus anciennes seront supprimées afin que le budget mémoire respecte cette limite.


### Nombre maximum d’annulations
Vous pouvez contrôler le nombre maximal d’opérations.

## Restaurer la caméra
Pour chaque opération, le point de vue de la caméra est enregistré.
Si vous activez cette option, annuler ou rétablir une opération réinitialisera la caméra au point de vue enregistré.

## Inclure les actions

* `Lumières` - Lorsque cette option est désactivée, les opérations sur les lumières (à part les déplacements de gizmo) seront ignorées par la pile d’historique
* `Matcaps & HDRIs` - Lorsque cette option est désactivée, les changements de matcaps et d’HDRI seront ignorés par la pile d’historique
* `PostProcess` - Lorsque cette option est désactivée, les changements des options de post-traitement seront ignorés par la pile d’historique

## Statistiques de mémoire

Cette section fournit une répartition de la mémoire utilisée par Nomad.
