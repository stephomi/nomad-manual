# ![](/icons/scene.webp) Scéna {#scene}

Tato nabídka vám umožňuje spravovat objekty, světla, kamery a replikátory (repeaters) v Nomadu. Zobrazuje hierarchii scény jako stromový náhled, který vám umožní upravovat mnoho aspektů vašich objektů. Také umožňuje vytvářet nové objekty a objekty různými způsoby spojovat a rozdělovat.


![](/images/scene_menu_summary.webp)


## Panel zkratek {#shortcut-bar}
| Akce                  | Ikona                             | Popis                                                                                                              |
| :-------------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| [Přidat...](#add-menu) | ![](/icons/plus.webp)            | Zobrazí [nabídku Přidat](#add-menu) pro přidání objektu do scény                                                   |
| Smazat                | ![](/icons/trash.webp)           | Smaže objekt                                                                                                       |
| Zamknout              | ![](/icons/lock.webp)            | Způsobí, že objekt nelze ve viewportu vybrat. Stále jej však lze vybrat ve stromovém zobrazení.                   |
| Sloučit               | ![](/icons/merge.webp)           | Sloučí vybrané objekty do jednoho objektu bez změny geometrie                                                     |
| Oddělit               | ![](/icons/diagonal.webp)        | Pokud je objekt tvořen samostatnými polygonovými „skořápkami“, rozdělí jej na více objektů. Opak operace sloučení |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | Zobrazí nabídku [Boolean](#boolean)                                                                                |
| Klonovat              | ![](/icons/clone.webp)           | Duplikuje objekt do nového objektu                                                                                |
| Instance              | ![](/icons/link.webp)            | Duplikuje objekt jako instanci, takže modelovací změny na jednom se projeví na všech instancích                   |
| Zrušit instanci       | ![](/icons/unlink.webp)          | Převede instanci na unikátní tvar, takže modelovací změny se již nekopírují do ostatních instancí                 |
| Sync                  | ![](/icons/link.webp)            | Pokud mají instance potomky, zajistí, že všechny instance sdílejí stejnou hierarchii potomků                      |


## Stromová struktura {#tree-view}
![](/images/scene_treeview.webp) 

| Akce        | Ikona                      | Popis                    |
| :---------: | :------------------------: | :----------------------: |
| Vybrat      | ![](/icons/checked.webp)  | Přepne výběr/nevybráno   |
| Viditelné   | ![](/icons/eye_open.webp) | Přepne viditelnost       |
| Nabídka     | ![](/icons/more.webp)     | Zobrazí nabídku objektu  |

::: tip TIP: Rychlý výběr nebo skrytí více objektů

Klepnutím na ikonu výběru přepnete jeden objekt, nebo tažením vertikálně ve sloupci výběru vyberete více objektů. Totéž lze provést ve sloupci viditelnosti.

:::

### Ovládání stromového zobrazení {#tree-view-manipulation}

Dlouze stiskněte položku ve stromovém zobrazení, dokud nezžloutne. Poté ji můžete posouvat nahoru nebo dolů ve stromu, stejně jako ji přetáhnout na jinou položku a udělat z ní jejího potomka.

Když je vybráno více položek, většina bude tmavě žlutá, jedna bude světlejší žlutá. Dlouze stiskněte a táhněte světlejší položku, abyste přesunuli všechny objekty najednou.

Když vyberete rodičovskou položku, ve výchozím nastavení se vyberou i všechny její potomci. Klepnutím na ikonu rodiče přepínáte mezi výběrem pouze rodiče, nebo rodiče i potomků.

### Nabídka objektu {#object-menu}

Kliknutím na tlačítko se třemi tečkami (...) u objektu ve stromovém zobrazení se zobrazí nabídka objektu. 
Mnoho z těchto voleb je podobných panelu zkratek nahoře, zopakovaných pro pohodlí.

|       Akce        |                        Ikona                        | Popis                                                                                                                                                                   |
| :---------------: | :-------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instance     |               ![](/icons/link.webp)               | Duplikuje objekt jako instanci, takže modelovací změny na jednom se projeví na všech instancích.                                                                      |
|       Klonovat    |              ![](/icons/clone.webp)               | Duplikuje objekt do nového objektu                                                                                                                                     |
|        Název      |              ![](/icons/pencil.webp)              | Změní název objektu                                                                                                                                                    |
|       Smazat      |              ![](/icons/trash.webp)               | Smaže objekt                                                                                                                                                           |
|     Smazat+       |            ![](/icons/removeNode.webp)            | Smaže objekt i jeho potomky                                                                                                                                            |
|   Zrušit instanci |              ![](/icons/unlink.webp)              | Převede instanci na unikátní tvar, takže modelovací změny se již nekopírují do ostatních instancí.                                                                    |
| Oddělit topologii |             ![](/icons/separate.webp)             | Pokud je objekt tvořen samostatnými polygonovými „skořápkami“, rozdělí jej na více objektů. Opak operace sloučení.                                                    |
| Oddělit Face Group |            ![](/icons/faceGroup.webp)           | Pokud má objekt více face group, rozdělí síť na samostatné objekty.                                                                                                   |
|   Oddělit vrstvy  |              ![](/icons/layer.webp)               | Pokud má objekt vrstvy, rozdělí každou vrstvu do samostatného objektu. Užitečné pro posílání blendshapeů do jiných aplikací.                                         |
|   Sloučit -> Vrstvy    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Pokud je vybráno více objektů se shodnou topologií, sloučí tyto objekty do vrstev primárního objektu (ostatní objekty budou smazány). Opět užitečné pro blendshapy přicházející Z jiných aplikací.<br><br> Všimněte si, že vrstvy budou ve výchozím stavu vypnuté. Povolte je, pokud potřebujete upravit jejich posuvníky. |




### Vícenásobný výběr {#multiselection}
Můžete vybrat více objektů, abyste dosáhli dvou věcí:
- použití nástroje gizmo k přesunu několika objektů najednou
- sloučení objektů pomocí operací sloučení a boolean.

Můžete to udělat zaškrtnutím `Multiselection` a poté klikáním na objekty v seznamu.

::: tip Rychlý vícenásobný výběr
Můžete také vybírat více objektů ve viewportu podržením zkratky `Smooth` a klepnutím na jinou síť (mesh).

Objekt můžete odznačit opětovným klepnutím na něj (pouze pokud váš výběr obsahuje více než jeden objekt).
:::

::: warning Omezené funkce gizma
Při použití vícenásobného výběru bude nástroj gizmo vždy ignorovat maskování.
Také je odstraněno škálování v osách X/Y/Z.

Důvodem je, že vícenásobný výběr umožňuje pouze transformaci celé sítě, nikoli transformaci jednotlivých vrcholů.
To může být v budoucnu vylepšeno.
:::


## Spojit {#join}
Tato volba jednoduše vytvoří jednu položku objektu z více vybraných objektů.

Příklad můžete vidět na videu v sekci [Oddělit](#separate).

## Booleovské operace {#boolean}
![](/images/scene_boolean_menu.webp) 
Kombinuje objekty do jednoho povrchu.

`Voxel merge` zachová objem objektů a vypočítá nové rovnoměrně rozmístěné polygony na povrchu. Kvůli výpočetnímu kroku si voxelové sloučení poradí se složitou geometrií, ale může ztratit jemné detaily, pokud cílové rozlišení není dostatečně vysoké.

`Boolean` se pokusí ponechat polygony v jejich původním rozložení a sešít je tam, kde se objekty překrývají. To může vytvořit mnohem čistší a ostřejší výsledky než voxelové sloučení, vyžaduje však „vodotěsné“ sítě; v objektech nesmí být díry nebo poškozené tvary. Pokud to selže, obvykle bude fungovat voxel merge.

### Booleovské operace {#boolean-operations}
Jak Voxel Merge, tak Boolean používají viditelnost objektů k řízení operace:

#### Sjednocení {#union}
Oba objekty viditelné vytvoří boolean **union**, vnější „kůže“ objektů je spojena bez vnitřních povrchů. ![](/images/boolean_union.webp)

#### Odečíst {#subtract}
Jeden objekt neviditelný = boolean **subtract**, neviditelný objekt bude odečten od viditelného objektu. ![](/images/boolean_subtract.webp)

#### Průnik {#intersect}
Oba objekty neviditelné = boolean **intersection**, vytvoří nový tvar pouze tam, kde se dva objekty překrývají. ![](/images/boolean_intersect.webp)


### Tlačítko Voxel Merge {#voxel-merge-button}
Stisknutím tohoto tlačítka provedete voxelové sloučení vybraných objektů. Při použití na jednom objektu jej retopologizuje do rovnoměrně rozmístěných polygonů, což je užitečné, když má objekt natažené polygony.

### Rozlišení {#resolution}
Rozlišení voxelové 3D mřížky použité pro výpočet. Při změně této hodnoty se na objekt překryje šachovnicový vzor pro náhled velikosti polygonů.

### Vytvořit multirozlišení {#build-multiresolution}
Vytvoří úrovně multiresolution pod cílovým rozlišením. Pokud je tedy vaše rozlišení 400 a build multiresolution je 3, získáte novou síť například s 296 000 polygony, ale budou existovat 3 nižší subdiv úrovně s 74 000, 18 000, 4 000 poly.

### Zachovat ostré hrany {#keep-sharp-edges}
Povolí přichytávání voxelové sítě k hranám. Nejlépe funguje na jednoduchých tvarech.

### Booleovské tlačítko {#boolean-button}
Stisknutím tohoto tlačítka provedete polygonovou boolean operaci pomocí knihovny Manifold od Emmetta Lalishe. 


## Oddělit {#separate}
Pokud máte jeden objekt založený na několika nepropojených částech, můžete tento objekt rozdělit na několik objektů. 
To lze chápat jako opak [jednoduchého sloučení](#simple-merge).

![](/videos/merge_separate.mp4)


## Nabídka Přidat {#add-menu}

![](/images/scene_addmenu_overview.webp)

Tato nabídka vytváří primitiva, skupiny, kamery, repeatery a světla.

Primitiva jsou základní tvary, které lze upravovat pomocí parametrů. Jakmile primitivum upravíte podle svých potřeb, „validujete“ ho, čímž se parametry převedou na polygonovou síť, kterou lze sochat a malovat. Parametry primitiva nelze po validaci dále upravovat.


![](/images/scene_addmenu_top.webp)

### Na gizmu {#on-gizmo}
Povolí umístění nového primitiva tam, kde je aktuálně vybraný tvar nebo gizmo. Pokud je vypnuto, primitivum bude umístěno do středu scény.

### Vybrat gizmo {#select-gizmo}
Povolí automatické přepnutí na nástroj gizmo po vytvoření nového primitiva. 

### Pokročilé {#add-advanced}

Tato nabídka umožňuje nastavit preferenci, kde budou nová primitiva, skupiny a repeatery vytvářeny. Mohou být na vybraném objektu, v počátku světa, nebo v pozici gizma.


### UV {#uvs}
Povolí UV na primitivech. UV (často nazývané texturovací souřadnice) jsou dodatečná data používaná ve 3D k aplikaci textur na povrchy. Zabírají více paměti, ale pro většinu zařízení by to neměl být problém, pokud se nepouštíte do velmi vysokých počtů polygonů (např. 10 milionů a více). 

### Primitiva {#primitives}

| Primitivum     | Ikona                                     | Popis                                                                                                              |
| :------------: | :---------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Jednoduchá krychle, můžete ovládat dělení v osách X, Y a Z                                                        |
| Sphere         | ![](/icons/circle.webp)                  | Pro pohodlí je pojmenována Sphere, ale ve skutečnosti jde o subdividovaný box s vynuceným `Project on sphere`     |
| Cylinder       | ![](/icons/cylinder.webp)                | U primitiva válce můžete přidat středový otvor, například pro vytvoření duté trubky                               |
| Torus          | ![](/icons/torus.webp)                   | Torus může být dobrým výchozím bodem pro prsteny                                                                  |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                                  |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                                  |
| UV-sphere      | ![](/icons/circle.webp)                  | Koule s nerovnoměrným rozložením polygonů, viz [varování níže](#uv-sphere)                                        |
| Plane          | ![](/icons/rectangle.webp)               | Jednoduchá rovina, všimněte si, že je to jediné primitivum, které není uzavřené                                   |
| Tube           | ![](/icons/tool_tube.webp)               | viz [Tube](tools#tube)                                                                                            |
| Lathe          | ![](/icons/tool_lathe.webp)              | viz [Lathe](tools#lathe)                                                                                          |
| Triplanar      | ![](/icons/triplanar.webp)               | viz [Triplanar](#triplanar)                                                                                       |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | viz [Shadow Catcher](#shadow-catcher)                                                                             |
| Head           | ![](/icons/face.webp)                    | Jednoduchá hlava s vrstvou pro prolínání mezi mužským/ženským tvarem                                              |

::: tip
Pokud vás zajímá, jaká je základní síť po spuštění Nomadu: je to také subdividovaný box.
Základní síť v Nomadu však nepoužívá `Project on sphere`, což znamená, že není dokonale kulatá.
:::

### Panel nástrojů primitiv {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Jakmile je primitivum vytvořeno, objeví se panel nástrojů pro ovládání jeho parametrů.

* `Validate` Upeče primitivum do standardního objektu, aby jej bylo možné sochat a malovat.
* `Edit` Přepíná zobrazení gizma primitiva. To je zobrazeno přímo na primitivu pro ovládání jeho parametrů, např. šířky krychle nebo poloměru otvoru válce.
* `Mirror` Přepíná umístění mirror repeateru nad primitivum.
* `...` Zobrazí nabídku primitiva.

Různá primitiva mají na panelu další volby:

* `Project` Koule je konstruována jako subdividovaná krychle, což je lepší pro sochání, ale znamená to, že není dokonale kulatá. Tato volba vynutí tvar blíže k dokonalé kouli. Stejnou volbu sdílí icosahedron.
* `Cap` Přepíná koncové víčka tvaru, např. válec může mít víčka nahoře, dole, obě, nebo žádná.
* `Hole` Přepíná vytvoření otvoru skrz střed tvaru. Cyklicky přepíná mezi žádným otvorem, otvorem s jediným poloměrem nebo otvorem s různým poloměrem nahoře a dole.
* `Radius` Přepíná, zda má mít válec jediný poloměr, nebo odlišný poloměr nahoře a dole.
* `Disk` Přepíná, zda má být rovina čtyřstranný tvar, nebo kruhový tvar.

Malý panel pod hlavním panelem vám umožní přepínat mezi gizmem primitiva a transformačním gizmem.

::: tip

Kliknutím na název panelu jej přepnete nahoru nebo dolů na displeji. Kliknutím na šipku v rohu jej sbalíte.

:::


### Nabídka primitiv {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Obsahuje všechny parametry vybraného primitiva. Parametry jsou základní popis tvaru. Pro popis prstenu byste například popsali jeho vnější poloměr, vnitřní poloměr a počet polygonů.

Většina parametrů primitiv by měla být samozřejmá a existují některé společné parametry sdílené všemi primitivy:

* `UVs` Malé tlačítko UVs v horní části nabídky přepíná vytváření UV souřadnic
* `Validate` Malé tlačítko validate upeče primitivum do standardního objektu, aby jej bylo možné sochat a malovat.
* `Max faces` Nastaví horní limit počtu polygonů v objektu, aby se předešlo pádu zařízení.
* `Post subdivision` Povolí zvolený počet subdiv úrovní z multiresolution sekce nabídky topologie. Lze použít k vytváření vyhlazených, měkkých hran primitiv v kombinaci s nízkým dělením topologie. Například nastavení dělení topologie boxu na 2 a post subdivisions na 4 vytvoří box s hladkými rohy.
* `Linear subdivision` Nastaví, kolik úrovní lineárního dělení se použije před použitím běžného smooth dělení. Lze použít k ovládání, jak ostré nebo měkké jsou rohy na subdividovaných površích. Např. nastavte dělení topologie boxu na 2, post subdivisions na 4 a pak zkuste měnit linear subdivisions mezi 0 a 4. Rohy boxu přejdou z měkkých na ostré.

### Topologie {#topology}

Ovládá počet polygonů v primitivu. Ovládací prvky jsou obvykle propojené, takže změna jednoho aktivního posuvníku upraví všechny polygony rovnoměrně. Můžete klepnout na tlačítko pro odpojení a ovládat dělení X/Y/Z u tvaru samostatně.

### Geometrie {#geometry}

Ovládá celkovou velikost primitiva v jednotkách X/Y/Z u hranatých tvarů a v poloměru u kulatých tvarů.


### UV koule {#uv-sphere}
::: warning
UV Sphere není dobře vhodná pro sochání, zejména v oblasti pólů.

Upřednostněte prosím primitiva [Sphere](#sphere), [Box](#box) nebo [Icosahedron](#icosahedron) spolu s volbou `Project on sphere`.

Všimněte si, že topologie může být pro sochání přijatelná, pokud použijete velmi nízkou hodnotu posuvníků `Division`.
Poté můžete použít posuvník `Overall Subdivision` ke zvýšení počtu polygonů.

Ačkoli není vhodná pro obecné sochání, je užitečná pro oči; pokud kouli otočíte tak, aby póly ležely v oblasti zornice, rozložení polygonů přirozeně sedne pro malování a sochání duhovky a zornice.
:::


### Triplanární {#triplanar}
Toto primitivum je specifické tím, že byste na něj měli použít [nástroj Masking](tools.md#mask) pro tvarování geometrie.

![](/videos/triplanar.mp4)


::: tip
Dvojitým klepnutím na rovinu se kamera zaměří na tuto konkrétní rovinu.
Pokud však primitivum otáčíte pomocí gizma, nebude to fungovat.
:::

Triplanar používá maskovací informace ze 3 rovin k naplnění voxelové mřížky, která je následně polygonizována (díky [Voxel Remesheru](topology.md#voxel-remeshere)).

Každá rovina má vlastní rovinu symetrie.

::: warning
Pokaždé, když aktualizujete velikost Triplanar primitiva, kvalita maskovacího malování se zhorší.

Prozatím neexistuje možnost „zamknout“ malování na jedné rovině, ale možná přijde v budoucnu.
Můžete trochu pomoci pomocí [Connected Topology](stroke.md#connected-topology), protože pokud kurzor leží přesně na jedné rovině, neovlivní ostatní roviny.
:::

### Lapač stínů {#shadow-catcher}
Přidá rovinu s materiálem shadow catcher. Více podrobností viz [materiál Shadow Catcher](material.md#shadow-catcher). 


## Skupina/Kamera {#groupcamera}
### Skupina {#group}
Vytvoří „prázdný“ objekt, pod který můžete zanořit jiné objekty. Lze jej použít k jednoduché organizaci hierarchie tím, že pod skupinu umístíte mnoho objektů a poté ji zavřete. Skupina může být také použita jako pomocný objekt pro přesun objektů; mnoho objektů lze umístit pod skupinu a poté skupinu přesouvat, otáčet a škálovat pomocí nástroje gizmo.

### Přidat pohled {#add-view}
Vytvoří kameru.

## Opakovače {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeatery jsou uzly, které vytvářejí instance objektů pod nimi. 

### Pole {#array}
![](/images/scene_primitive_array.webp)

Když jsou objekty potomky tohoto uzlu, mohou být instancovány do mřížkového rozložení. Po výběru má ovládací prvky:
* Fit inside – přepíná mezi ovládáním velikosti mřížky/boxu pole nebo ovládáním rozestupu mezi instancemi pole
* CountX/Y/Z – počet instancí na každé ose
* OffsetX/Y/Z – vzdálenost mezi instancemi, když je přepnuto fit inside
* SizeX/Y/Z – šířka/výška/hloubka celé mřížky pole, když je přepnuto fit inside.

### Křivka {#curve}
![](/images/scene_primitive_curve.webp)
Vytvoří křivku, potomci tohoto uzlu budou opakováni podél křivky. Po výběru má ovládací prvky:
* Edit – umožní přidávání bodů na křivku a přesouvání bodů na křivce.
* Snap – přichytává body křivky k jiné geometrii
* Align – otáčí podřízené tvary tak, aby se zarovnaly ve směru křivky
* Count – počet instancí
* Closed – přepíná, zda se začátek a konec křivky spojí, nebo zda jde o otevřenou křivku
* Radius – přepíná ovládací prvky na každém bodě křivky pro řízení měřítka instancí
* Twist – přepíná ovládací prvky na každém bodě křivky pro řízení rotačního zkroucení instancí 
* B-spline – přepíná, zda instance sledují křivku přesně, nebo používají B-spline interpolaci, která má hladší výsledky. 

### Radiální {#radial}
![](/images/scene_primitive_radial.webp)

Potomci tohoto uzlu budou instancováni do kruhu. Přesunutím podřízeného objektu změníte poloměr tohoto repeateru. Po výběru má ovládací prvky:
* RadialX/Y/Z – výběrem těchto tlačítek nastavíte radiální osu a počet instancí.



### Zrcadlení {#mirror}
![](/images/scene_primitive_mirror.webp)

Potomci tohoto uzlu budou zrcadleni přes osu. Po výběru má ovládací prvky:
* Gizmo – povolí transformační gizmo pro nastavení středu zrcadlení. Lze jej také otáčet a škálovat. Po dokončení znovu klepněte na gizmo pro zobrazení standardních ovládacích prvků.
* X/Y/Z – nastaví rovinu zrcadlení

Všechny repeatery mají ovládací prvek `Validate`, který upeče výsledky repeateru a zeptá se, jak péct:
* Join children – instance jsou sloučeny do jednoho objektu
* Keep instances – instance zůstanou instancemi, ale již nebudou mít repeater jako „rodiče“
* Un-instances – instance jsou převedeny na unikátní objekty

::: tip Tip: Kombinování repeaterů
Repeatery lze vnořovat pod sebe a několik objektů lze udělat potomky repeaterů, což vede ke složitým efektům.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Pivoty repeaterů

Některé repeatery se pokusí automaticky nastavit pivot podřízených objektů, takže i když je přesunete nebo otočíte pomocí gizma, nepohnou se. Pokud potřebujete toto chování přepsat, vložte mezi repeater a potomka skupinu. Nyní můžete podřízený tvar přesouvat nezávisle na repeateru.
:::

## Světlo {#light}

![](/images/scene_primitive_light.webp)

### Směrové {#directional}
Vytvoří směrové světlo, nekonečně vzdálený zdroj světla jako slunce.

### Reflektor {#spot}
Vytvoří reflektor (spot light) s ovládáním šířky kužele a měkkosti

### Bodové {#point}
Vytvoří bodové světlo

## Pokročilé {#advanced}
### Zaměřit na položku {#focus-on-item}
Dvojité kliknutí na položku v seznamu Scény vycentruje kameru na tuto položku ve 3D pohledu.

### Synchronizovat viditelnost {#sync-visibility}
Použití ikony oka ovlivní všechny vybrané položky. 

### Instance: Zobrazit {#instance-show}
Zobrazí barevnou kapsli vlevo od seznamu scény pro zobrazení instancí.


### Ikony {#icons}
Nastaví velikost a neprůhlednost ikon skupin, světel, kamer a zrcadel ve viewportu

### Čáry hierarchie {#hierarchy-lines}
Zobrazí čáru mezi rodičem a jeho potomky ve viewportu

## Dolní panel nástrojů {#bottom-toolbar}
Tyto ikony přepínají viditelnost skupin, světel, kamer, repeaterů a čar hierarchie ve viewportu.