# ![](/icons/sun.webp) Ombrage {#shading}

Ce menu contrôle les modes d'ombrage de Nomad, les propriétés de l'éclairage, l'environnement et le matcap, ainsi que le brouillard.

![](/images/shading_overview.webp)



Vous avez le choix entre plusieurs modes de rendu :

| Mode                        | Signification              | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Éclairé (PBR)](#pbr)       | Physically Based Rendering (rendu basé sur la physique) | Lumières, ombres, environnement, et métallité/rugosité peintes   |
| [MatCap](#matcap)           | Material Capture (capture de matériau) | Mode rapide pour sculpter, qui sollicite moins le GPU/CPU que le PBR |
| [Sans éclairage](#unlit)    | Couleur de surface         | Uniquement la couleur de surface, sans ombrage ni éclairage     |
| [ID d'objet](#object-id)    | Identifiant d'objet        | Une couleur aléatoire par objet, utile pour les applications de peinture. |
| [ID d'instance](#instance-id) | Identifiant d'instance   | Une couleur aléatoire par instance, utile pour repérer les maillages partagés |

Pour en savoir plus sur la métallité et la rugosité, consultez la section [Peinture](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Groupe de faces {#face-group}
Affiche les couleurs des groupes de faces par-dessus le modèle. Les groupes de faces sont des sélections colorées de polygones, que l'on crée avec l'outil [Groupe de faces](tools#facegroup) ; la plupart des primitives en ont aussi automatiquement.

Certains outils filtrent automatiquement selon les groupes de faces quand ceux-ci sont visibles.

### ![](/icons/palette.webp) Afficher la peinture {#show-paint}
Nomad peut stocker la couleur, la rugosité et la métallité dans les sommets de votre sculpture. Cette case à cocher active ou désactive l'affichage de ces propriétés pour toute la scène.

Notez que si vous avez à la fois des propriétés de sommets et des textures, et que les deux sont activées, leurs valeurs sont multipliées entre elles.

### ![](/icons/shield.webp) Afficher le masque {#show-mask}
Active ou désactive l'affichage en niveaux de gris du masque des [outils de masque](tools#mask). Quand il est désactivé, le masque l'est aussi : pratique pour faire des retouches rapides sans le masque, puis le réactiver sans le perdre.

### ![](/icons/tool_hide.webp) Utiliser Masquer {#use-hide}

Active ou désactive les faces cachées. Notez que cela ne fonctionne que si vous n'êtes PAS dans l'outil Masquer !

### ![](/icons/image.webp) Utiliser des textures {#use-textures}

Nomad permet d'attribuer des textures aux objets depuis le menu [Matériau](material). Si des textures sont attribuées, cette case à cocher les active ou les désactive pour toute la scène.

Vous ne pouvez pas créer ni modifier de textures dans Nomad, mais les textures des fichiers importés fonctionnent. Les textures d'opacité fonctionnent en Éclairé, MatCap et Sans éclairage, les cartes de normales en Éclairé et MatCap, la couleur en Éclairé et Sans éclairage, et l'émission, la rugosité et la métallité uniquement en Éclairé. Le bouton est grisé quand la scène n'a aucune texture.

### Présentation du PBR et des lumières {#pbr}
Ce manuel n'entrera pas dans les détails du rendu basé sur la physique (PBR).

Une chose importante à retenir : l'éclairage et le matériau sont entièrement séparés.
Vous pouvez donc peindre la couleur, la rugosité et la métallité de votre objet pendant que l'éclairage est géré à part.
Cela vous permet de peindre votre objet puis d'ajuster l'éclairage plus tard, sans casser l'aspect général de votre modèle.

Les lumières, l'environnement et le brouillard ne sont disponibles qu'en [mode PBR](#pbr).
Pour des raisons de performances, vous êtes limité à 4 lumières sur mobile et 6 sur ordinateur.

::: tip
Vous pouvez charger un fichier glTF contenant plus de lumières : Nomad les conservera toutes.
Mais les performances ne suivront pas forcément.
:::

::: tip
Vous pouvez simuler de nombreuses lumières en rendant des objets sans éclairage/émissifs, puis en activant l'illumination globale dans le menu [Post-traitement](postprocess).
:::

### Présentation des types de lumière {#light-types-overview}

Voici les types de lumière actuellement gérés :

| Mode                        | Description                                             | Peut projeter des ombres |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Directionnel](#directional) | Lumière solaire située infiniment loin                 | Oui              |
| [Environnement](#env-light) | Une lumière lointaine calée sur le HDR de l'environnement | Oui           |
| [Projecteur](#spot)         | Lumières en forme de cône                               | Oui              |
| [Point](#point)             | Point lumineux omnidirectionnel                         | Oui              |

#### ![](/icons/sun.webp) Directionnel {#directional}
Elle émet de la lumière depuis l'infini, avec une intensité uniforme.
Sa position 3d dans la scène n'a pas d'importance, seule son orientation compte.

Vous pouvez attacher cette lumière à la caméra, pour garder un éclairage constant.  
Par exemple, elle peut servir de lumière de contour (une lumière forte placée derrière votre modèle, dirigée vers la caméra) qui éclaire toujours l'arrière de votre modèle.

#### ![](/icons/panorama.webp) Lumière d'environnement {#env-light}
Un [HDR d'environnement](#environment) convient bien pour un éclairage doux d'ensemble, mais si une lumière forte et nette est visible dans le HDR, l'ombre qu'elle crée est très douce, souvent même invisible. Combiner une lumière directionnelle avec le HDR d'environnement peut aider, mais il est parfois difficile de bien les aligner.

Cette lumière fait le travail pour vous. Elle pivote automatiquement pour s'aligner sur la partie la plus lumineuse du HDR, puis vous réglez séparément son intensité et son angle (la douceur des ombres). 

#### ![](/icons/spotlight.webp) Projecteur {#spot}
Le projecteur émet de la lumière dans une seule direction, limitée par un cône.

#### ![](/icons/light.webp) Point {#point}
La lumière ponctuelle émet dans toutes les directions, et peut elle aussi projeter des ombres.

#### Ombres {#shadows}
Chaque lumière peut projeter des ombres, et vous pouvez choisir leur mode de calcul dans ses [réglages](#light-extra-controls). Si vous voyez des artefacts d'ombre, les curseurs `Tolérance` qui s'y trouvent peuvent aider.

La qualité des ombres dépend de la taille des objets par rapport à toute la scène.  
Si votre scène contient un grand objet qui n'a pas besoin de projeter d'ombre (par exemple un grand plan), pensez à désactiver la projection d'ombres dans ses [réglages de matériau](material.md#casts-shadows).

## ![](/icons/sun.webp) Lumières {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Case à cocher Lumières {#lights-checkbox}

Active ou désactive toutes les lumières directes de la scène.



### Ajouter une lumière {#add-light}

Ajoute une lumière à la scène, jusqu'à 4 lumières sur mobile et 6 sur ordinateur. Dès qu'une lumière est ajoutée, la liste des lumières s'affiche avec ses boutons, et une barre d'outils de lumière apparaît en haut de la vue.

![](/images/shading_lights_icons.webp)

* Le texte indique le nom de la lumière et sa luminosité. Touchez-le pour sélectionner la lumière.
* L'icône en forme d'œil active ou désactive la visibilité.
* L'icône en forme de crayon permet de renommer la lumière.
* L'icône de corbeille supprime une lumière.
* L'icône de copie duplique une lumière. 
* L'icône à 3 points ouvre l'éditeur complet de la lumière. La plupart de ses fonctions sont aussi accessibles depuis la barre d'outils qui apparaît dans la vue. 

Vous pouvez aussi faire glisser une lumière dans la liste pour la réordonner.

### ![](/icons/spotlight.webp)  Icônes {#icons}

Affiche ou masque les icônes des lumières dans la vue.

### Barre d'outils de lumière {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Cette barre d'outils apparaît en haut de la vue quand une lumière est sélectionnée.

* `Visible` active ou désactive la visibilité de la lumière.
* Directionnel/Environnement/Projecteur/Point change le type de lumière. Touchez pour passer de l'un à l'autre, ou faites un appui long pour afficher un menu.
* L'intensité contrôle la force de la lumière ; la valeur peut dépasser 1.0 pour des lumières très intenses, ce qui est utile avec l'illumination globale du Post-traitement.
* Toucher la pastille de couleur ouvre un sélecteur de couleur. Nomad propose plusieurs façons de choisir une couleur. Le réglage en Kelvin offre une façon naturelle de choisir un éclairage chaud ou froid.
* Ombre active ou désactive les ombres.
* Angle (_directionnelle et environnement_) ou Taille (_projecteur et point_) définit la largeur d'une lumière. Une lumière plus large projette des ombres douces, un éclairage doux et un reflet plus doux sur les objets.
* Fixation (_directionnelle uniquement_), Angle du cône et Douceur (_projecteur uniquement_) sont décrits plus bas, dans l'[éditeur de lumière](#light-extra-controls).
* ... affiche `Cloner`, `Recentrer` et `Supprimer`, ainsi que les réglages d'ombre.

### Réglages supplémentaires des lumières {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

L'icône à 3 points d'une lumière dans la liste ouvre son éditeur complet. Notez que certaines options sont propres à certains types de lumière.

* `Directionnel/Environnement/Projecteur/Point` permet de changer le type de lumière.
* Toucher la `pastille de couleur` ouvre un sélecteur de couleur. 
* `Intensité` contrôle la force de la lumière.
* `Fixation` (_directionnelle uniquement_) rattache la lumière au monde (`Fixe`) ou à la caméra (`Caméra`). Par exemple, si vous placez une lumière directionnelle derrière votre personnage comme lumière de contour, avec la fixation sur la caméra, la lumière reste toujours derrière le personnage quand vous faites pivoter la caméra.
* `Douceur` (_projecteur uniquement_) contrôle la netteté du bord du cône du projecteur. 0 donne un bord très net. 1 est très doux, avec un dégradé jusqu'au centre du cône de lumière. Dans la vue, le petit point bleu sur le cône du projecteur permet de régler la douceur directement.
* `Angle du cône` (_projecteur uniquement_) contrôle l'ouverture du projecteur. Un petit angle donne un faisceau très fin, 170 une lumière très étalée. Dans la vue, le point orange permet de régler l'angle du cône directement.
* `Angle` (_directionnelle et environnement uniquement_) est la taille apparente de la lumière : voyez-le comme la taille du soleil dans le ciel. Un angle plus grand donne des ombres plus douces et des reflets plus larges.
* `Taille` (_projecteur et point uniquement_) est la largeur de la lumière. Une lumière plus grande projette des ombres plus douces.
* `Ombre` active ou désactive les ombres de cette lumière.
* Le type d'ombre choisit comment les ombres sont calculées. Une `Texture d'ombre` rend la scène depuis la lumière, et projette donc aussi l'ombre de la géométrie que la caméra ne voit pas. `Espace écran` n'utilise que ce qui est déjà visible à l'écran : c'est moins coûteux, mais expérimental. En général, la texture d'ombre est plus fiable.
* `Tolérance` (_espace écran uniquement_) : si des artefacts d'ombre sont visibles (les ombres ne semblent pas toucher les surfaces, ou du bruit et des motifs apparaissent dans les ombres), ajuster la tolérance peut corriger ces problèmes.
* `Contact` ajoute des ombres plus précises sur de courtes distances, là où les objets se touchent. Avec `Auto`, seule la lumière dominante de la scène reçoit des ombres de contact ; `Non` et `Oui` les imposent pour cette lumière. Son curseur `Tolérance` fonctionne comme celui ci-dessus.

Le bouton `...` de la barre d'outils de la vue regroupe les mêmes réglages d'ombre, plus :

* `Cloner` duplique la lumière.
* `Recentrer` place la lumière devant la caméra, en gardant son orientation.
* `Supprimer` supprime la lumière.


## ![](/icons/panorama.webp) Environnement {#environment}

![](/images/shading_environment.webp)

Dans le monde réel, la lumière vient de toutes les directions : le bleu du ciel, le vert de l'herbe, le rouge d'un bâtiment... Toute cette lumière de l'« environnement » peut être simulée avec une carte d'environnement. 

La case à cocher à côté du titre active ou désactive l'éclairage d'environnement.

Nomad fournit plusieurs cartes d'environnement d'exemple, en intérieur et en extérieur, avec différentes teintes et luminosités. Essayez-en plusieurs pour voir laquelle fait le mieux ressortir les détails de vos sculptures.

Touchez l'image pour voir les cartes d'environnement disponibles. Dans cette fenêtre, choisissez `Importer…` pour charger les vôtres. Le mieux est d'utiliser des images HDR (High Dynamic Range), au format latlong ou équirectangulaire, en fichiers .hdr ou .exr. Le navigateur peut aussi télécharger des environnements directement depuis [Poly Haven](https://polyhaven.com/hdris), qui propose une belle collection de cartes d'environnement gratuites.

### Exposition {#env-exposure}
Règle la luminosité de la carte d'environnement. Les cartes sont souvent trop lumineuses quand on les combine avec des lumières classiques : baisser l'exposition aide à équilibrer, surtout avec l'illumination globale des réglages de [Post-traitement](postprocess).

### Rotation {#env-rotation}

Comme les cartes d'environnement capturent la lumière venant de toutes les directions, vous pouvez les faire pivoter pour que les reflets et l'éclairage général s'accordent bien avec votre sculpture. Vous pouvez aussi faire pivoter l'environnement en faisant glisser 3 doigts horizontalement sur la vue.

### Attaché à la caméra {#env-attached}
Attache l'environnement à la caméra.

L'éclairage reste ainsi constant, ce qui peut être utile pendant la sculpture.

### Flou (arrière-plan) {#env-background-blur}
Ce curseur n'apparaît que si l'[arrière-plan](background.md) est réglé sur l'environnement. Il floute l'image d'environnement derrière votre modèle, sans changer l'éclairage.


## ![](/icons/fog.webp) Brouillard {#fog}

Le brouillard ajoute de la profondeur atmosphérique à votre scène et rend les faisceaux de lumière visibles. Activez-le avec la case à cocher à côté du titre. Comme les lumières et l'environnement, il n'est disponible qu'en mode [Éclairé (PBR)](#pbr).

::: tip Des faisceaux de lumière plus marqués
Baissez l'`Environnement` du brouillard, et utilisez un projecteur ou une lumière ponctuelle puissante. Augmentez la `Densité` jusqu'à ce que le brouillard soit bien visible. Pour voir des faisceaux dans un brouillard plus léger, réglez la `Direction de diffusion` sur une valeur positive élevée et orientez la caméra vers la lumière.
:::

### Couleur {#fog-color}
La couleur du brouillard et de la lumière qu'il diffuse.

### Densité {#fog-density}
La vitesse à laquelle le brouillard s'épaissit avec la distance.

### Opacité maximale {#fog-opacity}
Limite la part de la scène que le brouillard peut couvrir, même à forte densité.

### Direction de diffusion {#fog-scattering}
La direction dans laquelle le brouillard diffuse la lumière (aussi appelée anisotropie). Les valeurs positives éclaircissent le brouillard quand vous regardez vers une lumière, les valeurs négatives quand vous regardez à l'opposé, et zéro diffuse la lumière de façon égale dans toutes les directions.

### ![](/icons/panorama.webp) Environnement {#fog-environment}
L'intensité avec laquelle l'[environnement](#environment) éclaire le brouillard. Le réglage est grisé quand l'environnement est désactivé.

### Bruit {#fog-noise}
Mélange du bruit au brouillard pour le découper en nappes, sans changer sa densité globale. Quand le bruit est supérieur à 0, un curseur `Taille` règle la taille du motif.

### Forme {#fog-shape}
Où le brouillard remplit la scène :

* `Uniforme` - remplit toute la scène.
* `Vertical` - garde le brouillard dans une bande verticale aux bords adoucis. Les curseurs `Bas` et `Haut` règlent la hauteur de ses bords inférieur et supérieur, et leur bouton en forme d'œil affiche la bande dans la vue pendant que vous les ajustez.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Comme son nom l'indique (MATerial CAPture, capture de matériau), un matcap réunit l'éclairage et les informations de matériau dans une seule image.
Comme le matériau est déjà contenu dans le matcap, les canaux de peinture de rugosité et de métallité sont ignorés.
La couleur peinte est multipliée par le matcap : avec un matcap noir ou gris, peindre en blanc ne le rendra pas plus clair.

Les artistes préfèrent souvent ce mode pour sculpter, car il permet de se concentrer sur la forme et la géométrie elles-mêmes.

Toucher la sphère ouvre un navigateur d'images. Vous pouvez aussi ajouter vos propres matcaps : en général, n'importe quelle photo, rendu, ou même peinture d'une sphère, recadrée au plus près dans un carré, fera l'affaire. De nombreuses bibliothèques de matcaps sont disponibles en ligne ; une ressource utile est la [bibliothèque de matcaps nidorx](https://github.com/nidorx/matcaps).

### Utiliser le MatCap global {#matcap-global}

Les artistes utilisent en général un seul matcap pour toute la sculpture, mais si cette option est désactivée, l'objet sélectionné peut avoir son propre matcap. Cela peut servir d'effet artistique pour des résultats saisissants.

::: tip
Désactivez cette option, et utilisez l'image d'un globe oculaire pour les yeux de vos personnages !
:::

### Rotation {#matcap-rotation}
Un matcap est une forme particulière de carte d'environnement : comme elle, il peut pivoter. Vous pouvez aussi le faire à tout moment dans la vue en faisant glisser 3 doigts vers la gauche ou la droite.

Le bouton de cadenas à côté du curseur verrouille la rotation, pour qu'un glisser à 3 doigts ne fasse pas tourner le matcap par accident.



## ![](/icons/circle_fill.webp) Sans éclairage {#unlit}

Ce mode n'affiche que la couleur de surface. Il est utile pour vérifier que la couleur de surface de vos objets est bien celle que vous attendez, sans être distrait par les lumières, les ombres, les reflets ou la transparence. 

Ce mode peut aussi servir pour des rendus non photoréalistes, avec un aspect plat, façon dessin animé.

## ![](/icons/cube.webp) ID d'objet {#object-id}

Toutes les informations d'éclairage et de surface sont ignorées, et chaque objet est affiché avec une couleur unie qui lui est propre. Rendu en plus d'un rendu PBR, cela permet, dans un logiciel de peinture, de sélectionner par couleur, et donc de faire des corrections de couleur sur des objets précis.

Notez que ces couleurs apparaissent aussi dans l'[arborescence du menu Scène](scene#tree-view).

### ID aléatoire {#object-random}

Génère un nouveau jeu de couleurs aléatoires. 

## ![](/icons/link.webp) ID d'instance {#instance-id}

Comme ID d'objet, mais les instances ont la même couleur. 

### ID aléatoire {#instance-random}

Génère un nouveau jeu de couleurs aléatoires.
