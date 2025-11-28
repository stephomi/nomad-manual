# ![](/icons/sun.webp) Skuggning {#shading}

Den här menyn styr skuggningslägena som används av Nomad, ljusegenskaper och miljöljus-/matcap‑egenskaper.

![](/images/shading_overview.webp)



Du kan välja mellan flera renderingslägen:

| Läge                        | Betydelse                 | Beskrivning                                                    |
| :-------------------------: | :-----------------------: | :------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Fysikbaserad rendering    | Målning med metallikhet/roughness                              |
| [Matcap](#matcap)           | Material Capture          | Används under skulptering med lägre gpu/cpu‑användning än PBR  |
| [Unlit](#unlit)             | Ytfärg                    | Endast ytfärg utan skuggning eller belysning                   |
| [Object Id](#object-id)      | Objekt‑ID                 | En slumpmässig färg per objekt, användbart i målningsprogram   |
| [Instance Id](#instance-id)  | Instans‑ID                | En slumpmässig färg per instans, användbart för att identifiera delade mesh:er |

Om du vill lära dig mer om metallikhet och roughness, se avsnittet [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Ytgrupp {#face-group}
Visa överlägg med facegroup‑färger. Facegroups är färglagda polygonval som kan skapas med verktyget [Face group](tools#facegroup), och skapas automatiskt med de flesta primitiver.

Vissa verktyg kommer automatiskt att filtrera efter facegroups när facegroups är synliga.

### Visa färg {#show-paint}
Nomad kan lagra färg, roughness, metallikhet i vertexarna på din skulpt. Du kan slå av/på visningen av dessa egenskaper globalt med den här kryssrutan.

Observera att om du har både vertex‑egenskaper och texturer, och båda är aktiverade, kommer värdena att multipliceras med varandra.

### Visa mask {#show-mask}
Slå av/på gråskalemaskens överlägg från [maskverktygen](tools#mask). När detta är avstängt är masken också avstängd, vilket är användbart för att göra snabba ändringar utan mask, sedan kan du slå på den igen utan att förlora masken.

### Använd dölj {#use-hide}

Slå av/på dolda ytor. Observera att detta bara fungerar om du INTE är i hide‑verktyget!

### Använd texturer {#use-textures}

Nomad tillåter att texturer tilldelas objekt från [materialmenyn](material). Om texturer är tilldelade kan de slås av/på globalt med den här kryssrutan.







### PBR- och ljusöversikt {#pbr}
Den här manualen går inte in på detaljerna kring fysikbaserad rendering (PBR).

En viktig sak att komma ihåg är att belysning och material är helt separerade.
Det betyder att du kan måla objektets färg, roughness och metallikhet medan belysningen hanteras oberoende.
Det gör att du kan måla ditt objekt och sedan justera belysningen senare utan att förstöra helhetsintrycket av din modell.

Ljus är endast tillgängliga med [PBR‑läge](#pbr).
Av prestandaskäl är du begränsad till endast 4 ljus.

::: tip
Du kan ladda en glTF‑fil med fler än 4 ljus och Nomad kommer att behålla alla.
Det kommer dock inte nödvändigtvis att fungera bra prestandamässigt.
:::

::: tip
Du kan fejka många ljus genom att göra objekt unlit/emissiva och sedan aktivera global illumination i menyn [post process](postprocess).
:::

### Översikt över ljustyper {#light-types-overview}

Här är de ljustyper som för närvarande stöds:

| Läge                        | Beskrivning                                              | Kan kasta skuggor                                      |
| :-------------------------: | :------------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Oändligt avlägset solljus                                | ja                                                     |
| [Environment](#environment) | Ett avlägset ljus som matchas mot miljöns HDR           | ja                                                     |
| [Spot](#spot)               | Konformade ljus				                            | Ja                                                     |
| [Point](#point)             | Punktljus i alla riktningar                             | Ja, men endast via mindre robusta skärmbaserade skuggor |

#### Riktad {#directional}
Det avger ljus från oändligt långt bort, med jämn intensitet.
Dess 3D‑position i scenen spelar ingen roll, endast dess orientering.

Du kan fästa detta ljus vid kameran, så att det ger konsekvent belysning.  
Till exempel kan du använda det för att skapa ett kantljus (ett starkt ljus som kommer bakifrån din modell och pekar mot kameran) som alltid lyser upp baksidan av din modell.

#### Miljöljus {#env-light}
Att använda en [environment HDR](#environment) fungerar bra för övergripande mjuk belysning, men om det finns en stark, skarp ljuskälla synlig i HDR‑bilden blir skuggan från den ofta väldigt mjuk, ibland knappt synlig. Att använda ett riktat ljus (directional) i kombination med environment‑HDR kan hjälpa, men det kan vara svårt att få dem att linjera.

Det här ljuset gör jobbet åt dig. Ljuset roteras automatiskt för att linjera med den ljusaste delen av HDR‑bilden, sedan kan du styra dess intensitet och vinkel (skuggmjukhet) separat. 

#### Spot {#spot}
Spotlight avger ljus i en enda riktning, begränsat av en konform.

#### Punkt {#point}
Punktljus avger ljus i alla riktningar.  
För närvarande stöder punktljus inte skuggor.

#### Skuggor {#shadows}
Alternativet `normal bias` kan användas för att minska vanliga skuggartefakter (acne/peter‑panning).

Skuggkvaliteten beror på objektens storlek relativt hela scenen.  
Om du har ett stort objekt i scenen som inte behöver kasta skuggor (till exempel ett stort plan), se till att inaktivera skuggkastning i dess [materialinställningar](material.md#cast-shadows).

## Ljus {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Ljusruta {#lights-checkbox}

Slå av/på alla direkta ljus i scenen.



### Lägg till ljus {#add-light}

Lägg till ett ljus i scenen, upp till maximalt 4. När ett ljus läggs till visas ljuslistaren med knappar, och en ljusverktygsrad läggs till högst upp i vyn.

![](/images/shading_lights_icons.webp)

* Texten visar ljusets namn och ljusstyrka.
* Ögonikonen slår av/på synlighet.
* Pennikonen låter dig byta namn på ljuset.
* Papperskorgsikonen tar bort ett ljus.
* Kopieringsikonen duplicerar ett ljus. 
* Ikonen med 3 prickar öppnar en fullständig ljuseditor. Det mesta av denna funktionalitet finns också i verktygsraden som visas i vyn. 

### ![](/icons/spotlight.webp) Ikoner {#icons}

Slå av/på visning av ljusikoner i vyn.

### Ljusrad {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Den här verktygsraden visas högst upp i vyn när ett ljus är markerat.

* Show slår av/på ljusets synlighet.
* Directional/Environment/Spot/Point ändrar ljustyp. Tryck för att växla, eller håll ned för att se en meny.
* Intensity styr ljusstyrkan, värdet kan gå över 1,0 för mycket intensiva ljus, användbart tillsammans med Global Illumination i Post Process.
* Färgrutan öppnar en färgväljare när du trycker på den. Nomad erbjuder flera sätt att välja färg. Kelvin‑kontroll ger ett naturligt sätt att välja varmt/kallt ljus.
* Shadow slår av/på skuggor.
* Size ställer in ljusets bredd. Bredare ljus ger mjukare skuggor, mjukare belysning och en mjukare highlight på objekt.
* ... öppnar extra kontroller.

### Extra ljuskontroller {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Observera att vissa alternativ är specifika för vissa ljustyper.

* `Clone` duplicerar ljuset.
* `Recenter` flyttar ljuset tillbaka till origo.
* `Delete` tar bort ljuset.
* `Directional/Environment/Spot/Point` låter dig ändra ljustyp.
* `Colour swatch` öppnar en färgväljare när du trycker på den. 
* `Intensity` styr ljusstyrkan.
* `Attachment` (_endast directional_) ställer in om ljuset ska vara förälder till världen eller till kameran. T.ex. om du använder ett riktat ljus bakom din karaktär som kantljus, kommer ljuset alltid att ligga bakom karaktären när Attachment är satt till camera och du roterar kameran.
* `Angle` (_endast directional och environment_) är ljusets skenbara storlek, tänk på det som hur stor solen ser ut på himlen. Större vinklar ger mjukare skuggor och bredare highlights.
* `Softness` (_endast spotlight_) styr skärpan på kanten av spotlight‑konen. 0 är en mycket skarp kant. 1 är mycket mjuk, med en gradient in mot mitten av ljuskäglan. I vyn kan den lilla blå pricken på spotlight‑konen användas för att ställa in softness interaktivt.
* `Cone angle` (_endast spotlight_) styr spridningsvinkeln för spotlighten. En liten vinkel ger en mycket smal ljusstråle, 170 ger en mycket bred ljusspridning. I vyn kan den orange pricken användas för att ställa in cone angle interaktivt.
* `Shadow` slår av/på skuggor för det aktuella ljuset.
* `Shadow map` och `screenspace` är olika sätt att beräkna skuggor, generellt är shadow map mer pålitligt.
* `Contact` justerar hur skuggor beräknas. Skuggor är ett svårt problem inom datorgrafik och kan orsaka artefakter i rendering. Mer exakta skuggor kan väljas för det viktigaste ljuset i en scen; den här kontrollen avgör om det viktigaste ljuset väljs automatiskt av Nomad eller av användaren.
* `Tolerance` om skuggartefakter är synliga (antingen att skuggor inte verkar ha kontakt med ytor, eller att det finns brus och mönster i skuggorna) kan justering av tolerance hjälpa till att lösa dessa problem.


## Miljö {#environment}

![](/images/shading_environment.webp)

Ljus i den verkliga världen kommer från alla riktningar; himlens blå, gräsets gröna, en byggnads röda – allt detta ljus från ”miljön” kan simuleras med en environment‑karta. 

Nomad levereras med flera exempel på environment‑kartor för inomhus‑ och utomhusmiljöer, med olika färgstick och ljusstyrkenivåer. Prova olika kartor för att se vilka som framhäver mest detaljer i dina skulpturer.

Tryck på bilden för att se tillgängliga environment‑kartor. I den dialogen kan du välja ”Import...” för att ladda dina egna. Det är bäst att använda High Dynamic Range (HDR)‑bilder i latlong‑ eller equirectangular‑format, som .hdr‑ eller .exr‑filer. [www.polyhaven.com](https://polyhaven.com/hdris) har en bra samling gratis environment‑kartor att använda; generellt är 1k HDR‑kartor en bra storlek och kvalitet.

### Exponering {#env-exposure}
Justera ljusstyrkan på environment‑kartan. Ofta kan kartorna vara för ljusa när de används tillsammans med vanliga ljus; att sänka exposure kan hjälpa balansen, särskilt tillsammans med Global Illumination i [Post Process](postprocess)‑inställningarna.

### Rotation {#env-rotation}

Eftersom environment‑kartor fångar ljus från alla riktningar kan du rotera dem för att få reflektioner och övergripande belysning att samspela bra med din skulpt.

### Fäst vid kamera {#env-attached}
Fäst environment‑kartan vid kameran.

Det tvingar belysningen att vara konsekvent, vilket kan vara användbart under skulptering.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Som namnet antyder (MATerial CAPture) tar en matcap hand om både belysning och materialinformation i en enda bild.
Eftersom materialet redan finns i matcap:en ignoreras målkanalerna för roughness och metallikhet.
Målningsfärgen multipliceras med matcap:en, vilket betyder att om du har en svart/grå matcap kommer vit färg inte att göra den ljusare.

Konstnärer föredrar ofta detta läge för skulptering eftersom det låter dem fokusera på formen och geometrin i sig.

Att trycka på sfären öppnar en bildbläddrare. Du kan också lägga till din egen matcap; i princip kan vilket foto, rendering eller till och med en målning av en sfär som beskärts tajt till en kvadrat användas. Många matcap‑bibliotek finns online, en användbar resurs är [nidorx matcap library](https://github.com/nidorx/matcaps).

### Använd global Matcap {#matcap-global}

Vanligtvis använder konstnärer en enda matcap för hela skulpten, men om denna växel är avstängd kan varje objekt ha sin egen matcap. Detta kan användas konstnärligt för att få slående resultat.

::: tip
Inaktivera det här alternativet och använd en bild av ett öga för din karaktärs ögon!
:::

### Rotation {#matcap-rotation}
En matcap är en specialiserad form av environment‑karta, så precis som en environment‑karta kan den roteras. Du kan också göra detta när som helst i vyn genom att dra med tre fingrar åt vänster och höger.



## ![](/icons/circle_fill.webp) Oupplyst {#unlit}

Detta läge visar endast ytfärgen. Det kan vara användbart för att kontrollera att ytfärgen på dina objekt är som du förväntar dig, utan att distraheras av ljus, skuggor, reflektioner eller transparens. 

Detta läge kan också användas för icke‑fotorealistiska renderingar, för att uppnå ett platt, tecknat utseende.

## ![](/icons/cube.webp) Objekt-ID {#object-id}

All belysnings‑ och ytinformation ignoreras, och varje objekt skuggas med en unik platt färg. Om detta renderas tillsammans med en PBR‑render kan det användas i ett målningsprogram för att välja efter färg och därmed kunna göra färgkorrigeringar på specifika objekt.

Observera att dessa färger också visas i [Scenmenyns trädvy](scene#tree-view).

### Slumpa id {#object-random}

Generera en ny uppsättning slumpmässiga färger. 

## ![](/icons/link.webp) Instans-ID {#instance-id}

Samma som Object ID, men instanser får samma färg. 

### Slumpa id {#instance-random}

Generera en ny uppsättning slumpmässiga färger.