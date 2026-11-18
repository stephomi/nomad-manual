# ![](/icons/brush.webp) Pociągnięcie {#stroke}

---
![](/images/stroke_overview.webp) 

## Przegląd {#overview}

Możesz dostosować zachowanie pociągnięcia dla większości pędzli narzędzi.
Ustawienia przypominają te z aplikacji do malowania 2d, ale niektóre opcje są typowe tylko dla rzeźbienia i 3d.

Opcje są podzielone na 5 podmenu:

| Nazwa     | Ikona                        | Opis                                                                     |
| :-------: | :--------------------------: | :----------------------------------------------------------------------: |
| Pociągnięcie | ![](/icons/brush.webp)    | Określa, jak pociągnięcie jest nakładane na model                        |
| Alfa      | ![](/icons/alpha.webp)      | Jak tekstura w skali szarości jest używana jako odcisk pędzla            |
| Zanikanie | ![](/icons/falloff.webp)    | Określa, jak siła pędzla zmienia się od środka do krawędzi               |
| Filtr     | ![](/icons/filter.webp)     | Jak geometria modelu wpływa na działanie pędzla                          |
| Nacisk    | ![](/icons/pressure.webp)   | Określa reakcję na nacisk rysika                                         |

::: tip
Nie wszystkie opcje pociągnięcia dotyczą każdego narzędzia. Opcje, których bieżące narzędzie nie używa, są wyłączone lub ukryte. 
:::


## ![](/icons/brush.webp) Pociągnięcie {#stroke-1}

### ![](/icons/radius.webp) Promień {#radius}

![](/images/stroke_radius.webp)

Opcje promienia są ustawieniami globalnymi: dotyczą wszystkich narzędzi.

#### Przestrzeń {#size}

* `Ekran` - promień jest ustawiany w jednostkach ekranu. Jeśli ustawisz promień na 100 pikseli, pozostanie on szeroki na 100 pikseli bez względu na to, czy przybliżasz, czy oddalasz widok.
* `Świat (3D)` - promień jest ustawiany w jednostkach 3d. Jeśli na przykład utworzysz kulę i ustawisz promień tak, by był tej samej wielkości co kula, promień pozostanie wielkości kuli podczas przybliżania i oddalania.

#### ![](/icons/link.webp) Synchronizuj skrót {#sync-shortcut}

Gdy ta opcja jest włączona, ustawienia promienia i sylwetki są synchronizowane po przełączeniu na pędzle skrótów (`Gładkie`, `Maska` lub `Ukryj`). Dzięki temu szybkie wygładzanie czy maskowanie odbywa się pędzlem tej samej wielkości co narzędzie, którego właśnie używasz.

#### ![](/icons/link.webp) Udostępnij promień {#share-radius}

Gdy ta opcja jest włączona, wszystkie narzędzia używają tego samego promienia. Domyślnie każde narzędzie ma własny promień.


### Typ pociągnięcia {#stroke-type}

![](/images/stroke_strokemode.webp)

Pociągnięcia mogą działać w kilku trybach:

