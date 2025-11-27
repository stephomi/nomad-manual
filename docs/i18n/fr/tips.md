# ![](/icons/manual.webp) Conseils

[[toc]]

## Comment démarrer un modèle

Les débutants en sculpture 3D demandent souvent quelle est la meilleure façon de démarrer un modèle. Il n’y a pas de meilleure façon, différentes personnes ont des préférences différentes. Voici quelques-unes des approches les plus courantes.

### Sculpter sur une sphère, multirésolution

Le modèle par défaut au lancement de Nomad est la méthode la plus courante. Utilisez les outils Déplacer, Argile, Pli pour pousser et tirer la sphère afin de lui donner une forme, utilisez les niveaux de subdivision bas lorsque vous voulez faire de gros changements rapidement, utilisez les niveaux de subdivision élevés pour le travail de détail.

Un problème fréquent est que vous manquerez souvent de polygones là où vous en avez besoin, alors que vous en aurez trop ailleurs. Par exemple, si vous transformez la sphère par défaut en un corps entier, il est probable que vous n’aurez pas assez de détails pour faire les doigts, alors que vous aurez beaucoup de polygones gaspillés à l’arrière de la tête. Pour des formes principalement sphériques comme une tête, cela peut toutefois convenir.

### Dyntopo

L’activation de Dyntopo ajoutera et supprimera des polygones de manière adaptative pendant que vous sculptez. Ces polygones seront des triangles, et les débutants n’aiment souvent pas la disposition désordonnée comparée au look propre de la multirésolution. Cela vaut la peine d’insister ! Si vous activez l’ombrage lisse, désactivez le fil de fer et cessez de vous soucier de la disposition, ce mode peut donner une sensation très proche de l’argile. N’oubliez pas que si vous utilisez un gros pinceau, ou un pinceau de lissage, ce mode peut aussi supprimer des polygones, de sorte que l’outil reste toujours rapide et réactif. Une fois que vous avez terminé un premier passage de la sculpture, vous pouvez la cloner et la passer dans le quad remesher pour obtenir une belle topologie, puis reprojeter les détails originaux sur un niveau de subdivision élevé.

### Remesh voxel

Le remesh voxel appliquera une topologie principalement en quads sur votre sculpture. Cette opération est rapide aux résolutions basses, et peut être utilisée pour remplacer rapidement des polygones étirés ou trop denses par une disposition régulièrement espacée. C’est une excellente façon de démarrer un corps entier à partir d’une sphère ; disons que vous commencez par une tête, vous pouvez étirer un cou, faire un remesh voxel. Étirez un corps, remesh voxel, les bras, remesh voxel, et ainsi de suite, jusqu’à ce que vous ayez les formes de base.

### Utiliser plusieurs objets

De nombreux guides d’anatomie représentent un corps à partir de simples sphères, cylindres, cubes. Vous pouvez également sculpter de cette façon dans Nomad. Cela a l’avantage de vous permettre de lier des objets entre eux dans la hiérarchie de scène, afin que vous puissiez par exemple faire pivoter le cou et que la tête suive. Pouvoir utiliser l’outil de gizmo pour des translations/rotations/mises à l’échelle précises est également très utile, et vous pouvez aussi définir des pivots par forme pour qu’elles se déplacent exactement comme prévu. Lorsque les blocs de base sont au bon endroit, vous pouvez tous les sélectionner et faire un remesh voxel ou un booléen pour les fusionner en une seule surface pour une sculpture plus détaillée.

Une astuce pratique pour cette façon de travailler est de commencer avec une sphère, de l’étirer en une forme de saucisse, d’appuyer sur pivot, de cliquer sur « bottom », puis d’appuyer à nouveau sur pivot. Vous avez maintenant une partie de corps qui peut être clonée, déplacée le long de la longueur de la première sphère, clonée, tournée, clonée, glissée, clonée, etc. pour mettre en place un corps rapidement.

### Tubes

L’outil Tube est un excellent moyen de démarrer une sculpture. Queues de reptiles, bras, jambes, doigts, sourcils, tout cela peut être rapidement esquissé avec l’outil Tube, puis facilement édité ensuite. Il permet également de modifier le profil de la section, ce qui autorise des changements de forme rapides. Vous pouvez valider la forme pour commencer à sculpter dessus, puis faire un remesh voxel avec d’autres objets pour obtenir un maillage de corps complet.

### Utiliser d’autres applications

Certaines personnes préfèrent démarrer un modèle dans d’autres applications, c’est très bien aussi. Des outils comme Blender ou Valence permettent de démarrer des modèles en low poly, qui peuvent ensuite être importés dans Nomad pour la sculpture.

