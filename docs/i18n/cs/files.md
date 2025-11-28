# ![](/icons/open.webp) Soubory {#files}

Nabídka Soubory umožňuje ukládat a načítat projekty Nomad, importovat a exportovat 3D modely a exportovat vyrenderované obrázky.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

V horní části této nabídky je zobrazen náhled posledního uložení. Kliknutím na tento náhled se otevře mini prohlížeč, dvojitým klepnutím na jiný projekt se zobrazí mini nabídka pro otevření, přidání, uložení, klonování, přejmenování nebo smazání daného projektu.

### ![](/icons/nomad.webp) Předvolba {#preset}
Získejte přístup ke kolekci ukázek a komponent postav. Vyberte jednu, poté ji vyberte znovu a zvolte Otevřít, Přidat do scény nebo Klonovat položku do své složky projektů.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Uložit {#save}
Uloží projekt Nomad.

### ![](/icons/save_as.webp) Uložit jako... {#save-as}
Zobrazí prohlížeč projektů, který umožní uložit projekt Nomad pod novým názvem.

### ![](/icons/pencil.webp) Přejmenovat {#rename}
Zobrazí textové pole pro přejmenování aktuálního projektu.

### ![](/icons/open.webp) Otevřít... {#open}
Zobrazí prohlížeč projektů pro otevření projektu.

### ![](/icons/add_file.webp) Přidat do scény... {#add}
Zobrazí prohlížeč projektů, po výběru projektu bude jeho obsah sloučen s aktuální scénou.

### ![](/icons/trash.webp) Smazat... {#delete}
Zobrazí prohlížeč projektů, všechny vybrané projekty budou smazány ze souborového systému.

### ![](/icons/new_file.webp) Nový {#new}
Spustí nový projekt, pokud existují neuložené změny, budete dotázáni, zda je chcete uložit.

### ![](/icons/autosave.webp) Automatické ukládání... {#auto-save}
Nabídka pro nastavení možností automatického ukládání.

Pokud povolíte automatické ukládání, můžete nastavit časovač, aby se v pravidelných intervalech zobrazovalo vyskakovací okno.
Nomad neukládá na pozadí, protože 3D soubory mohou být poměrně velké a během modelování by to mohlo způsobovat znatelné zpomalení.

Navíc, aby se předešlo problémům s nedostatkem paměti, je scéna obvykle před uložením komprimována.
Tato komprese/dekomprese také zpomalí operaci ukládání.

### Časovač vyskakovacího okna {#timer-pop-up}
Jak často se bude vyskakovací okno časovače zobrazovat.

### Časový limit vyskakovacího okna {#popup-timeout}
Povolit časový limit vyskakovacího okna.

### Zrušit automatické uložení {#discard-autosave}
Pokud pro projekt existuje soubor automatického uložení, bude automaticky načten místo původního projektu. Pokud to není žádoucí, toto tlačítko automatické uložení smaže. Načtení souboru pak načte poslední ruční uložení projektu.


## Import {#import}

### ![](/icons/add_file.webp) Import {#import-button}
Pro import 3D souborů, které nejsou projekty Nomad.

Když do Nomadu importujete externí soubor scény, můžete jej buď *importovat*, nebo *přidat*.

Přidání souboru jednoduše přidá objekty do aktuální scény.
Import souboru vytvoří nový projekt Nomad s novými objekty.

Nomad umí importovat tyto formáty:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimentální)

### ![](/icons/cog.webp) Pokročilé {#advanced}
Zobrazí pokročilé možnosti importu:

### Projekt/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Zachovat topologii {#keep-topology}
Nomad se ve výchozím nastavení při načítání pokusí opravit problematickou geometrii. Povolíte-li tuto volbu, Nomad nebude měnit pořadí vrcholů/polí, odstraňovat duplicitní vrcholy/polygony ani odstraňovat nepoužité vrcholy.

#### Přeskočit textury {#skip-textures}
Přeskočí načítání textur u formátů, které je podporují, jako je glTF.

### Projekt / glTF {#project-gltf}
#### Zachovat nastavení GUI {#keep-gui-settings}
Povolí ukládání GUI a projektových nastavení do souboru Nomad .nom nebo glTF.

### OBJ {#obj}
#### Rozdělit OBJ podle skupin {#split-obj-by-groups}
Povolí rozdělení skupin OBJ do samostatných objektů.

#### Barevný prostor {#color-space}
Nastaví režim barev interpretovaných z OBJ jako Lineární, sRGB nebo Auto.

