# ![](/icons/history.webp) Cronologia {#history}
![](/images/history_overview.webp)

Come nella maggior parte degli strumenti di creazione di contenuti, in Nomad puoi annullare/ripristinare tutte le modifiche.
Esiste un limite al numero di operazioni annullabili, ma puoi controllare questo comportamento.

::: tip
Puoi usare delle gesture rapide per annullare/ripristinare:
- tocco con 2 dita per annullare
- tocco con 3 dita per ripristinare
:::

## Cronologia {#history-panel}
![](/images/history_history.webp)

Questo pannello mostra lo stack della cronologia, indicando il numero di passaggi, il nome dell’operazione e la quantità di memoria utilizzata da quel passaggio.

## Impostazioni {#settings}
![](/images/history_settings.webp)

### Limite cronologia (MB) {#history-limit-mb}
Se lo stack della cronologia supera questo valore, le operazioni più vecchie verranno rimosse in modo che il budget di memoria rientri in questo limite.


### Numero massimo di annullamenti {#maximum-undoable}
Puoi controllare il numero massimo di operazioni.

## Ripristina fotocamera {#restore-camera}
Per ogni operazione viene salvato il punto di vista della camera.
Se abiliti questa opzione, annullare o ripristinare un’operazione reimposterà la camera al punto di vista salvato.

## Includi azioni {#include-actions}

* `Lights` - Se disabilitato, le operazioni sulle luci (a parte gli spostamenti con il gizmo) verranno ignorate dallo stack della cronologia
* `Matcaps & HDRIs` - Se disabilitato, le modifiche a matcap e hdri verranno ignorate dallo stack della cronologia
* `PostProcess` - Se disabilitato, le modifiche alle opzioni di postprocess verranno ignorate dallo stack della cronologia

## Statistiche memoria {#memory-stats}

Questa sezione fornisce una ripartizione della memoria utilizzata da Nomad.