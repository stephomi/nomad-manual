# ![](/icons/play.webp) Pierwsze kroki {#getting-started}

## Witaj w Nomad! {#welcome-to-nomad}

Nomad to aplikacja do rzeźbienia 3d, która działa na wielu urządzeniach, a najlepiej sprawdza się na tabletach z rysikiem czułym na nacisk, np. na iPadzie z Apple Pencil albo na Samsungu Galaxy Tab z rysikiem.

Inspiruje się programami do rzeźbienia na komputery, takimi jak ZBrush i Blender, ale stawia na prosty, zrozumiały interfejs, nie rezygnując przy tym z funkcji. Jeśli używałeś już aplikacji do rzeźbienia 3d, w Nomad szybko poczujesz się jak w domu.

Jeśli rzeźbisz w 3d po raz pierwszy, warto poznać kilka podstaw.

::: tip Wolisz wideo?
Na YouTube jest teraz NAPRAWDĘ dużo poradników wideo dla początkujących, oto kilka świetnych:

* [Szybki kurs Nomad Sculpt (Nomad Sculpt Crash Course), Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Poradnik Nomad Sculpt dla początkujących, Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Seria NOMAD FOR BEGINNERS, SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Warto zajrzeć na główne kanały tych twórców, bo często publikują nowe poradniki.
:::

## Twoja pierwsza rzeźba {#your-first-sculpt}

Po pierwszym uruchomieniu Nomad zobaczysz na ekranie kulę. Wystarczy przeciągnąć po niej rysikiem, aby zacząć rzeźbić. Symetria jest domyślnie włączona, żeby rzeźbienie było łatwiejsze.

![](/videos/gettingstarted_01.mp4)

Aby powiększyć lub zmniejszyć pędzel, użyj suwaka promienia po lewej.

![](/videos/gettingstarted_02.mp4)

Aby pędzel działał mocniej lub słabiej, użyj suwaka intensywności po lewej.

![](/videos/gettingstarted_03.mp4)

Domyślnym narzędziem jest `Glina`, która dodaje materiał do powierzchni. Aby go odejmować, stuknij przycisk `Odejmij` po lewej. Aby znów dodawać, stuknij ponownie przycisk Odejmij.

![](/videos/gettingstarted_04.mp4)

Aby wygładzić powierzchnię, stuknij przycisk `Gładkie`. Aby wrócić do zwykłego rzeźbienia, stuknij go ponownie.

![](/videos/gettingstarted_05.mp4)

Aby obracać widok wokół modelu, przeciągnij w pustym miejscu poza modelem.

![](/videos/gettingstarted_06.mp4)

Aby przybliżyć lub oddalić widok, użyj gestu szczypania dwoma palcami.

![](/videos/gettingstarted_07.mp4)

Aby przesunąć kamerę, połóż 2 palce na ekranie i przeciągnij.

![](/videos/gettingstarted_08.mp4)

Jeśli popełnisz błąd, stuknij 2 palcami, aby cofnąć, albo użyj przycisku cofania w lewym dolnym rogu.

![](/videos/gettingstarted_09.mp4)

::: tip Wersja na komputery
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
:::

## Dodaj kolor {#add-color}

Nomad pozwala malować powierzchnię rzeźby. W menu narzędzi po prawej znajdź narzędzie `Farba` i kliknij je. Na lewym pasku narzędzi pojawi się kolorowa kula. Kliknij ją, aby otworzyć selektor kolorów. Wybierz kolor i maluj po modelu.

![](/videos/gettingstarted_10.mp4)

Aby wymazywać, stuknij przycisk `Wymaż` na lewym pasku narzędzi, a potem wymazuj na powierzchni. Stuknij go ponownie, aby wrócić do malowania.

![](/videos/gettingstarted_11.mp4)

Używając pędzla gliny w trybach dodawania i odejmowania, wygładzania i malowania, spróbuj zrobić prostą kreskówkową głowę:

![](/images/gettingstarted_head1.webp)

## Inne narzędzia {#other-tools}

Paleta narzędzi zawiera wiele narzędzi pomocnych przy rzeźbieniu. Do tej pory używałeś pędzla gliny (domyślnego narzędzia na start), wygładzania i malowania. Wygładzanie jest używane bardzo często, dlatego ma dodatkowy skrót na lewym pasku narzędzi.

Narzędzia w Nomad potrafią bardzo wiele: od typowo rzeźbiarskich, takich jak przenoszenie, bruzda czy napełnianie, po narzędzia takie jak podział i przycinanie, które przypominają raczej narzędzia stolarskie lub ślusarskie. Więcej informacji znajdziesz na stronie [Narzędzia](tools.md).

Spróbuj użyć narzędzi Przenieś, Bruzda, Napełnij i Gładkie, aby dodać głowie więcej szczegółów i zmienić jej kształt:

![](/images/gettingstarted_head2.webp)

Skoro znasz już podstawy Nomad, przyjrzyjmy się reszcie interfejsu.

## Interfejs {#interface}

![](/images/interface_overview1.webp)

* `Górne menu` - Menu, z których korzystasz z większości funkcji Nomad. Menu w lewym górnym rogu dotyczą głównie sceny i obiektów, a menu w prawym górnym rogu są związane z narzędziami. Na mniejszych ekranach te menu łączą się ze sobą, aby oszczędzać miejsce.
* `Statystyki` - Informacje o scenie, bieżącym obiekcie, stanie maski i zużyciu pamięci.
* `Kostka nawigacji` - Pomocnik, który pokazuje, z której strony patrzysz na rzeźbę, a także skrót do przechodzenia między widokami. Stuknięcie kostki przełącza widok na stukniętą stronę. Przeciąganie kostki obraca widok. Małe ikony obok kostki kadrują bieżący obiekt, przywracają domyślny widok początkowy, blokują kamerę lub włączają siatkę. W aplikacji nazywa się `Kostka orientacji`, a jej wygląd i położenie możesz zmienić w [Ustawieniach](settings.md#snap-cube).
* `Przybornik` - Narzędzia Nomad są dostępne w tym przewijanym obszarze.
* `Lewy pasek narzędzi` - Suwaki promienia i intensywności dla większości narzędzi, przyciski zależne od kontekstu dla pozostałych oraz skróty do symetrii, trybu alt/odejmowania narzędzia, wygładzania, maskowania, ukrywania, grup powierzchni, gizmo i opcji malowania. Kolejność skrótów możesz zmienić w menu [Interfejs](interface.md#side-bar).
* `Dolny pasek narzędzi` - Skróty do często używanych funkcji, opisane poniżej.

::: tip Jesteś leworęczny?
Możesz odbić położenie i kolejność wszystkich pasków narzędzi, zobacz [Odbij górny pasek](interface.md#mirror-top-bar) i inne powiązane opcje.
:::

## Dolny pasek narzędzi {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Cofnij` - cofa ostatnią operację
* `Przywróć` - przywraca ostatnio cofniętą operację
* `Historia` - otwiera opcje historii, opisane w menu [Historia](history.md).
* `Solo` - Przełącza między wyświetlaniem tylko bieżącego obiektu a wszystkich obiektów
* `Prześwietlenie` - Wyświetla wszystkie pozostałe obiekty w trybie prześwietlenia, a bieżący obiekt jako pełny. Długie przytrzymanie lub przesunięcie w górę pozwala wybrać matcap i kolor prześwietlenia oraz obiekty, których dotyczy.
* `Woksel` - Skrót do przycisku przebudowy w sekcji [Remesh wokselowy](topology.md#voxel-remesher). Długie przytrzymanie lub przesunięcie w górę pokazuje opcje remeshu wokselowego, takie jak rozdzielczość.
* `Siatka` - Włącza lub wyłącza wyświetlanie siatki. Długie przytrzymanie lub przesunięcie w górę pokazuje opcje siatki, takie jak jej kolor i przyciąganie.
* `Szkielet` - Włącza lub wyłącza nakładkę szkieletu. Długie przytrzymanie lub przesunięcie w górę pokazuje opcje szkieletu.
* `Inspektor` - Włącza wyświetlanie dodatkowych danych o bieżącej siatce. Domyślnie pokazuje UV, ale długie przytrzymanie lub przesunięcie w górę pozwala sprawdzić inne właściwości, jeśli istnieją, oraz wybrać, czy mają być wyświetlane w tle, czy na siatce.
* `Dzienniki` - Pokazuje lub ukrywa okno z dziennikami debugowania Nomad.
* `Grupa powierzchni` - Włącza lub wyłącza nakładkę grup powierzchni, zobacz narzędzie [Grupa powierzchni](tools.md#facegroup).

Skróty te możesz dodawać, usuwać i zmieniać ich kolejność w menu [Interfejs](interface.md#add-shortcuts-bottom).

## Następne kroki {#next-steps}

Czego nauczysz się dalej, zależy od Ciebie i od tego, co Cię interesuje! Oto kilka propozycji:

Chcesz dowiedzieć się więcej o narzędziach do rzeźbienia? Przejdź do sekcji [Narzędzia](tools.md).

Chcesz eksportować swoje modele? Albo importować modele, aby na nich rzeźbić? Albo tworzyć obrazy swoich rzeźb? Przejdź do sekcji [Pliki](files.md).

Chcesz dowiedzieć się więcej o kontrolowaniu szczegółowości rzeźby? Przejdź do sekcji [Topologia](topology.md) i poznaj multirezolucję oraz upraszczanie.

Chcesz pracować z większą liczbą obiektów? Łączyć proste obiekty i prymitywy w większą scenę? Przejdź do sekcji [Scena](scene.md).

Chcesz poznać *wszystko* o Nomad? Dobry wybór! Ten podręcznik opisuje cały program Nomad, zawiera mnóstwo wskazówek i trików, a u góry ma świetną wyszukiwarkę. Korzystaj z nawigacji po lewej, aby dowiedzieć się więcej.

Jeśli wolisz wideo, Holger Schönischka przygotował na YouTube ogromną kolekcję wskazówek i trików do Nomad: https://www.youtube.com/@ProcreateFX/videos


## Gdzie szukać pomocy {#getting-help}

Jeśli po przeczytaniu podręcznika i obejrzeniu poradników wideo nadal masz pytania, możesz porozmawiać z innymi użytkownikami Nomad lub z jego twórcą na trzy główne sposoby:

* Odwiedź forum: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Dołącz do czatu Nomad na Discordzie: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Napisz bezpośrednio do twórcy na adres support@nomadsculpt.com
