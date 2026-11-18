# ![](/icons/multires.webp) Topologia {#topology}

To menu zarządza topologią obiektów w Nomadzie i zawiera narzędzia do wypalania oraz przenoszenia detali między obiektami, a także między teksturami.

![](/images/topology_overview.webp)

Nomad opiera się na wielokątach: geometrię tworzą trójkąty i czworokąty.
Mówiąc o topologii, mamy na myśli zarówno liczbę ścian, jak i sposób, w jaki połączone są punkty (wierzchołki).

Warto pilnować topologii, zwłaszcza gdy chcesz rzeźbić lub malować drobne detale.

::: tip Jak pilnować topologii?
Możesz włączyć [Szkielet](settings.md#wireframe) albo po prostu wyłączyć [Płynne cieniowanie](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu Topologia ma kilka kart, ułożonych w dwóch rzędach:

| Metoda                                | Ikona                        | Opis                                                             |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Wielokrotna rozdzielczość](#multiresolution) | ![](/icons/multires.webp)   | Edycja kilku poziomów szczegółowości dzięki podziałowi |
| [Remesh wokselowy](#voxel-remesher)   | ![](/icons/voxel.webp)      | Tworzy nową topologię o jednolitej gęstości                      |
| [Topologia dynamiczna](#dynamic-topology) | ![](/icons/dynamic.webp)    | Dodaje i usuwa ściany lokalnie, na bieżąco, podczas rzeźbienia lub malowania |
| [Różne](#misc)                        | ![](/icons/topo_extra.webp) | Zamykanie otworów, wymuszanie manifold i konwersja na obiekt trzypłaszczyznowy |
| [Prymityw](#primitive)                | ![](/icons/dot.webp)        | Opcje prymitywu                                                  |
| [Uprość](#decimation)                 | ![](/icons/decimate.webp)      | Zmniejsza liczbę ścian, zachowując kształt                    |
| [Przebudowa na czworokąty](#quad-remesh) | ![](/icons/quad.webp)       | Odbudowuje obiekt z czystym układem czworokątów                 |
| [Rozwijanie UV](#uv-unwrap)           | ![](/icons/uv.webp)         | Tworzy UV do teksturowania                                       |
| [Zastosuj](#bake)                     | ![](/icons/bake.webp)       | Wypala detale i malowanie do tekstur, wierzchołków lub stempli VDM |


## Statystyki wielokątów {#polygon-stats}

![](/images/topology_stats.webp)

U góry każdej karty widać liczbę wielokątów zaznaczonego obiektu, a gdy w scenie jest więcej niż jeden obiekt, także całej sceny. Kolumny to kolejno liczba wierzchołków, trójkątów, czworokątów (wielokątów o 4 bokach) i współrzędnych UV (0, gdy obiekt nie ma UV).

Stuknij tę sekcję, aby zobaczyć listę wszystkich obiektów sceny z ich dokładnymi liczbami, w tym liczbą grup powierzchni.

## ![](/icons/cog.webp) Menu z kołem zębatym {#gear-menu}
Niektóre sekcje, na przykład te w kartach [Przebudowa na czworokąty](#quad-remesh) i [Zastosuj](#bake), mają dodatkowe opcje. Otwierasz je ikoną koła zębatego obok tytułu sekcji.

## ![](/icons/multires.webp) Wielokrotna rozdzielczość {#multiresolution}

![](/images/topology_multires_menu.webp)

### Czym jest wielokrotna rozdzielczość? {#what-is-multiresolution}
Wielokrotna rozdzielczość przydaje się głównie w dwóch sytuacjach:
- gładki podział, który zwiększa liczbę wielokątów obiektu,
- obsługa kilku poziomów rozdzielczości, dzięki czemu możesz przechodzić między drobnymi a dużymi zmianami.

![](/videos/multiresolution.mp4)

#### Praca z wielokrotną rozdzielczością {#multiresolution-workflow}
Ważne jest to, że możesz wrócić do niższej rozdzielczości, zmienić obiekt, a potem wrócić do najwyższej rozdzielczości bez utraty drobnych detali. Wszystkie detale wysokiej rozdzielczości zostaną automatycznie rzutowane na nowy kształt.

[Warstwy](layers.md#layers) działają na każdym poziomie rozdzielczości.

::: warning
Jeśli użyjesz narzędzia, które zmienia topologię obiektu, stracisz wszystkie pozostałe poziomy rozdzielczości!
Nomad zawsze powinien cię wtedy ostrzec, na przykład gdy używasz:
- [Remeshu wokselowego](#voxel-remesher)
- [Topologii dynamicznej](#dynamic-topology)
- [narzędzia Przytnij](tools.md#trim)
- [narzędzia Podziel](tools.md#split)
:::


### Suwak wielokrotnej rozdzielczości {#multiresolution-slider}
Ten suwak pokazuje, ile poziomów podziału ma bieżący obiekt. Jeśli widzisz 6 pionowych kresek, obiekt ma 6 poziomów podziału. Kółko wskazuje aktualnie wyświetlany poziom.

Małe ikony nad suwakiem pokazują, które opcje (`Zablokuj poziom 0`, `Liniowy`, `Ostra granica`, `Zachowaj trójkąty`) zostały użyte na danym poziomie.

### Odwróć {#reverse}
Na najniższym poziomie podziału przycisk Odwróć spróbuje utworzyć poziom poniżej bieżącego. Zwykle udaje się to tylko wtedy, gdy obiekt od początku powstał przez podział, na przykład w Nomadzie lub w innej aplikacji 3d obsługującej powierzchnie podziałowe z wielokrotną rozdzielczością.

### Podziel {#subdivide}
Przycisk *Podziel* zwiększa liczbę wielokątów czterokrotnie, więc pilnuj ich liczby, bo rośnie bardzo szybko! Gdy wynik byłby bardzo ciężki, Nomad poprosi o potwierdzenie.
Ważną cechą *powierzchni podziałowych* jest to, że dążą do *gładkiej powierzchni*.
Aby zobaczyć, jak to działa, wypróbuj przycisk *Podziel* na obiekcie z niewielką liczbą wielokątów.

To *wygładzanie* możesz wyłączyć opcją `Liniowy`.

### Usuń niższe {#delete-lower}
Usuwa poziomy podziału poniżej aktualnie wyświetlanego. Jeśli zrobisz to przez przypadek, możesz je odtworzyć przyciskiem Odwróć.

### Usuń wyższe {#delete-higher}
Usuwa poziomy podziału powyżej aktualnie wyświetlanego.

### ![](/icons/lock.webp) Zablokuj poziom 0 {#lock-lv0}
Zachowuje kształt najniższego poziomu podziału, gdy rzeźbisz na wyższych poziomach. Malowanie nadal trafia na poziom 0. Ma to znaczenie, gdy obiekt powstał w innej aplikacji, a siatka bazowa musi pozostać bez zmian.

Opcja jest dostępna tylko przed pierwszym podziałem. Gdy jest wyłączona, duże zmiany na wyższych poziomach podziału przesuwają też poziom 0.

### ![](/icons/linear.webp) Liniowy {#linear-subdivision}
Dzieli siatkę bez żadnego wygładzania.

### ![](/icons/group.webp) Ostra granica {#sharp-border}
Jeśli obiekt ma grupy powierzchni, ta opcja zachowuje ostre granice między nimi. Można ją ustawić osobno dla każdego poziomu podziału (suwak pokaże wtedy małą ikonę nad danym poziomem).

### ![](/icons/triangle.webp) Zachowaj trójkąty {#keep-triangles}
Większość typowych systemów powierzchni podziałowych podczas podziału zamienia wszystkie wielokąty na czworokąty. Ta opcja wymusza podział z użyciem trójkątów.

::: tip

Podział domyślnie wygładza wszystkie ostre krawędzie. Aby zachować lekko ostre krawędzie, spróbuj użyć `Liniowy` lub `Ostra granica` na pierwszych 2 poziomach podziału, a na wyższych je wyłącz. Uzyskasz w ten sposób półostrą podzieloną siatkę.

:::

### Pokaż najwyższy poziom {#show-highest-level}
Wyświetla najwyższy poziom ze wszystkimi detalami, gdy rzeźbisz na niższym. Przydaje się, by widzieć efekt końcowy podczas dużych zmian.

### Szkielet: Tylko poziom 0 {#wireframe-level-0-only}
Gdy [Szkielet](settings.md#wireframe) jest włączony, pokazuje tylko szkielet najniższego poziomu. Gęsty szkielet wysokich poziomów potrafi zasłonić kształt.


## ![](/icons/voxel.webp) Remesh wokselowy {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Remesh wokselowy nadaje całej siatce jednolitą rozdzielczość, czyli wszystkie wielokąty mają mniej więcej ten sam rozmiar. To bardzo wygodne, gdy nie chcesz myśleć o topologii, tylko swobodnie rzeźbić.

Typowa praca może zacząć się od remeshu wokselowego, by w niskiej rozdzielczości nakreślić przybliżony kształt.
Gdy za bardzo rozciągasz siatkę, co jakiś czas naciśnij przycisk *Ponownie utwórz siatkę*, aby uniknąć zniekształceń.

![](/videos/voxel_remesher.mp4)


::: tip Woksele?
Jak wspomnieliśmy, Nomad pracuje na wielokątach, ale remesh wokselowy jest wyjątkiem: do przebudowy siatki (tymczasowo) używa innego podejścia.

Duża różnica polega na tym, że podejście wokselowe nie dopuszcza samoprzecięć, więc zostaną one usunięte.
Nie obsługuje też siatek z otworami.

Przez otwory nie rozumiemy `otworu genus` (`dziury` w pączku), tylko siatki, które nie są `szczelne`/`zamknięte`.
W praktyce oznacza to, że przed przebudową wszystkie otwory zostaną wypełnione, podobnie jak przy [narzędziu Przytnij](tools.md#trim) czy [wypełnianiu otworów](#holes). Sposób wypełniania wybierasz opcją [Otwory](#voxel-holes) poniżej.
:::

### ![](/icons/voxel.webp) Ponownie utwórz siatkę {#voxel-remesh}
Wykonuje remesh wokselowy. Małe ikony na przycisku przypominają, które z poniższych opcji są włączone.

### Rozdzielczość {#voxel-resolution}
Rozmiar wokseli użytych w obliczeniach: wyższe wartości dają więcej detali. Podczas zmiany tego parametru na siatce pojawia się szachownica, która pokazuje podgląd wyniku.

Zakraplacz pobiera rozdzielczość z gęstości siatki w miejscu, które stukniesz. Przycisk z sześcianem obok przełącza wartość na `Długość krawędzi` w jednostkach świata: ta sama wartość daje wtedy te same detale na każdym obiekcie.

### Utwórz wielokrotną rozdzielczość {#build-multiresolution}
Tworzy niższe poziomy wielokrotnej rozdzielczości dla remeshu wokselowego. Jeśli ustawisz rozdzielczość za pomocą szachownicy, a tę opcję na 2, końcowy wynik będzie miał detale zgodne z suwakiem rozdzielczości, a w karcie wielokrotnej rozdzielczości znajdzie się na poziomie 2, czyli poniżej będą siatki o niższej rozdzielczości na poziomach 1 i 0. To dobry sposób, by jednocześnie uzyskać czystą siatkę z równymi wielokątami i siatkę kontrolną o niższej rozdzielczości.

Przy wysokich rozdzielczościach działa też szybciej i zużywa mniej pamięci. Ale przy niskiej rozdzielczości i wielu poziomach stracisz detale.

::: tip Wskazówka: wielokrotna rozdzielczość i stabilne wygładzanie

Ta opcja czasem tworzy w geometrii „pętle”, które trudno wygładzić i które dają małe pryszcze. Jeśli tak się stanie, włącz „Stabilne wygładzanie” w opcjach narzędzia Gładkie. 

:::

### Pogrub cienkie części {#thicken-thin-parts}
Części cieńsze niż woksele mogą się podczas remeshu rozpaść lub zniknąć. Ta opcja je pogrubia, żeby przetrwały: wyższe wartości pogrubiają mocniej. Nie jest dostępna razem z `Ostre krawędzie` ani `Ostra granica`.

### Otwory {#voxel-holes}
Sposób zamykania otworów przed remeshem:

* `Wypełnij` - Każdy otwór jest zamykany osobno, od jego krawędzi.
* `Kształt` - Otwory są zamykane zgodnie z otaczającą powierzchnią, a nakładające się otwarte fragmenty zostają połączone.

### ![](/icons/angle.webp) Ostre krawędzie {#keep-sharp-edges}
Przyciąga nowe punkty do ostrych krawędzi oryginalnej siatki. Przydaje się głównie przy prostych operacjach boolean na prymitywach i może wprowadzić zniekształcenia.

### ![](/icons/group.webp) Ostra granica {#voxel-sharp-border}
Nowe ściany podążają za granicami grup powierzchni, a granica pozostaje ostra tam, gdzie powierzchnia się wzdłuż niej załamuje.

### ![](/icons/group_separate.webp) Zachowaj osobne grupy {#keep-groups-separate}
Każda grupa powierzchni jest przebudowywana osobno: grupy nigdy się nie łączą, a każda pozostaje zamkniętym kawałkiem we własnej grupie. W tym trybie wielokrotna rozdzielczość nie jest tworzona. Opcja jest dostępna, gdy obiekt ma kilka grup powierzchni.

## ![](/icons/dynamic.webp) Topologia dynamiczna {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Wielokrotna rozdzielczość i remesh wokselowy to powszechne w branży metody kontroli topologii, ale obie wymagają pilnowania, by nie rozciągać wielokątów za bardzo ani nie ściskać ich za mocno. 

Topologia dynamiczna to inne podejście. Podczas rzeźbienia Nomad na bieżąco dodaje i usuwa wielokąty w trakcie pociągnięcia pędzla: rzeźbienie drobnych detali dodaje wiele małych wielokątów tam, gdzie są potrzebne, a wygładzanie w innych miejscach je usuwa.

Pamiętaj, że topologia dynamiczna używa trójkątów, a nie czworokątów. Może to wyglądać nieco chaotycznie, ale najlepiej w ogóle nie patrzeć na szkielet: skup się na ładnej rzeźbie bez martwienia się o topologię, a później użyj jednego z innych narzędzi Nomada do przebudowy siatki, by uzyskać czystą siatkę z czworokątów.

Zobacz, jak to działa, na filmie poniżej.

![](/videos/dynamic.mp4)

### Włączona {#enabled}
Włącza topologię dynamiczną. Pod suwakami promienia i intensywności pędzla pojawi się ikona DynTopo, którą możesz włączać i wyłączać DynTopo osobno dla każdego narzędzia. Może to zauważalnie wpłynąć na wydajność, a warstwy są poprawnie aktualizowane.

### Szczegół {#dyn-detail}
Ustala poziom szczegółów; jego działanie zależy od wyboru w „Szczegóły oparte na...” (patrz niżej). W trybie `Ekran` etykieta pokazuje docelowy rozmiar trójkąta w pikselach. W trybie `Stała` zakraplacz pozwala pobrać szczegółowość z gęstości siatki w miejscu, które stukniesz.

### Szczegóły oparte na... {#detail-based-on}
| Metoda   | Opis                                                            |
| :------: | :-------------------------------------------------------------: |
| Ekran    | Poziom szczegółów zależy od tego, jak duży jest obiekt na ekranie. Suwak szczegółów na 100% lub więcej daje drobne detale i małe trójkąty, a na 1% mało detali i duże trójkąty.  |
| Promień  | Poziom szczegółów wyznacza promień narzędzia. Mały promień daje drobne detale, duży promień mniej detali. Suwak szczegółów jest mnożnikiem tej proporcji.                     |
| Stała    | Poziom szczegółów wyznacza suwak szczegółów i nie zależy od rozmiaru na ekranie ani od rozmiaru narzędzia. To ta sama wartość co suwak [Szczegół](#all-detail) w `Ponownie utwórz siatkę`.             |

::: tip WSKAZÓWKA: tryb Promień

Aby lepiej poczuć, jak działa tryb Promień, zacznij przesuwać suwak szczegółów jednym palcem, a jednocześnie zmieniaj promień narzędzia drugim. Zobaczysz, jak są ze sobą powiązane.

:::

### Preferuj... {#prefer}
| Metoda   | Opis                    |
| :------: | :---------------------: |
| Szybkość | Stawia na wydajność     |
| Jakość   | Stawia na jakość        |

Gdy wybierzesz `Jakość`, są 2 główne różnice:
- zagęszczanie siatki odbywa się przed rzeźbieniem, więc przy malowaniu lub rzeźbieniu bardzo drobnych detali pojawia się mniej artefaktów interpolacji,
- zagęszczanie trwa, aż siatka osiągnie właściwy poziom szczegółów, zamiast działać stopniowo.
 
Dzięki temu nawet przy bardzo drobnych detalach czy szybkich pociągnięciach topologia zawsze zostanie zagęszczona zgodnie z oczekiwaniami.


### ![](/icons/pressure.webp) Użyj nacisku dla promienia {#use-pressure-on-radius}
Ma znaczenie tylko w trybie `Promień`. Gdy jest włączona, poziom szczegółów zawsze odpowiada rozmiarowi pędzla, nawet gdy ten zmienia się pod wpływem nacisku rysika.

### Użyj zanikania pociągnięcia {#use-stroke-falloff}

Uwzględnia w obliczeniach DynTopo także krzywą zanikania i alfę pędzla.

### Metoda {#method}
Wybierz, jak topologia dynamiczna zmienia siatkę, zarówno podczas rzeźbienia, jak i przy użyciu [Ponownie utwórz siatkę](#dyn-remesh):

| Metoda         | Opis                                                                  |
| :------------: | :-------------------------------------------------------------------: |
| Uniformizacja  | Może dodawać i usuwać ściany; to tryb użyty na filmie powyżej          |
| Podział        | Tylko dodaje nowe ściany, nie może ich usuwać                         |
| Upraszczanie   | Tylko usuwa ściany, nie może dodawać nowych                           |

### ![](/icons/shield.webp) Chroń zamaskowany obszar {#protect-masked-area}
Zamaskowane obszary chronią topologię przed zmianami.

### ![](/icons/normal.webp) Ekstrapolacja wierzchołków {#vertex-extrapolation}
Umieszcza punkty na gładkiej powierzchni, która podąża za krzywizną wokół nich, zamiast płasko na istniejących ścianach.

### Szczegół {#all-detail}
Rozdzielczość używana przy przebudowie siatki. Jeśli DynTopo działa w trybie „Stała”, będzie to ta sama wartość co suwak Szczegół na górze tego menu. Zakraplacz pobiera szczegółowość z gęstości siatki w miejscu, które stukniesz.

### Ponownie utwórz siatkę {#dyn-remesh}
Przebudowuje całą siatkę algorytmem DynTopo. Zwykle do pełnej przebudowy lepiej użyć [remeshu wokselowego](#voxel-remesher).

Ta metoda ma jednak nad wokselami przewagę: siatka nie musi być zamknięta, a zamaskowany obszar jest chroniony, więc lepiej kontrolujesz, gdzie ma być większa, a gdzie mniejsza gęstość.



## ![](/icons/topo_extra.webp) Różne {#misc}

![](/images/topology_misc_menu.webp)

Ta karta zbiera narzędzia do porządkowania lub konwersji siatki: zamykania otworów, wymuszania manifold i zamiany obiektu na trzypłaszczyznowy.

### ![](/icons/hole.webp) Otwory {#holes}
![](/images/topology_holes_menu.webp)
Najczęściej obiekt będzie szczelny, czyli siatka będzie „zamknięta”.

Jeśli obiekt ma otwory, możesz je wypełnić.

![](/videos/hole_filling.mp4)

::: tip
Remesh wokselowy automatycznie zamyka wszystkie otwory, niezależnie od tego, czy używasz go na 1, czy na wielu siatkach.
:::

#### Zamknij otwory {#close-holes}
Zamyka otwory.

#### Opcje {#holes-gear-menu}
Te opcje zmieniają sposób wypełniania otworów:

##### Grupa powierzchni {#fill-face-group}
Wybierz grupę powierzchni dla nowych ścian:

* `Mieszany` - Otwór otoczony jedną grupą powierzchni dostaje tę samą grupę, a otwór stykający się z kilkoma grupami dostaje nową.
* `Nowy` - Wypełnione otwory dostają nową grupę powierzchni.
* `Użyj ponownie` - Każdy otwór dostaje grupę powierzchni, która otacza go w największym stopniu.

##### Szczegół {#fill-detail}
Gęstość wielokątów użyta do wypełnienia otworu. Podczas przesuwania suwaka na modelu pojawia się szachownica, która pokazuje rozmiar trójkątów. Pole wyboru wyłącza tę opcję i używa tylko istniejących punktów, co zwykle tworzy nad otworem długie, cienkie trójkąty, trudne do rzeźbienia.

##### Mostek {#fill-non-manifold}
Wypełnia otwór razem z wyspami w jego środku jako jedną powierzchnię, zamiast wypełniać każdą krawędź osobno. Większy kąt pozwala połączyć mostkiem bardziej zakrzywione otwory. Pole wyboru wyłącza tę opcję.

### ![](/icons/cog.webp) Wymuś manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Próbuje naprawić krawędzie non-manifold. Przydaje się przy programach zewnętrznych, które nie obsługują krawędzi wspólnych dla więcej niż 2 ścian.

#### Oczyść {#clean}
Wykonuje oczyszczanie.

#### Opcje {#force-manifold-gear-menu}
Ta opcja zmienia sposób oczyszczania siatki:

##### Usuń małe ściany {#delete-small-faces}
Próg, poniżej którego małe wielokąty są usuwane i scalane. Włączasz go polem wyboru.


### ![](/icons/triplanar.webp) Trzypłaszczyznowy {#triplanar}
![](/images/topology_triplanar_menu.webp)
Zamienia siatkę na prymityw [trzypłaszczyznowy](scene.md#triplanar).
Prawdopodobnie stracisz przy tym sporo detali: warstwy, malowanie i wielokrotna rozdzielczość również zostaną utracone.

#### Wymuś formę sześcienną {#force-cubic}
Sprawia, że obiekt trzypłaszczyznowy jest sześcianem. W przeciwnym razie dopasowuje się do najbliższego prostopadłościanu otaczającego obiekt.

#### Konwertuj {#convert}
Wykonuje konwersję na obiekt trzypłaszczyznowy.

#### Rozdzielczość {#triplanar-resolution}
Rozdzielczość siatki trzypłaszczyznowej: wyższe wartości zachowują więcej detali.

## ![](/icons/decimate.webp) Uprość {#decimation}

![](/images/topology_decimation.webp)

Zmniejsza liczbę wielokątów, starając się zachować jak najwięcej detali, i używa przy tym trójkątów.

Przydaje się na przykład przy eksporcie do druku 3d.
Raczej nie używaj tej funkcji, jeśli chcesz dalej rzeźbić, bo może tworzyć nierówne trójkąty.

Zamaskowane obszary nie zostaną uproszczone.

![](/videos/decimate.mp4)

::: tip

Narzędzie [Quad Remesher](tools.md#quad-remesher) na obiektach z dużą liczbą wielokątów może liczyć bardzo długo i dawać trudne do kontrolowania wyniki. Przygotowanie siatki za pomocą [grup powierzchni](tools.md#facegroup) i upraszczania sprawi, że Quad Remesher zadziała znacznie szybciej, a ty zyskasz dużo większą kontrolę nad topologią.

* Podziel siatkę na grupy powierzchni, wyznaczając idealny przebieg czworokątów.
* Złagodź grupy powierzchni, by uzyskać gładkie granice grup.
* Uprość siatkę. Dzięki temu na granicach grup nie będzie cienkich ani zniekształconych ścian. W sekcji `Zachowaj granicę` upewnij się, że `Grupa powierzchni` jest włączona. Krawędzie trójkątów będą wtedy dokładnie podążać za granicami grup powierzchni.
* W opcjach Quad Remesher upewnij się, że łagodzenie jest wyłączone (bo siatka jest już złagodzona), a wyniki powinny być dobre.

:::

### Uprość {#decimate}
Rozpoczyna upraszczanie.

Ikony obok przycisku upraszczania pokazują poniższe opcje i pozwalają je włączać i wyłączać. Procent oznacza siłę danej opcji.

* ![](/icons/palette.webp)  `Zachowaj malowanie` - Umieszcza więcej trójkątów tam, gdzie są detale malowania.
* ![](/icons/triforce.webp) `Jednolite powierzchnie` - Preferuje trójkąty o równym rozmiarze.
* ![](/icons/hole.webp)  `Otwór` - Upraszczanie stara się nie zmieniać krawędzi przy otwartej geometrii i otworach.
* ![](/icons/group.webp) `Grupa powierzchni` - Upraszczanie stara się nie zmieniać granic grup powierzchni.
* ![](/icons/uv.webp) `UV` - Upraszczanie stara się nie zmieniać granic UV.

### Docelowe trójkąty {#target-triangles}
Ustala docelową liczbę trójkątów. Domyślnie to 50%; przycisk procent/cel przełącza między wartością procentową a dokładną docelową liczbą wielokątów.

### Opcje {#decimate-gear-menu}
Każda opcja ma pole wyboru do jej włączania i wartość określającą jej siłę:

#### ![](/icons/palette.webp) Zachowaj malowanie {#preserve-painting}
Wartość określa, jak dokładnie zostaną zachowane detale malowania. Wyższe wartości zachowują więcej malowania. Ustaw 0, jeśli malowanie nie ma dla ciebie znaczenia.

#### ![](/icons/triforce.webp) Jednolite powierzchnie {#uniform-faces}
Wyższe wartości dają trójkąty o podobnym rozmiarze.

#### Zachowaj granicę {#preserve-borders}
Chroni krawędzie przed upraszczaniem. Wagi krawędzi można ustawić dla granic `Otwór`, `Grupa powierzchni` lub `UV` (`UV` wymaga obiektu z UV).

## ![](/icons/quad.webp) Przebudowa na czworokąty {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Odbudowuje obiekt z czystym układem czworokątów. Ta karta ma kilka algorytmów przebudowy, każdy z własnym przyciskiem `Ponownie utwórz siatkę`, suwakiem `Docelowe czworokąty` i menu z kołem zębatym. Wypróbuj je na swoim obiekcie, bo dają dość różne wyniki!

### Quad Remesher {#quad-remesher}
Ten sam algorytm co narzędzie [Quad Remesher](tools.md#quad-remesher), opracowany przez [Exoside](https://exoside.com/). Jest dostępny tylko na niektórych platformach i wymaga zakupu: do tego czasu przycisk `Ponownie utwórz siatkę` pokazuje koszyk.

`Wybierz narzędzie` przełącza na narzędzie Quad Remesher, w którym rysujesz prowadnice i malujesz gęstość. W menu z kołem zębatym są `Adaptacyjna liczba czworoboków`, `Adaptacyjny rozmiar` (przy 100% rozmiar czworokątów podąża za krzywizną, przy 0% czworokąty są jednolite), `Wykryj twarde krawędzie` i `Reprojekcja wierzchołka`.

::: tip
Tam, gdzie jest dostępny, Quad Remesher zwykle daje najlepsze wyniki i największą kontrolę.
:::

### AutoRemesher {#autoremesher}
Alternatywny algorytm przebudowy na czworokąty, z opcjami dopasowania rozmiaru i kształtu czworokątów do powierzchni.

#### ![](/icons/cog.webp) Menu z kołem zębatym AutoRemesher {#autoremesher-gear-menu}
Menu z kołem zębatym zawiera te zaawansowane opcje:

##### Skalowanie krawędzi {#edge-scaling}
Skaluje rozmiar czworokątów: wyższe wartości dają większe czworokąty.

##### Adaptacyjność {#adaptivity}
Dopasowuje gęstość czworokątów do krzywizny. 0 daje jednolite czworokąty, 1 daje mniejsze czworokąty w zakrzywionych miejscach.

##### Anizotropia {#anisotropy}
Rozciąga czworokąty wzdłuż najbardziej płaskiego kierunku powierzchni. 0 daje kwadratowe czworokąty, 1 daje wydłużone czworokąty na rurach i grzbietach.

##### Ostra krawędź {#sharp-edge}
Krawędzie zgięte bardziej niż ten kąt są zachowywane jako ostre.

##### Wygładzanie normalnych {#smooth-normal}
0 zachowuje fasetowaną powierzchnię podczas przebudowy. Wyższe wartości wygładzają powierzchnię, uwzględniając normalne wierzchołków.

##### Maksymalne wypełnienie otworu {#autoremesher-max-fill-hole}
Algorytm czasem tworzy niechciane otwory. Jeśli otwór ma mniej wierzchołków niż ta wartość, zostanie wypełniony.

### Instant Mesh {#quad-remesh-instant}
Przebudowuje siatkę [algorytmem Instant Meshes autorstwa Wenzela Jakoba, Marca Tariniego, Daniele Panozzo i Olgi Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analizuje przebieg siatki i tworzy czystą topologię z czworokątów.

#### Ponownie utwórz siatkę {#instant-remesh}
Rozpoczyna przebudowę siatki.

#### Docelowe czworokąty {#target-quads}
Liczba czworokątów, którą algorytm spróbuje utworzyć.

#### ![](/icons/cog.webp) Menu z kołem zębatym Instant Mesh {#quad-remesh-instant-gear-menu}
Menu z kołem zębatym zawiera te zaawansowane opcje:

##### Kąt zagięcia {#crease-angle}
Próg ostrych narożników, które pomagają pokierować przebudową. Włączasz go polem wyboru.

##### Maksymalne wypełnienie otworu {#max-fill-hole}
Algorytm czasem tworzy niechciane otwory. Jeśli otwór ma mniej wierzchołków niż ta wartość, zostanie wypełniony.

### QuadriFlow {#quadriflow}
Przebudowuje siatkę algorytmem QuadriFlow, kolejnym sposobem na czysty układ czworokątów.

#### ![](/icons/cog.webp) Menu z kołem zębatym QuadriFlow {#quadriflow-gear-menu}
Menu z kołem zębatym zawiera te zaawansowane opcje:

##### Zachowaj granicę {#quadriflow-preserve-boundary}
Chroni krawędzie otworów.

##### Zachowaj ostre krawędzie {#keep-sharp}
Wyrównuje czworokąty z ostrymi krawędziami powierzchni.

##### Przepływ minimalnego kosztu {#min-cost-flow}
Używa solwera przepływu o minimalnym koszcie do ułożenia czworokątów. Działa wolniej, ale może dać bardziej regularną topologię.

## ![](/icons/uv.webp) Rozwijanie UV {#uv-unwrap}
Oblicza współrzędne tekstury (UV) dla zaznaczonego obiektu. Nomad ma dwie metody, `UVAtlas` i `BFF`, każdą z własnym przyciskiem `Rozwiń`.

![](/videos/unwrap.mp4)

::: tip UV?
UV często porównuje się do pakowania prezentu: jak najlepiej pociąć papier, by całkowicie okrył przedmiot, bez zakładek? 

UV działają podobnie, tylko zamiast papieru tniesz obiekt. Wyobraź sobie, że model jest z cienkiego plastiku: jak go pociąć, by rozłożyć go płasko, pomalować w tym płaskim stanie, a potem złożyć z powrotem?

Teraz wyobraź sobie, że powierzchnia modelu jest z rozciągliwej lycry. Możesz ją rozciągnąć na płasko, pociąć albo połączyć oba sposoby. Ale jeśli na rozłożonym obiekcie namalujesz szachownicę, po złożeniu będzie zniekształcona. Co lepsze: więcej cięć i mniej zniekształceń, czy mniej cięć i więcej zniekształceń?

UV to instrukcje, które mówią programowi 3d, jak „pociąć i rozciągnąć” obiekt przy nakładaniu tekstur. UV Atlas zwykle stawia na „więcej cięć, mniej zniekształceń”.


:::

::: tip UV w Nomadzie i innych aplikacjach

Większość teksturowanych modeli, które znajdziesz w sieci, ma tekstury nałożone przez UV. Nomad potrafi je zaimportować i wyświetlić w panelu [materiału](material.md#textures).

Modele tworzone w Nomadzie możesz malować bezpośrednio, bez UV. Jeśli chcesz je wyeksportować do innych aplikacji, np. [Procreate](https://procreate.art/), możesz „wypalić” informacje o kolorze z Nomada do tekstur przez UV. 

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas zwykle woli tworzyć więcej wysp przez cięcia, by zminimalizować zniekształcenia.

#### Rozwiń {#unwrap}
Oblicza UV dla zaznaczonego obiektu.

#### Opcje {#uvatlas-gear-menu}
Przyciski obok `Rozwiń`:

##### Grupa powierzchni {#atlas-face-group}
Gdy pokazuje `Tak`, cięcia UV wyznaczają grupy powierzchni. To ustawienie jest wspólne z BFF.

##### Usuń UV {#delete-uvs}
Przycisk kosza usuwa UV obiektu.

##### Inspekcja {#uv-inspect}
Pokazuje UV obiektu w tle.

#### Maks. rozciągnięcie {#max-stretch}
Niskie wartości dają mniej zniekształceń i więcej wysp, wysokie wartości więcej zniekształceń i mniej wysp. 

#### Odstęp między wyspami {#island-spacing}
Margines między wyspami. Niskie wartości marnują mniej miejsca, ale grożą przenikaniem tekstur między wyspami. 

::: warning
Obliczanie UV może chwilę potrwać: najlepiej, by siatka miała mniej niż 100 tys. wierzchołków.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV z BFF stawiają na „mniej cięć, więcej zniekształceń”. 

#### Opcje {#uv-bff-gear-menu}
Obok `Rozwiń` znajdują się te same przyciski `Grupa powierzchni`, usuwania i `Inspekcja` co w [UVAtlas](#uvatlas-gear-menu).

##### Grupa powierzchni {#bff-face-group}

Używa grup powierzchni do wyznaczenia cięć UV.

#### Liczba stożków {#cone-count}
Określa liczbę głównych rzutowań. Niższe wartości dają mniej wysp, ale więcej zniekształceń. Wyższe wartości dłużej się liczą.

#### Szwy niewidoczne {#seamless-patches}
Wpływa na układ fragmentów UV i może wprowadzić duże zniekształcenia. Działa najlepiej ze starannie przygotowanymi grupami powierzchni.

::: warning
BFF może tworzyć nakładające się UV, jeśli siatka ma uchwyty (jak otwór w pączku).
:::

### ![](/icons/preview.webp) Pokaż UV po rozpakowaniu {#show-uv-after-unwrap}
Po rozwinięciu otwiera widok inspekcji UV, żebyś od razu mógł sprawdzić wynik.

### ![](/icons/bake.webp) Zastosuj: Tekstura → Tekstura {#unwrap-bake-texture}
Dostępne tylko wtedy, gdy materiał obiektu ma tekstury. Gdy ponownie rozwiniesz UV, tekstury zostaną przeniesione na nowe UV, więc nadal będą pasować. Rozdzielczość domyślnie ma wartość `Auto`, czyli odpowiada największej teksturze, ale możesz ją ustawić samodzielnie.

## ![](/icons/bake.webp) Zastosuj {#bake}
Ta karta przenosi (wypala) detale i malowanie między obiektami oraz między wierzchołkami a teksturami.

`Od wysokiej rozdzielczości` używa innych obiektów jako źródła; liczba w nawiasie mówi, ilu. Nomad wybiera je tak:

- używane są wszystkie zaznaczone obiekty, a celem jest główny zaznaczony obiekt (najmocniej podświetlony w menu [Scena](scene.md))
- jeśli zaznaczony jest tylko jeden obiekt, Nomad używa zamiast tego wszystkich widocznych obiektów
- jeśli wszystkie inne obiekty są ukryte (na przykład przez Solo), używana jest cała scena

### ![](/icons/bake.webp) Zastosuj → Tekstura {#bake-texture}
![](/images/topology_bake_menu.webp)

Wypalanie tekstur tworzy tekstury, rzutując inne widoczne obiekty sceny na UV zaznaczonego obiektu. Obiekt musi mieć UV.

Typowy przebieg wypalania:
- Masz siatkę z drobnymi detalami i malowaniem
- Sklonuj ją
- Uprość ją (ustaw `Zachowaj malowanie` na 0)
- Rozwiń UV
- Wypal!

Otrzymasz siatkę o niskiej rozdzielczości, która zachowuje większość malowania i detali poprzedniego obiektu.

Po operacji kolory wierzchołków zostaną przeniesione na nową, wyłączoną warstwę, by nie kolidowały z teksturami.

#### Od samego siebie {#tex-from-itself}
Wypala obiekt na jego własne UV: malowanie staje się teksturami, a jeśli obiekt ma poziomy wielokrotnej rozdzielczości, detale najwyższego poziomu są wypalane na bieżący (na przycisku pojawia się wtedy ikona multires). Łatwo to przygotować, ale często potrzebujesz większej kontroli i wtedy bardziej przyda się następna opcja.

#### Od wysokiej rozdzielczości {#tex-from-high-res}
Wypala inne obiekty na zaznaczony obiekt. Liczba w nawiasie mówi, ile innych obiektów posłuży jako źródła o wysokiej rozdzielczości, wypalane na bieżący obiekt o niskiej rozdzielczości z UV. Inne obiekty nie muszą mieć podobnego układu ani topologii co wypalany obiekt, co daje dużą swobodę.

#### Rozdzielczość {#tex-bake-resolution}
Rozdzielczość wypalonej tekstury. Wypalane tekstury są zawsze kwadratowe, więc 1024 daje obraz 1024x1024. 

Przyciski poniżej to skróty do często używanych rozdzielczości. Dla porównania: 512x512 to stosunkowo mało, np. do grafiki na stronę i prostej geometrii, a 4096x4096 (w skrócie 4k) nadaje się do renderów wysokiej jakości.

#### Kolor, Chropowatość, Metaliczność, Normalna, Przemieszczenie, Emisyjne, Krycie {#tex-normal-roughness-metalness-color-emissive-opacity}
Te przyciski określają, które właściwości zostaną wypalone, każda do osobnej mapy. Po wypaleniu zostaną dodane jako tekstury do materiału bieżącego obiektu. `Przemieszczenie` wypala wysokość detali jako mapę przemieszczenia.

#### ![](/icons/cog.webp) Menu z kołem zębatym wypalania {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Menu z kołem zębatym zawiera te zaawansowane opcje:

##### Kopia zapasowa {#tex-backup}
Aby zobaczyć podgląd wypalonych tekstur, malowanie obiektu musi być wyłączone. `Kopia zapasowa (Malarskie → Warstwa)` przenosi malowanie na nową warstwę jako kopię zapasową, którą łatwo włączyć lub wyłączyć.

##### Użyj multires {#tex-use-multires}
Dla `Od samego siebie` na obiekcie z poziomami wielokrotnej rozdzielczości. Nomad odczytuje wysoką rozdzielczość przez poziomy podziału zamiast rzucać promienie: to szybsze i wolne od błędów rzutowania. Wyłącz tę opcję, aby wypalać z użyciem poniższych opcji.

##### Gładka baza {#tex-smooth-base}
Dla `Przemieszczenie` na obiekcie z poziomami wielokrotnej rozdzielczości. Mierzy przemieszczenie od podzielonej bazy zamiast od jej płaskich ścian. Zostaw ją włączoną, gdy mapa przemieszczenia trafi na dzieloną siatkę, jak przy adaptacyjnym podziale w Blenderze.

##### Szukaj na odległość {#tex-cage-radius}
Maksymalna odległość, w jakiej szukana jest powierzchnia źródłowa. Domyślnie jest mała, by uniknąć artefaktów, ale można ją zwiększyć, jeśli obiekty źródłowe są daleko od wypalanego obiektu.

##### Projekcja {#tex-projection}
Sposób znajdowania powierzchni źródłowej:

* `Promień` - Rzutuje wzdłuż normalnej powierzchni.
* `Promień + najbliższy` - Używa promienia wzdłuż normalnej, a gdy nie trafi, najbliższej powierzchni.
* `Najbliższy` - Rzutuje na najbliższy punkt powierzchni źródłowej.

##### Przesunięcie promienia {#tex-ray-offset}
Określa, skąd na wypalanym obiekcie zaczynają się obliczenia. Niewielkie odsunięcie od powierzchni eliminuje najczęstsze artefakty. Jeśli obiekty źródłowe są bardzo daleko od wypalanego obiektu, może trzeba będzie je zwiększyć. Nie jest używane przez `Najbliższy`.


### ![](/icons/bake.webp) Rzutowanie → Wierzchołek {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Rzutuje wyrzeźbione detale, malowanie, warstwy i tekstury na wartości wierzchołków.

Można to traktować jako odwrotność wypalania: wypalanie przenosi właściwości wierzchołków do tekstur, a rzutowanie przenosi tekstury (i inne właściwości)
 z powrotem do wierzchołków.

::: tip
Przy `Zastosuj → Tekstura` i `Rzutowanie → Wierzchołek` brane są pod uwagę zarówno kolory wierzchołków, jak i tekstury materiału.
:::

#### Od samego siebie {#vertex-from-itself}
Zamienia tekstury materiału na wartości wierzchołków. Ten przycisk jest aktywny tylko wtedy, gdy obiekt ma UV, a tekstury w materiale są włączone.

::: tip WSKAZÓWKA: malowanie tekstur
Nomad nie pozwala bezpośrednio malować i edytować tekstur, ale bardzo podobny efekt uzyskasz, rzutując tekstury na wartości wierzchołków, malując po wierzchołkach, a potem wypalając wierzchołki z powrotem do tekstur:

1. Przygotuj obiekt o małej liczbie wielokątów z UV
1. Wczytaj tekstury do jego materiału
1. Podziel go na tyle, by dało się po nim malować
1. Użyj `Rzutowanie → Wierzchołek` w trybie `Od samego siebie`: tekstura zamienia się w wartości wierzchołków
1. Maluj, wygładzaj, rozmazuj, stempluj, rób wszystkie potrzebne zmiany
1. Użyj `Zastosuj → Tekstura` w trybie `Od samego siebie`. Zmiany wracają do tekstur.
:::

#### Od wysokiej rozdzielczości {#vertex-from-high-res}
Zamienia inne obiekty na wartości wierzchołków zaznaczonego obiektu. Liczba na przycisku mówi, ile jest obiektów źródłowych. Przeznaczone głównie do użycia także na siatce o wysokiej rozdzielczości, zwykle z czystą topologią.

::: tip
Rzutowanie innych obiektów służy nie tylko do przenoszenia koloru, ale też do rzutowania wierzchołków na inne obiekty, np. bandaże można rzutować na postać.
:::

#### Wierzchołki, Kolor, Chropowatość, Metaliczność, Krycie, Maska, Warstwy, Grupa powierzchni {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Te przyciski określają, które właściwości zostaną rzutowane na zaznaczony obiekt. `Warstwy` przenosi pozostałe warstwy na zaznaczoną siatkę.

#### ![](/icons/cog.webp) Menu z kołem zębatym rzutowania {#vertex-reproject-gear-menu}
Menu z kołem zębatym zawiera te zaawansowane opcje:

##### Krycie → Maska {#vertex-opacity-to-mask}
Zamienia krycie źródła na maskę na zaznaczonym obiekcie.

##### Iteracje {#vertex-iterations}
Ile razy podczas rzutowania ma zostać zastosowane łagodzenie. Używane tylko wtedy, gdy `Wierzchołki` są włączone.

##### Złagodź {#vertex-relax}
Układ zaznaczonej siatki może zostać w pewnym stopniu wygładzony lub złagodzony, by lepiej dopasować się do obiektów źródłowych. `Gładkie` sprawdza się lepiej na siatkach z dużą liczbą wielokątów, `Złagodź` na siatkach z małą liczbą wielokątów. `Auto` pozwala Nomadowi wybrać najlepszą metodę.

##### Szukaj na odległość {#vertex-cage-radius}
Maksymalna odległość, w jakiej szukana jest powierzchnia źródłowa. Domyślnie jest mała, by uniknąć artefaktów, ale można ją zwiększyć, jeśli obiekty źródłowe są daleko od zaznaczonego obiektu.

##### Projekcja {#vertex-projection}
Sposób znajdowania powierzchni źródłowej:

* `Promień` - Rzutuje wzdłuż normalnej powierzchni.
* `Mieszanka adaptacyjna` - Miesza wynik promienia wzdłuż normalnej i najbliższej powierzchni w zależności od odległości i `Preferencja promienia`. Gdy jeden nie trafi, używa drugiego.
* `Najbliższy` - Rzutuje na najbliższy punkt powierzchni źródłowej.

##### Preferencja promienia {#vertex-ray-bias}
Tylko dla `Mieszanka adaptacyjna`. Wyższe wartości przesuwają mieszankę w stronę wyniku promienia wzdłuż normalnej, niższe w stronę najbliższego punktu.

##### Przesunięcie promienia {#ray-vertex-offset}
Określa, skąd na zaznaczonym obiekcie zaczynają się obliczenia. Niewielkie odsunięcie od powierzchni eliminuje niektóre artefakty. Jeśli obiekty źródłowe są bardzo daleko od wypalanego obiektu, może trzeba będzie je zwiększyć. Nie jest używane przez `Najbliższy`.

### ![](/icons/bake.webp) Zastosuj → VDM {#bake-vdm}
Tworzy stempel VDM (wektorowej mapy przemieszczeń) z zaznaczonego obiektu i dodaje go do biblioteki VDM. Nomad zapyta o nazwę.

Typowy przebieg pracy:
- Dodaj płaszczyznę albo wybierz `Nowy VDM` w selektorze VDM, aby dodać gotowo skonfigurowaną (prymityw [VDM](scene.md#add-menu))
- Wyrzeźb na niej kształt, zostawiając płaską krawędź
- Wypal!

UV płaszczyzny wyznaczają kwadrat, który zostanie wypalony, więc obiekt musi mieć UV. Rozmiar stempla wybierasz w `Rozdzielczość`, a przyciskami `Kolor`, `Chropowatość`, `Metaliczność` i `Krycie` decydujesz, co oprócz przemieszczenia zawiera stempel.

::: tip
Nie używaj DynTopo na płaszczyźnie: psuje jej UV i stempel wychodzi zniekształcony. Najdokładniejszy wynik daje rzeźbienie na warstwie, bo płaska płaszczyzna wciąż jest pod spodem. Malowanie też wymaga warstwy, inaczej materiał zostanie odciśnięty na całym kwadracie, a nie tylko tam, gdzie malowałeś.
:::

## ![](/icons/dot.webp) Prymityw {#primitive}
Parametry zaznaczonego prymitywu. Większość z nich jest też dostępna pod przyciskiem `…` na pasku narzędzi prymitywu w widoku.

![](/images/topology_primitive_screenshot.webp)
