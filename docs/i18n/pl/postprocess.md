# ![](/icons/postprocess.webp) Postprocessing {#post-process}

To menu steruje wieloma ustawieniami Nomad, które wpływają na wygląd renderu.

![](/images/postprocess_overview_drac.webp)

Postprocessing może znacząco zmienić ostateczny wygląd sceny.

![](/images/postprocess_overview.webp)
*Ta sama scena przed postprocessingiem i po nim, bez dodatkowych świateł i zmian materiałów.*

W zależności od urządzenia postprocessing może mocno wpływać na wydajność.
Globalne pole wyboru `Postprocessing` wyłącza cały postprocessing, dzięki czemu możesz szybko wrócić do rzeźbienia lub modelowania bez utraty swoich ustawień wstępnych.
Przy renderowaniu PBR warto włączyć [Okluzję otoczenia](#ambient-occlusion-ssao), [Odbicie](#reflection-ssr) i [Mapowanie odcienia](#tone-mapping).

Podczas rzeźbienia zwykle jednak lepiej wyłączyć postprocessing, aby skupić się na samym kształcie, a nie na renderze.


## Jakość {#quality}

![](/images/postprocess_quality.webp)

Te opcje poprawiają jakość renderu kosztem wydajności.

### Maks. próbkowanie klatek {#max-frame-sampling}
Przy renderowaniu pojedynczej klatki Nomad oblicza tylko część postprocessingu, przez co obraz może wyglądać na zaszumiony. To ustawienie określa, ile klatek zostanie wyrenderowanych i zmieszanych ze sobą, aby usunąć większość szumu. Niektóre efekty nie wymagają dodatkowych próbek (np. korekcja kolorów), a inne, takie jak miękkie cienie i globalne oświetlenie, mogą wymagać setek próbek, aby pozbyć się szumu.

W widoku widać to zawsze, gdy zostawisz Nomad w spokoju: jakość obrazu stopniowo się poprawia aż do maksymalnej liczby próbek, a potem się zatrzymuje. Po zatrzymaniu Nomad nic nie robi, co oszczędza baterię. Ta sama liczba obliczeń jest używana w sekcji renderowania [menu Pliki](files) po kliknięciu „export png”.

Pole wyboru obok suwaka włącza lub wyłącza próbkowanie klatek.

### Rozdzielczość renderowania {#resolution-multiplier}
Ten suwak steruje rozdzielczością renderu. Wartość x1.0 oznacza, że render powstaje w rozdzielczości pikselowej urządzenia. Wartość x0.5 renderuje w połowie rozdzielczości, co jest szybkie, ale daje niską jakość. Wartość większa niż 1 renderuje w większym rozmiarze, a potem pomniejsza obraz. Daje to wyższą jakość i mniej szumu, ale wydłuża czas renderowania.

Ma to duży wpływ na wydajność, więc staraj się nie przekraczać x1.25. Ta wartość nie jest zapisywana w ustawieniach, a efekt [Pixel Art](#pixel-art) ją zastępuje.

### ![](/icons/intensity.webp) Maks. liczba próbek {#max-samples}

Poprawia jakość efektów postprocessingu kosztem wydajności.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Rozprasza piksele (dithering), aby ograniczyć efekt pasmowania (na przykład w gradientach lub winiecie). Zwykle powinien być włączony, ale możesz go wyłączyć do konkretnych zadań (np. eksportu map głębi lub innych operacji na danych).

### ![](/icons/denoise.webp) Denoiser (oidn) {#oidn}

Stosuje odszumianie do obrazu po zebraniu wszystkich klatek. Pozwala to używać znacznie mniejszej liczby próbek. Odszumianie mocno obciąża procesor, więc włączaj je tylko wtedy, gdy obraz jest zaszumiony. Nie jest dostępne na każdym urządzeniu.

## Przeglądarka ustawień wstępnych {#preset-browser}
![](/images/postprocess_presets.webp)
Kliknięcie obrazu pod tytułem `Postprocessing` wyświetla kolekcję ustawień wstępnych postprocessingu. Przycisk `Nowy` tworzy ustawienie wstępne z bieżących ustawień. Wbudowane ustawienia wstępne można tylko klonować: aby zdefiniować własne, wybierz jedno z nich, kliknij `Klonuj` i wprowadź zmiany. Gdy ustawienie wstępne ma niezapisane zmiany, wyświetla `Niezapisane zmiany!`; aby je zapisać, kliknij obraz ustawienia wstępnego, kliknij ponownie w przeglądarce ustawień wstępnych i wybierz `Zapisz`.

## Pasek skrótów {#shortcut-bar}
Gdy postprocessing jest włączony, pasek na dole menu wymienia wszystkie efekty (`SSR`, `SSGI`, `SSAO`, `DoF`, `Rozświetlenie`...). Stuknij jeden z nich, aby przejść do jego sekcji. Wyłączone efekty są wyszarzone, więc pasek jest też szybkim podsumowaniem tego, co robi bieżące ustawienie wstępne.

## ![](/icons/postprocess_ssr.webp) Odbicie (SSR) {#reflection-ssr}
Dzięki tej opcji obiekty mogą odbijać inne obiekty w scenie, o ile te są widoczne na ekranie.
Jeśli w scenie są metaliczne i błyszczące obiekty, prawdopodobnie warto jej użyć.
Ta opcja wymaga trybu cieniowania [Oświetlony (PBR)](shading.md#pbr).


| SSR wyłączone              | SSR włączone              |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Globalne oświetlenie (SSGI) {#global-illumination-ssgi}

Globalne oświetlenie symuluje odbijanie się światła między powierzchniami, np. czerwona ściana rzuca czerwoną poświatę na pobliski biały obiekt. W połączeniu z okluzją otoczenia i odbiciami może to ogromnie zwiększyć realizm renderu. Podobnie jak odbicia, wymaga trybu cieniowania [Oświetlony (PBR)](shading.md#pbr).

`Siła` - Intensywność globalnego oświetlenia.



| SSGI wyłączone             | SSGI włączone             |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Za kulą znajduje się reflektor skierowany na sufit. Przy wyłączonym SSGI oświetlony jest tylko sufit. Przy włączonym SSGI światło odbija się od sufitu na ściany i na kulę._

## ![](/icons/postprocess_ssao.webp) Okluzja otoczenia (SSAO) {#ambient-occlusion-ssao}
Okluzja otoczenia przyciemnia obszary, do których światło ma mniejsze szanse dotrzeć (narożniki itp.).
Efekt zależy wyłącznie od geometrii modelu.

* `Siła` - Intensywność efektu.
* `Rozmiar` - Zasięg efektu.
* `Grubość` - Jaką grubość w głąb przyjmuje się dla obiektów zasłaniających, jako procent wartości `Rozmiar`.
* `Zabarwienie` - Kolor mnożony z okluzją, do efektów artystycznych.


| SSAO wyłączone              | SSAO włączone              |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
Okluzja otoczenia jest najbardziej widoczna w obszarach oświetlonych głównie światłem otoczenia. Obszary w silnym świetle bezpośrednim otrzymują znacznie słabszy efekt.

:::

## ![](/icons/postprocess_dof.webp) Głębia pola {#depth-of-field-dof}
Dodaje rozmycie w obszarach poza ostrością.

Wystarczy stuknąć model, aby zmienić punkt ostrości.

* `Tryb przysłony` - Steruje rozmyciem za pomocą jednej przysłony aparatu zamiast dwóch suwaków rozmycia poniżej.
* `Przysłona` (_tylko w trybie przysłony_) - Liczba przysłony obiektywu, jak w prawdziwym aparacie. Niższa wartość otwiera obiektyw i mocniej rozmywa.
* `Dalekie rozmycie` - Siła rozmycia stosowanego za punktem ostrości.
* `Bliskie rozmycie` - Siła rozmycia stosowanego między punktem ostrości a kamerą.


| DOF wyłączona             | Ostrość DOF na dalszym pierścieniu | Ostrość DOF na bliższym pierścieniu |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Rozświetlenie {#bloom}
Rozświetlenie (bloom) sprawia, że jasne obszary sceny świecą.

* `Intensywność` - siła efektu.
* `Promień` - Zasięg efektu.
* `Próg` - Jak jasne muszą być piksele w scenie, zanim zaczną świecić. Przy 0 świeci wszystko, a wysoka wartość sprawia, że świecą tylko najjaśniejsze piksele.
* `Zabarwienie` - kolor, który można dodać do rozświetlenia dla efektów artystycznych.

| Rozświetlenie wyłączone      | Rozświetlenie z promieniem 0 | Rozświetlenie z promieniem 1 |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Mapowanie odcienia {#tone-mapping}
Mapowanie odcienia to operacja, która przekształca wartości HDR do zakresu `[0, 1]`.
Jeśli go nie używasz (lub wybierzesz `Brak`), każda składowa koloru większa niż 1 zostanie obcięta.
Wszelkie różnice kolorów powyżej tego zakresu zostaną wtedy utracone.

* `Brak/Neutralne/Agx/ACES` - które mapowanie odcienia zastosować. `Brak` nie przekształca wartości (ale pozostałe ustawienia nadal działają). Pozostałe opcje przypominają wybór różnych klisz fotograficznych: każda inaczej radzi sobie z prześwietlonymi wartościami i kolorami. To bardzo obszerny temat, poszukaj informacji o tone mappingu, Agx i ACES, aby dowiedzieć się więcej!
* `Ekspozycja` - ogólna jasność obrazu, podobnie jak regulacja przysłony w aparacie. To szybki sposób na globalne rozjaśnienie lub przyciemnienie obrazu.
* `Nasycenie` - siła kolorów. 1 to wartość neutralna, 0 to obraz monochromatyczny, a wartości powyżej 1 są coraz bardziej nasycone.
* `Kontrast` - Ciemne partie stają się ciemniejsze, a jasne jaśniejsze. Używaj ostrożnie, bo przy wysokich wartościach może powodować artefakty.

Zauważ, że przy wyłączonym `Mapowanie odcienia` niektóre szczegóły znikają, bo piksele są zbyt jasne.

| Mapowanie odcienia wyłączone | Mapowanie odcienia włączone |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Mapowanie odcienia może wzmocnić efekt globalnego oświetlenia. Jeśli zmniejszysz intensywność mapy otoczenia, a zwiększysz główne źródło światła, możesz podnieść `Ekspozycja` w mapowaniu odcienia, aby lepiej zobaczyć efekty odbitego światła.
:::

## ![](/icons/postprocess_tone_curve.webp) Gradacja kolorów {#color-grading}
Podobnie jak narzędzie krzywych w Photoshopie, pozwala sterować balansem i rozkładem kolorów w obrazie. Ustawienie `Główna` wpływa na cały balans kolorów, a ustawienia `Czerwony`/`Zielony`/`Niebieski` pozwalają na precyzyjną kontrolę.

| Gradacja kolorów wyłączona    | Gradacja kolorów włączona    |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Krzywizna {#curvature}
Wykrywa miejsca, w których krzywizna gwałtownie się zmienia, i nadaje tym obszarom kolor.

* `Współczynnik` - ogólna intensywność efektu
* `Wypukłość` - jak mocno wykrywane są ostre zmiany wypukłe, w których umieszczany jest wybrany kolor (domyślnie biały)
* `Wgłębienie` - jak mocno wykrywane są zmiany wklęsłe, w których umieszczany jest wybrany kolor (domyślnie czarny)
* `Grubość` - jak szerokie są wykryte krawędzie.

Obok `Wypukłość` i `Wgłębienie` próbka koloru pozwala wybrać kolor, a mały przycisk określa, jak ten kolor miesza się z obrazem.


| Krzywizna wyłączona              | Krzywizna włączona             |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberracja chromatyczna {#chromatic-aberration}
Symuluje artefakty obiektywu, w których światło rozszczepia się przy krawędziach ekranu.

* `Siła` - jak mocno czerwona, zielona i niebieska składowa obrazu rozchodzą się w stronę krawędzi ekranu

| Aberracja wyłączona           | Aberracja włączona           |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Winieta {#vignette}
Symuluje artefakty obiektywu, przyciemniając krawędzie ekranu.

* `Rozmiar` - Rozmiar odwróconej elipsy nałożonej na obraz
* `Twardość` - Jak miękko lub ostro elipsa łączy się z obrazem.
* `Zabarwienie` - Kolor winiety, domyślnie czarny.


| Winieta wyłączona               | Winieta włączona               |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Tekstura (ziarno) {#grain}
Dodaje efekt ziarna, dzięki któremu obraz wygląda nieco mniej sztucznie.

* `Siła` - ilość ziarna/szumu dodawanego do obrazu.


| Ziarno wyłączone             | Ziarno włączone            |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Ostrość {#sharpness}
Efekt wyostrzenia podobny do tego z Photoshopa lub aplikacji do obróbki zdjęć.

* `Siła` - siła wyostrzenia stosowanego do obrazu.


| Ostrość wyłączona              | Ostrość włączona             |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Symuluje pixel art ze starych gier. Ten efekt zastępuje [Rozdzielczość renderowania](#resolution-multiplier).

* `Suwak` - rozmiar pikseli
* `Zezwól na próbkowanie klatek` - jeśli pojawia się dużo czarnych pikseli, spróbuj to włączyć. Bez tej opcji efekt pixel art wyłącza [próbkowanie klatek](#max-frame-sampling).

| Piksele wyłączone           | Piksele włączone           |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Linia skanowania {#scanline}
Symuluje wygląd starych monitorów CRT.

* `Współczynnik` - siła linii
* `Odstępy` - rozmiar linii

| Linie skanowania wyłączone     | Linie skanowania włączone     |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
