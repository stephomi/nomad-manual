# ![](/icons/operation.webp) Operatie {#operation}

Dit menu past in één keer een bewerking toe op het hele oppervlak van de geselecteerde objecten: gladstrijken, ontspannen, polijsten, opblazen, de kleuren aanpassen, en het schilderwerk en het masker vervagen of verscherpen.

![](/images/operation_overview.webp)

## Overzicht {#overview}

Een penseel werkt waar je een streek zet, maar een operatie werkt in één keer op elke vertex van de geselecteerde objecten. De titel toont de naam van het object, of het aantal objecten als er meerdere geselecteerd zijn.

Elke operatie is een schuifregelaar: sleep naar rechts om meer toe te passen, naar links om minder toe te passen (of de tegenovergestelde bewerking, bij schuifregelaars met een pijl aan beide kanten). De schuifregelaar springt terug naar nul zodra je loslaat, en elke sleepbeweging is één stap in de [Geschiedenis](history.md), zodat je een operatie meerdere keren in kleine doses kunt toepassen.

::: tip
Met de operaties ruim je snel een hele mesh op na een voxel-remesh of een booleaanse bewerking: een beetje `Ontspannen` maakt de driehoeken gelijkmatiger, een beetje `Gladstrijken` haalt de ruis weg, zonder dat je elk plekje met een penseel hoeft op te zoeken.
:::

## Filters {#filters}

De knoppen bovenaan beperken waar de operaties werken:

* `Masker` - Gemaskerde gebieden blijven onaangeroerd.
* `Verbergen` - Verborgen gebieden blijven onaangeroerd.
* `Offset` - (Met een [laag](layers.md) geselecteerd) Alleen de gebieden waar de actieve laag sculptwerk bevat worden beïnvloed, zodat je de inhoud van een laag kunt gladstrijken of opblazen zonder de rest aan te raken.

## Gladstrijken {#smoothing}

* `Volume behouden` - Strijkt glad zonder dat het oppervlak krimpt. De tandwielknop bevat de waarden voor `Krimpen` en `Opblazen` die hiervoor worden gebruikt.
* `Randen behouden` - Vertices op de rand van de mesh (de rand van een gat) blijven op hun plek.
* `Stabiel gladstrijken` - Probeert het gladstrijken onafhankelijk te maken van de topologie. Dit werkt het best wanneer de dichtheid van de polygonen sterk wisselt.
* `Gladstrijken` - Strijkt het oppervlak glad. Sleep naar links om het in plaats daarvan te `Verscherpen`.
* ![](/icons/group.webp) `Gladstrijken` - Strijkt de grenzen tussen [vlakkengroepen](tools.md#facegroup) glad, zodat kartelige groepsranden rechter worden. Sleep naar links om ze te verscherpen.
* `Ontspannen` - Maakt de polygonen gelijkmatiger en behoudt de vorm.
* ![](/icons/group.webp) `Ontspannen` - Ontspant de polygonen langs de grenzen van vlakkengroepen.
* `Hoeken behouden` - Met `Gladstrijken` en `Ontspannen` voor vlakkengroepen blijven de grenzen vast op plekken waar ze meer dan deze hoek afbuigen, zodat de hoeken scherp blijven terwijl de zijden glad worden. Zet het aan met het vinkje.

## Polijsten {#polish}

Maakt het oppervlak vlak in strakke facetten, zoals het gereedschap [Polijsten](tools.md#polish). `Hoek` bepaalt welke vlakken samen vlak worden: vlakken die minder dan deze hoek buigen, worden één facet. Een kleinere hoek behoudt meer vouwen en geeft kleinere facetten.

## Opblazen {#inflate}

Duwt het oppervlak naar buiten langs de normalen, of naar binnen als je naar links sleept. `Normaal (Ontspannen)` ontspant tegelijk de polygonen, zodat ze niet uitrekken; zet het uit met het vinkje.

## Kleuraanpassingen {#color-adjustments}

Kies het kanaal dat je wilt aanpassen: `Kleur`, `Ruwheid`, `Metaalheid`, `Dekking`, `Dichtheid` (de geschilderde dichtheid van de [Quad Remesher](tools.md#quad-remesher), als het object die heeft) of `Masker`. Daarna:

* `Belichting` - Maakt de waarden lichter of donkerder.
* `Verzadiging` - (Alleen `Kleur`) Meer of minder levendige kleuren.
* `Contrast` - Spreidt de waarden uit elkaar, of brengt ze dichter bij elkaar.
* `Kleurtoon` - Verschuift de kleuren over de kleurencirkel.

## Vervagen {#blur}

Vervaagt de gekozen kanalen over het oppervlak: zet `Kleur`, `Ruwheid`, `Metaalheid`, `Dekking`, `Dichtheid` of `Masker` aan en sleep dan aan `Vervagen`. Sleep naar links om in plaats daarvan te `Verscherpen`.

Voor het masker is dit hetzelfde als de schuifregelaar `Vervagen` van het gereedschap [Masker](tools.md#mask). Hier kun je ook de schilderkanalen vervagen.
