# ![](/icons/toolbox.webp) Verktyg {#tools}

![](/images/tools_menu.webp)

::: tip
Hoppa ned till [Verktyg](#tools-1) för beskrivningar av de enskilda verktygen.
:::

## Översikt {#overview}

Du väljer verktyg i `Verktygslåda` till höger och styr dem med `Verktygskontroller` till vänster. Fler inställningar finns i menyn `Verktyg`, bland menyerna uppe till höger.

Penselverktygen har reglage för storlek och intensitet. Markeringsverktygen har kontroller för flera olika sätt att markera. Längst ned bland verktygskontrollerna finns genvägar till ofta använda funktioner (Jämna ut, Mask, Dölj, Ytgrupp, Gizmo, Färg, Alpha).

Nomads verktyg är färgkodade i verktygslådan (stäng av `Färgade verktyg` i menyn [Gränssnitt](interface.md) för enfärgade etiketter):

* <span class=brush>**Penselverktyg**</span> (Lera, Pensel, Jämna ut, Lager, Blås upp, Radera lager, Quad Remesher)
* <span class=move>**Flyttverktyg**</span> (Flytta, Dra, Elastisk, Knuffa)
* <span class=mask>**Maskverktyg**</span> (Mask)
* <span class=paint>**Målarverktyg**</span> (Måla, Smeta ut)
* <span class=flatten>**Utplattningsverktyg**</span> (Platta ut, Plan, Polera)
* <span class=pinch>**Klämverktyg**</span> (Veck, Klämma)
* <span class=stamp>**Stämpelverktyg**</span> (Stämpel, VDM)
* <span class=selection>**Markeringsbaserade verktyg**</span>, där du först ritar en 2d-mask och sedan utförs en åtgärd (Beskär, Dela, Projekt)
* <span class=creation>**Skapandeverktyg**</span> (Rör, Svarv, Infoga)
* <span class=transform>**Transformeringsverktyg**</span> (Transformera, Gizmo, Ordna, Galler)
* <span class=misc>**Övriga verktyg**</span> (Ytgrupp, Dölj)
* <span class=view>**Visningsverktyg**</span> (Vy, Mät, Välj)



Många av verktygen kan anpassas med olika penselbeteenden, tryckkänslighet, texturer med mera via menyn [Penseldrag](stroke.md).


### Penselkontroller {#brush-controls}

Det vänstra verktygsfältet har reglage för radie och intensitet, och därefter kontroller som är specifika för verktygets kategori. De förklaras nedan.

![](/images/tool_left_panel.webp)

::: tip
För många verktyg kan intensitetsreglaget gå över 100 %, det är värt att experimentera med!
:::

### Sub-läge {#sub-mode}
Knappen direkt under intensitetsreglaget är knappen `Sub`. Dess etikett och funktion ändras med varje verktyg, och när du trycker på den aktiveras ett alternativt, oftast motsatt, beteende. För [Måla](#paint) ger den till exempel ett suddläge, och för [Veck](#crease) skapar den upphöjda kanter i stället för veck.

Som standard fungerar den som en tillfällig knapp: håll den nedtryckt för att använda den tillfälligt, och när du släpper stängs den av. Om du i stället trycker på den en gång förblir sub-läget aktiverat.

### Genvägar {#shortcuts}
Längst ned i det vänstra verktygsfältet finns genvägar till [Jämna ut](#smooth), [Mask](#mask), [Dölj](#hide), [Ytgrupp](#facegroup), [Gizmo](#gizmo), [Färg](painting.md#pbr-sliders) och [Alpha](stroke.md#alpha).

Som standard fungerar alla som tillfälliga knappar: håll en nedtryckt för att använda den tillfälligt, och när du släpper stängs den av. Om du i stället trycker på den en gång förblir genvägens läge aktiverat.

### Markeringskontroller {#selection-controls}

Verktygen [Mask](#mask), [Måla](#paint), [Beskär](#trim), [Dela](#split), [Projekt](#project), [Ytgrupp](#facegroup), [Dölj](#hide) och [Välj](#select) använder alla liknande kontroller för att markera områden på meshen.

![](/images/tools_shape_selector_panel.webp)

Tryck på formknappen i det vänstra verktygsfältet (den visar den aktuella formen, `Lasso` som standard) för att öppna ett popup-fönster med formerna. För verktyg som även fungerar med pensel (Mask, Måla, Ytgrupp, Dölj) innehåller samma popup-fönster också typerna av penseldrag.

* `Visa` - Ingen form, verktyget gör inget särskilt, precis som kameraläget.
* `Lasso` - En frihandsritad form
* `Polygon` - En sluten form som byggs upp av kurvor och/eller raka linjer. Se [Formredigering](#shape-editing) nedan för mer information.
* `Kurva` - (endast Projekt) - En frihandskurva för projektionen
* `Bana` - (endast Projekt) - En kurva som definieras av punkter. Se [Formredigering](#shape-editing) nedan för mer information.
* `Linje` - Dra en linje för att definiera ett plant snitt. Som standard påverkas meshen direkt; ändra alternativet `Redigera` om du inte vill det (håll fingret på eller svep över linjeikonen)
* `Band` - En remsa mellan två parallella hjälplinjer, med en gradient tvärs över. `Förläng` behåller fullt värde förbi den bortre hjälplinjen i stället för att stanna vid bandet, och `Vänd` byter vilken hjälplinje gradienten börjar från.
* `Rekt` - Dra en diagonal linje som anger hörnen på en rektangel. Håll fingret på eller svep för att visa alternativet `Redigera`, `Kvadrat` för att tvinga fram en kvadrat och `Centrerad` för att låta första klicket bli rektangelns mittpunkt.
* `Ellips` - Dra en diagonal linje som anger storleken på en ellips. Håll fingret på eller svep för att visa alternativet `Redigera`, `Cirkel` för att tvinga fram en cirkel och `Centrerad` för att låta första klicket bli ellipsens mittpunkt.
* `Vänd` - Inverterar formmasken, eller riktningen för verktyget Projekt.

De flesta verktyg har alternativet `Redigera`, som avgör vad som händer när du har ritat färdigt formen:
* `Redigera: av` - Åtgärden utförs så fort du släpper.
* `Redigera: på` - Formen förblir redigerbar. En grön knapp visas bredvid formen, och den utför åtgärden. Då kan du justera formen och vyn, och när du är redo att använda formen trycker du på den gröna knappen.
* `Redigera: håll` - Åtgärden utförs när du släpper, om du inte stannar kvar i slutet av penseldraget för att fortsätta redigera formen.

### Formredigering {#shape-editing}
Polygon- och kurvredigering fungerar på liknande sätt:

* Börja med att dra en linje som definierar 2 punkter, och dra sedan ut från mitten av linjen för att skapa en polygon eller kurva.
* Klicka på punkterna för att växla mellan mjuka och skarpa.
* Klicka och dra på kurv- eller linjesegmenten för att skapa nya punkter.
* För att ta bort en punkt drar du den mot sin granne tills den blir röd.
* Papperskorgsikonen i hörnet av polygon- eller banikonen tar bort formen.

### Inställningsmeny {#settings-menu}

Många verktyg har extra inställningar i menyn `Verktyg`, bland menyerna uppe till höger. Menyn är nedtonad för verktyg som saknar extra inställningar.

![](/images/tools_settings_menu.webp)

## Verktyg {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Lera](#clay)       | ![](/icons/tool_brush.webp)   <br> [Pensel](#brush)     | ![](/icons/tool_move.webp)       <br> [Flytta](#move)              | ![](/icons/tool_drag.webp)      <br> [Dra](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Elastisk](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Jämna ut](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Mask](#mask)       | ![](/icons/tool_paint.webp)   <br> [Måla](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Smeta ut](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Platta ut](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Plan](#planar)       | ![](/icons/tool_polish.webp)  <br> [Polera](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Veck](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Klämma](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Beskär](#trim)              | ![](/icons/tool_split.webp)     <br> [Dela](#split)         | ![](/icons/tool_project.webp)   <br> [Projekt](#project)     | ![](/icons/tool_layer.webp)   <br> [Lager](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Blås upp](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Knuffa](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Stämpel](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [Radera lager](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Rör](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Svarv](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Infoga](#insert)   | ![](/icons/tool_transform.webp)  <br> [Transformera](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Ytgrupp](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Dölj](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Mät](#measure) | [Ordna](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Välj](#select)       | ![](/icons/tool_lattice.webp)   <br> [Galler](#lattice)     | ![](/icons/tool_view.webp)    <br> [Vy](#view)       |

------

### ![](/icons/tool_clay.webp) Lera {#clay}
Verktyget Lera är praktiskt när du bygger upp din skulptur. `Sub` tar i stället bort material från skulpturen.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pensel {#brush}
Standardpenseln. `Sub` tar bort material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Flytta {#move}
Området under penseln fastnar på penseln, vilket ger en elastisk deformation. Markeringen behålls under hela förflyttningen, så om du flyttar bort penseln och sedan tillbaka dit du började blir det ingen deformation alls.

Sub-läget är `Normal`, som flyttar området under penseln längs ytans normal.

Den här penseln passar både för stora deformationer och för försiktiga småjusteringar.

#### Inställningar för Flytta {#move-settings}

* `Radie (Bakgrund)` - Hur långt utanför modellens kant du kan börja och ändå skulptera, praktiskt när du arbetar med ett objekts siluett. Kryssa ur det för att bara greppa när du börjar på modellen.
* `Endast vertex på samma sida` - Ignorerar vertexer som pekar i motsatt riktning mot deformationen.
* `Riktning` - Används av sub-läget `Normal` och avgör om ett drag trycker in eller drar ut ytan:
    * `Auto` - Väljer en av de två metoderna nedan åt dig, utifrån vinkeln på ytans normal.
    * `Normal 3D` - Jämför pekarens position på skärmen med ytans normal sedd från kameran.
    * `XY` - Använder pekarens position på skärmen (upp/ned, vänster/höger) för att avgöra om ytan trycks in eller dras ut.
    * `Tröskel` - Med `Auto`: den vinkelgräns som avgör vilken metod som används.
* `Rullhastighet` - Du kan vrida det greppade området medan du flyttar det: rulla med två fingrar, rulla pennan mellan fingrarna, eller håll ned en modifieringstangent (Alt, Ctrl, Shift eller Cmd) medan du drar med musen. Det finns ett reglage var för finger, penna och mus; kryssa ur ett för att stänga av den inmatningen.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Dra {#drag}
Området under penseln fastnar på penseln, vilket ger en elastisk deformation. Till skillnad från Flytta uppdateras markeringen hela tiden under penseldraget, så du kan dra ut längre, ormlika former, särskilt när DynTopo är aktiverat.

Sub-läget är `Normal`, som flyttar området under penseln längs ytans normal.

Den här penseln passar för lösare, mer gestaltande formändringar.

#### Inställningar för Dra {#drag-settings}

Dra har samma inställningar som [Flytta](#move-settings): `Radie (Bakgrund)`, `Endast vertex på samma sida`, `Riktning` och `Rullhastighet`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastisk {#elastic}
Greppa och dra i ytan som med [Flytta](#move), men med en elastisk deformation: i stället för att sluta vid penselns kant avtar dragningen mjukt med avståndet över objektet, ungefär som när du sträcker ut gummi. Penselns radie avgör hur brett dragningen verkar.

Sub-läget är `Normal`, som flyttar området under penseln längs ytans normal.

Den här penseln passar för stora, mjuka proportionsändringar som förblir jämna.

#### Inställningar för Elastisk {#elastic-settings}

Elastisk har samma inställningar som [Flytta](#move-settings), utom `Endast vertex på samma sida`. `Radie (Bakgrund)` är avstängt som standard.

### ![](/icons/tool_smooth.webp) Jämna ut {#smooth}
Jämnar ut området genom att medelvärdesbilda punkternas positioner. Verktyget är starkt beroende av polygontätheten.
Har du många polygoner blir utjämningen alltså mindre effektiv.

Sub-läget är `Slappna av`, som bara jämnar ut trådnätet men försöker behålla de geometriska detaljerna.

#### Inställningar för Jämna ut {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Ytgrupp {#smooth-facegroup}

* `Slappna av` - Jämnar ut ytgruppernas gränser. Använd en intensitet över 100 % för att snabbt jämna ut gränserna. `Auto` jämnar bara ut om förhandsvisningen av ytgrupper är aktiverad, `Nej` stänger av det och `Ja` slår på det.

##### Vertex {#vertex}
* `Bevara volymen` - Jämnar ut utan att ytan krymper, så att upprepad utjämning inte får dina former att tappa luft. Kugghjulsknappen bredvid innehåller mängderna `Krymp` och `Blås upp` som används för detta.
* `Bevara kanter` - På mesher med öppna kanter, till exempel ett plan, kan hörnen jämnas ut. Med det här alternativet ligger vertexerna längs meshens kant kvar på plats.
* `Stabil utjämning` - Försöker göra utjämningen oberoende av topologin. Det fungerar bäst när topologin har varierande täthet och med ett högt intensitetsvärde.
* `Slappna av` - Samma som det alternativa läget Slappna av i det vänstra verktygsfältet.

##### Målning {#painting}
* `Skärmutjämning` - Använd det här alternativet för att få en utjämning som är oberoende av topologin, även med höga polygonantal. `Auto`, `Nej` eller `Ja`.
* `Skärmexempel` - Utjämningens kvalitet: högre värden ger jämnare resultat men är långsammare.

::: tip
Högre polygontäthet kan kräva att du höjer intensiteten över 100 %. Mycket höga värden (300 %, 500 %) kan också fungera bra som skulpteringsverktyg: områden under penseln blir snabbt plana och släta, som när du slår på lera med en klubba!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask {#mask}
Med det här verktyget maskerar du vertexer. Maskerade vertexer skyddas mot skulptering och målning.

Sub-läget är `Avmaskera`, som suddar bort masken där den har målats.

Precis som markeringar i 2d-målarprogram kan masker målas med pensel eller skapas med formmarkeringar (`Lasso`, `Rekt`, `Band`...), göras suddigare eller skarpare. Välj pensel eller form i popup-fönstret för penseldrag i det vänstra verktygsfältet, se [Markeringskontroller](#selection-controls).

Till skillnad från i 2d-målarprogram kan masker också skapas utifrån ytgrupper, och de kan användas för att skapa ny geometri genom åtgärder som extrudering och extrahering.

![](/videos/tool_mask1.mp4)

 Ett verktygsfält med extra kontroller visas högst upp i vyn.

![](/images/tool_mask_toolbar.webp)

Tryck på fältets rubrik för att fälla ut eller fälla ihop det, eller tryck på pilen uppe till höger för att flytta det till gränssnittets över- eller underkant.

| Åtgärd                                             | Beskrivning                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Rensa allt          | Rensar masken på alla objekt. När även andra objekt är maskerade rensar en extra knapp `Rensa` bara de markerade objekten |
| ![](/icons/invert.webp)        Invertera             | Inverterar masken                                                                            |
| ![](/icons/sharpen.webp)       Skärpa            | Gör maskens kant skarpare                                                                      |
| ![](/icons/blur.webp)          Sudda               | Gör maskens kant suddigare                                                                         |
| ![](/icons/outline.webp)       Kant             | Maskerar meshens öppna kant, till exempel kanten på ett plan eller randen runt ett hål          |
| ![](/icons/blur.webp)          Sudda ->            | Dra åt höger för att göra masken suddigare, åt vänster för att göra den skarpare                                            |
| ![](/icons/circle_plus.webp)   Utöka ->            | Dra åt höger för att utöka det maskerade området, åt vänster för att krympa det                                      |
| ![](/icons/intensity.webp)     Förstärk ->           | Dra åt höger för att förstärka masken, åt vänster för att försvaga den, utan att ändra dess form           |
| ![](/icons/dig.webp)           Hålighet ->          | Bygger om masken utifrån ytans krökning: dra åt höger så att bara fördjupningarna går att måla, åt vänster så att bara upphöjningarna gör det |
| ![](/icons/culling.webp)       Fram              | Växlar till att bara maskera vertexer som är vända framåt                                                  |
| ![](/icons/eye_open.webp)      Synlig            | Med former: växlar till att ignorera vertexer som döljs bakom andra ytor                        |
|                                 Konvertera            | Konverterar masken till en ytgrupp                                                            |
| ![](/icons/group_to_mask.webp) På tryck (ytgrupp) | När det är aktiverat visas ytgrupperna, och ett tryck på en ytgrupp maskerar den                    |
|                                 På tryck (mask)      | När det är aktiverat fylls en hel 'ö' av maskerade eller omaskerade polygoner när du trycker på den. |
| ![](/icons/connect.webp)       Anslutna          | När det är aktiverat påverkar maskdragen bara sammanhängande topologi.                         |

##### Snabbgester för mask {#mask-quick-gesture}
Du kan använda gester i ZBrush-stil medan du håller ned snabbmaskknappen i det vänstra verktygsfältet:
| Åtgärd  | Gest (håll genvägen nere till vänster) |
| :-----: | :--------------------------------: |
| Invertera  | Tryck på bakgrunden              |
| Rensa   | Dra på bakgrunden             |
| Sudda    | Tryck på ett maskerat område                 |
| Skärpa | Tryck på ett omaskerat område               |


#### Inställningar för Mask {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Maskinställningarna används främst för att skapa geometri utifrån masken. Flikarna högst upp väljer åtgärd: [Extrahera](#extract), [Dela](#split-mask) eller [Skulptera](#carve). Alternativen nedanför ändras efter åtgärden.

* `Förhandsgranska` - Visar hur den nya geometrin kommer att se ut medan du justerar inställningarna.
* `Röntgen` - Vilka objekt som ritas i röntgenläge under förhandsvisningen: `Ingen`, `Inte vald`, `Vald` eller `Alla`.

##### Extrahera {#extract}
* `Extrahera` - Skapar den extraherade geometrin som ett nytt objekt.
* `Avsluta åtgärd` - Hur den extraherade formen sluts. `Ingen` kopierar de maskerade polygonerna till en ny form och lämnar den öppen. `Fyll` gör samma sak, men fyller och jämnar ut hålet på baksidan (använd det inte på plana ytor). `Skal` sluter formen med hjälp av värdet `Höjd` och är standard.

::: tip

Om förhandsvisningen är aktiverad med röntgen kan knappen Extrahera vara förvirrande i början. Eftersom menyn är aktiv försöker den förhandsvisa en extrahering på din nya form och visa originalytan i röntgen. Men eftersom den nya ytan inte har någon mask kan extraheringen inte förhandsvisas, och Nomad varnar 'Inget att extrahera!'.

Det är helt normalt. Stäng menyn med maskinställningar för att se den nya formen och originalet, och markera originalytan igen om du behöver rensa masken eller rita nya masker.
:::

##### Dela {#split-mask}
* `Dela` - Extraherar både de maskerade OCH de omaskerade områdena till nya former.
* `Avsluta åtgärd` (maskerad) - Hur den maskerade delen sluts, med samma val `Ingen`, `Fyll` och `Skal` som för Extrahera.
* `Avsluta åtgärd` (omaskerad) - Hur den omaskerade delen sluts, med samma val.

##### Skulptera {#carve}
* `Skulptera` - Fungerar som om du hade skurit in i ytan med mängden `Höjd`, som när du skär loss en bit apelsinskal. `Höjd` kan inte vara 0.

##### Höjd {#thickness}
* `Höjd` - Den extraherade formens höjd. Plus/minus-knappen låter dig växla mellan extrudering utåt, inåt eller åt båda hållen.

##### Utjämning {#smoothness}
När det är aktivt jämnas den extraherade formen ut. Det fungerar bättre med högre polygonantal.
* `Alla` / `Endast kanter` - Jämnar ut hela formen, eller bara dess kanter så att ovansidans form lämnas orörd.
* `Iterationer` - Med `Alla`: hur mycket utjämning som tillämpas. Höga värden ger mycket mjukt rundade kanter, men formen börjar avvika från maskens form.
* `Vägg` - Med `Endast kanter`: hur mycket väggarna jämnas ut. Knappen bredvid växlar mellan Slappna av, som behåller de skarpa hörnen, och Jämna ut, som också rundar av dem.
* `Insida` - Med `Endast kanter`: hur mycket ovansidan jämnas till. Knappen bredvid växlar mellan Slappna av, som behåller de skulpterade detaljerna och bara jämnar till extruderingsriktningen (så att detaljerna inte ger upphov till spikar), och Jämna ut, som jämnar ut själva ytan.

##### Sidor {#edge-loop-side}
* `Rak` - Enkla väggar på den extraherade formens sidor.
* `Fasning` - (endast Extrahera med `Skal`) En sluttande kant på framsidan. `Fasning` anger dess bredd, i % av `Höjd` eller i världsenheter (knappen bredvid växlar), `Fasningsdelningar` delar upp den (`Auto` som standard), och med en kurva formar du dess profil.
* `Profil` - Formar väggarna med en profilkurva, med en `Bredd` i % av `Höjd` eller i världsenheter.
* `Mask` - Höjden följer masken: suddiga delar av masken får lägre höjd, vilket ger mjuka former med varierande höjd.
* `Väggdelningar` - Antalet kantslingor på sidorna. Med `Auto` väljer Nomad det antal delningar som ger kvadratiska polygoner som matchar polygonerna i det maskerade området.



### ![](/icons/tool_maskSelector.webp) Markeringsmask {#selection-mask}
Verktyget Markeringsmask (SelMask) är nu en del av [Mask-verktyget](#mask). För att maskera med former i stället för med penseldrag väljer du en form (`Lasso`, `Polygon`, `Rekt`...) i popup-fönstret för penseldrag i Mask-verktyget, se [Markeringskontroller](#selection-controls).

Sub-läget `Avmaskera` fungerar också med former och suddar då bort masken inuti formen.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Måla {#paint}
Lägger på färg och materialegenskaper. Du kan läsa mer om material i avsnittet [Målning](painting.md).

Sub-läget är `Radera`, som tar bort färg.

Förutom med penseldrag kan Måla också fylla former (`Lasso`, `Rekt`, `Band`...), se [Markeringskontroller](#selection-controls).

#### Inställningar för Måla {#paint-settings}
* `Lagerren filtrering` - Fungerar som lagrets alfalås i Photoshop eller Procreate. Om du målar på ett lager och det här är aktiverat kan du bara ändra där det redan finns färg; omålade områden skyddas. Det är bara tillgängligt när ett lager är valt.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smeta ut {#smudge}
Smetar ut färg och materialegenskaper. Inställningsmenyn för Smeta ut har ett reglage för `Kvalitet`: lägre värden ger snabbare penseldrag.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Platta ut {#flatten}
Plattar ut området genom att projicera punkterna på medelplanet.

Sub-läget är `Fyll`, som definierar ett plan utifrån den högsta punkten och tenderar att dra punkterna uppåt.

#### Inställningar för Platta ut {#flatten-settings}

* `Lås planriktning` - Använder planets riktning som beräknades vid första klicket. Som standard är det avstängt.
* `Lås planorsprung` - Använder första klicket som planets mittpunkt. Som standard är det avstängt, och det kan bara aktiveras tillsammans med `Lås planriktning`.

När ett eller båda av dessa är avstängda kan du gradvis fördjupa utplattningen eller ändra planets vinkel genom långa penseldrag som rör sig över olika djup och krökningar. Tillsammans med alternativen för områdessampling i penselmenyn ger det mycket exakt kontroll.

::: tip
När du arbetar i områden med stark krökning, till exempel när du försöker platta ut kinderna men verktyget hela tiden påverkar näsans sidor, kan du skapa en mask som skyddar de områden som utplattningen inte ska påverka.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Plan {#planar}
Gör punkterna plana genom att projicera dem på medelplanet, men med mindre uppbyggnad än Platta ut. Det ger renare ytor med skarpa kanter. Snabba penseldrag trycker och drar mer i ytan, medan långsammare drag som börjar i redan plana områden och arbetar sig utåt bättre bevarar planet.

Sub-läget är `Fyll`, som definierar ett plan utifrån den högsta punkten och tenderar att dra punkterna uppåt.

Plan är egentligen samma verktyg som `Platta ut`, men med `Lås planriktning` aktiverat. Det ger stabilare ytor med skarpa kanter, medan Platta ut kan vara mer skulpturalt och användas för att skapa halvplana områden.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Polera {#polish}
Ytterligare en medlem i Platta ut-familjen, inställd för att polera ytor till rena plan. Det är samma verktyg som `Platta ut`, med andra standardvärden i [Penseldrag](stroke.md): `Spårning bakom penseldraget`, `Områdes-normalfilter` och `Djupmaskering` är aktiverade.

Sub-läget är `Fyll`, precis som för Platta ut.

Polera har samma inställningar som [Platta ut](#flatten-settings): `Lås planriktning` och `Lås planorsprung`.

### ![](/icons/tool_crease.webp) Veck {#crease}
Veck är användbart för att skulptera små skåror eller fördjupningar.

Sub-läget är `Invertera`, som skapar ett upphöjt veck.

#### Inställningar för Veck {#crease-settings}

* `Klämfaktor` - Hur mycket vertexerna dras i sidled mot penseln. Om klämningen är 1 och förskjutningen 0 ändras inte ytans djup alls, bara topologin, och kanterna dras mot penseldraget.
* `Offsetfaktor` - Hur mycket vertexerna trycks in eller dras ut på djupet. Om klämningen är 0 och förskjutningen 1 blir vecken djupa eller kraftigt upphöjda, men de ser hackiga ut eftersom för lite geometri dras mot vecket för att forma dess sidor och botten ordentligt.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Klämma {#pinch}
Det här verktyget kan användas för att göra kanter skarpare.

Sub-läget är `Invertera`, som för isär vertexerna.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Beskär {#trim}
Beskär tar bort en bit av din mesh och ger dig val för hur hålet som blir kvar ska hanteras. Det använder [Markeringskontroller](#selection-controls) för att definiera beskärningen.

Sub-läget är `Vänd`, som inverterar formen så att den andra sidan tas bort.

::: tip
Eftersom verktyget projicerar från kameran får du en varning om kameran är i perspektivläge.

I ortografiskt läge går snittet genom meshen parallellt med vyn, vilket oftast är vad man förväntar sig. Med en perspektivkamera ser snittet olika ut på objektets bortre och närmre sida.
:::

#### Inställningar för Beskär {#trim-settings}

Inställningarna är samlade under `Hål utfyllnad`:

* `Streckmålning` - Om målning är aktiverad i målningsmenyn fylls det lagade området med den färg som är vald.
* `Boolean` - Fyller hålet efter beskärningen med ett område av fyrhörningar. Det fyllda området blir plant.
* `Legacy` - Fyller hålet med ett triangulerat område. Det fyllda området blir plant.
* `Fyll` - Fyller hålet med ett triangulerat område. Det fyllda området blir en välvd yta, som hinnan på en såpbubbla.
* `Ingen` - Fyller inte hålet.

Med `Boolean` innehåller avsnittet `Detalj`:

* `Form` - Ungefärlig storlek på de fyrhörningar och trianglar som används på formens sida av snittet.
* `Hål` - Ungefärlig storlek på de trianglar eller polygoner som används i det fyllda hålet. Länkknappen bredvid `Detalj` håller värdet i synk med `Form`; bryt länken för att ställa in det separat.
* `Bevara topologi` - Jämnar inte ut och förenklar inte snittets kant, så att meshens ursprungliga topologi behålls nära maskerade och dolda ytor.

Med `Legacy`:

* `Detalj` - Ungefärlig storlek på de trianglar som används vid beskärningen.
* `Hålslätning` - Hur mycket trianglarna i det fyllda området slappnas av.
* `Tröskel epsilon` - Ett värde som kan justeras för att förbättra den äldre algoritmen för hålutfyllnad.

Med `Fyll`:

* `Detalj` - Ungefärlig storlek på de trianglar som används vid beskärningen.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Dela {#split}
Liknar verktyget [Beskär](#trim), men medan Beskär kastar markeringen behåller Dela den som ett nytt objekt.

Sub-läget är `Dela`: varje bit behålls som ett eget objekt, så överlappande former (till exempel med symmetri) delas upp i separata delar i stället för att slås ihop till en.

#### Inställningar för Dela {#split-settings}

Dela har samma inställningar under `Hål utfyllnad` som [Beskär](#trim-settings): `Streckmålning`, metoderna `Boolean`, `Legacy`, `Fyll` och `Ingen`, samt deras alternativ för `Detalj`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projekt {#project}
Verktyget Projekt påminner om [Beskär](#trim), men det varken tar bort eller skapar någon geometri, det flyttar bara vertexerna så att de följer markeringen.

![](/videos/tool_project.mp4)

::: tip
Om du använder Projekt i ett lager kan du blanda mellan den ursprungliga och den projicerade formen med lagrets reglage.
:::

### ![](/icons/tool_layer.webp) Lager {#layer}
Höjer ytan, men med en begränsad höjd.

Om du håller pennan mot skärmen och fortsätter måla över ett område höjs Lager till en viss höjd och sedan inte längre, till skillnad från andra verktyg som fortsätter att bygga på höjden.

Observera att gränsen som standard bara gäller per penseldrag! Börjar du ett nytt penseldrag bygger det vidare från den nya ythöjden.

För att få en konstant maxhöjd över många penseldrag använder du verktyget Lager tillsammans med Nomads system för [Lager](layers.md).

Skapa ett lager och använd det här verktyget. Maxhöjden utgår nu från lagret, så du kan göra hur många penseldrag som helst och höjden blir alltid densamma.

`Sub` använder ett minsta djup och skapar skåror.

#### Inställningar för Lager {#layer-settings}

* `Använd lagerdata` - När det är aktivt och ett lager är valt används lagrets data för att sätta maxhöjden. En varning påminner dig när inget lager är valt.
* `Blås upp` - När det är aktivt justeras riktningen som verktyget verkar i, för jämnare resultat.
* `Slappna av (Normal)` - Med `Blås upp` aktiverat: hur mycket normalerna jämnas ut.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Blås upp {#inflate}
Flyttar vertexerna längs deras egna normaler. `Sub` flyttar vertexerna längs den inverterade normalen.

#### Inställningar för Blås upp {#inflate-setings}
* `Slappna av (Normal)` - Hur mycket normalerna jämnas ut.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Knuffa {#nudge}
Flyttar eller 'smetar' punkter i penseldragets riktning.

Sub-läget är `Vikning`, som skjuter en veckning av material längs penseldraget: en utbuktning framför penseln och en svacka bakom den.

#### Inställningar för Knuffa {#nudge-settings}
* `Jämna ut` - Hur mycket området under penseln jämnas ut medan du knuffar det, vilket håller den utsmetade ytan ren.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stämpel {#stamp}

Klicka och dra för att höja ett område av skulpturen i formen av den valda alfan.

Det är helt enkelt [Pensel-verktyget](#brush) med typen av penseldrag inställd på `Lås + radie`.

`Sub` trycker in stämpeln i stället för att dra ut den ur ytan.

::: tip
Stämpel fungerar oftast bäst med högupplöst geometri. Söker du på nätet efter 'wrinkles alpha', 'pores alpha', 'scales alpha' och liknande kan sådana alfatexturer tillsammans med Stämpel vara ett utmärkt sätt att lägga till organiska detaljer på en karaktärsskulptur.

De två typerna av penseldrag passar för olika saker.

* `Lås + radie` har en fast *höjd*, och genom att dra justerar du stämpelns bredd och rotation. Bra för hudtexturer som ska ha samma djup eller höjd, men olika rotation och skala för att dölja upprepade mönster.
* `Lås + intensitet` har en fast *bredd*, och genom att dra justerar du stämpelns rotation och höjd. Bra för nitar, som ska ha samma storlek men olika rotation och höjd.

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Stämplar en vektorförskjutningskarta (VDM). Till skillnad från en alfa, som bara kan trycka ytan uppåt eller nedåt, lagrar en VDM en fullständig 3d-form, så den kan stämpla överhäng som öron, horn eller ihoprullade blad. Den fungerar som [Stämpel](#stamp), med samma typer av penseldrag `Lås + radie` och `Lås + intensitet`.

`Sub` (`Invertera`) vänder stämpelns djup, så att den trycks in i ytan som en gjutform.

Själva VDM:en väljs i menyn [Alpha](stroke.md#alpha), som också har ett reglage för `Höjd` som bara skalar stämpelns höjd och lämnar dess förskjutning i sidled oförändrad.

Med knappen `Skapa` i det vänstra verktygsfältet gör du egna stämplar:

* `Ny VDM...` - Lägger till ett plan förberett för VDM-skulptering. Skulptera din form på det och baka den sedan med `Topologi -> Baka -> VDM`: Nomad lägger till den nya stämpeln i VDM-biblioteket och väljer den.
* `Fånga VDM` - (Experimentellt) Dra över ytan på en modell för att greppa det området och göra det till en VDM-stämpel. `Tolerans` plattar mjukt ut kanten på det fångade området.

::: tip
Undvik DynTopo när du skulpterar på ett VDM-plan, det förstör planets UV:er och förvränger stämpeln. Håll också skulpteringen borta från planets kant, annars får stämpeln en hård kant.
:::


### ![](/icons/tool_clearLayer.webp) Radera lager {#delete-layer}
Med det här verktyget kan du nollställa lager lokalt. Du behöver ett aktivt lager, annars händer ingenting. Det suddar bort lagrets skulpterade data, och även dess färg när målning är aktiverad.

Sub-läget är `Invertera`, som förstärker lagret något i stället för att sudda bort det.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Rör {#tube}
Skapar ett rör genom att du ritar en kurva.
![](/images/tool_tube_new.webp)

När röret har skapats kan banan redigeras i 3d-rymden med kontroller som liknar den vanliga [Formredigering](#shape-editing) och kurvredigeringen.

![](/videos/tool_tube.mp4)

#### Rörets vänstra verktygsfält {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Det vänstra verktygsfältet har följande alternativ:

* `Synka` - Om det aktuella röret är instansierat och rörets barnnoder skiljer sig mellan instanserna synkroniseras de igen.
* `Snap` - När det är aktivt fäster kurv- och banlägena mot andra objekt medan du ritar. När det är inaktivt fäster bara första punkten, och resten av röret ritas på det djupet.
* `Förskjutning` - Anger djupet för fästningen: vid 0 % fäster mitten av rörets tvärsnitt mot ytan, positiva värden lyfter det från ytan och negativa sänker det. 100 % motsvarar rörets radie.
* `Visa` - Inget ritläge, så att du kan flytta kameran fritt.
* `Kurva` - Skissa ett rör på fri hand. Det har en liten utfällbar meny:
    * `Redigera` - Vad som händer när du avslutar penseldraget, se [Markeringskontroller](#selection-controls): skapa röret direkt, behåll kurvan redigerbar med en grön bekräftelsecirkel bredvid, eller `Håll` i slutet av penseldraget för att fortsätta redigera.
    * `Stängd` - Gör röret till en slinga.
    * `Fortsätt rita` - Stanna kvar i verktyget efter att ett rör har bekräftats, för att rita nästa.
    * `Noggrannhet` - Hur många kurvpunkter som används för att omvandla den ritade banan till ett rör. 0 % använder minsta möjliga antal punkter, men missar små krökningar i banan. 100 % är mycket noggrant och använder många punkter.
* `Bana` - Skapa ett rör genom att klicka ut kurvpunkter. Tryck på den gröna cirkeln för att bekräfta banan. Det har en liten utfällbar meny:
    * `B-spline` - Ett alternativt sätt att rita kurvor, där kurvpunkterna oftast inte ligger direkt på kurvan, men resultatet kan bli mjukare än med standardmetoden.
    * `Stängd` - Gör röret till en slinga
    * `Skärm` - När det är aktivt är banan 'fastnålad' på skärmen, så att du kan flytta vyn och objektet medan banan ligger kvar på sin plats. När det är inaktivt är banan en del av 3d-scenen och rör sig med kameran och objekten.
* `Snitt` - Kurvan blir en ring runt formen, skuren genom dess två punkter i den riktning du tittade från.

##### Rörets övre verktygsfält {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
När ett rör är markerat visas ett verktygsfält med extra kontroller högst upp i vyn. Klicka på fältets rubrik för att fälla ihop eller fälla ut det, och klicka på pilen uppe till höger för att flytta fältet till vyns över- eller underkant.

* `Slutför` - Bakar röret till vanliga polygoner så att det kan skulpteras.
* `Redigera` - Visar kurvpunkterna så att de kan flyttas
* `Spegel` - Lägger till en spegel-repeater som förälder till kurvan
* `Snap` - Fäster kurvpunkterna mot närliggande ytor
* `Stängd` - Sammanfogar kurvans början och slut till en slinga
* `B-spline` - Växlar mellan Catmull-Rom- och B-spline-interpolering.
* `Hätta` - Växlar mellan hättor i båda ändarna av röret, bara i början eller slutet, eller inga hättor.
* `Hål` - Ger röret tjocklek och gör det till en ledning. Växlar mellan hål i båda ändarna, bara i slutet, eller inga hål.
* `Radie` - Växlar mellan en enhetlig radie, en radie i början och slutet, eller en radie per kurvpunkt. De redigeras med orange handtag på kurvan.
* `Twist` - Växlar mellan ingen vridning, en enhetlig vridning, en vridning i början och slutet, eller en vridning per kurvpunkt. De redigeras med rosa handtag på kurvan.
* `Profil` - Växlar mellan ingen profil (alltså en cirkulär profil), en enhetlig profil, en profil i början och slutet, eller en profil per punkt.
* `Profilredigering` - Visar en profilredigerare. Den fungerar som verktygen för [Formredigering](#shape-editing), kan spara och läsa in profilförinställningar och har en knapp för att redigera profilen i 3d-rymden.
* `Spiral` - Visar en meny för att ge röret en spiralvridning. Menyn har alternativen `Vridningsvinkel`, `Förskjutning`, `Skala` och `Vinkelförskjutning`.
* `X-indelningar` - Antalet indelningar runt röret; med 4 indelningar blir röret till exempel fyrkantigt.
* `Konstant densitet` - När det är aktivt hålls polygonerna kvadratiska. När det är avstängt kan du ställa in `Y-indelningar` längs rörets längd.
* `...` - Menyn med rörinställningar.

#### Växlingsknapp för att ta bort kurvpunkter {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Under verktygsfältet finns en knapp för att ta bort kurvpunkter. När du drar en kurvpunkt nära en annan blir den röd, vilket betyder att punkten tas bort om du släpper. Gör du små justeringar och inte vill ta bort punkter kan du stänga av borttagningen med den här knappen.



#### Rörinställningar {#tube-settings}
* `Primitiv` - Knappar för att aktivera eller inaktivera UV:er, eller för att slutföra röret.
* `Postdelning` - En genväg för att ställa in multiresolution-nivån innan du slutför.
* `Linjär indelning` - En genväg för att ställa in nivån för linjär indelning innan du slutför.
* `Division X` - Samma som X-indelningar i verktygsfältet.
* `Division Y` - Samma som Y-indelningar i verktygsfältet.
* `Kurva (Repeater)` - Omvandlar röret till en [kurv-repeater](scene.md#curve)

::: tip
Indelningar på 4 och Postdelning på 3 ger mjuka rör med rundade ändar, bra för maskar, ormar och kroppsdelar.
:::


### ![](/icons/tool_lathe.webp) Svarv {#lathe}
Skapar en rotationsyta genom att du ritar en kurva.

Det här verktyget är perfekt för former som vaser och vinglas.

![](/videos/tool_lathe.mp4)

#### Svarvens vänstra verktygsfält {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Det vänstra verktygsfältet har följande alternativ:

* `Synka` - Om den aktuella svarvformen är instansierad och dess barnnoder skiljer sig mellan instanserna synkroniseras de igen.
* `Fast` - När det är aktiverat är svarvens centrum fast och visas på skärmen. Mittlinjen har redigeringspunkter som kan justeras. När det är avstängt uppdateras svarvens centrum dynamiskt efter början och slutet av den ritade kurvan.
* `Visa` - Inget ritläge, så att du kan flytta kameran fritt.
* `Kurva` - Rita svarvens profil i ett enda drag. Det har en liten utfällbar meny:
    * `Redigera` - Vad som händer när du lyfter pennan, se [Markeringskontroller](#selection-controls): skapa svarvformen direkt, behåll kurvan redigerbar med en grön cirkel bredvid för att skapa den, eller `Håll` i slutet av penseldraget för att fortsätta redigera.
    * `Stängd` - Sammanfogar kurvans början och slut till en slinga
    * `Fortsätt rita` - Stanna kvar i verktyget efter att en svarvform har bekräftats, för att rita nästa.
    * `Noggrannhet` - Hur många kurvpunkter som används för att omvandla den ritade banan till ett rör. 0 % använder minsta möjliga antal punkter, men missar små krökningar i banan. 100 % är mycket noggrant och använder många punkter.
* `Bana` - Skapa en svarvform genom att klicka ut kurvpunkter. Tryck på den gröna cirkeln för att bekräfta banan. Det har en liten utfällbar meny:
    * `B-spline` - Ett alternativt sätt att rita kurvor, där kurvpunkterna oftast inte ligger direkt på kurvan, men resultatet kan bli mjukare än med standardmetoden.
    * `Stängd` - Gör röret till en slinga
    * `Skärm` - När det är aktivt är banan 'fastnålad' på skärmen, så att du kan flytta vyn och objektet medan banan ligger kvar på sin plats. När det är inaktivt är banan en del av 3d-scenen och rör sig med kameran och objekten.

#### Svarvens övre verktygsfält {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

När en svarvform är markerad visas ett verktygsfält med extra kontroller högst upp i vyn. Klicka på fältets rubrik för att fälla ihop eller fälla ut det, och klicka på pilen uppe till höger för att flytta fältet till vyns över- eller underkant.

* `Slutför` - Bakar svarvformen till vanliga polygoner så att den kan skulpteras.
* `Redigera` - Visar kurvpunkterna så att de kan flyttas
* `Spegel` - Lägger till en spegel-repeater som förälder till svarvformen
* `Snap` - Fäster kurvpunkterna mot närliggande ytor
* `Stabil` - När det är aktiverat är kurvprofilen barn till svarvens mittlinje. När det är avstängt kan mittlinjen redigeras utan att kurvan flyttas, vilket ger möjlighet till mer komplexa former.
* `Fokus` - Roterar vyn så att kurvprofilen ligger helt plant mot kameran.
* `Stängd` - Sammanfogar kurvans början och slut till en slinga
* `Hätta` - Om Stängd är avstängt: växlar mellan hättor i båda ändarna, bara i början eller slutet, eller inga hättor.
* `Hål` - Ger svarvformen tjocklek och gör den till en ledning. Växlar mellan hål i båda ändarna, bara i slutet, eller inga hål.
* `B-spline` - Växlar mellan Catmull-Rom- och B-spline-interpolering.
* `X-indelningar` - Antalet indelningar runt svarvformen; med 4 indelningar får svarvformen till exempel en fyrkantig profil.
* `Konstant densitet` - När det är aktivt hålls polygonerna kvadratiska. När det är avstängt kan du ställa in `Y-indelningar` längs formens längd.
* `...` - Menyn med svarvinställningar.

#### Svarvinställningar {#lathe-settings}
* `Primitiv` - Knappar för att aktivera eller inaktivera UV:er, eller för att slutföra formen.
* `Postdelning` - En genväg för att ställa in multiresolution-nivån innan du slutför.
* `Linjär indelning` - En genväg för att ställa in nivån för linjär indelning innan du slutför.
* `Division X` - Samma som X-indelningar i verktygsfältet.
* `Division Y` - Samma som Y-indelningar i verktygsfältet.
* `Kurva (Repeater)` - Omvandlar kurvprofilen till en [kurv-repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Infoga {#insert}
Placerar ett objekt på ytan av ett annat. Det används ungefär som stämpelverktyget, men för hela 3d-former.

Om du väljer en grundform i det vänstra verktygsfältet placerar ett klick-och-drag på valfri yta grundformen där du klickar, och draget bestämmer storleken. När du har dragit klart byter Infoga till läget [Transformera](#transform).

I instansläget skapar ett drag en ny instans och låter den glida över ytan. Storleken kopieras från den första formen, så på det här sättet kan du placera många lika stora instanser av ett objekt på andra ytor.

Du är inte begränsad till grundformer! Markera *vilken* form som helst i scenträdet, och om Infoga är i läget Instans eller Klona kan du dra ut kopior av det markerade objektet över vilken annan yta som helst.

Om ett objekt har en egen pivot används den som förankringspunkt. Se videon nedan.

Det vänstra verktygsfältet har också `Visa`, för att flytta kameran utan att infoga något, och `Synka`: när målobjektet är instansierat läggs det nya objektet till på alla andra instanser också.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformera {#transform}
Flytta, rotera och skala en modell direkt med 1 och 2 fingrar, oftast över ytan på ett annat objekt.

Det vänstra verktygsfältet har följande knappar:

* `Klona` / `Instans` - Gör en kopia eller en instans av objektet, se verktygsfältet för [Gizmo](#left-menu-toolbar).
* `Flytta` - Ett drag med ett finger flyttar objektet. När snap är aktivt glider objektet längs ytan under ditt finger.
* `Rotera` - Ett drag med ett finger roterar objektet. När snap är aktivt roteras det runt normalen på ytan under ditt finger.
* `Skala` - Ett drag med ett finger skalar objektet.

Ett verktygsfält högst upp i vyn har:

* `Mål` - Om verktyget flyttar objektet, dess grupp eller dess vertexer, precis som för [Gizmo](#left-menu-toolbar).
* `Snap` - Fäster modellen mot andra ytor.
* `Yta` / `Vertex` - Med `Snap`: fäster mot ytan, eller mot närmaste vertex.

Med Transformera kan du snabbt använda 2 av lägena genom att använda 2 fingrar:

* Dra ett objekt för att placera det. Sluta röra det första fingret, men lyft det inte från skärmen.
* Sätt ned det andra fingret på skärmen medan det första är kvar. När du drar med det andra fingret skalas objektet.
* Lyft det andra fingret och fortsätt dra med det första, så är objektet i flyttläge igen.

Du kan också byta det andra läget med ett tryck med andra fingret:

* Dra objektet för att placera det, sluta röra fingret, men lyft det inte från skärmen.
* Tryck med det andra fingret medan du håller kvar det första
* Verktyget byter till rotationsläge. Dra med det första fingret för att ställa in rotationen.
* Tryck med det andra fingret som förut, så byter verktyget tillbaka till flyttläge.

Det ger ett snabbt arbetsflöde för att klona objekt över ett annat, till exempel stenar över ett landskap. Lägg märke till att klonknappen också finns i det vänstra verktygsfältet så att den är lätt att nå:

* Använd Transformera för att flytta en sten på plats.
* Släpp, tryck på klonknappen
* Flytta den här stenen, rotera och skala efter behov
* Släpp, tryck på klonknappen
* Flytta den här stenen, och upprepa.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Med det här verktyget kan du flytta, rotera och skala objekt, och ändra deras pivot.

Handtaget i vyn har följande funktioner:

* `Flytta` - Dra i linjen med pilen för att flytta längs X/Y/Z. Dra i den persikofärgade punkten i mitten av gizmon för att flytta fritt i skärmplanet. Klicka på de röda, gröna och blå rutorna för att flytta i planen X/Y/Z.
* `Rotera` - Dra i de röda, gröna och blå cirklarna för att rotera runt X/Y/Z. Dra i sfären innanför cirklarna för att rotera fritt.
* `Skala` - Dra i de yttre röda, gröna och blå punkterna för att skala längs X/Y/Z. Dra i de yttre röda, gröna och blå konerna för att skala i planen X/Y/Z. Dra i den yttre persikofärgade cirkeln för att skala enhetligt.

![](/images/tool_gizmo.webp)

#### Noder och vertexer {#nodes-and-vertices}

Varje objekt i Nomad består av en nod och vertexer:

* `Nod` - Objektets 'handtag', som lagrar dess förflyttning, rotation och skala, den så kallade transformationsmatrisen.
* `Vertexer` - Punkterna som definierar objektets yta. De lagrar position och färginformation.

Om du har en enkel låda med 8 vertexer kan du flytta den antingen genom att ändra dess transformationsmatris eller genom att ändra vertexernas positioner. När du skulpterar vill du oftast ändra vertexerna, och när du flyttar objekt med gizmon vill du oftast ändra noden. Nomad låter dig göra båda.

#### Gizmons verktygsfält {#left-menu-toolbar}

Det vänstra verktygsfältet har:

* `Klona` - Gör en fristående kopia av det aktuella objektet, som du kan dra iväg med gizmon.
* `Instans` - Gör en instanskopia av det aktuella objektet. Objekten är länkade, så skulpteringsändringar på ett av dem syns på alla instanserna.
* `Pivot` - (Låsikonen, i stället för knappen `Sub`) När det är aktiverat kan gizmon flyttas och roteras utan att objektet flyttas. Precis som `Sub` kan du hålla den för en snabb ändring, eller trycka på den för att låta den vara på.

Ett verktygsfält högst upp i vyn har de övriga kontrollerna:

* `Mål` - Avgör om gizmon påverkar objektets nod eller dess vertexer:
    * `Auto` - Standard. Fungerar som `Grupp`, men om meshen har en mask eller symmetri är aktiverad fungerar det som `Vertice`.
    * `Vertice` - Tillämpar transformationen på vertexerna, med hänsyn till mask och symmetri. Det fungerar inte på grundformer som inte är slutförda, och instanser påverkas också.
    * `Objekt` - Flyttar bara det aktuella objektet och ignorerar symmetri och mask. Barnobjekt står kvar.
    * `Grupp` - Flyttar objektet och resten av dess hierarki och ignorerar symmetri och mask.
    * `Instans` - (Objekt och Grupp) Samma sak, men alla instanser av objektet flyttas med.
* `Pivot` - Ett popup-fönster för att snabbt placera pivoten, förklaras [nedan](#pivot).
* `Alla` / `Flytta` / `Rotera` / `Skala` - Visar alla gizmons handtag, eller bara de för att flytta, rotera eller skala.
* `Fäst` - Som standard flyttas gizmon till det markerade objektets pivot. När Fäst är aktiverat stannar gizmon där den är.
* `Rikta` - Växlar mellan att pivoten är riktad efter det aktuella objektet eller efter världen.
* `Snap` (rotation) - Gör att rotationsvärdena fäster i steg. Stegvärdet visas och kan ändras när snap är aktivt. Alternativet `Magnet` får rotationen att fastna vid ett steg när den passerar det och sedan röra sig fritt igen; stäng av det för att hoppa från steg till steg.
* `Snap` (förflyttning) - Gör att förflyttningsvärdena fäster i steg. Stegvärdet visas och kan ändras när snap är aktivt.

#### ![](/icons/reset.webp) Pivot {#pivot}
Med popup-fönstret `Pivot` i det övre verktygsfältet ändrar du snabbt pivoten. Pivotens position och orientering styr gizmon.

**Återställ**
* `Auto` - Objektets mitt, riktad efter dess transformation.
* `Mitten` - Flyttar pivoten till objektets mitt och behåller orienteringen.
* `Botten` - Flyttar pivoten till mitten av objektets undersida. Tryck igen för att använda världens omslutande låda i stället.
* `Topp` - Flyttar pivoten till mitten av objektets ovansida. Tryck igen för att använda världens omslutande låda i stället.
* `Objekt` - Flyttar pivoten till objektets origo, riktad efter dess transformation.
* `Mask` - Flyttar pivoten till mitten av det omaskerade området. Tryck igen för att byta till det maskerade området.
* `Rikta in` - Återställer rotationerna så att de är riktade efter världen och behåller positionen.
* `Vy` - Riktar pivoten efter den aktuella vyn och behåller positionen. Den följer inte kameran efteråt.

**Vid tryck (Pivot-läge)**

Bara aktivt när `Pivot` är på. Det avgör vad som händer när du trycker en gång på meshens yta:
* `Ingen` - Ingenting händer när du trycker på objektet
* `Normal` - Flyttar och roterar pivoten så att den riktas efter ytan där du trycker
* `Första` - Flyttar (men roterar inte) pivoten dit du trycker på ytan
* `Medial` - Flyttar pivoten till mitten av objektet, under den punkt där du trycker på ytan.

#### Inställningar för Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Kompakt` - Växlar gizmons layout så att de extra handtagen ligger utanför eller innanför rotationssfären
* `Gizmostorlek` - Gizmons storlek
* `Tjocklek` - Tjockleken på gizmons linjer
* `Opacitet` - Gizmons opacitet
* `Dölj vid interaktion` - Om gizmon ska döljas tillfälligt medan du drar i den

-----

* `Tröskel för tangentrullning` - Styr hur rotationen beter sig när du drar i cirkelhandtagen för att rotera runt X/Y/Z. Om värdet är 0 fungerar rotationen som en ratt: du drar runt i cirklar. Om värdet är 90 fungerar den som att dra i snöret på en jojo: du drar i en rak linje mot eller bort från där du först klickade. Värden mellan 0 och 90 kombinerar båda: under värdet blir det linjär rörelse, över värdet cirkelrörelse.
* `Numerisk inmatning` - När det är aktiverat öppnar ett enkelt tryck på gizmon ett fönster där du kan skriva in ett exakt värde för den axel du tryckte på.

::: warning
Verktygen [Gizmo](#gizmo) och [Transformera](#transform) har en egen kryssruta för symmetri, skild från symmetrin för skulptering!

Som standard är den här symmetrin avstängd.
:::

##### Matris {#matrix}
De exakta transformationsvärdena för objektet finns inte längre i Gizmons inställningar: de har flyttat till menyn `Transformera`, bland menyerna uppe till höger. Dess avsnitt `Matris` innehåller:

* ![](/icons/target.webp) `Flytta ursprung` - Flyttar objektet så att dess pivot hamnar i scenens mitt, origo.
* ![](/icons/bake.webp)  `Baka` - Fryser objektet där det är och sätter värdena för förflyttning och rotation till 0 och skalan till 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pivot` - Bakar pivoten: matrisvärdena motsvarar då var gizmons handtag befinner sig i världen.
* ![](/icons/reset.webp) `Återställ` - En genväg som sätter förflyttnings- och rotationsvärdena till 0 och skalan till 1, vilket flyttar och roterar objektet.

::: tip Baka eller baka till pivot
Skapa en låda, välj verktyget Gizmo och öppna och fäst menyn `Transformera`. Som standard är förflyttning och rotation 0 och skalan 1.

Aktivera pivotläget, flytta handtaget åt ena sidan och stäng av pivotläget. Pivoten har ändrats, men lägg märke till att förflyttningsvärdena fortfarande är 0.

Vill du se var pivoten *verkligen* är klickar du på knappen `Pivot` för att baka. Nu uppdateras förflyttningsvärdena. Lägg märke till att lådan inte rör sig under den här åtgärden, och inte heller i pivotläget.

Flytta och rotera lådan någonstans och tryck sedan på `Flytta ursprung`. Objektet flyttas så att pivoten hamnar i världens mitt, men rotationen lämnas oförändrad.

Klicka på `Återställ`, så sätts även rotationen till 0.

Flytta och rotera lådan igen, och klicka den här gången på `Baka`. Pivoten stannar där den är, lådan stannar där den är, men förflyttnings- och rotationsvärdena sätts till 0.

Öva på det här några gånger! Lär dig förstå att pivotvärdena är dolda och att Nomad sköter dem åt dig, men om du behöver placera pivoten på verkliga positioner i rymden gör baka pivot det åt dig.

:::

* `Förflyttning` - Förflyttningsvärdena för X, Y och Z
* `Rotation` - Rotationsvärdena för X, Y och Z
* `Skala` - Den enhetliga skalan om det är aktiverat, annars skalan för X, Y och Z.
* `Skevhet` - Skevhetsvärdena (skjuvning) för X, Y och Z, visas bara när objektet redan är skevt
* `Jamförd skala` - Växlar mellan att skala enhetligt eller oberoende längs varje axel

Till vänster kan du flytta gizmons pivot, se videon nedan i praktiken.
Det är särskilt användbart för rotation, eftersom det inte ändrar något för förflyttning.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Ytgrupp {#facegroup}

Med ytgrupper delar du upp ditt objekt i ytor med olika färger. Du kan använda grupperna på många sätt i Nomad:

* Ett snabbt sätt att markera för masker
* Dölja eller visa delar av ditt objekt
* Organisera ditt objekt utan att behöva dela upp det i separata delar
* Definiera UV-områden
* Styra quad remeshern
* Extra kontroll för verktyg som Jämna ut.

#### Ytgruppens vänstra verktygsfält {#facegroup-left-toolbar}

* `Grupp` - Knappen visar den aktuella ytgruppen. Tryck på den för att visa de tillgängliga ytgrupperna som färgrutor och välja en. Tryck på en ruta för att byta namn på den, ändra dess färg eller ta bort den. `Ta bort oanvänd` tar bort rutor som inte används, och `Återställ` tar bort alla. Plusikonen skapar nya rutor.
* `Punkt` - Måla på objektet för att definiera ytgrupper. När '+ Ytgrupp' är aktiverat skapar varje nytt penseldrag automatiskt en ny ytgrupp, praktiskt för att snabbt definiera områden. Ett tryck fyller det valda området. Reglaget anger punktens radie.
* `Slappna av` - Jämnar ut ytgruppernas gränser. Mycket användbart för att få rena kanter inför quad-omnätning, eller för att definiera paneler vid hårdytemodellering. Reglagen styr radie och intensitet för avslappningen.
* Former - Skapa ytgrupper med former i stället för pensel, via `Lås + radie`, `Lasso`, `Polygon`, `Linje`, `Rekt` och `Ellips`. Se [Markeringskontroller](#selection-controls) för mer information.
* `Välj` - Sub-läget. När det är aktiverat väljs rutan där penseldraget börjar, och den används sedan under resten av draget. Mycket användbart för att städa upp ytgrupper: om en ytgrupp har spridit sig för långt aktiverar du `Välj`, börjar ett penseldrag där ytgruppen är rätt och drar fram till gränsen för att tilldela rätt ruta igen.

#### Ytgruppens övre verktygsfält {#facegroup-top-toolbar}

Ett verktygsfält högst upp i vyn har extra kontroller:

* `Slappna av (Alla)` - Dra för att slappna av gränserna för alla ytgrupper på en gång.
* `Fram` / `Synlig` / `Anslutna` - Samma filter för penseldrag som i verktygsfältet för [Mask](#mask).
* `Från normaler` - Skapar ytgrupper utifrån vinkeln mellan ytor. Popup-fönstret har `Vinkel` och låter dig hoppa över små grupper utifrån deras `Antal ansikten` eller `Ytområde`, med `Förhandsgranska` innan du bekräftar.
* `Från delar` - Skapar en ytgrupp för varje separat del.
* `Från UV` - Skapar en ytgrupp för varje UV-ö.
* `Från mask` - Skapar en ytgrupp av det maskerade området.
* `På tryck` - Välj vad ett tryck på en ytgrupp gör: fyll den med den aktuella ytgruppen, dölj den, maskera den eller `Pose` (den tryckta gruppen och det som ligger bortom den avmaskeras, och gizmon hamnar i leden, med ett reglage för `Sudda` för masken). En andra knapp `På tryck`, tillgänglig när meshen har en mask, begränsar trycket till ytorna på samma sida av masken.
* Knappar för `Rensa` till verktygen [Dölj](#hide) och [Mask](#mask), för att visa allt igen eller rensa masken utan att lämna verktyget.

#### Inställningar för Ytgrupp {#facegroup-settings}

Menyn `Verktyg` extraherar ytgrupper till nya objekt, med samma alternativ som `Extrahera` i [inställningarna för Mask](#mask-settings). Knappen `Ytgrupp` högst upp väljer vilka grupper som extraheras, och det finns ett extra reglage för `Mellanrum`: det flyttar varje gräns inåt längs ytan, och ett negativt värde flyttar den utåt så att delarna överlappar. För angränsande paneler använder du halva det önskade mellanrummet.

### ![](/icons/tool_hide.webp) Dölj {#hide}
Döljer eller isolerar delar av objektet.

Huvudlägena styrs från det vänstra verktygsfältet:

* `Punkt` - Måla på objektet för att dölja delar av det.
* Former - Dölj med former i stället för pensel, via `Lasso`, `Polygon`, `Linje`, `Rekt` och `Ellips`. Se [Markeringskontroller](#selection-controls) för mer information.
* `Visa` - Sub-läget. Inverterar åtgärden, så att det valda läget visar delar av objektet i stället för att dölja dem.

Ett verktygsfält med extra kontroller visas högst upp i vyn:

* `Rensa allt` - Återställer objekten så att alla dolda delar visas igen. När även andra objekt har dolda delar återställer en extra knapp `Rensa` bara de markerade objekten.
* `Invertera` - Byter plats på dolda och synliga delar.
* `Radera` - Tar bort den dolda delen av objektet
* `Dela` - Delar av den dolda delen av objektet till en ny form.
* `Fram` / `Synlig` / `Anslutna` - Samma filter för penseldrag som i verktygsfältet för [Mask](#mask).
* `På tryck` (ytgrupp) - Använd ytgrupper för att snabbt dölja delar: ett tryck på en ytgrupp döljer hela ytgruppen.
* `På tryck` (mask) - Om en mask är aktiv döljer ett tryck den maskerade delen.

### ![](/icons/tool_measure.webp) Mät {#measure}
Dra för att mäta avståndet mellan 2 punkter. När mätningen är placerad kan du dra i ändpunkterna för att justera den.

Det vänstra verktygsfältet väljer hur avståndet mäts:

* `Linje` - En rak linje mellan de två punkterna.
* `Yta` - Avståndet längs ytan, efter snittet genom de två punkterna sett från kameran.
* `Tvärsnitt` - Omkretsen av tvärsnittet genom de två punkterna, som ett måttband runt en arm.
* `Vertex` - Fäster ändpunkterna mot närmaste vertex.
* `Gyllene snitt` - Visar en gul punkt vid mätningens gyllene snitt.
* Knappen `?` visar volym, ytarea och storlek för de markerade objekten.

### ![](/icons/tool_arrange.webp) Ordna {#arrange}
Rada upp och placera ut flera objekt på en gång, som justeringsverktygen i ett 2d-designprogram. Markera objekten först; med ett enda objekt verkar Ordna i stället på dess separata delar. En låda ritas runt markeringen, och du drar i dess handtag för att skala den.

Ett verktygsfält högst upp i vyn har kontrollerna:

* `Värld` / `Skärm` - Ordna längs världens axlar, eller längs skärmen (vänster, höger, upp, ned).
* `Rikta` - Riktar in objekten efter deras minimum, mitt eller maximum, på varje axel.
* `Fördela` - Fördelar objekten jämnt mellan de två yttersta, efter deras minimum, mitt eller maximum. Det kräver minst 3 objekt.
* `Linje` - Ställer objekten i en rad längs en axel.
* `Rutnät` - Ställer objekten i ett rutnät, med ett antal objekt längs `X`, `Y` och `Z`.
* `Cirkel` - (endast Värld) Ställer objekten i en cirkel runt axeln `X`, `Y` eller `Z`.
* `Sfär` - (endast Värld) Fördelar objekten över en sfär.

`Linje`, `Rutnät`, `Cirkel` och `Sfär` har alla ett reglage för `Mellanrum` som anger avståndet mellan objekten.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Det här verktyget omvandlar det markerade objektet till en ren topologi av fyrhörningar, med kontroller för täthet, kantflöde och symmetri.

::: tip
Quad Remesher utvecklas av [Exoside](https://exoside.com/) för iOS och dator.

På iOS är det ett köp inuti Nomad, en engångsbetalning på 16 USD.

För dator köper du en licens från [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Du kan köpa den enbart för Nomad på dator, eller en korslicens för alla datorprogram som stöds.

Om du redan äger Quad Remesher för ett annat datorprogram kan du [köpa en uppgradering till alla plattformar till ett lägre pris.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher finns inte för Android. På Android kan du använda de fria omnätarna med öppen källkod under fliken [Quad-omnätning](topology.md#quad-remesh) i Topologi (AutoRemesher, Instant Mesh, QuadriFlow), men räkna med att deras funktioner är mer begränsade.
:::

Så länge Quad Remesher inte är upplåst börjar det övre verktygsfältet med en kundvagnsknapp i stället för omnätningsknapparna. På iOS öppnar den köpet i appen. På dator visar den `Lås upp (köp, återställ, testning)`, som kontrollerar din Exoside-licens (eller startar provperioden). När det är aktivt aktiveras det vänstra och det övre verktygsfältet.

* `Punkt` - Den här penseln anger måltätheten. Intensitet 100 % målar i rött, vilket ger dubbla måltätheten av fyrhörningar i de områdena. Intensitet 0 % målar i cyan, vilket ger halva måltätheten i de områdena. Intensitet 50 % målar i grått, vilket ger standardtätheten.
* `Jämna ut` - Jämnar ut övergångarna mellan rött, grått och cyan.
* `Smeta ut` - Smetar ut tätheten som du har målat.
* `Kurva` - Skissa kurvor på skulpturens yta; quad remeshern använder dem som guider för kantflödet. Tryck på en kurva för att ta bort den.
* `Bana` - Rita banor på skulpturens yta; quad remeshern använder dem som guider för kantflödet. Tryck på en bana för att ta bort den.
* `Rekt` - Rita rektanglar på skulpturens yta; quad remeshern använder dem som guider för kantflödet. Tryck på en rektangel för att ta bort den.
* `Ellips` - Rita ellipser på skulpturens yta; quad remeshern använder dem som guider för kantflödet. Tryck på en ellips för att ta bort den.

#### Quad Remeshers övre verktygsfält {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Ett verktygsfält med extra kontroller visas högst upp i vyn:


* `<Antal>` - Klicka här för att starta omnätningen. Talet visar hur många fyrhörningar omnätningen siktar på.
* `Quads` - Ställ in målantalet fyrhörningar genom att dra åt vänster och höger, eller tryck för att skriva in ett exakt tal. Observera att det är en riktlinje snarare än ett fast tal: de olika kontrollerna i quad remeshern gör ofta att resultatet inte exakt motsvarar målet.
* `Halv` - En genväg som sätter målantalet till hälften av det nuvarande antalet polygoner.
* `Samma` - En genväg som sätter målantalet till det nuvarande antalet polygoner.
* `Guider` - Växlar mellan att använda eller ignorera guiderna. När det finns guider visar en andra knapp `Guider` hur många de är; tryck på den för att ta bort alla.
* `Täthet` - Växlar mellan att använda eller ignorera den målade tätheten. När det finns målad täthet tar en andra knapp `Täthet` bort den.
* `Ytgrupp` - Växlar mellan att använda eller ignorera ytgrupper för att styra quad remeshern.
* `Slappna av` - Växlar automatisk avslappning av ytgruppernas gränser under omnätningen. Om du redan har slappnat av eller jämnat ut gränserna kan du stänga av det här alternativet.
* `Slappna av-reglage` - Ett genvägsreglage för att slappna av ytgruppernas gränser.
* `Hårda kanter` - Försöker behålla hårda kanter.
* `Reprojektera vertex` - Reprojicerar den nya layouten på den ursprungliga meshen.
* `Sym` - Ger ett symmetriskt resultat. Observera att symmetrin alltid beräknas kring världens x-axel, så se till att modellen ligger i origo om du förväntar dig ett symmetriskt resultat.
* `...` - Popup-fönster med inställningar för Quad Remesher.

#### Inställningsmeny för Quad Remesher {#quad-remesher-settings-menu}

Knappen `...` i slutet av det övre verktygsfältet öppnar ett popup-fönster med resten av inställningarna:

* `Adaptiv Kvadrattal` - Använder mindre fyrhörningar i områden med stark krökning och större i områden med svag krökning.
* `Adaptiv storlek` - Anger hur mycket anpassning som görs. 100 % tillåter maximal anpassning av storleken, vid 0 % blir fyrhörningarna enhetliga.

::: tip

Ett recept för en bra quad-omnätning med minimalt med artefakter:

* Dela in meshen i ytgrupper som visar ditt ideala flöde av fyrhörningar.
* Slappna av ytgrupperna för att få mjuka gränser.
* Decimera. Då slipper du tunna eller förvrängda ytor längs ytgruppernas kanter. Se till att ytgrupp är aktiverat i inställningarna för decimering, så följer triangelkanterna exakt dina ytgruppskanter.

Se till att Slappna av är avstängt i alternativen för quad-omnätning (du har ju redan slappnat av meshen), så bör du få bra resultat.

:::

### ![](/icons/tool_select.webp) Välj {#select}
Använd formlägena (`Lasso`, `Rekt`, `Ellips`) för att markera objekt i scenen. `Avmarkera` tar bort objekt från markeringen.

### ![](/icons/tool_lattice.webp) Galler {#lattice}
Deformerar ett objekt med en bur av kontrollpunkter runt det, i stället för att skulptera dess yta. Genom att flytta några få punkter i buren böjer, vrider eller sträcker du hela objektet mjukt, perfekt för att justera proportioner eller posera utan att röra topologin. Deformationen förblir aktiv tills du slutför den.

Det vänstra verktygsfältet väljer hur du redigerar buren:

* `Punkter` - Dra direkt i burens punkter och kanter. Tryck på en punkt för att markera den.
* `Visa` - Flytta kameran utan att redigera buren.
* `Slappna av` - En pensel som slappnar av burpunkterna under den.
* `Elastisk` - En pensel som drar i burpunkterna med en elastisk avtoning, som verktyget [Elastisk](#elastic).
* `Gizmo` - Flytta, rotera och skala de markerade punkterna med gizmon. Dess sub-läge är `Pivot`.
* `Lasso` - Markera burpunkter med en lasso; `Avmarkera` tar bort dem från markeringen.

Formens popup-fönster har också `Mjuk radie`, som gör att drag i en punkt även flyttar grannpunkterna (i rutnätsceller, 0 flyttar bara markeringen), och `Invertera urval`.

Ett verktygsfält högst upp i vyn har:

* `Slutför` - Tillämpar deformationen på objektet och tar bort buren.
* `Återställ` - Tar bort buren och dess deformation.
* `Opacitet` - Burens opacitet på skärmen.
* `Spegelsidan` - Med symmetri: växlar vilken spegelsida av buren som visas och kan väljas, med en egen `Opacitet` för den dolda sidan.
* `Rutnätspunkter` - Vilka punkter i buren som kan flyttas: hela rutnätet, ytan och mittpunkten, eller bara ytan.
* `Styvhet` - Hur stel deformationen är, från mjuk (0 %) till stel och linjär (100 %).
* `Avtoning` - Hur långt utanför buren deformationen avtar.
* `Rikta` - Riktar buren efter objektet eller efter världen.
* `X`, `Y`, `Z` `Indelning` - Antalet celler i buren längs varje axel. Lägesknappen bredvid anger hur de hänger ihop: `x = y = z` använder samma antal på alla 3 axlar, `Enhetlig` behåller samma avstånd mellan punkterna på alla axlar, och med `Anpassad` ställer du in varje axel fritt.

#### Inställningar för Galler {#lattice-settings}
* `Rullhastighet` - Samma rullningsalternativ som för verktyget [Flytta](#move-settings), används när du drar i burpunkter.

### ![](/icons/tool_view.webp) Vy {#view}
Det här "verktyget" gör inget särskilt, det är helt enkelt ett sätt att titta på modellen utan att ändra något i scenen.

#### Inställningar för Vy {#view-settings}
Medan verktyget Vy är aktivt åsidosätter de här inställningarna vissa visningsalternativ, så att du får en ren vy när du presenterar eller granskar din modell:

* `Primitiv (Redigera)`, `Repeater (Redigera)`, `Ljus (Redigera)`, `Kamera (Redigera)` - Tillåter att grundformer, repeaters, ljus och kameror redigeras i vyn medan du är i verktyget Vy. Stäng av dem för att inte flytta deras handtag av misstag.
* `Kameragenväg (alltid)` - Visar alltid kamerans genvägsknappar i vyn.
* `Visa mask`, `Kontur`, `Mörka ej valda objekt` - Visar masken, konturen runt de markerade objekten, eller gör de omarkerade objekten mörkare. `Auto` följer din vanliga inställning, `Nej` och `Ja` tvingar fram den.
* `Visa linje (Symmetri)`, `Visa plan (Symmetri)` - Visar symmetrilinjen eller symmetriplanet, med samma val `Auto`, `Nej` och `Ja`.
* `Ikon` - Visar ikonerna för grupper, repeaters, ljus, kameror och hierarkin i vyn, med samma val.


## Verktygslådans snabbmeny {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Högerklicka eller håll fingret på ett verktyg i verktygslådan för att öppna en snabbmeny. Menyn har följande alternativ:

* `Spara` - Sparar ändringarna du har gjort i verktyget
* `Klona` - Duplicerar verktyget till en ny verktygsgenväg
* `Senaste sparning` - Återgår till verktygets senast sparade version
* `Ikon` - Byter verktygets ikon. När verktyget har en egen ikon tar den här knappen bort den.
* `→ ...` - Flyttar verktyget till en annan mapp i verktygslådan, eller till en ny
* `Återställ` - Återställer verktyget till standardinställningarna

Klonade verktyg har också `Byt namn` och `Radera`.
