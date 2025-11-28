# ![](/icons/paint.webp) Malování {#painting}

Ovládejte barvu, drsnost, kovovost malovaných tahů, umožněte hromadné vyplňování malovacích atributů a určete, jak malovací nástroje interagují s vrstvami, maskami a skrytými výběry.

![](/images/paint_overview.webp)  

## Přehled {#overview}

Nomad používá PBR malování vrcholů. Co to znamená?

### PBR {#pbr}
PBR, neboli fyzikálně založené vykreslování (Physically Based Rendering), je populární technika počítačové grafiky pro film, televizi, hry a mobilní zařízení. Tím, že jsou světla založena na fyzikálních vlastnostech a povrchy jsou definovány pomocí barvy, drsnosti a kovovosti, lze dosáhnout široké škály fotorealistických vzhledů.

### Malování vrcholů {#vertex-painting}

Malování vrcholů znamená, že informace o barvě jsou uloženy ve vrcholech modelu, nikoli v texturách. Protože Nomad zvládá modely se stovkami tisíc, často miliony vrcholů, měly by vaše modely být schopné mít velmi detailní povrchové malování; pokud můžete detail vymodelovat, můžete ho také namalovat.

To také znamená, že malování v Nomadu nevyžaduje UV mapování, což je v jiných 3D aplikacích často pomalý a technický proces. Mnoho jiných 3D aplikací nepodporuje tak vysoký počet vrcholů jako Nomad, nicméně Nomad má také dobré nástroje pro pečení textur a decimaci.

### Texturování {#texturing}

Nomad podporuje textury, ale ty musí být přítomné v importovaném modelu, nebo vzniknout pečením malby vrcholů do textur. 

Textura je jednoduše obrázek, ale v 3D kontextu obvykle označuje obrázek přiřazený k objektu.
Aby bylo možné obrázek „omotat“ kolem modelu, model potřebuje texturovací souřadnice (UV).

