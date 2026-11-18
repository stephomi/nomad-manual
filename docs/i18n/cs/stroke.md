# ![](/icons/brush.webp) Tah {#stroke}

---
![](/images/stroke_overview.webp) 

## Přehled {#overview}

Chování tahu si můžete přizpůsobit u většiny štětců nástrojů.
Nastavení se podobají těm, která znáte z 2d malířských aplikací, některé volby jsou ale specifické pro sochání a 3d.

Volby jsou rozdělené do 5 podnabídek:

| Název    | Ikona                        | Popis                                                              |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Tah      | ![](/icons/brush.webp)      | Určuje, jak se tah na model nanáší                                 |
| Alfa     | ![](/icons/alpha.webp)      | Jak se pro otisk štětce použije textura ve stupních šedi           |
| Útlum    | ![](/icons/falloff.webp)    | Určuje, jak se síla štětce mění od středu k okraji                 |
| Filtr    | ![](/icons/filter.webp)     | Jak geometrie modelu ovlivňuje štětec                              |
| Tlak     | ![](/icons/pressure.webp)   | Určuje odezvu na tlak stylusu                                      |

::: tip
Ne všechny volby tahu platí pro všechny nástroje. Volby, které aktuální nástroj nepoužívá, jsou neaktivní nebo skryté. 
:::


## ![](/icons/brush.webp) Tah {#stroke-1}

### ![](/icons/radius.webp) Poloměr {#radius}

![](/images/stroke_radius.webp)

Volby poloměru jsou globální nastavení: platí pro všechny nástroje.

#### Prostor {#size}

* `Obrazovka` - poloměr se zadává v jednotkách obrazovky. Když nastavíte poloměr na 100 pixelů, zůstane 100 pixelů široký, ať model přiblížíte, nebo oddálíte.
* `Svět (3D)` - poloměr se zadává v 3d jednotkách. Když například vytvoříte kouli a nastavíte poloměr na stejnou velikost, jako má koule, zůstane poloměr stejně velký jako koule i při přibližování a oddalování.

#### ![](/icons/link.webp) Synchronizace zkratky {#sync-shortcut}

Když je volba zapnutá, poloměr a nastavení siluety zůstávají synchronizované i po přepnutí na zkratkové štětce (`Hladit`, `Maska` nebo `Skrýt`). Rychlé vyhlazení nebo maskování tak použije stejnou velikost štětce jako nástroj, se kterým jste pracovali.

#### ![](/icons/link.webp) Sdílený poloměr {#share-radius}

Když je volba zapnutá, všechny nástroje používají stejný poloměr. Ve výchozím stavu má každý nástroj svůj vlastní.


### Typ tahu {#stroke-type}

![](/images/stroke_strokemode.webp)

Tahy mohou fungovat v několika režimech:

