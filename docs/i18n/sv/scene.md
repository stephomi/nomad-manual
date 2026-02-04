# ![](/icons/scene.webp) Scen {#scene}

Den här menyn låter dig hantera objekt, ljus, kameror och upprepare i Nomad. Den visar scenernas hierarki som en trädvy, vilket gör att du kan ändra många aspekter av dina objekt. Den låter dig också skapa nya objekt samt kombinera och dela upp objekt på olika sätt.


![](/images/scene_menu_summary.webp)


## Genvägspanel {#shortcut-bar}
| Åtgärd                | Ikon                              | Beskrivning                                                                                                        |
| :-------------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| [Lägg till...](#add-menu) | ![](/icons/plus.webp)            | Visa [Lägg till-menyn](#add-menu) för att lägga till ett objekt i scenen                                           |
| Ta bort               | ![](/icons/trash.webp)           | Ta bort objektet                                                                                                   |
| Lås                   | ![](/icons/lock.webp)            | Gör objektet icke-valbart i vyn. Det kan fortfarande väljas från trädvyn.                                          |
| Sammanfoga            | ![](/icons/merge.webp)           | Slå ihop de markerade objekten till ett enda objekt utan geometriändringar                                        |
| Separera              | ![](/icons/diagonal.webp)        | Om ett objekt består av separata polygon-skal, dela upp det i separata objekt. Motsatsen till sammanfogning        |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Visa [Boolean](#boolean)-menyn                                                                                     |
| Klona                 | ![](/icons/clone.webp)           | Duplicera objektet till ett nytt objekt                                                                            |
| Instans               | ![](/icons/link.webp)            | Duplicera objektet som en instans, så att modelländringar på ett påverkar alla instanser                          |
| Av-instansiera        | ![](/icons/unlink.webp)          | Konvertera en instans till en unik form, så att modelländringar inte längre kopieras till andra instanser         |
| Synka                 | ![](/icons/link.webp)            | Om instanser har barn, se till att alla instanser delar samma barnhierarki                                        |


## Trädvy {#tree-view}
![](/images/scene_treeview.webp) 

| Åtgärd      | Ikon                       | Beskrivning             |
| :---------: | :------------------------: | :---------------------: |
| Välj        | ![](/icons/checked.webp)  | Växla vald/ej vald      |
| Synlig      | ![](/icons/eye_open.webp) | Växla synlighet         |
| Meny        | ![](/icons/more.webp)     | Visa objektmeny         |

::: tip TIPS: Snabbt välja eller dölja många objekt

Tryck på välj-ikonen för att växla ett enskilt objekt, eller dra vertikalt i välj-kolumnen för att välja många objekt. Samma sak kan göras med synlighetskolumnen.

:::

### Trädvymanipulation {#tree-view-manipulation}

Håll ned på ett objekt i trädvyn tills det blir gult. Du kan sedan flytta det upp eller ner i trädvyn, samt dra det över ett annat objekt för att göra det till barn till det objektet.

När många objekt är markerade kommer de flesta vara mörkgula, ett kommer vara ljusare gult. Håll ned och dra på det ljusare objektet för att flytta alla objekten samtidigt.

När du väljer ett föräldraobjekt kommer som standard alla barnobjekt också att väljas. Genom att trycka på föräldraikonen växlar du mellan att välja bara föräldern, eller föräldern och barnen.

### Objektmeny {#object-menu}

Genom att klicka på ellipsknappen (...) för ett objekt i trädvyn visas objektmenyn. 
Många av dessa alternativ liknar genvägsraden högst upp, upprepade för bekvämlighet.

|       Åtgärd        |                        Ikon                        | Beskrivning                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instans        |               ![](/icons/link.webp)            | Duplicera objektet som en instans, så att modelländringar på ett påverkar alla instanser.                                                                              |
|        Klona        |              ![](/icons/clone.webp)            | Duplicera objektet till ett nytt objekt                                                                                                                                 |
|        Namn         |              ![](/icons/pencil.webp)           | Ändra objektets namn                                                                                                                                                    |
|       Ta bort       |              ![](/icons/trash.webp)            | Ta bort objektet                                                                                                                                                        |
|      Ta bort+       |            ![](/icons/removeNode.webp)         | Ta bort objektet och dess barn                                                                                                                                          |
|    Av-instansiera   |              ![](/icons/unlink.webp)           | Konvertera en instans till en unik form, så att modelländringar inte längre kopieras till andra instanser.                                                             |
| Separera topologi   |             ![](/icons/separate.webp)          | Om ett objekt består av separata polygon-skal, dela upp det i separata objekt. Motsatsen till sammanfogning.                                                           |
| Separera Face Group |            ![](/icons/faceGroup.webp)          | Om ett objekt har flera face-grupper, dela upp meshen i separata objekt.                                                                                                |
|   Separera lager    |              ![](/icons/layer.webp)            | Om ett objekt har lager, dela upp varje lager till ett separat objekt. Användbart för att skicka blendshapes till andra applikationer.                                 |
|   Sammanfoga -> Lager   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Om flera objekt är markerade och har matchande topologi, slå ihop dessa objekt till lager för huvudobjektet (de andra objekten tas bort). Återigen användbart för blendshapes som KOMMER FRÅN andra applikationer.<br><br> Observera att lagren är inaktiverade som standard. Aktivera dem om du behöver justera deras reglage. |




### Flerselektion {#multiselection}
Du kan välja flera objekt för att uppnå två saker:
- använda gizmo-verktyget för att flytta flera objekt samtidigt
- slå ihop objekt med sammanfognings- och boolean-operationer.

Du kan göra detta genom att använda kryssrutan `Multiselection` och sedan klicka på objekten i listan.

::: tip Snabb multiselektion
Du kan också multivälja i vyn genom att hålla ned genvägen `Smooth` och trycka på en annan mesh.

Du kan avmarkera ett objekt genom att trycka på det igen (endast om din markering innehåller mer än ett objekt).
:::

::: warning Begränsad gizmo-funktion
När du använder multiselektion kommer gizmo-verktyget alltid att ignorera maskning.
Dessutom tas X/Y/Z-skalning bort.

Anledningen är att multiselektion endast tillåter transformation av hela mesh:en, inte per-vertex-transformation.
Detta kan förbättras i framtiden.
:::


## Förena {#join}
Detta alternativ skapar helt enkelt en enda objektpost från flera markerade objekt.

Du kan se ett exempel i video i avsnittet [Separera](#separate).

## Boolesk {#boolean}
![](/images/scene_boolean_menu.webp) 
Kombinera objekt till en enda yta.

`Voxel merge` behåller objektens volym och beräknar nya jämnt fördelade polygoner på ytan. På grund av beräkningssteget kan en voxel-sammanfogning hantera komplex geometri, men kan tappa fin detalj om målupplösningen inte är tillräckligt hög.

`Boolean` försöker lämna polygonerna i deras ursprungliga layout och sy ihop polygonerna där objekt överlappar. Detta kan ge mycket renare och skarpare resultat än en voxel-sammanfogning, men kräver "vattentäta" mesher; det får inte finnas hål eller felaktiga former i objekten. Om detta misslyckas fungerar vanligtvis en voxel-sammanfogning.

### Booleska operationer {#boolean-operations}
Både Voxel Merge och Boolean använder objektsynlighet för att styra operationen:

#### Union {#union}
Båda objekten synliga skapar en boolean-**union**, objektens yttre skal kombineras utan inre ytor. ![](/images/boolean_union.webp)

#### Subtrahera {#subtract}
Ett objekt osynligt = boolean-**subtraktion**, det osynliga objektet subtraheras från det synliga objektet. ![](/images/boolean_subtract.webp)

#### Skärning {#intersect}
Båda objekten osynliga = boolean-**intersektion**, skapa en ny form endast där de två objekten överlappar. ![](/images/boolean_intersect.webp)


### Voxel-sammanslagning knapp {#voxel-merge-button}
Genom att trycka på denna knapp utförs en voxel-sammanfogning på de markerade objekten. När den används på ett enda objekt kommer det att retopologiseras till jämnt fördelade polygoner, användbart när ett objekt har utdragna polygoner.

### Upplösning {#resolution}
Upplösningen på voxel-3D-rutnätet som används för beräkningen. När detta värde ändras läggs ett schackrutemönster över objektet för att förhandsvisa polygonstorleken.

### Bygg multiresolution {#build-multiresolution}
Skapa multiresolution-nivåer under din målupplösning. Så om din upplösning är 400 och bygg multiresolution är 3, får du en ny mesh med säg 296 000 polygoner, men det kommer att finnas 3 subdiv-nivåer lägre vid 74 000, 18 000, 4 000.

### Behåll skarpa kanter {#keep-sharp-edges}
Aktivera snappning av voxel-meshen till kanter. Detta fungerar bäst på enkla former.

### Boolesk knapp {#boolean-button}
Genom att trycka på denna knapp utförs en polygon-boolean-operation med hjälp av Manifold-biblioteket av Emmett Lalish. 


## Separera {#separate}
Om du har ett enda objekt baserat på flera icke-sammanhängande delar kan du dela upp detta objekt i flera objekt. 
Detta kan ses som motsatsen till [Enkel sammanfogning](#simple-merge).

![](/videos/merge_separate.mp4)


## Lägg till-meny {#add-menu}

![](/images/scene_addmenu_overview.webp)

Den här menyn skapar primitiv, grupper, kameror, uppreprare och ljus.

Primitiv är grundläggande formtyper som kan justeras med parametrar. När du har justerat primitivet efter dina behov "validerar" du det, vilket bakar ned dessa parametrar till en polygonmesh som kan skulpteras och målas. Ett primitiv kan inte få sina parametrar justerade efter att det har validerats.


![](/images/scene_addmenu_top.webp)

### På gizmo {#on-gizmo}
Aktivera att placera det nya primitivet där den nuvarande valda formen eller gizmon är. När det är inaktiverat placeras primitivet i scenens centrum.

### Välj gizmo {#select-gizmo}
Aktivera automatisk växling till gizmo-verktyget när ett nytt primitiv skapas. 

### Avancerat {#add-advanced}

Den här menyn låter dig ställa in din preferens för var nya primitiv, grupper och uppreprare ska skapas. De kan skapas på det valda objektet, vid världens origo eller vid gizmons position.


### UV:n {#uvs}
Aktivera UV:s på primitiv. UV:s (ofta kallade texturkoordinater) är extra data som används i 3D för att tillåta texturer att appliceras på ytor. De tar upp mer minne, men för de flesta enheter bör detta inte vara ett problem om du inte når väldigt höga polyantal (t.ex. 10 miljoner polys eller mer). 

### Primitiver {#primitives}

| Primitiv      | Ikon                                      | Beskrivning                                                                                                      |
| :-----------: | :---------------------------------------: | :--------------------------------------------------------------------------------------------------------------: |
| Box           | ![](/icons/cube.webp)                    | En enkel kub, du kan styra indelningen i X, Y och Z                                                              |
| Sphere        | ![](/icons/circle.webp)                  | För enkelhetens skull kallas den Sphere men det är egentligen en subdividerad box, med `Project on sphere` tvingad |
| Cylinder      | ![](/icons/cylinder.webp)                | Du kan lägga till ett centralt hål för cylinder-primitivet, till exempel för att göra ett ihåligt rör           |
| Torus         | ![](/icons/torus.webp)                   | Torus kan vara en bra utgångspunkt för ringar                                                                    |
| Cone          | ![](/icons/cone.webp)                    | -                                                                                                                |
| Icosahedron   | ![](/icons/icosahedron.webp)             | -                                                                                                                |
| UV-sphere     | ![](/icons/circle.webp)                  | En sfär med ojämn poly-layout, se [Varning nedan](#uv-sphere)                                                    |
| Plane         | ![](/icons/rectangle.webp)               | En enkel plan yta, observera att detta är det enda primitivet som inte är slutet                                |
| Tube          | ![](/icons/tool_tube.webp)               | se [Tube](tools#tube)                                                                                            |
| Lathe         | ![](/icons/tool_lathe.webp)              | se [Lathe](tools#lathe)                                                                                          |
| Triplanar     | ![](/icons/triplanar.webp)               | se [Triplanar](#triplanar)                                                                                       |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | se [Shadow Catcher](#shadow-catcher)                                                                            |
| Head          | ![](/icons/face.webp)                    | Ett enkelt huvud med ett lager för att blanda mellan manligt/kvinnligt                                          |

::: tip
Om du undrar vad basmeshen är när du startar Nomad: detta är också en subdividerad box.
Dock använder basmeshen i Nomad inte `Project on sphere`, vilket betyder att den inte är perfekt rund.
:::

### Primtiv-verktygsrad {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

När ett primitiv har skapats visas en verktygsrad för att styra dess parametrar.

* `Validate` Baka primitivet till ett standardobjekt så att det kan skulpteras och målas.
* `Edit` Växla visning av primitivets gizmo. Den visas direkt på primitivet för att styra dess parametrar, t.ex. kubens bredd eller cylinderhålets radie.
* `Mirror` Växla placering av en spegel-uppreprare ovanför primitivet.
* `...` Visar primitiv-menyn.

Olika primitiv har extra alternativ på verktygsraden:

* `Project` Sfären konstrueras som en subdividerad kub, eftersom detta är bättre för skulptering, men det innebär att den inte är perfekt rund. Detta alternativ tvingar formen närmare en perfekt sfär. Icosahedron delar detta alternativ.
* `Cap` Växla ändlock på en form, t.ex. kan en cylinder ha lock upptill, nedtill, både och eller inga.
* `Hole` Växla om ett hål ska skapas genom mitten av en form. Detta växlar mellan inga hål, hål med en enda radie eller hål med olika radie upptill och nedtill.
* `Radius` Växla om en cylinder ska ha en enda radie eller olika radier upptill och nedtill.
* `Disk` Växla om en plane ska vara en fyrsidig form eller en cirkelform.

Den lilla verktygsraden under huvudverktygsraden låter dig växla mellan primitiv-gizmo och transform-gizmo.

::: tip

Genom att klicka på titeln på verktygsraden växlar du den till toppen eller botten av skärmen. Genom att klicka på pilen i hörnet fälls den ihop.

:::


### Primitiv-meny {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Den innehåller alla parametrar för det valda primitivet. Parametrar är grundbeskrivningar för en form. För att beskriva en ring skulle du till exempel beskriva dess yttre radie, dess inre radie och antalet polygoner.

De flesta primitivparametrar bör vara självförklarande, och det finns några vanliga parametrar som delas mellan alla primitiv:

* `UVs` Den lilla UV-knappen högst upp i menyn växlar skapandet av UV-koordinater
* `Validate` Den lilla validate-knappen bakar primitivet till ett standardobjekt så att det kan skulpteras och målas.
* `Max faces` Ställ in en övre gräns för antalet polygoner i objektet för att undvika att krascha din enhet.
* `Post subdivision` Aktivera det valda antalet subdivisioner från multiresolution-avsnittet i topologimenyn. Detta kan användas för att göra släta, mjukhörnade primitiv i kombination med låga topologiindelningar. Till exempel, om du ställer in en box-topologiindelning till 2 och post-subdivisioner till 4, får du en box med mjuka hörn.
* `Linear subdivision` Ställ in hur många nivåer av linjär subdivision som ska användas innan vanlig smooth-subdivision används. Detta kan användas för att styra hur skarpa eller mjuka hörnen är på de subdividerade ytorna. T.ex. ställ in en box-topologiindelning till 2, post-subdivisioner till 4 och prova sedan att ändra de linjära subdivisionerna mellan 0 och 4. Boxens hörn går från mjuka till skarpa.

### Topologi {#topology}

Detta styr antalet polygoner i ett primitiv. Vanligtvis är kontrollerna länkade, så att ändring av den aktiva reglaget justerar alla polygoner jämnt. Du kan trycka på avlänkningsknappen och styra X/Y/Z-indelningarna på en form separat.

### Geometri {#geometry}

Detta styr den övergripande storleken på ett primitiv, i X/Y/Z-enheter för fyrkantiga former och i radie för runda former.


### UV-sfär {#uv-sphere}
::: warning
UV Sphere är inte särskilt lämpad för skulptering, särskilt inte vid polerna.

Använd hellre primitivet [Sphere](#sphere), [Box](#box) eller [Icosahedron](#icosahedron) tillsammans med alternativet `Project on sphere`.

Observera att topologin kan vara acceptabel för skulptering om du använder ett mycket lågt värde för reglagen `Division`.
Du kan sedan använda reglaget `Overall Subdivision` för att öka antalet polygoner.

Även om den inte är lämplig för allmän skulptering är den användbar för ögon; om du roterar sfären så att polerna hamnar vid pupillen kommer polygonlayouten naturligt att passa för att måla och skulptera iris och pupill.
:::


### Triplan {#triplanar}
Detta primitiv är speciellt genom att du bör använda [Masking-verktyget](tools.md#mask) på det för att forma geometrin.

![](/videos/triplanar.mp4)


::: tip
Dubbeltryck på en plane så fokuserar kameran på just den planet.
Detta fungerar dock inte om du roterar primitivet med gizmon.
:::

Triplanar använder maskinformationen från 3 plan för att fylla ett voxel-rutnät som sedan polygoniseras (tack vare [Voxel Remesher](topology.md#voxel-remeshere)).

Varje plan har sitt eget symmetriplan.

::: warning
Varje gång du uppdaterar storleken på Triplanar-primitivet försämras kvaliteten på maskmålningen.

För närvarande finns det inget alternativ för att "låsa" målningen på ett enda plan, men det kan komma i framtiden.
Du kan använda [Connected Topology](stroke.md#connected-topology) för att hjälpa lite, i den meningen att om din markör ligger exakt på ett plan påverkar den inte de andra planen.
:::

### Skuggfångare {#shadow-catcher}
Lägg till en plane med Shadow Catcher-materialet. Se [Shadow Catcher-material](material.md#shadow-catcher) för mer detaljer. 


## Grupp/Kamera {#groupcamera}
### Grupp {#group}
Skapa ett "tomt" objekt som du kan göra andra objekt till barn under. Detta kan användas för att helt enkelt organisera hierarkin genom att lägga många objekt under en grupp och sedan stänga den. En grupp kan också användas som hjälp för att flytta objekt; många objekt kan placeras under en grupp och sedan kan gruppen flyttas, roteras och skalas med gizmo-verktyget.

### Lägg till vy {#add-view}
Skapa en kamera.

## Repeater {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Uppreprare är noder som skapar instanser av objekt under dem. 

### Array {#array}
![](/images/scene_primitive_array.webp)

När objekt görs till barn till denna nod kan de instansieras i ett rutnätsmönster. När den är vald har den kontroller för:
* Fit inside – växla mellan att styra storleken på arrayens rutnät/box eller att styra avståndet mellan array-instanserna
* CountX/Y/Z – antalet instanser på varje axel
* OffsetX/Y/Z – avståndet mellan instanserna när fit inside är aktiverat
* SizeX/Y/Z – bredd/höjd/djup för hela array-rutnätet när fit inside är aktiverat.

### Kurva {#curve}
![](/images/scene_primitive_curve.webp)
Detta skapar en kurva, barn till denna nod upprepas längs kurvan. När den är vald har den kontroller för:
* Edit – tillåt att lägga till punkter på kurvan och flytta punkter på kurvan.
* Snap – snäpper kurvpunkter till annan geometri
* Align – roterar barnformer för att linjera i kurvans riktning
* Count – antalet instanser
* Closed – växla om kurvan ska sammanfoga början och slut eller vara en öppen kurva
* Radius – växla kontroller på varje kurvpunkt för att styra instansernas skala
* Twist – växla kontroller på varje kurvpunkt för att styra instansernas vridrotation 
* B-spline – växla om instanserna ska följa kurvan exakt eller använda B-spline-interpolering som ger mjukare resultat. 

### Radiell {#radial}
![](/images/scene_primitive_radial.webp)

Barn till denna nod instansieras i en cirkel. Flytta barnobjektet för att ändra radien på denna uppreprare. När den är vald har den kontroller för:
* RadialX/Y/Z – genom att välja dessa knappar ställer du in den radiella axeln och antalet instanser.



### Spegling {#mirror}
![](/images/scene_primitive_mirror.webp)

Barn till denna nod speglas över en axel. När den är vald har den kontroller för:
* Gizmo – aktivera transform-gizmon för att ställa in spegelns centrum. Den kan också roteras och skalas. När du är klar, tryck på gizmo igen för att visa standardkontrollerna.
* X/Y/Z – ställ in spegelplanet

Alla uppreprare har en `Validate`-kontroll som bakar resultatet av uppreparen och frågar hur bakningen ska utföras:
* Join children – instanserna slås ihop till ett enda objekt
* Keep instances – instanserna förblir instanser men har inte längre uppreparen som "förälder"
* Un-instances – instanserna konverteras till unika objekt

::: tip Tips: Kombinera uppreprare
Uppreprare kan göras till barn under varandra och flera objekt kan göras till barn till uppreprare, vilket leder till komplexa effekter.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tips: Upprepar-pivoter

Vissa uppreprare försöker auto-pivota barnobjekten, så även om du flyttar eller roterar dem med gizmo-verktyget rör de sig inte. Om du behöver åsidosätta detta beteende, infoga en grupp mellan uppreparen och barnet. Nu kan du flytta barnformen oberoende av uppreparen.
:::

## Ljus {#light}

![](/images/scene_primitive_light.webp)

### Riktat {#directional}
Skapa ett riktat ljus, en oändligt avlägsen ljuskälla som solen.

### Spot {#spot}
Skapa ett spot-ljus med kontroller för konbredd och mjukhet

### Punkt {#point}
Skapa ett punktljus

## Avancerat {#advanced}
### Fokusera på objekt {#focus-on-item}
Dubbelklicka på ett objekt i scenlistan för att centrera kameran på det objektet i 3D-vyn.

### Synkronisera synlighet {#sync-visibility}
Att använda ögonikonen påverkar alla markerade objekt. 

### Instans: Visa {#instance-show}
Visa en färgkapsel till vänster om scenlistan för att visa instanser.


### Ikoner {#icons}
Ställ in storlek och opacitet på grupp-, ljus-, kamera- och spegelikoner i vyn

### Hierarkilinjer {#hierarchy-lines}
Visa en linje mellan förälder och dess barn i vyn

## Nedre verktygsrad {#bottom-toolbar}
Dessa ikoner växlar synlighet för Grupp, Ljus, Kamera, Uppreprare och Hierarkilinjer i vyn.