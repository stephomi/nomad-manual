# ![](/icons/manual.webp) Astuces {#tips}

[[toc]]

## Comment commencer un modèle {#how-to-start-a-model}

Les débutants en sculpture 3d demandent souvent quelle est la meilleure façon de commencer un modèle. Il n'y en a pas : chacun a ses préférences. Voici quelques-unes des approches les plus courantes.

### Sculpter sur une sphère, en multirésolution {#sculpt-on-sphere-multires}

Le modèle par défaut au lancement de Nomad est la méthode la plus courante. Utilisez les outils Déplacer, Argile et Pli pour pousser et tirer la sphère jusqu'à obtenir la forme voulue ; travaillez sur les niveaux de subdivision bas pour faire rapidement de grands changements, et sur les niveaux élevés pour les détails.

Un problème fréquent : vous manquez souvent de polygones là où il en faut, alors qu'il y en a trop ailleurs. Par exemple, si vous transformez la sphère par défaut en un corps entier, vous n'aurez sans doute pas assez de détail pour les doigts, alors que beaucoup de polygones seront gaspillés à l'arrière de la tête. Pour des formes plutôt sphériques comme une tête, en revanche, cela peut très bien aller.

### DynTopo {#dyntopo}

Activer DynTopo ajoute et retire des polygones à la volée pendant que vous sculptez. Ces polygones sont des triangles, et les débutants n'aiment souvent pas leur disposition désordonnée, comparée à l'aspect propre de la multirésolution. Ça vaut le coup d'insister ! Si vous activez l'ombrage lisse, désactivez le filaire et cessez de vous soucier de la disposition, ce mode peut donner une vraie sensation de terre glaise. N'oubliez pas qu'avec un grand pinceau, ou un pinceau de lissage, ce mode peut aussi retirer des polygones, pour que l'outil reste toujours rapide et réactif. Une fois une première version de la sculpture terminée, vous pouvez la cloner et la passer dans Quad Remesher pour obtenir une belle topologie, puis reprojeter les détails d'origine sur un niveau de subdivision élevé.

### Remaillage voxel {#voxel-remesh}

Le remaillage voxel applique à votre sculpture une topologie composée en majorité de quads. Cette opération est rapide aux basses résolutions, et permet de remplacer vite des polygones étirés ou trop denses par une répartition régulière. C'est une excellente façon de commencer un corps entier à partir d'une sphère : par exemple, partez d'une tête, étirez un cou, remaillage voxel. Étirez un corps, remaillage voxel, puis les bras, remaillage voxel, et ainsi de suite, jusqu'à obtenir les formes de base.

### Utiliser plusieurs objets {#use-multiple-objects}

Beaucoup de guides d'anatomie représentent le corps avec de simples sphères, cylindres et cubes. Vous pouvez aussi sculpter de cette façon dans Nomad. L'avantage est de pouvoir hiérarchiser les objets dans la scène : par exemple, vous faites pivoter le cou et la tête suit. Pouvoir utiliser l'outil Gizmo pour des déplacements, rotations et mises à l'échelle précis est aussi très utile, et vous pouvez définir un pivot par forme pour qu'elle bouge exactement comme prévu. Quand les blocs de base sont bien placés, sélectionnez-les tous, puis faites un remaillage voxel ou une opération booléenne pour les réunir en une seule surface, et sculpter plus de détails.

Une astuce pratique pour cette façon de travailler : partez d'une sphère, étirez-la en forme de saucisse, appuyez sur Pivot, touchez 'Bas', puis appuyez à nouveau sur Pivot. Vous avez maintenant une partie du corps que vous pouvez cloner, déplacer le long de la première sphère, cloner, faire pivoter, cloner, faire glisser, cloner, etc., pour mettre en place un corps rapidement.

### Tubes {#tubes}

L'outil Tube est une excellente façon de commencer une sculpture. Queues de reptiles, bras, jambes, doigts, sourcils : tout cela s'esquisse vite avec l'outil Tube, puis se modifie facilement ensuite. Il permet aussi de modifier le profil de la section, pour changer rapidement de forme. Vous pouvez valider la forme pour commencer à sculpter dessus, puis faire un remaillage voxel avec d'autres objets pour obtenir le maillage d'un corps entier.

### Utiliser d'autres applications {#use-other-apps}

Certaines personnes préfèrent commencer un modèle dans d'autres applications, et c'est très bien aussi. Des outils comme Blender ou Valence permettent de démarrer un modèle avec des techniques low poly, puis de l'importer dans Nomad pour le sculpter.

### Utiliser les préréglages fournis {#use-the-built-in-presets}

