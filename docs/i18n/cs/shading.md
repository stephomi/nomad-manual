# ![](/icons/sun.webp) Stínování {#shading}

Tato nabídka ovládá režimy stínování v Nomadu, vlastnosti osvětlení, prostředí a matcap a také mlhu.

![](/images/shading_overview.webp)



Můžete si vybrat z několika režimů vykreslování:

| Režim                       | Význam                     | Popis                                                           |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Osvětlené (PBR)](#pbr)     | Physically Based Rendering | Světla, stíny, prostředí a namalovaná kovovost/drsnost          |
| [MatCap](#matcap)           | Material Capture           | Rychlý režim pro sochání, s menší zátěží gpu/cpu než PBR        |
| [Neosvětlené](#unlit)       | Barva povrchu              | Jen barva povrchu, bez stínování a osvětlení                    |
| [ID objektu](#object-id)    | ID objektu                 | Náhodná barva pro každý objekt, užitečná pro malířské aplikace. |
| [ID instance](#instance-id) | ID instance                | Náhodná barva pro každou instanci, pomáhá rozpoznat sdílené sítě |

Pokud se chcete o kovovosti a drsnosti dozvědět víc, podívejte se do části [Malování vrcholů](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) SkupinaPovrch {#face-group}
Zobrazí barvy skupin ploch. Skupiny ploch jsou barevně odlišené výběry polygonů, které můžete vytvořit nástrojem [Skupina ploch](tools#facegroup) a které se automaticky vytvářejí u většiny primitiv.

Některé nástroje se při viditelných skupinách ploch automaticky omezují podle skupin ploch.

### ![](/icons/palette.webp) Zobrazit malbu {#show-paint}
Nomad umí ukládat barvu, drsnost a kovovost do vrcholů vaší sochy. Tímto zaškrtávacím políčkem zobrazení těchto vlastností globálně zapnete nebo vypnete.

Pokud máte vlastnosti vrcholů i textury a obojí je zapnuté, hodnoty se spolu vynásobí.

### ![](/icons/shield.webp) Zobrazit masku {#show-mask}
Zapne nebo vypne zobrazení masky ve stupních šedi z [nástrojů masky](tools#mask). Když je vypnuté, vypne se i samotná maska. Hodí se pro rychlé úpravy bez masky: pak ji znovu zapnete a o masku nepřijdete.

### ![](/icons/tool_hide.webp) Použít Skrytí {#use-hide}

Zapne nebo vypne skryté plochy. Funguje to jen tehdy, když NEJSTE v nástroji skrýt!

### ![](/icons/image.webp) Použít textury {#use-textures}

V Nomadu můžete objektům přiřadit textury v nabídce [materiál](material). Pokud jsou textury přiřazené, můžete je tímto zaškrtávacím políčkem globálně zapnout nebo vypnout.

Textury v Nomadu vytvářet ani upravovat nelze, textury z importovaných souborů ale fungují. Textury průhlednosti fungují v režimech Osvětlené, MatCap a Neosvětlené, normálové mapy v Osvětlené a MatCap, barva v Osvětlené a Neosvětlené a emisivita, drsnost a kovovost jen v Osvětlené. Když scéna nemá žádnou texturu, je tlačítko zašedlé.

### Přehled PBR a světel {#pbr}
Tato příručka nebude zacházet do podrobností o Physically Based Rendering.

Je dobré mít na paměti, že osvětlení a materiál jsou zcela oddělené.
Znamená to, že můžete objektu malovat barvu, drsnost a kovovost, zatímco osvětlení se řeší nezávisle.
Objekt tak můžete namalovat a osvětlení doladit později, aniž byste narušili celkový vzhled modelu.

Světla, prostředí a mlha jsou dostupné jen v [režimu PBR](#pbr).
Z důvodu výkonu můžete mít na mobilu nejvýš 4 světla a na počítači 6.

::: tip
Můžete načíst soubor glTF s více světly a Nomad je zachová všechna.
Výkon tím ale může utrpět.
:::

::: tip
Mnoho světel můžete nasimulovat tak, že objekty nastavíte jako neosvětlené/emisivní a v nabídce [Postproces](postprocess) zapnete globální osvětlení.
:::

### Přehled typů světel {#light-types-overview}

Toto jsou aktuálně podporované typy světel:

| Režim                       | Popis                                                   | Vrhá stíny       |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Směrové](#directional)     | Sluneční světlo z nekonečné dálky                       | Ano              |
| [Prostředí](#env-light)     | Vzdálené světlo sladěné s HDR prostředí                 | Ano              |
| [Bodové (kužel)](#spot)     | Světla ve tvaru kužele                                  | Ano              |
| [Bodové](#point)            | Všesměrový bodový zdroj světla                          | Ano              |

#### ![](/icons/sun.webp) Směrové {#directional}
Vyzařuje světlo z nekonečné dálky se stejnoměrnou intenzitou.
Na jeho 3d poloze ve scéně nezáleží, důležitá je jen jeho orientace.

Toto světlo můžete připojit ke kameře, takže osvětlení zůstává stejné.  
Můžete tak například vytvořit kontrastní světlo (rim light, silné světlo, které svítí zezadu modelu směrem ke kameře), které vždy osvětluje zadní stranu modelu.

#### ![](/icons/panorama.webp) Světlo prostředí {#env-light}
[HDR prostředí](#environment) se dobře hodí pro celkové měkké osvětlení, ale pokud je v HDR vidět silné ostré světlo, bude jeho stín velmi měkký, často vůbec neviditelný. Pomoci může kombinace směrového světla s HDR prostředím, jenže sladit je bývá obtížné.

Toto světlo tu práci udělá za vás. Automaticky se natočí tak, aby odpovídalo nejjasnější části HDR, a pak samostatně nastavíte jeho intenzitu a úhel (měkkost stínu). 

#### ![](/icons/spotlight.webp) Bodové (kužel) {#spot}
Toto světlo svítí jedním směrem a jeho paprsek je omezený tvarem kužele.

#### ![](/icons/light.webp) Bodové {#point}
Bodové světlo svítí do všech směrů a také může vrhat stíny.

#### Stíny {#shadows}
Každé světlo může vrhat stíny a v jeho [nastavení](#light-extra-controls) si zvolíte, jak se počítají. Pokud vidíte artefakty ve stínech, mohou pomoci tamní posuvníky `Tolerance`.

Kvalita stínů závisí na velikosti objektů vzhledem k celé scéně.  
Pokud máte ve scéně velký objekt, který stíny vrhat nemusí (například velkou rovinu), vypněte vrhání stínů v jeho [nastavení materiálu](material.md#casts-shadows).

## ![](/icons/sun.webp) Světla {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Zaškrtávací políčko světel {#lights-checkbox}

Zapne nebo vypne všechna přímá světla ve scéně.



### Přidat světlo {#add-light}

Přidá do scény světlo, na mobilu nejvýš 4 a na počítači 6. Po přidání světla se zobrazí seznam světel s tlačítky a v horní části zobrazení se objeví panel nástrojů světla.

![](/images/shading_lights_icons.webp)

* Text ukazuje název světla a jeho jas. Klepnutím světlo vyberete.
* Ikona oka přepíná viditelnost.
* Ikonou tužky světlo přejmenujete.
* Ikona koše světlo smaže.
* Ikona kopírování světlo zduplikuje. 
* Ikona se 3 tečkami otevře úplný editor světla. Většina jeho funkcí je dostupná i z panelu nástrojů, který se objeví v zobrazení. 

Světla v seznamu můžete také přetažením přeuspořádat.

### ![](/icons/spotlight.webp)  Ikony {#icons}

Zapne nebo vypne zobrazení ikon světel v zobrazení

### Panel nástrojů světla {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Tento panel nástrojů se objeví v horní části zobrazení, když je vybrané světlo.

* `Viditelný` přepíná viditelnost světla.
* Směrové/Prostředí/Bodové (kužel)/Bodové mění typ světla. Klepnutím je postupně přepínáte, dlouhým stiskem zobrazíte nabídku.
* Intenzita řídí sílu světla. Hodnota může přesáhnout 1,0 pro velmi intenzivní světla, což se hodí s globálním osvětlením v nabídce Postproces
* Klepnutím na barevný vzorek otevřete výběr barvy. Nomad nabízí několik způsobů, jak barvu vybrat. Ovládání v kelvinech nabízí přirozený způsob, jak zvolit teplé nebo studené osvětlení.
* Stín zapíná a vypíná stíny.
* Úhel (_směrové a prostředí_) nebo Velikost (_bodové s kuželem a bodové_) nastavuje šířku světla. Širší světla vrhají měkké stíny, měkčí osvětlení a měkčí odlesky na objektech.
* Připojení (_jen směrové_), Kuželový úhel a Měkkost (_jen bodové s kuželem_) jsou popsané níže v části [editor světla](#light-extra-controls).
* ... zobrazí `Klonovat`, `Znovu vystředit` a `Smazat` spolu s nastavením stínů.

### Další ovládání světla {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Ikona se 3 tečkami u světla v seznamu otevře jeho úplný editor. Některé volby jsou specifické jen pro určité typy světel.

* `Směrové/Prostředí/Bodové` umožňují změnit typ světla.
* Klepnutím na `barevný vzorek` otevřete výběr barvy. 
* `Intenzita` řídí sílu světla.
* `Připojení` (_jen směrové_) připojí světlo ke světu (`Pevně`) nebo ke kameře (`Kamera`). Pokud například použijete směrové světlo za postavou jako kontrastní světlo a zvolíte připojení ke kameře, bude světlo i při otáčení kamery vždy za postavou.
* `Měkkost` (_jen bodové s kuželem_) řídí ostrost okraje kužele světla. 0 znamená velmi ostrý okraj, 1 velmi měkký, s přechodem ke středu kužele. V zobrazení můžete měkkost nastavit interaktivně malou modrou tečkou na kuželi světla.
* `Kuželový úhel` (_jen bodové s kuželem_) řídí úhel rozptylu světla. Malý úhel dává velmi úzký paprsek, 170 velmi široký rozptyl. V zobrazení můžete kuželový úhel nastavit interaktivně oranžovou tečkou.
* `Úhel` (_jen směrové a prostředí_) je zdánlivá velikost světla, představte si, jak velké se slunce jeví na obloze. Větší úhly vrhají měkčí stíny a širší odlesky.
* `Velikost` (_jen bodové s kuželem a bodové_) je šířka světla. Větší světla vrhají měkčí stíny.
* `Stín` zapíná a vypíná stíny aktuálního světla.
* Typ stínu určuje, jak se stíny počítají. `Stínová mapa` vykreslí scénu z pohledu světla, takže stíní i geometrii, kterou kamera nevidí. `Oblast obrazovky` používá jen to, co je už vidět na obrazovce: je méně náročná, ale experimentální. Stínová mapa je obecně spolehlivější.
* `Tolerance` (_jen oblast obrazovky_): pokud jsou vidět artefakty stínů (stíny se nedotýkají povrchů, nebo je ve stínech šum a vzory), může úprava tolerance tyto problémy napravit.
* `Kontaktní` přidá přesnější stíny na krátké vzdálenosti, tam, kde se objekty dotýkají. Při `Auto` dostane kontaktní stíny jen nejvýraznější světlo ve scéně, `Ne` a `Ano` je pro toto světlo vynutí. Jeho posuvník `Tolerance` funguje stejně jako ten výše.

Tlačítko `...` na panelu nástrojů v zobrazení obsahuje stejná nastavení stínů a navíc:

* `Klonovat` světlo zduplikuje.
* `Znovu vystředit` přesune světlo před kameru a zachová jeho orientaci.
* `Smazat` světlo smaže.


## ![](/icons/panorama.webp) Prostředí {#environment}

![](/images/shading_environment.webp)

Světlo v reálném světě přichází ze všech směrů: modrá barva oblohy, zelená trávy, červená budovy. Všechno toto světlo z „prostředí“ lze simulovat pomocí mapy prostředí. 

Zaškrtávacím políčkem vedle názvu osvětlení prostředím zapnete nebo vypnete.

Nomad obsahuje několik ukázkových map prostředí pro interiéry i exteriéry, s různými odstíny a úrovněmi jasu. Vyzkoušejte různé mapy a zjistěte, která na vašich sochách nejlépe vynese detaily.

Klepnutím na obrázek zobrazíte dostupné mapy prostředí. V tomto okně zvolte `Importovat...`, pokud chcete načíst vlastní. Nejlepší jsou obrázky s vysokým dynamickým rozsahem (HDR) ve formátu latlong neboli equirectangular, jako soubory .hdr nebo .exr. Prohlížeč umí prostředí stahovat i přímo z [Poly Haven](https://polyhaven.com/hdris), který má dobrou sbírku bezplatných map prostředí.

### Expozice {#env-exposure}
Upraví jas mapy prostředí. V kombinaci s běžnými světly bývají mapy často příliš jasné. Snížení expozice pomůže vše vyvážit, zvlášť s globálním osvětlením v nastavení [Postproces](postprocess).

### Rotace {#env-rotation}

Mapy prostředí zachycují světlo ze všech směrů, takže je můžete natočit, aby se odrazy a celkové osvětlení k vaší soše dobře hodily. Prostředí můžete otáčet také tažením 3 prsty vodorovně po zobrazení.

### Připojeno ke kameře {#env-attached}
Připojí prostředí ke kameře.

Osvětlení tak zůstává stejné, což se může hodit při sochání.

### Rozostření (pozadí) {#env-background-blur}
Tento posuvník se zobrazuje, jen když je [pozadí](background.md) nastavené na prostředí. Rozostří obrázek prostředí za vaším modelem, aniž by změnil osvětlení.


## ![](/icons/fog.webp) Mlha {#fog}

Mlha dodá scéně atmosférickou hloubku a zviditelní paprsky světla. Zapnete ji zaškrtávacím políčkem vedle názvu. Stejně jako světla a prostředí je dostupná jen v režimu [Osvětlené (PBR)](#pbr).

::: tip Výraznější paprsky světla
Snižte u mlhy `Prostředí` a použijte jasné bodové světlo s kuželem nebo bodové světlo. Zvyšujte `Hustota`, dokud mlha nebude zřetelně vidět. Pro viditelné paprsky v řidší mlze nastavte `Směr rozptylu` na vysokou kladnou hodnotu a namiřte kameru směrem ke světlu.
:::

### Barva {#fog-color}
Barva mlhy a světla, které rozptyluje.

### Hustota {#fog-density}
Jak rychle mlha se vzdáleností houstne.

### Maximální krytí {#fog-opacity}
Omezuje, jak moc může mlha scénu zakrýt, i při vysoké hustotě.

### Směr rozptylu {#fog-scattering}
Směr, kterým mlha rozptyluje světlo (také se mu říká anizotropie). Kladné hodnoty zjasní mlhu, když se díváte směrem ke světlu, záporné, když se díváte od něj, a nula rozptyluje světlo rovnoměrně do všech směrů.

### ![](/icons/panorama.webp) Prostředí {#fog-environment}
Jak moc mlhu osvětluje [prostředí](#environment). Když je prostředí vypnuté, je volba zašedlá.

### Šum {#fog-noise}
Přimíchá do mlhy šum, který ji rozdělí na chuchvalce, aniž by se změnila její celková hustota. Když je šum nad 0, nastavíte posuvníkem `Velikost` velikost vzoru.

### Tvar {#fog-shape}
Kde mlha scénu vyplňuje:

* `Rovnoměrný` - vyplní celou scénu.
* `Svislý` - drží mlhu ve svislém pásu s měkkými okraji. Posuvníky `Dole` a `Nahoře` nastavují výšku jeho dolního a horního okraje a jejich tlačítko s okem při úpravách ukazuje pás v zobrazení.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Jak napovídá název (MATerial CAPture), matcap v jediném obrázku zahrnuje informace o osvětlení i o materiálu.
Protože materiál už je v matcapu obsažen, kanály malování drsnosti a kovovosti se ignorují.
Barva malby se s matcapem násobí, takže pokud máte černý nebo šedý matcap, bílá barva ho nezesvětlí.

Umělci tento režim při sochání často upřednostňují, protože se v něm mohou soustředit na samotný tvar a geometrii.

Klepnutím na kouli otevřete prohlížeč obrázků. Můžete přidat i vlastní matcap: obecně poslouží jakákoli fotka, render, nebo dokonce malba koule, která je těsně oříznutá do čtverce. Na internetu najdete mnoho knihoven matcapů, užitečným zdrojem je [knihovna matcapů nidorx](https://github.com/nidorx/matcaps).

### Použít globální MatCap {#matcap-global}

Umělci obvykle používají jediný matcap pro celou sochu, ale když tento přepínač vypnete, může mít vybraný objekt vlastní matcap. Dá se to využít umělecky k dosažení působivých výsledků.

::: tip
Vypněte tuto volbu a použijte na oči svých postav obrázek oční bulvy!
:::

### Rotace {#matcap-rotation}
Matcap je zvláštní druh mapy prostředí, takže ho stejně jako mapu prostředí můžete otáčet. Kdykoli to můžete udělat i v zobrazení tažením 3 prsty doleva a doprava.

Tlačítko zámku vedle posuvníku rotaci zamkne, takže tažení 3 prsty matcap omylem neotočí.



## ![](/icons/circle_fill.webp) Neosvětlené {#unlit}

Tento režim ukazuje jen barvu povrchu. Hodí se pro kontrolu, zda mají vaše objekty takovou barvu povrchu, jakou čekáte, aniž by vás rozptylovala světla, stíny, odrazy nebo průhlednost. 

Tento režim můžete použít i pro nefotorealistické rendery s plochým, komiksovým vzhledem.

## ![](/icons/cube.webp) ID objektu {#object-id}

Veškeré informace o osvětlení a povrchu se ignorují a každý objekt se vystínuje jedinečnou plochou barvou. Když tento obrázek vyrenderujete vedle PBR renderu, můžete ho v malířském programu použít k výběru podle barvy, a upravit tak barvy jen u konkrétních objektů.

Tyto barvy se objeví i ve [stromovém zobrazení nabídky Scéna](scene#tree-view).

### Náhodné ID {#object-random}

Vygeneruje novou sadu náhodných barev. 

## ![](/icons/link.webp) ID instance {#instance-id}

Stejné jako ID objektu, ale instance mají stejnou barvu. 

### Náhodné ID {#instance-random}

Vygeneruje novou sadu náhodných barev. 
