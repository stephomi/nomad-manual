# ![](/icons/open.webp) Fichiers {#files}

Le menu Fichiers vous permet d'enregistrer et de charger des projets Nomad, d'importer et d'exporter des modèles 3d, d'exporter des images de rendu, et de relier Nomad à d'autres applications. Il comporte trois onglets : `Fichiers`, `Rendu` et `Liaison`.

![](/images/file_menu.webp)

## Projet {#project}
![](/images/file_project.webp)

La miniature en haut montre le projet en cours, avec à côté la taille de son fichier, la sauvegarde automatique et l'historique enregistré. Touchez la miniature pour ouvrir un mini navigateur de vos projets, puis touchez un projet pour obtenir un menu permettant de l'ouvrir, l'ajouter, le remplacer, le cloner, le renommer ou le supprimer.

Quand le projet contient des modifications pas encore enregistrées, `Modifications non enregistrées !` s'affiche sous la miniature.

### Emplacement {#scope}
Sur ordinateur, choisissez où vos projets sont enregistrés :
* `Interne` - le réglage par défaut, comme sur mobile. Les projets sont enregistrés uniquement dans le dossier principal de Nomad.
* `Sur place` - quand vous ouvrez un projet situé hors du dossier de Nomad, l'enregistrement remplace le fichier d'origine. La sauvegarde automatique ne fonctionne pas pour ces projets externes.

### ![](/icons/nomad.webp) Préréglage {#preset}
Accédez à une collection de démos et d'éléments de personnages. Sélectionnez-en un, puis sélectionnez-le à nouveau pour choisir de l'`Ouvrir` ou de l'`Ajouter à la scène`. Ce navigateur permet aussi de télécharger des modèles gratuits depuis Poly Haven.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Historique... {#history}
Accès rapide aux options d'historique du projet, comme `Enregistrer l’historique`, qui conserve votre historique d'annulation quand le projet est enregistré. Un badge vert sur le bouton indique que l'historique est enregistré avec le projet. Voir [Historique](history.md#save-history) pour plus de détails.

### ![](/icons/save.webp) Enregistrer {#save}
Enregistre le projet Nomad. Si le projet n'a jamais été enregistré, un nom vous sera demandé.

### ![](/icons/save_as.webp) Enregistrer sous... {#save-as}
Enregistre le projet sous un nouveau nom, comme un nouveau projet.

### ![](/icons/save_as.webp) Remplacer... {#overwrite}
Affiche le navigateur de projets pour enregistrer la scène en cours par-dessus un autre projet. Activez `Sélection uniquement` pour n'enregistrer que les objets sélectionnés au lieu de toute la scène. Le navigateur a aussi un bouton `Enregistrer sous...` pour enregistrer plutôt un nouveau projet.

### ![](/icons/pencil.webp) Renommer {#rename}
Affiche un champ de texte pour renommer le projet en cours.

### ![](/icons/open.webp) Ouvrir... {#open}
Affiche le navigateur de projets pour ouvrir un projet.

### ![](/icons/add_file.webp) Ajouter à la scène... {#add}
Affiche le navigateur de projets : quand vous sélectionnez un projet, son contenu est fusionné avec la scène en cours.

### ![](/icons/trash.webp) Supprimer... {#delete}
Affiche le navigateur de projets : les projets sélectionnés sont supprimés du système de fichiers.

### ![](/icons/new_file.webp) Nouveau {#new}
Démarre un nouveau projet ; s'il y a des modifications non enregistrées, une confirmation vous est demandée. Cette confirmation vous permet de `Conserver` ou de `Réinitialiser` les réglages `Arrière-plan`, `Environnement`, `MatCap` et `Rayons X`, et de choisir si le nouveau projet utilise `Enregistrer l’historique`.

### ![](/icons/autosave.webp) Sauvegarde automatique... {#auto-save}
Menu des options de sauvegarde automatique. Activez `Sauvegarde automatique` pour enregistrer votre projet dans un fichier séparé à intervalles réguliers. Le badge sur le bouton indique si elle est activée.

Si Nomad n'enregistre pas en arrière-plan, c'est parce que les fichiers 3d peuvent être assez lourds, ce qui risquerait de provoquer un ralentissement notable pendant que vous sculptez.

