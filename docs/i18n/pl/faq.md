# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Platforma {#platform}
### Gdzie na urządzeniu znajdują się moje projekty? {#locate}
Projekty znajdują się w folderze `projects` w głównym folderze Nomad.

Na iOS do folderu Nomad masz dostęp przez aplikację Pliki.

Na Androidzie folder Nomad znajduje się w `Android/data/com.stephaneginier.nomad/files/`.  
W nowszych wersjach Androida (10/11) nie masz już dostępu do folderu `Android/data`.
Możesz dostać się do niego przez osobną aplikację, na przykład [tę](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Czy mogę testować wersje beta? {#beta}
Dla Windows i MacOS wersja beta może być dostępna na [stronie głównej](https://nomadsculpt.com).
<br>
Dla iOS jest prywatny TestFlight – zajrzyj na kanał #beta-ios na [Discordzie](https://discord.com/invite/8h7BwpRz29).
<br>
[Wersja demonstracyjna w przeglądarce](https://nomadsculpt.com/demo) jest zwykle aktualizowana o najnowsze funkcje.

### Dlaczego na Androidzie jest darmowa wersja próbna, a na iOS nie? {#android-trial}
Bo stare urządzenia z Androidem są kiepskie (niektóre nowe zresztą też...), a nie chciałem, żeby ktoś kupił aplikację i zobaczył czarny ekran.
Główny powód jest jednak taki, że płatne aplikacje na Androida nie są tam raczej normą.

### Jaki tablet najlepiej nadaje się do Nomad? {#best-tablet}

W skrócie: iPad.

Nieco dłuższa odpowiedź brzmi: 

> „Najnowszy iPad, _na jaki Cię stać_. Chyba że naprawdę nie znosisz Apple – wtedy najnowszy tablet Samsunga, na jaki Cię stać. Cokolwiek innego najpierw przetestuj.” 

Ludzie zawsze chcą więcej szczegółów, więc oto podsumowanie.

Nomad działa najlepiej na nowszych iPadach:

* iPady i iPhone'y mają dostęp do wtyczki [Quad Remesher](tools#quad-remesher) od [Exoside](https://exoside.com/)
* nowe iPady z najnowszym rysikiem obsługują [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), czyli obracanie rysika wokół własnej osi w niektórych narzędziach Nomad. 
* najnowsze układy z serii M są bardzo wydajne. 

Najnowszy i najdroższy dostępny iPad bardzo szybko wyrenderuje końcowe obrazy i pozwoli wyrzeźbić mnóstwo detali.

Spadek wydajności na tańszych i starszych iPadach nie jest jednak tak duży, jak się wydaje. Każdy iPad obsługujący Apple Pencil całkiem dobrze radzi sobie z Nomad. Na przykład:

* iPad Pro z 2023 roku obsłuży rzeźby z 5 milionami wielokątów bez utraty płynności, a obraz w jakości końcowej wyrenderuje w 5 sekund.
* iPad Pro z 2015 roku obsłuży obiekt z 1,2 miliona wielokątów z lekkim opóźnieniem, a obraz w jakości końcowej wyrenderuje w 20 sekund.

To duża różnica w wydajności, ale trzeba też wziąć pod uwagę cenę:

* Nowy iPad Pro z 2025 roku ze wszystkimi opcjami kosztuje *2500 USD*. 
* iPad Pro z 2023 roku kosztuje obecnie *400 USD* na eBayu.
* iPad Pro z 2015 roku kosztuje *250 USD* na eBayu.

Czy dodatkowe 4 miliony wielokątów i 15 zaoszczędzonych sekund są warte 2100 USD? To już Twoja decyzja.

Modele inne niż Pro mogą być jeszcze tańsze i oferują szeroki wybór rozmiarów i wydajności. Obecny iPad Air obsługuje rysik drugiej generacji z barrel roll i jest znacznie tańszy niż Pro. Rynek używanych i odnowionych urządzeń daje jeszcze więcej możliwości. 

Oznacza to, że niezależnie od budżetu powinieneś znaleźć iPada dla siebie. I pamiętaj, że większość rzeźb nie ma milionów wielokątów! Jeśli zmieścisz się poniżej 500 000 wielokątów, nawet stare iPady pozwolą Ci szybko rzeźbić.

`A co z Androidem?`

Wydajność graficzna Androida jest niższa niż iPadów. Według twórcy Nomad „Samsung Galaxy Tab S9 uruchamia Nomad o rząd wielkości wolniej niż iPad Air”. Mimo to wielu użytkowników jest bardzo zadowolonych ze swoich tabletów Samsunga – Nomad dobrze sprawdza się w większości prac rzeźbiarskich. 

Przy innych tabletach z Androidem zachowaj ostrożność. Wydajność sprzętu z Androidem bywa bardzo różna i trudno przewidzieć, jak będzie działał Nomad.

Najpierw przetestuj darmową wersję Nomad z wyłączonym zapisywaniem. 

`A co z pamięcią i miejscem na dane?`

Większość plików Nomad ma 100 MB lub mniej. Oznacza to, że niemal każdy kupiony dziś tablet, iPad czy z Androidem, ma mnóstwo miejsca na Twoje projekty Nomad.


### Kupiłem Nomad na jedno urządzenie. Czy mogę używać go na innym? {#multi-devices}
Tak, o ile korzysta ono z tego samego sklepu z aplikacjami i tego samego konta.

Jeśli na przykład kupiłeś aplikację w App Store na iOS, możesz używać jej na innych urządzeniach z iOS.

Jeśli kupiłeś ją na tablet z Androidem w Google Play, możesz używać jej na innych urządzeniach z Androidem.

Jeśli jednak kupiłeś Nomad na Androida, a potem kupisz iPada, musisz kupić aplikację ponownie.

Wynika to z tego, że Nomad nie ma własnego serwera licencji ani modelu subskrypcji. Nie ma też porozumienia między Apple, Google i AppGallery, które pozwalałoby współdzielić licencje. 


### Jak przywrócić zakup? {#restore}
Google Play i AppGallery same automatycznie synchronizują zakupy.

- Wejdź do menu Informacje (ikona Nomad w lewym górnym rogu) i naciśnij `Przywróć zakup`
- Sprawdź, czy jesteś zalogowany na to samo konto, którego użyłeś do zakupu Nomad (w Google Play).
- Uruchom ponownie urządzenie
- Czasem trzeba odczekać kilka godzin
- Upewnij się, że aplikacja Google Play jest aktualna
- Zainstaluj ponownie Nomad (najpierw [zrób kopię zapasową plików](#locate), jeśli nie chcesz niczego stracić)
- Możesz spróbować kupić aplikację ponownie i zobaczyć, co się stanie (uwaga: na tym samym koncie nie da się kupić tego samego produktu dwa razy)

:::tip
Możesz napisać do mnie na <support@nomadsculpt.com>, ale *jedyne*, co mogę zrobić, to potwierdzić, czy z danym adresem e-mail powiązany jest zakup.

Regularnie dostaję zgłoszenia o licencjach, które nie zaktualizowały się poprawnie po zmianie urządzenia na nowe.
Nie mam żadnego wpływu na płatności ani synchronizację kont – wszystkim zajmuje się Google/AppGallery!

W końcu zakup zawsze zostaje przywrócony, ale nie wiadomo, co pozwala przyspieszyć ten proces.
:::

::: warning
Nowsze urządzenia Huawei nie mają dostępu do usług Google.
W takim przypadku musisz kupić aplikację ponownie w AppGallery (sklepie z aplikacjami Huawei).
:::

### Czy możesz przetłumaczyć [mój-język] albo poprawić tłumaczenie? {#locale}
Dodanie nowego języka jest dla mnie stosunkowo proste, ale korzystam z tłumaczenia AI, bo dużo łatwiej obsłużyć nim regularne aktualizacje.
Pliki tłumaczeń znajdziesz [tutaj](https://github.com/stephomi/nomad-translation).

## Funkcje {#features}

### Dlaczego gizmo się nie przesuwa? {#gizmo-not-moving}
Być może masz włączone [przypinanie na lewym pasku narzędzi menu](tools#left-menu-toolbar). 

### Czy w Nomad można animować? {#animate}
Na razie nie. Oś czasu, która pozwalałaby animować warstwy, mogłaby być ciekawa, ale w tej chwili nie jest planowana.  

Chciałbym w przyszłości obsługiwać rigging/skinning, ale wiąże się to z kilkoma wyzwaniami (zwłaszcza z interakcją z narzędziami do rzeźbienia...), więc na razie nic nie jest pewne.


### Czy można porządnie modelować low poly? {#lowpoly}
Na razie nie.
Nie jest to właściwie zakres Nomad *Sculpt*, ale może w przyszłości dodam kilka narzędzi.


### Czy można tworzyć UV i teksturować? {#texturing}
Krótka odpowiedź: tak. Dłuższa odpowiedź: nie bezpośrednio, ale jest kilka sposobów, by połączyć świetne narzędzia Nomad do malowania wierzchołków z UV i teksturami.

* Nomad pozwala malować kolor, chropowatość i właściwości materiału bezpośrednio w wierzchołkach rzeźby.
* Nomad obsługuje bardzo duże liczby wierzchołków, więc możesz malować, nie martwiąc się o UV.
* Nomad może wczytywać tekstury do pędzli, co pozwala odciskać i malować teksturami.
* Nomad może wczytywać obiekty z przypisanymi już teksturami, na potrzeby renderowania.
* Nomad potrafi [rozwinąć UV](topology.md#uv-unwrap-uvatlas) obiektów o mniejszej liczbie wielokątów.
* Kolor, chropowatość i metaliczność można przenieść z tekstur na wierzchołki za pomocą [opcji rzutowania](topology.md#reproject-to-vertex).
* Kolor, chropowatość, metaliczność i normalne można wypalić z wierzchołków do tekstur za pomocą [opcji wypalania](topology.md#bake-texture)
* Wypalanie i rzutowanie działa między pojedynczymi obiektami lub wieloma obiektami albo między najwyższym a najniższym poziomem podziału jednego obiektu, co pozwala na różne sposoby pracy.
* Po wypaleniu eksport do OBJ zapisze też tekstury, które możesz przenieść do aplikacji takiej jak Procreate i malować bezpośrednio po nich.

### Czy mogę nagrać film z obracającym się modelem? {#video}
Na razie nie jest to planowane, ale iOS ma bardzo łatwą w użyciu [funkcję nagrywania ekranu](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados).

Na iOS przesuń palcem w dół od lewego górnego rogu i stuknij przycisk nagrywania. Pojawi się 3-sekundowe odliczanie – odsuń menu, by odsłonić Nomad, i użyj funkcji obrotu modelu (turntable). Na koniec ponownie przesuń palcem w dół od prawego górnego rogu i jeszcze raz stuknij przycisk nagrywania. W bibliotece zdjęć przytnij film, usuwając zbędne fragmenty na początku i na końcu.

### Czy możesz dodać [ulubioną-funkcję] jako przycisk na głównym ekranie? {#interface}
Tak, dolny pasek narzędzi można teraz dostosować w menu [Interfejs](interface.md#shortcuts), a także tworzyć pływające paski narzędzi.

### Jakie będą kolejne funkcje? {#next-features}
Mam mnóstwo pomysłów na średnio- i długoterminowy plan rozwoju, ale jeszcze nie wiem.  

Poprawki błędów i ulepszanie istniejących funkcji zawsze będą miały pierwszeństwo przed dodawaniem nowych.


### Czy w Nomad można riggować? {#rigging}
Nie, ale jest to planowane. Na razie możesz łączyć kształty w hierarchię i zmieniać punkty obrotu, co pozwala tworzyć proste rzeźby do pozowania.

### Czy można używać więcej niż 4 świateł? {#lights}
Możesz używać do 4 świateł na urządzeniach mobilnych i do 6 na komputerze. To ograniczenie silnika renderowania w czasie rzeczywistym w Nomad. Można to obejść za pomocą obiektów emisyjnych i globalnego oświetlenia w postprocessingu, jak pokazano w [tym poradniku](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Czy można importować narzędzia z Zbrush? {#zbrush-import}
Nie, Zbrush używa zastrzeżonego formatu. Powinieneś jednak móc wyodrębnić mapy alfa i używać ich w Nomad. 

### Dlaczego kolory nie zgadzają się z tym, co pomalowałem? Dlaczego w renderze nie mogę uzyskać bieli? {#paint-pbr}
Wyobraź sobie zdjęcie kartki papieru, zdjęcie lampki biurowej i zdjęcie słońca. Starsze aparaty i ekrany pokażą je wszystkie po prostu jako „białe”. Nowocześniejsze systemy potrafią pokazać różnicę między bielą odbitą od papieru, światłem emitowanym przez lampkę i oślepiającą jasnością słońca.

Współczesna grafika komputerowa stara się działać podobnie, naśladując fizykę światła i powierzchni. Nazywa się to `Physically Based Rendering`, czyli PBR, i na tym opiera się renderer PBR w Nomad. Wygląda to realistycznie i harmonijnie, ale jasno pomalowane kolory często wydają się ciemniejsze.

Jeśli chcesz, żeby render był bliższy pomalowanym kolorom, możesz to poprawić zarówno metodami nieopartymi na fizyce, jak i opartymi na niej:

Bez PBR:
* `Użyj trybu Nieoświetlony w menu Cieniowanie`. Kolory będą wyświetlane dokładnie tak, jak je pomalowano, ale tracisz całe cieniowanie. Przydaje się do szybkiego sprawdzenia i do bardziej graficznych efektów.
* `Użyj trybu MatCap w menu Cieniowanie`. Wybierz jaśniejszy matcap, w większości biały, bez kolorowego zabarwienia.

PBR:
* `Użyj neutralnego środowiska`. Możesz [zmienić środowisko](shading.md#environment) na bardziej neutralne. Unikaj środowisk wnętrz, bo zwykle mają mocniejsze zabarwienie. Wybierz raczej plener w świetle dziennym albo studio.
* `Wzmocnij oświetlenie`. Gdybyś fotografował białą kartkę w ciemnym pokoju, po prostu dodałbyś światła. Przy świetle środowiska zwiększaj suwak ekspozycji, aż kolory zaczną Ci odpowiadać, albo dodaj więcej pojedynczych świateł o większej intensywności.
* `Zwiększ ekspozycję kamery`. Gdyby w ciemnym pokoju nie było dodatkowych świateł, mógłbyś dłużej otworzyć migawkę aparatu albo użyć wyższej czułości ISO. W Nomad podobny efekt uzyskasz za pomocą postprocessingu. Przejdź do menu Postprocessing, włącz go, zjedź do mapowania odcienia, włącz je i zwiększaj suwak ekspozycji, aż kolory będą wyglądać dobrze.
* `Użyj koloru emisyjnego`. W menu Materiał możesz włączyć „Emisyjne” w sekcji tekstur, dzięki czemu obiekt będzie wyglądał jak źródło światła. Jeśli włączysz globalne oświetlenie w ustawieniach postprocessingu, będzie on oświetlał inne obiekty w scenie. Możesz też włączyć dla tego materiału opcję „Zawsze nieoświetlone”, co da podobny wygląd bez tekstury.

## Awarie {#crashes}

### Aplikacja się zawiesza, gdy zapisuję model lub robię remesh! {#crash-remesh}
Na urządzeniu kończy się pamięć (RAM).  
Aby zmniejszyć zużycie pamięci przez scenę, możesz użyć niektórych opcji z menu [Topologia](topology.md), by zmniejszyć liczbę wielokątów.

::: tip RAM/pamięć masowa
Liczy się ilość pamięci RAM, a nie pamięci masowej (która zwykle jest dużo większa).
:::


### Aplikacja się zawiesza, gdy wczytuję projekt! {#crash-load}
Jeśli plik jest mały, możesz mi go wysłać, a ja się mu przyjrzę (e-mailem na <support@nomadsculpt.com>).

W przeciwnym razie na urządzeniu prawdopodobnie kończy się pamięć RAM.

- Zamknij wszystkie inne otwarte aplikacje na urządzeniu.
- Rozpocznij w Nomad nowy projekt, zamiast mieć otwarty bieżący projekt.
- Jeśli aplikacja nadal się zawiesza, jedynym rozwiązaniem jest wczytanie [pliku projektu](#locate) na urządzeniu z większą ilością pamięci.

::: tip
Jeśli Twoje urządzenie mobilne nie może wczytać projektu, wypróbuj [wersję na komputer](https://nomadsculpt.com). W trybie Demo możesz jej używać za darmo do importu i eksportu projektów, choć dostępnych jest tylko kilka narzędzi do edycji.

Jeśli projekt używa [Warstw](layers.md), możesz je scalić, by zmniejszyć zużycie pamięci.
:::

### Aplikacja się zawiesza przy uruchamianiu Nomad! {#crash-start}
Jeśli aplikacja zawiesza się przy wczytywaniu, oznacza to, że Nomad ma problem z którymś plikiem w folderze Nomad.

Najczęściej dzieje się tak dlatego, że projekt jest ciężki i niestety przekracza limit pamięci RAM.

Znajdź [folder Nomad](#locate), a następnie zmieniaj nazwy niektórych plików lub je przenoś, aby znaleźć winowajcę.

Najpierw spróbuj zmienić nazwę pliku `settings.json`. Dzięki temu Nomad przestanie wczytywać ostatni projekt.

Jeśli to nie pomoże, spróbuj przenieść niektóre ostatnio dodane pliki poza ich foldery zasobów (`projects`, `matcaps`, `environments` itd.).

Możesz też zmienić nazwy samych folderów, by Nomad całkowicie je pominął.
Jeśli zmienisz nazwy lub przeniesiesz wszystkie pliki w folderze Nomad, efekt będzie taki sam jak po czystej instalacji.

::: tip
Gdy Nomad wczytuje plik przy uruchamianiu, zawsze przenosi go do folderu `can_be_deleted/`.
Jeśli operacja się powiedzie, plik wraca do swojego oryginalnego folderu.

Jeśli aplikacja zawiesi się przed zakończeniem wczytywania, Nomad przy następnym uruchomieniu wystartuje poprawnie, ponieważ pomija folder `can_be_deleted/`.

Możesz po prostu spróbować wczytać ten plik ponownie, jeśli uważasz, że tym razem się uda.
:::
