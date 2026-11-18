# ![](/icons/image.webp) Tło {#background}

To menu ustala kolor tła w Nomadzie, a także obrazy referencyjne, z których chcesz korzystać.

![](/images/background_overview.webp)

## Typ {#type}
![](/images/background_selector.webp)

Tło widoku może być jednego z trzech rodzajów.

* `Środowisko` - Pokazuje mapę otoczenia wybraną w menu [Cieniowanie](shading.md). Możesz ją dodatkowo regulować suwakami `Rozmycie` i `Ekspozycja` (jasność).
* `Kolor` - Jednolity kolor, który wybierasz sam.
* `Gradient` - Przejście między dwoma kolorami. Suwak `Współczynnik` przesuwa środek gradientu.

### Rodzaj gradientu {#gradient-type}
Przy opcji `Gradient` wybierasz jego kształt:
* `Liniowy` - Prosty gradient, którego kierunek ustawia suwak `Kąt`.
* `Promieniowy` - Okrągły gradient rozchodzący się od środka ekranu.
* `Niebo` - Gradient zaczepiony o horyzont świata, więc podąża za kamerą, gdy patrzysz w górę i w dół.

Każdy kolor ma przycisk resetu i pipetę, za pomocą której pobierzesz kolor z ekranu.

## ![](/icons/lock.webp) Synchronizuj z blokadą kamery {#sync-on-camera-lock}
Gdy kamera jest zablokowana [Nawigatorem](settings.md#snap-cube), obraz referencyjny podąża za ruchem kamery, dzięki czemu pozostaje dopasowany do rzeźby.

* `Zezwól na obrót` (trackball) - Pozwala kamerze się przechylać po wyjściu z blokady kamery.
* `Reset widoku przy odblokowaniu` - Resetuje widok po wyjściu z blokady kamery.

## Obraz referencyjny {#reference}

![](/images/background_reference.webp)

Możesz dodać w tle dowolny obraz, który posłuży ci za referencję. Stuknij `Importuj...`, aby go dodać, a potem zaznacz `Obraz referencyjny`, żeby go pokazać.
Możesz zmienić jego pozycję i skalę, na przykład gdy chcesz go przesunąć w róg ekranu.

### ![](/icons/tool_transform.webp) Przekształcenie {#transform}

Ten przycisk pozwala ustawić obraz referencyjny interaktywnie. Dwoma palcami przesuwasz, skalujesz i obracasz obraz, aż znajdzie się na miejscu. `Resetuj ustawienia` przywraca domyślne położenie obrazu. Końcowe ustawienie widać na suwakach poniżej:

* `Nakładka` - Przy 0% obraz referencyjny jest zawsze za obiektami, przy 100% przed nimi.
* `Krycie` - Jak bardzo przezroczysty jest obraz.
* `Postprocessing` - Stosuje efekty postprocessingu również do obrazu referencyjnego. Wyłącz, aby zachować oryginalne kolory.
* `Pozycja X` / `Pozycja Y` - Położenie obrazu w poziomie i w pionie.
* `Skala` - Skala obrazu.
* `Obrót` - Obrót obrazu.


::: tip

Kamery i obrazy referencyjne są ze sobą powiązane.

Jeśli więc ustawisz obraz referencyjny tak, by pasował do rzeźby, a potem utworzysz kamerę w [menu Kamera](camera.md), pozycja, obrót i skala obrazu referencyjnego zostaną zapisane razem z kamerą. Możesz wtedy wyłączyć obraz referencyjny i obrócić widok gdzie indziej. Gdy znów spojrzysz przez tę kamerę, obraz referencyjny włączy się z ustawieniami, których użyłeś.

Możesz nawet wybrać różne obrazy dla różnych kamer!

 ![](/videos/reference_camera.mp4)

:::
