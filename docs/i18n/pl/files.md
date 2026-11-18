# ![](/icons/open.webp) Pliki {#files}

Menu Pliki pozwala zapisywać i wczytywać projekty Nomad, importować i eksportować modele 3d, eksportować wyrenderowane obrazy oraz łączyć Nomad z innymi aplikacjami. Ma trzy zakładki: `Pliki`, `Renderuj` i `Połączenie`.

![](/images/file_menu.webp)

## Projekt {#project}
![](/images/file_project.webp)

Miniatura na górze pokazuje bieżący projekt, a obok niej rozmiar pliku, automatyczny zapis i zapisaną historię. Stuknij miniaturę, aby otworzyć małą przeglądarkę projektów, a potem stuknij projekt, aby wyświetlić menu pozwalające go otworzyć, dodać, nadpisać, sklonować, zmienić jego nazwę lub go usunąć.

Gdy projekt ma jeszcze niezapisane zmiany, pod miniaturą pojawia się komunikat `Niezapisane zmiany!`.

### Zakres {#scope}
Na komputerze wybierz, gdzie mają być zapisywane projekty:
* `Wewnętrzny` - ustawienie domyślne, tak jak na urządzeniach mobilnych. Projekty są zapisywane tylko w głównym folderze Nomad.
* `Oryginalny plik` - gdy otworzysz projekt spoza folderu Nomad, zapis nadpisuje oryginalny plik. Automatyczny zapis nie działa dla takich zewnętrznych projektów.

