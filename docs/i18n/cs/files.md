# ![](/icons/open.webp) Soubory {#files}

V nabídce soubory ukládáte a načítáte projekty Nomadu, importujete a exportujete 3d modely, exportujete vykreslené obrázky a propojujete Nomad s jinými aplikacemi. Má tři karty: `Soubory`, `Render` a `Propojení`.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

Náhled nahoře ukazuje aktuální projekt a vedle něj velikost jeho souboru, automatické uložení a uloženou historii. Klepnutím na náhled otevřete malý prohlížeč vašich projektů. Klepnutím na projekt pak otevřete nabídku, kde ho můžete otevřít, přidat, přepsat, naklonovat, přejmenovat nebo smazat.

Pokud má projekt změny, které ještě nejsou uložené, zobrazí se pod náhledem `Neuložené změny!`.

### Dosah {#scope}
Na počítači si zvolíte, kam se vaše projekty ukládají:
* `Interní` - výchozí volba, stejně jako na mobilu. Projekty se ukládají jen do hlavní složky Nomadu.
* `Původní soubor` - když otevřete projekt mimo složku Nomadu, uložení přepíše původní soubor. U těchto externích projektů nefunguje automatické ukládání.

### ![](/icons/nomad.webp) Přednastavení {#preset}
Přístup ke sbírce ukázek a součástí postav. Jednu vyberte a dalším výběrem zvolte, zda ji chcete `Otevřít`, nebo `Přidat do scény`. V tomto prohlížeči si také můžete stáhnout bezplatné modely z Poly Haven.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Historie... {#history}
Rychlý přístup k volbám historie projektu, například `Uložit historii`, které při uložení projektu zachová historii pro vracení změn. Zelený odznak na tlačítku ukazuje, že se historie ukládá spolu s projektem. Podrobnosti najdete v části [Historie](history.md#save-history).

### ![](/icons/save.webp) Uložit {#save}
Uloží projekt Nomadu. Pokud projekt ještě nikdy nebyl uložen, budete vyzváni k zadání názvu.

### ![](/icons/save_as.webp) Uložit jako... {#save-as}
Uloží projekt pod novým názvem jako nový projekt.

### ![](/icons/save_as.webp) Přepsat... {#overwrite}
Otevře prohlížeč projektů, kde můžete aktuální scénou přepsat jiný projekt. Zapněte `Zahrnout pouze vybrané objekty`, pokud chcete uložit jen vybrané objekty místo celé scény. Prohlížeč má také tlačítko `Uložit jako...`, kterým projekt místo toho uložíte jako nový.

### ![](/icons/pencil.webp) Přejmenovat {#rename}
Zobrazí textové pole pro přejmenování aktuálního projektu.

### ![](/icons/open.webp) Otevřít... {#open}
Otevře prohlížeč projektů, kde můžete projekt otevřít.

### ![](/icons/add_file.webp) Přidat do scény... {#add}
Otevře prohlížeč projektů. Obsah vybraného projektu se sloučí s aktuální scénou.

### ![](/icons/trash.webp) Smazat... {#delete}
Otevře prohlížeč projektů. Všechny vybrané projekty se smažou ze systému souborů.

### ![](/icons/new_file.webp) Nový {#new}
Založí nový projekt. Pokud máte neuložené změny, budete požádáni o potvrzení. V potvrzení můžete nastavení `Pozadí`, `Prostředí`, `MatCap` a `Rentgen` zvolit `Ponechat`, nebo `Vynulovat`, a také zvolit, zda nový projekt použije `Uložit historii`.

### ![](/icons/autosave.webp) Automatické ukládání... {#auto-save}
Nabídka s volbami automatického ukládání. Zapněte `Automatické ukládání`, pokud chcete projekt v pravidelných intervalech ukládat do samostatného souboru. Odznak na tlačítku ukazuje, zda je zapnuté.

Nomad neukládá na pozadí proto, že 3d soubory mohou být dost velké, a ukládání by tak při sochání mohlo způsobovat výrazné zasekávání.

Navíc se scéna před uložením obvykle komprimuje, aby nedošla paměť.
Tato komprese a dekomprese ukládání také zpomaluje.

### Interval ukládání {#timer-pop-up}
Kolik minut Nomad čeká mezi automatickými uloženími.

### Zobrazit odpočet {#popup-timeout}
Před každým automatickým uložením zobrazí odpočet, abyste ho mohli zrušit, pokud jste zrovna uprostřed práce. Když je volba vypnutá, Nomad uloží projekt, jakmile přestanete sochat.

### ![](/icons/trash.webp) Zrušení automatického ukládání {#discard-autosave}
Pokud pro projekt existuje soubor automatického uložení, načte se automaticky místo původního projektu. Pokud o to nestojíte, toto tlačítko automatické uložení smaže. Při načtení souboru se pak načte poslední ruční uložení projektu.

### ![](/icons/open.webp) Otevřít zastaralé uložení {#open-outdated-save}
Když má projekt automatické i ruční uložení, toto tlačítko otevře starší z nich (`Otevřít zastaralé automatické uložení` nebo `Otevřít zastaralé ruční uložení`) a zobrazí jeho datum. Hodí se, když poslední uložení není to, které jste chtěli.

### ![](/icons/storage.webp) Nedávno smazané... {#recently-deleted}
Nomad uchovává data projektů, které opustily složku projektů, a soubory nahrazené importem ještě několik dní, než je definitivně smaže. Soubory, jejichž import selhal, zůstanou, dokud je nesmažete. Tento seznam je ukazuje s jejich velikostí a datem, takže je můžete smazat jednotlivě, nebo tlačítkem `Smazat vše`.

## Importovat {#import}

### ![](/icons/add_file.webp) Importovat {#import-button}
Slouží k importu 3d souborů, které nejsou projekty Nomadu.

Když do Nomadu importujete soubor s externí scénou, můžete ho buď *přidat*, nebo s ním založit *nový* projekt.

Přidání souboru jednoduše vloží objekty do aktuální scény.
Volba `Nový` vytvoří nový projekt Nomadu s novými objekty.

Okno importu vypíše všechny vybrané soubory, každý s vlastními volbami importu. Takto lze importovat i obrázky: u každého zvolíte, zda se z něj stane `HDRI`, `MatCap`, `Referenční obrázek`, `Alfa`, `Textury` nebo `VDM`.

Nomad umí importovat tyto formáty:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), na platformách, které ho podporují

### ![](/icons/cog.webp) Nastavení {#advanced}
Tlačítko `Nastavení...` vedle náhledu projektu zobrazí hlavní volby importu. Tato nastavení se neukládají a okno importu ukazuje volby, které platí pro importované soubory.

### Všechny formáty {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Zachovat topologii {#keep-topology}
Nomad se ve výchozím stavu pokouší při načítání opravit problematickou geometrii. Zapnutím této volby Nomadu zabráníte měnit pořadí vrcholů a ploch, slučovat duplicity a odstraňovat nepoužité vrcholy.

::: warning
Se zapnutým `Zachovat topologii` nemusí operace jako booleovské operace, spojení, decimace nebo Manifold sloučit duplicitní vrcholy.
:::

#### ![](/icons/image.webp) Přeskočit textury {#skip-textures}
Nenačte textury vložené v souboru, u formátů, které je podporují, například glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Načíst nastavení UI {#keep-gui-settings}
Při otevírání nebo importu souboru projektu načte všechna nastavení rozhraní, která jsou v něm uložená.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Rozdělit OBJ podle skupin {#split-obj-by-groups}
Rozdělí skupiny OBJ do samostatných objektů.

#### ![](/icons/vertex.webp) Sloučit duplicitní pozice {#merge-duplicate-positions}
Sloučí vrcholy, které mají stejnou polohu.

#### ![](/icons/uv.webp) Sloučit duplicitní UV {#merge-duplicate-uvs}
Sloučí texturové souřadnice, které mají stejné UV.

#### ![](/icons/paint.webp) Barevný prostor {#color-space}
Nastaví, jak se barvy ze souboru interpretují: `Auto`, `Lineární` nebo `sRGB`. Pokud barvy nevypadají správně, zkuste tuto volbu přepnout.

#### ![](/icons/image.webp) Formát {#normal-format}
Formát normálových map v texturách: `Auto`, `OpenGL (+Y)` nebo `DirectX (-Y)`. Pokud detaily normálové mapy vypadají obráceně, zkuste ten druhý.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Barevný prostor {#color-space-ply}
Nastaví, jak se barvy ze souboru interpretují: `Auto`, `Lineární` nebo `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Sloučit duplicitní UV {#merge-duplicate-uvs-fbx}
Sloučí texturové souřadnice, které mají stejné UV.

#### ![](/icons/paint.webp) Barevný prostor {#color-space-fbx}
Nastaví, jak se barvy ze souboru interpretují: `Auto`, `Lineární` nebo `sRGB`.

#### ![](/icons/image.webp) Formát {#normal-format-fbx}
Formát normálových map v texturách: `Auto`, `OpenGL (+Y)` nebo `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Barevný prostor {#color-space-usd}
Nastaví, jak se barvy ze souboru interpretují: `Auto`, `Lineární` nebo `sRGB`.

#### ![](/icons/image.webp) Formát {#normal-format-usd}
Formát normálových map v texturách: `Auto`, `OpenGL (+Y)` nebo `DirectX (-Y)`.



## Exportovat {#export}
Uloží model do formátu 3d geometrie, který lze použít v jiném softwaru. 

![](/images/file_export.webp)

Různé formáty souborů podporují různé funkce, takže dostupné volby se mění podle zvoleného typu souboru.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Barvy vrcholů](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR vrcholů](#pbr-paint)       | ✅     | Nomad ✅<br>Jiné ⚠️  | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Jiné ⚠️  | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Vrstvy](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objekty                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Skupiny ploch                   | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchie                      | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Světla                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textury                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitiva, postproces atd.      | ✅     | Nomad ✅<br>Jiné ❌  | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Tlačítko exportu {#export-button}
Klepnutím exportujete geometrii se zvoleným nastavením. Tlačítko ukazuje zvolený formát a odhad velikosti souboru. Na Androidu je vedle něj tlačítko `Sdílet`, které soubor pošle rovnou do jiné aplikace.

### Formát souboru {#file-format}
Zvolte formát exportu: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` nebo `USD`. NOMAD je vlastní formát Nomadu, v jiném softwaru se nenačte, takže slouží hlavně k opětovnému importu do Nomadu.

### Zahrnout {#allvisibleselected}
Zvolte, které objekty se exportují: `Vše`, `Viditelné` nebo `Vybrané`. Číslo vedle každé volby ukazuje, kolik objektů se exportuje.

### Jeden soubor na objekt {#one-file-per-object}
Exportuje každý objekt do samostatného souboru. Číslo ukazuje, kolik souborů se zapíše.

### Typ {#type}
Když export zapisuje více souborů (jeden soubor na objekt, nebo OBJ s texturami), zvolte, zda je uložit jako `Složka`, nebo `Zip`. Některé aplikace (Google Drive, One Drive atd.) nepodporují import složek, takže místo toho můžete použít Zip.

### Vložit historii {#embed-history}
Jen pro NOMAD. Vloží do souboru historii vracení změn, která se obnoví při otevření souboru v Nomadu. Zvětšuje velikost souboru a vyžaduje, aby se celá scéna exportovala jako jediný soubor.

### Vložit prostředky {#embed-assets}
Jen pro NOMAD. Vloží do souboru vaše vlastní matcapy, prostředí a písma. Vestavěné prostředky se nevkládají.

### Barvy vrcholů {#vertex-colors}
Exportuje barvy vrcholů, pokud je formát souboru podporuje. Některé 3d programy je umí přečíst, ale ne všechny.

U OBJ můžete zvolit:
* `Žádný` - bez barev.
* `RGB` - barvy se připojí za vrcholy.
* `MRGB (ZBrush)` - alternativní způsob kódování barev, který podporuje i data masky.

### Barevný prostor {#color-space-export}
Jen pro OBJ s barvami vrcholů `RGB`. Zapíše barvy jako `Lineární` nebo `sRGB`.

### PBR barva {#pbr-paint}
Exportuje malování drsnosti, kovovosti a masky. Jiný software může tato data ignorovat.
PBR barvy vrcholů se exportují jako sekundární atributy barev vrcholů.
Kanály jsou zabalené takto:

|           | Kanál    |
| :-------: | :------: |
| Drsnost   | R        |
| Kovovost  | G        |
| Maska     | B        |


### Vrstvy {#layers}
Vrstvy jsou podporované pomocí glTF morph targetů. glTF je oficiálně podporuje, takže by měly fungovat i v jiném softwaru.
Nomad exportuje také barvy, drsnost a kovovost jednotlivých vrstev, ale jiný software je ignoruje.

### Malování vrstev {#layer-painting}
Exportuje malování ve vrstvách, které jiný software obvykle ignoruje.

### Skupina tváří {#face-group}
Exportuje skupiny ploch. Jejich export může někdy jinému softwaru působit potíže.

### Zapsat objekty {#write-objects}
Jen pro OBJ. Ponechá objekty oddělené. Vypněte, pokud chcete vše exportovat jako jediný objekt, například abyste mohli v Substance Painteru použít funkci „Mesh ID / Polygroup“.

### Normály {#normals}
Exportuje informace o normálách. Nomad si při importu jiných formátů vždy vypočítá vlastní normály.

### Tečny {#tangents}
Exportuje informace o tečnách, které se používají, pokud má model normálové mapy. 

### Textury {#textures}
Pokud jsou k materiálu přidané textury, exportují se. Tím se ale textury nezapékají, to se dělá pomocí voleb pečení v nabídce topologie.

### Formát {#fbx-format}
Jen pro FBX. `Binární` je menší, ale nemusí fungovat v každé aplikaci, `ASCII` je textový soubor.

### Komprimováno {#compressed}
Jen pro FBX. Zmenší velikost souboru za cenu pomalejšího exportu a importu.

### Přednastavení {#usd-preset}
Jen pro USD. Zvolte aplikaci, pro kterou exportujete: `OpenUSD`, `Apple`, `Procreate` nebo `Zbrush`. Některé volby jsou dostupné jen u některých přednastavení.

### Instance {#instance}
Jen pro USD. Exportuje instancované objekty jako instance, místo aby duplikoval jejich geometrii.

### Povolit zkosení {#allow-skew}
Jen pro USD. Povolí zkosení v maticových transformacích. Když je volba vypnutá, Nomad rozdělí zkosené transformace na samostatné transformace měřítka a rotace.

### Opakovač {#repeater}
Jen pro USD. Exportuje kopie vytvořené opakovači jako instance.

### Sloučit kopie {#join-copies}
Každý objekt se svými kopiemi z opakovače se stane jediným objektem.

::: tip Tip: import drsnosti a kovovosti do Blenderu

Blender umí importovat glTF/glb, ale atributy vrcholů pro kovovost a drsnost automaticky nerozpozná. Chcete-li je použít, vytvořte v editoru materiálu uzel Vertex Color a nastavte jeho vlastnost na další barevný atribut (obvykle Col.001). Připojte uzel „Separate XYZ“, X pošlete do roughness a Y do Metallic.

Toto video ukazuje celý postup:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: podpora funkcí USD

USD je složitý formát a jeho specifikace podporuje spoustu funkcí, ne každý 3d software je ale podporuje všechny. Například OSX/iOS nepodporují barvy vrcholů. Režimy přednastavení v exportu USD se snaží co nejlépe odhadnout kompatibilitu s OpenUSD, Apple, Procreate a Zbrush.

::: 

## ![](/icons/screen.webp) Render {#render}

Exportuje obrázek, který kombinuje všechna nastavení projektu (světla, materiály, postproces atd.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Náhled {#preview}

Tlačítko `Náhled` vedle názvu nabídky zprůhlední rozhraní, abyste lépe viděli kompozici výsledného obrázku.

### ![](/icons/home.webp) Ostření {#focus}
Zarámuje scénu nebo výběr tak, aby se vešly do velikosti renderu. Dalším klepnutím přepnete mezi oběma možnostmi.

### ![](/icons/map.webp) Výšková mapa {#heightmap}
Vykreslí scénu jako výškovou mapu ve stupních šedi z pohledu kamery, kde jsou nejbližší části nejsvětlejší. Zapnutím se přepne velikost na `Čtverec` a zarámuje se výběr. Malý posuvník v zobrazení umožňuje upravit `Ostření` přechodu.

Když je `Výšková mapa` zapnutá, objeví se vedle tlačítka exportu tlačítko `Uložit jako alfu`, které render uloží jako novou alfu štětce místo exportu souboru.

### ![](/icons/opacity.webp) Průhledné pozadí {#transparent-background}
Přidá renderu alfa kanál, což se hodí pro kombinování renderu s jinými obrázky ve 2d programech. Částečná průhlednost není podporována.

### ![](/icons/sliders.webp) Zobrazit rozhraní {#show-interface}
Zahrne do renderu rozhraní Nomadu.

### Konečná velikost {#final-size}
Rozlišení renderu: `Obrazovka`, `720`, `1080`, `4096`, `Čtverec` nebo `Vlastní`.

Když je nabídka Soubory aktivní, zobrazí se v zobrazení přerušovaný rámeček, který ukazuje oblast renderu, pokud neodpovídá rozlišení obrazovky.

### Šířka / Výška {#render-ratio}
S volbou `Vlastní` nastavíte šířku a výšku obrázku. Tlačítko řetězu mezi oběma posuvníky zachová poměr stran, když jeden z nich změníte. S volbou `Čtverec` lze nastavit jen šířku.

### ![](/icons/export.webp) Exportovat → PNG {#export-png}
Klepnutím na toto tlačítko spustíte vykreslování. Po dokončení zvolíte, jak obrázek uložit nebo sdílet. U velmi velkých rozměrů se nejprve zobrazí potvrzení: projekt si předtím uložte, pro případ, že zařízení dojde paměť.

## ![](/icons/network.webp) Propojení {#link}

Propojí Nomad s jiným zařízením nebo aplikací, abyste mohli posílat a přijímat objekty, nebo živě synchronizovat své úpravy. Jedno zařízení relaci hostí, ostatní se k ní připojí.

### Povolit GoZ {#enable-goz}
Jen na počítači. Výměna sítí se ZBrush na tomto počítači. `Odeslat` je importuje do ZBrush, `Načíst` importuje ze spuštěného ZBrush: `Výběr` vezme aktivní subtool, `Scéna` vezme všechny subtooly. GoZ můžete v ZBrush také kdykoli stisknout.

### Režim {#link-mode}
* `Vypnuto` - žádné propojení.
* `Hostitel` - toto zařízení hostí relaci a čeká, až se připojí ostatní.
* `Připojit se` - vyhledá zařízení v okolí; pak se klepnutím na jméno hostitele připojíte.

Chcete-li propojit dva Nomady, zvolte na jednom zařízení `Hostitel` a na ostatních `Připojit se`. Při propojení s Blenderem má být hostitelem Nomad: tlačítko nápovědy vedle názvu `Propojení` ukazuje, jak nainstalovat rozšíření Nomad Blender Link.

### ![](/icons/network.webp) Síťový port {#network-port}
Síťový port, který propojení používá. Měňte ho jen tehdy, když ho už používá jiná aplikace.

### Odeslat / Načíst {#send-get}
Po připojení můžete svůj výběr (`Výběr`) nebo celou scénu (`Scéna`) `Odeslat` do druhého zařízení, nebo je z něj `Načíst`. `Nahradit` smaže aktuální scénu a pak načte scénu druhého zařízení.

### ![](/icons/link.webp) Živá synchronizace {#live-sync}
Průběžně posílá vaše úpravy do druhého zařízení. `Pracovní pohled` synchronizuje i kameru. `Úpravy scény` určuje, které zařízení úpravy posílá: `Auto` dá směr podle poslední aktivity. Pak zvolte, co se synchronizuje: `Objekty a geometrie`, `Materiály`, `Světla`, `Kamery` a pokud to druhá strana podporuje, také `Stínování` a `PostProcess`.

::: tip
Existující objekty je nejprve potřeba jednou `Odeslat` nebo `Načíst`, aby se propojily a živá synchronizace je mohla aktualizovat.
:::
