# ![](/icons/manual.webp) Wskazówki {#tips}

[[toc]]

## Jak zacząć model {#how-to-start-a-model}

Początkujący w rzeźbieniu 3d często pytają, jak najlepiej zacząć model. Nie ma jednego najlepszego sposobu, każdy ma swoje upodobania. Oto kilka najpopularniejszych podejść.

### Rzeźbienie na kuli, wielokrotna rozdzielczość {#sculpt-on-sphere-multires}

Model domyślny, z którym uruchamia się Nomad, to najczęstszy punkt wyjścia. Narzędziami do przenoszenia, gliny i bruzd wypychasz i wyciągasz kulę, nadając jej kształt. Gdy chcesz szybko wprowadzić duże zmiany, używaj niższych poziomów podziału, a przy detalach wyższych.

Częsty problem polega na tym, że brakuje wielokątów tam, gdzie są potrzebne, a w innych miejscach jest ich za dużo. Jeśli na przykład wyciągniesz z domyślnej kuli całą postać, prawdopodobnie zabraknie detali na palce, a na tyle głowy zmarnujesz mnóstwo wielokątów. Przy kształtach zbliżonych do kuli, takich jak głowa, może to jednak zupełnie wystarczyć.

### Dyntopo {#dyntopo}

Włączenie Dyntopo sprawia, że podczas rzeźbienia wielokąty są dodawane i usuwane w zależności od potrzeb. Te wielokąty są trójkątami, a początkujący często nie lubią ich chaotycznego układu w porównaniu z czystą siatką wielokrotnej rozdzielczości. Warto jednak wytrwać! Jeśli włączysz płynne cieniowanie, wyłączysz szkielet i przestaniesz przejmować się układem siatki, ten tryb daje wrażenie pracy w prawdziwej glinie. Pamiętaj, że przy dużym pędzlu albo pędzlu wygładzającym ten tryb może też usuwać wielokąty, więc narzędzie zawsze działa szybko i płynnie. Gdy skończysz pierwsze podejście do rzeźby, możesz ją sklonować, przepuścić przez Quad Remesher, by uzyskać ładny układ siatki, i zrzutować oryginalne detale na wysoki poziom podziału.

### Remesh wokselowy {#voxel-remesh}

Remesh wokselowy nadaje rzeźbie topologię złożoną głównie z czworokątów. Przy niższych rozdzielczościach ta operacja jest szybka i pozwala szybko zastąpić rozciągnięte albo zbyt gęste wielokąty równomiernie rozłożoną siatką. To świetny sposób, by zacząć całą postać od kuli: zaczynasz na przykład od głowy, wyciągasz szyję, robisz remesh wokselowy. Wyciągasz tułów, remesh wokselowy, ręce, remesh wokselowy i tak dalej, aż uzyskasz podstawowe bryły.

### Używaj wielu obiektów {#use-multiple-objects}

Wiele podręczników anatomii przedstawia ciało za pomocą prostych kul, walców i sześcianów. W Nomad też możesz tak rzeźbić. Zaletą jest to, że w hierarchii sceny możesz łączyć obiekty w relacje rodzic–dziecko, więc na przykład obracasz szyję, a głowa podąża za nią. Bardzo przydatne jest też narzędzie Gizmo do precyzyjnego przesuwania, obracania i skalowania; możesz też ustawić punkt obrotu każdego kształtu, by poruszał się dokładnie tak, jak chcesz. Gdy podstawowe bryły są na swoich miejscach, możesz zaznaczyć je wszystkie i połączyć w jedną powierzchnię remeshem wokselowym lub operacją Boolean, by rzeźbić dalej szczegóły.

Przydatna sztuczka przy tej metodzie: zacznij od kuli, przeskaluj ją w wydłużoną „kiełbaskę”, naciśnij punkt obrotu, kliknij „dół” i ponownie naciśnij punkt obrotu. Masz teraz część ciała, którą możesz sklonować, przesunąć wzdłuż pierwszej kuli, sklonować, obrócić, sklonować, przesunąć, sklonować itd., by szybko rozplanować całą postać.

