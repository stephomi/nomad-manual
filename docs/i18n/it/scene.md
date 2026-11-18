# ![](/icons/scene.webp) Scena {#scene}

Questo menu ti permette di gestire oggetti, luci, fotocamere e ripetitori in Nomad. Mostra la gerarchia della scena come una vista ad albero, da cui puoi modificare molti aspetti dei tuoi oggetti. Ti permette anche di creare nuovi oggetti, e di unirli o dividerli in vari modi.


![](/images/scene_menu_summary.webp)


## Barra delle scorciatoie {#shortcut-bar}
| Azione                    | Icona                             | Descrizione                                                                                                         |
| :-----------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Aggiungi...](#add-menu)  | ![](/icons/plus.webp)            | Mostra il [menu Aggiungi](#add-menu) per aggiungere un oggetto alla scena                                           |
| Elimina                   | ![](/icons/trash.webp)           | Elimina gli oggetti selezionati. I loro figli vengono mantenuti.                                                    |
| Blocca                    | ![](/icons/lock.webp)            | Rende gli oggetti selezionati non selezionabili nel viewport. Si possono comunque selezionare dalla vista ad albero. Bloccare un gruppo blocca tutto ciò che contiene. Tocca di nuovo per sbloccare. |
| [Unisci](#join)           | ![](/icons/merge.webp)           | Unisce gli oggetti selezionati in un unico oggetto, senza modificarne la geometria                                  |
| [Dividi...](#separate)    | ![](/icons/separate.webp)        | Mostra il popup [Dividi](#separate), per spezzare un oggetto in più oggetti. È l'operazione inversa di Unisci       |
| [Booleano...](#boolean)   | ![](/icons/bool_subtract_circle.webp) | Mostra il popup [Booleano](#boolean)                                                                           |
| Clona                     | ![](/icons/clone.webp)           | Duplica gli oggetti selezionati in nuovi oggetti                                                                    |
| Istanza                   | ![](/icons/link.webp)            | Duplica gli oggetti selezionati come istanze: le modifiche di modellazione fatte su una si applicano a tutte le istanze. |
| Disinstanzia              | ![](/icons/unlink.webp)          | Converte un'istanza in una forma unica, così le modifiche di modellazione non vengono più copiate sulle altre istanze |
| Sincronizza               | ![](/icons/checked.webp)         | Quando è spuntata, le operazioni si applicano a tutte le istanze degli oggetti selezionati, non solo a quelli selezionati. È disponibile solo quando la selezione contiene delle istanze. La [scheda Sincronizza](#sync) del popup `Avanzato` stabilisce quali operazioni seguono questa casella. |

::: tip
Quando un'operazione avrà effetto anche sulle altre istanze, sul suo pulsante compare una piccola icona a forma di catena.
:::


## Vista ad albero {#tree-view}
![](/images/scene_treeview.webp) 

La vista ad albero elenca gli oggetti, i gruppi, i ripetitori, le luci e le fotocamere della scena. Accanto al nome di una mesh trovi il suo numero di vertici, con un'icona dei livelli colorata se ha dei livelli. Ogni riga ha questi pulsanti:

| Azione       | Icona                      | Descrizione              |
| :----------: | :------------------------: | :----------------------: |
| Nome         | ![](/icons/pencil.webp)   | Rinomina l'oggetto. Se è selezionato, tutti gli oggetti selezionati vengono rinominati insieme, con l'aggiunta di un numero. Una pressione lunga lo rinomina insieme ai suoi figli. |
| Seleziona    | ![](/icons/checked.webp)  | Seleziona/deseleziona    |
| Visibile     | ![](/icons/eye_open.webp) | Mostra/nasconde          |
| Menu         | ![](/icons/more.webp)     | Mostra il [menu dell'oggetto](#object-menu) |

::: tip CONSIGLIO: Selezionare o nascondere rapidamente molti oggetti

Tocca l'icona di selezione per selezionare o deselezionare un singolo oggetto, oppure trascina in verticale lungo la colonna di selezione per selezionare molti oggetti. Puoi fare lo stesso con la colonna della visibilità.

Una pressione lunga sull'icona di selezione o di visibilità agisce anche sui figli.

:::

### Intestazione della vista ad albero {#tree-view-header}

La riga sopra l'elenco offre qualche aiuto:

* ![](/icons/sort_down.webp) - comprime o espande tutti i gruppi in una volta.
* ![](/icons/preview.webp) - attiva o disattiva le `Anteprime oggetti`, una piccola miniatura renderizzata per ogni oggetto dell'elenco.
* ![](/icons/search.webp) - filtra l'elenco per nome.

### Gestione della vista ad albero {#tree-view-manipulation}

Tieni premuto su un elemento della vista ad albero finché non viene evidenziato. A quel punto puoi spostarlo su o giù nell'albero, oppure trascinarlo su un altro elemento per renderlo figlio di quell'elemento.

Quando sono selezionati più elementi, uno di loro è la selezione principale ed è più luminoso. Tieni premuto e trascina uno qualsiasi di loro per spostare tutti gli oggetti selezionati insieme.

Quando selezioni un elemento genitore, per impostazione predefinita vengono selezionati anche tutti i suoi figli. Toccando di nuovo il genitore passi dal selezionare solo il genitore al selezionare il genitore e i figli.

Tocca due volte un elemento per centrare la fotocamera su di esso (vedi [Avanzato](#focus-on-item)).

### Menu dell'oggetto {#object-menu}

Il pulsante con i puntini di sospensione (...) di un oggetto nella vista ad albero apre il menu dell'oggetto.
Molte di queste opzioni sono le stesse della barra delle scorciatoie in alto, ripetute per comodità.

|       Azione        |                        Icona                       | Descrizione                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Nome         |              ![](/icons/pencil.webp)           | Cambia il nome dell'oggetto                                                                                                                                             |
|    Disinstanzia     |              ![](/icons/unlink.webp)           | Converte un'istanza in una forma unica, così le modifiche di modellazione non vengono più copiate sulle altre istanze.                                                  |
|      Istanza        |               ![](/icons/link.webp)            | Duplica l'oggetto come istanza: le modifiche di modellazione fatte su una si applicano a tutte le istanze.                                                              |
|       Clona         |              ![](/icons/clone.webp)            | Duplica l'oggetto in un nuovo oggetto                                                                                                                                   |
|      Elimina        |              ![](/icons/trash.webp)            | Elimina l'oggetto. I suoi figli vengono mantenuti, a meno che `Figli` non sia spuntato.                                                                                 |
|       Figli         |            ![](/icons/hierarchy.webp)          | Quando è spuntato, `Istanza`, `Clona` ed `Elimina` agiscono anche sui figli dell'oggetto.                                                                               |
|  Dividi per Parti   |             ![](/icons/separate.webp)          | Se un oggetto è composto da parti scollegate, crea un oggetto separato per ognuna di esse. È l'operazione inversa di Unisci.                                            |
|  Dividi per Gruppi  |            ![](/icons/group.webp)          | Se un oggetto ha più gruppi di facce, crea un oggetto separato per ogni gruppo di facce.                                                                                    |
|  Dividi per Livelli |              ![](/icons/layer.webp)            | Se un oggetto ha dei livelli, crea oggetti separati per la mesh di base e per ogni livello. Utile per inviare blendshape ad altre applicazioni.                          |
|  Unisci → Livelli   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Se sono selezionati più oggetti con la stessa topologia, li unisce come livelli dell'oggetto principale (gli altri oggetti vengono eliminati). Anche questo è utile per i blendshape che arrivano DA altre applicazioni.<br><br> Nota che i livelli sono disattivati per impostazione predefinita. Attivali se devi regolarne i cursori. |
| Curva (Ripetitore)  |              ![](/icons/curve.webp)            | Solo per un tubo o un lathe: aggiunge come figlio dell'oggetto un ripetitore [Curva](#curve) che segue la stessa curva.                                                |
|        Tubo         |             ![](/icons/tube.webp)              | Per un lathe, aggiunge come figlio un [tubo](tools.md#tube) che ne segue il profilo. Per un cilindro, un cono o un toro, lo converte in un tubo della stessa forma, così puoi piegarlo lungo una curva. |




### Selezione multipla {#multiselection}
Selezionare più oggetti ti permette di fare due cose:
- usare lo strumento gizmo per spostare più oggetti insieme
- fondere gli oggetti con le operazioni di unione e booleane.

Nella vista ad albero, tocca l'icona di selezione di ogni oggetto oppure trascina lungo la colonna di selezione. Quando tocchi i nomi, tieni premuta la scorciatoia `Maschera` (o `Ctrl` sulla tastiera) per aggiungere o togliere un singolo oggetto, oppure la scorciatoia `Leviga` (o `Shift`) per selezionare tutti gli oggetti tra quello corrente e quello che tocchi.

::: tip Selezione multipla rapida
Puoi selezionare più oggetti anche nel viewport, tenendo premuta la scorciatoia `Leviga` (o `Shift`) e toccando un'altra mesh.

Puoi deselezionare un oggetto toccandolo di nuovo (solo se la selezione contiene più di un oggetto).
:::

Il gizmo sposta tutti gli oggetti selezionati insieme, vedi [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Unisci {#join}
Questa opzione crea semplicemente un unico oggetto a partire da più oggetti selezionati.
I punti e le UV più vicini del [raggio di saldatura](#weld-radius) vengono fusi.

Trovi un esempio in video nella sezione [Dividi](#separate).

## ![](/icons/bool_subtract_circle.webp) Booleano {#boolean}
![](/images/scene_boolean_menu.webp) 
Combina più oggetti in un'unica superficie.

`Unione voxel` conserva il volume degli oggetti e calcola sulla superficie nuovi poligoni distribuiti in modo uniforme. Grazie a questo passaggio di calcolo, un'unione voxel riesce a gestire geometrie complesse, ma può perdere i dettagli fini se la risoluzione scelta non è abbastanza alta.

`Booleano` cerca di lasciare i poligoni nella loro disposizione originale e li cuce dove gli oggetti si sovrappongono. Il risultato può essere molto più pulito e netto di un'unione voxel, ma richiede mesh "stagne": gli oggetti non devono avere aperture o forme malformate. Se non funziona, di solito un'unione voxel ci riesce.

### Operazioni booleane {#boolean-operations}
Sia Unione voxel sia Booleano usano la visibilità degli oggetti per controllare l'operazione, come ricordano le note in fondo al popup:

#### Unione {#union}
Entrambi gli oggetti visibili danno un'**unione** booleana: le superfici esterne degli oggetti vengono combinate, senza superfici interne. ![](/images/boolean_union.webp)

#### Sottrazione {#subtract}
Un oggetto invisibile = **sottrazione** booleana: l'oggetto invisibile viene sottratto da quello visibile. ![](/images/boolean_subtract.webp)

#### Intersezione {#intersect}
Entrambi gli oggetti invisibili = **intersezione** booleana: crea una nuova forma solo dove i due oggetti si sovrappongono. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Unione voxel {#voxel-merge-button}
Questo pulsante esegue un'unione voxel sugli oggetti selezionati. Se lo usi su un solo oggetto, ne ricostruisce la topologia con poligoni distribuiti in modo uniforme: utile quando un oggetto ha poligoni stirati. Le opzioni qui sotto funzionano come quelle del [Remesher voxel](topology.md#voxel-remesher).

### Risoluzione {#resolution}
La risoluzione della griglia 3d di voxel usata per il calcolo. Quando modifichi questo valore, sull'oggetto compare una scacchiera che mostra in anteprima la dimensione dei poligoni.

Il contagocce accanto al cursore prende il dettaglio dalla densità della mesh sotto il tuo dito. Il pulsante accanto trasforma il cursore in una `Lunghezza bordo`, una dimensione nel mondo: lo stesso valore dà lo stesso dettaglio su qualsiasi oggetto.

### Crea multirisoluzione {#build-multiresolution}
Crea dei livelli di multirisoluzione sotto la risoluzione scelta. Quindi, se la risoluzione è 400 e `Crea multirisoluzione` è 3, otterrai una nuova mesh di circa 296.000 poligoni, ma con 3 livelli di suddivisione più bassi, di circa 74.000, 18.500 e 4.600.

### Ispessisci le parti sottili {#thicken-thin-parts}
Ispessisce le parti troppo sottili per la griglia di voxel, così non si spezzano. Non è disponibile con `Bordi affilati` o `Bordo netto`.

### Aperture {#holes}
Come vengono chiuse le aperture degli oggetti aperti prima dell'unione:
* `Riempi` - ogni apertura viene chiusa da sola, a partire dal suo bordo.
* `Forma` - le aperture vengono chiuse seguendo la superficie circostante, e i pezzi aperti che si sovrappongono vengono uniti.

### ![](/icons/angle.webp) Mantieni bordi affilati {#keep-sharp-edges}
Il pulsante `Bordi affilati` aggancia la mesh voxel agli spigoli vivi degli oggetti. Funziona meglio sulle forme semplici, e in alcune zone può introdurre distorsioni.

### ![](/icons/group.webp) Bordo netto {#sharp-border}
Le nuove facce seguono i bordi dei gruppi di facce, e un bordo resta netto dove la superficie forma una piega lungo di esso.

### ![](/icons/group_separate.webp) Gruppi separati {#keep-groups-separate}
Ogni gruppo di facce viene ricostruito per conto suo: i gruppi non si fondono mai, e ciascuno resta un pezzo chiuso nel proprio gruppo. In questa modalità la multirisoluzione non viene creata.

### ![](/icons/bool_subtract_circle.webp) Pulsante Booleano {#boolean-button}
Questo pulsante esegue un'operazione booleana sui poligoni, usando la libreria Manifold di Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Pulisci sovrapposizioni {#clean-overlaps}
Quando è selezionato un solo oggetto, il pulsante `Booleano` diventa `Pulisci sovrapposizioni`: fonde le parti dell'oggetto che si attraversano in una superficie pulita.


## ![](/icons/separate.webp) Dividi {#separate}
Se hai un unico oggetto composto da più parti scollegate, puoi dividerlo in più oggetti.
Puoi vederla come l'operazione opposta di [Unisci](#join).

Il popup `Dividi...` offre tre modi per dividere gli oggetti selezionati:
* `Dividi per Parti` - crea un oggetto separato per ogni parte scollegata.
* `Dividi per Gruppi` - crea un oggetto separato per ogni gruppo di facce.
* `Dividi per Livelli` - crea oggetti separati per la mesh di base e per ogni livello.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Aggiungi {#add-menu}

![](/images/scene_addmenu_overview.webp)

Questo menu crea primitive, gruppi, fotocamere, ripetitori e luci.

Le primitive sono forme di base che puoi regolare tramite dei parametri. Quando la primitiva è come la vuoi, la "confermi": i parametri vengono trasformati in una mesh di poligoni che puoi scolpire e dipingere. Una volta confermata, non puoi più modificare i parametri della primitiva.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Sul gizmo {#on-gizmo}
Posiziona la nuova primitiva dove si trova la forma selezionata o il gizmo. Quando è disattivato, la primitiva viene posizionata al centro della scena.

### ![](/icons/gizmo.webp) Seleziona gizmo {#select-gizmo}
Passa automaticamente allo strumento gizmo quando crei una nuova primitiva.

### ![](/icons/cog.webp) Avanzato {#add-advanced}

Questo menu ti permette di scegliere dove creare le nuove primitive, i gruppi e i ripetitori: sull'oggetto selezionato, all'origine del mondo, o nella posizione del gizmo.


### UV {#uvs}
L'interruttore `UV` accanto al titolo Primitiva attiva le UV sulle primitive. Le UV (spesso chiamate coordinate di texture) sono dati aggiuntivi usati nel 3d per applicare le texture alle superfici. Occupano più memoria, ma sulla maggior parte dei dispositivi non dovrebbe essere un problema, a meno di arrivare a un numero di poligoni molto alto (per esempio 10 milioni o più).

### Primitive {#primitives}

| Primitiva              | Icona                                     | Descrizione                                                                                                     |
| :--------------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Parallelepipedo        | ![](/icons/cube.webp)                    | È un semplice cubo, di cui puoi controllare le divisioni in X, Y e Z                                            |
| Sfera Quad             | ![](/icons/circle.webp)                  | Un parallelepipedo suddiviso con `Proietta sulla sfera` forzato, così ha una disposizione regolare di quad, ottima per scolpire |
| Cilindro               | ![](/icons/cylinder.webp)                | Puoi aggiungere un'apertura centrale al cilindro, per esempio per fare un tubo cavo                             |
| Toro                   | ![](/icons/torus.webp)                   | Il toro può essere un buon punto di partenza per gli anelli                                                     |
| Cono                   | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosaedro              | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Sfera UV               | ![](/icons/circle.webp)                  | Una sfera con una disposizione irregolare dei poligoni, vedi l'[avviso più sotto](#uv-sphere)                   |
| Piano                  | ![](/icons/rectangle.webp)               | È un semplice piano; nota che è l'unica primitiva non chiusa                                                    |
| Testo                  | ![](/icons/text.webp)                    | Testo 3d, con carattere, stile, allineamento, profondità e piega. `Unisci lettere` fonde le lettere che si toccano |
| Tubo                   | ![](/icons/tube.webp)                    | vedi [Tubo](tools#tube)                                                                                         |
| Lathe                  | ![](/icons/lathe.webp)                   | vedi [Lathe](tools#lathe)                                                                                       |
| Triplanare             | ![](/icons/triplanar.webp)               | vedi [Triplanare](#triplanar)                                                                                   |
| VDM                    | ![](/icons/vdm.webp)                     | Un piano pronto per scolpire un timbro di vector displacement: include le UV ed è rivolto verso la fotocamera   |
| Raccoglitore di ombre  | ![](/icons/material_shadow_catcher.webp) | vedi [Raccoglitore di ombre](#shadow-catcher)                                                                   |
| Testa                  | ![](/icons/face.webp)                    | Una testa semplice, con un livello per passare da maschile a femminile                                          |

::: tip
Se ti chiedi cosa sia la mesh di base all'avvio di Nomad: è anch'essa un parallelepipedo suddiviso.
Però la mesh di base di Nomad non usa `Proietta sulla sfera`, quindi non è perfettamente rotonda.
:::

### Barra degli strumenti della primitiva {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Quando crei una primitiva, compare una barra degli strumenti per controllarne i parametri.

* `Conferma` Trasforma la primitiva in un oggetto normale, così puoi scolpirla e dipingerla.
* `Specchio` Aggiunge o toglie un ripetitore specchio sopra la primitiva.
* `Tutti` (icona a occhio) Sceglie quali maniglie mostrare direttamente sulla primitiva per controllarne i parametri, per esempio la larghezza del cubo o il raggio dell'apertura di un cilindro: `Nessuno`, `Tutti`, o un solo tipo (raggio, apertura, profilo...) a seconda della primitiva.
* `Divisione` Il numero di divisioni della primitiva, qui lungo X per un parallelepipedo.
* `Densità costante` Quando stiri la primitiva lungo un asse con il gizmo, aumentano la sua dimensione e le sue divisioni invece di stirarsi i poligoni, così le facce restano quadrate. Disponibile su parallelepipedi, piani e cilindri.
* `...` Mostra il menu della primitiva.

Alcune primitive hanno opzioni aggiuntive nella barra:

* `Sfera` La sfera è costruita come un cubo suddiviso, perché è meglio per scolpire, ma così non è perfettamente rotonda. Questa opzione avvicina la forma a una sfera perfetta. Anche l'icosaedro ha questa opzione.
* `Estremità` Attiva o disattiva i tappi alle estremità di una forma: per esempio un cilindro può avere i tappi sopra, sotto, su entrambi i lati o su nessuno.
* `Apertura` Crea un'apertura che attraversa il centro della forma. Passa ciclicamente da nessuna apertura, a un'apertura con un solo raggio, a un'apertura con raggi diversi sopra e sotto.
* `Raggio` Sceglie se un cilindro ha un solo raggio, o raggi diversi sopra e sotto.
* `Disco` Sceglie se un piano è una forma a 4 lati o un cerchio.

La piccola barra sotto quella principale ti permette di passare dal gizmo della primitiva al gizmo di trasformazione.

::: tip

Toccando il titolo della barra la sposti in alto o in basso sullo schermo. Toccando la freccia nell'angolo la comprimi.

:::


### Menu della primitiva {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Contiene tutti i parametri della primitiva selezionata. I parametri sono la descrizione di base di una forma. Per descrivere un anello, per esempio, indicheresti il raggio esterno, il raggio interno e il numero di poligoni.

La maggior parte dei parametri delle primitive si spiega da sé, e alcuni sono comuni a tutte le primitive:

* `UV` Il piccolo pulsante UV in cima al menu attiva o disattiva la creazione delle coordinate UV
* `Conferma` Il piccolo pulsante di conferma trasforma la primitiva in un oggetto normale, così puoi scolpirla e dipingerla.
* `Facce max` Imposta un limite massimo al numero di poligoni dell'oggetto, per evitare che il dispositivo vada in crash.
* `Post-suddivisione` Applica il numero di suddivisioni scelto, tramite la sezione multirisoluzione del menu Topologia. Combinata con poche divisioni di topologia, serve a creare primitive levigate con angoli morbidi. Per esempio, con le divisioni di topologia di un parallelepipedo a 2 e la post-suddivisione a 4, ottieni un parallelepipedo dagli angoli arrotondati.
* `Suddivisione lineare` Imposta quanti livelli di suddivisione lineare usare prima della normale suddivisione levigata. Serve a controllare quanto sono netti o morbidi gli angoli delle superfici suddivise. Per esempio, imposta le divisioni di topologia di un parallelepipedo a 2 e la post-suddivisione a 4, poi prova a variare la suddivisione lineare tra 0 e 4: gli angoli del parallelepipedo passeranno da morbidi a netti.

### Topologia {#topology}

Controlla il numero di poligoni di una primitiva. Di solito i controlli sono collegati, quindi muovendo l'unico cursore attivo regoli tutti i poligoni in modo uniforme. Puoi toccare il pulsante di scollegamento per controllare separatamente le divisioni X/Y/Z di una forma.

### Geometria {#geometry}

Controlla la dimensione complessiva di una primitiva, in unità X/Y/Z per le forme squadrate e come raggio per le forme rotonde.


### ![](/icons/circle.webp) Sfera UV {#uv-sphere}
::: warning
La Sfera UV non è molto adatta per scolpire, soprattutto ai poli.

Preferisci la [primitiva](#primitives) Sfera Quad, Parallelepipedo o Icosaedro, insieme all'opzione `Proietta sulla sfera`.

Nota che la topologia può andare bene per scolpire se usi un valore molto basso per i cursori `Divisione`.
Poi puoi usare il cursore `Suddivisione complessiva` per aumentare il numero di poligoni.

Anche se non è adatta per scolpire in generale, è utile per gli occhi: se ruoti la sfera in modo che i poli si trovino sulla pupilla, la disposizione dei poligoni si presta naturalmente a dipingere e scolpire l'iride e la pupilla.
:::


### ![](/icons/triplanar.webp) Triplanare {#triplanar}
Questa primitiva è speciale: per modellarne la geometria si usa lo [strumento Maschera](tools.md#mask).

![](/videos/triplanar.mp4)


::: tip
Tocca due volte un piano e la fotocamera si centrerà proprio su quel piano.
Però non funziona se hai ruotato la primitiva con il gizmo.
:::

La triplanare usa le informazioni di maschera di 3 piani per riempire una griglia di voxel, che viene poi trasformata in poligoni (grazie al [Remesher voxel](topology.md#voxel-remesher)).

Ogni piano ha il suo piano di simmetria.

::: warning
Ogni volta che cambi la dimensione della primitiva Triplanare, la qualità della maschera dipinta peggiora.

Per ora non c'è un'opzione per "bloccare" la pittura su un solo piano, ma forse arriverà in futuro.
Puoi aiutarti un po' con la [Topologia collegata](stroke.md#connected-topology): se il cursore si trova esattamente su un piano, non influirà sugli altri piani.
:::

### ![](/icons/material_shadow_catcher.webp) Raccoglitore di ombre {#shadow-catcher}
Aggiunge un piano con il materiale raccoglitore di ombre. Vedi il [materiale Raccoglitore di ombre](material.md#shadow-catcher) per maggiori dettagli.


## Gruppo/Fotocamera {#groupcamera}
### ![](/icons/share.webp) Gruppo {#group}
Crea un oggetto "vuoto" sotto cui puoi mettere altri oggetti come figli. Puoi usarlo semplicemente per organizzare la gerarchia, mettendo molti oggetti sotto un gruppo e poi chiudendolo. Un gruppo può anche aiutarti a spostare gli oggetti: metti molti oggetti sotto un gruppo, poi sposta, ruota e scala il gruppo con lo strumento gizmo.

### ![](/icons/camera.webp) Fotocamera {#add-view}
Crea una fotocamera.

## Ripetitori {#repeaters}
![](/images/scene_primitive_repeaters.webp)

I ripetitori sono nodi che creano istanze degli oggetti posti sotto di essi.

### ![](/icons/array.webp) Array {#array}
![](/images/scene_primitive_array.webp)

Gli oggetti messi come figli di questo nodo possono essere ripetuti come istanze su una griglia. Quando è selezionato, offre questi controlli:
* `Adatta all'interno` - quando è attivo, tutte le copie vengono posizionate dentro i limiti dell'array; quando è disattivato, i cursori impostano lo spazio tra le copie
* `Conteggio X/Y/Z` - il numero di istanze su ogni asse
* `Dimensione X/Y/Z` - la dimensione della griglia lungo ogni asse, o la distanza tra le copie quando `Adatta all'interno` è disattivato
* `Randomizza...` - aggiunge variazioni casuali alle copie, vedi [Randomizza](#curve) più sotto.

### ![](/icons/curve.webp) Curva {#curve}
![](/images/scene_primitive_curve.webp)
Crea una curva: i figli di questo nodo vengono ripetuti lungo la curva. Quando è selezionato, offre questi controlli:
* `Curva` - modifica la curva: aggiungi punti alla curva e sposta i punti sulla curva.
* `Mostra` - mostra o nasconde la curva e i suoi punti.
* `Aggancio` - aggancia i punti della curva ad altra geometria.
* `Simm` - modifica la curva in modo simmetrico.
* `Chiuso` - unisce l'inizio e la fine della curva, oppure la lascia aperta.
* `B-spline` - fa seguire alle istanze la curva esattamente, oppure usa un'interpolazione b-spline, che dà risultati più morbidi.
* `Deforma` - piega ogni copia lungo la curva, così le copie si congiungono alle vicine (`Morbido` ne piega i lati perché si congiungano senza angolo).
* `Allinea` - ruota le copie per seguire la direzione della curva.
* `Pivot` - il pivot delle copie: la curva stessa (`Se stessa`) o i suoi figli.
* `Conteggio` - il numero di istanze. Il pulsante di modalità accanto passa a `Distanza`: una spaziatura fissa tra le copie, e il numero segue la lunghezza della curva.
* `Raggio` - controlli su ogni punto della curva per impostare la scala delle istanze.
* `Torsione` - controlli su ogni punto della curva per impostare la rotazione di torsione delle istanze.
* `Alterna` - ruota una copia sì e una no attorno alla curva: 90° per gli anelli di una catena, 180° per foglie o denti di una cerniera, attorno all'`Asse` che scegli.
* `Spirale...` - avvolge le copie attorno alla curva, in più fili (corda, treccia, nastro...).
* `Randomizza...` - aggiunge variazioni casuali alle copie; ogni riga può invece aggiungere la stessa quantità a ogni copia.

Sotto la barra degli strumenti, l'interruttore `(unisci)` fonde un punto con un altro quando lo trascini sopra di esso. `IK` (cinematica inversa) ti permette di mettere in posa la curva: trascina un punto e i punti collegati lo seguono. Tocca un punto per bloccarlo o sbloccarlo, tieni premuto per bloccarli o sbloccarli tutti; i punti bloccati restano fermi.

### ![](/icons/radial.webp) Radiale {#radial}
![](/images/scene_primitive_radial.webp)

I figli di questo nodo vengono ripetuti come istanze su un cerchio. Sposta l'oggetto figlio per cambiare il raggio di questo ripetitore. Quando è selezionato, offre questi controlli:
* RadialeX/Y/Z - questi pulsanti impostano l'asse radiale e il numero di istanze.



### ![](/icons/mirror.webp) Specchio {#mirror}
![](/images/scene_primitive_mirror.webp)

I figli di questo nodo vengono specchiati rispetto a un asse. Quando è selezionato, offre questi controlli:
* Gizmo - attiva il gizmo di trasformazione per impostare il centro dello specchio. Puoi anche ruotarlo e scalarlo. Quando hai finito, tocca di nuovo gizmo per far ricomparire i controlli normali.
* X/Y/Z - imposta il piano dello specchio

### ![](/icons/surface.webp) Superficie {#surface}

I figli di questo nodo vengono copiati sulla superficie di un oggetto: una copia per faccia, per spigolo o per vertice, oppure distribuite a caso. Quando è selezionato, offre questi controlli:
* Modalità - posiziona le copie sulle `Facce`, sugli `Spigoli` o sui vertici, oppure le `Distribuisci`.
* Ogni - una copia ogni N facce, spigoli o vertici. `Casuale` li sceglie invece a caso, e `Rimescola` estrae un'altra serie casuale.
* Spaziatura - quando distribuisci, la distanza minima tra due copie.
* Allinea - le copie poggiano sulla superficie seguendone la normale, invece di mantenere l'orientamento dell'originale.
* Aggancia - proietta l'originale sul punto più vicino della superficie, e le copie lo seguono.
* Adatta dimensione, Inclina - scalano e deformano le copie secondo la forma di ogni faccia.
* Deforma - piega ogni copia sulla sua faccia, o lungo il suo spigolo, così le copie vicine si congiungono senza spazi.

Tutti i ripetitori hanno un controllo `Conferma`, che trasforma il risultato del ripetitore in oggetti normali e ti chiede come farlo:
* Unisci figli - le istanze vengono unite in un unico oggetto
* Mantieni istanze - le istanze restano istanze, ma non hanno più il ripetitore come "genitore"
* Disinstanzia - le istanze vengono convertite in oggetti unici

`Appiattisci tutto` conferma anche i ripetitori annidati dentro questo, così ogni copia diventa un oggetto normale.

::: tip Consiglio: Combinare i ripetitori
I ripetitori possono essere messi uno sotto l'altro, e più oggetti possono diventare figli dei ripetitori: così ottieni effetti complessi.

![](/images/scene_repeater_combine.webp)
:::

::: tip Consiglio: Pivot dei ripetitori

Alcuni ripetitori cercano di gestire automaticamente il pivot degli oggetti figli, quindi anche se li sposti o li ruoti con lo strumento gizmo, non si muovono. Se devi aggirare questo comportamento, inserisci un gruppo tra il ripetitore e il figlio. Ora puoi spostare la forma figlia indipendentemente dal ripetitore.
:::

## Luce {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Direzionale {#directional}
Crea una luce direzionale, una sorgente di luce infinitamente lontana, come il sole.

### ![](/icons/panorama.webp) Ambiente {#environment}
Crea una luce ambiente, che illumina la scena da un'immagine che la circonda (illuminazione basata su immagini, come un HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Crea una luce spot, con controlli per l'ampiezza e la morbidezza del cono.

### ![](/icons/light.webp) Puntiforme {#point}
Crea una luce puntiforme.

## ![](/icons/cog.webp) Avanzato {#advanced}
Il pulsante `Avanzato` in basso a sinistra del pannello apre un popup con due schede: `Generale` e `Sincronizza`.

### ![](/icons/focus.webp) UI: Focalizzare sull'oggetto con doppio tocco {#focus-on-item}
Toccando due volte un elemento nell'elenco della Scena, la fotocamera si centra su quell'elemento nella vista 3d.

### ![](/icons/eye_open.webp) Sincronizza visibilità {#sync-visibility}
Quando è attiva, l'icona a occhio di un elemento selezionato agisce su tutti gli elementi selezionati.

### ![](/icons/bang.webp) Evidenziazione {#highlight}
Evidenzia gli oggetti selezionati nel viewport quando la selezione cambia.

### ![](/icons/link.webp) Mostra (Istanza) {#instance-show}
Mostra una capsula colorata a sinistra dell'elenco della scena per indicare le istanze.

### ![](/icons/preview.webp) Anteprime oggetti {#object-previews}
Mostra una miniatura renderizzata per ogni oggetto nell'elenco della scena. È lo stesso del pulsante di anteprima sopra l'elenco.

### Raggio di saldatura {#weld-radius}
Sotto il titolo `Unisci`, `Raggio saldatura posizione` e `Raggio saldatura UV`: i punti e le UV più vicini di questi raggi vengono fusi. Ciascuno si può disattivare con la sua casella di spunta. Vale per Unisci, Booleano, Rifila, Decima, il remeshing e l'importazione dei file.

### Icone {#icons}
Imposta la `Dimensioni` minima e massima e l'`Opacità` delle icone di gruppi, luci, fotocamere e ripetitori nel viewport.

### ![](/icons/hierarchy.webp) Linee gerarchiche {#hierarchy-lines}
Mostra nel viewport una linea tra un genitore e i suoi figli. Quando è attivo, puoi anche impostare:
* `Usa pivot Nomad` - le linee partono dal pivot usato dagli strumenti Trasforma e Gizmo. Quando è disattivato, usano il pivot di base naturale, che può essere lontano dal centro dell'oggetto.
* `Spessore` - la larghezza delle linee. Il pulsante accanto al cursore aggiunge loro un contorno.
* Il colore delle linee.

### ![](/icons/link.webp) Sincronizza {#sync}
La scheda `Sincronizza` stabilisce, per ogni operazione (`Aggiungi`, `Elimina`, `Blocca`, `Clona`, `Istanza`, `Disinstanzia`, `Unisci`, `Dividi` e `Booleano`), se si applica a tutte le istanze della selezione:
* `Auto` - segue la casella `Sincronizza` in cima al menu Scena.
* `No` - solo gli oggetti selezionati.
* `Sì` - sempre tutte le istanze.

Per impostazione predefinita `Unisci`, `Dividi` e `Booleano` sono su `Sì` e gli altri su `Auto`. `Ripristina` riporta questi valori predefiniti.

## Barra inferiore {#bottom-toolbar}
Queste icone mostrano o nascondono nel viewport gruppi, luci, fotocamere, ripetitori e linee gerarchiche. Le icone mostrate nel canvas si possono toccare per selezionarle e modificarle direttamente.
