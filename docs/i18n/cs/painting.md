# ![](/icons/paint.webp) Barva {#painting}

Nastavuje barvu, drsnost a kovovost malířských tahů, umožňuje vyplnit celý objekt vlastnostmi malby a určuje, jak malířské nástroje pracují s vrstvami, maskami a skrytými oblastmi.

![](/images/paint_overview.webp)  

## Přehled {#overview}

Nomad používá PBR malování do vrcholů. Co to znamená?

### PBR {#pbr}
PBR (Physically Based Rendering, fyzikálně založené vykreslování) je oblíbená technika počítačové grafiky ve filmu, televizi, hrách i na mobilních zařízeních. Díky osvětlení vycházejícímu z fyzikálních vlastností a popisu povrchů pomocí barvy, drsnosti a kovovosti lze dosáhnout široké škály fotorealistických vzhledů.

### Malování do vrcholů {#vertex-painting}

Malování do vrcholů znamená, že se informace o malbě ukládají do vrcholů modelu, a ne do textur. Protože Nomad zvládá modely se stovkami tisíc, často i miliony vrcholů, můžete mít na modelech velmi detailní malbu: co dokážete vymodelovat, to dokážete i namalovat.

Znamená to také, že malování v Nomadu nevyžaduje UV mapování, které je v jiných 3d aplikacích často pomalé a technické. Mnoho jiných 3d aplikací tak vysoké počty vrcholů jako Nomad nezvládá, Nomad ale nabízí i dobré nástroje pro pečení textur a decimaci, které pomohou.

### Texturování {#texturing}

Nomad textury podporuje, ale musí být součástí importovaného modelu, nebo vzniknout vypečením malby z vrcholů do textur. 

Textura je prostě obrázek, ve 3d ale obvykle znamená obrázek přiřazený k objektu.
Aby se obrázek mohl obtočit kolem modelu, potřebuje model texturové souřadnice (UV).

