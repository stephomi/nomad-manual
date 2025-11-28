# ![](/icons/paint.webp) Malowanie {#painting}

Kontroluj kolor, szorstkość, metaliczność pociągnięć pędzla, umożliwiaj zalewanie (flood fill) atrybutów farby oraz sposób, w jaki narzędzia malarskie wchodzą w interakcję z warstwami, maskami i ukrytymi zaznaczeniami.

![](/images/paint_overview.webp)  

## Przegląd {#overview}

Nomad używa wierzchołkowego malowania PBR. Co to oznacza?

### PBR {#pbr}
PBR, czyli Physically Based Rendering, to popularna technika grafiki komputerowej stosowana w filmie, telewizji, grach i na urządzeniach mobilnych. Dzięki opieraniu świateł na właściwościach fizycznych oraz definiowaniu powierzchni poprzez kolor, szorstkość i metaliczność można uzyskać szeroką gamę fotorealistycznych wyglądów.

### Malowanie wierzchołków {#vertex-painting}

Malowanie wierzchołków oznacza, że informacje o farbie są przechowywane w wierzchołkach modelu, a nie w teksturach. Ponieważ Nomad potrafi obsługiwać modele liczące setki tysięcy, a często miliony wierzchołków, Twoje modele mogą mieć bardzo szczegółowe malowanie powierzchni; jeśli możesz wyrzeźbić detal, możesz też go pomalować.

Oznacza to również, że malowanie w Nomadzie nie wymaga mapowania UV, które w innych aplikacjach 3D jest często powolnym i technicznym procesem. Wiele innych aplikacji 3D nie obsługuje tak wysokiej liczby wierzchołków jak Nomad, jednak Nomad ma też dobre narzędzia do wypalania tekstur i dekymacji.

### Teksturowanie {#texturing}

Nomad obsługuje tekstury, ale muszą one być obecne w zaimportowanym modelu lub zostać utworzone poprzez wypalenie malowania wierzchołków do tekstur. 

Tekstura to po prostu obraz, ale w kontekście 3D zazwyczaj odnosi się do obrazu przypisanego do obiektu.
Aby owinąć obraz wokół modelu, model potrzebuje współrzędnych tekstury (UV).

