# ![](/icons/layer.webp) Warstwy {#layers}

To menu zawiera stos warstw, czyli sposób na niedestrukcyjne zapisywanie zmian obiektu, oraz wiele sposobów łączenia warstw i ponownego ich wykorzystania.

![](/images/layers_overview.webp) 

## Przegląd {#overview}

Warstwy w Nomad mają kilka zastosowań.

Informacje o malowaniu (kolor, chropowatość, metaliczność, krycie) działają w warstwach podobnie jak w aplikacjach do malowania 2d. Możesz utworzyć warstwę i malować na niej model. Warstwę można włączać i wyłączać, zmieniać jej krycie, duplikować ją, zmieniać jej kolejność w stosie warstw i tryb mieszania.

Nomad używa warstw także do rzeźbienia. Warstwa może przechowywać drobne szczegóły, takie jak zmarszczki, albo duże zmiany, dzięki czemu działa jak blendshapes/shape keys/morph targets w innych aplikacjach 3d. Możesz na przykład wyrzeźbić różne wyrazy twarzy na różnych warstwach, a potem suwakami warstw łączyć je w nowe miny.

W tym przypadku zmiany zapisane w warstwie po prostu się sumują, więc kolejność warstw nie ma znaczenia, inaczej niż przy malowaniu.

