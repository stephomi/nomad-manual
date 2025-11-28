# ![](/icons/material.webp) Matériau {#material}

Ce menu vous permet de changer le matériau de l’objet courant, les propriétés de rendu de l’objet/matériau, et d’assigner des textures au matériau.

![](/images/material_overview.webp)

Les matériaux définissent l’apparence d’un objet, en contrôlant la façon dont il réagit à la lumière et aux autres objets. L’apparence d’un objet est contrôlée par les propriétés suivantes :

* `Type de matériau`
* `Couleur`
* `Rugosité`
* `Métallicité`
* `Opacité`
* `Réflectance`
* `Émissif/non-éclairé`

Des combinaisons de ces propriétés permettent d’obtenir une grande variété de résultats, du photoréaliste au cartoon en passant par l’expérimental.

La couleur, la rugosité, la métallicité et l’opacité peuvent être peintes, voir les [options de peinture de sommets](painting.md) pour plus d’informations.

Le type de matériau, la réflectance, émissif/non-éclairé sont des propriétés de matériau expliquées ci‑dessous.

Les boutons copier/coller en haut de ce menu vous permettent de copier des matériaux d’un objet à un autre.

Notez que le moteur de rendu de Nomad est un moteur temps réel ; bien que puissant, il privilégie la vitesse à la précision pour certains effets. 

## Types de matériau {#material-types}

![](/images/material_types.webp)

