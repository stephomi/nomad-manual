# ![](/icons/material.webp) Materiál {#material}

Toto menu umožňuje změnit materiál aktuálního objektu, vlastnosti vykreslování objektu/materiálu a přiřadit materiálu textury.

![](/images/material_overview.webp)

Materiály určují, jak objekt vypadá, tím, že řídí, jak reaguje na světlo a na ostatní objekty. Vzhled objektu je řízen těmito vlastnostmi:

* `Typ materiálu`
* `Barva`
* `Drsnost`
* `Kovovost`
* `Průhlednost`
* `Odrazivost`
* `Emisní/neosvětlený`

Kombinace těchto vlastností umožňují dosáhnout široké škály výsledků od fotorealistických po kreslené až po experimentální.

Barvu, drsnost, kovovost a průhlednost lze malovat, více informací viz [Možnosti Vertex Paint](painting.md).

Typ materiálu, odrazivost, emisní/neosvětlený jsou materiálové vlastnosti vysvětlené níže.

Tlačítka kopírovat/vložit v horní části tohoto menu umožňují kopírovat materiály z jednoho objektu na druhý.

Všimněte si, že renderer Nomadu je renderer v reálném čase; i když je výkonný, u některých efektů upřednostňuje rychlost před přesností. 

## Typy materiálu {#material-types}

![](/images/material_types.webp)

