# ![](/icons/sun.webp) Cieniowanie {#shading}

To menu kontroluje tryby cieniowania używane przez Nomad, właściwości oświetlenia oraz właściwości światła otoczenia/matcap.

![](/images/shading_overview.webp)



Możesz wybrać pomiędzy kilkoma trybami renderowania:

| Mode                        | Meaning                    | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | Malowanie z użyciem metaliczności/szorstkości                   |
| [Matcap](#matcap)           | Material Capture           | Używany podczas rzeźbienia, zużywa mniej GPU/CPU niż PBR        |
| [Unlit](#unlit)             | Surface Color              | Tylko kolor powierzchni, bez cieniowania i oświetlenia          |
| [Object Id](#object-id)      | Object ID                  | Losowy kolor na obiekt, przydatne w programach do malowania     |
| [Instance Id](#instance-id)  | Instance ID                | Losowy kolor na instancję, przydatne do identyfikacji współdzielonych siatek |

Jeśli chcesz dowiedzieć się więcej o metaliczności i szorstkości, zobacz sekcję [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Grupa ścian {#face-group}
Nakładka kolorów grup ścian. Grupy ścian to kolorowe zaznaczenia wielokątów, które można tworzyć narzędziem [Face group](tools#facegroup) i które są tworzone automatycznie dla większości prymitywów.

Niektóre narzędzia będą automatycznie filtrować po grupach ścian, gdy są one widoczne.

### Pokaż malowanie {#show-paint}
Nomad może przechowywać kolor, szorstkość i metaliczność w wierzchołkach twojej rzeźby. Możesz globalnie przełączać wyświetlanie tych właściwości tym polem wyboru.

Zauważ, że jeśli masz zarówno właściwości wierzchołków, jak i tekstury, i oba są włączone, wartości zostaną pomnożone przez siebie.

### Pokaż maskę {#show-mask}
Przełącz szarą nakładkę maski z [mask tools](tools#mask). Gdy jest wyłączona, maska jest również wyłączona, co jest przydatne do szybkich zmian bez maski; potem możesz ją ponownie włączyć i nie stracisz swojej maski.

### Użyj ukrywania {#use-hide}

Przełącz ukryte ściany. Zauważ, że działa to tylko wtedy, gdy NIE jesteś w narzędziu hide!

### Użyj tekstur {#use-textures}

Nomad pozwala przypisywać tekstury do obiektów z menu [material](material). Jeśli tekstury są przypisane, można je globalnie przełączać tym polem wyboru.







### Przegląd PBR i świateł {#pbr}
Ten podręcznik nie będzie wchodził w szczegóły dotyczące fizycznie poprawnego renderingu (Physically Based Rendering).

Ważne jest, aby pamiętać, że oświetlenie i materiał są całkowicie rozdzielone.
Oznacza to, że możesz malować kolor, szorstkość i metaliczność obiektu, podczas gdy oświetlenie jest obsługiwane niezależnie.
Pozwala to pomalować obiekt, a następnie później dopracować oświetlenie bez psucia ogólnego wyglądu modelu.

Światła są dostępne tylko w [trybie PBR](#pbr).
Ze względów wydajnościowych jesteś ograniczony do 4 świateł.

::: tip
Możesz wczytać plik glTF z więcej niż 4 światłami i Nomad zachowa wszystkie.
Nie musi to jednak działać wydajnie.
:::

::: tip
Możesz „udawać” wiele świateł, ustawiając obiekty jako unlit/emissive, a następnie włączając globalne oświetlenie w menu [post process](postprocess).
:::

### Przegląd typów świateł {#light-types-overview}

Oto typy świateł obecnie obsługiwane:

| Mode                        | Description                                             | Can cast shadows                                       |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Światło słoneczne z nieskończonej odległości           | tak                                                    |
| [Environment](#environment) | Odległe światło dopasowane do HDR otoczenia            | tak                                                    |
| [Spot](#spot)               | Światła w kształcie stożka				                | Tak                                                    |
| [Point](#point)             | Punktowe światło dookólne                              | Tak, ale tylko przez mniej solidne cienie ekranowe     |

#### Kierunkowe {#directional}
Emituje światło z nieskończonej odległości, z jednolitą intensywnością.
Jego pozycja 3D w scenie nie ma znaczenia, liczy się tylko orientacja.

Możesz przypiąć to światło do kamery, dzięki czemu oświetlenie będzie spójne.  
Na przykład możesz użyć go jako światła obrysowego (mocne światło emitowane zza modelu, skierowane w stronę kamery), które zawsze oświetla tył twojego modelu.

#### Środowiskowe {#env-light}
Użycie [environment hdr](#environment) dobrze sprawdza się przy ogólnym miękkim oświetleniu, ale jeśli w HDR widoczne jest silne, ostre źródło światła, cień przez nie tworzony będzie bardzo miękki, często w ogóle niewidoczny. Użycie światła kierunkowego w połączeniu z HDR otoczenia może pomóc, ale ich wyrównanie może być trudne.

To światło wykonuje tę pracę za ciebie. Światło zostanie automatycznie obrócone tak, aby wyrównać się z najjaśniejszą częścią HDR, a następnie możesz osobno kontrolować jego intensywność i kąt (miękkość cienia). 

#### Reflektor {#spot}
Światło typu spot emituje światło w jednym kierunku, ograniczone kształtem stożka.

#### Punktowe {#point}
Światło punktowe emituje światło we wszystkich kierunkach.  
Obecnie światło punktowe nie obsługuje cieni.

#### Cienie {#shadows}
Opcja `normal bias` może być użyta do zredukowania typowych artefaktów cieni (acne/peter-panning).

Jakość cieni zależy od rozmiaru obiektów względem całej sceny.  
Jeśli masz duży obiekt w scenie, który nie musi rzucać cieni (na przykład duża płaszczyzna), upewnij się, że wyłączysz rzucanie cieni w jego [ustawieniach materiału](material.md#cast-shadows).

## Światła {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Pole wyboru Światła {#lights-checkbox}

Przełącz wszystkie światła bezpośrednie w scenie.



### Dodaj światło {#add-light}

Dodaj światło do sceny, maksymalnie 4. Gdy światło zostanie dodane, wyświetlona zostanie lista świateł z przyciskami, a na górze widoku pojawi się pasek narzędzi świateł.

![](/images/shading_lights_icons.webp)

* Tekst pokazuje nazwę światła i jasność.
* Ikona oka przełącza widoczność.
* Ikona ołówka pozwala zmienić nazwę światła.
* Ikona kosza usuwa światło.
* Ikona kopiowania duplikuje światło. 
* Ikona z 3 kropkami otwiera pełny edytor światła. Większość tej funkcjonalności jest również dostępna z paska narzędzi, który pojawia się w widoku. 

### ![](/icons/spotlight.webp) Ikony {#icons}

Przełącz wyświetlanie ikon świateł w widoku

### Pasek narzędzi świateł {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Ten pasek narzędzi pojawi się na górze widoku, gdy światło jest zaznaczone.

* Show przełącza widoczność światła.
* Directional/Environment/Spot/Point zmienia typ światła. Stuknij, aby przełączać, lub przytrzymaj, aby zobaczyć menu.
* Intensity kontroluje siłę światła; wartość może przekraczać 1.0 dla bardzo intensywnych świateł, co jest przydatne przy użyciu z Global Illumination w Post Process.
* Kliknięcie próbki koloru otwiera selektor koloru. Nomad oferuje kilka sposobów wyboru koloru. Kontrola Kelvin daje naturalny sposób wyboru ciepłego/chłodnego oświetlenia.
* Shadow przełącza cienie.
* Size ustawia szerokość światła. Szersze światła rzucają miękkie cienie, miękkie oświetlenie i bardziej miękkie refleksy na obiektach.
* ... otwiera dodatkowe kontrolki.

### Dodatkowe kontrolki światła {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Zauważ, że niektóre opcje są specyficzne dla określonych typów świateł.

* `Clone` duplikuje światło.
* `Recenter` przenosi światło z powrotem do środka sceny.
* `Delete` usuwa światło.
* `Directional/Environment/Spot/Point` pozwalają zmienić typ światła.
* `colour swatch` po kliknięciu otwiera selektor koloru. 
* `Intensity` kontroluje siłę światła.
* `Attachment` (_tylko directional_) ustawia, czy światło jest przypięte do świata, czy do kamery. Np. jeśli używasz światła kierunkowego za postacią jako światła obrysowego, to przy ustawieniu attachment na camera, obracanie kamery zawsze będzie utrzymywać światło za postacią.
* `Angle` (_tylko directional i environment_) to pozorny rozmiar światła, pomyśl o tym jak o tym, jak duże słońce wydaje się na niebie. Większe kąty dają bardziej miękkie cienie i szersze refleksy.
* `Softness` (_tylko spotlight_) kontroluje ostrość krawędzi stożka światła. 0 to bardzo ostra krawędź. 1 to bardzo miękka, z gradientem do środka stożka światła. W widoku mała niebieska kropka na stożku światła może być użyta do interaktywnego ustawiania miękkości.
* `Cone angle` (_tylko spotlight_) kontroluje kąt rozwarcia reflektora. Mały kąt to bardzo cienka wiązka światła, 170 to bardzo szeroki rozkład światła. W widoku pomarańczowa kropka może być użyta do interaktywnego ustawiania kąta stożka.
* `Shadow` przełącza cienie dla bieżącego światła.
* `Shadow map` i `screenspace` to różne sposoby obliczania cieni; ogólnie shadow map jest bardziej niezawodny.
* `Contact` reguluje sposób obliczania cieni kontaktowych. Cienie są trudnym problemem w grafice komputerowej i mogą powodować artefakty w renderingu. Bardziej dokładne cienie można wybrać dla najważniejszego światła w scenie; ta kontrolka określa, czy najważniejsze światło jest wybierane automatycznie przez Nomad, czy przez użytkownika.
* `Tolerance` – jeśli widoczne są artefakty cieni (cienie nie wydają się stykać z powierzchniami lub w cieniach pojawia się szum i wzory), regulacja tolerance może pomóc rozwiązać te problemy.


## Środowisko {#environment}

![](/images/shading_environment.webp)

Światło w prawdziwym świecie pochodzi ze wszystkich kierunków; błękit nieba, zieleń trawy, czerwień budynku – całe to światło z „otoczenia” można zasymulować za pomocą mapy środowiskowej (environment map). 

Nomad zawiera kilka przykładowych map środowiskowych dla wnętrz i plenerów, o różnych odcieniach i poziomach jasności. Wypróbuj różne mapy, aby zobaczyć, która najlepiej wydobywa detale twoich rzeźb.

Stuknij obraz, aby zobaczyć dostępne mapy środowiskowe. Z tego okna dialogowego wybierz „Import...”, aby wczytać własną. Najlepiej używać obrazów HDR (High Dynamic Range) w formacie latlong lub equirectangular, jako pliki .hdr lub .exr. Strona [www.polyhaven.com](https://polyhaven.com/hdris) ma dobrą kolekcję darmowych map środowiskowych; zazwyczaj mapy hdr 1k mają dobry rozmiar i jakość.

### Ekspozycja {#env-exposure}
Reguluje jasność mapy środowiskowej. Często mapy mogą być zbyt jasne przy użyciu z normalnymi światłami; zmniejszenie ekspozycji może pomóc w zbalansowaniu, szczególnie przy użyciu z Global Illumination w ustawieniach [Post Process](postprocess).

### Obrót {#env-rotation}

Ponieważ mapy środowiskowe rejestrują światło ze wszystkich kierunków, możesz je obracać, aby uzyskać dobre połączenie odbić i ogólnego oświetlenia z twoją rzeźbą.

### Dołączone do kamery {#env-attached}
Przypnij środowisko do kamery.

Wymusi to spójne oświetlenie, co może być przydatne podczas rzeźbienia.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Jak sugeruje nazwa (MATerial CAPture), matcap zawiera zarówno informacje o oświetleniu, jak i materiale w jednym obrazie.
Ponieważ materiał jest już obecny w matcapie, kanały malowania szorstkości i metaliczności będą ignorowane.
Kolor malowania zostanie pomnożony przez matcap, co oznacza, że jeśli masz czarny/szary matcap, użycie białej farby nie sprawi, że będzie jaśniejszy.

Artyści często preferują ten tryb do rzeźbienia, ponieważ pozwala im skupić się na kształcie i samej geometrii.

Stuknięcie w sferę otworzy przeglądarkę obrazów. Możesz też dodać własny matcap – zazwyczaj dowolne zdjęcie, render, a nawet malunek sfery przyciętej ciasno do kwadratu może zostać użyty. W sieci dostępnych jest wiele bibliotek matcap; przydatnym źródłem jest [biblioteka matcap nidorx](https://github.com/nidorx/matcaps).

### Użyj globalnego Matcap {#matcap-global}

Zazwyczaj artyści używają jednego matcapa dla całej rzeźby, ale jeśli ten przełącznik jest wyłączony, każdy obiekt może mieć własny matcap. Można to artystycznie wykorzystać do uzyskania wyrazistych rezultatów.

::: tip
Wyłącz tę opcję i użyj obrazu gałki ocznej dla oczu swojej postaci!
:::

### Obrót {#matcap-rotation}
Matcap jest wyspecjalizowaną formą mapy środowiskowej, więc podobnie jak mapa środowiskowa może być obracany. Możesz to również robić w dowolnym momencie w widoku, przeciągając trzema palcami w lewo i prawo.



## ![](/icons/circle_fill.webp) Bez oświetlenia {#unlit}

Ten tryb pokazuje tylko kolor powierzchni. Może być przydatny do sprawdzenia, czy kolory powierzchni twoich obiektów są takie, jakich oczekujesz, bez rozpraszania przez światła, cienie, odbicia, przezroczystość. 

Tryb ten może być również używany do nie-fotorealistycznych renderów, aby uzyskać płaski, kreskówkowy wygląd.

## ![](/icons/cube.webp) ID obiektu {#object-id}

Wszystkie informacje o oświetleniu i powierzchni są ignorowane, a każdy obiekt jest cieniowany unikalnym płaskim kolorem. Jeśli zostanie to wyrenderowane obok renderu PBR, może być użyte w programie do malowania do zaznaczania po kolorze, a tym samym do wykonywania korekcji kolorów na konkretnych obiektach.

Zauważ, że te kolory pojawią się również w [widoku drzewa w menu Scene](scene#tree-view).

### Losuj ID {#object-random}

Wygeneruj nowy zestaw losowych kolorów. 

## ![](/icons/link.webp) ID instancji {#instance-id}

Tak samo jak Object ID, ale instancje będą miały ten sam kolor. 

### Losuj ID {#instance-random}

Wygeneruj nowy zestaw losowych kolorów.