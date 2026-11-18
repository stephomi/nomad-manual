# ![](/icons/manual.webp) Tips {#tips}

[[toc]]

## Hoe begin je een model? {#how-to-start-a-model}

Beginners in 3d-sculpting vragen vaak wat de beste manier is om een model te beginnen. Er is geen beste manier: iedereen heeft zijn eigen voorkeur. Hier zijn een paar van de meest gebruikte aanpakken.

### Sculpten op een bol, multires {#sculpt-on-sphere-multires}

Het standaardmodel waarmee Nomad opstart, is de meest gebruikte manier. Duw en trek de bol in vorm met tools als verplaatsen, klei en plooi. Gebruik de lagere onderverdelingsniveaus als je snel grote veranderingen wilt maken, en de hogere voor detailwerk.

Een veelvoorkomend probleem is dat je polygonen tekortkomt waar je ze nodig hebt, terwijl je er elders te veel hebt. Duw je de standaardbol bijvoorbeeld uit tot een heel lichaam, dan heb je waarschijnlijk niet genoeg detail voor de vingers, terwijl er veel polygonen verspild worden aan de achterkant van het hoofd. Voor vooral ronde vormen zoals een hoofd kan dit echter prima werken.

### Dyntopo {#dyntopo}

Met Dyntopo aan worden er tijdens het sculpten automatisch polygonen toegevoegd en verwijderd waar dat nodig is. Dat zijn driehoeken, en beginners vinden die rommelige indeling vaak minder mooi dan de nette look van multires. Zet toch door! Zet vloeiende shading aan, het draadmodel uit, en maak je geen zorgen meer over de indeling: deze modus kan heel erg als klei aanvoelen. Vergeet niet dat deze modus met een groot penseel of een gladstrijkpenseel ook polygonen weghaalt, zodat de tool altijd snel en vlot blijft reageren. Als de eerste versie van je sculpt klaar is, kun je hem klonen, door de quad remesher halen voor een nette indeling, en de oorspronkelijke details op een hoog onderverdelingsniveau herprojecteren.

### Voxel-remesh {#voxel-remesh}

Een voxel-remesh geeft je sculpt een topologie die vooral uit quads bestaat. Bij lagere resoluties gaat dit snel, en zo vervang je snel uitgerekte of te dichte polygonen door een gelijkmatig verdeelde indeling. Dit is een prima manier om vanuit een bol een heel lichaam te maken: begin bijvoorbeeld met een hoofd, trek er een nek uit, voxel-remesh. Trek een romp uit, voxel-remesh, armen, voxel-remesh, enzovoort, tot je de basisvormen hebt.

### Meerdere objecten gebruiken {#use-multiple-objects}

Veel anatomieboeken bouwen een lichaam op uit eenvoudige bollen, cilinders en kubussen. Zo kun je in Nomad ook sculpten. Het voordeel is dat je objecten in de scènehiërarchie aan elkaar kunt koppelen, zodat bijvoorbeeld het hoofd meedraait als je de nek draait. Met de gizmotool kun je ook precies verplaatsen, draaien en schalen, en je kunt per vorm een draaipunt instellen zodat alles precies beweegt zoals je verwacht. Staan de basisblokken op hun plek, selecteer ze dan allemaal en voeg ze met een voxel-remesh of een booleaanse bewerking samen tot één oppervlak om verder in detail te sculpten.

Een handige tip bij deze werkwijze: begin met een bol, schaal hem tot een uitgerekte worst, tik op draaipunt, kies 'onderkant' en tik weer op draaipunt. Je hebt nu een lichaamsdeel dat je kunt klonen, langs de lengte van de eerste bol kunt verplaatsen, klonen, draaien, klonen, verschuiven, klonen enz., om snel een lichaam op te zetten.

### Buizen {#tubes}

De buistool is een prima manier om een sculpt te beginnen. Reptielenstaarten, armen, benen, vingers, wenkbrauwen: je schetst ze allemaal snel met de buistool en past ze daarna makkelijk aan. Je kunt ook het profiel van de doorsnede aanpassen, zodat je de vorm snel verandert. Valideer de vorm om erop te gaan sculpten, en voxel-remesh hem samen met andere objecten tot een mesh voor het hele lichaam.

### Andere apps gebruiken {#use-other-apps}

Sommige mensen beginnen een model liever in een andere app, en dat is ook prima. Met tools als Blender of Valence kun je een model beginnen met low-polytechnieken en het daarna in Nomad importeren om te sculpten.

### De ingebouwde presets gebruiken {#use-the-built-in-presets}

