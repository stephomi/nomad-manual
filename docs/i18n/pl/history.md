# ![](/icons/history.webp) Historia {#history}
![](/images/history_overview.webp)

Jak w większości narzędzi do tworzenia treści, w Nomadzie możesz cofać i ponawiać wszystkie edycje.
Istnieje limit liczby operacji, które można cofnąć, ale możesz kontrolować to zachowanie.

::: tip
Możesz używać szybkich gestów do cofania/ponawiania:
- dotknięcie dwoma palcami, aby cofnąć
- dotknięcie trzema palcami, aby ponowić
:::

## Historia {#history-panel}
![](/images/history_history.webp)

Ten panel wyświetla stos historii, pokazując liczbę kroków, nazwę operacji oraz ilość pamięci używanej przez dany krok.

## Ustawienia {#settings}
![](/images/history_settings.webp)

### Limit historii (Mb) {#history-limit-mb}
Jeśli stos historii przekroczy tę wartość, starsze operacje zostaną usunięte, aby zużycie pamięci mieściło się w tym limicie.


### Maksymalna liczba cofnięć {#maximum-undoable}
Możesz kontrolować maksymalną liczbę operacji.

## Przywróć kamerę {#restore-camera}
Dla każdej operacji zapisywany jest punkt widzenia kamery.
Jeśli włączysz tę opcję, cofnięcie lub ponowienie operacji zresetuje kamerę do zapisanego punktu widzenia.

## Uwzględnij akcje {#include-actions}

* `Lights` - Po wyłączeniu operacje na światłach (poza przesunięciami gizma) będą ignorowane przez stos historii
* `Matcaps & HDRIs` - Po wyłączeniu zmiany matcapów i HDRI będą ignorowane przez stos historii
* `PostProcess` - Po wyłączeniu zmiany opcji postprocessingu będą ignorowane przez stos historii

## Statystyki pamięci {#memory-stats}

Ta sekcja przedstawia podział wykorzystania pamięci przez Nomad.