# ![](/icons/material.webp) Materiál {#material}

V této nabídce můžete změnit materiál aktuálního objektu, vlastnosti vykreslování objektu a materiálu a přiřadit materiálu textury.

![](/images/material_overview.webp)

Materiály určují, jak objekt vypadá, tím, že řídí, jak reaguje na světlo a na ostatní objekty. Vzhled objektu ovlivňují tyto vlastnosti:

* `Typ materiálu`
* `Barva`
* `Drsnost`
* `Kovovost`
* `Krytí`
* `Odrazivost`
* `Emise/neosvětlené`

Kombinacemi těchto vlastností dosáhnete široké škály výsledků, od fotorealistických přes kreslené až po experimentální.

Barvu, drsnost, kovovost a krytí lze malovat, víc informací najdete v [možnostech malování do vrcholů](painting.md).

Typ materiálu, odrazivost a emise/neosvětlené jsou vlastnosti materiálu vysvětlené níže.

Tlačítky `Kopírovat` a `Vložit` nahoře v této nabídce můžete kopírovat materiály z jednoho objektu na druhý.

Vykreslovač Nomadu pracuje v reálném čase; je výkonný, ale u některých efektů dává přednost rychlosti před přesností. 

## Typy materiálů {#material-types}

![](/images/material_types.webp)

Typy materiálů v Nomadu jsou Neprůhledný, Podpovrchová, Míchání, Přídavné, Lom světla, Dithering a Stínový zachytávač.

### ![](/icons/material_opaque.webp) Neprůhledný {#opaque}
Výchozí režim, který povrch bere jako jednoduchý materiál s podporou malované barvy, drsnosti, kovovosti a krytí. Malované krytí, textura krytí nebo alfa kanál barevné textury objekt stále zprůhlední, pomocí ditheringu. Ignoruje se jen hlavní posuvník krytí.

### ![](/icons/material_subsurface.webp) Podpovrchová {#subsurface}
Tento režim simuluje materiály, ve kterých se světlo uvnitř rozptyluje a rozmazává, jako kůže, vosk nebo nefrit.

Vyžaduje režim stínování PBR. Nejlepšího výsledku dosáhnete s alespoň jedním směrovým nebo bodovým (spot) světlem, ideálně s tlumeným prostředím.

Barevný vzorek nastavuje barvu rozptýleného světla.

`Hloubka` určuje, jak daleko se světlo rozptýlí od přední strany pod povrch a zase ven přední stranou. Změkčuje to ostré stíny a rozmazává detaily povrchu.

`Průsvitnost` určuje, jak se světlo rozptyluje z přední strany tvaru na zadní, například jako když prosvítá spodní stranou listu, nebo když jsou uši silně podsvícené zezadu. Abyste to viděli, potřebujete světlo, které vrhá stíny.

### ![](/icons/material_blending.webp) Míchání {#blending}

Podobné jako Neprůhledný, ale podporuje posuvník krytí, takže materiál může přecházet mezi plným a průhledným. Jde o jediný jednoduchý posuvník krytí, na rozdíl od malovaného krytí, které podporuje neprůhledný materiál. 

::: warning
Režim míchání může u složitých nebo protínajících se tvarů způsobovat blikání a přeskakování.
:::

### ![](/icons/material_additive.webp) Přídavné {#additive}
S tímto materiálem můžete síť udělat poloprůhlednou. Podobá se materiálu míchání, ale zatímco míchání se mísí s okolím, přídavné bude vždy světlejší než objekty za ním. Hodí se pro jasné efekty, jako jsou paprsky světla, oheň nebo výbuchy.

