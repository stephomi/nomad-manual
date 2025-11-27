# ![](/icons/manual.webp) Wskazówki

[[toc]]

## Jak rozpocząć model

Początkujący w rzeźbieniu 3D często pytają, jaki jest najlepszy sposób na rozpoczęcie modelu. Nie ma jednego najlepszego sposobu – różni ludzie mają różne preferencje. Oto kilka najczęściej spotykanych podejść.

### Rzeźbienie na sferze, multires

Domyślny model po uruchomieniu Nomada to najczęściej używany sposób. Używaj narzędzi Move, Clay, Crease, aby wypychać i wciągać sferę w pożądany kształt, używaj niższych poziomów podziału, gdy chcesz szybko wprowadzać duże zmiany, oraz wyższych poziomów podziału do pracy nad detalami.

Częstym problemem jest to, że często zabraknie Ci wielokątów tam, gdzie ich potrzebujesz, podczas gdy w innych miejscach będzie ich za dużo. Np. jeśli z domyślnej sfery wyciągniesz pełne ciało, prawdopodobnie nie będziesz mieć wystarczającej ilości detalu, aby wyrzeźbić palce, a jednocześnie będziesz mieć mnóstwo zmarnowanych wielokątów z tyłu głowy. Dla kształtów w większości sferycznych, jak głowa, może to jednak być w porządku.

### Dyntopo

Włączenie Dyntopo będzie adaptacyjnie dodawać i usuwać wielokąty podczas rzeźbienia. Te wielokąty będą trójkątami i początkujący często nie lubią tego „bałaganu” w siatce w porównaniu z czystym wyglądem multires. Warto się jednak przemóc! Jeśli włączysz gładkie cieniowanie, wyłączysz siatkę (wireframe) i przestaniesz przejmować się układem, ten tryb może dać bardzo „gliniany” feeling. Pamiętaj, że przy użyciu dużego pędzla lub pędzla Smooth ten tryb może również usuwać wielokąty, więc narzędzie zawsze wydaje się szybkie i responsywne. Gdy skończysz pierwsze przejście rzeźby, możesz ją sklonować, przepuścić przez quad remesher, aby uzyskać ładny układ, a następnie przeprojektować (reproject) oryginalne detale na wysoki poziom podziału.

### Voxel remesh

Voxel remesh zastosuje w większości czworokątną topologię na Twojej rzeźbie. Ta operacja jest szybka przy niższych rozdzielczościach i może być używana do szybkiej zamiany rozciągniętych lub zbyt gęstych wielokątów na równomiernie rozłożony układ. To świetny sposób na rozpoczęcie pełnego ciała od sfery; powiedzmy, że zaczynasz od głowy, możesz wyciągnąć szyję, zrobić voxel remesh. Wyciągnąć tułów, voxel remesh, ramiona, voxel remesh i tak dalej, aż uzyskasz podstawowe formy.

### Używanie wielu obiektów

Wiele atlasów anatomicznych przedstawia ciało jako złożone z prostych sfer, walców, kostek. W Nomadzie możesz rzeźbić w podobny sposób. Ma to tę zaletę, że możesz rodzicować (parent) obiekty w hierarchii sceny, tak aby np. przy obrocie szyi głowa podążała za nią. Możliwość używania narzędzia gizmo do precyzyjnego przesuwania/obracania/skali jest również bardzo przydatna, a do tego możesz ustawiać pivoty dla poszczególnych kształtów, aby poruszały się dokładnie tak, jak oczekujesz. Gdy podstawowe bryły są na właściwych miejscach, możesz zaznaczyć je wszystkie i użyć voxel remesh lub boolean, aby połączyć je w jedną powierzchnię do bardziej szczegółowego rzeźbienia.

Przydatna wskazówka dla takiego sposobu pracy: zacznij od sfery, przeskaluj ją w wydłużoną „parówkę”, naciśnij Pivot, kliknij „Bottom”, naciśnij Pivot ponownie. Masz teraz część ciała, którą możesz klonować, przesuwać wzdłuż długości pierwszej sfery, klonować, obracać, klonować, przesuwać itd., aby szybko rozłożyć całe ciało.

### Tubes

Narzędzie Tube to świetny sposób na rozpoczęcie rzeźby. Ogony gadów, ramiona, nogi, palce, brwi – wszystko to można szybko naszkicować narzędziem Tube, a następnie łatwo edytować. Pozwala ono również modyfikować profil przekroju, co umożliwia szybkie zmiany kształtu. Możesz zatwierdzić (validate) kształt, aby zacząć na nim rzeźbić, a następnie użyć voxel remesh wraz z innymi obiektami, aby uzyskać pełną siatkę ciała.

### Używanie innych aplikacji

