# ![](/icons/open.webp) Pliki {#files}

Menu plików pozwala zapisywać i wczytywać projekty Nomad, importować i eksportować modele 3D oraz eksportować wyrenderowane obrazy.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

Na górze tego menu wyświetlany jest miniaturowy podgląd ostatniego zapisu. Kliknięcie tej miniatury otwiera mini-przeglądarkę; stuknij dwukrotnie inny projekt, aby wyświetlić mini-menu z opcjami otwarcia, dodania, zapisania, sklonowania, zmiany nazwy lub usunięcia tego projektu.

### ![](/icons/nomad.webp) Preset {#preset}
Uzyskaj dostęp do kolekcji demonstracji i komponentów postaci. Wybierz jeden element, a następnie wybierz ponownie, aby zdecydować, czy chcesz Otworzyć, Dodać do sceny, czy Sklonować wpis do folderu projektów.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Zapisz {#save}
Zapisz projekt Nomad.

### ![](/icons/save_as.webp) Zapisz jako... {#save-as}
Wyświetl przeglądarkę projektów, aby zapisać projekt Nomad pod nową nazwą.

### ![](/icons/pencil.webp) Zmień nazwę {#rename}
Wyświetl pole tekstowe do zmiany nazwy bieżącego projektu.

### ![](/icons/open.webp) Otwórz... {#open}
Wyświetl przeglądarkę projektów, aby otworzyć projekt.

### ![](/icons/add_file.webp) Dodaj do sceny... {#add}
Wyświetl przeglądarkę projektów; po wybraniu projektu jego zawartość zostanie scalona z bieżącą sceną.

### ![](/icons/trash.webp) Usuń... {#delete}
Wyświetl przeglądarkę projektów; wszystkie wybrane projekty zostaną usunięte z systemu plików.

### ![](/icons/new_file.webp) Nowy {#new}
Rozpocznij nowy projekt; jeśli istnieją niezapisane zmiany, zostaniesz zapytany, czy chcesz je zapisać.

### ![](/icons/autosave.webp) Autozapis... {#auto-save}
Menu do kontrolowania opcji autozapisu.

Jeśli włączysz autozapis, możesz ustawić timer tak, aby wyskakujące okienko pojawiało się w regularnych odstępach czasu.  
Nomad nie zapisuje w tle, ponieważ pliki 3D mogą być dość duże, co mogłoby powodować zauważalne przycięcia podczas rzeźbienia.

Dodatkowo, aby uniknąć problemów z brakiem pamięci, scena jest zazwyczaj kompresowana przed operacją zapisu.  
Ta kompresja/dekompresja również spowalnia operację zapisu.

### Timer pop up {#timer-pop-up}
Jak często będzie pojawiać się wyskakujące okienko timera.

### Limit czasu wyskakującego okna {#popup-timeout}
Włącz limit czasu dla wyskakującego okna.

### Odrzuć autozapis {#discard-autosave}
Jeśli dla projektu istnieje plik autozapisu, zostanie on automatycznie wczytany zamiast oryginalnego projektu. Jeśli nie jest to wymagane, ten przycisk usunie autozapis. Wczytanie pliku spowoduje wtedy załadowanie ostatniego ręcznego zapisu projektu.


## Import {#import}

### ![](/icons/add_file.webp) Importuj {#import-button}
Do importowania plików 3D, które nie są projektami Nomad.

Gdy importujesz zewnętrzny plik sceny do Nomad, możesz go *zaimportować* lub *dodać*.

Dodanie pliku po prostu doda obiekty do bieżącej sceny.  
Importowanie pliku utworzy nowy projekt Nomad z nowymi obiektami.

Nomad może importować następujące formaty:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, eksperymentalnie)

### ![](/icons/cog.webp) Zaawansowane {#advanced}
Wyświetl zaawansowane opcje importu:

### Projekt/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Zachowaj topologię {#keep-topology}
Domyślnie Nomad próbuje naprawić problematyczną geometrię podczas wczytywania. Włączenie tej opcji uniemożliwi Nomadowi zmianę kolejności wierzchołków/płaszczyzn, usuwanie zduplikowanych wierzchołków/płaszczyzn oraz usuwanie nieużywanych wierzchołków.

#### Pomiń tekstury {#skip-textures}
Pomiń wczytywanie tekstur dla formatów, które je obsługują, takich jak glTF.

### Projekt / glTF {#project-gltf}
#### Zachowaj ustawienia GUI {#keep-gui-settings}
Włącz zapisywanie ustawień GUI i projektu w pliku Nomad .nom lub glTF.

### OBJ {#obj}
#### Rozdziel OBJ według grup {#split-obj-by-groups}
Włącz podział grup OBJ na osobne obiekty.

#### Przestrzeń barw {#color-space}
Ustaw tryb kolorów interpretowany z pliku OBJ jako Linear, sRGB lub Auto.

