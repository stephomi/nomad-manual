# ![](/icons/pencil.webp) Tah    

---
![](/images/stroke_overview.webp) 

## Přehled 

Chování tahu můžete přizpůsobit u většiny nástrojových štětců.
Nastavení je podobné těm v 2D malovacích aplikacích, některé volby jsou ale specifické pro sochání a 3D.

Možnosti jsou rozdělené do 5 podnabídek:

| Název    | Ikona                        | Popis                                                              |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Řídí, jak je tah aplikován na model                                |
| Alpha    | ![](/icons/alpha.webp)      | Jak je šedotónová textura použita pro otisk štětce                |
| Falloff  | ![](/icons/falloff.webp)    | Řídí, jak se síla štětce mění od středu k okraji                   |
| Filter   | ![](/icons/filter.webp)     | Jak je štětec ovlivněn geometrií modelu                            |
| Pressure | ![](/icons/pressure.webp)   | Řídí odezvu na tlak stylusu                                        |

::: tip
Ne všechny volby tahu platí pro všechny nástroje. Volby tahu, které aktuální nástroj nepoužívá, budou zakázané nebo skryté. 
:::


## Stroke

### Poloměr

![](/images/stroke_radius.webp)

#### Sdílet poloměr

Je-li zapnuto, všechny nástroje budou používat stejný poloměr; výchozí chování je, že každý nástroj má svůj vlastní poloměr.

#### Velikost

* Screen – poloměr je nastaven v jednotkách obrazovky. Pokud nastavíte poloměr na šířku 100 pixelů, zůstane 100 pixelů široký bez ohledu na přiblížení nebo oddálení.
* Constant (3d) – poloměr je nastaven v 3D jednotkách. Například pokud vytvoříte kouli a nastavíte poloměr na stejnou velikost jako koule, poloměr zůstane stejně velký jako koule při přibližování i oddalování.


### Tah

![](/images/stroke_strokemode.webp)

Tahy mohou fungovat v několika režimech:

### ![](/icons/stroke_dot.webp) Dot
Táhněte jako běžný malířský tah. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
Alfa štětce se bude otáčet podle směru tahu, užitečné pro vytváření stehů na látce. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
 Otiskne tah štětce s pevnou **_výškou_**. Tažením nastavíte měřítko a rotaci.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Otiskne tah štětce s pevným **_poloměrem_**. Tažením nastavíte výšku a rotaci.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Nástroje `Move` a `Drag` mají své vlastní 3 volby:

### ![](/icons/snake.webp) Drag

