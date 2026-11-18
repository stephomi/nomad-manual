# ![](/icons/sliders.webp) Menu Interfejs {#interface-menu}

To menu zawiera wiele opcji dostosowywania interfejsu Nomada. 

![](/images/interface_overview2.webp)

Nomada można dopasować do siebie bardzo dokładnie; to menu dzieli się na 5 kart: Interfejs, Skróty, Gest, Powiązania i Debuguj.

![](/images/interface_menu.webp)


::: tip
Ta strona opisuje menu Interfejs, a nie sam interfejs! Ogólny interfejs jest opisany w [Pierwszych krokach](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interfejs {#interface}

Karta Interfejs określa kolory, rozmiar i układ interfejsu Nomada. Ma dwie podkarty: `Wygląd` i `Układ`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Kolory {#presets}

![](/images/interface_presets.webp)

Podkarta `Wygląd` zaczyna się od zestawu gotowych schematów kolorów interfejsu. Stuknij jeden, aby go zastosować, a potem dopracuj go opcjami poniżej.

#### Akcent i Podstawowa {#color-widgetcolor-base}
Główne kolory interfejsu: `Akcent` dla zaznaczonych przycisków i pasków suwaków, `Podstawowa` dla paneli.

#### Krycie tekstu {#text-opacity}
Łagodzi kontrast tekstu i ikon względem paneli.

#### Przełączniki, Pole wyboru, Karty {#high-contrast-button}
Styl przełączników (`Miękkie` lub `Pełne`), pól wyboru (`Kontur`, `Akcent` lub `Wypełnienie`) i kart (`Podkreślenie`, `Miękkie` lub `Pełne`).

#### Kolorowe narzędzia {#colored}
Koloruje ikony według kategorii, np. wszystkie narzędzia maski są brązowe, narzędzia podziału czerwone, narzędzia spłaszczające zielone itd.

#### Cień paneli {#material-color-preview}
Panele rzucają cień, który odróżnia je od sceny.

#### Przezroczysty panel {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Po włączeniu pojawiają się dodatkowe opcje wyglądu menu i paneli w Nomadzie: `Odcień paneli` ustala ich kolor, `Siła rozmycia` to, jak bardzo rozmyta jest scena za nimi, a `Szkło` dodaje załamanie światła i odblaski na krawędziach, najlepiej widoczne przy słabym rozmyciu.

::: tip
Na małych urządzeniach warto ustawić odcień paneli na prawie biały, przezroczysty, ze słabym rozmyciem, żeby menu nie zasłaniały sceny.
:::

#### ![](/icons/reset.webp) Przywróć wygląd {#reset-style}
Przywraca domyślne wartości wszystkich opcji wyglądu.

### ![](/icons/panel_detach.webp) Układ {#layout}

Podkarta `Układ` określa, gdzie znajdują się elementy i jak są duże.

#### Przybornik {#toolbox}

Opcje menu narzędzi po prawej stronie interfejsu Nomada.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Zmień rozmiar {#ui-resize-corner}

Włącza uchwyt zmiany rozmiaru w dolnym rogu przybornika.

##### Ukryj {#hidden}
Zwykle ikona przybornika na górnym pasku przełącza między długą pojedynczą kolumną a listą narzędzi w wielu kolumnach. Ta opcja sprawia, że przełącza między listą w wielu kolumnach a ukryciem przybornika.

##### Zresetuj kolejność {#reset-order}
Przywraca domyślną kolejność narzędzi w przyborniku. Własne ikony pozostają w przyborniku na końcu listy.

#### Górny pasek {#rows-auto-1}
`Responsywność` określa, co robi górny pasek, gdy nie mieści się na ekranie, co ma znaczenie głównie na małych ekranach: `Wiele linii` zawija menu w kilka linii, a `Przewiń` zostawia jedną linię, którą można przewijać.

#### Odbij górny pasek {#mirror-top-bar}
Odwraca kolejność menu na górnym pasku.

#### Odbij paski boczne {#mirror-side-bars}
Zamienia paski boczne miejscami, tak że przybornik jest po lewej, a opcje narzędzi po prawej.

#### Odbij dolny pasek {#mirror-bottom-bar}
Przenosi dolny pasek do prawego dolnego rogu i odwraca kolejność przycisków.

#### ![](/icons/move.webp) Przeciągaj panel {#drag-panel}
Pływający panel zawsze przesuwasz, przeciągając jego pasek; ta opcja pozwala przeciągać go także za resztę panelu. W trybie `Auto` palec lub rysik przesuwa panel tylko wtedy, gdy ruch jest bardziej poziomy niż pionowy, więc przeciągnięcie w pionie nadal przewija zawartość. Ustaw `Tak`, aby przeciągać panel również myszą, w dowolnym kierunku.

#### ![](/icons/pencil.webp) Użyj okna dialogowego Nomad {#use-nomad-dialog}
Gdy wpisujesz nazwę lub wartość, pokazuje własne okno tekstowe Nomada zamiast systemowego.

#### ![](/icons/stylus.webp) Kropka przy najechaniu {#hover-dot}
Pokazuje w interfejsie małą kropkę, gdy wykryty zostanie rysik zawieszony nad ekranem.

#### ![](/icons/help.webp) Pomoc po najechaniu {#help-popup-on-hover}

Na urządzeniach obsługujących najeżdżanie określa, czy pomoc kontekstowa Nomada, oznaczona ikoną ![](/icons/help.webp), pojawia się po najechaniu, czy dopiero po stuknięciu.

#### Ogólna skala {#overall-scale}
Mnożnik rozmiaru wszystkich elementów interfejsu.
#### Szerokość panelu {#panel-width}
Szerokość menu i paneli.
#### Skala czcionki {#font-scale}
Skaluje czcionki.
#### Odstęp pionowy {#vertical-spacing}
Odstęp między elementami w menu i panelach.
#### Odstęp pionowy (Lewo) {#vertical-spacing-left}
Odstęp między elementami na lewym pasku narzędzi.

#### Przesunięcia krawędzi {#edge-offset}
Zmieniaj te wartości tylko wtedy, gdy masz problem ze stukaniem w przyciski przy krawędziach ekranu. Jeśli suwaki są wyłączone, Nomad używa wartości bezpiecznego obszaru podawanych przez samo urządzenie.

::: tip
Przy przenoszeniu Nomada na nowe urządzenie (np. z iPhone 12 na iPhone 15) pamiętaj, by przywrócić domyślne wartości przesunięć krawędzi!
:::

#### ![](/icons/reset.webp) Przywróć układ {#reset-layout}
Przywraca domyślne wartości wszystkich opcji układu.

## ![](/icons/window.webp) Skróty {#shortcuts}

Karta Skróty określa, które szybkie przyciski pojawiają się wokół widoku, i pozwala tworzyć własne pływające paski narzędzi.

### Pasek boczny {#side-bar}
Przyciski szybkich narzędzi na dole lewego paska bocznego: `Gładkie`, `Maska`, `Ukryj`, `Grupa powierzchni` i `Gizmo`. Przeciągaj je, aby zmienić ich kolejność.

### Dolny pasek {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Stuknij skrót, aby dodać go do dolnego paska lub z niego usunąć. Domyślnie włączone są:
* `Cofnij` - cofa poprzednią operację
* `Przywróć` - przywraca ostatnio cofniętą operację
* `Solo` - Tymczasowo ukrywa wszystkie inne obiekty, zostawiając widoczny tylko zaznaczony. Naciśnij ponownie, aby przywrócić wszystkie obiekty.
* `Prześwietlenie` - Tymczasowo czyni wszystkie inne obiekty półprzezroczystymi, zostawiając pełny tylko zaznaczony. Naciśnij ponownie, aby przywrócić domyślne materiały.
* `Woksel` - Przebudowuje bieżący obiekt remeshem wokselowym z ostatnio użytą rozdzielczością. Przytrzymanie lub przesunięcie w górę wyświetla suwak rozdzielczości i przełącznik ostrych krawędzi.
* `Siatka` - Pokazuje lub ukrywa siatkę widoku. Przytrzymanie lub przesunięcie w górę pozwala zmienić kolor i krycie siatki.
* `Szkielet` - Włącza lub wyłącza nakładkę szkieletu. Przytrzymanie lub przesunięcie w górę pozwala zmienić kolor i krycie szkieletu.
* `Inspekcja` - pozwala oglądać właściwości siatki, takie jak UV, wypalone tekstury i inne, nałożone na tło Nomada.
* `Grupa powierzchni` - Włącza lub wyłącza nakładkę grup powierzchni, więcej w [Narzędzia->Grupa powierzchni](tools.md#facegroup)

Dostępne są też inne często używane skróty: `Kontur`, `Projekcja` (perspektywiczna lub ortograficzna), `MatCap`, `DynTopo` oraz przyciski [wielokrotnej rozdzielczości](topology.md#multiresolution) `Podziel`, `Odwróć` i poziomów.

#### ![](/icons/more.webp) Powiązania {#bindings-list}

Prawie każdą funkcję Nomada można dodać do dolnego paska przyciskiem powiązań, który pokazuje, ile skrótów zawiera pasek. Po jego stuknięciu pojawia się menu powiązań:

![](/images/interface_bindings_search.webp)

Możesz szukać według kategorii ikonami na górze albo wpisać nazwę funkcji w polu wyszukiwania. Stuknij funkcję, aby dodać ją do paska. Stuknij ponownie, aby ją usunąć.

#### ![](/icons/eye_open.webp) Widoczne {#order}

Pokazuje lub ukrywa cały dolny pasek.

#### ![](/icons/reset.webp) Wyzeruj {#reset}

Przywraca domyślne ustawienia dolnego paska.

### Okna pływające {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Przycisk + dodaje pływający pasek narzędzi. Nie będzie widoczny, dopóki przyciskiem powiązań nie dodasz do niego skrótów; potem możesz go pokazać.

Możesz utworzyć wiele pasków, a każdy ma wiersz z tymi opcjami:

* Przeciągnij uchwyt po lewej stronie wiersza, aby zmienić kolejność pasków.
* `Nazwa` - Nazwa paska narzędzi.
* `Widoczne` - Pokazuje lub ukrywa pasek.
* `Pasek` - Pokazuje pasek tytułu nad paskiem narzędzi.
* `Minimalny` - Zostawia pasek na ekranie, gdy interfejs jest zminimalizowany.
* `Powiązania` - Otwiera okno powiązań, w którym dodajesz funkcje do paska lub je z niego usuwasz.
* `Usuń` - Usuwa pasek narzędzi.


## ![](/icons/gesture.webp) Gest {#gesture}
Menu Gest określa, jak palec, rysik, mysz i gładzik sterują Nomadem.

![](/images/interface_gesture.webp)

### Opcje gestów {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad może ograniczać operacje w zależności od urządzenia wejściowego. Na przykład przeciągnięcie palcem może tylko poruszać kamerą, a przeciągnięcie rysikiem tylko rzeźbić. Jeśli masz mysz lub gładzik, je też możesz przypisać do określonych operacji.

Każdy wiersz to jedna operacja: włącz `Palec`, `Piórko` i `Mysz`, aby wybrać, które urządzenia mogą ją wykonywać.

* `Aparat` - Porusza kamerą.
* `Edycja węzła` - Przeciąganie uchwytów rysowanych w widoku, na przykład przy edycji prymitywu, krzywej, repeatera czy światła.
* `Rzeźbienie` - Rzeźbienie pędzlami. Narzędzia, które mają poniżej własny wiersz, stosują się do niego.
* `Wybierz obiekt` - Stuknięcie obiektu zaznacza go.
* `Wybór materiału` - Przytrzymanie w widoku pobiera kolor lub materiał spod kursora. Działa tylko wtedy, gdy bieżący pędzel ma włączone malowanie.
* `Po stuknięciu` - Skróty stuknięć narzędzi takich jak Maska, Ukryj i Grupa powierzchni (patrz niżej).
* `Malowanie` - Narzędzia Farba i Smużenie.
* `Maska` - Narzędzie Maska.
* `Ściana` - Narzędzia Ukryj i Grupa powierzchni.
* `Utwórz` - Narzędzia Rura, Bryła obrotowa i Wstaw.
* `Wytnij` - Narzędzia Przytnij, Podziel i Rzutuj.
* `Wybierz` - Narzędzia Wybierz i Zmierz.
* `Gizmo` - Narzędzia Gizmo i Krata.
* `Przekształcenie` - Narzędzia Przekształcenie i Rozmieść.

::: tip
Na tablecie często ustawia się tak, by rzeźbić i malować mógł tylko rysik, a palce służyły do kamery. Dzięki temu dłoń czy przypadkowy palec nigdy nie zostawią pociągnięcia na modelu.
:::

### ![](/icons/tool_smooth.webp) Palec zawsze wygładza {#finger-always-smooths}
Gdy opcja jest włączona, palec zawsze wygładza, gdy aktywne jest narzędzie do rzeźbienia, niezależnie od pędzla. Włączenie jej usuwa `Palec` z wiersza `Rzeźbienie`, więc rysik rzeźbi, a palec wygładza.

### Zezwól na ruch poza obiektem {#allow-air-stroke}
Pozwala rozpocząć pociągnięcie, nawet jeśli kursor najpierw trafi poza siatkę. Wybierz narzędzia, których to dotyczy: `Narzędzie` (wszystkie pozostałe pędzle), `Gładkie`, `Maska` i `Ukryj`. Działa tylko dla urządzeń, które mogą rzeźbić, ale nie poruszają kamerą, więc te przyciski są wyłączone, dopóki któreś z twoich urządzeń nie zostanie tak ustawione.

### ![](/icons/stroke.webp) Przyciąganie pociągnięcia {#stroke-snap}
Zatrzymaj kursor na końcu pociągnięcia, aby zamienić je w prostą linię lub gładką krzywą. Przeciągaj dalej, aby obracać i skalować przyciągnięte pociągnięcie wokół jego punktu początkowego.

`Czas przytrzymania` określa, jak długo musisz trzymać kursor nieruchomo, zanim pociągnięcie zostanie przyciągnięte albo kształt przejdzie w tryb edycji.

### ![](/icons/stylus.webp) Użyj dodatkowych próbek wejściowych {#use-extra-input-samples}
Używa dodatkowych próbek wejściowych zgłaszanych przez urządzenie. Wyłącz tę opcję, jeśli pociągnięcia są poszarpane albo nacisk działa niepoprawnie. Ta opcja nie jest widoczna na iOS.

### ![](/icons/tool_mask.webp) Maska {#mask}

![](/images/interface_gesture_mask.webp)

`Skróty jednym stuknięciem` - Włącza poniższe skróty jednym stuknięciem bez przytrzymywania przycisku maski. Dostępne są wtedy gesty:
* stuknięcie tła odwraca maskę
* stuknięcie zamaskowanego obszaru rozmywa maskę
* stuknięcie niezamaskowanego obszaru wyostrza maskę

#### Naciśnięcie i przytrzymanie {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Przytrzymanie w narzędziu Maska przełącza między pędzlem maski a lassem (SelMask):
* `Naciśnięcie i przytrzymanie - Rzeźbienie` - Przytrzymaj i przeciągaj dalej: pociągnięcie jest rysowane w drugim trybie, a poprzedni wraca po jego zakończeniu.
* `Naciśnięcie i przytrzymanie - Przełącz` - Przytrzymaj i puść bez ruszania, aby przełączyć między tymi trybami.

### ![](/icons/tool_smooth.webp) Gładkie {#smooth}
`Naciśnięcie i przytrzymanie - Lasso` - Przytrzymanie w narzędziu Gładkie przełącza na narzędzie Wybierz na czas pociągnięcia zaznaczającego.

### ![](/icons/tool_hide.webp) Ukryj {#hide}
![](/images/interface_gesture_hide.webp)

`Skróty jednym stuknięciem` włącza w narzędziu Ukryj te skróty:
* Stuknięcie grupy powierzchni ukrywa ją
* Stuknięcie pustego miejsca odwraca ukryte wielokąty

### ![](/icons/finger3.webp) Trzy palce {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Jeśli twoje urządzenie obsługuje gesty trzema palcami, możesz przypisać do nich skróty. 

Macierz opcji pozwala przypisać przeciągnięcia w pionie i w poziomie do osobnych skrótów albo wybrać `Nie`, by je wyłączyć. Jeśli ten sam gest zostanie wybrany dla 2 opcji, jedna z nich zostanie wyłączona, a jej nazwa przekreślona.

* `Obróć oświetlenie` - Obraca otoczenie, światła i MatCap.
* `Promień narzędzia` - Zmienia promień narzędzia.
* `Intensywność narzędzia` - Zmienia intensywność narzędzia. 

### ![](/icons/fingerprint.webp) Historia 2/3 {#history-23}
`Skróty historii` - po włączeniu działają te gesty:
* Cofnij - stuknięcie 2 palcami
* Przywróć - stuknięcie 3 palcami

`Naciśnięcie i przytrzymanie` - po włączeniu przytrzymanie 2 lub 3 palców szybko cofa lub przywraca kolejne operacje.

### ![](/icons/mouse.webp) Kółko myszy {#mouse-wheel}
`Prędkość (3d zoom)` określa, jak szybko kółko przybliża widok, a `Prędkość (interfejs 2d)`, jak szybko przewija menu i panele. Przycisk minus obok każdego suwaka odwraca kierunek.

### ![](/icons/fingerprint.webp) Gładzik {#trackpad}
Na Macu `Dwa palce` określa, co robią dwa palce na gładziku. Szczypanie zawsze przybliża, a obracanie palcami zawsze przechyla widok.
* `Wyłączone` - Przewijanie dwoma palcami przybliża, jak kółko myszy. Palce nie są odczytywane osobno.
* `Przesuwanie` - Dwa palce przesuwają widok, a podniesienie jednego z nich obraca. Tak samo jak na tablecie.
* `Obrót orbitalny` - Dwa palce obracają widok, a podniesienie jednego z nich przesuwa.

### Dostępność {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Okno pomocnicze` wyświetla pływający pasek narzędzi do przeciągania, szczypania, przechylania i sterowania kamerą.

### Kamera {#camera}
Skrót do menu `Kamera` (opcje kamery były kiedyś tutaj, ale zostały przeniesione do menu Kamera).

### Dwukrotne stuknięcie ołówkiem → Powiązania {#pencil-tap}

Skrót do menu `Powiązania`, w którym ustawiasz, co robi dwukrotne stuknięcie ołówkiem. Poza iOS opcja nazywa się `Przycisk ołówka → Powiązania` i dotyczy przycisku rysika.

### Odrzucanie dłoni {#palm-rejection}
Na telefonach i tabletach ignoruje dotyk, którego powierzchnia styku przekracza `Maks. próg rozmiaru`, na przykład dłoń opartą o ekran. Może nie działać na każdym urządzeniu, więc wyłącz tę opcję, jeśli masz problem z obsługą widoku.


## ![](/icons/keyboard.webp) Powiązania {#bindings}
Skróty klawiszowe i przyciskowe ustawiasz w menu powiązań:

![](/images/interface_bindings.webp)
Prawie wszystkie funkcje Nomada można przypisać do skrótów klawiszowych, jeśli urządzenie ma klawiaturę, do dodatkowych przycisków rysika, a nawet do kontrolerów do gier.

Aby utworzyć powiązanie, stuknij prostokąt obok funkcji i naciśnij klawisz lub przycisk. 

Funkcje znajdziesz ikonami kategorii na górze albo wpisując nazwę w pasku wyszukiwania. 

Poszczególne powiązania można wyłączyć polem wyboru obok ich nazwy. Przytrzymaj pole wyboru i przeciągnij, aby zmienić kolejność na liście.

Gdy dwa włączone powiązania używają tego samego skrótu, obok nich pojawia się ikona ![](/icons/help.webp), która wymienia kolidujące funkcje.

### ![](/icons/more.webp) Menu kontekstowe {#context-menu}
Ikona ![](/icons/more.webp) za każdym powiązaniem otwiera menu kontekstowe:

![](/images/interface_bindings_context.webp)

* `Klonuj` - Klonuje powiązanie, na przykład by nadać funkcji drugi skrót.
* `Wyzeruj` - Resetuje powiązanie
* `Usuń` - Usuwa powiązanie. Możliwe tylko wtedy, gdy funkcja ma więcej niż jedno powiązanie.

Pod nimi niektóre powiązania mają dodatkowe opcje:

* `Tryb klawiszy` - Dla skrótów narzędzi i szybkich skrótów (Maska, Gładkie, Gizmo, Ukryj, Grupa powierzchni, Dodaj/odejmij) określa, jak naciśnięcie klawisza przełącza narzędzia. `Auto` używa domyślnego ustawienia z opcji [Zaawansowane](#advanced).
  * `Przytrzymaj` - Trzymaj klawisz, aby używać narzędzia, puść go, aby wrócić do poprzedniego narzędzia.
  * `Przełącz` - Jedno naciśnięcie przełącza narzędzie.
  * `Szybkie naciśnięcie` - Przytrzymaj, aby użyć narzędzia chwilowo, albo naciśnij krótko, aby się na nie przełączyć.
* `Przytrzymaj Cofnij` - Dla szybkich skrótów określa, czy puszczenie przytrzymanego klawisza zawsze wraca do poprzedniego narzędzia, nawet gdy to narzędzie było już aktywne.
* `Przełącz poprzednie narzędzie` - Dla skrótów narzędzi: naciśnięcie skrótu bieżącego narzędzia wraca do ostatniego narzędzia. Wymaga `Tryb klawiszy` ustawionego na `Przełącz` lub `Szybkie naciśnięcie`.
* `Pozycja` - Dla skrótów okien pływających: otwiera okno tam, gdzie było (`Zachowaj poprzedni`), lub pod kursorem (`Przy kursorze`).
* `Przesuwanie (po zwolnieniu)` / `Powiększanie (po zwolnieniu)` - Dla powiązań przybliżania i przesuwania kamery: po puszczeniu klawisza przełącza na drugie z nich.
* Kierunek przeciągania - Dla `Obróć oświetlenie`, `Promień narzędzia` i `Intensywność narzędzia` wybiera przeciąganie w poziomie lub w pionie.
* `Synchronizacja` - Dla funkcji, które dodają, klonują lub tworzą instancje obiektów, określa, czy wynik ma być synchronizowany. Domyślnie używa ustawienia synchronizacji z menu Scena.
* `Na tle` - Dla szybkich skrótów Gładkie i Maska: przeciąganie po tle z wciśniętym klawiszem rysuje lasso, zaznaczające dla Gładkie i maskujące dla Maska.
* `Wymuś kamerę` - Dla powiązań kamery: porusza kamerą, nawet jeśli ten sam skrót jest używany przez inne powiązanie, zwykle skrót narzędzia lub Dodaj/odejmij.
* `Obrót liniowy` - Dla powiązania przechyłu: przechyla widok przeciąganiem w poziomie, w pionie lub po przekątnej, zamiast ruchem wokół punktu obrotu.

::: tip
Z `Szybkie naciśnięcie` jeden klawisz robi obie rzeczy: przytrzymaj go, by szybko wygładzić lub zamaskować i wrócić do pędzla po puszczeniu, albo stuknij, by zostać przy tym narzędziu.
:::

### ![](/icons/cog.webp) Zaawansowane {#advanced}
Na dole menu powiązań jest menu z kołem zębatym z opcjami zaawansowanymi:

![](/images/interface_bindings_advanced.webp)

* `Szybkie skróty` - Domyślne `Tryb klawiszy` i `Przytrzymaj Cofnij` dla skrótów Maska, Gładkie, Gizmo, Ukryj, Grupa powierzchni i Dodaj/odejmij.
* `Skróty narzędzi` - Domyślne `Tryb klawiszy` i `Przełącz poprzednie narzędzie` dla skrótów narzędzi. Z `Przełącz poprzednie narzędzie` możesz przełączać się między dwoma narzędziami tym samym klawiszem.
* `Okno skrótów` - `Tryb klawiszy` skrótów, które pokazują okna pływające.
* `Odwróć zoom Y` - Odwraca kierunek przeciągania w pionie przy przybliżaniu powiązaniem.
* `Obrót liniowy` - Przechyla widok przeciąganiem w poziomie, w pionie lub po przekątnej, zamiast ruchem wokół punktu obrotu.
* `SpaceMouse` - Włącza obsługę 3Dconnexion SpaceMouse. W niektórych systemach pojawiają się dodatkowe opcje: czym porusza (`Obiekt`, `Kamera`, `Pierwsza osoba`, `Dron`), `Automatycznie aktualizuj punkt obrotu`, czyli przenoszenie punktu obrotu na powierzchnię pod kursorem, gdy zaczyna się ruch, oraz prędkości `Przesuwanie`, `Powiększanie` i `Obrót`.
* `Strefy martwe (dryf)` - Dla kontrolerów `Gamepad`, `Joystick` i `Przycisk`. Zwiększ te wartości, jeśli kamera porusza się, gdy nie dotykasz kontrolera.
* `Promień narzędzia` - Jak przeciąganie powiązaniem promienia zmienia rozmiar pędzla (`Okrąg`, `Wyśrodkowany` lub `dx`), a następnie ile powiązania promienia dodają (w pikselach) lub mnożą przy każdym naciśnięciu.
* `Intensywność narzędzia` - Ile powiązania intensywności dodają lub mnożą przy każdym naciśnięciu.
* `Kamera - Szybkość` - Prędkości `Przesuwanie` i `Obrót` powiązań, które przesuwają i obracają widok.
* `Resetuj powiązania` - przywraca domyślne wszystkie powiązania.
* `Zresetuj kolejność` - przywraca domyślną kolejność listy powiązań.


## Wyświetlanie skrótów klawiszowych ⌘ na iOS {#ios-keyboard-shortcuts-display}

Na urządzeniach z iOS z klawiaturą przytrzymaj klawisz ⌘ (cmd), aby wyświetlić listę skrótów.

Obsługa klawiatury na Androidzie jest nieco eksperymentalna.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debuguj {#debug}
W tym menu są opcje eksperymentalne i debugowania. Większość z nich należy zostawić z wartościami domyślnymi i zmieniać tylko po kontakcie z pomocą techniczną Nomada. Ikony na górze przenoszą do poszczególnych sekcji.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalizuj UV` - Nomad normalizuje UV zaznaczonej siatki do kafelka [0-1].

### ![](/icons/sun.webp) Cieniowanie {#render}
* `Zapis głębokości refrakcji (tył)` - Tylne ściany siatek z refrakcją są zapisywane do bufora głębokości.
* `Gładkie normalne ważone kątem` - Zmiana w działaniu płynnego cieniowania, która w niektórych przypadkach pozwala uniknąć zagnieceń.

### ![](/icons/speed.webp) Docelowe FPS {#target-fps}
Gdy opcja jest wyłączona, Nomad synchronizuje liczbę klatek na sekundę z częstotliwością odświeżania ekranu.

Gdy jest włączona, możesz ustawić, ile klatek na sekundę renderuje Nomad.

### ![](/icons/window.webp) Interfejs {#debug-interface}
* `Przybornik: pokaż wszystko` - Nomad ukrywa narzędzia, które nie mają zastosowania przy bieżącym zaznaczeniu, np. wszystkie pędzle rzeźbiarskie są ukryte na niezatwierdzonych prymitywach. Ta opcja przyciemnia wyłączone narzędzia zamiast je ukrywać.

Pozostałe opcje interfejsu, które kiedyś były tutaj, znajdują się teraz w karcie [Interfejs](#interface).

### ![](/icons/turntable.webp) Obrotnica {#gif-turntable}
Nomad potrafi wyeksportować animowany GIF z obracającym się modelem. Z powodu ograniczeń formatu GIF jakość jest niska. Nagrywanie ekranu zwykle sprawdza się lepiej.

* `Czas trwania` - ile sekund trwa obrót
* `Maks. próbkowanie klatek` - Wiele efektów wysokiej jakości w renderowaniu Nomada powstaje przez łączenie kilku klatek. Ten suwak ustala, ile klatek połączyć, a jego pole wyboru włącza lub wyłącza tę funkcję.
* `Centrum obrotu` - wokół czego obraca się kamera: `Zachowaj aktualne` zachowuje bieżący punkt obrotu, `(0, 0, 0)` używa środka świata, a `Scena` środka sceny.
* `Przezroczyste tło` - Używa przezroczystości w GIF-ach. GIF obsługuje tylko 1-bitową przezroczystość, więc krawędzie mogą być mocno poszarpane.
* `Eksportuj (GIF)` - rozpoczyna eksport GIF-a.

### ![](/icons/postprocess.webp) Postprocessing {#post-process}
* `Filtrowanie` - Opcja debugowania
* `Format` - Opcja debugowania
* `Ponowne użycie buforów` - Opcja debugowania

### ![](/icons/ram.webp) Wydajność {#performance}
* `Wielowątkowość: ogólna` - Opcja debugowania
* `Wielowątkowość: rzeźbienie` - Opcja debugowania
* `Rysuj powtórzenia przez instancje` - Rysuje wszystkie kopie repeatera jednym wywołaniem rysowania. Opcja debugowania.

### ![](/icons/star.webp) Funkcja {#feature}
* `nom: kompresja multires` - Zmniejsza rozmiar projektów i eksportów Nomada, które używają wielokrotnej rozdzielczości. Takich plików nie otworzą starsze wersje Nomada. Ta opcja może w przyszłości zniknąć i stać się domyślnie włączona.
* `Odwróć przekątną czworokąta (dotknięciem)` -  Opcja debugowania

### ![](/icons/bug.webp) Debuguj {#dev}
* `Dzienniki` - Otwiera okno dziennika
* `Rejestruj zdarzenia` - Zapisuje zdarzenia wskaźnika (palec, rysik, mysz) w oknie dziennika, by pomóc zbadać problemy z obsługą wejścia.
* `FPS` - dodaje licznik klatek na sekundę do statystyk widoku.
* `Okno oceny aplikacji` - Opcja debugowania, na iOS i Androidzie.

### ![](/icons/image.webp) Niestandardowe ikony {#custom-icons}
Zastępuje ikony Nomada twoimi własnymi plikami png.
* `Importuj ikony` - Importuje pliki png do `tmp_session/icons`. Każdy zastępuje ikonę bazową o tej samej nazwie. Znikają po ponownym uruchomieniu Nomada.
* `Eksportuj ikony narzędzi` - Kopiuje bazowe ikony `tool_<tool>.png` do `tmp_session/icons`, bez nadpisywania. Możesz je tam edytować i zastosować przyciskiem `Wczytaj ikony ponownie`.
* `Wczytaj ikony ponownie` - Stosuje ikony z `tmp_session/icons`.

### Przebudowa na czworokąty {#quad-remesh}
Opcji przebudowy na czworokąty nie ma już w tym menu: zobacz [Przebudowa na czworokąty](topology.md#quad-remesh-instant) w menu Topologia i narzędzie [Quad Remesher](tools.md#quad-remesher).

### Utwórz miniatury dla sklepu {#make-store-thumbnails}
Renderuje zrzuty ekranu w rozmiarach pasujących do App Store na iOS.