### Rury {#tubes}

Narzędzie Rura to świetny sposób na rozpoczęcie rzeźby. Ogony gadów, ręce, nogi, palce, brwi – wszystko to szybko naszkicujesz narzędziem Rura, a potem łatwo zmienisz. Pozwala ono też modyfikować profil przekroju, dzięki czemu szybko zmienisz kształt. Możesz zatwierdzić kształt, by zacząć na nim rzeźbić, i połączyć go remeshem wokselowym z innymi obiektami, by uzyskać siatkę całej postaci.

### Używaj innych aplikacji {#use-other-apps}

Niektórzy wolą zaczynać model w innych aplikacjach – to też jest w porządku. Narzędzia takie jak Blender czy Valence pozwalają zacząć model technikami low poly, a potem zaimportować go do Nomad, by na nim rzeźbić.

### Używaj wbudowanych ustawień wstępnych {#use-the-built-in-presets}

W menu [Pliki](files.md) kliknij `Ustawienie wstępne…` po lewej stronie sekcji projektu. Znajdziesz tam kilka gotowych kształtów głów i ciał od Blender Foundation. Wybierz ten, który Ci się podoba, stuknij go ponownie i dodaj do sceny. 

### Używaj modeli z internetu {#use-online-models}

W internecie dostępnych jest wiele darmowych modeli, na przykład na polyhaven, sketchfab czy turbosquid. Zwykle można je zaimportować do Nomad i rzeźbić bezpośrednio na nich albo używać ich jako referencji.

### Nie ma zasad! {#no-rules}

Ostatecznie możesz łączyć te techniki dowolnie albo nie używać żadnej z nich! Nomad jest pod tym względem bardzo elastyczny: zaawansowani użytkownicy mogą zacząć od rur, potem przejść do dyntopo, dołączyć pobraną stopę, przebudować całość na czworokąty, a na koniec dodać detale w wielokrotnej rozdzielczości. Liczy się to, co działa dla Ciebie.

## Grupy powierzchni {#facegroups}

Narzędzie Grupa powierzchni ma wiele zastosowań, co wyjaśnia ten film na YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Poniżej znajdziesz tekstowe podsumowanie funkcji omówionych w tym filmie.

### Po co grupy powierzchni? {#why-facegroups}

Grupy powierzchni pozwalają porządkować i zaznaczać ściany (w tym podręczniku „ściany” i „wielokąty” oznaczają to samo). Najłatwiej to wyjaśnić w porównaniu z innymi narzędziami Nomad do zaznaczania i porządkowania. Nomad pozwala tworzyć obiekty, nadawać im nazwy i łączyć je w hierarchię, więc łatwo zbudować strukturę obiektów opisującą na przykład pokój złożony z podłogi, ścian, krzesła, stołu i tak dalej.

Przy postaci możesz wstępnie zbudować bryłę z osobnych obiektów na głowę, rękę i nogę, ale gdy połączysz wszystkie części w jedną siatkę, ta struktura znika. Nad fragmentami postaci możesz pracować za pomocą masek, ale ciągłe malowanie maski na dłonie, potem na nos, potem znowu na dłonie bywa męczące.

Tu przydają się grupy powierzchni. Pozwalają oznaczyć ściany wielokątów kolorem, a potem zaznaczać i edytować wielokąty o tym samym kolorze. Pamiętaj, że kolor grupy powierzchni i kolor wierzchołków to dwie różne rzeczy.

Najbliższym porównaniem jest kolorowanie mapy, a potem zaznaczanie państw lub regionów według koloru.

Na głowie postaci możesz pomalować strefy oczodołów, nosa, ust, podbródka i uszu, a potem łatwo je zaznaczać. Przy rzeźbieniu twardych powierzchni i mechanizmów przydaje się to do wyznaczania paneli i sekcji.

