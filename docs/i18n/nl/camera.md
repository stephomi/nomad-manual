# ![](/icons/camera.webp) Camera {#camera}

In dit menu maak en bewerk je camera's, en bepaal je hoe je met de camera werkt.

![](/images/camera_overview2.webp)

Camera's hebben in Nomad verschillende toepassingen:

* aanzichten instellen om vanuit precieze hoeken te sculpten
* als fotocamera om je objecten in beeld te brengen
* als camera in de eerste persoon om door je scène te navigeren
* als orthografische camera voor isometrische games of renders in industriële stijl.

## De camera bedienen {#control}

### Rotatie {#rotation}
Je draait de camera door met *één* vinger over de achtergrond te slepen.
Sleep je met je vinger over je model, dan begin je in plaats daarvan te sculpten.

::: tip Kan ik de camera draaien als ik niet bij de achtergrond kan?
Ja: zet *twee* vingers op het scherm, alsof je wilt verschuiven of zoomen, en laat dan *één* vinger los.
:::

### Focus / Herstellen {#focus}
*Dubbeltik* op het model om op het aangetikte punt te focussen.
*Dubbeltik* je op de achtergrond, dan focust de camera op de geselecteerde mesh of op de hele scène, zie [Dubbel tik op achtergrond](#dtap-tap-background).


### Verplaatsen {#translation}
Door *twee* vingers te bewegen, verschuif je de camera.


### Inzoomen {#zooming}
Met het knijpgebaar zoom je in en uit.


### Rollen {#rolling}
Je kunt de weergave *rollen* door *twee* vingers te draaien.
::: warning
Dit gebaar is alleen beschikbaar in de rotatiemodi `Trackball`.
:::

### Bediening op desktop {#desktop}

Op desktop gebruik je de toets alt/opt om de camera te bedienen:

* met de punt slepen in een lege ruimte = camera draaien
* alt+slepen met de punt = verschuiven
* alt+slepen met de punt, dan alt loslaten = zoomen (zoals in ZBrush)

Heb je een Wacom-tablet met 2 of meer knoppen op de pen, stel de punt en de knoppen dan zo in via de Wacom-instellingen:

* punt = linkerklik
* onderste knop = middelste klik
* bovenste knop = rechterklik

Met die instellingen bedien je de camera volledig met de pen:

* bovenste knop en zwevend bewegen = camera draaien
* onderste knop en zwevend bewegen = verschuiven

## Camerabediening {#camera-controls}

![](/images/camera_list.webp)

### Weergaven {#views}
Met `Weergave toevoegen` sla je camerastandpunten op.
Klik je op de naam van de weergave, dan zet de camera die weergave terug.


::: tip
Een opgeslagen weergave bewaart de instellingen van het [Projectietype](#projection) en ook de [referentieafbeelding](background.md).  
Handig als je wilt wisselen tussen referentieaanzichten van voren, links en achteren met elk een andere achtergrond.
:::

| Actie       | Icoon                         | Beschrijving                                                                |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Zichtbaar   | ![](/icons/eye_open.webp)    | Zet de camera aan of uit. Verborgen camera's worden overgeslagen door de knoppen vorige/volgende |
| Naam        |                               | Selecteert de camera                                                        |
| Afbeelding  | ![](/icons/image.webp)       | Een miniatuur van de referentieafbeelding, als die aan de camera is gekoppeld |
| Projectie   | ![](/icons/perspective.webp) | De projectie van de camera, met het gezichtsveld in perspectief             |
| Weergave bijwerken | ![](/icons/update_view.webp) | Werkt de opgeslagen weergave bij met het huidige standpunt          |
| Hernoem     | ![](/icons/pencil.webp)      | Wijzigt de naam van de camera                                               |
| Verwijderen | ![](/icons/trash.webp)       | Verwijdert de camera                                                        |

### ![](/icons/camera_add.webp) Weergave toevoegen {#add}
Maakt een nieuwe camera op basis van de huidige weergave.

### ![](/icons/camera.webp) Iconen {#icons-test}

Bepaalt of de camera-iconen in de viewport zichtbaar zijn. De knop verschijnt naast `Weergave toevoegen` zodra je een camera hebt. Het icoon van een geselecteerde camera is altijd zichtbaar.

### Projectietype {#projection}
Kies tussen `Perspectief` en `Orthografisch`.

In perspectief kun je het `Verticaal gezichtsveld` (field of view, FOV) van je camera aanpassen. De bijbehorende brandpuntsafstand van een 35mm-camera staat boven de schuifregelaar, handig als je gewend bent aan fotografie.
Voor het sculpten raden we meestal een kleine FOV aan, omdat dat helpt bij de verhoudingen.  
De modus `Orthografisch` komt min of meer overeen met een FOV van 0.

### Eerste Persoon {#fps}
Alleen in perspectief. Zet het draaipunt direct op de camera, in plaats van op de sculpt. Slepen met een vinger over de achtergrond houdt de camera op zijn plek maar verandert de rotatie, zoals in games in de eerste persoon. Handig wanneer je omgevingen sculpt in plaats van losse objecten.

![](/images/camera_rotation_ortho_view.webp)

### Rotatietype {#rotation-type}
Standaard gebruikt de camera de rotatiemodus `Draaischijf`.
Je hebt dan maar twee vrijheidsgraden. Dat is intuïtiever, maar soms wil je meer flexibiliteit.  
Schakel je over naar `Trackball`, dan kun je de weergave *rollen* door *twee* vingers op de viewport te draaien. Er zijn twee modi `Trackball`: de eerste rolt de weergave als een bal onder je vinger, de tweede (met het pijlenicoon) draait de weergave op basis van de horizontale en verticale beweging van je sleepbeweging, wat voor sommige gebruikers vertrouwder aanvoelt.

### Orthografische snap {#orthographic}

Staat dit aan en heb je een toetsenbord, dan snapt de camera naar het dichtstbijzijnde voor-, achter-, boven-, onder-, linker- of rechteraanzicht als je shift ingedrukt houdt tijdens het draaien, en wordt de camera orthografisch. De camera wordt ook orthografisch wanneer je op de navigator klikt om naar het voor-, achter-, linker-, rechter-, boven- of onderaanzicht te springen.

### Weergave herstellen {#reset}

Zet de camera vooraan en past de scène in beeld.

### Weergave uitlijnen {#snap}
Snapt naar het dichtstbijzijnde voor-, achter-, linker-, rechter-, boven- of onderaanzicht. Sta je al in een van die aanzichten, dan springt een nieuwe klik 180 graden naar de andere kant.

### Snelheid {#speed}

Vind je dat de camera te langzaam of te snel beweegt, dan kun je een snelheidsfactor instellen voor `Rotatie`, `Inzoomen` en `Verplaatsen`. Handig als je sculpt heel groot of heel klein is.

### Overzicht van het draaipunt {#pivot}

Als je de camera draait, zie je een klein roze stipje: dat is het draaipunt van je camera.  
Het is heel belangrijk om te weten waar je draaipunt ligt, zodat je niet verdwaalt of gefrustreerd raakt door de camera.

Standaard wordt het draaipunt bijgewerkt bij deze handelingen:
- dubbeltikken op het model
- dubbeltikken op de achtergrond (het nieuwe draaipunt ligt dan in het midden van je mesh)
- *twee* vingers op het scherm zetten (verschuiven/zoomen/rollen) zet het draaipunt in het midden tussen de *twee* vingers

### Draaipunt bijwerken… {#update-pivot}

Met deze opties bepaal je verder wanneer het draaipunt wordt bijgewerkt:

* `Wanneer de camera begint te bewegen` - Werkt het draaipunt bij zodra je met de camera begint te werken.
* `Draaipunt buiten object` - Staat een nieuw draaipunt toe, ook als je buiten het oppervlak van het object zoomt. Vereist `Wanneer de camera begint te bewegen`.
* `Bij dubbel tikken` - Werkt het rotatiepunt bij wanneer je dubbeltikt op het oppervlak van het object.
* `Beeldhouwen (Streek)` - Werkt het draaipunt bij wanneer je sculpt.

::: tip
Ben je eraan gewend, dan kun je het roze (hulp)stipje verbergen in het menu [Instellingen](settings.md).
:::

### Centreren beeld bij uitzoomen {#center-view-when-zooming-out}
Bij het uitzoomen schuift de camera niet opzij: hij beweegt alleen naar achteren, zodat de weergave gecentreerd blijft.

### Dubbel tikken op object {#dtap-object}
Staat dit aan, dan focust de camera bij dubbeltikken op een object op het aangetikte punt.

### Dubbel tik op achtergrond {#dtap-tap-background}
Staat dit aan, dan focust de camera bij dubbeltikken op de achtergrond op:
* `Selectie` - De geselecteerde objecten.
* `Scène` - De hele scène.
* `Wisselen` - Wisselt bij elke dubbeltik tussen de twee. Er zijn twee opties `Wisselen`: ze verschillen in welke als eerste komt, zoals hun iconen laten zien.
