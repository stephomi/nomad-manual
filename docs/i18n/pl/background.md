# ![](/icons/image.webp) Tło

To menu kontroluje kolor tła Nomada, a także wszelkie obrazy referencyjne, które mają być używane.

![](/images/background_overview.webp)

## Tło
![](/images/background_selector.webp)

Istnieją trzy opcje tła widoku.

* `Environment` - Pokazuje mapę otoczenia wybraną w [Shading](shading). Może być dodatkowo kontrolowana za pomocą rozmycia (Blur) i ekspozycji (Exposure – jasność).
* `Color` - Jednolity kolor, który możesz wybrać.
* `Gradient` - Przejście koloru z góry na dół. Suwak Factor pozwala określić punkt środkowy gradientu.  

## Obraz referencyjny

![](/images/background_reference.webp)

Możesz dodać wybrany przez siebie obraz w tle, aby używać go jako referencji.
Możesz zmieniać jego pozycję i skalę, na przykład jeśli chcesz przenieść go do rogu ekranu.

### ![](/icons/tool_transform.webp) Transform 

Ten przycisk pozwala interaktywnie umieścić obraz referencyjny. Użyj 2 palców, aby przesuwać, skalować i obracać obraz referencyjny. Końcowe położenie zostanie odzwierciedlone w suwakach poniżej:

* `Overlay` - przy 0% obraz referencyjny będzie zawsze za obiektami, przy 100% jest przed nimi.
* `Opacity` - Jak bardzo przezroczysty jest obraz.
* `Position` - Pozycja X i Y obrazu.
* `Rotation` - Obrót obrazu.
* `Scale` - Skala obrazu.


::: tip

Kamery i obrazy referencyjne są ze sobą powiązane. 

Oznacza to, że jeśli ustawisz obraz referencyjny tak, aby pokrywał się z rzeźbą, a następnie utworzysz kamerę z [Camera menu](camera), pozycja, obrót i skala obrazu referencyjnego zostaną również zapisane z kamerą. Możesz wyłączyć obraz referencyjny, obrócić się do innego widoku. Jeśli ponownie spojrzysz przez kamerę, obraz referencyjny zostanie aktywowany z użytymi wcześniej ustawieniami.

Dotyczy to nawet wybierania różnych obrazów dla różnych kamer!

 ![](/videos/reference_camera.mp4)

:::
