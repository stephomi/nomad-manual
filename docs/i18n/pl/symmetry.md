# ![](/icons/symmetry.webp) Symetria {#symmetry}

To menu określa, jak pociągnięcia są powtarzane po drugiej stronie płaszczyzny lustra, promieniście lub jako kafelki, a także pozwala przywrócić symetrię obiektom, które ją utraciły.

![](/images/symmetry_overview.webp) 

## Przegląd {#overview}
Symetrii możesz używać na kilka sposobów:

* Jako lustra, które odbija pracę względem osi X (lewo/prawo), Y (góra/dół), Z (tył/przód) albo ich kombinacji.
* Symetrię radialną można ustawić na osiach X, Y i Z z wybraną liczbą powtórzeń, np. do rzeźbienia rozgwiazdy.
* Kafelkowanie powtarza pociągnięcia na całym obiekcie, tak aby rzeźba układała się w kafelki bez widocznych łączeń.
* Lustro może działać względem początku układu (tryb świata) albo względem środka obiektu (tryb lokalny).
* Rzeźbę, która od początku nie była symetryczna, można wymusić jako symetryczną.

Skrót do włączania i wyłączania symetrii znajdziesz też w lewym panelu szybkiego dostępu (*„Sym”*). Mała litera „L/W” pokazuje, czy Nomad jest w trybie symetrii lokalnej czy świata. Możesz też przytrzymać przycisk albo przeciągnąć go w stronę środka ekranu, aby otworzyć menu.

![](/images/symmetry_button.webp) 