De plus, pour éviter de manquer de mémoire, la scène est en général compressée avant l'enregistrement.
Cette compression/décompression ralentit aussi l'enregistrement.

### Intervalle {#timer-pop-up}
Le nombre de minutes entre deux sauvegardes automatiques.

### Afficher le compte à rebours {#popup-timeout}
Affiche un compte à rebours avant chaque sauvegarde automatique, pour pouvoir l'annuler si vous êtes en plein travail. Une fois désactivé, Nomad enregistre dès que vous arrêtez de sculpter.

### ![](/icons/trash.webp) Supprimer l'auto-sauvegarde {#discard-autosave}
Si un fichier de sauvegarde automatique existe pour un projet, il est chargé automatiquement à la place du projet d'origine. Si vous n'en voulez pas, ce bouton supprime la sauvegarde automatique. Le chargement du fichier ouvrira alors le dernier enregistrement manuel du projet.

### ![](/icons/open.webp) Ouvrir la sauvegarde obsolète {#open-outdated-save}
Quand un projet a à la fois une sauvegarde automatique et un enregistrement manuel, ce bouton ouvre le plus ancien des deux (`Ouvrir la sauvegarde automatique obsolète` ou `Ouvrir la sauvegarde manuelle obsolète`), avec sa date. Pratique si la dernière sauvegarde n'est pas celle que vous vouliez.

### ![](/icons/storage.webp) Supprimés récemment... {#recently-deleted}
Nomad conserve pendant quelques jours les données des projets sortis du dossier des projets, ainsi que les fichiers remplacés par une importation, avant de les supprimer définitivement. Les fichiers dont l'importation a échoué restent jusqu'à ce que vous les supprimiez. Cette liste les affiche avec leur taille et leur date : vous pouvez les supprimer un par un ou avec `Tout supprimer`.

## Importer {#import}

### ![](/icons/add_file.webp) Importer {#import-button}
Pour importer des fichiers 3d qui ne sont pas des projets Nomad.

Quand vous importez un fichier de scène externe dans Nomad, vous pouvez soit l'*ajouter*, soit démarrer un *nouveau* projet avec.

Ajouter un fichier ajoute simplement ses objets à la scène en cours.
Choisir `Nouveau` crée un nouveau projet Nomad contenant ces objets.

La fenêtre d'importation liste tous les fichiers que vous avez choisis, chacun avec ses options d'importation. Vous pouvez aussi importer des images de cette façon : choisissez pour chacune si elle devient un `HDRI`, une `MatCap`, une `Image de référence`, un `Alpha`, des `Textures` ou un `VDM`.

Nomad peut importer ces formats :
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), sur les plateformes qui le gèrent

### ![](/icons/cog.webp) Réglages {#advanced}
Le bouton `Réglages...` à côté de la miniature du projet affiche les principales options d'importation. Ces réglages ne sont pas enregistrés, et la fenêtre d'importation montre les options qui s'appliquent aux fichiers que vous importez.

### Tous les formats {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Conserver la topologie {#keep-topology}
Par défaut, Nomad essaie de corriger la géométrie problématique au chargement. Avec cette option, Nomad ne réordonne plus les sommets et les faces, ne fusionne plus les doublons et ne supprime plus les sommets inutilisés.

::: warning
Avec `Conserver la topologie`, des opérations comme Booléen, Joindre, Décimer ou Manifold risquent de ne pas fusionner les sommets en double.
:::

