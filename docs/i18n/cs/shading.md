# ![](/icons/sun.webp) Stínování {#shading}

Tato nabídka ovládá režimy stínování používané v Nomadu, vlastnosti světel a vlastnosti světla prostředí/matcapu.

![](/images/shading_overview.webp)



Můžete si vybrat z několika režimů vykreslování:

| Mode                        | Meaning                    | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | Malování s metalicitou/drsností                                |
| [Matcap](#matcap)           | Material Capture           | Používá se při sochání s nižším využitím GPU/CPU než PBR        |
| [Unlit](#unlit)             | Surface Color              | Pouze barva povrchu bez stínování a osvětlení                  |
| [Object Id](#object-id)      | Object ID                  | Náhodná barva na objekt, užitečné pro malířské aplikace        |
| [Instance Id](#instance-id)  | Instance ID                | Náhodná barva na instanci, užitečné pro identifikaci sdílených meshů |

Pokud se chcete dozvědět více o metalicitě a drsnosti, podívejte se na sekci [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Skupina ploch {#face-group}
Překryvné barvy facegroup. Facegroup jsou barevné výběry polygonů, které lze vytvořit nástrojem [Face group](tools#facegroup) a automaticky vznikají u většiny primitiv.

Některé nástroje budou automaticky filtrovat podle facegroup, pokud jsou facegroup viditelné.

### Zobrazit malbu {#show-paint}
Nomad může ukládat barvu, drsnost a metalicitu do vrcholů (vertices) vaší sochy. Zobrazení těchto vlastností můžete globálně přepínat tímto zaškrtávacím políčkem.

Všimněte si, že pokud máte jak vlastnosti ve vrcholech, tak textury a obojí je povoleno, hodnoty se budou mezi sebou násobit.

### Zobrazit masku {#show-mask}
Přepíná šedotónový překryv masky z [mask tools](tools#mask). Když je toto vypnuto, maska je také vypnutá, což je užitečné pro rychlé úpravy bez masky; poté ji můžete znovu zapnout a masku neztratíte.

### Použít skrýt {#use-hide}

Přepíná skryté plochy. Poznámka: funguje pouze pokud NEjste v nástroji hide!

### Použít textury {#use-textures}

Nomad umožňuje přiřadit textury objektům z nabídky [material](material). Pokud jsou textury přiřazeny, lze je globálně přepínat tímto zaškrtávacím políčkem.







### Přehled PBR a světel {#pbr}
Tento manuál nepůjde do detailů fyzikálně založeného renderingu (Physically Based Rendering).

Důležité je mít na paměti, že osvětlení a materiál jsou zcela oddělené.
To znamená, že můžete malovat barvu, drsnost a metalicitu objektu, zatímco osvětlení je řešeno nezávisle.
Umožňuje to namalovat objekt a pak později doladit osvětlení, aniž by se rozbil celkový vzhled modelu.

Světla jsou dostupná pouze v [PBR režimu](#pbr).
Z důvodů výkonu jste omezeni na maximálně 4 světla.

::: tip
Můžete načíst soubor glTF s více než 4 světly a Nomad je všechny zachová.
Nemusí to však nutně běžet plynule.
:::

::: tip
Mnoho světel můžete „falšovat“ tím, že objekty nastavíte jako unlit/emissive a poté zapnete globální iluminaci v nabídce [post process](postprocess).
:::

### Přehled typů světel {#light-types-overview}

Zde jsou typy světel, které jsou aktuálně podporovány:

| Mode                        | Description                                             | Can cast shadows                                       |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Sluneční světlo z nekonečné vzdálenosti               | ano                                                    |
| [Environment](#environment) | Vzdálené světlo odpovídající HDR prostředí             | ano                                                    |
| [Spot](#spot)               | Kuželová světla				                        | Ano                                                    |
| [Point](#point)             | Bodové světlo svítící všemi směry                      | Ano, ale pouze méně robustní screen-space stíny       |

#### Směrové {#directional}
Vyzařuje světlo z nekonečné vzdálenosti s jednotnou intenzitou.
Jeho 3D pozice ve scéně není důležitá, záleží pouze na orientaci.

Toto světlo můžete připojit ke kameře, takže bude mít konzistentní osvětlení.  
Například ho můžete použít jako rim light (silné světlo vycházející zezadu modelu směrem ke kameře), které vždy osvětluje zadní část vašeho modelu.

#### Prostředí (environment) světlo {#env-light}
Použití [environment hdr](#environment) dobře funguje pro celkové měkké osvětlení, ale pokud je v HDR viditelné silné ostré světlo, stín jím vytvořený bude velmi měkký, často téměř neviditelný. Pomoci může použití směrového světla v kombinaci s environment HDR, ale může být obtížné je zarovnat.

Toto světlo tuto práci udělá za vás. Světlo se automaticky natočí tak, aby se zarovnalo s nejjasnější částí HDR, a vy pak můžete samostatně ovládat jeho intenzitu a úhel (měkkost stínu). 

#### Reflektor {#spot}
Reflektor (spot light) vyzařuje světlo jedním směrem, omezené tvarem kužele.

#### Bodové {#point}
Bodové světlo vyzařuje světlo všemi směry.  
V tuto chvíli bodové světlo nepodporuje stíny.

#### Stíny {#shadows}
Volba `normal bias` může být použita ke snížení běžných artefaktů stínů (acne/peter-panning).

Kvalita stínů závisí na velikosti objektů vzhledem k celé scéně.  
Pokud máte ve scéně velký objekt, který nemusí vrhat stíny (například velkou rovinu), ujistěte se, že je u něj vrhání stínů vypnuto v [nastavení materiálu](material.md#cast-shadows).

## Světla {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Zaškrtávací políčko Světla {#lights-checkbox}

Přepíná všechna přímá světla ve scéně.



### Přidat světlo {#add-light}

Přidá světlo do scény, maximálně 4. Když je světlo přidáno, zobrazí se seznam světel s tlačítky a do horní části viewportu se přidá panel nástrojů světla.

![](/images/shading_lights_icons.webp)

* Text zobrazuje název světla a jas.
* Ikona oka přepíná viditelnost.
* Ikona tužky umožňuje přejmenovat světlo.
* Ikona koše světlo smaže.
* Ikona kopie světlo duplikuje. 
* Ikona se 3 tečkami otevře plný editor světla. Většina této funkčnosti je také dostupná z panelu nástrojů, který se objeví ve viewportu. 

### ![](/icons/spotlight.webp) Ikony {#icons}

Přepíná zobrazení ikon světel ve viewportu.

### Lišta světel {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Tento panel nástrojů se objeví v horní části viewportu, když je vybráno světlo.

* Show přepíná viditelnost světla.
* Directional/Environment/Spot/Point mění typ světla. Klepnutím cyklujete, dlouhým stiskem zobrazíte nabídku.
* Intensity ovládá sílu světla, hodnota může jít nad 1.0 pro velmi intenzivní světla, užitečné při použití s Global Illumination v Post Process.
* Kliknutím na vzorek barvy se otevře výběr barvy. Nomad nabízí několik způsobů volby barvy. Ovládání Kelvin poskytuje přirozený způsob výběru teplého/studeného světla.
* Shadow přepíná stíny.
* Size nastavuje šířku světla. Širší světla vrhají měkčí stíny, měkčí osvětlení a měkčí odlesk na objektech.
* ... otevře další ovládací prvky.

### Rozšířené ovladače světel {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Všimněte si, že některé volby jsou specifické pro určité typy světel.

* `Clone` duplikuje světlo.
* `Recenter` přesune světlo zpět do počátku.
* `Delete` světlo smaže.
* `Directional/Environment/Spot/Point` umožňují změnit typ světla.
* `colour swatch` po kliknutí otevře výběr barvy. 
* `Intensity` ovládá sílu světla.
* `Attachment` (_pouze directional_) nastaví, zda je světlo rodičem světa, nebo kamery. Např. pokud použijete směrové světlo za postavou jako rim light, při nastavení attachment na camera bude při otáčení kamery světlo vždy za postavou.
* `Angle` (_pouze directional a environment_) je zdánlivá velikost světla, představte si ji jako to, jak velké se slunce jeví na obloze. Větší úhly vrhají měkčí stíny a širší odlesky.
* `Softness` (_pouze spotlight_) ovládá ostrost okraje kužele reflektoru. 0 je velmi ostrý okraj. 1 je velmi měkký, s přechodem ke středu světelného kužele. Ve viewportu lze malým modrým bodem na kuželu reflektoru interaktivně nastavovat softness.
* `Cone angle` (_pouze spotlight_) ovládá rozptylový úhel reflektoru. Malý úhel je velmi tenký paprsek světla, 170 je velmi široký rozptyl světla. Ve viewportu lze oranžovým bodem interaktivně nastavovat cone angle.
* `Shadow` přepíná stíny pro aktuální světlo.
* `Shadow map` a `screenspace` jsou různé způsoby výpočtu stínů, obecně je shadow map spolehlivější.
* `Contact` upravuje, jak jsou stíny počítány. Stíny jsou v počítačové grafice obtížný problém a mohou způsobovat artefakty v renderu. Pro nejdůležitější světlo ve scéně lze zvolit přesnější stíny; toto ovládání určuje, zda nejdůležitější světlo vybere automaticky Nomad, nebo uživatel.
* `Tolerance` pokud jsou viditelné artefakty stínů (stíny se nezdají dotýkat povrchů, nebo je v nich šum a vzory), úprava tolerance může pomoci tyto problémy vyřešit.


## Prostředí {#environment}

![](/images/shading_environment.webp)

Světlo ve skutečném světě přichází ze všech směrů; modrá oblohy, zelená trávy, červená budovy – toto světlo z „prostředí“ lze simulovat environment mapou. 

Nomad obsahuje několik ukázkových environment map pro vnitřní i venkovní prostředí s různými odstíny a úrovněmi jasu. Vyzkoušejte různé mapy a zjistěte, která nejlépe zvýrazní detaily vašich soch.

Klepnutím na obrázek zobrazíte dostupné environment mapy. V tomto dialogu zvolte „Import...“ pro načtení vlastní. Nejlepší je používat obrázky s vysokým dynamickým rozsahem (HDR) ve formátu latlong nebo equirectangular jako soubory .hdr nebo .exr. Stránka [www.polyhaven.com](https://polyhaven.com/hdris) má dobrou kolekci bezplatných environment map; obecně jsou 1k hdr mapy dobrou velikostí i kvalitou.

### Expozice {#env-exposure}
Upravuje jas environment mapy. Často mohou být mapy příliš jasné při použití s běžnými světly; snížení expozice může pomoci vyvážit scénu, zvláště při použití s Global Illumination v nastavení [Post Process](postprocess).

### Rotace {#env-rotation}

Protože environment mapy zachycují světlo ze všech směrů, můžete je otáčet, aby se odrazy a celkové osvětlení dobře kombinovaly s vaší sochou.

### Připojeno ke kameře {#env-attached}
Připojí prostředí ke kameře.

Vynutí konzistentní osvětlení, což může být užitečné během sochání.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Jak název napovídá (MATerial CAPture), matcap se stará jak o informace o osvětlení, tak o materiálu v jediném obrázku.
Protože materiál je již v matcapu obsažen, malovací kanály drsnosti a metalicity budou ignorovány.
Barva malby bude s matcapem násobena, což znamená, že pokud máte černý/šedý matcap, použití bílé barvy ho nezesvětlí.

Umělci tento režim často preferují pro účely sochání, protože jim umožňuje soustředit se na tvar a geometrii samotnou.

Klepnutím na kouli se otevře prohlížeč obrázků. Můžete také přidat vlastní matcap; obecně lze použít jakoukoli fotografii, render nebo dokonce malbu koule, která byla těsně oříznuta do čtverce. Online je k dispozici mnoho knihoven matcapů, užitečným zdrojem je [nidorx matcap library](https://github.com/nidorx/matcaps).

### Použít globální Matcap {#matcap-global}

Obvykle umělci používají jeden matcap pro celou sochu, ale pokud je toto přepínání vypnuto, může mít každý objekt svůj vlastní matcap. To lze umělecky využít k dosažení výrazných výsledků.

::: tip
Vypněte tuto volbu a použijte obrázek oční bulvy pro oči vaší postavy!
:::

### Rotace {#matcap-rotation}
Matcap je specializovaná forma environment mapy, takže stejně jako environment mapu ho lze otáčet. Můžete to také kdykoli udělat ve viewportu tažením třemi prsty doleva a doprava.



## ![](/icons/circle_fill.webp) Bez osvětlení {#unlit}

Tento režim zobrazuje pouze barvu povrchu. Může být užitečný pro kontrolu, zda jsou barvy povrchů vašich objektů takové, jak očekáváte, aniž by vás rozptylovala světla, stíny, odrazy či průhlednost. 

Tento režim lze také použít pro ne-fotorealistické rendery, k dosažení plochého, kresleného vzhledu.

## ![](/icons/cube.webp) ID objektu {#object-id}

Veškeré informace o osvětlení a povrchu jsou ignorovány a každý objekt je stínován jedinečnou plochou barvou. Pokud je toto vyrenderováno vedle PBR renderu, lze to v malířském programu použít k výběru podle barvy a tím k barevným korekcím konkrétních objektů.

Všimněte si, že tyto barvy se také objeví ve [stromovém zobrazení nabídky Scene](scene#tree-view).

### Náhodné id {#object-random}

Vygeneruje novou sadu náhodných barev. 

## ![](/icons/link.webp) ID instance {#instance-id}

Stejné jako Object ID, ale instance budou mít stejnou barvu. 

### Náhodné id {#instance-random}

Vygeneruje novou sadu náhodných barev.