### ![](/icons/stroke_dot.webp) Kropka {#dot}
Przeciągasz jak zwykłym pociągnięciem pędzla. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roluj {#roll}
Alfa pędzla obraca się zgodnie z kierunkiem pociągnięcia. Przydaje się do tworzenia szwów na tkaninie. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Blokada + promień {#lock-radius}
Odciska pociągnięcie o stałej **_wysokości_**. Przeciąganie ustawia skalę i obrót.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Blokada + intensywność {#lock-intensity}
Odciska pociągnięcie o stałym **_promieniu_**. Przeciąganie ustawia wysokość i obrót.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Tryby `Blokada + promień` i `Blokada + intensywność` ignorują ustawienia [Nacisku](#pressure), ponieważ rozmiar i siłę ustala już samo przeciąganie.
:::

![](/images/stroke_strokemodemove.webp)

Narzędzia `Przenieś` i `Przeciągnij` mają własne 3 opcje:

### ![](/icons/snake.webp) Przeciągnij {#drag}

Przez cały czas pociągnięcia aktualizuje to, co znajduje się w promieniu pędzla. Szybkie pociągnięcie zostawi powierzchnię w tyle, a wolne będzie trzymać materiał, tworząc dłuższe kształty. To domyślny tryb narzędzia `Przeciągnij`. Z `Topologią dynamiczną` możesz w ten sposób tworzyć wężowate wyciągnięcia. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Przechwyć {#grab}
Na początku pociągnięcia zaznacza to, co znajduje się w promieniu pędzla, i trzyma to zaznaczenie do końca. Przydaje się do precyzyjniejszego przesuwania: możesz starannie dobrać odległość przesunięcia i nie ruszysz przypadkiem więcej, niż początkowo zaznaczyłeś. To domyślny tryb narzędzia `Przenieś`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Blokada + promień (przeciąganie) {#lock-radius-drag}
Promień ustawiony przez użytkownika jest ignorowany i zmienia się dynamicznie w zależności od tego, jak daleko od punktu początkowego przeciągniesz pociągnięcie. Mała odległość = mały promień, większa odległość = większy promień. Suwakiem intensywności sterujesz kształtem zanikania. Przydaje się do szkicowania organicznych, gumowatych kształtów.
![](/videos/stroke_lockradius_drag.mp4) 

Niektóre inne narzędzia wyświetlają tu własne typy pociągnięć, na przykład `Złagodź`, `Gładkie` i `Smużenie` w narzędziach do wygładzania, albo kształty takie jak `Lasso` i `Krzywa` w narzędziach opartych na zaznaczeniu. Opisano je przy każdym [narzędziu](tools.md).


### Dostosuj intensywność odstępów {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Pociągnięcia o małym odstępie (poniżej 50%) szybko się kumulują, przez co są intensywniejsze niż te o większym odstępie. Ten przełącznik to kompensuje, więc pociągnięcia mają mniej więcej tę samą intensywność bez względu na odstęp.

### Odstęp pociągnięć {#stroke-spacing}
Jak daleko od siebie nakładane są kolejne odciski pędzla podczas przeciągania. Wartości poniżej 100% nakładają się na siebie, dając wrażenie ciągłego pociągnięcia. Wartości powyżej 100% zaczynają zostawiać przerwy, co przydaje się do rzeźbienia detali takich jak szwy czy zamki błyskawiczne.

### Stabilizator powolnej liny {#lazy-rope-stabilizer}
Pociągnięcie podąża za wskaźnikiem z pewnym opóźnieniem, w stałej odległości. Pozwala to rysować gładkie linie.
![](/videos/stroke_lazy_rope.mp4) 

### Wygładzanie pociągnięć {#stroke-smoothing}
Uśrednia kilka kolejnych pozycji wskaźnika, aby pociągnięcie było gładsze.
Przy wysokich wartościach pociągnięcie zostaje w tyle za wskaźnikiem, ale w końcu go dogania.
Przydaje się do rysowania gładkich linii.

### Promień przyciągania {#snap-radius}
Przyciąga pociągnięcie do poprzedniego, gdy wskaźnik startuje blisko miejsca, w którym ostatnie pociągnięcie się skończyło. Promień określa, jak daleko szukać końca poprzedniego pociągnięcia. Przydaje się przy rysowaniu długich, ciągłych linii z częstymi przerwami.

### ![](/icons/trail.webp) Ślad pociągnięcia pędzla {#trail}

Gdy ta opcja jest włączona, każdy nowy odcisk ponownie nakłada też ostatnie punkty pociągnięcia znajdujące się za nim. `Liczba śladów` ustala, ile punktów jest nakładanych ponownie, `Intensywność śladu` – jak mocno, a `Promień śladu` – o ile się powiększają.

Ślad działa tylko z typem pociągnięcia `Kropka` i nie działa z [wpływem zanikania](#influence) `Grzbiet`.

### ![](/icons/silhouette.webp) Sylwetka {#silhouette}
![](/images/stroke_silhouette.webp)
Domyślnie pociągnięcia działają tylko na powierzchnię modelu w promieniu pędzla. Gdy sylwetka jest włączona, pociągnięcie jest rzutowane przez cały model. Bardzo się to przydaje przy wstępnym szkicowaniu bryły modelu albo przy kształtach, których boki mają pozostać prostopadłe.

Kierunek rzutowania możesz ustawić wprost:

* `X`, `Y`, `Z` - rzutowanie wzdłuż stałej osi.
* `Wyświetl` - rzutowanie wzdłuż kierunku kamery.
* `Jeśli przyciągnięte` - rzutowanie wzdłuż kierunku kamery, ale tylko wtedy, gdy kamera jest przyciągnięta do widoku. W przeciwnym razie pociągnięcie pozostaje zwykłym pociągnięciem.
* `Najbliższe` - rzutowanie wzdłuż osi najbliższej kierunkowi kamery. To ustawienie domyślne.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Zrandomizuj {#randomize}

![](/images/stroke_randomize.webp)

`Intensywność`, `Przesunięcie`, `Obrót` i `Skala` pociągnięcia mogą być losowane niezależnie. Pole wyboru w danym wierszu włącza lub wyłącza losowanie. Daje to wiele efektów: na przykład losowanie z narzędziem do malowania tworzy cętkowany kolor, a z narzędziem do bruzd pozwala uzyskać detale skóry.

`Okres (wolniej)` ustala długość cyklu losowania: zwiększ go, by uzyskać powolne, płynne zmiany, zmniejsz, by uzyskać szybki szum. Mały przycisk obok każdego wiersza skaluje okres tylko dla tego wiersza.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Zrandomizuj - HSV {#randomize-hsv}

W narzędziach, które malują, losować można też `Odcień`, `Nasycenie` i `Wartość` koloru farby, z osobnym okresem. Świetnie sprawdza się to przy dodawaniu subtelnych zmian koloru skóry czy kamienia.

### Przesunięcie pociągnięć {#stroke-offset}

Nakłada stałe przesunięcie na pociągnięcie, żeby palec go nie zasłaniał. Przydaje się na małych ekranach. To ustawienie globalne: włączasz je polem wyboru i dotyczy wszystkich narzędzi.


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

`Alfa` to tekstura, która moduluje działanie pędzla.
To obraz w skali szarości, w którym czarne piksele oznaczają brak deformacji, a białe pełną deformację.

Kliknij obraz alfy, aby go zmienić. Oprócz wbudowanych alf i tych, które sam zaimportujesz, lista alf pozwala też pobrać mapy przemieszczeń z Poly Haven.

Kliknij podgląd materiału, aby wczytać alfę z ustawienia wstępnego materiału. Możesz tu też zapisywać ustawienia wstępne materiałów i zdecydować, czy tekstury mają być osadzone razem z narzędziem.

::: tip
Tekstura nigdy nie jest skalowana, więc duże tekstury mogą spowolnić działanie.
:::

### ![](/icons/blend_contrast.webp) Popraw alfę {#invert-pixels}
Przycisk `Popraw...` przy zaimportowanej alfie otwiera okienko, które poprawia sam obraz: jego średnią wartość, odwrócenie pikseli (czarny staje się biały, a biały czarny), obrót o 90° oraz odbicie w poziomie lub w pionie. Plik obrazu jest zapisywany na nowo, więc inne aplikacje też widzą poprawiony obraz.

::: tip

Wbudowanych alf dostarczanych z Nomad nie można poprawiać.

:::

### Projekcja {#projection}

Sposób rzutowania alfy na model:

* `Powierzchnia` - alfa leży na powierzchni pod pędzlem i dopasowuje się do jej orientacji.
* `Ekran` - alfa jest rzutowana prosto z widoku.
* `Kafelkowanie` - alfa jest rzutowana z widoku i zostaje w miejscu, gdy malujesz po niej, jak szablon, dzięki czemu powtarzający się wzór łączy się bez szwów. Obrót jest zablokowany, a nacisk rysika nie zmienia rozmiaru wzoru.
* `Trzypłaszczyznowy` - alfa jest rzutowana wzdłuż 3 osi. Opcje skalowania, obrotu i rozmieszczenia opisane niżej zostają zastąpione ustawieniami tekstury trzypłaszczyznowej.

### ![](/icons/diagonal.webp) Skalowanie {#scaling}

Pędzel w Nomad to okrąg o promieniu ustawionym przez użytkownika. Tekstury są często kwadratowe lub prostokątne, a parametry `Skalowanie` pozwalają zdecydować, jak tekstura ma się zmieścić w okręgu. Dla kwadratowej tekstury wartość 0.7 zmieści ją wewnątrz okręgu. Wartość 1 powiększy teksturę tak, by to okrąg zmieścił się w niej, a jej krawędzie zostaną przycięte.

![](/images/alpha_scaling.webp) 

Włączenie `Skalowanie Y` pozwala rozciągnąć alfę w pionie. Pierwszy suwak staje się wtedy `Skalowanie X`.

![](/images/alpha_scaling_y.webp) 

`Odwróć poziomo` odbija alfę z lewej na prawą.

### Obrót {#rotation}

Tekstura alfy obraca się zgodnie z kierunkiem pociągnięcia. Możesz dodać przesunięcie obrotu, a jeśli ikona kłódki jest włączona, tekstura pozostanie zablokowana w tym obrocie względem ekranu.

Przycisk z piórem obok obraca alfę, gdy obracasz rysik wokół własnej osi (barrel roll), przy pociągnięciach `Blokada + promień` i `Blokada + intensywność`, o ile obrót nie jest zablokowany. Działa to tylko z rysikami, które to obsługują.

### Rozmieszczenie sąsiadująco {#tiling}
![](/images/stroke_tiling.webp) 

Jak często tekstura powtarza się w profilu pędzla. Tryby `Rozmieszczenie sąsiadująco - X` i `Rozmieszczenie sąsiadująco - Y` pozwalają ograniczyć się do jednej tekstury w pociągnięciu (`Brak`), powtarzać teksturę (`Powtarzanie`) albo odbijać co drugą teksturę, by tworzyć wzory lub ułatwić uzyskanie tekstur bez szwów (`Odbicie lustrzane`). Są dostępne z pociągnięciem `Roluj`, projekcją `Kafelkowanie` lub `Rozmieszczenie sąsiadująco` większym niż 1.

`Dopasuj do wewnątrz` ma znaczenie tylko dla niekwadratowych alf i tekstur pędzla. Gdy jest włączone, każdy obraz jest powielany osobno, bez odstępów. Wyłącz je, by alfa i pozostałe obrazy pozostały zsynchronizowane, gdy mają różne proporcje.

![](/videos/alpha_tiling.mp4) 



### Średnia wartość {#mid-value}

Domyślnie czarne piksele oznaczają brak deformacji, a białe pełną deformację na zewnątrz. Na przykład pędzel typu glina z alfą przedstawiającą skały wyciągnie powierzchnię tylko tam, gdzie alfa nie jest czarna.

Jeśli chcesz, żeby pędzel wciskał powierzchnię albo jednocześnie wciskał I wyciągał, zmień średnią wartość. Gdy ustawisz ją na 0.5, średnia szarość w alfie nic nie zrobi, czerń wciśnie powierzchnię, a biel ją wyciągnie.

Dwa przyciski pomagają znaleźć właściwą wartość: kwadratowy przycisk odczytuje średnią wartość z obrzeża obrazu, a próbnik pozwala wskazać ją bezpośrednio na alfie.




## ![](/icons/falloff.webp) Zanikanie {#falloff}

![](/images/falloff_menu.webp) 

Działa podobnie do [Alfy](#alpha), z tą różnicą, że intensywnością sterujesz jedną krzywą. Zanikanie łączy się z alfą, więc możesz użyć tekstury do detali, a zanikania do kontroli wygaszania na krawędziach i intensywności w środku narzędzia.

Gdy krzywa jest na górze, deformacja jest pełna, a gdy jest na dole, pędzel nic nie robi.

Krzywą możesz traktować jak przekrój przez czubek pędzla. Dolna część pokazuje podgląd tego, jak pojedynczy „odcisk” pędzla wyglądałby na powierzchni modelu. Jeśli pędzel ma teksturę alfy, ona również jest tam widoczna, więc od razu widać, jak zanikanie i alfa ze sobą współgrają.

### ![](/icons/fx.webp) Ustawienie wstępne {#preset}
Gdy wybrane jest `Ustawienie wstępne...`, kliknięcie wykresu krzywej otwiera menu gotowych ustawień. Zaokrąglone krzywe dają miękkie efekty, a kanciaste ostrzejsze. Przycisk `Odejmij` na lewym pasku narzędzi w praktyce odwraca zanikanie: szczyt krzywej wciska powierzchnię zamiast ją wyciągać i na odwrót.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Po wybraniu tej opcji możesz rysować własne krzywe zanikania. Edytor krzywych działa tak samo jak krzywe w pozostałych częściach Nomad:

* Kliknij krzywą, aby utworzyć nowy punkt
* Przeciągnij punkt, aby zmienić jego położenie
* Kliknij punkt, aby przełączyć go między ostrym a gładkim
* Przeciągnij punkt na sąsiedni, aby go usunąć

### ![](/icons/curve_bspline.webp) B-splajn {#b-spline}
Po wybraniu tej opcji możesz rysować własne krzywe zanikania. Edytor działa tak samo jak Catmull-Rom, ale punkty wpływają na krzywą, zamiast leżeć bezpośrednio na niej, co ułatwia uzyskanie gładszych kształtów.

### ![](/icons/curve_bevel.webp) Faza {#bevel}
Punkty są połączone prostymi odcinkami z zaokrąglonymi narożnikami, których wielkość zależy od ostrości każdego punktu. Przydaje się do pędzli z płaskim wierzchem i czystą fazą na krawędzi.

Edytor krzywych ma 3 przyciski:

| Element   | Ikona                       | Opis                                              |
| :-------: | :-------------------------: | :-----------------------------------------------: |
| Maksymalizuj | ![](/icons/maximize.webp) | Powiększa edytor krzywych                         |
| Wyzeruj   | ![](/icons/reset.webp)     | Przywraca krzywą do stanu domyślnego              |
| Symetria  | ![](/icons/symmetric.webp) | Wyświetla krzywą jako symetryczny „czubek pędzla” |


### Wpływ {#influence}

* `Kula` (3d) - wpływ jest obliczany na podstawie odległości wierzchołka od środka pędzla.
* `Okrąg` (2d) - wierzchołek jest najpierw rzutowany na płaszczyznę obszaru, a dopiero potem mierzona jest jego odległość od środka pędzla. Podobnie próbkowane są alfy. 
* `Walec` - wpływ jest rzutowany przez obszar w kształcie walca. Działa to tak samo jak włączenie opisanej niżej [Sylwetki](#silhouette-1).
* `Grzbiet` - zanikanie jest mierzone w poprzek pociągnięcia, więc krzywa staje się przekrojem całego pociągnięcia. Przycisk `Sym` odbija wtedy profil w poprzek pociągnięcia: edytujesz jedną stronę, a druga podąża za nią. Gdy jest wyłączony, krzywa biegnie od lewej strony pociągnięcia do prawej. Niedostępne dla narzędzi opartych na spłaszczaniu.

### ![](/icons/silhouette.webp) Sylwetka {#silhouette-1}
Domyślnie pociągnięcia działają tylko na powierzchnię modelu w promieniu pędzla. Gdy sylwetka jest włączona, pociągnięcie jest rzutowane przez cały model. Bardzo się to przydaje przy wstępnym szkicowaniu bryły modelu albo przy kształtach, których boki mają pozostać prostopadłe. Ma te same opcje rzutowania co [Sylwetka](#silhouette) w zakładce Pociągnięcie.



## ![](/icons/filter.webp) Filtr {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Akumulacja pociągnięć {#accumulate-stroke}
Znosi limit tego, ile materiału można dodać lub usunąć w jednym pociągnięciu. Na przykład narzędzie `Glina` ma tę opcję włączoną, więc materiał może się nadbudowywać, a narzędzie `Pędzel` ma ją wyłączoną, więc pociągnięcie przestaje dodawać materiał, jeśli wciąż przesuwasz je po tym samym fragmencie siatki. 

### ![](/icons/culling.webp) Tylko przednie wierzchołki {#front-facing-vertex-only}
Ta opcja ignoruje wierzchołki zwrócone tyłem.
Przydaje się, gdy chcesz malować fragment cienkiej geometrii bez wpływu na jej drugą stronę.
Działa też przy rzeźbieniu, ale mogą pojawić się artefakty.

### ![](/icons/eye_open.webp) Tylko widoczne wierzchołki {#visible-vertex-only}
Ignoruje wierzchołki zasłonięte przez inne powierzchnie, patrząc z kamery. Opcja pojawia się przy pociągnięciach kształtem (lasso, prostokąt...) w narzędziach do maskowania i malowania oraz w narzędziach `Grupa powierzchni` i `Ukryj`.

### ![](/icons/dynamic.webp) Zezwól na topologię dynamiczną {#allow-dynamic-topology}
Ta opcja jest dostępna tylko wtedy, gdy siatka jest w trybie [Topologii dynamicznej](topology.md#dynamic-topology). Możesz włączać lub wyłączać topologię dynamiczną osobno dla każdego narzędzia.

### ![](/icons/connect.webp) Połączona topologia {#connected-topology}
Rzeźbi tylko wierzchołki połączone z powierzchnią, której dotykasz narzędziem. Na przykład z narzędziem `Przenieś` pozwala przesunąć część modelu, nawet jeśli przenika się ona z inną częścią.
![](/videos/connected_topology.mp4)

### Chroń obszar {#protect-area}
![](/images/filter_protect_area.webp) 

Te opcje chronią fragmenty siatki przed działaniem narzędzi w różnych sytuacjach. Każdą z nich można ustawić na `Auto`, `Nie` lub `Tak`, a mała strzałka pokazuje, czemu odpowiada w tej chwili `Auto`.

* `Ukryj` - czy części siatki ukryte narzędziem do ukrywania mają być chronione. Przy `Auto` ukryte powierzchnie są chronione, chyba że widać ich szkielet (zobacz ustawienia [Szkielet](settings.md#wireframe)).
* `Maska` - czy zamaskowane części siatki mają być chronione. Przy `Auto` zamaskowane części są chronione, dopóki maska jest widoczna w menu [Cieniowanie](shading).
* `Grupa powierzchni` - czy narzędzie ma działać tylko w obrębie pierwszej dotkniętej grupy powierzchni. Przy `Auto` zależy to od tego, czy grupy powierzchni są widoczne w menu [Cieniowanie](shading).

Przycisk `(All)` określa, czy te zabezpieczenia są globalne, wspólne dla wszystkich narzędzi, czy ustawiane osobno dla każdego narzędzia.


### Próbkowanie obszaru {#area-sampling}
Niektóre pędzle lub opcje pociągnięcia potrzebują do działania normalnej i położenia płaszczyzny względem powierzchni.

Możesz określić, jak ta uśredniona płaszczyzna jest obliczana, ustawiając obszar próbkowania jako ułamek promienia narzędzia.

Przy 100% brany jest pod uwagę każdy punkt wewnątrz okręgu zaznaczenia.

Przy 0% brany jest pod uwagę tylko najbliższy wierzchołek lub trójkąt. Wartości `Promień normalny` i `Promień pozycji` mogą być ze sobą powiązane albo odblokowane i ustawiane niezależnie.

### Filtr normalnych obszaru {#keep-sharp-edges}
Wyklucza punkty, których normalne zbyt mocno odbiegają od normalnej powierzchni.

Zmienia to sposób obliczania płaszczyzny obszaru (próbkowanie obszaru), więc najbardziej przydaje się w narzędziach typu glina lub opartych na spłaszczaniu, albo gdy chcesz pokolorować w miarę płaską powierzchnię, nie wychodząc poza nią.

Kąty `Min.` i `Max.` sterują przejściem między punktami wykluczonymi a w pełni objętymi działaniem, co pokazuje mały kolorowy krążek obok nich.

![](/videos/filter_keep_sharp_edges.mp4)

### Filtr normalnych wygaszania {#falloff-normal-filter}
Podobnie jak [Filtr normalnych obszaru](#keep-sharp-edges) wyklucza punkty, których normalne zbyt mocno odbiegają od normalnej powierzchni, ale działa na zanikanie pędzla, a nie na obliczanie płaszczyzny. Przydaje się do malowania zagłębień lub wypukłości.


### Maskowanie głębokości {#depth-masking}
![](/images/stroke_depthmask.webp)

Wyklucza punkty, które leżą powyżej lub poniżej pewnej odległości od obliczonej płaszczyzny (próbkowanie obszaru).

Dzięki temu możesz malować tylko na wypukłych fragmentach albo tylko we wgłębieniach.

Wykres przedstawia przekrój powierzchni: pozioma linia to miejsce, w którym leży powierzchnia, a okrąg to promień zanikania farby powyżej i poniżej powierzchni. `Przesunięcie wysokości` to procent powyżej lub poniżej powierzchni, od którego zaczyna się obliczanie maskowania. Gdy włączone jest `Zanikanie głębokości`, suwaki `Górny obszar` i `Dolny obszar` pozwalają skalować zanikanie powyżej i poniżej punktu przesunięcia.

#### Przykład: malowanie we wgłębieniach {#example-paint-in-cavities}
Aby malować tylko we wgłębieniach, ustaw przesunięcie wysokości na -100% i przesuń suwak górnego obszaru tak, by okrąg oddalił się od poziomej linii. Pierwsze kliknięcie ustala wtedy „zerową” głębokość, a działanie obejmuje tylko obszary leżące poniżej niej.

![](/videos/stroke_depth_cavity.mp4)

#### Przykład: malowanie na wypukłościach {#example-paint-on-bumps}
Aby malować tylko wysoko położone obszary, ustaw przesunięcie wysokości na +90%, tak by dół okręgu odrobinę przecinał poziomą linię. Kliknięcie na szczycie „wysokiego” obszaru ustala głębokość, więc pomalowane zostanie wszystko na tej głębokości, trochę poniżej niej i wszystko, co leży wyżej. Głębokie wgłębienia zostaną pominięte.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Nacisk {#pressure}
![](/images/pressure_menu.webp) 

Określa, jak nacisk rysika wpływa na pędzle.

### Użyj ustawień globalnych {#use-global-settings}

Domyślnie opcja `Użyj ustawień globalnych` jest włączona, co oznacza, że wszystkie pędzle mają te same wartości nacisku. Odznacz ją, aby bieżące narzędzie miało własne ustawienia nacisku.

### ![](/icons/radius.webp) Promień {#pressure-radius}

Ta krzywa określa, jak nacisk wpływa na promień pędzla. Domyślnie zależność jest liniowa, więc jeśli Twój rysik reaguje płynnie, zmiana promienia też powinna być płynna. Wiele rysików ma jednak nieliniową reakcję, którą możesz skompensować tą krzywą. Jeśli na przykład masz wrażenie, że przy mocnym nacisku promień nie osiąga maksimum, wybierz ustawienie wstępne krzywej, takie jak „out-pow3”, wygięte ku górze, aby promień rósł szybciej.

To okno działa podobnie jak wykres krzywej zanikania: możesz wybrać ustawienie wstępne, stukając w okno krzywej, albo narysować własne krzywe w trybach `Catmull-Rom`, `B-splajn` i `Faza`.

Jeśli chcesz mieć stały promień, wyłącz tę sekcję.

### ![](/icons/intensity.webp) Intensywność {#pressure-intensity}

Działa podobnie jak krzywa promienia, ale steruje intensywnością. Jeśli chcesz mieć stałą intensywność, wyłącz tę sekcję.

### Ogranicz ciśnienie do 100% {#limit-pressure}

Pilnuje, by nacisk rysika nigdy nie przekroczył 100%. To ustawienie globalne.

### Wygładzanie nacisku {#pressure-smoothing}

Uśrednia odczyty nacisku rysika, by uzyskać płynniejsze efekty.
