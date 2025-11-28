# ![](/icons/layer.webp) Warstwy {#layers}

To menu zawiera stos warstw – sposób na przechowywanie edycji obiektu w nieniszczący sposób – oraz wiele metod łączenia i ponownego wykorzystania warstw.

![](/images/layers_overview.webp) 

## Przegląd {#overview}

Warstwy w Nomadzie pełnią wiele funkcji.

Informacje o malowaniu (Kolor, Szorstkość, Metaliczność, Krycie) działają z warstwami podobnie jak w 2D aplikacjach malarskich. Można utworzyć warstwę i nanieść farbę na model. Warstwę można włączać i wyłączać, regulować jej krycie, duplikować, zmieniać jej kolejność w stosie warstw oraz modyfikować tryb mieszania.

Nomad używa też warstw do rzeźbienia. Warstwa może przechowywać drobne detale, takie jak zmarszczki, albo duże zmiany, pozwalając jej działać jak blendshapes/shape keys/morph targets w innych aplikacjach 3D. Na przykład możesz wyrzeźbić różne wyrazy twarzy na różnych warstwach i regulować suwaki warstw, aby łączyć je w nowe ekspresje.

W tym przypadku zmiany zapisane w warstwie są czysto addytywne, kolejność warstw nie ma znaczenia tak jak w przypadku malowania.