Tik in het menu [Bestanden](files.md) op `Preset…` links in het projectgedeelte. Daar vind je verschillende presets voor hoofden en lichaamsvormen van de Blender Foundation. Selecteer er een die je bevalt, tik er nog eens op en voeg hem toe aan je scène.

### Online modellen gebruiken {#use-online-models}

Online zijn veel gratis modellen te vinden, bijvoorbeeld op polyhaven, sketchfab en turbosquid. Meestal kun je die in Nomad importeren en er direct op sculpten, of ze als referentie gebruiken.

### Geen regels! {#no-rules}

Uiteindelijk kun je elke combinatie van deze technieken gebruiken, of geen enkele! Nomad is daarin heel flexibel. Gevorderde gebruikers beginnen misschien met buizen, gaan dan verder met dyntopo, combineren dat met een gedownloade voet, doen alles door de quad remesher en gebruiken tot slot multires voor het laatste detail. Wat voor jou werkt.

## Vlakkengroepen {#facegroups}

De vlakkengroeptool kun je voor veel dingen gebruiken, zoals uitgelegd in deze YouTube-video: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Dit is een samenvatting in tekst van wat er in die video aan bod komt.

### Waarom vlakkengroepen? {#why-facegroups}

Met vlakkengroepen kun je vlakken ordenen en selecteren ('vlakken' en 'polygonen' betekenen in deze handleiding hetzelfde). Dat is het makkelijkst uit te leggen door ze te vergelijken met de andere selectie- en ordeningstools van Nomad. In Nomad kun je objecten maken, ze een naam geven en ze aan elkaar koppelen; zo bouw je makkelijk een structuur van objecten op voor bijvoorbeeld een kamer met een vloer, muren, een stoel, een tafel enzovoort.

Voor een personage zet je misschien eerst de grote vormen neer met losse objecten voor hoofd, arm en been, maar zodra je alle stukken samenvoegt tot één mesh, is die structuur weg. Je kunt met maskers aan delen van een personage werken, maar het wordt vermoeiend om steeds opnieuw een masker te schilderen voor de handen, dan de neus, dan weer de handen.

Daar komen vlakkengroepen van pas. Je geeft vlakken een kleur als label, en kunt daarna polygonen met dezelfde kleur selecteren en bewerken. Let op: de kleur van een vlakkengroep en vertexkleur zijn twee verschillende dingen.

Je kunt het het best vergelijken met kleuren op een landkaart schilderen, en later landen of regio's op kleur kunnen selecteren.

Bij het hoofd van een personage kun je zones schilderen voor de oogkassen, neus, lippen, kin en oren, en die later makkelijk selecteren. Bij hard-surface- en mechanisch sculpten kun je er panelen en onderdelen mee afbakenen.

### Vlakkengroepen maken en bewerken {#creating-and-editing-facegroups}

Je kunt vlakkengroepen aanbrengen met een penseel, waarbij elke nieuwe streek een nieuwe vlakkengroep maakt, of je kunt de vlakkengroep onder de cursor oppakken en uitbreiden. Je kunt ze ook met vormen maken.

* Punt, standaardmodus - één sleepbeweging maakt een nieuwe vlakkengroepkleur aan en wijst die toe aan de vlakken waar je overheen sleept. Elke nieuwe sleepbeweging maakt een nieuwe vlakkengroep. Een tik vult een aaneengesloten gebied met een nieuwe vlakkengroep.
* Punt, modus `Kiezen` - als de knop `Kiezen` in de linker werkbalk actief is, pakt Nomad de vlakkengroep onder de cursor op en past die toe tijdens de rest van de sleepbeweging. Handig om vlakkengroepen bij te werken zonder ze eerst handmatig te selecteren.

### Maskeren {#masking}

Als de maskertool actief is en de vlakkengroepknop in de werkbalk ervan aan staat, maskeer je een vlakkengroep door erop te tikken.


### Verbergen {#hiding}

Als de verbergtool actief is en de vlakkengroepknop in de werkbalk ervan aan staat, verberg je een vlakkengroep door erop te tikken.

### Ordenen {#organizing}

Zoals eerder gezegd kun je met vlakkengroepen je mesh ordenen zonder losse objecten te hoeven maken. Je wilt een hoofd misschien niet opsplitsen in losse objecten voor neus, kin en oren, maar het is wel heel handig om ze als vlakkengroepen vast te leggen.

### UV-gebieden {#uv-regions}

De tool UV Atlas probeert zelf naden te bepalen, maar legt ze soms waar je ze niet wilt hebben. Heeft een object vlakkengroepen en staat de vlakkengroepoptie aan in de opties van UV Atlas, dan gebruikt hij de randen van de vlakkengroepen als UV-naden.

