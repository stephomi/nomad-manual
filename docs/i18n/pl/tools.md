# ![](/icons/toolbox.webp) Narzędzia {#tools}

![](/images/tools_menu.webp)

::: tip
Opisy poszczególnych narzędzi znajdziesz niżej, w sekcji [Narzędzia](#tools-1).
:::

## Przegląd {#overview}

Narzędzia wybierasz w panelu `Przybornik` po prawej stronie, a sterujesz nimi w panelu `Sterowanie narzędziem` po lewej. Dodatkowe ustawienia znajdziesz w menu `Narzędzie`, w menu w prawym górnym rogu.

Narzędzia pędzlowe mają suwaki rozmiaru i intensywności. Narzędzia zaznaczania mają przyciski kilku stylów zaznaczania. Na dole panelu sterowania narzędziem są skróty do często używanych operacji (Gładkie, Maska, Ukryj, Grupa powierzchni, Gizmo, Kolor, Alfa).

Narzędzia Nomada są w przyborniku oznaczone kolorami (wyłącz `Kolorowe narzędzia` w menu [Interfejs](interface.md), jeśli wolisz zwykłe etykiety):

* <span class=brush>**Narzędzia pędzlowe**</span> (Glina, Pędzel, Gładkie, Warstwa, Napełnij, Us. warstwę, Quad Remesher)
* <span class=move>**Narzędzia przesuwania**</span> (Przenieś, Przeciągnij, Elastyczne, Przesuń)
* <span class=mask>**Narzędzie maski**</span> (Maska)
* <span class=paint>**Narzędzia malarskie**</span> (Farba, Smużenie)
* <span class=flatten>**Narzędzia spłaszczające**</span> (Spłaszcz, Płaski, Poleruj)
* <span class=pinch>**Narzędzia ściskające**</span> (Bruzda, Ściśnięcie)
* <span class=stamp>**Narzędzia stemplujące**</span> (Stempel, VDM)
* <span class=selection>**Narzędzia oparte na zaznaczeniu**</span>, w których najpierw rysujesz maskę 2d, a potem wykonywana jest operacja (Przytnij, Podziel, Rzutuj)
* <span class=creation>**Narzędzia tworzenia**</span> (Rura, Bryła obrotowa, Wstaw)
* <span class=transform>**Narzędzia przekształcania**</span> (Przekształcenie, Gizmo, Rozmieść, Krata)
* <span class=misc>**Narzędzia różne**</span> (Grupa powierzchni, Ukryj)
* <span class=view>**Narzędzia widoku**</span> (Wyświetl, Zmierz, Wybierz)



Wiele z tych narzędzi możesz dostosować: zachowanie pędzla, nacisk, tekstury itd. ustawisz w menu [Pociągnięcie](stroke.md).


### Sterowanie pędzlem {#brush-controls}

Lewy pasek narzędzi ma suwaki promienia i intensywności, a pod nimi przyciski zależne od rodzaju narzędzia, opisane poniżej.

![](/images/tool_left_panel.webp)

::: tip
W wielu narzędziach suwak intensywności można przesunąć powyżej 100%. Warto poeksperymentować!
:::

### Tryb alternatywny {#sub-mode}
Przycisk tuż pod suwakiem intensywności to przycisk `Odejmij`. Jego etykieta i działanie zmieniają się w zależności od narzędzia, a po wciśnięciu włącza on alternatywne, zwykle odwrotne zachowanie. Na przykład w narzędziu [Farba](#paint) włącza tryb wymazywania, a w narzędziu [Bruzda](#crease) tworzy wypukłe krawędzie zamiast bruzd.

Domyślnie działa jak przycisk chwilowy: możesz go przytrzymać, aby włączyć go na chwilę, a gdy go puścisz, wyłączy się. Jeśli go stukniesz, tryb alternatywny pozostanie włączony na stałe.

### Skróty {#shortcuts}
Na dole lewego paska narzędzi znajdują się skróty do narzędzi [Gładkie](#smooth), [Maska](#mask), [Ukryj](#hide), [Grupa powierzchni](#facegroup), [Gizmo](#gizmo), [Kolor](painting.md#pbr-sliders) i [Alfa](stroke.md#alpha).

Domyślnie wszystkie działają jak przyciski chwilowe: możesz przytrzymać skrót, aby włączyć go na chwilę, a gdy go puścisz, wyłączy się. Jeśli go stukniesz, tryb tego skrótu pozostanie włączony na stałe.

### Sterowanie zaznaczeniem {#selection-controls}

Narzędzia [Maska](#mask), [Farba](#paint), [Przytnij](#trim), [Podziel](#split), [Rzutuj](#project), [Grupa powierzchni](#facegroup), [Ukryj](#hide) i [Wybierz](#select) zaznaczają obszary siatki za pomocą podobnych przycisków.

![](/images/tools_shape_selector_panel.webp)

Stuknij przycisk kształtu na lewym pasku narzędzi (pokazuje bieżący kształt, domyślnie `Lasso`), aby otworzyć okienko z kształtami. W narzędziach, które działają też pędzlem (Maska, Farba, Grupa powierzchni, Ukryj), to samo okienko zawiera również typy pociągnięć.

* `Widok` - Brak kształtu, narzędzie nie robi nic szczególnego, tak jak tryb kamery.
* `Lasso` - Kształt rysowany odręcznie.
* `Wielokąt` - Zamknięty kształt złożony z krzywych i/lub odcinków prostych. Więcej informacji znajdziesz niżej, w sekcji [Edycja kształtu](#shape-editing).
* `Krzywa` - (tylko Rzutuj) Odręczna krzywa do rzutowania.
* `Ścieżka` - (tylko Rzutuj) Krzywa wyznaczona przez punkty. Więcej informacji znajdziesz niżej, w sekcji [Edycja kształtu](#shape-editing).
* `Linia` - Przeciągnij linię, aby wyznaczyć płaski przekrój. Domyślnie operacja wykona się na siatce od razu. Jeśli tego nie chcesz, zmień opcję `Edytuj` (przytrzymaj ikonę linii lub przesuń po niej palcem).
* `Pas` - Pasek między dwiema równoległymi prowadnicami, z gradientem w poprzek. `Rozszerz` zachowuje pełną wartość także za dalszą prowadnicą, zamiast kończyć się na pasie, a `Odwróć` zamienia prowadnicę, od której zaczyna się gradient.
* `Prostokąt` - Przeciągnij linię po przekątnej, aby wyznaczyć narożniki prostokąta. Przytrzymaj lub przesuń palcem, aby pokazać opcję `Edytuj`, `Kwadrat`, aby wymusić kwadrat, oraz `Wyśrodkowany`, aby pierwsze kliknięcie wyznaczało środek prostokąta.
* `Elipsa` - Przeciągnij linię po przekątnej, aby wyznaczyć rozmiar elipsy. Przytrzymaj lub przesuń palcem, aby pokazać opcję `Edytuj`, `Okrąg`, aby wymusić okrąg, oraz `Wyśrodkowana`, aby pierwsze kliknięcie wyznaczało środek elipsy.
* `Odwróć` - Odwraca maskę kształtu albo kierunek narzędzia Rzutuj.

Większość narzędzi ma opcję `Edytuj`, która decyduje, co się dzieje po narysowaniu kształtu:
* `Edycja: wyłączona` - Operacja wykonuje się, gdy tylko puścisz.
* `Edycja: włączona` - Kształt pozostaje edytowalny. Obok niego pojawia się zielony przycisk, który wykonuje operację. Możesz więc poprawić kształt i ustawić widok, a gdy wszystko będzie gotowe, nacisnąć zielony przycisk.
* `Edycja: przytrzymaj` - Operacja wykonuje się po puszczeniu, chyba że przytrzymasz palec na końcu pociągnięcia, aby dalej edytować kształt.

### Edycja kształtu {#shape-editing}
Edycja wielokąta i edycja krzywej działają podobnie:

* Na początek przeciągnij linię, aby wyznaczyć 2 punkty, a potem wyciągnij środek linii, aby utworzyć wielokąt lub krzywą.
* Klikaj punkty, aby przełączać je między gładkimi a ostrymi.
* Kliknij i przeciągnij odcinek krzywej lub linii, aby dodać nowe punkty.
* Aby usunąć punkt, przeciągnij go na sąsiedni, aż zrobi się czerwony.
* Ikona kosza w rogu ikony wielokąta lub ścieżki usuwa kształt.

### Menu ustawień {#settings-menu}

Wiele narzędzi ma dodatkowe ustawienia, które znajdziesz w menu `Narzędzie`, w menu w prawym górnym rogu. Dla narzędzi bez dodatkowych ustawień to menu jest wyszarzone.

![](/images/tools_settings_menu.webp)

## Narzędzia {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Glina](#clay)       | ![](/icons/tool_brush.webp)   <br> [Pędzel](#brush)     | ![](/icons/tool_move.webp)       <br> [Przenieś](#move)              | ![](/icons/tool_drag.webp)      <br> [Przeciągnij](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Elastyczne](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Gładkie](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Maska](#mask)       | ![](/icons/tool_paint.webp)   <br> [Farba](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Smużenie](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Spłaszcz](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Płaski](#planar)       | ![](/icons/tool_polish.webp)  <br> [Poleruj](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Bruzda](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Ściśnięcie](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Przytnij](#trim)              | ![](/icons/tool_split.webp)     <br> [Podziel](#split)         | ![](/icons/tool_project.webp)   <br> [Rzutuj](#project)     | ![](/icons/tool_layer.webp)   <br> [Warstwa](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Napełnij](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Przesuń](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Stempel](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [Us. warstwę](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Rura](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Bryła obrotowa](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Wstaw](#insert)   | ![](/icons/tool_transform.webp)  <br> [Przekształcenie](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Grupa powierzchni](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Ukryj](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Zmierz](#measure) | [Rozmieść](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Wybierz](#select)       | ![](/icons/tool_lattice.webp)   <br> [Krata](#lattice)     | ![](/icons/tool_view.webp)    <br> [Wyświetl](#view)       |

------

### ![](/icons/tool_clay.webp) Glina {#clay}
Narzędzie Glina przydaje się do budowania bryły rzeźby. `Odejmij` usuwa materiał z rzeźby.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pędzel {#brush}
Standardowy pędzel. `Odejmij` usuwa materiał.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Przenieś {#move}
Obszar pod pędzlem przykleja się do pędzla, co pozwala na elastyczne odkształcanie. Zaznaczenie jest zachowywane przez cały ruch, więc jeśli odsuniesz pędzel, a potem wrócisz nim do punktu startu, nie zobaczysz żadnego odkształcenia.

Tryb alternatywny to `Normalna`: przesuwa obszar pod pędzlem wzdłuż normalnej powierzchni.

Ten pędzel sprawdza się zarówno przy dużych odkształceniach, jak i przy drobnych, precyzyjnych poprawkach.

#### Ustawienia narzędzia Przenieś {#move-settings}

* `Promień (Tło)` - Jak daleko od krawędzi modelu możesz zacząć i nadal rzeźbić. Przydaje się przy pracy nad sylwetką obiektu. Odznacz, aby chwytać tylko wtedy, gdy zaczynasz na modelu.
* `Tylko ta sama strona` - Pomija wierzchołki skierowane przeciwnie do kierunku odkształcenia.
* `Kierunek` - Używany przez tryb alternatywny `Normalna`. Decyduje, czy przeciągnięcie wypycha, czy wciąga powierzchnię:
    * `Auto` - Wybiera za ciebie jedną z dwóch metod poniżej, na podstawie kąta normalnej powierzchni.
    * `Normalna 3D` - Porównuje położenie wskaźnika na ekranie z normalną powierzchni widzianą z kamery.
    * `XY` - O wypchnięciu lub wciągnięciu decyduje położenie wskaźnika na ekranie (góra/dół, lewo/prawo).
    * `Próg` - Przy opcji `Auto` graniczny kąt, który decyduje o wyborze metody.
* `Szybkość obrotu` - Chwycony obszar możesz skręcać podczas przesuwania: obracając dwoma palcami, obracając rysik wokół jego osi albo przytrzymując klawisz modyfikujący (Alt, Ctrl, Shift lub Cmd) podczas przeciągania myszą. Dla palca, rysika i myszy jest osobny suwak. Odznacz któryś, aby wyłączyć dane wejście.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Przeciągnij {#drag}
Obszar pod pędzlem przykleja się do pędzla, co pozwala na elastyczne odkształcanie. W odróżnieniu od narzędzia Przenieś zaznaczenie jest stale aktualizowane w trakcie pociągnięcia, więc możesz wyciągać dłuższe, wężowate kształty, zwłaszcza przy włączonej topologii dynamicznej.

Tryb alternatywny to `Normalna`: przesuwa obszar pod pędzlem wzdłuż normalnej powierzchni.

Ten pędzel nadaje się do swobodniejszych, bardziej szkicowych zmian kształtu.

#### Ustawienia narzędzia Przeciągnij {#drag-settings}

Przeciągnij ma te same ustawienia co [Przenieś](#move-settings): `Promień (Tło)`, `Tylko ta sama strona`, `Kierunek` i `Szybkość obrotu`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastyczne {#elastic}
Chwyta i ciągnie powierzchnię jak [Przenieś](#move), ale odkształca ją elastycznie: zamiast urywać się na krawędzi pędzla, pociągnięcie łagodnie słabnie z odległością na całym obiekcie, trochę jak rozciąganie gumy. Promień pędzla ustala, jak szeroko sięga to pociągnięcie.

Tryb alternatywny to `Normalna`: przesuwa obszar pod pędzlem wzdłuż normalnej powierzchni.

Ten pędzel świetnie nadaje się do dużych, miękkich zmian proporcji, po których powierzchnia zostaje gładka.

#### Ustawienia narzędzia Elastyczne {#elastic-settings}

Elastyczne ma te same ustawienia co [Przenieś](#move-settings), oprócz `Tylko ta sama strona`. `Promień (Tło)` jest domyślnie wyłączony.

### ![](/icons/tool_smooth.webp) Gładkie {#smooth}
Wygładza obszar, uśredniając położenie punktów. Działanie tego narzędzia mocno zależy od gęstości wielokątów.
Im więcej wielokątów, tym słabsze wygładzanie.

Tryb alternatywny to `Złagodź`: wygładza tylko siatkę krawędzi, starając się zachować detale geometrii.

#### Ustawienia narzędzia Gładkie {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Grupa powierzchni {#smooth-facegroup}

* `Złagodź` - Wygładza granice grup powierzchni. Ustaw intensywność powyżej 100%, aby szybko wygładzić granice. `Auto` wygładza tylko wtedy, gdy podgląd grup powierzchni jest włączony, `Nie` wyłącza tę funkcję, a `Tak` ją włącza.

##### Wierzchołek {#vertex}
* `Zachowaj objętość` - Wygładza bez kurczenia powierzchni, więc wielokrotne wygładzanie nie spłaszcza twoich kształtów. Przycisk z kołem zębatym obok skrywa używane do tego wartości `Pomniejsz` i `Napełnij`.
* `Zachowaj granicę` - W siatkach z otwartymi krawędziami, np. w płaszczyźnie, wygładzanie może zaokrąglić narożniki. Ta opcja utrzymuje wierzchołki na brzegu siatki w miejscu.
* `Stabilne wygładzanie` - Stara się, by wygładzanie nie zależało od topologii. Działa najlepiej przy zróżnicowanej gęstości siatki i wysokiej intensywności wygładzania.
* `Złagodź` - To samo co tryb alternatywny Złagodź na lewym pasku narzędzi.

##### Malowanie {#painting}
* `Wygładzanie ekranu` - Użyj tej opcji, aby wygładzanie nie zależało od topologii, nawet przy dużej liczbie wielokątów. `Auto`, `Nie` lub `Tak`.
* `Próbki ekranu` - Jakość wygładzania: wyższe wartości dają gładszy wynik, ale działają wolniej.

::: tip
Przy gęstszej siatce może być potrzebna intensywność powyżej 100%. Bardzo wysokie wartości (300%, 500%) sprawdzają się też jako narzędzie rzeźbiarskie: szybko spłaszczają i wygładzają obszar pod pędzlem, jak uderzenie pobijakiem w glinę!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maska {#mask}
To narzędzie pozwala maskować wierzchołki. Zamaskowane wierzchołki są chronione przed rzeźbieniem i malowaniem.

Tryb alternatywny to `Usuń maskę`: wymazuje maskę tam, gdzie została namalowana.

Podobnie jak zaznaczenia w programach do malowania 2d, maski możesz malować pędzlem albo tworzyć kształtami zaznaczenia (`Lasso`, `Prostokąt`, `Pas`...), a także je rozmywać i wyostrzać. Pędzel lub kształt wybierasz w okienku pociągnięć na lewym pasku narzędzi, zobacz [Sterowanie zaznaczeniem](#selection-controls).

W odróżnieniu od programów do malowania 2d maski możesz też tworzyć z grup powierzchni, a za ich pomocą tworzyć nową geometrię, np. przez wytłaczanie lub wyodrębnianie.

![](/videos/tool_mask1.mp4)

 U góry widoku pojawia się pasek z dodatkowymi przyciskami.

![](/images/tool_mask_toolbar.webp)

Stuknij tytuł paska, aby go rozwinąć lub zwinąć, albo stuknij strzałkę w prawym górnym rogu, aby przenieść go na górę lub na dół interfejsu.

| Działanie                                          | Opis                                                                                       |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Wyczyść wszystko   | Czyści maskę na wszystkich obiektach. Gdy zamaskowane są też inne obiekty, dodatkowy przycisk `Wyczyść` czyści tylko zaznaczone obiekty |
| ![](/icons/invert.webp)        Odwróć             | Odwraca maskę                                                                              |
| ![](/icons/sharpen.webp)       Wyostrzenie        | Wyostrza krawędź maski                                                                     |
| ![](/icons/blur.webp)          Rozmycie           | Rozmywa krawędź maski                                                                      |
| ![](/icons/outline.webp)       Obramowanie        | Maskuje otwarty brzeg siatki, np. krawędź płaszczyzny lub obrzeże otworu                   |
| ![](/icons/blur.webp)          Rozmycie ->        | Przeciągnij w prawo, aby rozmyć maskę, w lewo, aby ją wyostrzyć                           |
| ![](/icons/circle_plus.webp)   Powiększ ->        | Przeciągnij w prawo, aby powiększyć zamaskowany obszar, w lewo, aby go zmniejszyć          |
| ![](/icons/intensity.webp)     Wzmocnij ->        | Przeciągnij w prawo, aby wzmocnić maskę, w lewo, aby ją osłabić, bez zmiany jej kształtu   |
| ![](/icons/dig.webp)           Wgłębienie ->      | Odtwarza maskę na podstawie krzywizny powierzchni: przeciągnij w prawo, aby do malowania zostały tylko wgłębienia, w lewo, aby zostały tylko wypukłości |
| ![](/icons/culling.webp)       Przód              | Przełącza maskowanie tylko wierzchołków zwróconych do przodu                               |
| ![](/icons/eye_open.webp)      Widoczne           | Przy kształtach przełącza pomijanie wierzchołków zasłoniętych przez inne powierzchnie      |
|                                 Konwertuj          | Zamienia maskę w grupę powierzchni                                                         |
| ![](/icons/group_to_mask.webp) Po stuknięciu (grupa powierzchni) | Gdy włączone, pokazywane są grupy powierzchni, a stuknięcie grupy powierzchni ją maskuje |
|                                 Po stuknięciu (maska) | Gdy włączone, stuknięcie „wyspy” zamaskowanych lub niezamaskowanych wielokątów wypełnia całą tę wyspę |
| ![](/icons/connect.webp)       Połączona          | Gdy włączone, pociągnięcia maski działają tylko na połączoną topologię                     |

##### Szybkie gesty maski {#mask-quick-gesture}
Przytrzymując przycisk szybkiego maskowania na lewym pasku narzędzi, możesz wykonywać gesty w stylu ZBrusha:
| Działanie   | Gest (przytrzymaj skrót w lewym dolnym rogu) |
| :---------: | :------------------------------------------: |
| Odwróć      | Stuknij tło                                  |
| Wyczyść     | Przeciągnij po tle                           |
| Rozmycie    | Stuknij zamaskowany obszar                   |
| Wyostrzenie | Stuknij niezamaskowany obszar                |


#### Ustawienia maski {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Ustawienia maski służą głównie do tworzenia geometrii z maski. Karty u góry wybierają operację: [Wyodrębnij](#extract), [Podziel](#split-mask) lub [Wyryj](#carve). Opcje pod nimi zmieniają się zależnie od operacji.

* `Podgląd` - Pokazuje, jak będzie wyglądać nowa geometria, gdy zmieniasz ustawienia.
* `X-Ray` - Które obiekty są rysowane w trybie prześwietlenia podczas podglądu: `Brak`, `Nie zaznaczony`, `Wybrane` lub `Wszystkie`.

##### Wyodrębnij {#extract}
* `Wyodrębnij` - Tworzy wyodrębnioną geometrię jako nowy obiekt.
* `Działanie zamykania` - Jak zamykany jest wyodrębniony kształt. `Brak` kopiuje zamaskowane wielokąty do nowego kształtu i zostawia go otwartym. `Wypełnienie` robi to samo, a dodatkowo wypełnia i wygładza otwór z tyłu (nie używaj go na płaskich powierzchniach). `Powłoka` zamyka kształt, korzystając z wartości `Wysokość`, i jest opcją domyślną.

::: tip

Jeśli podgląd jest włączony razem z prześwietleniem, kliknięcie przycisku Wyodrębnij może na początku zdezorientować. Ponieważ menu jest aktywne, Nomad próbuje pokazać podgląd wyodrębnienia na twoim nowym kształcie, a oryginalną powierzchnię wyświetla w prześwietleniu. Na nowej powierzchni nie ma jednak maski, więc podglądu nie da się pokazać i Nomad ostrzega, że nie ma czego wyodrębnić.

To normalne. Zamknij menu ustawień maski, aby zobaczyć nowy kształt i oryginał, a jeśli chcesz wyczyścić maskę lub narysować nowe, ponownie zaznacz oryginalną powierzchnię.
:::

##### Podziel {#split-mask}
* `Podziel` - Wyodrębnia do nowych kształtów zarówno obszary zamaskowane, JAK I niezamaskowane.
* `Działanie zamykania` (zamaskowane) - Jak zamykana jest zamaskowana część, z tymi samymi opcjami `Brak`, `Wypełnienie` i `Powłoka` co przy wyodrębnianiu.
* `Działanie zamykania` (niezamaskowane) - Jak zamykana jest niezamaskowana część, z tymi samymi opcjami.

##### Wyryj {#carve}
* `Wyryj` - Działa tak, jakbyś przyciął powierzchnię na głębokość `Wysokość`, jak przy wycinaniu kawałka skórki pomarańczy. `Wysokość` nie może wynosić 0.

##### Wysokość {#thickness}
* `Wysokość` - Wysokość wyodrębnionego kształtu. Przycisk plus/minus przełącza między wytłaczaniem na zewnątrz, do wewnątrz lub w obie strony.

##### Gładkość {#smoothness}
Gdy włączone, wygładza wyodrębniony kształt. Działa lepiej przy większej liczbie wielokątów.
* `Wszystkie` / `Tylko brzegi` - Wygładza cały kształt albo tylko jego brzegi, nie ruszając kształtu górnej powierzchni.
* `Iteracje` - Przy opcji `Wszystkie` siła wygładzania. Wysokie wartości dają bardzo gładkie, zaokrąglone krawędzie, ale kształt zaczyna odbiegać od maski.
* `Ścianka` - Przy opcji `Tylko brzegi` siła wygładzania ścianek. Jej przycisk przełącza między Złagodź, które zachowuje ostre narożniki, a Wygładź, które również je zaokrągla.
* `Wnętrze` - Przy opcji `Tylko brzegi` jak bardzo wyrównywana jest górna powierzchnia. Jej przycisk przełącza między Złagodź, które zachowuje wyrzeźbione detale i wyrównuje tylko kierunek wytłaczania (dzięki czemu detale nie tworzą kolców), a Wygładź, które wygładza samą powierzchnię.

##### Boki {#edge-loop-side}
* `Proste` - Zwykłe ścianki po bokach wyodrębnionego kształtu.
* `Faza` - (tylko Wyodrębnij z opcją `Powłoka`) Skośne obrzeże na przedniej krawędzi. `Faza` ustawia jego szerokość w % wartości `Wysokość` lub w jednostkach świata (przełącza je przycisk obok), `Podziały fazy` je dzielą (domyślnie `Auto`), a krzywa pozwala nadać mu profil.
* `Profil` - Kształtuje ścianki krzywą profilu, o szerokości `Szerokość` w % wartości `Wysokość` lub w jednostkach świata.
* `Maska` - Wysokość podąża za maską: rozmyte fragmenty maski dostają mniejszą wysokość, co pozwala tworzyć miękkie kształty o zmiennej wysokości.
* `Podziały ścianki` - Liczba pętli krawędzi na bokach. Przy opcji `Auto` Nomad dobiera liczbę podziałów tak, by powstały kwadratowe wielokąty pasujące do wielokątów zamaskowanego obszaru.



### ![](/icons/tool_maskSelector.webp) Maska zaznaczenia {#selection-mask}
Narzędzie Maska zaznaczenia (Zaz. maskę) jest teraz częścią [narzędzia Maska](#mask). Aby maskować kształtami zamiast pociągnięciem pędzla, wybierz kształt (`Lasso`, `Wielokąt`, `Prostokąt`...) w okienku pociągnięć narzędzia Maska, zobacz [Sterowanie zaznaczeniem](#selection-controls).

Tryb alternatywny `Usuń maskę` działa także z kształtami i wymazuje maskę wewnątrz kształtu.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Farba {#paint}
Nakłada kolor i właściwości materiału. Więcej o materiałach przeczytasz w sekcji [Malowanie](painting.md).

Tryb alternatywny to `Wymaż`: usuwa farbę.

Oprócz pociągnięć pędzlem Farba potrafi też wypełniać kształty (`Lasso`, `Prostokąt`, `Pas`...), zobacz [Sterowanie zaznaczeniem](#selection-controls).

#### Ustawienia narzędzia Farba {#paint-settings}
* `Filtrowanie warstwy` - Działa jak blokada przezroczystości warstwy w Photoshopie czy Procreate. Gdy malujesz na warstwie z włączoną tą opcją, możesz zmieniać tylko miejsca, gdzie farba już jest, a niepomalowane obszary są chronione. Opcja jest dostępna tylko wtedy, gdy zaznaczona jest warstwa.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smużenie {#smudge}
Rozmazuje kolor i właściwości materiału. Menu ustawień smużenia zawiera suwak `Jakość`: niższe wartości oznaczają szybsze pociągnięcia.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Spłaszcz {#flatten}
Spłaszcza obszar, rzutując punkty na uśrednioną płaszczyznę.

Tryb alternatywny to `Wypełnij`: wyznacza płaszczyznę na wysokości najwyższego punktu i ma tendencję do podciągania punktów w górę.

#### Ustawienia narzędzia Spłaszcz {#flatten-settings}

* `Zablokuj kierunek płaszczyzny` - Używa kierunku płaszczyzny obliczonego przy pierwszym kliknięciu. Domyślnie wyłączone.
* `Zablokuj początek płaszczyzny` - Używa pierwszego kliknięcia jako środka płaszczyzny. Domyślnie wyłączone; można to włączyć tylko razem z `Zablokuj kierunek płaszczyzny`.

Gdy jedna z tych opcji lub obie są wyłączone, możesz stopniowo pogłębiać spłaszczenie albo zmieniać kąt płaszczyzny długimi pociągnięciami, które przechodzą przez obszary o różnej głębokości i krzywiźnie. W połączeniu z opcjami próbkowania obszaru w menu pędzla daje to bardzo precyzyjną kontrolę.

::: tip
Gdy pracujesz w miejscach o dużej krzywiźnie, np. spłaszczasz policzki, a narzędzie wciąż zahacza o boki nosa, utwórz maskę, która ochroni obszary, których pędzel Spłaszcz nie powinien ruszać.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Płaski {#planar}
Ustawia punkty w jednej płaszczyźnie, rzutując je na uśrednioną płaszczyznę, ale z mniejszym narastaniem niż pędzel Spłaszcz. Daje to czystsze powierzchnie z ostrymi krawędziami. Szybkie pociągnięcia mocniej wypychają i wciągają powierzchnię, a wolniejsze, zaczynane od już płaskich obszarów i prowadzone na zewnątrz, lepiej utrzymują płaszczyznę.

Tryb alternatywny to `Wypełnij`: wyznacza płaszczyznę na wysokości najwyższego punktu i ma tendencję do podciągania punktów w górę.

Płaski to w rzeczywistości to samo narzędzie co `Spłaszcz`, ale z włączoną opcją `Zablokuj kierunek płaszczyzny`. Dzięki temu tworzy stabilniejsze powierzchnie z ostrymi krawędziami, podczas gdy Spłaszcz jest bardziej rzeźbiarski i nadaje się do tworzenia półpłaskich obszarów.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Poleruj {#polish}
Kolejny członek rodziny Spłaszcz, ustawiony tak, by polerować powierzchnie do czystych płaszczyzn. To samo narzędzie co `Spłaszcz`, ale z innymi domyślnymi ustawieniami w menu [Pociągnięcie](stroke.md): włączone są `Ślad pociągnięcia pędzla`, `Filtr normalnych obszaru` i `Maskowanie głębokości`.

Tryb alternatywny to `Wypełnij`, tak jak w narzędziu Spłaszcz.

Poleruj ma te same ustawienia co [Spłaszcz](#flatten-settings): `Zablokuj kierunek płaszczyzny` i `Zablokuj początek płaszczyzny`.

### ![](/icons/tool_crease.webp) Bruzda {#crease}
Narzędzie Bruzda przydaje się do rzeźbienia małych nacięć i wgnieceń.

Tryb alternatywny to `Odwróć`: tworzy wypukłą bruzdę.

#### Ustawienia narzędzia Bruzda {#crease-settings}

* `Siła ściskania` - Jak mocno wierzchołki są ściągane na boki w stronę pędzla. Przy ściskaniu równym 1 i przesunięciu równym 0 powierzchnia nie zmienia głębokości, zmienia się tylko topologia: krawędzie są ściągane w stronę pociągnięcia.
* `Współczynnik przesunięcia` - Jak mocno wierzchołki są wypychane lub wciągane w głąb. Przy ściskaniu równym 0 i przesunięciu równym 1 powstają głębokie bruzdy lub wypukłe wgniecenia, ale wyglądają na poszarpane, bo do bruzdy nie zostaje ściągnięte dość geometrii, by dokładnie zdefiniować jej boki i dno.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Ściśnięcie {#pinch}
Tego narzędzia możesz używać do wyostrzania krawędzi.

Tryb alternatywny to `Odwróć`: rozsuwa wierzchołki.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Przytnij {#trim}
Narzędzie Przytnij usuwa fragment siatki i daje kilka sposobów na to, co zrobić z pozostałą po nim luką. Obszar cięcia wyznaczasz za pomocą [sterowania zaznaczeniem](#selection-controls).

Tryb alternatywny to `Odwróć`: odwraca kształt, więc usuwana jest druga strona.

::: tip
Ponieważ to narzędzie rzutuje z kamery, zobaczysz ostrzeżenie, jeśli kamera jest w trybie perspektywy.

W trybie ortograficznym cięcie przez siatkę jest równoległe do widoku, czego zwykle się oczekuje. Przy kamerze perspektywicznej cięcie wygląda inaczej po dalszej stronie obiektu niż po bliższej.
:::

#### Ustawienia narzędzia Przytnij {#trim-settings}

Ustawienia są zebrane w sekcji `Wypełnianie otworów`:

* `Malowanie pociągnięciami` - Jeśli malowanie jest włączone w menu malowania, załatany obszar zostanie wypełniony aktualnie wybranym kolorem.
* `Boolean` - Wypełnia otwór po cięciu obszarem z czworokątów. Wypełniony obszar jest płaski.
* `Dziedzictwo` - Wypełnia otwór po cięciu obszarem z trójkątów. Wypełniony obszar jest płaski.
* `Wypełnij` - Wypełnia otwór obszarem z trójkątów. Wypełniony obszar jest zakrzywioną powierzchnią, jak błona bańki mydlanej.
* `Brak` - Nie wypełnia otworu.

Przy metodzie `Boolean` sekcja `Szczegół` zawiera:

* `Kształt` - Przybliżony rozmiar czworokątów i trójkątów po stronie kształtu cięcia.
* `Otwory` - Przybliżony rozmiar trójkątów lub wielokątów w wypełnionym otworze. Przycisk łącza obok `Szczegół` utrzymuje tę wartość zgodną z `Kształt`; rozłącz go, aby ustawiać ją osobno.
* `Zachowaj topologię` - Nie wygładza ani nie upraszcza brzegu cięcia, zachowując oryginalną topologię siatki w pobliżu zamaskowanych i ukrytych ścian.

Przy metodzie `Dziedzictwo`:

* `Szczegół` - Przybliżony rozmiar trójkątów użytych przy cięciu.
* `Wygładzanie otworów` - Jak mocno trójkąty są rozluźniane w wypełnionym obszarze.
* `Epsilon progu` - Wartość, którą możesz dostosować, aby poprawić działanie starszego algorytmu wypełniania otworów.

Przy metodzie `Wypełnij`:

* `Szczegół` - Przybliżony rozmiar trójkątów użytych przy cięciu.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Podziel {#split}
Działa podobnie jak [Przytnij](#trim), z tą różnicą, że Przytnij odrzuca zaznaczenie, a Podziel zachowuje je jako nowy obiekt.

Tryb alternatywny to `Podziel`: każdy kawałek zostaje osobnym obiektem, więc nachodzące na siebie kształty (np. przy symetrii) są cięte na osobne części, zamiast łączyć się w jedną.

#### Ustawienia narzędzia Podziel {#split-settings}

Podziel ma te same ustawienia `Wypełnianie otworów` co [Przytnij](#trim-settings): `Malowanie pociągnięciami`, metody `Boolean`, `Dziedzictwo`, `Wypełnij` i `Brak` oraz ich opcje `Szczegół`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Rzutuj {#project}
Narzędzie Rzutuj przypomina narzędzie [Przytnij](#trim), ale nie usuwa ani nie tworzy geometrii, tylko przesuwa wierzchołki tak, by dopasowały się do zaznaczenia.

![](/videos/tool_project.mp4)

::: tip
Jeśli użyjesz narzędzia Rzutuj na warstwie, suwakiem warstwy możesz płynnie mieszać kształt oryginalny z rzutowanym.
:::

### ![](/icons/tool_layer.webp) Warstwa {#layer}
Podnosi powierzchnię, ale ogranicza jej wysokość.

Jeśli trzymasz rysik na ekranie i wciąż malujesz po tym samym obszarze, Warstwa podniesie go do pewnej wysokości i dalej już nie pójdzie, w przeciwieństwie do innych narzędzi, które ciągle dokładają wysokości.

Uwaga: domyślnie limit obowiązuje tylko w obrębie jednego pociągnięcia! Gdy zaczniesz nowe pociągnięcie, narzędzie zacznie budować od nowej wysokości powierzchni.

Aby ustawić stałą maksymalną wysokość dla wielu pociągnięć, używaj narzędzia Warstwa razem z systemem [Warstw](layers.md) w Nomadzie.

Utwórz warstwę i użyj tego narzędzia. Maksymalna wysokość jest teraz wyznaczana przez warstwę, więc możesz robić wiele pociągnięć, a wysokość zawsze będzie taka sama.

`Odejmij` używa minimalnej głębokości, tworząc rowki.

#### Ustawienia narzędzia Warstwa {#layer-settings}

* `Użyj danych warstwy` - Gdy włączone i zaznaczona jest warstwa, maksymalna wysokość jest wyznaczana na podstawie danych warstwy. Ostrzeżenie przypomina, gdy żadna warstwa nie jest zaznaczona.
* `Napełnij` - Gdy włączone, dostosowuje kierunek działania narzędzia Warstwa, aby uzyskać gładszy wynik.
* `Złagodź (Normalna)` - Przy włączonej opcji `Napełnij` siła wygładzania normalnych.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Napełnij {#inflate}
Przesuwa wierzchołki wzdłuż ich własnych normalnych. `Odejmij` przesuwa wierzchołki wzdłuż odwróconych normalnych.

#### Ustawienia narzędzia Napełnij {#inflate-setings}
* `Złagodź (Normalna)` - Siła wygładzania normalnych.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Przesuń {#nudge}
Przesuwa lub „rozmazuje” punkty w kierunku pociągnięcia.

Tryb alternatywny to `Fałda`: przepycha fałdę materiału wzdłuż pociągnięcia, z wybrzuszeniem przed pędzlem i zagłębieniem za nim.

#### Ustawienia narzędzia Przesuń {#nudge-settings}
* `Gładkie` - Jak mocno obszar pod pędzlem jest wygładzany podczas przesuwania, dzięki czemu rozmazana powierzchnia pozostaje czysta.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stempel {#stamp}

Kliknij i przeciągnij, aby wypiętrzyć fragment rzeźby w kształcie wybranej alfy.

To po prostu [narzędzie Pędzel](#brush) z typem pociągnięcia ustawionym na `Blokada + promień`.

`Odejmij` wciska stempel w powierzchnię, zamiast go z niej wyciągać.

::: tip
Stempel zwykle działa najlepiej na geometrii o wysokiej rozdzielczości. Jeśli poszukasz w sieci haseł typu „wrinkles alpha”, „pores alpha”, „scales alpha” itp., takie tekstury alfa w połączeniu ze Stemplem świetnie nadają się do dodawania organicznych detali do rzeźby postaci.

Dwa tryby pociągnięcia przydają się do różnych rzeczy.

* `Blokada + promień` ma stałą *wysokość*, a przeciąganie zmienia szerokość i obrót stempla. Dobre do tekstur skóry, które muszą mieć tę samą głębokość/wysokość, ale różne obroty i skale, żeby ukryć powtarzający się wzór.
* `Blokada + intensywność` ma stałą *szerokość*, a przeciąganie zmienia obrót i wysokość stempla. Dobre do nitów, które muszą mieć ten sam rozmiar, ale różne obroty i wysokości.

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Odciska wektorową mapę przemieszczeń (VDM). W odróżnieniu od alfy, która może tylko wypchnąć powierzchnię w górę lub w dół, VDM przechowuje pełny kształt 3d, więc może odcisnąć nawisy, takie jak uszy, rogi czy zawinięte liście. Działa jak [Stempel](#stamp), z tymi samymi trybami pociągnięcia `Blokada + promień` i `Blokada + intensywność`.

`Odejmij` (`Odwróć`) odwraca głębokość stempla, aby wcisnąć go w powierzchnię jak formę.

Samą mapę VDM wybierasz w menu [Alfa](stroke.md#alpha), które ma też suwak `Wysokość` skalujący tylko wysokość stempla, bez zmiany jego przemieszczenia na boki.

Przycisk `Utwórz` na lewym pasku narzędzi pozwala tworzyć własne stemple:

* `Nowy VDM...` - Dodaje płaszczyznę przygotowaną do rzeźbienia VDM. Wyrzeźb na niej swój kształt, a potem wypal go przez `Topologia -> Zastosuj -> VDM`: Nomad doda nowy stempel do biblioteki VDM i go wybierze.
* `Przechwyć VDM` - (eksperymentalne) Przeciągnij po powierzchni modelu, aby pobrać ten fragment i zamienić go w stempel VDM. `Tolerancja` płynnie spłaszcza brzeg przechwyconego obszaru.

::: tip
Nie używaj DynTopo podczas rzeźbienia na płaszczyźnie VDM: psuje to UV płaszczyzny i zniekształca stempel. Trzymaj też rzeźbę z dala od brzegu płaszczyzny, inaczej stempel będzie miał ostrą krawędź.
:::


### ![](/icons/tool_clearLayer.webp) Usuń warstwę {#delete-layer}
To narzędzie pozwala lokalnie zresetować warstwy. Potrzebujesz aktywnej warstwy, inaczej nic się nie stanie. Wymazuje wyrzeźbione dane warstwy, a przy włączonym malowaniu także jej farbę.

Tryb alternatywny to `Odwróć`: zamiast wymazywać warstwę, lekko ją wzmacnia.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Rura {#tube}
Tworzy rurę na podstawie narysowanej krzywej.
![](/images/tool_tube_new.webp)

Po utworzeniu rury jej ścieżkę możesz edytować w przestrzeni 3d za pomocą przycisków podobnych do standardowej [edycji kształtu](#shape-editing) i edycji krzywych.

![](/videos/tool_tube.mp4)

#### Lewy pasek narzędzia Rura {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Lewy pasek narzędzi ma następujące opcje:

* `Synchronizacja` - Jeśli bieżąca rura ma instancje, a obiekty podrzędne rury różnią się między instancjami, ta opcja ponownie je synchronizuje.
* `Przyciągnij` - Gdy włączone, w trybach krzywej i ścieżki rysowana rura przyciąga się do innych obiektów. Gdy wyłączone, przyciąga się tylko pierwszy punkt, a reszta rury jest rysowana na tej samej głębokości.
* `Przesunięcie` - Ustala głębokość przyciągania: przy 0% środek przekroju rury przyciąga się do powierzchni, wartości dodatnie unoszą ją nad powierzchnię, a ujemne obniżają. 100% odpowiada promieniowi rury.
* `Widok` - Brak trybu rysowania, więc możesz swobodnie poruszać kamerą.
* `Krzywa` - Odręczne szkicowanie rury. Ma małe rozwijane menu:
    * `Edytuj` - Co się dzieje po zakończeniu pociągnięcia, zobacz [Sterowanie zaznaczeniem](#selection-controls): od razu tworzy rurę, zostawia krzywą do edycji z zielonym kółkiem zatwierdzania obok albo pozwala `Edycja: przytrzymaj` na końcu pociągnięcia, aby dalej edytować.
    * `Zamknięty` - Zamienia rurę w pętlę.
    * `Rysuj dalej` - Po zatwierdzeniu rury zostajesz w narzędziu, aby narysować kolejną.
    * `Dokładność` - Ile punktów krzywej zostanie użytych do zamiany narysowanej ścieżki w rurę. 0% używa najmniejszej liczby punktów, ale pomija drobne zmiany krzywizny. 100% jest bardzo dokładne i używa wielu punktów.
* `Ścieżka` - Tworzy rurę przez klikanie kolejnych punktów krzywej. Stuknij zielone kółko, aby zatwierdzić ścieżkę. Ma małe rozwijane menu:
    * `B-splajn` - Alternatywna metoda rysowania krzywej, w której punkty krzywej zwykle nie leżą bezpośrednio na niej, ale wynik może być gładszy niż przy metodzie domyślnej.
    * `Zamknięty` - Zamienia rurę w pętlę.
    * `Ekran` - Gdy włączone, ścieżka jest „przypięta” do ekranu, więc możesz poruszać widokiem i obiektem, a ścieżka zostaje w miejscu. Gdy wyłączone, ścieżka jest częścią sceny 3d i porusza się razem z kamerą i obiektami.
* `Przekrój` - Krzywa staje się pierścieniem wokół kształtu, przecinającym go przez dwa punkty wzdłuż kierunku, z którego patrzyłeś.

##### Górny pasek narzędzia Rura {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Gdy rura jest zaznaczona, u góry widoku pojawia się pasek z dodatkowymi przyciskami. Kliknij tytuł paska, aby go zwinąć lub rozwinąć, a strzałkę w prawym górnym rogu, aby przenieść pasek na górę lub na dół widoku.

* `Zatwierdź` - Zamienia rurę w zwykłe wielokąty, aby można ją było rzeźbić.
* `Edytuj` - Pokazuje punkty krzywej, aby można było nimi manipulować.
* `Lustro` - Dodaje powtarzacz lustrzany jako rodzica tej krzywej.
* `Przyciągnij` - Przyciąga punkty krzywej do pobliskich powierzchni.
* `Zamknięty` - Łączy początek i koniec krzywej w pętlę.
* `B-splajn` - Przełącza między interpolacją Catmull-Rom a B-splajn.
* `Zakończenie` - Przełącza kolejno: zakończenia na obu końcach rury, tylko na początku lub tylko na końcu, albo brak zakończeń.
* `Otwór` - Nadaje rurze grubość, zamieniając ją w rurkę z otworem. Przełącza kolejno: otwór na obu końcach, tylko na końcu albo brak otworów.
* `Promień` - Przełącza kolejno: jednolity promień, promień na początku i na końcu albo promień dla każdego punktu krzywej. Edytujesz je pomarańczowymi uchwytami na krzywej.
* `Skręt` - Przełącza kolejno: brak skrętu, jednolity skręt, skręt na początku i na końcu albo skręt dla każdego punktu krzywej. Edytujesz je różowymi uchwytami na krzywej.
* `Profil` - Przełącza kolejno: brak profilu (czyli profil okrągły), jednolity profil, profil na początku i na końcu albo profil dla każdego punktu.
* `Edycja profilu` - Pokazuje edytor profilu. Działa podobnie jak [edycja kształtu](#shape-editing), pozwala zapisywać i wczytywać ustawienia wstępne profilu i ma przełącznik, który pozwala edytować profil w przestrzeni 3d.
* `Spirala` - Pokazuje menu, które dodaje do rury spiralny skręt. Menu ma opcje `Kąt skrętu`, `Przesunięcie`, `Skala` i `Przesunięcie kąta`.
* `Podział X` - Liczba podziałów wokół rury; na przykład 4 podziały dają rurę o kwadratowym przekroju.
* `Stała gęstość` - Gdy włączone, utrzymuje kwadratowe wielokąty. Gdy wyłączone, pozwala ustawić `Podział Y` wzdłuż długości rury.
* `...` - Menu ustawień rury.

#### Przełącznik usuwania punktów krzywej {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Pod paskiem jest przełącznik usuwania punktów krzywej. Gdy przeciągasz punkt krzywej blisko innego, robi się czerwony, co oznacza, że po puszczeniu zostanie usunięty. Jeśli robisz drobne poprawki i nie chcesz usuwać punktów, ten przycisk wyłącza usuwanie.



#### Ustawienia rury {#tube-settings}
* `Prymityw` - Przyciski do włączania i wyłączania UV oraz do zatwierdzania rury.
* `Podział następczy` - Skrót do ustawienia poziomu wielokrotnej rozdzielczości przed zatwierdzeniem.
* `Podział liniowy` - Skrót do ustawienia poziomu podziału liniowego przed zatwierdzeniem.
* `Podział X` - To samo co `Podział X` na pasku.
* `Podział Y` - To samo co `Podział Y` na pasku.
* `Krzywa (Powtarzacz)` - Zamienia rurę w [powtarzacz krzywej](scene.md#curve).

::: tip
4 podziały i podział następczy na poziomie 3 dają gładkie rury o zaokrąglonych końcach, dobre na robaki, węże czy części ciała.
:::


### ![](/icons/tool_lathe.webp) Bryła obrotowa {#lathe}
Tworzy powierzchnię obrotową na podstawie narysowanej krzywej.

To narzędzie świetnie sprawdza się przy kształtach takich jak wazony czy kieliszki.

![](/videos/tool_lathe.mp4)

#### Lewy pasek narzędzia Bryła obrotowa {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Lewy pasek narzędzi ma następujące opcje:

* `Synchronizacja` - Jeśli bieżąca bryła obrotowa ma instancje, a jej obiekty podrzędne różnią się między instancjami, ta opcja ponownie je synchronizuje.
* `Stałe` - Gdy włączone, oś bryły obrotowej jest ustalona i widoczna na ekranie. Ta linia środkowa ma punkty edycji, które możesz przesuwać. Gdy wyłączone, oś bryły jest na bieżąco dopasowywana do początku i końca narysowanej krzywej.
* `Widok` - Brak trybu rysowania, więc możesz swobodnie poruszać kamerą.
* `Krzywa` - Rysuje profil bryły jednym pociągnięciem. Ma małe rozwijane menu:
    * `Edytuj` - Co się dzieje, gdy podniesiesz rysik, zobacz [Sterowanie zaznaczeniem](#selection-controls): od razu tworzy bryłę, zostawia krzywą do edycji z zielonym kółkiem obok, które tworzy bryłę, albo pozwala `Edycja: przytrzymaj` na końcu pociągnięcia, aby dalej edytować.
    * `Zamknięty` - Łączy początek i koniec krzywej w pętlę.
    * `Rysuj dalej` - Po zatwierdzeniu bryły obrotowej zostajesz w narzędziu, aby narysować kolejną.
    * `Dokładność` - Ile punktów krzywej zostanie użytych do zamiany narysowanej ścieżki w bryłę. 0% używa najmniejszej liczby punktów, ale pomija drobne zmiany krzywizny. 100% jest bardzo dokładne i używa wielu punktów.
* `Ścieżka` - Tworzy bryłę obrotową przez klikanie kolejnych punktów krzywej. Stuknij zielone kółko, aby zatwierdzić ścieżkę. Ma małe rozwijane menu:
    * `B-splajn` - Alternatywna metoda rysowania krzywej, w której punkty krzywej zwykle nie leżą bezpośrednio na niej, ale wynik może być gładszy niż przy metodzie domyślnej.
    * `Zamknięty` - Zamienia krzywą w pętlę.
    * `Ekran` - Gdy włączone, ścieżka jest „przypięta” do ekranu, więc możesz poruszać widokiem i obiektem, a ścieżka zostaje w miejscu. Gdy wyłączone, ścieżka jest częścią sceny 3d i porusza się razem z kamerą i obiektami.

#### Górny pasek narzędzia Bryła obrotowa {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Gdy bryła obrotowa jest zaznaczona, u góry widoku pojawia się pasek z dodatkowymi przyciskami. Kliknij tytuł paska, aby go zwinąć lub rozwinąć, a strzałkę w prawym górnym rogu, aby przenieść pasek na górę lub na dół widoku.

* `Zatwierdź` - Zamienia bryłę obrotową w zwykłe wielokąty, aby można ją było rzeźbić.
* `Edytuj` - Pokazuje punkty krzywej, aby można było nimi manipulować.
* `Lustro` - Dodaje powtarzacz lustrzany jako rodzica tej bryły.
* `Przyciągnij` - Przyciąga punkty krzywej do pobliskich powierzchni.
* `Stabilny` - Gdy włączone, profil krzywej jest podporządkowany linii środkowej bryły. Gdy wyłączone, linię środkową możesz edytować bez przesuwania krzywej, co pozwala uzyskać bardziej złożone kształty.
* `Ostrość` - Obraca widok tak, by profil krzywej był widoczny idealnie płasko względem kamery.
* `Zamknięty` - Łączy początek i koniec krzywej w pętlę.
* `Zakończenie` - Gdy opcja Zamknięty jest wyłączona, przełącza kolejno: zakończenia na obu końcach, tylko na początku lub tylko na końcu, albo brak zakończeń.
* `Otwór` - Nadaje bryle grubość, zamieniając ją w rurkę z otworem. Przełącza kolejno: otwór na obu końcach, tylko na końcu albo brak otworów.
* `B-splajn` - Przełącza między interpolacją Catmull-Rom a B-splajn.
* `Podział X` - Liczba podziałów wokół bryły; na przykład 4 podziały dają bryłę o kwadratowym przekroju.
* `Stała gęstość` - Gdy włączone, utrzymuje kwadratowe wielokąty. Gdy wyłączone, pozwala ustawić `Podział Y` wzdłuż długości profilu.
* `...` - Menu ustawień bryły obrotowej.

#### Ustawienia bryły obrotowej {#lathe-settings}
* `Prymityw` - Przyciski do włączania i wyłączania UV oraz do zatwierdzania bryły.
* `Podział następczy` - Skrót do ustawienia poziomu wielokrotnej rozdzielczości przed zatwierdzeniem.
* `Podział liniowy` - Skrót do ustawienia poziomu podziału liniowego przed zatwierdzeniem.
* `Podział X` - To samo co `Podział X` na pasku.
* `Podział Y` - To samo co `Podział Y` na pasku.
* `Krzywa (Powtarzacz)` - Zamienia profil krzywej w [powtarzacz krzywej](scene.md#curve).

### ![](/icons/tool_insert.webp) Wstaw {#insert}
Umieszcza obiekt na powierzchni innego obiektu. W użyciu przypomina narzędzie Stempel, ale dla pełnych kształtów 3d.

Jeśli wybierzesz prymityw na lewym pasku narzędzi, kliknięcie i przeciągnięcie po dowolnej powierzchni umieści prymityw w miejscu kliknięcia, a przeciągnięcie ustali jego rozmiar. Gdy skończysz przeciągać, Wstaw przełączy się w tryb [Przekształcenie](#transform).

W trybie instancji przeciąganie tworzy nową instancję i przesuwa ją po powierzchni. Rozmiar jest kopiowany z pierwszego kształtu, dzięki czemu możesz rozmieścić na innych powierzchniach wiele instancji obiektu o tym samym rozmiarze.

Nie musisz wstawiać wyłącznie prymitywów! Zaznacz *dowolny* kształt na liście obiektów sceny, a jeśli Wstaw jest w trybie instancji lub klonowania, możesz przeciągać kopie zaznaczonego obiektu po dowolnej innej powierzchni.

Jeśli obiekt ma własny punkt obrotu, służy on jako punkt zaczepienia. Zobacz film poniżej.

Lewy pasek narzędzi ma też przycisk `Widok`, aby poruszać kamerą bez wstawiania czegokolwiek, oraz `Synchronizacja`: gdy obiekt docelowy ma instancje, nowy obiekt jest dodawany także do wszystkich pozostałych instancji.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Przekształcenie {#transform}
Przesuwa, obraca i skaluje model bezpośrednio jednym lub dwoma palcami, zwykle po powierzchni innego obiektu.

Lewy pasek narzędzi ma takie przyciski:

* `Klonuj` / `Instancja` - Tworzy kopię lub instancję obiektu, zobacz paski narzędzia [Gizmo](#left-menu-toolbar).
* `Przenieś` - Przeciąganie jednym palcem przesuwa obiekt. Gdy przyciąganie jest włączone, obiekt przesuwa się po powierzchni pod palcem.
* `Obróć` - Przeciąganie jednym palcem obraca obiekt. Gdy przyciąganie jest włączone, obraca go wokół normalnej powierzchni pod palcem.
* `Skala` - Przeciąganie jednym palcem skaluje obiekt.

Pasek u góry widoku zawiera:

* `Cel` - Czy narzędzie przesuwa obiekt, jego grupę czy jego wierzchołki, tak samo jak w przypadku [Gizmo](#left-menu-toolbar).
* `Przyciągnij` - Przyciąga model do innych powierzchni.
* `Powierzchnia` / `Wierzchołek` - Przy włączonym `Przyciągnij` przyciąga do powierzchni albo do najbliższego wierzchołka.

Przekształcenie pozwala szybko łączyć 2 z tych trybów za pomocą dwóch palców:

* Przeciągnij obiekt, aby go ustawić. Zatrzymaj pierwszy palec, ale nie odrywaj go od ekranu.
* Dotknij ekranu drugim palcem, wciąż trzymając pierwszy. Gdy przeciągasz drugim palcem, obiekt się skaluje.
* Podnieś drugi palec i dalej przeciągaj pierwszym, a obiekt znów będzie w trybie przesuwania.

Drugi tryb możesz też zmienić stuknięciem drugiego palca:

* Przeciągnij obiekt, aby go ustawić, zatrzymaj się, ale nie odrywaj palca od ekranu.
* Stuknij drugim palcem, wciąż trzymając pierwszy.
* Narzędzie przełącza się w tryb obrotu. Przeciągnij pierwszym palcem, aby ustawić obrót.
* Stuknij drugim palcem jak wcześniej, a narzędzie wróci do trybu przesuwania.

To szybki sposób na rozmieszczanie klonów obiektu na innym obiekcie, np. kamieni na krajobrazie. Zauważ, że przycisk klonowania jest też pod ręką na lewym pasku narzędzi:

* Narzędziem Przekształcenie przesuń kamień na miejsce.
* Puść i naciśnij przycisk klonowania.
* Przesuń ten kamień, obróć lub przeskaluj go w razie potrzeby.
* Puść i naciśnij przycisk klonowania.
* Przesuń ten kamień i powtarzaj.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
To narzędzie pozwala przesuwać, obracać i skalować obiekty, a także zmieniać ich punkty obrotu.

Uchwyt w widoku ma następujące funkcje:

* `Przenieś` - Przeciągnij linię ze strzałką, aby przesuwać wzdłuż X/Y/Z. Przeciągnij brzoskwiniową kropkę na środku gizmo, aby przesuwać swobodnie w przestrzeni ekranu. Kliknij czerwony, zielony lub niebieski kwadrat, aby przesuwać w płaszczyznach X/Y/Z.
* `Obróć` - Przeciągnij czerwony, zielony lub niebieski okrąg, aby obracać wokół X/Y/Z. Przeciągnij kulę wewnątrz okręgów, aby obracać swobodnie.
* `Skala` - Przeciągnij zewnętrzne czerwone, zielone lub niebieskie kropki, aby skalować wzdłuż X/Y/Z. Przeciągnij zewnętrzne czerwone, zielone lub niebieskie stożki, aby skalować w płaszczyznach X/Y/Z. Przeciągnij zewnętrzny brzoskwiniowy okrąg, aby skalować jednolicie.

![](/images/tool_gizmo.webp)

#### Węzły i wierzchołki {#nodes-and-vertices}

Każdy obiekt w Nomadzie składa się z węzła i wierzchołków:

* `Węzeł` - „Uchwyt” obiektu, który przechowuje jego przesunięcie, obrót i skalę, czyli tak zwaną macierz przekształcenia.
* `Wierzchołki` - Punkty, które wyznaczają powierzchnię obiektu. Przechowują położenie i informacje o malowaniu.

Jeśli masz prosty sześcian złożony z 8 wierzchołków, możesz go przesunąć, zmieniając jego macierz przekształcenia albo położenie wierzchołków. Przy rzeźbieniu zwykle chcesz zmieniać wierzchołki, a przy przesuwaniu obiektów gizmo zwykle chcesz zmieniać węzeł. Nomad pozwala na jedno i drugie.

#### Paski narzędzia Gizmo {#left-menu-toolbar}

Lewy pasek narzędzi zawiera:

* `Klonuj` - Tworzy samodzielną kopię bieżącego obiektu, którą możesz odciągnąć za pomocą gizmo.
* `Utwórz instancję` - Tworzy kopię bieżącego obiektu jako instancję. Obiekty są powiązane, więc zmiany wyrzeźbione na jednym pojawią się na wszystkich instancjach.
* `Pkt obrotu` - (ikona kłódki, w miejscu przycisku `Odejmij`) Gdy włączone, gizmo możesz przesuwać i obracać bez przesuwania obiektu. Podobnie jak `Odejmij`, przytrzymaj go, aby włączyć na chwilę, albo stuknij, aby pozostał włączony.

Pasek u góry widoku zawiera pozostałe przyciski:

* `Cel` - Ustala, czy gizmo działa na węzeł, czy na wierzchołki obiektu:
    * `Auto` - Domyślne. Działa jak `Grupa`, ale jeśli siatka ma maskę lub symetria jest włączona, działa jak `Wierzchołek`.
    * `Wierzchołek` - Stosuje przekształcenie do wierzchołków, uwzględniając maskę i symetrię. Nie działa na niezatwierdzonych prymitywach, a instancje też są zmieniane.
    * `Obiekt` - Przesuwa tylko bieżący obiekt, ignorując symetrię i maskę. Obiekty podrzędne zostają na miejscu.
    * `Grupa` - Przesuwa obiekt razem z resztą jego hierarchii, ignorując symetrię i maskę.
    * `Instancja` - (Obiekt i Grupa) To samo, ale razem z obiektem przesuwa się każda jego instancja.
* `Pkt obrotu` - Okienko do szybkiego ustawiania punktu obrotu, opisane [niżej](#pivot).
* `Wszystkie` / `Przenieś` / `Obróć` / `Skala` - Pokazuje wszystkie uchwyty gizmo albo tylko uchwyty przesuwania, obrotu lub skalowania.
* `Przypnij` - Domyślnie gizmo przenosi się do punktu obrotu zaznaczonego obiektu. Gdy przypinanie jest włączone, gizmo zostaje tam, gdzie jest.
* `Wyrównaj` - Przełącza wyrównanie punktu obrotu do bieżącego obiektu lub do świata.
* `Przyciągnij` (obrót) - Włącza przyciąganie wartości obrotu do kroków. Wartość kroku jest wyświetlana i można ją edytować, gdy przyciąganie jest aktywne. Jego opcja `Magnes` sprawia, że obrót przykleja się do kroku, gdy go mija, a potem znów porusza się swobodnie; wyłącz ją, aby przeskakiwać od kroku do kroku.
* `Przyciągnij` (przesunięcie) - Włącza przyciąganie wartości przesunięcia do kroków. Wartość kroku jest wyświetlana i można ją edytować, gdy przyciąganie jest aktywne.

#### ![](/icons/reset.webp) Punkt obrotu {#pivot}
Okienko `Pkt obrotu` na górnym pasku pozwala szybko zmienić punkt obrotu. Położenie i orientacja punktu obrotu wyznaczają gizmo.

**Wyzeruj**
* `Auto` - Środek obiektu, wyrównany do jego przekształcenia.
* `Wyśrodkowany` - Przenosi punkt obrotu na środek obiektu, zachowując jego orientację.
* `Dół` - Przenosi punkt obrotu na środek spodu obiektu. Stuknij ponownie, aby użyć zamiast tego prostopadłościanu otaczającego w układzie świata.
* `Góra` - Przenosi punkt obrotu na środek góry obiektu. Stuknij ponownie, aby użyć zamiast tego prostopadłościanu otaczającego w układzie świata.
* `Obiekt` - Przenosi punkt obrotu do początku układu obiektu, wyrównany do jego przekształcenia.
* `Maska` - Przenosi punkt obrotu na środek niezamaskowanego obszaru. Stuknij ponownie, aby przełączyć na obszar zamaskowany.
* `Wyrównaj` - Zeruje obroty tak, by były wyrównane do świata, zachowując położenie.
* `Widok` - Wyrównuje punkt obrotu do bieżącego widoku, zachowując położenie. Potem nie podąża już za kamerą.

**Po jednym stuknięciu (tryb Pkt obrotu)**

Działa tylko wtedy, gdy `Pkt obrotu` jest włączony. Ustala, co się dzieje, gdy raz stukniesz powierzchnię siatki:
* `Brak` - Nic się nie dzieje po stuknięciu obiektu.
* `Normalna` - Przesuwa i obraca punkt obrotu tak, by był wyrównany do stukniętego miejsca powierzchni.
* `Pierwsze trafienie` - Przesuwa (ale nie obraca) punkt obrotu do stukniętego miejsca powierzchni.
* `Środkowa pozycja` - Przesuwa punkt obrotu do środka obiektu, pod stukniętym miejscem powierzchni.

#### Ustawienia gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Kompaktowy` - Przełącza układ gizmo: dodatkowe uchwyty są na zewnątrz lub wewnątrz kuli obrotu.
* `Rozmiar widżetu` - Rozmiar gizmo.
* `Grubość` - Grubość linii gizmo.
* `Krycie` - Krycie gizmo.
* `Ukryj przy interakcji` - Czy gizmo ma być chwilowo ukrywane podczas przeciągania.

-----

* `Próg przechyłu stycznego` - Ustala, jak zachowuje się obrót, gdy przeciągasz okręgi, aby obracać wokół X/Y/Z. Przy wartości 0 obrót działa jak pokrętło: prowadzisz palec po okręgu. Przy wartości 90 działa jak ciągnięcie sznurka jo-jo: przeciągasz w linii prostej do miejsca pierwszego kliknięcia lub od niego. Wartości między 0 a 90 łączą oba sposoby: poniżej wartości działa ruch liniowy, powyżej ruch po okręgu.
* `Wprowadzanie numeryczne` - Gdy włączone, pojedyncze stuknięcie gizmo otwiera okno, w którym wpiszesz dokładną wartość dla stukniętej osi.

::: warning
Narzędzia [Gizmo](#gizmo) i [Przekształcenie](#transform) mają własne pole symetrii, niezależne od symetrii rzeźbienia!

Domyślnie ta symetria jest wyłączona.
:::

##### Macierz {#matrix}
Dokładnych wartości przekształcenia obiektu nie ma już w ustawieniach gizmo: zostały przeniesione do menu `Przekształcenie`, w menu w prawym górnym rogu. Jego sekcja `Macierz` zawiera:

* ![](/icons/target.webp) `Przenieś początek` - Przesuwa obiekt tak, by jego punkt obrotu znalazł się w środku sceny, czyli w początku układu.
* ![](/icons/bake.webp)  `Zastosuj` - Utrwala obiekt w jego obecnym położeniu i ustawia wartości przesunięcia i obrotu na 0, a skalę na 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pkt obrotu` - Utrwala punkt obrotu: wartości macierzy odpowiadają wtedy położeniu uchwytu gizmo w świecie.
* ![](/icons/reset.webp) `Wyzeruj` - Skrót, który ustawia przesunięcie na 0, obrót na 0 i skalę na 1, przesuwając i obracając obiekt.

::: tip Zastosuj a zastosowanie punktu obrotu
Utwórz sześcian, wybierz narzędzie Gizmo, otwórz i przypnij menu `Przekształcenie`. Domyślnie przesunięcie i obrót wynoszą 0, a skala 1.

Włącz tryb punktu obrotu, przesuń uchwyt w bok i wyłącz tryb punktu obrotu. Punkt obrotu się zmienił, ale zwróć uwagę, że wartości przesunięcia nadal wynoszą 0.

Jeśli chcesz zobaczyć, gdzie punkt obrotu *naprawdę* jest, kliknij przycisk `Pkt obrotu` (zastosowanie punktu obrotu). Teraz wartości przesunięcia się zaktualizują. Zwróć uwagę, że sześcian się przy tym nie porusza, podobnie jak w trybie punktu obrotu.

Przesuń i obróć sześcian gdzieś indziej, a potem stuknij `Przenieś początek`. Obiekt przesunie się tak, by jego punkt obrotu znalazł się w środku świata, ale obrót pozostanie bez zmian.

Kliknij `Wyzeruj`, a obrót także zostanie ustawiony na 0.

Znów przesuń i obróć sześcian, a tym razem kliknij `Zastosuj`. Punkt obrotu zostaje na miejscu, sześcian też, ale wartości przesunięcia i obrotu są ustawiane na 0.

Poćwicz to kilka razy! Zrozum, że wartości punktu obrotu są ukryte i Nomad dba o nie za ciebie, ale gdy chcesz ustawić punkt obrotu w rzeczywistym miejscu w przestrzeni, zrobi to za ciebie zastosowanie punktu obrotu.

:::

* `Translacja` - Wartości przesunięcia X, Y, Z.
* `Obrót` - Wartości obrotu X, Y, Z.
* `Skala` - Skala jednolita, jeśli jest włączona, albo skala X, Y, Z, jeśli jest wyłączona.
* `Ścinanie` - Wartości ścinania X, Y, Z, wyświetlane tylko wtedy, gdy obiekt jest już ścięty.
* `Jednolite skalowanie` - Przełącza skalowanie jednolite lub osobno dla każdej osi.

Po lewej możesz przesunąć punkt obrotu gizmo; zobacz, jak to działa, na filmie poniżej.
Jest to szczególnie przydatne przy obrocie, bo przy przesunięciu niczego nie zmienia.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Grupa powierzchni {#facegroup}

Grupy powierzchni pozwalają podzielić obiekt na ściany w różnych kolorach. W Nomadzie możesz ich używać na wiele sposobów:

* Szybkie zaznaczanie przy tworzeniu masek
* Ukrywanie i pokazywanie fragmentów obiektu
* Porządkowanie obiektu bez dzielenia go na osobne części
* Wyznaczanie obszarów UV
* Prowadzenie Quad Remeshera
* Dodatkowa kontrola w narzędziach takich jak Gładkie

#### Lewy pasek narzędzia Grupa powierzchni {#facegroup-left-toolbar}

* `Grupa` - Przycisk pokazuje bieżącą grupę powierzchni. Stuknij go, aby wyświetlić dostępne grupy powierzchni jako próbki i wybrać jedną. Stuknij próbkę, aby zmienić jej nazwę, kolor albo ją usunąć. `Usuń nieużywane` usuwa nieużywane próbki, a `Wyzeruj` usuwa je wszystkie. Ikona plusa tworzy nowe próbki.
* `Kropka` - Maluj po obiekcie, aby wyznaczać grupy powierzchni. Gdy włączona jest opcja „+ Grupa powierzchni”, każde nowe pociągnięcie automatycznie tworzy nową grupę powierzchni, co przydaje się do szybkiego wyznaczania obszarów. Stuknięcie wypełnia wybrany obszar. Suwak ustawia promień kropki.
* `Złagodź` - Wygładza granice grup powierzchni. Bardzo przydatne do wyznaczania czystych krawędzi przed przebudową na czworokąty albo paneli przy modelowaniu twardych powierzchni. Suwaki ustawiają promień i intensywność łagodzenia.
* Kształty - Tworzenie grup powierzchni kształtami zamiast pędzlem: `Blokada + promień`, `Lasso`, `Wielokąt`, `Linia`, `Prostokąt` i `Elipsa`. Więcej informacji znajdziesz w sekcji [Sterowanie zaznaczeniem](#selection-controls).
* `Wybierz` - Tryb alternatywny. Gdy włączony, wybiera próbkę z miejsca, w którym zaczyna się pociągnięcie, i stosuje ją przez resztę pociągnięcia. Bardzo przydatne przy porządkowaniu obszarów grup powierzchni: jeśli grupa rozlała się za daleko, włącz `Wybierz`, zacznij pociągnięcie tam, gdzie grupa jest poprawna, i przeciągnij do granicy, aby przypisać właściwą grupę.

#### Górny pasek narzędzia Grupa powierzchni {#facegroup-top-toolbar}

Pasek u góry widoku zawiera dodatkowe przyciski:

* `Złagodź (Wszystkie)` - Przeciągnij, aby złagodzić granice wszystkich grup powierzchni naraz.
* `Przód` / `Widoczne` / `Połączona` - Te same filtry pociągnięć co na pasku narzędzia [Maska](#mask).
* `Z normalnych` - Tworzy grupy powierzchni na podstawie kąta między ścianami. Okienko zawiera `Kąt` i pozwala pominąć małe grupy na podstawie `Liczba ścianek` lub `Powierzchnia`, z opcją `Podgląd` przed zatwierdzeniem.
* `Z części` - Tworzy grupę powierzchni dla każdej rozłącznej części.
* `Z UV` - Tworzy grupę powierzchni dla każdej wyspy UV.
* `Z maski` - Tworzy grupę powierzchni z zamaskowanego obszaru.
* `Po stuknięciu` - Wybierz, co robi stuknięcie grupy powierzchni: wypełnia ją bieżącą grupą powierzchni, ukrywa ją, maskuje ją albo ustawia `Poza` (stuknięta grupa i wszystko, co leży za nią, zostaje odmaskowane, a gizmo ląduje w miejscu stawu, z suwakiem `Rozmycie` dla maski). Drugi przełącznik `Po stuknięciu`, dostępny, gdy siatka ma maskę, ogranicza stuknięcie do ścian po tej samej stronie maski.
* Przyciski `Wyczyść` dla narzędzi [Ukryj](#hide) i [Maska](#mask), aby pokazać wszystko lub wyczyścić maskę bez wychodzenia z narzędzia.

#### Ustawienia narzędzia Grupa powierzchni {#facegroup-settings}

Menu `Narzędzie` wyodrębnia grupy powierzchni do nowych obiektów, z tymi samymi opcjami co `Wyodrębnij` w [ustawieniach maski](#mask-settings). Przycisk `Grupa powierzchni` u góry wybiera, które grupy są wyodrębniane, a dodatkowy suwak `Szczelina` przesuwa każdą granicę do środka wzdłuż powierzchni; wartość ujemna przesuwa ją na zewnątrz, tworząc zakładkę. Przy sąsiadujących panelach użyj połowy żądanej szczeliny.

### ![](/icons/tool_hide.webp) Ukryj {#hide}
Ukrywa lub izoluje fragmenty obiektu.

Główne tryby wybierasz w lewym menu:

* `Kropka` - Maluj po obiekcie, aby ukrywać jego fragmenty.
* Kształty - Ukrywanie kształtami zamiast pędzlem: `Lasso`, `Wielokąt`, `Linia`, `Prostokąt` i `Elipsa`. Więcej informacji znajdziesz w sekcji [Sterowanie zaznaczeniem](#selection-controls).
* `Pokaż` - Tryb alternatywny: odwraca działanie, więc wybrany tryb pokazuje fragmenty obiektu zamiast je ukrywać.

U góry widoku pojawia się pasek z dodatkowymi przyciskami:

* `Wyczyść wszystko` - Przywraca obiekty: wszystkie ukryte fragmenty znów stają się widoczne. Gdy inne obiekty też mają ukryte fragmenty, dodatkowy przycisk `Wyczyść` przywraca tylko zaznaczone obiekty.
* `Odwróć` - Zamienia fragmenty ukryte z widocznymi.
* `Usuń` - Usuwa ukrytą część obiektu.
* `Podziel` - Wydziela ukrytą część obiektu jako nowy kształt.
* `Przód` / `Widoczne` / `Połączona` - Te same filtry pociągnięć co na pasku narzędzia [Maska](#mask).
* `Po stuknięciu` (grupa powierzchni) - Pozwala szybko ukrywać fragmenty za pomocą grup powierzchni: stuknięcie grupy powierzchni ukrywa ją w całości.
* `Po stuknięciu` (maska) - Jeśli maska jest aktywna, stuknięcie ukrywa zamaskowany fragment.

### ![](/icons/tool_measure.webp) Zmierz {#measure}
Przeciągnij, aby zmierzyć odległość między 2 punktami. Po ich umieszczeniu możesz przeciągać punkty końcowe, aby poprawić pomiar.

Lewy pasek narzędzi wybiera sposób mierzenia odległości:

* `Linia` - Linia prosta między dwoma punktami.
* `Powierzchnia` - Odległość wzdłuż powierzchni, po przekroju przechodzącym przez dwa punkty, tak jak widać go z kamery.
* `Przekrój` - Obwód przekroju przechodzącego przez dwa punkty, jak miarka krawiecka owinięta wokół ramienia.
* `Wierzchołek` - Przyciąga punkty końcowe do najbliższego wierzchołka.
* `Złoty podział` - Pokazuje żółtą kropkę w punkcie złotego podziału pomiaru.
* Przycisk `?` pokazuje objętość, pole powierzchni i rozmiar zaznaczonych obiektów.

### ![](/icons/tool_arrange.webp) Rozmieść {#arrange}
Wyrównuje i rozmieszcza kilka obiektów naraz, jak narzędzia wyrównywania w aplikacjach do projektowania 2d. Najpierw zaznacz obiekty; przy jednym obiekcie Rozmieść działa na jego osobne części. Wokół zaznaczenia rysowana jest ramka, której uchwyty możesz przeciągać, aby ją skalować.

Pasek u góry widoku zawiera przyciski:

* `Świat` / `Ekran` - Rozmieszcza wzdłuż osi świata albo wzdłuż ekranu (lewo, prawo, góra, dół).
* `Wyrównaj` - Wyrównuje obiekty do ich minimum, środka lub maksimum, na każdej osi.
* `Rozłóż` - Rozkłada obiekty równomiernie między dwoma skrajnymi, według ich minimum, środka lub maksimum. Wymaga co najmniej 3 obiektów.
* `Linia` - Ustawia obiekty w rzędzie wzdłuż osi.
* `Siatka` - Ustawia obiekty w siatce, z określoną liczbą obiektów na `X`, `Y` i `Z`.
* `Okrąg` - (tylko Świat) Ustawia obiekty na okręgu wokół osi `X`, `Y` lub `Z`.
* `Kula` - (tylko Świat) Rozmieszcza obiekty na kuli.

`Linia`, `Siatka`, `Okrąg` i `Kula` mają suwak `Odstępy`, który ustala odstęp między obiektami.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

To narzędzie zamienia zaznaczony obiekt w czystą topologię z czworokątów, z kontrolą nad gęstością, przebiegiem krawędzi i symetrią.

::: tip
Quad Remesher jest rozwijany przez [Exoside](https://exoside.com/) na iOS i komputery.

Na iOS jest to zakup w aplikacji Nomad, jednorazowa płatność 16 USD.

Na komputerach kup licencję od [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Możesz kupić ją tylko dla Nomada na komputer albo licencję krzyżową dla wszystkich obsługiwanych aplikacji desktopowych.

Jeśli masz już Quad Remeshera dla innej aplikacji desktopowej, możesz [taniej kupić rozszerzenie na wszystkie platformy.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher nie jest dostępny na Androida. Na Androidzie możesz korzystać z darmowych narzędzi open source na karcie [Przebudowa na czworokąty](topology.md#quad-remesh) w menu Topologia (AutoRemesher, Instant Mesh, QuadriFlow), ale pamiętaj, że mają one mniej funkcji.
:::

Dopóki Quad Remesher nie jest odblokowany, górny pasek zaczyna się od przycisku koszyka zamiast przycisków przebudowy. Na iOS otwiera on zakup w aplikacji. Na komputerach pokazuje `Odblokuj (zakup, przywrócenie, wersja próbna)`, co sprawdza twoją licencję Exoside (albo uruchamia wersję próbną). Po aktywacji lewy i górny pasek stają się dostępne.

* `Kropka` - Ten pędzel ustala docelową gęstość. Intensywność 100% maluje na czerwono, co daje w tych miejscach dwukrotnie większą gęstość czworokątów. Intensywność 0% maluje na turkusowo, co daje w tych miejscach o połowę mniejszą gęstość. Intensywność 50% maluje na szaro, co oznacza domyślną docelową gęstość.
* `Gładkie` - Wygładza przejścia między czerwonymi, szarymi i turkusowymi obszarami gęstości.
* `Smużenie` - Rozmazuje malowanie gęstości.
* `Krzywa` - Szkicuj krzywe na powierzchni rzeźby; Quad Remesher użyje ich jako prowadnic dla przebiegu krawędzi. Stuknij krzywą, aby ją usunąć.
* `Ścieżka` - Rysuj ścieżki na powierzchni rzeźby; Quad Remesher użyje ich jako prowadnic dla przebiegu krawędzi. Stuknij ścieżkę, aby ją usunąć.
* `Prostokąt` - Rysuj prostokąty na powierzchni rzeźby; Quad Remesher użyje ich jako prowadnic dla przebiegu krawędzi. Stuknij prostokąt, aby go usunąć.
* `Elipsa` - Rysuj elipsy na powierzchni rzeźby; Quad Remesher użyje ich jako prowadnic dla przebiegu krawędzi. Stuknij elipsę, aby ją usunąć.

#### Górny pasek narzędzia Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

U góry widoku pojawia się pasek z dodatkowymi przyciskami:


* `<Count>` - Kliknij, aby uruchomić przebudowę. Ta liczba pokazuje docelową liczbę czworokątów.
* `Czworokąty` - Ustaw docelową liczbę czworokątów, przesuwając w lewo i w prawo, albo stuknij, aby wpisać dokładną liczbę. To raczej wskazówka niż sztywna liczba: różne ustawienia Quad Remeshera często sprawiają, że wynik nie trafia dokładnie w ten cel.
* `Połowa` - Skrót, który ustawia docelową liczbę na połowę bieżącej liczby wielokątów.
* `Tak samo` - Skrót, który ustawia docelową liczbę na bieżącą liczbę wielokątów.
* `Przewodniki` - Włącza lub wyłącza użycie prowadnic. Gdy prowadnice istnieją, drugi przycisk `Przewodniki` pokazuje ich liczbę; stuknij go, aby usunąć je wszystkie.
* `Gęstość` - Włącza lub wyłącza użycie malowania gęstości. Gdy malowanie gęstości istnieje, drugi przycisk `Gęstość` je usuwa.
* `Grupa powierzchni` - Włącza lub wyłącza użycie grup powierzchni do sterowania Quad Remesherem.
* `Złagodź` - Włącza automatyczne łagodzenie granic grup powierzchni podczas przebudowy. Jeśli granice grup powierzchni są już złagodzone lub wygładzone, wyłącz tę opcję.
* `Złagodź` (suwak) - Suwak-skrót do łagodzenia granic grup powierzchni.
* `Twarde krawędzie` - Włącza próbę zachowania twardych krawędzi.
* `Reprojekcja wierzchołka` - Włącza rzutowanie nowego układu z powrotem na siatkę wejściową.
* `Sym` - Włącza symetryczny wynik. Pamiętaj, że symetria jest zawsze liczona względem osi X świata, więc jeśli oczekujesz symetrycznego wyniku, upewnij się, że model jest w początku układu.
* `...` - Okienko ustawień Quad Remeshera.

#### Menu ustawień Quad Remeshera {#quad-remesher-settings-menu}

Przycisk `...` na końcu górnego paska otwiera okienko z pozostałymi ustawieniami:

* `Adaptacyjna liczba czworoboków` - Włącza mniejsze czworokąty w miejscach o dużej krzywiźnie i większe w miejscach o małej.
* `Adaptacyjny rozmiar` - Ustala stopień adaptacji. 100% pozwala na maksymalne dopasowanie rozmiaru, a przy 0% czworokąty są jednolite.

::: tip

Przepis na dobrą przebudowę na czworokąty z minimalną liczbą artefaktów:

* Podziel siatkę na grupy powierzchni, aby wyznaczyć idealny przebieg czworokątów.
* Złagodź granice grup powierzchni, aby były gładkie.
* Uprość siatkę. Dzięki temu na krawędziach grup powierzchni nie będzie cienkich ani zniekształconych ścian. W ustawieniach upraszczania upewnij się, że grupy powierzchni są włączone. Wtedy krawędzie trójkątów będą dokładnie podążać za krawędziami grup powierzchni.

W opcjach przebudowy upewnij się, że łagodzenie jest wyłączone (bo siatka jest już złagodzona), a powinieneś uzyskać dobre wyniki.

:::

### ![](/icons/tool_select.webp) Wybierz {#select}
Użyj trybów kształtu (`Lasso`, `Prostokąt`, `Elipsa`), aby zaznaczać obiekty w scenie. `Anuluj zaznaczenie` usuwa obiekty z zaznaczenia.

### ![](/icons/tool_lattice.webp) Krata {#lattice}
Odkształca obiekt za pomocą klatki punktów kontrolnych wokół niego, zamiast rzeźbić jego powierzchnię. Przesunięcie kilku punktów klatki płynnie wygina, skręca lub rozciąga cały obiekt, co świetnie sprawdza się przy poprawianiu proporcji albo pozowaniu bez ruszania topologii. Odkształcenie pozostaje edytowalne, dopóki go nie zatwierdzisz.

Lewy pasek narzędzi wybiera sposób edycji klatki:

* `Punkty` - Przeciągaj bezpośrednio punkty i krawędzie klatki. Stuknij punkt, aby go zaznaczyć.
* `Widok` - Poruszaj kamerą bez edytowania klatki.
* `Złagodź` - Pędzel, który łagodzi punkty klatki pod nim.
* `Elastyczne` - Pędzel, który ciągnie punkty klatki z elastycznym zanikaniem, jak narzędzie [Elastyczne](#elastic).
* `Gizmo` - Przesuwaj, obracaj i skaluj zaznaczone punkty za pomocą gizmo. Jego tryb alternatywny to `Pkt obrotu`.
* `Lasso` - Zaznaczaj punkty klatki lassem; `Anuluj zaznaczenie` usuwa je z zaznaczenia.

Okienko kształtów ma też `Miękki promień`, dzięki któremu przeciąganie punktu porusza także sąsiednie punkty (w komórkach siatki; 0 porusza tylko zaznaczenie), oraz `Odwróć wybór`.

Pasek u góry widoku zawiera:

* `Zatwierdź` - Stosuje odkształcenie do obiektu i usuwa klatkę.
* `Wyzeruj` - Usuwa klatkę i jej odkształcenie.
* `Krycie` - Krycie wyświetlanej klatki.
* `Strona lustrzana` - Przy symetrii przełącza, która lustrzana strona klatki jest pokazywana i może być wybierana, z osobnym `Krycie` dla ukrytej strony.
* `Punkty siatki` - Które punkty klatki można przesuwać: pełną siatkę, powierzchnię i punkt środkowy albo tylko powierzchnię.
* `Sztywność` - Jak sztywne jest odkształcenie, od gładkiego (0%) do sztywnego i liniowego (100%).
* `Zanikanie` - Jak daleko poza klatką słabnie odkształcenie.
* `Wyrównaj` - Wyrównuje klatkę do obiektu albo do świata.
* `X`, `Y`, `Z` `Podział` - Liczba komórek klatki na każdej osi. Przycisk trybu obok ustala, jak są ze sobą powiązane: `x = y = z` używa tej samej liczby na 3 osiach, `Jednolity` zachowuje ten sam odstęp między punktami na każdej osi, a `Niestandardowe` pozwala ustawić każdą oś dowolnie.

#### Ustawienia kraty {#lattice-settings}
* `Szybkość obrotu` - Te same opcje obrotu co w narzędziu [Przenieś](#move-settings), używane przy przeciąganiu punktów klatki.

### ![](/icons/tool_view.webp) Wyświetl {#view}
To „narzędzie” nie robi nic szczególnego: to po prostu sposób na oglądanie modelu bez zmieniania sceny.

#### Ustawienia narzędzia Wyświetl {#view-settings}
Gdy narzędzie Wyświetl jest aktywne, te ustawienia zastępują niektóre opcje wyświetlania, dzięki czemu uzyskasz czysty widok do prezentacji lub sprawdzania modelu:

* `Prymityw (Edytuj)`, `Powtarzacz (Edytuj)`, `Światło (Edytuj)`, `Kamera (Edytuj)` - Pozwalają edytować w widoku prymitywy, powtarzacze, światła i kamery, gdy aktywne jest narzędzie Wyświetl. Wyłącz je, aby nie przesunąć przypadkiem ich uchwytów.
* `Skrót kamery (zawsze)` - Zawsze pokazuje w widoku przyciski skrótów kamery.
* `Pokaż maskę`, `Kontur`, `Przyciemnij niezaznaczone obiekty` - Pokazuje maskę, kontur zaznaczonych obiektów lub przyciemnia niezaznaczone obiekty. `Auto` stosuje twoje zwykłe ustawienie, a `Nie` i `Tak` je wymuszają.
* `Pokaż linię (Symetria)`, `Pokaż płaszczyznę (Symetria)` - Pokazuje linię lub płaszczyznę symetrii, z tymi samymi opcjami `Auto`, `Nie` i `Tak`.
* `Ikona` - Pokazuje w widoku ikony grup, powtarzaczy, świateł, kamer oraz hierarchię, z tymi samymi opcjami.


## Menu kontekstowe przybornika {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Kliknięcie prawym przyciskiem lub przytrzymanie narzędzia w przyborniku otwiera menu kontekstowe. To menu ma następujące opcje:

* `Zapisz` - Zapisuje wszystkie zmiany wprowadzone w narzędziu.
* `Klonuj` - Powiela narzędzie jako nowy skrót narzędzia.
* `Ostatni zapis` - Przywraca poprzednio zapisaną wersję narzędzia.
* `Ikona` - Zmienia ikonę narzędzia. Gdy narzędzie ma własną ikonę, ten przycisk ją usuwa.
* `→ ...` - Przenosi narzędzie do innego folderu przybornika albo do nowego.
* `Wyzeruj` - Przywraca domyślne ustawienia narzędzia.

Sklonowane narzędzia mają też opcje `Zmień nazwę` i `Usuń`.
