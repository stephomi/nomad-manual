# ![](/icons/material.webp) Materiał {#material}

To menu pozwala zmienić materiał bieżącego obiektu, właściwości renderowania obiektu/materiału oraz przypisać tekstury do materiału.

![](/images/material_overview.webp)

Materiały definiują wygląd obiektu, kontrolując, jak reaguje on na światło i inne obiekty. Wygląd obiektu jest kontrolowany przez następujące właściwości:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Kombinacje tych właściwości pozwalają uzyskać szeroką gamę efektów – od fotorealistycznych, przez kreskówkowe, po eksperymentalne.

Kolor, chropowatość (roughness), metaliczność (metalness) i krycie (opacity) można malować; więcej informacji znajdziesz w [Vertex Paint options](painting.md).

Typ materiału, reflectance, emssive/unlit to właściwości materiału opisane poniżej.

Przyciski kopiuj/wklej na górze tego menu pozwalają kopiować materiały z jednego obiektu na inny.

Pamiętaj, że renderer Nomada jest rendererem czasu rzeczywistego; mimo że jest wydajny, w przypadku niektórych efektów przedkłada szybkość nad dokładność. 

## Typy materiału {#material-types}

![](/images/material_types.webp)

Typy materiałów w Nomadzie to: Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Nieprzezroczysty {#opaque}
Domyślny tryb, który traktuje powierzchnie jako prosty materiał obsługujący malowany kolor, roughness, metalness, opacity.

### ![](/icons/material_subsurface.webp) Podpowierzchniowy {#subsurface}
Ten tryb może symulować materiał, który pozwala światłu rozmywać się i rozpraszać wewnętrznie, jak skóra, wosk, jadeit.

Aby uzyskać najlepszy efekt, przełącz się na tryb cieniowania PBR i użyj co najmniej jednego światła kierunkowego lub punktowego, najlepiej przy przyciemnionym otoczeniu.

`Depth` kontroluje, jak daleko światło rozprasza się od przodu, pod powierzchnią, a następnie z powrotem na przednią powierzchnię. Powoduje to zmiękczenie twardych cieni i rozmycie detali powierzchni.

`Translucency` kontroluje, jak światło rozprasza się z przodu na tył kształtu, jak rozproszenie przez spodnią stronę liścia lub gdy uszy są mocno podświetlone od tyłu. 

### ![](/icons/material_blending.webp) Mieszanie {#blending}

Podobny do Opaque, ale obsługuje suwak opacity, który pozwala mieszać materiał między pełną nieprzezroczystością a przezroczystością. Jest to prosty pojedynczy suwak krycia, w przeciwieństwie do malowalnego krycia obsługiwanego przez materiał opaque. 

::: warning
Tryb Blending może powodować migotanie i „wyskakiwanie” w złożonych lub przecinających się kształtach.
:::

### ![](/icons/material_additive.webp) Addytywny {#additive}
Możesz sprawić, że siatka będzie półprzezroczysta przy użyciu tego materiału. Jest podobny do materiału blending, ale podczas gdy blending miesza się z otoczeniem, additive będzie zawsze jaśniejszy niż obiekty za nim, co jest dobre do jasnych efektów, takich jak promienie światła, ogień, eksplozje.

Możesz ustawić wartość opacity wyższą niż 1, co oznacza, że obiekt będzie jaśniejszy.  
Może to być przydatne, jeśli chcesz użyć [bloom](postprocess.md#bloom) i `threshold parameter`, aby tylko ten obiekt świecił jak obiekt emisyjny.

Ten tryb ma zwykle mniej artefaktów niż [Blending](#blending) (order independent transparency).

### ![](/icons/material_refraction.webp) Załamanie {#refraction}
Ten tryb może być użyty do symulacji materiału szklanego. Ze względu na ograniczenia czasu rzeczywistego, autorefrakcja i wielowarstwowa refrakcja są częściowo ograniczone.

Malowana chropowatość (roughness) modelu wpływa na to, jak rozmyta jest refrakcja.
Domyślnie każdy obiekt utworzony w Nomadzie ma roughness nieco około 25%, więc refrakcja nie będzie idealna, lecz lekko rozmyta.
Możesz użyć przycisku `paint glossy`, aby przemalować model z roughness i metalness równymi 0 (kolory nie zostaną zmienione).

W grę wchodzą 2 różne chropowatości: jedna steruje rozmyciem odbicia na powierzchni, a druga wnętrza (refrakcją).  
Ponieważ jednak w Nomadzie jest tylko jeden kanał malowania roughness, chropowatość wnętrza i zewnętrza będzie miała tę samą wartość.  
Aby mieć różne wartości (na przykład lizak z ostrą powierzchnią, ale rozmytym wnętrzem), użyj suwaków `Surface glossiness` i `Interior roughness`, aby nadpisać malowaną chropowatość.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Sprawia, że obiekt jest półprzezroczysty poprzez odrzucanie części pikseli w losowy sposób.

### ![](/icons/material_shadow_catcher.webp) Łapacz cieni {#shadow-catcher}

Sprawia, że obiekt jest niewidoczny i jedynie przyjmuje cienie. Przydatne do łączenia renderów z Nomada z innymi obrazami. 

::: tip

Więcej informacji o przezroczystości i trybach mieszania można znaleźć na https://support.fab.com/s/article/Transparency-Opacity

:::

## Kontrolki {#controls}

![](/images/material_controls.webp)

### Zawsze nieoświetlony {#always-unlit}
Jeśli włączone, obiekt zignoruje PBR i Matcap i po prostu wyświetli swój kolor malowania bez cieniowania.
Pamiętaj, że jeśli używasz [Additive](#additive), możesz malować przezroczystość bezpośrednio, używając czarnego koloru.

### Krycie {#opacity}
Jak bardzo solidny lub nieprzezroczysty będzie obiekt; 100% to pełna nieprzezroczystość, 0% to pełna przezroczystość. Możesz też malować opacity dla dokładniejszej kontroli.

### Reflektancja {#reflectance}
Kontroluje ilość odbicia, jaką materiał otrzyma dla materiałów niemetalicznych. Najczęściej należy używać wartości domyślnej (która odpowiada standardowym 4% odbitego światła pod kątem prostym), ale można ją zwiększyć, aby wzmocnić odbicia i highlighty, na przykład w oczach postaci.

### Odwrócone odcinanie {#inverse-culling}
Odwraca normalne powierzchni. Zwykle nie jest wymagane, ale może być użyte, jeśli model wydaje się „na lewą stronę” lub w połączeniu z wyłączonym `Two sided` może posłużyć do tworzenia wnętrz, gdzie ściana najbliżej kamery jest zawsze ukryta.

### Gładkie cieniowanie {#smooth-shading}
Zobacz [global option](settings.md#smooth-shading).  
Wartość `Auto` użyje opcji globalnej.

### Dwustronny {#two-sided}
Zobacz [global option](settings.md#two-sided).  
Wartość `Auto` użyje opcji globalnej.

### Kolorowany tył {#coloured-backface}
Zobacz [global option](settings#two-sided).
Wartość `Auto` użyje opcji globalnej.

### Rzuca cienie {#casts-shadows}
Na razie `Auto` jest tym samym co `On`.
Przezroczyste obiekty również rzucają cienie (w wzorze dithering, aby emulować mieszane cienie).  
Pamiętaj, aby wyłączyć rzucanie cieni, jeśli masz duży obiekt w scenie, który nie musi rzucać cieni (na przykład duża podłoga).

### Otrzymuje cienie {#recieve-shadows}
Na razie `Auto` jest tym samym co `On`.

### Szkielet (siatka) {#wireframe}
Zobacz [global option](settings.md#wireframe).  
Wartość `Auto` użyje opcji globalnej.


## Tekstury {#textures}

![](/images/material_textures.webp)

Jeśli obiekt ma UV, można zastosować tekstury do materiału oprócz kolorów/roughness/metalness/opacity w wierzchołkach. Zwykle są one wynikiem wypalania tekstur (texture bake), ale można też używać obrazów utworzonych poza Nomadem.

Tekstury można zastosować do:

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Kliknięcie w slot tekstury otworzy selektor. Po przypisaniu tekstury do slotu materiału, ponowne kliknięcie otworzy panel tekstury:

### Opcje panelu tekstur {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Otwórz {#open}
Wybierz inną teksturę

### Brak {#none}
Usuń teksturę

### Krycie {#texture-opacity}

Jeśli obraz ma kanał alfa, pozwoli to użyć go do Opacity lub go zignorować.

### ![](/icons/link.webp) Ikona łańcucha/linku {#chainlink-icon}

Ikona linku w poniższych sekcjach, gdy jest włączona, oznacza, że użyte opcje będą współdzielone z innymi teksturami (color, normal, roughness, metalness, opacity, emissive), które również mają włączoną swoją ikonę linku. 

Pozwala to upewnić się, że jeśli masz wyrównane tekstury, pozostaną one wyrównane nawet po zmianie parametrów lub typów projekcji.


### Projekcja {#projection}
![](/images/material_projection.webp)

Ustawia sposób nakładania tekstury na obiekt.

* `Auto` - Jeśli obiekt ma UV, UV, w przeciwnym razie Triplanar
* `UV` - Użyj współrzędnych UV siatki do nałożenia tekstury. Jeśli siatka i tekstura pochodzą spoza Nomada lub mają być eksportowane z Nomada do użycia gdzie indziej, UV jest właściwą opcją.
* `Triplanar` - Rzutuje teksturę wzdłuż osi X, Y, Z i miesza szwy. 

### Trójpłaszczyznowa {#triplanar}
![](/images/material_triplanar.webp)

Projekcje triplanar to potężny, a zarazem prosty sposób nakładania tekstur na obiekty.

Triplanar jest jak 6 projektorów wideo z tym samym obrazem, świecących na przód, tył, lewo, prawo, górę i dół obiektu.

W razie potrzeby można to następnie wypalić do UV lub kolorów wierzchołków.


![](/images/material_triplanar_example.webp)

#### Metoda {#method}

* `Local` - Projekcja będzie poruszać się wraz z transformacją obiektu
* `World` - Projekcja pozostaje nieruchoma, a poruszanie obiektem przesuwa go przez projekcję.

#### Twardość {#hardness}

Sposób mieszania projekcji. 100% oznacza brak mieszania i ostre krawędzie projekcji. 0% oznacza mieszanie krawędzi pod szerokim kątem. Wartość domyślna to 90% – wystarczające mieszanie, aby ukryć krawędzie i pozwolić reszcie projekcji pozostać ostrą.

### Jednolite {#uniform}

Po zaznaczeniu ta sama twardość jest używana dla wszystkich projekcji. Po odznaczeniu pojawiają się dodatkowe kontrolki twardości dla projekcji X, Y, Z.


### Parametr {#parameter}
![](/images/material_parameter.webp)

#### Filtrowanie {#filtering}
Metoda filtrowania tekstury; `Auto` jest domyślne, dostępne metody to `Nearest`, `Linear`, `Mipmap`. Nearest nie wykonuje filtrowania, więc tekstury mogą mieć postrzępione artefakty przy oglądaniu z bliska. Linear i Mipmap zapewniają lepsze filtrowanie, więc tekstury wydają się rozmyte, a nie postrzępione z bliska.

#### Kafelkowanie-X {#tiling-x}
Jeśli parametr Scale jest większy niż 1, co sprawia, że tekstura jest mniejsza niż UV obiektu, określa, jak tekstura będzie kafelkowana wzdłuż osi X. `None` oznacza brak powtórzeń. `Repeat` będzie powielać teksturę. `Mirror` będzie powielać teksturę, przy czym co drugi kafelek będzie odwrócony, co może pomóc ukryć artefakty kafelkowania.

#### Kafelkowanie-Y {#tiling-y}
Tak samo jak Tiling-X, ale dla osi Y.

### Transformacja {#transform}
![](/images/material_transform.webp)

Dodatkowe 2D transformacje stosowane do tekstury w przestrzeni UV. Przycisk reset przywraca wartości domyślne, ikona łańcucha (gdy wybrane są tekstury inne niż color) połączy lub rozłączy transformację tak, aby była taka sama jak dla tekstury color.

#### Translacja {#translation}
Przesunięcie tekstury w osi X i Y

#### Rotacja {#rotation}
Obrót tekstury

#### Skala {#scale}
Skala tekstury; większe liczby sprawią, że tekstura będzie mniejsza na obiekcie. Użyj suwaków Tiling-X i Tiling-Y, aby kontrolować, co się wtedy dzieje.

### Jednolita skala {#uniform-scale}
Po wyłączeniu Nomad pokaże osobne kontrolki dla Scale-X i Scale-Y.