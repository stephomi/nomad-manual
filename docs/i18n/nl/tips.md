# ![](/icons/manual.webp) Tips {#tips}

[[toc]]

## Hoe een model te beginnen {#how-to-start-a-model}

Beginners in 3D‑sculpting vragen vaak wat de beste manier is om een model te beginnen. Er is geen beste manier; verschillende mensen hebben verschillende voorkeuren. Hier zijn enkele van de meer gangbare benaderingen.

### Beelden op bol, multires {#sculpt-on-sphere-multires}

Het standaardmodel wanneer Nomad start is de meest gebruikelijke manier. Gebruik de Move-, Clay- en Crease‑tools om de bol in vorm te duwen en te trekken; gebruik de lagere subdivisieniveaus wanneer je snel grote veranderingen wilt maken, gebruik hogere subdivisieniveaus voor detailwerk.

Een veelvoorkomend probleem is dat je vaak polygonen tekortkomt waar je ze nodig hebt, terwijl je elders te veel polygonen hebt. Als je bijvoorbeeld de standaardbol tot een volledig lichaam uitrekt, is de kans groot dat je niet genoeg detail hebt om de vingers te maken, terwijl je veel verspilde polygonen op de achterkant van het hoofd hebt. Voor overwegend bolvormige vormen zoals een hoofd kan dit echter prima zijn.

### Dyntopo {#dyntopo}

Door Dyntopo in te schakelen worden er adaptief polygonen toegevoegd en verwijderd terwijl je sculpt. Deze polygonen zijn driehoeken, en beginners houden vaak niet van de rommelige lay‑out vergeleken met de nette look van multires. Het is de moeite waard om vol te houden! Als je smooth shading inschakelt, wireframe uitschakelt en ophoudt je zorgen te maken over de lay‑out, kan deze modus een zeer klei‑achtig gevoel geven. Vergeet niet dat als je een grote brush of een smooth‑brush gebruikt, deze modus ook polygonen kan verwijderen, zodat de tool altijd snel en responsief aanvoelt. Zodra je een eerste pass van de sculpt af hebt, kun je deze klonen en door quad remesher halen om een nette lay‑out te krijgen, en de oorspronkelijke details opnieuw projecteren op een hoog subdivisieniveau.

### Voxel-remesh {#voxel-remesh}

Voxel remesh zal een grotendeels quad‑gebaseerde topologie op je sculpt toepassen. Deze bewerking is snel op lagere resoluties en kan worden gebruikt om snel uitgerekte of te dichte polygonen te vervangen door een gelijkmatig verdeelde lay‑out. Dit kan een geweldige manier zijn om een volledig lichaam vanuit een bol te starten; stel dat je met een hoofd begint, dan kun je een nek uittrekken, voxel remesh. Romp uittrekken, voxel remesh, armen, voxel remesh, enzovoort, totdat je de basisvormen hebt.

### Meerdere objecten gebruiken {#use-multiple-objects}

Veel anatomiegidsen stellen een lichaam voor met eenvoudige bollen, cilinders en kubussen. Je kunt in Nomad ook op deze manier sculpten. Dit heeft als voordeel dat je objecten in de scene‑hiërarchie aan elkaar kunt koppelen, zodat je bijvoorbeeld de nek kunt roteren en het hoofd volgt. Het kunnen gebruiken van de gizmo‑tool voor precieze translate/rotate/scale is ook erg nuttig, en je kunt per vorm pivots instellen zodat ze precies bewegen zoals je verwacht. Wanneer de basisblokken op de juiste plaats staan, kun je ze allemaal selecteren en voxel remesh of booleans gebruiken om ze samen te voegen tot één oppervlak voor meer gedetailleerd sculpten.