### Quad remesher {#quad-remesher}

De plugin quad remesher laat de randen meestal mooi over je model lopen, maar met de vlakkengroepoptie aan kun je hem met vlakkengroepen een handje helpen. Zo leg je makkelijk een nette edge flow vast rond de ogen, een wenkbrauwboog, de lippen of een wangplooi, bijvoorbeeld.

### Filteren met andere tools {#filter-with-other-tools}

Veel tools hebben opties om rekening te houden met vlakkengroepen, in hun eigen toolmenu of via het menu Streek -> Filter. De gladstrijktool kan bijvoorbeeld bij een sterkte boven 100% het detail binnen een vlakkengroep flink wegpoetsen, terwijl de rand van de vlakkengroep grotendeels intact blijft.

### Randen van vlakkengroepen ontspannen en gladstrijken {#relax-and-smooth-facegroup-borders}

De optie `Ontspannen` in de vlakkengroeptool strijkt de randen van vlakkengroepen uitstekend glad en laat de rest intact. Zo maak je mooi vloeiende randen tussen vlakkengroepen voordat je een quad remesh doet.

## Beperkingen op tablet/mobiel {#limitations-on-tabletmobile}

Tablets en telefoons zijn tegenwoordig erg krachtig, maar verschillen op belangrijke punten van desktops en laptops:

### Geen actieve koeling {#no-active-cooling}

Computers hebben ventilatoren en/of grote koellichamen om koel te blijven, en zijn gemaakt om op hoge temperaturen te draaien. Mobiele hardware is meestal in de eerste plaats ontworpen om dun te zijn, niet om de binnenkant koel te houden. Zet je Nomad op de hoogste kwaliteitsinstellingen (verlichtingsmodus PBR, complexe materialen, veel objecten, veel nabewerkingsopties aan), dan kan het apparaat oververhit raken en loopt de batterij heel snel leeg.

Beter is het om de matcap-verlichtingsmodus te gebruiken en een lagere `Renderresolutie` te kiezen (bovenaan het menu Nabewerking). Zo blijft het apparaat koel en kun je langer sculpten.

### Beperkt geheugen {#limited-memory}

Nomad kan resultaten halen die gelijk zijn aan die van de meeste sculptingapps op desktop, maar de wetten van de natuurkunde kan het niet buigen! De meeste desktops hebben twee keer zoveel geheugen als mobiele apparaten, en werkstations voor 3d-animatie vaak 4 of 8 keer zoveel. Het is daarom goed om in de gaten te houden hoeveel polygonen je gebruikt; test op je eigen apparaat wanneer het traag begint te worden. Bijna alle apparaten waarop Nomad draait, kunnen vrij makkelijk 1 miljoen polygonen aan. Een iPad Pro met M2 kan er zonder moeite 8 miljoen aan, en mensen hebben op de nieuwste iPads ruim boven dat aantal getest.

Toch hebben alleen de meest gedetailleerde sculpts meer dan 4 miljoen polygonen nodig. Maak je vrij eenvoudige objecten en kom je vaak boven 500.000, 1 miljoen of 4 miljoen uit, dan gebruik je te veel polygonen! Zorg dat `Vloeiende shading` aan staat in de [Instellingen](settings.md).

### Het besturingssysteem is minder vergevingsgezind voor zware apps {#os-is-less-forgiving-with-intensive-apps}

Apple en Android verwachten dat apps kleine bestanden heel snel opslaan en laden. Ze gaan er ook van uit dat apps heel snel kunnen wisselen tussen taken. Nomad gebruikt wat slimme trucs om bestanden vrij klein te houden en snel op te slaan, maar vindt het mobiele besturingssysteem dat Nomad er te lang over doet, dan sluit het de app gewoon af voordat de taak klaar is. Nog een reden om bestanden aan de kleine kant te houden: je kunt met sculpts van 37 miljoen polygonen werken, zoals een gebruiker op Discord meldde, maar aan te raden is het niet!

## Werken op kleine schermen {#working-on-small-screens}

Nomad is gemaakt voor tablets, maar werkt ook goed op telefoons. Met een paar aanpassingen aan de interface en je werkwijze wordt sculpten op een klein scherm zoals een telefoon een stuk makkelijker:

