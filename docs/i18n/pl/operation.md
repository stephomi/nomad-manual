# ![](/icons/operation.webp) Operacja {#operation}

To menu stosuje operację do całej powierzchni zaznaczonych obiektów naraz: wygładzanie, łagodzenie, polerowanie, napełnianie, korektę kolorów, rozmycie lub wyostrzenie malowania i maski.

![](/images/operation_overview.webp)

## Przegląd {#overview}

Pędzel działa tam, gdzie prowadzisz pociągnięcie, a operacja działa jednocześnie na każdy wierzchołek zaznaczonych obiektów. Tytuł pokazuje nazwę obiektu albo liczbę obiektów, gdy zaznaczonych jest kilka.

Każda operacja to suwak: przeciągnij go w prawo, aby zastosować więcej, w lewo, aby zastosować mniej (albo operację przeciwną, w przypadku suwaków ze strzałką po obu stronach). Po puszczeniu suwak wraca do zera, a każde przeciągnięcie to jeden krok w [Historii](history.md), więc możesz stosować operację kilka razy, w małych dawkach.

::: tip
Operacje to szybki sposób na wyczyszczenie całej siatki po przebudowie wokselowej lub operacji logicznej: odrobina `Złagodź` wyrównuje trójkąty, odrobina `Gładkie` usuwa szum, i nie musisz szukać każdego miejsca pędzlem.
:::

## Filtry {#filters}

Przyciski u góry ograniczają obszar działania operacji:

* `Maska` - Zamaskowane obszary pozostają nietknięte.
* `Ukryj` - Ukryte obszary pozostają nietknięte.
* `Przesunięcie` - (Gdy zaznaczona jest [warstwa](layers.md)) Zmieniają się tylko obszary, w których aktywna warstwa zawiera rzeźbienie, więc możesz wygładzić lub napełnić zawartość warstwy bez naruszania reszty.

## Wygładzanie {#smoothing}

* `Zachowaj objętość` - Wygładza bez kurczenia powierzchni. Przycisk z kołem zębatym zawiera używane przy tym wartości `Pomniejsz` i `Napełnij`.
* `Zachowaj granicę` - Wierzchołki na granicy siatki (krawędzi otworu) pozostają nieruchome.
* `Stabilne wygładzanie` - Stara się, aby wygładzanie nie zależało od topologii. Sprawdza się najlepiej, gdy gęstość wielokątów jest bardzo zróżnicowana.
* `Gładkie` - Wygładza powierzchnię. Przeciągnij w lewo, aby zamiast tego użyć `Wyostrzenie`.
* ![](/icons/group.webp) `Gładkie` - Wygładza granice między [grupami powierzchni](tools.md#facegroup), prostując postrzępione kontury grup. Przeciągnij w lewo, aby je wyostrzyć.
* `Złagodź` - Wyrównuje wielokąty, zachowując kształt.
* ![](/icons/group.webp) `Złagodź` - Łagodzi wielokąty wzdłuż granic grup powierzchni.
* `Zachowaj narożniki` - Przy `Gładkie` i `Złagodź` dla grup powierzchni granice pozostają nieruchome tam, gdzie skręcają bardziej niż o ten kąt, więc narożniki zostają ostre, a boki się wygładzają. Włączasz to jego polem wyboru.

## Poleruj {#polish}

Spłaszcza powierzchnię w czyste fasety, jak narzędzie [Poleruj](tools.md#polish). `Kąt` określa, które ścianki spłaszczają się razem: ścianki zagięte o mniej niż ten kąt tworzą jedną fasetę. Mniejszy kąt zachowuje więcej zagięć i mniejsze fasety.

## Napełnij {#inflate}

Wypycha powierzchnię na zewnątrz wzdłuż jej normalnych albo do środka, gdy przeciągasz w lewo. `Normalna (Złagodź)` jednocześnie łagodzi wielokąty, aby się nie rozciągały; możesz to wyłączyć jego polem wyboru.

## Korekta kolorów {#color-adjustments}

Wybierz kanał do korekty: `Kolor`, `Chropowatość`, `Metaliczność`, `Krycie`, `Gęstość` (malowanie gęstości dla [Quad Remesher](tools.md#quad-remesher), jeśli obiekt je ma) lub `Maska`, a następnie:

* `Ekspozycja` - Rozjaśnia lub przyciemnia wartości.
* `Nasycenie` - (Tylko `Kolor`) Kolory bardziej lub mniej żywe.
* `Kontrast` - Oddala wartości od siebie albo je do siebie zbliża.
* `Odcień` - Przesuwa kolory po kole barw.

## Rozmycie {#blur}

Rozmywa wybrane kanały na całej powierzchni: włącz `Kolor`, `Chropowatość`, `Metaliczność`, `Krycie`, `Gęstość` lub `Maska`, a potem przeciągnij `Rozmycie`. Przeciągnij w lewo, aby zamiast tego użyć `Wyostrzenie`.

W przypadku maski działa to tak samo jak suwak `Rozmycie` narzędzia [Maska](tools.md#mask). Tutaj możesz jednak rozmywać także kanały malowania.
