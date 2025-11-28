# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Platforma {#platform}
### Gdzie znajdują się moje projekty na urządzeniu? {#locate}
Projekty znajdują się w folderze `projects` wewnątrz głównego folderu Nomad.

W systemie iOS możesz uzyskać dostęp do folderu Nomad za pomocą aplikacji Pliki.

W systemie Android folder Nomad znajduje się w `Android/data/com.stephaneginier.nomad/files/`.  
W nowszych wersjach Androida (10/11) nie masz już dostępu do folderu `Android/data`.
Możesz uzyskać do niego dostęp za pomocą osobnej aplikacji, na przykład [tej](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Czy jest możliwość testowania wersji beta? {#beta}
Dla Windows i MacOS wersja beta może być dostępna na [stronie głównej](https://nomadsculpt.com).
<br>
Dla iOS istnieje prywatny TestFlight, odwiedź [Discord](https://discord.com/invite/8h7BwpRz29) na kanale #beta-ios.
<br>
[Demo webowe](https://nomadsculpt.com/demo) jest zazwyczaj aktualizowane o najnowsze funkcje.

### Dlaczego na Androidzie jest darmowy okres próbny, a na iOS nie? {#android-trial}
Ponieważ stare urządzenia z Androidem są kiepskie (a niektóre nowsze też...), i nie chciałem, żeby ludzie kupowali aplikację i witał ich czarny ekran.
Ale główny powód jest taki, że mam wrażenie, iż płatne aplikacje na Androidzie nie są tak naprawdę normą.

### Jaki tablet jest najlepszy do pracy z Nomad? {#best-tablet}

TL;DR: iPad.

Trochę dłuższa odpowiedź to 

> „Naj nowszy iPad, na który _cię stać_, chyba że naprawdę nie znosisz Apple, wtedy najnowszy tablet Samsunga, na który cię stać. Wszystko inne – najpierw przetestuj.” 

Ludzie zawsze chcą więcej informacji, więc oto podsumowanie.

Nomad działa najlepiej na nowszych iPadach:

* iPady i iPhone’y mogą korzystać z wtyczki [Quad Remesher](tools#quad-remesher) od [Exoside](https://exoside.com/)
* nowsze iPady z najnowszym rysikiem obsługują [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), możesz obracać rysik w niektórych narzędziach w Nomadzie. 
* wydajność najnowszych układów z serii M jest bardzo wysoka. 

Najnowszy, najdroższy dostępny iPad pozwoli bardzo szybko renderować finalne obrazy i rzeźbić z ogromną ilością detali.

Jednak spadek wydajności w tańszych i starszych iPadach nie jest tak duży, jak się ludziom wydaje. Każdy iPad obsługujący Apple Pencil uruchamia Nomad całkiem dobrze. Na przykład:

* iPad Pro z 2023 roku może obsłużyć rzeźby o 5 milionach polygonów i pozostaje responsywny, finalny obraz w wysokiej jakości może się renderować 5 sekund.
* iPad Pro z 2015 roku może obsłużyć obiekt o 1,2 miliona polygonów z lekkimi przycięciami, finalny obraz w wysokiej jakości może się renderować 20 sekund.

To duża różnica w wydajności, ale trzeba też wziąć pod uwagę cenę:

* iPad Pro z 2025 roku kosztuje *2500 USD* jako nowy, w pełnej konfiguracji. 
* iPad Pro z 2023 roku kosztuje obecnie około *400 USD* na eBay.
* iPad Pro z 2015 roku kosztuje około *250 USD* na eBay.

Czy dodatkowe 4 miliony polygonów i oszczędność 15 sekund są warte 2100 dolarów? To już zależy od ciebie.

Modele nie-Pro mogą być jeszcze tańsze i oferują szeroki wybór rozmiarów i wydajności. Obecny iPad Air obsługuje rysik 2. generacji z barrel rollem i jest znacząco tańszy niż Pro. Rynek urządzeń używanych i odnowionych daje jeszcze więcej opcji. 

Oznacza to, że niezależnie od budżetu powinieneś być w stanie znaleźć iPada dla siebie. I pamiętaj, że większość rzeźb nie ma milionów polygonów! Jeśli utrzymasz się poniżej 500 000 polygonów, nawet stare iPady pozwolą ci rzeźbić szybko.

`A co z Androidem?`

Wydajność grafiki na Androidzie jest niższa niż na iPadach. Według dewelopera Nomad „Samsung Galaxy Tab S9 uruchomi Nomad rząd wielkości wolniej niż iPad Air”. Mimo to wielu użytkowników jest bardzo zadowolonych ze swoich tabletów Samsunga, Nomad działa wystarczająco dobrze do większości rzeźbienia. 

W przypadku innych tabletów z Androidem zachowaj ostrożność. Sprzęt z Androidem może się bardzo różnić wydajnością, trudno przewidzieć, jak Nomad będzie działał.

Najpierw skorzystaj z darmowej wersji Nomad bez zapisu, aby przetestować urządzenie. 

`A co z pamięcią i miejscem na dane?`

Większość plików Nomad ma zwykle 100 MB lub mniej. Oznacza to, że praktycznie każdy tablet kupiony obecnie, iPad lub Android, będzie miał wystarczająco dużo miejsca na twoje projekty Nomad.


### Kupiłem Nomad na jedno urządzenie, czy mogę używać go na innym? {#multi-devices}
Tak, o ile korzystasz z tego samego sklepu z aplikacjami i tego samego konta.

Na przykład jeśli kupiłeś aplikację w sklepie App Store na iOS, możesz używać jej na innych urządzeniach z iOS.

Jeśli kupiłeś ją na tablet z Androidem w Google Play, możesz używać jej na innych urządzeniach z Androidem.

Jeśli jednak kupiłeś Nomad na Androidzie, a potem kupisz iPada, będziesz musiał kupić aplikację ponownie.

Dzieje się tak dlatego, że Nomad nie ma własnego serwera licencji ani modelu subskrypcji. Nie ma też porozumienia między Apple/Google/AppGallery w sprawie współdzielenia licencji. 


### Jak przywrócić mój zakup? {#restore}
Google Play i AppGallery obsługują synchronizację automatycznie.

- Wejdź w menu About (ikona Nomad w lewym górnym rogu) i naciśnij `restore purchase`
- Upewnij się, że jesteś zalogowany na to samo konto, którego użyłeś do zakupu Nomad (w Google Play).
- Uruchom ponownie urządzenie
- Czasami trzeba poczekać kilka godzin
- Upewnij się, że aplikacja Google Play jest zaktualizowana
- Zainstaluj ponownie Nomad (upewnij się, że [zrobiłeś kopię zapasową plików](#where-are-my-projects-located-on-my-device), jeśli nie chcesz nic stracić)
- Możesz spróbować kupić aplikację ponownie, aby zobaczyć, co się stanie (uwaga: nie możesz kupić dwa razy tego samego elementu na tym samym koncie)

:::tip
Możesz skontaktować się ze mną pod adresem <support@nomadsculpt.com>, ale *jedyną* rzeczą, jaką będę mógł zrobić, jest potwierdzenie, czy z danym adresem e-mail jest powiązany zakup.

Zwróć uwagę, że regularnie otrzymuję zgłoszenia dotyczące licencji, które nie aktualizują się poprawnie po zakupie nowego urządzenia.
Nie mam żadnej kontroli nad płatnościami i synchronizacją kont, wszystkim zajmują się Google/AppGallery!

Ostatecznie zakup zawsze zostaje przywrócony, ale nie jest jasne, jakie dokładnie kroki przyspieszają ten proces.
:::

::: warning
Nowsze urządzenia Huawei nie mają dostępu do usług Google.
W takim przypadku musisz kupić aplikację ponownie w AppGallery (sklep z aplikacjami Huawei).
:::

### Czy możecie przetłumaczyć lub poprawić [mój-język]? {#locale}
Stosunkowo łatwo mogę dodać kolejny język, ale polegam na tłumaczeniu AI, ponieważ znacznie łatwiej jest wtedy obsługiwać regularne aktualizacje.
Pliki tłumaczeń można znaleźć [tutaj](https://github.com/stephomi/nomad-translation).

## Funkcje {#features}

### Dlaczego gizmo się nie porusza? {#gizmo-not-moving}
Możliwe, że masz [włączony pin w lewym pasku narzędzi](tools#left-menu-toolbar). 

### Czy można animować w Nomad? {#animate}
Na razie nie. Funkcja osi czasu, która mogłaby animować warstwy, byłaby ciekawa, ale obecnie nie jest planowana.  

Chciałbym w przyszłości obsługiwać rigging/skinning, ale wiąże się to z kilkoma wyzwaniami (w szczególności interakcją z narzędziami do rzeźbienia...), więc na razie nic nie jest pewne.

### Czy można robić poprawne modelowanie low-poly? {#lowpoly}
Na razie nie.  
To nie jest tak naprawdę zakres Nomad *Sculpt*, ale możliwe, że w przyszłości dodam kilka narzędzi.

### Czy można robić UV i teksturowanie? {#texturing}
Krótka odpowiedź: Tak. Dłuższa odpowiedź: Nie bezpośrednio, ale istnieje kilka sposobów na połączenie znakomitych narzędzi malowania wierzchołków Nomada z UV i teksturami.

* Nomad pozwala malować kolor, szorstkość (roughness), właściwości materiału bezpośrednio w wierzchołkach rzeźby.
* Nomad pozwala na bardzo wysoką liczbę wierzchołków, dzięki czemu możesz malować bez martwienia się o UV.
* Nomad może wczytywać tekstury do użycia w pędzlach, co pozwala na stemplowanie i malowanie teksturami.
* Nomad może wczytywać obiekty z wcześniej przypisanymi teksturami, do celów renderingu.
* Nomad potrafi [rozwinąć UV](topology.md#uv-unwrap) obiekty o niższej liczbie polygonów.
* Kolor/szorstkość/metaliczność mogą być przenoszone z tekstur do wierzchołków za pomocą [opcji projekcji](topology.md#reproject-to-vertex).
* Kolor/szorstkość/metaliczność/normalne mogą być wypiekane z wierzchołków do tekstur za pomocą [opcji wypiekania](topology.md#bake-to-texture)
* Wypiekanie i projekcja mogą być wykonywane pomiędzy pojedynczymi obiektami lub wieloma obiektami, albo pomiędzy najwyższym i najniższym poziomem podziału jednego obiektu, co pozwala na różnorodne workflow wypiekania i projekcji.
* Po wypieczeniu, eksport pliku OBJ wyeksportuje również tekstury, które można przenieść do aplikacji takiej jak Procreate, aby malować bezpośrednio na teksturach.

### Czy mogę nagrać wideo obrotu (turntable)? {#video}
Na razie nieplanowane, iOS ma [funkcję nagrywania wideo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados), która jest bardzo łatwa w użyciu.

W iOS robi się to przez przeciągnięcie palcem w dół z lewego górnego rogu i stuknięcie przycisku nagrywania. Pojawi się 3‑sekundowe odliczanie, przesuń menu, aby odsłonić Nomad i użyj funkcji turntable. Po zakończeniu ponownie przesuń palcem w dół z prawego górnego rogu i stuknij przycisk nagrywania. Edytuj film w bibliotece zdjęć, aby usunąć zbędne fragmenty na początku i końcu nagrania.

### Czy możecie dodać [moją-ulubioną-funkcję] jako przycisk najwyższego poziomu? {#interface}
Tak, dolny pasek narzędzi można teraz dostosować z menu [interface](interface.md), a także można tworzyć pływające paski narzędzi.

### Jakie będą następne funkcje? {#next-features}
W średnio/długoterminowej mapie drogowej mam wiele pomysłów, ale jeszcze nie wiem.  

Poprawki błędów i ulepszanie istniejących funkcji zawsze będą miały wyższy priorytet niż dodawanie nowych.

### Czy można riggować w Nomad? {#rigging}
Nie, ale jest to planowane. Na razie możesz łączyć obiekty relacją rodzic‑potomek i zmieniać punkty obrotu (pivot), co pozwala na proste pozowalne rzeźby.

### Czy można używać więcej niż 4 świateł? {#lights}
Nie, to ograniczenie silnika renderującego w czasie rzeczywistym w Nomadzie. Można to obejść, używając obiektów emisyjnych i globalnego oświetlenia w postprocessingu, jak pokazano w [tym poradniku](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Czy można importować narzędzia ZBrush (ZTools)? {#zbrush-import}
Nie, ZBrush używa zastrzeżonego formatu. Powinieneś jednak móc wyodrębnić mapy alfa i używać ich w Nomadzie. 

### Dlaczego kolory nie zgadzają się z tym, co namalowałem? Dlaczego nie mogę uzyskać bieli w renderze? {#paint-pbr}
Wyobraź sobie zrobienie zdjęcia kartki papieru, lampki biurkowej i słońca. Starsze aparaty i ekrany po prostu pokażą je wszystkie jako „białe”. Nowsze systemy potrafią pokazać różnicę między odbitym białym papieru, emitowanym światłem lampki i super jasnym światłem słońca.

Współczesna grafika komputerowa próbuje działać w podobny sposób, emulując fizykę światła i powierzchni. Nazywa się to `Physically Based Rendering` lub PBR, i na tym oparty jest renderer PBR Nomada. Wygląda to realistycznie i zrównoważenie, ale często jaskrawo namalowane kolory wydają się ciemniejsze.

Jeśli potrzebujesz, aby render bardziej odpowiadał namalowanym kolorom, możesz to poprawić zarówno w sposób fizycznie poprawny, jak i niefizyczny:

Non PBR:
* `Use the 'Unlit' mode in the lighting menu`. Kolory będą wyświetlane dokładnie tak, jak zostały namalowane, ale tracisz całe cieniowanie. Przydatne do szybkich sprawdzeń i bardziej graficznego wyglądu.
* `Use the 'Matcap' mode in the lighting menu`. Wybierz jaśniejszy matcap, który jest głównie biały, bez zabarwienia kolorem.

PBR:
* `Use a neutral environment`. Możesz [zmienić środowisko](shading.md#environment) na bardziej neutralne. Unikaj środowisk wewnętrznych, ponieważ zwykle są bardziej zabarwione kolorem. Zamiast tego wybieraj dzienne środowiska zewnętrzne lub studyjne.
* `Boost the lighting`. Gdybyś robił zdjęcie białej kartki w ciemnym pokoju, po prostu dodałbyś więcej światła. Przy oświetleniu środowiskowym podnieś suwak ekspozycji, aż kolory zaczną wyglądać dla ciebie właściwie, lub dodaj więcej pojedynczych świateł o większej intensywności.
* `Boost the camera exposure`. Jeśli w ciemnym pokoju nie byłoby dodatkowych świateł, mógłbyś wydłużyć czas otwarcia migawki lub użyć wyższej czułości ISO. W Nomadzie podobny efekt uzyskasz w postprocessingu. Przejdź do postprocess, włącz, przejdź do tone mapping, włącz i podnieś suwak ekspozycji, aż kolory będą wyglądały odpowiednio.
* `Use emissive color`. W menu materiału możesz włączyć „emissive” w sekcji tekstur, co sprawi, że obiekt będzie wyglądał jak źródło światła. Jeśli w ustawieniach postprocess włączysz global illumination, będzie on rzucał światło na inne obiekty w scenie. Możesz też włączyć „unlit” dla tego materiału, co da podobny efekt bez tekstury.

## Awaryjne zamknięcia {#crashes}

### Aplikacja zamyka się, gdy zapisuję lub remeshuję mój model! {#crash-remesh}
Twoje urządzenie kończy pamięć (RAM).  
Aby zmniejszyć użycie pamięci w scenie, możesz użyć niektórych opcji [Topology](topology.md), aby zredukować liczbę polygonów.

::: tip RAM/Storage
Liczy się ilość pamięci RAM, a nie pamięci masowej (która zwykle jest dużo większa).
:::

### Aplikacja zamyka się, gdy ładuję mój projekt! {#crash-load}
Jeśli plik jest mały, możesz wysłać go do mnie, a ja na niego zerknę (mailem na <support@nomadsculpt.com>).

W przeciwnym razie urządzenie prawdopodobnie kończy pamięć RAM.

- Upewnij się, że zamknąłeś wszystkie inne otwarte aplikacje na urządzeniu.
- Zamiast mieć aktualnie otwarty projekt, rozpocznij nowy projekt w Nomadzie.
- Jeśli nadal crashuje, jedynym rozwiązaniem jest wczytanie [twojego pliku projektu](#where-are-my-projects-located-on-my-device) na urządzeniu z większą ilością pamięci.

::: tip
W przeglądarce desktopowej możesz spróbować wczytać swój plik [pod tym adresem](https://nomadsculpt.com/demo_save/), a następnie wyeksportować go z powrotem po uproszczeniu sceny.

Niektóre przeglądarki ograniczają ilość RAM, jaką może zająć pojedyncza karta, więc możliwe, że ta technika nie zadziała.

Jeśli twój projekt używa [Layers](layers.md), możesz je spłaszczyć (squash), aby zmniejszyć użycie pamięci.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Aplikacja zamyka się, gdy uruchamiam Nomad! {#crash-start}
Jeśli crashuje przy ładowaniu, oznacza to, że Nomad ma problem z jakimś plikiem znajdującym się w folderze Nomad.

Najczęściej dzieje się tak dlatego, że projekt jest ciężki i niestety przekroczy limit RAM.

Zlokalizuj [folder Nomad](#where-are-my-projects-located-on-my-device), a następnie zmień nazwę lub przenieś niektóre pliki, aby znaleźć winowajcę.

Najpierw spróbuj zmienić nazwę pliku `settings.json`. Dzięki temu Nomad przestanie ładować ostatni projekt.

Jeśli to nie zadziała, spróbuj przenieść niektóre ostatnie pliki poza ich odpowiednie foldery zasobów (`projects`, `matcaps`, `environments` itd.).

Możesz też zmienić nazwy samych folderów, aby Nomad całkowicie je zignorował.  
Jeśli zmienisz nazwę lub przeniesiesz wszystkie pliki w folderze Nomad, da to ten sam efekt co czysta instalacja.

::: tip
Gdy Nomad ładuje plik przy starcie, zawsze przenosi go do folderu `can_be_deleted/`.  
Jeśli operacja się powiedzie, plik jest przenoszony z powrotem do oryginalnego folderu.

Jeśli crash nastąpi przed zakończeniem ładowania, Nomad uruchomi się pomyślnie przy następnym starcie, ponieważ ignoruje folder `can_be_deleted/`.

Możesz po prostu spróbować załadować ten plik ponownie, jeśli uważasz, że może się udać.
:::