Dans le menu [Fichiers](files.md), touchez `Préréglage…` à gauche de la section du projet. Vous y trouverez plusieurs préréglages de têtes et de corps de la Blender Foundation. Sélectionnez celui qui vous plaît, touchez-le à nouveau, et ajoutez-le à votre scène. 

### Utiliser des modèles en ligne {#use-online-models}

De nombreux modèles gratuits sont disponibles en ligne, par exemple sur Poly Haven, Sketchfab ou TurboSquid. En général, ces modèles peuvent être importés dans Nomad, puis sculptés directement ou utilisés comme référence.

### Pas de règles ! {#no-rules}

Au final, vous pouvez combiner ces techniques comme vous voulez, ou n'en utiliser aucune ! Nomad est très souple de ce point de vue : un utilisateur avancé pourra commencer avec des tubes, passer à DynTopo, ajouter un pied téléchargé, tout passer dans Quad Remesher, puis utiliser la multirésolution pour les derniers détails. Faites ce qui vous convient.

## Groupes de faces {#facegroups}

L'outil Groupe de faces sert à beaucoup de choses, comme l'explique cette vidéo YouTube : https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Voici un résumé écrit des fonctions présentées dans cette vidéo.

### Pourquoi des groupes de faces ? {#why-facegroups}

Les groupes de faces permettent d'organiser et de sélectionner des faces (dans ce manuel, « faces » et « polygones » désignent la même chose). C'est plus facile à expliquer en les comparant aux autres outils de sélection et d'organisation de Nomad. Nomad vous permet de créer des objets, de les nommer, de les hiérarchiser : il est facile de construire une structure d'objets pour décrire une pièce composée d'un sol, de murs, d'une chaise, d'une table, etc.

Pour un personnage, vous pouvez faire une première ébauche avec des objets séparés pour la tête, les bras, les jambes, mais une fois tous les morceaux fusionnés en un seul maillage, cette structure est perdue. Vous pouvez travailler sur des parties du personnage avec des masques, mais il devient vite lassant de repeindre un masque pour les mains, puis le nez, puis à nouveau les mains.

C'est là que les groupes de faces sont utiles. Ils permettent d'étiqueter les faces des polygones avec une couleur, puis de sélectionner et de manipuler les polygones qui ont la même couleur. Notez que la couleur d'un groupe de faces et la couleur des sommets sont deux choses différentes.

L'analogie la plus proche serait de colorier une carte, pour pouvoir ensuite sélectionner des pays ou des régions d'après leur couleur.

Pour la tête d'un personnage, vous pouvez peindre des zones pour marquer les orbites, le nez, les lèvres, le menton, les oreilles, puis sélectionner facilement ces zones plus tard. En hard surface et en sculpture mécanique, cela peut servir à définir des panneaux et des sections.

### Créer et modifier des groupes de faces {#creating-and-editing-facegroups}

Les groupes de faces peuvent s'appliquer au pinceau, chaque nouveau trait créant un nouveau groupe de faces, ou bien l'outil peut sélectionner le groupe de faces sous le curseur et l'étendre. Vous pouvez aussi les créer avec des formes.

* Point, mode par défaut - un simple glisser définit une nouvelle couleur de groupe de faces et l'attribue aux faces que vous survolez. Chaque nouveau glisser définit un nouveau groupe de faces. Un toucher remplit d'un nouveau groupe de faces toute la zone connectée.
* Point, mode `Choisir` - quand le bouton `Choisir` de la barre d'outils de gauche est actif, Nomad sélectionne le groupe de faces sous le curseur et l'applique pendant tout le reste du glisser. C'est utile pour affiner les groupes de faces sans avoir à les sélectionner à la main.

### Masquage {#masking}

Quand l'outil Masque est actif et que le bouton de groupe de faces est activé dans sa barre d'outils, toucher un groupe de faces le masque.


### Masquer {#hiding}

Quand l'outil Masquer est actif et que le bouton de groupe de faces est activé dans sa barre d'outils, toucher un groupe de faces le cache.

### Organiser {#organizing}

Comme vu plus haut, les groupes de faces permettent d'organiser votre maillage sans avoir à créer des objets séparés. Vous ne voudrez peut-être pas découper une tête en objets séparés pour le nez, le menton et les oreilles, mais il est très utile de les avoir définis par des groupes de faces.

### Régions UV {#uv-regions}

Le dépliage UV Atlas essaie de définir les coutures automatiquement, mais en place parfois là où vous n'en voulez pas. Si un objet a des groupes de faces, et que l'option de groupes de faces est activée dans les options UV Atlas, les bordures des groupes de faces servent alors de coutures UV.