### ![](/icons/stroke_dot.webp) Bod {#dot}
Táhnete jako při běžném malování. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Otáčet {#roll}
Alfa štětce se otáčí podle směru tahu. Hodí se například na stehy na látce. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Zámek + poloměr {#lock-radius}
Otiskne tah štětce s pevnou **_výškou_**. Tažením nastavíte velikost a otočení.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Zámek + intenzita {#lock-intensity}
Otiskne tah štětce s pevným **_poloměrem_**. Tažením nastavíte výšku a otočení.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Režimy `Zámek + poloměr` a `Zámek + intenzita` ignorují nastavení [Tlaku](#pressure), protože velikost a sílu už určuje samotné tažení.
:::

![](/images/stroke_strokemodemove.webp)

Nástroje `Přesunout` a `Táhnout` mají vlastní 3 volby:

### ![](/icons/snake.webp) Tah {#drag}

Během tahu průběžně aktualizuje, co je uvnitř poloměru štětce. Rychlý tah povrch nechá za sebou, pomalý tah materiál drží a vytahuje delší tvary. Je to výchozí režim nástroje `Táhnout`. Se zapnutou volbou `Dynamická topologie` tak můžete vytvářet hadovité výtažky. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Chytit {#grab}
Na začátku tahu vybere, co je uvnitř poloměru štětce, a tento výběr si drží. Hodí se pro přesnější přesuny: vzdálenost posunu můžete pečlivě doladit, aniž byste omylem pohnuli větší částí, než jste původně vybrali. Je to výchozí režim nástroje `Přesunout`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Zámek + poloměr (tah) {#lock-radius-drag}
Nastavený poloměr se ignoruje a mění se dynamicky podle toho, jak daleko od počátečního bodu tah odtáhnete. Malá vzdálenost = malý poloměr, větší vzdálenost = větší poloměr. Posuvníkem intenzity řídíte tvar útlumu. Hodí se pro hrubé modelování organických, gumových tvarů.
![](/videos/stroke_lockradius_drag.mp4) 

Některé další nástroje zde nabízejí své vlastní typy tahu, například `Uvolnit`, `Hladit` a `Rozmazat` u vyhlazovacích nástrojů nebo tvary jako `Laso` a `Křivka` u nástrojů založených na výběru. Popisuje je stránka každého [nástroje](tools.md).


### Upravit intenzitu mezery {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Tahy s malou mezerou (pod 50 %) se rychle sčítají a jsou tak silnější než tahy s větší mezerou. Tento přepínač to vyrovnává, takže tahy mají zhruba stejnou intenzitu bez ohledu na mezeru.

### Mezera mezi tahy {#stroke-spacing}
Jak daleko od sebe se jednotlivé otisky štětce při tažení nanášejí. Hodnoty pod 100 % se překrývají a tah působí souvisle. Hodnoty nad 100 % začnou vytvářet mezery, což se hodí na detaily jako stehy nebo zipy.

### Stabilizátor lano {#lazy-rope-stabilizer}
Tah se táhne za ukazatelem s určitým odstupem. Díky tomu můžete kreslit plynulé čáry.
![](/videos/stroke_lazy_rope.mp4) 

### Vyhlazování tahu {#stroke-smoothing}
Zprůměruje několik poloh ukazatele, takže je tah plynulejší.
Při vysokých hodnotách se tah opožďuje za ukazatelem, ale nakonec ho dožene.
Hodí se pro kreslení plynulých čar.

### Poloměr přichycení {#snap-radius}
Přichytí tah k předchozímu, když ukazatel začne blízko místa, kde poslední tah skončil. Poloměr určuje, jak daleko se konec předchozího tahu hledá. Hodí se při kreslení dlouhých souvislých čar, když často děláte přestávky.

### ![](/icons/trail.webp) Stopa za tahem {#trail}

Když je volba zapnutá, každý nový otisk znovu nanese i několik posledních bodů tahu za sebou. `Počet stop` určuje, kolik bodů se znovu nanese, `Intenzita stopy` jak silné jsou a `Poloměr stopy` o kolik se zvětšují.

Stopa funguje jen s typem tahu `Bod` a nefunguje s [vlivem útlumu](#influence) `Hřbet`.

### ![](/icons/silhouette.webp) Silueta {#silhouette}
![](/images/stroke_silhouette.webp)
Ve výchozím stavu tahy ovlivňují jen povrch modelu uvnitř poloměru štětce. Se zapnutou siluetou se tah promítne skrz celý model. To se velmi hodí při prvotním hrubém modelování nebo u tvarů, jejichž boky mají zůstat kolmé.

Směr promítání můžete nastavit přímo:

* `X`, `Y`, `Z` - promítání podél pevné osy.
* `Zobrazení` - promítání ve směru kamery.
* `Pokud přichycen` - promítání ve směru kamery, ale jen když je kamera přichycená k pohledu. Jinak zůstává tah běžným tahem.
* `Nejbližší` - promítání podél osy nejbližší směru kamery. Toto je výchozí volba.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Náhodně {#randomize}

![](/images/stroke_randomize.webp)

`Intenzita`, `Posun`, `Rotace` a `Měřítko` tahu lze každou zvlášť náhodně měnit. Zaškrtávacím políčkem řádku ji zapnete nebo vypnete. Dá se tak dosáhnout řady efektů, například náhodnost s nástrojem malování vytvoří skvrnitou barvu a s nástrojem rýha zase detaily kůže.

`Perioda (pomalejší)` určuje délku náhodného cyklu: zvyšte ji pro pomalé, plynulé změny, snižte ji pro rychlý šum. Malé tlačítko vedle každého řádku mění periodu jen pro daný řádek.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Náhodně - HSV {#randomize-hsv}

U nástrojů, které malují, lze náhodně měnit také `Odstín`, `Saturace` a `Hodnota` barvy, s vlastní periodou. Skvělé pro jemné barevné variace kůže nebo kamene.

### Posun tahu {#stroke-offset}

Posune tah o stálou vzdálenost, aby ho nezakrýval váš prst. Hodí se na malých obrazovkách. Jde o globální nastavení: zapnete ho zaškrtávacím políčkem a platí pro všechny nástroje.


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

`Alfa` je textura, která upravuje chování štětce.
Je to obrázek ve stupních šedi: černé pixely znamenají žádnou deformaci, bílé plnou deformaci.

Klepnutím na obrázek alfy ji změníte. Kromě vestavěných alf a vašich vlastních importů umí seznam alf stahovat i displacement mapy z Poly Haven.

Klepnutím na náhled materiálu načtete alfu z přednastavení materiálu. Přednastavení materiálu zde také můžete ukládat a zvolit, zda se mají textury vložit do nástroje.

::: tip
Textura se nikdy nezmenšuje, takže velké textury mohou zpomalit výkon.
:::

### ![](/icons/blend_contrast.webp) Opravit alfu {#invert-pixels}
Tlačítko `Opravit...` u importované alfy otevře okno, které opraví samotný obrázek: jeho střední hodnotu, invertování pixelů (černá se změní na bílou a bílá na černou), otočení o 90° a vodorovné nebo svislé převrácení. Soubor obrázku se přepíše, takže opravený obrázek uvidí i ostatní aplikace.

::: tip

Vestavěné alfy, které jsou součástí Nomadu, opravit nelze.

:::

### Projekce {#projection}

Jak se alfa promítá na model:

* `Povrch` - alfa leží na povrchu pod štětcem a sleduje jeho orientaci.
* `Obrazovka` - alfa se promítá přímo z pohledu.
* `Dlaždice` - alfa se promítá z pohledu a zůstává na místě, zatímco přes ni malujete, jako šablona, takže opakující se vzor plynule navazuje. Rotace je zamčená a tlak pera nemění velikost vzoru.
* `Triplanar` - alfa se promítá podél 3 os. Volby měřítka, rotace a dláždění níže nahradí nastavení triplanární textury.

### ![](/icons/diagonal.webp) Stupnice {#scaling}

Štětec v Nomadu je kruh s poloměrem, který si nastavíte. Textury bývají čtvercové nebo obdélníkové a parametry `Stupnice` určují, jak se textura do kruhu vejde. U čtvercové textury se při hodnotě 0,7 vejde do kruhu celá. Hodnota 1 texturu zvětší tak, aby se kruh vešel do ní, a její okraje se ořežou.

![](/images/alpha_scaling.webp) 

Zapnutím `Stupnice Y` můžete alfu roztáhnout svisle. První posuvník se pak změní na `Stupnice X`.

![](/images/alpha_scaling_y.webp) 

`Převrátit vodorovně` zrcadlí alfu zleva doprava.

### Rotace {#rotation}

Textura alfy se otáčí podle směru tahu. Můžete přidat posun rotace, a když je zapnutá ikona zámku, zůstane textura vůči obrazovce zamčená v této rotaci.

Tlačítko s perem vedle ní otáčí alfou, když stylus otáčíte v prstech (barrel roll), u tahů `Zámek + poloměr` a `Zámek + intenzita`, pokud rotace není zamčená. Funguje jen se stylusy, které to podporují.

### Dláždění {#tiling}
![](/images/stroke_tiling.webp) 

Jak často se textura v profilu štětce opakuje. Režimy `Dláždění - X` a `Dláždění - Y` umožňují omezit tah na jedinou texturu (`Nic`), opakovat textury (`Opakovat`) nebo je zrcadlit, kdy je každá druhá textura převrácená, což vytváří vzory nebo pomáhá s navazujícími texturami (`Zrcadlit`). Jsou dostupné s tahem `Otáčet`, s projekcí `Dlaždice` nebo s `Dláždění` větším než 1.

`Pevné uložení (nečtvercové obrázky)` má význam jen u nečtvercových alf a textur štětce. Když je zapnuté, každý obrázek se dláždí samostatně bez mezer. Vypněte ho, pokud chcete, aby alfa a ostatní obrázky zůstaly sladěné i při různém poměru stran.

![](/videos/alpha_tiling.mp4) 



### Střední hodnota {#mid-value}

Ve výchozím stavu znamenají černé pixely žádnou deformaci a bílé plnou kladnou deformaci. Například štětec hlína s alfou kamenů tak povrch vytáhne ven jen tam, kde alfa není černá.

Pokud chcete, aby štětec povrch zatlačoval dovnitř, nebo zároveň zatlačoval dovnitř I vytahoval ven, upravte střední hodnotu. Když ji nastavíte na 0,5, střední šedá v alfě nedělá nic, černá zatlačuje dovnitř a bílá vytahuje ven.

Se správnou hodnotou pomohou dvě tlačítka: čtvercové tlačítko načte střední hodnotu z okraje obrázku a kapátkem ji můžete vybrat přímo na alfě.




## ![](/icons/falloff.webp) Útlum {#falloff}

![](/images/falloff_menu.webp) 

Podobá se [Alfě](#alpha), jen intenzitu řídíte jedinou křivkou. Kombinuje se s alfou, takže texturu můžete použít na detaily a útlum na řízení slábnutí k okrajům a intenzity uprostřed nástroje.

Když je křivka nahoře, jde o plnou deformaci, když je dole, štětec nemá žádný účinek.

Křivku si můžete představit jako průřez špičkou štětce. Spodní část ukazuje náhled jediného „otisku“ štětce na povrchu modelu, a pokud má štětec texturu alfy, zobrazí se i ta, abyste viděli, jak se útlum a alfa navzájem ovlivňují.

### ![](/icons/fx.webp) Přednastavení {#preset}
Když je vybrané `Přednastavení...`, klepnutím na graf křivky otevřete nabídku přednastavení. Zaoblené křivky dávají měkčí výsledky, hranaté ostřejší. Tlačítko `Méně` v levém panelu nástrojů útlum v podstatě obrátí, takže vrchol křivky povrch zatlačí dovnitř místo vytažení ven, nebo naopak.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Když je tato volba vybraná, můžete si nakreslit vlastní křivky útlumu. Editor křivky funguje stejně jako křivky ve zbytku Nomadu:

* Klepnutím na křivku vytvoříte nový bod
* Tažením bodu změníte jeho polohu
* Klepnutím na bod přepnete mezi ostrým a hladkým
* Přetažením bodu na sousední bod ho odstraníte

### ![](/icons/curve_bspline.webp) B-splajn {#b-spline}
Když je tato volba vybraná, můžete si nakreslit vlastní křivky útlumu. Editor funguje stejně jako Catmull-Rom, ale body křivku jen ovlivňují místo toho, aby ležely přímo na ní, což pomáhá vytvářet hladší tvary křivek.

### ![](/icons/curve_bevel.webp) Zkosení {#bevel}
Body jsou spojené rovnými čarami se zaoblenými rohy, jejichž velikost závisí na ostrosti každého bodu. Hodí se pro štětce s plochým vrcholem a čistým zkosením na okraji.

Editor křivky má 3 tlačítka:

| Položka        | Ikona                       | Popis                                        |
| :------------: | :-------------------------: | :------------------------------------------: |
| Maximalizovat  | ![](/icons/maximize.webp)  | Zvětší editor křivky                         |
| Resetovat      | ![](/icons/reset.webp)     | Vrátí křivku do výchozího stavu              |
| Symetrie       | ![](/icons/symmetric.webp) | Zobrazí křivku jako symetrickou „špičku štětce“ |


### Vliv {#influence}

* `Koule` (3d) - vliv se počítá ze vzdálenosti vrcholu od středu štětce.
* `Kruh` (2d) - vrchol se nejprve promítne na rovinu oblasti a teprve pak se měří jeho vzdálenost od středu štětce. Podobně se vzorkují alfy. 
* `Válec` - vliv se promítá skrz oblast jako válec. Je to totéž jako zapnout [Siluetu](#silhouette-1) níže.
* `Hřbet` - útlum se měří napříč tahem, takže křivka se stane průřezem celého tahu. Tlačítko `Sym` pak profil zrcadlí napříč tahem: upravíte jednu stranu a druhá ji následuje. Když je vypnuté, křivka vede od levé strany tahu k pravé. Není k dispozici u nástrojů založených na zploštění.

### ![](/icons/silhouette.webp) Silueta {#silhouette-1}
Ve výchozím stavu tahy ovlivňují jen povrch modelu uvnitř poloměru štětce. Se zapnutou siluetou se tah promítne skrz celý model. To se velmi hodí při prvotním hrubém modelování nebo u tvarů, jejichž boky mají zůstat kolmé. Nabízí stejné volby promítání jako [Silueta](#silhouette) na kartě Tah.



## ![](/icons/filter.webp) Filtr {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Akumulovat tah {#accumulate-stroke}
Zruší omezení, kolik hmoty lze jedním tahem přidat nebo ubrat. Například nástroj `Hlína` má tuto volbu zapnutou, takže materiál se může stále vrstvit, zatímco nástroj `Štětec` ji má vypnutou, takže tah přestane přidávat materiál, když jím opakovaně přejíždíte přes stejnou oblast sítě. 

### ![](/icons/culling.webp) Pouze přivrácené vrcholy {#front-facing-vertex-only}
Tato volba ignoruje odvrácené vrcholy.
Hodí se, když chcete malovat na část tenké geometrie a nezasáhnout přitom druhou stranu.
Funguje i při sochání, ale mohou se objevit artefakty.

### ![](/icons/eye_open.webp) Jen viditelné vrcholy {#visible-vertex-only}
Ignoruje vrcholy skryté z pohledu kamery za jinými povrchy. Tato volba se zobrazuje u tvarových tahů (laso, obdélník...) nástrojů pro maskování a malování a nástrojů `SkupinaPovrch` a `Skrýt`.

### ![](/icons/dynamic.webp) Povolit dynamickou topologii {#allow-dynamic-topology}
Tato volba je dostupná, jen pokud je vaše síť v režimu [Dynamická topologie](topology.md#dynamic-topology). Dynamickou topologii tak můžete vypnout nebo zapnout pro každý nástroj zvlášť.

### ![](/icons/connect.webp) Propojená topologie {#connected-topology}
Sochá jen vrcholy propojené s povrchem, kterého se nástrojem dotknete. Například s nástrojem `Přesunout` tak můžete posunout část modelu, i když se protíná s jinou částí.
![](/videos/connected_topology.mp4)

### Chránit oblast {#protect-area}
![](/images/filter_protect_area.webp) 

Tyto volby zabrání nástrojům ovlivňovat části sítě za různých podmínek. Každou můžete nastavit na `Auto`, `Ne` nebo `Ano` a malá šipka ukazuje, čemu `Auto` právě odpovídá.

* `Skrýt` - pokud jsou části sítě skryté nástrojem skrýt, určuje, zda mají být chráněné. Při `Auto` jsou skryté plochy chráněné, pokud není viditelný jejich drátový model (viz nastavení [Drátový model](settings.md#wireframe)).
* `Maska` - pokud jsou části sítě zamaskované, určuje, zda mají být chráněné. Při `Auto` jsou zamaskované části chráněné, dokud je maska viditelná v nabídce [Stínování](shading).
* `SkupinaPovrch` - určuje, zda lze nástroj použít jen uvnitř první skupiny ploch, které se dotknete. Při `Auto` se řídí tím, zda jsou skupiny ploch viditelné v nabídce [Stínování](shading).

Tlačítko `(Vše)` určuje, zda jsou tyto ochrany globální, sdílené všemi nástroji, nebo nastavené pro každý nástroj zvlášť.


### Vzorkování oblasti {#area-sampling}
Některé štětce nebo volby tahu potřebují ke své práci normálu a polohu roviny vůči povrchu.

Způsob výpočtu této průměrné roviny můžete řídit nastavením oblasti vzorkování jako poměru k poloměru nástroje.

Při 100 % se bere v úvahu každý bod uvnitř kruhu výběru.

Při 0 % se bere v úvahu jen nejbližší vrchol nebo trojúhelník. Hodnoty `Poloměr normálnosti` a `Poloměr pozice` můžete propojit, nebo je odemknout a nastavit každou zvlášť.

### Filtr normál podle oblasti {#keep-sharp-edges}
Vyloučí body, jejichž normály se příliš odchylují od normály povrchu.

Mění to výpočet roviny oblasti (Vzorkování oblasti), takže se to hodí hlavně u nástrojů typu hlína nebo zploštění, případně když chcete obarvit převážně rovný povrch, aniž by barva přetekla.

Úhly `Min` a `Max` řídí přechod mezi vyloučenými a plně ovlivněnými body, jak ukazuje malý barevný kotouč vedle nich.

![](/videos/filter_keep_sharp_edges.mp4)

### Filtr normál v doznívání {#falloff-normal-filter}
Podobně jako [Filtr normál podle oblasti](#keep-sharp-edges) vylučuje body, jejichž normály se příliš odchylují od normály povrchu, ale působí na útlum štětce místo výpočtu roviny. Hodí se pro malování rýh nebo hrbolků.


### Maskování hloubky {#depth-masking}
![](/images/stroke_depthmask.webp)

Vyloučí body, které jsou nad nebo pod určitou vzdáleností od vypočtené roviny (Vzorkování oblasti).

Můžete tak malovat jen na hrbolaté oblasti, nebo jen do prohlubní.

Graf znázorňuje průřez povrchem: vodorovná čára je povrch, kruh znázorňuje poloměr útlumu malby nad a pod povrchem. `Převýšení výšky` je procento nad nebo pod povrchem, od kterého začíná výpočet maskování. Se zapnutým `Spád hloubky` můžete posuvníky `Horní oblast` a `Dolní oblast` měnit velikost útlumu nad a pod bodem posunu.

#### Příklad: malování do prohlubní {#example-paint-in-cavities}
Chcete-li malovat jen do prohlubní, nastavte převýšení výšky na -100 % a posuvník horní oblasti upravte tak, aby byl od vodorovné čáry vzdálený. První klepnutí tak nastaví „nulovou“ hloubku a ovlivněny budou jen oblasti pod ní.

![](/videos/stroke_depth_cavity.mp4)

#### Příklad: malování na hrbolky {#example-paint-on-bumps}
Chcete-li malovat jen na vyvýšená místa, nastavte převýšení výšky na +90 %, aby spodek kruhu jen o kousek protínal vodorovnou čáru. Když klepnete na vrchol „vyvýšené“ oblasti, nastaví se hloubka tak, že se namaluje vše v této hloubce, kousek pod ní a vše výš. Hluboké prohlubně se přeskočí.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Tlak {#pressure}
![](/images/pressure_menu.webp) 

Určuje, jak tlak stylusu či pera ovlivňuje štětce.

### Použít globální nastavení {#use-global-settings}

Ve výchozím stavu je `Použít globální nastavení` zapnuté, takže všechny štětce sdílejí stejné hodnoty tlaku. Zrušte zaškrtnutí, pokud chcete aktuálnímu nástroji dát vlastní nastavení tlaku.

### ![](/icons/radius.webp) Poloměr {#pressure-radius}

Tato křivka určuje, jak tlak ovlivňuje poloměr štětce. Výchozí vztah je lineární, takže pokud má váš stylus plynulou odezvu, měla by i změna poloměru působit plynule. Mnoho stylusů má ale nelineární odezvu, kterou touto křivkou můžete vyrovnat. Pokud například máte pocit, že poloměr při silném tlaku nedosáhne maxima, použijte přednastavení křivky jako „out-pow3“, které se ohýbá nahoru, aby poloměr rostl dříve.

Toto okno se podobá zobrazení křivky útlumu: klepnutím do okna křivky použijete přednastavení, nebo si vlastní křivky nakreslíte v režimech `Catmull-Rom`, `B-splajn` a `Zkosení`.

Pokud chcete stálý poloměr, tuto sekci vypněte.

### ![](/icons/intensity.webp) Intenzita {#pressure-intensity}

Podobá se křivce poloměru, ale řídí intenzitu. Pokud chcete stálou intenzitu, tuto sekci vypněte.

### Omezit tlak na 100% {#limit-pressure}

Zajistí, že tlak stylusu nikdy nepřekročí 100 %. Jde o globální nastavení.

### Vyhlazování tlaku {#pressure-smoothing}

Zprůměruje události tlaku stylusu, takže výsledky jsou plynulejší.