### PLY {#ply}
#### Przestrzeń barw {#color-space-ply}
Ustaw tryb kolorów interpretowany z pliku PLY jako Linear, sRGB lub Auto.


### FBX {#fbx}
#### Przestrzeń barw {#color-space-fbx}
Ustaw tryb kolorów interpretowany z pliku FBX jako Linear, sRGB lub Auto.



## Eksport {#export}
Zapis do formatu geometrii 3D, który może być użyty w innym oprogramowaniu. 

![](/images/file_export.webp)

Różne formaty plików obsługują różne funkcje; dostępne opcje będą się zmieniać w zależności od wybranego typu pliku.

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


### Wszystko/Widoczne/Zaznaczone {#allvisibleselected}
Aktywny stan przycisku określa, które obiekty zostaną wyeksportowane. Liczba obok ikon wskazuje, ile obiektów zostanie wyeksportowanych dla danej opcji.

### Kolory wierzchołków {#vertex-colors}
Eksportuj kolory wierzchołków, jeśli są obsługiwane przez format pliku.

### PBR Paint {#pbr-paint}
Kolory wierzchołków PBR są eksportowane jako dodatkowe atrybuty kolorów wierzchołków.  
Kanały są pakowane w następujący sposób:

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Warstwy {#layers}
Warstwy są obsługiwane poprzez cele morfingu (morph targets) w glTF.  
Nomad eksportuje również kolory, szorstkość (roughness) i metaliczność (metalness) per warstwa, ale będzie to ignorowane przez inne oprogramowanie.

### Malowanie warstwowe {#layer-painting}
Eksportuj malowanie warstw; zazwyczaj ignorowane przez inne oprogramowanie.

### Grupa ścian {#face-group}
Eksportuj grupy ścian (facegroups); eksport może czasem powodować problemy w innym oprogramowaniu.

### Normale {#normals}
Eksportuj informacje o normalnych. Zauważ, że Nomad zawsze oblicza własne normale podczas importu innych formatów plików.

### Tangenty {#tangents}
Eksportuj informacje o tangentach, używane, jeśli model ma mapy normalnych. 

### Tekstury {#textures}
Jeśli do materiału zostały dodane tekstury, zostaną one wyeksportowane. Zauważ, że nie spowoduje to wypalenia (bake) tekstur; odbywa się to poprzez opcje bake w topologii.

### Przycisk eksportu {#export-button}
Kliknij, aby wyeksportować geometrię z użyciem wybranych ustawień.

::: tip Wskazówka: Import roughness i metalness do Blendera

Blender potrafi importować glTF/glb, ale nie interpretuje automatycznie atrybutów wierzchołków dla metalness i roughness. Aby ich użyć, w edytorze materiałów utwórz węzeł Vertex Color i ustaw jego właściwość na kolejny atrybut koloru (zwykle Col.001). Podłącz węzeł „Separate XYZ”, wyślij X do Roughness, a Y do Metallic.

Ten film pokazuje proces:

![](/videos/blender_pbr.mp4)

::: 

::: tip Wskazówka: Obsługa funkcji USD

USD to złożony format; jego specyfikacja obsługuje wiele funkcji, ale nie każde oprogramowanie 3D je wspiera. Na przykład OSX/iOS nie obsługują kolorów wierzchołków.  
Tryby preset w eksporterze USD próbują jak najlepiej dopasować się do kompatybilności z OpenUSD, Apple, Procreate, ZBrush.

::: 

## Render {#render}

Eksport obrazu, który jest kombinacją wszystkich ustawień w projekcie (światła, materiały, postprocessing itd.). 

![](/images/file_render.webp)
### Podgląd {#preview}

Mały przycisk podglądu obok tytułu menu przyciemni paski narzędzi, aby ułatwić podgląd końcowego rezultatu.

### Przezroczyste tło {#transparent-background}
Włącz kanał alfa dla renderu; przydatne do łączenia renderu z innymi obrazami w programach 2D. Zauważ, że częściowa przezroczystość nie jest obsługiwana.

### Pokaż interfejs {#show-interface}
Włącz dołączanie interfejsu Nomad do renderu.

### Proporcje renderu {#render-ratio}
Mnożnik rozdzielczości obrazu.

### Ostateczny rozmiar {#final-size}
Rozdzielczość używana do renderu. Gdy wybrana jest opcja `Custom`, suwaki szerokości i wysokości zostaną włączone. 

Gdy menu Plik jest aktywne, w widoku zostanie narysowany przerywany obrys wskazujący obszar renderu, jeśli nie odpowiada on rozdzielczości ekranu (zauważ, że aby był poprawny, musisz być w trybie poziomym).

### Eksportuj PNG {#export-png}
Kliknij ten przycisk, aby rozpocząć proces renderowania. Po zakończeniu możesz wybrać sposób zapisania lub udostępnienia obrazu.