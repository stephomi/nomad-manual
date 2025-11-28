# ![](/icons/layer.webp) Livelli {#layers}

Questo menu contiene lo stack dei livelli, un modo per memorizzare le modifiche al tuo oggetto in maniera non distruttiva, e molti modi per combinare e riutilizzare i livelli.

![](/images/layers_overview.webp) 

## Panoramica {#overview}

I livelli di Nomad hanno molteplici scopi.

Le informazioni di pittura (Colore, Rugosità, Metallicità, Opacità) funzionano con i livelli in modo simile alle applicazioni di pittura 2D. È possibile creare un livello e applicare la pittura a un modello. Il livello può essere attivato o disattivato, la sua opacità può essere regolata, il livello può essere duplicato, il suo ordine può essere cambiato nello stack dei livelli, la sua modalità di fusione può essere regolata.

Nomad utilizza i livelli anche per lo sculpting. Un livello può memorizzare dettagli fini come rughe, oppure può memorizzare grandi cambiamenti, permettendo loro di funzionare come blendshape/shape key/morph target in altre applicazioni 3D. Ad esempio potresti scolpire diverse espressioni facciali su livelli differenti e regolare gli slider dei livelli per combinarle in nuove espressioni.

In questo caso le modifiche memorizzate in un livello sono puramente additive, l’ordine dei livelli non è importante come lo è per la pittura.