### Tworzenie i edycja grup powierzchni {#creating-and-editing-facegroups}

Grupy powierzchni możesz nakładać pędzlem – wtedy każde nowe pociągnięcie tworzy nową grupę – albo pobrać grupę spod kursora i ją rozszerzać. Możesz je też tworzyć za pomocą kształtów.

* Kropka, tryb domyślny – jedno przeciągnięcie tworzy nowy kolor grupy powierzchni i przypisuje go ścianom, po których przeciągasz. Każde nowe przeciągnięcie tworzy nową grupę. Stuknięcie wypełnia obszar nową grupą.
* Kropka, tryb `Wybierz` – gdy przycisk `Wybierz` na lewym pasku narzędzi jest aktywny, Nomad pobiera grupę powierzchni spod kursora i nakłada ją przez resztę przeciągnięcia. Pozwala to dopracowywać grupy bez ręcznego wybierania ich za każdym razem.

### Maskowanie {#masking}

Gdy aktywne jest narzędzie maski, a na jego pasku narzędzi włączony jest przycisk grupy powierzchni, stuknięcie grupy powierzchni ją maskuje.


### Ukrywanie {#hiding}

Gdy aktywne jest narzędzie do ukrywania, a na jego pasku narzędzi włączony jest przycisk grupy powierzchni, stuknięcie grupy powierzchni ją ukrywa.

### Porządkowanie {#organizing}

Jak wspomniano wcześniej, grupy powierzchni pozwalają porządkować siatkę bez tworzenia osobnych obiektów. Możesz nie chcieć dzielić głowy na osobne obiekty na nos, podbródek i uszy, ale bardzo przydaje się mieć je wyznaczone grupami powierzchni.

### Obszary UV {#uv-regions}

Narzędzie UV Atlas próbuje automatycznie wyznaczyć szwy, ale czasem umieszcza je tam, gdzie ich nie chcesz. Jeśli obiekt ma grupy powierzchni, a w opcjach UV Atlas włączona jest opcja grup powierzchni, jako szwy UV zostaną użyte granice grup.

### Quad Remesher {#quad-remesher}

Wtyczka Quad Remesher zwykle ładnie prowadzi krawędzie na modelu, ale gdy włączysz opcję grup powierzchni, możesz nimi pokierować jej działaniem. Ułatwia to uzyskanie czystego przebiegu krawędzi na przykład wokół oczu, łuku brwiowego, ust czy fałdu policzka.

### Filtrowanie w innych narzędziach {#filter-with-other-tools}

Wiele narzędzi ma opcje uwzględniające grupy powierzchni – w głównym menu narzędzia albo w menu Pociągnięcie -> Filtr. Na przykład narzędzie wygładzania z siłą powyżej 100% potrafi mocno wygładzić detale wewnątrz grupy powierzchni, zachowując przy tym względnie nienaruszoną jej granicę.

### Łagodzenie i wygładzanie granic grup powierzchni {#relax-and-smooth-facegroup-borders}

Opcja `Złagodź` w narzędziu Grupa powierzchni świetnie wygładza granice grup, nie naruszając innych elementów. To dobry sposób na uzyskanie gładkich granic grup przed przebudową siatki na czworokąty.

## Ograniczenia tabletów i telefonów {#limitations-on-tabletmobile}

Współczesne tablety i telefony są bardzo wydajne, ale w kilku ważnych kwestiach różnią się od komputerów stacjonarnych i laptopów:

### Brak aktywnego chłodzenia {#no-active-cooling}

Komputery mają wentylatory i/lub duże radiatory, które je chłodzą, i są projektowane do pracy w wysokich temperaturach. Urządzenia mobilne projektuje się przede wszystkim z myślą o smukłości, a nie o chłodzeniu podzespołów. Jeśli wyciśniesz z Nomad najwyższe ustawienia jakości (tryb oświetlenia PBR, złożone materiały, wiele obiektów, wiele włączonych opcji postprocessingu), urządzenie może się przegrzać, a bateria bardzo szybko rozładować. 