Nomad je umí vypočítat [automaticky](topology.md#uv-unwrap), ale nad celkovou kvalitou nemáte velkou kontrolu.

::: tip
Příklad pracovního postupu:
- Vymodelujte model v Nomadu a pak udělejte [UV rozbalení](topology.md#uv-unwrap)
- Pokud jste už v Nomadu začali malovat, můžete [přenést malbu z vrcholů do textur](topology.md#bake-texture)
- Exportujte do Procreate
- Texturujte v Procreate
- Exportujte zpět do Nomadu kvůli renderování
:::

To byl přehled, teď si projděme jednotlivé části nabídky malování:


## Tahové malování {#stroke-painting}
![](/images/paint_intensity.webp)  

Zapne malování pro tento nástroj, což se hodí, když potřebujete modelovat a malovat zároveň. Když nástroj malovat umí, ale toto políčko je vypnuté, připomene vám to ikona upozornění vedle nadpisu.

U nástrojů, jejichž hlavní funkcí je malování (např. Malovat, Rozmazat, Maska), toto políčko není.

### ![](/icons/opacity.webp) Intenzita malby {#paint-intensity}

Posuvník, se kterým můžete pro malbu použít jinou intenzitu, než je hlavní intenzita nástroje.

Tlačítko s posuvníky vedle něj přidá na boční panel rychlý posuvník intenzity malby, pro nástroje, které modelují a malují zároveň.

Tlačítka `Alfa`, `Útlum` a `Náhodně měnit intenzitu` určují, jestli tyto funkce ovlivní malbu. Můžete mít například u nástroje hlína zapnuté náhodné změny, ale barva se náhodně měnit nebude.

* `Alfa` - když je vypnutá, malba alfu ignoruje a pokryje celou plochu štětce. U nástroje VDM tlačítko nahrazuje `Materiál razítka`, které zapíná nebo vypíná materiál uložený v razítku.
* `Útlum` - když je vypnutý, malba zůstává v plné intenzitě až k okraji štětce.
* `Náhodně měnit intenzitu` - jestli náhodné změny intenzity v tahu ovlivňují malbu. Náhodná poloha, rotace a měřítko vždy posouvají celé razítko.

[Malovat vše](#paint-all) tyto možnosti ignoruje, ale jeho triplanární varianta alfu používá.

### ![](/icons/link.webp) Globální materiál {#global-material}
Když je tato možnost zapnutá, vybraný materiál bude stejný jako u ostatních nástrojů. Bere v úvahu jen nastavení drsnosti, kovovosti a barvy. Vypněte ji, chcete-li dát tomuto nástroji vlastní materiál.


## Materiál {#material}
![](/images/paint_material.webp) 

První ikona je tvar s náhledem materiálu. Tažením po 3d náhledu materiálu ho otáčíte. 

Druhá ikona je náhled malířského tahu s vybranou alfou a útlumem.

### ![](/icons/falloff.webp) Křivky {#curves}

Otevře editor křivek pro texturové sloty [posuvníků PBR](#pbr-sliders). Přemapuje hodnoty textury předtím, než se namalují, aniž by se změnil soubor obrázku. Malá ikona křivky na texturovém slotu ukazuje, že jeho křivka byla upravena.

### ![](/icons/cog.webp) Možnosti materiálu {#material-options}

Tlačítko `Materiál` vedle nadpisu obsahuje dvě nastavení.

`Náhled materiálu ve viewportu` určuje, co se stane na vybraném objektu, když měníte posuvníky barvy, drsnosti, kovovosti, krytí a intenzity:

* `Žádný` - Při úpravě vlastností se na modelu žádný náhled nezobrazí
* `Materiál` - Při úpravě vlastností se hodnoty materiálu zobrazí v náhledu na objektu.
* `Triplanar` - Materiál se zobrazí v náhledu jako triplanární projekce. 

Políčka barvy, drsnosti, kovovosti a krytí pod tím určují, které kanály nahradí [Kapátko materiálu](#material-picker).

### ![](/icons/dropper.webp) Kapátko materiálu {#material-picker}

Kapátko nabere materiál pod kurzorem z jakéhokoli objektu ve scéně. Nahradí se jen kanály zaškrtnuté v [Možnostech materiálu](#material-options).

## Předvolby materiálů {#material-presets}
Klepnutím na tvar s 3d náhledem otevřete nabídku předvoleb materiálů; můžete je klonovat a vytvářet si vlastní předvolby.

![](/images/paint_presets.webp) 

Přepínač `Vložit textury` uloží do předvolby kopii textur, které materiál používá. Bez něj předvolba na textury ve složce textures/ Nomadu jen odkazuje. Zapněte ho, když chcete sdílet předvolbu s texturami, aniž byste textury posílali zvlášť.

`Zahrnout alfu` uloží do předvolby materiálu i alfu štětce.

## Posuvníky PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr) malování používá 4 kanály:
- `Barva` Barva, kterou budete malovat. Kapátkem můžete nabrat barvu z jiných částí modelu nebo z referenčních obrázků.
- `Drsnost` Určuje, jak „drsný“ nebo „hladký“ je povrch. Nízká hodnota drsnosti znamená ostré odrazy.
- `Kovovost` Prostě říká, jestli je povrch kovový, nebo ne. Hodnota by měla být většinou buď 0 %, nebo 100 %, hodnoty mezi tím by měly být výjimečné.
- `Krytí` Jak moc je materiál průhledný. Přísně vzato nepatří do specifikace PBR, ale hodí se v mnoha situacích. 1 je zcela neprůhledné, 0 průhledné. Krytí a lom světla jsou různé věci: lom se v Nomadu řeší materiálem s refrakcí. 

Když vyberete předvolbu materiálu, malují se 3 kanály současně (krytí bývá záměrně vynechané). Místo pouhé „červené“ tak můžete malovat „červený drsný kov“ nebo „bílý hladký plast“.

Čtvereček je texturový slot: klepnutím na něj použijete pro danou vlastnost texturu místo pevné hodnoty. Barevná textura barvu tónuje, zatímco textura drsnosti, kovovosti nebo krytí hodnotu posuvníku nahradí (jeho popisek je pak přeškrtnutý). U textury krytí `Použít alfu jako hodnotu` čte alfa kanál textury místo její hodnoty ve stupních šedi.

U nástroje VDM, když razítko nese vlastní materiál, se vedle texturového slotu ukáže další slot s ním. Klepnutím na něj daný kanál razítka použijete, nebo ignorujete.

Ikona štětce vedle posuvníků vyplní danou vlastností celý objekt.

Zaškrtávací políčko danou vlastnost zapne nebo vypne, takže můžete například malovat jen barvu, nebo jen drsnost a krytí. 

Tady je několik příkladů různých hodnot drsnosti a kovovosti:

|                | Kovovost 0 %                      | Kovovost 100 %               |
| :------------: | :-------------------------------: | :--------------------------: |
| Drsnost 0 %    | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Drsnost 50 %   | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Drsnost 100 %  | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Drsnost a kovovost vyžadují režim stínování [Osvětlené (PBR)](shading.md#pbr). V režimu [MatCap](shading.md#matcap) nebo [Neosvětlené](shading.md#unlit) se ignorují a nabídka zobrazí upozornění.
:::

::: tip
Když pro PBR malování používáte textury, často se vyplatí přepnout na nástroj jako `Razítko`, nebo v nabídce tahu použít jiný režim než bod, který může texturu rozmazávat.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Pokud malujete kovový povrch na objekt s nižším počtem polygonů, zvažte zapnutí `Hladké odstíny` [globálně](settings.md#smooth-shading) nebo [pro jednotlivý objekt](material.md#smooth-shading).
:::

## ![](/icons/paint.webp) Malovat vše {#paint-all}

![](/images/paint_paint_all.webp)

Použije aktuální materiál na vybrané objekty, buď ve standardním režimu tlačítkem `Malovat vše`, nebo jako triplanární projekci tlačítkem `Malovat vše + Triplanar`. Triplanární varianta není dostupná u primitiv, která ještě nebyla potvrzena.

Políčka vedle posuvníků barvy/kovovosti/drsnosti/krytí se respektují: vypnuté vlastnosti se nevyplní.

Další tlačítka určují, co dalšího ovlivní vyplnění. Většina ukazuje procento a jsou zašedlá, když by neměla žádný účinek:

| Ikona                       | Popis                                         |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Maskované oblasti nebudou ovlivněny.          |
| ![](/icons/tool_hide.webp) | Skryté oblasti nebudou ovlivněny.             |
| ![](/icons/opacity.webp)   | Použije faktor malby nástroje nastavený výše. |
| ![](/icons/layer.webp)     | Nenamalované oblasti vrstvy nebudou ovlivněny. |
| ![](/icons/triplanar.webp) | `Vrchol`: triplanární varianta také posune povrch podle alfy, o zobrazenou intenzitu nástroje. |
| ![](/icons/cog.webp)       | Otevře nastavení triplanární projekce         |

### ![](/icons/cog.webp) Nastavení triplanární projekce {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Podobně jako v [nastavení triplanární projekce v nabídce materiálu](material.md#triplanar) můžete ovládat prolnutí projekcí, opakování (dlaždice) a posuny. 

Zaškrtávacím políčkem náhledu nahoře v této nabídce zapnete trvalý náhled, zatímco upravujete hodnoty.
