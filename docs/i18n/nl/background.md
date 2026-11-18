# ![](/icons/image.webp) Achtergrond {#background}

In dit menu stel je de achtergrondkleur van Nomad in, en eventuele referentiebeelden die je wilt gebruiken.

![](/images/background_overview.webp)

## Type {#type}
![](/images/background_selector.webp)

Er zijn drie opties voor de achtergrond van de viewport.

* `Omgeving` - Toont de environment map die je in [Shading](shading.md) hebt gekozen. Die kun je verder bijstellen met de schuifregelaars `Vervagen` en `Belichting` (helderheid). 
* `Kleur` - Een egale kleur naar keuze
* `Kleuroverloop` - Een overgang tussen twee kleuren. Met de schuifregelaar `Factor` verschuif je het midden van de overloop.  

### Type kleuroverloop {#gradient-type}
Bij `Kleuroverloop` kies je de vorm:
* `Lineair` - Een rechte overloop, waarvan je de richting instelt met de schuifregelaar `Hoek`.
* `Radiaal` - Een cirkelvormige overloop vanuit het midden van het scherm.
* `Hemel` - Een overloop die vastligt aan de horizon van de wereld, zodat hij met de camera meebeweegt als je omhoog en omlaag kijkt.

Elke kleur heeft een resetknop en een kleurkiezer, waarmee je een kleur van het scherm kunt oppikken.

## ![](/icons/lock.webp) Sync bij cameravergrendeling {#sync-on-camera-lock}
Als de camera vergrendeld is met de [Navigator](settings.md#snap-cube), volgt het referentiebeeld de bewegingen van de camera, zodat het netjes op je sculpt uitgelijnd blijft.

* `Rollen toestaan (trackball)` - Laat de camera rollen wanneer je de cameravergrendeling verlaat.
* `Weergave resetten bij ontgrendeling` - Zet de weergave terug wanneer je de cameravergrendeling verlaat.

## Referentiebeeld {#reference}

![](/images/background_reference.webp)

Je kunt een afbeelding naar keuze op de achtergrond zetten om als referentie te gebruiken. Tik op `Importeer...` om er een toe te voegen en vink dan `Referentiebeeld` aan om hem te tonen.
Je kunt de positie en de schaal aanpassen, bijvoorbeeld als je hem naar een hoek van het scherm wilt verplaatsen.

### ![](/icons/tool_transform.webp) Transformeren {#transform}

Met deze knop plaats je het referentiebeeld interactief. Gebruik 2 vingers om het beeld te verschuiven, te schalen en te draaien tot het goed staat. `Instellingen herstellen` zet het beeld terug op de standaardplek. De uiteindelijke plaatsing zie je terug in de schuifregelaars hieronder:

* `Overlay` - Bij 0% staat het referentiebeeld altijd achter je objecten, bij 100% ervoor. 
* `Dekking` - Hoe doorzichtig het beeld is.
* `Nabewerking` - Past de nabewerkingseffecten ook toe op het referentiebeeld. Zet dit uit om de oorspronkelijke kleuren te behouden.
* `Positie X` / `Positie Y` - De X- en Y-positie van het beeld.
* `Schaal` - De schaal van het beeld.
* `Rotatie` - De rotatie van het beeld.


::: tip

Camera's en referentiebeelden zijn aan elkaar gekoppeld. 

Als je je referentiebeeld hebt uitgelijnd met je sculpt en daarna een camera aanmaakt in het [Camera-menu](camera.md), worden de positie, rotatie en schaal van het referentiebeeld samen met de camera opgeslagen. Je kunt het referentiebeeld dan uitzetten en naar een ander gezichtspunt draaien. Kijk je later weer door die camera, dan wordt het referentiebeeld opnieuw ingeschakeld met de instellingen die je gebruikte.

Je kunt zelfs voor elke camera een ander beeld kiezen!

 ![](/videos/reference_camera.mp4)

:::
