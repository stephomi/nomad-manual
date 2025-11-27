# ![](/icons/cog.webp) Nastavení 

Nabídka nastavení obsahuje mnoho možností pro ovládání vzhledu a chování aplikace Nomad.

![](/images/settings_overview.webp)

## Zobrazení
Tato sekce obsahuje rychlé zkratky pro většinu nastavení níže v této nabídce.

![](/images/settings_display_settings.webp)

### Hladké stínování 
Přepíná mezi hladkým a fasetovým stínováním. Při fasetovém stínování jsou polygony stínovány nezávisle, takže je vidět podkladová topologie.
Během fáze sochání může být užitečné vidět fasetové stínování a poté přepnout na hladké stínování pro renderování.

Vypnutí hladkého stínování mírně zlepšuje výkon.

### Obrys
Přepíná obrys aktuálního výběru.

To je užitečné pro vizuální zpětnou vazbu na aktuálně vybranou síť(e) v případě, že je [Ztmavit nevybrané](#darken-unselected-objects) vypnuto.

Z hlediska výkonu je použití [Ztmavit nevybrané](#darken-unselected-objects) mnohem lepší než použití obrysového řešení.

### Mřížka
Přepíná zobrazení pozadí s mřížkou, užitečné pro pochopení umístění objektů a měřítka.

### Oboustranné
Přepíná zobrazení polygonů z obou stran. Všechny plochy směřují určitým směrem.
Plochy považované za *zadní stranu* jsou ty, které směřují „od“ pohledu kamery.

Například výchozí jednoduchá koule bude mít plochy orientované směrem ven.
Pokud přesunete kameru dovnitř koule, uvidíte zadní stranu těchto ploch.

Většinu času byste zadní stranu ploch vidět neměli, takže jejich obarvení může pomoci odhalit potenciální problémy nebo nesprávnou topologii.

Vypnutí vykreslování `oboustranné` může mírně zlepšit výkon.

### Drátěný model
Přepíná překryvný drátěný model. 

Zapnutí drátěného modelu snižuje výkon.

### Přichytávací kostka
Přepíná pomocnou ikonu v rohu scény, užitečnou pro orientaci v prostoru a rychlé přepínání mezi pohledy zepředu/zezadu/zleva/zprava/zhora/zdola.

### Zobrazit malbu
Přepíná zobrazení malby. Výchozí materiál je bílý nemetalický s drsností 25 %.

### Použít skrývání
Přepíná režim skrývání. Když je vypnutý, stále existuje, jen je deaktivovaný. Toto tlačítko je vypnuté, pokud právě používáte nástroj skrývání.

### Zobrazit masku
Přepíná režim masky. Když je vypnutý, stále existuje, jen je deaktivovaný. Stisknutím tohoto tlačítka jej znovu aktivujete.

Pokud potřebujete masku skrýt A přesto ji mít aktivní, použijte barvu masky níže a nastavte ji na bílou. Nezapomeňte ji po dokončení vrátit na šedou!

Poznámka: toto tlačítko je vypnuté, pokud právě používáte nástroj masky. 

### Maska -> Neprůhledná
Maska -> neprůhledná bude ignorovat průhledné vrcholy pro maskovanou masku. Týká se to pouze průhlednosti vrcholů a textur; plochy skryté pomocí „skrýt“ zůstanou skryté.

### Zvýraznění
Přepíná záblesk zvýraznění výběru. Při výběru objektů dočasně na 500 milisekund problikne vybraný objekt sytě růžovou. Barvu a délku záblesku lze upravit níže.

### Statistiky
Přepíná zobrazení stavového textu ve 3D zobrazení. Zobrazuje informace o paměti systému, celkovém počtu vrcholů ve scéně a počtu vrcholů aktuálního výběru.

----- 

### Ztmavit nevybrané objekty
Objekty, které nejsou vybrané, budou ztmaveny, aby aktuální výběr více vynikl.

### Maska
Barva použitá pro maskování, ve výchozím nastavení středně šedá, násobená barvou objektu. Nastavte na bílou, aby byla maska neviditelná, ale po dokončení ji nezapomeňte vrátit na šedou!

## ![](/icons/cursor.webp) Kurzor

### Zobrazit kruh při sochání
Pokračovat v zobrazování poloměru štětce při sochání.

### Zobrazit malou tečku
Zobrazit tečku ve středu tahu štětce při sochání nebo když je změněn střed otáčení kamery.

### Zobrazit stabilizátor „lano“
Kreslit čáru označující délku „lana“, když je v nastavení tahu aktivní stabilizátor lazy rope.

## ![](/icons/cursor.webp) Indikátor
![](/images/settings_indicator.webp)

Zobrazuje vizuální indikátor(y) pro tutoriály a záznam obrazovky.

Tlačítka `Prst`, `Stylus` a `Myš` povolí zobrazení ikony, když je detekován daný typ vstupu.

### Barva
Barva indikátoru.

### Velikost/Ikona/Kruh
Ovládací prvky pro úpravu velikosti indikátoru a tvarů uvnitř indikátoru.

## ![](/icons/wireframe.webp) Drátěný model
![](/images/settings_wireframe.webp)
Aktivuje překryvný drátěný model.

### Cíl
Nastavuje, zda se drátěný model zobrazí u nevybraných objektů, pouze u vybraných objektů, nebo u všech objektů.

### Skrýt
Nastavuje, zda se drátěný model bude zobrazovat i pro skryté polygony.

### Multirezoluce: pouze úroveň 0
Multirezoluce zobrazí drátěné modely pro úroveň 0 tmavší a vyšší úrovně postupně světlejší. Když je tato volba zapnutá, zobrazí se pouze drátěný model úrovně 0.

### Barva
Nastaví barvu a průhlednost drátěného modelu.

## ![](/icons/grid.webp) Mřížka
![](/images/settings_grid.webp)
Aktivuje mřížku.

### Barva
Nastaví barvu a průhlednost mřížky.

### Přichytávání
Povolí přichytávání nástrojů založených na křivkách k mřížce.

## ![](/icons/culling.webp)Oboustranné
Povolí zobrazení polygonových ploch z obou stran.

### Barvit zadní stranu, Barva zadní strany
Povolí tónování zadních stran a nastaví barvu tónování.

## ![](/icons/outline.webp)Obrys
Povolí obrys kolem aktivního objektu.

### Barva obrysu, Tloušťka
Nastaví barvu a tloušťku obrysu.

## ![](/icons/bang.webp) Zvýraznění
Povolí krátký záblesk při změně aktivního objektu.
### Barva, Doba trvání
Nastaví barvu a délku záblesku v milisekundách.

## ![](/icons/snap_cube.webp) Přichytávací kostka
![](/images/settings_snapcube.webp)

Zobrazuje pomocnou ikonu v rohu scény, užitečnou pro rychlé přepínání mezi pohledy zepředu/zezadu/zleva/zprava/zhora/zdola. Klepnutím na strany kostky přepnete mezi ortografickými pohledy.

### Tvar
Vyberte mezi tvarem kostky, koule nebo gnomonu pro přichytávací kostku.

### Omezit zarovnání
Povolí uzamčení rotace kamery při tažení na přichytávací kostce. Když je aktivní, pohyb tažením na kostce bude pouze doleva/doprava nebo nahoru/dolů.

### Velikost
Nastaví velikost přichytávací kostky.

### Otočit o 180°
Povolí chování při klepnutí tak, že pokud je pohled přichycen, klepnutí na střed kostky otočí pohled o 180 stupňů. Například pokud je pohled přichycen na předek, klepnutí na kostku otočí pohled na zadní stranu.

### Pozice
Nastaví, v kterém rohu bude přichytávací kostka.

## ![](/icons/edit_radius_n.webp) Statistiky
![](/images/settings_stats.webp)

Zobrazuje informace o paměti systému, celkovém počtu vrcholů ve scéně a počtu vrcholů aktuálního výběru.

### Pozice
Nastaví, v kterém rohu budou statistiky.

## Primtive/Repeaters
## Číselný vstup
Povolí číselný vstup při klepnutí na widgety gizma.

## Multirezoluce
### Max. počet vrcholů
Nastaví práh, nad který nebude povolena operace dělení multirezoluce, protože by pravděpodobně způsobila pád aplikace Nomad. Výchozí hodnota je 10 milionů.
### Prah nízkého rozlišení
Při pohybu kamerou může být zobrazeno nižší rozlišení sítě. Tuto hodnotu můžete zvýšit, pokud chcete zobrazovat vyšší rozlišení sítě.

## Nastavení
### Obnovit výchozí
Obnoví všechna nastavení na výchozí hodnoty.