### ![](/icons/nomad.webp) Ustawienie wstępne {#preset}
Daje dostęp do kolekcji wersji demonstracyjnych i elementów postaci. Wybierz jeden z nich, a następnie stuknij go ponownie i wybierz `Otwórz` lub `Dodaj do sceny`. W tej przeglądarce możesz też pobrać darmowe modele z Poly Haven.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Historia... {#history}
Szybki dostęp do opcji historii projektu, takich jak `Zapisz historię`, która zachowuje historię cofania przy zapisie projektu. Zielona plakietka na przycisku oznacza, że historia jest zapisywana razem z projektem. Szczegóły znajdziesz w sekcji [Historia](history.md#save-history).

### ![](/icons/save.webp) Zapisz {#save}
Zapisuje projekt Nomad. Jeśli projekt nie był jeszcze zapisany, zostaniesz poproszony o podanie nazwy.

### ![](/icons/save_as.webp) Zapisz jako... {#save-as}
Zapisuje projekt pod nową nazwą, jako nowy projekt.

### ![](/icons/save_as.webp) Nadpisać... {#overwrite}
Wyświetla przeglądarkę projektów, aby zapisać bieżącą scenę w miejsce innego projektu. Włącz `Dołącz tylko zaznaczone obiekty`, aby zapisać tylko zaznaczone obiekty zamiast całej sceny. Przeglądarka ma też przycisk `Zapisz jako...`, który zamiast tego zapisuje scenę jako nowy projekt.

### ![](/icons/pencil.webp) Zmień nazwę {#rename}
Wyświetla pole tekstowe, w którym możesz zmienić nazwę bieżącego projektu.

### ![](/icons/open.webp) Otwórz... {#open}
Wyświetla przeglądarkę projektów, aby otworzyć projekt.

### ![](/icons/add_file.webp) Dodaj do sceny... {#add}
Wyświetla przeglądarkę projektów. Gdy wybierzesz projekt, jego zawartość zostanie scalona z bieżącą sceną.

### ![](/icons/trash.webp) Usuń... {#delete}
Wyświetla przeglądarkę projektów. Wybrane projekty zostaną usunięte z systemu plików.

### ![](/icons/new_file.webp) Nowy {#new}
Rozpoczyna nowy projekt. Jeśli masz niezapisane zmiany, zostaniesz poproszony o potwierdzenie. W oknie potwierdzenia możesz wybrać `Zachowaj` lub `Wyzeruj` dla ustawień `Tło`, `Środowisko`, `MatCap` i `Prześwietlenie`, a także zdecydować, czy nowy projekt ma używać opcji `Zapisz historię`.

### ![](/icons/autosave.webp) Automatyczny zapis... {#auto-save}
Menu z opcjami automatycznego zapisu. Włącz `Automatyczny zapis`, aby projekt był regularnie zapisywany w osobnym pliku. Plakietka na przycisku pokazuje, czy ta opcja jest włączona.

Nomad nie zapisuje w tle, ponieważ pliki 3d mogą być dość duże, co mogłoby powodować wyraźne przycięcia podczas rzeźbienia.

Dodatkowo, aby uniknąć problemów z brakiem pamięci, scena jest zwykle kompresowana przed zapisem.
Ta kompresja i dekompresja także spowalnia zapis.

### Interwał zapisu {#timer-pop-up}
Ile minut Nomad odczekuje między kolejnymi automatycznymi zapisami.

### Pokaż odliczanie {#popup-timeout}
Wyświetla odliczanie przed każdym automatycznym zapisem, więc możesz go anulować, jeśli jesteś w trakcie pracy. Gdy ta opcja jest wyłączona, Nomad zapisuje, gdy tylko przestaniesz rzeźbić.

### ![](/icons/trash.webp) Odrzuć automatyczny zapis {#discard-autosave}
Jeśli dla projektu istnieje plik automatycznego zapisu, zostanie on wczytany automatycznie zamiast oryginalnego projektu. Jeśli tego nie chcesz, ten przycisk usunie automatyczny zapis. Przy wczytywaniu pliku zostanie wtedy wczytany ostatni ręczny zapis projektu.

### ![](/icons/open.webp) Otwórz przestarzały zapis {#open-outdated-save}
Gdy projekt ma zarówno automatyczny, jak i ręczny zapis, ten przycisk otwiera starszy z nich (`Otwórz przestarzały autozapis` lub `Otwórz przestarzały zapis ręczny`), wraz z jego datą. Przydaje się, gdy najnowszy zapis nie jest tym, o który Ci chodziło.

### ![](/icons/storage.webp) Ostatnio usunięte... {#recently-deleted}
Nomad przechowuje dane projektów, które zniknęły z folderu projektów, oraz pliki zastąpione przez import, przez określoną liczbę dni, zanim usunie je na dobre. Pliki, których nie udało się zaimportować, pozostają, dopóki sam ich nie usuniesz. Ta lista pokazuje je wraz z rozmiarem i datą, więc możesz usuwać je pojedynczo lub przyciskiem `Usuń wszystko`.

## Importuj {#import}

### ![](/icons/add_file.webp) Importuj {#import-button}
Służy do importowania plików 3d, które nie są projektami Nomad.

Gdy importujesz do Nomad zewnętrzny plik sceny, możesz go *dodać* albo rozpocząć z nim *nowy* projekt.

Dodanie pliku po prostu dodaje obiekty do bieżącej sceny.
Wybranie `Nowy` utworzy nowy projekt Nomad zawierający nowe obiekty.

Okno importu wyświetla każdy wybrany plik z jego własnymi opcjami importu. W ten sposób możesz też importować obrazy: dla każdego z nich wybierz, czy ma się stać `HDRI`, `MatCap`, `Obraz referencyjny`, `Alfa`, `Tekstury` czy `VDM`.

Nomad może importować następujące formaty:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), na platformach, które go obsługują

### ![](/icons/cog.webp) Ustawienia {#advanced}
Przycisk `Ustawienia...` obok miniatury projektu wyświetla główne opcje importu. Te ustawienia nie są zapisywane, a okno importu pokazuje opcje, które dotyczą importowanych plików.

### Wszystkie formaty {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Zachowaj topologię {#keep-topology}
Domyślnie Nomad przy wczytywaniu próbuje naprawić problematyczną geometrię. Włączenie tej opcji sprawia, że Nomad nie zmienia kolejności wierzchołków i ścian, nie scala duplikatów i nie usuwa nieużywanych wierzchołków.

::: warning
Z opcją `Zachowaj topologię` operacje takie jak Boolean, Połącz, Uprość czy Manifold mogą nie scalić zduplikowanych wierzchołków.
:::

#### ![](/icons/image.webp) Pomiń tekstury {#skip-textures}
Nie wczytuje tekstur osadzonych w pliku, w formatach, które na to pozwalają, takich jak glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Wczytaj ustawienia interfejsu {#keep-gui-settings}
Przy otwieraniu lub importowaniu pliku projektu wczytuje wszystkie zapisane w nim ustawienia interfejsu.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Podziel OBJ według grup {#split-obj-by-groups}
Rozdziela grupy OBJ na osobne obiekty.

#### ![](/icons/vertex.webp) Połącz zduplikowane pozycje {#merge-duplicate-positions}
Scala wierzchołki, które mają tę samą pozycję.

#### ![](/icons/uv.webp) Połącz zduplikowane UV {#merge-duplicate-uvs}
Scala współrzędne tekstury, które mają te same UV.

#### ![](/icons/paint.webp) Przestrzeń kolorów {#color-space}
Określa, jak interpretować kolory z pliku: `Auto`, `Liniowy` lub `sRGB`. Jeśli kolory wyglądają niepoprawnie, spróbuj przełączyć tę opcję.

#### ![](/icons/image.webp) Format {#normal-format}
Format map normalnych w teksturach: `Auto`, `OpenGL (+Y)` lub `DirectX (-Y)`. Jeśli detale mapy normalnych wyglądają na odwrócone, wypróbuj drugi.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Przestrzeń kolorów {#color-space-ply}
Określa, jak interpretować kolory z pliku: `Auto`, `Liniowy` lub `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Połącz zduplikowane UV {#merge-duplicate-uvs-fbx}
Scala współrzędne tekstury, które mają te same UV.

#### ![](/icons/paint.webp) Przestrzeń kolorów {#color-space-fbx}
Określa, jak interpretować kolory z pliku: `Auto`, `Liniowy` lub `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Format map normalnych w teksturach: `Auto`, `OpenGL (+Y)` lub `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Przestrzeń kolorów {#color-space-usd}
Określa, jak interpretować kolory z pliku: `Auto`, `Liniowy` lub `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Format map normalnych w teksturach: `Auto`, `OpenGL (+Y)` lub `DirectX (-Y)`.



## Eksportuj {#export}
Zapisuje geometrię w formacie 3d, którego można używać w innych programach. 

![](/images/file_export.webp)

Różne formaty plików obsługują różne funkcje, więc dostępne opcje zmieniają się w zależności od wybranego typu pliku.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Kolory wierzchołków](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR wierzchołków](#pbr-paint)  | ✅     | Nomad ✅<br>Inne ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Czworokąty                      | ✅     | Nomad ✅<br>Inne ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Warstwy](#layers)              | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Obiekty                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Grupa powierzchni               | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchia                      | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Światła                         | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Tekstury                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Prymitywy, postprocessing itp.  | ✅     | Nomad ✅<br>Inne ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Przycisk eksportu {#export-button}
Kliknij go, aby wyeksportować geometrię z wybranymi ustawieniami. Przycisk pokazuje wybrany format i szacowany rozmiar pliku. Na Androidzie obok znajduje się przycisk `Udostępnij`, który wysyła plik prosto do innej aplikacji.

### Format pliku {#file-format}
Wybierz format eksportu: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` lub `USD`. NOMAD to własny format Nomad, którego inne programy nie wczytają, więc służy głównie do ponownego importu do Nomad.

### Dołącz {#allvisibleselected}
Wybierz, które obiekty mają zostać wyeksportowane: `Wszystkie`, `Widoczne` lub `Wybrane`. Liczba obok każdej opcji pokazuje, ile obiektów zostanie wyeksportowanych.

### Jeden plik na obiekt {#one-file-per-object}
Eksportuje każdy obiekt do osobnego pliku. Liczba pokazuje, ile plików zostanie zapisanych.

### Typ {#type}
Gdy eksport tworzy kilka plików (jeden plik na obiekt albo OBJ z teksturami), zapisz je w postaci `Folder` lub `Zip`. Niektóre aplikacje (Google Drive, One Drive itp.) nie obsługują importu folderów, więc możesz wtedy użyć Zip.

### Osadź historię {#embed-history}
Tylko NOMAD. Zapisuje historię cofania w pliku; zostanie ona przywrócona po otwarciu pliku w Nomad. Zwiększa to rozmiar pliku i wymaga eksportu całej sceny do jednego pliku.

### Osadź zasoby {#embed-assets}
Tylko NOMAD. Zapisuje w pliku Twoje własne matcapy, środowiska i czcionki. Wbudowane zasoby nie są osadzane.

### Kolory wierzchołków {#vertex-colors}
Eksportuje kolory wierzchołków, jeśli format pliku je obsługuje. Niektóre programy 3d potrafią je odczytać, ale nie wszystkie.

W przypadku OBJ możesz wybrać:
* `Brak` - bez kolorów.
* `RGB` - kolory są dopisywane po wierzchołkach.
* `MRGB (ZBrush)` - alternatywny sposób kodowania koloru, który obsługuje też dane maski.

### Przestrzeń kolorów {#color-space-export}
Tylko OBJ, z kolorami wierzchołków `RGB`. Zapisuje kolory jako `Liniowy` lub `sRGB`.

### Malowanie PBR {#pbr-paint}
Eksportuje malowanie chropowatości, metaliczności i maski. Inne programy mogą ignorować te dane.
Kolory wierzchołków PBR są eksportowane jako dodatkowe atrybuty kolorów wierzchołków.
Kanały są upakowane w następujący sposób:

|                | Kanał    |
| :------------: | :------: |
| Chropowatość   | R        |
| Metaliczność   | G        |
| Maskowanie     | B        |


### Warstwy {#layers}
Warstwy są obsługiwane za pomocą morph targetów glTF. glTF oficjalnie je obsługuje, więc powinny działać także w innych programach.
Nomad eksportuje też kolory, chropowatość i metaliczność każdej warstwy, ale inne programy je zignorują.

### Malowanie warstwy {#layer-painting}
Eksportuje malowanie warstw, zwykle ignorowane przez inne programy.

### Grupa powierzchni {#face-group}
Eksportuje grupy powierzchni. Czasami może to powodować problemy w innych programach.

### Zapisz obiekty {#write-objects}
Tylko OBJ. Zachowuje podział na osobne obiekty. Wyłącz tę opcję, aby wyeksportować wszystko jako jeden obiekt, na przykład żeby użyć funkcji „Mesh ID / Polygroup” w Substance Painter.

### Normalne {#normals}
Eksportuje informacje o normalnych. Pamiętaj, że przy imporcie innych formatów Nomad zawsze oblicza własne normalne.

### Styczne {#tangents}
Eksportuje informacje o stycznych, używane, gdy model ma mapy normalnych. 

### Tekstury {#textures}
Jeśli do materiału dodano tekstury, zostaną one wyeksportowane. Pamiętaj, że nie oznacza to wypalania tekstur: służą do tego opcje wypalania w menu Topologia.

### Format {#fbx-format}
Tylko FBX. `Binarny` jest mniejszy, ale może nie działać w każdej aplikacji, `ASCII` to plik tekstowy.

### Skompresowany {#compressed}
Tylko FBX. Zmniejsza rozmiar pliku kosztem wolniejszego eksportu i importu.

### Ustawienie wstępne {#usd-preset}
Tylko USD. Wybierz aplikację, dla której eksportujesz: `OpenUSD`, `Apple`, `Procreate` lub `Zbrush`. Niektóre opcje są dostępne tylko w niektórych ustawieniach wstępnych.

### Instancja {#instance}
Tylko USD. Eksportuje obiekty instancjonowane jako instancje, zamiast powielać ich geometrię.

### Zezwalaj na warpowanie {#allow-skew}
Tylko USD. Pozwala na pochylenie (skew) w przekształceniach macierzowych. Gdy ta opcja jest wyłączona, Nomad rozbija pochylone przekształcenia na osobne przekształcenia skalowania i obrotu.

### Powtarzacz {#repeater}
Tylko USD. Eksportuje kopie utworzone przez powtarzacze jako instancje.

### Połącz kopie {#join-copies}
Każdy obiekt razem z kopiami z jego powtarzacza staje się jednym obiektem.

::: tip Wskazówka: import chropowatości i metaliczności do Blendera

Blender potrafi importować glTF/glb, ale nie rozpoznaje automatycznie atrybutów wierzchołków dla metaliczności i chropowatości. Aby ich użyć, w edytorze materiałów utwórz węzeł Vertex Color i ustaw jego właściwość na kolejny atrybut koloru (zwykle Col.001). Podłącz węzeł „Separate XYZ”, a następnie wyślij X do roughness, a Y do Metallic.

Ten film pokazuje cały proces:

![](/videos/blender_pbr.mp4)

::: 

::: tip Wskazówka: obsługa funkcji USD

USD to złożony format: jego specyfikacja obejmuje wiele funkcji, ale nie każdy program 3d je wszystkie obsługuje. Na przykład OSX/iOS nie obsługują kolorów wierzchołków. Ustawienia wstępne w eksporterze USD starają się możliwie najlepiej zapewnić zgodność z OpenUSD, Apple, Procreate i Zbrush.

::: 

## ![](/icons/screen.webp) Renderuj {#render}

Eksportuje obraz łączący wszystkie ustawienia projektu (światła, materiały, postprocessing itd.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Podgląd {#preview}

Przycisk `Podgląd` obok tytułu menu sprawia, że interfejs staje się przezroczysty, co ułatwia ocenę kadru końcowego obrazu.

### ![](/icons/home.webp) Ostrość {#focus}
Kadruje scenę lub zaznaczenie tak, by mieściły się w rozmiarze renderu. Stuknij ponownie, aby przełączać się między nimi.

### ![](/icons/map.webp) Mapa wysokości {#heightmap}
Renderuje scenę jako mapę wysokości w skali szarości widzianą z kamery, na której najbliższe części są najjaśniejsze. Włączenie tej opcji przełącza rozmiar na `Kwadrat` i kadruje zaznaczenie. Mały pasek w widoku pozwala dostosować `Ostrość` gradientu.

Gdy `Mapa wysokości` jest włączona, obok przycisku eksportu pojawia się przycisk `Zapisz jako alfę`, który zapisuje render jako nową alfę pędzla zamiast eksportować plik.

### ![](/icons/opacity.webp) Przezroczyste tło {#transparent-background}
Dodaje do renderu kanał alfa, co przydaje się przy łączeniu renderu z innymi obrazami w programach 2d. Pamiętaj, że częściowa przezroczystość nie jest obsługiwana.

### ![](/icons/sliders.webp) Pokaż interfejs {#show-interface}
Dołącza interfejs Nomad do renderu.

### Końcowy rozmiar {#final-size}
Rozdzielczość renderu: `Ekran`, `720`, `1080`, `4096`, `Kwadrat` lub `Niestandardowy`.

Gdy menu Pliki jest aktywne, w widoku rysowana jest przerywana ramka wskazująca obszar renderu, jeśli nie odpowiada on rozdzielczości ekranu.

### Szerokość / Wysokość {#render-ratio}
Przy opcji `Niestandardowy` ustawiasz szerokość i wysokość obrazu. Przycisk łącza między dwoma suwakami zachowuje proporcje, gdy zmieniasz jeden z nich. Przy opcji `Kwadrat` można ustawić tylko szerokość.

### ![](/icons/export.webp) Eksportuj → PNG {#export-png}
Kliknij ten przycisk, aby rozpocząć renderowanie. Po zakończeniu możesz wybrać, jak zapisać lub udostępnić obraz. Przy bardzo dużych rozmiarach Nomad najpierw prosi o potwierdzenie: zapisz wcześniej projekt na wypadek, gdyby na urządzeniu zabrakło pamięci.

## ![](/icons/network.webp) Połączenie {#link}

Łączy Nomad z innym urządzeniem lub aplikacją, aby wysyłać i odbierać obiekty albo synchronizować zmiany na żywo. Jedno urządzenie jest hostem sesji, a pozostałe do niej dołączają.

### Włącz GoZ {#enable-goz}
Tylko na komputerze. Wymienia siatki z ZBrush na tym samym komputerze. `Wyślij` importuje je do ZBrush, `Pobierz` importuje z uruchomionego ZBrush: `Zaznaczenie` pobiera aktywny subtool, a `Scena` wszystkie subtoole. W każdej chwili możesz też nacisnąć GoZ w ZBrush.

### Tryb {#link-mode}
* `Wyłączone` - brak połączenia.
* `Host` - to urządzenie jest hostem sesji i czeka, aż inne do niej dołączą.
* `Dołącz` - wyszukuje urządzenia w pobliżu; stuknij nazwę hosta, aby do niego dołączyć.

Aby połączyć dwa egzemplarze Nomad, wybierz `Host` na jednym urządzeniu i `Dołącz` na pozostałych. Przy połączeniu z Blenderem hostem powinien być Nomad: przycisk pomocy obok tytułu `Połączenie` pokazuje, jak zainstalować rozszerzenie Nomad Blender Link.

### ![](/icons/network.webp) Port sieciowy {#network-port}
Port sieciowy używany przez połączenie. Zmień go tylko wtedy, gdy korzysta z niego już inna aplikacja.

### Wyślij / Pobierz {#send-get}
Po połączeniu przycisk `Wyślij` przesyła na drugie urządzenie Twoje `Zaznaczenie` lub całą scenę (`Scena`), a `Pobierz` pobiera je z niego. `Zastąp` usuwa bieżącą scenę, a następnie pobiera scenę z drugiego urządzenia.

### ![](/icons/link.webp) Synchronizacja na żywo {#live-sync}
Przesyła Twoje zmiany na drugie urządzenie na bieżąco, w trakcie pracy. `Widok roboczy` synchronizuje także kamerę. `Zmiany sceny` określa, które urządzenie wysyła zmiany: `Auto` przekazuje kierunek temu, na którym ostatnio coś się działo. Następnie wybierz, co ma być synchronizowane: `Obiekty i geometria`, `Materiały`, `Światła`, `Kamery`, a jeśli druga strona to obsługuje, także `Cieniowanie` i `Postprocessing`.

::: tip
Istniejące obiekty trzeba najpierw raz przesłać przyciskiem `Wyślij` lub `Pobierz`, aby je połączyć, zanim synchronizacja na żywo będzie mogła je aktualizować.
:::
