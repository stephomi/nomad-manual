# ![](/icons/transform.webp) Trasforma {#transform}

Questo menu mostra in numeri la trasformazione dell'oggetto selezionato: dove si trova, come è ruotato e scalato, e quanto è grande. Puoi digitare valori esatti, azzerarli o trasferirli nella mesh.

![](/images/transform_overview.webp)

## Panoramica {#overview}

Ogni oggetto ha un nodo che memorizza la sua traslazione, rotazione e scala (la sua matrice), oltre ai suoi vertici. Gli strumenti [Gizmo](tools.md#gizmo) e [Trasforma](tools.md#transform) modificano questa matrice quando trascini nella vista; questo menu ti permette di leggerla e di digitare i valori. Vedi [Nodi e vertici](tools.md#nodes-and-vertices) per la differenza tra spostare il nodo e spostare i vertici.

Trascina un valore a sinistra o a destra per cambiarlo, oppure toccalo per digitare un numero. I valori X, Y e Z sono colorati in rosso, verde e blu, come gli assi del gizmo.

::: tip
Digitare i valori è comodo per posizionare gli oggetti con precisione, per esempio per mettere più parti esattamente alla stessa altezza, o per riportare una rotazione a un numero tondo dopo una rotazione libera con il gizmo.
:::

## Matrice {#matrix}

Il titolo ti dice in quale spazio sono espressi i valori: `locale` (rispetto all'oggetto genitore) o `mondo`.

### Oggetto e Pivot {#object-pivot}

* `Oggetto` - I valori sono la trasformazione dell'oggetto stesso.
* `Pivot` - I valori guidano la selezione a partire dal suo [pivot](tools.md#pivot), come fanno le maniglie del gizmo: le righe sono a zero, e cambiandole sposti, ruoti o scali la selezione attorno al pivot. Attiva `Modifica` (l'icona del lucchetto) per spostare solo il pivot, mentre gli oggetti restano fermi.

### Locale e Mondo {#local-world}

Quando l'oggetto ha un genitore o dei figli, o sono selezionati più oggetti, puoi scegliere in quale spazio mostrare i valori: `Locale` (rispetto al genitore) o `Mondo`.

### Azioni {#actions}

| Azione        | Icona                         | Descrizione |
| :-----------: | :---------------------------: | :---------- |
| Sposta origine | ![](/icons/target.webp)      | Sposta l'oggetto nell'origine del mondo. |
| Trasferisci   | ![](/icons/bake.webp)        | Applica la matrice ai vertici e azzera la matrice. Visivamente non cambia nulla, ma ora l'origine dell'oggetto è l'origine del mondo. |
| Pivot         | ![](/icons/gizmo.webp)       | Trasferisce il pivot nell'oggetto: l'origine e l'orientamento dell'oggetto diventano quelli del pivot. Visivamente non cambia nulla. |
| Modifica      | ![](/icons/lock.webp)        | (Modalità `Pivot`) Sposta solo il pivot. |
| Ripristina    | ![](/icons/reset.webp)       | Riporta la trasformazione all'identità. In modalità `Pivot`, invece, rimette il pivot al suo posto. |

Quando l'oggetto selezionato ha delle istanze, il trasferimento chiede una conferma, con l'opzione `Disinstanzia`: il trasferimento modifica i vertici, che le istanze condividono.

### Traslazione, Rotazione, Scala {#translation-rotation-scale}

La posizione, la rotazione (in gradi) e la scala dell'oggetto, su X, Y e Z. I due pulsanti alla fine di ogni riga trasferiscono nei vertici solo quella parte della trasformazione, oppure la azzerano.

Compare anche una riga `Inclina` quando l'oggetto è inclinato, per esempio dopo una scala non uniforme di un genitore ruotato.

### Scala uniforme {#uniform-scale}

Quando è attiva, la scala è un unico valore, uguale sui tre assi. Disattivala per scalare X, Y e Z separatamente.

## Dimensione {#dimension}

Le dimensioni e il centro del riquadro di delimitazione della selezione, in unità del mondo. Con più oggetti selezionati, li comprende tutti.

* `Dimensioni` - Larghezza, altezza e profondità. Con il pulsante di collegamento attivo, cambiare una dimensione scala le altre due della stessa quantità, mantenendo le proporzioni.
* `Centrato` - Il centro del riquadro di delimitazione. Il pulsante con il mirino sposta la selezione in modo che il suo centro sia nell'origine del mondo.

::: tip
`Dimensioni` è il modo più rapido per dare a un oggetto una misura reale, per esempio prima di una stampa 3d: imposta l'altezza che vuoi e il collegamento mantiene le proporzioni.
:::
