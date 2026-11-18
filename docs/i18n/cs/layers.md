# ![](/icons/layer.webp) Vrstvy {#layers}

Tato nabídka obsahuje zásobník vrstev, tedy způsob, jak ukládat úpravy objektu nedestruktivně, a mnoho možností, jak vrstvy kombinovat a znovu využít.

![](/images/layers_overview.webp) 

## Přehled {#overview}

Vrstvy mají v Nomadu několik účelů.

Malba (barva, drsnost, kovovost, krytí) funguje s vrstvami podobně jako ve 2d malířských aplikacích. Můžete vytvořit vrstvu a malovat do ní na model. Vrstvu lze zapnout nebo vypnout, upravit její krytí, duplikovat ji, změnit její pořadí v zásobníku vrstev nebo nastavit její režim prolnutí.

Nomad vrstvy používá i pro modelování. Vrstva může uchovávat jemné detaily, jako jsou vrásky, nebo velké změny, a fungovat tak jako blendshapes/shape keys/morph targets v jiných 3d aplikacích. Můžete například vymodelovat různé výrazy obličeje do různých vrstev a posuvníky vrstev je pak kombinovat do nových výrazů.

V tomto případě se změny uložené ve vrstvě čistě sčítají, takže na pořadí vrstev nezáleží, jako je tomu u malby.