Warstwy można częściowo wymazywać za pomocą narzędzia [Delete Layer](tools.md#delete-layer), a warstwy mogą być również używane do tworzenia masek na podstawie różnych informacji zapisanych w warstwie.

![](/videos/layer.mp4)

::: tip
W przeciwieństwie do większości oprogramowania do rzeźbienia, zmiana topologii siatki nie spowoduje odrzucenia warstw. Możesz używać [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multires) lub narzędzi [Trim](tools.md#trim)/[Split](tools.md#split), ale pamiętaj, że przy użyciu [Voxel Remesher](topology.md#voxel-remesher) jakość warstwy będzie miała na to wpływ.
:::

::: tip
Jeśli używasz warstw jako blendshapes/morph targets, w [menu sceny](scene.md#object-menu) dostępne są dodatkowe funkcje warstw. Możesz rozdzielać warstwy na obiekty i łączyć pasujące obiekty w warstwy.
:::
----

## Menu warstw {#layer-menu}

![](/images/layers_menu.webp)

Naciśnij `Add layer`, aby utworzyć nową warstwę.

Każda warstwa ma nazwę, suwak do kontrolowania jej siły/współczynnika oraz przyciski opcji.

### Opcje {#options}

| Action       | Icon                         | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Show/hide the layer                                 |
| Blend Mode   | ![](/icons/opacity.webp)    | The photoshop style blending mode. The 4 icons display the modes for Color, Roughness, Metalness, Opacity.                                 |
| Edit Name    | ![](/icons/pencil.webp)     | Edit the layer name                                 |
| Delete       | ![](/icons/trash.webp)      | Delete the layer                                    |
| Duplicate    | ![](/icons/clone.webp)      | Duplicate the layer                                 |
| Merge Down   | ![](/icons/merge_down.webp) | Merge the layer with the lower layer (or base mesh) |
| More         | ![](/icons/more.webp)       | [More...](#more) options                            |

Aby przenieść warstwę w inne miejsce stosu warstw, naciśnij i przytrzymaj jej nazwę, a następnie przeciągnij.

### Więcej... {#more}

Przycisk „More...” wyświetli dodatkowe opcje dla bieżącej warstwy:

![](/images/layers_more.webp) 

#### Współczynniki kanałów {#channel-factors}

Te kontrolki pozwalają skalować ilość rzeźby/koloru/szorstkości/metaliczności/krycia dla warstwy. Wartości te są mnożone przez suwak współczynnika warstwy, więc na przykład jeśli siła warstwy wynosi 1, ale współczynnik kanału koloru to 0.5, kolor będzie wyświetlany z siłą 0.5.

`Offset` kontroluje siłę rzeźbienia warstwy. Podczas gdy kolor/szorstkość/metaliczność są ograniczone do zakresu 0–1, offset może mieć dowolną wartość, zarówno dodatnią, jak i ujemną. 

::: tip
Offset może być użyty do zamiany warstwy wypukłości w warstwę zagłębień lub uśmiechu w grymas:
![](/videos/layer_happysad.mp4)


Symetryczną warstwę można sklonować, a następnie podzielić na kształty lewej/prawej strony za pomocą del layer:
![](/videos/layer_leftright.mp4)

Warstwy z ujemnymi współczynnikami offset można wypalić do pustych warstw, aby tworzyć nowe dodatnie kształty.

Warstwy z dodatnimi współczynnikami offset powyżej 1 można wykorzystać do eksperymentowania z bardziej ekstremalnymi blendshapes.
:::

::: warning
Obecnie warstwy współdzielą tylko jeden kanał krycia dla wszystkich 3 kanałów (kolor/metaliczność/szorstkość).
Jeśli połączysz wiele warstw z intensywnością per-kanał, które nie są ustawione na pełną intensywność, możliwe, że końcowy rezultat będzie wyglądał inaczej.

Być może w przyszłości każdy kanał będzie miał własny kanał alfa, aby usunąć to ograniczenie.
:::


#### ![](/icons/tool_mask.webp) Maska {#mask}
Przycisk maski obok każdego suwaka utworzy maskę z danego kanału. Podobnie jak używanie warstw do tworzenia zaznaczeń w aplikacjach malarskich, pozwala to ponownie wykorzystać pracę wykonaną na warstwie do innych operacji.

#### ![](/icons/preview.webp) Podgląd {#preview}
![](/images/layers_preview.webp) 

Po włączeniu podglądane będą ustawienia ekstrakcji dla tej warstwy (zobacz następną sekcję).

Gdy włączony jest tryb xray, tylko wyekstrahowany kształt będzie nieprzezroczysty, reszta kształtu stanie się przezroczysta, co jest przydatne, jeśli używasz ujemnych wysokości ekstrakcji.

#### Ekstrakcja {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Przycisk `Extract` zduplikuje zawartość warstwy do nowego obiektu, zazwyczaj z określoną przez użytkownika grubością ustawioną w następnej sekcji.

`Closing action` określa sposób wykonania duplikacji:

* None - Po prostu wyodrębnij fragment, nie próbuj generować boków ani wypełniać żadnych otworów.
* Fill - Otwór jest wypełniany i wygładzany trójkątami. Nie używaj tej opcji dla płaskich powierzchni.
* Shell - Zamknij wyekstrahowany kształt z użyciem wartości grubości i opcji kierunku.
* Layer - Wyodrębnij różnicę warstwy.

#### ![](/icons/height.webp) Grubość {#thickness}
![](/images/layers_thickness.webp) 

Głębokość ekstruzji powłoki. Wartości dodatnie rosną na zewnątrz powierzchni, wartości ujemne w głąb powierzchni.

Przyciski plus/minus obok tej wartości ustawiają kierunek ekstruzji:
* Minus ( - ) rozpocznie od bieżącej powierzchni i wyekstruduje w dół. 
* Plus ( + ) rozpocznie od bieżącej powierzchni i wyekstruduje w górę.
* PlusMinus ( ± ) odepchnie górę i dół ekstruzji o równe wartości, tak że będzie ona w połowie zatopiona w oryginalnej powierzchni.

#### Gładkość {#smoothness}
![](/images/layers_smoothness.webp) 

Jeśli krawędzie obszaru do wyodrębnienia są postrzępione, ten suwak spróbuje rozmyć krawędź do gładszego kształtu. 

#### ![](/icons/height.webp) Pętla krawędzi (bok) {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Ta sekcja jest widoczna, gdy closing action to „Shell”. 

`Auto Edge-loop (side)` obliczy liczbę pętli krawędzi wzdłuż boków powłoki, aby utworzyć kwadratowe poligony. 

Jeśli jest wyłączone, suwak `Division` ustawi liczbę podziałów na bokach.

_To jest koniec podmenu „More...”._

### Zaawansowane {#advanced}
![](/images/layers_advanced.webp)

#### Zachowaj detale górnych warstw {#keep-top-layers-details}

Zapewnia, że drobne detale na wyższych warstwach pozostaną widoczne, gdy duże zmiany są wprowadzane na niższych warstwach.

Domyślnie, jeśli wyrzeźbisz drobne zmarszczki na warstwie, a następnie wprowadzisz duże zmiany w warstwie bazowej, zmarszczki zostaną utracone. Włączenie tego przełącznika pozwoli tym drobnym detalom zawsze „unosić się” ponad dużymi zmianami poniżej. Na poniższym filmie zobacz, jak detal zmarszczek jest domyślnie usuwany, ale pozostaje widoczny, gdy „keep top layers details” jest włączone:

![](/videos/layers_details.mp4)


#### UI: Rozwiń listę {#ui-expand-list}

Domyślne menu warstw pozwala przełączać widoczność warstw i krycie warstwy. Włączenie tej opcji rozwija pełne kontrolki dla każdej warstwy.

![](/images/layers_expand.webp)

#### Synchronizuj transformację {#sync-transform}

Jeśli włączone, wszystkie niezaznaczone warstwy zostaną dostosowane w zależności od transformacji obrotu, skali, pochylenia. 

Wyłącz tę opcję, jeśli inne warstwy mają być używane bez nowej transformacji, którą stosujesz.

Gdy ustawione na `Auto`, dostosowane zostaną tylko widoczne warstwy.