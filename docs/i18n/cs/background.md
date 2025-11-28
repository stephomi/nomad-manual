# ![](/icons/image.webp) Pozadí {#background}

Tato nabídka ovládá barvu pozadí Nomadu a také referenční obrázky, které se mají použít.

![](/images/background_overview.webp)

## Pozadí {#type}
![](/images/background_selector.webp)

Pro pozadí zobrazení jsou k dispozici tři možnosti.

* `Environment` – Zobrazí environment mapu vybranou v [Shading](shading). Tu lze dále ovládat pomocí rozostření (Blur) a ovladačů expozice (Exposure, jas).
* `Color` – Jednolitá barva, kterou si můžete zvolit.
* `Gradient` – Přechod barvy shora dolů. Posuvník Factor vám umožní určit střed přechodu.

## Referenční obrázek {#reference}

![](/images/background_reference.webp)

Na pozadí můžete přidat libovolný obrázek, který bude sloužit jako reference.
Můžete měnit jeho pozici a měřítko, například pokud jej chcete přesunout do rohu obrazovky.

### ![](/icons/tool_transform.webp) Transformace {#transform}

Toto tlačítko vám umožní umístit referenční obrázek interaktivně. Použijte 2 prsty pro posun, změnu měřítka a rotaci referenčního obrázku na místo. Konečné umístění se projeví v posuvnících níže:

* `Overlay` – při 0 % bude referenční obrázek vždy za vašimi objekty, při 100 % je před nimi.
* `Opacity` – Jak průhledný obrázek je.
* `Position` – Pozice obrázku v ose X a Y.
* `Rotation` – Rotace obrázku.
* `Scale` – Měřítko obrázku.


::: tip

Kamery a referenční obrázky jsou propojené.

To znamená, že pokud si nastavíte referenční obrázek tak, aby lícoval s vaším modelem, a vytvoříte kameru z [Camera menu](camera), pozice, rotace a měřítko referenčního obrázku se uloží spolu s kamerou. Můžete referenční obrázek vypnout, otočit se do jiného pohledu. Pokud se znovu podíváte skrz kameru, referenční obrázek se aktivuje s nastavením, které jste použili.

To dokonce zahrnuje i volbu různých obrázků pro různé kamery!

 ![](/videos/reference_camera.mp4)

:::