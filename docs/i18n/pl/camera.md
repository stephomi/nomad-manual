# ![](/icons/camera.webp) Kamera {#camera}

To menu pozwala tworzyć i modyfikować kamery, a także decydować, jak się nimi posługujesz.

![](/images/camera_overview2.webp)

Kamery w Nomad mają kilka zastosowań:

* Ustawianie widoków do rzeźbienia pod precyzyjnymi kątami
* Kadrowanie obiektów, jak aparatem fotograficznym
* jako kamera z perspektywy pierwszej osoby do poruszania się po scenie
* jako kamera ortograficzna do gier izometrycznych lub renderów w stylu przemysłowym.

## Sterowanie kamerą {#control}

### Obrót {#rotation}
Kamerę obracasz, przeciągając *jednym* palcem po tle.
Jeśli przeciągniesz palcem po modelu, zaczniesz zamiast tego rzeźbić.

::: tip Czy mogę obrócić kamerę, jeśli nie mam dostępu do tła?
Tak, połóż na ekranie *dwa* palce, jak gdybyś chciał zacząć gest przesuwania/powiększania, a potem podnieś *jeden* palec.
:::

### Ostrość / reset {#focus}
*Stuknij dwukrotnie* model, aby skupić widok na wskazanym punkcie.
Jeśli *stukniesz dwukrotnie* tło, kamera skupi się zamiast tego na zaznaczonej siatce lub całej scenie, zobacz [Stuknij dwukrotnie tło](#dtap-tap-background).


### Przesuwanie {#translation}
Przesuwając *dwa* palce, przesuwasz kamerę.


### Powiększanie {#zooming}
Gestem szczypania przybliżasz i oddalasz widok.


### Przechylanie {#rolling}
Możesz *przechylić* widok, obracając *dwa* palce.
::: warning
Ten gest jest dostępny tylko w trybach obrotu `Trackball`.
:::

### Sterowanie na komputerze {#desktop}

Na komputerze do sterowania kamerą służy klawisz alt/opt:

* przeciągnięcie końcówką w pustym miejscu = obrót kamery
* alt + przeciągnięcie końcówką = przesuwanie
* alt + przeciągnięcie końcówką, a potem puszczenie alt = powiększanie (tak jak w ZBrush)

W przypadku tabletów Wacom z piórem z 2 lub więcej przyciskami skonfiguruj końcówkę i przyciski w ustawieniach Wacom w ten sposób:

* końcówka = lewy klik
* dolny przycisk = środkowy klik
* górny przycisk = prawy klik

Przy tych ustawieniach możesz sterować kamerą wyłącznie piórem:

* górny przycisk i ruch w zawieszeniu = obrót kamery
* dolny przycisk i ruch w zawieszeniu = przesuwanie

## Ustawienia kamery {#camera-controls}

![](/images/camera_list.webp)

### Widoki {#views}
Punkty widoku kamery zapisujesz przyciskiem `Dodaj widok`.
Gdy klikniesz nazwę widoku, kamera go przywróci.


::: tip
Zapisany widok zachowuje ustawienia [typu projekcji](#projection), a także [obraz referencyjny](background.md).  
Przydaje się to, gdy chcesz przełączać się między widokami referencyjnymi z przodu, z lewej i z tyłu, każdy z innym tłem.
:::

| Operacja    | Ikona                         | Opis                                                                        |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Widoczność  | ![](/icons/eye_open.webp)    | Włącza lub wyłącza kamerę. Ukryte kamery są pomijane przez przyciski poprzedniej/następnej |
| Nazwa       |                               | Zaznacza kamerę                                                             |
| Obraz       | ![](/icons/image.webp)       | Miniatura obrazu referencyjnego, jeśli jest powiązany z kamerą             |
| Projekcja   | ![](/icons/perspective.webp) | Projekcja kamery, z polem widzenia w przypadku perspektywy                  |
| Aktualizuj widok | ![](/icons/update_view.webp) | Aktualizuje zapisany widok bieżącym punktem widoku                     |
| Zmień nazwę | ![](/icons/pencil.webp)      | Edytuje nazwę kamery                                                        |
| Usuń        | ![](/icons/trash.webp)       | Usuwa kamerę                                                                |

### ![](/icons/camera_add.webp) Dodaj widok {#add}
Tworzy nową kamerę na podstawie bieżącego widoku.

### ![](/icons/camera.webp) Ikony {#icons-test}

Określa, czy ikony kamer są widoczne w widoku. Przycisk pojawia się obok `Dodaj widok`, gdy masz już kamerę. Ikona zaznaczonej kamery jest zawsze widoczna.

### Typ projekcji {#projection}
Wybierz `Perspektywa` lub `Ortograficzne`.

W perspektywie możesz zmienić `Pionowe pole widzenia` (FoV) kamery. Nad suwakiem widać odpowiadającą mu ogniskową aparatu 35 mm, co przydaje się, jeśli znasz fotografię.
Do rzeźbienia zwykle zaleca się niskie pole widzenia, bo pomaga to w ocenie proporcji.  
Tryb `Ortograficzne` odpowiada mniej więcej polu widzenia równemu 0.

### Pierwsza osoba {#fps}
Tylko w perspektywie. Umieszcza punkt obrotu bezpośrednio w kamerze, a nie na rzeźbie. Przeciąganie palcem po tle nie zmienia położenia kamery, tylko jej obrót, podobnie jak w grach z perspektywy pierwszej osoby. Przydaje się przy rzeźbieniu otoczenia, a nie pojedynczych obiektów.

![](/images/camera_rotation_ortho_view.webp)

### Typ obrotu {#rotation-type}
Domyślnie kamera używa trybu obrotu `Obrotnica`.
Oznacza to, że masz tylko dwa stopnie swobody. Jest to bardziej intuicyjne, ale czasem potrzebujesz większej elastyczności.  
Możesz przełączyć się na `Trackball`, który pozwala *przechylać* widok, obracając *dwa* palce w widoku. Są dwa tryby `Trackball`: pierwszy obraca widok jak kulę pod palcem, a drugi (z ikoną strzałek) obraca widok na podstawie poziomego i pionowego ruchu przeciągnięcia, co niektórym może wydawać się bardziej znajome.

### Wyrównanie ortograficzne {#orthographic}

Gdy ta opcja jest włączona i masz klawiaturę, przytrzymanie shift podczas obracania widoku przyciąga kamerę do najbliższego widoku z przodu, z tyłu, z góry, z dołu, z lewej lub z prawej i przełącza ją w tryb ortograficzny. Kamera przechodzi w tryb ortograficzny także po kliknięciu kostki widoku, aby przyciągnąć ją do widoku z przodu, z tyłu, z lewej, z prawej, z góry lub z dołu.

### Resetuj widok {#reset}

Ustawia kamerę z przodu i dopasowuje scenę do widoku.

### Przyciągnij widok {#snap}
Przyciąga do najbliższego widoku z przodu, z tyłu, z lewej, z prawej, z góry lub z dołu. Jeśli jesteś już w jednym z tych widoków, ponowne kliknięcie obróci widok o 180 stopni na przeciwną stronę.

### Szybkość {#speed}

Jeśli kamera porusza się Twoim zdaniem zbyt wolno lub zbyt szybko, możesz ustawić mnożnik szybkości dla `Obrót`, `Powiększanie` i `Przesuwanie`. Przydaje się, gdy rzeźba jest bardzo duża lub bardzo mała.

### Punkt obrotu – przegląd {#pivot}

Podczas obracania kamery widać małą różową kropkę: to punkt obrotu kamery.  
Bardzo ważne jest, aby wiedzieć, gdzie znajduje się punkt obrotu, żeby nie zgubić się i nie irytować się kamerą.

Domyślnie punkt obrotu jest aktualizowany przez te czynności:
- dwukrotne stuknięcie modelu
- dwukrotne stuknięcie tła (nowy punkt obrotu znajdzie się w środku siatki)
- położenie *dwóch* palców na ekranie (przesuwanie/powiększanie/przechylanie) przenosi punkt obrotu na środek między *dwoma* palcami

### Punkt obrotu {#update-pivot}

Możesz dodatkowo określić, kiedy punkt obrotu ma być aktualizowany:

* `Przy geście uruchomienia kamery` - Aktualizuje punkt obrotu, gdy zaczynasz poruszać kamerą.
* `Punkt obrotu poza obiektem` - Pozwala ustawić nowy punkt obrotu nawet wtedy, gdy powiększasz poza powierzchnią obiektu. Wymaga `Przy geście uruchomienia kamery`.
* `Aktualizuj po 2× stuknięciu` - Aktualizuje punkt obrotu, gdy dwukrotnie stukniesz powierzchnię obiektu.
* `Rzeźbienie (Pociągnięcie)` - Aktualizuje punkt obrotu podczas rzeźbienia.

::: tip
Gdy już się przyzwyczaisz, możesz ukryć różową kropkę (podpowiedź) w menu [Ustawienia](settings.md).
:::

### Wyśrodkuj widok podczas oddalania {#center-view-when-zooming-out}
Podczas oddalania kamera nie przesuwa się na boki: tylko się cofa, więc widok pozostaje wyśrodkowany.

### Stuknij dwukrotnie obiekt {#dtap-object}
Gdy ta opcja jest włączona, dwukrotne stuknięcie obiektu skupia kamerę na wskazanym punkcie.

### Stuknij dwukrotnie tło {#dtap-tap-background}
Gdy ta opcja jest włączona, dwukrotne stuknięcie tła skupia kamerę na:
* `Zaznaczenie` - Zaznaczonych obiektach.
* `Scena` - Całej scenie.
* `Przełącz` - Przełącza między nimi przy każdym dwukrotnym stuknięciu. Są dwie opcje `Przełącz`, które różnią się tym, która z nich jest pierwsza, co pokazują ich ikony.