### Quad Remesher {#quad-remesher}

Le plugin Quad Remesher fait en général bien circuler les arêtes sur votre modèle, mais vous pouvez l'orienter avec les groupes de faces quand l'option correspondante est activée. Cela permet par exemple de définir facilement un flux d'arêtes propre autour des yeux, de l'arcade sourcilière, des lèvres ou d'un pli de la joue.

### Filtrer avec d'autres outils {#filter-with-other-tools}

Beaucoup d'outils ont des options pour tenir compte des groupes de faces, soit dans leur propre menu, soit dans le menu Trait -> Filtre. Par exemple, l'outil Lisser à une force supérieure à 100 % peut effacer énergiquement les détails à l'intérieur d'un groupe de faces, tout en préservant à peu près sa bordure.

### Relâcher et lisser les bordures des groupes de faces {#relax-and-smooth-facegroup-borders}

L'option `Relâcher` de l'outil Groupe de faces lisse très bien les bordures des groupes de faces tout en préservant le reste. C'est une excellente façon d'obtenir des bordures de groupes bien lisses avant un remaillage en quads.

## Limites des tablettes et mobiles {#limitations-on-tabletmobile}

Les tablettes et mobiles actuels sont très puissants, mais présentent des différences importantes avec les ordinateurs de bureau et portables :

### Pas de refroidissement actif {#no-active-cooling}

Les ordinateurs ont des ventilateurs et/ou de gros dissipateurs pour rester au frais, et sont conçus pour fonctionner à haute température. Le matériel mobile, lui, est d'abord pensé pour être fin, pas pour garder ses composants au frais. Si Nomad tourne avec ses réglages de qualité les plus élevés (mode d'éclairage PBR, matériaux complexes, beaucoup d'objets, de nombreuses options de post-traitement activées), l'appareil peut surchauffer et la batterie se vider très vite. 

Mieux vaut utiliser le mode d'éclairage MatCap, et une `Résolution de rendu` plus basse (en haut du menu Post-traitement). Ces choix gardent l'appareil au frais et vous permettent de sculpter plus longtemps.

### Mémoire limitée {#limited-memory}

Nomad peut obtenir des résultats équivalents à la plupart des applications de sculpture sur ordinateur, mais il ne peut pas défier les lois de la physique ! La plupart des ordinateurs ont deux fois plus de mémoire que les appareils mobiles, et les stations de travail conçues pour l'animation 3d en ont souvent 4 ou 8 fois plus. Il est donc bon de garder un œil sur le nombre de polygones que vous utilisez : faites quelques tests sur votre appareil pour voir à partir de quand il commence à ralentir. Presque tous les appareils capables de faire tourner Nomad gèrent assez facilement 1 million de polygones. Un iPad Pro M2 en gère confortablement 8 millions, et certains ont testé les derniers iPad bien au-delà.

Cela dit, seules les sculptures les plus détaillées ont besoin de plus de 4 millions de polygones ; si vous faites des objets relativement simples et que vous dépassez souvent 500 000, 1 million ou 4 millions, vous utilisez trop de polygones ! Vérifiez que l'`Ombrage lisse` est activé dans les [Réglages](settings.md).

### Le système est moins tolérant avec les applications gourmandes {#os-is-less-forgiving-with-intensive-apps}

Apple et Android s'attendent à ce que les applications enregistrent et chargent de petits fichiers très vite. Ils supposent aussi qu'elles peuvent passer d'une tâche à l'autre très rapidement. Là encore, Nomad utilise quelques astuces pour garder des fichiers relativement petits et les enregistrer très vite, mais si le système mobile estime que Nomad prend trop de temps, il le ferme tout simplement avant qu'il ait terminé. C'est une raison de plus de garder des fichiers plutôt légers ; il est possible de travailler sur des sculptures de 37 millions de polygones, comme l'a signalé un utilisateur sur Discord, mais ce n'est pas recommandé !

## Travailler sur un petit écran {#working-on-small-screens}

Nomad est conçu pour les tablettes, mais fonctionne bien aussi sur téléphone. Sculpter sur un petit écran comme celui d'un téléphone devient plus facile avec quelques ajustements de l'interface et de votre façon de travailler :

