# ![](/icons/pencil.webp) Pociągnięcie    

---
![](/images/stroke_overview.webp) 

## Przegląd 

Możesz dostosować zachowanie pociągnięcia dla większości narzędzi–pędzli.
Ustawienia są podobne do tych znanych z 2D‑owych aplikacji malarskich, jednak część opcji jest specyficzna dla rzeźbienia i 3D.

Opcje są podzielone na 5 pod‑menu:

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Kontroluje sposób nakładania pociągnięcia na model                |
| Alpha    | ![](/icons/alpha.webp)      | Określa, jak skala szarości tekstury jest używana w odcisku pędzla |
| Falloff  | ![](/icons/falloff.webp)    | Kontroluje zmianę siły pędzla od środka do krawędzi               |
| Filter   | ![](/icons/filter.webp)     | Określa, jak pędzel reaguje na geometrię modelu                   |
| Pressure | ![](/icons/pressure.webp)   | Kontroluje reakcję na nacisk rysika                               |

::: tip
Nie wszystkie opcje pociągnięcia mają zastosowanie do wszystkich narzędzi. Opcje, których bieżące narzędzie nie używa, będą wyłączone lub ukryte. 
:::


## Stroke

### Radius

![](/images/stroke_radius.webp)

#### Share radius

Po włączeniu wszystkie narzędzia używają tego samego promienia; domyślnie każde narzędzie ma własny promień.

#### Size

* Screen – promień jest ustawiany w jednostkach ekranu. Jeśli ustawisz promień na 100 pikseli, pozostanie on szeroki na 100 pikseli niezależnie od przybliżenia lub oddalenia.
* Constant (3d) – promień jest ustawiany w jednostkach 3D. Na przykład, jeśli utworzysz sferę i ustawisz promień na jej rozmiar, promień pozostanie tej samej wielkości co sfera podczas przybliżania i oddalania.


### Stroke

![](/images/stroke_strokemode.webp)

Pociągnięcia mogą działać w kilku trybach:

### ![](/icons/stroke_dot.webp) Dot
Przeciągaj jak zwykłe pociągnięcie malarskie. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
Alfa pędzla będzie obracana, aby podążać za kierunkiem pociągnięcia, co jest przydatne do tworzenia np. ściegów materiału. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
 Odcisk pędzla z ustaloną **_wysokością_**. Przeciąganie ustawia skalę i obrót.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Odcisk pędzla z ustalonym **_promieniem_**. Przeciąganie ustawia wysokość i obrót.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Narzędzia `Move` i `Drag` mają własne 3 opcje:

### ![](/icons/snake.webp) Drag

