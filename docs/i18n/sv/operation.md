# ![](/icons/operation.webp) Operation {#operation}

Den här menyn tillämpar en operation på hela ytan av de valda objekten på en gång: jämna ut, slappna av, polera, blås upp, justera färgerna, gör målningen och masken suddigare eller skarpare.

![](/images/operation_overview.webp)

## Översikt {#overview}

Medan en pensel bara verkar där du drar, verkar en operation på varje vertex i de valda objekten i ett enda svep. Rubriken visar objektets namn, eller antalet objekt när flera är valda.

Varje operation är ett skjutreglage: dra det åt höger för att tillämpa mer, åt vänster för att tillämpa mindre (eller den motsatta operationen, för reglage med en pil på båda sidor). Reglaget går tillbaka till noll när du släpper det, och varje drag blir ett enda steg i [Historik](history.md), så du kan tillämpa en operation flera gånger i små doser.

::: tip
Operationerna är ett snabbt sätt att städa upp ett helt nät efter en voxel-remesh eller en boolesk operation: lite `Slappna av` jämnar ut trianglarna, lite `Jämna ut` tar bort bruset, utan att du behöver leta upp varje ställe med en pensel.
:::

## Filter {#filters}

Knapparna högst upp begränsar var operationerna verkar:

* `Mask` - Maskerade områden lämnas orörda.
* `Dölj` - Dolda områden lämnas orörda.
* `Förskjutning` - (Med ett [lager](layers.md) valt) Bara de områden där det aktiva lagret innehåller skulptering påverkas, så du kan jämna ut eller blåsa upp innehållet i ett lager utan att röra resten.

## Utjämning {#smoothing}

* `Bevara volymen` - Jämnar ut utan att ytan krymper. Kugghjulsknappen innehåller värdena för `Krymp` och `Blås upp` som används för det.
* `Bevara kanter` - Vertexar på nätets kant (kanten runt ett hål) står stilla.
* `Stabil utjämning` - Försöker göra utjämningen oberoende av topologin. Fungerar bäst när polygontätheten varierar mycket.
* `Jämna ut` - Jämnar ut ytan. Dra åt vänster för att `Skärpa` den i stället.
* ![](/icons/group.webp) `Jämna ut` - Jämnar ut gränserna mellan [ytgrupper](tools.md#facegroup) och rätar ut taggiga gruppkonturer. Dra åt vänster för att skärpa dem.
* `Slappna av` - Jämnar ut polygonerna men behåller formen.
* ![](/icons/group.webp) `Slappna av` - Slappnar av polygonerna längs ytgruppernas gränser.
* `Bevara hörn` - Med ytgruppernas `Jämna ut` och `Slappna av` hålls gränserna fast där de svänger mer än den här vinkeln, så hörnen förblir skarpa medan sidorna jämnas ut. Slå på det med dess kryssruta.

## Polera {#polish}

Plattar ut ytan till rena fasetter, som verktyget [Polera](tools.md#polish). `Vinkel` bestämmer vilka ytor som plattas ut tillsammans: ytor som böjer sig mindre än den här vinkeln blir en enda fasett. En lägre vinkel behåller fler veck och mindre fasetter.

## Blås upp {#inflate}

Trycker ytan utåt längs dess normaler, eller inåt när du drar åt vänster. `Normal (Relax)` slappnar av polygonerna samtidigt så att de inte sträcks ut; stäng av det med dess kryssruta.

## Färgjusteringar {#color-adjustments}

Välj kanalen att justera, `Färg`, `Grovhet`, `Metallitet`, `Opacitet`, `Täthet` (tätheten som målas för [Quad Remesher](tools.md#quad-remesher), när objektet har någon) eller `Mask`, och sedan:

* `Exponering` - Gör värdena ljusare eller mörkare.
* `Mättnad` - (Bara `Färg`) Mer eller mindre livfulla färger.
* `Kontrast` - Sprider ut värdena, eller för dem närmare varandra.
* `Färgton` - Förskjuter färgerna runt färghjulet.

## Oskärpa {#blur}

Gör de valda kanalerna suddiga över ytan: slå på `Färg`, `Grovhet`, `Metallitet`, `Opacitet`, `Täthet` eller `Mask`, och dra sedan i `Oskärpa`. Dra åt vänster för att `Skärpa` i stället.

För masken är det samma sak som reglaget `Sudda` i verktyget [Mask](tools.md#mask). Här kan du göra även målningskanalerna suddiga.
