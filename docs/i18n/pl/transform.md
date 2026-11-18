# ![](/icons/transform.webp) Przekształcenie {#transform}

To menu pokazuje przekształcenie zaznaczonego obiektu w postaci liczb: gdzie się znajduje, jak jest obrócony i przeskalowany oraz jak duży jest. Możesz wpisać dokładne wartości, wyzerować je albo zastosować je do siatki.

![](/images/transform_overview.webp)

## Przegląd {#overview}

Każdy obiekt ma, oprócz wierzchołków, węzeł, który przechowuje jego translację, obrót i skalę (jego macierz). Narzędzia [Gizmo](tools.md#gizmo) i [Przekształcenie](tools.md#transform) zmieniają tę macierz, gdy przeciągasz w widoku; to menu pozwala ją odczytać i wpisać wartości ręcznie. Różnicę między przesuwaniem węzła a przesuwaniem wierzchołków wyjaśnia sekcja [Węzły i wierzchołki](tools.md#nodes-and-vertices).

Przeciągnij wartość w lewo lub w prawo, aby ją zmienić, albo stuknij ją, aby wpisać liczbę. Wartości X, Y i Z są zabarwione na czerwono, zielono i niebiesko, jak osie gizmo.

::: tip
Wpisywanie wartości przydaje się do precyzyjnego rozmieszczania obiektów, na przykład aby ustawić kilka części na dokładnie tej samej wysokości albo przywrócić okrągłą wartość obrotu po swobodnym obracaniu gizmo.
:::

## Macierz {#matrix}

Tytuł mówi, w jakiej przestrzeni wyrażone są wartości: `lokalna` (względem obiektu nadrzędnego) lub `świat`.

### Obiekt i punkt obrotu {#object-pivot}

* `Obiekt` - Wartości to własne przekształcenie obiektu.
* `Pkt obrotu` - Wartości sterują zaznaczeniem od jego [punktu obrotu](tools.md#pivot), tak samo jak uchwyty gizmo: wiersze pokazują zero, a ich zmiana przesuwa, obraca lub skaluje zaznaczenie wokół punktu obrotu. Włącz `Edytuj` (ikona kłódki), aby przesuwać sam punkt obrotu, podczas gdy obiekty stoją w miejscu.

### Lokalna i świat {#local-world}

Gdy obiekt ma obiekt nadrzędny lub podrzędne albo zaznaczonych jest kilka obiektów, możesz wybrać, w jakiej przestrzeni pokazywać wartości: `Lokalna` (względem obiektu nadrzędnego) lub `Świat`.

### Operacje {#actions}

| Operacja          | Ikona                         | Opis |
| :-----------: | :---------------------------: | :---------- |
| Przenieś początek | ![](/icons/target.webp)      | Przenosi obiekt do początku układu świata. |
| Zastosuj      | ![](/icons/bake.webp)        | Stosuje macierz do wierzchołków i zeruje macierz. Wizualnie nic się nie zmienia, ale początek obiektu jest teraz początkiem układu świata. |
| Pkt obrotu    | ![](/icons/gizmo.webp)       | Zapisuje punkt obrotu w obiekcie: początek i orientacja obiektu stają się początkiem i orientacją punktu obrotu. Wizualnie nic się nie zmienia. |
| Edytuj        | ![](/icons/lock.webp)        | (Tryb `Pkt obrotu`) Przesuwa sam punkt obrotu. |
| Wyzeruj       | ![](/icons/reset.webp)       | Zeruje przekształcenie do tożsamości. W trybie `Pkt obrotu` zamiast tego przywraca punkt obrotu na miejsce. |

Gdy zaznaczony obiekt ma instancje, zastosowanie wymaga potwierdzenia i oferuje opcję `Anuluj instancję`: zastosowanie zmienia wierzchołki, które są wspólne dla instancji.

### Translacja, obrót, skala {#translation-rotation-scale}

Położenie, obrót (w stopniach) i skala obiektu na osiach X, Y i Z. Dwa przyciski na końcu każdego wiersza stosują do wierzchołków tylko tę część przekształcenia albo ją zerują.

Wiersz `Ścinanie` pojawia się też, gdy obiekt jest pochylony, na przykład po niejednolitym skalowaniu obróconego obiektu nadrzędnego.

### Jednolite skalowanie {#uniform-scale}

Gdy ta opcja jest włączona, skala jest jedną wartością, taką samą na wszystkich trzech osiach. Wyłącz ją, aby skalować X, Y i Z osobno.

## Wymiary {#dimension}

Rozmiar i środek prostopadłościanu otaczającego zaznaczenie, w jednostkach świata. Gdy zaznaczonych jest kilka obiektów, obejmuje je wszystkie.

* `Rozmiar` - Szerokość, wysokość i głębokość. Gdy przycisk łącza jest włączony, zmiana jednego wymiaru skaluje dwa pozostałe o tyle samo, zachowując proporcje.
* `Wyśrodkowany` - Środek prostopadłościanu otaczającego. Przycisk celownika przesuwa zaznaczenie tak, aby jego środek znalazł się w początku układu świata.

::: tip
`Rozmiar` to najszybszy sposób, aby nadać obiektowi rzeczywiste wymiary, na przykład przed drukiem 3d: ustaw żądaną wysokość, a łącze zachowa proporcje.
:::