### Utiliser les préréglages intégrés

Depuis le menu Projet, cliquez sur `Preset...` en haut à droite. Vous y trouverez plusieurs préréglages de formes de têtes et de corps provenant de la Blender Foundation. Sélectionnez celui que vous aimez, touchez-le à nouveau, ajoutez-le à votre scène. 

### Utiliser des modèles en ligne

Il existe de nombreux modèles gratuits en ligne, par exemple Polyhaven, Sketchfab, Turbosquid. En général, ces modèles peuvent être importés dans Nomad, puis soit sculptés directement, soit utilisés comme référence.

### Pas de règles !

En fin de compte, vous pouvez utiliser n’importe quelle combinaison de ces techniques, ou aucune ! Nomad est très flexible à cet égard, les utilisateurs avancés peuvent commencer avec des tubes, puis du dyntopo, puis combiner avec un pied téléchargé, puis tout passer en quad remesh, puis en multirésolution pour les détails finaux. Tout ce qui fonctionne pour vous.

## Facegroups

L’outil Facegroup peut être utilisé pour de nombreuses choses, comme expliqué dans cette vidéo YouTube : https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Voici un résumé textuel des fonctionnalités couvertes dans cette vidéo.

### Pourquoi les facegroups ?

Les facegroups vous permettent d’organiser et de sélectionner des faces (« faces » et « polygones » sont utilisés de manière interchangeable dans ce manuel). C’est plus facile à expliquer par rapport aux autres outils de sélection et d’organisation de Nomad. Nomad vous permet de créer des objets, de les nommer, de les hiérarchiser, il est facile de créer une structure d’objets pour définir une pièce composée de sol, murs, chaise, table, etc.

Pour un personnage, vous pouvez faire un blocage initial en utilisant des objets séparés pour la tête, le bras, la jambe, mais une fois que vous fusionnez toutes les pièces en un seul maillage, cette structure est perdue. Vous pouvez travailler sur des sous-sections d’un personnage avec des masques, mais cela peut devenir fatigant de devoir sans cesse peindre un masque pour les mains, puis le nez, puis à nouveau les mains.

C’est là que les facegroups sont utiles. Ils vous permettent d’étiqueter des faces de polygones avec une couleur, puis de pouvoir sélectionner et manipuler les polygones qui ont la même couleur. Notez que la couleur de facegroup et la couleur de sommet (vertex color) sont deux choses différentes.

L’analogie la plus proche serait de peindre des couleurs sur une carte, puis de pouvoir plus tard sélectionner des pays ou des régions en fonction de la couleur.

Pour les têtes de personnages, vous pouvez peindre des zones pour marquer les orbites, le nez, les lèvres, le menton, les oreilles, puis sélectionner facilement ces zones plus tard. Pour la sculpture hard surface et mécanique, il peut être utile de définir des panneaux et des sections.

### Création et édition de facegroups

Les facegroups peuvent être appliqués avec un pinceau, où chaque nouveau trait crée un nouveau facegroup, ou bien ils peuvent sélectionner le facegroup sous le curseur et l’étendre. Ils peuvent également être créés à l’aide de formes.

* Point, auto-pick activé – un simple glisser définira une nouvelle couleur de facegroup et l’assignera aux faces sur lesquelles vous passez. Chaque nouveau glisser définira un nouveau facegroup. Un tapotement remplira un nouveau facegroup.
* Point, auto-pick désactivé – lorsque le bouton auto-pick est dans son mode « sub », Nomad sélectionnera le facegroup sous le curseur et l’appliquera pendant le reste du glisser. C’est utile pour affiner les facegroups sans avoir à les sélectionner manuellement.

### Masquage

Lorsque l’outil Masque est actif, et que le bouton facegroup est actif sur sa barre d’outils, toucher un facegroup le masquera.

### Masquage de la visibilité

Lorsque l’outil Hide est actif, et que le bouton facegroup est actif sur sa barre d’outils, toucher un facegroup le cachera.

### Organisation

Comme mentionné plus haut, les facegroups peuvent être utilisés pour organiser votre maillage sans vous obliger à créer des objets séparés. Vous ne voudrez peut-être pas découper une tête en objets séparés pour le nez, le menton, les oreilles, mais il est très utile de les définir via des facegroups.

### Régions UV

L’outil UV Atlas tentera de définir automatiquement des coutures, mais les placera parfois à des endroits indésirables. Si des facegroups existent sur un objet, et que l’option facegroup est active dans les options d’UV Atlas, il utilisera à la place les bordures de facegroups comme coutures UV.

