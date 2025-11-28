# ![](/icons/layer.webp) Lagen {#layers}

Dit menu bevat de lagenstapel: een manier om bewerkingen op je object niet-destructief op te slaan, en veel manieren om lagen te combineren en opnieuw te gebruiken.

![](/images/layers_overview.webp) 

## Overzicht {#overview}

Nomad-lagen hebben meerdere functies.

Verfinformatie (Kleur, Ruwheid, Metalness, Opaciteit) werkt met lagen op een vergelijkbare manier als in 2D-schilderapplicaties. Je kunt een laag aanmaken en verf op een model aanbrengen. De laag kan aan- of uitgezet worden, de dekking kan worden aangepast, de laag kan worden gedupliceerd, de volgorde in de lagenstapel kan worden gewijzigd en de overvloeimodus kan worden aangepast.

Nomad gebruikt lagen ook voor sculpting. Een laag kan fijne details zoals rimpels opslaan, of grote veranderingen, waardoor ze kunnen functioneren als blendshapes/shape keys/morph targets in andere 3D-applicaties. Je zou bijvoorbeeld verschillende gezichtsuitdrukkingen op verschillende lagen kunnen sculpteren en vervolgens de schuifregelaars van de lagen aanpassen om ze te combineren tot nieuwe uitdrukkingen.

In dit geval zijn de veranderingen die in een laag worden opgeslagen puur additief; de laagvolgorde is niet van belang zoals bij verf.

