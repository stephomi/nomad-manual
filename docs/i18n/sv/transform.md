# ![](/icons/transform.webp) Transformera {#transform}

Den här menyn visar det valda objektets transformation som siffror: var det befinner sig, hur det är roterat och skalat, och hur stort det är. Skriv in exakta värden, återställ dem eller baka in dem i nätet.

![](/images/transform_overview.webp)

## Översikt {#overview}

Varje objekt har en nod som lagrar dess förflyttning, rotation och skala (dess matris), utöver dess vertexar. Verktygen [Gizmo](tools.md#gizmo) och [Transformera](tools.md#transform) ändrar den matrisen när du drar i vyn; med den här menyn kan du läsa av den och skriva in värdena i stället. Se [Noder och vertexar](tools.md#nodes-and-vertices) för skillnaden mellan att flytta noden och att flytta vertexarna.

Dra ett värde åt vänster eller höger för att ändra det, eller tryck på det för att skriva in ett tal. X-, Y- och Z-värdena är färgade röda, gröna och blå, precis som gizmons axlar.

::: tip
Att skriva in värden är praktiskt för att placera objekt exakt, till exempel för att lägga flera delar på precis samma höjd, eller för att få tillbaka en rotation till ett jämnt tal efter en fri rotation med gizmon.
:::

## Matris {#matrix}

Rubriken visar i vilket rum värdena uttrycks: `lokal` (relativt föräldraobjektet) eller `värld`.

### Objekt och Pivot {#object-pivot}

* `Objekt` - Värdena är objektets egen transformation.
* `Pivot` - Värdena styr markeringen från dess [pivot](tools.md#pivot), på samma sätt som gizmons handtag: raderna visar noll, och när du ändrar dem flyttas, roteras eller skalas markeringen runt pivoten. Slå på `Redigera` (låsikonen) för att flytta bara pivoten medan objekten står still.

### Lokal och Värld {#local-world}

När objektet har en förälder eller barn, eller flera objekt är valda, kan du välja i vilket rum värdena visas: `Lokal` (relativt föräldern) eller `Värld`.

### Åtgärder {#actions}

| Åtgärd        | Ikon                          | Beskrivning |
| :-----------: | :---------------------------: | :---------- |
| Flytta ursprung | ![](/icons/target.webp)      | Flytta objektet till världens origo. |
| Baka          | ![](/icons/bake.webp)        | Tillämpa matrisen på vertexarna och återställ matrisen. Visuellt ändras ingenting, men objektets origo är nu världens origo. |
| Pivot         | ![](/icons/gizmo.webp)       | Baka in pivoten i objektet: objektets origo och orientering blir pivotens. Visuellt ändras ingenting. |
| Redigera      | ![](/icons/lock.webp)        | (Läget `Pivot`) Flytta bara pivoten. |
| Återställ     | ![](/icons/reset.webp)       | Återställ transformationen till identitet. I läget `Pivot` sätter den i stället tillbaka pivoten på sin plats. |

När det valda objektet har instanser ber bakningen om bekräftelse, med alternativet `Av-instans`: bakningen ändrar vertexarna, som instanserna delar.

### Förflyttning, Rotation, Skala {#translation-rotation-scale}

Objektets position, rotation (i grader) och skala, på X, Y och Z. De två knapparna i slutet av varje rad bakar in bara den delen av transformationen i vertexarna, eller återställer den.

En rad `Skevhet` visas också när objektet är skevt, till exempel efter en olikformig skalning av en roterad förälder.

### Jamförd skala {#uniform-scale}

När den är aktiverad är skalan ett enda värde, samma på alla tre axlarna. Avaktivera den för att skala X, Y och Z var för sig.

## Dimension {#dimension}

Storleken och mitten på markeringens omslutande låda, i världsenheter. Med flera objekt valda omfattar den alla.

* `Storlek` - Bredd, höjd och djup. Med länkknappen på skalas de två andra storlekarna lika mycket när du ändrar en, så proportionerna behålls.
* `Mitten` - Mitten på den omslutande lådan. Måltavleknappen flyttar markeringen så att dess mitt hamnar i världens origo.

::: tip
`Storlek` är det snabbaste sättet att ge ett objekt en verklig storlek, till exempel inför en 3d-utskrift: ställ in höjden du vill ha, så behåller länken proportionerna.
:::
