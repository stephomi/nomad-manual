# ![](/icons/cog.webp) Nastavení {#reset-to-default}

Nabídka nastavení obsahuje mnoho možností, jak ovlivnit vzhled a chování Nomadu.

![](/images/settings_overview.webp)

Řada tlačítek nahoře v nabídce vás přenese přímo do jednotlivých částí: `Kurzor`, `Indikátor`, `Drát`, `Mřížka`, `Oboustranné`, `Obrys`, `Zvýraznit`, `Navigátor`, `Statistiky`, `Úchopy`, `Tvar`, `Opakovače` a `Multires`.

## Nastavení zobrazení {#display-settings}
Tato část obsahuje rychlé zkratky pro většinu nastavení, která najdete níže v této nabídce.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Hladké odstíny {#smooth-shading}
Přepíná mezi hladkým a fasetovým stínováním. Při fasetovém stínování se polygony stínují každý zvlášť, takže vidíte topologii pod povrchem.
Fasetové stínování se může hodit během modelování a pro renderování pak přepnete na hladké.

Vypnutí hladkých odstínů trochu zlepší výkon.

### ![](/icons/outline.webp) Obrys {#outline-quick}
Zapne nebo vypne obrys kolem aktuálního výběru.

Hodí se jako vizuální zpětná vazba o právě vybrané síti (nebo sítích), pokud máte vypnuté [Ztmavit nevybrané objekty](#darken-unselected-objects).

Z hlediska výkonu je [Ztmavit nevybrané objekty](#darken-unselected-objects) mnohem lepší řešení než obrys.

### ![](/icons/grid.webp) Mřížka {#grid-quick}
Zapne nebo vypne mřížku v pozadí, která pomáhá pochopit umístění a měřítko objektů.

### ![](/icons/culling.webp) Oboustranné {#two-sided-quick}
Zapne nebo vypne zobrazení polygonů z obou stran. Každá plocha směřuje určitým směrem.
Plochy považované za *zadní strany* jsou ty, které směřují „od“ kamery.

Například jednoduchá koule při spuštění má plochy otočené ven.
Když kameru přesunete dovnitř koule, uvidíte zadní strany těchto ploch.

Většinou byste zadní strany ploch vidět neměli, takže jejich obarvení vám pomůže odhalit možné problémy nebo chybnou topologii.

Vypnutí vykreslování `Oboustranné` může trochu zlepšit výkon vykreslování.


### ![](/icons/wireframe.webp) Drátový model {#wireframe-quick}
Zapne nebo vypne překryv drátového modelu. 

Zapnutý drátový model snižuje výkon.

### ![](/icons/navigator.webp) Navigátor {#snap-cube-quick}
Zapne nebo vypne pomocnou ikonu v rohu scény, která pomáhá s orientací v prostoru a rychlým přepínáním mezi pohledy zepředu/zezadu/zleva/zprava/shora/zdola.

### ![](/icons/palette.webp) Zobrazit malbu {#show-painting}
Zapne nebo vypne zobrazení malby. Když je vypnuté, objekty se místo své malby zobrazí s bílým nekovovým materiálem s drsností 25 %.

### ![](/icons/tool_hide.webp) Použít Skrytí {#use-hide}
Zapne nebo vypne režim skrytí. Když je vypnutý, skrytí pořád existuje, jen je deaktivované. Toto tlačítko je nedostupné, pokud právě používáte nástroj skrytí.

### ![](/icons/shield.webp) Zobrazit masku {#show-mask}
Zapne nebo vypne režim masky. Když je vypnutý, maska pořád existuje, jen je deaktivovaná. Dalším stisknutím tlačítka ji znovu zapnete.

Pokud potřebujete masku skrýt A zároveň ji mít aktivní, nastavte níže barvu masky na bílou. Nezapomeňte ji pak vrátit na šedou!

Toto tlačítko je nedostupné, pokud právě používáte některý nástroj masky. 

### ![](/icons/shield.webp) Maska → Neprůhledný {#mask-opaque}
`Maska → Neprůhledný` u maskované masky ignoruje průhledné vrcholy. Týká se to jen krytí ve vrcholech a v texturách, plochy skryté pomocí „skrýt“ zůstanou skryté. Je dostupné jen tehdy, když je zapnuté `Zobrazit masku`.

### ![](/icons/bang.webp) Zvýraznit {#highlight-quick}
Zapne nebo vypne záblesk při výběru. Při výběru objektů vybraný objekt na 500 milisekund krátce blikne. Barvu a délku záblesku můžete upravit níže.

### ![](/icons/list.webp) Statistiky {#stats-quick}
Zapne nebo vypne stavový text ve 3d výřezu. Zobrazuje informace o systémové paměti, celkovém počtu vrcholů ve scéně a počtu vrcholů aktuálního výběru.

----- 

### ![](/icons/cube.webp) Ztmavit nevybrané objekty {#darken-unselected-objects}
Nevybrané objekty se ztmaví, aby aktuální výběr vynikl.

### ![](/icons/shield.webp) Maska {#mask}
Barva maskování, ve výchozím stavu středně šedá, která se násobí barvou objektu. Nastavte ji na bílou, aby byla maska neviditelná, ale nezapomeňte ji pak vrátit na šedou!

## ![](/icons/cursor.webp) Kurzor {#cursor}

### Kruh {#show-circle-while-sculpting}
Kdy se má zobrazovat kruh s poloměrem štětce:

* `Auto` - kruh se zobrazuje, ale během modelování se skryje.
* `Ne` - kruh se nikdy nezobrazuje.
* `Ano` - kruh se zobrazuje vždy, i během modelování.

### Zobrazit malou tečku {#show-small-dot}
Zobrazí tečku ve středu tahu štětce během modelování nebo při změně pivotu kamery.

### Zobrazit stabilizátor lana {#show-rope-stabilizer}
Vykreslí čáru, která ukazuje délku lana, když je v nastavení tahu aktivní [stabilizátor lana](stroke.md#lazy-rope-stabilizer).

### Zobrazit nápovědu náklonu {#show-roll-hint}
Zobrazí vodítko směru náklonu, když používáte klávesovou zkratku pro naklánění.

### ![](/icons/radius.webp) Velikost {#dot-size}
Velikost malé tečky.

### Barvy {#cursor-colors}
Kurzor mění barvu podle toho, co právě děláte: `Sochařit`, `Pozadí` (najetí nad pozadí), `Maska`, `Hladit`, `Kamera` a `Poloměr`. Každou barvu si tu můžete upravit.

## ![](/icons/cursor.webp) Indikátor {#indicator}
![](/images/settings_indicator.webp)

Zobrazuje vizuální indikátory pro návody a záznamy obrazovky. Zapnete ho nastavením na `Ano` (v iOS je k dispozici i možnost `Auto`).

Tlačítka `Prst`, `Stylus` a `Myš` zapnou zobrazení ikony, když je zjištěn daný typ vstupu.

### Barva {#indicator-color}
Barva indikátoru.

### Velikost/ikona/kruh {#indicator-shape}
Ovládání velikosti indikátoru a krytí ikony a kruhu v něm.

## ![](/icons/wireframe.webp) Drátový model {#wireframe}
![](/images/settings_wireframe.webp)
Zapne překryv drátového modelu.

### Cíl {#target}
Určuje, jestli se drátový model zobrazí i u nevybraných objektů, jen u vybraných, nebo u všech.

### Skrýt {#hide}
Určuje, jestli se drátový model zobrazí i u skrytých polygonů.

### Multirezoluce: Pouze úroveň 0 {#multiresolution-level-0-only}
Multirezoluce zobrazuje drátový model úrovně 0 tmavší a vyšší úrovně postupně světlejší. Když je tato možnost zapnutá, zobrazí se jen drátový model úrovně 0.

### Barva {#wireframe-color}
Nastavuje barvu a krytí drátového modelu.

## ![](/icons/grid.webp) Mřížka {#grid}
![](/images/settings_grid.webp)
Zapne mřížku.

### Zachycení {#snap}
Tyto možnosti přichytávají body nástrojů založených na křivkách a tvarech (`Soustruh`, `Trubka`, polygonové tvary a cesty...) během kreslení:

* `Přichytit k mřížce` - přichytí k mřížce.
* `Přichytit k bodům (zarovnané zobrazení)` - přichytí k blízkým existujícím bodům, když je kamera zarovnaná s osou.
* `Přichytit k bodům (volné zobrazení)` - přichytí k blízkým existujícím bodům, když kamera zarovnaná není.

### Barva {#grid-color}
Nastavuje barvu a krytí mřížky. Tyto možnosti se ukážou, když je mřížka vidět.

`Vinětace` mřížku směrem k okrajům postupně zeslabuje. `Práh přichycení dělení` nastavuje v pixelech, jak husté mohou být čáry mřížky na obrazovce, než mřížka přepne na jinou úroveň dělení.

## ![](/icons/culling.webp)Oboustranné {#two-sided}
Umožní vidět plochy polygonů z obou stran.

### Barva zadní strany {#backface-color}
`Zadní strana barevná` zapne obarvení zadních stran a `Barva zadní strany` nastaví barvu.

## ![](/icons/outline.webp)Obrys {#outline}
Zapne obrys kolem vybraných objektů.

### Barva obrysu, tloušťka {#outline-color-thickness}
Nastavuje barvu a `Tloušťka` obrysu.


## ![](/icons/bang.webp) Zvýraznit {#highlight}
Zapne krátký záblesk při změně výběru.
### Barva, doba trvání {#color-duration}
Nastavuje barvu a délku záblesku v milisekundách.

## ![](/icons/navigator.webp) Navigátor {#snap-cube}
![](/images/settings_snapcube.webp)

Zobrazí pomocnou ikonu v rohu scény, se kterou rychle přepnete mezi pohledy zepředu/zezadu/zleva/zprava/shora/zdola. Klepnutím na jeho strany přepínáte mezi ortografickými pohledy.

### Tvar {#shape}
Vyberte pro navigátor tvar koule, krychle nebo gnómonu (os).

### Omezit zarovnání {#restrict-alignment}
Zarovná pohledy přichycení s osami světa. Když je zapnuté, je možných jen 6 hlavních pohledů. Při `Auto` platí toto omezení jen tehdy, když je kamera v režimu `Otočný stůl`.

### Velikost {#size}
Nastavuje velikost navigátoru.

### Překlopit 180° {#flip-180}
Zapne chování při klepnutí: když je pohled přichycený, klepnutí na střed navigátoru otočí pohled o 180 stupňů. Když je například pohled přichycený zepředu, klepnutím na navigátor se otočíte do pohledu zezadu.

### Hrany a rohy {#edges-corners}
Přidá pohledy přichycení na hrany a rohy (jantarové zóny). Není dostupné s tvarem gnómonu.

### Tažení v režimu otočného stolu {#turntable-drag}
Tažení navigátoru otáčí bez naklánění kamery a zastavuje se na každém pohledu přichycení. Vypněte ho, chcete-li navigátorem otáčet místo toho rotací `Trackball`. Tak či tak zůstává tažení vodorovné nebo svislé. S kamerou v režimu `Otočný stůl` se navigátor táhne vždy tímto způsobem.

### Pozice {#snap-position}
Nastavuje, ve kterém rohu bude navigátor.


## ![](/icons/list.webp) Statistiky {#stats}
![](/images/settings_stats.webp)

Zobrazuje informace o systémové paměti, celkovém počtu vrcholů ve scéně a počtu vrcholů aktuálního výběru.

### Pozice {#stats-position}
Nastavuje, ve kterém rohu budou statistiky.

## ![](/icons/edit_radius.webp) Úchop {#handle}
Nastavení úchopů, které táhnete ve výřezu, například gizma.

### Číselný vstup {#gizmo-input}
Umožní zadat číslo po klepnutí na některý z ovládacích prvků gizma.

### Skrýt při interakci {#hide-on-interaction}
Gizmo během práce s ním zeslabí, aby nepřekáželo.

### ![](/icons/opacity.webp) Krytí {#handle-opacity}
Krytí úchopů.

## ![](/icons/shape_lasso.webp) Tvar {#shape-settings}
Jak na obrazovce vypadají tvary, které kreslíte tvarovými tahy (laso, obdélník, křivka...).

### ![](/icons/opacity.webp) Výplň, obrys {#shape-fill-outline}
Krytí vnitřku tvaru a čáry kolem něj.

### Barvy {#shape-colors}
Barva tvaru pro jednotlivé druhy nástrojů: `Maska`, `Skrýt`, `SkupinaPovrch` a `Oříznout`.

## ![](/icons/array.webp) Opakovače {#primitive-repeaters}
Limity pro kopie vytvářené [opakovači](scene#repeaters) (pole, radiální, křivka, povrch). Udržují Nomad svižný, když se opakovač vymkne z rukou.

### ![](/icons/cube.webp) Max. kopií {#repeater-max-copies}
Nejvyšší počet kopií, které jeden opakovač vytvoří. Nomadu dělá potíže velké množství objektů, ať jsou jakkoli malé.

### ![](/icons/cube.webp) Kopie ve scéně {#repeater-scene-copies}
Rozpočet kopií pro celou scénu. Kopie s nízkým počtem polygonů stojí málo geometrie, ale zůstává plnohodnotným objektem, takže malé kopie narazí nejdřív právě na tento limit.

### ![](/icons/triangle.webp) Max. počet ploch {#repeater-max-faces}
Rozpočet ploch pro všechny kopie ve scéně. Po jeho překročení přijdou o kopie jako první nejtěžší objekty.

## ![](/icons/multires.webp) Multirezoluce {#multires}
### Maximální počet vrcholů {#multires-lowres-count}
Nastaví práh, nad který nepovolí dělení multirezoluce, protože by Nomad nejspíš spadl: Nomad před dělením nekontroluje dostupnou paměť. Výchozí hodnota je 10 milionů.
### Práh nízkého rozlišení {#multires-lowres-threshold}
Při pohybu kamery se může zobrazovat nižší rozlišení sítě. Pokud chcete zobrazovat vyšší rozlišení sítě, můžete tuto hodnotu zvýšit.

## Nastavení {#advanced}
### ![](/icons/reset.webp) Obnovit na výchozí {#reset}
Vrátí všechny předvolby aplikace na výchozí hodnoty.

Některé prostředky se ukládají zvlášť a NEresetují se: projekty, klávesové zkratky, předvolby nástrojů, HDR prostředí, MatCapy, alfy, textury štětců a referenční obrázky. Vše, co se ukládá s projektem, například osvětlení, postproces nebo pohledy kamery, také zůstane beze změny.
