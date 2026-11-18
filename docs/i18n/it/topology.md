# ![](/icons/multires.webp) Topologia {#topology}

Questo menu controlla la topologia degli oggetti in Nomad e raccoglie gli strumenti per trasferire (fare il bake) dettagli tra oggetti e tra texture.

![](/images/topology_overview.webp)

Nomad lavora con i poligoni: usa triangoli e quad per gestire la geometria.
Con topologia intendiamo sia il numero di facce, sia il modo in cui i punti (vertici) sono collegati tra loro.

È importante tenere d'occhio la topologia, soprattutto se vuoi scolpire o dipingere dettagli fini.

::: tip Come tenere d'occhio la topologia?
Puoi mostrare il [Wireframe](settings.md#wireframe) o semplicemente disattivare l'[Ombreggiatura uniforme](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Il menu Topologia di Nomad ha diverse schede, disposte su due righe:

| Metodo                                | Icona                        | Descrizione                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multirisoluzione](#multiresolution)  | ![](/icons/multires.webp)   | Lavora su più livelli di dettaglio grazie alla suddivisione      |
| [Remesher voxel](#voxel-remesher)     | ![](/icons/voxel.webp)      | Ricalcola una nuova topologia con densità uniforme               |
| [Topologia dinamica](#dynamic-topology) | ![](/icons/dynamic.webp)  | Aggiunge/rimuove facce localmente, in tempo reale, mentre scolpisci o dipingi |
| [Varie](#misc)                        | ![](/icons/topo_extra.webp) | Chiude le aperture, forza la mesh a essere manifold e la converte in triplanare |
| [Primitiva](#primitive)               | ![](/icons/dot.webp)        | Opzioni della primitiva                                          |
| [Decima](#decimation)                 | ![](/icons/decimate.webp)   | Riduce il numero di facce mantenendo la forma                    |
| [Remeshing quad](#quad-remesh)        | ![](/icons/quad.webp)       | Ricostruisce l'oggetto con una disposizione pulita di quad       |
| [Sviluppo UV](#uv-unwrap)             | ![](/icons/uv.webp)         | Crea le UV per applicare le texture                              |
| [Trasferisci](#bake)                  | ![](/icons/bake.webp)       | Trasferisce dettagli e pittura su texture, vertici o timbri VDM  |


## Statistiche dei poligoni {#polygon-stats}

![](/images/topology_stats.webp)

La parte alta di ogni scheda mostra il numero di poligoni dell'oggetto selezionato, e quello dell'intera scena quando contiene più di un oggetto. Le colonne indicano il numero di vertici, di triangoli, di quad (poligoni a 4 lati) e di coordinate UV (0 se l'oggetto non ha UV).

Tocca questa sezione per vedere l'elenco di tutti gli oggetti della scena con i loro conteggi esatti, compreso il numero di gruppi di facce.

## ![](/icons/cog.webp) Menu ingranaggio {#gear-menu}
Alcune sezioni, come quelle delle schede [Remeshing quad](#quad-remesh) e [Trasferisci](#bake), hanno opzioni aggiuntive. Le apri con l'icona a forma di ingranaggio accanto al titolo della sezione.

## ![](/icons/multires.webp) Multirisoluzione {#multiresolution}

![](/images/topology_multires_menu.webp)

### Che cos'è la multirisoluzione? {#what-is-multiresolution}
La multirisoluzione serve soprattutto in due casi:
- l'algoritmo di suddivisione levigata, per aumentare il numero di poligoni dell'oggetto
- gestire più livelli di risoluzione, così da alternare modifiche su piccola e su grande scala

![](/videos/multiresolution.mp4)

#### Flusso di lavoro in multirisoluzione {#multiresolution-workflow}
Un aspetto importante della multirisoluzione è che puoi tornare a una risoluzione più bassa, modificare l'oggetto e poi tornare alla risoluzione più alta senza perdere i dettagli ad alta risoluzione. Tutti i dettagli ad alta risoluzione vengono riproiettati automaticamente.

I [Livelli](layers.md#layers) sono disponibili a ogni risoluzione.

::: warning
Se usi uno strumento che modifica la topologia dell'oggetto, perderai tutte le altre risoluzioni!
Nomad dovrebbe sempre avvisarti quando sta per succedere, per esempio quando usi:
- il [Remesher voxel](#voxel-remesher)
- la [Topologia dinamica](#dynamic-topology)
- lo [strumento Rifila](tools.md#trim)
- lo [strumento Dividi](tools.md#split)
:::


### Cursore della multirisoluzione {#multiresolution-slider}
Questo cursore indica il numero di livelli di suddivisione dell'oggetto corrente. Se ci sono 6 barre verticali, ci sono 6 livelli di suddivisione. Il cerchio indica il livello di suddivisione visualizzato in quel momento.

Le piccole icone sopra il cursore mostrano quali opzioni (`Blocca livello 0`, `Lineare`, `Bordo netto`, `Mantieni triangoli`) sono state usate per ciascun livello.

### Rovescia {#reverse}
Quando sei al livello di suddivisione più basso, il pulsante `Rovescia` prova a creare un livello sotto quello corrente. In genere funziona solo se l'oggetto è nato da una suddivisione, per esempio in Nomad o in altre applicazioni 3d che usano superfici di suddivisione in multirisoluzione.

### Suddividi {#subdivide}
Il pulsante *Suddividi* moltiplica per 4 il numero di poligoni: tieni d'occhio il conteggio, perché può crescere molto in fretta! Nomad chiede una conferma quando il risultato sarebbe molto pesante.
Un aspetto importante delle *superfici di suddivisione* è che tendono verso una *superficie levigata*.
Per capire come funziona, prova il pulsante *Suddividi* su un oggetto con pochi poligoni.

Puoi disattivare questo comportamento *levigato* con l'opzione `Lineare`.

### Elimina inferiore {#delete-lower}
Elimina le suddivisioni sotto il livello visualizzato, se ce ne sono. Se lo fai per sbaglio, puoi ricrearle con il pulsante `Rovescia`.

### Elimina superiore {#delete-higher}
Elimina le suddivisioni sopra il livello visualizzato, se ce ne sono.

### ![](/icons/lock.webp) Blocca livello 0 {#lock-lv0}
Conserva la forma del livello di suddivisione più basso quando scolpisci sui livelli superiori. La pittura invece arriva comunque fino al livello 0. Può essere importante se l'oggetto è stato creato in un'altra applicazione e la mesh di base deve restare invariata.

Questa opzione è disponibile solo prima della prima suddivisione. Quando è disattivata, le modifiche importanti fatte ai livelli di suddivisione più alti spostano anche il livello 0.

### ![](/icons/linear.webp) Lineare {#linear-subdivision}
Suddivide la mesh senza applicare alcuna levigatura.

### ![](/icons/group.webp) Bordo netto {#sharp-border}
Se l'oggetto ha dei gruppi di facce, attivando questa opzione i bordi tra i gruppi restano netti. Si può impostare per ogni livello di suddivisione (il cursore della multirisoluzione mostra una piccola icona sopra il livello per indicarlo).

### ![](/icons/triangle.webp) Mantieni triangoli {#keep-triangles}
Quasi tutti i sistemi classici di superfici di suddivisione cercano di convertire tutti i poligoni in quad durante la suddivisione. Questa opzione obbliga invece la suddivisione a usare i triangoli.

::: tip

Di base la suddivisione arrotonda tutti gli spigoli vivi. Per mantenere gli spigoli un po' netti, prova a usare `Lineare` o `Bordo netto` sui primi 2 livelli di suddivisione, poi disattivali per i livelli più alti. Otterrai una mesh suddivisa semi-netta.

:::

### Mostra livello più alto {#show-highest-level}
Mostra il livello più alto con tutti i suoi dettagli mentre scolpisci un livello più basso. Comodo per vedere il risultato finale mentre fai modifiche importanti.

### Wireframe: Solo livello 0 {#wireframe-level-0-only}
Quando il [Wireframe](settings.md#wireframe) è attivo, mostra solo il wireframe del livello più basso. Il wireframe fitto dei livelli alti può nascondere la forma.


## ![](/icons/voxel.webp) Remesher voxel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Il `Remesher voxel` ricostruisce tutta la mesh con una risoluzione uniforme: tutti i poligoni hanno più o meno la stessa dimensione. È molto utile quando non vuoi pensare alla topologia e preferisci scolpire liberamente.

Un tipico flusso di lavoro può iniziare con il `Remesher voxel` per abbozzare una forma grezza a bassa risoluzione.
Ti basta premere ogni tanto il pulsante *Remesh* quando stai stirando troppo la mesh, per evitare troppa distorsione.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Come detto sopra, Nomad è un software a poligoni, ma il `Remesher voxel` è un'eccezione: per il remeshing usa (temporaneamente) un approccio diverso.

Una grande differenza è che l'approccio a voxel non accetta le autointersezioni, che quindi vengono risolte.
Inoltre non supporta le mesh con delle aperture.

Per aperture non intendiamo il `buco topologico` (il `buco` di una ciambella), ma le mesh che non sono `stagne`/`chiuse`.
In pratica, prima del remeshing tutte le aperture vengono riempite, in modo simile allo [strumento Rifila](tools.md#trim) o alla [funzione di chiusura delle aperture](#holes). L'opzione [Aperture](#voxel-holes) qui sotto sceglie come.
:::

### ![](/icons/voxel.webp) Remesh {#voxel-remesh}
Esegue il remeshing voxel. Le piccole icone sul pulsante ti ricordano quali delle opzioni qui sotto sono attive.

### Risoluzione {#voxel-resolution}
La dimensione dei voxel usati nel calcolo: valori più alti danno più dettaglio. Mentre modifichi questo parametro, sulla mesh compare una scacchiera che mostra un'anteprima del risultato.

Il contagocce prende la risoluzione dalla densità della mesh nel punto che tocchi. Il pulsante a forma di cubo accanto trasforma il valore in una `Lunghezza bordo` in unità del mondo: lo stesso valore dà allora lo stesso dettaglio su qualsiasi oggetto.

### Crea multirisoluzione {#build-multiresolution}
Crea livelli di multirisoluzione più bassi per il remeshing voxel. Se usi la scacchiera per scegliere una risoluzione e imposti `Crea multirisoluzione` a 2, il risultato finale avrà il dettaglio corrispondente al cursore della risoluzione e, nella scheda Multirisoluzione, sarà al livello 2: avrai quindi delle mesh di multirisoluzione a risoluzione più bassa ai livelli 1 e 0. È un buon modo per ottenere sia una mesh pulita con poligoni regolari, sia una mesh di controllo a risoluzione più bassa.

È anche più veloce e usa meno memoria alle alte risoluzioni. Però con una risoluzione bassa e molti livelli perderai dettagli.

::: tip Consiglio: Crea multirisoluzione e levigatura stabile

Questa opzione a volte crea dei "loop" nella geometria difficili da levigare, che producono piccoli brufoli. Se succede, attiva `Levigatura stabile` nelle opzioni dello strumento Leviga.

:::

### Ispessisci le parti sottili {#thicken-thin-parts}
Le parti più sottili dei voxel possono rompersi o sparire durante il remeshing. Questa opzione le ispessisce perché sopravvivano: valori più alti ispessiscono di più. Non è disponibile con `Bordi affilati` o `Bordo netto`.

### Aperture {#voxel-holes}
Come vengono chiuse le aperture prima del remeshing:

* `Riempi` - Ogni apertura viene chiusa da sola, a partire dal suo bordo.
* `Forma` - Le aperture vengono chiuse seguendo la superficie circostante, e i pezzi aperti che si sovrappongono vengono uniti.

### ![](/icons/angle.webp) Bordi affilati {#keep-sharp-edges}
Aggancia i nuovi punti agli spigoli vivi della mesh originale. È utile soprattutto per semplici operazioni booleane tra primitive, e può introdurre distorsioni.

### ![](/icons/group.webp) Bordo netto {#voxel-sharp-border}
Le nuove facce seguono i bordi dei gruppi di facce, e un bordo resta netto dove la superficie forma una piega lungo di esso.

### ![](/icons/group_separate.webp) Gruppi separati {#keep-groups-separate}
Ogni gruppo di facce viene ricostruito per conto suo: i gruppi non si fondono mai, e ciascuno resta un pezzo chiuso nel proprio gruppo. In questa modalità la multirisoluzione non viene creata. È disponibile quando l'oggetto ha più gruppi di facce.

## ![](/icons/dynamic.webp) Topologia dinamica {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
La multirisoluzione e il remeshing voxel sono metodi diffusi nel settore per controllare la topologia, ma entrambi ti obbligano a fare attenzione a non stirare troppo i poligoni o a non comprimerli troppo.

La topologia dinamica è un metodo alternativo. Mentre scolpisci, Nomad aggiunge e rimuove poligoni durante il tratto in modo adattivo: incidere piccoli dettagli aggiunge tanti piccoli poligoni dove servono, mentre levigare altrove ne toglie.

Nota che la topologia dinamica usa triangoli invece di quad. Il risultato può sembrare un po' disordinato, ma è quasi meglio non guardare il wireframe: concentrati su una bella scultura senza preoccuparti della topologia, poi più avanti potrai usare uno degli altri strumenti di remeshing di Nomad per ottenere una mesh pulita a quad.

Guarda il video qui sotto per vederla in azione.

![](/videos/dynamic.mp4)

### Abilitata {#enabled}
Attiva la topologia dinamica. Sotto i cursori del raggio e dell'intensità del pennello compare un'icona DynTopo, che ti permette di attivare o disattivare DynTopo strumento per strumento. Può avere un impatto notevole sulle prestazioni, e i livelli vengono aggiornati correttamente.

### Dettaglio {#dyn-detail}
Controlla la quantità di dettaglio; il suo comportamento cambia in base alla scelta in `Dettaglio basato su...`, vedi sotto. In modalità `Schermo` l'etichetta mostra la dimensione dei triangoli desiderata, in pixel. In modalità `Costante` un contagocce ti permette di prendere il dettaglio dalla densità della mesh nel punto che tocchi.

### Dettaglio basato su... {#detail-based-on}
| Metodo   | Descrizione                                                     |
| :------: | :-------------------------------------------------------------: |
| Schermo  | Il livello di dettaglio dipende da quanto è grande l'oggetto sullo schermo. Il cursore del dettaglio a 100% o più dà un dettaglio fine, con triangoli piccoli; a 1% un dettaglio basso, con triangoli grandi. |
| Raggio   | È il raggio dello strumento a definire la quantità di dettaglio: un raggio piccolo per un dettaglio fine, un raggio grande per un dettaglio basso. Il cursore del dettaglio fa da moltiplicatore su questo rapporto. |
| Costante | È il cursore del dettaglio a definire la quantità di dettaglio, indipendentemente dalla dimensione sullo schermo o da quella dello strumento. È lo stesso valore del cursore [Dettaglio](#all-detail) di `Remesh`. |

::: tip CONSIGLIO: Modalità Raggio

Per capire meglio come funziona la modalità Raggio, inizia a muovere il cursore del dettaglio con un dito e, nello stesso momento, cambia il raggio dello strumento con un altro dito. Vedrai come sono collegati.

:::

### Preferire... {#prefer}
| Metodo   | Descrizione                 |
| :------: | :-------------------------: |
| Velocità | Privilegia le prestazioni   |
| Qualità  | Privilegia la qualità       |

Quando privilegi la `Qualità`, le 2 differenze principali sono:
- la rifinitura viene applicata prima di scolpire, quindi avrai meno artefatti di interpolazione quando dipingi o scolpisci dettagli molto piccoli
- la rifinitura continua finché non raggiunge il livello di dettaglio giusto, invece di procedere per piccoli passi.

In questo modo, anche se scolpisci dettagli molto piccoli o fai tratti veloci, la topologia viene sempre rifinita come previsto.


### ![](/icons/pressure.webp) Usa la pressione sul raggio {#use-pressure-on-radius}
Serve solo se è attiva la modalità `Raggio`. Quando è attiva, il livello di dettaglio segue sempre la dimensione del pennello, anche quando questa è influenzata dalla pressione della penna.

### Usa decadimento tratto {#use-stroke-falloff}

Tiene conto anche della curva di decadimento e dell'alfa del pennello nei calcoli di DynTopo.

### Metodo {#method}
Sceglie come la topologia dinamica modifica la mesh, sia mentre scolpisci sia quando usi [Remesh](#dyn-remesh):

| Metodo           | Descrizione                                                            |
| :--------------: | :--------------------------------------------------------------------: |
| Uniformizzazione | Può aggiungere e rimuovere facce: è la modalità usata nel video sopra |
| Suddivisione     | Aggiunge solo nuove facce, non può rimuoverne                         |
| Decimazione      | Rimuove solo facce, non può aggiungerne                               |

### ![](/icons/shield.webp) Proteggi l'area mascherata {#protect-masked-area}
Le aree mascherate proteggono la topologia da qualsiasi modifica.

### ![](/icons/normal.webp) Estrapolazione dei vertici {#vertex-extrapolation}
Posiziona i punti su una superficie levigata che segue la curvatura attorno a loro, invece che in piano sulle facce esistenti.

### Dettaglio {#all-detail}
La risoluzione usata per il remeshing. Se DynTopo è in modalità `Costante`, è lo stesso valore del cursore Dettaglio in cima a questo menu. Il contagocce prende il dettaglio dalla densità della mesh nel punto che tocchi.

### Remesh {#dyn-remesh}
Esegue un remeshing globale con l'algoritmo di DynTopo. Di solito, per un remeshing completo, conviene usare il [Remesher voxel](#voxel-remesher).

Rispetto ai voxel ha però un vantaggio: la mesh non deve essere chiusa e l'area mascherata viene protetta, quindi controlli meglio dove mettere più o meno densità.

## ![](/icons/topo_extra.webp) Varie {#misc}

![](/images/topology_misc_menu.webp)

Questa scheda raccoglie gli strumenti per pulire o convertire la mesh: chiuderne le aperture, forzarla a essere manifold o trasformarla in una triplanare.

### ![](/icons/hole.webp) Aperture {#holes}
![](/images/topology_holes_menu.webp)
Nella maggior parte dei casi il tuo oggetto sarà stagno, cioè la mesh sarà "chiusa".

Se il tuo oggetto ha delle aperture, puoi riempirle.

![](/videos/hole_filling.mp4)

::: tip
Quando usi il remesher voxel, tutte le aperture vengono chiuse automaticamente, che tu lo usi su 1 o su più mesh.
:::

#### Chiudi aperture {#close-holes}
Esegue la chiusura delle aperture.

#### Opzioni {#holes-gear-menu}
Queste opzioni cambiano il modo in cui le aperture vengono riempite:

##### Gruppo di facce {#fill-face-group}
Sceglie il gruppo di facce delle nuove facce:

* `Misto` - Un'apertura circondata da un solo gruppo di facce lo riutilizza, un'apertura che tocca più gruppi ne riceve uno nuovo.
* `Nuovo` - Le aperture riempite ricevono un nuovo gruppo di facce.
* `Riutilizza` - Ogni apertura prende il gruppo di facce che la circonda di più.

##### Dettaglio {#fill-detail}
La densità di poligoni usata per riempire l'apertura. Mentre trascini questo cursore, sul modello compare una scacchiera che indica la dimensione dei triangoli da usare. La casella di spunta lo disattiva e usa solo i punti esistenti: di solito si ottengono triangoli lunghi e sottili sopra l'apertura, difficili da scolpire.

##### Ponte {#fill-non-manifold}
Riempie un'apertura e le isole al suo interno come un'unica superficie, invece di riempire ogni bordo per conto suo. Un angolo più alto collega aperture più curve. La casella di spunta lo disattiva.

### ![](/icons/cog.webp) Forza Manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Prova a ripulire gli spigoli non manifold. Può essere utile per i software esterni che non supportano spigoli condivisi da più di 2 facce.

#### Pulisci {#clean}
Esegue la pulizia.

#### Opzioni {#force-manifold-gear-menu}
Questa opzione cambia il modo in cui la mesh viene pulita:

##### Elimina piccole facce {#delete-small-faces}
Una soglia usata per rimuovere e unire i poligoni piccoli. La attivi con la sua casella di spunta.


### ![](/icons/triplanar.webp) Triplanare {#triplanar}
![](/images/topology_triplanar_menu.webp)
Converte la mesh in una primitiva [triplanare](scene.md#triplanar).
Probabilmente perderai molti dettagli nel processo: vanno persi anche i livelli, la pittura e la multirisoluzione.

#### Forza cubico {#force-cubic}
Fa sì che la triplanare sia un cubo. Altrimenti la triplanare si adatta al riquadro di delimitazione più vicino attorno all'oggetto.

#### Converti {#convert}
Esegue la conversione in triplanare.

#### Risoluzione {#triplanar-resolution}
La risoluzione della griglia della triplanare: valori più alti conservano più dettaglio.

## ![](/icons/decimate.webp) Decima {#decimation}

![](/images/topology_decimation.webp)

Riduce il numero di poligoni cercando di conservare il più possibile i dettagli, usando dei triangoli.

Questa funzione può esserti utile se vuoi esportare per la stampa 3d.
Però è meglio non usarla se vuoi continuare a scolpire sulla mesh, perché può produrre triangoli irregolari.

Nota che le aree mascherate non vengono decimate.

![](/videos/decimate.mp4)

::: tip

Usare lo [strumento Quad Remesher](tools.md#quad-remesher) su oggetti molto densi può richiedere molto tempo di calcolo e dare risultati difficili da controllare. Preparare la mesh con i [gruppi di facce](tools.md#facegroup) e la decimazione rende Quad Remesher molto più veloce e ti dà molto più controllo sulla topologia.

* Dividi la mesh in gruppi di facce per definire il flusso di quad ideale.
* Rilassa i gruppi di facce per ottenere bordi morbidi.
* Decima. Così non avrai facce sottili o distorte lungo i bordi dei gruppi di facce. In `Mantieni bordi`, assicurati che `Gruppo di facce` sia attivo: in questo modo i lati dei triangoli seguiranno esattamente i bordi dei gruppi di facce.
* Nelle opzioni di Quad Remesher assicurati che il rilassamento sia disattivato (hai già rilassato la mesh) e dovresti ottenere buoni risultati.

:::

### Decima {#decimate}
Avvia la decimazione.

Le icone accanto al pulsante `Decima` mostrano le opzioni qui sotto e ti permettono di attivarle o disattivarle. La percentuale indica quanto è forte quell'opzione.

* ![](/icons/palette.webp)  `Mantieni pittura` - Mette più triangoli dove ci sono dettagli di pittura.
* ![](/icons/triforce.webp) `Facce uniformi` - Preferisce triangoli di dimensioni regolari.
* ![](/icons/hole.webp)  `Apertura` - La decimazione cerca di lasciare invariati i bordi vicino alla geometria aperta e alle aperture.
* ![](/icons/group.webp) `Gruppo di facce` - La decimazione cerca di lasciare invariati i bordi dei gruppi di facce.
* ![](/icons/uv.webp) `UV` - La decimazione cerca di lasciare invariati i bordi delle UV.

### Triangoli target {#target-triangles}
Imposta il numero di triangoli desiderato. Il valore predefinito è 50%; il pulsante percentuale/target passa da una percentuale a un numero esatto di poligoni.

### Opzioni {#decimate-gear-menu}
Ogni opzione ha una casella di spunta per attivarla e un valore per la sua intensità:

#### ![](/icons/palette.webp) Mantieni pittura {#preserve-painting}
Il valore determina con quanta precisione vengono conservati i dettagli di pittura. Valori più alti conservano più pittura. Impostalo a 0 se la pittura non ti interessa.

#### ![](/icons/triforce.webp) Facce uniformi {#uniform-faces}
Valori più alti producono triangoli di dimensioni simili.

#### Mantieni bordi {#preserve-borders}
Impedisce che i bordi vengano decimati. Puoi impostare dei pesi per i bordi `Apertura`, `Gruppo di facce` o `UV` (`UV` richiede un oggetto con le UV).

## ![](/icons/quad.webp) Remeshing quad {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Ricostruisce l'oggetto con una disposizione pulita di quad. Questa scheda contiene diversi remesher, ognuno con il suo pulsante `Remesh`, il suo cursore `Quad target` e il suo menu ingranaggio. Provali sul tuo oggetto: danno risultati piuttosto diversi!

### Quad Remesher {#quad-remesher}
Lo stesso remesher dello strumento [Quad Remesher](tools.md#quad-remesher), sviluppato da [Exoside](https://exoside.com/). È disponibile solo su alcune piattaforme e va acquistato: finché non lo acquisti, il pulsante `Remesh` mostra un carrello.

`Seleziona strumento` passa allo strumento Quad Remesher, per disegnare le guide e dipingere la densità. Il menu ingranaggio contiene `Numero quad adattivo`, `Dimensione adattiva` (al 100% la dimensione dei quad segue la curvatura, allo 0% i quad sono uniformi), `Rileva bordi netti` e `Riproietta Vertice`.

::: tip
Dove è disponibile, Quad Remesher dà in genere i risultati migliori e il maggior controllo.
:::

### AutoRemesher {#autoremesher}
Un remesher a quad alternativo, con opzioni per adattare la dimensione e la forma dei quad alla superficie.

#### ![](/icons/cog.webp) Menu ingranaggio di AutoRemesher {#autoremesher-gear-menu}
Il menu ingranaggio contiene queste opzioni avanzate:

##### Scala bordi {#edge-scaling}
Scala la dimensione dei quad: valori più alti producono quad più grandi.

##### Adattività {#adaptivity}
Adatta la densità dei quad alla curvatura. 0 produce quad uniformi, 1 produce quad più piccoli nelle zone curve.

##### Anisotropia {#anisotropy}
Allunga i quad lungo la direzione più piatta della superficie. 0 produce quad quadrati, 1 produce quad allungati su tubi e creste.

##### Bordo netto {#sharp-edge}
Gli spigoli piegati più di questo angolo vengono conservati come spigoli vivi.

##### Smussa normali {#smooth-normal}
0 mantiene la superficie sfaccettata durante il remeshing. Valori più alti levigano la superficie tenendo conto delle normali dei vertici.

##### Riempimento massimo aperture {#autoremesher-max-fill-hole}
A volte l'algoritmo produce aperture indesiderate. Se un'apertura ha meno vertici di questo valore, viene riempita.

### Instant Mesh {#quad-remesh-instant}
Esegue il remeshing con l'[algoritmo Instant Meshes di Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analizza il flusso della mesh e crea una topologia pulita a quad.

#### Remesh {#instant-remesh}
Avvia il remeshing.

#### Quad target {#target-quads}
Il numero di quad che il remesher cercherà di creare.

#### ![](/icons/cog.webp) Menu ingranaggio di Instant Mesh {#quad-remesh-instant-gear-menu}
Il menu ingranaggio contiene queste opzioni avanzate:

##### Angolo piega {#crease-angle}
Una soglia per gli angoli vivi, che aiuta a guidare il remeshing. La attivi con la sua casella di spunta.

##### Riempimento massimo aperture {#max-fill-hole}
A volte l'algoritmo produce aperture indesiderate. Se un'apertura ha meno vertici di questo valore, viene riempita.

### QuadriFlow {#quadriflow}
Esegue il remeshing con l'algoritmo QuadriFlow, un altro modo per ottenere una disposizione pulita di quad.

#### ![](/icons/cog.webp) Menu ingranaggio di QuadriFlow {#quadriflow-gear-menu}
Il menu ingranaggio contiene queste opzioni avanzate:

##### Mantieni bordi {#quadriflow-preserve-boundary}
Protegge i bordi delle aperture.

##### Mantieni bordi netti {#keep-sharp}
Allinea i quad agli spigoli vivi della superficie.

##### Flusso a costo minimo {#min-cost-flow}
Usa un risolutore a flusso di costo minimo per la disposizione dei quad. Più lento, ma può dare una topologia più regolare.

## ![](/icons/uv.webp) Sviluppo UV {#uv-unwrap}
Calcola le coordinate di texture (UV) dell'oggetto selezionato. Nomad offre due metodi, `UVAtlas` e `BFF`, ciascuno con il suo pulsante `Sviluppa`.

![](/videos/unwrap.mp4)

::: tip UV?
Un paragone classico per le UV è incartare un regalo: qual è il modo migliore di tagliare la carta da regalo per coprire completamente un oggetto, senza sovrapposizioni?

Le UV sono simili, ma invece di tagliare la carta, tagli l'oggetto. Immagina che il tuo modello sia fatto di plastica sottile: come lo taglieresti per aprirlo e stenderlo in piano, dipingerlo così disteso e poi rimontarlo?

Ora immagina che la superficie del modello sia di lycra elastica. Potresti stirarla in piano, tagliarla, o fare un po' tutte e due le cose. Ma se dipingessi una scacchiera sull'oggetto disteso, una volta rimontato la scacchiera risulterebbe deformata. Qual è il metodo migliore: più tagli con meno distorsione, o meno tagli con più distorsione?

Le UV sono le istruzioni che dicono al software 3d come "tagliare e stirare" l'oggetto quando applica le texture. Lo strumento UVAtlas segue in genere l'approccio "più tagli, meno distorsione".


:::

::: tip Le UV, Nomad e le altre app

La maggior parte dei modelli con texture che trovi online usa le UV. Nomad può importarle e mostrarle tramite il pannello [Materiale](material.md#textures).

Quando crei modelli in Nomad, puoi dipingere direttamente sugli oggetti senza UV. Se devi esportarli verso altre app, per esempio [Procreate](https://procreate.art/), puoi trasferire (fare il bake) le informazioni di colore di Nomad in texture tramite le UV.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas preferisce in genere creare più isole con dei tagli, per ridurre al minimo la distorsione.

#### Sviluppa {#unwrap}
Calcola le UV dell'oggetto selezionato.

#### Opzioni {#uvatlas-gear-menu}
I pulsanti accanto a `Sviluppa`:

##### Gruppo di facce {#atlas-face-group}
Quando mostra `Sì`, sono i gruppi di facce a definire i tagli delle UV. Questa impostazione è condivisa con BFF.

##### Elimina le UV {#delete-uvs}
Il pulsante cestino elimina le UV dell'oggetto.

##### Ispeziona {#uv-inspect}
Mostra le UV dell'oggetto sullo sfondo.

#### Allungamento massimo {#max-stretch}
Valori bassi creano meno distorsione e più isole, valori alti creano più distorsione e meno isole.

#### Spaziatura tra isole {#island-spacing}
Lo spazio lasciato tra le isole. Valori bassi sprecano meno spazio, ma rischiano che le texture sbavino da un'isola all'altra.

::: warning
Il calcolo delle UV può richiedere un po' di tempo: meglio avere una mesh con meno di 100k vertici.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

Le UV di BFF seguono l'approccio "meno tagli, più distorsione".

#### Opzioni {#uv-bff-gear-menu}
Accanto a `Sviluppa` trovi gli stessi pulsanti `Gruppo di facce`, elimina e `Ispeziona` di [UVAtlas](#uvatlas-gear-menu).

##### Gruppo di facce {#bff-face-group}

Usa i gruppi di facce per definire i tagli delle UV.

#### Conteggio coni {#cone-count}
Definisce il numero di proiezioni principali usate. Valori più bassi producono meno isole ma più distorsione. Valori più alti richiedono più tempo di calcolo.

#### Patch senza giunture {#seamless-patches}
Influisce sulla disposizione delle patch UV, e può introdurre una distorsione importante. Funziona meglio con gruppi di facce creati con cura.

::: warning
BFF può creare UV sovrapposte se la mesh ha delle maniglie (come il buco di una ciambella).
:::

### ![](/icons/preview.webp) Mostra UV dopo lo sviluppo {#show-uv-after-unwrap}
Apre la vista di ispezione delle UV dopo lo sviluppo, così puoi controllare subito il risultato.

### ![](/icons/bake.webp) Trasferisci: Texture → Texture {#unwrap-bake-texture}
Disponibile solo quando il materiale dell'oggetto ha delle texture. Quando sviluppi di nuovo l'oggetto, le texture vengono trasferite sulle nuove UV, così continuano a combaciare. La risoluzione è `Auto` per impostazione predefinita, pari alla texture più grande, oppure puoi sceglierla tu.

## ![](/icons/bake.webp) Trasferisci {#bake}
Questa scheda trasferisce dettagli e pittura tra oggetti, e tra vertici e texture.

`Da alta risoluzione` usa altri oggetti come sorgente; il numero tra parentesi indica quanti. Nomad li sceglie così:

- vengono usati tutti gli oggetti selezionati, e l'oggetto selezionato principale è la destinazione (quello evidenziato di più nel menu [Scena](scene.md))
- se è selezionato un solo oggetto, Nomad usa invece tutti gli oggetti visibili
- se tutti gli altri oggetti sono nascosti (per esempio con Isolato), viene usata l'intera scena

### ![](/icons/bake.webp) Trasferisci → Texture {#bake-texture}
![](/images/topology_bake_menu.webp)

Il bake delle texture crea delle texture proiettando gli altri oggetti visibili della scena sulle UV dell'oggetto selezionato. L'oggetto deve avere le UV.

Ecco il tipico flusso di lavoro per il bake:
- Hai una mesh con dettagli fini e pittura
- Clonala
- Decimala (imposta `Mantieni pittura` a 0)
- Sviluppane le UV
- Fai il bake!

Ora dovresti avere una mesh a bassa risoluzione che conserva quasi tutta la pittura e i dettagli dell'oggetto di partenza.

Dopo l'operazione, i colori dei vertici vengono spostati in un nuovo livello disattivato, così non interferiscono con le texture.

#### Da sé stesso {#tex-from-itself}
Fa il bake dell'oggetto sulle sue stesse UV: la sua pittura diventa texture e, se ha dei livelli di multirisoluzione, i dettagli del livello più alto vengono trasferiti su quello corrente (in quel caso sul pulsante compare un'icona multirisoluzione). È semplice da impostare, ma spesso ti servirà più controllo: in quel caso l'opzione successiva è più utile.

#### Da alta risoluzione {#tex-from-high-res}
Fa il bake dagli altri oggetti verso l'oggetto selezionato. Il numero tra parentesi indica quanti altri oggetti verranno usati come sorgenti ad alta risoluzione e trasferiti sull'oggetto corrente a bassa risoluzione con UV. Gli altri oggetti non devono avere una disposizione o una topologia simili a quella dell'oggetto di destinazione, il che permette flussi di lavoro di bake molto versatili.

#### Risoluzione {#tex-bake-resolution}
La risoluzione della texture generata. Le texture di bake sono sempre quadrate, quindi 1024 crea un'immagine 1024x1024.

I pulsanti sotto sono scorciatoie per le risoluzioni più usate. Come riferimento, 512x512 è piuttosto piccola, adatta per esempio alla grafica web e alla geometria semplice. 4096x4096 (4k in breve) è per render di alta qualità.

#### Colore, Rugosità, Metallicità, Normale, Spostamento, Emissivo, Opacità {#tex-normal-roughness-metalness-color-emissive-opacity}
Questi pulsanti stabiliscono quali proprietà vengono trasferite, ciascuna in una mappa separata. Al termine del bake, le mappe vengono aggiunte come texture al materiale dell'oggetto corrente. `Spostamento` trasferisce l'altezza dei dettagli in una mappa di displacement.

#### ![](/icons/cog.webp) Menu ingranaggio di Trasferisci {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Il menu ingranaggio contiene queste opzioni avanzate:

##### Backup {#tex-backup}
Per vedere l'anteprima delle texture generate, le informazioni di pittura dell'oggetto vanno disattivate. `Backup (Pittura → Livello)` sposta tutta la pittura in un nuovo livello di backup, così puoi attivarla o disattivarla facilmente.

##### Usa multirisoluzione {#tex-use-multires}
Per `Da sé stesso` su un oggetto con livelli di multirisoluzione. Nomad legge l'alta risoluzione attraverso i livelli di suddivisione invece di lanciare raggi: è più veloce e senza errori di proiezione. Disattivalo per fare il bake con le opzioni qui sotto.

##### Base levigata {#tex-smooth-base}
Per `Spostamento` su un oggetto con livelli di multirisoluzione. Misura lo spostamento rispetto alla base suddivisa invece che rispetto alle sue facce piatte. Tienilo attivo quando la mappa di displacement andrà su una mesh suddivisa, come con la suddivisione adattiva di Blender.

##### Cerca la distanza {#tex-cage-radius}
La distanza massima entro cui cercare la superficie sorgente. Per impostazione predefinita è tenuta bassa per evitare artefatti, ma puoi aumentarla se gli oggetti sorgente sono lontani dall'oggetto di destinazione.

##### Proiezione {#tex-projection}
Come viene trovata la superficie sorgente:

* `Raggio` - Proietta lungo la normale della superficie.
* `Raggio + più vicino` - Usa il raggio lungo la normale, poi la superficie più vicina se il raggio non colpisce nulla.
* `Più vicino` - Proietta sul punto più vicino della superficie sorgente.

##### Offset del raggio {#tex-ray-offset}
Regola il punto di partenza dei calcoli di bake sull'oggetto di destinazione. Un piccolo scostamento dalla superficie evita gli artefatti più comuni. Se gli oggetti sorgente sono molto lontani dall'oggetto di destinazione, potrebbe essere necessario aumentarlo. Non viene usato da `Più vicino`.


### ![](/icons/bake.webp) Riproietta → Vertice {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Proietta dettagli scolpiti, pittura, livelli e texture nei valori dei vertici.

Puoi vederlo come l'inverso del bake: se il bake trasferisce le proprietà dei vertici nelle texture, la riproiezione trasferisce le texture (e altre proprietà)
 di nuovo nei vertici.

::: tip
Quando usi `Trasferisci → Texture` o `Riproietta → Vertice`, vengono presi in considerazione sia i colori dei vertici sia le texture del materiale.
:::

#### Da sé stesso {#vertex-from-itself}
Converte le texture del materiale in valori dei vertici. Questo pulsante è attivo solo se l'oggetto ha le UV e se le texture sono attive nel materiale.

::: tip CONSIGLIO: Dipingere le texture
Nomad non permette di dipingere e modificare direttamente le texture, ma puoi ottenere risultati molto simili proiettando le texture nei valori dei vertici, dipingendo sui vertici e poi facendo il bake dai vertici alle texture:

1. Prepara un oggetto low poly con le UV
1. Carica le texture nel suo materiale
1. Suddividilo abbastanza da poterci dipingere sopra
1. `Riproietta → Vertice` in modalità `Da sé stesso`: ora la texture è stata convertita in valori dei vertici
1. Dipingi, leviga, sfuma, timbra, fai tutte le modifiche che ti servono
1. `Trasferisci → Texture` in modalità `Da sé stesso`: le modifiche vengono riconvertite in texture.
:::

#### Da alta risoluzione {#vertex-from-high-res}
Converte gli altri oggetti in valori dei vertici sull'oggetto selezionato. Il numero su questo pulsante indica il numero di oggetti sorgente. È pensato soprattutto per essere usato anche su una mesh ad alta risoluzione, di solito con una topologia pulita.

::: tip
La riproiezione da altri oggetti non serve solo a trasferirne le informazioni di colore, ma anche a proiettare i vertici su altri oggetti: per esempio puoi proiettare delle bende su un personaggio.
:::

#### Vertici, Colore, Rugosità, Metallicità, Opacità, Maschera, Livelli, Gruppo di facce {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Questi pulsanti stabiliscono quali proprietà vengono proiettate sull'oggetto selezionato. `Livelli` trasferisce gli altri livelli sulla mesh selezionata.

#### ![](/icons/cog.webp) Menu ingranaggio di Riproietta {#vertex-reproject-gear-menu}
Il menu ingranaggio contiene queste opzioni avanzate:

##### Opacità → Maschera {#vertex-opacity-to-mask}
Trasforma l'opacità della sorgente in maschera sull'oggetto selezionato.

##### Iterazioni {#vertex-iterations}
Quante volte applicare il rilassamento durante la riproiezione. Usato solo quando `Vertici` è attivo.

##### Rilassa {#vertex-relax}
La disposizione della mesh selezionata può essere levigata o rilassata un po' per adattarsi meglio agli oggetti sorgente. `Leviga` è più adatto alle mesh dense, `Rilassa` a quelle low poly. `Auto` lascia scegliere a Nomad il metodo migliore.

##### Cerca la distanza {#vertex-cage-radius}
La distanza massima entro cui cercare la superficie sorgente. Per impostazione predefinita è tenuta bassa per evitare artefatti, ma puoi aumentarla se gli oggetti sorgente sono lontani dall'oggetto selezionato.

##### Proiezione {#vertex-projection}
Come viene trovata la superficie sorgente:

* `Raggio` - Proietta lungo la normale della superficie.
* `Miscela adattiva` - Miscela il raggio lungo la normale e la superficie più vicina in base alla distanza e a `Preferenza raggio`. Se uno dei due non colpisce nulla, usa l'altro.
* `Più vicino` - Proietta sul punto più vicino della superficie sorgente.

##### Preferenza raggio {#vertex-ray-bias}
Solo per `Miscela adattiva`. Valori più alti spostano la miscela verso il risultato del raggio lungo la normale, valori più bassi verso il punto più vicino.

##### Offset del raggio {#ray-vertex-offset}
Regola il punto di partenza dei calcoli sull'oggetto selezionato. Un piccolo scostamento dalla superficie evita alcuni artefatti. Se gli oggetti sorgente sono molto lontani dall'oggetto di destinazione, potrebbe essere necessario aumentarlo. Non viene usato da `Più vicino`.

### ![](/icons/bake.webp) Trasferisci → VDM {#bake-vdm}
Crea un timbro VDM (vector displacement) dall'oggetto selezionato e lo aggiunge alla libreria VDM. Ti verrà chiesto un nome.

Ecco il tipico flusso di lavoro:
- Aggiungi un piano, oppure scegli `Nuovo VDM` nel selettore VDM per aggiungerne uno già configurato (la primitiva [VDM](scene.md#add-menu))
- Scolpisci la tua forma sul piano, tenendo il bordo piatto
- Fai il bake!

Sono le UV del piano a definire il quadrato trasferito, quindi l'oggetto deve avere le UV. Scegli la dimensione del timbro con `Risoluzione`, e decidi con `Colore`, `Rugosità`, `Metallicità` e `Opacità` cosa porta il timbro oltre allo spostamento.

::: tip
Evita DynTopo sul piano: ne rovina le UV e il timbro viene fuori distorto. Scolpire in un livello dà il risultato più preciso, perché il piano piatto resta lì sotto. Anche la pittura richiede un livello, altrimenti il materiale viene timbrato su tutto il quadrato invece che solo dove hai dipinto.
:::

## ![](/icons/dot.webp) Primitiva {#primitive}
I parametri della primitiva selezionata. Quasi tutti sono disponibili anche dal pulsante `…` della barra degli strumenti della primitiva nel viewport.

![](/images/topology_primitive_screenshot.webp)