Een handige tip voor deze manier van werken is om met een bol te beginnen, deze te schalen tot een uitgerekte worst, op Pivot te drukken, op ‘Bottom’ te klikken, en nogmaals op Pivot te drukken. Je hebt nu een lichaamsdeel dat je kunt klonen, langs de lengte van de eerste bol kunt verplaatsen, klonen, roteren, klonen, schuiven, klonen, enzovoort, om snel een lichaam uit te zetten.

### Buizen {#tubes}

De Tube‑tool is een geweldige manier om een sculpt te beginnen. Reptielenstaarten, armen, benen, vingers, wenkbrauwen: ze kunnen allemaal snel worden geschetst met de Tube‑tool en daarna eenvoudig worden bewerkt. Je kunt ook het profiel van de dwarsdoorsnede aanpassen, wat snelle vormveranderingen mogelijk maakt. Je kunt de vorm valideren om erop te gaan sculpten, en hem samen met andere objecten voxel remeshen om een volledig lichaamsmesh te krijgen.

### Andere apps gebruiken {#use-other-apps}

Sommige mensen beginnen liever een model in andere apps, dat is ook prima. Tools zoals Blender of Valence maken het mogelijk om modellen met low‑poly‑technieken te starten; deze kunnen vervolgens in Nomad worden geïmporteerd voor sculpting.

### De ingebouwde presets gebruiken {#use-the-built-in-presets}

Klik in het Project‑menu rechtsboven op `Preset...`. Hier vind je verschillende hoofd‑ en lichaamsvorm‑presets van de Blender Foundation. Selecteer er een die je bevalt, tik er nogmaals op en voeg hem toe aan je scene. 

### Online modellen gebruiken {#use-online-models}

Er zijn veel gratis modellen online beschikbaar, bijvoorbeeld Polyhaven, Sketchfab, Turbosquid. Meestal kunnen deze modellen in Nomad worden geïmporteerd en ofwel direct worden gesculpt, of als referentie worden gebruikt.

### Geen regels! {#no-rules}

Uiteindelijk kun je elke combinatie van deze technieken gebruiken, of geen enkele! Nomad is hierin erg flexibel; gevorderde gebruikers beginnen misschien met tubes, gaan dan naar dyntopo, combineren het vervolgens met een gedownload voetmodel, doen daarna een quad remesh over alles, en gebruiken tenslotte multires voor het einddetail. Wat voor jou werkt, is goed.

## Facegroups {#facegroups}

De Facegroup‑tool kan voor veel dingen worden gebruikt, zoals uitgelegd in deze YouTube‑video: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Dit is een tekstsamenvatting van de functies die in die video worden behandeld.

### Waarom facegroups? {#why-facegroups}

Facegroups laten je vlakken organiseren en selecteren (‘faces’ en ‘polygons’ worden in deze handleiding door elkaar gebruikt). Dit is makkelijker uit te leggen vergeleken met Nomads andere selectie‑ en organisatietools. Nomad laat je objecten maken, ze een naam geven, ze aan elkaar koppelen; het is eenvoudig om een structuur van objecten te maken om een kamer te definiëren die bestaat uit vloer, muren, stoel, tafel enzovoort.

Voor een personage kun je een eerste block‑out doen met aparte objecten voor hoofd, arm, been, maar zodra je alle stukken samenvoegt tot één mesh, gaat deze structuur verloren. Je kunt met maskers aan subsecties van een personage werken, maar het kan vermoeiend worden om steeds weer een masker voor de handen, dan de neus, dan weer de handen te schilderen.

Hier zijn facegroups nuttig. Ze laten je polygon‑vlakken taggen met een kleur, en vervolgens polygonen selecteren en manipuleren die dezelfde kleur hebben. Merk op dat facegroup‑kleur en vertex‑kleur verschillende dingen zijn.

De meest vergelijkbare analogie is kleuren op een kaart schilderen, en later landen of regio’s kunnen selecteren op basis van kleur.

