# ![](/icons/toolbox.webp) Gereedschappen {#tools}

![](/images/tools_menu.webp)

::: tip
Spring naar [Gereedschappen](#tools-1) voor een beschrijving van elk gereedschap.
:::

## Overzicht {#overview}

Je kiest gereedschappen in de `Gereedschapskist` aan de rechterkant en bedient ze met de gereedschapsknoppen aan de linkerkant. Extra instellingen vind je in het menu `Gereedschap`, in het menu rechtsboven.

Kwastgereedschappen hebben knoppen voor de grootte en de intensiteit. Selectiegereedschappen hebben knoppen voor verschillende manieren van selecteren. Onderaan de gereedschapsknoppen staan snelkoppelingen naar veelgebruikte bewerkingen (Gladstrijken, Masker, Verbergen, Vlakkengroep, Gizmo, Kleur, Alpha).

De gereedschappen van Nomad hebben een kleurcode in de gereedschapskist (zet `Gekleurde gereedschappen` uit in het menu [Interface](interface.md) voor gewone labels):

* <span class=brush>**Kwastgereedschappen**</span> (Klei, Kwast, Gladstrijken, Laag, Opblazen, LaagVerwijderen, Quad Remesher)
* <span class=move>**Verplaatsgereedschappen**</span> (Verplaats, Slepen, Elastisch, Nudge)
* <span class=mask>**Maskergereedschap**</span> (Masker)
* <span class=paint>**Schildergereedschappen**</span> (Verf, Vlekken)
* <span class=flatten>**Afvlakgereedschappen**</span> (Plat maken, Vlak, Polijsten)
* <span class=pinch>**Knijpgereedschappen**</span> (Plooi, Knijpen)
* <span class=stamp>**Stempelgereedschappen**</span> (Stempel, VDM)
* <span class=selection>**Selectiegereedschappen**</span>, waarbij je eerst een 2d-masker tekent waarna een bewerking volgt (Trimmen, Splitsen, Projecteren)
* <span class=creation>**Aanmaakgereedschappen**</span> (Buis, Draaibank, Invoegen)
* <span class=transform>**Transformatiegereedschappen**</span> (Transformeren, Gizmo, Rangschikken, Rooster)
* <span class=misc>**Overige gereedschappen**</span> (Vlakkengroep, Verbergen)
* <span class=view>**Weergavegereedschappen**</span> (Bekijken, Meten, Selecteren)



Veel van deze gereedschappen kun je aanpassen met ander kwastgedrag, druk, texturen enz. via het menu [Streek](stroke.md). 


### Kwastknoppen {#brush-controls}

De linkerwerkbalk heeft schuifregelaars voor de straal en de intensiteit, gevolgd door knoppen die per soort gereedschap verschillen; die worden hieronder uitgelegd.

![](/images/tool_left_panel.webp)

::: tip
Bij veel gereedschappen kan de intensiteitsregelaar boven de 100% uitkomen. Het is de moeite waard om ermee te experimenteren!
:::

### Submodus {#sub-mode}
De knop direct onder de intensiteitsregelaar is de knop `Aftrekken`. Het label en de functie ervan veranderen per gereedschap; als je erop drukt, krijg je een alternatief, meestal tegengesteld gedrag. Bij [Verf](#paint) bijvoorbeeld wordt het een gummodus, bij [Plooi](#crease) maak je opstaande randen in plaats van groeven, enz.

Standaard werkt hij als een 'plakknop': houd hem ingedrukt om hem tijdelijk te gebruiken, en zodra je loslaat gaat hij weer uit. Tik je erop, dan blijft de submodus aan staan.

### Snelkoppelingen {#shortcuts}
Onderaan de linkerwerkbalk staan snelkoppelingen naar [Gladstrijken](#smooth), [Masker](#mask), [Verbergen](#hide), [Vlakkengroep](#facegroup), [Gizmo](#gizmo), [Kleur](painting.md#pbr-sliders) en [Alpha](stroke.md#alpha). 

Standaard werken ze allemaal als plakknoppen: houd er een ingedrukt om hem tijdelijk te gebruiken, en zodra je loslaat gaat hij weer uit. Tik je erop, dan blijft die snelkoppeling aan staan.

### Selectieknoppen {#selection-controls}

De gereedschappen [Masker](#mask), [Verf](#paint), [Trimmen](#trim), [Splitsen](#split), [Projecteren](#project), [Vlakkengroep](#facegroup), [Verbergen](#hide) en [Selecteren](#select) gebruiken allemaal vergelijkbare knoppen om delen van de mesh te selecteren.

![](/images/tools_shape_selector_panel.webp)

Tik op de vormknop in de linkerwerkbalk (die toont de huidige vorm, standaard `Lasso`) om een pop-up met de vormen te openen. Bij de gereedschappen die ook met een kwast werken (Masker, Verf, Vlakkengroep, Verbergen) staan in dezelfde pop-up ook de streektypes.

* `Bekijken` - Geen vorm: het gereedschap doet niets bijzonders, net als de cameramodus.
* `Lasso` - Een vorm die je uit de vrije hand tekent
* `Polygoon` - Een gesloten vorm opgebouwd uit krommen en/of rechte lijnen. Zie [Vormen bewerken](#shape-editing) hieronder voor meer informatie.
* `Kromme` - (alleen Projecteren) - Een uit de vrije hand getekende kromme voor de projectie
* `Pad` - (alleen Projecteren) - Een kromme die je met punten vastlegt. Zie [Vormen bewerken](#shape-editing) hieronder voor meer informatie.
* `Lijn` - Sleep een lijn om een vlakke snede te bepalen. Standaard wordt de bewerking meteen op de mesh uitgevoerd; wil je dat niet, wijzig dan de optie `Bewerk` (houd het lijnicoon lang ingedrukt of veeg erover)
* `Band` - Een strook tussen twee evenwijdige hulplijnen, met een overloop erdwars. `Verlengen` houdt de volle waarde aan voorbij de verste hulplijn in plaats van te stoppen bij de band, `Omdraaien` wisselt de hulplijn waar de overloop begint.
* `Rechthoek` -  Sleep een diagonale lijn: die bepaalt de hoeken van een rechthoek. Houd lang ingedrukt of veeg om de optie `Bewerk` te tonen, `Vierkant` om een vierkant af te dwingen, en `Gecentreerd` om de eerste klik het midden van de rechthoek te laten zijn.
* `Ellips` - Sleep een diagonale lijn: die bepaalt de grootte van een ellips. Houd lang ingedrukt of veeg om de optie `Bewerk` te tonen, `Cirkel` om een cirkel af te dwingen, en `Gecentreerd` om de eerste klik het midden van de ellips te laten zijn.
* `Draaien` - Keert het vormmasker om, of de richting van het gereedschap Projecteren.

De meeste gereedschappen hebben een optie `Bewerk` die bepaalt wat er gebeurt als je klaar bent met het tekenen van de vorm:
* `Bewerken: uit` - De bewerking wordt uitgevoerd zodra je loslaat.
* `Bewerken: aan` - De vorm blijft bewerkbaar. Naast de vorm verschijnt een groene knop die de bewerking uitvoert. Zo kun je de vorm aanpassen en de weergave bijstellen; ben je klaar, druk dan op de groene knop.
* `Bewerken: vasthouden` - De bewerking wordt uitgevoerd bij het loslaten, tenzij je aan het einde van de streek blijft vasthouden om de vorm verder te bewerken.

### Vormen bewerken {#shape-editing}
Polygonen en krommen bewerk je op vergelijkbare wijze:

* Sleep eerst een lijn om 2 punten vast te leggen, en trek dan vanuit het midden van de lijn naar buiten om een polygoon of kromme te maken.
* Klik op een punt om te wisselen tussen vloeiend en scherp. 
* Klik en sleep op een stuk kromme of lijn om nieuwe punten te maken.
* Om een punt te verwijderen, sleep je het tegen zijn buurpunt aan tot het rood wordt.
* Het prullenbakicoon in de hoek van het polygoon- of padicoon verwijdert de vorm.

### Menu Instellingen {#settings-menu}

Veel gereedschappen hebben extra instellingen in het menu `Gereedschap`, in het menu rechtsboven. Bij gereedschappen zonder extra instellingen is het menu grijs.

![](/images/tools_settings_menu.webp)

## Gereedschappen {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Klei](#clay)       | ![](/icons/tool_brush.webp)   <br> [Kwast](#brush)     | ![](/icons/tool_move.webp)       <br> [Verplaats](#move)         | ![](/icons/tool_drag.webp)      <br> [Slepen](#drag)         | ![](/icons/tool_elastic.webp)   <br> [Elastisch](#elastic)   | ![](/icons/tool_smooth.webp)  <br> [Gladstrijken](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Masker](#mask)     | ![](/icons/tool_paint.webp)   <br> [Verf](#paint)      | ![](/icons/tool_smudge.webp)     <br> [Vlekken](#smudge)         | ![](/icons/tool_flatten.webp)   <br> [Plat maken](#flatten)  | ![](/icons/tool_planar.webp)    <br> [Vlak](#planar)         | ![](/icons/tool_polish.webp)  <br> [Polijsten](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Plooi](#crease)    | ![](/icons/tool_pinch.webp)   <br> [Knijpen](#pinch)   | ![](/icons/tool_trim.webp)       <br> [Trimmen](#trim)           | ![](/icons/tool_split.webp)     <br> [Splitsen](#split)      | ![](/icons/tool_project.webp)   <br> [Projecteren](#project) | ![](/icons/tool_layer.webp)   <br> [Laag](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Opblazen](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Nudge](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Stempel](#stamp)          | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [LaagVerwijderen](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Buis](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Draaibank](#lathe) | ![](/icons/tool_insert.webp)  <br> [Invoegen](#insert) | ![](/icons/tool_transform.webp)  <br> [Transformeren](#transform) | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Vlakkengroep](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Verbergen](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Meten](#measure)   | [Rangschikken](#arrange)                                 | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Selecteren](#select)   | ![](/icons/tool_lattice.webp)   <br> [Rooster](#lattice)     | ![](/icons/tool_view.webp)    <br> [Bekijken](#view)       |

------

### ![](/icons/tool_clay.webp) Klei {#clay}
Het gereedschap Klei is handig om je sculpt op te bouwen. `Aftrekken` haalt juist materiaal weg.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Kwast {#brush}
De standaardkwast. `Aftrekken` haalt materiaal weg.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Verplaats {#move}
Het gebied onder de kwast blijft aan de kwast plakken, waardoor je het elastisch kunt vervormen. De selectie blijft tijdens het verplaatsen behouden: beweeg je de kwast weg en daarna terug naar waar je begon, dan zie je geen vervorming.

De submodus is `Normaal`: die verplaatst het gebied onder de kwast langs de normaal van het oppervlak.

Deze kwast is geschikt voor zowel grote vervormingen als voorzichtige kleine aanpassingen.

#### Instellingen van Verplaats {#move-settings}

* `Straal (Achtergrond)` - Hoe ver je van de rand van een model mag beginnen en toch nog boetseert; handig als je aan het silhouet van een object werkt. Vink het uit om alleen te grijpen als je op het model begint.
* `Alleen zelfde-kant vertex` - Negeert vertices die de andere kant op wijzen dan de vervorming.
* `Richting` - Wordt gebruikt door de submodus `Normaal` en bepaalt of slepen het oppervlak in- of uitduwt:
    * `Automatisch` - Kiest voor jou een van de twee methodes hieronder, op basis van de hoek van de oppervlaknormaal.
    * `Normaal 3D` - Vergelijkt de positie van de aanwijzer op het scherm met de oppervlaknormaal zoals de camera die ziet.
    * `XY` - Gebruikt de schermpositie van de aanwijzer (omhoog/omlaag, links/rechts) om te bepalen of er geduwd of getrokken wordt.
    * `Drempel` - Met `Automatisch` de grenshoek die bepaalt welke methode wordt gebruikt.
* `Rolsnelheid` - Je kunt het gegrepen gebied verdraaien terwijl je het verplaatst: rol met twee vingers, draai je stylus om zijn as, of houd een functietoets (Alt, Ctrl, Shift of Cmd) ingedrukt terwijl je met de muis sleept. Er is een schuifregelaar voor vinger, stylus en muis; vink er een uit om die invoer uit te zetten.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Slepen {#drag}
Het gebied onder de kwast blijft aan de kwast plakken, waardoor je het elastisch kunt vervormen. Anders dan bij Verplaats wordt de selectie tijdens de streek steeds bijgewerkt, zodat je langere, slangachtige vormen kunt trekken, vooral met Dynamische topologie aan.

De submodus is `Normaal`: die verplaatst het gebied onder de kwast langs de normaal van het oppervlak.

Deze kwast is geschikt voor lossere, gebarende vormveranderingen.

#### Instellingen van Slepen {#drag-settings}

Slepen heeft dezelfde instellingen als [Verplaats](#move-settings): `Straal (Achtergrond)`, `Alleen zelfde-kant vertex`, `Richting` en `Rolsnelheid`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastisch {#elastic}
Grijp en trek aan het oppervlak zoals met [Verplaats](#move), maar met een elastische vervorming: in plaats van te stoppen bij de rand van de kwast neemt de trekkracht geleidelijk af met de afstand over het hele object, een beetje zoals uitrekkend rubber. De kwaststraal bepaalt hoe breed de trekkracht reikt.

De submodus is `Normaal`: die verplaatst het gebied onder de kwast langs de normaal van het oppervlak.

Deze kwast is geschikt voor grote, zachte proportiewijzigingen die vloeiend blijven.

#### Instellingen van Elastisch {#elastic-settings}

Elastisch heeft dezelfde instellingen als [Verplaats](#move-settings), behalve `Alleen zelfde-kant vertex`. `Straal (Achtergrond)` staat standaard uit.

### ![](/icons/tool_smooth.webp) Gladstrijken {#smooth}
Strijkt het gebied glad door de posities van de punten uit te middelen. Dit gereedschap hangt sterk af van de polygoondichtheid.
Heb je veel polygonen, dan is het gladstrijken dus minder effectief.

De submodus is `Ontspannen`: die strijkt alleen het draadmodel glad maar probeert de geometrische details te behouden.

#### Instellingen van Gladstrijken {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Vlakkengroep {#smooth-facegroup}

* `Ontspannen` - Strijkt de randen van vlakkengroepen glad. Gebruik een intensiteit boven 100% om randen snel glad te strijken. `Auto` strijkt alleen glad als de weergave van vlakkengroepen aan staat, `Nee` zet het uit, `Ja` zet het aan. 

##### Vertex {#vertex}
* `Volume behouden` - Strijkt glad zonder het oppervlak te laten krimpen, zodat je vormen niet leeglopen als je vaak gladstrijkt. In de tandwielknop ernaast staan de hoeveelheden `Krimpen` en `Opblazen` die hiervoor worden gebruikt.
* `Randen behouden` - Bij meshes met open randen, zoals een vlak, kunnen de hoeken worden weggestreken. Met deze optie blijven de vertices op de rand van de mesh op hun plek.
* `Stabiel gladstrijken` - Probeert het gladstrijken onafhankelijk van de topologie te maken. Dit werkt het best bij een wisselende topologiedichtheid en een hoge intensiteit.
* `Ontspannen` - Hetzelfde als de alternatieve modus Ontspannen in de linkerwerkbalk.

##### Schilderen {#painting}
* `Schermgladstrijken` - Gebruik deze optie voor gladstrijken dat niet van de topologie afhangt, zelfs bij hoge polygoonaantallen. `Auto`, `Nee` of `Ja`.
* `Schermsamples` - De kwaliteit van het gladstrijken: hogere waarden geven een gladder resultaat, maar zijn trager.

::: tip
Bij een hogere polygoondichtheid moet je de intensiteit soms boven 100% zetten. Heel hoge waarden (300%, 500%) werken ook prima als boetseergereedschap: gebieden onder de kwast worden snel plat en glad, alsof je met een hamer op klei slaat!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Masker {#mask}
Met dit gereedschap maskeer je vertices. Gemaskeerde vertices zijn beschermd tegen boetseren en schilderen. 

De submodus is `Ontmaskeren`: die wist het masker waar het geschilderd is.

Net als selecties in 2d-tekenprogramma's kun je maskers schilderen met een kwast of maken met vormselecties (`Lasso`, `Rechthoek`, `Band`...), en ze vervagen of verscherpen. Kies de kwast of de vorm in de streek-pop-up van de linkerwerkbalk, zie [Selectieknoppen](#selection-controls).

Anders dan in 2d-tekenprogramma's kun je maskers ook maken via vlakkengroepen, en kun je met maskers nieuwe geometrie maken door te extruderen of te extraheren. 

![](/videos/tool_mask1.mp4)

 Bovenaan de viewport verschijnt een werkbalk met extra knoppen. 

![](/images/tool_mask_toolbar.webp)

Tik op de titel van de balk om hem in of uit te klappen, of tik op de pijl rechtsboven om hem naar de boven- of onderkant van het scherm te verplaatsen.

| Actie                                              | Beschrijving                                                                               |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Alles wissen       | Wist het masker op alle objecten. Zijn er ook andere objecten gemaskeerd, dan wist een extra knop `Wissen` alleen de geselecteerde objecten |
| ![](/icons/invert.webp)        Inverteren         | Keert het masker om                                                                        |
| ![](/icons/sharpen.webp)       Verscherpen        | Verscherpt de rand van het masker                                                          |
| ![](/icons/blur.webp)          Vervagen           | Vervaagt de rand van het masker                                                            |
| ![](/icons/outline.webp)       Rand               | Maskeert de open rand van de mesh, zoals de rand van een vlak of de rand van een gat       |
| ![](/icons/blur.webp)          Vervagen ->        | Sleep naar rechts om het masker te vervagen, naar links om het te verscherpen              |
| ![](/icons/circle_plus.webp)   Uitbreiden ->      | Sleep naar rechts om het gemaskeerde gebied te vergroten, naar links om het te verkleinen  |
| ![](/icons/intensity.webp)     Versterken ->      | Sleep naar rechts om het masker te versterken, naar links om het te verdunnen, zonder de vorm te veranderen |
| ![](/icons/dig.webp)           Holte ->           | Bouwt het masker opnieuw op uit de kromming van het oppervlak: sleep naar rechts zodat alleen de holtes beschilderbaar blijven, naar links zodat alleen de bobbels dat blijven |
| ![](/icons/culling.webp)       Voorzijde          | Schakelt in dat alleen vertices die naar voren wijzen worden gemaskeerd                    |
| ![](/icons/eye_open.webp)      Zichtbaar          | Schakelt bij vormen in dat vertices die achter andere oppervlakken verborgen zitten worden genegeerd |
|                                 Converteer         | Zet het masker om in een vlakkengroep                                                      |
| ![](/icons/group_to_mask.webp) Bij tikken (vlakkengroep) | Als dit aan staat, worden vlakkengroepen getoond en maskeer je een vlakkengroep door erop te tikken |
|                                 Bij tikken (masker) | Als dit aan staat, vul je een 'eiland' van gemaskeerde of niet-gemaskeerde polygonen door erop te tikken. |
| ![](/icons/connect.webp)       Verbonden          | Als dit aan staat, werken maskerstreken alleen op verbonden topologie.                     |

##### Snelle gebaren voor het masker {#mask-quick-gesture}
Terwijl je de snelkoppeling voor het masker in de linkerwerkbalk ingedrukt houdt, kun je gebaren gebruiken zoals in ZBrush:
| Actie       | Gebaar (snelkoppeling linksonder ingedrukt) |
| :---------: | :-----------------------------------------: |
| Inverteren  | Tik op de achtergrond                       |
| Wissen      | Sleep over de achtergrond                   |
| Vervagen    | Tik op een gemaskeerd gebied                |
| Verscherpen | Tik op een niet-gemaskeerd gebied           |


#### Instellingen van Masker {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

De instellingen van Masker dienen vooral om geometrie te maken uit het masker. Met de tabbladen bovenaan kies je de bewerking: [Extraheer](#extract), [Splitsen](#split-mask) of [Graveren](#carve). De opties eronder veranderen per bewerking.

* `Voorbeeld` - Laat zien hoe de nieuwe geometrie eruit zal zien terwijl je de instellingen aanpast.
* `X-Ray` - Welke objecten tijdens het voorbeeld in x-ray worden getekend: `Geen`, `Ongekozen`, `Geselecteerd` of `Alles`.

##### Extraheer {#extract}
* `Extraheer` - Maakt van de geëxtraheerde geometrie een nieuw object.
* `Sluitingsactie` - Hoe de geëxtraheerde vorm wordt afgesloten. `Geen` kopieert de gemaskeerde polygonen naar een nieuwe vorm en laat die open. `Vullen` doet hetzelfde, maar vult het gat aan de achterkant en strijkt het glad (niet gebruiken op vlakke oppervlakken). `Schil` sluit de vorm af met de waarde van `Hoogte`; dit is de standaardinstelling.

::: tip

Als het voorbeeld met x-ray aan staat, kan een klik op de knop Extraheer in het begin verwarrend zijn. Omdat het menu actief is, probeert Nomad een extractie te tonen op je nieuwe vorm, en toont het oorspronkelijke oppervlak in x-ray. Maar omdat er geen masker op het nieuwe oppervlak staat, kan het geen voorbeeld tonen en waarschuwt Nomad dat er niets te extraheren is. 

Dat is normaal: sluit het menu met de maskerinstellingen om de nieuwe vorm en het origineel te zien, en selecteer het oorspronkelijke oppervlak opnieuw als je het masker wilt wissen of nieuwe maskers wilt tekenen.
:::

##### Splitsen {#split-mask}
* `Splitsen` - Haalt zowel het gemaskeerde ALS het niet-gemaskeerde gebied eruit als nieuwe vormen. 
* `Sluitingsactie` (gemaskeerd) - Hoe het gemaskeerde deel wordt afgesloten, met dezelfde keuzes `Geen`, `Vullen` en `Schil` als bij Extraheer.
* `Sluitingsactie` (niet gemaskeerd) - Hoe het niet-gemaskeerde deel wordt afgesloten, met dezelfde keuzes.

##### Graveren {#carve}
* `Graveren` - Werkt alsof je het oppervlak over een diepte van `Hoogte` hebt weggesneden, zoals je een stuk sinaasappelschil uitsnijdt. De `Hoogte` kan niet 0 zijn.

##### Hoogte {#thickness}
* `Hoogte` - De hoogte van de geëxtraheerde vorm. Met de plus/min-knop wissel je tussen extruderen naar buiten, naar binnen of naar beide kanten. 

##### Gladheid {#smoothness}
Als dit aan staat, wordt de geëxtraheerde vorm gladgestreken; dat werkt beter bij hogere polygoonaantallen. 
* `Alle` / `Alleen grenzen` - Strijkt de hele vorm glad, of alleen de randen, zodat de vorm van het bovenvlak onaangetast blijft.
* `Iteraties` - Met `Alle` de hoeveelheid gladstrijken. Hoge waarden geven heel gladde, ronde randen, maar wijken dan af van de vorm van het masker.
* `Wand` - Met `Alleen grenzen` de hoeveelheid gladstrijken op de wanden. De bijbehorende knop wisselt tussen Ontspannen, dat de scherpe hoeken behoudt, en Gladstrijken, dat ze ook afrondt.
* `Binnenkant` - Met `Alleen grenzen` hoeveel het bovenvlak wordt gelijkgetrokken. De bijbehorende knop wisselt tussen Ontspannen, dat de geboetseerde details behoudt en alleen de extrusierichting gelijktrekt (zodat details geen pieken meer veroorzaken), en Gladstrijken, dat het oppervlak zelf gladstrijkt.

##### Zijden {#edge-loop-side}
* `Recht` - Gewone wanden aan de zijkanten van de geëxtraheerde vorm.
* `Afschuining` - (alleen Extraheer met `Schil`) Een schuine rand aan de voorkant. `Afschuining` stelt de breedte in, in % van `Hoogte` of in wereldeenheden (de knop ernaast wisselt), `Afschuiningverdelingen` verdeelt hem (standaard `Auto`), en met een curve geef je het profiel vorm.
* `Profiel` - Geeft de wanden vorm met een profielcurve, met een `Breedte` in % van `Hoogte` of in wereldeenheden.
* `Masker` - De hoogte volgt het masker: vervaagde delen van het masker krijgen een lagere hoogte, wat zachte vormen met wisselende hoogte mogelijk maakt.
* `Wandverdelingen` - Het aantal edge loops op de zijkanten. Met `Auto` kiest Nomad het aantal verdelingen dat vierkante polygonen oplevert die passen bij de polygonen van het gemaskeerde gebied.



### ![](/icons/tool_maskSelector.webp) Selectiemasker {#selection-mask}
Het gereedschap Selectiemasker (SelMask) maakt nu deel uit van het [gereedschap Masker](#mask). Om met vormen te maskeren in plaats van met een kwaststreek, kies je een vorm (`Lasso`, `Polygoon`, `Rechthoek`...) in de streek-pop-up van het gereedschap Masker, zie [Selectieknoppen](#selection-controls).

De submodus `Ontmaskeren` werkt ook met vormen en wist het masker binnen de vorm.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Verf {#paint}
Brengt kleur en materiaaleigenschappen aan. Meer over materialen lees je in het onderdeel [Schilderen](painting.md).

De submodus is `Wissen`: die haalt verf weg.

Naast kwaststreken kan Verf ook vormen vullen (`Lasso`, `Rechthoek`, `Band`...), zie [Selectieknoppen](#selection-controls).

#### Instellingen van Verf {#paint-settings}
* `Laagfiltering` - Werkt als de alfavergrendeling van een laag in Photoshop of Procreate. Schilder je op een laag en staat dit aan, dan kun je alleen aanpassen waar al verf zit; onbeschilderde gebieden zijn beschermd. Alleen beschikbaar als er een laag is geselecteerd.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Vlekken {#smudge}
Veegt kleur en materiaaleigenschappen uit. Het instellingenmenu van Vlekken bevat een schuifregelaar `Kwaliteit`: lagere waarden geven snellere streken.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Plat maken {#flatten}
Maakt het gebied plat door de punten te projecteren op het gemiddelde vlak.

De submodus is `Vullen`: die legt een vlak vast op het hoogste punt en trekt de punten eerder omhoog.

#### Instellingen van Plat maken {#flatten-settings}

* `Vastzetting richting vlak` - Gebruikt de richting van het vlak die bij de eerste klik is berekend. Staat standaard uit.
* `Vastzetting oorsprong vlak`- Gebruikt de eerste klik als middelpunt van het vlak. Staat standaard uit en kan alleen samen met `Vastzetting richting vlak` worden aangezet.

Staat een van beide of staan ze allebei uit, dan kun je het afvlakken geleidelijk dieper maken of de hoek van het vlak veranderen met lange streken over verschillende diepten en krommingen. Samen met de gebied-sampling-opties van het kwastmenu geeft dit heel nauwkeurige controle.

::: tip
Werk je in gebieden met veel kromming, bijvoorbeeld als je de wangen wilt afvlakken maar het gereedschap steeds de zijkanten van de neus raakt, maak dan een masker om de delen te beschermen die het afvlakgereedschap niet mag raken.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Vlak {#planar}
Maakt punten vlak door ze op het gemiddelde vlak te projecteren, maar met minder opbouw dan Plat maken. Dit geeft strakkere oppervlakken met harde randen. Snelle streken duwen en trekken meer aan het oppervlak; langzamere streken die in al vlakke gebieden beginnen en naar buiten werken, houden het vlak beter aan.

De submodus is `Vullen`: die legt een vlak vast op het hoogste punt en trekt de punten eerder omhoog.

Vlak is eigenlijk hetzelfde gereedschap als `Plat maken`, maar met `Vastzetting richting vlak` aan. Het geeft daardoor stabielere oppervlakken met harde randen, terwijl Plat maken boetseerachtiger is en zich leent voor half vlakke gebieden.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Polijsten {#polish}
Nog een lid van de familie Plat maken, ingesteld om oppervlakken op te poetsen tot strakke vlakken. Het is hetzelfde gereedschap als `Plat maken`, met andere standaardwaarden voor [Streek](stroke.md): `Spoor`, `Gebieds-normaalfilter` en `Dieptemasking` staan aan.

De submodus is `Vullen`, net als bij Plat maken.

Polijsten heeft dezelfde instellingen als [Plat maken](#flatten-settings): `Vastzetting richting vlak` en `Vastzetting oorsprong vlak`.

### ![](/icons/tool_crease.webp) Plooi {#crease}
Plooigereedschappen zijn handig om kleine sneden of deuken te boetseren.

De submodus is `Inverteren`: die maakt een opstaande plooi.

#### Instellingen van Plooi {#crease-settings}

* `Knijp kracht` - Hoeveel vertices zijwaarts naar de kwast worden getrokken. Staat knijpen op 1 en offset op 0, dan verandert de diepte van het oppervlak niet, alleen de topologie: randen worden naar de streek getrokken.
* `Offsetfactor` - Hoeveel vertices in de diepte worden geduwd of getrokken. Staat knijpen op 0 en offset op 1, dan ontstaan diepe plooien of opstaande deuken, maar die zien er rafelig uit omdat er niet genoeg geometrie naar de plooi wordt getrokken om de zijkanten of de bodem ervan nauwkeurig te vormen.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Knijpen {#pinch}
Met dit gereedschap kun je randen scherper maken.

De submodus is `Inverteren`: die duwt vertices uit elkaar.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trimmen {#trim}
Het gereedschap Trimmen haalt een stuk van je mesh weg en biedt opties voor wat er met het achtergebleven gat gebeurt. Je bepaalt de snede met de [Selectieknoppen](#selection-controls).

De submodus is `Draaien`: die keert de vorm om, zodat juist de andere kant wordt verwijderd.

::: tip
Omdat dit gereedschap vanuit de camera projecteert, krijg je een waarschuwing als de camera in perspectiefmodus staat.

In orthografische modus loopt de snede door de mesh evenwijdig aan de weergave, wat meestal is wat je verwacht. Met een perspectiefcamera ziet de snede er aan de achterkant van het object anders uit dan aan de voorkant.
:::

#### Instellingen van Trimmen {#trim-settings}

De instellingen staan gegroepeerd onder `Gat vullen`:

* `Penseelschilderen` - Staat schilderen aan in het menu Schilderen, dan wordt het opgevulde gebied gevuld met de huidige kleur.
* `Boolean` - Vult het gat van de snede met een gebied van quads. Het opgevulde gebied is vlak.
* `Legacy` - Vult het gat van de snede met driehoeken. Het opgevulde gebied is vlak.
* `Vul` - Vult het gat met driehoeken. Het opgevulde gebied is gebogen, zoals het vlies van een zeepbel.
* `Geen` - Vult het gat niet.

Met `Boolean` bevat het onderdeel `Detail`:

* `Vorm` - De globale grootte van de quads en driehoeken aan de kant van de vorm.
* `Gaten` - De globale grootte van de driehoeken of polygonen op het opgevulde gat. De koppelknop naast `Detail` houdt deze waarde gelijk aan `Vorm`; ontkoppel hem om hem apart in te stellen.
* `Topologie behouden` - Strijkt de rand van de snede niet glad en vereenvoudigt hem niet, zodat de oorspronkelijke topologie van de mesh bij gemaskeerde en verborgen vlakken behouden blijft.

Met `Legacy`:

* `Detail` - De globale grootte van de driehoeken van de snede.
* `Gladmaken van gaten` - Hoeveel de driehoeken in het opgevulde gebied worden ontspannen.
* `Drempel epsilon` - Een waarde die je kunt bijstellen om het oude algoritme voor het vullen van gaten te verbeteren.

Met `Vul`:

* `Detail` - De globale grootte van de driehoeken van de snede.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Splitsen {#split}
Lijkt op het gereedschap [Trimmen](#trim), maar waar Trimmen de selectie weggooit, bewaart Splitsen de selectie als nieuw object.

De submodus is `Delen`: elk stuk wordt een eigen object, zodat overlappende vormen (bijvoorbeeld met symmetrie) in losse delen worden gesneden in plaats van tot één geheel te worden samengevoegd.

#### Instellingen van Splitsen {#split-settings}

Splitsen heeft dezelfde instellingen onder `Gat vullen` als [Trimmen](#trim-settings): `Penseelschilderen`, de methodes `Boolean`, `Legacy`, `Vul` en `Geen`, en hun opties voor `Detail`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projecteren {#project}
Het gereedschap Projecteren lijkt op [Trimmen](#trim), maar verwijdert of maakt geen geometrie: het verplaatst alleen vertices zodat ze de selectie volgen.

![](/videos/tool_project.mp4)

::: tip
Gebruik je Projecteren op een laag, dan kun je met de schuifregelaar van de laag mengen tussen de oorspronkelijke en de geprojecteerde vorm.
:::

### ![](/icons/tool_layer.webp) Laag {#layer}
Verhoogt het oppervlak, maar met een maximale hoogte.

Houd je de stylus op het scherm en blijf je over een gebied strijken, dan stijgt Laag tot een bepaalde hoogte en niet verder, terwijl andere gereedschappen steeds meer hoogte opbouwen.

Let op: standaard geldt de limiet alleen per streek! Begin je een nieuwe streek, dan bouwt die verder op vanaf de nieuwe hoogte van het oppervlak.

Wil je een vaste maximale hoogte over meerdere streken, gebruik het gereedschap Laag dan samen met het [Lagen](layers.md)-systeem van Nomad.

Maak een laag aan en gebruik dit gereedschap. De maximale hoogte komt nu van de laag, zodat je veel streken kunt zetten en de hoogte altijd gelijk blijft.

`Aftrekken` gebruikt een minimale diepte, waarmee je groeven maakt.

#### Instellingen van Laag {#layer-settings}

* `Gebruik laaggegevens` - Als dit aan staat en er een laag is geselecteerd, bepalen de gegevens van de laag de maximale hoogte. Een waarschuwing herinnert je eraan als er geen laag is geselecteerd.
* `Opblazen`- Past de richting aan waarin Laag werkt, voor een gladder resultaat.
* `Ontspannen (Normaal)` - Met `Opblazen` aan, de hoeveelheid gladstrijken die op de normalen wordt toegepast.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Opblazen {#inflate}
Verplaatst de vertices langs hun eigen normaal. `Aftrekken` verplaatst ze langs hun omgekeerde normaal.

#### Instellingen van Opblazen {#inflate-setings}
* `Ontspannen (Normaal)` - De hoeveelheid gladstrijken die op de normalen wordt toegepast.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge {#nudge}
Verplaatst of 'veegt' punten in de richting van de streek.

De submodus is `Vouw`: die duwt een plooi van materiaal voor de streek uit, met een bult voor de kwast en een dal erachter.

#### Instellingen van Nudge {#nudge-settings}
* `Gladstrijken` - Hoeveel het gebied onder de kwast wordt gladgestreken terwijl je het verschuift, zodat het uitgeveegde oppervlak netjes blijft.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stempel {#stamp}

Klik en sleep om een gebied van je sculpt omhoog te brengen in de vorm van de geselecteerde alpha.

Dit is gewoon het [gereedschap Kwast](#brush) met het streektype `Vergrendelen + straal`. 

`Aftrekken` drukt de stempel het oppervlak in in plaats van hem eruit te trekken.

::: tip
Stempel werkt meestal het best op geometrie met een hoge resolutie. Zoek online naar 'wrinkles alpha', 'pores alpha', 'scales alpha' enz.: met zulke alphatexturen en Stempel voeg je prachtig organisch detail toe aan een personage.

De twee streekmodi zijn voor verschillende dingen handig. 

* `Vergrendelen + straal` heeft een vaste *hoogte*; slepen past de breedte en rotatie van de stempel aan. Goed voor huidtexturen die overal even diep/hoog moeten zijn, maar met verschillende rotaties en schalen om herhalende patronen te verbergen.
* `Vergrendelen + intensiteit` heeft een vaste *breedte*; slepen past de rotatie en hoogte van de stempel aan. Goed voor klinknagels, die allemaal even groot moeten zijn, maar met verschillende rotaties en hoogtes. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Stempelt een vector displacement map (VDM). Een alpha kan het oppervlak alleen omhoog of omlaag duwen, maar een VDM bevat een volledige 3d-vorm en kan dus ook overhangende vormen stempelen, zoals oren, hoorns of omkrullende bladeren. Het werkt zoals [Stempel](#stamp), met dezelfde streekmodi `Vergrendelen + straal` en `Vergrendelen + intensiteit`.

`Aftrekken` (`Inverteren`) keert de diepte van de stempel om, zodat hij als een mal in het oppervlak wordt gedrukt.

De VDM zelf kies je in het menu [Alpha](stroke.md#alpha), dat ook een schuifregelaar `Hoogte` heeft om alleen de hoogte van de stempel te schalen, zonder de zijwaartse verplaatsing te veranderen.

Met de knop `Creëer` in de linkerwerkbalk maak je je eigen stempels:

* `Nieuwe VDM...` - Voegt een vlak toe dat klaar is om een VDM op te boetseren. Boetseer je vorm erop en bak hem dan met `Topologie -> Bakken -> VDM`: Nomad voegt de nieuwe stempel toe aan de VDM-bibliotheek en selecteert hem.
* `VDM vastleggen` - (Experimenteel) Sleep over het oppervlak van een model om dat gebied te grijpen en er een VDM-stempel van te maken. `Tolerantie` vlakt de rand van de opname geleidelijk af.

::: tip
Gebruik geen DynTopo als je op een VDM-vlak boetseert: dat beschadigt de UV's van het vlak en vervormt de stempel. Blijf met je sculpt ook uit de buurt van de rand van het vlak, anders krijgt de stempel een harde rand.
:::


### ![](/icons/tool_clearLayer.webp) Laag verwijderen {#delete-layer}
Met dit gereedschap zet je lagen plaatselijk terug. Je hebt een actieve laag nodig, anders gebeurt er niets. Het wist de geboetseerde gegevens van de laag, en ook de verf als schilderen aan staat.

De submodus is `Inverteren`: die versterkt de laag een beetje in plaats van hem te wissen.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Buis {#tube}
Maak een buis door een kromme te tekenen. 
![](/images/tool_tube_new.webp)

Is de buis gemaakt, dan kun je het pad in de 3d-ruimte bewerken met knoppen die lijken op die van [Vormen bewerken](#shape-editing) en de gewone krommebewerking. 

![](/videos/tool_tube.mp4)

#### Linkerwerkbalk van Buis {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

De linkerwerkbalk heeft de volgende opties:

* `Synchronisatie` - Is de huidige buis een instantie en verschillen de onderliggende nodes van de buis tussen de instanties, dan worden ze hiermee opnieuw gesynchroniseerd.
* `Snap` - Als dit aan staat, klikken de modi kromme en pad tijdens het tekenen vast op andere objecten. Staat het uit, dan klikt alleen het eerste punt vast en wordt de rest van de buis op die diepte getekend.
* `Offset` - Stelt de diepte van het vastklikken in: bij 0% klikt het midden van de doorsnede van de buis vast op het oppervlak, positieve waarden tillen de buis van het oppervlak, negatieve waarden laten hem zakken. 100% is gelijk aan de straal van de buis.
* `Bekijken` - Geen tekenmodus, zodat je de camera vrij kunt bewegen.
* `Kromme` - Schets een buis uit de vrije hand. Er hoort een klein uitklapmenu bij:
    * `Bewerk` - Wat er gebeurt als je de streek afmaakt, zie [Selectieknoppen](#selection-controls): de buis meteen maken, de kromme bewerkbaar houden met een groene bevestigingscirkel ernaast, of aan het einde van de streek blijven `Vasthouden` om verder te bewerken.
    * `Gesloten` - Maakt van de buis een lus.
    * `Blijven tekenen` - Blijf na het bevestigen van een buis in het gereedschap om de volgende te tekenen.
    * `Nauwkeurigheid` - Hoeveel punten er worden gebruikt om het getekende pad om te zetten in een buis. 0% gebruikt zo weinig mogelijk punten, maar mist kleine veranderingen in de kromming. 100% is heel nauwkeurig en gebruikt veel punten.
* `Pad` - Maak een buis door te klikken om de punten van de kromme te plaatsen. Tik op de groene cirkel om het pad te bevestigen. Er hoort een klein uitklapmenu bij:
    * `B-spline` - Een andere manier om krommen te tekenen, waarbij de punten meestal niet op de kromme zelf liggen, maar die gladdere resultaten kan geven dan de standaardmethode.
    * `Gesloten` - Maakt van de buis een lus.
    * `Scherm` - Als dit aan staat, zit het pad 'vastgeprikt' op het scherm: je kunt de weergave en het object bewegen terwijl het pad op zijn plek blijft. Staat het uit, dan hoort het pad bij de 3d-scène en beweegt het mee met de camera en de objecten.
* `Doorsnede` - De kromme wordt een ring rond de vorm, door de twee punten gesneden in de richting waaruit je keek.

##### Bovenste werkbalk van Buis {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Als er een buis is geselecteerd, verschijnt bovenaan de viewport een werkbalk met extra knoppen. Klik op de titel van de werkbalk om hem in of uit te klappen, en op de pijl rechtsboven om hem naar de boven- of onderkant van de viewport te verplaatsen.

* `Voltooien` - Bakt de buis om in gewone polygonen, zodat je erop kunt boetseren.
* `Bewerk` - Toont de punten van de kromme, zodat je ze kunt verplaatsen.
* `Spiegel` - Voegt een spiegelrepeater toe als ouder van deze kromme.
* `Snap` - Klikt de punten van de kromme vast op oppervlakken in de buurt.
* `Gesloten` - Verbindt het begin en het einde van de kromme tot een lus.
* `B-spline` - Wisselt tussen Catmull-Rom- en B-spline-interpolatie.
* `Deksel` - Wisselt tussen een deksel aan beide uiteinden van de buis, alleen aan het begin of het einde, of geen deksels.
* `Gat` - Geeft de buis een wanddikte, zodat het een pijp wordt. Wisselt tussen een gat aan beide uiteinden, alleen aan het einde, of geen gaten. 
* `Straal` - Wisselt tussen een gelijke straal, een straal aan het begin en het einde, of een straal per punt van de kromme. Je bewerkt ze met oranje handgrepen op de kromme.
* `Winding` - Wisselt tussen geen winding, een gelijke winding, een winding aan het begin en het einde, of een winding per punt van de kromme. Je bewerkt ze met roze handgrepen op de kromme.
* `Profiel` - Wisselt tussen geen profiel (dus een rond profiel), een gelijk profiel, een profiel aan het begin en het einde, of een profiel per punt.
* `Profiel bewerken` - Toont een profieleditor. Die werkt zoals [Vormen bewerken](#shape-editing), kan profielpresets opslaan en laden, en heeft een schakelaar om het profiel in de 3d-ruimte te bewerken.
* `Spiraal` - Toont een menu om de buis een spiraalvormige winding te geven. Dit menu heeft de opties `Windingshoek`, `Offset`, `Schaal` en `Hoek offset`.
* `X-verdelingen` - Het aantal verdelingen rond de buis; met 4 verdelingen krijg je bijvoorbeeld een vierkante buis. 
* `Constante dichtheid` - Als dit aan staat, blijven de polygonen vierkant. Staat het uit, dan kun je `Y-verdelingen` instellen over de lengte van de buis.
* `...` - Het instellingenmenu van Buis.

#### Schakelaar voor het verwijderen van punten {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Onder de werkbalk staat een schakelaar voor het verwijderen van punten van de kromme. Sleep je een punt dicht bij een ander punt, dan wordt het rood: laat je dan los, dan wordt het punt verwijderd. Doe je kleine aanpassingen en wil je geen punten verwijderen, dan zet je dat gedrag met deze knop uit.



#### Instellingen van Buis {#tube-settings}
* `Primitief` - Knoppen om UV's aan of uit te zetten, of om de buis te voltooien.
* `Naderhand onderverdelen` - Een snelkoppeling om het multiresolutieniveau in te stellen voordat je voltooit.
* `Lineaire subdivisie` - Een snelkoppeling om het niveau van lineaire subdivisie in te stellen voordat je voltooit. 
* `Verdeling X` - Hetzelfde als X-verdelingen in de werkbalk.
* `Verdeling Y` - Hetzelfde als Y-verdelingen in de werkbalk.
* `Kromme (Repeater)` - Zet de buis om in een [Kromme-repeater](scene.md#curve).

::: tip
Met 4 verdelingen en Naderhand onderverdelen op 3 krijg je gladde buizen met ronde uiteinden, ideaal voor wormen, slangen en lichaamsdelen.
:::


### ![](/icons/tool_lathe.webp) Draaibank {#lathe}
Maak een omwentelingsoppervlak door een kromme te tekenen.

Dit gereedschap is ideaal voor vormen als vazen en wijnglazen.

![](/videos/tool_lathe.mp4)

#### Linkerwerkbalk van Draaibank {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

De linkerwerkbalk heeft de volgende opties:

* `Synchronisatie` - Is de huidige draaibankvorm een instantie en verschillen de onderliggende nodes ervan tussen de instanties, dan worden ze hiermee opnieuw gesynchroniseerd.
* `Vast` - Als dit aan staat, ligt het midden van de draaibankvorm vast en wordt het op het scherm getoond. Deze middellijn heeft bewerkpunten die je kunt aanpassen. Staat het uit, dan past het midden zich steeds aan het begin en het einde van de getekende kromme aan.
* `Bekijken` - Geen tekenmodus, zodat je de camera vrij kunt bewegen.
* `Kromme` - Teken het profiel van de draaibankvorm in één streek. Er hoort een klein uitklapmenu bij:
    * `Bewerk` - Wat er gebeurt als je de stylus optilt, zie [Selectieknoppen](#selection-controls): de vorm meteen maken, de kromme bewerkbaar houden met een groene cirkel ernaast om de vorm te maken, of aan het einde van de streek blijven `Vasthouden` om verder te bewerken.
    * `Gesloten` - Verbindt het begin en het einde van de kromme tot een lus.
    * `Blijven tekenen` - Blijf na het bevestigen van een draaibankvorm in het gereedschap om de volgende te tekenen.
    * `Nauwkeurigheid` - Hoeveel punten er worden gebruikt om het getekende pad om te zetten in een buis. 0% gebruikt zo weinig mogelijk punten, maar mist kleine veranderingen in de kromming. 100% is heel nauwkeurig en gebruikt veel punten.
* `Pad` - Maak een draaibankvorm door te klikken om de punten van de kromme te plaatsen. Tik op de groene cirkel om het pad te bevestigen. Er hoort een klein uitklapmenu bij:
    * `B-spline` - Een andere manier om krommen te tekenen, waarbij de punten meestal niet op de kromme zelf liggen, maar die gladdere resultaten kan geven dan de standaardmethode.
    * `Gesloten` - Maakt van de buis een lus.
    * `Scherm` - Als dit aan staat, zit het pad 'vastgeprikt' op het scherm: je kunt de weergave en het object bewegen terwijl het pad op zijn plek blijft. Staat het uit, dan hoort het pad bij de 3d-scène en beweegt het mee met de camera en de objecten.

#### Bovenste werkbalk van Draaibank {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Als er een draaibankvorm is geselecteerd, verschijnt bovenaan de viewport een werkbalk met extra knoppen. Klik op de titel van de werkbalk om hem in of uit te klappen, en op de pijl rechtsboven om hem naar de boven- of onderkant van de viewport te verplaatsen.

* `Voltooien` - Bakt de draaibankvorm om in gewone polygonen, zodat je erop kunt boetseren.
* `Bewerk` - Toont de punten van de kromme, zodat je ze kunt verplaatsen.
* `Spiegel` - Voegt een spiegelrepeater toe als ouder van deze draaibankvorm.
* `Snap` - Klikt de punten van de kromme vast op oppervlakken in de buurt.
* `Stabiel` - Als dit aan staat, is het profiel van de kromme gekoppeld aan de middellijn van de draaibankvorm. Staat het uit, dan kun je de middellijn bewerken zonder dat de kromme meebeweegt, wat complexere vormen mogelijk maakt.
* `Focus` - Draait de weergave zodat je het profiel van de kromme precies plat voor de camera ziet.
* `Gesloten` - Verbindt het begin en het einde van de kromme tot een lus.
* `Deksel` - Als Gesloten uit staat: wisselt tussen een deksel aan beide uiteinden, alleen aan het begin of het einde, of geen deksels.
* `Gat` - Geeft de draaibankvorm een wanddikte, zodat het een pijp wordt. Wisselt tussen een gat aan beide uiteinden, alleen aan het einde, of geen gaten. 
* `B-spline` - Wisselt tussen Catmull-Rom- en B-spline-interpolatie.
* `X-verdelingen` - Het aantal verdelingen rond de draaibankvorm; met 4 verdelingen krijg je bijvoorbeeld een vierkant profiel. 
* `Constante dichtheid` - Als dit aan staat, blijven de polygonen vierkant. Staat het uit, dan kun je `Y-verdelingen` instellen over de lengte van de vorm.
* `...` - Het instellingenmenu van Draaibank.

#### Instellingen van Draaibank {#lathe-settings}
* `Primitief` - Knoppen om UV's aan of uit te zetten, of om de vorm te voltooien.
* `Naderhand onderverdelen` - Een snelkoppeling om het multiresolutieniveau in te stellen voordat je voltooit.
* `Lineaire subdivisie` - Een snelkoppeling om het niveau van lineaire subdivisie in te stellen voordat je voltooit. 
* `Verdeling X` - Hetzelfde als X-verdelingen in de werkbalk.
* `Verdeling Y` - Hetzelfde als Y-verdelingen in de werkbalk.
* `Kromme (Repeater)` - Zet het profiel van de kromme om in een [Kromme-repeater](scene.md#curve).

### ![](/icons/tool_insert.webp) Invoegen {#insert}
Plaatst een object op het oppervlak van een ander object. In gebruik lijkt het op Stempel, maar dan voor volledige 3d-vormen.

Kies je een primitief in de linkerwerkbalk, dan plaatst klikken en slepen op een willekeurig oppervlak een primitief op de plek waar je klikt; het slepen bepaalt de grootte. Ben je klaar met slepen, dan schakelt Invoegen over naar de modus [Transformeren](#transform).

In de modus Instantie maakt slepen een nieuwe instantie die je over het oppervlak schuift. De grootte wordt overgenomen van de eerste vorm, zodat je veel even grote instanties van een object over andere oppervlakken kunt verspreiden.

Je hoeft niet alleen primitieven in te voegen! Selecteer *elke willekeurige* vorm in de outliner: staat Invoegen in de modus Instantie of Klonen, dan sleep je kopieën van het geselecteerde object over elk ander oppervlak.

Heeft een object een eigen draaipunt, dan wordt dat als ankerpunt gebruikt. Zie de video hieronder.

De linkerwerkbalk heeft ook `Bekijken`, om de camera te bewegen zonder iets in te voegen, en `Synchronisatie`: is het doelobject een instantie, dan wordt het nieuwe object ook aan alle andere instanties toegevoegd.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformeren {#transform}
Verplaats, draai en schaal een model direct met 1 en 2 vingers, meestal over het oppervlak van een ander object.

De linkerwerkbalk heeft deze knoppen:

* `Klonen` / `Instantie` - Maakt een kopie of een instantie van het object, zie de werkbalk van [Gizmo](#left-menu-toolbar).
* `Verplaats` - Slepen met één vinger verplaatst het object. Staat snappen aan, dan schuift het object over het oppervlak onder je vinger.
* `Draaien` - Slepen met één vinger draait het object. Staat snappen aan, dan draait het rond de normaal van het oppervlak onder je vinger.
* `Schaal` - Slepen met één vinger schaalt het object.

Een werkbalk bovenaan de viewport heeft:

* `Doel` - Of het gereedschap het object, zijn groep of zijn vertices verplaatst, net als bij de [Gizmo](#left-menu-toolbar).
* `Snappen` - Klikt het model vast op andere oppervlakken.
* `Oppervlak` / `Vertex` - Met `Snappen`: vastklikken op het oppervlak, of op de dichtstbijzijnde vertex.

Met Transformeren kun je snel 2 van deze modi combineren door 2 vingers te gebruiken:

* Sleep een object om het te plaatsen. Stop met het bewegen van je eerste vinger, maar til hem niet van het scherm.
* Zet je tweede vinger op het scherm terwijl de eerste blijft liggen. Terwijl je de tweede vinger sleept, wordt het object geschaald.
* Til de tweede vinger op en sleep verder met de eerste: het object staat weer in de verplaatsmodus.

Je kunt de tweede modus ook wisselen met een tik van de tweede vinger:

* Sleep het object om het te plaatsen, stop met bewegen, maar til je vinger niet van het scherm.
* Tik met je tweede vinger terwijl je de eerste vinger laat liggen.
* Het gereedschap schakelt over naar draaien. Sleep met je eerste vinger om de rotatie in te stellen.
* Tik zoals eerder met de tweede vinger: het gereedschap schakelt terug naar verplaatsen.

Zo kun je heel snel objecten over een ander object klonen, bijvoorbeeld rotsen over een landschap. De kloonknop staat ook in de linkerwerkbalk, zodat je er makkelijk bij kunt:

* Verplaats een rots met het gereedschap Transformeren naar zijn plek.
* Laat los en druk op de kloonknop.
* Verplaats deze rots en draai of schaal hem waar nodig.
* Laat los en druk op de kloonknop.
* Verplaats deze rots, en herhaal.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Met dit gereedschap verplaats, draai en schaal je objecten, en pas je hun draaipunt aan.

De handgreep in de viewport heeft de volgende functies:

* `Verplaats` - Sleep aan de lijn met pijl om langs X/Y/Z te verplaatsen. Sleep aan de perzikkleurige stip in het midden van de gizmo om vrij in de schermruimte te verplaatsen. Klik op de rode, groene of blauwe vierkantjes om in de X/Y/Z-vlakken te verplaatsen.
* `Draaien` - Sleep aan de rode/groene/blauwe cirkels om rond X/Y/Z te draaien. Sleep aan de bol binnen de cirkels om vrij te draaien.
* `Schaal`- Sleep aan de buitenste rode/groene/blauwe stippen om langs X/Y/Z te schalen. Sleep aan de buitenste rode/groene/blauwe kegels om in de X/Y/Z-vlakken te schalen. Sleep aan de buitenste perzikkleurige cirkel om gelijkmatig te schalen.

![](/images/tool_gizmo.webp)

#### Nodes en vertices {#nodes-and-vertices}

Elk object in Nomad bestaat uit een node en vertices:

* `Node` - De 'handgreep' van het object, die de verschuiving, rotatie en schaal bewaart: de transformatiematrix.
* `Vertices` - De punten die het oppervlak van een object bepalen; ze bewaren de positie en de verfgegevens.

Heb je een eenvoudige kubus van 8 vertices, dan kun je die verplaatsen door de transformatiematrix te wijzigen, of door de posities van de vertices te wijzigen. Bij het boetseren wil je meestal de vertices aanpassen; als je objecten met de gizmo verplaatst, wil je meestal de node aanpassen. In Nomad kan allebei. 

#### Werkbalken van Gizmo {#left-menu-toolbar}

De linkerwerkbalk heeft:

* `Klonen` - Maakt een zelfstandige kopie van het huidige object, die je met de gizmo kunt wegslepen.
* `Instantie` - Maakt een instantie van het huidige object. De objecten zijn gekoppeld, dus wat je op het ene object boetseert, verschijnt op alle instanties.
* `Draaipunt` - (Slotje, op de plek van de knop `Aftrekken`) Als dit aan staat, kun je de gizmo verplaatsen en draaien zonder het object te verplaatsen. Net als bij `Aftrekken` houd je hem ingedrukt voor een snelle wijziging, of tik je erop om hem aan te laten.

Een werkbalk bovenaan de viewport heeft de overige knoppen:

* `Doel` - Bepaalt of de gizmo de node of de vertices van een object aanpast:
    * `Automatisch` - De standaardinstelling. Werkt als `Groep`, maar als de mesh een masker heeft of symmetrie aan staat, werkt het als `Vertex`.
    * `Vertex` - Past de transformatie toe op de vertices, rekening houdend met masker en symmetrie. Werkt niet op niet-voltooide primitieven, en instanties worden ook aangepast.
    * `Object` - Verplaatst alleen het huidige object, zonder rekening te houden met symmetrie en masker. Onderliggende objecten blijven staan.
    * `Groep` - Verplaatst het object en de rest van zijn hiërarchie, zonder rekening te houden met symmetrie en masker.
    * `Instantie` - (Object en Groep) Hetzelfde, maar alle instanties van het object bewegen mee.
* `Draaipunt` - Een pop-up om snel het draaipunt te plaatsen, [hieronder](#pivot) uitgelegd.
* `Alles` / `Verplaats` / `Draaien` / `Schaal` - Toont alle handgrepen van de gizmo, of alleen die voor verplaatsen, draaien of schalen.
* `Vastzetten` - Standaard springt de gizmo naar het draaipunt van het geselecteerde object. Staat vastzetten aan, dan blijft de gizmo waar hij nu is.
* `Uitlijnen` - Wisselt tussen een draaipunt dat is uitgelijnd met het huidige object en een draaipunt dat is uitgelijnd met de wereld.
* `Kleven` (rotatie) - Laat rotatiewaarden in stappen vastklikken; de stapwaarde wordt getoond en kan worden aangepast als kleven aan staat. Met de optie `Magneet` blijft de rotatie even hangen bij een stap als je die passeert en beweegt daarna weer vrij; zet hem uit om van stap naar stap te springen.
* `Kleven` (verplaatsing) - Laat verplaatsingswaarden in stappen vastklikken; de stapwaarde wordt getoond en kan worden aangepast als kleven aan staat.

#### ![](/icons/reset.webp) Draaipunt {#pivot}
Met de pop-up `Draaipunt` in de bovenste werkbalk pas je het draaipunt snel aan. De positie en de oriëntatie van het draaipunt sturen de gizmo.

**Herstellen** 
* `Auto` - Midden van het object, uitgelijnd met zijn transformatie.
* `Midden` - Verplaatst het draaipunt naar het midden van het object, met behoud van de oriëntatie.
* `Onderkant` - Verplaatst het draaipunt naar het midden van de onderkant van het object. Tik nogmaals om in plaats daarvan de bounding box van de wereld te gebruiken.
* `Bovenkant` - Verplaatst het draaipunt naar het midden van de bovenkant van het object. Tik nogmaals om in plaats daarvan de bounding box van de wereld te gebruiken.
* `Object` - Verplaatst het draaipunt naar de oorsprong van het object, uitgelijnd met zijn transformatie.
* `Masker` - Verplaatst het draaipunt naar het midden van het niet-gemaskeerde gebied. Tik nogmaals om over te schakelen naar het gemaskeerde gebied.
* `Uitlijnen` - Zet de rotaties terug zodat ze met de wereld zijn uitgelijnd, met behoud van de positie.
* `Weergave` - Lijnt het draaipunt uit met de huidige weergave, met behoud van de positie. Het volgt de camera daarna niet.

**Bij tikken (Draaipunt-modus)**

Alleen actief als `Draaipunt` aan staat; bepaalt wat er gebeurt als je één keer op het oppervlak van de mesh tikt:
* `Geen` - Doet niets als je op het object tikt.
* `Normaal` - Verplaatst en draait het draaipunt zodat het uitgelijnd is met de plek waar je op het oppervlak tikt.
* `Eerst` - Verplaatst het draaipunt (zonder het te draaien) naar de plek waar je op het oppervlak tikt.
* `Midden` - Verplaatst het draaipunt naar het midden van het object, onder de plek waar je op het oppervlak tikt.

#### Instellingen van Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Compact` - Wisselt de indeling van de gizmo, met de extra handgrepen buiten of binnen de rotatiebol.
* `Gizmo-grootte` - De grootte van de gizmo.
* `Dikte` - De dikte van de lijnen van de gizmo.
* `Dekking` - De dekking van de gizmo.
* `Verberg bij interactie` - Of de gizmo tijdelijk verdwijnt terwijl je eraan sleept.

-----

* `Drempel voor tangentrollen` - Bepaalt hoe het draaien werkt als je aan de cirkels sleept om rond X/Y/Z te draaien. Staat deze waarde op 0, dan werkt draaien als een draaiknop: je sleept in cirkels rond de gizmo. Staat ze op 90, dan werkt draaien als het touwtje van een jojo: je sleept in een rechte lijn naar de plek waar je eerst klikte toe of ervan af. Waarden tussen 0 en 90 combineren beide: onder de waarde is het een lineaire beweging, erboven een cirkelbeweging.
* `Numerieke invoer` - Als dit aan staat, opent één tik op de gizmo een venster waarin je een exacte waarde invoert voor de aangetikte as.

::: warning
De gereedschappen [Gizmo](#gizmo) en [Transformeren](#transform) hebben hun eigen symmetrievakje, los van de symmetrie voor het boetseren!

Standaard staat deze symmetrie uit.
:::

##### Matrix {#matrix}
De exacte transformatiewaarden van het object staan niet meer in de instellingen van Gizmo: ze zijn verhuisd naar het menu `Transformeren`, in het menu rechtsboven. Het onderdeel `Matrix` daarvan heeft:

* ![](/icons/target.webp) `Verplaats oorsprong` - Verplaatst het object zodat zijn draaipunt in het midden van de scène ligt, de zogeheten oorsprong.
* ![](/icons/bake.webp)  `Toepassen` - Zet het object vast waar het nu staat en zet de verschuivings- en rotatiewaarden op 0 en de schaal op 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Draaipunt` - Bakt het draaipunt: de matrixwaarden komen overeen met waar de handgreep van de gizmo zich in de wereld bevindt.
* ![](/icons/reset.webp) `Reset` - Een snelkoppeling die de verschuivings- en rotatiewaarden op 0 en de schaal op 1 zet, waardoor het object wordt verplaatst en gedraaid.

::: tip Toepassen of draaipunt bakken
Maak een kubus, kies het gereedschap Gizmo, open het menu `Transformeren` en zet het vast. Standaard zijn verschuiving en rotatie 0 en is de schaal 1.

Zet de draaipuntmodus aan, verplaats de handgreep naar een kant en zet de draaipuntmodus weer uit. Het draaipunt is veranderd, maar zie dat de verschuivingswaarden nog steeds 0 zijn. 

Wil je zien waar het draaipunt *echt* is, klik dan op de knop `Draaipunt` om het te bakken. Nu worden de verschuivingswaarden bijgewerkt. Zie dat de kubus bij deze bewerking niet beweegt, net zo min als in de draaipuntmodus.

Verplaats en draai de kubus ergens heen en tik dan op `Verplaats oorsprong`. Het object wordt zo verplaatst dat zijn draaipunt in het midden van de wereld ligt, maar de rotatie blijft ongewijzigd.

Klik op `Reset`, en ook de rotatie wordt op 0 gezet.

Verplaats en draai de kubus nog eens en klik nu op `Toepassen`. Het draaipunt blijft waar het is, de kubus blijft waar hij is, maar de verschuivings- en rotatiewaarden worden op 0 gezet.

Oefen dit een paar keer! Zo krijg je door dat de waarden van het draaipunt verborgen zijn en dat Nomad ze voor je bijhoudt, maar dat je met het bakken van het draaipunt het draaipunt op een echte plek in de ruimte kunt vastleggen als dat nodig is.

:::

* `Verschuiving` - De verschuivingswaarden X, Y, Z.
* `Rotatie` - De rotatiewaarden X, Y, Z.
* `Schaal` - De uniforme schaal als die aan staat, anders de schaal X, Y, Z.
* `Scheef` - De scheefstandwaarden (shear) X, Y, Z, alleen getoond als het object al scheef staat.
* `Uniforme schaal` - Schakelt tussen gelijkmatig schalen en elke as apart schalen.

Links kun je het draaipunt van de gizmo verplaatsen; in de video hieronder zie je het in actie.
Dit is vooral handig voor de rotatie, want voor de verschuiving verandert het niets.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Vlakkengroep {#facegroup}

Met vlakkengroepen deel je je object op in vlakken met verschillende kleuren. Je kunt deze groepen in Nomad op veel manieren gebruiken:

* Als snelle selectiemethode voor maskers
* Om delen van je object te verbergen of te tonen
* Om je object te ordenen zonder het in losse delen te splitsen
* Om UV-gebieden te bepalen
* Om de quad remesher te sturen
* Als extra controle voor gereedschappen zoals Gladstrijken.

#### Linkerwerkbalk van Vlakkengroep {#facegroup-left-toolbar}

* `Groep` - De knop toont de huidige vlakkengroep. Tik erop om de beschikbare vlakkengroepen als stalen te zien en er een te kiezen. Tik op een staal om hem te hernoemen, van kleur te veranderen of te verwijderen. `Verwijder ongebruikte` verwijdert de ongebruikte stalen, `Herstellen` verwijdert ze allemaal. Met het plusicoon maak je nieuwe stalen.
* `Punt` - Schilder op het object om vlakkengroepen te bepalen. Staat '+ Vlakkengroep' aan, dan maakt elke nieuwe streek automatisch een nieuwe vlakkengroep, handig om snel gebieden af te bakenen. Een tik vult het gekozen gebied. De schuifregelaar stelt de straal van de punt in.
* `Ontspannen` - Strijkt de randen van vlakkengroepen glad. Heel handig voor strakke randen bij quad-remeshen, of om panelen te bepalen bij hard-surface-modelleren. De schuifregelaars bepalen de straal en de intensiteit van het ontspannen.
* Vormen - Maak vlakkengroepen met vormen in plaats van met een kwast, via `Vergrendelen + straal`, `Lasso`, `Polygoon`, `Lijn`, `Rechthoek` en `Ellips`. Zie [Selectieknoppen](#selection-controls) voor meer informatie.
* `Kiezen` - De submodus. Als deze aan staat, wordt de staal gekozen waar de streek begint, en wordt die staal de rest van de streek gebruikt. Heel handig om vlakkengroepen op te schonen: is een vlakkengroep te ver doorgelopen, zet dan `Kiezen` aan, begin een streek op een plek waar de staal klopt en sleep tot aan de rand om de juiste staal opnieuw toe te wijzen.

#### Bovenste werkbalk van Vlakkengroep {#facegroup-top-toolbar}

Een werkbalk bovenaan de viewport heeft extra knoppen:

* `Ontspannen (Alles)` - Sleep om de randen van alle vlakkengroepen tegelijk te ontspannen.
* `Voorzijde` / `Zichtbaar` / `Verbonden` - Dezelfde streekfilters als in de werkbalk van [Masker](#mask).
* `Uit normalen` - Maakt vlakkengroepen op basis van de hoek tussen vlakken. In de pop-up stel je de `Hoek` in, en kun je kleine groepen overslaan op basis van hun `Aantal zijden` of `Oppervlakte`, met een `Voorbeeld` voordat je bevestigt.
* `Uit delen` - Maakt een vlakkengroep voor elk los deel.
* `Uit UV’s` - Maakt een vlakkengroep voor elk UV-eiland.
* `Uit masker` - Maakt een vlakkengroep van het gemaskeerde gebied.
* `Bij tikken` - Kies wat een tik op een vlakkengroep doet: hem vullen met de huidige vlakkengroep, hem verbergen, hem maskeren, of hem in `Pose` zetten (de aangetikte groep en alles wat erachter ligt wordt ontmaskerd en de gizmo komt op het gewricht te staan, met een schuifregelaar `Vervagen` voor het masker). Een tweede schakelaar `Bij tikken`, beschikbaar als de mesh een masker heeft, beperkt de tik tot de vlakken aan dezelfde kant van het masker.
* Knoppen `Wissen` voor de gereedschappen [Verbergen](#hide) en [Masker](#mask), om alles weer zichtbaar te maken of het masker te wissen zonder het gereedschap te verlaten.

#### Instellingen van Vlakkengroep {#facegroup-settings}

Het menu `Gereedschap` haalt vlakkengroepen eruit als nieuwe objecten, met dezelfde opties als `Extraheer` in de [Instellingen van Masker](#mask-settings). Met de knop `Vlakkengroep` bovenaan kies je welke groepen worden geëxtraheerd, en er is een extra schuifregelaar `Spleet`: die verschuift elke rand naar binnen over het oppervlak; een negatieve waarde verschuift hem naar buiten, zodat de delen overlappen. Gebruik voor aangrenzende panelen de helft van de gewenste spleet.

### ![](/icons/tool_hide.webp) Verbergen {#hide}
Verberg of isoleer delen van het object. 

De hoofdmodi bedien je vanuit het linkermenu:

* `Punt` - Strijk met de kwast over het object om delen ervan te verbergen.
* Vormen -  Verberg met vormen in plaats van met een kwast, via `Lasso`, `Polygoon`, `Lijn`, `Rechthoek` en `Ellips`. Zie [Selectieknoppen](#selection-controls) voor meer informatie.
* `Tonen` - De submodus: keert de bewerking om, zodat de gekozen modus delen van het object toont in plaats van verbergt.

Bovenaan de viewport verschijnt een werkbalk met extra knoppen:

* `Alles wissen` - Herstelt de objecten: alle verborgen delen worden weer zichtbaar. Hebben andere objecten ook verborgen delen, dan herstelt een extra knop `Wissen` alleen de geselecteerde objecten.
* `Inverteren` - Wisselt de verborgen en zichtbare delen om.
* `Verwijderen` - Verwijdert het verborgen deel van het object.
* `Splitsen` - Maakt van het verborgen deel van het object een nieuwe vorm.
* `Voorzijde` / `Zichtbaar` / `Verbonden` - Dezelfde streekfilters als in de werkbalk van [Masker](#mask).
* `Bij tikken` (vlakkengroep) - Gebruik vlakkengroepen om snel delen te verbergen: een tik op een vlakkengroep verbergt de hele vlakkengroep.
* `Bij tikken` (masker) - Is er een masker actief, dan verbergt een tik het gemaskeerde deel.

### ![](/icons/tool_measure.webp) Meten {#measure}
Sleep om de afstand tussen 2 punten te meten. Zijn ze geplaatst, dan kun je de eindpunten verslepen om de meting bij te stellen.

In de linkerwerkbalk kies je hoe de afstand wordt gemeten:

* `Lijn` - Een rechte lijn tussen de twee punten.
* `Oppervlak` - De afstand over het oppervlak, langs de snede door de twee punten zoals de camera die ziet.
* `Doorsnede` - De omtrek van de doorsnede door de twee punten, zoals een meetlint om een arm.
* `Vertex` - Klikt de eindpunten vast op de dichtstbijzijnde vertex.
* `Gulden snede` - Toont een gele stip op het punt van de gulden snede van de meting.
* De knop `?` toont het volume, de oppervlakte en de afmetingen van de geselecteerde objecten.

### ![](/icons/tool_arrange.webp) Rangschikken {#arrange}
Lijn meerdere objecten tegelijk uit en verdeel ze, zoals met de uitlijngereedschappen van een 2d-ontwerpprogramma. Selecteer eerst de objecten; met één object werkt Rangschikken in plaats daarvan op de losse delen ervan. Rond de selectie wordt een kader getekend; sleep aan de handgrepen ervan om de selectie te schalen.

Een werkbalk bovenaan de viewport heeft de knoppen:

* `Wereld` / `Scherm` - Rangschikt langs de assen van de wereld, of langs het scherm (links, rechts, boven, onder).
* `Uitlijnen` - Lijnt de objecten per as uit op hun minimum, midden of maximum.
* `Verdelen` - Verdeelt de objecten gelijkmatig tussen de twee buitenste, op basis van hun minimum, midden of maximum. Er zijn minstens 3 objecten nodig.
* `Lijn` - Zet de objecten op een rij langs een as.
* `Raster` - Zet de objecten in een raster, met een aantal objecten op `X`, `Y` en `Z`.
* `Cirkel` - (alleen Wereld) Zet de objecten in een cirkel rond de as `X`, `Y` of `Z`.
* `Bol` - (alleen Wereld) Verdeelt de objecten over een bol.

`Lijn`, `Raster`, `Cirkel` en `Bol` hebben allemaal een schuifregelaar `Tussenruimte` voor de afstand tussen de objecten.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Dit gereedschap zet het geselecteerde object om in een nette topologie van quads, met instellingen voor de dichtheid, de edge flow en de symmetrie. 

::: tip
Quad Remesher wordt ontwikkeld door [Exoside](https://exoside.com/) voor iOS en desktop. 

Op iOS is het een in-app-aankoop binnen Nomad, een eenmalige betaling van $16 USD.

Voor desktop koop je een licentie bij [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Je kunt een licentie kopen voor alleen Nomad desktop, of een gecombineerde licentie voor alle ondersteunde desktopprogramma's.

Heb je Quad Remesher al voor een ander desktopprogramma, dan kun je [voordeliger upgraden naar alle platforms.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher is niet beschikbaar voor Android. Op Android kun je de gratis opensource-remeshers van het tabblad [Quad-remesh](topology.md#quad-remesh) in Topologie gebruiken (AutoRemesher, Instant Mesh, QuadriFlow), maar houd er rekening mee dat die minder mogelijkheden hebben.
:::

Zolang Quad Remesher niet is ontgrendeld, begint de bovenste werkbalk met een winkelwagenknop in plaats van de remesh-knoppen. Op iOS opent die de in-app-aankoop. Op desktop toont hij `Ontgrendel (aankoop, herstel, proefversie)`, waarmee je Exoside-licentie wordt gecontroleerd (of de proefperiode start). Zodra het actief is, worden de linker- en de bovenste werkbalk ingeschakeld.

* `Punt` - Met deze kwast stel je de doeldichtheid in. Intensiteit op 100% schildert rood, wat op die plekken twee keer de doeldichtheid aan quads gebruikt. Intensiteit op 0% schildert cyaan, wat op die plekken de helft van de doeldichtheid gebruikt. Intensiteit op 50% schildert grijs, wat de standaard doeldichtheid gebruikt.
* `Gladstrijken` - Strijkt de overgangen tussen rood, grijs en cyaan glad.
* `Vlekken` - Veegt de dichtheidsschildering uit.
* `Kromme` - Schets krommen op het oppervlak van je sculpt; de quad remesher gebruikt die als richtlijnen voor de edge flow. Tik op een kromme om hem te verwijderen.
* `Pad` - Teken paden op het oppervlak van je sculpt; de quad remesher gebruikt die als richtlijnen voor de edge flow. Tik op een pad om het te verwijderen. 
* `Rechthoek` - Teken rechthoeken op het oppervlak van je sculpt; de quad remesher gebruikt die als richtlijnen voor de edge flow. Tik op een pad om het te verwijderen.
* `Ellips` - Teken ellipsen op het oppervlak van je sculpt; de quad remesher gebruikt die als richtlijnen voor de edge flow. Tik op een pad om het te verwijderen.

#### Bovenste werkbalk van Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Bovenaan de viewport verschijnt een werkbalk met extra knoppen:


* `<Count>` - Klik hierop om de quad remesher te starten; het getal laat zien wat het beoogde aantal quads is.
* `Quads` - Stel het beoogde aantal quads in door naar links en rechts te schuiven, of tik om een exact getal in te voeren. Dit is eerder een richtwaarde dan een vast getal: door de verschillende instellingen van de quad remesher komt het resultaat vaak niet precies op dit aantal uit.
* `Half` - Een snelkoppeling die het beoogde aantal op de helft van het huidige aantal polygonen zet.
* `Zelfde` - Een snelkoppeling die het beoogde aantal gelijk zet aan het huidige aantal polygonen.
* `Richtlijnen` - Schakelt het gebruik van de richtlijnen in of uit. Zijn er richtlijnen, dan toont een tweede knop `Richtlijnen` hun aantal; tik erop om ze allemaal te verwijderen.
* `Dichtheid` - Schakelt het gebruik van de dichtheidsschildering in of uit. Is er dichtheid geschilderd, dan verwijdert een tweede knop `Dichtheid` die.
* `Vlakkengroep` - Schakelt in of uit of vlakkengroepen de quad remesher sturen.
* `Ontspannen` - Schakelt het automatisch ontspannen van de randen van vlakkengroepen tijdens het quad-remeshen in of uit. Heb je de randen van je vlakkengroepen al ontspannen of gladgestreken, zet deze optie dan uit.
* `Ontspannen (schuifregelaar)` - Een snelkoppeling om de randen van vlakkengroepen te ontspannen.
* `Harde randen` - Probeert harde randen te behouden.
* `Vertex herprojecteren` - Projecteert de nieuwe indeling terug op de oorspronkelijke mesh.
* `Sym` - Zorgt voor een symmetrisch resultaat. Let op: de symmetrie wordt altijd berekend rond de x-as van de wereld, dus zorg dat je model in de oorsprong staat als je een symmetrisch resultaat verwacht.
* `...` - De pop-up met instellingen van de quad remesher. 

#### Instellingenmenu van Quad Remesher {#quad-remesher-settings-menu}

De knop `...` aan het einde van de bovenste werkbalk opent een pop-up met de overige instellingen:

* `Adaptief aantal quads` - Gebruikt kleinere quads in sterk gekromde gebieden en grotere quads in minder gekromde gebieden.
* `Adaptieve grootte` - Stelt de mate van aanpassing in. Bij 100% is de aanpassing maximaal, bij 0% zijn de quads overal even groot.

::: tip

Een recept voor een goede quad-remesh met zo min mogelijk artefacten:

* Verdeel de mesh in vlakkengroepen om je ideale quadverloop te bepalen.
* Ontspan de vlakkengroepen voor gladde randen.
* Decimeer. Zo heb je geen dunne of vervormde vlakken op de randen van de vlakkengroepen. Zorg dat vlakkengroep aan staat in de instellingen van Decimeren: dan volgen de randen van de driehoeken precies de randen van je vlakkengroepen. 

Zorg dat ontspannen uit staat in de opties van de quad-remesh (je hebt de mesh immers al ontspannen), dan krijg je een goed resultaat.

:::

### ![](/icons/tool_select.webp) Selecteren {#select}
Gebruik de vormmodi (`Lasso`, `Rechthoek`, `Ellips`) om objecten in de scène te selecteren. `Deselecteren` haalt objecten uit de selectie.

### ![](/icons/tool_lattice.webp) Rooster {#lattice}
Vervorm een object met een kooi van controlepunten eromheen, in plaats van op het oppervlak te boetseren. Door een paar punten van de kooi te verplaatsen buig, verdraai of rek je het hele object vloeiend, ideaal om proporties aan te passen of te poseren zonder de topologie aan te raken. De vervorming blijft live totdat je hem voltooit.

In de linkerwerkbalk kies je hoe je de kooi bewerkt:

* `Punten` - Sleep direct aan de punten en ribben van de kooi. Tik op een punt om het te selecteren.
* `Bekijken` - Beweeg de camera zonder de kooi te bewerken.
* `Ontspannen` - Een kwast die de punten van de kooi eronder ontspant.
* `Elastisch` - Een kwast die de punten van de kooi met een elastische afname meetrekt, zoals het gereedschap [Elastisch](#elastic).
* `Gizmo` - Verplaats, draai en schaal de geselecteerde punten met de gizmo. De submodus is `Draaipunt`.
* `Lasso` - Selecteer punten van de kooi met een lasso; `Deselecteren` haalt ze uit de selectie.

De vorm-pop-up heeft ook `Zachte straal`, waarmee het verslepen van punten ook de naburige punten meeneemt (in rastercellen; 0 verplaatst alleen de selectie), en `Selectie omkeren`.

Een werkbalk bovenaan de viewport heeft:

* `Voltooien` - Past de vervorming toe op het object en verwijdert de kooi.
* `Herstellen` - Verwijdert de kooi en de vervorming.
* `Dekking` - De weergavedekking van de kooi.
* `Spiegel zijkant` - Wisselt bij symmetrie welke spiegelkant van de kooi wordt getoond en kan worden aangeklikt, met een eigen `Dekking` voor de verborgen kant.
* `Rasterpunten` - Welke punten van de kooi je kunt verplaatsen: het hele raster, het oppervlak plus het middelpunt, of alleen het oppervlak.
* `Rigiditeit` - Hoe stijf de vervorming is, van vloeiend (0%) tot stijf en lineair (100%).
* `Falloff` - Hoe ver de vervorming buiten de kooi doorloopt.
* `Uitlijnen` - Lijnt de kooi uit met het object, of met de wereld.
* `X`, `Y`, `Z` `Verdeling` - Het aantal cellen van de kooi op elke as. De modusknop ernaast bepaalt hoe ze samenhangen: `x = y = z` gebruikt hetzelfde aantal op alle 3 de assen, `Uniform` houdt op elke as dezelfde afstand tussen de punten, en met `Aangepast` stel je elke as vrij in.

#### Instellingen van Rooster {#lattice-settings}
* `Rolsnelheid` - Dezelfde rolopties als bij het gereedschap [Verplaats](#move-settings), gebruikt bij het verslepen van punten van de kooi.

### ![](/icons/tool_view.webp) Bekijken {#view}
Dit "gereedschap" doet niets bijzonders: het is gewoon een manier om het model te bekijken zonder je scène te wijzigen.

#### Instellingen van Bekijken {#view-settings}
Zolang het gereedschap Bekijken actief is, overschrijven deze instellingen een aantal weergaveopties, zodat je een strak beeld krijgt om je model te presenteren of te controleren:

* `Primitief (Bewerk)`, `Repeater (Bewerk)`, `Licht (Bewerk)`, `Camera (Bewerk)` - Staan het bewerken van primitieven, repeaters, lichten en camera's in de viewport toe terwijl je in het gereedschap Bekijken zit. Zet ze uit om te voorkomen dat je per ongeluk aan hun handgrepen trekt.
* `Camerasneltoets (altijd)` - Toont de camerasnelkoppelingen altijd in de viewport.
* `Toon masker`, `Omlijning`, `Verduister niet-geselecteerde objecten` - Toont het masker of de omlijning van de geselecteerde objecten, of maakt de niet-geselecteerde objecten donkerder. `Auto` volgt je gewone instelling, `Nee` en `Ja` dwingen het af.
* `Lijn tonen (Symmetrie)`, `Vlak tonen (Symmetrie)` - Toont de symmetrielijn of het symmetrievlak, met dezelfde keuzes `Auto`, `Nee` en `Ja`.
* `Icoon` - Toont de iconen van groepen, repeaters, lichten, camera's en de hiërarchie in de viewport, met dezelfde keuzes.


## Contextmenu van de gereedschapskist {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Klik met de rechtermuisknop op een gereedschap in de gereedschapskist of houd het lang ingedrukt om een contextmenu te openen. Dit menu heeft de volgende opties:

* `Opslaan` - Slaat de wijzigingen op die je aan het gereedschap hebt gemaakt.
* `Klonen` - Dupliceert het gereedschap naar een nieuwe snelkoppeling.
* `Laatste opslag` - Zet het gereedschap terug naar de vorige opgeslagen versie.
* `Icoon` - Verandert het icoon van het gereedschap. Heeft het gereedschap een eigen icoon, dan verwijdert deze knop dat.
* `→ ...` - Verplaatst het gereedschap naar een andere map van de gereedschapskist, of naar een nieuwe.
* `Herstellen` - Zet het gereedschap terug naar de standaardinstellingen.

Gekloonde gereedschappen hebben ook `Hernoem` en `Verwijderen`.