Ustawienia symetrii są zapisywane osobno dla każdego obiektu, a tytuł menu pokazuje nazwę edytowanego obiektu.
Narzędzia do rzeźbienia mają wspólny stan włączenia/wyłączenia, natomiast narzędzia przekształcania ([Przekształcenie](tools.md#transform) i [Gizmo](tools.md#gizmo)) mają własny.

::: tip
Menu symetrii służy głównie do sterowania symetrią pociągnięć. Obiekty możesz też odbijać i powielać za pomocą [repeaterów z menu sceny](scene#repeaters).
:::

## ![](/icons/symmetry.webp) Włączona {#enabled}
Włącza lub wyłącza tryb lustra, tak samo jak przycisk `Sym` w lewym panelu szybkiego dostępu. Gdy symetria jest wyłączona, przypomina o tym ikona ostrzeżenia, a menu informuje też, kiedy bieżące narzędzie ignoruje symetrię.

## Płaszczyzny {#planes}

Włącz płaszczyznę (lub płaszczyzny) symetrii i ustaw liczbę powtórzeń symetrii radialnej. Nie musisz wybierać tylko jednej płaszczyzny: możesz włączyć 1, 2 lub wszystkie 3 płaszczyzny, aby uzyskać złożoną symetrię.

Wiersz `Radialna` ustawia liczbę powtórzeń symetrii radialnej wokół każdej osi. Tu również nie jesteś ograniczony do jednej osi, a symetria radialna może nawet działać razem z symetrią płaszczyzn, dzięki czemu bardzo szybko uzyskasz szczegółowe efekty. (Łączna liczba powtórzeń jest ograniczona do 200).

![](/videos/symmetry_demo.mp4) 

## Kafelkowanie {#tile}

Powtarza pociągnięcia wzdłuż osi w regularnych odstępach, tak aby rzeźba układała się w kafelki bez widocznych łączeń. Przydaje się do wzorów, cegieł albo tekstury, którą planujesz powielać.

Włącz kafelkowanie dla każdej osi przyciskami `Kafelkowanie`, a potem ustaw `Liczba` (ile powtórzeń mieści się na obiekcie) albo `Odległość` (odstęp między dwoma powtórzeniami). Przełącznik po lewej zmienia jedno na drugie.

## Metoda {#method}
Lustro może być `Lokalna` i przesuwać się razem z obiektem albo `Świat` i pozostawać w miejscu. Jeśli nie wiesz, którego trybu potrzebujesz, obserwuj wskaźniki płaszczyzny lustra i symetrii radialnej nałożone na obiekt. W trybie lokalnym, gdy przesuniesz model narzędziami przekształcania (`Gizmo` lub `Przekształcenie`), wskaźniki lustra przesuną się razem z nim. W trybie świata wskaźniki lustra pozostają nieruchome, a obiekt przesuwa się przez nie.

## Lustro {#mirroring}
![](/images/symmetry_mirroring.webp)

Podczas rzeźbienia w pobliżu płaszczyzn symetrii niektóre pędzle nie zachowują idealnej symetrii. Ta sekcja pozwala ją przywrócić, kopiując jedną stronę rzeźby na drugą.

`Kierunek` - Dwa przyciski strzałek obok tytułu `Lustro` określają, która strona zostanie skopiowana na drugą. Nomad wylicza to na podstawie bieżącego widoku, więc strona na ekranie pozostaje ta sama bez względu na to, z której strony patrzysz na model.

![](/icons/shield.webp) `Maska` - Przycisk maski pozwala wyodrębnić to, co zostanie odbite: zamaskowanie strony docelowej chroni ten obszar, a zamaskowanie strony źródłowej sprawia, że ten obszar nie zostanie przeniesiony na stronę docelową.

![](/icons/tool_hide.webp) `Ukryj` - Gdy ta opcja jest aktywna, obszary ukryte po stronie źródłowej nie są odbijane na stronę docelową.

`Lustro` (zachowaj topologię) próbuje ustalić, czy topologia po obu stronach lustra jest taka sama, a jeśli tak, po prostu przesuwa wierzchołki. To najczęstszy przypadek. Symetria radialna jest pomijana. Jeśli topologia nie jest symetryczna, Nomad proponuje wymuszenie odbicia za pomocą `Wytnij • Lustro`.

Przyciski `Wytnij` przecinają obiekt wzdłuż płaszczyzn symetrii. Zmieniają topologię, więc są bardziej destrukcyjne niż `Lustro`. Liczba na każdym przycisku mówi, ile obiektów otrzymasz:

* `Wytnij` - usuwa jedną stronę obiektu.
* `Wytnij • Lustro` - przecina obiekt, kopiuje jedną stronę, odbija ją na drugą i spaja wierzchołki wzdłuż lustra. Ta metoda bywa konieczna, gdy model po obu stronach lustra bardzo się różni.
* `Wytnij • Podziel` - przecina obiekt i zachowuje każdą stronę jako osobny obiekt.
* `Wytnij • Lustro • Podziel` - jak `Wytnij • Lustro`, ale każda strona staje się osobnym obiektem.

Jeśli zaznaczonych jest kilka obiektów, `Lustro` i [Przerzuć obiekt](#flip-object) działają na wszystkie.

### Przerzuć obiekt {#flip-object}
![](/images/symmetry_flip.webp)
Zamienia lewą stronę z prawą i odwrotnie, wzdłuż `X`, `Y` lub `Z`. Wygląda to podobnie, jak gdybyś w menu narzędzia gizmo ustawił skalę -1 na osi X.

## Zerowanie i edycja {#reset-and-edit}

![](/images/symmetry_edit.webp)

Położenie i orientację symetrii można edytować (choć nie jest to zalecane!). W razie potrzeby `Środek świata` (`Środek obiektu` w trybie lokalnym) i `Orientacja` przywracają domyślne położenie i orientację symetrii.

Nomad zwykle wie, gdzie umieścić płaszczyznę symetrii. Nie zaleca się ustawiania jej ręcznie, ale zaawansowani użytkownicy mogą to zrobić przyciskiem `Edycja gizmo`. Po jego kliknięciu pojawia się gizmo, którym możesz przesuwać i obracać płaszczyznę symetrii. Aby przywrócić domyślny środek i orientację, użyj przycisków zerowania powyżej.

`Z Pivotu` umieszcza płaszczyznę symetrii w punkcie obrotu narzędzia [Gizmo](tools.md#gizmo). Ta opcja jest dostępna tylko wtedy, gdy aktywne jest narzędzie `Gizmo`.

Działanie tych opcji zależy od przestrzeni (*Lokalna/Świat*), w której się znajdujesz.
Jeśli więc coś nie działa tak, jak oczekujesz, sprawdź, czy jesteś we właściwej przestrzeni.

::: tip
Edycja płaszczyzny symetrii za pomocą gizmo jest nieco eksperymentalna, raczej nie powinna być Ci potrzebna!
:::

## Opcje wyświetlania {#show-options}
![](/images/symmetry_show.webp)


`Pokaż linię` i `Pokaż płaszczyznę` włączają nakładkę w widoku, pokazującą położenie symetrii. Wyłączenie tych opcji zaczyna działać dopiero po zamknięciu menu symetrii.
