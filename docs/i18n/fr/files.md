# ![](/icons/open.webp) Fichiers {#files}

Le menu Fichiers vous permet d’enregistrer et de charger des projets Nomad, d’importer et d’exporter des modèles 3D, et d’exporter des images rendues.

![](/images/file_menu.webp)

## Projet {#project}
![](/images/file_project.webp)

Une vignette de la dernière sauvegarde est affichée en haut de ce menu. Cliquer sur cette vignette ouvre un mini-navigateur, touchez deux fois un autre projet pour afficher un mini-menu permettant d’ouvrir, ajouter, enregistrer, cloner, renommer ou supprimer ce projet.

### ![](/icons/nomad.webp) Préréglage {#preset}
Accédez à une collection de démos et de composants de personnages. Sélectionnez-en un, puis sélectionnez à nouveau pour choisir Ouvrir, Ajouter à la scène ou Cloner l’entrée dans votre dossier de projets.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Enregistrer {#save}
Enregistrer le projet Nomad.

### ![](/icons/save_as.webp) Enregistrer sous... {#save-as}
Affiche le navigateur de projets pour vous permettre d’enregistrer le projet Nomad sous un nouveau nom.

### ![](/icons/pencil.webp) Renommer {#rename}
Affiche une zone de texte pour renommer le projet actuel.

### ![](/icons/open.webp) Ouvrir... {#open}
Affiche le navigateur de projets pour ouvrir un projet.

### ![](/icons/add_file.webp) Ajouter à la scène... {#add}
Affiche le navigateur de projets, lorsque vous sélectionnez un projet, son contenu sera fusionné avec la scène actuelle.

### ![](/icons/trash.webp) Supprimer... {#delete}
Affiche le navigateur de projets, tout projet sélectionné sera supprimé du système de fichiers.

### ![](/icons/new_file.webp) Nouveau {#new}
Démarre un nouveau projet, si des modifications n’ont pas été enregistrées il vous sera demandé si vous souhaitez les sauvegarder.

### ![](/icons/autosave.webp) Sauvegarde automatique... {#auto-save}
Menu pour contrôler les options de sauvegarde automatique.

Si vous activez la sauvegarde automatique, vous pouvez configurer un minuteur afin qu’une fenêtre contextuelle apparaisse à intervalles réguliers.
Nomad n’enregistre pas en arrière-plan car les fichiers 3D peuvent être très volumineux et cela peut provoquer un lag important pendant que vous sculptez.

De plus, pour éviter les problèmes de mémoire, la scène est généralement compressée avant l’opération de sauvegarde.
Cette compression/décompression ralentira également l’opération de sauvegarde.

### Fenêtre contextuelle du minuteur {#timer-pop-up}
Fréquence d’apparition de la fenêtre contextuelle du minuteur.

### Durée de la fenêtre contextuelle {#popup-timeout}
Activer le délai d’expiration de la fenêtre contextuelle.

### Ignorer la sauvegarde automatique {#discard-autosave}
Si un fichier de sauvegarde automatique existe pour un projet, il sera automatiquement chargé à la place du projet original. Si cela n’est pas souhaité, ce bouton supprimera la sauvegarde automatique. Le chargement du fichier utilisera alors la dernière sauvegarde manuelle du projet.


## Importer {#import}

### ![](/icons/add_file.webp) Importer {#import-button}
Pour importer des fichiers 3D qui ne sont pas des projets Nomad.

Lorsque vous importez un fichier de scène externe dans Nomad, vous pouvez soit l’*importer*, soit l’*ajouter*.

Ajouter un fichier va simplement ajouter les objets à la scène actuelle.
Importer un fichier va créer un nouveau projet Nomad contenant les nouveaux objets.

Nomad peut importer les formats suivants :
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, expérimental)

### ![](/icons/cog.webp) Avancé {#advanced}
Affiche les options d’import avancées :

### Projet/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Conserver la topologie {#keep-topology}
Par défaut, Nomad va tenter de corriger la géométrie problématique au chargement. Activer cette option empêchera Nomad de réordonner les sommets/faces, de supprimer les doublons de sommets/faces et de supprimer les sommets non utilisés.

#### Ignorer les textures {#skip-textures}
Ignorer le chargement des textures pour les formats qui les prennent en charge comme glTF.

### Projet / glTF {#project-gltf}
#### Conserver les paramètres de l’interface {#keep-gui-settings}
Activer l’enregistrement de l’interface et des paramètres du projet dans le fichier Nomad .nom ou glTF.

### OBJ {#obj}
#### Scinder l’OBJ par groupes {#split-obj-by-groups}
Activer la séparation des groupes OBJ en objets distincts.

