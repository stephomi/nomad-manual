# ![](/icons/history.webp) Historia {#history}
![](/images/history_overview.webp)

Jak w większości programów do tworzenia treści, w Nomadzie możesz cofać i ponawiać każdą edycję.
Historia potrafi mocno urosnąć, dlatego sam decydujesz, ile jej zostaje w pamięci, ile trafia do pamięci masowej i czy jest zapisywana razem z projektem.

::: tip
Do cofania i ponawiania możesz używać szybkich gestów:
- stuknięcie 2 palcami cofa
- stuknięcie 3 palcami ponawia
:::

## ![](/icons/history.webp) Historia {#history-panel}
![](/images/history_history.webp)

Ten panel pokazuje stos historii: numer kroku, nazwę operacji, obiekt, którego dotyczyła, oraz ilość pamięci zajmowanej przez dany krok.

Stuknij wpis, aby wrócić (albo przeskoczyć do przodu) do tego stanu. Przytrzymaj wpis, aby trwale usunąć go razem z całą starszą historią. To szybki sposób na zwolnienie pamięci, gdy jesteś już zadowolony z rzeźby.

### ![](/icons/speed.webp) Odtwórz {#replay}
Przycisk odtwarzania w lewym dolnym rogu cofa wszystko do samego początku, a potem ponawia operacje jedna po drugiej. To fajny sposób, żeby zobaczyć, jak powstawała twoja rzeźba. Suwak ustawia prędkość w operacjach na sekundę. Stuknij przycisk ponownie, aby zatrzymać odtwarzanie. Zatrzymuje je też cofnięcie, ponowienie albo stuknięcie wpisu.

Przed startem okienko pozwala wybrać:
* `Odwróć` - Cofa od bieżącego stanu do samego początku, zamiast odtwarzać od początku.
* `Przywróć kamerę` - Kamera podąża za odtwarzanymi operacjami, nawet gdy opcja [Przywróć kamerę](#restore-camera) jest wyłączona.
* `Wygładzanie kamery` - Kamera płynnie przechodzi między widokami, zamiast przeskakiwać od jednego do drugiego. Wyższe wartości dają spokojniejszą kamerę.

::: warning
Odtwarzanie jest funkcją eksperymentalną.
:::

## Dołącz działania {#include-actions}

Ikony na dole panelu Historia decydują, jakie rodzaje edycji są zapisywane w historii:

| Działanie      | Ikona                         | Opis                                                                                |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Światła     | ![](/icons/light.webp)        | Edycje świateł. Przesunięcie światła za pomocą Gizmo jest zapisywane zawsze, bo może wpływać na inne obiekty w hierarchii sceny |
| Cieniowanie | ![](/icons/sun.webp)          | Tryby PBR, MatCap i Nieoświetlony, MatCapy i HDRI                                   |
| Postprocessing | ![](/icons/postprocess.webp)  | Edycje postprocessingu                                                       |
| Zaznaczenie | ![](/icons/tool_lattice.webp) | Edycje zaznaczenia w Kracie, takie jak kliknięcia, zaznaczenia lassem i odznaczanie |

## Ustawienia {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Przywróć kamerę {#restore-camera}
Przy każdej operacji zapisywany jest punkt widzenia kamery.
Gdy włączysz tę opcję, cofnięcie lub ponowienie operacji przywróci kamerę do zapisanego punktu widzenia.

### ![](/icons/history.webp) Zapisz historię {#save-history}
Zachowuje historię cofania przy zapisie projektu, więc przetrwa ona ponowne otwarcie projektu. Wyłącz tę opcję, jeśli chcesz mieć mniejsze pliki projektów.

### ![](/icons/ram.webp) Limit pamięci RAM {#history-limit-mb}
Maksymalna ilość historii przechowywanej w pamięci RAM. Starsze stany są przenoszone do pamięci masowej i wczytywane z powrotem w razie potrzeby, nie są usuwane.

### ![](/icons/save.webp) Limit pamięci masowej {#storage-limit}
Maksymalna ilość pamięci masowej zajmowanej przez historię tego projektu. Po osiągnięciu limitu najstarsze operacje są trwale usuwane.

::: tip
Nowy limit zaczyna działać po następnej edycji, cofnięciu lub ponowieniu.
:::

### ![](/icons/undo.webp) Ostrzeżenie przy cofaniu {#maximum-undoable}
Gdy chcesz za jednym razem cofnąć się o więcej operacji niż ta liczba, Nomad najpierw poprosi o potwierdzenie. Jeśli potem coś zmienisz, wszystkie operacje po tym punkcie przepadną, więc ta opcja chroni cię przed przypadkowym stuknięciem daleko w dół listy.

## Statystyki pamięci {#memory-stats}

Ta sekcja pokazuje, ile pamięci zużywa Nomad i na co.
