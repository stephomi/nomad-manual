# ![](/icons/layer.webp) Lager {#layers}

Den här menyn innehåller lagerstacken, ett sätt att spara ändringar på ditt objekt på ett icke-destruktivt sätt, samt många sätt att kombinera och återanvända lager.

![](/images/layers_overview.webp) 

## Översikt {#overview}

Nomad-lager har flera användningsområden.

Målningsinformation (Färg, Råhet, Metallhet, Opacitet) fungerar med lager på ett sätt som liknar 2D-målningsprogram. Ett lager kan skapas och färg appliceras på en modell. Lagret kan slås av eller på, dess opacitet kan justeras, lagret kan dupliceras, dess ordning kan ändras i lagerstacken och dess blandningsläge kan justeras.

Nomad använder också lager för skulptering. Ett lager kan lagra fina detaljer som rynkor, eller det kan lagra stora förändringar, vilket gör att de kan fungera som blendshapes/shape keys/morph targets i andra 3D-program. Till exempel kan du skulptera olika ansiktsuttryck på olika lager och justera lagrens reglage för att kombinera dem till nya uttryck.

I det här fallet är ändringarna som lagras i ett lager enbart additiva, lagerordningen spelar ingen roll som den gör för färg.

Lager kan delvis raderas via verktyget [Delete Layer](tools.md#delete-layer), och lager kan också användas för att skapa masker baserat på den olika information som lagras i lagret.

![](/videos/layer.mp4)

::: tip
Till skillnad från de flesta skulpteringsprogram kommer ändring av ett meshs topologi inte att ta bort lagren. Du kan använda [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multires) eller verktygen [Trim](tools.md#trim)/[Split](tools.md#split), men observera att när du använder [Voxel Remesher](topology.md#voxel-remesher) kommer kvaliteten på lagret att påverkas.
:::

::: tip
Om du använder lager för blendshapes/morph targets finns extra lagerfunktionalitet i [scenmenyn](scene.md#object-menu). Du kan separera lager till objekt och kombinera matchande objekt till lager.
:::
----

## Lagermeny {#layer-menu}

![](/images/layers_menu.webp)

Tryck på `Add layer` för att skapa ett nytt lager.

Varje lager har ett namn, ett reglage för att styra dess styrka/faktor och alternativknappar.

### Alternativ {#options}

| Åtgärd       | Ikon                         | Beskrivning                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Synlig       | ![](/icons/eye_open.webp)   | Visa/dölj lagret                                    |
| Blandningsläge | ![](/icons/opacity.webp)  | Photoshop-liknande blandningsläge. De 4 ikonerna visar lägena för Färg, Råhet, Metallhet, Opacitet. |
| Redigera namn | ![](/icons/pencil.webp)    | Redigera lagernamnet                                |
| Ta bort      | ![](/icons/trash.webp)      | Ta bort lagret                                      |
| Duplicera    | ![](/icons/clone.webp)      | Duplicera lagret                                    |
| Slå ihop nedåt | ![](/icons/merge_down.webp) | Slå ihop lagret med det undre lagret (eller basmeshen) |
| Mer          | ![](/icons/more.webp)       | [Mer...](#more) alternativ                          |

För att flytta ett lager till en annan plats i lagerstacken, tryck och håll på dess namn och dra sedan.

### Mer... {#more}

Knappen ”More...” visar extra alternativ för det aktuella lagret:

![](/images/layers_more.webp) 

#### Kanal­faktorer {#channel-factors}

Dessa kontroller låter dig skala mängden skulptering/färg/råhet/metallhet/opacitet för lagret. Dessa värden multipliceras med lagrets faktorreglage, så om till exempel lagerstyrkan är 1 men färgkanalfaktorn är 0,5, kommer färgen som visas att vara på 0,5 styrka.

`Offset` styr lagrets skulpteringsstyrka. Medan färg/råhet/metallhet kläms mellan 0 och 1 kan offset vara vilket värde som helst, både positivt och negativt. 

::: tip
Offset kan användas för att göra ett lager med bulor till ett lager med gropar, eller ett leende till en sur min:
![](/videos/layer_happysad.mp4)


Ett symmetriskt lager kan klonas och sedan delas upp i vänster/höger-former med del layer:
![](/videos/layer_leftright.mp4)

Lager med negativa offsetfaktorer kan bakas ned till tomma lager för att skapa nya positiva former.

Lager med positiva offsetfaktorer över 1 kan användas för att experimentera med mer extrema blendshapes.
:::

::: warning
För närvarande delar lager endast en enda opacitetskanal för alla 3 kanaler (färg/metallhet/råhet).
Om du slår ihop flera lager med kanalvis intensitet som inte är på full intensitet är det möjligt att slutresultatet ser annorlunda ut.

Kanske kommer varje kanal i framtiden att ha sin egen alfakanal för att ta bort denna begränsning.
:::


#### ![](/icons/tool_mask.webp) Mask {#mask}
Maskknappen bredvid varje reglage skapar en mask från den kanalen. Liknande hur lager används för att göra markeringar i målningsprogram gör detta att du kan återanvända arbete du gjort i ett lager för andra operationer.

#### ![](/icons/preview.webp) Förhandsvisning {#preview}
![](/images/layers_preview.webp) 

När den är aktiverad förhandsvisas extraheringsinställningarna för detta lager (se nästa avsnitt).

När röntgenläge är aktiverat kommer endast den extraherade formen att vara solid, resten av formen görs transparent, vilket är användbart om du använder negativa extraheringshöjder.

#### Extrahera {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Knappen `Extract` duplicerar innehållet i lagret till ett nytt objekt, vanligtvis med en användarspecificerad tjocklek som ställs in i nästa avsnitt.

`Closing action` avgör hur dupliceringen görs:

* None - Extrahera helt enkelt delen, försök inte skapa sidor eller fylla några hål.
* Fill - Hålet fylls och jämnas ut med trianglar. Använd inte det här alternativet för plana ytor.
* Shell - Stäng den extraherade formen med tjockleksvärdet och riktningsalternativen.
* Layer - Extrahera lagerskillnaden.

#### ![](/icons/height.webp) Tjocklek {#thickness}
![](/images/layers_thickness.webp) 

Djupet på skalextruderingen. Positiva värden växer ut från ytan, negativa värden växer in i ytan.

Plus/minus bredvid detta värde ställer in extruderingens riktning:
* Minus ( - ) börjar från den aktuella ytan och extruderar nedåt. 
* Plus ( + ) börjar från den aktuella ytan och extruderar uppåt.
* PlusMinus ( ± ) skjuter extruderingens topp och botten bortåt med lika stora mängder, så att den blir till hälften inbäddad i den ursprungliga ytan.

#### Släthet {#smoothness}
![](/images/layers_smoothness.webp) 

Om kanterna på området som ska extraheras är taggiga försöker detta reglage sudda ut kanten till en mjukare form. 

#### ![](/icons/height.webp) Kantögla (sida) {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Detta avsnitt är synligt när closing action är ”Shell”. 

`Auto Edge-loop (side)` beräknar antalet kantloopar längs skalets sidor för att skapa fyrkantiga polygoner. 

Om det är inaktiverat ställer reglaget `Division` in antalet indelningar på sidorna.

_Detta är slutet på undermenyn ”More...“._

### Avancerat {#advanced}
![](/images/layers_advanced.webp)

#### Behåll detalj i översta lager {#keep-top-layers-details}

Säkerställ att små detaljer på högre lager förblir synliga när stora förändringar görs på lägre lager.

Som standard, om du skulpterar små rynkor på ett lager och sedan gör stora ändringar på baslagret, kommer rynkorna att försvinna. Om du aktiverar denna växel kan dessa små detaljer alltid flyta ovanför de lägre stora förändringarna. I följande video kan du se hur rynkdetaljen tas bort som standard, men förblir synlig när ”keep top layers details” är aktiverat:

![](/videos/layers_details.mp4)


#### UI: Fäll ut lista {#ui-expand-list}

Standardlagermenyn låter dig växla lagersynlighet och lageropacitet. Om du aktiverar det här alternativet expanderas fullständiga kontroller för varje lager.

![](/images/layers_expand.webp)

#### Synka transformering {#sync-transform}

Om det är aktiverat kommer alla icke-markerade lager att justeras beroende på transformens rotation, skala, skevning. 

Inaktivera det här alternativet om de andra lagren är avsedda att användas utan den nya transform som du applicerar.

När den är inställd på `Auto` kommer endast de synliga lagren att justeras.