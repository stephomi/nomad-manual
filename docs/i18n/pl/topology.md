# ![](/icons/multires.webp) Topologia {#topology}

To menu kontroluje topologię obiektów w Nomadzie, a także narzędzia do wypiekania (bake) i przenoszenia detali między obiektami oraz między teksturami.

![](/images/topology_overview.webp)

Nomad opiera się na wielokątach, używa trójkątów i czworokątów do obsługi geometrii.
Przez topologię rozumiemy zarówno liczbę ścian, jak i sposób, w jaki punkty (wierzchołki) są połączone.

Ważne jest, aby śledzić topologię, zwłaszcza jeśli chcesz rzeźbić lub malować drobne detale.

::: tip Jak śledzić swoją topologię?
Możesz wyświetlić [Wireframe](settings.md#wireframe) lub po prostu wyłączyć [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu topologii w Nomadzie ma kilka sekcji:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Edycja wielu poziomów detalu przy użyciu podziału (subdivision)  |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Przeliczenie nowej topologii o jednolitej gęstości               |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Lokalnie dodaje/usuwa ściany w czasie rzeczywistym podczas rzeźbienia lub malowania |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Dekompozycja (decimation), UV, baking, remeshing, reprojekcja    |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Opcje prymitywów                                                 |


## Statystyki poligonów {#polygon-stats}

![](/images/topology_stats.webp)

Górna sekcja menu topologii wyświetla informacje o wielokątach dla wybranego obiektu i całej sceny. Liczby pokazują całkowitą liczbę wierzchołków, całkowitą liczbę trójkątów oraz całkowitą liczbę quadów (czterokątnych wielokątów).

Stuknięcie w tę sekcję wyświetli listę statystyk wielokątów dla wszystkich obiektów wielokątnych w scenie.

## ![](/icons/multires.webp) Multiresolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### Czym jest multiresolution? {#what-is-multiresolution}
Funkcja multiresolution jest przydatna w dwóch głównych scenariuszach:
- Algorytm gładkiego podziału (smooth subdivision), aby zwiększyć liczbę wielokątów obiektu
- Obsługa wielu poziomów rozdzielczości, aby można było przełączać się między edycją w małej i dużej skali

![](/videos/multiresolution.mp4)

#### Przepływ pracy z multiresolution {#multiresolution-workflow}
Ważnym aspektem multiresolution jest to, że możesz wrócić do niższej rozdzielczości, wprowadzić zmiany w obiekcie, a następnie wrócić do najwyższej rozdzielczości bez utraty detali wysokiej rozdzielczości. Wszystkie detale wysokiej rozdzielczości zostaną automatycznie zreprojekowane.

::: warning
Jeśli używasz narzędzia, które zmienia topologię obiektu, utracisz wszystkie pozostałe poziomy rozdzielczości tego obiektu!
Zawsze powinieneś otrzymać ostrzeżenie, gdy może do tego dojść, na przykład gdy używasz:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim tool](tools.md#trim)
- [Split tool](tools.md#split)
:::


### Suwak multiresolution {#multiresolution-slider}
Ten suwak wskazuje liczbę poziomów podziału w bieżącym obiekcie. Jeśli są 6 pionowych kresek, oznacza to 6 poziomów podziału. Kółko wskazuje aktualnie wyświetlany poziom podziału. 

### Odwróć {#reverse}
Na najniższym poziomie podziału przycisk Reverse spróbuje utworzyć poziom poniżej bieżącego. Zazwyczaj jest to możliwe tylko wtedy, gdy obiekt został pierwotnie utworzony z podziałem, np. w Nomadzie lub innych aplikacjach 3D obsługujących powierzchnie subdivision z multiresolution.

### Subdividuj {#subdivide}
Przycisk *Subdivide* zwiększy liczbę wielokątów 4‑krotnie, więc pamiętaj, aby obserwować liczbę wielokątów, ponieważ może bardzo szybko rosnąć!
Ważnym aspektem *Subdivision Surface* jest to, że zbiega ona do *Smooth Surface*.
Aby zrozumieć, jak to działa, możesz wypróbować przycisk *Subdivide* na obiekcie z niewielką liczbą wielokątów.

Możesz wyłączyć to zachowanie *Smooth*, zaznaczając opcję `Linear subdivision`.

### Usuń niższe {#delete-lower}
Jeśli istnieją poziomy podziału poniżej aktualnie wyświetlanego poziomu, usuń je. Jeśli zrobisz to przypadkowo, możesz je odtworzyć przyciskiem Reverse.

### Usuń wyższe {#delete-higher}
Jeśli istnieją poziomy podziału powyżej aktualnie wyświetlanego poziomu, usuń je.

### Liniowa subdivizja {#linear-subdivision}
Dzieli siatkę bez zastosowania wygładzania.

### Ostry brzeg {#sharp-border}
Jeśli obiekt ma facegroupy, włączenie tej opcji zachowa ostre krawędzie na granicach facegroup. Można to ustawić na każdym poziomie podziału (suwak podziału będzie miał małą ikonę nad poziomem, aby to wskazać).

### Zachowaj trójkąty {#keep-triangles}
Większość standardowych systemów subdivision surface próbuje konwertować wszystkie wielokąty na quady podczas operacji podziału. Ten przełącznik wymusi użycie trójkątów podczas podziału.

### Zablokuj (LV0) {#lock-lv0}

Zapobiega modyfikowaniu najniższego poziomu podziału. Może to być ważne, jeśli obiekt został wygenerowany w innej aplikacji i obiekt bazowy musi pozostać niezmieniony. Gdy ta opcja jest wyłączona, duże zmiany wprowadzane na wyższych poziomach podziału będą przesuwać poziom 0.

::: tip 

Subdivision domyślnie wygładza wszystkie ostre krawędzie. Aby zachować krawędzie lekko ostre, poeksperymentuj z użyciem linear subdivision lub Sharp border na pierwszych 2 poziomach podziału, a następnie wyłącz je na wyższych poziomach. Utworzy to pół‑ostro podzieloną siatkę.

:::


## ![](/icons/voxel.webp) Voxel Remesher {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Podczas używania `Voxel Remesher` cała siatka zostanie wymuszona na topologię o jednolitej rozdzielczości, co oznacza, że wszystkie wielokąty mają mniej więcej ten sam rozmiar. Jest to bardzo przydatne, gdy nie chcesz myśleć o topologii i po prostu swobodnie rzeźbić.

Typowy workflow rzeźbienia może zaczynać się od użycia `Voxel Remesher` do zablokowania ogólnego kształtu w niskiej rozdzielczości.
Po prostu naciskaj przycisk *Remesh* od czasu do czasu, gdy zbyt mocno rozciągasz siatkę, aby uniknąć nadmiernych zniekształceń.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Jak wspomniano powyżej, Nomad jest oprogramowaniem poligonalnym, ale `Voxel Remesher` jest jednym wyjątkiem, w którym do remeshingu (tymczasowo) używane jest inne podejście.

Jedną z dużych różnic jest to, że podejście voxelowe nie akceptuje samoprzecięć, więc zostaną one usunięte.
Nie obsługuje też siatek z dziurami.

Przez dziury nie rozumiemy `genus hole` (`dziura` w torusie), ale siatki, które nie są `wodoszczelne`/`zamknięte`.
Zazwyczaj oznacza to, że przed zastosowaniem remeshingu wszystkie dziury zostaną wypełnione, podobnie jak w [Trim tool](tools.md#trim) lub [Hole filling feature](scene.md#hole-filling).
:::

### Remesh {#voxel-remesh}
Wykonaj voxel remesh.

### Rozdzielczość {#voxel-resolution}
Rozmiar voxelów używanych podczas obliczeń. Podczas zmiany tego parametru na siatkę zostanie nałożony wzór szachownicy, aby dać podgląd rezultatu.

### Zbuduj multiresolution {#build-multiresolution}
Tworzy niższe poziomy multiresolution dla voxel remesh. Jeśli użyjesz wzoru szachownicy do ustawienia rozdzielczości i ustawisz build multiresolution na 2, końcowy rezultat będzie miał detal odpowiadający suwakowi rozdzielczości, a w zakładce multires będzie na poziomie 2, co oznacza, że masz siatki multires o niższej rozdzielczości na poziomie 1 i 0. Może to być dobry sposób na jednoczesne wygenerowanie czystej siatki z równymi wielokątami i posiadanie niskorozdzielczościowej siatki kontrolnej.

::: tip Tip: Build multiresolution i stable smoothing

Ta opcja może czasami powodować „pętle” w geometrii, które trudno wygładzić, powodując małe „pryszcze”. Jeśli tak się stanie, włącz „Stable smoothing” w opcjach narzędzia smooth. 

:::

### Zachowaj ostre krawędzie {#keep-sharp-edges}
Włącza przyciąganie nowych punktów do ostrych krawędzi oryginalnej siatki. Może to wprowadzać zniekształcenia.

## ![](/icons/dynamic.webp) Dynamic Topology {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution i voxel remeshing to powszechne w branży metody kontrolowania topologii, ale obie wymagają pilnowania, aby nie rozciągać wielokątów zbyt mocno ani nie ściskać ich zbyt ciasno. 

Dynamic Topology jest alternatywną metodą. Podczas rzeźbienia Nomad adaptacyjnie dodaje i usuwa wielokąty w trakcie pociągnięcia pędzla, więc rzeźbienie drobnych detali doda wiele małych wielokątów tam, gdzie ich potrzebujesz, a wygładzanie w innych miejscach usunie wielokąty.

Zwróć uwagę, że dynamic topology używa trójkątów zamiast quadów. Może to wyglądać trochę „bałaganiarsko”, ale często lepiej jest nie patrzeć na siatkę (wireframe), tylko skupić się na stworzeniu ładnej rzeźby bez martwienia się o topologię, a później użyć jednego z innych narzędzi remeshingu Nomada, aby wygenerować czystą siatkę quadów.

Zobacz wideo poniżej w akcji.

![](/videos/dynamic.mp4)

### Włączone {#enabled}
Włącza dynamic topology. Ikona DynTopo zostanie umieszczona pod suwakami promienia i intensywności pędzla, aby umożliwić przełączanie Dyntopo dla każdego narzędzia.

### Detal {#dyn-detail}
Kontroluje ilość detalu, a jego zachowanie zmienia się w zależności od wyboru „Detail based on...”, patrz poniżej.

### Detal bazujący na... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Poziom detalu zależy od tego, jak duży obiekt jest na ekranie. Suwak detail to 100% lub więcej dla drobnych detali (małe trójkąty) lub 1% dla niskiego detalu (duże trójkąty).  |
| Radius   | Promień narzędzia definiuje ilość detalu. Użyj małego promienia narzędzia dla drobnych detali, dużego promienia dla niskiego detalu. Suwak detail jest mnożnikiem tego stosunku.                     |
| Constant | Suwak detail definiuje ilość detalu i nie jest zależny od rozmiaru ekranu ani rozmiaru narzędzia.             |

::: tip TIP: Tryb Radius

Aby lepiej zrozumieć, jak działa tryb radius, zacznij przesuwać suwak detail jednym palcem, a jednocześnie zmieniaj promień narzędzia drugim palcem. Zobaczysz, jak są ze sobą powiązane.

:::

### Preferuj... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Preferuj wydajność |
| Quality | Preferuj jakość    |

Gdy preferujesz `Quality`, dwie główne różnice to:
- rafinacja jest stosowana przed rzeźbieniem, więc otrzymasz mniej artefaktów interpolacji podczas malowania lub rzeźbienia bardzo drobnych detali
- rafinacja działa, dopóki nie zbiegnie do właściwego poziomu detalu, w przeciwieństwie do zachowania przyrostowego.
 
Dzięki temu, jeśli rzeźbisz bardzo drobne detale lub wykonujesz szybkie pociągnięcia, topologia zawsze zostanie dopracowana zgodnie z oczekiwaniami


### Użyj nacisku dla promienia {#use-pressure-on-radius}
Istotne tylko, jeśli `Radius` jest aktywny. Po włączeniu poziom detalu zawsze będzie odzwierciedlał rozmiar pędzla, nawet gdy rozmiar pędzla jest modyfikowany przez nacisk rysika.

### Użyj wygaszenia pociągnięcia {#use-stroke-falloff}

Uwzględnia również krzywą wygaszania (falloff) pędzla i alfę w obliczeniach dyntopo.

### Metoda {#method}
Niezależnie od tego, czy używasz `Dynamic Topology` na swoim [Brush](#brush), czy [Globalnie](#global), możesz wybrać tryb jego działania:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Może dodawać i usuwać ściany, jest to tryb używany w powyższym filmie |
| Subdivision    | Dodaje tylko nowe ściany, nie może usuwać ścian                      |
| Decimation     | Usuwa ściany, nie może dodawać nowych                                 |

### Chroń zamaskowany obszar {#protect-masked-area}
Włącza ochronę zamaskowanych obszarów przed zmianami topologii.

### Ekstrapolacja wierzchołków {#vertex-extrapolation}


### Detal {#all-detail}
Rozdzielczość używana do operacji remesh. Jeśli Dyntopo jest w trybie „Constant”, będzie to ta sama wartość co suwak Detail na górze tego menu.

### Remesh {#dyn-remesh}
Wykonuje globalny remesh przy użyciu algorytmu dyntopo. Zazwyczaj do pełnego remeshingu powinieneś używać [Voxel Remesher](#voxel-remesher).

Jednak jedną z zalet w porównaniu z voxelami jest to, że zamaskowany obszar będzie chroniony, więc masz lepszą kontrolę nad tym, gdzie umieścić większą lub mniejszą gęstość.



## ![](/icons/topo_extra.webp) Różne {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu koła zębatego {#gear-menu}
Wiele narzędzi w tym menu ma dodatkowe opcje. Można je otworzyć za pomocą ikony koła zębatego obok tytułu sekcji.

### Decymacja {#decimation}

![](/images/topology_decimation.webp)

Zmniejsza liczbę wielokątów, starając się zachować jak najwięcej detali, używając trójkątów.

Ta funkcja może być przydatna, jeśli chcesz eksportować model do druku 3D.
Nie powinieneś jednak z niej korzystać, jeśli chcesz dalej na nim rzeźbić, ponieważ może generować nierówne trójkąty.

Zauważ, że zamaskowane obszary nie będą dekomponowane.

![](/videos/decimate.mp4)

::: tip

Używanie [Quadremesh tool](tools.md#quad-remesher) na obiektach o wysokiej liczbie wielokątów może zająć dużo czasu i dawać wyniki trudne do kontrolowania. Wstępne przetworzenie siatki za pomocą [facegroups](tools.md#facegroup-1) i decimate sprawi, że Quadremesh będzie działał znacznie szybciej i pozwoli na znacznie większą kontrolę nad topologią.

* Oznacz siatkę facegroupami, aby zdefiniować idealny przepływ quadów.
* Użyj Facegroup relax, aby wygładzić granice facegroup.
* Użyj Decimate. Zapewni to brak cienkich lub zniekształconych ścian na krawędziach facegroup. W ustawieniach decimate upewnij się, że facegroup jest włączone. Sprawi to, że krawędzie trójkątów będą dokładnie podążać za krawędziami facegroup.
* W opcjach Quadremesh upewnij się, że relax jest wyłączony (ponieważ już wygładziłeś siatkę), i powinieneś uzyskać dobre rezultaty.

:::

#### Decymuj {#decimate}
Rozpocznij operację decimate.

Ikony obok przycisku decimate pozwalają przełączać opcje wpływające na dekompozycję. Procent wskazuje siłę danej opcji i można go ustawić w zaawansowanym menu koła zębatego.

* ![](/icons/palette.webp)  `Preserve Painting` - Umieszcza więcej trójkątów tam, gdzie występują detale malowania.
* ![](/icons/triforce.webp) `Uniform Faces` - Preferuje tworzenie równomiernie rozmiarowo trójkątów.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate spróbuje zachować granice w pobliżu otwartej geometrii i dziur bez zmian.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate spróbuje zachować granice facegroup bez zmian.
* ![](/icons/uv.webp) `Preserve UV Borders` - Decimate spróbuje zachować granice UV bez zmian.

#### ![](/icons/cog.webp) Menu koła zębatego decymacji {#decimate-gear-menu}
Menu koła zębatego ma następujące zaawansowane opcje:
##### Zachowaj malowanie {#preserve-painting}
Pole wyboru przełącza ten tryb, a wartość określa, jak dokładnie zostaną zachowane detale malowania. Wyższe wartości zachowają więcej malowania. Ustaw na 0, jeśli nie zależy ci na malowaniu.


##### Jednorodne ściany {#uniform-faces}
Pole wyboru przełącza ten tryb. Wyższe wartości dadzą trójkąty o podobnym rozmiarze.

##### Zachowaj krawędzie {#preserve-borders}
Włącz, aby zapobiec dekompozycji granic. Wagi granic można wybrać dla granic `Geometry`, `Face Group` lub `UV`.

#### Docelowe trójkąty {#target-triangles}
Ustaw docelową liczbę trójkątów. Domyślna wartość to 50%, przycisk percent/target przełącza między procentem a dokładną docelową liczbą wielokątów.



### UV Unwrap - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Oblicza współrzędne tekstury (UV) dla bieżącej siatki, zazwyczaj preferując tworzenie większej liczby wysp z cięciami, aby zminimalizować zniekształcenia.

Mała ikona oka między tytułem menu a kołem zębatym przełącza podgląd UV na obiekcie.

![](/videos/unwrap.mp4)

#### Rozwiń {#unwrap}
Oblicz UV dla wybranego obiektu, które zostaną wyświetlone w tle.

#### Usuń UV {#delete-uvs}
Usuń UV z obiektu.

#### ![](/icons/cog.webp) Menu koła zębatego UVAtlas {#uvatlas-gear-menu}
Menu koła zębatego ma następujące zaawansowane opcje:

#### Grupa ścian {#atlas-face-group}

Użyj facegroup do zdefiniowania cięć dla UV.

##### Maksymalne rozciągnięcie {#max-stretch}
Niskie wartości tworzą mniejsze zniekształcenia i więcej wysp, wysokie wartości tworzą większe zniekształcenia i mniej wysp. 

##### Odstęp między wyspami {#island-spacing}
Ilość odstępu między wyspami. Niskie wartości marnują mniej miejsca, ale zwiększają ryzyko „przeciekania” tekstur między wyspami. 

::: warning
Obliczanie UV może zająć trochę czasu, najlepiej mieć siatkę z mniej niż 100k wierzchołków.
:::

::: tip UVs?
Popularną analogią dla UV jest pakowanie prezentu; jaki jest najlepszy sposób na wycięcie papieru do pakowania, aby całkowicie pokryć obiekt, bez nakładania się fragmentów? 

UV są podobne, ale zamiast cięcia papieru, tniesz obiekt. Wyobraź sobie, że twój model jest wykonany z cienkiego plastiku – jak byś go pociął, aby rozłożyć go na płasko, pomalować w tym płaskim stanie, a następnie złożyć z powrotem?

Teraz wyobraź sobie, że powierzchnia twojego modelu jest wykonana z rozciągliwej lycry. Możesz rozciągnąć model na płasko, albo go pociąć, albo połączyć oba podejścia. Ale jeśli namalujesz szachownicę na obiekcie po spłaszczeniu, szachownica będzie zniekształcona po ponownym złożeniu. Która metoda jest lepsza: więcej cięć i mniej zniekształceń, czy mniej cięć i więcej zniekształceń?

UV to instrukcje mówiące oprogramowaniu 3D, jak „ciąć i rozciągać” obiekt podczas nakładania tekstur. Narzędzie UV Atlas generalnie stosuje podejście „więcej cięć, mniej zniekształceń”.


:::

::: tip UV w Nomadzie i innych aplikacjach

Większość teksturowanych modeli, które znajdziesz online, będzie teksturowana przy użyciu UV. Nomad może je importować i wyświetlać poprzez panel [material](material#textures).

Gdy modele są tworzone w Nomadzie, możesz malować bezpośrednio na obiektach bez UV. Jeśli musisz je wyeksportować do innych aplikacji, np. [Procreate](https://procreate.art/), możesz „wypiec” informacje o kolorze Nomada w tekstury za pomocą UV. 

:::

### UV Unwrap - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV BFF preferują podejście „mniej cięć, więcej zniekształceń”. 

#### ![](/icons/cog.webp) Menu koła zębatego UV BFF {#uv-bff-gear-menu}

#### Grupa ścian {#bff-face-group}

Użyj facegroup do zdefiniowania cięć dla UV.

##### Liczba stożków {#cone-count}
Definiuje liczbę głównych projekcji użytych w procesie. Niższe wartości dadzą mniej wysp, ale więcej zniekształceń.

##### Bezszwowe płaty {#seamless-patches}
Wpływa na układ łatek UV, najlepiej działa z starannie utworzonymi facegroupami.

### Bake -> tekstura {#bake-texture}
![](/images/topology_bake_menu.webp)

Baking tekstur tworzy tekstury poprzez rzutowanie innych widocznych obiektów w scenie na UV wybranego obiektu.

Oto typowy workflow dla bakingu:
- Masz siatkę z drobnymi detalami i malowaniem
- Sklonuj ją
- Użyj Decimate (ustaw `Preserve painting` na 0)
- Zrób UV unwrap
- Bake!

Domyślnie Nomad uwzględni wszystkie widoczne siatki w scenie.
Możesz także użyć trybu Solo, aby szybko ukryć większość innych siatek.
Jeśli nie ma innych widocznych obiektów, wtedy pod uwagę zostanie wzięta cała scena.

Powinieneś teraz mieć siatkę o niskiej rozdzielczości, która zachowuje większość malowania i detali poprzedniego obiektu.

Po operacji kolory wierzchołków zostaną przeniesione do nowej wyłączonej warstwy, aby nie kolidowały z teksturami.

#### Z siebie {#tex-from-itself}
Wypieka najwyższy poziom multiresolution do najniższego poziomu na bieżącym obiekcie. Jest to proste do skonfigurowania, ale często będziesz potrzebować większej kontroli, w takim przypadku bardziej przydatna jest następna opcja.

#### Z wysokiej rozdzielczości () {#tex-from-high-res}
Wypieka z innych widocznych obiektów w scenie do wybranego obiektu. Liczba w nawiasach wskazuje liczbę innych widocznych obiektów, które zostaną użyte jako cele high‑res i wypieczone do bieżącego obiektu low‑res z UV. Inne obiekty nie muszą być podobne pod względem układu lub topologii do obiektu, na który wypiekasz, co pozwala na elastyczne workflow bakingu.

#### Rozdzielczość {#tex-bake-resolution}
Rozdzielczość wypiekanej tekstury. Tekstury bake są zawsze kwadratowe, więc 1024 utworzy obraz 1024x1024. 

Przyciski poniżej to skróty do często używanych rozdzielczości. Dla odniesienia: 512x512 jest stosunkowo małe, np. do grafiki webowej i prostej geometrii. 4096x4096 (w skrócie 4k) jest przeznaczone do renderów wysokiej jakości.

#### ![](/icons/cog.webp) Menu koła zębatego Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Menu koła zębatego ma następujące zaawansowane opcje:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity {#tex-normal-roughness-metalness-color-emissive-opacity}
Te pola wyboru określają, które właściwości zostaną wypieczone, każda do osobnej mapy. Po zakończeniu bakingu zostaną one dodane jako tekstury do materiału bieżącego obiektu.

##### Kopia zapasowa {#tex-backup}
Aby podglądać wypieczone tekstury, informacje o malowaniu obiektu powinny być wyłączone. Ta opcja przeniesie wszelkie informacje o malowaniu do nowej warstwy jako kopii zapasowej, aby można je było łatwo włączać/wyłączać.

#### Promień klatki (cage) {#tex-cage-radius}
Reguluje, jak daleko od obiektu bake wysyłane są promienie w poszukiwaniu obiektów docelowych. Domyślnie ta odległość jest utrzymywana na niskim poziomie, aby uniknąć artefaktów, ale można ją zwiększyć, jeśli obiekty docelowe są daleko od obiektu bake.

##### Przesunięcie promienia {#tex-ray-offset}
Reguluje, skąd rozpoczynają się obliczenia bake na obiekcie bake. Domyślnie zaczynają się 5% od powierzchni, co unika większości typowych artefaktów. Jeśli obiekty docelowe są bardzo daleko od obiektu bake, ten offset może wymagać zwiększenia.


### Rzutuj ponownie na wierzchołki {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Rzutuje wyrzeźbione detale, malowanie, warstwy, tekstury na wartości wierzchołków.

Można o tym myśleć jako o odwrotności bakingu; jeśli baking przenosi właściwości wierzchołków do tekstur, reprojekcja przenosi tekstury (i inne właściwości)
 z powrotem do wierzchołków.

::: tip
Podczas używania `Bake to texture` lub `Reproject to vertex` zarówno kolory wierzchołków, jak i tekstury materiału będą brane pod uwagę.
:::

#### Z siebie {#vertex-from-itself}
Konwertuje tekstury z materiału na wartości wierzchołków. Ten przycisk będzie aktywny tylko wtedy, gdy obiekt ma UV i w materiale są aktywne tekstury.

::: tip TIP: Malowanie tekstur
Nomad nie obsługuje bezpośrednio malowania i edycji tekstur, ale bardzo podobne rezultaty można osiągnąć, rzutując tekstury -> wartości wierzchołków, malując na wierzchołkach, a następnie wypiekając wierzchołki -> tekstury:

1. Skonfiguruj obiekt low poly z UV
1. Załaduj tekstury do jego materiału
1. Podziel go (subdivide) wystarczająco, aby można było na nim malować
1. Użyj `Reproject to vertex` w trybie `From itself`, teraz tekstura została przekonwertowana na wartości wierzchołków
1. Maluj, wygładzaj, rozmazuj, stempluj – wykonaj wszystkie potrzebne edycje
1. Użyj `Bake to texture` w trybie `From itself`. Te edycje zostaną z powrotem przekonwertowane na tekstury.
:::

#### Z wysokiej rozdzielczości () {#vertex-from-high-res}
Konwertuje wszystkie widoczne obiekty na wartości wierzchołków na wybranym obiekcie. Liczba na tym przycisku wskazuje liczbę widocznych obiektów.

::: tip
Reprojekcja innych obiektów może być używana nie tylko do przenoszenia informacji o kolorze z innych obiektów, ale także do rzutowania wierzchołków na inne obiekty, np. bandaże mogą zostać zreprojekowane na postać.
:::

#### ![](/icons/cog.webp) Menu koła zębatego Reproject {#vertex-reproject-gear-menu}
Menu koła zębatego ma następujące zaawansowane opcje:

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Te pola wyboru określają, które właściwości zostaną zreprojekowane na wybrany obiekt. 

#### Wygładź {#vertex-relax}
Wybrana siatka może mieć swój układ wygładzony lub rozluźniony w pewnym stopniu, aby lepiej dopasować się do celów reprojekcji. Smooth jest lepsze dla siatek o wysokiej liczbie wielokątów. Relax jest lepsze dla siatek low poly. Auto pozwoli Nomadowi określić najlepszą metodę.

#### Iteracje {#vertex-iterations}
Ile razy operacja relax powinna zostać zastosowana podczas reprojekcji.

#### Promień klatki (cage) {#vertex-cage-radius}
Reguluje, jak daleko od wybranego obiektu wysyłane są promienie w poszukiwaniu obiektów docelowych. Domyślnie ta odległość jest utrzymywana na niskim poziomie, aby uniknąć artefaktów, ale można ją zwiększyć, jeśli obiekty docelowe są daleko od obiektu bake.

#### Bias promienia {#vertex-ray-bias}
Niższe wartości preferują rzutowanie na najbliższy punkt na powierzchni docelowej. Wyższe wartości preferują punkt przecięcia z użyciem normalnej powierzchni. 

#### Przesunięcie promienia {#ray-vertex-offset}
Reguluje, skąd rozpoczynają się obliczenia bake na wybranym obiekcie. Domyślnie zaczynają się 5% od powierzchni, co unika pewnych artefaktów. Jeśli obiekty docelowe są bardzo daleko od obiektu bake, ten offset może wymagać zwiększenia.


### Quad Remesh - Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remesh przy użyciu [algorytmu Instant Meshes autorstwa Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analizuje przepływ siatki i tworzy czystą topologię quadów.

::: tip
Na iOS i desktopie narzędzie [Quad remesher](tools#quad-remesher) daje lepsze rezultaty i większą kontrolę.
:::

#### Remesh {#instant-remesh}
Rozpocznij operację instant meshes.

#### Docelowe quady {#target-quads}
Liczba wielokątów quad, które quad remesh spróbuje utworzyć.

#### ![](/icons/cog.webp) Menu koła zębatego Quad Remesh Instant {#quad-remesh-instant-gear-menu}
Menu koła zębatego ma następujące zaawansowane opcje:

##### Kąt załamania {#crease-angle}
Próg ostrych krawędzi, który spróbuje pomóc w prowadzeniu operacji remesh.

#### Maksymalne wypełnienie dziury {#max-fill-hole}
Algorytm może czasami tworzyć niepożądane dziury. Jeśli dziura ma mniej wierzchołków niż ta wartość, zostanie wypełniona.

### Dziury {#holes}
![](/images/topology_holes_menu.webp)
Większość czasu twój obiekt prawdopodobnie będzie wodoszczelny, co oznacza, że siatka jest „zamknięta”.

Jeśli obiekt ma dziury, możesz je wypełnić. Zauważ, że działa to tylko na „naiwne” dziury, a więc nie może „zespawać” dwóch oddzielnych granic.

![](/videos/hole_filling.mp4)

::: tip
Gdy uruchamiasz Voxel remesher, wszystkie dziury są automatycznie zamykane, niezależnie od tego, czy używasz go na jednej, czy na wielu siatkach.
:::

#### Zamknij dziury {#close-holes}
Wykonaj akcję zamykania dziur.

#### ![](/icons/cog.webp) Menu koła zębatego Dziur {#holes-gear-menu}
Menu koła zębatego ma następujące zaawansowane opcje:

##### Detal {#fill-detail}
Gęstość wielokątów używana do wypełnienia dziury. Podczas przeciągania tego suwaka na modelu zostanie pokazany wzór szachownicy, który da wskazanie rozmiaru trójkątów do użycia. Pole wyboru wyłączy to i użyje tylko istniejących punktów, co zazwyczaj stworzy długie, cienkie trójkąty nad dziurą, które mogą być trudne do rzeźbienia.

##### Wypełnij niemani-fold {#fill-non-manifold}
Spróbuj wypełnić dziurę non‑manifold.

##### Grupa ścian {#fill-face-group}

Podczas wypełniania dziur: czy każda dziura powinna otrzymać własną facegroup (Auto), czy wszystkie powinny współdzielić jedną facegroup (Off), czy nie tworzyć facegroup (On).

### Wymuś manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Próbuje wyczyścić krawędzie non‑manifold. Może być przydatne dla zewnętrznego oprogramowania, które nie obsługuje krawędzi mających więcej niż 2 ściany wspólne.

#### Wyczyść {#clean}
Wykonaj akcję clean.
#### ![](/icons/cog.webp) Menu koła zębatego Force manifold {#force-manifold-gear-menu}
Menu koła zębatego ma następujące zaawansowane opcje:

#### Usuń małe ściany {#delete-small-faces}
Próg używany do usuwania i łączenia małych wielokątów.


### Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Konwertuje siatkę na prymityw [triplanar](scene.md#triplanar).
Prawdopodobnie utracisz dużo detali w tym procesie.

#### Wymuś sześcienność {#force-cubic}
Wymusza, aby triplanar był sześcianem. W przeciwnym razie triplanar dopasuje się do najbliższego pudełka ograniczającego (bounding box) wokół obiektu.

#### Konwertuj {#convert}
Wykonaj akcję triplanar.

#### Rozdzielczość {#triplanar-resolution}
Rozmiar voxela używany w operacji triplanar.

## ![](/icons/dot.webp) Prymityw {#primitive}
Parametry wybranego prymitywu. Są one również dostępne na pasku narzędzi prymitywów w widoku.

![](/images/topology_primitive_screenshot.webp)