* Un toucher à 4 doigts masque ou affiche toute l'interface, pour vous laisser plus de place pour sculpter.
* Un glisser à 3 doigts vers le haut ou le bas change le rayon du pinceau.
* Vous pouvez réduire la taille de l'interface pour afficher plus de boutons si vous avez une bonne vue, ou l'agrandir dans le cas contraire !
* Les menus les plus larges peuvent parfois gêner la sculpture : vous pouvez les rendre transparents et sans flou pour voir la sculpture sous le menu.
* Si vous sculptez au doigt, utilisez l'option [`Décalage de trait`](stroke.md#stroke-offset) pour éloigner un peu le centre du pinceau de votre doigt.
* Ces options, et bien d'autres, se trouvent dans le [menu Interface](./interface.md). 


## Déformateur de gonflement ou de pointe {#inflate-or-peak-deformer}

Beaucoup d'applications 3d proposent un déformateur de gonflement, qui pousse tous les sommets le long de leur normale d'une quantité réglable. Nomad n'a pas encore de déformateurs, mais vous pouvez imiter ce comportement avec le pinceau Gonfler :

* Sélectionnez le pinceau Gonfler
* Dans le [menu Trait](./stroke.md#stroke), passez le type de trait sur `Saisie + rayon`
* Rendez le rayon du pinceau plus grand que votre sculpture ; si besoin, éloignez la caméra de la sculpture.
* Touchez puis faites glisser un trait sur la surface de votre objet : quand le rayon est plus grand que l'objet, toute la forme est gonflée uniformément d'une quantité fixe.
* Réglez l'intensité du pinceau pour contrôler le gonflement
* Si besoin, utilisez le masquage pour protéger certaines zones ou y réduire l'effet du gonflement.

## Supprimer les bosses ou « boutons » après un remaillage voxel {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Le remaillage voxel est idéal pour obtenir des polygones régulièrement espacés, mais crée parfois une topologie qui provoque de petites bosses ou des « boutons » au lissage. Par exemple :

* Utilisez le pinceau Pli sur la sphère par défaut pour tracer une spirale
* Faites un remaillage voxel avec `Construire une multirésolution` à 3
* Lissez avec une forte intensité
* Des artefacts apparaissent (plus faciles à voir avec un matcap très contrasté) :

![](/videos/tip_pimples_before.mp4)

Pour corriger en sculptant, essayez l'option `Lissage stable` dans les réglages de Lisser. Elle s'accommode de la topologie irrégulière du remaillage voxel, et donne un résultat propre.

![](/videos/tip_pimples_stable_smooth.mp4)

Pour corriger la topologie elle-même, utilisez une nouvelle primitive, les outils de remaillage en quads, ou un modeleur 3d externe, puis projetez les détails du maillage d'origine sur le nouveau via `Divers -> Baking -> Reprojeter → Sommet`. 

![](/videos/tip_pimples_reproject.mp4)

## Éclairage de plein jour {#daylight-lighting}

Le rendu PBR par défaut est, comme son nom l'indique, basé sur la physique : comme une photo numérique non retouchée, il peut paraître un peu terne et plat. Les lumières et le post-traitement de Nomad permettent de rendre les images plus éclatantes.

Voici un rendu par défaut ; voyons si nous pouvons l'améliorer :
![](/images/tips_lighting_default.webp)

Activer le post-traitement et le mappage tonal ajoute de la luminosité et du contraste :

![](/images/tips_lighting_tonemap.webp)

Côté lumières, l'éclairage d'environnement par défaut convient bien pour sculpter, mais peut être amélioré pour un rendu final. Une façon d'y réfléchir est de séparer la lumière directe (par exemple le soleil) de la lumière d'environnement (par exemple celle du bleu du ciel, ou du sol). En réduisant la lumière d'environnement et en la faisant pivoter, on commence à obtenir l'éclairage qu'aurait le sujet s'il se trouvait à l'ombre :

![](/images/tips_lighting_env.webp)

On peut ajouter une lumière directe, et augmenter son intensité pour simuler un soleil franc. En l'équilibrant avec la lumière d'environnement, on obtient un résultat agréable :

![](/images/tips_lighting_sunlight.webp)

Les personnages gagnent à passer leur matériau en transluminescence, avec un projecteur placé derrière eux et dirigé vers les oreilles pour les faire rayonner :

![](/images/tips_lighting_sss.webp)

Expérimentez ensuite avec le reste des réglages de post-traitement ! L'illumination globale et l'occlusion ambiante rendent l'éclairage plus réaliste. La courbure et la netteté aident à faire ressortir les détails de la sculpture. L'aberration chromatique, la profondeur de champ, le grain, l'éclat et le vignettage simulent des effets d'appareil photo. Notez qu'à mesure que vous activez des fonctions, il faut ajuster l'éclairage et les autres valeurs de post-traitement pour compenser.

Voici le rendu avec une série complète de réglages de post-traitement :
![](/images/tips_lighting_final.webp)