### Quad remesher

Le plugin Quad Remesher fera généralement circuler les arêtes de manière harmonieuse sur votre modèle, mais vous pouvez utiliser les facegroups pour l’aider à se diriger lorsque l’option facegroup est activée. Cela peut faciliter la définition d’un flux d’arêtes propre autour des yeux, d’une arête de sourcil, des lèvres, d’un pli de joue par exemple.

### Filtrer avec d’autres outils

De nombreux outils ont des options pour être sensibles aux facegroups, soit depuis leur menu d’outil principal, soit via le menu Stroke -> Filtering. Par exemple, l’outil de lissage à des forces supérieures à 100 % peut lisser agressivement les détails à l’intérieur d’un facegroup, tout en gardant la bordure du facegroup relativement intacte.

### Relaxer et lisser les bordures de facegroups

L’option Relax dans l’outil Facegroup fait un excellent travail de lissage des bordures de facegroups tout en conservant les autres caractéristiques intactes. C’est un excellent moyen de définir des bordures de facegroups lisses avant un quad remesh.

## Limitations sur tablette/mobile

Les tablettes et mobiles actuels sont très puissants, mais présentent des différences importantes par rapport aux ordinateurs de bureau et aux ordinateurs portables :

### Pas de refroidissement actif

Les ordinateurs ont des ventilateurs et/ou de grands dissipateurs thermiques pour rester au frais, et sont conçus pour fonctionner à des températures élevées. Le matériel mobile est généralement conçu d’abord pour la finesse, pas pour aider à garder l’intérieur au frais. Si Nomad est poussé à ses réglages de qualité les plus élevés (mode d’éclairage PBR, matériaux complexes, nombreux objets, de nombreuses options de post-traitement activées), cela peut à la fois surchauffer l’appareil et vider la batterie très rapidement. 

Une meilleure approche consiste à utiliser un mode d’éclairage matcap, et un multiplicateur de rendu plus faible (en haut du menu de post-process). Ces choix garderont l’appareil au frais et vous permettront de sculpter plus longtemps.

### Mémoire limitée

Nomad peut obtenir des résultats équivalents à la plupart des applications de sculpture de bureau, mais il ne peut pas plier les lois de la physique ! La plupart des ordinateurs de bureau ont deux fois plus de mémoire que les appareils mobiles, les stations de travail conçues pour l’animation 3D ont souvent 4x ou 8x plus de mémoire. Pour cette raison, il est bon d’être conscient du nombre de polygones que vous utilisez, de faire quelques tests sur votre appareil pour voir à partir de quand il commence à ralentir. Presque tous les appareils capables de faire tourner Nomad peuvent gérer 1 million de polygones assez facilement. Un iPad Pro M2 peut gérer confortablement 8 millions, des personnes ont testé sur les derniers iPads bien au-delà de ce chiffre.

Cela dit, seules les sculptures les plus détaillées ont besoin de plus de 4 millions de polygones ; si vous faites des objets relativement simples et que vous vous retrouvez souvent au-dessus de 500 000, 1 million, 4 millions, vous utilisez trop de polygones ! Assurez-vous que le mode d’ombrage lisse est activé dans les options.

### L’OS est moins tolérant avec les applications intensives

Apple et Android s’attendent à ce que les applications sauvegardent et chargent de petits fichiers très rapidement. Ils supposent également que les applications peuvent changer de tâche très vite. Là encore, Nomad fait quelques astuces intelligentes pour garder les fichiers relativement petits et les sauvegarder très rapidement, mais si l’OS mobile décide que Nomad prend trop de temps, il le tuera simplement avant qu’il ait terminé sa tâche. C’est une autre raison de garder les fichiers de petite taille ; il est possible de travailler avec des sculptures de 37 millions de polygones comme l’a rapporté un utilisateur sur Discord, mais ce n’est pas recommandé !

## Travailler sur de petits écrans

Nomad est conçu pour fonctionner sur tablettes, mais fonctionne aussi bien sur téléphones. La sculpture sur un petit écran comme un téléphone peut être facilitée par quelques ajustements d’interface et de flux de travail :

