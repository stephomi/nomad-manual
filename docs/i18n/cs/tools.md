# ![](/icons/toolbox.webp) Nástroje {#tools}

![](/images/tools_menu.webp)

::: tip
Popisy jednotlivých nástrojů najdete níže v části [Nástroje](#tools-1).
:::

## Přehled {#overview}

Nástroje vybíráte v panelu `Nástroje` vpravo a ovládáte je pomocí `Ovládání nástroje` vlevo. Další nastavení najdete v menu `Nástroj` v pravém horním menu.

Štětce mají ovládání velikosti a intenzity. Výběrové nástroje mají ovládání pro několik stylů výběru. Ve spodní části ovládání nástroje jsou zkratky pro často používané operace (Hladit, Maska, Skrýt, Skupina ploch, Gizmo, Barva, Alfa).

Nástroje Nomadu jsou v panelu nástrojů barevně rozlišené (pro prosté popisky vypněte `Barevné nástroje` v menu [Rozhraní](interface.md)):

* <span class=brush>**Štětce**</span> (Hlína, Štětec, Hladit, Vrstva, Zvětšit, Smazat vrstvu, Quad Remesher)
* <span class=move>**Nástroje pro přesun**</span> (Přesunout, Táhnout, Elastický, Posunout)
* <span class=mask>**Nástroj Maska**</span> (Maska)
* <span class=paint>**Malířské nástroje**</span> (Malovat, Rozmazat)
* <span class=flatten>**Nástroje pro zploštění**</span> (Zploštit, Planar, Leštění)
* <span class=pinch>**Nástroje pro sevření**</span> (Rýha, Štípnout)
* <span class=stamp>**Razítka**</span> (Razítko, VDM)
* <span class=selection>**Nástroje založené na výběru**</span>, kde se nejdřív nakreslí 2d maska a pak proběhne operace (Oříznout, Rozdělit, Projekt)
* <span class=creation>**Nástroje pro tvorbu**</span> (Trubka, Soustruh, Vložit)
* <span class=transform>**Transformační nástroje**</span> (Přeměnit, Gizmo, Uspořádat, Mřížka)
* <span class=misc>**Různé nástroje**</span> (Skupina ploch, Skrýt)
* <span class=view>**Nástroje pro zobrazení**</span> (Pohled, Měřit, Vybrat)



Mnoho z těchto nástrojů můžete přizpůsobit v menu [Tah](stroke.md): jiné chování štětce, tlak, textury atd. 


### Ovládání štětce {#brush-controls}

Levý panel nástrojů má posuvníky pro poloměr a intenzitu a pod nimi ovládací prvky podle kategorie nástroje, popsané níže.

![](/images/tool_left_panel.webp)

::: tip
Posuvník intenzity jde u mnoha nástrojů nad 100 %, vyplatí se s tím experimentovat!
:::

### Vedlejší režim {#sub-mode}
Tlačítko přímo pod posuvníkem intenzity je tlačítko `Méně`. Jeho popisek a funkce se mění s každým nástrojem a po stisknutí vyvolá jiné, obvykle opačné chování. Například u nástroje [Malovat](#paint) zapne mazání, u nástroje [Rýha](#crease) vytvoří místo rýh vystouplé hrany atd.

Ve výchozím stavu funguje jako přídržné tlačítko: když ho podržíte, režim se dočasně zapne, a když ho pustíte, zase se vypne. Když na něj klepnete, vedlejší režim zůstane trvale zapnutý.

### Zkratky {#shortcuts}
Ve spodní části levého panelu nástrojů jsou zkratky pro [Hladit](#smooth), [Maska](#mask), [Skrýt](#hide), [Skupina ploch](#facegroup), [Gizmo](#gizmo), [Barva](painting.md#pbr-sliders), [Alfa](stroke.md#alpha) . 

Ve výchozím stavu všechny fungují jako přídržná tlačítka: když tlačítko podržíte, režim se dočasně zapne, a když ho pustíte, zase se vypne. Když na něj klepnete, režim zkratky zůstane trvale zapnutý.

### Ovládání výběru {#selection-controls}

Nástroje [Maska](#mask), [Malovat](#paint), [Oříznout](#trim), [Rozdělit](#split), [Projekt](#project), [Skupina ploch](#facegroup), [Skrýt](#hide) a [Vybrat](#select) používají k výběru oblastí sítě podobné ovládání.

![](/images/tools_shape_selector_panel.webp)

Klepněte na tlačítko tvaru v levém panelu nástrojů (ukazuje aktuální tvar, ve výchozím stavu `Laso`) a otevře se okno s tvary. U nástrojů, které fungují i se štětcem (Maska, Malovat, Skupina ploch, Skrýt), jsou ve stejném okně i typy tahu.

* `Zobrazit` - Žádný tvar, nástroj nedělá nic zvláštního, podobně jako režim kamery.
* `Laso` - Tvar kreslený od ruky
* `Polygon` - Uzavřený tvar složený z křivek a/nebo rovných čar. Více v části [Úprava tvaru](#shape-editing) níže.
* `Křivka` - (jen Projekt) - Křivka kreslená od ruky pro projekci
* `Cesta` - (jen Projekt) - Křivka definovaná body. Více v části [Úprava tvaru](#shape-editing) níže.
* `Čára` - Tažením nakreslíte čáru, která určí rovinný řez. Ve výchozím stavu se operace na síti provede hned, pokud to nechcete, změňte volbu `Upravit` (dlouhý stisk nebo přejetí po ikoně čáry)
* `Pás` - Pruh mezi dvěma rovnoběžnými vodítky s přechodem napříč. `Rozšířit` zachová plnou hodnotu i za vzdálenějším vodítkem, místo aby skončila na okraji pásu, `Obrátit` prohodí vodítko, od kterého přechod začíná.
* `Obdélník` -  Tažením nakreslíte úhlopříčku, která určí rohy obdélníku. Dlouhým stiskem nebo přejetím zobrazíte volbu `Upravit`, `Čtverec` pro vynucení čtvercového tvaru a `Centrovaný`, kdy první klepnutí určí střed obdélníku.
* `Elipsa` - Tažením nakreslíte úhlopříčku, která určí velikost elipsy. Dlouhým stiskem nebo přejetím zobrazíte volbu `Upravit`, `Kruh` pro vynucení kruhového tvaru a `Centrovaný`, kdy první klepnutí určí střed elipsy.
* `Převrátit` - Převrátí masku tvaru nebo směr nástroje Projekt.

Většina nástrojů má volbu `Upravit`, která určuje, co se stane, když tvar dokreslíte:
* `Úprava: vypnuto` - Operace proběhne hned, jak pustíte.
* `Úprava: zapnuto` - Tvar zůstane upravitelný. Vedle tvaru se objeví zelené tlačítko, které operaci provede. Můžete tak tvar upravit a změnit pohled, a když je tvar připravený, stisknete zelené tlačítko.
* `Úprava: podržet` - Operace proběhne po puštění, pokud na konci tahu nepodržíte prst, abyste mohli tvar dál upravovat.

### Úprava tvaru {#shape-editing}
Úprava polygonu a úprava křivky fungují podobně:

* Nejdřív tažením nakreslete čáru, která určí 2 body, pak táhněte ze středu čáry ven a vytvořte polygon nebo křivku.
* Klepnutím na bod přepnete mezi hladkým a ostrým.
* Klepnutím a tažením na úseku křivky nebo čáry vytvoříte nové body.
* Bod smažete tak, že ho přetáhnete na sousední bod, až zčervená.
* Ikona koše v rohu ikony polygonu nebo cesty tvar smaže.

### Menu nastavení {#settings-menu}

Mnoho nástrojů má další nastavení v menu `Nástroj` v pravém horním menu. U nástrojů bez dalších nastavení je menu zašedlé.

![](/images/tools_settings_menu.webp)

## Nástroje {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Hlína](#clay)       | ![](/icons/tool_brush.webp)   <br> [Štětec](#brush)     | ![](/icons/tool_move.webp)       <br> [Přesunout](#move)              | ![](/icons/tool_drag.webp)      <br> [Táhnout](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Elastický](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Hladit](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Maska](#mask)       | ![](/icons/tool_paint.webp)   <br> [Malovat](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Rozmazat](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Zploštit](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Planar](#planar)       | ![](/icons/tool_polish.webp)  <br> [Leštění](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Rýha](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Štípnout](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Oříznout](#trim)              | ![](/icons/tool_split.webp)     <br> [Rozdělit](#split)         | ![](/icons/tool_project.webp)   <br> [Projekt](#project)     | ![](/icons/tool_layer.webp)   <br> [Vrstva](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Zvětšit](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Posunout](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Razítko](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [Smazat vrstvu](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Trubka](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Soustruh](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Vložit](#insert)   | ![](/icons/tool_transform.webp)  <br> [Přeměnit](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Skupina ploch](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Skrýt](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Měřit](#measure) | [Uspořádat](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Vybrat](#select)       | ![](/icons/tool_lattice.webp)   <br> [Mřížka](#lattice)     | ![](/icons/tool_view.webp)    <br> [Pohled](#view)       |

------

### ![](/icons/tool_clay.webp) Hlína {#clay}
Nástroj Hlína se hodí k postupnému nabalování hmoty na sochu. `Méně` naopak hmotu ze sochy ubírá.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Štětec {#brush}
Standardní štětec. `Méně` hmotu ubírá.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Přesunout {#move}
Oblast pod štětcem se ke štětci přichytí, což umožňuje pružnou deformaci. Výběr se během přesunu nemění, takže když štětec odtáhnete a pak ho vrátíte tam, kde jste začali, žádnou deformaci neuvidíte.

Vedlejší režim je `Normální` a posouvá oblast pod štětcem ve směru normály povrchu.

Tento štětec se hodí jak na velké deformace, tak na pečlivé drobné úpravy.

#### Nastavení nástroje Přesunout {#move-settings}

* `Poloměr (Pozadí)` - Jak daleko od okraje modelu můžete být, abyste ještě modelovali; hodí se při práci na siluetě objektu. Odškrtněte ho, pokud chcete uchopovat jen tehdy, když začnete na modelu.
* `Pouze vrchol stejné strany` - Ignoruje vrcholy, které směřují opačně, než je směr deformace.
* `Směr` - Používá ho vedlejší režim `Normální` a určuje, zda tah povrch vytlačí, nebo vtáhne:
    * `Automaticky` - Vybere za vás jednu ze dvou metod níže podle úhlu normály povrchu.
    * `Normální 3D` - Porovná polohu ukazatele na obrazovce s normálou povrchu, jak ji vidí kamera.
    * `XY` - O vytlačení či vtažení rozhoduje poloha ukazatele na obrazovce (nahoru/dolů, vlevo/vpravo).
    * `Prahová hodnota` - U volby `Automaticky` mezní úhel, který rozhoduje, jaká metoda se použije.
* `Rychlost otáčení` - Uchopenou oblast můžete při přesunu natáčet: otočte dvěma prsty, otočte stylusem kolem jeho osy, nebo při tažení myší držte modifikační klávesu (Alt, Ctrl, Shift nebo Cmd). Pro prsty, stylus i myš je samostatný posuvník; odškrtnutím daný vstup vypnete.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Táhnout {#drag}
Oblast pod štětcem se ke štětci přichytí, což umožňuje pružnou deformaci. Na rozdíl od nástroje Přesunout se výběr během tahu průběžně aktualizuje, takže můžete vytahovat delší, hadovité tvary, zvlášť se zapnutou dynamickou topologií.

Vedlejší režim je `Normální` a posouvá oblast pod štětcem ve směru normály povrchu.

Tento štětec se hodí na volnější, gestické změny tvaru.

#### Nastavení nástroje Táhnout {#drag-settings}

Táhnout má stejná nastavení jako [Přesunout](#move-settings): `Poloměr (Pozadí)`, `Pouze vrchol stejné strany`, `Směr` a `Rychlost otáčení`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastický {#elastic}
Uchopí a táhne povrch jako [Přesunout](#move), ale s pružnou deformací: místo aby tah skončil na okraji štětce, plynule slábne se vzdáleností napříč objektem, trochu jako když natahujete gumu. Poloměr štětce určuje, jak široký tah bude.

Vedlejší režim je `Normální` a posouvá oblast pod štětcem ve směru normály povrchu.

Tento štětec se hodí na velké, měkké změny proporcí, které zůstanou hladké.

#### Nastavení nástroje Elastický {#elastic-settings}

Elastický má stejná nastavení jako [Přesunout](#move-settings), kromě `Pouze vrchol stejné strany`. `Poloměr (Pozadí)` je ve výchozím stavu vypnutý.

### ![](/icons/tool_smooth.webp) Hladit {#smooth}
Vyhlazuje oblast průměrováním poloh bodů. Tento nástroj hodně závisí na hustotě polygonů.
Čím víc polygonů máte, tím slabší vyhlazení bude.

Vedlejší režim je `Uvolnit`, který vyhlazuje jen drátěný model a snaží se zachovat geometrické detaily.

#### Nastavení nástroje Hladit {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Skupina ploch {#smooth-facegroup}

* `Uvolnit` - Vyhladí hranice skupin ploch. Pro rychlé vyhlazení hranic použijte intenzitu nad 100 %. `Auto` vyhlazuje jen tehdy, když je zapnutý náhled skupin ploch, `Ne` vyhlazování vypne, `Ano` ho zapne. 

##### Vrchol {#vertex}
* `Zachovat objem` - Vyhlazuje, aniž by se povrch smršťoval, takže opakované vyhlazování vaše tvary nevyfoukne. Tlačítko s ozubeným kolem vedle obsahuje hodnoty `Zmenšit` a `Zvětšit`, které se k tomu používají.
* `Zachovat hranice` - U sítí s otevřenými okraji, například roviny, se mohou rohy vyhladit. Tato volba udrží vrcholy na okraji sítě na místě.
* `Stabilní vyhlazení` - Snaží se, aby vyhlazení nezáviselo na topologii. Nejlépe funguje při proměnlivé hustotě topologie a s vysokou intenzitou vyhlazení.
* `Uvolnit` - Totéž co alternativní režim Uvolnit v levém panelu nástrojů.

##### Malování {#painting}
* `Vyhlazování obrazovky` - Tuto volbu použijte pro vyhlazení nezávislé na topologii, a to i při vysokém počtu polygonů. `Auto`, `Ne` nebo `Ano`.
* `Ukázky obrazovky` - Kvalita vyhlazení, vyšší hodnoty vyhlazují lépe, ale pomaleji.

::: tip
Při vyšší hustotě polygonů může být potřeba zvednout intenzitu nad 100 %. Velmi vysoké hodnoty (300 %, 500 %) navíc fungují dobře i jako modelovací nástroj: oblasti pod štětcem rychle srovnají do roviny a vyhladí, jako když do hlíny bouchnete paličkou!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maska {#mask}
Tento nástroj umožňuje maskovat vrcholy. Maskované vrcholy jsou chráněné před modelováním i malováním. 

Vedlejší režim je `Odmaskovat` a maže masku tam, kde byla namalovaná.

Podobně jako výběry ve 2d malířských programech můžete masky malovat štětcem nebo je vytvářet výběrem tvarů (`Laso`, `Obdélník`, `Pás`...), rozmazávat je nebo zaostřovat. Štětec nebo tvar vyberete v okně tahů v levém panelu nástrojů, viz [Ovládání výběru](#selection-controls).

Na rozdíl od 2d malířských programů je můžete vytvářet i ze skupin ploch a z masek můžete vytvářet novou geometrii operacemi typu vytažení či extrakce. 

![](/videos/tool_mask1.mp4)

 V horní části výřezu se objeví panel nástrojů s dalšími ovládacími prvky. 

![](/images/tool_mask_toolbar.webp)

Klepnutím na název panelu ho rozbalíte nebo sbalíte, klepnutím na šipku vpravo nahoře ho přesunete do horní nebo dolní části rozhraní.

| Akce                                               | Popis                                                                                      |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Vymazat vše        | Vymaže masku na všech objektech. Když jsou maskované i jiné objekty, další tlačítko `Vymazat` vymaže jen vybrané objekty |
| ![](/icons/invert.webp)        Obrátit            | Obrátí masku                                                                               |
| ![](/icons/sharpen.webp)       Zaostřit           | Zaostří okraj masky                                                                        |
| ![](/icons/blur.webp)          Rozmazat           | Rozmaže okraj masky                                                                        |
| ![](/icons/outline.webp)       Okraj              | Zamaskuje otevřený okraj sítě, například okraj roviny nebo lem díry                        |
| ![](/icons/blur.webp)          Rozmazat ->        | Tažením doprava masku rozmažete, doleva zaostříte                                          |
| ![](/icons/circle_plus.webp)   Rozšířit ->        | Tažením doprava maskovanou oblast rozšíříte, doleva zmenšíte                               |
| ![](/icons/intensity.webp)     Zesílit ->         | Tažením doprava masku zesílíte, doleva zeslabíte, aniž by se změnil její tvar              |
| ![](/icons/dig.webp)           Dutina ->          | Znovu vytvoří masku podle zakřivení povrchu: tažením doprava zůstanou malovatelné jen dutiny, doleva jen hrboly |
| ![](/icons/culling.webp)       Přední             | Přepne maskování jen vrcholů natočených dopředu                                            |
| ![](/icons/eye_open.webp)      Viditelné         | U tvarů přepne ignorování vrcholů skrytých za jinými povrchy                               |
|                                 Převést            | Převede masku na skupinu ploch                                                             |
| ![](/icons/group_to_mask.webp) Na dotek (skupina ploch) | Když je zapnuto, zobrazí se skupiny ploch a klepnutím na skupinu ploch ji zamaskujete |
|                                 Na dotek (maska)   | Když je zapnuto, klepnutím na „ostrov" maskovaných nebo nemaskovaných polygonů ho celý vyplníte. |
| ![](/icons/connect.webp)       Připojené          | Když je zapnuto, tahy masky ovlivní jen propojenou topologii.                              |

##### Rychlé gesto masky {#mask-quick-gesture}
Když držíte tlačítko rychlého maskování v levém panelu nástrojů, můžete používat gesta ve stylu ZBrushe:
| Akce     | Gesto (držte zkratku vlevo dole)   |
| :------: | :--------------------------------: |
| Obrátit  | Klepnutí na pozadí                 |
| Vymazat  | Tažení po pozadí                   |
| Rozmazat | Klepnutí na maskovanou oblast      |
| Zaostřit | Klepnutí na nemaskovanou oblast    |


#### Nastavení masky {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Nastavení masky slouží hlavně k vytváření geometrie z masky. Záložky nahoře vybírají operaci: [Extrakt](#extract), [Rozděl](#split-mask) nebo [Ryt](#carve). Volby pod nimi se mění podle operace.

* `Náhled` - Při úpravách nastavení ukazuje, jak bude nová geometrie vypadat.
* `Rentgen` - Které objekty se během náhledu vykreslí rentgenově: `Žádné`, `Nevybrané`, `Vybrané` nebo `Vše`.

##### Extrakt {#extract}
* `Extrakt` - Vytvoří extrahovanou geometrii jako nový objekt.
* `Uzavírací akce` - Jak se extrahovaný tvar uzavře. `Žádné` zduplikuje maskované polygony do nového tvaru a nechá ho otevřený. `Vyplnit` udělá totéž, ale díru na zadní straně vyplní a vyhladí (nepoužívejte na plochých površích). `Kryt` uzavře tvar podle hodnoty `Výška` a je výchozí volbou.

::: tip

Pokud je zapnutý náhled s rentgenem, může být kliknutí na tlačítko Extrakt zpočátku matoucí. Protože je menu aktivní, Nomad se pokusí zobrazit náhled extrakce na vašem novém tvaru a původní povrch zobrazí rentgenově. Na novém povrchu ale žádnou masku nemáte, takže náhled extrakce zobrazit nejde a Nomad vás upozorní, že není co extrahovat. 

To je v pořádku. Zavřete menu nastavení masky, uvidíte nový tvar i původní, a pokud potřebujete masku vymazat nebo nakreslit novou, znovu vyberte původní povrch.
:::

##### Rozděl {#split-mask}
* `Rozděl` - Extrahuje maskovanou I nemaskovanou oblast do nových tvarů. 
* `Uzavírací akce` (maskované) - Jak se uzavře maskovaná část, se stejnými volbami `Žádné`, `Vyplnit` a `Kryt` jako u extraktu.
* `Uzavírací akce` (nemaskované) - Jak se uzavře nemaskovaná část, se stejnými volbami.

##### Ryt {#carve}
* `Ryt` - Chová se, jako byste do povrchu zařízli do hloubky `Výška`, podobně jako když vykrojíte kus pomerančové kůry. `Výška` nemůže být 0.

##### Výška {#thickness}
* `Výška` - Výška extrahovaného tvaru. Tlačítkem plus/minus přepínáte mezi vytažením ven, dovnitř nebo na obě strany. 

##### Hladkost {#smoothness}
Když je zapnutá, vyhladí extrahovaný tvar; lépe funguje při vyšším počtu polygonů. 
* `Vše` / `Pouze hranice` - Vyhladí celý tvar, nebo jen jeho okraje a horní plochu nechá být.
* `Iterace` - U volby `Vše` míra vyhlazení. Vysoké hodnoty dají velmi hladké zaoblené hrany, ale tvar se začne odchylovat od tvaru masky.
* `Stěna` - U volby `Pouze hranice` míra vyhlazení stěn. Jeho tlačítko přepíná mezi Uvolnit, které zachová ostré rohy, a Hladit, které je také zaoblí.
* `Vnitřek` - U volby `Pouze hranice` jak moc se srovná horní plocha. Jeho tlačítko přepíná mezi Uvolnit, které zachová vymodelované detaily a srovná jen směr vytažení (takže detaily přestanou vytvářet hroty), a Hladit, které vyhladí samotný povrch.

##### Boky {#edge-loop-side}
* `Rovné` - Obyčejné stěny po stranách extrahovaného tvaru.
* `Zkosení` - (jen Extrakt s volbou `Kryt`) Šikmý lem na přední hraně. `Zkosení` nastavuje jeho šířku v % výšky `Výška` nebo v jednotkách světa (přepíná se tlačítkem vedle), `Dělení zkosení` ho rozdělí (ve výchozím stavu `Auto`) a křivkou můžete tvarovat jeho profil.
* `Profil` - Tvaruje stěny profilovou křivkou, s parametrem `Šířka` v % výšky `Výška` nebo v jednotkách světa.
* `Maska` - Výška se řídí maskou: rozmazané části masky dostanou nižší výšku, takže vzniknou měkké tvary s proměnlivou výškou.
* `Dělení stěny` - Počet smyček hran po stranách. S volbou `Auto` zvolí Nomad takový počet dělení, aby vznikly čtvercové polygony odpovídající polygonům maskované oblasti.



### ![](/icons/tool_maskSelector.webp) Výběrová maska {#selection-mask}
Nástroj Výběrová maska (SelMask) je nyní součástí [nástroje Maska](#mask). Pokud chcete maskovat tvary místo tahu štětcem, vyberte tvar (`Laso`, `Polygon`, `Obdélník`...) v okně tahů nástroje Maska, viz [Ovládání výběru](#selection-controls).

Vedlejší režim `Odmaskovat` funguje i s tvary a maže masku uvnitř tvaru.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Malovat {#paint}
Nanáší barvu a vlastnosti materiálu. Více o materiálu se dozvíte v části [Malování](painting.md).

Vedlejší režim je `Vymazat` a barvu odstraňuje.

Kromě tahů štětcem umí Malovat také vyplňovat tvary (`Laso`, `Obdélník`, `Pás`...), viz [Ovládání výběru](#selection-controls).

#### Nastavení malování {#paint-settings}
* `Filtrovat vrstvu` - Funguje jako zámek průhlednosti vrstvy ve Photoshopu nebo Procreate. Když malujete na vrstvu a tato volba je zapnutá, můžete měnit jen místa, kde už barva je; nenamalované oblasti jsou chráněné. Je dostupná jen tehdy, když je vybraná vrstva.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Rozmazat {#smudge}
Rozmazává barvu a vlastnosti materiálu. Menu nastavení obsahuje posuvník `Kvalita`, nižší hodnoty znamenají rychlejší tahy.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Zploštit {#flatten}
Zplošťuje oblast promítnutím bodů na průměrnou rovinu.

Vedlejší režim je `Vyplnit`: rovinu určí nejvyšší bod a body mají tendenci se zvedat.

#### Nastavení zploštění {#flatten-settings}

* `Zamknout směr roviny` - Použije směr roviny vypočtený při prvním klepnutí. Ve výchozím stavu je vypnuto.
* `Zamknout počátek roviny`- Použije první klepnutí jako střed roviny. Ve výchozím stavu je vypnuto a zapnout se dá jen spolu s volbou `Zamknout směr roviny`.

Když je jedna nebo obě volby vypnuté, můžete zploštění postupně prohlubovat nebo měnit úhel roviny dlouhými tahy přes místa s různou hloubkou a zakřivením. Spolu s volbami vzorkování oblasti v menu štětce to dává velmi přesnou kontrolu.

::: tip
Když pracujete v oblastech s velkým zakřivením, například chcete zploštit tváře, ale nástroj stále zasahuje boky nosu, zkuste vytvořit masku, která ochrání místa, na která štětec Zploštit nemá sahat.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Srovná body do roviny promítnutím na průměrnou rovinu, ale s menším nabalováním než štětec Zploštit. Vznikají tak čistší povrchy s ostrými hranami. Rychlé tahy povrch víc tlačí a táhnou, pomalejší tahy, které začínají v už rovných oblastech a pokračují ven, rovinu lépe udrží.

Vedlejší režim je `Vyplnit`: rovinu určí nejvyšší bod a body mají tendenci se zvedat.

Planar je ve skutečnosti stejný nástroj jako `Zploštit`, jen se zapnutou volbou `Zamknout směr roviny`. Vytváří proto stabilnější povrchy s ostrými hranami, zatímco Zploštit je víc sochařský a hodí se na polorovné oblasti.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Leštění {#polish}
Další člen rodiny Zploštit, nastavený tak, aby vyleštil povrchy do čistých rovin. Je to stejný nástroj jako `Zploštit`, jen s jinými výchozími hodnotami v menu [Tah](stroke.md): zapnuté jsou `Stopa za tahem`, `Filtr normál podle oblasti` a `Maskování hloubky`.

Vedlejší režim je `Vyplnit`, stejně jako u Zploštit.

Leštění má stejná nastavení jako [Zploštit](#flatten-settings): `Zamknout směr roviny` a `Zamknout počátek roviny`.

### ![](/icons/tool_crease.webp) Rýha {#crease}
Nástroj Rýha se hodí k modelování drobných zářezů a prohlubní.

Vedlejší režim je `Obrátit` a vytvoří vystouplou rýhu.

#### Nastavení rýhy {#crease-settings}

* `Faktor sevření` - Jak moc se vrcholy stahují do stran ke štětci. Když je sevření 1 a posunutí 0, hloubka povrchu se nezmění, změní se jen topologie: hrany se stáhnou k tahu.
* `Faktor posunutí` - Jak moc se vrcholy tlačí či táhnou do hloubky. Když je sevření 0 a posunutí 1, vzniknou hluboké rýhy nebo vystouplé hřbety, ale budou zubaté, protože se k rýze nestáhne dost geometrie, aby přesně definovala její boky nebo dno.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Štípnout {#pinch}
Tento nástroj můžete použít ke zostření hran.

Vedlejší režim je `Obrátit` a vrcholy roztahuje od sebe.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Oříznout {#trim}
Nástroj Oříznout odstraní kus sítě a nabízí volby, jak naložit s mezerou, která po něm zůstane. Oblast ořezu určíte pomocí [Ovládání výběru](#selection-controls).

Vedlejší režim je `Převrátit` a obrátí tvar, takže se odstraní druhá strana.

::: tip
Protože tento nástroj promítá z kamery, dostanete upozornění, pokud je kamera v perspektivním režimu.

V ortografickém režimu je řez sítí rovnoběžný s pohledem, což obvykle čekáte. S perspektivní kamerou bude řez na vzdálenější straně objektu vypadat jinak než na bližší.
:::

#### Nastavení ořezu {#trim-settings}

Nastavení jsou seskupená pod `Plnění otvoru`:

* `Tahové malování` - Pokud je v menu malování zapnuté malování, vyplněná oblast dostane aktuálně vybranou barvu.
* `Bool` - Vyplní díru po ořezu oblastí ze čtyřúhelníků. Vyplněná oblast bude rovná.
* `Legacy` - Vyplní díru po ořezu trojúhelníkovou oblastí. Vyplněná oblast bude rovná.
* `Vyplnit` - Vyplní díru trojúhelníkovou oblastí. Vyplněná oblast bude zakřivená, jako blána mýdlové bubliny.
* `Žádný` - Díru nevyplní.

S volbou `Bool` obsahuje část `Detail`:

* `Tvar` - Přibližná velikost čtyřúhelníků a trojúhelníků na straně tvaru.
* `Otvory` - Přibližná velikost trojúhelníků či polygonů ve vyplněné díře. Tlačítko řetězu vedle `Detail` ji udržuje v souladu s hodnotou `Tvar`; zrušte propojení, pokud ji chcete nastavit samostatně.
* `Zachovat topologii` - Nevyhlazuje a nezjednodušuje okraj řezu, takže u maskovaných a skrytých ploch zůstane původní topologie sítě.

S volbou `Legacy`:

* `Detail` - Přibližná velikost trojúhelníků použitých při ořezu.
* `Vyhlazení otvorů` - Jak moc se trojúhelníky ve vyplněné oblasti uvolní.
* `Epsilon prahu` - Hodnota, kterou můžete upravit pro zlepšení starého algoritmu vyplňování děr.

S volbou `Vyplnit`:

* `Detail` - Přibližná velikost trojúhelníků použitých při ořezu.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Rozdělit {#split}
Podobný nástroji [Oříznout](#trim), jen s tím rozdílem, že zatímco Oříznout výběr zahodí, Rozdělit ho zachová jako nový objekt.

Vedlejší režim je `Dělit`: každý kus se zachová jako samostatný objekt, takže překrývající se tvary (například se symetrií) se rozříznou na samostatné části, místo aby se spojily do jedné.

#### Nastavení rozdělení {#split-settings}

Rozdělit má stejná nastavení `Plnění otvoru` jako [Oříznout](#trim-settings): `Tahové malování`, metody `Bool`, `Legacy`, `Vyplnit` a `Žádný` a jejich volby `Detail`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projekt {#project}
Nástroj Projekt vypadá jako nástroj [Oříznout](#trim), ale geometrii nemaže ani nevytváří, jen posouvá vrcholy tak, aby odpovídaly výběru.

![](/videos/tool_project.mp4)

::: tip
Když Projekt použijete na vrstvě, můžete posuvníkem vrstvy prolínat mezi původním a promítnutým tvarem.
:::

### ![](/icons/tool_layer.webp) Vrstva {#layer}
Zvedá povrch, ale omezuje výšku.

Když necháte stylus na displeji a přejíždíte stále po stejném místě, Vrstva povrch zvedne do určité výšky a dál už ne, zatímco jiné nástroje výšku stále nabalují.

Pozor, ve výchozím stavu platí limit jen pro jeden tah! Když začnete nový tah, bude se stavět od nové výšky povrchu.

Pokud chcete stálou maximální výšku přes mnoho tahů, použijte nástroj Vrstva spolu se systémem [Vrstvy](layers.md) v Nomadu.

Vytvořte vrstvu a použijte tento nástroj. Maximální výška se teď určuje podle vrstvy, takže můžete udělat mnoho tahů a výška zůstane vždy stejná.

`Méně` použije minimální hloubku a vytváří drážky.

#### Nastavení nástroje Vrstva {#layer-settings}

* `Použít data vrstvy` - Když je zapnuto a je vybraná vrstva, maximální výška se určí podle dat vrstvy. Když žádná vrstva vybraná není, připomene vám to upozornění.
* `Zvětšit`- Když je zapnuto, upraví směr, kterým nástroj Vrstva působí, pro hladší výsledky.
* `Uvolnit (Normála)` - Se zapnutou volbou `Zvětšit` míra vyhlazení normál.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Zvětšit {#inflate}
Posouvá vrcholy podél jejich vlastních normál. `Méně` je posouvá podél obrácených normál.

#### Nastavení nástroje Zvětšit {#inflate-setings}
* `Uvolnit (Normála)` - Míra vyhlazení normál.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Posunout {#nudge}
Posouvá neboli „roztírá" body ve směru tahu.

Vedlejší režim je `Záhyb` a tlačí před sebou záhyb hmoty podél tahu: před štětcem vzniká vyboulení, za ním prohlubeň.

#### Nastavení nástroje Posunout {#nudge-settings}
* `Hladit` - Jak moc se oblast pod štětcem během posouvání vyhlazuje, aby roztíraný povrch zůstal čistý.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Razítko {#stamp}

Klepnutím a tažením zvednete oblast sochy do tvaru vybrané alfy.

Je to jednoduše [nástroj Štětec](#brush) s typem tahu nastaveným na `Zámek + poloměr`. 

`Méně` razítko do povrchu vtlačí, místo aby ho z povrchu vytáhlo.

::: tip
Razítko obvykle funguje nejlépe s geometrií ve vysokém rozlišení. Když na internetu vyhledáte „wrinkles alpha", „pores alpha", „scales alpha" atd., najdete alfa textury, se kterými je Razítko skvělý způsob, jak přidat postavě organické detaily.

Oba režimy tahu se hodí na něco jiného. 

* `Zámek + poloměr` má pevnou *výšku*, tažením měníte šířku a natočení razítka. Hodí se na texturu kůže, kde potřebujete stejnou hloubku/výšku, ale různé natočení a velikost, aby se skryly opakující se vzory.
* `Zámek + intenzita` má pevnou *šířku*, tažením měníte natočení a výšku razítka. Hodí se na nýty, které musí mít všechny stejnou velikost, ale různé natočení a výšku. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Otiskne mapu vektorového posunutí (VDM). Na rozdíl od alfy, která umí povrch jen zvednout nebo stlačit, ukládá VDM celý 3d tvar, takže dokáže otisknout i převisy, jako jsou uši, rohy nebo stočené listy. Funguje jako [Razítko](#stamp), se stejnými režimy tahu `Zámek + poloměr` a `Zámek + intenzita`.

`Méně` (`Obrátit`) obrátí hloubku razítka, takže ho vtlačí do povrchu jako formu.

Samotné VDM vybíráte v menu [Alfa](stroke.md#alpha), kde je také posuvník `Výška`, který mění jen výšku razítka a boční posunutí nechá beze změny.

Tlačítkem `Vytvořit` v levém panelu nástrojů si můžete vyrobit vlastní razítka:

* `Nový VDM...` - Přidá rovinu připravenou pro modelování VDM. Vymodelujte na ní svůj tvar a pak ho vypečte přes `Topologie -> Péct -> VDM`: Nomad přidá nové razítko do knihovny VDM a vybere ho.
* `Zachytit VDM` - (Experimentální) Tažením po povrchu modelu zachytíte danou oblast a uděláte z ní razítko VDM. `Tolerance` plynule zploští okraj zachyceného tvaru.

::: tip
Při modelování na rovině VDM se vyhněte DynTopo, poškozuje UV roviny a zkresluje razítko. Držte se se sochou také dál od okraje roviny, jinak bude mít razítko ostrou hranu.
:::


### ![](/icons/tool_clearLayer.webp) Smazat vrstvu {#delete-layer}
Tento nástroj umí lokálně resetovat vrstvy; potřebujete aktivní vrstvu, jinak se nic nestane. Maže vymodelovaná data vrstvy a při zapnutém malování i její barvu.

Vedlejší režim je `Obrátit` a vrstvu místo mazání mírně zesílí.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Trubka {#tube}
Vytvoří trubku nakreslením křivky. 
![](/images/tool_tube_new.webp)

Jakmile je trubka vytvořená, můžete její dráhu upravovat ve 3d prostoru podobným ovládáním jako u standardní [Úpravy tvaru](#shape-editing) a nástrojů pro úpravu křivek. 

![](/videos/tool_tube.mp4)

#### Levý panel nástrojů trubky {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Levý panel nástrojů nabízí tyto volby:

* `Synchronizovat` - Pokud je aktuální trubka instancovaná a některé podřízené uzly trubky se mezi instancemi liší, tímto je znovu sesynchronizujete.
* `Zachycení` - Když je zapnuto, režimy křivka a cesta se při kreslení přichytávají k jiným objektům. Když je vypnuto, přichytí se jen první bod a zbytek trubky se nakreslí v této hloubce.
* `Posunutí` - Nastavuje hloubku přichycení; při 0 % se k povrchu přichytí střed průřezu trubky, kladné hodnoty ji od povrchu zvednou, záporné ji sníží. 100 % odpovídá poloměru trubky.
* `Zobrazit` - Bez kreslení, takže můžete volně pohybovat kamerou.
* `Křivka` - Volné kreslení trubky od ruky. Má malé rozbalovací menu:
    * `Upravit` - Co se stane, když tah dokončíte, viz [Ovládání výběru](#selection-controls): trubka se hned vytvoří, křivka zůstane upravitelná se zeleným potvrzovacím kolečkem vedle, nebo `Úprava: podržet`, kdy na konci tahu podržíte prst a můžete dál upravovat.
    * `Uzavřeno` - Udělá z trubky smyčku.
    * `Kreslit dál` - Po potvrzení trubky zůstanete v nástroji a můžete kreslit další.
    * `Přesnost` - Kolik bodů křivky se použije k převodu nakreslené dráhy na trubku. 0 % použije nejmenší počet bodů, ale nezachytí drobné změny zakřivení dráhy. 100 % bude velmi přesné a použije mnoho bodů.
* `Cesta` - Vytvoří trubku klepáním, kterým určujete body křivky. Cestu potvrdíte klepnutím na zelené kolečko. Má malé rozbalovací menu:
    * `B-splajn` - Alternativní způsob kreslení křivky, při kterém body obvykle neleží přímo na křivce, ale výsledek může být hladší než u výchozí metody.
    * `Uzavřeno` - Udělá z trubky smyčku
    * `Obrazovka` - Když je zapnuto, cesta je „připnutá" k obrazovce, takže můžete pohybovat pohledem i objektem a cesta zůstane na místě. Když je vypnuto, cesta je součástí 3d scény a pohybuje se s kamerou a objekty.
* `Průřez` - Z křivky se stane prstenec kolem tvaru, proříznutý přes její dva body ve směru, ze kterého jste se dívali.

##### Horní panel nástrojů trubky {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Když je vybraná trubka, objeví se v horní části výřezu panel nástrojů s dalšími ovládacími prvky. Klepnutím na název panelu ho sbalíte nebo rozbalíte, klepnutím na šipku vpravo nahoře ho přesunete do horní nebo dolní části výřezu.

* `Dokončit` - Převede trubku na běžné polygony, aby se dala modelovat.
* `Upravit` - Zobrazí body křivky, abyste s nimi mohli pracovat
* `Zrcadlo` - Přidá zrcadlový opakovač jako rodiče této křivky
* `Zachycení` - Přichytí body křivky k blízkým povrchům
* `Uzavřeno` - Spojí začátek a konec křivky do smyčky
* `B-splajn` - Přepíná mezi interpolací Catmull-Rom a B-splajn.
* `Víčko` - Přepíná mezi víčky na obou koncích trubky, jen na začátku nebo na konci, nebo bez víček.
* `Díra` - Dodá trubce tloušťku a udělá z ní rouru. Přepíná mezi dírou na obou koncích, jen na konci, nebo bez děr. 
* `Poloměr` - Přepíná mezi jednotným poloměrem, poloměrem na začátku a na konci, nebo poloměrem pro každý bod křivky. Upravují se oranžovými úchyty na křivce.
* `Vinutí` - Přepíná mezi žádným vinutím, jednotným vinutím, vinutím na začátku a na konci, nebo vinutím pro každý bod křivky. Upravují se růžovými úchyty na křivce.
* `Profil` - Přepíná mezi žádným profilem (tedy kruhovým), jednotným profilem, profilem na začátku a na konci, nebo profilem pro každý bod.
* `Úprava profilu` - Zobrazí editor profilu. Funguje podobně jako nástroje [Úpravy tvaru](#shape-editing), umí ukládat a načítat předvolby profilů a má přepínač, kterým můžete profil upravovat ve 3d prostoru.
* `Spirála` - Zobrazí menu pro přidání spirálového vinutí trubky. Menu obsahuje volby `Úhel vinutí`, `Posunutí`, `Míra` a `Posun úhlu`.
* `Dělení X` - Počet dělení po obvodu trubky, například 4 dělení vytvoří čtvercovou trubku. 
* `Konstantní hustota` - Když je zapnuto, polygony zůstanou čtvercové. Když je vypnuto, můžete nastavit `Dělení Y` po délce trubky.
* `...` - Menu nastavení trubky.

#### Přepínač mazání bodů křivky {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Pod panelem nástrojů je přepínač mazání bodů křivky. Když přetáhnete bod křivky blízko k jinému, zčervená, což znamená, že po puštění se bod smaže. Pokud děláte drobné úpravy a nechcete body mazat, tímto tlačítkem mazání bodů vypnete.



#### Nastavení trubky {#tube-settings}
* `Primitivum` - Tlačítka pro zapnutí/vypnutí UV nebo pro dokončení trubky.
* `Post-pododdíl` - Zkratka pro nastavení úrovně multirezoluce před dokončením.
* `Lineární poddělení` - Zkratka pro nastavení úrovně lineárního poddělení před dokončením. 
* `Dělení X` - Totéž co Dělení X v panelu nástrojů.
* `Dělení Y` - Totéž co Dělení Y v panelu nástrojů.
* `Křivka (Opakovač)` - Převede trubku na [křivkový opakovač](scene.md#curve)

::: tip
Dělení 4 a Post-pododdíl 3 vytvoří hladké trubky se zaoblenými konci, vhodné na červy, hady a části těla.
:::


### ![](/icons/tool_lathe.webp) Soustruh {#lathe}
Vytvoří rotační plochu nakreslením křivky.

Tento nástroj je skvělý na tvary jako vázy nebo sklenice na víno.

![](/videos/tool_lathe.mp4)

#### Levý panel nástrojů soustruhu {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Levý panel nástrojů nabízí tyto volby:

* `Synchronizovat` - Pokud je aktuální soustruh instancovaný a některé podřízené uzly soustruhu se mezi instancemi liší, tímto je znovu sesynchronizujete.
* `Pevná` - Když je zapnuto, střed soustruhu je pevný a zobrazený na obrazovce. Tato středová osa má body, které můžete upravovat. Když je vypnuto, střed soustruhu se dynamicky přizpůsobuje začátku a konci nakreslené křivky.
* `Zobrazit` - Bez kreslení, takže můžete volně pohybovat kamerou.
* `Křivka` - Nakreslí profil soustruhu jedním tahem. Má malé rozbalovací menu:
    * `Upravit` - Co se stane, když zvednete stylus, viz [Ovládání výběru](#selection-controls): soustruh se hned vytvoří, křivka zůstane upravitelná se zeleným kolečkem vedle pro vytvoření soustruhu, nebo `Úprava: podržet`, kdy na konci tahu podržíte prst a můžete dál upravovat.
    * `Uzavřeno` - Spojí začátek a konec křivky do smyčky
    * `Kreslit dál` - Po potvrzení soustruhu zůstanete v nástroji a můžete kreslit další.
    * `Přesnost` - Kolik bodů křivky se použije k převodu nakreslené dráhy na trubku. 0 % použije nejmenší počet bodů, ale nezachytí drobné změny zakřivení dráhy. 100 % bude velmi přesné a použije mnoho bodů.
* `Cesta` - Vytvoří soustruh klepáním, kterým určujete body křivky. Cestu potvrdíte klepnutím na zelené kolečko. Má malé rozbalovací menu:
    * `B-splajn` - Alternativní způsob kreslení křivky, při kterém body obvykle neleží přímo na křivce, ale výsledek může být hladší než u výchozí metody.
    * `Uzavřeno` - Udělá z trubky smyčku
    * `Obrazovka` - Když je zapnuto, cesta je „připnutá" k obrazovce, takže můžete pohybovat pohledem i objektem a cesta zůstane na místě. Když je vypnuto, cesta je součástí 3d scény a pohybuje se s kamerou a objekty.

#### Horní panel nástrojů soustruhu {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Když je vybraný soustruh, objeví se v horní části výřezu panel nástrojů s dalšími ovládacími prvky. Klepnutím na název panelu ho sbalíte nebo rozbalíte, klepnutím na šipku vpravo nahoře ho přesunete do horní nebo dolní části výřezu.

* `Dokončit` - Převede soustruh na běžné polygony, aby se dal modelovat.
* `Upravit` - Zobrazí body křivky, abyste s nimi mohli pracovat
* `Zrcadlo` - Přidá zrcadlový opakovač jako rodiče tohoto soustruhu
* `Zachycení` - Přichytí body křivky k blízkým povrchům
* `Stabilní` - Když je zapnuto, profil křivky je podřízený středové ose soustruhu. Když je vypnuto, můžete středovou osu upravovat, aniž by se křivka pohnula, což umožňuje složitější tvary.
* `Ostření` - Natočí pohled tak, aby profil křivky ležel dokonale rovně proti kameře.
* `Uzavřeno` - Spojí začátek a konec křivky do smyčky
* `Víčko` - Když je Uzavřeno vypnuté, přepíná mezi víčky na obou koncích, jen na začátku nebo na konci, nebo bez víček.
* `Díra` - Dodá soustruhu tloušťku a udělá z něj rouru. Přepíná mezi dírou na obou koncích, jen na konci, nebo bez děr. 
* `B-splajn` - Přepíná mezi interpolací Catmull-Rom a B-splajn.
* `Dělení X` - Počet dělení po obvodu soustruhu, například 4 dělení vytvoří soustruh se čtvercovým profilem. 
* `Konstantní hustota` - Když je zapnuto, polygony zůstanou čtvercové. Když je vypnuto, můžete nastavit `Dělení Y` po délce trubky.
* `...` - Menu nastavení soustruhu.

#### Nastavení soustruhu {#lathe-settings}
* `Primitivum` - Tlačítka pro zapnutí/vypnutí UV nebo pro dokončení trubky.
* `Post-pododdíl` - Zkratka pro nastavení úrovně multirezoluce před dokončením.
* `Lineární poddělení` - Zkratka pro nastavení úrovně lineárního poddělení před dokončením. 
* `Dělení X` - Totéž co Dělení X v panelu nástrojů.
* `Dělení Y` - Totéž co Dělení Y v panelu nástrojů.
* `Křivka (Opakovač)` - Převede profil křivky na [křivkový opakovač](scene.md#curve)

### ![](/icons/tool_insert.webp) Vložit {#insert}
Umístí objekt na povrch jiného objektu. Používá se podobně jako Razítko, ale pro plné 3d tvary.

Když v levém panelu nástrojů vyberete primitivum, klepnutím a tažením na libovolném povrchu umístíte primitivum na místo klepnutí a tažením určíte jeho velikost. Jakmile tažení dokončíte, Vložit se přepne do režimu [Přeměnit](#transform).

V režimu Instance vytvoří tažení novou instanci a posouvá ji po povrchu. Velikost se převezme z prvního tvaru, takže můžete po jiných površích rozmístit mnoho stejně velkých instancí objektu.

Nemusíte vkládat jen primitiva! Vyberte v seznamu objektů *jakýkoli* tvar, a pokud je Vložit v režimu Instance nebo Klonovat, můžete kopie vybraného objektu přetahovat po libovolném jiném povrchu.

Pokud má objekt vlastní pivot, použije se jako kotevní bod. Viz video níže.

Levý panel nástrojů má také `Zobrazit`, kterým pohnete kamerou, aniž byste cokoli vložili, a `Synchronizovat`: když je cílový objekt instancovaný, nový objekt se přidá i na všechny ostatní instance.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Přeměnit {#transform}
Přesouvá, otáčí a mění velikost modelu přímo jedním a dvěma prsty, obvykle po povrchu jiného objektu.

Levý panel nástrojů má tato tlačítka:

* `Klonovat` / `Instance` - Vytvoří kopii nebo instanci objektu, viz panel nástrojů [Gizmo](#left-menu-toolbar).
* `Přesunout` - Tažením jedním prstem objekt přesunete. Když je zapnuté přichycení, objekt klouže po povrchu pod vaším prstem.
* `Otočit` - Tažením jedním prstem objekt otočíte. Když je zapnuté přichycení, otáčí se kolem normály povrchu pod vaším prstem.
* `Škála` - Tažením jedním prstem změníte velikost objektu.

Panel nástrojů v horní části výřezu obsahuje:

* `Cíl` - Zda nástroj pohybuje objektem, jeho skupinou, nebo jeho vrcholy, stejně jako u [Gizma](#left-menu-toolbar).
* `Přichytit` - Přichytí model k jiným povrchům.
* `Povrch` / `Vrchol` - Se zapnutým `Přichytit` se přichytí k povrchu, nebo k nejbližšímu vrcholu.

Pomocí dvou prstů můžete v nástroji Přeměnit rychle používat dva z těchto režimů:

* Tažením umístěte objekt. Prvním prstem přestaňte hýbat, ale nezvedejte ho z obrazovky.
* Dokud držíte první prst, dotkněte se obrazovky druhým prstem. Tažením druhého prstu měníte velikost objektu.
* Zvedněte druhý prst a pokračujte v tažení prvním prstem, objekt je opět v režimu přesunu.

Druhý režim můžete také změnit klepnutím druhým prstem:

* Tažením umístěte objekt, přestaňte hýbat, ale nezvedejte prst z obrazovky.
* Dokud držíte první prst, klepněte druhým prstem
* Nástroj se přepne do režimu otáčení. Tažením prvního prstu nastavíte natočení.
* Klepněte druhým prstem jako předtím a nástroj se přepne zpět do režimu přesunu.

Je to rychlý postup pro klonování objektů po jiném objektu, například kamenů po krajině. Všimněte si, že tlačítko klonování je pro snadný přístup také v levém panelu nástrojů:

* Nástrojem Přeměnit přesuňte kámen na místo.
* Pusťte a stiskněte tlačítko klonování
* Přesuňte tento kámen, podle potřeby ho otočte či změňte velikost
* Pusťte a stiskněte tlačítko klonování
* Přesuňte tento kámen a opakujte.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Tento nástroj umožňuje přesouvat, otáčet a měnit velikost objektů a upravovat jejich pivoty.

Úchyt ve výřezu nabízí tyto funkce:

* `Přesunout` - Tažením za čáru se šipkou posouváte v ose X/Y/Z. Tažením za broskvovou tečku uprostřed gizma posouváte volně v prostoru obrazovky. Tažením za červený, zelený či modrý čtverec posouváte v rovinách X/Y/Z.
* `Otočit` - Tažením za červený/zelený/modrý kruh otáčíte kolem os X/Y/Z. Tažením za kouli uvnitř kruhů otáčíte volně.
* `Škála`- Tažením za vnější červené/zelené/modré tečky měníte velikost v osách X/Y/Z. Tažením za vnější červené/zelené/modré kužely měníte velikost v rovinách X/Y/Z. Tažením za vnější broskvový kruh měníte velikost rovnoměrně.

![](/images/tool_gizmo.webp)

#### Uzly a vrcholy {#nodes-and-vertices}

Každý objekt v Nomadu se skládá z uzlu a vrcholů:

* `Uzel` - „Držadlo" objektu, které uchovává jeho posun, natočení a měřítko, tzv. transformační matici.
* `Vrcholy` - Body, které definují povrch objektu; uchovávají polohu a informace o barvě.

Máte-li jednoduchou krychli z 8 vrcholů, můžete ji posunout změnou její transformační matice, nebo změnou poloh vrcholů. Při modelování obvykle chcete měnit vrcholy, při přesouvání objektů gizmem obvykle chcete měnit uzel. Nomad umí obojí. 

#### Panely nástrojů gizma {#left-menu-toolbar}

Levý panel nástrojů obsahuje:

* `Klonovat` - Vytvoří samostatnou kopii aktuálního objektu, kterou můžete gizmem odtáhnout.
* `Instance` - Vytvoří instanci aktuálního objektu. Objekty jsou propojené, takže změny modelování na jednom objektu se projeví na všech instancích.
* `Pivot` - (Ikona zámku místo tlačítka `Méně`) Když je zapnuto, můžete gizmo přesouvat a otáčet, aniž by se pohnul objekt. Stejně jako `Méně` ho podržte pro rychlou změnu, nebo na něj klepněte, aby zůstal zapnutý.

Panel nástrojů v horní části výřezu obsahuje ostatní ovládací prvky:

* `Cíl` - Určuje, zda gizmo ovlivní uzel, nebo vrcholy objektu:
    * `Automaticky` - Výchozí volba, funguje jako `Skupina`, ale pokud má síť masku nebo je zapnutá symetrie, funguje jako `Vrchol`.
    * `Vrchol` - Použije transformaci na vrcholy a zohlední masku i symetrii. Nefunguje na nedokončená primitiva a ovlivní i instance.
    * `Objekt` - Přesune jen aktuální objekt a ignoruje symetrii i masku. Podřízené objekty zůstanou na místě.
    * `Skupina` - Přesune objekt i zbytek jeho hierarchie a ignoruje symetrii i masku.
    * `Instance` - (Objekt a Skupina) Totéž, ale s objektem se pohybují i všechny jeho instance.
* `Pivot` - Okno pro rychlé umístění pivotu, popsané [níže](#pivot).
* `Vše` / `Přesunout` / `Otočit` / `Měřítko` - Zobrazí všechny úchyty gizma, nebo jen úchyty pro přesun, otáčení či změnu měřítka.
* `Připnout` - Ve výchozím stavu se gizmo přesune na pivot vybraného objektu. Když je připnutí zapnuté, gizmo zůstane tam, kde právě je.
* `Zarovnat` - Přepíná, zda je pivot zarovnaný s aktuálním objektem, nebo se světem.
* `Přichytit` (otáčení) - Zapne přichytávání hodnot natočení k krokům; hodnota kroku se zobrazí a dá se upravit, když je přichycení zapnuté. Jeho volba `Magnet` způsobí, že se natočení při přechodu přes krok na chvíli „přilepí" a pak se zase volně pohybuje; vypněte ji, pokud chcete skákat z kroku na krok.
* `Přichytit` (posun) - Zapne přichytávání hodnot posunu k krokům; hodnota kroku se zobrazí a dá se upravit, když je přichycení zapnuté.

#### ![](/icons/reset.webp) Pivot {#pivot}
Okno `Pivot` v horním panelu nástrojů umožňuje rychle měnit pivot. Poloha a orientace pivotu určují gizmo.

**Obnovit** 
* `Auto` - Střed objektu, zarovnaný s jeho transformací.
* `Střed` - Přesune pivot do středu objektu a zachová jeho orientaci.
* `Dole` - Přesune pivot doprostřed spodní části objektu. Dalším klepnutím použijete místo toho ohraničující kvádr ve světě.
* `Nahoře` - Přesune pivot doprostřed horní části objektu. Dalším klepnutím použijete místo toho ohraničující kvádr ve světě.
* `Objekt` - Přesune pivot do počátku objektu, zarovnaný s jeho transformací.
* `Maska` - Přesune pivot do středu nemaskované oblasti. Dalším klepnutím přepnete na maskovanou oblast.
* `Zarovnat` - Vynuluje natočení tak, aby bylo zarovnané se světem, a zachová polohu.
* `Pohled` - Zarovná pivot s aktuálním pohledem a zachová polohu. Kameru pak už nesleduje.

**Při klepnutí (režim Pivot)**

Aktivní jen se zapnutým `Pivot`, určuje, co se stane, když jednou klepnete na povrch sítě:
* `Žádný` - Po klepnutí na objekt se nic nestane
* `Normála` - Přesune a natočí pivot tak, aby byl zarovnaný s místem klepnutí na povrch
* `První` - Přesune (ale neotočí) pivot na místo klepnutí na povrch
* `Medián` - Přesune pivot doprostřed objektu, pod místo klepnutí na povrch.

#### Nastavení gizma {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Kompaktní` - Přepíná rozvržení gizma: další úchyty jsou vně, nebo uvnitř koule otáčení
* `Velikost gizma` - Velikost gizma
* `Tloušťka` - Tloušťka čar gizma
* `Krytí` - Krytí gizma
* `Skrýt při interakci` - Přepíná, zda se gizmo při tažení dočasně skryje

-----

* `Práh sklopení tangenty` - Určuje, jak se chová otáčení při tažení za kruhové úchyty pro rotaci kolem os X/Y/Z. Při hodnotě 0 funguje otáčení jako otočný ovladač: táhnete gizmem v kruzích. Při hodnotě 90 funguje jako tahání za provázek jojo: táhnete v přímce k místu prvního klepnutí, nebo od něj. Hodnoty mezi 0 a 90 kombinují obojí; pod hodnotou bude pohyb přímý, nad ní kruhový.
* `Číselný vstup` - Když je zapnuto, jedno klepnutí na gizmo otevře okno, kam můžete zadat přesnou hodnotu pro osu, na kterou jste klepli.

::: warning
Nástroje [Gizmo](#gizmo) a [Přeměnit](#transform) mají vlastní zaškrtávací políčko symetrie, oddělené od symetrie pro modelování!

Ve výchozím stavu je tato symetrie vypnutá.
:::

##### Matice {#matrix}
Přesné hodnoty transformace objektu už nejsou v nastavení gizma: přesunuly se do menu `Přeměnit` v pravém horním menu. Jeho část `Matice` obsahuje:

* ![](/icons/target.webp) `Přesunout počátek` - Přesune objekt tak, aby jeho pivot byl ve středu scény, tzv. počátku.
* ![](/icons/bake.webp)  `Vypéct` - Zafixuje objekt tam, kde právě je, a nastaví hodnoty posunu a natočení na 0 a měřítko na 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pivot` - Vypeče pivot: hodnoty matice budou odpovídat tomu, kde je úchyt gizma ve světě.
* ![](/icons/reset.webp) `Resetovat` - Zkratka, která nastaví hodnoty posunu na 0, natočení na 0 a měřítko na 1, takže objekt přesune a otočí.

::: tip Vypéct vs. vypéct do pivotu
Vytvořte krychli, vyberte nástroj Gizmo a otevřete a připněte menu `Přeměnit`. Ve výchozím stavu jsou posun a natočení 0 a měřítko 1.

Zapněte režim pivotu, posuňte úchyt na jednu stranu a režim pivotu vypněte. Pivot se změnil, ale všimněte si, že hodnoty posunu jsou stále 0. 

Pokud chcete vidět, kde pivot *skutečně* je, klepněte na tlačítko vypečení `Pivot`. Teď se hodnoty posunu aktualizují. Všimněte si, že se krychle při této operaci nepohne, stejně jako v režimu pivotu.

Krychli někam přesuňte a otočte, pak klepněte na `Přesunout počátek`. Objekt se přesune tak, aby jeho pivot byl ve středu světa, ale natočení zůstane beze změny.

Klepněte na `Resetovat` a na 0 se nastaví i natočení.

Krychli znovu přesuňte a otočte, tentokrát klepněte na `Vypéct`. Pivot zůstane, kde je, krychle zůstane, kde je, ale hodnoty posunu a natočení se nastaví na 0.

Vyzkoušejte si to několikrát! Pochopte, že hodnoty pivotu jsou skryté a Nomad se o ně stará za vás, ale pokud potřebujete nastavit pivot do skutečného místa v prostoru, udělá to za vás vypečení pivotu.

:::

* `Posun` - Hodnoty posunu X, Y, Z
* `Rotace` - Hodnoty natočení X, Y, Z
* `Měřítko` - Jednotné měřítko, pokud je zapnuté, nebo měřítko X, Y, Z, pokud je vypnuté.
* `Klopení` - Hodnoty zkosení X, Y, Z, zobrazují se jen tehdy, když už je objekt zkosený
* `Jednotné měřítko` - Přepíná mezi rovnoměrnou změnou měřítka a samostatnou změnou v každé ose

Vlevo můžete posouvat pivot gizma, jak to funguje, uvidíte ve videu níže.
To se hodí hlavně pro otáčení, protože na posun to nemá žádný vliv.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Skupina ploch {#facegroup}

Skupiny ploch vám umožňují rozdělit objekt na různě obarvené plochy. V Nomadu je můžete využít mnoha způsoby:

* Rychlý způsob výběru pro masky
* Skrývání a zobrazování částí objektu
* Uspořádání objektu, aniž byste ho museli rozdělit na samostatné části
* Určení oblastí UV
* Řízení Quad Remesheru
* Další ovládání pro nástroje jako Hladit.

#### Levý panel nástrojů skupiny ploch {#facegroup-left-toolbar}

* `Skupina` - Tlačítko ukazuje aktuální skupinu ploch. Klepnutím na něj zobrazíte dostupné skupiny ploch jako vzorky a jednu vyberete. Klepnutím na vzorek ho můžete přejmenovat, změnit jeho barvu nebo ho smazat. `Odebrat nepoužité` smaže nepoužité vzorky, `Resetovat` odstraní všechny. Ikonou plus vytvoříte nové vzorky.
* `Bod` - Malováním po objektu určujete skupiny ploch. Když je zapnuté „+ Skupina ploch", každý nový tah automaticky vytvoří novou skupinu ploch, což se hodí pro rychlé vymezení oblastí. Klepnutí vyplní vybranou oblast. Posuvník nastavuje poloměr bodu.
* `Uvolnit` - Vyhlazuje hranice skupin ploch. Velmi užitečné pro vytvoření čistých hran pro quad remeshing nebo pro vymezení panelů při hard surface modelování. Posuvníky ovládají poloměr a intenzitu uvolnění.
* Tvary - Vytváří skupiny ploch tvary místo štětce, pomocí `Zámek + poloměr`, `Laso`, `Polygon`, `Čára`, `Obdélník` a `Elipsa`. Více v části [Ovládání výběru](#selection-controls).
* `Vybrat` - Vedlejší režim. Když je zapnutý, vybere vzorek v místě, kde tah začíná, a použije ho po zbytek tahu. Velmi užitečné pro úklid oblastí skupin ploch; pokud se skupina ploch rozšířila příliš daleko, zapněte `Vybrat`, začněte tah tam, kde je vzorek skupiny ploch správně, a táhněte až k hranici, abyste přiřadili správný vzorek.

#### Horní panel nástrojů skupiny ploch {#facegroup-top-toolbar}

Panel nástrojů v horní části výřezu obsahuje další ovládací prvky:

* `Uvolnit (Vše)` - Tažením uvolníte hranice všech skupin ploch najednou.
* `Přední` / `Viditelné` / `Připojené` - Stejné filtry tahu jako v panelu nástrojů [Maska](#mask).
* `Z normál` - Vytvoří skupiny ploch podle úhlu mezi plochami. Okno obsahuje `Úhel` a umožňuje vynechat malé skupiny podle `Počet stěn` nebo `Plocha povrchu`, s `Náhled` před potvrzením.
* `Z částí` - Vytvoří skupinu ploch pro každou nespojenou část.
* `Z UV` - Vytvoří skupinu ploch pro každý UV ostrov.
* `Z masky` - Vytvoří skupinu ploch z maskované oblasti.
* `Na dotek` - Zvolte, co udělá klepnutí na skupinu ploch: vyplní ji aktuální skupinou ploch, skryje ji, zamaskuje ji, nebo `Póza` (klepnutá skupina a vše za ní se odmaskuje a gizmo se umístí na kloub, s posuvníkem `Rozmazat` pro masku). Druhý přepínač `Na dotek`, dostupný, když má síť masku, omezí klepnutí na plochy na stejné straně masky.
* Tlačítka `Vymazat` pro nástroje [Skrýt](#hide) a [Maska](#mask), kterými vše odkryjete nebo vymažete masku, aniž byste opustili nástroj.

#### Nastavení skupiny ploch {#facegroup-settings}

Menu `Nástroj` extrahuje skupiny ploch do nových objektů, se stejnými volbami jako `Extrakt` v [Nastavení masky](#mask-settings). Tlačítko `Skupina ploch` nahoře vybírá, které skupiny se extrahují, a navíc je tu posuvník `Mezera`: posune každou hranici po povrchu dovnitř, záporná hodnota ji posune ven, aby se překrývaly. U sousedních panelů použijte polovinu požadované mezery.

### ![](/icons/tool_hide.webp) Skrýt {#hide}
Skrývá nebo izoluje části objektu. 

Hlavní režimy se ovládají z levého menu:

* `Bod` - Štětcem po objektu skrýváte jeho části.
* Tvary -  Skrývá tvary místo štětce, pomocí `Laso`, `Polygon`, `Čára`, `Obdélník` a `Elipsa`. Více v části [Ovládání výběru](#selection-controls).
* `Zobrazit` - Vedlejší režim, obrátí operaci, takže zvolený režim části objektu zobrazí, místo aby je skryl.

V horní části výřezu se objeví panel nástrojů s dalšími ovládacími prvky:

* `Vymazat vše` - Obnoví objekty, všechny skryté části se znovu zobrazí. Když mají skryté části i jiné objekty, další tlačítko `Vymazat` obnoví jen vybrané objekty.
* `Obrátit` - Prohodí skryté a viditelné části.
* `Smazat` - Smaže skrytou část objektu
* `Rozdělit` - Oddělí skrytou část objektu do nového tvaru.
* `Přední` / `Viditelné` / `Připojené` - Stejné filtry tahu jako v panelu nástrojů [Maska](#mask).
* `Na dotek` (skupina ploch) - Rychlé skrývání částí pomocí skupin ploch: klepnutím na skupinu ploch skryjete celou skupinu.
* `Na dotek` (maska) - Pokud je aktivní maska, klepnutím skryjete maskovanou část.

### ![](/icons/tool_measure.webp) Měřit {#measure}
Tažením změříte vzdálenost mezi 2 body. Po umístění můžete koncovými body táhnout a měření upravit.

Levý panel nástrojů určuje, jak se vzdálenost měří:

* `Čára` - Přímka mezi oběma body.
* `Povrch` - Vzdálenost po povrchu, podél řezu procházejícího oběma body z pohledu kamery.
* `Průřez` - Obvod průřezu procházejícího oběma body, jako krejčovský metr kolem paže.
* `Vrchol` - Přichytí koncové body k nejbližšímu vrcholu.
* `Zlatý řez` - Zobrazí žlutou tečku v bodě zlatého řezu měřené vzdálenosti.
* Tlačítko `?` zobrazí objem, plochu povrchu a velikost vybraných objektů.

### ![](/icons/tool_arrange.webp) Uspořádat {#arrange}
Zarovná a rozmístí několik objektů najednou, podobně jako nástroje zarovnání ve 2d grafických aplikacích. Nejdřív vyberte objekty; s jediným objektem pracuje Uspořádat místo toho s jeho samostatnými částmi. Kolem výběru se vykreslí rámeček, tažením za jeho úchyty měníte jeho velikost.

Ovládací prvky jsou v panelu nástrojů v horní části výřezu:

* `Svět` / `Obrazovka` - Uspořádá podél os světa, nebo podél obrazovky (vlevo, vpravo, nahoře, dole).
* `Zarovnat` - Zarovná objekty podle jejich minima, středu nebo maxima v každé ose.
* `Rozmístit` - Rozmístí objekty rovnoměrně mezi dva krajní, podle jejich minima, středu nebo maxima. Potřebuje alespoň 3 objekty.
* `Čára` - Seřadí objekty do řady podél osy.
* `Mřížka` - Seřadí objekty do mřížky, s počtem objektů v ose `X`, `Y` a `Z`.
* `Kruh` - (jen Svět) Seřadí objekty do kruhu kolem osy `X`, `Y` nebo `Z`.
* `Koule` - (jen Svět) Rozmístí objekty po kouli.

`Čára`, `Mřížka`, `Kruh` a `Koule` mají všechny posuvník `Rozestupy` pro mezeru mezi objekty.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Tento nástroj převede vybraný objekt na čistou topologii ze čtyřúhelníků, s ovládáním hustoty, toku hran a symetrie. 

::: tip
Quad Remesher vyvíjí společnost [Exoside](https://exoside.com/) pro iOS a desktop. 

Na iOS je to nákup v aplikaci Nomad, jednorázová platba 16 USD.

Pro desktop si kupte licenci od [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Můžete si ji koupit jen pro Nomad na desktopu, nebo jako společnou licenci pro všechny podporované desktopové aplikace.

Pokud už Quad Remesher pro jinou desktopovou aplikaci vlastníte, můžete si [levněji koupit upgrade na všechny platformy.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher není pro Android dostupný. Android může používat bezplatné open source remeshery na záložce topologie [Quad přesíťování](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), počítejte ale s tím, že nabízejí méně funkcí.
:::

Dokud Quad Remesher neodemknete, začíná horní panel nástrojů tlačítkem košíku místo tlačítek pro remesh. Na iOS otevře nákup v aplikaci. Na desktopu zobrazí `Odemknout (koupit, obnovit, zkušební verze)`, které ověří vaši licenci Exoside (nebo spustí zkušební verzi). Po aktivaci se zpřístupní levý i horní panel nástrojů.

* `Bod` - Tímto štětcem nastavujete cílovou hustotu. Intenzita 100 % maluje červeně, což v těchto oblastech použije dvojnásobnou cílovou hustotu čtyřúhelníků. Intenzita 0 % maluje azurově, což v těchto oblastech použije poloviční cílovou hustotu. Intenzita 50 % maluje šedě, což použije výchozí cílovou hustotu.
* `Hladit` - Vyhladí přechody hustoty mezi červenou, šedou a azurovou.
* `Rozmazat` - Rozmaže namalovanou hustotu.
* `Křivka` - Kreslete křivky po povrchu sochy, Quad Remesher je použije jako vodítka pro tok hran. Klepnutím na křivku ji smažete.
* `Cesta` - Kreslete cesty po povrchu sochy, Quad Remesher je použije jako vodítka pro tok hran. Klepnutím na cestu ji smažete. 
* `Obdélník` - Kreslete obdélníky po povrchu sochy, Quad Remesher je použije jako vodítka pro tok hran. Klepnutím na cestu ji smažete.
* `Elipsa` - Kreslete elipsy po povrchu sochy, Quad Remesher je použije jako vodítka pro tok hran. Klepnutím na cestu ji smažete.

#### Horní panel nástrojů Quad Remesheru {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

V horní části výřezu se objeví panel nástrojů s dalšími ovládacími prvky:


* `<Count>` - Klepnutím spustíte proces Quad Remesheru; číslo ukazuje cílový počet čtyřúhelníků.
* `Čtyřúhelníky` - Cílový počet čtyřúhelníků nastavíte posouváním doleva a doprava, nebo klepnutím zadáte přesné číslo. Berte ho spíš jako vodítko než pevné číslo, různé volby Quad Remesheru často způsobí, že výsledek cíli přesně neodpovídá.
* `Poloviční` - Zkratka, která nastaví cílový počet na polovinu aktuálního počtu polygonů.
* `Stejný` - Zkratka, která nastaví cílový počet na aktuální počet polygonů.
* `Vodítka` - Přepíná použití nebo ignorování vodítek. Když nějaká vodítka existují, druhé tlačítko `Vodítka` ukazuje jejich počet; klepnutím je všechna smažete.
* `Hustota` - Přepíná použití nebo ignorování namalované hustoty. Když je hustota namalovaná, druhé tlačítko `Hustota` ji odstraní.
* `Skupina ploch` - Přepíná použití nebo ignorování skupin ploch k řízení Quad Remesheru.
* `Uvolnit` - Přepíná automatické uvolnění hranic skupin ploch během remeshingu. Pokud už jste hranice skupin ploch uvolnili či vyhladili, tuto volbu vypněte.
* `Posuvník Uvolnit` - Zkratkový posuvník pro uvolnění hranic skupin ploch.
* `Tvrdé hrany` - Přepíná snahu zachovat ostré hrany.
* `Znovuprojektovat vrchol` - Přepíná zpětné promítnutí nového rozložení na vstupní síť.
* `Sym` - Přepíná symetrický výsledek. Symetrie se vždy počítá kolem osy x světa, takže pokud čekáte symetrický výsledek, ujistěte se, že je model v počátku.
* `...` - Okno nastavení Quad Remesheru. 

#### Menu nastavení Quad Remesheru {#quad-remesher-settings-menu}

Tlačítko `...` na konci horního panelu nástrojů otevře okno se zbývajícími nastaveními:

* `Přizpůsobivý počet kvádrů` - Přepíná použití menších čtyřúhelníků v oblastech s velkým zakřivením a větších v oblastech s malým zakřivením.
* `Adaptivní velikost` - Nastavuje míru přizpůsobení. 100 % umožní maximální přizpůsobení velikosti, při 0 % budou čtyřúhelníky stejně velké.

::: tip

Recept na dobrý quad remesh s minimem chyb:

* Rozdělte síť do skupin ploch podle ideálního toku čtyřúhelníků.
* Uvolněte skupiny ploch, aby měly hladké hranice.
* Použijte decimaci. Ta zajistí, že na hranách skupin ploch nebudou tenké ani zkreslené plochy. V nastavení decimace mějte zapnuté skupiny ploch. Hrany trojúhelníků pak budou přesně sledovat hrany skupin ploch. 

V nastavení quad remeshe mějte vypnuté uvolnění (síť už jste uvolnili) a měli byste dostat dobré výsledky.

:::

### ![](/icons/tool_select.webp) Vybrat {#select}
Režimy tvarů (`Laso`, `Obdélník`, `Elipsa`) použijte k výběru objektů ve scéně. `Zrušit výběr` odebere objekty z výběru.

### ![](/icons/tool_lattice.webp) Mřížka {#lattice}
Deformuje objekt pomocí klece z řídicích bodů kolem něj, místo modelování jeho povrchu. Posunutím několika bodů klece plynule ohnete, zkroutíte nebo protáhnete celý objekt, což se skvěle hodí na úpravu proporcí nebo pózování, aniž byste sahali na topologii. Deformace zůstává živá, dokud ji nepotvrdíte.

Levý panel nástrojů určuje, jak klec upravujete:

* `Body` - Táhnete přímo body a hrany klece. Klepnutím bod vyberete.
* `Zobrazit` - Pohybujete kamerou, aniž byste upravovali klec.
* `Uvolnit` - Štětec, který uvolňuje body klece pod sebou.
* `Elastický` - Štětec, který táhne body klece s pružným útlumem, jako nástroj [Elastický](#elastic).
* `Gizmo` - Gizmem přesouváte, otáčíte a měníte velikost vybraných bodů. Jeho vedlejší režim je `Pivot`.
* `Laso` - Vybírá body klece lasem, `Zrušit výběr` je z výběru odebere.

Okno tvarů obsahuje také `Měkký rádius`, díky kterému tažení bodu pohne i sousedními body (v buňkách mřížky, 0 pohne jen výběrem), a `Invertovat výběr`.

Panel nástrojů v horní části výřezu obsahuje:

* `Dokončit` - Použije deformaci na objekt a odstraní klec.
* `Resetovat` - Odstraní klec i její deformaci.
* `Krytí` - Krytí zobrazení klece.
* `Zrcadlová strana` - Se symetrií přepíná, která zrcadlová strana klece se zobrazí a dá se vybírat, s vlastním `Krytí` pro skrytou stranu.
* `Body mřížky` - Které body klece lze posouvat: celou mřížku, povrch a středový bod, nebo jen povrch.
* `Tuhost` - Jak tuhá je deformace, od hladké (0 %) po tuhou a lineární (100 %).
* `Útlum` - Jak daleko za klecí deformace slábne.
* `Zarovnat` - Zarovná klec s objektem, nebo se světem.
* `X`, `Y`, `Z` `Dělení` - Počet buněk klece v každé ose. Tlačítko režimu vedle určuje jejich vztah: `x = y = z` použije stejný počet ve všech 3 osách, `Jednotný` zachová stejné rozestupy bodů v každé ose a `Vlastní` vám umožní nastavit každou osu volně.

#### Nastavení mřížky {#lattice-settings}
* `Rychlost otáčení` - Stejné volby otáčení jako u nástroje [Přesunout](#move-settings), použité při tažení bodů klece.

### ![](/icons/tool_view.webp) Pohled {#view}
Tento „nástroj" nedělá nic zvláštního, je to prostě způsob, jak si model prohlížet, aniž byste scénu měnili.

#### Nastavení pohledu {#view-settings}
Dokud je nástroj Pohled aktivní, tato nastavení přepisují některé volby zobrazení, abyste měli čistý pohled pro prezentaci nebo kontrolu modelu:

* `Primitivum (Upravit)`, `Opakovač (Upravit)`, `Světlo (Upravit)`, `Kamera (Upravit)` - V nástroji Pohled umožní upravovat ve výřezu primitiva, opakovače, světla a kamery. Vypněte je, abyste jejich úchyty omylem nepohnuli.
* `Zkratka kamery (vždy)` - Ve výřezu vždy zobrazí tlačítka zkratek kamery.
* `Zobrazit masku`, `Obrys`, `Ztmavit nevybrané objekty` - Zobrazí masku, obrys vybraných objektů, nebo ztmaví nevybrané objekty. `Auto` se řídí vaším obvyklým nastavením, `Ne` a `Ano` ho vynutí.
* `Zobrazit čáru (Symetrie)`, `Zobrazit rovinu (Symetrie)` - Zobrazí čáru nebo rovinu symetrie, se stejnými volbami `Auto`, `Ne` a `Ano`.
* `Ikona` - Zobrazí ve výřezu ikony skupin, opakovačů, světel, kamer a hierarchie, se stejnými volbami.


## Kontextové menu panelu nástrojů {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Kliknutím pravým tlačítkem nebo dlouhým stiskem na nástroj v panelu nástrojů otevřete kontextové menu. Obsahuje tyto volby:

* `Uložit` - Uloží změny, které jste v nástroji provedli
* `Klonovat` - Zduplikuje nástroj do nové zkratky nástroje
* `Poslední uložené` - Vrátí nástroj do naposledy uložené verze
* `Ikona` - Změní ikonu nástroje. Pokud má nástroj vlastní ikonu, toto tlačítko ji odstraní.
* `→ ...` - Přesune nástroj do jiné složky panelu nástrojů, nebo do nové
* `Resetovat` - Obnoví výchozí nastavení nástroje
