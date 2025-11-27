# ![](/icons/interface.webp) Menu interfejsu 

To menu kontroluje wiele opcji dostosowywania interfejsu Nomada. 

![](/images/interface_overview2.webp)

Nomad może być dostosowany na bardzo głębokim poziomie, to menu jest podzielone na 4 sekcje: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Ta strona dotyczy menu interfejsu, a nie samego interfejsu! Ogólny interfejs jest opisany w [Getting Started](gettingstarted.md).
:::

## Interface 

Sekcja interfejsu pozwala dodawać skróty, tworzyć pływające paski narzędzi oraz kontrolować kolor, rozmiar i wygląd interfejsu użytkownika Nomada.

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

Dolny pasek narzędzi ma domyślnie włączone następujące skróty:
* `Undo` - cofnij poprzednią operację
* `Redo` - przywróć poprzednio cofniętą operację
* `Solo` - Tymczasowo ukryj wszystkie inne obiekty, pozostawiając widoczny tylko zaznaczony. Naciśnij ponownie, aby przywrócić wszystkie obiekty.
* `X-ray` - Tymczasowo spraw, by wszystkie inne obiekty były półprzezroczyste, pozostawiając tylko zaznaczony obiekt jako pełny. Naciśnij ponownie, aby przywrócić domyślne materiały.
* `Voxel remesh` - Przemeszuj bieżący obiekt, używając ostatnio użytej rozdzielczości wokseli. Długie przytrzymanie lub przesunięcie w górę wywoła suwak rozdzielczości i przełącznik ostrych krawędzi.
* `Grid` - Przełącz widok siatki. Długie przytrzymanie lub przesunięcie w górę pozwoli zmienić kolor i krycie siatki.
* `Wireframe` - Przełącz nakładkę siatki krawędzi. Długie przytrzymanie lub przesunięcie w górę pozwoli zmienić kolor i krycie siatki krawędzi.
* `Inspector` - pozwala wyświetlać właściwości siatki, takie jak UV, wypalone tekstury i inne właściwości, nakładane na tło Nomada.
* `Face Group` - Przełącz nakładkę grup powierzchni, więcej informacji w [Tools->FaceGroup](tools.md#facegroup) 

Inne często używane skróty są dostępne z tego menu, znacznie więcej można znaleźć w przycisku bindings.

#### ![](/icons/more.webp) Bindings

Prawie każdą funkcję Nomada można dodać do paska skrótów za pomocą przycisku bindings. Po kliknięciu przycisku zostanie wyświetlone menu powiązań:

![](/images/interface_bindings_search.webp)

Możesz wyszukiwać według kategorii za pomocą ikon u góry lub użyć pola wyszukiwania, aby znaleźć funkcje po nazwie. Kliknij funkcję, aby dodać ją do paska narzędzi. Kliknij ponownie, aby ją usunąć.

#### ![](/icons/list.webp) Order

Wyświetli listę skrótów. Przytrzymaj długo, a następnie przeciągnij, aby zmienić kolejność skrótów.

#### ![](/icons/reset.webp) Reset

Reset przywróci dolny pasek narzędzi do ustawień domyślnych.

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

Kliknięcie + doda pływający pasek narzędzi. Nie będzie widoczny, dopóki nie klikniesz przycisku bindings i nie dodasz do niego skrótów, a następnie możesz go uczynić widocznym. 

Możesz utworzyć wiele pasków narzędzi, każdy pasek ma w tym menu następujące opcje:

* ![](/icons/checked.webp) `Visible` - Przełącz widoczność paska narzędzi
* ![](/icons/more.webp)`Bindings` - Wyświetl okno powiązań, aby wybrać funkcje do dodania lub usunięcia z paska narzędzi.
* ![](/icons/list.webp)`Order` - Wyświetl menu zmiany kolejności paska narzędzi.
* ![](/icons/reset.webp) `Reset` - Zresetuj pasek narzędzi do stanu domyślnego.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Przełącz uchwyt zmiany rozmiaru w prawym dolnym rogu paska narzędzi.
* ![](/icons/sort_down.webp) `Collapsable` - Przełącz uchwyt zwijania w prawym górnym rogu.
* ![](/icons/trash.webp) `Delete` - Usuń pasek narzędzi.

### Toolbox

Opcje dla menu narzędzi po prawej stronie interfejsu Nomada.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

Przełącz uchwyt zmiany rozmiaru w dolnym rogu paska narzędzi.

#### Hidden
Normalnie ikona toolbox w górnym pasku przełącza się między długą pojedynczą kolumną a wielokolumnową listą narzędzi. Ta opcja przełącza między listą wielokolumnową a ukryciem.

#### Colored
Koloruje ikony według kategorii, np. wszystkie narzędzia maskujące są brązowe, narzędzia dzielące czerwone, narzędzia spłaszczające zielone itd.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
Zresetuj domyślne narzędzia w toolboxie do domyślnej kolejności. Niestandardowe ikony pozostaną w toolboxie na końcu listy.


### Presets

![](/images/interface_presets.webp)

Zbiór kolorystycznych presetów dla interfejsu.

#### High-contrast button
Alternatywny styl przycisków, który sprawia, że są bardziej widoczne, gdy są włączone. Jeśli ustawione na Auto, Nomad użyje tego trybu, gdy kontrast kolorów UI między stanem włączonym/wyłączonym jest niski.

#### Color widget/Color base
Główne kolory używane w interfejsie.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
Po włączeniu pojawią się dodatkowe opcje kontrolujące wygląd menu i paneli w Nomadzie. Można dostosować ich kolor, przezroczystość i poziom rozmycia.

::: tip
Na małych urządzeniach może być użyteczne ustawienie panelu kolorów na prawie biały, przezroczysty i z niską siłą rozmycia, aby menu nie zasłaniały sceny.
:::

----

### Mirror top bar
Odwróć kolejność menu w górnym pasku.

### Mirror side bars
Zamień paski boczne tak, aby toolbox był po lewej, a opcje narzędzi po prawej.

### Mirror bottom bar
Przenieś dolny pasek do prawego dolnego rogu i odwróć kolejność przycisków.

### Material color preview
Gdy wybierasz kolor materiału, podgląd tego materiału jest wyświetlany na aktualnie zaznaczonym obiekcie.

----
### Help popup on hover

Dla urządzeń obsługujących najechanie (hover), włącz, aby pomoc kontekstowa w Nomadzie, reprezentowana ikoną ![](/icons/help.webp), pojawiała się przy najechaniu lub tylko po kliknięciu.

----

### Overall scale
Mnożnik rozmiaru wszystkich elementów UI.
### Panel width
Szerokość menu i paneli.
### Font scale
Skalowanie czcionek.
### Vertical spacing
Odstęp między elementami w menu i panelach.
### Vertical spacing (left)
Odstęp między elementami w lewym pasku narzędzi.

----

### Edge offset
Powinieneś zmieniać te wartości tylko wtedy, gdy masz problemy z interakcją z przyciskami przy krawędziach ekranu. Jeśli te suwaki są wyłączone, Nomad użyje wartości bezpiecznego obszaru zwróconych przez samo urządzenie.

::: tip
Przy przenoszeniu Nomada na nowe urządzenie (np. wymiana iPhone 12 na iPhone 15) upewnij się, że zresetujesz opcje krawędzi do wartości domyślnych!
:::

### Reset style
Zresetuj wszystkie elementy UI do wartości domyślnych.


## Gesture
Menu gestów kontroluje, jak rysik i dotknięcia palcem sterują Nomadem.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad może ograniczać operacje w zależności od urządzenia wejściowego. Na przykład przeciągnięcie palcem może tylko poruszać kamerą, podczas gdy przeciągnięcie rysikiem może tylko rzeźbić. Jeśli masz mysz lub gładzik, można je również przypisać do kontrolowania konkretnych operacji.

Nomad pozwala obecnie ustawić, aby te tryby były kontrolowane przez dowolną kombinację gestów palcem, rysikiem lub myszą:

* Camera
* Sculpt
* Gizmo
* Material picking (przez długie przytrzymanie)
* Select object


`Finger always smooths` - Wygładzanie może być ustawione tak, aby działało tylko przy przeciąganiu palcem.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Włącz następujące skróty na jedno stuknięcie bez konieczności przytrzymywania przycisku mask. Umożliwi to następujące gesty:
* stuknij w tło, aby odwrócić maskę
* stuknij w zamaskowany obszar, aby rozmyć maskę
* stuknij w niezamaskowany obszar, aby wyostrzyć maskę

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Długie przytrzymanie przełączy między Mask i SelMask i rozpocznie nowy pociągnięcie. Po zakończeniu pociągnięcia poprzednie narzędzie zostanie ponownie wybrane. 
* `Tool` - Długie przytrzymanie i puszczenie bez poruszania, aby przełączyć między Mask i SelMask. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` włączy następujące skróty dla narzędzia hide:
* Stuknij w grupę powierzchni, aby ją ukryć
* Stuknij w pustą przestrzeń, aby odwrócić ukryte poligony

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

Jeśli twoje urządzenie obsługuje gesty trzema palcami, skonfiguruj skróty dla tego gestu. 

Macierz opcji pozwala zdefiniować pionowe i poziome przeciągnięcia jako osobne skróty. Zauważ, że jeśli ten sam gest zostanie wybrany dla 2 opcji, jedna zostanie wyłączona.

* `Rotate lighting` - Obracaj środowisko, światła i Matcap.
* `Tool Radius` - Edytuj promień narzędzia.
* `Tool Intensity` - Edytuj intensywność narzędzia. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - po włączeniu aktywne są następujące gesty:
* Undo - stuknij dwoma palcami
* Redo - stuknij trzema palcami

`Long press` - po włączeniu, przytrzymanie 2/3 palców spowoduje szybkie cofanie/ponawianie.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` wyświetli pływający pasek narzędzi do kontrolowania przeciągania, szczypania, obracania i operacji kamery.

### Camera
Skrót do przejścia do menu `Camera` (opcje kamery były kiedyś tutaj, ale zostały przeniesione do menu kamery).

### Pencil double tap -> Bindings 

Skrót do przejścia do menu `Bindings` (opcje pojedynczego i podwójnego stuknięcia Pencil były kiedyś tutaj, ale zostały przeniesione do menu bindings).


## Bindings
Skróty klawiaturowe i przycisków można zdefiniować w menu bindings:

![](/images/interface_bindings.webp)
Prawie wszystkie funkcje w Nomadzie można przypisać do skrótów klawiaturowych, jeśli twoje urządzenie ma klawiaturę, lub do dodatkowych przycisków na rysiku, a nawet kontrolerów gamepada.

Aby utworzyć powiązanie, kliknij prostokąt obok funkcji i naciśnij klawisz/przycisk. 

Znajdź funkcje za pomocą ikon kategorii u góry lub za pomocą paska wyszukiwania, aby znaleźć po nazwie. 

Poszczególne powiązania można wyłączyć za pomocą pola wyboru obok nazwy powiązania.

### ![](/icons/more.webp) Context menu
Ikona ![](/icons/more.webp) za każdym powiązaniem wyświetla menu kontekstowe:

![](/images/interface_bindings_context.webp)

* `Clone` - Sklonuj powiązanie
* `Reset` - Zresetuj powiązanie
* `Delete` - Usuń powiązanie
* `Toggle shortcut on key tap` - Skonfiguruj, czy stuknięcie vs długie przytrzymanie są traktowane inaczej. Po włączeniu stuknięcie aktywuje narzędzie. Długie przytrzymanie aktywuje narzędzie tylko podczas trzymania klawisza, po puszczeniu powróci ono do poprzedniego narzędzia. Czasem nazywane „sticky keys” w innych aplikacjach 3D.

### Advanced
Na dole menu bindings znajduje się menu zębatki dla zaawansowanych opcji:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Stuknięcie standardowych skrótów dla mask, smooth, gizmo, hide, sub przełączy w ten tryb, ale przytrzymanie klawisza przełączy w ten tryb tylko na czas trzymania, a po puszczeniu tryb powróci do poprzedniego. Czasem nazywane „sticky keys” w innych aplikacjach 3D.
* `Toggle tool shortcuts` - Przy użyciu jednego ze skrótów narzędzi, jeśli ten sam skrót zostanie naciśnięty dwa razy, przełączy z powrotem na poprzednie narzędzie. W ten sposób możesz przełączać się między dwoma narzędziami tym samym skrótem.
* `Invert Y (Zooming)` - Odwróci kierunek zoomu
* `Reset bindings` - zresetuj wszystkie powiązania do wartości domyślnych.


## iOS ⌘ Wyświetlanie skrótów klawiaturowych

Na urządzeniach iOS z klawiaturą przytrzymaj klawisz ⌘ (cmd), aby wyświetlić listę skrótów.

Obsługa klawiatury na Androidzie jest nieco eksperymentalna.

![](/images/shortcuts.webp)


## Debug
W tym menu znajdują się niektóre eksperymentalne i debugowe opcje. Wiele z nich powinno pozostać w ustawieniach domyślnych i być zmieniane dopiero po kontakcie z pomocą techniczną Nomada.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - Nomad znormalizuje UV w obrębie kafelka [0-1].

### Quad Remesh
* `Instant Mesh` - Włącz algorytm instant remesh
* `Quadriflow` - Alternatywna metoda quad remesh.

### Render
* `Heightmap` - Zmień widok na renderowanie głębokości sceny. Może to być użyte do tworzenia map alfa do użycia w pędzlach.
* `Refraction write depth (back)` - Tylna strona siatek refrakcyjnych będzie zapisywana do bufora głębokości.
* `Flip Y (normal map)` - Odwróć kanał Y podczas wypalania map normalnych, wymagane przez niektóre silniki gier i renderery.
* `Angle weighted smooth normals` - Modyfikacja sposobu działania gładkiego cieniowania, która może zapobiegać załamaniom w niektórych przypadkach.

### Target FPS
Po wyłączeniu Nomad zsynchronizuje liczbę klatek na sekundę z częstotliwością odświeżania wyświetlacza.

Po włączeniu możesz ustawić liczbę klatek na sekundę, z jaką Nomad będzie renderował.

### Interface
* `Top: layout` 
  * Collapse: Na małych urządzeniach górny pasek zostanie zredukowany do większej liczby podmenu. 
  * Scroll: Jeśli jesteś przyzwyczajony do Nomada na dużych ekranach i wolisz normalny układ, włączenie tego użyje standardowego szerokiego górnego paska, który można przewijać.
  * Multiline: Wyświetl całe górne menu w kilku wierszach.
* `Bottom: draggable popup` - Dolny pasek narzędzi ma kilka przycisków, które wyświetlają okno dialogowe. Jeśli ta opcja jest włączona, te okna dialogowe można przenosić w inne miejsce na ekranie.  
* `Toolbox: show all` - Nomad ukrywa narzędzia, które nie są istotne dla bieżącego zaznaczenia, np. wszystkie pędzle rzeźbiące są ukryte na prymitywach, które nie są zatwierdzone. Ta opcja przyciemni wyłączone narzędzia zamiast je ukrywać.
* `Toolbox: colored` - Koloruje ikony toolboxa w zależności od ich typu.
* `Panel: Drop shadows` - Rysuj cienie pod menu i panelami. Na niektórych starszych urządzeniach może to wpływać na wydajność.
* `Panel: Blending` - Opcja debugowa
* `Pointer: hovering dot` - Dla urządzeń obsługujących najechanie rysikiem wyświetlaj kropkę, gdy rysik unosi się nad menu i panelami.

### Gif turntable
Nomad może eksportować animowany gif typu turntable. Zwróć uwagę, że z powodu ograniczeń formatu gif jakość jest niska. Nagrywanie ekranu jest zwykle lepszą metodą.

* `Duration` - jak długo w sekundach będzie trwał turntable
* `Rotation center` - gdzie znajduje się pivot kamery, a więc wokół której części sceny będzie się obracać kamera
* `Transparent background` - Użyj opcji przezroczystości dla gifów. Zauważ, że gify obsługują tylko 1-bitową przezroczystość, więc krawędzie mogą być mocno postrzępione.
* `Max frame sampling` - Wiele wysokiej jakości efektów renderowania Nomada pochodzi z łączenia kilku klatek. Ten suwak ustawia, ile klatek łączyć.
* `Export (GIF)` - rozpocznij proces eksportu gifa.

### Post Process
* `Filtering` - Opcja debugowa
* `Format` - Opcja debugowa
* `Buffer reuse` - Opcja debugowa

### Performance
* `Multicore general` - Opcja debugowa
* `Multicore sculpting` - Opcja debugowa
* `Partial Drawing` - Funkcja eksperymentalna! Używaj, jeśli rzeźbisz stosunkowo małą część siatki o wysokiej liczbie polygonów. Powinna sprawić, że rzeźbienie będzie płynniejsze, ale nie powinieneś włączać siatki krawędzi! Może też powodować artefakty wizualne podczas pociągnięć pędzlem.

### Feature
* `Flip quad split (on tap)` -  Opcja debugowa
* `Join: merge radius` - Wierzchołki zostaną automatycznie zespawane, jeśli są wystarczająco blisko siebie podczas łączenia siatek. Możesz dostosować promień tym suwakiem.

### Debug
* `Logs` - Wyświetl okno logów
* `App review popup` - Opcja debugowa
* `FPS` - dodaj licznik klatek na sekundę do statystyk widoku.