Les types de matériau Nomad sont Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaque {#opaque}
Le mode par défaut qui traite les surfaces comme un matériau simple prenant en charge la couleur, la rugosité, la métallicité et l’opacité peintes.

### ![](/icons/material_subsurface.webp) Sous-surface {#subsurface}
Ce mode peut simuler un matériau qui laisse la lumière se diffuser et se disperser en interne, comme la peau, la cire, le jade.

Pour de meilleurs résultats, passez en mode d’éclairage PBR et utilisez au moins une lumière directionnelle ou spot, idéalement avec un environnement peu lumineux.

`Depth` contrôle jusqu’où la lumière se disperse depuis l’avant, sous la surface, puis ressort par la surface avant. Cela a pour effet d’adoucir les ombres dures et de flouter les détails de surface.

`Translucency` contrôle la façon dont la lumière se disperse de l’avant vers l’arrière d’une forme, comme la diffusion à travers l’envers d’une feuille, ou lorsque des oreilles sont fortement rétro‑éclairées. 

### ![](/icons/material_blending.webp) Fusion {#blending}

Similaire à Opaque, mais prend en charge le curseur d’opacité pour permettre au matériau de passer du solide au transparent. Il s’agit d’un simple curseur unique pour l’opacité, par opposition à l’opacité peignable prise en charge par le matériau opaque. 

::: warning
Le mode Blending peut provoquer du scintillement et des sauts visuels dans les formes complexes ou qui s’intersectent.
:::

### ![](/icons/material_additive.webp) Additif {#additive}
Vous pouvez rendre votre maillage semi‑transparent avec ce matériau. Il est similaire au matériau Blending, mais alors que Blending se mélange avec son environnement, Additive sera toujours plus lumineux que les objets derrière lui, ce qui est adapté aux effets lumineux comme les rayons de lumière, le feu, les explosions.

Vous pouvez définir une valeur d’opacité supérieure à 1, ce qui signifie que l’objet sera plus lumineux.  
Cela peut être utile si vous voulez utiliser le [bloom](postprocess.md#bloom) et le `paramètre de seuil` pour ne faire briller que cet objet comme un objet émissif.

Ce mode a tendance à produire moins d’artefacts que le [Blending](#blending) (transparence indépendante de l’ordre).

### ![](/icons/material_refraction.webp) Réfraction {#refraction}
Ce mode peut être utilisé pour simuler un matériau de type verre. En raison des contraintes du temps réel, l’auto‑réfraction et la réfraction multi‑couches sont quelque peu limitées.

La rugosité peinte du modèle influe sur le flou de la réfraction.
Par défaut, chaque objet créé dans Nomad a une rugosité légèrement autour de 25 %, ainsi la réfraction ne sera pas parfaite mais un peu floue.
Vous pouvez utiliser le bouton `paint glossy` pour repeindre votre modèle avec une rugosité et une métallicité de 0 (les couleurs ne seront pas affectées).

Deux rugosités différentes entrent en jeu : celle qui contrôle le flou de la réflexion sur la surface, et celle qui contrôle l’intérieur (réfraction).  
Cependant, comme il n’y a qu’un seul canal de rugosité peinte dans Nomad, la rugosité intérieure et extérieure partageront la même valeur.  
Afin d’avoir des valeurs différentes (par exemple une sucette avec une surface nette mais un intérieur flou), utilisez les curseurs `Surface glossiness` et `Interior roughness` pour remplacer la rugosité peinte.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Tramage {#dithering}
Rend l’objet semi‑transparent en supprimant certains pixels de manière aléatoire.

### ![](/icons/material_shadow_catcher.webp) Capteur d’ombres {#shadow-catcher}

Rend l’objet invisible et ne reçoit que les ombres. Utile pour combiner des rendus Nomad avec d’autres images. 

::: tip

Vous trouverez plus d’informations sur la transparence et les modes de fusion sur https://support.fab.com/s/article/Transparency-Opacity

:::

## Contrôles {#controls}

![](/images/material_controls.webp)

### Toujours non éclairé {#always-unlit}
Si activé, l’objet ignorera PBR et Matcap et affichera simplement sa couleur peinte sans ombrage.
Notez que si vous utilisez [Additive](#additive), vous pouvez peindre la transparence directement en utilisant la couleur noire.

### Opacité {#opacity}
Détermine à quel point un objet apparaît solide ou opaque ; 100 % est solide, 0 % est transparent. Vous pouvez également peindre l’opacité pour un contrôle plus fin.

### Réflectance {#reflectance}
Contrôle la quantité de réflexion que recevra le matériau pour les matériaux non métalliques. La plupart du temps, la valeur par défaut doit être utilisée (qui correspond aux 4 % standard de lumière réfléchie à angle normal), mais elle peut être augmentée pour renforcer les reflets et les brillances dans les yeux d’un personnage, par exemple.

### Culling inversé {#inverse-culling}
Inverse les normales d’une surface. Généralement non nécessaire, mais peut être utilisé si un modèle apparaît à l’envers, ou en combinaison avec `Two sided` désactivé, pour créer des intérieurs où le mur le plus proche de la caméra est toujours masqué.

### Ombrage lisse {#smooth-shading}
Voir l’[option globale](settings.md#smooth-shading).  
La valeur `Auto` utilisera l’option globale.

### Double face {#two-sided}
Voir l’[option globale](settings.md#two-sided).  
La valeur `Auto` utilisera l’option globale.

### Arrière-plan coloré {#coloured-backface}
Voir l’[option globale](settings#two-sided).
La valeur `Auto` utilisera l’option globale.

### Projette des ombres {#casts-shadows}
Pour l’instant, `Auto` est identique à `On`.
Les objets transparents projettent également des ombres (avec un motif en tramage pour émuler des ombres fusionnées).  
Veillez à désactiver la projection d’ombres si vous avez un grand objet dans votre scène qui n’a pas besoin d’en projeter (par exemple un grand sol).

### Reçoit des ombres {#recieve-shadows}
Pour l’instant, `Auto` est identique à `On`.

### Fil de fer {#wireframe}
Voir l’[option globale](settings.md#wireframe).  
La valeur `Auto` utilisera l’option globale.


## Textures {#textures}

![](/images/material_textures.webp)

Si un objet possède des UV, des textures peuvent alors être appliquées au matériau en plus de la couleur/rugosité/métallicité/opacité de sommet. Il s’agit généralement du résultat d’un baking de textures, mais des images créées en dehors de Nomad peuvent également être utilisées.

Les textures peuvent être appliquées à

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Cliquer sur un emplacement de texture ouvrira un sélecteur. Une fois qu’une texture a été assignée à un emplacement de matériau, cliquer à nouveau ouvrira un panneau de texture :

### Options du panneau de textures {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Ouvrir {#open}
Sélectionner une autre texture

### Aucun {#none}
Supprimer la texture

### Opacité {#texture-opacity}

Si l’image possède un canal alpha, cela vous permettra de l’utiliser pour l’Opacité, ou de l’ignorer.

### ![](/icons/link.webp) Icône chaîne / lien {#chainlink-icon}

L’icône de lien dans les sections suivantes, lorsqu’elle est activée, signifie que les options utilisées seront partagées avec les autres textures (color, normal, roughness, metalness, opacity, emissive) qui ont également leur icône de lien activée. 

Cela vous permet de vous assurer que si vous avez des textures alignées, elles resteront alignées même si vous modifiez les paramètres ou les types de projection.


### Projection {#projection}
![](/images/material_projection.webp)

Définit comment la texture doit être appliquée à l’objet.

* `Auto` - Si l’objet possède des UV, UV, sinon Triplanar
* `UV` - Utilise les coordonnées UV du maillage pour appliquer la texture. Si le maillage et la texture proviennent de l’extérieur de Nomad, ou doivent être exportés depuis Nomad pour être utilisés ailleurs, UV est l’option correcte.
* `Triplanar` - Projette la texture le long des axes X, Y, Z et fusionne les coutures. 

### Triplanaire {#triplanar}
![](/images/material_triplanar.webp)

Les projections triplanaires sont un moyen puissant mais simple d’appliquer des textures aux objets.

Triplanar revient à disposer de 6 vidéoprojecteurs avec la même image, projetant sur l’avant, l’arrière, la gauche, la droite, le dessus et le dessous de votre objet.

Cela peut ensuite être baked en UV ou en couleurs de sommets si nécessaire.


![](/images/material_triplanar_example.webp)

#### Méthode {#method}

* `Local` - La projection se déplacera avec la transformation de l’objet
* `World` - La projection reste fixe, déplacer l’objet le fera glisser à travers la projection.

#### Dureté {#hardness}

Détermine comment les projections se mélangent. 100 % ne fera aucun mélange et les bords des projections seront nets. 0 % mélangera les bords sur un large angle. La valeur par défaut est 90 %, suffisamment de mélange pour masquer les bords tout en laissant le reste des projections net.

### Uniforme {#uniform}

Lorsqu’il est coché, la même dureté est utilisée pour toutes les projections. Lorsqu’il est décoché, des contrôles de dureté supplémentaires sont affichés pour les projections X, Y, Z.


### Paramètre {#parameter}
![](/images/material_parameter.webp)

#### Filtrage {#filtering}
La méthode de filtrage de texture à utiliser, `Auto` est la valeur par défaut, les méthodes sont `Nearest`, `Linear`, `Mipmap`. Nearest ne fait aucun filtrage, les textures peuvent donc présenter des artefacts crénelés lorsqu’elles sont vues de près. Linear et Mipmap effectuent un meilleur filtrage, de sorte que les textures apparaissent floues plutôt que crénelées de près.

#### Répétition-X {#tiling-x}
Si le paramètre Scale est supérieur à 1, rendant la texture plus petite que les UV de l’objet, définit comment la texture sera répétée le long de l’axe X. `None` signifie aucune répétition. `Repeat` fera des copies de la texture. `Mirror` fera des copies de la texture, avec chaque seconde copie inversée, ce qui peut aider à masquer les artefacts de répétition.

#### Répétition-Y {#tiling-y}
Identique à Tiling-X, mais pour l’axe Y.

### Transformation {#transform}
![](/images/material_transform.webp)

Transformations 2D supplémentaires appliquées à la texture dans l’espace UV. Le bouton de réinitialisation remet les valeurs par défaut, l’icône de chaîne (lorsque des textures autres que color sont sélectionnées) liera ou déliera la transformation pour qu’elle soit identique à celle de la texture color.

#### Translation {#translation}
Le décalage X et Y de la texture

#### Rotation {#rotation}
La rotation de la texture

#### Échelle {#scale}
L’échelle de la texture, des valeurs plus grandes rendront la texture plus petite sur l’objet, utilisez les curseurs Tiling-X et Tiling-Y pour contrôler ce qui se passe.

### Échelle uniforme {#uniform-scale}
Lorsqu’il est désactivé, Nomad affichera des contrôles séparés pour Scale-X et Scale-Y.