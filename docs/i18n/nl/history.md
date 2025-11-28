# ![](/icons/history.webp) Geschiedenis {#history}
![](/images/history_overview.webp)

Zoals bij de meeste contentcreatietools kun je in Nomad alle bewerkingen ongedaan maken en opnieuw uitvoeren.
Er is een limiet aan hoeveel bewerkingen ongedaan kunnen worden gemaakt, maar je kunt dit gedrag aanpassen.

::: tip
Je kunt snelle gebaren gebruiken om ongedaan maken/opnieuw uit te voeren:
- Tik met 2 vingers om ongedaan te maken
- Tik met 3 vingers om opnieuw uit te voeren
:::

## Geschiedenis {#history-panel}
![](/images/history_history.webp)

Dit paneel toont de geschiedenisstapel, met het aantal stappen, de naam van de bewerking en de hoeveelheid geheugen die die stap gebruikt.

## Instellingen {#settings}
![](/images/history_settings.webp)

### Geschiedenislimiet (Mb) {#history-limit-mb}
Als de geschiedenisstapel deze waarde overschrijdt, worden de oudere bewerkingen verwijderd zodat het geheugengebruik binnen deze limiet blijft.

### Maximum aantal ongedaan-acties {#maximum-undoable}
Je kunt het maximale aantal bewerkingen instellen.

## Camera herstellen {#restore-camera}
Voor elke bewerking wordt het camerastandpunt opgeslagen.
Als je deze optie inschakelt, zal het ongedaan maken of opnieuw uitvoeren van een bewerking de camera terugzetten naar het opgeslagen standpunt.

## Acties opnemen {#include-actions}

* `Lights` - Indien uitgeschakeld, worden lichtbewerkingen (behalve gizmo-verplaatsingen) genegeerd door de geschiedenisstapel
* `Matcaps & HDRIs` - Indien uitgeschakeld, worden wijzigingen aan matcaps en hdri's genegeerd door de geschiedenisstapel
* `PostProcess` - Indien uitgeschakeld, worden wijzigingen aan de postprocess-opties genegeerd door de geschiedenisstapel

## Geheugenstatistieken {#memory-stats}

Dit gedeelte geeft een uitsplitsing van het geheugenverbruik door Nomad.