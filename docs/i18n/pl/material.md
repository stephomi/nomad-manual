# ![](/icons/material.webp) Materiał {#material}

To menu pozwala zmienić materiał bieżącego obiektu, właściwości renderowania obiektu i materiału oraz przypisać materiałowi tekstury.

![](/images/material_overview.webp)

Materiały określają wygląd obiektu, sterując tym, jak reaguje on na światło i na inne obiekty. Za wygląd obiektu odpowiadają te właściwości:

* `Typ materiału`
* `Kolor`
* `Chropowatość`
* `Metaliczność`
* `Krycie`
* `Refleksyjność`
* `Emisyjne/nieoświetlone`

Łącząc te właściwości, uzyskasz bardzo różne efekty: od fotorealistycznych, przez kreskówkowe, po eksperymentalne.

Kolor, chropowatość, metaliczność i krycie można malować, więcej informacji znajdziesz w [opcjach malowania wierzchołków](painting.md).

Typ materiału, refleksyjność i emisyjność/brak oświetlenia to właściwości materiału opisane poniżej.

Przyciski `Kopiuj` i `Wklej` u góry tego menu pozwalają kopiować materiały z jednego obiektu na drugi.

Pamiętaj, że renderer Nomad działa w czasie rzeczywistym: choć ma duże możliwości, w przypadku niektórych efektów stawia szybkość ponad dokładność.

## Typy materiałów {#material-types}

![](/images/material_types.webp)

Typy materiałów w Nomad to: Nieprzezroczysty, Podpowierzchnia, Mieszanie, Addytywny, Refrakcja, Dithering i Łapacz cienia.

### ![](/icons/material_opaque.webp) Nieprzezroczysty {#opaque}
Tryb domyślny, który traktuje powierzchnie jak prosty materiał obsługujący malowany kolor, chropowatość, metaliczność i krycie. Malowane krycie, tekstura krycia lub kanał alfa tekstury koloru nadal sprawiają, że obiekt jest prześwitujący, przy użyciu ditheringu. Ignorowany jest tylko główny suwak krycia.

### ![](/icons/material_subsurface.webp) Podpowierzchnia {#subsurface}
Ten tryb symuluje materiały, w których światło rozmywa się i rozprasza wewnątrz, takie jak skóra, wosk czy jadeit.

Wymaga trybu cieniowania PBR. Aby uzyskać najlepszy efekt, użyj co najmniej jednego światła kierunkowego lub reflektora, najlepiej przy przyciemnionym otoczeniu.

Próbka koloru ustawia kolor rozproszonego światła.

`Głębia` określa, jak daleko światło rozprasza się od przodu pod powierzchnię i z powrotem na zewnątrz przez przednią powierzchnię. Zmiękcza to ostre cienie i rozmywa szczegóły powierzchni.

`Translucencja` określa, jak światło rozprasza się od przodu do tyłu kształtu, jak przy prześwitywaniu przez spód liścia albo przez uszy mocno oświetlone od tyłu. Aby to zobaczyć, potrzebujesz światła rzucającego cienie.

### ![](/icons/material_blending.webp) Mieszanie {#blending}

Podobny do trybu Nieprzezroczysty, ale obsługuje suwak krycia, dzięki któremu materiał może przechodzić od pełnego do przezroczystego. To prosty pojedynczy suwak krycia, w odróżnieniu od malowanego krycia obsługiwanego przez materiał nieprzezroczysty.

::: warning
Tryb mieszania może powodować migotanie i przeskoki przy złożonych lub przecinających się kształtach.
:::

### ![](/icons/material_additive.webp) Addytywny {#additive}
Ten materiał pozwala uczynić siatkę półprzezroczystą. Jest podobny do materiału mieszania, ale o ile mieszanie łączy się z otoczeniem, o tyle materiał addytywny jest zawsze jaśniejszy od obiektów za nim, co sprawdza się przy jasnych efektach, takich jak promienie światła, ogień czy eksplozje.

