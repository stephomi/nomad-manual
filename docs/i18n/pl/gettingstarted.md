# Pierwsze kroki

## Witamy w Nomadzie!

Nomad to aplikacja do rzeźbienia 3D, która działa na wielu urządzeniach, a najlepiej sprawdza się na tabletach z rysikiem czułym na nacisk, np. Apple iPad z Apple Pencil lub Samsung Galaxy Tab z rysikiem.

Aplikacja jest inspirowana desktopowymi programami do rzeźbienia, takimi jak ZBrush i Blender, z naciskiem na łatwy do zrozumienia interfejs, bez rezygnowania z funkcji. Jeśli używałeś wcześniej aplikacji do rzeźbienia 3D, Nomad wyda się bardzo znajomy.

Jeśli to Twój pierwszy raz z rzeźbieniem 3D, warto poznać kilka podstaw.

::: tip Wolisz wideo?
Na YouTube jest teraz BARDZO dużo filmów dla początkujących, oto kilka świetnych linków:

* [Nomad Sculpt Crash Course by Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial by Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS series by SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Warto zajrzeć na główne kanały tych twórców, często publikują nowe poradniki.
:::

## Twój pierwszy model

Po pierwszym uruchomieniu Nomada zobaczysz na ekranie kulę. Po prostu przeciągnij rysikiem po kuli, aby zacząć rzeźbić. Symetria jest domyślnie włączona, aby ułatwić rzeźbienie.

![](/videos/gettingstarted_01.mp4)

Aby powiększyć lub zmniejszyć pędzel, użyj suwaka promienia po lewej stronie.

![](/videos/gettingstarted_02.mp4)

Aby wzmocnić lub osłabić pędzel, użyj suwaka intensywności po lewej stronie.

![](/videos/gettingstarted_03.mp4)

Domyślnym narzędziem jest `Clay tool` i dodaje ono materiał do powierzchni. Aby odejmować materiał z powierzchni, stuknij przycisk `Sub` po lewej. Aby znów dodawać materiał, stuknij ponownie przycisk Sub.

![](/videos/gettingstarted_04.mp4)

Aby wygładzić powierzchnię, stuknij przycisk `Smooth`. Aby wrócić do zwykłego rzeźbienia, stuknij ponownie przycisk Smooth.

![](/videos/gettingstarted_05.mp4)

Aby obrócić widok wokół modelu, przeciągnij w pustej przestrzeni poza modelem.

![](/videos/gettingstarted_06.mp4)

Aby przybliżać i oddalać, użyj gestu szczypania/rozsuwania dwoma palcami.

![](/videos/gettingstarted_07.mp4)

Aby przesunąć kamerę (pan), przyłóż 2 palce do ekranu i przeciągnij.

![](/videos/gettingstarted_08.mp4)

Jeśli popełnisz błąd, dwukrotne stuknięcie dwoma palcami cofnie akcję, możesz też użyć przycisku cofania w lewym dolnym rogu. 

![](/videos/gettingstarted_09.mp4)

::: tip Wersja desktopowa
Na komputerze klawisz alt/opt służy do sterowania kamerą:

* tip przeciągnięcie w pustej przestrzeni = obrót kamery
* alt+tip przeciągnięcie = przesunięcie (pan)
* alt+tip przeciągnięcie, potem puszczenie alt = zoom (tak jak w ZBrushu)

W tabletach Wacom z dwoma lub więcej przyciskami na piórku użyj ustawień Wacoma, aby skonfigurować końcówkę i przyciski w ten sposób:

* tip = lewy przycisk myszy
* dolny rocker = środkowy przycisk myszy
* górny rocker = prawy przycisk myszy

Z tymi ustawieniami możesz sterować kamerą wyłącznie piórkiem:

* górny rocker i ruch w powietrzu = obrót kamery
* dolny rocker i ruch w powietrzu = przesunięcie (pan)
:::

## Dodawanie koloru

Nomad pozwala malować powierzchnię Twojej rzeźby. W menu narzędzi po prawej znajdź narzędzie `Paint` i kliknij je. Na lewym pasku narzędzi pojawi się kolorowa kula. Kliknij ją, aby otworzyć selektor koloru. Wybierz kolor i maluj po swoim modelu.

![](/videos/gettingstarted_10.mp4)

Aby wymazywać, stuknij przycisk `Erase` na lewym pasku narzędzi, a następnie wymazuj po powierzchni. Stuknij ponownie przycisk erase, aby wrócić do trybu malowania.

![](/videos/gettingstarted_11.mp4)

Używając pędzla clay w trybach add/sub, smooth i paint, spróbuj stworzyć prostą kreskówkową głowę:

![](/images/gettingstarted_head1.webp)

## Inne narzędzia

Paleta narzędzi zawiera wiele narzędzi pomagających w rzeźbieniu. Do tej pory używałeś pędzla clay (domyślne narzędzie startowe), smooth i paint. Ponieważ smooth jest używane bardzo często, ma dodatkowy skrót na lewym pasku narzędzi.

Narzędzia w Nomadzie potrafią bardzo wiele, od narzędzi stricte rzeźbiarskich, takich jak move, crease, inflate, po narzędzia takie jak split i trim, które bardziej przypominają narzędzia stolarskie lub ślusarskie. Strona [Tools](tools.md) zawiera więcej informacji.

Spróbuj użyć narzędzi move, crease, inflate i smooth, aby dodać więcej detali do swojej głowy, zmienić jej kształt:

![](/images/gettingstarted_head2.webp)

Skoro znasz już podstawy Nomada, przyjrzyjmy się reszcie interfejsu.

## Interfejs

![](/images/interface_overview1.webp)

* `Top menus` - Menu dające dostęp do większości funkcji Nomada. Menu w lewym górnym rogu dotyczą głównie sceny i obiektów, menu w prawym górnym rogu są związane z narzędziami. Na mniejszych ekranach te menu zostaną złożone, aby zaoszczędzić miejsce.
* `Stats` - Informacje o scenie, aktualnym obiekcie, statusie maski, użyciu pamięci.
* `Nav Cube` - Pomocnik pokazujący, z której strony patrzysz na rzeźbę, a także skrót do przeskakiwania między widokami. Stuknięcie kostki ustawi widok na stukniętą stronę. Przeciąganie kostki będzie ją obracać. Stuknij małe ikony obok kostki, aby wycentrować aktualny obiekt lub zresetować widok do domyślnego.
* `Toolbox` - Narzędzia Nomada są dostępne w tym przewijanym obszarze.
* `Left toolbar` - Suwaki promienia i intensywności dla większości narzędzi, kontekstowe przyciski dla innych narzędzi oraz skróty do symetrii, trybu alt/sub narzędzia, maskowania, wygładzania, gizma i opcji malowania.
* `Bottom toolbar` - Skróty do często używanych funkcji, opisane poniżej.

::: tip Leworęczny?
Możesz odbić lustrzanie położenie i kolejność wszystkich pasków narzędzi, zobacz [Mirror top bar](interface.md#mirror-top-bar) i inne powiązane opcje.
:::

## Dolny pasek narzędzi

![](/images/interface_bottom_toolbar.webp)

* `Undo` - cofa ostatnią operację
* `Redo` - przywraca ostatnio cofniętą operację
* `History` - dostęp do opcji historii, opisanych w menu [History](history.md).
* `Solo` - Przełącza wyświetlanie tylko aktualnego obiektu lub wszystkich obiektów
* `X-Ray` - Sprawia, że wszystkie inne obiekty są renderowane w trybie prześwietlenia (x-ray), a aktualny obiekt jest pełny. Długie przytrzymanie lub przesunięcie w górę pozwoli ustawić kolor i przezroczystość trybu x-ray.
* `Voxel` - Skrót do przycisku [Voxel Remesher](topology.md#voxel-remesher) (voxel remesh). Długie przytrzymanie lub przesunięcie w górę ujawni skróty do ustawienia jakości voxel remesh.
* `Grid` - Przełącza wyświetlanie siatki. Długie przytrzymanie lub przesunięcie w górę ujawni opcje siatki.
* `Wire` - Przełącza nakładkę siatki krawędzi (wireframe). Długie przytrzymanie lub przesunięcie w górę ujawni opcje dla wireframe.
* `Inspect` - Przełącza wyświetlanie dodatkowych danych o aktualnej siatce. Domyślnie wyświetlane są UV, ale długie przytrzymanie lub przesunięcie w górę pozwoli sprawdzić inne właściwości, jeśli istnieją, oraz czy są wyświetlane w tle czy na siatce.

## Kolejne kroki

To, czego powinieneś się nauczyć dalej, zależy od Ciebie i od tego, co Cię interesuje! Oto kilka propozycji:

Chcesz dowiedzieć się więcej o narzędziach do rzeźbienia? Przejdź do sekcji [Tools](tools.md).

Chcesz eksportować swoje modele? Albo importować modele do rzeźbienia? Albo tworzyć obrazy swoich rzeźb? Przejdź do sekcji [Files](files.md).

Chcesz dowiedzieć się więcej o kontrolowaniu poziomu detalu w swojej rzeźbie? Przejdź do sekcji [Topology](topology.md) i poznaj multires oraz decimation.

Chcesz pracować z większą liczbą obiektów? Łączyć proste obiekty i prymitywy w większą scenę? Przejdź do sekcji [Scene](scene.md).

Chcesz nauczyć się *wszystkiego* o Nomadzie? Dobry wybór! Ten podręcznik obejmuje całego Nomada, zawiera mnóstwo porad i trików oraz ma świetną wyszukiwarkę na górze. Użyj nawigacji po lewej, aby dowiedzieć się więcej.

Jeśli wolisz wideo, Holger Schönischka przygotował ogromną kolekcję porad i trików do Nomada na YouTube: https://www.youtube.com/@ProcreateFX/videos


## Uzyskiwanie pomocy

Jeśli nadal masz pytania po przeczytaniu podręcznika i obejrzeniu filmów instruktażowych, są trzy główne sposoby, aby porozmawiać z innymi użytkownikami Nomada lub z deweloperem Nomada:

* Odwiedź forum: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Dołącz do czatu Nomad na Discordzie: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Skontaktuj się bezpośrednio z deweloperem pod adresem support@nomadsculpt.com
