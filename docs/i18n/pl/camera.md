# ![](/icons/camera.webp) Kamera {#camera}

To menu pozwala tworzyć i modyfikować kamery, a także kontrolować sposób interakcji z nimi.

![](/images/camera_overview2.webp)

Kamery w Nomad mają kilka zastosowań:

* Ustawianie widoków do rzeźbienia z precyzyjnych kątów
* Używanie jak aparatu fotograficznego do kadrowania obiektów
* Jako kamera z perspektywy pierwszej osoby do nawigacji po scenie
* Jako kamera ortograficzna do gier izometrycznych lub renderingu w stylu przemysłowym.

## Sterowanie kamerą {#control}

### Obrót {#rotation}
Obracasz kamerę, przeciągając *jednym* palcem po tle.
Jeśli przeciągniesz palcem po modelu, zamiast tego rozpocznie się operacja rzeźbienia.

::: tip Czy mogę obracać kamerę, jeśli nie mam dostępu do tła?
Tak, możesz położyć *dwa* palce na ekranie – tak jakbyś chciał rozpocząć gest przesuwania/powiększania – a następnie podnieść *jeden* palec.
:::

### Ustaw ostrość / Resetuj {#focus}
*Podwójne stuknięcie* w model ustawi ostrość na wskazanym punkcie.
Jeśli *podwójnie stukniesz* w tło, kamera ustawi ostrość na zaznaczonej siatce.

### Przesuwanie {#translation}
Przesuwając *dwa* palce, możesz przesuwać (panować) kamerę.

### Przybliżanie {#zooming}
Gest szczypania pozwala przybliżać i oddalać widok.

### Obracanie (rolling) {#rolling}
Możesz *obracać* widok, obracając *dwa* palce.
::: warning
Ten gest jest dostępny tylko w trybie obrotu `trackball`.
:::

### Sterowanie na komputerze {#desktop}

Na komputerze stacjonarnym klawisz alt/opt służy do sterowania kamerą:

* tip przeciąganie po pustej przestrzeni = obrót kamery
* alt+tip przeciąganie = przesuwanie
* alt+tip przeciąganie, następnie puszczenie alt = powiększanie (tak jak w ZBrushu)

W tabletach Wacom z 2 lub większą liczbą przycisków na piórze użyj ustawień Wacom, aby skonfigurować końcówkę i przyciski w następujący sposób:

* tip = lewy przycisk myszy
* dolny rocker = środkowy przycisk myszy
* górny rocker = prawy przycisk myszy

Z tymi ustawieniami możesz manipulować kamerą wyłącznie piórem:

* górny rocker i ruch w powietrzu = obrót kamery
* dolny rocker i ruch w powietrzu = przesuwanie

## Ustawienia kamery {#camera-controls}

![](/images/camera_list.webp)

### Widoki {#views}
Możesz zapisywać punkty widokowe kamery za pomocą `Add View`.
Jeśli klikniesz nazwę widoku, kamera przywróci ten widok.

