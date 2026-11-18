# ![](/icons/brush.webp) Streek {#stroke}

---
![](/images/stroke_overview.webp) 

## Overzicht {#overview}

Bij de meeste penselen kun je aanpassen hoe de streek zich gedraagt.
De instellingen lijken op die van 2d-tekenapps, maar sommige opties zijn specifiek voor sculpting en 3d.

De opties zijn verdeeld over 5 submenu's:

| Naam     | Icoon                        | Beschrijving                                                       |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Streek   | ![](/icons/brush.webp)      | Bepaalt hoe de streek op het model wordt toegepast                 |
| Alpha    | ![](/icons/alpha.webp)      | Hoe een grijswaardentextuur wordt gebruikt als penseelafdruk       |
| Afname   | ![](/icons/falloff.webp)    | Bepaalt hoe de sterkte van het penseel verloopt van midden naar rand |
| Filter   | ![](/icons/filter.webp)     | Hoe de geometrie van het model het penseel beïnvloedt              |
| Druk     | ![](/icons/pressure.webp)   | Bepaalt hoe het penseel reageert op de druk van je stylus          |

::: tip
Niet elke streekoptie geldt voor elke tool. Opties die de huidige tool niet gebruikt, zijn uitgeschakeld of verborgen.
:::


## ![](/icons/brush.webp) Streek {#stroke-1}

### ![](/icons/radius.webp) Straal {#radius}

![](/images/stroke_radius.webp)

De straalopties zijn globale instellingen: ze gelden voor elke tool.

#### Ruimte {#size}

* `Scherm` - de straal wordt in schermeenheden ingesteld. Maak je de straal 100 pixels breed, dan blijft hij 100 pixels breed, of je nu in- of uitzoomt.
* `Wereld (3D)` - de straal wordt in 3d-eenheden ingesteld. Maak je bijvoorbeeld een bol en stel je de straal even groot in als die bol, dan blijft de straal even groot als de bol, hoe je ook in- of uitzoomt.

#### ![](/icons/link.webp) Sneltoets synchroniseren {#sync-shortcut}

Als dit aan staat, blijven de straal- en silhouetinstellingen gelijk wanneer je naar de sneltoetspenselen overschakelt (`Gladstrijken`, `Masker` of `Verbergen`). Zo gebruikt een snelle gladstrijk- of maskeerbeurt dezelfde penseelgrootte als de tool waarmee je bezig was.

#### ![](/icons/link.webp) Deel straal {#share-radius}

Als dit aan staat, gebruiken alle tools dezelfde straal. Standaard heeft elke tool zijn eigen straal.


### Streektype {#stroke-type}

![](/images/stroke_strokemode.webp)

Een streek kan op verschillende manieren werken:

