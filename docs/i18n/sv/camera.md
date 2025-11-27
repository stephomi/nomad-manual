# ![](/icons/camera.webp) Kamera

Den här menyn låter dig skapa och ändra kameror, samt styra hur du interagerar med kameror.

![](/images/camera_overview2.webp)

Kameror i Nomad har flera användningsområden:

* Ställa in vyer för skulptering från precisa vinklar
* Användas som en fotokamera för att komponera dina objekt
* som en förstapersonskamera för att navigera i din scen
* som en ortografisk kamera för isometriska spel eller rendering i industriell stil.

## Styra kameran

### Rotation
Du roterar kameran genom att dra *ett* finger på bakgrunden.
Om du drar fingret på din modell startar du istället skulpteringsåtgärden.

::: tip Kan jag rotera kameran om jag inte kommer åt bakgrunden?
Ja, du kan lägga *två* fingrar på skärmen – som om du ville starta en panorerings-/zoomgest – och sedan släppa *ett* finger.
:::

### Fokus / Återställ
*Dubbeltryck* på modellen för att fokusera den punkt du valt.
Om du *dubbeltrycker* på bakgrunden kommer kameran istället att fokusera på det valda meshet.


### Förflyttning
Genom att flytta *två* fingrar kan du panorera kameran.


### Zoomning
Genom att använda nypgesten kan du zooma in/ut.


### Rullning
Du kan *rulla* vyn genom att rotera *två* fingrar.
::: warning
Den här gesten är endast tillgänglig för rotationsläget `trackball`.
:::

### Skrivbordskontroller

På skrivbord används alt/opt-tangenten för att styra kameran:

* tip dra i tomt utrymme = rotera kamera
* alt+tip dra = panorera
* alt+tip dra, släpp sedan alt = zooma (samma som i ZBrush)

Med Wacom-ritplattor som har 2 eller fler knappar på pennan, använd Wacom-inställningarna för att konfigurera spets och knappar så här:

* spets = vänsterklick
* nedre vippa = mittenklick
* övre vippa = högerklick

Med dessa inställningar kan du manipulera kameran enbart med pennan:

* övre vippa och hovra-rörelse = rotera kamera
* nedre vippa och hovra-rörelse = panorera

## Kamerakontroller

![](/images/camera_list.webp)

### Vyer
Du kan spara kamerapositioner genom att använda `Add View`.
Om du klickar på vynamnet kommer kameran att återställa vyn.


::: tip
En sparad vy kommer att spara inställningarna för [Projection Type](#projection-type) och även [Reference image](background.md).  
Det kan vara användbart om du vill växla mellan fram-/vänster-/bakre referensvyer med olika bakgrunder.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Toggle the camera. Hidden cameras will be skipped from previous/next button |
| Name        |                               | Select the camera                                                           |
| Image       | ![](/icons/image.webp)       | A thumbnail of a reference image if it is linked to the camera              |
| Update View | ![](/icons/update_view.webp) | Update the saved view with the current view point                           |
| Edit Name   | ![](/icons/pencil.webp)      | Edit the camera name                                                        |
| Delete      | ![](/icons/trash.webp)       | Delete the camera                                                           |

### ![](/icons/tool_view.webp) Add View
Skapa en ny kamera baserad på den aktuella vyn.

### ![](/icons/camera.webp) Icons

Växla om kameraikoner är synliga i vyn. Om en kamera är vald är dess ikon alltid synlig.

### Projection Type
Du kan ändra `Field of View` (FOV / brännvidd) för din kamera.
Det rekommenderas vanligtvis att använda låg FOV för skulpteringsändamål, eftersom det kan hjälpa med proportioner.  
Du kan också använda läget `Orthographic`, som mer eller mindre motsvarar en FOV lika med 0

### First Person
Aktivera så att pivotpunkten sätts direkt på kameran istället för på skulpturen. Att dra ett finger på bakgrunden kommer att hålla kamerapositionen låst men ändra rotationen, liknande hur förstapersonsspel fungerar. Användbart när du skulpterar miljöer snarare än enstaka objekt.

![](/images/camera_rotation_ortho_view.webp)

### Rotation Type
Som standard använder kameran rotationsläget `Turntable`.
Det betyder att du bara har två frihetsgrader, det är mer intuitivt men i vissa fall vill du ha mer flexibilitet.  
Du kan växla till `Trackball`, då kan du *rulla* vyn genom att rotera *två* fingrar i vyn. På skrivbord finns ett alternativt trackball-läge som kan kännas mer bekant för vissa användare.

### Orthographic snap

När detta är aktiverat, om du har ett tangentbord och håller ned shift medan du roterar vyn, kommer kameran att snäppa till närmaste fram-/bak-/topp-/botten-/vänster-/höger-vy och göra kameran ortografisk. Kameran kommer också att göras ortografisk när vykuben klickas för att snäppa till fram/bak/vänster/höger/topp/botten.

### Reset view

Flytta kameran till frontvy och anpassa scenen så att den passar i vyn

### Snap view
Snäpp till närmaste fram-/bak-/vänster-/höger-/topp-/botten-vy. Om du redan är i en av dessa vyer kommer ett nytt klick att snäppa 180 grader till motsatt sida.

### Speed

Om du tycker att kameran rör sig för långsamt eller för snabbt kan du ställa in en hastighetsmultiplikator för `rotation`, `translation` och `zooming`. Användbart om din skulpt är väldigt stor eller väldigt liten.

### Pivot overview

När du roterar kameran kan du se en liten rosa prick, detta är din kamerapivotpunkt.  
Det är väldigt viktigt att förstå var din pivot är så att du inte går vilse eller blir frustrerad av kameran.

Som standard uppdateras pivotpunkten genom dessa åtgärder:
- dubbeltryck på modellen
- dubbeltryck på bakgrunden (den nya pivotpunkten kommer att vara i mitten av ditt mesh)
- att lägga *två* fingrar på skärmen (panorera/zooma/rulla) uppdaterar pivotpunkten till mitten av de *två* fingrarna

### Update Pivot...

Du kan ytterligare anpassa hur pivotpunkten uppdateras med dessa alternativ:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
När du har vant dig kan du dölja den (hint) rosa pricken om du går in i menyn [Settings](settings.md).
:::

### Double tap on object
När `Focus` är aktiverat kommer dubbeltryck att flytta pivotpunkten till det objekt du tryckte på.

### Double tap on background
När detta är aktiverat ställs pivotpunkten in till antingen Selection, Scene eller växlar mellan dem.
