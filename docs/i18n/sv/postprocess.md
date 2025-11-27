# ![](/icons/postprocess.webp) Efterbearbetning 

Den här menyn styr många aspekter av Nomad som påverkar hur renderingen ser ut.

![](/images/postprocess_overview_drac.webp)

Att använda efterbearbetning kan förändra den slutliga looken på din scen avsevärt.

![](/images/postprocess_overview.webp)
*Samma scen före och efter efterbearbetning, utan extra ljus eller materialändringar.*

Efterbearbetning kan påverka prestandan mycket beroende på din enhet.
Det finns en global kryssruta för att inaktivera all efterbearbetning, så att du snabbt kan gå tillbaka till skulptering/modellering utan att förlora dina förinställningar.
För PBR-rendering bör [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) och [Tone Mapping](#tone-mapping) vara aktiverade.

Oftast vill du dock ha efterbearbetningen avstängd när du skulpterar, för att fokusera på själva formen i renderingen.


## Quality

![](/images/postprocess_quality.webp)
### Max frame sampling
Nomad beräknar en viss mängd efterbearbetning för en enskild bildruta, vilket kan se brusigt ut. Den här kontrollen avgör hur många bildrutor som ska renderas och sedan blandas ihop för att ta bort de flesta brusartefakter. Vissa effekter kräver inga extra sampel (t.ex. färgkorrigering), medan andra som global illumination kan kräva hundratals sampel för att bli brusfria. 

I vyn kan detta ses när Nomad lämnas ifred; bildkvaliteten förfinas gradvis upp till max antal sampel och stannar sedan. Detta antal beräkningar används också i renderingssektionen i [Files-menyn](files) när ”export png” klickas.

### Resolution multiplier
Den här skjutreglaget styr upplösningen på efterbearbetningen. Ett värde på x1.0 innebär att renderingarna görs i enhetens pixelupplösning. Ett värde på x0.5 renderar i halv upplösning, vilket går snabbt men ger låg kvalitet. Ett värde större än 1 renderar i större storlek och skalas sedan ned. Detta ger högre kvalitet, mindre brus men längre renderingstider.

### Max samples

Detta ökar kvaliteten på efterbearbetningen, men generellt har `Full resolution` större inverkan. 

### Full resolution
När den är aktiverad tvingar den upplösningsmultiplikatorn till x1.0

### Denoiser (oidn)

Applicera en brusreducerare på bilden. Detta kan göra att du kan använda mycket färre sampel. Detta fungerar bara om `Full Resolution` är aktiverat. Observera att brusreduceringen sker efter att alla sampel har beräknats och kan vara processorintensiv.

## Preset browser
![](/images/postprocess_presets.webp)
Genom att klicka på bilden visas en samling förinställningar för efterbearbetning. För att definiera egna förinställningar, välj en, klicka på ”clone”, gör ändringar. För att spara, klicka på förinställningsbilden, klicka igen inne i preset browser och välj ”save”.


## Reflection (SSR)
Med det här alternativet kan objekt reflektera andra objekt i scenen, så länge objekten är synliga på skärmen.
Om du har metalliska och blanka objekt i din scen bör det här alternativet troligen användas.
Detta alternativ är endast effektivt i PBR-läge.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Global Illumination (SSGI)

Global illumination simulerar hur ljus studsar mellan ytor, t.ex. att en röd vägg kastar rött ljus på ett närliggande vitt objekt. Detta kan avsevärt förbättra realismen i en rendering när det används tillsammans med ambient occlusion och reflektioner. 

`Strength` - Intensiteten på global illumination. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_En spotlight är placerad bakom sfären och riktad mot taket. Med SSGI av är det bara taket som är upplyst. Med SSGI på studsar ljuset från taket till väggarna till sfären._

## Ambient Occlusion (SSAO)
Ambient occlusion mörkar områden där ljuset har mindre chans att nå (hörn osv).
Effekten beror endast på modellens geometri.

* `Strength`- Intensiteten på effekten.
* `Size`- Hur utbredd effekten är.
* `Curvature bias` - Hur känslig effekten är i förhållande till variationer i ytan.
* `Color` - En toning som multipliceras in i occlusionen, används för kreativa effekter.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO kommer att vara mest synlig i områden som huvudsakligen är upplysta av omgivningsljus. Områden som är under starkt direkt ljus får en mycket svagare AO-effekt.

:::

## Depth of Field (DOF)
Lägg till en oskärpeffekt på området som ligger utanför fokus.

Tryck helt enkelt på din modell för att ändra fokuspunkt.

* `Far blur` - Mängden oskärpa som appliceras på den del som ligger bortom fokuspunkten.
* `Near blur` - Mängden oskärpa som appliceras mellan fokuspunkten och kameran.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Bloom
Bloom får de ljusa områdena i din scen att glöda.

* `Intensity` - styrkan på effekten.
* `Radius` - Spridningen av effekten.
* `Threshold` - Hur ljusa pixlar måste vara i scenen innan de börjar blomma. Ett lågt värde gör att allt blommar, ett högt värde gör att endast de ljusaste pixlarna blommar.
* `Color` - en toning som kan läggas till i bloom för kreativa effekter.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Tone Mapping
Tone Mapping är en operation som mappar HDR-värden till intervallet `[0, 1]`.
Om du inte använder det (eller väljer `none`) kommer alla färgkomponenter högre än 1 att klippas.
Alla färgvariationer över detta intervall går då förlorade.

* `None/Neutral/Agx/ACES` - vilken tonemapper som ska användas. `None` gör ingen ommappning (men de andra kontrollerna fungerar fortfarande). De andra alternativen liknar att välja olika filmtyper; de hanterar överexponerade värden och färger på olika sätt. Detta är ett mycket djupt ämne, sök på tone mapping, Agx, ACES för mer information!
* `Exposure` - bildens övergripande ljusstyrka, liknande att justera bländaren på en kamera. Detta kan vara ett snabbt sätt att globalt ljusa upp eller mörka ned en bild.
* `Saturation` - färgstyrka. 1 är neutralt, 0 är monokromt, värden över 1 är alltmer mättade.
* `Contrast` - Gör mörka områden mörkare och ljusa områden ljusare. Använd varsamt, det kan introducera artefakter vid höga värden.

Observera att med `Tone Mapping` inaktiverat försvinner vissa detaljer eftersom pixlarna är för ljusa.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping kan förstärka effekten av global illumination. Om du sänker intensiteten på miljökartan, höjer den primära ljuskällan, kan du öka `exposure` i tone mapping för att se mer av ljusstudseffekterna.
:::

## Color Grading
Liknande kurvverktyget i Photoshop låter detta dig kontrollera balansen och fördelningen av färg i bilden. `main`-kontrollen påverkar hela färgbalansen, `red`/`green`/`blue`-kontrollerna ger finjustering. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Upptäck var det finns snabba förändringar i krökning och applicera en färg på dessa områden.

* `Factor` - den övergripande intensiteten på effekten
* `Bump` - hur mycket den hittar skarpa konvexa förändringar och placerar den valda färgen där (vitt som standard)
* `Cavity` - hur mycket den upptäcker konkava förändringar och placerar den valda färgen där (svart som standard)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Chromatic Aberration
Simulera linsartefakter där ljuset bryts upp runt skärmens kanter.

* `Strength` - hur mycket de röda/gröna/blå delarna av bilden separeras mot skärmens kanter

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignette
Simulera linsartefakter genom att mörka ned skärmens kanter.

* `Size` - Storleken på en inverterad ellips som placeras över bilden
* `Hardness` - Hur suddig eller skarp ellipsen blandas ovanpå bilden.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Lägg till en korn-effekt; det kan hjälpa till att göra bilden lite mindre artificiell.

* `Strength` - mängden korn/brus som läggs till i bilden.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Sharpness
En skärpeeffekt liknande den i Photoshop eller fotoappar.

* `Strength` - mängden skärpa som appliceras på bilden.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Simulera retro-spelens pixelgrafik.

* `Slider` - storleken på pixlarna
* `Allow frame sampling` - om du får många svarta pixlar, prova att slå på detta, vilket åsidosätter standardsamplingen.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Simulera utseendet hos gamla CRT-skärmar.

* `Factor` - styrkan på linjerna
* `Spacing` - storleken på linjerna

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering

Dithra pixlar för att minska bandningsartefakter. Vanligtvis bör detta vara aktiverat, men kan stängas av för specifika operationer (t.ex. export av djupkartor eller andra dataspecifika operationer).
