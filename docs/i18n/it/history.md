# ![](/icons/history.webp) Cronologia {#history}
![](/images/history_overview.webp)

Come nella maggior parte degli strumenti di creazione, in Nomad puoi annullare e ripetere ogni modifica.
La cronologia può diventare molto grande, quindi sei tu a decidere quanta ne resta in memoria, quanta ne viene conservata nell'archiviazione e se viene salvata con il progetto.

::: tip
Puoi usare dei gesti rapidi per annullare/ripetere:
- tocco con 2 dita per annullare
- tocco con 3 dita per ripetere
:::

## ![](/icons/history.webp) Cronologia {#history-panel}
![](/images/history_history.webp)

Questo pannello mostra la pila della cronologia: il numero dei passaggi, il nome dell'operazione, l'oggetto a cui è stata applicata e la quantità di memoria occupata da quel passaggio.

Tocca una voce per tornare indietro (o avanti) a quello stato. Tieni premuta una voce per eliminare definitivamente quella e tutta la cronologia precedente: un modo rapido per liberare memoria quando sei soddisfatto della tua scultura.

### ![](/icons/speed.webp) Riproduci {#replay}
Il pulsante play in basso a sinistra torna alla radice, poi ripete le operazioni una alla volta: un modo divertente per vedere la tua scultura prendere forma. Il cursore imposta la velocità in operazioni al secondo. Tocca di nuovo il pulsante per fermarla; anche un annulla/ripeti o un tocco su una voce la interrompe.

Prima di partire, un popup ti permette di scegliere:
* `Rovescia` - Annulla dallo stato attuale fino alla radice, invece di riprodurre dalla radice.
* `Ripristina telecamera` - La fotocamera segue le operazioni riprodotte, anche quando [Ripristina telecamera](#restore-camera) è disattivato.
* `Fluidità fotocamera` - La fotocamera scorre dolcemente da una vista all'altra invece di saltare da una all'altra. Valori più alti danno una fotocamera più calma.

::: warning
La riproduzione è sperimentale.
:::

## Includi azioni {#include-actions}

Le icone in fondo al pannello Cronologia scelgono quali tipi di modifiche vengono registrate nella cronologia:

| Azione          | Icona                         | Descrizione                                                                         |
| :-------------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Luci            | ![](/icons/light.webp)        | Modifiche alle luci. Lo spostamento di una luce con il Gizmo viene sempre registrato, perché può influire su altri oggetti nella gerarchia della scena |
| Shading         | ![](/icons/sun.webp)          | La modalità PBR, MatCap e Unlit, le MatCap e le HDRI                                |
| Post processing | ![](/icons/postprocess.webp)  | Modifiche al post processing                                                        |
| Selezione       | ![](/icons/tool_lattice.webp) | Modifiche alla selezione del Reticolo, come clic, selezioni a lazo e deselezioni    |

## Impostazioni {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Ripristina telecamera {#restore-camera}
Per ogni operazione viene salvato il punto di vista della fotocamera.
Se attivi questa opzione, annullando o ripetendo un'operazione la fotocamera torna al punto di vista salvato.

### ![](/icons/history.webp) Salva cronologia {#save-history}
Conserva la cronologia degli annullamenti quando salvi il progetto, così resta disponibile quando lo riapri. Disattivala per avere file di progetto più leggeri.

### ![](/icons/ram.webp) Limite RAM {#history-limit-mb}
La quantità massima di cronologia tenuta in RAM. Gli stati più vecchi vengono spostati nell'archiviazione e ricaricati quando servono: non vengono eliminati.

### ![](/icons/save.webp) Limite di archiviazione {#storage-limit}
La quantità massima di spazio di archiviazione usata dalla cronologia di questo progetto. Quando si raggiunge il limite, le operazioni più vecchie vengono eliminate definitivamente.

::: tip
Un nuovo limite ha effetto dopo la modifica, l'annullamento o la ripetizione successiva.
:::

### ![](/icons/undo.webp) Avviso di annullamento {#maximum-undoable}
Tornare indietro di più operazioni di questo numero in un colpo solo chiede prima una conferma. Se poi fai una modifica, tutte le operazioni successive a quel punto vanno perse: così sei protetto da un tocco accidentale troppo in basso nell'elenco.

## Statistiche della memoria {#memory-stats}

Questa sezione mostra nel dettaglio la memoria usata da Nomad.
