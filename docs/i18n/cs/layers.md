# ![](/icons/layer.webp) Vrstvy 

Tato nabídka obsahuje zásobník vrstev – způsob, jak ne‑destruktivně ukládat úpravy objektu – a mnoho možností, jak vrstvy kombinovat a znovu využívat.

![](/images/layers_overview.webp) 

## Přehled

Vrstvy v Nomadu slouží k více účelům.

Informace o malbě (Barva, Drsnost, Kovovost, Krytí) fungují s vrstvami podobně jako v 2D malovacích aplikacích. Lze vytvořit vrstvu a na model malovat. Vrstva může být zapínána/vypínána, lze jí měnit krytí, vrstvu lze duplikovat, měnit její pořadí v zásobníku vrstev a upravovat její režim prolnutí.

Nomad také používá vrstvy pro sochání. Vrstva může uchovávat jemné detaily jako vrásky, nebo i velké změny, takže může fungovat jako blendshape/shape key/morph target v jiných 3D aplikacích. Například můžete vymodelovat různé výrazy obličeje na různých vrstvách a pomocí posuvníků vrstev je kombinovat do nových výrazů.

V tomto případě jsou změny uložené ve vrstvě čistě aditivní, pořadí vrstev nemá význam jako u malby.

Vrstvy lze částečně mazat pomocí nástroje [Delete Layer](tools.md#delete-layer) a vrstvy lze také použít k vytváření masek na základě různých informací uložených ve vrstvě.

![](/videos/layer.mp4)

::: tip
Na rozdíl od většiny sochařského softwaru změna topologie meshe vrstvy neodstraní. Můžete použít [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multiresolution) nebo nástroje [Trim](tools.md#trim)/[Split](tools.md#split), ale pamatujte, že při použití [Voxel Remesher](topology.md#voxel-remesher) bude kvalita vrstvy ovlivněna.
:::

::: tip
Pokud používáte vrstvy jako blendshapes/morph targets, je v [nabídce scény](scene.md#object-menu) k dispozici rozšířená funkcionalita vrstev. Můžete rozdělit vrstvy na objekty a kombinovat odpovídající objekty zpět do vrstev.
:::
----

## Nabídka vrstev 

![](/images/layers_menu.webp)

Stisknutím `Add layer` vytvoříte novou vrstvu.

Každá vrstva má název, posuvník pro ovládání její síly/faktoru a tlačítka voleb.

### Možnosti

| Akce        | Ikona                        | Popis                                               |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Viditelnost | ![](/icons/eye_open.webp)   | Zobrazit/skrýt vrstvu                               |
| Režim prolnutí | ![](/icons/opacity.webp) | Photoshop‑styl režimu prolnutí. Čtyři ikony zobrazují režimy pro Barvu, Drsnost, Kovovost, Krytí. |
| Upravit název | ![](/icons/pencil.webp)   | Upravit název vrstvy                                |
| Smazat      | ![](/icons/trash.webp)      | Smazat vrstvu                                       |
| Duplikovat  | ![](/icons/clone.webp)      | Duplikovat vrstvu                                   |
| Sloučit dolů | ![](/icons/merge_down.webp) | Sloučit vrstvu s nižší vrstvou (nebo základním meshem) |
| Více        | ![](/icons/more.webp)       | Možnosti [More...](#more)                           |

Pro přesunutí vrstvy na jiné místo v zásobníku vrstev podržte prst na jejím názvu a přetáhněte ji.

### More...

Tlačítko „More...” zobrazí další možnosti pro aktuální vrstvu:

![](/images/layers_more.webp) 

#### Faktory kanálů

Tato nastavení umožňují škálovat množství sochání/barvy/drsnosti/kovovosti/krytí pro danou vrstvu. Tyto hodnoty se násobí proti posuvníku faktoru vrstvy, takže například pokud je síla vrstvy 1, ale faktor kanálu barvy je 0,5, pak bude barva zobrazena s poloviční silou 0,5.

`Offset` ovládá sílu sochařské části vrstvy. Zatímco barva/drsnost/kovovost jsou omezovány mezi 0 a 1, offset může nabývat libovolných hodnot, kladných i záporných. 

::: tip
Offset lze použít k proměně vrstvy hrbolků ve vrstvu prohlubní, nebo úsměvu v mračení:
![](/videos/layer_happysad.mp4)


Symetrickou vrstvu lze naklonovat a poté rozdělit na levý/pravý tvar pomocí del layer:
![](/videos/layer_leftright.mp4)

Vrstvy se zápornými offset faktory lze vypéct do prázdných vrstev a vytvořit z nich nové kladné tvary.

Vrstvy s kladnými offset faktory nad 1 lze použít k experimentování s extrémnějšími blendshapes.
:::

::: warning
V tuto chvíli vrstvy sdílejí jediný kanál krytí pro všechny 3 kanály (barva/kovovost/drsnost).
Pokud sloučíte více vrstev s intenzitou na úrovni kanálů, které nejsou na plné hodnotě, je možné, že konečný výsledek bude vypadat jinak.

Možná v budoucnu bude mít každý kanál svůj vlastní alfa kanál, aby se toto omezení odstranilo.
:::


#### ![](/icons/tool_mask.webp) Mask
Tlačítko masky vedle každého posuvníku vytvoří masku z daného kanálu. Podobně jako používání vrstev k vytváření výběrů v malovacích aplikacích vám to umožní znovu použít práci provedenou ve vrstvě pro jiné operace.

#### ![](/icons/preview.webp) Preview
![](/images/layers_preview.webp) 

Po zapnutí zobrazí náhled nastavení extrakce pro tuto vrstvu (viz další sekce).

Když je zapnutý rentgen (xray), bude plný pouze extrahovaný tvar, zbytek tvaru bude průhledný, což je užitečné, pokud používáte záporné výšky extrakce.

#### Extract
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Tlačítko `Extract` duplikuje obsah vrstvy do nového objektu, obvykle s uživatelem zadanou tloušťkou nastavenou v následující sekci.

`Closing action` určuje, jak bude duplikace provedena:

* None – Jednoduše část extrahovat, nepokoušet se generovat boky ani vyplňovat díry.
* Fill – Díra je vyplněna a vyhlazena trojúhelníky. Nepoužívejte tuto možnost pro rovné plochy.
* Shell – Uzavřít extrahovaný tvar s použitím hodnoty tloušťky a voleb směru.
* Layer – Extrahovat rozdíl vrstvy.

#### ![](/icons/height.webp) Thickness
![](/images/layers_thickness.webp) 

Hloubka skořepinové extruze. Kladné hodnoty rostou ven z povrchu, záporné hodnoty rostou do povrchu.

Plus/mínus vedle této hodnoty nastavuje směr extruze:
* Minus ( - ) začne od aktuálního povrchu a extruduje dolů. 
* Plus ( + ) začne od aktuálního povrchu a extruduje nahoru.
* PlusMinus ( ± ) odtlačí horní i spodní část extruze o stejnou hodnotu, takže bude napůl zapuštěná v původním povrchu.

#### Smoothness
![](/images/layers_smoothness.webp) 

Pokud jsou okraje oblasti, která má být extrahována, zubaté, tento posuvník se pokusí okraj rozmazat do hladšího tvaru. 

#### ![](/icons/height.webp) Edge loop (side)
![](/images/layers_edgeloop.webp) 

Tato sekce je viditelná, když je closing action nastaveno na „Shell”. 

`Auto Edge-loop (side)` vypočítá počet edge loopů podél boků skořepiny tak, aby vznikly čtvercové polygony. 

Pokud je vypnuto, posuvník `Division` nastaví počet dělení na bocích.

_Toto je konec podnabídky „More...“._

### Advanced
![](/images/layers_advanced.webp)

#### Keep top layers details

Zajistí, aby malé detaily na vyšších vrstvách zůstaly viditelné, když se na nižších vrstvách provádějí velké změny.

Ve výchozím nastavení, pokud na vrstvě vymodelujete malé vrásky a poté provedete velké změny na základní vrstvě, vrásky se ztratí. Zapnutí tohoto přepínače umožní, aby tyto malé detaily vždy „plavaly“ nad spodními velkými změnami. V následujícím videu uvidíte, jak se detail vrásek ve výchozím stavu odstraní, ale zůstane viditelný, když je „keep top layers details“ zapnuté:

![](/videos/layers_details.mp4)


#### UI: Expand list

Výchozí nabídka vrstev umožňuje přepínat viditelnost vrstev a jejich krytí. Zapnutím této volby se rozbalí úplné ovládací prvky pro každou vrstvu.

![](/images/layers_expand.webp)

#### Sync transform

Pokud je zapnuto, všechny nevybrané vrstvy budou upraveny v závislosti na transformaci – rotaci, měřítku, zkosení. 

Vypněte tuto volbu, pokud mají být ostatní vrstvy používány bez nové transformace, kterou aplikujete.

Když je nastaveno na `Auto`, budou upraveny pouze viditelné vrstvy.