Podczas pociągnięcia cały czas aktualizuje to, co znajduje się w promieniu pędzla. Szybkie pociągnięcie zostawi powierzchnię w tyle, natomiast wolne będzie „trzymać się” materiału, tworząc dłuższe kształty. To domyślny tryb narzędzia `Drag`. Z włączoną `Dynamic Topology` można w ten sposób tworzyć wężowate ekstruzje. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Zaznacza to, co znajduje się w promieniu pędzla w momencie rozpoczęcia pociągnięcia i utrzymuje to zaznaczenie. Jest to przydatne do bardziej precyzyjnych przesunięć, ponieważ możesz dokładnie regulować odległość ruchu i nie przesuniesz przypadkowo więcej, niż pierwotnie zaznaczyłeś. To domyślny tryb narzędzia `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
Ustawiony przez użytkownika promień jest ignorowany i dynamicznie wyznaczany na podstawie odległości przeciągnięcia od punktu startowego. Mała odległość = mały promień, większa odległość = większy promień. Użyj suwaka intensywności, aby kontrolować kształt wygaszania (falloff). Przydatne do blokowania organicznych, gumowatych kształtów.
![](/videos/stroke_lockradius_drag.mp4) 



### Adjust spacing intensity
![](/images/stroke_space_smooth.webp)

Pociągnięcia z małym odstępem (mniejszym niż 50%) mogą szybko się kumulować, dając intensywniejszy efekt niż przy większych odstępach. Ten przełącznik kompensuje to, aby pociągnięcia miały zbliżoną intensywność niezależnie od odstępu.

### Stroke spacing
Jak daleko od siebie nakładać kolejne odciski pędzla podczas przeciągania. Wartości poniżej 100% powodują nakładanie się, dając wrażenie ciągłego pociągnięcia. Wartości powyżej 100% zaczną zostawiać przerwy, co jest przydatne np. do rzeźbienia detali takich jak szwy czy zamki błyskawiczne.

### Lazy rope stabilizer
Pociągnięcia będą opóźnione względem pozycji wskaźnika o określoną odległość. Można tego użyć do rysowania gładkich linii.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke smoothing
Uśrednia wiele pozycji wskaźnika, aby uzyskać gładsze pociągnięcie.
Przy wysokich wartościach pociągnięcie będzie opóźnione względem wskaźnika, ale ostatecznie go dogoni.
Przydatne do rysowania gładkich linii.

### Snap radius
Przyciąga początek pociągnięcia do końca poprzedniego. Promień określa, jak daleko szukać końca poprzedniego pociągnięcia. Może to być przydatne przy rysowaniu długich, ciągłych linii z częstymi przerwami.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Domyślnie pociągnięcia wpływają tylko na powierzchnię modelu w obrębie promienia pędzla. Po włączeniu silhouette pociągnięcie będzie rzutowane przez cały model. Może to być bardzo użyteczne przy wstępnym blokowaniu modelu lub dla kształtów, w których boki muszą pozostać prostopadłe.

Kierunek projekcji można ustawić ręcznie; domyślna metoda „Closest” wykryje najlepszy kąt względem widoku. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

Intensywność, przesunięcie, obrót i skala pociągnięcia mogą być losowane niezależnie. Można w ten sposób tworzyć różne efekty, np. losowanie z narzędziem paint może dać nakrapiane kolory, a z narzędziem crease – detale skóry.

![](/videos/stroke_randomize.mp4) 

### Stroke Offset

Nakłada stałe przesunięcie na pociągnięcie. Jest to przydatne na małych ekranach, gdzie palec zasłaniałby pociągnięcie. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

`Alpha` to tekstura modulująca zachowanie pędzla.
To obraz w skali szarości, gdzie czarne piksele oznaczają brak deformacji, a białe – pełną deformację.

Kliknij obraz alfa, aby go zmienić.

Kliknij podgląd materiału, aby wczytać alfę z presetu materiału. Możesz też zapisywać tu presety materiałów i zdecydować, czy osadzać tekstury w narzędziu.

::: tip
Tekstura nigdy nie jest zmieniana rozmiarem, więc duże tekstury mogą spowalniać działanie.
:::

### Invert pixels
Odwraca wartości obrazu, tak że czarne piksele stają się białe, a białe – czarne.

::: tip

Wbudowane alfy dostarczane z Nomad nie mogą być odwracane.

:::

### Scaling

Rozmiar pędzla w Nomad to okrąg o promieniu zdefiniowanym przez użytkownika. Tekstury są często kwadratowe lub prostokątne; parametry `Scaling` pozwalają zdecydować, jak tekstura ma się mieścić w tym okręgu. Dla kwadratowej tekstury wartość 0.7 sprawi, że zmieści się ona w okręgu. Wartość 1 powiększy teksturę tak, aby okrąg mieścił się w jej wnętrzu, przycinając krawędzie.

![](/images/alpha_scaling.webp) 

Włączenie `Scaling - Y` pozwala rozciągać alfę w pionie.

![](/images/alpha_scaling_y.webp) 

### Rotation

Tekstura alfa będzie obracana, aby podążać za kierunkiem pociągnięcia. Możesz dodać offset obrotu, a jeśli ikona kłódki jest włączona, tekstura pozostanie zablokowana w tym obrocie względem ekranu.

### Tiling
![](/images/stroke_tiling.webp) 

Jak często tekstura powtarza się w profilu pędzla. Tryby tilingu pozwalają ograniczyć się do pojedynczej tekstury w pociągnięciu, powtarzanych tekstur lub odbijanych lustrzanie, gdzie co druga tekstura jest odwrócona, aby tworzyć wzory lub pomagać w uzyskaniu bezszwowych tekstur.

![](/videos/alpha_tiling.mp4) 



### Mid value

Domyślnie czarne piksele oznaczają brak deformacji, a białe – pełną dodatnią deformację, więc np. pędzel clay z teksturą alfa skał będzie wyciągał powierzchnię tylko tam, gdzie alfa nie jest czarna.

Jeśli chcesz, aby pędzel wciskał powierzchnię do środka lub jednocześnie wciskał i wyciągał, możesz zmodyfikować wartość środkową. Jeśli ustawisz ją na 0.5, średnia szarość w alfie nie zrobi nic, czerń będzie wciskać, a biel – wyciągać.




## Falloff

![](/images/falloff_menu.webp) 

Działa podobnie jak [Alpha](#alpha), z tą różnicą, że intensywność jest sterowana pojedynczą krzywą. Jest ona łączona z alfą, dzięki czemu możesz użyć tekstury do detalu, a falloff do kontrolowania wygaszania krawędzi i intensywności w centrum narzędzia.

Gdy krzywa jest na górze, oznacza to pełną deformację; gdy na dole – pędzel nie ma efektu.

Możesz myśleć o krzywej jak o przekroju przez czubek pędzla. Dolna część pokazuje podgląd pojedynczego „odcisku” pędzla na powierzchni modelu, a jeśli pędzel ma teksturę alfa, będzie ona również pokazana, aby zobrazować, jak falloff i alfa ze sobą współdziałają.

### Preset
Po wybraniu tej opcji kliknięcie na wykres krzywej otworzy menu presetów. Zaokrąglone krzywe dają miększe rezultaty, kanciaste – ostrzejsze. Przycisk `Sub` w lewym pasku narzędzi efektywnie odwraca falloff, więc szczyt krzywej będzie wciskał powierzchnię zamiast ją wyciągać, lub odwrotnie.

### Catmull-Rom
Po wybraniu użytkownik może rysować własne krzywe falloff. Edytor krzywych działa tak samo jak krzywe w pozostałych częściach Nomad:

* Kliknij na krzywej, aby utworzyć nowy punkt
* Przeciągnij punkt, aby go przesunąć
* Kliknij punkt, aby przełączać między ostrym a gładkim
* Przeciągnij punkt na sąsiedni, aby go usunąć

### B-spline
Po wybraniu użytkownik może rysować własne krzywe falloff. Edytor działa tak samo jak w Catmull-Rom, ale punkty krzywej wpływają na jej kształt zamiast leżeć bezpośrednio na niej, co może ułatwić tworzenie gładszych kształtów.

Edytor krzywej ma 3 przyciski:

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Rozwija edytor krzywej                       |
| Reset    | ![](/icons/reset.webp)     | Przywraca krzywą do stanu domyślnego        |
| Symmetry | ![](/icons/symmetric.webp) | Wyświetla krzywą jako symetryczny „czubek pędzla” |


### Influence

* Sphere (3d) – Wpływ jest obliczany na podstawie odległości wierzchołka od środka pędzla.
* Circle (2d) – Wierzchołek jest najpierw rzutowany na płaszczyznę obszaru, a dopiero potem mierzona jest jego odległość od środka pędzla. Jest to podobne do sposobu próbkowania alf.
* Cylinder – Wpływ jest rzutowany przez obszar jako cylinder, używany przez tryb Silhouette poniżej.

### Silhouette
Domyślnie pociągnięcia wpływają tylko na powierzchnię modelu w obrębie promienia pędzla. Po włączeniu silhouette pociągnięcie będzie rzutowane przez cały model. Może to być bardzo użyteczne przy wstępnym blokowaniu modelu lub dla kształtów, w których boki muszą pozostać prostopadłe.



## Filter

![](/images/filter_menu.webp) 

### Accumulate stroke
Usuwa limit ilości materiału dodawanego/usuwanego w jednym pociągnięciu. Np. narzędzie `Clay` ma tę opcję włączoną, więc materiał może się wciąż kumulować, podczas gdy `Brush` ma ją wyłączoną, więc pociągnięcia przestaną dodawać materiał, jeśli będziesz wielokrotnie przejeżdżać po tym samym obszarze siatki. 

### Front-facing vertex only
Ta opcja ignoruje wierzchołki odwrócone tyłem.
Może być przydatna, jeśli chcesz malować część cienkiej geometrii bez wpływania na drugą stronę.
Działa również przy rzeźbieniu, ale możesz zauważyć pewne artefakty.

### Allow dynamic topology
Ta opcja jest dostępna tylko wtedy, gdy siatka jest w trybie [Dynamic Topology](topology.md#dynamic-topology). Możesz włączać lub wyłączać dynamic topology osobno dla każdego narzędzia.

### Connected topology
Włącza rzeźbienie tylko na wierzchołkach połączonych z powierzchnią, której dotykasz narzędziem. Na przykład z narzędziem `Move` pozwoli to przesuwać część, nawet jeśli przecina się ona z inną częścią.
![](/videos/connected_topology.mp4)

### Protect Area
![](/images/filter_protect_area.webp) 

Te opcje zatrzymują działanie narzędzi na częściach siatki w różnych warunkach. 

Opcja „Auto” oznacza, że jeśli masz włączone hide, mask lub facegroup w menu [Shading](shading), będą one chronione, ale jeśli są tam wyłączone, ochrona jest dezaktywowana.

* `All` – Przełącznik określający, czy filtry ochrony są globalne, czy per narzędzie.
* `Hide` – Jeśli części siatki są ukryte narzędziem hide, określa, czy mają być chronione.
* `Mask` – Jeśli części siatki są zamaskowane, określa, czy mają być chronione.
* `Facegroup` – Określa, czy możesz używać narzędzia tylko w obrębie pierwszej dotkniętej grupy ścian (facegroup).


### Keep sharp edges
Wyklucza punkty, których normalne zbyt mocno różnią się od normalnej powierzchni.

Zmienia sposób obliczania płaszczyzny obszaru (Area sampling).

Opcja ta może być przydatna dla narzędzi opartych na spłaszczaniu lub gdy chcesz kolorować głównie płaską powierzchnię bez „wylewania się” na boki.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Niektóre pędzle lub opcje pociągnięcia wymagają normalnej płaszczyzny i położenia płaszczyzny względem powierzchni, aby działać.

Możesz kontrolować sposób obliczania tej średniej płaszczyzny, ustawiając obszar próbkowania jako procent promienia narzędzia.

Przy 100% brane są pod uwagę wszystkie punkty wewnątrz okręgu zaznaczenia.

Przy 0% brany jest pod uwagę tylko najbliższy wierzchołek lub trójkąt. Wartości te mogą być połączone dla `Normal radius` i `Position radius` lub odblokowane i ustawiane niezależnie.


### Depth masking
![](/images/stroke_depthmask.webp)

Wyklucza punkty znajdujące się powyżej lub poniżej określonej odległości od obliczonej płaszczyzny (Area sampling).

Można tego użyć do malowania tylko na wypukłościach lub tylko w zagłębieniach.

Wykres przedstawia przekrój powierzchni; pozioma linia to miejsce, gdzie znajduje się powierzchnia, okrąg reprezentuje promień wygaszania pędzla powyżej i poniżej powierzchni. `Height offset` to procent powyżej lub poniżej powierzchni, od którego zaczyna się obliczanie maskowania. `Top area` i `Bottom area` pozwalają skalować wygaszanie powyżej i poniżej punktu offsetu.

#### Example: Paint in cavities
Aby malować tylko w zagłębieniach, ustaw height offset na -100% i dostosuj suwak top area tak, aby był odsunięty od linii poziomej. Oznacza to, że pierwsze kliknięcie ustawia „zerową” głębokość, a następnie wpływ będzie miała tylko powierzchnia poniżej tej głębokości.

![](/videos/stroke_depth_cavity.mp4)

#### Example: Paint on bumps
Aby malować tylko na wypukłościach, ustaw height offset na +90%, tak aby dół okręgu przecinał linię poziomą w niewielkim stopniu. Gdy klikniesz na szczycie „wysokiej” strefy, ustawi to głębokość tak, że wszystko na tej głębokości, trochę poniżej i wszystko powyżej będzie malowane. Głębokie zagłębienia zostaną pominięte.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Kontroluje, jak nacisk rysika/pióra wpływa na pędzle.

Domyślnie włączone jest `Use global settings`, co oznacza, że wszystkie pędzle współdzielą te same wartości nacisku.

### Pressure - Radius

Ta krzywa kontroluje, jak promień pędzla reaguje na nacisk. Domyślnie jest to zależność liniowa, więc jeśli twój rysik ma płynną odpowiedź, zmiana promienia również powinna być płynna. Wiele rysików ma jednak nieliniową charakterystykę, którą możesz skompensować tą krzywą. Na przykład, jeśli promień nie wydaje się osiągać maksymalnej wartości przy dużym nacisku, użyj presetu krzywej takiego jak „out-pow3”, z wygięciem skierowanym w górę, aby zwiększyć promień wcześniej.

To okno dialogowe jest podobne do wyświetlania krzywej falloff; możesz użyć presetu, stukając w okno krzywej, lub narysować własne krzywe w trybach Catmull-Rom i B-Spline.

Jeśli chcesz stały promień, wyłącz tę sekcję.

### Pressure - Intensity

Podobne do krzywej promienia, ale kontroluje intensywność. Jeśli chcesz stałą intensywność, wyłącz tę sekcję.

### Pressure smoothing

Uśrednia zdarzenia nacisku rysika dla gładszych rezultatów.