Typy materiálu v Nomadu jsou Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Neprůhledný {#opaque}
Výchozí režim, který považuje povrchy za jednoduchý materiál podporující malovanou barvu, drsnost, kovovost a průhlednost.

### ![](/icons/material_subsurface.webp) Podpovrchový {#subsurface}
Tento režim může simulovat materiál, který umožňuje světlu se interně rozmazávat a rozptylovat, jako je kůže, vosk, jadeit.

Pro nejlepší výsledek přepněte na PBR stínování a použijte alespoň jedno směrové nebo bodové světlo, ideálně s tlumeným prostředím.

`Depth` určuje, jak daleko se světlo rozptyluje z přední strany pod povrch a pak znovu ven předním povrchem. To má za následek změkčení tvrdých stínů a rozmazání detailů povrchu.

`Translucency` řídí, jak se světlo rozptyluje z přední na zadní stranu tvaru, jako rozptyl světla spodní stranou listu nebo když jsou uši silně nasvícené zezadu. 

### ![](/icons/material_blending.webp) Mísení {#blending}

Podobné jako Opaque, ale podporuje posuvník průhlednosti, který umožňuje materiálu přecházet mezi pevným a průhledným. Jde o jednoduchý jediný posuvník pro průhlednost, oproti malovatelné průhlednosti podporované neprůhledným materiálem. 

::: warning
Režim Blending může způsobovat blikání a problikávání u složitých nebo protínajících se tvarů.
:::

### ![](/icons/material_additive.webp) Aditivní {#additive}
S tímto materiálem můžete udělat svou síť (mesh) poloprůhlednou. Je podobný materiálu Blending, ale zatímco Blending se mísí se svým okolím, Additive bude vždy jasnější než objekty za ním, což je vhodné pro jasné efekty jako světelné paprsky, oheň, exploze.

Můžete nastavit hodnotu průhlednosti vyšší než 1, což znamená, že objekt bude jasnější.  
To může být užitečné, pokud chcete použít [bloom](postprocess.md#bloom) a `parametr threshold`, abyste nechali zářit pouze tento objekt jako emisní objekt.

Tento režim má tendenci mít méně artefaktů než [Blending](#blending) (transparentnost nezávislá na pořadí).

### ![](/icons/material_refraction.webp) Refrakce {#refraction}
Tento režim lze použít k simulaci skleněného materiálu. Kvůli omezením reálného času jsou samolomy a vícevrstvé lomy do určité míry omezené.

Malovaná drsnost modelu ovlivňuje, jak rozmazaný lom je.
Ve výchozím nastavení má každý objekt vytvořený v Nomadu drsnost mírně kolem 25 %, takže lom nebude dokonalý, ale mírně rozmazaný.
Můžete použít tlačítko `paint glossy` k přemalování modelu s drsností a kovovostí 0 (barvy nebudou ovlivněny).

Hrají zde roli 2 různé drsnosti: jedna řídí, jak rozmazaný je odraz na povrchu, a druhá řídí vnitřek (lom).  
Protože však v Nomadu existuje pouze jeden malovací kanál drsnosti, budou vnitřní i vnější drsnost sdílet stejnou hodnotu.  
Abyste mohli mít různé hodnoty (například lízátko s ostrým povrchem, ale rozmazaným vnitřkem), použijte posuvníky `Surface glossiness` a `Interior roughness` k přepsání malované drsnosti.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Způsobí, že objekt bude poloprůhledný tím, že náhodně vyřazuje některé pixely.

### ![](/icons/material_shadow_catcher.webp) Zachytávač stínů {#shadow-catcher}

Způsobí, že objekt bude neviditelný a bude pouze přijímat stíny. Užitečné pro kombinování renderů z Nomadu s jinými obrázky. 

::: tip

Další informace o průhlednosti a režimech míchání najdete na https://support.fab.com/s/article/Transparency-Opacity

:::

## Ovládání {#controls}

![](/images/material_controls.webp)

### Vždy neosvětlené {#always-unlit}
Pokud je povoleno, objekt bude ignorovat PBR a Matcap a jednoduše zobrazí svou malovanou barvu bez stínování.
Všimněte si, že pokud používáte [Additive](#additive), můžete malovat průhlednost přímo pomocí černé barvy.

### Průhlednost {#opacity}
Jak pevný nebo neprůhledný se objekt jeví; 100 % je pevný, 0 % je průhledný. Pro jemnější kontrolu můžete také malovat průhlednost.

### Odrazivost {#reflectance}
Řídí množství odrazu, které materiál přijímá pro ne-kovové materiály. Většinu času by se měla používat výchozí hodnota (která odpovídá standardním 4 % odraženého světla v kolmém úhlu), ale lze ji zvýšit pro zesílení odrazů a zvýraznění například v očích postav.

### Inverzní odřezávání {#inverse-culling}
Obrátí normály povrchu. Obvykle není potřeba, ale lze jej použít, pokud se model jeví naruby, nebo v kombinaci s vypnutým `Two sided` lze použít k tvorbě interiérů, kde je stěna nejblíže kameře vždy skrytá.

### Hladké stínování {#smooth-shading}
Viz [globální volba](settings.md#smooth-shading).  
Hodnota `Auto` použije globální volbu.

### Oboustranné {#two-sided}
Viz [globální volba](settings.md#two-sided).  
Hodnota `Auto` použije globální volbu.

### Barevná zadní strana {#coloured-backface}
Viz [globální volba](settings#two-sided).
Hodnota `Auto` použije globální volbu.

### Vrhá stíny {#casts-shadows}
Prozatím je `Auto` stejné jako `On`.
Průhledné objekty také vrhají stíny (v dithering vzoru pro emulaci míchaných stínů).  
Ujistěte se, že vypnete vrhání stínů, pokud máte ve scéně velký objekt, který nemusí vrhat stíny (například velkou podlahu).

### Přijímá stíny {#recieve-shadows}
Prozatím je `Auto` stejné jako `On`.

### Drátěný model {#wireframe}
Viz [globální volba](settings.md#wireframe).  
Hodnota `Auto` použije globální volbu.


## Textury {#textures}

![](/images/material_textures.webp)

Pokud má objekt UV souřadnice, lze k materiálu kromě vrcholové barvy/drsnosti/kovovosti/průhlednosti aplikovat i textury. Obvykle jsou výsledkem bake textur, ale lze použít i obrázky vytvořené mimo Nomad.

Textury lze aplikovat na

* Barvu
* Normálu
* Drsnost
* Kovovost
* Průhlednost
* Emisi

Kliknutím na slot textury se otevře výběr. Po přiřazení textury do slotu materiálu se po opětovném kliknutí zobrazí panel textury:

### Možnosti panelu textur {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Otevřít {#open}
Vybrat jinou texturu

### Žádné {#none}
Odstranit texturu

### Průhlednost {#texture-opacity}

Pokud má obrázek alfa kanál, toto umožní použít jej pro průhlednost (Opacity) nebo jej ignorovat.

### ![](/icons/link.webp) Ikona řetězu/odkazu {#chainlink-icon}

Ikona odkazu v následujících sekcích, pokud je povolena, znamená, že jakékoli použité volby budou sdíleny s ostatními texturami (barva, normála, drsnost, kovovost, průhlednost, emise), které mají také povolenou svou ikonu odkazu. 

To vám umožní zajistit, že pokud máte zarovnané textury, zůstanou zarovnané i při změně parametrů nebo typů projekce.


### Projekce {#projection}
![](/images/material_projection.webp)

Nastaví, jak má být textura na objekt aplikována.

* `Auto` - Pokud má objekt UV, UV, jinak Triplanar
* `UV` - Použije UV souřadnice meshe k aplikaci textury. Pokud mesh a textura pocházejí mimo Nomad nebo mají být z Nomadu exportovány k použití jinde, UV je správná volba.
* `Triplanar` - Promítá texturu podél os X, Y, Z a mísí spoje. 

### Triplanární {#triplanar}
![](/images/material_triplanar.webp)

Triplanární projekce jsou výkonný, ale jednoduchý způsob aplikace textur na objekty.

Triplanar je jako mít 6 videoprojektorů se stejným obrázkem, které svítí na přední, zadní, levou, pravou, horní a spodní stranu objektu.

Pokud je potřeba, lze to poté bakeovat do UV nebo vrcholových barev.


![](/images/material_triplanar_example.webp)

#### Metoda {#method}

* `Local` - Projekce se bude pohybovat s transformací objektu
* `World` - Projekce zůstane fixní, pohyb objektu jím bude „klouzat“ skrz projekci.

#### Tvrdost {#hardness}

Jak se projekce mísí. 100 % nebude dělat žádné míchání a hrany projekcí budou ostré. 0 % bude míchat hrany přes široký úhel. Výchozí hodnota je 90 %, což je dostatečné míchání k ukrytí hran a zároveň ponechání zbytku projekcí ostrých.

### Uniformní {#uniform}

Pokud je zaškrtnuto, používá se stejná tvrdost pro všechny projekce. Pokud není zaškrtnuto, zobrazí se další ovládací prvky tvrdosti pro projekce X, Y, Z.


### Parametr {#parameter}
![](/images/material_parameter.webp)

#### Filtrování {#filtering}
Metoda filtrování textury, `Auto` je výchozí, metody jsou `Nearest`, `Linear`, `Mipmap`. Nearest neprovádí žádné filtrování, takže textury mohou zblízka vykazovat zubaté artefakty. Linear a Mipmap provádějí lepší filtrování, takže textury vypadají zblízka spíše rozmazaně než zubatě.

#### Dlaždicování-X {#tiling-x}
Pokud je parametr Scale větší než 1, takže textura je menší než UV objektu, jak bude textura dlážděna podél osy X. `None` znamená žádné opakování. `Repeat` bude dělat kopie textury. `Mirror` bude dělat kopie textury, přičemž každá druhá kopie bude převrácená, což může pomoci skrýt artefakty dlaždicování.

#### Dlaždicování-Y {#tiling-y}
Stejné jako Tiling-X, ale pro osu Y.

### Transformace {#transform}
![](/images/material_transform.webp)

Další 2D transformace aplikované na texturu v UV prostoru. Tlačítko reset vrátí výchozí hodnoty, ikona řetězu (pokud jsou vybrány jiné textury než barva) propojí nebo odpojí transformaci tak, aby byla stejná jako u barevné textury.

#### Posun {#translation}
Posun textury v osách X a Y

#### Rotace {#rotation}
Rotace textury

#### Měřítko {#scale}
Měřítko textury, větší čísla způsobí, že textura bude na objektu menší, použijte posuvníky Tiling-X a Tiling-Y k řízení, co se stane.

### Uniformní měřítko {#uniform-scale}
Pokud je vypnuto, Nomad zobrazí samostatné ovládací prvky pro Scale-X a Scale-Y.