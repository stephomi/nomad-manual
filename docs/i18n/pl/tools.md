# ![](/icons/toolbox.webp) Narzędzia {#tools}

![](/images/tools_menu.webp)

::: tip
Przejdź do [Narzędzia](#tools-1), aby zobaczyć opisy poszczególnych narzędzi.
:::

## Przegląd {#overview}

Narzędzia wybiera się z `Toolbox` po prawej stronie, a steruje się nimi za pomocą `Tool Controls` po lewej. Dodatkowe ustawienia znajdują się w menu `Settings`, pierwszej ikonie w prawym górnym rogu.

Narzędzia pędzla mają kontrolki rozmiaru i intensywności. Narzędzia zaznaczania mają kontrolki dla różnych stylów zaznaczania. Na dole panelu narzędzi znajdują się skróty do często używanych operacji (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Narzędzia Nomad są kolorystycznie oznaczone w toolboxie:

* <span class=brush>**Narzędzia pędzla**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Narzędzia przesuwania**</span> (Move, Drag)
* <span class=mask>**Narzędzia maskowania**</span> (Mask, SelMask)
* <span class=paint>**Narzędzia malowania**</span> (Paint, Smudge)
* <span class=flatten>**Narzędzia spłaszczania**</span> (Flatten, Planar)
* <span class=pinch>**Narzędzia ściskania**</span> (Crease, Pinch)
* <span class=selection>**Narzędzia oparte na zaznaczeniu**</span>, w których najpierw rysuje się 2D maskę, a potem wykonywana jest operacja (Trim, Split, Project)
* <span class=creation>**Narzędzia tworzenia**</span> (Tube, Lathe, Insert)
* <span class=transform>**Narzędzia transformacji**</span> (Transform, Gizmo)
* <span class=misc>**Różne narzędzia**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Narzędzie widoku**</span>



Wiele z tych narzędzi można dostosować pod względem zachowania pędzla, nacisku, tekstur itp. za pomocą menu [Stroke](stroke.md). 


### Sterowanie pędzlem {#brush-controls}

Lewy pasek narzędzi zawiera suwaki promienia i intensywności, a następnie specyficzne dla kategorii narzędzia kontrolki, opisane poniżej.

![](/images/tool_left_panel.webp)

::: tip
Suwak intensywności dla wielu narzędzi może przekraczać 100%, warto poeksperymentować!
:::

### Tryb podrzędny {#sub-mode}
Przycisk bezpośrednio pod suwakiem intensywności to przycisk `Sub`. Jego etykieta i funkcja zmieniają się w zależności od narzędzia, a po wciśnięciu wywołuje alternatywne, zwykle przeciwne zachowanie. Np. dla [Paint](#paint) włącza tryb Erase, dla [Crease](#crease) tworzy wypukłe krawędzie zamiast wcięć itp.

Domyślnie działa jak przycisk chwilowy; tzn. możesz go przytrzymać, aby tymczasowo go włączyć, po puszczeniu zostanie wyłączony. Jeśli go stukniesz, tryb sub będzie aktywny na stałe.

### Skróty {#shortcuts}
Na dole lewego paska narzędzi znajdują się skróty do [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Domyślnie wszystkie działają jak przyciski chwilowe; tzn. możesz je przytrzymać, aby tymczasowo je włączyć, po puszczeniu zostaną wyłączone. Jeśli je stukniesz, dany tryb skrótu będzie aktywny na stałe.

### Sterowanie zaznaczeniem {#selection-controls}

Narzędzia [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) i [Hide](#hide) używają podobnych kontrolek do zaznaczania obszarów siatki.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Kształt rysowany odręcznie
* `Polygon` - Zamknięty kształt zdefiniowany kombinacją krzywych i/lub linii prostych. Zobacz [Shape editing](#shape-editing) poniżej, aby uzyskać więcej informacji.
* `Curve` - (tylko Project) - Krzywa rysowana odręcznie do projekcji
* `Path` - (tylko Project) - Krzywa zdefiniowana punktami. Zobacz [Shape editing](#shape-editing) poniżej, aby uzyskać więcej informacji.
* `Line` - Przeciągnij linię, aby zdefiniować płaski segment. Domyślnie operacja zostanie wykonana na siatce natychmiast, wyłącz auto validate, jeśli tego nie chcesz (długie przytrzymanie lub przesunięcie na ikonie linii)
* `Rect` - Przeciągnij linię po przekątnej, aby zdefiniować narożniki prostokąta. Długie przytrzymanie lub przesunięcie ujawnia opcje auto validate, wymuszenia kształtu kwadratu oraz ustawienia pierwszego kliknięcia jako środka prostokąta.
* `Ellipse` - Przeciągnij linię po przekątnej, aby zdefiniować rozmiar elipsy. Długie przytrzymanie lub przesunięcie ujawnia opcje auto validate, wymuszenia kształtu koła oraz ustawienia pierwszego kliknięcia jako środka elipsy.
* `Flip` - odwróć maskę kształtu lub kierunek narzędzia project.

Większość narzędzi ma opcję auto validate, co oznacza, że operacja zostanie wykonana natychmiast po zakończeniu rysowania kształtu. Gdy auto validate jest wyłączone, obok kształtu pojawi się zielony przycisk, który wykona operację. Pozwala to edytować kształt, dostosować widok, a gdy będziesz gotowy do użycia kształtu, naciśnij zielony przycisk.

### Edycja kształtu {#shape-editing}
Edycja wielokątów i krzywych zachowuje się w podobny sposób:

* Na początek przeciągnij linię, aby zdefiniować 2 punkty, następnie przeciągnij ze środka linii, aby zdefiniować wielokąt lub krzywą.
* Kliknij punkty, aby przełączać je między gładkimi a ostrymi. 
* Kliknij i przeciągnij na odcinkach krzywej lub linii, aby tworzyć nowe punkty.
* Aby usunąć punkt, przeciągnij go na sąsiedni, aż zmieni kolor na czerwony.
* Ikona kosza w rogu ikony wielokąta lub ścieżki usunie kształt.

### Menu ustawień {#settings-menu}

Wiele narzędzi ma dodatkowe ustawienia znajdujące się w menu settings, pierwszej ikonie w prawym górnym rogu:

![](/images/tools_settings_menu.webp)

## Narzędzia {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Glina {#clay}
Narzędzie Clay jest przydatne do budowania rzeźby. `Sub` usuwa materiał z rzeźby.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pędzel {#brush}
Standardowy pędzel. `Sub` usuwa materiał.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Przesuń {#move}
Obszar pod pędzlem „przykleja się” do pędzla, umożliwiając elastyczną deformację. Zaznaczenie jest utrzymywane podczas przesuwania, więc jeśli odsuniesz pędzel, a potem wrócisz w to samo miejsce, nie zobaczysz deformacji.

Tryb sub to `Normal` i przesuwa obszar pod pędzlem wzdłuż normalnej powierzchni.

To narzędzie jest dobre zarówno do dużych deformacji, jak i precyzyjnych, małych zmian.

#### Ustawienia narzędzia Przesuń {#move-settings}

* `Radius (Background)` - Jak daleko od krawędzi modelu możesz być i nadal rzeźbić, przydatne przy pracy nad sylwetką obiektu. 
* `Same-side vertex only` - Ignoruj wierzchołki, które są zwrócone w przeciwnym kierunku niż deformacja.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Przeciągnij {#drag}
Obszar pod pędzlem „przykleja się” do pędzla, umożliwiając elastyczną deformację. W przeciwieństwie do pędzla Move, zaznaczenie jest ciągle aktualizowane podczas pociągnięcia, więc można tworzyć dłuższe, „wężowe” obiekty, szczególnie gdy włączona jest Dynamic Topology.

Tryb sub to `Normal` i przesuwa obszar pod pędzlem wzdłuż normalnej powierzchni.

To narzędzie jest dobre do luźniejszych, gesturalnych zmian kształtu.

#### Ustawienia narzędzia Przeciągnij {#drag-settings}

* `Radius (Background)` - Jak daleko od krawędzi modelu możesz być i nadal rzeźbić, przydatne przy pracy nad sylwetką obiektu. 
* `Same-side vertex only` - Ignoruj wierzchołki, które są zwrócone w przeciwnym kierunku niż deformacja.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Wygładzanie {#smooth}
Wygładza obszar poprzez uśrednianie pozycji punktów. To narzędzie jest silnie zależne od gęstości wielokątów.
Jeśli masz wiele wielokątów, wygładzanie będzie mniej efektywne.

Tryb sub to `Relax`, który wygładza tylko siatkę (wireframe), starając się zachować detale geometryczne.

#### Ustawienia wygładzania {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Grupa ścian {#smooth-facegroup}

* `Relax` - Wygładza krawędzie facegroupów. Użyj intensywności większej niż 100%, aby szybko wygładzić krawędzie. `Auto` wygładza tylko wtedy, gdy podgląd facegroupów jest włączony, `Off` wyłącza, `On` włącza. 

##### Wierzchołek {#vertex}
* `Sticky vertex on border` - Dla siatek z otwartymi krawędziami, np. płaszczyzny, możliwe jest wygładzenie narożników. Włączenie tej opcji zablokuje otwarte krawędzie.
* `Relax` - to samo co alternatywny tryb relax na lewym pasku narzędzi.
* `Stable smoothing` - Próbuje uczynić wygładzanie niezależnym od topologii. Najlepiej działa przy zróżnicowanej gęstości topologii i wysokiej wartości intensywności wygładzania.

##### Malowanie {#painting}
* `Screen Smoothing` - Użyj tej opcji, aby uzyskać wygładzanie niezależne od topologii, nawet przy wysokich liczbach wielokątów.
* `Screen samples` - Jakość wygładzania, wyższe wartości będą gładsze, ale wolniejsze.

::: tip
Wyższe gęstości wielokątów mogą wymagać podniesienia intensywności powyżej 100%. Bardzo wysokie wartości (300%, 500%) mogą też dobrze działać jako narzędzie rzeźbiarskie, szybko spłaszczając i wygładzając obszary pod pędzlem, jak uderzenie gliny młotkiem!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maska {#mask}
To narzędzie pozwala maskować wierzchołki. Zamaskowane wierzchołki są chronione przed rzeźbieniem lub malowaniem. 

Tryb sub to `Unmask` i wymazuje obszary, gdzie maska została nałożona.

Podobnie jak zaznaczenia w 2D programach malarskich, maski można malować pędzlem lub tworzyć za pomocą kształtów, rozmywać lub wyostrzać. 

W przeciwieństwie do programów 2D, można je też tworzyć za pomocą facegroupów, a maski mogą być używane do tworzenia nowej geometrii poprzez operacje typu ekstrudowanie/wyciąganie. 

![](/videos/tool_mask1.mp4)

 Na górze widoku pojawi się pasek narzędzi z dodatkowymi kontrolkami. 

![](/images/tool_mask_toolbar.webp)

Tytuł paska można stuknąć, aby go rozwinąć/zwinąć, a strzałkę w prawym górnym rogu, aby przenieść go na górę lub dół interfejsu.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | Wyczyść maskę                                                                             |
| ![](/icons/invert.webp)        Invert             | Odwróć maskę                                                                              |
| ![](/icons/sharpen.webp)       Sharpen            | Wyostrz krawędź maski                                                                     |
| ![](/icons/blur.webp)          Blur               | Rozmyj krawędź maski                                                                      |
|                                 Blur ->            | Przeciągnij w lewo/prawo, aby interaktywnie rozmywać maskę                                |
| ![](/icons/culling.webp)       Front              | Przełącz, aby maskować tylko wierzchołki skierowane do przodu                             |
|                                 Convert            | Konwertuj maskę na facegroup                                                              |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Po włączeniu facegroupy będą widoczne, a stuknięcie facegroupu zamaskuje go               |
|                                 On tap (mask)      | Po włączeniu stuknięcie „wyspy” zamaskowanych lub odmaskowanych wielokątów wypełni ją     |
| ![](/icons/vertex.webp)        Connected          | Po włączeniu pociągnięcia maski wpływają tylko na połączoną topologię                     |

##### Szybki gest maski {#mask-quick-gesture}
Możesz wykonywać gesty w stylu ZBrusha, trzymając przycisk szybkiego maskowania na lewym pasku narzędzi:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Stuknij w tło                      |
| Clear   | Przeciągnij po tle                 |
| Blur    | Stuknij w zamaskowany obszar       |
| Sharpen | Stuknij w odmaskowany obszar       |


#### Ustawienia maski {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Menu ustawień Mask służy głównie do tworzenia geometrii z maski. Z tego powodu domyślnym zachowaniem jest podgląd tego, jak będzie wyglądać nowa geometria. Możesz wybrać brak podglądu, podgląd extract, podgląd split oraz to, czy geometria będzie wyświetlana w trybie x-ray.

##### Grubość {#thickness}
* `Height` - Wysokość wyciągniętego kształtu. Ikona Plus/Minus pozwala przełączać się między ekstrudowaniem na zewnątrz, do wewnątrz lub wyśrodkowanym. 
* `Height/Height+Mask` - Przełączanie między stałą wysokością a sytuacją, w której rozmyte części maski wpływają na wysokość, pozwalając na miękkie i zróżnicowane wysokości kształtów. 

##### Gładkość {#smoothness}
Po włączeniu wygładza krawędź wyciągniętego kształtu, działa lepiej przy wyższej liczbie wielokątów. 
* `Iterations` - Ilość zastosowanego wygładzania. Wysokie wartości dadzą bardzo gładkie, zakrzywione krawędzie, ale kształt zacznie odbiegać od maski.
* `All/Sharp border/Borders only` - Wygładzanie może działać we wszystkich kierunkach, wygładzając boki i górę wyciągniętego kształtu, lub wygładzać górę i boki, ale zachować ostrą krawędź, albo wygładzać tylko krawędź, pozostawiając górną powierzchnię bez zmian.

##### Pętla krawędzi (bok) {#edge-loop-side}
* `Auto Edge-loop (side)` - Oblicza liczbę podziałów na bokach wyciągniętego kształtu, aby utworzyć kwadratowe wielokąty dopasowane do wielokątów obszaru zamaskowanego. Po wyłączeniu możesz sam ustawić liczbę edge loopów suwakiem.

----

##### Ekstrakcja {#extract}
* `Extract` - Utwórz wyciągniętą geometrię.
* `Closing action` - Jak ma zachowywać się extract. 'None' duplikuje zamaskowane polygony do nowego kształtu. 'Fill' robi to samo i próbuje załatać tylną powierzchnię. 'Shell' wyciąga do wartości ustawionej w 'thickness' i jest domyślne.

::: tip

Jeśli podgląd jest w trybie 'Extract' z włączonym 'X-ray', kliknięcie przycisku Extract może być na początku mylące. Ponieważ menu jest aktywne, spróbuje ono podglądnąć ekstrakcję na nowym kształcie i włączy x-ray na oryginalnej powierzchni. Jednak ponieważ nie masz maski na nowej powierzchni, nie może wykonać podglądu ekstrakcji i Nomad ostrzeże „Nothing to Extract!”.

To normalne, zamknij menu ustawień maski, aby zobaczyć nowy kształt i oryginał, a następnie wybierz ponownie oryginalną powierzchnię, jeśli musisz wyczyścić maskę lub narysować nowe maski.
:::

##### Podział {#split-mask}
* `Split` - Wyciągnie zarówno zamaskowane, jak i odmaskowane regiony do nowych kształtów. 
* `Closing action (masked)` - Jak ma zachowywać się extract maski. 'None' duplikuje zamaskowane polygony do nowego kształtu. 'Fill' robi to samo i próbuje załatać tylną powierzchnię. 'Shell' wyciąga do wartości ustawionej w 'thickness' i jest domyślne.
* `Closing action (unmasked)` - Jak ma zachowywać się extract odmaskowanej części. 'None' duplikuje odmaskowane polygony do nowego kształtu. 'Fill' robi to samo i próbuje załatać tylną powierzchnię. 'Shell' wyciąga do wartości ustawionej w 'thickness' i jest domyślne.
* `Sync border` - Zapewnia, że krawędź między zamaskowanymi i odmaskowanymi wyciągniętymi kształtami pozostaje blisko siebie. Po wyłączeniu, ponieważ operacja shell wyciąga każdą ścianę wzdłuż jej normalnej, między kształtami może powstać szczelina.

##### Rzeźbienie {#carve}
* `Carve` - W trybie domyślnym zachowuje się tak, jakbyś przyciął powierzchnię na głębokość 'thickness', jak wycięcie kawałka skórki pomarańczy. 



### ![](/icons/tool_maskSelector.webp) Maska zaznaczenia {#selection-mask}
To narzędzie jest w większości podobne do [Masking tool](#mask), główna różnica polega na tym, że nie używasz stroke do malowania maski, ale [Selection Controls](#selection-controls).

Tryb sub to `Unmask` i wymazuje maskę za pomocą kontrolek zaznaczenia.

Selection mask współdzieli te same ustawienia narzędzia co `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Malowanie {#paint}
Nakłada kolor i właściwości materiału. Aby dowiedzieć się więcej o materiale, odwiedź sekcję [Painting](painting.md).

Tryb sub to `Erase` i usuwa farbę.

#### Ustawienia malowania {#paint-settings}
* `Layer fitering` - Działa jak blokada alfy warstwy w Photoshopie lub Procreate. Jeśli malujesz na warstwie, po włączeniu tej opcji możesz modyfikować tylko miejsca, gdzie farba już istnieje; niepomalowane obszary będą chronione.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Rozmazywanie {#smudge}
Rozmazuje kolor i właściwości materiału. Menu ustawień Smudge zawiera suwak `Quality`, niższe wartości oznaczają szybsze pociągnięcia.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Spłaszczanie {#flatten}
Spłaszcza obszar, rzutując punkty na średnią płaszczyznę.

Tryb sub to `Fill` i definiuje płaszczyznę ustawioną przez najwyższy punkt, z tendencją do podciągania punktów w górę.

#### Ustawienia spłaszczania {#flatten-settings}

* `Lock plane direction` - Użyj kierunku płaszczyzny obliczonego przy pierwszym kliknięciu. Domyślnie wyłączone.
* `Lock plane origin`- Użyj pierwszego kliknięcia jako środka płaszczyzny. Domyślnie wyłączone.

Gdy jedna lub obie opcje są wyłączone, flatten może być stopniowo pogłębiany lub kąt płaszczyzny może być zmieniany za pomocą długich pociągnięć przechodzących przez różne głębokości i krzywizny. W połączeniu z opcjami próbkowania obszaru w menu pędzla daje to bardzo precyzyjną kontrolę.

::: tip
Przy pracy w obszarach o dużej krzywiźnie, np. próbując spłaszczyć policzki, ale narzędzie ciągle wpływa na boki nosa, spróbuj utworzyć maskę, aby chronić obszary, których flatten nie powinien dotykać.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planarne {#planar}
Ustawia punkty w jednej płaszczyźnie, rzutując je na średnią płaszczyznę, ale z mniejszym narastaniem niż pędzel Flatten. Tworzy to czystsze, twarde powierzchnie. Szybkie pociągnięcia bardziej wypychają i wciągają powierzchnię, wolniejsze, zaczynające się od już płaskich obszarów i wychodzące na zewnątrz, lepiej utrzymują płaszczyznę.

Tryb sub to `Fill` i definiuje płaszczyznę ustawioną przez najwyższy punkt, z tendencją do podciągania punktów w górę.

Planar jest w rzeczywistości tym samym narzędziem co `Flatten`, ale z włączonym `Lock plane direction`, co oznacza, że ma tendencję do tworzenia stabilniejszych, twardych powierzchni, podczas gdy flatten może być bardziej rzeźbiarski i używany do tworzenia półpłaskich obszarów.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Zagięcie {#crease}
Narzędzia Crease są przydatne do rzeźbienia małych nacięć lub wgłębień.

Tryb sub to `Invert` i tworzy wypukłe wcięcia.

#### Ustawienia zagięcia {#crease-settings}

* `Pinch factor` - Jak bardzo ściągać wierzchołki na boki w kierunku pociągnięcia pędzla. Jeśli pinch jest na 1, a offset na 0, powierzchnia nie będzie miała zmian głębokości, tylko zmiany topologii, ściągając krawędzie w kierunku pociągnięcia.
* `Offset factor` - Jak bardzo wypychać/wciągać wierzchołki w głąb. Jeśli pinch jest na 0, a offset na 1, powstaną głębokie wcięcia lub wypukłe wgłębienia, ale będą wyglądać poszarpanie, ponieważ za mało geometrii jest ściągane w kierunku wcięcia, aby dokładnie zdefiniować boki lub dno.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Ściśnięcie {#pinch}
To narzędzie może być używane do wyostrzania krawędzi.

Tryb sub to `Invert` i rozsuwa wierzchołki.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Przycinanie {#trim}
Narzędzie Trim działa poprzez usunięcie fragmentu siatki i daje opcje, jak przetworzyć powstałą lukę. Używa [Selection controls](#selection-controls) do zdefiniowania przycięcia.

::: tip
Ponieważ to narzędzie projektuje z kamery, otrzymasz ostrzeżenie, jeśli kamera jest w trybie perspektywicznym.

W trybie ortograficznym cięcie przez siatkę jest równoległe do widoku, co zwykle jest oczekiwane. W trybie perspektywicznym cięcie będzie wyglądać inaczej po dalszej i bliższej stronie obiektu.
:::

#### Ustawienia przycinania {#trim-settings}

* `Stroke painting` - Jeśli malowanie jest włączone w menu Paint, załatany obszar zostanie wypełniony aktualnie wybranym kolorem.
* `Boolean` - wypełnia dziurę po przycięciu regionem quadów. Wypełniony region będzie płaski.
* `Legacy` - wypełnia dziurę po przycięciu regionem triangulowanym. Wypełniony region będzie płaski.
* `Fill` - wypełnia dziurę triangulowanym regionem. Wypełniony region będzie zakrzywioną powierzchnią, jak błona bańki mydlanej.
* `None` - nie wypełnia dziury.
* `Boolean Detail Shape` - Przybliżony rozmiar quadów i trójkątów użytych po stronie kształtu przycięcia.
* `Boolean Detail Hole` - Przybliżony rozmiar trójkątów lub wielokątów użytych w wypełnionej dziurze po przycięciu. 
* `Legacy Detail` - Przybliżony rozmiar trójkątów użytych przy przycięciu.
* `Legacy Hole smoothing` - Jak bardzo trójkąty są relaksowane na wypełnionym obszarze.
* `Legacy Threshold espilon` - Wartość, którą można dostosować, aby poprawić działanie algorytmu wypełniania dziur Legacy.
* `Fill Detail` - Przybliżony rozmiar trójkątów użytych przy przycięciu.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Podział {#split}
Podobne do narzędzia [Trim](#trim), z tą różnicą, że Trim odrzuca zaznaczenie, a Split zachowuje zaznaczenie jako nowy obiekt.

#### Ustawienia podziału {#split-settings}

* `Stroke painting` - Jeśli malowanie jest włączone w menu Paint, załatany obszar zostanie wypełniony aktualnie wybranym kolorem.
* `Boolean` - wypełnia dziurę po podziale regionem quadów. Wypełnione regiony będą płaskie.
* `Legacy` - wypełnia dziurę po podziale regionem triangulowanym. Wypełnione regiony będą płaskie.
* `Fill` - wypełnia dziury triangulowanym regionem. Wypełnione regiony będą zakrzywionymi powierzchniami, jak błona bańki mydlanej.
* `None` - nie wypełnia dziur.
* `Boolean Detail Shape` - Przybliżony rozmiar quadów i trójkątów użytych po stronie kształtu podziału.
* `Boolean Detail Hole` - Przybliżony rozmiar trójkątów lub wielokątów użytych w wypełnionej dziurze po podziale. 
* `Legacy Detail` - Przybliżony rozmiar trójkątów użytych przy podziale.
* `Legacy Hole smoothing` - Jak bardzo trójkąty są relaksowane na wypełnionym obszarze.
* `Legacy Threshold espilon` - Wartość, którą można dostosować, aby poprawić działanie algorytmu wypełniania dziur Legacy.
* `Fill Detail` - Przybliżony rozmiar trójkątów użytych przy podziale.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projekcja {#project}
Narzędzie Project wygląda jak [Trim](#trim), ale nie usuwa ani nie tworzy geometrii, tylko przesuwa wierzchołki, aby dopasować je do zaznaczenia.

![](/videos/tool_project.mp4)

::: tip
Jeśli użyjesz Project będąc na warstwie, możesz mieszać między oryginalnym a zprojekowanym kształtem suwakiem warstwy.
:::

### ![](/icons/tool_layer.webp) Warstwa {#layer}
Podnosi powierzchnię, ale ogranicza wysokość.

Jeśli trzymasz rysik na ekranie i wciąż malujesz po obszarze, Layer podniesie go do pewnej wysokości i dalej nie pójdzie, w przeciwieństwie do innych narzędzi, które będą wciąż kumulować wysokość.

Zauważ, że domyślnie limit jest ustawiany tylko na pociągnięcie! Jeśli zaczniesz nowe pociągnięcie, będzie budować od nowej wysokości powierzchni.

Aby ustawić stałą maksymalną wysokość w wielu pociągnięciach, użyj narzędzia Layer z systemem [Layers](layers.md) Nomada.

Utwórz warstwę i użyj tego narzędzia. Maksymalna wysokość jest teraz ustawiona z warstwy, więc możesz wykonywać wiele pociągnięć pędzlem, a wysokość zawsze będzie taka sama.

`Sub` użyje minimalnej głębokości, tworząc rowki.

#### Ustawienia warstwy {#layer-settings}

* `Use layer data` - Po włączeniu i przy zaznaczonej warstwie używa danych warstwy do ustawienia maksymalnej wysokości.
* `Inflate`- Po włączeniu dostosowuje kierunek działania Layer, aby uzyskać gładsze rezultaty.
* `Relax (Normal)` - Ilość wygładzania stosowanego do normalnych.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Nadmuchanie {#inflate}
Przesuwa wierzchołki wzdłuż ich własnych normalnych. `Sub` przesuwa wierzchołki wzdłuż odwróconej normalnej.

#### Ustawienia nadmuchiwania {#inflate-setings}
* `Relax (Normal)` - Ilość wygładzania stosowanego do normalnych.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Szturchnięcie {#nudge}
Przesuwa lub „rozmazuje” punkty w kierunku pociągnięcia.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stempel {#stamp}

Kliknij i przeciągnij, aby podnieść obszar rzeźby w kształcie wybranego Alpha.

To po prostu [Brush tool](#brush) z typem stroke ustawionym na `Lock + radius`. 

`Sub` wciśnie stempel do środka zamiast wyciągać go z powierzchni.

::: tip
Stamp zwykle najlepiej działa przy wysokiej rozdzielczości geometrii. Jeśli poszukasz w sieci „wrinkles alpha”, „pores alpha”, „scales alpha” itp., te tekstury alpha i Stamp mogą być świetnym sposobem na dodanie organicznych detali do rzeźby postaci.

Dwa tryby stroke są przydatne do różnych rzeczy. 

* `Lock + radius` ma stałą *wysokość*, przeciąganie zmienia szerokość i rotację stempla. Dobre do tekstur skóry, gdzie muszą mieć tę samą głębokość/wysokość, ale różne rotacje i skale, aby ukryć powtarzające się wzory.
* `Lock + intensity` ma stałą *szerokość*, przeciąganie zmienia rotację i wysokość stempla. Dobre do nitów, gdzie wszystkie muszą mieć ten sam rozmiar, ale różne rotacje i wysokości. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Usuń warstwę {#delete-layer}
To narzędzie może resetować warstwy lokalnie, potrzebujesz aktywnej warstwy, w przeciwnym razie nic się nie stanie.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Rura {#tube}
Twórz rurę, rysując krzywą. 
![](/images/tool_tube_new.webp)

Po utworzeniu rury ścieżkę można edytować w przestrzeni 3D, używając podobnych kontrolek jak standardowe narzędzia [Shape editing](#shape-editing) i edycji krzywych. 

![](/videos/tool_tube.mp4)

#### Lewy pasek narzędzi Rury {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Lewy pasek narzędzi ma następujące opcje:

* `Sync` - Jeśli bieżąca rura jest instancją i istnieją węzły podrzędne rury różniące się między instancjami, to je zsynchronizuje.
* `Snap` - Po włączeniu tryby curve i path będą przyciągać się do innych obiektów podczas rysowania. Po wyłączeniu pierwszy punkt będzie przyciągany, a reszta rury zostanie narysowana na tej głębokości. Ma małe menu rozwijane:
    * `Offset` - Ustaw głębokość przyciągania; 0% sprawi, że środek przekroju rury będzie przyciągany do powierzchni, wartości dodatnie uniosą ją nad powierzchnię, ujemne obniżą.
* `Curve` - Szkicuj rurę odręcznie. Ma małe menu rozwijane:
    * `Auto-validate` - Utworzy rurę natychmiast po zakończeniu pociągnięcia. Po wyłączeniu obok ścieżki krzywej będzie widoczny zielony okrąg walidacji, naciśnij go, aby zatwierdzić, lub użyj linku `Reset`, który pojawia się w tym menu, aby usunąć ścieżkę.
    * `Closed` - zamienia rurę w pętlę.
    * `Screen` - Dostępne tylko, gdy Auto-validate jest wyłączone. Po włączeniu ścieżka jest „przypięta” do ekranu, pozwalając na poruszanie widokiem i obiektem, a ścieżka pozostaje na miejscu. Po wyłączeniu ścieżka jest częścią sceny 3D i porusza się wraz z kamerą i obiektami.
    * `Accuracy` - Ile punktów krzywej zostanie użytych do konwersji narysowanej ścieżki na rurę. 0% użyje najmniejszej liczby punktów, ale pominie małe zmiany krzywizny ścieżki. 100% będzie bardzo dokładne i użyje wielu punktów.
* `Path` - Twórz rurę, klikając, aby zdefiniować punkty krzywej. Stuknij zielony okrąg, aby zatwierdzić ścieżkę. Ma małe menu rozwijane:
    * `B-spline` - Alternatywna metoda rysowania krzywej, w której punkty krzywej zwykle nie leżą bezpośrednio na krzywej, ale mogą dawać gładsze rezultaty niż metoda domyślna.
    * `Closed` - zamienia rurę w pętlę
    * `Screen` - Po włączeniu ścieżka jest „przypięta” do ekranu, pozwalając na poruszanie widokiem i obiektem, a ścieżka pozostaje na miejscu. Po wyłączeniu ścieżka jest częścią sceny 3D i porusza się wraz z kamerą i obiektami.

##### Górny pasek narzędzi Rury {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Gdy rura jest zaznaczona, na górze widoku pojawi się pasek narzędzi z dodatkowymi kontrolkami. Kliknij tytuł paska, aby go zwinąć/rozwinąć, a strzałkę w prawym górnym rogu, aby przenieść pasek na górę lub dół widoku.

* `Validate` - wypala rurę do zwykłych wielokątów, aby można ją było rzeźbić.
* `Edit` - wyświetla punkty krzywej, aby można je było modyfikować
* `Mirror` - dodaje repeater lustrzany jako rodzica tej krzywej
* `Snap` - przyciąga punkty krzywej do pobliskich powierzchni
* `Closed` - łączy początek i koniec krzywej w pętlę
* `B-spline` - Przełącza między interpolacją Catmull-rom a B-spline.
* `Cap` - Przełącza między zaślepkami na obu końcach rury, tylko na początku lub końcu, lub bez zaślepek.
* `Hole` - Dodaje grubość rurze, zamieniając ją w rurę z otworem. Przełącza między otworem na obu końcach, tylko na końcu lub bez otworów. 
* `Radius` - Przełącza między jednolitym promieniem, promieniem na początku i końcu lub promieniem na każdy punkt krzywej. Edytuje się je pomarańczowymi uchwytami na krzywej.
* `Twist` - Przełącza między brakiem skrętu, jednolitym skrętem, skrętem na początku i końcu lub skrętem na każdy punkt krzywej. Edytuje się je różowymi uchwytami na krzywej.
* `Profile` - Przełącza między brakiem profilu (czyli profilem kołowym), jednolitym profilem, profilem na początku i końcu lub profilem na każdy punkt.
* `Profile edit` - Wyświetla edytor profilu. Działa podobnie do narzędzi [Shape editing](#shape-editing), może zapisywać i wczytywać presety profilu oraz ma przełącznik pozwalający edytować profil w przestrzeni 3D.
* `Spiral` - Przełącza menu dodawania spiralnego skrętu do rury. Menu ma opcje `Twist Angle`, `Offset`, `Scale` i `Angle offset`.
* `X Divisions` - liczba podziałów wokół rury, 4 podziały utworzą np. rurę o przekroju kwadratowym. 
* `Constant density` - Po włączeniu utrzymuje kwadratowe wielokąty. Po wyłączeniu pozwala ustawić `Y divisions` wzdłuż długości rury.
* `...` - Menu ustawień Tube.

#### Przełącznik usuwania punktu krzywej {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Poniżej paska narzędzi znajduje się przełącznik usuwania punktu krzywej. Gdy przeciągniesz punkt krzywej blisko innego, zmieni kolor na czerwony, wskazując, że po puszczeniu punkt zostanie usunięty. Jeśli wykonujesz drobne edycje i nie chcesz usuwać punktów, ten przycisk wyłączy zachowanie usuwania punktów.



#### Ustawienia Rury {#tube-settings}
* `Primitive` - przyciski pozwalające włączyć/wyłączyć UV lub zatwierdzić rurę.
* `Post subdivision` - skrót do ustawienia poziomu multiresolution przed zatwierdzeniem.
* `Linear subdivision` - skrót do ustawienia poziomu linear subdivision przed zatwierdzeniem. 
* `Division X` - to samo co X Divisions na pasku narzędzi.
* `Division Y` - to samo co Y Divisions na pasku narzędzi.
* `Curve (Repeater)` - konwertuje rurę na [Curve Repeater](scene.md#curve)

::: tip
Division X ustawione na 4 i Post subdivision na 3 da gładkie, zaokrąglone końcówki rur, dobre na robaki, węże, części ciała.
:::


### ![](/icons/tool_lathe.webp) Tokarka {#lathe}
Twórz powierzchnię obrotową, rysując krzywą.

To narzędzie jest świetne do kształtów takich jak wazony, kieliszki do wina.

![](/videos/tool_lathe.mp4)

#### Lewy pasek narzędzi Tokarki {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Lewy pasek narzędzi ma następujące opcje:

* `Sync` - Jeśli bieżący lathe jest instancją i istnieją węzły podrzędne różniące się między instancjami, to je zsynchronizuje.
* `Fixed` - Po włączeniu środek lathe jest stały i wyświetlany na ekranie. Ta linia środkowa ma punkty edycji, które można dostosować. Po wyłączeniu środek lathe będzie dynamicznie aktualizowany, aby dopasować się do początku i końca narysowanej krzywej.
* `Curve` - Rysuj profil lathe jednym pociągnięciem. Ma małe menu rozwijane:
    * `Auto-validate` - Po włączeniu lathe zostanie utworzony po podniesieniu rysika z ekranu. Po wyłączeniu zielony okrąg obok krzywej można nacisnąć, aby utworzyć lathe. Krzywą można usunąć przyciskiem `Reset`.
    * `Closed` - łączy początek i koniec krzywej w pętlę
    * `Screen` - Dostępne tylko, gdy Auto-validate jest wyłączone. Po włączeniu ścieżka jest „przypięta” do ekranu, pozwalając na poruszanie widokiem i obiektem, a ścieżka pozostaje na miejscu. Po wyłączeniu ścieżka jest częścią sceny 3D i porusza się wraz z kamerą i obiektami.
    * `Accuracy` - Ile punktów krzywej zostanie użytych do konwersji narysowanej ścieżki na rurę. 0% użyje najmniejszej liczby punktów, ale pominie małe zmiany krzywizny ścieżki. 100% będzie bardzo dokładne i użyje wielu punktów.
* `Path` - Twórz lathe, klikając, aby zdefiniować punkty krzywej. Stuknij zielony okrąg, aby zatwierdzić ścieżkę. Ma małe menu rozwijane:
    * `B-spline` - Alternatywna metoda rysowania krzywej, w której punkty krzywej zwykle nie leżą bezpośrednio na krzywej, ale mogą dawać gładsze rezultaty niż metoda domyślna.
    * `Closed` - zamienia rurę w pętlę
    * `Screen` - Po włączeniu ścieżka jest „przypięta” do ekranu, pozwalając na poruszanie widokiem i obiektem, a ścieżka pozostaje na miejscu. Po wyłączeniu ścieżka jest częścią sceny 3D i porusza się wraz z kamerą i obiektami.

#### Górny pasek narzędzi Tokarki {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Gdy lathe jest zaznaczony, na górze widoku pojawi się pasek narzędzi z dodatkowymi kontrolkami. Kliknij tytuł paska, aby go zwinąć/rozwinąć, a strzałkę w prawym górnym rogu, aby przenieść pasek na górę lub dół widoku.

* `Validate` - wypala lathe do zwykłych wielokątów, aby można go było rzeźbić.
* `Edit` - wyświetla punkty krzywej, aby można je było modyfikować
* `Mirror` - dodaje repeater lustrzany jako rodzica tego lathe
* `Snap` - przyciąga punkty krzywej do pobliskich powierzchni
* `Stable` - Po włączeniu profil krzywej będzie zparentowany do linii środkowej lathe. Po wyłączeniu linia środkowa może być edytowana i nie będzie przesuwać krzywej, co pozwala na bardziej złożone kształty.
* `Focus` - Obraca widok, aby zobaczyć profil krzywej idealnie płasko do kamery.
* `Closed` - łączy początek i koniec krzywej w pętlę
* `Cap` - Jeśli Closed jest wyłączone, przełącza między zaślepkami na obu końcach rury, tylko na początku lub końcu, lub bez zaślepek.
* `Hole` - Dodaje grubość lathe, zamieniając go w rurę. Przełącza między otworem na obu końcach, tylko na końcu lub bez otworów. 
* `B-spline` - Przełącza między interpolacją Catmull-rom a B-spline.
* `X Divisions` - liczba podziałów wokół lathe, 4 podziały utworzą np. profil kwadratowy. 
* `Constant density` - Po włączeniu utrzymuje kwadratowe wielokąty. Po wyłączeniu pozwala ustawić `Y divisions` wzdłuż długości rury.
* `...` - Menu ustawień Lathe.

#### Ustawienia Tokarki {#lathe-settings}
* `Primitive` - przyciski pozwalające włączyć/wyłączyć UV lub zatwierdzić rurę.
* `Post subdivision` - skrót do ustawienia poziomu multiresolution przed zatwierdzeniem.
* `Linear subdivision` - skrót do ustawienia poziomu linear subdivision przed zatwierdzeniem. 
* `Division X` - to samo co X Divisions na pasku narzędzi.
* `Division Y` - to samo co Y Divisions na pasku narzędzi.
* `Curve (Repeater)` - konwertuje profil krzywej na [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Wstaw {#insert}
Umieszcza obiekt na powierzchni innego. W użyciu jest podobne do narzędzia Stamp, ale dla pełnych kształtów 3D.

Jeśli wybierzesz prymityw z lewego paska narzędzi, kliknięcie i przeciągnięcie na dowolnej powierzchni umieści prymityw w miejscu kliknięcia, a przeciągnięcie ustawi rozmiar. Po zakończeniu przeciągania Insert przełączy się w tryb [Transform](#transform).

W trybie Instance przeciąganie utworzy i przesunie nową instancję po powierzchni. Rozmiar zostanie skopiowany z pierwszego kształtu, w ten sposób możesz umieszczać wiele instancji obiektu o tym samym rozmiarze na innych powierzchniach.

Nie musisz wstawiać tylko prymitywów! Wybierz *dowolny* kształt w outlinerze, jeśli Insert jest w trybie Instance lub Clone, możesz przeciągać kopie wybranego obiektu po dowolnej powierzchni.

Jeśli obiekt ma niestandardowy pivot, zostanie on użyty jako punkt kotwiczenia. Zobacz wideo poniżej.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Przekształć {#transform}
Przesuwa/obraca/skaluje model bezpośrednio jednym i dwoma palcami, zwykle po powierzchni innego obiektu.

Narzędzie jest kontrolowane lewym paskiem narzędzi i ma 5 przycisków:

* `Snap` - przyciąga model do innych powierzchni
* `Group` - Jeśli zaznaczony obiekt ma kombinację obiektów i instancji, pozwala określić zachowanie narzędzia.
* `Move` - Przeciągnięcie jednym palcem przesuwa obiekt. Gdy Snap jest aktywny, przesuwa obiekt po powierzchni pod palcem.
* `Rotate` - Przeciągnięcie jednym palcem obraca obiekt. Gdy Snap jest aktywny, obraca wokół normalnej powierzchni pod palcem.
* `Scale` - Przeciągnięcie jednym palcem skaluje obiekt.

Transform może szybko używać 2 z tych trybów za pomocą dwóch palców:

* Przeciągnij obiekt, aby go umieścić. Przestań poruszać pierwszym palcem, ale nie podnoś go z ekranu.
* Dotknij drugim palcem ekranu, trzymając pierwszy palec. Gdy drugi palec jest przeciągany, obiekt będzie skalowany.
* Podnieś drugi palec i kontynuuj przeciąganie pierwszym palcem, obiekt znów będzie w trybie Move.

Możesz też zmienić drugi tryb gestem stuknięcia drugim palcem:

* Przeciągnij obiekt, aby go umieścić, przestań poruszać, ale nie podnoś palca z ekranu.
* Stuknij drugim palcem, trzymając pierwszy palec
* Narzędzie przełączy się w tryb Rotate. Przeciągnij pierwszym palcem, aby ustawić rotację.
* Stuknij drugim palcem jak wcześniej, narzędzie przełączy się z powrotem w tryb Move.

Daje to szybki workflow do klonowania obiektów na innym, np. kamieni na krajobrazie. Zauważ, że przycisk Clone jest również na lewym pasku narzędzi dla łatwego dostępu:

* Użyj narzędzia Transform, aby umieścić kamień.
* Puść, naciśnij przycisk Clone
* Przesuń ten kamień, obróć/skaluj w razie potrzeby
* Puść, naciśnij przycisk Clone
* Przesuń ten kamień, powtarzaj.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
To narzędzie pozwala przesuwać, obracać i skalować obiekty oraz zmieniać ich pivoty.

Uchwyt w widoku ma następujące funkcje:

* `Move` - Przeciągnij linię+strzałkę, aby przesuwać po X/Y/Z. Przeciągnij brzoskwiniową kropkę w środku gizma, aby przesuwać swobodnie w przestrzeni ekranu. Kliknij czerwone, zielone, niebieskie kwadraty, aby przesuwać w płaszczyznach X/Y/Z.
* `Rotate` - Przeciągnij czerwone/zielone/niebieskie okręgi, aby obracać po X/Y/Z. Przeciągnij kulę wewnątrz okręgów, aby obracać swobodnie.
* `Scale`- Przeciągnij zewnętrzne czerwone/zielone/niebieskie kropki, aby skalować po X/Y/Z. Przeciągnij zewnętrzne czerwone/zielone/niebieskie stożki, aby skalować w płaszczyznach X/Y/Z. Przeciągnij zewnętrzny brzoskwiniowy okrąg, aby skalować jednolicie.

![](/images/tool_gizmo.webp)

#### Węzły i wierzchołki {#nodes-and-vertices}

Każdy obiekt w Nomad składa się z węzła i wierzchołków:

* `Node` - „Uchwyt” obiektu, który przechowuje jego przesunięcie, rotację, skalę, czyli macierz transformacji.
* `Vertices` - Punkty definiujące powierzchnię obiektu, przechowują pozycję i informacje o malowaniu.

Jeśli masz prostą kostkę złożoną z 8 wierzchołków, możesz ją przesunąć, modyfikując macierz transformacji lub pozycje wierzchołków. Podczas rzeźbienia zwykle chcesz modyfikować wierzchołki, podczas przesuwania obiektów gizmem zwykle chcesz modyfikować węzeł. Nomad pozwala robić jedno i drugie. 

#### Lewy pasek menu {#left-menu-toolbar}

Lewy pasek narzędzi kontroluje, czy gizmo będzie działać na węźle czy wierzchołkach obiektu, a także inne funkcje:

* `Clone` - Tworzy niezależną kopię bieżącego obiektu, którą można przeciągnąć gizmem.
* `Instance` - Tworzy instancję bieżącego obiektu. Obiekty są połączone, więc zmiany rzeźbiarskie na jednym pojawią się na wszystkich instancjach.
* `Group/Object/Vertex/Auto` - Ustawia, czy gizmo będzie wpływać na węzeł czy wierzchołki obiektu. Domyślny tryb 'auto' próbuje zgadnąć najlepiej. Jeśli kilka obiektów jest zgrupowanych w hierarchii, 'Object' przesunie tylko bieżący obiekt, obiekty podrzędne pozostaną nieruchome. Gizmo może też brać pod uwagę maskowanie i symetrię.
* `Pin` - Domyślnie gizmo przesuwa się do pivotu zaznaczonego obiektu. Po włączeniu Pin gizmo pozostanie tam, gdzie jest.
* `Align` - Przełącza pivot między wyrównaniem do bieżącego obiektu a wyrównaniem do świata.
* `Snap rotation` - Włącza przyciąganie wartości rotacji do przyrostów, wartość przyciągania jest wyświetlana i można ją edytować po włączeniu.
* `Snap translation` - Włącza przyciąganie wartości przesunięcia do przyrostów, wartość przyciągania jest wyświetlana i można ją edytować po włączeniu.
* `Pivot` - Po włączeniu gizmo można przesuwać i obracać bez przesuwania obiektu. Ma dodatkowe menu opisane poniżej.

#### Punkt obrotu {#pivot}
Gdy tryb pivot jest aktywny, wyświetlane jest menu umożliwiające szybkie zmiany pivotu:

**Reset** 
* `Center` - Przesuwa pivot do środka obiektu
* `Bottom` - Przesuwa pivot na dół obiektu
* `Align` - Resetuje rotacje, aby były wyrównane do świata.
* `Mask` - Przesuwa pivot do środka odmaskowanego regionu.

**On Tap**
* `None` - nic nie robi po stuknięciu obiektu
* `Normal` - Przesuwa i obraca pivot, aby wyrównać go do miejsca stuknięcia na powierzchni
* `First` - Przesuwa (ale nie obraca) pivot do miejsca stuknięcia na powierzchni
* `Medial` - Przesuwa pivot do środka obiektu pod miejscem stuknięcia na powierzchni.

#### Ustawienia Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Macierz {#matrix}
* ![](/icons/target.webp) `Move origin` - Przesuwa obiekt tak, aby jego pivot był w środku sceny (origin).
* ![](/icons/bake.webp)  `Bake` - Zamraża obiekt w bieżącej pozycji i ustawia wartości translate/rotate na 0, scale na 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Sprawia, że wartości macierzy odpowiadają położeniu uchwytu gizma w świecie.
* ![](/icons/reset.webp) `Reset` - Skrót ustawiający wartości przesunięcia na 0, rotacji na 0, skali na 1, przesuwając i obracając obiekt.

::: tip Bake vs bake to pivot
Utwórz kostkę, wybierz narzędzie Gizmo, otwórz i przypnij menu ustawień. Domyślnie przesunięcie i rotacja są 0, skala 1.

Włącz tryb pivot, przesuń uchwyt na bok, wyłącz tryb pivot. Pivot się zmienił, ale zauważ, że wartości przesunięcia nadal są 0. 

Jeśli chcesz zobaczyć, gdzie pivot *naprawdę* jest, kliknij `Bake Pivot`. Teraz wartości przesunięcia się aktualizują. Zauważ, że kostka nie porusza się podczas tej operacji ani w trybie pivot.

Przesuń i obróć kostkę gdzieś, a następnie stuknij `Move Origin`. Przesuwa obiekt tak, aby jego pivot był w środku świata, ale pozostawia rotację bez zmian.

Kliknij `Reset`, a rotacja zostanie ustawiona na 0.

Przesuń i obróć kostkę ponownie, tym razem kliknij `Bake`. Pivot pozostaje tam, gdzie jest, kostka pozostaje tam, gdzie jest, ale wartości przesunięcia i rotacji są ustawione na 0.

Poćwicz to kilka razy! Zrozum, że wartości pivotu są ukryte, Nomad zajmuje się nimi za ciebie, ale jeśli musisz ustawić pivot w rzeczywistych lokalizacjach w przestrzeni, Bake Pivot ci w tym pomoże.

:::

* `Translation` - wartości przesunięcia X, Y, Z
* `Rotation` - wartości rotacji X, Y, Z
* `Scale` - Skala jednolita, jeśli jest włączona, lub skala X, Y, Z, jeśli wyłączona.
* `Uniform scale` - Przełącza możliwość skalowania jednolicie lub niezależnie na każdej osi

-----

* `Compact` - przełącza układ gizma, aby dodatkowe uchwyty były na zewnątrz lub wewnątrz kuli rotacji
* `Widget size` - rozmiar gizma
* `Thickness` - grubość linii gizma
* `Opacity` - przezroczystość gizma
* `Hide on interaction` - przełącza, czy gizmo ma być tymczasowo ukrywane podczas przeciągania

-----

* `Tangent roll threshold` - Kontroluje zachowanie interfejsu rotacji podczas przeciągania po okręgach, aby obracać po X/Y/Z. Jeśli wartość wynosi 0, rotacja działa jak pokrętło, przeciągasz gizmo po okręgu. Jeśli wartość wynosi 90, rotacja działa jak pociągnięcie za sznurek jo-jo; przeciągasz w linii prostej w kierunku lub od miejsca pierwszego kliknięcia. Wartości między 0 a 90 dadzą kombinację obu; poniżej wartości będzie ruch liniowy, powyżej ruch okrężny.
* `Numerical input` - Po włączeniu pojedyncze stuknięcie gizma wyświetli okno do wprowadzenia dokładnej wartości dla stukniętej osi widgetu.

::: warning
Narzędzia [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) i [Scale](#scale) używają własnego pola symetrii!

Domyślnie ta symetria jest wyłączona.
:::

Po lewej możesz przesuwać pivot gizma, zobacz wideo poniżej w akcji.
Jest to szczególnie przydatne przy rotacji, ponieważ nie zmienia nic dla przesunięcia.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Grupa ścian {#facegroup}

Facegroupy pozwalają zorganizować obiekt w różnokolorowe powierzchnie. Możesz używać tych grup na wiele sposobów w Nomadzie:

* Szybka metoda zaznaczania dla masek
* Ukrywanie/pokazywanie sekcji obiektu
* Organizowanie obiektu bez konieczności dzielenia go na osobne części
* Definiowanie regionów UV
* Kierowanie quad remeshera
* Dodatkowa kontrola dla narzędzi takich jak Smooth.

#### Lewy pasek narzędzi Grupy ścian {#facegroup-left-toolbar}

* `Patch ` - Wyświetla dostępne facegroupy jako łatki. Nieużywane łatki można usunąć. Stuknij łatkę, aby zmienić jej nazwę lub kolor. Ikona plus pozwala tworzyć nowe łatki.
* `Dot` - Maluj po obiekcie, aby definiować facegroupy. Gdy '+ Face Group' jest włączone, każde nowe pociągnięcie automatycznie tworzy nowy facegroup, przydatne do szybkiego definiowania regionów. Stuknięcie wypełni zaznaczony region. Suwak ustawia promień kropki.
* `Relax` - Wygładza krawędzie facegroupów. Bardzo przydatne do definiowania czystych krawędzi dla quad remeshingu lub paneli do modelowania hard surface. Suwaki kontrolują promień i intensywność operacji relax.
* `Shape selector` - Tworzy facegroupy za pomocą kształtów zamiast pędzla, poprzez `Lock+Radius`, `Lasso`, `Polygon`, `Rect` i `Ellipse`. Zobacz [Shape Selector](#shape-selector), aby uzyskać więcej informacji.
* `Auto-pick` - Po włączeniu wybierze łatkę, w której zaczyna się pociągnięcie, i zastosuje ją do reszty pociągnięcia. Bardzo przydatne do porządkowania regionów facegroupów; jeśli facegroup rozciągnął się za daleko, włącz Auto-pick, zacznij pociągnięcie tam, gdzie łatka facegroupu jest poprawna, i przeciągnij do krawędzi, aby przypisać poprawną łatkę.

### ![](/icons/tool_hide.webp) Ukryj {#hide}
Ukrywa lub izoluje części obiektu. 

Główne tryby są kontrolowane z lewego menu:

* `Dot` - Maluj po obiekcie, aby ukrywać jego części.
* `Shape selector` -  Ukrywa za pomocą kształtów zamiast pędzla, poprzez `Lasso`, `Polygon`, `Line`, `Rect` i `Ellipse`. Zobacz [Shape Selector](#shape-selector), aby uzyskać więcej informacji.
* `Show` - Odwraca operację, więc wybrany tryb będzie pokazywać zamiast ukrywać części obiektu.

Na górze widoku pojawi się pasek narzędzi z dodatkowymi kontrolkami:

* `Clear` - Przywraca obiekt, wszystkie ukryte części zostaną odkryte.
* `Invert` - Zamienia ukryte i odkryte części.
* `Facegroup` - Używa facegroupów do szybkiego ukrywania sekcji, stuknięcie facegroupu ukryje cały facegroup.
* `Mask` - Jeśli maska jest aktywna, stuknięcie tego przycisku ukryje zamaskowaną sekcję.
* `Delete` - Usuwa ukrytą część obiektu
* `Split` - Dzieli ukrytą część obiektu na nowy kształt.

### ![](/icons/tool_measure.webp) Pomiar {#measure}
Przeciągnij, aby zmierzyć odległość między 2 punktami.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

To narzędzie konwertuje zaznaczony obiekt na czysty układ topologii quadów, z kontrolą gęstości, przepływu krawędzi, symetrii. 

::: tip
Quad Remesher jest rozwijany przez [Exoside](https://exoside.com/) dla iOS i desktopu. 

Dla iOS jest to zakup w aplikacji w Nomadzie, jednorazowa opłata 16 USD.

Dla desktopu kup licencję od [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Możesz kupić ją tylko dla Nomad desktop lub licencję krzyżową dla wszystkich obsługiwanych aplikacji desktopowych.

Jeśli już posiadasz Quad Remesher dla innej aplikacji desktopowej, możesz [kupić upgrade na wszystkie platformy taniej.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher nie jest dostępny na Androida. Android może używać darmowego, otwartoźródłowego „Quad Remesh - Instant” dostępnego w menu Topology -> Misc, ale pamiętaj, że jego zestaw funkcji jest bardzo ograniczony.
:::

When to narzędzie zostanie aktywowane po raz pierwszy, zapyta, czy chcesz je włączyć jako zakup w aplikacji. Po aktywacji lewy i górny pasek narzędzi zostaną włączone.

* `Dot` - Ten pędzel ustawia docelową gęstość. Intensywność 100% będzie malować na czerwono, co spowoduje użycie dwukrotnej docelowej gęstości quadów w tych obszarach. Intensywność 0% będzie malować na cyjanowo, co spowoduje użycie połowy docelowej gęstości quadów w tych obszarach. Intensywność 50% będzie malować na szaro, co spowoduje użycie domyślnej docelowej gęstości quadów.
* `Smooth` - Wygładza przejścia gęstości czerwony/szary/cyjan.
* `Curve` - Szkicuj krzywe na powierzchni rzeźby, quad remesher użyje ich jako prowadnic dla przepływu krawędzi. Stuknij krzywą, aby ją usunąć.
* `Path` - Rysuj ścieżki na powierzchni rzeźby, quad remesher użyje ich jako prowadnic dla przepływu krawędzi. Stuknij ścieżkę, aby ją usunąć. 
* `Rect` - Rysuj prostokąty na powierzchni rzeźby, quad remesher użyje ich jako prowadnic dla przepływu krawędzi. Stuknij ścieżkę, aby ją usunąć.
* `Ellipse` - Rysuj elipsy na powierzchni rzeźby, quad remesher użyje ich jako prowadnic dla przepływu krawędzi. Stuknij ścieżkę, aby ją usunąć.

#### Górny pasek narzędzi Quad Remeshera {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Na górze widoku pojawi się pasek narzędzi z dodatkowymi kontrolkami:


* `<Count>` - Kliknij, aby rozpocząć proces quad remeshera, ta liczba informuje, jaka będzie docelowa liczba quadów.
* `Quads` - Ustaw docelową liczbę quadów, przesuwając w lewo i prawo lub stuknij, aby ustawić dokładną liczbę. Zauważ, że jest to bardziej wskazówka niż sztywna wartość – różne kontrolki quad remeshera często sprawią, że wynik nie będzie dokładnie odpowiadał temu celowi.
* `Half` - Skrót ustawiający wartość docelową na połowę bieżącej liczby polygonów.
* `Same` - Skrót ustawiający wartość docelową na bieżącą liczbę polygonów.
* `Guides` - wskazuje całkowitą liczbę prowadnic lub stuknij, aby usunąć wszystkie prowadnice.
* `Density X` - stuknij, aby usunąć całe malowanie gęstości.
* `Density (painting)` - przełącznik używania lub ignorowania malowania gęstości.
* `Face Group` - przełącznik używania lub ignorowania grup powierzchni (facegroups) do sterowania quad remesherem.
* `Relax` - przełącznik automatycznego relaksowania granic grup powierzchni podczas quad remeshingu. Jeśli granice grup powierzchni zostały już zrelaksowane/wygładzone, wyłącz tę opcję.
* `Relax Slider` - Skrótowy suwak do relaksowania granic grup powierzchni.
* `Hard Edges` - przełącznik próby zachowania twardych krawędzi.
* `Reproject Vertex` - przełącznik reprojekcji nowego układu na siatkę wejściową.
* `Symmetry` - Przełącznik włączający symetryczny wynik. Zauważ, że symetria jest zawsze obliczana względem osi X świata, więc upewnij się, że model znajduje się w punkcie początkowym (origin), jeśli oczekujesz symetrycznego rezultatu.
* `...` - menu ustawień Quadremeshera. 

#### Menu ustawień Quad Remeshera {#quad-remesher-settings-menu}

Większość tych ustawień jest dostępna na górnym pasku narzędzi.

* `<Count>, Half, Same` - To samo co przyciski Remesh, Half, Same na górnym pasku narzędzi.
* `Target Quads` - To samo co przycisk `Quads` na górnym pasku narzędzi.
* `Adaptive quad count` - przełącznik włączający używanie mniejszych quadów w obszarach o dużej krzywiźnie i większych quadów w obszarach o mniejszej krzywiźnie.
* `Adaptive size` - Ustawia poziom adaptacyjności. 100% pozwoli na maksymalny adaptacyjny rozmiar, przy 0% quady będą jednolite.
* `Auto-Detect Hard Edges` - przełącznik dostosowujący układ quad remesha tak, aby lepiej podążał za ostrymi powierzchniami.
* `Density (painting)` - To samo co przycisk `Density (painting)` na górnym pasku narzędzi.
* `Reproject Vertex` - przełącznik reprojekcji nowego układu na siatkę wejściową.
* `Face Group` - To samo co przycisk `Face Group` na górnym pasku narzędzi.
* `Relax Slider` - Skrótowy suwak do relaksowania granic grup powierzchni.

::: tip

Przepis na uzyskanie dobrego quad remesha z minimalnymi artefaktami:

* Podziel siatkę na grupy powierzchni (Facegroup), aby zdefiniować idealny przepływ quadów.
* Użyj Facegroup relax, aby uzyskać gładkie granice grup powierzchni.
* Przeprowadź Decimate. Zapewni to brak cienkich lub zniekształconych ścian na krawędziach grup powierzchni. W ustawieniach decimate upewnij się, że Facegroup jest włączone. Sprawi to, że krawędzie trójkątów będą dokładnie podążać za krawędziami grup powierzchni. 

W opcjach quad remesha upewnij się, że relax jest wyłączony (ponieważ siatka została już zrelaksowana), a powinieneś uzyskać dobre rezultaty.

:::

### ![](/icons/tool_select.webp) Zaznacz {#select}
Użyj trybów kształtu, aby zaznaczać obiekty na scenie. `Unselect` usunie obiekty z zaznaczenia.

### ![](/icons/tool_view.webp) Widok {#view}
To „narzędzie” nie robi nic szczególnego, jest to po prostu sposób na oglądanie modelu bez modyfikowania sceny.


## Menu kontekstowe zestawu narzędzi {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Kliknięcie prawym przyciskiem myszy lub długie przytrzymanie narzędzia w skrzynce narzędzi wywoła menu kontekstowe. Menu to ma następujące opcje:

* `Save` - zapisz wszelkie zmiany wprowadzone w narzędziu
* `Clone` - zduplikuj narzędzie jako nowy skrót narzędzia
* `Last save` - przywróć poprzednio zapisaną wersję narzędzia
* `Icon` - zmień ikonę narzędzia
* `Reset` - zresetuj narzędzie do wartości domyślnych