Nomad może [obliczyć je automatycznie](topology.md#uv-unwrap), ale nie masz dużej kontroli nad ogólną jakością.

::: tip
Przykładowy workflow:
- Rzeźb w Nomadzie, następnie wykonaj [UV unwrap](topology.md#uv-unwrap)
- Jeśli zacząłeś już malować w Nomadzie, możesz [przenieść malowanie wierzchołków do tekstur](topology.md#bake-vertex-colors-to-texture)
- Eksport do Procreate
- Teksturowanie w Procreate
- Eksport z powrotem do Nomada w celu renderowania
:::

To był przegląd, teraz przyjrzyjmy się sekcjom menu malowania:


## Malowanie pociągnięć {#stroke-painting}
![](/images/paint_intensity.webp)  

Włącz malowanie dla tego narzędzia, przydatne, jeśli chcesz rzeźbić i malować jednocześnie.

Dla narzędzi, w których malowanie jest główną funkcją (np. Paint, Smudge, Mask), to pole wyboru nie istnieje.

### Intensywność malowania {#paint-intensity}

Suwak pozwalający użyć innej intensywności niż podstawowa intensywność narzędzia.

Pola wyboru `Alpha`, `Falloff` i `Randomize` określają, czy te funkcje będą wpływać na malowanie. Np. możesz mieć włączone randomize dla narzędzia Clay, ale kolor nie będzie losowany.


## Materiał {#material}
![](/images/paint_material.webp) 

Pierwsza ikona to kształt podglądu materiału. Przeciąganie na podglądzie 3D materiału będzie go obracać. 

Druga ikona to podgląd pociągnięcia pędzla z wybranymi opcjami alfy i falloff.

Przycisk podglądu obok tytułu Material pozwala przełączać między none, Material lub Triplanar. Określa to, co się stanie, gdy interaktywnie zmieniasz właściwości farby:

* `None` - Na modelu nie będzie wyświetlany żaden podgląd podczas regulacji właściwości
* `Material` - Wartości materiału będą podglądane na obiekcie podczas regulacji właściwości. Jeśli używasz tekstur i model ma UV, zostaną użyte UV.
* `Triplanar` - Materiał będzie podglądany jako projekcja trójpłaszczyznowa (Triplanar). 

Pipeta może być użyta do pobrania wszystkich właściwości z obiektu w Twojej scenie.

## Presety materiałów {#material-presets}
Stuknięcie w 3D kształt podglądu wyświetli menu presetów materiałów, które można sklonować, aby zdefiniować własne presety.

![](/images/paint_presets.webp) 

Przełączniki `Embed Textures` i `Alpha` po włączeniu zapiszą wszystkie tekstury używane przez ten materiał w presecie. Jest to szerzej wyjaśnione poniżej.

## Suwaki PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

Malowanie [PBR](shading.md#pbr) używa 4 kanałów:
- `Color` Kolor, który będzie malowany. Pipeta może być użyta do wyboru koloru z innych części modelu lub z obrazów referencyjnych.
- `Roughness` Określa, jak „szorstka” lub „gładka” jest powierzchnia. Niska wartość szorstkości oznacza, że odbicia będą ostre.
- `Metalness` Określa po prostu, czy powierzchnia jest metaliczna, czy nie. Wartość powinna być najczęściej albo 0%, albo 100%, wartości pośrednie powinny być wyjątkowe.
- `Opacity` Jak bardzo materiał jest przezroczysty. Ściśle rzecz biorąc, nie jest to część specyfikacji PBR, ale jest użyteczna w wielu sytuacjach. 1 to całkowita nieprzezroczystość, 0 to pełna przezroczystość. Zauważ, że krycie (opacity) i załamanie światła (refraction) to różne rzeczy, załamanie w Nomadzie jest obsługiwane przez materiał refraction. 

Jeśli wybierzesz preset materiału, 3 kanały są malowane jednocześnie (krycie jest często celowo wyłączone). Oznacza to, że zamiast malować tylko „czerwony”, możesz malować „czerwony, szorstki metal” lub „biały, gładki plastik”.

Kwadrat to slot tekstury, kliknij go, aby użyć tekstury dla tej właściwości zamiast stałej wartości.

Ikona pędzla obok suwaków wypełni (flood fill) tę właściwość na całym obiekcie.

Pole wyboru włączy lub wyłączy daną właściwość, więc możesz np. malować tylko kolor albo tylko szorstkość i krycie. 

Oto kilka przykładów różnych właściwości szorstkości i metaliczności:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
W trybie [renderowania Matcap](shading.md#matcap) obsługiwany jest tylko kolor, metaliczność i szorstkość są ignorowane.
:::

::: tip
Podczas używania tekstur do malowania PBR często przydatne jest przełączenie się na narzędzie takie jak `Stamp` lub użycie menu Stroke, aby wybrać tryb inny niż dot, który może rozmazywać teksturę.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Możesz rozważyć włączenie `Smooth Shading` [globalnie](settings.md#smooth-shading) lub [per-obiekt](material.md#smooth-shading), jeśli malujesz metaliczną powierzchnię na obiekcie o niskiej liczbie polygonów.
:::

## Maluj wszystko {#paint-all}

![](/images/paint_paint_all.webp)

Zastosuj bieżący materiał do obiektu, w trybie standardowym za pomocą „Paint All” lub jako projekcję Triplanar.

Pola wyboru obok suwaków color/metalness/roughness/opacity są respektowane, wyłączone właściwości nie zostaną wypełnione.

Dodatkowe przyciski kontrolują, w jaki sposób Paint All może być dalej modyfikowane:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Obszary zamaskowane nie zostaną naruszone.    |
| ![](/icons/tool_hide.webp) | Obszary ukryte nie zostaną naruszone.         |
| ![](/icons/opacity.webp)   | użyj współczynnika malowania narzędzia powyżej. |
| ![](/icons/layer.webp)     | Niepomalowane obszary warstwy nie zostaną naruszone. |
| ![](/icons/triplanar.webp) | Wskaźnik ustawień triplanar                   |
| ![](/icons/cog.webp)       | Otwórz ustawienia Triplanar                   |

### Ustawienia trójpłaszczyznowe {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Podobnie jak w [ustawieniach triplanar w menu materiału](material.md#triplanar), możesz kontrolować mieszanie projekcji, tiling i przesunięcia. 

Użyj pola podglądu na górze tego menu, aby włączyć trwały podgląd podczas regulacji wartości.

## Materiał globalny {#global-material}
Jeśli ta opcja jest włączona, wybrany materiał będzie taki sam jak w innych narzędziach. Zauważ, że brane są pod uwagę tylko ustawienia szorstkości, metaliczności i koloru.