* Tik met 4 vingers om de hele interface te verbergen of te tonen, zodat je meer ruimte hebt om te sculpten.
* Sleep met 3 vingers omhoog en omlaag om de penseelstraal te veranderen.
* Je kunt de interface kleiner schalen zodat er meer knoppen passen als je goede ogen hebt, of groter als je slechte ogen hebt!
* De bredere menu's zitten soms in de weg bij het sculpten. Je kunt ze doorzichtig en onvervaagd maken, zodat je de sculpt onder het menu nog ziet.
* Sculpt je met een vinger, gebruik dan de optie [`Streekverschuiving`](stroke.md#stroke-offset) om het midden van het penseel een stukje van je vinger af te zetten.
* Deze en nog veel meer opties vind je in het [menu Interface](./interface.md).


## Opblaas- of piekdeformer {#inflate-or-peak-deformer}

Veel 3d-apps hebben een opblaasdeformer, die alle vertices over een instelbare afstand langs hun normaal naar buiten duwt. Nomad heeft op dit moment geen deformers, maar je kunt dit gedrag nabootsen met het opblaaspenseel:

* Kies het opblaaspenseel
* Zet in het [menu Streek](./stroke.md#stroke) de streekmethode op `Vergrendelen + straal`
* Maak de penseelstraal groter dan je sculpt; zoom zo nodig met de camera uit.
* Tik en sleep een streek over het oppervlak van je object; als de straal groter is dan het object, wordt de hele vorm gelijkmatig een vaste afstand opgeblazen.
* Stel de intensiteit van het penseel bij om te bepalen hoeveel er wordt opgeblazen
* Gebruik zo nodig een masker om bepaalde gebieden te beschermen of het effect daar te verminderen.

## Bultjes of 'puistjes' na een voxel-remesh weghalen {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Een voxel-remesh is ideaal voor gelijkmatig verdeelde polygonen, maar maakt soms een topologie die bij gladstrijken kleine bultjes of puistjes geeft. Bijvoorbeeld:

* Maak met het plooipenseel een krul op de standaardbol
* Doe een voxel-remesh met `Multiresolutie opbouwen` op 3
* Strijk glad met een hoge intensiteit
* Er verschijnen artefacten (makkelijker te zien met een matcapmateriaal met veel contrast):

![](/videos/tip_pimples_before.mp4)

Om het met sculpten op te lossen, probeer je de optie `Stabiel gladstrijken` in de instellingen van de gladstrijktool. Die kan overweg met de ongelijke topologie van de voxel-remesh en geeft een strak resultaat.

![](/videos/tip_pimples_stable_smooth.mp4)

Om de topologie zelf te herstellen, gebruik je een nieuwe primitieve, de quad-remeshtools of een extern 3d-modelleerprogramma, en projecteer je het detail van de oorspronkelijke mesh op de nieuwe via `Topologie -> Bakken -> Herprojecteer → Vertex`.

![](/videos/tip_pimples_reproject.mp4)

## Daglichtverlichting {#daylight-lighting}

De standaard PBR-render is, zoals de naam al zegt, fysiek gebaseerd. Net als een onbewerkte digitale foto kan hij er daardoor wat flets en vlak uitzien. Met de lichten en de nabewerking van Nomad kun je renders levendiger maken.

Hier is een standaardrender; eens kijken of we die mooier kunnen maken:
![](/images/tips_lighting_default.webp)

Nabewerking en toonmapping aanzetten geeft meer helderheid en contrast:

![](/images/tips_lighting_tonemap.webp)

Dan de lichten: het standaard omgevingslicht is prima om te sculpten, maar voor een eindrender kan het beter. Je kunt het zo bekijken: er is direct licht (bijvoorbeeld de zon) en omgevingslicht (bijvoorbeeld licht van de blauwe lucht en de grond). Door het omgevingslicht zwakker te maken en te draaien, krijg je al iets van de verlichting die je zou zien als het onderwerp in de schaduw stond:

![](/images/tips_lighting_env.webp)

Voeg een direct licht toe en zet de intensiteit hoog om fel zonlicht na te bootsen. Breng dat in balans met het omgevingslicht voor een mooi resultaat:

![](/images/tips_lighting_sunlight.webp)

Bij personages helpt het vaak om het materiaal op suboppervlak te zetten en een spotlicht achter het personage op de oren te richten, zodat ze gaan gloeien:

![](/images/tips_lighting_sss.webp)

Experimenteer daarna met de rest van de nabewerkingsinstellingen! Globale verlichting en ambient occlusion zorgen voor realistischere verlichting. Kromming en verscherpen halen meer detail uit de sculpt. Chromatische aberratie, scherptediepte, korrel, bloom en vignet bootsen camera-effecten na. Let op: hoe meer functies je aanzet, hoe meer je de verlichting en de andere nabewerkingswaarden moet bijstellen om dat te compenseren.

Hier is de render met een volledige set aanpassingen in de nabewerking:
![](/images/tips_lighting_final.webp)
