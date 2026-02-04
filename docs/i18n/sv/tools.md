# ![](/icons/toolbox.webp) Verktyg {#tools}

![](/images/tools_menu.webp)

::: tip
Hoppa ner till [Verktyg](#verktyg-1) för beskrivningar av de enskilda verktygen.
:::

## Översikt {#overview}

Verktyg väljs från `Toolbox` till höger och styrs med `Tool Controls` till vänster. Extra inställningar finns i menyn `Settings`, den första ikonen i menyn uppe till höger.

Penselverktyg har kontroller för storlek och intensitet. Markeringsverktyg har kontroller för flera markeringsstilar. Längst ner i verktygskontrollerna finns genvägar för ofta använda operationer (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Nomads verktyg är färgkodade i verktygslådan:

* <span class=brush>**Penselverktyg**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Flyttverktyg**</span> (Move, Drag)
* <span class=mask>**Maskverktyg**</span> (Mask, SelMask)
* <span class=paint>**Målarverktyg**</span> (Paint, Smudge)
* <span class=flatten>**Plattningsverktyg**</span> (Flatten, Planar)
* <span class=pinch>**Nypverktyg**</span> (Crease, Pinch)
* <span class=selection>**Markeringsbaserade verktyg**</span> där en 2d-mask ritas först, sedan utförs en operation (Trim, Split, Project)
* <span class=creation>**Skaparverktyg**</span> (Tube, Lathe, Insert)
* <span class=transform>**Transformationsverktyg**</span> (Transform, Gizmo)
* <span class=misc>**Övriga verktyg**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Visningsverktyg**</span>



Många av dessa verktyg kan anpassas med olika penselbeteenden, tryck, texturer osv via menyn [Stroke](stroke.md). 


### Penselkontroller {#brush-controls}

Verktygsfältet till vänster har reglage för radie och intensitet, och sedan verktygskategori-specifika kontroller, förklarade nedan.

![](/images/tool_left_panel.webp)

::: tip
Intensitetsreglaget för många verktyg kan gå över 100 %, värt att experimentera med!
:::

### Undermenyläge {#sub-mode}
Knappen direkt under intensitetsreglaget är `Sub`-knappen. Dess etikett och funktion ändras med varje verktyg, och när den trycks ned aktiveras ett alternativt, oftast motsatt beteende. T.ex. för [Paint](#paint) aktiveras ett raderingsläge, för [Crease](#crease) skapas upphöjda kanter istället för skåror osv.

Som standard fungerar den som en ”klistrig” knapp; dvs du kan hålla den nedtryckt för att tillfälligt aktivera den, när du släpper den stängs den av. Om du trycker snabbt på den aktiveras sub-läget permanent.

### Genvägar {#shortcuts}
Längst ner i verktygsfältet till vänster finns genvägar för [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Som standard fungerar alla dessa som ”klistriga” knappar; dvs du kan hålla dem nedtryckta för att tillfälligt aktivera dem, när du släpper dem stängs de av. Om du trycker snabbt på dem aktiveras genvägsläget permanent.

### Urvalskontroller {#selection-controls}

Verktygen [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) och [Hide](#hide) använder liknande kontroller för att välja områden av meshen.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - En frihandsritad form
* `Polygon` - En sluten form definierad av en kombination av kurvor och/eller raka linjer. Se [Shape editing](#shape-editing) nedan för mer info.
* `Curve` - (endast Project) - En frihandskurva för projektionen
* `Path` - (endast Project) - En kurva definierad av punkter. Se [Shape editing](#shape-editing) nedan för mer info.
* `Line` - Dra en linje för att definiera ett plant segment. Som standard verkar den på meshen direkt, stäng av auto validate om du inte vill detta (långtryck eller svep på linikonen)
* `Rect` - Dra en diagonal linje, detta definierar hörnen på en rektangelform. Långtryck eller svep för att visa alternativ för auto validate, tvinga till kvadratisk form, och för att första klicket ska vara rektangelns centrum.
* `Ellipse` - Dra en diagonal linje, detta definierar storleken på en ellips. Långtryck eller svep för att visa alternativ för auto validate, tvinga till cirkelform, och för att första klicket ska vara ellipsens centrum.
* `Flip` - invertera formmasken, eller riktningen på project-verktyget.

De flesta verktyg har ett alternativ för auto validate, vilket betyder att operationen sker så snart du har ritat klart formen. När auto validate är avstängt ritas en grön knapp bredvid formen som utför operationen. Detta låter dig redigera formen, justera vyn, och när du är redo att använda formen trycker du på den gröna knappen.

### Formredigering {#shape-editing}
Polygonredigering och kurvredigering beter sig på liknande sätt:

* För att börja, dra en linje för att definiera 2 punkter, dra sedan ut från mitten av linjen för att definiera en polygon eller kurva.
* Klicka på punkterna för att växla mellan mjuk och skarp.
* Klicka och dra på kurv- eller linjesektioner för att skapa nya punkter.
* För att ta bort en punkt, dra en punkt in i dess granne tills den blir röd.
* Papperskorgsikonen i hörnet på polygon- eller path-ikonen tar bort formen.

### Inställningsmeny {#settings-menu}

Många verktyg har extra inställningar som finns i menyn Settings, den första ikonen i menyn uppe till höger:

![](/images/tools_settings_menu.webp)

## Verktyg {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Lera {#clay}
Clay-verktyget är användbart för att bygga upp din skulptur. `Sub` tar bort material från din skulptur.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pensel {#brush}
Standardpenseln. `Sub` tar bort material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Flytta {#move}
Området under penseln kommer att ”fastna” vid penseln, vilket möjliggör elastisk deformation. Markeringen bibehålls under förflyttningen, så om du flyttar penseln bort och sedan tillbaka dit du började ser du ingen deformation.

Sub-läget är `Normal` och flyttar området under penseln längs ytnormalen.

Den här penseln är bra både för deformation i stor skala och för noggrann smådeformation.

#### Inställningar för Flytta {#move-settings}

* `Radius (Background)` - Hur långt från kanten av en modell du kan vara och ändå skulptera, användbart när du arbetar med siluetten av ett objekt. 
* `Same-side vertex only` - Ignorera verticer som pekar i motsatt riktning mot deformationen.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Dra {#drag}
Området under penseln kommer att ”fastna” vid penseln, vilket möjliggör elastisk deformation. Till skillnad från Move-penseln uppdateras markeringen kontinuerligt under draget, så det är möjligt att skapa längre, ormliknande objekt, särskilt när Dynamic Topology är aktiverat.

Sub-läget är `Normal` och flyttar området under penseln längs ytnormalen.

Den här penseln är bra för mer lösa, gestuella formförändringar.

#### Inställningar för Dra {#drag-settings}

* `Radius (Background)` - Hur långt från kanten av en modell du kan vara och ändå skulptera, användbart när du arbetar med siluetten av ett objekt. 
* `Same-side vertex only` - Ignorera verticer som pekar i motsatt riktning mot deformationen.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Jämna ut {#smooth}
Jämnar ut området genom att medelvärdesbilda punktpositionerna. Detta verktyg är starkt beroende av polygontätheten.
Om du har många polygoner blir utjämningen mindre effektiv.

Sub-läget är `Relax`, vilket bara jämnar ut wireframen men försöker behålla de geometriska detaljerna.

#### Inställningar för Jämna ut {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Ytgrupp {#smooth-facegroup}

* `Relax` - Jämnar ut kanterna på facegrupper. Använd intensitet större än 100 % för att snabbt jämna ut kanter. `Auto` jämnar bara ut om förhandsvisning av facegrupper är aktiverad, `Off` inaktiverar, `On` aktiverar. 

##### Vertex {#vertex}
* `Sticky vertex on border` - För mesher med öppna kanter, t.ex. ett plan, är det möjligt att jämna ut hörnen. Om detta alternativ aktiveras låses de öppna kanterna.
* `Relax` - samma som relax-alternativläget i verktygsfältet till vänster.
* `Stable smoothing` - Försöker göra utjämningen oberoende av topologi. Detta fungerar bäst med varierande topologitäthet och med ett högt värde på utjämningsintensiteten.

##### Målning {#painting}
* `Screen Smoothing` - Använd detta alternativ för att få topologioberoende utjämning, även vid höga polytal.
* `Screen samples` - Kvaliteten på utjämningen, högre värden blir jämnare men långsammare.

::: tip
Högre polygontäthet kan kräva att intensiteten höjs över 100 %. Mycket höga värden (300 %, 500 %) kan också fungera bra som skulpteringsverktyg, som tvingar områden att snabbt bli plana och släta under penseln, som att slå lera med en klubba!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask {#mask}
Detta verktyg låter dig maskera verticer. Maskerade verticer är skyddade från skulptering eller målning. 

Sub-läget är `Unmask` och raderar där masken har målats.

Liknande markeringar i 2D-målningsprogram kan masker målas med en pensel, eller skapas med formmarkeringar, suddas eller skärpas. 

Till skillnad från 2D-målningsprogram kan de också skapas via facegrupper, och masker kan användas för att skapa ny geometri via extruderings-/extraktionsliknande operationer. 

![](/videos/tool_mask1.mp4)

 En verktygsrad visas längst upp i vyn med extra kontroller. 

![](/images/tool_mask_toolbar.webp)

Titeln på raden kan tryckas på för att fälla ut/fälla ihop, eller så kan pilen uppe till höger tryckas på för att flytta den till över- eller underkanten av gränssnittet.

| Åtgärd                                            | Beskrivning                                                                               |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Clear             | Rensa masken                                                                              |
| ![](/icons/invert.webp)        Invert            | Invertera masken                                                                          |
| ![](/icons/sharpen.webp)       Sharpen           | Skärp maskkanten                                                                          |
| ![](/icons/blur.webp)          Blur              | Suddar maskkanten                                                                         |
|                                 Blur ->           | Dra vänster/höger för att interaktivt sudda masken                                       |
| ![](/icons/culling.webp)       Front             | Växla till att bara maskera framåtvända verticer                                         |
|                                 Convert           | Konvertera masken till en facegroup                                                      |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | När aktiverad visas facegrupper, och att trycka på en facegroup maskerar den             |
|                                 On tap (mask)     | När aktiverad kommer ett tryck på en ”ö” av mask eller omaskerade polygoner att fylla den ön. |
| ![](/icons/vertex.webp)        Connected         | När aktiverad tillåts endast maskdrag att påverka sammanhängande topologi.               |

##### Snabbrörelse för mask {#mask-quick-gesture}
Du kan utföra ZBrush-liknande gester medan du håller ned snabbmaskningsknappen i verktygsfältet till vänster:
| Åtgärd | Gest (håll ned nedre vänstra genvägen) |
| :----: | :-------------------------------------: |
| Invert | Tryck på bakgrunden                    |
| Clear  | Dra på bakgrunden                      |
| Blur   | Tryck på maskerat område               |
| Sharpen| Tryck på omaskerat område              |


#### Maskinställningar {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Maskinställningsmenyn används främst för att skapa geometri från masken. Därför är standardbeteendet att förhandsvisa hur den nya geometrin kommer att se ut. Du kan välja att inte ha någon förhandsvisning, en extract-förhandsvisning, en split-förhandsvisning, och om denna geometri ska visas i röntgenläge.

##### Tjocklek {#thickness}
* `Height` - Höjden på den extraherade formen. Plus/Minus-ikonen låter dig växla mellan en utåtgående extrudering, inåtgående, eller centrerad. 
* `Height/Height+Mask` - Växla mellan att höjden är konstant, eller om suddade delar av masken ska påverka höjden, vilket möjliggör mjuka och varierande höjdformer. 

##### Jämnhet {#smoothness}
När aktivt jämnar det ut kanten på den extraherade formen, fungerar bättre med högre polygontal. 
* `Iterations` - Mängden utjämning som appliceras. Höga värden ger mycket släta böjda kanter, men börjar avvika från maskformen.
* `All/Sharp border/Borders only` - Utjämning kan fungera i alla riktningar, jämna både sidor och topp på den extraherade formen, eller jämna topp och sidor men behålla en skarp kant, eller bara jämna kanten och lämna toppytan opåverkad.

##### Kantloop (sida) {#edge-loop-side}
* `Auto Edge-loop (side)` - Beräknar antalet indelningar på sidorna av den extraherade formen för att skapa fyrkanter som matchar polygonerna i det maskerade området. När inaktiverat kan du själv ställa in antalet edge loops med edge loop-reglaget.

----

##### Extrahera {#extract}
* `Extract` - Skapa den extraherade geometrin.
* `Closing action` - Hur extract ska bete sig. ”None” duplicerar de maskerade polygonerna till en ny form. ”Fill” gör samma sak och försöker lappa baksidan. ”Shell” extruderar till värdet som ställts in i ”thickness” och är standardläget.

::: tip

Om förhandsvisningen är i ”Extract”-läge med ”X-ray” aktiverat kan det vara förvirrande första gången du klickar på Extract-knappen. Eftersom menyn är aktiv försöker den förhandsvisa en extraktion på din nya form och röntga den ursprungliga ytan. Men eftersom du inte har någon mask på den nya ytan kan den inte förhandsvisa extraktionen, och Nomad varnar dig med ”Nothing to Extract!”. 

Detta är normalt, stäng maskinställningsmenyn för att se den nya formen och originalet, och välj originalytan igen om du behöver rensa masken eller rita nya masker.
:::

##### Dela upp {#split-mask}
* `Split` - Extraherar både de maskerade OCH omaskerade regionerna till nya former. 
* `Closing action (masked)` - Hur mask-extraktionen ska bete sig. ”None” duplicerar de maskerade polygonerna till en ny form. ”Fill” gör samma sak och försöker lappa baksidan. ”Shell” extruderar till värdet som ställts in i ”thickness” och är standardläget.
* `Closing action (unmasked)` - Hur den omaskerade extraktionen ska bete sig. ”None” duplicerar de maskerade polygonerna till en ny form. ”Fill” gör samma sak och försöker lappa baksidan. ”Shell” extruderar till värdet som ställts in i ”thickness” och är standardläget.
* `Sync border` - Säkerställ att kanten mellan de maskerade och omaskerade extraherade formerna håller sig nära varandra. När inaktiverat kan ett glapp uppstå mellan formerna eftersom shell-operationen extruderar varje yta längs sin normal.

##### Karva {#carve}
* `Carve` - I standardläge beter det sig som om du hade trimmat in i ytan med ”thickness”-värdet, som att skära ut en bit apelsinskal. 



### ![](/icons/tool_maskSelector.webp) Urvalsmask {#selection-mask}
Detta verktyg liknar mest [Masking-verktyget](#mask), den största skillnaden är att du inte använder stroke för att måla mask, utan istället använder [Markeringskontrollerna](#selection-controls).

Sub-läget är `Unmask` och raderar masken med hjälp av markeringskontrollerna.

Selection Mask delar samma verktygsinställningar som verktyget `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Måla {#paint}
Applicera färg och materialegenskaper. För att lära dig mer om material kan du besöka avsnittet [Painting](painting.md).

Sub-läget är `Erase` och tar bort färg.

#### Målningsinställningar {#paint-settings}
* `Layer fitering` - Detta fungerar som lagerets alpha lock i Photoshop eller Procreate. Om du målar på ett lager kan du, när detta är aktiverat, bara ändra där färg redan finns; omålade områden skyddas.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smeta {#smudge}
Smeta ut färg och materialegenskaper. Menyn för Smudge innehåller ett reglage `Quality`, lägre värden ger snabbare drag.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Platta till {#flatten}
Plattar till området genom att projicera punkterna på det genomsnittliga planet.

Sub-läget är `Fill` och definierar ett plan satt av den högsta punkten, och tenderar att dra upp punkter.

#### Inställningar för Platta till {#flatten-settings}

* `Lock plane direction` - Använd plandriktningen som beräknas vid första klicket. Som standard är detta inaktiverat.
* `Lock plane origin`- Använd första klicket som planets centrum. Som standard är detta inaktiverat.

När en eller båda av dessa är inaktiverade kan Flatten gradvis fördjupas eller planvinkeln ändras genom att använda långa drag som rör sig över olika djup och krökningar. Detta i kombination med områdessamplingsalternativen i penselmenyn kan ge mycket exakt kontroll.

::: tip
När du arbetar i områden med hög krökning, t.ex. när du försöker platta till kinderna men verktyget hela tiden påverkar sidorna av näsan, försök skapa en mask för att skydda områden som Flatten-penseln inte ska påverka.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Plan {#planar}
Gör punkter plana genom att projicera dem på det genomsnittliga planet, men med mindre uppbyggnad än Flatten-penseln. Detta skapar renare hårda ytor. Snabba drag trycker och drar mer på ytan, långsammare drag som börjar från redan plana områden och arbetar utåt bibehåller planet bättre.

Sub-läget är `Fill` och definierar ett plan satt av den högsta punkten, och tenderar att dra upp punkter.

Planar är egentligen samma verktyg som `Flatten`, men med `Lock plane direction` aktiverat, vilket gör att det tenderar att skapa mer stabila, hårdkantade ytor, medan Flatten kan vara mer skulpturalt och användas för att skapa halvplana områden.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Veck {#crease}
Crease-verktyg kan vara användbara för att skulptera små skåror eller bucklor.

Sub-läget är `Invert` och skapar en upphöjd skåra.

#### Inställningar för Veck {#crease-settings}

* `Pinch factor` - Hur mycket verticer dras sidledes mot penseln. Om pinch är 1 och offset 0 får ytan inga djupförändringar, bara topologiförändringar, där kanter dras mot draget.
* `Offset factor` - Hur mycket verticer trycks/dras i djup. Om pinch är 0 och offset 1 skapas djupa skåror eller upphöjda bucklor, men de ser kantiga ut eftersom inte tillräckligt med geometri dras mot skåran för att definiera sidorna eller botten exakt.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Nyp {#pinch}
Detta verktyg kan användas för att skärpa kanter.

Sub-läget är `Invert` och sprider verticer isär.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trimma {#trim}
Trim-verktyget fungerar genom att ta bort en bit av din mesh och ger alternativ för hur hålet som lämnas efter ska bearbetas. Det använder [Markeringskontrollerna](#selection-controls) för att definiera trimmet.

::: tip
Eftersom detta verktyg projicerar från kameran får du en varning om kameran är i perspektivläge.

I ortografiskt läge är snittet genom meshen parallellt med vyn, vilket vanligtvis är vad man förväntar sig. När det görs med en perspektivkamera ser snittet annorlunda ut på objektets bortre sida jämfört med den närmare sidan.
:::

#### Inställningar för Trimma {#trim-settings}

* `Stroke painting` - Om målning är aktiverad i målningsmenyn fylls det lappade området med den aktuellt valda färgen.
* `Boolean` - fyll hålet från trimmet med ett fyrkants-polyområde. Det fyllda området blir platt.
* `Legacy` - fyll hålet från trimmet med ett triangulerat område. Det fyllda området blir platt.
* `Fill` - fyll hålet med ett triangulerat område. Det fyllda området blir en böjd yta, som hinnan på en såpbubbla.
* `None` - fyll inte hålet.
* `Boolean Detail Shape` - Ungefärlig storlek på fyrkanter och trianglar som används på formens sida av trimmet.
* `Boolean Detail Hole` - Ungefärlig storlek på trianglar eller polygoner som används på det fyllda hålet från trimmet. 
* `Legacy Detail` - Ungefärlig storlek på trianglarna som används på trimmet.
* `Legacy Hole smoothing` - Hur mycket trianglarna relaxas på det fyllda området.
* `Legacy Threshold espilon` - Ett värde som kan justeras för att förbättra den äldre hålfyllningsalgoritmen.
* `Fill Detail` - Ungefärlig storlek på trianglarna som används på trimmet.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Dela {#split}
Liknar verktyget [Trim](#trim), förutom att medan Trim kastar bort markeringen behåller Split markeringen som ett nytt objekt.

#### Inställningar för Dela {#split-settings}

* `Stroke painting` - Om målning är aktiverad i målningsmenyn fylls det lappade området med den aktuellt valda färgen.
* `Boolean` - fyll hålet från splitten med ett fyrkants-polyområde. De fyllda områdena blir platta.
* `Legacy` - fyll hålet från splitten med ett triangulerat område. De fyllda områdena blir platta.
* `Fill` - fyll hålen med ett triangulerat område. De fyllda områdena blir böjda ytor, som hinnan på en såpbubbla.
* `None` - fyll inte hålen.
* `Boolean Detail Shape` - Ungefärlig storlek på fyrkanter och trianglar som används på formens sida av splitten.
* `Boolean Detail Hole` - Ungefärlig storlek på trianglar eller polygoner som används på det fyllda hålet från splitten. 
* `Legacy Detail` - Ungefärlig storlek på trianglarna som används på splitten.
* `Legacy Hole smoothing` - Hur mycket trianglarna relaxas på det fyllda området.
* `Legacy Threshold espilon` - Ett värde som kan justeras för att förbättra den äldre hålfyllningsalgoritmen.
* `Fill Detail` - Ungefärlig storlek på trianglarna som används på splitten.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projektera {#project}
Project-verktyget liknar verktyget [Trim](#trim), men det tar inte bort eller skapar någon geometri, det flyttar bara verticer för att anpassa dem till markeringen.

![](/videos/tool_project.mp4)

::: tip
Om du använder Project medan du är i ett lager kan du blanda mellan den ursprungliga och den projicerade formen med lagrets reglage.
:::

### ![](/icons/tool_layer.webp) Lager {#layer}
Höj ytan, men begränsa höjden.

Om du håller pennan nere och fortsätter att måla över ett område höjer Layer till en viss höjd och går inte längre, till skillnad från andra verktyg som fortsätter att bygga höjd.

Observera att begränsningen som standard bara sätts per drag! Om du börjar ett nytt drag byggs det från den nya ythöjden.

För att sätta en konstant maxhöjd över många drag, använd Layer-verktyget tillsammans med Nomads [Layers](layers.md)-system.

Skapa ett lager och använd detta verktyg. Maxhöjden sätts nu från lagret, så du kan applicera många penseldrag och höjden blir alltid densamma.

`Sub` använder ett minsta djup och skapar skåror.

#### Lagerinställningar {#layer-settings}

* `Use layer data` - När aktivt, och när ett lager är valt, använd lagerdatan för att sätta maxhöjden.
* `Inflate`- När aktivt justeras riktningen som Layer arbetar i för att få mjukare resultat.
* `Relax (Normal)` - Mängden utjämning som appliceras på normalerna.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Blås upp {#inflate}
Flytta verticer längs deras egna normaler. `Sub` flyttar verticer längs deras inverterade normal.

#### Inställningar för Blås upp {#inflate-setings}
* `Relax (Normal)` - Mängden utjämning som appliceras på normalerna.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Putta {#nudge}
Flytta eller ”smeta” punkter i dragets riktning.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stämpel {#stamp}

Klicka och dra för att höja ett område av skulpturen i formen av den valda alphan.

Detta är helt enkelt [Brush-verktyget](#brush) med slagtypen satt till `Lock + radius`. 

`Sub` trycker in stämpeln istället för att dra ut den från ytan.

::: tip
Stamp fungerar oftast bäst med högupplöst geometri. Om du söker online efter ”wrinkles alpha”, ”pores alpha”, ”scales alpha” osv kan dessa alpha-texturer och Stamp vara ett utmärkt sätt att lägga till organisk detalj på en karaktärsskulptur.

De två slaglägena är användbara för olika saker. 

* `Lock + radius` har en fast *höjd*, draget justerar bredd och rotation på stämpeln. Bra för hudtexturer där de behöver ha samma djup/höjd, men olika rotationer och skalor för att dölja upprepningsmönster.
* `Lock + intensity` har en fast *bredd*, draget justerar rotation och höjd på stämpeln. Bra för nitar, där alla måste ha samma storlek, men olika rotationer och höjder. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Ta bort lager {#delete-layer}
Detta verktyg kan återställa lager lokalt, du behöver ett aktivt lager annars händer inget.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Rör {#tube}
Skapa ett rör genom att rita en kurva. 
![](/images/tool_tube_new.webp)

När röret har skapats kan banan redigeras i 3D-rymden med liknande kontroller som de vanliga verktygen för [Shape editing](#shape-editing) och kurvredigering. 

![](/videos/tool_tube.mp4)

#### Rör – vänster verktygsrad {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Verktygsfältet till vänster har följande alternativ:

* `Sync` - Om det aktuella röret är instansierat och det finns barnnoder till röret som skiljer sig mellan instanserna, synkar detta dem igen.
* `Snap` - När aktivt kommer kurv- och path-lägena att snäppa mot andra objekt medan du ritar. När inaktivt snäpper första punkten, sedan ritas resten av röret på det djupet. Det har en liten undermeny:
    * `Offset` - Ställ in snäppets djup; 0 % gör att mitten av rörets tvärsnitt snäpper till ytan, positiva värden lyfter det från ytan, negativa värden sänker det.
* `Curve` - Skissa ett rör fritt. Det har en liten undermeny:
    * `Auto-validate` - Skapar röret så snart draget är klart. När inaktiverat visas en grön valideringscirkel bredvid kurvbanan, tryck på den för att validera, eller använd länken `Reset` som visas i denna meny för att ta bort banan.
    * `Closed` - gör röret till en slinga.
    * `Screen` - Endast tillgängligt när Auto-validate är inaktiverat. När aktivt är banan ”fastnålad” på skärmen, vilket gör att du kan flytta vyn och objektet medan banan ligger kvar. När inaktivt är banan en del av 3D-scenen och rör sig med kamera och objekt.
    * `Accuracy` - Hur många kurvpunkter som används för att konvertera den ritade banan till ett rör. 0 % använder minsta antal punkter men missar små krökningsförändringar. 100 % är mycket exakt och använder många punkter.
* `Path` - Skapa ett rör genom att klicka för att definiera kurvpunkter. Tryck på den gröna cirkeln för att validera banan. Det har en liten undermeny:
    * `B-spline` - En alternativ kurvritningsmetod där kurvpunkter vanligtvis inte ligger direkt på kurvan, men kan ge mjukare resultat än standardmetoden.
    * `Closed` - gör röret till en slinga
    * `Screen` - När aktivt är banan ”fastnålad” på skärmen, vilket gör att du kan flytta vyn och objektet medan banan ligger kvar. När inaktivt är banan en del av 3D-scenen och rör sig med kamera och objekt.

##### Rör – övre verktygsrad {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
När ett rör är valt visas en verktygsrad längst upp i vyn med extra kontroller. Klicka på verktygsradens titel för att fälla ihop/fälla ut den, och klicka på pilen uppe till höger för att flytta verktygsraden till över- eller underkanten av vyn.

* `Validate` - baka röret till vanliga polygoner så att det kan skulpteras.
* `Edit` - visa kurvpunkterna så att de kan manipuleras
* `Mirror` - lägg till en spegel-repeater som förälder till denna kurva
* `Snap` - snäpp kurvpunkter till närliggande ytor
* `Closed` - Koppla ihop början och slutet av kurvan till en slinga
* `B-spline` - Växla mellan Catmull-rom och B-spline-interpolering.
* `Cap` - Växla mellan lock i båda ändar av röret, eller bara början eller slutet, eller inga lock.
* `Hole` - Lägg till tjocklek på röret och gör det till ett rör med hål. Växla mellan hål i båda ändar, bara i slutet, eller inga hål. 
* `Radius` - Växla mellan en enhetlig radie, radie i början och slutet, eller radie per kurvpunkt. Dessa redigeras med orange handtag på kurvan.
* `Twist` - Växla mellan ingen twist, en enhetlig twist, twist i början och slutet, eller twist per kurvpunkt. Dessa redigeras med rosa handtag på kurvan.
* `Profile` - Växla mellan ingen profil (alltså cirkelprofil), en enhetlig profil, profil i början och slutet, eller profil per punkt.
* `Profile edit` - Visa en profileditor. Den fungerar liknande verktygen för [Shape editing](#shape-editing), kan spara och ladda profilpresets, och har en växel för att låta dig redigera profilen i 3D-rymden.
* `Spiral` - Växla en meny för att lägga till en spiralvridning på röret. Denna meny har alternativ för `Twist Angle`, `Offset`, `Scale` och `Angle offset`.
* `X Divisions` - antalet indelningar runt röret, 4 indelningar ger t.ex. ett fyrkantigt rör. 
* `Constant density` - när aktivt hålls polygonerna fyrkantiga. När inaktivt kan du ställa in `Y divisions` längs rörets längd.
* `...` - Tube-inställningsmeny.

#### Växel för borttagning av kurvpunkt {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Under verktygsraden finns en växlingsknapp för borttagning av kurvpunkter. När du drar en kurvpunkt nära en annan blir den röd, vilket indikerar att om du släpper tas punkten bort. Om du gör små ändringar och inte vill ta bort punkter inaktiverar denna knapp beteendet för borttagning av punkter.



#### Rörinställningar {#tube-settings}
* `Primitive` - knappar för att aktivera/inaktivera UV:n eller validera röret.
* `Post subdivision` - en genväg för att ställa in multiresolution-nivån innan validering.
* `Linear subdivision` - genväg för att ställa in linjär subdiv-nivå innan validering. 
* `Division X` - samma som X Divisions i verktygsraden.
* `Division Y` - samma som Y Divisions i verktygsraden.
* `Curve (Repeater)` - konvertera röret till en [Curve Repeater](scene.md#curve)

::: tip
Divisioner på 4 och Post subdivision på 3 ger släta, rundade rör, bra för maskar, ormar, kroppsdelar.
:::


### ![](/icons/tool_lathe.webp) Svarv {#lathe}
Skapa en rotationsyta genom att rita en kurva.

Detta verktyg är utmärkt för former som vaser, vinglas.

![](/videos/tool_lathe.mp4)

#### Svarv – vänster verktygsrad {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Verktygsfältet till vänster har följande alternativ:

* `Sync` - Om den aktuella Lathe-formen är instansierad och det finns barnnoder till den som skiljer sig mellan instanserna, synkar detta dem igen.
* `Fixed` - När aktiverat är lathe-centrumet fixerat och visas på skärmen. Denna mittlinje har redigeringspunkter som kan justeras. När inaktiverat uppdateras lathe-centrumet dynamiskt för att matcha början och slutet på den ritade kurvan.
* `Curve` - Rita lathe-profilen i ett drag. Det har en liten undermeny:
    * `Auto-validate` - När aktiverat skapas lathe-formen när pennan lyfts från skärmen. När inaktiverat kan en grön cirkel bredvid kurvan tryckas på för att skapa lathe-formen. Kurvan kan tas bort med knappen `Reset`.
    * `Closed` - Koppla ihop början och slutet av kurvan till en slinga
    * `Screen` - Endast tillgängligt när Auto-validate är inaktiverat. När aktivt är banan ”fastnålad” på skärmen, vilket gör att du kan flytta vyn och objektet medan banan ligger kvar. När inaktivt är banan en del av 3D-scenen och rör sig med kamera och objekt.
    * `Accuracy` - Hur många kurvpunkter som används för att konvertera den ritade banan till ett rör. 0 % använder minsta antal punkter men missar små krökningsförändringar. 100 % är mycket exakt och använder många punkter.
* `Path` - Skapa en lathe-form genom att klicka för att definiera kurvpunkter. Tryck på den gröna cirkeln för att validera banan. Det har en liten undermeny:
    * `B-spline` - En alternativ kurvritningsmetod där kurvpunkter vanligtvis inte ligger direkt på kurvan, men kan ge mjukare resultat än standardmetoden.
    * `Closed` - gör röret till en slinga
    * `Screen` - När aktivt är banan ”fastnålad” på skärmen, vilket gör att du kan flytta vyn och objektet medan banan ligger kvar. När inaktivt är banan en del av 3D-scenen och rör sig med kamera och objekt.

#### Svarv – övre verktygsrad {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

När en lathe-form är vald visas en verktygsrad längst upp i vyn med extra kontroller. Klicka på verktygsradens titel för att fälla ihop/fälla ut den, och klicka på pilen uppe till höger för att flytta verktygsraden till över- eller underkanten av vyn.

* `Validate` - baka lathe-formen till vanliga polygoner så att den kan skulpteras.
* `Edit` - visa kurvpunkterna så att de kan manipuleras
* `Mirror` - lägg till en spegel-repeater som förälder till denna lathe
* `Snap` - snäpp kurvpunkter till närliggande ytor
* `Stable` - När aktiverat föräldras kurvprofilen till lathe-centrumlinjen. När inaktiverat kan centrumlinjen redigeras utan att flytta kurvan, vilket möjliggör mer komplexa former.
* `Focus` - Roterar vyn så att kurvprofilen ses helt platt mot kameran.
* `Closed` - Koppla ihop början och slutet av kurvan till en slinga
* `Cap` - Om Closed är inaktiverat, växla mellan lock i båda ändar av röret, eller bara början eller slutet, eller inga lock.
* `Hole` - Lägg till tjocklek på lathe-formen och gör den till ett rör med hål. Växla mellan hål i båda ändar, bara i slutet, eller inga hål. 
* `B-spline` - Växla mellan Catmull-rom och B-spline-interpolering.
* `X Divisions` - antalet indelningar runt lathe-formen, 4 indelningar ger t.ex. en fyrkantig profil. 
* `Constant density` - när aktivt hålls polygonerna fyrkantiga. När inaktivt kan du ställa in `Y divisions` längs lathe-formens längd.
* `...` - Lathe-inställningsmeny.

#### Svarvsinställningar {#lathe-settings}
* `Primitive` - knappar för att aktivera/inaktivera UV:n eller validera röret.
* `Post subdivision` - en genväg för att ställa in multiresolution-nivån innan validering.
* `Linear subdivision` - genväg för att ställa in linjär subdiv-nivå innan validering. 
* `Division X` - samma som X Divisions i verktygsraden.
* `Division Y` - samma som Y Divisions i verktygsraden.
* `Curve (Repeater)` - konvertera kurvprofilen till en [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Infoga {#insert}
Placera ett objekt på ytan av ett annat. I användning liknar det Stamp-verktyget, men för fulla 3D-former.

Om du väljer en primitiv från verktygsfältet till vänster kommer ett klick-drag på en yta att placera en primitiv där du klickar, draget sätter storleken. När du slutar dra växlar Insert till läget [Transform](#transform).

I Instance-läge skapar och glider dragandet en ny instans över ytan. Storleken dupliceras från den första formen, på så sätt kan du placera många instanser av samma storlek av ett objekt över andra ytor.

Du behöver inte bara infoga primitiver! Välj *vilken som helst* form i outlinern, om Insert är i Instance- eller Clone-läge kan du dra kopior av det valda objektet över andra ytor.

Om ett objekt har en anpassad pivot används den som ankarpunkt. Se videon nedan.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformera {#transform}
Flytta/rotera/skala en modell direkt med 1 och 2 fingrar, vanligtvis över ytan av ett annat objekt.

Verktyget styrs med verktygsfältet till vänster och har 5 knappar:

* `Snap` - snäpp modellen mot andra ytor
* `Group` - Om det valda objektet har en kombination av objekt och instanser låter detta dig bestämma verktygets beteende.
* `Move` - Drag med ett finger flyttar objektet. När Snap är aktivt glider objektet längs ytan under ditt finger.
* `Rotate` - Drag med ett finger roterar objektet. När Snap är aktivt roterar det runt normalen på ytan under ditt finger.
* `Scale` - Drag med ett finger skalar objektet.

Transform kan användas för att snabbt använda 2 av dessa lägen med två fingrar:

* Dra ett objekt för att placera det. Sluta röra ditt första finger, men lyft det inte från skärmen.
* Rör vid skärmen med ditt andra finger medan du håller det första fingret nere. När det andra fingret dras skalar objektet.
* Lyft det andra fingret och fortsätt dra det första fingret, objektet är i Move-läge igen.

Du kan också byta det andra läget med en andra-finger-tryckgest:

* Dra objektet för att placera det, sluta röra men lyft inte fingret från skärmen.
* Tryck med ditt andra finger medan du håller det första fingret nere
* Verktyget växlar till rotationsläge. Dra ditt första finger för att ställa in rotationen.
* Tryck med det andra fingret som tidigare, verktyget växlar tillbaka till Move-läge.

Detta ger ett snabbt arbetsflöde för att klona objekt över ett annat, t.ex. stenar över ett landskap. Observera att Clone-knappen också finns i verktygsfältet till vänster för enkel åtkomst:

* Använd Transform-verktyget för att flytta en sten på plats.
* Släpp, tryck på Clone-knappen
* Flytta denna sten, rotera/skala efter behov
* Släpp, tryck på Clone-knappen
* Flytta denna sten, upprepa.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Detta verktyg låter dig flytta, rotera och skala objekt, samt ändra objektens pivoter.

Handtaget i vyn har följande funktioner:

* `Move` - Dra på linjen+pil för att flytta i X/Y/Z. Dra på den persikofärgade pricken i mitten av gizmon för att översätta fritt i skärmrymden. Klicka på de röda, gröna, blå fyrkanterna för att översätta i X/Y/Z-planen.
* `Rotate` - Dra på de röda/gröna/blå cirklarna för att rotera i X/Y/Z. Dra på sfären inom cirklarna för att rotera fritt.
* `Scale`- Dra på de yttre röda/gröna/blå prickarna för att skala i X/Y/Z. Dra på de yttre röda/gröna/blå konerna för att skala i X/Y/Z-planen. Dra på den yttre persikofärgade cirkeln för att skala enhetligt.

![](/images/tool_gizmo.webp)

#### Noder och hörnpunkter {#nodes-and-vertices}

Varje objekt i Nomad består av en nod och verticer:

* `Node` - Objektets ”handtag”, som lagrar dess förflyttning, rotation, skalning, kallat dess transformationsmatris.
* `Vertices` - Punkterna som definierar objektets yta, de lagrar position och målningsinformation.

Om du har en enkel låda gjord av 8 verticer kan du översätta den genom att ändra dess transformationsmatris eller genom att ändra vertexpositionerna. När du skulpterar vill du vanligtvis ändra verticerna, när du flyttar objekt med gizmon vill du vanligtvis ändra noden. Nomad låter dig göra båda. 

#### Vänster menyverktygsrad {#left-menu-toolbar}

Verktygsfältet till vänster styr om gizmon ska arbeta på noden eller verticerna, samt andra funktioner:

* `Clone` - Gör en fristående kopia av det aktuella objektet, som kan dras bort med gizmon.
* `Instance` - Gör en instanskopia av det aktuella objektet. Objekten är länkade, så skulpteringsändringar på ett objekt visas på alla instanser.
* `Group/Object/Vertex/Auto` - Ställer in om gizmon ska påverka noden eller verticerna på ett objekt. Standardläget ”Auto” försöker göra en kvalificerad gissning. Om flera objekt är föräldrade tillsammans i en hierarki flyttar ”Object” bara det aktuella objektet, barnobjekt förblir stilla. Gizmon kan också ta hänsyn till maskning och symmetri.
* `Pin` - Som standard flyttas gizmon till pivoten på det valda objektet. När Pin är aktiverat stannar gizmon där den är.
* `Align` - Växla mellan att pivoten är anpassad till det aktuella objektet eller till världen.
* `Snap rotation` - Aktivera att rotationsvärden snäpps till steg, snäppvärdet visas och kan redigeras när snäpp är aktivt.
* `Snap translation` - Aktivera att förflyttningsvärden snäpps till steg, snäppvärdet visas och kan redigeras när snäpp är aktivt.
* `Pivot` - När aktiverat kan gizmon flyttas och roteras utan att flytta objektet. Den har en extra meny som förklaras nedan.

#### Pivot {#pivot}
När pivot-läget är aktivt visas en meny för snabba pivotändringar:

**Reset** 
* `Center` - Flytta pivoten till objektets centrum
* `Bottom` - Flytta pivoten till objektets botten
* `Align` - Återställ rotationerna så att de är anpassade till världen.
* `Mask` - Flytta pivoten till centrum av den omaskerade regionen.

**On Tap**
* `None` - gör ingenting när objektet trycks på
* `Normal` - Flytta och rotera pivoten för att anpassa den till där ytan trycks på
* `First` - Flytta (men rotera inte) pivoten till där ytan trycks på
* `Medial` - Flytta pivoten till mitten av objektet, under där ytan trycks på.

#### Gizmo-inställningar {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Matris {#matrix}
* ![](/icons/target.webp) `Move origin` - Flytta objektet så att dess pivot är i scenens centrum, kallat origo.
* ![](/icons/bake.webp)  `Bake` - Frys objektet där det är och sätt translate/rotate-värden till 0, scale till 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Gör så att matrisvärdena motsvarar var gizmo-handtaget är i världen.
* ![](/icons/reset.webp) `Reset` - En genväg som sätter translate-värden till 0, rotate-värden till 0, scale till 1, vilket flyttar och roterar objektet.

::: tip Bake vs bake to pivot
Skapa en låda, välj Gizmo-verktyget, öppna och fäst inställningsmenyn. Som standard är translate och rotate 0, scale är 1.

Aktivera pivot-läge, flytta handtaget till ena sidan, inaktivera pivot-läge. Pivoten har ändrats, men observera att translate-värdena fortfarande är 0. 

Om du vill se var pivoten *egentligen* är, klicka på `Bake Pivot`. Nu uppdateras translate-värdena. Observera att lådan inte flyttas under denna operation, inte heller i pivot-läge.

Flytta och rotera lådan någonstans, tryck sedan på `Move Origin`. Den flyttar objektet så att dess pivot är i världens centrum, men lämnar rotationen oförändrad.

Klicka på `Reset`, så sätts rotationen också till 0.

Flytta och rotera lådan igen, klicka denna gång på `Bake`. Pivoten stannar där den är, lådan stannar där den är, men translate- och rotate-värdena sätts till 0.

Öva detta några gånger! Få en förståelse för att pivotvärdena är dolda, Nomad tar hand om det åt dig, men om du behöver sätta pivoten till verkliga positioner i rymden gör Bake Pivot det åt dig.

:::

* `Translation` - translate X-, Y-, Z-värden
* `Rotation` - rotate X-, Y-, Z-värden
* `Scale` - Den enhetliga skalningen om den är aktiverad, eller scale X, Y, Z om den är inaktiverad.
* `Uniform scale` - Växla möjligheten att skala enhetligt eller oberoende på varje axel

-----

* `Compact` - växla gizmo-layouten för att placera extra handtag utanför eller innanför rotationssfären
* `Widget size` - storleken på gizmon
* `Thickness` - storleken på linjerna på gizmon
* `Opacity` - opaciteten på gizmon
* `Hide on interaction` - växla om gizmon tillfälligt ska döljas när den dras

-----

* `Tangent roll threshold` - Styr hur rotationsgränssnittet beter sig när du drar på cirkelhandtagen för att rotera i X/Y/Z. Om detta värde är 0 fungerar rotation som en ratt, dra gizmon i cirklar. Om detta värde är 90 fungerar rotation som att dra i ett jojo-snöre; dra i en rak linje mot eller bort från där du först klickade. Värden mellan 0 och 90 gör en kombination av båda; under värdet blir det linjär rörelse, över värdet blir det cirkulär rörelse.
* `Numerical input` - när aktiverat öppnas ett fönster för att ange ett exakt värde för den axel du trycker på med ett enkelt tryck på gizmon.

::: warning
[Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) och [Scale](#scale) använder sina egna symmetrikryssrutor!

Som standard är denna symmetri avstängd.
:::

Till vänster kan du flytta gizmo-pivoten, du kan se videon nedan i aktion.
Detta är särskilt användbart för rotation, eftersom det inte ändrar något för förflyttning.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Ytgrupp {#facegroup}

Facegrupper låter dig organisera ditt objekt i olika färgade ytor. Du kan använda dessa grupper på många sätt i Nomad:

* En snabb markeringsmetod för masker
* Dölj/visa delar av ditt objekt
* Organisera ditt objekt utan att behöva dela upp det i separata delar
* Definiera UV-regioner
* Styra quad remesher
* Extra kontroll för verktyg som Smooth.

#### Ytgrupp – vänster verktygsrad {#facegroup-left-toolbar}

* `Patch ` - Visa tillgängliga facegrupper som patchar. Oanvända patchar kan tas bort. Tryck på en patch för att byta namn eller ändra dess färg. Plusikonen låter dig skapa nya patchar.
* `Dot` - Måla på objektet för att definiera facegrupper. När ”+ Face Group” är aktiverat skapar varje nytt drag automatiskt en ny facegroup, användbart för att snabbt definiera regioner. Ett tryck fyller den valda regionen. Reglaget ställer in prickens radie.
* `Relax` - Jämnar ut kanterna på facegrupper. Mycket användbart för att definiera rena kanter för quad remeshing eller för att definiera paneler för hård yta-modellering. Reglarna styr radie och intensitet för relax-operationen.
* `Shape selector` - Skapa facegrupper med former istället för en pensel, via `Lock+Radius`, `Lasso`, `Polygon`, `Rect` och `Ellipse`. Se [Shape Selector](#shape-selector) för mer info.
* `Auto-pick` - När aktiverat väljs patchen där draget börjar och applicerar den patchen för resten av draget. Mycket användbart för att städa upp facegroup-regioner; om en facegroup har sträckt sig för långt, aktivera Auto-pick, börja ett drag där facegroup-patchen är korrekt och dra upp till kanten för att tilldela rätt patch igen.

### ![](/icons/tool_hide.webp) Dölj {#hide}
Dölj eller isolera delar av objektet. 

De primära lägena styrs från menyn till vänster:

* `Dot` - Måla på objektet för att dölja delar av objektet.
* `Shape selector` - Dölj med former istället för en pensel, via `Lasso`, `Polygon`, `Line`, `Rect` och `Ellipse`. Se [Shape Selector](#shape-selector) för mer info.
* `Show` - invertera operationen, så att det valda läget visar istället för döljer delar av objektet.

En verktygsrad visas längst upp i vyn med extra kontroller:

* `Clear` - Återställ objektet, alla dolda delar visas igen.
* `Invert` - Växla de dolda och synliga delarna.
* `Facegroup` - Använd facegrupper för att snabbt dölja sektioner, att trycka på en facegroup döljer hela facegruppen.
* `Mask` - Om en mask är aktiv döljer ett tryck på denna knapp den maskerade sektionen.
* `Delete` - Ta bort den dolda delen av objektet
* `Split` - Dela den dolda delen av objektet till en ny form.

### ![](/icons/tool_measure.webp) Mät {#measure}
Dra för att mäta avståndet mellan 2 punkter.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Detta verktyg konverterar det valda objektet till en ren quad-topologilayout, med kontroller för täthet, kantflöde, symmetri. 

::: tip
Quad Remesher utvecklas av [Exoside](https://exoside.com/) för iOS och desktop. 

För iOS är det ett köp i appen i Nomad, en engångsbetalning på 16 USD.

För desktop, köp en licens från [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Du kan köpa det bara för Nomad desktop eller en korslicens för alla stödda desktopappar.

Om du redan äger Quad Remesher för en annan desktopapp kan du [köpa en uppgradering till alla plattformar till lägre kostnad.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher är inte tillgängligt för Android. Android kan använda den fria open source-lösningen ”Quad Remesh - Instant” som finns under Topology -> Misc-menyn, men förstå att dess funktionsuppsättning är mycket begränsad.
:::

When detta verktyg aktiveras för första gången kommer det att fråga om du vill aktivera det som ett köp i appen. När det är aktivt kommer de vänstra och övre verktygsraderna att aktiveras.

* `Dot` - Denna pensel ställer in måltätheten. Intensitet på 100 % målar rött, vilket använder dubbla målkvadtätheten i dessa områden. Intensitet på 0 % målar cyan, vilket använder halva målkvadtätheten i dessa områden. Intensitet på 50 % målar grått, vilket använder den förvalda målkvadtätheten.
* `Smooth` - Jämna ut övergångarna mellan röd/grå/cyan-täthet.
* `Curve` - Skissa kurvor på skulptens yta, quad remesher kommer att använda dessa som guider för kantflödet. Tryck på en kurva för att ta bort den.
* `Path` - Rita banor på skulptens yta, quad remesher kommer att använda dessa som guider för kantflödet. Tryck på en bana för att ta bort den. 
* `Rect` - Rita rektanglar på skulptens yta, quad remesher kommer att använda dessa som guider för kantflödet. Tryck på en bana för att ta bort den.
* `Ellipse` - Rita ellipser på skulptens yta, quad remesher kommer att använda dessa som guider för kantflödet. Tryck på en bana för att ta bort den.

#### Quad Remesher – övre verktygsrad {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

En verktygsrad visas högst upp i vyn med extra kontroller:


* `<Count>` - Klicka här för att starta quad remesher-processen, detta tal anger vad den målade quad-remesh-räkningen kommer att vara.
* `Quads` - Ställ in målantalet quads genom att dra åt vänster och höger, eller tryck för att ange ett exakt tal. Observera att detta är mer en riktlinje än ett fast tal, de olika kontrollerna i quad remesher innebär ofta att resultatet inte exakt matchar detta mål.
* `Half` - En genväg för att ställa in målantalet till hälften av nuvarande polygonantal.
* `Same` - En genväg för att ställa in målantalet till nuvarande polygonantal.
* `Guides` - anger det totala antalet guider, eller tryck för att ta bort alla guider.
* `Density X` - tryck för att ta bort all täthetsmålning.
* `Density (painting)` - växla för att använda eller ignorera täthetsmålning.
* `Face Group` - växla för att använda eller ignorera facegroups för att styra quad remesher.
* `Relax` - växla för att automatiskt relaxa facegroup-gränser under quad-remeshing. Om du redan har relaxat/jämnat ut dina facegroup-gränser, inaktivera detta alternativ.
* `Relax Slider` - En genvägsreglage för att relaxa facegroup-gränserna.
* `Hard Edges` - växla för att försöka bibehålla hårda kanter.
* `Reproject Vertex` - växla för att reprojicera den nya layouten till indata-meshen.
* `Symmetry` - Växla för att aktivera ett symmetriskt resultat. Observera att symmetri alltid beräknas runt världens x-axel, så se till att din modell är vid origo om du förväntar dig ett symmetriskt resultat.
* `...` - Quadremesher-inställningsmeny. 

#### Quad Remesher – inställningsmeny {#quad-remesher-settings-menu}

De flesta av dessa inställningar finns i den övre verktygsraden.

* `<Count>, Half, Same` - Samma som knapparna Remesh, Half, Same i den övre verktygsraden.
* `Target Quads` - Samma som knappen `Quads` i den övre verktygsraden
* `Adaptive quad count` - växla för att använda mindre quads i områden med hög krökning och större quads i områden med lägre krökning.
* `Adaptive size` - Ställ in mängden adaptivitet. 100 % tillåter maximal adaptiv storlek, vid 0 % blir quads enhetliga.
* `Auto-Detect Hard Edges` - växla för att anpassa quad-remesh-layouten för att bättre följa skarpa ytor.
* `Density (painting)` - Samma som knappen `Density (painting)` i den övre verktygsraden
* `Reproject Vertex` - växla för att reprojicera den nya layouten till indata-meshen.
* `Face Group` - Samma som knappen `Face Group` i den övre verktygsraden
* `Relax Slider` - En genvägsreglage för att relaxa facegroup-gränserna.

::: tip

Ett recept för att få en bra quad-remesh med minimala artefakter:

* Facegruppa meshen för att definiera ditt ideala quad-flöde.
* Facegroup relax för att få släta facegroup-gränser.
* Decimate. Detta säkerställer att du inte har tunna eller förvrängda ytor på facegroup-kanten. I decimate-inställningarna, se till att facegroup är aktiverat. Detta gör att triangelkanter följer dina facegroup-kanter exakt. 

I quad-remesh-alternativen, se till att relax är inaktiverat (eftersom du redan har relaxat meshen) och du bör få bra resultat.

:::

### ![](/icons/tool_select.webp) Markera {#select}
Använd form-lägena för att välja objekt i scenen. `Unselect` tar bort objekt från markeringen.

### ![](/icons/tool_view.webp) Visa {#view}
Detta "verktyg" gör inget särskilt, det är helt enkelt ett sätt att visa modellen utan att ändra din scen.


## Snabbmeny för verktygslåda {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Ett högerklick eller ett långt tryck på ett verktyg i verktygslådan visar en snabbmeny. Denna meny har följande alternativ:

* `Save` - spara alla ändringar du gjort i verktyget
* `Clone` - duplicera verktyget till en ny verktygsgenväg
* `Last save` - återgå till den senast sparade versionen av verktyget
* `Icon` - ändra ikonen för verktyget
* `Reset` - återställ verktyget till dess standardinställningar