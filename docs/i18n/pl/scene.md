# ![](/icons/scene.webp) Scena {#scene}

To menu pozwala zarządzać obiektami, światłami, kamerami i repeaterami w Nomadzie. Pokazuje hierarchię sceny w postaci drzewa, w którym możesz zmieniać wiele właściwości obiektów. Pozwala też tworzyć nowe obiekty oraz łączyć je i dzielić na różne sposoby.


![](/images/scene_menu_summary.webp)


## Pasek skrótów {#shortcut-bar}
| Akcja                  | Ikona                             | Opis                                                                                                                |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Dodaj...](#add-menu)  | ![](/icons/plus.webp)            | Otwiera [menu Dodaj](#add-menu), aby dodać obiekt do sceny                                                          |
| Usuń                   | ![](/icons/trash.webp)           | Usuwa zaznaczone obiekty. Ich obiekty podrzędne zostają.                                                            |
| Zablokuj               | ![](/icons/lock.webp)            | Sprawia, że zaznaczonych obiektów nie da się zaznaczyć w widoku. Nadal można je zaznaczyć w drzewie. Zablokowanie grupy blokuje wszystko, co jest pod nią. Stuknij ponownie, aby odblokować. |
| [Połącz](#join)        | ![](/icons/merge.webp)           | Łączy zaznaczone obiekty w jeden obiekt bez zmian w geometrii                                                       |
| [Podziel...](#separate) | ![](/icons/separate.webp)        | Otwiera okno [Podziel](#separate), aby rozbić obiekt na kilka obiektów. Odwrotność łączenia                          |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Otwiera okno [Boolean](#boolean)                                                                               |
| Klonuj                 | ![](/icons/clone.webp)           | Powiela zaznaczone obiekty jako nowe obiekty                                                                        |
| Utwórz instancję       | ![](/icons/link.webp)            | Powiela zaznaczone obiekty jako instancje, więc zmiany modelowania jednej trafiają do wszystkich instancji.          |
| Anuluj instancję       | ![](/icons/unlink.webp)          | Zamienia instancję w osobny kształt, więc zmiany modelowania nie są już kopiowane do innych instancji                |
| Synchronizacja         | ![](/icons/checked.webp)         | Gdy jest zaznaczone, operacje działają na wszystkie instancje zaznaczonych obiektów, a nie tylko na zaznaczone. Dostępne tylko wtedy, gdy zaznaczenie zawiera instancje. [Karta Synchronizacja](#sync) w oknie `Zaawansowane` określa, które operacje stosują się do tego pola wyboru. |

::: tip
Gdy operacja wpłynie także na inne instancje, na jej przycisku pojawia się mała ikona łańcucha.
:::


## Drzewo {#tree-view}
![](/images/scene_treeview.webp) 

Drzewo zawiera obiekty, grupy, repeatery, światła i kamery sceny. Obok nazwy siatki widać liczbę jej wierzchołków, a gdy ma warstwy, kolorową ikonę warstwy. Każdy wiersz ma te przyciski:

| Akcja        | Ikona                      | Opis                     |
| :----------: | :------------------------: | :----------------------: |
| Nazwa        | ![](/icons/pencil.webp)   | Zmienia nazwę obiektu. Jeśli obiekt jest zaznaczony, nazwa zmienia się we wszystkich zaznaczonych obiektach naraz, z dodanym numerem. Przytrzymaj, aby zmienić nazwę razem z obiektami podrzędnymi. |
| Wybierz      | ![](/icons/checked.webp)  | Zaznacza lub odznacza    |
| Widoczne     | ![](/icons/eye_open.webp) | Pokazuje lub ukrywa      |
| Menu         | ![](/icons/more.webp)     | Otwiera [menu obiektu](#object-menu) |

::: tip WSKAZÓWKA: szybkie zaznaczanie lub ukrywanie wielu obiektów

Stuknij ikonę zaznaczenia, aby przełączyć pojedynczy obiekt, albo przeciągnij pionowo po kolumnie zaznaczenia, aby zaznaczyć wiele obiektów. To samo działa w kolumnie widoczności.

Przytrzymaj ikonę zaznaczenia lub widoczności, aby objąć też obiekty podrzędne.

:::

### Nagłówek drzewa {#tree-view-header}

Wiersz nad listą ma kilka pomocnych przycisków:

* ![](/icons/sort_down.webp) - zwija lub rozwija wszystkie grupy naraz.
* ![](/icons/preview.webp) - włącza lub wyłącza `Podglądy obiektów`, czyli małą wyrenderowaną miniaturę każdego obiektu na liście.
* ![](/icons/search.webp) - filtruje listę po nazwie.

### Porządkowanie drzewa {#tree-view-manipulation}

Przytrzymaj element w drzewie, aż zostanie podświetlony. Możesz go wtedy przesunąć w górę lub w dół, a także upuścić na inny element, by stał się jego obiektem podrzędnym.

Gdy zaznaczonych jest wiele elementów, jeden z nich jest zaznaczeniem głównym i jest jaśniejszy. Przytrzymaj i przeciągnij dowolny z nich, aby przesunąć wszystkie zaznaczone obiekty naraz.

Gdy zaznaczasz element nadrzędny, domyślnie zaznaczane są też wszystkie jego obiekty podrzędne. Ponowne stuknięcie elementu nadrzędnego przełącza między zaznaczeniem samego elementu nadrzędnego a zaznaczeniem go razem z obiektami podrzędnymi.

Stuknij dwukrotnie element, aby skupić na nim kamerę (patrz [Zaawansowane](#focus-on-item)).

### Menu obiektu {#object-menu}

Stuknięcie przycisku z wielokropkiem (...) przy obiekcie w drzewie otwiera menu obiektu. 
Wiele z tych opcji powtarza dla wygody przyciski z paska skrótów na górze.

|       Akcja         |                       Ikona                        | Opis                                                                                                                                                                    |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Nazwa        |              ![](/icons/pencil.webp)           | Zmienia nazwę obiektu                                                                                                                                                   |
|  Anuluj instancję   |              ![](/icons/unlink.webp)           | Zamienia instancję w osobny kształt, więc zmiany modelowania nie są już kopiowane do innych instancji.                                                                  |
|  Utwórz instancję   |               ![](/icons/link.webp)            | Powiela obiekt jako instancję, więc zmiany modelowania jednej trafiają do wszystkich instancji.                                                                         |
|       Klonuj        |              ![](/icons/clone.webp)            | Powiela obiekt jako nowy obiekt                                                                                                                                         |
|        Usuń         |              ![](/icons/trash.webp)            | Usuwa obiekt. Jego obiekty podrzędne zostają, chyba że zaznaczono `Obiekty podrzędne`.                                                                                  |
|  Obiekty podrzędne  |            ![](/icons/hierarchy.webp)          | Gdy jest zaznaczone, `Utwórz instancję`, `Klonuj` i `Usuń` działają też na obiekty podrzędne.                                                                           |
| Podziel według Części |             ![](/icons/separate.webp)          | Jeśli obiekt składa się z niepołączonych części, tworzy osobny obiekt dla każdej z nich. Odwrotność łączenia.                                                         |
| Podziel według Grup |            ![](/icons/group.webp)          | Jeśli obiekt ma kilka grup powierzchni, tworzy osobny obiekt dla każdej grupy powierzchni.                                                                                 |
| Podziel według Warstw |              ![](/icons/layer.webp)            | Jeśli obiekt ma warstwy, tworzy osobne obiekty dla siatki bazowej i każdej warstwy. Przydaje się do przenoszenia blendshape'ów do innych aplikacji.                  |
|   Połącz → Warstwy  | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Jeśli zaznaczono kilka obiektów o zgodnej topologii, scala je w warstwy głównego obiektu (pozostałe obiekty zostaną usunięte). Również przydatne przy blendshape'ach przychodzących Z innych aplikacji.<br><br> Warstwy będą domyślnie wyłączone. Włącz je, jeśli chcesz regulować ich suwaki. |
| Krzywa (Powtarzacz) |              ![](/icons/curve.webp)            | Tylko dla rury lub bryły obrotowej: dodaje jako obiekt podrzędny repeater [Krzywa](#curve), który podąża za tą samą krzywą.                                             |
|        Rura         |             ![](/icons/tube.webp)              | Dla bryły obrotowej dodaje jako obiekt podrzędny [rurę](tools.md#tube), która podąża za jej profilem. Walec, stożek lub torus zamienia w rurę o tym samym kształcie, którą możesz wygiąć wzdłuż krzywej. |




### Zaznaczanie wielu obiektów {#multiselection}
Możesz zaznaczyć wiele obiektów, aby:
- przesuwać kilka obiektów naraz narzędziem Gizmo,
- scalać obiekty operacjami łączenia i boolean.

W drzewie stuknij ikonę zaznaczenia każdego obiektu albo przeciągnij po kolumnie zaznaczenia. Stukając w nazwy, przytrzymaj skrót `Maska` (lub `Ctrl` na klawiaturze), aby dodać lub usunąć pojedynczy obiekt, albo skrót `Gładkie` (lub `Shift`), aby zaznaczyć wszystkie obiekty między bieżącym a stukniętym.

::: tip Szybkie zaznaczanie wielu obiektów
W widoku też możesz zaznaczać wiele obiektów: przytrzymaj skrót `Gładkie` (lub `Shift`) i stuknij inną siatkę.

Obiekt odznaczysz, stukając go ponownie (tylko gdy zaznaczonych jest więcej obiektów niż jeden).
:::

Gizmo przesuwa wszystkie zaznaczone obiekty razem, patrz [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Połącz {#join}
Ta opcja po prostu tworzy jeden obiekt z kilku zaznaczonych obiektów.
Punkty i UV położone bliżej niż [promień zespawania](#weld-radius) zostają scalone.

Przykład na filmie znajdziesz w sekcji [Podziel](#separate).

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Łączy obiekty w jedną powierzchnię.

`Scalanie wokseli` zachowuje objętość obiektów i oblicza na powierzchni nowe, równomiernie rozłożone wielokąty. Dzięki temu etapowi obliczeń radzi sobie ze złożoną geometrią, ale może zgubić drobne detale, jeśli docelowa rozdzielczość jest za niska.

`Boolean` stara się zachować pierwotny układ wielokątów i zszywa je tam, gdzie obiekty się nakładają. Daje to znacznie czystsze i ostrzejsze wyniki niż scalanie wokseli, ale wymaga „szczelnych” siatek: obiekty nie mogą mieć otworów ani wadliwych kształtów. Jeśli to się nie uda, zwykle zadziała scalanie wokseli.

### Operacje boolean {#boolean-operations}
Zarówno scalanie wokseli, jak i Boolean sterują operacją przez widoczność obiektów, co przypominają podpowiedzi na dole okna:

#### Suma {#union}
Oba obiekty widoczne dają **sumę**: zewnętrzne powłoki obiektów zostają połączone, bez wewnętrznych powierzchni. ![](/images/boolean_union.webp)

#### Odejmowanie {#subtract}
Jeden obiekt ukryty = **odejmowanie**: ukryty obiekt zostaje odjęty od widocznego. ![](/images/boolean_subtract.webp)

#### Przecięcie {#intersect}
Oba obiekty ukryte = **przecięcie**: nowy kształt powstaje tylko tam, gdzie obiekty się nakładają. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Scalanie wokseli {#voxel-merge-button}
Ten przycisk wykonuje scalanie wokseli na zaznaczonych obiektach. Na pojedynczym obiekcie przebudowuje go z równomiernie rozłożonymi wielokątami, co przydaje się, gdy obiekt ma rozciągnięte wielokąty. Poniższe opcje działają jak w [remeshu wokselowym](topology.md#voxel-remesher).

### Rozdzielczość {#resolution}
Rozdzielczość siatki wokseli 3d użytej w obliczeniach. Podczas zmiany tej wartości na obiekcie pojawia się szachownica, która pokazuje rozmiar wielokątów.

Zakraplacz obok suwaka pobiera szczegółowość z gęstości siatki pod palcem. Przycisk obok przełącza suwak na `Długość krawędzi`, czyli rozmiar w świecie: ta sama wartość daje te same detale na każdym obiekcie.

### Utwórz wielokrotną rozdzielczość {#build-multiresolution}
Tworzy poziomy wielokrotnej rozdzielczości poniżej docelowej rozdzielczości. Jeśli rozdzielczość to 400, a ta opcja ma wartość 3, dostaniesz nową siatkę z około 296 000 wielokątów, ale pod nią będą 3 niższe poziomy podziału z około 74 000, 18 500 i 4 600 wielokątów.

### Pogrub cienkie części {#thicken-thin-parts}
Pogrubia części zbyt cienkie dla siatki wokseli, żeby się nie rozpadły. Nie jest dostępna razem z `Ostre krawędzie` ani `Ostra granica`.

### Otwory {#holes}
Sposób zamykania otworów w otwartych obiektach przed scaleniem:
* `Wypełnij` - każdy otwór jest zamykany osobno, od jego krawędzi.
* `Kształt` - otwory są zamykane zgodnie z otaczającą powierzchnią, a nakładające się otwarte fragmenty zostają połączone.

### ![](/icons/angle.webp) Zachowaj ostre krawędzie {#keep-sharp-edges}
Przycisk `Ostre krawędzie` przyciąga siatkę wokselową do ostrych krawędzi obiektów. Działa najlepiej na prostych kształtach i w niektórych miejscach może wprowadzić zniekształcenia.

### ![](/icons/group.webp) Ostra granica {#sharp-border}
Nowe ściany podążają za granicami grup powierzchni, a granica pozostaje ostra tam, gdzie powierzchnia się wzdłuż niej załamuje.

### ![](/icons/group_separate.webp) Zachowaj osobne grupy {#keep-groups-separate}
Każda grupa powierzchni jest przebudowywana osobno: grupy nigdy się nie łączą, a każda pozostaje zamkniętym kawałkiem we własnej grupie. W tym trybie wielokrotna rozdzielczość nie jest tworzona.

### ![](/icons/bool_subtract_circle.webp) Przycisk Boolean {#boolean-button}
Ten przycisk wykonuje operację boolean na wielokątach przy użyciu biblioteki Manifold autorstwa Emmetta Lalisha. 

### ![](/icons/bool_unite_circle.webp) Usuń nakładające się fragmenty {#clean-overlaps}
Gdy zaznaczony jest tylko jeden obiekt, przycisk `Boolean` zmienia się w `Usuń nakładające się fragmenty`: scala przecinające się części obiektu w czystą powierzchnię.


## ![](/icons/separate.webp) Podziel {#separate}
Jeśli masz jeden obiekt złożony z kilku niepołączonych części, możesz go podzielić na kilka obiektów. 
To przeciwieństwo [łączenia](#join).

Okno `Podziel...` oferuje trzy sposoby podziału zaznaczonych obiektów:
* `Podziel według Części` - tworzy osobny obiekt dla każdej niepołączonej części.
* `Podziel według Grup` - tworzy osobny obiekt dla każdej grupy powierzchni.
* `Podziel według Warstw` - tworzy osobne obiekty dla siatki bazowej i każdej warstwy.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Dodaj {#add-menu}

![](/images/scene_addmenu_overview.webp)

To menu tworzy prymitywy, grupy, kamery, repeatery i światła.

Prymitywy to podstawowe kształty, które dostosowujesz za pomocą parametrów. Gdy prymityw jest już taki, jak chcesz, „zatwierdzasz” go: parametry zostają zamienione na siatkę wielokątów, którą można rzeźbić i malować. Po zatwierdzeniu nie da się już zmieniać parametrów prymitywu.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Na manipulatorze {#on-gizmo}
Umieszcza nowy prymityw tam, gdzie jest aktualnie zaznaczony kształt lub gizmo. Gdy opcja jest wyłączona, prymityw pojawia się w środku sceny.

### ![](/icons/gizmo.webp) Wybierz manipulator {#select-gizmo}
Po utworzeniu nowego prymitywu automatycznie przełącza na narzędzie Gizmo. 

### ![](/icons/cog.webp) Zaawansowane {#add-advanced}

To menu pozwala wybrać, gdzie mają powstawać nowe prymitywy, grupy i repeatery: na zaznaczonym obiekcie, w początku układu współrzędnych świata lub w miejscu gizmo.


### UV {#uvs}
Przełącznik `UV` obok tytułu Prymityw włącza UV w prymitywach. UV (często nazywane współrzędnymi tekstury) to dodatkowe dane, dzięki którym w 3d można nakładać tekstury na powierzchnie. Zajmują więcej pamięci, ale na większości urządzeń nie powinno to być problemem, chyba że pracujesz z bardzo dużą liczbą wielokątów (np. 10 milionów lub więcej). 

### Prymitywy {#primitives}

| Prymityw       | Ikona                                     | Opis                                                                                                            |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Równoległościan | ![](/icons/cube.webp)                    | Prosty sześcian; możesz ustawić podział w osiach X, Y i Z                                                       |
| Kula Sześcienna | ![](/icons/circle.webp)                  | Podzielony sześcian z wymuszoną opcją `Kula` (rzutowanie na kulę), więc ma równy układ czworokątów, dobry do rzeźbienia |
| Walec          | ![](/icons/cylinder.webp)                | Walec może mieć otwór w środku, na przykład by zrobić pustą w środku rurkę                                      |
| Torus          | ![](/icons/torus.webp)                   | Torus to dobry punkt wyjścia na pierścienie                                                                     |
| Stożek         | ![](/icons/cone.webp)                    | -                                                                                                               |
| Dwudziestościan | ![](/icons/icosahedron.webp)            | -                                                                                                               |
| Kula UV        | ![](/icons/circle.webp)                  | Kula o nierównym układzie wielokątów, patrz [ostrzeżenie poniżej](#uv-sphere)                                   |
| Płaszczyzna    | ![](/icons/rectangle.webp)               | Prosta płaszczyzna; to jedyny prymityw, który nie jest zamknięty                                                |
| Tekst          | ![](/icons/text.webp)                    | Tekst 3d z czcionką, stylem, wyrównaniem, głębokością i wygięciem. `Scal litery` łączy stykające się litery     |
| Rura           | ![](/icons/tube.webp)                    | patrz [Rura](tools#tube)                                                                                        |
| Bryła obrotowa | ![](/icons/lathe.webp)                   | patrz [Bryła obrotowa](tools#lathe)                                                                             |
| Trzypłaszczyznowy | ![](/icons/triplanar.webp)            | patrz [Trzypłaszczyznowy](#triplanar)                                                                           |
| VDM            | ![](/icons/vdm.webp)                     | Płaszczyzna przygotowana do rzeźbienia stempla wektorowej mapy przemieszczeń: ma UV i jest zwrócona do kamery    |
| Łapacz cienia  | ![](/icons/material_shadow_catcher.webp) | patrz [Łapacz cienia](#shadow-catcher)                                                                          |
| Głowa          | ![](/icons/face.webp)                    | Prosta głowa z warstwą do płynnego przejścia między męską a żeńską                                              |

::: tip
Jeśli zastanawiasz się, czym jest siatka bazowa po uruchomieniu Nomada: to również podzielony sześcian.
Siatka bazowa w Nomadzie nie używa jednak rzutowania na kulę (`Kula`), więc nie jest idealnie okrągła.
:::

### Pasek narzędzi prymitywu {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Po utworzeniu prymitywu pojawia się pasek narzędzi do sterowania jego parametrami.

* `Zatwierdź` Zamienia prymityw w zwykły obiekt, który można rzeźbić i malować.
* `Odbicie lustrzane` Włącza lub wyłącza repeater lustrzany nad prymitywem.
* `Wszystkie` (ikona oka) Wybiera, które uchwyty do sterowania parametrami są widoczne bezpośrednio na prymitywie, np. szerokość sześcianu czy promień otworu walca: `Brak`, `Wszystkie` lub tylko jeden rodzaj (promień, otwór, profil...), zależnie od prymitywu.
* `Podział` Liczba podziałów prymitywu, tutaj w osi X dla sześcianu.
* `Stała gęstość` Gdy rozciągasz prymityw gizmo wzdłuż jednej osi, rośnie jego rozmiar i liczba podziałów, zamiast rozciągać się wielokąty, więc ściany pozostają kwadratowe. Dostępne dla sześcianów, płaszczyzn i walców.
* `...` Otwiera menu prymitywu.

Różne prymitywy mają na pasku dodatkowe opcje:

* `Kula` Kula jest zbudowana z podzielonego sześcianu, bo lepiej się go rzeźbi, ale przez to nie jest idealnie okrągła. Ta opcja przybliża kształt do idealnej kuli. Dwudziestościan też ma tę opcję.
* `Zakończenie` Włącza lub wyłącza zamknięcia końców kształtu, np. walec może mieć zamknięcie na górze, na dole, oba lub żadne.
* `Otwór` Tworzy otwór przez środek kształtu. Przełącza między brakiem otworu, otworem o jednym promieniu i otworem o różnych promieniach na górze i na dole.
* `Promień` Określa, czy walec ma jeden promień, czy różne promienie na górze i na dole.
* `Dysk` Określa, czy płaszczyzna ma kształt czworokąta, czy koła.

Mały pasek pod głównym paskiem przełącza między gizmo prymitywu a gizmo przekształceń.

::: tip

Stuknięcie tytułu paska przenosi go na górę lub na dół ekranu. Stuknięcie strzałki w rogu go zwija.

:::


### Menu prymitywu {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Zawiera wszystkie parametry zaznaczonego prymitywu. Parametry to podstawowy opis kształtu. Aby opisać pierścień, podałbyś na przykład jego promień zewnętrzny, promień wewnętrzny i liczbę wielokątów.

Większość parametrów prymitywów nie wymaga wyjaśnień, a kilka jest wspólnych dla wszystkich prymitywów:

* `UV` Mały przycisk UV na górze menu włącza tworzenie współrzędnych UV
* `Zatwierdź` Mały przycisk zatwierdzania zamienia prymityw w zwykły obiekt, który można rzeźbić i malować.
* `Maks. liczba powierzchni` Górny limit liczby wielokątów obiektu, który chroni urządzenie przed awarią.
* `Podział następczy` Stosuje wybraną liczbę podziałów z sekcji wielokrotnej rozdzielczości menu Topologia. W połączeniu z niewielką liczbą podziałów topologii pozwala tworzyć wygładzone prymitywy o miękkich narożnikach. Na przykład sześcian z podziałem topologii 2 i podziałem następczym 4 będzie miał gładkie narożniki.
* `Podział liniowy` Ile poziomów podziału liniowego zastosować przed zwykłym gładkim podziałem. Pozwala kontrolować, jak ostre lub miękkie są narożniki podzielonych powierzchni. Na przykład ustaw podział topologii sześcianu na 2, podział następczy na 4 i zmieniaj podział liniowy od 0 do 4. Narożniki sześcianu przejdą od miękkich do ostrych.

### Topologia {#topology}

Określa liczbę wielokątów prymitywu. Zwykle suwaki są powiązane, więc zmiana jednego aktywnego suwaka równomiernie zmienia wszystkie wielokąty. Możesz stuknąć przycisk rozłączenia i sterować podziałami X/Y/Z osobno.

### Geometria {#geometry}

Określa ogólny rozmiar prymitywu: w jednostkach X/Y/Z dla kształtów kanciastych i jako promień dla kształtów okrągłych.


### ![](/icons/circle.webp) Kula UV {#uv-sphere}
::: warning
Kula UV nie nadaje się dobrze do rzeźbienia, zwłaszcza na biegunach.

Lepiej wybierz [prymityw](#primitives) Kula Sześcienna, Równoległościan lub Dwudziestościan z opcją `Kula` (rzutowanie na kulę).

Topologia może być do przyjęcia przy rzeźbieniu, jeśli ustawisz bardzo niską wartość suwaków `Podział`.
Liczbę wielokątów zwiększysz potem suwakiem `Podział ogólny`.

Choć Kula UV nie nadaje się do zwykłego rzeźbienia, przydaje się na oczy: jeśli obrócisz ją tak, by biegun wypadał na źrenicy, układ wielokątów naturalnie pasuje do malowania i rzeźbienia tęczówki i źrenicy.
:::


### ![](/icons/triplanar.webp) Trzypłaszczyznowy {#triplanar}
Ten prymityw jest wyjątkowy: jego geometrię kształtujesz [narzędziem Maska](tools.md#mask).

![](/videos/triplanar.mp4)


::: tip
Stuknij dwukrotnie płaszczyznę, a kamera skupi się na niej.
Nie zadziała to jednak, jeśli obrócisz prymityw gizmo.
:::

Prymityw trzypłaszczyznowy wypełnia siatkę wokseli na podstawie maski z 3 płaszczyzn, a następnie zamienia ją na wielokąty (dzięki [remeshowi wokselowemu](topology.md#voxel-remesher)).

Każda płaszczyzna ma własną płaszczyznę symetrii.

::: warning
Każda zmiana rozmiaru prymitywu trzypłaszczyznowego pogarsza jakość namalowanej maski.

Na razie nie ma opcji „zablokowania” malowania na jednej płaszczyźnie, ale może pojawi się w przyszłości.
Trochę pomaga [Połączona topologia](stroke.md#connected-topology): jeśli kursor leży dokładnie na jednej płaszczyźnie, nie wpłynie na pozostałe.
:::

### ![](/icons/material_shadow_catcher.webp) Łapacz cienia {#shadow-catcher}
Dodaje płaszczyznę z materiałem łapacza cienia. Więcej szczegółów w opisie [materiału Łapacz cienia](material.md#shadow-catcher). 


## Grupa/Kamera {#groupcamera}
### ![](/icons/share.webp) Grupa {#group}
Tworzy „pusty” obiekt, pod którym możesz umieszczać inne obiekty. Pozwala po prostu uporządkować hierarchię: umieść wiele obiektów pod grupą, a potem ją zwiń. Grupa może też pomagać w przesuwaniu obiektów: umieść pod nią wiele obiektów, a potem przesuwaj, obracaj i skaluj grupę narzędziem Gizmo.

### ![](/icons/camera.webp) Kamera {#add-view}
Tworzy kamerę.

## Repeatery {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeatery to węzły, które tworzą instancje umieszczonych pod nimi obiektów. 

### ![](/icons/array.webp) Macierz {#array}
![](/images/scene_primitive_array.webp)

Obiekty podrzędne tego węzła mogą być powielane jako instancje w układzie siatki. Gdy węzeł jest zaznaczony, ma te ustawienia:
* `Dopasuj do wewnątrz` - gdy jest włączone, wszystkie kopie mieszczą się w granicach macierzy; gdy jest wyłączone, suwaki ustalają odstęp między kopiami
* `Liczba X/Y/Z` - liczba instancji w każdej osi
* `Rozmiar X/Y/Z` - rozmiar siatki w każdej osi albo odległość między kopiami, gdy `Dopasuj do wewnątrz` jest wyłączone
* `Zrandomizuj...` - dodaje losowe różnice między kopiami, patrz [Zrandomizuj](#curve) poniżej.

### ![](/icons/curve.webp) Krzywa {#curve}
![](/images/scene_primitive_curve.webp)
Tworzy krzywą, wzdłuż której powtarzane są obiekty podrzędne tego węzła. Gdy węzeł jest zaznaczony, ma te ustawienia:
* `Krzywa` - edycja krzywej: dodawanie i przesuwanie jej punktów.
* `Pokaż` - pokazuje lub ukrywa krzywą i jej punkty.
* `Przyciągnij` - przyciąga punkty krzywej do innej geometrii.
* `Sym` - edytuje krzywą symetrycznie.
* `Zamknięty` - łączy początek z końcem albo pozostawia krzywą otwartą.
* `B-splajn` - instancje podążają dokładnie za krzywą albo używają interpolacji B-splajn, która daje gładsze wyniki.
* `Dopasuj kształt` - wygina każdą kopię wzdłuż krzywej, tak by stykała się z sąsiednimi (`Płynne` wygina ich boki, by stykały się bez kąta).
* `Wyrównaj` - obraca kopie zgodnie z kierunkiem krzywej.
* `Pkt obrotu` - punkt obrotu kopii: sama krzywa (`Sama krzywa`) lub jej obiekty podrzędne.
* `Liczba` - liczba instancji. Przycisk trybu obok przełącza na `Odległość`: stały odstęp między kopiami, a ich liczba zależy od długości krzywej.
* `Promień` - uchwyty na każdym punkcie krzywej ustalające skalę instancji.
* `Skręt` - uchwyty na każdym punkcie krzywej ustalające skręcenie instancji.
* `Naprzemiennie` - obraca co drugą kopię wokół krzywej: o 90° dla ogniw łańcucha, o 180° dla liści czy ząbków zamka, wokół wybranej `Oś`.
* `Spirala...` - nawija kopie wokół krzywej w kilku splotach (lina, warkocz, wstążka...).
* `Zrandomizuj...` - dodaje losowe różnice między kopiami; każdy wiersz może zamiast tego dodawać tę samą wartość przy każdej kopii.

Pod paskiem narzędzi przełącznik `(Scal)` scala punkt z innym, gdy go na niego przeciągniesz. `IK` (kinematyka odwrotna) pozwala pozować krzywą: przeciągasz punkt, a połączone punkty podążają za nim. Stuknij punkt, aby go zablokować lub odblokować, przytrzymaj, aby zablokować lub odblokować wszystkie; zablokowane punkty pozostają na miejscu.

### ![](/icons/radial.webp) Radialna {#radial}
![](/images/scene_primitive_radial.webp)

Obiekty podrzędne tego węzła są powielane jako instancje po okręgu. Przesuń obiekt podrzędny, aby zmienić promień tego repeatera. Gdy węzeł jest zaznaczony, ma te ustawienia:
* RadialX/Y/Z - te przyciski ustawiają oś powielania i liczbę instancji.



### ![](/icons/mirror.webp) Odbicie lustrzane {#mirror}
![](/images/scene_primitive_mirror.webp)

Obiekty podrzędne tego węzła są odbijane względem osi. Gdy węzeł jest zaznaczony, ma te ustawienia:
* Gizmo - włącza gizmo przekształceń, by ustawić środek odbicia. Można je też obracać i skalować. Gdy skończysz, stuknij ponownie Gizmo, aby wrócić do zwykłych ustawień.
* X/Y/Z - ustawia płaszczyznę odbicia

### ![](/icons/surface.webp) Powierzchnia {#surface}

Obiekty podrzędne tego węzła są kopiowane na powierzchnię obiektu: jedna kopia na ścianę, krawędź lub wierzchołek albo losowo rozsiane. Gdy węzeł jest zaznaczony, ma te ustawienia:
* Tryb - umieszcza kopie na ścianach (`Ściany`), krawędziach (`Krawędzie`) lub wierzchołkach albo je rozsiewa (`Rozsiej`).
* Co - jedna kopia co N ścian, krawędzi lub wierzchołków. `Losowo` wybiera je losowo, a `Przetasuj` losuje inny zestaw.
* Odstępy - przy rozsiewaniu minimalna odległość między dwiema kopiami.
* Wyrównaj - kopie stoją na powierzchni zgodnie z jej normalną, zamiast zachować orientację oryginału.
* Przyciągnij - rzutuje oryginał na najbliższy punkt powierzchni, a kopie podążają za nim.
* Dopasuj rozmiar, Ścinanie - skalują i rozciągają kopie do kształtu każdej ściany.
* Dopasuj kształt - wygina każdą kopię na jej ścianie lub wzdłuż jej krawędzi, by sąsiednie kopie stykały się bez przerw.

Wszystkie repeatery mają opcję `Zatwierdź`, która utrwala wynik działania repeatera i pyta, jak to zrobić:
* Połącz obiekty podrzędne - instancje zostają połączone w jeden obiekt
* Zachowaj instancje - instancje pozostają instancjami, ale bez nadrzędnego repeatera
* Anuluj instancję - instancje zostają zamienione w osobne obiekty

`Spłaszcz wszystko` utrwala także repeatery zagnieżdżone w tym repeaterze, więc każda kopia staje się zwykłym obiektem.

::: tip Wskazówka: łączenie repeaterów
Repeatery można zagnieżdżać jeden w drugim, a kilka obiektów może być obiektami podrzędnymi repeaterów, co pozwala uzyskać złożone efekty.

![](/images/scene_repeater_combine.webp)
:::

::: tip Wskazówka: punkty obrotu repeaterów

Niektóre repeatery automatycznie ustawiają punkt obrotu obiektów podrzędnych, więc nawet jeśli przesuniesz lub obrócisz je narzędziem Gizmo, nie zmienią położenia. Aby to obejść, wstaw grupę między repeater a obiekt podrzędny. Wtedy możesz przesuwać obiekt podrzędny niezależnie od repeatera.
:::

## Światło {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Kierunkowe {#directional}
Tworzy światło kierunkowe, czyli nieskończenie odległe źródło światła, jak słońce.

### ![](/icons/panorama.webp) Środowisko {#environment}
Tworzy światło środowiskowe, które oświetla scenę obrazem otaczającym ją ze wszystkich stron (oświetlenie oparte na obrazie, jak HDRI).

### ![](/icons/spotlight.webp) Stożkowe {#spot}
Tworzy światło stożkowe z ustawieniami szerokości i miękkości stożka.

### ![](/icons/light.webp) Wielokierunkowe {#point}
Tworzy światło punktowe, świecące we wszystkich kierunkach.

## ![](/icons/cog.webp) Zaawansowane {#advanced}
Przycisk `Zaawansowane` w lewym dolnym rogu panelu otwiera okno z dwiema kartami: `Ogólne` i `Synchronizacja`.

### ![](/icons/focus.webp) UI: Skup przy 2× stuknięciu {#focus-on-item}
Dwukrotne stuknięcie elementu na liście Scena ustawia kamerę w widoku 3d na tym elemencie.

### ![](/icons/eye_open.webp) Synchronizuj widoczność {#sync-visibility}
Gdy jest włączone, użycie ikony oka przy zaznaczonym elemencie wpływa na wszystkie zaznaczone elementy. 

### ![](/icons/bang.webp) Wyróżnianie {#highlight}
Podświetla zaznaczone obiekty w widoku, gdy zmienia się zaznaczenie.

### ![](/icons/link.webp) Pokaż (Instancja) {#instance-show}
Wyświetla kolorowy znacznik po lewej stronie listy sceny, który oznacza instancje.

### ![](/icons/preview.webp) Podglądy obiektów {#object-previews}
Pokazuje wyrenderowaną miniaturę każdego obiektu na liście sceny. Działa tak samo jak przycisk podglądu nad listą.

### Promień zespawania {#weld-radius}
Pod tytułem `Połącz` znajdziesz `Promień zespawania pozycji` i `Promień zespawania UV`: punkty i UV bliższe niż te promienie zostają scalone. Każdy z nich można wyłączyć polem wyboru. Dotyczy to łączenia, operacji Boolean, przycinania, upraszczania, przebudowy siatki i importu plików.

### Ikony {#icons}
Ustawia minimalny i maksymalny `Rozmiar` oraz `Krycie` ikon grup, świateł, kamer i repeaterów w widoku.

### ![](/icons/hierarchy.webp) Linie hierarchii {#hierarchy-lines}
Wyświetla w widoku linię między obiektem nadrzędnym a jego obiektami podrzędnymi. Gdy opcja jest włączona, możesz też ustawić:
* `Użyj pivot Nomad` - linie zaczynają się w punkcie obrotu używanym przez narzędzia Przekształcenie i Gizmo. Gdy opcja jest wyłączona, używają naturalnego punktu obrotu bazy, który może być daleko od środka obiektu.
* `Grubość` - szerokość linii. Przycisk obok suwaka dodaje do nich obrys.
* Kolor linii.

### ![](/icons/link.webp) Synchronizacja {#sync}
Karta `Synchronizacja` określa dla każdej operacji (`Dodaj`, `Usuń`, `Zablokuj`, `Klonuj`, `Utwórz instancję`, `Anuluj instancję`, `Połącz`, `Podziel` i `Boolean`), czy działa na wszystkie instancje zaznaczenia:
* `Auto` - zgodnie z polem wyboru `Synchronizacja` na górze menu Scena.
* `Nie` - tylko zaznaczone obiekty.
* `Tak` - zawsze wszystkie instancje.

Domyślnie `Połącz`, `Podziel` i `Boolean` mają wartość `Tak`, a pozostałe `Auto`. `Wyzeruj` przywraca te ustawienia domyślne.

## Dolny pasek narzędzi {#bottom-toolbar}
Te ikony pokazują lub ukrywają w widoku grupy, światła, kamery, repeatery i linie hierarchii. Ikony widoczne w widoku można stuknąć, by je zaznaczyć i bezpośrednio edytować.
