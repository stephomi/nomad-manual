# ![](/icons/faq.webp) Časté dotazy {#faq}

[[toc]]

## Platforma {#platform}
### Kde v zařízení najdu své projekty? {#locate}
Projekty jsou ve složce `projects` uvnitř hlavní složky Nomadu.

Na iOS se ke složce Nomadu dostanete přes aplikaci Soubory.

Na Androidu je složka Nomadu v `Android/data/com.stephaneginier.nomad/files/`.  
V novějších verzích Androidu (10/11) už ke složce `Android/data` přímý přístup nemáte.
Dostanete se k ní přes samostatnou aplikaci, například [tuto](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Dá se zapojit do beta testování? {#beta}
Pro Windows a MacOS může být beta dostupná na [domovské stránce](https://nomadsculpt.com).
<br>
Pro iOS existuje soukromý TestFlight, navštivte kanál #beta-ios na [Discordu](https://discord.com/invite/8h7BwpRz29).
<br>
[Webové demo](https://nomadsculpt.com/demo) obvykle obsahuje nejnovější funkce.

### Proč je na Androidu zkušební verze zdarma, ale na iOS ne? {#android-trial}
Protože stará zařízení s Androidem stojí za nic (a některá novější taky...) a nechtěl jsem, aby si lidé aplikaci koupili a přivítala je černá obrazovka.
Hlavním důvodem ale je, že placené aplikace na Androidu podle mě nejsou úplně běžné.

### Na jakém tabletu běží Nomad nejlépe? {#best-tablet}

Ve zkratce: na iPadu.

Trochu delší odpověď zní 

> „Nejnovější iPad, _který si můžete dovolit_, pokud Apple opravdu nesnášíte, tak nejnovější tablet Samsung, který si můžete dovolit. Cokoli jiného nejdřív vyzkoušejte.“ 

Lidé vždycky chtějí víc informací, takže tady je shrnutí.

Nomad běží nejlépe na novějších iPadech:

* iPady a iPhony mají přístup k pluginu [Quad Remesher](tools#quad-remesher) od [Exoside](https://exoside.com/)
* novější iPady s nejnovější tužkou podporují [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), takže u některých nástrojů v Nomadu můžete tužkou otáčet. 
* nejnovější čipy řady M jsou velmi výkonné. 

Nejnovější a nejdražší dostupný iPad vykreslí finální obrázky velmi rychle a umožní vám sochat spoustu detailů.

Pokles výkonu u levnějších a starších iPadů ale není tak velký, jak lidé čekají. Každý iPad, který podporuje Apple Pencil, zvládá Nomad docela dobře. Například:

* iPad Pro z roku 2023 zvládne sochy s 5 miliony polygonů a zůstane svižný, obrázek ve finální kvalitě vykreslí za 5 sekund.
* iPad Pro z roku 2015 zvládne objekt s 1,2 milionu polygonů s mírným zasekáváním, obrázek ve finální kvalitě vykreslí za 20 sekund.

To je velký rozdíl ve výkonu, musíte ale vzít v úvahu i cenu:

* iPad Pro z roku 2025 stojí nový se všemi možnostmi *2500 USD*. 
* iPad Pro z roku 2023 stojí momentálně na eBay *400 USD*.
* iPad Pro z roku 2015 stojí na eBay *250 USD*.

Stojí 4 miliony polygonů navíc a 15 ušetřených sekund za 2100 USD? To je na vás.

Modely bez označení Pro mohou být ještě levnější a nabízejí širokou škálu velikostí a výkonu. Současný iPad Air podporuje tužku 2. generace s barrel roll a je výrazně levnější než Pro. Trh s použitými a repasovanými zařízeními nabízí ještě víc možností. 

To znamená, že ať máte jakýkoli rozpočet, měli byste si najít iPad pro sebe. A pamatujte, že většina soch nemá miliony polygonů! Pokud zůstanete pod 500 000 polygony, budete i na starých iPadech sochat svižně.

`A co Android?`

Grafický výkon Androidu je nižší než u iPadů. Podle vývojáře Nomadu „Samsung Galaxy Tab S9 poběží s Nomadem o řád pomaleji než iPad Air“. Přesto je mnoho uživatelů se svými tablety Samsung velmi spokojených a Nomad na nich pro většinu sochání běží dobře. 

U ostatních tabletů s Androidem buďte opatrní. Výkon hardwaru s Androidem se může hodně lišit a není snadné předvídat, jak na něm Nomad poběží.

Nejdřív prosím vyzkoušejte bezplatnou verzi Nomadu s vypnutým ukládáním. 

`A co paměť a úložiště?`

Většina souborů Nomadu mívá 100 MB nebo méně. Téměř každý tablet, který si dnes koupíte, iPad i Android, tak bude mít pro vaše projekty Nomadu dost místa.


### Koupil jsem Nomad pro jedno zařízení, můžu ho používat i na jiném? {#multi-devices}
Ano, pokud používá stejný obchod s aplikacemi a stejný účet.

Pokud jste ho například koupili v App Store pro iOS, můžete ho používat i na svých dalších zařízeních s iOS.

Pokud jste ho koupili pro tablet s Androidem na Google Play, můžete ho používat i na svých dalších zařízeních s Androidem.

Pokud jste ale Nomad koupili na Androidu a pak si pořídíte iPad, budete ho muset koupit znovu.

Je to proto, že Nomad nemá vlastní licenční server ani model předplatného. Mezi Apple, Google a AppGallery neexistuje žádná dohoda o sdílení licencí. 


### Jak obnovit nákup? {#restore}
Google Play i AppGallery řeší synchronizaci automaticky.

- Přejděte do nabídky O aplikaci (ikona Nomadu vlevo nahoře) a klepněte na `Obnovit nákup`
- Ověřte, že jste přihlášeni ke stejnému účtu, se kterým jste Nomad koupili (na Google Play).
- Restartujte zařízení
- Někdy je potřeba pár hodin počkat
- Ujistěte se, že je aplikace Google Play aktuální
- Přeinstalujte Nomad (pokud nechcete o nic přijít, nezapomeňte si [zálohovat soubory](#locate))
- Můžete zkusit nákup zopakovat a uvidíte, co se stane (pozn.: stejnou položku nelze na stejném účtu koupit dvakrát)

:::tip
Můžete mi napsat na <support@nomadsculpt.com>, ale *jediné*, co můžu udělat, je ověřit, zda je k e-mailu přiřazený nákup.

Pravidelně dostávám hlášení o licencích, které se po pořízení nového zařízení správně neaktualizovaly.
Na platby a synchronizaci účtů nemám žádný vliv, vše řeší Google/AppGallery!

Nákup se nakonec vždycky obnoví, jen není jasné, jak celý proces urychlit.
:::

::: warning
Novější zařízení Huawei nemají přístup ke službám Google.
V takovém případě musíte aplikaci znovu koupit v AppGallery (obchod s aplikacemi Huawei).
:::

### Můžete přeložit nebo opravit [můj-jazyk]? {#locale}
Další jazyk můžu přidat poměrně snadno, ale spoléhám na překlad pomocí AI, protože se s ním při pravidelných aktualizacích pracuje mnohem snáz.
Soubory s překlady najdete [zde](https://github.com/stephomi/nomad-translation).

## Funkce {#features}

### Proč se gizmo nehýbe? {#gizmo-not-moving}
Možná máte [zapnuté připnutí na levém panelu nástrojů nabídky](tools#left-menu-toolbar). 

### Dá se v Nomadu animovat? {#animate}
Zatím ne. Časová osa, která by animovala vrstvy, by mohla být zajímavá, ale momentálně ji v plánu nemám.  

Rád bych v budoucnu podporoval rigging/skinning, ale přináší to několik výzev (hlavně souhru se sochařskými nástroji...), takže zatím nic jistého.


### Dá se dělat skutečné low-poly modelování? {#lowpoly}
Zatím ne.
To není tak úplně zaměření Nomad *Sculpt*, ale možná v budoucnu přidám pár nástrojů.


### Dají se dělat UV a texturování? {#texturing}
Krátká odpověď: Ano. Dlouhá odpověď: Ne přímo, ale existuje několik způsobů, jak skvělé nástroje Nomadu pro malování vrcholů zkombinovat s UV a texturami.

* V Nomadu můžete malovat barvu, drsnost a vlastnosti materiálu přímo do vrcholů vaší sochy.
* Nomad zvládá velmi vysoký počet vrcholů, takže můžete malovat a nemusíte se starat o UV.
* Nomad umí načíst textury do štětců, takže můžete texturami otiskovat a malovat.
* Nomad umí pro účely renderu načíst objekty s předem přiřazenými texturami.
* Nomad umí [rozbalit UV](topology.md#uv-unwrap-uvatlas) objektů s nižším počtem polygonů.
* Barvu, drsnost a kovovost lze přenést z textur do vrcholů pomocí [voleb projekce](topology.md#reproject-to-vertex).
* Barvu, drsnost, kovovost a normály lze zapéct z vrcholů do textur pomocí [voleb pečení](topology.md#bake-texture)
* Pečení a projekci lze provádět mezi jednotlivými objekty nebo mnoha objekty, případně mezi nejvyšší a nejnižší úrovní subdivize jednoho objektu, což umožňuje různé postupy pečení a projekce.
* Po zapečení se při exportu obj exportují i textury, které pak můžete otevřít v aplikaci jako Procreate a malovat přímo na ně.

### Můžu nahrát video s otáčením modelu? {#video}
Zatím to v plánu není, iOS má ale [funkci nahrávání obrazovky](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados), která se velmi snadno používá.

Na iOS přejeďte prstem dolů z levého horního rohu a klepněte na tlačítko nahrávání. Spustí se 3sekundový odpočet. Odsuňte nabídku, aby byl vidět Nomad, a použijte funkci otáčení. Až budete hotovi, přejeďte znovu dolů z pravého horního rohu a znovu klepněte na tlačítko nahrávání. Ve fotoknihovně video upravte a odstraňte přebytečné záběry na začátku a na konci.

### Můžete přidat [oblíbenou-funkci] jako tlačítko na hlavní úrovni? {#interface}
Ano, spodní panel nástrojů si teď můžete přizpůsobit v nabídce [Rozhraní](interface.md#shortcuts) a vytvářet můžete i plovoucí panely nástrojů.

### Jaké funkce přijdou dál? {#next-features}
Pro střednědobý a dlouhodobý plán mám spoustu nápadů, ale zatím nevím.  

Opravy chyb a vylepšování stávajících funkcí budou mít vždy přednost před přidáváním nových funkcí.


### Dá se v Nomadu riggovat? {#rigging}
Ne, ale je to v plánu. Zatím můžete tvary vnořovat do sebe a měnit otočné body, takže si vytvoříte jednoduché sochy, které jde napózovat.

### Dá se použít víc než 4 světla? {#lights}
Na mobilu můžete použít až 4 světla a na počítači až 6. Je to omezení vykreslovacího jádra Nomadu v reálném čase. Dá se to obejít pomocí emisivních objektů a globálního osvětlení v postprocesu, jak ukazuje [tento návod](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Dají se importovat nástroje ze Zbrush? {#zbrush-import}
Ne, Zbrush používá proprietární formát. Alfa mapy byste ale měli dokázat vyexportovat a použít v Nomadu. 

### Proč barvy neodpovídají tomu, co jsem namaloval? Proč v renderu nedostanu bílou? {#paint-pbr}
Představte si fotku kusu papíru, fotku stolní lampy a fotku slunce. Starší fotoaparáty a obrazovky z nich všech udělají prostě „bílou“. Modernější systémy dokážou ukázat rozdíl mezi bílou odraženou od papíru, světlem vyzařovaným lampou a extrémním jasem slunce.

Moderní počítačová grafika se snaží fungovat podobně a napodobuje fyziku světla a povrchů. Říká se tomu `Physically Based Rendering` neboli PBR a na tom je založený i PBR renderer Nomadu. Výsledek vypadá realisticky a vyváženě, ale jasně namalované barvy často působí tmavší.

Pokud potřebujete, aby render víc odpovídal namalovaným barvám, můžete to napravit fyzikálně nezaloženými i fyzikálně založenými způsoby:

Bez PBR:
* `Použijte režim Neosvětlené v nabídce Stínování`. Barvy se zobrazí přesně tak, jak jste je namalovali, ale přijdete o veškeré stínování. Hodí se pro rychlou kontrolu a grafičtější výstup.
* `Použijte režim MatCap v nabídce Stínování`. Zvolte jasnější matcap, který je převážně bílý, bez barevného nádechu.

PBR:
* `Použijte neutrální prostředí`. [Prostředí můžete změnit](shading.md#environment) na neutrálnější. Vyhněte se interiérovým prostředím, která bývají barevnější. Dejte přednost dennímu venkovnímu nebo studiovému prostředí.
* `Zesilte osvětlení`. Kdybyste fotili bílý papír v tmavé místnosti, prostě byste přidali světlo. U světla prostředí zvyšujte posuvník expozice, dokud vám barvy nebudou připadat správně, nebo přidejte další samostatná světla s vyšší intenzitou.
* `Zvyšte expozici kamery`. Kdyby v tmavé místnosti žádná další světla nebyla, mohli byste nechat závěrku fotoaparátu otevřenou déle, nebo použít citlivější ISO. V Nomadu dosáhnete podobného výsledku postprocesem. Přejděte do postprocesu, zapněte ho, sjeďte k mapování tónů, zapněte ho a zvyšujte posuvník expozice, dokud barvy nebudou vypadat správně.
* `Použijte emisní barvu`. V nabídce materiálu můžete u textur zapnout „emise“, díky čemuž bude objekt vypadat jako zdroj světla. Když v nastavení postprocesu zapnete globální osvětlení, bude vrhat světlo na ostatní objekty ve scéně. Pro daný materiál můžete také zapnout „Vždy neosvětlené“, čímž dosáhnete podobného vzhledu bez textury.

## Pády {#crashes}

### Aplikace spadne, když model ukládám nebo přesíťovávám! {#crash-remesh}
Vašemu zařízení dochází paměť (RAM).  
Spotřebu paměti ve scéně můžete snížit tak, že některými volbami v nabídce [Topologie](topology.md) snížíte počet polygonů.

::: tip RAM/úložiště
Rozhoduje velikost RAM, ne úložiště (které je obvykle mnohem větší).
:::


### Aplikace spadne, když načítám projekt! {#crash-load}
Pokud je soubor malý, můžete mi ho poslat a podívám se na něj (e-mailem na <support@nomadsculpt.com>).

Jinak zařízení nejspíš dochází paměť RAM.

- Zavřete v zařízení všechny ostatní otevřené aplikace.
- Místo otevřeného projektu založte v Nomadu nový projekt.
- Pokud aplikace stále padá, jediným řešením je načíst [soubor projektu](#locate) na zařízení s větší pamětí.

::: tip
Pokud projekt nejde načíst na mobilním zařízení, vyzkoušejte [verzi pro počítač](https://nomadsculpt.com). V režimu Demo ji můžete zdarma používat k importu a exportu projektů, i když je k dispozici jen pár nástrojů pro úpravy.

Pokud váš projekt používá [Vrstvy](layers.md), možná je budete chtít sloučit, abyste snížili spotřebu paměti.
:::

### Aplikace spadne, když spouštím Nomad! {#crash-start}
Pokud aplikace spadne při načítání, znamená to, že Nomad má potíže s určitým souborem ve složce Nomadu.

Většinou se to stane, protože je projekt náročný a bohužel překročí limit RAM.

Najděte [složku Nomadu](#locate) a pak přejmenujte nebo přesuňte některé soubory, abyste viníka našli.

Nejdřív zkuste přejmenovat `settings.json`. Nomad pak přestane načítat poslední projekt.

Pokud to nepomůže, zkuste přesunout některé nedávné soubory mimo jejich složky prostředků (`projects`, `matcaps`, `environments` atd.).

Můžete také přejmenovat samotné složky, aby je Nomad úplně ignoroval.
Když přejmenujete nebo přesunete všechny soubory ve složce Nomadu, bude to mít stejný výsledek jako čistá instalace.

::: tip
Když Nomad při spuštění načítá soubor, vždy ho přesune do složky `can_be_deleted/`.
Pokud operace uspěje, přesune se soubor zpět do své původní složky.

Pokud aplikace spadne dřív, než se načítání dokončí, Nomad se při dalším spuštění úspěšně spustí, protože složku `can_be_deleted/` ignoruje.

Pokud si myslíte, že by to mohlo uspět, můžete zkusit tento soubor načíst znovu.
:::