Vrstvy lze částečně mazat nástrojem [SmazatVrstva](tools.md#delete-layer) a lze z nich také vytvářet masky podle různých informací, které vrstva uchovává.

![](/videos/layer.mp4)

::: tip
Na rozdíl od většiny modelovacích programů změna topologie sítě vrstvy nezahodí. Můžete použít [voxelové přesíťování](topology.md#voxel-remesher), [multirezoluci](topology.md#multiresolution) nebo nástroje [Oříznout](tools.md#trim)/[Rozdělit](tools.md#split); při použití [voxelového přesíťování](topology.md#voxel-remesher) ale utrpí kvalita vrstvy.
:::

::: tip
Pokud vrstvy používáte jako blendshapes/morph targets, najdete další funkce pro vrstvy v [nabídce scény](scene.md#object-menu): můžete vrstvy oddělit do objektů a odpovídající objekty zase spojit do vrstev.
:::
----

## Nabídka vrstev {#layer-menu}

![](/images/layers_menu.webp)

V nadpisu je název vybraného objektu. Vrstvy nejsou dostupné u primitiv, takže primitivum nejdřív potvrďte.

Novou vrstvu vytvoříte tlačítkem `Přidat vrstvu`. `Sloučit vrstvy` sloučí všechny vrstvy do základní sítě; číslo vedle ikony udává, kolik vrstev máte.

Každá vrstva má název, posuvník pro nastavení její síly (faktoru) a tlačítka s možnostmi. Klepnutím na vrstvu z ní uděláte aktivní vrstvu: modelování i malování se ukládá do ní. Klepnutím na `Základ` budete znovu pracovat na základní síti.

### ![](/icons/sort_right.webp) Rozbalit seznam {#ui-expand-list}

Ve výchozím stavu seznam vrstev u každé vrstvy ukazuje jen viditelnost, režim prolnutí a sílu, a aktivní vrstva je rozbalená se všemi ovládacími prvky. Šipka vlevo od nadpisu rozbalí všechny ovládací prvky u každé vrstvy.

![](/images/layers_expand.webp)

### Možnosti {#options}

| Akce           | Ikona                        | Popis                                               |
| :------------: | :--------------------------: | :-------------------------------------------------  |
| Viditelný      | ![](/icons/eye_open.webp)   | Zobrazí nebo skryje vrstvu                          |
| Režim prolnutí | ![](/icons/opacity.webp)    | Režim prolnutí ve stylu Photoshopu. 4 ikony ukazují režimy pro barvu, drsnost, kovovost a krytí.                                 |
| Přejmenovat    | ![](/icons/pencil.webp)     | Upraví název vrstvy                                 |
| Smazat         | ![](/icons/trash.webp)      | Smaže vrstvu                                        |
| Klonovat       | ![](/icons/clone.webp)      | Duplikuje vrstvu                                    |
| Sloučit dolů   | ![](/icons/merge_down.webp) | Sloučí vrstvu s vrstvou pod ní (nebo se základní sítí) |
| Více           | ![](/icons/more.webp)       | Možnosti [Více...](#more)                           |

Když vrstva není rozbalená, najdete `Přejmenovat`, `Smazat`, `Klonovat` a `Sloučit dolů` v její nabídce [Více...](#more).

Chcete-li vrstvu přesunout jinam v zásobníku vrstev, podržte prst na jejím názvu a táhněte.

### Základ {#base}

Tlačítko se třemi tečkami v řádku `Základ` přesune malbu základní sítě do nové vrstvy pomocí tlačítka `Základ → Vrstva`. Základ se pak vrátí na podkladový materiál. To se hodí, když jste toho hodně namalovali ještě předtím, než jste vytvořili jakoukoli vrstvu.

* Tlačítka masky a skrytí vedle něj nechají maskované a skryté oblasti nedotčené.
* `Extrakt` - kanály, které se přesunou: `Barva`, `Krytí`, `Drsnost` a `Kovovost`.
* `Podkladový materiál` - když je zapnutý, přesunou se jen hodnoty, které se od tohoto materiálu liší. Nastavíte ho posuvníky, nebo ho kapátkem naberete z modelu.

### ![](/icons/more.webp) Více... {#more}

Tlačítko „Více...“ zobrazí další možnosti aktuální vrstvy, ve dvou kartách: nastavení (ikona ozubeného kola) a extrakce (ikona krychle).

![](/images/layers_more.webp) 

#### Faktory kanálu {#channel-factors}

Tyto ovládací prvky umožňují škálovat množství modelování/barvy/drsnosti/kovovosti/krytí vrstvy. Hodnoty se násobí posuvníkem faktoru vrstvy, takže když je například síla vrstvy 1, ale faktor barevného kanálu 0,5, zobrazí se barva se sílou 0,5.

`Offset` ovládá sílu modelování ve vrstvě. Zatímco barva/drsnost/kovovost jsou omezené na rozsah 0 až 1, offset může mít jakoukoli hodnotu, kladnou i zápornou. 

::: tip
Pomocí offsetu můžete z vrstvy hrbolů udělat vrstvu prohlubní, nebo z úsměvu zamračení:
![](/videos/layer_happysad.mp4)


Symetrickou vrstvu můžete naklonovat a pak ji nástrojem SmazatVrstva rozdělit na levý a pravý tvar:
![](/videos/layer_leftright.mp4)

Vrstvy se záporným faktorem offsetu lze vypéct do prázdných vrstev a získat tak nové kladné tvary.

Vrstvy s kladným faktorem offsetu nad 1 se hodí k experimentování s extrémnějšími blendshapes.
:::

::: warning
Vrstvy zatím sdílejí jediný kanál krytí pro všechny 3 kanály (barva/kovovost/drsnost).
Pokud sloučíte víc vrstev s intenzitou jednotlivých kanálů, které nejsou na plné intenzitě, může výsledek vypadat jinak.

Možná bude mít v budoucnu každý kanál vlastní alfa kanál, který toto omezení odstraní.
:::


#### ![](/icons/shield.webp) Maska {#mask}
Tlačítko masky vedle každého posuvníku vytvoří masku z daného kanálu. Podobně jako když v malířských aplikacích používáte vrstvy k vytváření výběrů, můžete tak práci odvedenou ve vrstvě znovu využít pro další operace.

#### ![](/icons/preview.webp) Náhled {#preview}
![](/images/layers_preview.webp) 

Následující možnosti jsou na kartě extrakce v nabídce „Více...“.

Když je zapnutý, ukáže náhled nastavení extrakce pro tuto vrstvu (viz další část).

`Rentgen` určuje, které objekty budou během náhledu průhledné (`Žádné`, `Nevybrané`, `Vybrané` nebo `Vše`), aby extrahovaný tvar zůstal plný. Hodí se, když používáte záporné výšky extrakce.

#### ![](/icons/mask_extract.webp) Extrakt {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Tlačítko `Extrakt` zduplikuje obsah vrstvy do nového objektu, obvykle s tloušťkou, kterou nastavíte v další části.

`Uzavírací akce` určuje, jak se duplikace provede:

* `Žádné` - Jen extrahuje část, nesnaží se vytvořit boky ani vyplnit díry.
* `Vyplnit` - Díra se vyplní trojúhelníky a vyhladí. Tuto možnost nepoužívejte pro rovné plochy.
* `Kryt` - Uzavře extrahovaný tvar podle hodnoty tloušťky a nastavení směru.
* `Vrstva` - Extrahuje rozdíl vrstvy.

#### ![](/icons/height.webp) Výška {#thickness}
![](/images/layers_thickness.webp) 

Hloubka vytažení krytu. Kladné hodnoty rostou ven z povrchu, záporné do povrchu. Když je uzavírací akce `Vrstva`, je skrytá.

Plus/minus vedle této hodnoty nastavuje směr vytažení:
* Minus ( - ) začne od aktuálního povrchu a vytahuje dolů. 
* Plus ( + ) začne od aktuálního povrchu a vytahuje nahoru.
* Plus-minus ( ± ) odsune horní a spodní stranu vytažení o stejný kus, takže bude z poloviny zanořené do původního povrchu.

#### Boky {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Tato část je vidět, když je uzavírací akce `Kryt`. 

`Dělení stěny` nastavuje počet dělení podél boků krytu. Se zapnutým přepínačem `Auto` Nomad dopočítá počet smyček hran tak, aby vznikly čtvercové polygony.

#### Hladkost {#smoothness}
![](/images/layers_smoothness.webp) 

Pokud jsou okraje extrahované oblasti zubaté, zapněte tuto možnost a vyhladí se do hezčího tvaru. `Vše` vyhladí celý extrahovaný povrch, `Pouze hranice` jen jeho okraje. `Iterace` nastavuje, jak silné vyhlazení bude.

_Tady končí podnabídka „Více...“._

### ![](/icons/cog.webp) Rozšířené {#advanced}
![](/images/layers_advanced.webp)

Tlačítko `Rozšířené` dole v nabídce se objeví, jakmile má objekt vrstvy.

#### Zachovat detaily horních vrstev {#keep-top-layers-details}

Zajistí, že malé detaily ve vyšších vrstvách zůstanou vidět, i když v nižších vrstvách provedete velké změny. Během modelování se deformace z horních vrstev ignoruje, ale jejich detaily zůstanou vidět. Dobře to funguje jen tehdy, když horní vrstvy obsahují poměrně malé detaily.

Ve výchozím stavu se stane, že když do vrstvy vymodelujete drobné vrásky a pak provedete velké změny v základní vrstvě, vrásky se ztratí. Zapnutím tohoto přepínače budou malé detaily vždy „plout“ nad velkými změnami pod nimi. V následujícím videu se podívejte, jak se detail vrásek ve výchozím stavu ztratí, ale se zapnutým „Zachovat detaily horních vrstev“ zůstane vidět:

![](/videos/layers_details.mp4)


#### Synchronizace transformace {#sync-transform}

Když je zapnutá, všechny nevybrané vrstvy se přizpůsobí rotaci, měřítku a zkosení transformace, když použijete nástroje Gizmo nebo Přeměnit. Může být `Auto`, `Ne` nebo `Ano`.

Vypněte tuto možnost, pokud se ostatní vrstvy mají používat bez nové transformace, kterou právě aplikujete.

Při nastavení `Auto` se přizpůsobí jen viditelné vrstvy.