Voor personagehoofden kun je zones schilderen om de oogkassen, neus, lippen, kin, oren te markeren, en die zones later eenvoudig selecteren. Voor hard‑surface‑ en mechanisch sculpten kan het handig zijn om panelen en secties te definiëren.

### Facegroups maken en bewerken {#creating-and-editing-facegroups}

Facegroups kunnen met een brush worden toegepast, waarbij elke nieuwe streek een nieuwe facegroup maakt, of ze kunnen de facegroup onder de cursor selecteren en uitbreiden. Ze kunnen ook met vormen worden gemaakt.

* Dot, auto‑pick ingeschakeld – een enkele sleepbeweging definieert een nieuwe facegroup‑kleur en wijst die toe aan de vlakken waarover je sleept. Elke nieuwe sleepbeweging definieert een nieuwe facegroup. Een tik zal een nieuwe facegroup floodfillen.
* Dot, auto‑pick uitgeschakeld – wanneer de auto‑pick‑knop in zijn ‘sub’-modus staat, zal Nomad de facegroup onder de cursor selecteren en deze toepassen tijdens de rest van de sleepbeweging. Dit is handig om facegroups te verfijnen zonder ze handmatig te hoeven selecteren.

### Maskeren {#masking}

Wanneer de Mask‑tool actief is en de Facegroup‑knop actief is op de toolbar, zal het tikken op een facegroup deze maskeren.

### Verbergen {#hiding}

Wanneer de Hide‑tool actief is en de Facegroup‑knop actief is op de toolbar, zal het tikken op een facegroup deze verbergen.

### Organiseren {#organizing}

Zoals eerder vermeld kunnen facegroups worden gebruikt om je mesh te organiseren zonder dat je aparte objecten hoeft te maken. Je wilt een hoofd misschien niet opsplitsen in aparte objecten voor neus, kin, oren, maar het is erg handig om ze via facegroups gedefinieerd te hebben.

### UV-regio's {#uv-regions}

De UV Atlas‑tool zal proberen naden automatisch te definiëren, maar zal soms naden plaatsen waar je ze niet wilt. Als er facegroups op een object bestaan en de Facegroup‑optie actief is in de UV Atlas‑opties, zal hij in plaats daarvan de facegroup‑randen als UV‑naden gebruiken.

### Quad-remesher {#quad-remesher}

De Quad Remesher‑plugin zal de randen meestal netjes over je model laten lopen, maar je kunt facegroups gebruiken om hem te sturen wanneer de Facegroup‑optie is ingeschakeld. Dit kan het eenvoudig maken om een nette edge‑flow rond ogen, wenkbrauwrand, lippen, wangplooi bijvoorbeeld te definiëren.

### Filteren met andere gereedschappen {#filter-with-other-tools}

Veel tools hebben opties om facegroup‑bewust te zijn, hetzij vanuit hun primaire toolmenu, hetzij via het menu Stroke -> Filtering. De Smooth‑tool kan bijvoorbeeld bij sterktes boven 100% agressief detail binnen een facegroup weg‑smoothen, maar de facegroup‑rand relatief intact houden.

### Facegroup-randen ontspannen en gladmaken {#relax-and-smooth-facegroup-borders}

De Relax‑optie binnen de Facegroup‑tool doet uitstekend werk in het smoothen van facegroup‑randen terwijl andere features intact blijven. Dit kan een geweldige manier zijn om gladde facegroup‑randregio’s te definiëren vóór het quad remeshen.

## Beperkingen op tablet/mobiel {#limitations-on-tabletmobile}

Huidige tablets en mobieltjes zijn zeer krachtig, maar hebben belangrijke verschillen met desktopcomputers en laptops:

### Geen actieve koeling {#no-active-cooling}

