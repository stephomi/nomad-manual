# ![](/icons/history.webp) Historik {#history}
![](/images/history_overview.webp)

Precis som i de flesta verktyg för att skapa innehåll kan du ångra/göra om alla redigeringar i Nomad.
Det finns en gräns för hur många åtgärder som kan ångras, men du kan styra detta beteende.

::: tip
Du kan använda snabba gester för att ångra/göra om:
- Tryck med 2 fingrar för att ångra
- Tryck med 3 fingrar för att göra om
:::

## Historik {#history-panel}
![](/images/history_history.webp)

Den här panelen visar historikstacken och visar antalet steg, åtgärdens namn och hur mycket minne det steget använder.

## Inställningar {#settings}
![](/images/history_settings.webp)

### Historikgräns (Mb) {#history-limit-mb}
Om historikstacken överskrider detta värde tas de äldre åtgärderna bort så att minnesbudgeten ryms inom denna gräns.


### Maximalt ångringsbart {#maximum-undoable}
Du kan styra det maximala antalet åtgärder.

## Återställ kamera {#restore-camera}
För varje åtgärd sparas kamerans vy.
Om du aktiverar det här alternativet kommer ångra eller göra om en åtgärd att återställa kameran till den sparade vyn.

## Inkludera åtgärder {#include-actions}

* `Lights` - När detta är inaktiverat ignoreras ljusåtgärder (förutom förflyttningar med gizmo) av historikstacken
* `Matcaps & HDRIs` - När detta är inaktiverat ignoreras ändringar av matcaps och HDRI:er av historikstacken
* `PostProcess` - När detta är inaktiverat ignoreras ändringar av postprocess-alternativen av historikstacken

## Minnesstatistik {#memory-stats}

Detta avsnitt ger en uppdelning av minnet som används av Nomad.