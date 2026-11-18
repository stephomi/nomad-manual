# ![](/icons/scene.webp) Scen {#scene}

I den här menyn hanterar du objekt, ljus, kameror och repeterare i Nomad. Den visar scenens hierarki som en trädvy, där du kan ändra många egenskaper hos dina objekt. Här skapar du också nya objekt, och kan foga ihop och dela upp objekt på olika sätt.


![](/images/scene_menu_summary.webp)


## Genvägsfält {#shortcut-bar}
| Åtgärd                 | Ikon                              | Beskrivning                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Lägg till...](#add-menu) | ![](/icons/plus.webp)         | Visar menyn [Lägg till](#add-menu) för att lägga till ett objekt i scenen                                           |
| Radera                 | ![](/icons/trash.webp)           | Raderar de markerade objekten. Deras barn behålls.                                                                  |
| Lås                    | ![](/icons/lock.webp)            | Gör att de markerade objekten inte kan markeras i vyn. De kan fortfarande markeras i trädvyn. Låser du en grupp låses allt under den. Tryck igen för att låsa upp. |
| [Foga ihop](#join)     | ![](/icons/merge.webp)           | Fogar ihop de markerade objekten till ett enda objekt utan att ändra geometrin                                      |
| [Dela...](#separate)   | ![](/icons/separate.webp)        | Visar popup-fönstret [Dela](#separate) för att dela upp ett objekt i flera objekt. Motsatsen till att foga ihop     |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Visar popup-fönstret [Boolean](#boolean)                                                                       |
| Klona                  | ![](/icons/clone.webp)           | Duplicerar de markerade objekten till nya objekt                                                                    |
| Instans                | ![](/icons/link.webp)            | Duplicerar de markerade objekten som instanser, så att ändringar i formen på en av dem görs på alla instanser.      |
| Av-instans             | ![](/icons/unlink.webp)          | Gör om en instans till en egen unik form, så att ändringar i formen inte längre kopieras till de andra instanserna  |
| Synka                  | ![](/icons/checked.webp)         | När den är ikryssad gäller åtgärderna alla instanser av de markerade objekten, inte bara de markerade. Den finns bara när markeringen innehåller instanser. Fliken [Synka](#sync) i popup-fönstret `Avancerat` anger vilka åtgärder som följer den här kryssrutan. |

::: tip
När en åtgärd också påverkar de andra instanserna visas en liten länkikon på knappen.
:::


## Trädvy {#tree-view}
![](/images/scene_treeview.webp) 

Trädvyn listar scenens objekt, grupper, repeterare, ljus och kameror. Bredvid en mesh namn ser du dess antal vertexer, och en färgad lagerikon när den har lager. Varje rad har de här knapparna:

| Åtgärd       | Ikon                       | Beskrivning              |
| :----------: | :------------------------: | :----------------------: |
| Namn         | ![](/icons/pencil.webp)   | Byter namn på objektet. Om det är markerat byter alla markerade objekt namn på en gång, med ett nummer tillagt. Håll intryckt för att byta namn på det och dess barn. |
| Välj         | ![](/icons/checked.webp)  | Markerar eller avmarkerar |
| Synlig       | ![](/icons/eye_open.webp) | Visar eller döljer       |
| Meny         | ![](/icons/more.webp)     | Visar [objektmenyn](#object-menu) |

::: tip TIPS: Markera eller dölj många objekt snabbt

Tryck på markeringsikonen för att markera eller avmarkera ett enda objekt, eller dra lodrätt längs markeringskolumnen för att markera många objekt. Samma sak fungerar med synlighetskolumnen.

Håll intryckt på markerings- eller synlighetsikonen för att även påverka barnen.

:::

### Trädvyns sidhuvud {#tree-view-header}

Raden ovanför listan har några hjälpmedel:

* ![](/icons/sort_down.webp) - fäller ihop eller ut alla grupper på en gång.
* ![](/icons/preview.webp) - visar eller döljer `Objektförhandsvisningar`, en liten renderad miniatyr för varje objekt i listan.
* ![](/icons/search.webp) - filtrerar listan efter namn.

### Hantera trädvyn {#tree-view-manipulation}

Håll intryckt på ett objekt i trädvyn tills det markeras. Sedan kan du flytta det uppåt eller nedåt i trädvyn, eller dra det över ett annat objekt för att göra det till ett barn till det objektet.

När många objekt är markerade är ett av dem huvudmarkeringen, och det ritas ljusare. Håll intryckt och dra i ett av dem för att flytta alla markerade objekt på en gång.

När du markerar ett överordnat objekt markeras som standard alla dess barn också. Trycker du på det överordnade objektet igen växlar du mellan att markera bara det och att markera det med alla barn.

Dubbeltryck på ett objekt för att fokusera kameran på det (se [Avancerat](#focus-on-item)).

### Objektmeny {#object-menu}

Klicka på knappen med tre punkter (...) för ett objekt i trädvyn för att visa objektmenyn.
Många av alternativen är desamma som i genvägsfältet högst upp, upprepade för enkelhetens skull.

|       Åtgärd        |                        Ikon                        | Beskrivning                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Namn         |              ![](/icons/pencil.webp)           | Byter namn på objektet                                                                                                                                                  |
|     Av-instans      |              ![](/icons/unlink.webp)           | Gör om en instans till en egen unik form, så att ändringar i formen inte längre kopieras till de andra instanserna.                                                    |
|      Instans        |               ![](/icons/link.webp)            | Duplicerar objektet som en instans, så att ändringar i formen på en av dem görs på alla instanser.                                                                     |
|        Klona        |              ![](/icons/clone.webp)            | Duplicerar objektet till ett nytt objekt                                                                                                                                |
|       Radera        |              ![](/icons/trash.webp)            | Raderar objektet. Dess barn behålls, om inte `Barn` är ikryssat.                                                                                                        |
|        Barn         |            ![](/icons/hierarchy.webp)          | När det är ikryssat påverkar `Instans`, `Klona` och `Radera` även objektets barn.                                                                                       |
|  Dela efter delar   |             ![](/icons/separate.webp)          | Om ett objekt består av delar som inte sitter ihop skapas ett separat objekt för var och en av dem. Motsatsen till att foga ihop.                                       |
| Dela efter grupper  |            ![](/icons/group.webp)          | Om ett objekt har flera ytgrupper skapas ett separat objekt för varje ytgrupp.                                                                                              |
|  Dela efter lager   |              ![](/icons/layer.webp)            | Om ett objekt har lager skapas separata objekt för grundmeshen och för varje lager. Praktiskt för att skicka blendshapes till andra program.                            |
|  Foga ihop → Lager  | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Om flera objekt är markerade och har samma topologi slås de ihop till lager i huvudobjektet (de andra objekten raderas). Återigen praktiskt för blendshapes som kommer FRÅN andra program.<br><br> Observera att lagren är inaktiverade som standard. Aktivera dem om du behöver justera deras reglage. |
|  Kurva (Repeterare) |              ![](/icons/curve.webp)            | Bara för ett rör eller en svarv: lägger till en repeterare av typen [Kurva](#curve) som följer samma kurva, som ett barn till objektet.                                 |
|        Rör          |             ![](/icons/tube.webp)              | För en svarv: lägger till ett [rör](tools.md#tube) som följer dess profil, som ett barn. För en cylinder, en kon eller en torus: gör om den till ett rör med samma form, så att du kan böja den längs en kurva. |




### Flerval {#multiselection}
Du kan markera flera objekt för att göra två saker:
- använda gizmon för att flytta flera objekt på en gång
- slå ihop objekt med åtgärderna Foga ihop och Boolean.

I trädvyn trycker du på markeringsikonen för varje objekt, eller drar längs markeringskolumnen. När du trycker på namnen kan du hålla in kortkommandot `Mask` (eller `Ctrl` på ett tangentbord) för att lägga till eller ta bort ett enda objekt, eller hålla in kortkommandot `Jämna ut` (eller `Shift`) för att markera alla objekt mellan det aktuella och det du trycker på.

::: tip Snabbt flerval
Du kan också markera flera objekt i vyn genom att hålla in kortkommandot `Jämna ut` (eller `Shift`) och trycka på en annan mesh.

Du kan avmarkera ett objekt genom att trycka på det igen (bara om din markering innehåller mer än ett objekt).
:::

Gizmon flyttar alla markerade objekt tillsammans, se [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Foga ihop {#join}
Det här alternativet gör helt enkelt ett enda objekt av flera markerade objekt.
Punkter och UV:er som ligger närmare varandra än [svetsradien](#weld-radius) slås ihop.

Du kan se ett exempel på video i avsnittet [Dela](#separate).

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Slår ihop objekt till en enda yta.

`Voxelsammanslagning` behåller objektens volym och beräknar nya, jämnt fördelade polygoner på ytan. Tack vare beräkningssteget klarar en voxelsammanslagning komplicerad geometri, men den kan tappa fina detaljer om målupplösningen inte är tillräckligt hög.

`Boolean` försöker behålla polygonerna i sin ursprungliga layout och sy ihop polygonerna där objekten överlappar. Det kan ge mycket renare och skarpare resultat än en voxelsammanslagning, men kräver "vattentäta" meshar: objekten får inte ha hål eller felaktiga former. Om det misslyckas brukar en voxelsammanslagning fungera.

### Booleska operationer {#boolean-operations}
Både Voxelsammanslagning och Boolean använder objektens synlighet för att styra operationen, som påminnelserna längst ner i popup-fönstret säger:

#### Union {#union}
Båda objekten synliga ger en boolesk **union**: objektens yttre skal slås ihop, utan några inre ytor. ![](/images/boolean_union.webp)

#### Subtraktion {#subtract}
Ett objekt osynligt = boolesk **subtraktion**: det osynliga objektet dras bort från det synliga. ![](/images/boolean_subtract.webp)

#### Snittyta {#intersect}
Båda objekten osynliga = booleskt **snitt**: en ny form skapas bara där de två objekten överlappar. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Voxelsammanslagning {#voxel-merge-button}
Den här knappen gör en voxelsammanslagning av de markerade objekten. Gör du den på ett enda objekt får det ny topologi med jämnt fördelade polygoner, vilket är praktiskt när ett objekt har utdragna polygoner. Alternativen nedan fungerar som för [Voxel-omnätning](topology.md#voxel-remesher).

### Upplösning {#resolution}
Upplösningen på det 3d-rutnät av voxlar som används för beräkningen. När du ändrar värdet läggs ett schackrutigt mönster över objektet som förhandsvisar polygonernas storlek.

Pipetten bredvid reglaget hämtar detaljnivån från meshens täthet under ditt finger. Knappen bredvid den växlar reglaget till `Kantlängd`, en storlek i världen: samma värde ger samma detaljnivå på alla objekt.

### Bygg multiresolution {#build-multiresolution}
Skapar multiresolution-nivåer under din målupplösning. Om upplösningen är 400 och Bygg multiresolution är 3 får du en ny mesh med säg 296 000 polygoner, men med 3 lägre indelningsnivåer på ungefär 74 000, 18 500 och 4 600.

### Förtjocka tunna delar {#thicken-thin-parts}
Gör delar som är för tunna för voxelrutnätet tjockare, så att de inte går sönder. Det går inte att använda tillsammans med `Skarpa kanter` eller `Skarp gräns`.

### Hål {#holes}
Hur hål i öppna objekt stängs före sammanslagningen:
* `Fyll` - varje hål stängs för sig, utifrån sin kant.
* `Form` - hålen stängs genom att följa den omgivande ytan, och öppna delar som överlappar fogas ihop.

### ![](/icons/angle.webp) Behåll skarpa kanter {#keep-sharp-edges}
Knappen `Skarpa kanter` fäster voxelmeshen mot objektens skarpa kanter. Det fungerar bäst på enkla former och kan ge förvrängningar på vissa ställen.

### ![](/icons/group.webp) Skarp gräns {#sharp-border}
De nya ytorna följer ytgruppernas gränser, och en gräns förblir skarp där ytan viks längs den.

### ![](/icons/group_separate.webp) Håll grupper åtskilda {#keep-groups-separate}
Varje ytgrupp får ny topologi för sig: grupperna slås aldrig ihop, och var och en förblir en sluten del i sin egen grupp. Multiresolution byggs inte i det här läget.

### ![](/icons/bool_subtract_circle.webp) Knappen Boolean {#boolean-button}
Den här knappen gör en boolesk operation på polygonerna med biblioteket Manifold av Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Rensa överlappningar {#clean-overlaps}
När bara ett objekt är markerat blir knappen `Boolean` till `Rensa överlappningar`: den slår ihop de delar av objektet som korsar varandra till en ren yta.


## ![](/icons/separate.webp) Dela {#separate}
Om du har ett enda objekt som består av flera delar som inte sitter ihop kan du dela upp det i flera objekt.
Det kan ses som motsatsen till [Foga ihop](#join).

Popup-fönstret `Dela...` har tre sätt att dela upp de markerade objekten:
* `Dela efter delar` - skapar ett separat objekt för varje del som inte sitter ihop med resten.
* `Dela efter grupper` - skapar ett separat objekt för varje ytgrupp.
* `Dela efter lager` - skapar separata objekt för grundmeshen och för varje lager.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menyn Lägg till {#add-menu}

![](/images/scene_addmenu_overview.webp)

Den här menyn skapar primitiver, grupper, kameror, repeterare och ljus.

Primitiver är grundformer som kan justeras med parametrar. När du har justerat primitiven efter dina behov "slutför" du den, vilket bakar in parametrarna i en polygonmesh som går att skulptera och måla på. En primitiv kan inte längre få sina parametrar justerade när den har slutförts.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) På gizmo {#on-gizmo}
Placerar den nya primitiven där den markerade formen eller gizmon finns. När det är av placeras primitiven i scenens mitt.

### ![](/icons/gizmo.webp) Välj gizmo {#select-gizmo}
Byter automatiskt till gizmoverktyget när en ny primitiv skapas.

### ![](/icons/cog.webp) Avancerat {#add-advanced}

I den här menyn väljer du var nya primitiver, grupper och repeterare ska skapas. De kan hamna på det markerade objektet, i världens origo eller där gizmon är.


### UV:er {#uvs}
Knappen `UVs` bredvid rubriken Primitiv aktiverar UV:er på primitiver. UV:er (ofta kallade texturkoordinater) är extra data som används i 3d för att kunna lägga texturer på ytor. De tar mer minne, men på de flesta enheter borde det inte vara något problem om du inte ger dig in på väldigt höga polygonantal (till exempel 10 miljoner polygoner eller fler).

### Primitiver {#primitives}

| Primitiv       | Ikon                                      | Beskrivning                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | En enkel kub, du kan styra indelningen i X, Y och Z                                                             |
| Kvadsfär       | ![](/icons/circle.webp)                  | En indelad box där `Sfär` alltid är på, så att den får en jämn layout av fyrhörningar som passar bra att skulptera på |
| Cylinder       | ![](/icons/cylinder.webp)                | Du kan lägga till ett hål i mitten av cylindern, till exempel för att göra ett ihåligt rör                       |
| Torus          | ![](/icons/torus.webp)                   | Torusen kan vara en bra utgångspunkt för ringar                                                                 |
| Kon            | ![](/icons/cone.webp)                    | -                                                                                                               |
| Ikosaeder      | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-sfär        | ![](/icons/circle.webp)                  | En sfär med ojämn polygonlayout, se [Varning nedan](#uv-sphere)                                                 |
| Plan           | ![](/icons/rectangle.webp)               | Ett enkelt plan, observera att det är den enda primitiven som inte är sluten                                    |
| Text           | ![](/icons/text.webp)                    | 3d-text, med typsnitt, stil, justering, djup och böjning. `Sammanfoga bokstäver` smälter ihop bokstäver som rör vid varandra |
| Rör            | ![](/icons/tube.webp)                    | se [Rör](tools#tube)                                                                                            |
| Svarv          | ![](/icons/lathe.webp)                   | se [Svarv](tools#lathe)                                                                                         |
| Triplanar      | ![](/icons/triplanar.webp)               | se [Triplanar](#triplanar)                                                                                      |
| VDM            | ![](/icons/vdm.webp)                     | Ett plan förberett för att skulptera en stämpel med vektorförskjutning: det har UV:er och är vänt mot kameran     |
| Skuggfångare   | ![](/icons/material_shadow_catcher.webp) | se [Skuggfångare](#shadow-catcher)                                                                              |
| Huvud          | ![](/icons/face.webp)                    | Ett enkelt huvud med ett lager för att blanda mellan man och kvinna                                             |

::: tip
Om du undrar vad grundmeshen är när du startar Nomad: det är också en indelad box.
Men grundmeshen i Nomad använder inte `Sfär` (projicering på en sfär), så den är inte helt rund.
:::

### Primitivens verktygsfält {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

När en primitiv har skapats dyker ett verktygsfält upp där du styr dess parametrar.

* `Slutför` Bakar in primitiven i ett vanligt objekt så att den går att skulptera och måla på.
* `Spegla` Lägger till eller tar bort en spegelrepeterare ovanför primitiven.
* `Alla` (ögonikonen) Väljer vilka handtag som visas direkt på primitiven för att styra dess parametrar, till exempel kubens bredd eller radien på en cylinders hål: `Ingen`, `Alla`, eller bara en sorts handtag (radie, hål, profil...) beroende på primitiven.
* `Division` Antalet indelningar i primitiven, här längs X för en box.
* `Konstant densitet` När du sträcker ut primitiven längs en axel med gizmon växer storleken och indelningarna i stället för att polygonerna dras ut, så att ytorna förblir kvadratiska. Finns för boxar, plan och cylindrar.
* `...` Visar primitivens meny.

Olika primitiver har extra alternativ i verktygsfältet:

* `Sfär` Sfären är uppbyggd som en indelad kub, eftersom det är bättre för skulptering, men det betyder att den inte är helt rund. Det här alternativet tvingar formen närmare en perfekt sfär. Ikosaedern har också det här alternativet.
* `Hätta` Slår på eller av ändlock på en form, till exempel kan en cylinder ha lock upptill, nedtill, båda eller inget.
* `Hål` Slår på eller av ett hål genom mitten av en form. Växlar mellan inget hål, ett hål med en enda radie och ett hål med olika radie upptill och nedtill.
* `Radie` Väljer om en cylinder ska ha en enda radie eller olika radie upptill och nedtill.
* `Skiva` Väljer om ett plan ska vara fyrsidigt eller runt.

Det lilla verktygsfältet under huvudverktygsfältet låter dig växla mellan primitivens gizmo och transformgizmon.

::: tip

Klickar du på verktygsfältets rubrik flyttas det mellan skärmens överkant och nederkant. Klickar du på pilen i hörnet fälls det ihop.

:::


### Primitivens meny {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Här finns alla parametrar för den markerade primitiven. Parametrarna är den grundläggande beskrivningen av en form. För att beskriva en ring skulle du till exempel ange dess yttre radie, dess inre radie och antalet polygoner.

De flesta parametrar för primitiver förklarar sig själva, och några vanliga parametrar finns för alla primitiver:

* `UVs` Den lilla knappen UVs högst upp i menyn slår på eller av skapandet av UV-koordinater
* `Slutför` Den lilla slutför-knappen bakar in primitiven i ett vanligt objekt så att den går att skulptera och måla på.
* `Max. ytor` Sätter en övre gräns för antalet polygoner i objektet så att din enhet inte kraschar.
* `Postdelning` Använder det valda antalet indelningar från avsnittet Multiresolution i menyn Topologi. Tillsammans med få indelningar i topologin kan du göra utjämnade primitiver med mjuka hörn. Om du till exempel sätter en box topologiindelningar till 2 och postindelningen till 4 får du en box med mjuka hörn.
* `Linjär indelning` Anger hur många nivåer linjär indelning som används innan vanlig mjuk indelning tar vid. Med det styr du hur skarpa eller mjuka hörnen blir på de indelade ytorna. Sätt till exempel en box topologiindelningar till 2 och postindelningen till 4, och prova sedan att ändra den linjära indelningen mellan 0 och 4. Boxens hörn går från mjuka till skarpa.

### Topologi {#topology}

Styr antalet polygoner i en primitiv. Oftast är reglagen länkade, så att det enda aktiva reglaget justerar alla polygoner jämnt. Du kan trycka på knappen för att bryta länken och styra indelningarna i X/Y/Z var för sig.

### Geometri {#geometry}

Styr primitivens övergripande storlek, i X/Y/Z-enheter för kantiga former och som radie för runda former.


### ![](/icons/circle.webp) UV-sfär {#uv-sphere}
::: warning
UV-sfären passar dåligt för skulptering, särskilt vid polerna.

Använd hellre [primitiverna](#primitives) Kvadsfär, Box eller Ikosaeder, tillsammans med alternativet `Sfär`.

Observera att topologin kan duga för skulptering om du använder ett mycket lågt värde på reglagen `Division`.
Sedan kan du höja antalet polygoner med reglaget `Total indelning`.

Den passar inte för vanlig skulptering, men är användbar till ögon: om du roterar sfären så att polerna hamnar vid pupillen passar polygonlayouten naturligt för att måla och skulptera iris och pupill.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Det speciella med den här primitiven är att du formar geometrin med [maskverktyget](tools.md#mask).

![](/videos/triplanar.mp4)


::: tip
Dubbeltryck på ett plan så fokuserar kameran på just det planet.
Det fungerar dock inte om du roterar primitiven med gizmon.
:::

Triplanar använder maskinformationen från 3 plan för att fylla ett voxelrutnät som sedan görs om till polygoner (tack vare [Voxel-omnätning](topology.md#voxel-remesher)).

Varje plan har sitt eget symmetriplan.

::: warning
Varje gång du ändrar storleken på primitiven Triplanar försämras kvaliteten på den målade masken.

Än så länge finns inget alternativ för att "låsa" målningen till ett enda plan, men det kanske kommer i framtiden.
Du kan använda [Ansluten topologi](stroke.md#connected-topology) som en liten hjälp: om markören ligger precis på ett plan påverkas inte de andra planen.
:::

### ![](/icons/material_shadow_catcher.webp) Skuggfångare {#shadow-catcher}
Lägger till ett plan med materialet Skuggfångare. Se [materialet Skuggfångare](material.md#shadow-catcher) för mer information.


## Grupp/Kamera {#groupcamera}
### ![](/icons/share.webp) Grupp {#group}
Skapar ett "tomt" objekt som du kan lägga andra objekt under. Det kan användas för att helt enkelt organisera hierarkin, genom att lägga många objekt under en grupp och sedan fälla ihop den. En grupp kan också vara ett hjälpmedel för att flytta objekt: lägg många objekt under en grupp och flytta, rotera eller skala sedan gruppen med gizmon.

### ![](/icons/camera.webp) Kamera {#add-view}
Skapar en kamera.

## Repeterare {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeterare är noder som skapar instanser av objekten under dem.

### ![](/icons/array.webp) Array {#array}
![](/images/scene_primitive_array.webp)

När objekt görs till barn till den här noden kan de instansieras i ett rutnät. När den är markerad har den reglage för:
* `Passas inuti` - när det är på placeras alla kopior inom arrayens gränser; när det är av anger reglagen avståndet mellan kopiorna
* `Antal X/Y/Z` - antalet instanser längs varje axel
* `Storlek X/Y/Z` - rutnätets storlek längs varje axel, eller avståndet mellan kopiorna när `Passas inuti` är av
* `Randomisera...` - ger kopiorna slumpmässiga variationer, se [Randomisera](#curve) nedan.

### ![](/icons/curve.webp) Kurva {#curve}
![](/images/scene_primitive_curve.webp)
Skapar en kurva, och barnen till den här noden upprepas längs kurvan. När den är markerad har den reglage för:
* `Kurva` - redigerar kurvan: lägg till punkter på kurvan och flytta punkter på den.
* `Visa` - visar eller döljer kurvan och dess punkter.
* `Snap` - fäster kurvans punkter mot annan geometri.
* `Sym` - redigerar kurvan symmetriskt.
* `Stängd` - väljer om kurvan ska förena start och slut, eller vara en öppen kurva.
* `B-spline` - väljer om instanserna ska följa kurvan exakt, eller använda B-spline-interpolering som ger mjukare resultat.
* `Forma efter ytan` - böjer varje kopia längs kurvan så att kopiorna möter sina grannar (`Mjuk` böjer deras sidor så att de möts utan vinkel).
* `Justera` - roterar kopiorna så att de följer kurvans riktning.
* `Pivot` - kopiornas pivot: själva kurvan (`Själv`) eller dess barn.
* `Antal` - antalet instanser. Lägesknappen bredvid växlar till `Avstånd`: ett fast avstånd mellan kopiorna, och antalet följer kurvans längd.
* `Radie` - reglage på varje kurvpunkt som anger instansernas skala.
* `Twist` - reglage på varje kurvpunkt som anger instansernas vridning.
* `Växla` - vänder varannan kopia runt kurvan: 90° för kedjelänkar, 180° för löv eller blixtlåständer, runt den `Axel` du väljer.
* `Spiral...` - lindar kopiorna runt kurvan, i flera strängar (rep, fläta, band...).
* `Randomisera...` - ger kopiorna slumpmässiga variationer; varje rad kan i stället lägga till samma mängd för varje kopia.

Under verktygsfältet finns knappen `(sammanfoga)`, som slår ihop en punkt med en annan när du drar den ovanpå den. `IK` (inverterad kinematik) låter dig posera kurvan: dra i en punkt så följer de anslutna punkterna med. Tryck på en punkt för att låsa eller låsa upp den, håll intryckt för att låsa eller låsa upp alla; låsta punkter stannar på sin plats.

### ![](/icons/radial.webp) Radiell {#radial}
![](/images/scene_primitive_radial.webp)

Barnen till den här noden instansieras i en cirkel. Flytta barnobjektet för att ändra repeterarens radie. När den är markerad har den reglage för:
* RadialX/Y/Z - de här knapparna anger den radiella axeln och antalet instanser.



### ![](/icons/mirror.webp) Spegla {#mirror}
![](/images/scene_primitive_mirror.webp)

Barnen till den här noden speglas över en axel. När den är markerad har den reglage för:
* Gizmo - aktiverar transformgizmon för att ange spegelns mittpunkt. Den kan också roteras och skalas. När du är klar trycker du på gizmo igen för att visa de vanliga reglagen.
* X/Y/Z - anger spegelplanet

### ![](/icons/surface.webp) Yta {#surface}

Barnen till den här noden kopieras ut på ytan av ett objekt: en kopia per yta, per kant eller per vertex, eller utspridda slumpmässigt. När den är markerad har den reglage för:
* Läge - placerar kopiorna på `Ytor`, på `Kanter` eller på vertexerna, eller `Sprid` ut dem.
* Varje - en kopia var N:te yta, kant eller vertex. `Slumpmässig` väljer dem slumpmässigt i stället, och `Blanda om` drar ett nytt slumpmässigt urval.
* Mellanrum - vid spridning, minsta avståndet mellan två kopior.
* Rikta - kopiorna står på ytan och följer dess normal, i stället för att behålla originalets orientering.
* Fäst - projicerar originalet på närmaste punkt på ytan, och kopiorna följer med.
* Anpassa storlek, Skevhet - skalar och sträcker kopiorna efter formen på varje yta.
* Forma efter ytan - böjer varje kopia över sin yta, eller längs sin kant, så att intilliggande kopior möts utan glipor.

Alla repeterare har reglaget `Slutför`, som bakar in repeterarens resultat och frågar hur det ska göras:
* Foga ihop barn - instanserna fogas ihop till ett enda objekt
* Behåll instanser - instanserna förblir instanser, men har inte längre repeteraren som "förälder"
* Av-instans - instanserna görs om till unika objekt

`Platta ut alla` bakar även in de repeterare som ligger inuti den här, så att varje kopia blir ett vanligt objekt.

::: tip Tips: Kombinera repeterare
Repeterare kan läggas under varandra, och flera objekt kan göras till barn till repeterare, vilket ger avancerade effekter.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tips: Repeterarnas pivoter

Vissa repeterare försöker sätta barnobjektens pivot automatiskt, så även om du flyttar eller roterar dem med gizmon rör de sig inte. Om du behöver komma runt det, lägg in en grupp mellan repeteraren och barnet. Då kan du flytta barnformen oberoende av repeteraren.
:::

## Ljus {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Riktad {#directional}
Skapar ett riktat ljus, en oändligt avlägsen ljuskälla som solen.

### ![](/icons/panorama.webp) Miljö {#environment}
Skapar ett miljöljus, som lyser upp scenen från en bild runt omkring den (bildbaserad belysning, som en HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Skapar en spotlight, med reglage för konens bredd och mjukhet

### ![](/icons/light.webp) Punkt {#point}
Skapar ett punktljus

## ![](/icons/cog.webp) Avancerat {#advanced}
Knappen `Avancerat` längst ner till vänster i panelen öppnar ett popup-fönster med två flikar: `Allmänt` och `Synka`.

### ![](/icons/focus.webp) Gränssnitt: Fokusera på objekt vid dubbeltryck {#focus-on-item}
Dubbeltryck på ett objekt i scenlistan för att centrera kameran på det objektet i 3d-vyn.

### ![](/icons/eye_open.webp) Synka synlighet {#sync-visibility}
När det här är på påverkar ögonikonen på ett markerat objekt alla markerade objekt.

### ![](/icons/bang.webp) Markering {#highlight}
Framhäver de markerade objekten i vyn när markeringen ändras.

### ![](/icons/link.webp) Visa (Instans) {#instance-show}
Visar en färgad kapsel till vänster i scenlistan för att markera instanser.

### ![](/icons/preview.webp) Objektförhandsvisningar {#object-previews}
Visar en renderad miniatyr för varje objekt i scenlistan. Samma sak som förhandsvisningsknappen ovanför listan.

### Svetsradie {#weld-radius}
Under rubriken `Foga ihop`, `Positionsradie för svetsning` och `Svetsradie för UV`: punkter och UV:er som ligger närmare varandra än de här radierna slås ihop. Var och en kan stängas av med sin kryssruta. Det gäller Foga ihop, Boolean, Beskär, Decimera, omnätning och filimport.

### Ikoner {#icons}
Anger minsta och största `Storlek` och `Opacitet` för ikonerna för grupper, ljus, kameror och repeterare i vyn.

### ![](/icons/hierarchy.webp) Hierarkilinjer {#hierarchy-lines}
Visar en linje mellan ett överordnat objekt och dess barn i vyn. När det här är på kan du också ställa in:
* `Använd Nomad pivot` - linjerna utgår från pivoten som används av verktygen Transformera och Gizmo. När det är av används den naturliga grundpivoten, som kan ligga långt från objektets mitt.
* `Tjocklek` - linjernas bredd. Knappen bredvid reglaget ger dem en kontur.
* Linjernas färg.

### ![](/icons/link.webp) Synka {#sync}
Fliken `Synka` anger för varje åtgärd (`Lägg till`, `Radera`, `Lås`, `Klona`, `Instans`, `Av-instans`, `Foga ihop`, `Dela` och `Boolean`) om den gäller alla instanser i markeringen:
* `Auto` - följer kryssrutan `Synka` högst upp i scenmenyn.
* `Nej` - bara de markerade objekten.
* `Ja` - alltid alla instanser.

Som standard står `Foga ihop`, `Dela` och `Boolean` på `Ja` och de andra på `Auto`. `Återställ` tar tillbaka de här standardvärdena.

## Nedre verktygsfält {#bottom-toolbar}
De här ikonerna visar eller döljer grupper, ljus, kameror, repeterare och hierarkilinjer i vyn. Ikoner som visas i vyn kan du trycka på för att markera och redigera dem direkt.
