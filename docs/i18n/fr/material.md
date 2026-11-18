# ![](/icons/material.webp) Matériau {#material}

Ce menu vous permet de changer le matériau de l'objet actuel, les propriétés de rendu de l'objet et du matériau, et d'attribuer des textures au matériau.

![](/images/material_overview.webp)

Les matériaux définissent l'apparence d'un objet, en déterminant comment il réagit à la lumière et aux autres objets. L'apparence d'un objet dépend de ces propriétés :

* `Type de matériau`
* `Couleur`
* `Rugosité`
* `Métallité`
* `Opacité`
* `Réflectance`
* `Émissif/Sans éclairage`

En combinant ces propriétés, vous obtenez une grande variété de résultats, du photoréaliste au cartoon en passant par l'expérimental.

La couleur, la rugosité, la métallité et l'opacité peuvent être peintes, voir les [options de peinture aux sommets](painting.md) pour en savoir plus.

Le type de matériau, la réflectance et l'émissif/sans éclairage sont des propriétés du matériau expliquées ci-dessous.

Les boutons `Copier` et `Coller` en haut de ce menu vous permettent de copier un matériau d'un objet à un autre.

Notez que le moteur de rendu de Nomad est un moteur temps réel : bien que puissant, il privilégie la vitesse plutôt que l'exactitude pour certains effets. 

## Types de matériaux {#material-types}

![](/images/material_types.webp)

Les types de matériaux de Nomad sont Opaque, Transluminescence, Fusion, Additif, Réfraction, Tramage et Capteur d'ombres.

### ![](/icons/material_opaque.webp) Opaque {#opaque}
Le mode par défaut, qui traite les surfaces comme un matériau simple qui gère la couleur, la rugosité, la métallité et l'opacité peintes. L'opacité peinte, une texture d'opacité ou le canal alpha de la texture de couleur rendent quand même l'objet transparent, par tramage. Seul le curseur d'opacité principal est ignoré.

### ![](/icons/material_subsurface.webp) Transluminescence {#subsurface}
Ce mode simule les matériaux dans lesquels la lumière se diffuse et s'étale à l'intérieur, comme la peau, la cire ou le jade.

Il nécessite le mode d'ombrage PBR. Pour un meilleur résultat, utilisez au moins une lumière directionnelle ou un spot, idéalement avec un environnement sombre.

La pastille de couleur règle la couleur de la lumière diffusée.

`Profondeur` règle jusqu'où la lumière se diffuse depuis l'avant, sous la surface, puis ressort par la surface avant. Cela adoucit les ombres dures et estompe les détails de la surface.

`Translucidité` règle la diffusion de la lumière de l'avant vers l'arrière d'une forme, comme la lumière qui traverse le dessous d'une feuille, ou des oreilles fortement éclairées par derrière. Il vous faut une lumière qui projette des ombres pour la voir.

### ![](/icons/material_blending.webp) Fusion {#blending}

Semblable à Opaque, mais gère le curseur d'opacité pour que le matériau passe progressivement de plein à transparent. C'est un simple curseur d'opacité unique, contrairement à l'opacité peinte que gère le matériau opaque. 

::: warning
Le mode Fusion peut provoquer des scintillements et des sauts d'affichage sur des formes complexes ou qui se croisent.
:::

### ![](/icons/material_additive.webp) Additif {#additive}
Ce matériau rend votre maillage semi-transparent. Il ressemble au matériau Fusion, mais alors que Fusion se mélange à son environnement, Additif est toujours plus lumineux que les objets derrière lui : idéal pour des effets lumineux comme des rayons de lumière, du feu ou des explosions.

Vous pouvez régler une opacité supérieure à 1, ce qui rend l'objet plus lumineux.  
C'est utile si vous voulez utiliser l'[Éclat](postprocess.md#bloom) et son paramètre `Seuil` pour ne faire briller que cet objet, comme un objet émissif.

Ce mode a tendance à produire moins d'artefacts que [Fusion](#blending) (transparence indépendante de l'ordre).

### ![](/icons/material_refraction.webp) Réfraction {#refraction}
Ce mode permet de simuler un matériau comme le verre. Il nécessite le mode d'ombrage PBR. À cause des contraintes du temps réel, l'auto-réfraction et la réfraction à plusieurs couches sont assez limitées.

