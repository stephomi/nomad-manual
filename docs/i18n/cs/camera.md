# ![](/icons/camera.webp) Kamera {#camera}

V této nabídce můžete vytvářet a upravovat kamery a také nastavit, jak s kamerou pracujete.

![](/images/camera_overview2.webp)

Kamery mají v Nomadu několik využití:

* Nastavení pohledů pro modelování z přesných úhlů
* Jako fotoaparát k zarámování vašich objektů
* Jako kamera z pohledu první osoby k pohybu po scéně
* Jako ortografická kamera pro izometrické hry nebo technicky laděné rendery.

## Ovládání kamery {#control}

### Rotace {#rotation}
Kameru otáčíte tažením *jedním* prstem po pozadí.
Když táhnete prstem po modelu, začnete místo toho modelovat.

::: tip Můžu otáčet kamerou, když se nedostanu k pozadí?
Ano, položte na obrazovku *dva* prsty, jako byste chtěli začít gesto posunu nebo přiblížení, a pak *jeden* prst zvedněte.
:::

### Zaostření / reset {#focus}
*Dvojitým klepnutím* na model zaostříte na vybraný bod.
Když *dvakrát klepnete* na pozadí, kamera místo toho zaostří na vybranou síť nebo celou scénu, viz [Dvakrát klepněte na pozadí](#dtap-tap-background).


### Posun {#translation}
Pohybem *dvou* prstů kameru posouváte.


### Přibližování {#zooming}
Gestem sevření prstů přibližujete a oddalujete.


### Naklánění {#rolling}
Pohled můžete *naklánět* otáčením *dvou* prstů.
::: warning
Toto gesto je dostupné jen v režimech rotace `Trackball`.
:::

### Ovládání na počítači {#desktop}

Na počítači se kamera ovládá klávesou Alt/Option:

* tažení hrotem v prázdném prostoru = otáčení kamery
* Alt + tažení hrotem = posun
* Alt + tažení hrotem a pak puštění Alt = přiblížení (stejně jako v ZBrush)

U tabletů Wacom s pery, která mají 2 nebo více tlačítek, nastavte v nastavení Wacom hrot a tlačítka takto:

* hrot = levé kliknutí
* spodní tlačítko = prostřední kliknutí
* horní tlačítko = pravé kliknutí

S tímto nastavením můžete kameru ovládat čistě perem:

* horní tlačítko a pohyb perem nad displejem = otáčení kamery
* spodní tlačítko a pohyb perem nad displejem = posun

## Ovládání kamer {#camera-controls}

![](/images/camera_list.webp)

### Pohledy {#views}
Pohledy kamery si můžete uložit pomocí `Přidat výhled`.
Když klepnete na název pohledu, kamera se do něj vrátí.


::: tip
Uložený pohled si pamatuje nastavení [Projekce](#projection) a také [referenční obrázek](background.md).  
To se hodí, když chcete přepínat mezi referenčními pohledy zepředu, zleva a zezadu s různými pozadími.
:::

| Akce              | Ikona                         | Popis                                                                       |
| :---------------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Viditelnost       | ![](/icons/eye_open.webp)    | Zapne nebo vypne kameru. Skryté kamery tlačítka předchozí/další přeskočí    |
| Název             |                               | Vybere kameru                                                               |
| Obrázek           | ![](/icons/image.webp)       | Náhled referenčního obrázku, pokud je s kamerou propojený                   |
| Projekce          | ![](/icons/perspective.webp) | Projekce kamery, v perspektivě i se zorným polem                            |
| Aktualizovat pohled | ![](/icons/update_view.webp) | Aktualizuje uložený pohled podle aktuálního úhlu pohledu                  |
| Upravit název     | ![](/icons/pencil.webp)      | Upraví název kamery                                                         |
| Smazat            | ![](/icons/trash.webp)       | Smaže kameru                                                                |

### ![](/icons/camera_add.webp) Přidat výhled {#add}
Vytvoří novou kameru podle aktuálního pohledu.

### ![](/icons/camera.webp) Ikony {#icons-test}

Určuje, jestli jsou ikony kamer vidět ve výřezu. Tlačítko se objeví vedle `Přidat výhled`, jakmile máte nějakou kameru. Ikona vybrané kamery je vidět vždy.

### Projekce {#projection}
Vyberte mezi `Perspektiva` a `Ortografický`.

V perspektivě můžete měnit `Svislé zorné pole` kamery. Nad posuvníkem se ukazuje odpovídající ohnisková vzdálenost 35mm fotoaparátu, což se hodí, pokud jste zvyklí z fotografie.
Pro modelování se obvykle doporučuje nízké zorné pole, protože pomáhá s proporcemi.  
Režim `Ortografický` odpovídá zhruba zornému poli rovnému 0.

### První osoba {#fps}
Jen v perspektivě. Umístí pivot přímo do kamery místo na model. Tažení prstem po pozadí pak nechá polohu kamery zamčenou a mění jen její natočení, podobně jako ve hrách z pohledu první osoby. Hodí se, když modelujete prostředí, a ne jednotlivé objekty.

![](/images/camera_rotation_ortho_view.webp)

### Typ rotace {#rotation-type}
Ve výchozím stavu kamera používá režim rotace `Otočný stůl`.
To znamená, že máte jen dva stupně volnosti; je to intuitivnější, ale někdy budete chtít víc volnosti.  
Můžete přepnout na `Trackball` a pak budete moct pohled *naklánět* otáčením *dvou* prstů ve výřezu. Režimy `Trackball` jsou dva: první otáčí pohledem jako koulí pod prstem, druhý (s ikonou šipek) otáčí pohledem podle vodorovného a svislého pohybu tažení, což může být pro některé uživatele známější.

### Ortografické uchycení {#orthographic}

Když je zapnuté a máte klávesnici, držení klávesy Shift při otáčení pohledu přichytí kameru k nejbližšímu pohledu zepředu/zezadu/shora/zdola/zleva/zprava a přepne kameru na ortografickou. Kamera se přepne na ortografickou také po klepnutí na kostku pohledů, která ji přichytí k pohledu zepředu/zezadu/zleva/zprava/shora/zdola.

### Obnovit pohled {#reset}

Přesune kameru dopředu a vměstná scénu do pohledu.

### Zarovnat pohled {#snap}
Přichytí kameru k nejbližšímu pohledu zepředu/zezadu/zleva/zprava/shora/zdola. Pokud už jste v jednom z těchto pohledů, dalším klepnutím se otočíte o 180 stupňů na opačnou stranu.

### Rychlost {#speed}

Pokud vám kamera přijde moc pomalá nebo moc rychlá, můžete nastavit násobitel rychlosti pro `Rotace`, `Zvětšování` a `Přesun`. Hodí se, když je váš model hodně velký nebo hodně malý.

### Přehled pivotu {#pivot}

Když otáčíte kamerou, vidíte malou růžovou tečku: to je pivot kamery, tedy bod, kolem kterého se otáčí.  
Je velmi důležité vědět, kde pivot máte, abyste se neztratili a kamera vás nefrustrovala.

Ve výchozím stavu se pivot aktualizuje těmito úkony:
- dvojité klepnutí na model
- dvojité klepnutí na pozadí (nový pivot bude ve středu vaší sítě)
- položení *dvou* prstů na obrazovku (posun/přiblížení/naklánění) aktualizuje pivot do středu mezi *dvěma* prsty

### Aktualizovat střed otočení... {#update-pivot}

Aktualizaci pivotu můžete dál přizpůsobit těmito možnostmi:

* `Když se kamera začne pohybovat` - Aktualizuje pivot, když začnete s kamerou pracovat.
* `Povolit pivot mimo objekt` - Povolí nový pivot, i když přibližujete mimo povrch objektu. Vyžaduje `Když se kamera začne pohybovat`.
* `Při dvojitém klepnutí` - Aktualizuje pivot rotace, když dvakrát klepnete na povrch objektu.
* `Sochařit (Tah)` - Aktualizuje pivot, když modelujete.

::: tip
Až si zvyknete, můžete růžovou tečku (nápovědu) skrýt v nabídce [Nastavení](settings.md).
:::

### Centrování pohledu při oddalování {#center-view-when-zooming-out}
Při oddalování se kamera neposouvá do stran: jen couvá, takže pohled zůstává vystředěný.

### Dvakrát klepněte na objekt {#dtap-object}
Když je zapnuté, dvojité klepnutí na objekt zaostří kameru na bod, na který jste klepli.

### Dvakrát klepněte na pozadí {#dtap-tap-background}
Když je zapnuté, dvojité klepnutí na pozadí zaostří kameru na:
* `Výběr` - Vybrané objekty.
* `Scéna` - Celou scénu.
* `Přepnout` - Při každém dvojitém klepnutí přepne mezi oběma. Možnosti `Přepnout` jsou dvě a liší se tím, která z nich je první, jak ukazují jejich ikony.
