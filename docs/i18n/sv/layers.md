# ![](/icons/layer.webp) Lager {#layers}

Den här menyn innehåller lagerstacken, ett sätt att spara ändringar av ditt objekt på ett icke-destruktivt sätt, och många sätt att kombinera och återanvända lager.

![](/images/layers_overview.webp) 

## Översikt {#overview}

Lager i Nomad fyller flera funktioner.

Målningsinformation (färg, grovhet, metallitet, opacitet) fungerar med lager ungefär som i 2d-målningsprogram. Du kan skapa ett lager och måla på en modell. Lagret kan slås på eller av, få sin opacitet justerad, dupliceras, flyttas i lagerstacken och få sitt blendläge ändrat.

Nomad använder också lager för skulptering. Ett lager kan lagra fina detaljer som rynkor, eller stora förändringar, så att de fungerar som blendshapes/shape keys/morph targets i andra 3d-program. Du kan till exempel skulptera olika ansiktsuttryck på olika lager och justera lagrens reglage för att kombinera dem till nya uttryck.

I det fallet är ändringarna i ett lager rent additiva: lagrens ordning spelar ingen roll, som den gör för målning.

Lager kan delvis raderas med verktyget [Radera lager](tools.md#delete-layer), och lager kan också användas för att skapa masker utifrån den information som finns lagrad i lagret.

![](/videos/layer.mp4)

::: tip
Till skillnad från de flesta skulpteringsprogram försvinner inte lagren när du ändrar nätets topologi. Du kan använda [Voxel-omnätning](topology.md#voxel-remesher), [Multiresolution](topology.md#multiresolution) eller verktygen [Beskär](tools.md#trim)/[Dela](tools.md#split), men observera att lagrets kvalitet påverkas när du använder [Voxel-omnätning](topology.md#voxel-remesher).
:::

::: tip
Om du använder lager för blendshapes/morph targets finns det extra lagerfunktioner i [scenmenyn](scene.md#object-menu). Du kan dela upp lager i objekt och kombinera matchande objekt till lager.
:::
----

## Lagermeny {#layer-menu}

![](/images/layers_menu.webp)

Rubriken visar namnet på det valda objektet. Lager finns inte på grundformer, så validera grundformen först.

Tryck på `Lägg till lager` för att skapa ett nytt lager. `Slå ihop lager` slår ihop alla lager med basnätet; siffran bredvid ikonen visar hur många lager det finns.

Varje lager har ett namn, ett reglage för dess styrka/faktor och alternativknappar. Tryck på ett lager för att göra det aktivt: skulptering och målning hamnar i det lagret. Tryck på `Bas` för att arbeta på basnätet igen.

### ![](/icons/sort_right.webp) Expandera listan {#ui-expand-list}

Som standard visar lagerlistan bara synligheten, blendläget och styrkan för varje lager, och det aktiva lagret är expanderat med alla sina kontroller. Pilen till vänster om rubriken expanderar alla kontroller för varje lager.

![](/images/layers_expand.webp)

### Alternativ {#options}

| Åtgärd       | Ikon                         | Beskrivning                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Synlig       | ![](/icons/eye_open.webp)   | Visa/dölj lagret                                    |
| Blendläge    | ![](/icons/opacity.webp)    | Blendläge i photoshop-stil. De 4 ikonerna visar lägena för färg, grovhet, metallitet och opacitet. |
| Redigera namn | ![](/icons/pencil.webp)    | Redigera lagrets namn                               |
| Radera       | ![](/icons/trash.webp)      | Radera lagret                                       |
| Duplicera    | ![](/icons/clone.webp)      | Duplicera lagret                                    |
| Slå samman ner | ![](/icons/merge_down.webp) | Slå samman lagret med lagret under (eller basnätet) |
| Mer          | ![](/icons/more.webp)       | Alternativen under [Mer...](#more)                  |

När ett lager inte är expanderat finns `Redigera namn`, `Radera`, `Duplicera` och `Slå samman ner` i dess meny [Mer...](#more).

För att flytta ett lager till en annan plats i lagerstacken håller du fingret på dess namn och drar.

### Bas {#base}

Knappen med 3 punkter på raden `Bas` flyttar basnätets målning till ett nytt lager, med knappen `Bas → Lager`. Basen återställs sedan till bakgrundsmaterialet. Det är praktiskt när du har målat mycket innan du skapade något lager.

* Mask- och döljknapparna bredvid lämnar maskerade och dolda områden orörda.
* `Extrahera` - kanalerna som ska flyttas: `Färg`, `Opacitet`, `Grovhet` och `Metallitet`.
* `Bakgrundsmaterial` - om det är aktiverat flyttas bara de värden som skiljer sig från det här materialet. Ställ in det med reglagen, eller hämta det från modellen med pipetten.

### ![](/icons/more.webp) Mer... {#more}

Knappen 'Mer...' visar extra alternativ för det aktuella lagret, i två flikar: inställningarna (kugghjulsikonen) och extraheringen (kubikonen).

![](/images/layers_more.webp) 

#### Kanalfaktorer {#channel-factors}

Med de här kontrollerna kan du skala mängden skulptering/färg/grovhet/metallitet/opacitet för lagret. Värdena multipliceras med lagrets faktorreglage, så om lagrets styrka till exempel är 1 men färgkanalens faktor är 0,5, visas färgen med styrkan 0,5.

`Förskjutning` styr lagrets skulpteringsstyrka. Medan färg/grovhet/metallitet är begränsade till mellan 0 och 1 kan förskjutningen ha vilket värde som helst, både positivt och negativt.

::: tip
Förskjutningen kan användas för att göra ett lager med bulor till ett lager med gropar, eller ett leende till en sur min:
![](/videos/layer_happysad.mp4)


Ett symmetriskt lager kan klonas och sedan delas upp i en vänster- och en högerform med Radera lager:
![](/videos/layer_leftright.mp4)

Lager med negativa förskjutningsfaktorer kan bakas ned i tomma lager för att skapa nya positiva former.

Lager med positiva förskjutningsfaktorer över 1 kan användas för att experimentera med mer extrema blendshapes.
:::

::: warning
För närvarande delar lagren en enda opacitetskanal för alla 3 kanalerna (färg/metallitet/grovhet).
Om du slår ihop flera lager med intensitet per kanal som inte är på full intensitet kan slutresultatet se annorlunda ut.

Kanske får varje kanal sin egen alfakanal i framtiden, så att den här begränsningen försvinner.
:::


#### ![](/icons/shield.webp) Mask {#mask}
Maskknappen bredvid varje reglage skapar en mask från den kanalen. Ungefär som när du använder lager för att göra markeringar i målningsprogram kan du på så sätt återanvända arbetet i ett lager till andra operationer.

#### ![](/icons/preview.webp) Förhandsgranska {#preview}
![](/images/layers_preview.webp) 

Följande alternativ finns i extraheringsfliken i menyn 'Mer...'.

När det är aktiverat förhandsvisas extraheringsinställningarna för det här lagret (se nästa avsnitt).

`Röntgen` väljer vilka objekt som görs genomskinliga under förhandsvisningen (`Ingen`, `Inte vald`, `Vald` eller `Alla`), så att den extraherade formen förblir solid. Det är användbart om du använder negativa extraheringshöjder.

#### ![](/icons/mask_extract.webp) Extrahera {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Knappen `Extrahera` duplicerar lagrets innehåll till ett nytt objekt, oftast med en tjocklek som du väljer i nästa avsnitt.

`Avsluta åtgärd` bestämmer hur dupliceringen görs:

* `Ingen` - Extraherar bara delen, utan att försöka skapa sidor eller fylla några hål.
* `Fyll` - Hålet fylls och jämnas ut med trianglar. Använd inte det här alternativet för plana ytor.
* `Skal` - Sluter den extraherade formen med tjockleken och riktningsalternativen.
* `Lager` - Extraherar lagrets skillnad.

#### ![](/icons/height.webp) Höjd {#thickness}
![](/images/layers_thickness.webp) 

Djupet på skalets extrudering. Positiva värden växer ut från ytan, negativa värden växer in i ytan. Den döljs när den avslutande åtgärden är `Lager`.

Plus/minus bredvid värdet ställer in extruderingens riktning:
* Minus ( - ) startar från den aktuella ytan och extruderar nedåt.
* Plus ( + ) startar från den aktuella ytan och extruderar uppåt.
* PlusMinus ( ± ) skjuter extruderingens över- och undersida ut lika mycket, så att den sitter till hälften inbäddad i den ursprungliga ytan.

#### Sidor {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Det här avsnittet syns när den avslutande åtgärden är `Skal`.

`Väggdelningar` ställer in antalet indelningar längs skalets sidor. Med reglaget `Auto` påslaget räknar Nomad ut antalet kantslingor som ger kvadratiska polygoner.

#### Glathet {#smoothness}
![](/images/layers_smoothness.webp) 

Om kanterna på området som ska extraheras är taggiga kan du aktivera det här alternativet för att jämna ut dem till en snyggare form. `Alla` jämnar ut hela den extraherade ytan, `Endast kanter` jämnar ut dess kanter. `Iterationer` ställer in hur stark utjämningen är.

_Här slutar undermenyn 'Mer...'._

### ![](/icons/cog.webp) Avancerat {#advanced}
![](/images/layers_advanced.webp)

Knappen `Avancerat` längst ned i menyn visas när objektet har lager.

#### Behåll detaljer i översta lager {#keep-top-layers-details}

Ser till att små detaljer på högre lager förblir synliga när stora ändringar görs på lägre lager. Medan du skulpterar ignoreras deformationen från de översta lagren, men deras detaljer förblir synliga. Det fungerar bara bra om de översta lagren innehåller relativt små detaljer.

Om du som standard skulpterar små rynkor på ett lager och sedan gör stora ändringar på baslagret försvinner rynkorna. Med det här alternativet aktiverat svävar de små detaljerna alltid ovanpå de stora ändringarna under. I följande video ser du hur rynkdetaljen tas bort som standard, men förblir synlig när 'behåll detaljer i översta lager' är aktiverat:

![](/videos/layers_details.mp4)


#### Synkronisera transform {#sync-transform}

När det är på justeras alla icke valda lager efter transformationens rotation, skala och skevhet när du använder verktygen Gizmo eller Transformera. Det kan vara `Auto`, `Nej` eller `Ja`.

Avaktivera det här alternativet om de andra lagren ska användas utan den nya transformationen som du tillämpar.

När det är inställt på `Auto` justeras bara de synliga lagren.