Computers hebben ventilatoren en/of grote heatsinks om ze koel te houden en zijn ontworpen om op hoge temperaturen te draaien. Mobiele hardware is meestal in de eerste plaats ontworpen voor dunheid, niet om de interne onderdelen koel te houden. Als Nomad op de hoogste kwaliteitsinstellingen wordt gedraaid (PBR‑lichtmodus, complexe materialen, veel objecten, veel post‑processingopties ingeschakeld), kan dit zowel het apparaat oververhitten als de batterij zeer snel leegtrekken. 

Een betere aanpak is om een matcap‑lichtmodus te gebruiken en een lagere render multiplier (bovenaan het Post Process‑menu). Deze keuzes houden het apparaat koel en laten je langer sculpten.

### Beperkt geheugen {#limited-memory}

Nomad kan resultaten behalen die gelijk zijn aan de meeste desktop‑sculptingapps, maar kan de natuurwetten niet buigen! De meeste desktopcomputers hebben het dubbele geheugen van mobiele apparaten; workstations die voor 3D‑animatie zijn gebouwd, hebben vaak 4x of 8x zoveel geheugen. Daarom is het goed om je bewust te zijn van hoeveel polygonen je gebruikt; doe wat tests op je apparaat om te zien wanneer het traag begint te worden. Vrijwel alle apparaten die Nomad kunnen draaien, kunnen 1 miljoen polygonen vrij gemakkelijk aan. Een M2 iPad Pro kan comfortabel 8 miljoen aan; mensen hebben op de nieuwste iPads tests gedaan die daar ruim boven gaan.

Dat gezegd hebbende, alleen de meest gedetailleerde sculpts hebben meer dan 4 miljoen polys nodig; als je relatief eenvoudige objecten maakt en merkt dat je vaak boven 500.000, 1 miljoen, 4 miljoen uitkomt, gebruik je te veel polygonen! Zorg dat smooth shaded‑modus is ingeschakeld in de opties.

### OS is minder vergevingsgezind met intensieve apps {#os-is-less-forgiving-with-intensive-apps}

Apple en Android verwachten dat apps kleine bestanden zeer snel opslaan en laden. Ze gaan er ook van uit dat apps zeer snel kunnen wisselen tussen taken. Nomad doet opnieuw slimme trucs om bestandsgroottes relatief klein te houden en ze zeer snel op te slaan, maar als het mobiele OS besluit dat Nomad te lang bezig is, zal het de app simpelweg afsluiten voordat hij zijn taak heeft voltooid. Dit is nog een reden om bestanden aan de kleine kant te houden; het is mogelijk om met sculpts van 37 miljoen polys te werken, zoals een gebruiker op Discord meldde, maar het wordt niet aanbevolen!

## Werken op kleine schermen {#working-on-small-screens}

Nomad is ontworpen om op tablets te werken, maar werkt ook goed op telefoons. Sculpten op een klein scherm zoals een telefoon kan makkelijker worden gemaakt met een paar UI‑ en workflow‑aanpassingen:

* Een tik met 4 vingers schakelt de volledige UI aan/uit, zodat je meer ruimte hebt om te sculpten.
* Een sleepbeweging met 3 vingers omhoog en omlaag verandert de brush‑radius.
* De UI‑schaal kan kleiner worden gemaakt om meer knoppen te laten passen als je goed zicht hebt, of groter als je slecht zicht hebt.
* De bredere menu’s kunnen soms in de weg zitten van de sculpt; je kunt ze transparant en onscherp maken zodat je de sculpt onder het menu kunt zien.
* Als je met een vinger sculpt, gebruik dan de Offset‑optie om het brush‑centrum een beetje van je vinger af te zetten.
* Deze en veel meer opties zijn te vinden in het [Interface‑menu](./interface.md). 

## Inflate- of peak-deformer {#inflate-or-peak-deformer}

Veel 3D‑apps hebben een Inflate‑deformer die alle vertices langs hun normaal met een instelbare hoeveelheid naar buiten duwt. Hoewel Nomad momenteel geen deformers heeft, is het mogelijk dit gedrag te emuleren met de Inflate‑brush:

