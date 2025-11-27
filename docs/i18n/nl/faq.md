# ![](/icons/faq.webp) FAQ

[[toc]]

## Platform 
### Waar staan mijn projecten op mijn apparaat?
De projecten staan in de map `projects` binnen de hoofdmap van Nomad.

Op iOS kun je de Nomad-map openen met de iOS Bestanden-app.

Op Android staat de Nomad-map in `Android/data/com.stephaneginier.nomad/files/`.  
Op recente Android-versies (10/11) heb je geen toegang meer tot de map `Android/data`.
Je kunt er toegang toe krijgen via een aparte app, bijvoorbeeld [deze](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Is er een manier om de bèta te testen?
Voor Windows & MacOS is er mogelijk een bèta beschikbaar op de [Homepage](https://nomadsculpt.com).
<br>
Voor iOS is er een privé-TestFlight, bezoek de [Discord](https://discord.com/invite/8h7BwpRz29) in het #beta-ios-kanaal.
<br>
De [Web Demo](https://nomadsculpt.com/demo) wordt meestal bijgewerkt met de nieuwste functies.

### Waarom is er een gratis proefversie op Android, maar niet op iOS?
Omdat oude Android-apparaten slecht zijn (en sommige recente ook...), en ik niet wilde dat mensen de app kopen en dan worden begroet met een zwart scherm.
Maar de belangrijkste reden is dat ik het gevoel heb dat betaalde Android-apps niet echt de norm zijn.

### Wat is de beste tablet om Nomad op te draaien?

TLDR: Een iPad.

Het iets langere antwoord is 

> "De nieuwste iPad _die je je kunt veroorloven_, tenzij je echt een hekel hebt aan Apple, in dat geval de nieuwste Samsung-tablet die je je kunt veroorloven. Alles daarbuiten: eerst testen." 

Mensen willen altijd meer informatie, dus hier is een samenvatting.

Nomad draait het best op nieuwere iPads:

* iPads en iPhones hebben toegang tot de [Quad Remesher](tools#quad-remesher)-plugin van [Exoside](https://exoside.com/)
* recente iPads met de nieuwste pencil-ondersteuning ondersteunen [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0); je kunt de pencil draaien in bepaalde tools in Nomad. 
* de prestaties van de nieuwste M-serie chips zijn erg snel. 

De nieuwste, duurste iPad die beschikbaar is, kan eindbeelden zeer snel renderen en laat je met veel detail sculpteren.

De prestatie-afname bij goedkopere en oudere iPads is echter niet zo erg als mensen verwachten. Elke iPad die een Apple Pencil ondersteunt, draait Nomad behoorlijk goed. Bijvoorbeeld:

* Een iPad Pro uit 2023 kan 5 miljoen poly-sculpts aan en blijft responsief; een eindbeeld kan in 5 seconden renderen.
* Een iPad Pro uit 2015 kan een object van 1,2 miljoen poly aan met wat vertraging; een eindbeeld kan in 20 seconden renderen.

Dat is een groot prestatieverschil, maar je moet ook rekening houden met de prijs:

* De iPad Pro van 2025 kost *$2500 USD* nieuw met alle opties. 
* De iPad Pro van 2023 kost momenteel *$400 USD* op eBay.
* De iPad Pro van 2015 kost *$250 USD* op eBay.

Is 4 miljoen extra polys en 15 seconden tijdwinst $2100 waard? Dat is aan jou.

Niet-Pro-modellen kunnen nog goedkoper zijn en bieden een grote variatie aan formaten en prestaties om uit te kiezen. De huidige iPad Air ondersteunt de gen 2 pencil met barrel roll en is aanzienlijk goedkoper dan de Pro. De tweedehands- en refurbished-markt biedt nog meer opties. 

Dit betekent dat je, wat je budget ook is, een iPad zou moeten kunnen vinden die bij je past. En onthoud dat de meeste sculpts geen miljoenen polys zijn! Als je onder de 500.000 polys kunt blijven, laten zelfs oude iPads je snel sculpteren.

`Hoe zit het met Android?`

De grafische prestaties van Android liggen onder die van iPads. Volgens de ontwikkelaar van Nomad "draait een Samsung Galaxy Tab S9 Nomad een orde van grootte langzamer dan een iPad Air". Dat gezegd hebbende, veel gebruikers zijn erg tevreden met hun Samsung-tablets; Nomad draait prima voor de meeste sculpttaken. 

Wees voorzichtig met andere Android-tablets. Android-hardware kan enorm variëren in prestaties; het is niet eenvoudig te voorspellen hoe Nomad zal draaien.

Gebruik eerst de gratis versie van Nomad zonder opslaan om te testen. 

`Hoe zit het met geheugen en opslag?`

De meeste Nomad-bestanden zijn 100 MB of kleiner. Dit betekent dat vrijwel elke tablet die je tegenwoordig koopt, iPad of Android, ruim voldoende opslag heeft voor je Nomad-projecten.


### Ik heb Nomad voor één apparaat gekocht, kan ik het op een ander apparaat gebruiken?
Zolang het dezelfde appstore en hetzelfde account gebruikt, ja.

Als je het bijvoorbeeld in de iOS App Store hebt gekocht, kun je het op je andere iOS-apparaten gebruiken.

Als je het voor je Android-tablet in Google Play hebt gekocht, kun je het op je andere Android-apparaten gebruiken.

Als je Nomad echter op Android hebt gekocht en daarna een iPad aanschaft, moet je het opnieuw kopen.

Dit komt omdat Nomad geen eigen licentieserver of abonnementsmodel heeft. Er is geen overeenkomst tussen Apple/Google/AppGallery om licenties te delen. 


### Hoe herstel ik mijn aankoop?
Google Play en AppGallery regelen de synchronisatie automatisch.

- Ga naar het About-menu (linksboven op het Nomad-icoon) en tik op `restore purchase`
- Controleer dubbel of je bent ingelogd met hetzelfde account dat je hebt gebruikt om Nomad te kopen (op Google Play).
- Herstart het apparaat
- Soms moet je een paar uur wachten
- Zorg dat de Google Play-app up-to-date is
- Installeer Nomad opnieuw (zorg dat je [een back-up van je bestanden maakt](#where-are-my-projects-located-on-my-device) als je niets wilt verliezen)
- Je kunt proberen opnieuw te kopen om te zien wat er gebeurt (opmerking: je kunt hetzelfde item niet twee keer kopen op hetzelfde account)

:::tip
Je kunt contact met me opnemen via <support@nomadsculpt.com>, maar het *enige* wat ik kan doen is bevestigen of er een aankoop aan een e-mailadres is gekoppeld.

Let op: ik krijg regelmatig meldingen over licenties die niet correct worden bijgewerkt na de aanschaf van een nieuw apparaat.
Ik heb geen enkele controle over de betaling en accountsynchronisatie, dat wordt volledig door Google/AppGallery afgehandeld!

Uiteindelijk wordt de aankoop altijd hersteld, maar de stappen om dit proces te versnellen zijn onduidelijk.
:::

::: warning
Recente Huawei-apparaten hebben geen toegang tot Google-services.
In dat geval moet je de app opnieuw kopen in AppGallery (Huawei App Store).
:::

### Kun je [mijn-taal] vertalen of verbeteren?
Ik kan relatief eenvoudig een andere taal toevoegen, maar ik vertrouw op AI-vertaling omdat dat veel makkelijker is om bij regelmatige updates te gebruiken.
De vertaalbestanden zijn [hier](https://github.com/stephomi/nomad-translation) te vinden.

## Features

### Waarom beweegt de gizmo niet?
Je hebt mogelijk [pin ingeschakeld in de linker menubalk](tools#left-menu-toolbar). 

### Kunnen we animeren in Nomad?
Nog niet. Een tijdlijnfunctie die lagen kan animeren zou interessant kunnen zijn, maar is op dit moment niet echt gepland.  

Ik zou in de toekomst graag rigging/skinning ondersteunen, maar dat brengt een aantal uitdagingen met zich mee (met name de interactie met sculpting-tools...) dus er is nog niets zeker.


### Kunnen we echt low-poly modelleren?
Nog niet.
Dit valt niet echt binnen de scope van Nomad *Sculpt*, maar misschien bied ik in de toekomst een paar tools aan.


### Kunnen we uv en texturing doen?
Korte antwoord: Ja. Lange antwoord: Niet direct, maar er zijn verschillende manieren om Nomads uitstekende vertex paint-tools te combineren met uv's en textures.

* Nomad laat je kleur, roughness en materiaaleigenschappen direct in de vertices van je sculpt schilderen.
* Nomad ondersteunt zeer hoge vertex-aantallen zodat je kunt schilderen zonder je zorgen te maken over uv's.
* Nomad kan textures laden om in brushes te gebruiken, zodat je kunt stempelen en schilderen met textures.
* Nomad kan objecten laden die al textures toegewezen hebben, voor renderdoeleinden.
* Nomad kan [UV-unwrappen](topology.md#uv-unwrap) op low-poly-objecten.
* Kleur/roughness/metalness kan van textures naar vertices worden overgezet via [de projectopties](topology.md#reproject-to-vertex).
* Kleur/roughness/metalness/normals kan van vertices naar textures worden gebakken via [de bake-opties](topology.md#bake-to-texture)
* Baken en projecteren kan worden gedaan tussen losse objecten of meerdere objecten, of tussen de hoogste en laagste subdivisieniveaus van één object, wat een verscheidenheid aan bake- en project-workflows mogelijk maakt.
* Na het baken zal het exporteren van een obj ook textures exporteren, die je vervolgens in een app als Procreate kunt gebruiken om direct op textures te schilderen.

### Kan ik een turntable-video opnemen?
Niet gepland op dit moment; iOS heeft een [video-opnamefunctie](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) die heel eenvoudig te gebruiken is.

Op iOS doe je dit door vanaf de linkerbovenhoek naar beneden te vegen en op de opnameknop te tikken. Je krijgt een aftelling van 3 seconden; veeg het menu weg om Nomad te tonen en gebruik de turntable-functie. Als je klaar bent, veeg je opnieuw vanaf de rechterbovenhoek naar beneden en tik je weer op de opnameknop. Bewerk de video in de fotobibliotheek om overtollige beelden aan het begin en einde te verwijderen.

### Kun je [favoriete-functie] toevoegen als een top-level knop?
Ja, de onderste toolbar kan nu worden aangepast via het [interface](interface.md)-menu, en zwevende toolbars kunnen nu worden aangemaakt.

### Wat zijn de volgende features?
Voor de middellange/lange termijn-roadmap heb ik veel ideeën, maar ik weet het nog niet.  

Bugfixes en het verbeteren van bestaande functies hebben altijd een hogere prioriteit dan het toevoegen van nieuwe functies.


### Kunnen we riggen in Nomad?
Nee, maar het is wel gepland. Voor nu kun je vormen aan elkaar koppelen (parenten) en draaipunten aanpassen, wat eenvoudige poseerbare sculpts mogelijk maakt.

### Kunnen we meer dan 4 lichten gebruiken?
Nee, dit is een beperking van de realtime render-engine binnen Nomad. Het is mogelijk dit te faken met emissive-objecten en global illumination in post-process, zoals getoond in [deze tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Kunnen we Zbrush-tools importeren?
Nee, Zbrush gebruikt een proprietair formaat. Je zou de alpha-maps moeten kunnen exporteren en in Nomad gebruiken. 

### Waarom komen de kleuren niet overeen met wat ik heb geschilderd? Waarom krijg ik geen wit in de render?
Stel je een foto voor van een vel papier, versus een foto van een bureaulamp, versus een foto van de zon. Oudere camera's en schermen maken ze allemaal gewoon ‘wit’. Modernere systemen kunnen een verschil laten zien tussen het gereflecteerde wit van papier, het uitgestraalde licht van een lamp en het superheldere van de zon.

Moderne computergraphics probeert op een vergelijkbare manier te werken, door de fysica van licht en oppervlakken te emuleren. Dit heet `Physically Based Rendering`, of PBR, en Nomads PBR-renderer is hierop gebaseerd. Dit ziet er realistisch en gebalanceerd uit, maar vaak lijken fel geschilderde kleuren donkerder.

Als je wilt dat de render dichter bij de geschilderde kleuren ligt, kun je dit zowel op niet-fysisch gebaseerde als fysisch gebaseerde manieren oplossen:

Non PBR:
* `Gebruik de 'Unlit'-modus in het lichtmenu`. Kleuren worden exact getoond zoals geschilderd, maar je verliest ook alle shading. Handig voor snelle controles en meer grafische output.
* `Gebruik de 'Matcap'-modus in het lichtmenu`. Kies een helderdere matcap die grotendeels wit is, zonder kleurzweem.

PBR:
* `Gebruik een neutrale environment`. Je kunt [de environment veranderen](shading.md#environment) naar een neutralere. Vermijd indoor-environments omdat die vaak meer kleurzweem hebben. Kies liever een daglicht-buiten- of studio-environment.
* `Verhoog de belichting`. Als je een foto van wit papier in een donkere kamer zou maken, zou je simpelweg meer licht toevoegen. Verhoog bij de environment light de exposure-slider totdat de kleuren goed aanvoelen, of voeg meer individuele lichten met hogere intensiteit toe.
* `Verhoog de camera-exposure`. Als de donkere kamer geen extra lichten had, zou je de camera de sluiter langer open kunnen laten houden of een gevoeliger ISO gebruiken. In Nomad kun je een vergelijkbaar resultaat bereiken met post-processing. Ga naar post process, schakel in, ga naar tone mapping, schakel in en verhoog de exposure-slider totdat de kleuren goed aanvoelen.
* `Gebruik emissive color`. In het material-menu kun je 'emissive' inschakelen onder textures, waardoor een object als lichtbron verschijnt. Als je global illumination inschakelt in de post-process-instellingen, zal het licht werpen op andere objecten in de scène. Je kunt ook 'unlit' inschakelen voor dat materiaal, wat een vergelijkbare look geeft zonder texture.

## Crashes

### Het crasht wanneer ik mijn model opsla of remesh!
Je apparaat raakt door het geheugen (RAM) heen.  
Om het geheugengebruik in je scène te verminderen, kun je enkele van de [Topology](topology.md)-opties gebruiken om het aantal polygonen te verlagen.

::: tip RAM/Opslag
Waar het om gaat is de hoeveelheid RAM, niet de opslag (die meestal veel groter is).
:::


### Het crasht wanneer ik mijn project laad!
Als het bestand klein is, kun je het naar mij sturen en kijk ik ernaar (per e-mail <support@nomadsculpt.com>).

Anders raakt het apparaat waarschijnlijk door het RAM-geheugen heen.

- Zorg dat je alle andere geopende apps op je apparaat sluit.
- Start een nieuw project in Nomad in plaats van een project al geopend te hebben.
- Als het nog steeds crasht, is de enige oplossing om [je projectbestand](#where-are-my-projects-located-on-my-device) te laden op een apparaat met meer geheugen.

::: tip
Op een desktopbrowser kun je proberen je bestand te laden [op deze url](https://nomadsculpt.com/demo_save/) en het daarna weer te exporteren nadat je je scène hebt vereenvoudigd.

Sommige browsers beperken de hoeveelheid RAM die één tabblad kan gebruiken, dus het is mogelijk dat deze techniek niet werkt.

Als je project [Layers](layers.md) gebruikt, kun je overwegen ze samen te voegen om het geheugengebruik te verminderen.
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

### Het crasht wanneer ik Nomad start!
Als het crasht tijdens het laden, betekent dit dat Nomad moeite heeft met een bepaald bestand dat in de Nomad-map staat.

Meestal gebeurt dit omdat het project zwaar is en helaas de RAM-limiet zal overschrijden.

Zoek de [Nomad-map](#where-are-my-projects-located-on-my-device) op en hernoem of verplaats vervolgens enkele bestanden om de boosdoener te vinden.

Probeer eerst `settings.json` te hernoemen. Dan stopt Nomad met het laden van het laatst geopende project.

Als dat niet werkt, probeer dan enkele recente bestanden buiten hun respectievelijke resource-mappen te verplaatsen (`projects`, `matcaps`, `environments`, enz.).

Je kunt ook de mappen zelf hernoemen zodat Nomad ze volledig negeert.
Als je alle bestanden in de Nomad-map hernoemt of verplaatst, krijg je hetzelfde resultaat als een schone installatie.

::: tip
Wanneer Nomad een bestand bij het opstarten laadt, verplaatst het het bestand altijd naar de map `can_be_deleted/`.
Als de bewerking slaagt, wordt het vervolgens teruggezet naar de oorspronkelijke map.

Als het crasht voordat het laden is voltooid, zal Nomad bij de volgende start wel succesvol opstarten, omdat het de map `can_be_deleted/` negeert.

Je kunt gewoon proberen dit bestand opnieuw te laden als je denkt dat het kan slagen.
:::
