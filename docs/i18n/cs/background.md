# ![](/icons/image.webp) Pozadí {#background}

Toto menu ovládá barvu pozadí v Nomadu a také referenční obrázky, které chcete použít.

![](/images/background_overview.webp)

## Typ {#type}
![](/images/background_selector.webp)

Pro pozadí výřezu jsou na výběr tři možnosti.

* `Prostředí` - Zobrazí mapu prostředí zvolenou v menu [Stínování](shading.md). Dál ji můžete upravit posuvníky `Rozmazání` a `Expozice` (jas). 
* `Barva` - Jednolitá barva podle vašeho výběru
* `Přechod` - Plynulý přechod mezi dvěma barvami. Posuvníkem `Faktor` posunete střed přechodu.  

### Typ přechodu {#gradient-type}
U volby `Přechod` vyberte jeho tvar:
* `Lineární` - Rovný přechod, jeho směr určuje posuvník `Úhel`.
* `Radiální` - Kruhový přechod vycházející ze středu obrazovky.
* `Obloha` - Přechod ukotvený k horizontu světa, takže se mění s kamerou, když se díváte nahoru a dolů.

Každá barva má tlačítko pro reset a kapátko, kterým můžete nabrat barvu z obrazovky.

## ![](/icons/lock.webp) Synchronizovat s uzamčením kamery {#sync-on-camera-lock}
Když je kamera uzamčená pomocí [Orientační kostky](settings.md#snap-cube), referenční obrázek sleduje pohyb kamery, takže zůstává zarovnaný s vaší sochou.

* `Povolit náklon (trackball)` - Povolí náklon kamery, když opustíte uzamčení kamery.
* `Resetovat zobrazení při odemknutí` - Při opuštění uzamčení kamery se pohled vrátí do výchozího stavu.

## Referenční obrázek {#reference}

![](/images/background_reference.webp)

Do pozadí můžete přidat libovolný obrázek, podle kterého budete modelovat. Klepněte na `Importovat...` a obrázek přidejte, pak zaškrtněte `Referenční obrázek`, aby se zobrazil.
Můžete měnit jeho polohu a měřítko, třeba když ho chcete přesunout do rohu obrazovky.

### ![](/icons/tool_transform.webp) Transformace {#transform}

Tímto tlačítkem umístíte referenční obrázek interaktivně. Dvěma prsty obrázek posouvejte, zvětšujte a otáčejte, dokud nesedí. `Resetovat nastavení` vrátí obrázek do výchozí polohy. Výsledné umístění se promítne do posuvníků níže:

* `Překrytí` - Při 0 % je referenční obrázek vždy za vašimi objekty, při 100 % je před nimi. 
* `Krytí` - Jak moc je obrázek průhledný.
* `Postproces` - Použije na referenční obrázek efekty postprocesu. Vypněte ho, pokud chcete zachovat původní barvy.
* `Pozice X` / `Pozice Y` - Poloha obrázku v ose X a Y.
* `Měřítko` - Měřítko obrázku.
* `Rotace` - Natočení obrázku.


::: tip

Kamery a referenční obrázky jsou propojené. 

Když si tedy referenční obrázek zarovnáte se sochou a pak v [menu Kamera](camera.md) vytvoříte kameru, uloží se s ní i poloha, natočení a měřítko referenčního obrázku. Referenční obrázek pak můžete vypnout a otočit se do jiného pohledu. Jakmile se znovu podíváte skrz kameru, referenční obrázek se zapne s nastavením, které jste použili.

Každá kamera může mít dokonce i jiný obrázek!

 ![](/videos/reference_camera.mp4)

:::