Lepiej używać trybu oświetlenia MatCap i niższej wartości `Rozdzielczość renderowania` (na górze menu Postprocessing). Dzięki temu urządzenie pozostanie chłodne, a Ty będziesz mógł rzeźbić dłużej.

### Ograniczona pamięć {#limited-memory}

Nomad może dać efekty dorównujące większości aplikacji do rzeźbienia na komputery, ale nie złamie praw fizyki! Większość komputerów ma dwa razy więcej pamięci niż urządzenia mobilne, a stacje robocze do animacji 3d często 4 lub 8 razy więcej. Dlatego warto pilnować, ile wielokątów używasz, i sprawdzić na swoim urządzeniu, kiedy zaczyna ono zwalniać. Niemal każde urządzenie, na którym działa Nomad, bez trudu radzi sobie z 1 milionem wielokątów. iPad Pro z M2 swobodnie obsłuży 8 milionów, a użytkownicy testowali najnowsze iPady na znacznie większych liczbach.

Mimo to tylko najbardziej szczegółowe rzeźby potrzebują ponad 4 milionów wielokątów. Jeśli tworzysz stosunkowo proste obiekty i często przekraczasz 500 000, 1 milion czy 4 miliony, używasz za dużo wielokątów! Upewnij się, że w [Ustawieniach](settings.md) włączone jest `Płynne cieniowanie`.

### System jest mniej wyrozumiały dla wymagających aplikacji {#os-is-less-forgiving-with-intensive-apps}

Apple i Android oczekują, że aplikacje będą bardzo szybko zapisywać i wczytywać małe pliki. Zakładają też, że aplikacje potrafią błyskawicznie przełączać się między zadaniami. Nomad stosuje sprytne sztuczki, by pliki były względnie małe i zapisywały się bardzo szybko, ale jeśli system mobilny uzna, że Nomad zajmuje mu za dużo czasu, po prostu go zamknie, zanim skończy swoje zadanie. To kolejny powód, by trzymać rozmiar plików w ryzach; da się pracować z rzeźbami liczącymi 37 milionów wielokątów, jak donosił jeden z użytkowników na Discordzie, ale nie jest to zalecane!

## Praca na małych ekranach {#working-on-small-screens}

Nomad jest zaprojektowany z myślą o tabletach, ale dobrze działa też na telefonach. Rzeźbienie na małym ekranie, takim jak w telefonie, ułatwi kilka zmian w interfejsie i sposobie pracy:

* Stuknięcie 4 palcami ukrywa i przywraca cały interfejs, dając więcej miejsca na rzeźbienie.
* Przeciąganie 3 palcami w górę i w dół zmienia promień pędzla
* Interfejs możesz pomniejszyć, by zmieścić więcej przycisków, jeśli masz dobry wzrok, albo powiększyć, jeśli gorzej widzisz!
* Szersze menu mogą czasem zasłaniać rzeźbę; możesz ustawić je jako przezroczyste i bez rozmycia, by widzieć rzeźbę pod menu.
* Jeśli rzeźbisz palcem, użyj opcji [`Przesunięcie pociągnięć`](stroke.md#stroke-offset), aby odsunąć środek pędzla nieco od palca.
* Te i wiele innych opcji znajdziesz w [menu Interfejs](./interface.md). 


## Deformator napełniania lub wypiętrzania {#inflate-or-peak-deformer}

Wiele aplikacji 3d ma deformator napełniania, który przesuwa wszystkie wierzchołki wzdłuż ich normalnych o zadaną wartość. Nomad nie ma obecnie deformatorów, ale takie działanie można uzyskać pędzlem Napełnij:

* Wybierz pędzel Napełnij
* W [menu Pociągnięcie](./stroke.md#stroke) zmień typ pociągnięcia na `Blokada + promień`
* Ustaw promień pędzla większy niż rzeźba; w razie potrzeby oddal kamerę od rzeźby.
* Kliknij i przeciągnij pociągnięcie po powierzchni obiektu; gdy promień jest większy niż obiekt, cały kształt zostanie równomiernie napełniony o stałą wartość.
* Intensywnością pędzla regulujesz stopień napełnienia
* W razie potrzeby użyj maskowania, by ochronić niektóre obszary albo osłabić w nich efekt napełniania.

## Usuwanie grudek i „pryszczy” po remeshu wokselowym {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Remesh wokselowy świetnie tworzy równomiernie rozłożone wielokąty, ale czasem powstaje topologia, która przy wygładzaniu daje drobne grudki lub „pryszcze”. Na przykład:

* Użyj pędzla Bruzda na domyślnej kuli i narysuj spiralę
* Wykonaj remesh wokselowy z opcją `Utwórz wielokrotną rozdzielczość` ustawioną na 3
* Wygładź z dużą intensywnością
* pojawiają się artefakty (łatwiej je zobaczyć z kontrastowym materiałem matcap):

![](/videos/tip_pimples_before.mp4)

Aby naprawić to rzeźbieniem, wypróbuj opcję `Stabilne wygładzanie` w ustawieniach wygładzania. Radzi sobie ona z nierównym układem topologii po remeshu wokselowym i daje czyste efekty.

![](/videos/tip_pimples_stable_smooth.mp4)

Aby naprawić samą topologię, użyj nowego prymitywu, narzędzi do przebudowy na czworokąty albo zewnętrznego programu do modelowania 3d, a następnie zrzutuj detale z oryginalnej siatki na nową przez `Topologia -> Zastosuj -> Rzutowanie → Wierzchołek`. 

![](/videos/tip_pimples_reproject.mp4)

## Oświetlenie dzienne {#daylight-lighting}

Domyślny render PBR jest, jak wskazuje nazwa, oparty na fizyce, więc podobnie jak nieobrobione zdjęcie cyfrowe może wyglądać nieco blado i płasko. Światła i postprocessing w Nomad pozwalają nadać renderom więcej życia.

Oto domyślny render – zobaczmy, czy uda się go poprawić:
![](/images/tips_lighting_default.webp)

Włączenie postprocessingu i mapowania odcienia może dodać jasności i kontrastu:

![](/images/tips_lighting_tonemap.webp)

Przejdźmy do świateł: domyślne światło środowiska dobrze sprawdza się przy rzeźbieniu, ale do końcowego renderu można je poprawić. Warto rozdzielić światło bezpośrednie (np. słońce) od światła otoczenia (np. światła z błękitu nieba czy od ziemi). Zmniejszenie i obrócenie światła środowiska zaczyna oddawać, jak wyglądałoby oświetlenie, gdyby obiekt znajdował się w cieniu:

![](/images/tips_lighting_env.webp)

Można dodać światło bezpośrednie i zwiększyć jego intensywność, by zasymulować ostre słońce. Zrównoważenie go ze światłem środowiska daje przyjemny efekt:

![](/images/tips_lighting_sunlight.webp)

Postaciom często służy zmiana materiału na podpowierzchniowy i umieszczenie za postacią światła stożkowego skierowanego na uszy, by zaczęły prześwitywać:

![](/images/tips_lighting_sss.webp)

Potem poeksperymentuj z resztą ustawień postprocessingu! Globalne oświetlenie i okluzja otoczenia pomagają uzyskać bardziej realistyczne światło. Krzywizna i wyostrzenie wydobywają więcej detali rzeźby. Aberracja chromatyczna, głębia pola, ziarno, rozświetlenie i winieta symulują efekty aparatu. Pamiętaj, że po włączeniu kolejnych funkcji trzeba dostosować oświetlenie i inne wartości postprocessingu, by to skompensować.

Oto render z pełnym zestawem poprawek postprocessingu:
![](/images/tips_lighting_final.webp)
