# ![](/icons/postprocess.webp) Postprocessing {#post-process}

To menu kontroluje wiele aspektów Nomada wpływających na wygląd renderu.

![](/images/postprocess_overview_drac.webp)

Użycie postprocessingu może znacząco zmienić ostateczny wygląd sceny.

![](/images/postprocess_overview.webp)
*Ta sama scena przed i po postprocessingu, bez dodatkowych świateł ani zmian materiałów.*

Post process może mocno wpływać na wydajność, w zależności od urządzenia.
Jest globalny checkbox wyłączający cały postprocess, aby można było szybko wrócić do rzeźbienia/modelowania bez utraty presetów.
Dla renderingu PBR [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) i [Tone Mapping](#tone-mapping) powinny być włączone.

Jednak najczęściej chcesz mieć post process wyłączony podczas rzeźbienia, aby skupić się na samym kształcie renderu.


## Jakość {#quality}

![](/images/postprocess_quality.webp)
### Maksymalne próbkowanie klatki {#max-frame-sampling}
Nomad obliczy pewną ilość postprocessingu dla pojedynczego renderu klatki, co może wyglądać szumiąco. To ustawienie określa, ile klatek zostanie wyrenderowanych, a następnie zblendowanych, aby usunąć większość zaszumionych artefaktów. Niektóre efekty nie wymagają dodatkowych próbek (np. color grading), podczas gdy inne, jak global illumination, mogą wymagać setek próbek, aby były wolne od szumu. 

W widoku roboczym widać to, gdy Nomad zostanie pozostawiony w spokoju – jakość obrazu stopniowo się poprawia aż do osiągnięcia maksymalnej liczby próbek, a potem się zatrzymuje. Ta liczba obliczeń jest również używana w sekcji renderu w [menu Files](files), gdy kliknięty zostanie „export png”.

### Mnożnik rozdzielczości {#resolution-multiplier}
Ten suwak kontroluje rozdzielczość postprocessingu. Wartość x1.0 oznacza, że render jest wykonywany w natywnej rozdzielczości pikseli urządzenia. Wartość x0.5 będzie renderować w połowie rozdzielczości, co jest szybkie, ale niskiej jakości. Wartość większa niż 1 będzie renderować w większym rozmiarze, a następnie skalować w dół. Skutkuje to wyższą jakością, mniejszym szumem, ale dłuższym czasem renderu.

### Maksymalna liczba próbek {#max-samples}

Zwiększa to jakość postprocessu, ale zazwyczaj `Full resolution` ma większy wpływ. 

### Odszumiacz (oidn) {#oidn}

Zastosuj denoiser do obrazu. Pozwala to używać znacznie mniejszej liczby próbek. Działa tylko, jeśli `Full Resolution` jest włączone. Zwróć uwagę, że odszumianie następuje po obliczeniu wszystkich próbek i może być obciążające dla procesora.

## Przeglądarka presetów {#preset-browser}
![](/images/postprocess_presets.webp)
Kliknięcie na obrazku wyświetli kolekcję presetów postprocessingu. Aby zdefiniować własne presety, wybierz jeden, kliknij „clone”, wprowadź zmiany. Aby zapisać, kliknij obrazek presetu, kliknij ponownie wewnątrz przeglądarki presetów i wybierz „save”.


## Odbicie (SSR) {#reflection-ssr}
Dzięki tej opcji obiekty mogą odbijać inne obiekty w scenie, o ile są one widoczne na ekranie.
Jeśli masz w scenie metaliczne i błyszczące obiekty, ta opcja powinna prawdopodobnie być używana.
Ta opcja działa tylko w trybie PBR.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Globalne oświetlenie (SSGI) {#global-illumination-ssgi}

Global illumination symuluje, jak światło odbija się między powierzchniami, np. czerwona ściana rzuci czerwone światło na pobliski biały obiekt. Może to ogromnie zwiększyć realizm renderu, gdy jest używane z ambient occlusion i odbiciami. 

`Strength` - Intensywność global illumination. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Reflektor znajduje się za sferą, skierowany w sufit. Z wyłączonym SSGI oświetlony jest tylko sufit. Z włączonym SSGI światło odbija się od sufitu na ściany i na sferę._

## Otaczająca okluzja (SSAO) {#ambient-occlusion-ssao}
Ambient occlusion przyciemnia obszary, do których światło ma mniejsze szanse dotrzeć (rogi itp.).
Efekt zależy wyłącznie od geometrii modelu.

* `Strength`- Intensywność efektu.
* `Size`- Jak szeroko rozprzestrzenia się efekt.
* `Curvature bias` - Jak czuły jest efekt względem zmian powierzchni.
* `Color` - Barwa mnożona przez zacienienie, używana do kreatywnych efektów.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO będzie najbardziej widoczne w obszarach oświetlonych głównie światłem środowiskowym. Obszary znajdujące się pod silnym bezpośrednim światłem otrzymają znacznie słabszy efekt AO.

:::

## Głębia ostrości (DOF) {#depth-of-field-dof}
Dodaje efekt rozmycia w obszarach znajdujących się poza punktem ostrości.

Po prostu stuknij w model, aby zmienić punkt ostrości.

* `Far blur` - Ilość rozmycia stosowana po dalszej stronie punktu ostrości.
* `Near blur` - Ilość rozmycia stosowana między punktem ostrości a kamerą.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Poświata {#bloom}
Bloom sprawia, że jasne obszary sceny świecą.

* `Intensity` - siła efektu.
* `Radius` - Zasięg efektu.
* `Threshold` - Jak jasne muszą być piksele w scenie, zanim zaczną bloomować. Niska wartość sprawi, że wszystko będzie bloomować, wysoka pozwoli bloomować tylko najjaśniejszym pikselom.
* `Color` - barwa, którą można dodać do bloom dla kreatywnych efektów.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Mapowanie tonalne {#tone-mapping}
Tone Mapping to operacja, która remapuje wartości HDR do zakresu `[0, 1]`.
Jeśli go nie używasz (lub wybierzesz `none`), każdy składnik koloru wyższy niż 1 zostanie obcięty.
Wszelkie różnice kolorów powyżej tego zakresu zostaną utracone.

* `None/Neutral/Agx/ACES` - który tonemapper ma być użyty. `None` nie wykonuje remapowania (ale pozostałe kontrolki nadal działają). Pozostałe opcje są podobne do wyboru różnych typów filmu – w różny sposób radzą sobie z prześwietlonymi wartościami i kolorami. To bardzo rozległy temat, poszukaj informacji o tone mapping, Agx, ACES, aby dowiedzieć się więcej!
* `Exposure` - ogólna jasność obrazu, podobna do regulacji przysłony w aparacie. Może to być szybki sposób na globalne rozjaśnienie lub przyciemnienie obrazu.
* `Saturation` - siła koloru. 1 jest neutralne, 0 to monochrom, wartości powyżej 1 są coraz bardziej nasycone.
* `Contrast` - Sprawia, że ciemne partie są ciemniejsze, a jasne jaśniejsze. Używaj ostrożnie, przy wysokich wartościach może wprowadzać artefakty.

Zauważ, że przy wyłączonym `Tone Mapping` niektóre detale znikają, ponieważ piksele są zbyt jasne.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping może wzmocnić efekt global illumination. Jeśli zmniejszysz intensywność mapy środowiskowej, zwiększysz moc głównego źródła światła, możesz następnie zwiększyć `exposure` w tone mapping, aby zobaczyć więcej efektów światła odbitego.
:::

## Korekcja kolorów {#color-grading}
Podobnie jak narzędzie krzywych w Photoshopie, pozwala kontrolować balans i rozkład kolorów w obrazie. Kontrolka `main` wpływa na cały balans kolorów, a `red`/`green`/`blue` pozwalają na precyzyjną kontrolę. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Krzywizna {#curvature}
Wykrywa miejsca, w których występują szybkie zmiany krzywizny, i nakłada na te obszary kolor.

* `Factor` - ogólna intensywność efektu
* `Bump` - jak mocno będą wykrywane ostre wypukłe zmiany i umieszczany tam będzie wybrany kolor (domyślnie biały)
* `Cavity` - jak mocno będą wykrywane wklęsłe zmiany i umieszczany tam będzie wybrany kolor (domyślnie czarny)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Aberracja chromatyczna {#chromatic-aberration}
Symuluje artefakty obiektywu, w których światło rozszczepia się przy krawędziach ekranu.

* `Strength` - jak mocno czerwone/zielone/niebieskie składowe obrazu są rozdzielane przy krawędziach ekranu

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Winieta {#vignette}
Symuluje artefakty obiektywu poprzez przyciemnianie krawędzi ekranu.

* `Size` - Rozmiar odwróconej elipsy nałożonej na obraz
* `Hardness` - Jak rozmyta lub ostra jest elipsa mieszana z obrazem.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Ziarno {#grain}
Dodaje efekt ziarna, co może pomóc sprawić, że obraz będzie wyglądał mniej sztucznie.

* `Strength` - ilość ziarna/szumu dodanego do obrazu.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Ostrość {#sharpness}
Efekt wyostrzania podobny do tego w Photoshopie lub aplikacjach do obróbki zdjęć.

* `Strength` - ilość wyostrzenia zastosowana do obrazu.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel art {#pixel-art}
Symuluje pikselart z retro gier.

* `Slider` - rozmiar pikseli
* `Allow frame sampling` - jeśli pojawia się dużo czarnych pikseli, spróbuj to włączyć – nadpisze to domyślne próbkowanie.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Skanlinia {#scanline}
Symuluje wygląd starych monitorów CRT.

* `Factor` - siła linii
* `Spacing` - rozmiar linii

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering {#dithering}

Dithering pikseli w celu redukcji artefaktów pasmowania. Zazwyczaj powinien być włączony, ale można go wyłączyć dla specyficznych operacji (np. eksport map głębi lub innych operacji specyficznych dla danych).