### ![](/icons/stroke_dot.webp) Punt {#dot}
Sleep zoals bij een gewone verfstreek.
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rollen {#roll}
De alpha van het penseel draait mee met de richting van de streek. Handig om stiksels in stof te maken.
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Vergrendelen + straal {#lock-radius}
Stempelt een penseelafdruk met een vaste **_hoogte_**. Door te slepen stel je de schaal en de rotatie in.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Vergrendelen + intensiteit {#lock-intensity}
Stempelt een penseelafdruk met een vaste **_straal_**. Door te slepen stel je de hoogte en de rotatie in.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
De modi `Vergrendelen + straal` en `Vergrendelen + intensiteit` negeren de instellingen voor [Druk](#pressure), omdat het slepen de grootte en de sterkte al bepaalt.
:::

![](/images/stroke_strokemodemove.webp)

De tools `Verplaats` en `Slepen` hebben hun eigen 3 opties:

### ![](/icons/snake.webp) Slepen {#drag}

Werkt tijdens de streek steeds bij wat zich binnen de penseelstraal bevindt. Bij een snelle streek blijft het oppervlak achter, terwijl een langzame streek het materiaal vasthoudt en zo langere vormen maakt. Dit is de standaardmodus van de tool `Slepen`. Met `Dynamische topologie` kun je hiermee slangachtige uitstulpingen maken.
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grijpen {#grab}
Selecteert wat zich binnen de penseelstraal bevindt op het moment dat je de streek begint, en houdt die selectie vast. Dat is handig voor nauwkeuriger verplaatsen: je kunt de afstand rustig bijstellen zonder per ongeluk meer te verplaatsen dan je in eerste instantie had geselecteerd. Dit is de standaardmodus van de tool `Verplaats`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Vergrendelen + straal (slepen) {#lock-radius-drag}
De ingestelde straal wordt genegeerd en hangt af van hoe ver je de streek vanaf het beginpunt sleept: een kleine afstand geeft een kleine straal, een grotere afstand een grotere straal. Met de intensiteitsschuif bepaal je de vorm van de afname. Handig om organische, rubberachtige vormen neer te zetten.
![](/videos/stroke_lockradius_drag.mp4) 

Sommige andere tools tonen hier hun eigen streektypes, bijvoorbeeld `Ontspannen`, `Gladstrijken` en `Vlekken` bij de gladstrijktools, of vormen zoals `Lasso` en `Kromme` bij de tools die met selecties werken. Die worden bij elke [tool](tools.md) beschreven.


### Pas de intensiteit van de ruimte aan {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Streken met een kleine tussenruimte (minder dan 50%) stapelen snel op en worden daardoor sterker dan streken met een grotere tussenruimte. Deze schakelaar compenseert dat, zodat streken ongeveer even sterk zijn, wat de tussenruimte ook is.

### Streekafstand {#stroke-spacing}
Hoe ver de afdrukken van het penseel tijdens het slepen uit elkaar liggen. Onder 100% overlappen ze en lijkt de streek doorlopend. Boven 100% ontstaan er gaten, handig voor details zoals stiksels of ritsen.

### Trage touwstabilisator {#lazy-rope-stabilizer}
De streek loopt een bepaalde afstand achter de aanwijzer aan. Zo kun je vloeiende lijnen tekenen.
![](/videos/stroke_lazy_rope.mp4) 

### Streekvervloeiing {#stroke-smoothing}
Neemt het gemiddelde van meerdere aanwijzerposities voor een vloeiendere streek.
Bij hoge waarden loopt de streek achter de aanwijzer aan, maar haalt hem uiteindelijk in.
Handig om vloeiende lijnen te tekenen.

### Snapstraal {#snap-radius}
Laat de streek aansluiten op de vorige als de aanwijzer begint in de buurt van waar de vorige streek eindigde. De straal bepaalt hoe ver er naar het einde van de vorige streek wordt gezocht. Handig als je lange doorlopende lijnen tekent en daarbij vaak even pauzeert.

### ![](/icons/trail.webp) Spoor {#trail}

Als dit aan staat, past elke nieuwe afdruk ook de laatste punten van de streek erachter opnieuw toe. `Spooraantal` bepaalt hoeveel punten opnieuw worden toegepast, `Spoorintensiteit` hoe sterk ze zijn en `Spoorstraal` hoeveel groter ze worden.

Spoor werkt alleen met het streektype `Punt`, en niet met de [afname-invloed](#influence) `Kam`.

### ![](/icons/silhouette.webp) Silhouet {#silhouette}
![](/images/stroke_silhouette.webp)
Standaard werkt een streek alleen op het oppervlak van het model binnen de penseelstraal. Met silhouet aan wordt de streek door het hele model heen geprojecteerd. Dat is erg handig bij het eerste opzetten van een model, of voor vormen waarvan de zijkanten loodrecht moeten blijven.

Je kunt de projectierichting zelf instellen:

* `X`, `Y`, `Z` - projecteert langs een vaste as.
* `Bekijken` - projecteert langs de kijkrichting van de camera.
* `Als vastgemaakt` - projecteert langs de kijkrichting van de camera, maar alleen zolang de camera op een aanzicht is vastgeklikt. Anders blijft het een gewone streek.
* `Dichtstbijzijnde` - projecteert langs de as die het dichtst bij de kijkrichting van de camera ligt. Dit is de standaard.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Willekeurig {#randomize}

![](/images/stroke_randomize.webp)

De `Intensiteit`, `Verschuiving`, `Rotatie` en `Schaal` van de streek kun je elk willekeurig laten variëren. Met het vinkje van een rij zet je die aan of uit. Zo krijg je allerlei effecten: met de schildertool geeft het bijvoorbeeld een gevlekte kleur, en met de plooitool kun je er huiddetail mee maken.

`Periode (langzamer)` bepaalt de lengte van de willekeurige cyclus: verhoog hem voor trage, golvende variaties, verlaag hem voor snelle ruis. Met het kleine knopje naast elke rij schaal je de periode voor alleen die rij.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Willekeurig - HSV {#randomize-hsv}

Bij tools die schilderen kun je ook de `Kleurtoon`, `Verzadiging` en `Waarde` van de verfkleur willekeurig laten variëren, met een eigen periode. Ideaal voor subtiele kleurvariatie in huid of steen.

### Streekverschuiving {#stroke-offset}

Verschuift de streek een vaste afstand, zodat je vinger hem niet bedekt. Handig op kleine schermen. Het is een globale instelling: zet hem aan met het vinkje, en hij geldt voor elke tool.


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

De `Alpha` is een textuur die bepaalt hoe je penseel werkt.
Het is een grijswaardenafbeelding: zwarte pixels betekenen geen vervorming, witte pixels volledige vervorming.

Tik op de alpha-afbeelding om een andere te kiezen. Naast de ingebouwde alpha's en je eigen geïmporteerde afbeeldingen kan de alphalijst ook displacement maps van Poly Haven downloaden.

Tik op het materiaalvoorbeeld om een alpha uit een materiaalpreset te laden. Hier kun je ook materiaalpresets opslaan en ervoor kiezen om texturen in de tool in te sluiten.

::: tip
De textuur wordt nooit verkleind, dus grote texturen kunnen alles trager maken.
:::

### ![](/icons/blend_contrast.webp) Alpha corrigeren {#invert-pixels}
De knop `Corrigeren...` bij een geïmporteerde alpha opent een venster dat de afbeelding zelf corrigeert: de middenwaarde, het inverteren van de pixels (zwart wordt wit en wit wordt zwart), een rotatie van 90° en horizontaal of verticaal spiegelen. Het afbeeldingsbestand wordt herschreven, dus ook andere apps zien de gecorrigeerde afbeelding.

::: tip

De ingebouwde alpha's die met Nomad worden meegeleverd, kun je niet corrigeren.

:::

### Projectie {#projection}

Hoe de alpha op het model wordt geprojecteerd:

* `Oppervlak` - de alpha ligt op het oppervlak onder het penseel en volgt de oriëntatie ervan.
* `Scherm` - de alpha wordt recht vanuit het beeld geprojecteerd.
* `Tegel` - de alpha wordt vanuit het beeld geprojecteerd en blijft op zijn plek terwijl je eroverheen schildert, net als een sjabloon, zodat een herhalend patroon naadloos aansluit. De rotatie is vergrendeld en de pendruk verandert de grootte van het patroon niet.
* `Triplanar` - de alpha wordt langs de 3 assen geprojecteerd. De opties voor schalen, rotatie en patroontegels hieronder worden vervangen door de instellingen van de triplanar textuur.

### ![](/icons/diagonal.webp) Schalen {#scaling}

Het penseel in Nomad is een cirkel met een straal die je zelf instelt. Texturen zijn vaak vierkant of rechthoekig; met de parameters voor `Schalen` bepaal je hoe de textuur in de cirkel past. Bij een vierkante textuur past een waarde van 0,7 binnen de cirkel. Bij een waarde van 1 wordt de textuur groter geschaald, zodat de cirkel erin past en de randen wegvallen.

![](/images/alpha_scaling.webp) 

Zet je `Schalen Y` aan, dan kun je de alpha verticaal uitrekken. De eerste schuif wordt dan `Schalen X`.

![](/images/alpha_scaling_y.webp) 

`Horizontaal spiegelen` spiegelt de alpha van links naar rechts.

### Rotatie {#rotation}

De alpha-textuur draait mee met de richting van de streek. Je kunt een rotatieverschuiving toevoegen, en als het slotje aan staat, blijft de textuur vast in die rotatie ten opzichte van het scherm.

Met de penknop ernaast draait de alpha mee als je je stylus om zijn as draait (barrel roll), bij de streken `Vergrendelen + straal` en `Vergrendelen + intensiteit` en zolang de rotatie niet vergrendeld is. Dit werkt alleen met een stylus die het ondersteunt.

### Patroontegels {#tiling}
![](/images/stroke_tiling.webp) 

Hoe vaak de textuur zich herhaalt binnen het penseelprofiel. Met `Patroontegels - X` en `Patroontegels - Y` kun je kiezen voor één enkele textuur in de streek (`Geen`), herhaalde texturen (`Herhaal`), of gespiegelde, waarbij elke tweede textuur wordt omgedraaid om patronen te maken of naadloze texturen te helpen maken (`Spiegeling`). Ze zijn beschikbaar met de streek `Rollen`, de projectie `Tegel`, of `Patroontegels` boven 1.

`Strakke pasvorm (niet-vierkante afbeeldingen)` doet er alleen toe bij niet-vierkante alpha's en penseeltexturen. Als dit aan staat, wordt elke afbeelding op zichzelf getegeld, zonder tussenruimte. Zet het uit om de alpha en de andere afbeeldingen gelijk te laten lopen als hun beeldverhoudingen verschillen.

![](/videos/alpha_tiling.mp4) 



### Middenwaarde {#mid-value}

Standaard betekenen zwarte pixels geen vervorming en witte pixels volledige positieve vervorming. Een kleipenseel met een alpha-textuur van rotsen trekt het oppervlak dus alleen naar buiten waar de alpha niet zwart is.

Wil je dat het penseel het oppervlak naar binnen duwt, of zowel naar binnen duwt ALS naar buiten trekt, pas dan de middenwaarde aan. Stel je de waarde in op 0,5, dan doet een middengrijs in de alpha niets, duwt zwart naar binnen en trekt wit naar buiten.

Twee knoppen helpen je de juiste waarde te vinden: de vierkante knop leest de middenwaarde af van de rand van de afbeelding, en met de kiezer pik je hem direct op de alpha zelf.




## ![](/icons/falloff.webp) Afname {#falloff}

![](/images/falloff_menu.webp) 

Dit lijkt op de [Alpha](#alpha), alleen stuur je de intensiteit hier met één enkele curve. De afname wordt gecombineerd met de alpha: zo gebruik je een textuur voor detail en de afname om het vervagen naar de rand en de intensiteit in het midden van de tool te regelen.

Staat de curve bovenaan, dan is er volledige vervorming; staat hij onderaan, dan heeft het penseel geen effect.

Zie de curve als een dwarsdoorsnede door de punt van het penseel. Het onderste deel toont hoe één enkele 'afdruk' van het penseel er op het oppervlak van het model uitziet. Heeft het penseel een alpha-textuur, dan wordt die ook getoond, zodat je ziet hoe de afname en de alpha samenwerken.

### ![](/icons/fx.webp) Preset {#preset}
Met `Preset...` geselecteerd opent een tik op de curvegrafiek een menu met presets. Ronde curves geven zachtere resultaten, hoekige curves scherpere. De knop `Aftrekken` in de linker werkbalk keert de afname in feite om: de bovenkant van de curve duwt dan het oppervlak in in plaats van eruit te trekken, of andersom.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Hiermee teken je je eigen afnamecurves. De curve-editor werkt net als de curves elders in Nomad:

* Tik op de curve om een nieuw punt te maken
* Sleep een punt om het te verplaatsen
* Tik op een punt om te wisselen tussen scherp en vloeiend
* Sleep een punt op een buurpunt om het te verwijderen

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Hiermee teken je je eigen afnamecurves. De editor werkt hetzelfde als bij Catmull-Rom, maar de punten trekken aan de curve in plaats van er direct op te liggen. Zo maak je makkelijker vloeiende curvevormen.

### ![](/icons/curve_bevel.webp) Afschuining {#bevel}
De punten worden verbonden met rechte lijnen, met afgeronde hoeken waarvan de grootte afhangt van de scherpte van elk punt. Handig voor penselen met een vlakke bovenkant en een strakke afschuining aan de rand.

De curve-editor heeft 3 knoppen:

| Item          | Icoon                       | Beschrijving                                   |
| :-----------: | :-------------------------: | :--------------------------------------------: |
| Maximaliseren | ![](/icons/maximize.webp)  | Vergroot de curve-editor                       |
| Herstellen    | ![](/icons/reset.webp)     | Zet de curve terug naar de standaardvorm       |
| Symmetrie     | ![](/icons/symmetric.webp) | Toont de curve als een symmetrische 'penseelpunt' |


### Invloed {#influence}

* `Bol` (3d) - De invloed wordt berekend aan de hand van de afstand van de vertex tot het midden van het penseel.
* `Cirkel` (2d) - De vertex wordt eerst op het vlak van het gebied geprojecteerd, en pas daarna wordt de afstand tot het midden van het penseel gemeten. Zo worden alpha's ook gesampled.
* `Cilinder` - De invloed wordt als een cilinder door het gebied heen geprojecteerd. Dit is hetzelfde als [Silhouet](#silhouette-1) hieronder aanzetten.
* `Kam` - De afname wordt dwars op de streek gemeten, zodat de curve de dwarsdoorsnede van de hele streek wordt. De knop `Sym` spiegelt het profiel dan over de streek: bewerk de ene kant en de andere volgt. Staat hij uit, dan loopt de curve van de linkerkant van de streek naar de rechterkant. Niet beschikbaar voor de afvlaktools.

### ![](/icons/silhouette.webp) Silhouet {#silhouette-1}
Standaard werkt een streek alleen op het oppervlak van het model binnen de penseelstraal. Met silhouet aan wordt de streek door het hele model heen geprojecteerd. Dat is erg handig bij het eerste opzetten van een model, of voor vormen waarvan de zijkanten loodrecht moeten blijven. Het heeft dezelfde projectieopties als het [Silhouet](#silhouette) van het tabblad Streek.


## ![](/icons/filter.webp) Filter {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Streek opbouwen {#accumulate-stroke}
Haalt de grens weg voor hoeveel materiaal je per streek kunt toevoegen of weghalen. De tool `Klei` heeft dit bijvoorbeeld aan staan, zodat het materiaal blijft opbouwen, terwijl het bij de tool `Kwast` uit staat: blijf je met dezelfde streek over hetzelfde stuk mesh gaan, dan stopt de streek met materiaal toevoegen.

### ![](/icons/culling.webp) Alleen voortuitkijkende vertex {#front-facing-vertex-only}
Deze optie negeert vertices die van je af gericht zijn.
Handig als je een deel van dunne geometrie wilt beschilderen zonder de andere kant te raken.
Het werkt ook bij sculpten, maar dan kun je wat artefacten krijgen.

### ![](/icons/eye_open.webp) Alleen zichtbare vertices {#visible-vertex-only}
Negeert vertices die, vanuit de camera gezien, achter andere oppervlakken verborgen liggen. Deze optie verschijnt bij vormstreken (lasso, rechthoek...) van de maskeer- en schildertools, en van de tools `Vlakkengroep` en `Verbergen`.

### ![](/icons/dynamic.webp) Dynamische topologie toestaan {#allow-dynamic-topology}
Deze optie is alleen beschikbaar als je mesh in de modus [Dynamische topologie](topology.md#dynamic-topology) staat. Zo kun je dynamische topologie per tool aan- of uitzetten.

### ![](/icons/connect.webp) Verbonden topologie {#connected-topology}
Sculpt alleen de vertices die verbonden zijn met het oppervlak dat je met de tool aanraakt. Met de tool `Verplaats` kun je zo bijvoorbeeld een onderdeel verplaatsen, ook als het een ander onderdeel doorsnijdt.
![](/videos/connected_topology.mp4)

### Bescherm gebied {#protect-area}
![](/images/filter_protect_area.webp) 

Deze opties voorkomen dat tools onder bepaalde omstandigheden delen van je mesh beïnvloeden. Elke optie kan op `Auto`, `Nee` of `Ja` staan, en het pijltje laat zien waar `Auto` op dat moment op uitkomt.

* `Verbergen` - Als delen van de mesh verborgen zijn met de verbergtool, bepaal je hier of ze beschermd worden. Op `Auto` worden verborgen vlakken beschermd, tenzij hun draadmodel zichtbaar is (zie de instellingen voor [Draadmodel](settings.md#wireframe)).
* `Masker` - Als delen van de mesh gemaskeerd zijn, bepaal je hier of ze beschermd worden. Op `Auto` worden gemaskeerde delen beschermd zolang het masker zichtbaar is in het menu [Shading](shading).
* `Vlakkengroep` - Bepaal of je een tool alleen binnen de eerst aangeraakte vlakkengroep kunt gebruiken. Op `Auto` volgt dit of vlakkengroepen zichtbaar zijn in het menu [Shading](shading).

Met de knop `(Alles)` bepaal je of deze beschermingen globaal zijn, gedeeld door alle tools, of per tool worden ingesteld.


### Gebied sampling {#area-sampling}
Sommige penselen of streekopties hebben een vlaknormaal en een vlakpositie op het oppervlak nodig om te werken.

Je bepaalt hoe dit gemiddelde vlak wordt berekend door het samplegebied in te stellen als verhouding van de straal van de tool.

Bij 100% telt elk punt binnen de selectiecirkel mee.

Bij 0% telt alleen de dichtstbijzijnde vertex of driehoek mee. Je kunt deze waarden koppelen voor zowel `Normaalradius` als `Positieradius`, of ontkoppelen en los van elkaar instellen.

### Gebieds-normaalfilter {#keep-sharp-edges}
Sluit punten uit waarvan de normaal te veel afwijkt van de normaal van het oppervlak.

Dit verandert hoe het vlak van het gebied wordt berekend (Gebied sampling), dus het is vooral nuttig voor klei- of afvlaktools, of als je een grotendeels vlak oppervlak wilt inkleuren zonder dat de kleur overloopt.

De hoeken `Min` en `Max` bepalen de overgang tussen uitgesloten en volledig beïnvloede punten, zoals het kleine gekleurde schijfje ernaast laat zien.

![](/videos/filter_keep_sharp_edges.mp4)

### Verval-normaalfilter {#falloff-normal-filter}
Net als het [Gebieds-normaalfilter](#keep-sharp-edges) sluit het punten uit waarvan de normaal te veel afwijkt van de normaal van het oppervlak, maar het werkt op de afname van het penseel in plaats van op de berekening van het vlak. Handig om plooien of bulten te beschilderen.


### Dieptemasking {#depth-masking}
![](/images/stroke_depthmask.webp)

Sluit punten uit die meer dan een bepaalde afstand boven of onder het berekende vlak liggen (Gebied sampling).

Zo kun je alleen op bobbelige delen schilderen, of alleen in holtes.

De grafiek toont een dwarsdoorsnede van het oppervlak: de horizontale lijn is waar het oppervlak ligt, en de cirkel stelt de afnamestraal van de verf voor, boven en onder het oppervlak. `Hoogte compensatie` is een percentage boven of onder het oppervlak waar de maskering begint. Met `Diepte-afname` aan kun je met `Bovenste gebied` en `Onderste gebied` de afname boven en onder dat punt schalen.

#### Voorbeeld: schilderen in holtes {#example-paint-in-cavities}
Om alleen in holtes te schilderen, zet je de hoogtecompensatie op -100% en stel je de schuif voor het bovenste gebied zo in dat die los van de horizontale lijn komt. De eerste tik bepaalt dan de 'nul'-diepte, en alleen wat dieper ligt, wordt beïnvloed.

![](/videos/stroke_depth_cavity.mp4)

#### Voorbeeld: schilderen op bulten {#example-paint-on-bumps}
Om alleen op hoge delen te schilderen, zet je de hoogtecompensatie op +90%, zodat de onderkant van de cirkel de horizontale lijn een klein stukje snijdt. Tik je bovenop een 'hoog' gebied, dan bepaalt dat de diepte: alles op die diepte, een klein beetje eronder en alles wat hoger ligt, wordt beschilderd. Diepe holtes worden overgeslagen.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Druk {#pressure}
![](/images/pressure_menu.webp) 

Bepaalt hoe de druk van je stylus of pen de penselen beïnvloedt.

### Gebruik globale instellingen {#use-global-settings}

Standaard staat `Gebruik globale instellingen` aan, zodat alle penselen dezelfde drukwaarden delen. Vink het uit om de huidige tool zijn eigen drukinstellingen te geven.

### ![](/icons/radius.webp) Radius {#pressure-radius}

Deze curve bepaalt hoe de penseelstraal reageert op druk. Standaard is het verband lineair: reageert je stylus soepel, dan voelt de verandering van de straal ook soepel aan. Veel stylussen reageren echter niet lineair, en dat kun je met deze curve compenseren. Heb je bijvoorbeeld het gevoel dat de straal bij hoge druk zijn maximum niet haalt, kies dan een curvepreset zoals 'out-pow3', met een bocht naar boven, zodat de straal eerder groter wordt.

Dit venster lijkt op de weergave van de afnamecurve: kies een preset door op het curvevenster te tikken, of teken je eigen curves met de modi `Catmull-Rom`, `B-spline` en `Afschuining`.

Wil je een constante straal, zet dit onderdeel dan uit.

### ![](/icons/intensity.webp) Intensiteit {#pressure-intensity}

Net als de straalcurve, maar dan voor de intensiteit. Wil je een constante intensiteit, zet dit onderdeel dan uit.

### Beperk druk tot 100% {#limit-pressure}

Zorgt ervoor dat de stylusdruk nooit boven 100% uitkomt. Dit is een globale instelling.

### Drukafvlakking {#pressure-smoothing}

Neemt het gemiddelde van de drukmetingen van de stylus voor vloeiendere resultaten.
