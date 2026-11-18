# ![](/icons/paint.webp) Malowanie {#painting}

Określa kolor, chropowatość i metaliczność pociągnięć farby, pozwala wypełniać obiekt atrybutami malowania i decyduje, jak narzędzia malarskie współpracują z warstwami, maskami i ukrytymi obszarami.

![](/images/paint_overview.webp)  

## Przegląd {#overview}

Nomad używa malowania wierzchołków PBR. Co to oznacza?

### PBR {#pbr}
PBR (Physically Based Rendering, czyli renderowanie oparte na fizyce) to popularna technika grafiki komputerowej, stosowana w filmie, telewizji, grach i na urządzeniach mobilnych. Dzięki oparciu świateł na właściwościach fizycznych i opisaniu powierzchni kolorem, chropowatością i metalicznością można uzyskać bardzo wiele fotorealistycznych wyglądów.

### Malowanie wierzchołków {#vertex-painting}

Malowanie wierzchołków oznacza, że informacje o malowaniu są zapisywane w wierzchołkach modelu, a nie w teksturach. Nomad radzi sobie z modelami o setkach tysięcy, a często milionach wierzchołków, więc Twoje modele mogą mieć bardzo szczegółowe malowanie powierzchni: jeśli potrafisz wyrzeźbić dany szczegół, możesz go też pomalować.

Oznacza to również, że malowanie w Nomad nie wymaga mapowania UV, które w innych aplikacjach 3d bywa powolnym i technicznym procesem. Wiele innych aplikacji 3d nie obsługuje tak dużej liczby wierzchołków jak Nomad, ale Nomad ma też dobre narzędzia do wypalania tekstur i upraszczania, które w tym pomagają.

### Teksturowanie {#texturing}

Nomad obsługuje tekstury, ale muszą one pochodzić z importowanego modelu albo z wypalenia malowania wierzchołków do tekstur.

Tekstura to po prostu obraz, ale w kontekście 3d zwykle oznacza obraz przypisany do obiektu.
Aby owinąć obraz wokół modelu, model potrzebuje współrzędnych tekstury (UV).