::: tip
Zapisany widok zachowa ustawienia [Projection Type](#projection-type), a także [Reference image](background.md).  
Może to być przydatne, jeśli chcesz przełączać się między przednim/lewym/tylnym widokiem referencyjnym z różnymi tłami.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Toggle the camera. Hidden cameras will be skipped from previous/next button |
| Name        |                               | Select the camera                                                           |
| Image       | ![](/icons/image.webp)       | A thumbnail of a reference image if it is linked to the camera              |
| Update View | ![](/icons/update_view.webp) | Update the saved view with the current view point                           |
| Edit Name   | ![](/icons/pencil.webp)      | Edit the camera name                                                        |
| Delete      | ![](/icons/trash.webp)       | Delete the camera                                                           |

### ![](/icons/tool_view.webp) Dodaj widok {#add}
Utwórz nową kamerę na podstawie bieżącego widoku.

### ![](/icons/camera.webp) Ikony {#icons-test}

Przełącz widoczność ikon kamer w widoku. Jeśli kamera jest zaznaczona, jej ikona jest zawsze widoczna.

### Typ projekcji {#projection}
Możesz zmienić `Field of View` (FOV / ogniskową) swojej kamery.
Zazwyczaj zaleca się używanie niskiego FOV do celów rzeźbienia, ponieważ pomaga to w proporcjach.  
Możesz także użyć trybu `Orthographic`, który jest mniej więcej równoważny FOV równemu 0.

### Pierwsza osoba {#fps}
Włącza ustawienie punktu obrotu bezpośrednio na kamerze, zamiast na rzeźbie. Przeciąganie palcem po tle zablokuje pozycję kamery, ale zmieni jej obrót, podobnie jak w grach z perspektywy pierwszej osoby. Przydatne podczas rzeźbienia środowisk, a nie pojedynczych obiektów.

![](/images/camera_rotation_ortho_view.webp)

### Typ obrotu {#rotation-type}
Domyślnie kamera używa trybu obrotu `Turntable`.
Oznacza to, że masz tylko dwa stopnie swobody; jest to bardziej intuicyjne, ale w niektórych przypadkach będziesz potrzebować większej elastyczności.  
Możesz przełączyć się na `Trackball`, wtedy będziesz mógł *obracać* widok, obracając *dwa* palce na widoku. Na komputerze stacjonarnym dostępny jest alternatywny tryb trackball, który może być bardziej znajomy dla niektórych użytkowników.

### Ortograficzne przyciąganie {#orthographic}

Po włączeniu, jeśli masz klawiaturę, przytrzymanie klawisza Shift podczas obracania widoku spowoduje przeskoczenie kamery do najbliższego widoku przód/tył/góra/dół/lewo/prawo i ustawienie kamery w tryb ortograficzny. Kamera zostanie również ustawiona na ortograficzną, gdy kliknięta zostanie kostka widoku, aby przeskoczyć do przodu/tyłu/lewo/prawo/góra/dół.

### Resetuj widok {#reset}

Przesuń kamerę na przód i dopasuj scenę do widoku.

### Przyciągnij widok {#snap}
Przeskocz do najbliższego widoku przód/tył/lewo/prawo/góra/dół. Jeśli już znajdujesz się w jednym z tych widoków, ponowne kliknięcie spowoduje przeskoczenie o 180 stopni na przeciwną stronę.

### Prędkość {#speed}

Jeśli czujesz, że kamera porusza się zbyt wolno lub zbyt szybko, możesz ustawić mnożnik prędkości dla `rotation`, `translation` i `zooming`. Przydatne, jeśli twoja rzeźba jest bardzo duża lub bardzo mała.

### Przegląd punktu obrotu {#pivot}

Podczas obracania kamery możesz zobaczyć małą różową kropkę – to jest punkt obrotu (pivot) kamery.  
Bardzo ważne jest, aby rozumieć, gdzie znajduje się pivot, aby nie zgubić się ani nie frustrować pracą z kamerą.

Domyślnie pivot jest aktualizowany przez następujące operacje:
- podwójne stuknięcie w model
- podwójne stuknięcie w tło (nowy pivot będzie na środku twojej siatki)
- położenie *dwóch* palców na ekranie (pan/zoom/roll) zaktualizuje pivot na środek *dwóch* palców

### Aktualizuj punkt obrotu... {#update-pivot}

Możesz dalej dostosować aktualizowanie pivotu za pomocą tych opcji:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Kiedy już się do tego przyzwyczaisz, możesz ukryć (podpowiedź) różową kropkę w menu [Settings](settings.md).
:::

### Podwójne stuknięcie na obiekcie {#dtap-object}
Gdy `Focus` jest włączony, podwójne stuknięcie przeniesie pivot na stuknięty obiekt.

### Podwójne stuknięcie na tle {#dtap-tap-background}
Po włączeniu ustawia pivot na jeden z: Selection, Scene lub przełącza między nimi.