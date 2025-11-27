# ![](/icons/scene.webp) Scena 

To menu pozwala zarządzać obiektami, światłami, kamerami i replikatorami (repeaters) w Nomadzie. Wyświetla hierarchię sceny w postaci drzewa, umożliwiając modyfikację wielu aspektów obiektów. Pozwala także tworzyć nowe obiekty oraz łączyć i rozdzielać obiekty na różne sposoby.


![](/images/scene_menu_summary.webp)


## Pasek skrótów
| Akcja                 | Ikona                             | Opis                                                                                                              |
| :-------------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| [Dodaj...](#add-menu) | ![](/icons/plus.webp)            | Wyświetl [menu Dodaj](#add-menu), aby dodać obiekt do sceny                                                       |
| Usuń                  | ![](/icons/trash.webp)           | Usuń obiekt                                                                                                       |
| Zablokuj              | ![](/icons/lock.webp)            | Uczyń obiekt niemożliwym do zaznaczenia w widoku 3D. Nadal można go zaznaczyć z drzewa sceny.                    |
| Połącz                | ![](/icons/merge.webp)           | Połącz zaznaczone obiekty w jeden obiekt bez zmiany geometrii                                                     |
| Rozdziel              | ![](/icons/diagonal.webp)        | Jeśli obiekt składa się z oddzielnych „skorup” poligonów, rozbij go na osobne obiekty. Odwrotność operacji Połącz |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | Wyświetl menu [Boolean](#boolean)                                                                                 |
| Klonuj                | ![](/icons/clone.webp)           | Duplikuj obiekt jako nowy, niezależny obiekt                                                                      |
| Instancja             | ![](/icons/link.webp)            | Duplikuj obiekt jako instancję, tak aby zmiany modelowania jednego były stosowane do wszystkich instancji        |
| Usuń instancję        | ![](/icons/unlink.webp)          | Zamień instancję w unikalny kształt, aby zmiany modelowania nie były już kopiowane do innych instancji           |
| Synchronizuj          | ![](/icons/link.webp)            | Jeśli instancje mają dzieci, upewnij się, że wszystkie instancje mają tę samą hierarchię dzieci                   |


## Widok drzewa
![](/images/scene_treeview.webp) 

| Akcja        | Ikona                      | Opis                      |
| :----------: | :------------------------: | :-----------------------: |
| Zaznacz      | ![](/icons/checked.webp)  | Przełącz zaznaczone/niezaznaczone |
| Widoczny     | ![](/icons/eye_open.webp) | Przełącz widoczność       |
| Menu         | ![](/icons/more.webp)     | Wyświetl menu obiektu     |

::: tip WSKAZÓWKA: Szybkie zaznaczanie lub ukrywanie wielu obiektów

Stuknij ikonę zaznaczenia, aby przełączyć pojedynczy obiekt, lub przeciągnij pionowo po kolumnie zaznaczenia, aby zaznaczyć wiele obiektów. To samo można zrobić z kolumną widoczności.

:::

### Manipulacja w widoku drzewa

Przytrzymaj długo element w widoku drzewa, aż zmieni kolor na żółty. Następnie możesz przesuwać go w górę lub w dół w drzewie, a także przeciągnąć na inny element, aby stał się jego dzieckiem.

Gdy zaznaczonych jest wiele elementów, większość będzie ciemnożółta, jeden będzie jaśniejszy. Przytrzymaj długo i przeciągnij jaśniejszy element, aby przesunąć wszystkie obiekty naraz.

Gdy zaznaczysz element nadrzędny, domyślnie wszystkie elementy podrzędne również zostaną zaznaczone. Stuknięcie ikony rodzica przełącza między zaznaczeniem tylko rodzica a rodzica z dziećmi.

### Menu obiektu

Kliknięcie przycisku z wielokropkiem (...) dla obiektu w widoku drzewa wyświetli menu obiektu. 
Wiele z tych opcji jest podobnych do paska skrótów u góry, powtórzonych dla wygody.

|       Akcja        |                        Ikona                        | Opis                                                                                                                                                                     |
| :----------------: | :-------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     Instancja      |               ![](/icons/link.webp)               | Duplikuj obiekt jako instancję, tak aby zmiany modelowania jednego były stosowane do wszystkich instancji.                                                             |
|       Klonuj       |              ![](/icons/clone.webp)               | Duplikuj obiekt jako nowy, niezależny obiekt                                                                                                                            |
|       Nazwa        |              ![](/icons/pencil.webp)              | Zmień nazwę obiektu                                                                                                                                                     |
|       Usuń         |              ![](/icons/trash.webp)               | Usuń obiekt                                                                                                                                                             |
|      Usuń+         |            ![](/icons/removeNode.webp)            | Usuń obiekt wraz z jego dziećmi                                                                                                                                         |
|   Usuń instancję   |              ![](/icons/unlink.webp)              | Zamień instancję w unikalny kształt, aby zmiany modelowania nie były już kopiowane do innych instancji.                                                                |
| Rozdziel topologię |             ![](/icons/separate.webp)             | Jeśli obiekt składa się z oddzielnych „skorup” poligonów, rozbij go na osobne obiekty. Odwrotność operacji Połącz.                                                     |
| Rozdziel grupę ścian |            ![](/icons/faceGroup.webp)          | Jeśli obiekt ma wiele grup ścian (face groups), rozbij siatkę na osobne obiekty.                                                                                        |
|  Rozdziel warstwy  |              ![](/icons/layer.webp)               | Jeśli obiekt ma warstwy, rozdziel każdą warstwę do osobnego obiektu. Przydatne przy wysyłaniu blendshape’ów do innych aplikacji.                                       |
| Połącz -> Warstwy  | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Jeśli zaznaczono wiele obiektów o pasującej topologii, połącz te obiekty w warstwy głównego obiektu (pozostałe obiekty zostaną usunięte). Ponownie przydatne dla blendshape’ów pochodzących Z innych aplikacji.<br><br> Zwróć uwagę, że warstwy będą domyślnie wyłączone. Włącz je, jeśli chcesz regulować ich suwaki. |




### Wielokrotne zaznaczanie
Możesz zaznaczyć wiele obiektów, aby osiągnąć dwie rzeczy:
- używać narzędzia gizmo do jednoczesnego przesuwania kilku obiektów
- łączyć obiekty za pomocą operacji Połącz i Boolean.

Możesz to zrobić, zaznaczając pole `Multiselection`, a następnie klikając obiekty na liście.

::: tip Szybkie wielokrotne zaznaczanie
Możesz także zaznaczać wiele obiektów w widoku 3D, przytrzymując skrót `Smooth` i stukając w inną siatkę.

Możesz odznaczyć obiekt, stukając go ponownie (tylko jeśli w zaznaczeniu jest więcej niż jeden obiekt).
:::

::: warning Ograniczenia gizmo
Przy wielokrotnym zaznaczeniu narzędzie gizmo zawsze ignoruje maskowanie.
Skalowanie X/Y/Z jest również wyłączone.

Powodem jest to, że wielokrotne zaznaczenie pozwala tylko na transformację całej siatki, a nie na transformację wierzchołków.
Może to zostać ulepszone w przyszłości.
:::


## Połącz
Ta opcja po prostu utworzy jeden wpis obiektu z wielu zaznaczonych obiektów.

Przykład wideo można zobaczyć w sekcji [Rozdziel](#separate).

## Boolean
![](/images/scene_boolean_menu.webp) 
Łącz obiekty w jedną powierzchnię.

`Voxel merge` zachowa objętość obiektów i obliczy nowe, równomiernie rozmieszczone poligony na powierzchni. Ze względu na etap obliczeń łączenie wokselowe radzi sobie złożoną geometrią, ale może utracić drobne detale, jeśli docelowa rozdzielczość nie jest wystarczająco wysoka.

`Boolean` spróbuje pozostawić poligony w ich oryginalnym układzie i zszyć je w miejscach, gdzie obiekty się nakładają. Może to dać znacznie czystsze i ostrzejsze rezultaty niż łączenie wokselowe, jednak wymaga „szczelnych” siatek; w obiektach nie może być dziur ani uszkodzonych kształtów. Jeśli to się nie powiedzie, zazwyczaj zadziała łączenie wokselowe.

### Operacje Boolean
Zarówno Voxel Merge, jak i Boolean używają widoczności obiektów do sterowania operacją:

#### Union
Oba obiekty widoczne utworzą **sumę** (union) boolowską – zewnętrzna „skóra” obiektów zostanie połączona, bez wewnętrznych powierzchni. ![](/images/boolean_union.webp)

#### Subtract
Jeden obiekt niewidoczny = **różnica** (subtract) boolowska – niewidoczny obiekt zostanie odjęty od widocznego. ![](/images/boolean_subtract.webp)

#### Intersect
Oba obiekty niewidoczne = **część wspólna** (intersection) boolowska – powstanie nowy kształt tylko w miejscu, gdzie obiekty się nakładają. ![](/images/boolean_intersect.webp)


### Przycisk Voxel Merge
Naciśnięcie tego przycisku wykona operację łączenia wokselowego na zaznaczonych obiektach. Wykonane na pojedynczym obiekcie przetopologizuje go do równomiernie rozmieszczonych poligonów, co jest przydatne, gdy obiekt ma rozciągnięte poligony.

### Resolution
Rozdzielczość trójwymiarowej siatki wokseli używanej do obliczeń. Po zmianie tej wartości na obiekt nakładany jest wzór szachownicy, aby podglądnąć rozmiar poligonów.

### Build multiresolution
Utwórz poziomy wielorozdzielczości poniżej docelowej rozdzielczości. Jeśli więc rozdzielczość wynosi 400, a build multiresolution to 3, otrzymasz nową siatkę z np. 296 000 poligonów, ale będą 3 niższe poziomy subdiv: 74 000, 18 000, 4 000.

### Keep sharp edges
Włącz przyciąganie siatki wokselowej do krawędzi. Najlepiej działa na prostych kształtach.

### Przycisk Boolean
Naciśnięcie tego przycisku wykona operację boolowską na poligonach z użyciem biblioteki Manifold autorstwa Emmetta Lalisha. 


## Separate
Jeśli masz pojedynczy obiekt złożony z kilku niepołączonych części, możesz rozdzielić go na kilka obiektów. 
Można to traktować jako przeciwieństwo [prostego łączenia](#simple-merge).

![](/videos/merge_separate.mp4)


## Add menu

![](/images/scene_addmenu_overview.webp)

To menu tworzy prymitywy, grupy, kamery, repeatery i światła.

Prymitywy to podstawowe typy kształtów, które można regulować za pomocą parametrów. Gdy dopasujesz prymityw do swoich potrzeb, „walidujesz” go, co sprowadza parametry do siatki poligonowej, którą można rzeźbić i malować. Po walidacji prymitywu nie można już zmieniać jego parametrów.


![](/images/scene_addmenu_top.webp)

### On gizmo
Włącz umieszczanie nowego prymitywu w miejscu aktualnie zaznaczonego kształtu lub gizma. Gdy wyłączone, prymityw zostanie umieszczony w centrum sceny.

### Select gizmo
Włącz automatyczne przełączanie na narzędzie gizmo po utworzeniu nowego prymitywu. 

### Advanced

To menu pozwala ustawić preferencje dotyczące miejsca tworzenia nowych prymitywów, grup i repeaterów. Mogą być tworzone na zaznaczonym obiekcie, w początku układu współrzędnych (world origin) lub w miejscu gizma.


### UV's
Włącz UV dla prymitywów. UV (często nazywane współrzędnymi tekstury) to dodatkowe dane używane w 3D, aby umożliwić nakładanie tekstur na powierzchnie. Zajmują więcej pamięci, ale dla większości urządzeń nie powinno to być problemem, chyba że pracujesz na bardzo wysokich liczbach poligonów (np. 10 milionów i więcej). 

### Primitives

| Prymityw       | Ikona                                     | Opis                                                                                                              |
| :------------: | :---------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Prosty sześcian, możesz kontrolować podziały w X, Y i Z                                                           |
| Sphere         | ![](/icons/circle.webp)                  | Dla wygody nazwana „Sphere”, ale w rzeczywistości to podzielony sześcian z wymuszonym `Project on sphere`        |
| Cylinder       | ![](/icons/cylinder.webp)                | Możesz dodać otwór w środku walca, np. aby zrobić pustą rurę                                                      |
| Torus          | ![](/icons/torus.webp)                   | Torus może być dobrym punktem wyjścia dla pierścieni                                                              |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                                 |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                                 |
| UV-sphere      | ![](/icons/circle.webp)                  | Sfera z nierównym układem poligonów, zobacz [ostrzeżenie poniżej](#uv-sphere)                                     |
| Plane          | ![](/icons/rectangle.webp)               | Prosta płaszczyzna, jedyny prymityw, który nie jest zamknięty                                                     |
| Tube           | ![](/icons/tool_tube.webp)               | zobacz [Tube](tools#tube)                                                                                         |
| Lathe          | ![](/icons/tool_lathe.webp)              | zobacz [Lathe](tools#lathe)                                                                                       |
| Triplanar      | ![](/icons/triplanar.webp)               | zobacz [Triplanar](#triplanar)                                                                                    |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | zobacz [Shadow Catcher](#shadow-catcher)                                                                          |
| Head           | ![](/icons/face.webp)                    | Prosta głowa z warstwą do mieszania między męską/żeńską                                                           |

::: tip
Jeśli zastanawiasz się, jaka jest siatka bazowa po uruchomieniu Nomada: to również podzielony sześcian.
Jednak siatka bazowa w Nomadzie nie używa `Project on sphere`, co oznacza, że nie jest idealnie okrągła.
:::

### Pasek narzędzi prymitywu

![](/images/scene_primitive_toolbar.gif)

Po utworzeniu prymitywu pojawi się pasek narzędzi do sterowania jego parametrami.

* `Validate` Wypal prymityw do standardowego obiektu, aby można go było rzeźbić i malować.
* `Edit` Przełącz wyświetlanie gizma prymitywu. Jest ono pokazane bezpośrednio na prymitywie, aby kontrolować jego parametry, np. szerokość sześcianu lub promień otworu walca.
* `Mirror` Przełącz umieszczenie repeatera lustrzanego nad prymitywem.
* `...` Wyświetl menu prymitywu.

Różne prymitywy mają dodatkowe opcje na pasku narzędzi:

* `Project` Sfera jest skonstruowana jako podzielony sześcian, co jest lepsze do rzeźbienia, ale oznacza, że nie jest idealnie okrągła. Ta opcja wymusi kształt bliższy idealnej sferze. Icosahedron ma tę samą opcję.
* `Cap` Przełącz zaślepki końcowe kształtu, np. walec może mieć zaślepki na górze, na dole, na obu końcach lub żadnych.
* `Hole` Przełącz tworzenie otworu przez środek kształtu. Przełącza między brakiem otworu, otworem o jednym promieniu lub otworem o różnych promieniach na górze i na dole.
* `Radius` Przełącz, czy walec ma mieć jeden promień, czy różne promienie na górze i na dole.
* `Disk` Przełącz, czy płaszczyzna ma być kształtem czterokątnym, czy okrągłym.

Mały pasek narzędzi pod głównym paskiem pozwala przełączać się między gizmem prymitywu a gizmem transformacji.

::: tip

Kliknięcie tytułu paska narzędzi przełączy go między górą a dołem ekranu. Kliknięcie strzałki w rogu zwinie go.

:::


### Menu prymitywu

![](/images/scene_primitive_menu.webp)

Zawiera wszystkie parametry zaznaczonego prymitywu. Parametry to podstawowy opis kształtu. Aby opisać pierścień, na przykład, określisz jego promień zewnętrzny, promień wewnętrzny i liczbę poligonów.

Większość parametrów prymitywów jest dość oczywista, a część jest wspólna dla wszystkich prymitywów:

* `UVs` Mały przycisk UVs na górze menu przełącza tworzenie współrzędnych UV
* `Validate` Mały przycisk validate wypala prymityw do standardowego obiektu, aby można go było rzeźbić i malować.
* `Max faces` Ustaw górny limit liczby poligonów w obiekcie, aby uniknąć zawieszenia urządzenia.
* `Post subdivision` Włącz wybraną liczbę poziomów podziału z sekcji multiresolution w menu topologii. Można tego użyć do tworzenia wygładzonych prymitywów z miękkimi krawędziami w połączeniu z niskimi podziałami topologii. Na przykład ustaw podziały topologii sześcianu na 2, a post subdivisions na 4 – otrzymasz sześcian z gładkimi narożnikami.
* `Linear subdivision` Ustaw, ile poziomów podziału liniowego użyć przed zastosowaniem zwykłego gładkiego podziału. Pozwala to kontrolować, jak ostre lub miękkie są krawędzie na podzielonych powierzchniach. Np. ustaw podziały topologii sześcianu na 2, post subdivisions na 4, a następnie zmieniaj linear subdivisions między 0 a 4. Narożniki sześcianu przejdą od miękkich do ostrych.

### Topology

Kontroluje liczbę poligonów w prymitywie. Zwykle suwaki są połączone, więc zmiana aktywnego suwaka równomiernie dostosuje wszystkie poligony. Możesz stuknąć przycisk rozłączenia i sterować podziałami X/Y/Z kształtu osobno.

### Geometry

Kontroluje ogólny rozmiar prymitywu – w jednostkach X/Y/Z dla kształtów „kwadratowych” oraz w promieniu dla kształtów okrągłych.


### UV Sphere
::: warning
UV Sphere nie nadaje się dobrze do rzeźbienia, szczególnie w okolicach biegunów.

Preferuj prymitywy [Sphere](#sphere), [Box](#box) lub [Icosahedron](#icosahedron) wraz z opcją `Project on sphere`.

Zauważ, że topologia może być akceptowalna do rzeźbienia, jeśli użyjesz bardzo niskiej wartości suwaków `Division`.
Możesz wtedy użyć suwaka `Overall Subdivision`, aby zwiększyć liczbę poligonów.

Choć nie nadaje się do ogólnego rzeźbienia, jest przydatna do oczu; jeśli obrócisz sferę tak, aby bieguny znalazły się w miejscu źrenicy, układ poligonów naturalnie dopasuje się do malowania i rzeźbienia tęczówki i źrenicy.
:::


### Triplanar
Ten prymityw jest szczególny, ponieważ do kształtowania geometrii powinieneś używać [narzędzia Mask](tools.md#mask).

![](/videos/triplanar.mp4)


::: tip
Podwójne stuknięcie w płaszczyznę spowoduje, że kamera skupi się na tej konkretnej płaszczyźnie.
Nie zadziała to jednak, jeśli obrócisz prymityw gizmem.
:::

Triplanar używa informacji maski z 3 płaszczyzn do wypełnienia siatki wokseli, która jest następnie poligonizowana (dzięki [Voxel Remesher](topology.md#voxel-remeshere)).

Każda płaszczyzna ma własną płaszczyznę symetrii.

::: warning
Za każdym razem, gdy zaktualizujesz rozmiar prymitywu Triplanar, jakość malowania maski ulegnie pogorszeniu.

Na razie nie ma opcji „zablokowania” malowania na pojedynczej płaszczyźnie, ale być może pojawi się w przyszłości.
Możesz użyć [Connected Topology](stroke.md#connected-topology), aby trochę pomóc – jeśli kursor leży dokładnie na jednej płaszczyźnie, nie wpłynie na pozostałe.
:::

### Shadow Catcher
Dodaj płaszczyznę z materiałem shadow catcher. Zobacz [materiał Shadow Catcher](material.md#shadow-catcher), aby uzyskać więcej szczegółów. 


## Group/Camera
### Group
Utwórz „pusty” obiekt, pod który możesz podpinać inne obiekty. Można go użyć po prostu do organizacji hierarchii, umieszczając wiele obiektów w grupie, a następnie ją zwijając. Grupa może też służyć jako pomoc przy przemieszczaniu obiektów; wiele obiektów można umieścić w grupie, a następnie przesuwać, obracać i skalować grupę narzędziem gizmo.

### Add view
Utwórz kamerę.

## Repeaters
![](/images/scene_primitive_repeaters.webp)

Repeatery to węzły tworzące instancje obiektów znajdujących się pod nimi. 

### Array
![](/images/scene_primitive_array.webp)

Gdy obiekty są dziećmi tego węzła, mogą być instancjowane w układzie siatki. Po zaznaczeniu ma on następujące kontrolki:
* Fit inside – przełączanie między kontrolą rozmiaru siatki/pudełka array a kontrolą odstępu między instancjami
* CountX/Y/Z – liczba instancji na każdej osi
* OffsetX/Y/Z – odległość między instancjami, gdy fit inside jest przełączone
* SizeX/Y/Z – szerokość/wysokość/głębokość całej siatki array, gdy fit inside jest przełączone.

### Curve
![](/images/scene_primitive_curve.webp)
Tworzy krzywą, a dzieci tego węzła będą powtarzane wzdłuż krzywej. Po zaznaczeniu ma następujące kontrolki:
* Edit – pozwala dodawać punkty do krzywej i przesuwać punkty na krzywej.
* Snap – przyciąga punkty krzywej do innej geometrii
* Align – obraca kształty potomne, aby wyrównać je w kierunku krzywej
* Count – liczba instancji
* Closed – przełącz, czy krzywa łączy początek i koniec, czy jest otwarta
* Radius – przełącz kontrolki na każdym punkcie krzywej do sterowania skalą instancji
* Twist – przełącz kontrolki na każdym punkcie krzywej do sterowania skrętem (rotacją) instancji 
* B-spline – przełącz, czy instancje mają dokładnie podążać za krzywą, czy używać interpolacji B-spline dla gładszych rezultatów. 

### Radial
![](/images/scene_primitive_radial.webp)

Dzieci tego węzła będą instancjowane w okręgu. Przesuń obiekt potomny, aby zmienić promień repeatera. Po zaznaczeniu ma następujące kontrolki:
* RadialX/Y/Z – wybranie tych przycisków ustawia oś radialną i liczbę instancji.



### Mirror
![](/images/scene_primitive_mirror.webp)

Dzieci tego węzła będą lustrzane względem osi. Po zaznaczeniu ma następujące kontrolki:
* Gizmo – włącz gizmo transformacji, aby ustawić środek lustrzanego odbicia. Można je także obracać i skalować. Po zakończeniu stuknij ponownie gizmo, aby przywrócić standardowe kontrolki.
* X/Y/Z – ustaw płaszczyznę lustrzaną

Wszystkie repeatery mają kontrolkę `Validate`, która wypala wynik repeatera i pyta, jak wykonać wypalanie:
* Join children – instancje są łączone w jeden obiekt
* Keep instances – instancje pozostają instancjami, ale nie mają już repeatera jako „rodzica”
* Un-instances – instancje są konwertowane na unikalne obiekty

::: tip Wskazówka: Łączenie repeaterów
Repeatery można zagnieżdżać jeden pod drugim, a kilka obiektów może być dziećmi repeaterów, co prowadzi do złożonych efektów.

![](/images/scene_repeater_combine.webp)
:::

::: tip Wskazówka: Pivoty repeaterów

Niektóre repeatery próbują automatycznie ustawić pivot obiektów potomnych, więc nawet jeśli przesuwasz lub obracasz je gizmem, nie będą się poruszać. Jeśli chcesz nadpisać to zachowanie, wstaw grupę między repeater a dziecko. Teraz możesz przesuwać kształt potomny niezależnie od repeatera.
:::

## Light

![](/images/scene_primitive_light.webp)

### Directional
Utwórz światło kierunkowe, nieskończenie odległe źródło światła, jak słońce.

### Spot
Utwórz reflektor (spot light) z kontrolą szerokości stożka i miękkości krawędzi

### Point
Utwórz światło punktowe

## Advanced
### Focus on item
Podwójne kliknięcie elementu na liście Sceny wycentruje kamerę na tym elemencie w widoku 3D.

### Sync visibility
Użycie ikony oka wpłynie na wszystkie zaznaczone elementy. 

### Instance: Show
Wyświetl kolorową kapsułkę po lewej stronie listy sceny, aby pokazać instancje.


### Icons
Ustaw rozmiar i przezroczystość ikon grup, świateł, kamer i luster w widoku 3D

### Hierarchy lines
Wyświetl linię między rodzicem a jego dziećmi w widoku 3D

## Dolny pasek narzędzi
Te ikony przełączają widoczność grup, świateł, kamer, repeaterów i linii hierarchii w widoku 3D.
