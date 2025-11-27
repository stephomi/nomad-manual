# ![](/icons/image.webp) Bakgrund

Den här menyn styr bakgrundsfärgen i Nomad, samt eventuella referensbilder som ska användas.

![](/images/background_overview.webp)

## Bakgrund 
![](/images/background_selector.webp)

Det finns tre alternativ för vyfönstrets bakgrund.

* `Environment` - Visar miljökartan som valts i [Shading](shading). Detta kan styras ytterligare med Blur och Exposure (ljusstyrka)-kontrollerna. 
* `Color` - En enfärgad bakgrund som du kan välja själv
* `Gradient` - En färgövergång från topp till botten. Med reglaget Factor kan du bestämma mittpunkten för övergången.  

## Referensbild

![](/images/background_reference.webp)

Du kan lägga till en valfri bild i bakgrunden som ska användas som referens.
Du kan ändra position och skala, till exempel om du vill flytta den till ett hörn av skärmen.

### ![](/icons/tool_transform.webp) Transform 

Den här knappen låter dig placera referensbilden interaktivt. Använd två fingrar för att panorera, skala och rotera referensbilden på plats. Den slutliga placeringen återspeglas i reglagen nedan:

* `Overlay` - vid 0 % kommer referensbilden alltid att ligga bakom dina objekt, vid 100 % ligger den framför. 
* `Opacity` - Hur genomskinlig bilden är.
* `Position` - Bildens X- och Y-position.
* `Rotation` - Bildrotation.
* `Scale` - Bildskala.


::: tip

Kameror och referensbilder är länkade. 

Detta innebär att om du ställer in din referensbild så att den linjerar med din skulpt, och du skapar en kamera från [Camera-menyn](camera), så sparas även referensbildens position, rotation och skala tillsammans med kameran. Du kan stänga av referensbilden, rotera till en annan vy. Om du tittar genom kameran igen aktiveras referensbilden med de inställningar du använde.

Detta inkluderar till och med att välja olika bilder för olika kameror!

 ![](/videos/reference_camera.mp4)

:::