La rugosité peinte sur le modèle détermine le flou de la réfraction.
Par défaut, chaque objet créé dans Nomad a une rugosité d'environ 25 % : la réfraction n'est donc pas parfaite, mais un peu floue.
Le bouton `Peindre brillant` repeint votre modèle avec une rugosité et une métallité de 0 (les couleurs ne sont pas modifiées).

Deux rugosités différentes entrent en jeu : celle qui détermine le flou du reflet à la surface, et celle qui détermine le flou de l'intérieur (la réfraction).  
Mais comme Nomad n'a qu'un seul canal de rugosité peinte, la rugosité intérieure et la rugosité extérieure partagent la même valeur.  
Pour avoir des valeurs différentes (par exemple une sucette à la surface nette mais à l'intérieur flou), utilisez les curseurs `Surface` et `Intérieur` sous `Remplacer la rugosité` pour remplacer la rugosité peinte.

![](/videos/refraction.mp4)

#### Indice de réfraction {#index-of-refraction}
À quel point la lumière est déviée en entrant dans l'objet. Plus la valeur est élevée, plus elle est déviée, comme avec une lentille épaisse.

#### Absorption {#absorption}
Simule la lumière absorbée pendant sa traversée du volume, teintée par la pastille de couleur, avec `Facteur` pour en régler la force. Les parties fines sont plus claires car elles laissent passer plus de lumière, tandis que les zones épaisses sont plus sombres. Nomad n'utilise qu'une approximation de l'épaisseur de l'objet : l'effet dépend donc beaucoup de la forme.


### ![](/icons/material_dithering.webp) Tramage {#dithering}
Rend l'objet semi-transparent en supprimant certains pixels de façon aléatoire.

### ![](/icons/material_shadow_catcher.webp) Capteur d'ombres {#shadow-catcher}

Rend l'objet invisible, en ne gardant que les ombres qu'il reçoit des lumières. Utile pour combiner des rendus de Nomad avec d'autres images, généralement sur un plan. La pastille de couleur règle la couleur de l'ombre.

Une lumière qui projette des ombres doit être présente dans la scène, sinon le capteur d'ombres n'a aucun effet. Les boutons `Métallité → 0%` et `Métallité → 100%` repeignent l'objet : entièrement métallique, le capteur d'ombres peut aussi refléter la scène quand le post-traitement [Réflexion (SSR)](postprocess.md#reflection-ssr) est activé.

::: tip

Vous trouverez plus d'informations sur la transparence et les modes de fusion sur https://support.fab.com/s/article/Transparency-Opacity

:::

## Commandes {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Toujours sans éclairage {#always-unlit}
Si cette option est activée, l'objet ignore le PBR et le MatCap et affiche simplement sa couleur peinte, sans ombrage.
Notez qu'avec [Additif](#additive), vous pouvez peindre directement la transparence en utilisant du noir.

### Opacité {#opacity}
À quel point un objet paraît plein ou opaque : 100 % est plein, 0 % est transparent. Le curseur s'affiche pour les types Fusion, Additif, Tramage et Capteur d'ombres. Vous pouvez aussi peindre l'opacité pour un contrôle plus fin.

### Passe de pré-réfraction {#pre-refract-pass}
Fusion et Additif uniquement. Dessine cet objet transparent avant la passe de réfraction. Utile quand un objet réfractif se trouve devant d'autres surfaces transparentes.

### Réflectance {#reflectance}
Règle la quantité de reflet que reçoivent les matériaux non métalliques. La plupart du temps, gardez la valeur par défaut (qui correspond aux 4 % standard de lumière réfléchie sous incidence normale), mais vous pouvez l'augmenter pour renforcer les reflets et les éclats dans les yeux d'un personnage, par exemple. Elle nécessite le mode d'ombrage PBR.

### ![](/icons/culling.webp) Inverser le culling {#inverse-culling}
Inverse les normales d'une surface. Ce n'est généralement pas nécessaire, mais cela peut servir si un modèle apparaît à l'envers, ou, combiné avec `Recto verso` désactivé, pour créer des intérieurs dont le mur le plus proche de la caméra est toujours caché.

Les options suivantes peuvent valoir `Auto`, `Non` ou `Oui`. Avec `Auto`, la flèche indique la valeur réellement utilisée.

### ![](/icons/sphere_smooth.webp) Ombrage lisse {#smooth-shading}
Voir l'[option globale](settings.md#smooth-shading).  
La valeur `Auto` utilise l'option globale.

### ![](/icons/culling.webp) Recto verso {#two-sided}
Les faces sont visibles des deux côtés. Voir l'[option globale](settings.md#two-sided-quick).  
La valeur `Auto` utilise l'option globale.

### ![](/icons/culling.webp) Face arrière colorée {#coloured-backface}
Voir l'[option globale](settings.md#two-sided-quick).
La valeur `Auto` utilise l'option globale.

### ![](/icons/shadow_cast.webp) Projeter des ombres {#casts-shadows}
Les objets transparents projettent aussi des ombres (avec un motif tramé pour imiter des ombres semi-transparentes).  
Pensez à désactiver la projection d'ombres si votre scène contient un grand objet qui n'a pas besoin d'en projeter (par exemple un grand sol).

### ![](/icons/shadow_receive.webp) Recevoir des ombres {#recieve-shadows}
Indique si les ombres des autres objets sont dessinées sur cet objet.

### ![](/icons/wireframe.webp) Filaire {#wireframe}
Voir l'[option globale](settings.md#wireframe).  
La valeur `Auto` utilise l'option globale.

### ![](/icons/trash.webp) Réinitialiser les normales {#reset-normals}
Affiché seulement quand un objet importé contient ses propres normales (par exemple avec `Conserver la topologie`). Il les supprime, pour que l'ombrage utilise les normales calculées à partir de la surface.


## Textures {#textures}

![](/images/material_textures.webp)

Si un objet a des UV, vous pouvez appliquer des textures au matériau en plus de la couleur, de la rugosité, de la métallité et de l'opacité des sommets. Elles proviennent généralement d'un baking de textures, mais vous pouvez aussi utiliser des images créées en dehors de Nomad. `UV:✓` ou `UV:✗` à côté du titre vous indique si l'objet a des UV.

Des textures peuvent être appliquées à :

* Couleur
* Normale
* Rugosité
* Métallité
* Opacité
* Déplacement
* Émissif

Une ligne `Occlusion` apparaît aussi quand un objet importé a une texture d'occlusion, mais Nomad ne l'utilise pas.

Le curseur de chaque ligne règle la force d'application de sa texture, de nulle à totale. `Couleur` et `Émissif` ont aussi une pastille de couleur qui teinte la texture, et `Émissif` règle l'intensité de la lueur.

`Déplacement` règle jusqu'où la carte de déplacement pousse la surface. Son bouton `Appliquer` déplace les sommets selon le déplacement, puis supprime la carte. Le résultat va dans le calque actif.

Le bouton de palette à côté du titre ouvre les préréglages de matériau du menu [Peinture](painting.md) : touchez-en un pour copier ses textures sur l'objet. Sur ordinateur, les images importées se synchronisent avec leur fichier d'origine quand vous revenez dans Nomad, et un bouton de synchronisation à côté du titre les recharge.

Toucher un emplacement de texture ouvre un sélecteur. Une fois qu'une texture est attribuée à un emplacement du matériau, toucher à nouveau l'emplacement ouvre un panneau de texture :

### Options du panneau de texture {#texture-panel-options}

![](/images/material_texture_panel.webp)

Le panneau affiche la taille de l'image et un aperçu de la texture.

### ![](/icons/open.webp) Ouvrir {#open}
Choisit une autre texture. Sur ordinateur, `Explorer` affiche le fichier image dans votre explorateur de fichiers.

### ![](/icons/circle_cross.webp) Aucun {#none}
Supprime la texture

### Opacité {#texture-opacity}

Texture de couleur uniquement. Si l'image a un canal alpha, vous pouvez l'utiliser pour l'opacité, ou l'ignorer.

### Format {#normal-format}
Texture de normales uniquement. Les cartes de normales existent en deux variantes, `OpenGL (+Y)` et `DirectX (-Y)`. Si les détails semblent inversés, essayez l'autre.

### Hauteur {#displacement-height}
Texture de déplacement uniquement.
* `Local` - La hauteur grandit et rétrécit avec l'échelle de l'objet.
* `Global` - La hauteur reste la même quelle que soit l'échelle de l'objet.

### Multiplier {#multiply}
Textures de rugosité, de métallité et d'opacité uniquement. Multiplie les valeurs de la texture. Quand la valeur n'est pas à 100 %, elle s'affiche sur l'emplacement de texture.

### ![](/icons/link.webp) Icône de lien {#chainlink-icon}

Quand l'icône de lien des sections suivantes est activée, les options choisies sont partagées avec les autres textures (couleur, normale, rugosité, métallité, opacité, émissif) dont l'icône de lien est aussi activée. 

Ainsi, si vous avez des textures alignées, elles restent alignées même quand vous modifiez les paramètres ou le type de projection.


### Projection {#projection}
![](/images/material_projection.webp)

Détermine comment la texture est appliquée à l'objet.

* `Auto` - UV si l'objet a des UV, sinon Triplanaire
* `UV` - Utilise les coordonnées UV du maillage pour appliquer la texture. Si le maillage et la texture viennent d'ailleurs que de Nomad, ou s'ils seront exportés de Nomad pour être utilisés ailleurs, UV est la bonne option.
* `Triplanaire` - Projette la texture selon les axes X, Y et Z, et fond les raccords. 

### Triplanaire {#triplanar}
![](/images/material_triplanar.webp)

Les projections triplanaires sont un moyen à la fois simple et puissant d'appliquer des textures aux objets.

Le triplanaire, c'est comme avoir 6 vidéoprojecteurs qui projettent tous la même image sur l'avant, l'arrière, la gauche, la droite, le dessus et le dessous de votre objet.

Le résultat peut ensuite être appliqué par baking dans des UV ou dans les couleurs des sommets si besoin.


![](/images/material_triplanar_example.webp)

#### Méthode {#method}

* `Local` - La projection suit la transformation de l'objet
* `Global` - Les projections restent fixes : déplacer l'objet le fait glisser à travers la projection.

#### Dureté {#hardness}

La façon dont les projections se mélangent. À 100 %, il n'y a aucun fondu, et les bords des projections sont nets. À 0 %, les bords se fondent sur un large angle. La valeur par défaut est de 90 % : assez de fondu pour cacher les bords, tout en gardant le reste des projections net.

### Uniforme {#uniform}

Quand cette case est cochée, la même dureté s'applique à toutes les projections. Quand elle est décochée, des réglages de dureté supplémentaires apparaissent pour les projections X, Y et Z.


### Paramètre {#parameter}
![](/images/material_parameter.webp)

#### Filtrage {#filtering}
La méthode de filtrage de la texture : `Auto` par défaut, ou `Au plus proche`, `Linéaire`, `Mipmap`. Au plus proche ne filtre pas du tout : les textures peuvent donc présenter des artefacts crénelés vues de près. Linéaire et Mipmap filtrent mieux : de près, les textures paraissent floues plutôt que crénelées.

#### Recouvrement - X {#tiling-x}
Si le paramètre Échelle est supérieur à 1, ce qui rend la texture plus petite que les UV de l'objet, détermine comment la texture se répète le long de l'axe X. `Aucun` signifie aucune répétition. `Répéter` fait des copies de la texture. `Miroir` fait des copies de la texture en inversant une copie sur deux, ce qui peut aider à cacher les artefacts de répétition.

#### Recouvrement - Y {#tiling-y}
Comme Recouvrement - X, mais pour l'axe Y.

### Transformation {#transform}
![](/images/material_transform.webp)

Des transformations 2d supplémentaires appliquées à la texture dans l'espace UV. Le bouton de réinitialisation remet les valeurs par défaut ; l'icône de lien (quand une texture autre que la couleur est sélectionnée) lie ou délie la transformation de celle de la texture de couleur.

#### Translation {#translation}
Le décalage de la texture en X et en Y

#### Rotation {#rotation}
La rotation de la texture

#### Échelle {#scale}
L'échelle de la texture : plus la valeur est grande, plus la texture est petite sur l'objet. Utilisez les options Recouvrement - X et Recouvrement - Y pour choisir ce qui se passe alors.

### Échelle uniforme {#uniform-scale}
Quand cette option est désactivée, Nomad affiche des réglages séparés pour Échelle X et Échelle Y.
