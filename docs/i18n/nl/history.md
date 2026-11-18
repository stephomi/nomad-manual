# ![](/icons/history.webp) Geschiedenis {#history}
![](/images/history_overview.webp)

Zoals in de meeste creatieve programma's kun je in Nomad elke bewerking ongedaan maken en opnieuw uitvoeren.
De geschiedenis kan flink groeien, dus jij bepaalt hoeveel ervan in het geheugen blijft, hoeveel er op de opslag wordt bewaard en of hij met je project wordt opgeslagen.

::: tip
Met snelle gebaren maak je iets ongedaan of voer je het opnieuw uit:
- tik met 2 vingers om ongedaan te maken
- tik met 3 vingers om opnieuw uit te voeren
:::

## ![](/icons/history.webp) Geschiedenis {#history-panel}
![](/images/history_history.webp)

Dit paneel toont de geschiedenis: het nummer van elke stap, de naam van de bewerking, het object waarop ze werd toegepast en hoeveel geheugen die stap inneemt.

Tik op een regel om terug (of vooruit) te springen naar die toestand. Houd een regel lang ingedrukt om hem en alle oudere geschiedenis definitief te verwijderen: een snelle manier om geheugen vrij te maken zodra je tevreden bent met je sculpt.

### ![](/icons/speed.webp) Afspelen {#replay}
De afspeelknop linksonder spoelt terug naar het begin en voert de bewerkingen dan een voor een opnieuw uit: een leuke manier om je sculpt te zien ontstaan. De schuifregelaar stelt de snelheid in, in bewerkingen per seconde. Tik nogmaals op de knop om te stoppen; ongedaan maken, opnieuw uitvoeren of een tik op een regel stopt het afspelen ook.

Voordat het begint, kies je in een pop-up:
* `Omgekeerd` - Maakt de bewerkingen ongedaan vanaf de huidige toestand terug naar het begin, in plaats van ze vanaf het begin af te spelen.
* `Camera herstellen` - De camera volgt de afgespeelde bewerkingen, ook als [Camera herstellen](#restore-camera) uit staat.
* `Camera-afvlakking` - De camera glijdt soepel van het ene gezichtspunt naar het andere in plaats van te verspringen. Hogere waarden geven een rustigere camera.

::: warning
Afspelen is experimenteel.
:::

## Acties opnemen {#include-actions}

Met de iconen onderaan het paneel Geschiedenis kies je welke soorten bewerkingen in de geschiedenis worden vastgelegd:

| Actie       | Icoon                         | Beschrijving                                                                        |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Lichten     | ![](/icons/light.webp)        | Wijzigingen aan lichten. Een licht verplaatsen met de gizmo wordt altijd vastgelegd, omdat het andere objecten in de scènehiërarchie kan beïnvloeden |
| Shading     | ![](/icons/sun.webp)          | De modus PBR, MatCap of Unlit, matcaps en HDRI's                                    |
| Nabewerking | ![](/icons/postprocess.webp)  | Wijzigingen aan de nabewerking                                                      |
| Selectie    | ![](/icons/tool_lattice.webp) | Wijzigingen aan de selectie van het rooster, zoals klikken, lassoselecties en deselecteren |

## Instellingen {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Camera herstellen {#restore-camera}
Bij elke bewerking wordt het gezichtspunt van de camera opgeslagen.
Als je deze optie aanzet, springt de camera bij ongedaan maken of opnieuw uitvoeren terug naar dat opgeslagen gezichtspunt.

### ![](/icons/history.webp) Geschiedenis opslaan {#save-history}
Bewaart de geschiedenis wanneer het project wordt opgeslagen, zodat je na het heropenen van het project nog steeds dingen ongedaan kunt maken. Zet het uit om je projectbestanden kleiner te houden.

### ![](/icons/ram.webp) RAM-limiet {#history-limit-mb}
De maximale hoeveelheid geschiedenis die in het RAM-geheugen blijft. Oudere toestanden worden naar de opslag verplaatst en weer ingeladen wanneer dat nodig is; ze worden niet verwijderd.

### ![](/icons/save.webp) Opslaglimiet {#storage-limit}
De maximale hoeveelheid opslagruimte die de geschiedenis van dit project mag gebruiken. Wordt de limiet bereikt, dan worden de oudste bewerkingen definitief verwijderd.

::: tip
Een nieuwe limiet gaat in na de volgende bewerking, ongedaan maken of opnieuw uitvoeren.
:::

### ![](/icons/undo.webp) Waarschuwing bij ongedaan maken {#maximum-undoable}
Als je in één keer meer dan dit aantal bewerkingen terugspringt, wordt eerst om bevestiging gevraagd. Doe je daarna een bewerking, dan gaan alle bewerkingen na dat punt verloren; zo ben je beschermd tegen een per ongeluk getikte regel ver onderaan de lijst.

## Geheugenstatistieken {#memory-stats}

Dit onderdeel laat zien hoeveel geheugen Nomad gebruikt, uitgesplitst per onderdeel.
