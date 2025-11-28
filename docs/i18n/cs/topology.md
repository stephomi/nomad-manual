# ![](/icons/multires.webp) Topologie {#topology}

Tato nabídka ovládá topologii objektů v Nomadu, stejně jako nástroje pro „pečení“ a přenos detailů mezi objekty a mezi texturami.

![](/images/topology_overview.webp)

Nomad je založený na polygonech, používá trojúhelníky a čtyřúhelníky (quady) pro práci s geometrií.
Topologií myslíme jak počet ploch, tak způsob, jakým jsou body (vrcholy) propojené.

Je důležité mít přehled o topologii, obzvlášť pokud chcete model detailně sochat nebo malovat.

::: tip Jak sledovat svou topologii?
Můžete zobrazit [drátěný model (Wireframe)](settings.md#wireframe) nebo jednoduše vypnout [hladké stínování (Smooth Shading)](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Nabídka Topology v Nomadu má několik sekcí:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Úprava více úrovní detailu pomocí subdivize                      |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Přepočítá novou topologii s rovnoměrnou hustotou                 |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Lokální přidávání/odebírání ploch v reálném čase při sochání či malbě |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimace, UV, baking, remeshing, reprojekce                      |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Možnosti primitiv                                                |


## Počty polygonů {#polygon-stats}

![](/images/topology_stats.webp)

Horní část nabídky Topology zobrazuje informace o polygonech pro vybraný objekt a celou scénu. Čísla ukazují celkový počet vrcholů, celkový počet trojúhelníků a celkový počet quadů (4stranných polygonů).

Klepnutím na tuto sekci zobrazíte seznam statistik polygonů pro všechny polygonální objekty ve scéně.

## ![](/icons/multires.webp) Multirezoluce {#multiresolution}

![](/images/topology_multires_menu.webp)

### Co je multirezoluce? {#what-is-multiresolution}
Funkce multiresolution je užitečná hlavně ve dvou scénářích:
- Hladký subdivizní algoritmus pro zvýšení počtu polygonů objektu
- Práce s více úrovněmi rozlišení, abyste mohli střídat úpravy v malém a velkém měřítku

![](/videos/multiresolution.mp4)

#### Postup práce s multirezolucí {#multiresolution-workflow}
Důležitým aspektem multiresolution je, že se můžete vrátit na nižší rozlišení, provést změny na objektu a pak se vrátit na nejvyšší rozlišení bez ztráty detailů ve vysokém rozlišení. Všechny detaily ve vysokém rozlišení budou automaticky promítnuty (projektovány).

::: warning
Pokud používáte nástroj, který mění topologii objektu, přijdete o všechny ostatní úrovně rozlišení objektu!
Vždy byste měli dostat varování v případě, že se to má stát, například když používáte:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim tool](tools.md#trim)
- [Split tool](tools.md#split)
:::


### Posuvník multirezoluce {#multiresolution-slider}
Tento posuvník ukazuje počet úrovní subdivize v aktuálním objektu. Pokud je zde 6 svislých pruhů, existuje 6 úrovní subdivize. Kroužek označuje aktuálně zobrazenou úroveň subdivize. 

### Obrátit {#reverse}
Na nejnižší úrovni subdivize se tlačítko Reverse pokusí vytvořit úroveň pod tou aktuální. Obecně to lze provést jen tehdy, pokud byl objekt od začátku vytvořen pomocí subdivize, například v Nomadu nebo v jiných 3D aplikacích, které používají multiresolution subdivision surfaces.

### Subdividovat {#subdivide}
Tlačítko *Subdivide* zvýší počet polygonů 4×, proto sledujte počet polygonů, protože může velmi rychle narůstat!
Důležitým aspektem *Subdivision Surface* je, že konvergují k *hladkému povrchu (Smooth Surface)*.
Pro pochopení fungování můžete zkusit tlačítko *Subdivide* na objektu s jen několika málo polygony.

Toto *Smooth* chování můžete vypnout zaškrtnutím volby `Linear subdivision`.

### Smazat nižší {#delete-lower}
Pokud existují subdivize pod aktuálně zobrazenou úrovní, smaže je. Pokud to uděláte omylem, můžete je znovu vytvořit tlačítkem Reverse.

### Smazat vyšší {#delete-higher}
Pokud existují subdivize nad aktuálně zobrazenou úrovní, smaže je.

### Lineární subdivize {#linear-subdivision}
Subdividuje mesh bez aplikace vyhlazování.

### Ostrý okraj {#sharp-border}
Pokud má objekt facegroupy, zapnutí této volby udrží hranice facegroup ostré. Lze nastavit na každé úrovni subdivize (na posuvníku subdivize se nad úrovní zobrazí malá ikona jako indikace).

### Zachovat trojúhelníky {#keep-triangles}
Většina standardních systémů subdivision surface se při subdivizi snaží převést všechny polygony na quady. Toto přepínání vynutí, aby subdivize používala trojúhelníky.

### Zamknout (LV0) {#lock-lv0}

Zabrání úpravám nejnižší úrovně subdivize. To může být důležité, pokud byl objekt vygenerován v jiné aplikaci a základní objekt musí zůstat nezměněn. Když je tato volba vypnutá, velké změny provedené na vyšších úrovních subdivize budou posouvat i úroveň 0.

::: tip 

Subdivize ve výchozím nastavení vyhladí všechny ostré hrany. Pokud chcete hrany ponechat mírně ostré, zkuste použít lineární subdivizi nebo Sharp border na prvních 2 úrovních subdivize a pak je na vyšších úrovních vypnout. Vznikne tak polovičně ostrý subdividovaný mesh.

:::


## ![](/icons/voxel.webp) Voxelový remesher {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Při použití `Voxel Remesher` bude celá síť (mesh) přinucena mít jednotné rozlišení topologie, což znamená, že všechny polygony mají víceméně stejnou velikost. To je velmi užitečné, když nechcete přemýšlet o topologii a chcete jen volně sochat.

Typický sochařský workflow může začít použitím `Voxel Remesher` pro nahrubé „block-out“ tvaru s nízkým rozlišením.
Jednoduše občas stiskněte tlačítko *Remesh*, když síť příliš natahujete, abyste se vyhnuli velkému zkreslení.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Jak bylo uvedeno výše, Nomad je polygonální software, ale `Voxel Remesher` je výjimka, kde se (dočasně) používá jiný přístup k provedení remeshingu.

Velký rozdíl je v tom, že voxelový přístup nepřijímá samo-průniky (self intersection), takže ty budou vyřešeny.
Také nepodporuje mesh s dírami.

Dírami zde nemyslíme `genus hole` (`díru` v donutu), ale mesh, který není `vodotěsný`/`uzavřený`.
Typicky to znamená, že před aplikací remeshingu budou všechny díry vyplněny, podobně jako u [Trim tool](tools.md#trim) nebo [funkce vyplnění děr (Hole filling)](scene.md#hole-filling).
:::

### Remesh {#voxel-remesh}
Spustí voxelový remesh.

### Rozlišení {#voxel-resolution}
Velikost voxelů použitých během výpočtu. Při změně tohoto parametru se na mesh překryje šachovnicový vzor, který poskytne náhled výsledku.

### Vytvořit multirezoluci {#build-multiresolution}
Vytvoří nižší úrovně multiresolution pro voxelový remesh. Pokud použijete šachovnicový vzor k nastavení rozlišení a nastavíte build multiresolution na 2, konečný výsledek bude mít detail odpovídající posuvníku rozlišení a v záložce multires bude na úrovni 2, což znamená, že máte nižší multires meshe na úrovni 1 a 0. To může být dobrý způsob, jak vygenerovat čistý mesh s rovnoměrnými polygony a zároveň mít nízko-poly řídicí mesh.

::: tip Tip: Build multiresolution a stable smoothing

Tato volba může někdy způsobit „smyčky“ v geometrii, které se těžko vyhlazují a vytvářejí malé pupínky. Pokud se to stane, zapněte 'Stable smoothing' v nastavení nástroje Smooth. 

:::

### Zachovat ostré hrany {#keep-sharp-edges}
Zapne přichytávání nových bodů k ostrým hranám původního meshe. Může to zavést zkreslení.

## ![](/icons/dynamic.webp) Dynamická topologie {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution a voxel remeshing jsou běžné průmyslové metody pro kontrolu topologie, ale obě vyžadují, abyste hlídali, zda polygony příliš nenatahujete nebo příliš nestlačujete. 

Dynamic Topology je alternativní metoda. Při sochání Nomad adaptivně přidává a odebírá polygony během tahu štětcem, takže vyřezávání malých detailů přidá mnoho malých polygonů tam, kde je potřebujete, a vyhlazování jinde polygony odebírá.

Všimněte si, že dynamic topology používá trojúhelníkové polygony místo quadů. Může to vypadat trochu nepořádně, ale je téměř lepší na drátěný model nekoukat, jen se soustředit na pěkně vypadající sochu bez starostí o topologii, a později použít některý z dalších remeshing nástrojů Nomadu k vygenerování čisté quad sítě.

Podívejte se na video níže v akci.

![](/videos/dynamic.mp4)

### Zapnuto {#enabled}
Zapne dynamic topology. Ikona DynTopo bude umístěna pod posuvníky poloměru a intenzity štětce, aby bylo možné Dyntopo přepínat pro každý nástroj zvlášť.

### Detail {#dyn-detail}
Ovládá množství detailu, jeho chování se mění podle volby 'Detail based on...', viz níže.

### Detail založený na... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Úroveň detailu závisí na tom, jak velký je objekt na obrazovce. Posuvník detailu je 100 % a více pro jemný detail (malé trojúhelníky) nebo 1 % pro nízký detail (velké trojúhelníky).  |
| Radius   | Poloměr nástroje definuje množství detailu. Malý poloměr nástroje pro jemný detail, velký poloměr pro nízký detail. Posuvník detailu je násobitel tohoto poměru.                     |
| Constant | Posuvník detailu definuje množství detailu a není ovlivněn velikostí obrazovky ani velikostí nástroje.             |

::: tip TIP: Radius mode

Abyste lépe pochopili, jak funguje režim Radius, začněte jedním prstem posouvat posuvník detailu a zároveň druhým prstem měňte poloměr nástroje. Uvidíte, jak jsou propojené.

:::

### Preferovat... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Upřednostnit výkon |
| Quality | Upřednostnit kvalitu     |

Když upřednostníte `Quality`, jsou zde 2 hlavní rozdíly:
- zpřesnění (refinement) se aplikuje před socháním, takže při malování nebo sochání velmi malých detailů dostanete méně interpolačních artefaktů
- zpřesnění běží, dokud nekonverguje na správnou úroveň detailu, na rozdíl od inkrementálního chování.
 
Díky tomu, pokud socháte velmi malé detaily nebo děláte rychlé tahy, bude topologie vždy zpřesněna podle očekávání.


### Použít tlak na poloměr {#use-pressure-on-radius}
Relevantní pouze pokud je aktivní `Radius`. Když je zapnuto, úroveň detailu bude vždy odrážet velikost štětce, i když je velikost štětce ovlivněna tlakem pera.

### Použít plynulost tahu {#use-stroke-falloff}

Do výpočtů dyntopo zahrne také křivku doznění (falloff) štětce a alfu.

### Metoda {#method}
Ať už používáte `Dynamic Topology` na [Brush](#brush) nebo [Globally](#global), můžete zvolit režim, ve kterém pracuje:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Může přidávat i odebírat plochy, to je režim použitý ve videu výše     |
| Subdivision    | Přidává nové plochy, nemůže plochy odebírat                            |
| Decimation     | Odebírá plochy, nemůže plochy přidávat                                 |

### Chránit maskovanou oblast {#protect-masked-area}
Zapne ochranu zamaskovaných oblastí před změnou topologie.

### Extrapolace vrcholů {#vertex-extrapolation}


### Detail {#all-detail}
Rozlišení použité pro operaci remesh. Pokud je Dyntopo v režimu 'Constant', bude to stejná hodnota jako posuvník Detail v horní části této nabídky.

### Remesh {#dyn-remesh}
Spustí globální remesh pomocí algoritmu dyntopo. Obvykle byste pro plný remeshing měli použít [Voxel Remesher](#voxel-remesher).

Jedna výhoda oproti voxelům je však ta, že zamaskovaná oblast bude chráněna, takže máte lepší kontrolu nad tím, kde mít větší či menší hustotu.



## ![](/icons/topo_extra.webp) Různé {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu ozubeného kola {#gear-menu}
Mnoho nástrojů v této nabídce má další volby. K nim se dostanete přes ikonu ozubeného kola vedle názvu sekce.

### Decimace {#decimation}

![](/images/topology_decimation.webp)

Sníží počet polygonů při snaze zachovat co nejvíce detailů, s použitím trojúhelníkových polygonů.

Tato funkce může být užitečná, pokud chcete exportovat pro 3D tisk.
Neměli byste ji však pravděpodobně používat, pokud chcete na modelu dál sochat, protože může vytvářet nerovnoměrné trojúhelníky.

Všimněte si, že zamaskované oblasti nebudou decimovány.

![](/videos/decimate.mp4)

::: tip

Použití [Quadremesh tool](tools.md#quad-remesher) na vysoce polygonálních objektech může trvat dlouho a dávat výsledky, které se těžko kontrolují. Předzpracování meshe pomocí [facegroups](tools.md#facegroup-1) a decimate způsobí, že Quadremesh poběží mnohem rychleji a umožní mnohem větší kontrolu nad topologií.

* Označte mesh facegroupy tak, aby definovaly ideální tok quadů.
* Použijte Facegroup relax pro vyhlazení hranic facegroup.
* Proveďte Decimate. Tím zajistíte, že na hranách facegroup nebudete mít tenké nebo zkreslené plochy. V nastavení decimate se ujistěte, že je facegroup zapnutá. Tím se hrany trojúhelníků přesně přizpůsobí hranám facegroup.
* V možnostech Quadremesh se ujistěte, že je relax vypnutý (protože jste mesh už vyhladili) a měli byste dostat dobré výsledky.

:::

#### Decimovat {#decimate}
Spustí operaci decimate.

Ikony vedle tlačítka decimate umožňují přepínat volby, které ovlivňují decimaci. Procento udává, jak silně je daná volba uplatněna, a lze jej nastavit v rozšířeném gear menu.

* ![](/icons/palette.webp)  `Preserve Painting` - Umístí více trojúhelníků tam, kde je detail v malbě.
* ![](/icons/triforce.webp) `Uniform Faces` - Preferuje vytváření rovnoměrně velkých trojúhelníků.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate se pokusí zachovat hranice u otevřené geometrie a děr beze změny.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate se pokusí zachovat hranice facegroup beze změny.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Decimate se pokusí zachovat UV hranice beze změny.

#### ![](/icons/cog.webp) Menu decimace (ozubené kolo) {#decimate-gear-menu}
Gear menu má tyto pokročilé volby:
##### Zachovat malbu {#preserve-painting}
Zaškrtávací políčko přepíná tento režim, hodnota určuje, jak přesně bude zachován detail malby. Vyšší hodnoty zachovají více malby. Nastavte na 0, pokud vám na malbě nezáleží.


##### Rovnoměrné plochy {#uniform-faces}
Zaškrtávací políčko přepíná tento režim. Vyšší hodnoty vytvoří trojúhelníky podobné velikosti.

##### Zachovat okraje {#preserve-borders}
Zapněte, aby se hranice nedezimovaly. Váhy hranic lze zvolit pro hranice `Geometry`, `Face Group` nebo `UV`.

#### Cílový počet trojúhelníků {#target-triangles}
Nastaví cílový počet trojúhelníků. Výchozí hodnota je 50 %, tlačítko percent/target přepíná mezi procentem nebo přesným cílovým počtem polygonů.



### UV rozbalení - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Vypočítá texturové souřadnice (UV) pro aktuální mesh, obecně s preferencí vytvářet více ostrovů s řezy, aby se minimalizovalo zkreslení.

Malá ikona oka mezi názvem nabídky a gear menu přepíná náhled UV na objektu.

![](/videos/unwrap.mp4)

#### Rozbalit {#unwrap}
Spočítá UV pro vybraný objekt, které budou zobrazeny na pozadí.

#### Smazat UV {#delete-uvs}
Smaže UV na objektu.

#### ![](/icons/cog.webp) Menu UVAtlas (ozubené kolo) {#uvatlas-gear-menu}
Gear menu má tyto pokročilé volby:

#### Skupina ploch {#atlas-face-group}

Použije facegroupy k definování řezů pro UV.

##### Maximální protažení {#max-stretch}
Nízké hodnoty vytvářejí menší zkreslení a více ostrovů, vysoké hodnoty větší zkreslení a méně ostrovů. 

##### Rozestup ostrovů {#island-spacing}
Množství odsazení mezi ostrovy. Nízké hodnoty méně plýtvají místem, ale zvyšují riziko prolínání textur mezi ostrovy. 

::: warning
Výpočet UV může chvíli trvat, je nejlepší mít mesh s méně než 100k vrcholy.
:::

::: tip UVs?
Běžná analogie pro UV je balení dárku; jak nejlépe nastříhat balicí papír, aby zcela pokryl objekt bez překryvů? 

UV jsou podobné, ale místo stříhání papíru stříháte objekt. Představte si, že váš model je z tenkého plastu – jak byste ho rozstříhali, abyste ho rozvinuli do plochy, v této ploché podobě na něj malovali a pak ho znovu složili?

Teď si představte, že povrch modelu je z pružného lycra materiálu. Můžete model roztáhnout do plochy, nebo ho rozřezat, nebo kombinaci obojího. Ale pokud byste na objekt v plochém stavu namalovali šachovnici, po opětovném složení by byla šachovnice zkreslená. Co je lepší – více řezů s menším zkreslením, nebo méně řezů s větším zkreslením?

UV jsou instrukce, které říkají 3D softwaru, jak „řezat a natahovat“ objekt při aplikaci textur. Nástroj UV Atlas obecně používá přístup „více řezů, méně zkreslení“.


:::

::: tip UV's and Nomad and other apps

Většina texturovaných modelů, které najdete online, bude texturována pomocí UV. Nomad je umí importovat a zobrazit přes panel [material](material#textures).

Když jsou modely vytvářeny v Nomadu, můžete malovat přímo na objekty bez UV. Pokud je potřebujete exportovat do jiných aplikací, např. [Procreate](https://procreate.art/), můžete „péct“ barevné informace Nomadu do textur přes UV. 

:::

### UV rozbalení - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF UV preferují přístup „méně řezů, více zkreslení“. 

#### ![](/icons/cog.webp) Menu UV BFF (ozubené kolo) {#uv-bff-gear-menu}

#### Skupina ploch {#bff-face-group}

Použije facegroupy k definování řezů pro UV.

##### Počet kuželů {#cone-count}
Definuje počet hlavních projekcí použitých při unwrapu. Nižší hodnoty vytvoří méně ostrovů, ale více zkreslení.

##### Bezešvé patche {#seamless-patches}
Ovlivňuje rozložení UV „patchů“, nejlépe funguje s pečlivě vytvořenými facegroupami.

### Bake -> textura {#bake-texture}
![](/images/topology_bake_menu.webp)

Texture baking vytvoří textury projekcí ostatních viditelných objektů ve scéně do UV vybraného objektu.

Typický workflow pro baking je následující:
- Máte mesh s jemnými detaily a malbou
- Naklonujete ho
- Provedete decimate (nastavte `Preserve painting` na 0)
- Provedete UV unwrap
- Bake!

Nomad ve výchozím nastavení bere v úvahu všechny viditelné meshe ve scéně.
Můžete také použít Solo mód pro rychlé skrytí většiny ostatních meshů.
Pokud nejsou žádné jiné viditelné objekty, vezme se v úvahu celá scéna.

Nyní byste měli mít nízko-poly mesh, který zachovává většinu malby a detailů vašeho původního objektu.

Po operaci budou barvy vrcholů přesunuty do nové vypnuté vrstvy, aby nezasahovaly do textur.

#### Ze sebe sama {#tex-from-itself}
Peče nejvyšší úroveň multiresolution do nejnižší úrovně na aktuálním objektu. To je jednoduché na nastavení, ale často budete potřebovat více kontroly, v takovém případě je užitečnější následující volba.

#### Z hi-res () {#tex-from-high-res}
Peče z ostatních viditelných objektů ve scéně do vybraného objektu. Číslo v závorkách udává počet ostatních viditelných objektů, které budou použity jako high-res cíle a upečeny do aktuálního low-res objektu s UV. Ostatní objekty nemusí být podobné v rozložení nebo topologii objektu, do kterého se peče, což umožňuje flexibilní workflow pro baking.

#### Rozlišení {#tex-bake-resolution}
Rozlišení upečené textury. Bake textury jsou vždy čtvercové, takže 1024 vytvoří obrázek 1024×1024. 

Tlačítka níže jsou zkratky pro běžně používaná rozlišení. Pro představu, 512×512 je relativně malé, např. pro webovou grafiku a jednoduchou geometrii. 4096×4096 (zkráceně 4k) je pro vysoce kvalitní rendery.

#### ![](/icons/cog.webp) Bake menu (ozubené kolo) {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Gear menu má tyto pokročilé volby:

##### Normál, Drsnost, Kovovost, Barva, Emise, Krytí {#tex-normal-roughness-metalness-color-emissive-opacity}
Tato zaškrtávací políčka určují, které vlastnosti budou upečeny, každá do samostatné mapy. Po dokončení bake budou tyto mapy přidány jako textury k materiálu aktuálního objektu.

##### Záloha {#tex-backup}
Aby bylo možné náhled upečených textur, měly by být informace o malbě objektu vypnuté. Tato volba přesune veškeré informace o malbě do nové vrstvy jako zálohu, aby je bylo možné snadno zapínat/vypínat.

#### Poloměr klece {#tex-cage-radius}
Upraví, jak daleko od objektu, do kterého se peče, jsou vysílány paprsky při hledání cílových objektů. Ve výchozím nastavení je tato vzdálenost nízká, aby se předešlo artefaktům, ale lze ji zvýšit, pokud jsou cílové objekty daleko od objektu, do kterého se peče.

##### Posun paprsku {#tex-ray-offset}
Upraví, odkud na objektu, do kterého se peče, začínají výpočty bake. Ve výchozím nastavení začínají 5 % od povrchu, což zabraňuje většině běžných artefaktů. Pokud jsou cílové objekty velmi daleko od objektu, do kterého se peče, může být nutné tento offset zvýšit.


### Reprojekce na vrcholy {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Promítne sochařské detaily, malbu, vrstvy a textury do hodnot vrcholů.

Můžete si to představit jako inverzi bakingu; pokud baking přenáší vlastnosti vrcholů do textur, reprojekce přenáší textury (a další vlastnosti)
 zpět do vrcholů.

::: tip
Při použití `Bake to texture` nebo `Reproject to vertex` se berou v úvahu jak barvy vrcholů, tak textury materiálu.
:::

#### Ze sebe sama {#vertex-from-itself}
Převede textury z materiálu do hodnot vrcholů. Toto tlačítko bude aktivní pouze tehdy, pokud má objekt UV a v materiálu jsou aktivní textury.

::: tip TIP: Texture painting
Nomad přímo nepodporuje malování a úpravu textur, ale velmi podobných výsledků lze dosáhnout projekcí textur -> hodnoty vrcholů, malováním na vrcholy a následným bake vrcholy -> textury:

1. Nastavte nízko-poly objekt s UV
1. Načtěte textury do jeho materiálu
1. Subdividujte ho dostatečně, aby se na něj dalo malovat
1. Proveďte `Reproject to vertex` v režimu `From itself`, nyní byla textura převedena na hodnoty vrcholů
1. Malujte, vyhlazujte, mazejte, razítkujte, dělejte jakékoli úpravy
1. Proveďte `Bake to texture` v režimu `From itself`. Tyto úpravy se převedou zpět do textur.
:::

#### Z hi-res () {#vertex-from-high-res}
Převede všechny viditelné objekty do hodnot vrcholů na vybraném objektu. Číslo na tomto tlačítku udává počet viditelných objektů.

::: tip
Reprojekce jiných objektů se dá použít nejen pro přenos barevných informací z jiných objektů, ale i pro projekci vrcholů na jiné objekty, např. obvazy lze promítnout na postavu.
:::

#### ![](/icons/cog.webp) Reproject menu (ozubené kolo) {#vertex-reproject-gear-menu}
Gear menu má tyto pokročilé volby:

#### Vrcholy, Drsnost, Kovovost, Barva, Krytí, Krytí->Maska, Maska, Vrstvy, Skupina ploch {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Tato zaškrtávací políčka určují, které vlastnosti budou promítnuty do vybraného objektu. 

#### Uvolnit {#vertex-relax}
Vybraný mesh může mít své rozložení vyhlazeno nebo „uvolněno“ (relax) do určité míry, aby lépe seděl na cíle reprojekce. Smooth je lepší pro high-poly meshe. Relax je lepší pro low-poly meshe. Auto nechá Nomad zvolit nejlepší metodu.

#### Iterace {#vertex-iterations}
Kolikrát má být operace relax aplikována během reprojekce.

#### Poloměr klece {#vertex-cage-radius}
Upraví, jak daleko od vybraného objektu jsou vysílány paprsky při hledání cílových objektů. Ve výchozím nastavení je tato vzdálenost nízká, aby se předešlo artefaktům, ale lze ji zvýšit, pokud jsou cílové objekty daleko od objektu, do kterého se peče.

#### Odchylka paprsku {#vertex-ray-bias}
Nižší hodnoty upřednostní projekci na nejbližší bod cílového povrchu. Vyšší hodnoty upřednostní průsečík s použitím normály povrchu. 

#### Posun paprsku {#ray-vertex-offset}
Upraví, odkud na vybraném objektu začínají výpočty bake. Ve výchozím nastavení začínají 5 % od povrchu, což zabraňuje určitým artefaktům. Pokud jsou cílové objekty velmi daleko od objektu, do kterého se peče, může být nutné tento offset zvýšit.


### Quad Remesh - Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remesh pomocí [algoritmu Instant Meshes od Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analyzuje tok meshe a vytváří čistou quad topologii.

::: tip
Na iOS a desktopu dává nástroj [Quad remesher](tools#quad-remesher) lepší výsledky a více kontroly.
:::

#### Remesh {#instant-remesh}
Spustí operaci instant meshes.

#### Cílové quady {#target-quads}
Počet quad polygonů, které se Quad Remesh pokusí vytvořit.

#### ![](/icons/cog.webp) Quad Remesh Instant menu (ozubené kolo) {#quad-remesh-instant-gear-menu}
Gear menu má tyto pokročilé volby:

##### Úhel zalomení {#crease-angle}
Práh ostrých rohů, který se pokusí pomoci vést operaci remesh.

#### Maximální vyplnění díry {#max-fill-hole}
Algoritmus může někdy vytvářet nežádoucí díry. Pokud má díra méně vrcholů než tato hodnota, bude vyplněna.

### Díry {#holes}
![](/images/topology_holes_menu.webp)
Většinu času bude váš objekt pravděpodobně vodotěsný, což znamená, že mesh je „uzavřený“.

Pokud má váš objekt díry, můžete je vyplnit. Všimněte si, že to funguje jen na „naivní“ díry, takže nemůže „svařit“ dva oddělené okraje.

![](/videos/hole_filling.mp4)

::: tip
Když spustíte Voxel remesher, všechny díry se automaticky uzavřou, ať už ho používáte na jednom nebo více meshech.
:::

#### Zavřít díry {#close-holes}
Spustí akci uzavření děr.

#### ![](/icons/cog.webp) Menu díry (ozubené kolo) {#holes-gear-menu}
Gear menu má tyto pokročilé volby:

##### Detail {#fill-detail}
Hustota polygonů použitá k vyplnění díry. Při tažení tohoto posuvníku se na modelu zobrazí šachovnicový vzor, který dá představu o velikosti trojúhelníků. Zaškrtávací políčko toto vypne a použije pouze existující body, což obvykle vytvoří dlouhé tenké trojúhelníky přes díru, které se těžko sochají.

##### Vyplnit nemanifold {#fill-non-manifold}
Pokusí se vyplnit non-manifold díry.

##### Skupina ploch {#fill-face-group}

Při vyplňování děr – má každá díra dostat vlastní facegroup (Auto), nebo mají všechny sdílet jednu facegroup (Off), nebo se facegroupy nemají vytvářet (On).

### Vynutit manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Pokusí se vyčistit non-manifold hrany. Může být užitečné pro externí software, který nepodporuje hrany sdílené více než 2 plochami.

#### Vyčistit {#clean}
Spustí akci čištění.
#### ![](/icons/cog.webp) Force manifold menu (ozubené kolo) {#force-manifold-gear-menu}
Gear menu má tyto pokročilé volby:

#### Smazat malé plochy {#delete-small-faces}
Práh použitý k odstranění a spojení malých polygonů.


### Triplanární {#triplanar}
![](/images/topology_triplanar_menu.webp)
Převede mesh na [triplanar](scene.md#triplanar) primitivum.
Pravděpodobně při tom ztratíte hodně detailů.

#### Vynutit kubické {#force-cubic}
Vynutí, aby triplanar byl krychle. Jinak se triplanar přizpůsobí nejbližší ohraničující krabici (bounding box) kolem objektu.

#### Převést {#convert}
Spustí akci triplanar.

#### Rozlišení {#triplanar-resolution}
Velikost voxelu použitá v operaci triplanar.

## ![](/icons/dot.webp) Primitiva {#primitive}
Parametry pro vybrané primitivum. Tyto volby jsou také dostupné v panelu nástrojů primitiva ve viewportu.

![](/images/topology_primitive_screenshot.webp)