Krytí můžete nastavit i na hodnotu vyšší než 1, objekt pak bude jasnější.  
To se hodí, pokud chcete použít [bloom](postprocess.md#bloom) a parametr `Prahová hodnota`, aby tento objekt zářil jako emisní objekt.

Tento režim mívá méně artefaktů než [Míchání](#blending) (průhlednost nezávislá na pořadí).

### ![](/icons/material_refraction.webp) Lom světla {#refraction}
Tento režim slouží k simulaci skla. Vyžaduje režim stínování PBR. Kvůli omezením vykreslování v reálném čase je lom světla v sobě samém a vícevrstvý lom poněkud omezený.

Malovaná drsnost modelu ovlivňuje, jak rozmazaný lom bude.
Ve výchozím stavu má každý objekt vytvořený v Nomadu drsnost kolem 25 %, takže lom nebude dokonalý, ale trochu rozmazaný.
Tlačítkem `Lesklý nátěr` můžete model přemalovat na drsnost a kovovost 0 (barvy se nezmění).

Ve hře jsou 2 různé drsnosti: jedna určuje, jak rozmazaný je odraz na povrchu, druhá řídí vnitřek (lom).  
Nomad ale má jen jeden malovaný kanál drsnosti, takže vnitřní i vnější drsnost sdílejí stejnou hodnotu.  
Chcete-li mít různé hodnoty (například lízátko s ostrým povrchem, ale rozmazaným vnitřkem), použijte posuvníky `Povrch` a `Interiér` v části `Přepsat drsnost`, které malovanou drsnost přepíšou.

![](/videos/refraction.mp4)

#### Index lomu {#index-of-refraction}
Jak moc se světlo ohne, když vstupuje do objektu. Vyšší hodnoty ho ohýbají víc, jako tlustá čočka.

#### Absorpce {#absorption}
Simuluje pohlcování světla při průchodu objemem, zabarvené barevným vzorkem; `Faktor` nastavuje sílu. Tenké části jsou světlejší, protože propouštějí víc světla, zatímco silná místa jsou tmavší. Používá se jen přibližná tloušťka objektu, takže efekt hodně závisí na tvaru.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Udělá objekt poloprůhledným tím, že náhodně vynechá některé pixely.

### ![](/icons/material_shadow_catcher.webp) Stínový zachytávač {#shadow-catcher}

Udělá objekt neviditelným, takže jen přijímá stíny od světel. Hodí se ke kombinování renderů z Nomadu s jinými obrázky, obvykle na rovině. Barevný vzorek nastavuje barvu stínu.

Ve scéně musí být světlo vrhající stíny, jinak stínový zachytávač nedělá nic. Tlačítka `Kovovost → 0%` a `Kovovost → 100%` objekt přemalují: když je plně kovový, může stínový zachytávač také odrážet scénu, pokud je zapnutý postproces [Odraz (SSR)](postprocess.md#reflection-ssr).

::: tip

Další informace o průhlednosti a režimech míchání najdete na https://support.fab.com/s/article/Transparency-Opacity

:::

## Ovládání {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Vždy neosvětlené {#always-unlit}
Když je zapnuté, objekt ignoruje PBR i Matcap a jednoduše zobrazí svou malovanou barvu bez stínování.
Pokud používáte [Přídavné](#additive), můžete průhlednost malovat přímo černou barvou.

### Krytí {#opacity}
Jak plný nebo neprůhledný objekt bude: 100 % je plný, 0 % průhledný. Posuvník se ukazuje u typů Míchání, Přídavné, Dithering a Stínový zachytávač. Pro jemnější kontrolu můžete krytí i malovat.

### Předrefrakční průchod {#pre-refract-pass}
Jen Míchání a Přídavné. Vykreslí tento průhledný objekt před průchodem lomu světla. Hodí se, když je objekt s lomem světla před jinými průhlednými povrchy.

### Odrazivost {#reflectance}
Určuje množství odrazu, které materiál dostane, u nekovových materiálů. Většinou byste měli použít výchozí hodnotu (odpovídá standardním 4 % odraženého světla při kolmém úhlu), ale můžete ji zvýšit a posílit tak odrazy a odlesky například v očích postavy. Vyžaduje režim stínování PBR.

### ![](/icons/culling.webp) Inverzní odstranění {#inverse-culling}
Obrátí normály povrchu. Obvykle to není potřeba, ale hodí se, když model vypadá naruby, nebo v kombinaci s vypnutým `Oboustranné` k vytváření interiérů, kde je stěna nejblíže ke kameře vždy skrytá.

Následující možnosti lze nastavit na `Auto`, `Ne` nebo `Ano`. U `Auto` šipka ukazuje hodnotu, která se skutečně použije.

### ![](/icons/sphere_smooth.webp) Hladké odstíny {#smooth-shading}
Viz [globální možnost](settings.md#smooth-shading).  
Hodnota `Auto` použije globální možnost.

### ![](/icons/culling.webp) Oboustranné {#two-sided}
Plochy budou vidět z obou stran. Viz [globální možnost](settings.md#two-sided-quick).  
Hodnota `Auto` použije globální možnost.

### ![](/icons/culling.webp) Zadní strana barevná {#coloured-backface}
Viz [globální možnost](settings.md#two-sided-quick).
Hodnota `Auto` použije globální možnost.

### ![](/icons/shadow_cast.webp) Vrhání stínů {#casts-shadows}
Stíny vrhají i průhledné objekty (ditheringovým vzorem, který napodobuje prolnuté stíny).  
Nezapomeňte vrhání stínů vypnout, pokud máte ve scéně velký objekt, který stíny vrhat nepotřebuje (například velkou podlahu).

### ![](/icons/shadow_receive.webp) Příjem stínů {#recieve-shadows}
Jestli se na tomto objektu vykreslují stíny od ostatních objektů.

### ![](/icons/wireframe.webp) Drátový model {#wireframe}
Viz [globální možnost](settings.md#wireframe).  
Hodnota `Auto` použije globální možnost.

### ![](/icons/trash.webp) Resetovat normály {#reset-normals}
Zobrazí se jen tehdy, když importovaný objekt nese vlastní normály (například se `Zachovat topologii`). Odstraní je, takže stínování použije normály vypočítané z povrchu.


## Textury {#textures}

![](/images/material_textures.webp)

Pokud má objekt UV, můžete na materiál kromě barvy/drsnosti/kovovosti/krytí ve vrcholech použít i textury. Obvykle jsou výsledkem pečení textur, ale můžete použít i obrázky vytvořené mimo Nomad. `UV:✓` nebo `UV:✗` vedle nadpisu ukazuje, jestli má objekt UV.

Textury lze použít pro

* Barva
* Normála
* Drsnost
* Kovovost
* Krytí
* Posunutí
* Emise

Řádek `Okluze` se objeví také tehdy, když má importovaný objekt texturu okluze, Nomad ji ale nepoužívá.

Posuvník v každém řádku nastavuje, jak silně se textura použije, od vůbec po úplně. `Barva` a `Emise` mají také barevný vzorek, který texturu tónuje, a `Emise` nastavuje sílu záře.

`Posunutí` nastavuje, jak daleko mapa posunutí vytlačí povrch. Jeho tlačítko `Použít` posune vrcholy podle posunutí a mapu pak odstraní. Výsledek se uloží do aktivní vrstvy.

Tlačítko palety vedle nadpisu otevře předvolby materiálů z nabídky [malování](painting.md): klepnutím na jednu zkopírujete její textury na objekt. Na počítači se importované obrázky synchronizují s původním souborem, když se vrátíte do Nomadu, a tlačítko synchronizace vedle nadpisu je znovu načte.

Klepnutím na texturový slot otevřete výběr. Když už je ke slotu materiálu textura přiřazená, dalším klepnutím otevřete panel textury:

### Možnosti panelu textury {#texture-panel-options}

![](/images/material_texture_panel.webp)

Panel ukazuje velikost obrázku a náhled textury.

### ![](/icons/open.webp) Otevřít {#open}
Vybere jinou texturu. Na počítači `Prozkoumat` ukáže soubor obrázku ve správci souborů.

### ![](/icons/circle_cross.webp) Žádný {#none}
Odstraní texturu.

### Krytí {#texture-opacity}

Jen barevná textura. Pokud má obrázek alfa kanál, můžete ho použít pro krytí, nebo ho ignorovat.

### Formát {#normal-format}
Jen textura normál. Normálové mapy existují ve dvou variantách, `OpenGL (+Y)` a `DirectX (-Y)`. Pokud detaily vypadají obráceně, zkuste tu druhou.

### Výška {#displacement-height}
Jen textura posunutí.
* `Lokální` - Výška roste a klesá s měřítkem objektu.
* `Svět` - Výška zůstává stejná bez ohledu na měřítko objektu.

### Násobit {#multiply}
Jen textury drsnosti, kovovosti a krytí. Vynásobí hodnoty textury. Když není 100 %, hodnota se ukáže na texturovém slotu.

### ![](/icons/link.webp) Ikona řetězu/propojení {#chainlink-icon}

Když je ikona propojení v následujících částech zapnutá, všechna použitá nastavení se sdílejí s ostatními texturami (barva, normála, drsnost, kovovost, krytí, emise), které mají ikonu propojení také zapnutou. 

Díky tomu zůstanou zarovnané textury zarovnané, i když změníte parametry nebo typ projekce.


### Projekce {#projection}
![](/images/material_projection.webp)

Nastavuje, jak se textura na objekt použije.

* `Auto` - UV, pokud má objekt UV, jinak Triplanar
* `UV` - K použití textury se využijí UV souřadnice sítě. Pokud síť a textura pocházejí odjinud než z Nomadu, nebo je budete z Nomadu exportovat a používat jinde, je UV správná volba.
* `Triplanar` - Promítne texturu podél os X, Y, Z a prolne švy. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanární projekce je výkonný, a přitom jednoduchý způsob, jak na objekty použít textury.

Je to jako mít 6 projektorů se stejným obrázkem, které svítí na přední, zadní, levou, pravou, horní a spodní stranu objektu.

Výsledek pak můžete v případě potřeby vypéct do UV nebo do barev vrcholů.


![](/images/material_triplanar_example.webp)

#### Metoda {#method}

* `Lokální` - Projekce se pohybuje s transformací objektu
* `Svět` - Projekce zůstává na místě a objekt jí při posunu projíždí.

#### Tvrdost {#hardness}

Jak se projekce prolínají. 100 % neprolíná vůbec a okraje projekcí budou ostré. 0 % prolne okraje v širokém úhlu. Výchozí hodnota je 90 %, dost prolnutí na skrytí okrajů, přičemž zbytek projekcí zůstane ostrý.

### Jednotný {#uniform}

Když je zaškrtnuté, použije se pro všechny projekce stejná tvrdost. Když není, objeví se další ovládání tvrdosti pro projekce X, Y a Z.


### Parametr {#parameter}
![](/images/material_parameter.webp)

#### Filtr {#filtering}
Metoda filtrování textury: výchozí je `Auto`, dalšími metodami jsou `Nejbližší`, `Lineární` a `Mipmap`. Nejbližší nefiltruje vůbec, takže zblízka mohou mít textury zubaté artefakty. Lineární a Mipmap filtrují lépe, takže textury jsou zblízka spíš rozmazané než zubaté.

#### Dláždění - X {#tiling-x}
Když je parametr Měřítko větší než 1 a textura je tak menší než UV objektu, určuje, jak se textura opakuje podél osy X. `Nic` znamená žádné opakování. `Opakovat` vytvoří kopie textury. `Zrcadlit` vytvoří kopie textury, z nichž každá druhá je převrácená, což může pomoci skrýt artefakty opakování.

#### Dláždění - Y {#tiling-y}
Stejné jako Dláždění - X, ale pro osu Y.

### Přeměnit {#transform}
![](/images/material_transform.webp)

Další 2d transformace použité na texturu v prostoru UV. Tlačítko resetu vrátí výchozí hodnoty; ikona řetězu (když jsou vybrané jiné textury než barva) propojí nebo rozpojí transformaci tak, aby byla stejná jako u barevné textury.

#### Posun {#translation}
Posun textury v ose X a Y.

#### Rotace {#rotation}
Rotace textury.

#### Měřítko {#scale}
Měřítko textury: větší čísla texturu na objektu zmenší. Co se pak stane, určíte možnostmi Dláždění - X a Dláždění - Y.

### Jednotné měřítko {#uniform-scale}
Když je vypnuté, Nomad ukáže samostatné ovládání pro měřítko X a měřítko Y.