Během tahu bude neustále aktualizovat to, co je uvnitř poloměru štětce. Rychlý tah nechá povrch za sebou, zatímco pomalý tah bude „držet“ materiál a vytvářet delší tvary. Toto je výchozí režim pro nástroj `Drag`. S `Dynamic Topology` lze použít k vytváření hadovitých extruzí. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Při spuštění štětce vybere to, co je uvnitř poloměru štětce, a toto výběrové území si ponechá. To je užitečné pro přesnější přesuny, protože můžete pečlivě upravit vzdálenost posunu a omylem neposunout víc, než jste původně vybrali. Toto je výchozí režim pro nástroj `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
Uživatelský poloměr je ignorován a dynamicky se nastavuje podle toho, jak daleko je tah tažen od počátečního bodu. Malá vzdálenost = malý poloměr, větší vzdálenost = větší poloměr. Pomocí posuvníku intenzity ovládáte tvar falloffu. Užitečné pro blokování organických gumových tvarů.
![](/videos/stroke_lockradius_drag.mp4) 



### Upravit intenzitu rozestupu
![](/images/stroke_space_smooth.webp)

Tahy s malým rozestupem (nižším než 50 %) se mohou rychle kumulovat a vytvářet intenzivnější tahy než vyšší hodnoty rozestupu. Toto přepínání to kompenzuje, takže tahy budou přibližně stejně intenzivní bez ohledu na rozestup.

### Rozestup tahu
Jak daleko od sebe se má aplikovat každý otisk štětce během tažení. Hodnoty nižší než 100 % se budou překrývat a vytvářet dojem souvislého tahu. Hodnoty vyšší než 100 % začnou zanechávat mezery, což je užitečné pro sochání detailů jako švy nebo zipy.

### Lazy rope stabilizer
Tahy budou zaostávat za pozicí ukazatele o určitou vzdálenost. To lze použít k kreslení hladkých čar.
![](/videos/stroke_lazy_rope.mp4) 

### Vyhlazování tahu
Průměruje více pozic ukazatele pro hladší tah.
Při vysokých hodnotách bude tah zaostávat za ukazatelem, ale nakonec ho dožene.
To je užitečné pro kreslení hladkých čar.

### Snap radius
Přichytí začátek tahu ke konci předchozího tahu. Poloměr určuje, jak daleko se má hledat konec předchozího tahu. To může být užitečné při kreslení dlouhých souvislých čar s častými pauzami.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Ve výchozím nastavení tahy ovlivňují pouze povrch modelu v rámci poloměru štětce. Když je silueta zapnutá, tah bude promítán skrz celý model. To může být velmi užitečné při počátečním blokování modelu nebo pro tvary, které vyžadují, aby boky zůstaly kolmé.

Směr projekce lze nastavit explicitně, výchozí metoda „Closest“ detekuje nejlepší úhel vzhledem k pohledu. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

Intenzita, posun, rotace a měřítko tahu mohou být náhodně měněny. To lze použít k vytvoření různých efektů, např. náhodnění s nástrojem paint může vytvořit skvrnitou barvu, nebo náhodnění s nástrojem crease lze použít k tvorbě detailů kůže.

![](/videos/stroke_randomize.mp4) 

### Posun tahu

Aplikuje na tah konstantní posun. To je užitečné pro malé obrazovky, kde by váš prst zakrýval tah. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

`Alpha` je textura, která moduluje chování štětce.
Je to šedotónový obrázek, kde černé pixely znamenají žádnou deformaci a bílé pixely plnou deformaci.

Kliknutím na obrázek alfy ji změníte.

Kliknutím na náhled materiálu načtete alfu z přednastavení materiálu. Zde můžete také ukládat přednastavení materiálů a zvolit, zda se mají textury s nástrojem vkládat.

::: tip
Textura se nikdy nemění velikostí, takže velké textury mohou zpomalit výkon.
:::

### Invertovat pixely
Obrátí hodnoty obrázku, takže černé pixely se stanou bílými a bílé pixely černými.

::: tip

Vestavěné alfy dodávané s Nomad nelze invertovat.

:::

### Škálování

Velikost štětce v Nomad je kruh s uživatelem definovaným poloměrem. Textury jsou často čtvercové nebo obdélníkové, parametry `Scaling` vám umožní rozhodnout, jak má textura do kruhu zapadnout. Pro čtvercovou texturu hodnota 0,7 zapadne do kruhu. Hodnota 1 zvětší texturu tak, aby se kruh vešel dovnitř, přičemž okraje budou oříznuty.

![](/images/alpha_scaling.webp) 

Zapnutím `Scaling - Y` můžete alfu vertikálně roztahovat.

![](/images/alpha_scaling_y.webp) 

### Rotace

Textura alfy se bude otáčet podle směru tahu. Můžete přidat rotační offset a pokud je ikona zámku zapnutá, textura zůstane uzamčená v této rotaci vzhledem k obrazovce.

### Dlaždicování
![](/images/stroke_tiling.webp) 

Jak často se textura opakuje v profilu štětce. Režimy dlaždicování umožňují omezit se na jednu texturu v rámci tahu, opakované textury nebo zrcadlené, kde je každá druhá textura převrácená, aby se vytvořily vzory nebo pomohlo vytvářet bezešvé textury.

![](/videos/alpha_tiling.mp4) 



### Střední hodnota

Ve výchozím nastavení černé pixely znamenají žádnou deformaci a bílé pixely plnou kladnou deformaci, takže například clay štětec s alfa texturou kamenů bude povrch vytahovat ven pouze tam, kde alfa není černá.

Pokud chcete, aby štětec povrch vtlačoval dovnitř nebo zároveň vtlačoval i vytahoval, můžete upravit střední hodnotu. Pokud ji nastavíte na 0,5, střední šedá v alfě nebude dělat nic, černá bude vtlačovat dovnitř, bílá vytahovat ven.




## Falloff

![](/images/falloff_menu.webp) 

Je podobný [Alfa](#alpha), ale intenzitu řídíte jednou křivkou. Ta se kombinuje s alfou, takže můžete použít texturu pro detail a falloff pro řízení vytrácení okrajů a intenzity ve středu nástroje.

Když je křivka nahoře, jde o plnou deformaci, když je dole, štětec nemá žádný efekt.

Křivku si můžete představit jako průřez špičkou štětce. Spodní část zobrazuje náhled toho, jak by vypadal jeden „otisk“ štětce na povrchu modelu, a pokud má štětec alfa texturu, zobrazí se také, aby bylo vidět, jak se falloff a alfa ovlivní.

### Preset
Je-li vybráno, kliknutím na graf křivky se zobrazí nabídka presetů. Zaoblené křivky dávají měkčí výsledky, hranaté křivky ostřejší. Tlačítko `Sub` v levém panelu v podstatě obrátí falloff, takže vršek křivky bude povrch vtlačovat místo vytahování ven, nebo naopak.

### Catmull-Rom
Při výběru může uživatel kreslit vlastní křivky falloffu. Editor křivek funguje stejně jako křivky ve zbytku Nomad:

* Kliknutím na křivku vytvoříte nový bod
* Tažením bod přesunete
* Kliknutím na bod přepínáte mezi ostrým a hladkým
* Přetažením bodu do sousedního bodu ho odstraníte

### B-spline
Při výběru může uživatel kreslit vlastní křivky falloffu. Editor funguje stejně jako Catmull-Rom, ale body křivku ovlivňují, místo aby na ní ležely přímo, což může pomoci vytvářet hladší tvary křivek.

Editor křivek má 3 tlačítka:

| Položka  | Ikona                       | Popis                                       |
| :------: | :-------------------------: | :-----------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Rozbalí editor křivky                      |
| Reset    | ![](/icons/reset.webp)     | Vrátí křivku do výchozího stavu            |
| Symmetry | ![](/icons/symmetric.webp) | Zobrazí křivku jako symetrickou „špičku“   |


### Vliv

* Sphere (3d) – Vliv se počítá podle vzdálenosti vrcholu od středu štětce.
* Circle (2d) – Vrchol se nejprve promítne do roviny oblasti a pak se bere jeho vzdálenost od středu štětce. Je to podobné tomu, jak se samplují alfy. 
* Cylinder – Vliv je promítán skrz oblast jako válec, používá se v režimu Silhouette níže.

### Silhouette
Ve výchozím nastavení tahy ovlivňují pouze povrch modelu v rámci poloměru štětce. Když je silueta zapnutá, tah bude promítán skrz celý model. To může být velmi užitečné při počátečním blokování modelu nebo pro tvary, které vyžadují, aby boky zůstaly kolmé.



## Filter

![](/images/filter_menu.webp) 

### Akumulovat tah
Povolí neomezené množství materiálu, které lze přidat/odebrat jedním tahem. Např. nástroj `Clay` to má zapnuté, takže materiál se může stále nabalovat, zatímco nástroj `Brush` to má vypnuté, takže tahy přestanou přidávat materiál, pokud budete stejným tahem jezdit po stejné oblasti sítě. 

### Pouze čelní vrcholy
Tato volba ignoruje zadní vrcholy.
Může být užitečná, pokud chcete malovat část tenké geometrie bez ovlivnění druhé strany.
Funguje i pro sochání, ale můžete zaznamenat některé artefakty.

### Povolit dynamickou topologii
Tato volba je dostupná pouze pokud je vaše síť v režimu [Dynamic Topology](topology.md#dynamic-topology). Dynamickou topologii můžete povolit nebo zakázat pro každý nástroj zvlášť.

### Connected topology
Povolí sochat pouze vrcholy, které jsou propojené s povrchem, kterého se nástrojem dotknete. Například při použití s nástrojem `Move` vám to umožní posunout část, i když se protíná s jinou částí.
![](/videos/connected_topology.mp4)

### Protect Area
![](/images/filter_protect_area.webp) 

Tyto volby zastaví nástroje v ovlivňování částí sítě za různých podmínek. 

Volba „Auto“ znamená, že pokud máte v nabídce [Shading](shading) zapnuté hide, mask nebo facegroup, budou chráněny, ale pokud jsou v této nabídce vypnuté, ochrana je deaktivována.

* `All` – Přepínač, zda jsou ochranné filtry globální, nebo pro každý nástroj zvlášť.
* `Hide` – Pokud jsou části sítě skryté nástrojem hide, nastaví, zda mají být chráněny.
* `Mask` – Pokud jsou části sítě maskované, nastaví, zda mají být chráněny.
* `Facegroup` – Nastaví, zda můžete nástroj použít pouze v rámci první dotčené facegroup.


### Zachovat ostré hrany
Vynechá body, jejichž normály se příliš liší od normály povrchu.

Změní způsob výpočtu roviny oblasti (Area sampling).

Tato volba může být užitečná pro nástroje založené na zarovnání do roviny nebo pokud chcete barvit převážně plochý povrch bez přetékání přes hrany.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Některé štětce nebo volby tahu vyžadují pro svou funkci normálu roviny a pozici roviny vůči povrchu.

Můžete řídit, jak se tato průměrná rovina počítá, nastavením vzorkovací oblasti jako poměru k poloměru nástroje.

Při 100 % se berou v úvahu všechny body uvnitř výběrového kruhu.

Při 0 % se bere v úvahu pouze nejbližší vrchol nebo trojúhelník. Tyto hodnoty mohou být propojené pro `Normal radius` i `Position radius`, nebo odemčené a nastavené nezávisle.


### Depth masking
![](/images/stroke_depthmask.webp)

Vynechá body, které jsou nad nebo pod určitou vzdáleností od vypočtené roviny (Area sampling).

To lze použít k malování pouze na hrbolatých oblastech nebo pouze v dutinách.

Graf představuje průřez povrchem; vodorovná čára je místo, kde je povrch, kruh představuje poloměr falloffu malby relativně nad a pod povrchem. `Height offset` je procento nad nebo pod povrchem, kde se začne výpočet maskování. `Top area` a `Bottom area` umožňují škálovat falloff nad a pod bodem offsetu.

#### Příklad: Malování v dutinách
Chcete-li malovat pouze dutiny, nastavte height offset na -100 % a upravte posuvník top area tak, aby byl dál od vodorovné čáry. To znamená, že první kliknutí nastaví „nulovou“ hloubku a pak budou ovlivněny pouze oblasti pod touto hloubkou.

![](/videos/stroke_depth_cavity.mp4)

#### Příklad: Malování na hrbolech
Chcete-li malovat pouze ve vysokých oblastech, nastavte height offset na +90 %, aby se spodní část kruhu malým kouskem protínala s vodorovnou čarou. Když kliknete na vrchol „vysoké“ zóny, nastaví se tím hloubka tak, že vše v této hloubce, plus trochu pod ní a vše nad ní, bude malováno. Hluboké dutiny budou přeskočeny.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Řídí, jak tlak stylusu/pera ovlivňuje štětce.

Ve výchozím nastavení je zapnuto `Use global settings`, což znamená, že všechny štětce sdílejí stejné hodnoty tlaku.

### Pressure - Radius

Tato křivka řídí, jak je poloměr štětce ovlivněn tlakem. Výchozí je lineární vztah, takže pokud má váš stylus plynulou odezvu, změna poloměru by měla také působit plynule. Mnoho stylusů má ale nelineární odezvu, kterou můžete touto křivkou kompenzovat. Například pokud máte pocit, že se poloměr při vysokém tlaku nedostane na maximální hodnotu, použijte preset křivky jako „out-pow3“ s ohybem směřujícím nahoru, aby se poloměr zvyšoval dříve.

Tento dialog je podobný zobrazení křivky falloffu, můžete použít preset klepnutím do okna křivky nebo kreslit vlastní křivky v režimech Catmull-Rom a B-Spline.

Pokud chcete konstantní poloměr, tuto sekci vypněte.

### Pressure - Intensity

Podobné jako u poloměru, ale pro řízení intenzity. Pokud chcete konstantní intenzitu, tuto sekci vypněte.

### Vyhlazování tlaku

Průměruje události tlaku stylusu pro hladší výsledky.