Nomad potrafi [obliczyć je automatycznie](topology.md#uv-unwrap), ale nie masz wtedy dużego wpływu na ogólną jakość.

::: tip
Przykładowy sposób pracy:
- Rzeźbisz w Nomad, a potem robisz [rozwijanie UV](topology.md#uv-unwrap)
- Jeśli zacząłeś już malować w Nomad, możesz [przenieść malowanie wierzchołków do tekstur](topology.md#bake-texture)
- Eksportujesz do Procreate
- Teksturujesz w Procreate
- Eksportujesz z powrotem do Nomad, aby wyrenderować
:::

To tyle tytułem wstępu, przyjrzyjmy się teraz sekcjom menu malowania:


## Malowanie pociągnięciami {#stroke-painting}
![](/images/paint_intensity.webp)  

Włącza malowanie dla tego narzędzia, co przydaje się, gdy chcesz jednocześnie rzeźbić i malować. Gdy narzędzie potrafi malować, ale to pole jest wyłączone, przypomina o tym ikona ostrzeżenia obok tytułu.

W narzędziach, których główną funkcją jest malowanie (np. Farba, Smużenie, Maska), tego pola wyboru nie ma.

### ![](/icons/opacity.webp) Intensywność farby {#paint-intensity}

Suwak, który pozwala użyć innej intensywności niż główna intensywność narzędzia.

Przycisk z suwakami obok niego dodaje do paska bocznego szybki suwak intensywności farby, w narzędziach, które jednocześnie rzeźbią i malują.

Przyciski `Alfa`, `Zanikanie` i `Zrandomizuj intensywność` określają, czy te funkcje wpływają na malowanie. Możesz na przykład włączyć losowość dla narzędzia Glina, a kolor nie będzie losowany.

* `Alfa` - gdy jest wyłączona, malowanie ignoruje alfę i pokrywa cały obszar pędzla. W narzędziu VDM ten przycisk zastępuje `Materiał stempla`, który włącza lub wyłącza materiał zapisany w stemplu.
* `Zanikanie` - gdy jest wyłączone, malowanie ma pełną intensywność aż do krawędzi pędzla.
* `Zrandomizuj intensywność` - czy losowość intensywności z randomizera pociągnięcia wpływa na malowanie. Losowość położenia, obrotu i skali zawsze przesuwa cały stempel.

Te opcje są ignorowane przez [Maluj wszystko](#paint-all), ale jego wariant trzypłaszczyznowy używa alfy.

### ![](/icons/link.webp) Materiał globalny {#global-material}
Jeśli ta opcja jest włączona, wybrany materiał jest taki sam jak w pozostałych narzędziach. Uwzględnia ona tylko ustawienia chropowatości, metaliczności i koloru. Wyłącz ją, aby nadać temu narzędziu własny materiał.


## Materiał {#material}
![](/images/paint_material.webp) 

Pierwsza ikona to kształt podglądu materiału. Przeciąganie po podglądzie materiału 3d obraca go.

Druga ikona to podgląd pociągnięcia farby z wybraną alfą i opcjami zanikania.

### ![](/icons/falloff.webp) Krzywe {#curves}

Otwiera edytor krzywych dla gniazd tekstur [suwaków PBR](#pbr-sliders). Przekształca wartości tekstury przed ich namalowaniem, nie zmieniając pliku obrazu. Mała ikona krzywej na gnieździe tekstury informuje, że jego krzywa została zmieniona.

### ![](/icons/cog.webp) Opcje materiału {#material-options}

Przycisk `Materiał` obok tytułu zawiera dwa ustawienia.

`Podgląd materiału w widoku` określa, co dzieje się na zaznaczonym obiekcie, gdy zmieniasz suwaki koloru, chropowatości, metaliczności, krycia i intensywności:

* `Brak` - Podczas zmiany właściwości na modelu nie jest wyświetlany żaden podgląd.
* `Materiał` - Podczas zmiany właściwości wartości materiału są wyświetlane na obiekcie.
* `Trzypłaszczyznowy` - Podgląd materiału jest wyświetlany jako projekcja trzypłaszczyznowa.

Pola wyboru koloru, chropowatości, metaliczności i krycia poniżej określają, które kanały zastępuje [Próbnik materiału](#material-picker).

### ![](/icons/dropper.webp) Próbnik materiału {#material-picker}

Pipeta pobiera materiał spod kursora, z dowolnego obiektu w scenie. Zastępowane są tylko kanały zaznaczone w [Opcjach materiału](#material-options).

## Ustawienia wstępne materiałów {#material-presets}
Stuknięcie kształtu podglądu 3d otwiera menu ustawień wstępnych materiałów, które możesz klonować, aby tworzyć własne ustawienia wstępne.

![](/images/paint_presets.webp) 

Przełącznik `Osadź tekstury` zapisuje kopię tekstur używanych przez ten materiał wewnątrz ustawienia wstępnego. Bez niego ustawienie wstępne tylko odwołuje się do tekstur w folderze textures/ Nomad. Włącz go, gdy chcesz udostępnić ustawienie wstępne z teksturami bez osobnego wysyłania tekstur.

`Uwzględnij alfę` zapisuje w ustawieniu wstępnym materiału także alfę pędzla.

## Suwaki PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

Malowanie [PBR](shading.md#pbr) używa 4 kanałów:
- `Kolor` Kolor, który zostanie namalowany. Pipetą możesz pobrać kolor z innych części modelu albo z obrazów referencyjnych.
- `Chropowatość` Określa, jak „szorstka” lub „gładka” jest powierzchnia. Niska wartość chropowatości oznacza ostre odbicia.
- `Metaliczność` Po prostu określa, czy powierzchnia jest metaliczna, czy nie. W większości przypadków wartość powinna wynosić 0% albo 100%, a wartości pośrednie powinny być wyjątkiem.
- `Krycie` Na ile materiał jest prześwitujący. Ściśle mówiąc, nie należy ono do specyfikacji PBR, ale przydaje się w wielu sytuacjach. 1 to pełne krycie, 0 to przezroczystość. Pamiętaj, że krycie i refrakcja to różne rzeczy: refrakcję w Nomad obsługuje materiał refrakcyjny.

Jeśli wybierzesz ustawienie wstępne materiału, 3 kanały są malowane jednocześnie (krycie jest często celowo pomijane). Dzięki temu zamiast malować po prostu „czerwienią”, możesz malować „czerwonym, szorstkim metalem” albo „białym, gładkim plastikiem”.

Kwadrat to gniazdo tekstury: kliknij je, aby dla tej właściwości użyć tekstury zamiast jednolitej wartości. Tekstura koloru zabarwia kolor, a tekstura chropowatości, metaliczności lub krycia zastępuje wartość suwaka (jego etykieta jest wtedy przekreślona). W przypadku tekstury krycia `Użyj alfy jako wartości` odczytuje kanał alfa tekstury zamiast jej wartości w skali szarości.

W narzędziu VDM, gdy stempel ma własny materiał, obok gniazda tekstury pojawia się dodatkowe gniazdo, które go pokazuje. Stuknij je, aby użyć tego kanału stempla lub go zignorować.

Ikona pędzla obok suwaków wypełnia daną właściwością cały obiekt.

Pole wyboru włącza lub wyłącza daną właściwość, więc możesz na przykład malować tylko kolor albo tylko chropowatość i krycie.

Oto kilka przykładów różnych wartości chropowatości i metaliczności:

|                | Metaliczność 0%                   | Metaliczność 100%            |
| :------------: | :-------------------------------: | :--------------------------: |
| Chropowatość 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Chropowatość 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Chropowatość 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Chropowatość i metaliczność wymagają trybu cieniowania [Oświetlony (PBR)](shading.md#pbr). W trybie [MatCap](shading.md#matcap) lub [Nieoświetlony](shading.md#unlit) są ignorowane, a menu wyświetla ostrzeżenie.
:::

::: tip
Przy malowaniu PBR teksturami często warto przełączyć się na narzędzie takie jak `Stempel` albo w menu pociągnięcia wybrać tryb inny niż kropka, który może rozmazywać teksturę.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Rozważ włączenie `Płynne cieniowanie` [globalnie](settings.md#smooth-shading) lub [dla obiektu](material.md#smooth-shading), jeśli malujesz metaliczną powierzchnię na obiekcie o mniejszej liczbie wielokątów.
:::

## ![](/icons/paint.webp) Maluj wszystko {#paint-all}

![](/images/paint_paint_all.webp)

Stosuje bieżący materiał do zaznaczonych obiektów, w trybie standardowym przyciskiem `Maluj wszystko` albo jako projekcję trzypłaszczyznową przyciskiem `Maluj wszystko + Trzypłaszczyznowy`. Wariant trzypłaszczyznowy nie jest dostępny dla niezatwierdzonych prymitywów.

Pola wyboru obok suwaków koloru, metaliczności, chropowatości i krycia są respektowane: wyłączone właściwości nie zostaną wypełnione.

Dodatkowe przyciski określają, co jeszcze wpływa na działanie Maluj wszystko. Większość z nich pokazuje wartość procentową i jest wyszarzona, gdy nie miałaby żadnego efektu:

| Ikona                       | Opis                                          |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Zamaskowane obszary pozostają nietknięte.     |
| ![](/icons/tool_hide.webp) | Ukryte obszary pozostają nietknięte.          |
| ![](/icons/opacity.webp)   | Używa powyższego współczynnika malowania narzędzia. |
| ![](/icons/layer.webp)     | Niepomalowane obszary warstwy pozostają nietknięte. |
| ![](/icons/triplanar.webp) | `Wierzchołek`: wariant trzypłaszczyznowy dodatkowo przesuwa powierzchnię zgodnie z alfą, o pokazaną intensywność narzędzia. |
| ![](/icons/cog.webp)       | Otwiera ustawienia trzypłaszczyznowe          |

### ![](/icons/cog.webp) Ustawienia trzypłaszczyznowe {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Podobnie jak w [ustawieniach trzypłaszczyznowych w menu materiału](material.md#triplanar), możesz sterować mieszaniem projekcji, kafelkowaniem i przesunięciami.

Pole wyboru podglądu u góry tego menu włącza stały podgląd podczas zmiany wartości.