#### Espace colorimétrique {#color-space}
Définir le mode colorimétrique interprété depuis l’OBJ en Linéaire, sRGB ou Auto.

### PLY {#ply}
#### Espace colorimétrique {#color-space-ply}
Définir le mode colorimétrique interprété depuis le PLY en Linéaire, sRGB ou Auto.


### FBX {#fbx}
#### Espace colorimétrique {#color-space-fbx}
Définir le mode colorimétrique interprété depuis le FBX en Linéaire, sRGB ou Auto.



## Exporter {#export}
Enregistrer vers un format de géométrie 3D pouvant être utilisé dans d’autres logiciels. 

![](/images/file_export.webp)

Différents formats de fichiers prennent en charge différentes fonctionnalités, les options disponibles changeront en fonction du type de fichier sélectionné.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Tout/Visible/Sélection {#allvisibleselected}
L’état du bouton actif définit quels objets seront exportés. Le nombre à côté des icônes indique combien d’objets seront exportés pour cette option.

### Couleurs de sommet {#vertex-colors}
Exporter les couleurs de sommets si le format de fichier le permet.

### Peinture PBR {#pbr-paint}
Les couleurs de sommets PBR sont exportées comme attributs secondaires de couleurs de sommets.
Les canaux sont organisés de la façon suivante :

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Couches {#layers}
Les calques sont pris en charge via les morph targets glTF.
Nomad exporte également des couleurs, rugosité et métallicité par calque, mais cela sera ignoré par les autres logiciels.

### Peinture par couche {#layer-painting}
Exporter la peinture de calques, généralement ignorée par les autres logiciels.

### Groupe de faces {#face-group}
Exporter les groupes de faces, l’export peut parfois interférer avec d’autres logiciels.

### Normales {#normals}
Exporter les informations de normales. Notez que Nomad recalculera toujours ses propres normales lors de l’import d’autres formats de fichiers.

### Tangentes {#tangents}
Exporter les informations de tangentes, utilisées si le modèle possède des normal maps. 

### Textures {#textures}
Si des textures ont été ajoutées au matériau, elles seront exportées. Notez que cela ne fera pas de baking de textures, cette opération se fait via les options de baking dans la topologie.

### Bouton d’export {#export-button}
Cliquez sur ce bouton pour exporter la géométrie en utilisant les paramètres sélectionnés.

::: tip Tip: Import roughness and metalness to Blender

Blender peut importer du glTF/glb, mais ne comprend pas automatiquement les attributs de sommets pour la métallicité et la rugosité. Pour les utiliser, dans l’éditeur de matériaux créez un nœud Vertex Color, définissez sa propriété sur l’attribut de couleur suivant (généralement Col.001). Connectez un nœud ‘Separate XYZ’, envoyez X vers Roughness et Y vers Metallic.

Cette vidéo montre le processus :

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: USD feature support

USD est un format complexe, sa spécification prend en charge de nombreuses fonctionnalités, mais tous les logiciels 3D ne les prennent pas toutes en charge. macOS/iOS ne prennent par exemple pas en charge la couleur de sommet. Les modes prédéfinis dans l’exporteur USD tentent de proposer le meilleur compromis de compatibilité avec OpenUSD, Apple, Procreate, ZBrush.

::: 

## Rendu {#render}

Exporter une image qui est la combinaison de tous les réglages du projet (lumières, matériaux, post-traitement, etc.). 

![](/images/file_render.webp)
### Aperçu {#preview}

Le petit bouton d’aperçu à côté du titre du menu va assombrir les barres d’outils pour aider à prévisualiser le résultat final.

### Arrière-plan transparent {#transparent-background}
Activer un canal alpha pour le rendu, utile pour combiner le rendu avec d’autres images dans des programmes 2D. Notez que la transparence partielle n’est pas prise en charge.

### Afficher l’interface {#show-interface}
Activer l’inclusion de l’interface de Nomad dans le rendu.

### Ratio de rendu {#render-ratio}
Un multiplicateur sur la résolution de l’image.

### Taille finale {#final-size}
La résolution à utiliser pour le rendu. Lorsque `Custom` est sélectionné, les curseurs de largeur et de hauteur sont activés. 

Lorsque le menu Fichier est actif, un cadre en pointillés est dessiné dans la vue pour indiquer la région de rendu si elle ne correspond pas à la résolution de l’écran (notez que vous devez être en mode paysage pour que ce soit correct).

### Exporter en PNG {#export-png}
Cliquez sur ce bouton pour démarrer le processus de rendu. Une fois terminé, vous pouvez choisir comment enregistrer ou partager l’image.