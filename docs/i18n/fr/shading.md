# ![](/icons/sun.webp) Ombrage {#shading}

Ce menu contrôle les modes d’ombrage utilisés par Nomad, les propriét��s d’éclairage, ainsi que les propriétés de lumière d’environnement/matcap.

![](/images/shading_overview.webp)



Vous pouvez choisir entre plusieurs modes de rendu :

| Mode                        | Signification              | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Rendu Physiquement Réaliste | Peinture avec métallicité/rugosité                              |
| [Matcap](#matcap)           | Material Capture           | Utilisé pendant la sculpture, avec une charge GPU/CPU plus faible que le PBR |
| [Unlit](#unlit)             | Couleur de surface         | Couleur de surface uniquement, sans ombrage ni éclairage        |
| [Object Id](#object-id)      | ID d’objet                 | Une couleur aléatoire par objet, utile pour les logiciels de peinture |
| [Instance Id](#instance-id)  | ID d’instance              | Une couleur aléatoire par instance, utile pour identifier les maillages partagés |

Pour en savoir plus sur la métallicité et la rugosité, voir la section [Peinture de sommets](painting.md).

---

![](/images/shading_second.webp)

### Groupe de faces {#face-group}
Superpose les couleurs des groupes de faces. Les groupes de faces sont des sélections colorées de polygones qui peuvent être créées avec l’outil [Face group](tools#facegroup), et sont générées automatiquement avec la plupart des primitives.

Certains outils filtreront automatiquement par groupes de faces lorsque ceux‑ci sont visibles.

### Afficher la peinture {#show-paint}
Nomad peut stocker la couleur, la rugosité et la métallicité dans les sommets de votre sculpture. Vous pouvez activer/désactiver l’affichage de ces propriétés globalement avec cette case à cocher.

Notez que si vous avez à la fois des propriétés de sommets et des textures, et que les deux sont activées, les valeurs seront multipliées entre elles.

### Afficher le masque {#show-mask}
Active/désactive la superposition en niveaux de gris du masque des [outils de masque](tools#mask). Quand ceci est désactivé, le masque est également désactivé, ce qui est utile pour faire des modifications rapides sans le masque, puis vous pouvez le réactiver sans perdre votre masque.

### Utiliser Cacher {#use-hide}

Active/désactive les faces cachées. Notez que cela ne fonctionne que si vous n’êtes PAS dans l’outil de masquage/cachage !

### Utiliser les textures {#use-textures}

Nomad permet d’assigner des textures aux objets depuis le menu [material](material). Si des textures sont assignées, elles peuvent être activées/désactivées globalement avec cette case à cocher.







### Vue d’ensemble PBR et lumières {#pbr}
Ce manuel n’entrera pas dans les détails du rendu physiquement réaliste (PBR).

Un point important à garder à l’esprit est que l’éclairage et le matériau sont complètement séparés.
Cela signifie que vous pouvez peindre la couleur, la rugosité et la métallicité de votre objet tandis que l’éclairage est géré indépendamment.
Cela vous permet de peindre votre objet puis d’ajuster l’éclairage plus tard, sans casser l’apparence générale de votre modèle.

Les lumières ne sont disponibles qu’avec le [mode PBR](#pbr).
Pour des raisons de performance, vous êtes limité à 4 lumières seulement.

::: tip
Vous pouvez charger un fichier glTF contenant plus de 4 lumières et Nomad les conservera toutes.
Cependant, les performances ne seront pas forcément bonnes.
:::

::: tip
Vous pouvez simuler de nombreuses lumières en rendant des objets non éclairés/émissifs, puis en activant l’illumination globale dans le menu [post process](postprocess).
:::

### Vue d’ensemble des types de lumière {#light-types-overview}

Voici les types de lumières actuellement pris en charge :

| Mode                        | Description                                             | Peut projeter des ombres                                   |
| :-------------------------: | :-----------------------------------------------------: | :--------------------------------------------------------: |
| [Directional](#directional) | Lumière solaire à distance infinie                     | oui                                                        |
| [Environment](#environment) | Lumière distante correspondant à l’environnement HDR   | oui                                                        |
| [Spot](#spot)               | Lumières en forme de cône                              | Oui                                                        |
| [Point](#point)             | Point lumineux omnidirectionnel                        | Oui, mais uniquement via des ombres en espace‑écran moins robustes |

#### Directionnelle {#directional}
Elle émet de la lumière depuis une distance infinie, avec une intensité uniforme.
Sa position 3D dans la scène n’a pas d’importance, seule son orientation compte.

Vous pouvez attacher cette lumière à la caméra, de façon à obtenir un éclairage constant.  
Par exemple, vous pouvez l’utiliser pour créer un « rim light » (une lumière forte qui vient de l’arrière de votre modèle, pointant vers la caméra) qui éclaire toujours l’arrière de votre modèle.

#### Lumière d’environnement {#env-light}
L’utilisation d’un [HDR d’environnement](#environment) fonctionne bien pour un éclairage global doux, mais si une source lumineuse forte et nette est visible dans le HDR, l’ombre créée sera très douce, souvent à peine visible. Utiliser une lumière directionnelle en combinaison avec le HDR d’environnement peut aider, mais il peut être difficile de les aligner.

Cette lumière fait le travail pour vous. Elle sera automatiquement orientée pour s’aligner avec la partie la plus lumineuse du HDR, puis vous pouvez contrôler séparément son intensité et son angle (douceur des ombres). 

#### Spot {#spot}
Une lumière spot émet de la lumière dans une seule direction, limitée par une forme de cône.

#### Point {#point}
Une lumière ponctuelle émet de la lumière dans toutes les directions.  
Pour le moment, la lumière ponctuelle ne prend pas en charge les ombres.

#### Ombres {#shadows}
L’option `normal bias` peut être utilisée pour réduire les artefacts d’ombre courants (acné/peter‑panning).

La qualité des ombres dépend de la taille des objets par rapport à l’ensemble de la scène.  
Si vous avez un grand objet dans votre scène qui n’a pas besoin de projeter des ombres (par exemple un grand plan), assurez‑vous de désactiver la projection d’ombres dans ses [paramètres de matériau](material.md#cast-shadows).

## Lumières {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Case à cocher Lumières {#lights-checkbox}

Active/désactive toutes les lumières directes de la scène.



### Ajouter une lumière {#add-light}

Ajoute une lumière à la scène, jusqu’à un maximum de 4. Lorsqu’une lumière est ajoutée, la liste des lumières s’affiche avec des boutons, et une barre d’outils de lumière est ajoutée en haut de la vue.

![](/images/shading_lights_icons.webp)

* Le texte affiche le nom de la lumière et sa luminosité.
* L’icône en forme d’œil active/désactive la visibilité.
* L’icône de crayon permet de renommer la lumière.
* L’icône de corbeille supprime une lumière.
* L’icône de copie duplique une lumière. 
* L’icône à 3 points ouvre un éditeur de lumière complet. La plupart de ces fonctionnalités sont également disponibles depuis la barre d’outils qui apparaît dans la vue.

### ![](/icons/spotlight.webp)  Icônes {#icons}

Active/désactive l’affichage des icônes de lumière dans la vue.

### Barre d’outils Lumière {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Cette barre d’outils apparaît en haut de la vue lorsqu’une lumière est sélectionnée.

* Show active/désactive la visibilité de la lumière.
* Directional/Environment/Spot/Point change le type de lumière. Touchez pour faire défiler, ou faites un appui long pour voir un menu.
* Intensity contrôle la puissance de la lumière, la valeur peut dépasser 1,0 pour des lumières très intenses, utile lorsqu’elles sont utilisées avec l’illumination globale dans Post Process.
* Le nuancier de couleur, lorsqu’on clique dessus, ouvre un sélecteur de couleur. Nomad propose plusieurs façons de choisir une couleur. Le contrôle en Kelvin offre une manière naturelle de sélectionner un éclairage chaud/froid.
* Shadow active/désactive les ombres.
* Size définit la largeur d’une lumière. Des lumières plus larges projettent des ombres plus douces, un éclairage plus doux et un reflet plus diffus sur les objets.
* ... ouvre des contrôles supplémentaires.

### Contrôles supplémentaires de la lumière {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Notez que certaines options sont spécifiques à certains types de lumières.

* `Clone` duplique la lumière.
* `Recenter` ramène la lumière à l’origine.
* `Delete` supprime la lumière.
* `Directional/Environment/Spot/Point` permettent de changer le type de lumière.
* Le `nuancier de couleur`, lorsqu’on clique dessus, ouvre un sélecteur de couleur. 
* `Intensity` contrôle la puissance de la lumière.
* `Attachment` (_directional uniquement_) définit si la lumière est parentée au monde ou à la caméra. Par exemple, si vous utilisez une lumière directionnelle derrière votre personnage comme rim light, lorsque « attachment as camera » est sélectionné, la rotation de la caméra gardera toujours la lumière derrière le personnage.
* `Angle` (_directional et environment uniquement_) est la taille apparente de la lumière, pensez‑y comme à la taille du soleil dans le ciel. Des angles plus grands projettent des ombres plus douces et des reflets plus larges.
* `Softness` (_spotlight uniquement_) contrôle la netteté du bord du cône du spot. 0 donne un bord très net. 1 est très doux, avec un dégradé vers le centre du cône lumineux. Dans la vue, le petit point bleu sur le cône du spot peut être utilisé pour régler la douceur de manière interactive.
* `Cone angle` (_spotlight uniquement_) contrôle l’angle d’ouverture du spot. Un petit angle donne un faisceau de lumière très fin, 170 donne une diffusion de lumière très large. Dans la vue, le point orange peut être utilisé pour régler l’angle du cône de manière interactive.
* `Shadow` active/désactive les ombres pour la lumière courante.
* `Shadow map` et `screenspace` sont différentes méthodes de calcul des ombres, en général « shadow map » est plus fiable.
* `Contact` ajuste la façon dont les ombres sont calculées. Les ombres sont un problème difficile en infographie et peuvent provoquer des artefacts de rendu. Des ombres plus précises peuvent être sélectionnées pour la lumière la plus importante d’une scène ; ce contrôle détermine si cette lumière est sélectionnée automatiquement par Nomad ou par l’utilisateur.
* `Tolerance` si des artefacts d’ombre sont visibles (soit les ombres ne semblent pas toucher les surfaces, soit il y a du bruit et des motifs dans les ombres), ajuster la tolérance peut aider à corriger ces problèmes.


## Environnement {#environment}

![](/images/shading_environment.webp)

Dans le monde réel, la lumière vient de toutes les directions ; le bleu du ciel, le vert de l’herbe, le rouge d’un bâtiment, toute cette lumière provenant de « l’environnement » peut être simulée avec une carte d’environnement. 

Nomad est livré avec plusieurs exemples de cartes d’environnement pour des scènes intérieures et extérieures, avec différentes teintes et niveaux de luminosité. Essayez différentes cartes pour voir lesquelles font le mieux ressortir les détails de vos sculptures.

Touchez l’image pour voir les cartes d’environnement disponibles. Depuis cette boîte de dialogue, choisissez « Import... » pour charger les vôtres. Il est préférable d’utiliser des images à grande plage dynamique (HDR), au format latlong ou équirectangulaire, en fichiers .hdr ou .exr. [www.polyhaven.com](https://polyhaven.com/hdris) propose une bonne collection de cartes d’environnement gratuites, en général les cartes HDR 1k offrent une bonne taille et une bonne qualité.

### Exposition {#env-exposure}
Ajuste la luminosité de la carte d’environnement. Souvent, les cartes peuvent être trop lumineuses lorsqu’elles sont utilisées avec des lumières classiques ; réduire l’exposition peut aider à équilibrer, en particulier lorsqu’elles sont utilisées avec l’illumination globale dans les paramètres de [Post Process](postprocess).

### Rotation {#env-rotation}

Comme les cartes d’environnement capturent la lumière venant de toutes les directions, vous pouvez les faire pivoter pour obtenir des reflets et un éclairage global qui se combinent bien avec votre sculpture.

### Attaché à la caméra {#env-attached}
Attache l’environnement à la caméra.

Cela force l’éclairage à rester constant, ce qui peut être utile pendant la sculpture.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Comme son nom l’indique (MATerial CAPture), un matcap gère à la fois l’éclairage et les informations de matériau dans une seule image.
Puisque le matériau lui‑même est déjà présent dans le matcap, les canaux de peinture de rugosité et de métallicité seront ignorés.
La couleur de peinture sera multipliée par le matcap, ce qui signifie que si vous avez un matcap noir/gris, utiliser une peinture blanche ne le rendra pas plus lumineux.

Les artistes ont tendance à privilégier ce mode pour la sculpture, car il leur permet de se concentrer sur la forme et la géométrie elles‑mêmes.

Toucher la sphère ouvre un explorateur d’images. Vous pouvez également ajouter votre propre matcap ; en général, n’importe quelle photo, rendu, voire une peinture d’une sphère recadrée serrée dans un carré peut être utilisée. De nombreuses bibliothèques de matcaps sont disponibles en ligne, une ressource utile est la [bibliothèque de matcaps de nidorx](https://github.com/nidorx/matcaps).

### Utiliser le Matcap global {#matcap-global}

En général, les artistes utilisent un seul matcap pour l’ensemble de la sculpture, mais si ce bouton est désactivé, chaque objet peut avoir son propre matcap. Cela peut être utilisé de manière artistique pour obtenir des résultats saisissants.

::: tip
Désactivez cette option et utilisez une image de globe oculaire pour les yeux de vos personnages !
:::

### Rotation {#matcap-rotation}
Un matcap est une forme spécialisée de carte d’environnement, donc comme une carte d’environnement, il peut être pivoté. Vous pouvez également le faire à tout moment dans la vue en faisant glisser avec 3 doigts vers la gauche ou la droite.



## ![](/icons/circle_fill.webp) Non éclairé {#unlit}

Ce mode n’affiche que la couleur de surface. Il peut être utile pour vérifier que les couleurs de surface de vos objets sont bien celles que vous attendez, sans être distrait par les lumières, les ombres, les reflets ou la transparence. 

Ce mode peut également être utilisé pour des rendus non photoréalistes, afin d’obtenir un aspect plat et cartoon.

## ![](/icons/cube.webp) ID objet {#object-id}

Toutes les informations d’éclairage et de surface sont ignorées, et chaque objet est ombré avec une couleur unie unique. Si ceci est rendu en parallèle d’un rendu PBR, cela peut être utilisé dans un logiciel de peinture pour sélectionner par couleur, et ainsi pouvoir faire des corrections colorimétriques sur des objets spécifiques.

Notez que ces couleurs apparaîtront également dans la [vue arborescente du menu Scene](scene#tree-view).

### Randomiser l’ID {#object-random}

Génère un nouveau jeu de couleurs aléatoires. 

## ![](/icons/link.webp) ID d’instance {#instance-id}

Identique à Object ID, mais les instances auront la même couleur. 

### Randomiser l’ID {#instance-random}

Génère un nouveau jeu de couleurs aléatoires.