Lagen kunnen gedeeltelijk worden gewist via het gereedschap [Delete Layer](tools.md#delete-layer), en lagen kunnen ook worden gebruikt om maskers te maken op basis van de verschillende informatie die in de laag is opgeslagen.

![](/videos/layer.mp4)

::: tip
In tegenstelling tot de meeste sculptsoftware worden lagen niet verwijderd als je de topologie van een mesh wijzigt. Je kunt de [Voxel Remesher](topology.md#voxel-remesher), de [Multiresolution](topology.md#multires) of de gereedschappen [Trim](tools.md#trim)/[Split](tools.md#split) gebruiken, maar houd er rekening mee dat bij gebruik van de [Voxel Remesher](topology.md#voxel-remesher) de kwaliteit van de laag wordt beïnvloed.
:::

::: tip
Als je lagen gebruikt voor blendshapes/morph targets, is er extra laagfunctionaliteit in het [scenemenu](scene.md#object-menu). Je kunt lagen opsplitsen in objecten en overeenkomende objecten combineren tot lagen.
:::
----

## Laagmenu {#layer-menu}

![](/images/layers_menu.webp)

Druk op `Add layer` om een nieuwe laag te maken.

Elke laag heeft een naam, een schuifregelaar om de sterkte/factor te regelen, en knopopties.

### Opties {#options}

| Actie        | Icoon                        | Beschrijving                                        |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Zichtbaar    | ![](/icons/eye_open.webp)   | Laag tonen/verbergen                                |
| Blend Mode   | ![](/icons/opacity.webp)    | De Photoshop-achtige overvloeimodus. De 4 iconen tonen de modi voor Kleur, Ruwheid, Metalness, Opaciteit. |
| Naam bewerken| ![](/icons/pencil.webp)     | De naam van de laag bewerken                       |
| Verwijderen  | ![](/icons/trash.webp)      | De laag verwijderen                                 |
| Dupliceren   | ![](/icons/clone.webp)      | De laag dupliceren                                  |
| Samenvoegen omlaag | ![](/icons/merge_down.webp) | De laag samenvoegen met de onderliggende laag (of basismesh) |
| Meer         | ![](/icons/more.webp)       | [Meer...](#more) opties                             |

Om een laag naar een andere positie in de lagenstapel te verplaatsen, houd je de naam ingedrukt en sleep je deze.

### Meer... {#more}

De knop ‘More...’ toont extra opties voor de huidige laag:

![](/images/layers_more.webp) 

#### Kanalenfactoren {#channel-factors}

Met deze bedieningselementen kun je de hoeveelheid sculpt/kleur/ruwheid/metalness/opaciteit voor de laag schalen. Deze waarden worden vermenigvuldigd met de factor-schuifregelaar van de laag. Dus als bijvoorbeeld de laagsterkte 1 is, maar de channelfactor voor kleur 0,5, dan wordt de kleur weergegeven met een sterkte van 0,5.

`Offset` regelt de sculptsterkte van de laag. Terwijl kleur/ruwheid/metalness worden begrensd tussen 0 en 1, kan offset elke waarde aannemen, zowel positief als negatief. 

::: tip
Offset kan worden gebruikt om een laag met bulten te veranderen in een laag met holtes, of een glimlach in een frons:
![](/videos/layer_happysad.mp4)


Een symmetrische laag kan worden gekloond en vervolgens met del layer worden opgesplitst in linker-/rechtervormen:
![](/videos/layer_leftright.mp4)

Lagen met negatieve offsetfactoren kunnen worden gebakken naar lege lagen om nieuwe positieve vormen te maken.

Lagen met positieve offsetfactoren boven 1 kunnen worden gebruikt om te experimenteren met extremere blendshapes.
:::

::: warning
Op dit moment delen lagen slechts één opaciteitskanaal voor alle 3 kanalen (kleur/metalness/ruwheid).
Als je meerdere lagen samenvoegt met kanaalspecifieke intensiteit die niet op volledige intensiteit staat, is het mogelijk dat het eindresultaat er anders uitziet.

Misschien zal in de toekomst elk kanaal zijn eigen alfakanaal hebben om deze beperking te verwijderen.
:::


#### ![](/icons/tool_mask.webp) Masker {#mask}
De maskknop naast elke schuifregelaar maakt een masker van dat kanaal. Vergelijkbaar met het gebruik van lagen om selecties te maken in schilderapplicaties, kun je hiermee werk dat je in een laag hebt gedaan hergebruiken voor andere bewerkingen.

#### ![](/icons/preview.webp) Voorbeeld {#preview}
![](/images/layers_preview.webp) 

Indien ingeschakeld, wordt een voorbeeld getoond van de extract-instellingen voor deze laag (zie de volgende sectie).

Wanneer röntgen (xray) is ingeschakeld, zal alleen de geëxtraheerde vorm solide zijn; de rest van de vorm wordt transparant gemaakt, wat handig is als je negatieve extractiehoogtes gebruikt.

#### Extractie {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

De knop `Extract` dupliceert de inhoud van de laag naar een nieuw object, meestal met een door de gebruiker gespecificeerde dikte die wordt ingesteld in de volgende sectie.

`Closing action` bepaalt hoe de duplicatie wordt uitgevoerd:

* None - Extraheer het deel simpelweg, probeer geen zijkanten te genereren of gaten te vullen.
* Fill - Het gat wordt gevuld en gladgemaakt met driehoeken. Gebruik deze optie niet voor vlakke oppervlakken.
* Shell - Sluit de geëxtraheerde vorm met de diktewaarde en richtingsopties.
* Layer - Extraheer het laagverschil.

#### ![](/icons/height.webp) Dikte {#thickness}
![](/images/layers_thickness.webp) 

De diepte van de shell-extrusie. Positieve waarden groeien uit het oppervlak, negatieve waarden groeien in het oppervlak.

De plus/min-knop naast deze waarde bepaalt de richting van de extrusie:
* Min ( - ) begint vanaf het huidige oppervlak en extrudeert naar beneden. 
* Plus ( + ) begint vanaf het huidige oppervlak en extrudeert naar boven.
* PlusMinus ( ± ) duwt de boven- en onderkant van de extrusie met gelijke hoeveelheden uit elkaar, zodat deze half in het oorspronkelijke oppervlak wordt ingebed.

#### Gladheid {#smoothness}
![](/images/layers_smoothness.webp) 

Als de randen van het gebied dat moet worden geëxtraheerd gekarteld zijn, zal deze schuifregelaar proberen de rand te vervagen tot een gladdere vorm. 

#### ![](/icons/height.webp) Randlus (zijkant) {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Deze sectie is zichtbaar wanneer de closing action ‘Shell’ is. 

`Auto Edge-loop (side)` berekent het aantal edge loops langs de shellzijkanten om vierkante polygonen te creëren. 

Indien uitgeschakeld, bepaalt de schuifregelaar `Division` het aantal verdelingen aan de zijkanten.

_Einde van het submenu ‘More...’._

### Geavanceerd {#advanced}
![](/images/layers_advanced.webp)

#### Bovenste laagdetails behouden {#keep-top-layers-details}

Zorgt ervoor dat kleine details op hogere lagen zichtbaar blijven wanneer grote veranderingen op lagere lagen worden aangebracht.

Standaard geldt: als je kleine rimpels op een laag sculpteert en vervolgens grote veranderingen aan de basislaag aanbrengt, gaan de rimpels verloren. Door deze schakelaar in te schakelen, blijven die kleine details altijd boven de grote veranderingen op de lagere lagen zweven. In de volgende video zie je hoe de rimpeldetails standaard worden verwijderd, maar zichtbaar blijven wanneer ‘keep top layers details’ is ingeschakeld:

![](/videos/layers_details.mp4)


#### UI: Lijst uitklappen {#ui-expand-list}

In het standaard lagenmenu kun je de zichtbaarheid van lagen en de dekking van de laag aanpassen. Als je deze optie inschakelt, worden de volledige bedieningselementen voor elke laag uitgevouwen.

![](/images/layers_expand.webp)

#### Transformatie synchroniseren {#sync-transform}

Indien ingeschakeld, worden alle niet-geselecteerde lagen aangepast op basis van de transformatierotatie, schaal en skew. 

Schakel deze optie uit als de andere lagen bedoeld zijn om te worden gebruikt zonder de nieuwe transformatie die je toepast.

Wanneer ingesteld op `Auto`, worden alleen de zichtbare lagen aangepast.