Warstwy można częściowo wymazywać narzędziem [Usuń warstwę](tools.md#delete-layer), a także tworzyć z nich maski na podstawie różnych informacji zapisanych w warstwie.

![](/videos/layer.mp4)

::: tip
W przeciwieństwie do większości programów do rzeźbienia zmiana topologii siatki nie usuwa warstw. Możesz używać [Remeshu wokselowego](topology.md#voxel-remesher), [Multirezolucji](topology.md#multiresolution) czy narzędzi [Przytnij](tools.md#trim)/[Podziel](tools.md#split), pamiętaj jednak, że [Remesh wokselowy](topology.md#voxel-remesher) obniża jakość warstwy.
:::

::: tip
Jeśli używasz warstw jako blendshapes/morph targets, dodatkowe funkcje warstw znajdziesz w [menu sceny](scene.md#object-menu): możesz rozdzielić warstwy na obiekty i połączyć pasujące obiekty w warstwy.
:::
----

## Menu warstw {#layer-menu}

![](/images/layers_menu.webp)

Tytuł pokazuje nazwę zaznaczonego obiektu. Warstwy nie są dostępne dla prymitywów, więc najpierw zatwierdź prymityw.

Naciśnij `Dodaj warstwę`, aby utworzyć nową warstwę. `Scal warstwy` scala wszystkie warstwy z siatką bazową, a liczba obok ikony pokazuje, ile jest warstw.

Każda warstwa ma nazwę, suwak sterujący jej siłą/współczynnikiem oraz przyciski opcji. Stuknij warstwę, aby stała się aktywna: rzeźbienie i malowanie trafiają wtedy do tej warstwy. Stuknij `Podstawowa`, aby znów pracować na siatce bazowej.

### ![](/icons/sort_right.webp) Rozwiń listę {#ui-expand-list}

Domyślnie lista warstw pokazuje tylko widoczność, tryb mieszania i siłę każdej warstwy, a aktywna warstwa jest rozwinięta ze wszystkimi ustawieniami. Strzałka po lewej stronie tytułu rozwija pełne ustawienia wszystkich warstw.

![](/images/layers_expand.webp)

### Opcje {#options}

| Operacja     | Ikona                        | Opis                                                |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Widoczne     | ![](/icons/eye_open.webp)   | Pokazuje/ukrywa warstwę                             |
| Mieszanie    | ![](/icons/opacity.webp)    | Tryb mieszania w stylu Photoshopa. 4 ikony pokazują tryby dla koloru, chropowatości, metaliczności i krycia.                                 |
| Zmień nazwę  | ![](/icons/pencil.webp)     | Edytuje nazwę warstwy                               |
| Usuń         | ![](/icons/trash.webp)      | Usuwa warstwę                                       |
| Duplikuj     | ![](/icons/clone.webp)      | Duplikuje warstwę                                   |
| Scal w dół   | ![](/icons/merge_down.webp) | Scala warstwę z warstwą poniżej (lub z siatką bazową) |
| Więcej       | ![](/icons/more.webp)       | Opcje [Więcej...](#more)                            |

Gdy warstwa nie jest rozwinięta, `Zmień nazwę`, `Usuń`, `Duplikuj` i `Scal w dół` znajdziesz w jej menu [Więcej...](#more).

Aby przenieść warstwę w inne miejsce stosu, przytrzymaj jej nazwę, a potem przeciągnij.

### Podstawowa {#base}

Przycisk z 3 kropkami w wierszu `Podstawowa` przenosi malowanie siatki bazowej do nowej warstwy za pomocą przycisku `Podstawowa → Warstwa`. Siatka bazowa wraca wtedy do materiału tła. Przydaje się to, gdy dużo malowałeś, zanim utworzyłeś jakąkolwiek warstwę.

* Przyciski maski i ukrywania obok niego pozostawiają zamaskowane i ukryte obszary nietknięte.
* `Wyodrębnij` - kanały do przeniesienia: `Kolor`, `Krycie`, `Chropowatość` i `Metaliczność`.
* `Materiał tła` - jeśli ta opcja jest włączona, przenoszone są tylko wartości różniące się od tego materiału. Ustaw go suwakami albo pobierz z modelu pipetą.

### ![](/icons/more.webp) Więcej... {#more}

Przycisk „Więcej...” pokazuje dodatkowe opcje bieżącej warstwy na dwóch kartach: ustawienia (ikona koła zębatego) i wyodrębnianie (ikona sześcianu).

![](/images/layers_more.webp) 

#### Współczynniki kanału {#channel-factors}

Te ustawienia pozwalają skalować ilość rzeźbienia, koloru, chropowatości, metaliczności i krycia w warstwie. Wartości te są mnożone przez suwak współczynnika warstwy, więc jeśli na przykład siła warstwy wynosi 1, a współczynnik kanału koloru 0,5, kolor zostanie wyświetlony z siłą 0,5.

`Przesunięcie` steruje siłą rzeźbienia warstwy. Kolor, chropowatość i metaliczność są ograniczone do zakresu od 0 do 1, natomiast przesunięcie może mieć dowolną wartość, zarówno dodatnią, jak i ujemną.

::: tip
Przesunięcie pozwala zamienić warstwę wypukłości w warstwę wgłębień albo uśmiech w grymas:
![](/videos/layer_happysad.mp4)


Symetryczną warstwę można sklonować, a następnie rozdzielić na kształt lewy i prawy narzędziem Usuń warstwę:
![](/videos/layer_leftright.mp4)

Warstwy z ujemnym współczynnikiem przesunięcia można zapisać do pustych warstw, aby uzyskać nowe, dodatnie kształty.

Warstwy z dodatnim współczynnikiem przesunięcia większym niż 1 pozwalają eksperymentować z bardziej skrajnymi blendshapes.
:::

::: warning
Obecnie warstwy mają tylko jeden wspólny kanał krycia dla wszystkich 3 kanałów (kolor/metaliczność/chropowatość).
Jeśli scalasz kilka warstw z intensywnością poszczególnych kanałów poniżej pełnej, wynik końcowy może wyglądać inaczej.

Być może w przyszłości każdy kanał będzie miał własny kanał alfa, co usunie to ograniczenie.
:::


#### ![](/icons/shield.webp) Maska {#mask}
Przycisk maski obok każdego suwaka tworzy maskę z danego kanału. Podobnie jak przy używaniu warstw do tworzenia zaznaczeń w aplikacjach do malowania, pozwala to wykorzystać pracę wykonaną w warstwie do innych operacji.

#### ![](/icons/preview.webp) Podgląd {#preview}
![](/images/layers_preview.webp) 

Poniższe opcje znajdują się na karcie wyodrębniania w menu „Więcej...”.

Gdy ta opcja jest włączona, pokazuje podgląd ustawień wyodrębniania tej warstwy (zobacz następną sekcję).

`Prześwietlenie` określa, które obiekty stają się przezroczyste podczas podglądu (`Brak`, `Nie zaznaczony`, `Wybrane` lub `Wszystkie`), aby wyodrębniany kształt pozostał pełny. Przydaje się to, gdy używasz ujemnych wysokości wyodrębniania.

#### ![](/icons/mask_extract.webp) Wyodrębnij {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Przycisk `Wyodrębnij` duplikuje zawartość warstwy do nowego obiektu, zwykle z grubością ustawioną w następnej sekcji.

`Działanie zamykania:` określa sposób duplikowania:

* `Brak` - Po prostu wyodrębnia część, bez tworzenia boków ani wypełniania otworów.
* `Wypełnienie` - Otwór jest wypełniany trójkątami i wygładzany. Nie używaj tej opcji dla płaskich powierzchni.
* `Powłoka` - Zamyka wyodrębniony kształt zgodnie z wartością grubości i opcjami kierunku.
* `Warstwa` - Wyodrębnia różnicę warstwy.

#### ![](/icons/height.webp) Wysokość {#thickness}
![](/images/layers_thickness.webp) 

Głębokość wyciągnięcia powłoki. Wartości dodatnie rosną na zewnątrz powierzchni, a ujemne do jej wnętrza. Ta opcja jest ukryta, gdy działanie zamykania to `Warstwa`.

Plus/minus obok tej wartości ustawia kierunek wyciągnięcia:
* Minus ( - ) zaczyna od bieżącej powierzchni i wyciąga w dół.
* Plus ( + ) zaczyna od bieżącej powierzchni i wyciąga w górę.
* PlusMinus ( ± ) odsuwa górę i dół wyciągnięcia o tę samą wartość, więc kształt jest w połowie zagłębiony w oryginalnej powierzchni.

#### Boki {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Ta sekcja jest widoczna, gdy działanie zamykania to `Powłoka`.

`Podziały ścianki` ustawia liczbę podziałów wzdłuż boków powłoki. Gdy jego przełącznik `Auto` jest włączony, Nomad sam oblicza liczbę pętli krawędziowych tak, aby powstały kwadratowe wielokąty.

#### Gładkość {#smoothness}
![](/images/layers_smoothness.webp) 

Jeśli krawędzie wyodrębnianego obszaru są postrzępione, włącz tę opcję, aby wygładzić je w ładniejszy kształt. `Wszystkie` wygładza całą wyodrębnioną powierzchnię, a `Tylko brzegi` tylko jej krawędzie. `Iteracje` określa siłę wygładzania.

_To koniec podmenu „Więcej...”._

### ![](/icons/cog.webp) Zaawansowane {#advanced}
![](/images/layers_advanced.webp)

Przycisk `Zaawansowane` na dole menu pojawia się, gdy obiekt ma już warstwy.

#### Zachowaj szczegóły warstwy górnej {#keep-top-layers-details}

Sprawia, że drobne szczegóły na wyższych warstwach pozostają widoczne, gdy wprowadzasz duże zmiany na niższych warstwach. Podczas rzeźbienia deformacja pochodząca z górnych warstw jest ignorowana, ale ich szczegóły pozostają widoczne. Działa to dobrze tylko wtedy, gdy górne warstwy zawierają stosunkowo drobne szczegóły.

Domyślnie, jeśli wyrzeźbisz drobne zmarszczki na warstwie, a potem wprowadzisz duże zmiany w warstwie bazowej, zmarszczki zostaną utracone. Włączenie tej opcji sprawia, że drobne szczegóły zawsze unoszą się nad dużymi zmianami poniżej. Na poniższym filmie zobacz, jak zmarszczki znikają przy ustawieniach domyślnych, ale pozostają widoczne po włączeniu opcji „Zachowaj szczegóły warstwy górnej”:

![](/videos/layers_details.mp4)


#### Synchronizuj transformację {#sync-transform}

Gdy ta opcja jest włączona, wszystkie niezaznaczone warstwy są dostosowywane do obrotu, skali i ścinania przekształcenia, gdy używasz narzędzi Gizmo lub Przekształcenie. Może mieć wartość `Auto`, `Nie` lub `Tak`.

Wyłącz tę opcję, jeśli pozostałe warstwy mają być używane bez nowego przekształcenia, które stosujesz.

Przy ustawieniu `Auto` dostosowywane są tylko widoczne warstwy.
