# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Plateforme {#platform}
### Où se trouvent mes projets sur mon appareil ? {#locate}
Les projets se trouvent dans le dossier `projects`, à l'intérieur du dossier principal de Nomad.

Sur iOS, vous pouvez accéder au dossier de Nomad avec l'application Fichiers.

Sur Android, le dossier de Nomad se trouve dans `Android/data/com.stephaneginier.nomad/files/`.  
Sur les versions récentes d'Android (10/11), vous n'avez plus accès au dossier `Android/data`.
Vous pouvez y accéder avec une application séparée, par exemple [celle-ci](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Est-il possible de tester les versions bêta ? {#beta}
Pour Windows et macOS, une bêta est parfois disponible sur la [page d'accueil](https://nomadsculpt.com).
<br>
Pour iOS, il existe un TestFlight privé : rendez-vous sur le [Discord](https://discord.com/invite/8h7BwpRz29), dans le canal #beta-ios.
<br>
La [démo web](https://nomadsculpt.com/demo) reçoit en général les dernières fonctionnalités.

### Pourquoi y a-t-il un essai gratuit sur Android, mais pas sur iOS ? {#android-trial}
Parce que les vieux appareils Android sont nuls (et certains récents aussi...), et je ne voulais pas que des gens achètent l'application pour tomber sur un écran noir.
Mais la raison principale, c'est que j'avais l'impression que les applications Android payantes ne sont pas vraiment la norme.

### Quelle est la meilleure tablette pour Nomad ? {#best-tablet}

En bref : un iPad.

La réponse un peu plus longue :

> « Le plus récent iPad _que vous pouvez vous offrir_, sauf si vous détestez vraiment Apple, auquel cas la plus récente tablette Samsung que vous pouvez vous offrir. Pour tout le reste, testez d'abord. » 

On veut toujours plus de détails, alors voici un résumé.

Nomad fonctionne le mieux sur les iPad récents :

* les iPad et iPhone ont accès au plugin [Quad Remesher](tools#quad-remesher) d'[Exoside](https://exoside.com/)
* les iPad récents avec le dernier Pencil gèrent le [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0) : vous pouvez faire tourner le Pencil sur lui-même avec certains outils de Nomad. 
* les dernières puces de la série M sont très rapides. 

Le plus récent et plus cher des iPad pourra rendre les images finales très vite, et vous laissera sculpter énormément de détails.

Cependant, la baisse de performances avec des iPad moins chers et plus anciens est moins forte qu'on ne le pense. Tout iPad compatible avec l'Apple Pencil fait plutôt bien tourner Nomad. Par exemple :

* Un iPad Pro de 2023 gère des sculptures de 5 millions de polygones en restant réactif, et rend une image de qualité finale en 5 secondes.
* Un iPad Pro de 2015 gère un objet de 1,2 million de polygones avec un peu de latence, et rend une image de qualité finale en 20 secondes.

C'est une grosse différence de performances, mais il faut aussi tenir compte du prix :

* L'iPad Pro 2025 coûte *2500 $ US* neuf, avec toutes les options. 
* L'iPad Pro 2023 coûte actuellement *400 $ US* sur eBay.
* L'iPad Pro 2015 coûte *250 $ US* sur eBay.

4 millions de polygones de plus et 15 secondes gagnées valent-ils 2100 $ ? À vous de voir.

Les modèles non Pro peuvent être encore moins chers, et offrent un large choix de tailles et de performances. L'iPad Air actuel gère le Pencil de 2e génération avec le barrel roll, et coûte nettement moins cher que le Pro. Le marché de l'occasion et du reconditionné offre encore plus de choix. 

Autrement dit, quel que soit votre budget, vous devriez trouver un iPad qui vous convient. Et rappelez-vous que la plupart des sculptures ne font pas des millions de polygones ! Si vous restez sous les 500 000 polygones, même un vieil iPad vous permettra de sculpter rapidement.

`Et Android ?`

Les performances graphiques d'Android sont inférieures à celles des iPad. Selon le développeur de Nomad, « une Samsung Galaxy Tab S9 fait tourner Nomad environ dix fois plus lentement qu'un iPad Air ». Cela dit, beaucoup d'utilisateurs sont très contents de leur tablette Samsung : Nomad y fonctionne bien pour la plupart des sculptures. 

Pour les autres tablettes Android, soyez prudent. Les performances du matériel Android varient énormément, et il n'est pas facile de prévoir comment Nomad tournera.

Testez d'abord avec la version gratuite de Nomad, où l'enregistrement est désactivé. 

`Et la mémoire et le stockage ?`

La plupart des fichiers Nomad font 100 Mo ou moins. Presque n'importe quelle tablette achetée aujourd'hui, iPad ou Android, aura donc largement la place pour vos projets Nomad.


### J'ai acheté Nomad sur un appareil, puis-je l'utiliser sur un autre ? {#multi-devices}
Oui, tant qu'il utilise le même magasin d'applications et le même compte.

Par exemple, si vous l'avez acheté sur l'App Store d'iOS, vous pouvez l'utiliser sur vos autres appareils iOS.

Si vous l'avez acheté pour votre tablette Android sur Google Play, vous pouvez l'utiliser sur vos autres appareils Android.

En revanche, si vous avez acheté Nomad sur Android et que vous prenez ensuite un iPad, vous devrez l'acheter à nouveau.

C'est parce que Nomad n'a pas son propre serveur de licences ni de modèle d'abonnement. Il n'existe aucun accord entre Apple, Google et AppGallery pour partager les licences. 


### Comment restaurer mon achat ? {#restore}
Google Play et AppGallery gèrent tous les deux la synchronisation automatiquement.

- Allez dans le menu À propos (l'icône Nomad en haut à gauche), et touchez `Restaurer l'achat`
- Vérifiez que vous êtes connecté au même compte que celui utilisé pour acheter Nomad (sur Google Play).
- Redémarrez l'appareil
- Il faut parfois attendre quelques heures
- Vérifiez que l'application Google Play est à jour
- Réinstallez Nomad (pensez à [sauvegarder vos fichiers](#locate) si vous ne voulez rien perdre)
- Vous pouvez essayer d'acheter à nouveau pour voir ce qui se passe (remarque : vous ne pouvez pas acheter deux fois le même article avec le même compte)

:::tip
Vous pouvez me contacter à <support@nomadsculpt.com>, mais la *seule* chose que je pourrai faire est de confirmer si un achat est associé à une adresse e-mail.

Je reçois régulièrement des signalements de licences qui ne se mettent pas à jour correctement après l'achat d'un nouvel appareil.
Je n'ai aucun contrôle sur le paiement et la synchronisation des comptes : tout est géré par Google/AppGallery !

L'achat finit toujours par être restauré, mais on ne sait pas vraiment quelles étapes permettent d'accélérer le processus.
:::

::: warning
Les appareils Huawei récents n'ont pas accès aux services Google.
Dans ce cas, vous devrez acheter à nouveau l'application sur AppGallery (le magasin d'applications de Huawei).
:::

### Pouvez-vous traduire ou corriger [ma-langue] ? {#locale}
Je peux assez facilement ajouter une langue, mais je m'appuie sur la traduction par IA, bien plus pratique pour les mises à jour régulières.
Les fichiers de traduction se trouvent [ici](https://github.com/stephomi/nomad-translation).

## Fonctionnalités {#features}

### Pourquoi le gizmo ne bouge-t-il pas ? {#gizmo-not-moving}
Vous avez peut-être activé l'[épinglage dans la barre d'outils du menu de gauche](tools#left-menu-toolbar). 

### Peut-on animer dans Nomad ? {#animate}
Pas pour l'instant. Une timeline permettant d'animer les calques pourrait être intéressante, mais ce n'est pas vraiment prévu pour le moment.  

J'aimerais gérer le rigging/skinning à l'avenir, mais cela pose quelques difficultés (notamment l'interaction avec les outils de sculpture...), donc rien de sûr pour l'instant.


### Peut-on faire du vrai modelage low poly ? {#lowpoly}
Pas pour l'instant.
Ce n'est pas vraiment le domaine de Nomad *Sculpt*, mais j'ajouterai peut-être quelques outils à l'avenir.


### Peut-on faire des UV et du texturage ? {#texturing}
Réponse courte : oui. Réponse longue : pas directement, mais il existe plusieurs façons de combiner les excellents outils de peinture aux sommets de Nomad avec des UV et des textures.

* Nomad vous permet de peindre la couleur, la rugosité et les propriétés du matériau directement dans les sommets de votre sculpture.
* Nomad accepte un très grand nombre de sommets, pour que vous puissiez peindre sans vous soucier des UV.
* Nomad peut charger des textures à utiliser dans les pinceaux, pour tamponner et peindre avec des textures.
* Nomad peut charger des objets auxquels des textures sont déjà attribuées, pour le rendu.
* Nomad peut faire le [dépliage UV](topology.md#uv-unwrap-uvatlas) d'objets moins denses.
* La couleur, la rugosité et la métallité peuvent être transférées des textures vers les sommets avec [les options de projection](topology.md#reproject-to-vertex).
* La couleur, la rugosité, la métallité et les normales peuvent être transférées des sommets vers des textures avec [les options de baking](topology.md#bake-texture)
* Le baking et la projection peuvent se faire entre un objet et un autre, entre plusieurs objets, ou entre le niveau de subdivision le plus élevé et le plus bas d'un même objet, ce qui permet de nombreuses méthodes de travail.
* Après le baking, exporter un OBJ exporte aussi les textures, que vous pouvez ensuite ouvrir dans une application comme Procreate pour peindre directement dessus.

### Puis-je enregistrer une vidéo en plateau tournant ? {#video}
Ce n'est pas prévu pour l'instant, mais iOS dispose d'une [fonction d'enregistrement vidéo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) très simple à utiliser.

Sous iOS, balayez vers le bas depuis le coin supérieur gauche, puis touchez le bouton d'enregistrement. Un compte à rebours de 3 secondes démarre : balayez le menu pour faire réapparaître Nomad, et utilisez la fonction plateau tournant. Une fois terminé, balayez à nouveau vers le bas depuis le coin supérieur droit, et touchez de nouveau le bouton d'enregistrement. Modifiez ensuite la vidéo depuis la photothèque pour couper le surplus au début et à la fin.

### Pouvez-vous ajouter [ma-fonction-préférée] sous forme de bouton principal ? {#interface}
Oui : la barre d'outils du bas peut maintenant être personnalisée depuis le menu [Interface](interface.md#shortcuts), et vous pouvez aussi créer des barres d'outils flottantes.

### Quelles sont les prochaines fonctionnalités ? {#next-features}
Pour la feuille de route à moyen et long terme, j'ai beaucoup d'idées, mais rien n'est encore décidé.  

Corriger les bugs et améliorer les fonctionnalités existantes passera toujours avant l'ajout de nouvelles fonctionnalités.


### Peut-on faire du rigging dans Nomad ? {#rigging}
Non, mais c'est prévu. Pour l'instant, vous pouvez hiérarchiser des formes et modifier leurs points de pivot, ce qui permet de créer des sculptures simples à poser.

### Peut-on utiliser plus de 4 lumières ? {#lights}
Vous pouvez utiliser jusqu'à 4 lumières sur mobile, et jusqu'à 6 sur ordinateur. C'est une limite du moteur de rendu en temps réel de Nomad. Vous pouvez la contourner avec des objets émissifs et l'illumination globale du post-traitement, comme le montre [ce tutoriel](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Peut-on importer des outils ZBrush ? {#zbrush-import}
Non, ZBrush utilise un format propriétaire. Vous devriez cependant pouvoir extraire les alphas et les utiliser dans Nomad. 

### Pourquoi les couleurs ne correspondent-elles pas à ce que j'ai peint ? Pourquoi est-ce que je n'obtiens pas de blanc au rendu ? {#paint-pbr}
Imaginez une photo d'une feuille de papier, une photo d'une lampe de bureau et une photo du soleil. Les appareils photo et écrans anciens rendront tout cela simplement « blanc ». Les systèmes plus modernes savent montrer la différence entre le blanc réfléchi par le papier, la lumière émise par une lampe et l'éclat intense du soleil.

L'image de synthèse moderne essaie de fonctionner de la même façon, en imitant la physique de la lumière et des surfaces. C'est ce qu'on appelle le `Physically Based Rendering` (rendu basé sur la physique), ou PBR, et le moteur PBR de Nomad repose sur ce principe. Le résultat est réaliste et équilibré, mais les couleurs peintes très claires paraissent souvent plus sombres.

Si vous avez besoin d'un rendu plus proche des couleurs peintes, vous pouvez y remédier de façon non physique ou physique :

Sans PBR :
* `Utilisez le mode 'Sans éclairage' du menu Ombrage`. Les couleurs s'affichent exactement comme peintes, mais vous perdez aussi tout l'ombrage. Pratique pour des vérifications rapides, et pour un rendu plus graphique.
* `Utilisez le mode 'MatCap' du menu Ombrage`. Choisissez un matcap plus clair, presque blanc, sans teinte de couleur.

Avec PBR :
* `Utilisez un environnement neutre`. Vous pouvez [changer l'environnement](shading.md#environment) pour un plus neutre. Évitez les environnements d'intérieur, souvent plus colorés. Préférez un environnement extérieur en plein jour ou un studio.
* `Renforcez l'éclairage`. Si vous preniez en photo une feuille blanche dans une pièce sombre, vous ajouteriez simplement de la lumière. Sur la lumière d'environnement, montez le curseur d'exposition jusqu'à ce que les couleurs vous semblent justes, ou ajoutez d'autres lumières plus intenses.
* `Augmentez l'exposition de la caméra`. Si la pièce sombre n'avait pas d'autre lumière, vous pourriez laisser l'obturateur ouvert plus longtemps, ou utiliser un ISO plus sensible. Dans Nomad, vous obtenez un résultat semblable avec le post-traitement. Allez dans Post-traitement, activez-le, descendez jusqu'au mappage tonal, activez-le, et montez le curseur d'exposition jusqu'à ce que les couleurs vous semblent justes.
* `Utilisez une couleur émissive`. Dans le menu Matériau, vous pouvez activer 'Émissif' dans les textures, ce qui fait apparaître l'objet comme une source de lumière. Si vous activez l'illumination globale dans les réglages de post-traitement, il éclairera les autres objets de la scène. Vous pouvez aussi activer 'Toujours sans éclairage' pour ce matériau, ce qui donne un aspect semblable sans texture.

## Plantages {#crashes}

### L'application plante quand j'enregistre ou remaille mon modèle ! {#crash-remesh}
Votre appareil manque de mémoire (RAM).  
Pour réduire la mémoire utilisée par votre scène, vous pouvez réduire le nombre de polygones avec certaines options du menu [Topologie](topology.md).

::: tip RAM/stockage
Ce qui compte, c'est la quantité de RAM, pas le stockage (qui est en général bien plus grand).
:::


### L'application plante quand je charge mon projet ! {#crash-load}
Si le fichier est petit, vous pouvez me l'envoyer pour que j'y jette un œil (par e-mail à <support@nomadsculpt.com>).

Sinon, l'appareil manque probablement de mémoire RAM.

- Fermez toutes les autres applications ouvertes sur votre appareil.
- Démarrez un nouveau projet dans Nomad plutôt que de garder un projet ouvert.
- Si cela plante encore, la seule solution est de charger [votre fichier projet](#locate) sur un appareil avec plus de mémoire.

::: tip
Si votre appareil mobile ne parvient pas à charger le projet, essayez la [version ordinateur](https://nomadsculpt.com). Vous pouvez l'utiliser gratuitement en mode démo pour importer et exporter des projets, même si seuls quelques outils d'édition sont disponibles.

Si votre projet utilise des [Calques](layers.md), vous pouvez les fusionner pour réduire la mémoire utilisée.
:::

### L'application plante au démarrage de Nomad ! {#crash-start}
Si elle plante au chargement, c'est que Nomad bute sur un fichier présent dans le dossier de Nomad.

La plupart du temps, c'est parce que le projet est lourd et dépasse malheureusement la limite de RAM.

Trouvez le [dossier de Nomad](#locate), puis renommez ou déplacez certains fichiers pour trouver le coupable.

Commencez par renommer `settings.json`. Ainsi, le dernier projet ne sera plus chargé.

Si cela ne suffit pas, essayez de déplacer quelques fichiers récents hors de leurs dossiers de ressources respectifs (`projects`, `matcaps`, `environments`, etc.).

Vous pouvez aussi renommer les dossiers eux-mêmes pour que Nomad les ignore complètement.
Si vous renommez ou déplacez tous les fichiers du dossier de Nomad, vous obtiendrez le même résultat qu'une installation propre.

::: tip
Quand Nomad charge un fichier au démarrage, il déplace toujours ce fichier dans le dossier `can_be_deleted/`.
Si l'opération réussit, le fichier est remis dans son dossier d'origine.

Si l'application plante avant la fin du chargement, Nomad démarrera normalement la fois suivante, car il ignore le dossier `can_be_deleted/`.

Vous pouvez simplement réessayer de charger ce fichier si vous pensez que cela peut fonctionner.
:::
