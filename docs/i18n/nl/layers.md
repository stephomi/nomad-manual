# ![](/icons/layer.webp) Lagen {#layers}

Dit menu bevat de lagenstapel: een manier om aanpassingen aan je object niet-destructief op te slaan, met veel mogelijkheden om lagen te combineren en opnieuw te gebruiken.

![](/images/layers_overview.webp) 

## Overzicht {#overview}

Lagen in Nomad hebben meerdere functies.

Schilderinformatie (kleur, ruwheid, metaalheid, dekking) werkt met lagen zoals in 2d-tekenapps. Je maakt een laag aan en schildert op het model. Je kunt de laag aan- en uitzetten, de dekking aanpassen, de laag dupliceren, de volgorde in de lagenstapel veranderen en de mengmodus aanpassen.

Nomad gebruikt lagen ook voor sculpten. Een laag kan fijne details zoals rimpels bevatten, maar ook grote veranderingen, zodat ze werken zoals blendshapes/shape keys/morph targets in andere 3d-programma's. Je kunt bijvoorbeeld verschillende gezichtsuitdrukkingen op verschillende lagen sculpten en met de schuifregelaars van de lagen nieuwe uitdrukkingen samenstellen.

In dat geval zijn de veranderingen in een laag puur optellend: de volgorde van de lagen maakt niet uit, anders dan bij schilderen.