Nomad je umí [spočítat automaticky](topology.md#uv-unwrap), ale nemáte velkou kontrolu nad celkovou kvalitou.

::: tip
Příklad pracovního postupu:
- Modelujte v Nomadu, poté proveďte [UV rozbalení](topology.md#uv-unwrap)
- Pokud jste už začali malovat v Nomadu, můžete [přenést malbu vrcholů do textur](topology.md#bake-vertex-colors-to-texture)
- Exportujte do Procreate
- Texturujte v Procreate
- Exportujte zpět do Nomadu pro účely renderování
:::

To byl přehled, nyní si projdeme jednotlivé části malovacího menu:


## Malování tahem {#stroke-painting}
![](/images/paint_intensity.webp)  

Povolí malování pro tento nástroj, užitečné, pokud potřebujete současně modelovat a malovat.

U nástrojů, kde je malování primární funkcí (např. Paint, Smudge, Mask), toto zaškrtávací políčko neexistuje.

### Intenzita malby {#paint-intensity}

Posuvník, který vám umožní použít jinou intenzitu než primární intenzitu nástroje.

Zaškrtávací políčka `Alpha`, `Falloff` a `Randomize` určují, zda tyto funkce ovlivní malování. Například můžete mít u nástroje Clay zapnuté náhodnění, ale barva se náhodně měnit nebude.


## Materiál {#material}
![](/images/paint_material.webp) 

První ikona je náhledový tvar materiálu. Tažením na 3D náhledu materiálu jej otočíte. 

Druhá ikona je náhled malovacího tahu se zvolenou alfou a průběhem (falloff).

Tlačítko náhledu vedle názvu Material vám umožní přepínat mezi None, Material nebo Triplanar. To určuje, co se stane, když interaktivně měníte vlastnosti malby:

* `None` – Při úpravě vlastností se na modelu nezobrazí žádný náhled
* `Material` – Hodnoty materiálu se budou při úpravě vlastností náhledově zobrazovat na objektu. Pokud používáte textury a model má UV, použijí se UV souřadnice.
* `Triplanar` – Materiál se bude náhledově promítat jako triplanární projekce. 

Kapátko lze použít k nasamplování všech vlastností z objektu ve scéně.

## Předvolby materiálu {#material-presets}
Klepnutím na 3D náhledový tvar se otevře menu předvoleb materiálů, které lze klonovat a definovat tak vlastní předvolby.

![](/images/paint_presets.webp) 

Přepínače `Embed Textures` a `Alpha`, pokud jsou zapnuté, uloží všechny textury použité tímto materiálem přímo do předvolby. To je níže vysvětleno podrobněji.

## Posuvníky PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr) malování používá 4 kanály:
- `Color` Barva, která bude malována. Kapátko lze použít k výběru barvy z jiných částí modelu nebo z referenčních obrázků.
- `Roughness` Udává, jak je povrch „drsný“ nebo „hladký“. Nízká hodnota drsnosti znamená, že odlesky budou ostré.
- `Metalness` Udává, zda je povrch kovový nebo ne. Hodnota by měla být většinu času buď 0 % nebo 100 %, mezilehlé hodnoty by měly být výjimečné.
- `Opacity` Jak moc je materiál průhledný. Přísně vzato není součástí PBR specifikace, ale v mnoha situacích je užitečná. 1 je zcela neprůhledné, 0 je průhledné. Všimněte si, že neprůhlednost a refrakce jsou odlišné věci, refrakce je v Nomadu řešena pomocí refrakčního materiálu. 

Pokud zvolíte předvolbu materiálu, malují se současně 3 kanály (opacity je často záměrně vynechána). To znamená, že místo pouhého malování „červené“ můžete malovat „červený drsný kov“ nebo „bílý hladký plast“.

Čtverec je slot pro texturu, kliknutím na něj použijete pro danou vlastnost texturu místo pevné hodnoty.

Ikona štětce vedle posuvníků zaplní (flood fill) danou vlastnost po celém objektu.

Zaškrtávací políčko povolí nebo zakáže danou vlastnost, takže můžete například malovat pouze barvu, nebo pouze drsnost a neprůhlednost. 

Zde jsou příklady různých hodnot drsnosti a kovovosti:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
V režimu [Matcap renderingu](shading.md#matcap) je podporována pouze barva, kovovost a drsnost jsou ignorovány.
:::

::: tip
Při použití textur pro PBR malování je často užitečné přepnout na nástroj jako `Stamp`, nebo v menu Stroke použít jiný režim než Dot, který může texturu rozmazávat.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Pokud malujete kovový povrch na objektu s nižším počtem polygonů, můžete zvážit zapnutí `Smooth Shading` [globálně](settings.md#smooth-shading) nebo [pro konkrétní objekt](material.md#smooth-shading).
:::

## Malovat vše {#paint-all}

![](/images/paint_paint_all.webp)

Aplikuje aktuální materiál na objekt, buď ve standardním režimu pomocí „Paint All“, nebo jako triplanární projekci.

Zaškrtávací políčka vedle posuvníků color/metalness/roughness/opacity jsou respektována, jakékoli vypnuté vlastnosti nebudou vyplněny.

Další tlačítka určují, jak může být Paint All dále ovlivněno:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Maskované oblasti nebudou ovlivněny.          |
| ![](/icons/tool_hide.webp) | Skryté oblasti nebudou ovlivněny.             |
| ![](/icons/opacity.webp)   | Použít výše uvedený faktor malování nástroje. |
| ![](/icons/layer.webp)     | Nenamalované oblasti vrstvy nebudou ovlivněny.|
| ![](/icons/triplanar.webp) | Indikátor triplanárního nastavení             |
| ![](/icons/cog.webp)       | Otevřít nastavení Triplanar                   |

### Nastavení triplanárního zobrazení {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Podobně jako [triplanární nastavení v menu materiálu](material.md#triplanar) můžete ovládat prolínání projekcí, dlaždicování a posuny. 

Pomocí zaškrtávacího políčka Preview v horní části tohoto menu můžete při úpravě hodnot zapnout trvalý náhled.

## Globální materiál {#global-material}
Pokud je tato možnost zapnutá, vybraný materiál bude stejný jako u ostatních nástrojů. Všimněte si, že se bere v úvahu pouze nastavení drsnosti, kovovosti a barvy.