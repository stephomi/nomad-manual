# ![](/icons/history.webp) Historie {#history}
![](/images/history_overview.webp)

Jako ve většině tvůrčích aplikací můžete v Nomadu vrátit zpět a znovu provést jakoukoli úpravu.
Historie může hodně narůst, proto si sami určíte, kolik z ní zůstane v paměti, kolik se uchová v úložišti a zda se uloží spolu s projektem.

::: tip
Pro zpět/znovu můžete použít rychlá gesta:
- klepnutí 2 prsty vrátí krok zpět
- klepnutí 3 prsty krok znovu provede
:::

## ![](/icons/history.webp) Historie {#history-panel}
![](/images/history_history.webp)

Tento panel zobrazuje zásobník historie: počet kroků, název operace, objekt, na který byla použita, a kolik paměti daný krok zabírá.

Klepnutím na položku skočíte zpět (nebo dopředu) do daného stavu. Dlouhým stiskem položky ji trvale smažete spolu s celou starší historií, což je rychlý způsob, jak uvolnit paměť, když už jste se sochou spokojeni.

### ![](/icons/speed.webp) Přehrát {#replay}
Tlačítko přehrávání vlevo dole přetočí historii na začátek a pak operace jednu po druhé znovu provede. Je to zábavný způsob, jak sledovat, jak vaše socha vzniká. Posuvník nastavuje rychlost v operacích za sekundu. Dalším klepnutím na tlačítko přehrávání zastavíte, zastaví ho i zpět/znovu nebo klepnutí na položku.

Před spuštěním si v okně můžete vybrat:
* `Opačný` - Vrací kroky od aktuálního stavu zpět až na začátek, místo přehrávání od začátku.
* `Obnovit kameru` - Kamera sleduje přehrávané operace, i když je volba [Obnovit kameru](#restore-camera) vypnutá.
* `Vyhlazení kamery` - Kamera mezi pohledy plynule klouže, místo aby na každý skočila. Vyšší hodnoty dávají klidnější kameru.

::: warning
Přehrávání je experimentální.
:::

## Zahrnout akce {#include-actions}

Ikony ve spodní části panelu Historie určují, jaké druhy úprav se do historie zaznamenávají:

| Akce        | Ikona                         | Popis                                                                               |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Světla      | ![](/icons/light.webp)        | Úpravy světel. Posun světla gizmem se zaznamená vždy, protože může ovlivnit další objekty v hierarchii scény |
| Stínování   | ![](/icons/sun.webp)          | Režimy PBR, MatCap a Unlit, matcapy a HDRI                                          |
| PostProcess | ![](/icons/postprocess.webp)  | Úpravy postprocesu                                                                  |
| Výběr       | ![](/icons/tool_lattice.webp) | Úpravy výběru mřížky, například klepnutí, výběry lasem a zrušení výběru             |

## Nastavení {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Obnovit kameru {#restore-camera}
U každé operace se uloží pohled kamery.
Když tuto volbu zapnete, vrácení nebo opakování operace vrátí kameru do uloženého pohledu.

### ![](/icons/history.webp) Uložit historii {#save-history}
Při uložení projektu zachová historii úprav, takže vám zůstane i po jeho opětovném otevření. Vypněte ji, pokud chcete mít menší soubory projektu.

### ![](/icons/ram.webp) Limit RAM {#history-limit-mb}
Maximální objem historie uchovávané v RAM. Starší stavy se přesunou do úložiště a v případě potřeby se znovu načtou, nemažou se.

### ![](/icons/save.webp) Limit úložiště {#storage-limit}
Maximální místo v úložišti, které smí historie tohoto projektu zabrat. Po dosažení limitu se nejstarší operace trvale smažou.

::: tip
Nový limit začne platit po další úpravě, kroku zpět nebo znovu.
:::

### ![](/icons/undo.webp) Upozornění při vracení změn {#maximum-undoable}
Pokud skočíte zpět o víc operací naráz, než je tato hodnota, Nomad si nejdřív vyžádá potvrzení. Když potom provedete novou úpravu, všechny operace po tomto bodě se ztratí, takže vás to chrání před nechtěným klepnutím hluboko v seznamu.

## Statistiky paměti {#memory-stats}

Tato část ukazuje, kolik paměti Nomad využívá a na co.
