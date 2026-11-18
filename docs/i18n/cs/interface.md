# ![](/icons/sliders.webp) Nabídka Rozhraní {#interface-menu}

Tato nabídka obsahuje spoustu možností, jak si přizpůsobit rozhraní Nomadu.

![](/images/interface_overview2.webp)

Nomad si můžete přizpůsobit opravdu do hloubky, tato nabídka je rozdělená do 5 karet: Rozhraní, Zkratky, Gesto, Vazby, Ladění.

![](/images/interface_menu.webp)


::: tip
Tato stránka popisuje nabídku Rozhraní, ne samotné rozhraní! Rozhraní jako celek je popsané v části [Začínáme](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Rozhraní {#interface}

Karta Rozhraní řídí barvy, velikost a rozložení uživatelského rozhraní Nomadu. Má dvě podkarty, `Vzhled` a `Rozložení`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Barvy {#presets}

![](/images/interface_presets.webp)

Podkarta `Vzhled` začíná sadou barevných přednastavení rozhraní. Klepnutím jedno použijete a pak ho doladíte níže uvedenými možnostmi.

#### Akcent a Základ {#color-widgetcolor-base}
Hlavní barvy rozhraní: `Akcent` pro vybraná tlačítka a výplň posuvníků, `Základ` pro panely.

#### Krytí textu {#text-opacity}
Zjemní text a ikony vůči panelům.

#### Přepínače, Zaškrtávací pole, Karty {#high-contrast-button}
Styl přepínacích tlačítek (`Jemné` nebo `Plné`), zaškrtávacích polí (`Obrys`, `Akcent` nebo `Výplň`) a karet (`Podtržení`, `Jemné` nebo `Plné`).

#### Barevné nástroje {#colored}
Obarví ikony podle kategorie, např. všechny nástroje masky jsou hnědé, nástroje řezu červené, nástroje zploštění zelené atd.

#### Stín panelů {#material-color-preview}
Panely vrhají stín, aby vystoupily ze scény.

#### Průhledný panel {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Když je zapnutý, objeví se další možnosti, kterými řídíte vzhled nabídek a panelů v Nomadu: `Odstín panelů` nastaví jejich barvu, `Intenzita rozostření` jak moc se rozostří scéna za nimi a `Sklo` přidá lom a odlesky na okrajích, nejvíc viditelné při slabém rozostření.

::: tip
Na malých zařízeních se vyplatí nastavit odstín panelů skoro na bílou, průhlednou, se slabým rozostřením, aby nabídky nezakrývaly scénu.
:::

#### ![](/icons/reset.webp) Obnovit vzhled {#reset-style}
Vrátí všechny možnosti vzhledu na výchozí hodnoty.

### ![](/icons/panel_detach.webp) Rozložení {#layout}

Podkarta `Rozložení` určuje, kde co je a jak je to velké.

#### Nástroje {#toolbox}

Možnosti panelu nástrojů vpravo v rozhraní Nomadu.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Změnit velikost {#ui-resize-corner}

Přepne úchyt pro změnu velikosti v dolním rohu panelu nástrojů.

##### Skryto {#hidden}
Ikona panelu nástrojů v horní liště normálně přepíná mezi jedním dlouhým sloupcem a vícesloupcovým seznamem nástrojů. S touto možností přepíná mezi vícesloupcovým seznamem a skrytím.

##### Resetovat pořadí {#reset-order}
Vrátí výchozí nástroje v panelu nástrojů do výchozího pořadí. Vlastní ikony zůstanou v panelu nástrojů na konci seznamu.

#### Horní lišta {#rows-auto-1}
`Responzivní` určuje, co horní lišta udělá, když se nevejde na obrazovku, což se týká hlavně malých obrazovek: `Víceřádkový` zalomí nabídky do více řádků, `Posun` ponechá jeden řádek, který můžete posouvat.

#### Zrcadlit horní panel {#mirror-top-bar}
Obrátí pořadí nabídek v horní liště.

#### Zrcadlit boční panely {#mirror-side-bars}
Prohodí boční panely, takže panel nástrojů je vlevo a možnosti nástroje vpravo.

#### Zrcadlit dolní panel {#mirror-bottom-bar}
Přesune spodní lištu do pravého dolního rohu a obrátí pořadí tlačítek.

#### ![](/icons/move.webp) Přetahovat panel {#drag-panel}
Plovoucí panel se vždy přesouvá tažením za jeho lištu, tato možnost umožňuje táhnout i za jeho tělo. V režimu `Auto` prst nebo stylus panel přesune jen tehdy, když je tah spíš vodorovný než svislý, takže svislým tahem obsah dál posouváte. Nastavte `Ano`, chcete-li táhnout i myší, v libovolném směru.

#### ![](/icons/pencil.webp) Použít Nomad dialog {#use-nomad-dialog}
Při zadávání názvu nebo hodnoty zobrazí vlastní textový dialog Nomadu místo nativního.

#### ![](/icons/stylus.webp) Tečka při najetí kurzorem {#hover-dot}
Zobrazí v UI malou tečku, když je detekován stylus ve vznosu.

#### ![](/icons/help.webp) Nápověda při najetí {#help-popup-on-hover}

Na zařízeních, která podporují najetí kurzorem, určuje, zda se kontextová nápověda Nomadu označená ikonou ![](/icons/help.webp) zobrazí při najetí, nebo jen po klepnutí.

#### Celková škála {#overall-scale}
Násobitel velikosti všech prvků UI.
#### Šířka panelu {#panel-width}
Šířka nabídek a panelů.
#### Škála písma {#font-scale}
Změní velikost písma.
#### Vertikální rozestupy {#vertical-spacing}
Rozestupy mezi prvky v nabídkách a panelech.
#### Vertikální rozestupy (vlevo) {#vertical-spacing-left}
Rozestupy mezi prvky v levém panelu nástrojů.

#### Posuny okrajů {#edge-offset}
Tyto hodnoty měňte jen tehdy, když máte potíže s tlačítky na okrajích obrazovky. Pokud jsou posuvníky vypnuté, Nomad použije hodnoty bezpečných oblastí, které vrací samotné zařízení.

::: tip
Když přecházíte s Nomadem na nové zařízení (např. z iPhonu 12 na iPhone 15), nezapomeňte vrátit možnosti okrajů na výchozí hodnoty!
:::

#### ![](/icons/reset.webp) Obnovit rozložení {#reset-layout}
Vrátí všechny možnosti rozložení na výchozí hodnoty.

## ![](/icons/window.webp) Zkratky {#shortcuts}

Karta Zkratky určuje, která rychlá tlačítka se zobrazí kolem viewportu, a umožňuje vytvořit si vlastní plovoucí panely nástrojů.

### Boční panel {#side-bar}
Rychlá tlačítka nástrojů v dolní části levého bočního panelu: `Hladit`, `Maska`, `Skrýt`, `SkupinaPovrch` a `Gizmo`. Přetažením změníte jejich pořadí.

### Spodní lišta {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Klepnutím na zkratku ji přidáte do spodní lišty, nebo ji z ní odeberete. Tyto jsou zapnuté ve výchozím stavu:
* `Zpět` - vrátí předchozí operaci
* `Vpřed` - obnoví naposledy vrácenou operaci
* `Sólo` - Dočasně skryje všechny ostatní objekty, viditelný zůstane jen vybraný. Dalším stiskem obnovíte všechny objekty.
* `Rentgen` - Dočasně zprůhlední všechny ostatní objekty, plný zůstane jen vybraný. Dalším stiskem obnovíte výchozí materiály.
* `Voxel` - Přesíťuje aktuální objekt s naposledy použitým voxelovým rozlišením. Dlouhým stiskem nebo tahem nahoru zobrazíte posuvník rozlišení a přepínač ostrých hran.
* `Mřížka` - Přepne mřížku zobrazení. Dlouhým stiskem nebo tahem nahoru můžete změnit barvu a krytí mřížky.
* `Drát` - Přepne překryv drátového modelu. Dlouhým stiskem nebo tahem nahoru můžete změnit barvu a krytí drátového modelu.
* `Kontrola` - zobrazí vlastnosti sítě, jako jsou UV, zapečené textury a další, na pozadí Nomadu.
* `SkupinaPovrch` - Přepne překryv skupin ploch, více v části [Nástroje->Skupina ploch](tools.md#facegroup)

K dispozici jsou i další často používané zkratky: `Obrys`, `Projekce` (perspektivní nebo ortografická), `MatCap`, `DynTopo` a tlačítka [multirezoluce](topology.md#multiresolution) `Poddělení`, `Opačný` a úrovně.

#### ![](/icons/more.webp) Vazby {#bindings-list}

Do spodní lišty můžete přes tlačítko vazeb přidat téměř jakoukoli funkci Nomadu; tlačítko ukazuje, kolik zkratek lišta obsahuje. Po klepnutí na tlačítko se zobrazí nabídka vazeb:

![](/images/interface_bindings_search.webp)

Hledat můžete podle kategorie pomocí ikon nahoře, nebo funkce najít podle názvu ve vyhledávacím poli. Klepnutím na funkci ji přidáte do panelu nástrojů. Dalším klepnutím ji odeberete.

#### ![](/icons/eye_open.webp) Viditelný {#order}

Zobrazí nebo skryje celou spodní lištu.

#### ![](/icons/reset.webp) Resetovat {#reset}

Resetovat vrátí spodní lištu do výchozího nastavení.

### Plovoucí okna {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Klepnutím na + přidáte plovoucí panel nástrojů. Nebude viditelný, dokud neklepnete na tlačítko vazeb a nepřidáte do něj nějaké zkratky; pak ho můžete zviditelnit.

Panelů nástrojů můžete vytvořit mnoho, každý má řádek s těmito možnostmi:

* Tažením za úchyt vlevo na řádku změníte pořadí panelů nástrojů.
* `Název` - Název panelu nástrojů.
* `Viditelný` - Přepne viditelnost panelu nástrojů.
* `Lišta` - Zobrazí na panelu nástrojů záhlaví.
* `Minimalizované` - Ponechá panel nástrojů na obrazovce, i když je rozhraní minimalizované.
* `Vazby` - Zobrazí okno vazeb, ve kterém vyberete funkce, které chcete do panelu přidat nebo z něj odebrat.
* `Smazat` - Smaže panel nástrojů.


## ![](/icons/gesture.webp) Gesto {#gesture}
Nabídka Gesto určuje, jak Nomad ovládáte prstem, stylusem, myší a trackpadem.

![](/images/interface_gesture.webp)

### Možnosti gest {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad může omezit operace podle vstupního zařízení. Například tažení prstem může jen pohybovat kamerou, zatímco tažením stylusem jen sochat. Pokud máte myš nebo trackpad, můžete jim také přiřadit konkrétní operace.

Každý řádek je jedna operace: přepínači `Prst`, `Stylus` a `Myš` zvolíte, které vstupy ji mohou provádět.

* `Kamera` - Pohyb kamerou.
* `Úprava uzlu` - Tažení úchytů vykreslených na plátně, například při úpravě primitiva, křivky, opakovače nebo světla.
* `Sochařit` - Sochání štětci. Nástroje, které mají vlastní řádek níže, se řídí tím řádkem.
* `Vybrat objekt` - Klepnutím na objekt ho vyberete.
* `Výběr materiálu` - Dlouhým stiskem na plátně převezmete barvu nebo materiál pod kurzorem. Funguje jen tehdy, když má aktuální štětec zapnuté malování.
* `Na dotek` - Zkratky klepnutím u nástrojů jako Maska, Skrýt a SkupinaPovrch (viz níže).
* `Barva` - Nástroje Malovat a Rozmazat.
* `Maska` - Nástroj Maska.
* `Plocha` - Nástroje Skrýt a SkupinaPovrch.
* `Vytvořit` - Nástroje Trubka, Soustruh a Vložit.
* `Řez` - Nástroje Oříznout, Rozdělit a Projekt.
* `Vybrat` - Nástroje Vybrat a Měřit.
* `Gizmo` - Nástroje Gizmo a Mřížka.
* `Transformace` - Nástroje Přeměnit a Uspořádat.

::: tip
Na tabletu je běžné nastavení, že sochat a malovat smí jen stylus a prsty zůstanou pro kameru. Dlaň ani zatoulaný prst pak na modelu nikdy nezanechají tah.
:::

### ![](/icons/tool_smooth.webp) Prst vždy vyhlazuje {#finger-always-smooths}
Když je zapnuto, prst při aktivním sochařském nástroji vždy vyhlazuje, ať je zvolený jakýkoli štětec. Zapnutím se z řádku `Sochařit` odebere `Prst`, takže stylus sochá a prst vyhlazuje.

### Povolit tah mimo objekt {#allow-air-stroke}
Tah může začít, i když kurzor nejdřív dopadne mimo síť. Zvolte nástroje, pro které to platí: `Nástroj` (všechny ostatní štětce), `Hladit`, `Maska` a `Skrýt`. Funguje to jen u vstupů, které mohou sochat, ale nehýbou kamerou, takže tato tlačítka jsou vypnutá, dokud některý ze vstupů takto nenastavíte.

### ![](/icons/stroke.webp) Přichycení tahu {#stroke-snap}
Podržte ukazatel na konci tahu v klidu a tah se přichytí na rovnou čáru nebo hladkou křivku. Dalším tažením přichycený tah otáčíte a měníte jeho měřítko kolem počátečního bodu.

`Doba podržení` nastaví, jak dlouho musíte vydržet v klidu, než se tah přichytí nebo než se tvar přepne do úprav.

### ![](/icons/stylus.webp) Použijte extra vstupní vzorky {#use-extra-input-samples}
Použije dodatečné vstupní vzorky, které hlásí zařízení. Vypněte to, pokud jsou vaše tahy zubaté nebo se tlak chová nesprávně. Na iOS se tato možnost nezobrazuje.

### ![](/icons/tool_mask.webp) Maska {#mask}

![](/images/interface_gesture_mask.webp)

`Zkratky jedním dotykem` - Zapne následující zkratky jedním klepnutím, aniž byste museli držet tlačítko masky. Umožní tato gesta:
* klepnutím na pozadí masku invertujete
* klepnutím na maskovanou oblast masku rozostříte
* klepnutím na nemaskovanou oblast masku zaostříte

#### Dlouhý stisk {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Dlouhý stisk s nástrojem Maska přepíná mezi štětcem masky a lasem (SelMask):
* `Dlouhý stisk - Sochařit` - Dlouze stiskněte a pokračujte v tažení: tah se nakreslí druhým režimem a na konci tahu se vrátí ten předchozí.
* `Dlouhý stisk - Přepnout` - Dlouze stiskněte a pusťte bez pohybu, čímž přepnete mezi oběma režimy.

### ![](/icons/tool_smooth.webp) Hladit {#smooth}
`Dlouhý stisk - Laso` - Dlouhý stisk s nástrojem Hladit přepne na dobu výběrového tahu na nástroj Vybrat.

### ![](/icons/tool_hide.webp) Skrýt {#hide}
![](/images/interface_gesture_hide.webp)

`Zkratky jedním dotykem` zapne u nástroje Skrýt tyto zkratky:
* Klepnutím na skupinu ploch ji skryjete
* Klepnutím do prázdného prostoru invertujete skryté polygony

### ![](/icons/finger3.webp) Tři prsty {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Pokud vaše zařízení podporuje gesta třemi prsty, nastavte pro toto gesto zkratky.

Matice možností umožňuje přiřadit svislému a vodorovnému tažení samostatné zkratky, nebo zvolit `Ne` a gesto nepoužít. Pokud je stejné gesto zvolené pro 2 možnosti, jedna se vypne a její název se přeškrtne.

* `Otočte osvětlení` - Otáčí prostředím, světly a matcapem.
* `Poloměr nástroje` - Mění poloměr nástroje.
* `Intenzita nástroje` - Mění intenzitu nástroje.

### ![](/icons/fingerprint.webp) Historie 2/3 {#history-23}
`Historie zkratek` - když je zapnuto, jsou aktivní tato gesta:
* Zpět - klepnutí 2 prsty
* Vpřed - klepnutí 3 prsty

`Dlouhý stisk` - když je zapnuto, podržením 2/3 prstů rychle vracíte/obnovujete kroky.

### ![](/icons/mouse.webp) Kolečko myši {#mouse-wheel}
`Rychlost (3D přiblížení)` nastaví, jak rychle kolečko přibližuje pohled, a `Rychlost (2D rozhraní)`, jak rychle posouvá nabídky a panely. Tlačítko mínus vedle každého posuvníku obrátí směr.

### ![](/icons/fingerprint.webp) Trackpad {#trackpad}
Na Macu `Dva prsty` určuje, co dělají dva prsty na trackpadu. Sevření prstů vždy přibližuje a otočení prstů vždy naklání pohled.
* `Vypnuto` - Posouvání dvěma prsty přibližuje, jako kolečko myši. Prsty se nečtou jednotlivě.
* `Posun` - Dva prsty posouvají pohled a zvednutím jednoho z nich pohled otáčíte. Stejně jako na tabletu.
* `Otáčení` - Dva prsty otáčejí pohled a zvednutím jednoho z nich pohled posouváte.

### Přístupnost {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Asistenční okno` zobrazí plovoucí panel nástrojů pro tažení, sevření, naklánění a ovládání kamery.

### Kamera {#camera}
Zkratka do nabídky `Kamera` (možnosti kamery bývaly tady, ale přesunuly se do nabídky Kamera).

### Dvojité poklepání tužky -> Vazby {#pencil-tap}

Zkratka do nabídky `Vazby`, kde nastavíte, co dělá dvojité poklepání tužkou. Mimo iOS se jmenuje `Tlačítko tužky → Vazby` a týká se tlačítka stylusu.

### Vyloučení dlaně {#palm-rejection}
Na telefonech a tabletech ignoruje doteky, jejichž plocha je větší než `Maximální práh velikosti`, například dlaň opřenou o obrazovku. Nemusí fungovat na každém zařízení, takže pokud máte s plátnem potíže, vypněte to.


## ![](/icons/keyboard.webp) Vazby {#bindings}
Klávesové zkratky a zkratky tlačítek nastavíte v nabídce Vazby:

![](/images/interface_bindings.webp)
Téměř všechny funkce Nomadu lze přiřadit klávesovým zkratkám, pokud má zařízení klávesnici, nebo dalším tlačítkům na stylusu, či dokonce herním ovladačům.

Vazbu vytvoříte tak, že klepnete na obdélník vedle funkce a stisknete klávesu/tlačítko.

Funkce najdete pomocí ikon kategorií nahoře, nebo podle názvu ve vyhledávacím poli.

Jednotlivé vazby můžete vypnout zaškrtávacím polem vedle názvu vazby. Dlouhým stiskem zaškrtávacího pole a tažením změníte pořadí seznamu.

Když dvě zapnuté vazby používají stejnou zkratku, objeví se vedle nich ikona ![](/icons/help.webp), která vypíše kolidující funkce.

### ![](/icons/more.webp) Kontextová nabídka {#context-menu}
Ikona ![](/icons/more.webp) za každou vazbou otevře kontextovou nabídku:

![](/images/interface_bindings_context.webp)

* `Klonovat` - Naklonuje vazbu, například abyste funkci dali druhou zkratku.
* `Resetovat` - Resetuje vazbu
* `Smazat` - Smaže vazbu. Jde to jen tehdy, když má funkce víc než jednu vazbu.

Pod nimi mají některé vazby další možnosti:

* `Režim kláves` - U zkratek nástrojů a rychlých zkratek (Maska, Hladit, Gizmo, Skrýt, SkupinaPovrch, Přidat/Odebrat) určuje, jak stisk klávesy přepíná nástroje. `Auto` použije výchozí nastavení z možností [Rozšířené](#advanced).
  * `Držet` - Držte klávesu, chcete-li nástroj použít, a pusťte ji, chcete-li se vrátit k předchozímu nástroji.
  * `Přepnout` - Jedním stiskem nástroj přepnete.
  * `Rychlý stisk` - Podržením nástroj použijete dočasně, rychlým stiskem se na něj přepnete.
* `Návrat po uvolnění` - U rychlých zkratek určuje, zda se po puštění držené klávesy vždy vrátíte k předchozímu nástroji, i když už byl tento nástroj aktivní.
* `Přepnout předchozí nástroj` - U zkratek nástrojů: stisk zkratky aktuálního nástroje přepne zpět na poslední nástroj. Vyžaduje `Režim kláves` na `Přepnout` nebo `Rychlý stisk`.
* `Pozice` - U zkratek plovoucích oken určuje, zda se okno otevře tam, kde bylo (`Zachovat předchozí`), nebo pod kurzorem (`Na kurzoru`).
* `Posun (při uvolnění)` / `Přiblížení (při uvolnění)` - U vazeb přiblížení a posunu kamery: po puštění klávesy přepne na tu druhou.
* Směr tažení - U `Otočit osvětlení`, `Poloměr nástroje` a `Intenzita nástroje` zvolte vodorovné nebo svislé tažení.
* `Synchronizovat` - U funkcí, které přidávají, klonují nebo instancují objekty, určuje, zda se výsledek synchronizuje. Ve výchozím stavu se použije hodnota synchronizace nastavená v nabídce Scéna.
* `Na pozadí` - U rychlých zkratek Hladit a Maska: tažením po pozadí se drženou klávesou nakreslíte laso, výběrové laso u Hladit a laso masky u Maska.
* `Vynutit kameru` - U vazeb kamery pohne kamerou, i když stejnou zkratku používá jiná vazba, typicky zkratka nástroje nebo Přidat/Odebrat.
* `Lineární náklon` - U vazby naklánění naklání vodorovným, svislým nebo úhlopříčným tažením místo pohybu kolem otočného bodu.

::: tip
S `Rychlý stisk` zvládne jedna klávesa obojí: podržte ji pro rychlé vyhlazení nebo maskování a po puštění jste zpět u svého štětce, nebo na ni klepněte a na tom nástroji zůstanete.
:::

### ![](/icons/cog.webp) Rozšířené {#advanced}
Ve spodní části nabídky Vazby je nabídka ozubeného kolečka s pokročilými možnostmi:

![](/images/interface_bindings_advanced.webp)

* `Rychlé zkratky` - Výchozí `Režim kláves` a `Návrat po uvolnění` pro zkratky Maska, Hladit, Gizmo, Skrýt, SkupinaPovrch a Přidat/Odebrat.
* `Nástrojové zkratky` - Výchozí `Režim kláves` a `Přepnout předchozí nástroj` pro zkratky nástrojů. S `Přepnout předchozí nástroj` můžete jednou klávesou neustále přepínat mezi dvěma nástroji.
* `Okno zkratek` - `Režim kláves` zkratek, které zobrazují plovoucí okna.
* `Překlopit zoom Y` - Obrátí svislý směr tažení při přibližování pomocí vazby.
* `Lineární náklon` - Naklání pohled vodorovným, svislým nebo úhlopříčným tažením místo pohybu kolem otočného bodu.
* `SpaceMouse` - Zapne podporu 3Dconnexion SpaceMouse. Na některých systémech se objeví další možnosti: čím pohybuje (`Objekt`, `Kamera`, `První osoba`, `Dron`), `Automaticky aktualizovat pivot`, který při zahájení pohybu přesune otočný bod na povrch pod kurzorem, a rychlosti `Přesun`, `Zvětšování` a `Rotace`.
* `Mrtvé zóny (drift)` - Pro ovladače `Gamepad`, `Joystick` a `Tlačítko`. Zvyšte tyto hodnoty, pokud se kamera hýbe, i když na ovladač nesaháte.
* `Poloměr nástroje` - Jak tažení s vazbou poloměru mění velikost štětce (`Kruh`, `Střed` nebo `dx`) a o kolik vazby poloměru při každém stisku přičtou (v pixelech) nebo vynásobí.
* `Intenzita nástroje` - O kolik vazby intenzity při každém stisku přičtou nebo vynásobí.
* `Kamera - Rychlost` - Rychlost `Přesun` a `Rotace` u vazeb, které posouvají a otáčejí pohled.
* `Resetovat přiřazení kláves` - vrátí všechny vazby na výchozí hodnoty.
* `Resetovat pořadí` - obnoví výchozí pořadí seznamu vazeb.


## Zobrazení klávesových zkratek ⌘ na iOS {#ios-keyboard-shortcuts-display}

Na zařízeních iOS s klávesnicí podržte klávesu ⌘ (cmd) a zobrazí se seznam zkratek.

Podpora klávesnice na Androidu je zatím trochu experimentální.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Ladění {#debug}
V této nabídce jsou uložené některé experimentální a ladicí možnosti. Mnoho z nich byste měli nechat ve výchozím nastavení a měnit je až po konzultaci s podporou Nomadu. Ikony nahoře přeskočí na jednotlivé sekce.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalizace UV` - Nomad normalizuje UV vybrané sítě do dlaždice [0-1].

### ![](/icons/sun.webp) Stínování {#render}
* `Zapisovat hloubku lomu (vzadu)` - Zadní strana sítí s lomem se zapíše do hloubkového bufferu.
* `Hladké normály vážené úhlem` - Úprava fungování hladkého stínování, která v některých případech zabrání záhybům.

### ![](/icons/speed.webp) Cílové FPS {#target-fps}
Když je vypnuto, Nomad synchronizuje počet snímků za sekundu s obnovovací frekvencí displeje.

Když je zapnuto, můžete nastavit, kolik snímků za sekundu bude Nomad vykreslovat.

### ![](/icons/window.webp) Rozhraní {#debug-interface}
* `Nástroje: zobrazit vše` - Nomad skrývá nástroje, které nejsou pro aktuální výběr relevantní, např. na nedokončených primitivech jsou skryté všechny sochařské štětce. Tato možnost vypnuté nástroje místo skrytí jen ztlumí.

Ostatní možnosti rozhraní, které tu dřív byly, jsou teď na kartě [Rozhraní](#interface).

### ![](/icons/turntable.webp) Otočný stůl {#gif-turntable}
Nomad umí exportovat animovaný gif s otočným stolem. Kvůli omezením formátu gif je kvalita nízká. Lepší bývá nahrávání obrazovky.

* `Doba trvání` - jak dlouho v sekundách bude otočný stůl trvat
* `Maximální vzorkování rámců` - Mnoho vysoce kvalitních efektů vykreslování Nomadu vzniká skládáním několika snímků dohromady. Tento posuvník nastaví, kolik snímků se složí, a jeho zaškrtávací pole ho zapíná nebo vypíná.
* `Střed otáčení` - kolem čeho se kamera otáčí: `Zachovat aktuální` ponechá aktuální otočný bod, `(0, 0, 0)` použije střed světa, `Scéna` střed scény.
* `Průhledné pozadí` - Použije pro gif průhlednost. Gif podporuje jen 1bitovou průhlednost, takže okraje mohou být ošklivě zubaté.
* `Exportovat (GIF)` - spustí export gifu.

### ![](/icons/postprocess.webp) Postproces {#post-process}
* `Filtr` - Ladicí možnost
* `Formát` - Ladicí možnost
* `Znovu použít buffery` - Ladicí možnost

### ![](/icons/ram.webp) Výkon {#performance}
* `Více vláken: obecné` - Ladicí možnost
* `Více vláken: sochání` - Ladicí možnost
* `Kreslit opakování instancemi` - Vykreslí všechny kopie opakovače jediným voláním vykreslení. Ladicí možnost.

### ![](/icons/star.webp) Funkce {#feature}
* `nom: komprimovat multirezoluci` - Zmenší projekty a exporty Nomadu, které používají multirezoluci. Takové soubory nelze otevřít ve starších verzích Nomadu. Tato možnost může být v budoucnu odstraněna a zapnuta natrvalo.
* `Obrátit diagonálu čtyřúhelníku (klepnutím)` - Ladicí možnost

### ![](/icons/bug.webp) Ladění {#dev}
* `Záznamy` - Otevře okno se záznamy
* `Zaznamenávat události` - Zapisuje události ukazatele (prst, stylus, myš) do okna záznamů, abyste mohli prozkoumat problémy se vstupem.
* `FPS` - přidá do statistik viewportu počítadlo snímků za sekundu.
* `Okno hodnocení aplikace` - Ladicí možnost, na iOS a Androidu.

### ![](/icons/image.webp) Vlastní ikony {#custom-icons}
Nahradí ikony Nomadu vašimi vlastními soubory png.
* `Importovat ikony` - Importuje soubory png do `tmp_session/icons`. Každý nahradí základní ikonu se stejným názvem. Po restartu Nomadu se zahodí.
* `Exportovat ikony nástrojů` - Zkopíruje základní ikony `tool_<tool>.png` do `tmp_session/icons`, aniž by cokoli přepsal. Tam je můžete upravit a použít pomocí `Znovu načíst ikony`.
* `Znovu načíst ikony` - Použije ikony z `tmp_session/icons`.

### Quad přesíťování {#quad-remesh}
Možnosti quad přesíťování už v této nabídce nejsou: viz [Quad přesíťování](topology.md#quad-remesh-instant) v nabídce Topologie a nástroj [Quad Remesher](tools.md#quad-remesher).

### Vytvořit náhledy obchodu {#make-store-thumbnails}
Vyrenderuje snímky obrazovky ve velikostech vhodných pro iOS App Store.