### PLY {#ply}
#### Barevný prostor {#color-space-ply}
Nastaví režim barev interpretovaných z PLY jako Lineární, sRGB nebo Auto.


### FBX {#fbx}
#### Barevný prostor {#color-space-fbx}
Nastaví režim barev interpretovaných z FBX jako Lineární, sRGB nebo Auto.



## Export {#export}
Uloží do formátu 3D geometrie, který lze použít v jiném softwaru. 

![](/images/file_export.webp)

Různé formáty souborů podporují různé funkce, dostupné možnosti se mění podle zvoleného typu souboru.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Vše / Viditelné / Vybrané {#allvisibleselected}
Aktivní stav tlačítka určuje, které objekty budou exportovány. Číslo vedle ikon udává, kolik objektů bude pro danou volbu exportováno.

### Vrcholové barvy {#vertex-colors}
Exportuje barvy vrcholů, pokud je formát souboru podporuje.

### PBR malba {#pbr-paint}
PBR barvy vrcholů jsou exportovány jako sekundární atributy barev vrcholů.
Kanály jsou zabaleny následujícím způsobem:

|           | Kanál   |
| :-------: | :-----: |
| Drsnost   | R       |
| Kovovost  | G       |
| Maskování | B       |


### Vrstvy {#layers}
Vrstvy jsou podporovány prostřednictvím glTF morph targets.
Nomad také exportuje barvy, drsnost a kovovost na úrovni vrstev, ale ostatní software je obvykle ignoruje.

### Malování vrstev {#layer-painting}
Exportuje malování vrstev, obvykle ignorováno jiným softwarem.

### Skupina ploch {#face-group}
Exportuje facegroupy, export může někdy způsobovat problémy v jiném softwaru.

### Normály {#normals}
Exportuje informace o normálách. Všimněte si, že Nomad při importu jiných formátů souborů vždy přepočítá vlastní normály.

### Tangenty {#tangents}
Exportuje informace o tangentech, používané pokud má model normálové mapy. 

### Textury {#textures}
Pokud byly do materiálu přidány textury, budou exportovány. Toto však neprovádí bake textur, ten se provádí pomocí možností bake v topologii.

### Tlačítko Export {#export-button}
Kliknutím na toto tlačítko exportujete geometrii s použitím zvolených nastavení.

::: tip Tip: Import drsnosti a kovovosti do Blenderu

Blender umí importovat glTF/glb, ale automaticky nerozpozná vertex atributy pro kovovost a drsnost. Pro jejich použití v editoru materiálů vytvořte uzel Vertex Color, nastavte jeho vlastnost na další barevný atribut (obvykle Col.001). Připojte uzel 'Separate XYZ', pošlete X na Roughness a Y na Metallic.

Toto video ukazuje postup:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: Podpora funkcí USD

USD je komplexní formát, jeho specifikace podporuje mnoho funkcí, ale ne všechen 3D software je podporuje. Například macOS/iOS nepodporují barvy vrcholů. Přednastavené režimy v rámci exportéru USD se snaží o co nejlepší odhad kompatibility s OpenUSD, Apple, Procreate, ZBrush.

::: 

## Rendering {#render}

Exportuje obrázek, který je kombinací všech nastavení v projektu (světla, materiály, postprocessing atd.). 

![](/images/file_render.webp)
### Náhled {#preview}

Malé tlačítko náhledu vedle názvu nabídky ztlumí panely nástrojů, aby lépe zobrazilo finální výsledek.

### Průhledné pozadí {#transparent-background}
Povolí alfa kanál pro render, užitečné pro kombinování renderu s jinými obrázky v 2D programech. Částečná průhlednost není podporována.

### Zobrazit rozhraní {#show-interface}
Povolí zahrnutí uživatelského rozhraní Nomad do renderu.

### Poměr renderu {#render-ratio}
Násobitel rozlišení obrázku.

### Konečná velikost {#final-size}
Rozlišení použité pro render. Když je vybráno `Custom`, budou povoleny posuvníky šířky a výšky. 

Když je aktivní nabídka Soubor, bude ve viewportu vykreslena přerušovaná překryvná oblast označující oblast renderu, pokud se neshoduje s rozlišením obrazovky (pro správné zobrazení musíte být v režimu na šířku).

### Export PNG {#export-png}
Kliknutím na toto tlačítko spustíte proces renderování. Po dokončení si můžete zvolit, jak obrázek uložit nebo sdílet.