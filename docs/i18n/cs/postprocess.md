# ![](/icons/postprocess.webp) Postprocess 

Tato nabídka ovládá mnoho aspektů Nomadu, které ovlivňují vzhled renderu.

![](/images/postprocess_overview_drac.webp)

Použití postprocessingu může výrazně změnit finální vzhled vaší scény.

![](/images/postprocess_overview.webp)
*Stejná scéna před a po postprocessingu, bez dalších světel nebo změn materiálů.*

Postprocess může výrazně ovlivnit výkon v závislosti na vašem zařízení.
Je zde globální zaškrtávací políčko pro vypnutí veškerého postprocessingu, takže se můžete rychle vrátit ke skulptování/modelování, aniž byste přišli o své presety.
Pro PBR renderování by měly být zapnuté [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) a [Tone Mapping](#tone-mapping).

Většinu času ale budete chtít mít postprocessing při skulptování vypnutý, abyste se mohli soustředit na samotný tvar renderu.


## Quality

![](/images/postprocess_quality.webp)
### Max frame sampling
Nomad pro jeden snímek vypočítá určité množství postprocessingu, který může vypadat zrnitě. Toto nastavení určuje, kolik snímků se vyrenderuje a následně smíchá dohromady, aby se odstranila většina šumových artefaktů. Některé efekty nevyžadují žádné extra vzorky (např. color grading), zatímco jiné, jako globální iluminace, mohou vyžadovat stovky vzorků, aby byly bez šumu. 

Ve viewportu je to vidět vždy, když necháte Nomad chvíli být – kvalita obrazu se postupně zpřesňuje až do maxima vzorků a pak se zastaví. Tento počet výpočtů se používá také v sekci renderu v [Files menu](files), když kliknete na „export png“.

### Resolution multiplier
Tento posuvník ovládá rozlišení postprocessingu. Hodnota x1.0 znamená, že se rendery provádějí v rozlišení pixelů zařízení. Hodnota x0.5 bude renderovat v polovičním rozlišení, což je rychlé, ale nízké kvality. Hodnota vyšší než 1 bude renderovat ve větší velikosti a pak obraz zmenší. Výsledkem je vyšší kvalita, méně šumu, ale delší časy renderu.

### Max samples

Toto zvýší kvalitu postprocessingu, ale obecně bude mít větší dopad `Full resolution`. 

### Full resolution
Po zapnutí vynutí multiplikátor rozlišení na x1.0

### Denoiser (oidn)

Aplikuje na obraz denoiser. To vám umožní používat mnohem nižší počet vzorků. Funguje pouze tehdy, pokud je zapnuté `Full Resolution`. Všimněte si, že odšumování probíhá až po výpočtu všech vzorků a může být náročné na procesor.

## Preset browser
![](/images/postprocess_presets.webp)
Kliknutím na obrázek se zobrazí kolekce presetů postprocessingu. Pro definování vlastních presetů nějaký vyberte, klikněte na „clone“, proveďte změny. Pro uložení klikněte na obrázek presetu, znovu klikněte uvnitř preset browseru a zvolte „save“.


## Reflection (SSR)
S touto volbou mohou objekty odrážet jiné objekty ve scéně, pokud jsou tyto objekty viditelné na obrazovce.
Pokud máte ve scéně kovové a lesklé objekty, tuto volbu byste pravděpodobně měli použít.
Tato volba je účinná pouze v PBR režimu.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Global Illumination (SSGI)

Globální iluminace simuluje, jak se světlo odráží mezi povrchy, např. červená zeď vrhá červený nádech na blízký bílý objekt. Při použití s ambient occlusion a odrazy může výrazně zvýšit realističnost renderu. 

`Strength` - Intenzita globální iluminace. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Reflektor je za koulí a míří na strop. Se SSGI vypnutým je osvětlený pouze strop. Se SSGI zapnutým se světlo odráží ze stropu na stěny a na kouli._

## Ambient Occlusion (SSAO)
Ambient occlusion ztmavuje oblasti, kam má světlo menší šanci proniknout (rohy atd.).
Efekt závisí pouze na geometrii modelu.

* `Strength`- Intenzita efektu.
* `Size`- Jak rozšířený efekt je.
* `Curvature bias` - Jak citlivý je efekt vzhledem k variacím povrchu.
* `Color` - Tón násobený do occlusion, používaný pro kreativní efekty.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO bude nejviditelnější v oblastech osvětlených hlavně environment světlem. Oblasti pod silným přímým světlem dostanou mnohem slabší AO efekt.

:::

## Depth of Field (DOF)
Přidá efekt rozostření v oblasti mimo rovinu zaostření.

Jednoduše klepněte na svůj model pro změnu zaostřovacího bodu.

* `Far blur` - Množství rozostření aplikované na vzdálenější stranu od zaostřovacího bodu.
* `Near blur` - Množství rozostření aplikované mezi zaostřovacím bodem a kamerou.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Bloom
Bloom způsobí, že světlé oblasti vaší scény budou zářit.

* `Intensity` - síla efektu.
* `Radius` - Rozsah efektu.
* `Threshold` - Jak jasné musí být pixely ve scéně, než začnou zářit. Nízká hodnota způsobí, že bude zářit vše, vysoká hodnota dovolí zářit pouze nejjasnějším pixelům.
* `Color` - tón, který lze do bloom efektu přidat pro kreativní účely.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Tone Mapping
Tone Mapping je operace, která převádí HDR hodnoty do rozsahu `[0, 1]`.
Pokud jej nepoužijete (nebo zvolíte `none`), jakákoli barevná složka vyšší než 1 bude oříznuta.
Jakékoli barevné variace nad tímto rozsahem se tak ztratí.

* `None/Neutral/Agx/ACES` - jaký tonemapper použít. `None` nedělá žádné mapování (ale ostatní ovládací prvky stále fungují). Ostatní možnosti jsou podobné volbě různých filmových materiálů – různým způsobem pracují s přeexponovanými hodnotami a barvami. Je to velmi hluboké téma, pro více informací si vyhledejte tone mapping, Agx, ACES!
* `Exposure` - celkový jas obrazu, podobně jako úprava clony u fotoaparátu. Může to být rychlý způsob, jak globálně zesvětlit nebo ztmavit obraz.
* `Saturation` - síla barev. 1 je neutrální, 0 je monochromatické, hodnoty nad 1 jsou stále více saturované.
* `Contrast` - Zesiluje rozdíl mezi tmavými a světlými oblastmi. Používejte opatrně, při vysokých hodnotách může zavádět artefakty.

Všimněte si, že s vypnutým `Tone Mapping` některé detaily mizí, protože pixely jsou příliš jasné.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping může zesílit efekt globální iluminace. Pokud snížíte intenzitu environment mapy, zvýšíte primární zdroj světla, můžete zvýšit `exposure` v tone mappingu, abyste viděli více efektů odraženého světla.
:::

## Color Grading
Podobně jako nástroj křivek ve Photoshopu vám to umožňuje ovládat vyvážení a rozložení barev v obrazu. `main` ovládací prvek ovlivňuje celkové barevné vyvážení, `red`/`green`/`blue` umožňují jemné doladění. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Detekuje místa, kde dochází k rychlým změnám křivosti, a na tyto oblasti aplikuje barvu.

* `Factor` - celková intenzita efektu
* `Bump` - jak moc bude hledat ostré konvexní změny a umisťovat tam zvolenou barvu (výchozí je bílá)
* `Cavity` - jak moc bude detekovat konkávní změny a umisťovat tam zvolenou barvu (výchozí je černá)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Chromatic Aberration
Simuluje artefakty objektivu, kdy se světlo rozkládá u okrajů obrazovky.

* `Strength` - jak moc se červené/zelené/modré části obrazu rozštěpí směrem k okrajům obrazovky

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignette
Simuluje artefakty objektivu ztmavením okrajů obrazovky.

* `Size` - Velikost invertované elipsy umístěné přes obraz
* `Hardness` - Jak rozmazaně nebo ostře je elipsa smíchána s obrazem.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Přidá efekt zrna, který může pomoci, aby obraz působil méně uměle.

* `Strength` - množství zrna/šumu přidaného do obrazu.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Sharpness
Efekt doostření podobný tomu ve Photoshopu nebo aplikacích pro úpravu fotek.

* `Strength` - množství doostření aplikovaného na obraz.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Simuluje pixel art z retro her.

* `Slider` - velikost pixelů
* `Allow frame sampling` - pokud dostáváte spoustu černých pixelů, zkuste toto zapnout; přepíše to výchozí sampling.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Simuluje vzhled starých CRT monitorů.

* `Factor` - síla linek
* `Spacing` - velikost linek

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering

Dithering pixelů pro redukci pruhových (banding) artefaktů. Obvykle by měl být zapnutý, ale může být vypnut pro specifické operace (např. export depth map nebo jiné operace specifické pro data).
