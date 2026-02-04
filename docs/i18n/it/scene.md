# ![](/icons/scene.webp) Scena {#scene}

Questo menu consente di gestire oggetti, luci, camere e ripetitori in Nomad. Mostra la gerarchia della scena come una vista ad albero, permettendoti di modificare molti aspetti dei tuoi oggetti. Consente anche di creare nuovi oggetti, nonché di combinare e separare oggetti in vari modi.


![](/images/scene_menu_summary.webp)


## Barra di scelta rapida {#shortcut-bar}
| Azione                | Icona                             | Descrizione                                                                                                        |
| :-------------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| [Aggiungi...](#add-menu) | ![](/icons/plus.webp)            | Mostra il [menu Aggiungi](#add-menu) per aggiungere un oggetto alla scena                                          |
| Elimina               | ![](/icons/trash.webp)           | Elimina l'oggetto                                                                                                  |
| Blocca                | ![](/icons/lock.webp)            | Rende l'oggetto non selezionabile nella viewport. Può comunque essere selezionato dalla vista ad albero.          |
| Unisci                | ![](/icons/merge.webp)           | Unisce gli oggetti selezionati in un singolo oggetto senza modifiche alla geometria                               |
| Separa                | ![](/icons/diagonal.webp)        | Se un oggetto è composto da gusci poligonali distinti, li suddivide in oggetti separati. L'operazione inversa di Unisci |
| [Booleana...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Mostra il menu [Booleana](#boolean)                                                                                |
| Clona                 | ![](/icons/clone.webp)           | Duplica l'oggetto in un nuovo oggetto                                                                              |
| Istanza               | ![](/icons/link.webp)            | Duplica l'oggetto come istanza, così le modifiche di modellazione su uno vengono applicate a tutte le istanze      |
| Rimuovi istanza       | ![](/icons/unlink.webp)          | Converte un'istanza in una forma unica, così le modifiche di modellazione non vengono più copiate alle altre istanze |
| Sincronizza           | ![](/icons/link.webp)            | Se le istanze hanno figli, assicura che tutte le istanze condividano la stessa gerarchia di figli                 |


## Vista ad albero {#tree-view}
![](/images/scene_treeview.webp) 

| Azione       | Icona                      | Descrizione              |
| :----------: | :------------------------: | :----------------------: |
| Seleziona    | ![](/icons/checked.webp)  | Attiva/disattiva selezione |
| Visibile     | ![](/icons/eye_open.webp) | Attiva/disattiva visibilità |
| Menu         | ![](/icons/more.webp)     | Mostra il menu oggetto   |

::: tip SUGGERIMENTO: Selezionare o nascondere rapidamente molti oggetti

Tocca l'icona di selezione per attivare/disattivare un singolo oggetto, oppure trascina verticalmente sulla colonna di selezione per selezionare molti oggetti. Lo stesso si può fare con la colonna di visibilità.

:::

### Manipolazione della vista ad albero {#tree-view-manipulation}

Tieni premuto a lungo su un elemento nella vista ad albero finché non diventa giallo. Puoi quindi spostarlo verso l'alto o verso il basso nella vista ad albero, nonché trascinarlo sopra un altro elemento per renderlo figlio di quell'elemento.

Quando molti elementi sono selezionati, la maggior parte sarà giallo scuro, uno sarà giallo più chiaro. Tieni premuto a lungo e trascina l'elemento più chiaro per spostare tutti gli oggetti contemporaneamente.

Quando selezioni un elemento padre, per impostazione predefinita verranno selezionati anche tutti gli elementi figli. Toccando l'icona del padre si alterna tra la selezione del solo padre, o del padre e dei figli.

### Menu oggetto {#object-menu}

Facendo clic sul pulsante con i tre puntini (...) per un oggetto nella vista ad albero verrà mostrato il menu oggetto. 
Molte di queste opzioni sono simili alla barra scorciatoie in alto, ripetute per comodità.

|       Azione        |                        Icona                        | Descrizione                                                                                                                                                             |
| :-----------------: | :-------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Istanza        |               ![](/icons/link.webp)               | Duplica l'oggetto come istanza, così le modifiche di modellazione su uno vengono applicate a tutte le istanze                                                          |
|        Clona        |              ![](/icons/clone.webp)               | Duplica l'oggetto in un nuovo oggetto                                                                                                                                   |
|        Nome         |              ![](/icons/pencil.webp)              | Cambia il nome dell'oggetto                                                                                                                                             |
|       Elimina       |              ![](/icons/trash.webp)               | Elimina l'oggetto                                                                                                                                                       |
|      Elimina+       |            ![](/icons/removeNode.webp)            | Elimina l'oggetto e i suoi figli                                                                                                                                        |
|   Rimuovi istanza   |              ![](/icons/unlink.webp)              | Converte un'istanza in una forma unica, così le modifiche di modellazione non vengono più copiate alle altre istanze                                                   |
| Separare topologia  |             ![](/icons/separate.webp)             | Se un oggetto è composto da gusci poligonali distinti, li suddivide in oggetti separati. L'operazione inversa di Unisci                                                |
| Separa gruppo facce |            ![](/icons/faceGroup.webp)             | Se un oggetto ha più gruppi di facce, suddivide la mesh in oggetti separati                                                                                            |
|  Separa livelli     |              ![](/icons/layer.webp)               | Se un oggetto ha livelli, suddivide ogni livello in un oggetto separato. Utile per inviare blendshape ad altre applicazioni                                            |
|   Unisci -> Livelli | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Se sono selezionati più oggetti con topologia corrispondente, li unisce in livelli per l'oggetto principale (gli altri oggetti verranno eliminati). Ancora una volta, utile per blendshape provenienti DA altre applicazioni.<br><br> Nota che i livelli saranno disabilitati per impostazione predefinita. Abilitali se hai bisogno di regolare i loro slider. |




### Selezione multipla {#multiselection}
Puoi selezionare più oggetti per ottenere due cose:
- usare lo strumento gizmo per spostare più oggetti contemporaneamente
- unire oggetti usando operazioni di unione e booleane.

Puoi farlo usando la casella di controllo `Multiselection`, e poi facendo clic sull'oggetto nell'elenco.

::: tip Selezione multipla rapida
Puoi anche selezionare più oggetti nella viewport tenendo premuta la scorciatoia `Smooth` e toccando un'altra mesh.

Puoi deselezionare un oggetto toccandolo di nuovo (solo se la tua selezione contiene più di un oggetto).
:::

::: warning Funzionalità gizmo limitata
Quando usi la selezione multipla, lo strumento gizmo ignorerà sempre il mascheramento.
Inoltre, la scalatura X/Y/Z è disabilitata.

Il motivo è che la selezione multipla consente solo trasformazioni dell'intera mesh, non trasformazioni per vertice.
Questo potrebbe essere migliorato in futuro.
:::


## Unisci {#join}
Questa opzione creerà semplicemente una singola voce oggetto a partire da più oggetti selezionati.

Puoi vedere un esempio in video nella sezione [Separa](#separate).

## Booleana {#boolean}
![](/images/scene_boolean_menu.webp) 
Combina oggetti in una singola superficie.

`Voxel merge` manterrà il volume degli oggetti e calcolerà nuovi poligoni equidistanti sulla superficie. A causa della fase di calcolo, un'unione voxel può gestire geometrie complesse, ma può perdere dettagli fini se la risoluzione di destinazione non è sufficientemente alta.

`Boolean` tenterà di mantenere i poligoni nel loro layout originale e cucire i poligoni dove gli oggetti si sovrappongono. Questo può produrre risultati molto più puliti e nitidi rispetto a un'unione voxel, tuttavia richiede mesh "stagni"; non possono esserci buchi o forme malformate negli oggetti. Se questo fallisce, di solito un'unione voxel funzionerà.

### Operazioni booleane {#boolean-operations}
Sia Voxel Merge che Booleana useranno la visibilità degli oggetti per controllare l'operazione:

#### Unione {#union}
Entrambi gli oggetti visibili creeranno una **unione** booleana, la pelle esterna degli oggetti viene combinata, senza superfici interne. ![](/images/boolean_union.webp)

#### Sottrai {#subtract}
Un oggetto invisibile = **sottrazione** booleana, l'oggetto invisibile verrà sottratto dall'oggetto visibile. ![](/images/boolean_subtract.webp)

#### Intersezione {#intersect}
Entrambi gli oggetti invisibili = **intersezione** booleana, crea una nuova forma solo dove i due oggetti si sovrappongono. ![](/images/boolean_intersect.webp)


### Pulsante Voxel Merge {#voxel-merge-button}
Premendo questo pulsante verrà eseguita un'operazione di unione voxel sugli oggetti selezionati. Se eseguita su un singolo oggetto, effettuerà una retopologia in poligoni equidistanti, utile quando un oggetto ha poligoni stirati.

### Risoluzione {#resolution}
La risoluzione della griglia 3D voxel utilizzata per il calcolo. Quando questo valore viene modificato, un motivo a scacchiera viene sovrapposto all'oggetto per mostrare in anteprima la dimensione dei poligoni.

### Crea multirisoluzione {#build-multiresolution}
Crea livelli di multirisoluzione al di sotto della risoluzione di destinazione. Quindi, se la tua risoluzione è 400 e "build multiresolution" è 3, otterrai una nuova mesh con, ad esempio, 296.000 poligoni, ma ci saranno 3 livelli di suddivisione inferiori a 74.000, 18.000, 4.000k.

### Mantieni spigoli vivi {#keep-sharp-edges}
Abilita l'aggancio della mesh voxel ai bordi. Funziona meglio su forme semplici.

### Pulsante booleana {#boolean-button}
Premendo questo pulsante verrà eseguita un'operazione booleana sui poligoni usando la libreria Manifold di Emmett Lalish. 


## Separa {#separate}
Se hai un singolo oggetto basato su diverse parti scollegate, puoi suddividere questo oggetto in più oggetti. 
Questo può essere visto come l'opposto della [Unione semplice](#simple-merge).

![](/videos/merge_separate.mp4)


## Menu Aggiungi {#add-menu}

![](/images/scene_addmenu_overview.webp)

Questo menu crea primitive, gruppi, camere, ripetitori e luci.

Le primitive sono forme di base che possono essere regolate tramite parametri. Una volta che hai regolato la primitiva secondo le tue esigenze, la "convalidi", operazione che converte tali parametri in una mesh poligonale che può essere scolpita e dipinta. Una primitiva non può più avere i suoi parametri modificati dopo essere stata convalidata.


![](/images/scene_addmenu_top.webp)

### Sul gizmo {#on-gizmo}
Abilita il posizionamento della nuova primitiva dove si trova la forma selezionata o il gizmo corrente. Quando è disabilitato, la primitiva verrà posizionata al centro della scena.

### Seleziona gizmo {#select-gizmo}
Abilita il passaggio automatico allo strumento gizmo quando viene creata una nuova primitiva. 

### Avanzato {#add-advanced}

Questo menu ti consente di impostare la tua preferenza per dove verranno create nuove primitive, gruppi, ripetitori. Possono essere sull'oggetto selezionato, all'origine del mondo o nella posizione del gizmo.


### UV {#uvs}
Abilita le UV sulle primitive. Le UV (spesso chiamate coordinate di texture) sono dati extra usati in 3D per permettere l'applicazione di texture sulle superfici. Occupano più memoria, ma per la maggior parte dei dispositivi questo non dovrebbe essere un problema a meno che tu non arrivi a conteggi poligonali molto alti (ad es. 10 milioni di poligoni o più). 

### Primitive {#primitives}

| Primitiva      | Icona                                     | Descrizione                                                                                                       |
| :------------: | :---------------------------------------: | :---------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | È un semplice cubo, puoi controllare le divisioni in X, Y e Z                                                     |
| Sfera          | ![](/icons/circle.webp)                  | Per comodità è chiamata Sfera ma in realtà è un box suddiviso, con `Project on sphere` forzato                    |
| Cilindro       | ![](/icons/cylinder.webp)                | Puoi aggiungere un foro centrale alla primitiva cilindro, ad esempio per creare un tubo cavo                      |
| Toro           | ![](/icons/torus.webp)                   | Il toro può essere un buon punto di partenza per anelli                                                           |
| Cono           | ![](/icons/cone.webp)                    | -                                                                                                                 |
| Icosaedro      | ![](/icons/icosahedron.webp)             | -                                                                                                                 |
| Sfera UV       | ![](/icons/circle.webp)                  | Una sfera con disposizione poligonale irregolare, vedi [avviso sotto](#uv-sphere)                                 |
| Piano          | ![](/icons/rectangle.webp)               | È un semplice piano, nota che è l'unica primitiva che non è chiusa                                                |
| Tubo           | ![](/icons/tool_tube.webp)               | vedi [Tubo](tools#tube)                                                                                           |
| Tornio         | ![](/icons/tool_lathe.webp)              | vedi [Tornio](tools#lathe)                                                                                        |
| Triplanare     | ![](/icons/triplanar.webp)               | vedi [Triplanare](#triplanar)                                                                                     |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | vedi [Shadow Catcher](#shadow-catcher)                                                                            |
| Testa          | ![](/icons/face.webp)                    | Una semplice testa con un livello per sfumare tra maschile/femminile                                              |

::: tip
Se ti chiedi qual è la mesh di base quando avvii Nomad: è anch'essa un box suddiviso.
Tuttavia la mesh di base in Nomad non usa `Project on sphere`, il che significa che non è perfettamente rotonda.
:::

### Barra strumenti primitive {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Una volta creata una primitiva, apparirà una barra strumenti per controllarne i parametri.

* `Validate` Converte la primitiva in un oggetto standard in modo che possa essere scolpito e dipinto.
* `Edit` Attiva/disattiva la visualizzazione del gizmo della primitiva. Questo è mostrato direttamente sulla primitiva per controllarne i parametri, ad es. la larghezza del cubo o il raggio del foro di un cilindro.
* `Mirror` Attiva/disattiva il posizionamento di un ripetitore specchio sopra la primitiva.
* `...` Mostra il menu della primitiva.

Primitive diverse avranno opzioni extra sulla barra strumenti:

* `Project` La sfera è costruita come un cubo suddiviso, poiché questo è migliore per la scultura, ma significa che non è perfettamente rotonda. Questa opzione forzerà la forma più vicina a una sfera perfetta. L'icosaedro condivide questa opzione.
* `Cap` Attiva/disattiva i tappi terminali su una forma, ad es. un cilindro può avere tappi in alto, in basso, in entrambi o nessuno.
* `Hole` Attiva/disattiva un foro creato attraverso il centro di una forma. Cicla tra nessun foro, foro con un singolo raggio o foro con raggio diverso in alto e in basso.
* `Radius` Attiva/disattiva se un cilindro deve avere un singolo raggio o un raggio diverso in alto e in basso.
* `Disk` Attiva/disattiva se un piano deve essere una forma a 4 lati o una forma circolare.

La piccola barra strumenti sotto la barra principale ti permette di alternare tra il gizmo della primitiva e il gizmo di trasformazione.

::: tip

Facendo clic sul titolo della barra strumenti la sposterai in alto o in basso sullo schermo. Facendo clic sulla freccia nell'angolo la comprimerai.

:::


### Menu primitive {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Contiene tutti i parametri per la primitiva selezionata. I parametri sono le descrizioni di base di una forma. Per descrivere un anello, ad esempio, descriveresti il suo raggio esterno, il suo raggio interno e il numero di poligoni.

La maggior parte dei parametri delle primitive dovrebbe essere autoesplicativa, e ci sono alcuni parametri comuni condivisi tra tutte le primitive:

* `UVs` Il piccolo pulsante UVs in alto nel menu attiva/disattiva la creazione delle coordinate UV
* `Validate` Il piccolo pulsante Validate converte la primitiva in un oggetto standard in modo che possa essere scolpito e dipinto.
* `Max faces` Imposta un limite massimo al numero di poligoni nell'oggetto per evitare di mandare in crash il dispositivo.
* `Post subdivision` Abilita il numero scelto di suddivisioni dalla sezione multiresolution del menu topologia. Può essere usato per creare primitive con angoli morbidi e smussati in combinazione con basse divisioni di topologia. Ad esempio, impostando le divisioni di topologia di un box a 2 e le post subdivision a 4, otterrai un box con angoli morbidi.
* `Linear subdivision` Imposta quanti livelli di suddivisione lineare usare prima di usare la suddivisione morbida regolare. Può essere usato per controllare quanto sono netti o morbidi gli angoli sulle superfici suddivise. Ad es., imposta le divisioni di topologia di un box a 2, le post subdivision a 4, poi prova a cambiare le linear subdivision tra 0 e 4. Gli angoli del box passeranno da morbidi a netti.

### Topologia {#topology}

Controlla il numero di poligoni in una primitiva. Di solito i controlli sono collegati, quindi modificando l'unico slider attivo verranno regolati tutti i poligoni in modo uniforme. Puoi toccare il pulsante di scollegamento e controllare separatamente le divisioni X/Y/Z su una forma.

### Geometria {#geometry}

Controlla la dimensione complessiva di una primitiva, in unità X/Y/Z per le forme quadrangolari e in raggio per le forme rotonde.


### Sfera UV {#uv-sphere}
::: warning
La Sfera UV non è adatta alla scultura, specialmente ai poli.

Preferisci le primitive [Sfera](#sphere), [Box](#box) o [Icosaedro](#icosahedron), insieme all'opzione `Project on sphere`.

Nota che la topologia può essere accettabile per la scultura se usi un valore molto basso per gli slider `Division`.
Puoi poi usare lo slider `Overall Subdivision` per aumentare il numero di poligoni.

Pur non essendo adatta alla scultura generale, è utile per gli occhi; se ruoti la sfera in modo che i poli si trovino sulla pupilla, la disposizione dei poligoni si adatterà naturalmente per dipingere e scolpire iride e pupilla.
:::


### Triplanare {#triplanar}
Questa primitiva è particolare in quanto dovresti usare lo [strumento Maschera](tools.md#mask) su di essa per modellare la geometria.

![](/videos/triplanar.mp4)


::: tip
Tocca due volte su un piano e la camera si concentrerà su quel piano specifico.
Questo però non funzionerà se ruoti la primitiva con il gizmo.
:::

Triplanare usa le informazioni di maschera di 3 piani per riempire una griglia voxel che viene poi poligonalizzata (grazie al [Voxel Remesher](topology.md#voxel-remeshere)).

Ogni piano ha il proprio piano di simmetria.

::: warning
Ogni volta che aggiorni la dimensione della primitiva Triplanare, la qualità della pittura della maschera si degraderà.

Per ora non c'è un'opzione per "bloccare" la pittura su un singolo piano, ma potrebbe arrivare in futuro.
Puoi usare la [Topologia connessa](stroke.md#connected-topology) per aiutare un po', nel senso che se il cursore si trova precisamente su un piano non influenzerà gli altri piani.
:::

### Cattura ombra {#shadow-catcher}
Aggiunge un piano con il materiale shadow catcher. Vedi [materiale Shadow Catcher](material.md#shadow-catcher) per maggiori dettagli. 


## Gruppo/Camera {#groupcamera}
### Gruppo {#group}
Crea un oggetto "vuoto", al quale puoi collegare altri oggetti come figli. Può essere usato semplicemente per organizzare la gerarchia mettendo molti oggetti sotto un gruppo, quindi chiudendolo. Un gruppo può anche essere usato come aiuto per spostare oggetti; molti oggetti possono essere messi sotto un gruppo e poi il gruppo può essere spostato, ruotato, scalato con lo strumento gizmo.

### Aggiungi vista {#add-view}
Crea una camera.

## Ripetitori {#repeaters}
![](/images/scene_primitive_repeaters.webp)

I ripetitori sono nodi che creano istanze degli oggetti al di sotto di essi. 

### Array {#array}
![](/images/scene_primitive_array.webp)

Quando gli oggetti sono figli di questo nodo, possono essere istanziati in un layout a griglia. Quando è selezionato, ha controlli per:
* Fit inside - alterna tra il controllo della dimensione della griglia/scatola dell'array o il controllo dello spazio tra le istanze dell'array
* CountX/Y/Z - il numero di istanze su ciascun asse
* OffsetX/Y/Z - distanza tra le istanze quando "fit inside" è attivo
* SizeX/Y/Z - larghezza/altezza/profondità della griglia totale dell'array quando "fit inside" è attivo.

### Curva {#curve}
![](/images/scene_primitive_curve.webp)
Crea una curva, i figli di questo nodo verranno ripetuti lungo la curva. Quando è selezionato, ha controlli per:
* Edit - permette di aggiungere punti alla curva e spostare i punti sulla curva
* Snap - aggancia i punti della curva ad altra geometria
* Align - ruota le forme figlie per allinearle alla direzione della curva
* Count - il numero di istanze
* Closed - attiva/disattiva la chiusura della curva unendo inizio e fine, oppure la mantiene aperta
* Radius - attiva i controlli su ogni punto della curva per controllare la scala delle istanze
* Twist - attiva i controlli su ogni punto della curva per controllare la rotazione di torsione delle istanze 
* B-spline - attiva/disattiva il fatto che le istanze seguano esattamente la curva o usino l'interpolazione B-spline, che ha risultati più morbidi. 

### Radiale {#radial}
![](/images/scene_primitive_radial.webp)

I figli di questo nodo verranno istanziati in un cerchio. Sposta l'oggetto figlio per modificare il raggio di questo ripetitore. Quando è selezionato, ha controlli per:
* RadialX/Y/Z - selezionando questi pulsanti imposti l'asse radiale e il numero di istanze.



### Specchio {#mirror}
![](/images/scene_primitive_mirror.webp)

I figli di questo nodo verranno specchiati rispetto a un asse. Quando è selezionato ha controlli per:
* Gizmo - abilita il gizmo di trasformazione per impostare il centro dello specchio. Può anche essere ruotato e scalato. Quando hai finito, tocca di nuovo gizmo per mostrare i controlli standard.
* X/Y/Z - imposta il piano di specchio

Tutti i ripetitori hanno un controllo `Validate`, che converte in bake i risultati del ripetitore e chiede come eseguire il bake:
* Join children - le istanze vengono unite in un singolo oggetto
* Keep instances - le istanze rimangono istanze, ma non hanno più il ripetitore come "genitore"
* Un-instances - le istanze vengono convertite in oggetti unici

::: tip Suggerimento: combina i ripetitori
I ripetitori possono essere collegati come figli l'uno dell'altro e diversi oggetti possono essere resi figli dei ripetitori, portando a effetti complessi.

![](/images/scene_repeater_combine.webp)
:::

::: tip Suggerimento: pivot dei ripetitori

Alcuni ripetitori cercheranno di impostare automaticamente il pivot degli oggetti figli, quindi anche se li sposti o ruoti con lo strumento gizmo, non si muoveranno. Se hai bisogno di ignorare questo comportamento, inserisci un gruppo tra il ripetitore e il figlio. Ora puoi spostare la forma figlia indipendentemente dal ripetitore.
:::

## Luce {#light}

![](/images/scene_primitive_light.webp)

### Direzionale {#directional}
Crea una luce direzionale, una sorgente luminosa infinitamente lontana come il sole.

### Spot {#spot}
Crea una luce spot, con controlli sulla larghezza del cono e sulla morbidezza

### Punto {#point}
Crea una luce puntiforme

## Avanzato {#advanced}
### Metti a fuoco elemento {#focus-on-item}
Facendo doppio clic su un elemento nell'elenco Scena, la camera verrà centrata su quell'elemento nella vista 3D.

### Sincronizza visibilità {#sync-visibility}
Usare l'icona dell'occhio influenzerà tutti gli elementi selezionati. 

### Istanza: Mostra {#instance-show}
Mostra una capsula colorata a sinistra dell'elenco scena per indicare le istanze.


### Icone {#icons}
Imposta dimensione e opacità delle icone di gruppo, luce, camera, specchio nella viewport

### Linee gerarchia {#hierarchy-lines}
Mostra una linea tra il genitore e i suoi figli nella viewport

## Barra degli strumenti inferiore {#bottom-toolbar}
Queste icone attivano/disattivano la visibilità di Gruppo, Luce, Camera, Ripetitore e linee di gerarchia nella viewport.