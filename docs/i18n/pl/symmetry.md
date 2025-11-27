# ![](/icons/symmetry.webp) Symetria

To menu kontroluje, w jaki sposób pociągnięcia pędzla będą powielane względem płaszczyzny lustrzanej lub promieniowo, oraz umożliwia przywrócenie symetrii w obiektach niesymetrycznych.

![](/images/symmetry_overview.webp) 

## Przegląd 
Symetrii możesz używać na kilka sposobów:

* Jako lustra, odbijając pracę względem osi X (lewo/prawo), Y (góra/dół), Z (tył/przód) lub ich kombinacji. 
* Symetria promieniowa może być ustawiona na osiach X Y Z z określoną liczbą powtórzeń, np. rzeźbienie rozgwiazdy. 
* Lustra mogą działać względem początku układu współrzędnych (tryb świata, *world mode*) lub względem środka obiektu (tryb lokalny, *local mode*).
* Rzeźby, które zaczęły jako niesymetryczne, mogą zostać wymuszone na symetryczne.

Skrót do włączania/wyłączania symetrii znajduje się również w lewym panelu szybkiego dostępu (*„Sym”*). Małe „L/W” wskazuje, czy Nomad jest w trybie symetrii lokalnej (Local) czy światowej (World). Możesz także przytrzymać dłużej lub przesunąć palcem do środka ekranu, aby wywołać menu.

![](/images/symmetry_button.webp) 

Jest to opcja globalna, więc jej stan przenosi się między różnymi narzędziami.
Jedynymi wyjątkami są narzędzia transformacji ([Move](#translate), [Rotate](#rotate), [Scale](#scale) i [Gizmo](#gizmo)), które mają własny stan symetrii.

::: tip
Menu symetrii służy głównie do kontrolowania symetrii pociągnięć. Możesz także odbijać i powielać obiekty za pomocą [repeaterów dostępnych w menu sceny](scene#repeaters). 
:::

## Enabled
Przełącza tryb lustrzany, to samo co przycisk `Sym` w lewym panelu szybkiego dostępu. 

## Planes

Włącz płaszczyznę(-ny) symetrii oraz ustaw liczbę powtórzeń dla symetrii promieniowej. Zauważ, że nie musisz wybierać tylko jednej płaszczyzny – możesz mieć włączone 1, 2 lub 3 płaszczyzny dla złożonej symetrii.

Oś i liczba powtórzeń dla symetrii promieniowej. Zauważ, że one również nie są ograniczone do pojedynczej osi i mogą działać w połączeniu z symetrią względem płaszczyzn, aby bardzo szybko generować szczegółowe rezultaty. (Łączna liczba powtórzeń jest ograniczona do 150)

![](/videos/symmetry_demo.mp4) 

## Method
Lustro może być „Local” i poruszać się razem z obiektem, albo „World” i pozostawać nieruchome. Jeśli nie masz pewności, którego trybu potrzebujesz, obserwuj płaszczyznę lustrzaną i wskaźniki promieniowe nałożone na obiekt. W trybie lokalnym, gdy użyjesz gizma transformacji i przesuniesz model, wskaźniki lustrzane również się przesuną. W trybie światowym wskaźniki pozostaną nieruchome, a obiekt będzie się przez nie przesuwał.

## Mirroring
![](/images/symmetry_mirroring.webp)

Podczas rzeźbienia w pobliżu płaszczyzn symetrii niektóre pędzle mogą zachowywać się niesymetrycznie. Ta sekcja pozwala przywrócić symetrię poprzez skopiowanie jednej strony rzeźby na drugą. 

`Direction` – przyciski `<<` i `>>` określają, która strona zostanie skopiowana na drugą. Nomad oblicza to na podstawie bieżącego widoku, więc ustawienie `<<` na przykład zawsze skopiuje z prawej strony ekranu na lewą.

![](/icons/shield.webp) `Mask` – przycisk maski pozwala odizolować to, co będzie lustrzane; zamaskowanie strony docelowej ochroni ten obszar, a zamaskowanie strony źródłowej uniemożliwi odbicie tego obszaru na stronę docelową. 

![](/icons/tool_hide.webp) `Hide` – gdy jest aktywne, obszary ukryte po stronie źródłowej nie zostaną odbite na stronę docelową. 

`Mirror` spróbuje zidentyfikować, czy topologia po obu stronach lustra jest taka sama, a jeśli tak, po prostu przesunie wierzchołki. To bardziej typowy scenariusz.

`Split & Mirror` zasadniczo przetnie obiekt wzdłuż lustra, skopiuje jedną stronę, odbije ją na drugą i zespawa wierzchołki wzdłuż lustra. Jest to opcja bardziej destrukcyjna i usunie wielorozdzielczość (multiresolution), ale czasem ta metoda jest wymagana, jeśli model bardzo różni się po obu stronach lustra.

### Flip object
![](/images/symmetry_flip.webp)
Zamienia lewą stronę z prawą i odwrotnie. Efekt wizualnie podobny do użycia menu narzędzia gizmo i ustawienia skali na -1 na osi X.

## Reset and Edit

![](/images/symmetry_edit.webp)

Możliwe jest edytowanie położenia i orientacji symetrii (choć nie jest to zalecane!). W razie potrzeby `World center` i `Orientation` zresetują położenie i orientację symetrii do wartości domyślnych.

Nomad zazwyczaj wie, gdzie umieścić płaszczyznę symetrii. Nie zaleca się ręcznej regulacji, ale przycisk `Gizmo (Edit)` umożliwia to zaawansowanym użytkownikom. Po kliknięciu tego przycisku pojawia się gizmo, które pozwala przesuwać i obracać płaszczyznę symetrii. Jeśli chcesz przywrócić domyślny środek i orientację, zrobią to przyciski `object center` i `orientation`.

Zachowanie tych opcji zmienia się w zależności od przestrzeni (*Local/World*), w której się znajdujesz.
Jeśli więc nie działa to tak, jak się spodziewasz, upewnij się, że jesteś w odpowiedniej przestrzeni.

::: tip
Przycisk `Gizmo (Edit)` jest celowo wyszarzony jako przypomnienie, że prawdopodobnie nie powinieneś go używać!
:::

## Show options
![](/images/symmetry_show.webp)


`Show line` i `Show plane` przełączają nakładkę w widoku, pokazującą położenie symetrii. Zauważ, że wyłączenie tych opcji zadziała dopiero po zamknięciu menu symetrii.
