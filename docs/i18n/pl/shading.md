# ![](/icons/sun.webp) Cieniowanie {#shading}

To menu steruje trybami cieniowania w Nomad, właściwościami oświetlenia, środowiskiem i matcapem oraz mgłą.

![](/images/shading_overview.webp)



Możesz wybierać spośród kilku trybów renderowania:

| Tryb                        | Znaczenie                  | Opis                                                                      |
| :-------------------------: | :------------------------: | :-----------------------------------------------------------------------: |
| [Oświetlony (PBR)](#pbr)    | Physically Based Rendering | Światła, cienie, środowisko oraz malowana metaliczność/chropowatość       |
| [MatCap](#matcap)           | Material Capture           | Szybki tryb do rzeźbienia, mniej obciąża GPU/CPU niż PBR                  |
| [Nieoświetlony](#unlit)     | Kolor powierzchni          | Tylko kolor powierzchni, bez cieniowania i oświetlenia                    |
| [ID obiektu](#object-id)    | ID obiektu                 | Losowy kolor dla każdego obiektu, przydatny w aplikacjach do malowania.   |
| [ID instancji](#instance-id) | ID instancji              | Losowy kolor dla każdej instancji, pomaga rozpoznać współdzielone siatki  |

Jeśli chcesz dowiedzieć się więcej o metaliczności i chropowatości, zajrzyj do sekcji [Malowanie wierzchołków](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Grupa powierzchni {#face-group}
Nakłada na model kolory grup powierzchni. Grupy powierzchni to kolorowe zaznaczenia wielokątów, które możesz tworzyć narzędziem [Grupa powierzchni](tools#facegroup); większość prymitywów tworzy je też automatycznie.

Niektóre narzędzia automatycznie filtrują według grup powierzchni, gdy grupy są widoczne.

### ![](/icons/palette.webp) Pokaż malowanie {#show-paint}
Nomad może przechowywać kolor, chropowatość i metaliczność w wierzchołkach rzeźby. Tym polem wyboru możesz globalnie włączać i wyłączać wyświetlanie tych właściwości.

Pamiętaj, że jeśli masz jednocześnie właściwości wierzchołków i tekstury, a obie te rzeczy są włączone, ich wartości zostaną pomnożone.

### ![](/icons/shield.webp) Pokaż maskę {#show-mask}
Włącza i wyłącza nakładkę maski w skali szarości tworzonej [narzędziami maski](tools#mask). Gdy ta opcja jest wyłączona, maska również przestaje działać. Przydaje się to do szybkich zmian bez maski: potem możesz ją znowu włączyć i nie stracisz jej.

### ![](/icons/tool_hide.webp) Użyj funkcji Ukryj {#use-hide}

Włącza i wyłącza ukrywanie ścian. Pamiętaj, że działa to tylko wtedy, gdy NIE jesteś w narzędziu do ukrywania!

### ![](/icons/image.webp) Użyj tekstur {#use-textures}

Nomad pozwala przypisywać tekstury do obiektów w menu [Materiał](material). Jeśli tekstury są przypisane, możesz je globalnie włączać i wyłączać tym polem wyboru.

W Nomad nie można tworzyć ani edytować tekstur, ale tekstury z importowanych plików działają. Tekstury krycia działają w trybach Oświetlony, MatCap i Nieoświetlony, mapy normalnych w trybach Oświetlony i MatCap, kolor w trybach Oświetlony i Nieoświetlony, a emisja, chropowatość i metaliczność tylko w trybie Oświetlony. Przycisk jest wyszarzony, gdy scena nie zawiera żadnej tekstury.

### PBR i światła – przegląd {#pbr}
Ten podręcznik nie będzie wchodzić w szczegóły renderowania opartego na fizyce (Physically Based Rendering).

Warto pamiętać o jednym: oświetlenie i materiał są od siebie całkowicie niezależne.
Oznacza to, że możesz malować kolor, chropowatość i metaliczność obiektu, a oświetlenie jest obsługiwane osobno.
Dzięki temu możesz pomalować obiekt, a potem dopracować oświetlenie, nie psując ogólnego wyglądu modelu.

Światła, środowisko i mgła są dostępne tylko w [trybie PBR](#pbr).
Ze względu na wydajność możesz mieć maksymalnie 4 światła na urządzeniach mobilnych i 6 na komputerze.

::: tip
Możesz wczytać plik glTF z większą liczbą świateł, a Nomad zachowa je wszystkie.
Nie musi to jednak działać płynnie.
:::

::: tip
Możesz zasymulować wiele świateł, ustawiając obiekty jako nieoświetlone/emisyjne, a następnie włączając globalne oświetlenie w menu [Postprocessing](postprocess).
:::

### Typy świateł – przegląd {#light-types-overview}

Obecnie obsługiwane są następujące typy świateł:

| Tryb                        | Opis                                                        | Rzuca cienie |
| :-------------------------: | :---------------------------------------------------------: | :----------: |
| [Kierunkowe](#directional)  | Światło słoneczne z nieskończenie daleka                    | Tak          |
| [Środowisko](#env-light)    | Odległe światło dopasowane do HDR środowiska                | Tak          |
| [Stożkowe](#spot)           | Światło w kształcie stożka                                  | Tak          |
| [Wielokierunkowe](#point)   | Punktowe źródło światła świecące we wszystkich kierunkach   | Tak          |

#### ![](/icons/sun.webp) Kierunkowe {#directional}
Emituje światło z nieskończenie daleka, z jednakową intensywnością.
Jego położenie w scenie 3d nie ma znaczenia, liczy się tylko kierunek.

Możesz przyłączyć to światło do kamery, aby oświetlenie było zawsze takie samo.  
Możesz w ten sposób na przykład uzyskać światło konturowe (rim light – mocne światło padające zza modelu w stronę kamery), które zawsze oświetla tył modelu.

#### ![](/icons/panorama.webp) Światło środowiska {#env-light}
[HDR środowiska](#environment) dobrze sprawdza się jako ogólne, miękkie oświetlenie, ale jeśli w HDR widać mocne, ostre źródło światła, rzucany przez nie cień będzie bardzo miękki, często w ogóle niewidoczny. Pomóc może połączenie HDR środowiska ze światłem kierunkowym, ale trudno je ze sobą dokładnie zgrać.

To światło robi to za Ciebie. Automatycznie obraca się tak, by pokrywało się z najjaśniejszą częścią HDR, a Ty osobno sterujesz jego intensywnością i kątem (miękkością cienia). 

#### ![](/icons/spotlight.webp) Stożkowe {#spot}
Światło stożkowe świeci w jednym kierunku, w obrębie stożka.

#### ![](/icons/light.webp) Wielokierunkowe {#point}
Światło wielokierunkowe świeci we wszystkich kierunkach i również może rzucać cienie.

#### Cienie {#shadows}
Każde światło może rzucać cienie, a sposób ich obliczania wybierasz w jego [ustawieniach](#light-extra-controls). Jeśli widzisz artefakty cieni, mogą pomóc znajdujące się tam suwaki `Tolerancja`.

Jakość cieni zależy od wielkości obiektów w stosunku do całej sceny.  
Jeśli w scenie jest duży obiekt, który nie musi rzucać cieni (na przykład duża płaszczyzna), wyłącz rzucanie cieni w jego [ustawieniach materiału](material.md#casts-shadows).

## ![](/icons/sun.webp) Światła {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Pole wyboru świateł {#lights-checkbox}

Włącza i wyłącza wszystkie światła bezpośrednie w scenie.



### Dodaj światło {#add-light}

Dodaje światło do sceny – maksymalnie 4 na urządzeniach mobilnych i 6 na komputerze. Po dodaniu światła wyświetla się lista świateł z przyciskami, a u góry widoku pojawia się pasek narzędzi światła.

![](/images/shading_lights_icons.webp)

* Tekst pokazuje nazwę światła i jego jasność. Stuknij go, aby zaznaczyć światło.
* Ikona oka włącza i wyłącza widoczność.
* Ikona ołówka pozwala zmienić nazwę światła.
* Ikona kosza usuwa światło.
* Ikona kopiowania powiela światło. 
* Ikona 3 kropek otwiera pełny edytor światła. Większość tych funkcji jest dostępna także na pasku narzędzi, który pojawia się w widoku. 

Możesz też przeciągnąć światło na liście, aby zmienić kolejność.

### ![](/icons/spotlight.webp)  Ikony {#icons}

Włącza i wyłącza wyświetlanie ikon świateł w widoku

### Pasek narzędzi światła {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Ten pasek narzędzi pojawia się u góry widoku, gdy zaznaczysz światło.

* `Widoczne` włącza i wyłącza widoczność światła.
* Kierunkowe/Środowisko/Stożkowe/Wielokierunkowe zmienia typ światła. Stuknij, aby przełączać kolejno, albo przytrzymaj, aby wyświetlić menu.
* Intensywność steruje siłą światła. Wartość może przekroczyć 1.0 dla bardzo intensywnych świateł, co przydaje się przy globalnym oświetleniu w Postprocessingu.
* Kliknięcie próbki koloru otwiera selektor kolorów. Nomad oferuje kilka sposobów wybierania koloru. Suwak Kelvin to naturalny sposób na wybór ciepłego lub chłodnego światła.
* Cień włącza i wyłącza cienie.
* Kąt (_kierunkowe i środowisko_) lub Rozmiar (_stożkowe i wielokierunkowe_) ustala szerokość światła. Szersze światła rzucają miękkie cienie, dają miękkie oświetlenie i łagodniejsze odblaski na obiektach.
* Połączenie (_tylko kierunkowe_), Kąt stożkowy i Miękkość (_tylko stożkowe_) są opisane niżej, w części o [edytorze światła](#light-extra-controls).
* ... otwiera `Klonuj`, `Wyśrodkuj` i `Usuń`, a także ustawienia cieni.

### Dodatkowe ustawienia światła {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Ikona 3 kropek przy świetle na liście otwiera jego pełny edytor. Pamiętaj, że niektóre opcje dotyczą tylko wybranych typów świateł.

* `Kierunkowe/Środowisko/Stożkowe/Wielokierunkowe` pozwala zmienić typ światła.
* Kliknięcie `próbki koloru` otwiera selektor kolorów. 
* `Intensywność` steruje siłą światła.
* `Połączenie` (_tylko kierunkowe_) przypina światło do świata (`Stałe`) albo do kamery (`Kamera`). Jeśli na przykład używasz światła kierunkowego za postacią jako światła konturowego, to przy połączeniu z kamerą światło pozostanie za postacią bez względu na to, jak obracasz kamerę.
* `Miękkość` (_tylko stożkowe_) steruje ostrością krawędzi stożka światła. 0 to bardzo ostra krawędź. 1 to bardzo miękka, z gradientem ku środkowi stożka. W widoku możesz interaktywnie ustawiać miękkość małą niebieską kropką na stożku światła.
* `Kąt stożkowy` (_tylko stożkowe_) steruje kątem rozwarcia światła. Mały kąt to bardzo wąska wiązka, a 170 to bardzo szeroki snop światła. W widoku możesz interaktywnie ustawiać kąt stożka pomarańczową kropką.
* `Kąt` (_tylko kierunkowe i środowisko_) to pozorna wielkość światła – pomyśl o tym, jak duże wydaje się słońce na niebie. Większe kąty dają miękkie cienie i szersze odblaski.
* `Rozmiar` (_tylko stożkowe i wielokierunkowe_) to szerokość światła. Większe światła rzucają miękkie cienie.
* `Cień` włącza i wyłącza cienie dla bieżącego światła.
* Typ cienia określa, jak są obliczane cienie. `Mapa cieni` renderuje scenę z punktu widzenia światła, więc zacienia też geometrię, której kamera nie widzi. `Przestrzeń ekranu` korzysta tylko z tego, co już widać na ekranie: jest mniej wymagająca, ale eksperymentalna. Zwykle mapa cieni jest bardziej niezawodna.
* `Tolerancja` (_tylko przestrzeń ekranu_): jeśli widać artefakty cieni (cienie nie stykają się z powierzchnią albo pojawia się w nich szum i wzory), dostosowanie tolerancji może pomóc.
* `Kontaktowe` dodaje dokładniejsze cienie na krótkich odległościach, tam gdzie obiekty się stykają. Przy `Auto` cienie kontaktowe dostaje tylko dominujące światło w scenie; `Nie` i `Tak` wymuszają ich wyłączenie lub włączenie dla tego światła. Jego suwak `Tolerancja` działa jak opisany wyżej.

Przycisk `...` na pasku narzędzi w widoku zawiera te same ustawienia cieni, a także:

* `Klonuj` powiela światło.
* `Wyśrodkuj` przenosi światło przed kamerę, zachowując jego kierunek.
* `Usuń` usuwa światło.


## ![](/icons/panorama.webp) Środowisko {#environment}

![](/images/shading_environment.webp)

W prawdziwym świecie światło pada ze wszystkich stron: błękit nieba, zieleń trawy, czerwień budynku – całe to światło z „otoczenia” można zasymulować mapą środowiska. 

Pole wyboru obok tytułu włącza i wyłącza oświetlenie środowiskowe.

Nomad zawiera kilka przykładowych map środowiska dla wnętrz i plenerów, o różnych odcieniach i poziomach jasności. Wypróbuj różne mapy, aby sprawdzić, która najlepiej wydobywa detale Twoich rzeźb.

Stuknij obraz, aby zobaczyć dostępne mapy środowiska. W tym oknie wybierz `Importuj...`, aby wczytać własną. Najlepiej używać obrazów HDR (High Dynamic Range) w formacie latlong, czyli equirectangular, jako plików .hdr lub .exr. Przeglądarka może też pobierać środowiska bezpośrednio z [Poly Haven](https://polyhaven.com/hdris), gdzie znajdziesz dobrą kolekcję darmowych map środowiska.

### Ekspozycja {#env-exposure}
Dostosowuje jasność mapy środowiska. W połączeniu ze zwykłymi światłami mapy bywają zbyt jasne; zmniejszenie ekspozycji pomaga zachować równowagę, zwłaszcza przy globalnym oświetleniu w ustawieniach [Postprocessing](postprocess).

### Obrót {#env-rotation}

Mapy środowiska rejestrują światło ze wszystkich kierunków, więc możesz je obracać, aby odbicia i ogólne oświetlenie dobrze współgrały z rzeźbą. Środowisko możesz też obracać, przeciągając 3 palcami poziomo po widoku.

### Przyłączono do kamery {#env-attached}
Przyłącza środowisko do kamery.

Oświetlenie pozostaje wtedy niezmienne, co może się przydać podczas rzeźbienia.

### Rozmycie (tło) {#env-background-blur}
Ten suwak pojawia się tylko wtedy, gdy [tło](background.md) jest ustawione na środowisko. Rozmywa obraz środowiska za modelem, nie zmieniając oświetlenia.


## ![](/icons/fog.webp) Mgła {#fog}

Mgła dodaje scenie atmosferycznej głębi i sprawia, że widać snopy światła. Włącz ją polem wyboru obok tytułu. Podobnie jak światła i środowisko jest dostępna tylko w trybie [Oświetlony (PBR)](#pbr).

::: tip Mocniejsze snopy światła
Zmniejsz wartość `Środowisko` mgły i użyj jasnego światła stożkowego lub wielokierunkowego. Zwiększaj `Gęstość`, aż mgła będzie wyraźnie widoczna. Aby snopy były widoczne w rzadszej mgle, ustaw `Kierunek rozpraszania` na wysoką wartość dodatnią i skieruj kamerę w stronę światła.
:::

### Kolor {#fog-color}
Kolor mgły i rozpraszanego przez nią światła.

### Gęstość {#fog-density}
Jak szybko mgła gęstnieje wraz z odległością.

### Maksymalne krycie {#fog-opacity}
Ogranicza, jak bardzo mgła może zasłonić scenę, nawet przy dużej gęstości.

### Kierunek rozpraszania {#fog-scattering}
Kierunek, w którym mgła rozprasza światło (nazywany też anizotropią). Wartości dodatnie rozjaśniają mgłę, gdy patrzysz w stronę światła, ujemne – gdy patrzysz w przeciwną stronę, a zero rozprasza światło równomiernie we wszystkich kierunkach.

### ![](/icons/panorama.webp) Środowisko {#fog-environment}
Jak mocno [środowisko](#environment) oświetla mgłę. Opcja jest wyszarzona, gdy środowisko jest wyłączone.

### Szum {#fog-noise}
Dodaje do mgły szum, który rozbija ją na płaty bez zmiany jej ogólnej gęstości. Gdy szum jest większy od 0, suwak `Rozmiar` ustala wielkość wzoru.

### Kształt {#fog-shape}
Gdzie mgła wypełnia scenę:

* `Jednolity` - wypełnia całą scenę.
* `Pionowy` - utrzymuje mgłę w pionowo ograniczonym pasie o miękkich krawędziach. Suwaki `Dół` i `Góra` ustalają wysokość jego dolnej i górnej krawędzi, a ich przycisk z okiem pokazuje pas w widoku, gdy je dostosowujesz.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Jak sugeruje nazwa (MATerial CAPture, czyli „przechwycenie materiału”), matcap zawiera w jednym obrazie zarówno informacje o oświetleniu, jak i o materiale.
Ponieważ sam materiał jest już zawarty w matcapie, kanały malowania chropowatości i metaliczności są ignorowane.
Malowany kolor jest mnożony przez matcap, więc jeśli masz czarny lub szary matcap, biała farba go nie rozjaśni.

Artyści chętnie wybierają ten tryb do rzeźbienia, bo pozwala skupić się na samym kształcie i geometrii.

Stuknięcie kuli otwiera przeglądarkę obrazów. Możesz też dodać własny matcap: zwykle nada się dowolne zdjęcie, render, a nawet obraz kuli ciasno przycięty do kwadratu. W internecie dostępnych jest wiele bibliotek matcapów, przydatnym źródłem jest [biblioteka matcapów nidorx](https://github.com/nidorx/matcaps).

### Użyj globalnego MatCap {#matcap-global}

Zwykle artyści używają jednego matcapa dla całej rzeźby, ale jeśli ten przełącznik jest wyłączony, zaznaczony obiekt może mieć własny matcap. Można to wykorzystać artystycznie, by uzyskać efektowne rezultaty.

::: tip
Wyłącz tę opcję i użyj obrazu gałki ocznej na oczy swoich postaci!
:::

### Obrót {#matcap-rotation}
Matcap to szczególny rodzaj mapy środowiska, więc tak jak mapę środowiska można go obracać. W każdej chwili możesz to też zrobić w widoku, przeciągając 3 palcami w lewo i w prawo.

Przycisk kłódki obok suwaka blokuje obrót, więc przeciągnięcie 3 palcami nie obróci przypadkiem matcapa.



## ![](/icons/circle_fill.webp) Nieoświetlony {#unlit}

Ten tryb pokazuje tylko kolor powierzchni. Przydaje się do sprawdzenia, czy kolory powierzchni obiektów są takie, jak oczekujesz, bez rozpraszania się światłami, cieniami, odbiciami czy przezroczystością. 

Można go też używać do niefotorealistycznych renderów, by uzyskać płaski, kreskówkowy wygląd.

## ![](/icons/cube.webp) ID obiektu {#object-id}

Wszystkie informacje o oświetleniu i powierzchni są ignorowane, a każdy obiekt jest cieniowany innym, jednolitym kolorem. Jeśli wyrenderujesz to razem z renderem PBR, możesz w programie graficznym zaznaczać obszary według koloru i w ten sposób korygować kolory konkretnych obiektów.

Pamiętaj, że te kolory pojawiają się też w [widoku drzewa w menu Scena](scene#tree-view).

### Losowy ID {#object-random}

Generuje nowy zestaw losowych kolorów. 

## ![](/icons/link.webp) ID instancji {#instance-id}

Tak samo jak ID obiektu, ale instancje mają ten sam kolor. 

### Losowy ID {#instance-random}

Generuje nowy zestaw losowych kolorów.
