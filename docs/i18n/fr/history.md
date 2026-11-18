# ![](/icons/history.webp) Historique {#history}
![](/images/history_overview.webp)

Comme la plupart des outils de création, Nomad vous permet d'annuler et de rétablir toutes vos modifications.
L'historique peut devenir volumineux : vous choisissez donc quelle part reste en mémoire, quelle part est conservée sur le stockage, et s'il est enregistré avec votre projet.

::: tip
Des gestes rapides permettent d'annuler et de rétablir :
- Touchez avec 2 doigts pour annuler
- Touchez avec 3 doigts pour rétablir
:::

## ![](/icons/history.webp) Historique {#history-panel}
![](/images/history_history.webp)

Ce panneau affiche la pile de l'historique : le numéro de chaque étape, le nom de l'opération, l'objet concerné et la mémoire occupée par cette étape.

Touchez une entrée pour revenir en arrière (ou avancer) jusqu'à cet état. Un appui long sur une entrée la supprime définitivement, avec tout l'historique plus ancien : un moyen rapide de libérer de la mémoire une fois satisfait de votre sculpture.

### ![](/icons/speed.webp) Rejouer {#replay}
Le bouton de lecture en bas à gauche revient à la base, puis rétablit les opérations une par une : une façon amusante de voir votre sculpture prendre forme. Le curseur règle la vitesse, en opérations par seconde. Touchez à nouveau le bouton pour arrêter ; une annulation, un rétablissement ou un appui sur une entrée l'arrêtent aussi.

Avant le démarrage, une fenêtre vous laisse choisir :
* `Inverser` - Annule depuis l'état actuel jusqu'à la base, au lieu de rejouer depuis la base.
* `Restaurer la caméra` - La caméra suit les opérations rejouées, même quand [Restaurer la caméra](#restore-camera) est désactivé.
* `Lissage de la caméra` - La caméra glisse d'un point de vue à l'autre au lieu de sauter de l'un à l'autre. Plus la valeur est élevée, plus la caméra est calme.

::: warning
La fonction Rejouer est expérimentale.
:::

## Actions incluses {#include-actions}

Les icônes en bas du panneau Historique choisissent quels types de modifications sont enregistrés dans l'historique :

| Action          | Icône                         | Description                                                                         |
| :-------------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Lumières        | ![](/icons/light.webp)        | Les modifications de lumières. Déplacer une lumière avec le Gizmo est toujours enregistré, car cela peut affecter d'autres objets de la hiérarchie de la scène |
| Ombrage         | ![](/icons/sun.webp)          | Les modes PBR, MatCap et Unlit, les MatCaps et les HDRI                             |
| Post-traitement | ![](/icons/postprocess.webp)  | Les modifications du post-traitement                                                |
| Sélection       | ![](/icons/tool_lattice.webp) | Les modifications de sélection du Treillis, comme les clics, les sélections au lasso et la désélection |

## Réglages {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Restaurer la caméra {#restore-camera}
Pour chaque opération, le point de vue de la caméra est enregistré.
Si vous activez cette option, annuler ou rétablir une opération replace la caméra sur le point de vue enregistré.

### ![](/icons/history.webp) Enregistrer l’historique {#save-history}
Conserve l'historique d'annulation à l'enregistrement du projet, pour le retrouver quand vous rouvrez le projet. Désactivez-le pour garder des fichiers de projet plus légers.

### ![](/icons/ram.webp) Limite de RAM {#history-limit-mb}
La quantité maximale d'historique gardée en RAM. Les états plus anciens sont déplacés sur le stockage et rechargés au besoin : ils ne sont pas supprimés.

### ![](/icons/save.webp) Limite de stockage {#storage-limit}
L'espace de stockage maximal utilisé par l'historique de ce projet. Une fois la limite atteinte, les opérations les plus anciennes sont supprimées définitivement.

::: tip
Une nouvelle limite prend effet après la prochaine modification, annulation ou rétablissement.
:::

### ![](/icons/undo.webp) Avertissement d’annulation {#maximum-undoable}
Revenir en arrière de plus de ce nombre d'opérations d'un coup demande d'abord une confirmation. Si vous faites ensuite une modification, toutes les opérations après ce point sont perdues : cette option vous protège donc d'un appui accidentel tout en bas de la liste.

## Statistiques mémoire {#memory-stats}

Cette section détaille la mémoire utilisée par Nomad.
