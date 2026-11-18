# ![](/icons/cog.webp) Ustawienia {#reset-to-default}

Menu ustawień zawiera wiele opcji, które określają wygląd i działanie Nomad.

![](/images/settings_overview.webp)

Rząd przycisków u góry menu przenosi od razu do wybranej sekcji: `Kursor`, `Wskaźnik`, `Drut`, `Siatka`, `Dwustronny`, `Kontur`, `Wyróżnianie`, `Nawigator`, `Statystyki`, `Uchwyty`, `Kształt`, `Repeatery` i `Multirezolucja`.

## Ustawienia wyświetlania {#display-settings}
Ta sekcja zawiera skróty do większości ustawień opisanych niżej w tym menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Płynne cieniowanie {#smooth-shading}
Przełącza między cieniowaniem płynnym i fasetowym. Przy cieniowaniu fasetowym wielokąty są cieniowane niezależnie, więc widać topologię siatki.
Cieniowanie fasetowe przydaje się na etapie rzeźbienia, a do renderowania możesz przełączyć się na płynne.

Wyłączenie płynnego cieniowania nieznacznie poprawia wydajność.

### ![](/icons/outline.webp) Kontur {#outline-quick}
Włącza lub wyłącza kontur wokół bieżącego zaznaczenia.

Przydaje się, aby widzieć, które siatki są zaznaczone, gdy opcja [Przyciemnij niezaznaczone](#darken-unselected-objects) jest wyłączona.

Pod względem wydajności opcja [Przyciemnij niezaznaczone](#darken-unselected-objects) jest znacznie lepsza niż kontur.

### ![](/icons/grid.webp) Siatka {#grid-quick}
Włącza lub wyłącza siatkę w tle, która pomaga ocenić położenie i skalę obiektów.

### ![](/icons/culling.webp) Dwustronny {#two-sided-quick}
Włącza lub wyłącza wyświetlanie wielokątów z obu stron. Każda ścianka jest skierowana w określoną stronę.
Ścianki uznawane za *tylne* to te, które są zwrócone „od” punktu widzenia kamery.

Na przykład ścianki prostej kuli startowej są skierowane na zewnątrz.
Jeśli przesuniesz kamerę do wnętrza kuli, zobaczysz tylne strony tych ścianek.

Zwykle tylne strony ścianek nie powinny być widoczne, więc ich pokolorowanie pomaga wykryć potencjalne problemy lub nieprawidłową topologię.

Wyłączenie renderowania `Dwustronny` może nieco poprawić wydajność renderowania.


### ![](/icons/wireframe.webp) Szkielet {#wireframe-quick}
Włącza lub wyłącza nakładkę szkieletu.

Pamiętaj, że włączenie szkieletu obniża wydajność.

### ![](/icons/navigator.webp) Nawigator {#snap-cube-quick}
Włącza lub wyłącza ikonę pomocniczą w rogu sceny, która ułatwia orientację w przestrzeni i szybkie przełączanie między widokami z przodu, z tyłu, z lewej, z prawej, z góry i z dołu.

### ![](/icons/palette.webp) Pokaż malowanie {#show-painting}
Włącza lub wyłącza wyświetlanie malowania. Gdy jest wyłączone, obiekty są wyświetlane z białym, niemetalicznym materiałem o chropowatości 25%, zamiast ich malowania.

### ![](/icons/tool_hide.webp) Użyj funkcji Ukryj {#use-hide}
Włącza lub wyłącza tryb ukrywania. Po wyłączeniu ukrycie nadal istnieje, jest tylko nieaktywne. Ten przycisk jest niedostępny, gdy używasz narzędzia ukrywania.

### ![](/icons/shield.webp) Pokaż maskę {#show-mask}
Włącza lub wyłącza tryb maski. Po wyłączeniu maska nadal istnieje, jest tylko nieaktywna. Naciśnij ten przycisk ponownie, aby ją przywrócić.

Jeśli chcesz ukryć maskę, ALE zachować jej działanie, ustaw poniżej kolor maski na biały. Pamiętaj, aby potem przywrócić szary!

Ten przycisk jest niedostępny, gdy używasz narzędzia maski.

### ![](/icons/shield.webp) Maska → Nieprzezroczysty {#mask-opaque}
`Maska → Nieprzezroczysty` ignoruje przezroczyste wierzchołki w zamaskowanym obszarze. Dotyczy to tylko krycia wierzchołków i tekstur: ścianki ukryte funkcją „ukryj” pozostają ukryte. Opcja jest dostępna tylko wtedy, gdy włączone jest `Pokaż maskę`.

### ![](/icons/bang.webp) Wyróżnianie {#highlight-quick}
Włącza lub wyłącza błysk wyróżnienia zaznaczenia. Przy zaznaczaniu obiektów zaznaczony obiekt na chwilę błyska przez 500 milisekund. Kolor i długość błysku możesz zmienić poniżej.

### ![](/icons/list.webp) Statystyki {#stats-quick}
Włącza lub wyłącza tekst stanu w widoku 3d. Pokazuje on informacje o pamięci systemu, łącznej liczbie wierzchołków w scenie i liczbie wierzchołków bieżącego zaznaczenia.

----- 

### ![](/icons/cube.webp) Przyciemnij niezaznaczone obiekty {#darken-unselected-objects}
Niezaznaczone obiekty są przyciemniane, aby bieżące zaznaczenie się wyróżniało.

### ![](/icons/shield.webp) Maska {#mask}
Kolor maskowania, domyślnie średnioszary, mnożony z kolorem obiektu. Ustaw go na biały, aby maska była niewidoczna, ale pamiętaj, aby potem przywrócić szary!

## ![](/icons/cursor.webp) Kursor {#cursor}

### Okrąg {#show-circle-while-sculpting}
Kiedy pokazywać okrąg promienia pędzla:

* `Auto` - pokazuje okrąg, ale ukrywa go podczas rzeźbienia.
* `Nie` - nigdy nie pokazuje okręgu.
* `Tak` - zawsze pokazuje okrąg, także podczas rzeźbienia.

### Pokaż małą kropkę {#show-small-dot}
Wyświetla kropkę w środku pociągnięcia pędzla podczas rzeźbienia albo gdy zmienia się punkt obrotu kamery.

### Pokaż stabilizator liny {#show-rope-stabilizer}
Rysuje linię pokazującą długość liny, gdy w ustawieniach pociągnięcia aktywny jest [Stabilizator powolnej liny](stroke.md#lazy-rope-stabilizer).

### Pokaż wskazówkę przechyłu {#show-roll-hint}
Pokazuje prowadnicę kierunku przechyłu, gdy używasz skrótu klawiszowego przechyłu.

### ![](/icons/radius.webp) Rozmiar {#dot-size}
Rozmiar małej kropki.

### Kolory {#cursor-colors}
Kursor zmienia kolor w zależności od tego, co robisz: `Rzeźbienie`, `Tło` (gdy kursor jest nad tłem), `Maska`, `Gładkie`, `Kamera` i `Promień`. Każdy z tych kolorów możesz tutaj dostosować.

## ![](/icons/cursor.webp) Wskaźnik {#indicator}
![](/images/settings_indicator.webp)

Wyświetla wskaźniki wizualne na potrzeby poradników i nagrań ekranu. Ustaw na `Tak`, aby go włączyć (na iOS jest też opcja `Auto`).

Przyciski `Palec`, `Piórko` i `Mysz` włączają wyświetlanie ikony po wykryciu danego rodzaju wejścia.

### Kolor {#indicator-color}
Kolor wskaźnika.

### Rozmiar/ikona/okrąg {#indicator-shape}
Ustawienia rozmiaru wskaźnika oraz krycia ikony i okręgu we wskaźniku.

## ![](/icons/wireframe.webp) Szkielet {#wireframe}
![](/images/settings_wireframe.webp)
Włącza nakładkę szkieletu.

### Cel {#target}
Określa, czy szkielet pokazują niezaznaczone obiekty, tylko zaznaczone obiekty, czy wszystkie obiekty.

### Ukryj {#hide}
Określa, czy szkielet jest nadal wyświetlany dla ukrytych wielokątów.

### Multirezolucja: tylko poziom 0 {#multiresolution-level-0-only}
Multirezolucja wyświetla szkielet poziomu 0 ciemniej, a wyższe poziomy coraz jaśniej. Gdy ta opcja jest włączona, wyświetlany jest tylko szkielet poziomu 0.

### Kolor {#wireframe-color}
Ustawia kolor i krycie szkieletu.

## ![](/icons/grid.webp) Siatka {#grid}
![](/images/settings_grid.webp)
Włącza siatkę.

### Przyciągnij {#snap}
Te opcje sprawiają, że punkty narzędzi opartych na krzywych i kształtach (`Bryła obrotowa`, `Rura`, kształty wielokątów i ścieżek...) są przyciągane podczas rysowania:

* `Przyciągaj do siatki` - przyciąga do siatki.
* `Przyciągaj do punktów (widok wyrównany)` - przyciąga do pobliskich istniejących punktów, gdy kamera jest wyrównana do osi.
* `Przyciągaj do punktów (widok dowolny)` - przyciąga do pobliskich istniejących punktów, gdy kamera nie jest wyrównana.

### Kolor {#grid-color}
Ustawia kolor i krycie siatki. Te opcje pojawiają się, gdy siatka jest widoczna.

`Winieta` stopniowo wygasza siatkę w stronę jej krawędzi. `Próg podziału siatki` określa w pikselach, jak gęsto linie siatki mogą leżeć na ekranie, zanim siatka przełączy się na inny poziom podziału.

## ![](/icons/culling.webp)Dwustronny {#two-sided}
Pozwala widzieć ścianki wielokątów z obu stron.

### Kolor tylnej powierzchni {#backface-color}
`Kolorowa powierzchnia tylna` włącza zabarwienie tylnych stron ścianek, a `Kolor tylnej powierzchni` ustawia kolor zabarwienia.

## ![](/icons/outline.webp)Kontur {#outline}
Włącza kontur wokół zaznaczonych obiektów.

### Kolor konturu, grubość {#outline-color-thickness}
Ustawia kolor i `Grubość` konturu.


## ![](/icons/bang.webp) Wyróżnianie {#highlight}
Włącza krótki błysk przy zmianie zaznaczenia.
### Kolor, czas trwania {#color-duration}
Ustawia kolor i czas trwania błysku w milisekundach.

## ![](/icons/navigator.webp) Nawigator {#snap-cube}
![](/images/settings_snapcube.webp)

Wyświetla ikonę pomocniczą w rogu sceny, która pozwala szybko przełączać się między widokami z przodu, z tyłu, z lewej, z prawej, z góry i z dołu. Stuknij jego boki, aby przełączać się między widokami ortograficznymi.

### Kształt {#shape}
Wybierz kulę, sześcian albo gnomon jako kształt nawigatora.

### Ogranicz wyrównanie {#restrict-alignment}
Wyrównuje widoki przyciągania do osi świata. Gdy ta opcja jest włączona, możliwych jest tylko 6 głównych widoków. Przy `Auto` to ograniczenie działa tylko wtedy, gdy kamera jest w trybie `Obrotnica`.

### Rozmiar {#size}
Ustawia rozmiar nawigatora.

### Obróć o 180° {#flip-180}
Włącza takie działanie stuknięcia, że gdy widok jest przyciągnięty, stuknięcie środka nawigatora obraca widok o 180 stopni. Na przykład gdy widok jest przyciągnięty z przodu, stuknięcie nawigatora obraca go do widoku z tyłu.

### Krawędzie i narożniki {#edges-corners}
Dodaje widoki przyciągania na krawędziach i narożnikach (bursztynowe strefy). Niedostępne dla kształtu gnomona.

### Przeciąganie w trybie obrotnicy {#turntable-drag}
Przeciąganie nawigatora obraca widok bez przechylania kamery i zatrzymuje się na każdym widoku przyciągania. Wyłącz tę opcję, aby przeciągać nawigator z obrotem `Trackball`. W obu przypadkach przeciąganie odbywa się poziomo lub pionowo. Przy kamerze w trybie `Obrotnica` nawigator zawsze przeciąga się w ten sposób.

### Pozycja {#snap-position}
Określa, w którym rogu znajduje się nawigator.


## ![](/icons/list.webp) Statystyki {#stats}
![](/images/settings_stats.webp)

Wyświetla informacje o pamięci systemu, łącznej liczbie wierzchołków w scenie i liczbie wierzchołków bieżącego zaznaczenia.

### Pozycja {#stats-position}
Określa, w którym rogu wyświetlane są statystyki.

## ![](/icons/edit_radius.webp) Uchwyt {#handle}
Ustawienia uchwytów przeciąganych w widoku, takich jak gizmo.

### Wprowadzanie numeryczne {#gizmo-input}
Pozwala wpisywać wartości liczbowe po stuknięciu jednego z elementów sterujących gizmo.

### Ukryj przy interakcji {#hide-on-interaction}
Wygasza gizmo podczas korzystania z niego, aby nie przeszkadzało.

### ![](/icons/opacity.webp) Krycie {#handle-opacity}
Krycie uchwytów.

## ![](/icons/shape_lasso.webp) Kształt {#shape-settings}
Jak na ekranie wyglądają kształty rysowane pociągnięciami kształtów (lasso, prostokąt, krzywa...).

### ![](/icons/opacity.webp) Wypełnienie, obrys {#shape-fill-outline}
Krycie wnętrza kształtu i linii wokół niego.

### Kolory {#shape-colors}
Kolor kształtu dla każdego rodzaju narzędzia: `Maska`, `Ukryj`, `Grupa powierzchni` i `Przytnij`.

## ![](/icons/array.webp) Repeatery {#primitive-repeaters}
Limity kopii tworzonych przez [repeatery](scene#repeaters) (szyk, radialny, krzywa, powierzchnia). Dzięki nim Nomad pozostaje responsywny, gdy repeater wymknie się spod kontroli.

### ![](/icons/cube.webp) Maks. kopii {#repeater-max-copies}
Największa liczba kopii tworzonych przez jeden repeater. Nomad źle radzi sobie z dużą liczbą obiektów, bez względu na ich rozmiar.

### ![](/icons/cube.webp) Kopie w scenie {#repeater-scene-copies}
Limit kopii dla całej sceny. Kopia o małej liczbie wielokątów kosztuje niewiele geometrii, ale nadal jest pełnym obiektem, więc małe kopie osiągają najpierw właśnie ten limit.

### ![](/icons/triangle.webp) Maks. liczba powierzchni {#repeater-max-faces}
Limit ścianek dla wszystkich kopii w scenie. Po jego przekroczeniu kopie tracą najpierw najcięższe obiekty.

## ![](/icons/multires.webp) Multirezolucja {#multires}
### Maks. liczba wierzchołków {#multires-lowres-count}
Ustawia próg, powyżej którego operacja podziału multirezolucji nie jest dozwolona, bo taka liczba wierzchołków najpewniej spowodowałaby awarię Nomad: Nomad nie sprawdza dostępnej pamięci przed podziałem. Wartość domyślna to 10 milionów.
### Próg niskiej rozdzielczości {#multires-lowres-threshold}
Podczas poruszania kamerą może być wyświetlana siatka w niższej rozdzielczości. Możesz zwiększyć tę wartość, jeśli chcesz wyświetlać siatkę w wyższej rozdzielczości.

## Ustawienia {#advanced}
### ![](/icons/reset.webp) Przywróć domyślne {#reset}
Przywraca wszystkie preferencje aplikacji do wartości domyślnych.

Niektóre zasoby są zapisywane osobno i NIE są resetowane: projekty, skróty klawiszowe, ustawienia wstępne narzędzi, otoczenia HDR, MatCapy, alfy, tekstury pędzli i obrazy referencyjne. Wszystko, co jest zapisane w projekcie, na przykład oświetlenie, postprocessing czy widoki kamery, również pozostaje nienaruszone.