Niektórzy wolą zaczynać model w innych aplikacjach i to też jest w porządku. Narzędzia takie jak Blender czy Valence pozwalają zaczynać modele technikami low poly, a następnie można je zaimportować do Nomada do rzeźbienia.

### Używanie wbudowanych presetów

W menu projektu kliknij `Preset...` w prawym górnym rogu. Znajdziesz tam kilka presetów kształtów głów i ciał od Blender Foundation. Wybierz taki, który Ci się podoba, stuknij go ponownie, aby dodać go do sceny. 

### Używanie modeli online

W sieci dostępnych jest wiele darmowych modeli, np. Polyhaven, Sketchfab, Turbosquid. Zazwyczaj można je zaimportować do Nomada i albo rzeźbić na nich bezpośrednio, albo używać jako referencji.

### Brak zasad!

Ostatecznie możesz używać dowolnej kombinacji tych technik albo żadnej z nich! Nomad jest pod tym względem bardzo elastyczny – zaawansowani użytkownicy mogą zacząć od tubes, potem przejść na dyntopo, potem połączyć z pobraną stopą, potem wszystko przepuścić przez quad remesh, a na końcu użyć multires do finalnych detali. Rób to, co działa dla Ciebie.

## Facegroups

Narzędzie Facegroup może być używane do wielu rzeczy, co wyjaśniono w tym filmie na YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

To jest tekstowe podsumowanie funkcji omówionych w tym filmie.

### Dlaczego facegroups?

Facegroups pozwalają organizować i zaznaczać „faces” (w tym podręczniku „faces” i „polygons” są używane zamiennie). Jest to łatwiejsze do wyjaśnienia w porównaniu z innymi narzędziami zaznaczania i organizacji w Nomadzie. Nomad pozwala tworzyć obiekty, nazywać je, rodzicować, łatwo jest stworzyć strukturę obiektów definiującą pokój złożony z podłogi, ścian, krzesła, stołu itd.

Dla postaci możesz zrobić początkowy block-out używając osobnych obiektów dla głowy, ramienia, nogi, ale gdy połączysz wszystkie części w jedną siatkę, ta struktura zostaje utracona. Możesz pracować na podsekcjach postaci za pomocą masek, ale może być męczące ciągłe malowanie maski na dłonie, potem na nos, potem znowu na dłonie.

Tu właśnie przydają się facegroups. Pozwalają oznaczać poligony kolorem, a następnie zaznaczać i manipulować poligonami o tym samym kolorze. Zauważ, że kolor facegroup i kolor wierzchołków (vertex color) to różne rzeczy.

Najbliższa analogia to malowanie kolorów na mapie, a następnie możliwość zaznaczania krajów lub regionów na podstawie koloru.

Dla głów postaci możesz pomalować strefy oznaczające oczodoły, nos, usta, podbródek, uszy, a potem łatwo zaznaczać te strefy. Przy twardych powierzchniach i rzeźbieniu mechanicznym przydatne może być definiowanie paneli i sekcji.

### Tworzenie i edycja facegroups

Facegroups można nakładać pędzlem, gdzie każdy nowy pociąg tworzy nową facegroup, albo mogą wybierać facegroup pod kursorem i ją rozszerzać. Można je też tworzyć za pomocą kształtów.

* Dot, auto-pick włączony – pojedyncze przeciągnięcie zdefiniuje nowy kolor facegroup i przypisze go do faces, po których przeciągniesz. Każde nowe przeciągnięcie zdefiniuje nową facegroup. Stuknięcie wypełni nową facegroup.
* Dot, auto-pick wyłączony – gdy przycisk auto-pick jest w trybie „sub”, Nomad wybierze facegroup pod kursorem i będzie ją stosował podczas reszty przeciągnięcia. Jest to przydatne do dopracowywania facegroups bez konieczności ręcznego ich wybierania.

### Maskowanie

Gdy narzędzie Mask jest aktywne, a przycisk facegroup jest aktywny na jego pasku narzędzi, stuknięcie facegroup zamaskuje ją.


### Ukrywanie

Gdy narzędzie Hide jest aktywne, a przycisk facegroup jest aktywny na jego pasku narzędzi, stuknięcie facegroup ukryje ją.

### Organizacja

Jak wspomniano wcześniej, facegroups mogą być używane do organizowania siatki bez konieczności tworzenia osobnych obiektów. Możesz nie chcieć dzielić głowy na osobne obiekty dla nosa, podbródka, uszu, ale bardzo przydatne jest zdefiniowanie ich za pomocą facegroups.

### Regiony UV

