# ![](/icons/multires.webp) Topologi {#topology}

Den här menyn styr topologin för objekt i Nomad, samt verktyg för att baka och överföra detaljer mellan objekt och mellan texturer.

![](/images/topology_overview.webp)

Nomad är baserat på polygoner, den använder trianglar och fyrkanter (quads) för att hantera geometrin.
Med topologi menar vi både antalet ytor men också hur punkter (vertices) är sammanlänkade.

Det är viktigt att hålla koll på topologin, särskilt om du vill skulptera eller måla in fina detaljer.

::: tip Hur håller man koll på sin topologi?
Du kan visa [Wireframe](settings.md#wireframe) eller helt enkelt inaktivera [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Topologimenyn i Nomad har flera sektioner:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Redigera flera detaljnivåer med hjälp av subdivision            |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Beräkna om en ny topologi med enhetlig densitet                 |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Lägg till/ta bort ytor lokalt i realtid vid skulptering eller målning |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimering, UV, baking, remeshing, reprojektion                 |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Primitive-alternativ                                             |


## Polygonstatistik {#polygon-stats}

![](/images/topology_stats.webp)

Den översta delen av topologimenyn visar polygoninformation för det valda objektet och hela scenen. Siffrorna visar totalt antal vertices, totalt antal trianglar och totalt antal quads (fyrsidiga polygoner).

Om du trycker på den här sektionen visas en lista med polygonstatistik för alla polygonobjekt i scenen.

## ![](/icons/multires.webp) Multiresolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### Vad är multiresolution? {#what-is-multiresolution}
Multiresolution-funktionen är användbar i två huvudsakliga scenarier:
- Den släta subdivision-algoritmen för att öka polyantalet på ditt objekt
- Hantera flera upplösningsnivåer så att du kan växla mellan små och stora ändringar

![](/videos/multiresolution.mp4)

#### Arbetsflöde för multiresolution {#multiresolution-workflow}
En viktig aspekt av multiresolution är att du kan gå tillbaka till en lägre upplösning, göra ändringar på ditt objekt och sedan gå tillbaka till den högsta upplösningen utan att förlora högupplösta detaljer. Alla högupplösta detaljer projiceras automatiskt.

::: warning
Om du använder ett verktyg som ändrar topologin på ditt objekt kommer du att förlora alla andra upplösningsnivåer på objektet!
Du bör alltid få en varning om detta kan hända, till exempel när du använder:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim-verktyget](tools.md#trim)
- [Split-verktyget](tools.md#split)
:::


### Multiresolution‑reglage {#multiresolution-slider}
Detta reglage visar antalet subdivisionsnivåer i det aktuella objektet. Om det finns 6 vertikala staplar finns det 6 subdivisionsnivåer. Cirkeln visar vilken subdivisionsnivå som visas.

### Ångra {#reverse}
När du är på den lägsta subdivisionsnivån försöker Reverse-knappen skapa en nivå under den aktuella. Observera att detta i allmänhet bara är möjligt om objektet skapades med subdivision från början, till exempel i Nomad eller i andra 3D-applikationer med multiresolution subdivision surfaces.

### Subdividiera {#subdivide}
Knappen *Subdivide* ökar antalet polygoner med 4, så se till att hålla ett öga på polyantalet eftersom det kan öka väldigt snabbt!
En viktig aspekt av *Subdivision Surface* är att de konvergerar mot en *Smooth Surface*.
För att förstå hur det fungerar kan du prova *Subdivide*-knappen på ett objekt med bara några få polygoner.

Du kan inaktivera detta *Smooth*-beteende genom att kryssa i alternativet `Linear subdivision`.

### Ta bort lägre {#delete-lower}
Om det finns subdivisionsnivåer under den aktuella nivån tas de bort. Om du gör detta av misstag kan du återskapa dem med Reverse-knappen.

### Ta bort högre {#delete-higher}
Om det finns subdivisionsnivåer över den aktuella nivån tas de bort.

### Linjär subdivision {#linear-subdivision}
Subdividera meshen utan att applicera smoothing.

### Skarp kant {#sharp-border}
Om ditt objekt har facegroups kommer aktivering av detta alternativ att hålla facegroup-gränser skarpa. Detta kan ställas in på varje subdivisionsnivå (subdivision-reglaget får en liten ikon ovanför nivån för att indikera detta).

### Behåll trianglar {#keep-triangles}
De flesta standardiserade subdivision surface-system försöker konvertera alla polygoner till quads under en subdivision-operation. Denna växel tvingar subdivision att använda trianglar i stället.

### Lås (LV0) {#lock-lv0}

Förhindra att den lägsta subdivisionsnivån ändras. Detta kan vara viktigt om ditt objekt genererades i en annan applikation och basobjektet måste förbli oförändrat. När detta alternativ är inaktiverat kommer stora ändringar på högre subdivisionsnivåer att flytta nivå 0.

::: tip 

Subdivision kommer som standard att jämna ut alla skarpa kanter. För att behålla kanter något skarpa kan du experimentera med att använda Linear subdivision eller Sharp border på de första 2 subdivisionsnivåerna och sedan stänga av det för de högre nivåerna. Detta skapar en halvskarp subdividerad mesh.

:::


## ![](/icons/voxel.webp) Voxel‑ommeshing {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
När du använder `Voxel Remesher` kommer hela meshen att tvinga topologin att ha en enhetlig upplösning, vilket innebär att alla polygoner har mer eller mindre samma storlek. Detta är mycket användbart när du inte vill tänka på topologi utan bara vill skulptera fritt.

Ett typiskt skulpteringsarbetsflöde kan börja med att använda `Voxel Remesher` för att blocka ut en grov form med låg upplösning.
Tryck helt enkelt på *Remesh*-knappen då och då när du sträcker meshen för mycket för att undvika för mycket distorsion.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Som nämnts ovan är Nomad ett polygonbaserat program, men `Voxel Remesher` är ett undantag där en annan metod används (tillfälligt) för att utföra remeshing.

En stor skillnad är att voxel-metoden inte accepterar självskärningar, så dessa kommer att lösas.
Den stöder inte heller mesher med hål i.

Med hål menar vi inte `genus hole` (`hålet` i en donut), utan i stället mesher som inte är `watertight`/`closed`.
Typiskt innebär det att innan remeshing appliceras kommer alla hål att fyllas, på liknande sätt som [Trim-verktyget](tools.md#trim) eller [Hole filling-funktionen](scene.md#hole-filling).
:::

### Remesh {#voxel-remesh}
Utför voxel-remesh.

### Upplösning {#voxel-resolution}
Storleken på voxlarna som används under beräkningen. När du ändrar denna parameter visas ett schackrutemönster över meshen för att ge en förhandsvisning av resultatet.

### Bygg multiresolution {#build-multiresolution}
Skapa lägre multiresolution-nivåer för voxel-remeshen. Om du använder schackrutemönstret för att ställa in en upplösning och sätter Build multiresolution till 2, kommer slutresultatet att ha detaljer som matchar resolution-reglaget, och om du går till multires-fliken kommer det att vara på nivå 2, vilket betyder att du har lägre upplösnings-multimesher på nivå 1 och nivå 0. Detta kan vara ett bra sätt att både generera en ren mesh med jämna polygoner och ha en lågupplöst kontrollmesh.

::: tip Tip: Build multiresolution och stable smoothing

Detta alternativ kan ibland orsaka ”loopar” i geometrin som kan vara svåra att jämna ut, vilket orsakar små ”finnar”. Om detta händer, aktivera 'Stable smoothing' i smooth-verktygets alternativ. 

:::

### Behåll skarpa kanter {#keep-sharp-edges}
Aktivera snappning av de nya punkterna till skarpa kanter på den ursprungliga meshen. Det kan introducera distorsion.

## ![](/icons/dynamic.webp) Dynamisk topologi {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution och voxel-remeshing är vanliga metoder i branschen för att kontrollera topologi, men båda kräver att du ser till att du inte sträcker polygoner för mycket eller pressar ihop dem för hårt. 

Dynamic Topology är en alternativ metod. När du skulpterar kommer Nomad adaptivt att lägga till och ta bort polygoner under penseldraget, så att inristning av små detaljer lägger till många små polygoner där du behöver dem, och smoothing på andra ställen tar bort polygoner.

Observera att Dynamic Topology använder triangulära polygoner i stället för quads. Detta kan se lite rörigt ut, men det är nästan bättre att inte titta på wireframen, utan bara fokusera på att göra en snygg skulpt utan att oroa dig för topologi, och senare kan du använda något av Nomads andra remeshing-verktyg för att generera en ren quad-mesh.

Se videon nedan i aktion.

![](/videos/dynamic.mp4)

### Aktiverad {#enabled}
Slå på Dynamic Topology. En DynTopo-ikon placeras under reglagen för penselradie och intensitet så att du kan slå av/på Dyntopo per verktyg.

### Detalj {#dyn-detail}
Styr detaljnivån, dess beteende ändras baserat på valet 'Detail based on...', se nedan.

### Detalj baserad på... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Detaljnivån beror på hur stor objektet är på skärmen. Detail-reglaget är 100 % eller högre för fin detalj (små trianglar) eller 1 % för låg detalj (stora trianglar).  |
| Radius   | Penselradien definierar detaljnivån. Använd en liten penselradie för fin detalj, en stor penselradie för låg detalj. Detail-reglaget är en multiplikator på detta förhållande.                     |
| Constant | Detail-reglaget definierar detaljnivån och påverkas inte av skärmstorlek eller penselstorlek.             |

::: tip TIP: Radius-läge

För att få en bättre känsla för hur Radius-läget fungerar, börja flytta Detail-reglaget med ett finger och ändra samtidigt penselradien med ett annat finger. Du kommer att se hur de hänger ihop.

:::

### Föredra... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Prioritera prestanda |
| Quality | Prioritera kvalitet |

När du prioriterar `Quality` är de två huvudsakliga skillnaderna:
- förfining appliceras innan skulptering, så du får färre interpoleringsartefakter när du målar eller skulpterar mycket små detaljer
- förfining körs tills den konvergerar till rätt detaljnivå, i kontrast till ett inkrementellt beteende.
 
På så sätt kommer topologin alltid att förfinas som förväntat om du skulpterar mycket små detaljer eller gör snabba drag.


### Använd tryck på radie {#use-pressure-on-radius}
Endast relevant om `Radius` är aktiverat. När det är aktiverat kommer detaljnivån alltid att spegla penselstorleken, även när penselstorleken påverkas av pennttryck.

### Använd penselövergång {#use-stroke-falloff}

Inkludera även penselns falloff-kurva och alfa i dyntopo-beräkningarna.

### Metod {#method}
Oavsett om du använder `Dynamic Topology` på din [Brush](#brush) eller [Globalt](#global), kan du välja i vilket läge den ska fungera:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Den kan lägga till och ta bort ytor, detta är läget som används i videon ovan |
| Subdivision    | Lägger bara till nya ytor, kan inte ta bort ytor                     |
| Decimation     | Tar bara bort ytor, kan inte lägga till ytor                         |

### Skydda maskerat område {#protect-masked-area}
Aktivera så att maskerade områden skyddar topologin från att ändras.

### Vertex‑extrapolering {#vertex-extrapolation}


### Detalj {#all-detail}
Upplösningen som används för remesh-operationen. Om Dyntopo är i 'Constant'-läge kommer det att vara samma värde som Detail-reglaget högst upp i denna meny.

### Remesh {#dyn-remesh}
Utför en global remesh med dyntopo-algoritmen. Vanligtvis bör du använda [Voxel Remesher](#voxel-remesher) för full remeshing.

En fördel jämfört med voxlar är dock att det maskerade området skyddas, så du kan ha bättre kontroll över var du vill ha mer eller mindre densitet.



## ![](/icons/topo_extra.webp) Diverse {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Kugghjulsmeny {#gear-menu}
Många av verktygen i denna meny har extra alternativ. De kan nås via kugghjulsikonen bredvid sektionsrubriken.

### Decimering {#decimation}

![](/images/topology_decimation.webp)

Minska antalet polygoner genom att försöka behålla så mycket detaljer som möjligt, med triangulära polygoner.

Denna funktion kan vara användbar om du vill exportera för 3D-utskrift.
Du bör dock troligen inte använda den om du vill fortsätta skulptera på objektet, eftersom den kan producera ojämna trianglar.

Observera att maskerade områden inte kommer att decimeras.

![](/videos/decimate.mp4)

::: tip

Att använda [Quadremesh-verktyget](tools.md#quad-remesher) på högupplösta objekt kan ta lång tid att beräkna och ge resultat som är svåra att kontrollera. Förbehandling av meshen med [facegroups](tools.md#facegroup-1) och decimate gör att Quadremesh kör mycket snabbare och ger mycket mer kontroll över topologin.

* Facegroupa meshen för att definiera ditt ideala quad-flöde.
* Facegroup relax för att få släta facegroup-gränser.
* Decimate. Detta säkerställer att du inte har tunna eller förvrängda ytor på facegroup-kanten. I decimate-inställningarna, se till att facegroup är aktiverat. Detta gör att triangelkanter följer dina facegroup-kanter exakt.
* I Quadremesh-alternativen, se till att relax är inaktiverat (eftersom du redan har relaxat meshen) och du bör få bra resultat.

:::

#### Decimera {#decimate}
Starta decimate-operationen.

Ikonerna bredvid Decimate-knappen låter dig slå av/på alternativ som påverkar decimeringen. Procenttalet anger hur starkt alternativet är och kan ställas in i den avancerade gear-menyn.

* ![](/icons/palette.webp)  `Preserve Painting` - Placera fler trianglar där det finns målningsdetaljer.
* ![](/icons/triforce.webp) `Uniform Faces` - Föredra att skapa jämnstora trianglar.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate försöker hålla kanter nära öppen geometri och hål oförändrade.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate försöker hålla facegroup-gränser oförändrade.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Decimate försöker hålla UV-gränser oförändrade.

#### ![](/icons/cog.webp) Kugghjulsmeny för decimering {#decimate-gear-menu}
Gear-menyn har dessa avancerade alternativ:
##### Bevara målning {#preserve-painting}
Kryssrutan slår av/på detta läge, värdet avgör hur noggrant målningsdetaljer bevaras. Högre värden bevarar mer målning. Sätt till 0 om du inte bryr dig om målningen.


##### Enhetliga ytor {#uniform-faces}
Kryssrutan slår av/på detta läge. Högre värden ger trianglar med liknande storlek.

##### Bevara kanter {#preserve-borders}
Aktivera för att förhindra att kanter decimeras. Border-vikter kan väljas för `Geometry`-, `Face Group`- eller `UV`-kanter.

#### Måltal trianglar {#target-triangles}
Ställ in målantalet trianglar. Standardvärdet är 50 %, knappen percent/target växlar mellan en procentandel eller ett exakt målantal polygoner.



### UV‑Unwrap – UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Beräkna texturkoordinater (UV) för den aktuella meshen, generellt med preferens för att skapa fler öar med snitt för att minimera distorsion.

Det lilla öga-ikonen mellan menyrubriken och gear-menyn växlar förhandsvisning av UV:er på objektet.

![](/videos/unwrap.mp4)

#### Unwrap {#unwrap}
Beräkna UV för det valda objektet, som visas i bakgrunden.

#### Ta bort UV {#delete-uvs}
Ta bort UV på objektet.

#### ![](/icons/cog.webp) UVAtlas kugghjulsmeny {#uvatlas-gear-menu}
Gear-menyn har dessa avancerade alternativ:

#### Ytgrupp {#atlas-face-group}

Använd facegroups för att definiera snitten för UV:erna.

##### Maximal tänjning {#max-stretch}
Låga värden skapar mindre distorsion och fler öar, höga värden skapar mer distorsion och färre öar. 

##### Öavstånd {#island-spacing}
Mängden padding mellan öarna. Låga värden slösar mindre utrymme men riskerar att texturer blöder mellan öarna. 

::: warning
Beräkning av UV kan ta lite tid, det är bäst att ha en mesh med färre än 100k vertices.
:::

::: tip UVs?
En vanlig analogi för UV är att slå in ett paket; vad är det bästa sättet att klippa presentpapper för att helt täcka ett objekt utan överlappningar? 

UV är liknande, men i stället för att klippa pappret klipper du objektet. Föreställ dig att din modell är gjord av tunn plast, hur skulle du klippa isär modellen för att veckla ut den platt, måla på den i det platta tillståndet och sedan sätta ihop den igen?

Föreställ dig nu att ytan på din modell är gjord av stretchigt lycra. Du skulle kunna sträcka modellen platt, eller klippa den, eller en kombination av båda. Men om du målade ett schackrutemönster på objektet när det var utplattat skulle schackrutorna vara förvrängda när du satte ihop det igen. Vilken metod är bättre, fler snitt med mindre distorsion eller färre snitt med mer distorsion?

UV är instruktioner som talar om för 3D-programvara hur man ska ”klippa och sträcka” objektet när texturer appliceras. UV Atlas-verktyget använder generellt ett tillvägagångssätt med ”fler snitt, mindre distorsion”.


:::

::: tip UV och Nomad och andra appar

De flesta texturerade modeller du hittar online är texturerade med UV. Nomad kan importera och visa detta via [materialpanelen](material#textures).

När modeller skapas i Nomad kan du måla direkt på objekt utan UV. Om du behöver exportera dem till andra appar, t.ex. [Procreate](https://procreate.art/), kan du ”baka” Nomad-färginformation till texturer via UV. 

:::

### UV‑Unwrap – BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF-UV föredrar ett tillvägagångssätt med ”färre snitt, mer distorsion”. 

#### ![](/icons/cog.webp) UV BFF‑kugghjulsmeny {#uv-bff-gear-menu}

#### Ytgrupp {#bff-face-group}

Använd facegroups för att definiera snitten för UV:erna.

##### Konantal {#cone-count}
Definiera antalet huvudsakliga projektioner som används. Lägre värden ger färre öar men mer distorsion.

##### Sömlösa patchar {#seamless-patches}
Påverkar layouten av UV-patcharna, fungerar bäst med noggrant skapade facegroups.

### Baka -> textur {#bake-texture}
![](/images/topology_bake_menu.webp)

Texture baking skapar texturer genom att projicera andra synliga objekt i scenen in i UV:erna på det valda objektet.

Här är ett typiskt arbetsflöde för baking:
- Du har en mesh med fina detaljer och målning
- Klona den
- Decimate den (sätt `Preserve painting` till 0)
- UV-unwrappa den
- Baka!

Nomad tar som standard hänsyn till alla synliga mesher i scenen.
Du kan också använda Solo-läget för att snabbt dölja de flesta andra mesher.
Om det inte finns några andra synliga objekt kommer hela scenen att tas med i beräkningen.

Du bör nu ha en lågupplöst mesh som behåller det mesta av färgen och detaljerna från ditt tidigare objekt.

Efter operationen flyttas vertex-färger till ett nytt inaktiverat lager så att de inte stör texturerna.

#### Från sig själv {#tex-from-itself}
Baka den högsta multiresolution-nivån till den lägsta nivån på det aktuella objektet. Detta är enkelt att ställa in, men ofta behöver du mer kontroll, i vilket fall nästa alternativ är mer användbart.

#### Från högupplöst () {#tex-from-high-res}
Baka från de andra synliga objekten i scenen till det valda objektet. Siffran inom parentes anger antalet andra synliga objekt som kommer att användas som högupplösta mål och bakas in i det aktuella lågupplösta objektet med UV. De andra objekten behöver inte vara liknande i layout eller topologi som objektet som bakas, vilket möjliggör flexibla bake-arbetsflöden.

#### Upplösning {#tex-bake-resolution}
Upplösningen på den bakade texturen. Bake-texturer är alltid kvadratiska, så 1024 skapar en 1024x1024-bild. 

Knapparna nedan är genvägar för vanliga upplösningar. Som referens är 512x512 relativt litet, t.ex. för webb-grafik och enkel geometri. 4096x4096 (4k) är för högkvalitativa renderingar.

#### ![](/icons/cog.webp) Baka‑kugghjulsmeny {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Gear-menyn har dessa avancerade alternativ:

##### Normal, Roughness, Metalness, Färg, Emissiv, Opacitet {#tex-normal-roughness-metalness-color-emissive-opacity}
Dessa kryssrutor avgör vilka egenskaper som bakas, var och en till separata kartor. När bakningen är klar läggs dessa till som texturer i materialet på det aktuella objektet.

##### Säkerhetskopia {#tex-backup}
För att förhandsvisa de bakade texturerna bör objektets målningsinformation inaktiveras. Detta alternativ överför all målningsinformation till ett nytt lager som backup så att det enkelt kan aktiveras/inaktiveras.

#### Bur‑radie {#tex-cage-radius}
Justera hur långt bort från bake-objektet strålar skickas för att leta efter målobjekt. Som standard hålls detta avstånd lågt för att undvika artefakter, men kan ökas om målobjekten är långt från bake-objektet.

##### Strål‑offset {#tex-ray-offset}
Justera var bake-beräkningarna startar på bake-objektet. Som standard startar de 5 % bort från ytan, vilket undviker de vanligaste artefakterna. Om målobjekten är mycket långt från bake-objektet kan denna offset behöva ökas.


### Projektera om till vertex {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projicera skulpterade detaljer, målning, lager, texturer till vertex-värden.

Det kan ses som motsatsen till baking; om baking överför vertex-egenskaper till texturer, överför reproject texturer (och andra egenskaper)
 tillbaka till vertices.

::: tip
När du använder `Bake to texture` eller `Reproject to vertex` tas både vertex-färger och materialtexturer med i beräkningen.
:::

#### Från sig själv {#vertex-from-itself}
Konvertera texturer från materialet till vertex-värden. Denna knapp är bara aktiv om objektet har UV och texturer är aktiva i materialet.

::: tip TIP: Texture painting
Nomad stöder inte direkt målning och redigering av texturer, men mycket liknande resultat kan uppnås genom att projicera texturer -> vertex-värden, måla på vertices och sedan baka vertex -> texturer:

1. Ställ in ett lågpoly-objekt med UV
1. Ladda texturer i dess material
1. Subdividera det tillräckligt för att kunna måla på det
1. `Reproject to vertex` i läget `From itself`, nu har texturen konverterats till vertex-värden
1. Måla, jämna, smeta, stämpla, gör vilka ändringar du behöver
1. `Bake to texture` i läget `From itself`. Dessa ändringar konverteras tillbaka till texturer.
:::

#### Från högupplöst () {#vertex-from-high-res}
Konvertera alla synliga objekt till vertex-värden på det valda objektet. Siffran på denna knapp anger antalet synliga objekt.

::: tip
Reprojektion av andra objekt kan användas inte bara för att överföra färginformation från andra objekt, utan också för att projicera vertices på andra objekt, t.ex. kan bandage projiceras på en karaktär.
:::

#### ![](/icons/cog.webp) Omsprojekterings‑kugghjulsmeny {#vertex-reproject-gear-menu}
Gear-menyn har dessa avancerade alternativ:

#### Vertices, Roughness, Metalness, Färg, Opacitet, Opacitet->Mask, Mask, Lager, Ytgrupp {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Dessa kryssrutor avgör vilka egenskaper som projiceras till det valda objektet. 

#### Relax {#vertex-relax}
Den valda meshen kan få sin layout jämnad eller relaxad en viss mängd för att bättre passa reprojektionsmålen. Smooth är bättre för högupplösta mesher. Relax är bättre för lågupplösta mesher. Auto låter Nomad avgöra bästa metod.

#### Iterationer {#vertex-iterations}
Hur många gånger relax-operationen ska appliceras under reprojektionen.

#### Bur‑radie {#vertex-cage-radius}
Justera hur långt bort från det valda objektet strålar skickas för att leta efter målobjekt. Som standard hålls detta avstånd lågt för att undvika artefakter, men kan ökas om målobjekten är långt från bake-objektet.

#### Strål‑bias {#vertex-ray-bias}
Lägre värden prioriterar projektion till närmaste punkt på målobjektets yta. Högre värden prioriterar en skärningspunkt med hjälp av ytans normal. 

#### Strål‑offset {#ray-vertex-offset}
Justera var bake-beräkningarna startar på det valda objektet. Som standard startar de 5 % bort från ytan, vilket undviker vissa artefakter. Om målobjekten är mycket långt från bake-objektet kan denna offset behöva ökas.


### Quad Remesh – Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remesha med [Instant Meshes-algoritmen av Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Den analyserar flödet i en mesh och skapar ren quad-topologi.

::: tip
På iOS och desktop ger [Quad remesher](tools#quad-remesher)-verktyget bättre resultat och mer kontroll.
:::

#### Remesh {#instant-remesh}
Starta Instant Meshes-operationen.

#### Måltal fyrkanter {#target-quads}
Antalet quad-polygoner som Quad Remesh försöker skapa.

#### ![](/icons/cog.webp) Quad Remesh Instant‑kugghjulsmeny {#quad-remesh-instant-gear-menu}
Gear-menyn har dessa avancerade alternativ:

##### Vinkel för kantbrytning {#crease-angle}
En tröskel för skarpa hörn som försöker hjälpa till att styra remesh-operationen.

#### Max fyllnadshål {#max-fill-hole}
Algoritmen kan ibland skapa oönskade hål. Om ett hål har färre vertices än detta värde fylls det.

### Hål {#holes}
![](/images/topology_holes_menu.webp)
För det mesta kommer ditt objekt troligen att vara watertight, vilket betyder att meshen är ”sluten”.

Om ditt objekt har hål kan du fylla dem. Observera att det bara fungerar på ”naiva” hål, så det kan inte ”svetsa” två separata kanter.

![](/videos/hole_filling.mp4)

::: tip
När du kör Voxel Remesher stängs alla hål automatiskt, oavsett om du använder den på ett eller flera mesher.
:::

#### Stäng hål {#close-holes}
Utför åtgärden för att stänga hål.

#### ![](/icons/cog.webp) Hål‑kugghjulsmeny {#holes-gear-menu}
Gear-menyn har dessa avancerade alternativ:

##### Detalj {#fill-detail}
Polygondensiteten som används för att fylla hålet. När du drar i detta reglage visas ett schackrutemönster på modellen, vilket ger en indikation på triangelstorleken som ska användas. Kryssrutan inaktiverar detta och använder bara befintliga punkter, vilket vanligtvis skapar långa tunna trianglar över hålet, som kan vara svåra att skulptera.

##### Fyll icke‑manifold {#fill-non-manifold}
Försök fylla non-manifold-hål.

##### Ytgrupp {#fill-face-group}

När hål fylls, ska varje hål få sin egen facegroup (Auto), eller ska de alla dela en facegroup (Off), eller ska inga facegroups skapas (On).

### Tvinga manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Försök att rensa non-manifold-kanter. Det kan vara användbart för extern programvara som inte stöder kanter som har mer än 2 ytor gemensamt.

#### Rensa {#clean}
Utför Clean-åtgärden.
#### ![](/icons/cog.webp) Tvinga manifold‑kugghjulsmeny {#force-manifold-gear-menu}
Gear-menyn har dessa avancerade alternativ:

#### Ta bort små ytor {#delete-small-faces}
En tröskel som används för att ta bort och slå ihop små polygoner.


### Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Konverterar meshen till en [triplanar](scene.md#triplanar)-primitiv.
Du kommer sannolikt att förlora mycket detaljer i processen.

#### Tvinga kubisk {#force-cubic}
Tvinga triplanaren att vara en kub. Annars anpassas triplanaren till den närmaste bounding box runt ditt objekt.

#### Konvertera {#convert}
Utför triplanar-åtgärden.

#### Upplösning {#triplanar-resolution}
Voxelstorleken som används i triplanar-operationen.

## ![](/icons/dot.webp) Primitiv {#primitive}
Parametrar för den valda primitivformen. Dessa finns också i primitivens verktygsrad i vyn.

![](/images/topology_primitive_screenshot.webp)