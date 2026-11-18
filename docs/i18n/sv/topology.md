# ![](/icons/multires.webp) Topologi {#topology}

Den här menyn styr objektens topologi i Nomad, och har verktyg för att baka och överföra detaljer mellan objekt, och mellan texturer.

![](/images/topology_overview.webp)

Nomad bygger på polygoner: geometrin hanteras med trianglar och fyrhörningar (quads).
Med topologi menar vi både antalet ytor och hur punkterna (vertexerna) är förbundna med varandra.

Det är viktigt att hålla koll på topologin, särskilt om du vill skulptera eller måla fina detaljer.

::: tip Hur håller du koll på topologin?
Du kan visa [Wireframe](settings.md#wireframe) eller helt enkelt stänga av [Jämn skuggning](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Nomads topologimeny har flera flikar, på två rader:

| Metod                                 | Ikon                         | Beskrivning                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Redigera flera detaljnivåer med hjälp av indelning               |
| [Voxel-omnätning](#voxel-remesher)    | ![](/icons/voxel.webp)      | Beräkna en ny topologi med jämn täthet                           |
| [Dynamisk topologi](#dynamic-topology) | ![](/icons/dynamic.webp)   | Lägg till och ta bort ytor lokalt i realtid medan du skulpterar eller målar |
| [Blandat](#misc)                      | ![](/icons/topo_extra.webp) | Stäng hål, tvinga manifold och konvertera till triplanar         |
| [Grundform](#primitive)               | ![](/icons/dot.webp)        | Alternativ för primitiver                                        |
| [Decimera](#decimation)               | ![](/icons/decimate.webp)      | Minska antalet ytor och behåll formen                         |
| [Quad-omnätning](#quad-remesh)        | ![](/icons/quad.webp)       | Bygg om objektet med en ren layout av fyrhörningar               |
| [UV-uppackning](#uv-unwrap)           | ![](/icons/uv.webp)         | Skapa UV:er för texturering                                      |
| [Baka](#bake)                         | ![](/icons/bake.webp)       | Baka detaljer och målning till texturer, vertexer eller VDM-stämplar |


## Polygonstatistik {#polygon-stats}

![](/images/topology_stats.webp)

Överst i varje flik visas polygonantalet för det markerade objektet, och för hela scenen när den har mer än ett objekt. Kolumnerna visar antalet vertexer, trianglar, fyrhörningar (polygoner med 4 sidor) och UV-koordinater (0 när objektet saknar UV:er).

Tryck på det här avsnittet för att lista alla objekt i scenen med exakta siffror, inklusive antalet ytgrupper.

## ![](/icons/cog.webp) Kugghjulsmeny {#gear-menu}
Vissa avsnitt, som de i flikarna [Quad-omnätning](#quad-remesh) och [Baka](#bake), har extra alternativ. Öppna dem med kugghjulsikonen bredvid avsnittets rubrik.

## ![](/icons/multires.webp) Multiresolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### Vad är multiresolution? {#what-is-multiresolution}
Multiresolution är användbart i två huvudsakliga fall:
- Den mjuka indelningsalgoritmen, för att öka antalet polygoner i ditt objekt
- Att hantera flera upplösningsnivåer, så att du kan växla mellan ändringar i liten och stor skala

![](/videos/multiresolution.mp4)

#### Arbetsflöde med multiresolution {#multiresolution-workflow}
En viktig egenskap hos multiresolution är att du kan gå tillbaka till en lägre upplösning, göra ändringar i objektet och sedan gå tillbaka till den högsta upplösningen utan att förlora de högupplösta detaljerna. Alla högupplösta detaljer projiceras automatiskt.

[Lager](layers.md#layers) finns på alla upplösningar.

::: warning
Om du använder ett verktyg som ändrar objektets topologi förlorar du alla andra upplösningar av objektet!
Du bör alltid få en varning när det kan hända, till exempel när du använder:
- [Voxel-omnätning](#voxel-remesher)
- [Dynamisk topologi](#dynamic-topology)
- [verktyget Beskär](tools.md#trim)
- [verktyget Dela](tools.md#split)
:::


### Multiresolution-reglaget {#multiresolution-slider}
Reglaget visar antalet indelningsnivåer i det aktuella objektet. Finns det 6 lodräta streck finns det 6 indelningsnivåer. Cirkeln visar vilken indelningsnivå som visas just nu.

Små ikoner ovanför reglaget visar vilka alternativ (`Lås nivå 0`, `Linjär`, `Skarp gräns`, `Behåll trianglar`) som användes för varje nivå.

### Omvänd {#reverse}
När du är på den lägsta indelningsnivån försöker knappen Omvänd skapa en nivå under den aktuella. Observera att det i regel bara går om objektet från början skapades med indelning, till exempel i Nomad eller i andra 3d-program som har multiresolution med indelningsytor.

### Dela upp {#subdivide}
Knappen *Dela upp* fyrdubblar antalet polygoner, så håll ett öga på polygonantalet eftersom det kan växa väldigt snabbt! Nomad ber om bekräftelse när resultatet skulle bli väldigt tungt.
En viktig egenskap hos *indelningsytor* (subdivision surfaces) är att de närmar sig en *mjuk yta*.
För att förstå hur det fungerar kan du prova knappen *Dela upp* på ett objekt med bara några få polygoner.

Du kan stänga av det här *mjuka* beteendet med alternativet `Linjär`.

### Ta bort lägre {#delete-lower}
Raderar indelningarna under den nivå som visas, om det finns några. Gör du det av misstag kan du återskapa dem med knappen Omvänd.

### Ta bort högre {#delete-higher}
Raderar indelningarna ovanför den nivå som visas, om det finns några.

### ![](/icons/lock.webp) Lås nivå 0 {#lock-lv0}
Behåller formen på den lägsta indelningsnivån när du skulpterar på högre nivåer. Målning förs ändå ner till nivå 0. Det kan vara viktigt om objektet skapades i ett annat program och grundobjektet måste förbli oförändrat.

Alternativet finns bara före den första indelningen. När det är av flyttar stora ändringar på högre indelningsnivåer även nivå 0.

### ![](/icons/linear.webp) Linjär {#linear-subdivision}
Delar upp meshen utan någon utjämning.

### ![](/icons/group.webp) Skarp gräns {#sharp-border}
Om objektet har ytgrupper håller det här alternativet ytgruppernas gränser skarpa. Det kan ställas in för varje indelningsnivå (indelningsreglaget får då en liten ikon ovanför nivån som visar det).

### ![](/icons/triangle.webp) Behåll trianglar {#keep-triangles}
De flesta vanliga system för indelningsytor försöker göra om alla polygoner till fyrhörningar vid en indelning. Det här alternativet tvingar indelningen att använda trianglar i stället.

::: tip

Indelning jämnar som standard ut alla skarpa kanter. För att behålla kanterna lite skarpa kan du experimentera med `Linjär` eller `Skarp gräns` på de 2 första indelningsnivåerna och sedan stänga av det för de högre nivåerna. Då får du en halvskarp indelad mesh.

:::

### Visa högsta nivån {#show-highest-level}
Visar den högsta nivån med alla dess detaljer medan du skulpterar på en lägre nivå. Praktiskt för att se slutresultatet medan du gör stora ändringar.

### Wireframe: Endast nivå 0 {#wireframe-level-0-only}
När [Wireframe](settings.md#wireframe) är på visas bara wireframen för den lägsta nivån. Den täta wireframen på de höga nivåerna kan dölja formen.


## ![](/icons/voxel.webp) Voxel-omnätning {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Med `Voxel-omnätning` tvingas hela meshen få en topologi med jämn upplösning, vilket betyder att alla polygoner blir ungefär lika stora. Det är mycket användbart när du inte vill tänka på topologin utan bara skulptera fritt.

Ett typiskt arbetsflöde kan börja med att du använder `Voxel-omnätning` för att bygga upp en grov form med låg upplösning.
Tryck helt enkelt på knappen *Remesha* då och då när du sträcker ut meshen för mycket, så undviker du för stora förvrängningar.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Som sagt ovan är Nomad ett polygonbaserat program, men `Voxel-omnätning` är ett undantag där ett annat angreppssätt används (tillfälligt) för att göra omnätningen.

En stor skillnad är att voxelmetoden inte tillåter att ytan skär sig själv, så sådana ställen löses upp.
Den stödjer inte heller meshar med hål.

Med hål menar vi inte `genus-hål` (hålet i en munk), utan meshar som inte är `vattentäta`/`slutna`.
I praktiken betyder det att alla hål fylls innan omnätningen görs, ungefär som med [verktyget Beskär](tools.md#trim) eller [hålfyllningen](#holes). Alternativet [Hål](#voxel-holes) nedan väljer hur.
:::

### ![](/icons/voxel.webp) Remesha {#voxel-remesh}
Utför voxel-omnätningen. Små ikoner på knappen påminner dig om vilka av alternativen nedan som är på.

### Upplösning {#voxel-resolution}
Storleken på voxlarna som används i beräkningen, högre värden ger fler detaljer. Medan du ändrar värdet läggs ett schackrutigt mönster över meshen som förhandsvisar resultatet.

Pipetten hämtar upplösningen från meshens täthet där du trycker. Kubknappen bredvid den växlar värdet till en `Kantlängd` i världsenheter: samma värde ger då samma detaljnivå på alla objekt.

### Bygg multiresolution {#build-multiresolution}
Skapar lägre multiresolution-nivåer för voxel-omnätningen. Om du använder det schackrutiga mönstret för att välja en upplösning och sätter Bygg multiresolution till 2, får slutresultatet detaljer som motsvarar upplösningsreglaget, och går du till fliken Multiresolution står den på nivå 2, vilket betyder att du har meshar med lägre upplösning på nivå 1 och nivå 0. Det kan vara ett bra sätt att både få en ren mesh med jämna polygoner och en styrmesh med lägre upplösning.

Det går också snabbare och använder mindre minne vid höga upplösningar. Men med låg upplösning och många nivåer förlorar du detaljer.

::: tip Tips: Bygg multiresolution och stabil utjämning

Det här alternativet kan ibland ge "slingor" i geometrin som är svåra att jämna ut och som orsakar små knottror. Om det händer, aktivera `Stabil utjämning` bland alternativen för verktyget Jämna ut.

:::

### Förtjocka tunna delar {#thicken-thin-parts}
Delar som är tunnare än voxlarna kan gå sönder eller försvinna vid omnätningen. Det här alternativet gör dem tjockare så att de klarar sig, högre värden gör dem tjockare. Det går inte att använda tillsammans med `Skarpa kanter` eller `Skarp gräns`.

### Hål {#voxel-holes}
Hur hål stängs före omnätningen:

* `Fyll` - Varje hål stängs för sig, utifrån sin kant.
* `Form` - Hålen stängs genom att följa den omgivande ytan, och öppna delar som överlappar fogas ihop.

### ![](/icons/angle.webp) Skarpa kanter {#keep-sharp-edges}
Fäster de nya punkterna mot skarpa kanter i den ursprungliga meshen. Det är mest användbart för enkla booleska operationer med primitiver, och det kan ge förvrängningar.

### ![](/icons/group.webp) Skarp gräns {#voxel-sharp-border}
De nya ytorna följer ytgruppernas gränser, och en gräns förblir skarp där ytan viks längs den.

### ![](/icons/group_separate.webp) Håll grupper åtskilda {#keep-groups-separate}
Varje ytgrupp får ny topologi för sig: grupperna slås aldrig ihop, och var och en förblir en sluten del i sin egen grupp. Multiresolution byggs inte i det här läget. Alternativet finns när objektet har flera ytgrupper.

## ![](/icons/dynamic.webp) Dynamisk topologi {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution och voxel-omnätning är vanliga metoder i branschen för att styra topologin, men båda kräver att du ser upp så att du inte drar ut polygonerna för mycket eller trycker ihop dem för tätt.

Dynamisk topologi är en annan metod. Medan du skulpterar lägger Nomad till och tar bort polygoner under penseldraget efter behov, så när du ristar in små detaljer läggs många små polygoner till just där du behöver dem, och när du jämnar ut någon annanstans tas polygoner bort.

Observera att dynamisk topologi använder trianglar i stället för fyrhörningar. Det kan se lite rörigt ut, men det är nästan bättre att inte titta på wireframen alls: koncentrera dig på att göra en snygg skulptur utan att oroa dig för topologin, och använd sedan något av Nomads andra omnätningsverktyg för att få en ren mesh med fyrhörningar.

Se videon nedan för att se det i praktiken.

![](/videos/dynamic.mp4)

### Aktiverad {#enabled}
Slår på dynamisk topologi. En DynTopo-ikon placeras under reglagen för penselns radie och intensitet, så att du kan slå på eller av DynTopo per verktyg. Det kan märkbart påverka prestandan, och lagren uppdateras korrekt.

### Detalj {#dyn-detail}
Styr detaljnivån. Hur den beter sig beror på vad du valt under "Detaljer baserade på...", se nedan. I läget `Skärm` visar etiketten målstorleken för trianglarna i pixlar. I läget `Konstant` kan du med en pipett hämta detaljnivån från meshens täthet där du trycker.

### Detaljer baserade på... {#detail-based-on}
| Metod    | Beskrivning                                                     |
| :------: | :-------------------------------------------------------------: |
| Skärm    | Detaljnivån beror på hur stort objektet är på skärmen. Detaljreglaget på 100 % eller mer ger fina detaljer med små trianglar, och 1 % ger låg detaljnivå med stora trianglar.  |
| Radie    | Verktygets radie bestämmer detaljnivån. Använd en liten verktygsradie för fina detaljer och en stor för låg detaljnivå. Detaljreglaget är en faktor på det här förhållandet.        |
| Konstant | Detaljreglaget bestämmer detaljnivån, och påverkas inte av skärmstorleken eller verktygets storlek. Det är samma värde som reglaget [Detalj](#all-detail) för `Omnäta`.             |

::: tip TIPS: Läget Radie

För att få en bättre känsla för hur läget Radie fungerar kan du börja dra i detaljreglaget med ett finger och samtidigt ändra verktygets radie med ett annat finger. Då ser du hur de hänger ihop.

:::

### Föredra... {#prefer}
| Metod     | Beskrivning          |
| :-------: | :------------------: |
| Hastighet | Prioritera prestanda |
| Kvalitet  | Prioritera kvalitet  |

När du prioriterar `Kvalitet` är de 2 största skillnaderna:
- förfiningen görs före skulpteringen, så du får färre interpoleringsartefakter när du målar eller skulpterar mycket små detaljer
- förfiningen körs tills den når rätt detaljnivå, i stället för att ske stegvis.
 
På så sätt förfinas topologin alltid som väntat, även om du skulpterar mycket små detaljer eller gör snabba penseldrag


### ![](/icons/pressure.webp) Använd tryck på radien {#use-pressure-on-radius}
Gäller bara om `Radie` är aktiverat. När det här är på följer detaljnivån alltid penselns storlek, även när penselns storlek påverkas av pennans tryck.

### Använd penseldragets avtoning {#use-stroke-falloff}

Tar även med penselns avtoningskurva och alpha i DynTopo-beräkningarna.

### Metod {#method}
Väljer hur dynamisk topologi ändrar meshen, både medan du skulpterar och när du använder [Omnäta](#dyn-remesh):

| Metod          | Beskrivning                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisering | Kan både lägga till och ta bort ytor, det är läget som används i videon ovan |
| Indelning      | Lägger bara till nya ytor, kan inte ta bort ytor                      |
| Decimering     | Tar bara bort ytor, kan inte lägga till nya ytor                      |

### ![](/icons/shield.webp) Skydda maskerat område {#protect-masked-area}
Skyddar maskerade områden så att topologin där inte ändras.

### ![](/icons/normal.webp) Vertexextrapolering {#vertex-extrapolation}
Placerar punkterna på en mjuk yta som följer krökningen runt dem, i stället för platt på de befintliga ytorna.

### Detalj {#all-detail}
Upplösningen som används för omnätningen. Om DynTopo står i läget `Konstant` är det samma värde som reglaget Detalj högst upp i menyn. Pipetten hämtar detaljnivån från meshens täthet där du trycker.

### Omnäta {#dyn-remesh}
Gör en omnätning av hela meshen med DynTopo-algoritmen. Oftast bör du använda [Voxel-omnätning](#voxel-remesher) när du vill göra om hela meshen.

En fördel jämfört med voxlarna är dock att meshen inte behöver vara sluten, och att maskerade områden skyddas, så du får bättre kontroll över var du vill ha mer eller mindre täthet.



## ![](/icons/topo_extra.webp) Blandat {#misc}

![](/images/topology_misc_menu.webp)

Den här fliken samlar verktyg för att rensa eller konvertera meshen: stänga dess hål, tvinga den att vara manifold eller göra om den till en triplanar.

### ![](/icons/hole.webp) Hål {#holes}
![](/images/topology_holes_menu.webp)
För det mesta är ditt objekt antagligen vattentätt, vilket betyder att meshen är "sluten".

Om objektet har hål kan du fylla dem.

![](/videos/hole_filling.mp4)

::: tip
När du kör voxel-omnätningen stängs alla hål automatiskt, oavsett om du använder den på en eller flera meshar.
:::

#### Stäng hål {#close-holes}
Utför stängningen av hålen.

#### Alternativ {#holes-gear-menu}
De här alternativen ändrar hur hålen fylls:

##### Ytgrupp {#fill-face-group}
Väljer ytgrupp för de nya ytorna:

* `Blandad` - Ett hål som omges av en enda ytgrupp återanvänder den, ett hål som gränsar till flera grupper får en ny.
* `Ny` - De fyllda hålen får en ny ytgrupp.
* `Återanvänd` - Varje hål får den ytgrupp som omger det mest.

##### Detalj {#fill-detail}
Polygontätheten som används för att fylla hålet. Medan du drar i reglaget visas ett schackrutigt mönster på modellen, som ger en uppfattning om vilken triangelstorlek som används. Kryssrutan stänger av det, och då används bara de befintliga punkterna, vilket oftast ger långa smala trianglar över hålet som kan vara svåra att skulptera.

##### Överbrygga {#fill-non-manifold}
Fyller ett hål och öarna inuti det som en enda yta, i stället för att fylla varje kant för sig. En större vinkel överbryggar mer böjda hål. Kryssrutan stänger av det.

### ![](/icons/cog.webp) Tvinga manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Försöker rensa bort kanter som inte är manifold. Det kan vara användbart för externa program som inte stödjer kanter som delas av fler än 2 ytor.

#### Rensa {#clean}
Utför rensningen.

#### Alternativ {#force-manifold-gear-menu}
Det här alternativet ändrar hur meshen rensas:

##### Ta bort små ytor {#delete-small-faces}
En tröskel som används för att ta bort och slå ihop små polygoner. Aktivera det med kryssrutan.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Gör om meshen till en [triplanar](scene.md#triplanar)-primitiv.
Du förlorar troligen mycket detaljer på vägen: lager, målning och multiresolution går också förlorade.

#### Tvinga kubform {#force-cubic}
Gör triplanaren till en kub. Annars anpassas triplanaren till den närmaste omslutande lådan runt objektet.

#### Konvertera {#convert}
Utför konverteringen till triplanar.

#### Upplösning {#triplanar-resolution}
Upplösningen på triplanarens rutnät, högre värden behåller fler detaljer.

## ![](/icons/decimate.webp) Decimera {#decimation}

![](/images/topology_decimation.webp)

Minskar antalet polygoner och försöker behålla så många detaljer som möjligt, med hjälp av trianglar.

Det kan vara användbart om du vill exportera för 3d-utskrift.
Men du bör nog inte använda det om du vill fortsätta skulptera på objektet, eftersom det kan ge ojämna trianglar.

Observera att maskerade områden inte decimeras.

![](/videos/decimate.mp4)

::: tip

Att använda [Quad Remesher-verktyget](tools.md#quad-remesher) på objekt med många polygoner kan ta lång tid och ge resultat som är svåra att styra. Förbereder du meshen med [ytgrupper](tools.md#facegroup) och decimering går Quad Remesher mycket snabbare, och du får mycket bättre kontroll över topologin.

* Dela in meshen i ytgrupper för att ange hur du vill att fyrhörningarna ska flöda.
* Slappna av ytgrupperna för att få mjuka gränser mellan dem.
* Decimera. Det ser till att du inte har några smala eller förvrängda ytor längs ytgruppernas kanter. Under `Bevara kanter`, se till att `Ytgrupp` är aktiverat. Då följer trianglarnas kanter exakt ytgruppernas kanter.
* I alternativen för Quad Remesher, se till att avslappning är avstängd (eftersom du redan har slappnat av meshen), så bör du få bra resultat.

:::

### Decimera {#decimate}
Startar decimeringen.

Ikonerna bredvid decimeringsknappen visar alternativen nedan och låter dig slå på eller av dem. Procentsatsen visar hur starkt alternativet är.

* ![](/icons/palette.webp)  `Bevara målning` - Placerar fler trianglar där det finns detaljer i målningen.
* ![](/icons/triforce.webp) `Enhetliga ytor` - Föredrar trianglar av jämn storlek.
* ![](/icons/hole.webp)  `Hål` - Decimeringen försöker lämna kanter nära öppen geometri och hål oförändrade.
* ![](/icons/group.webp) `Ytgrupp` - Decimeringen försöker lämna ytgruppernas gränser oförändrade.
* ![](/icons/uv.webp) `UV` - Decimeringen försöker lämna UV-gränserna oförändrade.

### Måltrianglar {#target-triangles}
Anger det önskade antalet trianglar. Standardvärdet är 50 %, och knappen procent/mål växlar mellan en procentsats och ett exakt antal polygoner.

### Alternativ {#decimate-gear-menu}
Varje alternativ har en kryssruta för att slå på eller av det, och ett värde för dess styrka:

#### ![](/icons/palette.webp) Bevara målning {#preserve-painting}
Värdet bestämmer hur noggrant detaljerna i målningen bevaras. Högre värden bevarar mer av målningen. Sätt det till 0 om du inte bryr dig om målningen.

#### ![](/icons/triforce.webp) Enhetliga ytor {#uniform-faces}
Högre värden ger trianglar av liknande storlek.

#### Bevara kanter {#preserve-borders}
Förhindrar att kanter decimeras. Vikter kan anges för kanterna `Hål`, `Ytgrupp` eller `UV` (`UV` kräver ett objekt med UV:er).

## ![](/icons/quad.webp) Quad-omnätning {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Bygger om objektet med en ren layout av fyrhörningar. Fliken har flera omnätningsverktyg, vart och ett med sin egen knapp `Remesha`, sitt reglage `Målquads` och sin kugghjulsmeny. Prova dem på ditt objekt, de ger ganska olika resultat!

### Quad Remesher {#quad-remesher}
Samma omnätning som verktyget [Quad Remesher](tools.md#quad-remesher), utvecklat av [Exoside](https://exoside.com/). Det finns bara på vissa plattformar och kräver ett köp: tills dess visar knappen `Remesha` en kundvagn.

`Välj verktyg` byter till verktyget Quad Remesher, där du ritar guider och målar tätheten. Kugghjulsmenyn innehåller `Adaptiv Kvadrattal`, `Adaptiv storlek` (på 100 % följer fyrhörningarnas storlek krökningen, på 0 % blir de enhetliga), `Automatisk upptäckt av hårda kanter` och `Reprojektera vertex`.

::: tip
Där Quad Remesher finns ger det i regel de bästa resultaten och mest kontroll.
:::

### AutoRemesher {#autoremesher}
En alternativ omnätning med fyrhörningar, med alternativ för att anpassa fyrhörningarnas storlek och form efter ytan.

#### ![](/icons/cog.webp) Kugghjulsmenyn för AutoRemesher {#autoremesher-gear-menu}
Kugghjulsmenyn har de här avancerade alternativen:

##### Kantskalning {#edge-scaling}
Skalar fyrhörningarnas storlek, högre värden ger större fyrhörningar.

##### Anpassning {#adaptivity}
Anpassar fyrhörningarnas täthet efter krökningen. 0 ger enhetliga fyrhörningar, 1 ger mindre fyrhörningar på böjda områden.

##### Anisotropi {#anisotropy}
Sträcker ut fyrhörningarna längs ytans plattaste riktning. 0 ger kvadratiska fyrhörningar, 1 ger avlånga fyrhörningar på rör och åsar.

##### Skarp kant {#sharp-edge}
Kanter som är böjda mer än den här vinkeln bevaras som skarpa detaljer.

##### Jämna ut normaler {#smooth-normal}
0 behåller ytan facetterad under omnätningen. Högre värden jämnar ut ytan genom att ta hänsyn till vertexnormalerna.

##### Max fyllhål {#autoremesher-max-fill-hole}
Algoritmen kan ibland skapa oönskade hål. Om ett hål har färre vertexer än det här värdet fylls det.

### Instant Mesh {#quad-remesh-instant}
Gör omnätningen med [algoritmen Instant Meshes av Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Den analyserar meshens flöde och skapar en ren topologi med fyrhörningar.

#### Remesha {#instant-remesh}
Startar omnätningen.

#### Målquads {#target-quads}
Antalet fyrhörningar som omnätningen försöker skapa.

#### ![](/icons/cog.webp) Kugghjulsmenyn för Instant Mesh {#quad-remesh-instant-gear-menu}
Kugghjulsmenyn har de här avancerade alternativen:

##### Veckvinkel {#crease-angle}
En tröskel för skarpa hörn som hjälper till att styra omnätningen. Aktivera den med kryssrutan.

##### Max fyllhål {#max-fill-hole}
Algoritmen kan ibland skapa oönskade hål. Om ett hål har färre vertexer än det här värdet fylls det.

### QuadriFlow {#quadriflow}
Gör omnätningen med algoritmen QuadriFlow, ett annat sätt att få en ren layout av fyrhörningar.

#### ![](/icons/cog.webp) Kugghjulsmenyn för QuadriFlow {#quadriflow-gear-menu}
Kugghjulsmenyn har de här avancerade alternativen:

##### Bevara kanter {#quadriflow-preserve-boundary}
Skyddar hålens kanter.

##### Behåll skarpa kanter {#keep-sharp}
Riktar in fyrhörningarna efter ytans skarpa kanter.

##### Minsta kostnadsflöde {#min-cost-flow}
Använder en lösare för minsta kostnadsflöde för layouten av fyrhörningar. Långsammare, men kan ge en mer regelbunden topologi.

## ![](/icons/uv.webp) UV-uppackning {#uv-unwrap}
Beräknar texturkoordinater (UV:er) för det markerade objektet. Nomad har två metoder, `UVAtlas` och `BFF`, var och en med sin egen knapp `Packa upp`.

![](/videos/unwrap.mp4)

::: tip UV:er?
En vanlig liknelse för UV:er är att slå in en present: hur klipper du bäst till omslagspapperet för att täcka ett föremål helt, utan att det överlappar?

UV:er fungerar på liknande sätt, men i stället för att klippa papperet klipper du i objektet. Föreställ dig att modellen var gjord av tunn plast: hur skulle du klippa isär den för att vika ut den platt, måla på den i det platta läget och sedan sätta ihop den igen?

Föreställ dig nu att modellens yta är gjord av töjbar lycra. Du kan sträcka ut modellen platt, klippa i den, eller både och. Men om du målade ett schackmönster på objektet när det låg platt skulle mönstret bli förvrängt när du satte ihop det igen. Vilket är bäst: fler snitt med mindre förvrängning, eller färre snitt med mer förvrängning?

UV:er är instruktioner som talar om för 3d-program hur objektet ska "klippas och sträckas" när texturer läggs på. Verktyget UVAtlas använder i regel principen "fler snitt, mindre förvrängning".


:::

::: tip UV:er i Nomad och andra appar

De flesta texturerade modeller du hittar på nätet är texturerade med UV:er. Nomad kan importera och visa dem via panelen [Material](material.md#textures).

När du gör modeller i Nomad kan du måla direkt på objekten utan UV:er. Om du behöver exportera dem till andra appar, till exempel [Procreate](https://procreate.art/), kan du "baka" Nomads färginformation till texturer via UV:er.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas föredrar i regel att göra fler öar med snitt, för att minimera förvrängningen.

#### Packa upp {#unwrap}
Beräknar UV:er för det markerade objektet.

#### Alternativ {#uvatlas-gear-menu}
Knapparna bredvid `Packa upp`:

##### Ytgrupp {#atlas-face-group}
När den visar `Ja` bestämmer ytgrupperna var UV:erna ska skäras. Inställningen delas med BFF.

##### Radera UVs {#delete-uvs}
Papperskorgsknappen raderar objektets UV:er.

##### Inspektera {#uv-inspect}
Visar objektets UV:er i bakgrunden.

#### Maximal töjning {#max-stretch}
Låga värden ger mindre förvrängning och fler öar, höga värden ger mer förvrängning och färre öar.

#### Öavstånd {#island-spacing}
Hur mycket utrymme det ska vara mellan öarna. Låga värden slösar mindre plats, men riskerar att texturer blöder över mellan öarna.

::: warning
Att beräkna UV:er kan ta en stund, det är bäst att ha en mesh med färre än 100k vertexer.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV:er från BFF följer principen "färre snitt, mer förvrängning".

#### Alternativ {#uv-bff-gear-menu}
Samma knappar `Ytgrupp`, radera och `Inspektera` som för [UVAtlas](#uvatlas-gear-menu) finns bredvid `Packa upp`.

##### Ytgrupp {#bff-face-group}

Använder ytgrupperna för att bestämma var UV:erna ska skäras.

#### Kon-räkning {#cone-count}
Anger antalet huvudprojektioner som används. Lägre värden ger färre öar men mer förvrängning. Högre värden tar längre tid att beräkna.

#### Sömlösa patchar {#seamless-patches}
Påverkar layouten av UV-patcharna, och kan ge kraftig förvrängning. Fungerar bäst med noggrant skapade ytgrupper.

::: warning
BFF kan skapa överlappande UV:er om meshen har handtag (som hålet i en munk).
:::

### ![](/icons/preview.webp) Visa UV efter uppackning {#show-uv-after-unwrap}
Öppnar UV-granskningsvyn efter uppackningen, så att du kan kontrollera resultatet direkt.

### ![](/icons/bake.webp) Baka: Textur → Textur {#unwrap-bake-texture}
Finns bara när objektets material har texturer. När du packar upp det igen överförs texturerna till de nya UV:erna, så att de fortfarande passar. Upplösningen är `Auto` som standard, vilket motsvarar den största texturen, men du kan också ställa in den själv.

## ![](/icons/bake.webp) Baka {#bake}
Den här fliken överför detaljer och målning mellan objekt, och mellan vertexer och texturer.

`Från högupplöst` använder andra objekt som källa, och siffran inom parentes visar hur många. Nomad väljer dem så här:

- alla markerade objekt används, och det huvudsakligt markerade objektet är målet (det som är tydligast framhävt i menyn [Scen](scene.md))
- om bara ett objekt är markerat använder Nomad i stället alla synliga objekt
- om alla andra objekt är dolda (till exempel med Solo) används hela scenen

### ![](/icons/bake.webp) Baka → Textur {#bake-texture}
![](/images/topology_bake_menu.webp)

Texturbakning skapar texturer genom att projicera andra synliga objekt i scenen på det markerade objektets UV:er. Objektet behöver UV:er.

Så här ser ett typiskt arbetsflöde för bakning ut:
- Du har en mesh med fina detaljer och målning
- Klona den
- Decimera den (sätt `Bevara målning` till 0)
- Packa upp dess UV:er
- Baka den!

Nu bör du ha en mesh med låg upplösning som behåller det mesta av målningen och detaljerna från ditt tidigare objekt.

Efter operationen flyttas vertexfärgerna till ett nytt, inaktiverat lager, så att de inte stör texturerna.

#### Från objektet självt {#tex-from-itself}
Bakar objektet på dess egna UV:er: målningen blir texturer, och om det har multiresolution-nivåer bakas detaljerna från den högsta nivån in på den aktuella (en multires-ikon visas då på knappen). Det är enkelt att ställa in, men ofta behöver du mer kontroll, och då är nästa alternativ mer användbart.

#### Från högupplöst {#tex-from-high-res}
Bakar från de andra objekten till det markerade objektet. Siffran inom parentes visar hur många andra objekt som används som högupplösta källor och bakas in i det aktuella lågupplösta objektet med UV:er. De andra objekten behöver inte ha liknande layout eller topologi som objektet som bakas, vilket ger stor frihet i arbetsflödet.

#### Upplösning {#tex-bake-resolution}
Upplösningen på den bakade texturen. Bakade texturer är alltid kvadratiska, så 1024 ger en bild på 1024x1024.

Knapparna nedanför är genvägar till vanliga upplösningar. Som jämförelse är 512x512 ganska litet, till exempel för webbgrafik och enkel geometri. 4096x4096 (4k i korthet) är för renderingar av hög kvalitet.

#### Färg, Grovhet, Metallitet, Normal, Förskjutning, Emissiv, Opacitet {#tex-normal-roughness-metalness-color-emissive-opacity}
De här knapparna bestämmer vilka egenskaper som bakas, var och en till en egen karta. När bakningen är klar läggs de till som texturer i det aktuella objektets material. `Förskjutning` bakar detaljernas höjd som en förskjutningskarta (displacement map).

#### ![](/icons/cog.webp) Kugghjulsmenyn för bakning {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Kugghjulsmenyn har de här avancerade alternativen:

##### Backup {#tex-backup}
För att förhandsvisa de bakade texturerna bör objektets målningsinformation vara inaktiverad. `Backup (Målning → Lager)` flyttar all målningsinformation till ett nytt lager som backup, så att den enkelt kan slås på och av.

##### Använd multires {#tex-use-multires}
För `Från objektet självt` på ett objekt med multiresolution-nivåer. Nomad läser den höga upplösningen genom indelningsnivåerna i stället för att skicka ut strålar: det går snabbare och ger inga projiceringsfel. Stäng av det för att baka med alternativen nedan.

##### Mjuk bas {#tex-smooth-base}
För `Förskjutning` på ett objekt med multiresolution-nivåer. Mäter förskjutningen från den indelade basen i stället för från dess platta ytor. Låt det vara på när förskjutningskartan ska användas på en indelad mesh, som med adaptiv indelning i Blender.

##### Sökavstånd {#tex-cage-radius}
Det största avstånd som används för att hitta källytan. Som standard hålls avståndet kort för att undvika artefakter, men det kan ökas om källobjekten ligger långt från objektet som bakas.

##### Projektion {#tex-projection}
Hur källytan hittas:

* `Stråle` - Projicerar längs ytans normal.
* `Stråle + närmaste` - Använder strålen längs normalen, och sedan den närmaste ytan om strålen missar.
* `Närmaste` - Projicerar till den närmaste punkten på källytan.

##### Strål offset {#tex-ray-offset}
Justerar varifrån bakningsberäkningarna startar på objektet som bakas. En liten förskjutning från ytan undviker de vanligaste artefakterna. Om källobjekten ligger mycket långt från objektet som bakas kan förskjutningen behöva ökas. Den används inte av `Närmaste`.


### ![](/icons/bake.webp) Projektera om → Vertex {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projicerar skulpterade detaljer, målning, lager och texturer till värden i vertexerna.

Du kan se det som motsatsen till bakning: om bakning överför vertexernas egenskaper till texturer, så överför omprojicering texturer (och andra egenskaper)
 tillbaka till vertexerna.

::: tip
När du använder `Baka → Textur` eller `Projektera om → Vertex` tas både vertexfärgerna och materialets texturer med i beräkningen.
:::

#### Från objektet självt {#vertex-from-itself}
Gör om texturerna från materialet till värden i vertexerna. Knappen är bara aktiv om objektet har UV:er och texturerna är aktiva i materialet.

::: tip TIPS: Texturmålning
Nomad har inget direkt stöd för att måla och redigera texturer, men du kan få mycket liknande resultat genom att projicera texturer -> vertexvärden, måla på vertexerna och sedan baka vertex -> texturer:

1. Förbered ett objekt med få polygoner och UV:er
1. Ladda in texturer i dess material
1. Dela upp det tillräckligt för att kunna måla på det
1. `Projektera om → Vertex` i läget `Från objektet självt`, nu har texturen gjorts om till vertexvärden
1. Måla, jämna ut, smeta ut, stämpla, gör de ändringar du behöver
1. `Baka → Textur`, i läget `Från objektet självt`. Ändringarna görs om till texturer igen.
:::

#### Från högupplöst {#vertex-from-high-res}
Gör om de andra objekten till vertexvärden på det markerade objektet. Siffran på knappen visar antalet källobjekt. Det är främst tänkt att användas på en högupplöst mesh även här, oftast med en ren topologi.

::: tip
Att projicera om andra objekt kan användas inte bara för att överföra färginformation från andra objekt, utan också för att projicera vertexer på andra objekt, till exempel kan bandage projiceras på en karaktär.
:::

#### Vertexer, Färg, Grovhet, Metallitet, Opacitet, Mask, Lager, Ytgrupp {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
De här knapparna bestämmer vilka egenskaper som projiceras på det markerade objektet. `Lager` överför de andra lagren till den markerade meshen.

#### ![](/icons/cog.webp) Kugghjulsmenyn för omprojicering {#vertex-reproject-gear-menu}
Kugghjulsmenyn har de här avancerade alternativen:

##### Opacitet → Mask {#vertex-opacity-to-mask}
Gör om källans opacitet till mask på det markerade objektet.

##### Iterationer {#vertex-iterations}
Hur många gånger avslappningen ska tillämpas under omprojiceringen. Används bara när `Vertexer` är på.

##### Avslappna {#vertex-relax}
Den markerade meshens layout kan jämnas ut eller slappnas av en viss mängd för att bättre passa källorna för omprojiceringen. `Jämna ut` är bättre för meshar med många polygoner, `Avslappna` är bättre för meshar med få polygoner. `Auto` låter Nomad välja den bästa metoden.

##### Sökavstånd {#vertex-cage-radius}
Det största avstånd som används för att hitta källytan. Som standard hålls avståndet kort för att undvika artefakter, men det kan ökas om källobjekten ligger långt från det markerade objektet.

##### Projektion {#vertex-projection}
Hur källytan hittas:

* `Stråle` - Projicerar längs ytans normal.
* `Adaptiv blandning` - Blandar strålen längs normalen och den närmaste ytan efter avståndet och `Strålprioritet`. Om den ena missar används den andra.
* `Närmaste` - Projicerar till den närmaste punkten på källytan.

##### Strålprioritet {#vertex-ray-bias}
Bara för `Adaptiv blandning`. Högre värden väger blandningen mot strålens resultat, lägre värden mot den närmaste punkten.

##### Strål offset {#ray-vertex-offset}
Justerar varifrån bakningsberäkningarna startar på det markerade objektet. En liten förskjutning från ytan undviker vissa artefakter. Om källobjekten ligger mycket långt från objektet som bakas kan förskjutningen behöva ökas. Den används inte av `Närmaste`.

### ![](/icons/bake.webp) Baka → VDM {#bake-vdm}
Skapar en VDM-stämpel (vektorförskjutning) från det markerade objektet och lägger till den i VDM-biblioteket. Du blir ombedd att ange ett namn.

Så här ser ett typiskt arbetsflöde ut:
- Lägg till ett plan, eller välj `Ny VDM` i VDM-väljaren för att lägga till ett färdigt förberett (primitiven [VDM](scene.md#add-menu))
- Skulptera din form på det, och håll kanten platt
- Baka det!

Planets UV:er bestämmer vilken kvadrat som bakas, så objektet behöver UV:er. Välj stämpelns storlek med `Upplösning`, och välj med `Färg`, `Grovhet`, `Metallitet` och `Opacitet` vad stämpeln ska innehålla utöver förskjutningen.

::: tip
Undvik DynTopo på planet, det förstör dess UV:er och stämpeln blir förvrängd. Att skulptera i ett lager ger det mest exakta resultatet, eftersom det platta planet fortfarande finns kvar under. Målning kräver också ett lager, annars stämplas materialet över hela kvadraten i stället för bara där du målade.
:::

## ![](/icons/dot.webp) Grundform {#primitive}
Parametrar för den markerade primitiven. De flesta finns också via knappen `…` i primitivens verktygsfält i vyn.

![](/images/topology_primitive_screenshot.webp)