Met het gereedschap [LaagVerwijderen](tools.md#delete-layer) wis je een laag gedeeltelijk, en je kunt lagen ook gebruiken om maskers te maken op basis van de verschillende informatie die erin zit.

![](/videos/layer.mp4)

::: tip
Anders dan in de meeste sculptprogramma's gaan de lagen niet verloren als je de topologie van een mesh verandert. Je kunt de [voxel-remesh](topology.md#voxel-remesher), de [multiresolutie](topology.md#multiresolution) of de gereedschappen [Trimmen](tools.md#trim)/[Splitsen](tools.md#split) gebruiken, maar let op: met de [voxel-remesh](topology.md#voxel-remesher) gaat de kwaliteit van de laag erop achteruit.
:::

::: tip
Gebruik je lagen voor blendshapes/morph targets, dan vind je extra laagfuncties in het [menu Scène](scene.md#object-menu): je kunt lagen naar aparte objecten splitsen, en overeenkomende objecten samenvoegen tot lagen.
:::
----

## Lagenmenu {#layer-menu}

![](/images/layers_menu.webp)

De titel toont de naam van het geselecteerde object. Lagen zijn niet beschikbaar voor primitieven, dus valideer de primitief eerst.

Druk op `Laag toevoegen` om een nieuwe laag te maken. `Lagen Samenvoegen` voegt alle lagen samen in de basismesh; het getal naast het icoon geeft aan hoeveel lagen er zijn.

Elke laag heeft een naam, een schuifregelaar voor de sterkte/factor, en optieknoppen. Tik op een laag om hem actief te maken: sculpten en schilderen gaan dan naar die laag. Tik op `Basis` om weer aan de basismesh te werken.

### ![](/icons/sort_right.webp) Lijst uitvouwen {#ui-expand-list}

Standaard toont de lagenlijst alleen de zichtbaarheid, de mengmodus en de sterkte van elke laag, en is alleen de actieve laag uitgevouwen met al zijn bedieningselementen. Met de pijl links van de titel vouw je alle bedieningselementen van elke laag uit.

![](/images/layers_expand.webp)

### Opties {#options}

| Actie        | Icoon                        | Beschrijving                                        |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Zichtbaar    | ![](/icons/eye_open.webp)   | Toont of verbergt de laag                           |
| Mengmodus    | ![](/icons/opacity.webp)    | Mengmodus zoals in Photoshop. De 4 iconen tonen de modi voor kleur, ruwheid, metaalheid en dekking. |
| Hernoem      | ![](/icons/pencil.webp)     | Wijzigt de naam van de laag                         |
| Verwijderen  | ![](/icons/trash.webp)      | Verwijdert de laag                                  |
| Klonen       | ![](/icons/clone.webp)      | Dupliceert de laag                                  |
| Samenvoegen naar beneden | ![](/icons/merge_down.webp) | Voegt de laag samen met de laag eronder (of met de basismesh) |
| Meer         | ![](/icons/more.webp)       | [Meer...](#more) opties                             |

Is een laag niet uitgevouwen, dan vind je `Hernoem`, `Verwijderen`, `Klonen` en `Samenvoegen naar beneden` in het menu [Meer...](#more).

Om een laag naar een andere plek in de lagenstapel te verplaatsen, houd je de naam ingedrukt en sleep je hem.

### Basis {#base}

De knop met de 3 puntjes in de rij `Basis` verplaatst het schilderwerk van de basismesh naar een nieuwe laag, met de knop `Basis → Laag`. De basis wordt daarna teruggezet op het achtergrondmateriaal. Handig als je al veel hebt geschilderd voordat je een laag aanmaakte.

* Met de masker- en verbergknoppen ernaast blijven gemaskerde en verborgen gebieden onaangeroerd.
* `Extraheer` - de kanalen die worden verplaatst: `Kleur`, `Dekking`, `Ruwheid` en `Metaalheid`.
* `Achtergrondmateriaal` - als dit aanstaat, worden alleen de waarden verplaatst die van dit materiaal afwijken. Stel het in met de schuifregelaars, of neem het met de pipet over van het model.

### ![](/icons/more.webp) Meer... {#more}

De knop 'Meer...' toont extra opties voor de huidige laag, verdeeld over twee tabbladen: de instellingen (tandwielicoon) en het extraheren (kubusicoon).

![](/images/layers_more.webp) 

#### Kanaalfactoren {#channel-factors}

Met deze regelaars schaal je de hoeveelheid sculpt, kleur, ruwheid, metaalheid en dekking van de laag. De waarden worden vermenigvuldigd met de factorschuifregelaar van de laag: is de sterkte van de laag bijvoorbeeld 1 maar de factor van het kleurkanaal 0.5, dan wordt de kleur op sterkte 0.5 getoond.

`Offset` regelt de sterkte van het sculptwerk in de laag. Kleur, ruwheid en metaalheid blijven tussen 0 en 1, maar de offset kan elke waarde hebben, zowel positief als negatief.

::: tip
Met de offset maak je van een laag met bobbels een laag met holtes, of van een glimlach een frons:
![](/videos/layer_happysad.mp4)


Een symmetrische laag kun je klonen en daarna met LaagVerwijderen opsplitsen in een linker- en rechtervorm:
![](/videos/layer_leftright.mp4)

Lagen met een negatieve offset kun je bakken naar lege lagen om nieuwe positieve vormen te maken.

Lagen met een positieve offset boven 1 kun je gebruiken om te experimenteren met extremere blendshapes.
:::

::: warning
Op dit moment delen lagen één enkel dekkingskanaal voor alle 3 de kanalen (kleur/metaalheid/ruwheid).
Voeg je meerdere lagen samen met een intensiteit per kanaal die niet op vol staat, dan kan het eindresultaat er anders uitzien.

Misschien krijgt in de toekomst elk kanaal een eigen alfakanaal, zodat deze beperking verdwijnt.
:::


#### ![](/icons/shield.webp) Masker {#mask}
De maskerknop naast elke schuifregelaar maakt een masker van dat kanaal. Net zoals je in tekenapps lagen gebruikt om selecties te maken, kun je zo werk dat je in een laag hebt gedaan hergebruiken voor andere bewerkingen.

#### ![](/icons/preview.webp) Voorbeeld {#preview}
![](/images/layers_preview.webp) 

De volgende opties staan in het tabblad voor extraheren van het menu 'Meer...'.

Als dit aanstaat, zie je een voorbeeld van de extractie-instellingen voor deze laag (zie de volgende sectie).

`X-Ray` kiest welke objecten tijdens het voorbeeld doorzichtig worden (`Geen`, `Ongekozen`, `Geselecteerd` of `Alles`), zodat de geëxtraheerde vorm massief blijft. Handig als je negatieve extractiehoogtes gebruikt.

#### ![](/icons/mask_extract.webp) Extraheer {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

De knop `Extraheer` dupliceert de inhoud van de laag naar een nieuw object, meestal met een dikte die je zelf instelt in de volgende sectie.

`Sluitingsactie` bepaalt hoe het dupliceren gebeurt:

* `Geen` - Extraheert alleen het deel, zonder zijkanten te maken of gaten te vullen.
* `Vullen` - Het gat wordt gevuld met driehoeken en gladgemaakt. Gebruik deze optie niet voor vlakke oppervlakken.
* `Schil` - Sluit de geëxtraheerde vorm af met de opties voor dikte en richting.
* `Laag` - Extraheert het verschil van de laag.

#### ![](/icons/height.webp) Hoogte {#thickness}
![](/images/layers_thickness.webp) 

De diepte van de extrusie van de schil. Positieve waarden groeien uit het oppervlak, negatieve waarden groeien het oppervlak in. Verborgen wanneer de sluitingsactie `Laag` is.

Met de plus/min naast deze waarde stel je de richting van de extrusie in:
* Min ( - ) begint bij het huidige oppervlak en extrudeert naar beneden.
* Plus ( + ) begint bij het huidige oppervlak en extrudeert naar boven.
* PlusMin ( ± ) duwt de boven- en onderkant van de extrusie evenveel uit elkaar, zodat ze half in het oorspronkelijke oppervlak zit.

#### Zijden {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Deze sectie is zichtbaar wanneer de sluitingsactie `Schil` is.

`Wandverdelingen` bepaalt het aantal verdelingen langs de zijkanten van de schil. Staat de schakelaar `Auto` aan, dan berekent Nomad het aantal randlussen zodat de polygonen vierkant worden.

#### Gladheid {#smoothness}
![](/images/layers_smoothness.webp) 

Zijn de randen van het te extraheren gebied kartelig, zet deze optie dan aan om ze tot een mooiere vorm glad te maken. `Alle` maakt het hele geëxtraheerde oppervlak glad, `Alleen grenzen` alleen de randen. `Iteraties` bepaalt hoe sterk het gladmaken is.

_Hier eindigt het submenu 'Meer...'._

### ![](/icons/cog.webp) Geavanceerd {#advanced}
![](/images/layers_advanced.webp)

De knop `Geavanceerd` onderaan het menu verschijnt zodra het object lagen heeft.

#### Details bovenste lagen behouden {#keep-top-layers-details}

Zorgt dat kleine details op hogere lagen zichtbaar blijven wanneer je grote veranderingen aanbrengt op lagere lagen. Tijdens het sculpten wordt de vervorming uit de bovenste lagen genegeerd, maar hun details blijven zichtbaar. Dit werkt alleen goed als die bovenste lagen vrij kleine details bevatten.

Sculpt je standaard kleine rimpels op een laag en breng je daarna grote veranderingen aan op de basislaag, dan gaan de rimpels verloren. Met deze schakelaar blijven die kleine details altijd boven de grote veranderingen eronder zweven. In de volgende video zie je hoe het rimpeldetail standaard verdwijnt, maar zichtbaar blijft als 'Details bovenste lagen behouden' aanstaat:

![](/videos/layers_details.mp4)


#### Transformatie synchroniseren {#sync-transform}

Staat dit aan, dan worden alle niet-geselecteerde lagen aangepast aan de rotatie, schaal en scheefstand van de transformatie wanneer je de gereedschappen Gizmo of Transformeren gebruikt. Het kan op `Auto`, `Nee` of `Ja` staan.

Zet deze optie uit als de andere lagen bedoeld zijn om zonder de nieuwe transformatie te worden gebruikt.

Op `Auto` worden alleen de zichtbare lagen aangepast.
