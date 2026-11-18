# ![](/icons/transform.webp) Transformeren {#transform}

Dit menu toont de transformatie van het geselecteerde object als getallen: waar het staat, hoe het gedraaid en geschaald is, en hoe groot het is. Typ exacte waarden, zet ze terug, of pas ze toe op de mesh.

![](/images/transform_overview.webp)

## Overzicht {#overview}

Elk object heeft naast zijn vertices een node die de verschuiving, rotatie en schaal opslaat (de matrix). De gereedschappen [Gizmo](tools.md#gizmo) en [Transformeren](tools.md#transform) veranderen die matrix wanneer je in de viewport sleept; in dit menu kun je hem aflezen en de waarden intypen. Zie [Nodes en vertices](tools.md#nodes-and-vertices) voor het verschil tussen de node verplaatsen en de vertices verplaatsen.

Sleep een waarde naar links of rechts om hem te veranderen, of tik erop om een getal te typen. De waarden voor X, Y en Z zijn rood, groen en blauw gekleurd, net als de assen van de gizmo.

::: tip
Waarden intypen is handig om objecten precies te plaatsen, bijvoorbeeld om meerdere onderdelen op exact dezelfde hoogte te zetten, of om na een vrije rotatie met de gizmo weer een rond getal te krijgen.
:::

## Matrix {#matrix}

De titel vertelt in welke ruimte de waarden zijn uitgedrukt: `lokaal` (ten opzichte van het ouderobject) of `wereld`.

### Object en draaipunt {#object-pivot}

* `Object` - De waarden zijn de eigen transformatie van het object.
* `Draaipunt` - De waarden sturen de selectie aan vanuit het [draaipunt](tools.md#pivot), net zoals de handvatten van de gizmo: de rijen staan op nul, en als je ze verandert, wordt de selectie rond het draaipunt verplaatst, gedraaid of geschaald. Zet `Bewerk` (het slotpictogram) aan om alleen het draaipunt te verplaatsen; de objecten blijven dan staan.

### Lokaal en wereld {#local-world}

Heeft het object een ouder of kinderen, of zijn er meerdere objecten geselecteerd, dan kies je in welke ruimte de waarden worden getoond: `Lokaal` (ten opzichte van de ouder) of `Wereld`.

### Acties {#actions}

| Actie         | Icoon                         | Beschrijving |
| :-----------: | :---------------------------: | :---------- |
| Verplaats oorsprong | ![](/icons/target.webp) | Verplaatst het object naar de oorsprong van de wereld. |
| Toepassen     | ![](/icons/bake.webp)        | Past de matrix toe op de vertices en zet de matrix terug. Visueel verandert er niets, maar de oorsprong van het object is nu de oorsprong van de wereld. |
| Draaipunt     | ![](/icons/gizmo.webp)       | Past het draaipunt toe op het object: de oorsprong en oriëntatie van het object worden die van het draaipunt. Visueel verandert er niets. |
| Bewerk        | ![](/icons/lock.webp)        | (Modus `Draaipunt`) Verplaatst alleen het draaipunt. |
| Reset         | ![](/icons/reset.webp)       | Zet de transformatie terug naar de identiteit. In de modus `Draaipunt` zet het in plaats daarvan het draaipunt terug op zijn plek. |

Heeft het geselecteerde object instanties, dan vraagt het toepassen om bevestiging, met een optie `Instantie opheffen`: toepassen verandert de vertices, en die worden door instanties gedeeld.

### Verschuiving, Rotatie, Schaal {#translation-rotation-scale}

De positie, rotatie (in graden) en schaal van het object, op X, Y en Z. De twee knoppen aan het eind van elke rij passen alleen dat deel van de transformatie toe op de vertices, of zetten het terug.

Er verschijnt ook een rij `Scheef` wanneer het object scheefgetrokken is, bijvoorbeeld na een niet-uniforme schaal van een gedraaide ouder.

### Uniforme schaal {#uniform-scale}

Staat dit aan, dan is de schaal één waarde, gelijk op alle drie de assen. Zet het uit om X, Y en Z apart te schalen.

## Afmeting {#dimension}

De grootte en het midden van het omhullende kader van de selectie, in wereldeenheden. Zijn er meerdere objecten geselecteerd, dan omvat het ze allemaal.

* `Grootte` - De breedte, hoogte en diepte. Staat de koppelingsknop aan, dan schaalt het veranderen van één maat de andere twee evenveel mee, zodat de verhoudingen behouden blijven.
* `Midden` - Het midden van het omhullende kader. De doelknop verplaatst de selectie zodat het midden op de oorsprong van de wereld ligt.

::: tip
Met `Grootte` geef je een object het snelst een echte afmeting, bijvoorbeeld voor een 3d-print: stel de gewenste hoogte in, en de koppeling behoudt de verhoudingen.
:::