* Un tapotement à 4 doigts bascule toute l’interface, vous donnant plus de place pour sculpter.
* Un glisser à 3 doigts vers le haut ou le bas change le rayon du pinceau.
* L’échelle de l’interface peut être réduite pour faire tenir plus de boutons si vous avez une bonne vue, ou agrandie si vous avez une mauvaise vue !
* Les menus plus larges peuvent parfois gêner la sculpture, vous pouvez les rendre transparents et non floutés pour vous permettre de voir la sculpture sous le menu.
* Si vous sculptez avec un doigt, utilisez l’option d’offset pour déplacer légèrement le centre du pinceau par rapport à votre doigt.
* Ces options et bien d’autres se trouvent dans le [menu Interface](./interface.md). 

## Déformeur d’inflation ou de pointe

De nombreuses applications 3D proposent un déformeur d’inflation, qui pousse tous les sommets le long de leur normale d’une valeur contrôlable. Bien que Nomad ne dispose pas encore de déformeurs, il est possible d’émuler ce comportement avec le pinceau Inflate :

* Sélectionnez le pinceau Inflate
* Dans le [menu Stroke](./stroke.md#stroke), changez la méthode de trait en `Lock + Radius'
* Donnez au pinceau un rayon plus grand que votre sculpture, zoomez la caméra en arrière si nécessaire.
* Cliquez puis faites glisser un trait sur la surface de votre objet ; lorsque le rayon est plus grand que l’objet, toute la forme sera gonflée uniformément d’une valeur fixe.
* Ajustez l’intensité du pinceau pour contrôler la quantité d’inflation.
* Utilisez le masquage si nécessaire pour protéger ou réduire l’effet de l’inflation dans certaines zones.

## Supprimer les bosses ou « boutons » après une opération de remesh voxel

Le remesh voxel est excellent pour créer des polygones régulièrement espacés, mais crée parfois une topologie qui provoquera de petites bosses ou boutons lors du lissage. Par exemple :

* Utilisez le pinceau Crease sur la sphère par défaut et faites une spirale
* Faites un remesh voxel avec « build multiresolution at 3 »
* Lissez avec une intensité élevée
* Des artefacts apparaissent (plus faciles à voir avec un matériau matcap à fort contraste) :

![](/videos/tip_pimples_before.mp4)

Pour corriger via la sculpture, essayez l’option `Stable smoothing` dans les paramètres de lissage. Elle peut gérer la disposition de topologie irrégulière du remesh voxel et donner des résultats propres.

![](/videos/tip_pimples_stable_smooth.mp4)

Pour corriger la topologie elle-même, utilisez une nouvelle primitive, ou les outils de quad remesh, ou un modeleur 3D externe, et projetez les détails du maillage original sur le nouveau via `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Éclairage de jour

Le rendu PBR par défaut est, comme son nom l’indique, physiquement basé, ce qui, comme une photo numérique non traitée, peut paraître un peu délavé et plat. Les lumières et le post-traitement de Nomad peuvent être utilisés pour rendre les rendus plus vibrants.

Voici un rendu par défaut, voyons si nous pouvons l’améliorer :
![](/images/tips_lighting_default.webp)

L’activation du post-traitement et du tonemapping peut ajouter de la luminosité et du contraste :

![](/images/tips_lighting_tonemap.webp)

Pour se concentrer sur les lumières, la lumière d’environnement par défaut est bonne pour la sculpture, mais peut être améliorée pour un rendu final. Une façon de penser à cela est de séparer la lumière directe (par exemple le soleil) de la lumière d’environnement (par exemple la lumière provenant du bleu du ciel, du sol). En réduisant la lumière d’environnement et en la faisant pivoter, on commence à capturer ce à quoi l’éclairage devrait ressembler si le sujet se trouvait dans une zone ombragée :

![](/images/tips_lighting_env.webp)

Une lumière directe peut être ajoutée, et son intensité augmentée pour simuler un soleil dur. En l’équilibrant avec la lumière d’environnement, on obtient un résultat agréable :

![](/images/tips_lighting_sunlight.webp)

Les personnages peuvent bénéficier du remplacement de leur matériau par un matériau à subsurface, et du placement d’un projecteur derrière le personnage visant les oreilles pour les faire briller :

![](/images/tips_lighting_sss.webp)

Ensuite, expérimentez avec le reste des paramètres de post-process ! Global Illumination et Ambient Occlusion aident à obtenir un éclairage plus réaliste. Curvature et Sharpen peuvent aider à faire ressortir plus de détails dans la sculpture. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette aident à simuler des effets de caméra. Notez qu’au fur et à mesure que des fonctionnalités sont activées, l’éclairage et les autres valeurs de post-traitement doivent être ajustés pour compenser.

Voici le rendu avec un ensemble complet d’ajustements de post-traitement :
![](/images/tips_lighting_final.webp)
