# ![](/icons/faq.webp) Často kladené otázky {#faq}

[[toc]]

## Platforma {#platform}
### Kde jsou na mém zařízení uloženy moje projekty? {#locate}
Projekty se nacházejí ve složce `projects` uvnitř hlavní složky Nomad.

V iOS se ke složce Nomad dostanete přes aplikaci Soubory.

V Androidu je složka Nomad v `Android/data/com.stephaneginier.nomad/files/`.  
V novějších verzích Androidu (10/11) už nemáte přístup ke složce `Android/data`.
Můžete se k ní dostat pomocí samostatné aplikace, například [této](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Je možné testovat beta verzi? {#beta}
Pro Windows a MacOS může být beta verze dostupná na [domovské stránce](https://nomadsculpt.com).
<br>
Pro iOS existuje soukromý TestFlight, navštivte [Discord](https://discord.com/invite/8h7BwpRz29) v kanálu #beta-ios.
<br>
[Webová ukázka](https://nomadsculpt.com/demo) je obvykle aktualizována s nejnovějšími funkcemi.

### Proč je na Androidu k dispozici bezplatná zkušební verze, ale na iOS ne? {#android-trial}
Protože stará Android zařízení jsou mizerná (a některá nová také...), a nechtěl jsem, aby si lidé koupili aplikaci a přivítala je černá obrazovka.
Hlavní důvod ale je, že placené aplikace na Androidu nejsou úplně standardem.

### Jaký je nejlepší tablet pro provozování Nomadu? {#best-tablet}

Stručně: iPad.

O něco delší odpověď je: 

> „Nejnovější iPad, který _si můžete dovolit_, pokud opravdu nesnášíte Apple, tak nejnovější tablet Samsung, který si můžete dovolit. Cokoli jiného si nejdřív otestujte.“ 

Lidé vždy chtějí víc informací, takže tady je shrnutí.

Nomad běží nejlépe na novějších iPadech:

* iPady a iPhony mají přístup k pluginu [Quad Remesher](tools#quad-remesher) od [Exoside](https://exoside.com/)
* novější iPady s poslední verzí Apple Pencil podporují [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), můžete tužku v určitých nástrojích v Nomadu otáčet.
* výkon nejnovějších čipů řady M je velmi vysoký. 

Nejnovější a nejdražší dostupný iPad dokáže velmi rychle renderovat finální obrázky a umožní vám modelovat s velkým množstvím detailů.

Pokles výkonu u levnějších a starších iPadů ale není tak dramatický, jak lidé čekají. Jakýkoli iPad, který podporuje Apple Pencil, spouští Nomad poměrně dobře. Například:

* iPad Pro z roku 2023 zvládne 5milionové modely a zůstává svižný, finální kvalitní obrázek se vyrenderuje za 5 sekund.
* iPad Pro z roku 2015 zvládne objekt s 1,2 milionu polygonů s mírným zpožděním, finální kvalitní obrázek se vyrenderuje za 20 sekund.

To je velký rozdíl ve výkonu, ale musíte vzít v úvahu i cenu:

* iPad Pro 2025 stojí *2500 USD* jako nový se všemi volbami.
* iPad Pro 2023 aktuálně stojí na eBay *400 USD*.
* iPad Pro 2015 stojí na eBay *250 USD*.

Stojí vám extra 4 miliony polygonů a ušetřených 15 sekund za 2100 dolarů? To je na vás.

Ne-Pro modely mohou být ještě levnější a nabízejí širokou škálu velikostí a výkonu. Současný iPad Air podporuje Apple Pencil 2. generace s barrel rollem a je výrazně levnější než Pro. Trh s použitými a repasovanými zařízeními nabízí ještě více možností. 

To znamená, že pro jakýkoli rozpočet byste měli být schopni najít vhodný iPad. A pamatujte, že většina modelů nemá miliony polygonů! Pokud se udržíte pod 500 000 polygonů, i starší iPady vám umožní rychlé modelování.

`A co Android?`

Grafický výkon Androidu je nižší než u iPadů. Podle vývojáře Nomadu „Samsung Galaxy Tab S9 spustí Nomad řádově pomaleji než iPad Air“. Přesto je mnoho uživatelů se svými tablety Samsung velmi spokojených, Nomad běží pro většinu modelovacích úloh dostatečně dobře. 

U ostatních Android tabletů buďte opatrní. Výkon hardwaru s Androidem se může velmi lišit a není snadné předpovědět, jak na něm Nomad poběží.

Nejprve prosím použijte bezplatnou verzi Nomadu bez ukládání a otestujte si to. 

`A co paměť a úložiště?`

Většina souborů Nomadu má obvykle 100 MB nebo méně. To znamená, že téměř jakýkoli tablet, který si dnes koupíte, ať už iPad nebo Android, bude mít pro vaše projekty Nomad dostatek místa.


### Koupil jsem Nomad pro jedno zařízení, mohu ho použít na jiném zařízení? {#multi-devices}
Pokud používá stejný obchod s aplikacemi a stejný účet, tak ano.

Například pokud jste ho koupili v iOS App Store, můžete ho používat na ostatních iOS zařízeních.

Pokud jste ho koupili pro Android tablet na Google Play, můžete ho používat na ostatních Android zařízeních.

Pokud jste ale koupili Nomad na Androidu a pak si pořídíte iPad, budete ho muset koupit znovu.

Je to proto, že Nomad nemá vlastní licenční server ani předplatné. Neexistuje žádná dohoda mezi Apple/Google/AppGallery ohledně sdílení licencí. 


### Jak obnovit svůj nákup? {#restore}
Google Play i AppGallery synchronizaci řeší automaticky.

- Jděte do nabídky About (ikona Nomad vlevo nahoře) a stiskněte `restore purchase`
- Zkontrolujte, že jste přihlášeni ke stejnému účtu, který jste použili k nákupu Nomadu (na Google Play).
- Restartujte zařízení
- Někdy je potřeba počkat pár hodin
- Ujistěte se, že aplikace Google Play je aktuální
- Přeinstalujte Nomad (pokud nechcete o nic přijít, nezapomeňte [zálohovat soubory](#where-are-my-projects-located-on-my-device))
- Můžete zkusit znovu provést nákup a podívat se, co se stane (poznámka: stejnou položku nemůžete na stejný účet koupit dvakrát)

:::tip
Můžete mě kontaktovat na <support@nomadsculpt.com>, ale *jediné*, co pro vás budu moci udělat, je potvrdit, zda je s daným e‑mailem spojen nákup.

Pravidelně dostávám hlášení o tom, že se licence po pořízení nového zařízení neaktualizují správně.
Nad platbami a synchronizací účtů nemám žádnou kontrolu, vše zajišťuje Google/AppGallery!

Nakonec se nákup vždy obnoví, ale není jasné, jaké kroky tento proces urychlí.
:::

::: warning
Novější zařízení Huawei nemají přístup ke službám Google.
V takovém případě budete muset aplikaci znovu zakoupit v AppGallery (obchod s aplikacemi Huawei).
:::

### Můžete přeložit nebo opravit [můj-jazyk]? {#locale}
Poměrně snadno mohu přidat další jazyk, ale spoléhám se na překlad pomocí AI, protože je mnohem jednodušší ho udržovat při pravidelných aktualizacích.
Soubory s překlady najdete [zde](https://github.com/stephomi/nomad-translation).

## Funkce {#features}

### Proč se gizmo nepohybuje? {#gizmo-not-moving}
Možná máte [zapnutý pin v levém panelu nástrojů](tools#left-menu-toolbar). 

### Můžeme v Nomadu animovat? {#animate}
Zatím ne. Časová osa, která by umožnila animovat vrstvy, by mohla být zajímavá, ale momentálně není v plánu.  

Do budoucna bych rád podporoval rigging/skinování, ale přináší to několik výzev (zejména interakci s modelovacími nástroji...), takže zatím nic jistého.


### Můžeme dělat pořádné low-poly modelování? {#lowpoly}
Zatím ne.
To není úplně v rozsahu Nomad *Sculpt*, ale možná v budoucnu přidám několik nástrojů.


### Můžeme dělat UV a texturování? {#texturing}
Krátká odpověď: Ano. Dlouhá odpověď: Ne přímo, ale existuje několik způsobů, jak zkombinovat vynikající nástroje Nomadu pro vertex paint s UV a texturami.

* Nomad umožňuje malovat barvu, drsnost a materiálové vlastnosti přímo do vrcholů modelu.
* Nomad umožňuje velmi vysoký počet vrcholů, takže můžete malovat bez starostí o UV.
* Nomad umí načítat textury pro použití ve štětcích, což umožňuje razítkování a malování texturami.
* Nomad umí načítat objekty s předem přiřazenými texturami pro účely renderingu.
* Nomad umí [UV rozbalit](topology.md#uv-unwrap) nízkopolygonální objekty.
* Barvu/drsnost/kovovost lze převést z textur do vrcholů pomocí [voleb pro projekci](topology.md#reproject-to-vertex).
* Barvu/drsnost/kovovost/normály lze péct z vrcholů do textur pomocí [voleb pro baking](topology.md#bake-to-texture)
* Baking a projekce mohou probíhat mezi jednotlivými objekty nebo mnoha objekty, případně mezi nejvyšší a nejnižší úrovní subdivize jednoho objektu, což umožňuje různé workflow pro baking a projekci.
* Po bakeování se při exportu OBJ exportují i textury, které lze vzít do aplikace jako Procreate a malovat přímo do textur.

### Můžu nahrát video otáčejícího se modelu (turntable)? {#video}
Zatím neplánováno, iOS má [funkci nahrávání videa](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados), která se velmi snadno používá.

V iOS to provedete tak, že stáhnete prstem z levého horního rohu a klepnete na tlačítko nahrávání. Po třísekundovém odpočtu menu odsuňte, aby byl vidět Nomad, a použijte funkci turntable. Po dokončení znovu stáhněte prstem z pravého horního rohu a znovu klepněte na tlačítko nahrávání. Video upravte v knihovně fotek a odstraňte přebytečné záběry na začátku a na konci.

### Můžete přidat [oblíbenou-funkci] jako tlačítko na hlavní lištu? {#interface}
Ano, spodní panel nástrojů lze nyní přizpůsobit v nabídce [interface](interface.md) a je možné vytvářet plovoucí panely nástrojů.

### Jaké budou další funkce? {#next-features}
Pro střednědobý/dlouhodobý plán mám spoustu nápadů, ale zatím nevím.  

Opravy chyb a vylepšování stávajících funkcí budou mít vždy vyšší prioritu než přidávání nových.


### Můžeme v Nomadu riggovat? {#rigging}
Ne, ale je to v plánu. Zatím můžete objekty vzájemně parentovat a měnit pivot body, což umožňuje jednoduché pózovatelné modely.

### Můžeme používat více než 4 světla? {#lights}
Ne, to je omezení realtime renderovacího enginu v Nomadu. Dá se to obejít pomocí emisivních objektů a globální iluminace v postprocessingu, jak je ukázáno v [tomto tutoriálu](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Můžeme importovat ZBrush tools? {#zbrush-import}
Ne, ZBrush používá proprietární formát. Měli byste ale být schopni z něj získat alpha mapy a použít je v Nomadu. 

### Proč barvy neodpovídají tomu, co jsem namaloval? Proč v renderu nedosáhnu čistě bílé? {#paint-pbr}
Představte si fotku kusu papíru, fotku stolní lampy a fotku slunce. Starší fotoaparáty a obrazovky z nich prostě udělají všechny „bílé“. Modernější systémy dokážou ukázat rozdíl mezi odraženou bílou papíru, vyzařovaným světlem lampy a super jasem slunce.

Moderní počítačová grafika se snaží fungovat podobně, napodobuje fyziku světla a povrchů. Říká se tomu `Physically Based Rendering` neboli PBR a renderer Nomadu je na něm založený. Výsledek vypadá realisticky a vyváženě, ale často se stává, že jasně namalované barvy vypadají tmavší.

Pokud potřebujete, aby render více odpovídal namalovaným barvám, můžete to napravit jak ne‑PBR, tak PBR způsoby:

Ne PBR:
* `Použijte režim „Unlit“ v nabídce osvětlení`. Barvy se zobrazí přesně tak, jak jsou namalované, ale přijdete o stínování. Hodí se pro rychlé kontroly a grafičtější výstup.
* `Použijte režim „Matcap“ v nabídce osvětlení`. Zvolte jasnější matcap, který je převážně bílý a bez barevného nádechu.

PBR:
* `Použijte neutrální prostředí`. Můžete [změnit prostředí](shading.md#environment) na neutrálnější. Vyhněte se interiérovým prostředím, protože bývají více barevná. Dejte přednost dennímu venkovnímu nebo studiovému prostředí.
* `Zvyšte osvětlení`. Kdybyste fotili bílý papír v tmavé místnosti, prostě byste přidali víc světla. U environment light zvyšte posuvník exposure, dokud barvy nezačnou působit správně, nebo přidejte více jednotlivých světel s vyšší intenzitou.
* `Zvyšte expozici kamery`. Kdyby v tmavé místnosti nešlo přidat světla, mohl by fotoaparát nechat déle otevřenou závěrku nebo použít citlivější ISO. V Nomadu dosáhnete podobného výsledku v postprocessingu. Jděte do post process, zapněte ho, sjeďte k tone mappingu, zapněte ho a zvyšte posuvník exposure, dokud barvy nebudou působit správně.
* `Použijte emisivní barvu`. V nabídce materiálu můžete pod texturami zapnout „emissive“, což způsobí, že objekt bude vypadat jako zdroj světla. Pokud v nastavení postprocessingu zapnete global illumination, bude vrhat světlo na ostatní objekty ve scéně. Můžete také pro daný materiál zapnout „unlit“, čímž dosáhnete podobného vzhledu i bez textury.

## Pády aplikace {#crashes}

### Aplikace spadne, když uložím nebo remeshuji model! {#crash-remesh}
Vašemu zařízení dochází paměť (RAM).  
Abyste snížili využití paměti ve scéně, můžete použít některé volby [Topology](topology.md) ke snížení počtu polygonů.

::: tip RAM/Úložiště
Důležité je množství RAM, ne úložiště (to je obvykle mnohem větší).
:::


### Aplikace spadne, když načtu svůj projekt! {#crash-load}
Pokud je soubor malý, můžete mi ho poslat a já se na něj podívám (e‑mailem na <support@nomadsculpt.com>).

Jinak zařízení pravděpodobně dochází RAM.

- Ujistěte se, že jste zavřeli všechny ostatní otevřené aplikace v zařízení.
- V Nomadu začněte nový projekt místo toho, abyste měli nějaký projekt právě otevřený.
- Pokud to stále padá, jediným řešením je načíst [soubor projektu](#where-are-my-projects-located-on-my-device) na zařízení s větší pamětí.

::: tip
Na desktopovém prohlížeči můžete zkusit načíst soubor [na této adrese](https://nomadsculpt.com/demo_save/) a po zjednodušení scény ho znovu exportovat.

Některé prohlížeče omezují množství RAM, které může zabrat jedna karta, takže je možné, že tato technika nebude fungovat.

Pokud váš projekt používá [Layers](layers.md), možná je budete chtít sloučit, abyste snížili využití paměti.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Aplikace spadne, když spustím Nomad! {#crash-start}
Pokud spadne při načítání, znamená to, že Nomad má problém s nějakým souborem ve složce Nomad.

Většinou se to stane proto, že je projekt příliš velký a bohužel překročí limit RAM.

Najděte [složku Nomad](#where-are-my-projects-located-on-my-device) a pak přejmenujte nebo přesuňte některé soubory, abyste našli viníka.

Nejprve zkuste přejmenovat `settings.json`. Tím se zastaví načítání posledního projektu.

Pokud to nepomůže, zkuste některé nedávné soubory přesunout mimo jejich příslušné složky se zdroji (`projects`, `matcaps`, `environments` atd.).

Můžete také přejmenovat samotné složky, aby je Nomad úplně ignoroval.
Pokud přejmenujete nebo přesunete všechny soubory ve složce Nomad, bude to mít stejný efekt jako čistá instalace.

::: tip
Když Nomad při startu načítá soubor, vždy ho přesune do složky `can_be_deleted/`.
Pokud se operace podaří, přesune ho zpět do původní složky.

Pokud spadne dřív, než se načítání dokončí, Nomad se při příštím spuštění spustí úspěšně, protože složku `can_be_deleted/` ignoruje.

Pokud si myslíte, že by se načtení mohlo podařit, můžete tento soubor jednoduše zkusit načíst znovu.
:::