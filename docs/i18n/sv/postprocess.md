# ![](/icons/postprocess.webp) Efterbehandling {#post-process}

Den här menyn styr många delar av Nomad som påverkar hur renderingen ser ut.

![](/images/postprocess_overview_drac.webp)

Efterbehandling kan förändra scenens slutliga utseende rejält.

![](/images/postprocess_overview.webp)
*Samma scen före och efter efterbehandling, utan extra ljus eller ändrade material.*

Efterbehandling kan påverka prestandan mycket beroende på din enhet.
Det finns en global kryssruta `Efterbehandling` som stänger av all efterbehandling, så att du snabbt kan gå tillbaka till att skulptera/modellera utan att förlora dina förinställningar.
För PBR-rendering bör [Omgivande Occlusion](#ambient-occlusion-ssao), [Reflektion](#reflection-ssr) och [Tonkartläggning](#tone-mapping) vara aktiverade.

Men för det mesta vill du ha efterbehandlingen avstängd när du skulpterar, för att kunna fokusera på själva formen.


## Kvalitet {#quality}

![](/images/postprocess_quality.webp)

De här alternativen förbättrar renderingens kvalitet, på bekostnad av prestandan.

### Maximal bildprovering {#max-frame-sampling}
Nomad beräknar en viss mängd efterbehandling för en enskild bildruta, vilket kan se brusigt ut. Den här kontrollen bestämmer hur många bildrutor som renderas och sedan blandas ihop för att ta bort det mesta av bruset. Vissa effekter kräver inga extra samplingar (t.ex. färgkorrigering), medan andra som mjuka skuggor och global belysning kan kräva hundratals samplingar för att bli brusfria.

I vyn syns det när du låter nomad vara ifred: bildkvaliteten förfinas gradvis upp till det maximala antalet samplingar och stannar sedan. När den har stannat gör Nomad ingenting, vilket sparar batteri. Samma antal beräkningar används också i renderingsdelen av [menyn Filer](files) när du klickar på 'export png'.

Kryssrutan bredvid reglaget slår på eller av bildprovningen.

### Renderupplösning {#resolution-multiplier}
Det här reglaget styr renderingens upplösning. Värdet x1.0 betyder att renderingen görs i enhetens pixelupplösning. Värdet x0.5 renderar i halv upplösning, vilket går snabbt men ger låg kvalitet. Ett värde större än 1 renderar i en större storlek och skalar sedan ned. Det ger högre kvalitet och mindre brus, men längre renderingstider.

Det påverkar prestandan kraftigt, så försök hålla det på x1.25 eller lägre. Värdet sparas inte i inställningarna, och effekten [Pixelkonst](#pixel-art) åsidosätter det.

### ![](/icons/intensity.webp) Max. samplingar {#max-samples}

Förbättrar kvaliteten på efterbehandlingseffekterna, på bekostnad av prestandan.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Använder dithering på pixlarna för att minska bandningsartefakter (till exempel i övertoningar eller vinjetter). Det bör oftast vara aktiverat, men kan stängas av för särskilda ändamål (t.ex. export av djupkartor eller andra dataspecifika ändamål).

### ![](/icons/denoise.webp) Dämpa ljud (oidn) {#oidn}

Tillämpar en brusreducering på bilden när alla bildrutor har samlats ihop. Det gör att du kan använda betydligt färre samplingar. Brusreducering kräver mycket av processorn, så aktivera den bara om bilden är brusig. Den finns inte på alla enheter.

## Förinställningar {#preset-browser}
![](/images/postprocess_presets.webp)
Om du klickar på bilden under rubriken `Efterbehandling` visas en samling förinställningar för efterbehandling. Använd `Ny` för att skapa en förinställning från dina nuvarande inställningar. De inbyggda förinställningarna kan bara klonas: för att skapa en egen väljer du en, klickar på `Klona` och gör dina ändringar. När en förinställning har ändringar som inte har sparats visas `Osparade ändringar!`; för att spara klickar du på förinställningens bild, klickar igen inne bland förinställningarna och väljer `Spara`.

## Genvägsfält {#shortcut-bar}
När efterbehandlingen är aktiverad listar ett fält längst ned i menyn alla effekter (`SSR`, `SSGI`, `SSAO`, `DoF`, `Blomma`...). Tryck på en för att hoppa till dess avsnitt. Effekter som är avstängda är gråade, så fältet är också en snabb sammanfattning av vad den aktuella förinställningen gör.

## ![](/icons/postprocess_ssr.webp) Reflektion (SSR) {#reflection-ssr}
Med det här alternativet kan objekt spegla andra objekt i scenen, så länge objekten syns på skärmen.
Om du har metalliska och blanka objekt i scenen bör du nog använda det här alternativet.
Alternativet kräver skuggningsläget [Upplyst (PBR)](shading.md#pbr).


| SSR av                     | SSR på                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Global illumination (SSGI) {#global-illumination-ssgi}

Global belysning simulerar hur ljuset studsar mellan ytor, t.ex. kastar en röd vägg rött ljus på ett vitt objekt i närheten. Det kan öka realismen i en rendering enormt när det används tillsammans med ambient occlusion och reflektioner. Precis som reflektioner kräver det skuggningsläget [Upplyst (PBR)](shading.md#pbr).

`Styrka` - Den globala belysningens intensitet.



| SSGI av                    | SSGI på                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_En spotlight står bakom sfären, riktad mot taket. Med SSGI av är bara taket upplyst. Med SSGI på studsar ljuset från taket till väggarna och vidare till sfären._

## ![](/icons/postprocess_ssao.webp) Omgivande Occlusion (SSAO) {#ambient-occlusion-ssao}
Ambient occlusion mörkar ned områden där ljuset har mindre chans att nå fram (hörn osv.).
Effekten beror bara på modellens geometri.

* `Styrka` - Effektens intensitet.
* `Storlek` - Hur utbredd effekten är.
* `Tjocklek` - Hur stor djuptjocklek som antas för skymmande objekt, i procent av `Storlek`.
* `Nyans` - En färg som multipliceras in i ocklusionen, för kreativa effekter.


| SSAO av                     | SSAO på                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO syns mest i områden som främst lyses upp av miljöljuset. Områden som ligger i starkt direkt ljus får en mycket svagare AO-effekt.

:::

## ![](/icons/postprocess_dof.webp) Skärpedjup {#depth-of-field-dof}
Lägger till en oskärpeeffekt på området som ligger utanför fokus.

Tryck bara på din modell för att ändra fokuspunkten.

* `Bländarläge` - Styr oskärpan med en enda kamerabländare, i stället för de två oskärpereglagen nedan.
* `Bländare` (_bara i bländarläge_) - Objektivets f-tal, som på en riktig kamera. Ett lägre värde öppnar objektivet och ger mer oskärpa.
* `Fjärroskärpa` - Mängden oskärpa på bortre sidan av fokuspunkten.
* `Nära oskärpa` - Mängden oskärpa mellan fokuspunkten och kameran.


| DOF av                    | DOF med fokus på bortre ringen | DOF med fokus på närmre ringen |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Blomma {#bloom}
Bloom får de ljusa delarna av scenen att glöda.

* `Intensitet` - effektens styrka.
* `Radie` - Effektens spridning.
* `Tröskel` - Hur ljusa pixlarna i scenen måste vara innan de börjar glöda. Vid 0 glöder allt; ett högt värde låter bara de allra ljusaste pixlarna glöda.
* `Nyans` - en färg som kan läggas till glöden för kreativa effekter.

| Bloom av                     | Bloom med radie 0           | Bloom med radie 1           |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Tonkartläggning {#tone-mapping}
Tonkartläggning är en operation som mappar om HDR-värden till intervallet `[0, 1]`.
Om du inte använder den (eller väljer `Ingen`) klipps varje färgkomponent som är högre än 1.
Alla färgvariationer över det intervallet går då förlorade.

* `Ingen/Neutral/Agx/ACES` - vilken tonkartläggare som används. `Ingen` mappar inte om något (men de andra kontrollerna fungerar ändå). De andra alternativen påminner om att välja olika filmtyper: de hanterar överexponerade värden och färger på olika sätt. Det här är ett väldigt djupt ämne, sök på tone mapping, Agx och ACES för mer information!
* `Exponering` - bildens övergripande ljusstyrka, ungefär som att justera bländaren på en kamera. Det kan vara ett snabbt sätt att göra en bild ljusare eller mörkare överlag.
* `Mättnad` - färgstyrka. 1 är neutralt, 0 är svartvitt, värden över 1 blir allt mer mättade.
* `Kontrast` - Gör mörka partier mörkare och ljusa ljusare. Använd det försiktigt, höga värden kan ge artefakter.

Lägg märke till att vissa detaljer försvinner med `Tonkartläggning` avstängd, eftersom pixlarna är för ljusa.

| Tonkartläggning av          | Tonkartläggning på         |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tonkartläggning kan förstärka effekten av global belysning. Om du sänker miljökartans intensitet och höjer den primära ljuskällan kan du öka tonkartläggningens `Exponering` för att se mer av det studsande ljuset.
:::

## ![](/icons/postprocess_tone_curve.webp) Färgteckning {#color-grading}
Precis som kurvverktyget i Photoshop låter det här dig styra balansen och fördelningen av färgerna i bilden. Kontrollen `Huvudsak` påverkar hela färgbalansen, kontrollerna `Röd`/`Grön`/`Blå` ger finare kontroll.

| Färgkorrigering av            | Färgkorrigering på           |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Krökning {#curvature}
Hittar ställen där krökningen ändras snabbt och färgar de områdena.

* `Faktor` - effektens övergripande intensitet
* `Bula` - hur mycket den hittar skarpa konvexa förändringar och lägger den valda färgen där (vit som standard)
* `Hålighet` - hur mycket den hittar konkava förändringar och lägger den valda färgen där (svart som standard)
* `Tjocklek` - hur breda de hittade kanterna är.

Bredvid `Bula` och `Hålighet` väljer en färgruta färgen, och en liten knapp väljer hur färgen blandas med bilden.


| Krökning av                      | Krökning på                    |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Kromatisk Aberration {#chromatic-aberration}
Simulerar objektivartefakter där ljuset delas upp i sina färger runt skärmens kanter.

* `Styrka` - hur mycket bildens röda, gröna och blå delar glider isär mot skärmens kanter

| Kromatisk av                  | Kromatisk på                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vinjett {#vignette}
Simulerar objektivartefakter genom att mörka ned skärmens kanter.

* `Storlek` - Storleken på en omvänd ellips som läggs över bilden
* `Hårdhet` - Hur suddigt eller skarpt ellipsen blandas ovanpå bilden.
* `Nyans` - Vinjettens färg, svart som standard.


| Vinjett av                      | Vinjett på                     |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Korn {#grain}
Lägger till en korneffekt, som kan få bilden att se lite mindre konstgjord ut.

* `Styrka` - mängden korn/brus som läggs till i bilden.


| Korn av                      | Korn på                    |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Skarphet {#sharpness}
En skärpningseffekt som liknar den i Photoshop eller fotoappar.

* `Styrka` - hur mycket bilden skärps.


| Skarphet av                    | Skarphet på                  |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixelkonst {#pixel-art}
Simulerar pixelgrafik från gamla spel. Den här effekten åsidosätter [Renderupplösning](#resolution-multiplier).

* `Reglage` - pixlarnas storlek
* `Tillåt bildrutesampling` - om du får många svarta pixlar, prova att slå på det här. Utan det stänger pixelkonsteffekten av [bildprovningen](#max-frame-sampling).

| Pixel av                    | Pixel på                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Linjeskanning {#scanline}
Simulerar utseendet hos gamla CRT-skärmar.

* `Faktor` - linjernas styrka
* `Mellanrum` - linjernas storlek

| Linjeskanning av               | Linjeskanning på              |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
