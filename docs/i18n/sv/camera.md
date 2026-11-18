# ![](/icons/camera.webp) Kamera {#camera}

I den här menyn skapar och ändrar du kameror, och styr hur du interagerar med kameran.

![](/images/camera_overview2.webp)

Kameror i Nomad har flera användningsområden:

* Ställa in vyer för att skulptera från exakta vinklar
* Används som en fotokamera för att rama in dina objekt
* som en förstapersonskamera för att röra dig genom scenen
* som en ortografisk kamera för isometriska spel eller rendering i industriell stil.

## Styra kameran {#control}

### Rotation {#rotation}
Du roterar kameran genom att dra med *ett* finger på bakgrunden.
Om du drar fingret på modellen börjar du i stället skulptera.

::: tip Kan jag rotera kameran om jag inte kommer åt bakgrunden?
Ja, du kan sätta *två* fingrar på skärmen - som om du ville panorera/zooma - och sedan släppa *ett* finger.
:::

### Fokusera / Återställ {#focus}
*Dubbeltryck* på modellen för att fokusera på den punkten.
Om du *dubbeltrycker* på bakgrunden fokuserar kameran i stället på det valda nätet eller hela scenen, se [Dubbeltryck på bakgrunden](#dtap-tap-background).


### Förflyttning {#translation}
Genom att röra *två* fingrar kan du panorera kameran.


### Zoomning {#zooming}
Med nypgesten zoomar du in och ut.


### Rullning {#rolling}
Du kan *rulla* vyn genom att vrida *två* fingrar.
::: warning
Den här gesten är bara tillgänglig i rotationslägena `Trackball`.
:::

### Datorkontroller {#desktop}

På datorn används alt/opt-tangenten för att styra kameran:

* dra med spetsen på tom yta = rotera kameran
* alt+dra med spetsen = panorera
* alt+dra med spetsen, släpp sedan alt = zooma (som i zbrush)

Med Wacom-plattor som har 2 eller fler knappar på pennan kan du ställa in spets och knappar så här i Wacoms inställningar:

* spets = vänsterklick
* nedre vippknapp = mittenklick
* övre vippknapp = högerklick

Med de inställningarna kan du styra kameran helt med pennan:

* övre vippknapp och svävande rörelse = rotera kameran
* nedre vippknapp och svävande rörelse = panorera

## Kamerakontroller {#camera-controls}

![](/images/camera_list.webp)

### Vyer {#views}
Du kan spara kameravyer med `Lägg till visning`.
Om du klickar på vyns namn återställer kameran den vyn.


::: tip
En sparad vy sparar inställningarna för [Projektionstyp](#projection) och även [Referensbilden](background.md).  
Det kan vara användbart om du vill växla mellan referensvyer framifrån/från vänster/bakifrån med olika bakgrunder.
:::

| Åtgärd      | Ikon                          | Beskrivning                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Synlighet   | ![](/icons/eye_open.webp)    | Slå på/av kameran. Dolda kameror hoppas över av knapparna föregående/nästa |
| Namn        |                               | Välj kameran                                                                |
| Bild        | ![](/icons/image.webp)       | En miniatyr av referensbilden, om en är länkad till kameran                 |
| Projektion  | ![](/icons/perspective.webp) | Kamerans projektion, med dess synfält när den är i perspektiv               |
| Uppdatera vy | ![](/icons/update_view.webp) | Uppdatera den sparade vyn med den aktuella vyn                             |
| Redigera namn | ![](/icons/pencil.webp)    | Redigera kamerans namn                                                      |
| Radera      | ![](/icons/trash.webp)       | Radera kameran                                                              |

### ![](/icons/camera_add.webp) Lägg till visning {#add}
Skapa en ny kamera utifrån den aktuella vyn.

### ![](/icons/camera.webp) Ikoner {#icons-test}

Bestämmer om kameraikonerna syns i vyn. Knappen visas bredvid `Lägg till visning` när du har en kamera. Om en kamera är vald syns dess ikon alltid.

### Projektionstyp {#projection}
Välj mellan `Perspektiv` och `Ortografisk`.

I perspektiv kan du ändra kamerans `Vertikal Fov` (synfält). Motsvarande brännvidd för en 35mm-kamera visas ovanför reglaget, praktiskt om du är van vid fotografering.
Ett lågt synfält rekommenderas oftast när du skulpterar, eftersom det hjälper dig att bedöma proportionerna.  
Läget `Ortografisk` motsvarar ungefär ett synfält lika med 0.

### Första person {#fps}
Bara i perspektiv. Placerar pivoten direkt på kameran i stället för på skulpturen. När du drar med ett finger på bakgrunden står kamerans position still men rotationen ändras, ungefär som i förstapersonsspel. Användbart när du skulpterar miljöer snarare än enstaka objekt.

![](/images/camera_rotation_ortho_view.webp)

### Rotationstyp {#rotation-type}
Som standard använder kameran rotationsläget `Vändskiva`.
Det betyder att du bara har två frihetsgrader; det är mer intuitivt, men ibland vill du ha mer flexibilitet.  
Du kan byta till `Trackball`, då kan du *rulla* vyn genom att vrida *två* fingrar i vyn. Det finns två `Trackball`-lägen: det första rullar vyn som en boll under fingret, medan det andra (med pilikonen) vrider vyn utifrån den vågräta och lodräta rörelsen i ditt drag, vilket kan kännas mer bekant för vissa användare.

### Ortografisk fast {#orthographic}

När den är aktiverad och du har ett tangentbord fäster kameran mot närmaste vy framifrån/bakifrån/ovanifrån/underifrån/från vänster/från höger om du håller ned shift medan du roterar vyn, och kameran blir ortografisk. Kameran blir också ortografisk när du klickar på navigatorn för att fästa mot fram/bak/vänster/höger/ovan/under.

### Återställ vy {#reset}

Flytta kameran framåt och få in hela scenen i vyn

### Fäst vy {#snap}
Fäster mot närmaste vy framifrån/bakifrån/från vänster/från höger/ovanifrån/underifrån. Om du redan är i en av de vyerna fäster ett nytt klick 180 grader mot motsatt sida.

### Hastighet {#speed}

Om du tycker att kameran rör sig för långsamt eller för snabbt kan du ställa in en hastighetsmultiplikator för `Rotation`, `Zoomning` och `Förflyttning`. Användbart om din skulptur är väldigt stor eller väldigt liten.

### Översikt över pivoten {#pivot}

När du roterar kameran ser du en liten rosa prick, det är kamerans pivotpunkt.  
Det är väldigt viktigt att förstå var pivoten är, så att du inte går vilse eller blir frustrerad av kameran.

Som standard uppdateras pivoten av följande:
- dubbeltryck på modellen
- dubbeltryck på bakgrunden (den nya pivoten hamnar i mitten av ditt nät)
- att sätta *två* fingrar på skärmen (panorera/zooma/rulla) lägger pivoten i mitten mellan de *två* fingrarna

### Uppdatera pivot... {#update-pivot}

Du kan anpassa när pivoten uppdateras ytterligare med de här alternativen:

* `När kameran börjar röra sig` - Uppdatera pivoten när du börjar interagera med kameran.
* `Tillåt pivot utanför objekt` - Tillåt en ny pivot även när du zoomar utanför objektets yta. Kräver `När kameran börjar röra sig`.
* `När dubbeltryck utförs` - Uppdatera rotationspivoten när du dubbeltrycker på objektets yta.
* `Skulptera (Penseldrag)` - Uppdatera pivoten när du skulpterar.

::: tip
När du har vant dig kan du dölja den rosa (hjälp)pricken i menyerna under [Inställningar](settings.md).
:::

### Centrera vy när man zoomar ut {#center-view-when-zooming-out}
När du zoomar ut panorerar kameran inte i sidled: den rör sig bara bakåt, så vyn förblir centrerad.

### Dubbeltryck på objektet {#dtap-object}
När det är aktiverat fokuserar kameran på den punkt du dubbeltrycker på ett objekt.

### Dubbeltryck på bakgrunden {#dtap-tap-background}
När det är aktiverat fokuserar kameran, när du dubbeltrycker på bakgrunden, på:
* `Val` - De valda objekten.
* `Scen` - Hela scenen.
* `Växla` - Växlar mellan de två vid varje dubbeltryck. Det finns två `Växla`-alternativ, de skiljer sig i vilket som kommer först, som deras ikoner visar.
