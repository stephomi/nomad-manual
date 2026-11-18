# ![](/icons/image.webp) Bakgrund {#background}

I den här menyn styr du Nomads bakgrundsfärg och de referensbilder du vill använda.

![](/images/background_overview.webp)

## Typ {#type}
![](/images/background_selector.webp)

Det finns tre alternativ för vyns bakgrund.

* `Miljö` - Visar den miljökarta som är vald under [Skuggning](shading.md). Du kan finjustera den med reglagen `Oskärpa` och `Exponering` (ljusstyrka).
* `Färg` - En enfärgad bakgrund i valfri färg
* `Gradient` - En övergång mellan två färger. Med reglaget `Faktor` flyttar du gradientens mittpunkt.

### Gradienttyp {#gradient-type}
Med `Gradient` väljer du dess form:
* `Linjär` - En rak gradient, vars riktning du ställer in med reglaget `Vinkel`.
* `Radiell` - En cirkulär gradient som utgår från skärmens mitt.
* `Himmel` - En gradient som är förankrad i världens horisont, så den följer kameran när du tittar upp och ner.

Varje färg har en återställningsknapp och en färgväljare, så att du kan hämta en färg direkt från skärmen.

## ![](/icons/lock.webp) Synka med kameralås {#sync-on-camera-lock}
När kameran är låst med [Navigatorn](settings.md#snap-cube) följer referensbilden kamerans rörelser, så att den hela tiden ligger i linje med din skulptur.

* `Tillåt rullning (Trackball)` - Låter kameran rulla när du lämnar kameralåset.
* `Återställ vy vid upplåsning` - Återställer vyn när du lämnar kameralåset.

## Referensbild {#reference}

![](/images/background_reference.webp)

Du kan lägga in valfri bild i bakgrunden att använda som referens. Tryck på `Importera...` för att lägga till en, och kryssa sedan i `Referensbild` för att visa den.
Du kan ändra position och skala, till exempel om du vill flytta bilden till ett hörn av skärmen.

### ![](/icons/tool_transform.webp) Transformera {#transform}

Med den här knappen placerar du referensbilden interaktivt. Använd två fingrar för att panorera, skala och rotera bilden på plats. `Återställ inställningar` flyttar tillbaka bilden till dess ursprungliga placering. Den slutliga placeringen syns i reglagen nedan:

* `Överlagring` - Vid 0 % ligger referensbilden alltid bakom dina objekt, vid 100 % ligger den framför.
* `Opacitet` - Hur genomskinlig bilden är.
* `Efterbehandling` - Tillämpar efterbehandlingseffekterna på referensbilden. Stäng av det för att behålla originalfärgerna.
* `Position X` / `Position Y` - Bildens X- och Y-position.
* `Skala` - Bildens skala.
* `Rotation` - Bildens rotation.


::: tip

Kameror och referensbilder hör ihop.

Det betyder att om du har ställt in referensbilden så att den ligger i linje med din skulptur och sedan skapar en kamera från [Kamera-menyn](camera.md), så sparas referensbildens position, rotation och skala tillsammans med kameran. Du kan stänga av referensbilden och rotera till en annan vy. När du tittar genom kameran igen aktiveras referensbilden med de inställningar du använde.

Du kan till och med välja olika bilder för olika kameror!

 ![](/videos/reference_camera.mp4)

:::
