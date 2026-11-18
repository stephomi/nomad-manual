# ![](/icons/scene.webp) Scéna {#scene}

V této nabídce spravujete objekty, světla, kamery a opakovače v Nomadu. Zobrazuje hierarchii scény jako stromovou strukturu, ve které můžete měnit mnoho vlastností objektů. Umožňuje také vytvářet nové objekty a různými způsoby objekty spojovat a rozdělovat.


![](/images/scene_menu_summary.webp)


## Panel zkratek {#shortcut-bar}
| Akce                   | Ikona                             | Popis                                                                                                               |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Přidat...](#add-menu) | ![](/icons/plus.webp)            | Zobrazí [nabídku Přidat](#add-menu) pro přidání objektu do scény                                                    |
| Smazat                 | ![](/icons/trash.webp)           | Smaže vybrané objekty. Jejich potomci zůstanou zachováni.                                                           |
| Zámek                  | ![](/icons/lock.webp)            | Vybrané objekty nepůjde vybrat ve viewportu. Ve stromové struktuře je vybrat stále můžete. Zamčením skupiny zamknete vše pod ní. Dalším klepnutím objekty odemknete. |
| [Spojit](#join)        | ![](/icons/merge.webp)           | Spojí vybrané objekty do jediného objektu beze změny geometrie                                                      |
| [Rozdělit...](#separate) | ![](/icons/separate.webp)      | Zobrazí okno [Rozdělit](#separate) pro rozdělení objektu na několik objektů. Opak spojení                          |
| [Booleovský...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Zobrazí okno [Booleovský](#boolean)                                                                     |
| Klonovat               | ![](/icons/clone.webp)           | Zduplikuje vybrané objekty do nových objektů                                                                        |
| Instance               | ![](/icons/link.webp)            | Zduplikuje vybrané objekty jako instance, takže úpravy tvaru jedné se projeví na všech instancích.                  |
| Zrušit instanci        | ![](/icons/unlink.webp)          | Převede instanci na samostatný tvar, takže se úpravy tvaru už nekopírují do ostatních instancí                     |
| Synchronizovat         | ![](/icons/checked.webp)         | Když je zaškrtnuté, operace se použijí na všechny instance vybraných objektů, nejen na ty vybrané. Je dostupné jen tehdy, když výběr obsahuje instance. Které operace se tímto zaškrtávacím polem řídí, určuje [karta Synchronizovat](#sync) v okně `Rozšířené`. |

::: tip
Když operace ovlivní i ostatní instance, zobrazí se na jejím tlačítku malá ikona řetízku.
:::


## Stromová struktura {#tree-view}
![](/images/scene_treeview.webp) 

Stromová struktura obsahuje objekty, skupiny, opakovače, světla a kamery scény. Vedle názvu sítě uvidíte počet jejích vrcholů a barevnou ikonu vrstvy, pokud má vrstvy. Každý řádek má tato tlačítka:

| Akce         | Ikona                      | Popis                    |
| :----------: | :------------------------: | :----------------------: |
| Název        | ![](/icons/pencil.webp)   | Přejmenuje objekt. Pokud je vybraný, přejmenují se najednou všechny vybrané objekty a přidá se k nim číslo. Dlouhým stiskem přejmenujete objekt i s jeho potomky. |
| Vybrat       | ![](/icons/checked.webp)  | Přepne výběr            |
| Viditelný    | ![](/icons/eye_open.webp) | Přepne viditelnost       |
| Nabídka      | ![](/icons/more.webp)     | Zobrazí [nabídku objektu](#object-menu) |

::: tip TIP: Rychlý výběr nebo skrytí mnoha objektů

Klepnutím na ikonu výběru přepnete jeden objekt, tažením svisle po sloupci výběru vyberete mnoho objektů. Totéž funguje se sloupcem viditelnosti.

Dlouhým stiskem ikony výběru nebo viditelnosti ovlivníte i potomky.

:::

### Záhlaví stromové struktury {#tree-view-header}

Řádek nad seznamem nabízí několik pomocníků:

* ![](/icons/sort_down.webp) - sbalí nebo rozbalí všechny skupiny najednou.
* ![](/icons/preview.webp) - přepne `Náhledy objektů`, malou vyrenderovanou miniaturu u každého objektu seznamu.
* ![](/icons/search.webp) - filtruje seznam podle názvu.

### Práce se stromovou strukturou {#tree-view-manipulation}

Dlouze stiskněte položku ve stromové struktuře, dokud se nezvýrazní. Pak ji můžete posunout nahoru nebo dolů, nebo ji přetáhnout na jinou položku, čímž se stane jejím potomkem.

Když je vybráno víc položek, jedna z nich je hlavní výběr a je vykreslená jasněji. Dlouhým stiskem a tažením jedné z nich přesunete všechny vybrané objekty najednou.

Když vyberete rodičovskou položku, ve výchozím stavu se vyberou i všechny její potomky. Dalším klepnutím na rodiče přepínáte mezi výběrem jen rodiče, nebo rodiče i s potomky.

Dvojitým klepnutím na položku na ni zaměříte kameru (viz [Rozšířené](#focus-on-item)).

### Nabídka objektu {#object-menu}

Klepnutím na tlačítko se třemi tečkami (...) u objektu ve stromové struktuře zobrazíte nabídku objektu.
Mnoho z těchto možností odpovídá panelu zkratek nahoře, jsou tu zopakované pro pohodlí.

|       Akce          |                        Ikona                       | Popis                                                                                                                                                                   |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Název        |              ![](/icons/pencil.webp)           | Změní název objektu                                                                                                                                                     |
|   Zrušit instanci   |              ![](/icons/unlink.webp)           | Převede instanci na samostatný tvar, takže se úpravy tvaru už nekopírují do ostatních instancí.                                                                         |
|      Instance       |               ![](/icons/link.webp)            | Zduplikuje objekt jako instanci, takže úpravy tvaru jedné se projeví na všech instancích.                                                                               |
|      Klonovat       |              ![](/icons/clone.webp)            | Zduplikuje objekt do nového objektu                                                                                                                                     |
|       Smazat        |              ![](/icons/trash.webp)            | Smaže objekt. Jeho potomci zůstanou zachováni, pokud není zaškrtnuto `Děti`.                                                                                            |
|        Děti         |            ![](/icons/hierarchy.webp)          | Když je zaškrtnuto, `Instance`, `Klonovat` a `Smazat` působí i na potomky objektu.                                                                                      |
| Rozdělit podle Částí |             ![](/icons/separate.webp)         | Pokud se objekt skládá z nespojených částí, vytvoří pro každou z nich samostatný objekt. Opak spojení.                                                                 |
| Rozdělit podle Skupin |            ![](/icons/group.webp)         | Pokud má objekt více skupin ploch, vytvoří pro každou skupinu ploch samostatný objekt.                                                                                  |
| Rozdělit podle Vrstev |              ![](/icons/layer.webp)       | Pokud má objekt vrstvy, vytvoří samostatné objekty pro základní síť a pro každou vrstvu. Hodí se pro posílání blendshapů do jiných aplikací.                            |
|   Spojit → Vrstvy   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Pokud je vybráno více objektů se shodnou topologií, sloučí je do vrstev hlavního objektu (ostatní objekty se smažou). Opět se hodí pro blendshapy, tentokrát přicházející Z jiných aplikací.<br><br> Vrstvy budou ve výchozím stavu vypnuté. Zapněte je, pokud potřebujete upravit jejich posuvníky. |
|  Křivka (Opakovač)  |              ![](/icons/curve.webp)            | Jen pro trubku nebo soustruh: přidá jako potomka objektu opakovač [Křivka](#curve), který sleduje stejnou křivku.                                                      |
|        Trubka       |             ![](/icons/tube.webp)              | U soustruhu přidá jako potomka [trubku](tools.md#tube), která sleduje jeho profil. Válec, kužel nebo torus převede na trubku stejného tvaru, kterou pak můžete ohýbat podél křivky. |




### Vícenásobný výběr {#multiselection}
Vybrat více objektů se hodí ke dvěma věcem:
- přesunout několik objektů najednou nástrojem gizmo
- sloučit objekty pomocí spojení a booleovských operací.

Ve stromové struktuře klepněte na ikonu výběru u každého objektu, nebo táhněte po sloupci výběru. Při klepání na názvy podržte zkratku `Maska` (nebo `Ctrl` na klávesnici), chcete-li přidat či odebrat jeden objekt, nebo zkratku `Hladit` (nebo `Shift`), chcete-li vybrat všechny objekty mezi aktuálním a tím, na který klepnete.

::: tip Rychlý vícenásobný výběr
Vybírat více objektů můžete i ve viewportu: podržte zkratku `Hladit` (nebo `Shift`) a klepněte na další síť.

Výběr objektu zrušíte opětovným klepnutím na něj (jen pokud je ve výběru víc než jeden objekt).
:::

Gizmo posouvá všechny vybrané objekty společně, viz [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Spojit {#join}
Tato možnost jednoduše udělá z několika vybraných objektů jedinou položku.
Body a UV bližší než [poloměr svaření](#weld-radius) se sloučí.

Příklad na videu najdete v sekci [Rozdělit](#separate).

## ![](/icons/bool_subtract_circle.webp) Booleovský {#boolean}
![](/images/scene_boolean_menu.webp) 
Spojí objekty do jediného povrchu.

`Slučit voxel` zachová objem objektů a na povrchu vypočítá nové, rovnoměrně rozložené polygony. Díky tomuto výpočtu zvládne voxelové sloučení i složitou geometrii, ale pokud cílové rozlišení není dost vysoké, může přijít o jemné detaily.

`Booleovský` se snaží ponechat polygony v původním rozložení a sešít je tam, kde se objekty překrývají. Výsledek tak může být mnohem čistší a ostřejší než u voxelového sloučení, vyžaduje to ale „vodotěsné“ sítě: objekty nesmí mít otvory ani poškozené tvary. Když to selže, voxelové sloučení obvykle funguje.

### Booleovské operace {#boolean-operations}
Voxelové sloučení i booleovská operace řídí výsledek podle viditelnosti objektů, jak připomínají poznámky ve spodní části okna:

#### Sjednocení {#union}
Oba objekty viditelné vytvoří booleovské **sjednocení**: vnější plášť objektů se spojí bez vnitřních ploch. ![](/images/boolean_union.webp)

#### Odečtení {#subtract}
Jeden objekt neviditelný = booleovské **odečtení**: neviditelný objekt se odečte od viditelného. ![](/images/boolean_subtract.webp)

#### Průnik {#intersect}
Oba objekty neviditelné = booleovský **průnik**: nový tvar vznikne jen tam, kde se oba objekty překrývají. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Slučit voxel {#voxel-merge-button}
Stisknutím tohoto tlačítka provedete voxelové sloučení vybraných objektů. Na jediném objektu ho přesíťuje na rovnoměrně rozložené polygony, což se hodí, když má objekt natažené polygony. Níže uvedené možnosti fungují stejně jako u [voxelového přesíťování](topology.md#voxel-remesher).

### Rozlišení {#resolution}
Rozlišení 3d voxelové mřížky použité pro výpočet. Při změně této hodnoty se na objekt překryje šachovnicový vzor s náhledem velikosti polygonů.

Kapátko vedle posuvníku převezme detail z hustoty sítě pod vaším prstem. Tlačítko vedle něj přepne posuvník na `Délka hrany`, velikost ve světě: stejná hodnota dá stejný detail na jakémkoli objektu.

### Vytvořit multirezoluci {#build-multiresolution}
Vytvoří úrovně multirezoluce pod cílovým rozlišením. Pokud je rozlišení 400 a `Vytvořit multirezoluci` je 3, dostanete novou síť s řekněme 296 000 polygony, ale pod ní budou 3 nižší úrovně dělení s přibližně 74 000, 18 500 a 4 600 polygony.

### Zesílit tenké části {#thicken-thin-parts}
Zesílí části, které jsou pro voxelovou mřížku příliš tenké, aby se nerozpadly. Není dostupné spolu s `Ostré hrany` ani `Ostrá hranice`.

### Otvory {#holes}
Jak se před sloučením uzavřou otvory v otevřených objektech:
* `Vyplnit` - každý otvor se uzavře samostatně, od svého okraje.
* `Tvar` - otvory se uzavřou podle okolního povrchu a otevřené kusy, které se překrývají, se spojí.

### ![](/icons/angle.webp) Udržovat ostré hrany {#keep-sharp-edges}
Tlačítko `Ostré hrany` přichytí voxelovou síť k ostrým hranám objektů. Nejlépe funguje na jednoduchých tvarech a na některých místech může způsobit deformace.

### ![](/icons/group.webp) Ostrá hranice {#sharp-border}
Nové plochy sledují hranice skupin ploch a hranice zůstane ostrá tam, kde se podél ní povrch láme.

### ![](/icons/group_separate.webp) Oddělit skupiny {#keep-groups-separate}
Každá skupina ploch se přesíťuje samostatně: skupiny se nikdy nespojí a každá zůstane uzavřeným kusem ve své vlastní skupině. V tomto režimu se multirezoluce nevytváří.

### ![](/icons/bool_subtract_circle.webp) Tlačítko Booleovský {#boolean-button}
Stisknutím tohoto tlačítka provedete polygonovou booleovskou operaci pomocí knihovny Manifold od Emmetta Lalishe.

### ![](/icons/bool_unite_circle.webp) Vyčistit překryvy {#clean-overlaps}
Když je vybraný jen jeden objekt, tlačítko `Booleovský` se změní na `Vyčistit překryvy`: sloučí části objektu, které se navzájem protínají, do čistého povrchu.


## ![](/icons/separate.webp) Rozdělit {#separate}
Pokud máte jeden objekt složený z několika nespojených částí, můžete ho rozdělit na několik objektů.
Dá se to chápat jako opak [spojení](#join).

Okno `Rozdělit...` nabízí tři způsoby, jak vybrané objekty rozdělit:
* `Rozdělit podle Částí` - vytvoří samostatný objekt pro každou nespojenou část.
* `Rozdělit podle Skupin` - vytvoří samostatný objekt pro každou skupinu ploch.
* `Rozdělit podle Vrstev` - vytvoří samostatné objekty pro základní síť a pro každou vrstvu.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Nabídka Přidat {#add-menu}

![](/images/scene_addmenu_overview.webp)

Tato nabídka vytváří primitiva, skupiny, kamery, opakovače a světla.

Primitiva jsou základní tvary, které lze upravovat pomocí parametrů. Když primitivum upravíte podle svých potřeb, „dokončíte“ ho, čímž se parametry zapečou do polygonové sítě, na které můžete sochat a malovat. Po dokončení už parametry primitiva měnit nelze.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Na gizmo {#on-gizmo}
Nové primitivum se umístí tam, kde je aktuálně vybraný tvar nebo gizmo. Když je vypnuto, primitivum se umístí do středu scény.

### ![](/icons/gizmo.webp) Vybrat gizmo {#select-gizmo}
Po vytvoření nového primitiva se automaticky přepne na nástroj gizmo.

### ![](/icons/cog.webp) Rozšířené {#add-advanced}

V této nabídce nastavíte, kde se mají vytvářet nová primitiva, skupiny a opakovače. Mohou vznikat na vybraném objektu, v počátku světa, nebo na místě gizma.


### UV {#uvs}
Přepínač `UV` vedle nadpisu Primitivum zapne UV u primitiv. UV (často nazývané texturovací souřadnice) jsou doplňková data, která ve 3d umožňují nanášet textury na povrchy. Zabírají víc paměti, ale na většině zařízení by to neměl být problém, pokud se nedostanete k velmi vysokým počtům polygonů (např. 10 milionů a víc).

### Primitiva {#primitives}

| Primitivum     | Ikona                                     | Popis                                                                                                           |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Kvádr          | ![](/icons/cube.webp)                    | Jednoduchá krychle, můžete nastavit dělení v X, Y a Z                                                           |
| Quad koule     | ![](/icons/circle.webp)                  | Dělený kvádr s vynucenou možností `Koule`, takže má rovnoměrnou síť čtyřúhelníků, která se dobře hodí k sochání |
| Válec          | ![](/icons/cylinder.webp)                | Válci můžete přidat díru uprostřed, například pro dutou trubku                                                  |
| Torus          | ![](/icons/torus.webp)                   | Torus může být dobrým výchozím bodem pro prsteny                                                                |
| Kužel          | ![](/icons/cone.webp)                    | -                                                                                                               |
| Ikosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV koule       | ![](/icons/circle.webp)                  | Koule s nerovnoměrným rozložením polygonů, viz [upozornění níže](#uv-sphere)                                    |
| Rovina         | ![](/icons/rectangle.webp)               | Jednoduchá rovina, jako jediné primitivum není uzavřená                                                         |
| Text           | ![](/icons/text.webp)                    | 3d text s písmem, stylem, zarovnáním, hloubkou a ohybem. `Sloučit písmena` spojí písmena, která se dotýkají     |
| Trubka         | ![](/icons/tube.webp)                    | viz [Trubka](tools#tube)                                                                                        |
| Soustruh       | ![](/icons/lathe.webp)                   | viz [Soustruh](tools#lathe)                                                                                     |
| Triplanární    | ![](/icons/triplanar.webp)               | viz [Triplanární](#triplanar)                                                                                   |
| VDM            | ![](/icons/vdm.webp)                     | Rovina připravená k sochání razítka vektorového posunutí: obsahuje UV a je natočená ke kameře                   |
| Stínový zachytávač | ![](/icons/material_shadow_catcher.webp) | viz [Stínový zachytávač](#shadow-catcher)                                                                   |
| Hlava          | ![](/icons/face.webp)                    | Jednoduchá hlava s vrstvou pro prolínání mezi mužskou a ženskou podobou                                         |

::: tip
Pokud vás zajímá, co je základní síť po spuštění Nomadu: je to také dělený kvádr.
Základní síť v Nomadu ale nepoužívá `Koule`, takže není dokonale kulatá.
:::

### Panel nástrojů primitiva {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Po vytvoření primitiva se zobrazí panel nástrojů pro ovládání jeho parametrů.

* `Dokončit` Zapeče primitivum do běžného objektu, na kterém můžete sochat a malovat.
* `Zrcadlit` Přepne umístění zrcadlového opakovače nad primitivum.
* `Vše` (ikona oka) Zvolte, které úchyty se zobrazí přímo na primitivu pro ovládání jeho parametrů, např. šířky krychle nebo poloměru díry válce: `Žádný`, `Vše`, nebo jen jeden druh (poloměr, díra, profil...) podle primitiva.
* `Dělení` Počet dělení primitiva, zde podél X u kvádru.
* `Konstantní hustota` Když primitivum gizmem natáhnete podél jedné osy, roste jeho velikost i počet dělení místo natahování polygonů, takže plochy zůstanou čtvercové. Dostupné u kvádrů, rovin a válců.
* `...` Zobrazí nabídku primitiva.

Různá primitiva mají na panelu nástrojů další možnosti:

* `Koule` Koule je postavená jako dělená krychle, protože to je pro sochání lepší, takže není dokonale kulatá. Tato možnost tvar přiblíží dokonalé kouli. Stejnou možnost má i ikosahedron.
* `Víčko` Přepíná víčka na koncích tvaru, např. válec může mít víčko nahoře, dole, na obou koncích, nebo nikde.
* `Díra` Přepíná díru středem tvaru. Střídá se bez díry, díra s jedním poloměrem a díra s různým poloměrem nahoře a dole.
* `Poloměr` Přepíná, zda má válec jeden poloměr, nebo různý poloměr nahoře a dole.
* `Disk` Přepíná, zda je rovina čtyřúhelník, nebo kruh.

Malý panel pod hlavním panelem nástrojů přepíná mezi gizmem primitiva a transformačním gizmem.

::: tip

Klepnutím na nadpis panelu nástrojů ho přesunete nahoru nebo dolů na obrazovce. Klepnutím na šipku v rohu ho sbalíte.

:::


### Nabídka primitiva {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Obsahuje všechny parametry vybraného primitiva. Parametry jsou základní popis tvaru. Prsten byste například popsali jeho vnějším poloměrem, vnitřním poloměrem a počtem polygonů.

Většina parametrů primitiv by měla být srozumitelná sama o sobě a některé parametry mají všechna primitiva společné:

* `UV` Malé tlačítko UV v horní části nabídky přepíná vytváření UV souřadnic
* `Dokončit` Malé tlačítko pro dokončení zapeče primitivum do běžného objektu, na kterém můžete sochat a malovat.
* `Max. počet ploch` Nastaví horní limit počtu polygonů objektu, aby zařízení nespadlo.
* `Post-pododdíl` Zapne zvolený počet dělení ze sekce multirezoluce v nabídce Topologie. V kombinaci s nízkým počtem dělení topologie z toho můžete udělat vyhlazená primitiva s měkkými rohy. Například kvádr s dělením topologie 2 a následným dělením 4 bude mít hladké rohy.
* `Lineární poddělení` Nastaví, kolik úrovní lineárního dělení se použije před běžným hladkým dělením. Tím řídíte, jak ostré nebo měkké budou rohy dělených povrchů. Např. nastavte kvádru dělení topologie na 2, následné dělení na 4 a pak zkoušejte měnit lineární dělení mezi 0 a 4. Rohy kvádru přejdou od měkkých k ostrým.

### Topologie {#topology}

Řídí počet polygonů primitiva. Ovládací prvky jsou obvykle propojené, takže změnou jediného aktivního posuvníku rovnoměrně upravíte všechny polygony. Klepnutím na tlačítko rozpojení můžete dělení tvaru v X/Y/Z ovládat zvlášť.

### Geometrie {#geometry}

Řídí celkovou velikost primitiva, v jednotkách X/Y/Z u hranatých tvarů a poloměrem u kulatých tvarů.


### ![](/icons/circle.webp) UV koule {#uv-sphere}
::: warning
UV koule se na sochání příliš nehodí, zvlášť na pólech.

Dejte raději přednost [primitivům](#primitives) Quad koule, Kvádr nebo Ikosahedron s možností `Koule`.

Topologie může být pro sochání přijatelná, pokud u posuvníků `Dělení` použijete velmi nízkou hodnotu.
Počet polygonů pak můžete zvýšit posuvníkem `Celkové dělení`.

I když se nehodí pro běžné sochání, hodí se na oči: když kouli natočíte tak, aby póly byly v místě zornice, rozložení polygonů přirozeně sedne pro malování a sochání duhovky a zornice.
:::


### ![](/icons/triplanar.webp) Triplanární {#triplanar}
Toto primitivum je zvláštní tím, že jeho geometrii tvarujete [nástrojem Maska](tools.md#mask).

![](/videos/triplanar.mp4)


::: tip
Dvojitým klepnutím na rovinu na ni kamera zaměří.
Nefunguje to ale, pokud primitivum otočíte gizmem.
:::

Triplanár používá informace o masce ze 3 rovin k vyplnění voxelové mřížky, která se pak převede na polygony (díky [voxelovému přesíťování](topology.md#voxel-remesher)).

Každá rovina má vlastní rovinu symetrie.

::: warning
Pokaždé, když změníte velikost triplanárního primitiva, kvalita malby masky se zhorší.

Zatím nelze malbu „zamknout“ na jedné rovině, ale možná to v budoucnu přijde.
Trochu pomoci může [spojitá topologie](stroke.md#connected-topology): pokud kurzor leží přesně na jedné rovině, neovlivní ostatní roviny.
:::

### ![](/icons/material_shadow_catcher.webp) Stínový zachytávač {#shadow-catcher}
Přidá rovinu s materiálem stínového zachytávače. Podrobnosti najdete v sekci [Materiál Stínový zachytávač](material.md#shadow-catcher).


## Skupina/Kamera {#groupcamera}
### ![](/icons/share.webp) Skupina {#group}
Vytvoří „prázdný“ objekt, pod který můžete vnořit další objekty. Hodí se k uspořádání hierarchie: dáte mnoho objektů pod jednu skupinu a tu sbalíte. Skupina může také pomoci s přesouváním objektů: mnoho objektů umístíte pod skupinu a pak skupinu nástrojem gizmo posunete, otočíte nebo změníte její měřítko.

### ![](/icons/camera.webp) Kamera {#add-view}
Vytvoří kameru.

## Opakovače {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Opakovače jsou uzly, které vytvářejí instance objektů pod sebou.

### ![](/icons/array.webp) Pole {#array}
![](/images/scene_primitive_array.webp)

Objekty, které se stanou potomky tohoto uzlu, lze instancovat do mřížky. Když je uzel vybraný, má tyto ovládací prvky:
* `Vložit dovnitř` - když je zapnuto, všechny kopie se umístí dovnitř hranic pole; když je vypnuto, posuvníky nastavují mezeru mezi kopiemi
* `Počet X/Y/Z` - počet instancí na každé ose
* `Velikost X/Y/Z` - velikost mřížky podél každé osy, nebo vzdálenost mezi kopiemi, když je `Vložit dovnitř` vypnuto
* `Náhodně...` - přidá kopiím náhodné odchylky, viz [Náhodně](#curve) níže.

### ![](/icons/curve.webp) Křivka {#curve}
![](/images/scene_primitive_curve.webp)
Vytvoří křivku a potomci tohoto uzlu se budou opakovat podél ní. Když je uzel vybraný, má tyto ovládací prvky:
* `Křivka` - úprava křivky: přidávání bodů a posouvání bodů na křivce.
* `Zobrazit` - zobrazí nebo skryje křivku a její body.
* `Zachycení` - přichytí body křivky k jiné geometrii.
* `Sym` - upravuje křivku symetricky.
* `Uzavřeno` - přepíná, zda se začátek a konec křivky spojí, nebo zda je křivka otevřená.
* `B-splajn` - přepíná, zda instance sledují křivku přesně, nebo použijí interpolaci b-splajnem s hladším výsledkem.
* `Deformovat` - ohne každou kopii podél křivky, takže kopie navazují na sousedy (`Plynulé` ohne jejich boky tak, aby navazovaly bez úhlu).
* `Zarovnat` - natočí kopie podle směru křivky.
* `Otočný bod` - otočný bod kopií: samotná křivka (`Vlastní`) nebo její potomci.
* `Počet` - počet instancí. Tlačítko režimu vedle něj přepne na `Vzdálenost`: pevnou mezeru mezi kopiemi, počet se pak řídí délkou křivky.
* `Poloměr` - ovládací prvky na každém bodu křivky pro nastavení měřítka instancí.
* `Zkrut` - ovládací prvky na každém bodu křivky pro nastavení zkroucení instancí.
* `Střídat` - otočí každou druhou kopii kolem křivky: o 90° pro články řetězu, o 180° pro listy nebo zuby zipu, kolem zvolené `Osa`.
* `Spirála...` - vine kopie kolem křivky v několika pramenech (lano, cop, stuha...).
* `Náhodně...` - přidá kopiím náhodné odchylky; každý řádek může místo toho přidat stejnou hodnotu u každé kopie.

Pod panelem nástrojů přepínač `(Sloučit)` sloučí bod s jiným, když ho na něj přetáhnete. `IK` (inverzní kinematika) umožňuje křivku pózovat: táhnete bodem a propojené body ho následují. Klepnutím na bod ho zamknete nebo odemknete, dlouhým stiskem zamknete nebo odemknete všechny; zamčené body zůstanou na místě.

### ![](/icons/radial.webp) Radiální {#radial}
![](/images/scene_primitive_radial.webp)

Potomci tohoto uzlu se instancují do kruhu. Posunutím potomka změníte poloměr opakovače. Když je uzel vybraný, má tyto ovládací prvky:
* RadialX/Y/Z - tato tlačítka nastaví osu kruhu a počet instancí.



### ![](/icons/mirror.webp) Zrcadlit {#mirror}
![](/images/scene_primitive_mirror.webp)

Potomci tohoto uzlu se zrcadlí podle osy. Když je uzel vybraný, má tyto ovládací prvky:
* Gizmo - zapne transformační gizmo pro nastavení středu zrcadlení. Lze ho také otáčet a měnit jeho měřítko. Až budete hotovi, klepněte znovu na gizmo a zobrazí se běžné ovládací prvky.
* X/Y/Z - nastaví rovinu zrcadlení

### ![](/icons/surface.webp) Povrch {#surface}

Potomci tohoto uzlu se kopírují na povrch objektu: jedna kopie na plochu, na hranu nebo na vrchol, nebo náhodně rozptýlené. Když je uzel vybraný, má tyto ovládací prvky:
* Režim - umístí kopie na `Plochy`, `Hrany` nebo vrcholy, nebo je `Rozptýlit`.
* Každých - jedna kopie každých N ploch, hran nebo vrcholů. `Náhodně` je místo toho vybere náhodně a `Promíchat` vylosuje jinou náhodnou sadu.
* Rozestupy - při rozptylování minimální vzdálenost mezi dvěma kopiemi.
* Zarovnat - kopie stojí na povrchu podle jeho normály, místo aby si zachovaly natočení originálu.
* Přichytit - promítne originál do nejbližšího bodu povrchu, kopie ho následují.
* Přizpůsobit velikost, Klopení - změní měřítko kopií a natáhne je podle tvaru každé plochy.
* Deformovat - ohne každou kopii na její plochu nebo podél její hrany, takže sousední kopie na sebe navazují bez mezer.

Všechny opakovače mají ovládací prvek `Dokončit`, který zapeče výsledek opakovače a zeptá se, jak zapečení provést:
* Spojit děti - instance se spojí do jediného objektu
* Zachovat instance - instance zůstanou instancemi, ale už nebudou mít „rodičovský“ opakovač
* Zrušit instanci - instance se převedou na samostatné objekty

`Zploštit vše` zapeče i opakovače vnořené v tomto opakovači, takže se z každé kopie stane obyčejný objekt.

::: tip Tip: Kombinace opakovačů
Opakovače lze vnořovat pod sebe a potomky opakovačů může být několik objektů, což vede ke složitým efektům.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Otočné body opakovačů

Některé opakovače se snaží automaticky nastavit otočný bod potomků, takže se nepohnou, ani když je posunete nebo otočíte nástrojem gizmo. Pokud to potřebujete obejít, vložte mezi opakovač a potomka skupinu. Pak můžete tvarem potomka hýbat nezávisle na opakovači.
:::

## Světlo {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Směrové {#directional}
Vytvoří směrové světlo, nekonečně vzdálený zdroj světla podobný slunci.

### ![](/icons/panorama.webp) Prostředí {#environment}
Vytvoří světlo prostředí, které osvětluje scénu obrázkem kolem ní (osvětlení podle obrázku, jako HDRI).

### ![](/icons/spotlight.webp) Bodové (reflektor) {#spot}
Vytvoří reflektor s nastavením šířky a měkkosti kužele

### ![](/icons/light.webp) Bodové {#point}
Vytvoří bodové světlo

## ![](/icons/cog.webp) Rozšířené {#advanced}
Tlačítko `Rozšířené` vlevo dole na panelu otevře okno se dvěma kartami: `Obecné` a `Synchronizovat`.

### ![](/icons/focus.webp) UI: Zaměřit na položku při dvojím klepnutí {#focus-on-item}
Dvojité klepnutí na položku v seznamu Scéna vystředí kameru na tuto položku ve 3d zobrazení.

### ![](/icons/eye_open.webp) Synchronizovat viditelnost {#sync-visibility}
Když je zapnuto, ikona oka u vybrané položky ovlivní všechny vybrané položky.

### ![](/icons/bang.webp) Zvýraznit {#highlight}
Při změně výběru zvýrazní vybrané objekty ve viewportu.

### ![](/icons/link.webp) Zobrazit (Instance) {#instance-show}
Zobrazí vlevo v seznamu scény barevnou kapsli, která označuje instance.

### ![](/icons/preview.webp) Náhledy objektů {#object-previews}
Zobrazí u každého objektu v seznamu scény vyrenderovanou miniaturu. Je to totéž jako tlačítko náhledu nad seznamem.

### Poloměr svaření {#weld-radius}
Pod nadpisem `Spojit` jsou `Poloměr svaření pozice` a `Poloměr svaření UV`: body a UV bližší než tyto poloměry se sloučí. Každý z nich lze vypnout jeho zaškrtávacím polem. Platí to pro spojení, booleovské operace, ořezání, decimaci, přesíťování a import souborů.

### Ikony {#icons}
Nastaví minimální a maximální `Velikost` a `Krytí` ikon skupin, světel, kamer a opakovačů ve viewportu.

### ![](/icons/hierarchy.webp) Hierarchické linie {#hierarchy-lines}
Zobrazí ve viewportu čáru mezi rodičem a jeho potomky. Když je zapnuto, můžete také nastavit:
* `Použij Nomad pivot` - čáry začínají v otočném bodě, který používají nástroje Transformace a Gizmo. Když je vypnuto, použije se přirozený základní otočný bod, který může být daleko od středu objektu.
* `Tloušťka` - šířka čar. Tlačítko vedle posuvníku k nim přidá obrys.
* Barvu čar.

### ![](/icons/link.webp) Synchronizovat {#sync}
Karta `Synchronizovat` určuje pro každou operaci (`Přidat`, `Smazat`, `Zámek`, `Klonovat`, `Instance`, `Zrušit instanci`, `Spojit`, `Rozdělit` a `Booleovský`), zda se použije na všechny instance výběru:
* `Auto` - řídí se zaškrtávacím polem `Synchronizovat` v horní části nabídky scény.
* `Ne` - jen vybrané objekty.
* `Ano` - vždy všechny instance.

Ve výchozím stavu jsou `Spojit`, `Rozdělit` a `Booleovský` na `Ano` a ostatní na `Auto`. `Resetovat` vrátí tyto výchozí hodnoty.

## Spodní panel nástrojů {#bottom-toolbar}
Tyto ikony přepínají viditelnost skupin, světel, kamer, opakovačů a hierarchických linií ve viewportu. Na ikony zobrazené na plátně můžete klepnout a přímo je tak vybrat a upravit.
