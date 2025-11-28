# ![](/icons/cog.webp) Nastavení {#reset-to-default}

Nabídka nastavení obsahuje mnoho možností pro ovládání vzhledu a chování aplikace Nomad.

![](/images/settings_overview.webp)

## Nastavení zobrazení {#display-settings}
Tato sekce obsahuje rychlé zkratky pro většinu nastavení níže v této nabídce.

![](/images/settings_display_settings.webp)

### Hladké stínování {#smooth-shading}
Přepíná mezi hladkým a fasetovým stínováním. Při fasetovém stínování jsou polygony stínovány nezávisle, takže je vidět podkladová topologie.
Během fáze sochání může být užitečné vidět fasetové stínování a poté přepnout na hladké stínování pro renderování.

Vypnutí hladkého stínování mírně zlepšuje výkon.

### Obrys {#outline-quick}
Přepíná obrys aktuálního výběru.

To je užitečné pro vizuální zpětnou vazbu na aktuálně vybranou síť(e) v případě, že je [Ztmavit nevybrané](#darken-unselected-objects) vypnuto.

Z hlediska výkonu je použití [Ztmavit nevybrané](#darken-unselected-objects) mnohem lepší než použití obrysového řešení.

### Mřížka {#grid-quick}
Přepíná zobrazení pozadí s mřížkou, užitečné pro pochopení umístění objektů a měřítka.

### Oboustranné {#two-sided-quick}
Přepíná zobrazení polygonů z obou stran. Všechny plochy směřují určitým směrem.
Plochy považované za *zadní stranu* jsou ty, které směřují „od“ pohledu kamery.

Například výchozí jednoduchá koule bude mít plochy orientované směrem ven.
Pokud přesunete kameru dovnitř koule, uvidíte zadní stranu těchto ploch.

Většinu času byste zadní stranu ploch vidět neměli, takže jejich obarvení může pomoci odhalit potenciální problémy nebo nesprávnou topologii.

Vypnutí vykreslování `oboustranné` může mírně zlepšit výkon.

### Drátový model {#wireframe-quick}
Přepíná překryvný drátěný model. 

Zapnutí drátěného modelu snižuje výkon.

### Krychle pro přichycení {#snap-cube-quick}
Přepíná pomocnou ikonu v rohu scény, užitečnou pro orientaci v prostoru a rychlé přepínání mezi pohledy zepředu/zezadu/zleva/zprava/zhora/zdola.

### Zobrazit malbu {#show-painting}
Přepíná zobrazení malby. Výchozí materiál je bílý nemetalický s drsností 25 %.

### Použít skrývání {#use-hide}
Přepíná režim skrývání. Když je vypnutý, stále existuje, jen je deaktivovaný. Toto tlačítko je vypnuté, pokud právě používáte nástroj skrývání.

### Zobrazit masku {#show-mask}
Přepíná režim masky. Když je vypnutý, stále existuje, jen je deaktivovaný. Stisknutím tohoto tlačítka jej znovu aktivujete.

Pokud potřebujete masku skrýt A přesto ji mít aktivní, použijte barvu masky níže a nastavte ji na bílou. Nezapomeňte ji po dokončení vrátit na šedou!

Poznámka: toto tlačítko je vypnuté, pokud právě používáte nástroj masky. 

### Maska -> Neprůhledná {#mask-opaque}
Maska -> neprůhledná bude ignorovat průhledné vrcholy pro maskovanou masku. Týká se to pouze průhlednosti vrcholů a textur; plochy skryté pomocí „skrýt“ zůstanou skryté.

### Zvýraznění {#highlight-quick}
Přepíná záblesk zvýraznění výběru. Při výběru objektů dočasně na 500 milisekund problikne vybraný objekt sytě růžovou. Barvu a délku záblesku lze upravit níže.

### Statistiky {#stats-quick}
Přepíná zobrazení stavového textu ve 3D zobrazení. Zobrazuje informace o paměti systému, celkovém počtu vrcholů ve scéně a počtu vrcholů aktuálního výběru.

----- 

### Ztmavit nevybrané objekty {#darken-unselected-objects}
Objekty, které nejsou vybrané, budou ztmaveny, aby aktuální výběr více vynikl.

### Maska {#mask}
Barva použitá pro maskování, ve výchozím nastavení středně šedá, násobená barvou objektu. Nastavte na bílou, aby byla maska neviditelná, ale po dokončení ji nezapomeňte vrátit na šedou!

## ![](/icons/cursor.webp) Kurzor {#cursor}

### Zobrazit kruh při sochání {#show-circle-while-sculpting}
Pokračovat v zobrazování poloměru štětce při sochání.

### Zobrazit malou tečku {#show-small-dot}
Zobrazit tečku ve středu tahu štětce při sochání nebo když je změněn střed otáčení kamery.

### Zobrazit stabilizátor (lano) {#show-rope-stabilizer}
Kreslit čáru označující délku „lana“, když je v nastavení tahu aktivní stabilizátor lazy rope.

## ![](/icons/cursor.webp) Ukazatel {#indicator}
![](/images/settings_indicator.webp)

Zobrazuje vizuální indikátor(y) pro tutoriály a záznam obrazovky.

Tlačítka `Prst`, `Stylus` a `Myš` povolí zobrazení ikony, když je detekován daný typ vstupu.

### Barva {#indicator-color}
Barva indikátoru.

### Velikost/Ikona/Kruh {#indicator-shape}
Ovládací prvky pro úpravu velikosti indikátoru a tvarů uvnitř indikátoru.

## ![](/icons/wireframe.webp) Drátový model {#wireframe}
![](/images/settings_wireframe.webp)
Aktivuje překryvný drátěný model.

### Cíl {#target}
Nastavuje, zda se drátěný model zobrazí u nevybraných objektů, pouze u vybraných objektů, nebo u všech objektů.

### Skrýt {#hide}
Nastavuje, zda se drátěný model bude zobrazovat i pro skryté polygony.

### Multirozlišení: pouze úroveň 0 {#multiresolution-level-0-only}
Multirezoluce zobrazí drátěné modely pro úroveň 0 tmavší a vyšší úrovně postupně světlejší. Když je tato volba zapnutá, zobrazí se pouze drátěný model úrovně 0.

### Barva {#wireframe-color}
Nastaví barvu a průhlednost drátěného modelu.

## ![](/icons/grid.webp) Mřížka {#grid}
![](/images/settings_grid.webp)
Aktivuje mřížku.

### Barva {#grid-color}
Nastaví barvu a průhlednost mřížky.

### Přichytávání {#snap}
Povolí přichytávání nástrojů založených na křivkách k mřížce.

## ![](/icons/culling.webp)Oboustranné {#two-sided}
Povolí zobrazení polygonových ploch z obou stran.

### Zbarvit zadní stranu, Barva zadní strany {#backface-color}
Povolí tónování zadních stran a nastaví barvu tónování.

## ![](/icons/outline.webp)Obrys {#outline}
Povolí obrys kolem aktivního objektu.

### Barva obrysu, Tloušťka {#outline-color-thickness}
Nastaví barvu a tloušťku obrysu.

## ![](/icons/bang.webp) Zvýraznění {#highlight}
Povolí krátký záblesk při změně aktivního objektu.
### Barva, Doba trvání {#color-duration}
Nastaví barvu a délku záblesku v milisekundách.

## ![](/icons/snap_cube.webp) Krychle pro přichycení {#snap-cube}
![](/images/settings_snapcube.webp)

Zobrazuje pomocnou ikonu v rohu scény, užitečnou pro rychlé přepínání mezi pohledy zepředu/zezadu/zleva/zprava/zhora/zdola. Klepnutím na strany kostky přepnete mezi ortografickými pohledy.

### Tvar {#shape}
Vyberte mezi tvarem kostky, koule nebo gnomonu pro přichytávací kostku.

### Omezit zarovnání {#restrict-alignment}
Povolí uzamčení rotace kamery při tažení na přichytávací kostce. Když je aktivní, pohyb tažením na kostce bude pouze doleva/doprava nebo nahoru/dolů.

### Velikost {#size}
Nastaví velikost přichytávací kostky.

### Otočit o 180 {#flip-180}
Povolí chování při klepnutí tak, že pokud je pohled přichycen, klepnutí na střed kostky otočí pohled o 180 stupňů. Například pokud je pohled přichycen na předek, klepnutí na kostku otočí pohled na zadní stranu.

### Pozice {#snap-position}
Nastaví, v kterém rohu bude přichytávací kostka.

## ![](/icons/edit_radius_n.webp) Statistiky {#stats}
![](/images/settings_stats.webp)

Zobrazuje informace o paměti systému, celkovém počtu vrcholů ve scéně a počtu vrcholů aktuálního výběru.

### Pozice {#stats-position}
Nastaví, v kterém rohu budou statistiky.

## Primitiva/Replikátory {#primitive-repeaters}
## Číselný vstup {#gizmo-input}
Povolí číselný vstup při klepnutí na widgety gizma.

## Multirozlišení {#multires}
### Maximální počet vrcholů {#multires-lowres-count}
Nastaví práh, nad který nebude povolena operace dělení multirezoluce, protože by pravděpodobně způsobila pád aplikace Nomad. Výchozí hodnota je 10 milionů.
### Práh nízkého rozlišení {#multires-lowres-threshold}
Při pohybu kamerou může být zobrazeno nižší rozlišení sítě. Tuto hodnotu můžete zvýšit, pokud chcete zobrazovat vyšší rozlišení sítě.

## Nastavení {#advanced}
### Obnovit výchozí {#reset}
Obnoví všechna nastavení na výchozí hodnoty.