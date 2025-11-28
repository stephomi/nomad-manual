# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Plateforme {#platform}
### Où se trouvent mes projets sur mon appareil ? {#locate}
Les projets se trouvent dans le dossier `projects` à l’intérieur du dossier principal de Nomad.

Sur iOS, vous pouvez accéder au dossier Nomad avec l’application Fichiers d’iOS.

Sur Android, le dossier Nomad se trouve dans `Android/data/com.stephaneginier.nomad/files/`.  
Sur les versions récentes d’Android (10/11), vous n’avez plus accès au dossier `Android/data`.
Vous pouvez y accéder via une application séparée, par exemple [celle-ci](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Y a-t-il un moyen de faire du bêta-test ? {#beta}
Pour Windows et MacOS, une bêta peut être disponible sur la [page d’accueil](https://nomadsculpt.com).
<br>
Pour iOS il existe un TestFlight privé, rendez-vous sur le [Discord](https://discord.com/invite/8h7BwpRz29) dans le canal #beta-ios.
<br>
La [démo Web](https://nomadsculpt.com/demo) est généralement mise à jour avec les dernières fonctionnalités.

### Pourquoi y a-t-il un essai gratuit sur Android mais pas sur iOS ? {#android-trial}
Parce que les vieux appareils Android sont mauvais (et certains récents aussi...), et je ne voulais pas que les gens achètent l’app pour être accueillis par un écran noir.
Mais la principale raison est que j’ai le sentiment que les applications payantes ne sont pas vraiment la norme sur Android.

### Quelle est la meilleure tablette pour faire tourner Nomad ? {#best-tablet}

TLDR : Un iPad.

La réponse un peu plus longue est :

> « Le dernier iPad _que vous pouvez vous permettre_, à moins que vous ne détestiez vraiment Apple, auquel cas la dernière tablette Samsung que vous pouvez vous permettre. Pour tout le reste, testez d’abord. » 

Les gens veulent toujours plus d’informations, voici donc un résumé.

Nomad fonctionne mieux sur les iPad récents :

* Les iPad et iPhone peuvent accéder au plugin [Quad Remesher](tools#quad-remesher) de [Exoside](https://exoside.com/)
* Les iPad récents avec le dernier Pencil gèrent le [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), vous pouvez faire pivoter le stylet dans certains outils de Nomad. 
* Les performances des derniers processeurs de la série M sont très rapides. 

Le tout dernier iPad le plus cher disponible pourra rendre des images finales très rapidement et vous permettra de sculpter avec beaucoup de détails.

Cependant, la baisse de performances avec des iPad plus anciens et moins chers n’est pas aussi importante que ce que l’on imagine. Tout iPad compatible avec l’Apple Pencil fait tourner Nomad correctement. Par exemple :

* Un iPad Pro de 2023 peut gérer des sculptures de 5 millions de polygones tout en restant réactif, une image finale de qualité peut être rendue en 5 secondes.
* Un iPad Pro de 2015 peut gérer un objet de 1,2 million de polygones avec un peu de latence, une image finale de qualité peut être rendue en 20 secondes.

C’est une grosse différence de performances, mais il faut aussi prendre en compte le prix :

* L’iPad Pro 2025 coûte *2500 $ US* neuf avec toutes les options. 
* L’iPad Pro 2023 coûte actuellement *400 $ US* sur eBay.
* L’iPad Pro 2015 coûte *250 $ US* sur eBay.

Est-ce que gagner 4 millions de polygones supplémentaires et 15 secondes vaut 2100 $ ? C’est à vous de voir.

Les modèles non Pro peuvent être encore moins chers et offrent une grande variété de tailles et de performances. L’iPad Air actuel prend en charge le Pencil de 2e génération avec barrel roll, et est nettement moins cher que le Pro. Le marché de l’occasion et du reconditionné offre encore plus d’options. 

Cela signifie que, quel que soit votre budget, vous devriez pouvoir trouver un iPad adapté. Et rappelez-vous que la plupart des sculptures ne font pas des millions de polygones ! Si vous pouvez rester sous les 500 000 polygones, même les vieux iPad vous permettront de sculpter rapidement.

`Et Android ?`

Les performances graphiques d’Android sont inférieures à celles des iPad. D’après le développeur de Nomad, « Une Samsung Galaxy Tab S9 fera tourner Nomad un ordre de grandeur plus lentement qu’un iPad Air ». Cela dit, beaucoup d’utilisateurs sont très satisfaits de leurs tablettes Samsung, Nomad fonctionne correctement pour la plupart des travaux de sculpture. 

Pour les autres tablettes Android, soyez prudent. Les performances matérielles peuvent énormément varier, il n’est pas facile de prédire comment Nomad va tourner.

Veuillez d’abord utiliser la version gratuite sans sauvegarde de Nomad pour tester. 

`Et la mémoire et le stockage ?`

La plupart des fichiers Nomad font 100 Mo ou moins. Cela signifie que presque toutes les tablettes que vous achetez aujourd’hui, iPad ou Android, auront largement assez de place pour vos projets Nomad.


### J’ai acheté Nomad pour un appareil, puis-je l’utiliser sur un autre appareil ? {#multi-devices}
Tant que c’est le même store et le même compte, oui.

Par exemple, si vous l’avez acheté sur l’App Store iOS, vous pouvez l’utiliser sur vos autres appareils iOS.

Si vous l’avez acheté pour votre tablette Android sur Google Play, vous pouvez l’utiliser sur vos autres appareils Android.

En revanche, si vous avez acheté Nomad sur Android puis que vous achetez un iPad, vous devrez l’acheter à nouveau.

C’est parce que Nomad n’a pas son propre serveur de licence ni de modèle d’abonnement. Il n’existe aucun accord entre Apple/Google/AppGallery pour gérer le partage de licence. 


### Comment restaurer mon achat ? {#restore}
Google Play et AppGallery gèrent tous deux la synchronisation automatiquement.

- Allez dans le menu À propos (icône Nomad en haut à gauche), et appuyez sur `restore purchase`
- Vérifiez bien que vous êtes connecté au même compte que celui utilisé pour acheter Nomad (sur Google Play).
- Redémarrez l’appareil
- Parfois il faut attendre quelques heures
- Assurez-vous que l’application Google Play est à jour
- Réinstallez Nomad (pensez à [sauvegarder vos fichiers](#where-are-my-projects-located-on-my-device) si vous ne voulez rien perdre)
- Vous pouvez essayer d’acheter à nouveau pour voir ce qu’il se passe (note : vous ne pouvez pas acheter deux fois le même article sur le même compte)

:::tip
Vous pouvez me contacter à <support@nomadsculpt.com> mais la *seule* chose que je pourrai faire est de confirmer si un email a un achat associé.

Notez que je reçois régulièrement des rapports concernant des licences qui ne se mettent pas correctement à jour après l’acquisition d’un nouvel appareil.
Je n’ai aucun contrôle sur le paiement ni sur la synchronisation des comptes, tout est géré par Google/AppGallery !

Au final, l’achat est toujours restauré, mais les étapes nécessaires pour accélérer le processus ne sont pas claires.
:::

::: warning
Les appareils Huawei récents n’ont pas accès aux services Google.
Dans ce cas, vous devrez acheter l’application à nouveau sur AppGallery (store Huawei).
:::

### Pouvez-vous traduire ou corriger [ma-langue] ? {#locale}
Je peux relativement facilement ajouter une autre langue, mais je m’appuie sur la traduction par IA car c’est beaucoup plus simple à gérer pour les mises à jour régulières.
Les fichiers de traduction se trouvent [ici](https://github.com/stephomi/nomad-translation).

## Fonctionnalités {#features}

### Pourquoi le gizmo ne bouge-t-il pas ? {#gizmo-not-moving}
Vous avez peut-être [activé l’épinglage dans la barre d’outils du menu de gauche](tools#left-menu-toolbar). 

### Peut-on animer dans Nomad ? {#animate}
Pas pour l’instant. Une timeline qui permettrait d’animer les calques pourrait être intéressante, mais ce n’est pas vraiment prévu pour le moment.  

J’aimerais prendre en charge le rigging/skinning à l’avenir, mais cela pose quelques défis (notamment l’interaction avec les outils de sculpture...) donc rien de sûr pour l’instant.


### Peut-on faire du vrai modélisme low-poly ? {#lowpoly}
Pas pour l’instant.
Ce n’est pas vraiment dans le champ d’action de Nomad *Sculpt*, mais je proposerai peut-être quelques outils à l’avenir.


### Peut-on faire des UV et du texturing ? {#texturing}
Réponse courte : Oui. Réponse longue : Pas directement, mais il existe plusieurs façons de combiner les excellents outils de peinture par sommets de Nomad avec des UV et des textures.

* Nomad vous permet de peindre la couleur, la rugosité et les propriétés de matériau directement dans les sommets de votre sculpture.
* Nomad permet des nombres de sommets très élevés afin que vous puissiez peindre sans vous soucier des UV.
* Nomad peut charger des textures à utiliser dans les brosses, ce qui permet de tamponner et peindre avec des textures.
* Nomad peut charger des objets ayant déjà des textures assignées, à des fins de rendu.
* Nomad peut faire un [dépliage UV](topology.md#uv-unwrap) sur des objets low poly.
* La couleur/la rugosité/la métallicité peuvent être transférées des textures vers les sommets via [les options de projection](topology.md#reproject-to-vertex).
* La couleur/la rugosité/la métallicité/les normales peuvent être bakées des sommets vers les textures via [les options de baking](topology.md#bake-to-texture)
* Le baking et la projection peuvent être gérés entre des objets uniques ou multiples, ou entre les niveaux de subdivision les plus haut et le plus bas d’un même objet, ce qui permet une grande variété de workflows de bake et de projection.
* Après le baking, l’export d’un obj exportera également les textures, qui pourront être utilisées dans une application comme Procreate pour peindre directement sur les textures.

### Puis-je enregistrer une vidéo de tournette ? {#video}
Ce n’est pas prévu pour l’instant, iOS dispose d’une [fonction d’enregistrement vidéo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) très simple à utiliser.

Sous iOS, faites glisser depuis le coin supérieur gauche, puis touchez le bouton d’enregistrement. Un compte à rebours de 3 secondes s’affiche, faites disparaître le menu pour révéler Nomad, et utilisez la fonction de turntable. Une fois terminé, faites à nouveau glisser depuis le coin supérieur droit, et touchez le bouton d’enregistrement. Éditez la vidéo depuis la photothèque pour supprimer les parties inutiles au début et à la fin.

### Pouvez-vous ajouter [insérer-fonctionnalité-préférée] en tant que bouton de niveau supérieur ? {#interface}
Oui, la barre d’outils inférieure peut maintenant être personnalisée depuis le menu [interface](interface.md), et des barres d’outils flottantes peuvent désormais être créées.

### Quelles sont les prochaines fonctionnalités ? {#next-features}
Pour la feuille de route à moyen/long terme, j’ai beaucoup d’idées mais je ne sais pas encore.  

Les corrections de bugs et l’amélioration des fonctionnalités existantes auront toujours une priorité plus élevée que l’ajout de nouvelles fonctionnalités.


### Peut-on faire du rig dans Nomad ? {#rigging}
Non, mais c’est prévu. Pour l’instant, vous pouvez faire de la hiérarchie entre les formes et modifier les pivots, ce qui permet de créer des sculptures simplement posables.

### Peut-on utiliser plus de 4 lumières ? {#lights}
Non, c’est une limitation du moteur de rendu temps réel de Nomad. Il est possible de contourner cela en utilisant des objets émissifs et l’illumination globale dans le post-process, comme montré dans [ce tutoriel](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Peut-on importer des tools ZBrush ? {#zbrush-import}
Non, Zbrush utilise un format propriétaire. Vous devriez pouvoir extraire les alpha maps et les utiliser dans Nomad. 

### Pourquoi les couleurs ne correspondent-elles pas à ce que j’ai peint ? Pourquoi ne puis-je pas obtenir de blanc dans le rendu ? {#paint-pbr}
Imaginez prendre une photo d’une feuille de papier, puis une photo d’une lampe de bureau, puis une photo du soleil. Les anciens appareils photo et écrans vont simplement tout afficher comme « blanc ». Les systèmes plus modernes peuvent montrer une différence entre le blanc réfléchi du papier, la lumière émise par la lampe, et le blanc super lumineux du soleil.

Les graphismes modernes sur ordinateur essaient de fonctionner de manière similaire, en imitant la physique de la lumière et des surfaces. C’est ce qu’on appelle le `Physically Based Rendering`, ou PBR, et le moteur PBR de Nomad est basé sur ce principe. Le rendu est réaliste et équilibré, mais souvent les couleurs très vives peintes apparaîtront plus sombres.

Si vous avez besoin que le rendu corresponde davantage aux couleurs peintes, vous pouvez corriger cela de manière non physiquement basée ou physiquement basée :

Non PBR :
* `Utilisez le mode “Unlit” dans le menu d’éclairage`. Les couleurs seront affichées exactement comme peintes, mais vous perdez aussi tout ombrage. Pratique pour des vérifications rapides et un rendu plus graphique.
* `Utilisez le mode “Matcap” dans le menu d’éclairage`. Choisissez un matcap plus clair, principalement blanc, sans teinte colorée.

PBR :
* `Utilisez un environnement neutre`. Vous pouvez [changer l’environnement](shading.md#environment) pour un environnement plus neutre. Évitez les environnements intérieurs car ils ont tendance à être plus colorés. Préférez un environnement extérieur de jour ou un studio.
* `Augmentez l’éclairage`. Si vous preniez une photo d’une feuille blanche dans une pièce sombre, vous ajouteriez simplement plus de lumière. Sur la lumière d’environnement, augmentez le curseur d’exposition jusqu’à ce que les couleurs vous semblent correctes, ou ajoutez plus de lumières individuelles avec plus d’intensité.
* `Augmentez l’exposition de la caméra`. Si la pièce sombre n’avait pas de lumière supplémentaire, vous pourriez laisser l’obturateur de l’appareil photo ouvert plus longtemps, ou utiliser une sensibilité ISO plus élevée. Dans Nomad, vous pouvez obtenir un résultat similaire avec le post-process. Allez dans post-process, activez-le, descendez jusqu’au tone mapping, activez-le, et augmentez le curseur d’exposition jusqu’à ce que les couleurs vous semblent correctes.
* `Utilisez la couleur émissive`. Dans le menu matériau, vous pouvez activer « emissive » sous textures, ce qui fera apparaître un objet comme une source de lumière. Si vous activez l’illumination globale dans les paramètres de post-process, il projettera de la lumière sur les autres objets de la scène. Vous pouvez aussi activer « unlit » pour ce matériau, ce qui donnera un résultat similaire sans texture.

## Crashes {#crashes}

### Ça plante quand j’enregistre ou remesh mon modèle ! {#crash-remesh}
Votre appareil manque de mémoire (RAM).  
Pour réduire l’utilisation de la mémoire dans votre scène, vous pouvez utiliser certaines options de [Topologie](topology.md) pour réduire le nombre de polygones.

::: tip RAM/Stockage
Ce qui compte, c’est la quantité de RAM, pas le stockage (qui est généralement beaucoup plus grand).
:::


### Ça plante quand je charge mon projet ! {#crash-load}
Si le fichier est petit, vous pouvez me l’envoyer et j’y jetterai un œil (par email <support@nomadsculpt.com>).

Sinon, l’appareil manque probablement de mémoire RAM.

- Assurez-vous de fermer toutes les autres applications ouvertes sur votre appareil.
- Démarrez un nouveau projet dans Nomad au lieu d’avoir un projet déjà ouvert.
- Si ça plante toujours, la seule solution est de charger [votre fichier projet](#where-are-my-projects-located-on-my-device) sur un appareil avec plus de mémoire.

::: tip
Sur un navigateur de bureau, vous pouvez essayer de charger votre fichier [à cette adresse](https://nomadsculpt.com/demo_save/) puis de l’exporter à nouveau après avoir simplifié votre scène.

Certains navigateurs limitent la quantité de RAM qu’un seul onglet peut utiliser, il est donc possible que cette technique ne fonctionne pas.

Si votre projet utilise des [Calques](layers.md), vous pouvez les aplatir pour réduire l’utilisation de la mémoire.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Ça plante quand je démarre Nomad ! {#crash-start}
Si ça plante au chargement, cela signifie que Nomad a un problème avec un certain fichier présent dans le dossier Nomad.

La plupart du temps, cela arrive parce que le projet est lourd et dépasse malheureusement la limite de RAM.

Repérez le [dossier Nomad](#where-are-my-projects-located-on-my-device), puis renommez ou déplacez certains fichiers pour trouver le coupable.

Commencez par renommer `settings.json`. De cette façon, il arrêtera de charger le dernier projet.

Si cela ne fonctionne pas, essayez de déplacer certains fichiers récents en dehors de leurs dossiers de ressources respectifs (`projects`, `matcaps`, `environments`, etc).

Vous pouvez aussi renommer les dossiers eux-mêmes pour que Nomad les ignore complètement.
Si vous renommez ou déplacez tous les fichiers du dossier Nomad, cela aura le même effet qu’une installation propre.

::: tip
Quand Nomad charge un fichier au démarrage, il déplace toujours le fichier dans le dossier `can_be_deleted/`.
Si l’opération réussit, il est ensuite déplacé vers son dossier d’origine.

Si l’application plante avant la fin du chargement, alors Nomad se lancera correctement au démarrage suivant, car il ignore le dossier `can_be_deleted/`.

Vous pouvez simplement essayer de charger à nouveau ce fichier si vous pensez que cela peut réussir.
:::