Narzędzie UV Atlas spróbuje automatycznie zdefiniować szwy, ale czasem umieści je tam, gdzie ich nie chcesz. Jeśli na obiekcie istnieją facegroups i opcja facegroup jest aktywna w opcjach UV Atlas, zamiast tego użyje granic facegroups jako szwów UV.

### Quad remesher

Plugin quad remesher zazwyczaj ładnie prowadzi krawędzie na Twoim modelu, ale możesz użyć facegroups, aby pomóc nim sterować, gdy opcja facegroup jest włączona. Może to ułatwić zdefiniowanie czystego przepływu krawędzi wokół oczu, łuku brwiowego, ust, fałdu policzka itp.

### Filtrowanie z innymi narzędziami

Wiele narzędzi ma opcje uwzględniania facegroups, albo w głównym menu narzędzia, albo przez Stroke -> Filtering. Na przykład narzędzie Smooth przy mocach powyżej 100% może agresywnie wygładzać detale wewnątrz facegroup, ale zachować granice facegroup w miarę nienaruszone.

### Relaksacja i wygładzanie granic facegroup

Opcja Relax w narzędziu Facegroup doskonale wygładza granice facegroups, zachowując inne cechy. To świetny sposób na zdefiniowanie gładkich granic facegroup przed quad remeshingiem.

## Ograniczenia na tabletach/urządzeniach mobilnych

Współczesne tablety i telefony są bardzo wydajne, ale mają istotne różnice w porównaniu z komputerami stacjonarnymi i laptopami:

### Brak aktywnego chłodzenia

Komputery mają wentylatory i/lub duże radiatory, aby utrzymać niską temperaturę i są zaprojektowane do pracy w wysokich temperaturach. Sprzęt mobilny jest zwykle projektowany przede wszystkim pod kątem smukłości, a nie chłodzenia wnętrza. Jeśli Nomad jest używany na najwyższych ustawieniach jakości (tryb oświetlenia PBR, złożone materiały, wiele obiektów, wiele włączonych opcji postprocessingu), może to zarówno przegrzać urządzenie, jak i bardzo szybko rozładować baterię. 

Lepszym podejściem jest użycie trybu oświetlenia matcap oraz niższego render multiplier (na górze menu postprocess). Te wybory utrzymają urządzenie w chłodzie i pozwolą Ci rzeźbić dłużej.

### Ograniczona pamięć

Nomad może osiągać rezultaty równe większości desktopowych aplikacji do rzeźbienia, ale nie może naginać praw fizyki! Większość komputerów stacjonarnych ma dwa razy więcej pamięci niż urządzenia mobilne, a stacje robocze do animacji 3D często mają 4x lub 8x więcej pamięci. Z tego powodu warto być świadomym, ile wielokątów używasz, zrobić kilka testów na swoim urządzeniu, aby zobaczyć, kiedy zaczyna się lag. Prawie wszystkie urządzenia, które potrafią uruchomić Nomada, radzą sobie dość łatwo z 1 milionem wielokątów. Ipad Pro z M2 radzi sobie komfortowo z 8 milionami, a ludzie testowali na najnowszych Ipadach wartości znacznie powyżej tego.

Mimo to tylko najbardziej szczegółowe rzeźby potrzebują więcej niż 4 milionów wielokątów; jeśli tworzysz stosunkowo proste obiekty i często przekraczasz 500 000, 1 milion, 4 miliony, używasz zbyt wielu wielokątów! Upewnij się, że masz włączony tryb smooth shaded w opcjach.

### System operacyjny jest mniej wyrozumiały dla intensywnych aplikacji

Apple i Android zakładają, że aplikacje będą zapisywać i wczytywać małe pliki bardzo szybko. Zakładają też, że aplikacje mogą bardzo szybko przełączać zadania. Nomad robi sprytne sztuczki, aby utrzymać rozmiary plików stosunkowo małe i zapisywać je bardzo szybko, ale jeśli mobilny system operacyjny uzna, że Nomad zajmuje zbyt dużo czasu, po prostu go zabije, zanim skończy zadanie. To kolejny powód, aby utrzymywać pliki po mniejszej stronie; możliwe jest pracowanie na rzeźbach 37 milionów wielokątów, jak zgłosił jeden użytkownik na Discordzie, ale nie jest to zalecane!

## Praca na małych ekranach

Nomad jest zaprojektowany do pracy na tabletach, ale dobrze działa także na telefonach. Rzeźbienie na małym ekranie, takim jak telefon, można ułatwić kilkoma zmianami w UI i workflow:

* Dotknięcie czterema palcami przełącza cały interfejs, dając więcej miejsca na rzeźbienie.
* Przeciągnięcie trzema palcami w górę i w dół zmienia promień pędzla.
* Skalę UI można zmniejszyć, aby zmieścić więcej przycisków, jeśli masz dobry wzrok, lub zwiększyć, jeśli masz słaby wzrok.
* Szerokie menu czasem zasłaniają rzeźbę, możesz je ustawić jako przezroczyste i bez rozmycia, aby widzieć rzeźbę pod spodem.
* Jeśli rzeźbisz palcem, użyj opcji offset, aby przesunąć środek pędzla nieco od palca.
* Te i wiele innych opcji znajdziesz w [Interface menu](./interface.md). 


## Deformer Inflate lub Peak

Wiele aplikacji 3D ma deformer Inflate, który wypycha wszystkie wierzchołki wzdłuż ich normalnych o kontrolowaną wartość. Choć Nomad obecnie nie ma deformerów, można zasymulować to zachowanie pędzlem Inflate:

* Wybierz pędzel Inflate
* W [Stroke menu](./stroke.md#stroke) zmień metodę stroke na `Lock + Radius'
* Ustaw promień pędzla większy niż Twoja rzeźba, w razie potrzeby oddal kamerę od rzeźby.
* Kliknij, a następnie przeciągnij stroke po powierzchni obiektu; gdy promień jest większy niż obiekt, cały kształt zostanie równomiernie napompowany o stałą wartość.
* Dostosuj intensywność pędzla, aby kontrolować ilość „napompowania”.
* Użyj maskowania, jeśli chcesz chronić lub zmniejszyć efekt Inflate w określonych obszarach.

## Usuwanie grudek lub „pryszczy” po operacji voxel remesh

Voxel remesh świetnie nadaje się do tworzenia równomiernie rozłożonych wielokątów, ale czasem tworzy topologię, która powoduje małe grudki lub „pryszcze” podczas wygładzania. Na przykład:

* Użyj pędzla Crease na domyślnej sferze i zrób spiralę
* Zrób voxel remesh z „build multiresolution at 3”
* Wygładzaj z wysoką intensywnością
* pojawiają się artefakty (łatwiej je zobaczyć przy materiale matcap o wysokim kontraście):

![](/videos/tip_pimples_before.mp4)

Aby naprawić to rzeźbieniem, spróbuj opcji `Stable smoothing` w ustawieniach Smooth. Potrafi ona poradzić sobie z nierównym układem topologii po voxel remesh i dać czyste rezultaty.

![](/videos/tip_pimples_stable_smooth.mp4)

Aby naprawić samą topologię, użyj nowego prymitywu, narzędzi quad remesh lub zewnętrznego modelera 3D i przenieś detale z oryginalnej siatki na nową przez `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Oświetlenie dzienne

Domyślny render PBR jest – jak sama nazwa wskazuje – fizycznie poprawny, co podobnie jak nieprzetworzone zdjęcie cyfrowe może wyglądać nieco wypłowiale i płasko. Światła i postprocessing w Nomadzie mogą sprawić, że rendery będą wyglądać bardziej żywo.

Oto domyślny render, zobaczmy, czy możemy go poprawić:
![](/images/tips_lighting_default.webp)

Włączenie postprocessingu i tonemappingu może dodać jasności i kontrastu:

![](/images/tips_lighting_tonemap.webp)

Skupiając się na światłach: domyślne światło środowiskowe jest dobre do rzeźbienia, ale można je poprawić na finalny render. Jednym ze sposobów myślenia o tym jest rozdzielenie światła bezpośredniego (np. słońce) od światła środowiskowego (np. światło z błękitu nieba, podłoża). Zmniejszając światło środowiskowe i obracając je, zaczynamy oddawać to, jak wyglądałoby oświetlenie, gdyby obiekt znajdował się w cieniu:

![](/images/tips_lighting_env.webp)

Można dodać światło bezpośrednie i zwiększyć jego intensywność, aby zasymulować ostre światło słoneczne. Zbalansowanie go ze światłem środowiskowym da przyjemny efekt:

![](/images/tips_lighting_sunlight.webp)

Postaciom może pomóc zmiana materiału na subsurface i umieszczenie światła punktowego (spotlight) za postacią, skierowanego na uszy, aby sprawić, że będą „świecić”:

![](/images/tips_lighting_sss.webp)

Następnie poeksperymentuj z resztą ustawień postprocessingu! Global Illumination i Ambient Occlusion pomagają w bardziej realistycznym oświetleniu. Curvature i Sharpen mogą pomóc wydobyć więcej detalu z rzeźby. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette pomagają symulować efekty kamery. Zauważ, że w miarę włączania kolejnych funkcji trzeba dostosowywać oświetlenie i inne wartości postprocessingu, aby to zrównoważyć.

Oto render z pełnym zestawem poprawek postprocessingu:
![](/images/tips_lighting_final.webp)