I livelli possono essere parzialmente cancellati tramite lo strumento [Delete Layer](tools.md#delete-layer), e i livelli possono anche essere usati per creare maschere basate sulle diverse informazioni memorizzate nel livello.

![](/videos/layer.mp4)

::: tip
A differenza della maggior parte dei software di sculpting, cambiare la topologia di una mesh non eliminerà i livelli. Puoi usare il [Voxel Remesher](topology.md#voxel-remesher), il [Multiresolution](topology.md#multires) o gli strumenti [Trim](tools.md#trim)/[Split](tools.md#split), ma nota che quando usi il [Voxel Remesher](topology.md#voxel-remesher), la qualità del livello verrà influenzata.
:::

::: tip
Se usi i livelli come blendshape/morph target, c’è funzionalità extra per i livelli nel [menu scena](scene.md#object-menu). Puoi separare i livelli in oggetti e combinare oggetti corrispondenti in livelli.
:::
----

## Menu livello {#layer-menu}

![](/images/layers_menu.webp)

Premi `Add layer` per creare un nuovo livello.

Ogni livello ha un nome, uno slider per controllarne l’intensità/fattore e dei pulsanti di opzione.

### Opzioni {#options}

| Azione       | Icona                        | Descrizione                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visibile     | ![](/icons/eye_open.webp)   | Mostra/nascondi il livello                          |
| Blend Mode   | ![](/icons/opacity.webp)    | La modalità di fusione in stile Photoshop. Le 4 icone mostrano le modalità per Colore, Rugosità, Metallicità, Opacità. |
| Modifica nome| ![](/icons/pencil.webp)     | Modifica il nome del livello                        |
| Elimina      | ![](/icons/trash.webp)      | Elimina il livello                                  |
| Duplica      | ![](/icons/clone.webp)      | Duplica il livello                                  |
| Unisci in basso | ![](/icons/merge_down.webp) | Unisci il livello con il livello sottostante (o la mesh di base) |
| Altro        | ![](/icons/more.webp)       | Opzioni [More...](#more)                            |

Per spostare un livello in un’altra parte dello stack, tieni premuto sul suo nome e trascinalo.

### Altro... {#more}

Il pulsante “More...” mostrerà opzioni aggiuntive per il livello corrente:

![](/images/layers_more.webp) 

#### Fattori canale {#channel-factors}

Questi controlli ti permettono di scalare la quantità di sculpt/colore/rugosità/metallicità/opacità per il livello. Questi valori vengono moltiplicati per lo slider del fattore del livello, quindi ad esempio se l’intensità del livello è 1, ma il fattore del canale colore è 0,5, allora il colore visualizzato avrà intensità 0,5.

`Offset` controlla l’intensità di sculpt del livello. Mentre colore/rugosità/metallicità sono limitati tra 0 e 1, l’offset può assumere qualsiasi valore, sia positivo che negativo. 

::: tip
Offset può essere usato per trasformare un livello di rigonfiamenti in un livello di cavità, o un sorriso in un broncio:
![](/videos/layer_happysad.mp4)


Un livello simmetrico può essere clonato e poi diviso in forme sinistra/destra con del layer:
![](/videos/layer_leftright.mp4)

I livelli con fattori di offset negativi possono essere fusi in livelli vuoti per creare nuove forme positive.

I livelli con fattori di offset positivi superiori a 1 possono essere usati per sperimentare blendshape più estremi.
:::

::: warning
Al momento i livelli condividono un unico canale di opacità per tutti e 3 i canali (colore/metallicità/rugosità).
Se unisci più livelli con intensità per canale che non sono al massimo, è possibile che il risultato finale appaia diverso.

In futuro, forse ogni canale avrà il proprio canale alfa per rimuovere questa limitazione.
:::


#### ![](/icons/tool_mask.webp) Maschera {#mask}
Il pulsante maschera accanto a ciascuno slider creerà una maschera da quel canale. In modo simile all’uso dei livelli per creare selezioni nelle applicazioni di pittura, questo ti permette di riutilizzare il lavoro fatto in un livello per altre operazioni.

#### ![](/icons/preview.webp) Anteprima {#preview}
![](/images/layers_preview.webp) 

Quando è attivato, mostrerà l’anteprima delle impostazioni di estrazione per questo livello (vedi la sezione successiva).

Quando l’xray è attivo, solo la forma estratta sarà solida, il resto della forma sarà reso trasparente, utile se stai usando altezze di estrazione negative.

#### Estrai {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Il pulsante `Extract` duplica il contenuto del livello in un nuovo oggetto, di solito con uno spessore specificato dall’utente impostato nella sezione successiva.

`Closing action` determina come viene eseguita la duplicazione:

* None - Semplicemente estrai la parte, senza generare lati o riempire buchi.
* Fill - Il buco viene riempito e smussato con triangoli. Non usare questa opzione per superfici piatte.
* Shell - Chiudi la forma estratta con il valore di spessore e le opzioni di direzione.
* Layer - Estrai la differenza del livello.

#### ![](/icons/height.webp) Spessore {#thickness}
![](/images/layers_thickness.webp) 

La profondità dell’estrusione della shell. I valori positivi crescono fuori dalla superficie, i valori negativi crescono verso l’interno della superficie.

Il pulsante più/meno accanto a questo valore imposta la direzione dell’estrusione:
* Minus ( - ) inizierà dalla superficie corrente ed estruderà verso il basso. 
* Plus ( + ) inizierà dalla superficie corrente ed estruderà verso l’alto.
* PlusMinus ( ± ) spingerà la parte superiore e inferiore dell’estrusione verso l’esterno in egual misura, così sarà a metà incorporata nella superficie originale.

#### Levigatezza {#smoothness}
![](/images/layers_smoothness.webp) 

Se i bordi della regione da estrarre sono frastagliati, questo slider tenterà di sfumare il bordo in una forma più liscia. 

#### ![](/icons/height.webp) Loop bordo (lato) {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Questa sezione è visibile quando la closing action è “Shell”. 

`Auto Edge-loop (side)` calcolerà il numero di edge loop lungo i lati della shell per creare poligoni quadrati. 

Se disattivato, lo slider `Division` imposterà il numero di suddivisioni sui lati.

_Questa è la fine del sottomenu “More...“._

### Avanzate {#advanced}
![](/images/layers_advanced.webp)

#### Mantieni i dettagli dei livelli superiori {#keep-top-layers-details}

Garantisce che i piccoli dettagli sui livelli superiori rimangano visibili quando vengono apportati grandi cambiamenti ai livelli inferiori.

Per impostazione predefinita, se scolpisci piccole rughe su un livello, poi vai a fare grandi modifiche al livello di base, le rughe andranno perse. Attivare questa opzione permetterà a quei piccoli dettagli di “galleggiare” sempre sopra i grandi cambiamenti sottostanti. Nel seguente video, osserva come il dettaglio delle rughe viene rimosso in modo predefinito, ma rimane visibile quando “keep top layers details” è attivato:

![](/videos/layers_details.mp4)


#### UI: Espandi elenco {#ui-expand-list}

Il menu livelli predefinito ti permette di attivare/disattivare la visibilità dei livelli e l’opacità del livello. Attivando questa opzione si espandono i controlli completi per ogni livello.

![](/images/layers_expand.webp)

#### Sincronizza trasformazione {#sync-transform}

Se attivato, tutti i livelli non selezionati verranno regolati in base alla trasformazione di rotazione, scala, skew. 

Disattiva questa opzione se gli altri livelli devono essere usati senza la nuova trasformazione che stai applicando.

Quando è impostato su `Auto`, verranno regolati solo i livelli visibili.