# ![](/icons/sun.webp) Skuggning {#shading}

Den här menyn styr Nomads skuggningslägen, ljusens egenskaper, miljön och matcap samt dimman.

![](/images/shading_overview.webp)



Du kan välja mellan flera renderingslägen:

| Läge                        | Betydelse                    | Beskrivning                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Upplyst (PBR)](#pbr)           | Physically Based Rendering (fysikaliskt baserad rendering) | Ljus, skuggor, miljö och målad metallitet/grovhet   |
| [MatCap](#matcap)           | Material Capture           | Snabbt läge för skulptering, som belastar gpu/cpu mindre än PBR        |
| [Obelyst](#unlit)             | Ytfärg              | Bara ytfärgen, utan skuggning eller belysning                  |
| [Objekt-ID](#object-id)     | Objekt-ID                  | En slumpmässig färg per objekt, användbart i målarprogram.    |
| [Instans-ID](#instance-id) | Instans-ID                | En slumpmässig färg per instans, användbart för att hitta delade mesher   |

Om du vill veta mer om metallitet och grovhet, se avsnittet [Vertexmålning](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Ytgrupp {#face-group}
Visar ytgruppernas färger ovanpå modellen. Ytgrupper är färgade urval av polygoner som du kan skapa med verktyget [Ytgrupp](tools#facegroup), och de skapas automatiskt för de flesta primitiver.

En del verktyg filtrerar automatiskt efter ytgrupper när ytgrupperna är synliga.

### ![](/icons/palette.webp) Visa måleri {#show-paint}
Nomad kan lagra färg, grovhet och metallitet i din skulpturs vertices. Med den här kryssrutan slår du på eller av visningen av de här egenskaperna globalt.

Observera att om du har både vertexegenskaper och texturer, och båda är aktiverade, multipliceras värdena med varandra.

### ![](/icons/shield.webp) Visa mask {#show-mask}
Slår på eller av gråskaleöverlägget från [maskverktygen](tools#mask). När det är avaktiverat är även masken avaktiverad. Det är användbart för att göra snabba ändringar utan masken: sedan kan du aktivera den igen utan att förlora din mask.

### ![](/icons/tool_hide.webp) Använd Dölj {#use-hide}

Slår på eller av dolda ytor. Observera att det bara fungerar om du INTE använder döljverktyget!

### ![](/icons/image.webp) Använd texturer {#use-textures}

I Nomad kan du tilldela objekt texturer från menyn [Material](material). Om texturer är tilldelade kan du slå på eller av dem globalt med den här kryssrutan.

Du kan inte skapa eller redigera texturer i Nomad, men texturer från importerade filer fungerar. Opacitetstexturer fungerar i Upplyst, MatCap och Obelyst, normal maps i Upplyst och MatCap, färg i Upplyst och Obelyst, och emission, grovhet och metallitet bara i Upplyst. Knappen är gråtonad när scenen inte har någon textur.

### Översikt över PBR och ljus {#pbr}
Den här manualen går inte in på detaljerna kring fysikaliskt baserad rendering (PBR).

En viktig sak att komma ihåg är att belysning och material är helt åtskilda.
Det betyder att du kan måla objektets färg, grovhet och metallitet medan belysningen hanteras separat.
Du kan alltså måla ditt objekt och justera belysningen senare, utan att förstöra modellens helhetsintryck.

Ljuskällor, miljön och dimman finns bara i [PBR-läget](#pbr).
Av prestandaskäl är du begränsad till 4 ljuskällor på mobilen och 6 på datorn.

::: tip
Du kan läsa in en glTF-fil med fler ljuskällor, och Nomad behåller dem alla.
Men det kommer inte nödvändigtvis att fungera smidigt.
:::

::: tip
Du kan fejka många ljuskällor genom att göra objekt obelysta/självlysande och sedan aktivera global belysning i menyn [Efterbehandling](postprocess).
:::

### Översikt över ljustyper {#light-types-overview}

Det här är de typer av ljus som stöds just nu:

| Läge                        | Beskrivning                                             | Kan kasta skuggor |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Riktad](#directional) | Solljus från oändligt långt bort                           | Ja              |
| [Miljö](#env-light)   | Ett avlägset ljus som matchas mot miljöns HDR  | Ja              |
| [Spot](#spot)               | Konformade ljus                                      | Ja              |
| [Punkt](#point)             | Punktljus som lyser åt alla håll                         | Ja              |

#### ![](/icons/sun.webp) Riktad {#directional}
Det skickar ut ljus från oändligt långt bort, med en jämn intensitet.
Dess 3d-position i scenen spelar ingen roll, bara dess orientering.

Du kan fästa det här ljuset vid kameran, så att belysningen förblir konsekvent.  
Du kan till exempel använda det för att göra ett kantljus (rim light, ett starkt ljus som kommer bakifrån modellen och pekar mot kameran) som alltid lyser upp modellens baksida.

#### ![](/icons/panorama.webp) Miljöljus {#env-light}
En [miljö-HDR](#environment) fungerar bra för mjuk allmänbelysning, men om det finns ett starkt, skarpt ljus i HDR-bilden blir skuggan det skapar väldigt mjuk, ofta knappt synlig. Att kombinera ett riktat ljus med miljö-HDR:en kan hjälpa, men det kan vara svårt att få dem att linjera.

Det här ljuset gör jobbet åt dig. Ljuset roteras automatiskt så att det linjerar med den ljusaste delen av HDR-bilden, och sedan kan du styra dess intensitet och vinkel (skuggornas mjukhet) separat.

#### ![](/icons/spotlight.webp) Spot {#spot}
En spotlight skickar ut ljus i en enda riktning, begränsat av en konform.

#### ![](/icons/light.webp) Punkt {#point}
Ett punktljus skickar ut ljus åt alla håll, och det kan också kasta skuggor.

#### Skuggor {#shadows}
Varje ljus kan kasta skuggor, och du kan välja hur de beräknas i dess [inställningar](#light-extra-controls). Om du ser artefakter i skuggorna kan reglagen för `Tolerans` där hjälpa.

Skuggornas kvalitet beror på objektens storlek i förhållande till hela scenen.  
Om du har ett stort objekt i scenen som inte behöver kasta skuggor (till exempel ett stort plan), se till att avaktivera skuggkastning i dess [materialinställningar](material.md#casts-shadows).

## ![](/icons/sun.webp) Belysning {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Kryssruta för belysning {#lights-checkbox}

Slår på eller av alla direkta ljuskällor i scenen.



### Lägg till ljus {#add-light}

Lägger till ett ljus i scenen, upp till 4 ljuskällor på mobilen och 6 på datorn. När ett ljus läggs till visas ljuslistan med knappar, och ett verktygsfält för ljuset läggs till högst upp i vyn.

![](/images/shading_lights_icons.webp)

* Texten visar ljusets namn och ljusstyrka. Tryck på den för att välja ljuset.
* Ögonikonen slår på eller av synligheten.
* Pennikonen låter dig byta namn på ljuset.
* Papperskorgsikonen raderar ett ljus.
* Kopieringsikonen duplicerar ett ljus.
* Ikonen med 3 punkter öppnar en komplett ljusredigerare. Det mesta av funktionerna finns också i verktygsfältet som visas i vyn.

Du kan också dra ett ljus i listan för att ändra ordningen.

### ![](/icons/spotlight.webp)  Ikoner {#icons}

Slår på eller av visningen av ljusikoner i vyn.

### Verktygsfält för ljus {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Det här verktygsfältet visas högst upp i vyn när ett ljus är valt.

* `Synlig` slår på eller av ljusets synlighet.
* Riktad/Miljö/Spot/Punkt ändrar ljustypen. Tryck för att växla mellan dem, eller håll intryckt för att se en meny.
* Intensitet styr ljusets styrka. Värdet kan gå över 1,0 för mycket starka ljus, vilket är användbart tillsammans med global belysning i Efterbehandling.
* Färgrutan öppnar en färgväljare när du klickar på den. Nomad har flera sätt att välja färg. Kelvin-reglaget ger ett naturligt sätt att välja varm eller kall belysning.
* Skugga slår på eller av skuggor.
* Vinkel (_riktat ljus och miljöljus_) eller Storlek (_spot och punkt_) anger hur brett ljuset är. Bredare ljus ger mjukare skuggor, mjukare belysning och mjukare högdagrar på objekten.
* Fäste (_bara riktat ljus_), Konvinkel och Mjukhet (_bara spot_) beskrivs i [ljusredigeraren](#light-extra-controls) nedan.
* ... visar `Klona`, `Centrera om` och `Radera`, tillsammans med skugginställningarna.

### Extra ljusinställningar {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Ikonen med 3 punkter för ett ljus i listan öppnar dess kompletta redigerare. Observera att en del alternativ bara gäller vissa ljustyper.

* `Riktad/Miljö/Spot/Punkt` låter dig ändra ljustypen.
* `Färgrutan` öppnar en färgväljare när du klickar på den.
* `Intensitet` styr ljusets styrka.
* `Fäste` (_bara riktat ljus_) anger om ljuset ska vara fäst vid världen (`Fast`) eller vid kameran (`Kamera`). Om du till exempel använder ett riktat ljus bakom din karaktär som kantljus, och fästet är satt till kameran, hamnar ljuset alltid bakom karaktären när du roterar kameran.
* `Mjukhet` (_bara spotlight_) styr hur skarp kanten på spotlightens kon är. 0 ger en mycket skarp kant. 1 är mycket mjukt, med en gradient in mot ljuskonens mitt. I vyn kan du använda den lilla blå punkten på spotlightens kon för att ställa in mjukheten direkt.
* `Konvinkel` (_bara spotlight_) styr spotlightens spridningsvinkel. En liten vinkel ger en mycket smal ljusstråle, 170 ger en mycket bred spridning. I vyn kan du använda den orange punkten för att ställa in konvinkeln direkt.
* `Vinkel` (_bara riktat ljus och miljöljus_) är ljusets skenbara storlek, ungefär som hur stor solen ser ut på himlen. Större vinklar ger mjukare skuggor och bredare högdagrar.
* `Storlek` (_bara spot och punkt_) är ljusets bredd. Större ljus ger mjukare skuggor.
* `Skugga` slår på eller av skuggor för det aktuella ljuset.
* Skuggtypen bestämmer hur skuggorna beräknas. En `Skuggkarta` renderar scenen från ljuset, så den skuggar också geometri som kameran inte ser. `Skärmyta` använder bara det som redan syns på skärmen: det är billigare, men experimentellt. Generellt är skuggkartan mer pålitlig.
* `Tolerans` (_bara skärmyta_): om det syns artefakter i skuggorna (antingen verkar skuggorna inte nå ända fram till ytorna, eller så finns det brus och mönster i skuggorna) kan du justera toleransen för att åtgärda det.
* `Kontakt` lägger till mer exakta skuggor över korta avstånd, där objekt nuddar varandra. Med `Auto` får bara det mest dominerande ljuset i scenen kontaktskuggor; `Nej` och `Ja` tvingar dem av eller på för det här ljuset. Dess reglage `Tolerans` fungerar som det ovan.

Knappen `...` i vyns verktygsfält har samma skugginställningar, plus:

* `Klona` duplicerar ljuset.
* `Centrera om` flyttar ljuset framför kameran och behåller dess orientering.
* `Radera` raderar ljuset.


## ![](/icons/panorama.webp) Miljö {#environment}

![](/images/shading_environment.webp)

I verkligheten kommer ljuset från alla håll: himlens blå, gräsets gröna, en byggnads röda. Allt det här ljuset från "miljön" kan simuleras med en miljökarta (environment map).

Använd kryssrutan bredvid rubriken för att slå på eller av miljöbelysningen.

Nomad levereras med flera exempel på miljökartor för inomhus- och utomhusmiljöer, med olika färgtoner och ljusstyrka. Prova olika kartor för att se vilken som lyfter fram flest detaljer i dina skulpturer.

Tryck på bilden för att se de tillgängliga miljökartorna. I den dialogen väljer du `Importera...` för att läsa in dina egna. Det är bäst att använda HDR-bilder (High Dynamic Range) i latlong- eller ekvirektangulärt format, som .hdr- eller .exr-filer. Bläddraren kan också ladda ner miljöer direkt från [Poly Haven](https://polyhaven.com/hdris), som har en bra samling gratis miljökartor.

### Exponering {#env-exposure}
Justerar miljökartans ljusstyrka. Kartorna kan ofta bli för ljusa tillsammans med vanliga ljuskällor. Att sänka exponeringen kan hjälpa till att balansera, särskilt tillsammans med global belysning i inställningarna för [Efterbehandling](postprocess).

### Rotation {#env-rotation}

Eftersom miljökartor fångar ljus från alla håll kan du rotera dem så att reflektionerna och den övergripande belysningen passar bra ihop med din skulptur. Du kan också rotera miljön genom att dra vågrätt med 3 fingrar i vyn.

### Fäst vid kamera {#env-attached}
Fäster miljön vid kameran.

Det gör att belysningen förblir konsekvent, vilket kan vara användbart när du skulpterar.

### Oskärpa (bakgrund) {#env-background-blur}
Det här reglaget visas bara när [bakgrunden](background.md) är inställd på miljön. Det gör miljöbilden bakom din modell suddig, utan att ändra belysningen.


## ![](/icons/fog.webp) Dimma {#fog}

Dimma ger scenen atmosfäriskt djup och gör ljusstrålar synliga. Aktivera den med kryssrutan bredvid rubriken. Precis som ljuskällorna och miljön finns den bara i läget [Upplyst (PBR)](#pbr).

::: tip Kraftigare ljusstrålar
Sänk dimmans `Miljö` och använd en stark spot eller ett starkt punktljus. Öka `Täthet` tills dimman syns tydligt. För synliga strålar i tunnare dimma, sätt `Spridningsriktning` till ett högt positivt värde och rikta kameran mot ljuset.
:::

### Färg {#fog-color}
Dimmans färg och färgen på ljuset den sprider.

### Täthet {#fog-density}
Hur snabbt dimman tätnar med avståndet.

### Maximal opacitet {#fog-opacity}
Begränsar hur mycket dimman kan täcka scenen, även vid hög täthet.

### Spridningsriktning {#fog-scattering}
Riktningen som dimman sprider ljuset i (kallas även anisotropi). Positiva värden gör dimman ljusare när du tittar mot ett ljus, negativa värden när du tittar bort från det, och noll sprider ljuset jämnt åt alla håll.

### ![](/icons/panorama.webp) Miljö {#fog-environment}
Hur mycket [miljön](#environment) lyser upp dimman. Den är gråtonad när miljön är avstängd.

### Brus {#fog-noise}
Blandar in brus i dimman så att den bryts upp i fläckar, utan att ändra dess totala täthet. När bruset är över 0 anger reglaget `Storlek` mönstrets storlek.

### Form {#fog-shape}
Var dimman fyller scenen:

* `Jämn` - fyller hela scenen.
* `Vertikal` - håller dimman inom ett lodrätt band med mjuka kanter. Reglagen `Nederkant` och `Överkant` anger höjden på dess nedre och övre kant, och deras ögonknapp visar bandet i vyn medan du justerar dem.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Som namnet antyder (MATerial CAPture) hanterar en matcap både belysning och materialinformation i en enda bild.
Eftersom själva materialet redan finns i matcap-bilden ignoreras målningskanalerna för grovhet och metallitet.
Målningsfärgen multipliceras med matcap-bilden, vilket betyder att om du har en svart/grå matcap blir den inte ljusare av vit färg.

Många föredrar det här läget när de skulpterar, eftersom det låter dem fokusera på själva formen och geometrin.

Om du trycker på sfären öppnas en bildbläddrare. Du kan också lägga till din egen matcap: i stort sett vilket foto, vilken rendering eller till och med målning av en sfär som helst kan användas, så länge den är tätt beskuren till en kvadrat. Det finns många matcap-bibliotek på nätet, ett användbart är [nidorx matcap-bibliotek](https://github.com/nidorx/matcaps).

### Använd global MatCap {#matcap-global}

Oftast används en enda matcap för hela skulpturen, men om det här alternativet är avaktiverat kan det valda objektet ha sin egen matcap. Det kan användas konstnärligt för att få slående resultat.

::: tip
Avaktivera det här alternativet och använd en bild av ett öga till dina karaktärers ögon!
:::

### Rotation {#matcap-rotation}
En matcap är en särskild sorts miljökarta, så precis som en miljökarta kan den roteras. Du kan också göra det när som helst i vyn genom att dra med 3 fingrar åt vänster och höger.

Låsknappen bredvid reglaget låser rotationen, så att en dragning med 3 fingrar inte vrider matcap-bilden av misstag.



## ![](/icons/circle_fill.webp) Obelyst {#unlit}

Det här läget visar bara ytfärgen. Det kan vara användbart för att kontrollera att objektens ytfärg är som du förväntar dig, utan att distraheras av ljus, skuggor, reflektioner och transparens.

Läget kan också användas för icke-fotorealistiska renderingar, för en platt, tecknad stil.

## ![](/icons/cube.webp) Objekt-ID {#object-id}

All information om belysning och ytor ignoreras, och varje objekt skuggas med en unik, platt färg. Om du renderar det här tillsammans med en PBR-rendering kan du använda det i ett målarprogram för att markera efter färg och på så sätt färgkorrigera specifika objekt.

Observera att de här färgerna också visas i [trädvyn i menyn Scen](scene#tree-view).

### Slumpmässigt ID {#object-random}

Skapar en ny uppsättning slumpmässiga färger.

## ![](/icons/link.webp) Instans-ID {#instance-id}

Samma som Objekt-ID, men instanser får samma färg.

### Slumpmässigt ID {#instance-random}

Skapar en ny uppsättning slumpmässiga färger.