#### ![](/icons/image.webp) Ignorer les textures {#skip-textures}
Ne charge pas les textures intégrées au fichier, pour les formats qui en ont, comme glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Charger les réglages UI {#keep-gui-settings}
À l'ouverture ou à l'importation d'un fichier projet, charge tous les réglages de l'interface qui y ont été enregistrés.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Scinder l'OBJ en groupes {#split-obj-by-groups}
Sépare les groupes de l'OBJ en objets distincts.

#### ![](/icons/vertex.webp) Fusionner les positions en double {#merge-duplicate-positions}
Fusionne les sommets qui ont la même position.

#### ![](/icons/uv.webp) Fusionner les UV en double {#merge-duplicate-uvs}
Fusionne les coordonnées de texture qui ont les mêmes UV.

#### ![](/icons/paint.webp) Espace de couleur {#color-space}
Choisit comment les couleurs du fichier sont interprétées : `Auto`, `Linéaire` ou `sRGB`. Essayez de changer cette option si les couleurs semblent fausses.

#### ![](/icons/image.webp) Format {#normal-format}
Le format des cartes de normales des textures : `Auto`, `OpenGL (+Y)` ou `DirectX (-Y)`. Essayez l'autre si les détails de la carte de normales semblent inversés.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Espace de couleur {#color-space-ply}
Choisit comment les couleurs du fichier sont interprétées : `Auto`, `Linéaire` ou `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Fusionner les UV en double {#merge-duplicate-uvs-fbx}
Fusionne les coordonnées de texture qui ont les mêmes UV.

#### ![](/icons/paint.webp) Espace de couleur {#color-space-fbx}
Choisit comment les couleurs du fichier sont interprétées : `Auto`, `Linéaire` ou `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Le format des cartes de normales des textures : `Auto`, `OpenGL (+Y)` ou `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Espace de couleur {#color-space-usd}
Choisit comment les couleurs du fichier sont interprétées : `Auto`, `Linéaire` ou `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Le format des cartes de normales des textures : `Auto`, `OpenGL (+Y)` ou `DirectX (-Y)`.



## Exporter {#export}
Enregistre dans un format de géométrie 3d utilisable dans d'autres logiciels. 

![](/images/file_export.webp)

Chaque format de fichier gère des fonctionnalités différentes : les options disponibles changent selon le type de fichier choisi.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Couleurs des sommets](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR aux sommets](#pbr-paint)   | ✅     | Nomad ✅<br>Autres ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Autres ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Calques](#layers)              | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objets                          | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Groupe de faces                 | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hiérarchie                      | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lumières                        | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitives, post-traitement, etc. | ✅   | Nomad ✅<br>Autres ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Bouton d'exportation {#export-button}
Touchez-le pour exporter la géométrie avec les réglages choisis. Le bouton affiche le format choisi et une estimation de la taille du fichier. Sur Android, un bouton `Partager` à côté envoie directement le fichier vers une autre application.

### Format de fichier {#file-format}
Choisissez le format d'exportation : `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` ou `USD`. NOMAD est le format propre à Nomad : il ne s'ouvre pas dans d'autres logiciels, il sert donc surtout à réimporter dans Nomad.

### Inclure {#allvisibleselected}
Choisissez quels objets seront exportés : `Tout`, `Visible` ou `Sélectionné`. Le nombre à côté de chaque option indique combien d'objets seront exportés.

### Un fichier par objet {#one-file-per-object}
Exporte chaque objet dans son propre fichier. Le nombre indique combien de fichiers seront écrits.

### Type {#type}
Quand l'exportation écrit plusieurs fichiers (un fichier par objet, ou un OBJ avec des textures), enregistrez-les dans un `Dossier` ou un `Zip`. Certaines applications (Google Drive, One Drive, etc.) ne gèrent pas l'importation de dossiers : utilisez alors Zip.

### Intégrer l’historique {#embed-history}
NOMAD uniquement. Inclut l'historique d'annulation dans le fichier ; il sera restauré à l'ouverture du fichier dans Nomad. Cela augmente la taille du fichier, et toute la scène doit être exportée en un seul fichier.

### Intégrer les ressources {#embed-assets}
NOMAD uniquement. Inclut vos matcaps, environnements et polices personnalisés dans le fichier. Les ressources fournies avec l'application ne sont pas intégrées.

### Couleurs des sommets {#vertex-colors}
Exporte les couleurs des sommets si le format de fichier les gère. Certains logiciels 3d savent les lire, mais pas tous.

Pour l'OBJ, vous avez le choix :
* `Aucun` - pas de couleurs.
* `RGB` - les couleurs sont ajoutées après les sommets.
* `MRGB (ZBrush)` - une autre façon de coder la couleur, qui gère aussi les données de masque.

### Espace de couleur {#color-space-export}
OBJ uniquement, avec les couleurs de sommets `RGB`. Écrit les couleurs en `Linéaire` ou en `sRGB`.

### Peinture PBR {#pbr-paint}
Exporte la peinture de rugosité, de métallité et de masque. D'autres logiciels peuvent ignorer ces données.
Les couleurs de sommets PBR sont exportées comme attributs de couleurs de sommets secondaires.
Les canaux sont regroupés de la façon suivante :

|           | Canal    |
| :-------: | :------: |
| Rugosité  | R        |
| Métallité | G        |
| Masque    | B        |


### Calques {#layers}
Les calques sont gérés via les morph targets glTF. glTF les prend officiellement en charge, ils devraient donc aussi fonctionner dans d'autres logiciels.
Nomad exporte aussi les couleurs, la rugosité et la métallité de chaque calque, mais les autres logiciels les ignorent.

### Peinture (calque) {#layer-painting}
Exporte la peinture des calques, en général ignorée par les autres logiciels.

### Groupe de faces {#face-group}
Exporte les groupes de faces ; cet export peut parfois gêner d'autres logiciels.

### Écrire les objets {#write-objects}
OBJ uniquement. Garde les objets séparés. Désactivez-le pour tout exporter en un seul objet, par exemple pour utiliser la fonction 'Mesh ID / Polygroup' de Substance Painter.

### Normales {#normals}
Exporte les informations de normales. Notez que Nomad calcule toujours ses propres normales quand il importe d'autres formats de fichier.

### Tangentes {#tangents}
Exporte les informations de tangentes, utilisées si le modèle a des cartes de normales. 

### Textures {#textures}
Si des textures ont été ajoutées au matériau, elles sont exportées. Notez que cela ne fait pas de baking de textures : celui-ci se fait avec les options de baking du menu Topologie.

### Format {#fbx-format}
FBX uniquement. `Binaire` est plus compact mais peut ne pas fonctionner dans toutes les applications ; `Ascii` est un fichier texte.

### Compressé {#compressed}
FBX uniquement. Réduit la taille du fichier, au prix d'une exportation et d'une importation plus lentes.

### Préréglage {#usd-preset}
USD uniquement. Choisissez l'application pour laquelle vous exportez : `OpenUSD`, `Apple`, `Procreate` ou `Zbrush`. Certaines options ne sont disponibles qu'avec certains préréglages.

### Instance {#instance}
USD uniquement. Exporte les objets instanciés sous forme d'instances, au lieu de dupliquer leur géométrie.

### Autoriser le cisaillement {#allow-skew}
USD uniquement. Autorise le cisaillement dans les matrices de transformation. Une fois désactivé, Nomad décompose les transformations cisaillées en transformations séparées d'échelle et de rotation.

### Répéteur {#repeater}
USD uniquement. Exporte les copies créées par les répéteurs sous forme d'instances.

### Fusionner les copies {#join-copies}
Chaque objet et les copies de son répéteur deviennent un seul objet.

::: tip Astuce : importer la rugosité et la métallité dans Blender

Blender sait importer le glTF/glb, mais ne comprend pas automatiquement les attributs de sommets pour la métallité et la rugosité. Pour les utiliser, créez un nœud Vertex Color dans l'éditeur de matériaux, et réglez sa propriété sur l'attribut de couleur suivant (en général Col.001). Branchez-y un nœud 'Separate XYZ', envoyez X vers Roughness et Y vers Metallic.

Cette vidéo montre la marche à suivre :

![](/videos/blender_pbr.mp4)

::: 

::: tip Astuce : fonctionnalités gérées en USD

USD est un format complexe : sa spécification prévoit de nombreuses fonctionnalités, mais tous les logiciels 3d ne les gèrent pas. Par exemple, OSX/iOS ne gèrent pas les couleurs de sommets. Les modes de préréglage de l'exportateur USD tentent d'offrir la meilleure compatibilité possible avec OpenUSD, Apple, Procreate et Zbrush.

::: 

## ![](/icons/screen.webp) Rendu {#render}

Exporte une image qui combine tous les réglages du projet (lumières, matériaux, post-traitement, etc.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Aperçu {#preview}

Le bouton `Aperçu` à côté du titre du menu rend l'interface transparente, pour vous aider à juger du cadrage du résultat final.

### ![](/icons/home.webp) Mise au point {#focus}
Cadre la scène ou la sélection pour qu'elle tienne dans la taille du rendu. Touchez à nouveau pour passer de l'une à l'autre.

### ![](/icons/map.webp) Carte de hauteur {#heightmap}
Rend la scène sous forme de carte de hauteur en niveaux de gris vue depuis la caméra, les parties les plus proches étant les plus claires. L'activer passe à la taille `Carré` et cadre la sélection. Une petite barre dans la vue vous permet d'ajuster la `Mise au point` du dégradé.

Quand `Carte de hauteur` est activé, un bouton `Enregistrer comme alpha` apparaît à côté du bouton d'exportation, pour enregistrer le rendu comme nouvel alpha de pinceau au lieu d'exporter un fichier.

### ![](/icons/opacity.webp) Arrière-plan transparent {#transparent-background}
Ajoute un canal alpha au rendu, utile pour combiner le rendu avec d'autres images dans des logiciels 2d. Notez que la transparence partielle n'est pas gérée.

### ![](/icons/sliders.webp) Afficher l'interface {#show-interface}
Inclut l'interface de Nomad dans le rendu.

### Taille finale {#final-size}
La résolution du rendu : `Écran`, `720`, `1080`, `4096`, `Carré` ou `Personnalisée`.

Quand le menu Fichiers est ouvert, un cadre en pointillés s'affiche dans la vue pour indiquer la zone de rendu, si elle ne correspond pas à la résolution de l'écran.

### Largeur / Hauteur {#render-ratio}
Avec `Personnalisée`, réglez la largeur et la hauteur de l'image. Le bouton de liaison entre les deux curseurs conserve les proportions quand vous modifiez l'un d'eux. Avec `Carré`, seule la largeur est réglable.

### ![](/icons/export.webp) Exporter → PNG {#export-png}
Touchez ce bouton pour lancer le rendu. Une fois terminé, vous pouvez choisir comment enregistrer ou partager l'image. Les très grandes tailles demandent d'abord une confirmation : enregistrez votre projet avant, au cas où votre appareil manquerait de mémoire.

## ![](/icons/network.webp) Liaison {#link}

Connectez Nomad à un autre appareil ou à une autre application, pour envoyer et recevoir des objets, ou pour synchroniser vos modifications en direct. Un appareil héberge la session, les autres la rejoignent.

### Activer GoZ {#enable-goz}
Sur ordinateur uniquement. Échange des maillages avec ZBrush sur cet ordinateur. `Envoyer` les importe dans ZBrush, `Récupérer` importe depuis le ZBrush ouvert : `Sélection` prend le subtool actif, `Scène` prend tous les subtools. Vous pouvez aussi appuyer sur GoZ dans ZBrush à tout moment.

### Mode {#link-mode}
* `Désactivé` - pas de liaison.
* `Hôte` - cet appareil héberge la session et attend que d'autres la rejoignent.
* `Rejoindre` - cherche les appareils à proximité ; touchez ensuite le nom de l'hôte pour le rejoindre.

Pour relier deux Nomad, choisissez `Hôte` sur un appareil et `Rejoindre` sur les autres. Pour une liaison avec Blender, Nomad doit être l'hôte : le bouton d'aide à côté du titre `Liaison` explique comment installer l'extension Nomad Blender Link.

### ![](/icons/network.webp) Port réseau {#network-port}
Le port réseau utilisé par la liaison. Ne le changez que si une autre application l'utilise déjà.

### Envoyer / Récupérer {#send-get}
Une fois connecté, utilisez `Envoyer` pour transmettre votre `Sélection` ou toute la `Scène` à l'autre appareil, ou `Récupérer` pour les obtenir depuis celui-ci. `Remplacer` supprime la scène en cours, puis récupère la scène de l'autre appareil.

### ![](/icons/link.webp) Synchronisation en direct {#live-sync}
Transmet vos modifications à l'autre appareil au fil de votre travail. `Vue de travail` synchronise aussi la caméra. `Modifications de la scène` indique quel appareil envoie les modifications : `Auto` donne la main à l'appareil le plus récemment actif. Choisissez ensuite ce qui est synchronisé : `Objets et géométrie`, `Matériaux`, `Lumières`, `Caméras`, et, quand l'autre côté le gère, `Ombrage` et `Post-traitement`.

::: tip
Les objets existants doivent d'abord passer une fois par `Envoyer` ou `Récupérer`, pour être liés avant que la synchronisation en direct puisse les mettre à jour.
:::
