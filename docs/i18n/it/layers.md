# ![](/icons/layer.webp) Livelli {#layers}

Questo menu contiene la pila dei livelli, un modo per salvare le modifiche al tuo oggetto in modo non distruttivo, e tanti modi per combinare e riutilizzare i livelli.

![](/images/layers_overview.webp) 

## Panoramica {#overview}

In Nomad i livelli servono a più scopi.

Le informazioni di pittura (Colore, Rugosità, Metallicità, Opacità) funzionano con i livelli in modo simile alle app di pittura 2d. Puoi creare un livello e dipingere sul modello. Il livello si può attivare o disattivare, regolarne l'opacità, duplicarlo, cambiarne l'ordine nella pila dei livelli e modificarne la modalità di fusione.

Nomad usa i livelli anche per la scultura. Un livello può contenere dettagli fini come le rughe, oppure grandi modifiche, e funzionare così come le blendshape/shape key/morph target di altre app 3d. Per esempio, puoi scolpire diverse espressioni facciali su livelli diversi e regolare i cursori dei livelli per combinarle in nuove espressioni.

In questo caso le modifiche salvate in un livello si sommano soltanto: l'ordine dei livelli non conta come per la pittura.

I livelli possono essere cancellati in parte con lo strumento [DelLayer](tools.md#delete-layer), e possono anche servire a creare maschere a partire dalle diverse informazioni che contengono.

![](/videos/layer.mp4)

::: tip
A differenza della maggior parte dei software di scultura, cambiare la topologia di una mesh non elimina i livelli. Puoi usare il [Remeshing dei voxel](topology.md#voxel-remesher), la [Multirisoluzione](topology.md#multiresolution) o gli strumenti [Rifila](tools.md#trim)/[Dividi](tools.md#split), ma tieni presente che con il [Remeshing dei voxel](topology.md#voxel-remesher) la qualità del livello ne risente.
:::

::: tip
Se usi i livelli come blendshape/morph target, trovi altre funzioni per i livelli nel [menu Scena](scene.md#object-menu): puoi separare i livelli in oggetti, e combinare oggetti corrispondenti in livelli.
:::
----

## Menu Livelli {#layer-menu}

![](/images/layers_menu.webp)

Il titolo mostra il nome dell'oggetto selezionato. I livelli non sono disponibili sulle primitive, quindi prima convalida la primitiva.

Premi `Aggiungi livello` per creare un nuovo livello. `Unisci livelli` unisce tutti i livelli nella mesh di base; il numero accanto alla sua icona indica quanti livelli ci sono.

Ogni livello ha un nome, un cursore per controllarne l'intensità/il fattore, e dei pulsanti di opzione. Tocca un livello per renderlo attivo: scultura e pittura finiscono in quel livello. Tocca `Base` per tornare a lavorare sulla mesh di base.

### ![](/icons/sort_right.webp) Espandi elenco {#ui-expand-list}

Di default, l'elenco dei livelli mostra solo la visibilità, la modalità di fusione e l'intensità di ogni livello, e il livello attivo è espanso con tutti i suoi controlli. La freccia a sinistra del titolo espande tutti i controlli per ogni livello.

![](/images/layers_expand.webp)

### Opzioni {#options}

| Azione       | Icona                        | Descrizione                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visibile     | ![](/icons/eye_open.webp)   | Mostra/nasconde il livello                          |
| Fusione      | ![](/icons/opacity.webp)    | La modalità di fusione in stile Photoshop. Le 4 icone mostrano le modalità per Colore, Rugosità, Metallicità e Opacità. |
| Modifica nome | ![](/icons/pencil.webp)    | Modifica il nome del livello                        |
| Elimina      | ![](/icons/trash.webp)      | Elimina il livello                                  |
| Duplica      | ![](/icons/clone.webp)      | Duplica il livello                                  |
| Unisci sotto | ![](/icons/merge_down.webp) | Unisce il livello a quello sottostante (o alla mesh di base) |
| Altro        | ![](/icons/more.webp)       | Opzioni [Altro...](#more)                           |

Quando un livello non è espanso, `Modifica nome`, `Elimina`, `Duplica` e `Unisci sotto` si trovano nel suo menu [Altro...](#more).

Per spostare un livello in un altro punto della pila, tieni premuto sul suo nome, poi trascina.

### Base {#base}

Il pulsante con i 3 puntini della riga `Base` sposta la pittura della mesh di base in un nuovo livello, con il pulsante `Base → Livello`. La base viene poi riportata al materiale di sfondo. È comodo quando hai dipinto molto prima di creare un livello.

* I pulsanti maschera e nascondi accanto lasciano intatte le zone mascherate e nascoste.
* `Estrai` - i canali da spostare: `Colore`, `Opacità`, `Rugosità` e `Metallicità`.
* `Materiale di sfondo` - se è attivo, vengono spostati solo i valori diversi da questo materiale. Impostalo con i cursori, o prelevalo dal modello con il contagocce.

### ![](/icons/more.webp) Altro... {#more}

Il pulsante 'Altro...' mostra opzioni aggiuntive per il livello attuale, in due schede: le impostazioni (icona a ingranaggio) e l'estrazione (icona a cubo).

![](/images/layers_more.webp) 

#### Fattori canale {#channel-factors}

Questi controlli ti permettono di scalare la quantità di scultura/colore/rugosità/metallicità/opacità del livello. Questi valori vengono moltiplicati per il cursore del fattore del livello: per esempio, se l'intensità del livello è 1 ma il fattore del canale colore è 0.5, il colore viene mostrato con intensità 0.5.

`Spostamento` controlla l'intensità della scultura del livello. Mentre colore/rugosità/metallicità sono limitati tra 0 e 1, lo spostamento può avere qualsiasi valore, positivo o negativo. 

::: tip
Lo spostamento può trasformare un livello di rilievi in un livello di cavità, o un sorriso in un broncio:
![](/videos/layer_happysad.mp4)


Un livello simmetrico può essere clonato e poi diviso in forme sinistra/destra con DelLayer:
![](/videos/layer_leftright.mp4)

I livelli con fattori di spostamento negativi possono essere trasferiti su livelli vuoti per creare nuove forme positive.

I livelli con fattori di spostamento positivi superiori a 1 servono a sperimentare blendshape più estreme.
:::

::: warning
Per ora i livelli condividono un solo canale di opacità per tutti e 3 i canali (colore/metallicità/rugosità).
Se unisci più livelli con un'intensità per canale non al massimo, il risultato finale potrebbe apparire diverso.

Forse in futuro ogni canale avrà il proprio canale alfa, per eliminare questo limite.
:::


#### ![](/icons/shield.webp) Maschera {#mask}
Il pulsante maschera accanto a ogni cursore crea una maschera da quel canale. Come quando usi i livelli per fare selezioni nelle app di pittura, questo ti permette di riutilizzare il lavoro fatto in un livello per altre operazioni.

#### ![](/icons/preview.webp) Anteprima {#preview}
![](/images/layers_preview.webp) 

Le opzioni seguenti si trovano nella scheda estrazione del menu 'Altro...'.

Quando è attiva, mostra l'anteprima delle impostazioni di estrazione per questo livello (vedi la sezione successiva).

`Raggi X` sceglie quali oggetti rendere trasparenti durante l'anteprima (`Nessuno`, `Non selezionati`, `Selezionati` o `Tutti`), così la forma estratta resta piena. È utile se usi altezze di estrazione negative.

#### ![](/icons/mask_extract.webp) Estrai {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Il pulsante `Estrai` duplica il contenuto del livello in un nuovo oggetto, di solito con uno spessore scelto da te nella sezione successiva.

`Azione di chiusura` stabilisce come avviene la duplicazione:

* `Nessuno` - Estrae semplicemente la parte, senza cercare di generare i lati o riempire i buchi.
* `Riempi` - Il buco viene riempito con triangoli e levigato. Non usare questa opzione per le superfici piatte.
* `Involucro` - Chiude la forma estratta con il valore di spessore e le opzioni di direzione.
* `Livello` - Estrae la differenza del livello.

#### ![](/icons/height.webp) Altezza {#thickness}
![](/images/layers_thickness.webp) 

La profondità dell'estrusione dell'involucro. I valori positivi crescono fuori dalla superficie, quelli negativi dentro la superficie. È nascosta quando l'azione di chiusura è `Livello`.

Il più/meno accanto a questo valore imposta la direzione dell'estrusione:
* Meno ( - ) parte dalla superficie attuale ed estrude verso il basso. 
* Più ( + ) parte dalla superficie attuale ed estrude verso l'alto.
* PiùMeno ( ± ) allontana la parte superiore e quella inferiore dell'estrusione della stessa quantità, così risulta immersa per metà nella superficie originale.

#### Lati {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Questa sezione è visibile quando l'azione di chiusura è `Involucro`. 

`Divisioni parete` imposta il numero di divisioni lungo i lati dell'involucro. Con il suo interruttore `Auto` attivo, Nomad calcola il numero di edge loop per creare poligoni quadrati.

#### Levigatezza {#smoothness}
![](/images/layers_smoothness.webp) 

Se i bordi della zona da estrarre sono frastagliati, attiva questa opzione per levigarli in una forma più gradevole. `Tutti` leviga tutta la superficie estratta, `Solo bordi` ne leviga i bordi. `Iterazioni` imposta l'intensità della levigatura.

_Qui finisce il sottomenu 'Altro...'._

### ![](/icons/cog.webp) Avanzato {#advanced}
![](/images/layers_advanced.webp)

Il pulsante `Avanzato` in fondo al menu compare quando l'oggetto ha dei livelli.

#### Conserva i dettagli dei livelli superiori {#keep-top-layers-details}

Fa sì che i piccoli dettagli dei livelli superiori restino visibili quando apporti grandi modifiche a quelli inferiori. Mentre scolpisci, la deformazione che arriva dai livelli superiori viene ignorata, ma i loro dettagli restano visibili. Funziona bene solo se quei livelli superiori contengono dettagli relativamente piccoli.

Di default, se scolpisci piccole rughe su un livello e poi fai grandi modifiche al livello di base, le rughe vanno perse. Attivando questa opzione, quei piccoli dettagli restano sempre "a galla" sopra le grandi modifiche sottostanti. Nel video seguente, guarda come il dettaglio delle rughe viene rimosso di default, ma resta visibile quando 'Conserva i dettagli dei livelli superiori' è attivo:

![](/videos/layers_details.mp4)


#### Sincronizza trasformazione {#sync-transform}

Quando è attivo, tutti i livelli non selezionati vengono adattati in base alla rotazione, alla scala e all'inclinazione della trasformazione, quando usi gli strumenti Gizmo o Trasforma. Può essere `Auto`, `No` o `Sì`.

Disattiva questa opzione se gli altri livelli devono essere usati senza la nuova trasformazione che stai applicando.

Con `Auto`, vengono adattati solo i livelli visibili.
