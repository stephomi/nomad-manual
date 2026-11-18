# ![](/icons/postprocess.webp) Postproces {#post-process}

Tato nabídka ovládá řadu nastavení Nomadu, která ovlivňují vzhled renderu.

![](/images/postprocess_overview_drac.webp)

Postproces dokáže výrazně změnit konečný vzhled vaší scény.

![](/images/postprocess_overview.webp)
*Stejná scéna před postprocesem a po něm, bez dalších světel nebo změn materiálu.*

Postproces může podle zařízení hodně ovlivnit výkon.
Globální zaškrtávací políčko `Postproces` vypne veškerý postproces, takže se můžete rychle vrátit k modelování, aniž byste přišli o své předvolby.
Pro PBR vykreslování byste měli mít zapnuté [Ambientní okluze](#ambient-occlusion-ssao), [Odraz](#reflection-ssr) a [Mapování tónů](#tone-mapping).

Většinou ale budete chtít mít postproces při modelování vypnutý, abyste se soustředili na samotný tvar, a ne na vykreslení.


## Kvalita {#quality}

![](/images/postprocess_quality.webp)

Tyto možnosti zlepšují kvalitu renderu na úkor výkonu.

### Maximální vzorkování rámců {#max-frame-sampling}
Nomad pro vykreslení jediného snímku spočítá jen určité množství postprocesu, což může vypadat zrnitě. Toto nastavení určuje, kolik snímků se vykreslí a pak smíchá dohromady, aby zmizela většina šumu. Některé efekty žádné další vzorky nepotřebují (např. barevné korekce), jiné, jako měkké stíny a globální osvětlení, mohou k odstranění šumu potřebovat stovky vzorků. 

Ve výřezu to uvidíte vždy, když Nomad necháte chvíli být: kvalita obrazu se postupně zlepšuje až do maximálního počtu vzorků a pak se zastaví. Jakmile se zastaví, Nomad nic nedělá, což šetří baterii. Stejný počet výpočtů se použije také v části pro rendery v [nabídce Soubory](files) po klepnutí na export PNG.

Zaškrtávací políčko vedle posuvníku vzorkování snímků zapíná a vypíná.

### Rozlišení vykreslování {#resolution-multiplier}
Tento posuvník řídí rozlišení renderu. Hodnota x1.0 znamená, že se vykresluje v pixelovém rozlišení zařízení. Hodnota x0.5 vykresluje v polovičním rozlišení, což je rychlé, ale v nízké kvalitě. Hodnota větší než 1 vykreslí obraz ve větší velikosti a pak ho zmenší. Výsledkem je vyšší kvalita a méně šumu, ale delší čas vykreslování.

Na výkon to má zásadní vliv, takže se snažte držet hodnotu na x1.25 nebo nižší. Tato hodnota se neukládá do nastavení a efekt [Pixel Art](#pixel-art) ji přepisuje.

### ![](/icons/intensity.webp) Max vzorků {#max-samples}

Zlepšuje kvalitu efektů postprocesu na úkor výkonu.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Rozptýlí pixely, aby se omezily artefakty v podobě pruhů (například v přechodech nebo vinětaci). Obvykle by měl být zapnutý, ale pro některé operace ho můžete vypnout (např. při exportu hloubkových map nebo jiných datově specifických operacích).

### ![](/icons/denoise.webp) Odzvučovač (oidn) {#oidn}

Po nasčítání všech snímků obraz odšumí. Díky tomu můžete použít mnohem méně vzorků. Odšumování je náročné na procesor, takže ho zapínejte jen tehdy, když je obraz zašuměný. Není dostupné na všech zařízeních.

## Prohlížeč předvoleb {#preset-browser}
![](/images/postprocess_presets.webp)
Klepnutím na obrázek pod nadpisem `Postproces` zobrazíte sbírku předvoleb postprocesu. Tlačítkem `Nový` vytvoříte předvolbu z aktuálního nastavení. Vestavěné předvolby lze jen klonovat: chcete-li si vytvořit vlastní, jednu vyberte, klepněte na `Klonovat` a proveďte změny. Když má předvolba neuložené změny, ukáže `Neuložené změny!`; pro uložení klepněte na obrázek předvolby, klepněte znovu uvnitř prohlížeče předvoleb a zvolte `Uložit`.

## Panel zkratek {#shortcut-bar}
Když je postproces zapnutý, panel dole v nabídce ukazuje všechny efekty (`SSR`, `SSGI`, `SSAO`, `DoF`, `Bloom`...). Klepnutím na jeden z nich přeskočíte do jeho části. Vypnuté efekty jsou zašedlé, takže panel zároveň rychle shrnuje, co aktuální předvolba dělá.

## ![](/icons/postprocess_ssr.webp) Odraz (SSR) {#reflection-ssr}
S touto možností mohou objekty odrážet jiné objekty ve scéně, pokud jsou tyto objekty vidět na obrazovce.
Pokud máte ve scéně kovové a lesklé objekty, měli byste tuto možnost nejspíš používat.
Vyžaduje režim stínování [Osvětlené (PBR)](shading.md#pbr).


| SSR vypnuto                | SSR zapnuto               |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Globální osvětlení (SSGI) {#global-illumination-ssgi}

Globální osvětlení simuluje, jak se světlo odráží mezi povrchy; například červená stěna vrhne červený nádech na blízký bílý objekt. Ve spojení s ambientní okluzí a odrazy může realističnost renderu ohromně zvýšit. Stejně jako odrazy vyžaduje režim stínování [Osvětlené (PBR)](shading.md#pbr).

`Síla` - Intenzita globálního osvětlení. 



| SSGI vypnuto               | SSGI zapnuto              |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Za koulí je bodové světlo namířené na strop. S vypnutým SSGI je osvětlený jen strop. Se zapnutým SSGI se světlo odráží ze stropu na stěny a z nich na kouli._

## ![](/icons/postprocess_ssao.webp) Ambientní okluze (SSAO) {#ambient-occlusion-ssao}
Ambientní okluze ztmaví místa, kam světlo pronikne s menší pravděpodobností (rohy apod.).
Efekt závisí jen na geometrii modelu.

* `Síla`- Intenzita efektu.
* `Velikost`- Jak daleko se efekt rozprostírá.
* `Tloušťka` - Jakou tloušťku do hloubky předpokládat u zakrývajících objektů, v procentech z hodnoty `Velikost`.
* `Odstín` - Barva, kterou se okluze násobí, pro kreativní efekty.


| SSAO vypnuto                | SSAO zapnuto               |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO je nejvíc vidět v místech osvětlených hlavně světlem prostředí. Místa pod silným přímým světlem dostanou mnohem slabší efekt AO.

:::

## ![](/icons/postprocess_dof.webp) Hloubka ostrosti {#depth-of-field-dof}
Přidá rozmazání oblastem mimo zaostření.

Ohniskový bod změníte jednoduše klepnutím na model.

* `Režim clony` - Rozmazání řídí jediná clona kamery místo dvou posuvníků rozmazání níže.
* `Clona` (_jen v režimu clony_) - Clonové číslo objektivu, jako u skutečného fotoaparátu. Nižší hodnota objektiv otevře a rozmaže víc.
* `Vzdálené rozmazání` - Míra rozmazání za ohniskovým bodem.
* `Blízké rozmazání` - Míra rozmazání mezi ohniskovým bodem a kamerou.


| DOF vypnuto               | DOF zaostřeno na vzdálený kruh | DOF zaostřeno na blízký kruh |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Bloom {#bloom}
Bloom rozzáří jasná místa vaší scény.

* `Intenzita` - síla efektu.
* `Poloměr` - Jak daleko se efekt rozprostírá.
* `Prahová hodnota` - Jak jasné musí pixely ve scéně být, aby začaly zářit. Při 0 září všechno, vysoká hodnota nechá zářit jen nejjasnější pixely.
* `Odstín` - barva, kterou můžete bloomu přidat pro kreativní efekty.

| Bloom vypnuto                | Bloom s poloměrem 0         | Bloom s poloměrem 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Mapování tónů {#tone-mapping}
Mapování tónů je operace, která přemapuje hodnoty HDR do rozsahu `[0, 1]`.
Pokud ho nepoužijete (nebo zvolíte `Žádný`), každá barevná složka vyšší než 1 se ořízne.
Všechny barevné odstíny nad tímto rozsahem se pak ztratí.

* `Žádný/Neutrální/Agx/ACES` - který tone mapper použít. `Žádný` nic nepřemapovává (ostatní ovládací prvky ale fungují dál). Ostatní možnosti se podobají výběru různých filmových materiálů: každá jinak zachází s přeexponovanými hodnotami a barvami. Je to velmi hluboké téma, pro víc informací si vyhledejte tone mapping, Agx a ACES!
* `Expozice` - celkový jas obrazu, podobně jako nastavení clony na fotoaparátu. Je to rychlý způsob, jak celý obraz zesvětlit nebo ztmavit.
* `Saturace` - síla barev. 1 je neutrální, 0 černobílé, hodnoty nad 1 jsou stále sytější.
* `Kontrast` - Tmavá místa ztmaví a světlá zesvětlí. Používejte opatrně, při vysokých hodnotách může vytvářet artefakty.

Všimněte si, že s vypnutým `Mapování tónů` některé detaily mizí, protože pixely jsou příliš jasné.

| Mapování tónů vypnuto       | Mapování tónů zapnuto      |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Mapování tónů může zesílit efekt globálního osvětlení. Když snížíte intenzitu mapy prostředí a zvýšíte hlavní zdroj světla, můžete zvýšit `Expozice` mapování tónů a lépe uvidíte efekty odraženého světla.
:::

## ![](/icons/postprocess_tone_curve.webp) Obarvování {#color-grading}
Podobně jako nástroj křivky ve Photoshopu umožňuje řídit vyvážení a rozložení barev v obraze. Ovládání `Hlavní` ovlivňuje celé vyvážení barev, ovládání `Červená`/`Zelená`/`Modrá` umožňují jemné doladění. 

| Obarvování vypnuto            | Obarvování zapnuto           |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Zakřivení {#curvature}
Najde místa, kde se zakřivení prudce mění, a obarví je.

* `Faktor` - celková intenzita efektu
* `Hrbol` - jak moc hledá ostré vypouklé změny a obarví je vybranou barvou (ve výchozím stavu bílou)
* `Dutina` - jak moc hledá vydutá místa a obarví je vybranou barvou (ve výchozím stavu černou)
* `Tloušťka` - jak široké jsou nalezené hrany.

Vedle `Hrbol` a `Dutina` je barevný vzorek pro výběr barvy a malé tlačítko, kterým zvolíte, jak se barva s obrazem prolne.


| Zakřivení vypnuto                | Zakřivení zapnuto              |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Chromatická aberace {#chromatic-aberration}
Simuluje vadu objektivu, kdy se světlo u okrajů obrazovky rozkládá.

* `Síla` - jak moc se červená/zelená/modrá složka obrazu směrem k okrajům obrazovky rozchází

| Chromatika vypnuta            | Chromatika zapnuta           |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vinětace {#vignette}
Simuluje vadu objektivu, kdy jsou okraje obrazovky tmavší.

* `Velikost` - Velikost převrácené elipsy položené přes obraz
* `Tvrdost` - Jak rozmazaně nebo ostře se elipsa prolne s obrazem.
* `Odstín` - Barva vinětace, ve výchozím stavu černá.


| Vinětace vypnuta                | Vinětace zapnuta               |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Zrno {#grain}
Přidá efekt zrna, díky kterému může obraz působit o něco méně uměle.

* `Síla` - množství zrna/šumu přidaného do obrazu.


| Zrno vypnuto                 | Zrno zapnuto               |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Ostrost {#sharpness}
Efekt doostření podobný tomu ve Photoshopu nebo v aplikacích na úpravu fotek.

* `Síla` - míra doostření obrazu.


| Ostrost vypnuta                | Ostrost zapnuta              |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Simuluje pixel art ze starých her. Tento efekt přepisuje [Rozlišení vykreslování](#resolution-multiplier).

* `Posuvník` - velikost pixelů
* `Povolit vzorkování rámce` - pokud se objevuje hodně černých pixelů, zkuste tuto možnost zapnout. Bez ní efekt pixel art vypne [vzorkování snímků](#max-frame-sampling).

| Pixely vypnuty              | Pixely zapnuty             |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Rozprostření skenování {#scanline}
Simuluje vzhled starých CRT monitorů.

* `Faktor` - síla řádků
* `Rozestupy` - velikost řádků

| Řádky vypnuty                  | Řádky zapnuty                 |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
