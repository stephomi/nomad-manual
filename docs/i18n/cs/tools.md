# ![](/icons/toolbox.webp) Nástroje {#tools}

![](/images/tools_menu.webp)

::: tip
Přeskočte dolů na [Nástroje](#tools-1) pro popisy jednotlivých nástrojů.
:::

## Přehled {#overview}

Nástroje se vybírají z `Toolbox` vpravo a ovládají se přes `Tool Controls` vlevo. Další nastavení najdete v nabídce `Settings`, první ikona v pravém horním rohu.

Štětcové nástroje mají ovládání velikosti a intenzity. Výběrové nástroje mají ovládání pro různé styly výběru. Spodní část ovládání nástroje obsahuje zkratky pro často používané operace (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Nástroje Nomadu jsou v panelu nástrojů barevně kódované:

* <span class=brush>**Štětcové nástroje**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Pohybové nástroje**</span> (Move, Drag)
* <span class=mask>**Maskovací nástroje**</span> (Mask, SelMask)
* <span class=paint>**Malovací nástroje**</span> (Paint, Smudge)
* <span class=flatten>**Zplošťovací nástroje**</span> (Flatten, Planar)
* <span class=pinch>**Pinch nástroje**</span> (Crease, Pinch)
* <span class=selection>**Nástroje založené na výběru**</span>, kde se nejprve nakreslí 2D maska a pak se provede operace (Trim, Split, Project)
* <span class=creation>**Tvořicí nástroje**</span> (Tube, Lathe, Insert)
* <span class=transform>**Transformační nástroje**</span> (Transform, Gizmo)
* <span class=misc>**Různé nástroje**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Nástroj View**</span>



Mnoho těchto nástrojů lze přizpůsobit různým chováním štětce, tlakem, texturami atd. přes nabídku [Stroke](stroke.md). 


### Ovládání štětce {#brush-controls}

Levý panel nástrojů má posuvníky pro poloměr a intenzitu a pak ovládání specifická pro kategorii nástroje, vysvětlená níže.

![](/images/tool_left_panel.webp)

::: tip
Posuvník intenzity u mnoha nástrojů může jít nad 100 %, stojí za to experimentovat!
:::

### Režim Sub {#sub-mode}
Tlačítko přímo pod posuvníkem intenzity je tlačítko `Sub`. Jeho popisek a funkce se mění s každým nástrojem a po stisknutí vyvolá alternativní, obvykle opačné chování. Např. u [Paint](#paint) vyvolá režim mazání (Erase), u [Crease](#crease) vytváří vystouplé hrany místo rýh atd.

Ve výchozím nastavení funguje jako „lepivé“ tlačítko; tj. můžete ho držet pro dočasné vyvolání, po uvolnění se vypne. Pokud na něj klepnete, sub režim zůstane trvale aktivní.

### Zkratky {#shortcuts}
Ve spodní části levého panelu nástrojů jsou zkratky pro [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Ve výchozím nastavení všechny fungují jako „lepivá“ tlačítka; tj. můžete je držet pro dočasné vyvolání, po uvolnění se vypnou. Pokud na ně klepnete, daný režim zkratky zůstane trvale aktivní.

### Ovládání výběru {#selection-controls}

Nástroje [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) a [Hide](#hide) používají podobné ovládání pro výběr oblastí sítě.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Volně kreslený tvar
* `Polygon` - Uzavřený tvar definovaný kombinací křivek a/nebo přímek. Více informací viz [Shape editing](#shape-editing) níže.
* `Curve` - (pouze Project) - Volně kreslená křivka pro projekci
* `Path` - (pouze Project) - Křivka definovaná body. Více informací viz [Shape editing](#shape-editing) níže.
* `Line` - Tažením čáry definujete rovinný segment. Ve výchozím nastavení se operace na síti provede okamžitě, vypněte auto validate, pokud to nechcete (dlouhé podržení nebo přejetí na ikoně čáry).
* `Rect` -  Tažením úhlopříčky definujete rohy obdélníkového tvaru. Dlouhým podržením nebo přejetím zobrazíte volby pro auto validate, vynucení čtvercového tvaru a pro to, aby první klik byl středem obdélníku.
* `Ellipse` - Tažením úhlopříčky definujete velikost elipsy. Dlouhým podržením nebo přejetím zobrazíte volby pro auto validate, vynucení kruhového tvaru a pro to, aby první klik byl středem elipsy.
* `Flip` - Inverze masky tvaru nebo směru nástroje Project.

Většina nástrojů má volbu auto validate, což znamená, že operace proběhne hned po dokončení kreslení tvaru. Když je auto validate vypnuté, vedle tvaru se zobrazí zelené tlačítko, které operaci provede. To vám umožní tvar upravovat, měnit pohled a až budete připraveni tvar použít, stiskněte zelené tlačítko.

### Úprava tvaru {#shape-editing}
Úprava polygonu a křivky se chová podobně:

* Na začátku táhněte čáru pro definování 2 bodů, pak táhněte ze středu čáry pro definování polygonu nebo křivky.
* Kliknutím na body přepínáte mezi hladkým a ostrým.
* Kliknutím a tažením na úsecích křivky nebo čáry vytváříte nové body.
* Pro smazání bodu ho přetáhněte do jeho souseda, dokud nezčervená.
* Ikona koše v rohu ikony polygonu nebo cesty smaže tvar.

### Nabídka Nastavení {#settings-menu}

Mnoho nástrojů má další nastavení v nabídce settings, první ikona v pravém horním menu:

![](/images/tools_settings_menu.webp)

## Nástroje {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Hlína {#clay}
Nástroj Clay je užitečný pro budování objemu sochy. `Sub` bude materiál z vaší sochy odebírat.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Štětec {#brush}
Standardní štětec. `Sub` bude materiál odebírat.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Posun {#move}
Oblast pod štětcem se „přilepí“ na štětec, což umožňuje elastickou deformaci. Výběr je během přesunu zachován, takže pokud štětec odsunete a pak ho vrátíte zpět na původní místo, neuvidíte žádnou deformaci.

Sub režim je `Normal` a bude oblast pod štětcem posouvat podél normály povrchu.

Tento štětec je vhodný jak pro velkorozměrové deformace, tak pro jemné malé úpravy.

#### Nastavení nástroje Posun {#move-settings}

* `Radius (Background)` - Jak daleko od okraje modelu můžete být a stále modelovat, užitečné při práci na siluetě objektu. 
* `Same-side vertex only` - Ignoruje vrcholy, které směřují opačným směrem než deformace.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Tažení {#drag}
Oblast pod štětcem se „přilepí“ na štětec, což umožňuje elastickou deformaci. Na rozdíl od štětce Move se výběr během tahu průběžně aktualizuje, takže je možné vytvářet delší, hadovité objekty, zvláště když je aktivní Dynamic Topology.

Sub režim je `Normal` a bude oblast pod štětcem posouvat podél normály povrchu.

Tento štětec je vhodný pro volnější, gestické změny tvaru.

#### Nastavení nástroje Tažení {#drag-settings}

* `Radius (Background)` - Jak daleko od okraje modelu můžete být a stále modelovat, užitečné při práci na siluetě objektu. 
* `Same-side vertex only` - Ignoruje vrcholy, které směřují opačným směrem než deformace.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Vyhladit {#smooth}
Vyhlazuje oblast zprůměrováním pozic bodů. Tento nástroj je silně závislý na hustotě polygonů.
Pokud máte mnoho polygonů, vyhlazování bude méně účinné.

Sub režim je `Relax`, který vyhlazuje pouze drátěný model, ale snaží se zachovat geometrické detaily.

#### Nastavení nástroje Vyhladit {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Skupina ploch {#smooth-facegroup}

* `Relax` - Vyhlazuje hranice facegroup. Použijte intenzitu vyšší než 100 % pro rychlé vyhlazení hran. `Auto` bude vyhlazovat pouze pokud je zapnutý náhled facegroup, `Off` vypne, `On` zapne. 

##### Vrchol {#vertex}
* `Sticky vertex on border` - U sítí s otevřenými hranami, např. rovina, je možné vyhladit rohy. Zapnutí této volby uzamkne otevřené hrany.
* `Relax` - stejné jako relax alternativní režim v levém panelu nástrojů.
* `Stable smoothing` - Snaží se udělat vyhlazování nezávislé na topologii. Nejlépe funguje s proměnlivou hustotou topologie a s vysokou hodnotou intenzity vyhlazování.

##### Malování {#painting}
* `Screen Smoothing` - Použijte tuto volbu pro topologicky nezávislé vyhlazování, i při vysokých počtech polygonů.
* `Screen samples` - Kvalita vyhlazování, vyšší hodnoty budou hladší, ale pomalejší.

::: tip
Vyšší hustoty polygonů mohou vyžadovat zvýšení intenzity nad 100 %. Velmi vysoké hodnoty (300 %, 500 %) mohou také dobře fungovat jako sochařský nástroj, který nutí oblasti rychle přecházet do plochých a hladkých pod štětcem, jako když udeříte do hlíny palicí!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maska {#mask}
Tento nástroj umožňuje maskovat vrcholy. Maskované vrcholy jsou chráněny před modelováním nebo malováním. 

Sub režim je `Unmask` a bude masku v místě tahu mazat.

Podobně jako výběry v 2D malovacích programech lze masky malovat štětcem nebo vytvářet pomocí tvarových výběrů, rozmazávat nebo zostřovat. 

Na rozdíl od 2D programů je lze také vytvářet pomocí facegroup a masky lze použít k vytváření nové geometrie pomocí operací typu extruze/extrakce. 

![](/videos/tool_mask1.mp4)

 V horní části viewportu se objeví panel nástrojů s dalšími ovládacími prvky. 

![](/images/tool_mask_toolbar.webp)

Název panelu lze klepnutím rozbalit/sbalit, nebo klepnutím na šipku vpravo nahoře přesunout panel nahoru nebo dolů v UI.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Clear              | Vymazat masku                                                                              |
| ![](/icons/invert.webp)        Invert             | Inverze masky                                                                              |
| ![](/icons/sharpen.webp)       Sharpen            | Zostřit okraj masky                                                                        |
| ![](/icons/blur.webp)          Blur               | Rozmazat okraj masky                                                                       |
|                                 Blur ->            | Tažením vlevo/vpravo interaktivně rozmazáváte masku                                        |
| ![](/icons/culling.webp)       Front              | Přepíná maskování pouze předních vrcholů                                                   |
|                                 Convert            | Převést masku na facegroup                                                                 |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Pokud je zapnuto, zobrazí facegroup, klepnutím na facegroup ji zamaskujete                |
|                                 On tap (mask)      | Pokud je zapnuto, klepnutí na „ostrov“ masky nebo nemaskovaných polygonů jej zaplní        |
| ![](/icons/vertex.webp)        Connected          | Pokud je zapnuto, dovolí tahy masky ovlivnit pouze souvislou topologii                     |

##### Rychlé gesto Masky {#mask-quick-gesture}
Můžete provádět gesta ve stylu ZBrushe při držení tlačítka rychlé masky v levém panelu:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Klepnutí na pozadí                 |
| Clear   | Tažení na pozadí                   |
| Blur    | Klepnutí na maskovanou oblast      |
| Sharpen | Klepnutí na nemaskovanou oblast    |


#### Nastavení Masky {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Nabídka Mask settings se používá hlavně k vytváření geometrie z masky. Proto je výchozí chování náhled toho, jak bude nová geometrie vypadat. Můžete zvolit žádný náhled, náhled extrakce, náhled split a zda bude tato geometrie zobrazena v režimu x-ray.

##### Tloušťka {#thickness}
* `Height` - Výška extrahovaného tvaru. Ikona Plus/Minus umožňuje cyklovat mezi extruzí směrem ven, dovnitř nebo centrovanou. 
* `Height/Height+Mask` - Přepíná mezi konstantní výškou nebo tím, zda rozmazané části masky ovlivní výšku, což umožňuje měkké a proměnlivé výšky tvarů. 

##### Hladkost {#smoothness}
Pokud je aktivní, vyhlazuje okraj extrahovaného tvaru, funguje lépe při vyšším počtu polygonů. 
* `Iterations` - Množství aplikovaného vyhlazení. Vysoké hodnoty vytvoří velmi hladké zakřivené hrany, ale začnou se odchylovat od tvaru masky.
* `All/Sharp border/Borders only` - Vyhlazování může fungovat ve všech směrech, vyhlazovat boky i horní část extrahovaného tvaru, nebo vyhlazovat horní část a boky, ale zachovat ostrý okraj, nebo vyhlazovat pouze okraj a horní plochu ponechat nedotčenou.

##### Okrajová smyčka (bok) {#edge-loop-side}
* `Auto Edge-loop (side)` - Vypočítá počet dělení na bocích extrahovaného tvaru tak, aby vznikly čtvercové polygony odpovídající polygonům maskované oblasti. Po vypnutí můžete počet edge loop nastavit sami posuvníkem edge loop.

----

##### Extrakce {#extract}
* `Extract` - Vytvoří extrahovanou geometrii.
* `Closing action` - Jak se má Extract chovat. „None“ duplikuje maskované polygony do nového tvaru. „Fill“ udělá totéž a pokusí se zaplnit zadní plochu. „Shell“ extruduje do výšky nastavené v „thickness“ a je výchozí.

::: tip

Pokud je náhled v režimu „Extract“ s povoleným „X-ray“, může být kliknutí na tlačítko Extract zpočátku matoucí. Protože je nabídka aktivní, pokusí se náhledově extrahovat na vašem novém tvaru a původní povrch zobrazit v x-ray. Protože ale na novém povrchu nemáte masku, nemůže extrakci náhledově provést a Nomad vás upozorní „Nothing to Extract!“. 

To je v pořádku, zavřete nabídku mask settings, abyste viděli nový tvar a původní, a znovu vyberte původní povrch, pokud potřebujete masku vymazat nebo kreslit nové masky.
:::

##### Rozdělení {#split-mask}
* `Split` - Extrahuje maskované I nemaskované oblasti do nových tvarů. 
* `Closing action (masked)` - Jak se má chovat extrakce masky. „None“ duplikuje maskované polygony do nového tvaru. „Fill“ udělá totéž a pokusí se zaplnit zadní plochu. „Shell“ extruduje do výšky nastavené v „thickness“ a je výchozí.
* `Closing action (unmasked)` - Jak se má chovat extrakce nemaskované části. „None“ duplikuje maskované polygony do nového tvaru. „Fill“ udělá totéž a pokusí se zaplnit zadní plochu. „Shell“ extruduje do výšky nastavené v „thickness“ a je výchozí.
* `Sync border` - Zajistí, aby okraj mezi maskovanými a nemaskovanými extrahovanými tvary zůstal blízko sebe. Po vypnutí se může mezi tvary vytvořit mezera, protože operace shell extruduje každou plochu podél její normály.

##### Vyřezat {#carve}
* `Carve` - V základním režimu se chová, jako byste do povrchu vyřízli nástrojem Trim do hloubky „thickness“, jako když vyříznete kus pomerančové kůry. 



### ![](/icons/tool_maskSelector.webp) Výběrová maska {#selection-mask}
Tento nástroj je většinou podobný nástroji [Mask](#mask), hlavní rozdíl je v tom, že masku nemalujete tahem, ale používáte [Selection Controls](#selection-controls).

Sub režim je `Unmask` a bude masku mazat pomocí výběrových ovládacích prvků.

Selection mask sdílí stejná nastavení nástroje jako nástroj `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Malba {#paint}
Aplikuje barvu a materiálové vlastnosti. Více o materiálech najdete v sekci [Painting](painting.md).

Sub režim je `Erase` a bude malbu odstraňovat.

#### Nastavení Malby {#paint-settings}
* `Layer fitering` - Funguje jako uzamčení alfa vrstvy ve Photoshopu nebo Procreate. Pokud malujete na vrstvu a je to zapnuté, můžete upravovat pouze tam, kde už barva existuje; nenamalované oblasti budou chráněny.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Rozmazání {#smudge}
Rozmazává barvu a materiálové vlastnosti. Nabídka nastavení Smudge obsahuje posuvník `Quality`, nižší hodnoty znamenají rychlejší tahy.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Zploštit {#flatten}
Zplošťuje oblast projekcí bodů na průměrnou rovinu.

Sub režim je `Fill` a definuje rovinu podle nejvyššího bodu a má tendenci body vytahovat nahoru.

#### Nastavení nástroje Zploštit {#flatten-settings}

* `Lock plane direction` - Použije směr roviny vypočítaný při prvním kliknutí. Ve výchozím nastavení vypnuto.
* `Lock plane origin`- Použije první klik jako střed roviny. Ve výchozím nastavení vypnuto.

Pokud je jedna nebo obě tyto volby vypnuté, lze Flatten postupně prohlubovat nebo měnit úhel roviny pomocí dlouhých tahů, které se pohybují přes různé hloubky a zakřivení. V kombinaci s volbami vzorkování oblasti v nabídce štětce to může nabídnout velmi přesnou kontrolu.

::: tip
Při práci v oblastech s vysokým zakřivením, např. při snaze zploštit tváře, ale nástroj stále ovlivňuje boky nosu, zkuste vytvořit masku pro ochranu oblastí, které by Flatten neměl ovlivnit.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Rovinný {#planar}
Zplošťuje body projekcí na průměrnou rovinu, ale s menším „nabíháním“ než štětec Flatten. Vytváří čistší tvrdé plochy. Rychlé tahy více tlačí a tahají povrch, pomalejší tahy, které začínají z již rovinných oblastí a rozšiřují se ven, rovinu více zachovávají.

Sub režim je `Fill` a definuje rovinu podle nejvyššího bodu a má tendenci body vytahovat nahoru.

Planar je ve skutečnosti stejný nástroj jako `Flatten`, ale s povoleným `Lock plane direction`, což znamená, že má tendenci vytvářet stabilnější, tvrdé plochy, zatímco Flatten může být více sochařský a používaný k vytváření poloplochých oblastí.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Rýha {#crease}
Nástroj Crease je užitečný pro modelování malých řezů nebo důlků.

Sub režim je `Invert` a vytváří vystouplou rýhu.

#### Nastavení nástroje Rýha {#crease-settings}

* `Pinch factor` - Jak moc tahat vrcholy do stran směrem ke štětci. Pokud je pinch 1 a offset 0, povrch nebude mít žádné změny hloubky, jen změny topologie, tahající hrany směrem k tahu.
* `Offset factor` - Jak moc tlačit/tahat vrcholy do hloubky. Pokud je pinch 0 a offset 1, vzniknou hluboké rýhy nebo vystouplé důlky, ale budou vypadat zubatě, protože se k rýze nestáhne dost geometrie, aby přesně definovala boky nebo dno rýhy.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Štípnutí {#pinch}
Tento nástroj lze použít k zostření hran.

Sub režim je `Invert` a bude vrcholy od sebe odtlačovat.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Ořez {#trim}
Nástroj Trim funguje tak, že odstraní část sítě a nabízí volby, jak zpracovat vzniklou mezeru. Pro definování řezu používá [Selection controls](#selection-controls).

::: tip
Protože tento nástroj promítá z kamery, dostanete varování, pokud je kamera v perspektivním režimu.

V ortografickém režimu je řez skrz síť rovnoběžný s pohledem, což lidé obvykle očekávají. V perspektivě bude řez na vzdálenější straně objektu vypadat jinak než na bližší.
:::

#### Nastavení nástroje Ořez {#trim-settings}

* `Stroke painting` - Pokud je v nabídce Paint zapnuto malování, zaplátovaná oblast bude vyplněna aktuálně zvolenou barvou.
* `Boolean` - Zaplní díru po řezu oblastí z quad polygonů. Vyplněná oblast bude plochá.
* `Legacy` - Zaplní díru po řezu triangulovanou oblastí. Vyplněná oblast bude plochá.
* `Fill` - Zaplní díru triangulovanou oblastí. Vyplněná oblast bude zakřivená plocha, jako film mýdlové bubliny.
* `None` - Dírku nevyplňovat.
* `Boolean Detail Shape` - Přibližná velikost quadů a trojúhelníků použitých na straně tvaru řezu.
* `Boolean Detail Hole` - Přibližná velikost trojúhelníků nebo polygonů použitých na vyplněné díře řezu. 
* `Legacy Detail` - Přibližná velikost trojúhelníků použitých na řezu.
* `Legacy Hole smoothing` - Jak moc jsou trojúhelníky na vyplněné oblasti relaxovány.
* `Legacy Threshold espilon` - Hodnota, kterou lze upravit pro zlepšení staršího algoritmu vyplňování děr.
* `Fill Detail` - Přibližná velikost trojúhelníků použitých na řezu.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Rozdělit {#split}
Podobné nástroji [Trim](#trim), s tím rozdílem, že Trim výběr zahodí, zatímco Split výběr zachová jako nový objekt.

#### Nastavení nástroje Rozdělit {#split-settings}

* `Stroke painting` - Pokud je v nabídce Paint zapnuto malování, zaplátovaná oblast bude vyplněna aktuálně zvolenou barvou.
* `Boolean` - Zaplní díru po splitu oblastí z quad polygonů. Vyplněné oblasti budou ploché.
* `Legacy` - Zaplní díru po splitu triangulovanou oblastí. Vyplněné oblasti budou ploché.
* `Fill` - Zaplní díry triangulovanou oblastí. Vyplněné oblasti budou zakřivené plochy, jako film mýdlové bubliny.
* `None` - Dírky nevyplňovat.
* `Boolean Detail Shape` - Přibližná velikost quadů a trojúhelníků použitých na straně tvaru splitu.
* `Boolean Detail Hole` - Přibližná velikost trojúhelníků nebo polygonů použitých na vyplněné díře splitu. 
* `Legacy Detail` - Přibližná velikost trojúhelníků použitých na splitu.
* `Legacy Hole smoothing` - Jak moc jsou trojúhelníky na vyplněné oblasti relaxovány.
* `Legacy Threshold espilon` - Hodnota, kterou lze upravit pro zlepšení staršího algoritmu vyplňování děr.
* `Fill Detail` - Přibližná velikost trojúhelníků použitých na splitu.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projekce {#project}
Nástroj Project vypadá jako [Trim](#trim), ale nemaže ani nevytváří žádnou geometrii, pouze posouvá vrcholy tak, aby odpovídaly výběru.

![](/videos/tool_project.mp4)

::: tip
Pokud použijete Project v rámci vrstvy, můžete pomocí posuvníku vrstvy míchat mezi původním a projektovaným tvarem.
:::

### ![](/icons/tool_layer.webp) Vrstvy {#layer}
Zvedá povrch, ale omezuje výšku.

Pokud držíte pero dole a přejíždíte přes oblast, Layer zvedne do určité výšky a dál už ne, na rozdíl od jiných nástrojů, které budou výšku stále kumulovat.

Všimněte si, že ve výchozím nastavení je limit nastaven pouze na tah! Pokud začnete nový tah, bude se stavět z nové výšky povrchu.

Pro nastavení konstantní maximální výšky napříč mnoha tahy použijte nástroj Layer se systémem [Layers](layers.md) v Nomadu.

Vytvořte vrstvu a použijte tento nástroj. Maximální výška je nyní nastavena z vrstvy, takže můžete aplikovat mnoho tahů a výška bude vždy stejná.

`Sub` použije minimální hloubku a vytváří rýhy.

#### Nastavení vrstev {#layer-settings}

* `Use layer data` - Pokud je aktivní a je vybraná vrstva, použije data vrstvy pro nastavení maximální výšky.
* `Inflate`- Pokud je aktivní, upraví směr, kterým Layer pracuje, pro hladší výsledky.
* `Relax (Normal)` - Množství vyhlazení aplikovaného na normály.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Nafouknout {#inflate}
Posouvá vrcholy podél jejich vlastních normál. `Sub` posouvá vrcholy podél jejich invertované normály.

#### Nastavení nástroje Nafouknout {#inflate-setings}
* `Relax (Normal)` - Množství vyhlazení aplikovaného na normály.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Postrčit {#nudge}
Posouvá nebo „rozmazává“ body ve směru tahu.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Razítko {#stamp}

Klepněte a táhněte pro zvednutí oblasti sochy ve tvaru zvoleného Alpha.

Jde jednoduše o [Brush](#brush) se stroke typem nastaveným na `Lock + radius`. 

`Sub` vtlačí stamp dovnitř místo toho, aby ho vytahoval z povrchu.

::: tip
Stamp obvykle funguje nejlépe s geometrií ve vysokém rozlišení. Pokud online vyhledáte „wrinkles alpha“, „pores alpha“, „scales alpha“ atd., tyto alpha textury a Stamp mohou být skvělým způsobem, jak přidat organické detaily do sochy postavy.

Dva režimy stroke jsou užitečné pro různé věci. 

* `Lock + radius` má pevnou *výšku*, tažením upravujete šířku a rotaci stampu. Dobré pro textury kůže, kde musí mít stejnou hloubku/výšku, ale různé rotace a měřítka pro skrytí opakujících se vzorů.
* `Lock + intensity` má pevnou *šířku*, tažením upravujete rotaci a výšku stampu. Dobré pro nýty, kde musí mít všechny stejnou velikost, ale různé rotace a výšky. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Smazat vrstvu {#delete-layer}
Tento nástroj může lokálně resetovat vrstvy, musíte mít aktivní vrstvu, jinak se nic nestane.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Trubice {#tube}
Vytvořte trubici nakreslením křivky. 
![](/images/tool_tube_new.webp)

Jakmile je trubice vytvořena, lze cestu upravovat ve 3D prostoru pomocí podobných ovládacích prvků jako standardní nástroje [Shape editing](#shape-editing) a úpravy křivek. 

![](/videos/tool_tube.mp4)

#### Levý panel nástroje Trubice {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Levý panel nástrojů má následující volby:

* `Sync` - Pokud je aktuální trubice instancovaná a existují poduzly trubice, které se mezi instancemi liší, tímto je znovu synchronizujete.
* `Snap` - Pokud je aktivní, režimy Curve a Path se při kreslení přichytávají na jiné objekty. Pokud je vypnutý, první bod se přichytí, pak se zbytek trubice nakreslí v této hloubce. Má malé rozbalovací menu:
    * `Offset` - Nastaví hloubku přichycení; 0 % znamená, že střed průřezu trubice se přichytí k povrchu, kladné hodnoty ho zvednou od povrchu, záporné ho sníží.
* `Curve` - Volně nakreslete trubici. Má malé rozbalovací menu:
    * `Auto-validate` - Vytvoří trubici hned po dokončení tahu. Po vypnutí bude vedle cesty křivky viditelný zelený validační kruh, stiskněte ho pro potvrzení, nebo použijte odkaz `Reset`, který se v této nabídce objeví pro odstranění cesty.
    * `Closed` - Udělá z trubice smyčku.
    * `Screen` - Dostupné pouze pokud je Auto-validate vypnuté. Pokud je aktivní, cesta je „připnutá“ k obrazovce, což umožňuje pohybovat pohledem a objektem, zatímco cesta zůstává na místě. Pokud je vypnuté, cesta je součástí 3D scény a pohybuje se s kamerou a objekty.
    * `Accuracy` - Kolik bodů křivky se použije pro převod nakreslené cesty na trubici. 0 % použije nejnižší počet bodů, ale vynechá malé změny zakřivení cesty. 100 % bude velmi přesné a použije mnoho bodů.
* `Path` - Vytvořte trubici klikáním pro definování bodů křivky. Klepněte na zelený kruh pro potvrzení cesty. Má malé rozbalovací menu:
    * `B-spline` - Alternativní metoda kreslení křivky, kde body křivky obvykle neleží přímo na křivce, ale může dávat hladší výsledky než výchozí metoda.
    * `Closed` - Udělá z trubice smyčku
    * `Screen` - Pokud je aktivní, cesta je „připnutá“ k obrazovce, což umožňuje pohybovat pohledem a objektem, zatímco cesta zůstává na místě. Pokud je vypnuté, cesta je součástí 3D scény a pohybuje se s kamerou a objekty.

##### Horní panel nástroje Trubice {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Když je trubice vybraná, v horní části viewportu se objeví panel nástrojů s dalšími ovládacími prvky. Kliknutím na název panelu ho sbalíte/rozbalíte a kliknutím na šipku vpravo nahoře panel přesunete nahoru nebo dolů ve viewportu.

* `Validate` - Zapeče trubici do běžných polygonů, aby bylo možné ji sochat.
* `Edit` - Zobrazí body křivky, aby je bylo možné upravovat
* `Mirror` - Přidá jako rodiče této křivky mirror repeater
* `Snap` - Přichytí body křivky k blízkým povrchům
* `Closed` - Spojí začátek a konec křivky do smyčky
* `B-spline` - Přepíná mezi interpolací Catmull-rom a B-spline.
* `Cap` - Cykluje mezi uzávěry na obou koncích trubice, pouze na začátku nebo konci, nebo bez uzávěrů.
* `Hole` - Přidá trubici tloušťku, čímž ji převede na dutou trubku. Cykluje mezi otvorem na obou koncích, pouze na konci nebo bez otvorů. 
* `Radius` - Cykluje mezi jednotným poloměrem, poloměrem na začátku a konci nebo poloměrem na každý bod křivky. Tyto se upravují oranžovými úchyty na křivce.
* `Twist` - Cykluje mezi žádným twistem, jednotným twistem, twistem na začátku a konci nebo twistem na každý bod křivky. Tyto se upravují růžovými úchyty na křivce.
* `Profile` - Cykluje mezi žádným profilem (tedy kruhovým profilem), jednotným profilem, profilem na začátku a konci nebo profilem na každý bod.
* `Profile edit` - Zobrazí editor profilu. Funguje podobně jako nástroje [Shape editing](#shape-editing), umí ukládat a načítat preset profilu a má přepínač pro úpravu profilu ve 3D prostoru.
* `Spiral` - Zobrazí nabídku pro přidání spirálového twistu trubici. Tato nabídka má volby `Twist Angle`, `Offset`, `Scale` a `Angle offset`.
* `X Divisions` - Počet dělení kolem trubice, např. 4 dělení vytvoří čtvercovou trubici. 
* `Constant density` - Pokud je aktivní, udržuje polygony čtvercové. Po vypnutí umožní nastavit `Y divisions` podél délky trubice.
* `...` - Nabídka nastavení Tube.

#### Přepínač mazání bodů křivky {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Pod panelem nástrojů je přepínač mazání bodu křivky. Když přetáhnete bod křivky blízko jiného, zčervená, což značí, že po uvolnění bude bod smazán. Pokud děláte malé úpravy a nechcete body mazat, tímto tlačítkem chování mazání bodů vypnete.



#### Nastavení nástroje Trubice {#tube-settings}
* `Primitive` - Tlačítka pro zapnutí/vypnutí UV nebo pro potvrzení (validate) trubice.
* `Post subdivision` - Zkratka pro nastavení úrovně multiresolution před potvrzením.
* `Linear subdivision` - Zkratka pro nastavení úrovně lineárního dělení před potvrzením. 
* `Division X` - Stejné jako X Divisions v panelu nástrojů.
* `Division Y` - Stejné jako Y Divisions v panelu nástrojů.
* `Curve (Repeater)` - Převede trubici na [Curve Repeater](scene.md#curve)

::: tip
Division nastavené na 4 a Post subdivision na 3 vytvoří hladké trubice s kulatými konci, vhodné pro červy, hady, části těla.
:::


### ![](/icons/tool_lathe.webp) Soustruh {#lathe}
Vytvoří rotační plochu nakreslením křivky.

Tento nástroj je skvělý pro tvary jako vázy, sklenice na víno.

![](/videos/tool_lathe.mp4)

#### Levý panel nástroje Soustruh {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Levý panel nástrojů má následující volby:

* `Sync` - Pokud je aktuální lathe instancované a existují poduzly lathe, které se mezi instancemi liší, tímto je znovu synchronizujete.
* `Fixed` - Pokud je zapnuto, střed lathe je pevný a zobrazený na obrazovce. Tato středová čára má editační body, které lze upravovat. Pokud je vypnuto, střed lathe se dynamicky aktualizuje tak, aby odpovídal začátku a konci nakreslené křivky.
* `Curve` - Nakreslete profil lathe jedním tahem. Má malé rozbalovací menu:
    * `Auto-validate` - Pokud je zapnuto, lathe se vytvoří, když zvednete pero z obrazovky. Pokud je vypnuto, vedle křivky se objeví zelený kruh, kterým lathe vytvoříte. Křivku lze smazat tlačítkem `Reset`.
    * `Closed` - Spojí začátek a konec křivky do smyčky
    * `Screen` - Dostupné pouze pokud je Auto-validate vypnuté. Pokud je aktivní, cesta je „připnutá“ k obrazovce, což umožňuje pohybovat pohledem a objektem, zatímco cesta zůstává na místě. Pokud je vypnuté, cesta je součástí 3D scény a pohybuje se s kamerou a objekty.
    * `Accuracy` - Kolik bodů křivky se použije pro převod nakreslené cesty na trubici. 0 % použije nejnižší počet bodů, ale vynechá malé změny zakřivení cesty. 100 % bude velmi přesné a použije mnoho bodů.
* `Path` - Vytvořte lathe klikáním pro definování bodů křivky. Klepněte na zelený kruh pro potvrzení cesty. Má malé rozbalovací menu:
    * `B-spline` - Alternativní metoda kreslení křivky, kde body křivky obvykle neleží přímo na křivce, ale může dávat hladší výsledky než výchozí metoda.
    * `Closed` - Udělá z trubice smyčku
    * `Screen` - Pokud je aktivní, cesta je „připnutá“ k obrazovce, což umožňuje pohybovat pohledem a objektem, zatímco cesta zůstává na místě. Pokud je vypnuté, cesta je součástí 3D scény a pohybuje se s kamerou a objekty.

#### Horní panel nástroje Soustruh {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Když je lathe vybrané, v horní části viewportu se objeví panel nástrojů s dalšími ovládacími prvky. Kliknutím na název panelu ho sbalíte/rozbalíte a kliknutím na šipku vpravo nahoře panel přesunete nahoru nebo dolů ve viewportu.

* `Validate` - Zapeče lathe do běžných polygonů, aby bylo možné ho sochat.
* `Edit` - Zobrazí body křivky, aby je bylo možné upravovat
* `Mirror` - Přidá jako rodiče tohoto lathe mirror repeater
* `Snap` - Přichytí body křivky k blízkým povrchům
* `Stable` - Pokud je zapnuto, profil křivky bude parentován ke středové čáře lathe. Pokud je vypnuto, středovou čáru lze upravovat a nebude křivku posouvat, což umožňuje složitější tvary.
* `Focus` - Otočí pohled tak, aby byl profil křivky dokonale plochý vůči kameře.
* `Closed` - Spojí začátek a konec křivky do smyčky
* `Cap` - Pokud je Closed vypnuté, cykluje mezi uzávěry na obou koncích trubice, pouze na začátku nebo konci, nebo bez uzávěrů.
* `Hole` - Přidá lathe tloušťku, čímž ho převede na dutou trubku. Cykluje mezi otvorem na obou koncích, pouze na konci nebo bez otvorů. 
* `B-spline` - Přepíná mezi interpolací Catmull-rom a B-spline.
* `X Divisions` - Počet dělení kolem lathe, např. 4 dělení vytvoří lathe se čtvercovým profilem. 
* `Constant density` - Pokud je aktivní, udržuje polygony čtvercové. Po vypnutí umožní nastavit `Y divisions` podél délky trubice.
* `...` - Nabídka nastavení Lathe.

#### Nastavení nástroje Soustruh {#lathe-settings}
* `Primitive` - Tlačítka pro zapnutí/vypnutí UV nebo pro potvrzení (validate) trubice.
* `Post subdivision` - Zkratka pro nastavení úrovně multiresolution před potvrzením.
* `Linear subdivision` - Zkratka pro nastavení úrovně lineárního dělení před potvrzením. 
* `Division X` - Stejné jako X Divisions v panelu nástrojů.
* `Division Y` - Stejné jako Y Divisions v panelu nástrojů.
* `Curve (Repeater)` - Převede profil křivky na [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Vložit {#insert}
Umístí objekt na povrch jiného. Použitím je podobný nástroji Stamp, ale pro plné 3D tvary.

Pokud vyberete primitivum z levého panelu nástrojů, klepnutí a tažení na jakýkoli povrch umístí primitivum na místo kliknutí, tažení nastaví velikost. Po dokončení tažení se Insert přepne do režimu [Transform](#transform).

V režimu Instance tažení vytvoří a posune novou instanci po povrchu. Velikost bude zkopírována z prvního tvaru, takže můžete umístit mnoho stejně velkých instancí objektu na jiné povrchy.

Nemusíte vkládat jen primitiva! Vyberte *jakýkoli* tvar v outlineru, pokud je Insert v režimu Instance nebo Clone, můžete přetahovat kopie vybraného objektu po jakémkoli jiném povrchu.

Pokud má objekt vlastní pivot, použije se jako kotevní bod. Viz video níže.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformace {#transform}
Přesouvá/otáčí/škáluje model přímo jedním a dvěma prsty, obvykle po povrchu jiného objektu.

Nástroj se ovládá levým panelem nástrojů a má 5 tlačítek:

* `Snap` - Přichytí model na jiné povrchy
* `Group` - Pokud má vybraný objekt kombinaci objektů a instancí, toto umožňuje určit chování nástroje.
* `Move` - Tažení jedním prstem přesune objekt. Pokud je Snap aktivní, bude objekt klouzat po povrchu pod vaším prstem.
* `Rotate` - Tažení jedním prstem otočí objekt. Pokud je Snap aktivní, bude rotovat kolem normály povrchu pod vaším prstem.
* `Scale` - Tažení jedním prstem škáluje objekt.

Transform lze použít pro rychlé ovládání 2 z těchto režimů pomocí dvou prstů:

* Přetáhněte objekt pro jeho umístění. Přestaňte prvním prstem hýbat, ale nezvedejte ho z obrazovky.
* Dotkněte se druhým prstem obrazovky, zatímco první prst držíte dole. Jak druhý prst táhnete, objekt se škáluje.
* Zvedněte druhý prst a pokračujte v tažení prvním prstem, objekt bude opět v režimu Move.

Druhý režim můžete změnit také klepnutím druhým prstem:

* Přetáhněte objekt pro jeho umístění, přestaňte hýbat, ale nezvedejte prst z obrazovky.
* Klepněte druhým prstem, zatímco první prst držíte dole
* Nástroj se přepne do režimu Rotate. Tažením prvního prstu nastavíte rotaci.
* Klepněte druhým prstem znovu, nástroj se přepne zpět do režimu Move.

To umožňuje rychlý pracovní postup pro klonování objektů po jiném, např. kameny po krajině. Všimněte si, že tlačítko Clone je také v levém panelu nástrojů pro snadný přístup:

* Použijte nástroj Transform pro umístění kamene.
* Pusťte, stiskněte tlačítko Clone
* Přesuňte tento kámen, otočte/škálujte podle potřeby
* Pusťte, stiskněte tlačítko Clone
* Přesuňte tento kámen, opakujte.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Tento nástroj umožňuje přesouvat, otáčet a škálovat objekty a měnit pivoty objektů.

Ovládací prvek ve viewportu má následující funkce:

* `Move` - Tažením na čáře se šipkou přesouváte v osách X/Y/Z. Tažením na broskvovém bodu uprostřed gizma přesouváte volně v rovině obrazovky. Kliknutím na červené, zelené, modré čtverce přesouváte v rovinách X/Y/Z.
* `Rotate` - Tažením na červených/zelených/modrých kruzích rotujete v osách X/Y/Z. Tažením na kouli uvnitř kruhů rotujete volně.
* `Scale`- Tažením na vnějších červených/zelených/modrých bodech škálujete v osách X/Y/Z. Tažením na vnějších červených/zelených/modrých kuželech škálujete v rovinách X/Y/Z. Tažením na vnějším broskvovém kruhu škálujete jednotně.

![](/images/tool_gizmo.webp)

#### Uzly a vrcholy {#nodes-and-vertices}

Každý objekt v Nomadu se skládá z uzlu a vrcholů:

* `Node` - „Rukojeť“ objektu, která ukládá jeho posun, rotaci a škálu, tzv. transformační matici.
* `Vertices` - Body, které definují povrch objektu, ukládají pozici a informace o malbě.

Pokud máte jednoduchou kostku složenou z 8 vrcholů, můžete ji posunout úpravou transformační matice nebo úpravou pozic vrcholů. Při sochání obvykle chcete upravovat vrcholy, při přesouvání objektů pomocí gizma obvykle chcete upravovat uzel. Nomad umožňuje obojí. 

#### Levý panel nabídky {#left-menu-toolbar}

Levý panel ovládá, zda bude gizmo pracovat s uzlem nebo vrcholy, a další funkce:

* `Clone` - Vytvoří samostatnou kopii aktuálního objektu, kterou lze odtáhnout pomocí gizma.
* `Instance` - Vytvoří instanční kopii aktuálního objektu. Objekty jsou propojené, takže změny sochání na jednom objektu se projeví na všech instancích.
* `Group/Object/Vertex/Auto` - Nastaví, zda bude gizmo ovlivňovat uzel nebo vrcholy objektu. Výchozí režim „auto“ se pokusí o nejlepší odhad. Pokud je několik objektů zřetězených v hierarchii, „Object“ přesune pouze aktuální objekt, podřízené objekty zůstanou na místě. Gizmo může také brát v úvahu maskování a symetrii.
* `Pin` - Ve výchozím nastavení se gizmo přesune k pivotu vybraného objektu. Pokud je Pin zapnutý, gizmo zůstane tam, kde právě je.
* `Align` - Přepíná pivot zarovnaný s aktuálním objektem nebo se světem.
* `Snap rotation` - Zapne přichytávání hodnot rotace na kroky, hodnota kroku se zobrazuje a lze ji upravit, když je Snap aktivní.
* `Snap translation` - Zapne přichytávání hodnot posunu na kroky, hodnota kroku se zobrazuje a lze ji upravit, když je Snap aktivní.
* `Pivot` - Pokud je zapnuto, lze gizmo přesouvat a otáčet bez pohybu objektu. Má další nabídku vysvětlenou níže.

#### Střed (Pivot) {#pivot}
Když je režim Pivot aktivní, zobrazí se nabídka pro rychlé změny pivotu:

**Reset** 
* `Center` - Přesune pivot do středu objektu
* `Bottom` - Přesune pivot na spodní část objektu
* `Align` - Resetuje rotace tak, aby byly zarovnány se světem.
* `Mask` - Přesune pivot do středu nemaskované oblasti.

**On Tap**
* `None` - Při klepnutí na objekt nic nedělá
* `Normal` - Přesune a otočí pivot tak, aby se zarovnal s místem klepnutí na povrch
* `First` - Přesune (ale neotočí) pivot na místo klepnutí na povrch
* `Medial` - Přesune pivot doprostřed objektu pod místo klepnutí na povrch.

#### Nastavení Gizma {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Matice {#matrix}
* ![](/icons/target.webp) `Move origin` - Přesune objekt tak, aby jeho pivot byl ve středu scény, tzv. v počátku.
* ![](/icons/bake.webp)  `Bake` - „Zamrazí“ objekt v aktuální pozici a nastaví hodnoty translate/rotate na 0, scale na 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Nastaví hodnoty matice tak, aby odpovídaly pozici gizma ve světě.
* ![](/icons/reset.webp) `Reset` - Zkratka, která nastaví hodnoty posunu na 0, rotace na 0, scale na 1 a objekt přesune a otočí.

::: tip Bake vs bake to pivot
Vytvořte kostku, vyberte nástroj Gizmo, otevřete a připněte nabídku nastavení. Ve výchozím nastavení jsou posun a rotace 0, scale je 1.

Zapněte režim Pivot, přesuňte gizmo na jednu stranu, vypněte Pivot. Pivot se změnil, ale všimněte si, že hodnoty posunu jsou stále 0. 

Pokud chcete vidět, kde pivot *skutečně* je, klikněte na `Bake Pivot`. Nyní se hodnoty posunu aktualizují. Všimněte si, že kostka se během této operace ani v režimu Pivot nepohne.

Přesuňte a otočte kostku někam a pak klepněte na `Move Origin`. Přesune objekt tak, aby jeho pivot byl ve středu světa, ale rotaci ponechá beze změny.

Klikněte na `Reset` a rotace se také nastaví na 0.

Znovu kostku přesuňte a otočte, tentokrát klikněte na `Bake`. Pivot zůstane tam, kde je, kostka zůstane tam, kde je, ale hodnoty posunu a rotace se nastaví na 0.

Procvičte si to několikrát! Získejte představu, že hodnoty pivotu jsou skryté, Nomad se o ně stará za vás, ale pokud potřebujete nastavit pivot na skutečná místa v prostoru, Bake Pivot to pro vás udělá.

:::

* `Translation` - Hodnoty posunu X, Y, Z
* `Rotation` - Hodnoty rotace X, Y, Z
* `Scale` - Jednotná škála, pokud je zapnutá, nebo škála X, Y, Z, pokud je vypnutá.
* `Uniform scale` - Přepíná možnost škálovat jednotně nebo nezávisle v každé ose

-----

* `Compact` - Přepíná rozložení gizma tak, aby byly další úchyty vně nebo uvnitř rotační koule
* `Widget size` - Velikost gizma
* `Thickness` - Tloušťka čar gizma
* `Opacity` - Průhlednost gizma
* `Hide on interaction` - Přepíná, zda se má gizmo při tažení dočasně skrýt

-----

* `Tangent roll threshold` - Ovládá chování rotačního UI při tažení na kruhových úchytech pro rotaci v osách X/Y/Z. Pokud je hodnota 0, rotace funguje jako ciferník, gizmo táhnete v kruzích. Pokud je hodnota 90, rotace funguje jako tahání za provázek joja; táhnete v přímce směrem k místu prvního kliknutí nebo od něj. Hodnoty mezi 0 a 90 dělají kombinaci obojího; pod hodnotou bude lineární pohyb, nad hodnotou kruhový.
* `Numerical input` - Pokud je zapnuto, jedno klepnutí na gizmo zobrazí okno pro zadání přesné hodnoty pro osu klepnutého widgetu.

::: warning
Nástroje [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) a [Scale](#scale) používají vlastní zaškrtávací políčko symetrie!

Ve výchozím nastavení je tato symetrie vypnutá.
:::

Vlevo můžete přesouvat pivot gizma, viz video níže v akci.
To je obzvlášť užitečné pro rotaci, protože to nemění nic na posunu.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Skupina ploch {#facegroup}

Facegroup vám umožňují organizovat objekt do různě barevných ploch. Tyto skupiny můžete v Nomadu používat mnoha způsoby:

* Rychlá metoda výběru pro masky
* Skrývání/zobrazování částí objektu
* Organizace objektu bez nutnosti ho rozdělovat na samostatné části
* Definování UV oblastí
* Navádění nástroje quad remesher
* Dodatečná kontrola pro nástroje jako Smooth.

#### Levý panel nástroje Skupina ploch {#facegroup-left-toolbar}

* `Patch ` - Zobrazí dostupné facegroup jako „záplaty“. Nepoužívané záplaty lze smazat. Klepnutím na záplatu ji přejmenujete nebo změníte její barvu. Ikona plus umožňuje vytvářet nové záplaty.
* `Dot` - Malujte na objekt pro definování facegroup. Pokud je zapnuto `+ Face Group`, každý nový tah automaticky vytvoří novou facegroup, užitečné pro rychlé definování oblastí. Klepnutí zaplní vybranou oblast. Posuvník nastavuje poloměr tečky.
* `Relax` - Vyhlazuje hranice facegroup. Velmi užitečné pro definování čistých hran pro quad remeshing nebo pro definování panelů pro hard-surface modelování. Posuvníky ovládají poloměr a intenzitu operace Relax.
* `Shape selector` - Vytváří facegroup pomocí tvarů místo štětce, přes `Lock+Radius`, `Lasso`, `Polygon`, `Rect` a `Ellipse`. Více informací viz [Shape Selector](#shape-selector).
* `Auto-pick` - Pokud je zapnuto, vybere záplatu, kde tah začíná, a tuto záplatu použije pro zbytek tahu. Velmi užitečné pro úklid oblastí facegroup; pokud se facegroup rozšířila příliš daleko, zapněte Auto-pick, začněte tah z místa, kde je záplata správná, a táhněte k hranici pro znovupřiřazení správné záplaty.

### ![](/icons/tool_hide.webp) Skrýt {#hide}
Skrývá nebo izoluje části objektu. 

Hlavní režimy se ovládají z levého panelu:

* `Dot` - Štětcem na objektu skrývá části objektu.
* `Shape selector` -  Skrývá pomocí tvarů místo štětce, přes `Lasso`, `Polygon`, `Line`, `Rect` a `Ellipse`. Více informací viz [Shape Selector](#shape-selector).
* `Show` - Inverze operace, takže zvolený režim bude části objektu zobrazovat místo skrývat.

V horní části viewportu se objeví panel nástrojů s dalšími ovládacími prvky:

* `Clear` - Obnoví objekt, všechny skryté části se odhalí.
* `Invert` - Prohodí skryté a viditelné části.
* `Facegroup` - Použije facegroup pro rychlé skrývání částí, klepnutím na facegroup skryjete celou skupinu.
* `Mask` - Pokud je aktivní maska, klepnutím na toto tlačítko skryjete maskovanou část.
* `Delete` - Smaže skrytou část objektu
* `Split` - Rozdělí skrytou část objektu do nového tvaru.

### ![](/icons/tool_measure.webp) Měření {#measure}
Tažením změříte vzdálenost mezi dvěma body.

### ![](/icons/tool_remesh.webp) Čtyřúhelníkový remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Tento nástroj převede vybraný objekt na čisté quad topologické uspořádání s ovládáním hustoty, toku hran a symetrie. 

::: tip
Quad Remesher vyvíjí [Exoside](https://exoside.com/) pro iOS a desktop. 

Pro iOS je to nákup v aplikaci v Nomadu, jednorázová platba 16 USD.

Pro desktop si zakupte licenci od [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Můžete si ho koupit jen pro Nomad desktop nebo jako křížovou licenci pro všechny podporované desktopové aplikace.

Pokud již vlastníte Quad Remesher pro jinou desktopovou aplikaci, můžete [zakoupit upgrade na všechny platformy za nižší cenu.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher není dostupný pro Android. Android může použít bezplatný open-source „Quad Remesh - Instant“ dostupný v nabídce Topology -> Misc, ale mějte na paměti, že jeho sada funkcí je velmi omezená.
:::

When je tento nástroj poprvé aktivován, zeptá se, zda jej chcete povolit jako nákup v aplikaci. Jakmile je aktivní, levý a horní panel nástrojů budou povoleny.

* `Dot` - Tento štětec nastaví cílovou hustotu. Intenzita 100 % bude malovat červeně, což v těchto oblastech použije dvojnásobnou cílovou hustotu quadů. Intenzita 0 % bude malovat tyrkysově, což v těchto oblastech použije poloviční cílovou hustotu quadů. Intenzita 50 % bude malovat šedě, což použije výchozí cílovou hustotu quadů.
* `Smooth` - Vyhlazuje přechody mezi červenou/šedou/tyrkysovou hustotou.
* `Curve` - Skicuje křivky na povrchu sochy, quad remesher je použije jako vodítka pro tok hran. Klepnutím na křivku ji smažete.
* `Path` - Kreslí cesty na povrchu sochy, quad remesher je použije jako vodítka pro tok hran. Klepnutím na cestu ji smažete. 
* `Rect` - Kreslí obdélníky na povrchu sochy, quad remesher je použije jako vodítka pro tok hran. Klepnutím na cestu ji smažete.
* `Ellipse` - Kreslí elipsy na povrchu sochy, quad remesher je použije jako vodítka pro tok hran. Klepnutím na cestu ji smažete.

#### Horní panel Čtyřúhelníkového remesheru {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

V horní části viewportu se objeví panel nástrojů s dalšími ovládacími prvky:


* `<Count>` - Kliknutím spustíte proces quad remesheru, toto číslo udává, jaký bude cílový počet quadů.
* `Quads` - Nastavte cílový počet quadů tažením doleva a doprava, nebo klepnutím zadejte přesné číslo. Všimněte si, že jde spíše o vodítko než pevné číslo, různé ovládací prvky quad remesheru často způsobí, že výsledek nebude přesně odpovídat tomuto cíli.
* `Half` - Zkratka pro nastavení cílového počtu na polovinu aktuálního počtu polygonů.
* `Same` - Zkratka pro nastavení cílového počtu na aktuální počet polygonů.
* `Guides` - udává celkový počet vodítek, nebo klepnutím smažete všechna vodítka.
* `Density X` - klepnutím odstraníte veškeré malování hustoty.
* `Density (painting)` - přepínač pro použití nebo ignorování malování hustoty.
* `Face Group` - přepínač pro použití nebo ignorování facegroup pro řízení quad remesheru.
* `Relax` - přepínač pro automatické uvolnění hranic facegroup během quad remeshingu. Pokud jste již hranice facegroup uvolnili/vyhladili, tuto volbu zakažte.
* `Relax Slider` - Zkratkový posuvník pro uvolnění hranic facegroup.
* `Hard Edges` - přepínač pro pokus o zachování ostrých hran.
* `Reproject Vertex` - přepínač pro reprojekci nového rozložení na vstupní mesh.
* `Symmetry` - Přepínač pro povolení symetrického výsledku. Všimněte si, že symetrie je vždy počítána kolem světové osy X, takže pokud očekáváte symetrický výsledek, ujistěte se, že je váš model v počátku souřadnic.
* `...` - Nabídka nastavení Quadremesheru. 

#### Nabídka nastavení Čtyřúhelníkového remesheru {#quad-remesher-settings-menu}

Většina těchto nastavení je dostupná v horním panelu nástrojů.

* `<Count>, Half, Same` - Stejné jako tlačítka Remesh, Half, Same v horním panelu nástrojů.
* `Target Quads` - Stejné jako tlačítko `Quads` v horním panelu nástrojů
* `Adaptive quad count` - přepínač pro použití menších quadů v oblastech s vysokým zakřivením a větších quadů v oblastech s nižším zakřivením.
* `Adaptive size` - Nastavte míru adaptivity. 100 % umožní maximální adaptivní velikost, při 0 % budou quady jednotné.
* `Auto-Detect Hard Edges` - přepínač pro přizpůsobení rozložení quad remeshe tak, aby lépe sledovalo ostré povrchy.
* `Density (painting)` - Stejné jako tlačítko `Density (painting)` v horním panelu nástrojů
* `Reproject Vertex` - přepínač pro reprojekci nového rozložení na vstupní mesh.
* `Face Group` - Stejné jako tlačítko `Face Group` v horním panelu nástrojů
* `Relax Slider` - Zkratkový posuvník pro uvolnění hranic facegroup.

::: tip

Recept, jak získat dobrý quad remesh s minimem artefaktů:

* Rozdělte mesh do facegroup, abyste definovali ideální tok quadů.
* Použijte Facegroup relax pro získání hladkých hranic facegroup.
* Decimate. Tím zajistíte, že na hranách facegroup nebudete mít tenké nebo deformované plochy. V nastavení decimate se ujistěte, že je facegroup povoleno. To způsobí, že hrany trojúhelníků budou přesně sledovat hrany vašich facegroup. 

V možnostech quad remeshe se ujistěte, že je relax vypnutý (protože jste mesh již uvolnili) a měli byste získat dobré výsledky.

:::

### ![](/icons/tool_select.webp) Výběr {#select}
Použijte režimy tvaru k výběru objektů ve scéně. `Unselect` odstraní objekty z výběru.

### ![](/icons/tool_view.webp) Pohled {#view}
Tento „nástroj“ nedělá nic konkrétního, je to pouze způsob, jak si model prohlížet bez úprav vaší scény.


## Kontekstová nabídka nástrojů {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Kliknutí pravým tlačítkem nebo dlouhé stisknutí nástroje v toolboxu vyvolá kontextovou nabídku. Tato nabídka má následující možnosti:

* `Save` - uloží všechny změny, které jste v nástroji provedli
* `Clone` - duplikuje nástroj do nové zkratky nástroje
* `Last save` - vrátí se k naposledy uložené verzi nástroje
* `Icon` - změní ikonu nástroje
* `Reset` - resetuje nástroj na jeho výchozí nastavení