* Selecteer de Inflate‑brush
* Verander in het [Stroke‑menu](./stroke.md#stroke) de stroke‑methode naar `Lock + Radius'
* Maak de brush‑radius groter dan je sculpt; zoom de camera indien nodig weg van de sculpt.
* Klik en sleep een stroke op het oppervlak van je object; wanneer de radius groter is dan het object, wordt de volledige vorm gelijkmatig met een vaste hoeveelheid opgeblazen.
* Pas de brush‑intensiteit aan om de hoeveelheid inflatie te regelen.
* Gebruik masking indien nodig om bepaalde gebieden te beschermen of het effect van Inflate daar te verminderen.

## Bulten of 'puistjes' verwijderen na een voxel-remesh-bewerking {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel remesh is geweldig om gelijkmatig verdeelde polygonen te maken, maar creëert soms topologie die kleine bultjes of puistjes veroorzaakt bij het smoothen. Bijvoorbeeld:

* Gebruik de Crease‑brush op de standaardbol en maak een swirl
* Voxel remesh met ‘build multiresolution at 3’
* Smooth met hoge intensiteit
* Artefacten verschijnen (makkelijker te zien met een hoog‑contrast matcap‑materiaal):

![](/videos/tip_pimples_before.mp4)

Om dit via sculpting te verhelpen, probeer de optie `Stable smoothing` in de Smooth‑instellingen. Deze kan de ongelijke topologielay‑out van de voxel remesh aan en levert schone resultaten op.

![](/videos/tip_pimples_stable_smooth.mp4)

Om de topologie zelf te repareren, gebruik een nieuwe primitive, of de Quad Remesh‑tools, of een externe 3D‑modeler, en projecteer detail van de oorspronkelijke mesh naar de nieuwe via `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Daglichtbelichting {#daylight-lighting}

De standaard PBR‑render is, zoals de naam al aangeeft, fysiek gebaseerd, wat – net als een onbewerkte digitale foto – er wat flets en vlak uit kan zien. Nomads lichten en post‑processing kunnen worden gebruikt om renders er levendiger uit te laten zien.

Hier is een standaardrender; laten we kijken of we hem beter kunnen laten ogen:
![](/images/tips_lighting_default.webp)

Door Post Processing en Tonemapping in te schakelen kun je helderheid en contrast toevoegen:

![](/images/tips_lighting_tonemap.webp)

Om je op de lichten te concentreren: het standaard omgevingslicht is goed om mee te sculpten, maar kan worden verbeterd voor een eindrender. Een manier om hierover na te denken is om direct licht (bijv. de zon) te scheiden van omgevingslicht (bijv. licht van de blauwe lucht, de grond). Door het omgevingslicht te verminderen en te roteren, begin je vast te leggen hoe de belichting eruit zou moeten zien als het onderwerp zich in een schaduwrijke omgeving bevindt:

![](/images/tips_lighting_env.webp)

Er kan een direct licht worden toegevoegd en de intensiteit kan worden verhoogd om harde zon te simuleren. Door dit in balans te brengen met het omgevingslicht bereik je een aangenaam resultaat:

![](/images/tips_lighting_sunlight.webp)

Personages kunnen profiteren van het wisselen van hun materiaal naar Subsurface en het plaatsen van een spotlight achter het personage, gericht op de oren om ze te laten gloeien:

![](/images/tips_lighting_sss.webp)

Experimenteer daarna met de rest van de Post Process‑instellingen! Global Illumination en Ambient Occlusion helpen bij realistischer licht. Curvature en Sharpen kunnen helpen om meer detail in de sculpt naar voren te brengen. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette helpen camera‑effecten te simuleren. Merk op dat naarmate er meer features worden ingeschakeld, de belichting en andere post‑processingwaarden moeten worden aangepast om dit te compenseren.

Hier is de render met een volledige set post‑processingaanpassingen:
![](/images/tips_lighting_final.webp)