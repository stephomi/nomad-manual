# ![](/icons/interface.webp) Nabídka rozhraní {#interface-menu}

Tato nabídka ovládá mnoho možností pro přizpůsobení rozhraní Nomadu. 

![](/images/interface_overview2.webp)

Nomad lze přizpůsobit do poměrně velké hloubky, tato nabídka je rozdělena do 4 sekcí: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Tato stránka je o nabídce rozhraní, ne o samotném rozhraní! Celkové rozhraní je popsáno v [Začínáme](gettingstarted.md).
:::

## Rozhraní {#interface}

Sekce Interface vám umožní přidávat zkratky, vytvářet plovoucí panely nástrojů a ovládat barvu, velikost a vzhled uživatelského rozhraní Nomadu.

![](/images/interface_overview3.webp)

### Přidat zkratky (dole)… {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Spodní panel nástrojů má ve výchozím nastavení povoleny tyto zkratky:
* `Undo` - vrátí zpět předchozí operaci
* `Redo` - obnoví dříve vrácenou operaci
* `Solo` - Dočasně skryje všechny ostatní objekty a ponechá viditelný pouze vybraný. Opětovným stiskem obnovíte všechny objekty.
* `X-ray` - Dočasně učiní všechny ostatní objekty poloprůhlednými a ponechá pouze vybraný objekt plný. Opětovným stiskem obnovíte výchozí materiály.
* `Voxel remesh` - Přeremeshuje aktuální objekt pomocí naposledy použitého voxelového rozlišení. Dlouhé podržení nebo přejetí nahoru zobrazí posuvník rozlišení a přepínač ostrých hran.
* `Grid` - Přepne zobrazení mřížky. Dlouhé podržení nebo přejetí nahoru umožní změnit barvu a neprůhlednost mřížky.
* `Wireframe` - Přepne překryv drátového modelu. Dlouhé podržení nebo přejetí nahoru umožní změnit barvu a neprůhlednost drátového modelu.
* `Inspector` - umožní zobrazit vlastnosti vaší sítě, jako jsou UV, vypálené textury a další vlastnosti, překryté na pozadí Nomadu.
* `Face Group` - Přepne překryv facegroup, více informací v [Tools->FaceGroup](tools.md#facegroup) 

Další běžně používané zkratky jsou dostupné z této nabídky, mnohem více jich lze najít v tlačítku bindings.

#### ![](/icons/more.webp) Přiřazení {#bindings-list}

Téměř každou funkci Nomadu lze přidat na panel zkratek pomocí tlačítka bindings. Po kliknutí na tlačítko se zobrazí nabídka bindings:

![](/images/interface_bindings_search.webp)

Můžete vyhledávat podle kategorií pomocí ikon nahoře nebo použít vyhledávací pole k nalezení funkcí podle názvu. Kliknutím na funkci ji přidáte na panel nástrojů. Opětovným kliknutím ji odstraníte.

#### ![](/icons/list.webp) Pořadí {#order}

Zobrazí seznam zkratek. Dlouhým stiskem a tažením můžete zkratky přeuspořádat.

#### ![](/icons/reset.webp) Obnovit {#reset}

Reset obnoví spodní panel nástrojů do výchozího nastavení.

### Přidat zkratky (okno)… + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Kliknutím na + přidáte plovoucí panel nástrojů. Nebude viditelný, dokud nekliknete na tlačítko bindings a nepřidáte do něj nějaké zkratky, poté jej můžete zviditelnit. 

Můžete vytvořit mnoho panelů nástrojů, každý panel má v této nabídce následující možnosti:

* ![](/icons/checked.webp) `Visible` - Přepne viditelnost panelu nástrojů
* ![](/icons/more.webp)`Bindings` - Zobrazí okno bindings pro výběr funkcí k přidání nebo odebrání z panelu nástrojů.
* ![](/icons/list.webp)`Order` - Zobrazí nabídku pro změnu pořadí panelu nástrojů.
* ![](/icons/reset.webp) `Reset` - Obnoví panel nástrojů do výchozího stavu.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Přepne úchyt pro změnu velikosti v pravém dolním rohu panelu nástrojů.
* ![](/icons/sort_down.webp) `Collapsable` - Přepne úchyt pro sbalení v pravém horním rohu.
* ![](/icons/trash.webp) `Delete` - Smaže panel nástrojů.

### Panel nástrojů {#toolbox}

Možnosti pro nabídku nástrojů na pravé straně rozhraní Nomadu.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Roh změny velikosti UI {#ui-resize-corner}

Přepne úchyt pro změnu velikosti v dolním rohu panelu nástrojů.

#### Skryté {#hidden}
Normálně ikona toolboxu v horní liště přepíná mezi dlouhým jednoduchým sloupcem nebo vícesloupcovým seznamem nástrojů. Tato možnost přepíná mezi vícesloupcovým seznamem nebo skrytím.

#### Barevné {#colored}
Barevně odliší ikony podle kategorie, např. všechny maskovací nástroje jsou hnědé, nástroje pro dělení červené, nástroje pro zarovnání zelené atd.

#### Řádky: Auto (>1) {#rows-auto-1}

#### Obnovit pořadí {#reset-order}
Obnoví výchozí nástroje v toolboxu do výchozího pořadí. Vlastní ikony zůstanou v toolboxu na konci seznamu.


### Předvolby {#presets}

![](/images/interface_presets.webp)

Sbírka barevných předvoleb pro rozhraní.

#### Tlačítko s vysokým kontrastem {#high-contrast-button}
Alternativní styl tlačítek, který je činí viditelnějšími, když jsou aktivní. Pokud je nastaveno na Auto, Nomad použije tento režim, když je barevný kontrast UI mezi zapnuto/vypnuto nízký.

#### Barevný widget/Základ barvy {#color-widgetcolor-base}
Základní barvy použité v rozhraní.

#### Průhledný panel, Barevný panel, Síla rozostření {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Po zapnutí se objeví další možnosti pro ovládání vzhledu nabídek a panelů v Nomadu. Lze upravit jejich barvu, průhlednost a míru rozostření.

::: tip
Na malých zařízeních může být užitečné nastavit panel barev téměř na bílou, průhlednou a s nízkou mírou rozostření, aby nabídky nezakrývaly scénu.
:::

----

### Zrcadlit horní lištu {#mirror-top-bar}
Obrátí pořadí nabídek v horní liště.

### Zrcadlit boční lišty {#mirror-side-bars}
Prohodí postranní lišty tak, aby byl toolbox vlevo a možnosti nástroje vpravo.

### Zrcadlit spodní lištu {#mirror-bottom-bar}
Přesune spodní lištu do pravého dolního rohu a obrátí pořadí tlačítek.

### Náhled barvy materiálu {#material-color-preview}
Když vyberete barvu pro materiál, náhled tohoto materiálu se zobrazí na aktuálně vybraném objektu.

----
### Nápověda při podržení kurzoru {#help-popup-on-hover}

Pro zařízení, která podporují hover, určuje, zda se kontextová nápověda v Nomadu reprezentovaná ikonou ![](/icons/help.webp) zobrazí při najetí, nebo pouze při kliknutí.

----

### Celkové měřítko {#overall-scale}
Násobitel velikosti všech prvků UI.
### Šířka panelu {#panel-width}
Šířka nabídek a panelů.
### Měřítko písma {#font-scale}
Měřítko písem.
### Vertikální rozteč {#vertical-spacing}
Rozestupy mezi prvky v nabídkách a panelech.
### Vertikální rozteč (vlevo) {#vertical-spacing-left}
Rozestupy mezi prvky v levém panelu nástrojů.

----

### Okrajový odsazení {#edge-offset}
Tyto hodnoty byste měli měnit pouze v případě, že máte problémy s interakcí s tlačítky na okrajích obrazovky. Pokud jsou tyto posuvníky vypnuté, Nomad použije hodnoty bezpečné oblasti vrácené samotným zařízením.

::: tip
Při migraci Nomadu na nové zařízení (např. výměna iPhone 12 za iPhone 15) nezapomeňte resetovat možnosti okrajů na výchozí hodnoty!
:::

### Obnovit styl {#reset-style}
Obnoví všechny prvky UI do výchozích hodnot.


## Gesta {#gesture}
Nabídka Gesture ovládá, jak stylus a dotyky prstů ovládají Nomad.

![](/images/interface_gesture.webp)

### Možnosti gest {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad může omezit operace na základě vstupního zařízení. Například tažení prstem může pouze pohybovat kamerou, zatímco tažení stylusem může pouze modelovat. Pokud máte myš nebo trackpad, lze je také přiřadit ke konkrétním operacím.

Nomad vám aktuálně umožňuje nastavit tyto režimy tak, aby byly ovládány libovolnou kombinací gest prstu, stylusu nebo myši:

* Camera
* Sculpt
* Gizmo
* Material picking (dlouhým stiskem)
* Select object


`Finger always smooths` - Smooth lze nastavit tak, aby fungoval pouze při tažení prstem.

### ![](/icons/tool_mask.webp) Maska {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Povolit následující zkratky jedním klepnutím bez nutnosti držet tlačítko mask. Umožní následující gesta:
* klepnutí na pozadí invertuje masku
* klepnutí na maskovanou oblast rozmaže masku
* klepnutí na nemaskovanou oblast zostří masku

### Přepnout Maska <-> SelMask {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Dlouhý stisk přepne mezi Mask a SelMask a začne nový tah. Na konci tahu se znovu vybere předchozí nástroj. 
* `Tool` - Dlouhý stisk a uvolnění bez pohybu přepne mezi Mask a SelMask. 

### ![](/icons/tool_hide.webp) Skrýt {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` povolí následující zkratky s nástrojem hide:
* Klepnutí na face group ji skryje
* Klepnutí do prázdného prostoru invertuje skryté polygony

### ![](/icons/finger3.webp) Tři prsty {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Pokud vaše zařízení podporuje gesta třemi prsty, nakonfigurujte pro toto gesto zkratky. 

Mřížka možností vám umožní definovat vertikální a horizontální tažení jako samostatné zkratky. Všimněte si, že pokud je stejné gesto zvoleno pro 2 možnosti, jedna bude deaktivována.

* `Rotate lighting` - Otočí prostředí, světla a Matcap.
* `Tool Radius` - Upraví poloměr nástroje.
* `Tool Intensity` - Upraví intenzitu nástroje. 

### ![](/icons/fingerprint.webp) Historie 2/3 {#history-23}
`History shortcuts` - pokud je povoleno, jsou aktivní následující gesta:
* Undo - klepnutí 2 prsty
* Redo - klepnutí 3 prsty

`Long press` - pokud je povoleno, podržení 2/3 prstů rychle opakovaně vrací/obnovuje.

### Zpřístupnění {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` zobrazí plovoucí panel nástrojů pro ovládání tažení, štípnutí, rolování a operací kamery.

### Kamera {#camera}
Zkratka pro přechod do nabídky `Camera` (možnosti kamery zde dříve byly, ale byly přesunuty do nabídky kamery).

### Dvojité klepnutí tužkou -> Přiřazení {#pencil-tap}

Zkratka pro přechod do nabídky `Bindings` (možnosti pro klepnutí a dvojité klepnutí Pencil zde dříve byly, ale byly přesunuty do nabídky bindings).


## Přiřazení {#bindings}
Klávesové a tlačítkové zkratky lze definovat v nabídce bindings:

![](/images/interface_bindings.webp)
Téměř všechny funkce v Nomadu lze přiřadit ke klávesovým zkratkám, pokud má vaše zařízení klávesnici, nebo k dalším tlačítkům na stylusu či dokonce ovladačům gamepadu.

Chcete-li vytvořit binding, klikněte na obdélník vedle funkce a stiskněte klávesu/tlačítko. 

Funkce najdete pomocí ikon kategorií nahoře nebo pomocí vyhledávacího pole pro hledání podle názvu. 

Jednotlivé bindingy lze deaktivovat pomocí zaškrtávacího políčka vedle názvu bindingu.

### ![](/icons/more.webp) Kontextová nabídka {#context-menu}
Ikona ![](/icons/more.webp) za každým bindingem zobrazí kontextovou nabídku:

![](/images/interface_bindings_context.webp)

* `Clone` - Klonuje binding
* `Reset` - Resetuje binding
* `Delete` - Smaže binding
* `Toggle shortcut on key tap` - Nastaví, zda se klepnutí vs dlouhý stisk chovají odlišně. Pokud je povoleno, klepnutí aktivuje nástroj. Dlouhý stisk aktivuje nástroj pouze po dobu držení klávesy, po uvolnění se vrátí předchozí nástroj. V jiných 3D aplikacích se tomu někdy říká „sticky keys“.

### Pokročilé {#advanced}
Ve spodní části nabídky bindings je nabídka ozubeného kola pro pokročilé možnosti:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Klepnutí na standardní zkratky pro mask, smooth, gizmo, hide, sub přepne do tohoto režimu, ale podržení klávesy přepne do tohoto režimu pouze po dobu držení, po uvolnění se režim vrátí na předchozí. V jiných 3D aplikacích se tomu někdy říká „sticky keys“.
* `Toggle tool shortcuts` - Při použití jedné ze zkratek nástrojů, pokud je stejná zkratka stisknuta dvakrát, přepne se zpět na předchozí nástroj. Tímto způsobem můžete stále přepínat mezi dvěma nástroji stejnou klávesou.
* `Invert Y (Zooming)` - Inverzuje zoom
* `Reset bindings` - resetuje všechny bindingy na výchozí hodnoty.


## iOS ⌘ Zobrazení klávesových zkratek {#ios-keyboard-shortcuts-display}

Na zařízeních iOS s klávesnicí podržte klávesu ⌘ (cmd) pro zobrazení seznamu zkratek.

Podpora klávesnice na Androidu je trochu experimentální.

![](/images/shortcuts.webp)


## Ladění {#debug}
V této nabídce jsou uloženy některé experimentální a ladicí možnosti. Mnoho z těchto možností by mělo zůstat ve výchozím nastavení a měnit se pouze po kontaktování podpory Nomadu.

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad normalizuje UV do dlaždice [0-1].

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Povolit algoritmus instant remesh
* `Quadriflow` - Alternativní metoda quad remeshe.

### Render {#render}
* `Heightmap` - Změní viewport tak, aby vykresloval hloubku scény. To lze použít k vytvoření alfa map pro použití ve štětcích.
* `Refraction write depth (back)` - Zadní strana refrakčních meshů bude zapsána do depth bufferu.
* `Flip Y (normal map)` - Inverzuje kanál y při bakeování normálových map, vyžadováno pro některé herní a renderovací enginy.
* `Angle weighted smooth normals` - Úprava způsobu fungování hladkého stínování, která může v určitých případech zabránit záhybům.

### Cílové FPS {#target-fps}
Pokud je vypnuto, Nomad synchronizuje počet snímků za sekundu s obnovovací frekvencí vašeho displeje.

Pokud je zapnuto, můžete nastavit počet snímků za sekundu, které bude Nomad vykreslovat.

### Rozhraní {#debug-interface}
* `Top: layout` 
  * Collapse: Na malých zařízeních se horní lišta sbalí do více podnabídek. 
  * Scroll: Pokud jste zvyklí na Nomad na velkých displejích a preferujete normální rozložení, povolením této volby se použije standardní široká horní lišta, kterou lze posouvat.
  * Multiline: Zobrazí celou horní nabídku na několika řádcích.
* `Bottom: draggable popup` - Spodní panel nástrojů má několik tlačítek, která otevírají dialog. Pokud je tato možnost povolena, lze tyto dialogy přesunout jinam na obrazovce.  
* `Toolbox: show all` - Nomad skryje nástroje, které nejsou relevantní pro aktuální výběr, např. všechny sculpt štětce jsou skryty na primitivech, které nejsou validované. Tato možnost ztlumí neaktivní nástroje místo jejich skrytí.
* `Toolbox: colored` - Barevně odliší ikony toolboxu podle jejich typu.
* `Panel: Drop shadows` - Kreslí stíny kolem nabídek a panelů. Na některých starších zařízeních to může ovlivnit výkon.
* `Panel: Blending` - Ladicí možnost
* `Pointer: hovering dot` - Pro zařízení, která podporují hover stylusu, zobrazí tečku, když stylus přejíždí nad nabídkami a panely.

### Gif turntable {#gif-turntable}
Nomad může exportovat animovaný gif turntable. Všimněte si, že kvůli omezením formátu gif je kvalita nízká. Záznam obrazovky je obvykle lepší metoda.

* `Duration` - jak dlouhý v sekundách bude turntable
* `Rotation center` - kde je pivot kamery, tedy kolem které části scény se bude kamera otáčet
* `Transparent background` - Použije průhledné pozadí pro gify. Všimněte si, že gify podporují pouze 1bitovou průhlednost, takže okraje mohou být silně zubaté.
* `Max frame sampling` - Mnoho vysoce kvalitních renderovacích efektů Nomadu vzniká kombinací několika snímků dohromady. Tento posuvník nastavuje, kolik snímků se má kombinovat.
* `Export (GIF)` - spustí proces exportu gifu.

### Post Process {#post-process}
* `Filtering` - Ladicí možnost
* `Format` - Ladicí možnost
* `Buffer reuse` - Ladicí možnost

### Výkon {#performance}
* `Multicore general` - Ladicí možnost
* `Multicore sculpting` - Ladicí možnost
* `Partial Drawing` - Experimentální funkce! Použijte, pokud modelujete relativně malou část vysoce polygonální sítě. Mělo by to učinit modelování plynulejším, ale neměli byste zapínat wireframe! Také to může během tahů štětcem přidat vizuální artefakty.

### Funkce {#feature}
* `Flip quad split (on tap)` -  Ladicí možnost
* `Join: merge radius` - Vrcholy budou automaticky svařeny, pokud jsou při spojování meshů dostatečně blízko. Poloměr můžete upravit tímto posuvníkem.

### Ladění {#dev}
* `Logs` - Zobrazí okno s logy
* `App review popup` - Ladicí možnost
* `FPS` - přidá počítadlo snímků za sekundu do statistik viewportu.