Możesz ustawić krycie większe niż 1, co oznacza, że obiekt będzie jaśniejszy.  
Przydaje się to, jeśli chcesz użyć efektu [bloom](postprocess.md#bloom) i `parametru progu`, aby tylko ten obiekt świecił jak obiekt emisyjny.

Ten tryb zwykle daje mniej artefaktów niż [Mieszanie](#blending) (przezroczystość niezależna od kolejności).

### ![](/icons/material_refraction.webp) Refrakcja {#refraction}
Tego trybu możesz użyć do symulowania szkła. Wymaga trybu cieniowania PBR. Ze względu na ograniczenia renderowania w czasie rzeczywistym refrakcja obiektu w sobie samym i refrakcja wielowarstwowa są dość ograniczone.

Malowana chropowatość modelu wpływa na to, jak bardzo rozmyta jest refrakcja.
Domyślnie każdy obiekt utworzony w Nomad ma chropowatość około 25%, więc refrakcja nie będzie idealna, tylko lekko rozmyta.
Przyciskiem `Malowanie błyszczące` możesz przemalować model z chropowatością i metalicznością równymi 0 (kolory pozostaną bez zmian).

W grę wchodzą 2 różne chropowatości: jedna określa, jak rozmyte jest odbicie na powierzchni, a druga steruje wnętrzem (refrakcją).  
Ponieważ jednak Nomad ma tylko jeden malowany kanał chropowatości, chropowatość wnętrza i powierzchni ma tę samą wartość.  
Aby uzyskać różne wartości (na przykład lizak o gładkiej powierzchni, ale rozmytym wnętrzu), użyj suwaków `Powierzchni` i `Wnętrza` w sekcji `Nadpisz chropowatość`, aby zastąpić malowaną chropowatość.

![](/videos/refraction.mp4)

#### Indeks refrakcji {#index-of-refraction}
Jak bardzo światło się załamuje, gdy wchodzi do obiektu. Wyższe wartości załamują je mocniej, jak gruba soczewka.

#### Pochłanianie {#absorption}
Symuluje pochłanianie światła podczas przechodzenia przez objętość, zabarwione kolorem próbki, a `Współczynnik` ustawia siłę efektu. Cienkie części są jaśniejsze, bo przepuszczają więcej światła, a grube obszary są ciemniejsze. Używane jest tylko przybliżenie grubości obiektu, więc efekt w dużym stopniu zależy od kształtu.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Sprawia, że obiekt jest półprzezroczysty, losowo pomijając część pikseli.

### ![](/icons/material_shadow_catcher.webp) Łapacz cienia {#shadow-catcher}

Sprawia, że obiekt jest niewidoczny i tylko przyjmuje cienie od świateł. Przydaje się do łączenia renderów z Nomad z innymi obrazami, zwykle na płaszczyźnie. Próbka koloru ustawia kolor cienia.

W scenie musi być światło rzucające cienie, w przeciwnym razie łapacz cienia nic nie robi. Przyciski `Metaliczność → 0%` i `Metaliczność → 100%` przemalowują obiekt: w pełni metaliczny łapacz cienia może też odbijać scenę, gdy włączony jest efekt postprocessingu [Odbicie (SSR)](postprocess.md#reflection-ssr).

::: tip

Więcej informacji o przezroczystości i trybach mieszania znajdziesz na stronie https://support.fab.com/s/article/Transparency-Opacity

:::

## Ustawienia {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Zawsze nieoświetlone {#always-unlit}
Jeśli ta opcja jest włączona, obiekt ignoruje PBR i MatCap i po prostu wyświetla swój malowany kolor bez cieniowania.
Jeśli używasz trybu [Addytywny](#additive), możesz malować przezroczystość bezpośrednio czarnym kolorem.

### Krycie {#opacity}
Jak pełny, czyli nieprzezroczysty, wydaje się obiekt: 100% to pełny obiekt, 0% to przezroczysty. Suwak jest wyświetlany dla typów Mieszanie, Addytywny, Dithering i Łapacz cienia. Krycie możesz też malować, aby mieć nad nim większą kontrolę.

### Przebieg prerefrakcji {#pre-refract-pass}
Tylko Mieszanie i Addytywny. Rysuje ten przezroczysty obiekt przed przebiegiem refrakcji. Przydaje się, gdy obiekt refrakcyjny znajduje się przed innymi przezroczystymi powierzchniami.

### Refleksyjność {#reflectance}
Określa ilość odbić, jakie otrzymuje materiał niemetaliczny. Zwykle należy używać wartości domyślnej (odpowiadającej standardowym 4% światła odbitego przy kącie prostopadłym), ale możesz ją zwiększyć, na przykład aby wzmocnić odbicia i rozbłyski w oczach postaci. Wymaga trybu cieniowania PBR.

### ![](/icons/culling.webp) Ignorowanie odwróconych {#inverse-culling}
Odwraca normalne powierzchni. Zwykle nie jest to potrzebne, ale przydaje się, gdy model wygląda na wywrócony na lewą stronę, a w połączeniu z wyłączoną opcją `Dwustronny` pozwala tworzyć wnętrza, w których ściana najbliższa kamerze jest zawsze ukryta.

Poniższe opcje można ustawić na `Auto`, `Nie` lub `Tak`. Przy `Auto` strzałka pokazuje wartość, która jest faktycznie używana.

### ![](/icons/sphere_smooth.webp) Płynne cieniowanie {#smooth-shading}
Zobacz [opcję globalną](settings.md#smooth-shading).  
Wartość `Auto` używa opcji globalnej.

### ![](/icons/culling.webp) Dwustronny {#two-sided}
Ścianki są widoczne z obu stron. Zobacz [opcję globalną](settings.md#two-sided-quick).  
Wartość `Auto` używa opcji globalnej.

### ![](/icons/culling.webp) Kolorowa powierzchnia tylna {#coloured-backface}
Zobacz [opcję globalną](settings.md#two-sided-quick).
Wartość `Auto` używa opcji globalnej.

### ![](/icons/shadow_cast.webp) Rzucanie cieni {#casts-shadows}
Przezroczyste obiekty również rzucają cienie (we wzorze ditheringu, który naśladuje mieszane cienie).  
Pamiętaj, aby wyłączyć rzucanie cieni, jeśli w scenie jest duży obiekt, który nie musi ich rzucać (na przykład duża podłoga).

### ![](/icons/shadow_receive.webp) Przyjmowanie cieni {#recieve-shadows}
Czy cienie innych obiektów są rysowane na tym obiekcie.

### ![](/icons/wireframe.webp) Szkielet {#wireframe}
Zobacz [opcję globalną](settings.md#wireframe).  
Wartość `Auto` używa opcji globalnej.

### ![](/icons/trash.webp) Resetuj normalne {#reset-normals}
Wyświetlana tylko wtedy, gdy importowany obiekt ma własne normalne (na przykład przy imporcie z opcją `Zachowaj topologię`). Usuwa je, więc cieniowanie korzysta z normalnych obliczonych na podstawie powierzchni.


## Tekstury {#textures}

![](/images/material_textures.webp)

Jeśli obiekt ma UV, do materiału możesz przypisać tekstury, oprócz koloru, chropowatości, metaliczności i krycia wierzchołków. Zwykle są one wynikiem wypalania tekstur, ale możesz też użyć obrazów utworzonych poza Nomad. `UV:✓` lub `UV:✗` obok tytułu informuje, czy obiekt ma UV.

Tekstury można przypisać do:

* Koloru
* Normalnej
* Chropowatości
* Metaliczności
* Krycia
* Przemieszczenia
* Emisji

Wiersz `Okluzja` pojawia się też, gdy importowany obiekt ma teksturę okluzji, ale Nomad jej nie używa.

Suwak każdego wiersza określa, jak mocno stosowana jest jego tekstura, od wcale do w pełni. `Kolor` i `Emisyjne` mają też próbkę koloru, która zabarwia teksturę, a `Emisyjne` ustawia siłę świecenia.

`Przemieszczenie` określa, jak daleko mapa przemieszczenia wypycha powierzchnię. Jego przycisk `Zastosuj` przesuwa wierzchołki o wartość przemieszczenia, a potem usuwa mapę. Wynik trafia do aktywnej warstwy.

Przycisk palety obok tytułu otwiera ustawienia wstępne materiałów z menu [Malowanie](painting.md): stuknij jedno z nich, aby skopiować jego tekstury na obiekt. Na komputerze importowane obrazy synchronizują się z oryginalnym plikiem, gdy wracasz do Nomad, a przycisk synchronizacji obok tytułu wczytuje je ponownie.

Kliknięcie gniazda tekstury otwiera selektor. Gdy tekstura jest już przypisana do gniazda materiału, kolejne kliknięcie otwiera panel tekstury:

### Opcje panelu tekstury {#texture-panel-options}

![](/images/material_texture_panel.webp)

Panel pokazuje rozmiar obrazu i podgląd tekstury.

### ![](/icons/open.webp) Otwórz {#open}
Wybiera inną teksturę. Na komputerze `Eksploruj` pokazuje plik obrazu w przeglądarce plików.

### ![](/icons/circle_cross.webp) Brak {#none}
Usuwa teksturę.

### Krycie {#texture-opacity}

Tylko tekstura koloru. Jeśli obraz ma kanał alfa, możesz go użyć jako krycia albo go zignorować.

### Format {#normal-format}
Tylko tekstura normalnej. Mapy normalnych występują w dwóch wariantach: `OpenGL (+Y)` i `DirectX (-Y)`. Jeśli szczegóły wyglądają na odwrócone, wypróbuj drugi wariant.

### Wysokość {#displacement-height}
Tylko tekstura przemieszczenia.
* `Lokalna` - Wysokość rośnie i maleje razem ze skalą obiektu.
* `Świat` - Wysokość pozostaje taka sama bez względu na skalę obiektu.

### Mnożenie {#multiply}
Tylko tekstury chropowatości, metaliczności i krycia. Mnoży wartości tekstury. Gdy wartość jest inna niż 100%, jest wyświetlana na gnieździe tekstury.

### ![](/icons/link.webp) Ikona łańcucha/łącza {#chainlink-icon}

Gdy ikona łącza w poniższych sekcjach jest włączona, używane opcje są wspólne z innymi teksturami (kolor, normalna, chropowatość, metaliczność, krycie, emisja), które także mają włączoną ikonę łącza.

Dzięki temu wyrównane tekstury pozostają wyrównane, nawet gdy zmieniasz parametry lub typ projekcji.


### Projekcja {#projection}
![](/images/material_projection.webp)

Określa, jak tekstura jest nakładana na obiekt.

* `Auto` - UV, jeśli obiekt ma UV, w przeciwnym razie Trzypłaszczyznowy
* `UV` - Nakłada teksturę według współrzędnych UV siatki. Jeśli siatka i tekstura pochodzą spoza Nomad albo zostaną wyeksportowane z Nomad do użycia gdzie indziej, właściwą opcją jest UV.
* `Trzypłaszczyznowy` - Rzutuje teksturę wzdłuż osi X, Y i Z i wygładza szwy.

### Trzypłaszczyznowy {#triplanar}
![](/images/material_triplanar.webp)

Projekcja trzypłaszczyznowa to skuteczny, a zarazem prosty sposób nakładania tekstur na obiekty.

Działa tak, jakby 6 projektorów z tym samym obrazem świeciło na przód, tył, lewą i prawą stronę, górę i dół obiektu.

W razie potrzeby wynik można potem wypalić do UV lub kolorów wierzchołków.


![](/images/material_triplanar_example.webp)

#### Metoda {#method}

* `Lokalna` - Projekcja przesuwa się razem z przekształceniem obiektu
* `Świat` - Projekcja pozostaje nieruchoma, a przesuwany obiekt przesuwa się przez nią.

#### Twardość {#hardness}

Jak mieszają się projekcje. Przy 100% nie ma mieszania, a krawędzie projekcji są ostre. Przy 0% krawędzie mieszają się w szerokim zakresie kątów. Wartość domyślna to 90%: na tyle dużo mieszania, aby ukryć krawędzie, a reszta projekcji pozostaje ostra.

### Jednolity {#uniform}

Gdy ta opcja jest zaznaczona, dla wszystkich projekcji używana jest ta sama twardość. Gdy nie jest zaznaczona, pojawiają się osobne ustawienia twardości dla projekcji X, Y i Z.


### Parametr {#parameter}
![](/images/material_parameter.webp)

#### Filtrowanie {#filtering}
Metoda filtrowania tekstury. Domyślnie `Auto`, dostępne metody to `Najbliższy`, `Liniowy` i `Mipmapa`. Najbliższy nie filtruje, więc z bliska tekstury mogą mieć postrzępione artefakty. Liniowy i Mipmapa filtrują lepiej, więc z bliska tekstury wyglądają na rozmyte, a nie postrzępione.

#### Rozmieszczenie sąsiadująco - X {#tiling-x}
Jeśli parametr Skala jest większy niż 1, przez co tekstura jest mniejsza niż UV obiektu, ta opcja określa, jak tekstura jest powtarzana wzdłuż osi X. `Brak` oznacza brak powtórzeń. `Powtarzanie` tworzy kopie tekstury. `Odbicie lustrzane` tworzy kopie tekstury, odwracając co drugą, co pomaga ukryć artefakty powtarzania.

#### Rozmieszczenie sąsiadująco - Y {#tiling-y}
Tak samo jak Rozmieszczenie sąsiadująco - X, ale dla osi Y.

### Przekształcenie {#transform}
![](/images/material_transform.webp)

Dodatkowe przekształcenia 2d stosowane do tekstury w przestrzeni UV. Przycisk zerowania przywraca wartości domyślne, a ikona łańcucha (gdy wybrane są tekstury inne niż kolor) łączy lub rozłącza przekształcenie z przekształceniem tekstury koloru.

#### Translacja {#translation}
Przesunięcie tekstury w osiach X i Y

#### Obrót {#rotation}
Obrót tekstury

#### Skala {#scale}
Skala tekstury: większe liczby zmniejszają teksturę na obiekcie. To, co dzieje się wtedy z teksturą, ustawisz opcjami Rozmieszczenie sąsiadująco - X i Rozmieszczenie sąsiadująco - Y.

### Jednolite skalowanie {#uniform-scale}
Gdy ta opcja jest wyłączona, Nomad pokazuje osobne ustawienia skali X i skali Y.
