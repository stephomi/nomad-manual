# ![](/icons/multires.webp) Topologie {#topology}

Tato nabídka řídí topologii objektů v Nomadu a nabízí také nástroje pro zapékání a přenos detailů mezi objekty i mezi texturami.

![](/images/topology_overview.webp)

Nomad pracuje s polygony: geometrii tvoří trojúhelníky a čtyřúhelníky.
Topologií rozumíme jak počet ploch, tak i to, jak jsou body (vrcholy) navzájem propojené.

Je důležité mít topologii pod kontrolou, zvlášť pokud chcete sochat nebo malovat jemné detaily.

::: tip Jak mít topologii pod kontrolou?
Můžete zobrazit [drátový model](settings.md#wireframe) nebo jednoduše vypnout [hladké stínování](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Nabídka Topologie má několik karet ve dvou řadách:

| Metoda                                | Ikona                        | Popis                                                            |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multirezoluce](#multiresolution)     | ![](/icons/multires.webp)   | Úpravy na několika úrovních detailu pomocí dělení                |
| [Voxelové přesíťování](#voxel-remesher) | ![](/icons/voxel.webp)    | Přepočítá novou topologii s rovnoměrnou hustotou                 |
| [Dynamická topologie](#dynamic-topology) | ![](/icons/dynamic.webp) | Přidává a ubírá plochy lokálně v reálném čase při sochání nebo malování |
| [Různé](#misc)                        | ![](/icons/topo_extra.webp) | Uzavření otvorů, vynucení manifoldu a převod na triplanár        |
| [Primitiva](#primitive)               | ![](/icons/dot.webp)        | Možnosti primitiva                                               |
| [Decimace](#decimation)               | ![](/icons/decimate.webp)      | Sníží počet ploch a zachová přitom tvar                       |
| [Quad přesíťování](#quad-remesh)      | ![](/icons/quad.webp)       | Znovu postaví objekt s čistou sítí čtyřúhelníků                  |
| [Rozbalení UV](#uv-unwrap)            | ![](/icons/uv.webp)         | Vytvoří UV pro texturování                                       |
| [Péct](#bake)                         | ![](/icons/bake.webp)       | Zapeče detaily a malbu do textur, vrcholů nebo VDM razítek       |


## Statistiky polygonů {#polygon-stats}

![](/images/topology_stats.webp)

Horní část každé karty ukazuje počty polygonů vybraného objektu, a pokud scéna obsahuje víc objektů, i celé scény. Sloupce udávají počet vrcholů, trojúhelníků, čtyřúhelníků (polygonů se 4 stranami) a UV souřadnic (0, když objekt nemá UV).

Klepnutím na tuto část zobrazíte seznam všech objektů scény s přesnými počty, včetně počtu skupin ploch.

## ![](/icons/cog.webp) Nabídka ozubeného kolečka {#gear-menu}
Některé sekce, například na kartách [Quad přesíťování](#quad-remesh) a [Péct](#bake), mají další možnosti. Otevřete je ikonou ozubeného kolečka vedle názvu sekce.

## ![](/icons/multires.webp) Multirezoluce {#multiresolution}

![](/images/topology_multires_menu.webp)

### Co je multirezoluce? {#what-is-multiresolution}
Multirezoluce se hodí ve dvou hlavních situacích:
- hladké dělení, kterým zvýšíte počet polygonů objektu
- práce s několika úrovněmi rozlišení, takže můžete střídat drobné a velké úpravy

![](/videos/multiresolution.mp4)

#### Postup s multirezolucí {#multiresolution-workflow}
Důležitou vlastností multirezoluce je, že se můžete vrátit na nižší rozlišení, upravit objekt a pak se vrátit na nejvyšší rozlišení, aniž byste přišli o jemné detaily. Všechny detaily vysokého rozlišení se automaticky promítnou.

[Vrstvy](layers.md#layers) jsou k dispozici na každé úrovni rozlišení.

::: warning
Pokud použijete nástroj, který mění topologii objektu, přijdete o všechny ostatní úrovně rozlišení!
Než se to stane, měli byste vždy dostat varování, například když používáte:
- [voxelové přesíťování](#voxel-remesher)
- [dynamickou topologii](#dynamic-topology)
- [nástroj Oříznout](tools.md#trim)
- [nástroj Rozdělit](tools.md#split)
:::


### Posuvník multirezoluce {#multiresolution-slider}
Tento posuvník ukazuje počet úrovní dělení aktuálního objektu. Když vidíte 6 svislých čárek, má objekt 6 úrovní dělení. Kroužek označuje právě zobrazenou úroveň.

Malé ikony nad posuvníkem ukazují, které možnosti (`Zamknout úroveň 0`, `Lineární`, `Ostrá hrana`, `Udržet trojúhelníky`) byly u jednotlivých úrovní použity.

### Opačný {#reverse}
Na nejnižší úrovni dělení se tlačítko Opačný pokusí vytvořit úroveň pod tou aktuální. Obvykle to jde jen tehdy, když objekt vznikl dělením už od začátku, třeba v Nomadu nebo v jiné 3d aplikaci, která pracuje s multirezolučními dělenými povrchy.

### Poddělení {#subdivide}
Tlačítko *Poddělení* zčtyřnásobí počet polygonů, takže počet polygonů hlídejte, umí vyrůst velmi rychle! Pokud by výsledek byl příliš těžký, Nomad se nejdřív zeptá na potvrzení.
Důležitou vlastností *dělených povrchů* je, že se postupně blíží *hladkému povrchu*.
Abyste pochopili, jak to funguje, zkuste tlačítko *Poddělení* na objektu s několika málo polygony.

Toto *vyhlazování* můžete vypnout možností `Lineární`.

### Smazat nižší {#delete-lower}
Smaže úrovně dělení pod právě zobrazenou úrovní. Pokud to uděláte omylem, můžete je znovu vytvořit tlačítkem Opačný.

### Smazat vyšší {#delete-higher}
Smaže úrovně dělení nad právě zobrazenou úrovní.

### ![](/icons/lock.webp) Zamknout úroveň 0 {#lock-lv0}
Zachová tvar nejnižší úrovně dělení, když sochaříte na vyšších úrovních. Malba se do úrovně 0 přenáší i tak. To může být důležité, pokud objekt vznikl v jiné aplikaci a základní síť musí zůstat beze změny.

Tato možnost je dostupná jen před prvním dělením. Když je vypnutá, větší změny na vyšších úrovních dělení posunou i úroveň 0.

### ![](/icons/linear.webp) Lineární {#linear-subdivision}
Rozdělí síť bez jakéhokoli vyhlazení.

### ![](/icons/group.webp) Ostrá hrana {#sharp-border}
Pokud má objekt skupiny ploch, tato možnost zachová hranice skupin ostré. Lze ji nastavit pro každou úroveň dělení zvlášť (posuvník dělení pak nad danou úrovní zobrazí malou ikonu).

### ![](/icons/triangle.webp) Udržet trojúhelníky {#keep-triangles}
Většina běžných systémů dělených povrchů se při dělení snaží převést všechny polygony na čtyřúhelníky. Tento přepínač vynutí, aby dělení místo toho použilo trojúhelníky.

::: tip

Dělení ve výchozím stavu zaoblí všechny ostré hrany. Chcete-li hrany ponechat trochu ostré, vyzkoušejte `Lineární` nebo `Ostrá hrana` na prvních 2 úrovních dělení a na vyšších úrovních je vypněte. Vznikne tak poloostrá dělená síť.

:::

### Zobrazit nejvyšší úroveň {#show-highest-level}
Zobrazí nejvyšší úroveň se všemi detaily, zatímco sochaříte na nižší úrovni. Hodí se, když chcete při velkých úpravách vidět konečný výsledek.

### Drátový model: Pouze úroveň 0 {#wireframe-level-0-only}
Když je zapnutý [drátový model](settings.md#wireframe), zobrazí se drátový model jen nejnižší úrovně. Hustý drátový model vysokých úrovní by jinak mohl zakrývat tvar.


## ![](/icons/voxel.webp) Voxelové přesíťování {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
`Voxelové přesíťování` vynutí pro celou síť topologii s rovnoměrným rozlišením, takže všechny polygony mají zhruba stejnou velikost. To je velmi užitečné, když nechcete řešit topologii a prostě chcete volně sochat.

Typický postup sochání může začít tím, že pomocí `Voxelové přesíťování` nahrubo vytvarujete základní tvar v nízkém rozlišení.
Kdykoli síť příliš natáhnete, stačí čas od času stisknout tlačítko *Remesh*, abyste se vyhnuli přílišné deformaci.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Jak bylo řečeno výše, Nomad je polygonový software, ale `Voxelové přesíťování` je výjimka: k přesíťování se (dočasně) používá jiný přístup.

Jeden velký rozdíl je, že voxelový přístup nepřipouští samoprůniky, takže se vyřeší.
Také nepodporuje sítě s otvory.

Otvory nemyslíme `genus hole` (`díru` uprostřed donutu), ale sítě, které nejsou `vodotěsné`/`uzavřené`.
V praxi to znamená, že před přesíťováním se všechny otvory zaplní, podobně jako u [nástroje Oříznout](tools.md#trim) nebo [funkce vyplnění otvorů](#holes). Způsob určuje níže popsaná možnost [Otvory](#voxel-holes).
:::

### ![](/icons/voxel.webp) Remesh {#voxel-remesh}
Spustí voxelové přesíťování. Malé ikony na tlačítku připomínají, které z níže uvedených možností jsou zapnuté.

### Rozlišení {#voxel-resolution}
Velikost voxelů použitých při výpočtu, vyšší hodnoty dávají více detailu. Při změně tohoto parametru se na síť překryje šachovnicový vzor, který ukazuje náhled výsledku.

Kapátko převezme rozlišení z hustoty sítě v místě, kam klepnete. Tlačítko s kostkou vedle něj přepne hodnotu na `Délka hrany` ve světových jednotkách: stejná hodnota pak dá stejný detail na jakémkoli objektu.

### Vytvořit multirezoluci {#build-multiresolution}
Vytvoří při voxelovém přesíťování nižší úrovně multirezoluce. Pokud rozlišení nastavíte podle šachovnicového vzoru a `Vytvořit multirezoluci` nastavíte na 2, bude mít výsledek detail odpovídající posuvníku rozlišení, a když přejdete na kartu Multirezoluce, bude na úrovni 2, takže pod ním budou sítě nižšího rozlišení na úrovni 1 a úrovni 0. Je to dobrý způsob, jak získat čistou síť s rovnoměrnými polygony a zároveň řídicí síť s nižším rozlišením.

Při vysokém rozlišení je to také rychlejší a spotřebuje méně paměti. Při nízkém rozlišení a mnoha úrovních ale přijdete o detaily.

::: tip Tip: Vytvořit multirezoluci a stabilní vyhlazování

Tato možnost někdy v geometrii vytvoří „smyčky“, které se špatně vyhlazují a dělají malé pupínky. Pokud se to stane, zapněte v možnostech nástroje Hladit „Stabilní vyhlazování“.

:::

### Zesílit tenké části {#thicken-thin-parts}
Části tenčí než voxely se mohou při přesíťování rozpadnout nebo zmizet. Tato možnost je zesílí, aby přežily, vyšší hodnoty zesilují víc. Není dostupná spolu s `Ostré hrany` ani `Ostrá hranice`.

### Otvory {#voxel-holes}
Jak se otvory před přesíťováním uzavřou:

* `Vyplnit` - Každý otvor se uzavře samostatně, od svého okraje.
* `Tvar` - Otvory se uzavřou podle okolního povrchu a otevřené kusy, které se překrývají, se spojí.

### ![](/icons/angle.webp) Ostré hrany {#keep-sharp-edges}
Přichytí nové body k ostrým hranám původní sítě. Hodí se hlavně pro jednoduché booleovské operace s primitivy a může způsobit deformace.

### ![](/icons/group.webp) Ostrá hranice {#voxel-sharp-border}
Nové plochy sledují hranice skupin ploch a hranice zůstane ostrá tam, kde se podél ní povrch láme.

### ![](/icons/group_separate.webp) Oddělit skupiny {#keep-groups-separate}
Každá skupina ploch se přesíťuje samostatně: skupiny se nikdy nespojí a každá zůstane uzavřeným kusem ve své vlastní skupině. V tomto režimu se multirezoluce nevytváří. Možnost je dostupná, když má objekt několik skupin ploch.

## ![](/icons/dynamic.webp) Dynamická topologie {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multirezoluce a voxelové přesíťování jsou běžné způsoby řízení topologie, ale u obou musíte hlídat, abyste polygony příliš nenatáhli nebo příliš nestlačili.

Dynamická topologie je alternativní přístup. Během tahu štětcem Nomad průběžně přidává a ubírá polygony, takže když vyrýváte drobné detaily, přidá mnoho malých polygonů přesně tam, kde je potřebujete, a vyhlazování jinde polygony ubere.

Dynamická topologie používá trojúhelníky, ne čtyřúhelníky. Může to vypadat trochu neuspořádaně, ale na drátový model je lepší se skoro nedívat: soustřeďte se na pěknou sochu bez starostí o topologii a později můžete některým z dalších nástrojů Nomadu pro přesíťování vytvořit čistou síť ze čtyřúhelníků.

Podívejte se na video níže.

![](/videos/dynamic.mp4)

### Povolená {#enabled}
Zapne dynamickou topologii. Pod posuvníky poloměru a intenzity štětce se objeví ikona DynTopo, kterou můžete DynTopo zapínat pro každý nástroj zvlášť. Může znatelně ovlivnit výkon a vrstvy se aktualizují správně.

### Detail {#dyn-detail}
Řídí množství detailu, jeho chování závisí na volbě „Detail podle…“, viz níže. V režimu `Obrazovka` popisek ukazuje cílovou velikost trojúhelníku v pixelech. V režimu `Konstantní` můžete kapátkem převzít detail z hustoty sítě v místě, kam klepnete.

### Detail podle… {#detail-based-on}
| Metoda     | Popis                                                           |
| :--------: | :-------------------------------------------------------------: |
| Obrazovka  | Úroveň detailu závisí na tom, jak velký je objekt na obrazovce. Posuvník detailu na 100 % nebo víc dává jemný detail s malými trojúhelníky, 1 % hrubý detail s velkými trojúhelníky.  |
| Poloměr    | Množství detailu určuje poloměr nástroje. Malý poloměr nástroje dává jemný detail, velký poloměr hrubý detail. Posuvník detailu tento poměr násobí.                     |
| Konstantní | Množství detailu určuje posuvník detailu a nezávisí na velikosti obrazovky ani nástroje. Je to stejná hodnota jako posuvník [Detail](#all-detail) u `Remesh`.             |

::: tip TIP: Režim Poloměr

Abyste lépe pochopili, jak režim Poloměr funguje, začněte jedním prstem posouvat posuvník detailu a zároveň druhým prstem měňte poloměr nástroje. Uvidíte, jak spolu souvisejí.

:::

### Upřednostnit... {#prefer}
| Metoda   | Popis               |
| :------: | :-----------------: |
| Rychlost | Upřednostní výkon   |
| Kvalita  | Upřednostní kvalitu |

Když upřednostníte `Kvalita`, jsou tu 2 hlavní rozdíly:
- zjemnění se provede ještě před sochařením, takže při malování nebo sochání velmi drobných detailů vznikne méně artefaktů interpolace
- zjemňování běží, dokud nedosáhne správné úrovně detailu, místo aby postupovalo po krocích.
 
Díky tomu bude topologie vždy zjemněná podle očekávání, i když sochaříte velmi drobné detaily nebo děláte rychlé tahy



### ![](/icons/pressure.webp) Použít tlak na poloměru {#use-pressure-on-radius}
Má smysl jen v režimu `Poloměr`. Když je zapnutá, úroveň detailu vždy odpovídá velikosti štětce, i když velikost štětce ovlivňuje tlak pera.

### Použít útlum tahu {#use-stroke-falloff}

Do výpočtů DynTopo zahrne i křivku útlumu štětce a alfu.

### Metoda {#method}
Zvolte, jak dynamická topologie mění síť, a to při sochání i při použití [Remesh](#dyn-remesh):

| Metoda         | Popis                                                                 |
| :------------: | :-------------------------------------------------------------------: |
| Unifikace      | Může přidávat i ubírat plochy, tento režim je použitý ve videu výše   |
| Rozdělení      | Pouze přidává nové plochy, nemůže je ubírat                           |
| Decimace       | Pouze ubírá plochy, nemůže přidávat nové                              |

### ![](/icons/shield.webp) Chránit maskovanou oblast {#protect-masked-area}
Maskované oblasti budou chráněné před změnami topologie.

### ![](/icons/normal.webp) Extrapolace vrcholů {#vertex-extrapolation}
Umístí body na hladký povrch, který sleduje zakřivení kolem nich, místo aby ležely naplocho na stávajících plochách.

### Detail {#all-detail}
Rozlišení použité pro přesíťování. Pokud je DynTopo v režimu „Konstantní“, je to stejná hodnota jako posuvník Detail v horní části této nabídky. Kapátko převezme detail z hustoty sítě v místě, kam klepnete.

### Remesh {#dyn-remesh}
Spustí přesíťování celé sítě algoritmem DynTopo. Pro úplné přesíťování byste ale obvykle měli použít [voxelové přesíťování](#voxel-remesher).

Oproti voxelům má tu výhodu, že síť nemusí být uzavřená a maskovaná oblast zůstane chráněná, takže lépe určíte, kde má být hustota větší a kde menší.



## ![](/icons/topo_extra.webp) Různé {#misc}

![](/images/topology_misc_menu.webp)

Tato karta sdružuje nástroje k čištění nebo převodu sítě: uzavření otvorů, vynucení manifoldu nebo převod na triplanár.

### ![](/icons/hole.webp) Otvory {#holes}
![](/images/topology_holes_menu.webp)
Většinou bude váš objekt vodotěsný, tedy síť bude „uzavřená“.

Pokud má objekt otvory, můžete je vyplnit.

![](/videos/hole_filling.mp4)

::: tip
Když spustíte voxelové přesíťování, všechny otvory se automaticky uzavřou, ať už ho používáte na 1 síť nebo na více sítí.
:::

#### Zavřít otvory {#close-holes}
Provede uzavření otvorů.

#### Možnosti {#holes-gear-menu}
Tyto možnosti mění způsob vyplnění otvorů:

##### Skupina ploch {#fill-face-group}
Zvolte skupinu ploch pro nové plochy:

* `Smíšené` - Otvor obklopený jedinou skupinou ploch ji převezme, otvor dotýkající se několika skupin dostane novou.
* `Nový` - Vyplněné otvory dostanou novou skupinu ploch.
* `Znovu použít` - Každý otvor převezme skupinu ploch, která ho obklopuje nejvíc.

##### Detail {#fill-detail}
Hustota polygonů použitá k vyplnění otvoru. Při posouvání tohoto posuvníku se na modelu zobrazí šachovnicový vzor, který naznačí velikost trojúhelníků. Zaškrtávací pole tuto možnost vypne a použijí se jen stávající body, z čehož obvykle vzniknou přes otvor dlouhé tenké trojúhelníky, na kterých se špatně sochá.

##### Přemostit {#fill-non-manifold}
Vyplní otvor a ostrůvky uvnitř něj jako jeden povrch, místo aby vyplnil každý okraj zvlášť. Vyšší úhel přemostí zakřivenější otvory. Zaškrtávací pole tuto možnost vypne.

### ![](/icons/cog.webp) Vynutit manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Pokusí se vyčistit hrany, které nejsou manifold. Může se hodit pro externí software, který nepodporuje hrany sdílené více než 2 plochami.

#### Vyčistit {#clean}
Provede vyčištění.

#### Možnosti {#force-manifold-gear-menu}
Tato možnost mění způsob čištění sítě:

##### Smazat malé plochy {#delete-small-faces}
Práh, podle kterého se malé polygony odstraní a spojí. Zapnete ho jeho zaškrtávacím polem.


### ![](/icons/triplanar.webp) Triplanární {#triplanar}
![](/images/topology_triplanar_menu.webp)
Převede síť na [triplanární](scene.md#triplanar) primitivum.
Pravděpodobně při tom přijdete o hodně detailu: ztratí se i vrstvy, malba a multirezoluce.

#### Vynutit krychli {#force-cubic}
Triplanár bude krychle. Jinak se triplanár přizpůsobí nejbližšímu ohraničujícímu kvádru kolem objektu.

#### Převést {#convert}
Provede převod na triplanár.

#### Rozlišení {#triplanar-resolution}
Rozlišení mřížky triplanáru, vyšší hodnoty zachovají více detailu.

## ![](/icons/decimate.webp) Decimace {#decimation}

![](/images/topology_decimation.webp)

Sníží počet polygonů a snaží se přitom zachovat co nejvíc detailů, s použitím trojúhelníků.

Tato funkce se může hodit, když chcete exportovat pro 3d tisk.
Pokud ale chcete na objektu dál sochat, raději ji nepoužívejte, protože může vytvořit nerovnoměrné trojúhelníky.

Maskované oblasti se nedecimují.

![](/videos/decimate.mp4)

::: tip

Výpočet [nástroje Quad Remesher](tools.md#quad-remesher) na objektech s vysokým počtem polygonů může trvat dlouho a dávat těžko ovladatelné výsledky. Když síť předem připravíte pomocí [skupin ploch](tools.md#facegroup) a decimace, Quad Remesher poběží mnohem rychleji a topologii budete mít mnohem víc pod kontrolou.

* Rozdělte síť na skupiny ploch podle ideálního toku čtyřúhelníků.
* Uvolněte skupiny ploch, aby měly hladké hranice.
* Decimujte. Tím zajistíte, že na hranici skupin ploch nebudou tenké ani zdeformované plochy. V části `Zachovat hranice` mějte zapnuté `SkupinaPovrch`. Hrany trojúhelníků pak budou přesně sledovat hranice skupin ploch.
* V možnostech Quad Remesheru mějte vypnuté uvolnění (síť už je uvolněná) a měli byste dostat dobré výsledky.

:::

### Decimace {#decimate}
Spustí decimaci.

Ikony vedle tlačítka decimace zobrazují níže uvedené možnosti a umožňují je přepínat. Procento udává, jak silná daná možnost je.

* ![](/icons/palette.webp)  `Zachovat malbu` - Více trojúhelníků umístí tam, kde jsou detaily malby.
* ![](/icons/triforce.webp) `Jednotné plochy` - Upřednostní trojúhelníky podobné velikosti.
* ![](/icons/hole.webp)  `Díra` - Decimace se pokusí zachovat beze změny okraje u otevřené geometrie a otvorů.
* ![](/icons/group.webp) `SkupinaPovrch` - Decimace se pokusí zachovat beze změny hranice skupin ploch.
* ![](/icons/uv.webp) `UV` - Decimace se pokusí zachovat beze změny hranice UV.

### Cílové trojúhelníky {#target-triangles}
Nastaví cílový počet trojúhelníků. Výchozí hodnota je 50 %, tlačítko procent/cíle přepíná mezi procentem a přesným cílovým počtem polygonů.

### Možnosti {#decimate-gear-menu}
Každá možnost má zaškrtávací pole pro zapnutí a hodnotu pro sílu:

#### ![](/icons/palette.webp) Zachovat malbu {#preserve-painting}
Hodnota určuje, jak přesně se zachová detail malby. Vyšší hodnoty zachovají více malby. Pokud vám na malbě nezáleží, nastavte 0.

#### ![](/icons/triforce.webp) Jednotné plochy {#uniform-faces}
Vyšší hodnoty dají trojúhelníky podobné velikosti.

#### Zachovat hranice {#preserve-borders}
Zabrání decimaci okrajů. Váhy okrajů lze nastavit pro hranice `Díra`, `SkupinaPovrch` nebo `UV` (`UV` vyžaduje objekt s UV).

## ![](/icons/quad.webp) Quad přesíťování {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Znovu postaví objekt s čistou sítí čtyřúhelníků. Tato karta nabízí několik přesíťovačů, každý s vlastním tlačítkem `Remesh`, posuvníkem `Cílové čtyřúhelníky` a nabídkou ozubeného kolečka. Vyzkoušejte je na svém objektu, výsledky se dost liší!

### Quad Remesher {#quad-remesher}
Stejný přesíťovač jako nástroj [Quad Remesher](tools.md#quad-remesher), vyvinutý společností [Exoside](https://exoside.com/). Je dostupný jen na některých platformách a je potřeba ho zakoupit: do té doby tlačítko `Remesh` ukazuje košík.

`Vybrat nástroj` přepne na nástroj Quad Remesher, kde můžete kreslit vodítka a malovat hustotu. Nabídka ozubeného kolečka obsahuje `Přizpůsobivý počet kvádrů`, `Adaptivní velikost` (při 100 % se velikost čtyřúhelníků řídí zakřivením, při 0 % jsou čtyřúhelníky stejně velké), `Automatické zjišťování tvrdých hran` a `Znovuprojektovat vrchol`.

::: tip
Tam, kde je dostupný, dává Quad Remesher obecně nejlepší výsledky a nejvíc kontroly.
:::

### AutoRemesher {#autoremesher}
Alternativní přesíťovač na čtyřúhelníky s možnostmi, jak přizpůsobit velikost a tvar čtyřúhelníků povrchu.

#### ![](/icons/cog.webp) Nabídka ozubeného kolečka AutoRemesheru {#autoremesher-gear-menu}
Nabídka ozubeného kolečka obsahuje tyto pokročilé možnosti:

##### Měřítko hran {#edge-scaling}
Mění velikost čtyřúhelníků, vyšší hodnoty dávají větší čtyřúhelníky.

##### Adaptivita {#adaptivity}
Přizpůsobí hustotu čtyřúhelníků zakřivení. 0 dává stejně velké čtyřúhelníky, 1 menší čtyřúhelníky v zakřivených oblastech.

##### Anizotropie {#anisotropy}
Protáhne čtyřúhelníky ve směru, kde je povrch nejplošší. 0 dává čtvercové čtyřúhelníky, 1 protáhlé čtyřúhelníky na trubicích a hřebenech.

##### Ostrá hrana {#sharp-edge}
Hrany ohnuté víc, než je tento úhel, se zachovají jako ostré prvky.

##### Vyhlazení normál {#smooth-normal}
0 ponechá povrch během přesíťování fasetovaný. Vyšší hodnoty povrch vyhladí s ohledem na normály vrcholů.

##### Maximální vyplnění otvorů {#autoremesher-max-fill-hole}
Algoritmus někdy vytvoří nechtěné otvory. Pokud má otvor méně vrcholů než tato hodnota, vyplní se.

### Instant Mesh {#quad-remesh-instant}
Přesíťuje pomocí [algoritmu Instant Meshes od autorů Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analyzuje tok sítě a vytvoří čistou topologii ze čtyřúhelníků.

#### Remesh {#instant-remesh}
Spustí přesíťování.

#### Cílové čtyřúhelníky {#target-quads}
Počet čtyřúhelníků, který se přesíťovač pokusí vytvořit.

#### ![](/icons/cog.webp) Nabídka ozubeného kolečka Instant Mesh {#quad-remesh-instant-gear-menu}
Nabídka ozubeného kolečka obsahuje tyto pokročilé možnosti:

##### Úhel záhybu {#crease-angle}
Práh pro ostré rohy, který pomáhá vést přesíťování. Zapnete ho jeho zaškrtávacím polem.

##### Maximální vyplnění otvorů {#max-fill-hole}
Algoritmus někdy vytvoří nechtěné otvory. Pokud má otvor méně vrcholů než tato hodnota, vyplní se.

### QuadriFlow {#quadriflow}
Přesíťuje pomocí algoritmu QuadriFlow, dalšího způsobu, jak získat čistou síť ze čtyřúhelníků.

#### ![](/icons/cog.webp) Nabídka ozubeného kolečka QuadriFlow {#quadriflow-gear-menu}
Nabídka ozubeného kolečka obsahuje tyto pokročilé možnosti:

##### Zachovat hranice {#quadriflow-preserve-boundary}
Chrání okraje otvorů.

##### Zachovat ostré hrany {#keep-sharp}
Zarovná čtyřúhelníky s ostrými hranami povrchu.

##### Tok s minimálními náklady {#min-cost-flow}
Pro rozložení čtyřúhelníků použije řešič toku s minimálními náklady. Je pomalejší, ale může dát pravidelnější topologii.

## ![](/icons/uv.webp) Rozbalení UV {#uv-unwrap}
Vypočítá texturovací souřadnice (UV) vybraného objektu. Nomad nabízí dvě metody, `UVAtlas` a `BFF`, každou s vlastním tlačítkem `Rozbalit`.

![](/videos/unwrap.mp4)

::: tip UV?
UV se často přirovnávají k balení dárku: jak nejlépe nastříhat balicí papír, aby zakryl celý předmět bez překrývání?

S UV je to podobné, jen místo papíru stříháte objekt. Představte si, že je váš model z tenkého plastu: jak byste ho rozstříhali, abyste ho rozložili naplocho, v tomto plochém stavu na něj malovali a pak ho zase složili dohromady?

Teď si představte, že povrch modelu je z pružné lycry. Model byste mohli natáhnout naplocho, rozstříhat, nebo obojí. Ale kdybyste na rozložený objekt namalovali šachovnici, po složení by byla zdeformovaná. Co je lepší: víc střihů a menší deformace, nebo méně střihů a větší deformace?

UV jsou pokyny, které 3d softwaru říkají, jak objekt při nanášení textur „rozstříhat a natáhnout“. Nástroj UV Atlas obecně volí přístup „víc střihů, menší deformace“.


:::

::: tip UV, Nomad a jiné aplikace

Většina texturovaných modelů, které najdete na internetu, má textury nanesené pomocí UV. Nomad je umí importovat a zobrazit přes panel [materiálu](material.md#textures).

Modely vytvořené v Nomadu můžete malovat přímo i bez UV. Pokud je potřebujete exportovat do jiných aplikací, např. do [Procreate](https://procreate.art/), můžete barevné informace z Nomadu „zapéct“ do textur pomocí UV.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas obecně dává přednost více ostrovům se střihy, aby minimalizoval deformace.

#### Rozbalit {#unwrap}
Vypočítá UV vybraného objektu.

#### Možnosti {#uvatlas-gear-menu}
Tlačítka vedle `Rozbalit`:

##### SkupinaPovrch {#atlas-face-group}
Když ukazuje `Ano`, určují střihy UV skupiny ploch. Toto nastavení je společné s BFF.

##### Smazat UV {#delete-uvs}
Tlačítko s košem smaže UV objektu.

##### Kontrola {#uv-inspect}
Zobrazí UV objektu na pozadí.

#### Maximální protažení {#max-stretch}
Nízké hodnoty dávají menší deformace a víc ostrovů, vysoké hodnoty větší deformace a méně ostrovů.

#### Rozestup ostrovů {#island-spacing}
Velikost mezery mezi ostrovy. Nízké hodnoty plýtvají méně místem, ale hrozí, že textury budou mezi ostrovy prosakovat.

::: warning
Výpočet UV může chvíli trvat, nejlépe je mít síť s méně než 100k vrcholy.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV metodou BFF dávají přednost přístupu „méně střihů, větší deformace“.

#### Možnosti {#uv-bff-gear-menu}
Vedle `Rozbalit` jsou stejná tlačítka `SkupinaPovrch`, smazání a `Kontrola` jako u [UVAtlas](#uvatlas-gear-menu).

##### SkupinaPovrch {#bff-face-group}

Střihy UV určí skupiny ploch.

#### Počet kuželů {#cone-count}
Určuje počet použitých hlavních projekcí. Nižší hodnoty dávají méně ostrovů, ale větší deformace. Vyšší hodnoty se déle počítají.

#### Bezešvé záplaty {#seamless-patches}
Ovlivňuje rozložení UV záplat a může způsobit výrazné deformace. Nejlépe funguje s pečlivě vytvořenými skupinami ploch.

::: warning
BFF může vytvořit překrývající se UV, pokud má síť ucha (jako je díra donutu).
:::

### ![](/icons/preview.webp) Zobrazit UV po rozbalení {#show-uv-after-unwrap}
Po rozbalení otevře zobrazení kontroly UV, takže výsledek hned zkontrolujete.

### ![](/icons/bake.webp) Péct: Textura → Textura {#unwrap-bake-texture}
Dostupné jen tehdy, když má materiál objektu textury. Když objekt znovu rozbalíte, textury se přenesou na nové UV, takže dál sedí. Rozlišení je ve výchozím stavu `Auto` a odpovídá největší textuře, nebo ho můžete nastavit sami.

## ![](/icons/bake.webp) Péct {#bake}
Tato karta přenáší detaily a malbu mezi objekty a mezi vrcholy a texturami.

`Z vysokého rozlišení` používá jako zdroj jiné objekty, číslo v závorce udává jejich počet. Nomad je vybírá takto:

- použijí se všechny vybrané objekty a cílem je hlavní vybraný objekt (nejvýrazněji zvýrazněný v nabídce [Scéna](scene.md))
- pokud je vybraný jen jeden objekt, Nomad místo toho použije všechny viditelné objekty
- pokud jsou všechny ostatní objekty skryté (například pomocí Sólo), použije se celá scéna

### ![](/icons/bake.webp) Péct → Textura {#bake-texture}
![](/images/topology_bake_menu.webp)

Zapékání textur vytvoří textury promítnutím ostatních viditelných objektů scény do UV vybraného objektu. Objekt musí mít UV.

Typický postup zapékání:
- Máte síť s jemnými detaily a malbou
- Naklonujte ji
- Decimujte ji (`Zachovat malbu` nastavte na 0)
- Rozbalte její UV
- Zapečte ji!

Teď byste měli mít síť s nízkým rozlišením, která si zachovává většinu malby a detailů původního objektu.

Po operaci se barvy vrcholů přesunou do nové vypnuté vrstvy, aby se netloukly s texturami.

#### Ze stejného objektu {#tex-from-itself}
Zapeče objekt do jeho vlastních UV: z jeho malby se stanou textury, a pokud má úrovně multirezoluce, zapečou se detaily nejvyšší úrovně do té aktuální (na tlačítku se pak zobrazí ikona multirezoluce). Nastavení je jednoduché, ale často budete potřebovat víc kontroly a pak se víc hodí další možnost.

#### Z vysokého rozlišení {#tex-from-high-res}
Zapeče ostatní objekty do vybraného objektu. Číslo v závorce udává počet ostatních objektů, které se použijí jako zdroje s vysokým rozlišením a zapečou se do aktuálního objektu s nízkým rozlišením a UV. Ostatní objekty nemusí mít podobné rozložení ani topologii jako zapékaný objekt, což umožňuje všestranné postupy zapékání.

#### Rozlišení {#tex-bake-resolution}
Rozlišení zapečené textury. Zapečené textury jsou vždy čtvercové, takže 1024 vytvoří obrázek 1024x1024.

Tlačítka pod ním jsou zkratky pro často používaná rozlišení. Pro představu: 512x512 je poměrně malé, třeba pro webovou grafiku a jednoduchou geometrii. 4096x4096 (zkráceně 4k) je pro vysoce kvalitní rendery.

#### Barva, Drsnost, Kovovost, Normála, Posunutí, Emise, Krytí {#tex-normal-roughness-metalness-color-emissive-opacity}
Tato tlačítka určují, které vlastnosti se zapečou, každá do samostatné mapy. Po dokončení zapékání se přidají jako textury do materiálu aktuálního objektu. `Posunutí` zapeče výšku detailů jako mapu posunutí (displacement).

#### ![](/icons/cog.webp) Nabídka ozubeného kolečka zapékání {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Nabídka ozubeného kolečka obsahuje tyto pokročilé možnosti:

##### Záloha {#tex-backup}
Abyste viděli náhled zapečených textur, musí být malba objektu vypnutá. `Záloha (Malování → Vrstva)` přesune veškerou malbu do nové vrstvy jako zálohu, kterou pak snadno zapnete nebo vypnete.

##### Použít multires {#tex-use-multires}
Pro `Ze stejného objektu` u objektu s úrovněmi multirezoluce. Nomad čte vysoké rozlišení přes úrovně dělení místo vrhání paprsků: je to rychlejší a bez chyb projekce. Vypněte to, chcete-li zapékat s níže uvedenými možnostmi.

##### Hladká základna {#tex-smooth-base}
Pro `Posunutí` u objektu s úrovněmi multirezoluce. Měří posunutí od rozdělené základny místo od jejích plochých ploch. Nechte zapnuté, když mapa posunutí půjde na dělenou síť, třeba s adaptivním dělením v Blenderu.

##### Vyhledávací vzdálenost {#tex-cage-radius}
Maximální vzdálenost, ve které se hledá zdrojový povrch. Ve výchozím stavu je nízká, aby nevznikaly artefakty, ale můžete ji zvýšit, pokud jsou cílové objekty od zapékaného objektu daleko.

##### Projekce {#tex-projection}
Jak se hledá zdrojový povrch:

* `Paprsek` - Promítá podél normály povrchu.
* `Paprsek + nejbližší` - Použije paprsek podél normály, a když mine, použije nejbližší povrch.
* `Nejbližší` - Promítá do nejbližšího bodu zdrojového povrchu.

##### Posunutí paprsku {#tex-ray-offset}
Upraví, odkud na zapékaném objektu výpočty zapékání začínají. Malé odsazení od povrchu zabrání většině běžných artefaktů. Pokud jsou cílové objekty od zapékaného objektu velmi daleko, může být potřeba odsazení zvětšit. `Nejbližší` ho nepoužívá.


### ![](/icons/bake.webp) Přeprojektovat → Vrchol {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Promítne vysochané detaily, malbu, vrstvy a textury do hodnot vrcholů.

Dá se to chápat jako opak zapékání: zapékání přenáší vlastnosti vrcholů do textur, přeprojektování přenáší textury (a další vlastnosti)
 zpět do vrcholů.

::: tip
Při použití `Péct → Textura` nebo `Přeprojektovat → Vrchol` se berou v úvahu barvy vrcholů i textury materiálu.
:::

#### Ze stejného objektu {#vertex-from-itself}
Převede textury z materiálu na hodnoty vrcholů. Tlačítko je aktivní jen tehdy, když má objekt UV a v materiálu jsou aktivní textury.

::: tip TIP: Malování textur
Nomad přímo nepodporuje malování a úpravy textur, ale velmi podobného výsledku dosáhnete tak, že textury promítnete do hodnot vrcholů, malujete na vrcholy a pak vrcholy zapečete zpět do textur:

1. Připravte objekt s nízkým počtem polygonů a s UV
1. Načtěte textury do jeho materiálu
1. Rozdělte ho natolik, aby se na něj dalo malovat
1. `Přeprojektovat → Vrchol` v režimu `Ze stejného objektu`, textura se teď převedla na hodnoty vrcholů
1. Malujte, vyhlazujte, rozmazávejte, razítkujte, upravte, co potřebujete
1. `Péct → Textura` v režimu `Ze stejného objektu`. Úpravy se převedou zpět do textur.
:::

#### Z vysokého rozlišení {#vertex-from-high-res}
Převede ostatní objekty na hodnoty vrcholů vybraného objektu. Číslo na tlačítku udává počet zdrojových objektů. Je to určené hlavně pro použití na síti s vysokým rozlišením, typicky s čistou topologií.

::: tip
Přeprojektování jiných objektů neslouží jen k přenosu barev, ale i k promítnutí vrcholů na jiné objekty, např. obvazy lze promítnout na postavu.
:::

#### Vrcholky, Barva, Drsnost, Kovovost, Krytí, Maska, Vrstvy, SkupinaPovrch {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Tato tlačítka určují, které vlastnosti se promítnou na vybraný objekt. `Vrstvy` přenese ostatní vrstvy na vybranou síť.

#### ![](/icons/cog.webp) Nabídka ozubeného kolečka přeprojektování {#vertex-reproject-gear-menu}
Nabídka ozubeného kolečka obsahuje tyto pokročilé možnosti:

##### Krytí → Maska {#vertex-opacity-to-mask}
Převede krytí zdroje na masku na vybraném objektu.

##### Iterace {#vertex-iterations}
Kolikrát se během přeprojektování použije uvolnění. Používá se jen při zapnutém `Vrcholky`.

##### Uvolnit {#vertex-relax}
Rozložení vybrané sítě lze do jisté míry vyhladit nebo uvolnit, aby lépe sedla na cíle přeprojektování. `Hladit` je lepší pro sítě s vysokým počtem polygonů, `Uvolnit` pro sítě s nízkým počtem polygonů. `Auto` nechá Nomad vybrat nejlepší metodu.

##### Vyhledávací vzdálenost {#vertex-cage-radius}
Maximální vzdálenost, ve které se hledá zdrojový povrch. Ve výchozím stavu je nízká, aby nevznikaly artefakty, ale můžete ji zvýšit, pokud jsou cílové objekty od vybraného objektu daleko.

##### Projekce {#vertex-projection}
Jak se hledá zdrojový povrch:

* `Paprsek` - Promítá podél normály povrchu.
* `Adaptivní směs` - Míchá paprsek podél normály a nejbližší povrch podle vzdálenosti a `Preference paprsku`. Když jeden mine, použije druhý.
* `Nejbližší` - Promítá do nejbližšího bodu zdrojového povrchu.

##### Preference paprsku {#vertex-ray-bias}
Jen pro `Adaptivní směs`. Vyšší hodnoty posouvají směs k výsledku paprsku podél normály, nižší k nejbližšímu bodu.

##### Posunutí paprsku {#ray-vertex-offset}
Upraví, odkud na vybraném objektu výpočty začínají. Malé odsazení od povrchu zabrání některým artefaktům. Pokud jsou cílové objekty od zapékaného objektu velmi daleko, může být potřeba odsazení zvětšit. `Nejbližší` ho nepoužívá.

### ![](/icons/bake.webp) Péct → VDM {#bake-vdm}
Vytvoří z vybraného objektu VDM razítko (vektorové posunutí) a přidá ho do knihovny VDM. Budete požádáni o název.

Typický postup:
- Přidejte rovinu, nebo ve výběru VDM zvolte `Nový VDM`, čímž přidáte už nastavenou rovinu (primitivum [VDM](scene.md#add-menu))
- Vysochejte na ní svůj tvar a okraj nechte rovný
- Zapečte ji!

Zapékaný čtverec určují UV roviny, takže objekt musí mít UV. Velikost razítka zvolíte pomocí `Rozlišení` a tlačítky `Barva`, `Drsnost`, `Kovovost` a `Krytí` určíte, co razítko kromě posunutí ponese.

::: tip
Na rovině nepoužívejte DynTopo, poškodí její UV a razítko vyjde zdeformované. Nejpřesnější výsledek dá sochání ve vrstvě, protože plochá rovina pod ní zůstane. Malování také potřebuje vrstvu, jinak se materiál otiskne přes celý čtverec, ne jen tam, kde jste malovali.
:::

## ![](/icons/dot.webp) Primitiva {#primitive}
Parametry vybraného primitiva. Většina z nich je dostupná i přes tlačítko `…` na panelu nástrojů primitiva ve viewportu.

![](/images/topology_primitive_screenshot.webp)
