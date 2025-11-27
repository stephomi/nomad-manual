# ![](/icons/camera.webp) Camera

Dit menu laat je camera's maken en wijzigen, en bepaalt ook hoe je met camera's omgaat.

![](/images/camera_overview2.webp)

Camera's in Nomad hebben verschillende toepassingen:

* Weergaven instellen om vanuit precieze hoeken te beeldhouwen
* Gebruiken als fotocamera om je objecten in te kaderen
* Als een camera in eerste persoonsperspectief om door je scène te navigeren
* Als orthografische camera voor isometrische games of industriële stijlrendering.

## De camera bedienen

### Rotatie
Je roteert de camera door met *één* vinger over de achtergrond te slepen.
Als je met je vinger over je model sleept, start je in plaats daarvan de beeldhouwbewerking.

::: tip Kan ik de camera roteren als ik geen toegang heb tot de achtergrond?
Ja, je kunt *twee* vingers op het scherm plaatsen – alsof je een pan/zoom‑gebaar wilt starten – en dan *één* vinger loslaten.
:::

### Focus / Reset
*Dubbel tikken* op het model om te focussen op het gekozen punt.
Als je *dubbel tikt* op de achtergrond, focust de camera in plaats daarvan op de geselecteerde mesh.


### Translatie
Door *twee* vingers te bewegen kun je de camera pannen.


### Zoomen
Met het knijpgebaar kun je in- en uitzoomen.


### Rollen
Je kunt het beeld *rollen* door *twee* vingers te roteren.
::: warning
Dit gebaar is alleen beschikbaar voor de rotatiemodus `trackball`.
:::

### Desktop‑bediening

Op desktop wordt de alt/opt‑toets gebruikt om de camera te bedienen:

* tip slepen in lege ruimte = camera roteren
* alt+tip slepen = pannen
* alt+tip slepen, dan alt loslaten = zoomen (zoals in ZBrush)

Bij Wacom‑tablets met 2 of meer knoppen op de pen kun je in de Wacom‑instellingen de tip en knoppen als volgt configureren:

* tip = linkermuisklik
* onderste rocker = middelste muisklik
* bovenste rocker = rechtermuisklik

Met deze instellingen kun je de camera volledig met de pen bedienen:

* bovenste rocker en zwevend bewegen = camera roteren
* onderste rocker en zwevend bewegen = pannen

## Camerabediening

![](/images/camera_list.webp)

### Weergaven
Je kunt camerastandpunten opslaan met `Add View`.
Als je op de naam van de weergave klikt, herstelt de camera die weergave.


::: tip
Een opgeslagen weergave bewaart de instellingen van het [Projection Type](#projection-type) en ook de [Reference image](background.md).  
Dit kan handig zijn als je wilt wisselen tussen voor/links/achter‑referentieweergaven met verschillende achtergronden.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | De camera in- of uitschakelen. Verborgen camera's worden overgeslagen door de vorige/volgende‑knop |
| Name        |                               | De camera selecteren                                                        |
| Image       | ![](/icons/image.webp)       | Een miniatuur van een referentie‑afbeelding als die aan de camera is gekoppeld |
| Update View | ![](/icons/update_view.webp) | De opgeslagen weergave bijwerken met het huidige standpunt                 |
| Edit Name   | ![](/icons/pencil.webp)      | De cameranaam bewerken                                                      |
| Delete      | ![](/icons/trash.webp)       | De camera verwijderen                                                       |

### ![](/icons/tool_view.webp) Add View
Maak een nieuwe camera op basis van de huidige weergave.

### ![](/icons/camera.webp) Icons

Schakel in of camera‑iconen zichtbaar zijn in de viewport. Als een camera is geselecteerd, is het pictogram altijd zichtbaar.

### Projection Type
Je kunt de `Field of View` (FOV / brandpuntsafstand) van je camera wijzigen.
Voor beeldhouwen wordt meestal aangeraden een lage FOV te gebruiken, omdat dit kan helpen bij de verhoudingen.  
Je kunt ook de modus `Orthographic` gebruiken, die min of meer overeenkomt met een FOV gelijk aan 0.

### First Person
Schakel in om het draaipunt direct op de camera te plaatsen in plaats van op het beeldhouwwerk. Slepen met een vinger op de achtergrond vergrendelt de camerapositie, maar verandert de rotatie, vergelijkbaar met hoe spellen in eerste persoon werken. Handig bij het beeldhouwen van omgevingen in plaats van losse objecten.

![](/images/camera_rotation_ortho_view.webp)

### Rotation Type
Standaard gebruikt de camera de rotatiemodus `Turntable`.
Dit betekent dat je slechts twee vrijheidsgraden hebt; het is intuïtiever, maar in sommige gevallen wil je meer flexibiliteit.  
Je kunt overschakelen naar `Trackball`; dan kun je het beeld *rollen* door *twee* vingers op de viewport te roteren. Op desktop is er een alternatieve trackball‑modus die voor sommige gebruikers vertrouwder kan zijn.

### Orthographic snap

Indien ingeschakeld, zal de camera, als je een toetsenbord hebt en shift ingedrukt houdt tijdens het roteren van de weergave, vastklikken naar de dichtstbijzijnde voor/achter/boven/onder/links/rechts‑weergave en orthografisch worden. De camera wordt ook orthografisch gemaakt wanneer op de view‑cube wordt geklikt om vast te klikken naar voor/achter/links/rechts/boven/onder.

### Reset view

Verplaats de camera naar voren en pas de scène in de weergave.

### Snap view
Klik vast naar de dichtstbijzijnde voor/achter/links/rechts/boven/onder‑weergave. Als je je al in een van deze weergaven bevindt, zal nogmaals klikken 180 graden naar de tegenoverliggende zijde vastklikken.

### Speed

Als je vindt dat de camera te langzaam of te snel beweegt, kun je een snelheidsvermenigvuldiger instellen voor `rotation`, `translation` en `zooming`. Handig als je sculptuur erg groot of erg klein is.

### Pivot‑overzicht

Wanneer je de camera roteert, zie je een kleine roze stip; dit is je draaipunt (pivot) van de camera.  
Het is erg belangrijk te begrijpen waar je draaipunt zich bevindt, zodat je niet verdwaalt of gefrustreerd raakt door de camera.

Standaard wordt het draaipunt bijgewerkt via deze handelingen:
- dubbel tikken op het model
- dubbel tikken op de achtergrond (het nieuwe draaipunt komt in het midden van je mesh)
- *twee* vingers op het scherm plaatsen (pan/zoom/rollen) zal het draaipunt bijwerken naar het midden van de *twee* vingers

### Update Pivot...

Je kunt verder aanpassen wanneer het draaipunt wordt bijgewerkt met deze opties:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Als je eraan gewend bent, kun je de (hint) roze stip verbergen in de [Settings](settings.md)‑menu's.
:::

### Double tap on object
Wanneer `Focus` is ingeschakeld, verplaatst dubbel tikken het draaipunt naar het getikte object.

### Double tap on background
Indien ingeschakeld, stel het draaipunt in op een van Selection, Scene, of wissel daartussen.
