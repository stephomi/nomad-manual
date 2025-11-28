# ![](/icons/cog.webp) Ustawienia {#reset-to-default}

Menu ustawień zawiera wiele opcji kontrolujących wygląd i zachowanie Nomad.

![](/images/settings_overview.webp)

## Ustawienia wyświetlania {#display-settings}
Ta sekcja zawiera skróty szybkiego uruchamiania do większości ustawień znajdujących się niżej w tym menu.

![](/images/settings_display_settings.webp)

### Gładkie cieniowanie {#smooth-shading}
Przełączanie między gładkim a fasetowym cieniowaniem. Przy cieniowaniu fasetowym poligony są cieniowane niezależnie, dzięki czemu widać ich topologię.
Może być przydatne oglądanie fasetowego cieniowania podczas rzeźbienia, a następnie przełączenie na gładkie cieniowanie do renderingu.

Wyłączenie gładkiego cieniowania nieco poprawia wydajność.

### Obrys {#outline-quick}
Przełącz obrys aktualnie zaznaczonego obiektu.

Jest to przydatne, aby uzyskać wizualną informację zwrotną o aktualnie zaznaczonej siatce(-ach) w przypadku, gdy [Przyciemnij niezaznaczone](#darken-unselected-objects) jest wyłączone.

Z punktu widzenia wydajności używanie [Przyciemnij niezaznaczone](#darken-unselected-objects) jest znacznie lepsze niż używanie obrysu.

### Siatka {#grid-quick}
Przełącz siatkę w tle, przydatną do zrozumienia położenia i skali obiektów.

### Dwustronne {#two-sided-quick}
Przełącz dwustronne wyświetlanie poligonów. Wszystkie ściany są skierowane w pewnym kierunku.
Ściany uznawane za *tylną stronę* to te, które są skierowane „od” punktu widzenia kamery.

Na przykład startowa prosta kula ma ściany skierowane na zewnątrz.
Jeśli przesuniesz kamerę do wnętrza kuli, zobaczysz tylną stronę tych ścian.

Najczęściej nie powinieneś widzieć tylnej strony ścian, więc ich kolorowanie może pomóc wykryć potencjalne problemy lub nieprawidłową topologię.

Wyłączenie renderowania `dwustronnego` może nieco poprawić wydajność renderowania.


### Szkielet (Wireframe) {#wireframe-quick}
Przełącz nakładkę szkieletu siatki. 

Pamiętaj, że włączenie szkieletu obniży wydajność.

### Kostka wyrównania (Snap cube) {#snap-cube-quick}
Przełącz pomocniczą ikonę w rogu sceny, przydatną do orientowania się w przestrzeni i szybkiego przełączania między widokami przód/tył/lewo/prawo/góra/dół.

### Pokaż malowanie {#show-painting}
Przełącz wyświetlanie malowania. Domyślnie używany jest biały, niemetaliczny materiał o szorstkości 25%.

### Użyj ukrywania {#use-hide}
Przełącz tryb ukrywania. Gdy jest wyłączony, nadal istnieje, tylko jest nieaktywny. Ten przycisk jest wyłączony, jeśli aktualnie używasz narzędzia ukrywania.

### Pokaż maskę {#show-mask}
Przełącz tryb maski. Gdy jest wyłączony, nadal istnieje, tylko jest nieaktywny. Naciśnij ten przycisk ponownie, aby go ponownie włączyć.

Jeśli musisz ukryć maskę I nadal mieć ją aktywną, użyj koloru maski poniżej i ustaw go na biały. Pamiętaj, aby po zakończeniu zmienić go z powrotem na szary!

Zwróć uwagę, że ten przycisk jest wyłączony, jeśli aktualnie używasz narzędzia maski. 

### Maska -> Nieprzezroczysta {#mask-opaque}
Maska -> nieprzezroczysta zignoruje przezroczyste wierzchołki dla zamaskowanej maski. Ma to znaczenie tylko dla przezroczystości wierzchołków i tekstur; ściany ukryte przez „ukryj” nadal będą ukryte.

### Podświetlenie {#highlight-quick}
Przełącz błysk podświetlenia zaznaczenia. Przy zaznaczaniu obiektów wybrany obiekt jest tymczasowo podświetlany jaskrawym różem przez 500 milisekund. Kolor i długość błysku można dostosować poniżej.

### Statystyki {#stats-quick}
Przełącz wyświetlanie tekstu statusu w widoku 3D. Wyświetla on informacje o pamięci systemowej, całkowitej liczbie wierzchołków w scenie oraz liczbie wierzchołków aktualnego zaznaczenia.

----- 

### Przyciemnij niezaznaczone obiekty {#darken-unselected-objects}
Obiekty, które nie są zaznaczone, zostaną przyciemnione, aby aktualne zaznaczenie bardziej się wyróżniało.

### Maska {#mask}
Kolor używany do maskowania, domyślnie średnia szarość, mnożony przez kolor obiektu. Ustaw na biały, aby maska była niewidoczna, ale pamiętaj, aby po zakończeniu zmienić go z powrotem na szary!

## ![](/icons/cursor.webp) Kursor {#cursor}

### Pokaż okrąg podczas rzeźbienia {#show-circle-while-sculpting}
Kontynuuj wyświetlanie promienia pędzla podczas rzeźbienia.

### Pokaż małą kropkę {#show-small-dot}
Wyświetl kropkę w centrum pociągnięcia pędzla podczas rzeźbienia lub gdy zmieniany jest punkt obrotu kamery.

### Pokaż stabilizator liny {#show-rope-stabilizer}
Rysuj linię wskazującą długość liny, gdy w ustawieniach pociągnięcia aktywny jest stabilizator „lazy rope”.

## ![](/icons/cursor.webp) Wskaźnik {#indicator}
![](/images/settings_indicator.webp)

Wyświetlaj wizualny wskaźnik(-i) na potrzeby samouczków i nagrań ekranu.

Przyciski `Finger`, `Stylus` i `Mouse` włączą wyświetlanie ikony, gdy wykryty zostanie dany typ wejścia.

### Kolor {#indicator-color}
Kolor wskaźnika.

### Rozmiar/Ikona/Okrąg {#indicator-shape}
Elementy sterujące do regulacji rozmiaru wskaźnika i kształtów wewnątrz wskaźnika.

## ![](/icons/wireframe.webp) Szkielet (Wireframe) {#wireframe}
![](/images/settings_wireframe.webp)
Aktywuj nakładkę szkieletu siatki.

### Cel {#target}
Ustaw, czy szkielet będzie widoczny dla obiektów niezaznaczonych, tylko zaznaczonych, czy wszystkich obiektów.

### Ukryj {#hide}
Ustaw, czy szkielet będzie nadal wyświetlany dla ukrytych poligonów.

### Multiresolution: tylko poziom 0 {#multiresolution-level-0-only}
Multiresolution wyświetla szkielety dla poziomu 0 ciemniejsze, a wyższe poziomy stopniowo jaśniejsze. Po włączeniu tej opcji wyświetlany będzie tylko szkielet poziomu 0.

### Kolor {#wireframe-color}
Ustaw kolor i przezroczystość szkieletu.

## ![](/icons/grid.webp) Siatka {#grid}
![](/images/settings_grid.webp)
Aktywuj siatkę.

### Kolor {#grid-color}
Ustaw kolor i przezroczystość siatki.

### Przyciąganie {#snap}
Włącz przyciąganie do siatki dla narzędzi opartych na krzywych.

## ![](/icons/culling.webp)Two sided {#two-sided}
Włącz widoczność ścian poligonów z obu stron.

### Kolor tylnej ściany, kolor tylnej ściany {#backface-color}
Włącz barwienie tylnej strony ścian oraz ustaw kolor tego zabarwienia.

## ![](/icons/outline.webp)Outline {#outline}
Włącz obrys wokół aktywnego obiektu.

### Kolor obrysu, grubość {#outline-color-thickness}
Ustaw kolor i grubość obrysu.


## ![](/icons/bang.webp) Podświetlenie {#highlight}
Włącz krótki błysk, gdy aktywny obiekt zostanie zmieniony.
### Kolor, czas trwania {#color-duration}
Ustaw kolor i czas trwania błysku w milisekundach.

## ![](/icons/snap_cube.webp) Kostka wyrównania (Snap cube) {#snap-cube}
![](/images/settings_snapcube.webp)

Wyświetl pomocniczą ikonę w rogu sceny, przydatną do szybkiego przełączania między widokami przód/tył/lewo/prawo/góra/dół. Stuknij w boki kostki, aby przełączać się między widokami ortograficznymi.

### Kształt {#shape}
Wybierz między kostką, kulą lub kształtem gnomonu dla kostki przyciągania.

### Ogranicz wyrównanie {#restrict-alignment}
Włącz blokadę obrotu kamery podczas przeciągania na kostce przyciągania. Gdy jest aktywna, ruch przeciągania na kostce będzie odbywał się tylko w lewo/prawo lub góra/dół.

### Rozmiar {#size}
Ustaw rozmiar kostki przyciągania.

### Obróć o 180 {#flip-180}
Włącz zachowanie stuknięcia tak, aby jeśli widok jest przyciągnięty, stuknięcie w środek kostki obróciło widok o 180 stopni. Na przykład, jeśli widok jest przyciągnięty do przodu, stuknięcie kostki widoku obróci go do widoku z tyłu.

### Pozycja {#snap-position}
Ustaw, w którym rogu będzie znajdować się kostka przyciągania.


## ![](/icons/edit_radius_n.webp) Statystyki {#stats}
![](/images/settings_stats.webp)

Wyświetl informacje o pamięci systemowej, całkowitej liczbie wierzchołków w scenie oraz liczbie wierzchołków aktualnego zaznaczenia.

### Pozycja {#stats-position}
Ustaw, w którym rogu będą wyświetlane statystyki.

## Prymityw/Powielacze {#primitive-repeaters}
## Wejście numeryczne {#gizmo-input}
Zezwól na wprowadzanie wartości liczbowych po stuknięciu w uchwyty gizma.

## Multiresolution {#multires}
### Maksymalna liczba wierzchołków {#multires-lowres-count}
Ustaw próg, powyżej którego nie będzie można wykonać operacji podziału multires powyżej tej liczby poligonów, co prawdopodobnie spowodowałoby awarię Nomad. Domyślnie jest to 10 milionów.
### Próg niskiej rozdzielczości {#multires-lowres-threshold}
Niższa rozdzielczość siatki może być wyświetlana podczas poruszania kamerą. Możesz zwiększyć tę wartość, jeśli chcesz wyświetlać siatkę w wyższej rozdzielczości.

## Ustawienia {#advanced}
### Przywróć domyślne {#reset}
Przywróć wszystkie ustawienia do wartości domyślnych.