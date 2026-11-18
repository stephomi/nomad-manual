# ![](/icons/history.webp) Historik {#history}
![](/images/history_overview.webp)

Som i de flesta verktyg för att skapa innehåll kan du ångra och göra om alla ändringar i Nomad.
Historiken kan bli stor, så du bestämmer själv hur mycket av den som ligger kvar i minnet, hur mycket som sparas på lagringen och om den sparas med ditt projekt.

::: tip
Du kan använda snabba gester för att ångra och göra om:
- tryck med 2 fingrar för att ångra
- tryck med 3 fingrar för att göra om
:::

## ![](/icons/history.webp) Historik {#history-panel}
![](/images/history_history.webp)

Den här panelen visar historikstapeln: antalet steg, åtgärdens namn, objektet den gällde och hur mycket minne steget använder.

Tryck på en post för att hoppa tillbaka (eller framåt) till det läget. Håll fingret på en post för att permanent radera den och all äldre historik, ett snabbt sätt att frigöra minne när du är nöjd med din skulptur.

### ![](/icons/speed.webp) Spela upp {#replay}
Uppspelningsknappen längst ned till vänster spolar tillbaka till roten och gör sedan om åtgärderna en i taget, ett roligt sätt att se din skulptur växa fram. Reglaget ställer in hastigheten i åtgärder per sekund. Tryck på knappen igen för att stoppa; ångra/gör om eller ett tryck på en post stoppar också uppspelningen.

Innan den börjar får du välja i ett popup-fönster:
* `Omvänd` - Ångrar från det aktuella läget tillbaka till roten, i stället för att spela upp från roten.
* `Återställ kamera` - Kameran följer de uppspelade åtgärderna, även när [Återställ kamera](#restore-camera) är avstängt.
* `Kamerautjämning` - Kameran glider mjukt mellan vyerna i stället för att hoppa till var och en. Högre värden ger en lugnare kamera.

::: warning
Uppspelningen är experimentell.
:::

## Inkludera åtgärder {#include-actions}

Ikonerna längst ned i panelen Historik väljer vilka typer av ändringar som sparas i historiken:

| Åtgärd      | Ikon                          | Beskrivning                                                                         |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Ljus      | ![](/icons/light.webp)        | Ändringar av ljus. Att flytta ett ljus med gizmon sparas alltid, eftersom det kan påverka andra objekt i scenens hierarki |
| Skuggning     | ![](/icons/sun.webp)          | Lägena PBR, MatCap och Obelyst, matcaps och HDRI-bilder                              |
| Efterbehandling | ![](/icons/postprocess.webp)  | Ändringar av efterbehandlingen                                                     |
| Val   | ![](/icons/tool_lattice.webp) | Ändringar av markeringen i gallret, till exempel klick, lassomarkeringar och avmarkering |

## Inställningar {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Återställ kamera {#restore-camera}
Kamerans synvinkel sparas för varje åtgärd.
Om du aktiverar det här alternativet återställs kameran till den sparade synvinkeln när du ångrar eller gör om en åtgärd.

### ![](/icons/history.webp) Spara historik {#save-history}
Behåller ångrahistoriken när projektet sparas, så att den finns kvar när du öppnar projektet igen. Stäng av det för att hålla nere storleken på dina projektfiler.

### ![](/icons/ram.webp) RAM-gräns {#history-limit-mb}
Hur mycket historik som högst hålls i RAM-minnet. Äldre lägen flyttas till lagringen och läses in igen vid behov, de raderas inte.

### ![](/icons/save.webp) Lagringsgräns {#storage-limit}
Hur mycket lagringsutrymme projektets historik högst får använda. När gränsen nås raderas de äldsta åtgärderna permanent.

::: tip
En ny gräns börjar gälla efter nästa ändring, ångring eller omgörning.
:::

### ![](/icons/undo.webp) Ångravarning {#maximum-undoable}
Om du hoppar tillbaka fler åtgärder än så här på en gång får du först bekräfta det. Gör du en ändring efteråt försvinner alla åtgärder efter den punkten, så det här skyddar dig mot ett oavsiktligt tryck långt ned i listan.

## Minnesstatistik {#memory-stats}

Det här avsnittet visar en uppdelning av minnet som Nomad använder.
